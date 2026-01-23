# Prompt Engineering for Clay

Framework for building effective Claygent and AI prompts that scale reliably.

## Table of Contents
1. [Why Prompting Matters in Clay](#why-prompting-matters-in-clay)
2. [Prompt Structure Framework](#prompt-structure-framework)
3. [Specificity Techniques](#specificity-techniques)
4. [Output Formatting Rules](#output-formatting-rules)
5. [Iteration Methodology](#iteration-methodology)
6. [Prompt QA Checklist](#prompt-qa-checklist)
7. [Bad vs Good Prompt Examples](#bad-vs-good-prompt-examples)
8. [Advanced Techniques](#advanced-techniques)

---

## Why Prompting Matters in Clay

**Scale amplifies everything:**
- Claygent runs on thousands of rows
- Small prompt issues → massive waste
- 10% failure rate on 10,000 rows = 1,000 bad results

**Quality directly impacts:**
- Client deliverable accuracy
- Credit consumption (reruns are expensive)
- Downstream workflow reliability

**The goal:** Prompts that work consistently across diverse inputs.

---

## Prompt Structure Framework

### The 5-Part Structure

```
1. INPUT: What data you're providing
2. ACTION: What you want the AI to do
3. OUTPUT: Format and structure of response
4. CONSTRAINTS: Boundaries and limitations
5. EXAMPLES: Input/output samples (optional but powerful)
```

### Part 1: INPUT

Clearly state what data is being provided:

```
You are given:
- Company name: {{Company Name}}
- Company website: {{Website URL}}
- Company description: {{Description}}
```

### Part 2: ACTION

State the task in clear, imperative terms:

```
Find the company's target market and primary value proposition.
```

**Good action words:** Find, Extract, Determine, Classify, Summarize, Compare

### Part 3: OUTPUT

Define exact format expected:

```
Return your answer as JSON:
{
  "target_market": "B2B or B2C",
  "primary_customers": "description of ideal customer",
  "value_proposition": "one sentence"
}
```

### Part 4: CONSTRAINTS

Set boundaries to prevent common failures:

```
Rules:
- Only use information found on the company's website
- If information cannot be found, return "Unknown" - do not guess
- Keep descriptions under 50 words
- Do not include generic marketing language
```

### Part 5: EXAMPLES (Optional)

Show input/output pairs:

```
Example:
Input: Slack, slack.com, "Business messaging platform..."
Output: {"target_market": "B2B", "primary_customers": "Teams and enterprises needing real-time communication", "value_proposition": "Replace email with faster, organized team messaging"}
```

---

## Specificity Techniques

### Be Explicit About WHERE to Look

**Vague (bad):**
```
Find information about the company.
```

**Specific (good):**
```
Visit {{Website URL}}/about and extract the company's mission statement from the "About Us" section.
```

### Define What "Success" Looks Like

**Vague (bad):**
```
Get the company's industry.
```

**Specific (good):**
```
Determine the company's primary industry. Use one of these standard categories:
- Technology / Software
- Healthcare / Life Sciences
- Financial Services
- Manufacturing
- Retail / E-commerce
- Professional Services
- Other (specify)
```

### Specify What to Do When Data Isn't Found

**Missing (bad):**
```
Find the CEO's name.
```

**Complete (good):**
```
Find the CEO's name from the company's team or about page.
If no CEO is listed, look for: President, Founder, Managing Director.
If no executive is found, return "Not Found" - do not guess or invent a name.
```

### Positive and Negative Scope

**Positive scope (look here):**
```
Search these sources in order:
1. Company website /about and /team pages
2. LinkedIn company page
3. Crunchbase profile
```

**Negative scope (don't look here):**
```
Do NOT use:
- Wikipedia (often outdated)
- Social media posts
- Job boards
- News articles older than 1 year
```

---

## Output Formatting Rules

### Single Value Output

For simple extractions, keep it clean:

```
Output only the industry name, nothing else.
No explanations, no caveats, just the answer.
```

### Structured JSON Output

For multi-field extraction, define schema precisely:

```
Return exactly this JSON structure:
{
  "company_size": "SMB / Mid-Market / Enterprise",
  "target_industry": "string",
  "pricing_model": "Per Seat / Per Usage / Flat Rate / Unknown",
  "has_free_trial": true/false
}

Use null for any field that cannot be determined.
```

### Handling Multiple Results

```
If multiple results found, return up to 3, ordered by relevance.
Format as comma-separated list.
Example: "VP Sales, Head of Revenue, CRO"

If only one result, return just that one.
If no results, return "Not Found".
```

### Confidence Indication (Advanced)

```
Return your answer with a confidence score:
{
  "answer": "your answer",
  "confidence": "high / medium / low",
  "source": "where you found this"
}

Use "high" if found on official company page.
Use "medium" if found on third-party source.
Use "low" if inferred but not explicitly stated.
```

---

## Iteration Methodology

### The Iteration Loop

```
1. Write initial prompt
2. Test on 5-10 diverse rows
3. Review ALL outputs (not just first few)
4. Identify failure patterns
5. Add constraints for each pattern
6. Retest on same rows + 10 new ones
7. Repeat until <5% failure rate
8. Scale to full dataset
```

### Choosing Test Rows

Select diverse samples:
- Different company sizes (startup, mid-market, enterprise)
- Different industries
- Different geographies
- Edge cases (incomplete data, unusual formats)

### Failure Pattern Categories

| Pattern | Example | Fix |
|---------|---------|-----|
| Hallucination | Made-up data | Add "do not guess" constraint |
| Wrong source | Used Wikipedia | Add source restrictions |
| Format error | Extra text in output | Specify "output only X" |
| Partial extraction | Missed second value | Add "check for multiple" |
| Timeout | Complex pages | Simplify or use Navigator |

### Documentation

Keep a prompt log:
```
Version 1: Initial prompt - 40% failure rate (hallucinations)
Version 2: Added "do not guess" - 25% failure rate (wrong sources)
Version 3: Added source restrictions - 10% failure rate (format issues)
Version 4: Added output format - 3% failure rate (acceptable)
```

---

## Prompt QA Checklist

Before deploying to full table:

- [ ] Clear objective stated in first sentence
- [ ] All required inputs referenced with `{{}}`
- [ ] Output format explicitly defined
- [ ] "Not found" behavior specified
- [ ] Source restrictions defined
- [ ] Word/character limits set where appropriate
- [ ] Tested on 10+ diverse rows
- [ ] Failure rate < 5%
- [ ] Edge cases handled
- [ ] No unnecessary instructions (token efficiency)

---

## Bad vs Good Prompt Examples

### Example 1: Company Research

**Bad:**
```
Tell me about this company.
```

**Good:**
```
Using {{Website URL}}, extract the company's core business.

Return:
{
  "business_type": "B2B SaaS / B2C App / Services / Marketplace / Other",
  "primary_product": "one sentence description",
  "target_customer": "who they sell to"
}

Rules:
- Only use official company website
- If unclear, return "Unknown" for that field
- Keep descriptions under 20 words
```

### Example 2: Person Research

**Bad:**
```
Find information about {{Person Name}}.
```

**Good:**
```
Using LinkedIn profile {{LinkedIn URL}}, extract:

1. Current job title (exact as listed)
2. Current company name
3. Time in current role (years/months)
4. Previous company (most recent)

Return as:
{
  "title": "",
  "company": "",
  "tenure": "",
  "previous_company": ""
}

If LinkedIn is inaccessible, return all fields as "Not Found".
Do not search other sources or guess.
```

### Example 3: Personalization

**Bad:**
```
Write a personalized email opener for {{Person Name}}.
```

**Good:**
```
Write a one-line email opener for {{First Name}}, {{Title}} at {{Company Name}}.

Context available:
- Company description: {{Description}}
- Recent news: {{News}} (may be empty)
- LinkedIn summary: {{LinkedIn Summary}} (may be empty)

Rules:
- Reference ONE specific thing about them or their company
- Keep under 15 words
- Don't mention your product
- Sound conversational, not salesy
- If no specific info available, return "skip"

Example outputs:
- "Saw your recent podcast on scaling remote teams - great insights on async communication."
- "Congrats on the Series B - exciting time for {{Company Name}}."
- "Noticed you're expanding the sales team - that's usually a fun challenge."
```

---

## Advanced Techniques

### Chain-of-Thought for Complex Research

For multi-step reasoning, make the AI show its work:

```
Research {{Company Name}} to determine if they're a good fit for our sales automation tool.

Think through these steps:
1. What does the company do?
2. How big is their sales team likely to be?
3. What sales tools are they currently using?
4. What's their likely budget?

After your analysis, provide:
{
  "fit_score": 1-10,
  "reasoning": "brief explanation",
  "recommended_action": "pursue / nurture / skip"
}
```

### Multi-Step Decomposition

Instead of one complex prompt, chain multiple simple prompts:

**Column 1:** Find the company's about page URL
**Column 2:** Extract mission from about page
**Column 3:** Classify industry based on mission
**Column 4:** Generate personalization based on industry

### Confidence Scoring

For data that will be used in critical decisions:

```
Find {{Company Name}}'s annual revenue.

Return:
{
  "revenue": "$X million" or "Unknown",
  "confidence": "high/medium/low",
  "source": "where you found this"
}

Confidence levels:
- High: Found on official investor relations, SEC filings, or company press release
- Medium: Found on Crunchbase, LinkedIn, or reputable news source
- Low: Estimated based on employee count or industry averages
```

### Fallback Chains

Design prompts to try multiple approaches:

```
Find the company's headquarters location.

Try these sources in order:
1. Footer of {{Website URL}}
2. Contact page
3. LinkedIn company page
4. Google Maps listing

Return the first valid result found, with source:
{
  "location": "City, State/Country",
  "source": "website footer / contact page / linkedin / google"
}

If not found in any source, return:
{"location": "Not Found", "source": "none"}
```
