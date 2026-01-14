#!/usr/bin/env python3
"""
Test coverage enforcer hook.

Checks if new/changed source code has corresponding tests.
Uses delta coverage approach - only checks new code, ignores legacy gaps.

Exit codes:
  0 = Test file exists or file skipped
  1 = Test file missing (non-blocking warning)
"""

import json
import os
import sys
from pathlib import Path
from typing import Optional

# Add lib to path for imports
DEVKIT_PATH = os.environ.get("CLAUDE_DEVKIT", str(Path.home() / ".claude" / "devkit"))
sys.path.insert(0, DEVKIT_PATH)

try:
    from lib.core.output import severity_badge, is_ci
    from lib.core.config import is_extension_enabled, get_extension_option
except ImportError:
    # Fallback if core library not available
    def severity_badge(level: str, plain_text: bool = False) -> str:
        badges = {
            "critical": "[CRITICAL]",
            "high": "[HIGH]",
            "medium": "[MEDIUM]",
            "low": "[LOW]",
            "info": "[INFO]",
        }
        return badges.get(level.lower(), "[INFO]")

    def is_ci() -> bool:
        return any(os.getenv(v) for v in ["CI", "GITHUB_ACTIONS", "GITLAB_CI"])

    def is_extension_enabled(name: str, settings=None) -> bool:
        return True

    def get_extension_option(name: str, option: str, default=None, settings=None):
        return default


# Debug mode
DEBUG = os.environ.get("CLAUDE_HOOK_DEBUG") == "1"


def debug(msg: str) -> None:
    """Print debug message if debug mode enabled."""
    if DEBUG:
        print(f"[DEBUG] {msg}", file=sys.stderr)


# Test file patterns by source extension
SOURCE_PATTERNS = {
    ".py": [
        "tests/test_{name}.py",
        "tests/{name}_test.py",
        "{dir}/test_{name}.py",
        "test_{name}.py",
        "{name}_test.py",
    ],
    ".ts": [
        "__tests__/{name}.test.ts",
        "{name}.test.ts",
        "{name}.spec.ts",
        "{dir}/__tests__/{name}.test.ts",
        "tests/{name}.test.ts",
    ],
    ".tsx": [
        "__tests__/{name}.test.tsx",
        "{name}.test.tsx",
        "{name}.spec.tsx",
        "{dir}/__tests__/{name}.test.tsx",
        "tests/{name}.test.tsx",
    ],
    ".js": [
        "__tests__/{name}.test.js",
        "{name}.test.js",
        "{name}.spec.js",
        "{dir}/__tests__/{name}.test.js",
        "tests/{name}.test.js",
    ],
    ".jsx": [
        "__tests__/{name}.test.jsx",
        "{name}.test.jsx",
        "{name}.spec.jsx",
        "{dir}/__tests__/{name}.test.jsx",
        "tests/{name}.test.jsx",
    ],
}

# Patterns to skip
SKIP_PATTERNS = [
    "test",
    "spec",
    "__tests__",
    ".claude",
    "node_modules",
    ".git",
    "dist",
    "build",
    "coverage",
]

# File patterns to skip (in addition to test files)
SKIP_FILE_PATTERNS = [
    ".config.",
    ".d.ts",
    "index.",
    "__init__",
    "setup.py",
    "conftest.py",
]


def should_skip_file(file_path: str) -> bool:
    """Check if file should be skipped from coverage check."""
    path = Path(file_path)
    path_str = str(path).lower()

    # Skip based on path patterns
    for pattern in SKIP_PATTERNS:
        if pattern in path_str:
            debug(f"Skipping {file_path}: matches skip pattern '{pattern}'")
            return True

    # Skip based on file patterns
    for pattern in SKIP_FILE_PATTERNS:
        if pattern in path.name.lower():
            debug(f"Skipping {file_path}: matches file pattern '{pattern}'")
            return True

    # Skip non-source extensions
    if path.suffix not in SOURCE_PATTERNS:
        debug(f"Skipping {file_path}: not a tracked source extension")
        return True

    # Check custom skip patterns from config
    custom_patterns = get_extension_option(
        "test-coverage-enforcer",
        "skipPatterns",
        default=[],
    )
    for pattern in custom_patterns:
        import fnmatch
        if fnmatch.fnmatch(path.name, pattern):
            debug(f"Skipping {file_path}: matches custom pattern '{pattern}'")
            return True

    return False


def find_test_file(source_file: str) -> Optional[str]:
    """
    Find corresponding test file for a source file.

    Args:
        source_file: Path to source file

    Returns:
        Path to test file if found, None otherwise
    """
    path = Path(source_file)
    ext = path.suffix
    name = path.stem
    dir_path = path.parent

    if ext not in SOURCE_PATTERNS:
        return None

    patterns = SOURCE_PATTERNS[ext]

    for pattern in patterns:
        # Substitute placeholders
        test_path_str = pattern.format(name=name, dir=str(dir_path))
        test_path = Path(test_path_str)

        debug(f"Checking for test file: {test_path}")

        if test_path.exists():
            debug(f"Found test file: {test_path}")
            return str(test_path)

        # Also try relative to project root
        if not test_path.is_absolute():
            # Try finding in common test directories
            for test_dir in ["tests", "test", "__tests__", "spec"]:
                alt_path = Path(test_dir) / test_path.name
                if alt_path.exists():
                    debug(f"Found test file: {alt_path}")
                    return str(alt_path)

    return None


def get_suggested_test_path(source_file: str) -> str:
    """Get suggested path for creating a test file."""
    path = Path(source_file)
    ext = path.suffix
    name = path.stem

    if ext not in SOURCE_PATTERNS:
        return f"tests/test_{name}.py"

    # Return first pattern as suggestion
    pattern = SOURCE_PATTERNS[ext][0]
    return pattern.format(name=name, dir=str(path.parent))


def main() -> None:
    """Main entry point for the hook."""
    # Check if extension is enabled
    if not is_extension_enabled("test-coverage-enforcer"):
        debug("Extension disabled, exiting")
        sys.exit(0)

    # Read hook input from stdin
    try:
        hook_input = json.loads(sys.stdin.read())
    except json.JSONDecodeError as e:
        debug(f"Failed to parse hook input: {e}")
        sys.exit(0)

    tool_name = hook_input.get("tool_name", "")
    tool_input = hook_input.get("tool_input", {})

    debug(f"Tool: {tool_name}")
    debug(f"Input: {json.dumps(tool_input, indent=2)}")

    # Only check Edit and Write operations
    if tool_name not in ("Edit", "Write"):
        debug(f"Skipping: not an Edit or Write operation")
        sys.exit(0)

    # Get file path from tool input
    file_path = tool_input.get("file_path", "")
    if not file_path:
        debug("No file_path in tool input")
        sys.exit(0)

    # Normalize path
    file_path = str(Path(file_path).resolve())
    debug(f"Checking file: {file_path}")

    # Check if file should be skipped
    if should_skip_file(file_path):
        sys.exit(0)

    # Look for corresponding test file
    test_file = find_test_file(file_path)

    if test_file is not None:
        debug(f"Test file found: {test_file}")
        sys.exit(0)

    # No test file found - emit warning
    suggestion = get_suggested_test_path(file_path)

    # Format output
    badge = severity_badge("medium", plain_text=is_ci())
    relative_path = file_path
    try:
        relative_path = str(Path(file_path).relative_to(Path.cwd()))
    except ValueError:
        pass

    warning_msg = (
        f"{badge} No test file found for {relative_path}\n\n"
        f"Suggestion: Create test file at {suggestion}"
    )

    # Output as JSON for hook system
    output = {"warning": warning_msg}
    print(json.dumps(output))

    # Exit with warning code (non-blocking)
    sys.exit(1)


if __name__ == "__main__":
    main()
