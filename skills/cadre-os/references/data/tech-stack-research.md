# Tech Stack Research Workflow

Step-by-step process for researching and populating the Tech Stack Survey grid.

## Overview

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

## Error Handling

| Situation | Action |
|-----------|--------|
| Tool name ambiguous | Ask: "Did you mean X, Y, or Z?" |
| Tools Library unavailable | Skip, proceed to web research |
| No info found anywhere | Set all fields to "Unknown - needs manual research" |
| Rate limited on web search | Pause, retry, or report partial results |
| Excel file locked/corrupted | Report error, offer to output as new file |
