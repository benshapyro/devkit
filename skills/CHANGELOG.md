# Skills Changelog

All notable changes to skills in this repository.

## [Unreleased]

## 2025-01-21

### Added

**Phase 4 Domain Skills**

- **security-guardian** - OWASP Top 10, authentication, authorization, API security, secrets management
- **database-migration** - Zero-downtime patterns, tool comparison, rollback strategies, testing
- **observability-engineering** - OpenTelemetry, structured logging, tracing, alerting, collectors
- **sre-runbook-generator** - Runbook templates, incident classification, escalation, automation
- **web-accessibility-auditor** - WCAG 2.2, ARIA patterns, keyboard navigation, screen reader testing

---

## cadre-os

### [2.1.0] - 2025-01-10

#### What Changed

- **Removed deprecated template** - Deleted `mbr-template-legacy.pptx`
- **Eliminated code duplication** - Inference logic now single source in `tech-stack-research.md`
- **Defined Pre-flight Check** - Added to `checklists.md` (was referenced but undefined)
- **Merged solution-brief files** - `solution-brief-guide.md` + `solution-brief-template.md` → `solution-brief.md`
- **Standardized SOP commands** - Fixed 7 inconsistent commands in `solutions-sop.md`
- **Added cross-references** - `question-library.md` → `follow-up-patterns.md`

#### Technical Changes

| Action | File | Details |
|--------|------|---------|
| DELETE | `assets/templates/mbr-template-legacy.pptx` | Deprecated |
| EDIT | `references/data/tools-library.md` | Removed 30 lines, added cross-ref |
| EDIT | `references/discovery/checklists.md` | Added Pre-flight Check definition |
| MERGE | `references/deliverables/solution-brief.md` | Combined guide + template |
| EDIT | `assets/sops/solutions-sop.md` | Fixed 7 command names |
| EDIT | `references/discovery/question-library.md` | Added cross-ref |
| EDIT | `SKILL.md` | Updated solution-brief reference |

**Net result:** -166 lines (425 added, 591 removed)

---

### [2.0.0] - 2025-01-09

#### What Changed for Users

- **SKILL.md is now a navigation hub** - Commands and triggers moved to reference files for faster loading
- **Faster context loading** - Reduced from 651 to ~280 lines
- **Clearer Lite Mode** - Now defined once: "Excel-based capture when Airtable unavailable"
- **All content preserved** - Just reorganized into proper reference locations
- **Comprehensive assets documentation** - Full inventory in `assets/README.md`

#### Technical Changes

**Extracted to new files:**

| Original Location | New File |
|-------------------|----------|
| Lines 15-111 (9 command tables) | `references/commands.md` |
| Lines 117-174 (trigger routing) | `references/trigger-mapping.md` |

**Removed (duplicated existing refs):**

| Lines | Content | Already Exists In |
|-------|---------|-------------------|
| 186-203 | Brand quick ref | `references/brand/brand.md` |
| 207-244 | Discovery dimensions | `references/methodology/playbook.md` |
| 247-261 | Lite mode info | `references/discovery/lite-mode.md` |
| 269-306 | Solutions workflow | `references/solutions/assistants/workflow.md` |
| 310-341 | Prompt patterns | `references/solutions/prompts/patterns/*` |
| 344-387 | Airtable schema | `references/data/discovery-catalog.md` |
| 469-477 | Scoring reference | `references/solutions/assistants/scoring-criteria.md` |

**Added:**

- `references/commands.md` - Full command reference (~100 lines)
- `references/trigger-mapping.md` - Trigger-to-reference routing (~100 lines)
- `assets/README.md` - Comprehensive asset documentation (~150 lines)
- Grouped navigation hub table in Reference Files section
- "Last verified" notes on model-specific prompt references

**Standardized:**

- Placeholder notation to `{{VAR}}` format
- Role references made generic (project lead, consultant)

#### Migration

This is a breaking change. Redeploy to get the new structure.

```bash
./scripts/deploy.py
```

All functionality is preserved — content is reorganized, not removed.
