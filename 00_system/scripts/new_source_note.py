#!/usr/bin/env python3
"""Create a new source note in the matching subject and branch directory."""

from __future__ import annotations

import argparse
import sys

from _hub_utils import VAULT_ROOT, branch_dir, kebab_name, load_taxonomy, normalize_source_type


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a source note with fixed frontmatter in 03_vault/02_source-notes."
    )
    parser.add_argument("--title", required=True, help="Note title shown inside the markdown file.")
    parser.add_argument("--subject-main", required=True, help="Subject slug.")
    parser.add_argument("--subject-branch", required=True, help="Branch slug.")
    parser.add_argument("--zotero-key", required=True, help="Zotero item key.")
    parser.add_argument(
        "--source-type",
        required=True,
        help="books / papers / courses / reference",
    )
    parser.add_argument(
        "--filename",
        help="Optional custom file name without extension. Defaults to a slug from --title.",
    )
    parser.add_argument(
        "--status",
        default="captured",
        help="Initial note status. Default: captured.",
    )
    return parser.parse_args()


def validate_taxonomy(subject_main: str, subject_branch: str) -> None:
    taxonomy = load_taxonomy()
    if subject_main not in taxonomy:
        raise ValueError(f"Unknown subject: {subject_main}")
    if subject_branch not in taxonomy[subject_main]["branches"]:
        raise ValueError(f"Unknown branch under {subject_main}: {subject_branch}")


def build_note_content(
    title: str,
    subject_main: str,
    subject_branch: str,
    source_type: str,
    zotero_key: str,
    status: str,
) -> str:
    return f"""---
type: source-note
subject_main: {subject_main}
subject_branch: {subject_branch}
source_type: {source_type}
status: {status}
zotero_key: {zotero_key}
authors: []
year: ""
priority: medium
review_due: ""
---

# {title}

## 1. 核心内容

- 用 3 到 5 条写清这份资料在讲什么、解决什么问题、提出什么观点或结果。

## 2. 关键概念

- 概念 A：
- 概念 B：

## 3. 关键论证 / 公式 / 方法

- 关键论证：
- 关键公式：
- 关键方法：

## 4. 我的问题

- 这里有哪些地方我还没理解？

## 5. 关联笔记

- [[相关概念笔记]]
- [[相关问题笔记]]

## 6. 后续动作

- [ ] 补全作者、年份与 Zotero 条目
- [ ] 回链到对应 MOC
- [ ] 判断是否需要拆出 concept note / method note / question note
"""


def main() -> int:
    args = parse_args()

    try:
        validate_taxonomy(args.subject_main, args.subject_branch)
        source_type = normalize_source_type(args.source_type)
    except Exception as exc:  # noqa: BLE001
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    filename_stem = args.filename if args.filename else kebab_name(args.title)
    note_filename = f"{filename_stem}.md"
    target_dir = VAULT_ROOT / "02_source-notes" / args.subject_main / branch_dir(args.subject_branch)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / note_filename

    if target_path.exists():
        print(f"Error: source note already exists: {target_path}", file=sys.stderr)
        return 1

    note_content = build_note_content(
        title=args.title,
        subject_main=args.subject_main,
        subject_branch=args.subject_branch,
        source_type=source_type,
        zotero_key=args.zotero_key,
        status=args.status,
    )
    target_path.write_text(note_content, encoding="utf-8")
    print(f"Created source note at {target_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
