#!/usr/bin/env python3
"""Phase 3 — verify all 20 past-paper JSONs parse, the figure field shape
is correct, and every figure.src resolves to an existing file in
public/section{1,2}-figures/.

Complement to verify-section2-load.ts (which only covers Section 2).
This script also checks Section 1 wiring.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/khasochir/Desktop/mathematica2")
DATA = REPO / "data" / "questions"
PUBLIC = REPO / "public"

YEARS = ["2021", "2022", "2023", "2024", "2025"]
VARIANTS = ["A", "B", "C", "D"]


def assert_figure_shape(label, fig):
    issues = []
    if not isinstance(fig.get("src"), str):
        issues.append(f"{label}: src not a string")
    if not isinstance(fig.get("alt_mn"), str) or not fig["alt_mn"]:
        issues.append(f"{label}: alt_mn missing")
    if not isinstance(fig.get("alt_en"), str) or not fig["alt_en"]:
        issues.append(f"{label}: alt_en missing")
    if not isinstance(fig.get("width"), int) or fig["width"] <= 0:
        issues.append(f"{label}: width invalid ({fig.get('width')})")
    if not isinstance(fig.get("height"), int) or fig["height"] <= 0:
        issues.append(f"{label}: height invalid ({fig.get('height')})")
    return issues


def main():
    issues = []
    s1_count = 0
    s2_count = 0
    files_seen = set()

    for year in YEARS:
        for v in VARIANTS:
            tk = f"{year}{v}"
            # Section 1
            f1 = DATA / f"{tk.lower()}.json"
            if f1.exists():
                try:
                    data = json.load(f1.open())
                except Exception as e:
                    issues.append(f"{f1.name}: parse error — {e}")
                    continue
                for q in data:
                    fig = q.get("figure")
                    if fig is None:
                        continue
                    qn = q.get("questionNumber")
                    label = f"{tk} Q{qn}"
                    issues.extend(assert_figure_shape(label, fig))
                    if not fig["src"].startswith("/section1-figures/"):
                        issues.append(f"{label}: src must start with /section1-figures/, got {fig['src']}")
                    path = PUBLIC / fig["src"].lstrip("/")
                    if not path.exists():
                        issues.append(f"{label}: figure file missing at {path}")
                    files_seen.add(path.name)
                    s1_count += 1

            # Section 2
            f2 = DATA / f"{tk.lower()}-section2.json"
            if f2.exists():
                try:
                    data = json.load(f2.open())
                except Exception as e:
                    issues.append(f"{f2.name}: parse error — {e}")
                    continue
                for item in data:
                    fig = item.get("figure")
                    if fig is None:
                        continue
                    p = item.get("problem")
                    sub = item.get("subproblem")
                    label = f"{tk} {p}.{sub}"
                    if sub != 1:
                        issues.append(f"{label}: figure on subproblem {sub} (must be 1)")
                    issues.extend(assert_figure_shape(label, fig))
                    if not fig["src"].startswith("/section2-figures/"):
                        issues.append(f"{label}: src must start with /section2-figures/, got {fig['src']}")
                    path = PUBLIC / fig["src"].lstrip("/")
                    if not path.exists():
                        issues.append(f"{label}: figure file missing at {path}")
                    files_seen.add(path.name)
                    s2_count += 1

    # Cross-check: every PNG on disk should be referenced by at least one entry
    s1_disk = {f.name for f in (PUBLIC / "section1-figures").glob("*.png")}
    s2_disk = {f.name for f in (PUBLIC / "section2-figures").glob("*.png")}
    orphans = (s1_disk | s2_disk) - files_seen
    if orphans:
        for o in sorted(orphans):
            issues.append(f"orphan PNG (no JSON ref): {o}")

    print(f"=== Wired-figures verification ===")
    print(f"Section 1 figure refs: {s1_count}")
    print(f"Section 2 figure refs: {s2_count}")
    print(f"Total: {s1_count + s2_count}")
    print(f"Unique PNGs referenced: {len(files_seen)}")
    print(f"PNGs on disk: {len(s1_disk) + len(s2_disk)}")
    print(f"Issues: {len(issues)}")
    for i in issues:
        print(f"  ⚠ {i}")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
