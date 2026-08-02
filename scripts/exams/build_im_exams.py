#!/usr/bin/env python3
"""Course exams for Integrated Math 1 and 2 — three per course.

A course exam is a FIXED sitting that spans every unit of the course, unlike
the per-unit tests (one unit) and the bank runner (adaptive drill with
miss->similar retry). It answers a different question: not "can you do this
skill" but "where does this student stand across everything the course
taught".

Questions are SELECTED from the already-verified IM problem banks rather than
authored fresh. That is the right call three times over: every item already
carries a passing sympy check, the figure-bearing items already carry their
figures, and each item is already tagged with its unit and difficulty level —
which is exactly the metadata an exam blueprint needs. Re-authoring 204 items
would add risk and subtract nothing.

Blueprint, per exam:
  - EVERY unit of the course is represented, PER_UNIT questions each, so a
    result can name the weak unit rather than just a score.
  - Within a unit the picks ladder through levels 1 -> 2 -> 3 where the bank
    has them, so each unit's block has its own difficulty ramp.
  - The three exams of a course are DISJOINT: no variant appears in two of
    them, so a student can sit all three without meeting a repeat.
  - Selection is deterministic (no rng), so rebuilding is reproducible and a
    diff shows real changes only.

Run: python3 scripts/exams/build_im_exams.py   (then npm run verify:exams)
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BANK = os.path.join(ROOT, "data", "problembank")
OUT = os.path.join(ROOT, "data", "course-exams")
os.makedirs(OUT, exist_ok=True)

PER_UNIT = 4          # questions drawn from each unit, per exam
N_EXAMS = 3

COURSES = [
    {
        "slug": "integrated-1",
        "title": "Integrated Math 1",
        "minutes": 55,
        "intro": ("A full-course exam: every unit of Integrated Math 1 is represented, so the "
                  "result shows which units are solid and which need another pass."),
    },
    {
        "slug": "integrated-2",
        "title": "Integrated Math 2",
        "minutes": 50,
        "intro": ("A full-course exam: every unit of Integrated Math 2 is represented, so the "
                  "result shows which units are solid and which need another pass."),
    },
    {
        "slug": "integrated-3",
        "title": "Integrated Math 3",
        "minutes": 55,
        "intro": ("A full-course exam: every unit of Integrated Math 3 is represented, so the "
                  "result shows which units are solid and which need another pass."),
    },
]


def _by_unit(topic):
    """unit id -> forms, ordered by level so the picks ladder in difficulty."""
    out = {u["id"]: [] for u in topic["units"]}
    for f in topic["forms"]:
        if f["unit"] in out:
            out[f["unit"]].append(f)
    for uid in out:
        out[uid].sort(key=lambda f: (f["level"], f["id"]))
    return out


def _level_pattern(levels):
    """The difficulty shape of one unit's block of PER_UNIT questions.

    Only four units across IM1 and IM2 carry level-3 forms, so a level 3 has
    to be PLACED deliberately — left to a round-robin it lands in the third
    exam and the first exam ends up with no hard question at all, unable to
    discriminate at the top. Where a unit has no level 3, the block leans on
    level 2 instead of padding with easy items.
    """
    have = set(levels)
    if 3 in have:
        return [1, 2, 2, 3][:PER_UNIT]
    if 2 in have:
        return [1, 1, 2, 2][:PER_UNIT]
    return [1] * PER_UNIT


def _pick_for_unit(forms, exam_index, used):
    """Pick PER_UNIT variants for one unit: stratified by level, figures first.

    Two rules beyond "don't repeat":
      - spread across ARCHETYPES. Four variants of one form would test one
        skill four times and then misreport the whole unit.
      - prefer a figure-bearing variant whenever the unit has any. In the
        geometry-flavoured units most items carry a diagram, and reading the
        diagram IS the skill — an exam that quietly picked the text-only
        variants would test something easier than the unit teaches.
    """
    picked = []
    if not forms:
        return picked
    unit_has_figures = any(v.get("geoFigure") for f in forms for v in f["variants"])
    pattern = _level_pattern([f["level"] for f in forms])
    used_forms = set()

    for slot, want in enumerate(pattern):
        # Forms at the wanted level, else the closest level available.
        at_level = [f for f in forms if f["level"] == want]
        if not at_level:
            at_level = sorted(forms, key=lambda f: abs(f["level"] - want))
        # Prefer an archetype this unit has not used yet in THIS exam.
        fresh = [f for f in at_level if f["id"] not in used_forms] or at_level
        rot = (exam_index + slot) % len(fresh)
        order = fresh[rot:] + fresh[:rot]
        # In a unit that has diagrams, prefer a form that ACTUALLY carries them.
        # Preferring figures only among a chosen form's variants is too late —
        # if the form was text-only there is no figure left to prefer, which is
        # how the first cut ended up with 3 diagrams in a 36-question exam.
        if unit_has_figures:
            order.sort(key=lambda f: 0 if any(v.get("geoFigure") for v in f["variants"]) else 1)

        chosen = None
        for f in order:
            cands = [v for v in f["variants"] if v["id"] not in used]
            if not cands:
                continue
            if unit_has_figures:
                with_fig = [v for v in cands if v.get("geoFigure")]
                cands = with_fig or cands
            chosen = (f, cands[(exam_index * 7 + slot) % len(cands)])
            break
        if chosen is None:
            continue
        used.add(chosen[1]["id"])
        used_forms.add(chosen[0]["id"])
        picked.append(chosen)
    return picked


def build_course(course):
    path = os.path.join(BANK, "%s.json" % course["slug"])
    with open(path) as fh:
        topic = json.load(fh)
    units = topic["units"]
    by_unit = _by_unit(topic)

    used = set()          # shared across the three exams -> they stay disjoint
    written = []
    for k in range(N_EXAMS):
        questions = []
        for u in units:
            for f, v in _pick_for_unit(by_unit[u["id"]], k, used):
                q = {
                    "id": v["id"],
                    "unit": u["id"],
                    "unitTitle": u["title"],
                    "level": f["level"],
                    "skill": f["skill"],
                    "statement": v["statement"],
                    "options": v["options"],
                    "correctIndex": v["correctIndex"],
                    "explanation": v["explanation"],
                    "check": v["check"],
                }
                if v.get("geoFigure"):
                    q["geoFigure"] = v["geoFigure"]
                questions.append(q)
        exam = {
            "meta": {
                "examId": "%s-exam-%d" % (course["slug"], k + 1),
                "course": course["slug"],
                "courseTitle": course["title"],
                "label": "%s — Practice Exam %d" % (course["title"], k + 1),
                "intro": course["intro"],
                "minutes": course["minutes"],
                "totalQuestions": len(questions),
                "unitsCovered": len(units),
            },
            "questions": questions,
        }
        fn = os.path.join(OUT, "%s.json" % exam["meta"]["examId"])
        with open(fn, "w") as fh:
            json.dump(exam, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        figs = sum(1 for q in questions if q.get("geoFigure"))
        lv = {1: 0, 2: 0, 3: 0}
        for q in questions:
            lv[q["level"]] += 1
        written.append((exam["meta"]["examId"], len(questions), len(units), figs, lv))
    return written


def main():
    total = 0
    for course in COURSES:
        for eid, nq, nu, figs, lv in build_course(course):
            total += nq
            print("wrote %s.json — %d questions across %d units, %d with figures "
                  "(L1 %d / L2 %d / L3 %d)" % (eid, nq, nu, figs, lv[1], lv[2], lv[3]))
    print("TOTAL: %d exams, %d questions" % (len(COURSES) * N_EXAMS, total))


if __name__ == "__main__":
    main()
