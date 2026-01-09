# Brain Update Generator

Generate formatted documents for updating Client Brains after discovery sessions.

## Contents

1. [When to Use](#when-to-use)
2. [Execution Flow](#execution-flow)
3. [Brain Section Mapping](#brain-section-mapping)
4. [Parsing the Current Brain](#parsing-the-current-brain)
5. [Generating the Update Document](#generating-the-update-document)
6. [Document Template](#document-template)

---

## When to Use

After completing a debrief (Steps 1-7), generate a Brain Update document when:
- New stakeholder insights were captured
- Relationship dynamics changed
- Decisions were made
- New preferences/patterns were learned
- Any information belongs in the narrative Brain (not just structured Catalog)

**The Brain Update doc makes it easy to copy/paste into the Client Brain Google Doc.**

---

## Execution Flow

### Step 8A: Fetch Current Brain

The Brain Link was captured during Pre-flight Check (Step 0B). Now fetch the actual content:

```
Google Drive MCP: google_drive_fetch
Document ID: [extracted from Brain Link URL]
```

**Extracting Document ID from Brain Link:**
```
URL: https://docs.google.com/document/d/1ABC123xyz/edit
Document ID: 1ABC123xyz
```

If Brain Link is empty or fetch fails:
- Note: "No existing Brain found - all entries will be NEW"
- Continue with generation (treat everything as NEW)

### Step 8B: Parse Brain into Sections

Extract current state from each Brain section:

```
CURRENT_BRAIN = {
  "stakeholders": {
    "Karl Winters": {
      "title": "CFO",
      "role_type": "Economic Buyer",
      "power": 9,
      "sentiment": 5,
      "notes": "Conservative, data-driven"
    },
    ...
  },
  "relationship_health": {
    "score": 7,
    "trend": "improving",
    "last_contact": "2024-11-15"
  },
  "active_context": {
    "phase": "Discovery",
    "blockers": ["IT bandwidth", "Budget approval pending"],
    "open_questions": ["Timeline for Phase 2?"],
    "whats_working": ["Direct communication"],
    "whats_not": ["Long email chains"]
  },
  "decisions": [
    {"date": "2024-11-01", "decision": "Proceed with discovery", "made_by": "Karl"}
  ],
  "preferences": {
    "communication": ["Prefers Slack over email"],
    "meetings": ["Morning meetings preferred"],
    "avoid": ["Don't surprise in large meetings"]
  }
}
```

### Step 8C: Compare to Debrief Findings

For each extracted insight from the debrief, categorize:

| Category | Criteria | Action |
|----------|----------|--------|
| **NEW** | Entity/item not in current Brain | Add with full details |
| **UPDATE** | Entity exists, values changed | Show old → new |
| **CONFIRM** | Entity exists, might need update (low confidence) | Flag for review |
| **SKIP** | Already captured accurately | Don't include |

**Comparison Logic:**

```
For each PERSON from debrief:
  IF name NOT IN current_brain.stakeholders:
    → NEW
  ELSE:
    old = current_brain.stakeholders[name]
    IF sentiment changed OR power changed OR role changed:
      → UPDATE (show diff)
    ELSE IF new notes/insights:
      → UPDATE (append notes)
    ELSE:
      → SKIP

For each DECISION from debrief:
  IF decision NOT IN current_brain.decisions (fuzzy match):
    → NEW
  ELSE:
    → SKIP

For each PREFERENCE/PATTERN learned:
  IF not already in preferences section:
    → NEW
  ELSE:
    → SKIP
```

### Step 8D: Generate Update Document

Use the docx skill to create a formatted Word document:

```
Read: /mnt/skills/public/docx/SKILL.md
```

Generate the document using the template below.

---

## Brain Section Mapping

Map debrief findings to Brain sections:

| Debrief Finding | Brain Section | Format |
|-----------------|---------------|--------|
| Person with Power/Sentiment | 2. Stakeholder Map | Table row |
| Person insights/concerns | 2. Stakeholder Map (Notes column) | Bullet points |
| Relationship observation | 3. Relationship Health | Paragraph with date |
| Current blocker | 4. Active Context → Blockers | Bullet point |
| Open question | 4. Active Context → Open Questions | Bullet point |
| Win/progress | 4. Active Context → Recent Wins | Bullet with date |
| Decision made | 5. Key Decisions Log | Table row |
| Communication preference | 6. Preferences → Communication | Bullet point |
| Meeting preference | 6. Preferences → Meetings | Bullet point |
| Thing that works | 6. Preferences → Things that work | Bullet point |
| Thing to avoid | 6. Preferences → Things to avoid | Bullet point |

---

## Parsing the Current Brain

### Section Detection

Look for these headers in the Brain document:

```
"Client Overview" or "## Client Overview" → Section 1
"Stakeholder Map" or "## Stakeholder Map" → Section 2
"Relationship Health" or "## Relationship Health" → Section 3
"Active Context" or "## Active Context" → Section 4
"Key Decisions" or "## Key Decisions" → Section 5
"Preferences" or "## Preferences" → Section 6
"Update Log" or "## Update Log" → Section 7
```

### Stakeholder Table Parsing

The Stakeholder Map typically has a table format:

```
| Name | Title | Role Type | Power | Sentiment | Notes |
|------|-------|-----------|-------|-----------|-------|
| Karl Winters | CFO | Economic Buyer | 9 | 5 | Conservative... |
```

Extract into structured format for comparison.

### Handling Variations

Brains may have slight variations in structure. Be flexible:
- Headers might be `##` or `###` or bold text
- Tables might use `|` or be formatted lists
- Sections might be in different order

If parsing fails for a section, note it and treat those items as potentially NEW.

---

## Generating the Update Document

### Document Structure

```
┌─────────────────────────────────────────────────────────────┐
│  BRAIN UPDATE                                               │
│  Client: [Client Name]                                      │
│  Session: [Session Title]                                   │
│  Date: [Date]                                               │
│  Generated: [Timestamp]                                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INSTRUCTIONS                                               │
│  1. Open the Client Brain Google Doc                        │
│  2. Navigate to each section listed below                   │
│  3. Copy/paste the updates into the appropriate location    │
│  4. Delete this document when done                          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📍 SECTION 2: STAKEHOLDER MAP                              │
│  ─────────────────────────────                              │
│                                                             │
│  [Content organized by NEW → UPDATE → CONFIRM]              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📍 SECTION 3: RELATIONSHIP HEALTH                          │
│  ─────────────────────────────────                          │
│                                                             │
│  [Content]                                                  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  ... [Additional sections as needed] ...                    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  📍 SECTION 7: UPDATE LOG                                   │
│  ────────────────────────                                   │
│                                                             │
│  ADD THIS ENTRY:                                            │
│  [Date] - [Session Type]: [Brief summary of what changed]   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Formatting by Category

**NEW entries:**
```
🆕 NEW: [Name/Item]
━━━━━━━━━━━━━━━━━━
[Full details to add]
```

**UPDATE entries:**
```
✏️ UPDATE: [Name/Item]
━━━━━━━━━━━━━━━━━━━━━
• [Field]: [Old Value] → [New Value]
• [Field]: [Old Value] → [New Value]
• Add to Notes: [New information]
```

**CONFIRM entries (low confidence):**
```
❓ CONFIRM: [Name/Item]
━━━━━━━━━━━━━━━━━━━━━━
Current: [What's in Brain]
Heard in session: [What was said]
→ Update needed? [Suggested action]
```

---

## Document Template

### Section: Stakeholder Map

```
📍 SECTION 2: STAKEHOLDER MAP
─────────────────────────────

🆕 NEW: Sarah Chen
━━━━━━━━━━━━━━━━━━
Add this row to the Stakeholder Map table:

| Name | Title | Role Type | Power | Sentiment | Notes |
|------|-------|-----------|-------|-----------|-------|
| Sarah Chen | Controller | Influencer | 6 | 5 | Reports to Karl. Owns month-end close. Cautious about change but open to pilots. |


✏️ UPDATE: Karl Winters
━━━━━━━━━━━━━━━━━━━━━━━━
Find Karl Winters in the table and update:

• Sentiment: 5 → 8  (volunteered to champion AI pilot)
• Add to Notes: "Now acting as interim COO. Increasingly bought-in to AI transformation."
```

### Section: Relationship Health

```
📍 SECTION 3: RELATIONSHIP HEALTH
─────────────────────────────────

APPEND to the relationship narrative:

[2024-12-01] Strong session. Karl has evolved from cautious supporter 
to active champion - volunteered to personally sponsor the AI pilot 
before we even asked. Relationship trending positive. 
Score recommendation: 7 → 8.
```

### Section: Key Decisions

```
📍 SECTION 5: KEY DECISIONS LOG
───────────────────────────────

🆕 ADD this row to the decisions table:

| Date | Decision | Made By | Rationale |
|------|----------|---------|-----------|
| 2024-12-01 | Approved AI pilot for month-end close | Karl Winters | "Let's prove the value quickly with a contained scope" |
```

### Section: Preferences

```
📍 SECTION 6: PREFERENCES & PATTERNS
────────────────────────────────────

🆕 ADD to "Things that work well":
• Lead with ROI numbers - Karl responds well to concrete financial impact
• Keep slides minimal - he prefers discussion over presentation

🆕 ADD to "Things to avoid":
• Don't schedule meetings after 4pm - he has hard stop for family
```

### Section: Update Log

```
📍 SECTION 7: UPDATE LOG
────────────────────────

ADD this entry at the top:

[2024-12-01] Interview with Karl Winters: 
Updated stakeholder sentiment (Karl 5→8), added new stakeholder (Sarah Chen), 
logged AI pilot decision. See Discovery Catalog session ID: recXXXXX.
```

---

## Output Delivery

After generating the document:

1. Save to `/mnt/user-data/outputs/[Client]-brain-update-[Date].docx`
2. Provide download link to user
3. Summarize what's in the update:
   - X new stakeholders
   - Y stakeholder updates
   - Z decisions logged
   - N preferences captured

**Example response:**

```
Brain Update document generated:

[Download: CES Brain Update 2024-12-01](computer:///mnt/user-data/outputs/CES-brain-update-2024-12-01.docx)

**Summary:**
• 1 new stakeholder (Sarah Chen)
• 1 stakeholder update (Karl Winters - sentiment 5→8)
• 1 decision logged (AI pilot approved)
• 2 new preferences captured

Open your CES Brain Google Doc and copy/paste from each section.
```

---

## Error Handling

| Situation | Response |
|-----------|----------|
| Brain Link missing | Generate doc with all items as NEW, note "No existing Brain found" |
| Brain fetch fails | Generate doc with all items as NEW, note "Could not access Brain" |
| Brain parse fails | Generate doc with all items as NEW/CONFIRM, note parsing issue |
| No updates needed | Skip document generation, note "No Brain updates needed from this session" |
| Only Catalog updates | Note "All findings captured in Discovery Catalog - no narrative Brain updates needed" |
