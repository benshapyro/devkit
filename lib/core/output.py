"""
Output formatting utilities for devkit extensions.

Provides:
- Severity badges with emoji
- Markdown table generation
- CI detection
- Spinner context manager (terminal only)
"""

import os
import sys
import threading
import time
from contextlib import contextmanager
from typing import Iterator


# CI environment variables to check
CI_ENV_VARS = [
    "CI",
    "CONTINUOUS_INTEGRATION",
    "GITHUB_ACTIONS",
    "GITLAB_CI",
    "CIRCLECI",
    "JENKINS_URL",
    "TRAVIS",
    "BUILDKITE",
    "AZURE_PIPELINES",
    "TEAMCITY_VERSION",
    "CODEBUILD_BUILD_ID",
]


def is_ci() -> bool:
    """
    Detect if running in a CI environment.

    Returns:
        True if any CI environment variable is set
    """
    return any(os.getenv(var) for var in CI_ENV_VARS)


def is_interactive() -> bool:
    """
    Detect if running in an interactive terminal.

    Returns:
        True if stdout is a TTY and not in CI
    """
    return sys.stdout.isatty() and not is_ci()


# Severity levels with emoji and ANSI colors
SEVERITY_STYLES = {
    "critical": {
        "emoji": "\U0001f534",  # Red circle
        "color": "\033[91m",  # Bright red
        "label": "CRITICAL",
    },
    "high": {
        "emoji": "\U0001f7e0",  # Orange circle
        "color": "\033[93m",  # Yellow/orange
        "label": "HIGH",
    },
    "medium": {
        "emoji": "\U0001f7e1",  # Yellow circle
        "color": "\033[93m",  # Yellow
        "label": "MEDIUM",
    },
    "low": {
        "emoji": "\U0001f7e2",  # Green circle
        "color": "\033[92m",  # Green
        "label": "LOW",
    },
    "info": {
        "emoji": "\U0001f535",  # Blue circle
        "color": "\033[94m",  # Blue
        "label": "INFO",
    },
    "success": {
        "emoji": "\u2705",  # Check mark
        "color": "\033[92m",  # Green
        "label": "SUCCESS",
    },
    "warning": {
        "emoji": "\u26a0\ufe0f",  # Warning sign
        "color": "\033[93m",  # Yellow
        "label": "WARNING",
    },
    "error": {
        "emoji": "\u274c",  # X mark
        "color": "\033[91m",  # Red
        "label": "ERROR",
    },
}

RESET_COLOR = "\033[0m"


def severity_badge(level: str, plain_text: bool = False) -> str:
    """
    Get a severity badge with emoji and optional color.

    Args:
        level: Severity level (critical, high, medium, low, info, success, warning, error)
        plain_text: If True, omit emoji (for CI output)

    Returns:
        Formatted severity badge string
    """
    style = SEVERITY_STYLES.get(level.lower(), SEVERITY_STYLES["info"])

    if plain_text or is_ci():
        return f"[{style['label']}]"

    return f"{style['emoji']} {style['label']}"


def severity_text(level: str, text: str, plain_text: bool = False) -> str:
    """
    Wrap text with severity color.

    Args:
        level: Severity level
        text: Text to colorize
        plain_text: If True, no color codes

    Returns:
        Colorized text (or plain if in CI)
    """
    style = SEVERITY_STYLES.get(level.lower(), SEVERITY_STYLES["info"])

    if plain_text or is_ci() or not is_interactive():
        return f"[{style['label']}] {text}"

    return f"{style['color']}{style['emoji']} {text}{RESET_COLOR}"


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """
    Generate a markdown table.

    Args:
        headers: List of column headers
        rows: List of rows, each row is a list of cell values

    Returns:
        Formatted markdown table string
    """
    if not headers:
        return ""

    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            if i < len(widths):
                widths[i] = max(widths[i], len(str(cell)))

    # Build table
    lines = []

    # Header row
    header_cells = [h.ljust(widths[i]) for i, h in enumerate(headers)]
    lines.append("| " + " | ".join(header_cells) + " |")

    # Separator row
    sep_cells = ["-" * widths[i] for i in range(len(headers))]
    lines.append("| " + " | ".join(sep_cells) + " |")

    # Data rows
    for row in rows:
        cells = []
        for i, cell in enumerate(row):
            if i < len(widths):
                cells.append(str(cell).ljust(widths[i]))
        lines.append("| " + " | ".join(cells) + " |")

    return "\n".join(lines)


def markdown_list(items: list[str], ordered: bool = False) -> str:
    """
    Generate a markdown list.

    Args:
        items: List of items
        ordered: If True, create numbered list

    Returns:
        Formatted markdown list string
    """
    lines = []
    for i, item in enumerate(items, 1):
        if ordered:
            lines.append(f"{i}. {item}")
        else:
            lines.append(f"- {item}")
    return "\n".join(lines)


def markdown_code_block(code: str, language: str = "") -> str:
    """
    Generate a markdown code block.

    Args:
        code: Code content
        language: Optional language identifier

    Returns:
        Formatted code block
    """
    return f"```{language}\n{code}\n```"


class Spinner:
    """Simple terminal spinner for long-running operations."""

    FRAMES = ["[    ]", "[=   ]", "[==  ]", "[=== ]", "[ ===]", "[  ==]", "[   =]"]

    def __init__(self, message: str):
        self.message = message
        self.running = False
        self.thread = None

    def _spin(self):
        """Spin animation loop."""
        i = 0
        while self.running:
            frame = self.FRAMES[i % len(self.FRAMES)]
            sys.stderr.write(f"\r{frame} {self.message}")
            sys.stderr.flush()
            time.sleep(0.1)
            i += 1

    def start(self):
        """Start the spinner."""
        if not is_interactive():
            # In CI, just print the message once
            print(f"... {self.message}", file=sys.stderr)
            return

        self.running = True
        self.thread = threading.Thread(target=self._spin, daemon=True)
        self.thread.start()

    def stop(self, success: bool = True):
        """Stop the spinner."""
        self.running = False

        if not is_interactive():
            return

        if self.thread:
            self.thread.join(timeout=0.2)

        # Clear line and show result
        icon = "\u2705" if success else "\u274c"
        sys.stderr.write(f"\r{icon} {self.message}\n")
        sys.stderr.flush()


@contextmanager
def spinner(message: str) -> Iterator[None]:
    """
    Context manager for showing a spinner during operations.

    In CI environments, just prints the message without animation.

    Args:
        message: Message to display next to spinner

    Example:
        with spinner("Processing files..."):
            do_long_operation()
    """
    s = Spinner(message)
    s.start()
    try:
        yield
    except Exception:
        s.stop(success=False)
        raise
    else:
        s.stop(success=True)


def progress_bar(current: int, total: int, width: int = 40) -> str:
    """
    Generate a text progress bar.

    Args:
        current: Current progress value
        total: Total value
        width: Bar width in characters

    Returns:
        Progress bar string like [=========>          ] 50%
    """
    if total == 0:
        pct = 100
    else:
        pct = int((current / total) * 100)

    filled = int((current / max(total, 1)) * width)
    bar = "=" * filled

    if filled < width:
        bar += ">"
        bar += " " * (width - filled - 1)
    else:
        bar = "=" * width

    return f"[{bar}] {pct}%"
