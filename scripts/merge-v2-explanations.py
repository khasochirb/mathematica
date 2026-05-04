#!/usr/bin/env python3
"""
T2 merge — populate data/questions/*.json `solution` fields from the v2
explanation CSVs at /Users/khasochir/Desktop/outputs/explanations/.

Order: 34 main 1:1 CSVs first (testkey-v2.csv → testkey.json), then
algebra-batch1-v2.csv last. Last-write-wins, so the 15 hand-curated batch
explanations override their main-CSV counterparts.

CSV schemas vary across the corpus (column-name drift documented in PHASES.md
P3). Script normalizes silently:
  - explanation column: explanation_md OR explanation_v2
  - existing-solution column: existing_solution OR solution_existing
  (other columns aren't read by this merge — only `source` for matching).

Run from repo root:
  python3 scripts/merge-v2-explanations.py
"""

import csv
import json
import os
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
JSON_DIR = REPO_ROOT / "data" / "questions"
CSV_DIR = Path("/Users/khasochir/Desktop/outputs/explanations")


def explanation_value(row: dict) -> str:
    return row.get("explanation_md") or row.get("explanation_v2") or ""


def load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_json(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: list[dict]) -> None:
    # 2-space indent, trailing newline, ensure_ascii=False to keep Cyrillic +
    # LaTeX literals readable in the source. Matches existing JSON formatting.
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")


def merge_one_to_one(csv_path: Path, json_path: Path) -> tuple[int, int, int]:
    rows = load_csv(csv_path)
    questions = load_json(json_path)

    by_source = {q["source"]: q for q in questions}
    rows_by_source = {r["source"]: r for r in rows}

    merged = 0
    overwrote = 0
    skipped = 0
    for src, q in by_source.items():
        row = rows_by_source.get(src)
        if row is None:
            skipped += 1
            continue
        new_sol = explanation_value(row)
        if not new_sol:
            skipped += 1
            continue
        if q.get("solution"):
            overwrote += 1
        q["solution"] = new_sol
        merged += 1

    write_json(json_path, questions)
    return merged, overwrote, skipped


def merge_batch_overrides(csv_path: Path) -> tuple[int, int, list[str]]:
    """algebra-batch1: sources span multiple JSONs. Match by source, override
    whatever was just written by the 1:1 merge."""
    rows = load_csv(csv_path)

    # Build a global source → (json_path, question_dict) lookup
    json_files = sorted(p for p in JSON_DIR.glob("*.json"))
    source_index: dict[str, tuple[Path, dict]] = {}
    json_cache: dict[Path, list[dict]] = {}
    for jf in json_files:
        data = load_json(jf)
        json_cache[jf] = data
        for q in data:
            source_index[q["source"]] = (jf, q)

    merged = 0
    not_found = []
    touched_files: set[Path] = set()
    for r in rows:
        src = r["source"]
        new_sol = explanation_value(r)
        if not new_sol:
            continue
        target = source_index.get(src)
        if target is None:
            not_found.append(src)
            continue
        jf, q = target
        q["solution"] = new_sol
        touched_files.add(jf)
        merged += 1

    for jf in touched_files:
        write_json(jf, json_cache[jf])

    return merged, len(touched_files), not_found


def main() -> int:
    if not CSV_DIR.exists():
        print(f"FATAL: CSV dir not found: {CSV_DIR}", file=sys.stderr)
        return 1

    one_to_one = sorted(
        p for p in CSV_DIR.glob("*-v2.csv") if "algebra" not in p.name
    )
    batch_csv = CSV_DIR / "algebra-batch1-v2.csv"

    total_merged = 0
    total_overwrote = 0
    total_skipped = 0
    print(f"=== Phase 1: 1:1 main CSV → JSON merge ({len(one_to_one)} files) ===")
    for csv_path in one_to_one:
        base = csv_path.name.replace("-v2.csv", "")
        json_path = JSON_DIR / f"{base}.json"
        if not json_path.exists():
            print(f"  SKIP {csv_path.name}: no matching JSON")
            continue
        merged, overwrote, skipped = merge_one_to_one(csv_path, json_path)
        print(
            f"  {csv_path.name:25s} → {json_path.name:18s} "
            f"merged={merged:3d}  overwrote={overwrote:3d}  skipped={skipped}"
        )
        total_merged += merged
        total_overwrote += overwrote
        total_skipped += skipped

    print(f"\nPhase 1 total: merged={total_merged}, overwrote={total_overwrote}, skipped={total_skipped}")

    print(f"\n=== Phase 2: algebra-batch1 override ({batch_csv.name}) ===")
    if not batch_csv.exists():
        print(f"  SKIP: {batch_csv} not found")
    else:
        b_merged, b_files, b_not_found = merge_batch_overrides(batch_csv)
        print(f"  merged={b_merged}, files touched={b_files}")
        if b_not_found:
            print(f"  NOT FOUND: {b_not_found}")
        total_merged += b_merged

    print(f"\n=== TOTAL: {total_merged} solution-field writes ===")

    # Final audit: every JSON question now has a non-empty solution
    print(f"\n=== Post-merge audit ===")
    total_q = 0
    total_with_sol = 0
    files_with_gaps = []
    for jf in sorted(JSON_DIR.glob("*.json")):
        data = load_json(jf)
        n = len(data)
        nsol = sum(1 for q in data if q.get("solution"))
        total_q += n
        total_with_sol += nsol
        if nsol < n:
            files_with_gaps.append((jf.name, nsol, n))
    print(f"  {total_with_sol}/{total_q} questions have non-empty solutions")
    if files_with_gaps:
        print(f"  GAPS:")
        for name, nsol, n in files_with_gaps:
            print(f"    {name}: {nsol}/{n}")
        return 2
    print(f"  ✓ all questions populated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
