"""
Coverage report parsing for devkit extensions.

Supports:
- Jest coverage (JSON format)
- Pytest coverage (JSON format via pytest-cov)
- Delta coverage calculation
"""

from dataclasses import dataclass, field
from pathlib import Path
import json
from typing import Optional


@dataclass
class FileCoverage:
    """Coverage data for a single file."""
    path: str
    statements_total: int
    statements_covered: int
    branches_total: int
    branches_covered: int
    functions_total: int
    functions_covered: int
    lines_covered: list[int] = field(default_factory=list)
    lines_uncovered: list[int] = field(default_factory=list)

    @property
    def line_coverage(self) -> float:
        """Calculate line coverage percentage."""
        total = len(self.lines_covered) + len(self.lines_uncovered)
        if total == 0:
            return 100.0
        return (len(self.lines_covered) / total) * 100

    @property
    def statement_coverage(self) -> float:
        """Calculate statement coverage percentage."""
        if self.statements_total == 0:
            return 100.0
        return (self.statements_covered / self.statements_total) * 100


@dataclass
class CoverageReport:
    """Complete coverage report."""
    files: dict[str, FileCoverage] = field(default_factory=dict)
    total_statements: int = 0
    covered_statements: int = 0
    total_branches: int = 0
    covered_branches: int = 0
    total_functions: int = 0
    covered_functions: int = 0

    @property
    def line_coverage(self) -> float:
        """Overall line coverage percentage."""
        if self.total_statements == 0:
            return 100.0
        return (self.covered_statements / self.total_statements) * 100

    @property
    def branch_coverage(self) -> float:
        """Overall branch coverage percentage."""
        if self.total_branches == 0:
            return 100.0
        return (self.covered_branches / self.total_branches) * 100

    @property
    def function_coverage(self) -> float:
        """Overall function coverage percentage."""
        if self.total_functions == 0:
            return 100.0
        return (self.covered_functions / self.total_functions) * 100


def parse_jest_coverage(json_path: str) -> Optional[CoverageReport]:
    """
    Parse Jest coverage JSON report.

    Jest outputs coverage in a specific format when using:
    jest --coverage --coverageReporters=json

    Args:
        json_path: Path to coverage-final.json or coverage-summary.json

    Returns:
        CoverageReport or None if parsing fails
    """
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    report = CoverageReport()

    # Check if this is coverage-final.json format
    for file_path, file_data in data.items():
        if file_path == "total":
            continue

        # Skip test files
        if "test" in file_path.lower() or "spec" in file_path.lower():
            continue

        # Extract statement data
        stmt_map = file_data.get("statementMap", {})
        stmt_hits = file_data.get("s", {})

        statements_total = len(stmt_map)
        statements_covered = sum(1 for v in stmt_hits.values() if v > 0)

        # Extract branch data
        branch_map = file_data.get("branchMap", {})
        branch_hits = file_data.get("b", {})

        branches_total = sum(len(b.get("locations", [])) for b in branch_map.values())
        branches_covered = sum(sum(1 for h in hits if h > 0) for hits in branch_hits.values())

        # Extract function data
        fn_map = file_data.get("fnMap", {})
        fn_hits = file_data.get("f", {})

        functions_total = len(fn_map)
        functions_covered = sum(1 for v in fn_hits.values() if v > 0)

        # Build line coverage lists
        lines_covered = []
        lines_uncovered = []

        for stmt_id, stmt in stmt_map.items():
            start_line = stmt.get("start", {}).get("line", 0)
            if stmt_hits.get(stmt_id, 0) > 0:
                if start_line not in lines_covered:
                    lines_covered.append(start_line)
            else:
                if start_line not in lines_uncovered:
                    lines_uncovered.append(start_line)

        file_cov = FileCoverage(
            path=file_path,
            statements_total=statements_total,
            statements_covered=statements_covered,
            branches_total=branches_total,
            branches_covered=branches_covered,
            functions_total=functions_total,
            functions_covered=functions_covered,
            lines_covered=sorted(lines_covered),
            lines_uncovered=sorted(lines_uncovered),
        )

        report.files[file_path] = file_cov
        report.total_statements += statements_total
        report.covered_statements += statements_covered
        report.total_branches += branches_total
        report.covered_branches += branches_covered
        report.total_functions += functions_total
        report.covered_functions += functions_covered

    return report


def parse_pytest_coverage(json_path: str) -> Optional[CoverageReport]:
    """
    Parse Pytest coverage JSON report.

    Generated with: pytest --cov --cov-report=json

    Args:
        json_path: Path to coverage.json

    Returns:
        CoverageReport or None if parsing fails
    """
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    report = CoverageReport()

    files_data = data.get("files", {})

    for file_path, file_data in files_data.items():
        # Skip test files
        if "test" in file_path.lower():
            continue

        summary = file_data.get("summary", {})

        # Pytest uses different field names
        statements_total = summary.get("num_statements", 0)
        statements_covered = summary.get("covered_lines", 0)
        branches_total = summary.get("num_branches", 0)
        branches_covered = summary.get("covered_branches", 0)

        # Get line details
        missing_lines = file_data.get("missing_lines", [])
        executed_lines = file_data.get("executed_lines", [])

        file_cov = FileCoverage(
            path=file_path,
            statements_total=statements_total,
            statements_covered=statements_covered,
            branches_total=branches_total,
            branches_covered=branches_covered,
            functions_total=0,  # Pytest doesn't track function coverage separately
            functions_covered=0,
            lines_covered=executed_lines,
            lines_uncovered=missing_lines,
        )

        report.files[file_path] = file_cov
        report.total_statements += statements_total
        report.covered_statements += statements_covered
        report.total_branches += branches_total
        report.covered_branches += branches_covered

    return report


def get_uncovered_lines(report: CoverageReport, file: str) -> list[int]:
    """
    Get uncovered lines for a specific file.

    Args:
        report: CoverageReport to search
        file: File path to look up

    Returns:
        List of uncovered line numbers
    """
    # Try exact match first
    if file in report.files:
        return report.files[file].lines_uncovered

    # Try matching by basename
    file_name = Path(file).name
    for path, cov in report.files.items():
        if Path(path).name == file_name:
            return cov.lines_uncovered

    return []


def calculate_delta_coverage(
    base: CoverageReport,
    current: CoverageReport,
    changed_files: Optional[list[str]] = None
) -> float:
    """
    Calculate coverage delta between two reports.

    Only considers new/changed code, ignoring existing gaps.

    Args:
        base: Baseline coverage report
        current: Current coverage report
        changed_files: Optional list of changed files to focus on

    Returns:
        Coverage percentage for new/changed code
    """
    if changed_files is None:
        # Compare all files
        changed_files = list(set(current.files.keys()) | set(base.files.keys()))

    new_lines_total = 0
    new_lines_covered = 0

    for file in changed_files:
        current_cov = current.files.get(file)
        base_cov = base.files.get(file)

        if current_cov is None:
            continue

        if base_cov is None:
            # New file - all lines are new
            new_lines_total += len(current_cov.lines_covered) + len(current_cov.lines_uncovered)
            new_lines_covered += len(current_cov.lines_covered)
        else:
            # Existing file - only count new lines
            base_lines = set(base_cov.lines_covered) | set(base_cov.lines_uncovered)
            current_lines = set(current_cov.lines_covered) | set(current_cov.lines_uncovered)

            new_lines = current_lines - base_lines

            for line in new_lines:
                new_lines_total += 1
                if line in current_cov.lines_covered:
                    new_lines_covered += 1

    if new_lines_total == 0:
        return 100.0

    return (new_lines_covered / new_lines_total) * 100


def find_coverage_report() -> Optional[tuple[str, str]]:
    """
    Find coverage report in common locations.

    Returns:
        Tuple of (report_path, report_type) or None
    """
    # Jest locations
    jest_paths = [
        "coverage/coverage-final.json",
        "coverage/coverage-summary.json",
        ".coverage/coverage-final.json",
    ]

    for path in jest_paths:
        if Path(path).exists():
            return path, "jest"

    # Pytest locations
    pytest_paths = [
        "coverage.json",
        ".coverage.json",
        "htmlcov/coverage.json",
    ]

    for path in pytest_paths:
        if Path(path).exists():
            return path, "pytest"

    return None


def parse_coverage_report(path: Optional[str] = None) -> Optional[CoverageReport]:
    """
    Auto-detect and parse coverage report.

    Args:
        path: Optional explicit path. If None, searches common locations.

    Returns:
        CoverageReport or None if not found
    """
    if path:
        # Try to detect type from content
        try:
            with open(path, "r") as f:
                data = json.load(f)

            # Jest format has file paths as top-level keys
            if any(key.endswith((".js", ".ts", ".jsx", ".tsx")) for key in data.keys()):
                return parse_jest_coverage(path)

            # Pytest format has "files" and "totals" keys
            if "files" in data and "totals" in data:
                return parse_pytest_coverage(path)

        except (FileNotFoundError, json.JSONDecodeError):
            return None

    # Auto-detect
    result = find_coverage_report()
    if result is None:
        return None

    path, report_type = result
    if report_type == "jest":
        return parse_jest_coverage(path)
    elif report_type == "pytest":
        return parse_pytest_coverage(path)

    return None
