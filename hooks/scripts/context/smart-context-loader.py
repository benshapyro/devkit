#!/usr/bin/env python3
"""
Smart context loader hook.

Analyzes user prompts and injects relevant project context.
Runs on UserPromptSubmit event.

Exit codes:
  0 = No keywords found, prompt unchanged
  3 = Context injected, prompt modified
"""

import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Optional

# Add lib to path for imports
DEVKIT_PATH = os.environ.get("CLAUDE_DEVKIT", str(Path.home() / ".claude" / "devkit"))
sys.path.insert(0, DEVKIT_PATH)

try:
    from lib.core.config import is_extension_enabled, get_extension_option
    from lib.core.output import is_ci
except ImportError:
    def is_extension_enabled(name: str, settings=None) -> bool:
        return True

    def get_extension_option(name: str, option: str, default=None, settings=None):
        return default

    def is_ci() -> bool:
        return any(os.getenv(v) for v in ["CI", "GITHUB_ACTIONS", "GITLAB_CI"])


# Debug mode
DEBUG = os.environ.get("CLAUDE_HOOK_DEBUG") == "1"


def debug(msg: str) -> None:
    """Print debug message if debug mode enabled."""
    if DEBUG:
        print(f"[DEBUG] {msg}", file=sys.stderr)


# Default keyword mappings
DEFAULT_KEYWORD_MAPPINGS = {
    "auth": ["src/auth/", "auth/", "login", "session", "authentication", "oauth"],
    "api": ["src/api/", "api/", "routes/", "controllers/", "endpoints/", "handlers/"],
    "database": ["migrations/", "models/", "schema", "queries/", "repositories/"],
    "test": ["tests/", "__tests__/", "test_", ".test.", ".spec."],
    "config": [".env", "config/", "settings", "configuration"],
    "build": ["webpack", "vite", "rollup", "esbuild", "build/"],
    "deploy": ["docker", "k8s", "kubernetes", "terraform", ".github/workflows", "ci/"],
    "frontend": ["components/", "pages/", "views/", "ui/", "src/app/"],
    "backend": ["server/", "services/", "middleware/"],
    "security": ["auth/", "crypto", "encryption", "security/"],
}


def get_keyword_mappings() -> dict[str, list[str]]:
    """Get keyword mappings including custom ones."""
    mappings = DEFAULT_KEYWORD_MAPPINGS.copy()

    # Add custom keywords from config
    custom = get_extension_option(
        "smart-context-loader",
        "customKeywords",
        default={},
    )

    if isinstance(custom, dict):
        mappings.update(custom)

    return mappings


def extract_keywords(prompt: str) -> list[str]:
    """Extract relevant keywords from prompt."""
    prompt_lower = prompt.lower()
    mappings = get_keyword_mappings()
    found = []

    for category in mappings.keys():
        if category in prompt_lower:
            debug(f"Found keyword: {category}")
            found.append(category)

    return found


def run_command(args: list[str], timeout: float = 1.0) -> Optional[str]:
    """Run a command and return stdout, or None on failure."""
    try:
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        debug(f"Command failed: {args[0]} - {e}")
    return None


def find_relevant_files(keywords: list[str], limit: int = 5) -> list[str]:
    """Find files relevant to the keywords using git ls-files."""
    mappings = get_keyword_mappings()
    relevant = set()

    for keyword in keywords:
        patterns = mappings.get(keyword, [])
        for pattern in patterns:
            # Use git ls-files with glob pattern
            output = run_command(["git", "ls-files", f"*{pattern}*"])
            if output:
                files = [f for f in output.split("\n") if f and not f.startswith(".")]
                relevant.update(files[:3])  # Limit per pattern

            if len(relevant) >= limit:
                break

    return sorted(list(relevant))[:limit]


def get_recent_changes(keywords: list[str], limit: int = 5) -> list[str]:
    """Get recent git commits related to keywords."""
    changes = []

    for keyword in keywords:
        output = run_command([
            "git", "log", "--oneline", "-3", f"--grep={keyword}"
        ])
        if output:
            commits = [c for c in output.split("\n") if c]
            changes.extend(commits)

        if len(changes) >= limit:
            break

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for c in changes:
        if c not in seen:
            seen.add(c)
            unique.append(c)

    return unique[:limit]


def get_todos(keywords: list[str], limit: int = 3) -> list[str]:
    """Find TODO comments in files related to keywords."""
    mappings = get_keyword_mappings()
    todos = []

    for keyword in keywords:
        patterns = mappings.get(keyword, [])
        for pattern in patterns:
            # Use git grep for TODOs in relevant files
            output = run_command([
                "git", "grep", "-n", "-i", "TODO",
                "--", f"*{pattern}*"
            ], timeout=1.5)

            if output:
                matches = [m for m in output.split("\n") if m]
                # Truncate long TODO lines
                for match in matches[:2]:
                    if len(match) > 100:
                        match = match[:97] + "..."
                    todos.append(match)

            if len(todos) >= limit:
                break

        if len(todos) >= limit:
            break

    return todos[:limit]


def build_context(
    relevant_files: list[str],
    recent_changes: list[str],
    todos: list[str]
) -> str:
    """Build context string to inject."""
    parts = ["[Auto-loaded context]"]

    if relevant_files:
        files_str = ", ".join(relevant_files)
        parts.append(f"\nRelevant files: {files_str}")

    if recent_changes:
        changes_str = "\n".join(f"  - {c}" for c in recent_changes)
        parts.append(f"\nRecent changes:\n{changes_str}")

    if todos:
        todos_str = "\n".join(f"  - {t}" for t in todos)
        parts.append(f"\nTODOs found:\n{todos_str}")

    return "\n".join(parts)


def main() -> None:
    """Main entry point for the hook."""
    # Check if extension is enabled
    if not is_extension_enabled("smart-context-loader"):
        debug("Extension disabled, exiting")
        sys.exit(0)

    # Read hook input from stdin
    try:
        hook_input = json.loads(sys.stdin.read())
    except json.JSONDecodeError as e:
        debug(f"Failed to parse hook input: {e}")
        sys.exit(0)

    prompt = hook_input.get("prompt", "")
    if not prompt:
        debug("No prompt provided")
        sys.exit(0)

    debug(f"Analyzing prompt: {prompt[:100]}...")

    # Extract keywords from prompt
    keywords = extract_keywords(prompt)

    if not keywords:
        debug("No keywords found")
        sys.exit(0)

    debug(f"Keywords found: {keywords}")

    # Get config options
    max_files = get_extension_option("smart-context-loader", "maxFiles", default=5)
    max_commits = get_extension_option("smart-context-loader", "maxCommits", default=5)
    max_todos = get_extension_option("smart-context-loader", "maxTodos", default=3)

    # Gather context
    relevant_files = find_relevant_files(keywords, limit=max_files)
    recent_changes = get_recent_changes(keywords, limit=max_commits)
    todos = get_todos(keywords, limit=max_todos)

    debug(f"Found {len(relevant_files)} files, {len(recent_changes)} commits, {len(todos)} TODOs")

    # If no context found, exit without modification
    if not any([relevant_files, recent_changes, todos]):
        debug("No context found")
        sys.exit(0)

    # Build context and modify prompt
    context = build_context(relevant_files, recent_changes, todos)
    modified_prompt = f"{context}\n\n{prompt}"

    # Output modified prompt
    output = {"prompt": modified_prompt}
    print(json.dumps(output))

    # Exit code 3 = modify input
    sys.exit(3)


if __name__ == "__main__":
    main()
