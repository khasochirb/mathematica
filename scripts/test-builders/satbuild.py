"""
Shared SAT builder framework — the authoring TOOLS for practice tests.

Any model authoring a new SAT test writes only a thin builder script:
question stems, parameter values, distractor error models, and verify[]
strings. Everything mechanical lives here: sympy assertion of verify[],
ascending-option ordering with derived answer letters (College Board
convention), option-collision detection, SPR length rules, figure-dims
readback via PIL, and blueprint-conformance checking (domain counts,
difficulty mix, SPR slots, answer-letter runs) that crashes the build on
drift instead of shipping it.

Usage (see scripts/test-builders/sat-practice-2.py for a worked example):

    from satbuild import TestBuilder
    tb = TestBuilder("sat-practice-3", figdir_prefix="sat-p3")
    qs.append(tb.mcq_numeric("SAT-P3-M1-Q01", "1", 1, "algebra",
        "linear_equations_one_var", "easy", body, solution, verify,
        correct, {distractor_value: "error name", ...},
        expect_letter="D"))
    ...
    tb.check_module("module1", m1, diff_mix={"easy": 8, ...},
                    spr_slots={4, 9, ...}, domains={"algebra": 7, ...})
    tb.write({"module1": m1, ...}, meta)

Companion figure tools: scripts/test-figures/satfigs.py.
Rules of the road: .claude/skills/practice-test-authoring/SKILL.md.
"""

import json
import re
from collections import Counter
from pathlib import Path

from sympy import simplify, sympify

REPO = Path(__file__).resolve().parent.parent.parent
FIGDIR = REPO / "public" / "sat-figures"


def assert_verified(qid: str, verify: list[str]) -> None:
    """Every verify[] entry must sympify to True — else crash the build."""
    for expr in verify:
        try:
            ok = sympify(expr)
        except Exception as e:  # noqa: BLE001
            raise SystemExit(f"{qid}: verify does not sympify: {expr!r} ({e})")
        if ok is not True and ok != True:  # noqa: E712
            raise SystemExit(f"{qid}: verify not True: {expr!r} -> {ok}")


def figure(name: str, alt_en: str) -> dict:
    """Figure ref for public/sat-figures/<name>.png; true pixel dims are
    read via PIL when the PNG exists (re-run the builder after the figure
    script), placeholder dims otherwise."""
    src = f"/sat-figures/{name}.png"
    width, height = 900, 620
    png = FIGDIR / f"{name}.png"
    if png.is_file():
        from PIL import Image
        with Image.open(png) as im:
            width, height = im.size
    return {"src": src, "alt_en": alt_en, "width": width, "height": height}


def mcq_numeric(qid, module, qnum, domain, skill, difficulty, body, solution,
                verify, correct, distractors, fmt=None, fig=None,
                expect_letter=None):
    """Numeric MCQ. Options are sorted ASCENDING by value (College Board
    convention) and the answer letter is DERIVED from the sort, then
    checked against the blueprint's expected letter so a distractor edit
    can't silently move the key. `distractors` maps value -> error name
    (the name documents WHICH student mistake produces that option)."""
    fmt = fmt or (lambda v: f"${v}$")
    vals = [correct] + list(distractors)
    assert len({simplify(v) for v in vals}) == 4, f"{qid}: option collision"
    ordered = sorted(vals, key=lambda v: float(simplify(v)))
    letters = "ABCD"
    options = {letters[i]: fmt(v) for i, v in enumerate(ordered)}
    answer = letters[ordered.index(correct)]
    if expect_letter:
        assert answer == expect_letter, \
            f"{qid}: answer letter {answer} != blueprint {expect_letter}"
    # The answer letter is DERIVED from the ascending sort, so the solution's
    # closing line can never be trusted to a hand-typed letter — rewrite it.
    solution = re.sub(r"correct answer is \*\*[A-D]\*\*",
                      f"correct answer is **{answer}**", solution)
    assert_verified(qid, verify)
    q = {"source": qid, "module": module, "questionNumber": qnum,
         "format": "mcq", "domain": domain, "skill_tag": skill,
         "difficulty": difficulty, "body": body, "options": options,
         "answer": answer, "solution": solution, "verify": verify}
    if fig:
        q["figure"] = fig
    return q


def mcq_listed(qid, module, qnum, domain, skill, difficulty, body, options,
               answer, solution, verify, fig=None):
    """MCQ with hand-ordered options (expressions, equations, statements,
    coordinate pairs). Order them logically — by leading coefficient,
    boundary value, or first coordinate — never randomly."""
    assert sorted(options) == list("ABCD"), f"{qid}: options must be A-D"
    assert len(set(options.values())) == 4, f"{qid}: duplicate option text"
    assert answer in options, f"{qid}: answer {answer} not an option"
    m = re.search(r"correct answer is \*\*([A-D])\*\*", solution)
    assert not m or m.group(1) == answer, \
        f"{qid}: solution names **{m.group(1)}** but the answer is {answer}"
    assert_verified(qid, verify)
    q = {"source": qid, "module": module, "questionNumber": qnum,
         "format": "mcq", "domain": domain, "skill_tag": skill,
         "difficulty": difficulty, "body": body, "options": options,
         "answer": answer, "solution": solution, "verify": verify}
    if fig:
        q["figure"] = fig
    return q


def spr(qid, module, qnum, domain, skill, difficulty, body, accepted,
        solution, verify, fig=None):
    """Student-produced response. `accepted` must list EVERY enterable
    form (improper fraction + decimal for non-integers); 5-char limit,
    6 with a minus sign — asserted here."""
    for a in accepted:
        limit = 6 if a.startswith("-") else 5
        assert len(a) <= limit, f"{qid}: SPR answer {a!r} too long"
    assert_verified(qid, verify)
    q = {"source": qid, "module": module, "questionNumber": qnum,
         "format": "spr", "domain": domain, "skill_tag": skill,
         "difficulty": difficulty, "body": body,
         "acceptedAnswers": accepted, "solution": solution,
         "verify": verify}
    if fig:
        q["figure"] = fig
    return q


def check_module(key, qs, diff_mix, spr_slots, domains):
    """Blueprint conformance: 22 questions numbered 1..22, exact
    difficulty mix, exact SPR positions, exact domain counts, and no run
    of 4 identical answer letters. Call once per module before write()."""
    assert len(qs) == 22, f"{key}: {len(qs)} questions"
    assert [q["questionNumber"] for q in qs] == list(range(1, 23)), \
        f"{key}: question numbers not 1..22"
    got_diff = Counter(q["difficulty"] for q in qs)
    assert got_diff == Counter(diff_mix), f"{key}: difficulty mix {got_diff}"
    got_spr = {q["questionNumber"] for q in qs if q["format"] == "spr"}
    assert got_spr == set(spr_slots), f"{key}: SPR at {sorted(got_spr)}"
    got_dom = Counter(q["domain"] for q in qs)
    assert got_dom == Counter(domains), f"{key}: domains {got_dom}"
    letters = [q["answer"] for q in qs if q["format"] == "mcq"]
    run, prev = 1, None
    for a in letters:
        run = run + 1 if a == prev else 1
        prev = a
        assert run < 4, f"{key}: run of 4 answer letter {a}"
    hist = Counter(letters)
    print(f"  {key}: 22 ok, letters {dict(sorted(hist.items()))}, "
          f"spr at {sorted(got_spr)}")


def write_test(out_path: Path, meta: dict, modules: dict) -> None:
    """Dump the final test JSON with unique-source assertion."""
    all_qs = [q for qs in modules.values() for q in qs]
    sources = [q["source"] for q in all_qs]
    assert len(set(sources)) == len(sources), "duplicate source ids"
    n_fig = sum(1 for q in all_qs if "figure" in q)
    data = {"meta": meta, **modules}
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"wrote {out_path.relative_to(REPO)}: {len(all_qs)} questions, "
          f"{n_fig} figures")
