---
name: cadre-os
description: "Cadre AI consulting operating system for strategy engagements. Use when working with Cadre clients for: (1) Discovery - session prep, debriefs, transcripts, (2) Context - client data, stakeholders, (3) Synthesis - patterns, gaps, priorities, (4) Deliverables - decks, summaries, reports, roadmaps, (5) Communications - emails, agendas, MBRs, (6) Tech Stack - surveys, research, integrations, (7) Lite Mode - Excel-based capture, (8) Solutions - AI assistants, prompts, discovery, scoping, specs, client catalog, (9) Brand - on-brand artifacts. Triggers on /prep, /debrief, /deck, /techstack, /lite, /solutions, or Cadre client names."
---

# Cadre OS

Cadre AI's consulting operating system. Single entry point for discovery, context, synthesis, deliverables, communications, and branded outputs.

## Commands

Slash commands provide explicit control. Use natural language OR commands — both work.

### Discovery & Analysis
| Command | Action | Arguments |
|---------|--------|-----------|
| `/prep` | Discovery session prep | `[client]` `[attendee]` `[duration]` |
| `/debrief` | Process session transcript | `[client]` `[mode:quick\|full\|lite]` |
| `/context` | Pull client data | `[client]` `[dimension]` |
| `/gaps` | Coverage gap analysis | `[client]` |
| `/patterns` | Cross-session pattern analysis | `[client]` |
| `/priorities` | Rank challenges and solutions | `[client]` |
| `/lite` | Get or populate lite Excel template | `[client]` `[action:template\|populate\|migrate]` |

### Tech Stack Inventory
| Command | Action | Arguments |
|---------|--------|-----------|
| `/techstack survey` | Output Google Form questions | `[client]` |
| `/techstack template` | Provide blank Excel template | — |
| `/techstack parse` | Parse survey responses into grid | (paste text or upload file) |
| `/techstack research` | Research API/integrations for tools | `[client]` `[verbose]` |
| `/techstack migrate` | Promote to Discovery Catalog | `[client]` |

### Artifacts
| Command | Action | Arguments |
|---------|--------|-----------|
| `/artifact overview` | Generate Tech Stack Overview (HTML) | `[client]` |
| `/artifact map` | Generate Integration Map (JSX; say "convert to HTML" for Portal) | `[client]` |
| `/artifact findings` | Generate Findings Summary (HTML) | `[client]` |

### Solutions (AI Builds)
| Command | Action | Arguments |
|---------|--------|-----------|
| `/solutions discover` | Scan docs + Catalog for assistant and prompt opportunities | `[client]` |
| `/solutions catalog` | Generate client-facing Solution Catalog HTML | `[client]` |
| `/solutions brief` | Generate solution brief for AI opportunity | `[use case]` |
| `/solutions assistants library` | Browse 50 proven assistant patterns | — |
| `/solutions assistants prioritize` | Score, rank, and classify opportunities | `[client]` |
| `/solutions assistants validate` | Check feasibility blockers | `[use case]` |
| `/solutions assistants estimate` | Calculate build time and cost | `[use case]` |
| `/solutions assistants spec` | Generate implementation spec | `[use case]` `[light\|full\|formal]` |
| `/solutions prompts patterns` | Browse 45+ prompt patterns by category | `[category]` |
| `/solutions prompts audit` | Review and improve an existing prompt | (paste prompt) |
| `/solutions prompts template` | Generate production system prompt | `[type]` |
| `/solutions prompts optimize` | Model-specific optimization guidance | `[model]` |

### Deliverables
| Command | Action | Arguments |
|---------|--------|-----------|
| `/deck` | Generate strategy deck | `[client]` |
| `/summary` | Executive summary | `[client]` |
| `/report` | Detailed findings report | `[client]` |
| `/roadmap` | Implementation roadmap | `[client]` |
| `/brief` | Solution/product brief | `[solution name]` |

### Communications
| Command | Action | Arguments |
|---------|--------|-----------|
| `/email` | Weekly client email | `[client]` |
| `/agenda` | Meeting agenda | `[client]` `[meeting-type]` |
| `/mbr` | Monthly business review | `[client]` |
| `/3p` | Internal 3P update | `[client]` |
| `/newsletter` | Internal newsletter | — |

### SOPs (Standard Operating Procedures)
| Command | Action |
|---------|--------|
| `/sop discovery` | Show Discovery Catalog SOP |
| `/sop techstack` | Show Tech Stack Survey SOP |

### Meta
| Command | Action |
|---------|--------|
| `/help` | List available commands |
| `/brand` | Show brand quick reference |

**Usage examples:**
```
/prep Acme Corp Sarah Chen 60min
/debrief Acme Corp full
/lite template
/lite populate Acme Corp
/techstack survey Acme Corp
/techstack research Acme Corp verbose
/artifact overview Acme Corp
/artifact map Acme Corp
/artifact findings Acme Corp
/solutions discover Acme Corp
/solutions catalog Acme Corp
/solutions assistants library
/solutions assistants prioritize Acme Corp
/solutions assistants spec Policy Lookup full
/solutions prompts patterns content-creation
/solutions prompts audit
/solutions prompts template customer-support
/deck Acme Corp
/email Acme Corp
/sop discovery
/sop techstack
/sop solutions
```

**Arguments are optional.** If omitted, Claude will ask for needed info.

---

## Trigger → Reference Mapping

| Trigger | Load These References |
|---------|----------------------|
| `/prep` or "prep me for" | `discovery/prep.md` + `methodology/archetypes.md` |
| `/debrief` or "debrief", transcript pasted | `discovery/debrief.md` + `data/discovery-catalog.md` (offers comms at end) |
| `/debrief lite` or "lite mode", Excel file | `discovery/lite-mode.md` + `data/lite-schema.md` |
| `/lite` or "lite template", "excel template" | `discovery/lite-mode.md` + `data/lite-schema.md` |
| `/lite populate` or "fill in template" | `discovery/lite-mode.md` + `data/lite-schema.md` |
| `/techstack survey` or "tech stack questions" | `data/tech-stack.md` |
| `/techstack template` or "blank tech stack" | `data/tech-stack.md` |
| `/techstack parse` or "parse survey responses" | `data/tech-stack.md` |
| `/techstack research` or "research integrations", "fill in API" | `data/tech-stack.md` + `data/tech-stack-research.md` + `data/tools-library.md` |
| `/techstack migrate` or "promote tech stack" | `data/tech-stack.md` + `data/discovery-catalog.md` |
| `/context` or "what do we know about" | `data/discovery-catalog.md` (query Airtable + Drive) |
| `/gaps` or "coverage", "what's missing" | `synthesis/gaps.md` + `methodology/playbook.md` |
| `/patterns` or "patterns", "themes" | `synthesis/patterns.md` + `data/discovery-catalog.md` |
| `/priorities` or "prioritize", "rank" | `synthesis/prioritizer.md` |
| `/deck` or "create deck", "strategy presentation" | `deliverables/strategy-deck.md` + `brand/brand.md` + read `pptx` skill |
| `/summary` or "executive summary", "one-pager" | `deliverables/executive-summary.md` + `brand/brand.md` |
| `/report` or "findings report" | `deliverables/report.md` + `brand/brand.md` + read `docx` skill |
| `/roadmap` or "implementation plan" | `deliverables/roadmap.md` + `brand/brand.md` |
| `/brief` or "solution brief", "product brief" | `deliverables/solution-brief-guide.md` + `deliverables/solution-brief-template.md` + `brand/brand.md` + `brand/brand-ui.md` |
| `/solutions brief` or "brief for [use case]" | `deliverables/solution-brief-guide.md` + `deliverables/solution-brief-template.md` + `solutions/assistants/workflow.md` + `brand/brand.md` + `brand/brand-ui.md` |
| `/email` or "weekly email", "client update" | `comms/weekly-email.md` + `brand/brand.md` |
| `/agenda` or "meeting agenda" | `comms/meeting-agenda.md` |
| `/mbr` or "monthly review", "MBR" | `comms/monthly-review.md` + `brand/brand.md` |
| `/3p` or "3P update", "progress update" | `comms/internal-comms.md` |
| `/newsletter` or "internal newsletter" | `comms/internal-comms.md` |
| "what questions should I ask" | `discovery/question-library.md` |
| "archetype", stakeholder strategy | `methodology/archetypes.md` |
| "discovery approach", methodology | `methodology/playbook.md` |
| Multiple attendees, edge cases | `discovery/special-scenarios.md` |
| Key insights, "what have we learned" | `synthesis/insights.md` |
| "Cadre brand", "on-brand", styling | `brand/brand.md` + `brand/brand-ui.md` |
| Brand voice, tone, messaging | `brand/brand.md` + `brand/brand-ui.md` |
| "tech stack overview", "visualize tech stack" | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| "integration map", "show connections" | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| "findings summary", "visualize findings" | `synthesis/data-to-artifact.md` + `discovery/lite-mode.md` |
| "generate artifact", "create artifact" | `synthesis/data-to-artifact.md` |
| `/artifact overview` | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| `/artifact map` | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| `/artifact findings` | `synthesis/data-to-artifact.md` + `discovery/lite-mode.md` |
| `/solutions discover` or "find opportunities", "what should we build" | `solutions/assistants/workflow.md` + `solutions/assistants/opportunity-categories.md` + `solutions/prompts/patterns/` |
| `/solutions catalog` or "solution catalog", "client catalog" | `solutions/assistants/workflow.md` + `brand/brand-ui.md` |
| `/solutions assistants library` or "browse use cases", "show assistant patterns" | `solutions/assistants/workflow.md` + `solutions/assistants/use-case-library.json` |
| `/solutions assistants prioritize` or "prioritize assistants", "rank opportunities" | `solutions/assistants/workflow.md` + `solutions/assistants/prioritization-framework.md` + `solutions/assistants/scoring-criteria.md` |
| `/solutions assistants validate` or "check feasibility" | `solutions/assistants/workflow.md` + `solutions/assistants/prioritization-framework.md` |
| `/solutions assistants estimate` or "estimate build time", "calculate cost" | `solutions/assistants/workflow.md` + `solutions/assistants/scoping-config.json` |
| `/solutions assistants spec` or "write spec", "create spec" | `solutions/assistants/workflow.md` + `solutions/assistants/spec-template.md` or `solutions/assistants/full-spec-template.md` |
| `/solutions prompts patterns` or "prompt patterns", "prompt examples" | `solutions/prompts/patterns/[category].md` |
| `/solutions prompts audit` or "review prompt", "improve prompt" | `solutions/prompts/audit/checklist.md` |
| `/solutions prompts template` or "system prompt template" | `assets/templates/prompts/[type].md` |
| `/solutions prompts optimize` or "optimize for Claude", "optimize for GPT" | `solutions/prompts/models/[model].md` |
| `/sop discovery` or "discovery catalog SOP/process" | Present `assets/sops/discovery-catalog-sop.md` to user |
| `/sop techstack` or "tech stack survey SOP/process" | Present `assets/sops/tech-stack-survey-sop.md` to user |
| `/sop solutions` or "solutions SOP/process" | Present `assets/sops/solutions-sop.md` to user |
| "what's the process for", "how do I", "show me the SOP" | Infer which SOP → present to user |

**SOP Behavior:**
- **Present SOP** when user asks about the process: "What's the process for debriefing?", "Show me the discovery SOP"
- **Follow SOP** when user requests action: "Debrief this transcript", "Help me populate the catalog"
- **When unclear:** Default to following the SOP, mention: "I'm following the Discovery Catalog SOP — want me to show you the full process?"
- Claude reads BOTH the SOP and detailed reference files when executing, but only presents the SOP to users

**Simple queries** (client lookup, stakeholder list): Use Data Access below directly — no reference file needed.

---

## Quick Reference: Cadre Brand

### Essential Colors

| Color | Hex | Use |
|-------|-----|-----|
| Warm Black | `#0C0407` | Primary text, buttons, headlines |
| Coral Red | `#DB4545` | Primary accent — CTAs, highlights, badges |
| Secondary Blue | `#08749B` | Supporting CTAs, links |
| Warm White | `#FAF9F6` | Primary background |
| Cream | `#F2EFE4` | Hero sections, feature areas |

### Voice
- Confident but approachable
- Evidence-based, not buzzword-heavy
- Action-oriented — every insight leads to a recommendation

For full brand guidelines: `brand/brand.md` (positioning, messaging) and `brand/brand-ui.md` (components)

---

## Quick Reference: Discovery

### Five Dimensions

| Dimension | Captures |
|-----------|----------|
| **People** | Stakeholders, roles, influence, sentiment, relationships |
| **Process** | Workflows, pain points, automation readiness, handoffs |
| **Technology** | Systems, integrations, data quality, tech debt |
| **Challenges** | Problems, impact, urgency, root causes |
| **Solutions** | Opportunities, feasibility, effort, dependencies |

### Nine Stakeholder Archetypes

| Archetype | Signal | Core Approach |
|-----------|--------|---------------|
| **Champion** | Enthusiastic, volunteering | Leverage as ally, don't over-rely |
| **Skeptic** | Arms crossed, "prove it" | Acknowledge concerns, show evidence |
| **Political** | Watches others, hedges | Build private rapport, understand agenda |
| **Technical** | Deep dives, jargon | Speak their language, respect expertise |
| **Executive** | Time-pressured, strategic | Lead with outcomes, be concise |
| **Quiet** | Brief answers, reserved | Create space, use written follow-ups |
| **Overwhelmed** | Frazzled, scope concerns | Show empathy, demonstrate quick wins |
| **Historian** | "We tried that", past-focused | Honor history, show what's different |
| **New Arrival** | Fresh perspective, limited context | Value outside view, help navigate politics |

For full engagement strategies, load `methodology/archetypes.md`.

### Four Discovery Modes

| Mode | Duration | Use When |
|------|----------|----------|
| **Prep Quick** | 2-5 min | Strong existing context, same-day call |
| **Prep Deep** | 10-15 min | Gaps in context, new attendees, external research needed |
| **Debrief Quick** | 3-5 min | Brief notes, display findings only, no Catalog writes |
| **Debrief Full** | 10-15 min | Full transcript, extract all entities, write to Catalog |
| **Lite Mode** | 5-10 min | Early-stage capture, client handoff, Excel-based storage |

---

## Lite Mode (Excel-Based Capture)

Lightweight alternative for early-stage engagements or client handoffs.

| Use Lite When | Use Full When |
|---------------|---------------|
| First 1-2 sessions | 3+ sessions |
| Client wants raw data | Need scoring (Priority/DVF) |
| Workshop / rapid assessment | Cross-client analysis |

**Commands:** `/lite template` | `/lite populate [client]` | `/lite migrate [client]` | `/debrief [client] lite`

**Template:** `assets/templates/discovery-catalog-lite-template.xlsx`

For full workflow: `discovery/lite-mode.md`

---

## Quick Reference: Solutions

Discover, scope, and deliver AI solutions (assistants + prompts) for clients.

### Workflow

```
DISCOVER → PRIORITIZE → VALIDATE → ESTIMATE → SPEC → CATALOG
```

### Assistants

50 proven patterns across 6 functions:
- Sales (10), Marketing (13), Finance/Ops (5)
- HR (5), Customer Success (6), General Productivity (11)

### Prompts

45+ prompt patterns across 5 categories:
- Content Creation, Analysis & Research, Code Generation
- Problem Solving, Education

### Solution Catalog Contents

Client-facing HTML artifact with two tabs:

**Assistants tab:**
- Name, Category, Status, Impact
- Purpose description
- Launch button (when Live)
- Modal with: full description, problem statement, sample prompts, knowledge base

**Prompts tab:**
- Name, Category, Priority
- Purpose description
- Copy button
- Modal with: full prompt text, usage guidance

**Statuses:** Not Selected, Backlog, In Progress, Testing, Live
**Impact levels:** High, Medium, Low

For full workflow: `solutions/assistants/workflow.md`

---

## Quick Reference: Prompt Patterns

45+ patterns for writing, optimizing, and auditing prompts.

### Pattern Categories

| Category | Examples |
|----------|----------|
| Content Creation | Blog posts, reports, documentation, marketing copy |
| Analysis & Research | SWOT, competitive analysis, synthesis, forecasting |
| Code Generation | Functions, debugging, architecture, code review |
| Problem Solving | Decisions, root cause, planning, risk assessment |
| Education | Explanations, quizzes, curriculum, tutoring |

### Model Optimization

| Model | Key Technique |
|-------|---------------|
| Claude 4.5 | XML tags, extreme explicitness |
| GPT-5.1 | Persistence instructions, adaptive reasoning |
| Gemini 3.0 Pro | Temperature 1.0, context-first structure |

### Template Types

- `customer-support.md` — Support agent with tool usage
- `document-analysis.md` — Multi-document synthesis
- `code-review.md` — Security, performance, style review
- `executive-briefing.md` — C-suite decision support

For patterns: `prompts/patterns/[category].md`
For audit: `prompts/audit/checklist.md`

---

## Data Access

### Discovery Catalog (Airtable)

**Base ID:** `apprH2AppvnKfUpT0`

| Table | ID | Primary Field |
|-------|-----|---------------|
| 0_Clients | `tbl9MiW4wWEHoNw6t` | Client Name |
| 1_Discovery_Log | `tblS0FNxft1FRkytp` | Session Title |
| 2_People | `tbl10xPpFKblRy3PL` | Full Name |
| 3_Process | `tblAibn7iHAvGqP1P` | Process Name |
| 4_Technology | `tblDdIuLzEQ2DwBYF` | Tool Name |
| 5_Challenges | `tblmGPfC8Y85laT6j` | Challenge Name |
| 6_Solutions | `tblleK2rzvC5V7sR0` | Solution Name |
| 7_Quotes | `tbl6dIJFlKBqlqmp4` | Quote Text |

**Common queries:**
```
# Get active clients
list_records: Base apprH2AppvnKfUpT0, Table tbl9MiW4wWEHoNw6t
Filter: NOT({Engagement Status} = 'Churned')

# Get all findings for a client
list_records: Filter by Client field with client record ID

# Get high-priority challenges
list_records: Table tblmGPfC8Y85laT6j, Filter: {Priority Score} >= 64
```

For full schema, load `data/discovery-catalog.md`.

### Client Brain (Google Drive)

```
# Find a client's brain
google_drive_search: name contains '[Client] Brain'

# Get Brain Link from Airtable client record
The Brain Link field in 0_Clients contains the Google Doc URL
```

For Brain structure, load `data/client-brain.md`.

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

## Scoring Reference

**Challenge Priority:** Impact × Urgency × Readiness (each 1-5, max 125)

**Solution DVF:** Desirability × Viability × Feasibility (each 1-5, max 125)

**Pattern Strength:** 1 source = Low | 2-3 sources = Medium | 4+ sources = High

**Insight Markers:** ⚡ Surprise | 🔄 Pattern | ⚠️ Contradiction | 💡 Opportunity

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
| Brand assets unavailable | Use brand quick reference in this file |
| Lite template structure mismatch | Ask for standard template or create fresh |
| Department name mismatch (Lite) | Flag and ask for correction |
| Solution referenced but missing (Lite) | Create placeholder, flag for user |
| Lite migration fails | Output JSON for manual Airtable entry |

---

## Asset Templates

Pre-built HTML/JSX templates for common artifacts. Copy and customize.

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

### Discovery
| File | Load When |
|------|-----------|
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

### Methodology
| File | Load When |
|------|-----------|
| [archetypes.md](references/methodology/archetypes.md) | Stakeholder engagement strategy |
| [playbook.md](references/methodology/playbook.md) | Discovery phases, coverage checklist |

### Data
| File | Load When |
|------|-----------|
| [discovery-catalog.md](references/data/discovery-catalog.md) | Before ANY Catalog writes (includes quickref) |
| [client-brain.md](references/data/client-brain.md) | Brain structure, update templates |
| [lite-schema.md](references/data/lite-schema.md) | Lite mode Excel schema, field mapping |
| [tech-stack.md](references/data/tech-stack.md) | Tech stack survey workflows |
| [tech-stack-research.md](references/data/tech-stack-research.md) | Research process with inference logic |
| [tools-library.md](references/data/tools-library.md) | Airtable Tools Library schema, queries |

### Synthesis
| File | Load When |
|------|-----------|
| [patterns.md](references/synthesis/patterns.md) | Pattern analysis |
| [gaps.md](references/synthesis/gaps.md) | Gap/coverage analysis |
| [prioritizer.md](references/synthesis/prioritizer.md) | Challenge/solution ranking |
| [insights.md](references/synthesis/insights.md) | Key insight generation |
| [data-to-artifact.md](references/synthesis/data-to-artifact.md) | Generating branded artifacts from data |

### Deliverables
| File | Load When |
|------|-----------|
| [strategy-deck.md](references/deliverables/strategy-deck.md) | Strategy presentation |
| [executive-summary.md](references/deliverables/executive-summary.md) | One-pager for leadership |
| [report.md](references/deliverables/report.md) | Detailed findings document |
| [roadmap.md](references/deliverables/roadmap.md) | Implementation plan |
| [solution-brief-guide.md](references/deliverables/solution-brief-guide.md) | Workshop protocol for briefs |
| [solution-brief-template.md](references/deliverables/solution-brief-template.md) | Modular brief template (7 modules) |

### Communications
| File | Load When |
|------|-----------|
| [weekly-email.md](references/comms/weekly-email.md) | Client weekly updates |
| [meeting-agenda.md](references/comms/meeting-agenda.md) | Meeting agendas |
| [monthly-review.md](references/comms/monthly-review.md) | Monthly business reviews |
| [internal-comms.md](references/comms/internal-comms.md) | 3P updates, newsletters |

### Brand
| File | Load When |
|------|-----------|
| [brand.md](references/brand/brand.md) | Positioning, voice, messaging |
| [brand-ui.md](references/brand/brand-ui.md) | UI components + before/after examples |

### Solutions - Assistants
| File | Load When |
|------|-----------|
| [workflow.md](references/solutions/assistants/workflow.md) | Any solutions command |
| [use-case-library.json](references/solutions/assistants/use-case-library.json) | Discover, library browse |
| [scoping-config.json](references/solutions/assistants/scoping-config.json) | Estimate calculations |
| [prioritization-framework.md](references/solutions/assistants/prioritization-framework.md) | Prioritize, validate |
| [opportunity-categories.md](references/solutions/assistants/opportunity-categories.md) | Discover |
| [scoring-criteria.md](references/solutions/assistants/scoring-criteria.md) | Prioritize |
| [spec-template.md](references/solutions/assistants/spec-template.md) | Light specs |
| [full-spec-template.md](references/solutions/assistants/full-spec-template.md) | Full specs |

### Solutions - Prompts
| File | Load When |
|------|-----------|
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

### SOPs
| File | Present When |
|------|--------------|
| [discovery-catalog-sop.md](assets/sops/discovery-catalog-sop.md) | User asks about discovery process |
| [tech-stack-survey-sop.md](assets/sops/tech-stack-survey-sop.md) | User asks about tech stack process |
| [solutions-sop.md](assets/sops/solutions-sop.md) | User asks about solutions/builds process |

### Asset Templates
| File | Use For |
|------|---------|
| [solution-catalog.html](assets/artifact-templates/solution-catalog.html) | Client-facing Solution Catalog (Assistants + Prompts) |
| [use-case-library.xlsx](assets/templates/use-case-library.xlsx) | Use case library (source of truth) |
| [scoping-spreadsheet.xlsx](assets/templates/scoping-spreadsheet.xlsx) | Build time calculator |
| [scoping-template.docx](assets/templates/scoping-template.docx) | Formal scoping document |
| [prioritization-matrix.docx](assets/templates/prioritization-matrix.docx) | Prioritization workshop template |
| [customer-support.md](assets/templates/prompts/customer-support.md) | Support agent system prompt |
| [document-analysis.md](assets/templates/prompts/document-analysis.md) | Document synthesis system prompt |
| [code-review.md](assets/templates/prompts/code-review.md) | Code review system prompt |
| [executive-briefing.md](assets/templates/prompts/executive-briefing.md) | Executive briefing system prompt |
