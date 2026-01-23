---
name: clickup-automation-architect
description: Design, build, and optimize ClickUp automations for consulting workflows. Use when users need to create automations, build approval workflows, set up client onboarding sequences, optimize automation usage against monthly limits, troubleshoot failing automations, or migrate manual processes to automated workflows. Includes ready-to-use recipes for consulting firms and limit optimization strategies.
---

# ClickUp Automation Architect

Design and implement ClickUp automations optimized for consulting workflows and monthly action limits.

## Quick Reference

| Need | Reference |
|------|-----------|
| Ready-to-use consulting recipes | `references/recipes.md` |
| Optimize against 10k/month limit | `references/optimization.md` |
| Troubleshoot failures | `references/troubleshooting.md` |
| Estimate monthly usage | Run `scripts/estimate_usage.py` |

## Core Concepts

**Automation formula:** `WHEN [trigger] → THEN [action(s)]`

**Where automations live:**
- Space level → affects all tasks in Space
- Folder level → affects all Lists within Folder
- List level → affects only that List

**Business tier limits:**
- 10,000 actions/month (resets 1st of month, PST)
- Enterprise: 250,000 actions/month
- One automation with multiple actions = 1 action count
- Alerts sent at 90% and 100%; exceeding pauses ALL workspace automations

## Workflow

### 1. Understand the Process

Before building, map the manual workflow:

```
Current state: What happens manually today?
Trigger point: What event starts the process?
Decision points: Any conditional branching?
Actions needed: What changes/notifications occur?
Frequency: How often will this fire?
```

### 2. Select Pattern

**Status-based workflow** — Use when work moves through stages
```
Trigger: Status changes to X
Actions: Notify, assign, create subtasks, update fields
```

**Time-based workflow** — Use for deadlines, reminders, escalations
```
Trigger: Due date arrives / X days before due / Task overdue
Actions: Alert, reassign, change priority
```

**Field-based workflow** — Use when data drives behavior
```
Trigger: Custom Field changes / changes to specific value
Actions: Route, categorize, calculate
```

**Creation-based workflow** — Use for standardization and setup
```
Trigger: Task created / Task created in List X
Actions: Apply template, set defaults, notify owner
```

### 3. Build the Automation

1. Navigate to Space/Folder/List where automation should live
2. Click "Automate" → "Add Automation"
3. Select trigger from categories (Task, Time, Custom Field)
4. Add conditions to filter (Business+ required for conditions)
5. Add actions in sequence
6. Name descriptively: `[Trigger] → [Primary Action] (Location)`
7. Test with a real task before enabling

### 4. Validate and Monitor

After enabling:
- Create test task to verify behavior
- Check Automate → Manage Automations → Activity tab
- Monitor usage in Activity → Usage tab
- Document in team wiki for maintenance

## Consulting Automation Patterns

### Client Onboarding (Most Common)

```
Trigger: Task created
Condition: List is "Client Onboarding"
Actions:
  1. Apply template "Client Onboarding Checklist"
  2. Set due date to 14 days from now
  3. Add comment "Onboarding initiated - see checklist"
  4. Add watcher: Account Manager Team
```

Estimated usage: 4 actions × projects/month

### Milestone Completion Alert

```
Trigger: Status changes to "Complete"
Condition: Tag contains "Milestone"
Actions:
  1. Send email to Custom Field "Client Contact"
  2. Create task "Invoice for [task name]" in Billing List
  3. Add comment "Milestone delivered"
```

Estimated usage: 3 actions × milestones/month

### Approval Routing

```
Trigger: Status changes to "Pending Approval"
Condition: Priority is High or Urgent
Actions:
  1. Add assigned comment to Custom Field "Approver"
  2. Set Custom Field "Review Submitted" to TODAY
  3. Change priority to Urgent (if not already)
```

Estimated usage: 3 actions × approval requests/month

### Missing Time Entry Detection

```
Trigger: Status changes to "Complete"
Condition: Time tracked equals 0
Actions:
  1. Add assigned comment "⚠️ No time logged - please add"
  2. Change status back to "In Review"
```

Estimated usage: 2 actions × completions without time

### Weekly Status Report Trigger

```
Trigger: Every Friday at 9am
Condition: None
Actions:
  1. Create task "Weekly Status Report" from template
  2. Assign to Project Manager
  3. Set due date to today
```

Estimated usage: 3 actions × weeks = ~12/month

For additional recipes, see `references/recipes.md`.

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Automation loops | Status A triggers status B triggers status A | Add condition to break cycle |
| Notification flood | Every status change notifies everyone | Filter to critical statuses only |
| Hardcoded assignees | Breaks when people leave | Use Custom Field "Owner" or role-based assignment |
| Automating undefined processes | Automates bad process faster | Map and fix manual workflow first |
| Too many separate automations | Hard to maintain, burns limits | Consolidate triggers with conditions |

## Limit Optimization

When approaching 10,000/month limit:

1. **Consolidate triggers** — One automation with conditions beats five separate automations
2. **Use webhooks** — Webhooks don't count against limits; offload logic to Make/Zapier
3. **Batch with templates** — Pre-populate subtasks in templates instead of automation-created subtasks
4. **Add precise conditions** — Filter out test tasks, non-critical statuses, empty assignees
5. **Move complex logic externally** — Make.com and Zapier handle branching ClickUp can't

See `references/optimization.md` for detailed strategies.

## Troubleshooting

**Automation not firing:**
- Check conditions aren't too restrictive
- Verify trigger event actually occurred
- Confirm automation is enabled (toggle ON)
- Check if monthly limit exceeded

**Automation fires unexpectedly:**
- Review conditions for gaps
- Check if multiple automations overlap
- Verify trigger scope (Space vs List level)

**Error: "Value must be option index or uuid":**
- Dropdown mapping issue
- Use Formatter to map option names to IDs

**Automation auto-disabled:**
- 5 failures in one week auto-deactivates
- Check Activity tab for error details
- Fix root cause, then re-enable

See `references/troubleshooting.md` for complete error reference.
