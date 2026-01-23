# Security Checklist

Pre-deployment security review checklist.

## Authentication & Sessions

- [ ] Passwords hashed with bcrypt/Argon2 (cost 12+)
- [ ] Sessions stored server-side (Redis/DB)
- [ ] Session cookies: `secure`, `httpOnly`, `sameSite`
- [ ] Session regeneration on login
- [ ] Session timeout configured
- [ ] Brute force protection (rate limiting)
- [ ] Account lockout after failed attempts
- [ ] Secure password reset flow
- [ ] MFA option available

## Authorization

- [ ] Deny by default
- [ ] Ownership verified on every request
- [ ] No direct object reference without validation
- [ ] Admin functions protected
- [ ] API scopes enforced
- [ ] Authorization failures logged

## Input Validation

- [ ] All user input validated
- [ ] Schema validation (zod/joi)
- [ ] File upload restrictions (type, size)
- [ ] URL validation for redirects
- [ ] Content-Type validation

## Injection Prevention

- [ ] Parameterized SQL queries
- [ ] ORM/ODM used correctly
- [ ] No shell commands with user input
- [ ] HTML output escaped
- [ ] `dangerouslySetInnerHTML` reviewed
- [ ] Content Security Policy configured

## Data Protection

- [ ] HTTPS everywhere
- [ ] HSTS enabled
- [ ] Sensitive data encrypted at rest
- [ ] PII handling documented
- [ ] Data retention policy implemented
- [ ] Backup encryption

## API Security

- [ ] Authentication required
- [ ] Rate limiting configured
- [ ] CORS properly configured
- [ ] Request size limits
- [ ] API versioning
- [ ] Error messages don't leak info

## Secrets Management

- [ ] No secrets in code
- [ ] .env files in .gitignore
- [ ] Secrets from environment/vault
- [ ] API keys hashed in database
- [ ] Rotation mechanism in place

## Dependencies

- [ ] `npm audit` / `pip-audit` clean
- [ ] No known vulnerable packages
- [ ] Unused dependencies removed
- [ ] Lock file committed

## Logging & Monitoring

- [ ] Security events logged
- [ ] No sensitive data in logs
- [ ] Centralized log management
- [ ] Alerting on anomalies
- [ ] Error tracking configured

## Infrastructure

- [ ] Security headers configured
- [ ] Debug mode disabled in production
- [ ] Default credentials changed
- [ ] Unnecessary ports closed
- [ ] Firewall rules configured

## Code Review

- [ ] Security-focused code review
- [ ] No TODO/FIXME security issues
- [ ] Sensitive operations audited
- [ ] Third-party code reviewed

---

## Quick Security Headers Check

```bash
curl -I https://yoursite.com
```

Expected headers:
```
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Security-Policy: default-src 'self'
X-XSS-Protection: 0
Referrer-Policy: strict-origin-when-cross-origin
```

---

## Quick Vulnerability Scan

```bash
# JavaScript
npm audit --production

# Python
pip-audit

# Dependencies check
npx snyk test

# Secrets scan
git secrets --scan
trufflehog git file://.
```

---

## Severity Levels

| Level | Response Time | Examples |
|-------|--------------|----------|
| Critical | Immediate | Auth bypass, RCE, SQL injection |
| High | 24 hours | XSS, CSRF, privilege escalation |
| Medium | 1 week | Info disclosure, missing headers |
| Low | Next sprint | Best practice violations |
