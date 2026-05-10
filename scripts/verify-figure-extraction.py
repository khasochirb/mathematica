#!/usr/bin/env python3
"""Sweep-verify Phase 2 figure extraction against the audit JSON.

For each audit entry, the saved PNG must exist and (if the entry came via
the pdfimages path) its width/height must match the fitz-determined
visual-order image at that (page, in_page_idx) position.

Override-path entries (page-jpeg crops for 2021B/C/D, render-and-crop for
composites) are not dimension-checked since they're hand-tuned crops; we
only verify the file exists and is non-trivial in size.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import fitz
from PIL import Image

REPO = Path("/Users/khasochir/Desktop/mathematica2")
PDF_DIR = Path("/Users/khasochir/Desktop/prev_tests")
S1_OUT = REPO / "public" / "section1-figures"
S2_OUT = REPO / "public" / "section2-figures"

PDF_FILENAMES = {
    "2021A": "2021A.pdf", "2021B": "2021B.pdf",
    "2021C": "2021C.pdf", "2021D": "2021D.pdf",
    "2022A": "2022A.pdf", "2022B": "2022B.pdf",
    "2022C": "2022C.pdf", "2022D": "2022D.pdf",
    "2023A": "2023A.pdf", "2023B": "2023B.pdf",
    "2023C": "2023C.pdf", "2023D": "2023D.pdf",
    "2024A": "2024A.pdf", "2024B": "2024B.pdf",
    "2024C": "2024C.pdf", "2024D": "2024D.pdf",
    "2025A": "ЭШ-2025-Математик-A-хувилбар.pdf",
    "2025B": "ЭШ-2025-Математик-B-хувилбар.pdf",
    "2025C": "ЭШ-2025-Математик-C-хувилбар.pdf",
    "2025D": "ЭШ-2025-Математик-D-хувилбар.pdf",
}


def matches(test_key, pattern):
    return bool(re.fullmatch(pattern, test_key))


def is_override(test_key, page, entry, overrides):
    """Returns True if this entry was extracted via render or page-jpeg
    override (not pdfimages direct). Skip dim-check for overrides."""
    for ov in overrides.get("page_jpeg_overrides", []) + \
              overrides.get("render_overrides", []):
        if not matches(test_key, ov["test_pattern"]):
            continue
        if ov["page"] != page:
            continue
        for sub in ov["entries"]:
            if entry["section"] == 1 and sub.get("questionNumber") == entry.get("questionNumber"):
                return True
            if entry["section"] == 2 and sub.get("problem") == entry.get("problem"):
                return True
    return False


def out_filename(entry):
    test = entry["test"]
    year = test[:4]
    version = entry["version"]
    if entry["section"] == 1:
        return S1_OUT / f"{year}-Q{entry['questionNumber']}-{version}.png"
    return S2_OUT / f"{year}-{entry['problem']}-{version}.png"


def main():
    audit = json.load((REPO / "scripts" / "figures-audit.json").open())
    overrides = json.load((REPO / "scripts" / "figure-crop-overrides.json").open())

    by_test_page = defaultdict(list)
    for e in audit:
        by_test_page[(e["test"], e["sourcePage"])].append(e)

    issues = []
    checked = 0
    skipped_override = 0

    for test_key in sorted({e["test"] for e in audit}):
        pdf_path = PDF_DIR / PDF_FILENAMES[test_key]
        doc = fitz.open(pdf_path)

        # Per-page visual-order map of (xref, width, height) excluding logos
        # (we don't have logo dims here so we'll just note which (w,h) are
        # candidates — it's fine for this verification since we match by
        # (page, in_page_idx) via the same logic the extractor uses).

        for (tk, page), entries in sorted(by_test_page.items()):
            if tk != test_key:
                continue
            page_obj = doc[page - 1]
            triples = []
            for img_info in page_obj.get_images(full=True):
                xref = img_info[0]
                rects = page_obj.get_image_rects(xref)
                if not rects:
                    continue
                rect = rects[0]
                triples.append((rect.y0, rect.x0, xref, img_info[2], img_info[3]))
            triples.sort()
            # Filter out logos: any (w, h) that appears across ≥3 pages is a logo.
            # We approximate: count this PDF's repeating dims.
            dim_count = defaultdict(int)
            for pi in range(len(doc)):
                pg = doc[pi]
                for ii in pg.get_images(full=True):
                    dim_count[(ii[2], ii[3])] += 1
            non_logo = [(y, x, xref, w, h) for (y, x, xref, w, h) in triples
                        if dim_count[(w, h)] < 3]

            for in_page_idx, entry in enumerate(entries):
                fn = out_filename(entry)
                if not fn.exists():
                    issues.append(f"{test_key} {entry.get('problem') or 'Q'+str(entry.get('questionNumber'))}: file missing ({fn.name})")
                    continue
                if is_override(test_key, page, entry, overrides):
                    skipped_override += 1
                    # File exists; just check it's non-trivial
                    sz = fn.stat().st_size
                    if sz < 1000:
                        issues.append(f"{test_key} {entry.get('problem') or 'Q'+str(entry.get('questionNumber'))}: file suspiciously small ({sz} bytes)")
                    continue
                # pdfimages path: dimension check
                if in_page_idx >= len(non_logo):
                    issues.append(f"{test_key} page {page} idx {in_page_idx}: no fitz image at this position (have {len(non_logo)})")
                    continue
                expected_w = non_logo[in_page_idx][3]
                expected_h = non_logo[in_page_idx][4]
                with Image.open(fn) as im:
                    actual_w, actual_h = im.size
                if (actual_w, actual_h) != (expected_w, expected_h):
                    issues.append(
                        f"{test_key} page {page} idx {in_page_idx} ({entry.get('problem') or 'Q'+str(entry.get('questionNumber'))}): "
                        f"file dims {actual_w}×{actual_h} ≠ fitz visual-order dims {expected_w}×{expected_h}"
                    )
                checked += 1
        doc.close()

    print(f"\n=== VERIFICATION ===")
    print(f"Audit entries: {len(audit)}")
    print(f"Checked via dim match (pdfimages path): {checked}")
    print(f"Skipped (override path, file existence only): {skipped_override}")
    print(f"Issues: {len(issues)}")
    for i in issues:
        print(f"  ⚠ {i}")
    sys.exit(1 if issues else 0)


if __name__ == "__main__":
    main()
