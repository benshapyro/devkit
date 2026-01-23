# Authorization Patterns

Access control and permission management.

## Authorization Models

### Role-Based Access Control (RBAC)

```javascript
// Define roles and permissions
const ROLES = {
  admin: ['read', 'write', 'delete', 'manage_users'],
  editor: ['read', 'write'],
  viewer: ['read']
};

// Check permission
function hasPermission(userRole, permission) {
  return ROLES[userRole]?.includes(permission) ?? false;
}

// Middleware
function requirePermission(permission) {
  return (req, res, next) => {
    if (!hasPermission(req.user.role, permission)) {
      return res.status(403).json({ error: 'Forbidden' });
    }
    next();
  };
}

// Usage
app.delete('/posts/:id',
  requirePermission('delete'),
  deletePost
);
```

### Attribute-Based Access Control (ABAC)

```javascript
// Policy-based decisions
const policies = [
  {
    action: 'edit',
    resource: 'document',
    condition: (user, resource) =>
      resource.ownerId === user.id ||
      resource.editors.includes(user.id)
  },
  {
    action: 'delete',
    resource: 'document',
    condition: (user, resource) =>
      resource.ownerId === user.id ||
      user.role === 'admin'
  }
];

function isAuthorized(user, action, resource) {
  const policy = policies.find(
    p => p.action === action && p.resource === resource.type
  );
  return policy?.condition(user, resource) ?? false;
}
```

---

## Resource-Level Authorization

### Ownership Verification

```javascript
// Always verify resource ownership
async function getDocument(userId, docId) {
  const doc = await db.documents.findById(docId);

  if (!doc) {
    throw new NotFoundError('Document not found');
  }

  // Check ownership or permission
  if (doc.ownerId !== userId && !doc.sharedWith.includes(userId)) {
    throw new ForbiddenError('Access denied');
  }

  return doc;
}
```

### Preventing IDOR

```javascript
// Bad: Direct object reference
app.get('/api/orders/:id', async (req, res) => {
  const order = await Order.findById(req.params.id);
  res.json(order); // Anyone can access any order!
});

// Good: Verify ownership
app.get('/api/orders/:id', async (req, res) => {
  const order = await Order.findOne({
    _id: req.params.id,
    userId: req.user.id // Scoped to user
  });

  if (!order) {
    return res.status(404).json({ error: 'Not found' });
  }

  res.json(order);
});
```

---

## Hierarchical Permissions

```javascript
// Organization hierarchy
const hierarchy = {
  org: ['team', 'project', 'document'],
  team: ['project', 'document'],
  project: ['document']
};

async function canAccessResource(user, resourceType, resourceId) {
  // Check direct access
  const directAccess = await checkDirectAccess(user, resourceType, resourceId);
  if (directAccess) return true;

  // Check parent access
  for (const parentType of getParentTypes(resourceType)) {
    const parentId = await getParentId(resourceType, resourceId, parentType);
    if (await checkDirectAccess(user, parentType, parentId)) {
      return true;
    }
  }

  return false;
}
```

---

## API Authorization

### Scoped API Keys

```javascript
// Define scopes
const SCOPES = {
  'read:users': 'Read user data',
  'write:users': 'Modify user data',
  'read:posts': 'Read posts',
  'write:posts': 'Create/modify posts'
};

// Verify scope
function requireScope(scope) {
  return (req, res, next) => {
    if (!req.apiKey.scopes.includes(scope)) {
      return res.status(403).json({
        error: 'Insufficient scope',
        required: scope
      });
    }
    next();
  };
}

// Usage
app.post('/api/users',
  authenticateApiKey,
  requireScope('write:users'),
  createUser
);
```

---

## Frontend Authorization

```javascript
// React permission component
function Can({ permission, children, fallback = null }) {
  const { user } = useAuth();

  if (!hasPermission(user.role, permission)) {
    return fallback;
  }

  return children;
}

// Usage
<Can permission="delete" fallback={<span>View only</span>}>
  <button onClick={handleDelete}>Delete</button>
</Can>
```

---

## Audit Logging

```javascript
// Log authorization decisions
function logAuthzDecision(userId, action, resource, allowed, reason) {
  logger.info({
    type: 'authorization',
    userId,
    action,
    resourceType: resource.type,
    resourceId: resource.id,
    allowed,
    reason,
    timestamp: new Date().toISOString()
  });
}
```

---

## Checklist

- [ ] Deny by default
- [ ] Verify ownership on every request
- [ ] Use consistent authorization model (RBAC/ABAC)
- [ ] Never trust client-provided IDs without validation
- [ ] Log authorization failures
- [ ] Separate read/write permissions
- [ ] Regular permission audits
