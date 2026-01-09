---
tool: claude-code
description: Validate implementation before shipping
allowed-tools: Bash, Read, Glob
argument-hint: [--only=types,lint,tests,build]
---

# Validate Command

Run automated checks: types, lint, tests, build.

**Workflow:** `/slop` (optional) → `/review` → `/validate` → `/ship`

## Flags

- `--only=X,Y` - Run only specific checks (types, lint, tests, build)

## 1. Detect Tech Stack

Check for config files to determine project type:

| File | Stack |
|------|-------|
| `package.json` | Node.js |
| `tsconfig.json` | TypeScript |
| `pyproject.toml` / `requirements.txt` | Python |
| `Cargo.toml` | Rust |
| `go.mod` | Go |

Use Glob to detect before running checks.

## 2. Run Checks

For each detected stack, run applicable checks. Track pass/fail status for each.

### TypeScript/Node.js

**Types** (if tsconfig.json exists):
```bash
npx tsc --noEmit
```

**Lint** (if lint script exists in package.json):
```bash
npm run lint
```

**Tests**:
```bash
npm test
```

**Build** (if build script exists):
```bash
npm run build
```

### Python

**Lint**:
```bash
ruff check . || flake8 .
```

**Types** (if configured):
```bash
mypy . || pyright .
```

**Tests**:
```bash
pytest -q
```

### Rust

**Check**:
```bash
cargo check
```

**Clippy**:
```bash
cargo clippy -- -D warnings
```

**Tests**:
```bash
cargo test
```

### Go

**Build**:
```bash
go build ./...
```

**Vet**:
```bash
go vet ./...
```

**Tests**:
```bash
go test ./...
```

## 3. Handle Results

For each check:
- **Passed**: Mark as ✅
- **Failed**: Mark as ❌, capture error output
- **Skipped**: Mark as ⏭️ (not applicable or --only filtered)

**Important:** Don't swallow errors. If a check fails, report it clearly.

## Report Format

```
## Validation Report

**Stack:** [detected languages/frameworks]

| Check | Status | Details |
|-------|--------|---------|
| Types | ✅ / ❌ / ⏭️ | [error summary if failed] |
| Lint | ✅ / ❌ / ⏭️ | [error summary if failed] |
| Tests | ✅ (N passed) / ❌ (N failed) / ⏭️ | [failure details] |
| Build | ✅ / ❌ / ⏭️ | [error summary if failed] |

### Summary
**READY TO SHIP** / **NEEDS FIXES**

[If needs fixes, list what to fix]
```

## Next Steps

- **All passed:** `/ship` to commit
- **Failures:** Fix issues and re-run `/validate`
