# Assistant Prioritization & Scoring

Detailed logic for opportunity scoring, V/E Ratio calculation, classifications, and portfolio balance.

## Table of Contents

- [Scoring Criteria](#scoring-criteria)
- [V/E Ratio](#ve-ratio)
- [2×2 Matrix Visualization](#2×2-matrix-visualization)
- [Classifications](#classifications)
- [Portfolio Balance](#portfolio-balance)
- [No-Match Handling](#no-match-handling)
- [Confidence Tiers](#confidence-tiers)

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

---

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

---

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

---

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

---

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
| 0.5–1.0 | Moderate value relative to effort | Consider if strategic fit is strong |
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
| Strategic Bets | ≥7.0 | ≥10 | 0.35–0.7 | Plan and invest |
| Maybe Later | <7.0 | <10 | 0.4–0.7 | Backlog |
| Avoid For Now | <7.0 | ≥10 | <0.4 | Deprioritize |

### Generating the Matrix

When presenting the matrix, list opportunities in each quadrant:

```
2×2 PRIORITIZATION MATRIX

QUICK WINS (Do First)
• Policy Lookup Bot (V/E: 1.50)
• Email Draft Assistant (V/E: 1.25)
• Meeting Prep Helper (V/E: 0.95)

STRATEGIC BETS (Worth Investment)
• Proposal Generator (V/E: 0.46)
• Customer Onboarding Guide (V/E: 0.52)

MAYBE LATER (Backlog)
• FAQ Bot (V/E: 0.65)
• Template Finder (V/E: 0.58)

AVOID FOR NOW (Poor ROI)
• Custom CRM Integration (V/E: 0.28)
• Legacy System Bridge (V/E: 0.22)
```

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

---

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

---

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

---

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

---

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

---

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
