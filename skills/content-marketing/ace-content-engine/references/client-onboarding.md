# Client Onboarding Guide

Use this guide to gather information and generate config files for new clients.

## Onboarding Questionnaire

### 1. Brand Voice Discovery

Ask the client:

**Tone & Personality**
- How would you describe your brand's personality in 3 words?
- What's your formality level? (casual, professional, formal)
- Are you authoritative, friendly, educational, or something else?

**Vocabulary**
- What words/phrases should we ALWAYS use? (e.g., "empower", "streamline")
- What words/phrases should we NEVER use? (e.g., "synergy", "leverage")
- Any industry jargon to use or avoid?

**Writing Style**
- Active or passive voice preference?
- Short punchy sentences or longer flowing prose?
- Do you use contractions? (we're vs we are)

**Examples**
- Share 2-3 pieces of content you love (yours or others')
- Share 1-2 pieces that DON'T match your voice

### 2. Products/Services

For each main product/service:
- Name and tagline
- Key benefits (3-5 bullet points)
- Main features
- What makes it different from competitors?
- Common use cases

### 3. Target Audience

For each audience segment:
- Job titles/roles
- Industry
- Company size
- Pain points they experience
- Goals they're trying to achieve
- How they prefer to consume content

---

## Config File Templates

### brand-voice.yaml

```yaml
client:
  name: "[Client Name]"
  industry: "[Industry]"
  website: "[URL]"

brand_voice:
  summary: >
    [2-3 sentence summary of voice]

  guidelines:
    - rule: "[Rule 1]"
      example_good: "[Good example]"
      example_bad: "[Bad example]"
      rationale: "[Why this matters]"

    - rule: "[Rule 2]"
      example_good: "[Good example]"
      example_bad: "[Bad example]"
      rationale: "[Why this matters]"

  tone:
    formality: "[casual/professional/formal]"
    personality: "[authoritative/friendly/helpful/educational]"
    energy: "[calm/confident/enthusiastic]"
    humor: "[none/occasional/frequent]"

  vocabulary:
    preferred:
      - "[word 1]"
      - "[word 2]"
    avoid:
      - "[word 1]"
      - "[word 2]"

  content_patterns:
    opening:
      - "[How to start articles]"
    closing:
      - "[How to end articles]"
```

### products.yaml

```yaml
products:
  - name: "[Product Name]"
    type: "primary"
    tagline: "[Tagline]"
    description: >
      [Product description]

    key_benefits:
      - "[Benefit 1]"
      - "[Benefit 2]"
      - "[Benefit 3]"

    features:
      - name: "[Feature Name]"
        description: "[What it does]"
        benefit: "[Why it matters]"

    differentiators:
      - "[What makes this unique]"

    use_cases:
      - "[Use case 1]"
      - "[Use case 2]"
```

### audience.yaml

```yaml
audience:
  primary:
    title: "[Job Title]"
    also_known_as:
      - "[Alternative title]"
    industry: "[Industry]"
    company_size: "[Size range]"

    pain_points:
      - "[Pain point 1]"
      - "[Pain point 2]"

    goals:
      - "[Goal 1]"
      - "[Goal 2]"

    content_preferences:
      format: "[blog/video/podcast/etc]"
      length: "[short/medium/long]"
      tone: "[casual/professional]"
```

---

## Quick Onboarding Script

For a fast onboarding, ask:

```
1. Describe your brand voice in one sentence
2. List 3 words you love and 3 words you hate
3. What's your main product and its #1 benefit?
4. Who's your ideal reader (job title + pain point)?
```

Then generate configs from their answers.
