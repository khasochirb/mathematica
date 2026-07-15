"""Problem-bank generator for topic: sequences (Sequences & Series).

Generates ~36 machine-verified variants for each of 8 exam forms.
Run `python3 scripts/pb/sequences.py` to execute the self-check.
"""

from itertools import product
from sympy import sympify, Rational, simplify

SLUG = "sequences"
TITLE = "Sequences & Series"
TITLE_MN = "Дараалал"
BLURB = ("Arithmetic and geometric: nth terms, sums, hidden ratios, "
         "and the infinite series that converges.")

TARGET = 36  # aim per form


# ----------------------------------------------------------------------------
# formatting helpers
# ----------------------------------------------------------------------------

def num_fmt(v):
    """Format a sympy number as KaTeX wrapped in $...$."""
    v = sympify(v)
    if v.is_Integer:
        return f"${int(v)}$"
    if v.is_Rational:
        p, q = v.p, v.q
        if p < 0:
            return f"$-\\frac{{{-p}}}{{{q}}}$"
        return f"$\\frac{{{p}}}{{{q}}}$"
    return f"${v}$"


def q_disp(v):
    """Display a ratio inside a statement (no dollar wrapping)."""
    v = sympify(v)
    if v.is_Integer:
        return f"{int(v)}"
    p, q = v.p, v.q
    if p < 0:
        return f"-\\frac{{{-p}}}{{{q}}}"
    return f"\\frac{{{p}}}{{{q}}}"


def n_fmt(v):
    return f"$n = {int(v)}$"


def pick_distractors(correct, candidates, want=3):
    """Return `want` values numerically distinct from correct & each other.

    Returns None if not enough valid candidates.
    """
    correct = sympify(correct)
    chosen = []
    for c in candidates:
        c = sympify(c)
        if simplify(c - correct) == 0:
            continue
        if any(simplify(c - x) == 0 for x in chosen):
            continue
        chosen.append(c)
        if len(chosen) == want:
            return chosen
    return None


def make_variant(vid, statement, correct, distractors, explanation, checks,
                 fmt=num_fmt, ci=0):
    """Assemble a variant dict placing the correct option at index ci."""
    opts_vals = list(distractors)
    opts_vals.insert(ci, correct)
    options = [fmt(v) for v in opts_vals]
    if len(set(options)) != 4:
        return None
    return {
        "id": vid,
        "statement": statement,
        "options": options,
        "correctIndex": ci,
        "explanation": explanation,
        "check": checks,
    }


def spaced(combos, count):
    """Pick `count` widely-spaced items from combos for numeric variety."""
    n = len(combos)
    if n <= count:
        return list(combos)
    step = n / float(count)
    out = []
    seen = set()
    i = 0.0
    while len(out) < count and int(i) < n:
        idx = int(i)
        if idx not in seen:
            seen.add(idx)
            out.append(combos[idx])
        i += step
    # top up if rounding left us short
    for idx in range(n):
        if len(out) >= count:
            break
        if idx not in seen:
            seen.add(idx)
            out.append(combos[idx])
    return out


# ----------------------------------------------------------------------------
# form generators
# ----------------------------------------------------------------------------

def gen_arith_nth():
    a1s = [2, 3, 4, 5, 6, 7, 8, 10, 12, -3, -5, 15]
    ds = [2, 3, 4, 5, 6, -2, -3, -4]
    ns = [7, 8, 9, 10, 11, 12, 15, 20]
    combos = spaced(list(product(a1s, ds, ns)), TARGET + 8)
    out = []
    i = 0
    for a1, d, n in combos:
        if len(out) >= TARGET:
            break
        correct = a1 + (n - 1) * d
        cands = [a1 + n * d, a1 + (n - 2) * d, a1 * n, n * d]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-anth-v{i:02d}"
        stmt = (f"An arithmetic sequence has $a_1 = {a1}$ and difference "
                f"$d = {d}$. Find $a_{{{n}}}$.")
        expl = (f"$a_n = a_1 + (n-1)d$: $a_{{{n}}} = {a1} + {n-1} \\cdot ({d}) "
                f"= {correct}$. The step count is $n-1$, not $n$.")
        checks = [f"{a1} + ({n}-1)*({d}) == {correct}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_geo_nth():
    combos = []
    for q, ns in [(2, [5, 6, 7, 8, 9]), (3, [4, 5, 6]), (4, [3, 4, 5])]:
        for b1 in [1, 2, 3, 5, 6]:
            for n in ns:
                combos.append((b1, q, n))
    combos = spaced(combos, TARGET + 8)
    out = []
    i = 0
    for b1, q, n in combos:
        if len(out) >= TARGET:
            break
        correct = b1 * q ** (n - 1)
        cands = [b1 * q ** n, b1 * q ** (n - 2), b1 * q * (n - 1), b1 * n * q]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-gnth-v{i:02d}"
        stmt = (f"A geometric sequence has $b_1 = {b1}$ and ratio $q = {q}$. "
                f"Find $b_{{{n}}}$.")
        expl = (f"$b_n = b_1 q^{{n-1}}$: $b_{{{n}}} = {b1} \\cdot {q}^{{{n-1}}} "
                f"= {correct}$.")
        checks = [f"{b1}*{q}**({n}-1) == {correct}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_arith_find_d():
    a1s = [2, 3, 4, 5, 6, 8, 10, 12, -4, -2, 15, 7]
    ds = [2, 3, 4, 5, 6, 7, -2, -3]
    ks = [5, 6, 7, 8, 9, 10, 11, 13]
    combos = spaced(list(product(a1s, ds, ks)), TARGET + 8)
    out = []
    i = 0
    for a1, d, k in combos:
        if len(out) >= TARGET:
            break
        ak = a1 + (k - 1) * d
        correct = d
        cands = [d + 1, d - 1, d + 2, d - 2]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-diff-v{i:02d}"
        stmt = (f"An arithmetic sequence has $a_1 = {a1}$ and "
                f"$a_{{{k}}} = {ak}$. Find the difference $d$.")
        expl = (f"From $a_{{{k}}} = a_1 + {k-1}d$: ${ak} = {a1} + {k-1}d$ "
                f"$\\Rightarrow d = \\frac{{{ak - a1}}}{{{k-1}}} = {d}$.")
        checks = [f"Rational({ak} - ({a1}), {k} - 1) == {d}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_arith_sum():
    a1s = [2, 3, 4, 5, 6, 8, 10, -3, 7, 12]
    ds = [2, 3, 4, 5, 6, -2, -3]
    ns = [6, 8, 10, 12, 14, 15, 9, 11]
    combos = spaced(list(product(a1s, ds, ns)), TARGET + 12)
    out = []
    i = 0
    for a1, d, n in combos:
        if len(out) >= TARGET:
            break
        an = a1 + (n - 1) * d
        correct = Rational((a1 + an) * n, 2)
        if not correct.is_Integer:
            continue
        cands = [(a1 + an) * n, a1 * n, an * n,
                 Rational((a1 + (a1 + n * d)) * n, 2)]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        # require integer distractors for clean options
        if any(not sympify(x).is_Integer for x in dist):
            dist2 = pick_distractors(correct, [c for c in cands
                                               if sympify(c).is_Integer])
            if dist2 is None:
                continue
            dist = dist2
        i += 1
        vid = f"SEQ-asum-v{i:02d}"
        stmt = (f"Find the sum of the first ${n}$ terms of the arithmetic "
                f"sequence with $a_1 = {a1}$, $d = {d}$.")
        expl = (f"Last term $a_{{{n}}} = {a1} + {n-1} \\cdot ({d}) = {an}$. "
                f"Sum $S_n = \\frac{{(a_1 + a_n)n}}{{2}} = "
                f"\\frac{{({a1} + {an}) \\cdot {n}}}{{2}} = {int(correct)}$.")
        checks = [f"{a1} + ({n}-1)*({d}) == {an}",
                  f"Rational(({a1} + ({an}))*{n}, 2) == {int(correct)}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_geo_sum():
    combos = []
    for q, ns in [(2, [4, 5, 6, 7, 8]), (3, [3, 4, 5]), (4, [3, 4])]:
        for b1 in [1, 2, 3, 4, 5, 6]:
            for n in ns:
                combos.append((b1, q, n))
    combos = spaced(combos, TARGET + 12)
    out = []
    i = 0
    for b1, q, n in combos:
        if len(out) >= TARGET:
            break
        correct = Rational(b1 * (q ** n - 1), q - 1)
        s_next = Rational(b1 * (q ** (n + 1) - 1), q - 1)
        cands = [b1 * q ** n, b1 * q ** (n - 1), b1 * (q ** n - 1), s_next]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-gsum-v{i:02d}"
        stmt = (f"Find the sum of the first ${n}$ terms of the geometric "
                f"sequence with $b_1 = {b1}$, $q = {q}$.")
        expl = (f"$S_n = b_1\\frac{{q^n - 1}}{{q - 1}} = {b1} \\cdot "
                f"\\frac{{{q}^{{{n}}} - 1}}{{{q - 1}}} = {int(correct)}$.")
        checks = [f"{b1}*({q}**{n} - 1)/({q} - 1) == {int(correct)}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_which_term():
    a1s = [2, 3, 4, 5, 6, 7, 8, 10, -3, 12]
    ds = [2, 3, 4, 5, 6, 7, -2, -3]
    ns = [6, 7, 8, 9, 10, 11, 12, 14, 16]
    combos = spaced(list(product(a1s, ds, ns)), TARGET + 8)
    out = []
    i = 0
    for a1, d, n in combos:
        if len(out) >= TARGET:
            break
        target = a1 + (n - 1) * d
        correct = n
        cands = [n + 1, n - 1, n + 2, n - 2]
        cands = [c for c in cands if c >= 1]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-whic-v{i:02d}"
        stmt = (f"In the arithmetic sequence with $a_1 = {a1}$, $d = {d}$: "
                f"which term equals ${target}$?")
        expl = (f"Solve ${a1} + (n-1) \\cdot ({d}) = {target}$: "
                f"$n - 1 = \\frac{{{target - a1}}}{{{d}}} = {n-1}$, so $n = {n}$.")
        checks = [f"{a1} + ({n} - 1)*({d}) == {target}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks,
                         fmt=n_fmt, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_infinite_geo():
    # (p, r) ratios with |q|<1 ; required divisor of S so b1 is integer
    ratios = [
        (1, 2), (1, 3), (2, 3), (1, 4), (3, 4),
        (1, 5), (2, 5), (3, 5), (4, 5),
        (-1, 2), (-1, 3), (-2, 3), (-1, 4), (-3, 4),
    ]
    Svals = [6, 8, 9, 10, 12, 15, 16, 18, 20, 21, 24, 25, 30, 36, 40]
    combos = []
    for (p, r) in ratios:
        q = Rational(p, r)
        for S in Svals:
            b1 = S * (1 - q)
            if b1.is_Integer and b1 != 0:
                combos.append((p, r, S, int(b1)))
    combos = spaced(combos, TARGET + 12)
    out = []
    i = 0
    for p, r, S, b1 in combos:
        if len(out) >= TARGET:
            break
        q = Rational(p, r)
        correct = S
        cands = [b1 / (1 + q), b1 * (1 - q), S + 1, S - 1, S + 2, S - 2]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-inf-v{i:02d}"
        stmt = (f"Find the sum of the infinite geometric series with "
                f"$b_1 = {b1}$ and $q = {q_disp(q)}$.")
        expl = (f"$|q| < 1$, so it converges: "
                f"$S = \\dfrac{{b_1}}{{1 - q}} = \\dfrac{{{b1}}}{{1 - "
                f"({q_disp(q)})}} = {S}$.")
        checks = [f"{b1}/(1 - Rational({p},{r})) == {S}"]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


def gen_geo_two_terms():
    combos = []
    for q in [2, 3]:
        for b1 in [1, 2, 3, 4, 5, 6]:
            for i0 in [1, 2, 3]:
                for gap in [2, 3, 4]:
                    j0 = i0 + gap
                    bj = b1 * q ** (j0 - 1)
                    if bj <= 2500:
                        combos.append((b1, q, i0, j0))
    combos = spaced(combos, TARGET + 12)
    out = []
    i = 0
    for b1, q, i0, j0 in combos:
        if len(out) >= TARGET:
            break
        bi = b1 * q ** (i0 - 1)
        bj = b1 * q ** (j0 - 1)
        gap = j0 - i0
        correct = b1
        cands = [b1 * q, q, b1 + 2, b1 - 1, b1 * q ** 2]
        cands = [c for c in cands if c >= 1]
        dist = pick_distractors(correct, cands)
        if dist is None:
            continue
        i += 1
        vid = f"SEQ-two-v{i:02d}"
        stmt = (f"A geometric sequence has $b_{{{i0}}} = {bi}$ and "
                f"$b_{{{j0}}} = {bj}$. Find $b_1$.")
        expl = (f"Divide: $\\frac{{b_{{{j0}}}}}{{b_{{{i0}}}}} = q^{{{gap}}} = "
                f"\\frac{{{bj}}}{{{bi}}} = {bj // bi}$, so $q = {q}$. "
                f"Then $b_1 = \\frac{{b_{{{i0}}}}}{{q^{{{i0-1}}}}} = {b1}$.")
        checks = [
            f"Rational({bj}, {bi}) == {q}**{gap}",
            f"{b1}*{q}**({i0}-1) == {bi}",
            f"{b1}*{q}**({j0}-1) == {bj}",
        ]
        v = make_variant(vid, stmt, correct, dist, expl, checks, ci=i % 4)
        if v:
            out.append(v)
        else:
            i -= 1
    return out


# ----------------------------------------------------------------------------
# assemble
# ----------------------------------------------------------------------------

FORMS_META = [
    ("arith-nth", "Arithmetic: the nth term", 1,
     "a_n = a_1 + (n−1)d — n−1 steps from the start.",
     gen_arith_nth),
    ("geo-nth", "Geometric: the nth term", 1,
     "b_n = b_1·q^(n−1) — multiply n−1 times.",
     gen_geo_nth),
    ("arith-find-d", "Finding the common difference", 1,
     "d = (a_k − a_1)/(k − 1) — divide by the number of steps.",
     gen_arith_find_d),
    ("arith-sum", "Arithmetic series sum", 2,
     "S_n = (a_1 + a_n)·n/2 — Gauss's pairing.",
     gen_arith_sum),
    ("geo-sum", "Geometric series sum", 2,
     "S_n = b_1(qⁿ − 1)/(q − 1).",
     gen_geo_sum),
    ("which-term", "Which term is it?", 2,
     "Set a_n = value, solve for n — it must land on a whole number.",
     gen_which_term),
    ("infinite-geo", "Infinite geometric series", 3,
     "S = b_1/(1 − q), valid only when |q| < 1.",
     gen_infinite_geo),
    ("geo-two-terms", "Geometric sequence from two terms", 3,
     "Divide the given terms to isolate a power of q.",
     gen_geo_two_terms),
]


def build():
    forms = []
    for fid, title, level, skill, gen in FORMS_META:
        variants = gen()
        forms.append({
            "id": fid,
            "title": title,
            "level": level,
            "skill": skill,
            "variants": variants,
        })
    return {
        "slug": SLUG,
        "title": TITLE,
        "titleMn": TITLE_MN,
        "blurb": BLURB,
        "forms": forms,
    }


# ----------------------------------------------------------------------------
# self-check
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    data = build()
    expected_ids = [m[0] for m in FORMS_META]
    forms = data["forms"]
    assert len(forms) == 8, f"expected 8 forms, got {len(forms)}"
    assert [f["id"] for f in forms] == expected_ids, "form ids/order mismatch"

    all_ids = set()
    total = 0
    min_per_form = 10 ** 9
    for f in forms:
        vs = f["variants"]
        assert len(vs) >= 32, f"form {f['id']} has {len(vs)} variants (<32)"
        min_per_form = min(min_per_form, len(vs))
        total += len(vs)
        for v in vs:
            # id uniqueness
            assert v["id"] not in all_ids, f"dup id {v['id']}"
            all_ids.add(v["id"])
            # options
            assert len(v["options"]) == 4, f"{v['id']} not 4 options"
            assert len(set(v["options"])) == 4, f"{v['id']} options not distinct"
            assert 0 <= v["correctIndex"] <= 3, f"{v['id']} bad correctIndex"
            # checks
            for cs in v["check"]:
                res = sympify(cs)
                assert bool(res) is True, f"{v['id']} check failed: {cs} -> {res}"
            # correct numerically distinct from distractors
            ci = v["correctIndex"]
            correct_str = v["options"][ci]
            correct_val = None
            try:
                correct_val = sympify(correct_str.strip("$").replace(
                    "\\frac", "").replace("{", "(").replace("}", ")"))
            except Exception:
                correct_val = None
            for idx, opt in enumerate(v["options"]):
                if idx == ci:
                    continue
                assert opt != correct_str, f"{v['id']} distractor equals correct"
                if correct_val is not None and "n =" not in opt:
                    try:
                        dv = sympify(opt.strip("$").replace(
                            "\\frac", "").replace("{", "(").replace("}", ")"))
                        assert simplify(correct_val - dv) != 0, \
                            f"{v['id']} distractor numerically equals correct"
                    except AssertionError:
                        raise
                    except Exception:
                        pass

    print(f"SELFCHECK OK  forms=8  total={total}  min_per_form={min_per_form}")
