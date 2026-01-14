"""
Core utilities for devkit extensions.

This module provides shared primitives for hooks, commands, and agents:
- git: Git operations (diff, blame, log, status)
- coverage: Coverage report parsing (Jest, Pytest)
- output: Markdown formatting, spinners, colors
- config: Settings loading, CI detection
"""

from lib.core.git import (
    get_diff,
    get_blame,
    get_recent_commits,
    get_changed_files,
    get_file_history,
    FileDiff,
    BlameInfo,
    Commit,
)

from lib.core.coverage import (
    parse_jest_coverage,
    parse_pytest_coverage,
    get_uncovered_lines,
    calculate_delta_coverage,
    CoverageReport,
)

from lib.core.output import (
    spinner,
    severity_badge,
    markdown_table,
    is_ci,
)

from lib.core.config import (
    load_settings,
    get_setting,
    Settings,
)

__all__ = [
    # git
    "get_diff",
    "get_blame",
    "get_recent_commits",
    "get_changed_files",
    "get_file_history",
    "FileDiff",
    "BlameInfo",
    "Commit",
    # coverage
    "parse_jest_coverage",
    "parse_pytest_coverage",
    "get_uncovered_lines",
    "calculate_delta_coverage",
    "CoverageReport",
    # output
    "spinner",
    "severity_badge",
    "markdown_table",
    "is_ci",
    # config
    "load_settings",
    "get_setting",
    "Settings",
]
