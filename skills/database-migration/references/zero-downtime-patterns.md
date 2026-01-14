# Zero-Downtime Migration Patterns

Strategies for schema changes without service interruption.

## The Expand-Contract Pattern

The fundamental pattern for safe migrations.

### Phase 1: Expand
Add new structures alongside existing ones.

```sql
-- Add new column (nullable)
ALTER TABLE orders ADD COLUMN status_v2 VARCHAR(50);
```

### Phase 2: Migrate
Update code to write to both old and new.

```javascript
// Write to both during transition
await db.orders.update(id, {
  status: newStatus,      // Old column
  status_v2: newStatus    // New column
});
```

### Phase 3: Backfill
Copy data from old to new.

```sql
UPDATE orders SET status_v2 = status WHERE status_v2 IS NULL;
```

### Phase 4: Switch
Update code to read from new.

```javascript
// Read from new column
const status = order.status_v2;
```

### Phase 5: Contract
Remove old structure after verification.

```sql
ALTER TABLE orders DROP COLUMN status;
ALTER TABLE orders RENAME COLUMN status_v2 TO status;
```

---

## Adding Columns

### Safe: Nullable Column
```sql
-- Always safe - no locking issues
ALTER TABLE users ADD COLUMN preferences JSONB;
```

### Risky: NOT NULL Without Default
```sql
-- DANGEROUS: Requires table rewrite
ALTER TABLE users ADD COLUMN created_at TIMESTAMP NOT NULL;

-- SAFE: Add with default first
ALTER TABLE users ADD COLUMN created_at TIMESTAMP DEFAULT NOW();
-- Then add NOT NULL constraint after backfill
```

---

## Removing Columns

### Step 1: Stop Writing
```javascript
// Remove from all writes
await user.save(); // No longer includes deprecated_field
```

### Step 2: Stop Reading
```javascript
// Remove from all reads
const user = await User.findById(id);
// Don't access user.deprecated_field
```

### Step 3: Drop Column
```sql
-- Only after code deployed everywhere
ALTER TABLE users DROP COLUMN deprecated_field;
```

---

## Renaming Tables

```sql
-- Step 1: Create new table
CREATE TABLE customers (LIKE users INCLUDING ALL);

-- Step 2: Create view with old name
CREATE VIEW users AS SELECT * FROM customers;

-- Step 3: Copy data
INSERT INTO customers SELECT * FROM users_old;

-- Step 4: Set up trigger for sync during transition
CREATE TRIGGER sync_users
AFTER INSERT OR UPDATE ON customers
FOR EACH ROW EXECUTE FUNCTION sync_to_users();

-- Step 5: After all code updated, drop view
DROP VIEW users;
DROP TABLE users_old;
```

---

## Adding Foreign Keys

```sql
-- Step 1: Add column without constraint
ALTER TABLE orders ADD COLUMN customer_id INTEGER;

-- Step 2: Backfill
UPDATE orders o SET customer_id = (
  SELECT id FROM customers c WHERE c.legacy_id = o.legacy_customer_id
);

-- Step 3: Add constraint (validate later)
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id) REFERENCES customers(id)
NOT VALID;  -- Don't validate existing rows yet

-- Step 4: Validate in background (PostgreSQL)
ALTER TABLE orders VALIDATE CONSTRAINT fk_customer;
```

---

## Index Changes

### Adding Index (Non-Blocking)
```sql
-- PostgreSQL
CREATE INDEX CONCURRENTLY idx_orders_date ON orders(created_at);

-- MySQL 5.6+
ALTER TABLE orders ADD INDEX idx_date (created_at),
  ALGORITHM=INPLACE, LOCK=NONE;
```

### Removing Index
```sql
-- Safe: Indexes can be dropped anytime
DROP INDEX CONCURRENTLY idx_old_index;
```

---

## Data Type Changes

### Widening (Safe)
```sql
-- VARCHAR(50) to VARCHAR(100) - usually safe
ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(100);
```

### Narrowing (Dangerous)
```sql
-- Must verify no data truncation
-- Check first:
SELECT MAX(LENGTH(name)) FROM users;

-- Then alter if safe
ALTER TABLE users ALTER COLUMN name TYPE VARCHAR(50);
```

### Type Conversion
```sql
-- Use expand-contract
ALTER TABLE users ADD COLUMN age_int INTEGER;
UPDATE users SET age_int = CAST(age_str AS INTEGER);
ALTER TABLE users DROP COLUMN age_str;
ALTER TABLE users RENAME COLUMN age_int TO age;
```

---

## Large Table Considerations

For tables with millions of rows:

### Batch Updates
```sql
-- Update in batches to avoid long locks
DO $$
DECLARE
  batch_size INT := 10000;
  affected INT;
BEGIN
  LOOP
    UPDATE orders
    SET status_v2 = status
    WHERE id IN (
      SELECT id FROM orders
      WHERE status_v2 IS NULL
      LIMIT batch_size
    );

    GET DIAGNOSTICS affected = ROW_COUNT;
    EXIT WHEN affected = 0;

    COMMIT;
    PERFORM pg_sleep(0.1); -- Brief pause
  END LOOP;
END $$;
```

### Online Schema Change Tools
- **pt-online-schema-change** (MySQL)
- **gh-ost** (MySQL)
- **pgroll** (PostgreSQL)

---

## Checklist

- [ ] Migration is backward compatible
- [ ] Rollback plan documented
- [ ] Tested with production-like data volume
- [ ] Monitoring in place for query performance
- [ ] Team notified of migration window
