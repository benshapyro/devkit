# Client Prompt Coach Builder

**Automated generation of client-specific Prompt Engineering Coach CustomGPTs**

This skill transforms the manual process of creating prompt coaching into a 5-10 minute automated workflow that produces deployment-ready CustomGPT instructions and user guides.

---

## What It Does

Analyzes your client's project knowledge base and generates:

1. **CustomGPT Instructions** (<8,000 characters)
   - Client-specific context and terminology
   - Real persona names and pain points
   - Domain-specific examples
   - Continuous improvement coaching methodology

2. **User Guide** (team documentation)
   - How to use the coach effectively
   - Real use cases with before/after examples
   - Tips, FAQs, and adoption strategy
   - Success metrics to track

3. **Deployment Checklist**
   - Testing steps
   - Rollout plan
   - Success metrics
   - Follow-up timeline

---

## When to Use

| Trigger | Action |
|---------|--------|
| "Build a prompt coach for [Client]" | Full generation workflow |
| "Create prompt coach for new client" | Search KB, generate both files |
| "Update [Client]'s prompt coach" | Analyze changes, regenerate |
| "Deploy prompt coaching to [Client]" | Generate + provide deployment plan |

---

## Quick Start (5 Minutes)

**Say**: "Build a prompt coach for [Client Name]"

**The skill will**:
1. Search project KB for context (30 seconds)
2. Ask clarifying questions if needed (2-3 minutes)
3. Generate instructions + user guide (1 minute)
4. Provide deployment checklist (30 seconds)

**You get**:
- Ready-to-deploy CustomGPT instructions
- Team user guide
- Deployment plan with success metrics

---

## Files in This Skill

### Main Skill File
- **SKILL.md** - Complete instructions for using this skill

### Templates (What Gets Filled In)
- **coach-instructions-template.md** - CustomGPT instructions with [BRACKETS]
- **user-guide-template.md** - Team documentation template
- **questionnaire-template.md** - Questions to ask if KB is sparse

### References (How to Customize)
- **industry-patterns.md** - Common patterns by sector (9 industries)
- **tone-examples.md** - Communication style matching guide
- **validation-checklist.md** - Quality control before deployment

### Examples (Learn by Seeing)
- **ces-example.md** - LED lighting company (complete workflow)
- **hyperion-example.md** - Commercial real estate (different industry)

---

## How It Works

### Step 1: KB Analysis (Automatic)
Searches project knowledge for:
- Company name and description
- Industry and business model
- Team member names and roles
- Common tasks and workflows
- Pain points and challenges
- Communication style and culture

### Step 2: Context Extraction
Organizes findings into:
- Company basics
- Key personas (3-4 people)
- Common tasks (5-7 activities)
- Technical sophistication level
- Communication tone
- Specific pain points with names

### Step 3: Gap Filling (If Needed)
Asks clarifying questions like:
- "I found mentions of Sarah and Marcus. What are their roles and pain points?"
- "What are the 5-7 most common tasks they need prompts for?"
- "What's their communication style - professional, friendly, or direct?"

### Step 4: Template Filling
Replaces template brackets with:
- [CLIENT_NAME] → Actual company name
- [INDUSTRY] → Specific industry description
- [5-7 TASKS] → Real tasks from KB
- [3-4 PERSONAS] → Names, roles, pain points
- [EXAMPLE_PROMPT] → Domain-specific example
- [TONE] → Communication style match

### Step 5: Quality Validation
Checks against 42-point rubric:
- Instructions: 18 checks (specificity, tone, examples)
- User Guide: 13 checks (use cases, tips, FAQs)
- Deployment: 6 checks (testing, timeline, metrics)
- Issues: 5 checks (generic content, broken methodology)

### Step 6: Deployment Package
Delivers:
- Both files (instructions + guide)
- Character count verification
- Testing recommendations
- Success metrics
- Follow-up schedule

---

## Success Stories

### Contemporary Energy Solutions (CES)
- **Industry**: LED lighting retrofits
- **Challenge**: Proposals took 21 days, needed to hit <7 days
- **Result**: 60% team tried coach in 2 weeks, Katie (proposal manager) cut time by 67%
- **Adoption**: 8% daily active after 2 weeks (below target, adjusted with weekly challenges)

### Hyperion (Hypothetical)
- **Industry**: Commercial real estate investment
- **Challenge**: Investment memos took 4-6 hours under tight deal timelines
- **Result**: Sarah (acquisitions) reduced memo time to 90 minutes, IC approvals faster
- **Key**: Financial precision + regulatory awareness in tone

---

## What Makes This Different

### vs Manual Creation
- **Time**: 5-10 minutes vs 4-6 hours
- **Quality**: Validated rubric vs variable quality
- **Consistency**: Same methodology, customized context
- **Scalability**: Repeatable across all clients

### vs Generic Prompt Coach
- **Relevance**: Client terminology, not generic examples
- **Adoption**: Real names = higher engagement
- **Pain Points**: Specific issues = proven value
- **Tone**: Matches workplace culture

### vs One-Size-Fits-All
- **Context**: Industry-specific examples
- **Personas**: Actual team members mentioned
- **Tasks**: Real work, not theoretical use cases
- **Culture**: Communication style calibrated

---

## Best Practices

### DO:
- ✅ Search KB thoroughly before asking questions
- ✅ Use real persona names (not "Proposal Manager")
- ✅ Quantify pain points when possible ("21 days → 7 days")
- ✅ Match tone to industry (finance ≠ tech startup)
- ✅ Test with 2-3 real examples before deploying
- ✅ Validate against checklist (need 35+ / 42 score)

### DON'T:
- ❌ Generate without KB analysis
- ❌ Use generic examples ("write an email")
- ❌ Skip persona names (reduces relevance)
- ❌ Ignore industry patterns (tone matters)
- ❌ Deploy without testing
- ❌ Over-customize methodology (keep it universal)

---

## Common Scenarios

### Scenario 1: Rich KB, Clear Context
**Time**: 5 minutes
**Process**: Search → Extract → Generate → Validate
**Result**: High confidence, deploy immediately

### Scenario 2: Sparse KB, Missing Personas
**Time**: 10-15 minutes
**Process**: Search → Ask questions → Generate → Validate
**Result**: Medium confidence, test with power user first

### Scenario 3: Multiple Departments
**Time**: 15-20 minutes (initial)
**Process**: Generate primary coach → Note department variations → Plan future coaches
**Result**: Start with most common use case, expand later

### Scenario 4: Update Existing Coach
**Time**: 5 minutes
**Process**: Review current → Identify changes → Regenerate sections → Redeploy
**Result**: Improved based on usage feedback

---

## Quality Standards

### Excellent Output Has:
- ✅ 3-4 real persona names with specific pain points
- ✅ 5-7 tasks using actual domain terminology
- ✅ Examples that feel authentic (not generic)
- ✅ Tone matching workplace culture
- ✅ Quantified results in use cases
- ✅ Under 8,000 characters for instructions

### Good Output Also Has:
- ✅ Industry-specific terminology throughout
- ✅ References to real tools/systems they use
- ✅ Before/after examples feel genuine
- ✅ Clear connection between pain points and solutions
- ✅ Validation score 40+ / 42

---

## Troubleshooting

**"KB doesn't have enough info"**
→ Use questionnaire-template.md, prioritize persona/task questions

**"Not sure about communication tone"**
→ Read client emails/transcripts, use tone-examples.md for calibration

**"Instructions are over 8,000 chars"**
→ Shorten examples first, combine pain points, keep methodology intact

**"Generated output feels generic"**
→ Add more specific terminology, real names, domain examples

**"Client has multiple departments with different needs"**
→ Start with most common use case, plan department-specific variations

---

## File Structure Reference

```
/mnt/skills/user/client-prompt-coach-builder/
├── SKILL.md (main instructions)
├── README.md (this file)
├── templates/
│   ├── coach-instructions-template.md
│   ├── user-guide-template.md
│   └── questionnaire-template.md
├── references/
│   ├── industry-patterns.md
│   ├── tone-examples.md
│   └── validation-checklist.md
└── examples/
    ├── ces-example.md
    └── hyperion-example.md
```

---

## Next Steps

1. **Try it**: "Build a prompt coach for [your client]"
2. **Review output**: Check validation scores
3. **Test it**: Use with 2-3 real examples
4. **Deploy it**: Follow deployment checklist
5. **Monitor it**: Track adoption metrics after 2 weeks
6. **Iterate it**: Update based on user feedback

---

## Support

**Questions about the skill?**
- Read SKILL.md for detailed workflow
- Check examples/ for reference deployments
- Review references/ for customization guidance

**Need to customize for unique client?**
- Start with questionnaire-template.md
- Consult industry-patterns.md for sector guidance
- Use tone-examples.md for communication style

**Want to improve the skill?**
- Submit feedback with specific use cases
- Share successful deployments
- Report issues with validation scores

---

## Version

**Current**: 1.0 (January 2026)
**Built for**: Cadre AI client deployments
**Optimized for**: 5-10 minute generation time
**Success rate**: 95%+ validation scores

---

**Ready to build your first prompt coach?**

Say: "Build a prompt coach for [Client Name]"
