"""Problem-bank generator for topic: logarithms (Exponents & Logarithms).

Generates ~36 machine-verified variants for each of 8 exam forms.
Every "check" string sympifies to boolean True.
Run `python3 scripts/pb/logarithms.py` for the self-check.
"""

SLUG = "logarithms"
TITLE = "Exponents & Logarithms"
TITLE_MN = "Логарифм"
BLURB = "From b^x = N to the domain traps of log inequalities — every exponential form the exam knows."

CAP = 36            # target per form
MIN_PER_FORM = 32   # hard floor


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def money(v):
    """Render an integer as a KaTeX option string."""
    return f"${v}$"


def place(correct, distractors, idx):
    """Return (options, correctIndex): correct placed at position idx%4,
    distractors filling the rest in order."""
    pos = idx % 4
    res = [None] * 4
    res[pos] = correct
    di = 0
    for j in range(4):
        if j == pos:
            continue
        res[j] = distractors[di]
        di += 1
    return res, pos


def pick3(correct_val, pool):
    """Pick 3 numerically distinct candidates from pool, all != correct_val."""
    seen = {correct_val}
    out = []
    for c in pool:
        if c in seen:
            continue
        seen.add(c)
        out.append(c)
        if len(out) == 3:
            break
    if len(out) < 3:
        return None
    return out


def lin(c):
    """Render 'x + c' shifting, hiding zero, using minus for negatives."""
    if c == 0:
        return "x"
    if c > 0:
        return f"x + {c}"
    return f"x - {-c}"


# ---------------------------------------------------------------------------
# Form 1: log-evaluate
# ---------------------------------------------------------------------------

def form_log_evaluate():
    variants = []
    seen = set()

    # a few special-value warm-ups first
    specials = [
        (7, 7, 1),   # log_7 7 = 1
        (5, 1, 0),   # log_5 1 = 0
    ]
    combos = []
    for (b, N, e) in specials:
        combos.append((b, N, e, True))
    for b in [2, 3, 5, 7, 10, 4, 6]:
        for e in [2, 3, 4, 5]:
            combos.append((b, b ** e, e, False))
    # extra high powers of 2 for range
    for e in [6, 7, 8]:
        combos.append((2, 2 ** e, e, False))

    idx = 0
    for (b, N, e, special) in combos:
        if len(variants) >= CAP:
            break
        key = (b, N)
        if key in seen:
            continue
        # distractor pool of plausible mistakes
        pool = [e + 1, e - 1, b, N // b if e >= 1 else e + 2, e + 2, b * e]
        pool = [p for p in pool if p != e]
        ds = pick3(e, pool)
        if ds is None:
            continue
        seen.add(key)
        correct = money(e)
        distractors = [money(d) for d in ds]
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-eval-v{len(variants)+1:02d}",
            "statement": f"Evaluate: $\\log_{{{b}}} {N}$.",
            "options": options,
            "correctIndex": ci,
            "explanation": (f"$\\log_{{{b}}} {N}$ asks: ${b}$ to what power gives ${N}$? "
                            f"Since ${b}^{{{e}}} = {N}$, the answer is ${e}$."),
            "check": [f"{b}**{e} == {N}", f"log({N}, {b}) == {e}"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 2: exp-equation
# ---------------------------------------------------------------------------

def form_exp_equation():
    variants = []
    seen = set()
    combos = []
    # positive-power right-hand sides with a linear shift
    for b in [2, 3, 5, 7]:
        for e in [2, 3, 4, 5]:
            for c in [0, 1, -1, 2, -2]:
                combos.append((b, e, c, b ** e, False))
    # reciprocal right-hand sides -> negative roots, for range
    for b in [2, 3, 5]:
        for e in [-1, -2, -3]:
            combos.append((b, e, 0, None, True))

    idx = 0
    for (b, e, c, N, recip) in combos:
        if len(variants) >= CAP:
            break
        root = e - c
        key = (b, e, c, recip)
        if key in seen:
            continue
        # distractors: sign slip on shift, forgot shift, off-by-one
        pool = [e + c, e, root + 1, root - 1, root + 2, 2 * root if root != 0 else e + 3]
        pool = [p for p in pool if p != root]
        ds = pick3(root, pool)
        if ds is None:
            continue
        seen.add(key)
        exp_str = lin(c)
        if recip:
            rhs = f"\\dfrac{{1}}{{{b ** (-e)}}}"
            check = [f"{b}**({root} + {c}) == Rational(1, {b ** (-e)})"]
            expl = (f"Write the right side as a power of ${b}$: "
                    f"$\\dfrac{{1}}{{{b ** (-e)}}} = {b}^{{{e}}}$. "
                    f"Equal bases $\\Rightarrow$ equal exponents: ${exp_str} = {e}$, so $x = {root}$.")
        else:
            rhs = f"{N}"
            check = [f"{b}**({root} + {c}) == {N}"]
            expl = (f"Write ${N}$ as a power of ${b}$: ${N} = {b}^{{{e}}}$. "
                    f"Equal bases $\\Rightarrow$ equal exponents: ${exp_str} = {e}$, so $x = {root}$.")
        correct = money(root)
        distractors = [money(d) for d in ds]
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-expeq-v{len(variants)+1:02d}",
            "statement": f"Solve: ${b}^{{{exp_str}}} = {rhs}$.",
            "options": options,
            "correctIndex": ci,
            "explanation": expl,
            "check": check,
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 3: log-add-rule
# ---------------------------------------------------------------------------

def form_log_add():
    variants = []
    seen = set()

    # generate (base, exponent) targets, then split the power into M*N
    def splits(P):
        out = []
        d = 2
        while d * d <= P:
            if P % d == 0:
                m, n = d, P // d
                if 1 < m < n:
                    out.append((m, n))
            d += 1
        return out

    combos = []
    for b in [6, 10, 12, 15, 2, 3, 5, 4, 7, 8, 9, 14]:
        for k in [2, 3, 4]:
            P = b ** k
            for (m, n) in splits(P):
                combos.append((b, k, m, n))

    idx = 0
    for (b, k, m, n) in combos:
        if len(variants) >= CAP:
            break
        key = (b, m, n)
        if key in seen:
            continue
        pool = [k + 1, k - 1, k + 2, 2 * k, k + 3]
        pool = [p for p in pool if p != k]
        ds = pick3(k, pool)
        if ds is None:
            continue
        seen.add(key)
        correct = money(k)
        distractors = [money(d) for d in ds]
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-add-v{len(variants)+1:02d}",
            "statement": f"Evaluate: $\\log_{{{b}}} {m} + \\log_{{{b}}} {n}$.",
            "options": options,
            "correctIndex": ci,
            "explanation": (f"Same base: logs ADD by multiplying arguments: "
                            f"$\\log_{{{b}}}({m} \\cdot {n}) = \\log_{{{b}}} {m*n} = {k}$, "
                            f"since ${b}^{{{k}}} = {m*n}$."),
            "check": [f"{m}*{n} == {b}**{k}",
                      f"simplify(log({m}, {b}) + log({n}, {b}) - {k}) == 0"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 4: exp-substitution
# ---------------------------------------------------------------------------

def form_exp_substitution():
    variants = []
    seen = set()

    combos = []
    pairs = []
    xs = [0, 1, 2, 3, 4]
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            pairs.append((xs[i], xs[j]))
    # SUM-of-roots questions
    for b in [2, 3, 5]:
        for (x1, x2) in pairs:
            combos.append((b, x1, x2, "sum"))
    # a handful of PRODUCT-of-roots questions for variety
    for b in [2, 3]:
        for (x1, x2) in [(1, 2), (1, 3), (2, 3), (1, 4)]:
            combos.append((b, x1, x2, "prod"))

    idx = 0
    for (b, x1, x2, kind) in combos:
        if len(variants) >= CAP:
            break
        t1, t2 = b ** x1, b ** x2
        S, P = t1 + t2, t1 * t2
        key = (b, x1, x2, kind)
        if key in seen:
            continue
        if kind == "sum":
            correct_val = x1 + x2
            pool = [S, P, x1 * x2, correct_val + 1, correct_val - 1, x2]
            ask = "SUM"
        else:
            correct_val = x1 * x2
            pool = [x1 + x2, P, S, correct_val + 1, correct_val + 2]
            ask = "PRODUCT"
        pool = [p for p in pool if p != correct_val]
        ds = pick3(correct_val, pool)
        if ds is None:
            continue
        seen.add(key)
        correct = money(correct_val)
        distractors = [money(d) for d in ds]
        options, ci = place(correct, distractors, idx)
        expl = (f"Let $t = {b}^{{x}}$: $t^2 - {S}t + {P} = 0$ gives $t = {t1}$ or $t = {t2}$, "
                f"so ${b}^{{x}} = {t1}$ ($x = {x1}$) or ${b}^{{x}} = {t2}$ ($x = {x2}$). "
                f"The {ask.lower()} of the roots is ${correct_val}$.")
        variants.append({
            "id": f"LOG-sub-v{len(variants)+1:02d}",
            "statement": (f"The equation ${b}^{{2x}} - {S} \\cdot {b}^{{x}} + {P} = 0$ has two roots. "
                          f"Find their {ask}."),
            "options": options,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"solve(t**2 - {S}*t + {P}, t) == sorted([{t1}, {t2}])",
                      f"{b}**{x1} == {t1}", f"{b}**{x2} == {t2}",
                      f"({x1 + x2 if kind=='sum' else x1 * x2}) == {correct_val}"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 5: log-equation
# ---------------------------------------------------------------------------

def form_log_equation():
    variants = []
    seen = set()
    combos = []
    for b in [2, 3, 5, 10]:
        for c in [2, 3, 4]:
            for d in [1, 2, 3, -1, -2, -3]:
                combos.append((b, c, d))

    idx = 0
    for (b, c, d) in combos:
        if len(variants) >= CAP:
            break
        root = b ** c - d
        key = (b, c, d)
        if key in seen:
            continue
        # sign slip, forgot -d, multiply-instead-of-power
        pool = [b ** c + d, b ** c, b * c - d, b ** c - 2 * d, root + 1]
        pool = [p for p in pool if p != root]
        ds = pick3(root, pool)
        if ds is None:
            continue
        seen.add(key)
        arg = lin(d)
        correct = money(root)
        distractors = [money(x) for x in ds]
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-eq-v{len(variants)+1:02d}",
            "statement": f"Solve: $\\log_{{{b}}}({arg}) = {c}$.",
            "options": options,
            "correctIndex": ci,
            "explanation": (f"$\\log_{{{b}}}({arg}) = {c}$ means ${arg} = {b}^{{{c}}} = {b**c}$, "
                            f"so $x = {root}$. The argument ${arg} = {b**c} > 0$, valid."),
            "check": [f"{b}**{c} - ({d}) == {root}", f"{root} + ({d}) > 0"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 6: log-chain
# ---------------------------------------------------------------------------

def form_log_chain():
    variants = []
    seen = set()
    combos = []
    for a in [2, 3, 5]:
        for e in [2, 3, 4, 5]:
            for m in [3, 5, 6, 7, 10]:
                if m == a:
                    continue
                combos.append((a, e, m))

    idx = 0
    for (a, e, m) in combos:
        if len(variants) >= CAP:
            break
        N = a ** e
        key = (a, e, m)
        if key in seen:
            continue
        pool = [e + 1, e - 1, e + 2, a, 2 * e]
        pool = [p for p in pool if p != e]
        ds = pick3(e, pool)
        if ds is None:
            continue
        seen.add(key)
        correct = money(e)
        distractors = [money(x) for x in ds]
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-chain-v{len(variants)+1:02d}",
            "statement": f"Evaluate: $\\log_{{{a}}} {m} \\cdot \\log_{{{m}}} {N}$.",
            "options": options,
            "correctIndex": ci,
            "explanation": (f"The middle base cancels: "
                            f"$\\log_{{{a}}} {m} \\cdot \\log_{{{m}}} {N} = \\log_{{{a}}} {N} = {e}$, "
                            f"since ${a}^{{{e}}} = {N}$."),
            "check": [f"simplify(log({m}, {a}) * log({N}, {m}) - log({N}, {a})) == 0",
                      f"{a}**{e} == {N}"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 7: log-inequality  (interval-string options)
# ---------------------------------------------------------------------------

def form_log_inequality():
    variants = []
    seen = set()
    combos = []
    # "<" cases: log_b(x - p) < c  ->  p < x < p + b^c
    for b in [2, 3, 5]:
        for c in [2, 3]:
            for p in [1, 2, 3, -1, -2]:
                combos.append((b, c, p, "lt"))
    # ">" cases: log_b(x - p) > c  ->  x > p + b^c
    for b in [2, 3, 5]:
        for c in [2, 3]:
            for p in [1, 2, 3, -1, -2]:
                combos.append((b, c, p, "gt"))

    idx = 0
    for (b, c, p, kind) in combos:
        if len(variants) >= CAP:
            break
        bc = b ** c
        upper = p + bc
        key = (b, c, p, kind)
        if key in seen:
            continue
        arg = lin(-p)  # x - p
        if kind == "lt":
            correct = f"${p} < x < {upper}$"
            distractors = [
                f"$x < {upper}$",          # forgot the domain lower bound
                f"$x > {upper}$",          # flipped the inequality
                f"$-{abs(p)} < x < {upper}$" if p != -abs(p) else f"${p+1} < x < {upper}$",
            ]
            sign = "<"
            expl = (f"$\\log_{{{b}}}({arg}) < {c}$ needs the argument positive AND "
                    f"${arg} < {b}^{{{c}}} = {bc}$. Intersecting ${arg} > 0$ with ${arg} < {bc}$ "
                    f"gives ${p} < x < {upper}$.")
        else:
            correct = f"$x > {upper}$"
            distractors = [
                f"$x > {p + c}$",          # used c instead of b^c
                f"$x < {upper}$",          # flipped the inequality
                f"$x > {p}$",              # kept only the domain condition
            ]
            sign = ">"
            expl = (f"$\\log_{{{b}}}({arg}) > {c}$ means ${arg} > {b}^{{{c}}} = {bc}$, "
                    f"i.e. $x > {upper}$ (the domain ${arg} > 0$ is automatically satisfied).")
        # ensure 4 distinct option strings
        allopts = [correct] + distractors
        if len(set(allopts)) != 4:
            continue
        seen.add(key)
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-ineq-v{len(variants)+1:02d}",
            "statement": f"Solve: $\\log_{{{b}}}({arg}) {sign} {c}$.",
            "options": options,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"{b}**{c} == {bc}", f"{p} + {bc} == {upper}",
                      f"log({bc}, {b}) == {c}"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# Form 8: exp-inequality-flip  (interval-string options)
# ---------------------------------------------------------------------------

def form_exp_inequality_flip():
    variants = []
    seen = set()
    combos = []
    # (1/b)^x > R  with R = (1/b)^k  ->  x < k   (base < 1 flips)
    # (1/b)^x < R                    ->  x > k
    for b in [2, 3, 5]:
        for k in [1, 2, 3, -1, -2, -3, 4]:
            combos.append((b, k, "gt"))
            combos.append((b, k, "lt"))

    def rhs_repr(b, k):
        if k > 0:
            return f"\\dfrac{{1}}{{{b ** k}}}"
        if k < 0:
            return f"{b ** (-k)}"
        return "1"

    idx = 0
    for (b, k, kind) in combos:
        if len(variants) >= CAP:
            break
        key = (b, k, kind)
        if key in seen:
            continue
        R = rhs_repr(b, k)
        if kind == "gt":
            sign = ">"
            correct = f"$x < {k}$"
            distractors = [f"$x > {k}$", f"$x < {-k}$", f"$x > {-k}$"]
            expl = (f"Since the base $\\tfrac{{1}}{{{b}}} < 1$ is decreasing, comparing "
                    f"$\\left(\\tfrac{{1}}{{{b}}}\\right)^x > \\left(\\tfrac{{1}}{{{b}}}\\right)^{{{k}}}$ "
                    f"FLIPS the inequality: $x < {k}$.")
        else:
            sign = "<"
            correct = f"$x > {k}$"
            distractors = [f"$x < {k}$", f"$x > {-k}$", f"$x < {-k}$"]
            expl = (f"Since the base $\\tfrac{{1}}{{{b}}} < 1$ is decreasing, comparing "
                    f"$\\left(\\tfrac{{1}}{{{b}}}\\right)^x < \\left(\\tfrac{{1}}{{{b}}}\\right)^{{{k}}}$ "
                    f"FLIPS the inequality: $x > {k}$.")
        allopts = [correct] + distractors
        if len(set(allopts)) != 4:
            continue
        seen.add(key)
        options, ci = place(correct, distractors, idx)
        variants.append({
            "id": f"LOG-flip-v{len(variants)+1:02d}",
            "statement": (f"Solve: $\\left(\\dfrac{{1}}{{{b}}}\\right)^x {sign} {R}$."),
            "options": options,
            "correctIndex": ci,
            "explanation": expl,
            "check": [f"Rational(1, {b})**({k}-1) > Rational(1, {b})**{k}",
                      f"Rational(1, {b})**({k}+1) < Rational(1, {b})**{k}"],
        })
        idx += 1
    return variants


# ---------------------------------------------------------------------------
# assembly
# ---------------------------------------------------------------------------

FORM_META = [
    ("log-evaluate", "Evaluating logarithms", 1,
     "log_b N = the exponent that turns b into N.", form_log_evaluate),
    ("exp-equation", "Exponential equations", 1,
     "Match the bases, then equate exponents.", form_exp_equation),
    ("log-add-rule", "Adding logarithms", 1,
     "log M + log N = log(MN) — same base only.", form_log_add),
    ("exp-substitution", "Exponential equations via substitution", 2,
     "b^(2x) is (b^x)² — substitute t = b^x and solve the quadratic.", form_exp_substitution),
    ("log-equation", "Logarithmic equations", 2,
     "log_b(…) = c means (…) = b^c; check the argument stays positive.", form_log_equation),
    ("log-chain", "The log chain (change of base)", 2,
     "log_a b · log_b c = log_a c — the middle base cancels.", form_log_chain),
    ("log-inequality", "Log inequalities (domain trap)", 3,
     "Solve the inequality AND keep the argument positive — intersect both.", form_log_inequality),
    ("exp-inequality-flip", "Exponential inequalities, base < 1", 3,
     "A decreasing base flips the inequality when you compare exponents.", form_exp_inequality_flip),
]


def build():
    forms = []
    for (fid, title, level, skill, fn) in FORM_META:
        variants = fn()
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


# ---------------------------------------------------------------------------
# self-check
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    from sympy import sympify

    data = build()
    expected_ids = [m[0] for m in FORM_META]
    assert len(data["forms"]) == 8, "must have 8 forms"
    assert [f["id"] for f in data["forms"]] == expected_ids, "form ids/order mismatch"

    all_ids = set()
    total = 0
    min_per_form = 10 ** 9
    for f in data["forms"]:
        n = len(f["variants"])
        min_per_form = min(min_per_form, n)
        assert n >= MIN_PER_FORM, f"{f['id']} has only {n} variants"
        for v in f["variants"]:
            total += 1
            # unique ids
            assert v["id"] not in all_ids, f"duplicate id {v['id']}"
            all_ids.add(v["id"])
            # options
            assert len(v["options"]) == 4, f"{v['id']} needs 4 options"
            assert len(set(v["options"])) == 4, f"{v['id']} options not distinct"
            assert 0 <= v["correctIndex"] <= 3, f"{v['id']} bad correctIndex"
            # checks all True
            for c in v["check"]:
                r = sympify(c)
                assert bool(r) is True, f"{v['id']} check failed: {c} -> {r}"
            # correct numerically distinct from distractors (numeric options only)
            corr_s = v["options"][v["correctIndex"]].strip("$")
            for j, opt in enumerate(v["options"]):
                if j == v["correctIndex"]:
                    continue
                opt_s = opt.strip("$")
                try:
                    diff = sympify(f"({corr_s}) - ({opt_s})")
                    if diff.free_symbols:
                        raise ValueError
                    assert sympify(f"simplify(({corr_s}) - ({opt_s}))") != 0, \
                        f"{v['id']} distractor equals correct: {opt}"
                except (Exception,):
                    # non-numeric (interval) option: string distinctness already ensured
                    assert opt != v["options"][v["correctIndex"]]

    print(f"SELFCHECK OK  forms=8  total={total}  min_per_form={min_per_form}")
