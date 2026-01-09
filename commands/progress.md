---
tool: claude-code
description: Save research findings as reusable knowledge documents
allowed-tools: Write, Read, Glob, Bash
argument-hint: [topic name]
---

# Progress Command

Save learned knowledge as reusable documents for future sessions.

## When to Use

- After `/research` with valuable findings
- After exploring complex codebase area
- When learning something useful for future sessions

## File Naming

**Format:** `YYYY-MM-DD-NNN-description.md`

- `YYYY-MM-DD` - Today's date
- `NNN` - Sequential number (001, 002, etc.)
- `description` - Kebab-case topic

**To find next number:**
```bash
ls docs/ | grep "^$(date +%Y-%m-%d)" | wc -l
```

## Workflow

### 1. Identify Learnings

If no topic provided, scan conversation for:
- Files and entry points discovered
- Patterns and conventions
- Gotchas and edge cases
- External doc links

### 2. Propose Document

```
## Proposed Knowledge Document

**Topic:** [auto-detected or provided]
**File:** `docs/YYYY-MM-DD-NNN-description.md`

### Preview

# [Topic] - Quick Reference

**Date:** YYYY-MM-DD
**Context:** [What prompted this]

## Key Files
| File | Purpose |
|------|---------|
| `path/to/file.ts:line` | [What it does] |

## Entry Points
- **[Task 1]:** Start at `file.ts:function()`

## Patterns
- [Pattern 1]

## Gotchas
- [Edge case to watch]

---
Save? (yes / edit / cancel)
```

### 3. Await Approval

- **yes** - Create file
- **edit** - User provides changes
- **cancel** - Don't save

### 4. Save

1. Create `docs/` if needed
2. Determine correct sequence number
3. Write file
4. Confirm location

## Template

```markdown
# [Topic] - Quick Reference

**Date:** YYYY-MM-DD
**Context:** [What prompted this research]

## Overview
[1-2 sentence summary]

## Key Files
| File | Purpose |
|------|---------|
| `path/file.ts:line` | [Description] |

## Entry Points
**[Task]:** `file.ts:functionName()`

## Patterns
### [Pattern Name]
[Description]

## Gotchas
- **[Issue]:** [What to watch out for]

## Resources
- [Link](url) - [What it covers]
```

## Notes

- Keep concise (1-2 pages max)
- Focus on "what you wish you knew when starting"
- Include file:line references
- Create NEW files (don't overwrite)
