---
name: clickup-guide
description: Consulting-firm-specific ClickUp guidance for structure, permissions, features, and workarounds. Use when users ask how to organize projects, whether clients can see something, what custom fields to use, which features to choose (subtasks vs checklists, docs vs descriptions), view/dashboard setup, time tracking limitations, or ClickUp's known gaps. Optimized for 30-person consulting firms on Business tier with client guest access needs.
---

# ClickUp Consulting Guide

Consulting-specific guidance for ClickUp structure, features, and workarounds. Optimized for Cadre AI's 30-person team on Business tier.

## Quick Reference

| Question | Reference |
|----------|-----------|
| How should I organize client projects? | `references/hierarchy-decisions.md` |
| Can clients see this? | `references/permissions-guests.md` |
| What custom fields do I need? | `references/custom-fields.md` |
| Subtasks vs checklists? Docs vs descriptions? | `references/feature-selection.md` |
| What views/dashboards should I create? | `references/views-dashboards.md` |
| How do I track billable time? | `references/time-billing.md` |
| What can't ClickUp do? | `references/limitations-workarounds.md` |

## Routing to Other Skills

**Automation questions?** → Use `clickup-automation-architect` skill for:
- Building automations and approval workflows
- Client onboarding sequences
- Monthly limit optimization
- Troubleshooting failed automations

## Core Decision Frameworks

### Space vs Folder vs List

| Use This | When | Consulting Example |
|----------|------|-------------------|
| **Space** | Different workflow/statuses needed; different team access | "Delivery", "Growth", "Operations" |
| **Folder** | Grouping related projects; complex project with phases | One folder per client |
| **List** | Tasks share similar outcome; single project phase | "Active Engagement", "Retainer Support" |

**Decision tree:**
1. Need different statuses/workflows? → **Space**
2. Need different team access/permissions? → **Space**
3. Complex project with multiple phases? → **Folder** with Lists inside
4. Grouping related work items? → **List**

**⚠️ Critical:** Don't create a Space per client—fragments views and prevents cross-client reporting. Use Folders per client within shared "Delivery" Space.

### Subtasks vs Checklists

| Feature | Subtasks | Checklists |
|---------|----------|------------|
| Own assignees | ✅ Yes | ⚠️ Limited |
| Due dates | ✅ Yes | ❌ No |
| Own status | ✅ Yes | ❌ Done/not done only |
| Custom Fields | ✅ Yes | ❌ No |
| Appears in views/reports | ✅ Yes | ❌ No |
| Time tracking | ✅ Yes | ❌ No |

**Use SUBTASKS when:** Different people, different timelines, need tracking in reports, need time logging.

**Use CHECKLISTS when:** Same person, one session, simple yes/no, SOPs, quick reminders.

### Docs vs Task Descriptions

**Use DOCS when:**
- Long-form content (1+ pages)
- Reference materials, SOPs, wikis
- Meeting agendas/notes
- Client-facing documentation

**Use TASK DESCRIPTIONS when:**
- Actionable items needing due dates
- Content requiring status tracking
- Work needing assignees and notifications

### View Selection

| View | Best For |
|------|----------|
| **List** | Daily task management, bulk editing |
| **Board** | Kanban workflows, visual progress |
| **Calendar** | Deadline tracking, scheduling |
| **Gantt** | Dependencies, timeline visualization |
| **Table** | Data entry, spreadsheet-like management |
| **Workload** | Capacity planning (requires time estimates) |
| **Dashboard** | KPIs, status reporting, team metrics |

## Recommended Consulting Structure

```
WORKSPACE: Cadre AI
├── SPACE: DELIVERY (all client work)
│   ├── FOLDER: [Client Name]
│   │   ├── LIST: Active Engagement
│   │   ├── LIST: Implementation Phase
│   │   └── LIST: Internal Notes (never share)
│   └── [Additional client folders...]
├── SPACE: GROWTH (sales, marketing, BD)
├── SPACE: OPERATIONS (HR, finance, admin)
└── SPACE: PROCESS LIBRARY (templates)
```

**Why this works:**
- Client = Folder enables cross-client visibility at Space level
- Roll-up reporting across all clients from Delivery Space
- Permissions controlled at Folder level for guest access
- Consistent statuses across all client work

## Essential Custom Fields for Consulting

| Field | Type | Purpose |
|-------|------|---------|
| Client Name | Dropdown | Filter, group, report by client |
| Project Type | Dropdown | Strategy / Implementation / Assessment |
| Engagement Status | Dropdown | Onboarding / Active / Closing / Complete |
| Billable | Checkbox | Track billable vs internal work |
| Client Contact | Email | For automated notifications |
| Project Manager | People | Single owner for accountability |

## Anti-Patterns to Avoid

| Don't | Why | Do Instead |
|-------|-----|------------|
| Space per client | Fragments views, kills reporting | Folder per client in shared Space |
| Share internal notes with guests | Confidentiality breach | Separate "Internal Notes" List, never share |
| Multiple assignees per task | Diffuses accountability, breaks Workload | One assignee + watchers |
| Skip time estimates | Workload view useless without them | Estimate everything, even roughly |
| Hardcode people in automations | Breaks when people leave | Use Custom Field "Owner" role |

## Business Tier Quick Facts

- **Cost:** $12/user/month (annual)
- **Automations:** 10,000/month
- **API Rate:** 100 requests/minute
- **Guests:** 5 free, then $5/month each
- **SSO:** Google only (Enterprise adds Microsoft, Okta, SAML)
- **Storage:** Unlimited

## When to Consider Enterprise

- Non-Google SSO required
- Hitting 10,000 automation limit
- API integrations exceeding 100/min
- Need audit logs for compliance
- Custom roles beyond Member/Admin/Guest
- HIPAA compliance for healthcare clients
