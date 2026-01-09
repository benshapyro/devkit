---
name: strategy-frameworks
description: Apply strategic business analysis frameworks (Porter's Five Forces, BCG Matrix, SWOT, McKinsey 7S). Use when analyzing industries, evaluating portfolios, strategic planning, organizational assessment, or when the user mentions Porter, BCG, SWOT, 7S, competitive forces, industry analysis, or strategic analysis.
---

# Strategy Frameworks

Apply structured strategic analysis frameworks to business problems. Each framework serves a specific purpose - use the right tool for the job.

## Quick Reference

| Framework | Purpose | Best For |
|-----------|---------|----------|
| Porter's Five Forces | Industry attractiveness | Market entry, investment decisions, competitive dynamics |
| BCG Matrix | Portfolio allocation | Resource allocation across products/business units |
| SWOT Analysis | Strategic planning | Broad assessment, quick situational analysis |
| McKinsey 7S | Organizational alignment | Change management, M&A integration, transformation |

## Framework Selection

Before starting, determine which framework fits the question:

**Use Porter's Five Forces when:**
- Evaluating market entry or exit
- Assessing industry profitability potential
- Understanding competitive dynamics
- M&A due diligence (industry assessment)

**Use BCG Matrix when:**
- Allocating resources across products/units
- Deciding where to invest or divest
- Portfolio strategy decisions
- Annual strategic planning

**Use SWOT Analysis when:**
- Starting strategic planning
- Quick situational assessment
- Evaluating new opportunities
- Need broad perspective fast

**Use McKinsey 7S when:**
- Planning organizational change
- M&A integration
- Diagnosing performance issues
- Transformation programs

See `references/framework-selection.md` for detailed decision tree.

---

## Porter's Five Forces (Quick Start)

Analyze industry competitive dynamics and profitability.

### Process
1. **Define industry scope** - Be specific (not "food industry" but "fast-casual restaurants in urban markets")
2. **Assess each force** - Rate as HIGH, MODERATE, or LOW impact
3. **Identify implications** - What does this mean for strategy?
4. **Develop responses** - Actions to address each force

### Five Forces to Analyze

| Force | Key Questions |
|-------|---------------|
| **Threat of New Entrants** | Capital requirements? Regulatory barriers? Brand loyalty? |
| **Buyer Power** | Concentration? Switching costs? Price sensitivity? |
| **Supplier Power** | How many suppliers? Substitute inputs? Forward integration risk? |
| **Threat of Substitutes** | Alternative solutions? Price-performance trade-off? |
| **Competitive Rivalry** | Number of competitors? Industry growth? Exit barriers? |

### Output Template

```markdown
# Porter's Five Forces: [Industry]

## Summary
- Industry Attractiveness: [HIGH/MODERATE/LOW]
- Key Insight: [1-2 sentences]

## Force Analysis

### Threat of New Entrants: [HIGH/MODERATE/LOW]
- [Key factor with impact]
- [Key factor with impact]
**Implication:** [Strategic response]

### Buyer Power: [HIGH/MODERATE/LOW]
- [Key factor with impact]
**Implication:** [Strategic response]

### Supplier Power: [HIGH/MODERATE/LOW]
- [Key factor with impact]
**Implication:** [Strategic response]

### Threat of Substitutes: [HIGH/MODERATE/LOW]
- [Key factor with impact]
**Implication:** [Strategic response]

### Competitive Rivalry: [HIGH/MODERATE/LOW]
- [Key factor with impact]
**Implication:** [Strategic response]

## Strategic Recommendations
1. [Priority action]
2. [Priority action]
3. [Priority action]
```

See `references/porter-five-forces.md` for detailed methodology.

---

## BCG Matrix (Quick Start)

Analyze product/business unit portfolio for resource allocation.

### Process
1. **List portfolio items** - Products, services, or business units
2. **Gather data** - Market share vs. largest competitor, market growth rate
3. **Plot on matrix** - Position each item in appropriate quadrant
4. **Determine strategy** - Invest, harvest, or divest based on position

### Quadrant Definitions

| Quadrant | Characteristics | Strategy |
|----------|-----------------|----------|
| **Stars** (High Growth, High Share) | Market leaders in growing markets | Invest to maintain leadership |
| **Cash Cows** (Low Growth, High Share) | Mature leaders generating cash | Harvest cash, minimal investment |
| **Question Marks** (High Growth, Low Share) | Uncertain potential | Invest selectively or divest |
| **Dogs** (Low Growth, Low Share) | Weak position in mature markets | Divest or manage for efficiency |

### Output Template

```markdown
# BCG Matrix: [Company] Portfolio

## Matrix Summary

|                    | High Market Share | Low Market Share |
|--------------------|-------------------|------------------|
| **High Growth**    | STARS             | QUESTION MARKS   |
| **Low Growth**     | CASH COWS         | DOGS             |

## Stars (Invest)
- **[Product]**: Market share [X], Growth [Y%]
  Strategy: [Action]

## Cash Cows (Harvest)
- **[Product]**: Market share [X], Growth [Y%]
  Strategy: [Action]

## Question Marks (Selective)
- **[Product]**: Market share [X], Growth [Y%]
  Decision: [INVEST / DIVEST] because [rationale]

## Dogs (Divest/Efficiency)
- **[Product]**: Market share [X], Growth [Y%]
  Decision: [Action]

## Portfolio Balance
- Cash generation sufficient: [YES/NO]
- Recommended rebalancing: [Actions]
```

See `references/bcg-matrix.md` for detailed methodology.

---

## SWOT Analysis (Quick Start)

Identify internal strengths/weaknesses and external opportunities/threats.

### Process
1. **Define objective** - What decision is this SWOT informing?
2. **Gather input** - Include diverse perspectives
3. **Analyze factors** - Internal (S/W) and external (O/T)
4. **Prioritize** - Top 3-5 per quadrant
5. **Convert to action** - Use TOWS matrix to develop strategies

### SWOT Categories

| Internal | External |
|----------|----------|
| **Strengths** - Capabilities providing advantage | **Opportunities** - External conditions to exploit |
| **Weaknesses** - Limitations hindering performance | **Threats** - External conditions posing risk |

### Output Template

```markdown
# SWOT Analysis: [Subject]

**Objective:** [What decision this informs]

## SWOT Matrix

| Strengths | Weaknesses |
|-----------|------------|
| 1. [Specific + metric] | 1. [Specific + impact] |
| 2. [Specific + metric] | 2. [Specific + impact] |
| 3. [Specific + metric] | 3. [Specific + impact] |

| Opportunities | Threats |
|---------------|---------|
| 1. [Specific + potential] | 1. [Specific + likelihood] |
| 2. [Specific + potential] | 2. [Specific + likelihood] |
| 3. [Specific + potential] | 3. [Specific + likelihood] |

## TOWS Strategic Actions

### SO (Strengths → Opportunities)
- Use [Strength] to capture [Opportunity]

### ST (Strengths → Threats)
- Use [Strength] to counter [Threat]

### WO (Weaknesses → Opportunities)
- Address [Weakness] to pursue [Opportunity]

### WT (Weaknesses → Threats)
- Minimize [Weakness] to avoid [Threat]

## Priority Actions
1. [Action] - Owner: [Name] - Timeline: [Date]
2. [Action] - Owner: [Name] - Timeline: [Date]
```

See `references/swot-analysis.md` for detailed methodology and TOWS matrix.

---

## McKinsey 7S (Quick Start)

Assess organizational alignment across 7 interconnected elements.

### Process
1. **Define scope** - Entire org, business unit, or department
2. **Assess current state** - Evaluate each of 7 elements
3. **Identify misalignments** - Where do elements conflict?
4. **Define future state** - What should each element look like?
5. **Plan interventions** - Prioritize changes needed

### The 7 Elements

**Hard Elements (Tangible):**
- **Strategy** - Plan to achieve competitive advantage
- **Structure** - Organizational hierarchy and reporting
- **Systems** - Processes, procedures, IT systems

**Soft Elements (Intangible):**
- **Shared Values** - Core beliefs and norms (central element)
- **Style** - Leadership approach and management style
- **Staff** - Talent, capabilities, development
- **Skills** - Organizational competencies

### Output Template

```markdown
# McKinsey 7S Analysis: [Organization]

**Scope:** [Entire org / Business unit / Department]
**Context:** [Strategic situation being evaluated]

## 7S Assessment

### Hard Elements

**Strategy:** [ALIGNED / MISALIGNED]
- Current: [Description]
- Issues: [Gaps identified]
- Action: [Changes needed]

**Structure:** [ALIGNED / MISALIGNED]
- Current: [Description]
- Issues: [Gaps identified]
- Action: [Changes needed]

**Systems:** [ALIGNED / MISALIGNED]
- Current: [Description]
- Issues: [Gaps identified]
- Action: [Changes needed]

### Soft Elements

**Shared Values:** [Central element]
- Current: [Description]
- Lived vs. Stated: [GAP / ALIGNED]
- Action: [Changes needed]

**Style:** [ALIGNED / MISALIGNED]
- Current: [Description]
- Action: [Changes needed]

**Staff:** [ALIGNED / MISALIGNED]
- Current: [Description]
- Action: [Changes needed]

**Skills:** [ALIGNED / MISALIGNED]
- Current: [Description]
- Action: [Changes needed]

## Critical Misalignments
1. [Element A] ↔ [Element B]: [Conflict description]
2. [Element C] ↔ [Element D]: [Conflict description]

## Implementation Roadmap
**Phase 1 (Months 1-3):** [Priority actions]
**Phase 2 (Months 4-6):** [Secondary actions]
```

See `references/mckinsey-7s.md` for detailed methodology.

---

## Common Mistakes

### All Frameworks
- **Vague analysis** - Be specific with metrics and evidence
- **No action items** - Always convert analysis to strategy
- **Static thinking** - Reassess regularly as conditions change
- **Wrong framework** - Match tool to problem type

### Porter's Five Forces
- Defining industry too broadly or narrowly
- Treating all forces equally (some matter more)
- Ignoring macro factors (regulation, technology)

### BCG Matrix
- Using absolute vs. relative market share
- Ignoring synergies between portfolio items
- Treating "Dogs" as always disposable

### SWOT Analysis
- Confusing internal vs. external factors
- Listing too many items (stick to top 3-5 per quadrant)
- Not converting to action (SWOT without TOWS)

### McKinsey 7S
- Focusing only on hard elements (Strategy, Structure, Systems)
- Ignoring that Shared Values are central
- Not addressing all 7 elements together

---

## Resources

- `references/framework-selection.md` - Decision tree for choosing framework
- `references/porter-five-forces.md` - Detailed Porter's methodology and template
- `references/bcg-matrix.md` - Detailed BCG methodology and template
- `references/swot-analysis.md` - Detailed SWOT methodology with TOWS matrix
- `references/mckinsey-7s.md` - Detailed 7S methodology and template

---

## Version History

- v1.0.0 (2026-01-08): Initial version with 4 core frameworks
