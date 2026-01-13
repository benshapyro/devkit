# Discovery Catalog Lite Mode

Lightweight Excel-based discovery capture for early-stage engagements or client handoffs.

**Full SOP:** See `assets/sops/discovery-catalog-sop.md` for complete step-by-step instructions.

---

## Contents

1. [Operational Details](#operational-details)
2. [When to Use Lite Mode](#when-to-use-lite-mode)
3. [Mode Detection](#mode-detection)
4. [Workflows](#lite-mode-workflows)
5. [Post-Call Workflow](#post-call-workflow)
6. [Entity Extraction](#entity-extraction)
7. [Validation](#validation)
8. [Writing to Excel](#writing-to-excel)
9. [Complete Workflow Example](#complete-workflow-example)
10. [Generate Artifacts](#generate-artifacts)
11. [Offer Comms](#offer-comms)
12. [Error Handling](#error-handling)

---

## Operational Details

### When to Create

**Trigger:** SOW is signed OR first discovery call is scheduled (whichever comes first)

Create the empty catalog structure before any meetings happen — have it ready to populate.

### File Location & Naming

```
Cadre Team Drive /
└── Clients /
    └── [Client Name] /
        ├── Discovery Catalog.xlsx        ← The catalog
        ├── Transcripts /
        │   └── [YYYY-MM-DD] [Type] - [Attendees].txt
        └── Discovery /
            └── Debriefs /
                └── [YYYY-MM-DD] Debrief - [Attendees].md
```

**File name:** `Discovery Catalog.xlsx` (no date stamp — it's a living doc)

### Claude Project Setup

1. Create a Claude Project for the client
2. Upload `Discovery Catalog.xlsx` to Project Knowledge
3. After each update, re-upload the latest version

### Claude Chat Naming

When starting a debrief chat: `[YYYY-MM-DD] Debrief - [Attendee(s)]`

**Examples:**
- `2024-12-30 Debrief - Sarah Chen`
- `2024-12-30 Debrief - Sales Team Workshop`

---

## When to Use Lite Mode

| Scenario | Use Lite Mode |
|----------|---------------|
| First 1-2 discovery sessions | ✓ Quick capture, migrate later |
| Rapid assessment / workshop | ✓ Same-day deliverable |
| Client wants raw data | ✓ Handoff artifact |
| Full engagement (3+ sessions) | ✗ Use Airtable Catalog |
| Need scoring (Priority/DVF) | ✗ Use Airtable Catalog |
| Cross-client pattern analysis | ✗ Use Airtable Catalog |

## Mode Detection

**Auto-detect Lite Mode when:**
- User uploads Excel file matching template structure
- User references "lite", "excel", or "template"
- User says "quick capture" or "don't use Airtable"

**Default to Full Mode when:**
- Client exists in Airtable Catalog
- No Excel file present
- User says "save to Catalog" or "full debrief"

**Explicit override:** User can always say "use lite mode" or "use full mode"

---

## Lite Mode Workflows

### 1. Provide Blank Template

**Triggers:**
- "give me the discovery template"
- "I need the excel catalog"
- "discovery catalog lite template"
- "start a new lite capture"

**Action:**
1. Copy template from `assets/discovery-catalog-lite-template.xlsx`
2. Present to user
3. Offer to fill it in: "Want me to populate this from a transcript, web research, or information you provide?"

---

### 2. Populate from Transcript

**Triggers:**
- User provides transcript + Excel template (uploaded or just requested)
- "fill in the template from this transcript"
- "debrief [client] lite mode"

**Process:**
1. Extract entities using standard debrief logic (see `debrief.md`)
2. Map to Lite schema (see `lite-schema.md`)
3. Write to Excel using openpyxl
4. Present updated file

**Field mapping:**
| Extracted Entity | Lite Location |
|------------------|---------------|
| Department/Team mentioned | Departments sheet |
| Challenges | Issues sheet |
| Solutions/Opportunities | Solutions sheet |
| Quotes | Issues → Pain Point Quote |
| Root causes | Issues → Pain Point Cause |
| Supporting data | Issues → Finding 1, 2, 3... |
| Technology mentioned | Solutions → Tech columns |

---

### 3. Populate from Research

**Triggers:**
- "research [company] and fill in the template"
- "populate from what we know about [client]"

**Process:**
1. Search connected sources (Drive, Slack, web) for client info
2. Extract issues and solutions from findings
3. Map to Lite schema
4. Write to Excel
5. Present with confidence notes

**Sources to search:**
- Google Drive: Client Brain, project docs
- Web: Company news, press releases, industry reports
- Slack: Recent discussions (with permission)
- Fireflies: Past transcripts

---

### 4. Populate from Direct Input

**Triggers:**
- "add an issue: [description]"
- "here's what we found: [bullet list]"
- User provides structured info in conversation

**Process:**
1. Parse user input into Issues/Solutions
2. Ask clarifying questions if needed (Department? Impact?)
3. Write to Excel
4. Present updated file

---

### 5. Migrate to Full Catalog

**Triggers:**
- "migrate this to Airtable"
- "convert to full catalog"
- "promote to catalog"

**Process:**
1. Read Excel file
2. Map fields to Airtable schema (see `lite-schema.md` mapping table)
3. Create records in dependency order:
   - Client (if not exists)
   - Session record
   - People (from quotes attribution)
   - Challenges (from Issues)
   - Solutions
4. Report created record counts
5. Offer to archive Excel

**Notes:**
- Impact Category → Challenge Type
- Pain Point Cause → Root Cause field
- Findings → Notes field (concatenated)
- No scoring in Lite → Set scores to 0, flag for manual review

---

## Output Guidelines

### When presenting filled Excel:
```
Here's your populated Discovery Catalog Lite:

**Summary:**
- Departments: 3 (Sales, Marketing, Product)
- Issues: 12 identified
- Solutions: 8 proposed

**Confidence notes:**
- High confidence: Issues from direct transcript quotes
- Medium: Solutions inferred from problem descriptions
- Low: Tech stack (needs validation)

[Download: discovery-catalog-acme-2024-12.xlsx]

Want me to migrate this to the full Airtable Catalog?
```

### When asking for missing info:
```
I've captured 8 issues but need more detail on:

1. **Department** for "Slow approval process" — which team owns this?
2. **Impact Category** for 3 issues — Revenue, Time, or Experience?
3. **Pain Point Quote** — any direct quotes from stakeholders?

Provide what you have and I'll update the template.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Template structure doesn't match | Ask user to use standard template |
| Department name mismatch | Flag and ask for correction |
| Solution referenced but not defined | Create placeholder in Solutions sheet |
| Missing required fields | Fill what's available, list gaps |
| Excel file corrupted | Offer to create fresh from extracted data |

---

## Integration with Other Modules

**cadre-os-synthesis:** Can run pattern analysis on Lite data (read Excel → analyze)

**cadre-os-deliverables:** Can generate decks/reports from Lite data

**cadre-os-context:** Does NOT query Lite files automatically (Excel is local, not indexed)

---

## Post-Call Workflow

Human + Claude workflow after each discovery call:

### 1. Download Transcript
- Get transcript from Fireflies (or transcription tool)
- Save to: `Cadre Team Drive / Clients / [Client Name] / Transcripts / [YYYY-MM-DD] [Type] - [Attendees].txt`

### 2. Create Claude Chat
- Open client's Claude Project
- Start new chat named: `[YYYY-MM-DD] Debrief - [Attendee(s)]`

### 3. Run Debrief
- Upload transcript
- (Optional) Add rough notes
- Type: `/debrief [Client Name] lite`

### 4. Review & Revise
- Claude shows Debrief Summary
- Human reviews, fixes errors, adds missing items
- Iterate until accurate

### 5. Save Debrief Summary
- Download artifact as `.md` file
- Save to: `Cadre Team Drive / Clients / [Client Name] / Discovery / Debriefs /`
- Upload to Claude Project Knowledge

### 6. Update Catalog
- Review Claude's catalog entries
- Open `Discovery Catalog.xlsx` from Drive
- Add new entries
- Re-upload to Claude Project Knowledge

### 7. Peer Review (Client-Facing Only)
If artifacts will be shown to client:
- Slack teammate for quick review (2-5 min)
- Make any final fixes

---

## Entity Extraction

### What to Extract

| Entity Type | Look For | Maps To |
|-------------|----------|---------|
| **Departments** | Team names, org units mentioned | Departments sheet |
| **Issues/Challenges** | Problems, pain points, complaints, blockers | Issues sheet |
| **Solutions** | Proposed fixes, opportunities, "we should..." statements | Solutions sheet |
| **Quotes** | Direct stakeholder statements in quotes | Issues → Pain Point Quote |
| **Root Causes** | "because...", "due to...", underlying reasons | Issues → Pain Point Cause |
| **Findings** | Data points, metrics, observations | Issues → Finding 1, 2, 3 |
| **Technology** | Tools, systems, platforms mentioned | Solutions → Tech columns |

### Extraction Patterns

**Issues/Challenges - look for:**
- "The problem is..."
- "We struggle with..."
- "It takes too long to..."
- "We're losing [money/time/customers] because..."
- Complaints, frustrations, blockers
- Negative sentiment about processes

**Solutions - look for:**
- "We could..."
- "What if we..."
- "I wish we had..."
- "Other companies use..."
- Proposed tools or approaches
- 💡 marker (unprompted client ideas = high value)

**Quotes - look for:**
- Text in quotation marks
- "As [Name] said..."
- Direct first-person statements from stakeholders
- Attribute with: "— [Name], [Title]" or "— [Role]"

**Root Causes - look for:**
- "because..."
- "due to..."
- "the reason is..."
- "this happens when..."
- Causal explanations

---

## Validation

Run these checks before writing to Excel:

1. **Check departments exist** for all issues/solutions
2. **Check solution references** in issues match Solutions sheet
3. **Check required fields** (name, description)
4. **Check impact category values** match valid options

**Valid Impact Categories:**
`New Revenue` | `Time Efficiency` | `Revenue Loss` | `Customer Experience` | `Competitive Position` | `Brand Awareness` | `Lead Quality` | `Brand Consistency` | `Product Quality` | `Strategic Decisions` | `Cost Reduction` | `Risk Mitigation` | `Employee Experience` | `Compliance`

**If errors exist:** Stop and ask user to clarify
**If only warnings:** Proceed but note warnings in output

---

## Writing to Excel

Use openpyxl to write extracted data. See `data/lite-schema.md` for field mapping.

**Sheet order and structure:**
1. **Departments** - Column A: Department Name, Column B: Hours Saved (optional)
2. **Issues** - Columns A-N with department, name, description, category, solution, quote, cause, findings
3. **Solutions** - Columns A-Q with department, name, description, impact, tech stack, data readiness

**Key rules:**
- Match department names exactly
- Solution references in Issues must exist in Solutions sheet
- Leave unknown fields blank (don't guess)
- Findings are numbered columns (Finding 1, Finding 2, etc.)

---

## Complete Workflow Example

**User:** "Debrief Acme Corp lite mode" + [pastes transcript]

**Claude's process:**

1. **Detect lite mode** — User said "lite mode"
2. **Load references** — Read `lite-mode.md` + `data/lite-schema.md`
3. **Extract entities** — Parse transcript for departments, issues, solutions, quotes
4. **Organize data** — Structure into dicts matching schema
5. **Validate** — Check department refs, solution refs, required fields
6. **Write to Excel** — Use openpyxl with schema field mapping
7. **Present** — Show summary with confidence notes and gaps
8. **Offer next steps** — Generate artifacts, comms, or migrate to Airtable

---

## Generate Artifacts

After populating the Lite template, offer to generate branded artifacts.

### When triggered

User says "create findings summary", "visualize the findings", "generate artifact", or asks "what's next?"

### Available Artifact

| Artifact | Template | What It Shows |
|----------|----------|---------------|
| Findings Summary | `findings-summary.html` | Issues + solutions side by side, quick wins, next steps |

### How It Works

The template contains **example data** (Acme Corp). Don't find-and-replace — instead:

1. **Read the template** to understand structure and CSS classes
2. **Load client data** from populated Lite Excel
3. **Generate fresh HTML** following the template's patterns
4. **Output as artifact** or save as file

See `synthesis/data-to-artifact.md` for detailed generation steps and CSS class reference.

### Output

After generating artifact:

```markdown
Here's your **Findings Summary** for {Client Name}:

**Highlights:**
- 8 issues identified (3 high-impact)
- 5 solutions proposed
- 2 quick wins ready for immediate action

[Download: findings-acme.html]

**Quick wins identified:**
1. AI Lead Enrichment — High impact, low effort
2. Meeting Notes Automation — High impact, low effort

**Next steps:**
- Present findings to stakeholders
- `/deck [client]` to generate full strategy deck
- `/roadmap [client]` to build implementation plan
```

---

## Offer Comms

After populating the catalog and generating artifacts:

> "Want me to draft the **follow-up email**? **Internal Slack summary**?"

**If follow-up email:** Generate client-facing email with:
- Thank you for the session
- Key topics discussed (high-level)
- Next steps and timeline
- Any action items for client

**If Slack summary:** Generate internal TL;DR:
- 2-3 sentence summary
- Key insights (with ⚡🔄💡 markers)
- Follow-up items
- Next session date if known
