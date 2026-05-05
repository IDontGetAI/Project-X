#!/usr/bin/env python3
"""Add a new branch to the taxonomy and create matching directories."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from _hub_utils import (
    LIBRARY_ROOT,
    TAXONOMY_PATH,
    VAULT_ROOT,
    branch_dir,
    ensure_gitkeep,
    load_taxonomy,
    moc_path_for_subject,
)


BRANCH_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CODE_PATTERN = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9]+)+$")
SOURCE_TYPE_DIRS = ["10_books", "20_papers", "30_courses", "40_reference"]
NOTE_ROOTS = [
    VAULT_ROOT / "02_source-notes",
    VAULT_ROOT / "03_concept-notes",
    VAULT_ROOT / "04_method-notes",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Add a new taxonomy branch and scaffold matching directories."
    )
    parser.add_argument("--subject-main", required=True, help="Existing subject slug.")
    parser.add_argument("--branch-name", required=True, help="New branch slug in kebab-case.")
    parser.add_argument("--branch-code", required=True, help="Stable uppercase branch code.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned changes without writing files.",
    )
    return parser.parse_args()


def validate_args(subject_main: str, branch_name: str, branch_code: str) -> None:
    if not BRANCH_PATTERN.fullmatch(branch_name):
        raise ValueError("branch-name must use lowercase kebab-case, e.g. dynamical-systems.")
    if not CODE_PATTERN.fullmatch(branch_code):
        raise ValueError("branch-code must use uppercase hyphen style, e.g. MATH-DYN.")

    taxonomy = load_taxonomy()
    if subject_main not in taxonomy:
        raise ValueError(f"Unknown subject: {subject_main}")
    if branch_name in taxonomy[subject_main]["branches"]:
        raise ValueError(f"Branch already exists: {subject_main}/{branch_name}")


def update_subjects_yaml(subject_main: str, branch_name: str, branch_code: str, dry_run: bool) -> None:
    original = TAXONOMY_PATH.read_text(encoding="utf-8")
    lines = original.splitlines()
    subject_header = f"{subject_main}:"

    try:
        subject_index = next(index for index, line in enumerate(lines) if line.strip() == subject_header)
    except StopIteration as exc:
        raise ValueError(f"Subject header not found in taxonomy: {subject_main}") from exc

    subject_end = len(lines)
    for index in range(subject_index + 1, len(lines)):
        line = lines[index]
        if line and not line.startswith(" ") and line.endswith(":"):
            subject_end = index
            break

    insert_at = subject_end
    while insert_at > subject_index + 1 and lines[insert_at - 1].strip() == "":
        insert_at -= 1

    new_block = [
        f"    {branch_name}:",
        f"      name: {branch_name}",
        f"      code: {branch_code}",
    ]
    updated_lines = lines[:insert_at] + new_block + lines[insert_at:]
    updated_text = "\n".join(updated_lines) + "\n"

    if dry_run:
        print(f"[dry-run] Would update {TAXONOMY_PATH}")
        return

    TAXONOMY_PATH.write_text(updated_text, encoding="utf-8")


def scaffold_directories(subject_main: str, branch_name: str, dry_run: bool) -> None:
    folder_name = branch_dir(branch_name)
    targets: list[Path] = []

    for source_type_dir in SOURCE_TYPE_DIRS:
        targets.append(LIBRARY_ROOT / subject_main / folder_name / source_type_dir)

    for note_root in NOTE_ROOTS:
        targets.append(note_root / subject_main / folder_name)

    if dry_run:
        for target in targets:
            print(f"[dry-run] Would create {target}")
        return

    for target in targets:
        ensure_gitkeep(target)


def append_moc_entry(subject_main: str, branch_name: str, dry_run: bool) -> None:
    moc_path = moc_path_for_subject(subject_main)
    entry = f"- `{branch_name}`: [[{branch_name}]] (待填写分支入口)"

    if not moc_path.exists():
        message = f"MOC file is missing: {moc_path}"
        if dry_run:
            print(f"[dry-run] {message}")
            return
        raise FileNotFoundError(message)

    content = moc_path.read_text(encoding="utf-8")
    if entry in content:
        return

    lines = content.splitlines()
    try:
        section_start = next(index for index, line in enumerate(lines) if line.strip() == "## 分支列表")
    except StopIteration:
        section_start = len(lines)
        lines.extend(["", "## 分支列表"])

    insert_at = len(lines)
    for index in range(section_start + 1, len(lines)):
        if lines[index].startswith("## "):
            insert_at = index
            break

    while insert_at > section_start + 1 and lines[insert_at - 1].strip() == "":
        insert_at -= 1

    updated_lines = lines[:insert_at] + [entry] + lines[insert_at:]
    updated_text = "\n".join(updated_lines) + "\n"

    if dry_run:
        print(f"[dry-run] Would append MOC entry to {moc_path}")
        return

    moc_path.write_text(updated_text, encoding="utf-8")


def main() -> int:
    args = parse_args()

    try:
        validate_args(args.subject_main, args.branch_name, args.branch_code)
        update_subjects_yaml(args.subject_main, args.branch_name, args.branch_code, args.dry_run)
        scaffold_directories(args.subject_main, args.branch_name, args.dry_run)
        append_moc_entry(args.subject_main, args.branch_name, args.dry_run)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    mode = "Planned" if args.dry_run else "Created"
    print(
        f"{mode} branch '{args.branch_name}' under '{args.subject_main}' "
        f"with code '{args.branch_code}'."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
