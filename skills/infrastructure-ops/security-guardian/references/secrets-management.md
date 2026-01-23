# Secrets Management

Handling credentials, API keys, and sensitive configuration.

## Environment Variables

### Loading Secrets

```javascript
// Use dotenv for local development
import dotenv from 'dotenv';

if (process.env.NODE_ENV !== 'production') {
  dotenv.config();
}

// Access secrets
const dbPassword = process.env.DATABASE_PASSWORD;
const apiKey = process.env.STRIPE_API_KEY;
```

### Required Validation

```javascript
// Validate required secrets at startup
const REQUIRED_SECRETS = [
  'DATABASE_URL',
  'JWT_SECRET',
  'STRIPE_API_KEY'
];

function validateSecrets() {
  const missing = REQUIRED_SECRETS.filter(
    key => !process.env[key]
  );

  if (missing.length > 0) {
    throw new Error(
      `Missing required secrets: ${missing.join(', ')}`
    );
  }
}

validateSecrets();
```

---

## Secret Patterns to Avoid

```javascript
// NEVER do this:
const API_KEY = 'sk_live_abc123...'; // Hardcoded
const password = 'supersecret';      // In code
const conn = 'postgres://user:pass@host'; // Inline credentials

// ALWAYS do this:
const API_KEY = process.env.API_KEY;
const password = process.env.DB_PASSWORD;
const conn = process.env.DATABASE_URL;
```

---

## .gitignore for Secrets

```gitignore
# Environment files
.env
.env.local
.env.*.local
.env.production

# Credentials
*.pem
*.key
credentials.json
service-account.json

# Config with secrets
config/local.json
config/production.json
```

---

## Secret Rotation

```javascript
// Support for rotating secrets
const secrets = {
  current: process.env.JWT_SECRET,
  previous: process.env.JWT_SECRET_PREVIOUS
};

function verifyToken(token) {
  // Try current secret first
  try {
    return jwt.verify(token, secrets.current);
  } catch (e) {
    // Fall back to previous during rotation
    if (secrets.previous) {
      return jwt.verify(token, secrets.previous);
    }
    throw e;
  }
}
```

---

## Secrets in Docker

```dockerfile
# NEVER embed secrets in Dockerfile
# Bad:
ENV API_KEY=sk_live_abc123

# Good: Use runtime injection
# docker run -e API_KEY=$API_KEY myapp
```

```yaml
# docker-compose.yml
services:
  app:
    environment:
      - DATABASE_URL
      - API_KEY
    env_file:
      - .env  # Not committed to git
```

---

## Cloud Secret Managers

### AWS Secrets Manager

```javascript
import { SecretsManager } from '@aws-sdk/client-secrets-manager';

const client = new SecretsManager({ region: 'us-east-1' });

async function getSecret(secretId) {
  const response = await client.getSecretValue({
    SecretId: secretId
  });

  return JSON.parse(response.SecretString);
}

// Cache secrets
let cachedSecrets = null;
let cacheExpiry = 0;

async function getSecrets() {
  if (cachedSecrets && Date.now() < cacheExpiry) {
    return cachedSecrets;
  }

  cachedSecrets = await getSecret('myapp/production');
  cacheExpiry = Date.now() + 5 * 60 * 1000; // 5 min cache

  return cachedSecrets;
}
```

### HashiCorp Vault

```javascript
import vault from 'node-vault';

const client = vault({
  apiVersion: 'v1',
  endpoint: process.env.VAULT_ADDR,
  token: process.env.VAULT_TOKEN
});

async function getSecret(path) {
  const result = await client.read(path);
  return result.data.data;
}
```

---

## API Key Generation

```javascript
import { randomBytes } from 'crypto';

// Generate secure API key
function generateApiKey() {
  const prefix = 'sk_live_'; // Identifiable prefix
  const random = randomBytes(24).toString('base64url');
  return prefix + random;
}

// Store hashed version
async function createApiKey(userId) {
  const key = generateApiKey();
  const hash = await hashApiKey(key);

  await db.apiKeys.create({
    userId,
    hash,
    prefix: key.slice(0, 12), // Store prefix for identification
    createdAt: new Date()
  });

  // Return key only once - never stored in plaintext
  return key;
}
```

---

## Encryption at Rest

```javascript
import { createCipheriv, createDecipheriv, randomBytes } from 'crypto';

const ALGORITHM = 'aes-256-gcm';

function encrypt(plaintext, key) {
  const iv = randomBytes(16);
  const cipher = createCipheriv(ALGORITHM, key, iv);

  let encrypted = cipher.update(plaintext, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const authTag = cipher.getAuthTag();

  return {
    iv: iv.toString('hex'),
    encrypted,
    authTag: authTag.toString('hex')
  };
}

function decrypt(data, key) {
  const decipher = createDecipheriv(
    ALGORITHM,
    key,
    Buffer.from(data.iv, 'hex')
  );

  decipher.setAuthTag(Buffer.from(data.authTag, 'hex'));

  let decrypted = decipher.update(data.encrypted, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return decrypted;
}
```

---

## Checklist

- [ ] No secrets in code or version control
- [ ] .env files in .gitignore
- [ ] Required secrets validated at startup
- [ ] Secrets rotatable without downtime
- [ ] API keys hashed in database
- [ ] Encryption key management in place
- [ ] Audit logging for secret access
