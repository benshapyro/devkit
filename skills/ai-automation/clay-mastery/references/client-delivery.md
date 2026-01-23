# Client Delivery Guide

How to package and hand off Clay implementations to clients.

---

## Delivery Philosophy

**Clients don't operate Clay directly.** Cadre builds and maintains Clay workflows. Delivery focuses on:

1. **Documentation** - What was built and why
2. **Results reporting** - Outputs and metrics
3. **Process transparency** - How it works conceptually
4. **Change requests** - How to request modifications

---

## Delivery Artifacts

### 1. Solution Overview Document

**Purpose:** Executive summary of what was built

**Template:**
```markdown
# Clay Implementation: [Client Name]

## Overview
Brief description of the automation implemented.

## Business Problem Solved
- What manual process was automated
- Time/cost savings achieved
- Data quality improvements

## Solution Components
| Workflow | Purpose | Frequency |
|----------|---------|-----------|
| Outbound Prospecting | Build target lists | Weekly |
| Inbound Enrichment | Enrich form submissions | Real-time |
| CRM Refresh | Update stale contacts | Monthly |

## Data Sources
- LinkedIn Sales Navigator
- Company websites
- Clearbit, Apollo, Prospeo (enrichment providers)

## Outputs Delivered
- Enriched contact lists (CSV/direct to CRM)
- Weekly prospect batches
- Data quality reports

## Ownership & Access
- Cadre maintains Clay workspace
- Client receives outputs via [method]
- Client contacts [name] for changes
```

### 2. Workflow Documentation

**Purpose:** Technical documentation of each workflow

**Template:**
```markdown
# Workflow: [Workflow Name]

## Purpose
What this workflow does and why.

## Trigger
How the workflow starts:
- Manual: Run on-demand
- Scheduled: Daily/Weekly at [time]
- Webhook: Triggered by [source]

## Input Requirements
| Field | Required | Format | Example |
|-------|----------|--------|---------|
| Company Name | Yes | Text | "Acme Inc" |
| Website | Yes | URL | "https://acme.com" |
| Target Title | No | Text | "VP Sales" |

## Processing Steps
1. **Find Domain** - Convert company name to website
2. **Enrich Company** - Get firmographics from Clearbit
3. **Filter ICP** - Score against criteria
4. **Find Contacts** - Search for decision-makers
5. **Enrich Contacts** - Email and phone waterfall
6. **Quality Check** - Validate data accuracy
7. **Export** - Push to [destination]

## Output Fields
| Field | Source | Notes |
|-------|--------|-------|
| First Name | LinkedIn | |
| Email | Waterfall | Verified |
| ICP Score | Formula | 0-100 |

## Quality Metrics
- Expected hit rate: 70-80%
- Average credits per lead: 8-12
- Typical processing time: 2-3 hours per 1,000

## Known Limitations
- Cannot access gated content
- International coverage varies by region
- Some industries have lower data availability
```

### 3. ICP Scoring Documentation

**Purpose:** Explain how leads are scored

**Template:**
```markdown
# ICP Scoring Model: [Client Name]

## Scoring Criteria

| Criterion | Weight | Scoring Rules |
|-----------|--------|---------------|
| Company Size | 30% | 100-500: Full, 50-99 or 501-1000: Half |
| Industry | 25% | Tech/Healthcare: Full, Other B2B: Half |
| Geography | 20% | US: Full, Canada/UK: Half |
| Title Seniority | 15% | VP+: Full, Director: Half |
| Tech Fit | 10% | Uses Salesforce: Full |

## Score Interpretation

| Score | Grade | Action |
|-------|-------|--------|
| 80-100 | A | Immediate outreach |
| 60-79 | B | Standard sequence |
| 40-59 | C | Nurture track |
| 0-39 | D | Do not contact |

## Example Calculations

**Example 1: Strong Fit**
- 200 employees (30 pts)
- Technology industry (25 pts)
- United States (20 pts)
- VP of Sales (15 pts)
- Uses Salesforce (10 pts)
- **Total: 100 - Grade A**

**Example 2: Moderate Fit**
- 75 employees (15 pts)
- Professional Services (12 pts)
- Canada (10 pts)
- Director (7 pts)
- No tech match (0 pts)
- **Total: 44 - Grade C**

## Adjusting the Model
To request scoring changes, contact [name] with:
- Which criterion to adjust
- New scoring rules
- Business rationale
```

---

## Output Delivery Methods

### Option 1: CRM Integration (Preferred)

**Setup:** Clay pushes directly to client's CRM

**Client experience:**
- New records appear automatically
- Custom fields populated
- No manual import needed

**Documentation for client:**
```markdown
## CRM Integration

Data flows automatically to your HubSpot/Salesforce:
- New contacts created in [list/campaign]
- Existing contacts updated (not duplicated)
- Custom fields populated: ICP Score, Data Source, Enrichment Date

**Field Mapping:**
| Clay Field | CRM Field |
|------------|-----------|
| First Name | firstname |
| ICP Score | lead_score__c |
| ... | ... |

**Sync Frequency:** [Real-time / Daily at X]

**Handling:** Duplicates checked by email before creation
```

### Option 2: Scheduled CSV Delivery

**Setup:** Automated export to shared location

**Client experience:**
- Weekly CSV in Google Drive/Dropbox
- Consistent format each delivery
- Historical files retained

**Documentation:**
```markdown
## Weekly Delivery

Every [day] at [time], a new file is delivered:
- Location: [Shared Drive link]
- Format: CSV, UTF-8 encoded
- Naming: prospects_YYYY-MM-DD.csv

**Columns Included:**
[list columns and descriptions]

**To Import to Your CRM:**
1. Download the latest file
2. Import using standard process
3. Map columns as documented
```

### Option 3: Sequencer Integration

**Setup:** Clay pushes to email sequencer

**Client experience:**
- Prospects added to campaign automatically
- Personalization fields populated
- Ready to send

**Documentation:**
```markdown
## Sequencer Integration

Qualified prospects automatically added to:
- Platform: [Smartlead/Instantly/Apollo]
- Campaign: [Campaign Name]
- Cadence: [X emails over Y days]

**Variables Populated:**
| Variable | Source |
|----------|--------|
| {{first_name}} | Clay enrichment |
| {{company}} | Clay enrichment |
| {{personalization}} | AI-generated |

**Review Process:**
Prospects enter campaign in "Pending" status.
[Sales team/Cadre] reviews and activates.
```

---

## Reporting Framework

### Weekly Metrics Report

**Template:**
```markdown
# Weekly Clay Report: [Client Name]
Week of [Date]

## Summary
- Records Processed: X
- Qualified Leads: X (Y%)
- Credits Used: X
- Cost per Lead: $X

## Workflow Performance

| Workflow | Input | Output | Hit Rate |
|----------|-------|--------|----------|
| Outbound | 500 | 380 | 76% |
| Inbound | 45 | 42 | 93% |

## Data Quality

| Metric | This Week | Trend |
|--------|-----------|-------|
| Email Validity | 92% | ↑ |
| Phone Coverage | 45% | → |
| ICP A-Grade | 35% | ↑ |

## Issues & Notes
- [Any issues encountered]
- [Adjustments made]
- [Recommendations]

## Next Week
- [Planned activities]
- [Expected outputs]
```

### Monthly Business Review

**Template:**
```markdown
# Monthly Clay Review: [Client Name]
[Month Year]

## Executive Summary
[2-3 sentences on overall performance]

## Volume Metrics

| Metric | Month | QTD | YTD |
|--------|-------|-----|-----|
| Leads Generated | X | X | X |
| Credits Used | X | X | X |
| Cost per Lead | $X | $X | $X |

## Quality Metrics

| Metric | Month | Target | Status |
|--------|-------|--------|--------|
| Email Validity | 91% | 90% | ✓ |
| ICP Fit Rate | 72% | 70% | ✓ |
| Contact Rate | 65% | 60% | ✓ |

## ROI Analysis
- Investment: $X (credits + management)
- Leads Generated: X
- Pipeline Created: $X (from CRM)
- ROI: X%

## Recommendations
1. [Recommendation with rationale]
2. [Recommendation with rationale]

## Q&A / Discussion Items
- [Topics for discussion]
```

---

## Change Request Process

### Documentation for Clients

```markdown
# Requesting Changes to Your Clay Workflows

## How to Request Changes

Email [contact] with:
1. **What** - Describe the change needed
2. **Why** - Business reason
3. **Priority** - Urgent / Standard / Nice-to-have
4. **Timeline** - When you need it

## Change Types

| Type | Turnaround | Examples |
|------|------------|----------|
| Quick Fix | 1-2 days | Fix a typo, adjust a filter |
| Enhancement | 3-5 days | Add a field, new data source |
| New Workflow | 1-2 weeks | New automation end-to-end |

## What We Need from You

**For ICP changes:**
- Updated criteria with specifics
- Example companies that fit/don't fit

**For new data fields:**
- Where it should come from
- How it will be used

**For new workflows:**
- Business process to automate
- Input sources
- Desired outputs
- Success criteria
```

---

## Handoff Checklist

### Before Delivery

- [ ] All workflows tested and stable
- [ ] Error handling in place
- [ ] Monitoring configured
- [ ] Documentation complete
- [ ] Client CRM/tools integrated
- [ ] Sample output reviewed with client

### Delivery Meeting Agenda

1. **Solution walkthrough** (15 min)
   - What was built
   - How it works (conceptual)
   - Where outputs go

2. **Output review** (10 min)
   - Sample records
   - Field explanations
   - Quality metrics

3. **Operations** (10 min)
   - Delivery schedule
   - Reporting cadence
   - Support process

4. **Q&A** (10 min)

### Post-Delivery

- [ ] Send documentation package
- [ ] Confirm first delivery received
- [ ] Schedule first check-in (1 week)
- [ ] Set up reporting cadence
- [ ] Document any immediate feedback

---

## Client FAQ Responses

**"Can we get access to Clay directly?"**
> We manage Clay on your behalf to ensure quality and efficiency. You receive the outputs and reporting, while we handle the technical operations. This lets your team focus on using the data rather than managing the tool.

**"How accurate is this data?"**
> We use multiple data sources and verification steps. Email accuracy is typically 90%+, verified through ZeroBounce. Company data comes from Clearbit and other premium sources. We document hit rates in weekly reports.

**"Can we add more fields?"**
> Yes, submit a change request with the fields you need. We'll evaluate data availability and credit impact, then implement.

**"What happens if something breaks?"**
> We monitor workflows proactively. If issues occur, you'll be notified and we'll resolve quickly. For urgent issues, contact [name/channel].

**"How do we know we're not overpaying for credits?"**
> We optimize for cost-efficiency: filtering before expensive enrichments, using appropriate provider tiers, and monitoring credit usage. Monthly reports include cost-per-lead metrics.
