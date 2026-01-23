# Validation Checklist
## Quality control before deployment

Use this checklist to verify coach instructions and user guide quality before deployment. Each item should get a YES before releasing to client.

---

## Part 1: CustomGPT Instructions Quality

### Context & Specificity

- [ ] **Company name appears 3+ times** throughout instructions
  - Not just in the header
  - Integrated naturally into examples and context
  - Reinforces "this is for us" feeling

- [ ] **Industry context is specific**, not generic
  - ❌ "Tech company"
  - ✅ "Commercial LED lighting retrofit company specializing in 100K+ sq ft facilities"

- [ ] **Business description is clear** (1-2 sentences max)
  - Someone unfamiliar could understand what they do
  - Includes their differentiator or specialty

### Personas & Pain Points

- [ ] **3-4 real names included** with roles
  - Not "Proposal Manager" → "Katie Hacker, Proposal Manager"
  - Names appear in context section and examples
  - Each has specific pain point mentioned

- [ ] **Pain points are specific** and quantified when possible
  - ❌ "Proposals take too long"
  - ✅ "Katie spends 21 days per proposal, needs to reduce to under 7 days"

- [ ] **Technical sophistication described** accurately
  - High-tech vs traditional industry
  - Power users vs beginners
  - Comfort with AI tools

### Tasks & Use Cases

- [ ] **5-7 common tasks listed** in context section
  - Actual work they do, not generic "writing" or "analysis"
  - Domain-specific terminology
  - Prioritized (most common first)

- [ ] **Example prompt is domain-specific**, not generic
  - ❌ "Write me an email"
  - ✅ "Draft a vendor qualification form for LED lighting suppliers including technical specs"

- [ ] **Improved prompt shows methodology**, not just length
  - Demonstrates all 7 coaching checks
  - Uses their terminology
  - Includes context they'd actually need

### Tone & Style

- [ ] **Communication tone matches** client culture
  - Professional for formal industries
  - Friendly for collaborative teams
  - Direct for results-driven orgs
  - Check tone-examples.md for calibration

- [ ] **Language complexity appropriate** for technical level
  - Jargon explained for beginners
  - Technical terms okay for power users
  - Industry terminology used correctly

- [ ] **Response style consistent** throughout
  - Same tone in all sections
  - No jarring shifts between formal/casual
  - Matches how they actually communicate

### Coaching Methodology

- [ ] **Continuous improvement loop present**
  - "MANDATORY" language for follow-up questions
  - All 3 question types included (Refinement, Expansion, Application)
  - "Signs to Keep Iterating" section exists

- [ ] **Core 7 checks unchanged** from template
  - Clear expectations
  - Affirmative language
  - Output format
  - Context inclusion
  - Examples if needed
  - Well-organized
  - Appropriate length

- [ ] **Testing together approach included**
  - Offers to test with real data
  - Activation loop described
  - Iteration based on results

### Technical Requirements

- [ ] **Character count under 8,000**
  - Check exact count (use word processor)
  - If over, trim examples first, then pain points
  - Never cut core methodology

- [ ] **No broken placeholders**
  - All [BRACKETS] filled in
  - No "TODO" or "FILL THIS IN" markers
  - No duplicate sections

- [ ] **Formatting is clean**
  - Headers consistent
  - Bullet points aligned
  - No weird spacing
  - Ready to copy/paste

---

## Part 2: User Guide Quality

### Structure & Completeness

- [ ] **All template sections present**
  - What is the Coach
  - When to Use
  - How to Use
  - Real [Client] Use Cases
  - Tips for Success
  - FAQs
  - Quick Reference

- [ ] **Client name throughout**, not "your company"
  - Appears in header
  - In use cases
  - In examples
  - Feels personalized

### Persona Use Cases

- [ ] **3-4 persona examples included**
  - Real names and roles
  - Before/after prompts
  - Domain-specific examples
  - Quantified improvements

- [ ] **Use cases feel authentic**, not manufactured
  - Could be real situations they face
  - Uses their terminology
  - Addresses actual pain points

- [ ] **Quantified results in each use case**
  - Time savings: "4 hours → 90 minutes"
  - Quality improvements: "80% first-draft usability"
  - Efficiency gains: "21 days → 7 days"
  - Specific numbers, not vague "better"

### Practical Guidance

- [ ] **Examples use their actual tasks**
  - Not generic "write an email"
  - Specific to their work
  - Common enough that everyone recognizes

- [ ] **Tips are actionable**, not theoretical
  - "Save prompts in a doc" not "Be organized"
  - "Test immediately" not "Iterate as needed"
  - "Ask Coach to test together" not "Practice more"

- [ ] **FAQs address real concerns**
  - Time investment ("5-10 minutes")
  - When to use vs not use
  - What if it doesn't work
  - Privacy/personal use

### Contact & Support

- [ ] **Primary contact identified**
  - Name and role
  - Communication channel (Slack/Teams/email)
  - When to reach out

- [ ] **Rollout plan described**
  - How they'll learn about it
  - Who to ask for help
  - Next steps after reading guide

---

## Part 3: Deployment Readiness

### Testing

- [ ] **Instructions tested with 2-3 real examples**
  - Used actual client tasks
  - Verified Coach responds appropriately
  - Confirmed tone matches
  - Tested continuous improvement loop

- [ ] **Character count verified** (under 8,000)
  - Exact count documented
  - Tested in ChatGPT (some platforms count differently)
  - Headroom for minor edits

- [ ] **User guide reviewed for accuracy**
  - No outdated information
  - Contact info current
  - Use cases realistic
  - Links work (if any)

### Documentation

- [ ] **Both files created and named correctly**
  - [Client]_PromptCoach_Instructions.md
  - [Client]_PromptCoach_UserGuide.md
  - Stored in accessible location

- [ ] **Deployment checklist provided**
  - Next steps clear
  - Timeline reasonable
  - Success metrics defined
  - Follow-up plan outlined

---

## Part 4: Common Issues Check

### Red Flags to Fix

- [ ] **No generic examples** like "write an email"
  - All examples domain-specific
  - Use their terminology
  - Feel authentic

- [ ] **No missing pain points** in context
  - At least 3 specific issues
  - Tied to real names
  - Quantified when possible

- [ ] **No tone mismatch**
  - Formal for professional services ✓
  - Casual for tech startups ✓
  - Direct for sales teams ✓
  - Professional-practical for manufacturing ✓

- [ ] **No broken methodology**
  - Continuous improvement loop intact
  - 7 checks present
  - Testing together included
  - Signs to iterate clear

- [ ] **No over-customization**
  - Core coaching approach unchanged
  - Context customized only
  - Methodology universal

---

## Scoring Rubric

Count YES answers in each section:

**Part 1 (Instructions): ___ / 18**
- 18/18 = Excellent, deploy immediately
- 15-17/18 = Good, minor fixes needed
- 12-14/18 = Needs improvement
- <12/18 = Significant rework required

**Part 2 (User Guide): ___ / 13**
- 13/13 = Excellent, ready to share
- 11-12/13 = Good, minor edits
- 9-10/13 = Needs improvement
- <9/13 = Major revision needed

**Part 3 (Deployment): ___ / 6**
- 6/6 = Deployment ready
- 5/6 = Almost ready
- 4/6 = Test more
- <4/6 = Not ready

**Part 4 (Issues): ___ / 5**
- 5/5 = Clean, no issues
- 4/5 = One minor issue
- 3/5 = Multiple issues
- <3/5 = Substantial problems

**Total: ___ / 42**
- 40-42 = Excellent quality, deploy
- 35-39 = Good quality, minor fixes
- 30-34 = Acceptable, some improvement needed
- <30 = Needs significant work

---

## Quick Quality Test (30 seconds)

Read instructions aloud. Does it sound like:

**Good signs**:
- You're talking to someone at the client company
- Examples feel real and specific
- You can picture the actual users
- Tone matches the workplace
- Pain points are concrete

**Bad signs**:
- Generic consultant-speak
- Could apply to any company
- Examples are theoretical
- Tone feels foreign
- Pain points are vague

If 3+ bad signs, revise before deployment.

---

## Pre-Deployment Verification

Final checks before handing off:

1. **Run spell-check** on both documents
2. **Verify all names spelled correctly**
3. **Confirm contact info current**
4. **Test instructions in actual ChatGPT**
5. **Have someone unfamiliar read user guide** - do they understand?

**Sign-off**:
- [ ] Instructions quality score: ___/18 (need 15+)
- [ ] User guide quality score: ___/13 (need 11+)
- [ ] Deployment readiness: ___/6 (need 5+)
- [ ] Issues check: ___/5 (need 4+)
- [ ] Tested with real examples: YES
- [ ] Ready to deploy: YES

**Deployed by**: _______________
**Deployment date**: _______________
**Follow-up scheduled**: _______________

---

## Post-Deployment Monitoring

After 1 week, check:
- [ ] Usage rate (50-70% tried it?)
- [ ] Feedback collected (survey or conversations)
- [ ] Common issues identified
- [ ] Success stories documented

After 2 weeks, check:
- [ ] Daily active users (20-30% goal)
- [ ] Custom GPTs created (2-3+ good sign)
- [ ] First-draft usability (80%+ goal)
- [ ] Iteration needed? (tone, examples, use cases)

---

## Remember

**Good is better than perfect**: 35+ total score = deploy and iterate
**Test with real users**: Best validation is actual usage
**Update based on feedback**: Living document, not set-it-and-forget-it
**Success = adoption**: Technical quality matters less than team engagement
