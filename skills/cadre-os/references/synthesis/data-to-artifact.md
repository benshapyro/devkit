# Data to Artifact Generation

How to generate branded client artifacts from Tech Stack Survey and Discovery Catalog Lite data.

---

## Overview

The artifact templates contain **example data** (Acme Corp) that renders correctly out of the box. To generate a client artifact:

1. **Load client data** from Excel or Airtable
2. **Read the template** to understand the structure
3. **Generate new HTML/JSX** with client data substituted for example data
4. **Output as artifact** or save as file

**Key principle:** Don't try to find-and-replace in the template. Instead, use the template as a **structural reference** and generate fresh HTML/JSX with the client's actual data.

---

## Available Artifacts

| Artifact | Template | Data Source |
|----------|----------|-------------|
| Tech Stack Overview | `tech-stack-overview.html` | Tech Stack Survey Excel |
| Integration Map | `integration-map.jsx` | Tech Stack Survey Excel |
| Findings Summary | `findings-summary.html` | Discovery Catalog Lite Excel |

Templates location: `assets/artifact-templates/`

---

## Artifact 1: Tech Stack Overview

### What This Artifact Shows

All data is defensible — either client-provided or Claude-researched with clear sources.

| Section | Data Source | Notes |
|---------|-------------|-------|
| Connectivity Potential | Calculated from Column H (API) | API Coverage, Connection Paths, Isolated count |
| Stats Row | Columns A, C, F, H | Total tools, spend, API counts, departments |
| Spend by Department | Columns C + F | Grouped sum of costs by department |
| Cost per User Outliers | Columns E + F | Highest and lowest cost/user |
| Tool Inventory | Columns A-H | Factual data only, no health/recommendations |

### Data Required

From Tech Stack Survey Excel:

| Column | Field | Required? | Used For |
|--------|-------|-----------|----------|
| A | Tool/System Name | Yes | Tool name |
| B | Primary Use/Purpose | No | Not displayed (would require inference) |
| C | Primary Department(s) | Yes | Department badges, spend grouping |
| D | Tool Owner/Champion | Yes | Detail row |
| E | # of Users | Yes | Detail row, cost per user calculation |
| F | Annual Cost | Yes | Cost column, totals, spend chart |
| G | Vendor/Provider | No | Vendor subtext |
| H | Has API? | Yes | API status, connectivity score |
| I | Upstream Tools | Yes | Possible integrations count |
| J | Downstream Tools | Yes | Possible integrations count |

### Generation Steps

1. **Load and parse Excel:**
```python
from openpyxl import load_workbook

wb = load_workbook('tech-stack-client.xlsx')
ws = wb['Tech Stack  Survey']  # Note: two spaces

tools = []
for row in ws.iter_rows(min_row=2, values_only=True):
    if row[0]:  # Has tool name
        tools.append({
            'name': row[0],
            'departments': row[2] or '',
            'owner': row[3] or '',
            'users': row[4] or 0,
            'cost': row[5] or 0,
            'vendor': row[6] or 'Unknown',
            'has_api': row[7] or 'Unknown',
            'upstream': row[8] or '',
            'downstream': row[9] or '',
        })
```

2. **Calculate connectivity metrics:**
```python
total_tools = len(tools)

# API coverage
api_yes = len([t for t in tools if str(t['has_api']).lower() == 'yes'])
api_no = len([t for t in tools if str(t['has_api']).lower() == 'no'])
api_unknown = total_tools - api_yes - api_no
connectivity_percent = round(api_yes / total_tools * 100) if total_tools > 0 else 0

# Connection paths (tools with at least one possible integration)
def has_connections(tool):
    return bool(tool['upstream']) or bool(tool['downstream'])

tools_with_paths = len([t for t in tools if has_connections(t)])

# Isolated tools (no API AND no connections)
isolated = [t for t in tools if str(t['has_api']).lower() == 'no' and not has_connections(t)]
isolated_count = len(isolated)

# Count possible integrations per tool
def count_integrations(tool):
    upstream = len([x.strip() for x in tool['upstream'].split(',') if x.strip()]) if tool['upstream'] else 0
    downstream = len([x.strip() for x in tool['downstream'].split(',') if x.strip()]) if tool['downstream'] else 0
    return upstream + downstream
```

3. **Calculate spend by department:**
```python
from collections import defaultdict

def parse_cost(cost_str):
    if not cost_str or str(cost_str).lower() == 'unknown':
        return 0
    import re
    cleaned = re.sub(r'[^\d.]', '', str(cost_str).split('/')[0])
    return float(cleaned) if cleaned else 0

dept_spend = defaultdict(float)
for tool in tools:
    cost = parse_cost(tool['cost'])
    for dept in [d.strip() for d in tool['departments'].split(',')]:
        if dept:
            dept_spend[dept] += cost

# Sort by spend descending
dept_spend_sorted = sorted(dept_spend.items(), key=lambda x: x[1], reverse=True)
total_spend = sum(dept_spend.values())
```

4. **Calculate cost per user outliers:**
```python
cost_per_user = []
for tool in tools:
    cost = parse_cost(tool['cost'])
    users = int(tool['users']) if tool['users'] else 0
    if cost > 0 and users > 0:
        cost_per_user.append({
            'name': tool['name'],
            'cpu': round(cost / users),
            'cost': cost,
            'users': users
        })

# Sort for highest and lowest
highest_cpu = sorted(cost_per_user, key=lambda x: x['cpu'], reverse=True)[:3]
lowest_cpu = sorted(cost_per_user, key=lambda x: x['cpu'])[:3]
```

5. **Generate HTML sections:**

**Connectivity hero:**
```html
<div class="score">{connectivity_percent}%</div>
<div class="score-sub">of tools have API access</div>

<!-- Factors -->
<span class="factor-value">{api_yes}/{total_tools}</span>  <!-- API Coverage -->
<span class="factor-value">{tools_with_paths}/{total_tools}</span>  <!-- Connection Paths -->
<span class="factor-value">{isolated_count}</span>  <!-- Isolated Tools -->

<p class="summary">{api_yes} of {total_tools} tools have APIs. {tools_with_paths} have at least one possible integration path. {isolated_count} tool(s) isolated — no API, no documented integrations.</p>
```

**Spend by department:** Generate one bar per department from `dept_spend_sorted`.

**Cost per user outliers:** Generate cards from `highest_cpu` and `lowest_cpu`.

**Tool inventory rows:** Generate one `<tr>` per tool:
- API status: `api-dot yes`, `api-dot no`, `api-dot unknown`
- Possible integrations: Show count from `count_integrations(tool)`
- Detail row: Owner, Users, Cost per User, list of possible integrations

6. **Output complete HTML** as artifact or file.

### Department Badge Classes

| Department Contains | CSS Class |
|---------------------|-----------|
| sales | `dept-badge sales` |
| marketing | `dept-badge marketing` |
| finance | `dept-badge finance` |
| engineering, it, tech | `dept-badge engineering` |
| operations, ops | `dept-badge operations` |
| everyone, company, all, company-wide | `dept-badge all` |
| (default) | `dept-badge` |

### What NOT to Include

These were removed because they require inference or judgment:

| Removed | Reason |
|---------|--------|
| Health status (green/yellow/red) | No clear calculation — what makes a tool "healthy"? |
| Spend by Category | Would require inferring category from purpose |
| Recommendations | Requires judgment, not data |
| "X connected" language | We know possible connections, not actual |
| Confidence badges | Muddies the distinction between fact and research |

---

## Artifact 2: Integration Map

### Data Required

From Tech Stack Survey Excel:

| Column | Field | Used For |
|--------|-------|----------|
| A | Tool/System Name | Node label |
| B | Purpose | Category inference |
| I | Upstream Tools | Incoming connections |
| J | Downstream Tools | Outgoing connections |
| K | Connection Method | Line style |

### Generation Steps

1. **Build tool ID mapping:**
```python
def to_id(name):
    return name.lower().replace(' ', '-').replace('.', '').replace('/', '-')

tool_ids = {to_id(t['name']): t for t in tools}
```

2. **Infer categories from tool name/purpose:**
```python
CATEGORY_KEYWORDS = {
    'crm': ['crm', 'salesforce', 'hubspot', 'customer', 'lead'],
    'communication': ['slack', 'teams', 'email', 'chat', 'zoom', 'meet'],
    'finance': ['quickbooks', 'xero', 'stripe', 'accounting', 'invoice', 'payment'],
    'automation': ['zapier', 'make', 'n8n', 'automate', 'workflow'],
    'storage': ['drive', 'dropbox', 'box', 'storage', 'file', 's3'],
    'project': ['asana', 'monday', 'jira', 'trello', 'project', 'task', 'clickup'],
    'analytics': ['tableau', 'looker', 'analytics', 'report', 'bi', 'metabase'],
}

def infer_category(tool):
    text = (tool['name'] + ' ' + tool['purpose']).lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in text for kw in keywords):
            return category
    return 'other'
```

3. **Parse connections:**
```python
def parse_connections(conn_str):
    if not conn_str:
        return []
    return [to_id(name.strip()) for name in conn_str.split(',') if name.strip()]
```

4. **Normalize connection methods:**
```python
def normalize_method(method):
    if not method:
        return 'api'
    m = method.lower()
    if 'native' in m or 'built-in' in m:
        return 'native'
    if 'zapier' in m or 'make' in m or 'ipaas' in m:
        return 'ipaas'
    if 'manual' in m or 'export' in m or 'csv' in m:
        return 'manual'
    return 'api'
```

5. **Generate TOOL_DATA array:**
```javascript
const TOOL_DATA = [
  { id: "salesforce", name: "Salesforce", category: "crm", upstream: ["webforms"], downstream: ["slack", "quickbooks"], connectionMethod: "native" },
  { id: "slack", name: "Slack", category: "communication", upstream: ["salesforce"], downstream: [], connectionMethod: "native" },
  // ... one entry per tool
];
```

6. **Output complete JSX** as artifact with:
- `CLIENT_NAME` = client name
- `DATE` = current date
- `TOOL_DATA` = generated array

### Converting to HTML for Client Portal

The Client Portal only accepts HTML. After generating the JSX artifact, offer:

> "Want me to convert this to HTML for the Client Portal?"

**If yes, generate a static HTML version:**

1. Replace React interactivity with pure HTML/CSS
2. Use SVG for the circular layout (pre-calculated positions)
3. Remove click handlers — show all connections by default, or use CSS hover states
4. Keep the same visual styling (Cadre brand colors)

**Conversion approach:**
```html
<!-- Static HTML structure -->
<div class="integration-map">
  <div class="header">...</div>
  <div class="stats-row">...</div>
  <svg class="map-canvas" viewBox="0 0 600 600">
    <!-- Draw connections as lines -->
    <line class="connection native" x1="..." y1="..." x2="..." y2="..."/>
    <!-- Draw nodes as circles with text -->
    <g class="tool-node" transform="translate(x, y)">
      <circle r="45" fill="..." stroke="..."/>
      <text>Tool Name</text>
    </g>
  </svg>
  <div class="legend">...</div>
</div>
```

**Position calculation:**
```javascript
// Circular layout
const centerX = 300, centerY = 300, radius = 200;
tools.forEach((tool, i) => {
  const angle = (i / tools.length) * 2 * Math.PI - Math.PI/2;
  tool.x = centerX + radius * Math.cos(angle);
  tool.y = centerY + radius * Math.sin(angle);
});
```

The HTML version loses click-to-highlight interactivity but renders in any browser and works in the Client Portal.

---

## Artifact 3: Findings Summary

### Data Required

From Discovery Catalog Lite Excel:

**Issues sheet (2_Issues):**
| Column | Field |
|--------|-------|
| A | Department |
| B | Issue Name |
| C | Description |
| D | Impact Category |
| E | Solution Name (link) |
| F | Pain Point Quote |

**Solutions sheet (3_Solutions):**
| Column | Field |
|--------|-------|
| A | Department |
| B | Solution Name |
| C | Description |
| D | Impact |
| E | Impact Note |

### Generation Steps

1. **Load issues and solutions:**
```python
wb = load_workbook('discovery-catalog-lite.xlsx')

issues = []
for row in wb['2_Issues'].iter_rows(min_row=2, values_only=True):
    if row[1]:  # Has issue name
        issues.append({
            'department': row[0] or '',
            'name': row[1],
            'description': row[2] or '',
            'impact_category': row[3] or 'Medium',
            'solution_link': row[4] or '',
            'quote': row[5] or '',
        })

solutions = []
for row in wb['3_Solutions'].iter_rows(min_row=2, values_only=True):
    if row[1]:  # Has solution name
        solutions.append({
            'department': row[0] or '',
            'name': row[1],
            'description': row[2] or '',
            'impact': row[3] or '',
            'effort': infer_effort(row),  # Based on tech complexity
        })
```

2. **Classify impact levels:**
```python
HIGH_IMPACT = ['Time Efficiency', 'Revenue Loss', 'New Revenue', 'Customer Experience']
MEDIUM_IMPACT = ['Competitive Position', 'Lead Quality', 'Cost Reduction']

def get_impact_level(category):
    if category in HIGH_IMPACT:
        return 'high'
    if category in MEDIUM_IMPACT:
        return 'medium'
    return 'low'
```

3. **Identify quick wins:**
```python
# Quick win = Low effort solution that addresses high-impact issue
quick_wins = []
for solution in solutions:
    if solution['effort'] == 'Low':
        # Check if it addresses any high-impact issues
        linked_issues = [i for i in issues if i['solution_link'] == solution['name']]
        if any(get_impact_level(i['impact_category']) == 'high' for i in linked_issues):
            quick_wins.append(solution)
```

4. **Group by dimension (department):**
```python
dimensions = {}
for issue in issues:
    dept = issue['department']
    if dept not in dimensions:
        dimensions[dept] = {'issues': [], 'solutions': []}
    dimensions[dept]['issues'].append(issue)

for solution in solutions:
    dept = solution['department']
    if dept in dimensions:
        dimensions[dept]['solutions'].append(solution)
```

5. **Generate recommended next steps:**
```python
next_steps = []

if quick_wins:
    next_steps.append({
        'title': 'Implement Quick Wins',
        'description': f'Start with {len(quick_wins)} low-effort, high-impact solutions'
    })

high_impact_unaddressed = [i for i in issues 
    if get_impact_level(i['impact_category']) == 'high' 
    and not i['solution_link']]
if high_impact_unaddressed:
    next_steps.append({
        'title': 'Address Critical Gaps',
        'description': f'{len(high_impact_unaddressed)} high-impact issues need solutions'
    })

next_steps.extend([
    {'title': 'Validate with Leadership', 'description': 'Present findings to executive team'},
    {'title': 'Develop Detailed Roadmap', 'description': 'Create phased implementation plan'},
    {'title': 'Define Success Metrics', 'description': 'Establish KPIs for each initiative'},
])
```

6. **Generate HTML sections:**

**Stats:** Total issues, total solutions, quick wins count, high-impact count

**Quick wins grid:** One card per quick win with title, description, type badge

**Issues column:** One `issue-card` per issue with:
- Title and meta badges (dimension, impact level)
- Description
- Source quote if available

**Solutions column:** One `solution-card` per solution with:
- Title and meta badges (type, effort level)
- Description
- "Addresses: {linked issue names}"

**Dimension coverage:** Bar chart showing issues vs solutions per department

**Next steps:** Numbered list

---

## CSS Class Reference

### API Status
```css
.api-dot.yes { background: var(--status-green); }
.api-dot.no { background: var(--status-red); }
.api-dot.unknown { background: var(--status-yellow); }

.api-label.yes { color: var(--status-green); }
.api-label.no { color: var(--status-red); }
.api-label.unknown { color: var(--status-yellow); }
```

### Department Badges
```css
.dept-badge.sales { background: #fef3c7; color: #92400e; }
.dept-badge.marketing { background: #fce7f3; color: #9d174d; }
.dept-badge.finance { background: #d1fae5; color: #065f46; }
.dept-badge.engineering { background: #dbeafe; color: #1e40af; }
.dept-badge.operations { background: #e0e7ff; color: #3730a3; }
.dept-badge.all { background: var(--cadre-black); color: var(--cadre-white); }
```

### Outlier Cards
```css
.outlier-card.high { border-left: 4px solid var(--status-red); }
.outlier-card.low { border-left: 4px solid var(--status-green); }
```

### Findings Summary (Impact/Effort Badges)
```css
.badge.impact-high { background: #fee2e2; color: #991b1b; }
.badge.impact-medium { background: #fef3c7; color: #92400e; }
.badge.impact-low { background: #f1f5f9; color: #475569; }

.badge.effort-low { background: #d1fae5; color: #065f46; }
.badge.effort-medium { background: #fef3c7; color: #92400e; }
.badge.effort-high { background: #fee2e2; color: #991b1b; }

.badge.type { background: #f3e8ff; color: #6b21a8; }  /* Process/Technology/Training */
.badge.dimension { background: #e0f2fe; color: #0369a1; }
```

### Issue/Solution Cards
```css
.issue-card.high { border-left-color: var(--cadre-danger); }
.issue-card.medium { border-left-color: var(--cadre-warning); }
.issue-card.low { border-left-color: var(--cadre-slate); }

.solution-card { border-left-color: var(--cadre-teal); }
```

---

## Output Format

When presenting artifacts to users:

```markdown
Here's your **{Artifact Name}** for {Client Name}:

**Summary:**
- {Key stat 1}
- {Key stat 2}
- {Key stat 3}

[Artifact rendered inline or file download link]

**What's included:**
- {Brief description of sections}

**Next steps:**
- {Suggested action 1}
- {Suggested action 2}
```

---

## Error Handling

| Situation | Action |
|-----------|--------|
| Missing tool name | Skip row |
| Missing cost | Display "—" or "Unknown" |
| No API info | Default to "Unknown" |
| Empty department | Use "Unassigned" |
| No connections | Show tool as isolated node |
| No quick wins | Hide quick wins section or show "None identified" |
| Parse error | Log warning, continue with available data |

---

## Template Reference

View the example-data templates to understand exact HTML structure:

- `assets/artifact-templates/tech-stack-overview.html` — 12-tool Acme Corp example
- `assets/artifact-templates/integration-map.jsx` — 9-tool connected network
- `assets/artifact-templates/findings-summary.html` — 8 issues, 6 solutions example

Copy the structural patterns (CSS classes, HTML nesting, section order) when generating client artifacts.
