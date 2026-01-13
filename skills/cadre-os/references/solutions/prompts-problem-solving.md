# Problem-Solving Patterns

Patterns for decision-making, planning, risk assessment, and root cause analysis.

## Table of Contents
- [Beginner Patterns](#beginner-patterns)
- [Intermediate Patterns](#intermediate-patterns)
- [Advanced Patterns](#advanced-patterns)

---

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

---

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

---

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

---

## Intermediate Patterns

### Root Cause Analysis (5 Whys)

Drill down to underlying causes.

**Template:**
```
Conduct 5 Whys analysis for: [PROBLEM]

PROBLEM: [symptom or issue observed]

WHY 1: Why does [problem] occur?
→ [First-level cause]

WHY 2: Why does [first-level cause] occur?
→ [Second-level cause]

WHY 3: Why does [second-level cause] occur?
→ [Third-level cause]

WHY 4: Why does [third-level cause] occur?
→ [Fourth-level cause]

WHY 5: Why does [fourth-level cause] occur?
→ [Root cause]

ROOT CAUSE SUMMARY: [concise statement]
RECOMMENDED ACTION: [intervention at root cause level]
```

---

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

---

### Risk Assessment Matrix

Identify and prioritize risks.

**Template:**
```
Conduct risk assessment for [PROJECT/DECISION]:

For each identified risk:

| Risk | Likelihood (1-5) | Impact (1-5) | Risk Score | Mitigation |
|------|-----------------|--------------|------------|------------|
| [Risk 1] | [L] | [I] | [L×I] | [action] |
| [Risk 2] | [L] | [I] | [L×I] | [action] |

LIKELIHOOD SCALE:
1 = Rare, 2 = Unlikely, 3 = Possible, 4 = Likely, 5 = Almost Certain

IMPACT SCALE:
1 = Negligible, 2 = Minor, 3 = Moderate, 4 = Major, 5 = Severe

Prioritize risks with score ≥12 for immediate mitigation.
Identify any risks that are acceptable, require monitoring, or need contingency plans.
```

---

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

---

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

---

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

---

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

---

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

---

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

---

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
