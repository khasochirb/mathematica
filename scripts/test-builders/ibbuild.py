"""Shared helpers for IB practice-paper builders.

House rules (practice-test-authoring core + ib-practice-test hub skill):
- every part carries a markscheme whose entry count equals its bracket;
- every part carries verify[] sympy assertions, asserted at build time;
- 'Show that' parts must end their markscheme with AG;
- question maximumMark = sum of part marks; paper totalMarks = sum of
  question maxima — asserted here so a broken paper never writes JSON.
"""
import json
import os
import re

from sympy import sympify

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

IB_MARK_RE = re.compile(r"^\(?(M\d|A\d|R\d|AG|FT)\)?$")


def assert_verified(label, verify):
    assert isinstance(verify, list) and verify, f"{label}: missing verify[]"
    for expr in verify:
        try:
            ok = sympify(expr)
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"{label}: verify does not sympify: {expr!r} ({e})")
        try:
            good = bool(ok) is True
        except TypeError:
            good = False
        if not good:
            raise SystemExit(f"{label}: verify not True: {expr!r} -> {ok}")


def part(label, body, marks, markscheme, answer, solution, verify):
    plabel = f"part ({label})"
    assert len(markscheme) == marks, (
        f"{plabel}: markscheme has {len(markscheme)} entries, bracket is [{marks}]")
    for entry in markscheme:
        assert IB_MARK_RE.match(entry["mark"]), f"{plabel}: bad mark code {entry['mark']!r}"
    if re.search(r"\bshow that\b", body, re.I):
        assert markscheme[-1]["mark"] == "AG", f"{plabel}: 'Show that' must end with AG"
    assert_verified(plabel, verify)
    return {"label": label, "body": body, "marks": marks, "markscheme": markscheme,
            "answer": answer, "solution": solution, "verify": verify}


def question(source, number, section, topic, skill_tag, parts,
             contextIntro=None, figure=None):
    total = sum(p["marks"] for p in parts)
    q = {"source": source, "number": number, "section": section,
         "maximumMark": total, "topic": topic, "skill_tag": skill_tag,
         "parts": parts}
    if contextIntro:
        q["contextIntro"] = contextIntro
    if figure:
        q["figure"] = figure
    return q


def write_paper(meta, questions, out_rel):
    grand = sum(q["maximumMark"] for q in questions)
    assert grand == meta["totalMarks"], (
        f"paper {meta['label']}: questions sum {grand} ≠ totalMarks {meta['totalMarks']}")
    nums = [q["number"] for q in questions]
    assert nums == sorted(nums) and len(set(nums)) == len(nums), "question numbering broken"
    out = os.path.join(ROOT, out_rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w") as fh:
        json.dump({"meta": meta, "questions": questions}, fh,
                  ensure_ascii=False, indent=2)
        fh.write("\n")
    n_parts = sum(len(q["parts"]) for q in questions)
    print(f"wrote {out_rel}: {len(questions)} questions, {n_parts} parts, {grand} marks")


def M1(note):
    return {"mark": "M1", "note": note}


def A1(note):
    return {"mark": "A1", "note": note}


def R1(note):
    return {"mark": "R1", "note": note}


def AG(note="answer given"):
    return {"mark": "AG", "note": note}
