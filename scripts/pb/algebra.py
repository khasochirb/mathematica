# -*- coding: utf-8 -*-
"""Problem-bank generator for the ЭЕШ 'Algebra' topic.

Exposes build() returning ~36 machine-verified variants for each of 8 forms.
Every 'check' string sympifies to boolean True; every variant has exactly 4
distinct options with the correct answer numerically distinct from the
distractors. Run `python3 scripts/pb/algebra.py` for the self-check.
"""

from sympy import sympify, simplify

SLUG = "algebra"
TITLE = "Algebra"
TITLE_MN = "Алгебр"
BLURB = "Equations, inequalities, systems, exponents — the moves behind a third of any exam."


# ---------------------------------------------------------------------------
# formatting + option-assembly helpers
# ---------------------------------------------------------------------------

def L(v):
    """LaTeX for an integer/rational value (no surrounding $)."""
    v = sympify(v)
    if v.q == 1:
        return str(v.p)
    if v < 0:
        return "-\\frac{%d}{%d}" % (-v.p, v.q)
    return "\\frac{%d}{%d}" % (v.p, v.q)


def num_options(correct, cand_vals, pos):
    """Build 4 distinct numeric options; correct placed at index `pos`."""
    correct = sympify(correct)
    opts = [correct]
    for c in cand_vals:
        c = sympify(c)
        if all(simplify(c - o) != 0 for o in opts):
            opts.append(c)
        if len(opts) == 4:
            break
    k = 1
    while len(opts) < 4:
        for c in (correct + k, correct - k):
            if all(simplify(c - o) != 0 for o in opts):
                opts.append(c)
                if len(opts) == 4:
                    break
        k += 1
    dist = opts[1:4]
    final = list(dist)
    final.insert(pos, correct)
    return ["$" + L(v) + "$" for v in final], pos


def str_options(correct_str, distractor_strs, pos):
    """Build 4 distinct string options; correct placed at index `pos`."""
    dist = []
    for s in distractor_strs:
        if s != correct_str and s not in dist:
            dist.append(s)
        if len(dist) == 3:
            break
    final = list(dist)
    final.insert(pos, correct_str)
    return final, pos


def term(p):
    """Render 'x + p' with a proper sign."""
    p = int(p)
    if p >= 0:
        return "x + %d" % p
    return "x - %d" % (-p)


# ---------------------------------------------------------------------------
# per-form raw generators.  Each returns a list of dicts:
#   numeric form:  {statement, explanation, check, numeric=True, correct, cands}
#   string  form:  {statement, explanation, check, numeric=False, correct, dists}
# ---------------------------------------------------------------------------

def gen_linear():
    out, seen = [], set()
    bs = [3, 5, -4, 7, -2, 8, -6, 4, -3, 9, -5, 6]
    roots = [2, 3, 4, 5, -2, -3, 6, -4, 7, -5, 8, -6]
    for a in range(2, 10):
        for root in roots:
            b = bs[(a + abs(root)) % len(bs)]
            c = a * root + b
            key = (a, b, c)
            if key in seen:
                continue
            seen.add(key)
            if b >= 0:
                stmt = "Solve: $%dx + %d = %d$." % (a, b, c)
            else:
                stmt = "Solve: $%dx - %d = %d$." % (a, -b, c)
            expl = ("Undo the addition first: $%dx = %d$, then divide by $%d$: "
                    "$x = %d$. Check: $%d\\cdot %d %s %d = %d$." %
                    (a, c - b, a, root, a, root,
                     "+" if b >= 0 else "-", abs(b), c))
            check = [
                "solve(%d*x + (%d) - (%d), x) == [%d]" % (a, b, c, root),
                "%d*%d + (%d) == %d" % (a, root, b, c),
            ]
            cands = ["Rational(%d,%d)" % (c + b, a), c - b, -root, root + 1, root - 1]
            out.append(dict(statement=stmt, explanation=expl, check=check,
                            numeric=True, correct=root, cands=cands))
            if len(out) >= 44:
                return out
    return out


def gen_exponent():
    out, seen = [], set()
    for p in range(2, 10):
        for q in range(2, 9):
            r = ((p * q + p) % 6) + 1
            e = p + q - r
            if e < 1:
                continue
            if p * q == p + q:          # keep the multiply-mistake distractor distinct
                continue
            key = (p, q, r)
            if key in seen:
                continue
            seen.add(key)
            stmt = ("Simplify: $\\dfrac{x^{%d} \\cdot x^{%d}}{x^{%d}}$." % (p, q, r))
            expl = ("Multiplying powers adds exponents ($%d+%d=%d$); dividing "
                    "subtracts ($%d-%d=%d$). Never multiply the exponents." %
                    (p, q, p + q, p + q, r, e))
            check = ["%d + %d - %d == %d" % (p, q, r, e)]
            # distractor exponents encoding common slips
            cand_exps = [p + q + r, p + q, p * q - r, e + 2, e + 3, e - 2, e + 5]
            picked = []
            for ce in cand_exps:
                if ce != e and ce >= 0 and ce not in picked:
                    picked.append(ce)
                if len(picked) == 3:
                    break
            kk = 4
            while len(picked) < 3:
                if e + kk != e and (e + kk) not in picked:
                    picked.append(e + kk)
                kk += 1
            dists = ["$x^{%d}$" % ce for ce in picked]
            correct = "$x^{%d}$" % e
            out.append(dict(statement=stmt, explanation=expl, check=check,
                            numeric=False, correct=correct, dists=dists))
            if len(out) >= 44:
                return out
    return out


def gen_evaluate():
    out, seen = [], set()
    for c1 in range(2, 7):
        for av in range(2, 7):
            for j in range(3):
                c2 = 2 + (av + c1 + 2 * j) % 5
                bv = 2 + (av * c1 + j) % 6
                val = c1 * av * av - c2 * bv
                key = (c1, av, c2, bv)
                if key in seen:
                    continue
                seen.add(key)
                stmt = ("Evaluate $%da^2 - %db$ when $a = %d$ and $b = %d$." %
                        (c1, c2, av, bv))
                expl = ("Square first, multiply second: $%d\\cdot %d^2 = %d$, then "
                        "subtract $%d\\cdot %d = %d$: answer $%d$. The square "
                        "belongs to $a$ alone, not to $%da$." %
                        (c1, av, c1 * av * av, c2, bv, c2 * bv, val, c1))
                check = ["%d*%d**2 - %d*%d == %d" % (c1, av, c2, bv, val)]
                cands = [(c1 * av) ** 2 - c2 * bv,      # squared the coefficient too
                         c1 * av * av + c2 * bv,        # sign slip
                         c1 * (2 * av) - c2 * bv,       # used 2a instead of a^2
                         val + c2, val - c1]
                out.append(dict(statement=stmt, explanation=expl, check=check,
                                numeric=True, correct=val, cands=cands))
                if len(out) >= 44:
                    return out
    return out


def gen_inequality():
    out, seen = [], set()
    roots = [3, -3, 4, -4, 5, -5, 2, -2, 6, -6, 7, -7]
    idx = 0
    for a in range(2, 7):
        for root in roots:
            crhs = 2 + (abs(root) % 4)
            pconst = crhs + a * root
            key = (a, root, crhs, idx % 2)
            if key in seen:
                continue
            seen.add(key)
            if idx % 2 == 0:
                stmt = "Solve: $%d - %dx < %d$." % (pconst, a, crhs)
                expl = ("Subtract $%d$: $-%dx < %d$. Dividing by $-%d$ FLIPS the "
                        "sign: $x > %d$." % (pconst, a, crhs - pconst, a, root))
                check = [
                    "Rational(%d - %d, %d) == %d" % (pconst, crhs, a, root),
                    "%d - %d*(%d+1) < %d" % (pconst, a, root, crhs),
                    "%d - %d*(%d-1) > %d" % (pconst, a, root, crhs),
                ]
                correct = "$x > %d$" % root
                dists = ["$x < %d$" % root, "$x > %d$" % (-root), "$x < %d$" % (-root)]
            else:
                stmt = "Solve: $%d - %dx > %d$." % (pconst, a, crhs)
                expl = ("Subtract $%d$: $-%dx > %d$. Dividing by $-%d$ FLIPS the "
                        "sign: $x < %d$." % (pconst, a, crhs - pconst, a, root))
                check = [
                    "Rational(%d - %d, %d) == %d" % (pconst, crhs, a, root),
                    "%d - %d*(%d-1) > %d" % (pconst, a, root, crhs),
                    "%d - %d*(%d+1) < %d" % (pconst, a, root, crhs),
                ]
                correct = "$x < %d$" % root
                dists = ["$x > %d$" % root, "$x < %d$" % (-root), "$x > %d$" % (-root)]
            idx += 1
            out.append(dict(statement=stmt, explanation=expl, check=check,
                            numeric=False, correct=correct, dists=dists))
            if len(out) >= 44:
                return out
    return out


def gen_system():
    out, seen = [], set()
    coeffsets = [(1, 1, 2, -1), (1, 1, 1, -1), (2, 1, 1, -1), (1, 2, 1, -1),
                 (1, -1, 2, 1), (3, 1, 1, 1), (2, -1, 1, 1), (1, 1, 3, -2),
                 (2, 3, 1, -1), (1, 2, 3, 1)]
    pairs = [(3, 2), (4, 1), (2, 5), (5, 3), (1, 4), (6, 2), (3, 4), (2, 1)]
    for (a1, b1, a2, b2) in coeffsets:
        if a1 * b2 - a2 * b1 == 0:
            continue
        for (x0, y0) in pairs:
            rhs1 = a1 * x0 + b1 * y0
            rhs2 = a2 * x0 + b2 * y0
            s = x0 + y0
            key = (a1, b1, a2, b2, x0, y0)
            if key in seen:
                continue
            seen.add(key)

            def xco(co):
                return "%dx" % co if co != 1 else "x"

            def yco(co):
                if co >= 0:
                    return "+ y" if co == 1 else "+ %dy" % co
                return "- y" if co == -1 else "- %dy" % (-co)

            eq1 = "%s %s = %d" % (xco(a1), yco(b1), rhs1)
            eq2 = "%s %s = %d" % (xco(a2), yco(b2), rhs2)
            stmt = ("The system $\\begin{cases} %s \\\\ %s \\end{cases}$ has "
                    "solution $(x; y)$. Find $x + y$." % (eq1, eq2))
            expl = ("Eliminate one variable to get $x = %d$, $y = %d$ (check BOTH "
                    "equations!), so $x + y = %d$." % (x0, y0, s))
            check = [
                "%d*%d + (%d)*%d == %d" % (a1, x0, b1, y0, rhs1),
                "%d*%d + (%d)*%d == %d" % (a2, x0, b2, y0, rhs2),
                "%d + %d == %d" % (x0, y0, s),
                "%d*%d - %d*%d != 0" % (a1, b2, a2, b1),
            ]
            cands = [x0, y0, x0 - y0, s + 1, s - 1, 2 * x0]
            out.append(dict(statement=stmt, explanation=expl, check=check,
                            numeric=True, correct=s, cands=cands))
            if len(out) >= 44:
                return out
    return out


def gen_rational():
    out, seen = [], set()
    rvals = [0, 1, -1, 2, -2, 3, -3, 4, 5, -4, 6, -5]
    qvals = [2, 3, 4, -2, -3, 5, -4, 6]
    for k in range(2, 6):
        for r in rvals:
            for q in qvals:
                if r + q == 0:
                    continue
                p = k * (r + q) - r
                key = (k, p, q)
                if key in seen:
                    continue
                seen.add(key)
                stmt = ("Solve: $\\dfrac{%s}{%s} = %d$." % (term(p), term(q), k))
                expl = ("Multiply both sides by $%s$ (allowed since $x \\ne %d$): "
                        "$%s = %d(%s)$, which gives $x = %d$. The denominator is "
                        "nonzero there, so it is valid." %
                        (term(q), -q, term(p), k, term(q), r))
                check = [
                    "solve((%s)/(%s) - %d, x) == [%d]" % (term(p), term(q), k, r),
                    "%d + (%d) != 0" % (r, q),
                ]
                cands = [-r, -q, r + 1, r - 1, k, r + 2]
                out.append(dict(statement=stmt, explanation=expl, check=check,
                                numeric=True, correct=r, cands=cands))
                if len(out) >= 44:
                    return out
    return out


def gen_absolute():
    out, seen = [], set()
    avals = [3, 2, 4, 1, 5, -1, -2, 6, -3, 7, -4, 8]
    idx = 0
    for a in avals:
        for bnum in range(2, 10):
            if a == 0:
                continue
            lo, hi = a - bnum, a + bnum
            key = (a, bnum, idx % 2)
            if key in seen:
                continue
            seen.add(key)
            check = [
                "Abs(%d - %d) == %d" % (lo, a, bnum),
                "Abs(%d - %d) == %d" % (hi, a, bnum),
                "Abs(%d - %d) < %d" % (a, a, bnum),
            ]
            if idx % 2 == 0:
                stmt = "Solve: $|x - %d| \\le %d$." % (a, bnum) if a >= 0 \
                    else "Solve: $|x + %d| \\le %d$." % (-a, bnum)
                expl = ("$|x - %d| \\le %d$ is a distance statement: $%d - %d \\le x "
                        "\\le %d + %d$, i.e. $[%d;\\, %d]$. The 'or' split belongs "
                        "to $\\ge$, not $\\le$." % (a, bnum, a, bnum, a, bnum, lo, hi))
                correct = "$%d \\le x \\le %d$" % (lo, hi)
                dists = ["$x \\le %d$" % hi,
                         "$x \\le %d \\text{ or } x \\ge %d$" % (lo, hi),
                         "$%d \\le x \\le %d$" % (-hi, -lo)]
            else:
                stmt = "Solve: $|x - %d| \\ge %d$." % (a, bnum) if a >= 0 \
                    else "Solve: $|x + %d| \\ge %d$." % (-a, bnum)
                expl = ("$|x - %d| \\ge %d$ means the distance from $x$ to $%d$ is at "
                        "least $%d$: $x \\le %d$ or $x \\ge %d$. The union belongs "
                        "to $\\ge$, not a single bracket." %
                        (a, bnum, a, bnum, lo, hi))
                correct = "$x \\le %d \\text{ or } x \\ge %d$" % (lo, hi)
                dists = ["$%d \\le x \\le %d$" % (lo, hi),
                         "$x \\ge %d$" % hi,
                         "$x \\le %d \\text{ or } x \\ge %d$" % (-hi, -lo)]
            idx += 1
            out.append(dict(statement=stmt, explanation=expl, check=check,
                            numeric=False, correct=correct, dists=dists))
            if len(out) >= 44:
                return out
    return out


def gen_parameter():
    out, seen = [], set()
    for p in range(2, 7):
        for q in range(2, 7):
            m = p * q
            for c1 in [2, 3, 4, 5]:
                c2 = q * c1 + 1
                key = (p, q, c1)
                if key in seen:
                    continue
                seen.add(key)
                stmt = ("For which value of $m$ does the system "
                        "$\\begin{cases} x + %dy = %d \\\\ %dx + my = %d "
                        "\\end{cases}$ have NO solution?" % (p, c1, q, c2))
                expl = ("No solution = parallel lines: coefficients proportional but "
                        "constants not. $\\frac{%d}{1} = \\frac{m}{%d}$ gives "
                        "$m = %d$, and $\\frac{%d}{%d} \\ne \\frac{%d}{1}$ confirms "
                        "they never meet." % (q, p, m, c2, c1, q))
                check = [
                    "Rational(%d*%d,1) == %d" % (q, p, m),
                    "Rational(%d,%d) != Rational(%d,1)" % (c2, c1, q),
                ]
                cands = [-m, m + 1, p + q, q, p, m - 1]
                out.append(dict(statement=stmt, explanation=expl, check=check,
                                numeric=True, correct=m, cands=cands))
                if len(out) >= 44:
                    return out
    return out


# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------

FORMS_META = [
    ("linear-two-step", "Two-step linear equations", 1,
     "Undo addition, then undo multiplication — in that order.", "lin", gen_linear),
    ("exponent-laws", "Exponent laws", 1,
     "x^a·x^b = x^(a+b); division subtracts exponents.", "exp", gen_exponent),
    ("evaluate-expression", "Evaluating expressions", 1,
     "Powers before products; substitute carefully.", "eval", gen_evaluate),
    ("inequality-flip", "Inequalities with a sign flip", 2,
     "Dividing by a negative reverses the inequality.", "ineq", gen_inequality),
    ("system-2x2", "Systems of two equations", 2,
     "Eliminate one variable; always check the pair in BOTH equations.", "sys", gen_system),
    ("rational-equation", "Rational equations", 2,
     "Clear the denominator, solve, then verify the denominator isn't zero.", "rat", gen_rational),
    ("absolute-inequality", "Absolute-value inequalities", 3,
     "|x − a| ≤ b is a distance statement: a ± b bracket the answer.", "abs", gen_absolute),
    ("system-parameter", "Systems with a parameter", 3,
     "No solution ⟺ slopes match, intercepts don't (proportional coefficients, unproportional constants).",
     "par", gen_parameter),
]

TARGET = 36


def _finalize(form_id, title, level, skill, abbrev, raw_list):
    variants = []
    for i, item in enumerate(raw_list[:TARGET]):
        pos = i % 4
        if item["numeric"]:
            opts, ci = num_options(item["correct"], item["cands"], pos)
        else:
            opts, ci = str_options(item["correct"], item["dists"], pos)
        variants.append({
            "id": "ALG-%s-v%02d" % (abbrev, i + 1),
            "statement": item["statement"],
            "options": opts,
            "correctIndex": ci,
            "explanation": item["explanation"],
            "check": item["check"],
        })
    return {"id": form_id, "title": title, "level": level, "skill": skill,
            "variants": variants}


def build():
    forms = []
    for form_id, title, level, skill, abbrev, gen in FORMS_META:
        forms.append(_finalize(form_id, title, level, skill, abbrev, gen()))
    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN,
            "blurb": BLURB, "forms": forms}


# ---------------------------------------------------------------------------
# self-check
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    data = build()
    expected_ids = [m[0] for m in FORMS_META]
    assert len(data["forms"]) == 8, "expected 8 forms, got %d" % len(data["forms"])
    assert [f["id"] for f in data["forms"]] == expected_ids, "form ids/order mismatch"

    all_ids = []
    total = 0
    min_per_form = 10 ** 9
    for meta, form in zip(FORMS_META, data["forms"]):
        assert form["id"] == meta[0]
        assert form["title"] == meta[1]
        assert form["level"] == meta[2]
        assert form["skill"] == meta[3]
        vs = form["variants"]
        assert len(vs) >= 32, "%s has only %d variants" % (form["id"], len(vs))
        min_per_form = min(min_per_form, len(vs))
        total += len(vs)
        for v in vs:
            all_ids.append(v["id"])
            opts = v["options"]
            assert len(opts) == 4, "%s: need 4 options" % v["id"]
            assert len(set(opts)) == 4, "%s: options not distinct" % v["id"]
            assert 0 <= v["correctIndex"] <= 3, "%s: bad correctIndex" % v["id"]
            # every check sympifies to boolean True
            for c in v["check"]:
                res = sympify(c)
                assert bool(res) is True, "%s: check failed -> %s" % (v["id"], c)
            # correct option numerically distinct from each distractor
            correct = opts[v["correctIndex"]]
            for j, o in enumerate(opts):
                if j == v["correctIndex"]:
                    continue
                try:
                    cv = sympify(correct.strip("$"))
                    ov = sympify(o.strip("$"))
                    assert simplify(cv - ov) != 0, "%s: distractor equals correct" % v["id"]
                except (SyntaxError, TypeError, AttributeError, ValueError):
                    # non-numeric (interval/string) options: string distinctness suffices
                    assert correct != o, "%s: duplicate option string" % v["id"]

    assert len(all_ids) == len(set(all_ids)), "variant ids not globally unique"
    print("SELFCHECK OK  forms=8  total=%d  min_per_form=%d" % (total, min_per_form))
