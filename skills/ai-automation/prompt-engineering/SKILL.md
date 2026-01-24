---
name: prompt-engineering
description: Comprehensive prompt engineering guidance for Claude 4.5, GPT-5.1, and Gemini 3.0 Pro. Use when users need to write prompts, optimize prompts for specific models, build AI agents or workflows, audit/improve existing prompts, or generate production system prompt templates. Covers 45+ patterns across content creation, analysis, code generation, problem-solving, and education use cases.
tagline: "Master AI interactions"
roles:
  - AI/ML Engineer
  - Content Creator
  - Full-Stack Developer
tasks:
  - Write Code
  - Automate Tasks
favorite: true
---

# Prompt Engineering

Comprehensive prompt engineering patterns, model-specific optimizations, and production templates.

## Quick Navigation

| Need | Action |
|------|--------|
| Find the right pattern for a task | Read `references/patterns/[category].md` |
| Optimize for a specific model | Read `references/models/[model].md` |
| Build an agent or workflow | Read `references/agentic/[topic].md` |
| Review/improve an existing prompt | Read `references/audit/checklist.md` |
| Generate a production template | Copy from `assets/templates/[use-case].md` |

## Pattern Selection by Use Case

| Use Case | Reference File | Examples |
|----------|---------------|----------|
| Content creation | `patterns/content-creation.md` | Blog posts, marketing copy, reports, documentation |
| Analysis & research | `patterns/analysis-research.md` | SWOT, competitive analysis, synthesis, forecasting |
| Code generation | `patterns/code-generation.md` | Functions, debugging, architecture, code review |
| Problem solving | `patterns/problem-solving.md` | Decisions, root cause, planning, risk assessment |
| Education | `patterns/education.md` | Explanations, quizzes, curriculum, tutoring |

## Model Selection

| Strength | Best Model | Key Consideration |
|----------|------------|-------------------|
| Autonomous coding, safety-critical | Claude 4.5 | Requires extreme explicitness; XML tags |
| Cost efficiency, conversational speed | GPT-5.1 | Needs persistence instructions; adaptive reasoning |
| Abstract reasoning, multimodal | Gemini 3.0 Pro | Keep temperature at 1.0; context-first structure |

For model-specific optimization techniques, read `references/models/[model].md`.

## Universal Principles (Always Apply)

These principles work across all models and should inform every prompt:

1. **Be explicit** — Models cannot read your mind. If outputs are too long, request brevity. If too simple, demand expert-level depth.

2. **Use affirmative language** — Tell models what TO do, not what NOT to do. "Output only the final answer" beats "Don't include explanations."

3. **Structure with delimiters** — Separate instructions, context, and examples. Use XML tags for Claude, markdown headers for GPT/Gemini.

4. **Provide complete context first** — Place documents/data at the top, instructions at the end. Use anchor phrases like "Based on the information above..."

5. **Specify output format precisely** — Define exact structure, length, tone. Without this, LLMs are text generators, not APIs.

6. **Include diverse examples** — 2-3 examples showing both desired outputs and edge cases. Avoid repetitive examples that limit generalization.

## Complexity Levels

Each pattern category includes beginner, intermediate, and advanced patterns:

- **Beginner**: Single-purpose, clear constraints, minimal moving parts
- **Intermediate**: Multi-step reasoning, structured frameworks, few-shot examples
- **Advanced**: Multi-pass refinement, adversarial analysis, multi-agent orchestration

Match complexity to task requirements—advanced patterns add overhead that simple tasks don't need.

## Anti-Pattern Quick Reference

Avoid these common mistakes:

| Anti-Pattern | Problem | Fix |
|--------------|---------|-----|
| Vague requests | "Fix my code" with no context | Include language, error, expected behavior |
| Negative constraints | "Don't use jargon" | "Use 8th-grade vocabulary" |
| Missing audience | "Write a summary" | "Write a summary for CFOs focused on margin trends" |
| Prescriptive reasoning | "First do X, then Y, then Z" | State goals, let model choose approach |
| One-and-done | Single attempt, blame model | Test 2-3 variations, iterate on winner |

## Template Assets

Production-ready system prompts in `assets/templates/`:

- `customer-support.md` — Support agent with tool usage and escalation
- `document-analysis.md` — Multi-document synthesis and extraction
- `code-review.md` — Security, performance, and style review
- `executive-briefing.md` — C-suite decision support format
