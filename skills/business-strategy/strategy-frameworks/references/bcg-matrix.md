# BCG Matrix - Deep Dive

## Overview

The BCG Growth-Share Matrix (Boston Consulting Group, 1970) is a portfolio planning tool that helps organizations allocate resources across products or business units based on market position and growth potential.

## Detailed Methodology

### Step 1: Define the Portfolio

**What to Include:**
- Individual products or product lines
- Business units or divisions
- Brands within a portfolio
- Geographic markets
- Customer segments

**Scope Decisions:**
- Analyze at consistent level (all products OR all BUs, not mixed)
- Include all significant revenue generators
- Consider including pipeline products as "Question Marks"

### Step 2: Gather Data

**Required Metrics:**

| Metric | Definition | How to Calculate |
|--------|------------|------------------|
| **Relative Market Share** | Your share divided by largest competitor's share | Your share ÷ #1 competitor share |
| **Market Growth Rate** | Annual industry growth rate | (This year - Last year) ÷ Last year |

**Relative Market Share Examples:**
- You have 20%, leader has 40% → RMS = 0.5 (Low)
- You have 40%, leader has 20% → RMS = 2.0 (High)
- Threshold: RMS > 1.0 = High, RMS < 1.0 = Low

**Market Growth Rate:**
- Typically use industry average or segment growth
- Threshold varies by industry (common: 10% = high growth)
- Consider adjusting for your company's growth targets

### Step 3: Plot on Matrix

**Matrix Axes:**
- X-axis: Relative Market Share (High → Low, left to right)
- Y-axis: Market Growth Rate (High at top, Low at bottom)

**Quadrant Definitions:**

```
                    HIGH                    LOW
               Market Share            Market Share
         ┌────────────────────┬────────────────────┐
    HIGH │                    │                    │
  Growth │      ★ STARS       │  ❓ QUESTION MARKS │
    Rate │                    │                    │
         │  Cash: Neutral     │  Cash: Negative    │
         │  Strategy: Invest  │  Strategy: Analyze │
         ├────────────────────┼────────────────────┤
     LOW │                    │                    │
  Growth │   🐄 CASH COWS     │     🐕 DOGS        │
    Rate │                    │                    │
         │  Cash: Positive    │  Cash: Neutral     │
         │  Strategy: Harvest │  Strategy: Divest  │
         └────────────────────┴────────────────────┘
```

### Step 4: Classify and Strategize

#### Stars (High Growth + High Share)

**Characteristics:**
- Market leaders in fast-growing markets
- Require significant investment to maintain position
- Eventually become Cash Cows as market matures
- Cash flow typically neutral (high earnings, high investment)

**Strategy:**
- Invest aggressively to maintain/grow share
- Defend against competitive attacks
- Reinvest profits into growth
- Prepare for transition to Cash Cow

**Metrics to Track:**
- Market share trend
- Competitive moves
- Investment efficiency (ROI)

#### Cash Cows (Low Growth + High Share)

**Characteristics:**
- Leaders in mature, stable markets
- Generate excess cash beyond reinvestment needs
- Lower investment requirements
- Fund other portfolio investments

**Strategy:**
- Maximize profitability
- Minimize investment (maintenance only)
- Harvest cash to fund Stars and Question Marks
- Extend lifecycle through efficiency

**Metrics to Track:**
- Profit margins
- Cash generation
- Market share stability
- Cost efficiency

#### Question Marks (High Growth + Low Share)

**Characteristics:**
- Operate in attractive, growing markets
- Poor competitive position currently
- Require significant investment to grow share
- High uncertainty - could become Star or Dog

**Strategy Decision:**
- **INVEST:** If path to market leadership exists
- **DIVEST:** If competitive advantage unlikely

**Investment Criteria:**
- Can we achieve #1 or #2 position?
- What investment is required?
- What's the realistic timeline?
- What's the risk of failure?

**Metrics to Track:**
- Market share trajectory
- Investment efficiency
- Competitive position improvement
- Break-even timeline

#### Dogs (Low Growth + Low Share)

**Characteristics:**
- Weak position in slow/declining markets
- Often cash traps (consume resources)
- Limited strategic value
- May have legacy reasons for existence

**Strategy Options:**
- **DIVEST:** Sell or shut down, redeploy resources
- **HARVEST:** Minimize investment, extract remaining value
- **NICHE:** Find defensible segment within market

**Keep a Dog When:**
- Provides synergy to other units
- Serves as competitive blocker
- Has loyal customer base with stable cash flow
- Turnaround is genuinely feasible

**Metrics to Track:**
- Cash flow (must be positive or neutral)
- Strategic interdependencies
- Exit costs vs. benefits

### Step 5: Portfolio Balance

**Healthy Portfolio Characteristics:**
- Sufficient Cash Cows to fund Stars and Question Marks
- Pipeline of Stars to become future Cash Cows
- Limited resources tied up in Dogs
- Balanced risk across portfolio

**Warning Signs:**
- Too many Question Marks (cash drain)
- No Stars (no future Cash Cows)
- Too many Dogs (wasted resources)
- Cash Cows declining faster than Stars maturing

**Cash Flow Balance:**
```
Cash Cows (generate) → Stars (reinvest) + Question Marks (selective)
                     ↓
               Dogs (minimize)
```

---

## Complete Output Template

```markdown
# BCG Matrix Analysis: [Company Name] Portfolio

**Analysis Date:** [Date]
**Analyst:** [Name]
**Scope:** [What's included in portfolio]

---

## Executive Summary

**Portfolio Health:** [HEALTHY / IMBALANCED / AT RISK]

**Key Findings:**
- [Main insight about portfolio]
- [Cash flow situation]
- [Priority action needed]

**Recommended Actions:**
1. [Top priority]
2. [Second priority]
3. [Third priority]

---

## Portfolio Matrix

### Visual Representation

```
                    HIGH                    LOW
               Market Share            Market Share
              (RMS > 1.0)            (RMS < 1.0)
         ┌────────────────────┬────────────────────┐
    HIGH │                    │                    │
  Growth │  [Product A]       │  [Product D]       │
   >10%  │  [Product B]       │  [Product E]       │
         │                    │                    │
         │      ★ STARS       │  ❓ QUESTION MARKS │
         ├────────────────────┼────────────────────┤
     LOW │                    │                    │
  Growth │  [Product C]       │  [Product F]       │
   <10%  │                    │  [Product G]       │
         │                    │                    │
         │   🐄 CASH COWS     │     🐕 DOGS        │
         └────────────────────┴────────────────────┘
```

### Data Table

| Product | Revenue | Market Share | #1 Competitor Share | RMS | Market Growth | Quadrant |
|---------|---------|--------------|-------------------|-----|---------------|----------|
| [A] | $[X]M | [X]% | [Y]% | [X.X] | [X]% | Star |
| [B] | $[X]M | [X]% | [Y]% | [X.X] | [X]% | Star |
| [C] | $[X]M | [X]% | [Y]% | [X.X] | [X]% | Cash Cow |
| [D] | $[X]M | [X]% | [Y]% | [X.X] | [X]% | Question Mark |
| [E] | $[X]M | [X]% | [Y]% | [X.X] | [X]% | Question Mark |
| [F] | $[X]M | [X]% | [Y]% | [X.X] | [X]% | Dog |

---

## Quadrant Analysis

### ★ Stars

#### [Product A]
- **Revenue:** $[X]M ([X]% of portfolio)
- **Market Share:** [X]% (RMS: [X.X])
- **Market Growth:** [X]%
- **Cash Position:** [Generating/Neutral/Consuming]
- **Competitive Threats:** [Description]
- **Strategy:** INVEST to maintain leadership
- **Investment Required:** $[X]M over [X] years
- **Target Outcome:** Transition to Cash Cow by [Year]

#### [Product B]
[Same structure]

---

### 🐄 Cash Cows

#### [Product C]
- **Revenue:** $[X]M ([X]% of portfolio)
- **Market Share:** [X]% (RMS: [X.X])
- **Market Growth:** [X]%
- **Cash Generation:** $[X]M annually
- **Margin:** [X]%
- **Strategy:** HARVEST for maximum cash
- **Investment Level:** Maintenance only ($[X]M/year)
- **Lifecycle Estimate:** [X] years remaining at current profitability

---

### ❓ Question Marks

#### [Product D]
- **Revenue:** $[X]M ([X]% of portfolio)
- **Market Share:** [X]% (RMS: [X.X])
- **Market Growth:** [X]%
- **Cash Position:** CONSUMING $[X]M annually
- **Path to Leadership:** [Feasible/Unlikely]

**Investment Decision:**
- [ ] **INVEST** - If: [conditions that would justify investment]
- [x] **DIVEST** - Because: [rationale for divestment]

**If Investing:**
- Required investment: $[X]M
- Timeline to profitability: [X] years
- Target market share: [X]%

#### [Product E]
[Same structure]

---

### 🐕 Dogs

#### [Product F]
- **Revenue:** $[X]M ([X]% of portfolio)
- **Market Share:** [X]% (RMS: [X.X])
- **Market Growth:** [X]%
- **Cash Position:** [Positive/Neutral/Negative]
- **Strategic Value:** [Description of any synergies]

**Recommended Action:**
- [ ] DIVEST immediately
- [x] HARVEST remaining value
- [ ] NICHE strategy (defensible segment)

**Divestment Analysis:**
- Expected sale value: $[X]M
- Exit costs: $[X]M
- Net benefit: $[X]M
- Resource reallocation: [Where to redeploy]

---

## Portfolio Balance Assessment

### Cash Flow Analysis

| Quadrant | Products | Annual Cash Flow | Net Position |
|----------|----------|------------------|--------------|
| Stars | [List] | ($[X]M) | Investment |
| Cash Cows | [List] | +$[X]M | Generation |
| Question Marks | [List] | ($[X]M) | Investment |
| Dogs | [List] | +/-$[X]M | [Varies] |
| **TOTAL** | | **+/-$[X]M** | [BALANCED/DEFICIT/SURPLUS] |

### Balance Assessment

**Strengths:**
- [Positive aspect of portfolio]
- [Positive aspect of portfolio]

**Weaknesses:**
- [Concern about portfolio]
- [Concern about portfolio]

**Risks:**
- [What could go wrong]
- [What could go wrong]

---

## Strategic Recommendations

### Priority 1: [Action]
- **Products Affected:** [List]
- **Action:** [Specific steps]
- **Investment/Divestment:** $[X]M
- **Expected Outcome:** [Result]
- **Timeline:** [When]

### Priority 2: [Action]
[Same structure]

### Priority 3: [Action]
[Same structure]

---

## Resource Allocation Plan

| Source | Amount | Destination | Purpose |
|--------|--------|-------------|---------|
| [Cash Cow] | $[X]M | [Star] | Maintain leadership |
| [Cash Cow] | $[X]M | [Question Mark] | Build share |
| [Dog sale] | $[X]M | [Star] | Accelerate growth |

---

## Monitoring Plan

| Product | Key Metric | Current | Target | Review |
|---------|------------|---------|--------|--------|
| [Star] | Market share | [X]% | [Y]% | Quarterly |
| [Cash Cow] | Margin | [X]% | [Y]% | Quarterly |
| [Question Mark] | Share trajectory | [X]% | [Y]% | Monthly |
| [Dog] | Cash flow | $[X]M | $0 | Monthly |

**Next Portfolio Review:** [Date]
```

---

## Anti-Patterns to Avoid

1. **Oversimplification** - BCG is a starting point, not the complete answer
2. **Using absolute share** - Must be RELATIVE to largest competitor
3. **Ignoring synergies** - Products may support each other
4. **Killing all Dogs** - Some Dogs have strategic value
5. **Static analysis** - Products move between quadrants over time
6. **One-size thresholds** - 10% growth may be low for tech, high for utilities
7. **Cash flow assumptions** - Stars don't always need investment; Dogs can be profitable
8. **BCG alone** - Combine with other analyses for complete picture

## Limitations

- Only two dimensions (misses profitability, strategic fit, risk)
- Assumes market share correlates with profitability (not always true)
- Doesn't account for market attractiveness beyond growth
- Static snapshot in dynamic markets
- Ignores competitive dynamics and strategic moves
- May encourage divestment of potentially valuable businesses

## When BCG Works Best

- Diversified companies with multiple business units
- Annual strategic planning cycles
- Resource allocation decisions
- Portfolio rebalancing
- M&A target identification

## When to Use Something Else

- Single-product companies → Use Porter's or SWOT
- Rapidly changing markets → More dynamic analysis needed
- Synergy-dependent portfolio → GE-McKinsey matrix
- Detailed business unit analysis → Individual BU strategies
