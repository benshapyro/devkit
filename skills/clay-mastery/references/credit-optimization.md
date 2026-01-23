# Credit Optimization

Strategies for minimizing Clay credit costs while maximizing data quality.

## Table of Contents
1. [Credit System Overview](#credit-system-overview)
2. [Credit Cost Reference](#credit-cost-reference)
3. [10 Credit-Saving Strategies](#10-credit-saving-strategies)
4. [API Key Integration (BYOK)](#api-key-integration-byok)
5. [Cost Modeling for Client Scoping](#cost-modeling-for-client-scoping)
6. [When to Upgrade Plans](#when-to-upgrade-plans)

---

## Credit System Overview

### How Credits Work
- Credits are consumed when enrichments run successfully
- Failed enrichments (no data found) are typically refunded
- Credits reset monthly based on billing cycle
- Unused credits roll over (capped at 2x monthly allocation)

### Current Pricing (December 2024)

| Plan | Monthly Cost | Credits/Month | Cost per 1K Credits |
|------|--------------|---------------|---------------------|
| Free | $0 | 100 | N/A |
| Starter | $134/mo | 2,000 | ~$67 |
| Explorer | $314/mo | 10,000 | ~$31 |
| Explorer+ | $629/mo | 20,000 | ~$31 |
| Pro | $720/mo | 50,000 | ~$14 |
| Pro+ | $1,800/mo | 150,000 | ~$12 |
| Enterprise | Custom | Custom | Negotiable |

**Key insight:** Pro tier is up to **6x cheaper per credit** than Starter.

### Rollover Rules
- Unused credits roll to next month
- Maximum rollover: 2x your monthly allocation
- Example: Pro (50K/mo) can accumulate up to 100K credits

---

## Credit Cost Reference

### Free Actions (0 Credits)

| Action | Notes |
|--------|-------|
| AI Formula Generator | Unlimited JavaScript formulas |
| Native cleaning tools | Normalize names, phones, whitespace |
| Clearbit Find Domain | Company name → domain |
| CRM imports (with API key) | HubSpot, Salesforce imports |
| CRM lookups | Check if record exists |
| CRM create/update | Push data back |
| Deduplication | Remove duplicate rows |
| Row filtering | Manual or formula-based |

### Low-Cost Actions (1-2 Credits)

| Action | Credits |
|--------|---------|
| Claygent Helium | 1 |
| Use AI (GPT-4, Claude Sonnet) | 1 |
| Email waterfall (per provider hit) | 2 |
| Prospeo | 2 |
| Dropcontact | 2 |
| Hunter | 2 |
| Datagma | 2 |
| BuiltWith | 2 |
| LinkedIn Sales Nav import | 1/row |

### Medium-Cost Actions (3-10 Credits)

| Action | Credits |
|--------|---------|
| Claygent Neon | 2 |
| Claygent Argon | 3 |
| Apollo enrichment | 3 |
| People Data Labs | 5 |
| Crunchbase | 5 |
| Clearbit Enrich | 8 |
| HG Insights (company) | 4 |
| HG Insights (tech) | 8 |

### High-Cost Actions (10+ Credits)

| Action | Credits |
|--------|---------|
| RocketReach | 10 |
| Selligence | 13 |
| ContactOut | 15 |
| Datagma Phone | 25 |
| Claygent Navigator | 6 |
| GPT-o1 | 6 |

---

## 10 Credit-Saving Strategies

### 1. Test on Small Batches First

**Never run enrichments on full table without testing.**

```
Testing progression:
5-10 rows → Verify output quality
50 rows → Confirm consistency
500 rows → Scale test
Full table → Production run
```

**Setting:** Right-click column → "Run Column" → "Choose number of rows"

### 2. Start with Companies, Not Contacts

**Company filtering saves the most credits.**

```
Wrong order (expensive):
1. Find contacts → 2. Enrich contacts → 3. Filter by company

Right order (cheap):
1. Enrich companies → 2. Filter by ICP → 3. THEN find contacts
```

**Savings:** 60-80% reduction in contact enrichment costs.

### 3. Reorder Waterfall (Cheapest First)

Default waterfalls may not be cost-optimized.

```
Optimized email waterfall:
Tier 1 (2 credits): Prospeo → Dropcontact → Datagma → Hunter
Tier 2 (5 credits): People Data Labs
Tier 3 (included): ZeroBounce verification
```

**How:** Click waterfall column → Customize → Drag to reorder

### 4. Use Conditional Runs

Gate expensive enrichments behind qualifying conditions.

```javascript
// Only run phone enrichment if:
// - Email exists
// - ICP score is high
// - Title is senior
{{Email}} && {{ICP Score}} >= 70 && {{Title}}.match(/vp|director|chief/i)
```

**Setting:** Column → Run Settings → "Only run if"

### 5. Turn Off Auto-Update While Building

**Critical:** Disable automatic column runs during table construction.

1. Click table settings (gear icon)
2. Disable "Auto-run enrichments"
3. Build all columns first
4. Test manually
5. Re-enable when ready for production

### 6. Connect Your Own API Keys (90% Savings)

**BYOK (Bring Your Own Key) math:**

| Feature | Clay Credits | Your API Key |
|---------|--------------|--------------|
| Use AI (GPT-4) | 1 credit (~$0.01) | ~$0.001 |
| Use AI (Claude) | 1 credit (~$0.01) | ~$0.001 |

**Savings:** ~90% reduction on AI-powered columns.

**Note:** Claygent web browsing cannot use BYOK—only "Use AI" features.

### 7. Use AI Formulas Instead of Claygent

**Free alternative for many tasks:**

| Task | Expensive Way | Free Way |
|------|---------------|----------|
| Categorize data | Claygent (1 credit) | AI Formula (0) |
| Extract from existing data | Use AI (1 credit) | Formula (0) |
| Conditional logic | Use AI (1 credit) | Formula (0) |
| String manipulation | Use AI (1 credit) | Formula (0) |

**Rule:** If the data already exists in your table, use a formula.

### 8. Filter Before Enriching

**Create a qualification step before expensive enrichments:**

```
Column 1: Basic company data (cheap/free)
Column 2: ICP Score formula (FREE)
Column 3: Filter view - Only show score >= 60
Column 4: Run expensive enrichments on filtered view only
```

### 9. Use Filtered Views to Limit Scope

**Views can control which rows get enriched:**

1. Create view with filter conditions
2. Select that view
3. Run column (only visible rows are processed)

**Use case:** Re-enrich only rows where email is empty.

### 10. Set Credit Spend Limits

**Prevent runaway costs:**

1. Workspace Settings → Credit Management
2. Set monthly spending cap
3. Set per-workbook limits
4. Enable notifications at 50%, 75%, 90%

---

## API Key Integration (BYOK)

### OpenAI Setup

**Requirements:**
- Paid Clay plan (Starter+)
- OpenAI account with API access
- **Tier 4+ recommended** (450,000 TPM minimum for Claygent)

**Steps:**
1. Get API key from platform.openai.com
2. Clay → Settings → Connections → Add Connection
3. Select OpenAI
4. Paste API key
5. Test connection

**Tier requirements:**
| OpenAI Tier | TPM Limit | Clay Usage |
|-------------|-----------|------------|
| Tier 1 | 10,000 | Basic Use AI only |
| Tier 2 | 40,000 | Limited Claygent |
| Tier 3 | 90,000 | Moderate Claygent |
| Tier 4 | 450,000 | **Recommended minimum** |
| Tier 5 | 1,000,000+ | Heavy usage |

### Anthropic Setup

**Steps:**
1. Get API key from console.anthropic.com
2. Clay → Settings → Connections → Add Connection
3. Select Anthropic
4. Paste API key
5. Test connection

**Cost comparison:**
| Model | Clay Credit | Direct API Cost |
|-------|-------------|-----------------|
| Claude Haiku | 0.5 credits | ~$0.00025/1K tokens |
| Claude Sonnet | 1 credit | ~$0.003/1K tokens |

### BYOK Limitations

**What BYOK covers:**
- "Use AI" columns (reasoning, classification, writing)
- AI Formula generation
- Custom model calls

**What BYOK does NOT cover:**
- Claygent web browsing
- Data provider enrichments
- CRM actions
- Waterfall queries

---

## Cost Modeling for Client Scoping

### Estimating Credits Per Workflow

**Standard outbound workflow:**
```
Per 1,000 leads:
- Sales Nav import: 1,000 credits
- Company enrichment: 0 (Clearbit domain free)
- Clearbit company: 8,000 credits (if needed)
- Email waterfall (avg 2 providers): 4,000 credits
- Phone waterfall (avg 2 providers): 8,000 credits
- AI personalization: 1,000 credits
---
Total: ~14,000-22,000 credits per 1,000 leads
```

### Per-Lead Cost Calculation

**Formula:**
```
(Total credits × Cost per credit) ÷ Valid leads = Cost per lead

Example (Pro plan):
(15,000 credits × $0.014) ÷ 700 valid leads = $0.30 per qualified lead
```

### ROI Framing for Clients

**Frame against alternatives:**

| Approach | Cost per 1,000 Leads | Data Quality |
|----------|---------------------|--------------|
| Manual research | $5,000+ (SDR time) | Variable |
| Single data provider | $500-2,000 | 40-50% coverage |
| Clay waterfall | $150-300 | 70-85% coverage |

**Key message:** Clay delivers 2x coverage at lower cost than single providers.

### Monthly Credit Budget Template

```
Client: [Name]
Workflow: Outbound prospecting

Monthly volume: 2,000 new leads
Credits per lead: ~15
Monthly credits needed: 30,000

Recommended plan: Pro ($720/mo for 50,000 credits)
Estimated monthly cost: $720
Per-lead cost: $0.36

Buffer: 20,000 credits for testing/iteration
```

---

## When to Upgrade Plans

### Break-Even Analysis

**Starter → Explorer upgrade:**
- Starter: 2,000 credits for $134 (~$67/1K)
- Explorer: 10,000 credits for $314 (~$31/1K)
- Break-even: ~4,600 credits/month

**Explorer → Pro upgrade:**
- Explorer: 10,000 credits for $314 (~$31/1K)
- Pro: 50,000 credits for $720 (~$14/1K)
- Break-even: ~22,600 credits/month

### Upgrade Indicators

**Consider upgrading when:**
- Consistently using 80%+ of monthly credits
- Running out before month-end
- Cost per credit matters (high-volume workflows)
- Need Pro features (CRM integrations)

### Feature Availability by Plan

| Feature | Starter | Explorer | Pro |
|---------|---------|----------|-----|
| API keys | ✅ | ✅ | ✅ |
| Phone enrichments | ✅ | ✅ | ✅ |
| Webhooks | ❌ | ✅ | ✅ |
| HTTP API | ❌ | ✅ | ✅ |
| CRM integrations | ❌ | ❌ | ✅ |
| Email sequencing | ❌ | ✅ | ✅ |
| Team features | ❌ | ❌ | ✅ |

**Note:** CRM integration requires Pro—factor this into client recommendations.
