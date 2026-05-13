#!/usr/bin/env python3
"""Extract Section 1 (Q1-Q36) from a past-paper PDF (2022-2025).

Output: structured list of {questionNumber, body, options{A..E}, answer}.

Past papers store the answer key on the last page. We parse both the
question pages (Q1-Q36 body + options) and the key page (Q1-Q36 → letter).

Scanned 2021 PDFs are out of scope here (defer to Phase 2.5 OCR).

Run:
    python3 scripts/extract-past-paper.py <pdf-path> [--json]
"""

import fitz  # PyMuPDF
import re
import sys
import json
from pathlib import Path
from typing import Optional


# Anchors: "N." at start-of-line where N is 1-36.
QUESTION_START_RE = re.compile(r"^\s*(?P<num>\d+)\.\s", re.MULTILINE)
# Option markers — `A.` / `B.` etc preceded by start-of-line or whitespace.
# The trailing char is permitted to be anything (math glyphs sometimes sit
# directly against the period, e.g. "A.𝑦=").
OPTION_RE = re.compile(r"(?:^|(?<=\s))([A-E])\.", re.MULTILINE)


def extract_full_text(pdf_path: str) -> str:
    pdf = fitz.open(pdf_path)
    chunks = []
    for page in pdf:
        chunks.append(page.get_text("text"))
    pdf.close()
    return "\n".join(chunks)


def split_into_questions(text: str) -> list[tuple[int, str]]:
    """Return list of (question_number, raw_text) tuples for Q1..Q36.

    A "real" question anchor (vs e.g. a formula-sheet numbered item) has
    an `A.` option marker within ~600 chars of itself. Anchor candidates
    that don't pass this gate are dropped.

    For repeated anchors (same number appearing multiple times — e.g. the
    formula sheet's `1.` followed by Section-1's `1.`), we keep only the
    candidate that has the option marker.
    """
    candidates: list[tuple[int, int]] = []
    # Real-question signature: this anchor is followed by ALL FIVE option
    # markers in order (A. → B. → C. → D. → E.) before the next plausible
    # number anchor. Formula-sheet items don't satisfy this.
    for m in QUESTION_START_RE.finditer(text):
        num = int(m.group("num"))
        if not (1 <= num <= 36):
            continue
        # Find the next number-period anchor to bound our search.
        next_m = QUESTION_START_RE.search(text, m.end())
        end = next_m.start() if next_m else len(text)
        window = text[m.end():end]
        cursor = 0
        all_five = True
        for letter in ["A", "B", "C", "D", "E"]:
            mm = re.search(rf"(?:^|\s){letter}\.", window[cursor:], re.MULTILINE)
            if not mm:
                all_five = False
                break
            cursor += mm.end()
        if all_five:
            candidates.append((num, m.start()))
    # Dedupe by question number — first hit wins.
    seen: set[int] = set()
    ordered: list[tuple[int, int]] = []
    for num, pos in candidates:
        if num in seen:
            continue
        seen.add(num)
        ordered.append((num, pos))
    # Sort by document position (already the case but be explicit).
    ordered.sort(key=lambda x: x[1])
    out = []
    for i, (num, pos) in enumerate(ordered):
        end_pos = ordered[i + 1][1] if i + 1 < len(ordered) else len(text)
        out.append((num, text[pos:end_pos]))
    return out


_PAGE_HEADER_RE = re.compile(
    r"(?:Хувилбар\s+[A-ZА-ЯЁ]|Математик\b|Элсэлтийн\s+ерөнхий\s+шалгалт"
    r"|Бодлого\s+\d+(?:-ээс|-өөс|-аас|-ийн)\s+\d+|Хоёрдугаар\s+хэсэг)",
)


def strip_page_header(s: str) -> str:
    """Past-paper PDFs put a page header/footer ("Хувилбар А · Математик ·
    Элсэлтийн ерөнхий шалгалт 2024 · <page #>") on every page. When the
    LAST option of a question sits at the end of a page, our extractor
    captures the trailing page header inside option E. Cut off there."""
    m = _PAGE_HEADER_RE.search(s)
    if m:
        return s[:m.start()].rstrip()
    return s


def normalize_math_text(s: str) -> str:
    """Collapse whitespace, strip the leading 'N.' marker, normalize fraction
    line breaks. Goal: a tokenizable, comparable string."""
    s = s.replace("­", "")  # soft hyphens
    s = strip_page_header(s)
    s = re.sub(r"\s+", " ", s)
    s = s.strip()
    return s


def parse_question(num: int, raw: str) -> dict:
    """Pull body + 5 options out of the raw text for one question."""
    # Strip the leading "N." marker.
    raw = re.sub(rf"^\s*{num}\.\s+", "", raw)
    # Find option-marker positions in order. Must appear as A→B→C→D→E.
    option_hits: list[tuple[str, int, int]] = []  # (letter, start, end_of_marker)
    expected = ["A", "B", "C", "D", "E"]
    cursor = 0
    for letter in expected:
        # Match the next `<letter>.` preceded by whitespace / start-of-string.
        # Trailing whitespace not required — math glyphs sometimes sit
        # directly against the period.
        pat = re.compile(rf"(?:^|(?<=\s))({letter})\.", re.MULTILINE)
        m = pat.search(raw, cursor)
        if not m:
            break
        option_hits.append((letter, m.start(1), m.end()))
        cursor = m.end()
    if len(option_hits) < 5:
        return {
            "questionNumber": num,
            "body": normalize_math_text(raw),
            "options": {},
            "extraction_warning": f"only {len(option_hits)} of 5 options found",
        }
    body_end = option_hits[0][1]
    body = raw[:body_end]
    options: dict[str, str] = {}
    for i, (letter, _start, end_of_marker) in enumerate(option_hits):
        next_start = option_hits[i + 1][1] if i + 1 < len(option_hits) else len(raw)
        text = raw[end_of_marker:next_start]
        options[letter] = normalize_math_text(text)
    return {
        "questionNumber": num,
        "body": normalize_math_text(body),
        "options": options,
    }


def find_answer_key(text: str) -> dict[int, str]:
    """Past papers print the answer key on a 'Хариулт' or similar page.
    Look for a `Q-letter` grid. Defensive: return whatever pairs we
    can pull out, even if partial."""
    # Heuristic patterns observed: a grid like
    #   1   2   3   ...   36
    #   B   D   A   ...   C
    # Or: "1. B  2. D  3. A ..."
    # Or appendix table.
    # First pass — look for runs of letter-only lines following number runs.
    key: dict[int, str] = {}

    # Pattern: "1. B" or "1) B" or "1 B" on lines, or as a stream
    for m in re.finditer(r"(?<![A-Z0-9])(?P<num>\d{1,2})\s*[\.\)]?\s+(?P<letter>[A-E])(?!\w)", text):
        num = int(m.group("num"))
        letter = m.group("letter")
        if 1 <= num <= 36 and num not in key:
            key[num] = letter

    return key


def extract(pdf_path: str) -> list[dict]:
    text = extract_full_text(pdf_path)
    qs = split_into_questions(text)
    key = find_answer_key(text)
    out = []
    for num, raw in qs:
        rec = parse_question(num, raw)
        if num in key:
            rec["answer"] = key[num]
        out.append(rec)
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    pdf_path = sys.argv[1]
    as_json = "--json" in sys.argv
    records = extract(pdf_path)
    if as_json:
        print(json.dumps(records, ensure_ascii=False, indent=2))
    else:
        print(f"Extracted {len(records)} questions from {Path(pdf_path).name}")
        warnings = [r for r in records if "extraction_warning" in r]
        print(f"  Extraction warnings: {len(warnings)}")
        for w in warnings[:5]:
            print(f"    Q{w['questionNumber']}: {w['extraction_warning']}")
        with_answers = sum(1 for r in records if "answer" in r)
        print(f"  Answer key hits: {with_answers}/36 expected")


if __name__ == "__main__":
    main()
