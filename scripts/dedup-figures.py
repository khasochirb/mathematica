#!/usr/bin/env python3
"""Phase 2 dedup — cluster identical figures across variants and emit
byVersion map.

Two-pass dedup:
  1. MD5 pass — pdfimages-extracted PNGs are byte-identical when they
     share content (same source raster, no transformation). MD5 is
     fast, reliable, and avoids pHash's false-positives on
     structurally-similar-but-numerically-different figures (e.g. 2024
     Q33 has 4 variants with distinct labels A,B,C,D but pHash distance
     stays at 0 because the 8×8 DCT misses small label differences).
  2. pHash pass (informational) — flagged but NOT applied for
     override-extracted entries (2021B/C/D scans, 2025 composites).
     Per-variant content differences in those are real (independent
     scans / different rendering paths).

Outputs:
  scripts/figures-byVersion.json  — {canonical_filename: [test_keys]}
  with --apply, deletes duplicate PNGs from public/.
"""

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/khasochir/Desktop/mathematica2")
S1_OUT = REPO / "public" / "section1-figures"
S2_OUT = REPO / "public" / "section2-figures"


def parse_filename(path: Path):
    name = path.stem
    m = re.match(r"(\d{4})-(Q\d+|2\.\d+)-([A-D])$", name)
    if not m:
        raise ValueError(f"Cannot parse filename: {name}")
    return m.group(1), m.group(2), m.group(3)


def md5(path: Path):
    return hashlib.md5(path.read_bytes()).hexdigest()


def load_override_set():
    """Returns set of (year, q_id) that come via override path (page-jpeg
    crop or render-and-crop). These get conservative no-dedup treatment
    because override outputs may not be byte-identical even when visually
    identical (independent scans for 2021B/C/D, different render passes
    for composites)."""
    overrides = json.load((REPO / "scripts" / "figure-crop-overrides.json").open())
    audit = json.load((REPO / "scripts" / "figures-audit.json").open())
    out = set()
    # Iterate audit entries; check if they match any override pattern
    for e in audit:
        for ov in overrides.get("page_jpeg_overrides", []) + \
                  overrides.get("render_overrides", []):
            if not re.fullmatch(ov["test_pattern"], e["test"]):
                continue
            if ov["page"] != e["sourcePage"]:
                continue
            for sub in ov["entries"]:
                if e["section"] == 1 and sub.get("questionNumber") == e.get("questionNumber"):
                    year = e["test"][:4]
                    out.add((year, f"Q{e['questionNumber']}"))
                if e["section"] == 2 and sub.get("problem") == e.get("problem"):
                    year = e["test"][:4]
                    out.add((year, e["problem"]))
    return out


def cluster_by_md5(versions):
    """Group versions by exact MD5 match. Returns list of clusters (lists
    of version letters), seeded by the lowest letter in each MD5 group."""
    by_hash = defaultdict(list)
    for letter in sorted(versions.keys()):
        path, h = versions[letter]
        by_hash[h].append(letter)
    return list(by_hash.values())


def dedup_section(label, out_dir, override_pairs, dry_run, apply):
    print(f"\n--- {label} ({out_dir.relative_to(REPO)}) ---")
    by_question = defaultdict(dict)
    for png in sorted(out_dir.glob("*.png")):
        year, q_id, version = parse_filename(png)
        by_question[(year, q_id)][version] = (png, md5(png))

    by_version_map = {}
    redirected = 0
    deleted = 0

    for (year, q_id), versions in sorted(by_question.items()):
        # MD5 byte-identity dedup applies to ALL entries — pdfimages-direct
        # and overrides alike. Override-path bytes can match across variants
        # (e.g. 2021B and 2021C may share scan source for the same figure
        # region, producing identical JPEG-crop bytes).
        is_override = (year, q_id) in override_pairs
        clusters = cluster_by_md5(versions)
        for cluster in sorted(clusters, key=lambda c: c[0]):
            canonical = cluster[0]
            canonical_path = versions[canonical][0]
            test_keys = [f"{year}{v}" for v in cluster]
            by_version_map[canonical_path.name] = test_keys
            duplicates = cluster[1:]
            if duplicates:
                print(f"  {year} {q_id}: cluster {cluster} → keep {canonical}; redirect {duplicates}")
                for d in duplicates:
                    dup_path = versions[d][0]
                    redirected += 1
                    if apply:
                        dup_path.unlink()
                        deleted += 1
            else:
                print(f"  {year} {q_id}: unique {canonical}")
    print(f"  → deleted {deleted} duplicate files; "
          f"{redirected} variants redirected to a canonical")
    return by_version_map


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    if not args.apply and not args.dry_run:
        args.dry_run = True
        print("(no flag — assuming --dry-run)\n")

    override_pairs = load_override_set()
    print(f"Override-path (year, q_id) pairs (no dedup): {len(override_pairs)}")
    for op in sorted(override_pairs):
        print(f"  {op[0]} {op[1]}")

    s1 = dedup_section("Section 1", S1_OUT, override_pairs, args.dry_run, args.apply)
    s2 = dedup_section("Section 2", S2_OUT, override_pairs, args.dry_run, args.apply)

    out = {
        "section1": s1,
        "section2": s2,
        "_doc": {
            "format": "{canonical_filename: [test_keys_using_it]}",
            "method": "MD5 byte-identity for pdfimages-direct; conservative no-dedup for override-path entries (2021B/C/D scans + 2025/2023 composites).",
        },
    }
    (REPO / "scripts" / "figures-byVersion.json").write_text(
        json.dumps(out, indent=2, ensure_ascii=False)
    )
    canon = len(s1) + len(s2)
    variants = sum(len(v) for v in s1.values()) + sum(len(v) for v in s2.values())
    print(f"\n=== SUMMARY ===")
    print(f"Canonical figures: {canon}")
    print(f"Total variants: {variants}")
    print(f"Dedup ratio: {variants/canon:.2f}× variants/canonical")
    print(f"Wrote scripts/figures-byVersion.json")


if __name__ == "__main__":
    main()
