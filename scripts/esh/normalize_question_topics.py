#!/usr/bin/env python3
"""Normalize the `topic` field of every ЭЕШ question to a canonical key.

The 54 files under data/questions/ accumulated 57 different spellings of the
14 topics — "Алгебр", "Coordinate Geometry", "Matrices", "linear algebra",
bare None — and the runtime has been papering over it with TOPIC_ALIASES in
lib/esh-questions.ts. That kept the UI working but left the data itself
unsortable: the moment anything reads a file without going through the alias
map (a script, an export, a new feature), the mess leaks.

This script makes the DATA canonical. It reads the same alias table the
runtime uses (parsed out of lib/esh-questions.ts, so the two cannot drift),
applies the per-question overrides below for items whose stored topic was
None/"other" (classified by hand, one read each, 2026-08-12), and rewrites
`topic` in place. Everything else in each file is untouched.

After this run the alias map is a safety net for FUTURE imports, not a crutch
the current data stands on — scripts/verify-esh-question-topics.test.ts
asserts every stored topic is already canonical.

Run: python3 scripts/esh/normalize_question_topics.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
QDIR = os.path.join(ROOT, "data", "questions")

CANONICAL = {
    "algebra", "geometry", "trigonometry", "functions", "logarithms",
    "sequences", "probability", "combinatorics", "calculus", "statistics",
    "arithmetic", "set_theory", "linear_algebra", "complex_numbers",
}

# Questions whose stored topic carried no information (None or literal
# "other"). Each was classified by reading the question. The subtopic noted
# in the file agrees with each call.
OVERRIDES = {
    "Test-2A-Q5": "functions",        # max of a quadratic on an interval
    "Test-2A-Q6": "algebra",          # radical equation, sum of squared roots
    "Test-2A-Q7": "geometry",         # slope through two points
    "Test-2A-Q8": "algebra",          # 2x2 system word problem
    "Test-2A-Q9": "functions",        # where a rational function is undefined
    "Test-2A-Q10": "algebra",         # custom operations
    "Test-2A-Q11": "functions",       # domain of 1/sqrt(16-x^2)
    "Test-2A-Q12": "complex_numbers", # product of powers of i
    "Test-2A-Q13": "geometry",        # unit-sided hexagon
    "Test-2A-Q14": "arithmetic",      # three-digit perfect cubes
    "Test-2A-Q15": "algebra",         # age problem
    "Test-2A-Q16": "algebra",         # sum of coefficients of (2-x^2)^2015
    "Test-2A-Q17": "trigonometry",    # which quadrant is 10 degrees
    "Test-2A-Q18": "trigonometry",    # reduction-formula identity
    "Test-2A-Q19": "trigonometry",    # tan from sin in quadrant II
    "Test-2A-Q20": "geometry",        # rhombus from its diagonals
    "Test-2A-Q21": "logarithms",      # log_200 identity with coprime A,B,C
    "Test-2A-Q22": "logarithms",      # nested logarithms
    "Test-2A-Q23": "geometry",        # box with edges 1:3:4, volume
    "Test-2A-Q24": "logarithms",      # exponential equation 25^x + 2*5^x
    "Test-2A-Q25": "geometry",        # area of triangle between lines
    "Test-2A-Q26": "probability",     # one boy one girl from 14+7
    "Test-2A-Q27": "linear_algebra",  # M^3 for a 2x2 matrix
    "Test-2A-Q28": "functions",       # inverse of 3x-5
    "Test-2A-Q29": "algebra",         # partial fractions
    "Test-2A-Q30": "algebra",         # remainder theorem, find a
    "Test-2A-Q31": "calculus",        # increasing intervals from f' graph
    "Test-2A-Q32": "linear_algebra",  # parallel vector combinations
    "Test-2A-Q33": "set_theory",      # set equality
    "Test-2A-Q34": "set_theory",      # inclusion-exclusion counts
    "Test-2A-Q35": "probability",     # distribution function of X
    "Test-2A-Q36": "probability",     # geometric probability on (0,2]^2
    "Test-2B-Q33": "set_theory",      # truth about M = {1,{2,3},2,∅}
    "Test-2B-Q34": "set_theory",      # inclusion-exclusion counts
    "Test-3A-Q28": "set_theory",      # shaded region of a Venn diagram
    "Test-3B-Q28": "set_theory",      # shaded region of a Venn diagram
}


def load_aliases():
    """The TOPIC_ALIASES table, parsed from the TypeScript source of truth."""
    ts = open(os.path.join(ROOT, "lib", "esh-questions.ts"), encoding="utf-8").read()
    m = re.search(r"const TOPIC_ALIASES: Record<string, string> = \{(.*?)\n\};", ts, re.S)
    if not m:
        raise SystemExit("TOPIC_ALIASES not found in lib/esh-questions.ts")
    return dict(re.findall(r'"([^"]+)":\s*"([^"]+)"', m.group(1)))


def main():
    aliases = load_aliases()

    def canonical(raw):
        if not raw or not isinstance(raw, str):
            return None
        low = raw.strip().lower()
        if low in CANONICAL:
            return low
        return aliases.get(low)

    # Two passes: resolve EVERYTHING first, write only if nothing is
    # unresolved — a half-normalized dataset is worse than the current mess.
    plans = []  # (path, questions, n_changed)
    unresolved = []
    for name in sorted(os.listdir(QDIR)):
        if not name.endswith(".json"):
            continue
        path = os.path.join(QDIR, name)
        with open(path, encoding="utf-8") as fh:
            questions = json.load(fh)
        n = 0
        for q in questions:
            source = q.get("source")
            new = OVERRIDES.get(source) or canonical(q.get("topic"))
            if new is None:
                unresolved.append((name, source, q.get("topic")))
                continue
            if q.get("topic") != new:
                q["topic"] = new
                n += 1
        if n:
            plans.append((path, questions, n))

    if unresolved:
        for name, source, topic in unresolved:
            print(f"UNRESOLVED {name} {source}: {topic!r}", file=sys.stderr)
        raise SystemExit(f"{len(unresolved)} question(s) have no canonical topic "
                         f"— add an alias or an override; nothing was written")

    changed_questions = 0
    for path, questions, n in plans:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(questions, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        changed_questions += n
    print(f"normalized {changed_questions} question(s) across {len(plans)} file(s)")


if __name__ == "__main__":
    main()
