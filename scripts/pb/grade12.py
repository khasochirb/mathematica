# -*- coding: utf-8 -*-
"""Grade 12 problem bank — the exit level of the High school band.

Companion to scripts/pb/grade9.py (see its header for the why): the verified
MCQ pool that the High band's exit exams select from, and Grade 12's own
topic-practice surface. Unit ids equal the Grade-12 topic slugs so bank units
link into /math/12/<slug>. Grade 12 is the ЭЕШ transition year — level 3
items sit at exam difficulty.
"""
import os
import sys

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from sympy import Rational

from imbank import fmt, lin, mk_num, mk_txt, form, pt

TI, LC, DV, AD, IG, VC, CS = (
    "trigonometric-identities", "limits-and-continuity", "derivatives",
    "applications-of-derivatives", "integrals", "vectors", "conic-sections",
)

UNITS = [
    {"id": TI, "title": "Trigonometric Identities",
     "blurb": "The Pythagorean identity, double angles, and trig equations."},
    {"id": LC, "title": "Limits & Continuity",
     "blurb": "Substitution, the 0/0 form, and limits at infinity."},
    {"id": DV, "title": "Derivatives",
     "blurb": "Power, chain and product rules, evaluated at a point."},
    {"id": AD, "title": "Applications of Derivatives",
     "blurb": "Tangent slopes, increasing intervals, and optimization."},
    {"id": IG, "title": "Integrals",
     "blurb": "Antiderivatives, definite integrals, and motion."},
    {"id": VC, "title": "Vectors",
     "blurb": "Components, magnitude, and perpendicularity."},
    {"id": CS, "title": "Conic Sections",
     "blurb": "Circles, parabola foci, and classifying conics."},
]

# Pythagorean triples (opp, adj, hyp) for exact trig values.
_TRIPS = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41)]


# ===========================================================================
# Trigonometric Identities
# ===========================================================================

def _g_pythagorean_identity():
    """Given sin(t) = p/q with a stated quadrant, find cos(t)."""
    raws = []
    for (p0, a0, q) in _TRIPS:
        for (p, a) in ((p0, a0), (a0, p0)):
            for (quad, cos_sign) in ((1, 1), (2, -1)):
                sin_v = Rational(p, q)
                cos_v = cos_sign * Rational(a, q)
                where = "0 < \\theta < \\dfrac{\\pi}{2}" if quad == 1 \
                    else "\\dfrac{\\pi}{2} < \\theta < \\pi"
                raws.append({
                    "statement": "Given that $\\sin\\theta = %s$ and $%s$, find "
                                 "$\\cos\\theta$." % (fmt(sin_v), where),
                    "correct": cos_v,
                    # wrong sign for the quadrant · echoed sin · quoted tan
                    "dvals": [-cos_v, sin_v, cos_sign * Rational(p, a)],
                    "explanation": "$\\cos^2\\theta = 1 - \\sin^2\\theta = 1 - %s = %s$, "
                                   "so $\\cos\\theta = \\pm%s$ — and the quadrant "
                                   "decides: in quadrant %s cosine is %s, giving $%s$. "
                                   "The identity only hands you the magnitude; the "
                                   "quadrant hands you the sign."
                                   % (fmt(sin_v ** 2), fmt(Rational(a * a, q * q)),
                                      fmt(Rational(a, q)), "I" if quad == 1 else "II",
                                      "positive" if cos_sign > 0 else "negative",
                                      fmt(cos_v)),
                    "check": ["Eq(Rational(%d,%d)**2 + Rational(%d,%d)**2, 1)"
                              % (p, q, a, q),
                              "Eq(Rational(%d,%d)**2, 1 - Rational(%d,%d)**2)"
                              % (abs(cos_v.p), cos_v.q, p, q)],
                })
    return raws


def _g_double_angle():
    """sin(2t) = 2 sin t cos t from a triple (acute t)."""
    raws = []
    for (p, a, q) in _TRIPS:
        for swap in (False, True):
            opp, adj = (p, a) if not swap else (a, p)
            sin_v, cos_v = Rational(opp, q), Rational(adj, q)
            s2 = 2 * sin_v * cos_v
            c2 = 1 - 2 * sin_v ** 2
            raws.append({
                "statement": "The acute angle $\\theta$ has $\\sin\\theta = %s$. Find "
                             "$\\sin 2\\theta$." % fmt(sin_v),
                "correct": s2,
                # doubled sin without cos · forgot the factor 2 · computed cos 2θ
                "dvals": [2 * sin_v, sin_v * cos_v, c2],
                "explanation": "$\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$, and "
                               "$\\cos\\theta = %s$ from the $%d$-$%d$-$%d$ triangle: "
                               "$2 \\cdot %s \\cdot %s = %s$. $\\sin 2\\theta \\ne "
                               "2\\sin\\theta$ — doubling the ANGLE is not doubling the "
                               "sine (indeed $%s > 1$ is impossible for a sine)."
                               % (fmt(cos_v), min(p, a), max(p, a), q, fmt(sin_v),
                                  fmt(cos_v), fmt(s2), fmt(2 * sin_v)) if 2 * sin_v > 1 else
                               "$\\sin 2\\theta = 2\\sin\\theta\\cos\\theta$, and "
                               "$\\cos\\theta = %s$ from the $%d$-$%d$-$%d$ triangle: "
                               "$2 \\cdot %s \\cdot %s = %s$. $\\sin 2\\theta \\ne "
                               "2\\sin\\theta$ — doubling the ANGLE is not doubling the "
                               "sine."
                               % (fmt(cos_v), min(p, a), max(p, a), q, fmt(sin_v),
                                  fmt(cos_v), fmt(s2)),
                "check": ["Eq(2*Rational(%d,%d)*Rational(%d,%d), Rational(%d,%d))"
                          % (opp, q, adj, q, s2.p, s2.q),
                          "Eq(Rational(%d,%d)**2 + Rational(%d,%d)**2, 1)"
                          % (opp, q, adj, q)],
            })
            # the cos 2θ sibling — same triple, the other double-angle formula
            raws.append({
                "statement": "The acute angle $\\theta$ has $\\sin\\theta = %s$. Find "
                             "$\\cos 2\\theta$." % fmt(sin_v),
                "correct": c2,
                # sign flipped (sin² - cos²) · dropped the 2 · computed sin 2θ
                "dvals": [-c2, 1 - sin_v ** 2, s2],
                "explanation": "$\\cos 2\\theta = 1 - 2\\sin^2\\theta = 1 - "
                               "2 \\cdot %s = %s$. The formula subtracts TWICE the "
                               "sine squared — $1 - \\sin^2\\theta$ is just "
                               "$\\cos^2\\theta$, a different quantity."
                               % (fmt(sin_v ** 2), fmt(c2)),
                "check": ["Eq(1 - 2*Rational(%d,%d)**2, Rational(%d,%d))"
                          % (opp, q, c2.p, c2.q)],
            })
    return raws


# Rational root pairs for factorable quadratics in sin/cos, with the solution
# count each root contributes on [0, 2pi): |r| < 1 → 2, |r| = 1 → 1, else 0.
_ROOT_PAIRS = [
    (Rational(1), Rational(1, 2)), (Rational(-1), Rational(1, 2)),
    (Rational(1, 2), Rational(-1, 2)), (Rational(1), Rational(-1)),
    (Rational(1, 2), Rational(2)), (Rational(-1, 2), Rational(3, 2)),
    (Rational(1), Rational(3, 2)), (Rational(1), Rational(0)),
    (Rational(-1), Rational(0)), (Rational(0), Rational(1, 2)),
    (Rational(3, 2), Rational(1, 2)), (Rational(-1), Rational(-1, 2)),
    (Rational(2), Rational(-2)), (Rational(-1, 2), Rational(1, 2)),
    (Rational(0), Rational(-1, 2)), (Rational(1), Rational(-1, 2)),
]


def _sol_count(r):
    if abs(r) < 1:
        return 2
    if abs(r) == 1:
        return 1
    return 0


def _root_range_check(r):
    """The sympy assertion behind a root's solution count."""
    n = _sol_count(r)
    if n == 2:
        return "Abs(Rational(%d,%d)) < 1" % (r.p, r.q)
    if n == 1:
        return "Eq(Abs(Rational(%d,%d)), 1)" % (r.p, r.q)
    return "Abs(Rational(%d,%d)) > 1" % (r.p, r.q)


def _g_trig_equation_count():
    """How many solutions does a factorable quadratic trig equation have?"""
    raws = []
    for func in ("sin", "cos"):
        for (r1, r2) in _ROOT_PAIRS:
            if r1 == r2:
                continue
            # a (f - r1)(f - r2) with integer coefficients
            den = r1.q * r2.q
            a = den
            b = int(-a * (r1 + r2))
            c = int(a * r1 * r2)
            n = _sol_count(r1) + _sol_count(r2)
            fl = "\\%s" % func
            terms = "%d%s^2 x" % (a, fl) if a != 1 else "%s^2 x" % fl
            if b:
                terms += " %s %s%s\\, x" % ("+" if b > 0 else "-",
                                            "" if abs(b) == 1 else abs(b), fl)
            if c:
                terms += " %s %d" % ("+" if c > 0 else "-", abs(c))
            others = [x for x in (0, 1, 2, 3, 4) if x != n][:3]
            raws.append({
                "statement": "How many solutions does the equation $%s = 0$ have for "
                             "$0 \\le x < 2\\pi$?" % terms,
                "correct": n,
                "dvals": others,
                "explanation": "Factor as a quadratic in $%s x$: the roots are "
                               "$%s x = %s$ and $%s x = %s$. A value strictly between "
                               "$-1$ and $1$ is hit twice per turn, $\\pm 1$ exactly "
                               "once, and anything beyond $\\pm 1$ never — total "
                               "$%d$. Count from the unit circle, root by root."
                               % (fl, fl, fmt(r1), fl, fmt(r2), n),
                "check": ["Eq(expand(%d*(s - Rational(%d,%d))*(s - Rational(%d,%d))), "
                          "%d*s**2 + (%d)*s + (%d))"
                          % (a, r1.p, r1.q, r2.p, r2.q, a, b, c)] +
                         [_root_range_check(r) for r in (r1, r2)],
            })
    return raws


# ===========================================================================
# Limits & Continuity
# ===========================================================================

def _g_limit_substitution():
    """Limit of a polynomial by direct substitution."""
    raws = []
    for a in (1, 2, -1, 3):
        for b in (2, -3, 5, -4):
            for c in (1, -2, 4):
                for t in (2, -1, 3, -2):
                    v = a * t * t + b * t + c
                    raws.append({
                        "statement": "Evaluate $\\displaystyle\\lim_{x \\to %d} "
                                     "\\left(%s\\right)$."
                                     % (t, _quad_str(a, b, c)),
                        "correct": v,
                        # sign slip on t in the middle term · evaluated at -t ·
                        # dropped the constant
                        "dvals": [a * t * t - b * t + c,
                                  a * t * t + b * (-t) + c if a * t * t + b * (-t) + c != a * t * t - b * t + c else v + 1,
                                  a * t * t + b * t],
                        "explanation": "Polynomials are continuous, so the limit IS the "
                                       "value: substitute $x = %d$ to get $%d$. No "
                                       "algebra tricks needed — save those for the "
                                       "$0/0$ forms."
                                       % (t, v),
                        "check": ["Eq(limit(%d*x**2 + (%d)*x + (%d), x, %d), %d)"
                                  % (a, b, c, t, v)],
                    })
    return raws


def _quad_str(a, b, c):
    s = "x^2" if a == 1 else ("-x^2" if a == -1 else "%dx^2" % a)
    if b:
        s += " %s %s" % ("+" if b > 0 else "-", "x" if abs(b) == 1 else "%dx" % abs(b))
    if c:
        s += " %s %d" % ("+" if c > 0 else "-", abs(c))
    return s


def _g_limit_hole():
    """0/0 holes: factor and cancel."""
    raws = []
    for a in (2, 3, 4, 5, 6, 7):
        raws.append({
            "statement": "Evaluate $\\displaystyle\\lim_{x \\to %d} "
                         "\\dfrac{x^2 - %d}{x - %d}$." % (a, a * a, a),
            "correct": 2 * a,
            # answered 0 (the numerator's value) · said undefined ≈ picked the
            # denominator's 0 as the answer... use a · a^2
            "dvals": [0, a, a * a],
            "explanation": "At $x = %d$ this is $\\frac{0}{0}$ — a hole, not an answer. "
                           "Factor: $\\dfrac{(x-%d)(x+%d)}{x-%d} = x + %d$ away from the "
                           "hole, so the limit is $%d$. $\\frac{0}{0}$ means \"do more "
                           "work\", never \"the answer is 0\"."
                           % (a, a, a, a, a, 2 * a),
            "check": ["Eq(limit((x**2 - %d)/(x - %d), x, %d), %d)" % (a * a, a, a, 2 * a)],
        })
    for a in (1, 2, 3, 4, 5):
        for b in (2, 3, 5, 6, 7):
            if a == b or a - b in (0, a, a * a):
                continue
            # (x - a)(x - b)/(x - a) -> a - b at x = a
            s, p = a + b, a * b
            raws.append({
                "statement": "Evaluate $\\displaystyle\\lim_{x \\to %d} "
                             "\\dfrac{x^2 - %dx + %d}{x - %d}$." % (a, s, p, a),
                "correct": a - b,
                # 0 · the other root · forgot to cancel and quoted a
                "dvals": [0, b, a] if a not in (0, a - b, b) else [0, b, a + b],
                "explanation": "The numerator factors as $(x - %d)(x - %d)$, so away "
                               "from the hole the function IS $x - %d$, and the limit "
                               "is $%d - %d = %d$."
                               % (a, b, b, a, b, a - b),
                "check": ["Eq(limit((x**2 - %d*x + %d)/(x - %d), x, %d), %d)"
                          % (s, p, a, a, a - b)],
            })
    return raws


def _g_limit_infinity():
    """Limit at infinity of a rational function with equal degrees."""
    raws = []
    for a in (2, 3, 4, 5, 6, 8):
        for d in (2, 3, 4, 5, 7):
            if a == d:
                continue
            for (b, e) in ((1, 2), (-3, 1), (5, -2)):
                for (c, f) in ((1, 3), (-2, 5)):
                    v = Rational(a, d)
                    if v in (Rational(b, e), Rational(c, f)):
                        continue
                    raws.append({
                        "statement": "Evaluate $\\displaystyle\\lim_{x \\to \\infty} "
                                     "\\dfrac{%s}{%s}$."
                                     % (_quad_str(a, b, c), _quad_str(d, e, f)),
                        "correct": v,
                        # ratio of the x-coefficients · ratio of the constants ·
                        # inverted
                        "dvals": [Rational(b, e), Rational(c, f), Rational(d, a)],
                        "explanation": "For $x$ huge, only the leading terms matter: "
                                       "$\\dfrac{%dx^2}{%dx^2} \\to %s$. The lower-order "
                                       "terms are noise at infinity — the constants' "
                                       "ratio $%s$ is what the limit at $0$ would care "
                                       "about, not the limit at $\\infty$."
                                       % (a, d, fmt(v), fmt(Rational(c, f))),
                        "check": ["Eq(limit((%d*x**2 + (%d)*x + (%d))/(%d*x**2 + (%d)*x "
                                  "+ (%d)), x, oo), Rational(%d,%d))"
                                  % (a, b, c, d, e, f, v.p, v.q)],
                    })
    return raws


# ===========================================================================
# Derivatives
# ===========================================================================

def _g_power_rule():
    """f(x) = a x^n: f'(t)."""
    raws = []
    for a in (2, 3, -2, 4, 5):
        for n in (3, 4):
            for t in (1, 2, -1, -2):
                v = a * n * t ** (n - 1)
                raws.append({
                    "statement": "Let $f(x) = %dx^%d$. Find $f'(%d)$." % (a, n, t),
                    "correct": v,
                    # forgot to multiply by the exponent · forgot to drop the
                    # power · evaluated f
                    "dvals": [a * t ** (n - 1), a * n * t ** n, a * t ** n],
                    "explanation": "Power rule: $f'(x) = %d \\cdot %d x^{%d} = %dx^{%d}$, "
                                   "so $f'(%d) = %d$. Both moves matter — multiply by "
                                   "the old exponent AND lower it by one."
                                   % (n, a, n - 1, a * n, n - 1, t, v),
                    "check": ["Eq(diff(%d*x**%d, x).subs(x, %d), %d)" % (a, n, t, v)],
                })
    return raws


def _g_chain_rule():
    """f(x) = (a x + b)^n: f'(t) = n a (a t + b)^(n-1)."""
    raws = []
    for a in (2, 3, -2):
        for b in (1, -2, 4, -1):
            for n in (2, 3):
                for t in (1, 2, -1):
                    inner = a * t + b
                    v = n * a * inner ** (n - 1)
                    raws.append({
                        "statement": "Let $f(x) = (%s)^%d$. Find $f'(%d)$."
                                     % (lin(a, b), n, t),
                        "correct": v,
                        # forgot the inner derivative · power rule on x alone ·
                        # evaluated f instead
                        "dvals": [n * inner ** (n - 1), n * a * t ** (n - 1),
                                  inner ** n],
                        "explanation": "Chain rule: $f'(x) = %d(%s)^{%d} \\cdot %d$ — the "
                                       "outer power TIMES the inner derivative. At "
                                       "$x = %d$: $%d \\cdot %d \\cdot %d = %d$. Dropping "
                                       "the inner factor $%d$ gives $%d$."
                                       % (n, lin(a, b), n - 1, a, t, n,
                                          inner ** (n - 1), a, v, a, n * inner ** (n - 1)),
                        "check": ["Eq(diff((%d*x + (%d))**%d, x).subs(x, %d), %d)"
                                  % (a, b, n, t, v)],
                    })
    return raws


def _g_product_rule_12():
    """f(x) = x^2 (x + a): f'(t)."""
    raws = []
    for a in (1, 2, -2, 3, -3, 4, 5, -4, 6):
        for t in (1, 2, -1, -2, 3, -3, 4):
            v = 2 * t * (t + a) + t * t
            d_prod = 2 * t                     # product of derivatives (2x · 1)
            d_first = 2 * t * (t + a)          # first term only
            d_f = t * t * (t + a)              # evaluated f
            raws.append({
                "statement": "Let $f(x) = x^2%s$. Find $f'(%d)$." % (_xpa(a), t),
                "correct": v,
                "dvals": [d_prod, d_first, d_f],
                "explanation": "Product rule: $f'(x) = 2x%s + x^2 \\cdot 1$; at $x = %d$ "
                               "this is $%d + %d = %d$. The derivative of a product is "
                               "NOT the product of the derivatives ($2x \\cdot 1$ gives "
                               "$%d$)." % (_xpa(a), t, d_first, t * t, v, d_prod),
                "check": ["Eq(diff(x**2*(x + (%d)), x).subs(x, %d), %d)" % (a, t, v)],
            })
    return raws


def _xpa(a):
    return "(x + %d)" % a if a > 0 else "(x - %d)" % -a


# ===========================================================================
# Applications of Derivatives
# ===========================================================================

def _g_tangent_slope():
    """Slope of the tangent to f = x^2 + bx + c at x = p."""
    raws = []
    for b in (2, -2, 4, -4, 6, -6, 3):
        for c in (1, -3, 5):
            for p in (1, 2, -1, 3, -2):
                m = 2 * p + b
                fp = p * p + b * p + c
                if m in (fp, p, 2 * p - b):
                    continue
                raws.append({
                    "statement": "What is the slope of the tangent to the curve "
                                 "$y = %s$ at the point where $x = %d$?"
                                 % (_quad_str(1, b, c), p),
                    "correct": m,
                    # evaluated y instead of y' · quoted x · sign slip on b
                    "dvals": [fp, p, 2 * p - b],
                    "explanation": "Slope means DERIVATIVE: $y' = 2x %s %d$, so at "
                                   "$x = %d$ the slope is $%d$. $%d$ is the HEIGHT of "
                                   "the curve there — the number the tangent touches, "
                                   "not its steepness."
                                   % ("+" if b > 0 else "-", abs(b), p, m, fp),
                    "check": ["Eq(diff(x**2 + (%d)*x + (%d), x).subs(x, %d), %d)"
                              % (b, c, p, m)],
                })
    return raws


def _g_increasing_interval():
    """Where is f = x^2 + bx + c increasing?"""
    raws = []
    for b in (2, 4, 6, -2, -4, -6, 8, -8, 10, -10, 3, -3, 5, -5):
        for c in (1, -2, 3):
            h = Rational(-b, 2)
            raws.append({
                "statement": "On what interval is $f(x) = %s$ increasing?"
                             % _quad_str(1, b, c),
                "correct": "$x > %s$" % fmt(h),
                # direction flipped · sign of the critical point flipped ·
                # increasing everywhere
                "dvals": ["$x < %s$" % fmt(h), "$x > %s$" % fmt(-h),
                          "all real numbers"],
                "explanation": "Increasing where $f' > 0$: $f'(x) = 2x %s %d > 0$ gives "
                               "$x > %s$. An upward parabola falls, bottoms out at its "
                               "vertex, then rises — the derivative's sign says which "
                               "side is which."
                               % ("+" if b > 0 else "-", abs(b), fmt(h)),
                "check": ["Eq(diff(x**2 + (%d)*x + (%d), x).subs(x, Rational(%d,%d)), 0)"
                          % (b, c, h.p, h.q),
                          "diff(x**2 + (%d)*x + (%d), x).subs(x, Rational(%d,%d) + 1) > 0"
                          % (b, c, h.p, h.q)],
            })
    return raws


def _g_optimize_product():
    """Two numbers with a fixed sum: the maximum product."""
    raws = []
    for S in (8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40,
              44, 48, 50, 52, 56, 60, 64):
        half = S // 2
        best = half * half
        raws.append({
            "statement": "Two positive numbers add up to $%d$. What is the largest "
                         "possible value of their product?" % S,
            "correct": best,
            # split off by one · S^2/2 (dropped a half) · used S itself
            "dvals": [(half - 1) * (half + 1), S * S // 2, S],
            "explanation": "With $x + y = %d$, the product $x(%d - x)$ is a downward "
                           "parabola peaking at $x = %d$: $%d \\cdot %d = %d$. Any "
                           "uneven split loses — even $%d \\cdot %d = %d$, just one "
                           "step off, is smaller."
                           % (S, S, half, half, half, best, half - 1, half + 1,
                              (half - 1) * (half + 1)),
            "check": ["Eq(%d*%d, %d)" % (half, half, best),
                      "%d*%d > (%d)*(%d)" % (half, half, half - 1, half + 1)],
        })
    return raws


# ===========================================================================
# Integrals
# ===========================================================================

def _g_antiderivative():
    """General antiderivative of a x^n."""
    raws = []
    for n in (2, 3, 4):
        for k in (1, 2, 3, 4, 5, 6, 7, 8):
            a = k * (n + 1)  # so the antiderivative's coefficient is the integer k
            raws.append({
                "statement": "Find $\\displaystyle\\int %dx^%d\\,dx$." % (a, n),
                "correct": "$%dx^%d + C$" % (k, n + 1),
                # differentiated instead · forgot to divide · kept the power
                "dvals": ["$%dx^%d + C$" % (a * n, n - 1) if n > 1 else "$%d + C$" % a,
                          "$%dx^%d + C$" % (a, n + 1),
                          "$%dx^%d + C$" % (k, n)],
                "explanation": "Raise the power, divide by the new power: "
                               "$\\dfrac{%d}{%d}x^{%d} + C = %dx^{%d} + C$. Check by "
                               "differentiating — it must give back $%dx^%d$."
                               % (a, n + 1, n + 1, k, n + 1, a, n),
                "check": ["Eq(diff(%d*x**%d, x), %d*x**%d)" % (k, n + 1, a, n),
                          "Eq(integrate(%d*x**%d, x), %d*x**%d)" % (a, n, k, n + 1)],
            })
    return raws


def _g_definite_linear():
    """Definite integral of 2x + c from 1 to b."""
    raws = []
    for b in (2, 3, 4, 5, 6):
        for c in (1, 2, 4, -2, 3, 5, -3):
            v = (b * b + c * b) - (1 + c)
            d_forgot_lower = b * b + c * b
            d_no_c = b * b - 1
            d_rect = (2 * b + c) * (b - 1)
            raws.append({
                "statement": "Evaluate $\\displaystyle\\int_1^{%d} (2x %s %d)\\,dx$."
                             % (b, "+" if c >= 0 else "-", abs(c)),
                "correct": v,
                # forgot the lower limit · dropped the constant term · integrand
                # at b times the width (a rectangle, not the area)
                "dvals": [d_forgot_lower, d_no_c, d_rect],
                "explanation": "An antiderivative is $x^2 %s %dx$; evaluate at both "
                               "limits: $(%d %s %d) - (1 %s %d) = %d$. Subtracting the "
                               "lower limit's value is half the Fundamental Theorem — "
                               "forgetting it gives $%d$."
                               % ("+" if c >= 0 else "-", abs(c), b * b,
                                  "+" if c >= 0 else "-", abs(c * b),
                                  "+" if c >= 0 else "-", abs(c), v, d_forgot_lower),
                "check": ["Eq(integrate(2*x + (%d), (x, 1, %d)), %d)" % (c, b, v)],
            })
    return raws


def _g_displacement():
    """Displacement from v(t) = at + b on [0, T]."""
    raws = []
    for a in (2, 4, 6, -2):
        for b in (3, 5, 1, 8):
            for T in (2, 3, 4, 5):
                v_end = a * T + b
                s = a * T * T // 2 + b * T if (a * T * T) % 2 == 0 else None
                if s is None or v_end <= 0:
                    continue
                d_rect = v_end * T   # final speed × time (== forgetting the 1/2,
                #                      the same wrong number two ways)
                d_start = b * T      # starting speed × time
                raws.append({
                    "statement": "A particle's velocity is $v(t) = %s$ metres per "
                                 "second. How far does it travel from $t = 0$ to "
                                 "$t = %d$ seconds?" % (lin(a, b, "t"), T),
                    "correct": s,
                    # final speed × time · starting speed × time · quoted the
                    # final speed itself
                    "dvals": [d_rect, d_start, v_end],
                    "explanation": "Distance is the integral of speed: "
                                   "$\\displaystyle\\int_0^{%d} (%s)\\,dt = "
                                   "\\left[%st^2 %s %dt\\right]_0^{%d} = %d$ m. "
                                   "Final-speed-times-time ($%d$) pretends the speed "
                                   "never changed."
                                   % (T, lin(a, b, "t"), fmt(Rational(a, 2)),
                                      "+" if b >= 0 else "-", abs(b), T, s, d_rect),
                    "check": ["Eq(integrate(%d*t + %d, (t, 0, %d)), %d)" % (a, b, T, s)],
                })
    return raws


# ===========================================================================
# Vectors
# ===========================================================================

def _g_vec_combination():
    """Components of u + k v."""
    raws = []
    for (ux, uy) in ((2, 3), (1, -4), (-3, 2), (4, 1)):
        for (vx, vy) in ((1, 2), (3, -1), (-2, 3)):
            for k in (2, 3, -2):
                rx, ry = ux + k * vx, uy + k * vy
                raws.append({
                    "statement": "Let $\\mathbf{u} = %s$ and $\\mathbf{v} = %s$. Find "
                                 "the components of $\\mathbf{u} %s %d\\mathbf{v}$."
                                 % ("$".join(["", pt(ux, uy), ""]).strip("$") if False else "(%d,\\ %d)" % (ux, uy),
                                    "(%d,\\ %d)" % (vx, vy), "+" if k > 0 else "-", abs(k)),
                    "correct": "$%s$" % pt(rx, ry),
                    # subtracted instead · forgot the scalar · scaled u too
                    "dvals": ["$%s$" % pt(ux - k * vx, uy - k * vy),
                              "$%s$" % pt(ux + vx, uy + vy),
                              "$%s$" % pt(k * (ux + vx), k * (uy + vy))],
                    "explanation": "Scale first, then add componentwise: "
                                   "$%d\\mathbf{v} = (%d,\\ %d)$, so the result is "
                                   "$(%d %s %d,\\ %d %s %d) = (%d,\\ %d)$."
                                   % (k, k * vx, k * vy, ux, "+" if k * vx >= 0 else "-",
                                      abs(k * vx), uy, "+" if k * vy >= 0 else "-",
                                      abs(k * vy), rx, ry),
                    "check": ["Eq(%d + %d*%d, %d)" % (ux, k, vx, rx),
                              "Eq(%d + %d*%d, %d)" % (uy, k, vy, ry)],
                })
    return raws


_VEC2 = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15),
         (7, 24, 25), (20, 21, 29), (12, 16, 20), (10, 24, 26)]


def _g_vec_magnitude_2d():
    """Magnitude of a displacement vector."""
    raws = []
    for (x, y, m) in _VEC2:
        for (sx, sy) in ((1, 1), (-1, 1), (1, -1)):
            a, b = sx * x, sy * y
            raws.append({
                "statement": "A hiker walks $%d$ km east and then $%d$ km %s. The "
                             "displacement vector is $(%d,\\ %d)$. What is its "
                             "magnitude, in km?"
                             % (abs(a), abs(b), "north" if b > 0 else "south", a, b)
                             if a > 0 else
                             "A hiker walks $%d$ km west and then $%d$ km %s. The "
                             "displacement vector is $(%d,\\ %d)$. What is its "
                             "magnitude, in km?"
                             % (abs(a), abs(b), "north" if b > 0 else "south", a, b),
                "correct": m,
                # forgot the square root · added the legs · took the longer leg
                "dvals": [m * m, abs(a) + abs(b), max(abs(a), abs(b))],
                "explanation": "Magnitude is the hypotenuse: $\\sqrt{%d^2 + %d^2} = "
                               "\\sqrt{%d} = %d$ km. Walking $%d$ km of path is not "
                               "being $%d$ km from the start — displacement cuts the "
                               "corner."
                               % (a, b, m * m, m, abs(a) + abs(b), abs(a) + abs(b)),
                "check": ["Eq(sqrt((%d)**2 + (%d)**2), %d)" % (a, b, m)],
            })
    return raws


def _g_vec_perpendicular():
    """Which vector is perpendicular to u?"""
    raws = []
    pairs = [(2, 3), (1, 4), (3, 5), (2, 5), (4, 3), (1, 2), (3, 2), (5, 2),
             (-2, 3), (2, -3), (-1, 4), (-3, 5), (4, -3), (-1, 2), (5, -2),
             (1, 3), (2, 7), (3, 7), (6, 5), (-4, 5), (3, -4), (1, 5), (7, 2),
             (-2, 5), (5, 4), (2, 9)]
    for (a, b) in pairs:
        for k in (1,):
            perp = (-k * b, k * a)
            wrongs = [(b, a), (a, -b), (-a, -b)]
            # all three must genuinely fail the dot-product test
            if any(a * wx + b * wy == 0 for (wx, wy) in wrongs):
                continue
            raws.append({
                "statement": "Which of the following vectors is perpendicular to "
                             "$\\mathbf{u} = (%d,\\ %d)$?" % (a, b),
                "correct": "$%s$" % pt(*perp),
                # swapped without a sign flip · flipped the wrong component ·
                # the opposite vector (parallel, not perpendicular)
                "dvals": ["$%s$" % pt(*w) for w in wrongs],
                "explanation": "Perpendicular means dot product zero: "
                               "$(%d)(%d) + (%d)(%d) = 0$ ✓. The recipe is swap the "
                               "components AND flip one sign — $(%d,\\ %d)$ swaps "
                               "without flipping, and its dot product is $%d$, not $0$."
                               % (a, perp[0], b, perp[1], b, a, a * b + b * a),
                "check": ["Eq(%d*(%d) + %d*(%d), 0)" % (a, perp[0], b, perp[1])] +
                         ["Ne(%d*(%d) + %d*(%d), 0)" % (a, wx, b, wy) for (wx, wy) in wrongs],
            })
    return raws


# ===========================================================================
# Conic Sections
# ===========================================================================

def _g_circle_center():
    """Center and radius from (x-h)^2 + (y-k)^2 = r^2."""
    raws = []
    for h in (2, 3, -1, -4, 5):
        for k in (1, -2, 4, -3):
            if h == k or h == -k:
                continue
            for r in (2, 3, 5, 6):
                raws.append({
                    "statement": "What are the center and radius of the circle "
                                 "$(x %s %d)^2 + (y %s %d)^2 = %d$?"
                                 % ("-" if h > 0 else "+", abs(h),
                                    "-" if k > 0 else "+", abs(k), r * r),
                    "correct": "center $%s$, radius $%d$" % (pt(h, k), r),
                    # signs read off directly · radius left squared · center
                    # coordinates swapped
                    "dvals": ["center $%s$, radius $%d$" % (pt(-h, -k), r),
                              "center $%s$, radius $%d$" % (pt(h, k), r * r),
                              "center $%s$, radius $%d$" % (pt(k, h), r)],
                    "explanation": "The template is $(x - h)^2 + (y - k)^2 = r^2$: the "
                                   "signs INSIDE are opposite the center, so the center "
                                   "is $%s$, and $r = \\sqrt{%d} = %d$ — the equation "
                                   "stores the radius squared."
                                   % (pt(h, k), r * r, r),
                    "check": ["Eq(((%d) - (%d))**2 + ((%d) - (%d))**2, 0)" % (h, h, k, k),
                              "Eq(sqrt(%d), %d)" % (r * r, r)],
                })
    return raws


def _g_parabola_focus():
    """Focus of y^2 = 4px and x^2 = 4py."""
    raws = []
    for p in (1, 2, 3, -1, -2, 4, -3, 5, 6, -4, 7, -5):
        raws.append({
            "statement": "Find the focus of the parabola $y^2 = %dx$." % (4 * p),
            "correct": "$%s$" % pt(p, 0),
            # wrong side · wrong axis · used 4p
            "dvals": ["$%s$" % pt(-p, 0), "$%s$" % pt(0, p), "$%s$" % pt(4 * p, 0)],
            "explanation": "$y^2 = 4px$ opens along the $x$-axis with focus $(p, 0)$: "
                           "here $4p = %d$, so $p = %d$ and the focus is $%s$. The "
                           "equation shows $4p$, not $p$ — divide before you plot."
                           % (4 * p, p, pt(p, 0)),
            "check": ["Eq(Rational(%d, 4), %d)" % (4 * p, p)],
        })
        raws.append({
            "statement": "Find the focus of the parabola $x^2 = %dy$." % (4 * p),
            "correct": "$%s$" % pt(0, p),
            "dvals": ["$%s$" % pt(0, -p), "$%s$" % pt(p, 0), "$%s$" % pt(0, 4 * p)],
            "explanation": "$x^2 = 4py$ opens along the $y$-axis with focus $(0, p)$: "
                           "here $p = %d$, so the focus is $%s$. Squaring $x$ means the "
                           "parabola opens up/down — the focus sits on the $y$-axis."
                           % (p, pt(0, p)),
            "check": ["Eq(Rational(%d, 4), %d)" % (4 * p, p)],
        })
    return raws


def _g_classify_conic():
    """Name the conic from A x^2 + B y^2 + ... = constant."""
    NAMES = ["circle", "ellipse", "hyperbola", "parabola"]
    raws = []
    cases = []
    for v in (4, 9, 16, 25, 36, 49, 64):
        cases.append((1, 1, v, "circle"))
    for (A, B) in ((4, 9), (9, 4), (1, 4), (25, 4), (9, 16), (4, 1), (16, 9)):
        cases.append((A, B, 36, "ellipse"))
    for (A, B) in ((1, -1), (4, -9), (-4, 9), (9, -4), (1, -4), (-1, 16)):
        cases.append((A, B, 36, "hyperbola"))
    for (A, B) in ((1, 0), (0, 1), (2, 0), (0, 3), (5, 0), (0, 2)):
        cases.append((A, B, 12, "parabola"))
    for (A, B, C, name) in cases:
        # parabola cases: the missing square shows up as a LINEAR term instead
        if name == "parabola":
            if A == 0:
                eq = "%sy^2 = %dx" % ("" if B == 1 else B, C)
            else:
                eq = "%sx^2 = %dy" % ("" if A == 1 else A, C)
        else:
            terms = []
            for (coef, var) in ((A, "x"), (B, "y")):
                if coef == 0:
                    continue
                mag = "" if abs(coef) == 1 else str(abs(coef))
                terms.append(("-" if coef < 0 else ("+" if terms else "")) +
                             (" " if terms else "") + "%s%s^2" % (mag, var))
            eq = " ".join(terms) + " = %d" % C
        checks = []
        if name == "circle":
            checks = ["Eq(%d, %d)" % (A, B), "%d > 0" % C]
        elif name == "ellipse":
            checks = ["%d > 0" % A, "%d > 0" % B, "Ne(%d, %d)" % (A, B)]
        elif name == "hyperbola":
            checks = ["%d < 0" % (A * B)]
        else:
            checks = ["Eq(%d, 0)" % (A * B), "Ne(%d, %d)" % (A, B)]
        dvals = [n for n in NAMES if n != name]
        why = {
            "circle": "equal positive coefficients on $x^2$ and $y^2$ make a circle",
            "ellipse": "both squares positive but with different coefficients make an ellipse",
            "hyperbola": "opposite signs on the two squares make a hyperbola",
            "parabola": "only ONE variable is squared, so it is a parabola",
        }[name]
        raws.append({
            "statement": "The graph of $%s$ is a:" % eq,
            "correct": name,
            "dvals": dvals,
            "explanation": "Look only at the squared terms: %s. Signs and symmetry of "
                           "the squares decide the family before any algebra." % why,
            "check": checks,
        })
    return raws


# ===========================================================================
# assembly
# ===========================================================================

def build():
    forms = [
        form("G12-TI1", "The Pythagorean identity", 1, TI,
             "cos from sin — magnitude from the identity, sign from the quadrant.",
             mk_num("G12-TI1", _g_pythagorean_identity())),
        form("G12-TI2", "Double angles", 2, TI,
             "sin 2θ = 2 sin θ cos θ, never 2 sin θ.", mk_num("G12-TI2", _g_double_angle())),
        form("G12-TI3", "Counting trig solutions", 3, TI,
             "Factor, then count each root on the unit circle.",
             mk_num("G12-TI3", _g_trig_equation_count())),
        form("G12-LC1", "Limits by substitution", 1, LC,
             "Continuous functions: the limit is the value.", mk_num("G12-LC1", _g_limit_substitution())),
        form("G12-LC2", "The 0/0 form", 2, LC,
             "Factor, cancel the hole, then substitute.", mk_num("G12-LC2", _g_limit_hole())),
        form("G12-LC3", "Limits at infinity", 3, LC,
             "Equal degrees: the leading coefficients' ratio.", mk_num("G12-LC3", _g_limit_infinity())),
        form("G12-DV1", "The power rule", 1, DV,
             "Multiply by the exponent, lower it by one.", mk_num("G12-DV1", _g_power_rule())),
        form("G12-DV2", "The chain rule", 2, DV,
             "Outer derivative times inner derivative.", mk_num("G12-DV2", _g_chain_rule())),
        form("G12-DV3", "The product rule", 3, DV,
             "u'v + uv' — not the product of derivatives.", mk_num("G12-DV3", _g_product_rule_12())),
        form("G12-AD1", "Tangent slopes", 1, AD,
             "The slope is f'(a), not f(a).", mk_num("G12-AD1", _g_tangent_slope())),
        form("G12-AD2", "Increasing intervals", 2, AD,
             "Increasing where f' > 0.", mk_txt("G12-AD2", _g_increasing_interval())),
        form("G12-AD3", "Optimization", 3, AD,
             "Fixed sum, maximum product: split evenly.", mk_num("G12-AD3", _g_optimize_product())),
        form("G12-IG1", "Antiderivatives", 1, IG,
             "Raise the power, divide by it, add C.", mk_txt("G12-IG1", _g_antiderivative())),
        form("G12-IG2", "Definite integrals", 2, IG,
             "Evaluate at both limits and subtract.", mk_num("G12-IG2", _g_definite_linear())),
        form("G12-IG3", "Integrals and motion", 3, IG,
             "Distance is the integral of speed.", mk_num("G12-IG3", _g_displacement())),
        form("G12-VC1", "Combining vectors", 1, VC,
             "Scale first, then add componentwise.", mk_txt("G12-VC1", _g_vec_combination())),
        form("G12-VC2", "Magnitude", 2, VC,
             "The hypotenuse of the component triangle.", mk_num("G12-VC2", _g_vec_magnitude_2d())),
        form("G12-VC3", "Perpendicular vectors", 3, VC,
             "Swap the components and flip one sign.", mk_txt("G12-VC3", _g_vec_perpendicular())),
        form("G12-CS1", "Circles from equations", 1, CS,
             "Center from the opposite signs, radius from the square root.",
             mk_txt("G12-CS1", _g_circle_center())),
        form("G12-CS2", "Parabola foci", 2, CS,
             "Read 4p, divide, and pick the right axis.", mk_txt("G12-CS2", _g_parabola_focus())),
        form("G12-CS3", "Classifying conics", 3, CS,
             "The squared terms' signs name the curve.", mk_txt("G12-CS3", _g_classify_conic())),
    ]
    return {
        # Slug "12" mirrors the course path /math/12 (see grade9.py).
        "slug": "12",
        "title": "Grade 12",
        "titleMn": "12-р анги",
        "blurb": "The High school band's exit level, drilled by topic — trig identities "
                 "and limits through calculus, vectors and conics. Level 3 sits at ЭЕШ "
                 "difficulty.",
        "units": UNITS,
        "forms": forms,
    }
