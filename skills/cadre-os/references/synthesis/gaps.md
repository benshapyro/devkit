# Gap Analysis

Assess discovery coverage against the methodology checklist and identify what's missing.

## Contents

1. [When to Use](#when-to-use)
2. [Execution Flow](#execution-flow)
3. [Coverage Checklist](#coverage-checklist)
4. [Scoring Coverage](#scoring-coverage)
5. [Output Format](#output-format)
6. [Example Output](#example-output)

---

## When to Use

User says something like:
- "What gaps remain in our discovery?"
- "Are we ready for strategy?"
- "What haven't we covered yet?"
- "Check our discovery coverage"
- "What else do we need to learn?"

---

## Execution Flow

### Step 0: Pre-flight Check

Before analyzing gaps, complete the Pre-flight Check from SKILL.md:
1. Load schema from `references/data/discovery-catalog.md`
2. Get Client ID from 0_Clients table
3. Fetch Client Brain for context (stakeholder dynamics, preferences)

### Step 1: Load Coverage Checklist

Reference the Discovery Coverage Checklist from the playbook:
```
Read: references/methodology/playbook.md
Section: "Discovery Coverage Checklist" (lines 215-263)
```

**DO NOT duplicate the checklist here.** The playbook is the single source of truth for what items to check. This file contains the verification criteria (HOW to check) and scoring methodology.

**Summary:** 5 dimensions, ~35 items total
- People Coverage (7 items)
- Process Coverage (7 items)
- Technology Coverage (7 items)
- Challenge Coverage (7 items)
- Solution Coverage (7 items)

### Step 2: Query Existing Findings

Query Discovery Catalog. Schema already loaded in Pre-flight Check.
Quick reference: `references/data/discovery-catalog.md`

```
Base ID: apprH2AppvnKfUpT0

For each table, get counts and key attributes:
- 2_People: Count, Stakeholder Type distribution, ADKAR Stage distribution
- 3_Process: Count, Automation Level distribution, Frequency values
- 4_Technology: Count, Tool Type distribution, API Available counts
- 5_Challenges: Count, Problem Type distribution, Impact Score ranges
- 6_Solutions: Count, Solution Type distribution, Feasibility Score ranges, Horizon distribution
```

### Step 3: Map Findings to Checklist

For each checklist item, determine:

| Status | Criteria |
|--------|----------|
| ✅ Covered | Finding exists with Medium+ confidence |
| ⚠️ Partial | Finding exists but Low confidence or incomplete |
| ❌ Missing | No relevant finding |
| 🔍 Inferred | Can be derived from other findings |

### Step 4: Calculate Coverage Scores

**Dimension Score:**
```
Score = (Covered × 1.0 + Partial × 0.5 + Inferred × 0.3) / Total Items
```

**Overall Readiness:**
```
Readiness = Average of all dimension scores
```

| Readiness Score | Status | Recommendation |
|-----------------|--------|----------------|
| 90%+ | Ready | Proceed to synthesis/strategy |
| 70-89% | Nearly Ready | Address critical gaps, then proceed |
| 50-69% | Gaps Remain | 1-2 more discovery sessions recommended |
| <50% | Early Stage | Continue discovery phase |

### Step 5: Prioritize Gaps

Rank missing items by:

1. **Criticality** — Is this blocking strategy development?
2. **Obtainability** — Can we get this in one session?
3. **Dependency** — Do other gaps depend on this?

---

## Verification Criteria

How to programmatically verify each checklist item from the playbook. Use these criteria when querying the Discovery Catalog.

### People Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Economic buyer identified | Person with Role_Type = "Economic Buyer" | Yes |
| Champion identified | Person with Archetype = "Champion" or Role_Type = "Champion" | Yes |
| Key influencers mapped | 3+ people with Power ≥ 7 | Yes |
| Potential blockers identified | People with Sentiment ≤ 4 or Archetype = "Skeptic" | Yes |
| Technical decision makers found | Person with Role_Type = "Technical Lead" | Medium |
| End users represented | At least one end-user perspective in sessions | Medium |
| Power dynamics understood | Power scores assigned to 80%+ of stakeholders | Medium |
| Sentiment baseline established | Sentiment scores assigned to 80%+ of stakeholders | Medium |

### Process Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Core workflows mapped | 3+ Process records | Yes |
| Pain points identified | Process records with challenges linked | Yes |
| Current state documented | Descriptions populated | Medium |
| Handoffs mapped | Integration_Points or handoff notes present | Medium |
| Automation opportunities flagged | Automation_Level assessed | Yes |
| Compliance requirements known | Notes mention compliance/governance | Medium |
| Volume metrics captured | Frequency or volume in Description | Low |

### Technology Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Core systems inventoried | 5+ Technology records | Yes |
| Integration points mapped | Integration_Points field populated | Yes |
| Data flows documented | Data flow mentioned in notes | Medium |
| API availability assessed | API_Available field populated | Yes |
| Data quality evaluated | Data_Quality field populated | Medium |
| Technical debt identified | Notes mention debt, legacy, or issues | Medium |
| Security requirements known | Notes mention security or compliance | Medium |

### Challenge Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Business challenges documented | Challenge with Category = business-related | Yes |
| Operational challenges documented | Challenge with Category = Process | Yes |
| Technical challenges documented | Challenge with Category = Technology | Yes |
| People challenges documented | Challenge with Category = People | Medium |
| Impact quantified | Impact field populated | Yes |
| Root causes identified | Root_Cause field populated | Yes |
| Urgency assessed | Urgency field populated | Yes |

### Solution Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| AI opportunities identified | Solution with Category = AI | Medium |
| Integration opportunities identified | Solution with Category = Integration | Medium |
| Process improvements identified | Solution with Category = Process | Medium |
| Quick wins flagged | Solution with Effort = Low AND Impact = High | Yes |
| Feasibility assessed | Feasibility field populated | Yes |
| Dependencies mapped | Dependencies field populated | Medium |

---

## Scoring Coverage

### Dimension Scoring

For each dimension, calculate:

```
Raw Coverage = Items Verified / Total Items
Weighted Coverage = (Critical Items Verified / Critical Total) × 0.7 
                  + (Non-Critical Verified / Non-Critical Total) × 0.3
```

### Readiness Assessment

| Dimension | Min for "Ready" | Min for "Proceed with Caution" |
|-----------|-----------------|-------------------------------|
| People | 75% | 50% |
| Process | 70% | 50% |
| Technology | 70% | 50% |
| Challenges | 80% | 60% |
| Solutions | 60% | 40% |

**Overall Readiness Rules:**
- All critical items in People + Challenges = Minimum requirement
- 3 of 5 dimensions at "Ready" threshold = Can proceed
- Any dimension below "Proceed with Caution" = Blocking gap

---

## Output Format

```markdown
# Discovery Coverage Analysis: [Client Name]
Generated: [Date]
Sessions Analyzed: [Count]
Total Findings: [Count]

## Readiness Summary

**Overall Readiness: [X]%** — [Ready / Nearly Ready / Gaps Remain / Early Stage]

| Dimension | Coverage | Status |
|-----------|----------|--------|
| People | [X]% | [✅/⚠️/❌] |
| Process | [X]% | [✅/⚠️/❌] |
| Technology | [X]% | [✅/⚠️/❌] |
| Challenges | [X]% | [✅/⚠️/❌] |
| Solutions | [X]% | [✅/⚠️/❌] |

## Detailed Coverage

### People ([X]%)
| Item | Status | Evidence |
|------|--------|----------|
| Economic buyer identified | ✅ | [Name, Title] |
| Champion identified | ⚠️ | Potential: [Name], needs validation |
| ... | | |

### Process ([X]%)
[Same format]

### Technology ([X]%)
[Same format]

### Challenges ([X]%)
[Same format]

### Solutions ([X]%)
[Same format]

## Critical Gaps

### Blocking Gaps (Must Address)
1. **[Gap Name]**
   - Why critical: [Explanation]
   - How to fill: [Recommended session/question]
   - Who to ask: [Stakeholder suggestion]

### Important Gaps (Should Address)
1. **[Gap Name]**
   - Current state: [What we have]
   - What's missing: [Specific need]
   - Recommended action: [How to fill]

## Recommended Next Steps

1. **[Action 1]** — [Rationale]
2. **[Action 2]** — [Rationale]
3. **[Action 3]** — [Rationale]

## Sessions Recommended

| Session Type | Focus | Attendees | Duration |
|--------------|-------|-----------|----------|
| [Type] | [What to cover] | [Who to invite] | [Time] |
```

---

## Example Output

```markdown
# Discovery Coverage Analysis: Contemporary Energy Solutions
Generated: November 2025
Sessions Analyzed: 6
Total Findings: 47

## Readiness Summary

**Overall Readiness: 72%** — Nearly Ready

| Dimension | Coverage | Status |
|-----------|----------|--------|
| People | 87% | ✅ |
| Process | 71% | ⚠️ |
| Technology | 85% | ✅ |
| Challenges | 71% | ⚠️ |
| Solutions | 50% | ⚠️ |

## Detailed Coverage

### People (87%)
| Item | Status | Evidence |
|------|--------|----------|
| Economic buyer identified | ✅ | James Wilson, CEO |
| Champion identified | ✅ | Sarah Chen, VP Operations |
| Key influencers mapped | ✅ | 5 stakeholders with Power ≥ 7 |
| Potential blockers identified | ✅ | Tom Bradley (Skeptic), Mike R (concerns) |
| Technical decision makers found | ✅ | Mike Rodriguez, IT Director |
| End users represented | ⚠️ | Only 1 end-user in sessions |
| Power dynamics understood | ✅ | 10 of 12 stakeholders scored |
| Sentiment baseline established | ⚠️ | 8 of 12 stakeholders scored |

### Process (71%)
| Item | Status | Evidence |
|------|--------|----------|
| Core workflows mapped | ✅ | 4 processes documented |
| Pain points identified | ✅ | Pain points linked to 3 of 4 |
| Current state documented | ✅ | Descriptions complete |
| Handoffs mapped | ⚠️ | Partial — Operations only |
| Automation opportunities flagged | ✅ | Automation_Level on all records |
| Compliance requirements known | ❌ | Not discussed |
| Volume metrics captured | ⚠️ | 2 of 4 have metrics |

### Challenges (71%)
| Item | Status | Evidence |
|------|--------|----------|
| Business challenges documented | ✅ | 2 business challenges |
| Operational challenges documented | ✅ | 4 operational challenges |
| Technical challenges documented | ✅ | 3 technical challenges |
| People challenges documented | ⚠️ | 1 people challenge, likely more |
| Impact quantified | ⚠️ | 5 of 9 have impact |
| Root causes identified | ✅ | 7 of 9 have root cause |
| Urgency assessed | ⚠️ | 6 of 9 have urgency |

### Solutions (50%)
| Item | Status | Evidence |
|------|--------|----------|
| AI opportunities identified | ✅ | 2 AI solutions |
| Integration opportunities identified | ✅ | 1 integration solution |
| Process improvements identified | ❌ | None documented |
| Quick wins flagged | ⚠️ | Potential but not scored |
| Feasibility assessed | ⚠️ | 2 of 4 have feasibility |
| Dependencies mapped | ❌ | Not documented |

## Critical Gaps

### Blocking Gaps (Must Address)
1. **Solution feasibility and dependencies not assessed**
   - Why critical: Can't prioritize recommendations without feasibility
   - How to fill: Technical validation session
   - Who to ask: IT Director + VP Operations

2. **Process compliance requirements unknown**
   - Why critical: Solutions may hit regulatory blockers
   - How to fill: Add compliance questions to next session
   - Who to ask: CFO or Legal if available

### Important Gaps (Should Address)
1. **End-user representation limited**
   - Current state: Only 1 end-user perspective
   - What's missing: Day-to-day operational reality
   - Recommended action: Include 2-3 end users in validation session

2. **Change management challenges under-documented**
   - Current state: 1 people challenge logged
   - What's missing: Training needs, resistance patterns
   - Recommended action: Add change management questions

## Recommended Next Steps

1. **Technical Validation Session** — Assess solution feasibility with IT team
2. **Compliance Check** — 30-min call with CFO on regulatory requirements
3. **End-User Validation** — Include frontline staff in synthesis session

## Sessions Recommended

| Session Type | Focus | Attendees | Duration |
|--------------|-------|-----------|----------|
| Technical Deep Dive | Solution feasibility, dependencies | IT Director, Tech Lead | 90 min |
| Synthesis | Validate findings with broader group | VP Ops, 2-3 end users | 60 min |
```
