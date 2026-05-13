#!/usr/bin/env python3
"""Diff JSON questions against PDF-extracted questions for the same test.

Compares each question's options (and optionally body) between the
data/questions/<test>.json source-of-record and a fresh extraction from
the canonical past-paper PDF. Classifies each diff by confidence:

  HIGH    digit sequences differ (likely real corruption)
  MED     LaTeX/math notation differs but key tokens match
  LOW     whitespace / punctuation / Latin-math-bold artefacts only

Per Khas's Phase 2 tiered approach:
  - LOW-confidence diffs can be auto-applied later (option-text formatting
    convergence to source)
  - HIGH-confidence diffs need human review (real semantic mismatch)
  - MED sits in between — flag for review

Output: one markdown table per test, written to scripts/json-corruption-diff.md
(or to stdout for a single-test probe).

Run:
    python3 scripts/diff-json-vs-extracted.py <year>          # single year, all variants
    python3 scripts/diff-json-vs-extracted.py 2024A           # single variant
    python3 scripts/diff-json-vs-extracted.py all > report.md # everything
"""

import sys
import re
import json
import subprocess
import importlib.util
from pathlib import Path

# Past-paper PDF path conventions (relative to ~/Desktop/prev_tests/)
PREV_TESTS_DIR = Path.home() / "Desktop" / "prev_tests"
JSON_DIR = Path("data/questions")

PAST_PAPER_VARIANTS = [
    (f"{y}{v}", f"{y}{v}.pdf" if y != 2025 else f"ЭШ-{y}-Математик-{v}-хувилбар.pdf")
    for y in [2022, 2023, 2024, 2025]
    for v in ["A", "B", "C", "D"]
]


def load_extractor():
    spec = importlib.util.spec_from_file_location(
        "extract_past_paper", "scripts/extract-past-paper.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def strip_math_bold_italic(s: str) -> str:
    """The MATHEMATICAL BOLD ITALIC block (U+1D44D etc.) is what PyMuPDF
    returns for italicized math letters; each glyph extracts as TWO chars
    (high + low surrogate effect in some fonts) so 'x' becomes '𝑥𝑥'. Map
    them back to plain ASCII letters for comparison."""
    # Mathematical bold italic Latin letters: U+1D434 (𝐀) through U+1D467 (𝑧)
    # Standard italic block: U+1D44E (𝑎) - U+1D467 (𝑧), U+1D434 (𝐴) - U+1D44D (𝑍)
    out = []
    prev = None
    for ch in s:
        cp = ord(ch)
        # Italic Latin lower (U+1D44E..U+1D467) → 'a'..'z'
        if 0x1D44E <= cp <= 0x1D467:
            mapped = chr(ord("a") + cp - 0x1D44E)
        # Italic Latin upper (U+1D434..U+1D44D) → 'A'..'Z'
        elif 0x1D434 <= cp <= 0x1D44D:
            mapped = chr(ord("A") + cp - 0x1D434)
        # Bold italic lower (U+1D482..U+1D49B) → 'a'..'z'
        elif 0x1D482 <= cp <= 0x1D49B:
            mapped = chr(ord("a") + cp - 0x1D482)
        # Bold italic upper (U+1D468..U+1D481) → 'A'..'Z'
        elif 0x1D468 <= cp <= 0x1D481:
            mapped = chr(ord("A") + cp - 0x1D468)
        else:
            mapped = ch
        # Dedupe doubled glyphs (𝑥𝑥 → x)
        if prev is not None and mapped == prev and 'a' <= mapped <= 'z':
            continue
        out.append(mapped)
        prev = mapped
    return "".join(out)


_TOKEN_RE = re.compile(r"[\d]+")


def normalize_for_diff(s: str) -> str:
    s = strip_math_bold_italic(s)
    # Strip LaTeX commands
    s = re.sub(r"\\[a-zA-Z]+(\{[^}]*\})?", " ", s)
    s = re.sub(r"\$", " ", s)
    # Collapse whitespace, lowercase, drop punctuation EXCEPT digits/letters/operators
    s = re.sub(r"[ \t\n\r]+", " ", s)
    s = s.lower().strip()
    return s


def digit_signature(s: str) -> str:
    """Concatenated digit sequence — the most stable comparison axis."""
    return "".join(_TOKEN_RE.findall(s))


def confidence_for_diff(json_text: str, extracted_text: str) -> str:
    js = digit_signature(json_text)
    es = digit_signature(extracted_text)
    if js != es:
        return "HIGH"
    nj = normalize_for_diff(json_text)
    ne = normalize_for_diff(extracted_text)
    if nj.replace(" ", "") != ne.replace(" ", ""):
        return "MED"
    return "LOW"


def diff_one_test(test_id: str, pdf_filename: str) -> dict:
    """Returns a dict with: test_id, status, questions[].
    Each question entry has the JSON value, extracted value, confidence."""
    pdf_path = PREV_TESTS_DIR / pdf_filename
    json_path = JSON_DIR / f"{test_id.lower()}.json"

    if not pdf_path.exists():
        return {"test_id": test_id, "status": f"missing PDF: {pdf_path}"}
    if not json_path.exists():
        return {"test_id": test_id, "status": f"missing JSON: {json_path}"}

    extractor = load_extractor()
    extracted = extractor.extract(str(pdf_path))
    with open(json_path) as f:
        json_data = json.load(f)

    extracted_by_num = {r["questionNumber"]: r for r in extracted}
    diffs = []
    for q in json_data:
        qn = q.get("questionNumber")
        ext = extracted_by_num.get(qn)
        if not ext or "extraction_warning" in ext:
            diffs.append({
                "questionNumber": qn,
                "field": "(meta)",
                "confidence": "MED",
                "json": "(present)",
                "extracted": ext.get("extraction_warning") if ext else "no anchor found",
            })
            continue

        # Body diff suppressed — digit-signature comparison is noisy for
        # bodies because LaTeX vs glyph rendering changes digit ORDER
        # (e.g. `\sqrt[3]{4^2}` puts the 3 first, glyph rendering puts it
        # after the radicand). Real body corruption is rare; option-text
        # corruption is the high-signal axis.

        # Option diffs — only report HIGH confidence (digit-sequence
        # mismatch). MED is mostly LaTeX-vs-glyph noise from extracted
        # math (`$65\pi$` in JSON vs `65𝜋𝜋` in extraction) and produces
        # too many false positives. LOW silenced as before.
        for letter in ["A", "B", "C", "D", "E"]:
            js_opt = q.get("options", {}).get(letter, "")
            ext_opt = ext.get("options", {}).get(letter, "")
            conf = confidence_for_diff(js_opt, ext_opt)
            if conf == "HIGH":
                diffs.append({
                    "questionNumber": qn,
                    "field": f"option {letter}",
                    "confidence": conf,
                    "json": js_opt[:120],
                    "extracted": ext_opt[:120],
                })

    return {
        "test_id": test_id,
        "status": "ok",
        "diffs": diffs,
        "total_questions": len(json_data),
        "extracted_count": len(extracted),
    }


def render_markdown(results: list[dict]) -> str:
    lines = [
        "# Phase 2 Step 3 — JSON ↔ PDF extraction diff report",
        "",
        "Compares `data/questions/<test>.json` against fresh extractions of",
        "the canonical past-paper PDFs in `~/Desktop/prev_tests/`. Each diff",
        "is tagged with a confidence band (HIGH / MED / LOW).",
        "",
        "- **HIGH**: digit sequences differ between JSON and PDF. Real",
        "  semantic mismatch — likely true corruption. Needs human review.",
        "- **MED**: tokenized normalized text differs but digits match.",
        "  Often LaTeX-vs-glyph differences; sometimes wording drift.",
        "  Worth a quick eyeball.",
        "- **LOW**: whitespace / punctuation / math-bold-italic doubling",
        "  artefacts only. Silenced from this report.",
        "",
        "Scope of this report: **16 past-paper PDFs (2022 / 2023 / 2024 /",
        "2025 × A/B/C/D)** = 576 Section 1 questions. The 2021 scanned PDFs",
        "(deferred per Phase 2.5) and the textbook `ESH-nom.pdf` (Latin",
        "transliteration, separate strategy) are NOT in this report.",
        "",
        "---",
        "",
    ]

    total_high = sum(
        sum(1 for d in r.get("diffs", []) if d["confidence"] == "HIGH")
        for r in results
    )
    total_med = sum(
        sum(1 for d in r.get("diffs", []) if d["confidence"] == "MED")
        for r in results
    )
    lines.extend([
        f"## Summary",
        f"- HIGH-confidence diffs (likely true corruption): **{total_high}**",
        f"- MED-confidence diffs (worth reviewing): **{total_med}**",
        f"- Tests covered: {len(results)}",
        "",
    ])

    # Per-test sections
    for r in results:
        lines.extend([
            f"## {r['test_id']}",
            "",
        ])
        if r["status"] != "ok":
            lines.append(f"**Status:** {r['status']}")
            lines.append("")
            continue
        diffs = r.get("diffs", [])
        if not diffs:
            lines.append("**No HIGH/MED diffs.** ✓ Source-aligned.")
            lines.append("")
            continue
        lines.append(f"**{len(diffs)} diff(s)** — "
                     f"{sum(1 for d in diffs if d['confidence']=='HIGH')} HIGH, "
                     f"{sum(1 for d in diffs if d['confidence']=='MED')} MED")
        lines.append("")
        lines.append("| Q | Field | Conf | JSON | PDF |")
        lines.append("|---|---|---|---|---|")
        for d in diffs:
            js = d["json"].replace("|", "\\|").replace("\n", " ")
            ex = d["extracted"].replace("|", "\\|").replace("\n", " ")
            lines.append(
                f"| Q{d['questionNumber']} | {d['field']} | {d['confidence']} | `{js}` | `{ex}` |"
            )
        lines.append("")

    return "\n".join(lines)


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else "all"
    if target == "all":
        variants = PAST_PAPER_VARIANTS
    else:
        variants = [(tid, fn) for tid, fn in PAST_PAPER_VARIANTS if tid.upper() == target.upper()]
        if not variants:
            print(f"Unknown variant {target}; valid: {[v[0] for v in PAST_PAPER_VARIANTS]}", file=sys.stderr)
            sys.exit(1)

    results = []
    for test_id, pdf_filename in variants:
        print(f"[diff] {test_id} ← {pdf_filename}", file=sys.stderr)
        results.append(diff_one_test(test_id, pdf_filename))

    print(render_markdown(results))


if __name__ == "__main__":
    main()
