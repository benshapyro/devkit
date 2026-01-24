---
tool: claude-code
description: Analyze code changes to identify blast radius - all files, functions, and tests that might be affected
allowed-tools: Read, Grep, Glob, Bash(git:*)
argument-hint: "[files...]"
---

# /regression-scan

Understand the impact of your changes before committing.

## Usage

```
/regression-scan [files...]
```

If no files specified, analyzes current git diff.

## Process

### 1. Identify Changed Code

**Get changed files:**
```bash
git diff --name-only HEAD
git diff --name-only --cached
```

**If files provided as arguments, use those instead.**

For each changed file, extract:
- Modified functions/methods
- Changed class definitions
- API signature changes
- Export changes

### 2. Build Dependency Graph

**Find files that import changed modules:**

For JavaScript/TypeScript:
```
Grep: import.*from ['"].*{changed_file}['"]
Grep: require\(['"].*{changed_file}['"]\)
```

For Python:
```
Grep: from {module} import
Grep: import {module}
```

**Find callers of changed functions:**
```
Grep: {function_name}\s*\(
```

**Check for database schema impacts:**
```
Glob: **/migrations/*.{sql,py,ts}
Grep: {table_name}|{column_name}
```

### 3. Find Affected Tests

**Direct test files:**
```
Glob: **/__tests__/{changed_file_name}*
Glob: **/test_{changed_file_name}*
Glob: **/{changed_file_name}.test.*
Glob: **/{changed_file_name}.spec.*
```

**Integration tests that import changed modules:**
```
Grep in test files: import.*{changed_module}
```

**E2E tests covering affected flows:**
```
Glob: **/e2e/**/*.{ts,js,py}
Grep: {feature_name}|{endpoint}
```

### 4. Identify Code Owners

**Get recent authors:**
```bash
git log --format='%an' -5 -- {file} | sort | uniq
```

**Check CODEOWNERS file:**
```
Read: .github/CODEOWNERS
```

### 5. Assess Risk Level

| Factor | Low | Medium | High |
|--------|-----|--------|------|
| Files affected | <5 | 5-15 | >15 |
| Function signature changes | None | Internal only | Public API |
| Test coverage | >80% | 50-80% | <50% |
| Database changes | None | Additive | Destructive |

### 6. Generate Impact Report

```markdown
## Blast Radius Analysis

**Analyzed:** {files}
**Scan Date:** {timestamp}

---

### Direct Changes

| File | Changes | Risk |
|------|---------|------|
| {file} | `{function}()` signature changed | 🟡 |
| {file} | New export added | 🟢 |
| {file} | Breaking: removed parameter | 🔴 |

---

### Dependency Graph

**{changed_file}** is imported by:
```
├── src/api/users.ts (direct)
│   ├── src/routes/user-routes.ts
│   └── src/controllers/user-controller.ts
├── src/middleware/auth.ts (direct)
└── tests/auth.test.ts (test)
```

---

### Affected Files ({count})

| File | Relationship | Impact |
|------|--------------|--------|
| {file} | imports {module} | Must update import |
| {file} | calls {function} | Verify compatibility |
| {file} | extends {class} | Check inheritance |

---

### Tests to Run

**Priority 1 - Directly affected:**
- [ ] `{test_file}` - tests modified code
- [ ] `{test_file}` - tests modified code

**Priority 2 - Integration:**
- [ ] `{test_file}` - imports affected module
- [ ] `{test_file}` - covers affected flow

**Priority 3 - E2E (if time permits):**
- [ ] `{test_file}` - covers feature area

**Quick test command:**
```bash
npm test -- --findRelatedTests {files}
# or
pytest {test_files}
```

---

### Breaking Change Assessment

| Change | Severity | Affected Consumers |
|--------|----------|-------------------|
| {description} | 🔴 BREAKING | {count} files |
| {description} | 🟡 CAUTION | {count} files |

---

### Suggested Reviewers

Based on code ownership and recent activity:
- **@{username}** - owns `{path}/`
- **@{username}** - last modified `{file}`
- **@{username}** - expert in `{area}`

---

### Recommendations

1. **Before committing:**
   - [ ] Run priority 1 tests
   - [ ] Update affected imports if API changed
   - [ ] Add migration notes if breaking

2. **For review:**
   - [ ] Request review from suggested owners
   - [ ] Highlight breaking changes in PR description

3. **Risk mitigation:**
   - [ ] Consider feature flag for gradual rollout
   - [ ] Prepare rollback plan
```

## Example

```
/regression-scan src/auth/controller.ts
```

Outputs analysis of all files affected by changes to the auth controller.

## Notes

- Prioritizes breadth over depth - shows full blast radius
- Uses static analysis - may miss dynamic imports
- Suggests but doesn't run tests automatically
- Works best with well-structured codebases with clear imports
