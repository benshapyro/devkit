---
name: ace-content-engine
description: Generate high-quality blog content with brand voice consistency, research support, and structured workflows. Use when writing blog posts, articles, or marketing content. Supports two modes - Workshop (guided, high-quality) and YOLO (quick draft). Handles brand voice configuration, citations, and content structure.
---

# ACE Content Engine

Generate blog content that matches brand voice, includes proper citations, and follows content best practices.

## Modes

**Workshop Mode** (default): Guided process with clarification questions. Use for high-quality, polished content.

**YOLO Mode**: Quick generation without questions. Trigger with phrases like "just quickly", "fast mode", or "YOLO".

## Quick Start

### Workshop Mode
```
User: Help me write a blog post about workflow automation for operations teams
→ Claude asks clarifying questions about angle, audience, key points
→ Claude generates structured content with citations
```

### YOLO Mode
```
User: Just quickly write a blog post about remote work productivity
→ Claude generates immediately with reasonable assumptions
→ Includes disclaimer about quality level
```

## Workshop Workflow

### Phase 1: Topic Exploration
- Understand the core topic
- Identify unique angle or hook
- Clarify target audience

### Phase 2: Content Planning
- Define key points to cover
- Gather supporting research
- Plan structure (intro, body sections, conclusion)

### Phase 3: Content Generation
- Generate following brand voice
- Include proper H2/H3 structure
- Add citations for statistics
- Suggest images if requested

### Phase 4: Quality Check
- Verify word count (default 1000-1500)
- Check brand voice compliance
- Confirm all key points covered

## Brand Voice Configuration

When brand config is provided, apply:
- **Vocabulary rules**: Use preferred words, avoid forbidden words
- **Tone settings**: Match formality and personality
- **Guidelines**: Follow specific do's and don'ts

**Config files to fill in:**
- [brand-voice.yaml](references/brand-voice.yaml) - Probo's voice config
- [products.yaml](references/products.yaml) - Probo's products/services
- [audience.yaml](references/audience.yaml) - Probo's target audience

**Example (for reference):**
- [sample-brand-voice.yaml](references/sample-brand-voice.yaml) - Filled example using fictional "TechFlow"

## Content Structure Requirements

Every blog post must have:
- **Title**: Clear, specific, 60 chars or less
- **Introduction**: Hook + context + preview (100-200 words)
- **Body**: 3-5 H2 sections, each with 2-3 H3 subsections
- **Conclusion**: Summary + call to action (100-150 words)

For detailed formatting rules, see [content-generator.md](references/content-generator.md).
For full workshop workflow, see [system-prompt.md](references/system-prompt.md).

## Citation Rules

**With sources**: Use inline hyperlinks `[Source](url)`
**Without sources**: Use "Industry observers note..." (never fake citations)
**Never**: Invent statistics or fabricate sources

## Research Support

For research tasks, see [research-agent.md](references/research-agent.md).

Research types:
- `trends` - Current developments and patterns
- `statistics` - Specific numbers and data points
- `competitors` - Competitor content analysis
- `comprehensive` - All of the above

## Client Onboarding

Two approaches based on engagement depth:

### Quick Onboarding (5 min)
For fast setup or small engagements:
1. Describe your brand voice in one sentence
2. List 3 words you love and 3 words you hate
3. What's your main product and its #1 benefit?
4. Who's your ideal reader (job title + pain point)?

See [client-onboarding.md](references/client-onboarding.md) for templates.

### Deep Discovery (60-90 min)
For comprehensive content strategy engagements:
- Brand personality & archetype exploration
- Vocabulary audit (power words, forbidden words)
- Writing style preferences
- Full persona development
- Content audit & gap analysis
- Content pillars & strategy

See [deep-discovery.md](references/deep-discovery.md) for full session guide.

## Critical Rules

1. Never invent statistics or citations
2. Always follow brand voice when configured
3. Maintain consistent tone throughout
4. Use proper heading hierarchy (H2 → H3)
5. Stay within word count limits

## Known Limitations

- Word count may occasionally exceed target (~1600 vs 1500) - review and trim
- Vocabulary checking may miss forbidden words - do a final scan
- Statistics can still be generated without sources - verify all claims
