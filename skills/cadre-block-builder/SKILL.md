---
name: cadre-block-builder
description: Creates implementation blocks for client engagements using compositional activity clusters. Use when (1) Planning new client work or scoping SOW components, (2) Defining project phases with month-by-month execution plans, (3) Creating blocks that go into client proposals or schedules. Generates both internal (detailed with risks/confidence) and client-facing (executive summary) versions. NOT for converting blocks to ClickUp (use project-resource-planner for that).
license: Complete terms in LICENSE.txt
---

# Cadre Block Builder

## Overview

This skill creates month-by-month implementation blocks for client engagements. Blocks are **compositional** - built from activity clusters that mix freely (Discovery + Integration + Testing) rather than locked into rigid project types.

**Key Capabilities**:
- Two-phase discovery workflow (broad search → targeted search)
- Compositional approach using 10 activity clusters
- Duration estimation based on cluster complexity
- Strategy/implementation boundary enforcement
- Risk analysis with plain English mitigation options
- Dual output generation (internal + client versions)
- Confidence scoring for internal planning
- Handoff preparation for `project-resource-planner`

---

## When to Use This Skill

✅ **Use for**:
- Creating blocks for new client SOWs
- Scoping phases of multi-month engagements
- Planning implementation work after strategy phase
- Defining month-by-month execution plans
- Generating client-facing project summaries

❌ **Don't use for**:
- Converting blocks to ClickUp tasks (use `project-resource-planner`)
- Quick time estimates without detailed planning
- Internal task tracking
- Ongoing project management

---

## Core Principles

### 1. Compositional, Not Categorical
Blocks combine activity clusters freely. Don't ask "What type of project?" Ask "What activities are we doing?"

**10 Activity Clusters**:
- Discovery & Strategy
- Process Design
- Integration
- Custom Development
- Automation
- AI/LLM Implementation
- Testing & QA
- Deployment
- Training & Enablement
- Optimization

See `references/activity-clusters.md` for detailed descriptions.

### 2. Strategy Boundary Enforcement
**Critical Rule**: Strategy blocks (Discovery + Process Design only) CANNOT include implementation clusters.

Implementation requires separate discovery after strategy approval. This protects both project quality and separate engagement revenue.

Script `enforce_strategy_boundary.py` validates this automatically.

### 3. Always Generate Both Versions
- **Internal**: Full detail, risks, confidence scores, technical notes, assumptions
- **Client**: Executive summary, outcomes, business value, no internal details

This prevents "we need a client version now" scrambling.

### 4. Conservative Estimation
Under-promise, over-deliver. Use complexity rubric to guide duration ranges, not optimistic guesses.

---

## Phase 1: Discovery Workflow

Follow this sequence for every block creation.

### Step 1: Initial Search Permission

Ask for broad search permission:

```
"Should I search for existing context about [Client/Project]? I'd check:
- Past project notes in knowledge base
- Gmail threads about this engagement  
- Slack discussions with [stakeholder names if known]
- Drive documents related to [initiative name if mentioned]

This helps me understand what context already exists."
```

**WAIT for user response before searching.**

### Step 2: Activity Cluster Identification

Ask user to describe what they're building. Listen for activities, don't force into categories.

```
"Tell me what you're building in this block. What activities are involved?

I'll listen for these types of work:
- Discovery & requirements
- Process mapping & design
- System integration
- Custom development
- Workflow automation
- AI/LLM implementation
- Testing & QA
- Deployment
- Training & documentation
- Ongoing optimization

Just describe the work - I'll identify which clusters apply."
```

After user describes, present identified clusters and validate:

```
"Based on your description, I see these activity clusters:
✓ Discovery & Strategy (requirements gathering, stakeholder interviews)
✓ Integration (connecting Salesforce to HubSpot)
✓ Testing & QA (validation before go-live)
✓ Training & Enablement (team onboarding on new workflow)

Did I miss anything or misunderstand what's included?"
```

### Step 3: Targeted Search Permission

Now that you know specifics, offer targeted searches:

```
"Now that I know you're building [specific solution], should I search for:
- Previous technical discussions about [technology mentioned]
- Similar integration work we've done before
- This client's documented system constraints
- Related requirements or specs that exist

This can inform duration estimates and risk identification."
```

**WAIT for user response before searching.**

### Step 4: Complexity Assessment

For each identified cluster, determine complexity using the rubric:

```
"For each activity cluster, help me understand complexity:

**Discovery & Strategy**:
- Simple: 1-2 stakeholders, clear problem (1-2 weeks)
- Medium: 3-5 stakeholders, moderate complexity (2-4 weeks)
- Complex: 10+ stakeholders, org change (4-8 weeks)
Which fits?

**Integration**:
- Simple: Pre-built connectors exist (2-4 weeks)
- Medium: Custom API work needed (4-8 weeks)
- Complex: Multiple systems, data mapping challenges (8-16 weeks)
Which fits?

[Continue for each cluster identified]
```

See `references/complexity-rubric.md` for full criteria.

### Step 5: Resource Gathering

Ask about team availability and timeline:

```
"Who's available and when?

From Cadre:
- Who's the PM/lead?
- What engineers are available?
- Any designers needed?

From Client:
- Who are the key stakeholders?
- How much time can they commit weekly?
- Who has final approval authority?

Timeline:
- When should this block start?
- Any hard deadlines or constraints?
- What's non-negotiable vs flexible?"
```

### Step 6: Strategy Boundary Check

Run `enforce_strategy_boundary.py` with identified clusters:

```python
from scripts.enforce_strategy_boundary import validate_boundary

try:
    result = validate_boundary(identified_clusters)
    # Proceed if valid
except StrategyBoundaryViolation as e:
    # Surface violation to user
    # Suggest splitting into separate engagements
```

If violation detected, explain:

```
"⚠️ STRATEGY BOUNDARY VIOLATION

I detected both strategy clusters (Discovery, Process Design) and 
implementation clusters (Integration, Development) in this block.

Per Cadre's methodology, these must be separate engagements:
- Strategy Engagement: Discovery + Process Design → recommendations
- Implementation Engagement: Separate SOW after strategy approved

This protects both project quality (implementation needs fresh discovery 
after strategy) and revenue (separate engagements).

Would you like me to create:
A) Strategy block only
B) Implementation block only (assuming strategy already complete)
C) Separate blocks for each"
```

### Step 7: Risk Checkpoint (Non-Blocking)

Surface 3-5 critical risks in plain English. Continue regardless of user response.

```
"⚠️ RISK CHECKPOINT (Optional - I'll continue regardless)

Based on what you've described, I see these potential issues:

1. **API Documentation Unknown**
   Client's legacy Salesforce instance might not have modern API docs.
   If missing, this could add 2-4 weeks for workarounds.
   Have we validated API exists and is documented?
   [Continue / Note as assumption / Client to confirm]

2. **Stakeholder Availability Assumption**
   Block assumes VP Sales available for weekly 1-hour check-ins.
   If unavailable, decisions could bottleneck.
   Has this time commitment been confirmed?
   [Confirm now / Identify backup / Reduce to biweekly]

3. **Data Quality Unknown**
   Assuming Salesforce data is clean enough for sync.
   If data is messy, could require cleanup phase first.
   Do we know data quality score?
   [Discovery sprint needed / Accept risk / Client provides sample]

Should I note these as assumptions and continue with block creation?"
```

See `references/risk-patterns.md` for common risks by cluster.

---

## Phase 2: Block Creation

### Step 1: Calculate Duration

Run `estimate_duration.py` with cluster complexity ratings:

```python
from scripts.estimate_duration import estimate_duration

duration = estimate_duration({
    'discovery': 'medium',
    'integration': 'complex',
    'testing': 'simple'
})

# Returns: {
#     'total_weeks': '11-22',
#     'total_months': '2.8-5.5',
#     'breakdown': {
#         'discovery': '2-4 weeks',
#         'integration': '8-16 weeks',
#         'testing': '1-2 weeks'
#     },
#     'confidence': 'medium'
# }
```

### Step 2: Calculate Confidence Score

Run `calculate_confidence.py`:

```python
from scripts.calculate_confidence import calculate_confidence

confidence = calculate_confidence(
    risk_count=len(identified_risks),
    assumption_count=len(assumptions),
    has_similar_past_work=check_past_work(),
    team_familiar_with_tech=check_team_familiarity(),
    client_relationship=determine_relationship(),
    dependencies_confirmed=check_dependencies()
)

# Returns score, level, interpretation, factors, recommendation
```

### Step 3: Structure Months

Distribute clusters across months based on duration and dependencies:

- If total < 4 weeks: Single month block
- If 4-12 weeks: 2-3 month structure
- If 12-24 weeks: 3-6 month structure
- If 24+ weeks: Consider splitting into multiple blocks

**Sequencing Logic**:
- Discovery always first (if present)
- Process Design before Implementation clusters
- Testing before Deployment
- Training/Enablement last (or alongside Deployment)
- Optimization in its own phase post-launch

### Step 4: Generate Internal Version

Use `assets/block-template-internal.md` as base. Include:

- Block overview with business value
- Activity clusters with complexity ratings
- Confidence score with basis
- Risk checkpoint (3-5 items)
- Assumptions documented
- Dependencies listed
- Month-by-month breakdown:
  - One-liner phase name
  - Outcome (what's achieved)
  - Activities (with technical notes)
  - Deliverables (with details)
  - Success indicators
  - Client time required
  - Cadre team allocation
  - Flexibility notes
  - Decision gate
  - Internal notes
- Handoff notes for resource-planner

### Step 5: Generate Client Version

Use `assets/block-template-client.md` as base. Transform internal version:

- Executive summary overview (business value)
- Timeline with high-level phases
- Month-by-month (client-friendly):
  - What You'll Get (outcome)
  - Key Activities (plain English)
  - Deliverables (business terms)
  - What We Need From You (time commitment)
  - Success Looks Like (measurable)
  - Decision Point (review checkpoint)
- Investment summary
- What Happens Next
- Flexibility Built In section

See `references/executive-communication.md` for language patterns.

### Step 6: Insert Decision Gates

For each month/phase transition, add appropriate decision gate from `references/decision-gates.md`:

- After Discovery: Requirements sign-off gate
- After Design: Technical approach approval gate
- Mid-Build: Progress demo gate
- After Testing: UAT sign-off gate
- Post-Deployment: Launch validation gate
- After Optimization: Handoff or Phase 2 gate

### Step 7: Validate Structure

Run `validate_block_structure.py` on both versions:

```python
from scripts.validate_block_structure import validate_block_structure

# Check internal version
internal_results = validate_block_structure(
    internal_block_text, 
    version='internal'
)

# Check client version
client_results = validate_block_structure(
    client_block_text,
    version='client'
)

# Fix any errors before presenting to user
```

### Step 8: Present to User

Show both versions with analysis:

```
## Internal Version
[Full internal block with risks, confidence, technical details]

## Client Version  
[Executive-friendly summary ready for SOW]

---

## Analysis

**Duration**: [X-Y] weeks ([X-Y] months)
**Confidence**: [Score]% ([Level])
**Complexity**: [Overall assessment]
**Risks Flagged**: [Count] items requiring attention

**Handoff Ready**: This block can be input into `project-resource-planner` 
to convert to ClickUp task structure with hour allocations and Gantt dependencies.

**Questions for Refinement**:
1. [Clarifying question about scope]
2. [Question about priority or approach]
3. [Question about constraints]
```

---

## Using the Scripts

### estimate_duration.py
Calculates duration ranges from cluster complexity:

```python
duration = estimate_duration({
    'discovery': 'simple',
    'integration': 'medium',
    'testing': 'simple',
    'training': 'simple'
})
```

Returns total weeks, months, breakdown per cluster, and confidence level.

### enforce_strategy_boundary.py
Validates no mixing of strategy and implementation:

```python
from scripts.enforce_strategy_boundary import validate_boundary

try:
    result = validate_boundary(['discovery', 'process_design', 'training'])
    # Returns: {'valid': True, 'block_type': 'strategy_only', ...}
except StrategyBoundaryViolation as e:
    # Handle violation - suggest splitting blocks
```

Raises exception if both strategy and implementation clusters present.

### calculate_confidence.py
Scores block confidence (internal only):

```python
confidence = calculate_confidence(
    risk_count=3,
    assumption_count=2,
    has_similar_past_work=True,
    team_familiar_with_tech=True,
    client_relationship='existing',
    dependencies_confirmed=True
)
```

Returns score (0-100), level, interpretation, factors, and recommendation.

### validate_block_structure.py
Ensures blocks have required sections:

```python
results = validate_block_structure(block_text, version='internal')

if not results['valid']:
    # Fix errors in results['errors']
    # Review warnings in results['warnings']
```

---

## Reference Materials

Load these as needed for detailed guidance:

### activity-clusters.md
Complete descriptions of all 10 activity clusters with:
- What each includes
- Complexity levels (Simple/Medium/Complex)
- Duration guidelines
- Risk patterns
- Common combinations

### complexity-rubric.md
Detailed criteria for rating each cluster Simple/Medium/Complex.
Use this during complexity assessment to make accurate estimates.

### risk-patterns.md
Common risks organized by activity cluster with:
- Risk description
- Impact assessment
- Mitigation strategies
- When to flag

### decision-gates.md
Standard checkpoint criteria for phase transitions with:
- Gate structure templates
- Go/no-go criteria
- Proceed options
- Example language

### executive-communication.md
Language patterns for client-facing blocks:
- Outcome-focused framing
- Flexibility language
- Handling unknowns
- Before/after examples

---

## Integration with Other Skills

### Upstream (Before Block Builder)
User typically has:
- Client conversations or notes
- Rough scope or requirements
- Budget/timeline constraints

### This Skill (Block Builder)
Creates:
- Internal block (detailed)
- Client block (executive summary)

### Downstream (After Block Builder)
Feed blocks into `project-resource-planner`:
- Converts months to week-by-week breakdown
- Assigns hour estimates to team members (AI Manager, AI Strategist, AI Engineer)
- Generates ClickUp import format
- Creates Gantt chart structure with dependencies

**Clean Handoff Format**:
Blocks already include:
✓ Activity breakdown (clusters)
✓ Timeline ranges (from duration estimation)
✓ Resource requirements (client time commitments)
✓ Decision gates (checkpoint timing)

---

## Common Pitfalls

### ❌ Don't assume project type
Ask "What are you building?" not "What type of project?"

### ❌ Don't skip search steps
Permission-based search builds context and prevents surprises

### ❌ Don't auto-generate implementation from strategy
Strategy → Implementation requires separate SOW, enforced by script

### ❌ Don't use technical language in client version
Transform to business outcomes using executive-communication.md patterns

### ❌ Don't skip risk checkpoint
Even if user doesn't respond, document assumptions for internal version

### ❌ Don't forget dual output
Always generate both internal and client versions together

### ❌ Don't mix up confidence and client-facing content
Confidence scores are internal only, never in client version

---

## Quality Checklist

Before considering a block complete:

✅ Both internal and client versions generated
✅ Strategy boundary validated (no mixing)
✅ Duration estimated from cluster complexity
✅ Confidence score calculated with basis
✅ 3-5 risks identified in plain English
✅ Assumptions documented
✅ Decision gates at each month/phase
✅ Client version uses plain English outcomes
✅ Flexibility language included
✅ Handoff notes for resource-planner present
✅ Structure validated with script

---

## Future Enhancements (Not Yet Built)

### Block Library (v2.0)
`assets/sample-blocks/` will house past blocks organized by:
- Cluster combinations
- Industry
- Duration

Skill will offer: "I found 3 similar blocks. Use [Block X] as template?"

### ClickUp Export (v2.0)
Direct integration to create ClickUp tasks from blocks (currently manual via resource-planner).

### Confidence Tracking (v3.0)
Compare predicted vs actual durations to improve estimation accuracy over time.
