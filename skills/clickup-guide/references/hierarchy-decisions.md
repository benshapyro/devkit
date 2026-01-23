# Hierarchy Decisions for Consulting Firms

How to structure ClickUp for a consulting firm with multiple clients and engagement types.

## The ClickUp Hierarchy

```
Workspace (Your organization - one per company)
└── Space (Department/functional area - owns its own settings)
    └── Folder (Project container - groups related Lists)
        └── List (Task collection - where tasks live)
            └── Task (Individual work item)
                └── Subtask (Smaller work breakdown)
```

**Key constraints:**
- Tasks MUST exist inside Lists (cannot exist alone)
- Folders are optional—Lists can exist directly in Spaces
- Each Space has its own statuses, ClickApps, and settings
- Business tier: 400 Lists per Space, 400 Folders per Space

## Decision Framework

### When to Create a SPACE

Create a new Space when you need:
- **Different workflows/statuses** — Delivery work moves through different stages than Sales pipeline
- **Different team access** — Not everyone should see HR or Finance data
- **Different ClickApps enabled** — Some teams need Sprints, others don't

**Consulting examples:**
- DELIVERY — All client project work
- GROWTH — Sales pipeline, marketing, business development
- OPERATIONS — HR, finance, admin, internal projects
- PROCESS LIBRARY — Templates and SOPs

### When to Create a FOLDER

Create a new Folder when you need:
- **Grouping related projects** within the same workflow
- **Complex project with multiple phases** that share statuses
- **Permission boundary** for client guest access

**Consulting examples:**
- One Folder per client (containing all their engagements)
- One Folder per major initiative (containing workstreams)
- One Folder per quarter for OKRs

### When to Create a LIST

Create a new List when you need:
- **Tasks sharing similar outcomes** or types
- **Single project phase** or workstream
- **Separation within a Folder** for different purposes

**Consulting examples:**
- "Active Engagement" — Current project tasks
- "Retainer Support" — Ongoing support requests
- "Internal Notes" — Team-only items (never share with client)

## The Client = Folder Pattern (Recommended)

```
SPACE: DELIVERY
├── FOLDER: Acme Corp
│   ├── LIST: Q4 Strategy Engagement
│   ├── LIST: Implementation Phase 1
│   ├── LIST: Retainer Support
│   └── LIST: Internal Notes
├── FOLDER: Beta Industries
│   ├── LIST: Assessment Project
│   └── LIST: Internal Notes
└── FOLDER: Gamma Holdings
    ├── LIST: Digital Transformation
    ├── LIST: Change Management
    └── LIST: Internal Notes
```

**Why this works:**

1. **Cross-client visibility** — See all client work in one Space view
2. **Roll-up reporting** — Dashboard at Space level shows all delivery metrics
3. **Consistent statuses** — All client work uses same workflow stages
4. **Permission control** — Share Folder with client guest, exclude Internal Notes List
5. **Scalability** — Add new clients as Folders without restructuring

## The Anti-Pattern: Space per Client

```
❌ DON'T DO THIS:
├── SPACE: Acme Corp
├── SPACE: Beta Industries
├── SPACE: Gamma Holdings
├── SPACE: Delta Corp
└── ... (fragments into dozens of Spaces)
```

**Why this fails:**

1. **Fragmented views** — Can't see all client work in one place
2. **No cross-client reporting** — Dashboards only work within one Space
3. **Duplicate statuses** — Must recreate workflow in each Space
4. **Settings sprawl** — Each Space needs separate configuration
5. **Navigation nightmare** — Sidebar becomes unusable with 20+ Spaces

## Separating Internal from Client-Visible

For each client Folder, maintain separation:

| List | Shareable? | Contents |
|------|------------|----------|
| Active Engagement | ✅ Yes | Tasks, milestones, deliverables client can see |
| Implementation | ✅ Yes | Technical work with client visibility |
| Internal Notes | ❌ Never | Strategy discussions, pricing, risk assessments, team feedback |

**What to keep internal:**
- Profit margin calculations
- Risk assessments and flags
- Team feedback and retrospectives
- Pricing and negotiation notes
- Other client references (confidentiality)

## Engagement Type Templates

### Strategy Engagement Structure

```
FOLDER: [Client] - Strategy Engagement
├── LIST: Discovery & Analysis
│   └── Statuses: Planning → In Progress → Analysis → Complete
├── LIST: Recommendations
│   └── Statuses: Drafting → Internal Review → Client Review → Final
├── LIST: Deliverables
│   └── Statuses: Not Started → In Progress → Review → Delivered
└── LIST: Internal Notes
```

### Implementation Project Structure

```
FOLDER: [Client] - Implementation
├── LIST: Backlog
│   └── Statuses: Backlog → Ready → In Progress → Done
├── LIST: Current Sprint
│   └── Statuses: To Do → In Progress → Review → Complete
├── LIST: Deployments
│   └── Statuses: Planned → Staging → Production → Verified
└── LIST: Internal Notes
```

### Retainer/Support Structure

```
FOLDER: [Client] - Retainer
├── LIST: Support Requests
│   └── Statuses: Requested → Triaged → In Progress → Complete
├── LIST: Monthly Hours Tracking
│   └── Custom Fields: Hours Allocated, Hours Used, Rollover
└── LIST: Internal Notes
```

## Status Recommendations by Space

### DELIVERY Space (Client Work)

```
Standard Project Statuses:
├── TO DO GROUP
│   ├── Backlog
│   └── Ready to Start
├── ACTIVE GROUP
│   ├── In Progress
│   ├── In Review
│   ├── Client Review
│   └── Blocked
└── COMPLETE GROUP
    ├── Complete
    └── Cancelled
```

### GROWTH Space (Sales)

```
Pipeline Statuses:
├── TO DO GROUP
│   ├── Lead
│   └── Qualified
├── ACTIVE GROUP
│   ├── Proposal Sent
│   ├── Negotiation
│   └── Contract Review
└── COMPLETE GROUP
    ├── Closed Won
    └── Closed Lost
```

## Naming Conventions

Consistent naming improves navigation and filtering:

**Folders:**
```
[Client Name] - [Engagement Type]
Examples:
  Acme Corp - Q4 Strategy
  Beta Industries - Implementation
  Gamma Holdings - Retainer 2025
```

**Lists:**
```
[Purpose] or [Phase Name]
Examples:
  Active Engagement
  Sprint 3
  Internal Notes
  Deliverables
```

**Tasks:**
```
[Action verb] [Object]
Examples:
  Draft executive summary
  Review competitive analysis
  Schedule kickoff meeting
```

## Migration Path: From Messy to Organized

If current structure doesn't follow these patterns:

**Phase 1: Consolidate Spaces**
1. Create new "DELIVERY" Space with correct statuses
2. Move client Folders from separate Spaces into DELIVERY
3. Archive empty Spaces

**Phase 2: Standardize Folders**
1. Rename Folders to consistent convention
2. Add "Internal Notes" List to each client Folder
3. Move sensitive tasks to Internal Notes

**Phase 3: Clean Up Lists**
1. Archive completed/stale Lists
2. Consolidate duplicate Lists
3. Apply consistent naming

**Tip:** Do migration during low-activity period. Notify team before making changes.
