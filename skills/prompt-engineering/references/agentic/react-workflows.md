# ReAct Workflows

ReAct (Reasoning + Acting) combines explicit reasoning with tool actions in a systematic loop. The model thinks about what to do, takes an action, observes the result, and decides next steps.

## Table of Contents
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
