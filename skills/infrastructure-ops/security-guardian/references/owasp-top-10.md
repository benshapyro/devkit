# OWASP Top 10 (2021)

Quick reference for the most critical web application security risks.

## A01: Broken Access Control

**Risk:** Users acting outside their intended permissions.

**Common Issues:**
- Missing authorization checks on endpoints
- IDOR (Insecure Direct Object References)
- Privilege escalation
- CORS misconfiguration

**Prevention:**
```javascript
// Always verify ownership
async function getDocument(userId, docId) {
  const doc = await db.documents.findById(docId);
  if (doc.ownerId !== userId) {
    throw new ForbiddenError('Access denied');
  }
  return doc;
}

// Use middleware for authorization
app.get('/admin/*', requireRole('admin'), adminRoutes);
```

**Checklist:**
- [ ] Deny by default
- [ ] Verify ownership on every request
- [ ] Use RBAC/ABAC consistently
- [ ] Log access control failures

---

## A02: Cryptographic Failures

**Risk:** Exposure of sensitive data due to weak cryptography.

**Common Issues:**
- Storing passwords in plain text
- Using weak algorithms (MD5, SHA1)
- Transmitting data over HTTP
- Hardcoded encryption keys

**Prevention:**
```javascript
// Use strong password hashing
import bcrypt from 'bcrypt';
const SALT_ROUNDS = 12;

const hash = await bcrypt.hash(password, SALT_ROUNDS);
const valid = await bcrypt.compare(input, hash);

// Use modern encryption
import { createCipheriv, randomBytes } from 'crypto';
const key = randomBytes(32); // 256-bit key
const iv = randomBytes(16);
const cipher = createCipheriv('aes-256-gcm', key, iv);
```

**Checklist:**
- [ ] HTTPS everywhere
- [ ] bcrypt/Argon2 for passwords
- [ ] AES-256 for encryption
- [ ] Keys in environment variables

---

## A03: Injection

**Risk:** Untrusted data sent to interpreters.

**Types:** SQL, NoSQL, OS Command, LDAP, XPath

**Prevention - SQL:**
```javascript
// NEVER concatenate user input
// Bad:
const query = `SELECT * FROM users WHERE id = ${userId}`;

// Good - Parameterized queries:
const result = await db.query(
  'SELECT * FROM users WHERE id = $1',
  [userId]
);

// Good - ORM:
const user = await User.findById(userId);
```

**Prevention - Command:**
```javascript
// Avoid shell commands with user input
// If necessary, use allowlists
const ALLOWED_COMMANDS = ['status', 'version'];
if (!ALLOWED_COMMANDS.includes(command)) {
  throw new Error('Invalid command');
}
```

**Checklist:**
- [ ] Use parameterized queries
- [ ] Use ORM/ODM
- [ ] Validate input against allowlist
- [ ] Escape special characters

---

## A04: Insecure Design

**Risk:** Flaws in design that can't be fixed by implementation.

**Common Issues:**
- Missing rate limiting
- No account lockout
- Weak password requirements
- Missing fraud controls

**Prevention:**
```javascript
// Rate limiting
import rateLimit from 'express-rate-limit';

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts
  message: 'Too many login attempts'
});

app.post('/login', loginLimiter, loginHandler);

// Account lockout
if (user.failedAttempts >= 5) {
  user.lockedUntil = Date.now() + 30 * 60 * 1000;
  throw new Error('Account locked');
}
```

**Checklist:**
- [ ] Threat modeling during design
- [ ] Rate limiting on sensitive endpoints
- [ ] Account lockout mechanisms
- [ ] Strong password policy

---

## A05: Security Misconfiguration

**Risk:** Insecure default configurations.

**Common Issues:**
- Default credentials
- Debug mode in production
- Unnecessary features enabled
- Missing security headers

**Prevention:**
```javascript
// Security headers
import helmet from 'helmet';
app.use(helmet());

// Disable debug in production
if (process.env.NODE_ENV === 'production') {
  app.set('debug', false);
}

// Remove sensitive headers
app.disable('x-powered-by');
```

**Security Headers:**
```
Content-Security-Policy: default-src 'self'
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000
```

**Checklist:**
- [ ] Remove default credentials
- [ ] Disable debug in production
- [ ] Configure security headers
- [ ] Minimal permissions

---

## A06: Vulnerable Components

**Risk:** Using libraries with known vulnerabilities.

**Prevention:**
```bash
# Regular audits
npm audit
pip-audit
cargo audit

# Automated updates
dependabot / renovate

# Lock file integrity
npm ci # uses package-lock.json
```

**Checklist:**
- [ ] Regular dependency audits
- [ ] Automated security updates
- [ ] Remove unused dependencies
- [ ] Monitor CVE databases

---

## A07: Authentication Failures

**Risk:** Broken authentication mechanisms.

**Common Issues:**
- Weak passwords allowed
- Credential stuffing vulnerable
- Session fixation
- Tokens in URLs

**Prevention:**
```javascript
// Strong password requirements
const passwordSchema = z.string()
  .min(12)
  .regex(/[A-Z]/, 'Need uppercase')
  .regex(/[a-z]/, 'Need lowercase')
  .regex(/[0-9]/, 'Need number')
  .regex(/[^A-Za-z0-9]/, 'Need special char');

// Secure session configuration
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: true,
    httpOnly: true,
    sameSite: 'strict',
    maxAge: 3600000 // 1 hour
  }
}));
```

**Checklist:**
- [ ] Strong password policy
- [ ] MFA available
- [ ] Secure session handling
- [ ] Brute force protection

---

## A08: Software and Data Integrity Failures

**Risk:** Code and data without integrity verification.

**Common Issues:**
- Insecure deserialization
- Unsigned updates
- Untrusted CI/CD pipelines
- Unverified data

**Prevention:**
```javascript
// Safe deserialization
// Bad:
const data = JSON.parse(userInput); // OK for JSON
const obj = pickle.loads(userInput); // DANGEROUS

// Good - validate schema:
const validated = schema.parse(JSON.parse(input));

// Verify signatures
import { verify } from 'crypto';
const isValid = verify(
  'sha256',
  data,
  publicKey,
  signature
);
```

**Checklist:**
- [ ] Validate data integrity
- [ ] Sign releases
- [ ] Secure CI/CD pipeline
- [ ] Use SRI for CDN resources

---

## A09: Security Logging and Monitoring Failures

**Risk:** Insufficient logging to detect attacks.

**What to Log:**
- Login attempts (success/failure)
- Access control failures
- Input validation failures
- Application errors

**Prevention:**
```javascript
// Structured logging
logger.warn({
  event: 'login_failed',
  userId: attemptedUser,
  ip: req.ip,
  userAgent: req.headers['user-agent'],
  timestamp: new Date().toISOString()
});

// Alert on anomalies
if (failedLogins > 10) {
  alerting.notify('Possible brute force attack');
}
```

**Checklist:**
- [ ] Log security events
- [ ] Centralized log management
- [ ] Alerting on anomalies
- [ ] Log retention policy

---

## A10: Server-Side Request Forgery (SSRF)

**Risk:** Server fetches attacker-controlled URLs.

**Prevention:**
```javascript
// Validate URLs
const url = new URL(userUrl);
const ALLOWED_HOSTS = ['api.example.com'];

if (!ALLOWED_HOSTS.includes(url.hostname)) {
  throw new Error('Invalid host');
}

// Block internal IPs
const BLOCKED = ['127.0.0.1', '10.', '192.168.', '172.16.'];
if (BLOCKED.some(prefix => url.hostname.startsWith(prefix))) {
  throw new Error('Internal URLs not allowed');
}
```

**Checklist:**
- [ ] Allowlist valid hosts
- [ ] Block internal IPs
- [ ] Validate URL schemes
- [ ] Use network segmentation
