---
name: cadre-os
description: "Cadre AI consulting operating system for strategy engagements. Use when working with Cadre clients for: (1) Discovery - session prep, debriefs, transcripts, (2) Context - client data, stakeholders, (3) Synthesis - patterns, gaps, priorities, (4) Deliverables - decks, summaries, reports, roadmaps, (5) Communications - emails, agendas, MBRs, (6) Tech Stack - surveys, research, integrations, (7) Lite Mode - Excel-based capture, (8) Solutions - AI assistants, prompts, discovery, scoping, specs, client catalog, (9) Brand - on-brand artifacts. Triggers on /prep, /debrief, /deck, /techstack, /lite, /solutions, or Cadre client names."
---

# Cadre OS

Cadre AI's consulting operating system. Single entry point for discovery, context, synthesis, deliverables, communications, and branded outputs.

**Lite Mode** = Excel-based data capture when Airtable is unavailable. Use `discovery-catalog-lite-template.xlsx` instead of Airtable Discovery Catalog.

## Commands

Slash commands provide explicit control. Use natural language OR commands — both work.

| Category | Examples |
|----------|----------|
| Discovery & Analysis | `/prep`, `/debrief`, `/context`, `/gaps`, `/patterns`, `/priorities`, `/lite` |
| Tech Stack | `/techstack survey`, `/techstack template`, `/techstack parse`, `/techstack research`, `/techstack migrate` |
| Artifacts | `/artifact overview`, `/artifact map`, `/artifact findings` |
| Solutions | `/solutions discover`, `/solutions catalog`, `/solutions brief`, `/solutions assistants *`, `/solutions prompts *` |
| Deliverables | `/deck`, `/summary`, `/report`, `/roadmap`, `/brief` |
| Communications | `/email`, `/agenda`, `/mbr`, `/3p`, `/newsletter` |
| SOPs | `/sop discovery`, `/sop techstack`, `/sop solutions` |
| Meta | `/help`, `/brand` |

See [commands.md](references/commands.md) for full command reference with arguments and examples.

See [trigger-mapping.md](references/trigger-mapping.md) for natural language trigger routing.

---

## Workflows

### Discovery Session

**Before call:** Load prep reference → Query Catalog + Brain for context → Identify attendee archetype → Select gap-targeted questions → Generate brief

**After call:** Load debrief reference → Extract entities by dimension → Score challenges/solutions → Write to Catalog → Update Brain

### Synthesis

**Pattern analysis:** Query all Catalog tables for client → Group by dimension → Identify cross-cutting themes → Score pattern strength by evidence count

**Gap analysis:** Load coverage checklist from playbook → Map existing findings → Identify uncovered areas → Recommend targeted sessions

**Prioritization:** Use stored Priority Score (challenges) and DVF Score (solutions) — do NOT recalculate

### Deliverables

**Always apply:**
1. Run synthesis first (patterns, priorities)
2. Pull client context from Catalog/Brain
3. Apply Cadre brand (load `brand/brand.md`)
4. Use appropriate system skill (pptx, docx)

**Selection guide:**
| Audience | Time | Deliverable |
|----------|------|-------------|
| Executive sponsor | 5 min | Executive Summary |
| Leadership team | 30-60 min | Strategy Deck |
| Project team | Reference doc | Findings Report |
| Implementation team | Planning | Roadmap |

### Communications

**Client comms:** Always check recent context (Catalog, Slack, Email) before drafting.

| Type | Cadence | Reference |
|------|---------|-----------|
| Weekly Email | Weekly | `comms/weekly-email.md` |
| Meeting Agenda | Per meeting | `comms/meeting-agenda.md` |
| Monthly Review | Monthly | `comms/monthly-review.md` |

**Internal comms:** Use 3P format for progress updates.

| Type | Cadence | Reference |
|------|---------|-----------|
| 3P Update | Weekly | `comms/internal-comms.md` |
| Newsletter | Monthly | `comms/internal-comms.md` |

---

## Data Write Rules

Before creating ANY Catalog records:

1. **Load schema first** — Read `data/discovery-catalog.md`
2. **Get client record ID** — Query 0_Clients, capture record ID
3. **Check existing records** — Query relevant tables for UPDATE vs CREATE
4. **Validate before writing:**
   - All field names match schema exactly
   - All select options are valid (API rejects invalid values)
   - All link fields are arrays: `["recXXX"]`

**Record creation order** (dependencies must exist first):
```
1. Session (1_Discovery_Log) → get session ID
2. People (2_People)
3. Processes (3_Process)
4. Technology (4_Technology)
5. Challenges (5_Challenges)
6. Solutions (6_Solutions)
7. Quotes (7_Quotes) → links to all above
8. Update Session with links to created records
```

**If schema read fails:** DO NOT create records. Output JSON for manual entry instead.

---

## Permission Gates

| Source | Permission |
|--------|------------|
| Catalog, Brain, Project files | Just do it (internal) |
| Slack, Gmail, Web, LinkedIn | Ask once per session, bundled |

**Bundle external sources:**
> "Should I also search Slack/Gmail and do web research? This helps with new contacts and recent context."

---

## Graceful Degradation

| Situation | Response |
|-----------|----------|
| No Brain exists | Use Catalog only, note limited narrative context |
| No Catalog records | First session — use generic framework |
| No attendees specified | Ask, or generate general prep |
| Sparse notes | Extract what's available, note low confidence |
| Unknown client | Ask for clarification, list known clients |
| Schema read fails | DO NOT create records; output JSON |
| Synthesis returns sparse results | Note limited evidence, run gap analysis |
| Brand assets unavailable | Use brand reference file |
| Lite template structure mismatch | Ask for standard template or create fresh |
| Department name mismatch (Lite) | Flag and ask for correction |
| Solution referenced but missing (Lite) | Create placeholder, flag for user |
| Lite migration fails | Output JSON for manual Airtable entry |

---

## Asset Templates

Pre-built HTML/JSX templates for common artifacts. See [assets/README.md](assets/README.md) for full inventory.

### Artifact Kit
| File | Use For |
|------|---------|
| [cadre-components.html](assets/artifact-kit/cadre-components.html) | Reusable HTML components with Cadre styling |
| [cadre-components.jsx](assets/artifact-kit/cadre-components.jsx) | Reusable React components with Cadre styling |

### Ready-to-Use Templates
| File | Use For |
|------|---------|
| [client-kickoff.html](assets/artifact-templates/client-kickoff.html) | Client engagement kickoff presentation |
| [monthly-business-review.html](assets/artifact-templates/monthly-business-review.html) | MBR presentation template (HTML artifact) |
| [mbr-template-01-07-25.pptx](assets/templates/mbr-template-01-07-25.pptx) | MBR slide library (42 slides, 13 sections, 29 variations) |
| [roi-calculator.jsx](assets/artifact-templates/roi-calculator.jsx) | Interactive ROI calculator |
| [transformation-deck.html](assets/artifact-templates/transformation-deck.html) | AI transformation strategy deck |
| [discovery-catalog-lite-template.xlsx](assets/templates/discovery-catalog-lite-template.xlsx) | Lite mode Excel template |
| [tech-stack-survey-template.xlsx](assets/templates/tech-stack-survey-template.xlsx) | Tech stack inventory template |
| [tech-stack-overview.html](assets/artifact-templates/tech-stack-overview.html) | Tech stack summary from survey data |
| [integration-map.jsx](assets/artifact-templates/integration-map.jsx) | Visual tool connection map |
| [findings-summary.html](assets/artifact-templates/findings-summary.html) | Discovery findings from Lite data |

**To use:** Copy template, replace placeholder content with client data from synthesis.

---

## Reference Files

### Discovery & Methodology

| File | Purpose |
|------|---------|
| [prep.md](references/discovery/prep.md) | Session prep (quick or deep mode) |
| [debrief.md](references/discovery/debrief.md) | Session debrief (quick or full mode) |
| [lite-mode.md](references/discovery/lite-mode.md) | Lite mode workflow + population |
| [question-library.md](references/discovery/question-library.md) | Question selection |
| [follow-up-patterns.md](references/discovery/follow-up-patterns.md) | Conditional follow-ups |
| [research-protocols.md](references/discovery/research-protocols.md) | External research |
| [insight-extraction.md](references/discovery/insight-extraction.md) | Entity extraction |
| [checklists.md](references/discovery/checklists.md) | Quality checks |
| [special-scenarios.md](references/discovery/special-scenarios.md) | Edge cases |
| [brain-update-generator.md](references/discovery/brain-update-generator.md) | Brain update docs |
| [archetypes.md](references/methodology/archetypes.md) | Stakeholder engagement strategy |
| [playbook.md](references/methodology/playbook.md) | Discovery phases, coverage checklist |

### Data & Schema

| File | Purpose |
|------|---------|
| [discovery-catalog.md](references/data/discovery-catalog.md) | Airtable schema — load before ANY Catalog writes |
| [client-brain.md](references/data/client-brain.md) | Brain structure, update templates |
| [lite-schema.md](references/data/lite-schema.md) | Lite mode Excel schema, field mapping |
| [tech-stack.md](references/data/tech-stack.md) | Tech stack survey workflows |
| [tech-stack-research.md](references/data/tech-stack-research.md) | Research process with inference logic |
| [tools-library.md](references/data/tools-library.md) | Airtable Tools Library schema, queries |

### Synthesis

| File | Purpose |
|------|---------|
| [patterns.md](references/synthesis/patterns.md) | Pattern analysis |
| [gaps.md](references/synthesis/gaps.md) | Gap/coverage analysis |
| [prioritizer.md](references/synthesis/prioritizer.md) | Challenge/solution ranking |
| [insights.md](references/synthesis/insights.md) | Key insight generation |
| [data-to-artifact.md](references/synthesis/data-to-artifact.md) | Generating branded artifacts from data |

### Deliverables

| File | Purpose |
|------|---------|
| [strategy-deck.md](references/deliverables/strategy-deck.md) | Strategy presentation |
| [executive-summary.md](references/deliverables/executive-summary.md) | One-pager for leadership |
| [report.md](references/deliverables/report.md) | Detailed findings document |
| [roadmap.md](references/deliverables/roadmap.md) | Implementation plan |
| [solution-brief-guide.md](references/deliverables/solution-brief-guide.md) | Workshop protocol for briefs |
| [solution-brief-template.md](references/deliverables/solution-brief-template.md) | Modular brief template (7 modules) |

### Communications

| File | Purpose |
|------|---------|
| [weekly-email.md](references/comms/weekly-email.md) | Client weekly updates |
| [meeting-agenda.md](references/comms/meeting-agenda.md) | Meeting agendas |
| [monthly-review.md](references/comms/monthly-review.md) | Monthly business reviews |
| [internal-comms.md](references/comms/internal-comms.md) | 3P updates, newsletters |

### Brand

| File | Purpose |
|------|---------|
| [brand.md](references/brand/brand.md) | Positioning, voice, messaging |
| [brand-ui.md](references/brand/brand-ui.md) | UI components + before/after examples |

### Solutions - Assistants

| File | Purpose |
|------|---------|
| [workflow.md](references/solutions/assistants/workflow.md) | Any solutions command |
| [use-case-library.json](references/solutions/assistants/use-case-library.json) | Discover, library browse |
| [scoping-config.json](references/solutions/assistants/scoping-config.json) | Estimate calculations |
| [prioritization-framework.md](references/solutions/assistants/prioritization-framework.md) | Prioritize, validate |
| [opportunity-categories.md](references/solutions/assistants/opportunity-categories.md) | Discover |
| [scoring-criteria.md](references/solutions/assistants/scoring-criteria.md) | Prioritize |
| [spec-template.md](references/solutions/assistants/spec-template.md) | Light specs |
| [full-spec-template.md](references/solutions/assistants/full-spec-template.md) | Full specs |

### Solutions - Prompts

| File | Purpose |
|------|---------|
| [content-creation.md](references/solutions/prompts/patterns/content-creation.md) | Content prompts |
| [analysis-research.md](references/solutions/prompts/patterns/analysis-research.md) | Analysis prompts |
| [code-generation.md](references/solutions/prompts/patterns/code-generation.md) | Code prompts |
| [problem-solving.md](references/solutions/prompts/patterns/problem-solving.md) | Decision/planning prompts |
| [education.md](references/solutions/prompts/patterns/education.md) | Teaching/tutoring prompts |
| [checklist.md](references/solutions/prompts/audit/checklist.md) | Prompt audit/review |
| [claude-4-5.md](references/solutions/prompts/models/claude-4-5.md) | Claude optimization |
| [gpt-5-1.md](references/solutions/prompts/models/gpt-5-1.md) | GPT optimization |
| [gemini-3-pro.md](references/solutions/prompts/models/gemini-3-pro.md) | Gemini optimization |
| [react-workflows.md](references/solutions/prompts/agentic/react-workflows.md) | Agent patterns |
| [tool-definitions.md](references/solutions/prompts/agentic/tool-definitions.md) | Tool use patterns |
| [multi-agent.md](references/solutions/prompts/agentic/multi-agent.md) | Multi-agent orchestration |

### Navigation

| File | Purpose |
|------|---------|
| [commands.md](references/commands.md) | Full command reference with arguments |
| [trigger-mapping.md](references/trigger-mapping.md) | Natural language → reference routing |

### SOPs (User-Facing)

| File | Present When |
|------|--------------|
| [discovery-catalog-sop.md](assets/sops/discovery-catalog-sop.md) | User asks about discovery process |
| [tech-stack-survey-sop.md](assets/sops/tech-stack-survey-sop.md) | User asks about tech stack process |
| [solutions-sop.md](assets/sops/solutions-sop.md) | User asks about solutions/builds process |
