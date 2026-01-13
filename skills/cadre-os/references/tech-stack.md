# Tech Stack Reference

Complete guide for client technology inventory: surveying, researching, and tracking software tools.

## Table of Contents

- [Tech Stack Survey](#tech-stack-survey)
  - [Overview](#overview)
  - [Workflows](#workflows)
  - [Operational Details](#operational-details)
  - [Workflow 1: Present Survey Questions](#workflow-1-present-survey-questions)
  - [Workflow 2: Provide Blank Template](#workflow-2-provide-blank-template)
  - [Workflow 3: Parse Survey Responses](#workflow-3-parse-survey-responses)
  - [Workflow 4: Research API/Integrations](#workflow-4-research-apiintegrations)
  - [Workflow 5: Migrate to Discovery Catalog](#workflow-5-migrate-to-discovery-catalog)
  - [Artifact Generation](#artifact-generation)
- [Tech Stack Research](#tech-stack-research)
  - [Research Overview](#research-overview)
  - [Step 1: Load and Parse Input](#step-1-load-and-parse-input)
  - [Step 2: Check Tools Library First](#step-2-check-tools-library-first)
  - [Step 3: Web Research for Gaps](#step-3-web-research-for-gaps)
  - [Step 4: Infer Integration Directions](#step-4-infer-integration-directions)
  - [Step 5: Infer Connection Method](#step-5-infer-connection-method)
  - [Step 6: Infer Data Transferred](#step-6-infer-data-transferred)
  - [Step 7: Write to Excel](#step-7-write-to-excel)
  - [Step 8: Present Results](#step-8-present-results)
- [Tools Library](#tools-library)
  - [Connection Details](#connection-details)
  - [Schema](#schema)
  - [Query Examples](#query-examples)
  - [Adding New Tools](#adding-new-tools)
- [Error Handling](#error-handling)

---

# Tech Stack Survey

Client technology inventory tool for capturing and researching their software landscape.

**Full SOP:** See `assets/sops/tech-stack-survey-sop.md` for complete step-by-step instructions.

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

See [Tech Stack Research](#tech-stack-research) section below for detailed research process.

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

> **Related:** See [data-schema.md](data-schema.md#4_technology) for full 4_Technology table schema.

---

## Artifact Generation

After research is complete, offer artifact generation:

| Command | Artifact | Format |
|---------|----------|--------|
| `/artifact overview [client]` | Tech Stack Overview | HTML (Client Portal compatible) |
| `/artifact map [client]` | Integration Map | JSX (say "convert to HTML" for Portal) |

> **Related:** See [synthesis.md](synthesis.md#data-to-artifact-generation) for generation instructions.

---

# Tech Stack Research

Step-by-step process for researching and populating the Tech Stack Survey grid.

## Research Overview

```
Partially-filled Excel (cols A-F)
  → Check Tools Library (Airtable)
  → Research gaps (web)
  → Infer directions
  → Write to Excel (cols G-O)
  → Present with confidence
```

---

## Step 1: Load and Parse Input

### Accept Excel file
```python
from openpyxl import load_workbook

wb = load_workbook('tech-stack-client.xlsx')
ws = wb['Tech Stack  Survey']  # Note: two spaces in sheet name

# Skip header row, get tool data
tools = []
for row in ws.iter_rows(min_row=2, values_only=True):
    if row[0]:  # Tool name exists
        tools.append({
            'name': row[0],
            'purpose': row[1],
            'departments': row[2],
            'owner': row[3],
            'users': row[4],
            'cost': row[5],
            'vendor': row[6],
            # Columns 7-12 to be researched
        })
```

---

## Step 2: Check Tools Library First

For each tool, query Airtable before web research:

```python
def check_tools_library(tool_name):
    """
    Query Tools Library for existing research.
    Returns dict with fields or None if not found.
    """
    # Search with exact match first
    results = airtable_search(
        base_id='appAE0wZaiOOzwOvE',
        table_id='tblUHZDNtmHL73lSn',
        filter=f"{{Tool Name}} = '{tool_name}'"
    )

    if not results:
        # Try fuzzy match
        results = airtable_search(
            base_id='appAE0wZaiOOzwOvE',
            table_id='tblUHZDNtmHL73lSn',
            filter=f"FIND('{tool_name.lower()}', LOWER({{Tool Name}})) > 0"
        )

    if results:
        record = results[0]
        return {
            'has_api': record.get('Has API', False),
            'api_docs': record.get('API Documentation'),
            'integrations': record.get('Integrations', ''),
            'description': record.get('One-Line Description', ''),
            'vendor': record.get('Company Name', ''),
            'category': record.get('Primary Category', ''),
            'confidence': record.get('Research Confidence', 'Medium'),
            'source': 'Tools Library'
        }

    return None
```

---

## Step 3: Web Research for Gaps

If tool not in Tools Library, research in priority order:

### 3a. Official Vendor Documentation

```python
def search_vendor_docs(tool_name, vendor=None):
    """
    Search for official API documentation.
    """
    queries = [
        f"{tool_name} API documentation",
        f"{tool_name} developer docs",
        f"{tool_name} integrations",
    ]
    if vendor:
        queries.append(f"{vendor} {tool_name} API")

    # Web search and fetch results
    for query in queries:
        results = web_search(query)
        for result in results:
            if is_official_docs(result.url, tool_name, vendor):
                return {
                    'has_api': detect_api_availability(result.content),
                    'api_docs': result.url,
                    'confidence': 'High',
                    'source': result.url
                }

    return None

def is_official_docs(url, tool_name, vendor):
    """Check if URL is official documentation."""
    official_patterns = [
        f"{tool_name.lower()}.com",
        f"{vendor.lower()}.com" if vendor else None,
        "developer.", "docs.", "api.",
    ]
    return any(p and p in url.lower() for p in official_patterns)
```

### 3b. Integration Directories

```python
def search_integration_directories(tool_name):
    """
    Search Zapier, Make, n8n for integration info.
    """
    directories = [
        f"site:zapier.com/apps {tool_name}",
        f"site:make.com/en/integrations {tool_name}",
        f"site:n8n.io/integrations {tool_name}",
    ]

    integrations = []
    for query in directories:
        results = web_search(query)
        if results:
            # Parse integration partners from results
            partners = extract_integration_partners(results[0].content)
            integrations.extend(partners)

    return {
        'integrations': list(set(integrations)),
        'confidence': 'Medium',
        'source': 'Integration directories'
    }
```

### 3c. General Web Search

```python
def search_web_general(tool_name):
    """
    Fallback to general web search.
    """
    results = web_search(f"{tool_name} API integrations")

    if results:
        # Extract what we can from snippets
        has_api = any(
            'API' in r.snippet and
            ('available' in r.snippet.lower() or 'documentation' in r.snippet.lower())
            for r in results
        )

        return {
            'has_api': has_api,
            'confidence': 'Low',
            'source': 'Web search'
        }

    return None
```

---

## Step 4: Infer Integration Directions

Parse the Integrations field and categorize as upstream/downstream:

```python
# Category → typical data flow direction
DIRECTION_MAP = {
    # Upstream (data sources)
    'CRM': 'upstream',
    'Sales': 'upstream',
    'Marketing': 'upstream',
    'E-commerce': 'upstream',
    'Forms': 'upstream',

    # Downstream (data consumers)
    'Communication': 'downstream',
    'Analytics': 'downstream',
    'Reporting': 'downstream',
    'Finance': 'downstream',
    'Accounting': 'downstream',

    # Bidirectional
    'Automation': 'both',
    'Project Management': 'both',
    'Collaboration': 'both',
    'Storage': 'both',
    'Data Management': 'both',
    'Development': 'both',
    'Productivity': 'both',
}

# Common tools with known directions
KNOWN_DIRECTIONS = {
    # Upstream (data sources)
    'Salesforce': 'upstream',
    'HubSpot': 'upstream',
    'Pipedrive': 'upstream',
    'Typeform': 'upstream',
    'Google Forms': 'upstream',
    'LinkedIn': 'upstream',
    'Shopify': 'upstream',
    'Stripe': 'upstream',

    # Downstream (data consumers)
    'Slack': 'downstream',
    'Email': 'downstream',
    'Microsoft Teams': 'downstream',
    'Tableau': 'downstream',
    'Looker': 'downstream',
    'QuickBooks': 'downstream',
    'Xero': 'downstream',

    # Bidirectional
    'Zapier': 'both',
    'Make': 'both',
    'n8n': 'both',
    'Google Sheets': 'both',
    'Airtable': 'both',
    'Notion': 'both',
    'Asana': 'both',
    'Jira': 'both',
    'GitHub': 'both',
}

def categorize_integrations(integrations_text, tool_category=None):
    """
    Parse integrations string and categorize by direction.

    Returns:
        upstream: list of tool names
        downstream: list of tool names
    """
    # Parse comma or newline separated
    tools = [t.strip() for t in re.split(r'[,\n]', integrations_text) if t.strip()]

    upstream = []
    downstream = []

    for tool in tools:
        # Check known directions first
        direction = KNOWN_DIRECTIONS.get(tool)

        if not direction:
            # Try to look up category in Tools Library
            category = lookup_tool_category(tool)
            direction = DIRECTION_MAP.get(category, 'both')

        if direction == 'upstream':
            upstream.append(tool)
        elif direction == 'downstream':
            downstream.append(tool)
        else:  # both
            upstream.append(tool)
            downstream.append(tool)

    return upstream, downstream
```

---

## Step 5: Infer Connection Method

```python
def infer_connection_method(tool_data):
    """
    Infer how tools are likely connected based on available info.
    """
    integrations = tool_data.get('integrations', '').lower()
    has_api = tool_data.get('has_api', False)

    # Check for iPaaS mentions
    if any(ipaas in integrations for ipaas in ['zapier', 'make', 'n8n', 'workato', 'tray']):
        return 'iPaaS (Integration Platform)'

    # Check for native integration signals
    if 'native' in integrations or 'built-in' in integrations:
        return 'Native Integration'

    # Check for webhook/API signals
    if has_api:
        return 'API/Webhook'

    # Check for manual signals
    if any(m in integrations for m in ['export', 'import', 'csv', 'manual']):
        return 'Manual Export/Import'

    return 'Unknown - needs manual research'
```

---

## Step 6: Infer Data Transferred

```python
def infer_data_transferred(tool_category, purpose):
    """
    Infer what type of data typically flows based on tool type.
    """
    DATA_BY_CATEGORY = {
        'CRM': 'Contacts, Deals, Activities',
        'Communication': 'Messages, Notifications',
        'Project Management': 'Tasks, Projects, Status Updates',
        'Analytics': 'Reports, Metrics, Dashboards',
        'Finance': 'Invoices, Transactions, Payments',
        'Marketing': 'Campaigns, Leads, Engagement Data',
        'HR': 'Employee Data, Time Tracking',
        'E-commerce': 'Orders, Products, Customers',
        'Development': 'Code, Issues, Deployments',
        'Storage': 'Files, Documents',
        'Automation': 'Triggers, Actions, Workflows',
    }

    if tool_category in DATA_BY_CATEGORY:
        return DATA_BY_CATEGORY[tool_category]

    # Try to infer from purpose
    purpose_lower = purpose.lower() if purpose else ''
    if 'crm' in purpose_lower or 'sales' in purpose_lower:
        return 'Contacts, Deals, Activities'
    if 'communication' in purpose_lower or 'chat' in purpose_lower:
        return 'Messages, Notifications'
    if 'project' in purpose_lower or 'task' in purpose_lower:
        return 'Tasks, Projects, Status Updates'

    return 'Unknown - needs manual research'
```

---

## Step 7: Write to Excel

```python
from openpyxl import load_workbook

def write_research_results(input_path, output_path, research_results):
    """
    Write research results to Tech Stack Survey Excel.

    research_results: list of dicts with keys:
        - row_num: Excel row number
        - has_api: Yes/No/Unknown
        - upstream: comma-separated string
        - downstream: comma-separated string
        - connection_method: string
        - data_transferred: string
        - notes: string
        - confidence: High/Medium/Low
        - sources: comma-separated URLs
    """
    wb = load_workbook(input_path)
    ws = wb['Tech Stack  Survey']

    # Add confidence and sources headers if not present
    if ws.cell(row=1, column=14).value != 'Research Confidence':
        ws.cell(row=1, column=14, value='Research Confidence')
    if ws.cell(row=1, column=15).value != 'Sources':
        ws.cell(row=1, column=15, value='Sources')

    for result in research_results:
        row = result['row_num']

        # Column 8: Does the tool have an official API?
        ws.cell(row=row, column=8, value=result.get('has_api', 'Unknown'))

        # Column 9: Upstream Tools (Inputs)
        ws.cell(row=row, column=9, value=result.get('upstream', ''))

        # Column 10: Downstream Tools (Outputs)
        ws.cell(row=row, column=10, value=result.get('downstream', ''))

        # Column 11: Connection Method
        ws.cell(row=row, column=11, value=result.get('connection_method', ''))

        # Column 12: Data Transferred
        ws.cell(row=row, column=12, value=result.get('data_transferred', ''))

        # Column 13: Notes/Additional Context (append, don't overwrite)
        existing_notes = ws.cell(row=row, column=13).value or ''
        new_notes = result.get('notes', '')
        if new_notes and new_notes not in existing_notes:
            ws.cell(row=row, column=13, value=f"{existing_notes}\n{new_notes}".strip())

        # Column 14: Research Confidence
        ws.cell(row=row, column=14, value=result.get('confidence', 'Low'))

        # Column 15: Sources
        ws.cell(row=row, column=15, value=result.get('sources', ''))

    wb.save(output_path)
    return output_path
```

---

## Step 8: Present Results

### Default output (confidence columns):

```markdown
Here's your **Tech Stack Survey** with research completed:

**Summary:**
- Tools researched: 12
- API availability confirmed: 9 (75%)
- Integration data found: 8 (67%)
- Needs manual research: 3

**Research sources used:**
- Tools Library: 4 tools found
- Vendor documentation: 6 tools
- Integration directories: 5 tools
- Web search: 2 tools

**Low confidence items (review recommended):**
| Tool | Field | Issue |
|------|-------|-------|
| CustomApp | API | No public documentation found |
| LegacySystem | Integrations | Vendor website outdated |

[Download: tech-stack-acme-researched.xlsx]
```

### Verbose output (show research first):

```markdown
## Research Results for Acme Corp Tech Stack

### 1. Salesforce
**Source:** Tools Library (High confidence)
- Has API: Yes
- API Docs: https://developer.salesforce.com/docs
- Integrations found: HubSpot, Slack, QuickBooks, Zapier, Gmail
- Inferred upstream: Website Forms, LinkedIn
- Inferred downstream: Slack, QuickBooks
- Connection method: Native Integration

### 2. QuickBooks Online
**Source:** Vendor docs + Zapier (Medium confidence)
- Has API: Yes
- API Docs: https://developer.intuit.com/
- Integrations found: Salesforce, Stripe, PayPal, Excel
- Inferred upstream: Salesforce, Bank Feeds
- Inferred downstream: Excel (reporting)
- Connection method: Native Integration

### 3. CustomApp
**Source:** Web search (Low confidence)
- Has API: Unknown - no public docs found
- Integrations: Unknown
- **Needs manual research**

---

Proceed with writing to Excel? (y/n)
```

---

# Tools Library

Cadre's internal database of researched software tools. Check here before web research.

## Connection Details

**Base:** Tools Library
**Base ID:** `appAE0wZaiOOzwOvE`

**Table:** Tools Database
**Table ID:** `tblUHZDNtmHL73lSn`

---

## Schema

| Field Name | Type | Field ID | Description |
|------------|------|----------|-------------|
| Tool Name | singleLineText | `fld9T5cjYQIXQ89DR` | Primary field |
| Tool URL | url | `fldIiJckfukFW413n` | Official website |
| Primary Category | singleSelect | `fldsZz0Muh9R5xEiJ` | See categories below |
| One-Line Description | multilineText | `fldrBnmd97StK3AdQ` | Brief description |
| Core Use Cases (JTBD) | multilineText | `fld0jeKd3v5DZDlMN` | Jobs-to-be-Done format |
| Company Name | singleLineText | `fldXnWGkrcdKoc4x4` | Vendor name |
| Pricing Model | singleLineText | `fld8wFjSvto2Dw57W` | Free/Freemium/Paid |
| Key Features | multilineText | `fldLnxlRSsn5liD6K` | Top 3-5 capabilities |
| Target Audience | singleLineText | `fldcIaY1esmvp3BVu` | Role @ company type |
| Differentiators | multilineText | `fld8gqOHcHeER3AO6` | What makes it unique |
| Security & Compliance | multilineText | `fldf1xCqvjOIRH8UN` | SOC2, GDPR, etc. |
| Alternative Tools | multilineText | `fldgY1InJPLWq7FmM` | 2-3 competitors |
| Reviews Summary | multilineText | `fldRzPYay0eoXekJj` | Pros/cons from G2, Capterra |
| Company Background | multilineText | `fldz1nQGAEq7LyGer` | Founded, funding, size |
| Integrations | multilineText | `fldwlMP5TiKzJasLp` | Major integrations (uncategorized) |
| Has API | checkbox | `fld4c6mu1BGTnv2yz` | Yes/No |
| API Documentation | url | `fldPMnjQF9xnhS2H0` | Link to API docs |
| Native ChatGPT | checkbox | `fldhgaeQhFW3WIGgs` | Has ChatGPT integration |
| Native Claude | checkbox | `fldd1K3ivrDvamVaw` | Has Claude integration |
| Native Gemini | checkbox | `fldX0HKivbQWlI37N` | Has Gemini integration |
| Native Copilot | checkbox | `fldIV0n7qDVj1nHLr` | Has Copilot integration |
| MCP Server | singleSelect | `fldTWjeUFiipwv5La` | Vendor Official / Community Only / None |
| MCP Server URL | url | `fldKeZgztsGCBseij` | Link to MCP server |
| Research Confidence | singleSelect | `fldWLvUUcVC75m4JF` | High / Medium / Low |
| Research Notes | multilineText | `fldJsW1b5JQ7Yv0JP` | Gaps, follow-ups |
| Submitted By | singleLineText | `fld8jd8cjmoUxC2If` | Slack username |
| Submitted At | dateTime | `fld4P26rAzNpKwk2G` | Timestamp |
| User Notes | multilineText | `fldSjebjkYs3n5n2x` | Original submission notes |

---

### Primary Category Options

- CRM
- Project Management
- Analytics
- AI Assistant
- Automation
- Communication
- Design
- Development
- Marketing
- Sales
- HR
- Finance
- Operations
- Data Management
- Security
- Productivity
- Customer Support
- E-commerce
- Collaboration
- Uncategorized

---

### MCP Server Options

| Value | Meaning |
|-------|---------|
| Vendor Official | Official MCP server from the vendor |
| Community Only | Community-maintained MCP server |
| None | No MCP server available |

---

## Query Examples

### Search by tool name
```python
# Exact match
filter = "{Tool Name} = 'Salesforce'"

# Contains (for partial match)
filter = "FIND('sales', LOWER({Tool Name})) > 0"
```

### Get tools with API
```python
filter = "{Has API} = TRUE()"
```

### Get tools by category
```python
filter = "{Primary Category} = 'CRM'"
```

### Get high-confidence research
```python
filter = "{Research Confidence} = 'High'"
```

---

### Mapping: Tools Library → Tech Stack Survey

| Tools Library Field | Tech Stack Survey Column |
|--------------------|--------------------------|
| Tool Name | Tool/System Name |
| Company Name | Vendor/Provider |
| Has API | Does the tool have an official API? |
| API Documentation | (Source URL for confidence) |
| Integrations | Upstream Tools + Downstream Tools (parsed) |
| One-Line Description | Notes/Additional Context |
| Research Confidence | Research Confidence |
| Primary Category | (Used for direction inference) |

---

### Parsing Integrations Field

The Integrations field is uncategorized text (comma or line-separated tool names).

**Inference logic for direction:** See [Step 4: Infer Integration Directions](#step-4-infer-integration-directions) for the complete direction inference algorithm including DIRECTION_MAP and KNOWN_DIRECTIONS lookups.

**Example:**
- Tool: Slack
- Integrations field: "Salesforce, Jira, GitHub, Email"
- Parsed:
  - Upstream: Salesforce (CRM), Jira (PM), GitHub (Dev)
  - Downstream: Email (Communication)

---

## Adding New Tools

When research completes for a tool not in Tools Library:

1. Ask user: "Add [Tool Name] to Tools Library for future use?"
2. If yes, create record with researched data
3. Set Research Confidence based on source quality
4. Add Research Notes for any gaps

**Minimum fields for new record:**
- Tool Name (required)
- Tool URL
- Primary Category
- One-Line Description
- Has API
- Integrations
- Research Confidence

---

# Error Handling

| Situation | Response |
|-----------|----------|
| Tool not found in any source | "Unknown - needs manual research" |
| Ambiguous tool name (e.g., "Office") | Ask: "Did you mean Microsoft Office, LibreOffice, or something else?" |
| Multiple tools with same name | Show options with vendor names |
| Survey response missing tool list | Ask user to provide tool names |
| Excel template structure mismatch | Ask user to use standard template |
| Airtable connection unavailable | Skip Tools Library, proceed to web research |
| Tool name ambiguous | Ask: "Did you mean X, Y, or Z?" |
| Tools Library unavailable | Skip, proceed to web research |
| No info found anywhere | Set all fields to "Unknown - needs manual research" |
| Rate limited on web search | Pause, retry, or report partial results |
| Excel file locked/corrupted | Report error, offer to output as new file |
