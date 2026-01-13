# Gemini 3.0 Pro Optimization Guide

> **Last verified:** 2025-01-09. Model capabilities may have changed.

Gemini 3 Pro achieves breakthrough reasoning (first model to exceed 1500 Elo on LMArena) while requiring simpler, more direct prompts than predecessors. Directness over persuasion, structure over verbosity, temperature at 1.0 always.

## Table of Contents
- [Key Characteristics](#key-characteristics)
- [Critical: Temperature at 1.0](#critical-temperature-at-10)
- [System Instructions](#system-instructions)
- [Prompt Structure](#prompt-structure)
- [Long Context Processing](#long-context-processing)
- [Deep Think Mode](#deep-think-mode)
- [Multimodal Capabilities](#multimodal-capabilities)
- [Media Resolution Control](#media-resolution-control)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Key Characteristics

| Trait | Implication |
|-------|-------------|
| 1M token context | Largest context window; process entire codebases |
| Temperature locked at 1.0 | Do NOT lower temperature—causes looping |
| Native multimodal | Text, image, video, audio in unified stack |
| Sparse MoE architecture | Efficient compute allocation |
| Deep Think mode | Extended reasoning for complex problems |
| Reduced sycophancy | Direct, honest responses |

**Benchmark positioning:**
- **Abstract reasoning:** 45.1% on ARC-AGI-2 (vs GPT-5.1's 17.6%)
- **Math:** 95% AIME without tools, 100% with code execution
- **Multimodal:** 72.7% on ScreenSpot-Pro (vs GPT-5.1's 3.5%)
- **Long-horizon planning:** $5,478 on Vending-Bench 2 (vs Claude's $3,838)

---

## Critical: Temperature at 1.0

**This is the most important Gemini-specific setting.**

```python
# ❌ DON'T DO THIS - causes looping and degradation
config={"temperature": 0.2}

# ✅ DO THIS - use default or explicitly set to 1.0
config={"temperature": 1.0}  # Or omit entirely
```

**Why:** Gemini 3's reasoning capabilities are optimized for temperature 1.0. The model handles determinism internally through its thinking mechanisms. Lowering temperature (which works for Claude/GPT) causes unexpected behavior with Gemini 3.

---

## System Instructions

Be concise and direct. Gemini 3 responds to clear instructions without persuasive language.

**Effective structure:**
```xml
<role>
You are Gemini 3, a specialized assistant for [Domain].
You are precise, analytical, and persistent.
</role>

<instructions>
1. Plan: Analyze the task and create a step-by-step plan
2. Execute: Carry out the plan. Track progress in TODO format
3. Validate: Review output against user's requirements
4. Format: Present answer in requested structure
</instructions>

<constraints>
- Verbosity: [Low/Medium/High]
- Tone: [Formal/Casual/Technical]
- Handling Ambiguity: Ask clarifying questions ONLY if critical info missing
</constraints>

<output_format>
1. Executive Summary: [2 sentence overview]
2. Detailed Response: [Main content]
</output_format>
```

**What works:**
- Clear roles: "You are a senior solution architect specializing in cloud infrastructure"
- Output constraints: "Be objective. Cite sources. Avoid corporate jargon."
- Verbosity level: "Provide direct, efficient answers. Only elaborate when requested."

**What doesn't work:**
- Overly long or persuasive instructions
- Complex Chain-of-Thought templates from older models
- Putting sensitive information in system instructions (not fully jailbreak-proof)

---

## Prompt Structure

Use XML or Markdown consistently (never mix within a single prompt).

**XML Template:**
```xml
<context>
[Background information, documents, data]
</context>

<task>
[Clear statement of what to do]
</task>

<constraints>
[Format, length, style requirements]
</constraints>
```

**Markdown Template:**
```markdown
## Context
[Background information]

## Task
[What to accomplish]

## Requirements
- [Requirement 1]
- [Requirement 2]
```

---

## Long Context Processing

For documents up to 1M tokens, use context-first, instruction-last structure:

```xml
<context>
[Insert entire document/codebase here - up to 1M tokens]
</context>

<task>
Based on the information above, [your specific question]
</task>
```

**Key phrase:** "Based on the information above" anchors Gemini's reasoning to provided context.

**Performance:** Near-perfect recall (>99.7%) on needle-in-haystack tests up to 1M tokens.

---

## Deep Think Mode

Extended reasoning for complex problems. Adds reasoning overhead but dramatically improves accuracy on hard tasks.

**When to enable:**
- Abstract reasoning problems
- Multi-step mathematical proofs
- Complex analysis requiring exploration
- Tasks where ARC-AGI-2 or AIME performance matters

**When to disable:**
- Simple queries
- Speed-critical applications
- Tasks where standard reasoning suffices

---

## Few-Shot Prompting

Works exceptionally well with Gemini 3:

```
Question: Why is the sky blue?
Explanation1: The sky appears blue because of Rayleigh scattering...
Explanation2: Due to Rayleigh scattering effect.
Answer: Explanation2

Question: What causes earthquakes?
Explanation1: Sudden release of energy in Earth's crust.
Explanation2: Earthquakes happen when tectonic plates suddenly slip...
Answer: Explanation1

Now answer: [your question]
```

---

## Self-Critique Pattern

Improves output quality:

```
Before returning your final response:
1. Did I answer the user's *intent*, not just literal words?
2. Is the tone authentic to the requested persona?
3. If I made assumptions due to missing data, did I flag them?
```

---

## Multimodal Capabilities

Gemini 3 processes text, images, video, and audio natively.

**ScreenSpot-Pro performance (UI element location):**
- Gemini 3: 72.7%
- GPT-5.1: 3.5%

**Use cases enabled by multimodal strength:**
- Computer-use agents
- UI automation
- Document understanding with images
- Video analysis

---

## Media Resolution Control

Control token usage for different media types:

| Setting | Tokens per Frame | Best For |
|---------|-----------------|----------|
| `media_resolution_low` | 70 | General video action recognition |
| `media_resolution_medium` | 560 | PDFs (quality saturates here) |
| `media_resolution_high` | 1,120 (images), 280 (video) | Images; video with dense text |

**Recommendations:**
- **Images:** Always use HIGH for maximum quality
- **PDFs:** Use MEDIUM (quality saturates; saves tokens)
- **Video:** Use LOW/MEDIUM for general content, HIGH for text-heavy

```python
config = types.GenerateContentConfig(
    media_resolution="media_resolution_medium"
)
```

---

## Sampling Parameters

| Parameter | Recommended | Notes |
|-----------|-------------|-------|
| temperature | **1.0** | NEVER change for Gemini 3 |
| top_k | 3-5 | Balanced performance |
| top_p | 0.9-0.95 | Default is 0.95 |
| max_output_tokens | Up to 64K | Set based on expected output |

**Full configuration:**
```python
from google.genai import types

config = types.GenerateContentConfig(
    temperature=1.0,
    top_k=5,
    top_p=0.95,
    max_output_tokens=8192,
    system_instruction="[Your system instructions]"
)
```

---

## Deep Research Feature

Agentic capability for comprehensive research:

1. **Planning:** Transforms query into multi-point research plan (editable)
2. **Searching:** Autonomously browses web, Gmail, Drive, Chat
3. **Reasoning:** Shows thinking process with transparency
4. **Reporting:** Generates comprehensive reports with citations

**Use cases:**
- Competitive analysis
- Due diligence
- Topic deep-dives
- Product comparisons

---

## Anti-Patterns to Avoid

### Lowering temperature
❌ `temperature: 0.2` for "more deterministic" output
✅ Keep at 1.0—Gemini handles determinism internally

### Complex CoT templates from older models
❌ Elaborate reasoning scaffolds that worked for GPT-3.5
✅ Direct instructions; Gemini's reasoning is built-in

### Mixing XML and Markdown
❌ `<context>` with `## Task` in same prompt
✅ Pick one format and use consistently

### Instructions before context (for long documents)
❌ Instructions at top, 500K tokens of documents, question at end
✅ Context first, instructions last with "Based on the information above"

### Over-prompting
❌ Verbose, persuasive instructions
✅ Concise, direct statements—Gemini 3 is less sensitive to prompt engineering theatrics

### Wrong media resolution
❌ HIGH for all videos (wastes tokens)
❌ LOW for images (loses quality)
✅ Match resolution to content type and quality needs
