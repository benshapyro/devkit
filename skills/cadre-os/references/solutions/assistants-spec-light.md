# Light GPT Spec Template

Use this template when drafting specs for selected opportunities.

---

## [GPT Name]

### Purpose
[One sentence: what it does, for whom, solving what problem]

### Core Workflow
1. [User action / input step]
2. [GPT processing step]
3. [Output / delivery step]
4. [Optional: iteration or refinement step]

### Inputs
- [What user provides - text, files, context]
- [Required vs optional inputs]
- [Format expectations]

### Outputs
- [What user receives]
- [Format: prose, table, document, etc.]
- [Typical length/depth]

### Knowledge Base Requirements
| File | Purpose | Format | Priority |
|------|---------|--------|----------|
| [filename.ext] | [What it contains] | [JSON/MD/TXT] | Required |
| [filename.ext] | [What it contains] | [JSON/MD/TXT] | Optional |

*Format recommendations:*
- JSON for structured data (catalogs, databases, records)
- Markdown for narrative content (guides, policies, procedures)
- TXT for simple text (minimal formatting needs)
- Avoid large PDFs when possible (slower retrieval)

### Capability Settings
| Capability | Setting | Rationale |
|------------|---------|-----------|
| Code Interpreter | Yes/No | [Why needed or not] |
| Web Browsing | Yes/No | [Why needed or not] |
| Image Generation | Yes/No | [Why needed or not] |

*Default: Enable only what's needed. More capabilities = more confusion.*

### Sample Conversation Starters
1. "[Action-oriented starter for primary use case]"
2. "[Starter for secondary use case]"
3. "[Starter that demonstrates scope]"
4. "[Starter for common scenario]"

### Key Instructions to Include

**If using knowledge base files:**
```
CRITICAL: SEARCH YOUR KNOWLEDGE DOCUMENTS BEFORE EVERY ANSWER.

FILES YOU HAVE ACCESS TO:
- [file-1.ext]: [topic/purpose]
- [file-2.ext]: [topic/purpose]

MANDATORY PROCESS:
1. First, search these files for relevant information
2. State which file(s) you found information in
3. If information NOT in files, say so explicitly
```

**Core behavior instructions:**
- [Key instruction 1 - what to always do]
- [Key instruction 2 - output format requirement]
- [Key instruction 3 - quality standard]
- [Key instruction 4 - boundary/scope limit]
- [Key instruction 5 - error handling]

**Scope boundaries:**
```
This GPT DOES:
- [In-scope task 1]
- [In-scope task 2]

This GPT does NOT:
- [Out-of-scope task 1]
- [Out-of-scope task 2]

If asked about out-of-scope topics:
"That's outside my focus. I'm designed for [purpose]. For [out-of-scope topic], I recommend [alternative]."
```

### Testing Scenarios

**1. Core Function Test**
- Prompt: "[Specific test prompt for primary use case]"
- Expected: [What good output looks like]
- Validates: [What this tests]

**2. Edge Case Test**
- Prompt: "[Prompt that tests boundaries or unusual input]"
- Expected: [How it should handle gracefully]
- Validates: [What this tests]

**3. Out-of-Scope Test**
- Prompt: "[Prompt for something outside scope]"
- Expected: [Polite refusal with redirect]
- Validates: [Boundary enforcement]

### Estimated Build Time
- Knowledge base curation: [X hours]
- Instruction drafting: [X hours]  
- Testing & refinement: [X hours]
- **Total: [X hours/days]**

### Success Metrics
| Metric | Target | How to Measure |
|--------|--------|----------------|
| Time savings | [X hrs/week] | User time tracking |
| Adoption | [X% of target users] | Usage analytics |
| Quality | [Specific quality bar] | Sample review |
| User satisfaction | [Rating target] | Feedback survey |

---

## Spec Quality Checklist

Before delivering spec, verify:

- [ ] Purpose is one clear sentence
- [ ] Workflow has 3-5 concrete steps
- [ ] Inputs and outputs are specific
- [ ] Knowledge base files are named with formats
- [ ] Capability settings have rationale
- [ ] Conversation starters are action-oriented
- [ ] Instructions include file priority block (if applicable)
- [ ] Scope boundaries are explicit
- [ ] Testing scenarios cover core + edge + boundary
- [ ] Build time estimate is realistic
- [ ] Success metrics are measurable
