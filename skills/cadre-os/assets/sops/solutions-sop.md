# Solutions Build Process SOP

Standard operating procedure for discovering, prioritizing, and delivering AI solutions (assistants + prompts).

## When to Use This Process

Use the Solutions workflow when:
- Client engagement includes AI assistant or prompt builds
- Discovery has revealed automation opportunities
- Client asks "what should we build?"
- You need to scope and prioritize solution opportunities
- You need to create a client-facing build plan

## Process Overview

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  DISCOVER   │───▶│  PRIORITIZE │───▶│  VALIDATE   │
│             │    │             │    │             │
│ • Scan docs │    │ • Score     │    │ • Check     │
│ • Query     │    │ • Rank      │    │   blockers  │
│   Catalog   │    │ • Classify  │    │ • Flag      │
│ • Browse    │    │ • Matrix    │    │   issues    │
│   Library   │    │             │    │             │
└─────────────┘    └─────────────┘    └─────────────┘
       │                                     │
       │                                     ▼
       │               ┌─────────────┐    ┌─────────────┐
       │               │   CATALOG   │◀───│  ESTIMATE   │
       │               │             │    │             │
       │               │ • Client    │    │ • Calculate │
       │               │   artifact  │    │   hours     │
       │               │ • Branded   │    │ • Calculate │
       │               │   HTML      │    │   cost      │
       │               └─────────────┘    └─────────────┘
       │                      │                  │
       │                      │                  ▼
       │                      │           ┌─────────────┐
       └──────────────────────┴──────────▶│    SPEC     │
                                          │             │
                                          │ • Light     │
                                          │ • Full      │
                                          │ • Formal    │
                                          └─────────────┘
```

## Step-by-Step Process

### Step 1: Discover Opportunities

**Command:** `/solutions discover [client]`

**What happens:**
1. Claude scans all project documents (transcripts, notes, analysis)
2. Claude queries Discovery Catalog for high-priority challenges and existing solution ideas
3. Claude matches findings against assistant patterns (50) and prompt patterns (45+)
4. Output: List of assistant and prompt opportunities with evidence

**Alternative entry:** `/solutions assistants library` or `/solutions prompts patterns` to browse patterns directly

**Duration:** 10-20 minutes

### Step 2: Prioritize Opportunities

**Command:** `/solutions assistants prioritize [client]`

**What happens:**
1. Claude scores each opportunity on 5 dimensions (Impact, Effort, Risk, Reuse, Strategic)
2. Calculates Priority Score and V/E Ratio
3. Classifies as Quick Win, Strategic Bet, Foundation Builder, Research, or Defer
4. Generates 2×2 matrix visualization

**Duration:** 10-15 minutes

### Step 3: Validate Selected Opportunities

**Command:** `/solutions assistants validate [use case]`

**What happens:**
1. Claude asks blocker questions for each selected opportunity
2. Checks: Integration availability, credentials, knowledge base, data freshness, dependencies
3. Flags issues and concerns

**Duration:** 5-10 minutes per opportunity

### Step 4: Estimate Build Time/Cost

**Command:** `/solutions assistants estimate [use case]`

**What happens:**
1. Claude breaks down build into components
2. Calculates total hours and cost
3. Compares to Library benchmarks if available

**Duration:** 5 minutes per opportunity

**Note:** Hours and cost are internal only—not shown in client catalog.

### Step 5: Generate Client Catalog

**Command:** `/solutions catalog [client]`

**What happens:**
1. Claude generates branded HTML artifact
2. Includes all prioritized assistants and prompts
3. Two tabs: Assistants, Prompts

**Duration:** 5-10 minutes

### Step 6: Generate Specs (As Needed)

**Command:** `/solutions assistants spec [use case] [light|full|formal]`

| Type | Duration | Use When |
|------|----------|----------|
| Light | 5-10 min | Quick review, internal alignment |
| Full | 20-30 min | Ready to build, handoff to builder |
| Formal | 30-45 min | Client approval, SOW attachment |

## Client Handoff Checklist

Before sharing Solution Catalog with client:

- [ ] All assistants have clear, jargon-free descriptions
- [ ] All prompts have clear purpose statements
- [ ] Status badges are accurate (Not Selected/Backlog/In Progress/Testing/Live)
- [ ] Impact levels assigned (High/Medium/Low)
- [ ] Sample prompts are specific and realistic
- [ ] Prompt text is complete and tested
- [ ] Launch links work (for Live assistants)
- [ ] Client name is correct
- [ ] Reviewed for typos

## Updating the Solution Catalog

The catalog is a static HTML snapshot. To update:

1. Make changes to source data (opportunities, status, prompts)
2. Run `/assistants portal [client]` again
3. Replace old artifact with new one

**Future state:** Status can be stored in Discovery Catalog Solutions table.

## Integration with Discovery Catalog

### Reading from Catalog

The `/assistants discover` command queries:
- **5_Challenges:** High-priority challenges suggest assistant opportunities
- **6_Solutions:** Existing solution ideas that may be assistant candidates
- **4_Technology:** Current tools that inform integration requirements

### Writing to Catalog (Optional)

After prioritization, Claude will ask:
> "Would you like me to add these opportunities to the Discovery Catalog as Solutions?"

If yes, creates Solution records with:
- Solution Name: [Assistant name]
- Solution Type: AI Assistant
- Status: Proposed
- Notes: Summary from spec

## Common Scenarios

### Scenario 1: New Engagement, No Discovery Yet

1. Use `/assistants library` to browse patterns
2. Show client the library to spark ideas
3. Run discovery after initial sessions

### Scenario 2: Discovery Complete, Ready to Scope Assistants

1. Run `/assistants discover [client]`
2. Run `/assistants prioritize [client]`
3. Validate top candidates
4. Generate portal for client review
5. Generate specs for approved builds

### Scenario 3: Client Knows What They Want

1. Skip discover/prioritize
2. Run `/assistants estimate [use case]` for each
3. Run `/assistants spec [use case] full` for approved ones
4. Generate portal showing just those assistants

### Scenario 4: Quick Portal for Sales/Proposal

1. Browse library, select relevant patterns
2. Skip full scoring—assign phases manually
3. Generate portal showing potential builds
4. Use as proposal attachment

## Troubleshooting

| Issue | Solution |
|-------|----------|
| No Library matches found | Use category averages; flag as novel |
| Client disputes priority | Re-score with their input; adjust weights |
| Blocker identified | Document in portal; mark status accordingly |
| Portal looks wrong | Regenerate; check for special characters in text |
| Estimates seem off | Compare to Library benchmarks; adjust components |

## Related Commands

| Command | When to Use |
|---------|-------------|
| `/context [client]` | Pull client background before discovery |
| `/gaps [client]` | Identify coverage gaps that suggest opportunities |
| `/roadmap [client]` | Create implementation roadmap including assistants |
| `/deck [client]` | Include assistant plan in strategy deck |
