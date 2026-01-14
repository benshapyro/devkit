# SRE Runbook Generator

Generate operational runbooks from service metadata, incident patterns, and infrastructure topology.

## When to Use

Activate when:
- Creating runbooks for new services
- Documenting incident response procedures
- Defining escalation paths
- Automating remediation steps
- Standardizing operational documentation

## Command Routing

| User Request | Action | Reference |
|--------------|--------|-----------|
| "create runbook" or "new runbook" | Generate runbook | runbook-anatomy.md |
| "incident levels" or "severity" | Define SEV levels | incident-classification.md |
| "escalation" or "on-call" | Document contacts | escalation-procedures.md |
| "database down" or "common issues" | Standard scenarios | common-scenarios.md |
| "automate runbook" | Auto-remediation | automation-patterns.md |

## Quick Reference

### Runbook Structure

```
1. Service Overview
   └─ Purpose, dependencies, SLAs

2. Incident Classification
   └─ SEV levels, impact criteria

3. Diagnostic Steps
   └─ Commands, dashboards, queries

4. Remediation Steps
   └─ Common fixes, rollback procedures

5. Escalation Path
   └─ Contacts, when to escalate

6. Post-Incident
   └─ Cleanup, documentation
```

### Severity Levels

| Level | Response | Impact |
|-------|----------|--------|
| SEV1 | Immediate, all-hands | Revenue/data loss, widespread outage |
| SEV2 | < 1 hour | Major feature down, many users affected |
| SEV3 | < 4 hours | Feature degraded, subset of users |
| SEV4 | Next business day | Minor issue, workaround available |

### Runbook Checklist

- [ ] Clear title and service scope
- [ ] Symptoms and detection method
- [ ] Step-by-step diagnostics
- [ ] Commands are copy-pasteable
- [ ] Escalation contacts with methods
- [ ] Rollback procedure documented
- [ ] Last reviewed date

## Reference Files

| File | Content |
|------|---------|
| runbook-anatomy.md | Complete runbook structure |
| incident-classification.md | SEV levels, impact criteria |
| escalation-procedures.md | Contact chains, escalation timing |
| common-scenarios.md | Database, API, memory, disk scenarios |
| automation-patterns.md | From manual to auto-remediation |
