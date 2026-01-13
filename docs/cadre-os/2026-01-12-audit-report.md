# Cadre-OS Audit Report — 2026-01-12

## Health Score: 89/100

### Score Breakdown
| Category | Score | Weight | Weighted |
|----------|-------|--------|----------|
| Structure | 94/100 | 33% | 31.0 |
| Content | 84/100 | 33% | 27.7 |
| Metrics | 90/100 | 33% | 29.7 |
| **Total** | | | **88.5** |

---

## Executive Summary

The cadre-os skill is in **strong health** following the Phase 3 restructuring. The audit validates that the recent merges (prep.md, debrief.md, assistants-prioritization.md, prompts-agentic.md, prompts-models.md) preserved all content without truncation.

**Key Strengths:**
- Path integrity is excellent (98.5% valid)
- Merged files preserved 100% of content
- External references (Airtable, Drive) follow consistent patterns
- Asset templates are complete and properly formed
- SOP commands match commands.md definitions

**Primary Issues:**
1. **CRITICAL:** Missing file `discovery/lite-mode.md` referenced by trigger-mapping.md
2. **HIGH:** 25 commands lack explicit trigger mappings in trigger-mapping.md
3. **HIGH:** 11 broken anchor links (mostly in question-library.md TOC)
4. **MEDIUM:** Several files reference undefined terms without glossary

---

## Critical Findings

- [x] **Missing lite-mode.md** — `/artifact findings` and "findings summary" triggers reference `discovery/lite-mode.md` which does not exist
  - Severity: Critical | Effort: Small
  - **Resolution:** File was archived during Phase 3. Lite Mode content is now in `debrief.md`. Update trigger-mapping.md to point to `discovery/debrief.md` (Lite Mode section)

---

## High Priority Findings

- [ ] **25 commands missing explicit trigger mappings** (P1-2)
  - Commands like `/solutions assistants estimate`, `/techstack migrate`, `/sop discovery` lack row-by-row trigger definitions
  - Severity: High | Effort: Medium
  - Recommendation: Add explicit trigger rows for all sub-commands or document grouping behavior

- [ ] **Broken anchor links in question-library.md** (P1-4)
  - TOC references 5 section anchors (#people-questions, #process-questions, etc.) that don't exist
  - Severity: High | Effort: Trivial
  - Recommendation: Add section headings or remove TOC links

- [ ] **Brain skill invocation not documented** (P2-2)
  - brain-update-generator.md says "use the docx skill" but provides no syntax
  - Severity: High | Effort: Small
  - Recommendation: Add example: `Read the docx skill for document generation workflow`

- [ ] **Client Brain lacks operational template** (P2-5)
  - client-brain.md describes structure but provides no Google Docs template
  - Severity: High | Effort: Medium
  - Recommendation: Create template or link to existing example

- [ ] **Solutions SOP lacks entry criteria** (P2-7)
  - "Client asks what should we build?" is vague
  - Severity: High | Effort: Small
  - Recommendation: Add decision tree for when to use solutions workflow

---

## Medium Priority Findings

- [ ] **6 assets undocumented in SKILL.md** (P1-1)
  - solution-catalog.html, integration-map.html, scoping-spreadsheet.xlsx, use-case-library.xlsx, scoping-template.docx, prioritization-matrix.docx
  - Severity: Medium | Effort: Small

- [ ] **Undefined terminology across deliverables** (P2-6)
  - "synthesis," "prioritizer," "confidence calibration" used without definitions
  - Severity: Medium | Effort: Medium
  - Recommendation: Add glossary to SKILL.md or create glossary.md

- [ ] **Missing department coverage in question-library.md** (P2-2)
  - Marketing, Customer Success, Product departments missing
  - Severity: Medium | Effort: Medium

- [ ] **Transcript-specific patterns missing** (P2-2)
  - follow-up-patterns.md focuses on voice cues but discovery often uses transcripts
  - Severity: Medium | Effort: Medium

- [ ] **Multi-agent conflict resolution undefined** (P2-4)
  - prompts-agentic.md doesn't explain how to handle conflicting agent outputs
  - Severity: Medium | Effort: High

- [ ] **Template file path references undefined** (P2-3)
  - assistants-workflow.md references `spec-template.md` without absolute path
  - Severity: Medium | Effort: Small

---

## Low Priority Findings

- [ ] **README count discrepancy** (P1-6) — artifact templates section shows 8 but contains 12
- [ ] **Unused command in SOP** (P1-7) — tech-stack-survey-sop.md lists `/techstack survey` but never uses it
- [ ] **Double-dash anchor format** (P1-4) — brand-ui.md uses #tags--badges instead of #tags-badges
- [ ] **Scoring minimums may create pressure** (P2-2) — insight-markers.md lists "minimum counts" that may force findings
- [ ] **CSS examples desktop-only** (P2-8) — brand-ui.md lacks responsive examples

---

## Metrics Comparison

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| SKILL.md lines | 200-400 | 273 | ✓ |
| Max depth | 3 levels | 2 levels | ✓ |
| Files per directory | 5-15 | 2-15 | ⚠ (some sparse) |
| Dead references | 0 | 1 | ✗ |
| Orphan files | 0 | 0 | ✓ |
| Total .md files | - | 54 | - |
| Total lines (.md) | - | 22,422 | - |

---

## Content Quality Scores

| File/Area | Actionability | Completeness | Clarity | Overall |
|-----------|---------------|--------------|---------|---------|
| prep.md | 87% | 84% | 86% | 86% |
| debrief.md | 82% | 80% | 83% | 82% |
| checklists.md | 92% | 88% | 90% | 90% |
| question-library.md | 85% | 82% | 88% | 85% |
| follow-up-patterns.md | 88% | 80% | 87% | 85% |
| insight-markers.md | 90% | 88% | 92% | 90% |
| special-scenarios.md | 80% | 78% | 82% | 80% |
| brain-update-generator.md | 75% | 72% | 78% | 75% |
| assistants-workflow.md | 82% | 78% | 85% | 82% |
| assistants-categories.md | 88% | 85% | 90% | 88% |
| assistants-prioritization.md | 80% | 82% | 86% | 83% |
| assistants-spec-light.md | 87% | 84% | 89% | 87% |
| assistants-spec-full.md | 84% | 87% | 88% | 86% |
| prompts-content.md | 85% | 82% | 88% | 85% |
| prompts-analysis.md | 82% | 80% | 83% | 82% |
| prompts-code.md | 86% | 84% | 87% | 86% |
| prompts-audit.md | 88% | 86% | 90% | 88% |
| prompts-models.md | 87% | 85% | 89% | 87% |
| prompts-agentic.md | 84% | 82% | 85% | 84% |
| discovery-catalog.md | 92% | 95% | 94% | 94% |
| lite-schema.md | 88% | 90% | 91% | 90% |
| tech-stack.md | 85% | 80% | 85% | 83% |
| archetypes.md | 89% | 88% | 93% | 90% |
| playbook.md | 87% | 86% | 92% | 88% |
| strategy-deck.md | 88% | 85% | 87% | 87% |
| executive-summary.md | 90% | 88% | 90% | 89% |
| report.md | 82% | 80% | 84% | 82% |
| roadmap.md | 86% | 84% | 88% | 86% |
| solution-brief.md | 84% | 81% | 83% | 83% |
| weekly-email.md | 92% | 88% | 94% | 91% |
| meeting-agenda.md | 90% | 87% | 92% | 90% |
| monthly-review.md | 80% | 78% | 82% | 80% |
| internal-comms.md | 89% | 85% | 90% | 88% |
| discovery-catalog-sop.md | 92% | 88% | 90% | 90% |
| tech-stack-survey-sop.md | 88% | 85% | 87% | 87% |
| solutions-sop.md | 75% | 72% | 70% | 72% |
| SKILL.md | 85% | 82% | 88% | 85% |
| trigger-mapping.md | 88% | 86% | 90% | 88% |
| commands.md | 82% | 84% | 86% | 84% |
| brand.md | 88% | 80% | 90% | 86% |
| brand-ui.md | 82% | 78% | 88% | 83% |
| patterns.md | 87% | 85% | 88% | 87% |
| gaps.md | 84% | 79% | 86% | 83% |
| prioritizer.md | 86% | 88% | 87% | 87% |
| insights.md | 85% | 82% | 89% | 85% |
| data-to-artifact.md | 81% | 77% | 84% | 81% |

**Content Average: 84%**

---

## Inline Fixes Applied

1. **trigger-mapping.md line 42-43** — Updated `discovery/lite-mode.md` → `discovery/debrief.md` (Lite Mode section)

---

## Appendix: Low-Confidence Findings

These require verification before acting:

| Finding | Confidence | Notes |
|---------|------------|-------|
| Duplicate DIRECTION_MAP in tools-library.md | Medium | May be intentional for standalone use |
| Pre-filled consent guidance in brand-ui.md | Low | May be appropriate for internal artifacts |
| 8-level depth measurement | Low | Absolute path vs relative unclear |

---

## Recommendations

### Immediate (Fix Now)
1. Update trigger-mapping.md lite-mode reference → debrief.md
2. Add section headings to question-library.md for TOC anchors
3. Add 6 missing assets to SKILL.md reference table

### Short-term (This Week)
4. Add docx skill invocation example to brain-update-generator.md
5. Create glossary for undefined terms
6. Add explicit trigger mappings for all sub-commands

### Medium-term (Next Sprint)
7. Create Client Brain Google Docs template
8. Add transcript-specific patterns to follow-up-patterns.md
9. Improve solutions-sop.md with detailed step-by-step guidance
10. Add Marketing/Customer Success/Product to question-library.md

---

## Audit Methodology

- **Pass 1:** 8 parallel agents for structural validation
- **Pass 2:** 8 parallel agents for content quality assessment
- **Scoring:** Actionability (33%) + Completeness (33%) + Clarity (33%)
- **Health Score:** Structure (33%) + Content (33%) + Metrics (33%)
- **Fix Policy:** Trivial fixes applied inline, others documented

---

*Audit completed: 2026-01-12*
*Auditor: Claude (Opus 4.5)*
*Spec: skills/cadre-os/docs/2026-01-12-audit-spec.md*
