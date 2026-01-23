# Contact Research Prompts

Tested prompts for researching people and contacts in Clay.

---

## 1. LinkedIn Profile Summary

**Use case:** Extract key info from LinkedIn profile

**Prompt:**
```
Using {{LinkedIn URL}}, extract this person's professional information:

Return:
{
  "full_name": "",
  "current_title": "exact title as shown",
  "current_company": "",
  "tenure_current_role": "X years Y months",
  "location": "City, State/Country",
  "headline": "their LinkedIn headline",
  "connection_count": "500+ / exact number / Unknown"
}

Rules:
- Use exact title as displayed (don't normalize)
- Calculate tenure from start date shown
- If profile is private or unavailable, return all fields as "Not Accessible"
```

**Model:** Claygent Helium (1 credit)

**Note:** Consider using LinkedIn enrichment (2-3 credits) for more reliable data.

---

## 2. Decision-Maker Identification

**Use case:** Find who owns a specific function at a company

**Prompt:**
```
Find the person responsible for {{Function}} at {{Company Name}}.

Search:
1. {{Website URL}}/team or /about/leadership
2. LinkedIn company page → People
3. Search "{{Function}} {{Company Name}}"

Target titles for {{Function}}:
- Sales: VP Sales, CRO, Head of Sales, Sales Director
- Marketing: CMO, VP Marketing, Head of Marketing
- Engineering: CTO, VP Engineering, Head of Engineering
- Operations: COO, VP Operations, Head of Ops
- Finance: CFO, VP Finance, Controller

Return:
{
  "name": "",
  "title": "",
  "linkedin_url": "",
  "confidence": "high/medium/low"
}

Confidence levels:
- High: Found on company website or confirmed LinkedIn
- Medium: Found on LinkedIn, title matches function
- Low: Best guess based on available info

If no one found, return: {"name": "Not Found", "confidence": "none"}
```

**Model:** Claygent Argon (3 credits)

---

## 3. Career Path Analysis

**Use case:** Understand person's background and trajectory

**Prompt:**
```
Analyze the career path of the person at {{LinkedIn URL}}.

Extract:
{
  "total_experience_years": X,
  "current_role": {
    "title": "",
    "company": "",
    "duration": "X years"
  },
  "previous_roles": [
    {
      "title": "",
      "company": "",
      "duration": ""
    }
  ],
  "education": "Highest degree and school",
  "career_trajectory": "Rising / Lateral / Specialist / Varied",
  "industry_focus": "primary industry"
}

Only include last 3 previous roles.
Career trajectory definitions:
- Rising: Progressively senior titles
- Lateral: Same-level moves between companies
- Specialist: Deep expertise in one area
- Varied: Multiple industries/functions
```

**Model:** Claygent Neon (2 credits)

---

## 4. Content and Thought Leadership

**Use case:** Find recent posts, articles, or talks for personalization

**Prompt:**
```
Find recent content or thought leadership from {{Person Name}}, {{Title}} at {{Company Name}}.

Search for:
1. LinkedIn posts (last 3 months)
2. Podcast appearances
3. Conference talks or webinars
4. Blog posts or articles
5. Twitter/X activity

Return:
{
  "has_content": true/false,
  "recent_posts": [
    {
      "type": "LinkedIn post / podcast / article / talk",
      "topic": "brief description",
      "date": "approximate",
      "url": "if available"
    }
  ],
  "content_themes": ["recurring topics they discuss"],
  "engagement_level": "high / moderate / low / none"
}

Engagement levels:
- High: Regular poster, podcast guest, speaker
- Moderate: Occasional posts, some articles
- Low: Rarely posts
- None: No public content found

Limit to 3 most recent/relevant content pieces.
```

**Model:** Claygent Argon (3 credits)

---

## 5. Mutual Connections and Interests

**Use case:** Find shared background for warm outreach

**Prompt:**
```
Find potential commonalities with {{Person Name}} based on {{LinkedIn URL}}.

Look for:
1. Shared alma maters (schools attended)
2. Shared previous employers
3. Industry groups or associations
4. Shared connections (if visible)
5. Shared interests or hobbies (from profile)
6. Geographic connections (hometown, lived in same city)

Return:
{
  "schools": ["list schools"],
  "previous_companies": ["list companies"],
  "groups_associations": ["professional groups"],
  "interests": ["hobbies, causes, interests shown"],
  "location_history": ["cities/regions"],
  "potential_hooks": ["2-3 specific conversation starters"]
}

Focus on items that could be genuine connection points.
If limited info visible, note: "Profile has limited visibility"
```

**Model:** Claygent Helium (1 credit)

---

## 6. Contact Verification

**Use case:** Confirm person still works at company

**Prompt:**
```
Verify that {{Person Name}} currently works at {{Company Name}} as {{Title}}.

Check:
1. LinkedIn profile (most reliable)
2. Company website team page
3. Recent company news/press releases mentioning them
4. Company email signature format (do they have email@company domain?)

Return:
{
  "verified": true/false,
  "confidence": "high/medium/low",
  "current_title": "actual current title (may differ)",
  "current_company": "actual current company",
  "verification_source": "where you confirmed this",
  "last_activity": "recent LinkedIn activity date if visible"
}

Verification confidence:
- High: LinkedIn shows current role, matches exactly
- Medium: LinkedIn shows role but minor title difference
- Low: Can't verify but no contradicting info

If person has clearly moved: 
{
  "verified": false,
  "moved_to": "new company if known",
  "confidence": "high"
}
```

**Model:** Claygent Helium (1 credit)

---

## Customization Notes

### Title Matching Flexibility

When searching for decision-makers, account for title variations:

```
VP of Sales = VP Sales = Vice President of Sales = Vice President, Sales
Head of Sales = Sales Leader = Chief Sales Officer (smaller companies)
```

### Seniority Filtering

Add seniority requirements to prompts:

```
Rules:
- Only return results for Director level and above
- Skip individual contributors unless specifically requested
- For startups (<50 employees), Managers may be decision-makers
```

### Privacy Considerations

Some profiles have limited visibility:

```
If profile is private or limited:
- Return what is visible
- Note "Limited Profile" in response
- Do not attempt to guess or infer hidden information
```

### Combining Sources

Best results come from multiple sources:

```
1. LinkedIn enrichment (structured data)
2. Claygent research (fills gaps)
3. Company website (verification)
4. News/PR (recent activity)
```

### Regional Variations

For non-US contacts:

```
Additional considerations:
- LinkedIn may be less used (Europe: Xing, China: no access)
- Title conventions differ (Managing Director in UK = CEO equivalent)
- Privacy laws may limit available data (GDPR in EU)
```
