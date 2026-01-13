# Assistants Reference

Complete workflow for discovering, prioritizing, scoping, and delivering AI assistant builds (CustomGPTs, Claude Projects, prompts).

## Table of Contents

- [Workflow Overview](#workflow-overview)
- [Discover Stage](#discover-stage)
- [Prioritize Stage](#prioritize-stage)
- [Validate Stage](#validate-stage)
- [Estimate Stage](#estimate-stage)
- [Spec Stage](#spec-stage)
- [Portal Stage](#portal-stage)
- [Opportunity Categories](#opportunity-categories)
- [Scoring Criteria](#scoring-criteria)
- [Classifications](#classifications)
- [Portfolio Balance](#portfolio-balance)
- [Light Spec Template](#light-spec-template)
- [Full Spec Template](#full-spec-template)

---

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

## Discover Stage

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

See [Opportunity Categories](#opportunity-categories) for detailed signal patterns.

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

**Pattern Matching**: Cross-reference `assistants-library.json` for similar proven patterns:
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

## Prioritize Stage

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

See [Scoring Criteria](#scoring-criteria) for detailed rubrics.

### Output Format

**Prioritized table:**

| Rank | Opportunity | Category | Impact | Effort | Risk | Reuse | Strat | Score | V/E | Class | Phase |
|------|-------------|----------|--------|--------|------|-------|-------|-------|-----|-------|-------|
| 1 | [Name] | [Cat] | X | X | X | X | X | X.X | X.X | 🏃 | 1 |

**2×2 Matrix visualization** (see [Classifications](#classifications))

**Portfolio balance check:**
- Distribution across functions
- Distribution across phases
- Flag imbalances

**Then ask:**
1. "Do any rankings surprise you?"
2. "For top candidates, do effort/risk scores match your intuition?"
3. "Which should I validate and estimate?"

---

## Validate Stage

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

## Estimate Stage

Calculate build time and cost using `assistants-scoping.json` assumptions.

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

## Spec Stage

Three depths available:

### Light Spec (5-10 min)
Quick summary for review. See [Light Spec Template](#light-spec-template).

Contents: Purpose, workflow, inputs/outputs, KB recommendations, key instructions outline, 3 test scenarios.

### Full Spec (20-30 min)
Complete implementation package. See [Full Spec Template](#full-spec-template).

Contents: Overview, detailed workflow, complete instructions (500-800 words), KB structure with samples, capability settings, 5+ conversation starters, 10+ test scenarios, setup checklist, troubleshooting, success metrics, maintenance schedule.

### Formal Scoping Doc
Client approval document. Use `assets/templates/scoping-template.docx`.

Includes Full Spec content plus: risk assessment, platform compatibility matrix, implementation phases, assumptions, approval sign-off.

---

## Portal Stage

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

Cross-reference `prompts.md` to identify prompt opportunities and suggest proven patterns.

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

## Opportunity Categories

Detailed signals and patterns for each MECE category.

### 1. Knowledge Retrieval

**What it solves:** Finding and synthesizing information from existing sources.

**Signals in discovery:**
- "Where do I find..."
- "Who knows about..."
- "I always have to ask [person] about..."
- "New hires take months to learn where things are"
- "The information exists but it's buried in..."
- "People keep asking the same questions"
- "Tribal knowledge" mentions
- Policy/procedure lookup friction

**Typical GPT solution:** Q&A bot with curated knowledge base, internal wiki assistant, policy lookup tool.

**Example opportunities:**
- Employee policy FAQ bot
- Product knowledge assistant
- Procedure lookup tool
- Onboarding knowledge guide

**Key success factors:**
- Quality of knowledge base curation
- Clear scope boundaries
- Confidence indicators on answers
- Escalation path when unsure

### 2. Content Generation

**What it solves:** Creating documents, communications, and materials that follow patterns.

**Signals in discovery:**
- "I write the same email every..."
- "Reports follow a standard template"
- "Copy-paste from previous versions"
- "Formatting takes forever"
- "Draft, review, revise cycle"
- "Everyone writes it differently"
- Mentions of templates, boilerplate, standard language

**Typical GPT solution:** Draft generator with templates, communication assistant, report builder.

**Example opportunities:**
- Meeting summary generator
- Proposal draft assistant
- Email template tool
- Status report builder
- Job description writer

**Key success factors:**
- Good examples/templates in knowledge base
- Clear tone and style guidelines
- Output format specification
- Human review expectation set

### 3. Analysis & Decision Support

**What it solves:** Processing information to generate insights or recommendations.

**Signals in discovery:**
- "I have to compare..."
- "Evaluating options takes..."
- "Need to weigh pros and cons"
- "Data is there but insights aren't obvious"
- "Decision criteria are complex"
- "Scoring/rating things manually"
- Mentions of analysis frameworks, rubrics, matrices

**Typical GPT solution:** Analysis assistant, decision framework tool, evaluation helper.

**Example opportunities:**
- Vendor comparison tool
- Risk assessment assistant
- Investment screening helper
- Candidate evaluation tool
- Market analysis assistant

**Key success factors:**
- Clear analysis framework
- Explicit criteria and weights
- Confidence levels on outputs
- Supporting evidence cited

### 4. Document Processing

**What it solves:** Extracting, summarizing, or transforming information from documents.

**Signals in discovery:**
- "Reading through documents to find..."
- "Extracting data from PDFs"
- "Summarizing long reports"
- "Comparing contract terms"
- "Pulling key points from..."
- "Manual data entry from documents"
- Mentions of review, extraction, abstraction

**Typical GPT solution:** Document summarizer, extraction tool, review assistant.

**Example opportunities:**
- Contract abstraction tool
- Meeting transcript summarizer
- Research paper digest
- Invoice data extractor
- Resume screening assistant

**Key success factors:**
- Code Interpreter enabled (mandatory)
- Clear extraction schema
- Output format specified
- Handling of edge cases

### 5. Process Guidance

**What it solves:** Walking users through multi-step workflows or procedures.

**Signals in discovery:**
- "The process has many steps"
- "People skip steps or do them wrong"
- "Checklist compliance is inconsistent"
- "How do I do X" questions
- "Depends on the situation"
- SOPs that aren't followed
- Training on procedures takes long

**Typical GPT solution:** Workflow guide, procedure assistant, checklist companion.

**Example opportunities:**
- New hire onboarding guide
- Incident response assistant
- Compliance checklist tool
- Project setup wizard
- Quality control guide

**Key success factors:**
- Complete process documentation
- Conditional logic handling
- Progress tracking capability
- Clear handoff points

### 6. Training & Enablement

**What it solves:** Teaching skills, explaining concepts, providing coaching.

**Signals in discovery:**
- "Training new people takes..."
- "Wish I had a coach for..."
- "Learning curve is steep"
- "Need to practice [skill]"
- "Explaining [concept] repeatedly"
- Onboarding duration concerns
- Skill gap mentions

**Typical GPT solution:** Training assistant, skill coach, concept explainer.

**Example opportunities:**
- Sales pitch practice coach
- Product training assistant
- Interview prep tool
- Skill development guide
- Concept explainer for [domain]

**Key success factors:**
- Good examples and scenarios
- Adaptive difficulty
- Feedback mechanisms
- Progress indicators

### Cross-Category Patterns

Some opportunities span categories. When this happens:
- Identify the **primary** category (where most value comes from)
- Note secondary benefits
- Consider if should be split into separate GPTs

**Common combinations:**
- Knowledge Retrieval + Process Guidance (FAQ that walks through steps)
- Document Processing + Analysis (Extract then analyze)
- Content Generation + Knowledge Retrieval (Generate using internal sources)

### Red Flags (Probably Not a Good GPT Opportunity)

- Requires real-time external data (consider API/Actions complexity)
- Needs to write back to systems (GPTs can't edit external files)
- Highly regulated output requiring human sign-off anyway
- Process changes frequently (maintenance burden)
- Edge cases dominate (hard to handle reliably)
- Success requires 99.9%+ accuracy (GPTs have error rates)
- No clear user who would adopt it

---

## Scoring Criteria

Detailed rubrics for each scoring dimension.

### Business Impact (Weight: 35%)

**8-10: High Impact**
- Saves 5+ hours/week per user
- Critical quality or accuracy improvement
- Directly enables revenue or prevents significant costs
- Addresses top-3 stated client priority

**5-7: Medium Impact**
- Saves 2-5 hours/week per user
- Meaningful efficiency gain
- Indirect revenue enablement
- Supports secondary priorities

**2-4: Low Impact**
- Saves <2 hours/week
- Nice-to-have convenience
- Minimal measurable business effect

**0-1: Minimal Impact**
- No clear time savings
- No quality improvement
- No strategic connection

### Effort (Weight: 25%, Inverted)

*Lower score = easier to build*

**0-2: Simple Build**
- Straightforward prompt engineering
- Minimal or no knowledge base needed
- No integrations required
- 1-2 days to build and test

**3-5: Moderate Build**
- Requires curated knowledge base
- Some prompt complexity
- Standard patterns apply
- 1-2 weeks to build and test

**6-8: Complex Build**
- Significant knowledge base curation
- Complex logic or multi-step workflows
- May need Actions for integrations
- 3-4 weeks to build and test

**9-10: High Complexity**
- Requires custom integrations
- Novel approaches needed
- Significant uncertainty
- Multiple weeks, iterative development

### Risk (Weight: 15%, Inverted)

*Lower score = safer*

**0-2: Low Risk**
- Internal use only
- Low stakes if wrong
- Easy for users to verify outputs
- No compliance implications

**3-5: Moderate Risk**
- Some accuracy sensitivity
- Moderate visibility
- Users can catch errors
- Standard compliance environment

**6-8: High Risk**
- Customer-facing outputs
- High accuracy requirements
- Compliance-adjacent content
- Significant impact if errors occur

**9-10: Critical Risk**
- Regulated outputs (financial, legal, medical)
- Brand-defining if wrong
- Difficult to verify accuracy
- Potential for significant harm

### Reuse Potential (Weight: 15%)

**8-10: High Reuse**
- Pattern applies to 3+ other teams/departments
- Core components extractable for other GPTs
- Platform-level capability

**5-7: Medium Reuse**
- Pattern applies to 1-2 other areas
- Some components reusable
- Department-level capability

**2-4: Low Reuse**
- Specific to one team/function
- Limited applicability elsewhere
- Specialized use case

**0-1: No Reuse**
- Unique, one-off need
- No extractable patterns

### Strategic Fit (Weight: 10%)

**8-10: Strong Alignment**
- Directly supports #1 client priority
- Executive sponsorship likely
- Competitive advantage potential

**5-7: Good Alignment**
- Supports top-3 priorities
- Clear stakeholder interest
- Meaningful strategic value

**2-4: Weak Alignment**
- Loosely connected to priorities
- Limited executive visibility
- Tactical improvement only

**0-1: No Alignment**
- Not connected to stated priorities
- No clear strategic value

---

## V/E Ratio

The V/E Ratio (Value/Effort Ratio) provides a single metric for comparing opportunities across different scales.

### Calculation

```
V/E Ratio = Value Score ÷ Estimated Build Hours
```

Where:
- **Value Score** = Priority Score from 5-dimension weighted scoring (0-10 scale)
- **Estimated Build Hours** = Total hours from ESTIMATE stage

### Interpretation

| V/E Ratio | Interpretation | Action |
|-----------|----------------|--------|
| >1.0 | High value relative to effort | Strong candidate; prioritize |
| 0.5-1.0 | Moderate value relative to effort | Consider if strategic fit is strong |
| <0.5 | Low value relative to effort | Deprioritize unless strategic necessity |

### Example Calculations

| Opportunity | Value Score | Build Hours | V/E Ratio | Interpretation |
|-------------|-------------|-------------|-----------|----------------|
| Email Assistant | 7.5 | 6 | 1.25 | High ROI |
| Proposal Generator | 8.2 | 18 | 0.46 | Lower ROI but high impact |
| Policy Lookup | 6.0 | 4 | 1.50 | Excellent ROI |
| Custom Integration | 7.0 | 25 | 0.28 | Poor ROI |

---

## 2×2 Matrix Visualization

Plot opportunities on a Value vs. Effort matrix to visualize prioritization.

### Matrix Quadrants

```
                        HIGH VALUE (Score ≥7.0)
                              │
                              │
    ┌─────────────────────────┼─────────────────────────┐
    │                         │                         │
    │      QUICK WINS         │     STRATEGIC BETS      │
    │                         │                         │
    │   • High value          │   • High value          │
    │   • Low effort          │   • High effort         │
    │   • Do first            │   • Worth investment    │
    │   • Build momentum      │   • Plan carefully      │
    │                         │                         │
────┼─────────────────────────┼─────────────────────────┼────
    │                         │                         │
    │      MAYBE LATER        │      AVOID FOR NOW      │
    │                         │                         │
    │   • Low value           │   • Low value           │
    │   • Low effort          │   • High effort         │
    │   • Nice-to-have        │   • Poor ROI            │
    │   • Fill-in work        │   • Revisit if scope    │
    │                         │     changes             │
    │                         │                         │
    └─────────────────────────┼─────────────────────────┘
                              │
                        LOW VALUE (Score <7.0)

    LOW EFFORT (<10 hrs)              HIGH EFFORT (≥10 hrs)
```

### Quadrant Definitions

| Quadrant | Value Score | Build Hours | V/E Ratio | Recommendation |
|----------|-------------|-------------|-----------|----------------|
| Quick Wins | ≥7.0 | <10 | >0.7 | Do first |
| Strategic Bets | ≥7.0 | ≥10 | 0.35-0.7 | Plan and invest |
| Maybe Later | <7.0 | <10 | 0.4-0.7 | Backlog |
| Avoid For Now | <7.0 | ≥10 | <0.4 | Deprioritize |

---

## Classifications

Five classifications based on scoring dimensions:

### 🏃 Quick Win

**Criteria:**
- Priority Score ≥ 7.0
- Effort Score ≤ 5 (meaning low effort)
- Risk Score ≤ 4 (meaning low risk)

**Characteristics:**
- Fast to build (typically <8 hours)
- High confidence in success
- Immediate, visible value
- Builds momentum and credibility

**Timeline:** 2-4 weeks to full deployment

**Selection guidance:** Always include 1-2 Quick Wins in any phase to demonstrate value early.

### 🎯 Strategic Bet

**Criteria:**
- Impact Score ≥ 8
- Priority Score ≥ 6.5

**Characteristics:**
- High business impact potential
- May require significant investment
- Worth the effort if executed well
- Often addresses core business problems

**Timeline:** 4-8 weeks to full deployment

**Selection guidance:** Include 1 Strategic Bet per phase if Quick Wins are also present; proves long-term value.

### 🧱 Foundation Builder

**Criteria:**
- Reuse Potential ≥ 7
- Priority Score ≥ 6.0

**Characteristics:**
- Enables future GPT builds
- Creates reusable components (knowledge bases, patterns)
- Platform-level capability
- May not be flashy but reduces future effort

**Timeline:** 3-6 weeks to full deployment

**Selection guidance:** Important for long-term efficiency; balance with Quick Wins for near-term value.

### 🔬 Research/Explore

**Criteria:**
- Any dimension has "high uncertainty" flag
- Confidence tier is "Low"
- Novel use case with no Library match

**Characteristics:**
- Unproven approach
- Requires validation before commitment
- May have high potential but unknown risks
- Needs pilot or prototype first

**Timeline:** Validation phase (1-2 weeks), then reassess

**Selection guidance:** Limit to 1 per phase; allocate small time budget to explore before full commitment.

### ⏸️ Defer

**Criteria:**
- Priority Score < 5.0

**Characteristics:**
- Low value relative to effort
- Not aligned with current priorities
- May become relevant later
- Document but don't build now

**Timeline:** Revisit in future phases

**Selection guidance:** Capture for future reference; don't spend time on specs.

### Classification Decision Tree

```
START
  │
  ├─ Priority Score < 5.0?
  │   └─ YES → ⏸️ DEFER
  │
  ├─ High uncertainty on any dimension?
  │   └─ YES → 🔬 RESEARCH/EXPLORE
  │
  ├─ Score ≥7.0 AND Effort ≤5 AND Risk ≤4?
  │   └─ YES → 🏃 QUICK WIN
  │
  ├─ Reuse ≥7 AND Score ≥6.0?
  │   └─ YES → 🧱 FOUNDATION BUILDER
  │
  ├─ Impact ≥8 AND Score ≥6.5?
  │   └─ YES → 🎯 STRATEGIC BET
  │
  └─ DEFAULT → Evaluate case-by-case
```

Note: An opportunity can meet criteria for multiple classifications. Priority order:
1. Defer (if score too low)
2. Research/Explore (if too uncertain)
3. Quick Win (if meets all criteria)
4. Foundation Builder (if high reuse)
5. Strategic Bet (if high impact)

---

## Portfolio Balance

Evaluate the overall mix of selected opportunities.

### Target Distribution

| Classification | Target % | Rationale |
|----------------|----------|-----------|
| Quick Wins | 20-30% | Build momentum, prove value |
| Strategic Bets | 15-25% | Drive significant impact |
| Foundation Builders | 30-40% | Enable future efficiency |
| Research/Explore | 5-10% | Manage innovation pipeline |

### Balance Check Questions

1. **Function distribution**: Are opportunities spread across relevant departments, or concentrated in one area?
2. **Complexity distribution**: Is there a healthy mix of Simple/Medium/Complex, or all one type?
3. **Timeline distribution**: Will value be delivered continuously, or all at once at the end?
4. **Risk distribution**: Is there too much concentration in high-risk opportunities?

### Imbalance Flags

| Imbalance | Flag Message | Suggestion |
|-----------|--------------|------------|
| All Quick Wins | "Portfolio may be too conservative" | Consider adding 1 Strategic Bet |
| All Strategic Bets | "Portfolio may be too ambitious" | Add Quick Wins to build momentum |
| Single function | "4 from Sales, 0 from Marketing" | Consider cross-functional balance |
| All Complex | "High risk portfolio—all Complex builds" | Add Simple wins to derisk |
| No Foundation | "Missing reusable components" | Consider Foundation Builder for efficiency |

### Balance Output Format

```
PORTFOLIO BALANCE CHECK

Distribution by Classification:
• Quick Wins: 2 (33%) ✓
• Strategic Bets: 1 (17%) ✓
• Foundation Builders: 2 (33%) ✓
• Research/Explore: 1 (17%) ✓

Distribution by Function:
• Sales: 3
• Marketing: 2
• HR: 1

Distribution by Complexity:
• Simple: 2
• Medium: 3
• Complex: 1

Total Build Time: 52 hours
Estimated Timeline: 6-8 weeks

⚠️ Note: Sales-heavy (50%). Consider Marketing opportunities if relevant.
```

---

## No-Match Handling

When an opportunity doesn't match any Library pattern:

### Step 1: Find Closest Matches

Search Library for:
1. Same MECE category
2. Similar target users
3. Similar integration requirements
4. Similar knowledge base needs

### Step 2: Present Options

```
NO EXACT LIBRARY MATCH

Closest patterns (for benchmarking reference):

1. "Sales Email Assistant" (65% similar)
   - Same category: Content Generation
   - Similar: Email output, CRM context
   - Different: Your use case adds proposal attachment
   - Benchmark: 5-8 hours

2. "Proposal Generator" (50% similar)
   - Same output type: Client-facing document
   - Similar: Uses company templates
   - Different: More complex integrations
   - Benchmark: 10-15 hours

Options:
A) Use closest match benchmark (5-8 hours) with adjustment
B) Use category average (Content Generation: 10 hours)
C) Flag for custom scoping (run full ESTIMATE stage)

Which approach for this opportunity?
```

### Step 3: If Nothing Close (<40% Similarity)

```
NO CLOSE LIBRARY MATCH

This appears to be a novel use case without a proven pattern.

Recommendation: Flag for custom scoping
• Run full ESTIMATE stage with detailed breakdown
• Mark confidence as "Low" until validated
• Consider as 🔬 Research/Explore classification

Proceed with custom scoping?
```

---

## Confidence Tiers

Apply confidence tiers to all estimates.

### Tier Definitions

| Tier | Symbol | Condition | Estimate Behavior |
|------|--------|-----------|-------------------|
| High | ✓ | All key inputs known; Library match exists | Point estimate |
| Medium | ~ | Some gaps; using Library benchmarks | Estimate with assumptions flagged |
| Low | ? | Major gaps; no Library match | Range estimate; "needs validation" |

### Key Inputs for High Confidence

- [ ] User count known
- [ ] Usage frequency known
- [ ] Integration requirements clear
- [ ] Knowledge base sources identified
- [ ] Complexity assessed
- [ ] Library match found

### Display Format

```
ESTIMATE: Customer Onboarding Assistant

| Component | Hours | Confidence |
|-----------|-------|------------|
| Instructions | 6 | ✓ High |
| KB Setup | 4 | ~ Medium (assuming 4 files) |
| Integration | 8 | ? Low (API availability unknown) |
| **Total** | **18** | **~ Medium overall** |

Assumptions:
• KB file count based on similar Library patterns
• Integration estimate pending API confirmation

Needs validation:
• Confirm Salesforce API access with IT
```

---

## Light Spec Template

Use this template when drafting specs for selected opportunities.

### [GPT Name]

#### Purpose
[One sentence: what it does, for whom, solving what problem]

#### Core Workflow
1. [User action / input step]
2. [GPT processing step]
3. [Output / delivery step]
4. [Optional: iteration or refinement step]

#### Inputs
- [What user provides - text, files, context]
- [Required vs optional inputs]
- [Format expectations]

#### Outputs
- [What user receives]
- [Format: prose, table, document, etc.]
- [Typical length/depth]

#### Knowledge Base Requirements
| File | Purpose | Format | Priority |
|------|---------|--------|----------|
| [filename.ext] | [What it contains] | [JSON/MD/TXT] | Required |
| [filename.ext] | [What it contains] | [JSON/MD/TXT] | Optional |

*Format recommendations:*
- JSON for structured data (catalogs, databases, records)
- Markdown for narrative content (guides, policies, procedures)
- TXT for simple text (minimal formatting needs)
- Avoid large PDFs when possible (slower retrieval)

#### Capability Settings
| Capability | Setting | Rationale |
|------------|---------|-----------|
| Code Interpreter | Yes/No | [Why needed or not] |
| Web Browsing | Yes/No | [Why needed or not] |
| Image Generation | Yes/No | [Why needed or not] |

*Default: Enable only what's needed. More capabilities = more confusion.*

#### Sample Conversation Starters
1. "[Action-oriented starter for primary use case]"
2. "[Starter for secondary use case]"
3. "[Starter that demonstrates scope]"
4. "[Starter for common scenario]"

#### Key Instructions to Include

**If using knowledge base files:**
```
CRITICAL: SEARCH YOUR KNOWLEDGE DOCUMENTS BEFORE EVERY ANSWER.

FILES YOU HAVE ACCESS TO:
- [file-1.ext]: [topic/purpose]
- [file-2.ext]: [topic/purpose]

MANDATORY PROCESS:
1. First, search these files for relevant information
2. State which file(s) you found information in
3. If information NOT in files, say so explicitly
```

**Core behavior instructions:**
- [Key instruction 1 - what to always do]
- [Key instruction 2 - output format requirement]
- [Key instruction 3 - quality standard]
- [Key instruction 4 - boundary/scope limit]
- [Key instruction 5 - error handling]

**Scope boundaries:**
```
This GPT DOES:
- [In-scope task 1]
- [In-scope task 2]

This GPT does NOT:
- [Out-of-scope task 1]
- [Out-of-scope task 2]

If asked about out-of-scope topics:
"That's outside my focus. I'm designed for [purpose]. For [out-of-scope topic], I recommend [alternative]."
```

#### Testing Scenarios

**1. Core Function Test**
- Prompt: "[Specific test prompt for primary use case]"
- Expected: [What good output looks like]
- Validates: [What this tests]

**2. Edge Case Test**
- Prompt: "[Prompt that tests boundaries or unusual input]"
- Expected: [How it should handle gracefully]
- Validates: [What this tests]

**3. Out-of-Scope Test**
- Prompt: "[Prompt for something outside scope]"
- Expected: [Polite refusal with redirect]
- Validates: [Boundary enforcement]

#### Estimated Build Time
- Knowledge base curation: [X hours]
- Instruction drafting: [X hours]
- Testing & refinement: [X hours]
- **Total: [X hours/days]**

#### Success Metrics
| Metric | Target | How to Measure |
|--------|--------|----------------|
| Time savings | [X hrs/week] | User time tracking |
| Adoption | [X% of target users] | Usage analytics |
| Quality | [Specific quality bar] | Sample review |
| User satisfaction | [Rating target] | Feedback survey |

### Spec Quality Checklist

Before delivering spec, verify:

- [ ] Purpose is one clear sentence
- [ ] Workflow has 3-5 concrete steps
- [ ] Inputs and outputs are specific
- [ ] Knowledge base files are named with formats
- [ ] Capability settings have rationale
- [ ] Conversation starters are action-oriented
- [ ] Instructions include file priority block (if applicable)
- [ ] Scope boundaries are explicit
- [ ] Testing scenarios cover core + edge + boundary
- [ ] Build time estimate is realistic
- [ ] Success metrics are measurable

---

## Full Spec Template

Complete, production-ready specification for building and deploying a CustomGPT.

### [GPT Name]

#### 1. Overview

**Purpose:** [One sentence: what it does, for whom, solving what problem]

**Success Criteria:**
- [Measurable outcome 1 - e.g., "Reduces report drafting time from 2 hours to 20 minutes"]
- [Measurable outcome 2 - e.g., "90%+ of outputs require only minor edits"]
- [Measurable outcome 3 - e.g., "Adopted by 80% of target users within 30 days"]

**Primary Users:** [Role/team who will use this daily]

**Secondary Users:** [Others who may use occasionally]

#### 2. Core Workflow

```
[Step 1: User Action]
    ↓
[Step 2: GPT Processing]
    ↓
[Step 3: Output Delivery]
    ↓
[Step 4: User Review/Iteration]
```

**Detailed Flow:**

1. **Trigger**: User [specific action - uploads file, asks question, provides context]
2. **Input Processing**: GPT [validates input, extracts key elements, identifies intent]
3. **Knowledge Search**: GPT [searches specific files, retrieves relevant content]
4. **Analysis/Generation**: GPT [applies framework, generates content, performs analysis]
5. **Output Formatting**: GPT [structures response per template, adds citations]
6. **Iteration**: User [requests changes, asks follow-ups] → GPT [refines output]

**Conditional Branches:**
- IF [condition A] → [different workflow path]
- IF [condition B] → [ask clarifying question before proceeding]
- IF [missing information] → [state what's missing, proceed with assumptions noted]

#### 3. Inputs & Outputs

**Required Inputs:**
| Input | Format | Example |
|-------|--------|---------|
| [Input 1] | [Text/File/Selection] | "[Example of what user provides]" |
| [Input 2] | [Text/File/Selection] | "[Example of what user provides]" |

**Optional Inputs:**
| Input | Format | Default if Not Provided |
|-------|--------|------------------------|
| [Optional 1] | [Format] | [What GPT assumes] |
| [Optional 2] | [Format] | [What GPT assumes] |

**Outputs:**
| Output | Format | Length/Depth |
|--------|--------|--------------|
| [Primary output] | [Prose/Table/Document] | [Target length] |
| [Secondary output] | [Format] | [Target length] |

**Output Template:**
```
## [Section 1 Header]
[Content requirements and structure]

## [Section 2 Header]
[Content requirements and structure]

## [Section 3 Header]
[Content requirements and structure]

---
Sources: [Citation format]
```

#### 4. Complete Instructions

Copy-paste ready instruction block:

```markdown
# [GPT Name]

## CRITICAL: KNOWLEDGE BASE PRIORITY
SEARCH YOUR KNOWLEDGE DOCUMENTS BEFORE EVERY ANSWER.

FILES YOU HAVE ACCESS TO:
- [file-1.ext]: [Description of contents and when to use]
- [file-2.ext]: [Description of contents and when to use]
- [file-3.ext]: [Description of contents and when to use]

MANDATORY PROCESS:
1. FIRST: Search these files for relevant information
2. State which file(s) you found information in
3. Quote or paraphrase from the files with citations
4. If information is NOT in files, say so explicitly before using other knowledge

NEVER skip searching the knowledge base.

---

## PURPOSE
[One clear sentence defining what this GPT does]

---

## PROCESS

When user [primary trigger]:
1. [Specific first action]
2. [Specific second action]
3. [Specific third action]
4. [Output formatting action]

When user [secondary trigger]:
1. [Different workflow step 1]
2. [Different workflow step 2]

---

## OUTPUT FORMAT

Structure every response as:

### [Section 1]
[Requirements for this section]

### [Section 2]
[Requirements for this section]

### [Section 3]
[Requirements for this section]

**Sources:** [File name] - [Specific section referenced]

---

## QUALITY STANDARDS

Before delivering any output:
- [ ] Knowledge base was searched first
- [ ] Sources are cited for key claims
- [ ] Format matches the template above
- [ ] Tone is [specified tone - professional/conversational/etc.]
- [ ] Length is appropriate ([target length])

If any check fails, revise before presenting to user.

---

## SCOPE BOUNDARIES

This GPT DOES:
- [In-scope task 1]
- [In-scope task 2]
- [In-scope task 3]

This GPT does NOT:
- [Out-of-scope task 1]
- [Out-of-scope task 2]
- [Out-of-scope task 3]

IF user requests something outside scope:
Respond: "That's outside my specialized focus. I'm designed specifically for [core purpose]. For [out-of-scope topic], I recommend [specific alternative]."

NEVER attempt tasks outside defined scope.

---

## HANDLING UNCERTAINTY

When information is incomplete:
- State what information is missing
- Provide best answer with assumptions clearly noted
- Ask maximum 2 clarifying questions if critical info needed
- Format: "Based on [assumption], here's my response. If [alternative], let me know and I'll adjust."

When knowledge base doesn't contain answer:
- State explicitly: "This isn't covered in my knowledge base."
- Offer what you CAN help with
- Do NOT make up information or guess

---

## ERROR PREVENTION

Common mistakes to avoid:
- [Specific error pattern 1] → Instead: [Correct approach]
- [Specific error pattern 2] → Instead: [Correct approach]
- [Specific error pattern 3] → Instead: [Correct approach]
```

#### 5. Knowledge Base Specification

**File Structure:**
```
knowledge-base/
├── [primary-file.json]      # [Purpose - e.g., "Core reference data"]
├── [secondary-file.md]      # [Purpose - e.g., "Process documentation"]
├── [templates.md]           # [Purpose - e.g., "Output templates and examples"]
└── [examples.md]            # [Purpose - e.g., "Sample inputs and outputs"]
```

**File Details:**

| File | Format | Size Target | Contents | Update Frequency |
|------|--------|-------------|----------|------------------|
| [file-1] | JSON | <2MB | [What it contains] | [How often updated] |
| [file-2] | Markdown | <1MB | [What it contains] | [How often updated] |
| [file-3] | Markdown | <500KB | [What it contains] | [How often updated] |

**Format Rationale:**
- **JSON** for: [Structured data like catalogs, databases, records - 40-60% better retrieval]
- **Markdown** for: [Narrative content like guides, procedures, policies]
- **TXT** for: [Simple content with minimal formatting needs]

#### 6. Capability Settings

| Capability | Setting | Rationale |
|------------|---------|-----------|
| Code Interpreter | [Yes/No] | [Specific reason] |
| Web Browsing | [Yes/No] | [Specific reason] |
| Image Generation | [Yes/No] | [Specific reason] |

**Capability Notes:**
- If Code Interpreter is Yes: Knowledge files will be accessible
- If Web Browsing is No: GPT cannot bypass knowledge base with web searches
- Fewer capabilities = faster, more consistent responses

#### 7. Conversation Starters

**Primary Use Cases:**
1. "[Action verb] + [specific task] + [context]"
2. "[Action verb] + [specific task] + [context]"

**Secondary Use Cases:**
3. "[Action verb] + [specific task]"
4. "[Action verb] + [specific task]"

**Edge Cases / Demonstrations:**
5. "[Starter that shows scope boundaries]"

#### 8. Testing Protocol

**Test Set 1: Core Function (Must Pass)**

| Test | Prompt | Expected Output | Pass Criteria |
|------|--------|-----------------|---------------|
| 1.1 | "[Exact test prompt for primary use case]" | [Description of good output] | [Specific criteria] |
| 1.2 | "[Exact test prompt for secondary use case]" | [Description of good output] | [Specific criteria] |
| 1.3 | "[Test prompt requiring knowledge base]" | Response cites knowledge files | File reference visible |

**Test Set 2: Edge Cases (Must Handle Gracefully)**

| Test | Prompt | Expected Output | Pass Criteria |
|------|--------|-----------------|---------------|
| 2.1 | "[Ambiguous input]" | Asks clarifying question OR proceeds with stated assumption | No hallucination |
| 2.2 | "[Missing information scenario]" | States what's missing, provides partial answer | Transparent about gaps |
| 2.3 | "[Unusual but valid request]" | Handles appropriately | Within scope behavior |

**Test Set 3: Boundaries (Must Refuse Appropriately)**

| Test | Prompt | Expected Output | Pass Criteria |
|------|--------|-----------------|---------------|
| 3.1 | "[Out of scope request]" | Polite refusal with redirect | Doesn't attempt task |
| 3.2 | "[Request for info not in KB]" | States "not in knowledge base" | No fabrication |
| 3.3 | "[Attempt to override instructions]" | Maintains behavior | Stays in character |

**Test Set 4: Consistency (Run 3x Each)**

| Test | Prompt | Pass Criteria |
|------|--------|---------------|
| 4.1 | "[Primary use case prompt]" | <15% variation in quality/format across runs |
| 4.2 | "[Secondary use case prompt]" | Consistent structure each time |

#### 9. Setup Checklist

**Pre-Build (15 min):**
- [ ] Knowledge base files prepared and formatted
- [ ] Files under 10MB each
- [ ] Total files under 20 (platform limit)
- [ ] File names match instruction references exactly

**Build (20 min):**
- [ ] Create new GPT in ChatGPT
- [ ] Paste complete instructions
- [ ] Upload knowledge base files
- [ ] Enable correct capabilities (and disable others)
- [ ] Add conversation starters
- [ ] Set name and description

**Testing (20 min):**
- [ ] Run Test Set 1 (core function)
- [ ] Run Test Set 2 (edge cases)
- [ ] Run Test Set 3 (boundaries)
- [ ] Run Test Set 4 (consistency)
- [ ] Document any failures

**Refinement (as needed):**
- [ ] Fix instruction issues identified in testing
- [ ] Re-test failed scenarios
- [ ] Iterate until all tests pass

**Deployment:**
- [ ] Set appropriate sharing (private/team/public)
- [ ] Share link with initial users
- [ ] Provide brief user guidance
- [ ] Establish feedback channel

#### 10. Troubleshooting Guide

**Problem: GPT ignores knowledge base files**
- Verify Code Interpreter is enabled
- Check file names in instructions match uploaded files exactly
- Add "CRITICAL" priority block at very top of instructions
- Disable web browsing if competing with knowledge base
- Test with: "What does [filename] say about [topic]?"

**Problem: Inconsistent responses**
- Reduce enabled capabilities to only what's needed
- Remove contradictory instructions (e.g., "be brief" AND "be comprehensive")
- Add explicit output format template
- Add self-check protocol before responding

**Problem: Shows code instead of analysis**
- Add: "Use Code Interpreter for internal calculations only. Never show code to user. Present all findings as written analysis."
- Or disable Code Interpreter if not needed for file reading

**Problem: Too slow or timeout errors**
- Reduce number of knowledge files
- Convert PDFs to TXT/Markdown
- Keep files under 10MB each
- Disable unused capabilities

**Problem: Goes out of scope**
- Add explicit "This GPT does NOT" section
- Add refusal template for out-of-scope requests
- Test with boundary scenarios and refine

**Problem: Asks too many clarifying questions**
- Add: "Maximum 2 clarifying questions. Otherwise proceed with stated assumptions."
- Add: "Provide best answer first, then ask if user wants adjustments."

#### 11. Success Metrics & Monitoring

| Metric | Target | Measurement Method | Review Frequency |
|--------|--------|-------------------|------------------|
| Time savings | [X hrs/week per user] | User self-report | Weekly for first month |
| Adoption rate | [X% of target users] | Usage count | Weekly |
| Output quality | [X% usable with minor edits] | Sample review | Bi-weekly |
| User satisfaction | [X/5 rating] | Quick survey | Monthly |
| Error rate | [<X% need significant rework] | User feedback | Ongoing |

**Feedback Collection:**
- Thumbs up/down on outputs
- Brief survey after first week of use
- Monthly check-in with power users
- Track common complaints/requests

**Iteration Triggers:**
- Satisfaction drops below target → Review instructions
- Common error pattern emerges → Add to error prevention section
- Feature requests accumulate → Evaluate scope expansion
- Usage drops off → Investigate adoption barriers

#### 12. Maintenance Schedule

**Weekly:**
- Review any error reports
- Check if knowledge base needs updates

**Monthly:**
- Review success metrics
- Gather user feedback
- Update knowledge base if source content changed
- Minor instruction refinements

**Quarterly:**
- Comprehensive performance review
- Consider scope expansion based on requests
- Update for any platform changes
- Re-run full test suite

### Spec Completeness Checklist

Before delivering this spec, verify:

- [ ] Purpose is clear and measurable
- [ ] Workflow covers main + edge paths
- [ ] Instructions are copy-paste ready
- [ ] Knowledge base files are specified with formats
- [ ] Capability settings have clear rationale
- [ ] 5+ conversation starters cover use cases
- [ ] Testing protocol has 10+ specific scenarios
- [ ] Setup checklist is actionable
- [ ] Troubleshooting covers common issues
- [ ] Success metrics are measurable
- [ ] Maintenance schedule is defined
