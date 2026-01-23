# Data Extraction Prompts

Prompts for scraping and extracting structured data from web pages.

---

## 1. Case Study Extraction

**Use case:** Pull customer names, outcomes, and industries from case studies

**Prompt:**
```
Visit {{Website URL}}/customers or {{Website URL}}/case-studies and extract customer information.

For each case study found, extract:
{
  "customer_name": "",
  "industry": "",
  "company_size": "if mentioned",
  "key_outcome": "primary result achieved",
  "metrics": ["specific numbers mentioned"],
  "case_study_url": ""
}

Return up to 10 case studies as an array.

Rules:
- Only extract from actual case studies, not logo walls
- Include specific metrics when available (%, $, time saved)
- If industry not stated, infer from company name
- Skip testimonials without company names

If no case studies page found, return: {"case_studies_found": false}
```

**Model:** Claygent Neon (2 credits) - good for structured lists

---

## 2. Team Page Scraping

**Use case:** Extract leadership team information

**Prompt:**
```
Visit {{Website URL}}/about/team or {{Website URL}}/leadership and extract team members.

For each person, extract:
{
  "name": "",
  "title": "",
  "linkedin_url": "if linked",
  "bio_snippet": "first 50 words of bio if available",
  "headshot_url": "if available"
}

Filter to include:
- C-level executives (CEO, CTO, CFO, etc.)
- VP and above
- Directors (if small company <50 people)
- Founders

Return as array, ordered by seniority.

If no team page found, try:
1. /about
2. /company
3. LinkedIn company page

If still not found: {"team_page_found": false}
```

**Model:** Claygent Neon (2 credits)

**For multiple pages:** Use Navigator (6 credits) if pagination required

---

## 3. Job Posting Analysis

**Use case:** Extract requirements, tech stack, and team size hints

**Prompt:**
```
Analyze job postings at {{Company Name}} from {{Careers URL}} or LinkedIn Jobs.

Find {{Target Role Type}} positions and extract:
{
  "total_openings": X,
  "roles": [
    {
      "title": "",
      "location": "",
      "seniority": "entry/mid/senior/lead",
      "key_requirements": ["top 3 skills"],
      "tech_stack_mentioned": ["tools/languages"],
      "team_mentioned": "team name if specified"
    }
  ],
  "hiring_signals": {
    "growth_indicator": "rapid/moderate/replacement",
    "team_size_hints": "any mentions of team size",
    "remote_policy": "remote/hybrid/onsite"
  }
}

Limit to 5 most relevant roles.

Growth indicators:
- Rapid: 5+ similar roles, "growing team" language
- Moderate: 1-4 roles, standard hiring
- Replacement: Single role, "backfill" language
```

**Model:** Claygent Argon (3 credits) or Navigator (6 credits) for complex job boards

---

## 4. Event and Webinar Discovery

**Use case:** Find upcoming events for outreach timing

**Prompt:**
```
Find upcoming events, webinars, or conferences for {{Company Name}}.

Search:
1. {{Website URL}}/events or /webinars
2. Their LinkedIn events
3. Eventbrite/Meetup listings
4. Conference speaker lists

Return:
{
  "has_upcoming_events": true/false,
  "events": [
    {
      "name": "",
      "type": "webinar/conference/meetup/trade show",
      "date": "YYYY-MM-DD",
      "topic": "",
      "registration_url": "",
      "is_hosting": true/false
    }
  ],
  "speaking_at": [
    {
      "event_name": "",
      "speaker_name": "",
      "topic": "",
      "date": ""
    }
  ]
}

Only include events within next 90 days.
If no events found: {"has_upcoming_events": false}
```

**Model:** Claygent Argon (3 credits)

---

## 5. News and Press Release Mining

**Use case:** Extract recent announcements for timely outreach

**Prompt:**
```
Find recent news and press releases about {{Company Name}}.

Search:
1. {{Website URL}}/news or /press
2. PR Newswire, Business Wire
3. Google News
4. Industry publications

Extract announcements from last 90 days:
{
  "recent_news": [
    {
      "headline": "",
      "date": "YYYY-MM-DD",
      "category": "funding/product/partnership/award/expansion/hire/other",
      "summary": "1-2 sentences",
      "source_url": "",
      "relevance_for_outreach": "high/medium/low"
    }
  ],
  "key_themes": ["recurring topics"],
  "suggested_hook": "best news item for personalized outreach"
}

Relevance scoring:
- High: Funding, executive hire, major product launch
- Medium: Partnership, award, expansion
- Low: Minor updates, routine announcements

Limit to 5 most relevant items.
```

**Model:** Claygent Argon (3 credits)

---

## 6. Product Feature Extraction

**Use case:** Understand product capabilities for positioning

**Prompt:**
```
Visit {{Website URL}} and extract product information.

Navigate to product, features, or solutions pages and extract:
{
  "product_name": "main product",
  "tagline": "main value prop",
  "core_features": [
    {
      "name": "",
      "description": "1 sentence",
      "category": "feature category"
    }
  ],
  "integrations": ["tools they integrate with"],
  "use_cases": ["who uses it and for what"],
  "differentiators": ["what they claim makes them unique"]
}

Rules:
- Extract up to 10 core features
- Focus on capabilities, not marketing fluff
- Note any comparison to competitors
- Include integration partners (important for tech positioning)

If multiple products, focus on primary product or specify which product for {{Target Use Case}}.
```

**Model:** Claygent Neon (2 credits)

---

## Handling Complex Extraction Scenarios

### Multi-Page Extraction

When data spans multiple pages:

```
Prompt Part 1 (find all URLs):
"List all case study URLs from {{Website URL}}/customers"
Return: Array of URLs

Prompt Part 2 (extract from each - use Write to Table):
"Extract details from {{Case Study URL}}"
Return: Structured data per case study
```

### Paginated Results

For pages with pagination:

```
Use Navigator (6 credits):
"Navigate to {{URL}}, click through all pagination pages, and extract all items.
Click 'Next' or 'Load More' until no more results.
Maximum 100 items."
```

### Dynamic Content

For JavaScript-rendered pages:

```
Use Navigator (6 credits):
"Wait for page to fully load, then scroll to bottom to trigger lazy loading.
Once all content is visible, extract..."
```

### Authentication Walls

Claygent cannot log in. Alternatives:

```
1. Use public information only
2. Request client provides CSV export
3. Use API if available (HTTP API enrichment)
4. Accept limited data availability
```

### Rate Limiting and Blocks

If site blocks scraping:

```
1. Reduce batch size
2. Add delays between requests
3. Use Navigator (more browser-like)
4. Try alternative data sources
5. Accept partial data
```

### JSON Output for Write to Table

When extracting lists that should become rows:

```
Return as JSON array with consistent keys:
[
  {"name": "A", "url": "...", "value": "..."},
  {"name": "B", "url": "...", "value": "..."}
]

This format works with Clay's "Write to Table" feature
to create one row per array item.
```
