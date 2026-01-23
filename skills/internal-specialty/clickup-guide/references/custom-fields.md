# Custom Fields for Consulting

Recommended Custom Fields, formula capabilities, governance practices, and workarounds for limitations.

## Field Types Overview

| Type | Use Case | Example |
|------|----------|---------|
| **Dropdown** | Single-select categories | Project Type, Status, Client Industry |
| **Multi-Select** | Multiple tags/categories | Skills Required, Stakeholders |
| **Number** | Quantifiable values | Hours, Score, Count |
| **Money/Currency** | Financial values | Budget, Revenue, Cost |
| **Date** | Dates beyond due date | Contract Start, Renewal Date |
| **Checkbox** | Yes/No toggles | Billable?, Approved?, NDA Signed? |
| **Text** | Short free text | Notes, Reference ID |
| **Email** | Email addresses | Client Contact, Sponsor Email |
| **Phone** | Phone numbers | Client Phone |
| **People** | ClickUp users | Project Manager, Reviewer |
| **Relationship** | Links to other tasks | Related Projects, Dependencies |
| **Rollup** | Aggregates from relationships | Total Hours from Subtasks |
| **Formula** | Calculated values | Budget Remaining, Utilization % |
| **Rating** | Star/emoji ratings | Client Satisfaction, Priority Score |
| **Progress** | Manual or auto progress | % Complete |

## Recommended Fields for Consulting

### Essential Fields (Create First)

| Field | Type | Scope | Purpose |
|-------|------|-------|---------|
| Client Name | Dropdown | Workspace | Filter, group, report by client |
| Project Type | Dropdown | Workspace | Strategy / Implementation / Assessment / Retainer |
| Engagement Status | Dropdown | Space | Onboarding / Active / Closing / Archived |
| Billable | Checkbox | Workspace | Track billable vs internal work |
| Project Manager | People | Space | Single accountable owner |
| Client Contact | Email | Folder | For automated notifications |

### Financial Tracking Fields

| Field | Type | Scope | Purpose |
|-------|------|-------|---------|
| Budget Hours | Number | Folder | Total allocated hours |
| Budget Amount | Currency | Folder | Total engagement value |
| Hourly Rate | Currency | Folder | Blended or specific rate |
| Hours Used | Rollup | Folder | Sum of time tracked |
| Budget Consumed % | Formula | Folder | (Hours Used / Budget Hours) × 100 |

### Project Health Fields

| Field | Type | Options | Purpose |
|-------|------|---------|---------|
| Health Status | Dropdown | Green / Yellow / Red | Quick visual indicator |
| Risk Level | Dropdown | Low / Medium / High / Critical | Risk tracking |
| Confidence | Dropdown | High / Medium / Low | Delivery confidence |
| Blockers | Multi-Select | Resource / Client / Technical / Scope | Categorize impediments |

### Client Relationship Fields

| Field | Type | Scope | Purpose |
|-------|------|-------|---------|
| Industry | Dropdown | Workspace | Sector categorization |
| Company Size | Dropdown | Workspace | SMB / Mid-Market / Enterprise |
| Relationship Owner | People | Folder | Account manager |
| Contract Renewal | Date | Folder | Renewal tracking |
| NPS Score | Rating | Folder | Client satisfaction |

## Formula Field Patterns

### Budget & Financial Formulas

**Budget Burn Rate:**
```
ROUND((field("Hours Used") / field("Budget Hours")) * 100, 1)
```
Returns: Percentage of budget consumed

**Budget Remaining:**
```
field("Budget Hours") - field("Hours Used")
```
Returns: Hours remaining

**Project Value Remaining:**
```
field("Budget Amount") - (field("Hours Used") * field("Hourly Rate"))
```
Returns: Dollar value remaining

**Profitability Estimate:**
```
field("Budget Amount") - (field("Hours Used") * field("Cost Rate"))
```
Returns: Estimated profit (requires Cost Rate field)

### Health & Status Formulas

**Project Health Indicator:**
```
IF(AND(field("Budget Consumed %") < 80, field("Days Remaining") > 5), "Green", 
IF(OR(field("Budget Consumed %") > 95, field("Days Remaining") < 2), "Red", "Yellow"))
```
Returns: Green / Yellow / Red based on budget and timeline

**Days Until Due:**
```
DAYS(field("Due Date"), TODAY())
```
Returns: Number of days remaining

**⚠️ Warning:** Formulas using TODAY() have significant limitations (see below).

### Utilization Formulas

**Task Utilization:**
```
ROUND((field("Time Tracked") / field("Time Estimate")) * 100, 1)
```
Returns: Percentage of estimate used

## Formula Field Limitations

**Critical limitations to know:**

| Limitation | Impact | Workaround |
|------------|--------|------------|
| TODAY() blocks sorting/filtering/grouping | Can't sort by "days remaining" | Use static date field + manual updates |
| TODAY() blocks Dashboard Calculation cards | Can't show real-time metrics | Use Rollup fields or external calculations |
| Text fields can't be formula inputs | Can't concatenate or manipulate text | Use Dropdown with text options instead |
| One nesting level only | Formula A can reference Formula B, but B can't reference another formula | Flatten calculations |
| Field names are case-sensitive | "budget" ≠ "Budget" | Use exact field names |
| Formulas don't transfer in templates | Must recreate after applying template | Document formulas separately |
| Text-appended formulas read as text | Can't SUM a field showing "$1,000" | Keep numeric, format in views |

### TODAY() Workaround

Instead of:
```
DAYS(field("Due Date"), TODAY())  ← Can't sort or filter
```

Use a static "Calculation Date" field updated weekly, or:
1. Create recurring task "Update Calculation Date"
2. Manually update a Date field called "As Of Date"
3. Formula: `DAYS(field("Due Date"), field("As Of Date"))`

## Cascading Dropdowns Workaround

**Problem:** ClickUp doesn't support cascading dropdowns (where selecting "Client A" auto-populates Industry, Account Manager, etc.).

**Workaround 1: Relationships + Rollups**

1. Create a "Clients" List with one task per client:
   ```
   Task: Acme Corp
   - Industry: Technology
   - Account Manager: Jane
   - Contract Value: $100,000
   ```

2. In project tasks, add Relationship field linked to Clients List

3. Add Rollup fields to pull Client data:
   - Rollup: Industry (from linked Client)
   - Rollup: Account Manager (from linked Client)

**Workaround 2: Automation-Based**

Create automations for each client:
```
Trigger: Custom Field "Client" changes to "Acme Corp"
Actions:
  - Set "Industry" to "Technology"
  - Set "Account Manager" to "Jane"
```

**Downside:** Requires one automation per client. Not scalable beyond ~20 clients.

**Workaround 3: External Integration**

Use Zapier/Make to:
1. Watch for Client field changes
2. Look up client data in external source (Airtable, Google Sheets)
3. Update related fields in ClickUp

## Field Governance

### Naming Convention

Use consistent naming to prevent sprawl:

```
[Emoji] [Category] - [Specific Name]

💰 Budget - Total Hours
💰 Budget - Amount
💰 Budget - Consumed %
💼 Client - Industry
💼 Client - Contact Email
📊 Project - Health Status
📊 Project - Risk Level
⏱️ Time - Estimate
⏱️ Time - Tracked
```

### Placement Strategy

| Scope | Use For | Example Fields |
|-------|---------|----------------|
| **Workspace** | Universal fields used everywhere | Client Name, Billable, Priority |
| **Space** | Department-specific fields | Delivery: Project Type, Engagement Status |
| **Folder** | Client or project-specific fields | Contract Renewal, Client Contact |
| **List** | Narrow use cases | Sprint-specific fields |

**Principle:** Place fields at the highest level where they're consistently used. Don't duplicate fields at multiple levels.

### Governance Process

1. **Designate a ClickUp Champion** — One person controls field creation
2. **Maintain field documentation:**
   - Field Name
   - Type
   - Location (Workspace/Space/Folder)
   - Purpose
   - Options (for dropdowns)
   - Owner
   - Date Created

3. **Approval process** — Request before creating new fields
4. **Monthly audit** — Review for duplicates, unused fields
5. **Cleanup** — Archive or delete fields no longer used

### Business vs Enterprise Field Management

| Capability | Business | Enterprise |
|------------|----------|------------|
| Create Custom Fields | ✅ | ✅ |
| Pin Custom Fields | ✅ | ✅ |
| Hide from Guests | ✅ | ✅ |
| **Move fields between locations** | ❌ | ✅ |
| **Merge duplicate fields** | ❌ | ✅ |
| **Granular field permissions** | Limited | Full |
| **Custom roles for field management** | ❌ | ✅ |

**Why Enterprise matters:** If you have field sprawl from organic growth, Enterprise's move/merge capabilities are the only way to clean up without recreating data.

## Field Anti-Patterns

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Duplicate fields at different levels | Data inconsistency, reporting issues | Consolidate to highest common level |
| Too many dropdowns | Overwhelming, low adoption | Limit to 5-7 options, use sparingly |
| Text fields for structured data | Can't filter, group, or report | Use Dropdown or standardized format |
| Creating field per client | Unscalable, cluttered | Use single "Client" dropdown |
| Formulas with TODAY() for dashboards | Breaks calculations | Use static date reference |
| No naming convention | Chaos as fields multiply | Implement convention early |

## Quick Setup: Minimum Viable Fields

For a new consulting engagement, create these fields first:

**At Workspace level (if not already):**
- Client Name (Dropdown)
- Billable (Checkbox)

**At client Folder level:**
- Project Manager (People)
- Client Contact (Email)
- Engagement Status (Dropdown: Onboarding / Active / Closing / Complete)
- Budget Hours (Number)

**Add later as needed:**
- Health Status
- Risk Level
- Financial tracking fields
- Formula calculations

Start simple. Add complexity only when you have a clear use case.
