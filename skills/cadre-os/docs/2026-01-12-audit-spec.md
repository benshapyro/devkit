# Cadre-OS Post-Refactoring Audit Specification

**Date:** 2026-01-12
**Scope:** Comprehensive validation and quality assessment post-Phase 3 restructuring
**Output:** Actionable checklist + narrative report with health score

---

## Executive Summary

This audit validates the Phase 3 cadre-os restructuring and evaluates overall skill quality. It uses a two-pass methodology: structural validation followed by full content review. Findings are prioritized via severity × effort matrix with trivial fixes applied inline.

---

## Audit Objectives

1. **Validate** — Confirm restructuring didn't break anything
2. **Measure** — Quantify improvements against ideal targets
3. **Assess** — Evaluate content quality for dual audience (Claude + humans)
4. **Identify** — Surface remaining improvement opportunities
5. **Score** — Produce numeric health rating for tracking

---

## Scope

### In Scope
- All files in `skills/cadre-os/` except archive
- SKILL.md accuracy and completeness
- All reference files (discovery/, solutions/, data/, etc.)
- All asset files and templates
- All SOPs
- Cross-references and internal links
- External reference structure (Airtable, Drive patterns)

### Exclusions
- `skills/archive/cadre-os/` — Intentionally deprecated files
- Functional testing of actual command execution
- Verification of external system content (Airtable data, Drive files)

---

## Methodology

### Two-Pass Approach

#### Pass 1: Structure & Validation
**Focus:** Does everything exist and connect properly?

| Agent | Area | Checks |
|-------|------|--------|
| 1 | SKILL.md | All paths exist, descriptions match content, no orphan references |
| 2 | trigger-mapping.md | All paths resolve, triggers map to correct files |
| 3 | Merged files | Content completeness (sections + key tables/examples preserved) |
| 4 | Cross-references | Internal links work, no circular dependencies |
| 5 | External refs | Airtable IDs follow pattern, Drive paths formatted correctly |
| 6 | Assets | All templates exist, README accurate, no orphans |
| 7 | SOPs | Commands match commands.md, no broken references |
| 8 | Metrics | File counts, line counts, depth measurements |

#### Pass 2: Content Quality
**Focus:** Is the content good for both Claude and human users?

| Agent | Area | Evaluation Criteria |
|-------|------|---------------------|
| 1-2 | Discovery files | Actionability, completeness, clarity |
| 3-4 | Solutions files | Actionability, completeness, clarity |
| 5 | Data/methodology | Actionability, completeness, clarity |
| 6 | Deliverables/comms | Actionability, completeness, clarity |
| 7 | SOPs + assets | Actionability, completeness, clarity |
| 8 | SKILL.md + triggers | Actionability, completeness, clarity |

---

## Quality Criteria

Each file evaluated on three dimensions (weighted equally):

### Actionability (33%)
- Can someone follow these instructions and succeed?
- Are steps concrete and executable?
- Are edge cases addressed?
- Is there a clear "what to do when X" guidance?

### Completeness (33%)
- Are there gaps or missing steps?
- Are all referenced items defined?
- Is the full workflow covered end-to-end?
- Are prerequisites stated?

### Clarity (33%)
- Is it well-written and unambiguous?
- Is detail level appropriate (not too sparse, not too verbose)?
- Does it work for both Claude (parseable) and humans (readable)?
- Are examples provided where helpful?

---

## Ideal Target State

### SKILL.md
| Metric | Target | Rationale |
|--------|--------|-----------|
| Line count | 200-400 | Room for growth if it improves clarity |
| Dead references | 0 | All listed files must exist |
| Description accuracy | 100% | Descriptions match actual file content |

### Directory Structure
| Metric | Target | Rationale |
|--------|--------|-----------|
| Max depth | 3 levels | references/category/subcategory/ max |
| Files per directory | 5-15 | Not too sparse, not too cluttered |
| Orphan files | 0 | Everything referenced from somewhere |

### Context Efficiency
| Workflow | Target Tokens | Rationale |
|----------|---------------|-----------|
| /prep | <15k | Should load SKILL.md + prep.md + maybe archetypes |
| /debrief | <20k | SKILL.md + debrief.md + schema + checklists |
| /solutions discover | <25k | Workflow + categories + library subset |

### Content Quality
| Dimension | Target Score | Notes |
|-----------|--------------|-------|
| Actionability | >80% | Instructions should be followable |
| Completeness | >85% | Few gaps or missing pieces |
| Clarity | >80% | Clear for both audiences |

---

## Findings Classification

### Severity Levels

| Level | Definition | Examples |
|-------|------------|----------|
| **Critical** | Blocks functionality | Broken reference to required file, missing schema |
| **High** | Significant impact | Wrong command in SOP, misleading instruction |
| **Medium** | Notable issue | Unclear section, missing example |
| **Low** | Minor improvement | Typo, formatting inconsistency |

### Effort Levels

| Level | Definition | Examples |
|-------|------------|----------|
| **Trivial** | <5 min fix | Typo, broken link, simple clarification |
| **Small** | 15-30 min | Add missing section, rewrite unclear paragraph |
| **Medium** | 1-2 hours | Restructure file, add comprehensive examples |
| **Large** | >2 hours | Major content creation, architectural change |

### Priority Matrix

```
                    EFFORT
              Trivial  Small  Medium  Large
         ┌─────────┬───────┬───────┬───────┐
Critical │ FIX NOW │ FIX NOW│ Plan  │ Plan  │
    S    ├─────────┼───────┼───────┼───────┤
    E    │ FIX NOW │ Soon  │ Plan  │Backlog│
 High    ├─────────┼───────┼───────┼───────┤
    V    │ Inline  │ Soon  │Backlog│Backlog│
 Medium  ├─────────┼───────┼───────┼───────┤
    E    │ Inline  │Backlog│Backlog│ Skip  │
    R    ├─────────┼───────┼───────┼───────┤
 Low     │ Inline  │Backlog│ Skip  │ Skip  │
    I    └─────────┴───────┴───────┴───────┘
    T
    Y

FIX NOW = Address immediately during audit
Inline  = Fix during audit if encountered
Soon    = Address within this session after audit
Plan    = Document for next work session
Backlog = Log for future consideration
Skip    = Note but don't track formally
```

---

## Fix Policy

### Fix Inline (During Audit)
- Typos
- Broken internal links
- Obviously wrong paths
- Simple formatting issues
- Missing punctuation

### Document for Later
- Content gaps requiring research
- Structural changes affecting multiple files
- Subjective improvements needing discussion
- Changes requiring external verification

---

## Uncertainty Handling

All findings flagged with confidence level:

| Confidence | Meaning | Action |
|------------|---------|--------|
| **High** | Definitely an issue | Include in findings, act on it |
| **Medium** | Likely an issue | Include in findings, verify before fixing |
| **Low** | Possibly an issue | Include in appendix, investigate if time permits |

---

## Health Score Calculation

### Formula
```
Health Score = (Structure Score × 0.33) + (Content Score × 0.33) + (Metrics Score × 0.33)
```

### Structure Score (0-100)
- Path validity: 40 points
- Cross-reference integrity: 30 points
- No orphan files: 20 points
- External ref patterns: 10 points

### Content Score (0-100)
- Actionability average: 33 points
- Completeness average: 33 points
- Clarity average: 34 points

### Metrics Score (0-100)
- SKILL.md in target range: 25 points
- Directory depth OK: 25 points
- Context efficiency targets met: 25 points
- No critical structural issues: 25 points

---

## Output Format

### Report Structure

```markdown
# Cadre-OS Audit Report — [DATE]

## Health Score: XX/100

### Score Breakdown
- Structure: XX/100
- Content: XX/100
- Metrics: XX/100

## Executive Summary
[2-3 paragraph overview]

## Critical Findings
- [ ] Finding 1 (Severity/Effort)
- [ ] Finding 2 (Severity/Effort)

## High Priority Findings
- [ ] Finding 3 (Severity/Effort)
...

## Medium Priority Findings
...

## Low Priority Findings
...

## Metrics Comparison

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| ... | ... | ... | ✓/✗ |

## Content Quality Scores

| File | Actionability | Completeness | Clarity | Overall |
|------|---------------|--------------|---------|---------|
| ... | XX% | XX% | XX% | XX% |

## Inline Fixes Applied
1. [Description of fix]
2. ...

## Appendix: Low-Confidence Findings
...
```

---

## Execution Plan

### Prerequisites
1. Clean git state (commit any pending changes)
2. docs/ directory exists
3. No other processes modifying skill files

### Pass 1 Execution
1. Launch 8 parallel agents for structural validation
2. Each agent reports findings to central collection
3. Compile Pass 1 findings
4. Apply trivial inline fixes
5. Commit fixes: "audit: fix trivial issues found in Pass 1"

### Pass 2 Execution
1. Launch 8 parallel agents for content quality
2. Each agent scores files on 3 dimensions
3. Compile Pass 2 scores and findings
4. Apply trivial inline fixes
5. Commit fixes: "audit: fix trivial issues found in Pass 2"

### Report Generation
1. Calculate health score
2. Generate report from template
3. Save to `skills/cadre-os/docs/2026-01-12-audit-report.md`
4. Commit report

### Completion Criteria
- Zero Critical severity findings remaining
- All findings documented in report
- Health score calculated
- Report saved to docs/

---

## Agent Assignments

### Pass 1 Agents

| ID | Name | Files | Deliverable |
|----|------|-------|-------------|
| P1-1 | SKILL Validator | SKILL.md | Path existence, description accuracy |
| P1-2 | Trigger Validator | trigger-mapping.md | Path resolution, trigger coverage |
| P1-3 | Merge Validator | prep.md, debrief.md, merged solutions | Content preservation check |
| P1-4 | CrossRef Validator | All .md files | Internal link validation |
| P1-5 | External Validator | All .md files | Airtable/Drive pattern check |
| P1-6 | Asset Validator | assets/, templates/ | Existence, README accuracy |
| P1-7 | SOP Validator | assets/sops/ | Command accuracy |
| P1-8 | Metrics Collector | Full skill | Counts, measurements, stats |

### Pass 2 Agents

| ID | Name | Files | Deliverable |
|----|------|-------|-------------|
| P2-1 | Discovery Quality A | prep.md, debrief.md | Quality scores + findings |
| P2-2 | Discovery Quality B | checklists.md, question-library.md, others | Quality scores + findings |
| P2-3 | Solutions Quality A | assistants-*.md | Quality scores + findings |
| P2-4 | Solutions Quality B | prompts-*.md | Quality scores + findings |
| P2-5 | Data Quality | data/*.md, methodology/*.md | Quality scores + findings |
| P2-6 | Deliverables Quality | deliverables/*.md, comms/*.md | Quality scores + findings |
| P2-7 | SOP/Asset Quality | SOPs, asset README | Quality scores + findings |
| P2-8 | Core Quality | SKILL.md, trigger-mapping.md, commands.md | Quality scores + findings |

---

## Appendix: Interview Decisions Log

| Question | Decision | Rationale |
|----------|----------|-----------|
| Baseline comparison | Ideal target state | Forward-looking, define what "good" looks like |
| Uncertainty handling | Flag all with confidence | Nothing missed, reviewer can filter |
| Merge verification depth | Section + key content | Balanced thoroughness |
| Target metrics | All (context, nav, counts) | Comprehensive measurement |
| Content vs structure | Full content review | User priority on quality |
| Quality criteria | All three equal | Balanced assessment |
| Workload approach | Multiple passes | Thorough, organized |
| Audience | Both Claude + humans | Dual-purpose files |
| SKILL.md target | 300-400 lines OK | Room for clarity improvements |
| Max depth | 3 levels OK | Flexibility where logical |
| Report format | Checklist + narrative | Actionable yet contextual |
| Fix policy | Trivial inline | Efficient, low-risk |
| External refs | Verify structure only | Pragmatic scope |
| Focus areas | Distribute evenly | Trust systematic approach |
| Done criteria | Zero critical + documented | Outcome-based |
| Health score | Numeric (X/100) | Trackable, comparable |
| Score weights | 33% each | Balanced view |
| Pass 2 scope | All files | Comprehensive |
| Exclusions | Archive only | Focused on live content |
