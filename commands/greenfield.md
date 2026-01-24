---
tool: claude-code
description: Discover and specify a new software project from scratch
allowed-tools: Write, Read, Edit, Task, WebSearch, WebFetch
argument-hint: "[project idea or problem]"
---

# Greenfield Command

Transform a new idea into actionable specifications.

**Not for:** Adding features to existing projects (use `/plan` instead)

## Output

Creates in `docs/`:
- `SPEC.md` - What to build (requirements, users, success criteria)
- `DESIGN.md` - How to build it (architecture, tech choices)
- `PLAN.md` - Implementation roadmap

## Discovery Process

### Phase 1: Vision (2-3 questions)
- What problem are you solving?
- Who has this problem?
- What does success look like?

### Phase 2: Core Problem (2-3 questions)
- What's the ONE thing that must work?
- What's the smallest valuable solution?

### Phase 3: Users (2-3 questions)
- Who is the primary user?
- What triggers their need?

### Phase 4: Technical (2-3 questions)
- What can be simplified for MVP?
- What existing tools/frameworks fit?
- Any hard constraints?

### Phase 5: Validation (2-3 questions)
- How will you know it's working?
- What would make you pivot?

### Phase 6: Scoping

| Scope | Definition |
|-------|------------|
| **Core MVP** | ONE problem, ONE user type |
| **Expanded MVP** | Multiple features, single user |
| **Full Vision** | All features, all users |

## Workflow

```
1. User provides idea
2. Interactive discovery (phases 1-6)
3. Update docs after each phase
4. Review complete specs
5. Finalize to docs/
6. Suggest: /plan [first feature]
```

## Key Behaviors

**Ask, don't assume:**
- "Why?" and "Can you give an example?"
- "If you could only have one..."
- "What does X specifically mean?"

**Scope control:**
- Default to smallest viable scope
- Move "nice to haves" to Full Vision
- "Let's validate the core first"

**Progressive documentation:**
- Update SPEC.md as requirements emerge
- Update DESIGN.md as tech decisions made
- Update PLAN.md as scope crystallizes

## Completion

1. Present summary of all three docs
2. Highlight MVP vs full vision
3. Suggest first feature

**Next Steps:**
- `/plan [first MVP feature]` - Start implementation
- `/research [technical topic]` - Deep dive on unknowns
