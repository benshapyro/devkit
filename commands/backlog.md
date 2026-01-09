---
tool: claude-code
description: Document bugs and improvements to project backlog (interactive loop)
allowed-tools: Read, Grep, Glob, Task, Write, Edit
argument-hint: [bug|enh|ux] [brief description]
---

# Backlog Mode

Document bugs and improvements WITHOUT implementing them.

## Initial Setup

1. If `$ARGUMENTS` provided, use as first item
2. Locate BACKLOG.md: `docs/BACKLOG.md`, `BACKLOG.md`, or `docs/*/BACKLOG.md`
3. If not found, create `docs/BACKLOG.md`

## Workflow Loop

### Step 1: Receive
- Accept ONE item at a time
- If multiple provided: "Let's start with the first one."

### Step 2: Classify

| Type | Criteria |
|------|----------|
| **BUG** | Broken, error, unexpected behavior |
| **ENH** | New feature or capability |
| **UX** | Visual or usability improvement |

State: "This sounds like a **[TYPE]**."

### Step 3: Check Duplicates
Read BACKLOG.md, search for similar entries.

### Step 4: Investigate

Use **Explore subagent** to find relevant code:
```
Task(subagent_type="Explore", prompt="Find code related to [X]")
```

For complex issues, run multiple agents in parallel.

### Step 5: Analyze
- What code is affected?
- Root cause (BUG) or approach (ENH/UX)
- Suggested priority (P1/P2/P3)

### Step 6: Preview Entry
Show complete entry to user before adding.

### Step 7: Document
After user confirms, add to BACKLOG.md and update statistics.

### Step 8: Next Item
"Next item? (or 'done' to exit)"

## Priority Guidelines

| Priority | Use When |
|----------|----------|
| **P1** | Blocks core functionality, security risk |
| **P2** | Significant but has workaround |
| **P3** | Minor, cosmetic, nice-to-have |

## Entry Templates

### BUG-XXX
```markdown
### [BUG-XXX] Title
- **Reported**: YYYY-MM-DD
- **Status**: Open
- **Priority**: P1/P2/P3
- **Description**: What's broken
- **Steps to Reproduce**: 1. ... 2. ...
- **Expected**: What should happen
- **Actual**: What happens
- **Affected Files**: `path/to/file.ts:line`
- **Proposed Fix**: High-level approach
```

### ENH-XXX
```markdown
### [ENH-XXX] Title
- **Reported**: YYYY-MM-DD
- **Status**: Open
- **Priority**: P1/P2/P3
- **Description**: What to add
- **User Impact**: Who benefits
- **Scope**: Small/Medium/Large
- **Affected Files**: `path/to/file.ts`
```

### UX-XXX
```markdown
### [UX-XXX] Title
- **Reported**: YYYY-MM-DD
- **Status**: Open
- **Priority**: P1/P2/P3
- **Description**: UX issue
- **Current**: How it works now
- **Proposed**: How it should work
- **Affected Components**: `Component.tsx`
```

## Critical Rules

1. **NO IMPLEMENTATION** - Only analyze and document
2. **ALWAYS PREVIEW** - Never add without confirmation
3. **ONE AT A TIME** - Don't batch items
4. **INCREMENT IDs** - Check highest existing ID

## On Exit

```
Backlog session complete. Added X items:
- BUG-001: title
- ENH-002: title
```
