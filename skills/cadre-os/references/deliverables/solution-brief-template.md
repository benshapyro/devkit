# Solution Brief Template

A single evolving document that grows from discovery through implementation.

---

## Document Header

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

## Module 0: Discovery & Validation

**Purpose:** Confirm this solution is worth building before investing in detailed specs.

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

[Any fundamental blockers identified — data doesn't exist, impossible integration, unrealistic timeline, etc.]

### Recommendation

☐ **Proceed** — Move to full brief development
☐ **Pivot** — Adjust approach: [describe pivot]
☐ **Kill** — Do not pursue: [rationale]

**Rationale:** [Why this recommendation]

---
```

---

## Module 1: Problem & Context

**Purpose:** Establish what we're solving and why it matters.

**Milestone:** Quick pitch ready.

```markdown
## Module 1: Problem & Context

### Problem Statement

[Clear problem statement. Use template below as starting point for operational efficiency problems:]

> [Role/Team] spends [X hours] per [timeframe] doing [activity] because [root cause]. This causes [impact] and costs approximately [$X per year].

### Who Experiences This Problem

| Person/Role | Department | How They're Affected |
|-------------|------------|---------------------|
| [Name, Role] | [Department] | [Impact on their work] |
| [Name, Role] | [Department] | [Impact on their work] |

### Quantified Impact

Show your math. Include labor costs, error costs, opportunity costs, etc.

| Cost Category | Calculation | Annual Cost |
|---------------|-------------|-------------|
| Labor cost | [X] hours × $[Y]/hr × [Z] frequency | $[amount] |
| [Other category] | [Calculation] | $[amount] |
| **Total Annual Impact** | | **$[total]** |

### Current Workaround

What do people do today to work around this problem?

[Describe current state — steps, tools, pain points]

Why is it inadequate?

[Explain why current approach doesn't scale or causes issues]

### Why Now?

What makes this urgent? Is it getting worse? Is there a deadline?

[Explain urgency drivers]

### Success Criteria

What does "solved" look like? Use measurable outcomes, not features.

| Metric | Current State | Target State |
|--------|---------------|--------------|
| [e.g., Processing time] | [e.g., 15 hours/month] | [e.g., <2 hours/month] |
| [e.g., Error rate] | [e.g., 8%] | [e.g., <2%] |
| [e.g., User satisfaction] | [e.g., 3/10] | [e.g., 8/10] |

---
```

---

## Module 2: Solution Concept

**Purpose:** Define what we're building from user/business perspective.

**Milestone:** Stakeholder alignment ready.

```markdown
## Module 2: Solution Concept

### Solution Direction

How specified is the solution direction?

☐ **Wide Open** — Seeking engineer input on how to solve this
☐ **Direction Set** — General approach defined, details TBD
☐ **Fully Specified** — Detailed solution concept below

### Solution Overview

What is this solution in plain language? How does it solve the problem?

[Write solution overview — or note "Seeking engineer input" if Wide Open]

### Capability Requirements

What must the solution be able to DO? (Not how — that's Module 4)

- [Capability 1 — e.g., Extract data from PDF invoices]
- [Capability 2 — e.g., Validate extracted data against rules]
- [Capability 3 — e.g., Create records in accounting system]
- [Capability 4]

### User Experience Vision

How will users interact with this? What's the workflow?

[Describe the user experience — can include mockups if helpful]

**Before/After Scenario:**

| Before | After |
|--------|-------|
| [Step-by-step current experience with times] | [Step-by-step future experience with times] |

### Scope Definition

**In Scope:**
- [What's included]
- [What's included]
- [What's included]

**Out of Scope:**
- [What's NOT included — be explicit]
- [What's NOT included — future phase?]

### What We're NOT Building

Explicit exclusions to prevent scope creep:

❌ [Thing we're not building — e.g., "Not a replacement for Salesforce"]
❌ [Thing we're not building — e.g., "Not a customer-facing portal"]
❌ [Thing we're not building — e.g., "Not handling edge case X"]

---
```

---

## Module 3: Constraints & Data

**Purpose:** Establish boundaries and validate data availability.

**Milestone:** Technical feasibility validated.

```markdown
## Module 3: Constraints & Data

### Budget & Timeline

| Constraint | Value | Notes |
|------------|-------|-------|
| **Budget Range** | $[X] - $[Y] | [Or "Not yet defined"] |
| **Timeline** | [Hard deadline or preferred timing] | |
| **Why this timeline** | [Business driver] | |

### Technology Constraints

**Must Integrate With:**
- [System 1 — e.g., QuickBooks for accounting]
- [System 2 — e.g., Salesforce for CRM]
- [System 3]

**Off-Limits / Cannot Use:**
- [Any prohibited tools, vendors, or approaches]

### Organizational Constraints

| Constraint | Details |
|------------|---------|
| **Approval Required** | [Who must sign off — names and roles] |
| **Political Sensitivities** | [Any landmines to avoid] |
| **Compliance/Security** | [SOC2, HIPAA, GDPR, etc.] |

### Data Reality Check

**Critical:** Validate that required data exists and is usable before significant engineering investment.

| Data Needed | Source | Quality (1-5) | Cleanup Needed? |
|-------------|--------|---------------|-----------------|
| [Data type 1] | [System/location] | [1-5] | [Yes/No + details] |
| [Data type 2] | [System/location] | [1-5] | [Yes/No + details] |
| [Data type 3] | [System/location] | [1-5] | [Yes/No + details] |

**Quality Scale:**
- 5 = Excellent (structured, complete, accessible, accurate)
- 4 = Good (minor gaps or formatting issues)
- 3 = Moderate (significant cleanup needed but usable)
- 2 = Poor (major gaps, inconsistencies, access issues)
- 1 = Unusable (would need to rebuild from scratch)

**⚠️ If any Data Quality < 3:** Budget data cleanup into solution scope and timeline.

**Data Access Issues:**
[Any blockers to accessing required data — permissions, privacy, credentials, etc.]

---
```

---

## Module 4: Technical Approach

**Purpose:** Define how we'll build this.

**Owner:** Engineer

**Milestone:** Engineering handoff ready.

```markdown
## Module 4: Technical Approach

### Architecture Overview

High-level description of the technical approach.

[Describe architecture — or include diagram]

```
[ASCII diagram or description for diagram creation]
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Source    │────▶│  Solution   │────▶│   Output    │
│   System    │     │  Component  │     │   System    │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Technology Stack

| Category | Choice | Notes |
|----------|--------|-------|
| **Existing Systems** | [Systems client already has] | |
| **New Systems** | [New tools/services to add] | |
| **Integration Method** | [APIs, webhooks, etc.] | |

### Component Breakdown

What are the major pieces that need to be built?

**Component 1: [Name]**
[What it does, key technical considerations]

**Component 2: [Name]**
[What it does, key technical considerations]

**Component 3: [Name]**
[What it does, key technical considerations]

### Human-in-the-Loop Evolution

*For AI-powered solutions: Define the autonomy progression.*

| Phase | Autonomy Level | Criteria to Advance |
|-------|----------------|---------------------|
| **Phase 1** | Assisted — AI does work, human reviews/approves everything | [Default starting point] |
| **Phase 2** | [e.g., Human spot-checks 20%] | [e.g., 95% accuracy over 100 tasks] |
| **Phase 3** | [e.g., Auto-approve if confidence >90%] | [e.g., 99% accuracy, zero critical errors] |

### Technical Assumptions

What must be true for this approach to work?

- [Technical assumption — e.g., API supports required operations]
- [Data assumption — e.g., Invoice PDFs are machine-readable]
- [Organizational assumption — e.g., IT will provide API credentials within 1 week]

---
```

---

## Module 5: Estimates & ROI

**Purpose:** Define effort, timeline, and investment case.

**Owner:** Engineer

**Milestone:** Investment decision ready.

```markdown
## Module 5: Estimates & ROI

### Complexity Assessment

| Factor | Score (1-5) | Rationale |
|--------|-------------|-----------|
| **Overall Complexity** | [1-5] | [Why this score] |

*Scale: 1=Simple, 2=Moderate, 3=Standard, 4=Complex, 5=Enterprise transformation*

### Effort Estimate

| Phase | Hours | Duration |
|-------|-------|----------|
| Discovery & Requirements | [X] | [X weeks] |
| Design & Architecture | [X] | [X weeks] |
| Build & Configure | [X] | [X weeks] |
| Testing & QA | [X] | [X weeks] |
| Training & Documentation | [X] | [X weeks] |
| Deployment & Support | [X] | [X weeks] |
| **TOTAL** | **[X] hours** | **[X] weeks** |

### Estimate Range

*Communicate uncertainty honestly.*

| Optimistic | Expected | Pessimistic |
|------------|----------|-------------|
| [X] hours | [Y] hours | [Z] hours |

**What would change the estimate:**
- Toward optimistic: [Factors — e.g., clean data, simple integrations]
- Toward pessimistic: [Factors — e.g., data cleanup, scope additions, availability delays]

### Investment & ROI

| Metric | Value |
|--------|-------|
| **Implementation Cost** | $[X] ([hours] × $[rate]) |
| **Annual Operating Cost** | $[X] (licenses, hosting, maintenance) |
| **Annual Benefit** | $[X] (from Module 1 quantified impact) |
| **Payback Period** | [X] months |
| **3-Year ROI** | [X]% |

### Dependencies & Prerequisites

What must happen before we can start or complete this?

- [ ] [Dependency 1 — e.g., API credentials from IT (2 week lead time)]
- [ ] [Dependency 2 — e.g., Data cleanup completed (if identified in Module 3)]
- [ ] [Dependency 3 — e.g., Stakeholder availability for testing]
- [ ] [Dependency 4 — e.g., Budget approval]

---
```

---

## Module 6: Risks & Adoption

**Purpose:** Identify what could go wrong and plan for successful adoption.

**Owner:** Collaborative (Strategist + Engineer)

**Milestone:** Implementation ready.

```markdown
## Module 6: Risks & Adoption

### Risk Register

| Risk | Likelihood | Impact | Mitigation | Owner |
|------|------------|--------|------------|-------|
| [Technical risk] | H/M/L | H/M/L | [How to prevent/handle] | [Name] |
| [Data risk] | H/M/L | H/M/L | [How to prevent/handle] | [Name] |
| [Adoption risk] | H/M/L | H/M/L | [How to prevent/handle] | [Name] |
| [Business risk] | H/M/L | H/M/L | [How to prevent/handle] | [Name] |

### Key Assumptions

What we're assuming is true. If these prove false, scope/estimate may change.

- [Assumption 1 — e.g., Client IT will provide sandbox access within 1 week]
- [Assumption 2 — e.g., Data volume is ~50 records/month as reported]
- [Assumption 3 — e.g., Primary user has 2 hours/week for testing]

### Open Questions

Questions that need answers before or during implementation.

| Question | Owner | Due | Status |
|----------|-------|-----|--------|
| [Question 1] | [Name] | [Date] | ⬜ Open |
| [Question 2] | [Name] | [Date] | ⬜ Open |
| [Question 3] | [Name] | [Date] | ⬜ Open |

### Change Management Plan

*70% of changes fail without proper reinforcement. Plan for adoption.*

| Element | Plan |
|---------|------|
| **Training Required** | [Hours, format, audience] |
| **Feedback Mechanism** | [How users report issues/suggestions] |
| **Review Cadence** | [e.g., Weekly for month 1, monthly for months 2-6] |
| **Success Owner** | [Who is accountable for adoption — name and role] |

### Go/No-Go Criteria

**Ship to production if:**
- ✅ [Criterion 1 — e.g., Accuracy ≥ 95% on test data]
- ✅ [Criterion 2 — e.g., Primary user validates workflow]
- ✅ [Criterion 3 — e.g., All P0 bugs resolved]
- ✅ [Criterion 4 — e.g., Training completed]

**Don't ship if:**
- 🚫 [Blocker 1 — e.g., Any data loss incidents during testing]
- 🚫 [Blocker 2 — e.g., Primary user rejects workflow]
- 🚫 [Blocker 3 — e.g., Critical integration failures]

---
```

---

## Appendix (Optional)

Add as needed for reference material.

```markdown
## Appendix

### A. Discovery Sources

| Source | Date | Key Insights |
|--------|------|--------------|
| [Meeting/Document name] | [Date] | [What we learned] |

### B. Comparable Solutions

| Solution | Similarity | Learnings |
|----------|------------|-----------|
| [Prior project or industry example] | [How it's similar] | [What we can apply] |

### C. Process Documentation

[Detailed current-state process if needed for reference]

### D. Stakeholder Map

| Stakeholder | Role | Interest | Influence | Strategy |
|-------------|------|----------|-----------|----------|
| [Name] | [Title] | [What they care about] | H/M/L | [How to engage] |
```

---

## Format Upgrades

**Primary format:** Markdown (.md)

**When to upgrade:**

| Format | Use When |
|--------|----------|
| **DOCX** | Formal client deliverable, needs Cadre branding, email attachment |
| **HTML** | Presenting in meeting, embedding in portal, visual polish matters |
| **PDF** | Final locked version, board/exec distribution |

**Brand application:**

When creating DOCX, HTML, or PDF versions, apply Cadre brand styling:
- Load `brand/brand.md` for voice, tone, and messaging patterns
- Load `brand/brand-ui.md` for colors, typography, and component styling
- Use brand colors: Primary Red (#DB4545), Blue (#08749B), warm backgrounds (#FAF9F6)
- Follow brand voice: direct, confident, jargon-free
