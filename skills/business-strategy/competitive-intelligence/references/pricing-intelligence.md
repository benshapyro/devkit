# Pricing Intelligence Guide

Framework for researching, analyzing, and responding to competitor pricing.

## Overview

Pricing intelligence helps you understand:
- How competitors price and package
- When and how they discount
- Your relative value position
- How to respond to pricing objections

## Data Collection Methods

### Public Pricing (B2C/SMB)

**Sources:**
| Source | What to Capture | Frequency |
|--------|-----------------|-----------|
| Pricing page | Tiers, features, prices | Weekly |
| Sign-up flow | Actual pricing, upsells | Monthly |
| Promotional emails | Discount patterns | As received |
| Review sites | Pricing mentions | Weekly |

**Automated Monitoring:**
- Use Visualping/Wachete on pricing pages
- Set alerts for "[competitor] pricing" news
- Monitor promotional landing pages

### Private Pricing (B2B/Enterprise)

**Sources:**
| Source | What to Capture | Method |
|--------|-----------------|--------|
| Sales conversations | Quoted prices, discounts | Win/loss interviews |
| Prospects | Competitor quotes | Ask during discovery |
| Former customers | Contract terms | Exit interviews |
| Industry contacts | Market rates | Networking |
| RFP databases | Public contract data | Research |

**Win/Loss Questions:**
- "How did our pricing compare to others?"
- "What was included at that price point?"
- "Did they offer any discounts or incentives?"

---

## Pricing Model Analysis

### Common Pricing Models

| Model | Description | Example |
|-------|-------------|---------|
| **Per Seat** | Price × number of users | $10/user/month |
| **Usage-Based** | Price tied to consumption | $0.01 per API call |
| **Tiered** | Feature bundles at price points | Starter/Pro/Enterprise |
| **Flat Rate** | Single price for all | $99/month unlimited |
| **Freemium** | Free tier + paid upgrades | Free core, paid premium |
| **Hybrid** | Combination of models | Base + per-seat + usage |

### Model Comparison Template

```markdown
# Pricing Model Comparison

## [Your Product]
- **Model:** [Per seat / Usage / Tiered / etc.]
- **Value Metric:** [What determines price]
- **Entry Price:** [$X/mo]
- **Mid-Market:** [$X/mo]
- **Enterprise:** [Custom]

## [Competitor A]
- **Model:** [Per seat / Usage / Tiered / etc.]
- **Value Metric:** [What determines price]
- **Entry Price:** [$X/mo]
- **Mid-Market:** [$X/mo]
- **Enterprise:** [Custom]
- **Key Difference:** [How their model differs]

## [Competitor B]
[Same structure]

## Implications

**Our Advantage:**
[Where our model works better for customers]

**Our Disadvantage:**
[Where competitor model is more attractive]

**Positioning:**
[How to talk about pricing differences]
```

---

## Pricing Comparison Matrix

### Template

```markdown
# Pricing Comparison: [Category]

**Data As Of:** [Date]
**Source:** [How data was gathered]

## List Price Comparison

| Tier | [Us] | [Comp A] | [Comp B] | [Comp C] |
|------|------|----------|----------|----------|
| **Entry/Starter** | | | | |
| Price | $X/mo | $Y/mo | $Z/mo | $W/mo |
| Users included | X | Y | Z | W |
| Storage/limits | X | Y | Z | W |
| **Professional/Growth** | | | | |
| Price | $X/mo | $Y/mo | $Z/mo | $W/mo |
| Users included | X | Y | Z | W |
| Key features | [List] | [List] | [List] | [List] |
| **Enterprise** | | | | |
| Price | Custom | Custom | $Z/mo | Custom |
| Starting at | ~$X/yr | ~$Y/yr | ~$Z/yr | ~$W/yr |

## What's Included (Feature Parity)

| Feature | [Us] Tier | [Comp A] Tier | [Comp B] Tier |
|---------|-----------|---------------|---------------|
| [Feature 1] | Starter | Pro | Enterprise |
| [Feature 2] | Pro | Pro | Pro |
| [Feature 3] | Enterprise | Pro | Not offered |
| [Feature 4] | Included | Add-on ($X) | Included |

## Hidden Costs

| Cost Type | [Us] | [Comp A] | [Comp B] |
|-----------|------|----------|----------|
| Implementation | $X | $Y | $Z |
| Training | Included | $X | $Y |
| Support upgrade | N/A | $X/mo | $Y/mo |
| API access | Included | $X/mo | Limited |
| Integrations | Included | $X each | Included |

## Total Cost of Ownership (Example: 50-seat deployment)

| Cost Component | [Us] | [Comp A] | [Comp B] |
|----------------|------|----------|----------|
| Annual license | $X | $Y | $Z |
| Implementation | $X | $Y | $Z |
| Training | $X | $Y | $Z |
| Support tier | $X | $Y | $Z |
| Required add-ons | $X | $Y | $Z |
| **Year 1 Total** | **$X** | **$Y** | **$Z** |
| **3-Year TCO** | **$X** | **$Y** | **$Z** |
```

---

## Discount Analysis

### Tracking Competitor Discounts

```markdown
# Discount Intelligence: [Competitor]

## Observed Discount Patterns

| Trigger | Discount Range | Evidence |
|---------|---------------|----------|
| End of quarter | 15-25% | Multiple deal reports |
| Multi-year commit | 20-30% | Win/loss interviews |
| Competitive displacement | Up to 40% | Prospect feedback |
| Annual prepay | 10-15% | Pricing page |
| Volume (100+ seats) | 20-25% | Contract data |

## Seasonal Patterns

| Period | Behavior | Our Response |
|--------|----------|--------------|
| Q4 (Oct-Dec) | Aggressive discounting to hit targets | Match competitively |
| Q1 (Jan-Mar) | Tighter discounts, focus on value | Lead with ROI |
| Q2-Q3 | Normal pricing | Standard approach |

## Discount Triggers (Red Flags)

**They Discount Aggressively When:**
- Losing to us (competitive deal)
- Prospect mentions budget concerns
- Multi-year opportunity
- Strategic logo/reference

**Our Counter-Strategy:**
- [How to respond to heavy discounting]
```

### Discount Authorization Guide

```markdown
# Internal Discount Guidelines

## Standard Authority

| Discount Level | Approval Required |
|----------------|-------------------|
| 0-10% | Sales rep authority |
| 10-20% | Manager approval |
| 20-30% | VP Sales approval |
| 30%+ | Executive approval |

## Competitive Match Guidelines

**When to Match:**
- Strategic accounts
- High reference value
- Multi-year commitment
- Large deal size

**When NOT to Match:**
- One-time discount to win; customer will expect it forever
- Signals we compete on price, not value
- Unprofitable at discount level
- Sets precedent for future deals
```

---

## Pricing Objection Handlers

### "They're Cheaper"

**Discovery:**
"What's included in that price? I want to make sure we're comparing apples to apples—including implementation, support, and any add-ons."

**Response:**
"Looking at total cost of ownership, our customers typically see [lower TCO / faster time-to-value / better ROI] because [specific reason]. [Customer X] initially thought [competitor] was cheaper, but after factoring in [specific costs], the total was actually [comparable/higher]."

**Proof:**
- TCO comparison spreadsheet
- Customer case study with ROI

### "Can You Match Their Price?"

**Discovery:**
"Help me understand—if price were exactly equal, which solution would you prefer and why?"

**Response:**
"We can discuss pricing, but I want to make sure you're getting the right solution first. [If they prefer us:] Let's talk about what we can do. [If unclear:] What would it take for price to be secondary to the value you're getting?"

**Avoid:**
- Immediately matching (devalues your offering)
- Defensive posture about pricing

### "Your Pricing Is Confusing"

**Discovery:**
"What specifically is confusing? I want to make sure you have clarity."

**Response:**
"Let me simplify: for a company your size with your needs, you're looking at [simple price quote]. The way we price is [brief explanation of model]. The reason we do it this way is [customer benefit]."

**Action:**
- Provide simple quote document
- Offer pricing call to walk through

---

## Value-Based Pricing Framework

### ROI Calculator Components

```markdown
# ROI Talking Points

## Time Savings
- [X hours saved per week per user]
- At [$Y fully loaded cost per hour]
- Annual value: $[Z]

## Error Reduction
- [X% reduction in errors]
- Average cost per error: $[Y]
- Annual savings: $[Z]

## Revenue Impact
- [X% improvement in conversion/retention/etc.]
- Revenue affected: $[Y]
- Annual impact: $[Z]

## Total Value vs. Investment

| Metric | Value |
|--------|-------|
| Annual investment | $X |
| Annual value delivered | $Y |
| ROI | X% |
| Payback period | X months |
```

### Value Positioning by Segment

| Segment | Price Sensitivity | Lead With |
|---------|-------------------|-----------|
| Enterprise | Lower | Total value, risk reduction, strategic fit |
| Mid-Market | Medium | ROI, time-to-value, TCO |
| SMB | Higher | Monthly cost, simplicity, quick wins |

---

## Competitive Price Positioning

### Price Position Matrix

```
         LOW PRICE                           HIGH PRICE
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  [Budget Option]                    [Premium]       │
    │       ●                                 ●           │
    │                                                     │
    │                    [Us]                             │
    │                     ●                               │
    │                                                     │
    │       [Comp B]              [Comp A]                │
    │          ●                     ●                    │
    │                                                     │
    └─────────────────────────────────────────────────────┘
```

### Positioning Statement by Position

**If You're Higher Priced:**
"Yes, we're not the cheapest option—and there's a reason. Our customers choose us because [specific value]. The companies that prioritize [value driver] find that [outcome]. Is that what you're optimizing for?"

**If You're Lower Priced:**
"We offer competitive pricing because [reason—efficiency, focus, etc.], not because we cut corners. You're getting [same/better] capabilities at a better value because [specific reason]."

**If You're Similar Priced:**
"We're in the same range as [competitor], so the decision really comes down to [differentiator]. Where we see customers choose us is when [scenario]."

---

## Best Practices

### Do
- Track list prices AND actual selling prices
- Include hidden costs in comparisons (implementation, support, add-ons)
- Update quarterly minimum
- Train sales on value-based selling
- Use TCO, not just list price

### Don't
- Compete purely on price (race to bottom)
- Share competitor pricing in writing (legal risk)
- Discount without getting something in return
- Assume competitor pricing is accurate (verify)
- Ignore pricing changes (react quickly)

### Ethical Guidelines

- Only use publicly available information
- Don't misrepresent yourself to get pricing
- Don't share competitor confidential pricing
- Verify data before using in sales materials
- Comply with antitrust regulations
