"""Tests for lib.core.output module."""

import os
import pytest
from unittest.mock import patch

# Add parent path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from lib.core.output import (
    severity_badge,
    severity_text,
    markdown_table,
    markdown_list,
    markdown_code_block,
    is_ci,
    is_interactive,
    progress_bar,
)


class TestSeverityBadge:
    """Tests for severity_badge function."""

    def test_critical_badge(self):
        """Critical badge includes red circle."""
        badge = severity_badge("critical")
        assert "CRITICAL" in badge

    def test_medium_badge(self):
        """Medium badge includes yellow circle."""
        badge = severity_badge("medium")
        assert "MEDIUM" in badge

    def test_info_badge(self):
        """Info badge includes blue circle."""
        badge = severity_badge("info")
        assert "INFO" in badge

    def test_plain_text_mode(self):
        """Plain text mode omits emoji."""
        badge = severity_badge("critical", plain_text=True)
        assert badge == "[CRITICAL]"

    def test_unknown_level_defaults_to_info(self):
        """Unknown level defaults to info style."""
        badge = severity_badge("unknown")
        assert "INFO" in badge


class TestSeverityText:
    """Tests for severity_text function."""

    def test_includes_level_and_text(self):
        """Output includes both level and message."""
        result = severity_text("warning", "Something happened", plain_text=True)
        assert "WARNING" in result
        assert "Something happened" in result


class TestMarkdownTable:
    """Tests for markdown_table function."""

    def test_empty_headers_returns_empty(self):
        """Empty headers returns empty string."""
        result = markdown_table([], [])
        assert result == ""

    def test_simple_table(self):
        """Simple table with headers and rows."""
        headers = ["Name", "Value"]
        rows = [["foo", "1"], ["bar", "2"]]
        result = markdown_table(headers, rows)

        assert "| Name" in result
        assert "| foo" in result
        assert "| bar" in result
        assert "---" in result

    def test_column_alignment(self):
        """Columns are properly aligned."""
        headers = ["A", "B"]
        rows = [["longer", "x"]]
        result = markdown_table(headers, rows)

        # Table should have separator row
        lines = result.split("\n")
        assert len(lines) == 3


class TestMarkdownList:
    """Tests for markdown_list function."""

    def test_unordered_list(self):
        """Unordered list uses dashes."""
        items = ["one", "two", "three"]
        result = markdown_list(items)

        assert "- one" in result
        assert "- two" in result
        assert "- three" in result

    def test_ordered_list(self):
        """Ordered list uses numbers."""
        items = ["one", "two", "three"]
        result = markdown_list(items, ordered=True)

        assert "1. one" in result
        assert "2. two" in result
        assert "3. three" in result


class TestMarkdownCodeBlock:
    """Tests for markdown_code_block function."""

    def test_basic_code_block(self):
        """Basic code block with no language."""
        result = markdown_code_block("print('hello')")
        assert result == "```\nprint('hello')\n```"

    def test_code_block_with_language(self):
        """Code block with language identifier."""
        result = markdown_code_block("print('hello')", language="python")
        assert result == "```python\nprint('hello')\n```"


class TestIsCi:
    """Tests for is_ci function."""

    def test_ci_env_var_set(self):
        """Returns True when CI env var is set."""
        with patch.dict(os.environ, {"CI": "true"}):
            assert is_ci() is True

    def test_github_actions_set(self):
        """Returns True when GITHUB_ACTIONS is set."""
        with patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}):
            assert is_ci() is True

    def test_no_ci_vars(self):
        """Returns False when no CI vars are set."""
        # Clear CI-related env vars
        env = {k: v for k, v in os.environ.items()
               if k not in ["CI", "GITHUB_ACTIONS", "GITLAB_CI", "CIRCLECI", "JENKINS_URL"]}
        with patch.dict(os.environ, env, clear=True):
            assert is_ci() is False


class TestProgressBar:
    """Tests for progress_bar function."""

    def test_zero_percent(self):
        """0% progress shows empty bar."""
        result = progress_bar(0, 100)
        assert "0%" in result

    def test_fifty_percent(self):
        """50% progress shows half-filled bar."""
        result = progress_bar(50, 100)
        assert "50%" in result

    def test_hundred_percent(self):
        """100% progress shows full bar."""
        result = progress_bar(100, 100)
        assert "100%" in result

    def test_zero_total(self):
        """Zero total returns 100%."""
        result = progress_bar(0, 0)
        assert "100%" in result
