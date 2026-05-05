#!/usr/bin/env python3
"""Shared helpers for the Knowledge Hub maintenance scripts."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TAXONOMY_PATH = PROJECT_ROOT / "00_system" / "taxonomy" / "subjects.yaml"
LIBRARY_ROOT = PROJECT_ROOT / "02_library"
VAULT_ROOT = PROJECT_ROOT / "03_vault"

SOURCE_TYPE_TO_DIR = {
    "books": "10_books",
    "papers": "20_papers",
    "courses": "30_courses",
    "reference": "40_reference",
}

_INVALID_WINDOWS_CHARS = re.compile(r'[<>:"/\\|?*]+')
_MULTI_SPACE = re.compile(r"\s+")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the mapping-only YAML subset used by subjects.yaml."""
    root: dict[str, Any] = {}
    stack: list[tuple[int, dict[str, Any]]] = [(-1, root)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        key, separator, value = line.partition(":")
        if not separator:
            raise ValueError(f"Invalid YAML line: {raw_line!r}")

        key = key.strip()
        value = value.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()

        if not stack:
            raise ValueError("YAML indentation is invalid.")

        current = stack[-1][1]
        if value == "":
            new_mapping: dict[str, Any] = {}
            current[key] = new_mapping
            stack.append((indent, new_mapping))
        else:
            current[key] = strip_quotes(value)

    return root


def load_taxonomy() -> dict[str, Any]:
    return parse_simple_yaml(TAXONOMY_PATH.read_text(encoding="utf-8"))


def branch_dir(branch_name: str) -> str:
    return "00_general" if branch_name == "general" else branch_name


def normalize_source_type(raw_value: str) -> str:
    value = raw_value.strip().lower()
    aliases = {
        "book": "books",
        "books": "books",
        "paper": "papers",
        "papers": "papers",
        "course": "courses",
        "courses": "courses",
        "reference": "reference",
        "references": "reference",
    }
    if value not in aliases:
        allowed = ", ".join(sorted(SOURCE_TYPE_TO_DIR))
        raise ValueError(f"Unsupported source type: {raw_value!r}. Allowed: {allowed}.")
    return aliases[value]


def sanitize_fragment(text: str) -> str:
    cleaned = _INVALID_WINDOWS_CHARS.sub(" ", text)
    cleaned = _MULTI_SPACE.sub(" ", cleaned).strip(" .")
    return cleaned or "untitled"


def kebab_name(text: str) -> str:
    ascii_slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    if ascii_slug:
        return ascii_slug
    return sanitize_fragment(text).replace(" ", "-")


def first_author(author_text: str) -> str:
    cleaned = author_text.strip()
    for delimiter in (";", ",", "&", "/", " and "):
        if delimiter in cleaned:
            cleaned = cleaned.split(delimiter, 1)[0].strip()
            break
    return sanitize_fragment(cleaned)


def subject_display_name(subject_slug: str) -> str:
    return " ".join(part.capitalize() for part in subject_slug.split("-"))


def moc_path_for_subject(subject_slug: str) -> Path:
    filename = f"{subject_display_name(subject_slug)} MOC.md"
    return VAULT_ROOT / "01_moc" / subject_slug / filename


def ensure_gitkeep(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    gitkeep = directory / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")
