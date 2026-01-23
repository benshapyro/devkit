# Synthesis Reference

Analysis workflows for patterns, gaps, priorities, insights, and artifact generation.

## Table of Contents

- [Pattern Analysis](#pattern-analysis)
- [Gap Analysis](#gap-analysis)
- [Prioritizer](#prioritizer)
- [Insight Generator](#insight-generator)
- [Data to Artifact Generation](#data-to-artifact-generation)

---

# Pattern Analysis

Identify cross-cutting themes and recurring patterns across discovery findings.

## When to Use

User says something like:
- "What patterns do you see across our discovery sessions?"
- "Are there themes in the challenges we've identified?"
- "What keeps coming up?"
- "Any common threads?"

## Pattern Analysis Flow

### Step 1: Load All Client Data

Query Discovery Catalog:

```
Base ID: apprH2AppvnKfUpT0

Query each table filtered by Client:
- 1_Discovery_Log — Session history
- 2_People — Stakeholder findings
- 3_Process — Workflow findings
- 4_Technology — System findings
- 5_Challenges — Pain points
- 6_Solutions — Opportunities
```

### Step 2: Group by Dimension

| Dimension | Source Tables | What to Extract |
|-----------|---------------|-----------------|
| People | 2_People | Roles, archetypes, sentiment patterns |
| Process | 3_Process | Workflow types, automation levels, pain points |
| Technology | 4_Technology | System categories, integration gaps, data quality |
| Challenges | 5_Challenges | Categories, impact levels, root causes |
| Solutions | 6_Solutions | Categories, feasibility patterns |

### Step 3: Identify Patterns

For each dimension, look for:

**Frequency Patterns**
- What categories appear most often?
- Which teams/departments come up repeatedly?
- What systems are mentioned across sessions?

**Correlation Patterns**
- Do certain challenges cluster together?
- Are specific technologies tied to specific pain points?
- Do certain stakeholder archetypes correlate with blockers?

**Contradiction Patterns**
- Where do stakeholders disagree?
- What findings conflict with each other?
- Where is confidence low across multiple sources?

**Absence Patterns**
- What's notably missing?
- Which dimensions have sparse coverage?
- What questions weren't answered?

### Step 4: Score Pattern Strength

| Evidence Count | Strength Label | Confidence |
|----------------|----------------|------------|
| 1 mention | Anecdotal | Low — single source, may be outlier |
| 2-3 mentions | Emerging | Medium — worth noting, validate further |
| 4-6 mentions | Established | High — multiple sources, likely real |
| 7+ mentions | Dominant | Very High — pervasive theme, prioritize |

Calculate mentions across:
- Different sessions (temporal breadth)
- Different stakeholders (perspective breadth)
- Different dimensions (domain breadth)

## Pattern Types

### Type 1: Thematic Patterns
Recurring themes across multiple dimensions.

**Example:** "Manual workarounds" appears in:
- Process: Data entry done manually
- Technology: Systems don't integrate
- Challenges: Time wasted on repetitive tasks
- People: Team frustration with manual work

**Signal:** Cross-dimensional theme = high-value insight

### Type 2: Stakeholder Patterns
Common attitudes or behaviors across people.

**Example:** Technical staff sentiment pattern:
- 3 of 4 technical leads are Skeptics
- All cite "we've tried this before" concerns
- Low confidence in AI solutions

**Signal:** Stakeholder alignment (or misalignment) affects implementation

### Type 3: Technology Patterns
System and integration themes.

**Example:** Data silo pattern:
- 4 systems with no API integration
- Manual data transfer between departments
- Inconsistent data quality flagged in 3 sessions

**Signal:** Technical debt or architecture issues

### Type 4: Process Patterns
Workflow and operational themes.

**Example:** Approval bottleneck pattern:
- 3 processes require VP approval
- Average wait time: 2 weeks mentioned twice
- Workarounds exist but create compliance risk

**Signal:** Organizational structure impediments

### Type 5: Challenge Clusters
Related problems that form a system.

**Example:** Reporting pain cluster:
- Challenge A: Can't get real-time data
- Challenge B: Reports take 2 days to compile
- Challenge C: Executives make decisions on stale data
- Root cause: No unified data warehouse

**Signal:** Solving root cause addresses multiple symptoms

## Evidence Scoring

### Source Quality Weights

| Source Type | Weight | Rationale |
|-------------|--------|-----------|
| Direct quote from stakeholder | 1.0 | Explicit evidence |
| Paraphrased stakeholder statement | 0.8 | Interpreted evidence |
| Observed in process documentation | 0.9 | Verified evidence |
| Inferred from context | 0.5 | Indirect evidence |
| Single mention, no corroboration | 0.3 | Weak evidence |

### Confidence Calculation

```
Pattern Confidence = (Sum of weighted evidence) / (Number of sources × Max possible weight)
```

Report as:
- **High confidence (>0.7):** Strong evidence, act on it
- **Medium confidence (0.4-0.7):** Likely real, validate if critical
- **Low confidence (<0.4):** Preliminary, needs more discovery

## Pattern Output Format

```markdown
# Pattern Analysis: [Client Name]
Generated: [Date]
Data Sources: [X] sessions, [Y] stakeholders, [Z] findings

## Executive Summary
[2-3 sentence overview of dominant patterns]

## Dominant Patterns

### Pattern 1: [Name]
**Strength:** [Dominant/Established/Emerging]
**Confidence:** [High/Medium/Low]
**Dimensions Affected:** [List]

**Evidence:**
- [Source 1]: "[Quote or finding]"
- [Source 2]: "[Quote or finding]"

**Implication:** [What this means for strategy]

## Emerging Patterns (Needs Validation)
- [Pattern with 2-3 mentions, worth watching]

## Contradictions to Resolve
| Finding A | Finding B | Sources | Recommended Resolution |
|-----------|-----------|---------|------------------------|

## Recommendations
1. [Action based on dominant pattern]
2. [Validation needed for emerging pattern]
```

---

# Gap Analysis

Assess discovery coverage against the methodology checklist and identify what's missing.

## When to Use

User says something like:
- "What gaps remain in our discovery?"
- "Are we ready for strategy?"
- "What haven't we covered yet?"
- "Check our discovery coverage"

## Gap Analysis Flow

### Step 0: Pre-flight Check

Before analyzing gaps:
1. Load schema from `data-schema.md`
2. Get Client ID from 0_Clients table
3. Fetch Client Brain for context

### Step 1: Load Coverage Checklist

Reference the Discovery Coverage Checklist from prep.md:
- 5 dimensions, ~35 items total
- People Coverage (7 items)
- Process Coverage (7 items)
- Technology Coverage (7 items)
- Challenge Coverage (7 items)
- Solution Coverage (7 items)

### Step 2: Query Existing Findings

```
Base ID: apprH2AppvnKfUpT0

For each table, get counts and key attributes:
- 2_People: Count, Stakeholder Type distribution, ADKAR Stage distribution
- 3_Process: Count, Automation Level distribution, Frequency values
- 4_Technology: Count, Tool Type distribution, API Available counts
- 5_Challenges: Count, Problem Type distribution, Impact Score ranges
- 6_Solutions: Count, Solution Type distribution, Feasibility Score ranges
```

### Step 3: Map Findings to Checklist

| Status | Criteria |
|--------|----------|
| Covered | Finding exists with Medium+ confidence |
| Partial | Finding exists but Low confidence or incomplete |
| Missing | No relevant finding |
| Inferred | Can be derived from other findings |

### Step 4: Calculate Coverage Scores

**Dimension Score:**
```
Score = (Covered × 1.0 + Partial × 0.5 + Inferred × 0.3) / Total Items
```

**Readiness Assessment:**

| Readiness Score | Status | Recommendation |
|-----------------|--------|----------------|
| 90%+ | Ready | Proceed to synthesis/strategy |
| 70-89% | Nearly Ready | Address critical gaps, then proceed |
| 50-69% | Gaps Remain | 1-2 more discovery sessions recommended |
| <50% | Early Stage | Continue discovery phase |

## Verification Criteria

### People Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Economic buyer identified | Person with Role_Type = "Economic Buyer" | Yes |
| Champion identified | Person with Archetype = "Champion" | Yes |
| Key influencers mapped | 3+ people with Power >= 7 | Yes |
| Potential blockers identified | People with Sentiment <= 4 or Archetype = "Skeptic" | Yes |
| Technical decision makers found | Person with Role_Type = "Technical Lead" | Medium |
| End users represented | At least one end-user perspective | Medium |

### Process Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Core workflows mapped | 3+ Process records | Yes |
| Pain points identified | Process records with challenges linked | Yes |
| Automation opportunities flagged | Automation_Level assessed | Yes |
| Handoffs mapped | Integration_Points or handoff notes present | Medium |

### Technology Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Core systems inventoried | 5+ Technology records | Yes |
| Integration points mapped | Integration_Points field populated | Yes |
| API availability assessed | API_Available field populated | Yes |

### Challenge Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Business challenges documented | Challenge with Category = business-related | Yes |
| Operational challenges documented | Challenge with Category = Process | Yes |
| Impact quantified | Impact field populated | Yes |
| Root causes identified | Root_Cause field populated | Yes |

### Solution Dimension

| Item | How to Verify | Critical? |
|------|---------------|-----------|
| Quick wins flagged | Solution with Effort = Low AND Impact = High | Yes |
| Feasibility assessed | Feasibility field populated | Yes |

## Gap Output Format

```markdown
# Discovery Coverage Analysis: [Client Name]
Generated: [Date]

## Readiness Summary

**Overall Readiness: [X]%** — [Ready / Nearly Ready / Gaps Remain / Early Stage]

| Dimension | Coverage | Status |
|-----------|----------|--------|
| People | [X]% | [Status] |
| Process | [X]% | [Status] |
| Technology | [X]% | [Status] |
| Challenges | [X]% | [Status] |
| Solutions | [X]% | [Status] |

## Critical Gaps

### Blocking Gaps (Must Address)
1. **[Gap Name]**
   - Why critical: [Explanation]
   - How to fill: [Recommended session/question]
   - Who to ask: [Stakeholder suggestion]

## Recommended Next Steps
1. **[Action 1]** — [Rationale]
```

---

# Prioritizer

Score and rank challenges and solutions to guide strategic recommendations.

## When to Use

User says something like:
- "Prioritize the challenges we've found"
- "Rank solutions by impact"
- "What should we tackle first?"
- "Which opportunities are most valuable?"

## Prioritization Flow

### Step 1: Load Findings

Query Discovery Catalog:
```
Get all Challenges:
Table: 5_Challenges
Fields: Challenge Name, Problem Type, Impact Score, Urgency Score, DVF Score,
        Priority Score, Root Cause, Confidence

Get all Solutions:
Table: 6_Solutions
Fields: Solution Name, Solution Type, Impact Score, Feasibility Score, Effort Score,
        Risk Score, Reuse Score, Dependencies
```

### Step 2: Use Stored Priority Scores

**IMPORTANT:** Use pre-calculated scores from Airtable. Do NOT recalculate.

**Challenge Priority Score:**
```
Priority Score = Impact × Urgency × Readiness  (max 125)
```

**Solution DVF Score:**
```
DVF Score = Desirability × Viability × Feasibility  (max 125)
```

### Step 3: Apply Adjustments

**Confidence Adjustment:**
```
Adjusted Score = Raw Score × (Confidence / 5)
```

**Dependency Adjustment:**
- Solution depends on another solution: -0.5 to base score
- Challenge marked as Root Cause: +1 to base score
- Solution addresses 2+ challenges: +1 to base score

## Challenge Prioritization Matrix

| | Urgency 8-10 | Urgency 5-7 | Urgency 1-4 |
|-----|--------------|-------------|-------------|
| **Impact 8-10** | Critical | Important | Planned |
| **Impact 5-7** | Important | Planned | Backlog |
| **Impact 1-4** | Planned | Backlog | Monitor |

**Priority Score Thresholds (max 125):**
- Critical: Score >= 100
- Important: Score 64-99
- Planned: Score 27-63
- Backlog: Score 8-26
- Monitor: Score < 8

## Solution Prioritization Matrix

| | Feasibility 8-10 | Feasibility 5-7 | Feasibility 1-4 |
|-----|------------------|-----------------|-----------------|
| **Impact 8-10** | Quick Win | Strategic | Invest |
| **Impact 5-7** | Strategic | Consider | Question |
| **Impact 1-4** | Consider | Question | Deprioritize |

**DVF Score Thresholds:**
- Quick Win: DVF >= 64
- Strategic: DVF 40-63
- Consider: DVF 20-39
- Question: DVF 10-19
- Deprioritize: DVF < 10

## Quick Win Identification

A solution is a **Quick Win** if:
- Impact Score >= 8 AND Effort Score <= 4
- OR: Impact Score >= 8 AND Feasibility Score >= 8 AND Effort Score <= 6
- OR: DVF Score >= 64 AND no blocking dependencies

## Sequencing Rules

1. **Dependencies First** — If Solution B depends on Solution A, A must come first
2. **Quick Wins Early** — High-impact, low-effort items in Phase 1
3. **Root Causes Before Symptoms** — Solving root causes has multiplier effect
4. **Stakeholder Alignment** — Factor in champion support

## Tiebreaker Rules

When scores are equal:
1. Higher confidence wins
2. Fewer dependencies wins
3. More stakeholder support wins
4. Earlier discovery wins (more validated)

## Prioritizer Output Format

```markdown
# Prioritized Recommendations: [Client Name]
Generated: [Date]

## Executive Summary
[2-3 sentences on top priorities]

## Challenge Priority Ranking

### Critical (Address Immediately)
| Rank | Challenge | Impact | Urgency | Score | Root Cause |
|------|-----------|--------|---------|-------|------------|

### Important (Phase 1)
[Same format]

## Solution Priority Ranking

### Quick Wins (Start Here)
| Rank | Solution | Impact | Effort | Feasibility | DVF | Addresses |
|------|----------|--------|--------|-------------|-----|-----------|

### Strategic Initiatives (Phase 1-2)
[Same format]

## Recommended Sequence

### Phase 1: Quick Wins (Weeks 1-4)
| Week | Initiative | Owner | Success Metric |
|------|------------|-------|----------------|

## Dependencies Map
[Visual or text representation]

## Risk Factors
| Solution | Risk Score | Description | Mitigation |
```

---

# Insight Generator

Synthesize findings into executive-ready insights with supporting evidence.

## When to Use

User says something like:
- "What are the key insights from discovery?"
- "Summarize what we've learned"
- "What should we tell the executive sponsor?"
- "Give me the headlines"

## Insight Generation Flow

### Step 1: Run Supporting Analyses

Before generating insights, execute:
1. **Pattern Analysis** — Identify dominant themes
2. **Gap Analysis** — Assess coverage completeness
3. **Prioritization** — Rank challenges and solutions

### Step 2: Gather Evidence

| Source | What to Extract |
|--------|-----------------|
| Patterns | Dominant themes (strength >= Established) |
| Gaps | Critical gaps, readiness score |
| Prioritizer | Top 3 challenges, top 3 solutions |
| Raw findings | High-confidence items (>= 7) |
| Stakeholder data | Key players, sentiment summary |

### Step 3: Apply Quality Tests

**The "So What?" Test**
For each finding/pattern, ask: "So what does this mean for the client?"

**The "Now What?" Test**
For each insight candidate: "What action does this suggest?"

**The "Surprise" Test**
Which findings challenge assumptions or reveal something unexpected?

### Step 4: Filter and Prioritize

Keep insights that are:
- **Actionable** — Points to a clear next step
- **Evidenced** — Supported by 2+ sources
- **Significant** — Impacts business outcomes
- **Non-obvious** — Adds value beyond surface observations

## Insight Types

### Type 1: Situation Insight
Frames the current state and context.
**Template:** "[Client] is facing [situation] characterized by [key evidence]."

### Type 2: Problem Insight
Identifies a root cause or systemic issue.
**Template:** "The underlying cause of [symptoms] is [root cause], which manifests as [evidence]."

### Type 3: People Insight
Reveals stakeholder dynamics or organizational patterns.
**Template:** "[Stakeholder pattern] suggests [implication], requiring [approach]."

### Type 4: Opportunity Insight
Highlights potential value or possibility.
**Template:** "There's an opportunity to [outcome] by [approach], which could [quantified benefit]."

### Type 5: Risk Insight
Surfaces a concern or potential blocker.
**Template:** "[Risk factor] could [negative outcome] unless [mitigation]."

### Type 6: Readiness Insight
Assesses preparedness for next steps.
**Template:** "[Client] is [readiness level] for [next phase] because [evidence]."

### Type 7: Sequence Insight
Recommends order of operations.
**Template:** "The optimal sequence is [order] because [dependency/logic]."

## Insight Quality Scoring

| Score | Description |
|-------|-------------|
| 5 | Compelling, well-evidenced, actionable, non-obvious |
| 4 | Strong, well-evidenced, actionable |
| 3 | Solid, adequate evidence, somewhat actionable |
| 2 | Weak, limited evidence or generic |
| 1 | Obvious, no evidence, or not actionable |

Include only insights scoring 3+.

## Insight Anti-Patterns

| Anti-Pattern | Example | Problem |
|--------------|---------|---------|
| Too vague | "There are some challenges" | No specificity |
| No evidence | "They seem resistant" | Unsubstantiated |
| Obvious | "They use multiple systems" | Doesn't add value |
| No action | "Data quality varies" | So what? |
| Jargon-heavy | "Digital transformation synergies" | Empty buzzwords |

## Insights Output Format

```markdown
# Discovery Insights: [Client Name]
Generated: [Date]
Based on: [X] sessions, [Y] stakeholders, [Z] findings

## Executive Summary
[3-4 sentence narrative: situation, key finding, opportunity, recommended path]

## Key Insights

### 1. [Insight Headline]
[2-3 sentence insight in plain language]

**Evidence:**
- [Source/session]: [Supporting quote or finding]
- [Source/session]: [Supporting quote or finding]

**Implication:** [What this means / what to do]

---

[Continue for 5-7 insights total]

## The Path Forward

1. **Immediate (This Week):** [Action]
2. **Short-term (Next 30 Days):** [Action]
3. **Medium-term (60-90 Days):** [Action]

## Confidence Assessment

| Insight | Confidence | Notes |
|---------|------------|-------|
| [Headline] | High | [Why] |
| [Headline] | Medium | [What would increase confidence] |

## What We Still Don't Know
- [Open question 1]
- [Open question 2]
```

---

# Data to Artifact Generation

Generate branded client artifacts from Tech Stack Survey and Discovery Catalog Lite data.

## Overview

The artifact templates contain **example data** (Acme Corp) that renders correctly out of the box. To generate a client artifact:

1. **Load client data** from Excel or Airtable
2. **Read the template** to understand the structure
3. **Generate new HTML/JSX** with client data substituted
4. **Output as artifact** or save as file

**Key principle:** Don't try to find-and-replace in the template. Use the template as a **structural reference** and generate fresh HTML/JSX.

## Available Artifacts

| Artifact | Template | Data Source |
|----------|----------|-------------|
| Tech Stack Overview | `tech-stack-overview.html` | Tech Stack Survey Excel |
| Integration Map | `integration-map.jsx` | Tech Stack Survey Excel |
| Findings Summary | `findings-summary.html` | Discovery Catalog Lite Excel |

Templates location: `assets/artifact-templates/`

## Artifact 1: Tech Stack Overview

### Data Required

| Column | Field | Required? | Used For |
|--------|-------|-----------|----------|
| A | Tool/System Name | Yes | Tool name |
| C | Primary Department(s) | Yes | Department badges, spend grouping |
| D | Tool Owner/Champion | Yes | Detail row |
| E | # of Users | Yes | Detail row, cost per user |
| F | Annual Cost | Yes | Cost column, totals |
| G | Vendor/Provider | No | Vendor subtext |
| H | Has API? | Yes | API status, connectivity score |
| I | Upstream Tools | Yes | Possible integrations count |
| J | Downstream Tools | Yes | Possible integrations count |

### Key Calculations

**Connectivity Score:**
```
API Coverage = tools_with_api / total_tools
Connection Paths = tools_with_at_least_one_integration / total_tools
Isolated = tools with no API AND no connections
```

**Spend by Department:** Group Annual Cost by Primary Department(s)

**Cost per User Outliers:** Annual Cost / # of Users, sorted for highest and lowest

### What NOT to Include

| Removed | Reason |
|---------|--------|
| Health status (green/yellow/red) | No clear calculation |
| Spend by Category | Would require inferring category |
| Recommendations | Requires judgment, not data |
| "X connected" language | We know possible connections, not actual |

## Artifact 2: Integration Map

### Data Required

| Column | Field | Used For |
|--------|-------|----------|
| A | Tool/System Name | Node label |
| B | Purpose | Category inference |
| I | Upstream Tools | Incoming connections |
| J | Downstream Tools | Outgoing connections |
| K | Connection Method | Line style |

### Category Inference

```python
CATEGORY_KEYWORDS = {
    'crm': ['crm', 'salesforce', 'hubspot', 'customer', 'lead'],
    'communication': ['slack', 'teams', 'email', 'chat', 'zoom'],
    'finance': ['quickbooks', 'xero', 'stripe', 'accounting'],
    'automation': ['zapier', 'make', 'n8n', 'automate'],
    'storage': ['drive', 'dropbox', 'box', 'storage', 'file'],
    'project': ['asana', 'monday', 'jira', 'trello', 'project'],
    'analytics': ['tableau', 'looker', 'analytics', 'report', 'bi'],
}
```

### Connection Methods

| Method | Style |
|--------|-------|
| native | Solid blue line |
| api | Dashed blue line |
| ipaas | Dotted purple line |
| manual | Dashed gray line |

## Artifact 3: Findings Summary

### Data Required

**Issues sheet (2_Issues):**
- Department, Issue Name, Description, Impact Category, Solution Name (link), Pain Point Quote

**Solutions sheet (3_Solutions):**
- Department, Solution Name, Description, Impact, Effort

### Key Logic

**Impact Levels:**
- High: Time Efficiency, Revenue Loss, New Revenue, Customer Experience
- Medium: Competitive Position, Lead Quality, Cost Reduction
- Low: Everything else

**Quick Win Identification:**
Quick win = Low effort solution that addresses high-impact issue

## CSS Class Reference

### API Status
```css
.api-dot.yes { background: var(--status-green); }
.api-dot.no { background: var(--status-red); }
.api-dot.unknown { background: var(--status-yellow); }
```

### Department Badges
```css
.dept-badge.sales { background: #fef3c7; color: #92400e; }
.dept-badge.marketing { background: #fce7f3; color: #9d174d; }
.dept-badge.finance { background: #d1fae5; color: #065f46; }
.dept-badge.engineering { background: #dbeafe; color: #1e40af; }
.dept-badge.operations { background: #e0e7ff; color: #3730a3; }
.dept-badge.all { background: var(--cadre-black); color: var(--cadre-white); }
```

### Impact/Effort Badges
```css
.badge.impact-high { background: #fee2e2; color: #991b1b; }
.badge.impact-medium { background: #fef3c7; color: #92400e; }
.badge.impact-low { background: #f1f5f9; color: #475569; }

.badge.effort-low { background: #d1fae5; color: #065f46; }
.badge.effort-medium { background: #fef3c7; color: #92400e; }
.badge.effort-high { background: #fee2e2; color: #991b1b; }
```

## Error Handling

| Situation | Action |
|-----------|--------|
| Missing tool name | Skip row |
| Missing cost | Display "—" or "Unknown" |
| No API info | Default to "Unknown" |
| Empty department | Use "Unassigned" |
| No connections | Show tool as isolated node |
| No quick wins | Hide section or show "None identified" |

## Template Reference

View the example-data templates to understand exact HTML structure:
- `assets/artifact-templates/tech-stack-overview.html`
- `assets/artifact-templates/integration-map.jsx`
- `assets/artifact-templates/findings-summary.html`

Copy structural patterns (CSS classes, HTML nesting, section order) when generating client artifacts.
