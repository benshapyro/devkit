# Devkit Extension Opportunities Research

**Date:** 2026-01-13
**Status:** Spec Complete
**Spec:** [2026-01-13-extension-spec.md](2026-01-13-extension-spec.md)

## Executive Summary

Research conducted by 5 parallel agents analyzing AI coding tools (Claude Code, Cursor, Copilot, Windsurf), community discussions, GitHub issues, and developer pain points. Goal: identify high-value commands, hooks, skills, and agents for the devkit.

**Key Finding:** Despite 85% AI tool adoption, developers report significant frustration with security gaps, context management, and workflow friction. Most complaints center on missing capabilities rather than model quality.

---

## Top 20 Ideas by Category

### Commands (Slash Commands)

| # | Name | One-liner | Effort | Value |
|---|------|-----------|--------|-------|
| 1 | `/trace` | Gather production error context for debugging | Medium (4-8h) | Critical |
| 2 | `/review-prep` | Generate PR descriptions with review guidance | Medium (4-8h) | High |
| 3 | `/deps-audit` | Security scan dependencies + generate upgrade PRs | Complex (1-2d) | Critical |
| 4 | `/regression-scan` | Identify blast radius before committing changes | Complex (1-2d) | High |
| 5 | `/deploy-check` | Pre-deployment safety checklist | Complex (1-2d) | High |

#### Command Details

**`/trace`**
- **Use case:** Developer receives production error, needs full debugging context
- **Implementation:** Parse stack trace → fetch source code → git blame → find similar errors → generate diagnostic report
- **Why valuable:** Developers spend 50%+ time debugging; compresses hours of context gathering into minutes

**`/review-prep`**
- **Use case:** Before creating PR, generate comprehensive description and catch obvious issues
- **Implementation:** Analyze git diff → detect breaking changes → check test coverage → generate PR description with review guidance
- **Why valuable:** Code review is #1 bottleneck (42-48% time savings possible)

**`/deps-audit`**
- **Use case:** Address security vulnerabilities in dependencies
- **Implementation:** Run security scanners → identify vulnerable packages → check changelogs for breaking changes → generate upgrade strategy
- **Why valuable:** 86% of codebases have vulnerable dependencies; current tools require separate setup

**`/regression-scan`**
- **Use case:** Before committing shared code changes, understand blast radius
- **Implementation:** Build dependency graph → find callers → identify affected tests → generate impact report
- **Why valuable:** Prevents "I didn't know that would break that" incidents

**`/deploy-check`**
- **Use case:** Pre-deployment safety verification
- **Implementation:** Run test suite → type check → security scan → check migrations → verify env vars → generate readiness report
- **Why valuable:** Codifies senior engineer knowledge about production readiness

---

### Hooks (Event-Driven Automation)

| # | Name | Event | One-liner | Effort | Value |
|---|------|-------|-----------|--------|-------|
| 1 | `secrets-scanner` | PreToolUse | Block hardcoded secrets before writing | Medium (6-8h) | Critical |
| 2 | `ai-security-scanner` | PostToolUse | SAST scan for SQL injection, XSS, etc. | Medium (6-8h) | Critical |
| 3 | `dependency-validator` | PreToolUse | Validate packages exist (prevent slopsquatting) | Medium (6-8h) | High |
| 4 | `test-coverage-enforcer` | PostToolUse | Warn on missing test coverage | Complex (1-2d) | High |
| 5 | `smart-context-loader` | UserPromptSubmit | Auto-inject relevant project context | Complex (1-2d) | High |

#### Hook Details

**`secrets-scanner`**
- **Event:** PreToolUse (Edit/Write)
- **Implementation:** Pattern match 100+ secret formats (AWS keys, GitHub tokens, etc.) + high-entropy string detection
- **Why valuable:** 39M secrets leaked on GitHub in 2024; catches AI-hallucinated secrets in generated code

**`ai-security-scanner`**
- **Event:** PostToolUse (Edit/Write)
- **Implementation:** Run lightweight SAST (bandit, eslint-plugin-security) on modified files
- **Why valuable:** 40% of AI-generated code contains security flaws; targets OWASP Top 10

**`dependency-validator`**
- **Event:** PreToolUse (Edit/Write on package.json/requirements.txt)
- **Implementation:** Query npm/PyPI registries to verify packages exist; check download stats and age
- **Why valuable:** Prevents "slopsquatting" attacks where AI suggests non-existent packages

**`test-coverage-enforcer`**
- **Event:** PostToolUse (Edit/Write)
- **Implementation:** Check if test files exist for modified source; run targeted coverage analysis
- **Why valuable:** Maintains TDD discipline with AI; catches untested code before production

**`smart-context-loader`**
- **Event:** UserPromptSubmit
- **Implementation:** Parse prompt for keywords → query git log → extract TODOs → inject relevant context
- **Why valuable:** Eliminates manual context gathering; improves AI response accuracy

---

### Skills (Domain Knowledge)

| # | Name | Domain | Effort | Value |
|---|------|--------|--------|-------|
| 1 | `security-guardian` | OWASP patterns, auth, API security | Medium (3-5d) | Critical |
| 2 | `database-migration-toolkit` | Zero-downtime migrations, rollback | Medium (4-5d) | High |
| 3 | `observability-engineer` | OpenTelemetry, structured logging, tracing | Medium (4-5d) | High |
| 4 | `sre-runbook-generator` | Incident response, operational playbooks | Simple (2-3d) | High |
| 5 | `web-accessibility-auditor` | WCAG 2.2, ARIA, screen reader testing | Medium (3-4d) | High |

#### Skill Details

**`security-guardian`**
- **Provides:** OAuth 2.1/OIDC patterns, RBAC/ABAC authorization, OWASP Top 10 prevention
- **References:** owasp-top-10-2025.md, auth-patterns.md, api-security-checklist.md
- **Why valuable:** Security consistently #1 concern; AI frequently hallucinates insecure patterns

**`database-migration-toolkit`**
- **Provides:** Expand-contract patterns, tool selection (Flyway/Alembic/Prisma), rollback procedures
- **References:** expand-contract-pattern.md, production-checklist.md, disaster-recovery.md
- **Why valuable:** Database migrations are "riskiest area" - manual processes cause months of delays

**`observability-engineer`**
- **Provides:** OpenTelemetry fundamentals, trace-log correlation, sampling strategies
- **References:** otel-log-model.md, trace-correlation.md, collector-patterns.md
- **Why valuable:** OpenTelemetry is industry standard; most devs don't understand proper sampling

**`sre-runbook-generator`**
- **Provides:** Runbook templates, incident classification, escalation procedures, PIR templates
- **References:** runbook-anatomy.md, sre-best-practices.md, incident-classification.md
- **Why valuable:** SOC 2/ISO 27001/DORA require documented incident response; most teams lack runbooks

**`web-accessibility-auditor`**
- **Provides:** WCAG 2.2 checklist, ARIA patterns, keyboard navigation, screen reader testing
- **References:** wcag-2.2-checklist.md, aria-authoring-practices.md, common-mistakes.md
- **Why valuable:** 4,605 ADA lawsuits in 2024; European Accessibility Act enforceable June 2025

---

### Agents (Specialized Sub-Agents)

| # | Name | Specialization | Effort | Value |
|---|------|----------------|--------|-------|
| 1 | `security-auditor` | SAST/SCA scanning, compliance validation | Medium (1d) | Critical |
| 2 | `pr-summarizer` | Generate PR descriptions, changelog entries | Simple (2-4h) | High |
| 3 | `test-coverage-analyzer` | Identify test gaps, recommend test cases | Medium (1d) | High |
| 4 | `migration-planner` | Framework upgrades, breaking change detection | Medium (1d) | High |
| 5 | `performance-profiler` | Identify bottlenecks, optimization opportunities | Medium (1d) | High |

#### Agent Details

**`security-auditor`**
- **Tools:** Read, Grep, Bash (security scanners)
- **Returns:** Security audit report with critical issues, dependency vulnerabilities, compliance status
- **Why valuable:** Security scanning generates massive context pollution; keeps audits comprehensive

**`pr-summarizer`**
- **Tools:** Read, Bash (git), Grep
- **Returns:** PR title, description, conventional commit messages, changelog entry
- **Why valuable:** Vague PR titles force reviewers to play detective; succinct summaries are "pure gold"

**`test-coverage-analyzer`**
- **Tools:** Read, Grep, Bash (coverage tools)
- **Returns:** Coverage report, critical gaps, recommended test cases with code stubs
- **Why valuable:** CI/CD integration with coverage reduces MTTR; risk-based testing is best practice

**`migration-planner`**
- **Tools:** Read, Grep, Bash, WebSearch, WebFetch
- **Returns:** Breaking changes detected, migration checklist, effort estimate, risk level
- **Why valuable:** AI can analyze dependencies and identify deprecated components automatically

**`performance-profiler`**
- **Tools:** Read, Grep, Bash (profiling tools)
- **Returns:** Hot paths, memory issues, database query analysis, optimization priorities
- **Why valuable:** Continuous profiling reveals 20-30% wasted cloud resources on inefficient code

---

## Key Pain Points from Research

### 1. Security at Scale
- 45% of AI-generated code fails security tests
- 322% more privilege escalation paths than human-written code
- 40% increase in secrets exposure
- AI-assisted commits merge 4x faster, bypassing review

### 2. The "Almost Right" Problem
- 66% spend more time debugging AI code than writing it
- 19% slower completion times in controlled studies
- Trust in AI accuracy dropped from 40% to 29% YoY

### 3. Context Rot
- 65% report missing context during refactoring
- Context gaps cited MORE often than hallucinations as root cause
- Standard AI only "sees" few thousand tokens in 400k+ file codebases

### 4. Technical Debt Accumulation
- AI PRs contain 1.7x more issues than human PRs
- 4x more code cloning (increasing maintenance burden)
- 7.2% decrease in delivery stability with 25% increase in AI usage

### 5. Token Limits and Incomplete Work
- "Half-painted kitchen" syndrome
- Tasks start but don't complete
- Unpredictable billing creates procurement friction

---

## Feature Gaps Identified

### High Priority
1. **Background Agents / Async Execution** - Fire and forget task queuing
2. **Persistent Memory Across Sessions** - Remember preferences, history, decisions
3. **Cost Transparency and Budget Controls** - Real-time token usage visibility
4. **Checkpoint Systems with Rollback** - Instant rewind for multi-file changes
5. **Security Validation Gates** - OWASP Top 10 scanning before code review

### Medium Priority
6. **Multi-Agent Orchestration Dashboard** - Visibility for parallel agents
7. **Spec-Driven Development Enforcement** - Requirements.md as source of truth
8. **Observability and Session Replay** - Trace every step of agent execution
9. **Architecture Debt Tracking** - Measure "AI debt" separately
10. **Monorepo / Polyglot Intelligence** - Cross-language dependency understanding

---

## Emerging Trends

1. **Model Context Protocol (MCP)** - 97M monthly SDK downloads, 10k active servers
2. **Legacy Modernization Agents** - 75% of enterprises will use AI by 2028
3. **Vibe Coding** - Shift from line-by-line to high-level conversation
4. **Progressive Disclosure** - Show complexity gradually
5. **Plan-Before-Act Workflows** - Require AI to show work before executing

---

## Implementation Priority Matrix

### Tier 1: Critical Security (Build First)
- `secrets-scanner` hook
- `security-auditor` agent
- `security-guardian` skill

### Tier 2: Developer Velocity (Build Next)
- `/review-prep` command
- `/trace` command
- `pr-summarizer` agent

### Tier 3: Code Quality (Build After)
- `test-coverage-analyzer` agent
- `dependency-validator` hook
- `database-migration-toolkit` skill

---

## Quick Wins (< 1 day effort)

1. **`pr-summarizer` agent** - 2-4 hours, immediate value
2. **`sre-runbook-generator` skill** - 2-3 days, universal need
3. **`/review-prep` command** - 4-8 hours, addresses top pain point

---

## Sources

### Developer Feedback
- Stack Overflow Developer Survey 2025
- HackerNews discussions on AI coding
- Reddit developer communities
- GitHub issues for Claude Code, Cursor, Copilot

### Security Research
- Veracode GenAI Code Security Report
- GitGuardian 2024 Secrets Report
- OWASP Top 10 2025

### Industry Analysis
- MIT Technology Review: AI Coding 2026
- RedMonk: 10 Things Developers Want from Agentic IDEs
- Qodo: State of AI Code Quality 2025
- InfoQ: AI-Generated Code Technical Debt

### Tool Documentation
- Claude Code Slash Commands
- Cursor Commands Documentation
- GitHub Copilot Chat Cheat Sheet
- Anthropic Model Context Protocol

---

## Validation Results

**Status:** Complete (2026-01-13)

Cross-referenced all 20 proposed ideas against existing devkit implementations.

---

### Commands Validation

| Proposed | Status | Overlap | Recommendation |
|----------|--------|---------|----------------|
| `/trace` | **Novel** | Partial: `systematic-debugging` skill planned but not built | Build - fills major debugging gap |
| `/review-prep` | **Extend** | `/review` exists but focuses on review, not PR generation | Extend `/review` or create standalone |
| `/deps-audit` | **Novel** | None. `security-scanner` skill planned (Tier 1) but not built | Build - critical security gap |
| `/regression-scan` | **Novel** | None. No blast radius analysis exists | Build - high value, moderate effort |
| `/deploy-check` | **Extend** | `/validate` exists but not deployment-specific | Extend `/validate` or standalone |

**Existing Commands in Devkit:**
- `/slop`, `/review`, `/validate`, `/ship`, `/plan`, `/research`, `/greenfield`, `/backlog`, `/progress`, `/learn`

---

### Hooks Validation

| Proposed | Status | Overlap | Recommendation |
|----------|--------|---------|----------------|
| `secrets-scanner` | **Extend** | `sensitive-file-guard` blocks file access by name, not content | Extend to scan content for secret patterns |
| `ai-security-scanner` | **Novel** | None. No SAST for SQL injection, XSS | Create new hook |
| `dependency-validator` | **Novel** | None. No package registry validation | Create new hook |
| `test-coverage-enforcer` | **Extend** | `test-on-change` runs tests but doesn't enforce coverage | Extend with coverage parsing |
| `smart-context-loader` | **Extend** | `skill-activation` suggests skills but doesn't inject context | Extend to inject project docs |

**Existing Hooks in Devkit:**
- `sensitive-file-guard`, `dangerous-command-blocker`, `auto-format`, `test-on-change`, `skill-activation`

---

### Skills Validation

| Proposed | Status | Overlap | Recommendation |
|----------|--------|---------|----------------|
| `security-guardian` | **Novel** | `api-design-patterns` has basic auth but no security focus | Create - significant gap |
| `database-migration-toolkit` | **Novel** | None. No migration patterns exist | Create - genuine gap |
| `observability-engineer` | **Investigate** | `service-integration` mentions observability but likely shallow | Verify depth, then create or extend |
| `sre-runbook-generator` | **Novel** | `internal-comms` has incident reports but not runbooks | Create - genuine gap |
| `web-accessibility-auditor` | **Novel/Extend** | `frontend-ui-integration` has cursory a11y mention | Create standalone or extend existing |

**Existing Skills in Devkit (29 total):**
- Development: `react-patterns`, `api-design-patterns`, `test-generator`, `tailwind-conventions`, `service-integration`, `webapp-testing`
- Content: `doc-coauthoring`, `documentation-templates`, `content-repurposer`, `ace-content-engine`
- Documents: `pdf`, `pptx`, `xlsx`
- Business: `cadre-os`, `product-management`, `competitive-intelligence`, `expense-categorizer`
- Design: `frontend-ui-integration`, `theme-factory`, `canvas-design`, `algorithmic-art`, `ai-art-generation`, `slack-gif-creator`
- Integration: `anthropic-messages-api`, `openai-responses-api`, `browser`, `data-querying`
- Meta: `skill-creator`, `internal-comms`

---

### Agents Validation

| Proposed | Status | Overlap | Recommendation |
|----------|--------|---------|----------------|
| `security-auditor` | **Extend** | `code-reviewer` has security checks but not SAST/SCA tools | Create for dedicated scanning + compliance |
| `pr-summarizer` | **Novel** | None. No PR description/changelog generation | Create - true gap |
| `test-coverage-analyzer` | **Novel** | `test-generator` skill exists but for generation, not analysis | Create for gap identification |
| `migration-planner` | **Novel** | None. `documentation-researcher` could support | Create - genuine gap |
| `performance-profiler` | **Duplicate** | `performance-optimizer` exists with full coverage | Skip - already exists |

**Existing Agents in Devkit (7 total):**
- `code-reviewer`, `debugger`, `documentation-researcher`, `git-helper`, `performance-optimizer`, `refactoring-assistant`, `spec-discovery`

---

### Summary: What to Build

#### Truly Novel (No Overlap)
- `/deps-audit` command
- `/regression-scan` command
- `ai-security-scanner` hook
- `dependency-validator` hook
- `security-guardian` skill
- `database-migration-toolkit` skill
- `sre-runbook-generator` skill
- `pr-summarizer` agent
- `test-coverage-analyzer` agent
- `migration-planner` agent

#### Extend Existing
- `/trace` → extend `debugger` agent or create command
- `/review-prep` → extend `/review` command
- `/deploy-check` → extend `/validate` command
- `secrets-scanner` → extend `sensitive-file-guard` hook
- `test-coverage-enforcer` → extend `test-on-change` hook
- `smart-context-loader` → extend `skill-activation` hook
- `security-auditor` → extend `code-reviewer` or create new
- `observability-engineer` → investigate `service-integration` first
- `web-accessibility-auditor` → extend `frontend-ui-integration` or standalone

#### Skip (Already Exists)
- `performance-profiler` → `performance-optimizer` agent already covers this

---

### Revised Priority Matrix

**Tier 1: Build First (Novel + High Value)**
1. `security-guardian` skill - No security skill exists
2. `/deps-audit` command - Critical security gap
3. `pr-summarizer` agent - Quick win, high value

**Tier 2: Extend Existing (Low Effort)**
4. Extend `sensitive-file-guard` with content scanning
5. Extend `/review` to generate PR descriptions
6. Extend `test-on-change` with coverage enforcement

**Tier 3: Build Next (Novel + Medium Effort)**
7. `ai-security-scanner` hook - SAST for AI code
8. `dependency-validator` hook - Slopsquatting prevention
9. `database-migration-toolkit` skill
10. `sre-runbook-generator` skill
