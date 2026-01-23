# Outbound Prospecting Workflow

Complete workflow for building prospect lists, enriching data, and pushing to sequencers.

## Workflow Overview

```
List Building → ICP Filter → Company Enrichment → Contact Finding → 
Contact Enrichment → Personalization → Sequencer Export
```

---

## Step 1: List Building Methods

### LinkedIn Sales Navigator Import

**Best for:** B2B prospecting, targeted lists

**Setup:**
1. Create "Find People" table
2. Select "External List" import method
3. Paste Sales Navigator search URL
4. Import (1 credit per row, max 2,500 results)

**Auto-created columns:** Name, LinkedIn Profile URL, Company Name, Title

**Tips:**
- Build search in Sales Nav first, refine until satisfied
- Use Boolean search for precise targeting
- Save search for future imports

### Google Maps (Local Businesses)

**Best for:** Local services, SMB prospecting

**Setup:**
1. Add Enrichment → Google Maps → Search Places
2. Input: search query + location
3. Output: Business name, address, phone, website, rating

**Example query:** `"dentist in San Diego, CA"`

### Job Board Scraping

**Best for:** Hiring companies (buying signal)

**Setup:**
1. Add Enrichment → Claygent
2. Provide job board URL (Indeed, LinkedIn Jobs)
3. Extract: Company name, job title, location

### CRM Export

**Best for:** Re-engaging existing database

**Setup:**
1. Add Enrichment → HubSpot/Salesforce → Import
2. Filter: Last contact > 90 days, Status = Open
3. Import relevant fields

### Custom Sources (HTTP API)

**Best for:** Proprietary data sources

**Setup:**
1. Add Enrichment → HTTP API
2. Configure endpoint, headers, parameters
3. Parse response with formula

---

## Step 2: ICP Filtering

**Goal:** Remove non-ICP records BEFORE expensive enrichments.

### Company-Level Filters (Run First)

```javascript
// Company size filter
{{Employee Count}} >= 50 && {{Employee Count}} <= 500

// Industry filter
["Technology", "Healthcare", "Finance"].includes({{Industry}})

// Geography filter
["CA", "NY", "TX"].includes({{State}})
```

### Create ICP Score Column

```javascript
let score = 0;
score += {{Employee Count}} >= 100 && {{Employee Count}} <= 500 ? 30 : 0;
score += ["Technology", "SaaS"].includes({{Industry}}) ? 25 : 0;
score += ["United States", "US"].includes({{Country}}) ? 20 : 0;
score += {{Funding}} ? 25 : 0;
score
```

### Filter View

1. Create new view
2. Add filter: ICP Score >= 60
3. Run subsequent enrichments on this view only

---

## Step 3: Company Enrichment

### Recommended Sequence

| Column | Enrichment | Credits | Purpose |
|--------|------------|---------|---------|
| Domain | Clearbit Find Domain | 0 | Company name → domain |
| Company Data | Clearbit Enrich | 8 | Firmographics |
| Tech Stack | BuiltWith | 2 | Technologies used |
| Funding | Harmonic | 3 | Startup funding data |

### Conditional Runs

```javascript
// Only run Clearbit Enrich if domain found
{{Domain}} && {{Domain}} !== ""

// Only run BuiltWith if tech matters for ICP
{{Industry}} === "Technology" && {{Domain}}
```

---

## Step 4: Contact Finding

### Find Decision Makers

**Option A: Apollo People Search**
- Input: Company domain + title keywords
- Output: Contact name, title, LinkedIn URL
- Credits: 3

**Option B: Claygent LinkedIn Search**
```
Find the {{Target Title}} at {{Company Name}}.
Search LinkedIn for this person.
Return: Full name, LinkedIn URL, exact title.
If multiple matches, return the most senior person.
```

### Common Target Titles by Persona

| Persona | Title Keywords |
|---------|----------------|
| Sales Leader | VP Sales, Head of Sales, CRO, Sales Director |
| Marketing Leader | CMO, VP Marketing, Head of Marketing |
| Tech Leader | CTO, VP Engineering, Head of Engineering |
| Operations | COO, VP Operations, Head of Ops |
| Finance | CFO, VP Finance, Controller |

---

## Step 5: Contact Enrichment

### Email Waterfall

**Recommended sequence:**
```
Prospeo (2) → Dropcontact (2) → Datagma (2) → Hunter (2) → 
Apollo (3) → People Data Labs (5) → ZeroBounce (included)
```

**Conditional:** Only run if contact was found
```javascript
{{Contact Name}} && {{LinkedIn URL}}
```

### Phone Waterfall (Optional)

**Recommended sequence:**
```
Apollo (3) → Lusha (4) → RocketReach (10)
```

**Conditional:** Only for high-value leads
```javascript
{{Email}} && {{ICP Score}} >= 80
```

---

## Step 6: Personalization

### AI Personalization Column

**Prompt:**
```
Write a personalized one-liner for a cold email opener.

Context:
- Recipient: {{First Name}}, {{Title}} at {{Company Name}}
- Company focus: {{Company Description}}
- Their LinkedIn: {{LinkedIn URL}}

Rules:
- Reference something specific about them or their company
- Keep under 20 words
- Don't mention your product
- Sound human, not salesy
- If no specific info, return "skip"

Output the one-liner only.
```

### Personalization Angles

| Data Point | Prompt Focus |
|------------|--------------|
| Recent funding | "Congrats on the Series B..." |
| Job posting | "Saw you're hiring for..." |
| News mention | "Read about your..." |
| Company growth | "Impressive growth at..." |
| Mutual connection | "We both know..." |

---

## Step 7: Sequencer Export

### Smartlead Setup

1. Get API key from Smartlead settings
2. Add to Clay: Settings → Connections → Smartlead
3. Create campaign in Smartlead with variables:
   - `{{first_name}}`
   - `{{company}}`
   - `{{personalization}}`
4. In Clay: Add Enrichment → Smartlead → Add Lead
5. Map columns to campaign variables

### Instantly Setup

1. Get API key from Instantly workspace settings
2. Add to Clay: Settings → Connections → Instantly
3. Create campaign with placeholder variables
4. In Clay: Add Enrichment → Instantly → Add Lead to Campaign
5. Map: email, first_name, company, custom fields

### Apollo Sequencing

**Note:** Apollo integration is primarily for enrichment. For sequencing:
1. Export Clay table as CSV
2. Import to Apollo
3. Add to Apollo sequence

### Column Mapping Template

| Sequencer Variable | Clay Column |
|-------------------|-------------|
| email | {{Email}} |
| first_name | {{First Name}} |
| last_name | {{Last Name}} |
| company | {{Company Name}} |
| title | {{Title}} |
| personalization | {{AI Snippet}} |
| linkedin_url | {{LinkedIn URL}} |

---

## End-to-End Example: B2B SaaS Outbound

**Target:** VP Sales at SaaS companies, 50-500 employees, US

**Table Structure:**

| Column | Type | Notes |
|--------|------|-------|
| Full Name | Import | From Sales Nav |
| Company | Import | From Sales Nav |
| LinkedIn URL | Import | From Sales Nav |
| Domain | Clearbit | Free |
| Employee Count | Clearbit Enrich | Conditional: if Domain |
| Industry | Clearbit Enrich | Same enrichment |
| ICP Score | Formula | Free |
| Work Email | Waterfall | Conditional: if ICP >= 60 |
| AI Snippet | Claygent | Conditional: if Email |
| Sequencer Status | Smartlead | Push qualified leads |

**Expected metrics:**
- 1,000 Sales Nav imports: 1,000 credits
- 800 pass ICP filter
- 600 emails found (75% coverage): ~1,800 credits
- 600 personalization: 600 credits
- **Total: ~3,400 credits for 600 ready-to-sequence leads**
