#!/usr/bin/env python3
"""Normalize a file name and move the source file into the library."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from _hub_utils import (
    LIBRARY_ROOT,
    SOURCE_TYPE_TO_DIR,
    branch_dir,
    first_author,
    load_taxonomy,
    normalize_source_type,
    sanitize_fragment,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Move a file from anywhere into the normalized 02_library layout."
    )
    parser.add_argument("--src", required=True, help="Source file path.")
    parser.add_argument("--subject-main", required=True, help="Subject slug.")
    parser.add_argument("--subject-branch", required=True, help="Branch slug.")
    parser.add_argument(
        "--source-type",
        required=True,
        help="books / papers / courses / reference",
    )
    parser.add_argument("--title", required=True, help="Short normalized title.")
    parser.add_argument("--author", required=True, help="First author or institution.")
    parser.add_argument("--year", required=True, help="Publication year.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the target path without moving the file.",
    )
    return parser.parse_args()


def validate_taxonomy(subject_main: str, subject_branch: str) -> None:
    taxonomy = load_taxonomy()
    if subject_main not in taxonomy:
        raise ValueError(f"Unknown subject: {subject_main}")
    if subject_branch not in taxonomy[subject_main]["branches"]:
        raise ValueError(f"Unknown branch under {subject_main}: {subject_branch}")


def build_filename(source_type: str, title: str, author: str, year: str, suffix: str) -> str:
    safe_title = sanitize_fragment(title)
    safe_author = first_author(author)
    safe_year = sanitize_fragment(year)

    if source_type == "papers":
        base_name = f"{safe_year} - {safe_author} - {safe_title}"
    elif source_type == "books":
        base_name = f"{safe_author} - {safe_title} ({safe_year})"
    elif source_type == "courses":
        base_name = f"{safe_author} - {safe_title} - {safe_year}"
    else:
        base_name = f"{safe_author} - {safe_title} ({safe_year})"

    return f"{base_name}{suffix}"


def main() -> int:
    args = parse_args()

    try:
        validate_taxonomy(args.subject_main, args.subject_branch)
        source_type = normalize_source_type(args.source_type)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    src = Path(args.src).expanduser().resolve()
    if not src.exists() or not src.is_file():
        print(f"Error: source file does not exist: {src}", file=sys.stderr)
        return 1

    suffix = src.suffix
    target_dir = (
        LIBRARY_ROOT
        / args.subject_main
        / branch_dir(args.subject_branch)
        / SOURCE_TYPE_TO_DIR[source_type]
    )
    target_dir.mkdir(parents=True, exist_ok=True)
    target_filename = build_filename(source_type, args.title, args.author, args.year, suffix)
    target_path = target_dir / target_filename

    if target_path.exists():
        print(f"Error: target file already exists: {target_path}", file=sys.stderr)
        return 1

    if args.dry_run:
        print("Dry run only. No file moved.")
        print(f"Source : {src}")
        print(f"Target : {target_path}")
        return 0

    shutil.move(str(src), str(target_path))
    print(f"Moved file to {target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
