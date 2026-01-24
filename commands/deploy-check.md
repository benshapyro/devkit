---
tool: claude-code
description: Run pre-deployment safety checks including tests, migrations, environment variables, and monitoring configuration
allowed-tools: Read, Grep, Glob, Bash
argument-hint: "[environment]"
---

# /deploy-check

Verify deployment readiness with a senior engineer's checklist.

## Usage

```
/deploy-check [environment]
```

Default environment is `production`.

## Process

### 1. Code Quality Checks

**Run tests:**
```bash
npm test 2>&1 || pytest -q 2>&1
```

**Type checking:**
```bash
npx tsc --noEmit 2>&1 || mypy . 2>&1
```

**Linting:**
```bash
npm run lint 2>&1 || ruff check . 2>&1
```

**Check for debug statements:**
```
Grep: console\.log\(|console\.debug\(|debugger;
Grep: print\(|breakpoint\(\)|pdb\.set_trace
Grep: TODO:|FIXME:|HACK:|XXX:
```

### 2. Database Checks

**Find pending migrations:**
```
Glob: **/migrations/*.{sql,py,ts,js}
```

```bash
# Check migration status
npx prisma migrate status 2>&1 || \
alembic current 2>&1 || \
npx knex migrate:status 2>&1
```

**Check for destructive migrations:**
```
Grep in migrations: DROP TABLE|DROP COLUMN|DELETE FROM|TRUNCATE
```

**Verify rollback scripts exist:**
```
Glob: **/migrations/*down*|**/migrations/*rollback*
```

### 3. Environment Checks

**Required env vars documented:**
```
Read: .env.example
Read: README.md (look for environment section)
```

**Check for hardcoded secrets:**
```
Grep: password\s*=\s*['"][^'"]+['"]
Grep: api_key\s*=\s*['"][^'"]+['"]
Grep: secret\s*=\s*['"][^'"]+['"]
```

**Feature flags configured:**
```
Grep: process\.env\.|os\.environ|ENV\[
Glob: **/config/*.{json,yaml,yml,ts,js}
```

### 4. Monitoring Checks

**Error tracking configured:**
```
Grep: Sentry|Bugsnag|Rollbar|NewRelic|Datadog
Glob: **/sentry.*.{js,ts,json}
```

**Logging in place:**
```
Grep: logger\.|logging\.|winston|pino|bunyan
```

**Health check endpoint:**
```
Grep: /health|/healthz|/ready|/live
```

**Runbooks exist:**
```
Glob: **/runbook*|**/RUNBOOK*|**/docs/operations*
```

### 5. Deployment Checks

**Branch status:**
```bash
git fetch origin
git status
git log --oneline origin/main..HEAD
```

**No merge conflicts:**
```bash
git diff --check
```

**CI status (if GitHub):**
```bash
gh run list --limit 5 2>/dev/null
```

**Dependencies up to date:**
```bash
npm outdated 2>&1 || pip list --outdated 2>&1
```

### 6. Security Quick Scan

**Run security audit:**
```bash
npm audit --production 2>&1 || safety check 2>&1
```

**Check for vulnerable patterns:**
```
Grep: eval\(|exec\(|dangerouslySetInnerHTML
```

### 7. Generate Report

```markdown
## Deployment Readiness: {environment}

**Checked at:** {timestamp}
**Branch:** {branch}
**Commit:** {short_hash}

---

### Summary

| Category | Status | Details |
|----------|--------|---------|
| Tests | ✅ / ❌ | {pass_count} passed, {fail_count} failed |
| Types | ✅ / ❌ | {error_count} errors |
| Lint | ✅ / ❌ | {warning_count} warnings |
| Security | ✅ / ⚠️ / ❌ | {vuln_count} vulnerabilities |
| Migrations | ✅ / ⚠️ | {pending_count} pending |
| Environment | ✅ / ⚠️ | {missing_count} undocumented vars |
| Monitoring | ✅ / ⚠️ | {status} |

---

### ✅ Passed ({count})

- **Tests:** {pass_count} passed, 0 failed
- **Type checking:** No errors
- **Linting:** Clean
- **Branch:** Up to date with origin/main
- **CI:** All checks passing
- **Security:** No critical vulnerabilities

---

### ⚠️ Warnings ({count})

| Issue | Location | Recommendation |
|-------|----------|----------------|
| Missing runbook | {feature} | Create runbook before deploy |
| TODO comments | {files} | Review and resolve |
| Outdated deps | {packages} | Update in next sprint |
| Debug statement | {file}:{line} | Remove before deploy |

---

### ❌ Blockers ({count})

| Issue | Location | Required Action |
|-------|----------|-----------------|
| Failing tests | {test_file} | Fix before deploy |
| Type errors | {file}:{line} | Resolve type issues |
| Critical vuln | {package} | Upgrade immediately |
| Pending migration | {migration} | Run or defer |
| Merge conflicts | {files} | Resolve conflicts |

---

### Pre-Deploy Checklist

**Required:**
- [ ] All blockers resolved
- [ ] Warnings reviewed and accepted
- [ ] Team notified of deployment
- [ ] Rollback plan confirmed

**Recommended:**
- [ ] Smoke test in staging
- [ ] Monitor error rates post-deploy
- [ ] Update changelog/release notes

---

### Rollback Plan

If issues occur after deployment:

1. **Immediate:** Revert to previous version
   ```bash
   git revert {commit_hash}
   # or
   kubectl rollout undo deployment/{name}
   ```

2. **Database:** Run down migrations if needed
   ```bash
   {rollback_command}
   ```

3. **Notify:** Alert team in #{channel}

---

### Recommendation

{READY TO DEPLOY | FIX BLOCKERS FIRST | REVIEW WARNINGS}

{Summary of what needs to happen before deploying}
```

## Environment-Specific Checks

| Environment | Additional Checks |
|-------------|-------------------|
| `production` | Full security scan, require all green |
| `staging` | Allow warnings, skip runbook check |
| `development` | Minimal checks, focus on tests |

## Example

```
/deploy-check production
```

Runs full deployment readiness check for production environment.

## Notes

- Blockers must be resolved before deploying to production
- Warnings are acceptable but should be tracked
- Some checks require CI integration (GitHub Actions, etc.)
- Customize checklist based on your infrastructure
