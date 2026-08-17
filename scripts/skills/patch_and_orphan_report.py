"""Two follow-ups for Khas: the mis-tagged production questions, and which
orphan strings sit on high-weight skills.

PART 1 — MIS-TAGGED QUESTIONS. Nine (topic, subtopic) pairs changed meaning
once I read the question body rather than the label. This lists every affected
question in data/questions/ with the skill_id it should carry, so Design can
patch them mechanically. One of them ("logarithms / negative exponents") has a
production TOPIC that is wrong, not merely imprecise — the item contains no
logarithm.

PART 2 — HIGH-VALUE ORPHANS. 623 bank questions carry a subtopic string the
resolver would not touch. Triaging all 172 strings is not the ask; finding the
ones that sit on heavy skills is, because those are questions we have already
paid for and are not using.

Every candidate below is a CANDIDATE. I am not writing them into the mapping
and the audit still counts them as orphans. The reason is the same one that
made the resolver conservative in the first place: these strings are generic
("тэгшитгэл" is just "equation"), so a plausible-looking guess is exactly the
kind of wrong tag that silently corrupts a student's record. What this report
gives is a ranked worklist — questions x weight of the skill they would most
likely land on — so the person confirming them starts where it pays.

Run: python3 scripts/skills/patch_and_orphan_report.py
"""

from __future__ import annotations

import collections
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GRAPH = json.load(open(os.path.join(ROOT, "data", "skills", "esh-skills.json")))
AUDIT = json.load(open(os.path.join(ROOT, "data", "skills", "esh-content-audit.json")))
SKILLS = {s["id"]: s for s in GRAPH["skills"]}

# --- Part 1 -----------------------------------------------------------------
# The nine pairs whose mapping changed after reading the question body, with
# the skill each should carry. `why` is what the question actually turned out
# to be. Verified individually against data/questions/.
# NOTE ON SCOPE: nine TAG PAIRS, but 31 QUESTION RECORDS. The two section-2
# pairs recur across all four 2022 variants (A/B/C/D). I verified the A variant
# by reading it, then spot-checked B, C and D: they are parallel items with the
# same structure and different constants ($y=x^2-2kx+k^2+k-2$ etc., cuboids with
# edge-sum 24 and 36), so the same skill applies to all twelve of each.
MISTAGGED = [
    (("logarithms", "negative exponents"), "integer-powers",
     "TOPIC IS WRONG, not just the subtopic. Test-2022A-Q1 is 'evaluate $3^{-2}$' "
     "— there is no logarithm in the item at all."),
    (("algebra", "factoring"), "factor-theorem",
     "Test-2022A-Q24 gives a ROOT and asks for the factorisation, so the method is "
     "the factor theorem, not trial factorisation."),
    (("algebra", "ratio"), "percent-and-proportion",
     "Test-2022A-Q10 is $a/2 = b/3$, find $(3a-b)/(a+2b)$ — proportional reasoning, "
     "not a ratio word problem."),
    (("functions", "парабол, экстремум"), "quadratic-function-vertex",
     "ONE skill, not two. For a parabola the extremum IS the vertex, and the item "
     "sits in functions, not calculus."),
    (("geometry", "тэгш өнцөгт параллелепипед"), "prism-volume-surface",
     "'rectangular parallelepiped' = cuboid. The 2022A item maximises its volume "
     "by completing the square, not by calculus."),
    (("linear_algebra", "translation vector"), "translation",
     "Tagged linear_algebra, but Test-2022A-Q7 translates a triangle — the skill is "
     "the geometric transformation."),
    (("calculus", "derivatives"), "derivative-trig",
     "Test-2022A-Q8 is $y=\\sin 2x$. Tag the NARROWEST true skill; chain-rule then "
     "arrives by inference."),
    (("probability", "divisibility probability"), "addition-rule",
     "Test-2022A-Q13 is P(divisible by 3 OR 5) — a union with an overlap."),
    (("probability", "variance (hypergeometric)"), "variance-of-random-variable",
     "'hypergeometric' is a red herring; at this level it is built from a "
     "distribution table by hand."),
]


def scan_questions():
    papers = [f"{y}{v}" for y in (2021, 2022, 2023, 2024, 2025) for v in "abcd"]
    legacy = [f"test{n}{v}" for n in range(1, 8) for v in "ab"]
    out = []
    for stem in papers + legacy:
        for suffix in ("", "-section2"):
            path = os.path.join(ROOT, "data", "questions", f"{stem}{suffix}.json")
            if not os.path.exists(path):
                continue
            data = json.load(open(path))
            items = data if isinstance(data, list) else data.get("problems",
                                                                 data.get("questions", []))
            for q in items:
                out.append({
                    "file": f"{stem}{suffix}.json",
                    "id": q.get("source") or f"{stem}-Q{q.get('questionNumber')}",
                    "topic": q.get("topic"),
                    "subtopic": (q.get("subtopic") or "").strip(),
                })
    return out


ALL_Q = scan_questions()

print("=" * 78)
print("PART 1 — MIS-TAGGED PRODUCTION QUESTIONS, with the skill_id to patch to")
print("=" * 78)
patch_rows = []
for (topic, sub), skill, why in MISTAGGED:
    hits = [q for q in ALL_Q
            if q["topic"] == topic and q["subtopic"].lower() == sub.lower()]
    print(f"\n  {topic} / {sub}")
    print(f"    -> skill_id: {skill}   ({SKILLS[skill]['exam_weight']:.2f}% of the exam)")
    print(f"    why: {why}")
    print(f"    {len(hits)} question(s) affected:")
    for h in hits:
        print(f"       {h['id']:<22} {h['file']}")
        patch_rows.append({**h, "skill_id": skill, "why": why})
print(f"\n  TOTAL: {len(patch_rows)} question records to patch across "
      f"{len(MISTAGGED)} tag pairs.")

# --- Part 2 -----------------------------------------------------------------
# Candidate skill for each high-frequency orphan string. `conf` is honest:
#   likely   the string names one thing and the skill is near-certain
#   probable one reading dominates, but the string is generic enough that the
#           question must be opened to be sure
#   split   the string covers several skills; these questions need re-tagging
#           individually, not a bulk mapping
CANDIDATES = {
    ("calculus", "талбай, интеграл"): ("area-under-curve", "probable", "'area, integral'"),
    ("algebra", "тэгшитгэл"): (None, "split", "'equation' — could be linear, quadratic, "
                                              "radical, rational or exponential"),
    ("algebra", "бутархай"): ("fraction-arithmetic", "probable", "'fraction'"),
    ("probability", "магадлал"): (None, "split", "'probability' — the whole topic"),
    ("calculus", "уламжлал, экстремум"): ("stationary-points-and-extrema", "likely",
                                          "'derivative, extremum'"),
    ("functions", "рационал функц"): ("rational-function-asymptotes", "probable",
                                      "'rational function'"),
    ("probability", "бөмбөг сонголтын магадлал"): ("counting-based-probability", "likely",
                                                   "'probability of selecting balls'"),
    ("algebra", "зэрэг"): ("integer-powers", "probable", "'power/exponent'"),
    ("functions", "квадрат функц"): ("quadratic-function-vertex", "likely",
                                     "'quadratic function'"),
    ("functions", "парабол"): ("quadratic-function-vertex", "likely", "'parabola'"),
    ("geometry", "тойрогт багтсан дөрвөн өнцөгт"): ("inscribed-circumscribed-circles",
                                                    "likely", "'cyclic quadrilateral'"),
    ("probability", "магадлал, тоолох"): ("counting-based-probability", "likely",
                                          "'probability, counting'"),
    ("algebra", "тэгшитгэлийн систем"): ("systems-two-linear", "probable",
                                         "'system of equations'"),
    ("geometry", "параллелограмм, төстэй гурвалжин"): ("triangle-similarity", "likely",
                                                       "'parallelogram, similar triangles'"),
    ("functions", "квадрат язгуурт функц"): ("domain-of-a-function", "probable",
                                             "'square-root function'"),
    ("geometry", "параллелепипед, пирамидын эзлэхүүн"): ("pyramid-volume-surface", "likely",
                                                         "'parallelepiped, pyramid volume'"),
    ("statistics", "гистограмм"): ("data-representation", "likely", "'histogram'"),
    ("calculus", "талбай, шүргэгч шулуун"): ("area-under-curve", "probable",
                                             "'area, tangent line'"),
    ("geometry", "гурвалжин"): (None, "split", "'triangle' — the whole family"),
    ("probability", "магадлал, хөзөр"): ("counting-based-probability", "likely",
                                         "'probability, playing cards'"),
    ("geometry", "огтлогдсон конус"): ("cone", "likely", "'truncated cone / frustum'"),
    ("algebra", "илэрхийлэл"): ("algebraic-expressions", "probable", "'expression'"),
    ("algebra", "логарифм"): (None, "split", "'logarithm' — definition, rules or equations"),
    ("algebra", "систем"): ("systems-two-linear", "probable", "'system'"),
    ("logarithms", "логарифм"): (None, "split", "'logarithm' — same ambiguity"),
    ("algebra", "шулуун"): ("line-equation", "probable", "'line'"),
    ("algebra", "зэргийн илэрхийлэл"): ("exponent-rules", "likely", "'power expression'"),
    ("geometry", "тэгш өнцөгт гурвалжин"): ("pythagoras", "probable", "'right triangle'"),
    ("combinatorics", "сэлгэмэл"): ("permutations", "likely", "'permutation'"),
    ("trigonometry", "тригонометр"): (None, "split", "'trigonometry' — the whole topic"),
}

orphan_counts = {(o["topic"], o["subtopic"]): o["questions"] for o in AUDIT["orphanStrings"]}

print("\n" + "=" * 78)
print("PART 2 — HIGH-VALUE ORPHANS: content we own and are not using")
print("=" * 78)
print("Ranked by questions x exam weight of the candidate skill. NOT auto-mapped.\n")

rows = []
for key, count in orphan_counts.items():
    cand = CANDIDATES.get(key)
    if not cand:
        continue
    skill, conf, gloss = cand
    weight = SKILLS[skill]["exam_weight"] if skill else 0.0
    rows.append((count * weight, count, key, skill, conf, gloss, weight))
rows.sort(key=lambda r: -r[0])

print(f"  {'value':>6}  {'qs':>4}  {'conf':<9} {'candidate skill':<32} {'wt':>5}  string")
print("  " + "-" * 92)
for value, count, key, skill, conf, gloss, weight in rows:
    if conf == "split":
        print(f"  {'--':>6}  {count:4d}  {conf:<9} {'NEEDS PER-ITEM TRIAGE':<32} {'--':>5}  "
              f"{key[1]}  ({gloss})")
    else:
        print(f"  {value:6.2f}  {count:4d}  {conf:<9} {skill:<32} {weight:5.2f}  "
              f"{key[1]}  ({gloss})")

confirmable = [r for r in rows if r[4] != "split"]
splits = [r for r in rows if r[4] == "split"]
print(f"\n  {sum(r[1] for r in confirmable)} questions across {len(confirmable)} strings "
      f"look bulk-confirmable (one skill each).")
print(f"  {sum(r[1] for r in splits)} questions across {len(splits)} strings are genuinely "
      f"ambiguous and need per-item triage.")
covered = sum(r[1] for r in rows)
total_orphans = AUDIT["counts"]["orphan"]
print(f"  Together these {len(rows)} strings account for {covered} of the "
      f"{total_orphans} orphans ({100*covered/total_orphans:.0f}%) — the remaining "
      f"{total_orphans - covered} sit in a long tail of 1-3 question strings.")

out = {
    "note": "Generated by scripts/skills/patch_and_orphan_report.py. Part 2 rows are "
            "CANDIDATES requiring confirmation; they are deliberately not written into "
            "the mapping.",
    "mistaggedQuestions": patch_rows,
    "orphanCandidates": [
        {"topic": k[0], "subtopic": k[1], "questions": c, "candidateSkill": s,
         "confidence": conf, "gloss": g, "candidateWeight": w, "value": round(v, 2)}
        for v, c, k, s, conf, g, w in rows
    ],
}
with open(os.path.join(ROOT, "data", "skills", "esh-patch-and-orphans.json"), "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")

# --- Part 3 -----------------------------------------------------------------
# SECOND-PASS candidates, added after the first report. These come from the
# long tail and are included ONLY where the string names one thing and that
# thing is one of the 73 empty skills — the question Khas actually asked is
# "which of the 73 are already covered", so the tail is worth scanning for
# exactly those and nothing else.
EXTRA_GAP_CANDIDATES = {
    ("functions", "тодорхойлогдох муж"): "domain-of-a-function",
    ("functions", "функцийн тодорхойлогдох муж"): "domain-of-a-function",
    ("algebra", "олон гишүүнт хуваах"): "polynomial-division",
    ("arithmetic", "анхны тоо"): "prime-factorisation",
    ("geometry", "пифагорын теорем"): "pythagoras",
    ("algebra", "absolute_value_equation"): "absolute-value-equations",
    ("algebra", "абсолют утгатай тэгшитгэл"): "absolute-value-equations",
    ("algebra", "absolute value inequality"): "absolute-value-inequalities",
    ("algebra", "quadratic_inequality"): "quadratic-inequalities",
    ("algebra", "quadratic_inequality_parameter"): "quadratic-inequalities",
    ("algebra", "polynomial_factoring"): "factoring-quadratic-trinomial",
    ("algebra", "matrix_operations"): "matrix-addition-scalar",
    ("algebra", "exponential_system"): "exponential-equations",
    ("algebra", "илтгэгч тэгшитгэл"): "exponential-equations",
    ("algebra", "экспоненциал тэгшитгэл"): "exponential-equations",
    ("functions", "урвуу функц"): "inverse-functions",
    ("functions", "экспоненциал функц"): "exponential-and-log-graphs",
    ("geometry", "гурвалжны талбай"): "triangle-area",
    ("geometry", "трапец"): "trapezoid-properties",
    ("geometry", "гурвалжны өнцөг"): "triangle-angle-sum",
    ("trigonometry", "радиан"): "unit-circle-and-radians",
    ("algebra", "квадратуудын ялгавар"): "special-products",
    ("algebra", "систем тэгшитгэл"): "systems-two-linear",
    ("functions", "график унших"): "data-representation",
}

gap_skills = set(AUDIT["skillsWithoutItems"])
counts = {(o["topic"], o["subtopic"]): o["questions"] for o in AUDIT["orphanStrings"]}

covered: dict[str, list[tuple[str, int, str]]] = {}
for key, cand in list(CANDIDATES.items()):
    skill = cand[0]
    if skill in gap_skills and key in counts:
        covered.setdefault(skill, []).append((key[1], counts[key], cand[1]))
for key, skill in EXTRA_GAP_CANDIDATES.items():
    if skill in gap_skills and key in counts:
        covered.setdefault(skill, []).append((key[1], counts[key], "second-pass"))

print("\n" + "=" * 78)
print("PART 3 — WHICH OF THE 73 EMPTY SKILLS THE ORPHANS ALREADY COVER")
print("=" * 78)
print("Asked for before writing new items. I wrote them first and cross-referenced")
print("after, so this is retrospective: it says where the 219 new items DUPLICATE")
print("questions the bank already owns.\n")
tot_q = sum(n for v in covered.values() for _, n, _ in v)
tot_w = sum(SKILLS[s]["exam_weight"] for s in covered)
for skill in sorted(covered, key=lambda s: -sum(n for _, n, _ in covered[s])):
    n = sum(x[1] for x in covered[skill])
    print(f"  {n:3d} q  {SKILLS[skill]['exam_weight']:5.2f}%  {skill}")
    for sub, q, conf in sorted(covered[skill], key=lambda x: -x[1]):
        print(f"          <- {q:2d}  {sub}  [{conf}]")
print(f"\n  {len(covered)} of the 73 already have bank questions hiding in orphans:")
print(f"    {tot_q} questions, {tot_w:.2f}% of the exam.")
print(f"  {73 - len(covered)} skills ({36.57 - tot_w:.2f}%) had nothing — the new items are")
print(f"    the only coverage they have.")
print(f"\n  So {3 * len(covered)} of the 219 new items ({100*3*len(covered)/219:.0f}%) duplicate")
print( "    existing coverage. They are not wasted — bank orphans carry no difficulty")
print( "    tier and no named distractors, which the adaptive test needs — but if the")
print( "    order had been reversed these skills would have been authored last, not")
print( "    first.")

untriaged = sum(o["questions"] for o in AUDIT["orphanStrings"]
                if (o["topic"], o["subtopic"]) not in CANDIDATES
                and (o["topic"], o["subtopic"]) not in EXTRA_GAP_CANDIDATES)
print(f"\n  BOUND ON THIS ANSWER: {untriaged} orphan questions remain untriaged, in a")
print( "  tail of 1-2 question strings. More of the 73 could be covered there, so")
print(f"  {len(covered)} is a floor, not a final count.")

out["gapSkillsCoveredByOrphans"] = {
    s: [{"subtopic": sub, "questions": q, "confidence": c} for sub, q, c in v]
    for s, v in covered.items()
}
out["untriagedOrphanQuestions"] = untriaged
with open(os.path.join(ROOT, "data", "skills", "esh-patch-and-orphans.json"), "w") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write("\n")
