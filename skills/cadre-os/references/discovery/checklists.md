# Quality Checklists

Pre-delivery quality checks for prep and debrief outputs.

---

## Prep Quality Checklist

### Quick Prep (2-5 min)

Before delivering briefing, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Mode explained to user | ✓ |
| 2 | Attendee names and titles included | ✓ |
| 3 | Session type confirmed | ✓ |
| 4 | Key context from Brain/Catalog present | ✓ |
| 5 | Questions target known gaps | ✓ |
| 6 | Questions scaled to duration | ✓ |
| 7 | Questions in plain English | ✓ |
| 8 | Handoff prompt included | ✓ |

**Quick Prep Minimum:**
- [ ] 3+ questions included
- [ ] At least 1 attendee profiled
- [ ] Session goal clear

---

### Deep Prep (10-15 min)

Before delivering briefing, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Mode explained to user | ✓ |
| 2 | All attendees profiled (name, title, background) | ✓ |
| 3 | Research phases completed or stopped appropriately | ✓ |
| 4 | Permissions requested before external research | ✓ |
| 5 | Time limits respected (≤10 min research) | ✓ |
| 6 | Questions target dimension gaps | ✓ |
| 7 | Questions match attendee roles | ✓ |
| 8 | Question count matches duration | ✓ |
| 9 | Conditional follow-ups included | ✓ |
| 10 | Proper sequencing (Landscape → Problems → Process → Specifics) | ✓ |
| 11 | Landmines/sensitive topics flagged | ✓ |
| 12 | Rapport topics identified | ✓ |
| 13 | Handoff prompt included | ✓ |

**Deep Prep Minimum:**
- [ ] All attendees have profile
- [ ] 8+ questions with follow-ups
- [ ] Gap analysis documented
- [ ] Research documented (even if minimal)

---

## Debrief Quality Checklist

### Quick Debrief (3-5 min)

Before delivering summary, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Mode explained to user | ✓ |
| 2 | TL;DR is ≤3 sentences | ✓ |
| 3 | Key takeaways have confidence levels | ✓ |
| 4 | Notable quotes captured (if any) | ✓ |
| 5 | Insight markers applied (⚡🔄⚠️💡) | ✓ |
| 6 | Quick assessment table included | ✓ |
| 7 | Full Debrief suggestion offered (if substantial content) | ✓ |
| 8 | Handoff prompt included | ✓ |

**Quick Debrief Confirms:**
- [ ] NO records created (display only)
- [ ] User knows records not saved

---

### Full Debrief (10-15 min)

Before saving to Catalog, verify:

| # | Check | Required |
|---|-------|----------|
| 1 | Pre-flight check passed (8 tables loaded) | ✓ |
| 2 | Client ID confirmed | ✓ |
| 3 | Session type confirmed with user | ✓ |
| 4 | Attendees confirmed with user | ✓ |
| 5 | All 5 dimensions extracted | ✓ |
| 6 | Quotes extracted (3-5 minimum for 60min) | ✓ |
| 7 | Insight markers applied | ✓ |
| 8 | Confirmation summary shown | ✓ |
| 9 | User confirmed (or revised) | ✓ |
| 10 | Records created in order | ✓ |
| 11 | Brain Update offered | ✓ |
| 12 | Handoff prompt included | ✓ |

---

## Pre-Save Checklist

### Before Creating Any Catalog Records

| # | Check | If Failed |
|---|-------|-----------|
| 1 | All 8 table schemas loaded | Stop, reload |
| 2 | Client record exists | Stop, create client first |
| 3 | Entity maps built (existing records) | May create duplicates |
| 4 | Session record exists or will be created first | Link will fail |
| 5 | Required fields populated | Save will fail |
| 6 | Select field values match schema exactly | Save will fail |
| 7 | Link fields use record IDs (not names) | Link will fail |

### Field Validation

| Field Type | Validation |
|------------|------------|
| singleSelect | Value must match schema options exactly |
| multipleRecordLinks | Must be array of record IDs |
| number | Must be numeric (no strings) |
| checkbox | Must be boolean |
| date | Must be ISO format (YYYY-MM-DD) |

---

## Record Creation Order

Always create records in this sequence:

```
1. Session (1_Discovery_Log) — get session ID
2. People (2_People) — link to Session
3. Processes (3_Process) — link to Session, People
4. Technology (4_Technology) — link to Session
5. Challenges (5_Challenges) — link to Session, People, Process, Tech
6. Solutions (6_Solutions) — link to Session, Challenges
7. Quotes (7_Quotes) — link to all above
8. Update Session — add links to all created records
```

**Why This Order:**
- Session must exist before anything links to it
- People often linked from other records
- Challenges often link to Process/Tech
- Solutions often link to Challenges
- Quotes link to everything

---

## Output Quality Checks

### Briefing Output (Prep)

| Section | Check |
|---------|-------|
| Quick Context | ≤3 sentences |
| Attendee Profiles | Name, title, background, rapport topic |
| Key Questions | Numbered, scaled to duration |
| Follow-ups | Nested under relevant questions |
| Landmines | Sensitive topics flagged |
| Handoff | One-line, not pushy |

### Summary Output (Debrief)

| Section | Check |
|---------|-------|
| TL;DR | ≤3 sentences |
| Key Takeaways | 3-5 bullets, insight markers applied |
| Powerful Quotes | Attribution, type, power rating |
| Extracted Entities | Organized by dimension |
| Follow-Up Items | Actionable, assigned if possible |

---

## Error Recovery Checklist

### If Catalog Save Fails

| Step | Action |
|------|--------|
| 1 | Note which records failed |
| 2 | Output JSON for manual entry |
| 3 | Continue with remaining workflow |
| 4 | Offer Brain Update despite failure |
| 5 | Document what needs manual follow-up |

### If Schema Mismatch

| Step | Action |
|------|--------|
| 1 | Check field name spelling |
| 2 | Check select option exact match |
| 3 | Check field ID vs field name |
| 4 | Output corrected JSON if fixable |
| 5 | Flag for schema refresh if needed |

---

## Quality Signals

### Good Debrief Indicators

- [ ] 3+ insight markers applied
- [ ] 5+ quotes captured (for 60min session)
- [ ] All 5 dimensions have content
- [ ] At least 1 ⚡ Surprise or 💡 Opportunity
- [ ] Entity counts feel proportional to session length

### Warning Signs

- 0 insight markers → Review for missed patterns
- <3 quotes from 60min session → Transcript quality issue?
- 0 entities in a dimension → Dimension not covered in session
- Many ⚠️ Contradictions → May need follow-up before saves
- Session feels thin → Consider Quick Debrief instead

---

## Handoff Prompts

### After Prep

```
After your call, say "debrief [client]" and paste your notes.
```

### After Full Debrief

```
Want me to run gap analysis or prioritize challenges?
```

### After Quick Debrief

```
Ready for Full Debrief to save to Catalog? Or want me to prep for your next session?
```
