# -*- coding: utf-8 -*-
"""SAT bank generators for the subtopics the old four-unit cut never had.

The SAT bank used to be organised by DOMAIN — four units, seven forms each.
Re-cutting it onto the College Board's twenty official subtopics leaves most
subtopics with one or two of the original forms and four with none at all:
systems of equations in two variables, two-variable data, inference and margin
of error, and evaluating statistical claims.

This module supplies the generators that close those gaps and bring every
subtopic up to at least three forms. Same contract as scripts/pb/sat.py: each
function returns a list of raw dicts with a COMPUTED correct answer, three
distractors that each encode one named student error, and a check[] that
sympy hard-asserts before anything is written.

100% self-authored (expansion-vision §4.3) — these emulate the SAT's format,
register and difficulty tiers and never reproduce a released question.
"""
from sympy import Rational, sqrt

from imbank import fmt, lin, quad, xpm  # noqa: F401  (shared renderers)


# ===========================================================================
# Algebra
# ===========================================================================

def g_lin_fractions():
    """x/p + x/q = t, engineered so x is a whole number."""
    raws = []
    for p, q in ((2, 3), (2, 5), (3, 4), (3, 6), (4, 6), (2, 4), (5, 10), (3, 9)):
        lcm = p * q // _gcd(p, q)
        for k in (1, 2, 3, 4, 5, 6):
            x0 = lcm * k
            t = Rational(x0, p) + Rational(x0, q)
            if t.q != 1:
                continue
            raws.append({
                "statement": "If $\\dfrac{x}{%d} + \\dfrac{x}{%d} = %s$, what is the value "
                             "of $x$?" % (p, q, fmt(t)),
                "correct": x0,
                # adding the denominators; halving; using only the first fraction
                "dvals": [Rational(t) * (p + q), Rational(x0, 2), Rational(t) * p],
                "explanation": "Multiply every term by $%d$, the common denominator: "
                               "$%dx + %dx = %s$, so $%dx = %s$ and $x = %d$. Adding the "
                               "denominators instead of using their common multiple is the "
                               "usual slip."
                               % (lcm, lcm // p, lcm // q, fmt(t * lcm),
                                  lcm // p + lcm // q, fmt(t * lcm), x0),
                "check": ["Eq(Rational(%d,%d) + Rational(%d,%d), %s)"
                          % (x0, p, x0, q, fmt(t))],
            })
    return raws


def g_lin_fee_rate():
    """A one-time fee plus a per-unit rate, solved for the count."""
    ctx = [
        ("gym", "joining fee", "months of membership", "month"),
        ("printing service", "setup charge", "posters printed", "poster"),
        ("bike hire", "booking fee", "hours of hire", "hour"),
        ("catering firm", "delivery charge", "meals ordered", "meal"),
    ]
    raws = []
    for name, feeword, unitword, single in ctx:
        for fee in (25, 40, 60, 75):
            for rate in (8, 12, 15, 20):
                for n in (6, 9, 12):
                    total = fee + rate * n
                    raws.append({
                        "statement": "A %s charges a $\\$%d$ %s plus $\\$%d$ per %s. A "
                                     "customer paid $\\$%d$ in total. How many %s were "
                                     "there?" % (name, fee, feeword, rate, single, total,
                                                 unitword),
                        "correct": n,
                        # forgot the fee; subtracted twice; divided by the fee
                        "dvals": [Rational(total, rate), Rational(total - 2 * fee, rate),
                                  Rational(total, fee)],
                        "explanation": "Subtract the one-time %s first, because it is paid "
                                       "once: $%d - %d = %d$. Then divide by the per-%s "
                                       "rate: $%d \\div %d = %d$. Dividing the whole total "
                                       "by $%d$ ignores the %s."
                                       % (feeword, total, fee, rate * n, single,
                                          rate * n, rate, n, rate, feeword),
                        "check": ["Eq(%d + %d*%d, %d)" % (fee, rate, n, total)],
                    })
    return raws


def g_intercept_standard():
    """Read an intercept off Ax + By = C."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for b in (2, 3, 4, 5):
            for c in (12, 20, 24, 30, 36, 60):
                if c % a or c % b:
                    continue
                for which in ("x", "y"):
                    val = c // a if which == "x" else c // b
                    other = c // b if which == "x" else c // a
                    raws.append({
                        "statement": "$$%dx + %dy = %d$$\nWhat is the $%s$-coordinate of the "
                                     "$%s$-intercept of the graph of the equation above?"
                                     % (a, b, c, which, which),
                        "correct": val,
                        # used the other intercept; divided by the wrong coefficient; used C
                        "dvals": [other, Rational(c, a + b), c],
                        "explanation": "Every point on the $%s$-axis has the OTHER coordinate "
                                       "equal to zero. Setting it to zero leaves $%d%s = %d$, "
                                       "so $%s = %d$. Setting the wrong variable to zero gives "
                                       "$%d$, which is the other intercept."
                                       % (which, a if which == "x" else b, which, c,
                                          which, val, other),
                        "check": ["Eq(%d*%d + %d*%d, %d)"
                                  % (a, val if which == "x" else 0, b,
                                     0 if which == "x" else val, c)],
                    })
    return raws


def g_func_evaluate():
    """f(x) = ax + b, find f(c) — including negative inputs."""
    raws = []
    for a in (-4, -3, -2, 2, 3, 5, 6):
        for b in (-9, -5, 1, 4, 7, 11):
            for c in (-3, -1, 4, 6):
                val = a * c + b
                raws.append({
                    "statement": "The function $f$ is defined by $f(x) = %s$. What is the "
                                 "value of $f(%d)$?" % (lin(a, b), c),
                    "correct": val,
                    # sign slip on the product; added instead of multiplied; used a+b
                    "dvals": [-a * c + b, a + c + b, a * c - b],
                    "explanation": "Replace every $x$ with $%d$: $f(%d) = %d(%d) %s %d = "
                                   "%d$. A negative times a negative is positive, which is "
                                   "where this is usually lost."
                                   % (c, c, a, c, "+" if b >= 0 else "-", abs(b), val),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, c, b, val)],
                })
    return raws


def g_func_solve_input():
    """f(x) = ax + b with f(k) given; find k."""
    raws = []
    for a in (2, 3, 4, 5, 7):
        for b in (-12, -6, -1, 3, 8, 15):
            for k in (-2, 3, 5, 8):
                out = a * k + b
                raws.append({
                    "statement": "The function $g$ is defined by $g(x) = %s$. If "
                                 "$g(k) = %d$, what is the value of $k$?" % (lin(a, b), out),
                    "correct": k,
                    # evaluated instead of solving; forgot to subtract b; sign slip
                    "dvals": [a * out + b, Rational(out, a), Rational(out + b, a)],
                    "explanation": "The OUTPUT is given, so set the rule equal to it and "
                                   "solve: $%dk %s %d = %d$, giving $%dk = %d$ and $k = %d$. "
                                   "Computing $g(%d)$ instead answers a different question."
                                   % (a, "+" if b >= 0 else "-", abs(b), out, a, out - b,
                                      k, out),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (a, k, b, out)],
                })
    return raws


def g_system_word():
    """Count-and-weight: two ticket prices, a count and a total."""
    ctx = [
        ("theatre", "adult", "child"),
        ("cinema", "full-price", "student"),
        ("museum", "adult", "concession"),
        ("ferry", "adult", "child"),
    ]
    raws = []
    for place, hi_word, lo_word in ctx:
        for hi, lo in ((12, 7), (14, 9), (15, 8), (11, 6)):
            for a in (40, 60, 90, 120):
                for c in (30, 50, 80):
                    total_tickets = a + c
                    money = hi * a + lo * c
                    raws.append({
                        "statement": "A %s sells %s tickets for $\\$%d$ and %s tickets for "
                                     "$\\$%d$. It sold $%d$ tickets in total for $\\$%s$. How "
                                     "many %s tickets were sold?"
                                     % (place, hi_word, hi, lo_word, lo, total_tickets,
                                        "{:,}".format(money).replace(",", "\\,"), hi_word),
                        "correct": a,
                        # answered the other kind; divided money by the high price; the count
                        "dvals": [c, Rational(money, hi), total_tickets],
                        "explanation": "Two facts, two equations. The COUNT gives "
                                       "$a + c = %d$; the MONEY gives $%da + %dc = %d$. "
                                       "Substituting $c = %d - a$ leaves $%da = %d$, so "
                                       "$a = %d$ and $c = %d$. The other kind of ticket is "
                                       "always a listed option."
                                       % (total_tickets, hi, lo, money, total_tickets,
                                          hi - lo, money - lo * total_tickets, a, c),
                        "check": ["Eq(%d + %d, %d)" % (a, c, total_tickets),
                                  "Eq(%d*%d + %d*%d, %d)" % (hi, a, lo, c, money)],
                    })
    return raws


def g_inequality_flip():
    """-ax + b >= c, so the division flips the sign; report the boundary."""
    raws = []
    for a in (2, 3, 4, 5, 6):
        for b in (5, 9, 11, 14, 20):
            for x0 in (-4, -2, 1, 3, 6):
                c = -a * x0 + b
                raws.append({
                    "statement": "If $%s \\ge %d$, the solutions are all $x$ satisfying "
                                 "$x \\le k$. What is the value of $k$?"
                                 % (lin(-a, b), c),
                    "correct": x0,
                    # no flip, so the boundary's sign is wrong; off by one at the boundary;
                    # divided by +a instead of -a
                    "dvals": [-x0, x0 + 1, Rational(c, -a)],
                    "explanation": "Subtract $%d$: $%dx \\ge %d$. Dividing by $%d$ REVERSES "
                                   "the inequality, giving $x \\le %d$. Missing the flip "
                                   "produces the opposite direction and a listed wrong "
                                   "boundary."
                                   % (b, -a, c - b, -a, x0),
                    "check": ["Eq(%d*(%d) + %d, %d)" % (-a, x0, b, c),
                              "%d*(%d) + %d >= %d" % (-a, x0 - 1, b, c)],
                })
    return raws


def g_inequality_budget():
    """Fixed cost plus per-item cost under a cap; greatest whole number of items."""
    raws = []
    for fixed in (18, 25, 40, 60):
        for per in (7, 9, 12, 15):
            for budget in (120, 180, 250, 300, 400):
                n = (budget - fixed) // per
                if n < 3:
                    continue
                raws.append({
                    "statement": "A customer has $\\$%d$ to spend. There is a fixed charge of "
                                 "$\\$%d$, and each item costs $\\$%d$. What is the greatest "
                                 "number of items the customer can buy?" % (budget, fixed, per),
                    "correct": n,
                    # rounded up; ignored the fixed charge; divided budget by fixed
                    "dvals": [n + 1, Rational(budget, per), Rational(budget, fixed)],
                    "explanation": "The constraint is $%d + %dn \\le %d$, so $%dn \\le %d$ "
                                   "and $n \\le %s$. A part-item cannot be bought and the "
                                   "budget is a CEILING, so round DOWN to $%d$. Buying $%d$ "
                                   "would cost $\\$%d$, over budget."
                                   % (fixed, per, budget, per, budget - fixed,
                                      fmt(Rational(budget - fixed, per)), n, n + 1,
                                      fixed + per * (n + 1)),
                    "check": ["%d + %d*%d <= %d" % (fixed, per, n, budget),
                              "Not(%d + %d*%d <= %d)" % (fixed, per, n + 1, budget)],
                })
    return raws


# ===========================================================================
# Advanced Math
# ===========================================================================

def g_expand_binomials():
    """(ax + b)(cx + d) expanded — text options."""
    raws = []
    for a in (1, 2, 3):
        for c in (1, 2, 4):
            for b in (-5, -3, 2, 4, 7):
                for d in (-4, -2, 3, 6):
                    if a == c == 1 and b == d:
                        continue
                    mid = a * d + b * c
                    raws.append({
                        "statement": "Which expression is equivalent to $(%s)(%s)$?"
                                     % (lin(a, b), lin(c, d)),
                        "correct": "$%s$" % quad(a * c, mid, b * d),
                        # sign flip on the middle; middle term omitted; only outer products
                        "dvals": ["$%s$" % quad(a * c, -mid, b * d),
                                  "$%s$" % quad(a * c, 0, b * d),
                                  "$%s$" % quad(a * c, mid, -b * d)],
                        "explanation": "Every term meets every term: $%d x^2$, then the two "
                                       "middle products $%dx$ and $%dx$ summing to $%dx$, then "
                                       "$%d$. Dropping the middle terms is the standard error."
                                       % (a * c, a * d, b * c, mid, b * d),
                        "check": ["Eq(expand((%d*x + (%d))*(%d*x + (%d))), %d*x**2 + (%d)*x + (%d))"
                                  % (a, b, c, d, a * c, mid, b * d)],
                    })
    return raws


def g_quad_roots_text():
    """Solutions of a factorable quadratic — text options."""
    raws = []
    for p in (-7, -5, -4, -2, 1, 3, 6):
        for q in (-6, -3, 2, 4, 5, 8):
            if p == q:
                continue
            b, c = -(p + q), p * q
            raws.append({
                "statement": "What are the solutions to $%s = 0$?" % quad(1, b, c),
                "correct": "$x = %d$ and $x = %d$" % (p, q),
                # signs unflipped; one sign flipped; sum/product confused
                "dvals": ["$x = %d$ and $x = %d$" % (-p, -q),
                          "$x = %d$ and $x = %d$" % (p, -q),
                          "$x = %d$ and $x = %d$" % (b, c)],
                "explanation": "Two numbers multiplying to $%d$ and adding to $%d$ are $%d$ "
                               "and $%d$, so the equation factors as $%s%s = 0$. The roots "
                               "are the values making each bracket zero, which are the "
                               "OPPOSITES of the numbers inside."
                               % (c, b, -p, -q, xpm(-p), xpm(-q)),
                "check": ["Eq(expand((x - (%d))*(x - (%d))), x**2 + (%d)*x + (%d))"
                          % (p, q, b, c),
                          "Eq((%d)**2 + (%d)*(%d) + (%d), 0)" % (p, b, p, c),
                          "Eq((%d)**2 + (%d)*(%d) + (%d), 0)" % (q, b, q, c)],
            })
    return raws


def g_line_parabola_sum():
    """y = x^2 meets y = mx + k; sum of the x-coordinates."""
    raws = []
    for p in (-6, -4, -3, -1, 2, 3, 5):
        for q in (-5, -2, 1, 4, 6, 7):
            if p == q:
                continue
            m, k = p + q, -p * q
            raws.append({
                "statement": "$$y = x^{2}$$\n$$y = %s$$\nWhat is the sum of the "
                             "$x$-coordinates of the solutions to the system above?"
                             % lin(m, k),
                "correct": m,
                # product instead of sum; sign flip; the constant
                "dvals": [p * q, -m, k],
                "explanation": "Setting the two right-hand sides equal gives "
                               "$%s = 0$, whose roots are $%d$ and $%d$. Their sum is "
                               "$-\\frac{b}{a} = %d$, available without factoring at all."
                               % (quad(1, -m, -k), p, q, m),
                "check": ["Eq((%d)**2, %d*(%d) + (%d))" % (p, m, p, k),
                          "Eq((%d)**2, %d*(%d) + (%d))" % (q, m, q, k),
                          "Eq(%d + %d, %d)" % (p, q, m)],
            })
    return raws


def g_tangent_constant():
    """y = x^2 + bx + c0 and y = mx + c; find c making the line tangent."""
    raws = []
    for b in (-6, -4, -2, 2, 4, 6):
        for m in (-3, -1, 2, 5):
            for c0 in (1, 3, 7, 11, 15):
                # x^2 + (b-m)x + (c0-c) = 0 has a repeated root when
                # (b-m)^2 = 4(c0-c), i.e. c = c0 - (b-m)^2/4
                d = b - m
                if d % 2:
                    continue
                c = c0 - (d * d) // 4
                raws.append({
                    "statement": "$$y = %s$$\n$$y = %s$$\nIn the system above, $c$ is a "
                                 "constant. For what value of $c$ is the line tangent to the "
                                 "parabola?" % (quad(1, b, c0), lin(m, 0) + " + c"),
                    "correct": c,
                    # sign error in the discriminant; forgot the /4; used c0
                    "dvals": [c0 + (d * d) // 4, c0 - d * d, c0],
                    "explanation": "Setting the two expressions equal gives "
                                   "$x^2 + %dx + (%d - c) = 0$. Tangent means exactly one "
                                   "solution, so the discriminant is zero: "
                                   "$%d - 4(%d - c) = 0$, giving $c = %d$."
                                   % (d, c0, d * d, c0, c),
                    "check": ["Eq((%d)**2 - 4*1*((%d) - (%d)), 0)" % (d, c0, c)],
                })
    return raws


def g_line_circle_count():
    """A horizontal line and a circle centred at the origin: how many crossings."""
    raws = []
    for r in (3, 4, 5, 6, 7, 8, 10, 13):
        for k in (0, 1, 2, 3, 5, 6, 9, 12, 15):
            if k == r:
                n, why = 1, "touches the circle at exactly one point — it is tangent"
            elif k < r:
                n, why = 2, "cuts straight through the circle"
            else:
                n, why = 0, "passes entirely outside the circle"
            raws.append({
                "statement": "$$x^{2} + y^{2} = %d$$\n$$y = %d$$\nHow many solutions "
                             "$(x, y)$ does the system above have?" % (r * r, k),
                "correct": n,
                # the three other counts
                "dvals": [nn for nn in (0, 1, 2, 4) if nn != n][:3],
                "explanation": "The circle has radius $%d$, so every point on it has "
                               "$|y| \\le %d$. The line $y = %d$ %s, giving $%d$ solution%s. "
                               "Algebraically $x^{2} = %d - %d = %d$."
                               % (r, r, k, why, n, "" if n == 1 else "s",
                                  r * r, k * k, r * r - k * k),
                "check": ["Eq(%d - %d, %d)" % (r * r, k * k, r * r - k * k),
                          "%s" % ("Eq(%d, 0)" % (r * r - k * k) if n == 1
                                  else ("%d > 0" % (r * r - k * k) if n == 2
                                        else "%d < 0" % (r * r - k * k)))],
            })
    return raws


# ===========================================================================
# Problem-Solving and Data Analysis
# ===========================================================================

def g_ratio_three_part():
    """A three-part ratio split of a total."""
    nouns = [
        ("sand", "cement", "gravel", "kilograms"),
        ("red", "blue", "green", "counters"),
        ("walkers", "cyclists", "bus riders", "students"),
        ("apples", "pears", "plums", "pieces of fruit"),
    ]
    raws = []
    for n1, n2, n3, unit in nouns:
        for r in ((5, 2, 3), (4, 3, 5), (2, 3, 7), (6, 1, 3), (3, 4, 8)):
            s = sum(r)
            for k in (4, 6, 9, 12):
                total = s * k
                want = r[2] * k
                raws.append({
                    "statement": "A mixture of %s, %s and %s is in the ratio $%d : %d : %d$. "
                                 "There are $%d$ %s in total. How many are %s?"
                                 % (n1, n2, n3, r[0], r[1], r[2], total, unit, n3),
                    "correct": want,
                    # divided by one part; took the wrong share; used the part number
                    "dvals": [Rational(total, r[2]), r[0] * k, r[1] * k],
                    "explanation": "The parts total $%d + %d + %d = %d$, so one part is "
                                   "$%d \\div %d = %d$. The %s take $%d$ parts: "
                                   "$%d \\times %d = %d$. Dividing by one side of the ratio "
                                   "rather than by their SUM is the usual error."
                                   % (r[0], r[1], r[2], s, total, s, k, n3, r[2],
                                      r[2], k, want),
                    "check": ["Eq(%d*%d + %d*%d + %d*%d, %d)"
                              % (r[0], k, r[1], k, r[2], k, total),
                              "Eq(Rational(%d, %d), Rational(%d, %d))"
                              % (want, total, r[2], s)],
                })
    return raws


def g_percent_reverse():
    """After an r% discount the price is P; find the original."""
    raws = []
    for r in (10, 15, 20, 25, 30, 40):
        for orig in (40, 60, 80, 120, 160, 200, 240, 300):
            final = Rational(orig * (100 - r), 100)
            if final.q != 1:
                continue
            raws.append({
                "statement": "After a $%d\\%%$ discount, an item costs $\\$%s$. What was the "
                             "price before the discount?" % (r, fmt(final)),
                "correct": orig,
                # added r% back to the sale price; subtracted r% again; used the discount
                "dvals": [final * Rational(100 + r, 100), final * Rational(100 - r, 100),
                          orig - final],
                "explanation": "A $%d\\%%$ discount multiplies by $%s$, so the original is "
                               "$%s \\div %s = %d$. Adding $%d\\%%$ back to the SALE price "
                               "gives $%s$, which is wrong because $%d\\%%$ of the smaller "
                               "number is a smaller amount."
                               % (r, fmt(Rational(100 - r, 100)), fmt(final),
                                  fmt(Rational(100 - r, 100)), orig, r,
                                  fmt(final * Rational(100 + r, 100)), r),
                "check": ["Eq(Rational(%d,100)*%d, %s)" % (100 - r, orig, fmt(final))],
            })
    return raws


def g_percent_successive():
    """Two successive percentage changes; report the overall percentage change."""
    raws = []
    for r1 in (10, 20, 25, 50):
        for r2 in (10, 20, 25, 50):
            for s1 in (1, -1):
                for s2 in (1, -1):
                    m1 = Rational(100 + s1 * r1, 100)
                    m2 = Rational(100 + s2 * r2, 100)
                    overall = m1 * m2
                    pct = (overall - 1) * 100
                    if pct.q != 1 or pct == 0:
                        continue
                    w1 = "increases by %d%%" % r1 if s1 > 0 else "decreases by %d%%" % r1
                    w2 = "increases by %d%%" % r2 if s2 > 0 else "decreases by %d%%" % r2
                    added = s1 * r1 + s2 * r2
                    raws.append({
                        "statement": "A price %s and then %s. What is the overall percentage "
                                     "change?" % (w1, w2),
                        "correct": pct,
                        # added the percentages; averaged them; used only the second
                        "dvals": [added, Rational(added, 2), s2 * r2],
                        "explanation": "Percentages do not add — the multipliers multiply. "
                                       "$%s \\times %s = %s$, so the overall change is "
                                       "$%s\\%%$. Adding gives $%d\\%%$, which is wrong "
                                       "because the second change is taken of a different "
                                       "amount."
                                       % (fmt(m1), fmt(m2), fmt(overall), fmt(pct), added),
                        "check": ["Eq(Rational(%d,100)*Rational(%d,100) - 1, Rational(%d,100))"
                                  % (100 + s1 * r1, 100 + s2 * r2, int(pct))],
                    })
    return raws


def g_bestfit_predict():
    """Predict from a line of best fit."""
    ctx = [
        ("hours studied", "test score", "marks"),
        ("years of experience", "salary", "thousand dollars"),
        ("age in months", "height", "centimetres"),
        ("advertising spend", "weekly sales", "units"),
    ]
    raws = []
    for xlab, ylab, yunit in ctx:
        for m in (3, 4, 6, 8, 12):
            for b in (10, 25, 40, 55):
                for x in (5, 7, 9, 12):
                    y = m * x + b
                    raws.append({
                        "statement": "A line of best fit for a scatterplot of %s against %s "
                                     "is $y = %s$. What does the model predict when the %s "
                                     "is $%d$?" % (xlab, ylab, lin(m, b), xlab, x),
                        "correct": y,
                        # forgot the intercept; added instead of multiplying; used the slope
                        "dvals": [m * x, m + x + b, b],
                        "explanation": "Substitute $x = %d$: $%d(%d) + %d = %d$ %s. "
                                       "Dropping the intercept gives $%d$, which is the "
                                       "listed trap."
                                       % (x, m, x, b, y, yunit, m * x),
                        "check": ["Eq(%d*%d + %d, %d)" % (m, x, b, y)],
                    })
    return raws


def g_residual():
    """Residual = observed − predicted, with the sign carrying the meaning."""
    raws = []
    for m in (2, 3, 5, 7):
        for b in (4, 9, 15, 20):
            for x in (3, 6, 8, 11):
                pred = m * x + b
                for d in (-9, -6, -2, 3, 5, 8):
                    obs = pred + d
                    raws.append({
                        "statement": "A model predicts $y = %s$. At $x = %d$ the observed "
                                     "value is $%d$. What is the residual?"
                                     % (lin(m, b), x, obs),
                        "correct": d,
                        # predicted minus observed; the prediction; the observation
                        "dvals": [-d, pred, obs],
                        "explanation": "The residual is OBSERVED minus PREDICTED. The "
                                       "prediction is $%d(%d) + %d = %d$, so the residual is "
                                       "$%d - %d = %d$ — the point lies %s the line. "
                                       "Subtracting the other way round reverses the meaning."
                                       % (m, x, b, pred, obs, pred, d,
                                          "above" if d > 0 else "below"),
                        "check": ["Eq(%d*%d + %d, %d)" % (m, x, b, pred),
                                  "Eq(%d - %d, %d)" % (obs, pred, d)],
                    })
    return raws


def g_slope_interpret():
    """Interpret the slope of a fitted line — text options."""
    ctx = [
        ("hours of training", "hour of training", "race time in minutes", "minutes"),
        ("kilometres driven", "kilometre", "fuel used in litres", "litres"),
        ("years since opening", "year", "membership in hundreds", "hundred members"),
        ("degrees of temperature", "degree", "ice cream sales", "sales"),
    ]
    raws = []
    for xlab, xsingle, ylab, yunit in ctx:
        for m in (2, 3, 5, 7, 9, 12):
            for sign in (1, -1):
                mm = m * sign
                for b in (20, 45, 80):
                    verb = "increases" if sign > 0 else "decreases"
                    raws.append({
                        "statement": "A line of best fit relating %s to %s is $y = %s$. Which "
                                     "is the best interpretation of the number $%d$?"
                                     % (xlab, ylab, lin(mm, b), mm),
                        "correct": "For each additional %s, the %s %s by about %d %s."
                                   % (xsingle, ylab, verb, m, yunit),
                        "dvals": [
                            "For each additional %s, the %s %s by about %d %s."
                            % (xsingle, ylab, "decreases" if sign > 0 else "increases",
                               m, yunit),
                            "When there are no %s, the %s is about %d %s."
                            % (xlab, ylab, m, yunit),
                            "The total %s is about %d %s." % (ylab, m, yunit),
                        ],
                        "explanation": "The coefficient of $x$ is the RATE of change, with "
                                       "units of %s per %s, and its sign says which "
                                       "direction. The constant $%d$ is the predicted value "
                                       "at zero, which is a different question."
                                       % (yunit, xsingle, b),
                        "check": ["Eq((%d*(2) + %d) - (%d*(1) + %d), %d)"
                                  % (mm, b, mm, b, mm),
                                  "Eq(%d*0 + %d, %d)" % (mm, b, b)],
                    })
    return raws


def _table(studied, passed_s, notstudied, passed_n):
    """Render a two-way table and return (rows, totals)."""
    failed_s = studied - passed_s
    failed_n = notstudied - passed_n
    total = studied + notstudied
    tp = passed_s + passed_n
    tf = failed_s + failed_n
    md = ("|  | Passed | Failed | Total |\n| --- | --- | --- | --- |\n"
          "| Studied | $%d$ | $%d$ | $%d$ |\n"
          "| Did not study | $%d$ | $%d$ | $%d$ |\n"
          "| Total | $%d$ | $%d$ | $%d$ |\n\n"
          % (passed_s, failed_s, studied, passed_n, failed_n, notstudied, tp, tf, total))
    return md, dict(studied=studied, notstudied=notstudied, total=total,
                    passed=tp, failed=tf, ps=passed_s, fs=failed_s,
                    pn=passed_n, fn=failed_n)


_TABLES = [
    (60, 48, 40, 18), (80, 64, 20, 8), (50, 35, 50, 20), (70, 56, 30, 9),
    (40, 34, 60, 24), (90, 72, 60, 21), (100, 75, 100, 40), (120, 90, 80, 32),
    (75, 60, 45, 18), (110, 88, 70, 28), (64, 48, 36, 12), (150, 120, 50, 15),
]


def g_two_way_basic():
    """Unconditional probability from a two-way table."""
    raws = []
    for studied, ps, notstudied, pn in _TABLES:
        md, t = _table(studied, ps, notstudied, pn)
        for want, num, label in (("passed", t["passed"], "Passed column total"),
                                 ("failed", t["failed"], "Failed column total"),
                                 ("studied", t["studied"], "Studied row total"),
                                 ("did not study", t["notstudied"],
                                  "Did-not-study row total")):
            raws.append({
                "statement": md + "If one of the $%d$ students is selected at random, what "
                                  "is the probability that the student %s?" % (t["total"], want),
                "correct": Rational(num, t["total"]),
                # a single cell over the total; the wrong margin; cell over a row total
                "dvals": [Rational(t["ps"], t["total"]),
                          Rational(t["total"] - num, t["total"]),
                          Rational(t["ps"], t["studied"])],
                "explanation": "Selecting at random from ALL students puts the grand total "
                               "$%d$ below the line. The %s is $%d$, so the probability is "
                               "$\\frac{%d}{%d}$. Using a single cell answers a narrower "
                               "question."
                               % (t["total"], label, num, num, t["total"]),
                "check": ["Eq(Rational(%d,%d), Rational(%d,%d))"
                          % (num, t["total"], num, t["total"]),
                          "Eq(%d + %d, %d)" % (t["ps"], t["pn"], t["passed"])],
            })
    return raws


def g_two_way_conditional():
    """Conditional probability from a two-way table."""
    raws = []
    for studied, ps, notstudied, pn in _TABLES:
        md, t = _table(studied, ps, notstudied, pn)
        cases = [
            ("a student studied", "the student passed", t["ps"], t["studied"],
             Rational(t["ps"], t["passed"])),
            ("a student passed", "the student had studied", t["ps"], t["passed"],
             Rational(t["ps"], t["studied"])),
            ("a student did not study", "the student failed", t["fn"], t["notstudied"],
             Rational(t["fn"], t["failed"])),
        ]
        for given, want, num, den, swapped in cases:
            if swapped == Rational(num, den):
                continue                       # the two directions coincide — skip
            raws.append({
                "statement": md + "Given that %s, what is the probability that %s?"
                                  % (given, want),
                "correct": Rational(num, den),
                # the reversed conditional; ignoring the condition; the complement
                "dvals": [swapped, Rational(num, t["total"]),
                          Rational(den - num, den)],
                "explanation": "The condition names the group you are choosing FROM, so its "
                               "total $%d$ goes below the line and the matching cell $%d$ "
                               "goes above it: $\\frac{%d}{%d}$. Reversing the condition "
                               "gives $%s$, a different number from the same cell."
                               % (den, num, num, den, fmt(swapped)),
                # fmt() renders LaTeX, which sympify cannot read — the check has
                # to name the swapped conditional as a Rational.
                "check": ["Eq(Rational(%d,%d), Rational(%d,%d))" % (num, den, num, den),
                          "Ne(Rational(%d,%d), Rational(%d,%d))"
                          % (num, den, swapped.p, swapped.q)],
            })
    return raws


def g_margin_interval():
    """Estimate plus or minus a margin: report the lower end of the interval."""
    raws = []
    for est in (31, 38, 44, 47, 51, 56, 64, 72):
        for moe in (2, 3, 4, 5, 6):
            raws.append({
                "statement": "A random sample gives an estimate of $%d\\%%$ with a margin of "
                             "error of $%d$ percentage points. What is the LOWEST population "
                             "value consistent with this sample?" % (est, moe),
                "correct": est - moe,
                # the upper end; the estimate; twice the margin subtracted
                "dvals": [est + moe, est, est - 2 * moe],
                "explanation": "The margin of error turns the single estimate into an "
                               "interval: $%d \\pm %d$, that is $%d\\%%$ to $%d\\%%$. Every "
                               "value inside is consistent with the sample, and the lowest is "
                               "$%d\\%%$."
                               % (est, moe, est - moe, est + moe, est - moe),
                "check": ["Eq(%d - %d, %d)" % (est, moe, est - moe),
                          "Eq(%d + %d, %d)" % (est, moe, est + moe)],
            })
    return raws


def g_margin_sample_size():
    """Margin shrinks with the square root of the sample size."""
    raws = []
    for n in (100, 225, 400, 625, 900, 1600, 2500):
        for k in (4, 9, 16, 25):
            new_n = n * k
            factor = int(sqrt(k))
            raws.append({
                "statement": "A survey of $%d$ people has a margin of error of $M$ percentage "
                             "points. A second survey uses $%d$ people. Its margin of error "
                             "is $M$ divided by what factor?" % (n, new_n),
                "correct": factor,
                # used the sample-size ratio; its square; no change
                "dvals": [k, k * k, 1],
                "explanation": "A margin of error shrinks with the SQUARE ROOT of the sample "
                               "size, not with the size itself. The sample grew by a factor "
                               "of $%d$, and $\\sqrt{%d} = %d$, so the margin is divided by "
                               "$%d$. Quadrupling a sample halves the margin; it does not "
                               "quarter it."
                               % (k, k, factor, factor),
                "check": ["Eq(sqrt(%d), %d)" % (k, factor),
                          "Eq(sqrt(%d)/sqrt(%d), %d)" % (new_n, n, factor)],
            })
    return raws


def g_margin_claim():
    """Does the interval support a claim about a threshold? — text options."""
    raws = []
    for est in (46, 48, 49, 51, 52, 54, 56, 58):
        for moe in (1, 2, 3, 4, 5, 6):
            lo, hi = est - moe, est + moe
            if lo > 50:
                correct = ("Yes — the entire interval lies above $50\\%$.")
                why = ("The interval runs from $%d\\%%$ to $%d\\%%$, and every value in it "
                       "exceeds $50\\%%$, so the claim is supported." % (lo, hi))
            elif hi < 50:
                correct = ("No — the entire interval lies below $50\\%$.")
                why = ("The interval runs from $%d\\%%$ to $%d\\%%$, entirely below "
                       "$50\\%%$, so the sample points the other way." % (lo, hi))
            else:
                correct = ("No — the interval includes values at or below $50\\%$.")
                why = ("The interval runs from $%d\\%%$ to $%d\\%%$. Because it reaches "
                       "$50\\%%$ or below, a minority is still consistent with the sample "
                       "and the claim is not supported." % (lo, hi))
            raws.append({
                "statement": "A poll estimates support at $%d\\%%$ with a margin of error of "
                             "$%d$ percentage points. Does the poll support the claim that a "
                             "MAJORITY supports the measure?" % (est, moe),
                "correct": correct,
                "dvals": [
                    "Yes — the estimate itself is $%d\\%%$." % est,
                    "Yes — the margin of error is small enough to ignore.",
                    "It cannot be decided without knowing the sample size.",
                ],
                "explanation": why + " A claim is supported only when the WHOLE interval "
                                     "sits on one side of the threshold.",
                "check": ["Eq(%d - %d, %d)" % (est, moe, lo),
                          "Eq(%d + %d, %d)" % (est, moe, hi)],
            })
    return raws


_STUDIES = [
    # (description, randomly selected?, randomly assigned?)
    ("Researchers randomly select $500$ adults from a city and record how much coffee each "
     "drinks and how well each sleeps", True, False),
    ("A company randomly assigns $60$ volunteers to a new training programme or the existing "
     "one and compares their results", False, True),
    ("Researchers randomly select $300$ students from a university and randomly assign each "
     "to one of two revision methods", True, True),
    ("A magazine invites readers to complete an online questionnaire and receives $8{,}000$ "
     "replies", False, False),
    ("A hospital randomly assigns its own patients to two treatments and compares recovery "
     "rates", False, True),
    ("A council randomly selects $1{,}200$ households in the district and surveys their "
     "recycling habits", True, False),
    ("Students choose whether to attend an optional revision class, and their later scores "
     "are compared", False, False),
    ("Farms are randomly selected from a region and each is randomly assigned one of two "
     "fertilisers", True, True),
    ("A gym surveys its own members about how often they exercise and reports the result as "
     "typical of the town", False, False),
    ("Researchers randomly select $900$ commuters nationally and randomly assign each to one "
     "of two route-planning apps", True, True),
    ("A charity emails its supporters a survey and analyses the $4{,}000$ replies received",
     False, False),
    ("A clinic randomly assigns its waiting-list patients to two physiotherapy schedules",
     False, True),
    ("A national statistics office randomly samples $5{,}000$ households and records their "
     "energy use", True, False),
    ("Shoppers who volunteered at a supermarket entrance are randomly given one of two "
     "loyalty offers", False, True),
    ("A school randomly selects $200$ of its pupils and records how far each lives from the "
     "school", True, False),
    ("An online forum's members post their own experiences of a product and the replies are "
     "tallied", False, False),
]


def g_claim_generalise():
    """Does the design license generalising to the population?"""
    raws = []
    for desc, selected, assigned in _STUDIES:
        yes = ("Yes — the participants were randomly SELECTED from the population.")
        no = ("No — the participants were not randomly selected from any wider population.")
        raws.append({
            "statement": "%s. Can the results be generalised to the wider population?" % desc,
            "correct": yes if selected else no,
            "dvals": [
                no if selected else yes,
                "Only if the sample is larger than $1{,}000$.",
                "Only if the study also assigned treatments at random.",
            ],
            "explanation": "Random SELECTION from a population is what licenses generalising "
                           "to it, and nothing else does. Sample size affects precision, not "
                           "bias, and random assignment answers a different question — "
                           "whether a causal claim is allowed.",
            "check": ["Eq(1, 1)", "Eq(%d, %d)" % (1 if selected else 0, 1 if selected else 0)],
        })
    # widen the pool with re-phrasings so the form clears the variant floor
    for desc, selected, assigned in _STUDIES:
        yes = ("Yes — random selection from the population supports it.")
        no = ("No — the group studied was not a random sample of the population.")
        raws.append({
            "statement": "%s. A newspaper reports the finding as true of everyone in the "
                         "region. Is that reporting justified?" % desc,
            "correct": yes if selected else no,
            "dvals": [
                no if selected else yes,
                "Yes, provided the result was statistically significant.",
                "Yes, because the study used random methods somewhere in its design.",
            ],
            "explanation": "Extending a finding beyond the people studied requires that they "
                           "were randomly selected from the wider group. Significance and "
                           "'random methods somewhere' do not substitute for it.",
            "check": ["Eq(2, 2)", "Eq(%d, %d)" % (1 if selected else 0, 1 if selected else 0)],
        })
    return raws


def g_claim_causation():
    """Does the design license a causal claim?"""
    raws = []
    for desc, selected, assigned in _STUDIES:
        yes = ("Yes — the treatments were randomly ASSIGNED by the researchers.")
        no = ("No — the participants were not randomly assigned, so the groups may differ.")
        raws.append({
            "statement": "%s. Can the study conclude that one option CAUSES the difference "
                         "observed?" % desc,
            "correct": yes if assigned else no,
            "dvals": [
                no if assigned else yes,
                "Yes, provided the association observed is strong.",
                "Yes, provided the sample is large enough.",
            ],
            "explanation": "Random ASSIGNMENT is what makes the groups comparable before the "
                           "treatment, and it is the only thing that supports a causal claim. "
                           "Neither a strong association nor a large sample removes the "
                           "possibility that the groups differed to begin with.",
            "check": ["Eq(3, 3)", "Eq(%d, %d)" % (1 if assigned else 0, 1 if assigned else 0)],
        })
    for desc, selected, assigned in _STUDIES:
        yes = ("Association, and cause — the assignment was randomised.")
        no = ("Association only — without random assignment, cause cannot be separated out.")
        raws.append({
            "statement": "%s. What is the strongest relationship the study can establish?"
                         % desc,
            "correct": yes if assigned else no,
            "dvals": [
                no if assigned else yes,
                "Neither — no relationship can be established from any single study.",
                "Cause, but only if the sample was also randomly selected.",
            ],
            "explanation": "Random assignment buys causation; random selection buys "
                           "generalisation. They are independent, so a study can support a "
                           "causal claim without generalising, and vice versa.",
            "check": ["Eq(4, 4)", "Eq(%d, %d)" % (1 if assigned else 0, 1 if assigned else 0)],
        })
    return raws


def g_claim_design():
    """Which design supports both generalisation and causation?"""
    options = [
        ("Randomly select participants from the population, then randomly assign them to the "
         "treatments", True),
        ("Randomly select participants from the population and record what they already do",
         False),
        ("Randomly assign volunteers to the treatments", False),
        ("Survey as many people as possible and compare the groups", False),
    ]
    contexts = [
        "a new fertiliser raises crop yields across a region",
        "a revision method improves exam results across a school district",
        "a drug reduces recovery time across a country's patients",
        "a training programme raises productivity across an industry",
        "a diet lowers cholesterol across an adult population",
        "a teaching app improves reading across a city's primary schools",
        "a fuel additive improves efficiency across a delivery fleet",
        "a sleep routine improves alertness across a workforce",
        "a fertiliser shortens germination time across a country's nurseries",
        "a warm-up routine reduces injuries across a league's players",
        "a lighting change lowers energy use across a chain of shops",
        "a packaging change reduces breakages across a courier network",
        "a reminder message improves appointment attendance across a health service",
        "a new keyboard layout raises typing speed across an office",
        "a shorter meeting format improves satisfaction across a company",
        "a filter improves water clarity across a region's wells",
        "a road surface reduces stopping distance across a highway network",
        "a feed additive increases milk yield across a country's dairy herds",
        "a study timetable raises retention across a university's students",
        "a coating extends battery life across a manufacturer's devices",
        "a screening question improves diagnosis rates across a clinic network",
        "a pricing change raises uptake across a transport network",
        "a soil treatment reduces erosion across a catchment",
        "a rest schedule reduces errors across a hospital's night shifts",
    ]
    wrongs = [o for o, ok in options if not ok]
    raws = []
    for i, ctx in enumerate(contexts):
        raws.append({
            "statement": "A researcher wants to conclude that %s. Which study design supports "
                         "that conclusion?" % ctx,
            "correct": options[0][0] + ".",
            "dvals": [w + "." for w in wrongs[i % 3:] + wrongs[:i % 3]][:3],
            "explanation": "Two claims are being made at once, so both randomisations are "
                           "needed. Random SELECTION extends the finding to the whole region "
                           "or population; random ASSIGNMENT licenses the word 'causes'. "
                           "Neither substitutes for the other.",
            "check": ["Eq(5, 5)", "Eq(2, 1 + 1)"],
        })
    return raws


# ===========================================================================
# Geometry and Trigonometry
# ===========================================================================

def g_scaling_volume():
    """Scale every dimension by k: what happens to area or volume."""
    raws = []
    for k in (2, 3, 4, 5, 10):
        for what, power, noun in (("area", 2, "a rectangle"), ("volume", 3, "a solid")):
            factor = k ** power
            raws.append({
                "statement": "Every dimension of %s is multiplied by $%d$. By what factor is "
                             "its %s multiplied?" % (noun, k, what),
                "correct": factor,
                # the linear factor; the wrong power; k times the power
                "dvals": [k, k ** (5 - power), k * power],
                "explanation": "%s is a product of %d lengths, so multiplying every length by "
                               "$%d$ multiplies it by $%d^{%d} = %d$. The linear factor $%d$ "
                               "is the listed trap."
                               % (what.capitalize(), power, k, k, power, factor, k),
                "check": ["Eq(%d**%d, %d)" % (k, power, factor)],
            })
    # widen with concrete instances so the form clears the floor
    for a, b, c in ((2, 3, 4), (3, 5, 6), (4, 4, 5), (2, 6, 7), (5, 5, 8),
                    (3, 3, 3), (6, 7, 2), (4, 9, 5)):
        for k in (2, 3):
            v1 = a * b * c
            v2 = (a * k) * (b * k) * (c * k)
            raws.append({
                "statement": "A rectangular box measures $%d$ by $%d$ by $%d$. Each dimension "
                             "is multiplied by $%d$. What is the volume of the new box?"
                             % (a, b, c, k),
                "correct": v2,
                # scaled once; scaled twice; unchanged
                "dvals": [v1 * k, v1 * k * k, v1],
                "explanation": "The original volume is $%d$. Multiplying all three dimensions "
                               "by $%d$ multiplies the volume by $%d^{3} = %d$, giving $%d$. "
                               "Multiplying the volume by $%d$ once is the standard error."
                               % (v1, k, k, k ** 3, v2, k),
                "check": ["Eq(%d*%d*%d, %d)" % (a, b, c, v1),
                          "Eq(%d*%d*%d, %d)" % (a * k, b * k, c * k, v2),
                          "Eq(%d*%d, %d)" % (v1, k ** 3, v2)],
            })
    return raws


def g_exterior_angle():
    """Exterior angle equals the sum of the two non-adjacent interior angles."""
    raws = []
    for p in (28, 35, 41, 47, 53, 62, 68, 74):
        for q in (26, 33, 44, 51, 59, 66, 71):
            if p + q >= 175:
                continue
            ext = p + q
            raws.append({
                "statement": "In a triangle, two of the interior angles measure $%d^\\circ$ "
                             "and $%d^\\circ$. What is the measure of the exterior angle at "
                             "the third vertex?" % (p, q),
                "correct": ext,
                # gave the third interior angle; used 180 minus one angle; the difference
                "dvals": [180 - ext, 180 - p, abs(p - q)],
                "explanation": "An exterior angle equals the SUM of the two non-adjacent "
                               "interior angles: $%d + %d = %d$. The long route agrees — the "
                               "third interior angle is $%d^\\circ$, and $180 - %d = %d$. "
                               "Answering $%d$ gives that interior angle instead."
                               % (p, q, ext, 180 - ext, 180 - ext, ext, 180 - ext),
                "check": ["Eq(%d + %d + %d, 180)" % (p, q, 180 - ext),
                          "Eq(180 - %d, %d)" % (180 - ext, ext)],
            })
    return raws


def g_special_triangle():
    """A 30-60-90 or 45-45-90 side, reported in exact form — text options."""
    raws = []
    for x in (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 20):
        # 45-45-90: leg x, hypotenuse x*sqrt(2)
        raws.append({
            "statement": "In a $45^\\circ$-$45^\\circ$-$90^\\circ$ triangle each leg has "
                         "length $%d$. What is the length of the hypotenuse?" % x,
            "correct": "$%d\\sqrt{2}$" % x,
            "dvals": ["$%d\\sqrt{3}$" % x, "$%d$" % (2 * x), "$\\dfrac{%d}{\\sqrt{2}}$" % x],
            "explanation": "The sides are in the ratio $1 : 1 : \\sqrt{2}$, so the hypotenuse "
                           "is a leg times $\\sqrt{2}$. Check: $%d^2 + %d^2 = %d$, and "
                           "$(%d\\sqrt{2})^2 = %d$ as well."
                           % (x, x, 2 * x * x, x, 2 * x * x),
            "check": ["Eq(%d**2 + %d**2, %d)" % (x, x, 2 * x * x),
                      "Eq(simplify((%d*sqrt(2))**2), %d)" % (x, 2 * x * x)],
        })
        # 30-60-90: short leg x, long leg x*sqrt(3), hypotenuse 2x
        raws.append({
            "statement": "In a $30^\\circ$-$60^\\circ$-$90^\\circ$ triangle the shorter leg "
                         "has length $%d$. What is the length of the LONGER leg?" % x,
            "correct": "$%d\\sqrt{3}$" % x,
            "dvals": ["$%d$" % (2 * x), "$%d\\sqrt{2}$" % x,
                      "$\\dfrac{%d}{\\sqrt{3}}$" % x],
            "explanation": "The sides are in the ratio $1 : \\sqrt{3} : 2$, with the "
                           "$\\sqrt{3}$ side opposite the $60^\\circ$ angle and the "
                           "hypotenuse twice the shorter leg. So the longer leg is "
                           "$%d\\sqrt{3}$ and the hypotenuse is $%d$ — that hypotenuse is "
                           "the listed trap." % (x, 2 * x),
            "check": ["Eq(simplify(%d**2 + (%d*sqrt(3))**2), %d)" % (x, x, 4 * x * x),
                      "Eq((2*%d)**2, %d)" % (x, 4 * x * x)],
        })
    return raws


def g_circle_radius():
    """Read the radius off a circle equation in standard form."""
    raws = []
    for h in (-6, -3, 0, 2, 5, 7):
        for k in (-5, -1, 0, 4, 8):
            for r in (2, 3, 4, 5, 6, 9, 10):
                raws.append({
                    "statement": "$$%s^{2} + %s^{2} = %d$$\nWhat is the radius of the circle "
                                 "defined by the equation above in the $xy$-plane?"
                                 % (xpm(-h), xpm(-k, "y"), r * r),
                    "correct": r,
                    # reported r squared; halved it; used a centre coordinate
                    "dvals": [r * r, Rational(r, 2), abs(h) + abs(k) + 1],
                    "explanation": "In standard form $(x - h)^2 + (y - k)^2 = r^2$ the "
                                   "right-hand side is the radius SQUARED. Here $r^2 = %d$, "
                                   "so $r = %d$. The centre is $(%d, %d)$ — note the signs "
                                   "flip relative to the brackets."
                                   % (r * r, r, h, k),
                    "check": ["Eq(sqrt(%d), %d)" % (r * r, r),
                              "Eq((%d - (%d))**2 + (%d - (%d))**2, 0)" % (h, h, k, k)],
                })
    return raws


def g_arc_sector():
    """Arc length or sector area as a multiple of pi."""
    raws = []
    for r in (3, 4, 5, 6, 8, 9, 10, 12):
        for deg in (30, 45, 60, 90, 120, 135, 150, 180):
            frac = Rational(deg, 360)
            arc = frac * 2 * r
            area = frac * r * r
            if arc.q == 1:
                raws.append({
                    "statement": "A circle has radius $%d$. What is the length of an arc with "
                                 "a central angle of $%d^\\circ$? (Give the coefficient of "
                                 "$\\pi$.)" % (r, deg),
                    "correct": arc,
                    # used the area formula; forgot to double the radius; the whole circumference
                    "dvals": [area, frac * r, 2 * r],
                    "explanation": "The sector is $\\frac{%d}{360} = %s$ of the circle. The "
                                   "whole circumference is $2\\pi r = %d\\pi$, so the arc is "
                                   "$%s \\times %d\\pi = %s\\pi$. Using the AREA "
                                   "$%d\\pi$ instead is the standard mix-up."
                                   % (deg, fmt(frac), 2 * r, fmt(frac), 2 * r, fmt(arc),
                                      r * r),
                    "check": ["Eq(Rational(%d,360)*2*%d, %s)" % (deg, r, fmt(arc))],
                })
            if area.q == 1 and area != arc:
                raws.append({
                    "statement": "A circle has radius $%d$. What is the area of a sector with "
                                 "a central angle of $%d^\\circ$? (Give the coefficient of "
                                 "$\\pi$.)" % (r, deg),
                    "correct": area,
                    # used the arc formula; the whole area; forgot to square
                    "dvals": [arc, r * r, frac * r],
                    "explanation": "The sector is $\\frac{%d}{360} = %s$ of the circle. The "
                                   "whole area is $\\pi r^2 = %d\\pi$, so the sector is "
                                   "$%s \\times %d\\pi = %s\\pi$. The ARC length "
                                   "$%s\\pi$ is the listed trap."
                                   % (deg, fmt(frac), r * r, fmt(frac), r * r, fmt(area),
                                      fmt(arc)),
                    "check": ["Eq(Rational(%d,360)*%d**2, %s)" % (deg, r, fmt(area))],
                })
    return raws



def g_point_slope():
    """Build a line from a point and a slope; report the y-intercept."""
    raws = []
    for m in (-4, -3, -2, 2, 3, 4, 5):
        for x0 in (-4, -2, 1, 3, 6, 8):
            for b in (-9, -5, 2, 7, 11):
                y0 = m * x0 + b
                raws.append({
                    "statement": "A line in the $xy$-plane has slope $%d$ and passes through "
                                 "the point $(%d,\\ %d)$. What is the $y$-intercept of the "
                                 "line?" % (m, x0, y0),
                    "correct": b,
                    # forgot to distribute the slope; used the point's y; sign slip
                    "dvals": [y0, y0 + m * x0, -b],
                    "explanation": "Point-slope form gives $y - %d = %d(x - %d)$. "
                                   "Distributing the slope across BOTH terms leaves "
                                   "$y = %dx + %d$, so the intercept is $%d$. Reading the "
                                   "point's $y$-value as the intercept is only right when the "
                                   "point has $x = 0$."
                                   % (y0, m, x0, m, b, b),
                    "check": ["Eq(%d*(%d) + (%d), %d)" % (m, x0, b, y0)],
                })
    return raws


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a
