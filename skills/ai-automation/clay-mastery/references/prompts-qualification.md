# Qualification Prompts

Prompts for ICP scoring, pain point identification, and lead qualification.

---

## 1. ICP Fit Scoring

**Use case:** Score company against ideal customer criteria

**Prompt:**
```
Evaluate this company against our ICP criteria and provide a fit score.

Company Data:
- Name: {{Company Name}}
- Industry: {{Industry}}
- Employee Count: {{Employee Count}}
- Revenue: {{Revenue}}
- Location: {{Location}}
- Description: {{Description}}

ICP Criteria (customize per client):
- Industry: Technology, Healthcare, Financial Services (weight: 25%)
- Company Size: 100-1,000 employees (weight: 30%)
- Revenue: $10M-$500M (weight: 20%)
- Location: North America (weight: 10%)
- Business Model: B2B SaaS preferred (weight: 15%)

Scoring rules:
- Perfect match = 100% of weight
- Partial match = 50% of weight
- No match = 0%

Return:
{
  "overall_score": 0-100,
  "breakdown": {
    "industry": {"match": "full/partial/none", "score": X},
    "size": {"match": "full/partial/none", "score": X},
    "revenue": {"match": "full/partial/none", "score": X},
    "location": {"match": "full/partial/none", "score": X},
    "business_model": {"match": "full/partial/none", "score": X}
  },
  "recommendation": "Strong Fit / Moderate Fit / Weak Fit / Not a Fit",
  "key_concern": "main disqualifying factor if any"
}
```

**Model:** Use AI (GPT-4) - 1 credit

**Alternative:** Formula-based scoring is FREE and often more consistent.

---

## 2. Pain Point Identification

**Use case:** Infer likely challenges from public information

**Prompt:**
```
Based on available information about {{Company Name}}, identify likely business challenges.

Context:
- Industry: {{Industry}}
- Size: {{Employee Count}} employees
- Description: {{Description}}
- Recent News: {{News}} (if available)
- Job Postings: {{Job Titles Hiring}} (if available)

Analyze and identify:
{
  "inferred_challenges": [
    {
      "challenge": "specific pain point",
      "confidence": "high/medium/low",
      "evidence": "what suggests this challenge",
      "relevance_to_our_solution": "how we might help"
    }
  ],
  "growth_stage_challenges": "typical challenges for this company stage",
  "industry_challenges": "common industry-specific issues",
  "recommended_angle": "best approach for outreach"
}

Confidence levels:
- High: Direct evidence (job posting for this, news about struggle)
- Medium: Strong inference (industry pattern, growth signals)
- Low: General assumption based on company type

Limit to top 3 most relevant challenges for {{Your Product Category}}.
```

**Model:** Use AI (GPT-4 or Claude) - 1 credit

---

## 3. Buying Signal Detection

**Use case:** Identify signs of active evaluation or need

**Prompt:**
```
Analyze {{Company Name}} for buying signals related to {{Product Category}}.

Data available:
- Tech stack: {{Tech Stack}}
- Recent job postings: {{Jobs}}
- Recent news: {{News}}
- Website changes: {{Website Data}}
- Funding status: {{Funding}}

Look for these signals:
1. Technology gaps (missing key tools in stack)
2. Hiring related roles (building team that would use product)
3. Competitor usage (using alternative solutions)
4. Growth triggers (funding, expansion, new leadership)
5. Pain indicators (complaints, reviews, job posting language)

Return:
{
  "signal_strength": "strong/moderate/weak/none",
  "signals_detected": [
    {
      "signal_type": "tech gap/hiring/competitor/growth/pain",
      "description": "",
      "source": "where you found this"
    }
  ],
  "competitor_usage": {
    "using_competitor": true/false,
    "which_competitor": "",
    "potential_displacement": "high/medium/low"
  },
  "timing_indicator": "urgent/near-term/future/unknown",
  "recommended_action": "immediate outreach/nurture/wait/skip"
}

Timing definitions:
- Urgent: Active evaluation, RFP out, contract ending
- Near-term: Building budget, hiring team, starting project
- Future: Early stage, not ready yet
- Unknown: Can't determine timeline
```

**Model:** Claygent Argon (3 credits) - requires research

---

## 4. Budget and Authority Signals

**Use case:** Assess likely budget and decision-making authority

**Prompt:**
```
Assess budget capacity and decision-making structure for {{Company Name}}.

Available data:
- Revenue: {{Revenue}}
- Employee Count: {{Employee Count}}
- Funding: {{Funding}}
- Industry: {{Industry}}
- Contact Title: {{Title}}

Analyze:
{
  "budget_assessment": {
    "estimated_range": "$X-$Y per year",
    "confidence": "high/medium/low",
    "basis": "how you estimated this"
  },
  "authority_assessment": {
    "contact_authority_level": "decision-maker/influencer/user/unknown",
    "likely_decision_maker_title": "who probably makes this decision",
    "buying_committee_likely": true/false
  },
  "procurement_complexity": "simple/moderate/complex",
  "typical_sales_cycle": "X months"
}

Budget estimation guidelines:
- Tech companies: 3-5% of revenue on software tools
- Enterprise (1000+): Larger budgets, longer cycles
- SMB (<100): Smaller budgets, faster decisions
- Recently funded: Likely spending on growth tools

Authority guidelines:
- VP+ typically can approve $50K+
- Directors: $10-50K
- Managers: <$10K
- Individual contributors: Influencers only
```

**Model:** Use AI (GPT-4) - 1 credit

---

## 5. Disqualification Check

**Use case:** Quickly filter out poor-fit leads

**Prompt:**
```
Check if {{Company Name}} should be disqualified from outreach.

Data:
- Industry: {{Industry}}
- Employee Count: {{Employee Count}}
- Location: {{Location}}
- Description: {{Description}}

Disqualification criteria (customize per client):
1. Industry exclusions: Government, Non-profit, Education (unless EdTech)
2. Size: Under 20 employees or over 10,000 employees
3. Geography: Outside North America and Europe
4. Business type: Agencies, Consultancies (unless specified)
5. Competitor: Already using [Competitor Name]
6. Status: Acquired, bankrupt, or shut down

Return:
{
  "qualified": true/false,
  "disqualification_reason": "reason if disqualified, null if qualified",
  "borderline": true/false,
  "borderline_reason": "if it's a close call, explain why",
  "override_consideration": "reason to potentially override disqualification"
}

If multiple disqualification criteria met, return the most important one.
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits (simple classification)

---

## 6. Lead Priority Ranking

**Use case:** Stack rank leads for outreach sequence

**Prompt:**
```
Rank this lead for outreach priority.

Lead data:
- Name: {{First Name}} {{Last Name}}
- Title: {{Title}}
- Company: {{Company Name}}
- ICP Score: {{ICP Score}}
- Buying Signals: {{Signals}}
- Recent Engagement: {{Engagement}}

Ranking factors:
1. ICP fit (from score)
2. Buying signal strength
3. Title seniority
4. Recent engagement (visited site, opened email)
5. Timing indicators

Return:
{
  "priority_tier": "P1/P2/P3/P4",
  "priority_score": 1-100,
  "key_factors": ["top 3 factors driving ranking"],
  "outreach_timing": "immediate/this_week/this_month/nurture",
  "suggested_channel": "email/linkedin/phone/multi-channel"
}

Priority definitions:
- P1: Hot - immediate outreach, high conversion potential
- P2: Warm - outreach this week, good potential
- P3: Cool - standard sequence, moderate potential
- P4: Cold - nurture only, low current potential
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## Formula-Based Alternatives (FREE)

### Simple ICP Score

```javascript
let score = 0;

// Size scoring (30 points)
const emp = Number({{Employee Count}}) || 0;
if (emp >= 100 && emp <= 1000) score += 30;
else if (emp >= 50 || emp <= 2000) score += 15;

// Industry scoring (25 points)
const targetIndustries = ["Technology", "Healthcare", "Finance"];
if (targetIndustries.includes({{Industry}})) score += 25;

// Location scoring (15 points)
if ({{Country}} === "United States" || {{Country}} === "US") score += 15;

// Revenue scoring (20 points)
const rev = Number(({{Revenue}}||"").replace(/\D/g,"")) || 0;
if (rev >= 10000000 && rev <= 500000000) score += 20;

// Funding bonus (10 points)
if ({{Has Funding}}) score += 10;

score
```

### Disqualification Formula

```javascript
const disqualified = 
  ["Government", "Non-profit"].includes({{Industry}}) ||
  Number({{Employee Count}}) < 20 ||
  Number({{Employee Count}}) > 10000 ||
  ({{Description}}||"").toLowerCase().includes("agency");

disqualified ? "Disqualified" : "Qualified"
```

### Priority Tier Formula

```javascript
const icpScore = Number({{ICP Score}}) || 0;
const hasSignal = {{Buying Signal}} && {{Buying Signal}} !== "none";
const isDecisionMaker = ({{Title}}||"").match(/VP|Chief|Director|Head/i);

icpScore >= 80 && hasSignal && isDecisionMaker ? "P1" :
icpScore >= 60 && (hasSignal || isDecisionMaker) ? "P2" :
icpScore >= 40 ? "P3" :
"P4"
```

---

## When to Use AI vs Formulas

| Scenario | Use AI | Use Formula |
|----------|--------|-------------|
| Binary classification | ✓ Complex | ✓ Simple rules |
| Numeric scoring | | ✓ Always |
| Nuanced analysis | ✓ | |
| High volume (10K+) | | ✓ Save credits |
| Custom criteria | ✓ First time | ✓ Once defined |
| Consistency critical | | ✓ Deterministic |

**Best practice:** Use formulas for scoring, AI for analysis and edge cases.
