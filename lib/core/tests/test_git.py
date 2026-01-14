"""Tests for lib.core.git module."""

import pytest
from unittest.mock import patch, MagicMock

# Add parent path for imports
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

from lib.core.git import (
    FileDiff,
    BlameInfo,
    Commit,
    run_git,
    get_diff,
    get_changed_files,
    get_current_branch,
    get_base_branch,
)


class TestFileDiff:
    """Tests for FileDiff dataclass."""

    def test_basic_diff(self):
        """FileDiff stores basic diff info."""
        diff = FileDiff(
            path="src/main.py",
            status="M",
            additions=10,
            deletions=5,
        )
        assert diff.path == "src/main.py"
        assert diff.status == "M"
        assert diff.additions == 10
        assert diff.deletions == 5

    def test_rename_diff(self):
        """FileDiff stores rename info."""
        diff = FileDiff(
            path="new_name.py",
            status="R",
            additions=0,
            deletions=0,
            old_path="old_name.py",
        )
        assert diff.old_path == "old_name.py"


class TestBlameInfo:
    """Tests for BlameInfo dataclass."""

    def test_blame_info(self):
        """BlameInfo stores all blame fields."""
        info = BlameInfo(
            commit_hash="abc123",
            author="John Doe",
            author_email="john@example.com",
            date="2024-01-15",
            line_number=42,
            content="print('hello')",
        )
        assert info.commit_hash == "abc123"
        assert info.author == "John Doe"
        assert info.line_number == 42


class TestCommit:
    """Tests for Commit dataclass."""

    def test_commit_info(self):
        """Commit stores all commit fields."""
        commit = Commit(
            hash="abc123def456",
            short_hash="abc123d",
            author="Jane Doe",
            author_email="jane@example.com",
            date="2024-01-15",
            message="feat: add feature",
            files_changed=["file1.py", "file2.py"],
        )
        assert commit.hash == "abc123def456"
        assert commit.short_hash == "abc123d"
        assert len(commit.files_changed) == 2


class TestRunGit:
    """Tests for run_git function."""

    def test_successful_command(self):
        """Successful git command returns output."""
        exit_code, stdout, stderr = run_git(["--version"])
        assert exit_code == 0
        assert "git version" in stdout.lower()

    def test_invalid_command(self):
        """Invalid git command returns error."""
        exit_code, stdout, stderr = run_git(["not-a-real-command"])
        assert exit_code != 0


class TestGetDiff:
    """Tests for get_diff function."""

    @patch("lib.core.git.run_git")
    def test_no_changes(self, mock_run):
        """No changes returns empty list."""
        mock_run.return_value = (0, "", "")
        result = get_diff()
        assert result == []

    @patch("lib.core.git.run_git")
    def test_modified_file(self, mock_run):
        """Modified file appears in diff."""
        # First call: name-status
        # Second call: numstat
        mock_run.side_effect = [
            (0, "M\tsrc/main.py\n", ""),
            (0, "10\t5\tsrc/main.py\n", ""),
        ]
        result = get_diff()
        assert len(result) == 1
        assert result[0].path == "src/main.py"
        assert result[0].status == "M"


class TestGetChangedFiles:
    """Tests for get_changed_files function."""

    @patch("lib.core.git.run_git")
    def test_no_changes(self, mock_run):
        """No changes returns empty list."""
        mock_run.return_value = (0, "", "")
        result = get_changed_files()
        assert result == []

    @patch("lib.core.git.run_git")
    def test_changed_files(self, mock_run):
        """Changed files are returned."""
        mock_run.return_value = (0, "file1.py\nfile2.py\n", "")
        result = get_changed_files()
        assert result == ["file1.py", "file2.py"]


class TestGetCurrentBranch:
    """Tests for get_current_branch function."""

    @patch("lib.core.git.run_git")
    def test_on_branch(self, mock_run):
        """Returns current branch name."""
        mock_run.return_value = (0, "feature-branch\n", "")
        result = get_current_branch()
        assert result == "feature-branch"

    @patch("lib.core.git.run_git")
    def test_detached_head(self, mock_run):
        """Returns None when not on a branch."""
        mock_run.return_value = (1, "", "")
        result = get_current_branch()
        assert result is None


class TestGetBaseBranch:
    """Tests for get_base_branch function."""

    @patch("lib.core.git.run_git")
    def test_has_main(self, mock_run):
        """Returns 'main' when main exists."""
        mock_run.return_value = (0, "  main\n", "")
        result = get_base_branch()
        assert result == "main"

    @patch("lib.core.git.run_git")
    def test_has_master(self, mock_run):
        """Returns 'master' when only master exists."""
        mock_run.return_value = (0, "  master\n", "")
        result = get_base_branch()
        assert result == "master"
