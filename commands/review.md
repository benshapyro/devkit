---
tool: claude-code
description: Review code changes for quality and best practices
allowed-tools: Read, Grep, Glob, Bash(git:*), Task
---

# Review Command

Qualitative code review for quality, style, security, and best practices.

**Workflow:** `/slop` (optional) → `/review` → `/validate` → `/ship`

## Process

### 1. Gather Changes

!`git diff --name-only`
!`git diff --staged --name-only`

If no changes found, inform the user and stop.

Get the full diff for review:
!`git diff`
!`git diff --staged`

### 2. Perform Review

**Option A: Use code-reviewer agent (if available)**

```
Task(
  subagent_type="code-reviewer",
  prompt="Review these code changes for quality, security, and best practices.

Files changed: [list from step 1]

Review focus:
- Code quality and maintainability (DRY, KISS, YAGNI)
- Security vulnerabilities (OWASP checklist)
- Style consistency with existing code
- Error handling patterns
- Test coverage for new/changed code

Provide:
- Overall assessment (APPROVE / REQUEST CHANGES)
- Positive findings
- Required changes (file:line references)
- Suggestions
- Security concerns"
)
```

**Option B: Direct review (if agent unavailable or for quick reviews)**

Review the changes directly, checking:

1. **Code Quality**
   - Is the code readable and self-documenting?
   - Are there any obvious bugs or logic errors?
   - Does it follow existing patterns in the codebase?

2. **Security**
   - Input validation on user data?
   - SQL injection, XSS, or other OWASP risks?
   - Secrets or credentials exposed?

3. **Style**
   - Matches existing code conventions?
   - Consistent naming, formatting?

4. **Testing**
   - Are new code paths tested?
   - Edge cases covered?

### 3. Present Results

```
## Code Review Summary

**Assessment:** APPROVE / REQUEST CHANGES

### Positive Findings
- [What's good about these changes]

### Required Changes
- `file.ts:42` - [Issue and fix]

### Suggestions
- `file.ts:67` - [Optional improvement]

### Security
- [Any concerns or "None identified"]
```

## Next Steps

- **APPROVED:** Run `/validate` then `/ship`
- **CHANGES REQUESTED:** Fix issues and re-run `/review`
