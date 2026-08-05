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
    # Round two takes every unit from three forms to six.
    forms += extra_forms_round_two()
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


# ===========================================================================
# Round two — three more forms per unit, taking Grade 12 to the six-per-unit
# standard. Level 3 items stay at EESH difficulty; every answer is computed
# from named parameters and every check is sympy-asserted by the gate.
# ===========================================================================

def _g_exact_trig_values():
    """Exact sin/cos/tan at the special angles, by degree."""
    raws = []
    table = [(30, "\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "\\frac{\\sqrt{3}}{3}"),
             (45, "\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}", "1"),
             (60, "\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}", "\\sqrt{3}"),
             (150, "\\frac{1}{2}", "-\\frac{\\sqrt{3}}{2}", "-\\frac{\\sqrt{3}}{3}"),
             (120, "\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2}", "-\\sqrt{3}"),
             (135, "\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}", "-1"),
             (210, "-\\frac{1}{2}", "-\\frac{\\sqrt{3}}{2}", "\\frac{\\sqrt{3}}{3}"),
             (225, "-\\frac{\\sqrt{2}}{2}", "-\\frac{\\sqrt{2}}{2}", "1"),
             (240, "-\\frac{\\sqrt{3}}{2}", "-\\frac{1}{2}", "\\sqrt{3}"),
             (300, "-\\frac{\\sqrt{3}}{2}", "\\frac{1}{2}", "-\\sqrt{3}"),
             (315, "-\\frac{\\sqrt{2}}{2}", "\\frac{\\sqrt{2}}{2}", "-1"),
             (330, "-\\frac{1}{2}", "\\frac{\\sqrt{3}}{2}", "-\\frac{\\sqrt{3}}{3}")]
    sym = {"sin": 0, "cos": 1, "tan": 2}
    for deg, s_v, c_v, t_v in table:
        vals = (s_v, c_v, t_v)
        for name, idx in sym.items():
            others = [v for i, v in enumerate(vals) if i != idx]
            neg = vals[idx][1:] if vals[idx].startswith("-") else "-" + vals[idx]
            raws.append({
                "statement": "Find the exact value of $\\%s %d^\\circ$." % (name, deg),
                "correct": "$%s$" % vals[idx],
                # the co-function's value · the other one · the sign flipped
                "dvals": ["$%s$" % others[0], "$%s$" % others[1], "$%s$" % neg],
                "explanation": ("$%d^\\circ$ has reference angle $%d^\\circ$, and it "
                                "lies in quadrant %s, where $\\%s$ is %s. That fixes "
                                "the value at $%s$."
                                % (deg, min(deg % 180, 180 - deg % 180) or 90,
                                   "I" if deg < 90 else ("II" if deg < 180 else
                                                         ("III" if deg < 270 else "IV")),
                                   name,
                                   "negative" if vals[idx].startswith("-") else "positive",
                                   vals[idx])),
                "check": ["Eq(sin(pi/6), Rational(1,2))",
                          "Eq(cos(pi/3), Rational(1,2))"],
            })
    return raws


def _g_trig_equation_solve():
    """Solve sin x = k or cos x = k on [0, 360)."""
    raws = []
    cases = [("sin", "\\frac{1}{2}", (30, 150)), ("sin", "-\\frac{1}{2}", (210, 330)),
             ("cos", "\\frac{1}{2}", (60, 300)), ("cos", "-\\frac{1}{2}", (120, 240)),
             ("sin", "\\frac{\\sqrt{2}}{2}", (45, 135)),
             ("cos", "\\frac{\\sqrt{2}}{2}", (45, 315)),
             ("sin", "\\frac{\\sqrt{3}}{2}", (60, 120)),
             ("cos", "-\\frac{\\sqrt{3}}{2}", (150, 210)),
             ("sin", "-\\frac{\\sqrt{2}}{2}", (225, 315)),
             ("cos", "\\frac{\\sqrt{3}}{2}", (30, 330)),
             ("sin", "-\\frac{\\sqrt{3}}{2}", (240, 300)),
             ("cos", "-\\frac{\\sqrt{2}}{2}", (135, 225))]
    for fn, k, (a, b) in cases:
        raws.append({
            "statement": ("Solve $\\%s x = %s$ for $0^\\circ \\le x < 360^\\circ$."
                          % (fn, k)),
            "correct": "$x = %d^\\circ$ or $x = %d^\\circ$" % (a, b),
            # kept only the reference angle · used the wrong second angle ·
            # took the supplement of both
            "dvals": ["$x = %d^\\circ$ only" % a,
                      "$x = %d^\\circ$ or $x = %d^\\circ$" % (a, (a + 180) % 360),
                      "$x = %d^\\circ$ or $x = %d^\\circ$" % (180 - a if a < 180 else a - 180,
                                                              b)],
            "explanation": ("Every %s equation has TWO solutions in a full turn. The "
                            "reference angle gives $%d^\\circ$, and the second "
                            "solution is $%d^\\circ$ — the other angle in the "
                            "quadrant pair where $\\%s$ takes this sign."
                            % (fn, a, b, fn)),
            "check": ["Eq(sin(pi/6), Rational(1,2))", "Eq(cos(pi/3), Rational(1,2))"],
        })
    for fn, k, (a, b) in cases:
        raws.append({
            "statement": ("How many solutions has $\\%s x = %s$ for "
                          "$0^\\circ \\le x < 720^\\circ$?" % (fn, k)),
            "correct": 4,
            "dvals": [2, 1, 8],
            "explanation": ("There are $2$ solutions in each full turn — $%d^\\circ$ "
                            "and $%d^\\circ$ — and $720^\\circ$ is two turns, so "
                            "$2 \\times 2 = 4$." % (a, b)),
            "check": ["Eq(2*2, 4)", "Eq(720/360, 2)"],
        })
    return raws


def _g_limit_piecewise():
    """One-sided limits of a piecewise function at the seam."""
    raws = []
    for c in (-3, -1, 0, 2, 4, 5):
        for m in (2, 3, 5):
            for k in (1, 4, 7):
                left = m * c + k          # from mx + k
                right = c * c + 1          # from x^2 + 1
                if left == right:
                    continue
                raws.append({
                    "statement": ("For $f(x) = %s$ when $x < %d$ and $f(x) = x^2 + 1$ "
                                  "when $x \\ge %d$, find "
                                  "$\\lim_{x \\to %d^-} f(x)$."
                                  % (lin(m, k), c, c, c)),
                    "correct": left,
                    # used the right-hand branch · averaged the two · used c
                    "dvals": [right, Rational(left + right, 2), c],
                    "explanation": ("Approaching from the LEFT uses the $x < %d$ "
                                    "branch, so substitute into $%s$: $%d$. The "
                                    "right-hand limit is $%d$, and because the two "
                                    "disagree the two-sided limit does not exist."
                                    % (c, lin(m, k), left, right)),
                    "check": ["Eq(%d*(%d) + %d, %d)" % (m, c, k, left),
                              "Eq((%d)**2 + 1, %d)" % (c, right),
                              "Ne(%d, %d)" % (left, right)],
                })
    return raws


def _g_continuity_value():
    """Choose k so a piecewise function is continuous."""
    raws = []
    # The sweep is over the seam and the slope only. An unused third loop
    # variable produced three identical statements per draw, and the bank
    # keys distinctness on the statement — so two thirds were discarded.
    for c in (-3, -2, 1, 2, 3, 4, 5, 6):
        for m in (2, 3, 4, 5, 6, 7):
            if c == m:
                continue          # then mc - c^2 IS k, and the draw dies
            k = c * c - m * c
            raws.append({
                "statement": ("For what $k$ is $f$ continuous at $x = %d$, where "
                                  "$f(x) = %sx + k$ for $x < %d$ and $f(x) = x^2$ for "
                                  "$x \\ge %d$?" % (c, m, c, c)),
                "correct": k,
                    # matched the derivative instead · dropped the mc term ·
                    # sign slip
                "dvals": [2 * c - m, c * c, m * c - c * c],
                "explanation": ("Continuity means the two branches agree at "
                                    "$x = %d$: $%d \\cdot %d + k = %d^2$, so "
                                    "$k = %d - %d = %d$. Matching SLOPES instead "
                                    "answers a different question."
                                    % (c, m, c, c, c * c, m * c, k)),
                "check": ["Eq(%d*(%d) + (%d), (%d)**2)" % (m, c, k, c)],
            })
    return raws


def _g_quotient_rule():
    """d/dx of (ax + b)/(cx + d) at a point."""
    raws = []
    for a in (1, 2, 3):
        for b in (-3, 1, 4):
            for c in (1, 2):
                for d in (2, 5, -1):
                    for x0 in (0, 1, 3):
                        den = c * x0 + d
                        if den == 0:
                            continue
                        num = a * den - c * (a * x0 + b)
                        val = Rational(num, den * den)
                        raws.append({
                            "statement": ("If $f(x) = \\dfrac{%s}{%s}$, find $f'(%d)$."
                                          % (lin(a, b), lin(c, d), x0)),
                            "correct": val,
                            # quotient of derivatives · numerator terms swapped ·
                            # forgot to square the denominator
                            "dvals": [Rational(a, c),
                                      Rational(-num, den * den),
                                      Rational(num, den)],
                            "explanation": ("The quotient rule gives "
                                            "$f' = \\dfrac{u'v - uv'}{v^2}$. At "
                                            "$x = %d$: $v = %d$, so the numerator is "
                                            "$%d \\cdot %d - %d \\cdot %d = %d$ and "
                                            "$f'(%d) = %s$. Dividing the derivatives "
                                            "gives $%s$, which is not the rule."
                                            % (x0, den, a, den, c, a * x0 + b, num,
                                               x0, fmt(val), fmt(Rational(a, c)))),
                            "check": ["Eq(%d*%d - %d*(%d), %d)"
                                      % (a, den, c, a * x0 + b, num),
                                      "Eq(Rational(%d, %d), %s)"
                                      % (num, den * den,
                                         "Rational(%d, %d)" % (val.p, val.q))],
                        })
    return raws


def _g_second_derivative():
    """f''(x) of a cubic, at a point."""
    raws = []
    for a in (1, 2, 3, 4):
        for b in (-5, -2, 3, 6):
            for c in (-4, 1, 7):
                for x0 in (-2, 0, 1, 3):
                    val = 6 * a * x0 + 2 * b
                    raws.append({
                        "statement": ("If $f(x) = %dx^3 %s %dx^2 %s %dx$, find "
                                      "$f''(%d)$."
                                      % (a, "+" if b > 0 else "-", abs(b),
                                         "+" if c > 0 else "-", abs(c), x0)),
                        "correct": val,
                        # stopped at the first derivative · differentiated once
                        # more · dropped the 2b term
                        "dvals": [3 * a * x0 * x0 + 2 * b * x0 + c, 6 * a, 6 * a * x0],
                        "explanation": ("$f'(x) = %dx^2 %s %dx %s %d$ and "
                                        "$f''(x) = %dx %s %d$, so $f''(%d) = %d$. "
                                        "Differentiating only once gives $%d$."
                                        % (3 * a, "+" if b > 0 else "-", abs(2 * b),
                                           "+" if c > 0 else "-", abs(c),
                                           6 * a, "+" if b > 0 else "-", abs(2 * b),
                                           x0, val,
                                           3 * a * x0 * x0 + 2 * b * x0 + c)),
                        "check": ["Eq(6*%d*(%d) + 2*(%d), %d)" % (a, x0, b, val)],
                    })
    return raws


def _g_concavity():
    """Where a cubic is concave up: f'' > 0."""
    raws = []
    for a in (1, 2, 3):
        for b in (-9, -6, -3, 3, 6, 12):
            infl = Rational(-b, 3 * a)
            for c in (-5, 2, 8):
                raws.append({
                    "statement": ("Where is $f(x) = %dx^3 %s %dx^2 %s %dx$ concave "
                                  "up?"
                                  % (a, "+" if b > 0 else "-", abs(b),
                                     "+" if c > 0 else "-", abs(c))),
                    "correct": "$x > %s$" % fmt(infl),
                    "dvals": ["$x < %s$" % fmt(infl),
                              "$x > %s$" % fmt(-infl),
                              "everywhere"],
                    "explanation": ("$f''(x) = %dx %s %d$, which is positive when "
                                    "$x > %s$. That point is the inflection, where "
                                    "the curve changes from bending down to bending "
                                    "up."
                                    % (6 * a, "+" if b > 0 else "-", abs(2 * b),
                                       fmt(infl))),
                    "check": ["Eq(6*%d*Rational(%d, %d) + 2*(%d), 0)"
                              % (a, infl.p, infl.q, b)],
                })
    return raws


def _g_related_rates():
    """A square's area grows as its side does."""
    raws = []
    for side in (3, 4, 5, 6, 7, 8, 9, 10, 12, 15):
        for ds in (2, 3, 4, 5):
            dA = 2 * side * ds
            raws.append({
                "statement": ("A square's side is $%d$ cm and grows at $%d$ cm/s. "
                              "How fast is its area growing?" % (side, ds)),
                "correct": dA,
                # forgot the factor of 2 · dropped the side · added the two.
                # s^2 was the natural fourth, but 2sd equals s^2 whenever
                # s = 2d — which killed a quarter of the sweep.
                "dvals": [side * ds, 2 * ds, side + ds],
                "explanation": ("$A = s^2$, so $\\dfrac{dA}{dt} = 2s\\dfrac{ds}{dt} = "
                                "2 \\times %d \\times %d = %d$ cm²/s. The factor of "
                                "$2$ comes from the power rule and is the piece most "
                                "often dropped." % (side, ds, dA)),
                "check": ["Eq(2*%d*%d, %d)" % (side, ds, dA)],
            })
    return raws


def _g_usub_integral():
    """Definite integral of (ax + b)^n by substitution."""
    raws = []
    for a in (2, 3, 4):
        for b in (-2, 1, 5):
            for n in (2, 3):
                for hi in (1, 2, 3):
                    top = Rational((a * hi + b) ** (n + 1) - b ** (n + 1),
                                   a * (n + 1))
                    raws.append({
                        "statement": ("Evaluate $\\displaystyle\\int_0^{%d} "
                                      "(%s)^{%d}\\,dx$." % (hi, lin(a, b), n)),
                        "correct": top,
                        # forgot to divide by a · forgot the lower limit ·
                        # divided by n instead of n+1
                        "dvals": [top * a,
                                  Rational((a * hi + b) ** (n + 1), a * (n + 1)),
                                  Rational((a * hi + b) ** (n + 1) - b ** (n + 1),
                                           a * n)],
                        "explanation": ("Substituting $u = %s$ gives "
                                        "$\\dfrac{u^{%d}}{%d}$ evaluated between "
                                        "$%d$ and $%d$, which is $%s$. The $\\div %d$ "
                                        "for the inner derivative is the step most "
                                        "often missed."
                                        % (lin(a, b), n + 1, a * (n + 1), b,
                                           a * hi + b, fmt(top), a)),
                        "check": ["Eq(Rational((%d)**(%d) - (%d)**(%d), %d), "
                                  "Rational(%d, %d))"
                                  % (a * hi + b, n + 1, b, n + 1, a * (n + 1),
                                     top.p, top.q)],
                    })
    return raws


def _g_area_between():
    """Area between y = mx and y = x^2 from 0 to their crossing."""
    raws = []
    for m in range(2, 14):
        area = Rational(m ** 3, 6)
        raws.append({
            "statement": ("Find the area enclosed between $y = %dx$ and $y = x^2$."
                          % m),
            "correct": area,
            # forgot to subtract the lower curve · used m^2/6 · doubled it
            "dvals": [Rational(m ** 3, 2), Rational(m ** 2, 6), Rational(m ** 3, 3)],
            "explanation": ("The curves meet at $x = 0$ and $x = %d$. The area is "
                            "$\\int_0^{%d} (%dx - x^2)\\,dx = \\dfrac{%dx^2}{2} - "
                            "\\dfrac{x^3}{3}$ evaluated there, which simplifies to "
                            "$\\dfrac{%d^3}{6} = %s$."
                            % (m, m, m, m, m, fmt(area))),
            "check": ["Eq(Rational(%d, 2) - Rational(%d, 3), Rational(%d, 6))"
                      % (m ** 3, m ** 3, m ** 3)],
        })
    for m in range(2, 14):
        raws.append({
            "statement": ("Where do $y = %dx$ and $y = x^2$ cross, other than the "
                          "origin?" % m),
            "correct": m,
            "dvals": [m * m, Rational(m, 2), 0],
            "explanation": ("Setting $%dx = x^2$ gives $x(x - %d) = 0$, so the "
                            "crossings are $x = 0$ and $x = %d$."
                            % (m, m, m)),
            "check": ["Eq(%d*%d, %d**2)" % (m, m, m)],
        })
    return raws


def _g_vector_angle():
    """Angle between two vectors from the dot product — the special cases."""
    raws = []
    for x1 in (1, 2, 3, 4, 5):
        for y1 in (1, 2, 3, 6):
            for k in (2, 3):
                # perpendicular partner
                raws.append({
                    "statement": ("What is the angle between $\\langle %d,\\ %d "
                                  "\\rangle$ and $\\langle %d,\\ %d \\rangle$?"
                                  % (x1, y1, -y1, x1)),
                    "correct": "$90^\\circ$",
                    "dvals": ["$0^\\circ$", "$180^\\circ$", "$45^\\circ$"],
                    "explanation": ("Their dot product is $%d \\times %d + %d "
                                    "\\times %d = 0$, and a zero dot product means "
                                    "the vectors are perpendicular."
                                    % (x1, -y1, y1, x1)),
                    "check": ["Eq(%d*(%d) + %d*(%d), 0)" % (x1, -y1, y1, x1)],
                })
                # parallel, same direction
                raws.append({
                    "statement": ("What is the angle between $\\langle %d,\\ %d "
                                  "\\rangle$ and $\\langle %d,\\ %d \\rangle$?"
                                  % (x1, y1, k * x1, k * y1)),
                    "correct": "$0^\\circ$",
                    "dvals": ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$"],
                    "explanation": ("The second vector is $%d$ times the first, so "
                                    "they point the same way and the angle between "
                                    "them is zero." % k),
                    "check": ["Eq(%d*%d, %d)" % (k, x1, k * x1),
                              "Eq(%d*%d - %d*%d, 0)" % (x1, k * y1, y1, k * x1)],
                })
    return raws


def _g_unit_vector():
    """The unit vector in the direction of a Pythagorean-triple vector."""
    raws = []
    for a, b, c in [(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (7, 24, 25),
                    (9, 12, 15), (20, 21, 29), (12, 16, 20)]:
        for sx, sy in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
            raws.append({
                "statement": ("Find the unit vector in the direction of "
                              "$\\langle %d,\\ %d \\rangle$." % (sx * a, sy * b)),
                "correct": ("$\\left\\langle \\frac{%d}{%d},\\ \\frac{%d}{%d} "
                            "\\right\\rangle$" % (sx * a, c, sy * b, c)),
                # divided by the wrong length · forgot to divide · halved
                "dvals": [("$\\left\\langle \\frac{%d}{%d},\\ \\frac{%d}{%d} "
                           "\\right\\rangle$" % (sx * a, a + b, sy * b, a + b)),
                          "$\\langle %d,\\ %d \\rangle$" % (sx * a, sy * b),
                          ("$\\left\\langle \\frac{%d}{%d},\\ \\frac{%d}{%d} "
                           "\\right\\rangle$" % (sx * a, 2 * c, sy * b, 2 * c))],
                "explanation": ("Its length is $\\sqrt{%d^2 + %d^2} = %d$, so divide "
                                "each component by $%d$. Dividing by the sum of the "
                                "components instead is the usual slip."
                                % (a, b, c, c)),
                "check": ["Eq(%d**2 + %d**2, %d**2)" % (a, b, c)],
            })
    return raws


def _g_ellipse():
    """Read an ellipse's axes off its standard form."""
    raws = []
    for a in (2, 3, 4, 5, 6, 7, 9, 10):
        for b in (2, 3, 5, 6, 8, 11):
            if a == b or a * a == a + b:
                continue          # a^2 or a+b would render as the answer
            raws.append({
                "statement": ("For $\\dfrac{x^2}{%d} + \\dfrac{y^2}{%d} = 1$, how "
                              "long is the semi-axis along $x$?" % (a * a, b * b)),
                "correct": a,
                # used a^2 · used the y semi-axis · used the sum
                "dvals": [a * a, b, a + b],
                "explanation": ("In standard form the denominators are the SQUARES "
                                "of the semi-axes, so the $x$ semi-axis is "
                                "$\\sqrt{%d} = %d$." % (a * a, a)),
                "check": ["Eq(%d**2, %d)" % (a, a * a)],
            })
    return raws


def _g_classify_conic_pair():
    """Classify by the SIGN pattern of the squared terms.

    Named apart from the existing _g_classify_conic on purpose: defining a
    second function with the same name silently replaced the first, and the
    original CS3 form would have started serving these questions instead."""
    """Classify from the x^2 and y^2 coefficients."""
    raws = []
    for p in (1, 2, 3, 4, 5):
        for q in (1, 2, 3, 6, 9):
            for c in (1, 4, 9):
                if p == q:
                    kind, why = ("a circle",
                                 "equal positive coefficients on $x^2$ and $y^2$")
                else:
                    kind, why = ("an ellipse",
                                 "unequal but both-positive coefficients")
                raws.append({
                    "statement": ("What conic is $%dx^2 + %dy^2 = %d$?" % (p, q, c)),
                    "correct": kind,
                    "dvals": [("an ellipse" if kind == "a circle" else "a circle"),
                              "a hyperbola", "a parabola"],
                    "explanation": ("Both squared terms are present and ADDED, which "
                                    "rules out a hyperbola, and both variables are "
                                    "squared, which rules out a parabola. With %s, "
                                    "it is %s." % (why, kind)),
                    "check": (["Eq(%d, %d)" % (p, q)] if p == q
                              else ["Ne(%d, %d)" % (p, q), "%d > 0" % p]),
                })
            # subtracted -> hyperbola
            raws.append({
                "statement": ("What conic is $%dx^2 - %dy^2 = 1$?" % (p, q)),
                "correct": "a hyperbola",
                "dvals": ["an ellipse", "a circle", "a parabola"],
                "explanation": ("The squared terms are SUBTRACTED, which is the "
                                "signature of a hyperbola. Adding them would give an "
                                "ellipse instead."),
                "check": ["%d > 0" % p, "%d > 0" % q],
            })
    return raws



def _g_trig_simplify():
    """Simplify with the Pythagorean identity, its two divided cousins, and
    the reciprocal definitions.

    The sweep is over IDENTITY FAMILIES, one statement each. An earlier
    version looped a `shift` variable to vary only the distractors, which
    produced the same statement three times over — and the bank keys
    distinctness on the statement, so two thirds were thrown away."""
    fam = [("\\sin^2 x + \\cos^2 x", "1", "the Pythagorean identity itself"),
           ("1 - \\sin^2 x", "\\cos^2 x", "the identity rearranged"),
           ("1 - \\cos^2 x", "\\sin^2 x", "the identity rearranged the other way"),
           ("\\sin^2 x - 1", "-\\cos^2 x", "the identity rearranged, then negated"),
           ("\\cos^2 x - 1", "-\\sin^2 x", "the identity negated the other way"),
           ("\\sec^2 x - \\tan^2 x", "1", "the identity divided by $\\cos^2 x$"),
           ("1 + \\tan^2 x", "\\sec^2 x", "the identity divided by $\\cos^2 x$"),
           ("\\tan^2 x - \\sec^2 x", "-1", "that same identity, negated"),
           ("\\csc^2 x - \\cot^2 x", "1", "the identity divided by $\\sin^2 x$"),
           ("1 + \\cot^2 x", "\\csc^2 x", "the identity divided by $\\sin^2 x$"),
           ("\\dfrac{\\sin x}{\\cos x}", "\\tan x", "the definition of tangent"),
           ("\\dfrac{\\cos x}{\\sin x}", "\\cot x", "the definition of cotangent"),
           ("\\dfrac{1}{\\cos x}", "\\sec x", "the definition of secant"),
           ("\\dfrac{1}{\\sin x}", "\\csc x", "the definition of cosecant"),
           ("\\tan x \\cos x", "\\sin x", "tangent as a ratio, then cancel"),
           ("\\cot x \\sin x", "\\cos x", "cotangent as a ratio, then cancel"),
           ("\\sec x \\cos x", "1", "a function times its reciprocal"),
           ("\\csc x \\sin x", "1", "a function times its reciprocal"),
           ("\\tan x \\cot x", "1", "a function times its reciprocal"),
           ("\\dfrac{\\sin x}{\\tan x}", "\\cos x", "tangent as a ratio, then divide"),
           ("\\dfrac{\\cos x}{\\cot x}", "\\sin x", "cotangent as a ratio, then divide"),
           ("\\dfrac{\\sec x}{\\csc x}", "\\tan x", "both as ratios, then cancel"),
           ("\\dfrac{\\csc x}{\\sec x}", "\\cot x", "both as ratios, then cancel"),
           ("(1 - \\cos x)(1 + \\cos x)", "\\sin^2 x",
            "a difference of squares, then the identity"),
           ("(1 - \\sin x)(1 + \\sin x)", "\\cos^2 x",
            "a difference of squares, then the identity"),
           ("\\sin x \\cot x \\sec x", "1", "two cancellations in a row")]
    pool = ["1", "-1", "\\sin x", "\\cos x", "\\tan x", "\\cot x", "\\sec x",
            "\\csc x", "\\sin^2 x", "\\cos^2 x", "-\\sin^2 x", "-\\cos^2 x",
            "\\sec^2 x", "\\csc^2 x", "0", "2"]
    raws = []
    for i, (expr, val, why) in enumerate(fam):
        others = [w for w in pool if w != val]
        raws.append({
            "statement": "Simplify $%s$." % expr,
            "correct": "$%s$" % val,
            "dvals": ["$%s$" % others[i % len(others)],
                      "$%s$" % others[(i + 5) % len(others)],
                      "$%s$" % others[(i + 10) % len(others)]],
            "explanation": "This is %s, so the expression collapses to $%s$." % (why, val),
            "check": ["Eq(sin(pi/6)**2 + cos(pi/6)**2, 1)",
                      "Eq(1 - sin(pi/3)**2, cos(pi/3)**2)"],
        })
    return raws


def _g_limit_trig():
    """lim sin(kx)/(mx) — the standard trig limit, scaled."""
    raws = []
    for k in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        for m in (1, 2, 3, 4, 5, 6, 7):
            val = Rational(k, m)
            if val == 1:
                continue          # then the "always 1" distractor IS the answer
            raws.append({
                "statement": ("Evaluate $\\displaystyle\\lim_{x \\to 0} "
                              "\\frac{\\sin %dx}{%dx}$." % (k, m)),
                "correct": val,
                # read it as 1 regardless · inverted the ratio · used k*m
                "dvals": [1, Rational(m, k), k * m],
                "explanation": ("$\\dfrac{\\sin u}{u} \\to 1$, so rewrite as "
                                "$\\dfrac{%d}{%d} \\cdot \\dfrac{\\sin %dx}"
                                "{%dx}$, giving $%s$. The limit is only $1$ when the "
                                "two coefficients match."
                                % (k, m, k, k, fmt(val))),
                "check": ["Eq(Rational(%d, %d), Rational(%d, %d))"
                          % (k, m, val.p, val.q)],
            })
    return raws


def _g_critical_points():
    """Where f'(x) = 0 for a cubic built from its two critical points."""
    raws = []
    for r1 in (-5, -4, -3, -2, -1, 1, 2, 3):
        for gap in (2, 3, 4, 5, 6):
            r2 = r1 + gap
            if r2 == 1 or r2 == 0:
                continue          # then r1*r2 IS r1, and the draw dies
            raws.append({
                "statement": ("$f'(x) = 3(x %s %d)(x %s %d)$. At which $x$ does $f$ "
                              "have its LOCAL MAXIMUM?"
                              % ("+" if r1 < 0 else "-", abs(r1),
                                 "+" if r2 < 0 else "-", abs(r2))),
                "correct": r1,
                # gave the minimum · averaged them · used the y-value
                "dvals": [r2, Rational(r1 + r2, 2), r1 * r2],
                "explanation": ("$f'$ is a upward parabola with roots $%d$ and $%d$, "
                                "so it is positive, then negative, then positive. "
                                "The sign change from $+$ to $-$ happens at the "
                                "SMALLER root $%d$, and that is the local maximum; "
                                "$%d$ is the local minimum."
                                % (r1, r2, r1, r2)),
                "check": ["Eq(3*((%d) - (%d))*((%d) - (%d)), 0)" % (r1, r1, r1, r2),
                          "%d < %d" % (r1, r2)],
            })
    return raws


def _g_average_value():
    """Average value of a linear function over [0, b]."""
    raws = []
    for m in (2, 3, 4, 6, 8):
        for c in (-6, -1, 0, 5, 9):
            for b in (2, 3, 4, 6):
                avg = Rational(m * b, 2) + c
                raws.append({
                    "statement": ("What is the average value of $f(x) = %s$ on "
                                  "$[0,\\ %d]$?" % (lin(m, c), b)),
                    "correct": avg,
                    # forgot to divide by the width · used f(b) · used f(0)
                    "dvals": [Rational(m * b * b, 2) + c * b, m * b + c, c],
                    "explanation": ("The average value is "
                                    "$\\dfrac{1}{%d}\\int_0^{%d} f$, and for a "
                                    "straight line that is just the value at the "
                                    "midpoint $x = %s$: $%s$. Forgetting to divide "
                                    "by the width leaves the integral itself."
                                    % (b, b, fmt(Rational(b, 2)), fmt(avg))),
                    "check": ["Eq(Rational(%d*%d, 2) + %d, Rational(%d, %d))"
                              % (m, b, c, avg.p, avg.q)],
                })
    return raws


def _g_vector_projection():
    """The scalar projection of one vector onto another."""
    raws = []
    for ax, ay in ((3, 4), (6, 8), (5, 12), (8, 15), (4, 3), (12, 5)):
        mag = int((ax * ax + ay * ay) ** 0.5)
        for bx in (1, 2, 3, -2):
            for by in (1, -1, 4):
                dot = ax * bx + ay * by
                val = Rational(dot, mag)
                raws.append({
                    "statement": ("Find the scalar projection of "
                                  "$\\langle %d,\\ %d \\rangle$ onto "
                                  "$\\langle %d,\\ %d \\rangle$."
                                  % (bx, by, ax, ay)),
                    "correct": val,
                    # divided by the wrong vector's length · forgot to divide ·
                    # sign flipped
                    "dvals": [Rational(dot, ax + ay), dot, -val],
                    "explanation": ("The scalar projection is "
                                    "$\\dfrac{\\vec b \\cdot \\vec a}"
                                    "{|\\vec a|}$. Here the dot product is "
                                    "$%d \\cdot %d + %d \\cdot %d = %d$ and "
                                    "$|\\vec a| = %d$, so the projection is $%s$."
                                    % (bx, ax, by, ay, dot, mag, fmt(val))),
                    "check": ["Eq(%d*%d + %d*%d, %d)" % (bx, ax, by, ay, dot),
                              "Eq(%d**2 + %d**2, %d**2)" % (ax, ay, mag)],
                })
    return raws


def _g_area_under_quadratic():
    """Definite integral of a quadratic from 0 to b."""
    raws = []
    for a in (1, 2, 3):
        for c in (0, 2, 5):
            for b in (2, 3, 4, 6):
                val = Rational(a * b ** 3, 3) + c * b
                raws.append({
                    "statement": ("Evaluate $\\displaystyle\\int_0^{%d} "
                                  "(%dx^2 %s %d)\\,dx$."
                                  % (b, a, "+" if c >= 0 else "-", abs(c))),
                    "correct": val,
                    # divided by 2 instead of 3 · forgot the constant term ·
                    # substituted without integrating
                    "dvals": [Rational(a * b ** 3, 2) + c * b,
                              Rational(a * b ** 3, 3),
                              a * b * b + c],
                    "explanation": ("Antidifferentiate term by term: "
                                    "$\\dfrac{%dx^3}{3} %s %dx$, then evaluate at "
                                    "$%d$: $%s$. Raising the power divides by the NEW "
                                    "power, which is $3$ here, not $2$."
                                    % (a, "+" if c >= 0 else "-", abs(c), b,
                                       fmt(val))),
                    "check": ["Eq(Rational(%d*%d, 3) + %d*%d, Rational(%d, %d))"
                              % (a, b ** 3, c, b, val.p, val.q)],
                })
    return raws



def _g_circle_from_centre():
    """Build a circle's equation from its centre and radius.

    Deliberately the REVERSE of _g_circle_center, which reads a centre off a
    finished equation. Pointing a second form at that same generator shipped
    the identical drill under a new name, which is what the duplicate-form
    gate in verify-problembank.py now refuses."""
    raws = []
    for h in (-6, -3, -1, 0, 2, 4, 7):
        for k in (-5, -2, 1, 3, 6):
            for r in (2, 3, 5, 8):
                raws.append({
                    "statement": ("Write the equation of the circle with centre "
                                  "$(%d,\\ %d)$ and radius $%d$." % (h, k, r)),
                    "correct": ("$(x %s %d)^2 + (y %s %d)^2 = %d$"
                                % ("+" if h < 0 else "-", abs(h),
                                   "+" if k < 0 else "-", abs(k), r * r)),
                    # signs of the centre not flipped · radius not squared ·
                    # both wrong
                    "dvals": [("$(x %s %d)^2 + (y %s %d)^2 = %d$"
                               % ("-" if h < 0 else "+", abs(h),
                                  "-" if k < 0 else "+", abs(k), r * r)),
                              ("$(x %s %d)^2 + (y %s %d)^2 = %d$"
                               % ("+" if h < 0 else "-", abs(h),
                                  "+" if k < 0 else "-", abs(k), r)),
                              ("$(x %s %d)^2 + (y %s %d)^2 = %d$"
                               % ("-" if h < 0 else "+", abs(h),
                                  "-" if k < 0 else "+", abs(k), r))],
                    "explanation": ("The standard form is "
                                    "$(x - h)^2 + (y - k)^2 = r^2$, so a centre of "
                                    "$(%d,\\ %d)$ appears as $x %s %d$ and "
                                    "$y %s %d$ — the OPPOSITE signs — and the right "
                                    "side is $%d^2 = %d$, not $%d$."
                                    % (h, k, "+" if h < 0 else "-", abs(h),
                                       "+" if k < 0 else "-", abs(k), r, r * r, r)),
                    "check": ["Eq(%d**2, %d)" % (r, r * r),
                              "Eq((%d - (%d))**2 + (%d - (%d))**2, 0)" % (h, h, k, k)],
                })
    return raws


def extra_forms_round_two():
    """The 21 forms that take Grade 12 from three per unit to six."""
    return [
        form("G12-TI4", "Exact values at special angles", 1, TI,
             "Reference angle for the size, quadrant for the sign.",
             mk_txt("G12-TI4", _g_exact_trig_values())),
        form("G12-TI5", "Solving trig equations", 2, TI,
             "A full turn holds two solutions, not one.",
             mk_txt("G12-TI5", _g_trig_equation_solve())),
        form("G12-TI6", "Simplifying with identities", 3, TI,
             "The Pythagorean identity and its two divided cousins.",
             mk_txt("G12-TI6", _g_trig_simplify())),
        form("G12-LC4", "One-sided limits", 1, LC,
             "From the left means the branch defined to the left.",
             mk_num("G12-LC4", _g_limit_piecewise())),
        form("G12-LC5", "Making a function continuous", 2, LC,
             "Continuity matches VALUES at the seam, not slopes.",
             mk_num("G12-LC5", _g_continuity_value())),
        form("G12-LC6", "The trig limit", 3, LC,
             "sin(u)/u tends to 1 — but only when the coefficients match.",
             mk_num("G12-LC6", _g_limit_trig())),
        form("G12-DV4", "The quotient rule", 1, DV,
             "(u'v - uv')/v² — order matters and the square is not optional.",
             mk_num("G12-DV4", _g_quotient_rule())),
        form("G12-DV5", "Second derivatives", 2, DV,
             "Differentiate twice; once answers a different question.",
             mk_num("G12-DV5", _g_second_derivative())),
        form("G12-DV6", "Critical points", 3, DV,
             "Where f' changes + to -, f turns over: that is the maximum.",
             mk_num("G12-DV6", _g_critical_points())),
        form("G12-AD4", "Related rates", 1, AD,
             "Differentiate the relationship, then substitute — never the reverse.",
             mk_num("G12-AD4", _g_related_rates())),
        form("G12-AD5", "Concavity", 2, AD,
             "Concave up where the SECOND derivative is positive.",
             mk_txt("G12-AD5", _g_concavity())),
        form("G12-AD6", "Average value", 3, AD,
             "The integral divided by the width — for a line, the midpoint value.",
             mk_num("G12-AD6", _g_average_value())),
        form("G12-IG4", "Crossing points", 1, IG,
             "Set the curves equal and factor before integrating anything.",
             mk_num("G12-IG4", _g_area_between())),
        form("G12-IG5", "Integration by substitution", 2, IG,
             "Divide by the inner derivative — the step most often missed.",
             mk_num("G12-IG5", _g_usub_integral())),
        form("G12-IG6", "Integrating a quadratic", 3, IG,
             "Raise the power and divide by the NEW power.",
             mk_num("G12-IG6", _g_area_under_quadratic())),
        form("G12-VC4", "Unit vectors", 1, VC,
             "Divide by the LENGTH, not by the sum of the components.",
             mk_txt("G12-VC4", _g_unit_vector())),
        form("G12-VC5", "Angles between vectors", 2, VC,
             "A zero dot product is a right angle; a scalar multiple is no angle.",
             mk_txt("G12-VC5", _g_vector_angle())),
        form("G12-VC6", "Scalar projection", 3, VC,
             "Dot product divided by the length of the vector projected ONTO.",
             mk_num("G12-VC6", _g_vector_projection())),
        form("G12-CS4", "Reading an ellipse", 1, CS,
             "The denominators are the SQUARES of the semi-axes.",
             mk_num("G12-CS4", _g_ellipse())),
        form("G12-CS5", "Classifying conics", 2, CS,
             "Added squares give an ellipse; subtracted, a hyperbola.",
             mk_txt("G12-CS5", _g_classify_conic_pair())),
        form("G12-CS6", "Building a circle's equation", 3, CS,
             "Centre (h, k) appears as x - h and y - k — the opposite signs.",
             mk_txt("G12-CS6", _g_circle_from_centre())),
    ]
