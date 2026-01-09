# Discovery Catalog SOP

How Cadre captures, organizes, and maintains client discovery findings.

---

## What is the Discovery Catalog?

A structured database of everything learned during client discovery: stakeholders, issues, solutions, and quick wins. It's the single source of truth that feeds all deliverables (decks, reports, roadmaps).

**Two formats:**
- **Lite (Excel)** — Default for most engagements. Simple, portable, no setup required.
- **Full (Airtable)** — For longer engagements or when clients want visibility.

---

## Step-by-Step Instructions

### Part A: Creating the Catalog

#### Step A1: Trigger
**When:** SOW is signed OR first discovery call is scheduled (whichever comes first)

**Who:** AI Manager or whoever is leading the engagement

#### Step A2: Get the Template

**Option 1 — From Claude (preferred):**
1. Open Claude
2. Type: `/lite template`
3. Claude generates the Discovery Catalog Lite Excel file
4. Download the file

**Option 2 — From Google Drive (backup):**
1. Go to: `Cadre Team Drive / Templates / Discovery Catalog Lite Template.xlsx`
2. Download or make a copy

#### Step A3: Save to Client Folder
1. Go to: `Cadre Team Drive / Clients / [Client Name] /`
2. If folder doesn't exist, create it
3. Save file as: `Discovery Catalog.xlsx` (no date stamp — it's a living doc)

#### Step A4: Link in Project Tracker
1. Open the client's ClickUp project (or wherever you track projects)
2. Add a link to the Discovery Catalog file
3. This ensures anyone on the project can find it without asking

#### Step A5: Upload to Claude Project
1. Open the client's Claude Project
2. Go to Project Knowledge
3. Upload the empty `Discovery Catalog.xlsx`
4. Claude now knows the catalog exists and can reference/update it

**Done.** Catalog is created and ready for population.

---

### Part B: Populating the Catalog (Post-Call Workflow)

This happens after every discovery call.

#### Step B1: Download Transcript
**When:** As soon as transcript is available (usually same day or next morning)

1. Go to Fireflies (or your transcription tool)
2. Find the call recording
3. Download the transcript
4. Save to: `Cadre Team Drive / Clients / [Client Name] / Transcripts / [YYYY-MM-DD] [Call Type] - [Attendees].txt`

**Example filename:** `2024-12-30 Discovery Interview - Sarah Chen.txt`

#### Step B2: Create New Claude Chat
1. Open the client's Claude Project
2. Start a new chat
3. Name it: `[YYYY-MM-DD] Debrief - [Attendee(s)]`

**Example chat name:** `2024-12-30 Debrief - Sarah Chen`

#### Step B3: Upload and Run Debrief
1. Upload the transcript file to the chat
2. (Optional) Add any rough notes you took during the call
3. Type: `/debrief [Client Name] lite`

**Example:** `/debrief Acme Corp lite`

#### Step B4: Review Debrief Summary
Claude generates a Debrief Summary artifact containing:
- TL;DR (3-4 sentences)
- Key Takeaways
- Powerful Quotes
- Extracted Entities (People, Processes, Technology, Challenges, Solutions)
- Follow-Up Items

**Your job:**
1. Read through the summary
2. Fix any errors (Claude may have misheard names, misunderstood context)
3. Add anything Claude missed
4. Remove anything irrelevant

#### Step B5: Save Debrief Summary
1. Download the Debrief Summary artifact as `.md` file
2. Save to: `Cadre Team Drive / Clients / [Client Name] / Discovery / Debriefs / [YYYY-MM-DD] Debrief - [Attendees].md`
3. Upload the saved file to Claude Project Knowledge

**Why both Drive and Claude?** Drive is your backup/archive. Claude Project Knowledge lets Claude reference it in future chats.

#### Step B6: Review Catalog Entries
Claude generates catalog entries for the Discovery Catalog Lite.

**Your job:**
1. Review each entry
2. Check the four required fields are filled:
   - Name (what is it?)
   - Description (one sentence explanation)
   - Source (who said it?)
   - Dimension (People, Process, Technology, Data, or General)
3. Fix any errors
4. Approve or revise

#### Step B7: Update the Catalog
1. Open `Discovery Catalog.xlsx` from the client's Drive folder
2. Add the new entries from Claude
3. Save the file
4. Re-upload updated file to Claude Project Knowledge (replace the old version)

#### Step B8: Optional — Generate Comms
Claude will ask: "Want me to draft the follow-up email? Internal Slack summary?"

**If yes:**
- Claude generates a follow-up email draft → Copy, paste into email, edit, send to client
- Claude generates Slack TL;DR → Copy, paste into internal Slack channel

**If no:** You're done.

---

### Part C: Migrating from Lite to Airtable

**When:** Engagement extends beyond initial scope OR client requests shared visibility

#### Step C1: Run Migration Command
1. Open Claude (client project)
2. Type: `/lite migrate [Client Name]`
3. Claude reads the Excel file and creates Airtable records

#### Step C2: Migration Review (30 minutes)
1. Open Airtable
2. Check for duplicates (Claude may have created entries that already exist)
3. Consolidate similar entries
4. Fix any extraction errors that accumulated in Lite
5. Verify all fields populated correctly

**Add "Migration Review" to your engagement extension checklist.**

---

### Part D: Quality Check Before Deliverables

**When:** Before generating any major deliverable (deck, report, roadmap)

#### Step D1: Run Catalog Audit
1. Open Claude (client project)
2. Type: `Audit the [Client Name] catalog before I create the [deliverable type]`

**Example:** `Audit the Acme Corp catalog before I create the strategy deck`

Claude checks for:
- Missing required fields
- Potential duplicates
- Conflicting information
- Issues without linked solutions
- Solutions without linked issues

#### Step D2: Review Flagged Items
1. Claude outputs a list of issues
2. Spend 15-20 minutes resolving them
3. Update the catalog with fixes

**Don't skip this.** Garbage in, garbage out.

---

### Part E: Generating Artifacts

**When:** Before client presentations, deliverable deadlines, or anytime someone needs a visual summary of findings.

#### Step E1: Ensure Data is Ready
1. Open the client's Claude Project
2. Confirm `Discovery Catalog.xlsx` is uploaded to Project Knowledge
3. If catalog was recently updated, re-upload the latest version

#### Step E2: Generate Findings Summary
1. In Claude, type: `/artifact findings [Client Name]`
2. Claude generates an HTML artifact showing:
   - Summary stats (issues, solutions, quick wins)
   - Issues and solutions side-by-side
   - Quick wins highlighted
   - Coverage by dimension
   - Recommended next steps

#### Step E3: Review and Revise
1. Review the artifact for accuracy
2. If something's wrong, tell Claude what to fix:
   - "Change the client name to Acme Corporation"
   - "The quick win about lead enrichment should be removed"
   - "Add a note that the CRM issue is high priority"
3. Claude revises the artifact
4. Repeat until it looks right

#### Step E4: Peer Review (Client-Facing Only)
If this artifact is going in front of the client:
1. Slack a teammate: "Quick review? [link to artifact]"
2. They spend 2-5 minutes checking for errors
3. Make any final fixes

*Skip this step for internal-only use.*

#### Step E5: Publish and Share
1. Click "Publish" on the artifact in Claude
2. Copy the shareable link
3. Use this link when presenting to client or sharing internally

#### Step E6: Add to Client Portal
1. Copy the HTML code from the artifact
2. Open the Client Portal
3. Navigate to the client's space
4. Paste the HTML into the code editor
5. Save

**Note:** If Claude generated JSX instead of HTML, ask: "Convert this to HTML for the Client Portal."

---

## Key Rules

### What Goes In the Catalog

**The test:** "Could this influence a recommendation?"

| Goes In | Stays in Notes |
|---------|----------------|
| Pain points that could become solutions | Small talk |
| Stakeholder opinions affecting buy-in | Background "nice to know" |
| Tool/process complaints | Off-topic tangents |
| Political dynamics | Overly granular details |
| Constraints (budget, timeline, resources) | — |

### Minimum Viable Entry

Every entry must have these four fields:

| Field | Example |
|-------|---------|
| Name | "CRM adoption resistance" |
| Description | "Sales team avoiding CRM; entering data in spreadsheets instead" |
| Source | "John Smith, VP Sales" |
| Dimension | "Technology" |

### Handling Conflicts

When stakeholders disagree, create **one entry** and note the conflict:

```
Name: CRM effectiveness disputed
Description: VP Sales says it's fine, needs training. Director of Ops says 
it's a nightmare, doesn't match workflow.
Source: VP Sales (pro), Director of Ops (con)
Dimension: Technology
```

### Entry Status

Never delete entries. Use status instead:

| Status | When to Use |
|--------|-------------|
| Active | Currently relevant (default) |
| Resolved | Issue addressed or solution implemented |
| Deprioritized | Client decided not to pursue |

### Client Access

**Catalog is internal only.** Clients see polished "What We Heard" summaries, not raw catalog.

---

## Naming Conventions

| Item | Format | Example |
|------|--------|---------|
| Catalog file | `Discovery Catalog.xlsx` | `Discovery Catalog.xlsx` |
| Transcript file | `[YYYY-MM-DD] [Type] - [Attendees].txt` | `2024-12-30 Discovery Interview - Sarah Chen.txt` |
| Debrief file | `[YYYY-MM-DD] Debrief - [Attendees].md` | `2024-12-30 Debrief - Sarah Chen.md` |
| Claude chat | `[YYYY-MM-DD] Debrief - [Attendees]` | `2024-12-30 Debrief - Sarah Chen` |

---

## Folder Structure

```
Cadre Team Drive /
└── Clients /
    └── [Client Name] /
        ├── Discovery Catalog.xlsx
        ├── Transcripts /
        │   └── [YYYY-MM-DD] [Type] - [Attendees].txt
        └── Discovery /
            └── Debriefs /
                └── [YYYY-MM-DD] Debrief - [Attendees].md
```

---

## Quick Reference

| Question | Answer |
|----------|--------|
| When to create? | SOW signed or first discovery call scheduled |
| When to populate? | After each call (same day or next morning) |
| Who populates? | Claude drafts, human reviews |
| Lite or Airtable? | Default Lite, migrate if engagement extends |
| What goes in? | If it could influence a recommendation |
| Minimum entry? | Name + description + source + dimension |
| Conflicting info? | One entry, note the conflict |
| Client access? | Internal only; synthesize for client |
| Old entries? | Status field, never delete |
| Before deliverables? | Claude audit + human review |

---

## Commands Reference

| Command | What It Does |
|---------|--------------|
| `/lite template` | Get blank Discovery Catalog Lite Excel |
| `/debrief [client] lite` | Run debrief, output for Excel |
| `/debrief [client] full` | Run debrief, write to Airtable |
| `/lite migrate [client]` | Migrate Excel data to Airtable |
| `/artifact findings [client]` | Generate Findings Summary HTML |
