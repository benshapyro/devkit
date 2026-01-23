#!/usr/bin/env python3
"""
Package all skills in the devkit into distributable zip files.

Usage:
    python scripts/package_skills.py [--dry-run] [--skill SKILL_NAME]

Options:
    --dry-run       Show what would be done without making changes
    --skill NAME    Only package a specific skill

Behavior:
    1. Finds all skill folders in skills/ (excludes hidden dirs like .zip, .archive)
    2. For each skill with an existing zip, archives the old zip with timestamp
    3. Creates fresh zip in skills/.zip/
    4. Excludes: __pycache__, .DS_Store, .git, *.pyc, .env, node_modules
"""

import argparse
import os
import shutil
import zipfile
from datetime import datetime
from pathlib import Path

# Directories
SKILLS_DIR = Path(__file__).parent.parent / "skills"
ZIP_DIR = SKILLS_DIR / ".zip"
ARCHIVE_DIR = SKILLS_DIR / ".archive"

# Exclusions - files/folders to skip when zipping
EXCLUDED_NAMES = {
    "__pycache__",
    ".DS_Store",
    ".git",
    ".env",
    "node_modules",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
}

EXCLUDED_EXTENSIONS = {
    ".pyc",
    ".pyo",
}


def should_exclude(path: Path) -> bool:
    """Check if a path should be excluded from the zip."""
    if path.name in EXCLUDED_NAMES:
        return True
    if path.suffix in EXCLUDED_EXTENSIONS:
        return True
    return False


def get_skill_folders() -> list[tuple[Path, str]]:
    """
    Get all skill folders with their group.
    Returns list of (skill_path, group_name) tuples.
    Skills can be at root level or inside group directories.
    """
    skills = []

    for item in SKILLS_DIR.iterdir():
        if not item.is_dir():
            continue
        # Skip hidden directories and special folders
        if item.name.startswith(".") or item.name.startswith("_"):
            continue

        # Check if this is a skill at root level
        if (item / "SKILL.md").exists():
            skills.append((item, ""))  # No group
            continue

        # Check if this is a group directory containing skills
        for subitem in item.iterdir():
            if not subitem.is_dir():
                continue
            if subitem.name.startswith(".") or subitem.name.startswith("_"):
                continue
            if (subitem / "SKILL.md").exists():
                skills.append((subitem, item.name))  # (skill_path, group_name)

    return sorted(skills, key=lambda x: (x[1], x[0].name))


def archive_existing_zip(skill_name: str, group: str, dry_run: bool = False) -> Path | None:
    """
    Move existing zip to archive with timestamp.
    Returns the archive path if moved, None if no existing zip.
    """
    # Zip location depends on group
    if group:
        existing_zip = ZIP_DIR / group / f"{skill_name}.zip"
    else:
        existing_zip = ZIP_DIR / f"{skill_name}.zip"

    if not existing_zip.exists():
        return None

    # Create per-skill archive directory
    skill_archive_dir = ARCHIVE_DIR / skill_name

    # Generate timestamped filename
    today = datetime.now().strftime("%Y-%m-%d")
    archive_name = f"{skill_name}-{today}.zip"
    archive_path = skill_archive_dir / archive_name

    # Handle same-day duplicates
    if archive_path.exists():
        counter = 1
        while archive_path.exists():
            archive_name = f"{skill_name}-{today}-{counter}.zip"
            archive_path = skill_archive_dir / archive_name
            counter += 1

    if dry_run:
        print(f"  Would archive: {existing_zip.name} -> .archive/{skill_name}/{archive_name}")
        return archive_path

    # Create archive directory and move
    skill_archive_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(existing_zip), str(archive_path))
    print(f"  Archived: {existing_zip.name} -> .archive/{skill_name}/{archive_name}")
    return archive_path


def create_skill_zip(skill_path: Path, group: str, dry_run: bool = False) -> Path:
    """Create a zip file for a skill folder in its group directory."""
    skill_name = skill_path.name

    # Zip goes in group subdirectory if grouped
    if group:
        zip_dir = ZIP_DIR / group
        zip_path = zip_dir / f"{skill_name}.zip"
    else:
        zip_dir = ZIP_DIR
        zip_path = ZIP_DIR / f"{skill_name}.zip"

    if dry_run:
        # Count files that would be included
        file_count = 0
        for root, dirs, files in os.walk(skill_path):
            # Filter out excluded directories
            dirs[:] = [d for d in dirs if not should_exclude(Path(d))]
            for f in files:
                if not should_exclude(Path(f)):
                    file_count += 1
        group_prefix = f"{group}/" if group else ""
        print(f"  Would create: {group_prefix}{skill_name}.zip ({file_count} files)")
        return zip_path

    # Ensure zip directory exists (including group subdirectory)
    zip_dir.mkdir(parents=True, exist_ok=True)

    # Create the zip
    file_count = 0
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(skill_path):
            # Filter out excluded directories (modifies in-place to skip recursion)
            dirs[:] = [d for d in dirs if not should_exclude(Path(d))]

            for file in files:
                file_path = Path(root) / file
                if should_exclude(file_path):
                    continue

                # Archive path preserves skill folder structure
                arcname = str(file_path.relative_to(skill_path.parent))
                zf.write(file_path, arcname)
                file_count += 1

    size_kb = zip_path.stat().st_size / 1024
    group_prefix = f"{group}/" if group else ""
    print(f"  Created: {group_prefix}{skill_name}.zip ({file_count} files, {size_kb:.0f}KB)")
    return zip_path


def package_skill(skill_path: Path, group: str, dry_run: bool = False) -> None:
    """Package a single skill: archive old zip if exists, create new zip."""
    skill_name = skill_path.name
    group_prefix = f"{group}/" if group else ""
    print(f"\n{group_prefix}{skill_name}/")

    # Archive existing zip if present
    archive_existing_zip(skill_name, group, dry_run)

    # Create new zip
    create_skill_zip(skill_path, group, dry_run)


def main():
    parser = argparse.ArgumentParser(description="Package skills into distributable zips")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--skill", type=str, help="Only package a specific skill")
    parser.add_argument("--group", type=str, help="Only package skills in a specific group")
    args = parser.parse_args()

    print("=" * 50)
    print("Packaging Skills")
    print("=" * 50)

    if args.dry_run:
        print("(DRY RUN - no changes will be made)\n")

    skills = get_skill_folders()

    if args.skill:
        # Filter to specific skill
        skills = [(s, g) for s, g in skills if s.name == args.skill]
        if not skills:
            print(f"Error: Skill '{args.skill}' not found")
            return 1

    if args.group:
        # Filter to specific group
        skills = [(s, g) for s, g in skills if g == args.group]
        if not skills:
            print(f"Error: No skills found in group '{args.group}'")
            return 1

    print(f"Found {len(skills)} skills to package:")
    for skill_path, group in skills:
        group_prefix = f"{group}/" if group else ""
        print(f"  - {group_prefix}{skill_path.name}")

    for skill_path, group in skills:
        package_skill(skill_path, group, args.dry_run)

    print("\n" + "=" * 50)
    print(f"Done. Zips in: skills/.zip/<group>/")
    if not args.dry_run:
        print(f"Archives in:   skills/.archive/")
    print("=" * 50)

    return 0


if __name__ == "__main__":
    exit(main())
