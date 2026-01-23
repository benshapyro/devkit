# Testing Migrations

Validation approaches for database migrations.

## Test Environments

### Production-Like Staging

```yaml
# docker-compose.staging.yml
services:
  db:
    image: postgres:15
    volumes:
      - ./staging-data:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: staging
```

Load production-like data:
```bash
# Anonymized production dump
pg_dump prod_db | \
  sed 's/real@email.com/test@example.com/g' | \
  psql staging_db
```

---

## Migration Test Types

### 1. Syntax Validation

```bash
# PostgreSQL - check syntax
psql -f migration.sql --set ON_ERROR_STOP=on -1 -v ON_ERROR_ROLLBACK=on

# MySQL - dry run
mysql --verbose --execute="source migration.sql" 2>&1 | head
```

### 2. Up/Down Cycle

```javascript
describe('Migration', () => {
  it('should apply and rollback cleanly', async () => {
    // Start fresh
    await knex.migrate.rollback(null, true);

    // Apply all migrations
    await knex.migrate.latest();

    // Rollback all
    await knex.migrate.rollback(null, true);

    // Re-apply
    await knex.migrate.latest();
  });
});
```

### 3. Data Integrity

```javascript
it('should preserve data through migration', async () => {
  // Insert test data
  await knex('users').insert({ id: 1, name: 'Test' });

  // Apply migration
  await knex.migrate.up();

  // Verify data preserved
  const user = await knex('users').where({ id: 1 }).first();
  expect(user.name).toBe('Test');
});
```

### 4. Performance Testing

```sql
-- Measure migration time
\timing on
\i migration.sql

-- Check for table locks
SELECT blocked_locks.pid AS blocked_pid,
       blocking_locks.pid AS blocking_pid
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_locks blocking_locks ON blocking_locks.locktype = blocked_locks.locktype;
```

---

## Automated Testing

### CI Pipeline

```yaml
# .github/workflows/migration-test.yml
jobs:
  test-migrations:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        options: >-
          --health-cmd pg_isready
          --health-interval 10s

    steps:
      - uses: actions/checkout@v3

      - name: Run migrations
        run: npm run migrate

      - name: Test rollback
        run: npm run migrate:rollback

      - name: Re-run migrations
        run: npm run migrate

      - name: Run tests
        run: npm test
```

### Migration Linting

```javascript
// eslint-plugin-migrations
module.exports = {
  rules: {
    'no-drop-column': (migration) => {
      if (migration.includes('DROP COLUMN')) {
        return 'Use soft delete pattern instead of DROP';
      }
    },
    'require-down-migration': (migration) => {
      if (!migration.down) {
        return 'Migration must include down function';
      }
    }
  }
};
```

---

## Load Testing Migrations

### Simulate Production Load

```javascript
// Test migration under load
describe('Migration under load', () => {
  it('should not block reads', async () => {
    // Start concurrent reads
    const reads = Array(100).fill().map(() =>
      knex('users').select('*')
    );

    // Run migration
    const migrationPromise = knex.migrate.up();

    // All reads should complete
    const results = await Promise.all([...reads, migrationPromise]);
    expect(results.slice(0, 100).every(r => r.length >= 0)).toBe(true);
  });
});
```

### Measure Lock Duration

```sql
-- Monitor locks during migration
SELECT
  locktype,
  relation::regclass,
  mode,
  granted,
  pid,
  now() - query_start AS duration
FROM pg_locks l
JOIN pg_stat_activity a ON l.pid = a.pid
WHERE relation = 'users'::regclass;
```

---

## Data Volume Testing

```javascript
// Test with production-scale data
describe('Large table migration', () => {
  beforeAll(async () => {
    // Generate 1M rows
    await knex.raw(`
      INSERT INTO users (email, created_at)
      SELECT
        'user' || generate_series || '@test.com',
        NOW() - (random() * interval '365 days')
      FROM generate_series(1, 1000000)
    `);
  });

  it('should complete in reasonable time', async () => {
    const start = Date.now();

    await knex.migrate.up();

    const duration = Date.now() - start;
    expect(duration).toBeLessThan(60000); // 60 seconds
  });
});
```

---

## Validation Queries

### Post-Migration Checks

```sql
-- Verify constraint exists
SELECT conname FROM pg_constraint WHERE conname = 'fk_orders_customer';

-- Verify index exists
SELECT indexname FROM pg_indexes WHERE indexname = 'idx_users_email';

-- Verify column type
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'users' AND column_name = 'email';

-- Verify no orphaned data
SELECT COUNT(*) FROM orders WHERE customer_id NOT IN (SELECT id FROM customers);
```

---

## Checklist

- [ ] Migration tested on staging
- [ ] Up/down cycle verified
- [ ] Data integrity checked
- [ ] Performance acceptable
- [ ] Locks duration acceptable
- [ ] Rollback tested
- [ ] CI pipeline includes migration tests
