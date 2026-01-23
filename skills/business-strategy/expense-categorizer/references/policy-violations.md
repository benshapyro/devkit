# Policy Violations Guide

Common expense policy violations, detection patterns, and severity levels.

## Violation Severity Levels

| Level | Definition | Action Required |
|-------|------------|-----------------|
| **Critical** | Fraud, falsification, gross misconduct | Immediate escalation to HR/Legal |
| **High** | Clear policy violation, significant amount | Manager + Finance approval required |
| **Medium** | Policy violation, moderate amount | Manager approval required |
| **Low** | Minor violation, easily corrected | Correction or explanation required |
| **Warning** | Near violation, best practice issue | Notification to employee |

---

## Critical Violations

### Expense Fraud

**Patterns:**
- Fictitious expenses (no actual purchase)
- Inflated amounts (actual receipt differs)
- Duplicate submissions (same expense submitted twice)
- Personal expenses claimed as business
- Collusion with vendors

**Detection Signals:**
- Vendor doesn't exist or can't be verified
- Sequential receipt numbers from same vendor
- Round numbers on receipts
- Altered or suspicious receipts
- Patterns matching known fraud schemes

**Action:**
- Immediate freeze on expense processing
- HR/Legal investigation
- Potential termination and legal action

### Receipt Falsification

**Patterns:**
- Doctored receipts (amounts changed)
- Forged receipts
- Receipts from closed businesses
- Inconsistent formatting within receipt

**Detection Signals:**
- Font inconsistencies
- Misaligned text
- Impossible dates (business closed)
- Metadata doesn't match claimed date

**Action:**
- Forensic review of submitted receipts
- Investigation of other submissions
- HR/Legal involvement

---

## High-Severity Violations

### Significant Overages Without Approval

**Threshold Examples:**
- Airfare exceeds policy by >50%
- Lodging exceeds policy by >50%
- Single meal exceeds 2x per-person limit
- Total trip expense >25% over estimate

**Detection Signals:**
- Automated flagging on amount
- Pattern of repeated overages
- Lack of pre-trip approval

**Resolution:**
- Manager justification required
- Finance review
- Potential partial reimbursement only

### Unauthorized Class of Service

**Examples:**
- First/business class without approval
- Premium car rental without approval
- Luxury hotel without justification
- Premium service upgrades

**Detection Signals:**
- Fare class codes on airfare
- Vehicle class on rental
- Hotel brand/rate analysis

**Resolution:**
- Reimburse at policy-allowed class
- Employee pays difference
- Exception requires executive approval

### Split Transactions

**Pattern:** Splitting single purchase into multiple receipts to avoid approval threshold

**Detection Signals:**
- Same vendor, same day, sequential times
- Amounts just under threshold
- Pattern of purchases at $X - $1

**Resolution:**
- Treat as single transaction
- Apply appropriate approval level
- Warning for first offense

### Personal Expenses Claimed

**Examples:**
- Personal meals with no business purpose
- Entertainment without business relationship
- Spouse/family travel costs
- Personal items on business purchases

**Detection Signals:**
- Weekend/holiday timing without travel
- Known personal vendors
- Attendee lists missing
- Unusual purchase patterns

**Resolution:**
- Expense rejected
- Recovery if already paid
- Policy retraining

---

## Medium-Severity Violations

### Missing Documentation

**Requirements Violated:**
- Receipt missing for expense >$75
- Attendees not listed for meals
- Business purpose not stated
- Missing approval for required expense

**Detection Signals:**
- Automated check for receipts
- Form field validation
- Policy rule enforcement

**Resolution:**
- Return to employee for documentation
- Withhold payment until complete
- Pattern may escalate severity

### Late Submissions

**Policy Example:** Expenses due within 30-60 days

**Detection Signals:**
- Expense date vs. submission date
- Automated age flagging

**Resolution:**
- Warning for first offense
- Reduced reimbursement for repeat
- Rejection for extremely late (90+ days)

### Minor Overages

**Threshold Examples:**
- Airfare 10-50% over policy
- Lodging 10-50% over policy
- Meal 25-100% over per-person limit

**Detection Signals:**
- Automated amount comparison

**Resolution:**
- Manager review and approval
- Justification documented
- Pattern tracking

### Incorrect Category

**Examples:**
- Categorizing entertainment as meals
- Categorizing personal as business
- Using wrong GL code

**Detection Signals:**
- Manual review
- Category anomaly detection
- Vendor mismatch with category

**Resolution:**
- Recategorization required
- Retraining for repeated issues

---

## Low-Severity Violations

### Minor Documentation Gaps

**Examples:**
- Business purpose vague but present
- Receipt unclear but readable
- Minor data entry errors

**Detection Signals:**
- Manual review
- Quality scoring

**Resolution:**
- Correction by employee
- Process without delay for minor issues

### Expense Entry Errors

**Examples:**
- Typos in vendor name
- Wrong date (off by a day)
- Minor calculation errors

**Detection Signals:**
- Automated validation
- Manual review

**Resolution:**
- Simple correction
- No policy action for honest mistakes

### Near-Policy Expenses

**Examples:**
- Meal at 95% of limit
- Hotel at policy maximum
- Repeated expenses at threshold

**Detection Signals:**
- Pattern analysis
- Threshold monitoring

**Resolution:**
- No action for occasional
- Review for patterns

---

## Warning-Level Issues

### Best Practice Deviations

**Examples:**
- Not using preferred vendors
- Not booking in advance
- Excessive taxi vs. cheaper transit
- Room service vs. restaurant

**Detection Signals:**
- Vendor analysis
- Booking timing analysis
- Cost comparison

**Resolution:**
- Advisory notification
- Cost awareness reminder

### Pattern Monitoring

**Watch For:**
- Expenses consistently near limits
- Same vendor repeated frequently
- Weekend/holiday expense patterns
- Expense timing around deadlines

**Action:**
- Track and monitor
- Periodic review
- Escalate if concerning pattern

---

## Detection Methods

### Automated Checks

| Check | Violation Type | Trigger |
|-------|---------------|---------|
| Amount threshold | Overage | Amount > limit |
| Receipt required | Documentation | Amount ≥ $75, no attachment |
| Duplicate detection | Fraud | Same vendor, amount, date |
| Category validation | Classification | Vendor/category mismatch |
| Date validation | Data quality | Future date, >90 days old |
| Split transaction | Fraud | Same vendor, same day, under threshold |

### Manual Review Triggers

| Trigger | Review Focus |
|---------|--------------|
| First submission | New employee onboarding |
| Amount > $1,000 | Manager review |
| Entertainment | Business purpose verification |
| International travel | All expenses verified |
| Audit sample | Random selection (~5%) |
| Previous issues | Enhanced scrutiny period |

### Analytics-Based Detection

| Pattern | Possible Violation |
|---------|-------------------|
| Expenses on weekends consistently | Personal expense claims |
| Same vendor repeatedly | Potential kickback or split |
| Round numbers frequently | Estimation vs. actual |
| Just under thresholds | Split transaction |
| Outlier vs. peers | Policy abuse |

---

## Response Framework

### For Employees

| Situation | Recommended Action |
|-----------|-------------------|
| Honest mistake | Correct and resubmit with explanation |
| Policy unclear | Ask manager/finance before incurring |
| Need exception | Get pre-approval in writing |
| Dispute rejection | Provide additional documentation |

### For Approvers

| Situation | Recommended Action |
|-----------|-------------------|
| Minor violation | Approve with note, coach employee |
| Moderate violation | Return for correction or justification |
| Significant violation | Reject, document, notify finance |
| Suspected fraud | Do not approve, escalate immediately |

### For Finance/Audit

| Situation | Recommended Action |
|-----------|-------------------|
| Pattern detected | Document and investigate |
| Single violation | Follow standard process |
| Repeated violations | Escalate to HR/management |
| Fraud suspected | Legal/HR involvement, preserve evidence |

---

## Policy Limit Examples

**Note:** These are examples; actual limits vary by organization.

| Category | Standard Limit | Exception Process |
|----------|---------------|-------------------|
| Domestic airfare | $800 | VP approval >$1,200 |
| International airfare | $2,500 | VP approval for business class |
| Lodging (per night) | $250 | Exceeds for high-cost cities |
| Meals (solo) | $50 | None |
| Meals (group/person) | $75 | Manager approval >$100 |
| Client meals/person | $150 | Director approval >$200 |
| Ground transport/day | $100 | Manager approval >$150 |
| Car rental class | Intermediate | Manager approval for larger |
| Conference registration | $2,000 | VP approval >$3,000 |
| Single purchase | $500 | Manager approval >$500 |

---

## Prevention Best Practices

### For Organizations

1. **Clear, written policy** - No ambiguity
2. **Regular training** - Annual refresher
3. **Pre-approval for exceptions** - Before expense incurred
4. **Automated controls** - Catch issues early
5. **Timely reimbursement** - Reduce pressure to bend rules
6. **Anonymous reporting** - Encourage speaking up

### For Employees

1. **Read the policy** - Know the rules
2. **When in doubt, ask** - Get guidance
3. **Document everything** - Receipts + purpose
4. **Submit promptly** - Don't wait
5. **Separate personal/business** - Clear boundaries
