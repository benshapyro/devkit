# Hyperion Example
## Complete reference deployment for commercial real estate investment firm

This example shows how the builder adapts for a different industry (commercial real estate vs LED lighting).

---

## Client Context (Hypothetical)

**Company**: Hyperion Commercial Partners
**Industry**: Commercial real estate investment and asset management
**Business**: Acquires and manages Class A office and industrial properties in secondary markets. Focus on value-add opportunities with 15-20% IRR targets. $500M AUM across 12 properties.

**Key Personas**:
1. Sarah Chen (Acquisitions Analyst) | Underwriting, investment memos | Memos take 4-6 hours, deal timelines tight
2. Marcus Williams (Asset Management VP) | Portfolio reporting, LP communications | Weekly updates for 12 properties time-consuming
3. Lisa Rodriguez (Investor Relations Manager) | Quarterly reports, LP Q&A | Complex formatting requirements, regulatory compliance
4. David Park (Managing Director) | Deal approvals, strategy | Needs executive summaries fast

**Common Tasks**:
- Investment memo writing (underwriting analysis)
- Market research and comps analysis
- LP quarterly updates and communications
- Portfolio performance reports
- Lease analysis and summaries
- Property valuation memos
- Board meeting materials

**Technical Level**: High for finance (4/5) - sophisticated with Excel/models, less with AI
**Communication Style**: Professional and direct (finance industry, investor-facing)
**Top Values**: Precision (financial accuracy critical), speed (deal timelines), professionalism (LP communications)

**Pain Points**:
- Sarah: Investment memos take 4-6 hours, deal timelines require faster turnaround
- Marcus: Weekly property updates repetitive across 12 assets
- Lisa: Quarterly LP reports require extensive formatting and compliance review
- Team: Data synthesis from multiple sources time-consuming

**Confidence**: MEDIUM (some KB content, but asked clarifying questions for personas)

---

## Questionnaire Responses (What We Asked)

Since KB was thinner, we asked:

**Q**: "What are the 3-4 people who will use this most?"
**A**: Sarah (acquisitions), Marcus (asset mgmt), Lisa (IR), David (approvals)

**Q**: "What tasks take the most time?"
**A**: Investment memos, LP communications, portfolio reports, market research

**Q**: "What's their biggest pain point?"
**A**: Sarah - memos take 4-6 hours under tight timelines; Marcus - weekly updates for 12 properties; Lisa - formatting/compliance burden

**Q**: "Technical sophistication?"
**A**: Very strong financially (models, Excel), but AI beginners. Conservative industry.

**Q**: "Communication style?"
**A**: Professional and direct - finance industry standard. Precision matters. Investor-facing.

**Q**: "Top values?"
**A**: Precision (financial), speed (deals), professionalism (LPs)

---

## Generated CustomGPT Instructions

**Character count**: 5,200 / 8,000 ✓

```markdown
# Prompt Engineering Coach for Hyperion Commercial Partners

You're a Prompt Coach for Hyperion Commercial Partners, a commercial real estate investment firm specializing in Class A office and industrial properties in secondary markets with value-add strategies. Help team members improve their ChatGPT prompts through iterative coaching conversations.

## Core Philosophy
**You're a coach, not a consultant.** Never end after one response. Always ask 2-3 follow-up questions to refine prompts through iteration.

[... Core methodology sections from template ...]

## Hyperion Context
- **Industry**: Commercial real estate investment and asset management
- **Common tasks**: Investment memo writing, market research, LP communications, portfolio reports, lease analysis, property valuations, board materials
- **Users**: Financially sophisticated (strong with Excel/models) but AI beginners. Conservative industry.
- **Values**: Precision (financial accuracy is critical), speed (deal timelines demand fast turnaround), professionalism (investor-facing communications)
- **Pain points**:
  - Sarah Chen (Acquisitions Analyst): Investment memos take 4-6 hours, deal timelines require faster analysis
  - Marcus Williams (Asset Management VP): Weekly updates for 12 properties are repetitive and time-consuming
  - Lisa Rodriguez (IR Manager): Quarterly LP reports require extensive formatting and compliance review
  - Team overall: Synthesizing data from multiple sources (CoStar, offering memos, rent rolls) is manual

## Response Style
- Professional and direct (finance industry standard)
- Show, don't just tell
- Quick wins first (2-3 changes that matter)
- Explain why (briefly)
- Always provide improved version (ready to copy)
- Keep conversation going
- Offer to test
- Build momentum

## Example

**USER**: "Write an investment memo for the property we're looking at"

**YOU**: "Questions first:
- What property type and market? (office/industrial, which secondary market?)
- What's the investment thesis? (value-add, stabilized, opportunistic?)
- Who's the audience? (IC, LP co-invest, partner review?)"

[User provides answers]

**Before**: "Write an investment memo for the property we're looking at"

**Issues**:
1. No property details (type, location, size, class)
2. Missing investment thesis and strategy
3. Doesn't specify audience (internal vs LP vs partner)
4. No key metrics mentioned (cap rate, IRR, equity multiple)
5. Output format unclear (executive summary, full memo, board deck?)

**After**: "Create an investment committee memo for acquiring [Property Name], a 150,000 SF Class A office building in [Secondary Market]. Include: (1) Executive Summary (investment thesis in 3-4 sentences), (2) Market Analysis (submarket fundamentals, comparable sales, rent growth outlook), (3) Property Overview (tenant roster, lease rollover schedule, in-place vs market rents), (4) Value-Add Strategy (specific renovations, re-tenanting plan, timeline), (5) Financial Analysis (purchase price, renovation budget, stabilized NOI, going-in and exit cap rates, 5-year cash flow projections), (6) Returns (levered/unlevered IRR, equity multiple, deal-level sensitivity analysis), (7) Risk Factors (lease rollover, market vacancy, capex timing), (8) Investment Recommendation. Target 15-20% IRR. Format for IC review - data-driven, objective tone, highlight key risks. 8-12 pages."

**Why Better**: Now ChatGPT knows exactly what property type, investment strategy, key financial metrics, and decision-making framework Hyperion uses. It'll structure the memo in your IC's preferred format with the risk-adjusted return analysis you need.

---

**Next questions**:
- "Want to test this with your actual underwriting data?"
- "Should we add comp set parameters (within 5 miles, last 12 months)?"
- "Need variations for different property types (office vs industrial)?"

[Rest of template continues...]
```

---

## Key Differences from CES

| Element | CES (LED Lighting) | Hyperion (Real Estate) |
|---------|-------------------|------------------------|
| **Industry Terms** | DLC, CCT, CRI, L70, Focus on Energy | Cap rate, IRR, NOI, Class A, value-add |
| **Common Tasks** | Proposals, vendor forms, rebates | Investment memos, LP updates, underwriting |
| **Tone** | Professional & practical | Professional & direct |
| **Values** | Quality + efficiency | Precision + speed |
| **Pain Points** | 21-day proposals, inconsistency | 4-6 hour memos, repetitive reports |
| **Tech Level** | Mixed (2-4/5) | High finance, low AI (4/5 + 1/5) |
| **Example Focus** | Technical specs, installations | Financial analysis, returns |

---

## Generated User Guide (Selected Sections)

**Real Hyperion Use Cases** (from guide):

### For Sarah Chen (Acquisitions Analyst)
**Before**: "Analyze this property investment"
**After (with Coach)**: "Analyze [Property Address] acquisition opportunity. Property: 200K SF industrial warehouse, [Market], asking $45M. Provide: (1) Market rent comparison (3-5 mile radius, similar class/size), (2) Cap rate analysis (going-in vs stabilized, compare to recent comps), (3) Value-add opportunities (roof replacement $800K, dock door upgrades $300K, improve tenant mix), (4) 5-year cash flow projection (assume 3% rent growth, 2% expense growth), (5) Return metrics (levered/unlevered IRR, equity multiple at 60% LTV), (6) Key risks (tenant concentration at 40%, $12M TI exposure in Year 3). Target 18-20% levered IRR. Format for IC review - tables for financials, bullet points for risks."

**Result**: Investment memo draft time reduced from 4-6 hours to 90 minutes, IC approvals faster

### For Marcus Williams (Asset Management VP)
**Before**: "Create property update"
**After (with Coach)**: "Create weekly asset management update for [12-property portfolio]. For each property: (1) Occupancy status (current %, changes from last week), (2) Leasing activity (tours scheduled, proposals out, LOIs signed), (3) Active issues (maintenance, tenant concerns, vendor delays), (4) Budget variance (actual vs budget YTD), (5) Upcoming milestones (lease expirations next 90 days, capital projects). Highlight any RED FLAGS (unexpected vacancy, budget overruns >10%, tenant default risk). Format as executive dashboard - one page per property, traffic light indicators (green/yellow/red), action items with owners. Professional but efficient tone - David reads these in 5 minutes."

**Result**: Weekly reporting time reduced from 3 hours to 45 minutes across 12 properties

### For Lisa Rodriguez (IR Manager)
**Before**: "Write quarterly LP update"
**After (with Coach)**: "Create Q4 2024 LP quarterly report for Hyperion Fund II ($200M fund, 8 properties). Include: (1) Portfolio Performance Summary (aggregate occupancy, NOI, NAV), (2) Investment Activity (1 acquisition, 2 dispositions with returns), (3) Asset-by-Asset Update (1 paragraph per property - performance, leasing, value-add progress), (4) Market Commentary (secondary market office/industrial trends, cap rate environment), (5) Fund Metrics (since-inception IRR, current distributions, NAV per share), (6) Outlook (2025 strategy, deployment plan, exit timeline). Comply with: SEC marketing rule (performance presentation), audited financials reconciliation, risk disclosure requirements. Tone: professional, transparent, confidence-inspiring. Target 15-20 pages, formatted for LP consumption."

**Result**: Quarterly report draft quality improved, compliance review time reduced by 40%

---

## Deployment Considerations

**What's Different for Real Estate**:

1. **Regulatory sensitivity** - LP communications have SEC requirements
2. **Financial precision** - Numbers must be exact (not "approximately")
3. **Conservative culture** - Finance industry slower AI adoption
4. **High stakes** - Investment decisions are multi-million dollar

**Rollout Strategy**:
- Start with Sarah (highest pain, analytically minded)
- Prove value with investment memo time savings
- Then Marcus (portfolio reporting, clear ROI)
- Lisa last (compliance concerns, most conservative)
- David sees results through team before using himself

**Success Metrics**:
- Sarah: Investment memo time 4-6 hours → 90 minutes
- Marcus: Weekly updates 3 hours → 45 minutes
- Lisa: Quarterly report draft quality + 40% faster compliance review
- Team: 3+ custom GPTs for repeated tasks

---

## Tone Comparison Examples

**Same feedback, different tones**:

### CES (Professional & Practical):
> "You're missing the format. Add this: 'Format as 2-page summary with executive overview.' That tells ChatGPT exactly what you need."

### Hyperion (Professional & Direct):
> "Specify output format: 'Create 2-page executive summary - first page key metrics, second page detailed breakdown.' Precision matters for IC review."

**Notice**: 
- CES: More conversational, practical focus
- Hyperion: More formal, precision focus
- Both direct, but Hyperion emphasizes financial accuracy

---

## Validation Scores

**Part 1 (Instructions): 18/18** ✓
- Real estate terminology throughout (cap rate, IRR, NOI) ✓
- 4 personas with specific financial pain points ✓
- Investment memo example feels authentic ✓
- Tone matches finance industry (professional & direct) ✓

**Part 2 (User Guide): 13/13** ✓
- Use cases feel real (underwriting, LP comms, portfolio reporting) ✓
- Quantified improvements (4-6 hours → 90 minutes) ✓
- Regulatory considerations mentioned ✓

**Total: 42/42 - Excellent quality**

---

## Key Learnings

**What This Example Teaches**:

1. **Industry terminology matters** - Using cap rate, IRR, value-add makes it feel native
2. **Tone calibration is critical** - Finance = direct + precise vs Manufacturing = practical + efficient
3. **Pain points must be specific** - "4-6 hours" > "takes too long"
4. **Regulatory context matters** - SEC rules for LP communications
5. **Rollout strategy varies** - Conservative industry = prove value with power user first

**Universal Elements** (same as CES):
- Continuous improvement loop
- 7 coaching checks
- Testing together approach
- Real persona names
- Quantified results

**This demonstrates**: Same methodology, different context = high-quality customization
