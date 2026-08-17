"""Does the graph actually do the job it exists for?

The whole justification for the prerequisite graph is this claim: the
placement directly probes ~30 skills but reports across all ~185, because a
correct answer credits everything upstream. That claim is testable, and if it
is false the graph is decorative. This script tests it.

Three questions, in order of how badly a wrong answer would hurt:

1. DOES INFERENCE REACH? For a 30-item probe set, what fraction of the graph
   is credited by upstream closure? Anything unreachable can never be inferred
   — it has to be probed directly or reported as unknown, and pretending
   otherwise is how a student gets credit for something nobody ever saw.

2. IS THE CREDIT HONEST? Inference should be weighted by edge strength along
   the path. A chain of three 0.6 edges is 0.22 of a claim, not a claim. The
   report shows the decay so a weak inference is visibly weak.

3. WHERE IS THE GRAPH THIN? Skills with no dependents are leaves: nothing is
   ever inferred FROM them, so they are only worth probing if they carry exam
   weight. Skills with very many dependents are the load-bearing ones, where a
   wrong edge does the most damage — those are the edges to re-read first.

Run: python3 scripts/skills/inference_report.py
"""

from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
G = json.load(open(os.path.join(ROOT, "data", "skills", "esh-skills.json")))

SKILLS = {s["id"]: s for s in G["skills"]}
PREREQS = {}
for e in G["edges"]:
    PREREQS.setdefault(e["skill_id"], []).append((e["prereq_skill_id"], e["strength"]))
DEPENDENTS = {}
for e in G["edges"]:
    DEPENDENTS.setdefault(e["prereq_skill_id"], []).append(e["skill_id"])


def credit_from(skill_id, floor=0.25):
    """Skills credited by a correct answer on `skill_id`, with decayed weight.

    Credit multiplies along the path: solving S credits a prerequisite P at
    `strength`, and P's own prerequisite at strength*strength'. Below `floor`
    the claim is too weak to be worth making, so the walk stops — that cutoff
    is what stops a single hard item from silently certifying half the graph.
    """
    best = {skill_id: 1.0}
    stack = [(skill_id, 1.0)]
    while stack:
        node, w = stack.pop()
        for pid, strength in PREREQS.get(node, []):
            nw = w * strength
            if nw < floor:
                continue
            if nw > best.get(pid, 0.0):
                best[pid] = nw
                stack.append((pid, nw))
    del best[skill_id]
    return best


# --- 1. The brief's own worked example ------------------------------------
print("=" * 72)
print("THE WORKED EXAMPLE FROM THE BRIEF")
print("=" * 72)
print("A student correctly solves a logarithmic equation. What do we now know?\n")
for sid, w in sorted(credit_from("logarithmic-equations").items(), key=lambda kv: -kv[1]):
    bar = "#" * int(round(w * 20))
    print(f"  {w:.2f} {bar:<20} {sid:<34} {SKILLS[sid]['name_en']}")
print(f"\n  -> {len(credit_from('logarithmic-equations'))} skills credited from ONE item.")

# --- 2. Reach of a realistic 30-item probe set ------------------------------
# Chosen the way the paper diagnostic chooses: spread across strands, biased
# to skills that sit DEEP in the graph (deep skills credit more upstream) and
# to skills that carry exam weight.
PROBE_30 = [
    # algebra (10)
    "logarithmic-equations", "quadratic-inequalities", "vieta-formulas", "remainder-theorem",
    "rational-equations", "systems-nonlinear", "composite-functions", "domain-of-a-function",
    "geometric-series", "complex-conjugate-division",
    # geometry-trig (8)
    "inscribed-circumscribed-circles", "line-circle-intersection", "cone",
    "pyramid-volume-surface", "transformation-matrices", "trig-equations", "cosine-rule",
    "dot-product",
    # analysis (5)
    "area-between-curves", "stationary-points-and-extrema", "definite-integral-absolute",
    "differential-equations-separable", "normal-line",
    # probability & statistics (5)
    "variance-of-random-variable", "conditional-probability", "geometric-probability",
    "combined-standard-deviation", "grouped-frequency-mean",
    # combinatorics (2)
    "stars-and-bars", "permutations-with-restrictions",
]
missing = [p for p in PROBE_30 if p not in SKILLS]
assert not missing, f"probe set names skills that do not exist: {missing}"

reached = {}
for p in PROBE_30:
    reached[p] = max(reached.get(p, 0.0), 1.0)
    for sid, w in credit_from(p).items():
        reached[sid] = max(reached.get(sid, 0.0), w)

print("\n" + "=" * 72)
print(f"REACH OF A {len(PROBE_30)}-ITEM PROBE SET")
print("=" * 72)
total = len(SKILLS)
print(f"  directly probed      {len(PROBE_30):3d} / {total}  ({100*len(PROBE_30)/total:.0f}%)")
print(f"  reached by inference {len(reached):3d} / {total}  ({100*len(reached)/total:.0f}%)")
strong = sum(1 for w in reached.values() if w >= 0.6)
print(f"  ...at credit >= 0.6  {strong:3d} / {total}  ({100*strong/total:.0f}%)")

# How good could a 30-item set be? Greedy maximum-coverage: repeatedly take
# the item that credits the most not-yet-credited exam weight. This is the
# number that matters for the paper diagnostic and for Phase 1's item budget —
# a hand-picked set answers "is my taste good", this answers "is 30 enough".
def greedy_probe_set(k, pool=None):
    pool = pool or list(SKILLS)
    closure = {s: set(credit_from(s)) | {s} for s in pool}
    chosen, covered = [], set()
    for _ in range(k):
        best, best_gain = None, -1.0
        for s in pool:
            if s in chosen:
                continue
            gain = sum(SKILLS[x]["exam_weight"] for x in closure[s] - covered)
            if gain > best_gain:
                best, best_gain = s, gain
        if best is None or best_gain <= 0:
            break
        chosen.append(best)
        covered |= closure[best]
    return chosen, covered


best30, best_cov = greedy_probe_set(30)
print("\n" + "=" * 72)
print("HOW GOOD COULD 30 ITEMS BE?  (greedy maximum-coverage)")
print("=" * 72)
bw = sum(SKILLS[s]["exam_weight"] for s in best_cov)
print(f"  best 30 items reach  {len(best_cov):3d} / {total} skills ({100*len(best_cov)/total:.0f}%)"
      f"  carrying {bw:.1f}% of the exam")
print(f"  my hand-picked 30    {len(reached):3d} / {total} skills ({100*len(reached)/total:.0f}%)")
for k in (20, 40, 50, 60):
    _, cov = greedy_probe_set(k)
    w = sum(SKILLS[s]["exam_weight"] for s in cov)
    print(f"  {k:3d} items ->        {len(cov):3d} / {total} skills ({100*len(cov)/total:.0f}%)"
          f"  carrying {w:.1f}% of the exam")
print("\n  The greedy 30, in order of marginal value:")
for i, s in enumerate(best30, 1):
    print(f"    {i:2d}. {s:<38} {SKILLS[s]['strand']:<22} d{SKILLS[s]['typical_difficulty']}")

unreached = sorted(set(SKILLS) - set(reached))
print(f"\n  NEVER REACHED: {len(unreached)} skills. These cannot be inferred from this")
print("  probe set — the adaptive test must probe them directly or report them")
print("  as unknown. This list is the honest limit of a 30-item sitting:")
by_strand = {}
for sid in unreached:
    by_strand.setdefault(SKILLS[sid]["strand"], []).append(sid)
for strand in sorted(by_strand):
    w = sum(SKILLS[s]["exam_weight"] for s in by_strand[strand])
    print(f"    {strand} ({w:.1f}% of the exam):")
    for sid in by_strand[strand]:
        print(f"      - {sid:<38} {SKILLS[sid]['exam_weight']:.2f}%  d{SKILLS[sid]['typical_difficulty']}")
uw = sum(SKILLS[s]["exam_weight"] for s in unreached)
print(f"\n  Unreached skills carry {uw:.1f}% of the exam in total.")

# --- 3. Where the graph is load-bearing ------------------------------------
print("\n" + "=" * 72)
print("LOAD-BEARING SKILLS — re-read these edges first, a mistake here is worst")
print("=" * 72)


def downstream(sid):
    seen, stack = set(), [sid]
    while stack:
        n = stack.pop()
        for d in DEPENDENTS.get(n, []):
            if d not in seen:
                seen.add(d)
                stack.append(d)
    return seen


ranked = sorted(SKILLS, key=lambda s: -len(downstream(s)))
for sid in ranked[:12]:
    n = len(downstream(sid))
    print(f"  {n:3d} skills depend on  {sid:<34} {SKILLS[sid]['name_en']}")

leaves = [s for s in SKILLS if not DEPENDENTS.get(s)]
print(f"\n  {len(leaves)} leaf skills (nothing is ever inferred FROM them).")
print("  A leaf is only worth an item if it carries exam weight; the heaviest:")
for sid in sorted(leaves, key=lambda s: -SKILLS[s]["exam_weight"])[:8]:
    print(f"    {SKILLS[sid]['exam_weight']:.2f}%  {sid}")
