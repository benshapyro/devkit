# Assistants Workflow Reference

Complete workflow for discovering, prioritizing, scoping, and delivering AI assistant builds (CustomGPTs, Claude Projects, prompts).

## Workflow Overview

```
DISCOVER → PRIORITIZE → VALIDATE → ESTIMATE → SPEC → PORTAL
```

| Stage | Command | Purpose | Output |
|-------|---------|---------|--------|
| Discover | `/assistants discover` | Find opportunities from docs + Catalog | Opportunity list |
| — | `/assistants library` | Browse 50 proven patterns | Pattern selection |
| Prioritize | `/assistants prioritize` | Score, rank, classify | Prioritized table |
| Validate | `/assistants validate` | Check for blockers | Feasibility assessment |
| Estimate | `/assistants estimate` | Calculate build time/cost | Hours and cost |
| Spec | `/assistants spec` | Generate implementation docs | Light, Full, or Formal |
| Portal | `/assistants portal` | Client-facing artifact | Branded HTML |

---

## DISCOVER Stage

Two entry points:

### Option 1: Knowledge Base + Catalog Scan

Search project documents AND Discovery Catalog for opportunities.

**Document scan looks for:**

| Category | Signals to Find |
|----------|-----------------|
| Knowledge Retrieval | Repeated questions, policy lookups, tribal knowledge |
| Content Generation | Template-based reports, repetitive emails, proposals |
| Analysis & Decision Support | Data interpretation, comparisons, recommendations |
| Document Processing | Extracting from files, summarizing docs, parsing |
| Process Guidance | Multi-step workflows, checklists, SOPs |
| Training & Enablement | Onboarding, skill development, coaching |

See `opportunity-categories.md` for detailed signal patterns.

**Discovery Catalog query:**
```
# Query high-priority challenges for GPT opportunity signals
list_records: Table 5_Challenges
Filter: {Priority Score} >= 64

# Query existing solutions that may be GPT candidates
list_records: Table 6_Solutions
Filter: {Solution Type} contains 'AI' OR {Solution Type} contains 'Automation'
```

**For each opportunity, capture:**
- **Name**: Clear, descriptive title
- **Problem Statement**: Current pain/inefficiency
- **Current State**: How done now (time, people, tools)
- **Assistant Solution**: What the AI assistant would do
- **Primary Users**: Who would use it
- **Category**: Which of the 6 above
- **Evidence**: Specific quotes/references from source
- **Source**: Document name or Catalog record

**Pattern Matching**: Cross-reference `use-case-library.json` for similar proven patterns:
- **Exact match**: "This matches our proven 'Sales Email Draft Assistant' pattern"
- **Category match**: "Similar use cases in Content Generation: [list 2-3]"
- **Semantic match**: "Related pattern (different scope): [name]"

When a match exists, inherit benchmark data (complexity, hours, success metrics).

### Option 2: Browse Library

For clients who want to explore proven patterns directly.

**Interactive flow:**

1. Show summary by function:
```
Use Case Library: 50 proven patterns

| Function | Count | Simple | Medium | Complex |
|----------|-------|--------|--------|---------|
| Sales | 10 | 2 | 3 | 5 |
| Marketing | 13 | 3 | 8 | 2 |
| Finance/Operations | 5 | 1 | 1 | 3 |
| HR | 5 | 1 | 3 | 1 |
| Customer Success | 6 | 1 | 3 | 2 |
| General Productivity | 11 | 3 | 7 | 1 |

Which function would you like to explore?
```

2. Show use cases for selected function (name, complexity, hours range, business value)

3. Drill into specific use case on request (full details)

4. Select use cases to add to opportunity list

---

## PRIORITIZE Stage

Score each opportunity (0-10 scale):

| Dimension | Weight | Summary |
|-----------|--------|---------|
| Business Impact | 35% | Time savings, error reduction, strategic value |
| Effort | 25% | Technical complexity, KB needs (inverted) |
| Risk | 15% | Accuracy requirements, sensitivity (inverted) |
| Reuse Potential | 15% | Applicability to other teams/use cases |
| Strategic Fit | 10% | Alignment with client priorities |

**Priority Score:**
```
Score = (Impact × 0.35) + ((10 - Effort) × 0.25) + ((10 - Risk) × 0.15) + (Reuse × 0.15) + (Strategic × 0.10)
```

**V/E Ratio** (Value/Effort): `Value Score ÷ Estimated Build Hours`
- >1.0 = High value relative to effort
- 0.5-1.0 = Moderate value relative to effort
- <0.5 = Low value relative to effort

See `scoring-criteria.md` for detailed rubrics and `prioritization-framework.md` for V/E calculation, matrix logic, and classification rules.

### Classifications

| Class | Criteria | Label | Phase |
|-------|----------|-------|-------|
| Quick Win | Score ≥7.0, Effort ≤5, Risk ≤4 | 🏃 | Phase 1 |
| Strategic Bet | Impact ≥8, Score ≥6.5 | 🎯 | Phase 2 |
| Foundation Builder | Reuse ≥7, Score ≥6.0 | 🧱 | Phase 2 |
| Research/Explore | High uncertainty | 🔬 | Validate first |
| Defer | Score <5.0 | ⏸️ | Backlog |

### Output Format

**Prioritized table:**

| Rank | Opportunity | Category | Impact | Effort | Risk | Reuse | Strat | Score | V/E | Class | Phase |
|------|-------------|----------|--------|--------|------|-------|-------|-------|-----|-------|-------|
| 1 | [Name] | [Cat] | X | X | X | X | X | X.X | X.X | 🏃 | 1 |

**2×2 Matrix visualization** (see prioritization-framework.md)

**Portfolio balance check:**
- Distribution across functions
- Distribution across phases
- Flag imbalances

**Then ask:**
1. "Do any rankings surprise you?"
2. "For top candidates, do effort/risk scores match your intuition?"
3. "Which should I validate and estimate?"

---

## VALIDATE Stage

For selected opportunities, check for blockers.

**Blocker questions:**

| Area | Question | Red Flag |
|------|----------|----------|
| Integrations | Does an API/MCP exist? | No API, custom build required |
| Credentials | Can client provide auth? | IT won't approve, security block |
| Knowledge Base | Do source files exist? | Extensive creation needed |
| Data Freshness | How often does data change? | Real-time needs, frequent updates |
| Dependencies | Other systems required? | Chain of dependencies |

**Output per use case:**
- ✅ **Clear to proceed**: No blockers
- ⚠️ **Proceed with caution**: Minor concerns, document assumptions
- 🛑 **Blocker identified**: Resolve before spec

---

## ESTIMATE Stage

Calculate build time and cost using `scoping-config.json` assumptions.

### Build Time Components

| Component | Simple | Medium | Complex |
|-----------|--------|--------|---------|
| Instructions | 3 hrs | 6 hrs | 10 hrs |
| KB per existing file | 1 hr | 1 hr | 1 hr |
| KB per new file | 2 hrs | 2 hrs | 2 hrs |
| Integration | 4 hrs | 8 hrs | 15 hrs |
| GPT Action | 3 hrs | 3 hrs | 3 hrs |

### Calculation

```
Total Hours = Instructions + KB Setup + KB Creation + Integrations + Actions

Estimated Cost = Total Hours × Hourly Rate ($150 default)

Complexity Rating:
- Simple: <8 hours
- Medium: 8-20 hours  
- Complex: >20 hours
```

### Output Format

```
ESTIMATE: [Use Case Name]

| Component | Hours |
|-----------|-------|
| Instructions (Medium) | 6 |
| KB Setup (3 existing files) | 3 |
| KB Creation (1 new file) | 2 |
| Integration - Salesforce (Medium) | 8 |
| GPT Action (1 action) | 3 |
| **Total** | **22 hrs** |

Complexity: Complex
Estimated Cost: $3,300
Confidence: High
```

**Library benchmark comparison** when match exists:
```
Library Benchmark: 10-15 hours
Your Estimate: 22 hours
Delta: +7-12 hours due to additional integration
```

---

## SPEC Stage

Three depths available:

### Light Spec (5-10 min)
Quick summary for review. Use `spec-template.md`.

Contents: Purpose, workflow, inputs/outputs, KB recommendations, key instructions outline, 3 test scenarios.

### Full Spec (20-30 min)
Complete implementation package. Use `full-spec-template.md`.

Contents: Overview, detailed workflow, complete instructions (500-800 words), KB structure with samples, capability settings, 5+ conversation starters, 10+ test scenarios, setup checklist, troubleshooting, success metrics, maintenance schedule.

### Formal Scoping Doc
Client approval document. Use `assets/templates/scoping-template.docx`.

Includes Full Spec content plus: risk assessment, platform compatibility matrix, implementation phases, assumptions, approval sign-off.

---

## PORTAL Stage

Generate client-facing Solution Catalog HTML artifact showing all assistants and prompts.

### Assistants Tab

**Card fields:**
| Field | Source |
|-------|--------|
| name | From opportunity |
| purpose | 1-2 sentence description |
| category | Function area (Finance Operations, Sales, etc.) |
| status | not-selected, backlog, in-progress, testing, live |
| impact | high, medium, low |
| description | Full description for modal |
| problem | Problem this solves (for modal) |
| link | Direct URL to assistant (shown only when Live) |
| samplePrompts | Array of 2-3 example prompts (for modal) |
| knowledgeBase | Description of KB contents (for modal) |

**Status options:**
- `not-selected` — Identified but not approved
- `backlog` — Approved, not started
- `in-progress` — Currently being built
- `testing` — Built, being validated
- `live` — Deployed and available

**Impact options:**
- `high` — Significant time/cost savings, strategic value
- `medium` — Moderate improvements
- `low` — Nice to have, incremental

### Prompts Tab

**Card fields:**
| Field | Source |
|-------|--------|
| name | Prompt name |
| purpose | What it does (1 sentence) |
| category | Function area |
| priority | 0-100 numeric score |
| promptText | Full prompt text (for modal + copy) |
| usage | When to use this (for modal) |

### Visual Format

- Cadre-branded design
- Tabbed interface (Assistants / Prompts)
- Search box and filter buttons
- Card grid with hover effects
- Click card → modal with full details
- Launch button (assistants, when Live)
- Copy button (prompts)

Template: `assets/artifact-templates/solution-catalog.html`

### Discovery Integration

`/assistants discover` now finds BOTH assistant and prompt opportunities:

**Assistant signals:** (same as before)
- Knowledge retrieval patterns
- Content generation patterns
- Process guidance patterns

**Prompt signals:** (from prompt-engineering patterns)
- Repetitive text tasks ("we write the same emails")
- Consistent formatting needs ("reports always follow this structure")
- Template-based writing ("we use this template for...")

Cross-reference `solutions/prompts/patterns/` to identify prompt opportunities and suggest proven patterns.

---

## Discovery Catalog Integration

### Reading from Catalog

Before `/assistants discover`:
- Query 5_Challenges for high-priority pain points
- Query 6_Solutions for existing AI/automation ideas
- Query 4_Technology for integration context

### Writing to Catalog

After prioritization, **prompt before writing**:

> "Would you like me to add these prioritized opportunities to the Discovery Catalog as Solutions?
> 
> This will create records in the Solutions table with:
> - Solution Name: [Assistant name]
> - Solution Type: AI Assistant
> - Linked Challenge: [If identified]
> - Status: Proposed
> - Notes: [Summary from spec]
> 
> Add to Catalog? (Yes/No)"

Only write if user confirms.

---

## Platform Compatibility

Track but don't filter. Flag limitations in Validate stage.

| Platform | Notes |
|----------|-------|
| ChatGPT | Primary target. Full feature support including Actions. |
| Claude | Compatible for most. No Actions equivalent yet. Use Projects. |
| Copilot | Limited. Check specific requirements. |
| Gemini | Varies. Test before committing. |

Example flag: "⚠️ Claude: No Actions — will need alternative for CRM integration"

---

## No-Match Handling

When opportunity doesn't match any Library pattern:

1. Find closest matches (same category, similar users, similar integrations)
2. Present options:
   - Use closest match benchmark with adjustment
   - Use category average
   - Flag for custom scoping
3. If nothing close (<40% similarity), mark as 🔬 Research/Explore

See `prioritization-framework.md` for detailed no-match logic.

---

## Confidence Tiers

Apply to all estimates:

| Tier | Symbol | Condition | Behavior |
|------|--------|-----------|----------|
| High | ✓ | All inputs known; Library match | Point estimate |
| Medium | ~ | Some gaps; using benchmarks | Estimate with assumptions |
| Low | ? | Major gaps; no match | Range; "needs validation" |
