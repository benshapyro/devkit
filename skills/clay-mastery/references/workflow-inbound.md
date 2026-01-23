# Inbound Lead Automation Workflow

Workflow for capturing inbound leads, enriching them, scoring for qualification, and routing to sales.

## Workflow Overview

```
Form Capture → Enrichment → Scoring → Routing → CRM Sync → Notification
```

---

## Step 1: Lead Source Integration

### Webhook Setup (Most Common)

1. Create new Clay table
2. Select "Webhook" as data source
3. Copy the unique webhook URL
4. Configure your form/tool to POST to this URL

### Supported Sources

| Source | Integration Method |
|--------|-------------------|
| Typeform | Native webhook |
| Webflow Forms | Zapier → Clay webhook |
| HubSpot Forms | HubSpot workflow → webhook |
| Calendly | Zapier/native webhook |
| Intercom | Zapier → Clay webhook |
| Custom forms | Direct POST to webhook |

### Webhook Payload Mapping

Clay auto-creates columns from webhook JSON keys:

```json
{
  "email": "john@company.com",
  "first_name": "John",
  "last_name": "Smith",
  "company": "Acme Inc",
  "phone": "555-123-4567",
  "message": "Interested in demo"
}
```

Each key becomes a column automatically.

---

## Step 2: Speed-to-Lead Enrichment

### Minimal Viable Enrichment (Fast Response)

For immediate acknowledgment, enrich only essentials:

| Column | Enrichment | Purpose |
|--------|------------|---------|
| Domain | Extract from email | Base for company lookup |
| Company Name | Clearbit | If not provided |
| Is Business Email | Formula | Filter personal emails |

**Domain extraction formula:**
```javascript
{{Email}}.split("@").pop().toLowerCase()
```

**Business email check:**
```javascript
!["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com"].includes({{Domain}})
```

### Full Enrichment (For Qualification)

After fast response, run complete enrichment:

| Column | Enrichment | Credits | Conditional |
|--------|------------|---------|-------------|
| Company Data | Clearbit Enrich | 8 | If business email |
| LinkedIn Profile | Enrich from Email | 2 | If business email |
| Tech Stack | BuiltWith | 2 | If target industry |
| Intent Signals | Bombora | Varies | If enterprise |

---

## Step 3: Lead Scoring

### Point-Based Scoring Model

```javascript
let score = 0;

// Company size (30 points max)
const emp = Number({{Employee Count}}) || 0;
score += emp >= 100 && emp <= 1000 ? 30 :
         emp >= 50 ? 20 :
         emp >= 10 ? 10 : 0;

// Title seniority (25 points max)
const title = ({{Title}} || "").toLowerCase();
score += title.match(/chief|ceo|cto|cfo|coo|president/) ? 25 :
         title.match(/vp|vice president/) ? 20 :
         title.match(/director|head/) ? 15 :
         title.match(/manager|lead/) ? 10 : 5;

// Industry fit (20 points max)
score += ["Technology", "SaaS", "Software"].includes({{Industry}}) ? 20 :
         ["Professional Services", "Finance"].includes({{Industry}}) ? 15 : 5;

// Data completeness (15 points max)
score += {{Phone}} ? 5 : 0;
score += {{LinkedIn URL}} ? 5 : 0;
score += {{Company Website}} ? 5 : 0;

// Business email bonus (10 points)
score += {{Is Business Email}} ? 10 : 0;

score
```

### AI-Assisted Scoring

**Prompt:**
```
Score this inbound lead from 0-100 based on fit for a B2B SaaS company.

Lead Info:
- Name: {{First Name}} {{Last Name}}
- Email: {{Email}}
- Company: {{Company Name}}
- Title: {{Title}}
- Employee Count: {{Employee Count}}
- Industry: {{Industry}}
- Message: {{Form Message}}

Scoring criteria:
- Company size 50-1000 employees: High fit
- Title is decision-maker: High fit
- Expressed clear intent: High fit
- Personal email: Low fit

Return only a number from 0-100.
```

### Score Thresholds

| Score | Grade | Action |
|-------|-------|--------|
| 80-100 | A | Immediate SDR follow-up |
| 60-79 | B | SDR follow-up within 24h |
| 40-59 | C | Marketing nurture sequence |
| 0-39 | D | Low priority / disqualify |

---

## Step 4: Lead Routing

### Round-Robin Assignment

**Formula for 3 SDRs:**
```javascript
const reps = ["rep1@company.com", "rep2@company.com", "rep3@company.com"];
const index = {{Row Number}} % reps.length;
reps[index]
```

### Territory-Based Routing

**Formula:**
```javascript
{{State}} === "CA" || {{State}} === "WA" || {{State}} === "OR" ? "west@company.com" :
{{State}} === "NY" || {{State}} === "MA" || {{State}} === "NJ" ? "east@company.com" :
{{State}} === "TX" || {{State}} === "FL" || {{State}} === "GA" ? "south@company.com" :
"central@company.com"
```

### Score-Based Routing

**Formula:**
```javascript
{{Lead Score}} >= 80 ? "senior-ae@company.com" :
{{Lead Score}} >= 60 ? "sdr-team@company.com" :
"nurture-queue@company.com"
```

---

## Step 5: CRM Sync

### HubSpot Integration

**Workflow:**
1. Lookup Contact by Email
2. If exists → Update Contact
3. If not exists → Create Contact
4. Create/Update Company
5. Associate Contact to Company

**Field mapping:**
```
email → email
{{First Name}} → firstname
{{Last Name}} → lastname
{{Phone}} → phone
{{Title}} → jobtitle
{{Lead Score}} → lead_score (custom)
{{Assigned Rep}} → hubspot_owner_id
{{Form Source}} → lead_source
```

### Salesforce Integration

**Workflow:**
1. Lookup Lead by Email (SOQL)
2. Upsert Lead record
3. Trigger Salesforce lead assignment rules

**SOQL for lookup:**
```sql
SELECT Id, Email FROM Lead WHERE Email = '{{Email}}'
```

---

## Step 6: Notifications

### Slack Notification for Hot Leads

**Setup:**
1. Add Enrichment → Slack → Send Message
2. Conditional: `{{Lead Score}} >= 80`
3. Configure message template

**Message template:**
```
🔥 *Hot Inbound Lead*

*Name:* {{First Name}} {{Last Name}}
*Company:* {{Company Name}} ({{Employee Count}} employees)
*Title:* {{Title}}
*Score:* {{Lead Score}}
*Email:* {{Email}}

*Message:* {{Form Message}}

Assigned to: {{Assigned Rep}}
```

### Email Notification

**Setup:**
1. Add Enrichment → Gmail/Outlook → Send Email
2. To: {{Assigned Rep}}
3. Subject: "New Lead: {{Company Name}} - Score: {{Lead Score}}"

---

## End-to-End Example: Demo Request Automation

**Trigger:** Demo request form submission

**Table Structure:**

| Column | Type | Conditional |
|--------|------|-------------|
| Email | Webhook input | - |
| First Name | Webhook input | - |
| Company | Webhook input | - |
| Domain | Formula | - |
| Is Business Email | Formula | - |
| Company Data | Clearbit | If business email |
| Lead Score | Formula | - |
| Lead Grade | Formula | - |
| Assigned Rep | Formula | Based on territory |
| HubSpot Lookup | HubSpot | - |
| HubSpot Create/Update | HubSpot | Based on lookup |
| Slack Notification | Slack | If score >= 70 |
| Calendly Link | Formula | Personalized booking link |
| Auto-Response | Gmail | Immediate |

**Auto-response email:**
```
Hi {{First Name}},

Thanks for requesting a demo! Based on your needs, I've assigned 
{{Assigned Rep Name}} to help you.

Book a time that works: {{Calendly Link}}

Looking forward to connecting!
```

**Expected flow:**
- Lead submits form → 
- Clay enriches (2-5 seconds) → 
- Score calculated → 
- CRM updated → 
- Slack alert sent → 
- Auto-response email sent
- **Total time: <30 seconds**
