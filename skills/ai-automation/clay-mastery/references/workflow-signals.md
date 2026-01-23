# Signal Monitoring Workflows

Workflows for tracking buying signals: job changes, funding, hiring, and technology changes.

## Signal Types Overview

| Signal | Meaning | Use Case |
|--------|---------|----------|
| Job Changes | Champion moved to new company | Expansion opportunity |
| Funding | Company has budget | New opportunity |
| Hiring | Team expansion | Growing need |
| Tech Changes | New tool adoption | Competitive/integration |
| News Mentions | Strategic changes | Timely outreach |

---

## Job Change Monitoring

### Clay's Native Job Change Feature

**Setup:**
1. Build table with LinkedIn Profile URLs
2. Click Actions → "Monitor for Job Changes"
3. Configure:
   - Historical check: 3, 6, or 12 months
   - Run frequency: Daily or weekly
4. Enable monitoring

**Output columns created:**
- Job Mover Name
- Previous Company
- New Company
- New LinkedIn URL
- Start Date

**Limitations:**
- Max 1,000 people per table
- Max 3 monitored tables per workspace
- Requires LinkedIn Profile URL

### Use Case: Champion Tracking

**Scenario:** Track former champions who left customer accounts

**Setup:**
1. Export closed-won contacts from CRM
2. Import to Clay with LinkedIn URLs
3. Enable job change monitoring
4. Create notification workflow

**Enrichment on job change detected:**
1. New company domain (Clearbit)
2. New company firmographics
3. ICP score for new company
4. Work email at new company

**Outreach trigger:**
```javascript
// Notify sales if:
// - Champion moved
// - New company fits ICP
{{Job Change Detected}} && {{New Company ICP Score}} >= 60
```

### Workflow: Champion Job Change → Outreach

| Column | Type | Notes |
|--------|------|-------|
| LinkedIn URL | Import | From CRM |
| Job Change Status | Clay Monitor | Native feature |
| New Company | Clay Monitor | Auto-populated |
| New Domain | Claygent | Find new company website |
| New Company Data | Clearbit | Firmographics |
| New ICP Score | Formula | Qualification |
| New Work Email | Waterfall | If qualified |
| Slack Alert | Slack | Notify rep |

---

## Funding Signal Monitoring

### Funding Data Sources

| Source | Best For | Credits |
|--------|----------|---------|
| Crunchbase | VC-backed startups | 5 |
| Harmonic | Early-stage startups | 3 |
| PitchBook (via API) | Comprehensive | Varies |
| Claygent + TechCrunch | Recent announcements | 1-3 |

### Setup: Funding Round Detection

**Option A: Import from Source**
1. Use Crunchbase or Harmonic to find recent fundings
2. Filter by: Round type, Amount, Date range, Industry
3. Import to Clay for enrichment

**Option B: Monitor Target Accounts**
1. List of target companies
2. Periodic Claygent check for funding news
3. Alert on new rounds detected

**Claygent prompt for funding detection:**
```
Search for recent funding announcements for {{Company Name}}.
Look at TechCrunch, Crunchbase, and PR newswires.

If funding found in last 90 days, return:
{
  "funded": true,
  "amount": "$X million",
  "round": "Series X",
  "date": "YYYY-MM-DD",
  "source_url": "URL"
}

If no recent funding, return:
{"funded": false}
```

### Funding-Triggered Workflow

| Signal | Action | Timing |
|--------|--------|--------|
| Seed/Series A | Add to nurture | Within 1 week |
| Series B | SDR outreach | Within 3 days |
| Series C+ | AE direct outreach | Same day |

**Routing formula:**
```javascript
{{Round}} === "Series C" || {{Round}} === "Series D" || Number({{Amount}}.replace(/\D/g,"")) > 50000000
  ? "ae-team@company.com"
  : {{Round}} === "Series B"
    ? "sdr-team@company.com"
    : "nurture-queue@company.com"
```

---

## Hiring Signal Monitoring

### Hiring as a Buying Signal

| What They're Hiring | What It Means |
|---------------------|---------------|
| SDRs/AEs | Sales expansion, may need tools |
| Engineers | Building product, need dev tools |
| Marketers | Growth focus, need marketing tools |
| Operations | Scaling, need ops tools |
| Your competitor's roles | Active in your space |

### Setup: Job Posting Detection

**Claygent prompt:**
```
Search {{Company Name}}'s careers page and LinkedIn Jobs.
Find job postings for roles related to: {{Target Department}}

Return:
{
  "hiring": true/false,
  "open_roles": ["role 1", "role 2"],
  "total_openings": X,
  "source_url": "careers page URL"
}

If no relevant openings, return:
{"hiring": false}
```

### Hiring Volume Scoring

```javascript
const roles = Number({{Total Openings}}) || 0;
const isTargetDept = {{Target Department Hiring}};

roles > 10 && isTargetDept ? "High Hiring Signal" :
roles > 5 && isTargetDept ? "Medium Hiring Signal" :
roles > 0 && isTargetDept ? "Low Hiring Signal" :
"No Signal"
```

### Competitor Role Detection

**Prompt:**
```
Search job postings at {{Company Name}} for roles mentioning any of these keywords:
- {{Competitor 1 Name}}
- {{Competitor 2 Name}}
- {{Your Product Category}}

Return:
{
  "competitor_mentioned": true/false,
  "which_competitor": "name or null",
  "role_title": "job title",
  "posting_url": "URL"
}
```

---

## Technology Change Monitoring

### BuiltWith for Tech Stack

**Initial enrichment:**
- Run BuiltWith on target accounts
- Store current tech stack

**Periodic refresh (monthly):**
- Re-run BuiltWith
- Compare to stored values
- Flag changes

### Tech Change Detection Formula

```javascript
const oldTech = ({{Previous Tech Stack}} || "").split(",");
const newTech = ({{Current Tech Stack}} || "").split(",");

const added = newTech.filter(t => !oldTech.includes(t));
const removed = oldTech.filter(t => !newTech.includes(t));

added.length > 0 || removed.length > 0 
  ? `Added: ${added.join(", ") || "none"} | Removed: ${removed.join(", ") || "none"}`
  : "No changes"
```

### Competitor Detection

**Check if using competitor:**
```javascript
const tech = ({{Tech Stack}} || "").toLowerCase();
const competitors = ["competitor1", "competitor2", "competitor3"];

competitors.filter(c => tech.includes(c)).join(", ") || "None detected"
```

**Check if added your integration:**
```javascript
const tech = ({{Tech Stack}} || "").toLowerCase();
const integrations = ["slack", "salesforce", "hubspot"]; // Your integrations

integrations.filter(i => tech.includes(i)).join(", ") || "None"
```

---

## News and Press Monitoring

### Claygent News Search

**Prompt:**
```
Search for recent news about {{Company Name}} in the last 30 days.
Sources: Google News, PR Newswire, Business Wire, TechCrunch.

Look for:
- Funding announcements
- Product launches
- Executive changes
- Partnerships
- Awards/recognition

Return the most significant news item:
{
  "has_news": true/false,
  "headline": "summary",
  "category": "funding/product/executive/partnership/other",
  "date": "YYYY-MM-DD",
  "source_url": "URL"
}
```

### News-Triggered Actions

| News Category | Action | Personalization |
|---------------|--------|-----------------|
| Funding | SDR outreach | Congratulate on raise |
| Product Launch | Marketing nurture | Reference new product |
| Executive Change | Wait 30 days, then reach out | Welcome new exec |
| Partnership | Research synergy | Reference partner |

---

## Signal Orchestration

### Combining Multiple Signals

**Composite signal score:**
```javascript
let signalScore = 0;

// Job change: +30
if ({{Champion Job Change}}) signalScore += 30;

// Recent funding: +25
if ({{Funding Last 90 Days}}) signalScore += 25;

// Hiring in target dept: +20
if ({{Target Dept Hiring}} === "High Hiring Signal") signalScore += 20;
else if ({{Target Dept Hiring}} === "Medium Hiring Signal") signalScore += 10;

// Tech change: +15
if ({{Added Competitor Tech}}) signalScore += 15;

// Recent news: +10
if ({{Has Recent News}}) signalScore += 10;

signalScore
```

### Signal-Based Routing

```javascript
{{Signal Score}} >= 50 ? "hot-leads@company.com" :
{{Signal Score}} >= 30 ? "warm-leads@company.com" :
{{Signal Score}} >= 10 ? "nurture@company.com" :
"no-action"
```

---

## End-to-End Example: Champion Tracking Program

**Goal:** Track 500 former champions for expansion

**Setup:**

| Column | Source | Purpose |
|--------|--------|---------|
| Contact Name | CRM Export | Champion info |
| LinkedIn URL | CRM Export | For monitoring |
| Former Company | CRM Export | Reference |
| Job Change Status | Clay Monitor | Detection |
| New Company | Clay Monitor | Where they went |
| New Company Domain | Claygent | Lookup |
| New Company Data | Clearbit | Qualification |
| New ICP Score | Formula | Fit score |
| New Work Email | Waterfall | Contact info |
| Assigned Rep | Formula | Routing |
| Slack Alert | Slack | Notification |

**Expected results:**
- ~15% job change rate annually (75 champions)
- ~60% go to ICP-fit companies (45 opportunities)
- Average deal value: $50K
- **Pipeline potential: $2.25M**

**Credit budget:**
- Monitoring: Native feature (no additional credits)
- Enrichment on changes: 75 × 15 credits = 1,125 credits/year
- **ROI: Extremely high**
