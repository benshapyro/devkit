# Claygent Mastery

Claygent is Clay's AI web research agent combining Google Search, LLMs (GPT/Claude), and web scraping. Over 1 billion runs completed, used daily by 30% of Clay customers.

## Table of Contents
1. [Model Selection Guide](#model-selection-guide)
2. [Claygent Navigator](#claygent-navigator)
3. [Prompt Structure Framework](#prompt-structure-framework)
4. [Input Configuration](#input-configuration)
5. [Output Formatting](#output-formatting)
6. [Multi-Step Research Chains](#multi-step-research-chains)
7. [QA and Iteration](#qa-and-iteration)
8. [Common Failure Modes](#common-failure-modes)

---

## Model Selection Guide

### Claygent Models (Web Research)

| Model | Credits | Best For | Performance Notes |
|-------|---------|----------|-------------------|
| **Helium** | 1 | High-volume tasks, general research | Best price-performance; outperforms GPT-4o-mini |
| **Neon** | 2 | Data formatting, structured extraction | Highest accuracy for multi-column JSON output |
| **Argon** | 3 | Deep research, complex analysis | Found 10/10 queries in Clay's testing |
| **Navigator** | 6 | Interactive pages, form filling | Browser automation with vision (Aug 2025) |

### External AI Models ("Use AI" Feature)

| Model | Credits | Best For |
|-------|---------|----------|
| GPT-4 | 1 | Good reasoning, general tasks |
| GPT-4o | 1 | Faster GPT-4, good balance |
| GPT-4o-mini | 0.5 | Cheapest, simple tasks |
| GPT-o1 | 6 | Advanced reasoning, complex logic |
| Claude Haiku | 0.5 | Fast, good for simple tasks |
| Claude Sonnet | 1 | Best for writing, human-like copy |
| Gemini 1.5 Flash | 0.5 | Fast, good for structured data |

### Decision Matrix

| Task Type | Recommended Model | Why |
|-----------|-------------------|-----|
| Simple web lookup | Claygent Helium (1) | Cost-effective for basic research |
| Extract table data | Claygent Neon (2) | Optimized for structured output |
| Complex company research | Claygent Argon (3) | Highest accuracy |
| Fill out forms, click buttons | Navigator (6) | Only option for interactive pages |
| Write email copy | Use AI - Claude Sonnet (1) | Best human-like writing |
| Simple data reasoning | Use AI - GPT-4o-mini (0.5) | Cheapest for basic logic |
| Classify/categorize | Use AI - GPT-4o-mini (0.5) | Cost-effective for simple decisions |

### Cost-Optimized Hybrid Approach

For maximum coverage at minimal cost:
1. Run Helium (1 credit) on all rows
2. Filter rows where Helium returned blank/incomplete
3. Run Argon (3 credits) only on failed rows
4. Result: Near-100% coverage at ~1.5 average credits/row

---

## Claygent Navigator

Released August 2025, Navigator adds browser automation with vision capabilities.

### What Navigator Can Do
- **Human-style navigation:** Click buttons, fill forms, apply filters
- **Visual reasoning:** Interpret page layouts, read tables, understand PDFs
- **Multi-step workflows:** Navigate through multiple pages
- **Step-by-step replay:** See exactly what actions were taken

### When to Use Navigator vs Basic Claygent

| Use Navigator (6 credits) | Use Basic Claygent (1-3 credits) |
|---------------------------|----------------------------------|
| Data behind search portals | Publicly visible pages |
| Filter/sort required | Direct URL access |
| Form submission needed | Static content extraction |
| Government databases | Standard company websites |
| Professional registries | LinkedIn profiles (via enrichment) |
| SEC filing navigation | News articles, blog posts |

### Navigator Prompt Examples

**Search Portal Navigation:**
```
Go to {{website_url}}, find the search box, enter "{{company_name}}", click search.
From the results, find the company's license number and expiration date.
Return as JSON: {"license_number": "", "expiration_date": ""}
```

**Form Filling:**
```
Navigate to {{portal_url}}. Fill in the search form:
- Business Name: {{company_name}}
- State: {{state}}
Click "Search" and extract the registration status from the results.
```

### Navigator Limitations
- Cannot handle CAPTCHAs
- Cannot authenticate (login walls)
- 6 credits per run (expensive for high volume)
- Slower than basic Claygent (browser rendering time)

---

## Prompt Structure Framework

Clay recommends a 4-part prompt structure:

### 1. State Your Input and Objective
Tell Claygent what data you're providing and what you want.

```
Using the company website {{Website URL}}, find information about their target customers.
```

### 2. Provide Your Input
Use curly brackets `{{Column Name}}` to reference data.

```
The company is {{Company Name}} with website {{Website URL}}.
Their description is: {{Company Description}}
```

### 3. State Guardrails and Rules
Define constraints, edge cases, and what NOT to do.

```
Rules:
- Only use information found on the company's official website
- If information is not found, return "Not Found" - do not guess
- Do not include generic descriptions
- Maximum 50 words
```

### 4. Outline Your Prefix (for personalization)
For consistent output formatting, especially for email copy.

```
Complete my sentence with this prefix: "I noticed your company focuses on"
```

### Full Prompt Example

```
Using the input, determine the primary industry vertical this company serves.

Input:
- Company: {{Company Name}}
- Website: {{Website URL}}
- Description: {{Company Description}}

Rules:
- Return ONE industry vertical only
- Use standard industry categories (Healthcare, Finance, Technology, Retail, Manufacturing, etc.)
- If unclear, return "General B2B"
- Do not explain your reasoning

Output the industry name only, nothing else.
```

---

## Input Configuration

### What Data to Pass to Claygent

**Essential inputs:**
- Company website URL (most important for company research)
- LinkedIn profile URL (for person research)
- Company name (for Google searches)

**Helpful context:**
- Company description (from earlier enrichment)
- Industry (helps narrow search)
- Person's title (for role-specific research)

**Avoid passing:**
- Raw HTML (too large, wastes tokens)
- Entire enrichment JSON blobs
- Irrelevant columns

### Using Column References

```
{{Column Name}}           - Basic reference
{{Column Name||""}}       - Fallback if empty
{{Company Name}} at {{Website URL}}  - Multiple columns
```

### URL vs Domain Inputs

| Input Type | When to Use | Example |
|------------|-------------|---------|
| Full URL | Specific page needed | `https://company.com/about` |
| Domain only | Homepage/general research | `company.com` |
| LinkedIn URL | Person research | `linkedin.com/in/name` |

---

## Output Formatting

### Output Types

| Type | Use When | Example Output |
|------|----------|----------------|
| Text | Single piece of info | "Enterprise SaaS" |
| Number | Numeric values | 150 |
| URL | Links | "https://..." |
| Boolean | Yes/no questions | true/false |
| JSON | Multiple fields | `{"field1": "value1"}` |

### JSON Schema Definition

For multi-field extraction, define the exact schema:

```
Return the following information as JSON:
{
  "target_market": "B2B or B2C",
  "company_size": "SMB, Mid-Market, or Enterprise",
  "primary_product": "one sentence description",
  "founded_year": "YYYY or Unknown"
}
```

### Handling Multiple Results

When multiple values are possible:

```
Return up to 3 job titles, comma-separated.
If only one found, return just that one.
Example output: "VP Sales, Head of Revenue, CRO"
```

---

## Multi-Step Research Chains

### Breaking Complex Research into Steps

**Problem:** Complex prompts often fail or hallucinate.
**Solution:** Chain multiple Claygent columns together.

**Example: Company Deep Research**

| Column | Input | Output |
|--------|-------|--------|
| 1. Find About Page | {{Website URL}} | About page URL |
| 2. Extract Mission | {{About Page URL}} | Mission statement |
| 3. Find Leadership | {{Website URL}} | Team page URL |
| 4. Extract CEO | {{Team Page URL}} | CEO name and LinkedIn |

### Using Write to Table for Chaining

1. First Claygent extracts list of URLs
2. "Write to Table" creates new rows for each URL
3. Second Claygent processes each URL individually

**Use case:** Extract all case studies from a company, then analyze each one.

---

## QA and Iteration

### Testing Methodology

1. **Start small:** Test on 5-10 diverse rows
2. **Review manually:** Check each output against source
3. **Identify patterns:** Note systematic failures
4. **Refine prompt:** Add constraints for failure patterns
5. **Retest:** Run on same rows plus 10 new ones
6. **Scale gradually:** 50 rows → 500 rows → full table

### Prompt QA Checklist

- [ ] Clear objective stated in first sentence
- [ ] All required inputs referenced with {{}}
- [ ] Output format explicitly defined
- [ ] Edge cases addressed (not found, multiple results)
- [ ] Guardrails prevent hallucination
- [ ] Tested on diverse sample (different industries, sizes)
- [ ] Failure rate < 10% on test batch

### Debugging Failed Rows

1. Click on failed row
2. View "Run Info" for that column
3. Check: Was the right URL accessed?
4. Check: Did the page have the data?
5. Check: Was the prompt interpreted correctly?

---

## Common Failure Modes

### Timeouts

**Symptoms:** Column shows "Timeout" error
**Causes:**
- OpenAI API rate limits (if using BYOK)
- Complex prompt requiring multiple page loads
- Slow website response

**Fixes:**
- Upgrade to OpenAI Tier 4+ (450,000 TPM minimum)
- Simplify prompt to reduce processing
- Use Navigator for slow-loading pages
- Reduce batch size

### Hallucinations

**Symptoms:** Plausible-sounding but incorrect data
**Causes:**
- Vague prompt without constraints
- Data not on page (AI invents it)
- Similar company names causing confusion

**Fixes:**
- Add explicit rule: "If not found, return 'Not Found'"
- Specify exact source: "Only use data from {{URL}}"
- Add verification step in separate column
- Use more specific URL (about page vs homepage)

### Wrong Page Sections

**Symptoms:** Extracts data from wrong part of page
**Causes:**
- Homepage too broad
- Multiple similar sections
- Dynamic content loading issues

**Fixes:**
- Provide specific page URL (e.g., /about, /team, /pricing)
- Add section guidance: "Look in the 'Leadership' section"
- Use Navigator for dynamic pages
- Chain: First find correct page, then extract

### Model-Specific Errors

**API key issues:**
- "Invalid API key" → Verify key in Settings > Connections
- "Rate limit exceeded" → Upgrade OpenAI tier or reduce batch size
- "Model not available" → Check if using deprecated model

**Claygent-specific:**
- "Failed to load page" → Website blocking bots, try Navigator
- "No results found" → Broaden search terms
- "Multiple results ambiguous" → Add more specific identifiers
