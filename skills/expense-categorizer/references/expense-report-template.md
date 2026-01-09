# Expense Report Templates

Templates for various expense report formats and scenarios.

## Standard Expense Report

### Header Information

```markdown
# Expense Report

**Employee:** [Name]
**Employee ID:** [ID]
**Department:** [Department]
**Manager:** [Manager Name]
**Report Period:** [Start Date] to [End Date]
**Report Date:** [Submission Date]
**Report Number:** [Auto-generated]

## Purpose/Description
[Brief description of expenses - e.g., "Q1 Client Visits" or "Annual Conference"]
```

### Expense Details Table

```markdown
## Expenses

| # | Date | Merchant | Description | Category | Amount | Receipt | Status |
|---|------|----------|-------------|----------|--------|---------|--------|
| 1 | YYYY-MM-DD | [Merchant] | [Description] | [Category] | $X.XX | ✓ | [Status] |
| 2 | YYYY-MM-DD | [Merchant] | [Description] | [Category] | $X.XX | ✓ | [Status] |
| 3 | YYYY-MM-DD | [Merchant] | [Description] | [Category] | $X.XX | ✓ | [Status] |

**Total Expenses:** $XXX.XX
```

### Summary by Category

```markdown
## Summary by Category

| Category | Count | Amount |
|----------|-------|--------|
| Travel: Airfare | X | $XXX.XX |
| Travel: Lodging | X | $XXX.XX |
| Travel: Meals | X | $XXX.XX |
| Meals: Client | X | $XXX.XX |
| [Other] | X | $XXX.XX |
| **Total** | **X** | **$XXX.XX** |
```

### Approval Section

```markdown
## Approvals

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Employee | [Name] | [Date] | [Signed] |
| Manager | [Name] | [Date] | [Pending] |
| Finance | [Name] | [Date] | [Pending] |
```

---

## Trip Expense Report

For business travel with multiple expenses.

```markdown
# Trip Expense Report

## Trip Information

| Field | Value |
|-------|-------|
| **Employee** | [Name] |
| **Destination** | [City, State/Country] |
| **Departure Date** | [YYYY-MM-DD] |
| **Return Date** | [YYYY-MM-DD] |
| **Trip Purpose** | [Business reason] |
| **Project/Client** | [If applicable] |
| **Approved By** | [Pre-approval reference] |

---

## Trip Expenses

### Transportation

| Date | Type | Description | Amount | Receipt |
|------|------|-------------|--------|---------|
| [Date] | Airfare | [Airline, Route] | $XXX.XX | ✓ |
| [Date] | Car Rental | [Company, Days] | $XXX.XX | ✓ |
| [Date] | Uber/Taxi | [Route] | $XX.XX | ✓ |
| [Date] | Mileage | [X miles @ $0.67] | $XX.XX | Log |
| [Date] | Parking | [Location] | $XX.XX | ✓ |

**Transportation Total:** $XXX.XX

### Lodging

| Date | Hotel | Location | Nightly Rate | Total | Receipt |
|------|-------|----------|--------------|-------|---------|
| [Date] | [Hotel Name] | [City] | $XXX.XX | $XXX.XX | ✓ |
| [Date] | [Hotel Name] | [City] | $XXX.XX | $XXX.XX | ✓ |

**Lodging Total:** $XXX.XX

### Meals

| Date | Type | Restaurant | Attendees | Amount | Receipt |
|------|------|------------|-----------|--------|---------|
| [Date] | Breakfast | [Name] | Solo | $XX.XX | ✓ |
| [Date] | Lunch | [Name] | [Names] | $XX.XX | ✓ |
| [Date] | Dinner | [Name] | [Names] | $XX.XX | ✓ |

**Meals Total:** $XXX.XX

### Other Expenses

| Date | Description | Category | Amount | Receipt |
|------|-------------|----------|--------|---------|
| [Date] | [Description] | [Category] | $XX.XX | ✓ |

**Other Total:** $XX.XX

---

## Trip Summary

| Category | Amount | Tax Treatment |
|----------|--------|---------------|
| Transportation | $XXX.XX | 100% deductible |
| Lodging | $XXX.XX | 100% deductible |
| Meals | $XXX.XX | 50% deductible |
| Other | $XX.XX | Varies |
| **Trip Total** | **$X,XXX.XX** | |

**Amount Reimbursable:** $X,XXX.XX
**Amount Pre-paid (Corporate Card):** $XXX.XX
**Amount Due Employee:** $XXX.XX
```

---

## Client Entertainment Report

For meals and events with clients/prospects.

```markdown
# Client Entertainment Expense Report

## Event Information

| Field | Value |
|-------|-------|
| **Employee** | [Name] |
| **Date** | [YYYY-MM-DD] |
| **Venue** | [Restaurant/Location] |
| **Client/Company** | [Client Name] |
| **Total Amount** | $XXX.XX |

---

## Business Purpose

[Detailed description of business discussion topics and objectives]

---

## Attendees

### Our Company
| Name | Title |
|------|-------|
| [Name] | [Title] |
| [Name] | [Title] |

### Client
| Name | Title | Company |
|------|-------|---------|
| [Name] | [Title] | [Company] |
| [Name] | [Title] | [Company] |

**Total Attendees:** X

---

## Expense Details

| Item | Amount |
|------|--------|
| Food & Beverages | $XXX.XX |
| Tax | $XX.XX |
| Tip | $XX.XX |
| **Total** | **$XXX.XX** |

**Cost per Person:** $XX.XX

---

## Tax Treatment

| Amount | Deductibility | Note |
|--------|---------------|------|
| $XXX.XX | 50% | Meals with clients |

---

## Approval

| Approver | Status | Date |
|----------|--------|------|
| Manager | [Pending/Approved] | [Date] |
| Director | [If >$200] | [Date] |
```

---

## Monthly Expense Summary

For regular monthly expense reporting.

```markdown
# Monthly Expense Summary

**Employee:** [Name]
**Department:** [Department]
**Month:** [Month Year]
**Submission Date:** [Date]

---

## Expense Summary

| Category | Count | Amount | % of Total |
|----------|-------|--------|------------|
| Travel | X | $XXX.XX | XX% |
| Meals & Entertainment | X | $XXX.XX | XX% |
| Office Supplies | X | $XX.XX | XX% |
| Technology | X | $XX.XX | XX% |
| Training | X | $XX.XX | XX% |
| Other | X | $XX.XX | XX% |
| **Total** | **X** | **$X,XXX.XX** | **100%** |

---

## Detailed Expenses

### Week 1 (MM/DD - MM/DD)

| Date | Merchant | Description | Category | Amount |
|------|----------|-------------|----------|--------|
| [Date] | [Merchant] | [Description] | [Category] | $XX.XX |
| [Date] | [Merchant] | [Description] | [Category] | $XX.XX |

**Week 1 Total:** $XXX.XX

### Week 2 (MM/DD - MM/DD)

[Same format...]

### Week 3 (MM/DD - MM/DD)

[Same format...]

### Week 4 (MM/DD - MM/DD)

[Same format...]

---

## Budget Comparison

| Category | Budget | Actual | Variance |
|----------|--------|--------|----------|
| Travel | $X,XXX | $X,XXX | ($XXX) |
| Meals | $XXX | $XXX | $XX |
| [Other] | $XXX | $XXX | $XX |
| **Total** | **$X,XXX** | **$X,XXX** | **($XXX)** |

---

## Notes

[Any explanations for variances or unusual expenses]
```

---

## Mileage Log

For personal vehicle business use.

```markdown
# Mileage Expense Log

**Employee:** [Name]
**Vehicle:** [Make/Model/Year]
**Period:** [Start Date] to [End Date]
**Rate:** $0.67/mile (2026 IRS rate)

---

## Trip Log

| Date | From | To | Purpose | Miles | Amount |
|------|------|----|---------| ------|--------|
| [Date] | [Origin] | [Destination] | [Business purpose] | XX.X | $XX.XX |
| [Date] | [Origin] | [Destination] | [Business purpose] | XX.X | $XX.XX |
| [Date] | [Origin] | [Destination] | [Business purpose] | XX.X | $XX.XX |

---

## Summary

| Metric | Value |
|--------|-------|
| Total Trips | X |
| Total Miles | XXX.X |
| Rate | $0.67/mile |
| **Total Reimbursement** | **$XXX.XX** |

---

## Certification

I certify that the mileage claimed above was for business purposes and
that no personal mileage is included.

**Employee Signature:** _____________ **Date:** _____________
```

---

## Per Diem Report

For flat-rate meal reimbursement during travel.

```markdown
# Per Diem Expense Report

**Employee:** [Name]
**Trip:** [Description]
**Location:** [City, State]
**Per Diem Rate:** $XX/day (GSA rate for location)

---

## Per Diem Calculation

| Date | Location | Breakfast | Lunch | Dinner | Daily Total |
|------|----------|-----------|-------|--------|-------------|
| [Date] | [City] | $X | $X | $X | $XX |
| [Date] | [City] | $X | $X | $X | $XX |
| [Date] | [City] | $X | $X | $X | $XX |

**Note:** First and last day of travel at 75% rate.

---

## Summary

| Item | Amount |
|------|--------|
| Full Days (X days @ $XX) | $XXX.XX |
| Partial Days (X days @ $XX) | $XX.XX |
| **Total Per Diem** | **$XXX.XX** |

---

## Meal Deductions

| Date | Meal | Reason | Deduction |
|------|------|--------|-----------|
| [Date] | Breakfast | Provided by hotel | -$X.XX |
| [Date] | Lunch | Provided at conference | -$X.XX |

**Total Deductions:** $XX.XX
**Net Per Diem:** $XXX.XX
```

---

## Expense Reconciliation Report

For matching expenses to corporate card statements.

```markdown
# Corporate Card Reconciliation

**Cardholder:** [Name]
**Card Ending:** XXXX
**Statement Period:** [Start Date] to [End Date]
**Statement Amount:** $X,XXX.XX

---

## Transaction Matching

| Date | Merchant | Card Amount | Reported Amount | Status | Notes |
|------|----------|-------------|-----------------|--------|-------|
| [Date] | [Merchant] | $XXX.XX | $XXX.XX | ✓ Match | |
| [Date] | [Merchant] | $XX.XX | $XX.XX | ✓ Match | |
| [Date] | [Merchant] | $XX.XX | - | ⚠ Missing | [Explanation] |
| [Date] | [Merchant] | $XXX.XX | $XXX.XX | ✓ Match | |

---

## Reconciliation Summary

| Status | Count | Amount |
|--------|-------|--------|
| Matched | X | $X,XXX.XX |
| Pending | X | $XXX.XX |
| Missing | X | $XX.XX |
| Personal (to be repaid) | X | $XX.XX |
| **Statement Total** | **X** | **$X,XXX.XX** |

---

## Outstanding Items

### Missing Expenses (need reports)
| Date | Merchant | Amount | Action Needed |
|------|----------|--------|---------------|
| [Date] | [Merchant] | $XX.XX | Submit expense report |

### Personal Charges (to be repaid)
| Date | Merchant | Amount | Repayment Method |
|------|----------|--------|------------------|
| [Date] | [Merchant] | $XX.XX | Payroll deduction |

---

## Certification

I have reviewed this statement and confirmed that all business expenses
have been reported and all personal charges will be repaid.

**Employee Signature:** _____________ **Date:** _____________
```

---

## Quick Entry Templates

### Single Expense

```markdown
**Date:** [YYYY-MM-DD]
**Merchant:** [Name]
**Amount:** $[XX.XX]
**Category:** [Category]
**Description:** [What was purchased]
**Business Purpose:** [Why needed for business]
**Receipt:** [Attached/Not Required]
```

### Meal with Attendees

```markdown
**Date:** [YYYY-MM-DD]
**Restaurant:** [Name]
**Amount:** $[XX.XX]
**Category:** Client Meals
**Business Purpose:** [Topics discussed]
**Attendees:**
- [Name 1], [Title], [Company]
- [Name 2], [Title], [Company]
**Receipt:** Attached
```

### Travel Day

```markdown
**Date:** [YYYY-MM-DD]
**Trip:** [Destination]

| Expense | Merchant | Amount | Category |
|---------|----------|--------|----------|
| Flight | [Airline] | $XXX.XX | Airfare |
| Hotel | [Hotel] | $XXX.XX | Lodging |
| Uber to airport | Uber | $XX.XX | Ground Transport |
| Dinner | [Restaurant] | $XX.XX | Travel Meals |

**Day Total:** $XXX.XX
```
