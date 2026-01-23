# Time Tracking & Billing

Native ClickUp time tracking capabilities, limitations, and integrations for consulting billing.

## Native Time Tracking

### Enabling Time Tracking

1. Click Workspace avatar → "ClickApps"
2. Find "Time Tracking" → Toggle ON
3. Also enable:
   - "Time Estimates" — For capacity planning
   - "Time Tracking Rollup" — Aggregate time from subtasks

### Tracking Methods

**Start/Stop Timer:**
- Open task → Click "Track Time" → Start
- From List view: Click clock icon on task row
- Timer visible in toolbar while running
- Switch tasks: timer moves to new task

**Manual Entry:**
1. Open task → Click "Track Time"
2. Enter duration (e.g., "2h 30m" or "2:30")
3. Select date and time
4. Add description/note
5. Toggle "Billable" if applicable
6. Click "Save"

### Billable vs Non-Billable

**Mark as Billable:** Click currency icon (💲) when creating/editing entry

**Set Default:** ClickApps → Time Tracking → Settings → Default billable status

**Best practice:** Default to billable, mark exceptions as non-billable. Easier than remembering to mark things billable.

### Timesheet Views

**Access:** More → Timesheets (pin to sidebar)

**My Timesheet:**
- View by task or by date
- Edit entries
- See capacity vs tracked

**All Timesheets (Admins):**
- View all team members' time
- Weekly capacity overview
- Billable/non-billable breakdown
- Export capabilities

### Time Tracking Limitations

| Capability | Native ClickUp | Notes |
|------------|----------------|-------|
| Start/stop timer | ✅ Yes | Works well |
| Manual entry | ✅ Yes | Works well |
| Billable flag | ✅ Yes | Simple on/off |
| Notes on entries | ✅ Yes | Good for descriptions |
| Timesheet view | ✅ Yes | Adequate for review |
| Export to CSV | ✅ Yes | For external processing |
| **Per-user billing rates** | ❌ No | Critical gap |
| **Per-client billing rates** | ❌ No | Critical gap |
| **Per-project billing rates** | ❌ No | Critical gap |
| **Time rounding rules** | ❌ No | No round to nearest X |
| **Invoicing** | ❌ No | Export only |
| **Utilization % calculation** | ❌ No | Manual calculation |
| **Budget alerts** | ❌ No | Requires workaround |

**The core problem:** ClickUp tracks TIME but not MONEY. You can't set different rates for different consultants, clients, or projects.

## Utilization Tracking

### Manual Utilization Calculation

**Formula:** Utilization % = (Billable Hours / Available Hours) × 100

**Example:**
- Consultant tracked 35 billable hours
- 40 available hours in week
- Utilization = 35/40 = 87.5%

### Dashboard Approximation

Create widgets to approximate utilization:

1. **Time Tracked by Assignee** (bar chart) — Shows hours per person
2. **Billable vs Non-Billable** (pie chart) — Shows split
3. **Calculation Card** — Can sum hours but can't calculate %

**Limitation:** No native utilization percentage. Must export and calculate externally.

### Time-Based Custom Fields

For better tracking without integrations:

```
Custom Fields at List level:
- Budgeted Hours (Number)
- Time Estimate (built-in)
- Time Tracked (built-in rollup)

Formula Field:
- Hours Remaining = Budgeted Hours - Time Tracked
- Budget Consumed % = (Time Tracked / Budgeted Hours) × 100
```

## Everhour Integration (Recommended)

Everhour solves ClickUp's billing rate limitations.

### What Everhour Adds

| Capability | Details |
|------------|---------|
| **Multiple billing rates** | Per-project, per-member, or per-task |
| **Time rounding** | Round to nearest 5/10/15/30 minutes |
| **Budget tracking** | Project budgets with alerts |
| **Invoicing** | Generate invoices from time data |
| **Utilization reports** | Automatic calculation |
| **Profitability** | Revenue vs cost analysis |

### Everhour Pricing

- **Free:** 5 users, basic features
- **Team:** $8.50/user/month — Full features
- **For Cadre (30 users):** ~$255/month

### Billing Methods in Everhour

| Method | Use Case | Configuration |
|--------|----------|---------------|
| **Non-billable** | Internal projects | No rate |
| **T&M Project Rate** | Single rate for project | Set $/hour at project level |
| **T&M Member Rate** | Different rates per consultant | Set $/hour per person per project |
| **Custom Task Rates** | Override for specific tasks | Set rate on individual tasks |
| **Fixed Fee** | Project-based billing | Set total budget regardless of hours |

### Everhour Setup

1. Install Everhour browser extension
2. Connect to ClickUp Workspace
3. Navigate to Projects in Everhour
4. Click $ icon on project
5. Choose billing method
6. Set rates

Time tracked in ClickUp automatically syncs with configured Everhour rates.

### Everhour vs Native Decision

| Scenario | Recommendation |
|----------|----------------|
| Internal time tracking only | Native ClickUp |
| Single billing rate for all work | Native ClickUp |
| Multiple consultant rates | **Everhour** |
| Client-specific rates | **Everhour** |
| Need invoicing from time data | **Everhour** |
| Budget alerts required | **Everhour** |
| Utilization reporting needed | **Everhour** |

## Timesheet Approvals

### Native Approval Workflow (Business+)

1. Admin configures:
   - Submission deadline
   - Reminder settings
   - Who submits to whom

2. Employee workflow:
   - Track time throughout week
   - Click "Submit for approval" before deadline
   - Timesheet locks pending review

3. Manager workflow:
   - See submissions in "To Review" tab
   - Approve, request changes, or comment
   - Approved timesheets lock permanently

### Approval Limitations

**⚠️ Key limitation:** Approvals are per-PERSON, not per-PROJECT.

**Impact:** Project managers cannot approve only their project's hours. They either approve employee's entire timesheet or nothing.

**Workaround:** Use filtering by project when reviewing, but approval still covers all hours.

## Accounting Integrations

### QuickBooks Online (Native)

**Available features:**
- Two-way customer sync
- One-way products, services, invoices (QBO → ClickUp)
- Creates "QuickBooks Online" Space with synced data

**NOT available:**
- Direct time entry sync (requires Zapier/Make)
- Invoice generation from ClickUp time

**Setup:**
1. App Center → QuickBooks Online
2. Connect account
3. Configure sync settings

### Xero (No Native Integration)

**Workarounds required:**

**Via Zapier:**
- Task completion → Create Xero invoice
- Time entry → Create invoice line item

**Via Make.com:**
- Full Xero API access
- Invoices, contacts, expense claims

**Via Everhour:**
- Export time data
- Import to Xero for invoicing

### Harvest (Native)

**Available features:**
- Bi-directional time sync
- Direct invoicing capability
- Project budgets

**Best for:** Teams already using Harvest who want ClickUp for project management.

### Integration Decision Framework

| Need | Solution |
|------|----------|
| Simple time tracking, manual invoicing | Native ClickUp + export to CSV |
| Multiple rates, professional invoicing | Everhour ($8.50/user/month) |
| QuickBooks integration | Native + Zapier for time sync |
| Xero integration | Make.com or Everhour |
| All-in-one time + invoicing | Harvest or Everhour |

## Complete Billing Stack for Consulting

**Recommended setup for 30-person firm:**

| Component | Cost | Purpose |
|-----------|------|---------|
| ClickUp Business | $360/month | Project management, native time tracking |
| Everhour Team | $255/month | Multi-rate billing, utilization, invoicing |
| Zapier Professional | ~$50/month | Accounting sync automation |
| **Total** | **~$665/month** | Complete time-to-invoice workflow |

### Workflow: Time to Invoice

```
1. Consultant tracks time in ClickUp
   └── Timer or manual entry
   └── Billable flag set
   └── Task associated with client project

2. Everhour calculates billing
   └── Applies consultant's rate
   └── Rounds per project settings
   └── Tracks against budget

3. Weekly/Monthly review
   └── Manager reviews in Everhour
   └── Adjustments made if needed
   └── Time approved

4. Invoice generation
   └── Everhour generates invoice
   └── OR Export to accounting system
   └── OR Zapier creates invoice in QBO/Xero

5. Client receives invoice
   └── Detailed time breakdown
   └── By task/project/consultant
```

## Vacation & Capacity Tracking

### Out of Office Tasks

Track PTO and unavailability:

```
Task: [Name] - PTO
├── Start Date: First day out
├── Due Date: Last day out
├── Time Estimate: Total OOO hours (e.g., 40h for 1 week)
├── Assignee: Person taking PTO
└── List: Capacity Tracking (or Operations)
```

**Result:** Shows in Workload view, blocks capacity.

### Capacity Custom Field

For non-standard schedules:

```
Custom Field: Weekly Capacity (Number)
- Full-time: 40
- Part-time: 20
- Contractor: varies

Use in Workload view configuration.
```

## Reporting Best Practices

### Weekly Time Review

1. Timesheets → Filter by This Week
2. Review total hours per person
3. Check billable ratio
4. Identify missing time entries
5. Follow up before week closes

### Monthly Client Reporting

1. Filter time by client Folder
2. Export to CSV
3. Summarize by task/phase
4. Include in client invoice or status report

### Utilization Reporting (Manual)

Until native utilization exists:

1. Export time data monthly
2. Calculate per-person:
   - Total hours tracked
   - Billable hours
   - Utilization % = Billable / Capacity
3. Track trend over time in spreadsheet

### Budget Monitoring

With Custom Fields:
1. Create Dashboard with Calculation cards
2. Show Budget Hours vs Time Tracked
3. Color-code by Budget Consumed %
4. Review weekly in PM meeting
