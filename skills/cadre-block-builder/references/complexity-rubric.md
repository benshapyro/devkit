# Complexity Rubric

Quick reference for rating activity cluster complexity. Use this to estimate durations accurately.

---

## Discovery & Strategy

### Simple (1-2 weeks)
- 1-2 stakeholders maximum
- Clear, well-defined problem
- Single department or team
- Requirements already partially documented
- Minimal research needed
- No political complexity

### Medium (2-4 weeks)
- 3-5 stakeholders
- Moderate problem complexity
- Cross-functional (2-3 departments)
- Some discovery and research needed
- Light competitive landscape analysis
- Some organizational dynamics

### Complex (4-8 weeks)
- 10+ stakeholders across organization
- Organizational change management required
- Significant political dynamics
- Deep research and analysis needed
- Multiple departments/business units
- External market analysis required

---

## Process Design

### Simple (1-2 weeks)
- 1-2 workflows to map
- Linear process, minimal branching
- Few decision points or approvals
- Single system/tool involved
- Clear current state documentation

### Medium (2-3 weeks)
- 3-5 workflows to map
- Some conditional branching logic
- Multiple approval chains
- 2-3 systems involved
- Current state needs discovery

### Complex (3-6 weeks)
- 10+ interconnected workflows
- Complex branching and exception handling
- Multiple approval layers
- 5+ systems involved
- Organizational process redesign

---

## Integration

### Simple (2-4 weeks)
- Pre-built connectors available (Zapier/Tray.io)
- Standard, well-documented APIs
- Minimal data transformation needed
- 1-2 systems to connect
- Simple authentication (API key)

### Medium (4-8 weeks)
- Custom API integration required
- Moderate data mapping/transformation
- 3-4 systems to connect
- OAuth or complex authentication
- Some legacy system challenges

### Complex (8-16 weeks)
- Multiple systems (5+) with complex dependencies
- Extensive data transformation and validation
- Legacy APIs with poor/no documentation
- Complex authentication schemes
- Real-time sync requirements
- High data volume considerations

---

## Custom Development

### Simple (4-6 weeks)
- 1-3 core features
- Standard tech stack (React, Node, etc.)
- Minimal backend complexity
- Basic UI/UX requirements
- No complex integrations
- Small user base (<100 users)

### Medium (8-12 weeks)
- 3-5 features with moderate complexity
- Some custom business logic
- Moderate UI/UX requirements
- 1-2 third-party integrations
- Medium user base (100-1000 users)
- Basic admin functionality

### Complex (12-24 weeks)
- 10+ features with complex interactions
- Sophisticated business logic
- Advanced UI/UX requirements
- Multiple third-party integrations
- Large user base (1000+ users)
- Advanced admin/reporting features
- Complex data models

---

## Automation

### Simple (1-3 weeks)
- 1-3 linear workflows
- Standard triggers (form submission, new record)
- Pre-built nodes/actions available
- Minimal data transformation
- Basic error handling

### Medium (3-6 weeks)
- 5-10 workflows with some complexity
- Conditional logic and branching
- Some custom JavaScript/Python
- Moderate data transformation
- Comprehensive error handling
- Testing across edge cases

### Complex (6-12 weeks)
- 20+ interconnected workflows
- Complex conditional branching
- Extensive custom code
- Complex data transformation logic
- Advanced error handling and retry logic
- Multiple systems orchestrated

---

## AI/LLM Implementation

### Simple (3-6 weeks)
- Single-purpose use case (summarization, Q&A)
- Basic prompt engineering
- Standard model (GPT-4, Claude)
- Simple RAG with existing docs
- Basic evaluation metrics
- Low-risk domain

### Medium (6-10 weeks)
- Multi-prompt workflow
- Custom RAG pipeline with chunking strategy
- Model comparison and selection
- Structured output requirements
- Performance testing and optimization
- Moderate-risk domain

### Complex (10-20 weeks)
- Multi-agent system with orchestration
- Fine-tuning or custom models
- Complex RAG with multiple data sources
- Advanced prompt engineering with chains
- Extensive testing and evaluation
- Production monitoring and observability
- High-risk domain (legal, medical, financial)

---

## Testing & QA

### Simple (1-2 weeks)
- Basic functional testing
- Small scope (<10 test cases)
- Few edge cases to validate
- Single environment (staging)
- Manual testing acceptable

### Medium (2-4 weeks)
- Comprehensive functional testing
- Moderate scope (10-50 test cases)
- User acceptance testing sessions
- Multiple environments
- Some automated tests
- Performance spot checks

### Complex (4-8 weeks)
- Extensive test coverage (100+ cases)
- Automated test suite required
- Load and performance testing
- Security testing and penetration testing
- Multiple user roles and permissions
- Complex data scenarios
- Regression testing

---

## Deployment

### Simple (1-2 weeks)
- Standard deployment process
- No data migration required
- Low-risk change
- Single environment push
- Straightforward rollback plan
- Limited user impact

### Medium (2-4 weeks)
- Data migration required
- Moderate complexity cutover
- Phased rollout approach
- Multiple environment promotion
- Moderate user impact
- Detailed rollback procedures

### Complex (4-8 weeks)
- Large-scale data migration
- Complex cutover coordination
- Blue-green or canary deployment
- Zero-downtime requirements
- High user impact
- Extensive rollback planning
- 24/7 monitoring post-launch

---

## Training & Enablement

### Simple (1-2 weeks)
- Basic documentation (user guide)
- Single training session
- Small user group (<10 people)
- Straightforward features
- Minimal change management

### Medium (2-3 weeks)
- Comprehensive documentation (user + admin guides)
- Multiple training sessions (different roles)
- Medium user group (10-50 people)
- Moderate change management
- Video tutorials
- Knowledge base setup

### Complex (3-6 weeks)
- Extensive documentation suite
- Train-the-trainer program
- Large user group (50+ people)
- Significant organizational change
- Multiple training formats (live, video, hands-on)
- Change management campaign
- Ongoing support planning

---

## Optimization

### Simple (2-4 weeks)
- Minor performance tweaks
- Basic monitoring setup
- Small bug fixes
- Simple feature enhancements
- Limited scope adjustments

### Medium (4-8 weeks)
- Significant performance optimizations
- Comprehensive monitoring and alerting
- Feature additions based on feedback
- Cost optimization efforts
- Workflow refinements

### Complex (8-12 weeks)
- Major performance overhaul
- Architectural improvements
- Extensive feature additions
- Advanced cost optimization
- Complex monitoring and observability
- Continuous improvement cycles

---

## Using This Rubric

1. **For each activity cluster in your block**, read the complexity descriptions
2. **Choose the level that best matches** your specific situation
3. **Use edge cases to decide**: If unsure between Simple and Medium, default to Medium (conservative)
4. **Input complexity ratings** into `estimate_duration.py` for total duration
5. **Document your reasoning** in the block's internal version for future reference

**Example**:
```
Integration cluster for Salesforce-HubSpot:
- Custom API work needed (not pre-built) → eliminates Simple
- 2 systems only, moderate data mapping → Medium fits
- No legacy challenges, good API docs → not Complex
Rating: Medium (4-8 weeks)
```
