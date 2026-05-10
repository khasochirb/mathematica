#!/usr/bin/env python3
"""
Phase 2 — Extract figures from past-paper PDFs.

Three extraction paths, in priority order:
  1. page_jpeg_override   — for scanned PDFs (2021 B/C/D), use the embedded
                            page-JPEG and crop a hand-tuned bbox.
  2. render_override      — for composite figures or workspace pages, render
                            the PDF page at 200dpi and crop a bbox.
  3. pdfimages direct     — default path for clean LaTeX PDFs.

Outputs:
    public/section1-figures/<year>-Q<num>-<version>.png
    public/section2-figures/<year>-2.<problem>-<version>.png

⚠ DO NOT use pdfimages alone for visual ordering. pdfimages emits images
in PDF object-stream order (creation order), NOT visual top-to-bottom.
We hit this on 2024B page 7: pdfimages emitted the parallelepiped (2.2)
before the f(x) graph (2.1), even though the graph is visually higher
on the page. Result: the audit-order matching swapped 2.1 ↔ 2.2.
Fix: use fitz (PyMuPDF) page.get_image_rects() and sort by rect.y0
ascending — fitz uses page coords with y=0 at TOP. See
get_visual_order_by_page() and build_pdfimages_index() below. The same
trap will bite anyone authoring pre-2021 years or other multi-figure
pages later.
"""

import io
import json
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

from PIL import Image

REPO = Path("/Users/khasochir/Desktop/mathematica2")
PDF_DIR = Path("/Users/khasochir/Desktop/prev_tests")
S1_OUT = REPO / "public" / "section1-figures"
S2_OUT = REPO / "public" / "section2-figures"
TMP = Path("/tmp/figextract")
RENDER_DPI = 200

LOGO_REPEAT_THRESHOLD = 3
SKIP_COVER_PAGE = 1

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


def load_overrides():
    return json.load((REPO / "scripts" / "figure-crop-overrides.json").open())


def matches_pattern(test_key: str, pattern: str) -> bool:
    return bool(re.fullmatch(pattern, test_key))


def out_filename(entry):
    test = entry["test"]
    year = test[:4]
    version = entry["version"]
    if entry["section"] == 1:
        return S1_OUT / f"{year}-Q{entry['questionNumber']}-{version}.png"
    else:
        return S2_OUT / f"{year}-{entry['problem']}-{version}.png"


def find_page_jpeg_override(test_key: str, page: int, entry: dict, overrides):
    for ov in overrides.get("page_jpeg_overrides", []):
        if not matches_pattern(test_key, ov["test_pattern"]):
            continue
        if ov["page"] != page:
            continue
        for sub in ov["entries"]:
            if sub.get("questionNumber") == entry.get("questionNumber") and \
               entry["section"] == 1:
                return sub["bbox"]
            if sub.get("problem") == entry.get("problem") and \
               entry["section"] == 2:
                return sub["bbox"]
    return None


def find_render_override(test_key: str, page: int, entry: dict, overrides):
    for ov in overrides.get("render_overrides", []):
        if not matches_pattern(test_key, ov["test_pattern"]):
            continue
        if ov["page"] != page:
            continue
        for sub in ov["entries"]:
            if sub.get("questionNumber") == entry.get("questionNumber") and \
               entry["section"] == 1:
                return sub["bbox"]
            if sub.get("problem") == entry.get("problem") and \
               entry["section"] == 2:
                return sub["bbox"]
    return None


def get_skip_pages(test_key: str, overrides) -> set:
    pages = set([SKIP_COVER_PAGE])
    pages.update(overrides.get("skip_pages", {}).get(test_key, []))
    return pages


def render_pdf_page(pdf_path: Path, page: int, dpi: int = RENDER_DPI) -> Image.Image:
    """Render one PDF page to PIL Image at given dpi using pdftoppm."""
    out = subprocess.run(
        ["pdftoppm", "-r", str(dpi), "-f", str(page), "-l", str(page),
         "-png", str(pdf_path)],
        capture_output=True, check=True,
    ).stdout
    return Image.open(io.BytesIO(out))


def extract_page_jpegs(pdf_path: Path, out_dir: Path):
    """Run `pdfimages -j` once per PDF to extract embedded page-JPEGs (for
    scanned PDFs). Returns a mapping {page_num → file path}."""
    out_dir.mkdir(parents=True, exist_ok=True)
    if any(out_dir.glob("p-*.jpg")):
        # cached
        pass
    else:
        subprocess.run(
            ["pdfimages", "-j", "-p", str(pdf_path), str(out_dir / "p")],
            check=True, capture_output=True,
        )
    page_jpegs = {}
    for f in sorted(out_dir.glob("p-*.jpg")):
        m = re.match(r"p-(\d+)-\d+\.jpg", f.name)
        if m:
            page_jpegs[int(m.group(1))] = f
    return page_jpegs


def pdfimages_list(pdf_path: Path):
    """Parse `pdfimages -list` output. Captures object ID (xref) so we can
    cross-reference with fitz position lookups for visual ordering."""
    out = subprocess.run(
        ["pdfimages", "-list", str(pdf_path)],
        capture_output=True, text=True, check=True,
    ).stdout
    rows = []
    for line in out.splitlines():
        line = line.strip()
        if not line or line.startswith("page") or line.startswith("---"):
            continue
        parts = line.split()
        if len(parts) < 14:
            continue
        # Column layout per pdfimages -list:
        # page num type width height color comp bpc enc interp object ID x-ppi y-ppi size ratio
        #  0    1   2    3     4      5    6    7   8   9       10    11  12    13    14   15
        rows.append({
            "page": int(parts[0]),
            "num": int(parts[1]),
            "type": parts[2],
            "width": int(parts[3]),
            "height": int(parts[4]),
            "xref": int(parts[10]),  # object ID
        })
    return rows


def get_visual_order_by_page(pdf_path: Path):
    """Use fitz (PyMuPDF) to determine the visual top-to-bottom order of
    embedded images on each page. Returns {page_num: [xref_in_visual_order]}.

    Fitz uses page coordinates with y=0 at TOP, so we sort by rect.y0 ascending
    (lowest y0 = top of page = first visually). Tie-break by x0 ascending
    (left-to-right when at same height).
    """
    import fitz
    out = {}
    doc = fitz.open(pdf_path)
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        page_num = page_idx + 1  # 1-indexed to match pdfimages
        triples = []
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            rects = page.get_image_rects(xref)
            if not rects:
                # Image referenced but not placed visually; skip
                continue
            # Take the first rect (an image can theoretically appear multiple
            # times on a page, but for our PDFs it's always once)
            rect = rects[0]
            triples.append((rect.y0, rect.x0, xref))
        triples.sort()  # by y0 ascending, then x0 ascending
        out[page_num] = [t[2] for t in triples]
    doc.close()
    return out


def extract_pdfimages_pngs(pdf_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    if not any(out_dir.glob("i-*.png")):
        subprocess.run(
            ["pdfimages", "-png", "-p", str(pdf_path), str(out_dir / "i")],
            check=True, capture_output=True,
        )
    return sorted(out_dir.glob("i-*.png"))


def find_logo_dims(rows):
    by_dim = defaultdict(set)
    for r in rows:
        if r["type"] == "image":
            by_dim[(r["width"], r["height"])].add(r["page"])
    return {dim for dim, pages in by_dim.items() if len(pages) >= LOGO_REPEAT_THRESHOLD}


def build_pdfimages_index(rows, files, logo_dims, skip_pages, visual_order_by_page):
    """Return {(page, in_page_idx): file_path} for question images only.

    in_page_idx is the visual top-to-bottom index (NOT the pdfimages output
    order, which follows PDF object stream order and may not match visual
    layout — see 2024B page 7 where pdfimages emits parallelepiped before
    f(x) graph but the graph is visually higher on the page).
    """
    if len(rows) != len(files):
        raise RuntimeError(
            f"pdfimages count mismatch: list={len(rows)} files={len(files)}"
        )
    # Map xref → file path. Multiple pdfimages rows can share an xref (image
    # + its smask are paired), so prefer the "image" type row when both exist.
    xref_to_file = {}
    for row, f in zip(rows, files):
        if row["type"] != "image":
            continue
        xref_to_file[row["xref"]] = f

    # For each page, drop logos and skipped pages, then walk the visual-order
    # xref list and assign in_page_idx based on visual position.
    out = {}
    for page, xref_list in visual_order_by_page.items():
        if page in skip_pages:
            continue
        # Build a lookup of (xref → row dims) for logo filtering on this page
        page_rows = {r["xref"]: r for r in rows
                     if r["page"] == page and r["type"] == "image"}
        idx = 0
        for xref in xref_list:
            row = page_rows.get(xref)
            if row is None:
                continue
            if (row["width"], row["height"]) in logo_dims:
                continue
            f = xref_to_file.get(xref)
            if f is None:
                continue
            out[(page, idx)] = f
            idx += 1
    return out


def process_test(test_key, audit_entries, overrides, dry_run=False):
    pdf_path = PDF_DIR / PDF_FILENAMES[test_key]
    tmp = TMP / test_key
    skip_pages = get_skip_pages(test_key, overrides)

    # Cache: pdfimages list, png files, page jpegs
    rows = pdfimages_list(pdf_path)
    pdfimages_files = extract_pdfimages_pngs(pdf_path, tmp / "imgs")
    logo_dims = find_logo_dims(rows)
    visual_order = get_visual_order_by_page(pdf_path)
    pdfimages_idx = build_pdfimages_index(
        rows, pdfimages_files, logo_dims, skip_pages, visual_order,
    )

    page_jpegs = None  # lazy-loaded
    rendered_pages = {}  # page → PIL image

    # Bucket entries by page so we can compute in-page indices for the
    # pdfimages path, where we match by order.
    by_page = defaultdict(list)
    for e in audit_entries:
        by_page[e["sourcePage"]].append(e)

    saved = []
    issues = []

    for page, entries in by_page.items():
        # Determine the path for THIS page's entries
        for in_page_idx, entry in enumerate(entries):
            jpeg_bbox = find_page_jpeg_override(test_key, page, entry, overrides)
            render_bbox = find_render_override(test_key, page, entry, overrides)

            dst = out_filename(entry)
            dst.parent.mkdir(parents=True, exist_ok=True)

            if jpeg_bbox:
                # Path 1: page-JPEG crop
                if page_jpegs is None:
                    page_jpegs = extract_page_jpegs(pdf_path, tmp / "pages")
                if page not in page_jpegs:
                    issues.append(f"{test_key} page {page}: no embedded page-JPEG")
                    continue
                img = Image.open(page_jpegs[page])
                cropped = img.crop(tuple(jpeg_bbox))
                if dry_run:
                    print(f"  DRY [jpeg-crop]  {test_key} p{page}  → {dst.name}  bbox={jpeg_bbox}")
                else:
                    cropped.save(dst)
                    saved.append(dst)
            elif render_bbox:
                # Path 2: render-and-crop
                if page not in rendered_pages:
                    rendered_pages[page] = render_pdf_page(pdf_path, page)
                img = rendered_pages[page]
                cropped = img.crop(tuple(render_bbox))
                if dry_run:
                    print(f"  DRY [render]     {test_key} p{page}  → {dst.name}  bbox={render_bbox}")
                else:
                    cropped.save(dst)
                    saved.append(dst)
            else:
                # Path 3: pdfimages direct
                src = pdfimages_idx.get((page, in_page_idx))
                if src is None:
                    issues.append(
                        f"{test_key} page {page} entry-{in_page_idx} "
                        f"({entry['description'][:40]}): no pdfimages source"
                    )
                    continue
                if dry_run:
                    print(f"  DRY [pdfimages]  {test_key} p{page}  → {dst.name}")
                else:
                    shutil.copy2(src, dst)
                    saved.append(dst)

    return saved, issues


def main():
    args = sys.argv[1:]
    dry_run = "--dry-run" in args
    only_year = None
    if "--year" in args:
        only_year = args[args.index("--year") + 1]

    overrides = load_overrides()
    audit = json.load((REPO / "scripts" / "figures-audit.json").open())
    by_test = defaultdict(list)
    for e in audit:
        by_test[e["test"]].append(e)

    tests = sorted(by_test) if not only_year else \
        [t for t in sorted(by_test) if t.startswith(only_year)]

    total = 0
    all_issues = []
    for test_key in tests:
        n = len(by_test[test_key])
        print(f"\n[{test_key}]  {n} expected figures")
        saved, issues = process_test(test_key, by_test[test_key], overrides, dry_run=dry_run)
        total += len(saved)
        all_issues.extend(issues)
        print(f"  → saved {len(saved)}/{n}")

    print(f"\n=== SUMMARY ===")
    print(f"Tests processed: {len(tests)}")
    print(f"Files saved: {total}")
    print(f"Issues: {len(all_issues)}")
    for issue in all_issues:
        print(f"  ⚠ {issue}")


if __name__ == "__main__":
    main()
