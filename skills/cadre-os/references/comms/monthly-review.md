# Monthly Business Review (MBR) Skill

Generate professional Monthly Business Review presentations for Cadre clients using a structured workflow with quality gates and modular slide templates.

## When to Use

**Trigger phrases:**
- "Start MBR for [client] [month]"
- "Monthly review for [client]"
- "Create [month] business review"
- "MBR workflow for [client]"
- "[Client] monthly deck"

**This skill is for:**
- Preparing monthly client presentations
- Synthesizing engagement progress, wins, and challenges
- Facilitating strategic decisions with clients
- Documenting action items and next steps

---

## Workflow Overview

The MBR workflow has **four phases** with explicit approval gates:

```
Phase 1: RESEARCH      → kb.md (knowledge base)
Phase 2: STRUCTURE     → outline.md (deck structure)
Phase 3: CONTENT       → content.md (slide-by-slide content)
Phase 4: GENERATION    → [client]-[month]-[year]-review.pptx
```

### Artifact Naming Convention

All artifacts save to `/mnt/user-data/outputs/`:
- `{client}-{month}-{year}-kb.md`
- `{client}-{month}-{year}-outline.md`
- `{client}-{month}-{year}-content.md`
- `{client}-{month}-{year}-review.pptx`

**Example:** `ces-january-2026-kb.md`

---

## Phase 1: Research (kb.md)

### Step 1: Search Project Knowledge

Search the project knowledge base for all context on Month X:
- Meeting transcripts and intelligence docs
- Status updates and check-ins
- Deliverable documentation
- Previous month's MBR for continuity

### Step 2: Offer Additional Searches

Present specific, optimal searches for each available data source:

**Gmail:**
- "Search for: `subject:[client] after:[month-start] before:[month-end]`"
- "Search for: `from:[client-contacts] [key-topics]`"

**Fireflies:**
- "Search for meetings with [client] in [date range]"
- "Get transcript for [specific meeting]"

**Google Drive:**
- "Search for: `[client] [month] [deliverable-type]`"

### Step 3: Document Findings

Create `kb.md` with structured findings:

```markdown
# [Client] [Month] [Year] - Knowledge Base

## Engagement Context
- Current phase: [X] of [Y]
- Key stakeholders: [names/roles]
- Active workstreams: [list]

## This Month's Activity
### Meetings Held
- [Date]: [Meeting type] - [Key topics]

### Deliverables
- [Status]: [Deliverable name]

### Key Wins
1. [Win with specific metric/outcome]

### Challenges Encountered
1. [Challenge] - Root cause: [cause] - Status: [status]

### Decisions Made
- [Decision] - Impact: [impact]

### Open Questions
1. [Question requiring client input]

## Previous Month Reference
[Summary of last month's action items and their status]
```

### Step 4: Clarifying Questions

Ask clarifying questions using the standard format:
- Explain the question
- Provide viable answers with explanations
- State recommendation

**Loop until `kb.md` is approved.**

---

## Phase 2: Structure (outline.md)

### Step 5: Generate Outline Options

Present 2-3 outline options with different emphases:

**Option A: Progress-Heavy**
- Best when: Strong month with many wins to celebrate
- Emphasis: Multiple Progress slides, brief Challenges

**Option B: Decision-Focused**
- Best when: Key decisions needed from client
- Emphasis: Multiple Discussion slides, clear options

**Option C: Balanced**
- Best when: Typical month with mix of progress and challenges
- Emphasis: Even coverage across all sections

### Step 6: Present Template Visually

Show the user the template PPTX so they can see slide options:
- Present `cadre-mbr-template-full.pptx`
- Point to relevant variations for their content
- Ask "Which fits best?" at decision points

### Step 7: Select Variations

For each slide type, suggest the appropriate variation based on content:

| Content Situation | Suggested Variation |
|-------------------|---------------------|
| 1 major opportunity | Opps-B (Deep dive) |
| 2-3 opportunities | Opps-A (3-card) |
| 4+ smaller ideas | Opps-C (Menu) |
| Binary decision | Discussion-A (Two-option) |
| Clear recommendation | Discussion-B (Single rec) |
| Exploratory topic | Discussion-C (Open) |

**Loop until `outline.md` is approved.**

---

## Phase 3: Content (content.md)

### Step 8: Generate Slide Content

Create `content.md` with exact content for each slide:

```markdown
# Slide 1: Title-A
- Client Name: Contemporary Energy Solutions
- Period: January 2026
- Month: 5 of 7

# Slide 2: ExecSum-A
- Status: ON TRACK
- Win 1: Proposal automation processing 87% of parts
- Win 2: AI training completed for 25 employees
- Win 3: Labor rate calculator in UAT
- Challenge 1: Lead generation - 0.01% response rate
- Challenge 2: Adoption - 70% report zero time savings
- Key Decision: ZoomInfo contract renewal by Dec 17

# Slide 3: Progress-A (Proposal Automation)
[Continue with specific content for each slide...]
```

### Step 9: Content Guidelines

**Tone:**
- Professional but warm
- Specific with metrics where possible
- Action-oriented language
- Acknowledge challenges honestly

**Length:**
- Titles: 3-6 words
- Bullet points: 1 line each
- Descriptions: 1-2 sentences max
- Cards: 2-4 bullet points

**Metrics:**
- Lead with the number: "87% parts coverage" not "Coverage is at 87%"
- Include comparison: "Up from 60% last month"
- Quantify impact: "Saving 2 hours per proposal"

### Step 10: Clarifying Questions

Ask about content gaps, emphasis, and accuracy.

**Loop until `content.md` is approved.**

---

## Phase 4: Generation (PPTX)

### Step 11: Generate Presentation

Use the html2pptx workflow:
1. Extract html2pptx library
2. Copy template slides
3. Replace placeholder content with content.md values
4. Generate PPTX

### Step 12: Visual Validation

Convert to images and validate:
- No text cutoff
- Proper alignment
- Consistent spacing
- Readable contrast

### Step 13: Final Review

Present the deck and ask:
- Any content changes needed?
- Any slide additions/removals?
- Ready to deliver?

### Step 14: Appendix (Optional)

After generating, ask:
"Would you like me to include appendix slides with alternative variations?"

Only add if explicitly requested.

**Loop until PPTX is approved.**

---

## Slide Variation Catalog

### Section 1: Title
| Code | Name | Use When |
|------|------|----------|
| Title-A | Standard | Always (required) - centered layout |

### Section 2: Executive Summary
| Code | Name | Use When |
|------|------|----------|
| ExecSum-A | Standard | Default - Wins/Challenges/Key Decision layout |
| ExecSum-B | Metrics-Forward | Lead with 4 key metrics, then narrative summary |
| ExecSum-C | Minimal | Large typography, 3 wins + 1 challenge + 1 ask |

**Selection Logic:**
- Default to ExecSum-A for typical months with balanced content
- Use ExecSum-B when metrics tell a compelling story (strong numbers to highlight)
- Use ExecSum-C for executive audiences or when simplicity is key

### Section 3: AI Roadmap
| Code | Name | Use When |
|------|------|----------|
| Roadmap-A | Quarterly | 4-quarter view (Q1-Q4) with workstreams |
| Roadmap-B | Monthly | 5-month view with "Now" indicator line |
| Roadmap-C | Workstream | 3-month deep dive with phased tasks |

**Selection Logic:**
- Use Roadmap-A for strategic planning discussions (board-level, annual reviews)
- Use Roadmap-B for operational reviews showing current position in timeline
- Use Roadmap-C when diving deep into a specific initiative's phases

### Section 4: Progress & Wins
| Code | Name | Use When |
|------|------|----------|
| Progress-A | List + Metrics | Completed items with 3 key metrics |
| Progress-B | Metrics Grid | 2x2 metrics with status breakdown |
| Progress-C | Success Stories | Individual achievements to highlight |

### Section 5: Challenges & Plans
| Code | Name | Use When |
|------|------|----------|
| Challenges-A | Standard | Balanced challenge + root cause + actions + in-progress |
| Challenges-B | Decision Needed | Blocker requiring client input (two-column: blocker + ask) |
| Challenges-C | Status Update | FYI only, no action needed (Resolved + Monitoring lists) |

**Selection Logic:**
- Default to Challenges-A for standard challenges with mitigation plans
- Use Challenges-B when client decision or action is required to unblock
- Use Challenges-C for reporting on previously-raised issues (resolved or still monitoring)

### Section 6: Discussion
| Code | Name | Use When |
|------|------|----------|
| Discussion-A | Two-option | Binary decision with clear trade-offs |
| Discussion-B | Single rec | Clear recommendation needing buy-in |
| Discussion-C | Open | Exploratory topic, no pre-structured options |

### Section 7: Assets
| Code | Name | Use When |
|------|------|----------|
| Asset-A | Full-bleed | Screenshot/diagram needs maximum space |
| Asset-B | Asset + caption | Asset needs context explanation below |
| Asset-C | Asset + bullets | Explaining specific elements of the asset |

### Section 8: Links
| Code | Name | Use When |
|------|------|----------|
| Link-A | Centered | Simple resource sharing |
| Link-B | Link + bullets + asset | Resource with preview and feature list |

### Section 9: Opportunities
| Code | Name | Use When |
|------|------|----------|
| Opps-A | 3-card | Standard 2-3 opportunities (Problem/Solution) |
| Opps-B | Deep dive | One major opportunity worth detailed explanation |
| Opps-C | Menu | 4-6 smaller ideas to surface |

**Selection Logic:**
- Count-based default: 1→Opps-B, 2-3→Opps-A, 4+→Opps-C
- Importance override: If opportunity is significant ($15K+), suggest Opps-B regardless of count

### Section 10: Feedback
| Code | Name | Use When |
|------|------|----------|
| Feedback-A | Open space | "Let's discuss X" moment |
| Feedback-B | Category boxes | Structured feedback on specific areas |

### Section 11: Scorecard
| Code | Name | Use When |
|------|------|----------|
| Scorecard-A | Standard | Success metrics + retrospective |

### Section 12: Looking Ahead
| Code | Name | Use When |
|------|------|----------|
| Ahead-A | Standard | Timeline + priorities + key dates |

### Section 13: Action Items
| Code | Name | Use When |
|------|------|----------|
| Actions-A | Standard | Two-column (Client + Cadre) checklist |

---

## Standard MBR Structure

A typical MBR follows this flow (adjust based on content):

1. **Title** (1 slide)
2. **Executive Summary** (1-3 slides - pick variation based on audience)
3. **AI Roadmap** (0-3 slides - include when discussing timeline/phases)
4. **Progress & Wins** (1-3 slides per workstream)
5. **Challenges & Plans** (1-2 slides)
6. **Discussion** (0-2 slides if decisions needed)
7. **Assets/Links** (0-3 slides as needed)
8. **Opportunities** (0-1 slide)
9. **Feedback** (0-1 slide)
10. **Scorecard** (0-1 slide)
11. **Looking Ahead** (1 slide)
12. **Action Items** (1 slide)

**Typical total: 8-18 slides**

---

## Question-Asking Protocol

Throughout the workflow, ask clarifying questions using this format:

```markdown
### Question: [Brief question title]

**Why this matters:** [1 sentence explaining the question's importance]

**Options:**

**A. [Option name]**
- [Description]
- *Best when:* [Scenario]

**B. [Option name]**
- [Description]
- *Best when:* [Scenario]

**C. [Option name]**
- [Description]
- *Best when:* [Scenario]

**My recommendation:** [Option] because [brief rationale]
```

---

## Template File

The modular template is stored at:
`mbr-template-01-07-25.pptx`

**Structure:**
- 13 section dividers (gray background, self-documenting)
- 29 slide variations (warm white background, pure placeholders)
- Total: 42 slides

**New in this version (January 2025):**
- Executive Summary variations (ExecSum-B Metrics-Forward, ExecSum-C Minimal)
- AI Roadmap section with 3 variations (Quarterly, Monthly, Workstream)
- Centered title slide text

**Slide Order:**
1. Title Section → Title Slide
2. Executive Summary Section → ExecSum-A, ExecSum-B, ExecSum-C
3. AI Roadmap Section → Roadmap-A, Roadmap-B, Roadmap-C
4. Progress & Wins Section → Progress-A, Progress-B, Progress-C
5. Challenges & Plans Section → Challenges-A, Challenges-B, Challenges-C
6. Discussion Section → Discussion-A, Discussion-B, Discussion-C
7. Assets Section → Asset-A, Asset-B, Asset-C
8. Links Section → Link-A, Link-B
9. Opportunities Section → Opps-A, Opps-B, Opps-C
10. Feedback Section → Feedback-A, Feedback-B
11. Scorecard Section → Scorecard-A
12. Looking Ahead Section → Ahead-A
13. Action Items Section → Actions-A

**To use:**
1. Present template to user with `present_files` tool
2. Reference slide numbers when discussing options
3. Generate final deck by selecting appropriate variations

---

## Continuity Best Practices

**Reference previous months:**
- Check last month's action items → report status
- Note progress on multi-month initiatives
- Acknowledge resolved challenges from prior months

**Maintain relationship context:**
- Use client's preferred terminology
- Reference key stakeholders by name
- Acknowledge organizational dynamics (e.g., family business)

**Track engagement health:**
- Adoption metrics over time
- ROI evidence accumulation
- Relationship temperature indicators
