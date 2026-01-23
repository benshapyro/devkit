# Authentication Patterns

Secure authentication implementation guide.

## Password Authentication

### Hashing

```javascript
import bcrypt from 'bcrypt';

const SALT_ROUNDS = 12; // Increase for more security

// Hash password
async function hashPassword(password) {
  return bcrypt.hash(password, SALT_ROUNDS);
}

// Verify password
async function verifyPassword(password, hash) {
  return bcrypt.compare(password, hash);
}
```

### Password Requirements

```javascript
import { z } from 'zod';

const passwordSchema = z.string()
  .min(12, 'Minimum 12 characters')
  .max(128, 'Maximum 128 characters')
  .regex(/[A-Z]/, 'Need uppercase letter')
  .regex(/[a-z]/, 'Need lowercase letter')
  .regex(/[0-9]/, 'Need number')
  .regex(/[^A-Za-z0-9]/, 'Need special character')
  .refine(
    (pwd) => !commonPasswords.includes(pwd.toLowerCase()),
    'Password too common'
  );
```

---

## Session Management

### Secure Session Configuration

```javascript
import session from 'express-session';
import RedisStore from 'connect-redis';

app.use(session({
  store: new RedisStore({ client: redisClient }),
  secret: process.env.SESSION_SECRET,
  name: 'sessionId', // Don't use default 'connect.sid'
  resave: false,
  saveUninitialized: false,
  cookie: {
    secure: true,           // HTTPS only
    httpOnly: true,         // No JavaScript access
    sameSite: 'strict',     // CSRF protection
    maxAge: 3600000,        // 1 hour
    domain: '.example.com'  // Scope to domain
  }
}));
```

### Session Regeneration

```javascript
// Regenerate session on login (prevent fixation)
async function login(req, user) {
  return new Promise((resolve, reject) => {
    req.session.regenerate((err) => {
      if (err) return reject(err);
      req.session.userId = user.id;
      req.session.createdAt = Date.now();
      resolve();
    });
  });
}
```

---

## JWT Authentication

### Token Generation

```javascript
import jwt from 'jsonwebtoken';

const ACCESS_TOKEN_EXPIRY = '15m';
const REFRESH_TOKEN_EXPIRY = '7d';

function generateTokens(userId) {
  const accessToken = jwt.sign(
    { userId, type: 'access' },
    process.env.JWT_SECRET,
    { expiresIn: ACCESS_TOKEN_EXPIRY }
  );

  const refreshToken = jwt.sign(
    { userId, type: 'refresh' },
    process.env.JWT_REFRESH_SECRET,
    { expiresIn: REFRESH_TOKEN_EXPIRY }
  );

  return { accessToken, refreshToken };
}
```

### Token Verification

```javascript
function verifyAccessToken(token) {
  try {
    const payload = jwt.verify(token, process.env.JWT_SECRET);
    if (payload.type !== 'access') {
      throw new Error('Invalid token type');
    }
    return payload;
  } catch (error) {
    throw new UnauthorizedError('Invalid token');
  }
}
```

### Token Storage

```javascript
// Frontend - Store in memory or httpOnly cookie
// NEVER store in localStorage

// Set via httpOnly cookie
res.cookie('accessToken', token, {
  httpOnly: true,
  secure: true,
  sameSite: 'strict',
  maxAge: 15 * 60 * 1000 // 15 minutes
});
```

---

## OAuth 2.0 / OpenID Connect

### OAuth Flow

```javascript
import { OAuth2Client } from 'google-auth-library';

const client = new OAuth2Client(
  process.env.GOOGLE_CLIENT_ID,
  process.env.GOOGLE_CLIENT_SECRET,
  'https://example.com/auth/google/callback'
);

// Generate auth URL
function getAuthUrl() {
  return client.generateAuthUrl({
    access_type: 'offline',
    scope: ['openid', 'email', 'profile'],
    state: generateState() // CSRF protection
  });
}

// Handle callback
async function handleCallback(code, state) {
  // Verify state matches
  if (!verifyState(state)) {
    throw new Error('Invalid state');
  }

  const { tokens } = await client.getToken(code);
  const ticket = await client.verifyIdToken({
    idToken: tokens.id_token,
    audience: process.env.GOOGLE_CLIENT_ID
  });

  return ticket.getPayload();
}
```

---

## Multi-Factor Authentication

### TOTP Implementation

```javascript
import { authenticator } from 'otplib';

// Generate secret for user
function generateMfaSecret(userEmail) {
  const secret = authenticator.generateSecret();
  const otpauth = authenticator.keyuri(
    userEmail,
    'MyApp',
    secret
  );
  return { secret, otpauth }; // otpauth for QR code
}

// Verify TOTP code
function verifyTotp(secret, token) {
  return authenticator.verify({ token, secret });
}
```

### Recovery Codes

```javascript
import { randomBytes } from 'crypto';

function generateRecoveryCodes(count = 10) {
  return Array.from({ length: count }, () =>
    randomBytes(4).toString('hex').toUpperCase()
  );
}

// Store hashed recovery codes
async function storeRecoveryCodes(userId, codes) {
  const hashed = await Promise.all(
    codes.map(code => bcrypt.hash(code, 10))
  );
  await db.users.update(userId, { recoveryCodes: hashed });
}
```

---

## Brute Force Protection

```javascript
import rateLimit from 'express-rate-limit';
import RedisStore from 'rate-limit-redis';

// Rate limiting
const loginLimiter = rateLimit({
  store: new RedisStore({ client: redisClient }),
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts per window
  keyGenerator: (req) => req.body.email || req.ip,
  handler: (req, res) => {
    res.status(429).json({
      error: 'Too many attempts. Try again later.'
    });
  }
});

// Account lockout
async function handleFailedLogin(userId) {
  await db.users.increment(userId, 'failedAttempts');
  const user = await db.users.findById(userId);

  if (user.failedAttempts >= 5) {
    await db.users.update(userId, {
      lockedUntil: Date.now() + 30 * 60 * 1000 // 30 min
    });
  }
}

async function resetFailedAttempts(userId) {
  await db.users.update(userId, {
    failedAttempts: 0,
    lockedUntil: null
  });
}
```

---

## Security Headers for Auth

```javascript
// Prevent caching of auth pages
app.use('/auth/*', (req, res, next) => {
  res.set({
    'Cache-Control': 'no-store, no-cache, must-revalidate',
    'Pragma': 'no-cache',
    'Expires': '0'
  });
  next();
});
```

---

## Checklist

- [ ] Passwords hashed with bcrypt (cost 12+)
- [ ] Sessions regenerated on login
- [ ] Cookies: secure, httpOnly, sameSite
- [ ] Brute force protection
- [ ] Account lockout mechanism
- [ ] MFA available for users
- [ ] Secure password reset flow
- [ ] Session timeout enforced
