# Content Creation Patterns

Patterns for writing, marketing, reports, documentation, and creative content.

## Table of Contents
- [Beginner Patterns](#beginner-patterns)
- [Intermediate Patterns](#intermediate-patterns)
- [Advanced Patterns](#advanced-patterns)

---

## Beginner Patterns

### Simple Direct Instruction

Clear, single-purpose commands for straightforward content tasks.

**Template:**
```
[ACTION VERB] a [CONTENT TYPE] about [TOPIC] that [SPECIFIC REQUIREMENT].
```

**Examples:**
- "Write a 100-word promotional email for our project management software that emphasizes time-saving benefits and includes a clear call-to-action."
- "Write a 3-paragraph explanation of API rate limiting for junior developers that includes one concrete example."

**Use when:** First drafts, straightforward tasks, quick summaries, simple rewrites.

**Avoid:** Being too vague, adding politeness phrases, mixing unrelated instructions.

---

### Role-Based Prompting

Assign a specific persona to frame tone, depth, and perspective.

**Template:**
```
You are a [SPECIFIC ROLE/EXPERT]. [TASK INSTRUCTION] for [AUDIENCE]. [OUTPUT REQUIREMENTS].
```

**Examples:**
- "You are a social media strategist with 10 years of B2B experience. Write three LinkedIn post ideas for a SaaS company launching an AI tool, focusing on thought leadership rather than direct selling."
- "You are a technical documentation specialist. Write installation instructions for a Python library for developers new to command-line tools. Keep it under 200 words with numbered steps."

**Use when:** Tone matters, expertise level matters, audience-specific writing.

**Avoid:** Generic roles ("helpful assistant"), conflicting roles, over-constraining.

---

### Basic Template Pattern

Structural skeleton with labeled sections for consistent formatting.

**Template:**
```
Write a [CONTENT TYPE] with the following structure:
[SECTION 1 NAME]: [instruction]
[SECTION 2 NAME]: [instruction]
[SECTION 3 NAME]: [instruction]
```

**Use when:** Reports, blog posts, newsletters, case studies, product descriptions—any recurring format.

**Avoid:** Overly rigid templates that stifle quality, insufficient guidance per section.

---

### Output Format Specification

Explicitly define format, length, structure, or style.

**Template:**
```
[TASK INSTRUCTION]

OUTPUT REQUIREMENTS:
- Format: [exact structure needed]
- Length: [specific range]
- Tone: [style for audience]
- Must include: [required elements]
```

**Use when:** Output feeds into other tools, requires specific formatting (JSON, Markdown), has strict length limits.

---

### Audience Targeting

Define the target reader's knowledge level, interests, and expectations.

**Template:**
```
Write [CONTENT TYPE] for [SPECIFIC AUDIENCE].

AUDIENCE CHARACTERISTICS:
- Knowledge level: [beginner/intermediate/expert]
- Primary concern: [what they care about]
- Reading context: [where/when they'll read this]

Adjust complexity and examples accordingly.
```

---

## Intermediate Patterns

### Few-Shot Prompting

Provide 2-5 examples so the model learns pattern, tone, and format through demonstration.

**Template:**
```
[EXAMPLE 1 INPUT] → [EXAMPLE 1 OUTPUT]
[EXAMPLE 2 INPUT] → [EXAMPLE 2 OUTPUT]
[EXAMPLE 3 INPUT] → [EXAMPLE 3 OUTPUT]

Now: [NEW INPUT] →
```

**Use when:** Specific tone matching, consistent formatting, stylistic imitation.

**Best practices:**
- Use 2-5 diverse examples (diminishing returns after 5)
- Examples should represent the full decision space
- Avoid examples that are too similar

---

### Structured Multi-Stage

Break complex content into explicit sequential steps that build on each other.

**Template:**
```
Create [CONTENT TYPE] using these stages:

STAGE 1: [First step with clear deliverable]
STAGE 2: [Next step building on Stage 1]
STAGE 3: [Final step with output specification]

Complete each stage before proceeding.
```

**Example (Case Study):**
```
Create a case study using these stages:

STAGE 1: List 5 key data points (problem, solution, metrics, timeline, quotes)
STAGE 2: Write a compelling 2-sentence narrative opening
STAGE 3: Complete with solution description and quantified results
```

**Use when:** Long-form content, research-based writing, argumentative pieces.

---

### Constrained Generation

Apply multiple specific boundaries to control output characteristics.

**Template:**
```
[TASK INSTRUCTION]

CONSTRAINTS:
- Length: [exact range]
- Vocabulary: [reading level or word restrictions]
- Must include: [required elements]
- Must avoid: [forbidden elements]
- Tone: [specific register]
```

**Use when:** SEO content, character-limited platforms, brand compliance, regulated industries, accessibility.

---

### Persona-Based Variation

Create multiple variations by systematically varying voice while keeping other parameters constant.

**Template:**
```
Write [CONTENT TYPE] about [TOPIC] in three variations:

VARIATION 1: [Persona A] voice - [characteristics]
VARIATION 2: [Persona B] voice - [characteristics]
VARIATION 3: [Persona C] voice - [characteristics]

Keep core message identical across all variations.
```

**Use when:** A/B testing tone, finding brand voice, targeting different segments.

---

### Tone Control Specification

Precisely calibrate emotional register through multidimensional tone definition.

**Template:**
```
[TASK INSTRUCTION]

TONE SPECIFICATIONS:
- Formality: [1-10 scale, with 1 = casual, 10 = formal]
- Energy: [low/medium/high]
- Attitude: [supportive/neutral/challenging]
- Voice: [first person/second person/third person]

Example of desired tone: "[sample sentence showing the tone]"
```

---

## Advanced Patterns

### Iterative Refinement Loop

Multi-pass content development with explicit evaluation criteria.

**Template:**
```
Create [CONTENT TYPE] using iterative refinement:

PASS 1 - DRAFT: Generate initial content focusing on [primary goal]
PASS 2 - EVALUATE: Review against these criteria: [criterion 1], [criterion 2], [criterion 3]
PASS 3 - REFINE: Improve based on evaluation, specifically addressing [focus area]
PASS 4 - POLISH: Final review for [tone/flow/consistency]

Output the final refined version.
```

**Use when:** High-stakes content, published thought leadership, final-draft quality.

**Note:** Diminishing returns after 3-4 passes.

---

### Chain-of-Thought Writing

Explicit step-by-step reasoning before generating final content.

**Template:**
```
Create [CONTENT TYPE] about [TOPIC].

Before writing, think through:
1. What is the core message?
2. What structure best serves this message?
3. What evidence/examples support each point?
4. What objections might readers have?

Then write the content, informed by your reasoning.
```

**Use when:** Complex arguments, analytical content, persuasive writing, strategic communications.

---

### Multi-Persona Synthesis

Orchestrate multiple expert perspectives into unified content.

**Template:**
```
Create [CONTENT TYPE] by synthesizing these perspectives:

PERSPECTIVE 1 - [Expert Role A]: [What they would emphasize]
PERSPECTIVE 2 - [Expert Role B]: [What they would emphasize]
PERSPECTIVE 3 - [Expert Role C]: [What they would emphasize]

Synthesize into unified content that:
- Incorporates insights from all perspectives
- Resolves apparent contradictions
- Maintains coherent voice throughout
```

**Use when:** Complex topics requiring multidisciplinary insight, balanced coverage of controversial topics.

---

### Interview Pattern

Let the model ask clarifying questions before generating.

**Template:**
```
You will create [CONTENT TYPE]. Before generating, ask me up to 5 clarifying questions about:
- Target audience and their knowledge level
- Key messages or themes to emphasize
- Tone and style preferences
- Length and format requirements
- Any constraints or must-avoid elements

After I answer, generate the content.
```

**Use when:** Underspecified requests, when user may not know what they need, high-stakes deliverables.
