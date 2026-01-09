# Tools Library (Airtable)

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

## Primary Category Options

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

## MCP Server Options

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

## Mapping: Tools Library → Tech Stack Survey

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

## Parsing Integrations Field

The Integrations field is uncategorized text (comma or line-separated tool names).

**Inference logic for direction:**

```python
# Tool categories and their typical data flow direction
UPSTREAM_CATEGORIES = [
    'CRM', 'Forms', 'Sales', 'Marketing',  # Data sources
]

DOWNSTREAM_CATEGORIES = [
    'Communication', 'Reporting', 'Analytics',  # Data consumers
    'Accounting', 'Finance',
]

BIDIRECTIONAL_CATEGORIES = [
    'Automation', 'Project Management', 'Collaboration',
    'Storage', 'Data Management',
]

def infer_direction(tool_name, tool_category):
    """
    Given a tool name from the Integrations field,
    infer if it's upstream, downstream, or both.
    """
    # Look up category of the integration tool
    integration_category = lookup_category(tool_name)
    
    if integration_category in UPSTREAM_CATEGORIES:
        return 'upstream'
    elif integration_category in DOWNSTREAM_CATEGORIES:
        return 'downstream'
    else:
        return 'both'  # List in both columns, user validates
```

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
