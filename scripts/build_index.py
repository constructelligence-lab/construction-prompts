#!/usr/bin/env python3
"""Generate the README library index and index/prompts.json from prompt front-matter.

The README index is generated, never hand-edited: every prompt file carries
front-matter and the same five sections, and this script turns that into the tables.

Usage:  python3 scripts/build_index.py
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / "prompts"
README = ROOT / "README.md"
INDEX = ROOT / "index" / "prompts.json"

BEGIN = "<!-- begin:index -->"
END = "<!-- end:index -->"
BADGE_BEGIN = "<!-- begin:badge -->"
BADGE_END = "<!-- end:badge -->"

SECTION_ORDER = [
    "Preconstruction",
    "Estimating and takeoff",
    "Architecture and design",
    "Visualisation and rendering",
    "Engineering",
    "Scheduling and planning",
    "Site and field operations",
    "Safety and compliance",
    "Contracts and commercial",
    "Business development",
    "Automation and analysis",
]

SECTION_BLURB = {
    "Preconstruction": "Qualifying work, framing the programme, finding the risk before you price it.",
    "Estimating and takeoff": "Sanity checks, pricing narratives, and the questions an estimator should be asked.",
    "Architecture and design": "Briefs, specifications, code checks and design review preparation.",
    "Visualisation and rendering": "Image prompts, iteration, and the words that go around a render.",
    "Engineering": "Structural and MEP sense checks, always with an engineer and never instead of one.",
    "Scheduling and planning": "Narratives, look-aheads and the records a delay claim is built from.",
    "Site and field operations": "Turning messy field notes into records somebody can act on.",
    "Safety and compliance": "Task-specific safety documents, written with a competent person.",
    "Contracts and commercial": "Notices, risk reviews and payment narratives, drafted for review.",
    "Business development": "Case studies, proposals and the writing that wins the next job.",
    "Automation and analysis": "For the person who would rather script it than retype it.",
}

FRONT_MATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def parse_front_matter(text: str) -> dict:
    match = FRONT_MATTER.match(text)
    if not match:
        return {}
    data: dict[str, object] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            data[key.strip()] = [item.strip() for item in value[1:-1].split(",") if item.strip()]
        else:
            data[key.strip()] = value
    return data


def load_prompts() -> list[dict]:
    entries = []
    for path in sorted(PROMPTS.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta = parse_front_matter(text)
        entries.append(
            {
                "title": str(meta.get("title", "")),
                "section": str(meta.get("section", "")),
                "slug": str(meta.get("slug", path.stem)),
                "models": meta.get("models", []),
                "tags": meta.get("tags", []),
                "updated": str(meta.get("updated", "")),
                "path": path.relative_to(ROOT).as_posix(),
            }
        )
    return entries


def render(entries: list[dict]) -> str:
    out: list[str] = []
    for section in SECTION_ORDER:
        group = [e for e in entries if e["section"] == section]
        if not group:
            continue
        group.sort(key=lambda e: e["title"].lower())
        out.append(f"### {section}")
        out.append("")
        blurb = SECTION_BLURB.get(section)
        if blurb:
            out.append(f"*{blurb}*")
            out.append("")
        out.append("| Prompt | File | Models | Tags |")
        out.append("| --- | --- | --- | --- |")
        for entry in group:
            models = ", ".join(entry["models"]) if entry["models"] else "any"
            tags = " ".join(f"`{tag}`" for tag in entry["tags"]) if entry["tags"] else ""
            filename = entry["path"].split("/")[-1]
            out.append(f"| **{entry['title']}** | [`{filename}`]({entry['path']}) | {models} | {tags} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def render_badge(count: int) -> str:
    return (
        f"![prompts](https://img.shields.io/badge/prompts-{count}-1f6feb) "
        "![licence](https://img.shields.io/badge/licence-CC%20BY%204.0-2ea043) "
        "![validated](https://img.shields.io/badge/index-validated%20in%20CI-6e7781)\n"
    )


def replace_block(text: str, begin: str, end: str, block: str) -> str:
    if begin not in text or end not in text:
        print(f"note: markers {begin} / {end} not found; skipped")
        return text
    head, rest = text.split(begin, 1)
    _, tail = rest.split(end, 1)
    return f"{head}{begin}\n{block}{end}{tail}"


def main() -> int:
    entries = load_prompts()
    sections = {e["section"] for e in entries}
    unknown = sections - set(SECTION_ORDER)
    if unknown:
        print(f"FAIL: prompts in unknown sections: {sorted(unknown)}")
        return 1

    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(
        json.dumps(
            {"generated_on": date.today().isoformat(), "count": len(entries), "prompts": entries},
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    if README.exists():
        text = README.read_text(encoding="utf-8")
        text = replace_block(text, BEGIN, END, render(entries))
        text = replace_block(text, BADGE_BEGIN, BADGE_END, render_badge(len(entries)))
        README.write_text(text, encoding="utf-8")

    print(f"indexed {len(entries)} prompts across {len(sections)} sections")
    return 0


if __name__ == "__main__":
    sys.exit(main())
