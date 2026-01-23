---
name: project-resource-planner
description: Transform semi-structured scopes of work (SOWs) and engagement schedules into detailed week-by-week resource allocation plans for ClickUp project management. Use when users need to convert client engagement documents into structured project plans with hour estimates for AI Managers, AI Strategists, and AI Engineers. Ideal for planning 2-12 month consulting engagements with discovery, strategy, and implementation phases.
---

# Project Resource Planner

Convert semi-structured SOWs into hierarchical, ClickUp-ready resource allocation plans with SMART goals and actionable sub-tasks.

## Role Definitions

**AI Manager**: Lead client meetings, create decks, coordinate timelines, facilitate workshops. Baseline 4-8 hrs/week, spikes to 12+ for kickoffs/presentations.

**AI Strategist**: Run discovery sessions, map processes, design solutions, create documentation, facilitate stakeholder interviews. Heavy during discovery (16-24 hrs/week), lighter during pure implementation (4-8 hrs/week).

**AI Engineer**: Build/configure AI systems, develop automations, handle technical setup, test/optimize, deploy solutions. Heavy during implementation (16-24+ hrs/week), lighter during strategy (4-8 hrs/week).

## SMART Goals Framework

All goals (monthly and weekly) must follow SMART criteria:
- **Specific**: Clear, unambiguous outcome
- **Measurable**: Quantifiable or verifiable completion
- **Achievable**: Realistic given resources and time
- **Relevant**: Ladders up to engagement objectives
- **Time-bound**: Has clear deadline (end of month/week)

**Monthly Goals**: Extract from SOW's month-by-month breakdown. Look for deliverables, milestones, outcomes. Transform into SMART format. Maximum 1-3 goals per month (less is more).

**Weekly Goals**: Create exactly 4 per month (one per week). Must ladder up to monthly goal and be SMART.

## Interactive Workflow

### Phase 1: Setup Questions
Ask these first:
1. Client name?
2. Engagement start date? (YYYY-MM-DD format)
3. Engagement duration? (2-3 months, 6 months, 12 months, or custom)
4. Paste the SOW/schedule/project description

### Phase 2: Initiative Extraction
After reading the SOW:
- Identify all major initiatives/workstreams
- Present as numbered list noting: months spanned, type (strategy/implementation/hybrid), dependencies
- Ask: "Process one at a time (interactive) or all at once (faster)?"

### Phase 3: Monthly Goal Extraction
For each initiative, extract monthly goals from the SOW's month-by-month breakdown:
- Look for deliverables, milestones, or outcomes specified for each month
- Transform into SMART goals (1-3 per month maximum, less is more)
- Validate: "I extracted these monthly goals for [Initiative]. Do they look right?"

### Phase 4: Weekly Goal & Sub-task Generation
For each monthly goal:
- Create exactly 4 weekly goals (one per week) that ladder up to monthly goal
- Each weekly goal must be SMART
- Generate 2-5 actionable sub-tasks per weekly goal
- Allocate hours at weekly goal level (not per sub-task)
- Tag each sub-task with responsible role in parentheses
- Show reasoning for hour allocation
- Validate: "Does this breakdown look right? [Approve / Adjust / Regenerate]"

### Phase 5: Primary Output Generation
Generate comprehensive markdown document with:
1. **Executive Summary**: Client, duration, initiatives, total hours per role, peak week
2. **Initiative Breakdowns**: Hierarchical structure (Initiative → Monthly Goals → Weekly Goals → Sub-tasks)
3. **Role Hour Summaries**: Totals, averages, peak weeks, load patterns per role
4. **Notes & Recommendations**: Concerns, dependencies, success factors, feedback loops

### Phase 6: Optional Outputs (Ask User)
After generating primary output:

1. **Ask**: "Would you like a Weekly Calendar View table showing all initiatives combined?" 
   - If yes: Generate comprehensive table with all work across all initiatives
   - If no: Skip to next question

2. **Ask**: "Would you like a CSV export for ClickUp import?"
   - If yes: Generate CSV with format specified below
   - If no: Done

## Hierarchical Output Structure

```markdown
# [Client] - Resource Allocation Plan
**Duration:** [Start Date] to [End Date] ([X] months)
**Generated:** [Date]

## Executive Summary
- **Total Initiatives:** X
- **AI Manager Total Hours:** X hours (avg X hrs/week)
- **AI Strategist Total Hours:** X hours (avg X hrs/week)
- **AI Engineer Total Hours:** X hours (avg X hrs/week)
- **Peak Week:** Week X ([Date]) with X total hours

## Initiative 1: [Initiative Name]
**Duration:** Month X - Month Y | **Type:** [Strategy/Implementation/Hybrid]

### Month 1: [Monthly SMART Goal - Deliverable/Milestone]
**Goal:** [Specific, measurable outcome to be achieved by end of month]

#### Week 1 ([Start Date - End Date]): [Weekly SMART Goal]
**Hours:** Manager: X | Strategist: X | Engineer: X
- [Actionable sub-task with clear deliverable] (Manager)
- [Actionable sub-task with clear deliverable] (Strategist)
- [Actionable sub-task with clear deliverable] (Engineer)
- [Actionable sub-task with clear deliverable] (Role)
- [Actionable sub-task with clear deliverable] (Role)

#### Week 2 ([Start Date - End Date]): [Weekly SMART Goal]
**Hours:** Manager: X | Strategist: X | Engineer: X
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)

#### Week 3 ([Start Date - End Date]): [Weekly SMART Goal]
**Hours:** Manager: X | Strategist: X | Engineer: X
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)

#### Week 4 ([Start Date - End Date]): [Weekly SMART Goal]
**Hours:** Manager: X | Strategist: X | Engineer: X
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)
- [Actionable sub-task] (Role)

### Month 2: [Monthly SMART Goal - Deliverable/Milestone]
[Continue pattern...]

## Initiative 2: [Initiative Name]
[Continue pattern...]

## Role Hour Summaries

### AI Manager
- **Total Hours:** X
- **Average per Week:** X
- **Peak Week:** Week X ([Date]) - X hours
- **Load Pattern:** [Description of how hours vary: e.g., "Elevated during kickoff and training weeks, baseline during implementation phases"]

### AI Strategist
- **Total Hours:** X
- **Average per Week:** X
- **Peak Week:** Week X ([Date]) - X hours
- **Load Pattern:** [Description]

### AI Engineer
- **Total Hours:** X
- **Average per Week:** X
- **Peak Week:** Week X ([Date]) - X hours
- **Load Pattern:** [Description]

## Notes & Recommendations

### Resource Allocation Concerns
[Flag any weeks where single role >24 hours, unrealistic expectations, or overallocation]

### Critical Dependencies
[Identify what must happen before what, cross-initiative dependencies, external dependencies]

### Success Factors
[Recommendations for smooth execution based on engagement type and complexity]

### Client Feedback Loops
[Weeks where client approval/feedback will impact timeline - add 3-5 day buffers]
```

## Optional: Weekly Calendar View Table

If user requests, generate this table showing ALL work across ALL initiatives:

```markdown
## Weekly Calendar View

| Week | Dates | Key Activities | Manager | Strategist | Engineer | Total |
|------|-------|----------------|---------|------------|----------|-------|
| 1 | [Range] | [Activities from all initiatives] | X | X | X | X |
| 2 | [Range] | [Activities from all initiatives] | X | X | X | X |
...
```

## Optional: CSV Export Format

If user requests CSV, generate with these exact columns:

**Column Headers:**
- Monthly Goal
- Weekly Goal
- SubTasks (comma-separated, role in parentheses)
- Start Date (YYYY-MM-DD)
- End Date (YYYY-MM-DD)
- AI Manager Hours (number)
- AI Strategist Hours (number)
- AI Engineer Hours (number)

**Example Row:**
```csv
"Platform Foundation & Secure Configuration","Validate Integration Architecture & Security Compliance","Conduct stakeholder alignment and kickoff meeting (Manager),Audit technology stack for integration compatibility (Strategist),Test Outlook and Dropbox integrations (Engineer),Document security and compliance requirements (Strategist),Create platform recommendation report (Strategist)",2025-11-01,2025-11-07,6,8,10
```

## Hour Allocation Patterns

**Recurring Weekly:**
- Client email update: Manager 2, Strategist 1
- Status check-in: Manager 2-3
- Internal sync: Manager 1, Strategist 1, Engineer 1

**Activity Types:**
- Executive kickoff: Manager 6-8, Strategist 4-6, Engineer 2
- Discovery workshop: Manager 4, Strategist 10-12, Engineer 2-4
- Technical audit: Manager 2, Strategist 6-8, Engineer 8-10
- System configuration: Manager 2, Strategist 4, Engineer 12-16
- Training delivery: Manager 6-8, Strategist 8-10, Engineer 4
- Testing/optimization: Manager 2-4, Strategist 4-6, Engineer 10-14
- Documentation: Manager 2, Strategist 8-10, Engineer 2
- Monthly review: Manager 6, Strategist 4, Engineer 2

**Phase Patterns:**
- **Strategy engagements (2-3 months)**: Heavy Strategist, moderate Manager, light Engineer
- **Implementation (6-12 months)**: Heavy Engineer, moderate Manager, light-moderate Strategist
- **Hybrid**: Early = Strategist-heavy, middle = Engineer-heavy, final = balanced
- **Month 1**: Always setup-heavy (all roles elevated)
- **Final month**: Handoff-focused (balanced, documentation heavy)

## Critical Guidelines

1. **SMART goals mandatory**: Every monthly and weekly goal must be Specific, Measurable, Achievable, Relevant, Time-bound
2. **Extract from SOW**: Monthly goals come from SOW's month-by-month breakdown, not invented
3. **Hierarchical structure**: Initiative → Monthly Goal → Weekly Goal → Sub-tasks
4. **Fixed hours at weekly level**: Use specific numbers (8, 12, 15), half-increments okay (1.5, 2.5)
5. **Role tags required**: Every sub-task ends with role in parentheses
6. **Exactly 4 weekly goals per month**: One per week, no more, no less
7. **2-5 sub-tasks per weekly goal**: Actionable, clear deliverables
8. **Sequential output**: Primary structure first, then ASK about optional outputs
9. **Show reasoning**: Explain hour allocations based on activity type and role patterns
10. **Validate incrementally**: Go initiative by initiative, get approval before continuing
11. **Watch for feedback loops**: Flag weeks requiring client approval, add buffers
12. **Flag overallocation**: Any role >24 hrs/week needs to be noted

## Client Feedback Loop Handling

Watch SOW for: "client review," "approval needed," "feedback loop," "stakeholder sign-off"

When found:
- Note in weekly goal if that week includes review/approval
- Add to Notes & Recommendations section
- Consider adding light coordination hours if needed: Manager 2, others 0

## Example Interaction Flow

User: "I need a resource plan for Hyperion engagement"

You: "I'll create a detailed resource plan with SMART goals and hierarchical structure. Questions:
1. Client name?
2. Engagement start date? (YYYY-MM-DD)
3. Duration?
4. Paste SOW when ready"

[User provides info and pastes SOW]

You: "Analyzed the SOW. Found 8 initiatives:
1. **LLM Application** (Months 1-6) - Implementation
2. **AI Email Assistant** (Months 1-2) - Implementation
...

Process one at a time (interactive) or all at once (faster)?"

[User chooses]

You: "For Initiative 1 - LLM Application, I extracted these monthly goals from the SOW:

Month 1: Deploy enterprise-ready LLM platform with validated integrations, secure workspaces, and foundational training for all employees by November 30.
Month 2: Launch 2 production-ready custom GPTs for Investment team with training and adoption plan by December 31.

Do these look right?"

[User approves]

You: [Generates complete hierarchical breakdown with weekly goals and sub-tasks]

[After generating primary output]

You: "Would you like a Weekly Calendar View table showing all initiatives combined?"

[User responds]

You: "Would you like a CSV export for ClickUp import?"

[User responds, generates if requested]

You: "Done! Your resource allocation plan is ready."
