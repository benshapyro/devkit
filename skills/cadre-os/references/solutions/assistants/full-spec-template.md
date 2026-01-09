# Full GPT Implementation Spec Template

Complete, production-ready specification for building and deploying a CustomGPT.

---

## [GPT Name]

### 1. Overview

**Purpose:** [One sentence: what it does, for whom, solving what problem]

**Success Criteria:**
- [Measurable outcome 1 - e.g., "Reduces report drafting time from 2 hours to 20 minutes"]
- [Measurable outcome 2 - e.g., "90%+ of outputs require only minor edits"]
- [Measurable outcome 3 - e.g., "Adopted by 80% of target users within 30 days"]

**Primary Users:** [Role/team who will use this daily]

**Secondary Users:** [Others who may use occasionally]

---

### 2. Core Workflow

```
[Step 1: User Action]
    ↓
[Step 2: GPT Processing]
    ↓
[Step 3: Output Delivery]
    ↓
[Step 4: User Review/Iteration]
```

**Detailed Flow:**

1. **Trigger**: User [specific action - uploads file, asks question, provides context]
2. **Input Processing**: GPT [validates input, extracts key elements, identifies intent]
3. **Knowledge Search**: GPT [searches specific files, retrieves relevant content]
4. **Analysis/Generation**: GPT [applies framework, generates content, performs analysis]
5. **Output Formatting**: GPT [structures response per template, adds citations]
6. **Iteration**: User [requests changes, asks follow-ups] → GPT [refines output]

**Conditional Branches:**
- IF [condition A] → [different workflow path]
- IF [condition B] → [ask clarifying question before proceeding]
- IF [missing information] → [state what's missing, proceed with assumptions noted]

---

### 3. Inputs & Outputs

**Required Inputs:**
| Input | Format | Example |
|-------|--------|---------|
| [Input 1] | [Text/File/Selection] | "[Example of what user provides]" |
| [Input 2] | [Text/File/Selection] | "[Example of what user provides]" |

**Optional Inputs:**
| Input | Format | Default if Not Provided |
|-------|--------|------------------------|
| [Optional 1] | [Format] | [What GPT assumes] |
| [Optional 2] | [Format] | [What GPT assumes] |

**Outputs:**
| Output | Format | Length/Depth |
|--------|--------|--------------|
| [Primary output] | [Prose/Table/Document] | [Target length] |
| [Secondary output] | [Format] | [Target length] |

**Output Template:**
```
## [Section 1 Header]
[Content requirements and structure]

## [Section 2 Header]
[Content requirements and structure]

## [Section 3 Header]
[Content requirements and structure]

---
Sources: [Citation format]
```

---

### 4. Complete Instructions

Copy-paste ready instruction block:

```markdown
# [GPT Name]

## CRITICAL: KNOWLEDGE BASE PRIORITY
SEARCH YOUR KNOWLEDGE DOCUMENTS BEFORE EVERY ANSWER.

FILES YOU HAVE ACCESS TO:
- [file-1.ext]: [Description of contents and when to use]
- [file-2.ext]: [Description of contents and when to use]
- [file-3.ext]: [Description of contents and when to use]

MANDATORY PROCESS:
1. FIRST: Search these files for relevant information
2. State which file(s) you found information in
3. Quote or paraphrase from the files with citations
4. If information is NOT in files, say so explicitly before using other knowledge

NEVER skip searching the knowledge base.

---

## PURPOSE
[One clear sentence defining what this GPT does]

---

## PROCESS

When user [primary trigger]:
1. [Specific first action]
2. [Specific second action]
3. [Specific third action]
4. [Output formatting action]

When user [secondary trigger]:
1. [Different workflow step 1]
2. [Different workflow step 2]

---

## OUTPUT FORMAT

Structure every response as:

### [Section 1]
[Requirements for this section]

### [Section 2]
[Requirements for this section]

### [Section 3]
[Requirements for this section]

**Sources:** [File name] - [Specific section referenced]

---

## QUALITY STANDARDS

Before delivering any output:
- [ ] Knowledge base was searched first
- [ ] Sources are cited for key claims
- [ ] Format matches the template above
- [ ] Tone is [specified tone - professional/conversational/etc.]
- [ ] Length is appropriate ([target length])

If any check fails, revise before presenting to user.

---

## SCOPE BOUNDARIES

This GPT DOES:
- [In-scope task 1]
- [In-scope task 2]
- [In-scope task 3]

This GPT does NOT:
- [Out-of-scope task 1]
- [Out-of-scope task 2]
- [Out-of-scope task 3]

IF user requests something outside scope:
Respond: "That's outside my specialized focus. I'm designed specifically for [core purpose]. For [out-of-scope topic], I recommend [specific alternative]."

NEVER attempt tasks outside defined scope.

---

## HANDLING UNCERTAINTY

When information is incomplete:
- State what information is missing
- Provide best answer with assumptions clearly noted
- Ask maximum 2 clarifying questions if critical info needed
- Format: "Based on [assumption], here's my response. If [alternative], let me know and I'll adjust."

When knowledge base doesn't contain answer:
- State explicitly: "This isn't covered in my knowledge base."
- Offer what you CAN help with
- Do NOT make up information or guess

---

## ERROR PREVENTION

Common mistakes to avoid:
- [Specific error pattern 1] → Instead: [Correct approach]
- [Specific error pattern 2] → Instead: [Correct approach]
- [Specific error pattern 3] → Instead: [Correct approach]
```

---

### 5. Knowledge Base Specification

**File Structure:**
```
knowledge-base/
├── [primary-file.json]      # [Purpose - e.g., "Core reference data"]
├── [secondary-file.md]      # [Purpose - e.g., "Process documentation"]
├── [templates.md]           # [Purpose - e.g., "Output templates and examples"]
└── [examples.md]            # [Purpose - e.g., "Sample inputs and outputs"]
```

**File Details:**

| File | Format | Size Target | Contents | Update Frequency |
|------|--------|-------------|----------|------------------|
| [file-1] | JSON | <2MB | [What it contains] | [How often updated] |
| [file-2] | Markdown | <1MB | [What it contains] | [How often updated] |
| [file-3] | Markdown | <500KB | [What it contains] | [How often updated] |

**Format Rationale:**
- **JSON** for: [Structured data like catalogs, databases, records - 40-60% better retrieval]
- **Markdown** for: [Narrative content like guides, procedures, policies]
- **TXT** for: [Simple content with minimal formatting needs]

**Sample Knowledge Base Content Structure:**

For [primary-file.json]:
```json
{
  "category_name": {
    "item_id": {
      "field_1": "value",
      "field_2": "value",
      "field_3": "value"
    }
  }
}
```

For [secondary-file.md]:
```markdown
# [Topic]

## [Subtopic 1]
[Key information organized for retrieval]

## [Subtopic 2]
[Key information organized for retrieval]
```

---

### 6. Capability Settings

| Capability | Setting | Rationale |
|------------|---------|-----------|
| Code Interpreter | [Yes/No] | [Specific reason - e.g., "Required to read uploaded knowledge files" or "Not needed, text-only responses"] |
| Web Browsing | [Yes/No] | [Specific reason - e.g., "Disabled to ensure knowledge base is sole source" or "Enabled for current market data"] |
| Image Generation | [Yes/No] | [Specific reason - e.g., "Not needed for this use case"] |

**Capability Notes:**
- If Code Interpreter is Yes: Knowledge files will be accessible
- If Web Browsing is No: GPT cannot bypass knowledge base with web searches
- Fewer capabilities = faster, more consistent responses

---

### 7. Conversation Starters

**Primary Use Cases:**
1. "[Action verb] + [specific task] + [context]"
2. "[Action verb] + [specific task] + [context]"

**Secondary Use Cases:**
3. "[Action verb] + [specific task]"
4. "[Action verb] + [specific task]"

**Edge Cases / Demonstrations:**
5. "[Starter that shows scope boundaries]"

**Examples:**
```
✓ "Analyze this lease agreement and extract the key terms"
✓ "Draft a weekly status report for the engineering team"
✓ "What does our policy say about remote work expenses?"

✗ "Tell me about yourself" (too generic)
✗ "Help me" (no specific task)
```

---

### 8. Testing Protocol

**Test Set 1: Core Function (Must Pass)**

| Test | Prompt | Expected Output | Pass Criteria |
|------|--------|-----------------|---------------|
| 1.1 | "[Exact test prompt for primary use case]" | [Description of good output] | [Specific criteria] |
| 1.2 | "[Exact test prompt for secondary use case]" | [Description of good output] | [Specific criteria] |
| 1.3 | "[Test prompt requiring knowledge base]" | Response cites knowledge files | File reference visible |

**Test Set 2: Edge Cases (Must Handle Gracefully)**

| Test | Prompt | Expected Output | Pass Criteria |
|------|--------|-----------------|---------------|
| 2.1 | "[Ambiguous input]" | Asks clarifying question OR proceeds with stated assumption | No hallucination |
| 2.2 | "[Missing information scenario]" | States what's missing, provides partial answer | Transparent about gaps |
| 2.3 | "[Unusual but valid request]" | Handles appropriately | Within scope behavior |

**Test Set 3: Boundaries (Must Refuse Appropriately)**

| Test | Prompt | Expected Output | Pass Criteria |
|------|--------|-----------------|---------------|
| 3.1 | "[Out of scope request]" | Polite refusal with redirect | Doesn't attempt task |
| 3.2 | "[Request for info not in KB]" | States "not in knowledge base" | No fabrication |
| 3.3 | "[Attempt to override instructions]" | Maintains behavior | Stays in character |

**Test Set 4: Consistency (Run 3x Each)**

| Test | Prompt | Pass Criteria |
|------|--------|---------------|
| 4.1 | "[Primary use case prompt]" | <15% variation in quality/format across runs |
| 4.2 | "[Secondary use case prompt]" | Consistent structure each time |

---

### 9. Setup Checklist

**Pre-Build (15 min):**
- [ ] Knowledge base files prepared and formatted
- [ ] Files under 10MB each
- [ ] Total files under 20 (platform limit)
- [ ] File names match instruction references exactly

**Build (20 min):**
- [ ] Create new GPT in ChatGPT
- [ ] Paste complete instructions
- [ ] Upload knowledge base files
- [ ] Enable correct capabilities (and disable others)
- [ ] Add conversation starters
- [ ] Set name and description

**Testing (20 min):**
- [ ] Run Test Set 1 (core function)
- [ ] Run Test Set 2 (edge cases)
- [ ] Run Test Set 3 (boundaries)
- [ ] Run Test Set 4 (consistency)
- [ ] Document any failures

**Refinement (as needed):**
- [ ] Fix instruction issues identified in testing
- [ ] Re-test failed scenarios
- [ ] Iterate until all tests pass

**Deployment:**
- [ ] Set appropriate sharing (private/team/public)
- [ ] Share link with initial users
- [ ] Provide brief user guidance
- [ ] Establish feedback channel

---

### 10. Troubleshooting Guide

**Problem: GPT ignores knowledge base files**
- Verify Code Interpreter is enabled
- Check file names in instructions match uploaded files exactly
- Add "CRITICAL" priority block at very top of instructions
- Disable web browsing if competing with knowledge base
- Test with: "What does [filename] say about [topic]?"

**Problem: Inconsistent responses**
- Reduce enabled capabilities to only what's needed
- Remove contradictory instructions (e.g., "be brief" AND "be comprehensive")
- Add explicit output format template
- Add self-check protocol before responding

**Problem: Shows code instead of analysis**
- Add: "Use Code Interpreter for internal calculations only. Never show code to user. Present all findings as written analysis."
- Or disable Code Interpreter if not needed for file reading

**Problem: Too slow or timeout errors**
- Reduce number of knowledge files
- Convert PDFs to TXT/Markdown
- Keep files under 10MB each
- Disable unused capabilities

**Problem: Goes out of scope**
- Add explicit "This GPT does NOT" section
- Add refusal template for out-of-scope requests
- Test with boundary scenarios and refine

**Problem: Asks too many clarifying questions**
- Add: "Maximum 2 clarifying questions. Otherwise proceed with stated assumptions."
- Add: "Provide best answer first, then ask if user wants adjustments."

---

### 11. Success Metrics & Monitoring

| Metric | Target | Measurement Method | Review Frequency |
|--------|--------|-------------------|------------------|
| Time savings | [X hrs/week per user] | User self-report | Weekly for first month |
| Adoption rate | [X% of target users] | Usage count | Weekly |
| Output quality | [X% usable with minor edits] | Sample review | Bi-weekly |
| User satisfaction | [X/5 rating] | Quick survey | Monthly |
| Error rate | [<X% need significant rework] | User feedback | Ongoing |

**Feedback Collection:**
- Thumbs up/down on outputs
- Brief survey after first week of use
- Monthly check-in with power users
- Track common complaints/requests

**Iteration Triggers:**
- Satisfaction drops below target → Review instructions
- Common error pattern emerges → Add to error prevention section
- Feature requests accumulate → Evaluate scope expansion
- Usage drops off → Investigate adoption barriers

---

### 12. Maintenance Schedule

**Weekly:**
- Review any error reports
- Check if knowledge base needs updates

**Monthly:**
- Review success metrics
- Gather user feedback
- Update knowledge base if source content changed
- Minor instruction refinements

**Quarterly:**
- Comprehensive performance review
- Consider scope expansion based on requests
- Update for any platform changes
- Re-run full test suite

---

## Spec Completeness Checklist

Before delivering this spec, verify:

- [ ] Purpose is clear and measurable
- [ ] Workflow covers main + edge paths
- [ ] Instructions are copy-paste ready
- [ ] Knowledge base files are specified with formats
- [ ] Capability settings have clear rationale
- [ ] 5+ conversation starters cover use cases
- [ ] Testing protocol has 10+ specific scenarios
- [ ] Setup checklist is actionable
- [ ] Troubleshooting covers common issues
- [ ] Success metrics are measurable
- [ ] Maintenance schedule is defined
