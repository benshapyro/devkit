---
tool: claude-code
description: Commit and ship validated changes
allowed-tools: Bash(git:*), Read, Glob
argument-hint: [--force] [optional commit message]
---

# Ship Command

Commit validated changes with proper formatting.

## Flags

- `--force` - Skip validation check (use when you know what you're doing)

## Pre-Ship Checks

### 1. Branch Safety

!`git branch --show-current`

**If on main/master:** Warn user and require explicit confirmation to continue.

### 2. Validation Status (unless --force)

Check if `/validate` was run recently by looking for validation artifacts or asking user.

If unclear, suggest: "Run `/validate` first, or use `/ship --force` to skip."

### 3. Git Status

!`git status --short`

If no changes, inform user and stop.

## Gather Information

**Staged changes:**
!`git diff --staged --stat`

**Unstaged changes:**
!`git diff --stat`

**Recent commits for style:**
!`git log --oneline -5`

## Generate Commit

### Analyze Changes

Based on the diff, determine:
- **Type**: feat, fix, docs, style, refactor, test, chore
- **Scope**: Component or module affected (optional)
- **Subject**: What the commit does (imperative mood)

### Commit Format

```
type(scope): subject

Body explaining why this change was made.
- Detail 1
- Detail 2
```

**Note:** Follow the project's existing commit style. Check recent commits for conventions (Co-authored-by, emoji, etc.).

### If Argument Provided

Use `$1` as the commit message subject (unless it's `--force`).

## Execute Commit

### Stage Changes

If there are unstaged changes:
- Show what will be staged
- Ask user before staging untracked files

### Create Commit

```bash
git commit -m "$(cat <<'EOF'
[generated message]
EOF
)"
```

### Verify Success

!`git log -1 --oneline`

## Report

```
## Ship Complete

**Commit:** [hash]
**Message:** [subject]
**Files changed:** [count]

### Next Steps
- Push to remote: `git push`
- Create PR: `gh pr create`
```

## Safety Rules

- Never force push
- Never push to main/master without explicit approval
- Always verify commit authorship before amend
- Report any pre-commit hook failures clearly
- If commit fails, explain why and suggest fixes
