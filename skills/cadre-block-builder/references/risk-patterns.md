# Risk Patterns by Activity Cluster

Common risks, dependencies, and mitigation strategies organized by cluster type.

---

## Discovery & Strategy Risks

### Stakeholder Availability
**Risk**: Key stakeholders unavailable for interviews or decisions
**Impact**: Delays in requirements gathering, incomplete understanding
**Mitigation**: 
- Schedule interviews 2-3 weeks in advance
- Identify backup decision-makers
- Use async methods (surveys, recorded interviews)

### Scope Creep During Discovery
**Risk**: Discovery phase expands beyond original intent
**Impact**: Timeline extension, budget overrun
**Mitigation**:
- Define clear discovery boundaries upfront
- Use timeboxed sprints
- Document scope changes and get approval

### Political Dynamics
**Risk**: Hidden political agendas or resistance to findings
**Impact**: Recommendations rejected, project stalled
**Mitigation**:
- Early stakeholder mapping
- Build coalition of supporters
- Present multiple options, not single recommendation

### Changing Requirements
**Risk**: Requirements shift as discovery progresses
**Impact**: Rework, timeline delays
**Mitigation**:
- Version control on requirements
- Formal change request process
- Frequent check-ins with sponsor

---

## Process Design Risks

### Current State Unclear
**Risk**: Existing processes poorly documented or understood
**Impact**: Design based on assumptions, may not fit reality
**Mitigation**:
- Shadow users doing current process
- Map "as-is" before "to-be"
- Validate with multiple team members

### Exception Handling Underestimated
**Risk**: Focus on happy path, miss 80% of edge cases
**Impact**: Process breaks in production, user frustration
**Mitigation**:
- Explicitly ask "What goes wrong?"
- Map exception flows
- Test with real messy data

### Approval Chain Complexity
**Risk**: Underestimate approval layers and politics
**Impact**: Process bottlenecks, user abandonment
**Mitigation**:
- Map all approval touchpoints early
- Build in escalation paths
- Plan for parallel approvals where possible

---

## Integration Risks

### API Documentation Missing/Incomplete
**Risk**: Legacy system APIs poorly documented
**Impact**: 2-4 week delay for discovery, workarounds needed
**Mitigation**:
- Audit API docs before committing to timeline
- Discovery sprint specifically for API validation
- Budget for reverse engineering if needed

### Authentication Complexity
**Risk**: OAuth, SSO, or complex auth schemes underestimated
**Impact**: 1-2 week delay, security review needed
**Mitigation**:
- Validate auth approach early with IT/security
- Test auth in isolation before building
- Plan for token refresh logic

### Rate Limiting
**Risk**: API rate limits constrain sync frequency
**Impact**: Can't meet real-time requirements, batch only
**Mitigation**:
- Check rate limits before committing to real-time sync
- Design for batch processing as fallback
- Implement exponential backoff

### Data Quality Issues
**Risk**: Source system data is messy, incomplete, or duplicate
**Impact**: Transformation complexity explodes, 2-4 week delay
**Mitigation**:
- Data quality assessment in discovery
- Build data validation into pipeline
- Plan for data cleanup phase

### Legacy System Limitations
**Risk**: Old system can't support modern integration patterns
**Impact**: Architecture changes, significant delays
**Mitigation**:
- Early technical spike to validate feasibility
- Identify legacy system constraints upfront
- Plan workarounds or alternatives

---

## Custom Development Risks

### Scope Creep
**Risk**: "Just one more feature" requests during build
**Impact**: Timeline slip, budget overrun, quality decline
**Mitigation**:
- Formal change request process
- Feature prioritization framework
- Phase 2 backlog for additional requests

### Technical Debt Accumulation
**Risk**: Speed prioritized over code quality
**Impact**: Harder to maintain, bugs increase over time
**Mitigation**:
- Build in refactoring time (15-20% of sprint)
- Code review requirements
- Technical debt register

### Third-Party API Changes
**Risk**: External API changes break integration
**Impact**: Unplanned rework, emergency fixes
**Mitigation**:
- Version lock external dependencies
- Monitor deprecation notices
- Build abstraction layer

### Performance Issues at Scale
**Risk**: Works in dev/staging but slow in production
**Impact**: User abandonment, requires optimization phase
**Mitigation**:
- Load testing before launch
- Performance benchmarks defined upfront
- Optimize early, not just at end

---

## Automation Risks

### Workflow Complexity Underestimated
**Risk**: "Simple" automation has hidden conditional logic
**Impact**: Timeline doubles, may exceed no-code tool limits
**Mitigation**:
- Map full workflow including exceptions first
- Validate tool capabilities before committing
- Have custom code backup plan

### Error Handling Gaps
**Risk**: Workflow fails silently, no one notices
**Impact**: Data loss, missed actions, user distrust
**Mitigation**:
- Build error notifications into every workflow
- Log all execution attempts
- Implement retry logic

### Tool Limitations Hit Mid-Project
**Risk**: Zapier/N8n can't handle required complexity
**Impact**: Tool switch or custom development needed
**Mitigation**:
- Validate capabilities with prototype first
- Keep workflows modular for easy migration
- Know tool limits before starting

---

## AI/LLM Implementation Risks

### Model Performance Unpredictable
**Risk**: Prompts work in testing but fail in production
**Impact**: Accuracy below acceptable threshold, rework needed
**Mitigation**:
- Test with diverse real data, not just examples
- Define minimum accuracy threshold before starting
- A/B test multiple prompt approaches

### Hallucination Management
**Risk**: LLM invents facts, especially critical in high-risk domains
**Impact**: User distrust, liability issues
**Mitigation**:
- Constrain outputs to source material only
- Human-in-the-loop for high-risk decisions
- Validation layers before presenting to users

### Cost Explosion
**Risk**: Usage scales faster than expected, costs spike
**Impact**: Budget overrun, need to throttle usage
**Mitigation**:
- Model right-sizing (don't use GPT-4 for simple tasks)
- Implement compression (LLMLingua)
- Usage caps and monitoring

### Latency Issues
**Risk**: User-facing features too slow for real-time use
**Impact**: Poor user experience, abandonment
**Mitigation**:
- Test latency under load before launch
- Consider streaming responses
- Cache common queries

---

## Testing & QA Risks

### Insufficient Test Coverage
**Risk**: Test only happy paths, miss edge cases
**Impact**: Bugs in production, user frustration
**Mitigation**:
- Test case review before starting
- Include negative test cases
- Real user data for testing

### UAT Stakeholder Unavailability
**Risk**: Users too busy to test properly
**Impact**: Sign-off delays, issues found post-launch
**Mitigation**:
- Schedule UAT windows in advance
- Incentivize participation
- Limit UAT duration to prevent fatigue

### Environment Differences
**Risk**: Works in staging, breaks in production
**Impact**: Launch delays, emergency fixes
**Mitigation**:
- Production-like staging environment
- Data volume testing
- Load testing before launch

---

## Deployment Risks

### Data Migration Complexity
**Risk**: Underestimate effort to migrate/transform data
**Impact**: Launch delays, data quality issues
**Mitigation**:
- Data mapping exercise early
- Trial migrations before cutover
- Validation scripts for data quality

### Rollback Plan Inadequate
**Risk**: Launch fails, can't revert cleanly
**Impact**: Extended outage, data loss
**Mitigation**:
- Test rollback procedure before launch
- Database backup before cutover
- Feature flags for gradual rollout

### User Communication Gap
**Risk**: Users surprised by changes, not prepared
**Impact**: Support flood, user resistance
**Mitigation**:
- Communication plan 2-3 weeks before launch
- Training before go-live
- Support resources ready for launch day

---

## Training & Enablement Risks

### Documentation Becomes Outdated
**Risk**: Features change faster than docs update
**Impact**: User confusion, support overhead
**Mitigation**:
- Version control on documentation
- Documentation updates in definition of done
- Regular doc review cycles

### Training Doesn't Stick
**Risk**: Users forget training before they use system
**Impact**: Support tickets, low adoption
**Mitigation**:
- Just-in-time training (right before launch)
- Quick reference guides at point of use
- Recorded training for reference

### Change Resistance
**Risk**: Users resist new system, prefer old way
**Impact**: Low adoption, parallel systems run
**Mitigation**:
- Early user involvement in design
- Highlight benefits, not just features
- Champions program

---

## Optimization Risks

### Premature Optimization
**Risk**: Optimize before understanding real usage patterns
**Impact**: Wasted effort on wrong areas
**Mitigation**:
- Instrument and measure first
- Let real usage guide optimization
- Focus on bottlenecks, not everything

### Breaking Changes
**Risk**: Optimization breaks existing functionality
**Impact**: User frustration, rollback needed
**Mitigation**:
- Comprehensive testing after optimizations
- Gradual rollout of changes
- Feature flags for quick rollback

---

## Using This Reference

**During Discovery**: Review relevant cluster risks, ask probing questions
**In Block Creation**: Include 3-5 highest-priority risks in risk checkpoint
**With Clients**: Use plain English, explain impact and mitigation options
**For Confidence Scoring**: More risks = lower confidence score

**Example Risk Documentation**:
```
⚠️ RISK CHECKPOINT

1. API Documentation Unknown (Integration Risk)
   Impact: Could add 2-4 weeks if docs missing
   Mitigation: Discovery sprint to audit API first
   Status: UNCONFIRMED
```
