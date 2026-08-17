"""The missing rungs — items for skills that have questions but cannot be probed.

The first gap batch (item_bank.py) answered "does this skill have any item at
all?" and closed all 73 zeroes. This one answers the question the adaptive
engine actually asks, which is not "any item" but "an easy one AND a hard
one". 87 skills fail that test, carrying 48.15% of the exam.

WHY A FLOOR AND A CEILING, specifically. lib/diagnostic-engine.ts decides a
topic verdict like this:

    const clearedHard = as.some((a) => a.correct && a.difficulty === 3);
    const missedEasy  = as.some((a) => !a.correct && a.difficulty === 1);

Those are exact equality tests on rungs 1 and 3. A skill whose twelve items
are all hard can never produce `missedEasy`, so a struggling student looks
identical to one who simply has not been asked yet — and the engine's own
`nextDifficulty` walks down to 1 looking for an easier probe that does not
exist. Twelve items and still unprobeable. That is the defect this closes,
and it is why most skills here need ONE item, not three: the existing
questions are fine, they are just all standing on the same rung.

SCALE. Everything here is authored on the ENGINE's 1..3 scale — 1 easy,
2 medium, 3 hard — the same scale as data/questions/*.json. This is
deliberately NOT the 2/3/4 the first gap batch used. That batch was authored
on the graph's 1..5 `typical_difficulty` scale, so its "4" means the same
rung as a paper question's "3". The two scales are reconciled in
coverage_report.py (GAP_TO_ENGINE) and the mismatch is called out for
whoever ingests esh-gap-items.json — an unconverted difficulty-4 row would
be invisible to `clearedHard`, which tests `=== 3`.

DEMAND IS READ, NOT TYPED. The worklist comes from data/skills/esh-coverage.json.
An item for a rung that is already covered is rejected, so this cannot
quietly re-author work that is already done — which is the mistake the orphan
cross-reference caught last time, when 30% of the first batch duplicated
questions we already owned.

VERIFICATION, two kinds, both at build time, same contract as item_bank.py:
  verify=  sympy assertion strings, each must sympify to True
  check=   a Python predicate for claims sympy cannot express (counting
           arguments are enumerated in full, never asserted)
Nothing is written if either fails.

ENGLISH ONLY. The Mongolian pass is one late job with a human teacher.

Run: python3 scripts/skills/rung_bank.py
"""

from __future__ import annotations

import collections
import json
import os
import sys

from sympy import (Rational, sqrt, pi, S, simplify, sympify, symbols, solve, Eq,
                   diff, integrate, binomial, factorial, limit, oo, sin, cos, tan,
                   log, exp, Abs, Matrix, expand, factor, nsimplify, gcd, floor)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ITEMS: list[dict] = []
_SEEN: set[str] = set()

RUNG_NAME = {1: "easy", 2: "medium", 3: "hard"}


def R(skill, diff, body, options, answer, verify, solution, errors, check=None):
    """One item on one rung. Raises rather than returning on any violation."""
    iid = f"{skill}--r{diff}"
    assert iid not in _SEEN, f"duplicate rung item {iid}"
    _SEEN.add(iid)
    assert diff in (1, 2, 3), f"{iid}: difficulty {diff} off the engine's 1..3 scale"
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
        "id": iid, "skill_id": skill, "difficulty": diff,
        "rung": RUNG_NAME[diff], "body": body, "options": options,
        "answer": answer, "solution": solution, "errors": errors,
        "verify": verify,
    })


def load_batches():
    here = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, here)
    import importlib
    # Same trap as item_bank: run as a script this module is __main__, so a
    # batch's `from rung_bank import R` would import a SECOND copy with its
    # own empty ITEMS list and register every item into the wrong one,
    # silently reporting nothing authored.
    sys.modules.setdefault("rung_bank", sys.modules[__name__])
    loaded = []
    for name in ("rungs_a", "rungs_b", "rungs_c", "rungs_d"):
        if os.path.exists(os.path.join(here, name + ".py")):
            importlib.import_module(name)
            loaded.append(name)
    return loaded


def main():
    cov = json.load(open(os.path.join(ROOT, "data", "skills", "esh-coverage.json")))
    graph = json.load(open(os.path.join(ROOT, "data", "skills", "esh-skills.json")))
    skills = {s["id"]: s for s in graph["skills"]}

    demand = {r["skill_id"]: list(r["missingRungs"])
              for r in cov["worklistInWeightOrder"]}
    order = [r["skill_id"] for r in cov["worklistInWeightOrder"]]
    total_needed = sum(len(v) for v in demand.values())
    weight_at_risk = cov["counts"]["weightAtRisk"]

    loaded = load_batches()

    # Every item must answer a rung that is genuinely missing.
    problems = []
    filled = collections.defaultdict(set)
    for it in ITEMS:
        sid, d = it["skill_id"], it["difficulty"]
        if sid not in skills:
            problems.append(f"{it['id']}: unknown skill")
            continue
        if sid not in demand:
            problems.append(f"{it['id']}: {sid} is already covered — nothing to fill")
            continue
        if d not in demand[sid]:
            problems.append(
                f"{it['id']}: {sid} needs rungs {demand[sid]}, not {d} "
                f"({RUNG_NAME[d]}) — this rung already has items")
            continue
        filled[sid].add(d)
    if problems:
        for p in problems:
            print("REJECTED " + p, file=sys.stderr)
        raise SystemExit(1)

    done_weight = 0.0
    fully_done = []
    for sid, rungs in demand.items():
        if filled.get(sid) == set(rungs):
            fully_done.append(sid)
            done_weight += skills[sid]["exam_weight"]
    remaining = [s for s in order if s not in fully_done]

    print("=" * 74)
    print("MISSING-RUNG BANK — skills that have questions but cannot be probed")
    print("=" * 74)
    print(f"  batches loaded       {', '.join(loaded) or '(none)'}")
    print(f"  skills needing work  {len(demand)}")
    print(f"  rungs to fill        {total_needed}")
    print(f"  items authored       {len(ITEMS)}")
    print(f"  skills fully closed  {len(fully_done)}")
    print(f"  weight at risk       {weight_at_risk:.2f}%")
    print(f"  weight closed        {done_weight:.2f}%")
    print(f"  weight remaining     {weight_at_risk - done_weight:.2f}%")

    if remaining:
        print("\n  still open, heaviest first:")
        for sid in remaining[:20]:
            got = sorted(filled.get(sid, ()))
            want = demand[sid]
            print(f"    {skills[sid]['exam_weight']:5.2f}%  {sid:<40s} "
                  f"need {[RUNG_NAME[r] for r in want]}"
                  + (f", have {[RUNG_NAME[r] for r in got]}" if got else ""))
        if len(remaining) > 20:
            print(f"    ... and {len(remaining) - 20} more")

    out = {
        "note": ("Generated by scripts/skills/rung_bank.py. Difficulty is on the "
                 "ENGINE scale 1=easy 2=medium 3=hard, matching data/questions/*.json "
                 "and lib/diagnostic-engine.ts. This is NOT the 2/3/4 scale used by "
                 "esh-gap-items.json, which is the graph's 1..5 typical_difficulty."),
        "difficultyScale": {"1": "easy", "2": "medium", "3": "hard",
                            "matches": "data/questions/*.json and lib/diagnostic-engine.ts"},
        "authoredInWeightOrder": True,
        "counts": {
            "skillsNeedingWork": len(demand),
            "rungsToFill": total_needed,
            "itemsAuthored": len(ITEMS),
            "skillsFullyClosed": len(fully_done),
            "weightAtRisk": weight_at_risk,
            "weightClosed": round(done_weight, 2),
            "weightRemaining": round(weight_at_risk - done_weight, 2),
        },
        "batchesLoaded": loaded,
        "remainingSkillsInWeightOrder": remaining,
        "items": ITEMS,
    }
    path = os.path.join(ROOT, "data", "skills", "esh-rung-items.json")
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=2)
    print(f"\nwrote {os.path.relpath(path, ROOT)}  ({len(ITEMS)} items)")

    def q(v):
        return "'" + str(v).replace("'", "''") + "'"

    lines = [
        "-- The missing rungs: items that give a skill the difficulty level it lacked.",
        "-- GENERATED by scripts/skills/rung_bank.py. Do not hand-edit.",
        "--",
        "-- These skills already had questions. What they did not have was a floor or a",
        "-- ceiling, and lib/diagnostic-engine.ts reaches a verdict by testing",
        "--   a.correct && a.difficulty === 3     (cleared hard)",
        "--   !a.correct && a.difficulty === 1    (missed easy)",
        "-- so a skill whose every question is hard can never register a struggling",
        "-- student, no matter how many questions it has.",
        "--",
        "-- hub is 'eysh' to match the CHECK constraint on skills.hub in migration 010.",
        "-- difficulty is already the engine scale here (1/2/3) — these items were",
        "-- authored on it, unlike esh_gap_items.sql which is converted on the way out.",
        f"-- {len(ITEMS)} items across {len(fully_done)} skills, "
        f"{done_weight:.2f}% of exam weight.",
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
            f"  ({q(it['id'])}, {q(it['skill_id'])}, 'eysh', {it['difficulty']}, "
            f"{q(it['body'])}, {q(json.dumps(it['options'], ensure_ascii=False))}::jsonb, "
            f"{q(it['answer'])}, {q(it['solution'])}, "
            f"{q(json.dumps(it['errors'], ensure_ascii=False))}::jsonb)"
        )
    lines.append(",\n".join(vals))
    lines += ["on conflict (id) do nothing;", "", "commit;", ""]
    sql = os.path.join(ROOT, "supabase", "seed", "esh_rung_items.sql")
    os.makedirs(os.path.dirname(sql), exist_ok=True)
    with open(sql, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {os.path.relpath(sql, ROOT)}")


if __name__ == "__main__":
    main()
