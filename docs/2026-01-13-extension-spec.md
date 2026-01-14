# Devkit Extension Specification

**Date:** 2026-01-13
**Status:** Approved
**Version:** 2.0

This specification defines the design decisions and implementation details for the devkit extension project, based on comprehensive stakeholder interview.

---

## Final Selection Summary

### Commands (4)
| Command | Purpose |
|---------|---------|
| `/trace` | Gather production error context for debugging |
| `/pr-prep` | Generate PR description (uses `pr-summarizer` agent internally) |
| `/regression-scan` | Show blast radius before committing changes |
| `/deploy-check` | Pre-deployment safety checklist |

### Hooks (2)
| Hook | Event | Purpose |
|------|-------|---------|
| `test-coverage-enforcer` | PostToolUse | Warn when new/changed code lacks tests |
| `smart-context-loader` | UserPromptSubmit | Auto-inject relevant project context |

### Skills (5)
| Skill | Purpose |
|-------|---------|
| `security-guardian` | OWASP patterns, auth, API security |
| `database-migration` | Zero-downtime migration patterns |
| `observability-engineering` | OpenTelemetry, logging, tracing |
| `sre-runbook-generator` | Generate runbooks from service metadata |
| `web-accessibility-auditor` | WCAG 2.2, ARIA, manual testing guides |

### Agents (4)
| Agent | Purpose |
|-------|---------|
| `security-auditor` | Scan codebase for vulnerabilities (read-only) |
| `pr-summarizer` | Generate PR descriptions, changelogs |
| `test-coverage-analyzer` | Identify test gaps, suggest test cases |
| `migration-planner` | Plan framework upgrades, detect breaking changes |

---

## Part 1: Decision Log

All architectural and design decisions captured during requirements gathering.

### 1.1 Core Architecture

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Extension architecture** | Layered (core library + thin wrappers) | Balance DRY with maintainability. Shared primitives (git, AST, coverage) with independent extension logic. |
| **Core language** | Python | Consistency with existing hooks. Rich ecosystem for git, AST parsing, coverage APIs. |
| **Configuration scope** | Global only (~/.claude/settings.json) | Simplicity. Avoid mental overhead of project-level overrides for v1. |
| **Versioning strategy** | Bundle versioning | All extensions share devkit version. Simpler mental model, coordinated releases. |
| **CI/CD support** | CI-aware mode | Detect CI env vars, adjust output (no spinners, proper exit codes). Same tools work everywhere. |

### 1.2 User Experience

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Performance budget** | Moderate (<2s) | Allow up to 2 seconds for checks. Noticeable but acceptable pause. |
| **Progress feedback** | Spinner with label | Show "Analyzing coverage..." while running. User knows something is happening. |
| **Warning tone** | Severity-colored | 🔴 CRITICAL / 🟡 MEDIUM / 🟢 INFO. Visual hierarchy guides attention. |
| **Report format** | Plain markdown | Universal, readable in terminal, easy to copy/paste. |
| **Discovery mechanism** | First-run prompt | On first relevant action, suggest the extension. Contextual learning. |
| **Failure handling** | Retry then warn | Retry once with backoff, then warn if still failing. Handles transient issues gracefully. |

### 1.3 Extension-Specific Decisions

| Extension | Decision | Choice |
|-----------|----------|--------|
| **pr-summarizer** | Inference level | Maximum inference. Analyze commits, generate full PR autonomously. |
| **pr-summarizer** | Large diff handling | Focus on key files. Identify high-impact files (APIs, schemas, tests), detail those, list others. |
| **security-guardian** | Skill structure | Topic-based references. SKILL.md as router, separate refs for auth, API security, OWASP. |
| **database-migration** | Primary focus | Zero-downtime patterns. Expand-contract, rolling migrations. |
| **sre-runbook-generator** | Input source | Service metadata. Parse docker-compose, k8s manifests, package.json to infer topology. |
| **web-accessibility-auditor** | Scope | Manual testing guides. Keyboard nav, screen reader testing. Automated tools miss the hard stuff. |
| **test-coverage-enforcer** | Threshold approach | Delta coverage only. New/changed code must have coverage, ignore existing gaps. |
| **security-auditor agent** | Permissions | Read-only. Can Read, Grep, Bash (scanners). Reports findings but never modifies code. |

### 1.4 Build Priority

| Priority | Extension | Effort | Rationale |
|----------|-----------|--------|-----------|
| **1** | `pr-summarizer` agent | 2-4 hours | Quickest win, immediate daily value |
| **2** | `/pr-prep` command | 1-2 hours | Thin wrapper around pr-summarizer |
| **3** | `test-coverage-enforcer` hook | 4-6 hours | Quality gate for AI-generated code |
| **4** | `security-guardian` skill | 3-5 days | Foundational security knowledge |
| **5** | `/trace` command | 4-8 hours | High-value debugging assistant |

---

## Part 2: Implementation Specifications

### 2.1 Shared Core Library

**Location:** `devkit/lib/core/`

```
lib/core/
├── __init__.py
├── git.py          # Git operations (diff, blame, log, status)
├── ast_utils.py    # Language-agnostic AST helpers
├── coverage.py     # Coverage report parsing (Jest, Pytest)
├── output.py       # Markdown formatting, spinners, colors
└── config.py       # Settings loading, CI detection
```

#### Core Utilities API

```python
# git.py
def get_diff(base: str = "HEAD") -> list[FileDiff]: ...
def get_blame(file: str, line: int) -> BlameInfo: ...
def get_recent_commits(count: int = 10) -> list[Commit]: ...
def get_changed_files() -> list[str]: ...
def get_file_history(file: str, count: int = 5) -> list[Commit]: ...

# coverage.py
def parse_jest_coverage(json_path: str) -> CoverageReport: ...
def parse_pytest_coverage(json_path: str) -> CoverageReport: ...
def get_uncovered_lines(report: CoverageReport, file: str) -> list[int]: ...
def calculate_delta_coverage(base: CoverageReport, current: CoverageReport) -> float: ...

# output.py
def spinner(message: str) -> ContextManager: ...
def severity_badge(level: str) -> str: ...  # Returns emoji + colored text
def markdown_table(headers: list, rows: list) -> str: ...
def is_ci() -> bool: ...  # Detect CI environment
```

---

### 2.2 Command: `/trace`

**Location:** `devkit/commands/trace.md`

**Purpose:** Gather complete diagnostic context from production errors for faster debugging.

```markdown
---
name: trace
description: >
  Gather production error context for debugging. Accepts stack traces,
  error messages, or error tracking URLs. Returns diagnostic report with
  source code, git history, and similar past errors.
---

# /trace

Debug production errors by gathering complete context automatically.

## Usage

```
/trace <error-input>
```

Where `<error-input>` is:
- A pasted stack trace
- An error message
- A Sentry/Bugsnag URL

## Process

1. **Parse error input**
   - Extract file paths and line numbers from stack trace
   - Identify error type and message

2. **Gather context**
   - Read source code at error locations (±10 lines)
   - Run `git blame` on affected lines
   - Find recent commits touching those files
   - Search for similar error patterns in codebase

3. **Generate diagnostic report**
   ```markdown
   ## Error Diagnostic Report

   ### Error Summary
   {error type}: {message}
   Location: {file}:{line}

   ### Source Context
   ```{language}
   {code with error line highlighted}
   ```

   ### Recent Changes
   - {commit hash} {date}: {message} by {author}

   ### Root Cause Hypothesis
   {AI analysis of likely cause}

   ### Similar Past Issues
   - {link to similar error in git history}

   ### Suggested Investigation
   1. {step}
   2. {step}
   ```

## Example

```
/trace TypeError: Cannot read property 'user' of undefined
    at AuthController.getProfile (src/auth/controller.ts:45)
    at Router.handle (node_modules/express/router.js:123)
```
```

---

### 2.3 Command: `/pr-prep`

**Location:** `devkit/commands/pr-prep.md`

**Purpose:** Prepare a pull request by generating description, catching issues, and providing review guidance. Internally spawns `pr-summarizer` agent.

```markdown
---
name: pr-prep
description: >
  Prepare a pull request by analyzing changes and generating a comprehensive
  PR description. Spawns pr-summarizer agent to do the analysis.
---

# /pr-prep

Generate a PR description and catch issues before creating the pull request.

## Usage

```
/pr-prep [base-branch]
```

Default base branch is `main` or `master`.

## Process

1. Spawn `pr-summarizer` agent to analyze changes
2. Present generated PR description
3. Highlight any concerns (missing tests, large files, potential breaking changes)
4. Offer to copy to clipboard or create PR directly

## Output

The agent returns:
- PR title (conventional commit format)
- PR description with changes, technical details, breaking changes
- Suggested commit messages
- Changelog entry
- List of files changed with impact notes

## Integration with /ship

After `/pr-prep`, you can run `/ship` to commit and push, or create the PR directly:

```
/pr-prep
# Review output
gh pr create --title "..." --body "..."
```
```

---

### 2.4 Command: `/regression-scan`

**Location:** `devkit/commands/regression-scan.md`

**Purpose:** Identify the blast radius of changes before committing.

```markdown
---
name: regression-scan
description: >
  Analyze code changes to identify all files, functions, and tests
  that might be affected. Shows blast radius before committing.
---

# /regression-scan

Understand the impact of your changes before committing.

## Usage

```
/regression-scan [files...]
```

If no files specified, analyzes current git diff.

## Process

1. **Identify changed code**
   - Parse git diff for modified functions/classes
   - Detect API signature changes

2. **Build dependency graph**
   - Find all files that import changed modules
   - Identify callers of changed functions
   - Detect database schema impacts

3. **Find affected tests**
   - Direct test files for changed code
   - Integration tests that might be affected
   - E2E tests covering affected flows

4. **Generate impact report**
   ```markdown
   ## Blast Radius Analysis

   ### Direct Changes
   - src/auth/controller.ts: `getProfile()` signature changed

   ### Affected Files (12)
   - src/api/users.ts (imports auth/controller)
   - src/middleware/auth.ts (calls getProfile)
   ...

   ### Tests to Run
   Priority 1 (directly affected):
   - tests/auth/controller.test.ts

   Priority 2 (integration):
   - tests/api/users.test.ts

   ### Breaking Change Risk
   🟡 MEDIUM: Function signature changed, 3 callers need update

   ### Suggested Reviewers
   - @alice (owns src/auth/)
   - @bob (last touched src/api/users.ts)
   ```

## Example

```
/regression-scan src/auth/controller.ts
```
```

---

### 2.5 Command: `/deploy-check`

**Location:** `devkit/commands/deploy-check.md`

**Purpose:** Pre-deployment safety checklist.

```markdown
---
name: deploy-check
description: >
  Run pre-deployment safety checks including tests, migrations,
  environment variables, and monitoring configuration.
---

# /deploy-check

Verify deployment readiness with a senior engineer's checklist.

## Usage

```
/deploy-check [environment]
```

Default environment is `production`.

## Checks Performed

1. **Code Quality**
   - [ ] All tests passing
   - [ ] Type checking passes
   - [ ] Linting passes
   - [ ] No console.log/print statements

2. **Database**
   - [ ] Pending migrations identified
   - [ ] Rollback scripts exist
   - [ ] No destructive migrations without confirmation

3. **Environment**
   - [ ] Required env vars documented
   - [ ] No hardcoded secrets
   - [ ] Feature flags configured

4. **Monitoring**
   - [ ] Error tracking configured (Sentry, etc.)
   - [ ] Key metrics have alerts
   - [ ] Runbook exists for critical paths

5. **Deployment**
   - [ ] Branch is up to date with main
   - [ ] No merge conflicts
   - [ ] CI pipeline passed

## Output

```markdown
## Deployment Readiness: production

### ✅ Passed (8)
- Tests: 142 passed, 0 failed
- Types: No errors
- Lint: Clean
...

### ⚠️ Warnings (2)
- Missing runbook for payment processing
- 3 TODO comments in changed files

### ❌ Blockers (1)
- Pending migration: 20240113_add_user_role.sql

### Recommendation
Fix blockers before deploying. Consider creating runbook for payment flow.
```
```

---

### 2.6 Hook: `test-coverage-enforcer`

**Location:** `devkit/hooks/test-coverage-enforcer.md`

**Purpose:** Warn when new or changed code lacks test coverage.

```markdown
---
name: test-coverage-enforcer
description: Warns when new/changed code lacks test coverage
event: PostToolUse
matcher: Edit|Write
---
```

#### Implementation

```python
#!/usr/bin/env python3
"""
Test coverage enforcer hook.
Checks if new/changed code has corresponding tests.
Uses delta coverage - only checks new code, ignores legacy gaps.
"""

import sys
import json
import subprocess
from pathlib import Path

# Import from core library
from lib.core.coverage import parse_jest_coverage, parse_pytest_coverage
from lib.core.output import severity_badge, spinner, is_ci

# File patterns
SOURCE_PATTERNS = {
    ".py": ("tests/test_{name}.py", "tests/{name}_test.py", "{dir}/test_{name}.py"),
    ".ts": ("__tests__/{name}.test.ts", "{name}.test.ts", "{name}.spec.ts"),
    ".tsx": ("__tests__/{name}.test.tsx", "{name}.test.tsx", "{name}.spec.tsx"),
    ".js": ("__tests__/{name}.test.js", "{name}.test.js", "{name}.spec.js"),
}

def find_test_file(source_file: str) -> str | None:
    """Find corresponding test file for a source file."""
    path = Path(source_file)
    ext = path.suffix
    name = path.stem
    dir_path = path.parent

    if ext not in SOURCE_PATTERNS:
        return None

    for pattern in SOURCE_PATTERNS[ext]:
        test_path = pattern.format(name=name, dir=dir_path)
        if Path(test_path).exists():
            return test_path

    return None

def check_coverage_delta(source_file: str) -> dict:
    """Check if new lines in source file have coverage."""
    # This is a simplified version - full implementation would:
    # 1. Run tests with coverage for just this file
    # 2. Parse coverage report
    # 3. Check which new lines are uncovered

    test_file = find_test_file(source_file)

    if test_file is None:
        return {
            "status": "missing",
            "message": f"No test file found for {source_file}",
            "suggestion": f"Create test file at {SOURCE_PATTERNS.get(Path(source_file).suffix, ['tests/'])[0]}"
        }

    return {
        "status": "exists",
        "test_file": test_file,
        "message": f"Test file exists: {test_file}"
    }

def main():
    hook_input = json.loads(sys.stdin.read())
    tool_name = hook_input.get("tool_name")
    tool_input = hook_input.get("tool_input", {})

    # Only check source file modifications
    if tool_name not in ("Edit", "Write"):
        sys.exit(0)

    file_path = tool_input.get("file_path", "")

    # Skip test files themselves
    if "test" in file_path.lower() or "spec" in file_path.lower():
        sys.exit(0)

    # Skip non-source files
    ext = Path(file_path).suffix
    if ext not in SOURCE_PATTERNS:
        sys.exit(0)

    result = check_coverage_delta(file_path)

    if result["status"] == "missing":
        print(json.dumps({
            "warning": f"{severity_badge('medium')} {result['message']}\n\nSuggestion: {result['suggestion']}"
        }))
        sys.exit(1)  # Warn but don't block

    sys.exit(0)

if __name__ == "__main__":
    main()
```

---

### 2.7 Hook: `smart-context-loader`

**Location:** `devkit/hooks/smart-context-loader.md`

**Purpose:** Auto-inject relevant project context into prompts.

```markdown
---
name: smart-context-loader
description: Automatically inject relevant project context based on prompt analysis
event: UserPromptSubmit
---
```

#### Implementation

```python
#!/usr/bin/env python3
"""
Smart context loader hook.
Analyzes user prompts and injects relevant project context.
"""

import sys
import json
import subprocess
from pathlib import Path

# Keywords that trigger context loading
KEYWORD_MAPPINGS = {
    "auth": ["src/auth/", "auth", "login", "session"],
    "api": ["src/api/", "routes/", "controllers/"],
    "database": ["migrations/", "models/", "schema"],
    "test": ["tests/", "__tests__/", "*.test.*"],
    "config": [".env.example", "config/", "settings"],
}

def extract_keywords(prompt: str) -> list[str]:
    """Extract relevant keywords from prompt."""
    prompt_lower = prompt.lower()
    found = []

    for category, _ in KEYWORD_MAPPINGS.items():
        if category in prompt_lower:
            found.append(category)

    return found

def find_relevant_files(keywords: list[str], limit: int = 5) -> list[str]:
    """Find files relevant to the keywords."""
    relevant = []

    for keyword in keywords:
        patterns = KEYWORD_MAPPINGS.get(keyword, [])
        for pattern in patterns:
            # Use git ls-files to find matching files
            try:
                result = subprocess.run(
                    ["git", "ls-files", f"*{pattern}*"],
                    capture_output=True, text=True, timeout=2
                )
                files = result.stdout.strip().split("\n")
                relevant.extend(f for f in files if f)
            except:
                pass

    return list(set(relevant))[:limit]

def get_recent_changes(keywords: list[str]) -> list[str]:
    """Get recent git commits related to keywords."""
    changes = []

    for keyword in keywords:
        try:
            result = subprocess.run(
                ["git", "log", "--oneline", "-5", f"--grep={keyword}"],
                capture_output=True, text=True, timeout=2
            )
            commits = result.stdout.strip().split("\n")
            changes.extend(c for c in commits if c)
        except:
            pass

    return changes[:5]

def get_todos(keywords: list[str]) -> list[str]:
    """Find TODO comments related to keywords."""
    todos = []

    for keyword in keywords:
        patterns = KEYWORD_MAPPINGS.get(keyword, [])
        for pattern in patterns:
            try:
                result = subprocess.run(
                    ["grep", "-r", "-n", "TODO", "--include", f"*{pattern}*"],
                    capture_output=True, text=True, timeout=2
                )
                matches = result.stdout.strip().split("\n")
                todos.extend(m for m in matches if m)
            except:
                pass

    return todos[:5]

def main():
    hook_input = json.loads(sys.stdin.read())
    prompt = hook_input.get("prompt", "")

    keywords = extract_keywords(prompt)

    if not keywords:
        sys.exit(0)

    # Gather context
    relevant_files = find_relevant_files(keywords)
    recent_changes = get_recent_changes(keywords)
    todos = get_todos(keywords)

    if not any([relevant_files, recent_changes, todos]):
        sys.exit(0)

    # Build context injection
    context_parts = ["[Auto-loaded context]"]

    if relevant_files:
        context_parts.append(f"\nRelevant files: {', '.join(relevant_files)}")

    if recent_changes:
        context_parts.append(f"\nRecent changes:\n" + "\n".join(f"  - {c}" for c in recent_changes))

    if todos:
        context_parts.append(f"\nTODOs found:\n" + "\n".join(f"  - {t}" for t in todos))

    # Return modified prompt with context
    modified_prompt = "\n".join(context_parts) + "\n\n" + prompt

    print(json.dumps({
        "prompt": modified_prompt
    }))
    sys.exit(3)  # Exit code 3 = modify input

if __name__ == "__main__":
    main()
```

---

### 2.8 Agent: `pr-summarizer`

**Location:** `devkit/agents/pr-summarizer.md`

**Purpose:** Generate comprehensive PR descriptions, commit messages, and changelog entries.

```yaml
---
name: pr-summarizer
description: >
  Generates comprehensive PR descriptions, conventional commit messages,
  and changelog entries by analyzing git diffs. Use when creating PRs
  or preparing code for review. Called by /pr-prep command.
tools:
  - Read
  - Grep
  - Bash  # Restricted to git commands
model: sonnet  # Fast, good at summarization
---
```

#### Output Template

```markdown
## PR Summary

### Title
{type}({scope}): {short description}

### Description
{1-3 sentence summary of what changed and why}

**Changes:**
- {bullet list of key changes}

**Technical Details:**
- {implementation notes for reviewers}

**Breaking Changes:**
{None or list of breaking changes}

**Testing:**
- {what was tested and how}

### Commit Messages (Conventional Commits)
```
{type}({scope}): {message}
```

### Changelog Entry
```markdown
## [{version}] - {date}

### Added/Changed/Fixed/Removed
- {change description}
```

### Files Changed ({count})
- {list of key files with brief descriptions}
```

#### Key File Detection Logic

For large diffs (>20 files), prioritize:
1. Files in `src/api/`, `routes/`, `controllers/` (API changes)
2. Files matching `*schema*`, `*migration*`, `*model*` (data changes)
3. Files in `__tests__/`, `test/`, `spec/` (test coverage)
4. Files matching `package.json`, `requirements.txt`, `Cargo.toml` (dependencies)
5. Files with most lines changed

---

### 2.9 Agent: `security-auditor`

**Location:** `devkit/agents/security-auditor.md`

**Purpose:** Scan codebase for security vulnerabilities (read-only).

```yaml
---
name: security-auditor
description: >
  Performs security audit of codebase. Scans for OWASP Top 10 vulnerabilities,
  hardcoded secrets, insecure dependencies, and compliance issues.
  Read-only - reports findings but never modifies code.
tools:
  - Read
  - Grep
  - Bash  # For running security scanners (npm audit, bandit, etc.)
model: sonnet
---
```

#### Output Template

```markdown
## Security Audit Report

### Summary
- 🔴 Critical: {count}
- 🟠 High: {count}
- 🟡 Medium: {count}
- 🟢 Low: {count}

### Critical Issues
{list with file:line and description}

### Dependency Vulnerabilities
| Package | Version | Vulnerability | Fix |
|---------|---------|---------------|-----|

### Compliance Status
- [ ] OWASP Top 10 coverage
- [ ] No hardcoded secrets
- [ ] Secure authentication patterns

### Recommendations
1. {prioritized fix}
2. {prioritized fix}
```

---

### 2.10 Agent: `test-coverage-analyzer`

**Location:** `devkit/agents/test-coverage-analyzer.md`

**Purpose:** Identify test gaps and suggest specific test cases.

```yaml
---
name: test-coverage-analyzer
description: >
  Analyzes test coverage, identifies gaps, and suggests specific test cases.
  Focuses on untested code paths, edge cases, and error handling.
tools:
  - Read
  - Grep
  - Bash  # For running coverage tools
model: sonnet
---
```

#### Output Template

```markdown
## Test Coverage Analysis

### Current Coverage
- Line coverage: {X}%
- Branch coverage: {X}%
- Function coverage: {X}%

### Critical Gaps

#### {file}:{function} ({X}% coverage)
Missing tests for:
- {scenario 1}
- {scenario 2}

Suggested test case:
```{language}
test('{description}', () => {
  // Arrange
  // Act
  // Assert
});
```

### Risk Assessment
- 🔴 High risk: {untested critical paths}
- 🟡 Medium risk: {untested utilities}
- 🟢 Low risk: {acceptable gaps}
```

---

### 2.11 Agent: `migration-planner`

**Location:** `devkit/agents/migration-planner.md`

**Purpose:** Plan framework upgrades and detect breaking changes.

```yaml
---
name: migration-planner
description: >
  Plans framework and library migrations. Analyzes codebase for deprecated
  API usage, identifies breaking changes, and creates step-by-step migration
  checklists with effort estimates.
tools:
  - Read
  - Grep
  - Bash
  - WebSearch  # For checking changelogs
  - WebFetch   # For reading migration guides
model: sonnet
---
```

#### Output Template

```markdown
## Migration Plan: {library} {old} → {new}

### Breaking Changes Detected ({count})
| Location | Current Usage | Required Change |
|----------|---------------|-----------------|

### Deprecated API Usage ({count})
- {file}:{line} - `{old_api}` → `{new_api}`

### Migration Checklist
- [ ] Update package version
- [ ] {specific change 1}
- [ ] {specific change 2}
- [ ] Run tests
- [ ] Update documentation

### Effort Estimate
- Complexity: {Low|Medium|High}
- Estimated time: {X hours/days}
- Risk level: {Low|Medium|High}

### Rollback Plan
{steps to revert if issues occur}
```

---

### 2.12 Skill: `security-guardian`

**Location:** `devkit/skills/security-guardian/`

**Structure:**
```
security-guardian/
├── SKILL.md
└── references/
    ├── owasp-top-10.md
    ├── authentication.md
    ├── authorization.md
    ├── api-security.md
    ├── secrets-management.md
    └── security-checklist.md
```

*(Full SKILL.md content as in previous spec)*

---

### 2.13 Skill: `database-migration`

**Location:** `devkit/skills/database-migration/`

**Structure:**
```
database-migration/
├── SKILL.md
└── references/
    ├── zero-downtime-patterns.md   # Expand-contract, rolling migrations
    ├── tool-comparison.md          # Flyway, Alembic, Prisma, pgroll
    ├── rollback-strategies.md      # Recovery procedures
    ├── testing-migrations.md       # Validation approaches
    └── production-checklist.md     # Pre-deployment verification
```

---

### 2.14 Skill: `observability-engineering`

**Location:** `devkit/skills/observability-engineering/`

**Structure:**
```
observability-engineering/
├── SKILL.md
└── references/
    ├── opentelemetry-guide.md      # Traces, metrics, logs
    ├── structured-logging.md       # Log format, correlation IDs
    ├── trace-correlation.md        # Connecting logs to traces
    ├── sampling-strategies.md      # Head, tail, adaptive sampling
    ├── alerting-patterns.md        # SLOs, error budgets
    └── collector-deployment.md     # Agent vs gateway patterns
```

---

### 2.15 Skill: `sre-runbook-generator`

**Location:** `devkit/skills/sre-runbook-generator/`

**Structure:**
```
sre-runbook-generator/
├── SKILL.md
└── references/
    ├── runbook-anatomy.md          # Structure and components
    ├── incident-classification.md  # SEV levels
    ├── escalation-procedures.md    # Who to call
    ├── common-scenarios.md         # Database down, API degraded, etc.
    └── automation-patterns.md      # From runbook to auto-remediation
```

---

### 2.16 Skill: `web-accessibility-auditor`

**Location:** `devkit/skills/web-accessibility-auditor/`

**Structure:**
```
web-accessibility-auditor/
├── SKILL.md
└── references/
    ├── wcag-2.2-checklist.md       # All success criteria
    ├── aria-patterns.md            # Correct ARIA usage
    ├── keyboard-navigation.md      # Focus management
    ├── screen-reader-testing.md    # NVDA, JAWS, VoiceOver
    ├── automated-testing.md        # axe-core, pa11y integration
    └── common-mistakes.md          # "No ARIA is better than bad ARIA"
```

---

## Part 3: Implementation Roadmap

### Phase 1: Quick Wins (Week 1)

| Day | Task | Deliverable |
|-----|------|-------------|
| 1 | Build core library scaffolding | `lib/core/` with git.py, coverage.py, output.py |
| 1-2 | Implement `pr-summarizer` agent | `agents/pr-summarizer.md` |
| 2 | Implement `/pr-prep` command | `commands/pr-prep.md` |
| 2-3 | Implement `test-coverage-enforcer` hook | `hooks/test-coverage-enforcer.md` |

### Phase 2: Commands & Agents (Week 2)

| Day | Task | Deliverable |
|-----|------|-------------|
| 4-5 | Implement `/trace` command | `commands/trace.md` |
| 5-6 | Implement `security-auditor` agent | `agents/security-auditor.md` |
| 6-7 | Implement `smart-context-loader` hook | `hooks/smart-context-loader.md` |

### Phase 3: More Commands & Agents (Week 3)

| Day | Task | Deliverable |
|-----|------|-------------|
| 8-9 | Implement `/regression-scan` command | `commands/regression-scan.md` |
| 9-10 | Implement `/deploy-check` command | `commands/deploy-check.md` |
| 10 | Implement `test-coverage-analyzer` agent | `agents/test-coverage-analyzer.md` |
| 10 | Implement `migration-planner` agent | `agents/migration-planner.md` |

### Phase 4: Skills (Week 4+)

| Task | Deliverable |
|------|-------------|
| `security-guardian` skill | `skills/security-guardian/` |
| `database-migration` skill | `skills/database-migration/` |
| `observability-engineering` skill | `skills/observability-engineering/` |
| `sre-runbook-generator` skill | `skills/sre-runbook-generator/` |
| `web-accessibility-auditor` skill | `skills/web-accessibility-auditor/` |

---

## Part 4: Testing Strategy

### Unit Tests

```
tests/
├── test_git.py
├── test_coverage.py
├── test_output.py
└── test_hooks/
    ├── test_coverage_enforcer.py
    └── test_context_loader.py
```

### Integration Tests

```python
def test_pr_summarizer_generates_valid_output():
    # Create test repo with changes
    # Spawn pr-summarizer agent
    # Verify output format matches template

def test_coverage_enforcer_warns_on_missing_tests():
    input_json = {
        "tool_name": "Write",
        "tool_input": {
            "file_path": "src/new_feature.py",
            "content": "def new_function(): pass"
        }
    }
    result = run_hook("test-coverage-enforcer", input_json)
    assert result.exit_code == 1  # Warning
    assert "No test file found" in result.output
```

### Performance Benchmarks

All hooks must complete within 2 seconds.

---

## Part 5: Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Adoption** | 50% of devkit users use /pr-prep | Command usage tracking |
| **Performance** | <2s for all hooks | Automated benchmarks |
| **PR Quality** | 80% of pr-summarizer outputs used without major edits | User feedback |
| **Test Coverage** | 70% of users enable coverage enforcer | Settings.json analysis |
| **Context Accuracy** | 90% of auto-loaded context is relevant | User feedback |

---

## Appendix A: CI Detection

```python
CI_ENV_VARS = [
    "CI",
    "CONTINUOUS_INTEGRATION",
    "GITHUB_ACTIONS",
    "GITLAB_CI",
    "CIRCLECI",
    "JENKINS_URL",
    "TRAVIS",
    "BUILDKITE",
]

def is_ci() -> bool:
    return any(os.getenv(var) for var in CI_ENV_VARS)
```

When CI detected:
- Disable spinners and interactive prompts
- Use plain text output (no emoji)
- Exit with appropriate codes for CI interpretation

---

## Appendix B: Severity Definitions

| Level | Exit Code | Description | Examples |
|-------|-----------|-------------|----------|
| **Critical** | 2 (block) | Immediate risk, must fix | Missing critical tests, security blockers |
| **High** | 1 (warn) | Significant risk, should fix soon | Low coverage on new code |
| **Medium** | 0 (log) | Moderate risk, fix when convenient | Missing edge case tests |
| **Low** | 0 (silent) | Best practice violation | Verbose test names |
