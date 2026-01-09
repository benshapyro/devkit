# Discovery Catalog Lite Schema

Excel-based schema for lightweight discovery capture.

## File Structure

```
discovery-catalog-lite.xlsx
├── Instructions (read-only guidance)
├── Departments (organizational units)
├── Issues (problems/challenges identified)
└── Solutions (proposed fixes/opportunities)
```

---

## Sheet Schemas

### Departments

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| Department Name | Text | ✓ | Exact name (case-sensitive, used for linking) |
| Estimated Hours Saved | Number | | Total weekly hours expected from all solutions |

**Notes:**
- Add departments before referencing them in Issues/Solutions
- Names must match exactly across all sheets

---

### Issues

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| Department | Text | ✓ | Must match Departments sheet exactly |
| Issue Name | Text | ✓ | Short, descriptive title |
| Description | Text | ✓ | Detailed explanation of the problem |
| Impact Category | Select | | See valid values below |
| Solution Name | Text | | Must match Solutions sheet (leave blank if none) |
| Pain Point Quote | Text | | Direct stakeholder quote with attribution |
| Pain Point Cause | Text | | Root cause of the issue |
| Diagram URL | URL | | Link to process diagram if available |
| Finding 1 | Text | | Supporting data point |
| Finding 2 | Text | | Supporting data point |
| Finding 3 | Text | | Supporting data point |
| Finding N... | Text | | Add more columns as needed |

**Impact Category valid values:**
- New Revenue
- Time Efficiency
- Revenue Loss
- Customer Experience
- Competitive Position
- Brand Awareness
- Lead Quality
- Brand Consistency
- Product Quality
- Strategic Decisions
- Cost Reduction
- Risk Mitigation
- Employee Experience
- Compliance

---

### Solutions

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| Department | Text | ✓ | Which department this serves |
| Solution Name | Text | ✓ | Human-readable name (referenced by Issues) |
| Description | Text | ✓ | Full explanation of what it does |
| Impact | Text | | Quantified benefit (e.g., "15-20 hrs/week saved") |
| Impact Note | Text | | Additional context |
| Diagram URL | URL | | Link to solution diagram |

**Technology columns (repeat pattern as needed):**
| Column | Type | Description |
|--------|------|-------------|
| Tech N Name | Text | Tool/platform name |
| Tech N Status | Select | "Current" or "New" |
| Tech N Cost | Text | Monthly cost (e.g., "$500/mo", "~$30/user/mo", "-") |

**Data requirement columns:**
| Column | Type | Valid Values |
|--------|------|--------------|
| Data Access | Select | Yes, No, Partial |
| Data Access Notes | Text | What data, where located |
| Data Cleanliness | Select | High, Med, Low |
| Data Cleanliness Notes | Text | Cleanup/prep needed |
| Data Complexity | Select | High, Med, Low |
| Data Complexity Notes | Text | Technical considerations |

---

## Mapping: Lite → Full Catalog (Airtable)

### Issues → Challenges

| Lite Field | Airtable Field | Transform |
|------------|----------------|-----------|
| Department | (lookup) | Match to Client's departments |
| Issue Name | Challenge Name | Direct |
| Description | Explanation | Direct |
| Impact Category | Challenge Type | Map (see below) |
| Pain Point Quote | → 7_Quotes table | Create linked record |
| Pain Point Cause | Root Cause | Direct |
| Finding 1-N | Notes | Concatenate with bullets |
| — | Impact | Default: 3 (flag for review) |
| — | Urgency | Default: 3 (flag for review) |
| — | Readiness | Default: 3 (flag for review) |
| — | Priority Score | Default: 27 (3×3×3) |

**Impact Category → Challenge Type mapping:**
| Lite Impact Category | Airtable Challenge Type |
|---------------------|------------------------|
| New Revenue | Revenue Impact |
| Revenue Loss | Revenue Impact |
| Time Efficiency | Operational Efficiency |
| Cost Reduction | Operational Efficiency |
| Customer Experience | Customer Impact |
| Employee Experience | People & Culture |
| Competitive Position | Strategic |
| Brand Awareness | Strategic |
| Brand Consistency | Strategic |
| Product Quality | Quality & Risk |
| Risk Mitigation | Quality & Risk |
| Compliance | Quality & Risk |
| Lead Quality | Revenue Impact |
| Strategic Decisions | Strategic |

---

### Solutions → Solutions

| Lite Field | Airtable Field | Transform |
|------------|----------------|-----------|
| Department | Department | Match to Client |
| Solution Name | Solution Name | Direct |
| Description | Description | Direct |
| Impact | Expected Impact | Direct |
| Impact Note | Notes | Append |
| Tech N Name | → 4_Technology table | Create/link records |
| Tech N Status | Status | "Current" → Existing, "New" → Proposed |
| Tech N Cost | Cost Estimate | Direct |
| Data Access | Data Readiness | Yes→5, Partial→3, No→1 |
| Data Cleanliness | Data Quality | High→5, Med→3, Low→1 |
| Data Complexity | Complexity | High→1, Med→3, Low→5 (inverted) |
| — | Desirability | Default: 3 |
| — | Viability | Default: 3 |
| — | Feasibility | Default: 3 |
| — | DVF Score | Default: 27 |

---

### Departments → (No direct mapping)

Departments in Lite are informal groupings. In Full Catalog:
- Check if department exists as a Process area
- Or map to People records by department
- Estimated Hours Saved → aggregate to Solution impacts

---

## Writing to Excel (openpyxl)

### Add Issue row:
```python
from openpyxl import load_workbook

wb = load_workbook('discovery-catalog.xlsx')
issues = wb['Issues']

# Find next empty row
next_row = issues.max_row + 1

# Write fields
issues.cell(row=next_row, column=1, value='Sales')  # Department
issues.cell(row=next_row, column=2, value='Manual lead research')  # Issue Name
issues.cell(row=next_row, column=3, value='Reps spend 10+ hrs/week researching leads')  # Description
issues.cell(row=next_row, column=4, value='Time Efficiency')  # Impact Category
issues.cell(row=next_row, column=5, value='AI Lead Enrichment')  # Solution Name
issues.cell(row=next_row, column=6, value='"I spend more time researching than selling" — SR')  # Quote
issues.cell(row=next_row, column=7, value='No automated enrichment tools')  # Cause

wb.save('discovery-catalog.xlsx')
```

### Add Solution row:
```python
solutions = wb['Solutions']
next_row = solutions.max_row + 1

solutions.cell(row=next_row, column=1, value='Sales')
solutions.cell(row=next_row, column=2, value='AI Lead Enrichment')
solutions.cell(row=next_row, column=3, value='Automated lead research using Clay + LinkedIn')
solutions.cell(row=next_row, column=4, value='10 hrs/week saved per rep')
# Tech 1
solutions.cell(row=next_row, column=7, value='Clay.com')
solutions.cell(row=next_row, column=8, value='New')
solutions.cell(row=next_row, column=9, value='~$800/mo')

wb.save('discovery-catalog.xlsx')
```

### Column index reference:
```
Issues sheet:
A(1): Department
B(2): Issue Name
C(3): Description
D(4): Impact Category
E(5): Solution Name
F(6): Pain Point Quote
G(7): Pain Point Cause
H(8): Diagram URL
I(9): Finding 1
J(10): Finding 2
K(11): Finding 3

Solutions sheet:
A(1): Department
B(2): Solution Name
C(3): Description
D(4): Impact
E(5): Impact Note
F(6): Diagram URL
G(7): Tech 1 Name
H(8): Tech 1 Status
I(9): Tech 1 Cost
J(10): Tech 2 Name
K(11): Tech 2 Status
L(12): Tech 2 Cost
... (pattern continues)
S(19): Data Access
T(20): Data Access Notes
U(21): Data Cleanliness
V(22): Data Cleanliness Notes
W(23): Data Complexity
X(24): Data Complexity Notes
```

---

## Validation Rules

Before writing, validate:

1. **Department exists:** Check Departments sheet before adding Issue/Solution
2. **Solution exists:** If Issue references a Solution, verify it exists (or create placeholder)
3. **No duplicates:** Check Issue Name + Department combo doesn't already exist
4. **Required fields:** Department, Issue/Solution Name, Description must be non-empty

### Validation code:
```python
def validate_department(wb, dept_name):
    depts = wb['Departments']
    for row in depts.iter_rows(min_row=2, values_only=True):
        if row[0] == dept_name:
            return True
    return False

def validate_solution_exists(wb, solution_name):
    solutions = wb['Solutions']
    for row in solutions.iter_rows(min_row=2, values_only=True):
        if row[1] == solution_name:
            return True
    return False
```

---

## Creating Fresh Template

If template needed from scratch:
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

wb = Workbook()

# Departments sheet
depts = wb.active
depts.title = 'Departments'
depts.append(['Department Name', 'Estimated Hours Saved'])
depts['A1'].font = Font(bold=True)
depts['B1'].font = Font(bold=True)

# Issues sheet
issues = wb.create_sheet('Issues')
issue_headers = ['Department', 'Issue Name', 'Description', 'Impact Category', 
                 'Solution Name', 'Pain Point Quote', 'Pain Point Cause', 
                 'Diagram URL', 'Finding 1', 'Finding 2', 'Finding 3']
issues.append(issue_headers)
for cell in issues[1]:
    cell.font = Font(bold=True)

# Solutions sheet
solutions = wb.create_sheet('Solutions')
solution_headers = ['Department', 'Solution Name', 'Description', 'Impact', 
                    'Impact Note', 'Diagram URL',
                    'Tech 1 Name', 'Tech 1 Status', 'Tech 1 Cost',
                    'Tech 2 Name', 'Tech 2 Status', 'Tech 2 Cost',
                    'Tech 3 Name', 'Tech 3 Status', 'Tech 3 Cost',
                    'Tech 4 Name', 'Tech 4 Status', 'Tech 4 Cost',
                    'Data Access', 'Data Access Notes',
                    'Data Cleanliness', 'Data Cleanliness Notes',
                    'Data Complexity', 'Data Complexity Notes']
solutions.append(solution_headers)
for cell in solutions[1]:
    cell.font = Font(bold=True)

# Instructions sheet
instructions = wb.create_sheet('Instructions', 0)
# ... add instruction text

wb.save('discovery-catalog-lite-template.xlsx')
```
