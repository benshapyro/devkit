# Prompt Audit Checklist

Systematic review framework for evaluating and improving prompts.

## Table of Contents
- [Quick Audit (5 minutes)](#quick-audit-5-minutes)
- [Comprehensive Audit](#comprehensive-audit)
- [Scoring Framework](#scoring-framework)
- [Common Issues by Category](#common-issues-by-category)
- [Improvement Prioritization](#improvement-prioritization)

---

## Quick Audit (5 minutes)

Run through these 7 questions for rapid assessment:

| # | Question | Pass/Fail |
|---|----------|-----------|
| 1 | Would a colleague with minimal context understand what's expected? | |
| 2 | Does it say what TO do (not just what NOT to do)? | |
| 3 | Is the output format explicitly specified? | |
| 4 | Is all necessary context provided (not assumed)? | |
| 5 | Are there examples if the task is complex? | |
| 6 | Is there clear structure/organization? | |
| 7 | Is the prompt appropriate length (not too short or bloated)? | |

**Score:** ___/7

- **7/7:** Ready for production
- **5-6/7:** Minor improvements needed
- **3-4/7:** Significant revision required
- **0-2/7:** Rewrite from scratch

---

## Comprehensive Audit

### Section 1: Clarity and Specificity

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Task definition** - Is the goal unambiguous? | | |
| **Action verbs** - Are instructions actionable? | | |
| **Scope boundaries** - Is it clear what's included/excluded? | | |
| **Assumptions** - Are assumptions stated explicitly? | | |
| **Colleague test** - Would someone else produce same output? | | |

**Section score:** ___/25

**Common fixes:**
- Replace vague verbs with specific actions
- Add explicit scope statements
- State assumptions rather than assuming shared context

---

### Section 2: Structure and Organization

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Logical flow** - Do sections follow sensible order? | | |
| **Delimiters** - Are sections clearly separated? | | |
| **Hierarchy** - Is information properly nested? | | |
| **Scannability** - Can key points be found quickly? | | |
| **Consistency** - Same format throughout? | | |

**Section score:** ___/25

**Common fixes:**
- Add XML tags (Claude) or markdown headers (GPT/Gemini)
- Move context before instructions
- Group related constraints together

---

### Section 3: Context and Information

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Completeness** - All needed info provided? | | |
| **Relevance** - No unnecessary information? | | |
| **Placement** - Context before instructions? | | |
| **Anchoring** - References to context explicit? | | |
| **Background** - Audience/purpose clear? | | |

**Section score:** ___/25

**Common fixes:**
- Add missing context the model can't infer
- Remove tangential information
- Use "Based on the information above" anchoring

---

### Section 4: Output Specification

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Format** - Structure clearly defined? | | |
| **Length** - Word/character limits specified? | | |
| **Tone** - Voice and style specified? | | |
| **Required elements** - Must-haves listed? | | |
| **Example output** - Sample provided if complex? | | |

**Section score:** ___/25

**Common fixes:**
- Add explicit format section
- Provide length guidance
- Include example of desired output

---

### Section 5: Examples and Demonstrations

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Presence** - Examples included where helpful? | | |
| **Diversity** - Examples show range of cases? | | |
| **Quality** - Examples demonstrate excellence? | | |
| **Edge cases** - Unusual situations covered? | | |
| **Anti-examples** - What NOT to do shown? | | |

**Section score:** ___/25

**Common fixes:**
- Add 2-3 diverse examples
- Include at least one edge case
- Show both good and bad outputs

---

### Section 6: Language and Framing

| Criterion | Score (1-5) | Notes |
|-----------|-------------|-------|
| **Affirmative** - Positive instructions dominate? | | |
| **Active voice** - Direct, actionable language? | | |
| **Precision** - No ambiguous words? | | |
| **Motivation** - Reasons behind constraints given? | | |
| **Role clarity** - Persona well-defined if used? | | |

**Section score:** ___/25

**Common fixes:**
- Convert "don't X" to "do Y instead"
- Replace "good" with specific criteria
- Add WHY behind unusual constraints

---

### Total Score Calculation

| Section | Score | Weight | Weighted |
|---------|-------|--------|----------|
| Clarity & Specificity | /25 | 25% | |
| Structure & Organization | /25 | 15% | |
| Context & Information | /25 | 20% | |
| Output Specification | /25 | 20% | |
| Examples & Demonstrations | /25 | 10% | |
| Language & Framing | /25 | 10% | |

**Weighted Total:** ___/100

**Rating:**
- 90-100: Excellent - Production ready
- 80-89: Good - Minor polish needed
- 70-79: Adequate - Several improvements needed
- 60-69: Needs work - Significant revision required
- Below 60: Poor - Fundamental restructuring needed

---

## Common Issues by Category

### Task Definition Issues
| Problem | Symptom | Solution |
|---------|---------|----------|
| Vague goal | Wildly varying outputs | Add specific success criteria |
| Multiple goals | Model picks one, ignores others | Break into separate prompts or prioritize explicitly |
| Implicit goal | Model misinterprets intent | State goal directly at start |

### Context Issues
| Problem | Symptom | Solution |
|---------|---------|----------|
| Missing context | Model makes wrong assumptions | Add all relevant background |
| Too much context | Model gets confused or slow | Remove irrelevant details |
| Wrong placement | Model ignores context | Move context before instructions |

### Format Issues
| Problem | Symptom | Solution |
|---------|---------|----------|
| No format spec | Inconsistent structure | Add explicit output format section |
| Over-specified | Awkward, forced output | Loosen constraints where flexibility helps |
| Format-content mismatch | Content doesn't fit format | Choose format that serves content |

### Example Issues
| Problem | Symptom | Solution |
|---------|---------|----------|
| No examples | Model guesses wrong pattern | Add 2-3 examples |
| Repetitive examples | Model over-fits to pattern | Diversify examples |
| Wrong examples | Model copies bad patterns | Replace with excellent examples |

---

## Improvement Prioritization

When multiple issues exist, fix in this order:

1. **Critical (fix first):**
   - Missing or wrong task definition
   - Missing critical context
   - Fundamentally broken structure

2. **High priority:**
   - No output format
   - Missing examples for complex tasks
   - Negative framing throughout

3. **Medium priority:**
   - Suboptimal structure
   - Missing motivation for constraints
   - Inconsistent formatting

4. **Low priority (polish):**
   - Minor wording improvements
   - Additional edge case examples
   - Tone refinement

---

## Quick Reference: Model-Specific Checks

### Claude-Specific
- [ ] Using XML tags for structure?
- [ ] Being extremely explicit (Claude is literal)?
- [ ] Examples are diverse (Claude pays close attention)?
- [ ] Not prescribing reasoning steps?

### GPT-Specific
- [ ] Persistence instructions included?
- [ ] Verbosity level specified?
- [ ] Reasoning effort appropriate for task?
- [ ] Tool usage rules in system prompt?

### Gemini-Specific
- [ ] Temperature at 1.0 (not lowered)?
- [ ] Context-first, instruction-last for long docs?
- [ ] Not over-engineering prompts (Gemini prefers direct)?
- [ ] Consistent format (XML or Markdown, not mixed)?
