# Tech Stack Survey

Client technology inventory tool for capturing and researching their software landscape.

**Full SOP:** See `assets/sops/tech-stack-survey-sop.md` for complete step-by-step instructions.

---

## Contents

1. [Overview](#overview)
2. [Workflows](#workflows)
3. [Operational Details](#operational-details)
4. [Workflow 1: Present Survey Questions](#workflow-1-present-survey-questions)
5. [Workflow 2: Provide Blank Template](#workflow-2-provide-blank-template)
6. [Workflow 3: Parse Survey Responses](#workflow-3-parse-survey-responses)
7. [Workflow 4: Research API/Integrations](#workflow-4-research-apiintegrations)
8. [Workflow 5: Migrate to Discovery Catalog](#workflow-5-migrate-to-discovery-catalog)
9. [Artifact Generation](#artifact-generation)
10. [Tools Library Integration](#tools-library-integration)
11. [Error Handling](#error-handling)

---

## Overview

The Tech Stack Survey has two components:

1. **Kickoff Survey** — Google Form questions to send to clients
2. **Tech Stack Grid** — Excel data grid to organize and enrich responses

**Template:** `assets/templates/tech-stack-survey-template.xlsx`

**Responsibility Split:**

| Columns | Who | What |
|---------|-----|------|
| A-G | Client | Tool Name, Purpose, Department, Owner, Users, Cost, Vendor |
| H+ | Cadre (Claude) | API, Upstream, Downstream, Connection Method, Notes |

---

## Workflows

| Command | Action |
|---------|--------|
| `/techstack survey` | Output Google Form questions |
| `/techstack template` | Provide blank Excel template |
| `/techstack parse` | Parse survey responses into grid |
| `/techstack research [client]` | Research and fill API/integration columns |
| `/techstack migrate [client]` | Promote to Discovery Catalog (4_Technology table) |

**Natural language triggers:**
- "tech stack survey questions"
- "parse these survey responses"
- "research the integrations for [client]'s tools"
- "fill in the API info for this tech stack"
- "what tools does [client] use"

---

## Operational Details

### When to Deploy

**Every engagement, at or around kickoff.** Don't wait until you think you need it.

### Who to Send It To

During discovery, ask: "Who on your team knows your tech stack best — tools, costs, who owns what?"

Send survey to that person, cc your champion if different.

### Email Template

**Subject:** Tech Stack Survey — [Client Name]

> Hi [Name],
>
> As part of our discovery, we're mapping out your technology stack to identify integration and automation opportunities.
>
> Attached is a short survey. Could you fill in columns A through G for each tool your team uses? We'll research the technical details (API, integrations, etc.) on our end.
>
> If you can get this back to us within the week, that would be great — the sooner we have it, the more we can prepare for our next conversation.
>
> Questions? Just reply to this email.
>
> Thanks!

### Turnaround Time

**Within a week, sooner is better.** Follow up at 5 days if not received.

### Handling Partial Responses

Accept what you get. Don't send it back for corrections.
- Research what you can
- Ask specific gaps in next call: "You mentioned Salesforce but we didn't see a marketing automation tool — do you use one?"

### File Location & Naming

```
Cadre Team Drive /
└── Clients /
    └── [Client Name] /
        ├── Tech Stack Survey.xlsx
        └── Deliverables /
            └── Tech Stack Overview.html
```

---

## Workflow 1: Present Survey Questions

### When triggered

User says `/techstack survey`, "give me the tech stack questions", "survey for [client]"

### Steps

1. **Ask for client name** (if not provided)

2. **Present the questions** in a clean, copy-pasteable format:

```markdown
## Tech Stack Inventory Survey

**For:** [Client Name]

Copy these questions into a Google Form:

---

**Form Title:** [Client Name] Tech Stack Inventory

**Form Description:**
Help us understand your current technology landscape. This survey takes 5-7 minutes and will help us provide better AI enablement recommendations.

---

### Questions

| # | Question | Type | Required |
|---|----------|------|----------|
| 1 | Your Name | Short answer | Yes |
| 2 | Your Role/Title | Short answer | Yes |
| 3 | Your Email | Short answer | Yes |
| 4 | Company Name | Short answer | Yes |
| 5 | List all software tools and platforms your company currently uses (one per line) | Paragraph | Yes |
| 6 | For each tool listed above, indicate the primary department(s) that use it | Paragraph | Yes |
| 7 | Who is the primary owner/champion for each tool? (e.g., IT Manager, Sales Director) | Paragraph | Yes |
| 8 | Approximately how many employees use each tool? | Paragraph | No |
| 9 | What is the approximate annual cost for each tool? (if known) | Paragraph | No |
| 10 | Are there any tools you wish you had but currently don't? | Paragraph | No |
| 11 | Are there any tools you plan to replace or eliminate soon? | Paragraph | No |
| 12 | Any additional context about your tech stack we should know? | Paragraph | No |
| 13 | Who on your team has the best knowledge of how these tools connect to each other? | Short answer | No |

---

**Next Steps:**
1. Export responses to Google Sheet
2. Import tool list into Tech Stack Grid  
3. Run `/techstack research [client]` to fill technical columns
```

3. **Offer the email template**

4. **Offer customization:** "Want me to add any custom questions?"

---

## Workflow 2: Provide Blank Template

### When triggered

User says `/techstack template`, "blank tech stack template", "empty tech inventory spreadsheet"

### Steps

1. Copy and present `assets/templates/tech-stack-survey-template.xlsx`

2. Explain the columns:

| Column | Client Fills | Claude Researches |
|--------|--------------|-------------------|
| A: Tool/System Name | ✓ | |
| B: Primary Use/Purpose | ✓ | |
| C: Primary Department(s) | ✓ | |
| D: Tool Owner/Champion | ✓ | |
| E: # of Users | ✓ | |
| F: Annual Cost | ✓ | |
| G: Vendor/Provider | ✓ (or Claude) | |
| H: Has API? | | ✓ |
| I: Upstream Tools | | ✓ |
| J: Downstream Tools | | ✓ |
| K: Connection Method | | ✓ |
| L: Data Transferred | | ✓ |
| M: Notes | | ✓ |
| N: Research Confidence | | ✓ |

---

## Workflow 3: Parse Survey Responses

### When triggered

User says `/techstack parse`, pastes paragraph text, or uploads CSV/XLSX from Google Forms

### Input formats accepted

**Format A: Pasted paragraphs**
```
Tools: Salesforce, HubSpot, Slack, QuickBooks, Asana
Departments: Sales uses Salesforce and HubSpot. Marketing uses HubSpot...
```

**Format B: CSV/XLSX from Google Forms**
Standard export with columns matching survey questions

### Steps

1. Detect input format (paragraph vs structured)
2. Extract tool names (one per line or comma-separated)
3. Match departments, owners, users, costs to each tool
4. Handle ambiguity by asking clarifying questions
5. Output to Tech Stack Grid format (Excel)

### Output

Populated Excel with columns A-G filled. Present and offer:

> "I've parsed [X] tools into the grid. Ready to research API and integration details? Say `/techstack research [client]`"

---

## Workflow 4: Research API/Integrations

### When triggered

User says `/techstack research [client]`, "research the integrations", "fill in the API info", or uploads partially-filled Excel

### Steps

See `tech-stack-research.md` for detailed research process.

**Summary:**

1. Load Excel, identify tools needing research
2. For each tool:
   - Check Tools Library (Airtable) first
   - If not found, web search vendor docs
   - Infer upstream/downstream from tool category
3. Fill columns H-N
4. Present summary with confidence levels

### Research priority order

1. **Airtable Tools Library** — Check if tool exists in our database first
2. **Official vendor documentation** — API docs, integration pages
3. **Integration directories** — Zapier, Make, n8n listings
4. **Web search** — General search for gaps

### Output modes

**Default:** Fill Excel + show summary

**Verbose (`/techstack research [client] verbose`):** Show research findings per tool, ask for confirmation, then write to Excel

### Output format

```markdown
**Tech Stack Research Complete**

**Summary:**
- Tools researched: 12
- API availability confirmed: 9 (75%)
- Integration data found: 8 (67%)
- Needs manual research: 3

**Low confidence items (review recommended):**
| Tool | Field | Issue |
|------|-------|-------|
| CustomApp | API | No public documentation found |

[Download: tech-stack-acme-2024-12.xlsx]

**Next steps:**
- Review low-confidence items
- `/techstack migrate [client]` to add to Discovery Catalog
- `/artifact overview [client]` to generate Tech Stack Overview
```

---

## Workflow 5: Migrate to Discovery Catalog

### When triggered

User says `/techstack migrate [client]`, "add this to the discovery catalog", "promote tech stack to Airtable"

### Steps

1. Read Tech Stack Grid
2. Get client record ID from Discovery Catalog
3. For each tool row:
   - Check if tool exists in 4_Technology table
   - If exists: Update record
   - If new: Create record
4. Report created/updated counts

### Field mapping

| Tech Stack Grid | 4_Technology Field |
|-----------------|-------------------|
| Tool/System Name | Tool Name |
| Primary Use/Purpose | Purpose |
| Primary Department(s) | Department (link) |
| Tool Owner/Champion | Owner |
| # of Users | User Count |
| Annual Cost | Annual Cost |
| Vendor/Provider | Vendor |
| Does the tool have an official API? | Has API |
| Connection Method | Integration Type |
| Notes/Additional Context | Notes |

---

## Artifact Generation

After research is complete, offer artifact generation:

| Command | Artifact | Format |
|---------|----------|--------|
| `/artifact overview [client]` | Tech Stack Overview | HTML (Client Portal compatible) |
| `/artifact map [client]` | Integration Map | JSX (say "convert to HTML" for Portal) |

See `synthesis/data-to-artifact.md` for generation instructions.

---

## Tools Library Integration

Before web research, check Cadre's internal Tools Library:

**Base:** Tools Library  
**Base ID:** `appAE0wZaiOOzwOvE`  
**Table:** Tools Database  
**Table ID:** `tblUHZDNtmHL73lSn`

**Query by tool name:**
```
filterByFormula: {Tool Name} = '[tool_name]'
```

**Fields to pull:**

| Tools Library Field | Maps To |
|--------------------|---------|
| Has API | Does the tool have an official API? |
| API Documentation | Source URL for API info |
| Integrations | Parse for upstream/downstream |
| One-Line Description | Notes/Additional Context |
| Research Confidence | Inherit confidence level |
| Company Name | Vendor/Provider (if missing) |

**If tool not in Tools Library:** Proceed to web research, then optionally add to Tools Library for future use.

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Tool not found in any source | "Unknown - needs manual research" |
| Ambiguous tool name (e.g., "Office") | Ask: "Did you mean Microsoft Office, LibreOffice, or something else?" |
| Multiple tools with same name | Show options with vendor names |
| Survey response missing tool list | Ask user to provide tool names |
| Excel template structure mismatch | Ask user to use standard template |
| Airtable connection unavailable | Skip Tools Library, proceed to web research |
