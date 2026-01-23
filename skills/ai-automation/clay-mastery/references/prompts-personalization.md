# Personalization Prompts

Prompts for generating personalized outreach content at scale.

---

## 1. One-Line Email Opener

**Use case:** Personalized first line for cold emails

**Prompt:**
```
Write a personalized one-line email opener for {{First Name}}, {{Title}} at {{Company Name}}.

Context available:
- Company description: {{Description}}
- Recent news: {{News}}
- LinkedIn headline: {{Headline}}
- Recent LinkedIn post: {{Recent Post}}

Rules:
- Reference ONE specific thing about them or their company
- Keep under 20 words
- Sound human and conversational, not salesy
- Don't mention your product or why you're emailing
- Avoid generic openers like "Hope you're well" or "I noticed..."

If no specific context available, return: "skip"

Good examples:
- "The expansion into APAC sounds like quite the undertaking - exciting times."
- "Your post about async communication really resonated - we've struggled with that too."
- "Congrats on the Series B - $30M gives you a lot of runway to build."

Bad examples (avoid):
- "I noticed you work at Company..." (generic)
- "Hope this email finds you well..." (cliche)
- "I see you're the VP of Sales..." (obvious)
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## 2. Company-Specific Value Prop

**Use case:** Tailor value proposition to company context

**Prompt:**
```
Write a 2-sentence value proposition for {{Company Name}} based on their situation.

Our product: {{Your Product Description}}
Key benefits: {{Your Key Benefits}}

Their context:
- Industry: {{Industry}}
- Size: {{Employee Count}} employees
- Current challenge (inferred): {{Pain Point}}
- Tech stack: {{Tech Stack}}

Write a value prop that:
1. Acknowledges their specific situation or challenge
2. Connects our solution to their likely needs
3. Keeps it under 40 words total
4. Sounds consultative, not pushy

Format: Two sentences. First addresses their situation, second bridges to solution.

Example output:
"Scaling a sales team from 10 to 50 reps creates massive data hygiene challenges. [Product] automatically enriches and validates contact data so your reps spend time selling, not researching."
```

**Model:** Use AI (GPT-4) - 1 credit

---

## 3. LinkedIn Connection Request

**Use case:** Personalized connection request (300 char limit)

**Prompt:**
```
Write a LinkedIn connection request for {{First Name}}, {{Title}} at {{Company Name}}.

Context:
- Their LinkedIn headline: {{Headline}}
- Mutual connection: {{Mutual Connection}}
- Common ground: {{Common Ground}}
- My reason for connecting: {{Connection Reason}}

Rules:
- MUST be under 300 characters (LinkedIn limit)
- Reference something specific about them
- State a genuine reason for connecting
- Don't pitch or ask for anything
- Sound like a real person, not a template

If mutual connection exists, mention them.
If common ground exists (school, company, interest), reference it.

Output only the message text, nothing else.

Good examples:
- "Hi Sarah - saw your post on PLG metrics. Building something similar at [Company] and would love to follow your thinking."
- "Hey Mike - fellow Berkeley alum here. Your work on RevOps at Stripe is impressive. Would be great to connect."

Character count must be under 300.
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## 4. Meeting Request Email

**Use case:** Full personalized meeting request

**Prompt:**
```
Write a short meeting request email to {{First Name}}, {{Title}} at {{Company Name}}.

Context about them:
- Company focus: {{Description}}
- Recent news: {{News}}
- Their likely challenge: {{Pain Point}}

Context about us:
- What we do: {{Your Product}}
- Relevant social proof: {{Social Proof}}
- Relevant case study: {{Case Study}}

Email structure:
1. Personalized opener (1 line referencing them)
2. Why I'm reaching out (1-2 sentences, relevant to their situation)
3. Social proof (1 sentence)
4. Soft CTA (1 sentence asking for time)

Rules:
- Total email under 100 words
- No fluffy language
- Specific, not generic
- One clear ask
- No attachments or links mentioned

Sign off with just first name.

Output the email body only, no subject line.
```

**Model:** Use AI (GPT-4) - 1 credit

---

## 5. Follow-Up Variation

**Use case:** Generate follow-up that adds value

**Prompt:**
```
Write follow-up email #{{Follow Up Number}} for {{First Name}} at {{Company Name}}.

Original email context: {{Original Email Summary}}
Days since last email: {{Days Since Last}}

Follow-up approach by number:
- #1: Brief bump with new angle or insight
- #2: Share relevant resource (article, stat, case study)
- #3: Direct question about their priorities
- #4: Breakup email (last attempt)

Rules:
- Reference the previous outreach subtly
- Add new value (insight, resource, question)
- Keep shorter than original (under 60 words)
- Don't be apologetic or pushy
- Different tone/angle than previous

For breakup (#4):
- Keep it light and professional
- Leave door open
- No guilt-tripping

Output email body only.
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## 6. Personalization at Scale (Tiered Approach)

**Use case:** Different personalization depth based on lead value

### Tier 1: High-Value Leads (Full Personalization)

```
Write highly personalized outreach for {{First Name}}, {{Title}} at {{Company Name}}.

Research all available context:
- LinkedIn profile: {{LinkedIn URL}}
- Company website: {{Website URL}}
- Recent news: {{News}}
- Recent content: {{Their Content}}
- Mutual connections: {{Mutuals}}
- Company challenges: {{Pain Points}}

Create:
{
  "personalized_opener": "1 line referencing specific detail",
  "relevant_insight": "observation about their business",
  "connection_point": "why you're reaching out to them specifically",
  "tailored_value_prop": "how you help companies like theirs",
  "suggested_subject_line": "personalized subject",
  "personalization_notes": "key details for sales rep"
}

This person is high priority. Invest in deep personalization.
```

**Model:** Claygent Argon (3 credits)

### Tier 2: Mid-Value Leads (Moderate Personalization)

```
Write personalized opener for {{First Name}}, {{Title}} at {{Company Name}}.

Context:
- Industry: {{Industry}}
- Company description: {{Description}}
- Recent news: {{News}}

Return:
{
  "opener": "1 personalized line",
  "angle": "company or industry based"
}

Keep efficient - use available structured data, minimal research.
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

### Tier 3: Lower-Value Leads (Template + Variables)

Use formulas instead of AI:

```javascript
const openers = {
  "Technology": `Scaling tech teams comes with unique data challenges.`,
  "Healthcare": `Healthcare companies face strict data requirements.`,
  "Finance": `Financial services need accurate, compliant data.`,
  "default": `Growing companies like ${{{Company Name}}} often struggle with data quality.`
};

openers[{{Industry}}] || openers["default"]
```

**Model:** Formula (FREE)

---

## 7. Subject Line Generation

**Use case:** Personalized subject lines that get opens

**Prompt:**
```
Generate 3 subject line options for email to {{First Name}} at {{Company Name}}.

Context:
- Their role: {{Title}}
- Company focus: {{Description}}
- Email angle: {{Email Angle}}

Subject line rules:
- Under 50 characters (mobile-friendly)
- No spam trigger words (free, guaranteed, act now)
- Lowercase or sentence case (not Title Case)
- Create curiosity or relevance
- Personalization when natural (name/company)

Return as array:
["option 1", "option 2", "option 3"]

Types to include:
1. Question-based
2. Relevance-based (industry/role specific)
3. Curiosity-based

Avoid:
- RE: or FWD: tricks
- ALL CAPS
- Excessive punctuation!!!
- Clickbait that doesn't match content
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

---

## Quality Control for Personalization

### Personalization Validator

```
Review this personalized content for quality:

Content: {{AI Generated Content}}
Recipient: {{First Name}} {{Last Name}}, {{Title}} at {{Company Name}}
Context used: {{Context Summary}}

Check for:
1. Accuracy - Does it correctly reference their info?
2. Relevance - Is the personalization actually relevant?
3. Tone - Does it sound human and appropriate?
4. Length - Is it appropriately concise?
5. Cringe factor - Would this embarrass the sender?

Return:
{
  "quality_score": 1-10,
  "issues": ["list any problems"],
  "approved": true/false,
  "suggested_edit": "improved version if needed"
}

Be critical. Generic personalization that sounds forced scores low.
```

**Model:** Use AI (GPT-4o-mini) - 0.5 credits

### Fallback Handling

When personalization fails, have fallbacks:

```javascript
// Formula to handle AI failures
const aiPersonalization = {{AI Opener}};
const fallback = `Quick question about ${{{Company Name}}}'s growth plans.`;

(aiPersonalization && aiPersonalization !== "skip" && aiPersonalization.length > 10)
  ? aiPersonalization
  : fallback
```
