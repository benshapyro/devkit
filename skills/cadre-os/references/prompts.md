# Prompt Patterns Reference

Comprehensive prompt engineering patterns organized by use case. Patterns at Beginner, Intermediate, and Advanced levels plus model-specific optimization guides.

## Table of Contents

- [Content Creation Patterns](#content-creation-patterns)
- [Analysis & Research Patterns](#analysis--research-patterns)
- [Code Generation Patterns](#code-generation-patterns)
- [Problem-Solving Patterns](#problem-solving-patterns)
- [Education Patterns](#education-patterns)
- [Prompt Audit Checklist](#prompt-audit-checklist)
- [Model Optimization Guides](#model-optimization-guides)
- [Agentic Prompt Patterns](#agentic-prompt-patterns)

---

# Content Creation Patterns

Patterns for writing, marketing, reports, documentation, and creative content.

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

## Intermediate Patterns

### Few-Shot Prompting

Provide 2-5 examples so the model learns pattern, tone, and format through demonstration.

**Template:**
```
[EXAMPLE 1 INPUT] -> [EXAMPLE 1 OUTPUT]
[EXAMPLE 2 INPUT] -> [EXAMPLE 2 OUTPUT]
[EXAMPLE 3 INPUT] -> [EXAMPLE 3 OUTPUT]

Now: [NEW INPUT] ->
```

**Use when:** Specific tone matching, consistent formatting, stylistic imitation.

**Best practices:**
- Use 2-5 diverse examples (diminishing returns after 5)
- Examples should represent the full decision space
- Avoid examples that are too similar

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

---

# Analysis & Research Patterns

Patterns for business analysis, research synthesis, competitive intelligence, and strategic planning.

## Beginner Patterns

### Structured Comparison

Side-by-side analysis of options on specified dimensions.

**Template:**
```
Compare [OPTION A], [OPTION B], and [OPTION C] on these dimensions:

1. [Dimension 1]: [what to evaluate]
2. [Dimension 2]: [what to evaluate]
3. [Dimension 3]: [what to evaluate]

For each option, provide a brief assessment per dimension, then recommend which is best for [specific use case].
```

### Summarization with Focus

Condense content with a specific analytical angle for a defined audience.

**Template:**
```
Summarize [CONTENT] for [AUDIENCE].

FOCUS: [specific aspect they care about]
LENGTH: [word count or format]
INCLUDE: [required elements]
EXCLUDE: [irrelevant details for this audience]
```

### Basic Data Interpretation

Transform raw numbers into insights with context.

**Template:**
```
Given this data: [numbers/metrics]

Analyze:
1. [Specific question about trends]
2. [Specific question about anomalies]
3. [Specific question about implications]

Context: [business/technical context]

Provide interpretation with supporting evidence from the data.
```

### Role-Based Analysis

Leverage expert persona for domain-specific insights.

**Template:**
```
You are a [DOMAIN EXPERT] with [YEARS] experience in [SPECIALIZATION].

Analyze [SUBJECT] from your expert perspective, focusing on:
- [Expert consideration 1]
- [Expert consideration 2]
- [Expert consideration 3]

Provide insights a generalist would miss.
```

## Intermediate Patterns

### Framework-Based Analysis

Apply established business/analytical frameworks systematically.

**SWOT Template:**
```
Conduct SWOT analysis for [COMPANY/PRODUCT/STRATEGY].

Context: [relevant background]

STRENGTHS: Internal capabilities and advantages
WEAKNESSES: Internal limitations and disadvantages
OPPORTUNITIES: External favorable conditions
THREATS: External risks and challenges

Then provide 2-3 strategic recommendations based on SWOT-derived insights, specifically addressing how to leverage strengths against opportunities and mitigate weaknesses against threats.
```

**Porter's Five Forces Template:**
```
Analyze [INDUSTRY/MARKET] using Porter's Five Forces:

1. Threat of new entrants: [barriers to entry analysis]
2. Bargaining power of suppliers: [supplier concentration, switching costs]
3. Bargaining power of buyers: [buyer concentration, price sensitivity]
4. Threat of substitutes: [alternative solutions available]
5. Competitive rivalry: [number of competitors, differentiation]

Conclude with strategic implications for [COMPANY].
```

**PESTEL Template:**
```
Conduct PESTEL analysis for [DECISION/STRATEGY]:

- Political: [government policy, regulation, trade]
- Economic: [growth, inflation, exchange rates]
- Social: [demographics, culture, trends]
- Technological: [innovation, automation, R&D]
- Environmental: [climate, sustainability, resources]
- Legal: [employment law, consumer protection, IP]

Identify the 3 most critical factors and their strategic implications.
```

### Multi-Criteria Evaluation Matrix

Weighted scoring for decision-making.

**Template:**
```
Evaluate [OPTIONS] using weighted criteria:

CRITERIA AND WEIGHTS:
- [Criterion 1]: [X]% weight
- [Criterion 2]: [Y]% weight
- [Criterion 3]: [Z]% weight
(Weights must sum to 100%)

For each option:
1. Score 1-10 on each criterion with brief justification
2. Calculate weighted score
3. Note qualitative factors not captured in scoring

RECOMMENDATION: Based on highest weighted score plus qualitative considerations.
```

### Sequential Research Process

Phased research with progressive inquiry.

**Template:**
```
Research [TOPIC] in phases:

PHASE 1 - LANDSCAPE: Map the key players, trends, and terminology
PHASE 2 - DEEP DIVE: Investigate [specific focus area] based on Phase 1 findings
PHASE 3 - ANALYSIS: Identify patterns, gaps, and implications
PHASE 4 - SYNTHESIS: Consolidate into actionable insights

After each phase, summarize findings before proceeding.
```

### Hypothesis-Testing Analysis

Apply scientific method with evidence evaluation.

**Template:**
```
Test this hypothesis: [STATEMENT]

EVIDENCE FOR:
- [Gather supporting data points]

EVIDENCE AGAINST:
- [Gather contradicting data points]

ALTERNATIVE HYPOTHESES:
- [Consider other explanations]

CONCLUSION:
- Accept / Reject / Modify hypothesis
- Confidence level: [High/Medium/Low]
- Key uncertainties remaining
```

### Cross-Source Synthesis

Integrate multi-source information with contradiction resolution.

**Template:**
```
Synthesize information from these sources on [TOPIC]:

[SOURCE 1]: [summary or full text]
[SOURCE 2]: [summary or full text]
[SOURCE 3]: [summary or full text]

ANALYSIS:
1. Points of agreement across sources
2. Points of contradiction (with assessment of which is more credible and why)
3. Gaps where no source provides coverage
4. Unified synthesis addressing contradictions
```

## Advanced Patterns

### Adversarial Analysis (Red Team / Blue Team)

Stress-test ideas through opposing viewpoints.

**Template:**
```
Analyze this proposition: [STATEMENT OR STRATEGY]

BLUE TEAM (Advocate):
Build the strongest possible case supporting this proposition.
- Key arguments with evidence
- Best-case scenarios
- Why objections fail

RED TEAM (Critic):
Identify flaws, risks, and counterarguments.
- Challenge assumptions
- Worst-case scenarios
- Why arguments fail

PURPLE TEAM (Judge):
Synthesize both perspectives.
- Genuinely strong points from each side
- Legitimate concerns that survive scrutiny
- Balanced assessment with modifications to strengthen the proposition
```

**Use when:** High-stakes decisions, strategy validation, investment evaluation.

### Multi-Dimensional Causal Analysis

Map root causes with confounders and interactions.

**Template:**
```
Analyze [PROBLEM/OUTCOME] across causal dimensions:

IMMEDIATE CAUSES: Direct triggers of the outcome
ROOT CAUSES: Underlying factors enabling immediate causes
CONTRIBUTING FACTORS: Conditions that amplified the problem
CONFOUNDING VARIABLES: Factors that appear causal but aren't
FEEDBACK LOOPS: How effects become causes
LEVERAGE POINTS: Where intervention would have greatest impact

Create a causal map showing relationships between factors.
```

### Scenario Analysis with Probabilistic Forecasting

Future planning under uncertainty using 2x2 matrices.

**Template:**
```
Develop scenarios for [DECISION] over [TIME HORIZON]:

KEY UNCERTAINTIES:
1. [Uncertainty A]: Range from [low state] to [high state]
2. [Uncertainty B]: Range from [low state] to [high state]

2x2 MATRIX SCENARIOS:

| | Uncertainty A: Low | Uncertainty A: High |
|---|---|---|
| **Uncertainty B: Low** | Scenario 1: [Name] | Scenario 2: [Name] |
| **Uncertainty B: High** | Scenario 3: [Name] | Scenario 4: [Name] |

For each scenario:
- Description and key characteristics
- Probability estimate (%)
- Strategic implications
- Recommended actions

CROSS-SCENARIO STRATEGY:
- No-regret moves (work in all scenarios)
- Options to preserve (hedging strategies)
- Big bets (scenario-specific investments)
```

### Multi-Agent Research System (ReAct)

Orchestrated research through specialized analytical perspectives.

**Template:**
```
Conduct research on [TOPIC] using specialized agents:

AGENT 1 - [EXPERTISE A]:
- Focus: [specific analytical lens]
- Key questions to answer: [list]

AGENT 2 - [EXPERTISE B]:
- Focus: [specific analytical lens]
- Key questions to answer: [list]

AGENT 3 - [EXPERTISE C]:
- Focus: [specific analytical lens]
- Key questions to answer: [list]

ORCHESTRATION:
1. Each agent conducts independent analysis
2. Agents share findings
3. Identify agreements, conflicts, and gaps
4. Synthesizing agent consolidates into unified assessment

OUTPUT: Integrated analysis with attributed insights.
```

---

# Code Generation Patterns

Patterns for writing code, debugging, architecture decisions, and code review.

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

## Code Anti-Patterns to Avoid

### Vague Request
- **Bad:** "Fix my code, it's not working"
- **Good:** Include: language, code, error message, expected vs actual behavior, sample input

### Missing Language/Framework
- **Bad:** "Write a function to fetch user data from an API"
- **Good:** "Write a TypeScript function using native fetch to get user data from `/api/users/{id}`. Return type should be `User | null`. Include 5-second timeout and handle network errors."

### No Edge Cases Specified
- **Bad:** "Write a function to divide two numbers"
- **Good:** Include: what to do with zero divisor, integer vs float handling, overflow behavior

### Asking for "Best" Without Criteria
- **Bad:** "What's the best way to store this data?"
- **Good:** "Compare storage options for [use case] optimizing for [read speed / write speed / cost / simplicity]. We expect [volume] with [access pattern]."

---

# Problem-Solving Patterns

Patterns for decision-making, planning, risk assessment, and root cause analysis.

## Beginner Patterns

### Simple Decision Framework

Basic pros/cons analysis with recommendation.

**Template:**
```
Help me decide between [OPTION A] and [OPTION B] for [CONTEXT].

For each option, analyze:
- Pros (advantages)
- Cons (disadvantages)
- Key risks
- Best suited when...

My priorities are: [PRIORITY 1], [PRIORITY 2], [PRIORITY 3]

Recommend which option best fits my priorities and explain why.
```

### Structured Problem Statement

Clarify the problem before solving.

**Template:**
```
Help me clarify this problem: [VAGUE PROBLEM DESCRIPTION]

Define:
1. SITUATION: What is the current state?
2. COMPLICATION: What changed or is challenging?
3. QUESTION: What specifically needs to be answered/solved?
4. CONSTRAINTS: What limitations exist?
5. SUCCESS CRITERIA: How will we know the problem is solved?
```

### Step-by-Step Planning

Break down a goal into actionable steps.

**Template:**
```
Create a step-by-step plan to [GOAL].

CONTEXT:
- Starting point: [current state]
- Resources available: [what we have]
- Timeline: [deadline or duration]

For each step:
1. Action to take
2. Expected outcome
3. Dependencies (what must happen first)
4. Potential blockers and mitigations
```

## Intermediate Patterns

### Root Cause Analysis (5 Whys)

Drill down to underlying causes.

**Template:**
```
Conduct 5 Whys analysis for: [PROBLEM]

PROBLEM: [symptom or issue observed]

WHY 1: Why does [problem] occur?
-> [First-level cause]

WHY 2: Why does [first-level cause] occur?
-> [Second-level cause]

WHY 3: Why does [second-level cause] occur?
-> [Third-level cause]

WHY 4: Why does [third-level cause] occur?
-> [Fourth-level cause]

WHY 5: Why does [fourth-level cause] occur?
-> [Root cause]

ROOT CAUSE SUMMARY: [concise statement]
RECOMMENDED ACTION: [intervention at root cause level]
```

### Decision Matrix

Quantitative comparison with weighted criteria.

**Template:**
```
Evaluate these options using a decision matrix:

OPTIONS:
- Option A: [description]
- Option B: [description]
- Option C: [description]

CRITERIA (with weights):
1. [Criterion 1]: [weight]%
2. [Criterion 2]: [weight]%
3. [Criterion 3]: [weight]%
4. [Criterion 4]: [weight]%
(Weights sum to 100%)

For each option:
- Score each criterion 1-10 with justification
- Calculate weighted total
- Note qualitative factors not captured in scoring

OUTPUT: Ranked recommendations with rationale.
```

### Risk Assessment Matrix

Identify and prioritize risks.

**Template:**
```
Conduct risk assessment for [PROJECT/DECISION]:

For each identified risk:

| Risk | Likelihood (1-5) | Impact (1-5) | Risk Score | Mitigation |
|------|-----------------|--------------|------------|------------|
| [Risk 1] | [L] | [I] | [LxI] | [action] |
| [Risk 2] | [L] | [I] | [LxI] | [action] |

LIKELIHOOD SCALE:
1 = Rare, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Almost Certain

IMPACT SCALE:
1 = Negligible, 2 = Minor, 3 = Moderate, 4 = Major, 5 = Severe

Prioritize risks with score >=12 for immediate mitigation.
Identify any risks that are acceptable, require monitoring, or need contingency plans.
```

### Stakeholder Analysis

Map stakeholders and their interests for decision-making.

**Template:**
```
Analyze stakeholders for [DECISION/PROJECT]:

For each stakeholder:
| Stakeholder | Interest/Concern | Influence Level | Support Level | Strategy |
|-------------|-----------------|-----------------|---------------|----------|
| [Group 1] | [what they care about] | High/Med/Low | Supporter/Neutral/Opponent | [approach] |

POWER-INTEREST GRID:
- High Power, High Interest: [manage closely]
- High Power, Low Interest: [keep satisfied]
- Low Power, High Interest: [keep informed]
- Low Power, Low Interest: [monitor]

KEY CONSIDERATIONS: What must we address to succeed?
```

### Trade-off Analysis

Explicit comparison when you can't have everything.

**Template:**
```
Analyze trade-offs for [DECISION]:

COMPETING VALUES:
- [Value A] vs [Value B]
- [Value C] vs [Value D]

For each trade-off pair:
1. What do we gain by prioritizing one?
2. What do we lose?
3. Is the trade-off reversible?
4. At what point does the trade-off flip?

RECOMMENDATION: Given [priorities], optimize for [chosen values] while maintaining minimum acceptable levels of [sacrificed values].
```

## Advanced Patterns

### Pre-Mortem Analysis

Imagine failure and work backward to prevent it.

**Template:**
```
Conduct pre-mortem for [PROJECT/DECISION]:

SCENARIO: It is [FUTURE DATE]. The project has failed spectacularly.

IMAGINATION EXERCISE:
1. What went wrong? (List 5-10 failure modes)
2. What warning signs did we ignore?
3. What assumptions proved false?
4. What external factors blindsided us?

For each failure mode:
- Likelihood if unaddressed
- Early warning indicators
- Preventive actions we can take now

OUTPUT: Priority-ranked list of risks with prevention strategies.
```

### Opportunity Cost Framework

Evaluate hidden costs of decisions.

**Template:**
```
Analyze opportunity costs for choosing [OPTION A] over alternatives:

DIRECT COSTS of Option A:
- [explicit costs]

OPPORTUNITY COSTS (what we give up):
- Option B would have provided: [benefits foregone]
- Option C would have provided: [benefits foregone]
- Time/resources spent here can't be spent on: [alternatives]

REVERSIBILITY:
- Can we change course later? At what cost?
- What options does this decision close off permanently?

CONCLUSION: Is Option A worth both its direct costs AND opportunity costs?
```

### Systems Thinking Analysis

Understand complex interconnections and feedback loops.

**Template:**
```
Analyze [SYSTEM/SITUATION] using systems thinking:

SYSTEM BOUNDARIES:
- What's inside the system? [components]
- What's outside? [environment]
- Where are the interfaces?

FEEDBACK LOOPS:
- Reinforcing loops (growth/decline): [describe]
- Balancing loops (stability): [describe]

DELAYS:
- Where are time lags between cause and effect?
- How do delays create unexpected behavior?

LEVERAGE POINTS:
- Where would small changes have large effects?
- What are the high-leverage interventions?

UNINTENDED CONSEQUENCES:
- What second-order effects might our intervention cause?
- How might the system adapt to resist change?
```

### Assumption Mapping

Surface and test hidden assumptions.

**Template:**
```
Map assumptions underlying [PLAN/STRATEGY]:

ASSUMPTION CATEGORIES:

1. MARKET ASSUMPTIONS:
   - [assumption]: How would we test this? What if wrong?

2. CAPABILITY ASSUMPTIONS:
   - [assumption]: How would we test this? What if wrong?

3. RESOURCE ASSUMPTIONS:
   - [assumption]: How would we test this? What if wrong?

4. TIMING ASSUMPTIONS:
   - [assumption]: How would we test this? What if wrong?

CRITICAL ASSUMPTIONS (plan fails if wrong):
- [assumption 1]: Confidence level, validation approach
- [assumption 2]: Confidence level, validation approach

ASSUMPTION TESTING PLAN: What can we do this week to validate critical assumptions?
```

### Decision Journal Template

Document decisions for future learning.

**Template:**
```
DECISION RECORD: [Decision Title]

DATE: [date]
DECISION MAKER: [who]

CONTEXT:
- Situation that prompted decision
- Constraints and pressures

OPTIONS CONSIDERED:
- Option A: [description, pros, cons]
- Option B: [description, pros, cons]
- Option C: [description, pros, cons]

DECISION: [chosen option]

RATIONALE:
- Primary reasons for choice
- Key assumptions made
- What information we wish we had

EXPECTED OUTCOMES:
- Success metrics
- Timeline for evaluation

REVIEW DATE: [when to assess outcome]
```

**Use:** Record at decision time, revisit at review date to learn from outcomes.

---

# Education Patterns

Patterns for explanations, tutoring, curriculum design, and assessment creation.

## Beginner Patterns

### ELI-X (Explain Like I'm X)

Adapt explanations to specific comprehension levels.

**Template:**
```
Explain [TOPIC] for [TARGET AUDIENCE].

Use:
- Simple language appropriate for their level
- Relatable analogies from their experience
- Concrete examples they would encounter
- Step-by-step breakdown where needed

Avoid:
- Jargon without definition
- Assumptions about prior knowledge
- Abstract concepts without grounding
```

**Examples:**
- "Explain a lunar eclipse for an 8-year-old using everyday objects they might see at home."
- "Explain covalent bonding as if I were a 10th grader who understands atoms but not molecular structures."
- "Explain Kubernetes to a senior executive who understands business but not infrastructure."

### Basic Quiz Generation

Create assessment questions with specified parameters.

**Template:**
```
Create [NUMBER] [QUESTION TYPE] questions on [TOPIC] for [GRADE LEVEL].

Parameters:
- Difficulty: [easy/medium/hard]
- Question types: [multiple choice / short answer / true-false]
- Focus areas: [specific subtopics]

Format each question as:
1. [Question]
   a) [Option A]
   b) [Option B]
   c) [Option C]
   d) [Option D]

   Correct Answer: [letter]
   Explanation: [why this is correct and others aren't]
```

### Concept Definition Generator

Create structured definitions with examples and connections.

**Template:**
```
Define [CONCEPT] for [GRADE LEVEL / AUDIENCE] in [SUBJECT AREA].

Include:
1. Clear, age-appropriate definition
2. 2-3 examples showing the concept in action
3. 1-2 non-examples (what it is NOT)
4. Connection to concepts they already know
5. A memorable analogy or mnemonic

Verify the explanation doesn't oversimplify to the point of inaccuracy.
```

## Intermediate Patterns

### PARTS Framework Lesson Plan

Comprehensive lesson planning using Persona, Aim, Recipients, Theme, Structure.

**Template:**
```
Create a lesson plan using the PARTS framework:

PERSONA: You are an expert [SUBJECT] teacher
AIM: Students will be able to [LEARNING OBJECTIVE]
RECIPIENTS: [GRADE LEVEL] students who [PRIOR KNOWLEDGE/CHARACTERISTICS]
THEME: [TOPIC/CONCEPT]
STRUCTURE: [DURATION] lesson

LESSON PLAN:

1. WARM-UP ([X] minutes):
   - Activation activity connecting to prior knowledge

2. DIRECT INSTRUCTION ([X] minutes):
   - Key concepts with explanations
   - Visual aids or demonstrations

3. GUIDED PRACTICE ([X] minutes):
   - Structured activity with scaffolding
   - Check for understanding questions

4. INDEPENDENT PRACTICE ([X] minutes):
   - Student application of concepts
   - Differentiation options

5. ASSESSMENT:
   - How to check if objective is met
   - Exit ticket or formative assessment

6. DIFFERENTIATION:
   - Supports for struggling learners
   - Extensions for advanced learners

MATERIALS NEEDED: [list]
STANDARDS ALIGNMENT: [if applicable]
```

### Adaptive Difficulty Tutoring

Responsive tutoring that adjusts based on understanding.

**Template:**
```
You are a patient, encouraging tutor helping with [SUBJECT/TOPIC].

TUTORING APPROACH:
1. Begin by asking what specific aspect they need help with
2. Gauge understanding with 1-2 diagnostic questions
3. Identify any misconceptions

ADAPTATION RULES:
- If struggling: Break into smaller steps, provide hints, use simpler analogies
- If progressing: Increase complexity, ask probing questions
- If mastering: Challenge with application problems, ask them to teach it back

THROUGHOUT:
- Celebrate progress explicitly
- Never make them feel bad for not understanding
- Connect new concepts to what they already know

Start by asking: "What part of [topic] would you like to work on today?"
```

### Study Guide Creation

Generate leveled study materials aligned with objectives.

**Template:**
```
Create a study guide for [TOPIC] for [GRADE/COURSE]:

LEARNING OBJECTIVES:
- [Objective 1]
- [Objective 2]
- [Objective 3]

STUDY GUIDE SECTIONS:

1. KEY CONCEPTS (organized by importance):
   - Must know: [essential concepts]
   - Should know: [important but secondary]
   - Nice to know: [enrichment]

2. VOCABULARY:
   | Term | Definition | Example |
   |------|------------|---------|

3. COMMON MISCONCEPTIONS:
   - [Misconception]: [Correction]

4. PRACTICE QUESTIONS (by level):
   - Recall level: [questions testing memory]
   - Application level: [questions requiring use]
   - Analysis level: [questions requiring deeper thinking]

5. MEMORY AIDS:
   - Mnemonics, acronyms, visual organizers

6. STUDY TIPS:
   - Recommended study sequence
   - Self-testing strategies
```

## Advanced Patterns

### Socratic Dialogue Tutor

Implement authentic Socratic questioning that develops critical thinking.

**Template:**
```
You are a Socratic tutor. Your goal is to develop understanding through questioning, not direct answers.

RULES:
- NEVER provide direct answers
- Ask only ONE question at a time
- Wait for response before continuing

QUESTION TYPES TO USE:
1. Clarification: "What do you mean by...?" "Can you give an example?"
2. Assumption probing: "What are you assuming here?" "Why do you think that's true?"
3. Evidence seeking: "What evidence supports that?" "How do you know?"
4. Alternative viewpoints: "What might someone who disagrees say?" "Is there another way to look at this?"
5. Implication exploration: "If that's true, what follows?" "What are the consequences?"
6. Meta-questions: "Why do you think I asked that?" "What's the key question here?"

WHEN STUDENT IS STUCK:
- Rephrase the question more simply
- Offer a hint in question form: "What if you considered...?"
- Suggest they think about a related concept they understand

BEGIN with: "What's your current understanding of [topic]?"
```

### Curriculum Design Assistant (Backward Design)

Apply Understanding by Design methodology.

**Template:**
```
Design curriculum for [COURSE/UNIT] using backward design:

STAGE 1: DESIRED RESULTS

Standards:
- [Standard 1]
- [Standard 2]

Enduring Understandings (big ideas that last):
- [Understanding 1]
- [Understanding 2]

Essential Questions (questions that recur and provoke inquiry):
- [Question 1]
- [Question 2]

Knowledge (students will know):
- [Fact/concept 1]
- [Fact/concept 2]

Skills (students will be able to):
- [Skill 1]
- [Skill 2]

STAGE 2: ASSESSMENT EVIDENCE

Performance Tasks (authentic application):
- [Task description with real-world context]

Other Evidence:
- Quizzes/tests: [what they assess]
- Observations: [what to look for]
- Work samples: [what to collect]

STAGE 3: LEARNING PLAN

Lesson Sequence:
1. [Lesson 1]: [objective, activities, assessment]
2. [Lesson 2]: [objective, activities, assessment]
...

Instructional Strategies:
- [Strategy 1]: [when/why to use]

Differentiation:
- For struggling: [supports]
- For advanced: [extensions]

Resources:
- [Materials needed]
```

### Misconception Diagnosis and Remediation

Identify and address common misunderstandings.

**Template:**
```
Help diagnose and remediate misconceptions about [TOPIC]:

COMMON MISCONCEPTIONS IN THIS TOPIC:
1. [Misconception]: [Why students think this]
2. [Misconception]: [Why students think this]
3. [Misconception]: [Why students think this]

DIAGNOSTIC QUESTIONS:
Questions that reveal which misconception a student holds:
- [Question 1]: If they answer [X], they likely believe [misconception A]
- [Question 2]: If they answer [Y], they likely believe [misconception B]

REMEDIATION STRATEGIES:
For each misconception:
- Cognitive conflict: [activity that creates contradiction]
- Correct model: [accurate explanation]
- Practice: [exercises that reinforce correct understanding]
- Check: [how to verify misconception is resolved]

Start diagnosis by asking: "[Diagnostic question that reveals common misconceptions]"
```

---

# Prompt Audit Checklist

Systematic review framework for evaluating and improving prompts.

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

## Model-Specific Checks

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

---

# Model Optimization Guides

> **Warning:** Model capabilities change frequently. Always consult current documentation for the latest best practices.

Optimization guides for major AI models: Claude, Gemini, and GPT. Each section covers model-specific characteristics, parameter settings, and patterns that maximize performance.

## Claude

Claude is a specification-driven model that rewards extreme precision over assumed intent. It follows instructions literally—powerful when prompted correctly, unforgiving when vague.

### Key Characteristics

| Trait | Implication |
|-------|-------------|
| Literal instruction following | Be explicit about everything; Claude won't infer "good" means "fully-featured" |
| XML tag training | Use XML structure; Claude treats it as native formatting |
| Extended thinking (up to 64K tokens) | Enable for complex reasoning; disable for simple tasks |
| Conservative behavior | More likely to acknowledge uncertainty; less prone to harmful outputs |
| Reduced sycophancy | Won't agree just to please; gives honest assessments |
| Context awareness | Tracks token usage; maintains coherent multi-hour sessions |

### XML Structure (Required)

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

### Explicitness is Non-Negotiable

Claude follows specifications precisely without improvisation.

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
```

### Provide Motivation

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

### Extended Thinking

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

- **Bad:** "First identify variables, then set up equation, then solve for x."
- **Good:** "Think about this math problem thoroughly. Consider multiple approaches and choose the most efficient path."

### Parameter Settings

**Breaking change:** Cannot specify both temperature AND top_p. Choose one.

| Task Type | Temperature |
|-----------|-------------|
| Analytical, factual, coding | 0.0 - 0.3 |
| Balanced, general conversation | 0.4 - 0.7 |
| Creative, brainstorming | 0.8 - 1.0 |

**max_tokens:** No default exists—must specify. Max 64K for output. Recommended: 4,000 for typical tasks.

### Tool Use

Tool description quality is the #1 factor in tool use performance.

**Minimum 3-4 sentences per tool covering:**
- What it does
- What it returns
- When to use it
- Format expectations
- Limitations

### Long Context Strategies

Claude supports 200K tokens standard (1M with beta headers).

**Structure:**
1. Place long documents (20K+ tokens) at TOP of prompt
2. Put instructions at the END
3. Use anchor phrases: "Based on the information above..."

**Context decay:** Quality drops when approaching limits. Start fresh sessions at 70-80% capacity.

### Claude Anti-Patterns to Avoid

- **Prescriptive reasoning steps:** State goals, let Claude choose approach
- **Over-constraining roles:** Keep personas specific but not restrictive
- **Minimal tool descriptions:** Always 3-4 sentences covering what/when/how/limitations
- **Ignoring extended thinking overhead:** Enable only for tasks requiring deliberation
- **Forcing entire repos into context:** Use RAG to retrieve relevant files per query
- **One-and-done prompting:** Test 2-3 variations, iterate on winner

## Gemini

Gemini achieves breakthrough reasoning while requiring simpler, more direct prompts. Directness over persuasion, structure over verbosity, temperature at 1.0 always.

### Key Characteristics

| Trait | Implication |
|-------|-------------|
| 1M token context | Largest context window; process entire codebases |
| Temperature locked at 1.0 | Do NOT lower temperature—causes looping |
| Native multimodal | Text, image, video, audio in unified stack |
| Deep Think mode | Extended reasoning for complex problems |
| Reduced sycophancy | Direct, honest responses |

### Critical: Temperature at 1.0

**This is the most important Gemini-specific setting.**

```python
# DON'T DO THIS - causes looping and degradation
config={"temperature": 0.2}

# DO THIS - use default or explicitly set to 1.0
config={"temperature": 1.0}  # Or omit entirely
```

**Why:** Gemini's reasoning capabilities are optimized for temperature 1.0. The model handles determinism internally through its thinking mechanisms. Lowering temperature causes unexpected behavior.

### System Instructions

Be concise and direct. Gemini responds to clear instructions without persuasive language.

**What works:**
- Clear roles: "You are a senior solution architect specializing in cloud infrastructure"
- Output constraints: "Be objective. Cite sources. Avoid corporate jargon."
- Verbosity level: "Provide direct, efficient answers. Only elaborate when requested."

**What doesn't work:**
- Overly long or persuasive instructions
- Complex Chain-of-Thought templates from older models
- Putting sensitive information in system instructions

### Prompt Structure

Use XML or Markdown consistently (never mix within a single prompt).

### Long Context Processing

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

### Deep Think Mode

Extended reasoning for complex problems.

**When to enable:**
- Abstract reasoning problems
- Multi-step mathematical proofs
- Complex analysis requiring exploration

**When to disable:**
- Simple queries
- Speed-critical applications
- Tasks where standard reasoning suffices

### Media Resolution Control

Control token usage for different media types:

| Setting | Best For |
|---------|----------|
| `media_resolution_low` | General video action recognition |
| `media_resolution_medium` | PDFs (quality saturates here) |
| `media_resolution_high` | Images; video with dense text |

### Gemini Anti-Patterns to Avoid

- **Lowering temperature:** Keep at 1.0—Gemini handles determinism internally
- **Complex CoT templates:** Direct instructions work better
- **Mixing XML and Markdown:** Pick one format and use consistently
- **Instructions before context:** Context first, instructions last
- **Over-prompting:** Concise, direct statements work better

## GPT

GPT features adaptive reasoning that dynamically adjusts thinking time—faster on simple tasks while maintaining deep reasoning for complex problems. Cost-efficient with excellent instruction following.

### Key Characteristics

| Trait | Implication |
|-------|-------------|
| Adaptive reasoning | Automatically allocates compute based on complexity |
| Cost efficient | $1.25/M input, 90% caching discounts |
| Three reasoning modes | none/minimal/medium/high for different use cases |
| Improved steerability | Better personality and formatting control |
| apply_patch tool | 35% fewer code edit failures |

### Reasoning Modes

Set via `reasoning_effort` parameter:

| Mode | Use Case | Token Impact |
|------|----------|--------------|
| `none` | Simple lookups, low-latency needs | Zero reasoning tokens |
| `minimal` | Basic tasks | Light reasoning |
| `medium` | Default balanced mode | Moderate reasoning |
| `high` | Complex problems, algorithm design | Deep exploration |

**Selection heuristic:**
- Simple extraction/lookup -> `none`
- Typical business logic -> `medium`
- Novel algorithm design or debugging -> `high`

### Persistence Instructions

GPT models tend to terminate prematurely on complex tasks. Explicit persistence instructions are critical:

```xml
<solution_persistence>
Treat yourself as an autonomous senior developer.
Persist until task is fully handled end-to-end.
Do not stop at partial fixes or ask for permission to continue.
</solution_persistence>
```

**Real-world impact:** Without persistence instructions, GPT fixed 2 of 17 TypeScript errors and stopped. With instructions, completed all 17 fixes autonomously.

### Verbosity Control

Three-tier verbosity management:

1. **Global API Parameter:** Set in API call
2. **Prompt-Level Override:** Specify in prompt
3. **Task-Specific Exceptions:** Different verbosity for code vs. status updates

### Tool Calling

Separate tool definitions from usage instructions:
- **Concise Tool Definition:** What it does and parameters
- **Detailed Usage Rules (in system prompt):** When to use, examples, error handling

### Native Code Tools

- **apply_patch:** Native tool for file operations with 35% fewer failures
- **shell:** Proposes bash commands with timeout and output limits

### Instruction Hierarchy

Priority order (highest to lowest):
1. **System messages** — Highest priority
2. **Developer messages** — Equivalent to system
3. **User messages** — Lowest priority

**Security implication:** System-level constraints override user attempts at prompt injection.

### GPT Anti-Patterns to Avoid

- **Missing persistence instructions:** Explicit "persist until fully resolved" instructions
- **Wrong reasoning mode:** Match mode to task complexity
- **Verbose tool definitions:** Concise definition + detailed rules in system prompt
- **Mixing verbosity expectations:** Tiered verbosity with explicit exceptions
- **Ignoring instruction hierarchy:** Put constraints in system messages
- **Premature termination:** Persistence instructions with specific completion criteria

---

# Agentic Prompt Patterns

Patterns for building AI agents that reason, use tools, and collaborate. These patterns enable more sophisticated AI workflows beyond single-turn prompts.

## ReAct Workflows

ReAct (Reasoning + Acting) combines explicit reasoning with tool actions in a systematic loop.

### Core Pattern

The ReAct cycle:

```
THOUGHT: [Analyze current state, decide what to investigate/do next]
ACTION: [Execute tool or operation]
OBSERVATION: [Record what was learned]
... repeat until goal achieved ...
CONCLUSION: [Summarize findings and result]
```

Each cycle builds on previous observations, creating a traceable chain of reasoning.

### When to Use ReAct

**Good fit:**
- Debugging (systematic investigation)
- Research requiring multiple sources
- Multi-step workflows with dependencies
- Exploration where path isn't predetermined
- Tasks requiring verification of intermediate steps

**Poor fit:**
- Simple, single-step tasks
- Tasks with known, fixed procedures
- Speed-critical applications (overhead of explicit reasoning)
- Tasks where tool sequence is predetermined

### Basic ReAct Template

```
Accomplish [GOAL] using the ReAct pattern.

For each step:

THOUGHT: What do I know so far? What should I investigate or do next? Why?

ACTION: [Choose one]
- Use tool: [tool_name] with [parameters]
- Make decision: [decision and rationale]
- Request information: [what's needed]

OBSERVATION: What did I learn from this action? How does it change my understanding?

Continue this cycle until:
1. Goal is fully accomplished
2. OR you've determined the goal cannot be accomplished (explain why)

Begin with your first THOUGHT about the most promising starting point.
```

### ReAct with Explicit State Tracking

```
Accomplish [GOAL] using ReAct with state tracking.

Maintain running state:
- KNOWN FACTS: [accumulate verified information]
- HYPOTHESES: [current working theories]
- OPEN QUESTIONS: [what still needs investigation]
- ACTIONS TAKEN: [log of completed actions]

For each cycle:

THOUGHT:
- Current state summary
- What the most valuable next action would be
- Expected outcome

ACTION: [specific action]

OBSERVATION: [result and new information]

STATE UPDATE:
- New facts learned: [add to KNOWN FACTS]
- Hypotheses confirmed/rejected: [update HYPOTHESES]
- New questions raised: [add to OPEN QUESTIONS]
- Action logged: [add to ACTIONS TAKEN]

Continue until goal achieved or determined impossible.
```

### Debugging with ReAct

```
Debug [ISSUE DESCRIPTION] using ReAct methodology.

ISSUE: [symptoms, error messages, reproduction steps]

For each investigation cycle:

THOUGHT:
- What are the possible causes based on current evidence?
- Which hypothesis is most likely?
- What's the most efficient way to test it?

ACTION: [Choose one]
- Read file: [path] to examine code
- Run command: [command] to test behavior
- Search: [term] to find related code
- Make edit: [change] to test hypothesis

OBSERVATION:
- What did I find?
- Does this confirm or reject my hypothesis?
- What new information does this provide?

Continue until:
1. Root cause identified
2. Fix implemented
3. Fix verified through testing

FINAL REPORT:
- Root cause: [explanation]
- Fix applied: [what was changed]
- Verification: [how we know it's fixed]
```

### Error Handling in ReAct

Handle failures gracefully:

```
ACTION: [attempted action]

OBSERVATION: FAILED - [error type]: [error message]

THOUGHT:
- Why did this fail? [analysis]
- Is this recoverable? [yes/no]
- If yes, what's the alternative approach?
- If no, what should I report?

[Either retry with modification or escalate]
```

**Common recovery patterns:**

| Error Type | Recovery Strategy |
|------------|-------------------|
| Tool timeout | Retry with simpler query or break into parts |
| Resource not found | Verify path, search for alternatives |
| Permission denied | Flag for user, suggest workaround |
| Rate limited | Wait and retry, or use alternative source |
| Invalid input | Reformat and retry |

## Multi-Agent Patterns

Orchestrate multiple specialized agents for complex tasks requiring diverse expertise or parallel processing.

### When to Use Multi-Agent

**Good fit:**
- Tasks requiring diverse expertise (technical + business + legal)
- Parallel research across different domains
- Adversarial analysis (red team / blue team)
- Tasks benefiting from multiple perspectives
- Complex workflows with distinct phases

**Poor fit:**
- Simple tasks a single agent handles well
- Tasks requiring tight coherence (multi-agent adds inconsistency)
- Speed-critical applications (orchestration adds latency)
- Tasks where expertise domains overlap heavily

### Pattern 1: Hub and Spoke (Orchestrator + Specialists)

One coordinator agent delegates to specialized agents and synthesizes results.

```
                    +--------------+
                    | Orchestrator |
                    |    Agent     |
                    +------+-------+
              +------------+------------+
              v            v            v
        +---------+  +---------+  +---------+
        |Specialist|  |Specialist|  |Specialist|
        | Agent A  |  | Agent B  |  | Agent C  |
        +---------+  +---------+  +---------+
```

**Best for:** Research tasks, analysis requiring multiple expert perspectives.

### Pattern 2: Pipeline (Sequential Processing)

Agents process in sequence, each building on previous output.

```
+---------+    +---------+    +---------+    +---------+
| Agent A | -> | Agent B | -> | Agent C | -> | Agent D |
| Research|    | Analysis|    | Draft   |    | Review  |
+---------+    +---------+    +---------+    +---------+
```

**Best for:** Workflows with clear phases (research -> analysis -> creation -> review).

### Pattern 3: Adversarial (Red Team / Blue Team)

Agents argue opposing positions to stress-test ideas.

```
Analyze this proposition: [STATEMENT OR STRATEGY]

BLUE TEAM (Advocate):
Build the strongest possible case supporting this proposition.
- Key arguments with evidence
- Best-case scenarios
- Why objections fail

RED TEAM (Critic):
Identify flaws, risks, and counterarguments.
- Challenge assumptions
- Worst-case scenarios
- Why arguments fail

PURPLE TEAM (Judge):
Review both team outputs and synthesize:
- Which Blue arguments survive Red scrutiny?
- Which Red concerns are legitimate vs. overblown?
- What modifications would strengthen the proposition?
```

**Best for:** Strategy validation, risk assessment, decision support.

### Pattern 4: Master-Clone (Dynamic Spawning)

Main agent spawns focused clones for parallel processing.

**Best for:** Tasks with parallel sub-components, when you need to maintain unified state while processing in parallel.

### Orchestration Strategies

**Parallel Execution:**
All agents work simultaneously on different aspects.

**Sequential with Gates:**
Each agent must complete before next begins, with quality gates.

**Iterative Refinement:**
Agents review each other's work in cycles.

### Information Sharing Protocols

**Structured Handoff:**
```
=== HANDOFF: [Source Agent] -> [Target Agent] ===

CONTEXT: [Why this handoff is happening]

KEY FINDINGS:
- [Finding 1]
- [Finding 2]

OPEN QUESTIONS:
- [Question for target agent]

RECOMMENDED FOCUS:
- [Where target agent should concentrate]

=== END HANDOFF ===
```

### Synthesis Patterns

**Weighted Integration:**
Assign weights to different agents based on relevance to the decision.

**Consensus Building:**
- Points all agents agree on -> High confidence findings
- Points with majority agreement -> Medium confidence findings
- Points of disagreement -> Flag for human review

### Multi-Agent Anti-Patterns to Avoid

- **Overlapping Responsibilities:** Clear domain boundaries with minimal overlap
- **No Synthesis Step:** Explicit orchestrator or synthesis agent
- **Over-Engineering Simple Tasks:** Match architecture complexity to task complexity
- **Ignoring Agent Conflicts:** Explicit conflict resolution protocol
- **No Exit Criteria:** Maximum iterations and convergence criteria

## Tool Definitions

Tool description quality is the single most important factor in reliable tool use. Detailed descriptions produce 54% improvement in task success.

### Why Tool Descriptions Matter

Models decide when and how to use tools based entirely on the descriptions you provide. Vague descriptions lead to:
- Random tool selection
- Parameter guessing
- Missing edge cases
- Failed workflows

### Required Elements

**Minimum Description Length: 3-4 sentences**

Every tool description should answer:
1. **What does it do?** (core function)
2. **What does it return?** (output format)
3. **What does it NOT return?** (limitations)
4. **When should it be used?** (trigger conditions)
5. **What format does it expect?** (input requirements)
6. **What are the edge cases?** (special handling)

### Example: Good Tool Definition

```json
{
  "name": "search_database",
  "description": "Search the customer database by name, email, or customer ID. Returns an array of matching customer records including name, email, signup_date, and subscription_tier. Supports partial matching for names and emails (minimum 3 characters). LIMITATION: Maximum 50 results returned; use filters for large result sets. WHEN TO USE: When user asks about a specific customer, needs to look up customer details, or wants to find customers matching criteria.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term. Can be: full/partial name (e.g., 'John', 'John Smith'), email address or partial email (e.g., 'john@', '@company.com'), or exact customer ID (e.g., 'CUST-12345'). Minimum 3 characters for partial matching."
      },
      "filter": {
        "type": "string",
        "enum": ["all", "active", "churned", "trial"],
        "description": "Filter results by customer status. Default: 'all'"
      }
    },
    "required": ["query"]
  }
}
```

### Common Mistakes

- **Relying on Tool Name Alone:** Describe exactly what can be searched and what's returned
- **Missing Return Format:** Specify fields and structure
- **No Trigger Guidance:** Include "WHEN TO USE:" section
- **Ambiguous Parameters:** Include format, examples, valid ranges
- **No Limitations:** Explicitly state what it can't do
- **Conflicting Tools Without Disambiguation:** Clear guidance on which to use when

### Template for New Tools

```json
{
  "name": "[verb_noun format, e.g., search_customers, create_task]",
  "description": "[1. What it does] [2. What it returns] [3. Format requirements] LIMITATION: [What it cannot do] WHEN TO USE: [Trigger conditions]",
  "input_schema": {
    "type": "object",
    "properties": {
      "[param_name]": {
        "type": "[type]",
        "description": "[What this parameter controls]. Format: [expected format with examples]. [Edge case handling or defaults]."
      }
    },
    "required": ["[required_params]"]
  }
}
```
