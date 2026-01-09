---
tool: claude-code
event: PreToolUse
matcher: Read|Edit|Write
type: command
command: python3 "$HOME/.claude/hooks/security/sensitive-file-guard.py"
---

# Sensitive File Guard

Prevents access to sensitive files containing credentials or secrets.

## Behavior

- Intercepts Read, Edit, and Write tool calls
- Checks file path against sensitive patterns
- Exit code 2 blocks access, 0 allows

## Blocked Files

| Type | Examples |
|------|----------|
| Environment files | `.env`, `.env.local`, `.env.production` |
| Credentials | `credentials.json`, `secrets.yaml` |
| SSH keys | `id_rsa`, `id_ed25519`, `.pem`, `.key` |
| Config files | `.netrc`, `.npmrc`, `.pypirc` |
| Sensitive dirs | `.ssh/`, `.aws/`, `.gnupg/`, `.kube/` |

## Allowed (Safe Suffixes)

Files ending with these are allowed:
- `.example`
- `.sample`
- `.template`
- `.dist`

## Debug

Set `CLAUDE_HOOK_DEBUG=1` to enable verbose logging.

## Exit Codes

- `0` = Allow access
- `2` = Block access (PreToolUse convention)

## Script Location

`scripts/security/sensitive-file-guard.py`
