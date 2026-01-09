# Insight Generator

Synthesize findings into executive-ready insights with supporting evidence.

## Contents

1. [When to Use](#when-to-use)
2. [Execution Flow](#execution-flow)
3. [Insight Types](#insight-types)
4. [Quality Criteria](#quality-criteria)
5. [Output Format](#output-format)
6. [Example Output](#example-output)

---

## When to Use

User says something like:
- "What are the key insights from discovery?"
- "Summarize what we've learned"
- "What should we tell the executive sponsor?"
- "Give me the headlines"
- "What's the story here?"

---

## Execution Flow

### Step 1: Run Supporting Analyses

Before generating insights, execute:

1. **Pattern Analysis** (see patterns.md)
   - Identify dominant themes
   - Surface contradictions

2. **Gap Analysis** (see gaps.md)
   - Assess coverage completeness
   - Note missing information

3. **Prioritization** (see prioritizer.md)
   - Rank challenges and solutions
   - Identify quick wins

### Step 2: Gather Evidence

From each analysis, extract:

| Source | What to Extract |
|--------|-----------------|
| Patterns | Dominant themes (strength ≥ Established) |
| Gaps | Critical gaps, readiness score |
| Prioritizer | Top 3 challenges, top 3 solutions |
| Raw findings | High-confidence items (≥7) |
| Stakeholder data | Key players, sentiment summary |

### Step 3: Identify Insight Candidates

Generate insight candidates by asking:

**The "So What?" Test**
For each finding/pattern, ask: "So what does this mean for the client?"

**The "Now What?" Test**  
For each insight candidate: "What action does this suggest?"

**The "Surprise" Test**
Which findings challenge assumptions or reveal something unexpected?

### Step 4: Filter and Prioritize Insights

Keep insights that are:
- **Actionable** — Points to a clear next step
- **Evidenced** — Supported by 2+ sources
- **Significant** — Impacts business outcomes
- **Non-obvious** — Adds value beyond surface observations

Discard insights that are:
- Obvious to anyone who read the session notes
- Not actionable
- Based on single low-confidence source
- Too generic to be useful

### Step 5: Structure the Narrative

Organize 5-7 insights into a coherent story:

```
Opening: The situation (1 insight)
    ↓
Core findings: What we discovered (3-4 insights)
    ↓
Opportunity: What's possible (1-2 insights)
    ↓
Implication: What to do next (woven throughout)
```

---

## Insight Types

### Type 1: Situation Insight
Frames the current state and context.

**Template:** "[Client] is facing [situation] characterized by [key evidence]."

**Example:** "CES is experiencing operational friction driven by disconnected systems, with 4 core platforms operating in silos."

### Type 2: Problem Insight
Identifies a root cause or systemic issue.

**Template:** "The underlying cause of [symptoms] is [root cause], which manifests as [evidence]."

**Example:** "Multiple reported pain points—slow reporting, data inconsistency, manual workarounds—trace back to a single root cause: no integration layer between core systems."

### Type 3: People Insight
Reveals stakeholder dynamics or organizational patterns.

**Template:** "[Stakeholder pattern] suggests [implication], requiring [approach]."

**Example:** "Technical staff skepticism, rooted in a failed AI initiative 2 years ago, means any solution must demonstrate quick wins before scaling."

### Type 4: Opportunity Insight
Highlights potential value or possibility.

**Template:** "There's an opportunity to [outcome] by [approach], which could [quantified benefit]."

**Example:** "Automating the current manual reporting process could recover 20+ hours per week while enabling real-time decision making."

### Type 5: Risk Insight
Surfaces a concern or potential blocker.

**Template:** "[Risk factor] could [negative outcome] unless [mitigation]."

**Example:** "Executive misalignment on pace vs. thoroughness could stall implementation unless addressed in the next session."

### Type 6: Readiness Insight
Assesses preparedness for next steps.

**Template:** "[Client] is [readiness level] for [next phase] because [evidence]. [Gap/strength] should be addressed first."

**Example:** "CES is nearly ready for strategy development, with strong stakeholder mapping and challenge documentation, though solution feasibility needs validation."

### Type 7: Sequence Insight
Recommends order of operations.

**Template:** "The optimal sequence is [order] because [dependency/logic]."

**Example:** "Quick wins in reporting should precede integration work—this builds credibility with skeptical technical staff and demonstrates ROI before larger investments."

---

## Quality Criteria

### Good Insight Characteristics

| Criterion | Test Question |
|-----------|---------------|
| Specific | Does it name specific people, systems, or numbers? |
| Evidenced | Can I point to 2+ sources that support this? |
| Actionable | Does it suggest what to do next? |
| Insightful | Would the client say "I hadn't thought of it that way"? |
| Connected | Does it link to other findings? |

### Insight Quality Scoring

Rate each candidate insight:

| Score | Description |
|-------|-------------|
| 5 | Compelling, well-evidenced, actionable, non-obvious |
| 4 | Strong, well-evidenced, actionable |
| 3 | Solid, adequate evidence, somewhat actionable |
| 2 | Weak, limited evidence or generic |
| 1 | Obvious, no evidence, or not actionable |

Include only insights scoring 3+.

### Common Insight Anti-Patterns

| Anti-Pattern | Example | Problem |
|--------------|---------|---------|
| Too vague | "There are some challenges" | No specificity |
| No evidence | "They seem resistant" | Unsubstantiated |
| Obvious | "They use multiple systems" | Doesn't add value |
| No action | "Data quality varies" | So what? |
| Jargon-heavy | "Digital transformation synergies" | Empty buzzwords |

---

## Output Format

```markdown
# Discovery Insights: [Client Name]
Generated: [Date]
Based on: [X] sessions, [Y] stakeholders, [Z] findings

## Executive Summary

[3-4 sentence narrative that tells the story: situation, key finding, opportunity, recommended path]

## Key Insights

### 1. [Insight Headline]
[2-3 sentence insight in plain language]

**Evidence:**
- [Source/session]: [Supporting quote or finding]
- [Source/session]: [Supporting quote or finding]

**Implication:** [What this means / what to do]

---

### 2. [Insight Headline]
[Same structure]

---

### 3. [Insight Headline]
[Same structure]

---

[Continue for 5-7 insights total]

## The Path Forward

Based on these insights, we recommend:

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
- [Open question 3]
```

---

## Example Output

```markdown
# Discovery Insights: Contemporary Energy Solutions
Generated: November 2025
Based on: 6 sessions, 12 stakeholders, 47 findings

## Executive Summary

CES is experiencing significant operational drag from disconnected systems and manual processes, costing an estimated 20+ hours per week in productivity. However, strong executive sponsorship and a clear champion in Sarah Chen create favorable conditions for transformation. The path forward should start with quick wins in reporting automation to build credibility with skeptical technical staff, then progress to strategic integration work. A phased approach addressing past initiative failures head-on will be critical to success.

## Key Insights

### 1. Manual Data Handling is the Root Cause of Multiple Pain Points

Four seemingly separate challenges—slow reporting, data inconsistency, executive frustration with stale data, and team time pressure—all trace back to a single root cause: no integration between core systems forces manual data transfer at every handoff.

**Evidence:**
- Sarah Chen (VP Ops): "We have people whose entire job is copying data between spreadsheets"
- Mike Rodriguez (IT): "Our ERP, CRM, and analytics tools have never talked to each other"
- Process mapping: 4 of 6 core workflows include manual data re-entry steps
- Estimated 20+ hours/week spent on manual data handling

**Implication:** Solving integration addresses multiple symptoms simultaneously. However, integration is a significant undertaking—start with automated reporting as proof of concept.

---

### 2. Past Failure Creates Present Skepticism

Technical staff resistance isn't irrational stubbornness—it's learned caution from a failed AI vendor engagement 2 years ago that promised much and delivered little. This skepticism must be addressed directly, not dismissed.

**Evidence:**
- Tom Bradley: "We tried an AI vendor two years ago, total disaster"
- 3 of 4 technical leads classified as Skeptic archetype
- Average technical staff sentiment: 4.2/10 (below neutral)
- Multiple unprompted mentions of "show me proof first"

**Implication:** Any solution must include a pilot phase with measurable outcomes before scaling. Involving skeptics in pilot design converts them from blockers to validators.

---

### 3. Strong Executive Sponsorship, But Alignment Needed

CEO James Wilson and COO Maria Santos are both supportive, but initial signals suggest different expectations on pace. Wilson mentioned "moving fast" while Santos emphasized "thorough piloting." This isn't a blocker yet, but could become one.

**Evidence:**
- Wilson: "We're ready to move fast on this"
- Santos: "I want to see extensive piloting before we commit"
- Both rated as Champions, but no joint session yet conducted

**Implication:** A synthesis session with both executives together should align on pilot scope and timeline before strategy presentation.

---

### 4. There's a Clear Quick Win in Automated Reporting

The daily reporting process—currently taking 2 days and producing stale data—can be automated with existing tools and delivered within 2 weeks. This is high-impact, low-effort, and addresses executive frustration directly.

**Evidence:**
- CFO: "I'm making decisions on data that's already outdated"
- Current report compilation: manual Excel work across 3 systems
- IT confirmed API access available for all data sources
- Similar automation at peer company took 10 days to implement

**Implication:** Start here. Quick win builds credibility, demonstrates ROI, and creates momentum for larger integration project.

---

### 5. Champion in Place, but End-User Voices Missing

Sarah Chen is an ideal champion—operational authority, executive access, genuinely frustrated with status quo. However, discovery has been top-heavy: only 1 of 12 stakeholders is a frontline end-user. We may be missing critical implementation reality.

**Evidence:**
- Sarah Chen: Power 9/10, Sentiment 9/10, actively volunteering resources
- Session attendance: 8 director+, 3 managers, 1 end-user
- Process documentation lacks daily workflow detail

**Implication:** Include 2-3 end-users in validation session to ground-truth operational assumptions before finalizing recommendations.

---

### 6. Solution Feasibility Needs Technical Validation

We've identified 4 potential solutions, but only 2 have confirmed feasibility assessments. The integration layer—the strategic centerpiece—is rated "Medium" feasibility without technical deep-dive.

**Evidence:**
- 2 of 4 solutions lack feasibility rating
- Integration layer dependencies not fully mapped
- IT Director flagged "bandwidth concerns" in passing

**Implication:** Technical validation session required before strategy presentation. Must confirm IT capacity and timeline reality.

---

### 7. The Optimal Sequence is Quick Win → Integration → AI

Dependencies and organizational dynamics suggest a clear sequence: automated reporting first (builds trust, quick ROI), integration layer second (enables data flow), AI-assisted data entry third (requires clean integrated data and skeptic buy-in).

**Evidence:**
- Dependency mapping: AI solution requires integration foundation
- Stakeholder analysis: Trust must be built with technical team
- CFO priority: "Real-time visibility" is top stated need

**Implication:** Resist pressure to "go big" immediately. Phased approach maximizes success probability given organizational dynamics.

---

## The Path Forward

Based on these insights, we recommend:

1. **Immediate (This Week):** Schedule executive alignment session with Wilson + Santos together
2. **Short-term (Next 30 Days):** Launch automated reporting pilot, include skeptics in design
3. **Medium-term (60-90 Days):** Technical deep-dive for integration layer, begin Phase 2 planning

## Confidence Assessment

| Insight | Confidence | Notes |
|---------|------------|-------|
| Manual data handling root cause | High | 8 corroborating data points |
| Past failure skepticism | High | Direct quotes, consistent pattern |
| Executive alignment gap | Medium | Based on separate sessions, not confirmed |
| Quick win opportunity | High | Technical feasibility confirmed |
| Missing end-user voice | High | Objective session attendance data |
| Solution feasibility gap | Medium | IT Director comment was brief |
| Optimal sequence | Medium | Logical inference, not validated |

## What We Still Don't Know

- Exact IT team capacity for integration project
- Regulatory/compliance constraints on data handling
- End-user adoption readiness and training needs
- Budget constraints beyond general "we have investment capacity"
```
