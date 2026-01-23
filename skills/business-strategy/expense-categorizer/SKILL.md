---
name: expense-categorizer
description: Categorize business expenses with proper tax treatment and policy compliance. Use when processing receipts, categorizing expenses, preparing expense reports, checking tax deductibility, or identifying policy violations.
---

# Expense Categorizer

Categorize expenses accurately for accounting, tax, and policy compliance.

## Quick Start

**Categorize a Single Expense:**

```markdown
# Expense Categorization

**Description:** Dinner with client at Restaurant XYZ
**Amount:** $185.00
**Date:** 2026-01-05
**Merchant:** Restaurant XYZ

## Categorization

| Field | Value |
|-------|-------|
| Category | Meals & Entertainment |
| Subcategory | Client Meals |
| GL Code | 6200-01 |
| Tax Treatment | 50% deductible |
| Policy Status | Compliant |
| Notes | Business purpose documented |
```

## Core Workflow

### Phase 1: Receipt/Expense Input

Gather expense information:

```markdown
# Expense Details

## Required Fields
- **Amount:** $[X.XX]
- **Date:** [YYYY-MM-DD]
- **Merchant:** [Business name]
- **Payment Method:** [Card ending/Cash/etc.]

## Recommended Fields
- **Description:** [What was purchased]
- **Business Purpose:** [Why expense was incurred]
- **Attendees:** [If meal/entertainment]
- **Project/Client:** [If applicable]

## Receipt Image
[Attach or reference receipt image]
```

### Phase 2: Category Assignment

Use the decision tree:

```
1. Is it travel-related?
   ├── Yes → Is it transportation?
   │         ├── Airfare → Travel: Airfare
   │         ├── Ground transport → Travel: Ground Transport
   │         └── Mileage → Travel: Mileage Reimbursement
   │
   │         Is it lodging?
   │         └── Yes → Travel: Lodging
   │
   │         Is it a meal during travel?
   │         └── Yes → Travel: Meals
   │
   └── No → Continue to step 2

2. Is it a meal or entertainment?
   ├── Client/prospect present → Meals: Client Entertainment
   ├── Team meal (no clients) → Meals: Team Meals
   ├── Solo meal (travel) → Travel: Meals
   └── Solo meal (local) → May not be deductible

3. Is it office/supplies?
   ├── Office supplies → Office: Supplies
   ├── Software/subscriptions → Technology: Software
   ├── Hardware/equipment → Technology: Equipment
   └── Furniture → Office: Furniture & Equipment

4. Is it professional services?
   ├── Legal → Professional Services: Legal
   ├── Accounting → Professional Services: Accounting
   ├── Consulting → Professional Services: Consulting
   └── Other → Professional Services: Other

5. Other categories...
   [See references/category-taxonomy.md for full list]
```

### Phase 3: Tax Treatment

Determine deductibility:

| Category | 2026 Deductibility | Notes |
|----------|-------------------|-------|
| Travel (business) | 100% | Must be away from tax home |
| Lodging | 100% | Reasonable and necessary |
| Airfare | 100% | Business purpose |
| Meals (travel) | 50% | Away from tax home |
| Client meals | 50% | Business discussion required |
| Team meals | 50% | Ordinary and necessary |
| Entertainment | 0% | Generally not deductible |
| Office supplies | 100% | Ordinary and necessary |
| Software | 100% | Or amortize if capital |
| Equipment <$2,500 | 100% | De minimis safe harbor |
| Equipment >$2,500 | Depreciate | Section 179 may apply |

See `references/tax-rules-2026.md` for detailed tax guidance.

### Phase 4: Policy Compliance

Check against company policy:

```markdown
# Policy Check: [Expense Description]

## Amount Limits
| Category | Limit | This Expense | Status |
|----------|-------|--------------|--------|
| Meals (solo) | $50/meal | $[X] | [✓/✗] |
| Meals (group) | $75/person | $[X] | [✓/✗] |
| Lodging | $250/night | $[X] | [✓/✗] |
| Airfare class | Economy | [Class] | [✓/✗] |

## Documentation Requirements
- [ ] Receipt attached
- [ ] Business purpose stated
- [ ] Attendees listed (if meal)
- [ ] Approval obtained (if required)

## Policy Status
[Compliant / Requires Approval / Violation]

## Notes
[Any flags or concerns]
```

See `references/policy-violations.md` for common violations.

### Phase 5: Output

Generate categorized expense:

```markdown
# Categorized Expense

## Expense Details
| Field | Value |
|-------|-------|
| Date | [YYYY-MM-DD] |
| Merchant | [Name] |
| Amount | $[X.XX] |
| Description | [Description] |

## Categorization
| Field | Value |
|-------|-------|
| Category | [Primary category] |
| Subcategory | [Subcategory] |
| GL Code | [XXXX-XX] |
| Cost Center | [If applicable] |
| Project | [If applicable] |

## Tax Treatment
| Field | Value |
|-------|-------|
| Deductible Amount | $[X.XX] |
| Deduction Rate | [X%] |
| Tax Category | [IRS category] |
| Notes | [Any special treatment] |

## Compliance
| Field | Value |
|-------|-------|
| Policy Status | [Compliant/Flagged/Violation] |
| Required Action | [None/Approval needed/etc.] |
| Flags | [Any concerns] |
```

---

## Category Quick Reference

### Top 20 Categories

| Category | GL Code | Tax Rate | Common Examples |
|----------|---------|----------|-----------------|
| Travel: Airfare | 6100-01 | 100% | Flights, baggage fees |
| Travel: Lodging | 6100-02 | 100% | Hotels, Airbnb |
| Travel: Ground Transport | 6100-03 | 100% | Uber, taxi, rental car |
| Travel: Meals | 6100-04 | 50% | Meals while traveling |
| Travel: Mileage | 6100-05 | 100% | Personal vehicle use |
| Meals: Client | 6200-01 | 50% | Client dinners, lunches |
| Meals: Team | 6200-02 | 50% | Team lunches, events |
| Office: Supplies | 6300-01 | 100% | Paper, pens, etc. |
| Office: Postage | 6300-02 | 100% | Shipping, stamps |
| Office: Printing | 6300-03 | 100% | Print services |
| Technology: Software | 6400-01 | 100% | SaaS, licenses |
| Technology: Hardware | 6400-02 | 100%/Dep | Computers, phones |
| Technology: Services | 6400-03 | 100% | IT support, hosting |
| Professional: Legal | 6500-01 | 100% | Attorney fees |
| Professional: Accounting | 6500-02 | 100% | CPA, bookkeeping |
| Professional: Consulting | 6500-03 | 100% | External consultants |
| Marketing: Advertising | 6600-01 | 100% | Ads, promotions |
| Marketing: Events | 6600-02 | Varies | Trade shows, sponsorships |
| Training: Education | 6700-01 | 100% | Courses, conferences |
| Training: Books | 6700-02 | 100% | Books, subscriptions |

See `references/category-taxonomy.md` for complete list.

---

## When to Use

**This skill is appropriate when:**
- Processing expense receipts for reimbursement
- Categorizing transactions for bookkeeping
- Preparing expense reports
- Checking tax deductibility of expenses
- Identifying policy violations
- Setting up expense category structures

**Trigger keywords:**
- "expense", "categorize expense"
- "receipt", "expense report"
- "tax deductible", "deduction"
- "business expense", "reimbursement"
- "travel expense", "meal expense"
- "policy violation", "expense policy"

## When NOT to Use

- **Invoice processing:** Different workflow (accounts payable)
- **Revenue transactions:** Not expense categorization
- **Personal expenses:** Not business deductible
- **Tax filing:** Consult tax professional
- **Complex tax situations:** Consult CPA

---

## Common Mistakes

### 1. Missing Business Purpose
**Problem:** Expense submitted without stating why
**Solution:** Always document business reason (required for IRS)

### 2. Wrong Meal Category
**Problem:** Treating all meals as 100% deductible
**Solution:** Most meals are 50% deductible; entertainment is 0%

### 3. Personal vs. Business
**Problem:** Including personal portion of mixed expenses
**Solution:** Prorate business vs. personal use

### 4. Exceeding Limits Without Approval
**Problem:** Booking first class without pre-approval
**Solution:** Check policy limits before incurring expense

### 5. Missing Receipts
**Problem:** No documentation for expenses over $75
**Solution:** Always capture receipt; IRS requires for >$75

### 6. Stale Expense Submission
**Problem:** Submitting expenses months late
**Solution:** Submit within 30-60 days per policy

### 7. Incorrect Mileage Rate
**Problem:** Using outdated IRS mileage rate
**Solution:** Use current rate (67 cents/mile for 2026)

---

## Receipt Requirements

### IRS Requirements

| Expense Amount | Documentation Required |
|----------------|----------------------|
| Under $75 | Receipt recommended but not required |
| $75 and over | Receipt required |
| Lodging | Receipt always required (any amount) |
| Meals | Record of amount, date, place, business purpose, attendees |

### Best Practices

Always capture:
- Itemized receipt (not just credit card slip)
- Date of expense
- Merchant name
- Amount paid
- Payment method
- Business purpose

---

## Batch Processing

For multiple expenses:

```markdown
# Expense Batch: [Date Range or Trip Name]

## Summary
- Total Expenses: [X]
- Total Amount: $[X,XXX.XX]
- Reimbursable: $[X,XXX.XX]
- Non-Reimbursable: $[X.XX]

## Expenses

| # | Date | Merchant | Amount | Category | GL Code | Tax % | Policy |
|---|------|----------|--------|----------|---------|-------|--------|
| 1 | [Date] | [Merchant] | $[X] | [Cat] | [GL] | [%] | [✓/✗] |
| 2 | [Date] | [Merchant] | $[X] | [Cat] | [GL] | [%] | [✓/✗] |
| 3 | [Date] | [Merchant] | $[X] | [Cat] | [GL] | [%] | [✓/✗] |

## Flags/Notes
- [Any items requiring attention]

## Totals by Category
| Category | Count | Amount |
|----------|-------|--------|
| Travel | [X] | $[X] |
| Meals | [X] | $[X] |
| [Other] | [X] | $[X] |
```

---

## Scripts

For automated processing, see:
- `scripts/categorize.py` - Auto-categorization logic
- `scripts/validate_receipt.py` - Receipt data validation

---

## Resources

- `references/category-taxonomy.md` - Complete 40+ category list with GL codes
- `references/tax-rules-2026.md` - Current IRS deduction rules
- `references/policy-violations.md` - Common violations and severity
- `references/receipt-extraction.md` - OCR best practices
- `references/expense-report-template.md` - Full report structure

---

## Version History

- v1.0.0 (2026-01-08): Initial version with core categorization, tax rules, and policy compliance
