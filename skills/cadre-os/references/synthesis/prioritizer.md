# Prioritizer

Score and rank challenges and solutions to guide strategic recommendations.

## Contents

1. [When to Use](#when-to-use)
2. [Execution Flow](#execution-flow)
3. [Scoring Framework](#scoring-framework)
4. [Prioritization Logic](#prioritization-logic)
5. [Output Format](#output-format)
6. [Example Output](#example-output)

---

## When to Use

User says something like:
- "Prioritize the challenges we've found"
- "Rank solutions by impact"
- "What should we tackle first?"
- "Which opportunities are most valuable?"
- "Help me sequence the recommendations"

---

## Execution Flow

### Step 0: Pre-flight Check

Before prioritizing, complete the Pre-flight Check from SKILL.md:
1. Load schema from `references/data/discovery-catalog.md`
2. Get Client ID from 0_Clients table
3. Fetch Client Brain for context (stakeholder dynamics, preferences)

### Step 1: Load Findings

Query Discovery Catalog. Schema already loaded in Pre-flight Check.
Quick reference: `references/data/discovery-catalog.md`

```
Base ID: apprH2AppvnKfUpT0

Get all Challenges:
Table: 5_Challenges (tblmGPfC8Y85laT6j)
Filter: {Client} = "[Client Name]"
Fields: Challenge Name, Problem Type, Impact Score, Urgency Score, DVF Score, 
        Priority Score, Root Cause, Confidence, 6_Solutions

Get all Solutions:
Table: 6_Solutions (tblleK2rzvC5V7sR0)
Filter: {Client} = "[Client Name]"
Fields: Solution Name, Solution Type, Impact Score, Feasibility Score, Effort Score,
        Risk Score, Reuse Score, Dependencies, 5_Challenges
```

### Step 2: Use Numeric Scores

The schema uses 1-10 numeric scales (no conversion needed):

| Field | Scale | Interpretation |
|-------|-------|----------------|
| Impact Score | 1-10 | 8-10 = High, 5-7 = Medium, 1-4 = Low |
| Urgency Score | 1-10 | 8-10 = High, 5-7 = Medium, 1-4 = Low |
| Feasibility Score | 1-10 | 8-10 = High, 5-7 = Medium, 1-4 = Low |
| Effort Score | 1-10 | 8-10 = High effort, 1-4 = Low effort |
| Risk Score | 1-10 | Higher = riskier |
| DVF Score | 1-100 | Pre-calculated Desirability × Viability × Feasibility |

**Note:** If scores are missing, use defaults: Impact=5, Urgency=5, Feasibility=5, Effort=5, Risk=3

### Step 3: Use Stored Priority Scores

**IMPORTANT:** Use pre-calculated scores from Airtable. Do NOT recalculate.

**Challenge Priority Score** (from `Priority Score` field):
```
Priority Score = Impact × Urgency × Readiness  (max 125)
```
This score is calculated when the record is created. Use it directly for ranking.

**Solution DVF Score** (from `DVF Score` field):
```
DVF Score = Desirability × Viability × Feasibility  (max 125)
```
This score is calculated when the record is created. Use it directly for ranking.

**Why use stored scores:**
- Consistency between Airtable views and synthesis outputs
- Avoids ranking discrepancies (Airtable shows A > B, synthesis shows B > A)
- Single source of truth for prioritization

**Fallback (only if stored scores missing):**
```
Challenge: (Impact × 0.4) + (Urgency × 0.3) + (Readiness × 0.3) × 25
Solution: (Desirability × 0.4) + (Viability × 0.3) + (Feasibility × 0.3) × 25
```

### Step 4: Apply Adjustments

**Confidence Adjustment:**
```
Adjusted Score = Raw Score × (Confidence / 5)
```
Note: Confidence field uses 1-5 scale ("1 - Low" to "5 - High")

**Dependency Adjustment:**
- Solution depends on another solution: -0.5 to base score
- Challenge marked as Root Cause: +1 to base score
- Solution addresses 2+ challenges: +1 to base score
- Solution has high Reuse Score (≥7): +0.5 to base score

### Step 5: Rank and Categorize

---

## Scoring Framework

### Challenge Prioritization Matrix

Using Impact Score (1-10) and Urgency Score (1-10):

| | Urgency 8-10 | Urgency 5-7 | Urgency 1-4 |
|-----|--------------|-------------|-------------|
| **Impact 8-10** | 🔴 Critical | 🟠 Important | 🟡 Planned |
| **Impact 5-7** | 🟠 Important | 🟡 Planned | 🟢 Backlog |
| **Impact 1-4** | 🟡 Planned | 🟢 Backlog | ⚪ Monitor |

**Priority Score Thresholds (using stored scores, max 125):**
- 🔴 Critical: Score ≥ 100 (e.g., 5×5×4 = 100)
- 🟠 Important: Score 64-99 (e.g., 4×4×4 = 64)
- 🟡 Planned: Score 27-63 (e.g., 3×3×3 = 27)
- 🟢 Backlog: Score 8-26 (e.g., 2×2×2 = 8)
- ⚪ Monitor: Score < 8

### Solution Prioritization Matrix

Using Impact Score (1-10) and Feasibility Score (1-10):

| | Feasibility 8-10 | Feasibility 5-7 | Feasibility 1-4 |
|-----|------------------|-----------------|-----------------|
| **Impact 8-10** | 🌟 Quick Win | 🎯 Strategic | 🔬 Invest |
| **Impact 5-7** | 🎯 Strategic | 📋 Consider | ❓ Question |
| **Impact 1-4** | 📋 Consider | ❓ Question | ❌ Deprioritize |

**DVF Score Thresholds (if using pre-calculated):**
- 🌟 Quick Win: DVF ≥ 64
- 🎯 Strategic: DVF 40-63
- 📋 Consider: DVF 20-39
- ❓ Question: DVF 10-19
- ❌ Deprioritize: DVF < 10

### Quick Win Identification

A solution is a **Quick Win** if:
- Impact Score ≥ 8 AND Effort Score ≤ 4
- OR: Impact Score ≥ 8 AND Feasibility Score ≥ 8 AND Effort Score ≤ 6
- OR: DVF Score ≥ 64 AND no blocking dependencies

### Strategic Bet Identification

A solution is a **Strategic Bet** if:
- Impact Score ≥ 8 AND Effort Score ≥ 7 AND Feasibility Score ≥ 5
- Addresses 2+ challenges (check 5_Challenges link count)
- Aligns with stated business priorities

---

## Prioritization Logic

### Sequencing Rules

1. **Dependencies First**
   - If Solution B depends on Solution A, A must come first
   - Map dependency chains before final ranking

2. **Quick Wins Early**
   - Schedule high-impact, low-effort items in Phase 1
   - Build credibility before larger investments

3. **Root Causes Before Symptoms**
   - If Challenge X causes Challenges Y and Z, prioritize X
   - Solving root causes has multiplier effect

4. **Stakeholder Alignment**
   - Factor in champion support for solution
   - Deprioritize if key blocker opposes without mitigation plan

### Tiebreaker Rules

When scores are equal:
1. Higher confidence wins
2. Fewer dependencies wins
3. More stakeholder support wins
4. Earlier discovery wins (more validated)

---

## Output Format

```markdown
# Prioritized Recommendations: [Client Name]
Generated: [Date]
Challenges Analyzed: [Count]
Solutions Analyzed: [Count]

## Executive Summary
[2-3 sentences on top priorities and recommended approach]

## Challenge Priority Ranking

### 🔴 Critical (Address Immediately)
| Rank | Challenge Name | Impact | Urgency | Score | Root Cause |
|------|----------------|--------|---------|-------|------------|
| 1 | [Name] | [1-10] | [1-10] | [X.X] | [✓/—] |

### 🟠 Important (Address in Phase 1)
[Same format]

### 🟡 Planned (Address in Phase 2)
[Same format]

### 🟢 Backlog (Future Consideration)
[Same format]

## Solution Priority Ranking

### 🌟 Quick Wins (Start Here)
| Rank | Solution Name | Impact | Effort | Feasibility | DVF | Addresses |
|------|---------------|--------|--------|-------------|-----|-----------|
| 1 | [Name] | [1-10] | [1-10] | [1-10] | [X] | [Challenge Names] |

### 🎯 Strategic Initiatives (Phase 1-2)
[Same format]

### 📋 Consider (Evaluate Further)
[Same format]

### ❓ Needs Validation
[Same format]

## Recommended Sequence

### Phase 1: Quick Wins (Weeks 1-4)
| Week | Initiative | Owner | Success Metric |
|------|------------|-------|----------------|
| 1-2 | [Solution Name] | [Suggested] | [Metric] |
| 3-4 | [Solution Name] | [Suggested] | [Metric] |

### Phase 2: Strategic (Months 2-3)
[Same format]

### Phase 3: Transformation (Months 4-6)
[Same format]

## Dependencies Map

```
[Solution A] 
    ↓ enables
[Solution B] ──depends on──→ [Solution C]
    ↓ enables
[Solution D]
```

## Risk Factors
| Solution Name | Risk Score | Risk Description | Mitigation |
|---------------|------------|------------------|------------|
| [Name] | [1-10] | [Description] | [Approach] |

## Scoring Notes
- Confidence-adjusted scores used where Confidence < 4
- [X] solutions have dependency penalties applied
- [Y] challenges marked as Root Cause (score boosted)
- DVF Scores used where available (pre-calculated in Catalog)
```

---

## Example Output

```markdown
# Prioritized Recommendations: Contemporary Energy Solutions
Generated: November 2025
Challenges Analyzed: 9
Solutions Analyzed: 4

## Executive Summary
The highest-priority challenge is manual data handling (Impact 9, Urgency 9), which cascades into multiple other pain points. We recommend starting with automated reporting (Quick Win, DVF 72) to build credibility, then tackling the system integration as a strategic Phase 2 initiative.

## Challenge Priority Ranking

### 🔴 Critical (Address Immediately)
| Rank | Challenge Name | Impact | Urgency | Score | Root Cause |
|------|----------------|--------|---------|-------|------------|
| 1 | Manual data entry consuming 20+ hrs/week | 9 | 9 | 8.7 | ✓ |
| 2 | No real-time visibility into operations | 9 | 8 | 8.1 | — |

### 🟠 Important (Address in Phase 1)
| Rank | Challenge Name | Impact | Urgency | Score | Root Cause |
|------|----------------|--------|---------|-------|------------|
| 3 | Reports take 2 days to compile | 8 | 7 | 7.2 | — |
| 4 | Data inconsistency across departments | 7 | 8 | 7.0 | — |
| 5 | Executives making decisions on stale data | 8 | 6 | 6.5 | — |

### 🟡 Planned (Address in Phase 2)
| Rank | Challenge Name | Impact | Urgency | Score | Root Cause |
|------|----------------|--------|---------|-------|------------|
| 6 | Training gaps on existing systems | 6 | 5 | 5.2 | — |
| 7 | No change management process | 5 | 4 | 4.3 | — |

### 🟢 Backlog (Future Consideration)
| Rank | Challenge Name | Impact | Urgency | Score | Root Cause |
|------|----------------|--------|---------|-------|------------|
| 8 | Mobile access limitations | 4 | 3 | 3.2 | — |
| 9 | Legacy system UI complaints | 3 | 3 | 2.8 | — |

## Solution Priority Ranking

### 🌟 Quick Wins (Start Here)
| Rank | Solution Name | Impact | Effort | Feasibility | DVF | Addresses |
|------|---------------|--------|--------|-------------|-----|-----------|
| 1 | Automated daily reporting dashboard | 9 | 3 | 9 | 72 | Reports slow, Stale data |
| 2 | Data validation rules in ERP | 7 | 3 | 8 | 56 | Data inconsistency |

### 🎯 Strategic Initiatives (Phase 1-2)
| Rank | Solution Name | Impact | Effort | Feasibility | DVF | Addresses |
|------|---------------|--------|--------|-------------|-----|-----------|
| 3 | Integration layer between ERP/CRM | 9 | 8 | 6 | 48 | Manual entry, No visibility, Data inconsistency |

### 📋 Consider (Evaluate Further)
| Rank | Solution Name | Impact | Effort | Feasibility | DVF | Addresses |
|------|---------------|--------|--------|-------------|-----|-----------|
| 4 | AI-powered data entry assistant | 8 | 6 | 5 | 32 | Manual data entry |

## Recommended Sequence

### Phase 1: Quick Wins (Weeks 1-4)
| Week | Initiative | Owner | Success Metric |
|------|------------|-------|----------------|
| 1-2 | Automated daily reporting dashboard | IT + Ops | Reports delivered same-day |
| 3-4 | Data validation rules in ERP | IT | 50% reduction in data errors |

### Phase 2: Strategic (Months 2-3)
| Month | Initiative | Owner | Success Metric |
|-------|------------|-------|----------------|
| 2 | Integration layer design | IT | Architecture approved |
| 3 | Integration layer Phase 1 | IT + Vendor | ERP-CRM connected |

### Phase 3: Transformation (Months 4-6)
| Month | Initiative | Owner | Success Metric |
|-------|------------|-------|----------------|
| 4-5 | Full integration deployment | IT | All systems connected |
| 6 | AI data entry pilot | IT + Ops | 30% time reduction |

## Dependencies Map

```
[Data validation rules] 
    ↓ enables clean data for
[Integration layer] 
    ↓ enables real-time data for
[Automated reporting dashboard] ←── can start in parallel
    ↓ builds foundation for
[AI data entry assistant]
```

## Risk Factors
| Solution Name | Risk Score | Risk Description | Mitigation |
|---------------|------------|------------------|------------|
| Integration layer | 7 | IT team bandwidth constrained | Phase implementation, consider contractor |
| AI data entry | 6 | Staff skepticism from past failure | Extensive pilot, involve skeptics |

## Scoring Notes
- Challenge 1 marked as Root Cause (+1 boost) — causes challenges 2, 3, 5
- Solution 3 has dependency penalty (-0.5) — needs validation rules first
- Solution 4 confidence-adjusted (×0.8) due to Feasibility uncertainty
- DVF Scores pulled from Catalog where available
```
