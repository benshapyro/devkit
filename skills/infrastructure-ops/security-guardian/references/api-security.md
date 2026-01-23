# API Security

Securing REST and GraphQL APIs.

## Authentication

### API Key Authentication

```javascript
// Middleware
async function authenticateApiKey(req, res, next) {
  const apiKey = req.headers['x-api-key'];

  if (!apiKey) {
    return res.status(401).json({ error: 'API key required' });
  }

  // Hash the key for lookup (store hashed in DB)
  const hashedKey = hashApiKey(apiKey);
  const keyRecord = await db.apiKeys.findByHash(hashedKey);

  if (!keyRecord || keyRecord.revokedAt) {
    return res.status(401).json({ error: 'Invalid API key' });
  }

  req.apiKey = keyRecord;
  next();
}
```

### Bearer Token

```javascript
function authenticateBearer(req, res, next) {
  const authHeader = req.headers.authorization;

  if (!authHeader?.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Bearer token required' });
  }

  const token = authHeader.slice(7);

  try {
    req.user = verifyToken(token);
    next();
  } catch (error) {
    res.status(401).json({ error: 'Invalid token' });
  }
}
```

---

## Rate Limiting

```javascript
import rateLimit from 'express-rate-limit';

// Global rate limit
const globalLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // 100 requests per window
  standardHeaders: true,
  legacyHeaders: false
});

// Stricter limit for auth endpoints
const authLimiter = rateLimit({
  windowMs: 60 * 1000, // 1 minute
  max: 5,
  message: { error: 'Too many attempts' }
});

// Per-user limit
const userLimiter = rateLimit({
  windowMs: 60 * 1000,
  max: 30,
  keyGenerator: (req) => req.user?.id || req.ip
});
```

---

## Input Validation

```javascript
import { z } from 'zod';

// Define schemas
const createUserSchema = z.object({
  email: z.string().email().max(255),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150).optional()
});

// Validation middleware
function validate(schema) {
  return (req, res, next) => {
    try {
      req.validated = schema.parse(req.body);
      next();
    } catch (error) {
      res.status(400).json({
        error: 'Validation failed',
        details: error.errors
      });
    }
  };
}

// Usage
app.post('/users', validate(createUserSchema), createUser);
```

---

## CORS Configuration

```javascript
import cors from 'cors';

const corsOptions = {
  origin: (origin, callback) => {
    const allowedOrigins = [
      'https://example.com',
      'https://app.example.com'
    ];

    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('CORS not allowed'));
    }
  },
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  allowedHeaders: ['Content-Type', 'Authorization'],
  credentials: true,
  maxAge: 86400 // 24 hours
};

app.use(cors(corsOptions));
```

---

## Request/Response Security

```javascript
import helmet from 'helmet';

app.use(helmet());

// Content-Type validation
app.use(express.json({ limit: '10kb' })); // Limit body size

// Remove sensitive headers
app.disable('x-powered-by');

// Add security headers
app.use((req, res, next) => {
  res.set({
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'Content-Security-Policy': "default-src 'self'"
  });
  next();
});
```

---

## GraphQL Security

```javascript
import depthLimit from 'graphql-depth-limit';
import { createComplexityLimitRule } from 'graphql-validation-complexity';

const server = new ApolloServer({
  typeDefs,
  resolvers,
  validationRules: [
    depthLimit(5), // Prevent deep queries
    createComplexityLimitRule(1000) // Limit complexity
  ],
  introspection: process.env.NODE_ENV !== 'production'
});

// Disable introspection in production
// Rate limit by query complexity
```

---

## Error Handling

```javascript
// Don't expose internal errors
app.use((err, req, res, next) => {
  logger.error({
    error: err.message,
    stack: err.stack,
    path: req.path,
    method: req.method
  });

  // Send safe error to client
  if (err.isOperational) {
    res.status(err.statusCode).json({
      error: err.message
    });
  } else {
    res.status(500).json({
      error: 'Internal server error'
    });
  }
});
```

---

## Checklist

- [ ] Authentication on all endpoints
- [ ] Rate limiting configured
- [ ] Input validation with schemas
- [ ] CORS properly configured
- [ ] Security headers set
- [ ] Error messages don't leak info
- [ ] Request size limits
- [ ] API versioning
