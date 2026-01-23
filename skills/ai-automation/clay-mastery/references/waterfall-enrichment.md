# Waterfall Enrichment

Waterfall enrichment is Clay's signature capability—sequential queries across multiple data providers until valid data is found, then stops to save credits.

## Table of Contents
1. [How Waterfalls Work](#how-waterfalls-work)
2. [Email Provider Rankings](#email-provider-rankings)
3. [Phone Provider Rankings](#phone-provider-rankings)
4. [Firmographic & Technographic Providers](#firmographic--technographic-providers)
5. [Building Custom Waterfalls](#building-custom-waterfalls)
6. [Optimal Provider Ordering](#optimal-provider-ordering)
7. [Coverage vs Cost Tradeoffs](#coverage-vs-cost-tradeoffs)

---

## How Waterfalls Work

**Sequential query logic:**
1. Provider A queried → returns no data → credits refunded → moves to Provider B
2. Provider B finds data → email verification runs (ZeroBounce default)
3. If verification fails or catch-all (optional) → continues to Provider C
4. Process continues until valid match OR all providers exhausted
5. Final result populates consolidated output column

**Key mechanics:**
- Users can reorder, add, or delete providers in any waterfall
- Clay provides pre-optimized default sequences for common data types
- Custom configurations can be saved as reusable "waterfall templates"
- Individual providers can be toggled on/off without removing them
- Credits only charged on successful data return (with some exceptions)

**Credit refund rules:**
- ✅ Refunded: Provider returns no data
- ✅ Refunded: Provider returns error
- ❌ NOT refunded: Invalid email returned (failed verification)
- ❌ NOT refunded: Catch-all email (unless configured to continue)

---

## Email Provider Rankings

Based on Clay's benchmark testing across 4,000+ contacts:

| Rank | Provider | Credits | Coverage | Best For |
|------|----------|---------|----------|----------|
| 1st | **Prospeo** | 2 | Highest | Overall best, real-time catch-all validation |
| 2nd | **Dropcontact** | 2 | Excellent | European coverage, GDPR compliant |
| 3rd | **Datagma** | 2 | Very Good | Also strong for phone numbers |
| 3rd | **Findymail** | 2 | Very Good | Tied with Datagma |
| 4th | **Hunter.io** | 2 | Good | Well-established, reliable |
| 5th | **People Data Labs** | 5 | Good | More expensive but comprehensive |
| 6th | **Nymblr** | 2 | Decent | Reasonable coverage |
| 7th | **Snov.io** | 2 | Decent | Good budget option |
| 8th | **Apollo** | 2 | Varies | Good for tech companies |

**Recommended email waterfall (B2B services):**
```
Prospeo → Dropcontact → Datagma → Hunter → Apollo → People Data Labs → ZeroBounce verification
```

**Geographic considerations:**
- **US-focused:** Prospeo → Apollo → Hunter → PDL
- **Europe-focused:** Dropcontact → Prospeo → Datagma
- **Global:** Full waterfall with all providers

**Company size considerations:**
- **SMB (< 100 employees):** Prospeo and Datagma perform best
- **Mid-market (100-1000):** All providers relatively equal
- **Enterprise (1000+):** Apollo and PDL have better coverage

---

## Phone Provider Rankings

Mobile numbers are expensive because they're difficult to source:

| Provider | Credits | Best Use Case | Notes |
|----------|---------|---------------|-------|
| Base search | 2 | Starting point | Lowest cost, try first |
| Apollo | 3 | Tech companies | Good US coverage |
| Lusha | 4 | B2B direct dials | Strong for sales roles |
| People Data Labs | 5 | Comprehensive | Good fallback |
| RocketReach | 10 | Last resort | Expensive but wide |
| Selligence | 13 | Premium data | High accuracy claims |
| ContactOut | 15 | LinkedIn → mobile | Best for social profiles |
| Datagma | 25 | Highest accuracy | Most expensive |

**Recommended phone waterfall:**
```
Base search → Apollo → Lusha → RocketReach → Validation
```

**Important:** Phone enrichment often has low coverage (30-50%). Set expectations accordingly.

---

## Firmographic & Technographic Providers

| Provider | Credits | Data Type | Notes |
|----------|---------|-----------|-------|
| **Clearbit (Find Domain)** | **0 FREE** | Company name → domain | Always use first |
| Clearbit Enrich | 8 | 100+ attributes | Revenue, headcount, funding |
| **BuiltWith** | 2 | Technology stack | What tools they use |
| HG Insights (tech) | 8 | Detailed tech data | Enterprise-grade |
| HG Insights (company) | 4 | Company enrichment | Firmographics |
| People Data Labs | 5 | Person + company | Comprehensive |
| Harmonic | 3 | Startup data | Funding, growth signals |
| Crunchbase | 5 | Funding details | Investment history |

**Recommended firmographic waterfall:**
```
Clearbit Find Domain (FREE) → Clearbit Enrich → Harmonic → PDL
```

**Recommended technographic waterfall:**
```
BuiltWith → HG Insights
```

---

## Building Custom Waterfalls

**When to customize vs use prebuilt:**
- Use prebuilt for standard email/phone finding
- Customize when targeting specific industries or geographies
- Customize when cost optimization is critical

**Creating a custom waterfall:**
1. Add enrichment column → Select "Waterfall" type
2. Choose data type (email, phone, company)
3. Click "Customize" to reorder providers
4. Drag providers to desired order (cheapest first)
5. Toggle off providers you don't want
6. Save as template for reuse

**Testing methodology:**
1. Run on 50 diverse rows
2. Track: hit rate per provider, cost per valid result
3. Remove providers with < 5% incremental coverage
4. Reorder based on cost-effectiveness

---

## Optimal Provider Ordering

**The golden rule:** Order providers cheapest-to-most-expensive, with highest-coverage providers first among equals.

**Email waterfall optimization:**
```
Tier 1 (2 credits): Prospeo → Dropcontact → Datagma → Findymail → Hunter
Tier 2 (3-5 credits): Apollo → People Data Labs
Tier 3 (verification): ZeroBounce (included)
```

**Why this order works:**
1. Prospeo has highest hit rate at lowest cost
2. Each subsequent provider catches what others missed
3. PDL is expensive but catches edge cases
4. Verification runs on ALL results automatically

**Industry-specific adjustments:**
- **Tech startups:** Move Apollo earlier (good startup coverage)
- **Professional services:** Move Hunter earlier (good for consultants, lawyers)
- **Healthcare:** Datagma performs well
- **Finance:** PDL has strong coverage

---

## Coverage vs Cost Tradeoffs

**Diminishing returns analysis:**

| Providers Used | Typical Coverage | Avg Cost/Contact |
|----------------|------------------|------------------|
| 1 provider | 40-50% | 2 credits |
| 2 providers | 55-65% | 3 credits |
| 3 providers | 65-75% | 4 credits |
| 5+ providers | 75-85% | 6+ credits |

**When to stop the waterfall:**
- **High-volume outbound:** Stop at 65-70% coverage (cost-effective)
- **ABM/high-value accounts:** Run full waterfall (coverage matters more)
- **Inbound enrichment:** Run full waterfall (already qualified leads)

**Fallback strategies when waterfall exhausts:**
1. **Claygent research:** Use AI to find email patterns on company website
2. **Domain pattern guessing:** first.last@domain.com, firstl@domain.com
3. **LinkedIn outreach:** Switch to InMail for unreachable contacts
4. **Skip and prioritize:** Focus on contacts with data

**Cost-per-qualified-lead calculation:**
```
(Total credits used × Cost per credit) ÷ Leads with valid email = Cost per qualified lead

Example: (500 credits × $0.035) ÷ 350 valid emails = $0.05 per lead
```

---

## Provider-Specific Notes

**Prospeo:**
- Real-time validation included
- Best overall performer in Clay's testing
- Handles catch-all domains well

**Dropcontact:**
- GDPR compliant (important for EU prospects)
- Strong for .fr, .de, .uk domains
- No LinkedIn data dependency

**Apollo:**
- Excellent for tech companies
- Sometimes returns `email_not_unlocked@domain.com` (need additional step)
- Good phone coverage too

**People Data Labs:**
- Most comprehensive database
- Higher cost but catches edge cases
- Good for enterprise contacts

**Hunter.io:**
- Well-established, reliable
- Good email pattern detection
- Limited phone data

**BuiltWith:**
- Only provider for detailed tech stacks
- Shows historical technology changes
- Useful for competitive intelligence
