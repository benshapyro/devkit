# Decision Gates Reference

Standard checkpoints and go/no-go criteria for phase transitions.

---

## Purpose of Decision Gates

**Decision gates**:
- Create natural pause points for client review
- Enable course correction before investing more
- Build trust through transparency
- Protect both parties from misalignment
- Allow graceful exit points if needed

**Key Principle**: Every block month should end with a decision gate

---

## Standard Gate Structure

```
**Decision Gate**: Review [deliverable] with [stakeholders]. 
Proceed to [next phase] or [alternative] based on [criteria].
```

---

## Discovery Phase Gate

### When
After completing discovery and requirements gathering

### Review With
- Client sponsor (budget owner)
- Key stakeholders interviewed
- Cadre PM

### Deliverables to Review
- Requirements document
- Stakeholder interview findings
- Current state assessment
- Proposed solution approach
- Rough timeline and effort estimate

### Go Criteria
✅ Requirements validated and signed off by sponsor
✅ Scope boundaries clearly defined
✅ Timeline is feasible given resources
✅ Budget approved for next phase
✅ No major blockers identified

### No-Go Scenarios
❌ Requirements still unclear or contested
❌ Political resistance surfaced, needs resolution
❌ Timeline not acceptable to client
❌ Budget not available
❌ Technical feasibility concerns

### Proceed Options
- **Go**: Move to next phase (design, build, etc.)
- **Iterate**: Additional discovery needed on specific areas
- **Pause**: Wait for dependencies or budget approval
- **Pivot**: Change approach based on findings
- **Stop**: Project not viable, graceful exit

### Example Gate Language
```
**Decision Gate**: Review requirements document and findings with VP Product 
and CFO. Proceed to design phase if requirements signed off and budget approved. 
If scope unclear, schedule follow-up discovery sprint. If budget unavailable, 
pause until Q2.
```

---

## Design/Planning Phase Gate

### When
After completing process design, architecture, or technical planning

### Review With
- Client technical lead
- Business owner
- Cadre architect/lead engineer

### Deliverables to Review
- Process maps or system architecture
- Technical approach document
- Integration touchpoints identified
- Risk assessment
- Detailed timeline and resource plan

### Go Criteria
✅ Design approved by technical and business stakeholders
✅ Architecture feasible with available systems
✅ Risks identified with mitigation plans
✅ Resources committed (both sides)
✅ Timeline aligned with business needs

### No-Go Scenarios
❌ Technical approach has major concerns
❌ Integration dependencies not addressed
❌ Resource availability uncertain
❌ Timeline doesn't align with business constraints

### Proceed Options
- **Go**: Move to build/implementation phase
- **Iterate**: Refine design based on feedback
- **Re-scope**: Simplify to meet timeline/budget
- **Pause**: Wait for infrastructure readiness

### Example Gate Language
```
**Decision Gate**: Review architecture and integration plan with IT Lead 
and Cadre engineering team. Proceed to build phase if technical approach 
approved and staging environment access confirmed. If integration concerns 
raised, schedule technical spike to validate feasibility.
```

---

## Build Phase Gate (Mid-Build)

### When
Halfway through development/implementation

### Review With
- Client product owner
- Key users (if applicable)
- Cadre PM

### Deliverables to Review
- Demo of work in progress
- Updated timeline based on actuals
- Any scope changes or risks surfaced
- Testing plan preview

### Go Criteria
✅ Progress on track with timeline
✅ Demo validated against requirements
✅ No major technical blockers
✅ Scope changes approved
✅ Testing plan agreed upon

### No-Go Scenarios
❌ Significant delays detected
❌ Demo doesn't match expectations
❌ Technical debt accumulating
❌ Scope changes out of control

### Proceed Options
- **Go**: Continue with plan as designed
- **Adjust**: Scope changes needed to hit timeline
- **Extend**: More time needed, budget approved
- **Simplify**: Reduce features to meet deadline

### Example Gate Language
```
**Decision Gate**: Demo current progress with Product Owner and key users. 
Proceed with full feature set if on track. If timeline slipping, prioritize 
must-have features for Phase 1 and defer nice-to-haves to Phase 2.
```

---

## Testing/UAT Phase Gate

### When
After testing complete, before production deployment

### Review With
- Client stakeholders who will sign off
- Cadre PM and lead engineer
- Support team (if applicable)

### Deliverables to Review
- Test results and bug report
- UAT sign-off documentation
- Deployment plan
- Training materials
- Support runbook

### Go Criteria
✅ All critical bugs resolved
✅ UAT sign-off obtained from stakeholders
✅ Deployment plan reviewed and approved
✅ Training completed (if required)
✅ Support resources ready
✅ Rollback plan tested

### No-Go Scenarios
❌ Critical bugs remain unresolved
❌ UAT not signed off
❌ Users not trained
❌ Production environment not ready

### Proceed Options
- **Go**: Deploy to production as planned
- **Fix-First**: Address remaining bugs before launch
- **Phased**: Deploy to subset of users first
- **Delay**: Wait for training completion or resources

### Example Gate Language
```
**Decision Gate**: Review test results and UAT feedback with VP Operations. 
Proceed to production deployment if all critical bugs resolved and stakeholders 
sign off. If concerns remain, deploy to pilot group of 10 users first, then 
full rollout after 1 week validation.
```

---

## Deployment Phase Gate

### When
Immediately after production deployment

### Review With
- Client operations team
- Cadre support team
- Business owner

### Deliverables to Review
- Deployment success confirmation
- Initial usage metrics
- Any launch issues encountered
- Support ticket volume
- Performance monitoring

### Go Criteria
✅ Deployment completed successfully
✅ No critical post-launch issues
✅ Users able to access system
✅ Performance meets expectations
✅ Support team handling volume

### No-Go Scenarios
❌ Deployment failed or rolled back
❌ Critical bugs in production
❌ Performance issues at scale
❌ Users blocked from access

### Proceed Options
- **Go**: Move to training/optimization phase
- **Stabilize**: Address launch issues before expanding
- **Rollback**: Revert to previous system
- **Iterate**: Quick fixes before broader rollout

### Example Gate Language
```
**Decision Gate**: Review launch results 48 hours post-deployment with 
Operations team. Proceed to full user training if no critical issues. 
If performance concerns, limit to current pilot users until optimizations 
applied.
```

---

## Optimization Phase Gate

### When
After initial optimization period (typically 2-4 weeks)

### Review With
- Client business owner
- Operations team
- Cadre PM

### Deliverables to Review
- Usage metrics and analytics
- Optimization results (performance, cost)
- User feedback summary
- Phase 2 recommendations

### Go Criteria
✅ System stable and performing well
✅ User adoption metrics positive
✅ Support ticket volume sustainable
✅ Phase 2 priorities identified
✅ Handoff documentation complete

### Proceed Options
- **Close**: Engagement complete, handoff to client
- **Phase 2**: Begin next set of enhancements
- **Retainer**: Ongoing optimization support
- **Extend**: Continue current work

### Example Gate Language
```
**Decision Gate**: Review 30-day performance metrics with Product Owner. 
If adoption >80% and performance metrics green, transition to client-managed 
operations with monthly check-ins. If adoption <50%, schedule discovery 
on adoption barriers.
```

---

## Special Gate: Strategy → Implementation Boundary

### Critical Rule
**Strategy blocks (Discovery + Process Design) CANNOT automatically lead to implementation blocks**

### When
After strategy/assessment engagement completes

### Review With
- C-level sponsor
- Finance (budget owner)
- Cadre leadership

### Deliverables to Review
- Strategy document with recommendations
- ROI projections for recommended approach
- High-level implementation plan (if strategy recommends building)
- Separate SOW for implementation engagement

### Go Criteria
✅ Strategy recommendations approved by leadership
✅ Budget allocated for implementation (separate from strategy)
✅ Implementation is strategic priority (not just "nice to have")
✅ Timeline aligns with business needs
✅ Client commits resources (team time, access)

### No-Go Scenarios
❌ Strategy recommendations not approved
❌ Implementation budget not available
❌ Not current priority for business
❌ Client lacks resources to support implementation

### Proceed Options
- **Separate Engagement**: New SOW for implementation work
- **Pause**: Client wants to digest strategy first
- **Internal**: Client implements recommendations internally
- **Partial**: Start with pilot/proof-of-concept only

### Example Gate Language
```
**Decision Gate**: Present strategy recommendations to executive team. 
If approved and budget allocated, create separate implementation SOW with 
fresh discovery phase. Implementation is new engagement, not automatic 
continuation. Client may choose to implement internally or pause.
```

---

## Using Decision Gates Effectively

### In Block Creation
- Add gate at end of each month/phase
- Be specific about what's reviewed and with whom
- Include multiple proceed options, not just go/stop
- Use client-friendly language

### In Client Conversations
- Frame as collaboration, not testing
- Emphasize client control and flexibility
- Position as risk mitigation
- Make criteria objective where possible

### In Practice
- Actually schedule gate review meetings
- Document gate decisions
- Update plans based on gate outcomes
- Don't skip gates to "save time"

### Red Flags
⚠️ Client resists gate reviews → may indicate alignment issues
⚠️ Gates repeatedly pushed back → resource or priority concerns
⚠️ Gate criteria changed at last minute → scope creep warning
⚠️ Multiple no-go gates → project viability question
