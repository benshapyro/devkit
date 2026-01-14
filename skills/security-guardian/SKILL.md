---
name: security-guardian
description: >
  Security patterns and best practices for application development. Use when
  implementing authentication, authorization, API security, or reviewing code
  for vulnerabilities. Covers OWASP Top 10, secrets management, and security
  checklists. Triggers on: auth, security, OWASP, vulnerability, secrets,
  encryption, XSS, SQL injection, CSRF.
---

# Security Guardian

Comprehensive security guidance for building secure applications.

## Quick Reference

| Topic | Reference | Use When |
|-------|-----------|----------|
| OWASP Top 10 | owasp-top-10.md | Reviewing for common vulnerabilities |
| Authentication | authentication.md | Implementing login, sessions, tokens |
| Authorization | authorization.md | Implementing access control, permissions |
| API Security | api-security.md | Securing REST/GraphQL endpoints |
| Secrets Management | secrets-management.md | Handling credentials, keys, tokens |
| Security Checklist | security-checklist.md | Pre-deployment security review |

## Command Routing

| Trigger | Action |
|---------|--------|
| "OWASP", "vulnerability scan" | Load owasp-top-10.md |
| "auth", "login", "session" | Load authentication.md |
| "permission", "access control", "RBAC" | Load authorization.md |
| "API security", "rate limit", "CORS" | Load api-security.md |
| "secrets", "credentials", "API key" | Load secrets-management.md |
| "security review", "audit" | Load security-checklist.md |

## Security Principles

1. **Defense in Depth**: Multiple layers of security
2. **Least Privilege**: Minimum necessary permissions
3. **Fail Secure**: Default to denial on errors
4. **Zero Trust**: Verify every request
5. **Secure by Default**: Safe configuration out of the box

## Quick Security Checks

### Input Validation
```javascript
// Always validate and sanitize
const sanitized = validator.escape(userInput);
const validated = schema.parse(data); // zod/joi
```

### Authentication
```javascript
// Use secure password hashing
const hash = await bcrypt.hash(password, 12);
const valid = await bcrypt.compare(input, hash);
```

### SQL Injection Prevention
```javascript
// Use parameterized queries
const result = await db.query(
  'SELECT * FROM users WHERE id = $1',
  [userId]
);
```

### XSS Prevention
```javascript
// React auto-escapes, but avoid:
// dangerouslySetInnerHTML={{ __html: userInput }}

// Use DOMPurify for rich text
const clean = DOMPurify.sanitize(html);
```

## When to Use This Skill

- Implementing user authentication
- Setting up authorization/permissions
- Building public-facing APIs
- Handling sensitive data
- Pre-deployment security review
- Responding to security audit findings
