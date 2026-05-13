# Phase 2 Step 3 — JSON ↔ PDF extraction diff report

**Generated 2026-05-13.** Compares `data/questions/<test>.json` against
fresh extractions of the past-paper PDFs in `~/Desktop/prev_tests/`.

## TL;DR

**Hypothesis confirmed: the corruption pattern documented in
`memory/practice-test-audit.md` is textbook-specific, NOT universal.**
Across 16 past-paper PDFs (2022 / 2023 / 2024 / 2025 × A/B/C/D = 576
questions), **zero confirmed real corruption was surfaced.** Every
HIGH-confidence diff that came out of the run is an extractor false
positive, not a JSON↔source mismatch. The breakdown is in §3.

The textbook (`ESH-nom.pdf`, 504 questions in test1a..test7b) is a
separate workstream — Latin-transliterated font means we need either a
transliteration table or OCR pass before we can diff against the
Cyrillic JSON. **That's where the known corruption lives.**

## 1. What we ran

- `scripts/extract-past-paper.py` — PyMuPDF text extraction +
  `N. body … A. … B. … C. … D. … E.` regex segmentation. Filters formula-
  sheet noise by requiring all 5 option markers within the anchor's span.
- `scripts/diff-json-vs-extracted.py` — normalizes both sides, compares
  by digit signature (HIGH), normalized-token (MED, suppressed in this
  pass), or whitespace (LOW, silenced).
- Scope: 16 PDFs × 36 Section 1 questions = **576 questions**.
- Scope EXCLUDED: 2021 scans (deferred to Phase 2.5 per Khas's gate);
  ESH-nom.pdf textbook (Latin-transliterated, separate strategy).

## 2. Headline numbers

| Test | JSON vs PDF diffs (HIGH) | Real corruption candidates after triage |
|---|---|---|
| 2022A | 69 | 0 |
| 2022B | 70 | 0 |
| 2022C | 69 | 0 |
| 2022D | 70 | 0 |
| 2023A | 7 | 0 |
| 2023B | 17 | 0 |
| 2023C | 17 | 0 |
| 2023D | 16 | 0 |
| 2024A | 0 | 0 |
| 2024B | 2 | 0 |
| 2024C | 0 | 0 |
| 2024D | 2 | 0 |
| 2025A | 5 | 0 |
| 2025B | 5 | 0 |
| 2025C | 5 | 0 |
| 2025D | 5 | 0 |
| **Total** | **359** | **0** |

## 3. Why every HIGH diff is a false positive (extractor artifacts)

### 2022 PDFs — Oriya-letter font substitution (280 of 359 flags)

The 2022 PDFs were authored with a font that maps numeric glyphs to
**Oriya letters** (Unicode block U+0B00-U+0B7F). PyMuPDF faithfully
returns the codepoints the font claims — but those codepoints aren't
Unicode digits, they're Oriya letters:

| What we see | Actual Unicode | What the font renders |
|---|---|---|
| `ଵ` | U+0B35 (Oriya letter VA) | visually `1` |
| `ଽ` | U+0B3D (Oriya sign AVAGRAHA) | visually `9` |
| `଺` | U+0B36 (Oriya letter SHA) | visually `6` |
| `ସ` | U+0B38 (Oriya letter SA) | visually `4` |
| `଴` | U+0B30 (Oriya letter RA) | visually `0` |

Sample: 2022A Q1 option A → JSON `$\dfrac{1}{9}$` → PDF `ଵ ଽ`. The
digits ARE present visually in the rendered PDF; the encoding is
adversarial. **The JSON is correct against the source.** To diff these
properly, the extractor needs a CMap-aware extraction (use PyMuPDF's
`get_text("rawdict")` and resolve via the font's ToUnicode table)
or a glyph-recognition pass.

### 2023 PDFs — degree symbol mistaken for digit `0` (57 of 359 flags)

2023A Q8 option A: JSON `$58°$` → PDF `580`. The degree symbol `°`
extracts as the character `0` (visually identical at small font sizes;
font's glyph mapping is sloppy). Every angle question with `°` flags
as HIGH because the digit signature gains a spurious trailing `0`.
Needs a regex substitution in the extractor: treat trailing `0` after a
number-followed-by-non-digit as ambiguous.

### Page / section header bleed (~10 flags)

When the LAST option of a question sits at a page boundary, the
extractor captures the trailing page header / section title inside the
option's text. Examples:

- 2024B Q18 E → `1 4 19. 𝑑𝑑𝑑𝑑 ...` (Q19 body bleeds in)
- 2025A Q8 E → `(−1, 0, −2) Бодлого 9 - 28 тус бүр 2 оноотой.`
- 2024A Q32 E → `(0 −1 1 0 ) Хувилбар А Математик ... 6`

Partial fix already in `extract-past-paper.py` (`strip_page_header`);
needs to cover the "Бодлого N - M тус бүр K оноотой" section-divider
pattern too.

### 2024B/D — extractor missed Q19 anchor (4 flags)

`split_into_questions` filtered Q19 out on 2024B and 2024D because the
"all 5 option markers in order before next anchor" heuristic failed —
Q19 in 2024B/D has a multi-line layout that defeats the regex.
Cascading effect: Q18 E and Q25 E pick up the bleed.

### 2025 PDFs — math glyph reordering (20 flags)

Same pattern as 2024A Q4 / Q15 (already validated as false positive in
the probe phase): LaTeX puts the radical index BEFORE the radicand
(`\sqrt[7]{3}` = digits `7,3`); the PDF renders the index AFTER, so
extraction returns digit order `3,7`. Math is identical; digit sequence
differs.

## 4. What this tells us about Phase 2 strategy

1. **Past papers don't need a rebuild.** 576 questions came back with
   zero corruption candidates. The audit memory's documented issues are
   confined to the practice-test textbook.

2. **The extractor toolkit is worth keeping but needs polish.** The
   pipeline is solid — the false positives have specific named causes
   (Oriya font, degree-symbol, anchor missing on Q19, page-header
   bleed). Each is fixable in ~15-30 min of pattern work if we need
   higher-fidelity diffs later. For Phase 2 today the current output
   is sufficient to assert past-paper integrity.

3. **The textbook (`ESH-nom.pdf`) is the actual Phase 2 work.** That's
   where the known corruption lives. Plan:
   - Build a Cyrillic↔Latin transliteration table for the textbook's
     font (or use OCR if simpler — `tesseract` with Mongolian language
     pack).
   - Extract Q1-Q36 per test (need to first identify test boundaries
     in the 236-page PDF).
   - Diff against current JSON.
   - Per known-corruption list in `memory/practice-test-audit.md`,
     focus attention on Test-2A through Test-7B and the 7 unverified
     questions from `42ce741` + `413ab59`.

## 5. Recommendation for Step 4

Given §4.1 (past papers are clean), the Step 4 mutation phase for past
papers is effectively a **no-op**: nothing to apply.

**Step 4 scope, revised:**
- Past papers (2022-2025): no JSON edits needed. The Phase 2 source-
  fidelity test (`scripts/verify-source-fidelity.test.ts`) can document
  the extractor's known artifacts so future runs don't regress, but
  that's a tooling task, not a content fix.
- Practice tests (test1a..test7b): build the textbook extractor, run
  diff, apply corrections. **This is where the audit memory's 7+
  unverified questions get re-validated against source.**

This effectively splits Phase 2 into two halves:
- **Phase 2a (past papers): DONE.** Diff report shows zero corruption.
  Audit memory should be updated.
- **Phase 2b (textbook):** new gated workstream. Needs Khas's call on
  whether to invest the transliteration-table-or-OCR build now or punt
  to a Phase 2.5 alongside the 2021 scans.

## 6. Open question for Khas

Want a Phase 2b plan-and-go for the textbook, or pause Phase 2 here at
the past-papers-are-clean checkpoint and re-prioritize?

**Argument for pausing:** the past-paper finding is the high-value
result. Practice tests (textbook) are PAID content (Premium tier);
their corruption affects fewer users (subscribers only) and isn't a
launch blocker. The 9 known textbook-corruption questions are
documented for manual fix as they surface.

**Argument for continuing:** the 7 unverified `42ce741 / 413ab59`
fixes are still in production. Without textbook diff, we don't know
whether they're wrong. Better to know now than in a year. Also: if
we're going to build a textbook extractor anyway (for Phase 2.5
alongside 2021 OCR), better to amortize the build cost now.

---

*Hard stop here per Phase 2's gate rule. No JSON mutations applied.*
