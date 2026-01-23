---
name: competitive-intelligence
description: Gather and analyze competitor information, create battle cards, build competitive matrices, and conduct win/loss analysis. Use when monitoring competitors, creating sales enablement materials, analyzing competitive landscape, or when the user mentions battle cards, competitive analysis, win/loss, market research, or competitor monitoring.
---

# Competitive Intelligence

Systematic gathering, analysis, and distribution of competitor information to inform strategy and enable sales teams.

## Quick Reference

| Asset | Purpose | When to Use |
|-------|---------|-------------|
| Battle Card | Sales enablement for competitive deals | Active sales situations |
| Competitive Matrix | Feature/capability comparison | Positioning, strategy |
| Win/Loss Analysis | Learn from deal outcomes | Continuous improvement |
| CI Dashboard | Ongoing monitoring | Regular updates |

## The CI Cycle

```
1. ORIENT → 2. IDENTIFY → 3. COLLECT → 4. ANALYZE → 5. DISTRIBUTE
     ↑                                                      │
     └──────────────────────────────────────────────────────┘
                        (Continuous)
```

### Step 1: Orient (Define Objectives)
Before collecting data, define what you need to know and why.

**Key Questions:**
- What business decisions will this inform?
- Who needs this intelligence?
- What's the urgency/timeline?

### Step 2: Identify Competitors

**Competitor Types:**
| Type | Definition | Example |
|------|------------|---------|
| Direct | Same product, same market | Coke vs. Pepsi |
| Indirect | Different product, same problem | Uber vs. public transit |
| Aspirational | Market leader to benchmark | Startup vs. industry leader |
| Perceived | Who prospects mention | Based on sales conversations |

**Jobs-to-be-Done Lens:** What is the customer trying to accomplish? Who else helps them do that?

### Step 3: Collect Data

**Source Priority:**
1. **Primary** - Win/loss interviews, sales feedback, customer conversations
2. **Digital** - Competitor websites, social media, review sites
3. **Technical** - Web scraping, API monitoring, SEO tools
4. **Market** - Similarweb, SEMrush, industry reports
5. **Human** - Conferences, earnings calls, job postings

### Step 4: Analyze

Transform data into actionable insights:
- Create competitor profiles and battle cards
- Build feature comparison matrices
- Identify patterns in win/loss data
- Apply frameworks (Porter's, SWOT)

### Step 5: Distribute

Get insights to people who need them:
- Integrate with CRM (Salesforce, HubSpot)
- Slack channels for real-time alerts
- Regular CI newsletters/digests
- Training and enablement sessions

---

## Battle Card (Quick Start)

Battle cards help sales reps win competitive deals. Use the **FIA Framework**: Fact → Impact → Act.

### Essential Sections

```markdown
# [Competitor Name] Battle Card

**Last Updated:** [Date]
**Win Rate Against:** [X%]

## Quick Take (30 seconds)
[One-liner positioning]

## When We Win
- [Differentiator 1 with proof]
- [Differentiator 2 with proof]

## When We Lose (Be Honest)
- [Their strength 1] → Our response: [How to handle]
- [Their strength 2] → Our response: [How to handle]

## Key Objections

### "[Their claim]"
**Trap Question:** [Question to expose weakness]
**Response:** [What to say]

## Pricing Intelligence
- Model: [Subscription/Usage/etc.]
- Entry: [$X/mo]
- Discounting: [When they discount]
```

See `references/battle-card-template.md` for complete template.

---

## Competitive Matrix (Quick Start)

Compare features/capabilities across competitors.

### Basic Template

```markdown
| Feature | Us | Competitor A | Competitor B | Why It Matters |
|---------|------|--------------|--------------|----------------|
| [Feature 1] | ✓✓ | ✓ | ✗ | [Customer impact] |
| [Feature 2] | ✓ | ✓✓ | ✓ | [Customer impact] |

Legend: ✓✓ Advanced | ✓ Basic | ⊕ Add-on | ○ Roadmap | ✗ Not available
```

See `references/competitive-matrix.md` for full templates.

---

## Monitoring Cadence

### What to Track

| Priority | What | Frequency |
|----------|------|-----------|
| Critical | Pricing, product launches, major news | Daily/Weekly |
| Important | Marketing campaigns, content, reviews | Weekly |
| Contextual | Hiring patterns, org changes, patents | Monthly |

### Automation Tips
- Set up Google Alerts for competitor names
- Use tools like Visualping for website change detection
- Monitor job boards for strategic signals
- Track G2/Capterra for review sentiment

See `references/monitoring-cadence.md` for detailed guide.

---

## Win/Loss Analysis (Quick Start)

Learn from deal outcomes to improve competitive position.

### Interview Timing
- 2-4 weeks after decision (fresh but with perspective)
- Use neutral interviewer (not the sales rep)
- 20-30 minutes, 10 questions max

### Essential Questions

**For Wins:**
1. What factors made you choose us over competitors?
2. Which competitors did you seriously evaluate?
3. Was there anything that nearly made you choose another provider?

**For Losses:**
1. What were the main reasons you didn't choose us?
2. Which competitor did you select, and why?
3. Was there anything we could have done differently?

See `references/win-loss-analysis.md` for complete methodology.

---

## Common Mistakes

### Battle Cards
- Too much background, not enough action items
- Neutral language (give content positive/negative charge)
- No "so what?" for your offering
- Rarely updated (should be at least quarterly)

### Competitive Analysis
- Only tracking direct competitors (miss disruptors)
- Collecting data without acting on it
- "Rose-colored glasses" (overestimate self, underestimate competitors)
- Siloed insights (not sharing across teams)

### Win/Loss
- Sales rep conducts interview (biased)
- Only analyzing wins (losses are more valuable)
- Surface-level answers ("better product" - dig deeper!)
- Not tagging themes for pattern analysis

---

## Resources

- `references/battle-card-template.md` - Complete FIA battle card template
- `references/competitive-matrix.md` - Feature comparison templates
- `references/monitoring-cadence.md` - What to track and how often
- `references/win-loss-analysis.md` - Interview methodology and questions
- `references/pricing-intelligence.md` - Pricing research framework

---

## Version History

- v1.0.0 (2026-01-08): Initial version with battle cards, matrices, win/loss
