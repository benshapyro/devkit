---
name: database-migration
description: >
  Database migration patterns for zero-downtime deployments. Use when planning
  schema changes, writing migrations, or deploying database updates. Covers
  expand-contract pattern, rollback strategies, and production checklists.
  Triggers on: migration, schema, database change, ALTER TABLE, zero-downtime.
---

# Database Migration

Safe database migration patterns for production systems.

## Quick Reference

| Topic | Reference | Use When |
|-------|-----------|----------|
| Zero-Downtime Patterns | zero-downtime-patterns.md | Planning schema changes |
| Tool Comparison | tool-comparison.md | Choosing migration tools |
| Rollback Strategies | rollback-strategies.md | Planning recovery |
| Testing Migrations | testing-migrations.md | Validating changes |
| Production Checklist | production-checklist.md | Pre-deployment review |

## Command Routing

| Trigger | Action |
|---------|--------|
| "zero-downtime", "expand-contract" | Load zero-downtime-patterns.md |
| "migration tool", "Flyway", "Alembic" | Load tool-comparison.md |
| "rollback", "revert", "undo" | Load rollback-strategies.md |
| "test migration", "validate" | Load testing-migrations.md |
| "deploy migration", "production" | Load production-checklist.md |

## Core Principles

1. **Never break running code**: Old code must work during migration
2. **Always reversible**: Every migration needs a rollback plan
3. **Test with production data**: Volume matters
4. **Deploy incrementally**: Small changes, frequent deploys
5. **Monitor everything**: Watch for performance degradation

## Common Patterns

### Add Column (Safe)
```sql
-- Step 1: Add nullable column
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Step 2: Backfill data
UPDATE users SET phone = '' WHERE phone IS NULL;

-- Step 3: Add constraint (later, after code updated)
ALTER TABLE users ALTER COLUMN phone SET NOT NULL;
```

### Rename Column (Expand-Contract)
```sql
-- Step 1: Add new column
ALTER TABLE users ADD COLUMN full_name VARCHAR(255);

-- Step 2: Backfill
UPDATE users SET full_name = name;

-- Step 3: Deploy code that writes to both
-- Step 4: Deploy code that reads from new
-- Step 5: Drop old column (after verification)
ALTER TABLE users DROP COLUMN name;
```

### Add Index (Non-Blocking)
```sql
-- PostgreSQL: CONCURRENTLY prevents locking
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- MySQL: ALGORITHM=INPLACE, LOCK=NONE
ALTER TABLE users ADD INDEX idx_email (email),
  ALGORITHM=INPLACE, LOCK=NONE;
```

## When to Use This Skill

- Planning database schema changes
- Writing migration scripts
- Deploying to production databases
- Reviewing migration PRs
- Recovering from failed migrations
