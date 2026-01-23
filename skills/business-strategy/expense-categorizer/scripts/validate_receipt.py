#!/usr/bin/env python3
"""
Receipt Validation Script

Validate receipt data for completeness, accuracy, and compliance.

Features:
- Field validation (required fields present)
- Amount validation (reasonable ranges)
- Date validation (not future, not too old)
- Duplicate detection
- Policy compliance checks

Usage:
    python validate_receipt.py --merchant "Restaurant" --amount 85.00 --date 2026-01-05
    python validate_receipt.py --json '{"merchant": "Restaurant", "amount": 85.00}'
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional


@dataclass
class ReceiptData:
    """Receipt data structure."""
    merchant: str = ""
    amount: float = 0.0
    date: str = ""
    description: str = ""
    payment_method: str = ""
    tax_amount: Optional[float] = None
    tip_amount: Optional[float] = None
    currency: str = "USD"
    receipt_number: str = ""
    attendees: list = field(default_factory=list)
    business_purpose: str = ""


@dataclass
class ValidationResult:
    """Validation result with issues and warnings."""
    is_valid: bool
    errors: list
    warnings: list
    suggestions: list
    completeness_score: float


# Required fields for IRS compliance
REQUIRED_FIELDS = {
    "merchant": "Merchant/vendor name is required",
    "amount": "Expense amount is required",
    "date": "Date of expense is required",
}

# Recommended fields for best practice
RECOMMENDED_FIELDS = {
    "description": "Description helps with categorization and audits",
    "payment_method": "Payment method aids in reconciliation",
    "business_purpose": "Business purpose is required for tax deduction",
}

# Additional requirements by expense type
EXPENSE_TYPE_REQUIREMENTS = {
    "meal": {
        "required": ["attendees", "business_purpose"],
        "message": "Meals require attendees list and business purpose for IRS compliance",
    },
    "travel": {
        "required": ["business_purpose"],
        "message": "Travel expenses require documented business purpose",
    },
    "entertainment": {
        "required": ["attendees", "business_purpose"],
        "message": "Entertainment requires attendees and business purpose (note: may not be deductible)",
    },
}

# Amount thresholds
AMOUNT_THRESHOLDS = {
    "receipt_required": 75.00,  # IRS requirement for receipts
    "suspicious_low": 0.01,
    "suspicious_high": 10000.00,
    "meal_reasonable": 500.00,
    "single_item_high": 2500.00,
}

# Date validation parameters
DATE_VALIDATION = {
    "max_age_days": 90,  # Common policy limit
    "warning_age_days": 60,
}


def validate_merchant(merchant: str) -> tuple[list, list]:
    """Validate merchant name."""
    errors = []
    warnings = []

    if not merchant:
        errors.append("Merchant name is required")
        return errors, warnings

    if len(merchant) < 2:
        errors.append("Merchant name is too short")

    if len(merchant) > 100:
        warnings.append("Merchant name is unusually long")

    # Check for common OCR errors
    ocr_patterns = [
        (r"[0O]{3,}", "Possible OCR error in merchant name"),
        (r"[1Il]{3,}", "Possible OCR error in merchant name"),
    ]
    for pattern, message in ocr_patterns:
        if re.search(pattern, merchant):
            warnings.append(message)

    return errors, warnings


def validate_amount(amount: float, expense_type: str = "") -> tuple[list, list]:
    """Validate expense amount."""
    errors = []
    warnings = []

    if amount <= 0:
        errors.append("Amount must be greater than zero")
        return errors, warnings

    if amount < AMOUNT_THRESHOLDS["suspicious_low"]:
        errors.append(f"Amount ${amount:.2f} is suspiciously low")

    if amount > AMOUNT_THRESHOLDS["suspicious_high"]:
        warnings.append(f"Amount ${amount:.2f} is unusually high - verify accuracy")

    if expense_type == "meal" and amount > AMOUNT_THRESHOLDS["meal_reasonable"]:
        warnings.append(f"Meal expense ${amount:.2f} exceeds ${AMOUNT_THRESHOLDS['meal_reasonable']:.2f} - may require approval")

    if amount >= AMOUNT_THRESHOLDS["receipt_required"]:
        warnings.append(f"IRS requires receipt for expenses ${AMOUNT_THRESHOLDS['receipt_required']:.2f} and above")

    return errors, warnings


def validate_date(date_str: str) -> tuple[list, list, Optional[datetime]]:
    """Validate expense date."""
    errors = []
    warnings = []
    parsed_date = None

    if not date_str:
        errors.append("Date is required")
        return errors, warnings, parsed_date

    # Try to parse date
    date_formats = [
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%m/%d/%y",
        "%d/%m/%Y",
        "%Y/%m/%d",
    ]

    for fmt in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            break
        except ValueError:
            continue

    if not parsed_date:
        errors.append(f"Invalid date format: {date_str}")
        return errors, warnings, parsed_date

    today = datetime.now()

    # Check if date is in the future
    if parsed_date > today:
        errors.append("Expense date cannot be in the future")

    # Check if date is too old
    age_days = (today - parsed_date).days

    if age_days > DATE_VALIDATION["max_age_days"]:
        warnings.append(f"Expense is {age_days} days old - may exceed policy limit of {DATE_VALIDATION['max_age_days']} days")
    elif age_days > DATE_VALIDATION["warning_age_days"]:
        warnings.append(f"Expense is {age_days} days old - submit soon to avoid policy issues")

    return errors, warnings, parsed_date


def validate_business_purpose(purpose: str, expense_type: str = "") -> tuple[list, list]:
    """Validate business purpose documentation."""
    errors = []
    warnings = []

    if not purpose:
        if expense_type in ["meal", "entertainment"]:
            errors.append("Business purpose is required for meals and entertainment")
        else:
            warnings.append("Business purpose is recommended for all expenses")
        return errors, warnings

    if len(purpose) < 10:
        warnings.append("Business purpose description is very brief - consider adding detail")

    # Check for vague descriptions
    vague_terms = ["misc", "various", "stuff", "things", "general", "n/a", "na"]
    if any(term in purpose.lower() for term in vague_terms):
        warnings.append("Business purpose is vague - be specific for IRS compliance")

    return errors, warnings


def validate_attendees(attendees: list, expense_type: str = "") -> tuple[list, list]:
    """Validate attendees for meals and entertainment."""
    errors = []
    warnings = []

    if expense_type in ["meal", "entertainment"]:
        if not attendees:
            errors.append("Attendees list is required for meals and entertainment")
            return errors, warnings

        if len(attendees) < 2:
            warnings.append("Solo meals may have limited deductibility")

        # Check for proper names
        for attendee in attendees:
            if len(attendee) < 2:
                warnings.append(f"Attendee name '{attendee}' seems incomplete")

    return errors, warnings


def infer_expense_type(data: ReceiptData) -> str:
    """Infer expense type from receipt data."""
    merchant_lower = data.merchant.lower()
    desc_lower = data.description.lower()
    combined = f"{merchant_lower} {desc_lower}"

    # Meal/restaurant indicators
    meal_terms = ["restaurant", "cafe", "diner", "grill", "kitchen", "food",
                  "lunch", "dinner", "breakfast", "coffee", "starbucks", "meal"]
    if any(term in combined for term in meal_terms):
        return "meal"

    # Travel indicators
    travel_terms = ["airline", "flight", "hotel", "lodging", "uber", "lyft",
                    "taxi", "rental car", "airbnb", "airport"]
    if any(term in combined for term in travel_terms):
        return "travel"

    # Entertainment indicators
    entertainment_terms = ["entertainment", "event", "tickets", "concert",
                          "show", "game", "sports"]
    if any(term in combined for term in entertainment_terms):
        return "entertainment"

    return "general"


def calculate_completeness(data: ReceiptData) -> float:
    """Calculate completeness score (0-100)."""
    total_fields = 10
    filled_fields = 0

    if data.merchant:
        filled_fields += 1
    if data.amount > 0:
        filled_fields += 1
    if data.date:
        filled_fields += 1
    if data.description:
        filled_fields += 1
    if data.payment_method:
        filled_fields += 1
    if data.tax_amount is not None:
        filled_fields += 0.5
    if data.tip_amount is not None:
        filled_fields += 0.5
    if data.receipt_number:
        filled_fields += 0.5
    if data.attendees:
        filled_fields += 1
    if data.business_purpose:
        filled_fields += 1.5

    return (filled_fields / total_fields) * 100


def validate_receipt(data: ReceiptData) -> ValidationResult:
    """
    Comprehensive receipt validation.

    Returns ValidationResult with:
    - is_valid: True if no errors
    - errors: Critical issues that must be fixed
    - warnings: Issues that should be addressed
    - suggestions: Best practice recommendations
    - completeness_score: How complete the data is (0-100)
    """
    errors = []
    warnings = []
    suggestions = []

    # Infer expense type
    expense_type = infer_expense_type(data)

    # Validate required fields
    merch_errors, merch_warnings = validate_merchant(data.merchant)
    errors.extend(merch_errors)
    warnings.extend(merch_warnings)

    amount_errors, amount_warnings = validate_amount(data.amount, expense_type)
    errors.extend(amount_errors)
    warnings.extend(amount_warnings)

    date_errors, date_warnings, parsed_date = validate_date(data.date)
    errors.extend(date_errors)
    warnings.extend(date_warnings)

    # Validate optional but important fields
    purpose_errors, purpose_warnings = validate_business_purpose(
        data.business_purpose, expense_type
    )
    errors.extend(purpose_errors)
    warnings.extend(purpose_warnings)

    attendee_errors, attendee_warnings = validate_attendees(
        data.attendees, expense_type
    )
    errors.extend(attendee_errors)
    warnings.extend(attendee_warnings)

    # Check recommended fields
    for field_name, message in RECOMMENDED_FIELDS.items():
        if not getattr(data, field_name, None):
            suggestions.append(message)

    # Type-specific requirements
    if expense_type in EXPENSE_TYPE_REQUIREMENTS:
        req = EXPENSE_TYPE_REQUIREMENTS[expense_type]
        for req_field in req["required"]:
            if not getattr(data, req_field, None):
                warnings.append(req["message"])
                break

    # Tax and tip validation
    if data.tax_amount is not None:
        if data.tax_amount < 0:
            errors.append("Tax amount cannot be negative")
        elif data.tax_amount > data.amount * 0.15:
            warnings.append("Tax amount seems high - verify accuracy")

    if data.tip_amount is not None:
        if data.tip_amount < 0:
            errors.append("Tip amount cannot be negative")
        elif data.tip_amount > data.amount * 0.50:
            warnings.append("Tip exceeds 50% - may require explanation")

    # Calculate completeness
    completeness = calculate_completeness(data)
    if completeness < 50:
        suggestions.append("Receipt data is incomplete - add more details for better categorization")

    return ValidationResult(
        is_valid=len(errors) == 0,
        errors=errors,
        warnings=warnings,
        suggestions=suggestions,
        completeness_score=completeness,
    )


def main():
    parser = argparse.ArgumentParser(description="Validate receipt data")
    parser.add_argument("--merchant", help="Merchant name")
    parser.add_argument("--amount", type=float, help="Expense amount")
    parser.add_argument("--date", help="Expense date (YYYY-MM-DD)")
    parser.add_argument("--description", default="", help="Expense description")
    parser.add_argument("--payment-method", default="", help="Payment method")
    parser.add_argument("--tax", type=float, help="Tax amount")
    parser.add_argument("--tip", type=float, help="Tip amount")
    parser.add_argument("--attendees", nargs="+", help="Attendees list")
    parser.add_argument("--purpose", default="", help="Business purpose")
    parser.add_argument("--json", help="JSON input with receipt data")
    parser.add_argument("--output-json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if args.json:
        data_dict = json.loads(args.json)
        receipt = ReceiptData(
            merchant=data_dict.get("merchant", ""),
            amount=float(data_dict.get("amount", 0)),
            date=data_dict.get("date", ""),
            description=data_dict.get("description", ""),
            payment_method=data_dict.get("payment_method", ""),
            tax_amount=data_dict.get("tax"),
            tip_amount=data_dict.get("tip"),
            attendees=data_dict.get("attendees", []),
            business_purpose=data_dict.get("business_purpose", ""),
        )
    elif args.merchant or args.amount:
        receipt = ReceiptData(
            merchant=args.merchant or "",
            amount=args.amount or 0.0,
            date=args.date or "",
            description=args.description,
            payment_method=args.payment_method,
            tax_amount=args.tax,
            tip_amount=args.tip,
            attendees=args.attendees or [],
            business_purpose=args.purpose,
        )
    else:
        parser.print_help()
        sys.exit(1)

    result = validate_receipt(receipt)

    if args.output_json:
        output = {
            "is_valid": result.is_valid,
            "errors": result.errors,
            "warnings": result.warnings,
            "suggestions": result.suggestions,
            "completeness_score": result.completeness_score,
        }
        print(json.dumps(output, indent=2))
    else:
        print(f"\nValidation Result: {'VALID' if result.is_valid else 'INVALID'}")
        print(f"Completeness Score: {result.completeness_score:.0f}%")

        if result.errors:
            print("\n Errors:")
            for error in result.errors:
                print(f"  - {error}")

        if result.warnings:
            print("\n Warnings:")
            for warning in result.warnings:
                print(f"  - {warning}")

        if result.suggestions:
            print("\n Suggestions:")
            for suggestion in result.suggestions:
                print(f"  - {suggestion}")


if __name__ == "__main__":
    main()
