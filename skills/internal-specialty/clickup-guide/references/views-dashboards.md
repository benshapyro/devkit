# Views & Dashboards

How to create effective views and dashboards for consulting workflows.

## View Types Overview

### Task Views (Display Existing Tasks)

| View | Best For | Consulting Use Case |
|------|----------|---------------------|
| **List** | Daily task management, bulk editing, detailed info | Personal to-do, task cleanup, data entry |
| **Board** | Kanban workflows, visual progress tracking | Delivery pipeline, approval flow |
| **Calendar** | Deadline tracking, scheduling | Milestone planning, due date visibility |
| **Gantt** | Dependencies, timeline visualization | Project planning, critical path |
| **Timeline** | Roadmaps, resource planning, portfolio | Multi-project overview, capacity |
| **Table** | Spreadsheet-like management, data entry | Custom Field heavy work, bulk updates |
| **Workload** | Capacity planning, resource allocation | Team utilization, assignment balancing |
| **Box/Team** | Workload by assignee | Who's overloaded, task distribution |

### Content Views (Create New Content)

| View | Best For | Consulting Use Case |
|------|----------|---------------------|
| **Doc** | Documentation, meeting notes, SOPs | Client deliverables, internal wikis |
| **Whiteboard** | Brainstorming, diagramming | Workshop facilitation, architecture |
| **Form** | Intake, requests, feedback | Client requests, internal submissions |
| **Dashboard** | KPIs, metrics, status reporting | Executive visibility, client updates |

## View Selection by Role

| Role | Primary Views | Why |
|------|---------------|-----|
| **Consultant** | List (My Tasks), Board (project) | Daily work, progress tracking |
| **Project Manager** | Board, Gantt, Workload | Delivery oversight, resource planning |
| **Partner/Principal** | Dashboard, Timeline | Portfolio health, high-level status |
| **Client (Guest)** | Board or Table (filtered) | Simple visibility, progress tracking |

## Essential Views to Create

### Personal Productivity Views

**"My Tasks" (Everything Level)**
```
Location: Everything (All Tasks)
View Type: List
Filters:
  - Assignee IS [Me]
  - Status IS NOT Complete, Cancelled
Group by: Due Date
Sort by: Priority (Descending)
```

**"Due This Week" (Everything Level)**
```
Location: Everything
View Type: List
Filters:
  - Assignee IS [Me]
  - Due Date IS This Week
  - Status IS NOT Complete
Sort by: Due Date (Ascending)
```

### Project Delivery Views

**"Delivery Pipeline" (Delivery Space)**
```
Location: DELIVERY Space
View Type: Board
Group by: Status
Filters:
  - Status IS NOT Complete, Cancelled
Show: Task name, Assignee, Due Date, Client Name
```

**"All Active Engagements" (Delivery Space)**
```
Location: DELIVERY Space
View Type: Table
Filters:
  - Engagement Status IS Active
Columns: Task Name, Client Name, Project Manager, Due Date, Health Status, Budget Consumed %
Group by: Client Name
```

**"Project Gantt" (Client Folder)**
```
Location: [Client] Folder
View Type: Gantt
Settings:
  - Show Dependencies: ON
  - Show Critical Path: ON
  - Color by: Status
  - Show Milestones: ON
```

### Resource Management Views

**"Team Workload" (Delivery Space)**
```
Location: DELIVERY Space
View Type: Workload
Settings:
  - Measure by: Time Estimates
  - Time Period: 2 Weeks
  - Show Subtasks: ON (critical!)
Capacity: Set per person (e.g., 40h/week)
```

**"Who's Behind" (Everything Level)**
```
Location: Everything
View Type: List
Filters:
  - Status IS NOT Complete
  - Due Date IS Overdue
Group by: Assignee
Sort by: Due Date (Ascending)
```

### Client-Facing Views

**"Client Progress Board"**
```
Location: [Client] Folder
View Type: Board
Filters:
  - List IS NOT "Internal Notes"
  - Tag DOES NOT CONTAIN "internal"
Columns: To Do, In Progress, In Review, Complete
Show: Task name, Due Date, Status
Hide: Time tracking, internal Custom Fields
```

**"Client Deliverables Table"**
```
Location: [Client] Folder
View Type: Table
Filters:
  - Tag CONTAINS "Deliverable"
  - List IS NOT "Internal Notes"
Columns: Task Name, Status, Due Date, Progress
```

## Dashboard Design

### Dashboard Limitations

**⚠️ Critical:** ClickUp does NOT support public Dashboard sharing. Dashboards require login.

**Workarounds for client visibility:**
1. **Guest Access** — Invite client as Guest, share Dashboard
2. **Scheduled Email** — Dashboard → Share → Schedule report → PDF to recipients
3. **Embedded Views in Doc** — Create public Doc with embedded views

**Other limitations:**
- Sprint cards update at 4am daily (not real-time)
- Max ~50 cards per dashboard for performance
- Cannot embed dashboard cards in Docs
- No cross-workspace data

### Widget Categories

| Category | Widgets | Use For |
|----------|---------|---------|
| **Status** | Workload by Status, Tasks by Status | Progress distribution |
| **Assignee** | Tasks by Assignee, Who's Behind | Workload visibility |
| **Time** | Time Reporting, Billable Report, Est vs Actual | Utilization, billing |
| **Sprint** | Burndown, Burnup, Velocity | Agile metrics |
| **Charts** | Bar, Pie, Line, Battery | Visual metrics |
| **Text/Embed** | Text Block, Embed | Context, external content |
| **Task Lists** | Task List, Filtered Tasks | Specific task views |

### Consulting Dashboard Templates

**Executive Portfolio Dashboard**
```
Purpose: Leadership visibility across all clients

Widgets:
├── Portfolio Card: All active engagements (Health Status coloring)
├── Pie Chart: Tasks by Client (distribution)
├── Bar Chart: Budget Consumed % by Client
├── Task List: Overdue items (filtered, max 10)
├── Time Reporting: This month by client
└── Text Block: Key updates (manually maintained)
```

**Project Health Dashboard (Per Client)**
```
Purpose: Single engagement tracking

Widgets:
├── Battery: Project Progress (% complete)
├── Pie Chart: Tasks by Status
├── Bar Chart: Time Estimated vs Tracked
├── Task List: Milestones (filtered by tag)
├── Task List: Blocked items
├── Workload by Status: Task distribution
└── Time Reporting: Hours this week
```

**Team Utilization Dashboard**
```
Purpose: Resource management visibility

Widgets:
├── Time Reporting: By assignee (bar chart)
├── Pie Chart: Billable vs Non-billable
├── Workload: Capacity vs assigned
├── Who's Behind: Overdue by person
├── Task List: Unassigned tasks
└── Calculation Card: Total hours this week
```

**Client Status Dashboard (for Guest sharing)**
```
Purpose: Client visibility (simplified)

Widgets:
├── Battery: Overall progress
├── Task List: Completed this week
├── Task List: In progress now
├── Task List: Coming up next week
├── Pie Chart: Status distribution
└── Text Block: Next milestone date
```

### Dashboard Best Practices

1. **One purpose per dashboard** — Don't combine executive overview with detailed project tracking
2. **Limit to 10-15 widgets** — More causes performance issues and cognitive overload
3. **Use consistent time ranges** — This Week, This Month, etc.
4. **Add text blocks for context** — Explain what metrics mean
5. **Filter aggressively** — Show only relevant data, not everything
6. **Protect dashboards** — Right-click → Protect to prevent accidental changes
7. **Name clearly** — "Delivery Portfolio" not "Dashboard 1"

## "Everything" Views

Views at Workspace level showing tasks across ALL Spaces you can access.

### Accessing Everything Views

1. Click "Spaces" in Global Navigation
2. Select "All Tasks"
3. Click "+View" to add views at this level

### Powerful Everything View Patterns

**Cross-Project My Tasks:**
```
Filter: Assignee IS [Me], Status NOT Complete
Group by: Space (shows work by department)
```

**All Client Milestones:**
```
Filter: Tag CONTAINS "Milestone", Space IS "Delivery"
Group by: Client Name
Sort by: Due Date
```

**Company-Wide Overdue:**
```
Filter: Due Date IS Overdue, Status NOT Complete
Group by: Assignee
```

### Everything View Limitations

- Cannot edit tasks from some protected Spaces
- Large workspaces may have performance issues
- Filters become critical to manage volume

## View Permissions

| Type | Visibility | Editable By |
|------|------------|-------------|
| **Public** | Everyone with location access | Anyone with edit permissions |
| **Private** | Only creator | Only creator |
| **Protected** | Everyone with access | Only those who can unprotect |

### When to Use Each

**Public Views:**
- Team standards everyone uses
- Client-facing views
- Onboarding views for new team members

**Private Views:**
- Personal filters and sorts
- Experimental layouts
- Views with sensitive filters

**Protected Views:**
- Prevent accidental changes to team views
- Lock down client-facing views
- Preserve carefully configured views

### Protecting a View

1. Right-click view tab
2. Select "Protect view"
3. Only Admins and Owner can unprotect

## Form Views

Forms create tasks from external submissions.

### Form Use Cases for Consulting

| Form | Purpose | Destination List |
|------|---------|------------------|
| Client Request Form | Support/change requests | Client Retainer List |
| Project Intake | New engagement requests | Pipeline List |
| Feedback Form | Client satisfaction | Feedback tracking List |
| Internal Request | Team resource requests | Operations List |

### Form Configuration

1. Navigate to destination List
2. Click "+View" → "Form"
3. Add questions (map to task fields and Custom Fields)
4. Configure submission behavior:
   - Apply template on submission
   - Auto-assign to specific person
   - Set default status

### Form Limitations (Business Tier)

**⚠️ Conditional logic requires Business Plus or Enterprise.**

**Workarounds:**
- Create multiple simpler forms for different scenarios
- Use external forms (Typeform, Jotform) with Zapier integration
- Post-submission automations to route tasks

### Sharing Forms

- Click "Copy link" in form edit mode
- Share URL—no ClickUp account needed to submit
- Embed code available for websites
