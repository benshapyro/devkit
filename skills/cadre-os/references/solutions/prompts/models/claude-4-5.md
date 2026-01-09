# Claude 4.5 Optimization Guide

Claude 4.5 is a specification-driven model that rewards extreme precision over assumed intent. It follows instructions literally—powerful when prompted correctly, unforgiving when vague.

## Table of Contents
- [Key Characteristics](#key-characteristics)
- [XML Structure (Required)](#xml-structure-required)
- [Extended Thinking](#extended-thinking)
- [Parameter Settings](#parameter-settings)
- [Tool Use](#tool-use)
- [Long Context Strategies](#long-context-strategies)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Key Characteristics

| Trait | Implication |
|-------|-------------|
| Literal instruction following | Be explicit about everything; Claude won't infer "good" means "fully-featured" |
| XML tag training | Use XML structure; Claude treats it as native formatting |
| Extended thinking (up to 64K tokens) | Enable for complex reasoning; disable for simple tasks |
| Conservative behavior | More likely to acknowledge uncertainty; less prone to harmful outputs |
| Reduced sycophancy | Won't agree just to please; gives honest assessments |
| Context awareness | Tracks token usage; maintains coherent multi-hour sessions |

---

## XML Structure (Required)

Claude was explicitly trained with XML tags. Use them for all non-trivial prompts.

**Standard Template:**
```xml
<role>
You are a [specific expert role] with expertise in [domain].
</role>

<task>
Your objective is to [specific goal] for [audience].
You should prioritize [values/principles].
</task>

<context>
[Relevant background information]
</context>

<instructions>
1. [Specific step with clear deliverable]
2. [Next step building on previous]
3. [Final output specification]
</instructions>

<constraints>
- Format: [exact structure needed]
- Length: [specific range]
- Tone: [style for audience]
</constraints>

<examples>
<example>
Input: [sample input]
Output: [desired output]
</example>
</examples>

<output_format>
[Precise structure for response]
</output_format>
```

**Common tag names:** `<instructions>`, `<context>`, `<examples>`, `<document>`, `<thinking>`, `<answer>`, `<format>`, `<constraints>`

**Best practice:** Use consistent, descriptive tag names. Nest hierarchically for complex structures.

---

## Explicitness is Non-Negotiable

Claude 4.5 follows specifications precisely without improvisation.

**Vague prompt (will underdeliver):**
```
Create a good dashboard for our analytics data.
```

**Explicit prompt (will deliver):**
```xml
<task>
Create a comprehensive analytics dashboard for business metrics.
The dashboard should be production-ready, fully interactive, and showcase best practices.
</task>

<requirements>
1. Include at least 5 different chart types (line, bar, pie, area, scatter)
2. Add interactive filters for date range, category, and metrics
3. Implement responsive design for mobile, tablet, and desktop
4. Include real-time update simulation
5. Add hover tooltips with detailed information
6. Make all components fully functional, not placeholder/mock
</requirements>

<constraints>
- Use React with modern hooks
- Include complete, working code—no TODOs or placeholders
- Professional appearance suitable for client presentation
</constraints>
```

---

## Provide Motivation

Explain WHY behind constraints so Claude can generalize.

**Without motivation:**
```
Never use ellipses.
```

**With motivation:**
```
Your response will be read aloud by a text-to-speech engine, so never use ellipses since the engine won't know how to pronounce them.
```

Claude will now also avoid other TTS-problematic characters without being told.

---

## Example Diversity

Claude pays close attention to examples. Ensure diversity.

**Problem:** Including one example with "Industrial Particleboard" caused Claude to default to that choice even when specs required different materials.

**Solution:** Use 2-3 diverse examples showing the full decision space:
- Example of choice A with reasoning
- Example of choice B with reasoning  
- Example showing edge case handling

---

## Extended Thinking

Enable for complex reasoning. Disable for simple tasks.

**When to enable:**
- Math, physics, coding problems
- Multi-step reasoning
- Complex analysis requiring verification
- Architecture decisions

**When to disable:**
- Simple queries
- Speed-critical applications
- Straightforward content generation
- Analytical tasks under 0.2-0.3 temperature

**Critical:** Do NOT prescribe reasoning steps.

❌ **Bad:**
```
First identify variables, then set up equation, then solve for x.
```

✅ **Good:**
```
Think about this math problem thoroughly. Consider multiple approaches and choose the most efficient path.
```

**API Configuration:**
```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250929",
    max_tokens=4000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[...]
)
```

Start with minimal budget (1,024 tokens), increase incrementally while testing.

---

## Parameter Settings

**Breaking change:** Cannot specify both temperature AND top_p. Choose one.

| Task Type | Temperature |
|-----------|-------------|
| Analytical, factual, coding | 0.0 - 0.3 |
| Balanced, general conversation | 0.4 - 0.7 |
| Creative, brainstorming | 0.8 - 1.0 |

**max_tokens:** No default exists—must specify. Max 64K for output. Recommended: 4,000 for typical tasks.

---

## Tool Use

Tool description quality is the #1 factor in tool use performance.

**Minimum 3-4 sentences per tool covering:**
- What it does
- What it returns
- When to use it
- Format expectations
- Limitations

**Example:**
```json
{
  "name": "get_weather",
  "description": "Get current weather information for a specific location. Returns temperature, conditions, humidity, and wind speed. IMPORTANT: Use city and state format for US locations (e.g., 'San Francisco, CA'). For international locations, include country (e.g., 'London, UK'). LIMITATION: Historical weather data not available—only current conditions. WHEN TO USE: When user asks about current weather, temperature, or conditions.",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state (e.g., 'San Francisco, CA') or city and country (e.g., 'London, UK'). Be as specific as possible."
      }
    },
    "required": ["location"]
  }
}
```

Use `strict: true` in production for guaranteed schema conformance.

---

## Long Context Strategies

Claude supports 200K tokens standard (1M with beta headers).

**Structure:**
1. Place long documents (20K+ tokens) at TOP of prompt
2. Put instructions at the END
3. Use anchor phrases: "Based on the information above..."

**Document wrapping:**
```xml
<document>
<source>Annual Report 2024</source>
<document_content>
[content here]
</document_content>
</document>
```

**For retrieval tasks:** Ask Claude to find relevant quotes before answering (grounds responses in provided context).

**Context decay:** Quality drops when approaching limits. Start fresh sessions at 70-80% capacity.

---

## Prefilling

Guide output format by starting the assistant response:

```python
messages = [
    {"role": "user", "content": "Analyze this data and return JSON..."},
    {"role": "assistant", "content": "{"}  # Forces JSON output
]
```

---

## Anti-Patterns to Avoid

### Prescriptive reasoning steps
❌ "First do X, then Y, then Z"
✅ State goals, let Claude choose approach

### Over-constraining roles
❌ "You are a world-renowned expert who only speaks in technical jargon"
✅ "You are a helpful assistant with expertise in [domain]"

### Minimal tool descriptions
❌ "Search the customer database"
✅ 3-4 sentences covering what/when/how/limitations

### Ignoring extended thinking overhead
❌ Enabling for "Is 9.11 larger than 9.9?"
✅ Enable only for tasks requiring deliberation

### Forcing entire repos into context
❌ Dumping 200K tokens of code
✅ Use RAG to retrieve relevant files per query

### One-and-done prompting
❌ Single attempt, blame model
✅ Test 2-3 variations, iterate on winner

### Bloated configuration files
❌ Multi-thousand-line CLAUDE.md files
✅ Minimal, tested directives (aim for <50 lines)
