#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill the `topics` map of every grade-placement table from the Mongolian
lesson mirrors, so placement topic titles are GENERATED, never typed.

    python3 scripts/i18n/mn_placement_topics.py          # write
    python3 scripts/i18n/mn_placement_topics.py --check  # exit 1 if stale

For each curated bank in lib/placement-bank.ts it collects the topic slugs
used by its questions, reads `title` from data/genmath/<dir>-mn/<slug>.json,
and writes i18n/placement-tables/<bank>.mn.json. The `questions` map is
preserved untouched (writers own it); a missing table is created with
`questions: {}`. A slug with no mirror is left out and reported, so the
runner falls back to the English title for it.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "lib" / "placement-bank.ts"
OUT = ROOT / "i18n" / "placement-tables"

# const name in lib/placement-bank.ts -> (table name, mirror dir)
BANKS = {
    "CURATED": ("6", "6-mn"),
    "GEO_CURATED": ("geometry", "geometry-mn"),
    "G7_CURATED": ("7", "7-mn"),
    "G8_CURATED": ("8", "8-mn"),
    "G9_CURATED": ("9", "9-mn"),
    "G10_CURATED": ("10", "10-mn"),
    "G11_CURATED": ("11", "11-mn"),
    "G12_CURATED": ("12", "12-mn"),
}


def bank_slugs(src: str) -> dict:
    out = {}
    for m in re.finditer(r"const (\w+): Curated\[\] = \[(.*?)\n\];", src, re.S):
        name, body = m.group(1), m.group(2)
        slugs = []
        for s in re.findall(r'Q\("([a-z0-9-]+)",', body):
            if s not in slugs:
                slugs.append(s)
        out[name] = slugs
    return out


def build() -> tuple:
    src = SRC.read_text(encoding="utf-8")
    found = bank_slugs(src)
    tables, missing = {}, []
    for const, (bank, mdir) in BANKS.items():
        if const not in found:
            sys.exit(f"{const} not found in {SRC}")
        path = OUT / f"{bank}.mn.json"
        old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        topics = {}
        for slug in found[const]:
            mirror = ROOT / "data" / "genmath" / mdir / f"{slug}.json"
            if not mirror.exists():
                missing.append(f"{bank}/{slug}")
                continue
            title = json.loads(mirror.read_text(encoding="utf-8")).get("title", "").strip()
            if title:
                topics[slug] = title
            else:
                missing.append(f"{bank}/{slug} (empty title)")
        tables[path] = {"topics": topics, "questions": old.get("questions", {})}
    return tables, missing


def dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2) + "\n"


def main() -> None:
    check = "--check" in sys.argv
    tables, missing = build()
    stale = []
    for path, obj in tables.items():
        text = dump(obj)
        if path.exists() and path.read_text(encoding="utf-8") == text:
            continue
        stale.append(path.relative_to(ROOT))
        if not check:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
    for m in missing:
        print(f"no Mongolian mirror title: {m}", file=sys.stderr)
    if check and stale:
        print("stale placement tables:", *stale, sep="\n  ", file=sys.stderr)
        sys.exit(1)
    if not check:
        print(f"wrote {len(stale)} table(s); {len(tables) - len(stale)} unchanged")


if __name__ == "__main__":
    main()
