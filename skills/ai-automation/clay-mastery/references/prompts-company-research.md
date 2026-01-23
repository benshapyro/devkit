# Company Research Prompts

Tested prompts for researching companies in Clay.

---

## 1. Company Overview Extraction

**Use case:** Get key facts from company website

**Prompt:**
```
Visit {{Website URL}} and extract the following company information:

1. What the company does (one sentence)
2. Primary product or service
3. Target customer type (B2B/B2C and who specifically)
4. Company founding year (if shown)
5. Headquarters location (if shown)

Return as JSON:
{
  "description": "",
  "primary_product": "",
  "target_customer": "",
  "founded": "YYYY or Unknown",
  "headquarters": "City, State/Country or Unknown"
}

Rules:
- Only use information from the official website
- Keep descriptions under 30 words
- Use "Unknown" for any field not found
```

**Model:** Claygent Helium (1 credit) or Neon (2 credits)

---

## 2. Tech Stack Identification

**Use case:** Find technologies a company uses

**Prompt:**
```
Research what technologies and tools {{Company Name}} uses.

Sources to check (in order):
1. {{Website URL}} - Look for integrations page, tech blog posts
2. Job postings - Tech requirements often reveal stack
3. BuiltWith/Wappalyzer data if available

Return:
{
  "infrastructure": ["AWS/GCP/Azure/etc"],
  "crm": "Salesforce/HubSpot/etc or Unknown",
  "marketing_tools": ["list tools"],
  "dev_stack": ["languages and frameworks"],
  "confidence": "high/medium/low"
}

If minimal information found, return what you can with confidence: "low".
```

**Model:** Claygent Argon (3 credits) - requires deeper research

**Note:** Consider using BuiltWith enrichment (2 credits) instead for accurate tech data.

---

## 3. Funding and Growth Signals

**Use case:** Identify recent funding, growth indicators

**Prompt:**
```
Research {{Company Name}} for recent funding and growth signals.

Look for:
1. Funding announcements in last 12 months
2. Significant hiring (job posting volume)
3. New office openings or expansions
4. Product launches
5. Major customer wins announced

Sources: TechCrunch, Crunchbase, company blog, PR newswire, LinkedIn

Return:
{
  "recent_funding": {
    "amount": "$X or None",
    "round": "Series X or None",
    "date": "YYYY-MM or None"
  },
  "growth_signals": ["list of signals found"],
  "signal_strength": "strong/moderate/weak/none"
}

If no information found, return signal_strength: "none" with empty arrays.
```

**Model:** Claygent Argon (3 credits)

---

## 4. Competitive Intelligence

**Use case:** Identify competitors mentioned or compared

**Prompt:**
```
Find competitors of {{Company Name}} based on {{Website URL}}.

Search for:
1. Comparison pages on their website
2. "Alternatives to" or "vs" pages
3. Industry mentions in their content
4. G2/Capterra competitor listings

Return:
{
  "direct_competitors": ["up to 5 names"],
  "mentioned_on_site": true/false,
  "competitor_category": "what space they compete in"
}

Rules:
- Only include actual competitors, not partners
- If website mentions competitors directly, note which ones
- If no clear competitors found, return empty array
```

**Model:** Claygent Neon (2 credits)

---

## 5. 10-K/Annual Report Analysis

**Use case:** Extract strategic priorities from public filings

**Prompt:**
```
Find and analyze {{Company Name}}'s most recent 10-K or annual report.

Extract:
1. Key strategic priorities mentioned
2. Risk factors that mention technology/operations
3. Revenue breakdown by segment (if available)
4. Major initiatives for coming year

Return:
{
  "strategic_priorities": ["list up to 3"],
  "key_risks": ["list up to 3 relevant to your product"],
  "revenue_segments": {"segment": "percentage"},
  "initiatives": ["list up to 3"],
  "filing_date": "YYYY-MM"
}

If company is private or no filing found, return:
{"private_company": true, "filing_available": false}
```

**Model:** Claygent Navigator (6 credits) - may need to navigate SEC site

**Note:** Best for public companies. For private companies, use funding/news research instead.

---

## 6. Pricing Page Analysis

**Use case:** Extract pricing model and tiers

**Prompt:**
```
Visit {{Website URL}}/pricing (or find pricing page) and extract pricing information.

Return:
{
  "pricing_available": true/false,
  "pricing_model": "per seat / per usage / flat rate / custom / freemium",
  "tiers": [
    {
      "name": "tier name",
      "price": "$X/month or Contact Sales",
      "key_features": ["up to 3 features"]
    }
  ],
  "has_free_trial": true/false,
  "has_free_tier": true/false,
  "enterprise_pricing": "listed / contact sales / not mentioned"
}

If no pricing page exists:
{"pricing_available": false, "pricing_model": "Unknown"}

Do not guess prices. If not clearly stated, mark as "Contact Sales".
```

**Model:** Claygent Neon (2 credits) - good for structured extraction

---

## Customization Notes

### Adapting for Different Industries

**SaaS companies:** Focus on pricing, integrations, tech stack
**Professional services:** Focus on service offerings, client types, case studies
**Manufacturing:** Focus on products, certifications, distribution
**Healthcare:** Focus on specialties, compliance, patient types

### Adding Industry-Specific Fields

```
// Add to any prompt for healthcare companies:
"compliance_certifications": ["HIPAA/SOC2/etc"],
"patient_types": "who they serve"

// Add for financial services:
"regulatory_status": "licensed/registered/etc",
"assets_under_management": "$X or Unknown"
```

### Combining with Enrichment Data

These prompts work best when combined with structured enrichment:

```
1. Run Clearbit first → Get firmographics
2. Run BuiltWith → Get tech stack
3. Run Claygent → Fill gaps and add context
```

This hybrid approach is more cost-effective than relying solely on AI research.
