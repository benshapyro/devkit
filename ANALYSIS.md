# Cadre-OS Solution Brief Enhancement Analysis

## Executive Summary

Kate's feedback on the cadre-os solution brief functionality has identified several missing features and reliability issues. This document outlines the current state, identified issues, root causes, and implementation plan.

**Slack Thread:** https://gocadre-ai.slack.com/archives/C09D9T85X45/p1770067273396169?thread_ts=1767770598.070709&cid=C09D9T85X45

---

## Current State

### Existing Functionality

The cadre-os skill contains comprehensive solution brief functionality:

**Location:** `/home/user/devkit/skills/internal-specialty/cadre-os/references/deliverables.md` (lines 739-1117)

**Structure:**
- **7 modules** (0-6) that users work through progressively
- **Workshop protocol:** Search → Synthesize → Present → Discuss → Refine → Confirm
- **Module templates** with specific structures for each phase
- **Quality checklists** for validation

**Module Overview:**
| Module | Name | Owner | Milestone |
|--------|------|-------|-----------|
| 0 | Discovery & Validation | Strategist | Feasibility confirmed |
| 1 | Problem & Context | Strategist | Quick pitch ready |
| 2 | Solution Concept | Strategist | Stakeholder alignment |
| 3 | Constraints & Data | Strategist | Technical feasibility |
| 4 | Technical Approach | Engineer | Engineering handoff |
| 5 | Estimates & ROI | Engineer | Investment decision |
| 6 | Risks & Adoption | Collaborative | Implementation ready |

**Commands:**
- `/brief [solution name]` - Standalone brief
- `/solutions brief [use case]` - Brief for AI solution from discovery pipeline

**Templates Available:**
- `scoping-template.docx` - Word template
- `scoping-spreadsheet.xlsx` - Spreadsheet format

---

## Issues Identified

### 1. Missing: Solution Complexity Exploration

**Kate's Feedback:**
> "During brief creation: I am directing it to a different solution from what it scoped to explore options, for example: from full blown mobile app to PWA, from AI to rule-based, from rule-based to AI, from assistant to automation, from automation to assistant, from PWA to automation, basically all directions of complexity movement."

**Observation:**
> "block-builder interviews to ask if which method we prefer but it'd be 🍌 if cadre-os can spin up different solutions based on complexity & ask us which one we want to explore"

**Current Gap:**
- The current workflow focuses on drafting content for a single solution direction
- No step to explore alternative approaches at different complexity levels
- User must manually redirect Claude to explore different solution types

**Desired State:**
- cadre-os should proactively offer 2-4 solution variations at different complexity levels
- Present trade-offs for each approach
- Let user select which direction to pursue

---

### 2. Missing: Post-Brief Enhancements

**Kate's Feedback:**
> "After the briefs, I ask it to:
> - Add additional features that are out of scope for now but client might want (SE opps)
> - Add hours expected for each module for strategist, engineer, & AI manager hours
> - Add expected meetings with clients for discovery & review
> - Create a prototype if it is a PWA webapp based on the brief"

**Current Gaps:**

#### A. Out of Scope Features (SE Opportunities)
- **Current:** Module 2 has "Scope Definition" with In Scope/Out of Scope, but it's minimal
- **Gap:** No explicit prompt to identify future enhancement opportunities for sales engineering
- **Impact:** Missing revenue opportunities and client planning insights

#### B. Role-Based Hour Estimates
- **Current:** Module 5 has effort estimates by phase, but not by role
- **Gap:** No breakdown of hours for Strategist, Engineer, AI Manager
- **Impact:** Harder to resource plan and understand who does what

#### C. Meeting Time Estimates
- **Current:** Module 5 focuses on build time only
- **Gap:** No accounting for discovery meetings, review sessions, client checkpoints
- **Impact:** Underestimates true project timeline and client involvement

#### D. Prototype Generation
- **Current:** Workflow ends at documentation
- **Gap:** No step to create PWA/webapp prototypes based on the brief
- **Impact:** Missed opportunity to visualize the solution and accelerate client buy-in

---

### 3. Reliability Issue: DOCX Format

**Kate's Feedback:**
> "Also skill is unreliability not always giving us a docx. Sometimes it's just an md that I have to ask to convert to docx"

**Current Gap:**
- The deliverables.md reference doesn't explicitly specify output format
- Relies on general system skills (pptx, docx) being invoked correctly
- No explicit instruction to output as DOCX file

**Root Cause:**
- Missing explicit format specification in workshop protocol
- No format enforcement in quality checklist
- Ambiguous about when to use markdown vs Word format

---

## Root Cause Analysis

### Issue 1: No Complexity Exploration
- **Root Cause:** Current protocol assumes user knows desired solution type
- **Why it matters:** Early-stage scoping requires exploring trade-offs before committing
- **block-builder precedent:** Other skills already use interview-based approach to explore options

### Issue 2A: No SE Opportunity Identification
- **Root Cause:** Out of Scope section treated as a constraint, not an opportunity
- **Why it matters:** SE opportunities are valuable for client planning and revenue
- **Cultural factor:** Focus on current scope, not future expansion

### Issue 2B: No Role-Based Estimates
- **Root Cause:** Module 5 template uses phase-based breakdown (Discovery, Build, Testing)
- **Why it matters:** Different roles (Strategist, Engineer, AI Manager) have different rates and availability
- **Missing structure:** No table for role × module breakdown

### Issue 2C: No Meeting Time
- **Root Cause:** Module 5 focuses on "build time" not total project time
- **Why it matters:** Client meetings are significant time commitment
- **Missing awareness:** Workshop protocol doesn't prompt for meeting planning

### Issue 2D: No Prototype Generation
- **Root Cause:** Workflow is documentation-focused, not artifact-focused
- **Why it matters:** Prototypes accelerate buy-in and clarify requirements
- **Missing trigger:** No conditional step based on solution type (PWA = offer prototype)

### Issue 3: DOCX Format Reliability
- **Root Cause:** No explicit format requirement in instructions
- **Why it matters:** Users expect consistent Word format for client deliverables
- **Missing enforcement:** Workshop protocol doesn't specify "export as DOCX"

---

## Future State Design

### Enhancement 1: Solution Exploration Phase

**When:** After user specifies solution name, before Module 0 or during Module 2

**Process:**
1. Acknowledge the solution concept
2. Ask if user wants to explore different complexity levels
3. Generate 2-4 solution variations:
   - **High complexity:** Full automation, native app, AI-powered
   - **Medium complexity:** Assisted workflow, PWA, hybrid AI/rules
   - **Low complexity:** Manual enhancement, spreadsheet-based, rule-based
   - **Alternative approach:** Different architecture or technology choice
4. Present comparison table:
   - Capabilities
   - User experience
   - Effort estimate (rough)
   - Data requirements
   - Pros/cons
5. Let user select which to pursue

**Example Output:**
```markdown
## Solution Exploration: Sales Rebate Assistant

I can help you explore this solution at different complexity levels:

| Approach | Description | Effort | Pros | Cons |
|----------|-------------|--------|------|------|
| **Full AI Automation** | LLM researches utilities, auto-populates rebate forms | High (120-160h) | Fastest for users, handles edge cases | Requires AI validation, higher cost |
| **Assisted AI** | LLM suggests utilities, user confirms and fills form | Medium (60-80h) | Balanced automation + control | Still requires user time |
| **Rule-Based Lookup** | Database of utilities by location, user selects | Low (30-40h) | Fast to build, reliable | Limited to known utilities, manual updates |
| **PWA vs Native** | Progressive web app vs mobile app | Medium vs High | PWA: works everywhere; Native: better UX | Trade-off: reach vs polish |

Which approach interests you? I can develop a brief for any of these, or a hybrid.
```

**Triggers:**
- After `/brief [solution name]` command
- During Module 2 (Solution Concept) if user indicates uncertainty
- If user redirects to different solution type during workshop

---

### Enhancement 2A: Out of Scope / Future Opportunities

**When:** After Module 2 (Solution Concept)

**Addition to Module 2 Template:**
```markdown
### Future Opportunities (Out of Scope)

Features intentionally excluded from initial build but valuable for future phases:

| Feature | Business Value | Estimated Effort | Priority for Phase 2 |
|---------|----------------|------------------|---------------------|
| [Feature 1] | [Value to client] | [Rough hours] | High / Medium / Low |
| [Feature 2] | [Value to client] | [Rough hours] | High / Medium / Low |

**Sales Engineering Opportunities:**
- [Potential expansion 1]
- [Potential expansion 2]
```

**Workshop Protocol Update:**
- After completing Module 2, prompt: "Should I identify future enhancement opportunities that are out of scope for now?"
- Generate 3-5 features that logically extend the solution
- Frame as SE opportunities for phase 2 planning

---

### Enhancement 2B: Role-Based Hour Estimates

**When:** Module 5 (Estimates & ROI)

**Enhanced Template:**
```markdown
## Module 5: Estimates & ROI

### Effort Estimate by Role

| Module/Phase | Strategist Hours | Engineer Hours | AI Manager Hours | Total Hours |
|--------------|------------------|----------------|------------------|-------------|
| Discovery & Requirements | [X] | [X] | [X] | [X] |
| Solution Design | [X] | [X] | [X] | [X] |
| Build & Configure | [X] | [X] | [X] | [X] |
| Testing & QA | [X] | [X] | [X] | [X] |
| Deployment & Training | [X] | [X] | [X] | [X] |
| **TOTALS** | **[X]** | **[X]** | **[X]** | **[X]** |

### Estimate Ranges by Role

| Role | Optimistic | Expected | Pessimistic |
|------|------------|----------|-------------|
| Strategist | [X] hours | [X] hours | [X] hours |
| Engineer | [X] hours | [X] hours | [X] hours |
| AI Manager | [X] hours | [X] hours | [X] hours |
| **TOTAL** | **[X]** | **[X]** | **[X]** |

### Client Meeting Time

| Meeting Type | Quantity | Duration Each | Total Hours | Attendees |
|--------------|----------|---------------|-------------|-----------|
| Discovery Sessions | [X] | [X] hours | [X] hours | [Roles] |
| Design Review | [X] | [X] hours | [X] hours | [Roles] |
| Progress Checkpoints | [X] | [X] hours | [X] hours | [Roles] |
| UAT & Training | [X] | [X] hours | [X] hours | [Roles] |
| **TOTAL MEETING TIME** | | | **[X] hours** | |

**Note:** Meeting time is client commitment, not billable hours.

### Total Project Timeline

| Component | Hours | Notes |
|-----------|-------|-------|
| Total Build Time | [X] | Strategist + Engineer + AI Manager |
| Client Meeting Time | [X] | Discovery + Reviews + Training |
| **Total Project Time** | **[X]** | End-to-end timeline |
```

**Workshop Protocol Update:**
- When generating Module 5, prompt: "Let me break down hours by role (Strategist, Engineer, AI Manager) and add expected meeting time."
- Calculate role-specific hours based on module complexity
- Add standard meeting cadence (discovery, reviews, UAT)

---

### Enhancement 2C: Prototype Generation Step

**When:** After Module 4 (Technical Approach), if solution type is PWA/webapp

**New Optional Step:**
```markdown
### Prototype Generation (Optional)

**Solution Type:** [PWA / Web App / Mobile App]

**Prototype Approach:**
☐ **HTML/CSS Mockup** — Static visual prototype
☐ **Interactive PWA** — Functional prototype with sample data
☐ **Figma Design** — Design mockup with flows
☐ **Skip** — Documentation only

**If Interactive PWA:**
- Uses artifact templates from `assets/artifact-templates/`
- Implements core user flows from Module 4
- Sample data based on Module 3 constraints
- Branded with Cadre styling from `brand.md`
```

**Workshop Protocol Update:**
```markdown
### After Module 4 Completion

If solution type includes PWA, web app, or interactive artifact:

1. Ask: "Would you like me to create a prototype based on this technical approach?"
2. If yes:
   - Use existing artifact templates if applicable
   - Generate interactive HTML/JSX artifact
   - Apply Cadre brand styling
   - Include sample data from brief
   - Present artifact with instructions for testing
3. If no: Proceed to Module 5
```

**Conditional Logic:**
- If Module 4 includes "PWA", "web app", "webapp", "portal", "dashboard" → Offer prototype
- If Module 4 is API, automation, backend only → Skip prototype offer
- User can always request prototype manually

---

### Enhancement 3: DOCX Format Enforcement

**Updates to Workshop Protocol:**

**After completing all modules:**
```markdown
### Final Deliverable

1. Generate complete brief content in markdown
2. Convert to DOCX format using Word export
3. Apply document styling:
   - Cadre brand colors (from brand.md)
   - Professional formatting (11pt body, 14-18pt headings)
   - Clean table formatting
4. Save as: `[Solution Name] - Solution Brief.docx`
5. Present download link to user

**Format:** Always deliver as DOCX unless user explicitly requests markdown.
```

**Addition to Quality Checklist:**
```markdown
### Solution Brief Quality Checklist

**Format & Delivery:**
- [ ] Exported as DOCX file (not markdown)
- [ ] File name format: [Solution Name] - Solution Brief.docx
- [ ] Cadre brand styling applied
- [ ] Tables render correctly in Word
- [ ] No markdown artifacts (##, **, etc.) visible
```

**Explicit Instruction in deliverables.md:**
```markdown
## Output Format

**CRITICAL:** Solution briefs must be delivered as DOCX files, not markdown.

**Process:**
1. Draft content in markdown during workshop
2. When brief is complete, convert to DOCX
3. Apply Cadre brand styling (see brand.md)
4. Verify formatting in Word
5. Deliver DOCX file to user

**Exception:** User can request markdown for intermediate drafts, but final deliverable must be DOCX.
```

---

## Implementation Plan

### Files to Modify

1. **Primary File:** `/home/user/devkit/skills/internal-specialty/cadre-os/references/deliverables.md`
   - Add Solution Exploration section (before Module 0)
   - Enhance Module 2 template (add Future Opportunities section)
   - Enhance Module 5 template (add role breakdown and meetings)
   - Add Prototype Generation step (after Module 4)
   - Update Workshop Protocol (DOCX enforcement)
   - Update Quality Checklist

### Changes Summary

| Section | Change Type | Lines to Add/Modify |
|---------|-------------|---------------------|
| Solution Exploration | New section | ~100 lines |
| Module 2 Enhancement | Template update | ~20 lines |
| Module 5 Enhancement | Template replacement | ~80 lines |
| Prototype Generation | New section | ~60 lines |
| Workshop Protocol | Updates throughout | ~40 lines |
| Quality Checklist | Add items | ~10 lines |
| **TOTAL** | | **~310 lines** |

### Testing Plan

After implementation:

1. **Test Solution Exploration:**
   - Run `/brief [new solution]` and verify exploration prompt
   - Verify comparison table generation
   - Test with different solution types (PWA, automation, AI assistant)

2. **Test Module 2 Enhancement:**
   - Complete a brief through Module 2
   - Verify Future Opportunities section is populated
   - Check SE opportunity identification

3. **Test Module 5 Enhancement:**
   - Complete a brief through Module 5
   - Verify role-based hour breakdown
   - Verify meeting time calculations
   - Check estimate ranges by role

4. **Test Prototype Generation:**
   - Complete a brief for PWA solution through Module 4
   - Verify prototype offer triggers
   - Test prototype generation with sample data

5. **Test DOCX Format:**
   - Complete a full brief
   - Verify DOCX output without prompting
   - Check Cadre brand styling
   - Verify tables and formatting

---

## Success Metrics

### Quantitative
- ✅ 100% of solution briefs start with complexity exploration
- ✅ 100% of Module 2 sections include Future Opportunities
- ✅ 100% of Module 5 estimates include role breakdown and meetings
- ✅ 100% of PWA solutions offer prototype generation
- ✅ 100% of final briefs delivered as DOCX

### Qualitative
- ✅ Users report less manual redirection needed
- ✅ Users report better resource planning from role breakdowns
- ✅ Users report SE opportunities are valuable
- ✅ Users report prototypes accelerate client buy-in
- ✅ Users report no format conversion needed

---

## Risks & Mitigations

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| Solution exploration adds too much friction | Medium | Low | Make it optional, can skip to direct brief |
| Role estimates are inaccurate | Medium | Medium | Provide ranges, allow user adjustment |
| Prototype generation takes too long | Low | Medium | Make it optional, offer simple mockup option |
| DOCX conversion fails in some environments | High | Low | Fallback to markdown with conversion instructions |
| Changes break existing brief workflow | High | Low | Thorough testing, backward compatibility |

---

## Next Steps

1. ✅ Complete this analysis
2. ⬜ Review with team/stakeholders
3. ⬜ Implement changes to deliverables.md
4. ⬜ Test all scenarios
5. ⬜ Update CHANGELOG.md
6. ⬜ Commit and push changes
7. ⬜ Create PR with link to Slack thread
8. ⬜ Deploy to cadre-os users

---

## Appendix: Kate's Full Feedback

**During brief creation:**
> "I am directing it to a _different_ solution from what it scoped to explore options, for example: from full blown mobile app to PWA, from AI to rule-based, from rule-based to AI, from assistant to automation, from automation to assistant, from PWA to automation, _basically all directions of complexity movement_.
>
> `block-builder` interviews to ask if which method we prefer but it'd be 🍌 if `cadre-os` can spin up different solutions based on complexity & ask us which one we want to explore"

**After the briefs:**
> "I ask it to:
> - Add additional features that are out of scope for now but client might want (SE opps).
> - Add hours expected for each module for strategist, engineer, & AI manager hours
> - Add expected meetings with clients for discovery & review
> - Create a prototype if it is a PWA webapp based on the brief."

**Format issue:**
> "Also skill is unreliability not always giving us a `docx`. Sometimes it's just an `md` that I have to ask to convert to docx"

---

**Analysis Date:** February 2, 2026
**Author:** Claude (via devkit analysis)
**Related Slack Thread:** https://gocadre-ai.slack.com/archives/C09D9T85X45/p1770067273396169
