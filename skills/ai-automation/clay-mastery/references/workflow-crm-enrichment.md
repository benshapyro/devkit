# CRM Enrichment Workflow

Workflow for refreshing stale CRM data, filling gaps, and maintaining data quality.

## Workflow Overview

```
Import Stale Data → Prioritize → Waterfall Enrich → Validate → Push Updates
```

---

## Step 1: Identifying Stale Data

### Data Decay Reality

B2B data decays at ~30% annually:
- Job changes
- Company changes (M&A, closures)
- Email bounces
- Phone disconnects

### HubSpot Import Filters

**Contacts needing refresh:**
```
Last Modified Date is more than 90 days ago
AND Email is known
AND Lifecycle Stage is any of: Lead, MQL, SQL
```

**Contacts with missing data:**
```
(Phone is unknown OR LinkedIn URL is unknown)
AND Email is known
AND Last Activity Date is within last 180 days
```

**High-value accounts needing refresh:**
```
Annual Revenue is greater than $1,000,000
AND Last Modified Date is more than 60 days ago
```

### Salesforce SOQL Queries

**Stale contacts:**
```sql
SELECT Id, FirstName, LastName, Email, Phone, Account.Name
FROM Contact
WHERE LastModifiedDate < LAST_N_DAYS:90
AND Email != null
AND Account.Type = 'Customer'
LIMIT 1000
```

**Missing data:**
```sql
SELECT Id, FirstName, LastName, Email, AccountId
FROM Contact
WHERE (Phone = null OR LinkedIn_URL__c = null)
AND Email != null
ORDER BY Account.AnnualRevenue DESC
LIMIT 1000
```

---

## Step 2: Prioritization Strategy

### Prioritization Matrix

| Priority | Criteria | Enrichment Depth |
|----------|----------|------------------|
| P1 | Active opportunities, high revenue | Full waterfall + phone |
| P2 | Recent engagement, mid-size accounts | Full waterfall |
| P3 | Dormant, smaller accounts | Basic waterfall only |

### Prioritization Formula

```javascript
let priority = 3; // Default low

// Bump up for high value
if (Number({{Annual Revenue}}) > 1000000) priority = 1;
else if (Number({{Annual Revenue}}) > 100000) priority = 2;

// Bump up for recent engagement
if ({{Last Activity}} && new Date({{Last Activity}}) > new Date(Date.now() - 30*24*60*60*1000)) {
  priority = Math.max(1, priority - 1);
}

// Bump up for open opportunities
if ({{Open Opportunity}}) priority = 1;

priority
```

### Budget Allocation by Priority

| Priority | % of Budget | Credit Allocation |
|----------|-------------|-------------------|
| P1 | 50% | Full waterfall + premium providers |
| P2 | 35% | Standard waterfall |
| P3 | 15% | Basic providers only |

---

## Step 3: Batch Enrichment Strategy

### Phased Rollout

**Week 1:** P1 records only (test and validate)
**Week 2:** P2 records
**Week 3-4:** P3 records

### Batch Sizes

- Start with 100 records per batch
- Verify quality before scaling
- Scale to 500-1000 per batch once validated
- Monitor credit consumption

### Enrichment Sequence

| Step | Column | Condition |
|------|--------|-----------|
| 1 | Domain from Email | Always |
| 2 | Company Enrichment | If domain exists |
| 3 | LinkedIn Lookup | If name + company |
| 4 | Email Verification | If email exists |
| 5 | Phone Waterfall | P1 and P2 only |
| 6 | Data Quality Score | Always |

---

## Step 4: Validation Before Push

### Data Quality Checks

**Email validation:**
```javascript
// Check email is valid and verified
{{Email Verification Status}} === "valid" || 
{{Email Verification Status}} === "catch-all"
```

**Title validation:**
```javascript
// Check title isn't placeholder
const title = ({{New Title}} || "").toLowerCase();
!(title.includes("unknown") || title.includes("n/a") || title === "")
```

**Company match validation:**
```javascript
// Verify company name is similar (prevent wrong person)
const original = ({{Original Company}} || "").toLowerCase();
const enriched = ({{Enriched Company}} || "").toLowerCase();
original.includes(enriched.slice(0,10)) || enriched.includes(original.slice(0,10))
```

### AI Validation Column

**Prompt:**
```
Compare original CRM data with enriched data. Flag any concerns.

Original:
- Name: {{Original Name}}
- Company: {{Original Company}}
- Title: {{Original Title}}

Enriched:
- Name: {{Enriched Name}}
- Company: {{Enriched Company}}
- Title: {{Enriched Title}}
- LinkedIn: {{LinkedIn URL}}

Respond with:
- "VALID" if data appears correct
- "REVIEW" if there are discrepancies that need human review
- "INVALID" if data is clearly wrong (different person)

Output only: VALID, REVIEW, or INVALID
```

### Create Quality Flag

```javascript
const validation = {{AI Validation}};
const emailValid = {{Email Status}} === "valid";
const dataComplete = {{Phone}} && {{LinkedIn URL}};

validation === "VALID" && emailValid ? "Ready to Push" :
validation === "REVIEW" ? "Needs Review" :
"Do Not Push"
```

---

## Step 5: Push Updates to CRM

### Update Rules

**Critical setting: Enable "Ignore blank values"**

This prevents empty Clay fields from overwriting good CRM data.

### Field Mapping Strategy

| CRM Field | Update Rule |
|-----------|-------------|
| Phone | Only if new and CRM is empty |
| LinkedIn URL | Only if new and CRM is empty |
| Title | Update if changed |
| Company | DO NOT update (may break associations) |
| Email | DO NOT update (primary key) |
| Enrichment Date | Always update |

### Conditional Update Logic

**Only update if new data exists:**
```javascript
// Conditional for Phone update column
{{New Phone}} && !{{CRM Phone}}
```

**Update even if CRM has data (refresh):**
```javascript
// For fields we want to keep fresh
{{New Title}} && {{New Title}} !== {{CRM Title}}
```

### HubSpot Update Configuration

1. Add Enrichment → HubSpot → Update Contact
2. Use {{HubSpot Contact ID}} from import
3. Map fields with transformation formulas as needed
4. Enable "Ignore blank values"
5. Run with conditional: `{{Quality Flag}} === "Ready to Push"`

### Salesforce Update Configuration

1. Add Enrichment → Salesforce → Update Record
2. Object: Contact
3. Record ID: {{Salesforce Contact ID}}
4. Map fields
5. Conditional: `{{Quality Flag}} === "Ready to Push"`

---

## Continuous Enrichment Setup

### Scheduled Import (Weekly)

1. Create Clay table with CRM import
2. Set filter: Modified in last 7 days OR missing key fields
3. Enable Auto-Update schedule: Weekly on Sunday
4. Run enrichment workflow automatically

### Trigger-Based Enrichment

1. Create webhook table in Clay
2. In CRM, create workflow:
   - Trigger: Record created OR status change
   - Action: POST to Clay webhook
3. Clay enriches and pushes back immediately

### Data Freshness Dashboard

Create formula for tracking enrichment status:

```javascript
const lastEnriched = new Date({{Last Enriched Date}});
const daysSince = Math.floor((Date.now() - lastEnriched) / (1000*60*60*24));

daysSince <= 30 ? "Fresh" :
daysSince <= 90 ? "Aging" :
daysSince <= 180 ? "Stale" :
"Critical"
```

---

## End-to-End Example: Quarterly CRM Refresh

**Goal:** Refresh all customer contacts quarterly

**Phase 1: Import & Prioritize**
- Import: Contacts where Customer = true, Last Modified > 90 days
- Prioritize: By account revenue
- Expected: 5,000 contacts

**Phase 2: Enrich (Week 1-2)**
- Run waterfall on batches of 500
- P1 (1,000 contacts): Full enrichment + phone
- P2 (2,000 contacts): Standard enrichment
- P3 (2,000 contacts): Basic enrichment

**Phase 3: Validate (Week 3)**
- AI validation on all
- Manual review of "REVIEW" flags (~5%)
- Calculate update readiness

**Phase 4: Push (Week 4)**
- Push "Ready to Push" records
- Log changes for audit trail
- Report on data quality improvements

**Credit Budget:**
- P1: 1,000 × 15 credits = 15,000
- P2: 2,000 × 8 credits = 16,000
- P3: 2,000 × 4 credits = 8,000
- **Total: ~39,000 credits**

**Success Metrics:**
- Email validity rate: 90%+
- Phone coverage increase: +20%
- LinkedIn coverage: 80%+
- Bounce rate reduction: -50%
