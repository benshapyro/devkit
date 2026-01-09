# Code Generation Patterns

Patterns for writing code, debugging, architecture decisions, and code review.

## Table of Contents
- [Beginner Patterns](#beginner-patterns)
- [Intermediate Patterns](#intermediate-patterns)
- [Advanced Patterns](#advanced-patterns)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## Beginner Patterns

### Direct Code Request

Instruction-based approach for simple functions and boilerplate.

**Template:**
```
Write a [LANGUAGE] function called [FUNCTION_NAME] that [DESCRIPTION].

Requirements:
- Input: [INPUT_DESCRIPTION with types]
- Output: [OUTPUT_DESCRIPTION with types]
- [CONSTRAINT_1]
- [CONSTRAINT_2]

Handle these edge cases:
- [EDGE_CASE_1]
- [EDGE_CASE_2]
```

**Example:**
```
Write a Python function called calculate_factorial that calculates the factorial of a number.

Requirements:
- Input: n (integer)
- Output: factorial of n (integer)
- Return 1 when n is 0
- Raise ValueError for negative inputs

Handle these edge cases:
- n = 0 should return 1
- n < 0 should raise ValueError with message "Factorial undefined for negative numbers"
```

---

### Debug This Code

Present buggy code with symptoms for targeted debugging.

**Template:**
```
Debug this [LANGUAGE] code:

```[language]
[CODE]
```

SYMPTOMS:
- Error message: [exact error]
- Expected behavior: [what should happen]
- Actual behavior: [what happens instead]
- Sample input: [input that triggers the bug]
- Sample output: [current incorrect output]

Identify the bug and provide the corrected code.
```

**Critical elements:** Include all five symptom elements—missing any forces the model to guess.

---

### Explain This Code

Step-by-step explanation for understanding existing code.

**Template:**
```
Explain this [LANGUAGE] code for a [AUDIENCE LEVEL]:

```[language]
[CODE]
```

Walk through:
1. What the code does overall
2. Each major section/function
3. Any non-obvious techniques or patterns used
4. Potential gotchas or edge cases
```

---

## Intermediate Patterns

### Structured Multi-Step Coding

Chain-of-thought before implementation (43%+ quality improvement).

**Template:**
```
Build [FEATURE DESCRIPTION].

Before coding:
1. Outline a step-by-step implementation plan
2. Identify dependencies and prerequisites
3. List potential edge cases
4. Note any assumptions

Then implement with comments explaining your approach.

CONSTRAINTS:
- Language: [LANGUAGE]
- Framework: [FRAMEWORK if applicable]
- Style: [coding conventions]
```

**Use when:** Features with multiple components, full-stack development, complex business logic.

**Avoid when:** Simple utility functions, time-critical prototyping.

---

### Code Review Pattern

Structured review with severity ratings and actionable fixes.

**Template:**
```
You are a senior developer conducting a code review.

Review this [LANGUAGE] code:

```[language]
[CODE]
```

Evaluate for:
1. Potential bugs
2. Security vulnerabilities
3. Performance issues
4. Code style and readability
5. Test coverage gaps

For each issue found:
- Severity: [Critical / Major / Minor]
- Location: [line number or function name]
- Problem: [description]
- Fix: [suggested correction]
```

**Note:** Never use as sole review for critical systems.

---

### Test Generation Pattern

Generate comprehensive test suites with coverage categories.

**Template:**
```
Generate tests for this [LANGUAGE] code using [TEST FRAMEWORK]:

```[language]
[CODE]
```

Include test cases for:
1. Happy path (normal operation)
2. Edge cases (boundary values, empty inputs)
3. Error conditions (invalid inputs, failures)
4. Boundary values (min/max, limits)

Use AAA pattern (Arrange, Act, Assert) with descriptive test names.

Output: Complete, runnable test file.
```

---

### Refactoring Pattern

Improve code quality while preserving behavior.

**Template:**
```
Refactor this [LANGUAGE] code to improve [QUALITY ASPECT]:

```[language]
[CODE]
```

GOALS:
- [Specific improvement 1]
- [Specific improvement 2]

CONSTRAINTS:
- Maintain identical external behavior
- Preserve existing tests
- [Additional constraints]

Provide:
1. Refactored code
2. Summary of changes made
3. Reasoning for each major change
```

**Quality aspects:** readability, performance, maintainability, testability, DRY compliance.

---

## Advanced Patterns

### Chain-of-Thought Architecture

Explicit reasoning before committing to architectural decisions.

**Template:**
```
Design architecture for [SYSTEM DESCRIPTION].

REQUIREMENTS:
- [Functional requirement 1]
- [Functional requirement 2]
- [Non-functional: scale, performance, etc.]

REASONING PROCESS:
1. Identify key architectural concerns for these requirements
2. Generate 2-3 distinct approaches with different tradeoffs
3. Analyze each approach against requirements
4. Recommend best approach with justification

Then provide:
- Component diagram (as text description or Mermaid)
- Key interfaces
- Data flow
- Technology recommendations
```

**Model-specific tips:**
- **Claude**: Use thinking keywords ("think hard", "consider carefully") to allocate reasoning budget
- **GPT**: Use "Let's approach this step-by-step"
- **Gemini**: Request structured output format alongside reasoning

---

### ReAct Debugging Pattern

Systematic debugging through Thought-Action-Observation cycles.

**Template:**
```
Debug [ISSUE DESCRIPTION] using systematic investigation.

For each step, follow this cycle:

THOUGHT: What do I know? What should I investigate next?
ACTION: [Read file / Run command / Make edit / Run test]
OBSERVATION: What did I learn from this action?

Continue until:
1. Root cause is identified
2. Fix is implemented
3. Tests verify the fix

Start with THOUGHT about the most likely causes.
```

**Prerequisites:** Tool-enabled environment (Claude Code, Cursor, etc.)

---

### Multi-File Code Generation

Coherent code across multiple files with proper imports.

**Template:**
```
Generate a [PROJECT TYPE] with this structure:

```
[DIRECTORY TREE]
```

REQUIREMENTS:
- [Feature requirements]
- [Integration requirements]

PATTERNS TO FOLLOW:
- Import style: [absolute/relative]
- Naming convention: [convention]
- [Reference existing patterns if applicable]

For each file:
- Complete implementation (no placeholders)
- Proper imports referencing other generated files
- Consistent type definitions across files

Generate files in dependency order (shared types first, then implementations).
```

---

### Performance Optimization Pattern

Systematic performance improvement with measurement.

**Template:**
```
Optimize this [LANGUAGE] code for [PERFORMANCE GOAL]:

```[language]
[CODE]
```

CURRENT METRICS (if known):
- [Execution time / Memory usage / etc.]

CONSTRAINTS:
- Must maintain correctness
- [Resource constraints]
- [Compatibility requirements]

ANALYSIS:
1. Identify performance bottlenecks
2. Propose optimizations ranked by impact
3. Assess tradeoffs (readability, maintainability)

OUTPUT:
- Optimized code
- Explanation of each optimization
- Expected improvement (order of magnitude)
- How to measure/verify improvement
```

---

## Anti-Patterns to Avoid

### Vague Request
❌ "Fix my code, it's not working"

✅ Include: language, code, error message, expected vs actual behavior, sample input

---

### Missing Language/Framework
❌ "Write a function to fetch user data from an API"

✅ "Write a TypeScript function using native fetch to get user data from `/api/users/{id}`. Return type should be `User | null`. Include 5-second timeout and handle network errors."

---

### No Edge Cases Specified
❌ "Write a function to divide two numbers"

✅ Include: what to do with zero divisor, integer vs float handling, overflow behavior

---

### Asking for "Best" Without Criteria
❌ "What's the best way to store this data?"

✅ "Compare storage options for [use case] optimizing for [read speed / write speed / cost / simplicity]. We expect [volume] with [access pattern]."

---

### Premature Optimization Request
❌ "Make this code as fast as possible" (without profiling data)

✅ "This function is called 10K times/second and profiling shows it takes 50ms average. Target is under 10ms. Current bottleneck appears to be [specific operation]."
