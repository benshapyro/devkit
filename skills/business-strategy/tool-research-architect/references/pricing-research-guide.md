# Pricing Research Guide

## Overview

Accurate, current pricing information is critical for client recommendations and ROI calculations. This guide helps you find and document pricing systematically.

## Priority Source Hierarchy

### 1. Official Pricing Page (Always Check First)

**Where to find:**
- domain.com/pricing
- domain.com/plans
- domain.com/buy
- pricing.[domain].com

**Why it's most reliable:**
- Most up-to-date information
- Directly from the vendor
- Legal implications keep it accurate

**What to capture:**
- All tier names and prices
- Billing frequency options (monthly/annual)
- What's included in each tier
- Free tier or trial information
- Any disclaimers or fine print

### 2. Official Documentation

**Where to find:**
- docs.[domain].com
- help.[domain].com
- support.[domain].com

**Best for:**
- API pricing details
- Usage-based pricing calculations
- Enterprise tier details
- Implementation costs

### 3. Sales/Contact Forms (When Custom Pricing)

**When to use:**
- Enterprise tier shows "Contact Sales"
- No public pricing available
- Tool is high-touch/high-value

**How to document:**
```markdown
**Enterprise:** Custom pricing via sales
- Contact required at domain.com/contact
- Estimated $X,000-$Y,000/year based on similar tools in category
```

### 4. Third-Party Sources (Use Cautiously)

**Sources:**
- G2, Capterra, Software Advice
- TrustRadius, GetApp
- Tech review sites

**Important caveats:**
- Often outdated (6-12 months behind)
- May not reflect current pricing
- Good for historical context only
- ALWAYS verify with official sources

**How to use:**
- Cross-reference with official pricing
- Note if discrepancies exist
- Use only when official pricing unavailable

## Date Sensitivity is CRITICAL

### Why Dates Matter

- Pricing changes frequently (quarterly or annually)
- New tiers get added or removed
- Promotions expire
- Currency exchange rates fluctuate
- Inflation adjustments happen

### How to Include Dates

**✓ Good examples:**
- "$29/user/month (as of November 2025)"
- "Free tier available (verified Oct 2024)"
- "Pricing updated September 2024"
- "Annual discount: 20% (confirmed Nov 23, 2025)"

**✗ Bad examples:**
- "$29/user/month" (no date)
- "Recent pricing" (too vague)
- "Current as of research" (not specific)

### Red Flags for Outdated Pricing

- Third-party sites with no "Last Updated" date
- Pricing pages without copyright year
- Screenshots from old reviews (check image dates)
- Forum discussions older than 6 months
- Cached versions of websites

## Common Pricing Models

### Per-User Subscription (Most Common)

**Pattern:**
```markdown
**Pricing Model:** Per-user subscription (monthly or annual)
- **Free Plan:** $0 - Limited to 2 users, basic features only
- **Starter:** $12/user/month ($10/month billed annually) - Core features, 10 projects
- **Professional:** $25/user/month ($20/month billed annually) - Advanced features, unlimited projects
- **Enterprise:** Custom pricing - SSO, dedicated support, SLA guarantees
```

**Key details to capture:**
- Per-user cost
- Monthly vs. annual pricing
- Minimum seat requirements
- What's included at each tier

### Freemium Model

**Pattern:**
```markdown
**Pricing Model:** Freemium (free tier + paid upgrades)
- **Free:** $0 forever - 1GB storage, basic features, 2 user limit
- **Premium:** $10/month - 100GB storage, priority support, no ads
- **Teams:** $25/user/month - Shared workspace, admin controls, 1TB storage
```

**Key details to capture:**
- Free tier limitations (users, storage, features)
- Whether credit card required for free tier
- Upgrade trigger points

### Usage-Based (API, Transactions)

**Pattern:**
```markdown
**Pricing Model:** Usage-based (pay per API call/transaction)
- **Free Tier:** $0 - 1,000 API calls/month included
- **Pay-as-you-go:** $0.01 per API call beyond free tier
- **Volume Discount:** $0.005 per call at 100k+/month
- **Enterprise:** $0.002 per call at 1M+/month, annual contract
```

**Key details to capture:**
- Free tier allocation
- Cost per unit (call, transaction, GB, etc.)
- Volume discount breakpoints
- Overage charges

### Flat Rate (Unlimited Users)

**Pattern:**
```markdown
**Pricing Model:** Flat monthly rate (unlimited users within team size)
- **Small Team:** $49/month - Up to 10 users, 50GB storage
- **Business:** $199/month - Up to 50 users, 500GB storage
- **Enterprise:** $499/month - Unlimited users, unlimited storage, priority support
```

**Key details to capture:**
- Fixed monthly/annual cost
- User limits for each tier
- Storage or feature caps

### One-Time Purchase (Perpetual License)

**Pattern:**
```markdown
**Pricing Model:** One-time purchase (perpetual license)
- **Standard:** $299 one-time - Includes 1 year of updates
- **Professional:** $599 one-time - Advanced features, lifetime updates
- **Maintenance:** $99/year optional - Continued updates and support
```

**Key details to capture:**
- One-time cost
- What updates/support are included
- Maintenance/support renewal costs

### Hybrid Models

**Pattern:**
```markdown
**Pricing Model:** Hybrid (base subscription + usage charges)
- **Base:** $99/month - Platform access, 10,000 API calls included
- **Additional usage:** $0.02 per API call beyond included amount
- **Enterprise:** $999/month - Unlimited API calls, priority support
```

## What to Document - Complete Checklist

### Essential Information

**1. Pricing Structure**
- [ ] How billing works (per-user, flat rate, usage-based)
- [ ] Billing frequency options (monthly, annual, one-time)
- [ ] Discounts available (annual vs. monthly)

**2. Starting Price**
- [ ] Lowest price point to get started
- [ ] What's included at this tier
- [ ] Limitations or restrictions

**3. Free Tier (if available)**
- [ ] Exact limitations (users, storage, features)
- [ ] Trial period vs. permanent free tier
- [ ] Whether credit card required
- [ ] Upgrade trigger points

**4. Minimum Commitments**
- [ ] Seat minimums ("3-seat minimum")
- [ ] Contract terms ("annual contract required")
- [ ] Setup fees or implementation costs
- [ ] Cancellation terms if notable

**5. Mid-Tier Options**
- [ ] Names of each tier
- [ ] Price at each level
- [ ] Key features differentiating tiers
- [ ] Sweet spot for most users

**6. Enterprise Pricing**
- [ ] Whether custom pricing available
- [ ] Typical features requiring enterprise tier
- [ ] Estimated price range if known
- [ ] Sales contact process

### Example: Complete Pricing Documentation

```markdown
**Pricing Model & Starting Price:** Per-user subscription (monthly or annual, 15% discount on annual)

- **Free Plan:** $0 - Limited to 2 users, 5 projects max, 1GB storage per user
  - No credit card required
  - Upgrade required for team features

- **Starter:** $12/user/month ($10.20/user/month billed annually)
  - Minimum 3 seats required ($36/month minimum)
  - Includes: 10 users max, unlimited projects, 10GB storage per user
  - Core features: Task management, basic reporting, mobile app

- **Professional:** $25/user/month ($21.25/user/month billed annually)
  - No minimum seats
  - Includes: Unlimited users, advanced analytics, 100GB storage per user
  - Additional features: Priority support, custom integrations, API access

- **Enterprise:** Custom pricing via sales (typical range: $50-75/user/month)
  - Contact: sales@domain.com
  - Includes: SSO, dedicated account manager, SLA guarantees, unlimited storage
  - Setup fee: ~$2,000 (quoted separately)
  - Annual contract required

**Free Trial:** 14-day trial of Professional plan features (no credit card required)

**Additional Costs:**
- Premium integrations: $5-15/month per integration
- Extra storage: $5/month per 100GB

*(Pricing verified November 23, 2025 from domain.com/pricing)*
```

## Research Process

### Step 1: Go Directly to Official Pricing Page (3 minutes)

**Actions:**
1. Visit domain.com/pricing or domain.com/plans
2. Screenshot for reference if complex
3. Note the date on the page (footer, copyright)
4. Check for any promotional banners or temporary pricing

**Capture:**
- All visible tier names and prices
- Key features at each tier
- Any disclaimers or fine print

### Step 2: Check for Hidden Details (2 minutes)

**Actions:**
1. Scroll to FAQ section on pricing page
2. Look for fine print about minimums
3. Check for asterisks (*) indicating additional terms
4. Click "View details" or expandable sections

**Common hidden details:**
- Seat minimums
- Annual commitment requirements
- Implementation fees
- Add-on costs

### Step 3: Verify Current Date (1 minute)

**Actions:**
1. Check page footer for copyright year
2. Look for "Updated [date]" indicators
3. Compare with cached/archived versions if suspicious
4. Check blog for recent pricing announcements

**Red flags:**
- Copyright year is old (2022 or earlier)
- Design looks outdated
- Promotions reference old dates

### Step 4: Cross-Reference if Available (2 minutes)

**Actions:**
1. Check multiple sources for same price
2. Verify across pricing calculators if available
3. Compare monthly vs. annual (should show discount)
4. Look for user reviews mentioning recent pricing

**Discrepancy handling:**
- Official source always wins
- Note if third-party sources differ
- Explain likely reason for difference

### Step 5: Document Uncertainties (1 minute)

**Actions:**
1. Mark anything requiring "Contact Sales"
2. Note estimated ranges when exact pricing unavailable
3. Flag regional variations if applicable
4. Call out recent changes if discovered

## Special Situations

### Situation 1: "Contact Sales" Only

```markdown
**Pricing Model:** Custom pricing (contact sales for quote)
- No public pricing available
- Typically enterprise-focused
- Sales contact: sales@domain.com or domain.com/contact
- Estimated range: $500-$5,000/month based on similar enterprise tools in category

**Note:** Tool does not publish standard pricing. Quotes are customized based on company size, usage, and requirements.
```

### Situation 2: Regional Pricing Variations

```markdown
**Pricing Model:** Per-user subscription (pricing varies by region)

**North America:**
- Professional: $25/user/month (USD)
- Enterprise: $50/user/month (USD)

**Europe:**
- Professional: €23/user/month (EUR)
- Enterprise: €45/user/month (EUR)

**UK:**
- Professional: £20/user/month (GBP)
- Enterprise: £40/user/month (GBP)

**Note:** Prices shown are for respective regions. Currency conversion not 1:1 due to VAT and regional pricing strategies.

*(Pricing verified November 2025 across regional sites)*
```

### Situation 3: Recent Pricing Changes

```markdown
**Pricing Model:** Per-user subscription (recently updated)

**Current Pricing (as of October 2024):**
- Professional: $25/user/month
- Enterprise: $50/user/month

**Note:** Pricing increased 40% in October 2024 (previous: $15/user and $30/user respectively). Existing customers grandfathered at previous rates through December 2025. Announcement: blog.domain.com/pricing-update-2024

*(Verified November 23, 2025)*
```

### Situation 4: Academic/Nonprofit Discounts

```markdown
**Pricing Model:** Per-user subscription with special pricing

**Standard Pricing:**
- Professional: $25/user/month
- Enterprise: $50/user/month

**Academic/Nonprofit Pricing:**
- Professional: $12.50/user/month (50% discount)
- Enterprise: $25/user/month (50% discount)
- Verification required: .edu email or 501(c)(3) documentation

**Apply:** domain.com/academic-pricing

*(Pricing verified November 2025)*
```

### Situation 5: Contradictory Information

```markdown
**Pricing Model:** Per-user subscription

**Official Pricing (domain.com/pricing, verified November 23, 2025):**
- Professional: $25/user/month
- Enterprise: Custom pricing

**Note on pricing variations:** Some third-party review sites (G2, Capterra) show $20/user/month—this represents outdated pricing from before the October 2024 price increase. Always verify current pricing on official website.
```

## Time Estimation

**Per tool:**
- Simple/transparent pricing: 2-3 minutes
- Multiple products/tiers: 5-7 minutes
- Complex enterprise pricing: 4-5 minutes
- Custom pricing only: 3-4 minutes (less to document)

**By research phase:**
- Official page review: 3 min
- Hidden details: 2 min
- Date verification: 1 min
- Cross-reference: 2 min
- Documentation: 1-2 min

## Quality Checklist

Before finalizing pricing section:

- [ ] Verified on official source (not third-party)
- [ ] Included current date/verification date
- [ ] Documented free tier if it exists
- [ ] Noted any minimums or commitments
- [ ] Clarified billing frequency options (monthly/annual)
- [ ] Checked for recent changes or announcements
- [ ] Captured setup fees if significant
- [ ] Noted discount percentages for annual billing
- [ ] Explained custom/enterprise pricing process

## Common Mistakes to Avoid

### Mistake 1: Trusting Third-Party Sites

**Problem:** G2 or Capterra showing different prices

**Solution:** Always verify on official site. Note discrepancy if exists:
```
"Some third-party sites show $20/user, but official pricing is $25/user as of Nov 2025"
```

### Mistake 2: Missing Annual Discount

**Problem:** Only documenting monthly pricing

**Solution:** Always check for annual option:
```
"$25/user/month OR $20/user/month billed annually (20% savings)"
```

### Mistake 3: Ignoring Seat Minimums

**Problem:** Stating "$10/user" without noting "3-seat minimum"

**Solution:** Be explicit about true starting cost:
```
"$10/user/month (3-seat minimum: $30/month minimum commitment)"
```

### Mistake 4: Confusing Trials and Free Tiers

**Problem:** "Free plan available" when it's actually a 14-day trial

**Solution:** Distinguish clearly:
```
- **Free Tier:** $0 forever (limited features)
- **Free Trial:** 14 days of Pro plan (then $X/month)
```

### Mistake 5: Omitting Dates

**Problem:** Pricing without verification date

**Solution:** Always include date stamp:
```
"$25/user/month (pricing verified November 23, 2025)"
```

## Pro Tips for Efficiency

1. **Use templates:** Copy/paste the format from assets/output-template.md

2. **Open multiple tabs:** Official site, pricing page, docs, and blog simultaneously

3. **Use browser search:** Cmd/Ctrl+F for "pricing", "plan", "cost" on official site

4. **Check URL structure:** Often domain.com/pricing or domain.com/plans follows consistent patterns

5. **Screenshot complex pricing:** Take a screenshot for reference if pricing table is complex

6. **Note promotional pricing:** If you see "Limited time" or "Sale" banners, note the regular price too

7. **Build a comparison spreadsheet:** For batch research, maintain a spreadsheet of all tool pricing for easy cross-referencing

## Final Reminders

- **Official sources only** for final documentation
- **Dates on everything** - pricing changes frequently
- **Complete picture** - don't just grab the headline price, get the full story
- **Verification dates** - include when you checked, not when pricing was set
- **Clear about unknowns** - "Custom pricing" is better than guessing
- **Context matters** - Enterprise pricing often 2-3x standard pricing

Quality pricing research enables accurate ROI calculations and confident client recommendations.
