# Analysis & Research Patterns

Patterns for business analysis, research synthesis, competitive intelligence, and strategic planning.

## Table of Contents
- [Beginner Patterns](#beginner-patterns)
- [Intermediate Patterns](#intermediate-patterns)
- [Advanced Patterns](#advanced-patterns)

---

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

**Example:**
```
Compare PostgreSQL, MongoDB, and DynamoDB on:
1. Data structure flexibility
2. Query complexity support
3. Horizontal scaling capabilities
4. Cost at 100GB scale
5. Learning curve for team
```

---

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

**Example:**
```
Summarize this earnings call transcript for the sales team.

FOCUS: Customer acquisition metrics and competitive mentions
LENGTH: 5 bullet points
INCLUDE: Any new product announcements affecting sales positioning
EXCLUDE: Tax implications and accounting methodology
```

---

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

---

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

---

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

---

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

**Example:**
```
Evaluate three market expansion strategies using:

- Growth potential: 40% weight
- Resource requirements: 25% weight
- Risk level: 20% weight
- Time to profitability: 15% weight

Options:
A. Geographic expansion to APAC
B. Vertical expansion to healthcare
C. Product expansion to enterprise tier
```

---

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

---

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

---

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

---

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

---

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

---

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

---

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

**Example:**
```
Analyze acquisition target using:

AGENT 1 - Financial Analyst: Revenue quality, margin sustainability, cash flow
AGENT 2 - Market Strategist: Competitive position, market trends, growth potential
AGENT 3 - Operations Expert: Integration complexity, synergy realism, culture fit
AGENT 4 - Risk Assessor: Deal-breakers, hidden liabilities, regulatory issues

Synthesize into investment recommendation.
```
