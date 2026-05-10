# Figures (Section 1 + Section 2)

One-pager on how the past-paper figures got into the repo and how to
re-extract or extend them.

## What's where

- **Static assets**:
  - `/public/section1-figures/<year>-Q<num>-<version>.png`
  - `/public/section2-figures/<year>-<problem>-<version>.png`
- **Audit + override + dedup state**: `scripts/figures-audit.json`,
  `scripts/figure-crop-overrides.json`, `scripts/figures-byVersion.json`
- **Source PDFs**: `~/Desktop/prev_tests/*.pdf` (not in repo)

## Naming + variant sharing

Files use the AAAA/BBBB/ABAB/ABBA mix found across variants. e.g.
`2024-Q5-A.png` is referenced by **both** 2024A and 2024C (ABAB pattern,
A=C share content). The `figure.src` field on each variant's JSON entry
points at the canonical filename — variants that share content share a
file. See `scripts/figures-byVersion.json` for the canonical → variants map.

## Re-extracting

```sh
python3 scripts/extract-figures.py        # extract all 20 PDFs
python3 scripts/extract-figures.py --year 2024
python3 scripts/dedup-figures.py --apply  # MD5-dedup duplicates
python3 scripts/verify-figure-extraction.py  # sweep-check vs audit
```

## Coverage (Phase 1 audit, 2026-05-10)

124 figures across the 20 past papers. After MD5 dedup: 81 canonical PNGs,
3.1 MB total bundle. See the gate JSON at `scripts/figures-audit-gate.json`
for per-year/per-section counts.

## Known gotchas (don't repeat my mistakes)

1. **pdfimages object-stream order ≠ visual order**. Hit on 2024B page 7:
   pdfimages returned the parallelepiped (2.2) before the f(x) graph (2.1)
   even though the graph is visually higher. Sort by fitz
   `page.get_image_rects()[*].y0` ascending instead. See the comment at the
   top of `scripts/extract-figures.py`.
2. **2021A is clean LaTeX-typeset, but 2021B/C/D are scanned PDFs**. Each
   page is a single 1275×1650 JPEG at ~160 dpi. `pdfimages` won't extract
   figures from those — use the page-JPEG + hand-tuned bbox path
   (`page_jpeg_overrides` in the override JSON).
3. **Composite figures** (Q3 2023, Q13 2025, 2.4 2025) — kept as
   single-PNG blocks for v1 per memory/section2-design.md style decision.
   Per-option splitting deferred to v1.1.
4. **2021C/2021D have no formula sheet on page 1** so their content pages
   are 1-shifted vs 2021A/B. The audit and override JSONs have
   year-specific page numbers; don't reuse 2021B's bboxes for C/D
   verbatim.
5. **pHash is too coarse** for figures with same overall structure but
   different numerical labels (e.g. 2024 Q33 with 4 distinct vertex-length
   variants all hash to distance 0). Use MD5 byte-identity for
   pdfimages-direct outputs; pHash gives false positives.

## What's NOT here

- The 14 legacy paid practice tests (test1a-test7b). Separate audit per
  `memory/practice-test-audit.md`.
- Pre-2021 years (2006-2020). Out of scope for v1.
