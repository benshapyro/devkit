# Rollback Strategies

Recovery procedures for failed migrations.

## Prevention First

### Pre-Migration Checklist
- [ ] Backup taken and verified
- [ ] Rollback script tested
- [ ] Migration tested on staging with prod data
- [ ] Maintenance window communicated
- [ ] Monitoring dashboards ready

---

## Rollback Types

### 1. Schema Rollback
Revert DDL changes (CREATE, ALTER, DROP).

```sql
-- down.sql
ALTER TABLE users DROP COLUMN new_column;
DROP INDEX idx_new_index;
```

### 2. Data Rollback
Restore data to previous state.

```sql
-- Restore from backup table
INSERT INTO users SELECT * FROM users_backup
ON CONFLICT (id) DO UPDATE SET
  name = EXCLUDED.name,
  email = EXCLUDED.email;
```

### 3. Application Rollback
Deploy previous application version.

```bash
# Kubernetes
kubectl rollout undo deployment/myapp

# Docker
docker-compose up -d --no-deps myapp:previous
```

---

## Rollback Patterns

### Pattern 1: Paired Migrations

Always write up and down together:

```javascript
// Knex migration
exports.up = async (knex) => {
  await knex.schema.createTable('audit_logs', table => {
    table.increments('id');
    table.string('action');
    table.timestamp('created_at');
  });
};

exports.down = async (knex) => {
  await knex.schema.dropTable('audit_logs');
};
```

### Pattern 2: Backup Table

Create backup before destructive changes:

```sql
-- Before migration
CREATE TABLE users_backup_20240113 AS SELECT * FROM users;

-- Migration
ALTER TABLE users DROP COLUMN legacy_field;

-- Rollback if needed
ALTER TABLE users ADD COLUMN legacy_field VARCHAR(100);
UPDATE users u SET legacy_field = b.legacy_field
FROM users_backup_20240113 b WHERE u.id = b.id;
```

### Pattern 3: Soft Delete Period

Don't immediately drop, rename first:

```sql
-- Instead of DROP
ALTER TABLE legacy_table RENAME TO _deprecated_legacy_table;

-- Keep for 30 days, then:
DROP TABLE _deprecated_legacy_table;
```

---

## Emergency Rollback Procedures

### Immediate: Stop the Migration

```sql
-- PostgreSQL: Cancel running queries
SELECT pg_cancel_backend(pid)
FROM pg_stat_activity
WHERE query LIKE '%ALTER TABLE%';

-- MySQL: Kill query
KILL QUERY <process_id>;
```

### Restore from Backup

```bash
# PostgreSQL
pg_restore -d mydb backup.dump

# MySQL
mysql mydb < backup.sql

# Point-in-time recovery
pg_restore --target-time="2024-01-13 10:00:00" backup.dump
```

### Partial Rollback

For expand-contract migrations:

```sql
-- If contract phase failed, stay expanded
-- Just fix the code to use old column again
-- No schema rollback needed
```

---

## Rollback Decision Tree

```
Migration Failed?
│
├─ Schema change incomplete?
│  └─ Run down migration
│
├─ Data corruption?
│  └─ Restore from backup
│
├─ Performance degradation?
│  └─ Drop new indexes, revert queries
│
├─ Application errors?
│  └─ Rollback application, then schema
│
└─ Partial failure?
   └─ Fix forward if possible, else full rollback
```

---

## Post-Rollback Actions

1. **Investigate root cause**
   - Check logs for errors
   - Review migration script
   - Analyze query plans

2. **Document the failure**
   - What failed
   - Why it failed
   - How it was resolved

3. **Fix and retest**
   - Modify migration
   - Test on staging
   - Add more validation

4. **Communicate**
   - Team notification
   - Incident report
   - Lessons learned

---

## Rollback Testing

```javascript
describe('Migration Rollback', () => {
  it('should successfully roll back', async () => {
    // Apply migration
    await knex.migrate.up();

    // Verify up state
    expect(await tableExists('new_table')).toBe(true);

    // Roll back
    await knex.migrate.down();

    // Verify rolled back
    expect(await tableExists('new_table')).toBe(false);
  });
});
```

---

## Checklist

- [ ] Every migration has a tested rollback
- [ ] Backups taken before production migrations
- [ ] Rollback procedures documented
- [ ] Team knows emergency procedures
- [ ] Monitoring alerts configured
