# Solution Brief

Complete reference for workshopping solution briefs with users. Combines workshop protocol, question framework, and module templates.

---

## Contents

**Part 1: Workshop Protocol**
1. [Overview](#overview)
2. [Session Opening Protocol](#session-opening-protocol)
3. [Module Workshop Protocol](#module-workshop-protocol)
4. [Question Framework](#question-framework)
5. [Tool Search Protocol](#tool-search-protocol)
6. [Document Management](#document-management)
7. [Module-Specific Guidance](#module-specific-guidance)
8. [Quality Checklist](#quality-checklist)

**Part 2: Module Templates**
9. [Document Header Template](#document-header-template)
10. [Module 0-6 Templates](#module-0-discovery--validation-template)

---

## Overview

### What This System Does

The Solution Brief is a single evolving document that grows from discovery through implementation. Rather than discrete templates (Tier 1, 2, 3), users progressively build out modules as the solution matures.

**Key principles:**
- One document that evolves over time
- Claude workshops each module with the user
- Assessment-first: understand what exists before proposing next steps
- Generate draft, then discuss: easier to react than create from nothing
- Synthesize with citations: show your work, cite your sources

### Triggers

| Command | When to Use |
|---------|-------------|
| `/brief [solution name]` | Standalone brief for any solution |
| `/solutions brief [use case]` | Brief for AI solution from discovery pipeline |

### Module Structure

| Module | Name | Owner | Milestone When Complete |
|--------|------|-------|------------------------|
| **0** | Discovery & Validation | Strategist | Feasibility confirmed |
| **1** | Problem & Context | Strategist | Quick pitch ready |
| **2** | Solution Concept | Strategist | Stakeholder alignment ready |
| **3** | Constraints & Data | Strategist | Technical feasibility validated |
| **4** | Technical Approach | Engineer | Engineering handoff ready |
| **5** | Estimates & ROI | Engineer | Investment decision ready |
| **6** | Risks & Adoption | Collaborative | Implementation ready |

Users can stop at any module. Module 1 alone = quick pitch. Modules 0-3 = stakeholder alignment. All modules = implementation-ready.

---

## Session Opening Protocol

### Adaptive Opening

When `/brief` is triggered, adapt your opening based on what the user provides:

**Scenario A: Solution name only**
```
User: /brief CES Rebate Assistant
```
Response flow:
1. Acknowledge the solution
2. Ask: "Would you like me to search project knowledge and connected tools (Fireflies, Drive) for context on this solution?"
3. If yes → Search, then present assessment
4. If no → Ask what they'd like to work on

**Scenario B: Solution name + context**
```
User: /brief CES Rebate Assistant - we discussed this in last week's discovery call with Jen
```
Response flow:
1. Search for the discovery call
2. Present what you found with citations
3. Show module status assessment
4. Propose which module to work on

**Scenario C: Existing document provided**
```
User: /brief [pastes existing brief content]
```
Response flow:
1. Analyze the provided content
2. Map content to modules
3. Show status: which modules are complete, in-progress, or missing
4. Propose which module to work on next

**Scenario D: Just the command**
```
User: /brief
```
Response flow:
1. Ask: "What solution are you working on?"
2. Then proceed with Scenario A or B based on response

### Status Display

After assessment, always show module status:

```
## Brief Status: [Solution Name]

| Module | Status | Notes |
|--------|--------|-------|
| 0. Discovery | ✅ Complete | Validated in Oct 15 call |
| 1. Problem | ✅ Complete | — |
| 2. Solution | 🔄 In Progress | Scope needs refinement |
| 3. Constraints | ⬜ Not Started | — |
| 4. Technical | ⬜ Not Started | — |
| 5. Estimates | ⬜ Not Started | — |
| 6. Risks | ⬜ Not Started | — |

**Recommendation:** Let's finish Module 2 (Solution Concept) — specifically the scope boundaries. Then we can move to Module 3.
```

---

## Module Workshop Protocol

### The Core Loop

For each module, follow this pattern:

1. **Search** (if user opted in) — Find relevant context from tools
2. **Synthesize** — Draft content based on what you found + conversation
3. **Present** — Show draft with citations
4. **Discuss** — Get feedback, answer questions
5. **Refine** — Update based on feedback
6. **Confirm** — Get approval to mark complete

### Generate Draft, Then Discuss

Default to drafting content rather than asking endless questions.

**Do this:**
```
Based on the Oct 15 discovery call, here's my draft for the Problem section:

**Problem Statement**
The rebate team spends 4-6 hours researching utility programs for each project. Information is scattered across utility websites, changes frequently, and mistakes cost $10-50K in missed rebates.
(Source: Fireflies - Oct 15 Discovery, 23:45)

**Who Experiences This**
- Jen (Rebate Coordinator) — primary researcher, loses half her week to this
- Sales reps — can't include accurate rebate estimates in proposals
(Source: Fireflies - Oct 15 Discovery, 31:20)

Does this capture the problem accurately? Anything to add or adjust?
```

**Not this:**
```
What's the problem you're trying to solve?
Who experiences this problem?
How much time do they spend on it?
What's the cost?
...
```

### When to Surface Options Before Drafting

For complex decisions, present options before drafting:

**Architecture choices (Module 4):**
```
For the technical approach, I see three viable options:

**Option A: CustomGPT with Knowledge Base**
- Simplest to build (20-30 hours)
- Limited to conversational interface
- Best when: Users comfortable with chat, data is mostly static

**Option B: N8N Workflow + Database**
- More complex (60-80 hours)
- Can integrate with existing systems
- Best when: Need automation, data updates frequently

**Option C: Hybrid (CustomGPT + N8N backend)**
- Most flexible (80-100 hours)
- Combines conversational UI with automation
- Best when: Want both ease of use and system integration

Based on CES's context (small team, wants quick wins), I'd recommend Option A to start, with a path to Option C later.

Which direction feels right?
```

**Risk prioritization (Module 6):**
```
I've identified 6 potential risks. Before I draft the risk register, let's align on which matter most:

1. Data quality in utility databases — could delay launch
2. User adoption — Jen might resist change
3. API rate limits — could slow down bulk lookups
4. Rebate program changes — data goes stale
5. Integration with SnapCount — unknown complexity
6. Budget approval — Tony hasn't signed off

Which 3-4 should we prioritize in the brief?
```

---

## Question Framework

When you need to ask clarifying questions (not drafting), use this pattern:

### The Pattern

For each question:
1. **Explain** — Why this question matters
2. **Options** — 2-4 viable answers with rationale
3. **Recommendation** — Your suggested answer and why

### Example Questions by Module

**Module 1: Problem & Context**

```
**Question: How should we quantify the impact?**

Why this matters: Quantified impact drives prioritization and ROI calculations. Vague problems get deprioritized.

Options:
A. **Time-based** — "X hours per week spent on Y"
   Best when: Problem is labor-intensive; easy to measure
   
B. **Cost-based** — "$X per year in errors/waste/fees"
   Best when: Direct financial impact; gets executive attention
   
C. **Risk-based** — "X% chance of Y compliance violation"
   Best when: Problem is about avoiding downside; hard to quantify time/cost
   
D. **Opportunity-based** — "Missing $X in potential revenue/savings"
   Best when: Problem is about unrealized upside

My recommendation: Option A (time-based) for this problem — Jen's 4-6 hours per project is concrete and relatable. We can calculate cost from there ($60/hr × 4.5 hrs × 50 projects = $13,500/year).
```

**Module 2: Solution Concept**

```
**Question: How specific should the solution concept be?**

Why this matters: Too vague = misaligned expectations. Too specific = constrains engineering unnecessarily.

Options:
A. **Wide open** — Describe the problem, let engineering propose solutions
   Best when: Multiple viable approaches; want engineer creativity
   
B. **Direction set** — General approach defined (e.g., "CustomGPT"), details TBD
   Best when: Clear category of solution; flexibility on implementation
   
C. **Fully specified** — Detailed requirements, UX, integrations defined
   Best when: Requirements are well-understood; less engineering judgment needed

My recommendation: Option B (direction set) — We know this should be a CustomGPT with a rebate database. Leave room for Kate to determine the best data structure and update mechanism.
```

**Module 3: Constraints & Data**

```
**Question: What's the data quality for utility rebate information?**

Why this matters: If data quality is low (1-3), we need to budget cleanup time. This directly impacts timeline and cost.

Options:
A. **Quality 5 (Excellent)** — Structured, complete, accessible, accurate
B. **Quality 4 (Good)** — Minor gaps or formatting issues
C. **Quality 3 (Moderate)** — Significant cleanup needed but usable
D. **Quality 2 (Poor)** — Major gaps, inconsistencies, access issues
E. **Quality 1 (Unusable)** — Would need to rebuild from scratch

My recommendation: Based on what Jen described (scattered across utility websites, no central database), this sounds like Quality 2. We should budget 20-30 hours for initial data collection and structuring.
```

---

## Tool Search Protocol

### User Opt-In

At session start, ask:
```
Would you like me to search project knowledge and connected tools (Fireflies, Drive, Gmail) for context on [solution name]?
```

If user says yes, proceed with searches. If no, rely on conversation.

### Search Per-Module

Don't search everything upfront. Search when working on each module:

| Module | Primary Sources | Search For |
|--------|----------------|------------|
| 0. Discovery | Fireflies, Project Knowledge | Discovery calls, initial assessments, opportunity notes |
| 1. Problem | Fireflies, Project Knowledge | Problem statements, stakeholder quotes, pain points, "hours spent," "frustrating" |
| 2. Solution | Project Knowledge, Drive | Prior briefs, solution discussions, similar solutions, "proposed," "recommendation" |
| 3. Constraints | Drive, Project Knowledge | Technical docs, system info, "API," "integration," "budget," "timeline" |
| 4. Technical | Drive, Project Knowledge | Architecture docs, prior specs, similar builds |
| 5. Estimates | Project Knowledge, Past Conversations | Prior estimates, similar project costs, "hours," "estimate" |
| 6. Risks | Fireflies, Project Knowledge | Risk discussions, concerns, "worried about," "blocker," "risk" |

### Search Principles

**Do:**
- Search for client name + relevant keywords
- Look for recent content first (last 30-60 days)
- Search multiple sources if first doesn't yield results
- Include stakeholder names when searching for their input

**Don't:**
- Search everything upfront (overwhelming)
- Give up after one failed search (try different keywords)
- Assume absence of results means no information exists

### Presenting Found Context

Always synthesize and cite:

```
**From the Oct 15 discovery call with Jen:**

The rebate research process takes 4-6 hours per project. Jen described checking "at least 15 different utility websites" and mentioned that program details "change every quarter without notice."
(Source: Fireflies - CES Discovery Oct 15, timestamps 23:45-25:30)

**From the CES project knowledge:**

This opportunity was identified as "P1 - High Impact" in the initial assessment, with estimated value of $15-20K annually.
(Source: CES-Opportunities-Assessment.md)
```

### Handling Gaps and Conflicts

**Small gaps:** Proceed with TBD, note what's missing
```
I couldn't find specific budget constraints in the available sources. I've marked this as TBD — can you confirm the budget range?
```

**Critical gaps:** Ask before proceeding
```
I searched Fireflies and Drive but couldn't find any technical documentation about SnapCount integration. This is critical for Module 3. Can you provide details or point me to where this might be documented?
```

**Conflicts:** Surface and ask user to resolve
```
I found conflicting information:
- Oct 15 call: Jen said "4-6 hours per project"
- Nov 3 email: Referenced "about 2 hours of research"

Which is more accurate? (The difference matters for ROI calculation)
```

---

## Document Management

### File Creation

**When to create:** After Module 1 (Problem & Context) is complete

**Naming:** `[solution-name]-brief.md`
- Example: `ces-rebate-assistant-brief.md`

**Location:** `/mnt/user-data/outputs/`

### File Updates

Update the file each time a module is completed or significantly revised. Always:
1. Update the status table in the document header
2. Add/revise the module content
3. Note the last updated date

### Presenting the File

After creating or updating:
```
I've [created/updated] the brief document. Here's the current status:

[Show status table]

Would you like to continue with Module X, or is there anything in the completed modules you'd like to revisit?
```

---

## Module-Specific Guidance

### Module 0: Discovery & Validation

**Purpose:** Confirm this solution is worth building before investing in detailed specs.

**Key questions to resolve:**
- Is this problem real and significant?
- Is a solution technically feasible?
- Are there blockers that would kill this?
- Should we proceed to full brief?

**Output:** Proceed/No-Go decision with rationale

**Sections:**
- Problem Hypothesis
- Validation Questions (what we need to answer)
- Feasibility Blockers (technical, data, organizational)
- Architecture Options (if multiple approaches)
- Recommendation (proceed / pivot / kill)

### Module 1: Problem & Context

**Purpose:** Establish what we're solving and why it matters.

**Problem Statement Template (example, not required):**
> [Role/Team] spends [X hours] per [timeframe] doing [activity] because [root cause]. This causes [impact] and costs approximately [$X per year].

**Key sections:**
- Problem Statement
- Who Experiences This (names, roles, how affected)
- Quantified Impact (show your math)
- Current Workaround (what they do today)
- Why Now (urgency drivers)
- Success Criteria (measurable outcomes)

### Module 2: Solution Concept

**Purpose:** Define what we're building from user/business perspective.

**Key sections:**
- Solution Direction (Wide Open / Direction Set / Fully Specified)
- Solution Overview (plain language description)
- Capability Requirements (what it must DO)
- User Experience Vision (how users interact)
- Scope Definition (In Scope / Out of Scope)
- What We're NOT Building (explicit exclusions)

### Module 3: Constraints & Data

**Purpose:** Establish boundaries and validate data availability.

**Key sections:**
- Budget & Timeline
- Technology Constraints (must integrate with, off-limits)
- Organizational Constraints (approvals, politics, compliance)
- Data Reality Check (required data, source, quality 1-5, cleanup needed)
- Data Access Issues

**Critical:** If Data Quality < 3 on any required data, budget cleanup into scope and timeline.

### Module 4: Technical Approach

**Purpose:** Define how we'll build this (engineer-owned).

**Key sections:**
- Architecture Overview (with diagram if helpful)
- Technology Stack (existing systems, new systems, integration method)
- Component Breakdown (major pieces to build)
- Human-in-the-Loop Evolution:
  - Phase 1: Assisted (AI does work, human reviews all)
  - Phase 2: [Define threshold for reduced review]
  - Phase 3: [Define threshold for full automation]
- Technical Assumptions

### Module 5: Estimates & ROI

**Purpose:** Define effort, timeline, and investment case (engineer-owned).

**Key sections:**
- Complexity Assessment (1-5 score with rationale)
- Effort Estimate (by phase: Discovery, Design, Build, Test, Train, Deploy)
- Estimate Range:
  | Optimistic | Expected | Pessimistic |
  |------------|----------|-------------|
  | X hours | Y hours | Z hours |
- What Would Change the Estimate
- Investment & ROI:
  - Implementation Cost
  - Annual Operating Cost
  - Annual Benefit (from Module 1)
  - Payback Period
- Dependencies & Prerequisites

### Module 6: Risks & Adoption

**Purpose:** Identify what could go wrong and plan for successful adoption.

**Key sections:**
- Risk Register:
  | Risk | Likelihood | Impact | Mitigation | Owner |
  |------|------------|--------|------------|-------|
- Key Assumptions (if false, scope/estimate may change)
- Open Questions (with owner and status)
- Change Management:
  - Training Required (hours, format, audience)
  - Feedback Mechanism
  - Review Cadence
  - Success Owner
- Go/No-Go Criteria (what must be true to ship)

---

## Quality Checklist

Before marking the brief complete, verify:

**Module 0-1 (Quick Pitch Ready):**
- [ ] Problem is specific and quantified
- [ ] Impact shows real numbers with math
- [ ] Urgency is clear
- [ ] Success criteria are measurable

**Module 0-3 (Stakeholder Alignment Ready):**
- [ ] Solution concept is clear in plain language
- [ ] Scope boundaries are explicit (in/out)
- [ ] Data reality is assessed (quality scores)
- [ ] Constraints are documented
- [ ] Key assumptions are listed

**Module 0-6 (Implementation Ready):**
- [ ] Technical approach has clear architecture
- [ ] Human-in-the-loop evolution is defined
- [ ] Estimates have ranges with uncertainty factors
- [ ] Risks have owners and mitigations
- [ ] Change management is planned
- [ ] Go/No-Go criteria are defined
- [ ] All sources are cited

---

# Part 2: Module Templates

Copy-paste ready templates for building solution brief documents.

---

## Document Header Template

```markdown
# [Solution Name] — Solution Brief

| Field | Value |
|-------|-------|
| **Client** | [Client Name] |
| **Created** | [Date] |
| **Last Updated** | [Date] |
| **Strategist** | [Name] |
| **Engineer** | [Name] |
| **Gap IDs** | [G001, G002] (if from Discovery Catalog) |

## Module Status

| Module | Status | Owner | Notes |
|--------|--------|-------|-------|
| 0. Discovery & Validation | ⬜ Not Started | Strategist | |
| 1. Problem & Context | ⬜ Not Started | Strategist | |
| 2. Solution Concept | ⬜ Not Started | Strategist | |
| 3. Constraints & Data | ⬜ Not Started | Strategist | |
| 4. Technical Approach | ⬜ Not Started | Engineer | |
| 5. Estimates & ROI | ⬜ Not Started | Engineer | |
| 6. Risks & Adoption | ⬜ Not Started | Collaborative | |

**Status Key:** ⬜ Not Started | 🔄 In Progress | ✅ Complete

---
```

---

## Module 0: Discovery & Validation Template

**Milestone:** Feasibility confirmed, proceed/no-go decision made.

```markdown
## Module 0: Discovery & Validation

### Problem Hypothesis

[1-2 sentences describing the suspected problem and who experiences it]

### Validation Questions

Questions that must be answered to validate this opportunity:

- [ ] [Question 1] — [Who can answer]
- [ ] [Question 2] — [Who can answer]
- [ ] [Question 3] — [Who can answer]

### Feasibility Assessment

| Factor | Assessment | Notes |
|--------|------------|-------|
| Technical feasibility | 🟢 / 🟡 / 🔴 | [Details] |
| Data availability | 🟢 / 🟡 / 🔴 | [Details] |
| Organizational readiness | 🟢 / 🟡 / 🔴 | [Details] |
| Budget/timeline fit | 🟢 / 🟡 / 🔴 | [Details] |

### Architecture Options (if applicable)

**Option A: [Name]**
- Approach: [Description]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Estimated effort: [Range]

**Option B: [Name]**
- Approach: [Description]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Estimated effort: [Range]

### Red Flags

[Any fundamental blockers identified]

### Recommendation

☐ **Proceed** — Move to full brief development
☐ **Pivot** — Adjust approach: [describe pivot]
☐ **Kill** — Do not pursue: [rationale]

**Rationale:** [Why this recommendation]

---
```

---

## Module 1: Problem & Context Template

**Milestone:** Quick pitch ready.

```markdown
## Module 1: Problem & Context

### Problem Statement

> [Role/Team] spends [X hours] per [timeframe] doing [activity] because [root cause]. This causes [impact] and costs approximately [$X per year].

### Who Experiences This Problem

| Person/Role | Department | How They're Affected |
|-------------|------------|---------------------|
| [Name, Role] | [Department] | [Impact on their work] |

### Quantified Impact

| Cost Category | Calculation | Annual Cost |
|---------------|-------------|-------------|
| Labor cost | [X] hours × $[Y]/hr × [Z] frequency | $[amount] |
| **Total Annual Impact** | | **$[total]** |

### Current Workaround

[Describe current state — steps, tools, pain points]

### Why Now?

[Explain urgency drivers]

### Success Criteria

| Metric | Current State | Target State |
|--------|---------------|--------------|
| [e.g., Processing time] | [e.g., 15 hours/month] | [e.g., <2 hours/month] |

---
```

---

## Module 2: Solution Concept Template

**Milestone:** Stakeholder alignment ready.

```markdown
## Module 2: Solution Concept

### Solution Direction

☐ **Wide Open** — Seeking engineer input on how to solve this
☐ **Direction Set** — General approach defined, details TBD
☐ **Fully Specified** — Detailed solution concept below

### Solution Overview

[Write solution overview in plain language]

### Capability Requirements

- [Capability 1]
- [Capability 2]
- [Capability 3]

### User Experience Vision

| Before | After |
|--------|-------|
| [Current experience] | [Future experience] |

### Scope Definition

**In Scope:**
- [What's included]

**Out of Scope:**
- [What's NOT included]

### What We're NOT Building

❌ [Explicit exclusion 1]
❌ [Explicit exclusion 2]

---
```

---

## Module 3: Constraints & Data Template

**Milestone:** Technical feasibility validated.

```markdown
## Module 3: Constraints & Data

### Budget & Timeline

| Constraint | Value | Notes |
|------------|-------|-------|
| **Budget Range** | $[X] - $[Y] | |
| **Timeline** | [Hard deadline or preferred timing] | |

### Technology Constraints

**Must Integrate With:**
- [System 1]
- [System 2]

**Off-Limits:**
- [Any prohibited tools]

### Organizational Constraints

| Constraint | Details |
|------------|---------|
| **Approval Required** | [Who must sign off] |
| **Compliance/Security** | [SOC2, HIPAA, etc.] |

### Data Reality Check

| Data Needed | Source | Quality (1-5) | Cleanup Needed? |
|-------------|--------|---------------|-----------------|
| [Data type 1] | [System] | [1-5] | [Yes/No] |

**Quality Scale:** 5=Excellent, 4=Good, 3=Moderate, 2=Poor, 1=Unusable

**⚠️ If any Data Quality < 3:** Budget data cleanup into scope.

---
```

---

## Module 4: Technical Approach Template

**Owner:** Engineer
**Milestone:** Engineering handoff ready.

```markdown
## Module 4: Technical Approach

### Architecture Overview

[Describe architecture or include diagram]

### Technology Stack

| Category | Choice | Notes |
|----------|--------|-------|
| **Existing Systems** | [Systems client has] | |
| **New Systems** | [New tools to add] | |
| **Integration Method** | [APIs, webhooks, etc.] | |

### Component Breakdown

**Component 1: [Name]**
[What it does, key technical considerations]

### Human-in-the-Loop Evolution

| Phase | Autonomy Level | Criteria to Advance |
|-------|----------------|---------------------|
| **Phase 1** | Assisted — human reviews everything | [Default] |
| **Phase 2** | [e.g., Spot-check 20%] | [e.g., 95% accuracy] |
| **Phase 3** | [e.g., Auto-approve if >90% confidence] | [e.g., 99% accuracy] |

### Technical Assumptions

- [Technical assumption]
- [Data assumption]

---
```

---

## Module 5: Estimates & ROI Template

**Owner:** Engineer
**Milestone:** Investment decision ready.

```markdown
## Module 5: Estimates & ROI

### Complexity Assessment

| Factor | Score (1-5) | Rationale |
|--------|-------------|-----------|
| **Overall Complexity** | [1-5] | [Why] |

### Effort Estimate

| Phase | Hours | Duration |
|-------|-------|----------|
| Discovery & Requirements | [X] | [X weeks] |
| Build & Configure | [X] | [X weeks] |
| Testing & QA | [X] | [X weeks] |
| **TOTAL** | **[X] hours** | **[X] weeks** |

### Estimate Range

| Optimistic | Expected | Pessimistic |
|------------|----------|-------------|
| [X] hours | [Y] hours | [Z] hours |

### Investment & ROI

| Metric | Value |
|--------|-------|
| **Implementation Cost** | $[X] |
| **Annual Benefit** | $[X] |
| **Payback Period** | [X] months |

### Dependencies

- [ ] [Dependency 1]
- [ ] [Dependency 2]

---
```

---

## Module 6: Risks & Adoption Template

**Owner:** Collaborative
**Milestone:** Implementation ready.

```markdown
## Module 6: Risks & Adoption

### Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [Risk] | H/M/L | H/M/L | [How to handle] | [Name] |

### Key Assumptions

- [Assumption 1]
- [Assumption 2]

### Open Questions

| Question | Owner | Due | Status |
|----------|-------|-----|--------|
| [Question] | [Name] | [Date] | ⬜ Open |

### Change Management Plan

| Element | Plan |
|---------|------|
| **Training Required** | [Hours, format, audience] |
| **Success Owner** | [Name and role] |

### Go/No-Go Criteria

**Ship if:**
- ✅ [Criterion 1]
- ✅ [Criterion 2]

**Don't ship if:**
- 🚫 [Blocker 1]

---
```

---

## Format Upgrades

**Primary format:** Markdown (.md)

**When to upgrade:**

| Format | Use When |
|--------|----------|
| **DOCX** | Formal client deliverable, email attachment |
| **HTML** | Presenting in meeting, embedding in portal |
| **PDF** | Final locked version, exec distribution |

**Brand application:** When creating DOCX/HTML/PDF, load `brand/brand.md` and `brand/brand-ui.md` for styling.
