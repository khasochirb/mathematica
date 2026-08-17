"""What is STILL genuinely uncovered, after the 219 gap items.

The first audit asked a binary question — does this skill have any item at
all? — and got 73 zeroes. Those are closed. This asks the question the
adaptive test actually cares about, which is not "any item" but "enough
items, spread across difficulty, to tell a guess from a grasp".

The threshold is the one the owner set for the gap batch and it is not
arbitrary: THREE items at difficulty 2/3/4. One item cannot distinguish a
student who knows the skill from a student who guessed a 4-option question;
two items at the same difficulty cannot tell you where the ceiling is. The
adaptive engine's own rule (lib/diagnostic-engine.ts) needs a cleared-hard
and a missed-easy to reach a verdict at all, so a skill whose items are all
difficulty 2 can only ever return "unknown".

So a skill counts as COVERED here when it has at least 3 items AND at least
one at difficulty <= 2 AND at least one at difficulty >= 3 — a floor and a
ceiling. Everything else is thin, and thin is ranked by exam weight, because
that is what it costs us.

TWO DIFFERENT DIFFICULTY SCALES ARE IN PLAY and conflating them is the one
way this report can lie:

  data/questions/*.json    1..3   easy / medium / hard  (evenly split, 406/408/410)
  skills[].typical_difficulty  1..5   how hard the SKILL is, not an item
  esh-gap-items.json       2/3/4  the discriminating band ON THE 1..5 SCALE

So a gap item at difficulty 4 is NOT harder than a paper item at difficulty
3 — it is the same "hard" rung counted on a longer ruler. Everything is
converted to the engine's 1..3 scale before it is compared, because that is
the scale lib/diagnostic-engine.ts actually reads (it tests `=== 3` for
cleared-hard and `=== 1` for missed-easy, and clamps with min(3)/max(1)).

Section-2 items ship no `difficulty` field at all, but every one of them
carries `difficulty_tier: "hard"` — 260 items. Reading only the numeric
field would throw that away and declare 52 mapped section-2 items
unreadable, which is how the first run of this script reported skills like
`quadratic-function-vertex` as having "12 items, none with a readable
difficulty" when in fact all twelve are hard.

Orphan questions do NOT count as coverage. They are real questions, but the
database cannot route a question whose skill_id is null, so until a tag is
confirmed they are invisible to the adaptive test. They are reported
separately as what they are: the cheapest way to close some of this.

Run: python3 scripts/skills/coverage_report.py
"""

from __future__ import annotations

import collections
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, "data", "skills")

GRAPH = json.load(open(os.path.join(D, "esh-skills.json")))
AUDIT = json.load(open(os.path.join(D, "esh-content-audit.json")))
GAP = json.load(open(os.path.join(D, "esh-gap-items.json")))
PATCH = json.load(open(os.path.join(D, "esh-patch-and-orphans.json")))

SKILLS = {s["id"]: s for s in GRAPH["skills"]}

MIN_ITEMS = 3
# The engine's scale. A "low" probe is one a student who half-knows the skill
# should still clear; a "high" probe needs the skill properly.
LOW_MAX = 1
HIGH_MIN = 3

# 1..5 (graph/gap-item scale) -> 1..3 (engine + question-bank scale).
# The gap batch only ever authors 2/3/4, so only those three rows can fire;
# 1 and 5 are mapped anyway so a future item outside the band cannot land on
# a KeyError and get silently dropped from the count.
GAP_TO_ENGINE = {1: 1, 2: 1, 3: 2, 4: 3, 5: 3}
TIER_TO_ENGINE = {"easy": 1, "medium": 2, "hard": 3}


def difficulties_by_skill():
    """(skill_id -> [difficulty, ...]) over everything the engine can route."""
    out = collections.defaultdict(list)

    # Production items that already carry a resolvable skill. The audit
    # recorded the mapping but not the difficulty, so re-read the papers.
    diff_by_qid = {}
    papers = [f"{y}{v}" for y in (2021, 2022, 2023, 2024, 2025) for v in "abcd"]
    legacy = [f"test{n}{v}" for n in range(1, 8) for v in "ab"]
    for label in papers + [f"{p}-section2" for p in papers] + legacy:
        path = os.path.join(ROOT, "data", "questions", f"{label}.json")
        if not os.path.exists(path):
            continue
        data = json.load(open(path))
        items = data if isinstance(data, list) else data.get(
            "problems", data.get("questions", []))
        for q in items:
            qid = q.get("source")
            if not qid:
                continue
            d = q.get("difficulty")
            if d is None:
                # Section 2 ships no numeric difficulty; the tier is still
                # authoritative and every section-2 item is tagged "hard".
                d = TIER_TO_ENGINE.get(q.get("difficulty_tier"))
            diff_by_qid[qid] = int(d) if d is not None else None

    unknown_difficulty = 0
    for rec in AUDIT["clean"]:
        d = diff_by_qid.get(rec["id"])
        if d is None:
            # An item whose difficulty is unreadable counts toward the item
            # total but toward NEITHER the floor nor the ceiling, so it can
            # never fake a spread into existence.
            unknown_difficulty += 1
            out[rec["skill_id"]].append(None)
        else:
            out[rec["skill_id"]].append(d)

    for it in GAP["items"]:
        out[it["skill_id"]].append(GAP_TO_ENGINE[int(it["difficulty"])])

    return out, unknown_difficulty


def classify(diffs):
    n = len(diffs)
    known = [d for d in diffs if d is not None]
    has_low = any(d <= LOW_MAX for d in known)
    has_high = any(d >= HIGH_MIN for d in known)
    if n == 0:
        return "empty", "no items at all"
    if n < MIN_ITEMS:
        return "thin", f"only {n} item{'s' if n != 1 else ''}"
    if not known:
        return "thin", f"{n} items, none with a readable difficulty"
    if not has_low and not has_high:
        return "thin", f"{n} items, all medium — no floor and no ceiling"
    if not has_high:
        return "thin", f"{n} items, none hard — no ceiling"
    if not has_low:
        return "thin", f"{n} items, none easy — no floor"
    return "covered", f"{n} items, floor and ceiling present"


def main():
    by_skill, unknown = difficulties_by_skill()

    rows = []
    for sid, s in SKILLS.items():
        diffs = by_skill.get(sid, [])
        state, why = classify(diffs)
        known = sorted(d for d in diffs if d is not None)
        # What is actually missing, as rungs on the engine's 1..3 scale. A
        # thin skill usually needs ONE item, not three — the existing ones
        # are fine, they just all sit on the same rung.
        missing = []
        if 1 not in known:
            missing.append(1)
        if 3 not in known:
            missing.append(3)
        if len(known) + len(missing) < MIN_ITEMS and 2 not in known:
            missing.append(2)
        rows.append({
            "skill_id": sid,
            "strand": s["strand"],
            "name_en": s["name_en"],
            "exam_weight": s["exam_weight"],
            "items": len(diffs),
            "difficulties": known,
            "state": state,
            "why": why,
            "missingRungs": missing if state != "covered" else [],
        })

    # Orphan strings whose confirmed tag would land on a thin/empty skill:
    # the cheapest coverage available, and it is authored already.
    thin_ids = {r["skill_id"] for r in rows if r["state"] != "covered"}
    orphan_relief = {}
    for entry in PATCH.get("emptySkillsCoveredByOrphans", []):
        if entry["skill_id"] in thin_ids:
            orphan_relief[entry["skill_id"]] = entry

    rows.sort(key=lambda r: (-r["exam_weight"], r["skill_id"]))
    need = [r for r in rows if r["state"] != "covered"]
    covered = [r for r in rows if r["state"] == "covered"]

    print("=" * 74)
    print("ЭЕШ SKILL COVERAGE — depth, not presence")
    print("=" * 74)
    print(f"  skills in graph        {len(rows)}")
    print(f"  COVERED (>=3, spread)  {len(covered)}")
    print(f"  need work              {len(need)}")
    print(f"    of which empty       {sum(1 for r in need if r['state'] == 'empty')}")
    print(f"    of which thin        {sum(1 for r in need if r['state'] == 'thin')}")
    print(f"  weight still at risk   {sum(r['exam_weight'] for r in need):.2f}%")
    print(f"  (items with no readable difficulty: {unknown})")

    print("\n" + "=" * 74)
    print("WORKLIST — highest exam weight first. This is the authoring order.")
    print("=" * 74)
    for i, r in enumerate(need, 1):
        relief = orphan_relief.get(r["skill_id"])
        tail = ""
        if relief:
            tail = (f"  <- {relief['questions']} orphan q already exist "
                    f"({relief['orphanStrings'][0] if relief.get('orphanStrings') else '?'})")
        print(f"{i:3d}. {r['exam_weight']:5.2f}%  {r['skill_id']:<42s} "
              f"{r['why']}{tail}")

    # AFTER-STATE. If the rung bank has been built, replay the same
    # classification with its items folded in. This deliberately does NOT
    # feed back into `worklistInWeightOrder` above: rung_bank.py reads that
    # worklist as its demand spec, so letting the after-state edit it would
    # make the two files chase each other and a from-scratch rebuild would
    # produce an empty worklist and silently author nothing.
    after = None
    rung_path = os.path.join(D, "esh-rung-items.json")
    if os.path.exists(rung_path):
        rung = json.load(open(rung_path))
        with_rungs = {sid: list(v) for sid, v in by_skill.items()}
        for it in rung["items"]:
            with_rungs.setdefault(it["skill_id"], []).append(int(it["difficulty"]))
        still = []
        for sid, s in SKILLS.items():
            state, why = classify(with_rungs.get(sid, []))
            if state != "covered":
                still.append({"skill_id": sid, "exam_weight": s["exam_weight"],
                              "why": why})
        still.sort(key=lambda r: -r["exam_weight"])
        after = {
            "source": "data/skills/esh-rung-items.json",
            "covered": len(SKILLS) - len(still),
            "stillThin": len(still),
            "weightStillAtRisk": round(sum(r["exam_weight"] for r in still), 2),
            "skills": still,
        }
        print("\n" + "=" * 74)
        print("AFTER the rung bank is applied")
        print("=" * 74)
        print(f"  covered              {after['covered']} / {len(SKILLS)}")
        print(f"  still thin           {after['stillThin']}")
        print(f"  weight still at risk {after['weightStillAtRisk']:.2f}%")
        for r in still[:15]:
            print(f"    {r['exam_weight']:5.2f}%  {r['skill_id']:<40s} {r['why']}")

    out = {
        "note": ("Generated by scripts/skills/coverage_report.py. 'Covered' means "
                 f">= {MIN_ITEMS} items with at least one at difficulty <= {LOW_MAX} "
                 f"and at least one >= {HIGH_MIN}. Orphans are NOT counted as "
                 "coverage: a question whose skill_id is null cannot be routed."),
        "thresholds": {"minItems": MIN_ITEMS, "lowMax": LOW_MAX, "highMin": HIGH_MIN},
        "counts": {
            "skills": len(rows),
            "covered": len(covered),
            "needWork": len(need),
            "empty": sum(1 for r in need if r["state"] == "empty"),
            "thin": sum(1 for r in need if r["state"] == "thin"),
            "weightAtRisk": round(sum(r["exam_weight"] for r in need), 2),
            "itemsToAuthor": sum(len(r["missingRungs"]) for r in need),
        },
        "worklistInWeightOrder": need,
        "orphanReliefAvailable": orphan_relief,
        "afterRungBank": after,
        "covered": covered,
    }
    path = os.path.join(D, "esh-coverage.json")
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=2)
    print(f"\nwrote {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    main()
