#!/usr/bin/env python3
"""
Expense Categorization Script

Automatically categorize business expenses based on:
1. Merchant Category Code (MCC)
2. Merchant name matching
3. Amount patterns
4. Keyword analysis

Usage:
    python categorize.py --merchant "Starbucks" --amount 45.00 --description "Coffee with client"
    python categorize.py --file expenses.csv --output categorized.csv
"""

import argparse
import csv
import json
import re
import sys
from dataclasses import dataclass, asdict
from typing import Optional
from pathlib import Path


@dataclass
class Expense:
    """Expense data structure."""
    date: str
    merchant: str
    amount: float
    description: str = ""
    mcc: Optional[str] = None
    payment_method: str = ""


@dataclass
class CategorizedExpense:
    """Categorized expense with tax and policy info."""
    date: str
    merchant: str
    amount: float
    description: str
    category: str
    subcategory: str
    gl_code: str
    tax_rate: float
    deductible_amount: float
    policy_status: str
    flags: list
    confidence: float


# Merchant Category Code (MCC) mappings
MCC_CATEGORIES = {
    # Airlines
    "3000-3350": ("Travel", "Airfare", "6100-01", 1.0),
    "4511": ("Travel", "Airfare", "6100-01", 1.0),

    # Lodging
    "3501-3999": ("Travel", "Lodging", "6100-02", 1.0),
    "7011": ("Travel", "Lodging", "6100-02", 1.0),

    # Car Rental
    "3351-3500": ("Travel", "Car Rental", "6100-03", 1.0),
    "7512": ("Travel", "Car Rental", "6100-03", 1.0),

    # Ground Transportation
    "4121": ("Travel", "Ground Transport", "6100-03", 1.0),  # Taxi
    "4789": ("Travel", "Ground Transport", "6100-03", 1.0),  # Transportation services

    # Restaurants
    "5812": ("Meals", "Restaurant", "6200-01", 0.5),
    "5813": ("Meals", "Bar/Lounge", "6200-01", 0.5),
    "5814": ("Meals", "Fast Food", "6200-01", 0.5),

    # Office Supplies
    "5111": ("Office", "Stationery", "6300-01", 1.0),
    "5943": ("Office", "Supplies", "6300-01", 1.0),
    "5044": ("Office", "Equipment", "6300-04", 1.0),

    # Technology
    "5045": ("Technology", "Hardware", "6400-02", 1.0),
    "5734": ("Technology", "Software", "6400-01", 1.0),
    "7372": ("Technology", "Software", "6400-01", 1.0),

    # Professional Services
    "8111": ("Professional", "Legal", "6500-01", 1.0),
    "8931": ("Professional", "Accounting", "6500-02", 1.0),
    "7392": ("Professional", "Consulting", "6500-03", 1.0),

    # Education
    "8220": ("Training", "Education", "6700-01", 1.0),
    "8299": ("Training", "Education", "6700-01", 1.0),
    "5942": ("Training", "Books", "6700-02", 1.0),
}


# Merchant name patterns for categorization
MERCHANT_PATTERNS = {
    # Airlines
    r"(united|delta|american|southwest|jetblue|alaska|frontier|spirit)\s*(air)?":
        ("Travel", "Airfare", "6100-01", 1.0),

    # Hotels
    r"(marriott|hilton|hyatt|ihg|wyndham|best western|holiday inn|hampton|courtyard)":
        ("Travel", "Lodging", "6100-02", 1.0),
    r"(airbnb|vrbo)":
        ("Travel", "Lodging", "6100-02", 1.0),

    # Rideshare
    r"(uber|lyft)\s*(trip)?":
        ("Travel", "Ground Transport", "6100-03", 1.0),

    # Coffee shops (treat as meals)
    r"(starbucks|dunkin|peet|blue bottle|philz)":
        ("Meals", "Coffee/Snacks", "6200-02", 0.5),

    # Restaurants
    r"(restaurant|cafe|bistro|grill|kitchen|eatery|diner)":
        ("Meals", "Restaurant", "6200-01", 0.5),

    # Fast food
    r"(mcdonald|burger king|wendy|chick-?fil-?a|chipotle|subway|taco bell|panera)":
        ("Meals", "Fast Food", "6200-02", 0.5),

    # Office supplies
    r"(staples|office depot|officemax|amazon.*supplies)":
        ("Office", "Supplies", "6300-01", 1.0),

    # Technology
    r"(apple|microsoft|google|adobe|zoom|slack|dropbox|github|aws|azure)":
        ("Technology", "Software/Services", "6400-01", 1.0),
    r"(best buy|b&h photo|newegg)":
        ("Technology", "Hardware", "6400-02", 1.0),

    # Shipping
    r"(ups|fedex|usps|dhl)":
        ("Office", "Shipping", "6300-02", 1.0),

    # Parking
    r"(parking|spothero|parkwhiz)":
        ("Travel", "Parking", "6100-03", 1.0),

    # Gas stations
    r"(shell|chevron|exxon|mobil|bp|texaco|76|arco|costco gas)":
        ("Travel", "Fuel", "6100-05", 1.0),

    # Conferences
    r"(eventbrite|conference|summit|expo)":
        ("Training", "Conferences", "6700-01", 1.0),
}


# Keywords for description-based categorization
DESCRIPTION_KEYWORDS = {
    # Client-related
    r"(client|customer|prospect|meeting with)":
        {"category_modifier": "Client", "tax_rate": 0.5},

    # Team-related
    r"(team|employee|staff|all-hands|offsite)":
        {"category_modifier": "Team", "tax_rate": 0.5},

    # Travel indicators
    r"(flight|airfare|plane|boarding)":
        {"force_category": ("Travel", "Airfare", "6100-01", 1.0)},
    r"(hotel|lodging|accommodation|stay)":
        {"force_category": ("Travel", "Lodging", "6100-02", 1.0)},
}


# Policy limits (example - customize per organization)
POLICY_LIMITS = {
    "Meals.solo": 50.00,
    "Meals.group_per_person": 75.00,
    "Meals.Client": 150.00,
    "Travel.Lodging": 300.00,
    "Travel.Airfare.domestic": 800.00,
    "Travel.Airfare.international": 2500.00,
    "Office.single_item": 500.00,
    "Technology.Hardware": 2500.00,
}


def categorize_by_mcc(mcc: str) -> Optional[tuple]:
    """Categorize expense by Merchant Category Code."""
    if not mcc:
        return None

    # Check exact match
    if mcc in MCC_CATEGORIES:
        return MCC_CATEGORIES[mcc]

    # Check range matches
    for mcc_range, category_info in MCC_CATEGORIES.items():
        if "-" in mcc_range:
            start, end = mcc_range.split("-")
            if start <= mcc <= end:
                return category_info

    return None


def categorize_by_merchant(merchant: str) -> Optional[tuple]:
    """Categorize expense by merchant name pattern matching."""
    merchant_lower = merchant.lower()

    for pattern, category_info in MERCHANT_PATTERNS.items():
        if re.search(pattern, merchant_lower, re.IGNORECASE):
            return category_info

    return None


def analyze_description(description: str) -> dict:
    """Analyze description for additional context."""
    modifiers = {}
    description_lower = description.lower()

    for pattern, info in DESCRIPTION_KEYWORDS.items():
        if re.search(pattern, description_lower, re.IGNORECASE):
            modifiers.update(info)

    return modifiers


def check_policy_compliance(expense: CategorizedExpense) -> tuple[str, list]:
    """Check expense against policy limits."""
    flags = []
    status = "Compliant"

    # Build policy key
    policy_key = f"{expense.category}.{expense.subcategory}"

    # Check if there's a limit for this category
    if policy_key in POLICY_LIMITS:
        limit = POLICY_LIMITS[policy_key]
        if expense.amount > limit:
            flags.append(f"Exceeds {policy_key} limit of ${limit:.2f}")
            status = "Requires Approval"

    # Check category-level limits
    category_key = expense.category
    if category_key in POLICY_LIMITS:
        limit = POLICY_LIMITS[category_key]
        if expense.amount > limit:
            flags.append(f"Exceeds {category_key} limit of ${limit:.2f}")
            status = "Requires Approval"

    # Additional policy checks
    if expense.amount > 500 and not expense.description:
        flags.append("Missing description for expense over $500")
        status = "Requires Approval"

    return status, flags


def categorize_expense(expense: Expense) -> CategorizedExpense:
    """
    Categorize an expense using multiple signals.

    Priority:
    1. MCC code (most reliable)
    2. Merchant name matching
    3. Description keywords
    4. Amount-based heuristics
    """
    category_info = None
    confidence = 0.0

    # Try MCC first (highest confidence)
    if expense.mcc:
        category_info = categorize_by_mcc(expense.mcc)
        if category_info:
            confidence = 0.95

    # Try merchant name matching
    if not category_info:
        category_info = categorize_by_merchant(expense.merchant)
        if category_info:
            confidence = 0.85

    # Analyze description for modifiers
    desc_modifiers = analyze_description(expense.description)

    # Apply forced category from description if found
    if "force_category" in desc_modifiers:
        category_info = desc_modifiers["force_category"]
        confidence = 0.80

    # Default category if nothing matched
    if not category_info:
        category_info = ("Uncategorized", "Other", "6900-00", 1.0)
        confidence = 0.50

    category, subcategory, gl_code, tax_rate = category_info

    # Apply modifiers from description
    if "category_modifier" in desc_modifiers:
        subcategory = f"{desc_modifiers['category_modifier']} {subcategory}"
    if "tax_rate" in desc_modifiers:
        tax_rate = desc_modifiers["tax_rate"]

    # Calculate deductible amount
    deductible_amount = expense.amount * tax_rate

    # Create categorized expense
    categorized = CategorizedExpense(
        date=expense.date,
        merchant=expense.merchant,
        amount=expense.amount,
        description=expense.description,
        category=category,
        subcategory=subcategory,
        gl_code=gl_code,
        tax_rate=tax_rate,
        deductible_amount=deductible_amount,
        policy_status="Pending",
        flags=[],
        confidence=confidence,
    )

    # Check policy compliance
    status, flags = check_policy_compliance(categorized)
    categorized.policy_status = status
    categorized.flags = flags

    return categorized


def process_csv(input_file: Path, output_file: Path) -> None:
    """Process a CSV file of expenses."""
    expenses = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            expense = Expense(
                date=row.get("date", ""),
                merchant=row.get("merchant", ""),
                amount=float(row.get("amount", 0)),
                description=row.get("description", ""),
                mcc=row.get("mcc"),
                payment_method=row.get("payment_method", ""),
            )
            expenses.append(expense)

    categorized = [categorize_expense(e) for e in expenses]

    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=asdict(categorized[0]).keys())
        writer.writeheader()
        for exp in categorized:
            writer.writerow(asdict(exp))

    print(f"Processed {len(categorized)} expenses to {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Categorize business expenses")
    parser.add_argument("--merchant", help="Merchant name")
    parser.add_argument("--amount", type=float, help="Expense amount")
    parser.add_argument("--description", default="", help="Expense description")
    parser.add_argument("--date", default="", help="Expense date")
    parser.add_argument("--mcc", help="Merchant Category Code")
    parser.add_argument("--file", type=Path, help="CSV file to process")
    parser.add_argument("--output", type=Path, help="Output CSV file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.file:
        if not args.output:
            args.output = args.file.with_stem(f"{args.file.stem}_categorized")
        process_csv(args.file, args.output)
    elif args.merchant and args.amount:
        expense = Expense(
            date=args.date or "2026-01-01",
            merchant=args.merchant,
            amount=args.amount,
            description=args.description,
            mcc=args.mcc,
        )
        result = categorize_expense(expense)

        if args.json:
            print(json.dumps(asdict(result), indent=2))
        else:
            print(f"\nCategorization Result:")
            print(f"  Category: {result.category}")
            print(f"  Subcategory: {result.subcategory}")
            print(f"  GL Code: {result.gl_code}")
            print(f"  Tax Rate: {result.tax_rate * 100:.0f}%")
            print(f"  Deductible: ${result.deductible_amount:.2f}")
            print(f"  Policy Status: {result.policy_status}")
            if result.flags:
                print(f"  Flags: {', '.join(result.flags)}")
            print(f"  Confidence: {result.confidence * 100:.0f}%")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
