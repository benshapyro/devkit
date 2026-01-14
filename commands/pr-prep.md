---
tool: claude-code
description: Prepare a pull request by analyzing changes and generating PR description
allowed-tools: Read, Grep, Glob, Bash(git:*), Task
argument-hint: [base-branch]
---

# PR Prep Command

Generate a comprehensive PR description and catch issues before creating the pull request.

**Workflow:** `/review` → `/validate` → `/pr-prep` → `gh pr create`

## Usage

```
/pr-prep [base-branch]
```

Default base branch is `main` or `master` (auto-detected).

## Process

### 1. Validate Ready State

!`git status --porcelain`

If uncommitted changes exist, warn the user:
> You have uncommitted changes. Consider committing or stashing before preparing your PR.

### 2. Detect Base Branch

If `$1` is provided, use it. Otherwise:

!`git branch -l main master | head -1 | tr -d ' *'`

### 3. Spawn PR Summarizer Agent

```
Task(
  subagent_type="pr-summarizer",
  description="Generate PR description",
  prompt="Analyze the current branch and generate a comprehensive PR summary.

Base branch: [detected or provided base]
Current branch: [from git branch --show-current]

Provide:
1. PR title (conventional commit format)
2. PR description with changes, technical details, breaking changes
3. Suggested commit messages
4. Changelog entry
5. List of key files changed with impact notes
6. Review guidance and risk assessment

Focus on high-value information for reviewers. Be thorough but concise."
)
```

### 4. Present Results

Display the agent's output, then offer actions:

```
## PR Ready

{Agent output here}

---

## Actions

**Copy to clipboard:**
The PR description is ready to paste into GitHub/GitLab.

**Create PR directly:**
```bash
gh pr create --title "feat(scope): description" --body "..."
```

**Push first (if needed):**
```bash
git push -u origin $(git branch --show-current)
```

---

**Next:** `/ship` to commit and push, or create PR directly with `gh pr create`
```

### 5. Check for Issues

Before finishing, check for common issues:

1. **Missing tests** - Did new code get test coverage?
2. **Large files** - Any files >500 lines added?
3. **Secrets** - Any potential secrets in the diff?
4. **Breaking changes** - Are they documented?

If issues found, list them:

```
## Pre-PR Checklist

- [ ] Missing tests for: src/new-feature.ts
- [ ] Consider splitting: src/large-file.ts (600 lines)
- [ ] Verify no secrets: check config.json changes
```

## Notes

- This command focuses on PR preparation, not creation
- Use `gh pr create` to actually create the PR
- The generated description follows conventional commit standards
- For quick PRs, you can skip this and use `gh pr create` directly
