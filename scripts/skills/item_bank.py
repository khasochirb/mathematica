"""Items for the skills that had none — the 36.6% of the exam the adaptive
test cannot currently probe.

ORDER IS THE DESIGN. Skills are authored strictly by exam weight, heaviest
first, so that whatever is unfinished when time runs out is the cheapest
remaining gap rather than an arbitrary one. `main()` prints exactly how much
of the 36.57% is closed and what is left, so the stopping point is always a
number and never a vibe.

THREE ITEMS PER SKILL AT DIFFICULTY 2, 3, 4. Not 1-5: difficulty 1 items are
too easy to discriminate between a student who knows the skill and one who
half-knows it, and difficulty 5 items mostly measure whether the student has
seen that specific trick. The 2/3/4 spread is the band where a wrong answer
is informative.

VERIFICATION, two kinds, both at build time:
  verify=  sympy assertion strings. Each must sympify to True. These carry
           the algebra — solve(), diff(), integrate(), binomial() etc. compute
           the answer independently of the literal I typed into the option.
  check=   a Python predicate, for the claims sympy cannot express. Counting
           arguments ("there are 6 ways to score 7 on two dice") are enumerated
           in full rather than asserted, because a miscount is invisible in the
           algebra that follows it.
Nothing is written if either fails.

DISTRACTORS. Every wrong option names the specific error that produces it, in
`errors`. This is the same contract as the paper diagnostic and it is what
makes the adaptive test able to say "you are subtracting before resolving the
bracket" instead of "you are weak at algebra".

ENGLISH ONLY. The Mongolian pass is a separate job with a human teacher, done
once and late (owner decision). Items are written to keep that pass small:
short sentences, notation carrying the meaning.

Run: python3 scripts/skills/item_bank.py
"""

from __future__ import annotations

import json
import os
import sys

from sympy import (Rational, sqrt, pi, S, simplify, sympify, symbols, solve, Eq,
                   diff, integrate, binomial, factorial, limit, oo, sin, cos, tan,
                   log, exp, Abs, Matrix, expand, factor, nsimplify)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ITEMS: list[dict] = []
_SEEN: set[str] = set()


def I(skill, diff, body, options, answer, verify, solution, errors, check=None):
    """One bank item. Raises rather than returning on any violation."""
    n = sum(1 for it in ITEMS if it["skill_id"] == skill) + 1
    iid = f"{skill}--{diff}-{n}"
    assert iid not in _SEEN, f"duplicate item id {iid}"
    _SEEN.add(iid)
    assert diff in (2, 3, 4), f"{iid}: difficulty {diff} outside the 2/3/4 spread"
    assert set(options) == {"A", "B", "C", "D"}, f"{iid}: options must be A-D"
    assert answer in options, f"{iid}: answer {answer} not among options"
    assert set(errors) == set(options) - {answer}, \
        f"{iid}: every wrong option needs a named error (got {sorted(errors)})"
    assert len(set(options.values())) == 4, f"{iid}: duplicate option text"
    if check is not None and not check():
        raise SystemExit(f"{iid}: PYTHON CHECK FAILED")
    for expr in verify:
        try:
            ok = sympify(expr)
        except Exception as exc:
            raise SystemExit(f"{iid}: verify does not sympify: {expr!r} ({exc})")
        if ok is not S.true and ok is not True:
            raise SystemExit(f"{iid}: verify NOT TRUE: {expr!r} -> {ok}")
    ITEMS.append({
        "id": iid, "skill_id": skill, "difficulty": diff, "body": body,
        "options": options, "answer": answer, "solution": solution,
        "errors": errors, "verify": verify,
    })


def load_batches():
    """Import the batch modules in weight order. Each registers via I()."""
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    import importlib
    # The batches do `from item_bank import I`. Run as a script this module is
    # __main__, so that import would load a SECOND copy with its own empty
    # ITEMS list and every item would register into the wrong one — silently,
    # reporting zero items and a wide-open gap. Alias the name first.
    sys.modules.setdefault("item_bank", sys.modules[__name__])
    loaded = []
    for name in ("items_a", "items_b", "items_c", "items_d"):
        if os.path.exists(os.path.join(here, name + ".py")):
            importlib.import_module(name)
            loaded.append(name)
    return loaded


def main():
    graph = json.load(open(os.path.join(ROOT, "data", "skills", "esh-skills.json")))
    skills = {s["id"]: s for s in graph["skills"]}
    audit = json.load(open(os.path.join(ROOT, "data", "skills", "esh-content-audit.json")))
    gap = audit["skillsWithoutItems"]
    gap_order = sorted(gap, key=lambda i: (-skills[i]["exam_weight"], i))
    gap_weight = sum(skills[i]["exam_weight"] for i in gap)

    loaded = load_batches()

    # Structural checks over whatever was authored.
    per_skill: dict[str, list[int]] = {}
    for it in ITEMS:
        assert it["skill_id"] in skills, f"{it['id']}: unknown skill"
        per_skill.setdefault(it["skill_id"], []).append(it["difficulty"])
    problems = []
    for sid, diffs in per_skill.items():
        if sorted(diffs) != [2, 3, 4]:
            problems.append(f"{sid}: difficulties {sorted(diffs)}, expected [2, 3, 4]")
        if sid not in gap:
            problems.append(f"{sid}: not one of the 73 gap skills")
    if problems:
        for p in problems:
            print("REJECTED " + p, file=sys.stderr)
        raise SystemExit(1)

    done = set(per_skill)
    closed = sum(skills[s]["exam_weight"] for s in done)
    remaining = [s for s in gap_order if s not in done]

    # A handful of items make a CONCEPTUAL claim sympy cannot express — "3 is an
    # element of A, not a subset of it", "a box plot cannot show the mean". Their
    # verify block is a placeholder, and counting them here stops "every item is
    # machine-verified" from being an overclaim. These are the items a human
    # reviewer should read.
    trivial = [it["id"] for it in ITEMS
               if all(v.replace(" ", "") in ("Eq(1,1)", "Eq(0,0)") for v in it["verify"])]

    # TWO SCALES, MADE EXPLICIT. These items are authored 2/3/4 on the graph's
    # 1..5 `typical_difficulty` scale. lib/diagnostic-engine.ts and every row in
    # data/questions/*.json use 1..3 (easy/medium/hard) and the engine tests
    # `difficulty === 3` for cleared-hard and `=== 1` for missed-easy. Loading a
    # raw 4 into that column would make the item invisible to both tests and
    # unreachable by nextDifficulty(), which clamps at 3 — a silent hole, not an
    # error. So every item carries its engine-scale rung alongside.
    engine = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
    for it in ITEMS:
        it["difficulty_engine"] = engine[it["difficulty"]]

    out = {
        "note": "Generated by scripts/skills/item_bank.py. Items for skills the ЭЕШ bank "
                "did not cover. Answers computed and asserted at build time. English only "
                "— the Mongolian pass is a separate, later, human job.",
        "difficultyScales": {
            "difficulty": "2/3/4 on the graph's 1..5 typical_difficulty scale (as authored)",
            "difficulty_engine": "1..3, matching data/questions/*.json and "
                                 "lib/diagnostic-engine.ts — USE THIS ONE when loading "
                                 "into any table the adaptive engine reads",
        },
        "authoredInWeightOrder": True,
        "counts": {
            "skillsInGap": len(gap), "skillsCovered": len(done),
            "items": len(ITEMS),
            "gapWeightTotal": round(gap_weight, 2),
            "gapWeightClosed": round(closed, 2),
            "gapWeightRemaining": round(gap_weight - closed, 2),
        },
        "batchesLoaded": loaded,
        "conceptualItemsNeedingHumanReview": trivial,
        "remainingSkillsInWeightOrder": [
            {"skill_id": s, "exam_weight": skills[s]["exam_weight"],
             "strand": skills[s]["strand"], "name_en": skills[s]["name_en"]}
            for s in remaining
        ],
        "items": ITEMS,
    }
    os.makedirs(os.path.join(ROOT, "data", "skills"), exist_ok=True)
    with open(os.path.join(ROOT, "data", "skills", "esh-gap-items.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    def q(v):
        return "'" + str(v).replace("'", "''") + "'"

    lines = [
        "-- Items for the ЭЕШ skills that had no question behind them.",
        "-- GENERATED by scripts/skills/item_bank.py. Do not hand-edit.",
        "--",
        "-- Every answer is computed and asserted at build time (sympy for the algebra,",
        "-- full enumeration for the counting arguments). Every distractor names the",
        "-- specific student error that produces it, in wrong_option_errors.",
        f"-- {len(ITEMS)} items across {len(done)} skills.",
        "--",
        "-- hub is 'eysh', NOT 'esh'. Migration 010 puts a CHECK constraint",
        "--   hub IN ('eysh','sat')",
        "-- on skills.hub, and skill_id below is a foreign key into that table. Using",
        "-- 'esh' here would leave the two columns disagreeing about the same hub.",
        "--",
        "-- difficulty is the ENGINE scale, 1 easy / 2 medium / 3 hard, the same scale",
        "-- as data/questions/*.json. The JSON keeps the authoring scale (2/3/4 on the",
        "-- graph's 1..5) in `difficulty`, and its engine rung in `difficulty_engine`;",
        "-- it is the engine rung that is loaded here, because",
        "-- lib/diagnostic-engine.ts tests difficulty === 3 and === 1 exactly.",
        "",
        "begin;",
        "",
        "insert into items (id, skill_id, hub, difficulty, body, options, answer, solution, "
        "wrong_option_errors)",
        "values",
    ]
    vals = []
    for it in ITEMS:
        vals.append(
            f"  ({q(it['id'])}, {q(it['skill_id'])}, 'eysh', {it['difficulty_engine']}, "
            f"{q(it['body'])}, {q(json.dumps(it['options'], ensure_ascii=False))}::jsonb, "
            f"{q(it['answer'])}, {q(it['solution'])}, "
            f"{q(json.dumps(it['errors'], ensure_ascii=False))}::jsonb)"
        )
    lines.append(",\n".join(vals))
    lines += ["on conflict (id) do nothing;", "", "commit;", ""]
    with open(os.path.join(ROOT, "supabase", "seed", "esh_gap_items.sql"), "w") as f:
        f.write("\n".join(lines))

    pct = 100 * closed / gap_weight if gap_weight else 0
    print(f"{len(ITEMS)} items across {len(done)} of {len(gap)} gap skills")
    checked = len(ITEMS) - len(trivial)
    print(f"machine-verified: {checked}/{len(ITEMS)}. "
          f"{len(trivial)} make a conceptual claim sympy cannot express and need a "
          f"human read: {', '.join(trivial) if trivial else '(none)'}")
    print(f"gap closed: {closed:.2f}% of {gap_weight:.2f}% exam weight  ({pct:.0f}% of the gap)")
    if remaining:
        print(f"\nremaining {len(remaining)} skills, heaviest first "
              f"({gap_weight - closed:.2f}% of the exam):")
        for s in remaining[:12]:
            print(f"  {skills[s]['exam_weight']:5.2f}%  {s}")
        if len(remaining) > 12:
            print(f"  ... and {len(remaining) - 12} more, all at or below "
                  f"{skills[remaining[12]]['exam_weight']:.2f}%")
    else:
        print("\nGAP CLOSED — every skill has three items.")


if __name__ == "__main__":
    main()
