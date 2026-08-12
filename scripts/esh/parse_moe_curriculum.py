#!/usr/bin/env python3
"""Parse the Mongolian MOE upper-secondary mathematics curriculum into data.

Source: Боловсрол, соёл, шинжлэх ухаан, спортын сайдын 2019 оны 08 дугаар
сарын 01-ны өдрийн А/492 дугаар тушаалын гуравдугаар хавсралт — the
ministry's grade 10-12 mathematics standard.

The ministry numbers every learning objective (суралцахуйн зорилт) as
<grade>.<section><letter>, e.g. `10.5б`, and marks the ones only the
elective ("сонгон судлах") programme covers with a star. That numbering is
the spine of the whole document, so it is what we key on: every ЭЕШ course
unit records the codes it teaches, and lib/esh-course.test.ts fails if a
core objective has no unit behind it.

Run: python3 scripts/esh/parse_moe_curriculum.py <pdf>   (writes the JSON)
"""
import json
import os
import re
import sys

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))), "data", "esh", "moe-curriculum.json")

STRANDS = {
    "АЛГЕБР": "algebra",
    "ГЕОМЕТР БА ТРИГОНОМЕТР": "geometry-trigonometry",
    "АНАЛИЗЫН ЭХЛЭЛ": "analysis",
    "МАГАДЛАЛ, СТАТИСТИК": "probability-statistics",
}
GRADES = {"X АНГИ": 10, "XI АНГИ": 11, "XII АНГИ": 12}

# The source PDF prints АЛГЕБР and ГЕОМЕТР БА ТРИГОНОМЕТР for all three
# grades, but АНАЛИЗЫН ЭХЛЭЛ only once (grade 11) and МАГАДЛАЛ, СТАТИСТИК
# only twice (grades 10 and 11). Grade 12 therefore has no strand header
# after ГЕОМЕТР БА ТРИГОНОМЕТР, and everything from 12.7 on would inherit
# it. That is an omission in the ministry's own typesetting, not a reading
# of the syllabus: 12.7 is derivatives and 12.12 is random variables. The
# document's literal answer is kept as `strandInDocument`; `strand` carries
# the correction, and only these five sections differ.
STRAND_OVERRIDE = {
    "12.7": "analysis",                 # Уламжлал
    "12.8": "analysis",                 # Интеграл
    "12.9": "analysis",                 # Дараалал, цуваа
    "12.10": "analysis",                # Математик индукц
    "12.11": "analysis",                # Дифференциал тэгшитгэл
    "12.12": "probability-statistics",  # Дискрет санамсаргүй хувьсагч
    "12.13": "probability-statistics",  # Хэвийн тархалт
    "12.14": "probability-statistics",  # Комбинаторик
    "12.15": "probability-statistics",  # Магадлал
}

SECTION = re.compile(r"^(\d{2}\.\d{1,2})\.\s*$")
# The letter is Cyrillic а-я — except where the ministry's typist reached for
# a LATIN homoglyph instead: `11.10a` and `11.12a` are typed with Latin "a",
# and a Cyrillic-only class silently drops both objectives. Accept the
# lookalikes and fold them back, so every code in the output is Cyrillic.
OBJECTIVE = re.compile(r"^(\d{2}\.\d{1,2}[а-яА-Яaeopcxy])\.?(\*)?\.?\s*(.*)$")
LATIN_TO_CYRILLIC = str.maketrans("aeopcxy", "аеорсху")


def parse(pdf_path):
    import pymupdf
    doc = pymupdf.open(pdf_path)
    lines = []
    for page in doc:
        lines.extend(page.get_text().split("\n"))

    grade, strand = None, None
    sections, cur_sec, cur_obj = [], None, None

    # The PDF's page numbers (28-38) sit on their own line and get swept into
    # whatever objective is open when the page breaks. They are the only bare
    # 2-digit numbers in the document body, so stripping them at a line end is
    # safe — and leaving them in would put "…хэрэглэх 29" in the data.
    PAGE_NO = re.compile(r"\s+(2[89]|3[0-8])$")

    def flush_obj():
        if cur_obj and cur_sec is not None:
            text = " ".join(cur_obj["text"].split())
            cur_obj["text"] = PAGE_NO.sub("", text)
            if cur_obj["text"]:
                cur_sec["objectives"].append(cur_obj)

    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if stripped in GRADES:
            flush_obj(); cur_obj = None
            grade = GRADES[stripped]
            continue
        if stripped in STRANDS:
            flush_obj(); cur_obj = None
            strand = STRANDS[stripped]
            continue
        if grade is None:
            continue

        m = SECTION.match(stripped)
        if m:
            flush_obj(); cur_obj = None
            code = m.group(1)
            cur_sec = {"code": code, "grade": grade,
                       "strand": STRAND_OVERRIDE.get(code, strand),
                       "strandInDocument": strand,
                       "title": "", "objectives": []}
            sections.append(cur_sec)
            continue
        if cur_sec is not None and not cur_sec["title"] and not OBJECTIVE.match(stripped):
            # the line right after a section number is the section's name
            if stripped:
                cur_sec["title"] = re.sub(r"\s+(2[89]|3[0-8])$", "",
                                          " ".join(stripped.split()))
            continue

        m = OBJECTIVE.match(stripped)
        if m and cur_sec is not None:
            flush_obj()
            cur_obj = {"code": m.group(1).translate(LATIN_TO_CYRILLIC),
                       "elective": bool(m.group(2)), "text": m.group(3)}
            continue
        if cur_obj is not None and stripped:
            cur_obj["text"] += " " + stripped

    flush_obj()
    return sections


# The ministry letters objectives а,б,в,г,д,е,ж,з,и,к,л,м,н — Cyrillic
# ordinals SKIP й. Every section must therefore be a clean prefix of this
# run; a hole means the regex dropped an objective (it has already happened
# once, on the Latin-homoglyph codes above), so it is checked, not assumed.
ORDINAL_LETTERS = "абвгдежзиклмноп"


def check(sections):
    problems = []
    for sec in sections:
        letters = [o["code"][len(sec["code"]):] for o in sec["objectives"]]
        want = list(ORDINAL_LETTERS[:len(letters)])
        if letters != want:
            problems.append("%s: letters %s, expected %s" % (sec["code"], letters, want))
        if not sec["title"]:
            problems.append("%s: no section title" % sec["code"])
    if problems:
        raise SystemExit("curriculum parse is lossy:\n  " + "\n  ".join(problems))


def main():
    pdf = sys.argv[1] if len(sys.argv) > 1 else None
    if not pdf or not os.path.exists(pdf):
        raise SystemExit("usage: parse_moe_curriculum.py <curriculum.pdf>")
    sections = parse(pdf)
    check(sections)
    core = sum(1 for s in sections for o in s["objectives"] if not o["elective"])
    elective = sum(1 for s in sections for o in s["objectives"] if o["elective"])
    corrected = [s["code"] for s in sections
                 if s["strand"] != s["strandInDocument"]]
    data = {
        "note": (
            "Parsed from the ministry PDF by scripts/esh/parse_moe_curriculum.py. "
            "The source omits the АНАЛИЗЫН ЭХЛЭЛ and МАГАДЛАЛ, СТАТИСТИК strand "
            "headers for grade 12, so sections %s would otherwise inherit ГЕОМЕТР "
            "БА ТРИГОНОМЕТР. `strandInDocument` is what the PDF literally says; "
            "`strand` carries the correction." % ", ".join(corrected)),
        "source": {
            "authority": "Боловсрол, соёл, шинжлэх ухаан, спортын яам",
            "order": "А/492",
            "date": "2019-08-01",
            "appendix": "Гуравдугаар хавсралт",
            "subject": "МАТЕМАТИК",
            "grades": [10, 11, 12],
        },
        "counts": {"sections": len(sections), "core": core, "elective": elective},
        "sections": sections,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote %s — %d sections, %d core + %d elective objectives"
          % (os.path.relpath(OUT), len(sections), core, elective))


if __name__ == "__main__":
    main()
