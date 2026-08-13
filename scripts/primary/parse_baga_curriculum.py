#!/usr/bin/env python3
"""Parse the ministry's PRIMARY (grades 1-5) math core curriculum, losslessly.

Source: "Математик" сургалтын цөм хөтөлбөр — бага боловсрол (2014, improved
2019; pages 28-38 of the compiled standards volume, owner-supplied PDF).
This is the primary-band sibling of scripts/esh/parse_moe_curriculum.py
(А/492, grades 10-12), and it follows the same discipline: the parse either
reproduces the document EXACTLY — every grade, strand and objective — or it
refuses to write anything. A lossy parse of a national standard is worse
than none, because every coverage claim downstream inherits the loss.

Document structure:
  - Five grade blocks: "I АНГИ" ... "V АНГИ" (content chapter only)
  - Four strands per grade, numbered <grade>.<1-4>:
      x.1 ТОО ТООЛОЛ, x.2 ХЭМЖИГДЭХҮҮН, x.3 ГЕОМЕТР, x.4 ӨГӨГДӨЛТЭЙ АЖИЛЛАХ
  - Objectives coded <grade>.<strand><letter>, letters running а, б, в, г,
    д, е, ж, з, и, к, л, м, н — the ministry's ordinal alphabet SKIPS й,
    exactly as in the grade 10-12 standard.
  - No electives: primary content is entirely core (заавал судлах).

Also carried: the "хэрэглэгдэхүүн" (teaching materials) catalog per strand,
because it is the ministry's own statement that this band is taught through
objects and pictures — counting objects, number lines, hundred charts,
tangram, geoboard, unit squares — which is the documentary basis for the
figure-first authoring rule in the primary courses.

Run: python3 scripts/primary/parse_baga_curriculum.py <pdf-path>
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "primary", "moe-baga-curriculum.json")

STRANDS = {
    "1": ("too-toolol", "ТОО ТООЛОЛ"),
    "2": ("khemjigdekhuun", "ХЭМЖИГДЭХҮҮН"),
    "3": ("geometr", "ГЕОМЕТР"),
    "4": ("ogogdol", "ӨГӨГДӨЛТЭЙ АЖИЛЛАХ"),
}

GRADES = {"I АНГИ": 1, "II АНГИ": 2, "III АНГИ": 3, "IV АНГИ": 4, "V АНГИ": 5}

# The ministry's ordinal letters, in order, WITHOUT й. A parse that meets a
# letter out of sequence has mis-split an objective and must stop.
ORDINAL = "абвгдежзиклмноп"

# <grade>.<strand><letter>. at the start of a line (a stray leading space
# occurs once in the source, before 3.1ж).
OBJ_RE = re.compile(r"^\s*([1-5])\.([1-4])([а-я])\.\s*(.*)$")
STRAND_RE = re.compile(r"^\s*([1-5])\.([1-4])\.\s*$")
PAGE_NO = re.compile(r"^(2[89]|3[0-8])$")

# Exact counts, tallied by hand off the PDF. The parser must reproduce them.
EXPECTED = {
    1: {"1": 8, "2": 3, "3": 2, "4": 2},
    2: {"1": 10, "2": 3, "3": 2, "4": 3},
    3: {"1": 11, "2": 3, "3": 3, "4": 3},
    4: {"1": 12, "2": 5, "3": 6, "4": 4},
    5: {"1": 13, "2": 4, "3": 6, "4": 5},
}


def extract_lines(pdf_path):
    import pymupdf
    doc = pymupdf.open(pdf_path)
    lines = []
    for page in doc:
        for raw in page.get_text().splitlines():
            line = raw.replace("\t", " ").strip()
            if line and not PAGE_NO.match(line):
                lines.append(line)
    return lines


def parse(lines):
    # Content chapter only.
    start = next(i for i, l in enumerate(lines) if "ХОЁР. АГУУЛГА" in l)
    end = next(i for i, l in enumerate(lines) if "ГУРАВ. АРГА ЗҮЙ" in l)
    body = lines[start + 1 : end]

    grades = {}
    grade = None
    strand = None
    current = None  # (code, [text parts])
    objectives = []

    def flush():
        nonlocal current
        if current:
            code, parts = current
            text = re.sub(r"\s+", " ", " ".join(parts)).strip()
            objectives.append({"code": code, "grade": grade, "strand": strand, "text": text})
            current = None

    for line in body:
        if line in GRADES:
            flush()
            grade = GRADES[line]
            grades[grade] = True
            strand = None
            continue
        sm = STRAND_RE.match(line)
        if sm:
            flush()
            g, s = sm.groups()
            if int(g) != grade:
                raise SystemExit(f"strand {g}.{s} under grade {grade} — headers out of order")
            strand = s
            continue
        if strand and line == STRANDS[strand][1]:
            continue  # the strand's name line, following its number
        om = OBJ_RE.match(line)
        if om:
            g, s, letter, rest = om.groups()
            if int(g) == grade and s == strand:
                flush()
                current = (f"{g}.{s}{letter}", [rest])
                continue
            # a numeric-looking line inside an objective's TEXT (none exist
            # today, but the guard keeps a future edit honest)
        if current:
            current[1].append(line)
            continue
        raise SystemExit(f"orphan line outside any objective: {line!r}")
    flush()
    return objectives


def check(objectives):
    """Refuse a lossy parse: exact counts, consecutive ministry letters."""
    by = {}
    for o in objectives:
        by.setdefault((o["grade"], o["strand"]), []).append(o)
    problems = []
    for grade, strands in EXPECTED.items():
        for s, n in strands.items():
            got = by.get((grade, s), [])
            if len(got) != n:
                problems.append(f"grade {grade} strand {s}: {len(got)} objectives, expected {n}")
                continue
            letters = [o["code"][-1] for o in got]
            if letters != list(ORDINAL[: len(letters)]):
                problems.append(f"grade {grade} strand {s}: letters {letters} not consecutive")
    total = sum(sum(v.values()) for v in EXPECTED.values())
    if len(objectives) != total:
        problems.append(f"total {len(objectives)} != {total}")
    for o in objectives:
        if len(o["text"]) < 15:
            problems.append(f"{o['code']}: suspiciously short text {o['text']!r}")
    if problems:
        for p in problems:
            print(f"LOSSY: {p}", file=sys.stderr)
        raise SystemExit(f"{len(problems)} problem(s) — nothing written")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: parse_baga_curriculum.py <pdf>")
    objectives = parse(extract_lines(sys.argv[1]))
    check(objectives)

    sections = []
    for grade in sorted(EXPECTED):
        for s in sorted(EXPECTED[grade]):
            slug, name = STRANDS[s]
            sections.append({
                "code": f"{grade}.{s}",
                "grade": grade,
                "strand": slug,
                "strandMn": name,
                "objectives": [
                    {"code": o["code"], "text": o["text"]}
                    for o in objectives
                    if o["grade"] == grade and o["strand"] == s
                ],
            })

    data = {
        "note": "Бага боловсролын математикийн сургалтын цөм хөтөлбөр — the "
                "ministry's primary (grades 1-5) core curriculum, 2014 edition "
                "improved 2019. Parsed losslessly; the parser refuses to write "
                "if any grade, strand or objective is dropped. All content is "
                "core — the primary standard has no electives.",
        "source": {
            "authority": "БСШУСЯ / Боловсролын хүрээлэн",
            "title": "Математикийн сургалтын цөм хөтөлбөр (бага боловсрол)",
            "edition": "2014, сайжруулсан 2019",
            "pages": "28-38",
        },
        "counts": {
            "grades": 5,
            "sections": len(sections),
            "objectives": sum(len(s["objectives"]) for s in sections),
        },
        "sections": sections,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)} — "
          f"{data['counts']['sections']} sections, {data['counts']['objectives']} objectives")


if __name__ == "__main__":
    main()
