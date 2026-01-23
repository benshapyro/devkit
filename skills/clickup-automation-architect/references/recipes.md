# Consulting Automation Recipes

Ready-to-implement automation patterns for consulting firms. Copy trigger/condition/action configurations directly into ClickUp.

## Client Lifecycle Automations

### New Client Folder Setup

**When to use:** New client wins from CRM or manual creation

```
Trigger: Folder created
Condition: Space is "Delivery"
Actions:
  1. Create List "Active Engagement" in folder
  2. Create List "Internal Notes" in folder
  3. Add comment "Client folder created - apply templates to Lists"
```

### Client Onboarding Sequence

**When to use:** Standardize every new engagement kickoff

```
Trigger: Task created
Condition: List is "Client Onboarding" AND Task type is not Subtask
Actions:
  1. Apply template "Client Onboarding Checklist"
  2. Set due date to 14 days from now
  3. Set Custom Field "Engagement Status" to "Onboarding"
  4. Add watcher: Custom Field "Account Manager"
  5. Send email to task creator: "Client onboarding initiated"
```

**Template should include subtasks:**
- [ ] Contract signed and filed
- [ ] Kickoff meeting scheduled
- [ ] Access credentials obtained
- [ ] Project folder structure created
- [ ] Team introductions complete
- [ ] First deliverable milestone set

### Engagement Kickoff Notification

**When to use:** Alert team when project officially starts

```
Trigger: Custom Field "Engagement Status" changes to "Active"
Condition: None
Actions:
  1. Post to Slack channel #project-updates
  2. Add comment "@assignees Engagement is now active"
  3. Create task "Schedule weekly status meeting" assigned to PM
```

### Client Offboarding

**When to use:** Ensure clean project closure

```
Trigger: Status changes to "Closed"
Condition: Task type is "Engagement" (or Tag contains "Engagement")
Actions:
  1. Apply template "Offboarding Checklist"
  2. Create task "Final invoice" in Billing List
  3. Create task "Collect testimonial/referral" in Growth List
  4. Add comment "Engagement closed - complete offboarding items"
```

---

## Approval Workflow Automations

### Submit for Review

**When to use:** Route deliverables through approval chain

```
Trigger: Status changes to "Pending Review"
Condition: None
Actions:
  1. Add assigned comment to Custom Field "Approver": "Please review this deliverable"
  2. Set Custom Field "Review Submitted Date" to TODAY
  3. Add watcher: Custom Field "Approver"
```

### Approval Notification

**When to use:** Notify creator when work is approved

```
Trigger: Status changes to "Approved"
Condition: None
Actions:
  1. Send email to task creator: "Your deliverable has been approved"
  2. Remove watcher: Custom Field "Approver"
  3. Change status to "Ready for Delivery"
```

### Rejection Handling

**When to use:** Route rejected work back with feedback requirement

```
Trigger: Status changes to "Needs Revision"
Condition: None
Actions:
  1. Assign to task creator
  2. Add assigned comment: "Revisions requested - see comments for feedback"
  3. Set Custom Field "Revision Count" to +1 (if formula field available)
  4. Set due date to 2 days from now
```

### Multi-Level Approval (Strategy → Partner → Client)

**When to use:** Sequential approval through hierarchy

```
Automation 1 - Strategy Lead Review:
Trigger: Status changes to "Strategy Review"
Condition: None
Actions:
  1. Add assigned comment to [Strategy Lead]: "Strategy review needed"
  2. Set Custom Field "Current Approver" to "Strategy Lead"

Automation 2 - Partner Review:
Trigger: Status changes to "Partner Review"
Condition: Custom Field "Current Approver" is "Strategy Lead"
Actions:
  1. Add assigned comment to [Partner]: "Partner review needed"
  2. Set Custom Field "Current Approver" to "Partner"

Automation 3 - Client Review:
Trigger: Status changes to "Client Review"
Condition: Custom Field "Current Approver" is "Partner"
Actions:
  1. Send email to Custom Field "Client Contact"
  2. Set Custom Field "Current Approver" to "Client"
```

---

## Time & Resource Automations

### Missing Time Entry Detection

**When to use:** Enforce time tracking discipline

```
Trigger: Status changes to "Complete"
Condition: Time tracked equals 0
Actions:
  1. Add assigned comment: "⚠️ No time logged on this task"
  2. Change status to "In Review"
  3. Set priority to High
```

### Over-Budget Alert

**When to use:** Flag tasks exceeding estimates

```
Trigger: Time tracked changes
Condition: Time tracked > Time estimate
Actions:
  1. Add comment: "⚠️ Task has exceeded time estimate"
  2. Add watcher: Custom Field "Project Manager"
  3. Set Custom Field "Budget Status" to "Over"
```

### Capacity Warning

**When to use:** Alert when workload exceeds threshold

```
Trigger: Assignee changes
Condition: Assignee workload > 40 hours (requires Workload view check)
Actions:
  1. Add comment: "⚠️ Assignee may be overallocated"
  2. Set Custom Field "Resource Flag" to "Review Needed"
```

**Note:** Native ClickUp can't directly trigger on workload. Use webhook to external system that checks capacity, or manual review process.

---

## Milestone & Delivery Automations

### Milestone Completion Alert

**When to use:** Notify stakeholders of major progress

```
Trigger: Status changes to "Complete"
Condition: Tag contains "Milestone" OR Task type is "Milestone"
Actions:
  1. Send email to Custom Field "Client Contact": "[Project] Milestone Complete"
  2. Post to Slack #client-updates
  3. Create task "Invoice for [task name]" in Billing List
```

### Deliverable Handoff

**When to use:** Transition completed work to client delivery

```
Trigger: Status changes to "Ready for Delivery"
Condition: None
Actions:
  1. Add assigned comment to Custom Field "Account Manager": "Ready to deliver to client"
  2. Set due date to 1 day from now
  3. Set priority to High
```

### Deadline Approaching Warning

**When to use:** Proactive alerts before due dates

```
Trigger: 3 days before due date
Condition: Status is not "Complete" AND Status is not "Blocked"
Actions:
  1. Add assigned comment: "Due date approaching in 3 days"
  2. Set priority to High (if Normal or Low)
```

### Overdue Escalation

**When to use:** Escalate missed deadlines

```
Trigger: Task is overdue
Condition: Priority is not Urgent
Actions:
  1. Set priority to Urgent
  2. Add watcher: Custom Field "Project Manager"
  3. Add comment: "⚠️ Task is now overdue"
```

---

## Communication & Notification Automations

### Weekly Status Report Trigger

**When to use:** Automate recurring report creation

```
Trigger: Every Friday at 9:00 AM
Condition: None
Actions:
  1. Create task "Weekly Status Report - [Week of DATE]" in Reports List
  2. Apply template "Weekly Status Template"
  3. Assign to Custom Field "Project Manager"
  4. Set due date to today at 5:00 PM
```

### Slack Channel Sync

**When to use:** Keep team informed of critical changes

```
Trigger: Status changes
Condition: Status is "Blocked" OR Status is "Complete"
Actions:
  1. Post to Slack #project-[client-name]
```

### Client Communication Log

**When to use:** Track all client touchpoints

```
Trigger: Comment posted
Condition: Comment contains "@client" OR Task has Tag "Client Communication"
Actions:
  1. Create task "[Original task name] - Client Touchpoint" in Communications Log List
  2. Copy comment to new task description
```

---

## Quality & Compliance Automations

### QA Checklist Application

**When to use:** Ensure quality review before delivery

```
Trigger: Status changes to "QA Review"
Condition: None
Actions:
  1. Apply template "QA Checklist"
  2. Add assigned comment to QA team: "Ready for quality review"
```

### Compliance Documentation

**When to use:** Ensure required documentation exists

```
Trigger: Status changes to "Complete"
Condition: Custom Field "Compliance Required" is checked
Actions:
  1. Add comment: "Compliance documentation required before close"
  2. Create subtask "Upload compliance documentation"
  3. Change status to "Documentation Pending"
```

### Risk Flag Escalation

**When to use:** Surface high-risk items to leadership

```
Trigger: Custom Field "Risk Level" changes to "High"
Condition: None
Actions:
  1. Add watcher: [Leadership Team]
  2. Set priority to Urgent
  3. Add comment: "🚨 High risk flagged - leadership notified"
  4. Post to Slack #leadership-alerts
```

---

## Integration Automations

### HubSpot Deal Won → Project Creation

**When to use:** Seamless CRM-to-PM handoff (requires Zapier/Make)

```
External Trigger (Zapier): HubSpot deal stage changes to "Closed Won"
ClickUp Actions via Zapier:
  1. Create Folder in Delivery Space named [Deal Name]
  2. Create task "Client Onboarding - [Deal Name]" in folder
  3. Set Custom Fields from HubSpot properties (Industry, Value, Contact)
  4. Assign to [Onboarding Specialist]
```

### Invoice Trigger on Milestone

**When to use:** Automate billing workflow

```
Trigger: Status changes to "Invoiceable"
Condition: Custom Field "Billable" is checked
Actions:
  1. Create task in "Invoicing" List with name "Invoice: [task name]"
  2. Set Custom Field "Invoice Amount" to [calculated value or manual]
  3. Assign to Finance team
  4. Add comment with time tracked summary
```

### Meeting Notes to Task

**When to use:** Convert Fireflies/meeting action items to tasks

```
External Trigger (Fireflies webhook): Meeting ends
Zapier/Make Actions:
  1. Parse action items from transcript
  2. For each action item: Create task in appropriate List
  3. Set assignee based on @mention detection
  4. Link to meeting recording in task description
```

---

## Usage Estimation by Recipe

| Recipe | Actions per Trigger | Estimated Monthly Volume | Monthly Actions |
|--------|---------------------|-------------------------|-----------------|
| Client Onboarding | 5 | 3-5 new clients | 15-25 |
| Missing Time Entry | 2 | 20-50 tasks | 40-100 |
| Milestone Alert | 3 | 10-20 milestones | 30-60 |
| Approval Routing | 3 | 30-50 approvals | 90-150 |
| Weekly Status | 3 | 4 weeks | 12 |
| Deadline Warning | 2 | 50-100 tasks | 100-200 |
| Overdue Escalation | 3 | 10-20 overdue | 30-60 |

**Typical consulting firm total:** 400-800 actions/month (well under 10k limit)

**Warning signs you're approaching limits:**
- High-volume Lists with multiple automations
- Status change triggers without conditions
- Automations creating tasks that trigger more automations
