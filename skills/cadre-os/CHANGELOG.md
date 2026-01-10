# Changelog

## [2.0.0] - 2025-01-09

### What Changed for Users

- **SKILL.md is now a navigation hub** - Commands and triggers moved to reference files for faster loading
- **Faster context loading** - Reduced from 651 to ~280 lines
- **Clearer Lite Mode** - Now defined once: "Excel-based capture when Airtable unavailable"
- **All content preserved** - Just reorganized into proper reference locations
- **Comprehensive assets documentation** - Full inventory in `assets/README.md`

### Technical Changes

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
- `CHANGELOG.md` - This file
- Grouped navigation hub table in Reference Files section
- "Last verified" notes on model-specific prompt references

**Standardized:**

- Placeholder notation to `{{VAR}}` format
- Role references made generic (project lead, consultant)

### Migration

This is a breaking change. Redeploy to get the new structure.

```bash
./scripts/deploy.py
```

All functionality is preserved — content is reorganized, not removed.
