# Special Scenarios

Handling edge cases in discovery prep and debrief.

---

## Multiple Attendees

### Prep Considerations

**Question Allocation:**
| Attendees | Approach |
|-----------|----------|
| 2-3 people | Prepare questions for each, but expect organic flow |
| 4-6 people | Prepare 2-3 targeted questions per person |
| 7+ people | Workshop format — group questions, not individual |

**Briefing Format Adjustment:**
```markdown
## Attendee Profiles (Multiple)

### [Name 1] — [Title] (Primary)
- Background: [key context]
- Priority questions: [2-3 specific to them]
- Rapport: [connection point]

### [Name 2] — [Title]
- Background: [key context]
- Priority questions: [2-3 specific to them]
- Rapport: [connection point]

### [Name 3] — [Title]
- Background: [key context]
- Priority questions: [2-3 specific to them]
- Rapport: [connection point]
```

**Dynamic Navigation Tips:**
- Start with most senior person (sets tone)
- Use names when redirecting: "Sarah, you mentioned..."
- Watch for quiet attendees — invite them in
- Note who defers to whom (reveals dynamics)

### Debrief Considerations

**Entity Attribution:**
- Tag quotes to specific speakers
- Note sentiment per person (may differ)
- Capture interpersonal dynamics observed

**Conflicting Information:**
- When attendees disagree, capture both views
- Mark as ⚠️ Contradiction
- Note which person said what
- Don't resolve — flag for follow-up

---

## Follow-Up Sessions

### What Changes

Follow-up sessions differ from initial discovery:
- Context already exists
- Skip Landscape layer (unless new topic)
- Go deeper on Problems/Specifics
- Validate prior findings

### Prep Adjustments

**Before:**
1. Review prior session notes
2. Check Catalog for this client's records
3. Identify what was learned vs. still unknown
4. Focus questions on gaps

**Briefing Format:**
```markdown
## Session Context

**Prior Session:** [Date] — [Type] — [Key takeaways]

**What We Learned:**
- [Confirmed fact 1]
- [Confirmed fact 2]

**What We Still Need:**
- [ ] [Gap 1] — priority question
- [ ] [Gap 2] — priority question

**Follow-Up Questions:**
1. "Last time you mentioned [X]. Has anything changed?"
2. "We want to dig deeper on [Y]. Can you walk me through..."
3. "You mentioned [Z] was a challenge. What's happened since?"
```

### Debrief Adjustments

**Update vs. Create:**
- Check if People/Process/Technology records exist
- UPDATE existing records (add to notes, adjust scores)
- Only CREATE if truly new entity
- Use Change History format for updates

**Change History Entry:**
```
[YYYY-MM-DD | Session: Follow-up with Sarah] 
Updated AI Readiness: 2 → 3 (pilot completed successfully)
```

---

## Scope Changes

### Mid-Engagement Pivot

When client priorities shift during engagement:

**Detection Signals:**
- New stakeholder introduces different priority
- Original sponsor's focus has changed
- External event shifted company direction
- Budget or timeline constraints changed

**Debrief Handling:**
1. Document the shift explicitly
2. Mark as ⚡ Surprise
3. Capture what changed and why
4. Note impact on existing findings

**Catalog Updates:**
- Don't delete prior findings — they're still valid context
- Add new records for new direction
- Update existing records with changed context
- Create Challenge record for "Scope Shift" if significant

### New Topic Emerges

When conversation reveals area outside original scope:

**During Session:**
- Note it but don't derail
- Ask one clarifying question
- Flag for potential expansion

**In Debrief:**
```markdown
## Scope Expansion Opportunity

New topic emerged: [Topic]
- Mentioned by: [Who]
- Context: [Why it came up]
- Relevance: [How it connects to engagement]

**Recommendation:** 
- [ ] Explore in follow-up session
- [ ] Add to current scope
- [ ] Note for future engagement
```

---

## Conflicting Information

### Same Person, Different Statements

When an individual contradicts themselves:

**During Session:**
- Note both statements with timestamps
- If safe, gently probe: "Earlier you mentioned X, now Y — help me understand"

**In Debrief:**
- Mark as ⚠️ Contradiction
- Capture both statements
- Don't resolve — flag for clarification
- Note possible explanations (context changed, nuance lost, etc.)

### Different People, Different Views

When stakeholders disagree:

**Capture Approach:**
```markdown
### ⚠️ Contradiction: [Topic]

**View A** — [Name, Title]:
"[Quote or summary]"

**View B** — [Name, Title]:
"[Quote or summary]"

**Analysis:**
- Possible explanation: [e.g., different visibility, role perspective]
- Impact: [How this affects our work]
- Resolution needed: [Yes/No, how]
```

**Catalog Handling:**
- Create records for both views
- Link both to the contradiction topic
- Add notes explaining the disagreement
- Create follow-up action to resolve

---

## Thin Sessions

### What Makes a Session "Thin"

- Duration < 15 minutes
- Transcript < 1500 words
- Few substantive answers
- Surface-level responses
- Dominated by logistics or small talk

### Debrief Approach

**Use Quick Debrief:**
- Don't force Full Debrief extraction
- Capture what exists, note the gaps
- Suggest follow-up session

**Output Format:**
```markdown
## Session Summary (Limited Content)

**Duration:** [X] minutes
**Content Level:** Thin — limited substantive discussion

**What We Captured:**
- [Finding 1]
- [Finding 2]

**Gaps Remaining:**
- [Dimension 1]: No coverage
- [Dimension 2]: Minimal coverage

**Recommendation:** Schedule focused follow-up on [specific gaps]
```

---

## Technical Issues

### Transcript Quality Problems

**Partial Transcript:**
- Work with what's available
- Note gaps: "Minutes 12-18 missing"
- Flag any context that might be lost

**Poor Speaker Attribution:**
- Note uncertainty: "Speaker unclear"
- Use context clues to attribute
- Ask user to clarify critical quotes

**Audio Quality Issues:**
- Mark unclear passages: "[inaudible]"
- Don't guess at missing words
- Note impact on findings

### Catalog Save Failures

**If record creation fails:**
1. Don't panic — capture the data
2. Output JSON for manual entry
3. Continue with remaining workflow
4. Note which records need manual creation

**Fallback Output:**
```markdown
## Manual Entry Required

Catalog save failed for the following records.
Please create manually in Airtable.

### [Record Type]
```json
{
  "fields": {
    "Name": "...",
    "Client": ["rec..."],
    ...
  }
}
```
```

---

## Sensitive Information

### When Sensitive Topics Emerge

**During Session:**
- Don't probe unnecessarily
- Respect boundaries
- Note the topic was raised

**In Debrief:**
- Capture relevance to engagement
- Don't include personal details
- Mark as sensitive if needed for team awareness

**Catalog Handling:**
- Use discretion in what's recorded
- Some things belong in conversation memory, not permanent records
- When in doubt, ask user before saving

### Off-the-Record Comments

When someone says "off the record" or "between us":

**Approach:**
- Honor the request
- Don't include in formal Catalog
- Note that relevant context exists
- User can decide what to do with it

---

## Session Types: Special Handling

### Group Workshop (4+ people)

**Prep:**
- Focus on group dynamics, not individual questions
- Prepare facilitation structure
- Identify likely perspectives by role

**Debrief:**
- Note group consensus vs. dissent
- Capture emerging themes
- Track participation levels
- Mark group decisions explicitly

### Observation/Shadowing

**Prep:**
- Minimal questions — focus on what to watch for
- Prepare observation checklist

**Debrief:**
- Focus on Process and Technology dimensions
- Note workarounds observed
- Capture what people do vs. what they say they do
- Time-stamp key observations

### System Demo

**Prep:**
- Prepare technical questions
- Know what capabilities to evaluate

**Debrief:**
- Heavy Technology dimension focus
- Capture screenshots/recordings if available
- Note system limitations observed
- Document integration points
