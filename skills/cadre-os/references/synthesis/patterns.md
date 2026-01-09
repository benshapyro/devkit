# Pattern Analysis

Identify cross-cutting themes and recurring patterns across discovery findings.

## Contents

1. [When to Use](#when-to-use)
2. [Execution Flow](#execution-flow)
3. [Pattern Types](#pattern-types)
4. [Evidence Scoring](#evidence-scoring)
5. [Output Format](#output-format)
6. [Example Output](#example-output)

---

## When to Use

User says something like:
- "What patterns do you see across our discovery sessions?"
- "Are there themes in the challenges we've identified?"
- "What keeps coming up?"
- "Any common threads?"

---

## Execution Flow

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

Organize findings into the five dimensions:

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

For each identified pattern:

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

### Step 5: Generate Pattern Report

---

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

---

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

---

## Output Format

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
- [Source 3]: "[Quote or finding]"

**Implication:** [What this means for strategy]

### Pattern 2: [Name]
[Same structure]

## Emerging Patterns (Needs Validation)
- [Pattern with 2-3 mentions, worth watching]
- [Pattern with 2-3 mentions, worth watching]

## Contradictions to Resolve
| Finding A | Finding B | Sources | Recommended Resolution |
|-----------|-----------|---------|------------------------|
| [Statement] | [Conflicting statement] | [Who said each] | [How to resolve] |

## Gaps in Pattern Analysis
- [Dimension or area with insufficient data]
- [Questions that remain unanswered]

## Recommendations
1. [Action based on dominant pattern]
2. [Validation needed for emerging pattern]
3. [Session recommended to resolve contradiction]
```

---

## Example Output

```markdown
# Pattern Analysis: Contemporary Energy Solutions
Generated: November 2025
Data Sources: 6 sessions, 12 stakeholders, 47 findings

## Executive Summary
Three dominant patterns emerged: pervasive manual data handling, stakeholder skepticism rooted in past failed initiatives, and siloed systems preventing cross-functional visibility. These patterns suggest a phased approach starting with quick wins to build trust before larger integration efforts.

## Dominant Patterns

### Pattern 1: Manual Data Handling Epidemic
**Strength:** Dominant (8 mentions)
**Confidence:** High
**Dimensions Affected:** Process, Technology, Challenges

**Evidence:**
- Sarah Chen (VP Ops): "We have people whose entire job is copying data between spreadsheets"
- Mike Rodriguez (IT Director): "No API connections between our core systems"
- Process mapping: 4 of 6 workflows include manual data entry steps
- Challenge log: 3 separate "time wasted on data entry" items

**Implication:** Automation opportunities are significant, but require integration infrastructure first.

### Pattern 2: Initiative Fatigue / Past Failure Shadow
**Strength:** Established (5 mentions)
**Confidence:** High
**Dimensions Affected:** People, Challenges

**Evidence:**
- 3 of 4 technical leads classified as Skeptic archetype
- Tom Bradley: "We tried an AI vendor two years ago, total disaster"
- Multiple mentions of "proof first, then scale" preference
- Low sentiment scores (avg 4.2) among technical staff

**Implication:** Must demonstrate quick wins before proposing large changes. Reference past failures explicitly and show what's different.

### Pattern 3: Departmental Data Silos
**Strength:** Established (4 mentions)
**Confidence:** Medium
**Dimensions Affected:** Technology, Process

**Evidence:**
- 4 core systems with no integration (ERP, CRM, custom tools)
- Operations and Sales using different data for same metrics
- CFO cited "can't get a single source of truth" as top frustration

**Implication:** Data integration/warehouse should be part of solution architecture.

## Emerging Patterns (Needs Validation)
- **Change management gap:** Training mentioned as concern in 2 sessions, but no formal change management process identified
- **Executive alignment uncertainty:** CEO and COO may have different priorities (mentioned once, low confidence)

## Contradictions to Resolve
| Finding A | Finding B | Sources | Recommended Resolution |
|-----------|-----------|---------|------------------------|
| "IT team is understaffed" | "We have budget for new hires" | IT Dir vs CFO | Clarify hiring timeline and constraints |
| "Ready to move fast" | "Need extensive piloting" | CEO vs VP Ops | Align on pilot scope in next session |

## Recommendations
1. **Address skepticism first:** Plan pilot project with measurable ROI in <30 days
2. **Validate executive alignment:** Schedule synthesis session with CEO + COO together
3. **Map integration requirements:** Technical deep-dive on API/data architecture
```
