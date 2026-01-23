# Multi-Agent Patterns

Orchestrate multiple specialized agents for complex tasks requiring diverse expertise or parallel processing.

## Table of Contents
- [When to Use Multi-Agent](#when-to-use-multi-agent)
- [Architecture Patterns](#architecture-patterns)
- [Agent Role Design](#agent-role-design)
- [Orchestration Strategies](#orchestration-strategies)
- [Information Sharing Protocols](#information-sharing-protocols)
- [Synthesis Patterns](#synthesis-patterns)
- [Anti-Patterns to Avoid](#anti-patterns-to-avoid)

---

## When to Use Multi-Agent

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

---

## Architecture Patterns

### Pattern 1: Hub and Spoke (Orchestrator + Specialists)

One coordinator agent delegates to specialized agents and synthesizes results.

```
                    ┌─────────────┐
                    │ Orchestrator│
                    │   Agent     │
                    └──────┬──────┘
              ┌───────────┼───────────┐
              ▼           ▼           ▼
        ┌─────────┐ ┌─────────┐ ┌─────────┐
        │Specialist│ │Specialist│ │Specialist│
        │ Agent A  │ │ Agent B  │ │ Agent C  │
        └─────────┘ └─────────┘ └─────────┘
```

**Best for:** Research tasks, analysis requiring multiple expert perspectives.

**Template:**
```
You are an orchestrator coordinating analysis of [TOPIC].

Available specialist agents:
- Agent A ([EXPERTISE A]): Focuses on [domain]
- Agent B ([EXPERTISE B]): Focuses on [domain]  
- Agent C ([EXPERTISE C]): Focuses on [domain]

Your workflow:
1. Break down the problem into specialist-appropriate sub-tasks
2. Assign each sub-task to the appropriate specialist
3. Collect and review specialist outputs
4. Synthesize into unified analysis
5. Identify gaps and request additional specialist work if needed

Final output should integrate all perspectives into coherent recommendation.
```

---

### Pattern 2: Pipeline (Sequential Processing)

Agents process in sequence, each building on previous output.

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Agent A │ -> │ Agent B │ -> │ Agent C │ -> │ Agent D │
│ Research│    │ Analysis│    │ Draft   │    │ Review  │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**Best for:** Workflows with clear phases (research → analysis → creation → review).

**Template:**
```
Process [TASK] through this agent pipeline:

STAGE 1 - Research Agent:
- Role: Gather relevant information
- Input: [initial query]
- Output: Structured research findings

STAGE 2 - Analysis Agent:
- Role: Interpret research, identify patterns
- Input: Research findings from Stage 1
- Output: Analytical insights and recommendations

STAGE 3 - Draft Agent:
- Role: Create deliverable based on analysis
- Input: Analysis from Stage 2
- Output: Initial draft

STAGE 4 - Review Agent:
- Role: Quality check and refinement
- Input: Draft from Stage 3
- Output: Final polished deliverable

Each agent completes fully before passing to next stage.
```

---

### Pattern 3: Adversarial (Red Team / Blue Team)

Agents argue opposing positions to stress-test ideas.

```
┌─────────────┐         ┌─────────────┐
│  Blue Team  │◄───────►│  Red Team   │
│  (Advocate) │         │  (Critic)   │
└──────┬──────┘         └──────┬──────┘
       │                       │
       └──────────┬────────────┘
                  ▼
          ┌─────────────┐
          │ Purple Team │
          │   (Judge)   │
          └─────────────┘
```

**Best for:** Strategy validation, risk assessment, decision support.

**Template:**
```
Conduct adversarial analysis of: [PROPOSITION]

BLUE TEAM (Advocate):
Your goal is to build the strongest possible case FOR this proposition.
- Assume it's correct and find evidence
- Address anticipated objections preemptively
- Identify best-case scenarios
Output: Strongest arguments supporting the proposition

RED TEAM (Critic):
Your goal is to find every flaw, risk, and weakness.
- Assume hidden problems exist and find them
- Challenge every assumption
- Identify worst-case scenarios
Output: Strongest arguments against the proposition

PURPLE TEAM (Judge):
Review both team outputs and synthesize:
- Which Blue arguments survive Red scrutiny?
- Which Red concerns are legitimate vs. overblown?
- What modifications would strengthen the proposition?
Output: Balanced assessment with specific recommendations
```

---

### Pattern 4: Master-Clone (Dynamic Spawning)

Main agent spawns focused clones for parallel processing.

**Best for:** Tasks with parallel sub-components, when you need to maintain unified state while processing in parallel.

**Template:**
```
You are the master agent for [COMPLEX TASK].

When facing parallelizable sub-tasks:
1. Spawn focused Task() clones with specific objectives
2. Each clone works independently on its assignment
3. Collect clone outputs
4. Synthesize into unified result
5. Continue main workflow

Maintain central state tracking:
- Active clones: [list]
- Pending synthesis: [outputs awaiting integration]
- Unified findings: [integrated results]
```

---

## Agent Role Design

### Role Specification Template

```
AGENT: [Agent Name]

EXPERTISE: [Specific domain and depth level]

PERSPECTIVE: [How this agent views problems]

RESPONSIBILITIES:
- [Primary task 1]
- [Primary task 2]

CONSTRAINTS:
- [What this agent should NOT do]
- [Boundaries of expertise]

OUTPUT FORMAT:
- [Expected structure of agent output]

HANDOFF CRITERIA:
- [When to pass work to another agent]
```

### Example: Investment Analysis Team

```
AGENT: Financial Analyst
EXPERTISE: Quantitative financial analysis, valuation modeling
PERSPECTIVE: Numbers-driven, focuses on financial metrics
RESPONSIBILITIES:
- Revenue and margin analysis
- Cash flow assessment
- Valuation modeling (DCF, comparables)
CONSTRAINTS:
- Do not assess strategic fit or market dynamics (Market Strategist's domain)
- Do not evaluate operational risks (Risk Assessor's domain)
OUTPUT FORMAT:
- Key financial metrics with trends
- Valuation range with assumptions
- Financial red flags

---

AGENT: Market Strategist
EXPERTISE: Competitive analysis, market dynamics, growth potential
PERSPECTIVE: Strategic, focuses on positioning and opportunity
RESPONSIBILITIES:
- Competitive landscape mapping
- Market sizing and growth trends
- Strategic fit assessment
CONSTRAINTS:
- Do not perform financial modeling (Financial Analyst's domain)
- Do not assess integration complexity (Operations Expert's domain)
OUTPUT FORMAT:
- Market position assessment
- Growth potential analysis
- Strategic rationale

---

AGENT: Risk Assessor
EXPERTISE: Due diligence, risk identification, regulatory compliance
PERSPECTIVE: Skeptical, focuses on what could go wrong
RESPONSIBILITIES:
- Identify deal-breakers
- Regulatory and compliance risks
- Hidden liabilities assessment
CONSTRAINTS:
- Do not assess strategic value (Market Strategist's domain)
- Do not perform valuations (Financial Analyst's domain)
OUTPUT FORMAT:
- Risk matrix (likelihood x impact)
- Deal-breaker flags
- Mitigation recommendations
```

---

## Orchestration Strategies

### Parallel Execution
All agents work simultaneously on different aspects.

```
Execute these agents in parallel:
- Agent A: [task] → Output A
- Agent B: [task] → Output B
- Agent C: [task] → Output C

Then synthesize outputs A, B, C into unified result.
```

### Sequential with Gates
Each agent must complete before next begins, with quality gates.

```
Sequential execution with gates:

GATE 1: Agent A completes [task]
- Quality check: [criteria]
- Pass: Proceed to Agent B
- Fail: Agent A revises

GATE 2: Agent B completes [task] using Agent A output
- Quality check: [criteria]
- Pass: Proceed to Agent C
- Fail: Return to appropriate earlier stage
```

### Iterative Refinement
Agents review each other's work in cycles.

```
Iteration cycle:

ROUND 1:
- Agent A produces draft
- Agent B critiques draft
- Agent A revises based on critique

ROUND 2:
- Repeat until quality threshold met or max iterations reached

Convergence criteria: [what "done" looks like]
Maximum iterations: [cap to prevent infinite loops]
```

---

## Information Sharing Protocols

### Structured Handoff
```
=== HANDOFF: [Source Agent] → [Target Agent] ===

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

### Shared State Document
```
=== SHARED STATE ===

VERIFIED FACTS:
- [Fact 1] (Source: Agent A)
- [Fact 2] (Source: Agent B)

WORKING HYPOTHESES:
- [Hypothesis 1] (Status: Testing)
- [Hypothesis 2] (Status: Confirmed)

CONFLICTS:
- [Agent A says X, Agent B says Y] → Resolution needed

ACTION LOG:
- [Timestamp] Agent A: [action]
- [Timestamp] Agent B: [action]

=== END SHARED STATE ===
```

---

## Synthesis Patterns

### Weighted Integration
```
Synthesize agent outputs with these weights:
- Agent A (Financial): 40% weight for financial decisions
- Agent B (Strategic): 35% weight for market decisions
- Agent C (Risk): 25% weight for go/no-go decisions

Where agents conflict, higher-weighted agent prevails unless lower-weighted agent identifies deal-breaker.
```

### Consensus Building
```
Identify:
1. Points all agents agree on → High confidence findings
2. Points with majority agreement → Medium confidence findings
3. Points of disagreement → Flag for human review

Final recommendation should be supportable by all agents or explicitly note dissent.
```

---

## Anti-Patterns to Avoid

### 1. Overlapping Responsibilities
❌ Two agents both doing "analysis"
✅ Clear domain boundaries with minimal overlap

### 2. No Synthesis Step
❌ Dumping all agent outputs without integration
✅ Explicit orchestrator or synthesis agent

### 3. Over-Engineering Simple Tasks
❌ Multi-agent system for a straightforward analysis
✅ Match architecture complexity to task complexity

### 4. Ignoring Agent Conflicts
❌ Cherry-picking preferred outputs
✅ Explicit conflict resolution protocol

### 5. Rigid Naming Without Context
❌ Agents ignore each other unless explicitly named
✅ Clear handoff protocols and shared state

### 6. No Exit Criteria
❌ Agents iterating forever
✅ Maximum iterations and convergence criteria
