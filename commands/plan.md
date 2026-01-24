---
tool: claude-code
description: Start a new feature with proper planning
allowed-tools: Task, Read, Grep, Glob, Bash(git:*)
argument-hint: "[--tdd] [--quick] [feature description]"
---

# Plan Command

Plan a feature before implementation.

**For new projects:** Use `/greenfield` first, then `/plan` for each feature.

## Flags

- `--tdd` - Test-Driven Development mode (write tests first)
- `--quick` - Skip detailed templates, just outline approach

## Validation

If no feature description provided, ask for one.

## Planning Steps

### 1. Gather Context (REQUIRED)

**You MUST read relevant files before planning.** Don't plan based on assumptions.

- Read relevant CLAUDE.md files
- Read files that will be modified
- Identify existing patterns and conventions

Use `Explore` agent or direct reads to understand current implementation.

### 2. Requirements Clarification

Ask if needed:
- Expected behavior?
- Edge cases?
- Performance requirements?

### 3. Create Plan

**Detail level by change type:**

| Change | Detail |
|--------|--------|
| Complex/risky | Line numbers + snippets |
| Medium | Function names |
| Simple | File paths |
| New files | Structure outline |

**Plan structure:**

```
## Feature: [description]

### Requirements
- [ ] Requirement 1
- [ ] Requirement 2

### Approach
1. [Step] - Why: [reasoning]
2. [Step]

### Files to Change

**`path/to/file.ts`** (lines X-Y)
- Current: [state]
- Change: [what]

**`path/to/new.ts`** (NEW)
- Purpose: [why]
- Contains: functionA(), functionB()

### Testing
- Unit: [cases]
- Integration: [approach]

### Risks
- [Risk] → [Mitigation]
```

### 4. TDD Mode (if --tdd)

Add to plan:

```
### TDD Order

1. Write failing tests:
   - `__tests__/feature.test.ts`

2. Implement to pass tests

3. Refactor (keep tests green)
```

### 5. Confidence Check

Before proceeding, verify:
- Requirements clear? (≥0.9 confidence)
- Technical approach sound?
- Dependencies identified?

If confidence <0.7, ask clarifying questions first.

### 6. Await Approval

Present plan. Wait for user approval before implementing.

## Quick Mode (--quick)

Skip templates. Just provide:
1. Brief approach (2-3 sentences)
2. Files to change (list)
3. Key risks (if any)

## Next Steps

After approval:
- `--tdd`: Write tests first
- Standard: Implement
- Then: `/slop` → `/review` → `/validate` → `/ship`
