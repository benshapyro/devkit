---
name: software-research-analyst
description: Conduct strategic software research for major purchases ($50K+ annual spend). Use when evaluating 2-5 finalist tools and need comprehensive analysis including pricing, features, integrations, vendor stability, user reviews, and TCO calculations. Produces executive-ready recommendations with evidence-based scoring and implementation plans. Best for SaaS evaluation, enterprise tool selection, and multi-year vendor commitments.
---

# Software Research Analyst

This skill provides a systematic methodology for conducting strategic-level software research when making major purchasing decisions. Use this when you need to move beyond surface-level comparisons and conduct actual due diligence.

## What This Skill Does

This skill transforms software evaluation from "read the marketing page" into strategic due diligence. It provides:

- **Systematic research framework**: 11-section template covering everything from vendor stability to total cost of ownership
- **Quality standards**: Ensures research is evidence-based, not opinion-based
- **Comparative analysis**: Structured scoring and trade-off identification
- **Executive deliverables**: Clear recommendations with supporting rationale

**Not a quick comparison tool** - This is for decisions worth $50K+ annually or multi-year commitments where getting it wrong is expensive.

## When to Use This Skill

Use this skill when:
- Evaluating 2-5 finalist tools for a major purchase
- Decision involves $50K+ annual spend or multi-year contract
- Need to justify choice to executives or board
- Multiple stakeholders with different requirements
- High implementation risk or switching cost

**Don't use for:**
- Quick feature comparisons between tools
- Personal/small team tool selection (<$5K/year)
- Already know which tool to use, just need implementation help

## The 5-Step Research Process

### Step 1: Gather Decision Context

Before starting research, understand:
- **What decision?** (e.g., "Replace Salesforce with more affordable CRM")
- **Budget parameters**: Annual software, implementation, training budgets
- **Critical requirements**: Must-haves vs nice-to-haves (rank top 5)
- **Timeline**: When must decision be made?
- **Stakeholders**: Who decides, who uses, who pays?

**Minimum needed to proceed:** Decision description, budget range, top 3 requirements, 2-5 tools to evaluate.

### Step 2: Create Research Brief

Run `scripts/init_research.py` to generate a customized research plan:

```bash
python scripts/init_research.py
```

The script will:
1. Prompt for decision context
2. Ask about requirements and tools
3. Generate a tailored research brief
4. Output a document ready for research

**Alternative:** If you prefer to start manually, load `references/template.md` and begin Section 1.

### Step 3: Conduct Systematic Research

For each tool, work through the 11-section template in `references/template.md`:

1. **Company & Product Foundation** - Vendor stability, product maturity
2. **Feature Analysis** - Core features, AI capabilities, gaps
3. **Technical Architecture** - API quality, integrations, data portability
4. **User Experience** - Ease of use, learning curve, real user feedback
5. **Pricing & TCO** - All costs including hidden fees, 3-year model
6. **Security & Compliance** - Certifications, uptime, incident history
7. **Support & Services** - Response times, implementation support
8. **Implementation Risks** - What could go wrong, mitigation strategies
9. **Decision Matrix** - Weighted scoring against criteria
10. **Strategic Recommendation** - SWOT, fit analysis, go/no-go
11. **Next Steps** - Action plan and timeline

**Time investment:** 2-4 hours per tool for comprehensive analysis.

**Research approach:**
- Start with vendor documentation and pricing
- Check G2/Capterra/TrustRadius reviews (focus on companies your size)
- Look for third-party analyst reports (Gartner, Forrester)
- Find real user discussions (Reddit, LinkedIn, Twitter)
- Verify security/compliance claims
- Check status pages for actual uptime

### Step 4: Compare & Score

After researching all tools:

**Create comparison matrices:**
- Feature availability and quality side-by-side
- Pricing at your scale (include all costs)
- Integration capabilities with your critical tools
- Support quality and response times

**Score each tool:**
- Use weighted criteria (defined in decision context)
- Score 1-5 on each criterion
- Calculate weighted totals
- Check deal-breakers (must-haves)

**Identify trade-offs:**
- "Tool A is easier to use but lacks advanced features"
- "Tool B is more expensive but includes modules that cost extra elsewhere"
- "Tool C has the best API but weakest support"

### Step 5: Deliver Recommendation

Structure your deliverable:

**Executive Summary** (2-3 paragraphs)
- One paragraph per tool with key finding
- Bottom-line recommendation
- Critical decision factors

**Detailed Analysis** (15,000-25,000 words)
- Complete template for each tool
- All 11 sections thoroughly covered
- Evidence and sources throughout

**Side-by-Side Comparison**
- Feature matrices
- Pricing comparison
- Trade-off analysis
- Category winners

**Final Recommendation**
- Clear winner with rationale
- Implementation approach
- Risk mitigation plan
- Decision timeline and next steps

## Research Quality Standards

### Source Hierarchy

Prioritize sources in this order:
1. **Official vendor documentation** - Pricing, features, security
2. **Third-party reviews** - G2, Capterra, TrustRadius (focus on similar companies)
3. **Analyst reports** - Gartner, Forrester (if available)
4. **Community discussions** - Reddit, LinkedIn, product forums
5. **News articles** - Recent developments, acquisitions, funding

### What "Deep Research" Actually Means

**Surface-level (DON'T DO THIS):**
> "HubSpot offers email marketing, CRM, and sales automation. Pricing starts at $15/month. It integrates with many tools."

**Deep research (DO THIS):**
> "HubSpot's Marketing Hub starts at $15/user/month (2-seat minimum = $30/month), but email marketing is limited to 1,000 sends/month at this tier. Based on 247 G2 reviews from 50-100 employee companies, the $800/month Professional tier is where most businesses land for unlimited contacts and advanced automation. Users praise the email builder (4.5/5 average) but complain about workflow automation's learning curve (3.2/5) and frequent price increases (mentioned in 23% of recent reviews). Salesforce integration requires $50/month Operations Hub add-on and users report 5-15 minute sync delays. Total 3-year TCO for our needs: $43,800 including $5,000 implementation and $800/year extra storage."

**Key differences:**
- Specific numbers with context (2-seat minimum, 1,000 sends limit)
- Evidence from reviews (247 reviews, specific ratings)
- Hidden costs identified (Operations Hub add-on)
- Real limitations noted (sync delays)
- Total cost calculated (3-year TCO)

### Always Include

For every claim:
- **Source**: Where did you find this? (URL if possible)
- **Date**: When was this information current? (e.g., "as of November 2025")
- **Confidence**: Verified/Likely/Estimated/Unknown

When information conflicts:
- Note the discrepancy explicitly
- Use most recent official source as truth
- Explain why one source is more reliable

### Red Flags to Watch For

**Company Health:**
- Recent layoffs or executive departures
- Funding concerns or acquisition rumors
- Declining Glassdoor ratings
- Market share loss to competitors

**Product Quality:**
- No meaningful updates in 12+ months
- Frequent bugs mentioned in recent reviews
- Features promised but not delivered
- Declining review scores over time

**Pricing:**
- Frequent price increases (>10% annually)
- Many reviews mentioning surprise charges
- Unclear or changing pricing structure
- Hidden fees not disclosed upfront

**Support:**
- Consistently poor support reviews
- Response times increasing over time
- Support moved offshore with quality issues
- Long ticket resolution times

**User Experience:**
- "Used to be great, now it's..." patterns
- Consistent UI/UX complaints
- High learning curve with poor training
- Mobile app rated poorly

## Using the Template

### Loading the Template

When ready to start systematic research, load `references/template.md`:

```bash
view references/template.md
```

The template provides 11 comprehensive sections to complete for each tool.

### Section Priority Guide

**Required for all research:**
- Section 1: Company & Product Foundation
- Section 2: Feature Analysis
- Section 5: Pricing & TCO
- Section 9: Decision Matrix
- Section 10: Strategic Recommendation

**Required for technical decisions:**
- Section 3: Technical Architecture
- Section 8: Implementation Risks

**Required for enterprise/compliance:**
- Section 6: Security & Compliance
- Section 7: Support & Services

**Optional (but valuable):**
- Section 4: User Experience (if adoption is a concern)
- Section 11: Next Steps (always helpful for action planning)

### Adapting for Different Tools

**SaaS platforms:** Complete all sections
**APIs/Developer tools:** Focus on Sections 3, 6, 7
**Enterprise software:** Heavy emphasis on Sections 6, 7, 8
**Workflow automation:** Emphasize Sections 2, 3, 4

### Time Management

- **Simple decision (2 similar tools, clear requirements):** 3-4 hours total
- **Standard decision (3 tools, moderate complexity):** 6-12 hours total
- **Complex decision (4-5 tools, many requirements):** 12-20 hours total

**Work iteratively:** Research one section across all tools before moving to next section. This makes comparison easier and ensures consistency.

## Quality Checklist

Before delivering research, verify:

### Completeness
- [ ] All required sections completed for each tool
- [ ] Every critical requirement explicitly evaluated
- [ ] All comparison tables filled out
- [ ] Clear recommendation provided with rationale

### Accuracy
- [ ] All pricing includes dates (e.g., "as of November 2025")
- [ ] Source URLs provided for key claims
- [ ] Review counts and ratings are current
- [ ] No contradictory information left unresolved
- [ ] Confidence levels indicated for estimates

### Depth
- [ ] Goes beyond marketing materials
- [ ] Includes real user experiences (specific examples)
- [ ] Identifies hidden costs and limitations
- [ ] Addresses implementation risks
- [ ] Quantifies claims (not just "many users say...")

### Objectivity
- [ ] Presents both strengths and weaknesses
- [ ] Doesn't parrot vendor marketing
- [ ] Acknowledges information gaps
- [ ] Separates facts from opinions
- [ ] Provides balanced perspective

### Utility
- [ ] Actionable recommendations
- [ ] Clear next steps with timeline
- [ ] Specific to the use case
- [ ] Decision-ready analysis
- [ ] Answers all key stakeholder questions

## Reference Files

### references/template.md
**When to load:** At the start of systematic research for each tool.

**What it contains:** Complete 11-section research framework with detailed guidance for each section, tables to fill out, and examples throughout.

**How to use:** Work through sections sequentially, completing all applicable parts. Takes 2-4 hours per tool.

### references/quality-guide.md
**When to load:** When validating research quality or when unsure what "deep research" means.

**What it contains:** Concrete examples of good vs bad research, red flag lists by category, and quality standards.

**How to use:** Reference while researching to ensure you're meeting quality standards. Use final checklist before delivering.

## Common Pitfalls to Avoid

**Parroting marketing claims:**
- Don't just copy feature lists from vendor websites
- Verify claims through reviews and third-party sources
- Look for gap between promises and reality

**Missing hidden costs:**
- Implementation fees
- Premium support charges
- Storage/API overages
- Required add-on modules
- Price escalation clauses

**Ignoring negative signals:**
- Bad reviews from companies your size
- Declining review scores over time
- Support quality complaints
- Security incident history

**Insufficient comparison:**
- Research tools in isolation
- Don't create direct comparison matrices
- Fail to identify clear trade-offs
- No weighted scoring methodology

**Weak recommendations:**
- Hedge without taking a position
- Fail to explain reasoning
- Don't address implementation risks
- No clear next steps

## Tips for Effective Research

**Start broad, then narrow:**
- Begin with vendor docs and pricing
- Check aggregate review sites
- Deep-dive into relevant reviews
- Find specific user stories and edge cases

**Focus on similar companies:**
- Filter reviews by company size
- Look for your industry specifically
- Check use cases that match yours
- Success stories in similar contexts

**Be skeptical of extremes:**
- Both 5-star and 1-star reviews may be outliers
- Look for patterns in 3-4 star reviews
- Weight recent reviews more heavily
- Check if negative issues were resolved

**Quantify everything possible:**
- Specific user counts, not "many users"
- Exact prices including all fees
- Actual response times from reviews
- Real uptime numbers from status pages

**Track your sources:**
- Save URLs as you go
- Note when information was published
- Distinguish verified facts from estimates
- Document where data gaps exist

## Example Usage Flow

**User asks:** "Help me choose between HubSpot, Salesforce, and Pipedrive for our 50-person sales team. Budget is $100K over 3 years."

**Claude response:**
1. "I'll conduct comprehensive research using strategic analysis methodology. Let me first gather some context..." [Asks 3-4 clarifying questions about requirements, timeline, critical integrations]

2. "I'll create a customized research plan..." [Runs init_research.py to generate tailored brief]

3. "Beginning systematic research on all three tools. This will take some time as I work through 11 key areas for each platform..." [Loads template, begins research]

4. "I've completed detailed analysis of all three platforms. Let me provide my findings..." [Delivers executive summary + full analysis + comparison + recommendation]

**Expected deliverable:** 20,000-30,000 word comprehensive analysis with clear recommendation, scoring matrices, and implementation plan.

## When to Stop vs Go Deeper

**Stop and deliver when:**
- All critical requirements have clear answers
- Scoring shows clear winner (>10 point gap)
- No significant unknowns remain
- Stakeholder questions can all be answered

**Go deeper when:**
- Tools score within 5 points of each other
- Major unknowns exist (pricing, integration capability)
- High-risk decision (expensive, hard to reverse)
- Stakeholders have conflicting requirements

**Escalate to user when:**
- Missing critical information not publicly available
- Need vendor demos or reference calls
- Technical proof-of-concept required
- Contract negotiation needed for custom pricing

---

**Remember:** This is strategic due diligence, not a quick comparison. Quality matters more than speed. A thorough analysis that takes 8-12 hours is better than a rushed analysis that leads to a $100K mistake.
