"""Problem-bank generator for topic: functions (Functions & Quadratics).

Generates ~36 machine-verified variants per form across 8 exam archetypes.
Run `python3 scripts/pb/functions.py` to execute the self-check.
"""

SLUG = "functions"
TITLE = "Functions & Quadratics"
TITLE_MN = "Функц"
BLURB = "Vertices, roots, discriminants, parameters — the parabola in every disguise it wears on exams."


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def place(correct, distractors, i):
    """Return (options, correctIndex) placing `correct` at slot i%4."""
    idx = i % 4
    opts = [None, None, None, None]
    opts[idx] = correct
    others = list(distractors)
    j = 0
    for p in range(4):
        if p == idx:
            continue
        opts[p] = others[j]
        j += 1
    return opts, idx


def signed_factor(r):
    """(x - r) with proper sign, e.g. (x - 2) or (x + 3)."""
    return f"(x - {r})" if r >= 0 else f"(x + {-r})"


def qstr(a, b, c):
    """Render a x^2 + b x + c as KaTeX (no surrounding $)."""
    parts = []
    parts.append("x^2" if a == 1 else f"{a}x^2")
    if b != 0:
        sign = "+" if b > 0 else "-"
        mag = abs(b)
        bt = "x" if mag == 1 else f"{mag}x"
        parts.append(f"{sign} {bt}")
    if c != 0:
        sign = "+" if c > 0 else "-"
        parts.append(f"{sign} {abs(c)}")
    return " ".join(parts)


def four_distinct_numbers(nums):
    return len(set(nums)) == 4


# --------------------------------------------------------------------------
# Form 1: vertex-read
# --------------------------------------------------------------------------
def gen_vertex():
    variants = []
    i = 0
    hs = [3, -2, 4, -1, 5, -4, 2, -6, 6, -3, 1, -5]
    ks = [-4, 5, 1, -6, 7, -3, 8, 2, -9, 6, -7, 4]
    for h in hs:
        for k in ks:
            if h == k:
                continue
            correct = f"$({h}; {k})$"
            d1 = f"$({-h}; {k})$"      # sign of h flipped
            d2 = f"$({h}; {-k})$"      # sign of k flipped
            d3 = f"$({k}; {h})$"       # coordinates swapped
            opts_set = {correct, d1, d2, d3}
            if len(opts_set) != 4:
                continue
            options, ci = place(correct, [d1, d2, d3], i)
            variants.append({
                "id": f"FUNC-vertex-v{len(variants)+1:02d}",
                "statement": f"The parabola $y = {signed_factor(h)}^2 {'+' if k>=0 else '-'} {abs(k)}$ has its vertex at…",
                "options": options,
                "correctIndex": ci,
                "explanation": f"Vertex form $y = (x - h)^2 + k$ puts the vertex at $(h; k)$: here $({h}; {k})$. Watch the sign: $(x - h)$ means the vertex sits at $+h$.",
                "check": [
                    f"({h} - {h})**2 + {k} == {k}",
                    f"({h}+1 - {h})**2 + {k} > {k}",
                ],
            })
            i += 1
            if len(variants) >= 36:
                return variants
    return variants


# --------------------------------------------------------------------------
# Form 2: factored-roots
# --------------------------------------------------------------------------
def gen_factored():
    variants = []
    i = 0
    for r1 in range(-5, 9):
        if r1 == 0:
            continue
        for r2 in range(r1 + 1, 10):
            if r2 == 0:
                continue
            S = r1 + r2
            if S == 0:
                continue
            prod = r1 * r2
            negS = -S
            diff = r2 - r1
            nums = [S, prod, negS, diff]
            if not four_distinct_numbers(nums):
                continue
            correct = f"${S}$"
            options, ci = place(correct, [f"${prod}$", f"${negS}$", f"${diff}$"], i)
            variants.append({
                "id": f"FUNC-roots-v{len(variants)+1:02d}",
                "statement": f"The equation ${signed_factor(r1)}{signed_factor(r2)} = 0$ has roots $x_1$ and $x_2$. Find $x_1 + x_2$.",
                "options": options,
                "correctIndex": ci,
                "explanation": f"A product is zero when a factor is zero: $x = {r1}$ or $x = {r2}$. Sum: ${S}$. (Vieta agrees: for $x^2 {'-' if S>=0 else '+'} {abs(S)}x {'+' if prod>=0 else '-'} {abs(prod)}$, the root sum is ${S}$.)",
                "check": [
                    f"solve({signed_factor(r1)}*{signed_factor(r2)}, x) == sorted([{r1}, {r2}])",
                    f"{r1} + {r2} == {S}",
                ],
            })
            i += 1
            if len(variants) >= 36:
                return variants
    return variants


# --------------------------------------------------------------------------
# Form 3: composition
# --------------------------------------------------------------------------
def gen_composition():
    variants = []
    i = 0
    for a in range(2, 7):
        for b in [-3, -1, 1, 2, 3, 5]:
            for n in range(2, 6):
                correct = a * n**2 + b
                d1 = (a * n + b)**2   # g(f(n)) — wrong order
                d2 = a * n + b        # forgot to square inside
                d3 = a * n**2         # forgot the +b
                nums = [correct, d1, d2, d3]
                if not four_distinct_numbers(nums):
                    continue
                copt = f"${correct}$"
                options, ci = place(copt, [f"${d1}$", f"${d2}$", f"${d3}$"], i)
                bsign = "+" if b >= 0 else "-"
                variants.append({
                    "id": f"FUNC-comp-v{len(variants)+1:02d}",
                    "statement": f"If $f(x) = {a}x {bsign} {abs(b)}$ and $g(x) = x^2$, find $f(g({n}))$.",
                    "options": options,
                    "correctIndex": ci,
                    "explanation": f"Inside first: $g({n}) = {n**2}$. Then $f({n**2}) = {a} \\cdot {n**2} {bsign} {abs(b)} = {correct}$. Composing in the wrong order gives $({a}\\cdot{n} {bsign} {abs(b)})^2$ — order matters.",
                    "check": [
                        f"{a}*{n}**2 + ({b}) == {correct}",
                    ],
                })
                i += 1
                if len(variants) >= 36:
                    return variants
    return variants


# --------------------------------------------------------------------------
# Form 4: discriminant
# --------------------------------------------------------------------------
DISC_OPTS = ["Two distinct real roots", "Exactly one real root",
             "No real roots", "Infinitely many roots"]


def _disc_variant(a, b, c, i, n):
    D = b * b - 4 * a * c
    if D > 0:
        correct = "Two distinct real roots"
        sign = ">"
        word = "Positive"
        tail = "two distinct roots"
    elif D == 0:
        correct = "Exactly one real root"
        sign = "=="
        word = "Zero"
        tail = "one (repeated) root"
    else:
        correct = "No real roots"
        sign = "<"
        word = "Negative"
        tail = "no real roots"
    distractors = [o for o in DISC_OPTS if o != correct]
    options, ci = place(correct, distractors, i)
    return {
        "id": f"FUNC-disc-v{n:02d}",
        "statement": f"How many real roots does ${qstr(a, b, c)} = 0$ have?",
        "options": options,
        "correctIndex": ci,
        "explanation": f"Discriminant: $D = ({b})^2 - 4 \\cdot {a} \\cdot ({c}) = {D}$. {word} ⟹ {tail}.",
        "check": [
            f"({b})**2 - 4*{a}*{c} == {D}",
            f"({b})**2 - 4*{a}*{c} {sign} 0",
        ],
    }


def gen_discriminant():
    two, one, none = [], [], []
    # two distinct real roots (D>0)
    for a in [1, 2]:
        for p in range(-3, 4):
            for q in range(p + 1, 6):
                b = -a * (p + q)
                c = a * p * q
                if b * b - 4 * a * c <= 0:
                    continue
                two.append((a, b, c))
    # exactly one real root (D=0): a(x+t)^2
    for a in [1, 2]:
        for t in [1, -1, 2, -2, 3, -3, 4, -4, 5, 6]:
            b = 2 * a * t
            c = a * t * t
            one.append((a, b, c))
    # no real roots (D<0)
    for b in [0, 1, 2, 3, 4, 5, 6, 2, 4]:
        for d in [1, 2, 3]:
            a = 1
            c = (b * b) // 4 + d
            if b * b - 4 * a * c < 0:
                none.append((a, b, c))
    # dedupe by statement key
    def dedupe(lst):
        seen = set()
        out = []
        for t in lst:
            if t in seen:
                continue
            seen.add(t)
            out.append(t)
        return out
    two, one, none = dedupe(two), dedupe(one), dedupe(none)

    variants = []
    i = 0
    pools = [two, one, none]
    idxs = [0, 0, 0]
    # round-robin ~12 from each until 36
    while len(variants) < 36:
        progressed = False
        for pi in range(3):
            if idxs[pi] < len(pools[pi]):
                a, b, c = pools[pi][idxs[pi]]
                idxs[pi] += 1
                variants.append(_disc_variant(a, b, c, i, len(variants) + 1))
                i += 1
                progressed = True
                if len(variants) >= 36:
                    break
        if not progressed:
            break
    return variants


# --------------------------------------------------------------------------
# Form 5: complete-square-min
# --------------------------------------------------------------------------
def gen_min():
    variants = []
    i = 0
    for hb in range(2, 9):          # b = 2*hb, hb from 2..8
        b = 2 * hb
        q = hb * hb
        for c in range(-6, 14):
            mn = c - q
            nums = [mn, c, q - c, q]
            if not four_distinct_numbers(nums):
                continue
            correct = f"${mn}$"
            # distractors: c (the constant), -min = q-c, q = (b/2)^2
            options, ci = place(correct, [f"${c}$", f"${q - c}$", f"${q}$"], i)
            variants.append({
                "id": f"FUNC-min-v{len(variants)+1:02d}",
                "statement": f"Find the MINIMUM value of $y = {qstr(1, b, c)}$.",
                "options": options,
                "correctIndex": ci,
                "explanation": f"Complete the square: $y = (x + {hb})^2 + ({mn})$. A square is never negative, so the minimum is ${mn}$, reached at $x = {-hb}$.",
                "check": [
                    f"({-hb})**2 + {b}*({-hb}) + {c} == {mn}",
                    f"({-hb + 1})**2 + {b}*({-hb + 1}) + {c} > {mn}",
                ],
            })
            i += 1
            if len(variants) >= 36:
                return variants
    return variants


# --------------------------------------------------------------------------
# Form 6: quadratic-inequality
# --------------------------------------------------------------------------
def _interval_between(a, b):
    return f"${a} < x < {b}$"


def gen_qineq():
    variants = []
    i = 0
    for r1 in range(-5, 7):
        for gap in [2, 3, 4, 5]:
            r2 = r1 + gap
            B = -(r1 + r2)   # coefficient of x
            C = r1 * r2
            tp = r1 + 1      # strictly inside (gap>=2)
            outside = r2 + 1
            correct = _interval_between(r1, r2)
            d1 = f"$x < {r1} \\text{{ or }} x > {r2}$"   # outside (sign of ineq)
            d2 = f"$x < {r2}$"                           # only one bound
            d3 = _interval_between(-r2, -r1)             # reflected sign
            opts_set = {correct, d1, d2, d3}
            if len(opts_set) != 4:
                continue
            options, ci = place(correct, [d1, d2, d3], i)
            variants.append({
                "id": f"FUNC-qineq-v{len(variants)+1:02d}",
                "statement": f"Solve: ${qstr(1, B, C)} < 0$.",
                "options": options,
                "correctIndex": ci,
                "explanation": f"Factor: ${signed_factor(r1)}{signed_factor(r2)} < 0$. An upward parabola is NEGATIVE between its roots: ${r1} < x < {r2}$.",
                "check": [
                    f"({tp} - {r1})*({tp} - {r2}) < 0",
                    f"({outside} - {r1})*({outside} - {r2}) > 0",
                ],
            })
            i += 1
            if len(variants) >= 36:
                return variants
    return variants


# --------------------------------------------------------------------------
# Form 7: tangency-parameter
# --------------------------------------------------------------------------
def gen_tangency():
    variants = []
    i = 0
    mags = list(range(4, 42, 2))   # even magnitudes 4..40
    for mag in mags:
        for sign in [1, -1]:
            b = sign * mag
            if b == 4:   # would collide correct(4) with coefficient b(4)
                continue
            m = (b * b) // 4
            hb = b // 2
            d1 = b * b        # forgot the /4
            d2 = (b * b) // 2  # divided by 2 instead of 4
            d3 = b            # used the coefficient b itself
            nums = [m, d1, d2, d3]
            if not four_distinct_numbers(nums):
                continue
            correct = f"${m}$"
            options, ci = place(correct, [f"${d1}$", f"${d2}$", f"${d3}$"], i)
            bsign = "+" if b >= 0 else "-"
            variants.append({
                "id": f"FUNC-tan-v{len(variants)+1:02d}",
                "statement": f"For which $m$ does $x^2 {bsign} {abs(b)}x + m = 0$ have exactly ONE root?",
                "options": options,
                "correctIndex": ci,
                "explanation": f"Exactly one root needs $D = 0$: $({b})^2 - 4m = 0 \\Rightarrow m = \\frac{{{b*b}}}{{4}} = {m}$. Then $x^2 {bsign} {abs(b)}x + {m} = (x {'+' if hb>=0 else '-'} {abs(hb)})^2$ — a perfect square kissing the axis.",
                "check": [
                    f"({b})**2 - 4*{m} == 0",
                    f"expand((x + ({hb}))**2) == x**2 + ({b})*x + {m}",
                ],
            })
            i += 1
            if len(variants) >= 36:
                return variants
    return variants


# --------------------------------------------------------------------------
# Form 8: inverse-value
# --------------------------------------------------------------------------
def gen_inverse():
    variants = []
    i = 0
    for a in range(2, 7):
        for b in [-3, -1, 1, 2, 4, 5]:
            for root in range(2, 7):
                v = a * root + b
                d1 = a * v + b     # computed f(v) — classic trap
                d2 = v - b         # forgot to divide by a
                d3 = root + 1      # off by one
                nums = [root, d1, d2, d3]
                if not four_distinct_numbers(nums):
                    continue
                correct = f"${root}$"
                options, ci = place(correct, [f"${d1}$", f"${d2}$", f"${d3}$"], i)
                bsign = "+" if b >= 0 else "-"
                variants.append({
                    "id": f"FUNC-inv-v{len(variants)+1:02d}",
                    "statement": f"If $f(x) = {a}x {bsign} {abs(b)}$, find $f^{{-1}}({v})$.",
                    "options": options,
                    "correctIndex": ci,
                    "explanation": f"$f^{{-1}}({v})$ asks which $x$ gives $f(x) = {v}$. Solve ${a}x {bsign} {abs(b)} = {v}$: $x = {root}$. (Computing $f({v})$ instead is the classic trap.)",
                    "check": [
                        f"solve({a}*x + ({b}) - {v}, x) == [{root}]",
                        f"{a}*{root} + ({b}) == {v}",
                    ],
                })
                i += 1
                if len(variants) >= 36:
                    return variants
    return variants


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build():
    return {
        "slug": SLUG,
        "title": TITLE,
        "titleMn": TITLE_MN,
        "blurb": BLURB,
        "forms": [
            {"id": "vertex-read", "title": "Reading the vertex", "level": 1,
             "skill": "y = (x−h)² + k has vertex (h; k) — mind the sign of h.",
             "variants": gen_vertex()},
            {"id": "factored-roots", "title": "Roots from factored form", "level": 1,
             "skill": "Zero-product property; Vieta's sum = −b/a.",
             "variants": gen_factored()},
            {"id": "composition", "title": "Composing functions", "level": 1,
             "skill": "f(g(x)): evaluate the inner function first.",
             "variants": gen_composition()},
            {"id": "discriminant", "title": "Counting roots with the discriminant", "level": 2,
             "skill": "D = b² − 4ac: positive two, zero one, negative none.",
             "variants": gen_discriminant()},
            {"id": "complete-square-min", "title": "Minimum via completing the square", "level": 2,
             "skill": "x² + bx + c = (x + b/2)² + (c − b²/4); the constant IS the minimum.",
             "variants": gen_min()},
            {"id": "quadratic-inequality", "title": "Quadratic inequalities", "level": 2,
             "skill": "Factor, find roots, read the sign between/outside.",
             "variants": gen_qineq()},
            {"id": "tangency-parameter", "title": "Parameter for exactly one root", "level": 3,
             "skill": "One root ⟺ D = 0; solve for the parameter.",
             "variants": gen_tangency()},
            {"id": "inverse-value", "title": "Inverse function values", "level": 3,
             "skill": "f⁻¹(v) = the input that outputs v — solve f(x) = v.",
             "variants": gen_inverse()},
        ],
    }


# --------------------------------------------------------------------------
# self-check
# --------------------------------------------------------------------------
if __name__ == "__main__":
    from sympy import sympify, simplify

    EXPECTED_IDS = ["vertex-read", "factored-roots", "composition", "discriminant",
                    "complete-square-min", "quadratic-inequality",
                    "tangency-parameter", "inverse-value"]

    data = build()
    forms = data["forms"]
    assert len(forms) == 8, f"expected 8 forms, got {len(forms)}"
    assert [f["id"] for f in forms] == EXPECTED_IDS, "form ids mismatch"

    all_ids = set()
    total = 0
    min_per_form = 10**9

    def strip(o):
        return o.strip().strip("$").strip()

    for f in forms:
        vs = f["variants"]
        assert len(vs) >= 32, f"form {f['id']} has only {len(vs)} variants"
        min_per_form = min(min_per_form, len(vs))
        total += len(vs)
        for v in vs:
            assert v["id"] not in all_ids, f"duplicate id {v['id']}"
            all_ids.add(v["id"])
            opts = v["options"]
            assert len(opts) == 4, f"{v['id']} options != 4"
            assert len(set(opts)) == 4, f"{v['id']} options not distinct"
            assert 0 <= v["correctIndex"] <= 3, f"{v['id']} bad correctIndex"
            # checks
            for cs in v["check"]:
                res = sympify(cs)
                assert bool(res) is True, f"{v['id']} check failed: {cs} -> {res}"
            # numeric distinctness of correct vs distractors
            ci = v["correctIndex"]
            correct = opts[ci]
            try:
                cval = sympify(strip(correct))
                cnum = cval.is_number
            except Exception:
                cval, cnum = None, False
            for k, o in enumerate(opts):
                if k == ci:
                    continue
                if cnum:
                    try:
                        oval = sympify(strip(o))
                        onum = oval.is_number
                    except Exception:
                        onum = False
                    if onum:
                        assert simplify(cval - oval) != 0, \
                            f"{v['id']} distractor equals correct: {o}"
                    else:
                        assert o != correct
                else:
                    assert o != correct

    print(f"SELFCHECK OK  forms=8  total={total}  min_per_form={min_per_form}")
