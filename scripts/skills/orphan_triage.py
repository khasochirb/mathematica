"""Triage the 623 orphan questions — per QUESTION, not per tag string.

WHY NOT PER STRING, WHICH IS WHAT WAS ASKED FOR. Two things showed up the
moment the question bodies were read rather than their labels:

1. The big strings are umbrellas. `algebra / тэгшитгэл` ("equation") covers
   21 questions, and the first three are a quadratic-from-a-product, a
   rational-exponent equation, and a different quadratic. One tag across all
   21 would be wrong for most of them, and wrong in a way nobody could see
   afterwards — a tag looks equally confident whether it was earned or
   guessed.

2. All 208 section-2 orphans are sub-parts sharing one `context`, and the
   subtopic string describes the SCENARIO, not the skill. In 2021A-2.1 the
   shared string is "cyclic quadrilateral"; part 1's own `instruction` says
   cosine theorem, and the same sentence then uses the sine theorem for the
   radius. The parts test different skills. A per-string tag cannot express
   that, so for section 2 the string is not evidence at all.

So this reads each question's own maths and proposes a skill from THAT, then
reports the string-level distribution as a by-product — which is what makes
the umbrellas visible.

HOW A PROPOSAL IS EARNED. A signature is a regex over the item's own text
(body/context + instruction + solution) paired with the skill it implies and
the legacy topics it is allowed to fire under. Every signature below is a
claim someone can check. A question resolves only when the signatures that
fire agree on ONE skill. If two disagree the question is reported AMBIGUOUS
with both named — it is not silently broken toward the more common one. If
none fire it is UNRESOLVED.

The point is the abstention. `content_audit.py` refused fuzzy matching
because "a 0.8-similar string is how тойрог and тойрог ба шүргэгч end up on
the same skill when they are two different lessons". Nothing here overrides
that: this proposes, it does not tag, and the output is explicitly a
worklist for a human — ideally one who reads Mongolian, which I do not.

Run: python3 scripts/skills/orphan_triage.py
"""

from __future__ import annotations

import collections
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, "data", "skills")

GRAPH = json.load(open(os.path.join(D, "esh-skills.json")))
AUDIT = json.load(open(os.path.join(D, "esh-content-audit.json")))
SKILLS = {s["id"]: s for s in GRAPH["skills"]}

# ---------------------------------------------------------------------------
# SIGNATURES. (name, pattern, skill_id, allowed legacy topics or None for any)
#
# Mongolian glosses are given for every term so a Mongolian reader can check
# the claim without reading the regex. These are the entries most worth
# re-reading, because they are the ones I cannot verify myself.
# ---------------------------------------------------------------------------
SIGNATURES: list[tuple[str, str, str, tuple[str, ...] | None]] = [
    # -- analysis ----------------------------------------------------------
    ("area between two named curves", r"хүрээлэгдэх.{0,40}талбай|талбай.{0,40}хүрээлэгдэх",
     "area-between-curves", ("calculus",)),
    ("tangent line", r"шүргэгч", "tangent-line", ("calculus",)),
    ("normal line", r"норм[аи]л шулуун", "normal-line", ("calculus",)),
    # 'calculus' ONLY, deliberately. Under topic=functions the same phrase
    # ("largest value") describes a parabola's vertex, which is
    # quadratic-function-vertex and not a derivative skill at all. Allowing
    # 'functions' here put 8 of the 13 'парабол' questions on the calculus
    # skill, which is the exact conflation this script exists to avoid.
    ("stationary points / extremum", r"экстремум|хамгийн их утга|хамгийн бага утга",
     "stationary-points-and-extrema", ("calculus",)),
    # The 2021 section-2 cubic parts say "буурах завсар" (decreasing interval)
    # on its own, never paired with "өсөх", so the paired pattern missed all
    # twelve of them.
    ("increasing/decreasing from f'",
     r"өсөх.{0,20}буурах|буурах.{0,20}өсөх|монотон|(өсөх|буурах)\s*завсар",
     "monotonicity-from-derivative", ("calculus",)),
    # "сэжигтэй цэг" — literally "suspicious point", the standard Mongolian
    # school term for a critical point of f.
    ("critical points of f", r"сэжигтэй цэг|критик цэг",
     "stationary-points-and-extrema", ("calculus",)),
    ("inflection / concavity", r"хотгор|гүдгэр|нугарал", "concavity-and-inflection",
     ("calculus",)),
    ("definite integral with bounds", r"\\int_", "definite-integral", ("calculus",)),
    ("volume of revolution", r"эргэлтийн бие|эргүүлэхэд үүсэх", "volume-of-revolution",
     ("calculus",)),

    # -- probability & statistics ------------------------------------------
    # "хөзөр" is a PLAYING card; the 2025 section-2 game uses "карт", numbered
    # cards, which is why twelve of them matched nothing.
    ("cards", r"хөзөр|карт", "classical-probability", ("probability",)),
    # With replacement the draws are independent; without, they are not. That
    # distinction IS the skill being tested in 2025A-2.2, and its three parts
    # split exactly along it.
    ("draws with replacement", r"буцаа\w*\s*хий(?!хгүй)", "independent-events",
     ("probability",)),
    ("draws without replacement", r"буцаа\w*\s*хийхгүй", "conditional-probability",
     ("probability",)),
    ("balls from a bag", r"бөмбөг|уутнаас", "counting-based-probability", ("probability",)),
    ("at least one / complement", r"дор хаяж|ядаж", "complementary-events", ("probability",)),
    ("conditional probability", r"нөхцөлт магадлал|бол.{0,30}магадлал.{0,10}ол",
     "conditional-probability", ("probability",)),
    ("expected value", r"математик дундаж|хүлээгдэх утга", "expected-value",
     ("probability", "statistics")),
    ("distribution law/function", r"тархалтын хууль|тархалтын функц",
     "discrete-random-variable", ("probability",)),
    ("histogram", r"гистограмм", "data-representation", ("statistics",)),
    ("grouped mean", r"бүлэглэсэн.{0,20}дундаж|давтамжийн хүснэгт|дундаж",
     "grouped-frequency-mean", ("statistics",)),
    ("standard deviation", r"стандарт хазайлт|дисперс", "variance-and-sd", ("statistics",)),

    # -- geometry & trigonometry -------------------------------------------
    ("cosine theorem", r"косинусын теорем", "cosine-rule", None),
    ("sine theorem", r"синусын теорем", "sine-rule", None),
    ("Pythagoras", r"пифагор", "pythagoras", None),
    ("cyclic quadrilateral", r"тойрогт багтсан.{0,20}дөрвөн өнцөгт",
     "inscribed-circumscribed-circles", ("geometry",)),
    ("inscribed circle", r"багтсан тойрог|багтаасан тойрог",
     "inscribed-circumscribed-circles", ("geometry",)),
    ("inscribed angle", r"багтсан өнцөг", "inscribed-angle", ("geometry",)),
    ("pyramid volume", r"пирамид", "pyramid-volume-surface", ("geometry",)),
    ("parallelepiped / prism", r"параллелепипед|призм", "prism-volume-surface",
     ("geometry",)),
    ("cone (incl. frustum)", r"конус", "cone", ("geometry",)),
    ("cylinder", r"цилиндр", "cylinder", ("geometry",)),
    ("sphere", r"бөмбөрцөг|сфер", "sphere", ("geometry",)),
    ("trapezoid", r"трапец", "trapezoid-properties", ("geometry",)),
    ("similar triangles", r"төстэй гурвалжин|төсөөт", "triangle-similarity", ("geometry",)),
    ("triangle area", r"гурвалжны талбай", "triangle-area", ("geometry",)),
    ("median of a triangle", r"медиан", "triangle-medians", ("geometry",)),
    ("altitude of a triangle", r"өндөрлөг|биссектрис", "triangle-altitude", ("geometry",)),
    ("line equation", r"шулууны тэгшитгэл", "line-equation", ("geometry", "algebra")),
    ("collinear points", r"коллинеар|нэг шулуун дээр", "vector-arithmetic",
     ("geometry",)),
    ("radians", r"радиан", "unit-circle-and-radians", ("trigonometry",)),
    ("trig simplification", r"хялбарчл", "trig-simplification", ("trigonometry",)),

    # -- algebra -----------------------------------------------------------
    # The word "тэгшитгэл" (equation) alongside a logarithm is what separates
    # solving one from evaluating one; Test-6A-Q17 says "тэгшитгэлийг бод"
    # outright and was landing on the weaker logarithm-definition.
    ("logarithm", r"логарифм.{0,60}тэгшитгэл|тэгшитгэл.{0,60}логарифм|\\log.{0,80}тэгшитгэл",
     "logarithmic-equations", ("algebra", "logarithms", "functions")),
    ("logarithmic inequality", r"логарифм.{0,30}тэнцэтгэл биш|тэнцэтгэл биш.{0,30}логарифм",
     "logarithmic-inequalities", ("algebra", "logarithms")),
    ("exponential equation", r"экспоненциал тэгшитгэл|илтгэгч тэгшитгэл",
     "exponential-equations", ("algebra", "logarithms")),
    ("absolute value", r"абсолют|үнэмлэхүй", "absolute-value-equations",
     ("algebra", "arithmetic")),
    ("prime numbers", r"анхны тоо", "prime-factorisation", ("arithmetic", "algebra")),
    # NOT bare "хувь": it is a substring of "хувьд" ("regarding"), which appears
    # in a quarter of all solutions. Requiring the % sign or an inflected form
    # that only means percentage drops 11 false positives, among them a question
    # about which point the line y=mx+b cannot pass through.
    ("percent", r"%|хувиар|хувийг|хувь нь|хувьтай",
     "percent-and-proportion", ("algebra", "arithmetic")),
    ("proportion", r"пропорц|харьцаа", "mixture-and-ratio-problems",
     ("algebra", "arithmetic")),
    ("speed / distance / work", r"хурд|зай.{0,20}хугацаа|ажил",
     "rate-and-work-problems", ("algebra",)),
    ("arithmetic progression", r"арифметик прогресс", "arithmetic-sequence",
     ("algebra", "sequences")),
    ("geometric progression", r"геометр прогресс", "geometric-sequence",
     ("algebra", "sequences")),
    ("polynomial division", r"хуваа.{0,15}олон гишүүнт|олон гишүүнт.{0,15}хуваа",
     "polynomial-division", ("algebra",)),
    ("linear system", r"тэгшитгэлийн систем|системийг бод",
     "systems-two-linear", ("algebra",)),
    # Fires only when a squared unknown is actually present, so it can never
    # be a strictly-broader twin of the linear signature above.
    ("non-linear system",
     r"(?=.*(тэгшитгэлийн систем|системийг бод))(?=.*\^\s*\{?\s*2)",
     "systems-nonlinear", ("algebra",)),
    ("quadratic inequality", r"квадрат тэнцэтгэл биш", "quadratic-inequalities",
     ("algebra",)),
    ("domain", r"тодорхойлогдох муж", "domain-of-a-function",
     ("functions", "algebra")),
    ("range", r"утгын муж", "range-of-a-function", ("functions", "algebra")),
    ("inverse function", r"урвуу функц", "inverse-functions", ("functions", "algebra")),
    ("composite function", r"нийлмэл функц", "composite-functions",
     ("functions", "algebra")),
    ("parabola vertex", r"параболын орой|оройн цэг", "quadratic-function-vertex",
     ("functions", "algebra")),
    ("asymptote", r"асимптот", "rational-function-asymptotes",
     ("functions", "algebra")),

    # -- NOTATION. The label is Mongolian; the maths is not. Where a question
    # writes the operator, that is better evidence than the word for it, and it
    # is evidence I can actually check. Most of the unresolved logarithm and
    # combinatorics questions were unresolved only because the body writes
    # \log and \binom and never spells the word out.
    ("writes a logarithm", r"\\log|\\ln\b|\\lg\b", "logarithm-definition",
     ("algebra", "logarithms", "functions")),
    # topic-restricted: the solution to a geometric-probability question
    # integrates to find an area, and Test-2A-Q36 ("pick x,y at random from
    # ]0,2]") was landing on definite-integral because of it.
    ("writes a definite integral", r"\\int_", "definite-integral", ("calculus",)),
    ("writes a binomial coefficient (counting)", r"\\binom|C_\{?\d|C\^",
     "combinations", ("combinatorics",)),
    # Same notation, different skill: under topic=probability the binomial
    # coefficient is the counting step INSIDE a probability, not the thing being
    # tested. Test-2A-Q26 ("14 boys, 7 girls, pick 2") is not a combinations
    # question, it is counting-based-probability.
    ("writes a binomial coefficient (probability)", r"\\binom|C_\{?\d|C\^",
     "counting-based-probability", ("probability",)),
    ("writes a factorial", r"\d\s*!|\\cdot\s*\d\s*!", "permutations",
     ("combinatorics",)),
    ("writes a matrix", r"\\begin\{pmatrix\}|\\begin\{bmatrix\}",
     "matrix-multiplication", ("algebra", "linear_algebra")),

    # -- english-language legacy tags (no gloss needed) --------------------
    ("matrix operations tag", r"^$", "matrix-multiplication", None),  # see TAG_MAP
]

# A signature that must NOT fire in a named context. `логарифм` under an
# inequality is a logarithmic INEQUALITY, a different skill; letting the
# equation signature fire there would either mistag it or, once the inequality
# signature is added, bury it in the ambiguous pile for no reason.
FORBID = {
    "logarithm": r"тэнцэтгэл биш|\\le|\\ge|[<>]",
    "writes a logarithm": r"тэнцэтгэл биш|\\le|\\ge|[<>]",
}

# Precedence, declared not inferred. When BOTH fire, the more specific skill is
# what the question is actually testing — an "area between two curves" question
# is of course evaluated with a definite integral, but the skill being probed is
# the area set-up. This is the only family where that is true; everywhere else
# two signatures disagreeing means two different sub-parts, and those stay
# ambiguous on purpose.
PRECEDENCE = [
    ("area-between-curves", "definite-integral"),
    ("volume-of-revolution", "definite-integral"),
    # A histogram question that asks for the average is testing the estimate,
    # not the chart. Test-2024B-2.3.2 asks for mean distance travelled.
    ("grouped-frequency-mean", "data-representation"),
    # A system containing a squared unknown is not a linear system, whatever
    # the word "system" alone suggests.
    ("systems-nonlinear", "systems-two-linear"),
    # Solving beats evaluating: \log proves logarithms are present, the word
    # "equation" proves one is being solved.
    ("logarithmic-equations", "logarithm-definition"),
    ("logarithmic-inequalities", "logarithm-definition"),
    ("logarithmic-inequalities", "logarithmic-equations"),
    # Naming the dependence structure is more specific than naming the setting.
    ("independent-events", "classical-probability"),
    ("conditional-probability", "classical-probability"),
    ("conditional-probability", "independent-events"),
]

# Legacy tags that are already English and unambiguous. These are exact-string
# claims, not pattern guesses, so they are applied directly.
TAG_MAP = {
    ("algebra", "matrix_operations"): "matrix-multiplication",
    ("algebra", "matrix_inverse"): "inverse-matrix-2x2",
    ("algebra", "absolute_value_simplification"): "absolute-value-equations",
    ("algebra", "absolute_value_equation"): "absolute-value-equations",
    ("algebra", "absolute value inequality"): "absolute-value-inequalities",
    ("algebra", "exponential_system"): "exponential-equations",
    ("algebra", "polynomial_roots"): "vieta-formulas",
    ("algebra", "polynomial_factoring"): "factoring-quadratic-trinomial",
    ("algebra", "arithmetic_progression"): "arithmetic-sequence",
    ("algebra", "quadratic_inequality"): "quadratic-inequalities",
    ("algebra", "quadratic_inequality_parameter"): "quadratic-inequalities",
    ("algebra", "algebraic_simplification"): "algebraic-expressions",
}

# re.S so a lookahead can reach across the newlines inside a solution.
COMPILED = [(n, re.compile(p, re.I | re.S), s, t) for n, p, s, t in SIGNATURES
            if p != r"^$"]
FORBIDDEN = {k: re.compile(v, re.I) for k, v in FORBID.items()}


def load_orphan_questions():
    ids = {o["id"]: o for o in AUDIT["orphans"]}
    found = {}
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
            if q.get("source") in ids:
                found[q["source"]] = q
    return ids, found


def text_of(q):
    """The question's OWN maths. For section 2 the shared context is included
    but the per-part instruction is what actually names the technique."""
    return " ".join(str(q.get(k, "")) for k in
                    ("body", "context", "instruction", "solution"))


def main():
    orphans, questions = load_orphan_questions()

    rows = []
    for qid, rec in orphans.items():
        q = questions.get(qid)
        topic = rec["topic"]
        sub = (rec["subtopic"] or "").strip().lower()

        direct = TAG_MAP.get((topic, sub))
        if direct:
            rows.append({"id": qid, "topic": topic, "subtopic": sub,
                         "section": 2 if (q or {}).get("section") == 2 else 1,
                         "status": "resolved", "skill_id": direct,
                         "basis": ["exact legacy tag (English, unambiguous)"]})
            continue

        if q is None:
            rows.append({"id": qid, "topic": topic, "subtopic": sub, "section": None,
                         "status": "unresolved", "skill_id": None,
                         "basis": ["question body not found in data/questions"]})
            continue

        txt = text_of(q)
        hits = []
        for name, rx, skill, topics in COMPILED:
            if topics is not None and topic not in topics:
                continue
            if not rx.search(txt):
                continue
            forbid = FORBIDDEN.get(name)
            if forbid is not None and forbid.search(txt):
                continue
            hits.append((name, skill))

        distinct = sorted({s for _, s in hits})
        for specific, general in PRECEDENCE:
            if specific in distinct and general in distinct:
                distinct.remove(general)
        if len(distinct) == 1:
            status, skill = "resolved", distinct[0]
        elif len(distinct) > 1:
            status, skill = "ambiguous", None
        else:
            status, skill = "unresolved", None
        rows.append({
            "id": qid, "topic": topic, "subtopic": sub,
            "section": 2 if q.get("section") == 2 else 1,
            "status": status, "skill_id": skill,
            "candidates": distinct if status == "ambiguous" else [],
            "basis": [n for n, _ in hits],
        })

    for r in rows:
        if r.get("skill_id") and r["skill_id"] not in SKILLS:
            raise SystemExit(f"{r['id']}: proposes unknown skill {r['skill_id']}")

    counts = collections.Counter(r["status"] for r in rows)
    s2 = collections.Counter(r["status"] for r in rows if r["section"] == 2)

    # String-level view: this is what shows the umbrellas.
    by_string = collections.defaultdict(collections.Counter)
    for r in rows:
        by_string[(r["topic"], r["subtopic"])][r["skill_id"] or f"({r['status']})"] += 1
    umbrellas = []
    for key, dist in by_string.items():
        real = [k for k in dist if not k.startswith("(")]
        if len(real) > 1:
            umbrellas.append({"topic": key[0], "subtopic": key[1],
                              "questions": sum(dist.values()),
                              "distinctSkills": len(real),
                              "distribution": dict(dist)})
    umbrellas.sort(key=lambda u: (-u["distinctSkills"], -u["questions"]))

    resolved = [r for r in rows if r["status"] == "resolved"]
    # Weight is summed over DISTINCT skills. Summing per question counts a
    # skill once for every question that lands on it and produced 133.8% of a
    # 100% exam, which is how this bug announced itself.
    touched = {r["skill_id"] for r in resolved}
    weight = sum(SKILLS[s]["exam_weight"] for s in touched)

    print("=" * 74)
    print("ORPHAN TRIAGE — per question, from the maths, not from the label")
    print("=" * 74)
    print(f"  orphan questions     {len(rows)}")
    print(f"    resolved           {counts['resolved']}")
    print(f"    ambiguous          {counts['ambiguous']}  (signatures disagree — needs a split or a human)")
    print(f"    unresolved         {counts['unresolved']}")
    print(f"  section-2 sub-parts  {sum(1 for r in rows if r['section'] == 2)}"
          f"  (resolved {s2['resolved']})")
    print(f"  distinct skills reached: {len(touched)}, "
          f"carrying {weight:.2f}% of the exam")

    print("\n" + "=" * 74)
    print(f"UMBRELLA TAGS — {len(umbrellas)} strings covering more than one skill")
    print("A single tag on any of these would be wrong for most of its questions.")
    print("=" * 74)
    for u in umbrellas[:20]:
        print(f"  {u['questions']:3d}q  {u['distinctSkills']} skills  "
              f"{u['topic']}/{u['subtopic']}")
        for k, n in sorted(u["distribution"].items(), key=lambda kv: -kv[1]):
            print(f"          {n:3d}  {k}")

    # What confirming these would actually buy, and what is left for a human.
    per_skill = collections.Counter(r["skill_id"] for r in resolved)
    unresolved_strings = collections.Counter(
        (r["topic"], r["subtopic"]) for r in rows if r["status"] == "unresolved")

    print("\n" + "=" * 74)
    print("WHAT CONFIRMING THE RESOLVED SET BUYS")
    print("Questions we already own, currently unroutable because skill_id is null.")
    print("=" * 74)
    for skill, n in per_skill.most_common(15):
        print(f"  {n:3d}q  {SKILLS[skill]['exam_weight']:5.2f}%  {skill}")
    if len(per_skill) > 15:
        print(f"  ... and {len(per_skill) - 15} more skills")

    print("\n" + "=" * 74)
    print("STILL NEEDS A HUMAN — biggest unresolved strings first")
    print("A Mongolian-reading teacher is the right reader for these; I am not.")
    print("=" * 74)
    for (t, sub), n in unresolved_strings.most_common(15):
        print(f"  {n:3d}q  {t}/{sub}")

    out = {
        "note": ("Generated by scripts/skills/orphan_triage.py. These are PROPOSALS "
                 "with their evidence, not tags. Nothing here is written into the "
                 "mapping or the database. 'ambiguous' means two signatures fired "
                 "for different skills and the question was NOT broken toward "
                 "either."),
        "method": ("Per question, from its own body/instruction/solution. The "
                   "subtopic string is not used as evidence except for the exact "
                   "English legacy tags in TAG_MAP, because the string describes "
                   "the scenario and, for section 2, is shared across parts that "
                   "test different skills."),
        "counts": {
            "orphanQuestions": len(rows),
            "resolved": counts["resolved"],
            "ambiguous": counts["ambiguous"],
            "unresolved": counts["unresolved"],
            "section2SubParts": sum(1 for r in rows if r["section"] == 2),
            "distinctSkillsReached": len(touched),
            "examWeightOfResolvedSkills": round(weight, 2),
        },
        "questionsPerProposedSkill": dict(per_skill.most_common()),
        "unresolvedStringsForAHuman": [
            {"topic": t, "subtopic": sub, "questions": n}
            for (t, sub), n in unresolved_strings.most_common()
        ],
        "umbrellaStrings": umbrellas,
        "proposals": rows,
    }
    path = os.path.join(D, "esh-orphan-triage.json")
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=2)
    print(f"\nwrote {os.path.relpath(path, ROOT)}")


if __name__ == "__main__":
    main()
