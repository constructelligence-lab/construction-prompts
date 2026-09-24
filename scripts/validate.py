#!/usr/bin/env python3
"""Validate the prompt library: file structure, front-matter, and the generated index."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import build_index as bi  # noqa: E402

REQUIRED_FILES = [
    "README.md",
    "index/prompts.json",
    "scripts/build_index.py",
    "scripts/validate.py",
    ".github/workflows/validate.yml",
]
REQUIRED_HEADINGS = [
    "## Use it when",
    "## The prompt",
    "## What good output looks like",
    "## Follow-ups",
    "## Guardrails",
]
MIN_PER_SECTION = 2
PLACEHOLDER = re.compile(r"\{\{[a-z0-9_]+\}\}")

errors: list[str] = []


def check_files() -> None:
    for rel in REQUIRED_FILES:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")


def check_prompt(path: Path) -> None:
    rel = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding="utf-8")
    meta = bi.parse_front_matter(text)
    for key in ("title", "section", "slug", "models", "tags", "updated"):
        if not meta.get(key):
            errors.append(f"{rel}: front-matter is missing '{key}'")
    if meta.get("section") and meta["section"] not in bi.SECTION_ORDER:
        errors.append(f"{rel}: unknown section {meta['section']!r}")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(meta.get("updated", ""))):
        errors.append(f"{rel}: updated must be YYYY-MM-DD")
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"{rel}: missing section '{heading}'")
    if not PLACEHOLDER.search(text):
        errors.append(f"{rel}: no {{placeholder}} variables, so the prompt cannot be adapted")
    body = text.split("## The prompt", 1)[-1]
    if not re.search(r"```text\n(.+?)```", body, re.S):
        errors.append(f"{rel}: '## The prompt' must contain a fenced text block")
    follows = text.split("## Follow-ups", 1)[-1].split("## Guardrails", 1)[0]
    if len([ln for ln in follows.splitlines() if ln.strip().startswith("-")]) < 2:
        errors.append(f"{rel}: give at least two follow-up prompts")


def check_sections(entries: list[dict]) -> None:
    for section in bi.SECTION_ORDER:
        count = len([e for e in entries if e["section"] == section])
        if count < MIN_PER_SECTION:
            errors.append(f"section '{section}' has {count} prompt(s); at least {MIN_PER_SECTION} required")


def check_index(entries: list[dict]) -> None:
    if not bi.INDEX.exists():
        errors.append("index/prompts.json is missing; run scripts/build_index.py")
        return
    data = json.loads(bi.INDEX.read_text(encoding="utf-8"))
    if data.get("count") != len(entries):
        errors.append(f"index/prompts.json says {data.get('count')} prompts; there are {len(entries)}")
    indexed = {p["path"] for p in data.get("prompts", [])}
    actual = {e["path"] for e in entries}
    for missing in sorted(actual - indexed):
        errors.append(f"{missing}: not present in index/prompts.json")
    for stale in sorted(indexed - actual):
        errors.append(f"{stale}: in index/prompts.json but no such file")


def check_readme(entries: list[dict]) -> None:
    text = bi.README.read_text(encoding="utf-8")
    if bi.BEGIN not in text or bi.END not in text:
        errors.append("README.md: generated index markers are missing")
        return
    block = text.split(bi.BEGIN, 1)[1].split(bi.END, 1)[0].strip("\n")
    if block.strip() != bi.render(entries).strip("\n"):
        errors.append("README.md: library index is out of date; run scripts/build_index.py")
    for entry in entries:
        if entry["title"] not in block:
            errors.append(f"README.md: {entry['title']} is missing from the index")
    if f"prompts-{len(entries)}-" not in text:
        errors.append("README.md: badge count does not match the number of prompts")


def main() -> int:
    check_files()
    entries = bi.load_prompts()
    if not entries:
        errors.append("no prompt files found under prompts/")
    for path in sorted(bi.PROMPTS.rglob("*.md")):
        check_prompt(path)
    check_sections(entries)
    check_index(entries)
    if bi.README.exists():
        check_readme(entries)

    if errors:
        print(f"FAIL: {len(errors)} problem(s)\n")
        for error in errors:
            print(f"  - {error}")
        return 1
    sections = len({e["section"] for e in entries})
    print(f"OK: {len(entries)} prompts in {sections} sections, index and README in sync")
    return 0


if __name__ == "__main__":
    sys.exit(main())
