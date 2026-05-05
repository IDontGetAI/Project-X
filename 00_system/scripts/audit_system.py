#!/usr/bin/env python3
"""Run read-only structural checks for the Knowledge Hub project."""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from _hub_utils import LIBRARY_ROOT, PROJECT_ROOT, VAULT_ROOT, branch_dir, load_taxonomy


NOTE_ROOTS = [
    VAULT_ROOT / "02_source-notes",
    VAULT_ROOT / "03_concept-notes",
    VAULT_ROOT / "04_method-notes",
]
CONTENT_NOTE_ROOTS = [
    VAULT_ROOT / "02_source-notes",
    VAULT_ROOT / "03_concept-notes",
    VAULT_ROOT / "04_method-notes",
    VAULT_ROOT / "05_question-notes",
    VAULT_ROOT / "06_project-notes",
    VAULT_ROOT / "07_daily",
]
PLACEHOLDER_MARKERS = [
    "TODO",
    "待补",
    "待填写",
    "概念标题",
    "方法标题",
    "问题标题",
    "项目标题",
    "资料标题",
    "示例",
    "AB12CD34",
    "\u951f\u65a4\u62f7",
]


def iter_real_files(root: Path):
    if not root.exists():
        return
    for path in root.rglob("*"):
        if path.is_file() and path.name != ".gitkeep":
            yield path


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}

    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}

    data: dict[str, str] = {}
    for raw_line in parts[1].splitlines():
        line = raw_line.strip()
        if not line or line.startswith("- "):
            continue
        key, separator, value = line.partition(":")
        if separator:
            data[key.strip()] = value.strip().strip('"')
    return data


def find_inbox_files() -> list[Path]:
    inbox_root = PROJECT_ROOT / "01_inbox"
    return sorted(iter_real_files(inbox_root))


def find_unknown_branch_dirs(taxonomy: dict) -> list[str]:
    issues: list[str] = []
    allowed = {
        subject: {branch_dir(branch_name) for branch_name in spec["branches"]}
        for subject, spec in taxonomy.items()
    }

    for subject_path in sorted(LIBRARY_ROOT.iterdir()):
        if not subject_path.is_dir():
            continue
        if subject_path.name not in allowed:
            issues.append(f"02_library/{subject_path.name} 未在主词表中定义")
            continue
        for branch_path in sorted(subject_path.iterdir()):
            if branch_path.is_dir() and branch_path.name not in allowed[subject_path.name]:
                issues.append(f"{branch_path.relative_to(PROJECT_ROOT)} 未在主词表中定义")

    for note_root in NOTE_ROOTS:
        if not note_root.exists():
            continue
        for subject_path in sorted(note_root.iterdir()):
            if not subject_path.is_dir():
                continue
            if subject_path.name not in allowed:
                issues.append(f"{subject_path.relative_to(PROJECT_ROOT)} 的学科未在主词表中定义")
                continue
            for branch_path in sorted(subject_path.iterdir()):
                if branch_path.is_dir() and branch_path.name not in allowed[subject_path.name]:
                    issues.append(f"{branch_path.relative_to(PROJECT_ROOT)} 未在主词表中定义")

    return issues


def find_missing_zotero_keys() -> list[Path]:
    issues: list[Path] = []
    for note in sorted(iter_real_files(VAULT_ROOT / "02_source-notes")):
        if note.suffix != ".md":
            continue
        frontmatter = parse_frontmatter(note)
        zotero_key = frontmatter.get("zotero_key", "").strip()
        if not zotero_key:
            issues.append(note)
    return issues


def find_placeholder_notes() -> list[Path]:
    issues: list[Path] = []
    for root in CONTENT_NOTE_ROOTS:
        for note in sorted(iter_real_files(root)):
            if note.suffix != ".md":
                continue
            text = note.read_text(encoding="utf-8").strip()
            if len(text) < 80:
                issues.append(note)
                continue
            if any(marker in text for marker in PLACEHOLDER_MARKERS):
                issues.append(note)
    return issues


def count_library_files_per_subject(taxonomy: dict) -> dict[str, int]:
    counts = defaultdict(int)
    for subject in taxonomy:
        subject_root = LIBRARY_ROOT / subject
        if not subject_root.exists():
            continue
        counts[subject] = sum(1 for _ in iter_real_files(subject_root))
    return counts


def count_source_notes_per_subject(taxonomy: dict) -> dict[str, int]:
    counts = defaultdict(int)
    source_root = VAULT_ROOT / "02_source-notes"
    for subject in taxonomy:
        subject_root = source_root / subject
        if not subject_root.exists():
            continue
        counts[subject] = sum(1 for note in iter_real_files(subject_root) if note.suffix == ".md")
    return counts


def find_subject_imbalance(taxonomy: dict) -> list[str]:
    issues: list[str] = []
    library_counts = count_library_files_per_subject(taxonomy)
    note_counts = count_source_notes_per_subject(taxonomy)

    for subject in taxonomy:
        library_total = library_counts.get(subject, 0)
        note_total = note_counts.get(subject, 0)
        if library_total >= 1 and (note_total == 0 or note_total * 3 < library_total):
            issues.append(
                f"{subject} 的 library 文件数为 {library_total}，source note 数为 {note_total}"
            )
    return issues


def print_section(title: str, items: list[str]) -> None:
    print(f"\n## {title}")
    if not items:
        print("- 未发现问题")
        return
    for item in items:
        print(f"- {item}")


def main() -> int:
    taxonomy = load_taxonomy()

    inbox_files = [str(path.relative_to(PROJECT_ROOT)) for path in find_inbox_files()]
    unknown_branches = find_unknown_branch_dirs(taxonomy)
    missing_zotero = [str(path.relative_to(PROJECT_ROOT)) for path in find_missing_zotero_keys()]
    placeholder_notes = [str(path.relative_to(PROJECT_ROOT)) for path in find_placeholder_notes()]
    imbalance = find_subject_imbalance(taxonomy)

    print("Knowledge Hub Audit Report")
    print("=" * 27)
    print(f"Project root: {PROJECT_ROOT}")

    print_section("未归类 inbox 文件", inbox_files)
    print_section("主词表之外的 branch 目录", unknown_branches)
    print_section("缺少 zotero_key 的 source note", missing_zotero)
    print_section("明显空白或占位未填写的笔记", placeholder_notes)
    print_section("library 与 source note 明显失衡的学科", imbalance)

    total_findings = sum(
        len(group)
        for group in (inbox_files, unknown_branches, missing_zotero, placeholder_notes, imbalance)
    )
    print(f"\n总问题数: {total_findings}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
