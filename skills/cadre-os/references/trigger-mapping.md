# Trigger → Reference Mapping

Maps natural language triggers and slash commands to the appropriate reference files.

## Discovery & Analysis

| Trigger | Load These References |
|---------|----------------------|
| `/prep` or "prep me for" | `discovery/prep.md` + `methodology/archetypes.md` |
| `/debrief` or "debrief", transcript pasted | `discovery/debrief.md` + `data/discovery-catalog.md` (offers comms at end) |
| `/debrief lite` or "lite mode", Excel file | `discovery/lite-mode.md` + `data/lite-schema.md` |
| `/lite` or "lite template", "excel template" | `discovery/lite-mode.md` + `data/lite-schema.md` |
| `/lite populate` or "fill in template" | `discovery/lite-mode.md` + `data/lite-schema.md` |
| `/context` or "what do we know about" | `data/discovery-catalog.md` (query Airtable + Drive) |
| `/gaps` or "coverage", "what's missing" | `synthesis/gaps.md` + `methodology/playbook.md` |
| `/patterns` or "patterns", "themes" | `synthesis/patterns.md` + `data/discovery-catalog.md` |
| `/priorities` or "prioritize", "rank" | `synthesis/prioritizer.md` |
| "what questions should I ask" | `discovery/question-library.md` |
| "archetype", stakeholder strategy | `methodology/archetypes.md` |
| "discovery approach", methodology | `methodology/playbook.md` |
| Multiple attendees, edge cases | `discovery/special-scenarios.md` |
| Key insights, "what have we learned" | `synthesis/insights.md` |

## Tech Stack

| Trigger | Load These References |
|---------|----------------------|
| `/techstack survey` or "tech stack questions" | `data/tech-stack.md` |
| `/techstack template` or "blank tech stack" | `data/tech-stack.md` |
| `/techstack parse` or "parse survey responses" | `data/tech-stack.md` |
| `/techstack research` or "research integrations", "fill in API" | `data/tech-stack.md` + `data/tech-stack-research.md` + `data/tools-library.md` |
| `/techstack migrate` or "promote tech stack" | `data/tech-stack.md` + `data/discovery-catalog.md` |
| "tech stack overview", "visualize tech stack" | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| "integration map", "show connections" | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |

## Artifacts

| Trigger | Load These References |
|---------|----------------------|
| `/artifact overview` | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| `/artifact map` | `synthesis/data-to-artifact.md` + `data/tech-stack.md` |
| `/artifact findings` | `synthesis/data-to-artifact.md` + `discovery/lite-mode.md` |
| "findings summary", "visualize findings" | `synthesis/data-to-artifact.md` + `discovery/lite-mode.md` |
| "generate artifact", "create artifact" | `synthesis/data-to-artifact.md` |

## Deliverables

| Trigger | Load These References |
|---------|----------------------|
| `/deck` or "create deck", "strategy presentation" | `deliverables/strategy-deck.md` + `brand/brand.md` + read `pptx` skill |
| `/summary` or "executive summary", "one-pager" | `deliverables/executive-summary.md` + `brand/brand.md` |
| `/report` or "findings report" | `deliverables/report.md` + `brand/brand.md` + read `docx` skill |
| `/roadmap` or "implementation plan" | `deliverables/roadmap.md` + `brand/brand.md` |
| `/brief` or "solution brief", "product brief" | `deliverables/solution-brief-guide.md` + `deliverables/solution-brief-template.md` + `brand/brand.md` + `brand/brand-ui.md` |

## Communications

| Trigger | Load These References |
|---------|----------------------|
| `/email` or "weekly email", "client update" | `comms/weekly-email.md` + `brand/brand.md` |
| `/agenda` or "meeting agenda" | `comms/meeting-agenda.md` |
| `/mbr` or "monthly review", "MBR" | `comms/monthly-review.md` + `brand/brand.md` |
| `/3p` or "3P update", "progress update" | `comms/internal-comms.md` |
| `/newsletter` or "internal newsletter" | `comms/internal-comms.md` |

## Brand

| Trigger | Load These References |
|---------|----------------------|
| "Cadre brand", "on-brand", styling | `brand/brand.md` + `brand/brand-ui.md` |
| Brand voice, tone, messaging | `brand/brand.md` + `brand/brand-ui.md` |

## Solutions

| Trigger | Load These References |
|---------|----------------------|
| `/solutions discover` or "find opportunities", "what should we build" | `solutions/assistants/workflow.md` + `solutions/assistants/opportunity-categories.md` + `solutions/prompts/patterns/` |
| `/solutions catalog` or "solution catalog", "client catalog" | `solutions/assistants/workflow.md` + `brand/brand-ui.md` |
| `/solutions brief` or "brief for [use case]" | `deliverables/solution-brief-guide.md` + `deliverables/solution-brief-template.md` + `solutions/assistants/workflow.md` + `brand/brand.md` + `brand/brand-ui.md` |
| `/solutions assistants library` or "browse use cases", "show assistant patterns" | `solutions/assistants/workflow.md` + `solutions/assistants/use-case-library.json` |
| `/solutions assistants prioritize` or "prioritize assistants", "rank opportunities" | `solutions/assistants/workflow.md` + `solutions/assistants/prioritization-framework.md` + `solutions/assistants/scoring-criteria.md` |
| `/solutions assistants validate` or "check feasibility" | `solutions/assistants/workflow.md` + `solutions/assistants/prioritization-framework.md` |
| `/solutions assistants estimate` or "estimate build time", "calculate cost" | `solutions/assistants/workflow.md` + `solutions/assistants/scoping-config.json` |
| `/solutions assistants spec` or "write spec", "create spec" | `solutions/assistants/workflow.md` + `solutions/assistants/spec-template.md` or `solutions/assistants/full-spec-template.md` |
| `/solutions prompts patterns` or "prompt patterns", "prompt examples" | `solutions/prompts/patterns/[category].md` |
| `/solutions prompts audit` or "review prompt", "improve prompt" | `solutions/prompts/audit/checklist.md` |
| `/solutions prompts template` or "system prompt template" | `assets/templates/prompts/[type].md` |
| `/solutions prompts optimize` or "optimize for Claude", "optimize for GPT" | `solutions/prompts/models/[model].md` |

## SOPs

| Trigger | Load These References |
|---------|----------------------|
| `/sop discovery` or "discovery catalog SOP/process" | Present `assets/sops/discovery-catalog-sop.md` to user |
| `/sop techstack` or "tech stack survey SOP/process" | Present `assets/sops/tech-stack-survey-sop.md` to user |
| `/sop solutions` or "solutions SOP/process" | Present `assets/sops/solutions-sop.md` to user |
| "what's the process for", "how do I", "show me the SOP" | Infer which SOP → present to user |

---

## SOP Behavior

- **Present SOP** when user asks about the process: "What's the process for debriefing?", "Show me the discovery SOP"
- **Follow SOP** when user requests action: "Debrief this transcript", "Help me populate the catalog"
- **When unclear:** Default to following the SOP, mention: "I'm following the Discovery Catalog SOP — want me to show you the full process?"
- Claude reads BOTH the SOP and detailed reference files when executing, but only presents the SOP to users

## Simple Queries

**Simple queries** (client lookup, stakeholder list): Use Data Access directly — no reference file needed.

## No-Match Fallback

If no trigger pattern matches, search all references for relevant content.
