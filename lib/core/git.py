"""
Git operations for devkit extensions.

Provides typed wrappers around git commands for:
- Diff analysis
- Blame information
- Commit history
- File change detection
"""

from dataclasses import dataclass
from pathlib import Path
import subprocess
import re
from typing import Optional


@dataclass
class FileDiff:
    """Represents a file diff from git."""
    path: str
    status: str  # A=added, M=modified, D=deleted, R=renamed
    additions: int
    deletions: int
    old_path: Optional[str] = None  # For renames


@dataclass
class BlameInfo:
    """Blame information for a specific line."""
    commit_hash: str
    author: str
    author_email: str
    date: str
    line_number: int
    content: str


@dataclass
class Commit:
    """Represents a git commit."""
    hash: str
    short_hash: str
    author: str
    author_email: str
    date: str
    message: str
    files_changed: list[str]


def run_git(args: list[str], cwd: Optional[str] = None) -> tuple[int, str, str]:
    """Run a git command and return (exit_code, stdout, stderr)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return 1, "", "Command timed out"
    except Exception as e:
        return 1, "", str(e)


def get_diff(base: str = "HEAD") -> list[FileDiff]:
    """
    Get file diffs compared to base.

    Args:
        base: Git ref to compare against (default: HEAD)

    Returns:
        List of FileDiff objects for changed files
    """
    diffs = []

    # Get list of changed files with status
    exit_code, stdout, _ = run_git(["diff", "--name-status", base])
    if exit_code != 0:
        return diffs

    for line in stdout.strip().split("\n"):
        if not line:
            continue

        parts = line.split("\t")
        if len(parts) < 2:
            continue

        status = parts[0][0]  # First char is status

        if status == "R":
            # Rename: status is like R100, has old and new path
            old_path = parts[1]
            new_path = parts[2] if len(parts) > 2 else parts[1]
            diffs.append(FileDiff(
                path=new_path,
                status="R",
                additions=0,
                deletions=0,
                old_path=old_path,
            ))
        else:
            diffs.append(FileDiff(
                path=parts[1],
                status=status,
                additions=0,
                deletions=0,
            ))

    # Get line counts
    exit_code, stdout, _ = run_git(["diff", "--numstat", base])
    if exit_code == 0:
        for line in stdout.strip().split("\n"):
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) >= 3:
                try:
                    additions = int(parts[0]) if parts[0] != "-" else 0
                    deletions = int(parts[1]) if parts[1] != "-" else 0
                    path = parts[2]

                    for diff in diffs:
                        if diff.path == path:
                            diff.additions = additions
                            diff.deletions = deletions
                            break
                except ValueError:
                    pass

    return diffs


def get_blame(file: str, line: int) -> Optional[BlameInfo]:
    """
    Get blame information for a specific line in a file.

    Args:
        file: Path to the file
        line: Line number (1-indexed)

    Returns:
        BlameInfo or None if not available
    """
    exit_code, stdout, _ = run_git([
        "blame", "-L", f"{line},{line}", "--porcelain", file
    ])

    if exit_code != 0:
        return None

    lines = stdout.strip().split("\n")
    if not lines:
        return None

    commit_hash = lines[0].split()[0]
    author = ""
    author_email = ""
    date = ""
    content = ""

    for l in lines:
        if l.startswith("author "):
            author = l[7:]
        elif l.startswith("author-mail "):
            author_email = l[12:].strip("<>")
        elif l.startswith("author-time "):
            # Convert timestamp to ISO date
            import datetime
            ts = int(l[12:])
            date = datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
        elif l.startswith("\t"):
            content = l[1:]

    return BlameInfo(
        commit_hash=commit_hash,
        author=author,
        author_email=author_email,
        date=date,
        line_number=line,
        content=content,
    )


def get_recent_commits(count: int = 10, path: Optional[str] = None) -> list[Commit]:
    """
    Get recent commits.

    Args:
        count: Number of commits to retrieve
        path: Optional file/directory to filter by

    Returns:
        List of Commit objects
    """
    commits = []

    # Format: hash, short_hash, author, email, date, message
    format_str = "%H%n%h%n%an%n%ae%n%ai%n%s%n---END---"

    args = ["log", f"-{count}", f"--format={format_str}"]
    if path:
        args.extend(["--", path])

    exit_code, stdout, _ = run_git(args)
    if exit_code != 0:
        return commits

    entries = stdout.split("---END---")
    for entry in entries:
        lines = entry.strip().split("\n")
        if len(lines) >= 6:
            commit_hash = lines[0]

            # Get files changed in this commit
            _, files_stdout, _ = run_git([
                "diff-tree", "--no-commit-id", "--name-only", "-r", commit_hash
            ])
            files = [f for f in files_stdout.strip().split("\n") if f]

            commits.append(Commit(
                hash=commit_hash,
                short_hash=lines[1],
                author=lines[2],
                author_email=lines[3],
                date=lines[4][:10],  # Just the date part
                message=lines[5],
                files_changed=files,
            ))

    return commits


def get_changed_files(staged: bool = False) -> list[str]:
    """
    Get list of changed files.

    Args:
        staged: If True, only return staged files

    Returns:
        List of file paths
    """
    if staged:
        exit_code, stdout, _ = run_git(["diff", "--name-only", "--cached"])
    else:
        exit_code, stdout, _ = run_git(["diff", "--name-only"])

    if exit_code != 0:
        return []

    return [f for f in stdout.strip().split("\n") if f]


def get_file_history(file: str, count: int = 5) -> list[Commit]:
    """
    Get commit history for a specific file.

    Args:
        file: Path to the file
        count: Number of commits to retrieve

    Returns:
        List of Commit objects affecting this file
    """
    return get_recent_commits(count=count, path=file)


def get_current_branch() -> Optional[str]:
    """Get the current branch name."""
    exit_code, stdout, _ = run_git(["branch", "--show-current"])
    if exit_code != 0:
        return None
    return stdout.strip()


def get_base_branch() -> str:
    """Get the base branch (main or master)."""
    exit_code, stdout, _ = run_git(["branch", "-l", "main", "master"])
    if "main" in stdout:
        return "main"
    return "master"


def get_commit_range(base: Optional[str] = None) -> tuple[str, str]:
    """
    Get commit range for current branch vs base.

    Returns:
        Tuple of (base_ref, head_ref)
    """
    if base is None:
        base = get_base_branch()

    # Get merge base
    exit_code, stdout, _ = run_git(["merge-base", base, "HEAD"])
    if exit_code != 0:
        return base, "HEAD"

    return stdout.strip(), "HEAD"
