# Scoring Criteria Reference

Detailed rubrics for each scoring dimension.

## Business Impact (Weight: 35%)

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

## Effort (Weight: 25%, Inverted)

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

## Risk (Weight: 15%, Inverted)

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

## Reuse Potential (Weight: 15%)

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

## Strategic Fit (Weight: 10%)

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

## Classification Logic

| Classification | Criteria | Timeline |
|----------------|----------|----------|
| Quick Win | Score ≥7.0 AND Effort ≤5 AND Risk ≤4 | 2-4 weeks |
| Strategic Build | Impact ≥8 AND Score ≥6.5 | 4-8 weeks |
| Foundation Builder | Reuse ≥7 AND Score ≥6.0 | 3-6 weeks |
| Research/Explore | High uncertainty on any dimension | Validate first |
| Defer | Score <5.0 | Document only |

**Portfolio Balance Targets:**
- Quick Wins: 20-30% (build momentum)
- Strategic Builds: 15-25% (drive value)
- Foundation Builders: 30-40% (enable future)
- Research: 5-10% (explore potential)
