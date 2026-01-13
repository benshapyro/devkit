# Agentic Prompt Patterns

Patterns for building AI agents that reason, use tools, and collaborate. These patterns enable more sophisticated AI workflows beyond single-turn prompts.

## Table of Contents

- [ReAct Workflows](#react-workflows)
- [Multi-Agent Patterns](#multi-agent-patterns)
- [Tool Definitions](#tool-definitions)

---

# ReAct Workflows

ReAct (Reasoning + Acting) combines explicit reasoning with tool actions in a systematic loop. The model thinks about what to do, takes an action, observes the result, and decides next steps.

## ReAct Table of Contents
- [Core Pattern](#core-pattern)
- [When to Use ReAct](#when-to-use-react)
- [Implementation Templates](#implementation-templates)
- [Debugging with ReAct](#debugging-with-react)
- [Research with ReAct](#research-with-react)
- [Persistence and State](#persistence-and-state)
- [Error Handling](#error-handling)
- [Model-Specific Tips](#model-specific-tips)

---

## Core Pattern

The ReAct cycle:

```
THOUGHT: [Analyze current state, decide what to investigate/do next]
ACTION: [Execute tool or operation]
OBSERVATION: [Record what was learned]
... repeat until goal achieved ...
CONCLUSION: [Summarize findings and result]
```

Each cycle builds on previous observations, creating a traceable chain of reasoning.

---

## When to Use ReAct

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

---

## Implementation Templates

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

---

## Debugging with ReAct

Systematic bug investigation:

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

**Example debugging session:**

```
ISSUE: API returns 500 error on user creation

THOUGHT: 500 errors typically indicate server-side exceptions. Most likely causes:
database constraint violation, null pointer, or validation failure. Let me check
the error logs first.

ACTION: Run command: `tail -50 /var/log/app/error.log`

OBSERVATION: Log shows "IntegrityError: duplicate key value violates unique
constraint 'users_email_key'". The email uniqueness check is failing.

THOUGHT: The email already exists in database. But the frontend should prevent
duplicate submissions. Either: (1) frontend validation missing, (2) race condition
with concurrent requests, or (3) the specific email is edge case. Let me check
the user creation endpoint.

ACTION: Read file: `src/api/users.py`

OBSERVATION: No email existence check before INSERT. Frontend validation exists
but backend doesn't verify. Race condition possible.

THOUGHT: Need to add server-side email uniqueness check before INSERT. This will
return a proper 409 Conflict instead of 500 Internal Server Error.

ACTION: Make edit: Add email check to create_user function

OBSERVATION: Edit applied. Let me verify with a test.

ACTION: Run command: `pytest tests/test_users.py::test_duplicate_email -v`

OBSERVATION: Test passes. Duplicate email now returns 409 with helpful message.

CONCLUSION:
- Root cause: Missing server-side email uniqueness validation
- Fix: Added email existence check returning 409 Conflict
- Verification: Duplicate email test passes
```

---

## Research with ReAct

Multi-source information gathering:

```
Research [TOPIC] to answer [SPECIFIC QUESTIONS].

For each research cycle:

THOUGHT:
- What do I know about [topic] so far?
- What gaps remain in answering the questions?
- What source would be most likely to fill the highest-priority gap?

ACTION: [Choose one]
- Search web: [query] for [expected information type]
- Read document: [source] for [specific information]
- Cross-reference: [claim] against [alternative source]

OBSERVATION:
- Key information found: [facts]
- Source credibility: [assessment]
- Conflicts with previous information: [if any]
- New questions raised: [if any]

Continue until questions are adequately answered.

SYNTHESIS:
- Answer to question 1: [answer with sources]
- Answer to question 2: [answer with sources]
- Confidence level: [high/medium/low]
- Remaining uncertainties: [what couldn't be determined]
```

---

## Persistence and State

For long-running ReAct workflows, maintain explicit state:

### State Checkpoint Template

```
=== CHECKPOINT [timestamp] ===

GOAL: [original objective]

PROGRESS:
- [x] Step 1: [completed action and result]
- [x] Step 2: [completed action and result]
- [ ] Step 3: [pending action]

CURRENT STATE:
- Key findings: [list]
- Open questions: [list]
- Blockers: [if any]

NEXT ACTION: [what to do next and why]

=== END CHECKPOINT ===
```

### Recovery After Interruption

```
Resume ReAct workflow from checkpoint:

[PASTE CHECKPOINT]

Review checkpoint and continue from NEXT ACTION.
Verify previous findings are still valid before proceeding.
```

---

## Error Handling

Handle failures gracefully within ReAct:

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

---

## Model-Specific Tips

### Claude
- Use explicit thinking keywords ("think hard", "consider carefully")
- Extended thinking mode pairs well with ReAct for complex reasoning
- Don't prescribe exact reasoning steps—state goals instead

### GPT
- Add persistence instructions to prevent premature termination
- Use "Let's approach this step-by-step" to activate systematic reasoning
- Include explicit completion criteria

### Gemini
- Keep temperature at 1.0
- Benefits from structured output format requests
- Works well with self-critique pattern at observation step

---

## When NOT to Use Full ReAct

Sometimes the overhead isn't justified:

**Use simplified approach for:**
- Well-defined procedures with known steps
- Single-tool tasks
- Speed-critical operations
- Tasks where you just need the answer, not the reasoning trace

**Simplified template:**
```
[TASK]

Use available tools as needed. Report your final answer.
```

---

# Multi-Agent Patterns

Orchestrate multiple specialized agents for complex tasks requiring diverse expertise or parallel processing.

## Multi-Agent Table of Contents
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

---

# Tool Definitions

Tool description quality is the single most important factor in reliable tool use. Detailed descriptions produce 54% improvement in task success.

## Tool Definitions Table of Contents
- [Why Tool Descriptions Matter](#why-tool-descriptions-matter)
- [Anatomy of a Great Tool Definition](#anatomy-of-a-great-tool-definition)
- [Required Elements](#required-elements)
- [Examples by Quality Level](#examples-by-quality-level)
- [Model-Specific Considerations](#model-specific-considerations)
- [Common Mistakes](#common-mistakes)

---

## Why Tool Descriptions Matter

Models decide when and how to use tools based entirely on the descriptions you provide. Vague descriptions lead to:
- Random tool selection
- Parameter guessing
- Missing edge cases
- Failed workflows

**Research finding:** Detailed tool descriptions (6+ sentences covering what/how/when/limitations) show 54% performance improvement over minimal descriptions.

---

## Anatomy of a Great Tool Definition

Every tool description should answer these questions:

1. **What does it do?** (core function)
2. **What does it return?** (output format)
3. **What does it NOT return?** (limitations)
4. **When should it be used?** (trigger conditions)
5. **What format does it expect?** (input requirements)
6. **What are the edge cases?** (special handling)

---

## Required Elements

### Minimum Description Length: 3-4 sentences

```json
{
  "name": "tool_name",
  "description": "[Sentence 1: What it does] [Sentence 2: What it returns] [Sentence 3: When to use it] [Sentence 4: Limitations or format requirements]",
  "input_schema": {
    "type": "object",
    "properties": {
      "param_name": {
        "type": "string",
        "description": "[Detailed parameter description including format, examples, edge cases]"
      }
    },
    "required": ["param_name"]
  }
}
```

### Parameter Descriptions

Each parameter needs:
- Type and format expectations
- Valid examples
- Edge case handling
- Default behavior (if applicable)

---

## Examples by Quality Level

### ❌ Bad: Minimal Description

```json
{
  "name": "search_database",
  "description": "Search the customer database",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {"type": "string"}
    }
  }
}
```

**Problems:**
- No indication of what can be searched
- No return format specified
- No guidance on query format
- No limitations mentioned

---

### ⚠️ Mediocre: Partial Description

```json
{
  "name": "search_database",
  "description": "Search the customer database by name, email, or customer ID. Returns matching customer records.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term"
      }
    }
  }
}
```

**Problems:**
- Still no format guidance
- No limitations
- Parameter description too brief

---

### ✅ Good: Comprehensive Description

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
      },
      "limit": {
        "type": "integer",
        "description": "Maximum results to return. Default: 20, Maximum: 50"
      }
    },
    "required": ["query"]
  }
}
```

---

## Full Example: Weather Tool

```json
{
  "name": "get_weather",
  "description": "Get current weather information for a specific location. Returns temperature (in requested unit), weather conditions (sunny, cloudy, rainy, etc.), humidity percentage, and wind speed. IMPORTANT: Use city and state format for US locations (e.g., 'San Francisco, CA'). For international locations, include country (e.g., 'London, UK'). LIMITATION: Only returns current conditions—historical data and forecasts are not available through this tool. WHEN TO USE: When user asks about current weather, temperature, what to wear, or whether they need an umbrella.",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The location to get weather for. Format: 'City, State' for US (e.g., 'San Francisco, CA', 'New York, NY') or 'City, Country' for international (e.g., 'London, UK', 'Tokyo, Japan'). Be as specific as possible to avoid ambiguity."
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "Temperature unit for the response. Default: fahrenheit for US locations, celsius for international locations if not specified."
      }
    },
    "required": ["location"]
  }
}
```

---

## Full Example: File Operations Tool

```json
{
  "name": "read_file",
  "description": "Read the contents of a file from the project directory. Returns the full text content of the file as a string. Supports text files including .txt, .md, .json, .py, .js, .ts, .html, .css, and other text-based formats. LIMITATION: Cannot read binary files (images, PDFs, executables)—use appropriate tools for those formats. Maximum file size: 1MB. WHEN TO USE: When you need to examine file contents, understand existing code, check configuration, or reference documentation.",
  "input_schema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Relative path to the file from project root. Use forward slashes (e.g., 'src/components/Button.tsx', 'config/settings.json'). Do not include leading slash."
      },
      "encoding": {
        "type": "string",
        "enum": ["utf-8", "ascii", "latin-1"],
        "description": "File encoding. Default: 'utf-8'. Use 'latin-1' for legacy files with special characters."
      }
    },
    "required": ["path"]
  }
}
```

---

## Model-Specific Considerations

### Claude
- Integrates tools directly into message structure
- Benefits most from detailed descriptions
- Use `strict: true` for guaranteed schema conformance
- Opus defaults to chain-of-thought before tool calls

### GPT
- Separate tool definitions from usage rules
- Put detailed usage instructions in system prompt
- Include 2-3 examples in system prompt (not tool description)
- Use `tool_choice` to force specific tool when needed

### Gemini
- Native function calling support
- Benefits from clear trigger conditions
- Works well with hierarchical tool organization

---

## Common Mistakes

### 1. Relying on Tool Name Alone
❌ Assuming "search_customers" is self-explanatory
✅ Describe exactly what can be searched and what's returned

### 2. Missing Return Format
❌ "Returns customer information"
✅ "Returns JSON with fields: id, name, email, signup_date, status"

### 3. No Trigger Guidance
❌ Description only covers what tool does
✅ Include "WHEN TO USE:" section for disambiguation

### 4. Ambiguous Parameters
❌ `"query": {"type": "string"}`
✅ Include format, examples, valid ranges, edge cases

### 5. No Limitations
❌ Implying tool can do everything
✅ Explicitly state what it can't do, rate limits, size limits

### 6. Conflicting Tools Without Disambiguation
❌ Two similar tools with no guidance on which to use
✅ Clear "use X when... use Y when..." in descriptions

---

## Template for New Tools

```json
{
  "name": "[verb_noun format, e.g., search_customers, create_task]",
  "description": "[1. What it does—core function] [2. What it returns—format and fields] [3. Important format requirements or constraints] LIMITATION: [What it cannot do] WHEN TO USE: [Trigger conditions that should invoke this tool]",
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
