# Migration Tool Comparison

Overview of popular database migration tools.

## JavaScript/TypeScript

### Prisma Migrate
```bash
npx prisma migrate dev --name add_users_table
npx prisma migrate deploy
```

**Pros:**
- Type-safe schema
- Auto-generated migrations
- Great developer experience

**Cons:**
- Less control over SQL
- PostgreSQL-focused
- Schema drift issues possible

### Knex.js
```javascript
// migrations/20240113_create_users.js
exports.up = function(knex) {
  return knex.schema.createTable('users', table => {
    table.increments('id');
    table.string('email').unique();
    table.timestamps(true, true);
  });
};

exports.down = function(knex) {
  return knex.schema.dropTable('users');
};
```

```bash
npx knex migrate:latest
npx knex migrate:rollback
```

**Pros:**
- Full SQL control
- Multi-database support
- Mature ecosystem

**Cons:**
- Manual migration writing
- No type safety

### TypeORM
```typescript
// migrations/1705123456-CreateUsers.ts
export class CreateUsers1705123456 implements MigrationInterface {
  async up(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.createTable(new Table({
      name: 'users',
      columns: [
        { name: 'id', type: 'int', isPrimary: true },
        { name: 'email', type: 'varchar', isUnique: true }
      ]
    }));
  }

  async down(queryRunner: QueryRunner): Promise<void> {
    await queryRunner.dropTable('users');
  }
}
```

---

## Python

### Alembic (SQLAlchemy)
```python
# migrations/versions/abc123_create_users.py
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(255), unique=True)
    )

def downgrade():
    op.drop_table('users')
```

```bash
alembic upgrade head
alembic downgrade -1
```

**Pros:**
- Powerful SQLAlchemy integration
- Auto-generate from models
- Flexible

**Cons:**
- Steeper learning curve
- Configuration complexity

### Django Migrations
```python
# Auto-generated from models
python manage.py makemigrations
python manage.py migrate
```

**Pros:**
- Automatic from models
- Built into Django
- Easy to use

**Cons:**
- Django-only
- Less control

---

## Java

### Flyway
```sql
-- V1__Create_users.sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE
);
```

```bash
flyway migrate
flyway info
flyway repair
```

**Pros:**
- Convention over configuration
- Plain SQL migrations
- Excellent versioning

**Cons:**
- Java/JVM required
- Undo requires paid version

### Liquibase
```xml
<!-- changelog.xml -->
<changeSet id="1" author="dev">
  <createTable tableName="users">
    <column name="id" type="int" autoIncrement="true">
      <constraints primaryKey="true"/>
    </column>
    <column name="email" type="varchar(255)">
      <constraints unique="true"/>
    </column>
  </createTable>
</changeSet>
```

**Pros:**
- Multiple formats (XML, YAML, SQL)
- Rollback support
- Diff generation

**Cons:**
- Verbose syntax
- Complex for simple needs

---

## Database-Specific

### pgroll (PostgreSQL)
```json
{
  "name": "add_email",
  "operations": [
    {
      "add_column": {
        "table": "users",
        "column": {
          "name": "email",
          "type": "varchar(255)"
        }
      }
    }
  ]
}
```

**Pros:**
- Zero-downtime by design
- Automatic expand-contract
- Version-based migrations

### gh-ost (MySQL)
```bash
gh-ost \
  --alter="ADD COLUMN phone VARCHAR(20)" \
  --database=mydb \
  --table=users \
  --execute
```

**Pros:**
- Online schema change
- Minimal locking
- Pausable/resumable

---

## Comparison Table

| Tool | Language | Auto-generate | Rollback | Zero-Downtime |
|------|----------|---------------|----------|---------------|
| Prisma | JS/TS | Yes | Limited | No |
| Knex | JS/TS | No | Yes | Manual |
| Alembic | Python | Yes | Yes | Manual |
| Django | Python | Yes | Limited | Manual |
| Flyway | Java | No | Paid | Manual |
| Liquibase | Java | Yes | Yes | Manual |
| pgroll | Any | No | Yes | Yes |
| gh-ost | Any | No | Yes | Yes |

---

## Recommendation

| Use Case | Recommended Tool |
|----------|-----------------|
| TypeScript + PostgreSQL | Prisma |
| Multi-database JS | Knex |
| Python + SQLAlchemy | Alembic |
| Django project | Django Migrations |
| Java enterprise | Flyway |
| Zero-downtime PostgreSQL | pgroll |
| Zero-downtime MySQL | gh-ost |
