---
name: clay-mastery
description: Comprehensive implementation guidance for Clay.com data enrichment and automation workflows. Use when building prospect lists, enriching CRM data, configuring AI agents (Claygent), designing waterfall enrichment sequences, optimizing credit usage, or delivering Clay-powered solutions to clients. Covers outbound prospecting, inbound automation, CRM enrichment, signal monitoring, prompt engineering for Claygent, and workflow handoff. Trigger on mentions of Clay, Claygent, waterfall enrichment, data enrichment, prospecting automation, lead scoring, email finding, or GTM automation.
---

# Clay Mastery

Implementation guidance for building Clay.com workflows. Clay is a data enrichment and GTM automation platform connecting 150+ data providers through waterfall enrichment, with AI research capabilities via Claygent.

## Clay Mental Model

**What Clay is:** An enrichable spreadsheet + data orchestration layer + AI research agent. Think of it as a programmable data pipeline where each column can query external APIs, run AI, or transform data.

**Core value proposition:** Access 150+ data providers without separate contracts. Waterfall enrichment queries multiple providers sequentially until data is found, achieving 2-3x coverage vs single providers.

**Key differentiator:** Credits are refunded when providers return nothing, making it cost-effective to try multiple sources.

## Core Workflow Pattern

Every Clay workflow follows this sequence:

```
FIND → FILTER → ENRICH → TRANSFORM → SCORE → EXPORT
```

| Stage | What Happens | Clay Features |
|-------|--------------|---------------|
| FIND | Import or build list | LinkedIn Sales Nav, Google Maps, CRM import, webhooks |
| FILTER | Remove non-ICP | Formulas, conditional logic, AI classification |
| ENRICH | Add missing data | Waterfall enrichment, Claygent research |
| TRANSFORM | Clean and normalize | AI formulas (free), native cleaning tools |
| SCORE | Qualify leads | Point-based formulas, AI scoring |
| EXPORT | Push to destination | CRM sync, sequencer integration, webhooks |

**Critical optimization:** Always FILTER before ENRICH. Filtering at the company level before enriching contacts saves 60-80% on credits.

## Feature Selection Guide

**When to use each Clay capability:**

| Task | Best Tool | Credits | Rationale |
|------|-----------|---------|-----------|
| Rule-based data manipulation | AI Formula Generator | FREE | Converts plain English to JavaScript |
| Structured extraction (tables, lists) | Claygent Neon | 2 | Optimized for multi-column output |
| General web research | Claygent Helium | 1 | Best price-performance ratio |
| Deep/complex research | Claygent Argon | 3 | Highest accuracy for difficult queries |
| Interactive pages (forms, filters) | Claygent Navigator | 6 | Browser automation with vision |
| Writing (emails, personalization) | Use AI with Claude | 1 | Best for human-like copy |
| Simple reasoning | Use AI with GPT-4o-mini | 0.5 | Cheapest for basic tasks |

**Decision tree:**
1. Can this be done with a formula? → Use AI Formula Generator (FREE)
2. Does it require browsing the web? → Use Claygent
3. Is the page interactive (forms, buttons)? → Use Navigator
4. Is it writing/copy? → Use AI with Claude
5. Is it simple data reasoning? → Use AI with GPT-4o-mini

**When helping with formulas, always provide BOTH:**
1. **AI Generator Description** — Plain English for Clay's "Describe your formula" box (use `/Column Name` syntax)
2. **Clayscript Code** — The actual JavaScript for "Write your own formula" (use `{{Column Name}}` syntax)

This gives users flexibility: paste the description for AI generation, or use the code directly for precision.

## Credit Quick Reference

**Current pricing (December 2024, annual billing):**
- Starter: $134/mo for 2K credits (~$67 per 1,000 credits)
- Explorer: $314/mo for 10K credits (~$31 per 1,000 credits)  
- Pro: $720/mo for 50K credits (~$14 per 1,000 credits) — 5x cheaper than Starter

**Top 5 credit-saving rules:**
1. Test on 5-10 rows before running full table
2. Start with company enrichment, then filter, then contact enrichment
3. Order waterfall providers cheapest-to-most-expensive
4. Use conditional runs to gate expensive enrichments
5. Connect your own API keys for AI (90% savings)

See [references/credit-optimization.md](references/credit-optimization.md) for detailed strategies.

## Reference Navigation

### Core Features
| Topic | Reference File | Use When |
|-------|----------------|----------|
| Waterfall enrichment | [waterfall-enrichment.md](references/waterfall-enrichment.md) | Building email/phone waterfalls, choosing providers |
| Claygent AI agent | [claygent-mastery.md](references/claygent-mastery.md) | Configuring Claygent, Navigator, model selection |
| Formulas | [formulas.md](references/formulas.md) | AI Formula Generator + Clayscript (JS, Lodash, Moment, FormulaJS) |
| Data transformation | [data-transformation.md](references/data-transformation.md) | Cleaning, normalizing, scoring data |
| CRM integrations | [crm-integrations.md](references/crm-integrations.md) | HubSpot, Salesforce sync patterns |

### Workflows & Templates
| Topic | Reference File | Use When |
|-------|----------------|----------|
| Outbound prospecting | [workflow-outbound.md](references/workflow-outbound.md) | Building prospect lists → enrichment → sequencer |
| Inbound automation | [workflow-inbound.md](references/workflow-inbound.md) | Form capture → scoring → routing |
| CRM enrichment | [workflow-crm-enrichment.md](references/workflow-crm-enrichment.md) | Refreshing stale CRM data |
| Signal monitoring | [workflow-signals.md](references/workflow-signals.md) | Job changes, funding, hiring triggers |

### Optimization & Operations
| Topic | Reference File | Use When |
|-------|----------------|----------|
| Credit optimization | [credit-optimization.md](references/credit-optimization.md) | Reducing costs, API key setup, cost modeling |
| Troubleshooting | [troubleshooting.md](references/troubleshooting.md) | Debugging errors, fixing failures |

### Prompt Engineering
| Topic | Reference File | Use When |
|-------|----------------|----------|
| Prompt framework | [prompt-engineering.md](references/prompt-engineering.md) | Learning Clay prompting principles |
| Company research prompts | [prompts-company-research.md](references/prompts-company-research.md) | Researching companies, tech stacks, funding |
| Contact research prompts | [prompts-contact-research.md](references/prompts-contact-research.md) | LinkedIn profiles, decision-makers |
| Data extraction prompts | [prompts-data-extraction.md](references/prompts-data-extraction.md) | Scraping case studies, team pages, jobs |
| Qualification prompts | [prompts-qualification.md](references/prompts-qualification.md) | ICP scoring, pain point identification |
| Personalization prompts | [prompts-personalization.md](references/prompts-personalization.md) | Icebreakers, relevance angles |
| Validation prompts | [prompts-validation.md](references/prompts-validation.md) | Data accuracy, source verification |

### Client Delivery
| Topic | Reference File | Use When |
|-------|----------------|----------|
| Client delivery | [client-delivery.md](references/client-delivery.md) | Documentation, handoff, maintenance |

## Common Implementation Patterns

### Pattern 1: LinkedIn → Enrichment → Sequencer
```
1. Import from Sales Navigator (1 credit/row)
2. Clearbit: Company name → domain (FREE)
3. Filter: headcount > 50 AND industry = target
4. Waterfall email: Prospeo → Dropcontact → Hunter (2 credits each, stops on success)
5. ZeroBounce verification (included)
6. Claygent: AI personalization snippet (1-2 credits)
7. Export to Smartlead/Instantly
```

### Pattern 2: Inbound Form → Qualified Lead
```
1. Webhook captures form submission
2. Work email conversion (if personal email)
3. Company enrichment: Clearbit (8 credits)
4. Lead score formula (FREE)
5. Conditional: If score > 70, enrich phone
6. CRM: Lookup → Create/Update
7. Slack notification for hot leads
```

### Pattern 3: CRM Data Refresh
```
1. Import from HubSpot (filter: updated > 90 days ago)
2. Waterfall enrichment for missing fields
3. AI validation: Is data current?
4. Push back with "ignore blank values" enabled
```

## Key Gotchas

1. **Always test on small batches first** - Run 5-10 rows before full table
2. **Turn off auto-run while building** - Prevents accidental full-table charges
3. **Waterfall order matters** - Put cheapest providers first
4. **CRM: Lookup before Create** - Prevents duplicates
5. **Claygent timeouts** - Need OpenAI Tier 4+ (450k TPM) for BYOK
6. **Navigator costs 6 credits** - Only use for truly interactive pages
7. **Credits refund on no-data** - But NOT on invalid/catch-all emails
8. **Job change monitoring** - Max 1,000 people per table, 3 tables total
