# Implementation Roadmap

Create phased action plans that sequence recommendations into executable timelines with milestones, dependencies, and success metrics.

## Contents

1. [When to Use](#when-to-use)
2. [Roadmap Structure](#roadmap-structure)
3. [Phase Design](#phase-design)
4. [Content Elements](#content-elements)
5. [Visual Formats](#visual-formats)
6. [Generation Process](#generation-process)
7. [Complete Example](#complete-example)

---

## When to Use

User says something like:
- "Create an implementation roadmap for [client]"
- "Build a phased action plan"
- "Generate the project timeline"
- "What should they do first, second, third?"

**Typical audience:** Project sponsors, implementation teams, steering committees
**Timeframes:** Usually 3-12 months
**Formats:** Document section, standalone visual, or slide(s)

### Roadmap vs. Other Deliverables

| Need | Deliverable |
|------|-------------|
| High-level timeline for leadership | Strategy Deck (roadmap section) |
| Detailed implementation plan | Standalone Roadmap |
| Week-by-week project schedule | Project plan (outside Cadre OS) |
| Reference documentation | Findings Report |

---

## Roadmap Structure

### Standard Three-Phase Model

Most Cadre engagements follow a three-phase approach:

| Phase | Name | Typical Duration | Focus |
|-------|------|------------------|-------|
| 1 | Quick Wins | 2-4 weeks | Build credibility, early ROI |
| 2 | Foundation | 4-12 weeks | Core capabilities, integrations |
| 3 | Scale | 3-6 months | Optimization, expansion |

### Phase Purposes

**Phase 1: Quick Wins**
- Demonstrate value fast
- Build organizational confidence
- Address "skeptic" stakeholders
- Low risk, high visibility
- Sets stage for larger initiatives

**Phase 2: Foundation**
- Establish core infrastructure
- Complete key integrations
- Build team capabilities
- Formalize processes
- Create feedback loops

**Phase 3: Scale**
- Expand successful pilots
- Optimize based on learnings
- Add advanced capabilities
- Measure and refine ROI
- Plan next horizons

### Alternative Structures

**Four-Phase (Longer Engagements):**
1. Quick Wins (2-4 weeks)
2. Foundation (6-8 weeks)
3. Integration (8-12 weeks)
4. Optimization (ongoing)

**Two-Phase (Simpler Engagements):**
1. Implementation (4-8 weeks)
2. Optimization (ongoing)

**Parallel Tracks:**
When initiatives can run simultaneously:
- Track A: Technology implementation
- Track B: Change management
- Track C: Process redesign

---

## Phase Design

### What Goes in Each Phase

#### Phase 1: Quick Wins

**Selection Criteria:**
- Impact = High AND Effort = Low (from prioritizer)
- Minimal dependencies
- Visible results in <4 weeks
- Low integration complexity
- Strong stakeholder support

**Typical Quick Wins:**
- Automated reporting/dashboards
- Simple workflow automation
- Data cleanup/standardization
- Pilot AI assistants (limited scope)
- Process documentation

**Deliverables:**
- Working solution(s)
- Early metrics
- Lessons learned
- Case for Phase 2

#### Phase 2: Foundation

**Selection Criteria:**
- Score ≥ 12 from prioritizer
- Dependencies from Phase 1 resolved
- Moderate complexity acceptable
- 4-12 week implementation

**Typical Foundation Work:**
- System integrations
- AI model training/tuning
- Process redesign
- Team training
- Governance frameworks

**Deliverables:**
- Core capabilities operational
- Integration complete
- Processes documented
- Team trained
- Metrics baseline established

#### Phase 3: Scale

**Selection Criteria:**
- Strategic importance
- Builds on Phase 1-2 success
- Higher complexity acceptable
- Clear ROI model

**Typical Scale Work:**
- Enterprise rollout
- Advanced AI capabilities
- Cross-functional integration
- Continuous improvement
- New use case expansion

**Deliverables:**
- Full deployment
- Measured ROI
- Optimization recommendations
- Future roadmap

### Sequencing Rules

Apply these rules from synthesis/prioritizer.md:

1. **Dependencies first** — If B requires A, schedule A before B
2. **Quick wins early** — Build credibility before big bets
3. **Root causes before symptoms** — Fix foundations first
4. **Stakeholder alignment** — Consider change readiness
5. **Resource constraints** — Don't overload teams

### Handling Dependencies

Document dependencies explicitly:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Automated   │────▶│ ERP-CRM     │────▶│ AI-Powered  │
│ Reporting   │     │ Integration │     │ Forecasting │
└─────────────┘     └─────────────┘     └─────────────┘
    Phase 1              Phase 2             Phase 3

Dependencies:
- ERP-CRM Integration requires: Reporting complete (validates data)
- AI Forecasting requires: ERP-CRM Integration (needs unified data)
```

---

## Content Elements

### For Each Phase

| Element | Description |
|---------|-------------|
| **Name** | Descriptive label (not just "Phase 1") |
| **Duration** | Specific timeframe (weeks or months) |
| **Objectives** | 2-3 bullet points on what success looks like |
| **Initiatives** | Specific projects/workstreams |
| **Milestone** | Concrete deliverable marking completion |
| **Dependencies** | What must be true to start |
| **Resources** | Who/what is needed |
| **Success Metrics** | How we measure completion |
| **Risks** | Key risks and mitigations |

### For Each Initiative

| Element | Description |
|---------|-------------|
| **Name** | Clear, specific title |
| **Description** | 1-2 sentences on scope |
| **Owner** | Suggested role/person |
| **Duration** | Estimated timeline |
| **Dependencies** | Prerequisites |
| **Deliverable** | What's produced |
| **Success Metric** | How measured |

### Milestones

Milestones should be:
- **Concrete** — A specific, observable outcome
- **Verifiable** — Can objectively assess if achieved
- **Meaningful** — Represents real progress
- **Celebratable** — Worth acknowledging with stakeholders

| Weak Milestone | Strong Milestone |
|----------------|------------------|
| "Phase 1 complete" | "Daily reports delivered automatically by 8am" |
| "Integration done" | "CRM and ERP sync in real-time with <1% error rate" |
| "Team trained" | "All dispatchers certified on new scheduling tool" |

---

## Visual Formats

### Format 1: Timeline View

```
┌────────────────────────────────────────────────────────────────────┐
│ Implementation Roadmap                                             │
├────────────────────────────────────────────────────────────────────┤
│                                                                    │
│     Dec           Jan           Feb           Mar           Apr    │
│      │             │             │             │             │     │
│      ▼             ▼             ▼             ▼             ▼     │
│  ╔═══════════╗ ╔═══════════════════════════╗ ╔═══════════════════╗│
│  ║ Phase 1   ║ ║ Phase 2                   ║ ║ Phase 3           ║│
│  ║ Quick Wins║ ║ Foundation                ║ ║ Scale             ║│
│  ╚═══════════╝ ╚═══════════════════════════╝ ╚═══════════════════╝│
│       │                 │                            │             │
│       ▼                 ▼                            ▼             │
│   [Milestone 1]    [Milestone 2]              [Milestone 3]        │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### Format 2: Swimlane View (Parallel Tracks)

```
┌────────────────────────────────────────────────────────────────────┐
│ Implementation Roadmap                                             │
├────────────────────────────────────────────────────────────────────┤
│              Week 1-2    Week 3-4    Month 2     Month 3           │
│                                                                    │
│ Technology   ┌────────────────────────────────────────────┐        │
│              │ Reporting │ Integration │ AI Rollout      │        │
│              └────────────────────────────────────────────┘        │
│                                                                    │
│ Process      ┌─────────────────────────────────────┐               │
│              │ Document  │ Redesign   │ Optimize  │               │
│              └─────────────────────────────────────┘               │
│                                                                    │
│ People       ┌──────────────────────────────────────────────┐      │
│              │ Awareness │ Training   │ Certification      │      │
│              └──────────────────────────────────────────────┘      │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

### Format 3: Phase Detail Cards

```
╔═══════════════════════════════════════╗
║ PHASE 1: QUICK WINS                   ║
║ Duration: Weeks 1-4                   ║
╠═══════════════════════════════════════╣
║                                       ║
║ OBJECTIVES                            ║
║ • Demonstrate early value             ║
║ • Build stakeholder confidence        ║
║ • Validate technical approach         ║
║                                       ║
║ INITIATIVES                           ║
║ □ Automated daily reporting           ║
║ □ Dashboard deployment                ║
║ □ Data validation scripts             ║
║                                       ║
║ MILESTONE                             ║
║ ✓ Reports delivered by 8am daily      ║
║                                       ║
║ SUCCESS METRICS                       ║
║ • 8+ hours/week saved                 ║
║ • 100% report accuracy                ║
║ • Stakeholder satisfaction >4/5       ║
║                                       ║
╚═══════════════════════════════════════╝
```

### Format 4: Document Table

```markdown
## Implementation Roadmap

| Phase | Duration | Initiatives | Milestone | Success Metrics |
|-------|----------|-------------|-----------|-----------------|
| **Phase 1: Quick Wins** | Weeks 1-4 | • Automated reporting<br>• Dashboard deployment | Reports by 8am daily | 8 hrs/wk saved |
| **Phase 2: Foundation** | Months 2-3 | • ERP-CRM integration<br>• Process redesign | Real-time data sync | <1% error rate |
| **Phase 3: Scale** | Months 4-6 | • AI forecasting<br>• Enterprise rollout | Predictive ops live | 30% efficiency gain |
```

---

## Generation Process

### Step 1: Gather Inputs

```
1. Run synthesis/prioritizer.md → Get:
   - Ranked challenges with scores
   - Ranked solutions with scores
   - Dependencies map
   - Recommended sequence

2. Query data access → Get:
   - Client constraints (timeline, budget, resources)
   - Stakeholder change readiness
   - Technical landscape
```

### Step 2: Assign to Phases

```
For each solution from prioritizer:

1. Check dependencies:
   - Any prerequisites unresolved? → Later phase
   - All dependencies met? → Can schedule

2. Apply phase criteria:
   - Impact=High, Effort=Low, No deps → Phase 1
   - Score ≥ 12, Moderate complexity → Phase 2
   - Strategic, builds on earlier → Phase 3

3. Validate sequencing:
   - Dependencies satisfied?
   - Resource conflicts avoided?
   - Change management realistic?
```

### Step 3: Define Details

```
For each phase:

1. Set duration based on initiative complexity
2. Write 2-3 clear objectives
3. List specific initiatives (from solutions)
4. Define concrete milestone
5. Set measurable success metrics
6. Identify key dependencies
7. Note resource requirements
8. Flag risks and mitigations
```

### Step 4: Create Visual

```
1. Choose format based on context:
   - Timeline: Simple sequential flow
   - Swimlane: Parallel workstreams
   - Cards: Detailed phase breakdown
   - Table: Document-friendly

2. Apply Cadre styling:
   - Colors: Deep Blue (#034377) headers
   - Accent: Coral Red (#DB4545) milestones
   - Clean, professional, minimal

3. Validate readability:
   - Can understand in 30 seconds?
   - Milestones clearly marked?
   - Dependencies visible?
```

### Step 5: Quality Check

Before delivery, verify:
- [ ] Phases logically sequenced
- [ ] Dependencies respected
- [ ] Quick wins in Phase 1
- [ ] Milestones are concrete and verifiable
- [ ] Success metrics are measurable
- [ ] Timeline is realistic
- [ ] Resource requirements noted
- [ ] Risks acknowledged

---

## Complete Example

### CES Implementation Roadmap

```markdown
# Contemporary Energy Solutions
## AI Implementation Roadmap

**Prepared by:** Cadre AI  
**Date:** November 28, 2025  
**Scope:** Operations AI Transformation

---

## Executive Summary

This roadmap outlines a three-phase approach to AI implementation at CES,
starting with quick wins to build organizational confidence, establishing
foundational integrations, then scaling to enterprise-wide optimization.

**Total Duration:** 6 months  
**Key Milestone:** Real-time operational visibility by end of Month 3

---

## Phase 1: Quick Wins
**Duration:** Weeks 1-4 (December 2025)

### Objectives
- Demonstrate immediate value through automated reporting
- Build credibility with skeptical technical staff
- Establish foundation for data integration

### Initiatives

| Initiative | Owner | Duration | Deliverable |
|------------|-------|----------|-------------|
| Automated Daily Reporting | IT Lead | 2 weeks | Dashboard pulling ERP + CRM + Analytics |
| Data Validation Framework | Data Team | 1 week | Validation scripts + error logging |
| Stakeholder Communication | Project Sponsor | Ongoing | Weekly updates to steering committee |

### Dependencies
- IT resource allocated (confirmed)
- System access credentials (confirmed)
- Executive sponsorship (confirmed)

### Milestone
✓ **Daily operational reports delivered by 8am** — replacing 2-day manual process

### Success Metrics
- Reports delivered on time: 100%
- Data accuracy: >99%
- Time saved: 8+ hours/week
- User satisfaction: >4/5 rating

### Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| IT resource conflict | Medium | High | Pre-committed allocation from CTO |
| Data quality issues | Medium | Medium | Validation framework catches errors |

---

## Phase 2: Foundation
**Duration:** Months 2-3 (January-February 2026)

### Objectives
- Eliminate data silos through ERP-CRM integration
- Implement AI-powered dispatch optimization
- Establish data governance framework

### Initiatives

| Initiative | Owner | Duration | Deliverable |
|------------|-------|----------|-------------|
| ERP-CRM Integration | IT Lead | 6 weeks | Real-time bidirectional sync |
| Dispatch Optimization MVP | Ops Manager | 4 weeks | AI routing for 2 regions (pilot) |
| Process Documentation | Process Lead | 3 weeks | SOPs for new workflows |
| Team Training | HR/Training | 2 weeks | Dispatcher certification program |

### Dependencies
- Phase 1 complete (reporting validates data quality)
- Integration budget approved
- Pilot regions selected

### Milestone
✓ **Real-time data sync operational** — ERP and CRM synchronized with <1% error rate

### Success Metrics
- Integration uptime: >99.5%
- Data sync latency: <5 minutes
- Dispatch efficiency (pilot): +20% improvement
- Team certification: 100% dispatchers trained

### Risks & Mitigations
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Integration complexity | Medium | High | Phased rollout, rollback plan |
| Change resistance | Medium | Medium | Champion network, early wins messaging |
| Scope creep | Medium | Medium | Strict change control process |

---

## Phase 3: Scale
**Duration:** Months 4-6 (March-May 2026)

### Objectives
- Expand dispatch optimization enterprise-wide
- Deploy predictive analytics for operations
- Achieve target ROI and efficiency gains

### Initiatives

| Initiative | Owner | Duration | Deliverable |
|------------|-------|----------|-------------|
| Dispatch Rollout | Ops Director | 8 weeks | All regions on AI dispatch |
| Predictive Maintenance | IT Lead | 6 weeks | Equipment failure prediction |
| Performance Analytics | Data Team | 4 weeks | Executive dashboard + alerts |
| Continuous Improvement | Project Lead | Ongoing | Optimization based on learnings |

### Dependencies
- Phase 2 integration stable
- Dispatch pilot successful
- Historical data available for predictive models

### Milestone
✓ **Predictive operations live** — AI-powered dispatch and maintenance prediction deployed enterprise-wide

### Success Metrics
- Dispatch efficiency: +40% vs. baseline
- Predictive accuracy: >85%
- Overall time savings: 30+ hours/week
- ROI achieved: >150% of investment

---

## Timeline Overview

```
         Dec        Jan        Feb        Mar        Apr        May
          │          │          │          │          │          │
Phase 1   ████████
          Quick Wins
                     │
Phase 2              ██████████████████████
                     Foundation
                                           │
Phase 3                                    ████████████████████████
                                           Scale
          │          │          │          │          │          │
          ▼          ▼          ▼          ▼          ▼          ▼
       Reports    Integration  Training   Rollout   Predictive  ROI
       Live       Complete     Done       Begin     Live        Review
```

---

## Resource Requirements

| Role | Phase 1 | Phase 2 | Phase 3 |
|------|---------|---------|---------|
| IT Lead | 50% | 75% | 50% |
| Data Team | 25% | 50% | 75% |
| Ops Manager | 25% | 50% | 50% |
| External (Cadre) | Support | Implementation | Advisory |

---

## Governance

**Steering Committee:** Monthly review with executive sponsors  
**Project Team:** Weekly standups, bi-weekly demos  
**Change Control:** All scope changes require steering committee approval

---

## Next Steps

1. **Approve roadmap and Phase 1 scope** — Owner: Executive Sponsor, By: Dec 6
2. **Confirm IT resource allocation** — Owner: CTO, By: Dec 8
3. **Kick off Phase 1** — Owner: Cadre + CES Team, By: Dec 11

---

*Prepared by Cadre AI | cadreai.com*
```
