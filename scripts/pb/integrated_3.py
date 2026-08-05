# -*- coding: utf-8 -*-
"""Problem-bank subject: Integrated Math 3 — mirrors /math/integrated-3.

Same construction as integrated_1.py / integrated_2.py: library archetypes
are REUSED where they drill exactly what an IM3 unit teaches (re-identified
with an `im3-` prefix, since variant ids are globally unique across the
bank), and the IM3-specific material — trig functions beyond the ratio
definitions, statistical inference, and modelling — is authored fresh below.

Every generator sweeps a parameter grid wide enough to fill a form after
degenerate draws are discarded, and every value stays exact — sympy checks
are built from Rational/Integer, never from Python float division, and
never from fmt() output (which is LaTeX and will not sympify). Symbolic
identity checks go through expand(...) (which evaluates to True); anything
that would leave a symbolic Ne/inequality unevaluated is checked at a
concrete point instead.

Self-check:  python3 scripts/pb/integrated_3.py
Regenerate:  python3 scripts/build_problembank.py
"""
import copy
import importlib.util
import os
import sys

from sympy import Integer, Rational

PB = os.path.dirname(os.path.abspath(__file__))
if PB not in sys.path:
    sys.path.insert(0, PB)

from imbank import fmt, form, lin, mk_num, mk_txt, pt  # noqa: E402

SLUG = "integrated-3"
TITLE = "Integrated Math 3"
TITLE_MN = "Нэгдсэн математик 3"
BLURB = ("Unit-by-unit practice for Integrated Math 3 — polynomial, rational "
         "and logarithmic functions through trigonometric functions, "
         "statistical inference and modelling.")

UNITS = [
    {"id": "polynomial-functions", "title": "Polynomial Functions",
     "blurb": "End behaviour, zeros with multiplicity, the remainder and factor theorems, and polynomial division."},
    {"id": "rational-and-radical-functions", "title": "Rational & Radical Functions",
     "blurb": "Asymptotes and holes, simplifying rational expressions, and radical equations with their extraneous roots."},
    {"id": "exponential-and-logarithmic-functions", "title": "Exponential & Logarithmic Functions",
     "blurb": "Logarithms as inverse exponentials, the log laws, change of base, and solving for the exponent."},
    {"id": "trigonometric-functions", "title": "Trigonometric Functions",
     "blurb": "Radians and the unit circle, exact values, amplitude and period of sinusoids, and the Pythagorean identity."},
    {"id": "function-families-and-inverses", "title": "Function Families & Inverses",
     "blurb": "Transformations across every family, even and odd symmetry, composition, and inverse functions."},
    {"id": "sequences-series-and-the-binomial-theorem", "title": "Sequences, Series & the Binomial Theorem",
     "blurb": "Arithmetic and geometric series, convergence of infinite geometric series, and Pascal's triangle."},
    {"id": "statistical-inference", "title": "Statistical Inference",
     "blurb": "Samples against populations, the normal model, z-scores, simulation verdicts, and margins of error."},
    {"id": "modelling-with-functions", "title": "Modelling with Functions",
     "blurb": "Choosing a function family from data, building models from minimal information, and reading residuals."},
]

# Library forms that drill exactly what an IM3 unit teaches, re-homed.
# fid -> IM3 unit. Sources searched: algebra_2, precalculus, prob_stats.
REMAP = {
    # Unit 1 — polynomial functions
    "degree-of-product": "polynomial-functions",
    "end-behavior": "polynomial-functions",
    "factored-cubic": "polynomial-functions",
    "remainder-theorem": "polynomial-functions",
    "zeros-multiplicity": "polynomial-functions",
    "polynomial-division": "polynomial-functions",
    # Unit 2 — rational & radical functions
    "rational-intercepts": "rational-and-radical-functions",
    "rational-function-features": "rational-and-radical-functions",
    "simplify-rational": "rational-and-radical-functions",
    "solve-radical": "rational-and-radical-functions",
    "hole-or-asymptote": "rational-and-radical-functions",
    # Unit 3 — exponential & logarithmic functions
    "exp-equation": "exponential-and-logarithmic-functions",
    "log-evaluate": "exponential-and-logarithmic-functions",
    "log-add-rule": "exponential-and-logarithmic-functions",
    "log-equation": "exponential-and-logarithmic-functions",
    "log-chain": "exponential-and-logarithmic-functions",
    "exp-substitution": "exponential-and-logarithmic-functions",
    "exp-inequality-flip": "exponential-and-logarithmic-functions",
    # Unit 4 — trigonometric functions (fresh forms below add the rest)
    "radian-exact": "trigonometric-functions",
    "point-on-circle": "trigonometric-functions",
    # Unit 5 — function families & inverses
    "composition": "function-families-and-inverses",
    "describe-transform": "function-families-and-inverses",
    "inverse-of-linear": "function-families-and-inverses",
    "transform-point-function": "function-families-and-inverses",
    "inverse-value": "function-families-and-inverses",
    # Unit 6 — sequences, series & the binomial theorem
    "arith-nth": "sequences-series-and-the-binomial-theorem",
    "geo-nth": "sequences-series-and-the-binomial-theorem",
    "pascal-row": "sequences-series-and-the-binomial-theorem",
    "arith-sum": "sequences-series-and-the-binomial-theorem",
    "geo-sum": "sequences-series-and-the-binomial-theorem",
    "which-term": "sequences-series-and-the-binomial-theorem",
    "binomial-coefficient": "sequences-series-and-the-binomial-theorem",
    "geo-two-terms": "sequences-series-and-the-binomial-theorem",
    "infinite-geo": "sequences-series-and-the-binomial-theorem",
    # Unit 7 — statistical inference (fresh forms below add the rest)
    "study-type": "statistical-inference",
    "sample-vs-population": "statistical-inference",
    # Unit 8 — modelling with functions (fresh forms below add the rest)
    "scatterplot-association": "modelling-with-functions",
    "line-of-fit": "modelling-with-functions",
    "exp-growth-value": "modelling-with-functions",
}

SOURCES = ["algebra_2", "precalculus", "prob_stats"]


def _load(name):
    spec = importlib.util.spec_from_file_location(
        "pbsrc3_%s" % name, os.path.join(PB, "%s.py" % name))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _remapped_forms():
    src = {}
    for name in SOURCES:
        for f in _load(name).build()["forms"]:
            src[f["id"]] = f
    out = []
    for fid, unit in REMAP.items():
        f = copy.deepcopy(src[fid])
        f["unit"] = unit
        f["id"] = "im3-%s" % fid
        for v in f["variants"]:
            v["id"] = "im3-%s" % v["id"]
        out.append(f)
    return out


# ===========================================================================
# Unit 4 — Trigonometric Functions (fresh)
# ===========================================================================

def _g_coterminal():
    """Reduce an out-of-range angle to its coterminal angle in [0, 360)."""
    bases = [30, 45, 60, 90, 120, 135, 150, 210, 225, 240, 270, 300, 315, 330]
    raws = []
    for base in bases:
        for k in (1, 2, -1, -2):
            big = base + 360 * k
            # error models: reflected the angle; went half a turn off;
            # measured from the wrong axis
            d1 = 360 - base
            d2 = (base + 180) % 360
            d3 = abs(base - 90)
            raws.append({
                "statement": ("Find the angle in $[0^\\circ, 360^\\circ)$ that is "
                              "coterminal with $%d^\\circ$." % big),
                "correct": Integer(base),
                "dvals": [Integer(d1), Integer(d2), Integer(d3)],
                "explanation": ("Add or subtract full turns of $360^\\circ$ until the "
                                "angle lands in $[0^\\circ, 360^\\circ)$: $%d^\\circ %s "
                                "%d \\cdot 360^\\circ = %d^\\circ$. Coterminal angles "
                                "share a terminal side, so every trig value of "
                                "$%d^\\circ$ equals that of $%d^\\circ$."
                                % (big, "-" if k > 0 else "+", abs(k), base, big, base)),
                "check": ["Eq(Mod(%d, 360), %d)" % (big, base)],
            })
    return raws


def _g_amplitude_period():
    """Amplitude and period of y = A sin(Bx) + C, asked alternately."""
    raws = []
    period_tex = {1: "2\\pi", 2: "\\pi", 3: "\\frac{2\\pi}{3}",
                  4: "\\frac{\\pi}{2}", 6: "\\frac{\\pi}{3}"}
    period_check = {1: "Eq(2*pi/1, 2*pi)", 2: "Eq(2*pi/2, pi)",
                    3: "Eq(2*pi/3, 2*pi/3)", 4: "Eq(2*pi/4, pi/2)",
                    6: "Eq(2*pi/6, pi/3)"}
    combos = []
    for A in (2, 3, 4, 5, -2, -3):
        for B in (1, 2, 3, 4, 6):
            for C in (0, 1, -2):
                combos.append((A, B, C))
    for i, (A, B, C) in enumerate(combos):
        fn = "y = %s\\sin(%s) %s %d" % (
            ("" if A == 1 else ("-" if A == -1 else str(A))),
            ("x" if B == 1 else "%dx" % B),
            "+" if C >= 0 else "-", abs(C))
        if C == 0:
            fn = fn.rsplit(" ", 2)[0]
        if i % 2 == 0:
            # amplitude question — |A|, and the sign trap is the point
            amp = abs(A)
            raws.append({
                "statement": "State the amplitude of $%s$." % fn,
                "correct": "$%d$" % amp,
                "dvals": ["$%d$" % -abs(A) if A < 0 else "$-%d$" % amp,
                          "$%d$" % B, "$%d$" % (2 * amp)],
                "explanation": ("The amplitude is $|A| = |%d| = %d$ — the half-height "
                                "of the wave, always positive (a negative $A$ flips "
                                "the graph, it does not make the wave negative). $%d$ "
                                "is the value of $B$, which controls the period, not "
                                "the height." % (A, amp, B)),
                "check": ["Eq(Abs(%d), %d)" % (A, amp)],
            })
        else:
            # period question — 2π/B
            raws.append({
                "statement": "State the period of $%s$." % fn,
                "correct": "$%s$" % period_tex[B],
                "dvals": ["$%s$" % ("2\\pi" if B != 1 else "\\pi"),
                          "$%d\\pi$" % (2 * B),
                          "$\\frac{\\pi}{%d}$" % (B + 1)],
                "explanation": ("The period of $\\sin(Bx)$ is $\\dfrac{2\\pi}{B} = "
                                "%s$: a bigger $B$ squeezes more cycles into the same "
                                "space, so the period SHRINKS. Multiplying by $B$ "
                                "instead of dividing is the standard slip."
                                % period_tex[B]),
                "check": [period_check[B]],
            })
    return raws


def _g_pythagorean_identity():
    """Given one trig value and the quadrant, find the other — sign included."""
    triples = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25),
               (20, 21, 29), (9, 40, 41), (12, 35, 37)]
    quads = [(2, "II"), (3, "III"), (4, "IV")]
    raws = []
    for p, q, r in triples:
        for qi, qname in quads:
            for given_sin in (True, False):
                # sin uses p/r, cos uses q/r (and swapped on the other ask)
                if given_sin:
                    g_num, want_num = p, q
                    g_name, want = "\\sin", "\\cos"
                    g_sign = 1 if qi == 2 else -1
                    want_sign = -1 if qi in (2, 3) else 1
                else:
                    g_num, want_num = q, p
                    g_name, want = "\\cos", "\\sin"
                    g_sign = -1 if qi in (2, 3) else 1
                    want_sign = 1 if qi == 2 else -1
                gv = Rational(g_sign * g_num, r)
                wv = Rational(want_sign * want_num, r)
                sgn_tex = "-" if gv < 0 else ""
                correct = "$%s$" % fmt(wv)
                raws.append({
                    "statement": ("Given $%s\\theta = %s\\frac{%d}{%d}$ with $\\theta$ "
                                  "in quadrant %s, find $%s\\theta$."
                                  % (g_name, sgn_tex, g_num, r, qname, want)),
                    "correct": correct,
                    "dvals": ["$%s$" % fmt(-wv), "$%s$" % fmt(Rational(want_num, g_num) * (1 if wv > 0 else -1)),
                              "$%s$" % fmt(Rational(g_num, r) * (1 if wv > 0 else -1))],
                    "explanation": ("Pythagorean identity first: $\\sin^2\\theta + "
                                    "\\cos^2\\theta = 1$ gives $%s^2\\theta = 1 - "
                                    "\\frac{%d}{%d} = \\frac{%d}{%d}$, so $%s\\theta = "
                                    "\\pm\\frac{%d}{%d}$. Quadrant %s fixes the sign: "
                                    "$%s\\theta = %s$."
                                    % (want, g_num * g_num, r * r,
                                       want_num * want_num, r * r, want,
                                       want_num, r, qname, want, fmt(wv))),
                    "check": [
                        "Eq(Rational(%d,%d)**2 + Rational(%d,%d)**2, 1)"
                        % (p, r, q, r),
                        "%s(Rational(%d,%d), 0)"
                        % ("Lt" if wv < 0 else "Gt", wv.p, wv.q),
                    ],
                })
    return raws


# ===========================================================================
# Unit 5 — Function Families & Inverses (fresh)
# ===========================================================================

def _g_even_odd():
    """Classify a polynomial as even, odd, or neither — by the algebra."""
    OPT_EVEN = "even — $f(-x) = f(x)$"
    OPT_ODD = "odd — $f(-x) = -f(x)$"
    OPT_NEITHER = "neither"
    OPT_BOTH = "both even and odd"
    raws = []

    def poly_tex(terms):
        # terms: list of (coef, power); render descending
        s = ""
        for c, k in terms:
            if c == 0:
                continue
            mono = ("%d" % abs(c)) if k == 0 else (
                ("x" if k == 1 else "x^%d" % k) if abs(c) == 1
                else ("%dx" % abs(c) if k == 1 else "%dx^%d" % (abs(c), k)))
            s += (" - " if c < 0 else (" + " if s else "")) + mono
        return s if s else "0"

    def f_of(terms, x):
        return sum(c * x ** k for c, k in terms)

    cases = []
    for a in (1, 2, 3):
        for b in (-3, -1, 2):
            cases.append(([(a, 4), (b, 2)], "even"))
            cases.append(([(a, 5), (b, 3)], "odd"))
            cases.append(([(a, 4), (b, 3)], "neither"))
    for a in (1, 2, -2):
        cases.append(([(a, 2), (5, 0)], "even"))
        cases.append(([(a, 3), (-4, 1)], "odd"))
        cases.append(([(a, 3), (2, 0)], "neither"))
        cases.append(([(a, 2), (3, 1)], "neither"))
    for terms, kind in cases:
        tex = poly_tex(terms)
        f2, fm2 = f_of(terms, 2), f_of(terms, -2)
        if kind == "even":
            correct, d = OPT_EVEN, [OPT_ODD, OPT_NEITHER, OPT_BOTH]
            why = ("every exponent is even, so $f(-x) = f(x)$ term by term")
            checks = ["Eq(%d, %d)" % (fm2, f2)]
        elif kind == "odd":
            correct, d = OPT_ODD, [OPT_EVEN, OPT_NEITHER, OPT_BOTH]
            why = ("every exponent is odd, so each term flips sign: "
                   "$f(-x) = -f(x)$")
            checks = ["Eq(%d, %d)" % (fm2, -f2)]
        else:
            correct, d = OPT_NEITHER, [OPT_EVEN, OPT_ODD, OPT_BOTH]
            why = ("the exponents mix parities, so $f(-x)$ is neither $f(x)$ "
                   "nor $-f(x)$ — test $x = 2$: $f(2) = %d$ but $f(-2) = %d$"
                   % (f2, fm2))
            checks = ["Ne(%d, %d)" % (fm2, f2), "Ne(%d, %d)" % (fm2, -f2)]
        raws.append({
            "statement": "Classify $f(x) = %s$ as even, odd, or neither." % tex,
            "correct": correct,
            "dvals": d,
            "explanation": ("Substitute $-x$: %s. (Even = mirror symmetry across "
                            "the $y$-axis; odd = point symmetry through the "
                            "origin; only $f(x) = 0$ is both.)" % why),
            "check": checks,
        })
    return raws


# ===========================================================================
# Unit 7 — Statistical Inference (fresh)
# ===========================================================================

def _g_sample_estimate():
    """Scale a sample proportion up to a population estimate."""
    raws = []
    grid = [
        (1200, 50, 30, "students", "support a later school start"),
        (1200, 40, 26, "students", "walk to school"),
        (800, 40, 18, "members", "want longer library hours"),
        (800, 25, 15, "members", "attend weekly"),
        (2000, 50, 32, "voters", "favour the proposal"),
        (2000, 25, 9, "voters", "are undecided"),
        (1500, 50, 21, "readers", "prefer print books"),
        (1500, 30, 12, "readers", "use the audiobook app"),
        (600, 30, 21, "employees", "cycle to work"),
        (600, 20, 13, "employees", "pack a lunch"),
        (900, 30, 24, "households", "recycle weekly"),
        (900, 45, 27, "households", "own a pet"),
        (2400, 60, 33, "shoppers", "use the loyalty card"),
        (2400, 40, 22, "shoppers", "visit weekly"),
        (3000, 75, 45, "residents", "support the new park"),
        (3000, 50, 28, "residents", "commute by bus"),
        (450, 30, 18, "players", "prefer evening matches"),
        (450, 25, 10, "players", "train daily"),
        (1600, 40, 25, "viewers", "stream weekly"),
        (1600, 80, 52, "viewers", "watch with subtitles"),
        (700, 35, 14, "gardeners", "grow vegetables"),
        (700, 28, 21, "gardeners", "compost"),
        (5000, 100, 63, "citizens", "back the measure"),
        (5000, 125, 80, "citizens", "read local news"),
        (1000, 40, 17, "runners", "race this year"),
        (1000, 50, 36, "runners", "train in the morning"),
        (360, 24, 15, "teachers", "assign weekly quizzes"),
        (360, 30, 21, "teachers", "use printed textbooks"),
    ]
    for N, n, k, who, what in grid:
        val = Rational(k, n) * N
        if val != int(val):
            continue
        val = Integer(val)
        raws.append({
            "statement": ("A population of $%d$ %s is studied through a random "
                          "sample of $%d$; exactly $%d$ of the sample %s. What is "
                          "the best estimate of how many of the %d %s?"
                          % (N, who, n, k, what, N, what)),
            "correct": val,
            # error models: reported the raw sample count; scaled the
            # complement; treated the count as a percent of the population
            "dvals": [Integer(k), Integer(Rational(n - k, n) * N), Integer(k * N // 100)],
            "explanation": ("The sample proportion is $\\hat{p} = \\frac{%d}{%d}$, "
                            "and because the sample was random it estimates the "
                            "population proportion: about $\\frac{%d}{%d} \\cdot %d "
                            "= %d$. The raw count $%d$ describes only the sample."
                            % (k, n, k, n, N, val, k)),
            "check": ["Eq(Rational(%d,%d)*%d, %d)" % (k, n, N, val)],
        })
    return raws


def _g_empirical_rule():
    """The 68–95–99.7 rule: percent in a band or a tail."""
    contexts = [
        ("Heights", 170, 8, "cm"),
        ("Test scores", 70, 6, "points"),
        ("Battery lives", 40, 4, "hours"),
        ("Fill volumes", 500, 5, "ml"),
        ("Reaction times", 300, 20, "ms"),
        ("Delivery times", 30, 5, "minutes"),
        ("Part lengths", 60, 2, "mm"),
        ("Daily sales", 240, 15, "units"),
    ]
    kinds = [
        ("between $%s$ and $%s$", 1, 1, "$68\\%$",
         ["$95\\%$", "$50\\%$", "$34\\%$"],
         "within one standard deviation of the mean lies about $68\\%$",
         "Eq(100 - 68, 32)"),
        ("between $%s$ and $%s$", 2, 2, "$95\\%$",
         ["$68\\%$", "$99.7\\%$", "$47.5\\%$"],
         "within two standard deviations lies about $95\\%$",
         "Eq(100 - 95, 5)"),
        ("above $%s$", None, 1, "$16\\%$",
         ["$32\\%$", "$68\\%$", "$84\\%$"],
         "outside one standard deviation lies $32\\%$, split into two tails "
         "of $16\\%$ each",
         "Eq(Rational(100 - 68, 2), 16)"),
        ("above $%s$", None, 2, "$2.5\\%$",
         ["$5\\%$", "$95\\%$", "$16\\%$"],
         "outside two standard deviations lies $5\\%$, split into two tails "
         "of $2.5\\%$ each",
         "Eq(Rational(100 - 95, 2), Rational(5, 2))"),
        ("below $%s$", -1, None, "$16\\%$",
         ["$68\\%$", "$32\\%$", "$2.5\\%$"],
         "the tail below one standard deviation holds "
         "$\\frac{100 - 68}{2} = 16\\%$",
         "Eq(Rational(100 - 68, 2), 16)"),
        ("below $%s$", -2, None, "$2.5\\%$",
         ["$16\\%$", "$5\\%$", "$0.3\\%$"],
         "the tail below two standard deviations holds "
         "$\\frac{100 - 95}{2} = 2.5\\%$",
         "Eq(Rational(100 - 95, 2), Rational(5, 2))"),
    ]
    raws = []
    for name, mu, sd, unit in contexts:
        for tpl, lo_k, hi_k, correct, dvals, why, check in kinds:
            if lo_k is not None and hi_k is not None:
                band = tpl % ("%d" % (mu - lo_k * sd), "%d" % (mu + hi_k * sd))
            elif tpl.startswith("above"):
                band = tpl % ("%d" % (mu + hi_k * sd))
            else:
                band = tpl % ("%d" % (mu + lo_k * sd))
            raws.append({
                "statement": ("%s are approximately normal with mean $%d$ %s and "
                              "standard deviation $%d$ %s. About what percent are "
                              "%s?" % (name, mu, unit, sd, unit, band)),
                "correct": correct,
                "dvals": list(dvals),
                "explanation": ("Convert the endpoints to standard deviations from "
                                "the mean, then apply the empirical rule: %s." % why),
                "check": [check],
            })
    return raws


def _g_z_scores():
    """Compute a z-score exactly (integer or half-integer)."""
    raws = []
    grid = []
    for mu, sd in [(70, 8), (100, 15), (64, 6), (500, 100), (40, 4),
                   (170, 8), (75, 6), (240, 20), (30, 5), (60, 12)]:
        for z in (Rational(-2), Rational(-3, 2), Rational(-1), Rational(-1, 2),
                  Rational(1, 2), Rational(1), Rational(3, 2), Rational(2),
                  Rational(5, 2)):
            x = mu + z * sd
            if x != int(x):
                continue
            grid.append((mu, sd, int(x), z))
    for mu, sd, x, z in grid:
        raws.append({
            "statement": ("A distribution has mean $%d$ and standard deviation "
                          "$%d$. Find the z-score of the value $%d$." % (mu, sd, x)),
            "correct": z,
            # error models: sign flipped; forgot to divide; divided by the mean
            "dvals": [-z, Integer(x - mu), z / 2],
            "explanation": ("$z = \\dfrac{x - \\mu}{\\sigma} = \\dfrac{%d - %d}{%d} "
                            # fmt() returns BARE LaTeX, so it needs its own
                            # $...$ here — the span above has already closed.
                            "= %s$: the value sits $%s$ standard deviation%s %s the "
                            "mean. The sign carries the direction — losing it is "
                            "the classic slip."
                            % (x, mu, sd, fmt(z), fmt(abs(z)),
                               "" if abs(z) == 1 else "s",
                               "below" if z < 0 else "above")),
            "check": ["Eq(Rational(%d - %d, %d), Rational(%d, %d))"
                      % (x, mu, sd, z.p, z.q)],
        })
    return raws


def _g_simulation_verdict():
    """Read a simulation: is the observed result consistent with the claim?"""
    OPT_DOUBT = ("doubt the claim — results this extreme are too rare to "
                 "blame on chance")
    OPT_CONSISTENT = ("consistent with the claim — ordinary sampling "
                      "variability explains it")
    OPT_PROOF = "the claim is proven false beyond doubt"
    OPT_MORE = "no conclusion is possible without a formula"
    scenarios = [
        ("A coin claimed fair lands heads $%d$ times in $100$ flips", 62),
        ("A die claimed fair shows a six $%d$ times in $60$ rolls", 16),
        ("A spinner claimed to land blue half the time shows $%d$ blues in $40$ spins", 26),
        ("A seed packet claiming $50\\%%$ germination sprouts $%d$ of $40$ seeds", 13),
        ("A sweet company claiming $40\\%%$ red produces a bag with $%d$ red of $25$", 5),
        ("A player claiming $30\\%%$ accuracy makes $%d$ of $20$ shots", 9),
        ("A poll model predicting $60\\%%$ support finds $%d$ supporters in $50$", 24),
        ("A machine rated $10\\%%$ defective produces $%d$ defects in $50$ parts", 9),
    ]
    trials = [(200, 4), (250, 5), (400, 8), (500, 5), (100, 3),
              (200, 24), (250, 40), (400, 60), (500, 80), (100, 15)]
    raws = []
    i = 0
    for stmt_tpl, obs in scenarios:
        for T, E in trials:
            i += 1
            if i > 40:
                break
            share = Rational(E, T)
            rare = share < Rational(1, 20)
            pct = fmt(share * 100)
            raws.append({
                "statement": ("%s. In $%d$ simulated trials run under the claim, "
                              "$%d$ trials were at least as extreme as the observed "
                              "result. What is the right conclusion?"
                              % (stmt_tpl % obs, T, E)),
                "correct": OPT_DOUBT if rare else OPT_CONSISTENT,
                "dvals": [OPT_CONSISTENT if rare else OPT_DOUBT, OPT_PROOF, OPT_MORE],
                "explanation": ("Under the claim, results this extreme appeared in "
                                "$\\frac{%d}{%d} = %s\\%%$ of trials — %s the $5\\%%$ "
                                "working line. %s (Simulation gives evidence, never "
                                "proof: the verdict is about plausibility.)"
                                % (E, T, pct,
                                   "below" if rare else "above",
                                   "That is too rare to blame on sampling wobble, "
                                   "so the claim itself is doubtful."
                                   if rare else
                                   "Chance produces such results routinely, so the "
                                   "observation is no evidence against the claim.")),
                "check": ["%s(Rational(%d,%d), Rational(1,20))"
                          % ("Lt" if rare else "Gt", E, T)],
            })
    return raws


def _g_margin_of_error():
    """MoE = 1/sqrt(n) as a percent, and the interval it builds."""
    ns = [(100, "10"), (400, "5"), (625, "4"), (1600, "2.5"), (2500, "2"), (10000, "1")]
    checks = {100: "Eq(1/sqrt(100), Rational(1,10))",
              400: "Eq(1/sqrt(400), Rational(1,20))",
              625: "Eq(1/sqrt(625), Rational(1,25))",
              1600: "Eq(1/sqrt(1600), Rational(1,40))",
              2500: "Eq(1/sqrt(2500), Rational(1,50))",
              10000: "Eq(1/sqrt(10000), Rational(1,100))"}
    raws = []
    # kind A: state the margin
    for n, moe in ns:
        others = [m for _, m in ns if m != moe][:3]
        raws.append({
            "statement": ("A poll samples $%d$ people at random. Using the quick "
                          "rule $\\text{MoE} \\approx \\frac{1}{\\sqrt{n}}$, its "
                          "margin of error is about:" % n),
            "correct": "$%s\\%%$" % moe,
            "dvals": ["$%s\\%%$" % m for m in others],
            "explanation": ("$\\frac{1}{\\sqrt{%d}}$ as a percent is $%s\\%%$. The "
                            "square root is why precision is expensive: quadrupling "
                            "the sample only halves the margin." % (n, moe)),
            "check": [checks[n]],
        })
    # kind B: interval endpoint
    for n, moe_pct, phat, lo, hi in [
        (400, 5, 52, 47, 57), (400, 5, 48, 43, 53), (400, 5, 61, 56, 66),
        (100, 10, 56, 46, 66), (100, 10, 63, 53, 73), (100, 10, 44, 34, 54),
        (625, 4, 58, 54, 62), (625, 4, 47, 43, 51), (625, 4, 66, 62, 70),
        (2500, 2, 54, 52, 56), (2500, 2, 49, 47, 51), (2500, 2, 62, 60, 64),
        (1600, 2, 55, 52, 58),   # (2.5 rounds the interval to halves; use ±2.5 -> 52.5 avoided)
    ]:
        if n == 1600:
            continue  # keep endpoints whole — 2.5-point margins make messy options
        raws.append({
            "statement": ("A random poll of $%d$ people finds $%d\\%%$ support. "
                          "With the quick-rule margin of error, the LOWEST "
                          "plausible level of true support is about:" % (n, phat)),
            "correct": "$%d\\%%$" % lo,
            "dvals": ["$%d\\%%$" % hi, "$%d\\%%$" % phat, "$%d\\%%$" % (lo - moe_pct)],
            "explanation": ("The margin is $\\frac{1}{\\sqrt{%d}} = %d\\%%$, so the "
                            "honest reading is the interval $%d\\%%$ to $%d\\%%$ — "
                            "the poll's single number minus the margin gives the "
                            "low end, $%d - %d = %d$."
                            % (n, moe_pct, lo, hi, phat, moe_pct, lo)),
            "check": [checks[n], "Eq(%d - %d, %d)" % (phat, moe_pct, lo)],
        })
        raws.append({
            "statement": ("A random poll of $%d$ people finds $%d\\%%$ support. "
                          "With the quick-rule margin of error, the HIGHEST "
                          "plausible level of true support is about:" % (n, phat)),
            "correct": "$%d\\%%$" % hi,
            "dvals": ["$%d\\%%$" % lo, "$%d\\%%$" % phat, "$%d\\%%$" % (hi + moe_pct)],
            "explanation": ("The margin is $\\frac{1}{\\sqrt{%d}} = %d\\%%$, so the "
                            "honest reading is the interval $%d\\%%$ to $%d\\%%$ — "
                            "the poll's single number plus the margin gives the "
                            "high end, $%d + %d = %d$."
                            % (n, moe_pct, lo, hi, phat, moe_pct, hi)),
            "check": [checks[n], "Eq(%d + %d, %d)" % (phat, moe_pct, hi)],
        })
    return raws


def _g_sample_size():
    """Invert the square-root law: sample size from a target margin."""
    raws = []
    # kind A: n for a target margin
    for m_tex, m_frac, n in [("5", "Rational(1,20)", 400), ("4", "Rational(1,25)", 625),
                             ("2", "Rational(1,50)", 2500), ("10", "Rational(1,10)", 100),
                             ("1", "Rational(1,100)", 10000), ("2.5", "Rational(1,40)", 1600)]:
        raws.append({
            "statement": ("A newspaper wants poll results with a margin of error "
                          "of about $%s\\%%$. Using $\\text{MoE} \\approx "
                          "\\frac{1}{\\sqrt{n}}$, how many people must it sample?"
                          % m_tex),
            "correct": Integer(n),
            "dvals": [Integer(n // 4), Integer(n * 4), Integer(int(round(n ** 0.5)))],
            "explanation": ("Set $\\frac{1}{\\sqrt{n}} = %s\\%%$ and invert: "
                            "$\\sqrt{n} = \\frac{100}{%s}$, so $n = %d$. The "
                            "margin's square root means small improvements in "
                            "precision demand large increases in sample."
                            % (m_tex, m_tex, n)),
            "check": ["Eq(1/sqrt(%d), %s)" % (n, m_frac)],
        })
    # kind B: growth factor to shrink a margin
    for a, b in [(10, 5), (10, 2), (8, 4), (8, 2), (6, 3), (6, 2),
                 (12, 6), (12, 4), (12, 3), (9, 3), (4, 2), (4, 1),
                 (15, 5), (15, 3), (20, 10), (20, 5), (20, 4), (16, 8),
                 (16, 4), (18, 9), (18, 6), (14, 7)]:
        r = a // b
        factor = r * r
        raws.append({
            "statement": ("A pollster wants to cut the margin of error from "
                          "$%d\\%%$ to $%d\\%%$. The sample size must be "
                          "multiplied by:" % (a, b)),
            "correct": Integer(factor),
            "dvals": [Integer(r), Integer(2 * factor), Integer(factor * factor)],
            "explanation": ("The margin runs as $\\frac{1}{\\sqrt{n}}$, so shrinking "
                            "it by a factor of $%d$ demands $%d^2 = %d$ times the "
                            "sample. Doubling the precision always quadruples the "
                            "bill." % (r, r, factor)),
            "check": ["Eq((Rational(%d,%d))**2, %d)" % (a, b, factor)],
        })
    return raws


# ===========================================================================
# Unit 8 — Modelling with Functions (fresh)
# ===========================================================================

def _g_family_from_table():
    """Identify the function family from four table values at x = 0..3."""
    OPT_LIN = "linear — constant first differences"
    OPT_EXP = "exponential — constant ratios"
    OPT_QUAD = "quadratic — constant second differences"
    OPT_NONE = "none of these families"
    raws = []
    cases = []
    for a in (2, 3, 4, -2, 5, 6, -3):
        for b in (1, 4, 7, 12, 20):
            ys = [b + a * x for x in range(4)]
            cases.append((ys, "lin", a))
    for a in (2, 3, 5, 4):
        for r in (2, 3):
            ys = [a * r ** x for x in range(4)]
            cases.append((ys, "exp", r))
    for a2 in (1, 2, -1, 3):
        for b in (0, 1, 3, -2):
            c = 2
            ys = [a2 * x * x + b * x + c for x in range(4)]
            cases.append((ys, "quad", 2 * a2))
    for ys, kind, key in cases:
        y0, y1, y2, y3 = ys
        tbl = "$%s$" % (",\\ ".join(fmt(y) for y in ys))
        if kind == "lin":
            correct, d = OPT_LIN, [OPT_EXP, OPT_QUAD, OPT_NONE]
            why = ("the first differences are constant at $%d$" % key)
            checks = ["Eq(%d - %d, %d - %d)" % (y1, y0, y2, y1),
                      "Eq(%d - %d, %d - %d)" % (y2, y1, y3, y2)]
        elif kind == "exp":
            correct, d = OPT_EXP, [OPT_LIN, OPT_QUAD, OPT_NONE]
            why = ("the ratios are constant at $%d$" % key)
            checks = ["Eq(Rational(%d,%d), Rational(%d,%d))" % (y1, y0, y2, y1),
                      "Eq(Rational(%d,%d), Rational(%d,%d))" % (y2, y1, y3, y2)]
        else:
            correct, d = OPT_QUAD, [OPT_LIN, OPT_EXP, OPT_NONE]
            why = ("the first differences change, but the SECOND differences "
                   "are constant at $%d$" % key)
            checks = ["Eq((%d - %d) - (%d - %d), (%d - %d) - (%d - %d))"
                      % (y2, y1, y1, y0, y3, y2, y2, y1),
                      "Ne(%d - %d, %d - %d)" % (y1, y0, y2, y1)]
        raws.append({
            "statement": ("For equal steps $x = 0, 1, 2, 3$ a table reads %s. "
                          "Which function family fits?" % tbl),
            "correct": correct,
            "dvals": d,
            "explanation": ("Run the tests in order — differences, ratios, second "
                            "differences: %s. That signature belongs to exactly "
                            "one family." % why),
            "check": checks,
        })
    return raws


def _g_model_from_points():
    """Build the line through two points and predict a third value."""
    contexts = [
        ("A candle is $%s$ cm tall $%d$ hours after lighting and $%s$ cm after $%d$ hours",
         "how tall (cm) is it after $%d$ hours?"),
        ("A tank holds $%s$ litres $%d$ minutes after the pump starts and $%s$ litres after $%d$ minutes",
         "how much (litres) does it hold after $%d$ minutes?"),
        ("A hiker is $%s$ km from camp $%d$ hours into the day and $%s$ km after $%d$ hours",
         "how far (km) is the hiker after $%d$ hours?"),
        ("A printer has $%s$ pages left $%d$ minutes into a job and $%s$ pages after $%d$ minutes",
         "how many pages remain after $%d$ minutes?"),
    ]
    raws = []
    i = 0
    for m in (3, 5, -3, -4, 2, 6, -2, 4):
        for b in (20, 45, 100, 60, 32):
            x1, x2, x3 = 2, 5, 8
            y1, y2 = m * x1 + b, m * x2 + b
            y3 = m * x3 + b
            if y1 <= 0 or y2 <= 0 or y3 <= 0:
                continue
            ctx, ask = contexts[i % len(contexts)]
            i += 1
            raws.append({
                "statement": (("%s. If the change is linear, %s")
                              % (ctx % (fmt(y1), x1, fmt(y2), x2), ask % x3)),
                "correct": Integer(y3),
                # error models: continued from y2 by one step's worth only;
                # sign-flipped the slope; reused the first reading
                "dvals": [Integer(y2 + m), Integer(-m * x3 + b), Integer(y1)],
                "explanation": ("Slope from the two readings: $m = \\frac{%s - %s}"
                                "{%d - %d} = %d$ per unit, and $%s = %d \\cdot %d + b$ "
                                "gives $b = %d$. So $y = %s$, and at $x = %d$: $%d$."
                                % (fmt(y2), fmt(y1), x2, x1, m, fmt(y1), m, x1, b,
                                   lin(m, b), x3, y3)),
                "check": ["Eq(Rational(%d - %d, %d - %d), %d)" % (y2, y1, x2, x1, m),
                          "Eq(%d*%d + %d, %d)" % (m, x3, b, y3)],
            })
    return raws


def _g_residual():
    """Residual = actual - predicted, sign and all."""
    raws = []
    grid = []
    for m in (2, 3, 4, 5, -2):
        for b in (1, 3, 10, 40):
            for x0 in (2, 3, 5, 6):
                for r in (-4, -3, -2, 2, 3, 4, 5, -5):
                    grid.append((m, b, x0, r))
    for m, b, x0, r in grid[:120]:
        pred = m * x0 + b
        y0 = pred + r
        if y0 <= 0:
            continue
        raws.append({
            "statement": ("A fitted model predicts $\\hat{y} = %s$. The measured "
                          "data point is $%s$. What is the residual at that "
                          "point?" % (lin(m, b), pt(x0, y0))),
            "correct": Integer(r),
            # error models: sign convention flipped; reported the prediction;
            # reported the measurement
            "dvals": [Integer(-r), Integer(pred), Integer(y0)],
            "explanation": ("Residual = actual $-$ predicted. The model predicts "
                            "$\\hat{y} = %d \\cdot %d %s %d = %d$, and the "
                            "measurement was $%d$, so $r = %d - %d = %s$ — the "
                            "data point sits %s the model."
                            % (m, x0, "+" if b >= 0 else "-", abs(b), pred, y0,
                               y0, pred, fmt(r),
                               "above" if r > 0 else "below")),
            "check": ["Eq(%d - (%d*%d + %d), %d)" % (y0, m, x0, b, r)],
        })
    return raws


def _g_quadratic_from_vertex():
    """Vertex + one point pin the parabola; evaluate it elsewhere."""
    raws = []
    grid = []
    for a in (1, 2, -1, -2, 3):
        for h in (1, 2, 3, -1, -2):
            for k in (2, -3, 5, -1):
                for d in (1, 2, 3):
                    grid.append((a, h, k, d))
    for a, h, k, d in grid:
        x1 = h + d
        y1 = a * d * d + k
        y0 = a * h * h + k          # value at x = 0, the asked prediction
        if abs(y0) > 60 or y1 == y0:
            continue
        raws.append({
            "statement": ("A parabola has vertex $%s$ and passes through $%s$. "
                          "What is its $y$-intercept?" % (pt(h, k), pt(x1, y1))),
            "correct": Integer(y0),
            # error models: dropped the stretch a (used a = 1); flipped the
            # sign of k; reported the vertex height. (Flipping the vertex
            # sign inside the square is NOT a usable distractor — squaring
            # erases it, so it lands on the right answer.)
            "dvals": [Integer(h * h + k), Integer(a * h * h - k), Integer(k)],
            "explanation": ("Vertex form does the work: $y = a(x - %s)^2 %s %s$ "
                            "with $a$ from the extra point — $%s = a(%d)^2 %s %s$ "
                            "gives $a = %d$. At $x = 0$: $y = %d(%s)^2 %s %s = %d$."
                            % (fmt(h), "+" if k >= 0 else "-", fmt(abs(k)),
                               fmt(y1), d, "+" if k >= 0 else "-", fmt(abs(k)),
                               a, a, fmt(-h), "+" if k >= 0 else "-",
                               fmt(abs(k)), y0)),
            "check": ["Eq(%d*(%d - %d)**2 + %d, %d)" % (a, x1, h, k, y1),
                      "Eq(%d*(0 - %d)**2 + %d, %d)" % (a, h, k, y0)],
        })
    return raws


# ===========================================================================
# assembly
# ===========================================================================

# ===========================================================================
# Batch 2 — the two forms that take the last Integrated 3 units to six.
# ===========================================================================

def _g_inverse_variation():
    raws = []
    for k in (12, 18, 24, 30, 36, 48, 60, 72):
        for x1 in (2, 3, 4, 6):
            if k % x1:
                continue
            for x2 in (2, 3, 4, 6, 8, 12):
                if x2 == x1 or k % x2:
                    continue
                y1, y2 = k // x1, k // x2
                raws.append({
                    "statement": ("$y$ varies inversely with $x$. When "
                                  "$x = %d$, $y = %d$. Find $y$ when "
                                  "$x = %d$." % (x1, y1, x2)),
                    "correct": y2,
                    "dvals": [y1, y1 * x2, Rational(y1 * x1, x2 * x2)],
                    "explanation": ("Inverse variation means the PRODUCT "
                                    "stays constant: $xy = %d \\cdot %d = "
                                    "%d$. So at $x = %d$, "
                                    "$y = \\frac{%d}{%d} = %d$. Direct "
                                    "variation would keep the RATIO "
                                    "constant instead, and the two move in "
                                    "opposite directions."
                                    % (x1, y1, k, x2, k, x2, y2)),
                    "check": ["Eq(%d*%d, %d*%d)" % (x1, y1, x2, y2)],
                })
    return raws


def _g_sinusoid_range():
    raws = []
    for A in (2, 3, 4, 5, 6, 7, 8, 9):
        for C in (-6, -3, -1, 0, 2, 4, 5, 10):
            raws.append({
                "statement": ("Find the MAXIMUM value of "
                              "$y = %d\\sin x %s$."
                              % (A, ("+ %d" % C) if C >= 0 else "- %d" % -C)),
                "correct": C + A,
                "dvals": [C - A, A, C],
                "explanation": ("$\\sin x$ never leaves $[-1, 1]$, so "
                                "$%d\\sin x$ never leaves $[-%d, %d]$, and "
                                "adding $%d$ lifts that to $[%d, %d]$. The "
                                "maximum is $%d$ — the midline plus the "
                                "amplitude. The amplitude $%d$ on its own "
                                "is the maximum only when the midline sits "
                                "at zero."
                                % (A, A, A, C, C - A, C + A, C + A, A)),
                "check": ["Eq((%d) + (%d), %d)" % (C, A, C + A)],
            })
            raws.append({
                "statement": ("Find the MINIMUM value of "
                              "$y = %d\\sin x %s$."
                              % (A, ("+ %d" % C) if C >= 0 else "- %d" % -C)),
                "correct": C - A,
                "dvals": [C + A, -A, C],
                "explanation": ("The lowest point sits one amplitude below "
                                "the midline: $%d - %d = %d$. Reading the "
                                "minimum as $-%d$ forgets that the whole "
                                "curve has been lifted to the midline "
                                "$y = %d$." % (C, A, C - A, A, C)),
                "check": ["Eq((%d) - (%d), %d)" % (C, A, C - A)],
            })
    return raws


def build():
    forms = _remapped_forms()

    U4 = "trigonometric-functions"
    forms += [
        form("im3-coterminal", "Coterminal angles", 1, U4,
             "Add or subtract full turns until the angle lands in [0°, 360°).",
             mk_num("im3-cot", _g_coterminal())),
        form("im3-amplitude-period", "Amplitude and period of a sinusoid", 2, U4,
             "Amplitude is |A|; the period of sin(Bx) is 2π/B — B squeezes, never stretches.",
             mk_txt("im3-ap", _g_amplitude_period())),
        form("im3-pythagorean-identity", "The Pythagorean identity with quadrants", 3, U4,
             "sin² + cos² = 1 gives the size; the quadrant gives the sign.",
             mk_txt("im3-pyth", _g_pythagorean_identity())),
        form("im3-sinusoid-range", "Maximum and minimum of a sinusoid", 2, U4,
             "Midline plus or minus the amplitude.",
             mk_num("im3-srange", _g_sinusoid_range())),
    ]

    U2 = "rational-and-radical-functions"
    forms += [
        form("im3-inverse-variation", "Inverse variation", 2, U2,
             "Inverse variation keeps the PRODUCT constant; direct variation keeps the ratio.",
             mk_num("im3-invvar", _g_inverse_variation())),
    ]

    U5 = "function-families-and-inverses"
    forms += [
        form("im3-even-odd", "Even, odd, or neither", 2, U5,
             "Substitute -x: all-even exponents mirror, all-odd flip, mixtures do neither.",
             mk_txt("im3-eo", _g_even_odd())),
    ]

    U7 = "statistical-inference"
    forms += [
        form("im3-sample-estimate", "From sample to population estimate", 1, U7,
             "The sample proportion, scaled to the population — that's what random sampling buys.",
             mk_num("im3-se", _g_sample_estimate())),
        form("im3-empirical-rule", "The 68–95–99.7 rule", 2, U7,
             "Bands hold 68/95/99.7 percent; what's outside splits evenly between two tails.",
             mk_txt("im3-er", _g_empirical_rule())),
        form("im3-z-score", "Computing z-scores", 2, U7,
             "z = (x - μ)/σ counts standard deviations from the mean, sign included.",
             mk_num("im3-z", _g_z_scores())),
        form("im3-simulation-verdict", "Reading a simulation", 2, U7,
             "Observed in under about 5% of simulated trials — doubt the claim, not your luck.",
             mk_txt("im3-sv", _g_simulation_verdict())),
        form("im3-margin-of-error", "The margin of error", 2, U7,
             "MoE ≈ 1/√n, and a poll's honest answer is the interval it builds.",
             mk_txt("im3-moe", _g_margin_of_error())),
        form("im3-sample-size", "Sample size and the square-root law", 3, U7,
             "Halving the margin quadruples the sample — invert 1/√n with care.",
             mk_num("im3-ssz", _g_sample_size())),
    ]

    U8 = "modelling-with-functions"
    forms += [
        form("im3-family-from-table", "Choosing the function family", 1, U8,
             "Constant differences: linear. Constant ratios: exponential. Constant second differences: quadratic.",
             mk_txt("im3-fam", _g_family_from_table())),
        form("im3-model-from-points", "A linear model from two readings", 2, U8,
             "Slope from the two points, intercept from either — then predict.",
             mk_num("im3-mfp", _g_model_from_points())),
        form("im3-residual", "Computing residuals", 2, U8,
             "Residual = actual - predicted; the sign says above or below the model.",
             mk_num("im3-res", _g_residual())),
        form("im3-quadratic-from-vertex", "A parabola from vertex and point", 3, U8,
             "Vertex form hands you h and k; one more point pins a.",
             mk_num("im3-qfv", _g_quadratic_from_vertex())),
    ]

    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    t = build()
    per = {u["id"]: 0 for u in t["units"]}
    lv = {u["id"]: set() for u in t["units"]}
    for f in t["forms"]:
        per[f["unit"]] += len(f["variants"])
        lv[f["unit"]].add(f["level"])
    print("%s: %d forms, %d variants" %
          (t["slug"], len(t["forms"]), sum(len(f["variants"]) for f in t["forms"])))
    for u in t["units"]:
        print("   %-44s %4d  levels %s" %
              (u["id"], per[u["id"]], sorted(lv[u["id"]])))
