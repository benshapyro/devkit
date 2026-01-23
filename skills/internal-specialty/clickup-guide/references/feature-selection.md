# Feature Selection Guide

Decision frameworks for choosing between similar ClickUp features.

## Subtasks vs Checklists

The most common question. Both break work into smaller pieces, but serve different purposes.

### Capability Comparison

| Capability | Subtasks | Checklists |
|------------|----------|------------|
| Own assignees | ✅ Yes | ⚠️ Limited (one per item) |
| Due dates | ✅ Yes | ❌ No |
| Own status | ✅ Yes | ❌ Done/not done only |
| Custom Fields | ✅ Yes | ❌ No |
| Appears in views/reports | ✅ Yes | ❌ No |
| Time tracking | ✅ Yes | ❌ No |
| Dependencies | ✅ Yes | ❌ No |
| Nested levels | ✅ Multiple | ❌ Flat only |
| Comments | ✅ Yes | ❌ No |

### Decision Framework

**Use SUBTASKS when:**
- Work requires different people at different times
- Items need their own due dates and timelines
- Progress needs tracking in views and reports
- You need time tracking on individual items
- Dependencies exist between items
- Items might become blocked independently

**Use CHECKLISTS when:**
- Simple yes/no completion tracking
- Items done by same person in one session
- Creating SOPs or quality assurance lists
- Quick reminders ("Don't forget to...")
- Order doesn't matter or is just suggested
- No need to report on individual items

### Consulting Examples

**Subtasks — Project Phases:**
```
Task: Q4 Strategy Engagement
├── Subtask: Phase 1 - Discovery (3 days, Senior Consultant)
├── Subtask: Phase 2 - Analysis (5 days, Analyst)
├── Subtask: Phase 3 - Recommendations (4 days, Principal)
└── Subtask: Phase 4 - Final Delivery (2 days, Partner)
```
Why subtasks: Different assignees, different durations, need to track time per phase.

**Checklist — Presentation Prep:**
```
Task: Client Presentation - Friday
Checklist:
  ☐ Check slides for typos
  ☐ Verify data sources cited
  ☐ Test screen share
  ☐ Send calendar reminder
  ☐ Print backup copies
```
Why checklist: Same person, one session, just quality reminders.

**Checklist — Deliverable QA:**
```
Task: Final Report Delivery
Checklist:
  ☐ Executive summary complete
  ☐ All charts labeled
  ☐ Sources cited
  ☐ Spell check run
  ☐ PDF exported
  ☐ Client name correct throughout
```
Why checklist: Quality gate before marking complete, no separate tracking needed.

---

## Docs vs Task Descriptions

Both hold text content, but serve different purposes in workflows.

### When to Use DOCS

- **Long-form content** (more than 1 page)
- **Reference materials** that outlive individual tasks
- **SOPs and wikis** that multiple tasks reference
- **Meeting agendas and notes** that need nested structure
- **Client-facing documentation** for sharing
- **Collaboration** where multiple people edit simultaneously
- **Version history** is important

**Doc examples:**
- Project charter
- Meeting notes archive
- Client onboarding guide
- Competitive analysis report
- Process documentation

### When to Use TASK DESCRIPTIONS

- **Actionable items** with due dates and assignees
- **Content needing status tracking** through workflow
- **Work requiring notifications** when things change
- **Short context** (few paragraphs) for the task
- **Activity log** of changes is needed

**Task description examples:**
- Brief for a specific deliverable
- Requirements for a single feature
- Context for a support request
- Instructions for task completion

### Hybrid Pattern: Doc-Linked Tasks

For major deliverables, use both:

```
Doc: "Q4 Strategy Report" (the actual content)
  └── Linked Task: "Complete Q4 Strategy Report"
       ├── Status: In Progress
       ├── Due: Dec 15
       ├── Assignee: Principal
       └── Description: "Link to doc: [Q4 Strategy Report]"
```

The Doc holds the content. The Task tracks the work. Link them together.

---

## Goals vs Tasks for OKRs

ClickUp has a Goals feature, but it has limitations for OKR tracking.

### Goals Feature Capabilities

| Capability | Available |
|------------|-----------|
| Progress tracking | ✅ Yes (Number, Currency, True/False, Task-based) |
| Target dates | ✅ Yes |
| Ownership | ✅ Yes |
| Folder organization | ✅ Yes |
| Link to tasks | ✅ Yes |
| Comments on goals | ❌ No |
| Check-in history | ❌ No |
| Confidence scoring | ❌ No |
| Health indicators | ❌ No |
| Weighted key results | ❌ No |
| Automated reminders | ❌ No |

### Recommendation: Hybrid Approach

**For simple OKR tracking:**
Use Goals feature with this mapping:
- Company Objective → Goal Folder
- Objective → Goal
- Key Result → Target (Number/Currency/Task/True-False)
- Initiatives → Linked Tasks

**For robust OKR management:**
Use Tasks with Custom Fields:
```
Space: OKRs & Goals
└── Folder: 2025 Company OKRs
    └── List: Q4 2025
        └── Task: OBJECTIVE - [Goal Name]
            ├── Subtask: KR1 - [Key Result]
            ├── Subtask: KR2 - [Key Result]
            └── Subtask: KR3 - [Key Result]

Custom Fields:
- OKR Type (Dropdown: Objective / Key Result / Initiative)
- Progress % (Number)
- Confidence Level (Dropdown: High / Medium / Low)
- Owner (People)
- Quarter (Dropdown)
```

**Workarounds for Goals limitations:**
- Use linked Docs for check-in notes and updates
- Create recurring tasks for weekly OKR reviews
- Add Custom Fields to linked tasks for health status

---

## Templates vs Recurring Tasks

Both help with repeated work, but work differently.

### Task Templates

**What they do:** Save a task structure (subtasks, checklists, description, Custom Fields) to reuse.

**Best for:**
- Complex tasks with consistent structure
- Onboarding processes
- Project phase kickoffs
- Deliverable creation

**Limitations:**
- Formula fields don't transfer
- Must manually apply each time (or use automation)
- Can't edit template after creation (must re-save)

### Recurring Tasks

**What they do:** Automatically create new task on schedule or when previous completes.

**Best for:**
- Regular cadence work (weekly reports, monthly reviews)
- Maintenance tasks
- Reminders that repeat

**Options:**
- **On Schedule:** Creates regardless of completion
- **When Closed:** Only creates after current one complete

**Settings to configure:**
- What copies over (subtasks, Custom Fields, assignees)
- Recurrence pattern (daily, weekly, monthly, custom)

### Decision Framework

| Scenario | Use |
|----------|-----|
| Same structure, ad-hoc creation | Template |
| Same structure, predictable schedule | Recurring Task |
| Complex onboarding, triggered by event | Template + Automation |
| Weekly status report every Friday | Recurring Task |
| New client setup (when deal closes) | Template (applied via Zapier) |

---

## Private vs Public Views

Views can be private (only you see) or public (team sees).

### Private Views

**Use for:**
- Personal task filters ("My Tasks Due This Week")
- Experimental layouts you're testing
- Custom sorts that only matter to you
- Sensitive filters (performance tracking)

**Creating:** Check "Private view" when creating

### Public Views

**Use for:**
- Team standards everyone should use
- Client-facing views (shared with guests)
- Dashboards for reporting
- Onboarding views for new team members

**Protecting:** Right-click → "Protect view" to prevent accidental changes

### Shared Private Views

Middle ground: Private but shared with specific people.

**Use for:**
- Leadership views not for whole team
- Project-specific views for core team only
- Views with sensitive filters

---

## Native Time Tracking vs Integrations

ClickUp has built-in time tracking, but gaps exist for consulting billing.

### Native Time Tracking Capabilities

| Capability | Available |
|------------|-----------|
| Start/stop timer | ✅ Yes |
| Manual entry | ✅ Yes |
| Billable flag | ✅ Yes |
| Notes on entries | ✅ Yes |
| Timesheet view | ✅ Yes |
| Export to CSV | ✅ Yes |
| Per-user billing rates | ❌ No |
| Per-client billing rates | ❌ No |
| Time rounding rules | ❌ No |
| Invoicing | ❌ No |
| Utilization % calculation | ❌ No |

### When to Use Native

- Internal time tracking only
- Single billing rate for all work
- Simple billable/non-billable split
- No invoicing from ClickUp needed

### When to Add Everhour

- Multiple billing rates (by person or project)
- Need time rounding (nearest 15 min)
- Want invoice generation
- Need utilization reporting
- Budgets with alerts

See `references/time-billing.md` for detailed Everhour setup.

---

## Comments vs Assigned Comments

Regular comments notify watchers. Assigned comments create action items.

### Regular Comments

- Notify all watchers and assignees
- Good for updates, questions, FYIs
- Appear in activity feed
- Can @mention specific people

### Assigned Comments

- Create a required action item
- Appear in assignee's "Assigned Comments" inbox
- Must be resolved (marked complete)
- Track accountability for responses

**When to use Assigned Comments:**
- Need specific person to respond
- Action required, not just FYI
- Want to track that response happened
- Following up on decisions needed

**Creating:** Click "Assign" button while drafting comment → Select person
