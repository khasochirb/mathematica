#!/usr/bin/env python3
"""Phase 3 — wire `figure` field into past-paper JSON files.

Reads:
  scripts/figures-audit.json       (per-entry descriptions, types, version)
  scripts/figures-byVersion.json   (canonical filename → variants)
  public/section{1,2}-figures/*.png (for actual width/height per file)

Writes (idempotent):
  data/questions/<test>.json              — Section 1: sets q.figure on
                                            matching questionNumber
  data/questions/<test>-section2.json     — Section 2: sets item.figure on
                                            problem's subproblem === 1

For each audit entry, looks up which canonical file the variant should
reference via the byVersion map, reads the PNG dimensions, and writes a
Figure object with src/alt_mn/alt_en/width/height. Re-running produces
identical output (idempotent — overwrites the existing figure field).
"""

import json
import re
from collections import defaultdict
from pathlib import Path

from PIL import Image

REPO = Path("/Users/khasochir/Desktop/mathematica2")
DATA = REPO / "data" / "questions"
S1_OUT = REPO / "public" / "section1-figures"
S2_OUT = REPO / "public" / "section2-figures"


def parse_filename(stem: str):
    """'2024-Q5-A' → ('2024', 'Q5', 'A'); '2024-2.1-A' → ('2024', '2.1', 'A')."""
    m = re.match(r"(\d{4})-(Q\d+|2\.\d+)-([A-D])", stem)
    if not m:
        raise ValueError(stem)
    return m.group(1), m.group(2), m.group(3)


def build_canonical_map():
    """Returns dict: (test_key, q_id) → canonical_filename.

    test_key: e.g. "2024A", "2024B"
    q_id: "Q5" (Section 1) or "2.1" (Section 2)
    canonical_filename: e.g. "2024-Q5-A.png"
    """
    by_version = json.load((REPO / "scripts" / "figures-byVersion.json").open())
    out = {}
    for fname, test_keys in {**by_version["section1"], **by_version["section2"]}.items():
        year, q_id, _ = parse_filename(Path(fname).stem)
        for tk in test_keys:
            out[(tk, q_id)] = fname
    return out


def build_alt_text_map():
    """Returns dict: (test_key, q_id) → audit description (used for alt
    text in v1 — same string for alt_en and alt_mn until a translation
    pass happens)."""
    audit = json.load((REPO / "scripts" / "figures-audit.json").open())
    out = {}
    for e in audit:
        if e["section"] == 1:
            q_id = f"Q{e['questionNumber']}"
        else:
            q_id = e["problem"]
        out[(e["test"], q_id)] = e["description"]
    return out


def png_dimensions(filename: str, section: int):
    base = S1_OUT if section == 1 else S2_OUT
    with Image.open(base / filename) as img:
        return img.size


def figure_for(test_key, q_id, section, canonical_map, alt_map, dim_cache):
    """Build the Figure dict for one (test, q_id). Returns None if no
    figure for this entry."""
    fname = canonical_map.get((test_key, q_id))
    if not fname:
        return None
    if fname not in dim_cache:
        dim_cache[fname] = png_dimensions(fname, section)
    w, h = dim_cache[fname]
    src_dir = "section1-figures" if section == 1 else "section2-figures"
    desc = alt_map.get((test_key, q_id), f"Figure for {q_id}")
    return {
        "src": f"/{src_dir}/{fname}",
        "alt_mn": desc,
        "alt_en": desc,
        "width": w,
        "height": h,
    }


def wire_section1(test_key, canonical_map, alt_map, dim_cache):
    f = DATA / f"{test_key.lower()}.json"
    if not f.exists():
        return 0, 0
    data = json.load(f.open())
    written = 0
    cleared = 0
    for q in data:
        qn = q.get("questionNumber")
        if qn is None:
            continue
        figure = figure_for(test_key, f"Q{qn}", 1, canonical_map, alt_map, dim_cache)
        if figure is not None:
            if q.get("figure") != figure:
                q["figure"] = figure
                written += 1
        else:
            if "figure" in q:
                # Remove stale figure entries (in case audit was tightened)
                del q["figure"]
                cleared += 1
    f.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    )
    return written, cleared


def wire_section2(test_key, canonical_map, alt_map, dim_cache):
    f = DATA / f"{test_key.lower()}-section2.json"
    if not f.exists():
        return 0, 0
    data = json.load(f.open())
    written = 0
    cleared = 0
    for item in data:
        problem = item.get("problem")
        sub = item.get("subproblem")
        if problem is None or sub is None:
            continue
        # Per design: figure is attached to subproblem === 1 only
        if sub == 1:
            figure = figure_for(test_key, problem, 2, canonical_map, alt_map, dim_cache)
        else:
            figure = None
        if figure is not None:
            if item.get("figure") != figure:
                item["figure"] = figure
                written += 1
        else:
            if "figure" in item:
                del item["figure"]
                cleared += 1
    f.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    )
    return written, cleared


def main():
    canonical_map = build_canonical_map()
    alt_map = build_alt_text_map()
    dim_cache = {}

    test_keys = sorted({key for key, _ in canonical_map.keys()})

    print("Wiring figures into question JSONs:\n")
    total_written = 0
    total_cleared = 0
    for tk in test_keys:
        w1, c1 = wire_section1(tk, canonical_map, alt_map, dim_cache)
        w2, c2 = wire_section2(tk, canonical_map, alt_map, dim_cache)
        if w1 + w2 + c1 + c2:
            print(f"  {tk}: S1 +{w1} -{c1}   S2 +{w2} -{c2}")
        total_written += w1 + w2
        total_cleared += c1 + c2

    print(f"\n=== SUMMARY ===")
    print(f"Tests touched: {len(test_keys)}")
    print(f"Figure fields set/updated: {total_written}")
    print(f"Stale figure fields cleared: {total_cleared}")


if __name__ == "__main__":
    main()
