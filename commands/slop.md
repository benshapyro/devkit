---
tool: claude-code
description: Remove AI-generated code slop from current branch
allowed-tools: Bash(git:*), Read, Edit, Grep, Glob
argument-hint: "[--dry-run]"
---

# Slop Command

Clean AI-generated code artifacts from your branch to match existing code style.

**Workflow:** [implement] → `/slop` → `/review` → `/validate` → `/ship`

## Flags

- `--dry-run` - Show what would be changed without making edits

## What is "Slop"?

AI code tells that make it look unnatural:

### 1. Over-Commenting
```typescript
// BAD
// Get the user from the database
const user = await db.getUser(id); // Fetch user by ID

// GOOD - self-documenting
const user = await db.getUser(id);
```

### 2. Defensive Overkill
```typescript
// BAD - redundant when TypeScript enforces types
function processUser(user: User) {
  if (!user) throw new Error('User is required');
  if (!user.id) throw new Error('User must have an id');
}

// GOOD - trust internal callers, validate at boundaries
function processUser(user: User) {
  // TypeScript guarantees user exists and has id
}
```

### 3. Type Escapes
```typescript
// BAD
const data = response as any;

// GOOD - fix the actual type
const data: ResponseType = response;
```

### 4. Unnecessary Try/Catch
```typescript
// BAD - wrapping non-throwing code
try {
  return a + b;
} catch (error) {
  console.error('Failed to add numbers', error);
  throw error;
}

// GOOD
return a + b;
```

### 5. Verbose Logging
```typescript
// BAD
console.log('Starting process...');
console.log('Processing...');
console.log('Done!');

// GOOD - log meaningful events only
```

### 6. Style Inconsistency
- JSDoc when file doesn't use it
- Different naming conventions
- Different import organization

## Workflow

### 1. Detect Default Branch

```bash
git symbolic-ref refs/remotes/origin/HEAD 2>/dev/null | sed 's@^refs/remotes/origin/@@' || echo "main"
```

### 2. Get Changed Files

```bash
git diff [default-branch]...HEAD --name-only
```

### 3. For Each Changed File

1. **Read the FULL file** to understand existing patterns
2. Compare new code against existing style
3. Identify slop patterns

### 4. Fix (or Report in --dry-run)

Remove or adjust:
- Unnecessary comments (keep business logic explanations)
- Redundant validation (keep boundary validation)
- Type escapes (fix properly)
- Pointless try/catch (keep intentional error handling)
- Excessive logging (match existing patterns)

### 5. Report

**Standard mode:** Brief summary of changes made
```
Cleaned 3 files:
- UserService.ts: Removed 4 comments, 2 redundant null checks
- PaymentController.ts: Fixed 1 `any` cast
- utils.ts: Removed try/catch wrapper (caller handles errors)
```

**Dry-run mode:** List what would change without editing
```
Would change 3 files:
- UserService.ts:23 - Remove comment "// Get user"
- UserService.ts:45 - Remove null check (TypeScript enforces)
...
```

## What NOT to Remove

- Comments explaining non-obvious business logic
- Validation at system boundaries (user input, external APIs)
- Error handling that matches existing patterns
- Logging that matches existing patterns
- Type assertions that are genuinely necessary

## Conservative Approach

When unsure, leave it. Better to keep something questionable than remove something important.

After running, verify changes make sense:
```bash
git diff
```
