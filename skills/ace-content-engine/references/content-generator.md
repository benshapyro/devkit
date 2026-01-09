# Content Generator Prompt

This prompt handles the generation of blog content. It can work with full context from Workshop Mode or generate directly when sufficient information is provided.

## When to Generate Immediately

**Generate content directly (without asking questions) when you have:**
- A clear topic with a specific angle or focus
- Target audience (from configuration or message)
- At least the topic is specific enough to write about

**Only ask clarifying questions if:**
- The topic is genuinely ambiguous (e.g., just "technology" with no angle)
- Critical information is missing AND you cannot make a reasonable assumption

**Default behavior:** When in doubt, GENERATE. You can always note assumptions made.

---

## Input Context

You may receive some or all of:
- **topic** - The subject to write about (required)
- **angle** - The unique perspective or hook (can infer if not provided)
- **audience** - Who will read this (use config or infer from topic)
- **key_points** - Things that must be included (optional)
- **research** - Facts, statistics, and sources gathered (optional)
- **brand_voice** - How to write (from configuration)
- **word_count** - Target length (default: 1000-1500 words)

If key information is missing, make reasonable assumptions and note them at the end of the draft.

---

## Blog Structure Requirements

### Title
- Clear, specific, and engaging
- Include the main benefit or hook
- Avoid clickbait—deliver on the promise
- 60 characters or less for SEO

### Introduction (100-200 words)
Must include:
- **Hook** - A compelling opening (question, statistic, or relatable scenario)
- **Context** - Brief background on why this matters
- **Preview** - What the reader will learn

Do NOT start with:
- "In today's fast-paced world..."
- "Have you ever wondered..."
- "In this article, we will..."

### Body Sections (700-1000 words)
Structure:
- **3-5 main sections** with H2 headings
- **Each H2 section MUST have 2-3 subsections** with H3 headings
- **One idea per subsection** - don't cram multiple topics
- **Logical flow** - each section builds on the previous

Each H2 section should:
- Start with a brief intro paragraph (1-2 sentences)
- Break into 2-3 H3 subsections for specific points
- Include supporting evidence or examples in subsections
- End with a transition to the next section

Example structure:
```
## Main Section Title (H2)
Brief intro to this section.

### Subsection One (H3)
Content for first point...

### Subsection Two (H3)
Content for second point...
```

### Conclusion (100-150 words)
Must include:
- **Summary** - Key takeaways (bullet points work well)
- **Call to action** - What should the reader do next?
- **Forward momentum** - Leave them motivated to act

---

## Word Count Management

**Default target:** 1000-1500 words (aim for ~1200 words)

**CRITICAL:** Word count is a strict requirement, not a guideline.
- Aim for the middle of the range (~1200 words for default)
- Maximum is a hard ceiling - NEVER exceed it
- If you notice content running long, edit down aggressively

If shorter length requested:
- Prioritize key points
- Reduce examples, not substance
- Keep intro/conclusion proportional

If longer length requested:
- Add more examples and detail
- Include additional sections
- Don't pad with filler

**Mandatory verification:** Before presenting output:
1. Estimate total word count
2. If over maximum, remove redundant examples or condense sections
3. If under minimum, add supporting details or examples
4. Re-verify after adjustments

---

## Brand Voice Application

### Check Guidelines
For each rule in `brand_voice.guidelines`:
1. Apply it throughout the content
2. Verify with examples (does output look like example_good?)

### Apply Tone
Match the configured:
- **Formality level** - casual, professional, or formal
- **Personality** - authoritative, friendly, helpful, educational

**Maintain tone consistency throughout:**
- Don't shift from promotional to educational mid-article
- Keep the same energy level from intro to conclusion
- If confident in intro, stay confident throughout
- Review draft to ensure tone doesn't waver

### Vocabulary Check
**MANDATORY before presenting output:**
1. Scan for words in `vocabulary.avoid` list
2. If ANY forbidden word found, REPLACE IT immediately
3. Common forbidden words to check: synergy, leverage, disrupt, game-changer, revolutionary, cutting-edge, best-in-class, paradigm, holistic
4. Use `vocabulary.preferred` words naturally: streamline, empower, efficiency, insight, transform, optimize, enable

**Example fix:** "Teams leverage automation" → "Teams use automation"

### Voice Override
If user requested a tone adjustment for this piece:
- Apply the override
- Note that it differs from standard brand voice
- Don't let override completely override brand identity

---

## Citation Requirements

### Statistics and Data
**Every statistic MUST have an inline hyperlink citation.** Format:
```markdown
According to [Source Name](https://exact-url-provided), 45% of work activities could be automated.
```

More examples of correct citation format:
- "Remote workers are [13% more productive](https://example.com/stanford-study) according to Stanford research."
- "A [McKinsey report](https://mckinsey.com/report) found that automation could affect 45% of work activities."

**NEVER include a statistic without a hyperlink** from the provided research.

### When Sources Are Missing
If research provided a fact without a URL:
- **Use this exact pattern:** "Industry observers note..." or "Market analysts suggest..."
- **NEVER use:** "Studies show...", "Research indicates...", "According to data..."
- **NEVER cite a specific percentage** without a linked source
- Note that verification is recommended
- Never invent a source or URL

**Example:**
- ❌ "Studies show AI investment is increasing 30%"
- ❌ "According to research, companies are investing more"
- ✅ "Industry observers note that AI investment appears to be accelerating"

### Fact Verification
Before including any statistic:
1. Confirm it's from the research provided
2. Verify the source name matches
3. Check the claim makes logical sense

**CRITICAL: Never invent or hallucinate statistics.**
If you need supporting data and don't have it from provided research:
- Use qualitative language ("many companies," "significant improvement")
- NEVER fabricate percentages, dollar amounts, or specific numbers
- Flag areas where research would strengthen the piece
- Better to be vague than to include unverified claims

---

## Key Points Integration

For each item in `key_points`:
1. Include it in the content
2. Integrate naturally (not just listed)
3. Support with context or evidence
4. Check that all are covered before finishing

If a key point doesn't fit the topic:
- Note the conflict
- Ask how to handle it
- Or integrate with a transition

---

## Image Suggestions

When `include_image_suggestions` is true:

Provide text descriptions for suggested images:

```markdown
**Suggested Images:**

1. **Hero image:** [Description of image that captures the article's theme]
   - Style: [e.g., professional, modern, diverse team]
   - Mood: [e.g., optimistic, focused, collaborative]

2. **Section image ([section name]):** [Description]
   - Purpose: [What this image illustrates]
```

Image description guidance:
- Be specific enough for stock search or AI generation
- Note the intended mood/style
- Explain what the image should convey
- 2-4 image suggestions for a standard blog post

---

## Quality Self-Check

Before presenting the draft, verify:

### Structure
- [ ] Has compelling introduction with hook
- [ ] Has 3-5 body sections with H2 headings
- [ ] Each H2 section has 2-3 H3 subsections
- [ ] Has conclusion with summary and CTA
- [ ] Word count is within target range (1000-1500 default)

### Brand Voice
- [ ] No words from the "avoid" list
- [ ] Tone matches configuration
- [ ] Guidelines are followed

### Accuracy
- [ ] All statistics have sources
- [ ] No invented facts or quotes
- [ ] Claims are from provided research only

### Completeness
- [ ] All key points are included
- [ ] CTA is clear and relevant
- [ ] No placeholder text remains

---

## Output Format

Present the draft in clean Markdown:

```markdown
# [Title]

*Reading time: X minutes*

[Introduction - compelling hook and context]

## [First Section Heading]

Brief intro to this section.

### [Subsection 1.1]
[Content with citations where needed]

### [Subsection 1.2]
[More content...]

## [Second Section Heading]

Brief intro to this section.

### [Subsection 2.1]
[Content...]

### [Subsection 2.2]
[Content...]

[Continue pattern for all sections]

## Conclusion

[Summary and call to action]

---

**Suggested Images:** (if requested)
[Image descriptions]

---

*[Optional: Brief company description and link]*
```

**Critical:** Every H2 section must contain H3 subsections. Do not create H2-only content.

---

## Handling Edge Cases

### Topic Too Broad
If the topic is very broad (e.g., "technology", "business", "investment"):

**Option A - Ask for clarification:**
"The topic 'technology' is quite broad. Could you help me narrow it down? For example:
- Technology investment strategies for mid-sized businesses?
- Emerging technologies in [specific industry]?
- Technology adoption challenges for enterprises?"

**Option B - Narrow and explain your choice:**
"I'll focus this article on 'technology investment strategies for mid-sized businesses' because:
- This angle is actionable and specific
- It aligns with [audience] concerns about ROI
- It allows for concrete examples and advice"

**ALWAYS either ask for clarification OR explain your chosen focus.** Never just generate comprehensive content on a broad topic without addressing the scope.

### Topic Too Narrow
If the topic is extremely specific:
1. Write to appropriate depth
2. Don't pad to hit word count
3. Suggest related topics if very short

### Conflicting Key Points
If key points conflict with each other or the topic:
1. Note the conflict
2. Ask for clarification
3. Propose a resolution

### No Research Provided
If no research was provided but statistics are needed:
1. Use qualitative language
2. Flag areas where data would strengthen the piece
3. Don't invent statistics

---

## YOLO Mode Variation

When `mode: yolo` is specified:

**Changes:**
- Skip Workshop Mode questions
- Make reasonable assumptions
- Generate immediately
- Accept 80% quality target

**Still required:**
- Basic structure (intro, body, conclusion)
- Brand voice application
- No hallucinated facts

**Include disclaimer:**
> *This is a quick draft generated in YOLO mode. It may need more editing than a workshop-generated piece. Review carefully before publishing.*
