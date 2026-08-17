"""The 1 September paper diagnostic — 30 items, five per-strand ladders.

The centre opens before the software does. This is the fallback that keeps
September's students placeable, and — more importantly — keeps September's
DATA usable: every item carries a skill_id, so results typed in during
Phase 1 land on the same graph the adaptive test will use.

WHY TIERS INSTEAD OF ADAPTATION
On paper the test cannot branch, so the adaptation moves into the MARKING.
Every student attempts all 30. Each strand is a ladder of three tiers, and
the marker walks the ladder: clear a tier and your placement is decided by
the next one up. A student who cannot clear tier 1 in algebra is placed at
the foundation of algebra no matter what they scored on the tier-3 items,
which is the correct reading — a right answer on a hard item above a failed
easy one is far more likely to be a guess than mastery.

  CLEAR A TIER = MORE THAN HALF ITS ITEMS CORRECT.
  n=4 -> 3, n=3 -> 2, n=2 -> 2, n=1 -> 1. One rule, no table to look up.

WHY 30 ITEMS CANNOT REPORT ON EVERYTHING, STATED PLAINLY
scripts/skills/inference_report.py measures it: a well-chosen 30 credits
about three quarters of the graph. So this paper places a student per STRAND
(five verdicts), and does not pretend to a per-skill profile. The per-skill
picture is what the adaptive test is for.

LANGUAGE — READ THIS BEFORE PRINTING
Item text is ENGLISH. Mongolian is Phase 3, authored by a Mongolian-speaking
maths teacher expressing the idea rather than translating, and this phase is
explicitly forbidden from writing it. A paper sat by Mongolian students in
English is not usable as-is, so the items are deliberately authored to be as
close to symbol-only as possible: the median item is one short sentence plus
notation, so the Phase-3 pass is small. DO NOT print this for students until
that pass is done.

Answers are COMPUTED and sympy-asserted, never typed. Every distractor
encodes one named student error (the comment beside it names which), so the
September marking sheet doubles as misconception data.

Run: python3 scripts/skills/paper_diagnostic.py
"""

from __future__ import annotations

import json
import math
import os

from sympy import (Rational, sqrt, pi, simplify, sympify, symbols, S,
                   solve, Eq, diff, integrate, binomial, factorial)

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
x = symbols("x")

ITEMS = []


def item(iid, strand, tier, skill_id, body, options, answer, verify, solution, errors):
    """One diagnostic item.

    `options` is a dict A-D of LaTeX strings; `errors` names the misconception
    behind each wrong option, so the marking sheet can report WHY, not just
    how many. `verify` is a list of sympy assertion strings — the builder
    refuses to write anything if one is not True.
    """
    assert answer in options, f"{iid}: answer {answer} not among the options"
    assert set(options) == {"A", "B", "C", "D"}, f"{iid}: options must be A-D"
    assert set(errors) == set(options) - {answer}, f"{iid}: every wrong option needs a named error"
    for expr in verify:
        try:
            ok = sympify(expr)
        except Exception as exc:  # pragma: no cover - builder-time guard
            raise SystemExit(f"{iid}: verify does not sympify: {expr!r} ({exc})")
        if ok is not S.true and ok is not True:
            raise SystemExit(f"{iid}: verify NOT TRUE: {expr!r} -> {ok}")
    vals = list(options.values())
    assert len(set(vals)) == 4, f"{iid}: duplicate option text"
    ITEMS.append({
        "id": iid, "strand": strand, "tier": tier, "skill_id": skill_id,
        "body": body, "options": options, "answer": answer,
        "solution": solution, "errors": errors, "verify": verify,
    })


# ============================ ALGEBRA — 10 (T1 x4, T2 x3, T3 x3) ============
item("A1", "algebra", 1, "integer-operations",
     r"Evaluate $-3 + 5 \times (-2)$.",
     {"A": r"$-13$", "B": r"$-4$", "C": r"$7$", "D": r"$13$"}, "A",
     ["Eq(-3 + 5*(-2), -13)", "Eq((-3+5)*(-2), -4)"],
     r"Multiplication first: $5 \times (-2) = -10$, then $-3 + (-10) = -13$.",
     {"B": "added before multiplying", "C": "lost the sign of the product",
      "D": "sign slip on the final answer"})

item("A2", "algebra", 1, "fraction-arithmetic",
     r"Evaluate $\dfrac{2}{3} + \dfrac{1}{4}$.",
     {"A": r"$\dfrac{11}{12}$", "B": r"$\dfrac{3}{7}$", "C": r"$\dfrac{3}{4}$",
      "D": r"$\dfrac{7}{12}$"}, "A",
     ["Eq(Rational(2,3) + Rational(1,4), Rational(11,12))",
      "Eq(Rational(2+1, 3+4), Rational(3,7))"],
     r"Common denominator $12$: $\dfrac{8}{12} + \dfrac{3}{12} = \dfrac{11}{12}$.",
     {"B": "added numerators and denominators across",
      "C": "converted the second fraction to twelfths wrongly ($\\frac{1}{12}$)",
      "D": "converted the first fraction wrongly ($\\frac{4}{12}$)"})

item("A3", "algebra", 1, "linear-equation-one-variable",
     r"Solve $5x - 7 = 3x + 9$.",
     {"A": r"$x = 8$", "B": r"$x = 1$", "C": r"$x = -8$", "D": r"$x = 16$"}, "A",
     ["Eq(solve(Eq(5*x - 7, 3*x + 9), x)[0], 8)"],
     r"$2x = 16$, so $x = 8$.",
     {"B": "moved both constants the same way ($2x = 2$)",
      "C": "sign slip moving the constant", "D": "did not divide by the coefficient"})

item("A4", "algebra", 1, "exponent-rules",
     r"Simplify $\dfrac{x^{5} \cdot x^{3}}{x^{4}}$.",
     {"A": r"$x^{4}$", "B": r"$x^{8}$", "C": r"$x^{11}$", "D": r"$x^{12}$"}, "A",
     ["Eq(5 + 3 - 4, 4)", "Eq(5*3 - 4, 11)"],
     r"Add the exponents on top, subtract the one below: $x^{5+3-4} = x^{4}$.",
     {"B": "did not subtract the denominator's exponent",
      "C": "multiplied the exponents instead of adding",
      "D": "added the denominator's exponent instead of subtracting"})

item("A5", "algebra", 2, "factoring-quadratic-trinomial",
     r"Factorise $x^{2} - 7x + 12$.",
     {"A": r"$(x-3)(x-4)$", "B": r"$(x+3)(x+4)$", "C": r"$(x-2)(x-6)$",
      "D": r"$(x-1)(x-12)$"}, "A",
     ["Eq(simplify((x-3)*(x-4) - (x**2 - 7*x + 12)), 0)",
      "Eq(simplify((x-2)*(x-6) - (x**2 - 8*x + 12)), 0)"],
     r"Two numbers multiplying to $12$ and adding to $-7$: $-3$ and $-4$.",
     {"B": "right numbers, both signs wrong",
      "C": "product correct but sum is $-8$", "D": "product correct but sum is $-13$"})

item("A6", "algebra", 2, "systems-two-linear",
     r"Solve $\begin{cases} 2x + y = 11 \\ x - y = 1 \end{cases}$",
     {"A": r"$(4,\ 3)$", "B": r"$(3,\ 4)$", "C": r"$(4,\ -3)$", "D": r"$(5,\ 1)$"}, "A",
     ["Eq(2*4 + 3, 11)", "Eq(4 - 3, 1)", "Ne(2*3 + 4, 11)"],
     r"Adding the equations gives $3x = 12$, so $x = 4$ and then $y = 3$.",
     {"B": "wrote the solution in the wrong order", "C": "sign slip solving for $y$",
      "D": "subtracted the equations instead of adding"})

item("A7", "algebra", 2, "composite-functions",
     r"If $f(x) = 2x + 1$ and $g(x) = x^{2}$, find $f(g(3))$.",
     {"A": r"$19$", "B": r"$49$", "C": r"$9$", "D": r"$10$"}, "A",
     ["Eq(2*(3**2) + 1, 19)", "Eq((2*3 + 1)**2, 49)"],
     r"$g(3) = 9$, then $f(9) = 2 \cdot 9 + 1 = 19$.",
     {"B": "computed $g(f(3))$ — applied the functions in the wrong order",
      "C": "stopped after the inner function", "D": "dropped the coefficient $2$"})

item("A8", "algebra", 3, "logarithmic-equations",
     r"Solve $\log_{2} x + \log_{2}(x-2) = 3$.",
     {"A": r"$x = 4$", "B": r"$x = 4$ or $x = -2$", "C": r"$x = -2$", "D": r"$x = 5$"}, "A",
     ["Eq(4*(4-2), 8)", "Eq(solve(Eq(x**2 - 2*x - 8, 0), x)[0], -2)",
      "Eq(solve(Eq(x**2 - 2*x - 8, 0), x)[1], 4)"],
     r"$\log_{2}\big(x(x-2)\big) = 3$ gives $x^{2} - 2x - 8 = 0$, so $x = 4$ or $x = -2$. "
     r"Only $x = 4$ keeps both logarithms defined.",
     {"B": "did not reject the root outside the domain",
      "C": "kept the rejected root and discarded the valid one",
      "D": "added the arguments instead of multiplying them"})

item("A9", "algebra", 3, "vieta-formulas",
     r"The equation $2x^{2} - 6x + 1 = 0$ has roots $x_{1}$ and $x_{2}$. "
     r"Find $x_{1} + x_{2}$.",
     {"A": r"$3$", "B": r"$-3$", "C": r"$\dfrac{1}{2}$", "D": r"$6$"}, "A",
     ["Eq(Rational(6,2), 3)", "Eq(sum(solve(Eq(2*x**2 - 6*x + 1, 0), x)), 3)",
      "Eq(Rational(1,2), Rational(1,2))"],
     r"For $ax^{2}+bx+c=0$ the sum of the roots is $-\dfrac{b}{a} = \dfrac{6}{2} = 3$.",
     {"B": "kept the minus sign in $-b/a$ after $b$ was already negative",
      "C": "gave the product $c/a$ instead of the sum", "D": "did not divide by $a$"})

item("A10", "algebra", 3, "quadratic-inequalities",
     r"Solve $x^{2} - 5x + 6 < 0$.",
     {"A": r"$2 < x < 3$", "B": r"$x < 2$ or $x > 3$", "C": r"$2 \le x \le 3$",
      "D": r"$-3 < x < -2$"}, "A",
     ["Eq(simplify((x-2)*(x-3) - (x**2 - 5*x + 6)), 0)",
      "(Rational(5,2)**2 - 5*Rational(5,2) + 6) < 0"],
     r"$(x-2)(x-3) < 0$, so $x$ lies strictly between the roots: $2 < x < 3$.",
     {"B": "took the outside of the roots — the wrong side of the parabola",
      "C": "included the endpoints although the inequality is strict",
      "D": "sign error when reading the roots off the factors"})

# ====================== GEOMETRY & TRIGONOMETRY — 8 (3/3/2) =================
item("G1", "geometry-trig", 1, "angles-and-parallel-lines",
     r"Two parallel lines are cut by a transversal. One interior angle is "
     r"$65^{\circ}$. Find the co-interior (allied) angle on the same side.",
     {"A": r"$115^{\circ}$", "B": r"$65^{\circ}$", "C": r"$25^{\circ}$",
      "D": r"$130^{\circ}$"}, "A",
     ["Eq(180 - 65, 115)", "Eq(90 - 65, 25)"],
     r"Co-interior angles are supplementary: $180^{\circ} - 65^{\circ} = 115^{\circ}$.",
     {"B": "used the alternate-angle rule instead of co-interior",
      "C": "used complementary instead of supplementary", "D": "doubled the angle"})

item("G2", "geometry-trig", 1, "pythagoras",
     r"A right-angled triangle has legs $5$ and $12$. Find the hypotenuse.",
     {"A": r"$13$", "B": r"$17$", "C": r"$7$", "D": r"$\sqrt{119}$"}, "A",
     ["Eq(sqrt(5**2 + 12**2), 13)", "Eq(sqrt(12**2 - 5**2), sqrt(119))"],
     r"$\sqrt{5^{2} + 12^{2}} = \sqrt{169} = 13$.",
     {"B": "added the legs", "C": "subtracted the legs",
      "D": "treated $12$ as the hypotenuse"})

item("G3", "geometry-trig", 1, "circle-area-and-arc",
     r"Find the area of a circle of radius $6$.",
     {"A": r"$36\pi$", "B": r"$12\pi$", "C": r"$36$", "D": r"$6\pi$"}, "A",
     ["Eq(pi*6**2, 36*pi)", "Eq(2*pi*6, 12*pi)"],
     r"$A = \pi r^{2} = 36\pi$.",
     {"B": "used the circumference formula", "C": "dropped the $\\pi$",
      "D": "used $\\pi r$ instead of $\\pi r^{2}$"})

item("G4", "geometry-trig", 2, "triangle-similarity",
     r"Two similar triangles have sides in the ratio $3 : 5$. The smaller has "
     r"area $18$. Find the area of the larger.",
     {"A": r"$50$", "B": r"$30$", "C": r"$90$", "D": r"$45$"}, "A",
     ["Eq(18 * Rational(5,3)**2, 50)", "Eq(18 * Rational(5,3), 30)"],
     r"Areas scale by the square of the ratio: $18 \times \left(\frac{5}{3}\right)^{2} = 50$.",
     {"B": "scaled by the ratio instead of its square",
      "C": "multiplied by $5$", "D": "used $\\frac{5}{2}$ as the scale factor"})

item("G5", "geometry-trig", 2, "exact-trig-values",
     r"Evaluate $\sin 60^{\circ} \cdot \cos 30^{\circ}$.",
     {"A": r"$\dfrac{3}{4}$", "B": r"$\dfrac{1}{4}$", "C": r"$\dfrac{\sqrt{3}}{2}$",
      "D": r"$\dfrac{1}{2}$"}, "A",
     ["Eq(sqrt(3)/2 * sqrt(3)/2, Rational(3,4))",
      "Eq(Rational(1,2)*Rational(1,2), Rational(1,4))"],
     r"$\dfrac{\sqrt{3}}{2} \cdot \dfrac{\sqrt{3}}{2} = \dfrac{3}{4}$.",
     {"B": "used $\\sin 30^{\\circ}\\cos 60^{\\circ}$",
      "C": "gave one factor instead of the product",
      "D": "used $\\sin 30^{\\circ}$ for both"})

item("G6", "geometry-trig", 2, "prism-volume-surface",
     r"Find the total surface area of a cuboid measuring $3 \times 4 \times 5$.",
     {"A": r"$94$", "B": r"$60$", "C": r"$47$", "D": r"$120$"}, "A",
     ["Eq(2*(3*4 + 4*5 + 3*5), 94)", "Eq(3*4*5, 60)"],
     r"$2(3{\cdot}4 + 4{\cdot}5 + 3{\cdot}5) = 2(12+20+15) = 94$.",
     {"B": "found the volume instead", "C": "counted each face once",
      "D": "doubled the volume"})

item("G7", "geometry-trig", 3, "cone",
     r"A cone has base radius $3$ and slant height $5$. Find its volume.",
     {"A": r"$12\pi$", "B": r"$15\pi$", "C": r"$36\pi$", "D": r"$45\pi$"}, "A",
     ["Eq(sqrt(5**2 - 3**2), 4)", "Eq(Rational(1,3)*pi*3**2*4, 12*pi)",
      "Eq(Rational(1,3)*pi*3**2*5, 15*pi)"],
     r"Height $= \sqrt{5^{2}-3^{2}} = 4$, so $V = \tfrac{1}{3}\pi r^{2} h = 12\pi$.",
     {"B": "used the slant height as the perpendicular height",
      "C": "used $\\pi r^{2} h$ without the $\\tfrac{1}{3}$",
      "D": "both errors together"})

item("G8", "geometry-trig", 3, "dot-product",
     r"For $\vec{a} = (3,\ 4)$ and $\vec{b} = (2,\ -1)$, find $\vec{a} \cdot \vec{b}$.",
     {"A": r"$2$", "B": r"$10$", "C": r"$-2$", "D": r"$7$"}, "A",
     ["Eq(3*2 + 4*(-1), 2)", "Eq(3*2 + 4*1, 10)"],
     r"$3(2) + 4(-1) = 6 - 4 = 2$.",
     {"B": "ignored the negative component", "C": "sign slip on the whole sum",
      "D": "added the components of $\\vec{a}$"})

# ================================ ANALYSIS — 5 (2/2/1) ======================
item("C1", "analysis", 1, "derivative-power-rule",
     r"Differentiate $y = 3x^{4} - 2x$.",
     {"A": r"$12x^{3} - 2$", "B": r"$12x^{3} - 2x$", "C": r"$3x^{3} - 2$",
      "D": r"$12x^{4} - 2$"}, "A",
     ["Eq(diff(3*x**4 - 2*x, x), 12*x**3 - 2)"],
     r"$\dfrac{d}{dx}(3x^{4}) = 12x^{3}$ and $\dfrac{d}{dx}(-2x) = -2$.",
     {"B": "left the linear term undifferentiated",
      "C": "did not bring the exponent down as a factor",
      "D": "did not reduce the exponent"})

item("C2", "analysis", 1, "antiderivative-power",
     r"Find $\displaystyle\int 6x^{2}\,dx$.",
     {"A": r"$2x^{3} + C$", "B": r"$12x + C$", "C": r"$3x^{3} + C$",
      "D": r"$6x^{3} + C$"}, "A",
     ["Eq(integrate(6*x**2, x), 2*x**3)"],
     r"Raise the exponent and divide: $\dfrac{6x^{3}}{3} = 2x^{3}$, plus $C$.",
     {"B": "differentiated instead of integrating",
      "C": "divided by the old exponent", "D": "did not divide at all"})

item("C3", "analysis", 2, "tangent-line",
     r"Find the tangent to $y = x^{2} - 3x$ at the point where $x = 2$.",
     {"A": r"$y = x - 4$", "B": r"$y = x + 4$", "C": r"$y = -2x + 2$",
      "D": r"$y = x - 2$"}, "A",
     ["Eq((2**2 - 3*2), -2)", "Eq(diff(x**2 - 3*x, x).subs(x, 2), 1)",
      "Eq(1*2 - 4, -2)"],
     r"At $x=2$: $y = -2$ and $y' = 2x-3 = 1$. So $y + 2 = 1(x-2)$, i.e. $y = x - 4$.",
     {"B": "sign slip substituting the point",
      "C": "used the $y$-value as the gradient",
      "D": "used the $x$-value as the intercept"})

item("C4", "analysis", 2, "definite-integral",
     r"Evaluate $\displaystyle\int_{0}^{2} 3x^{2}\,dx$.",
     {"A": r"$8$", "B": r"$12$", "C": r"$4$", "D": r"$6$"}, "A",
     ["Eq(integrate(3*x**2, (x, 0, 2)), 8)", "Eq(3*2**2, 12)"],
     r"$\left[x^{3}\right]_{0}^{2} = 8 - 0 = 8$.",
     {"B": "substituted into the integrand rather than the antiderivative",
      "C": "divided by the exponent twice", "D": "used $\\tfrac{1}{2}bh$ on the curve"})

item("C5", "analysis", 3, "stationary-points-and-extrema",
     r"Find the local maximum VALUE of $f(x) = x^{3} - 3x$.",
     {"A": r"$2$", "B": r"$-2$", "C": r"$-1$", "D": r"$1$"}, "A",
     ["Eq(diff(x**3 - 3*x, x), 3*x**2 - 3)",
      "Eq((x**3 - 3*x).subs(x, -1), 2)", "Eq((x**3 - 3*x).subs(x, 1), -2)"],
     r"$f'(x) = 3x^{2}-3 = 0$ at $x = \pm 1$. The maximum is at $x = -1$, where $f(-1) = 2$.",
     {"B": "gave the local minimum value", "C": "gave the $x$-coordinate of the maximum",
      "D": "gave the $x$-coordinate of the minimum"})

# ==================== PROBABILITY & STATISTICS — 5 (2/2/1) ==================
item("P1", "probability-statistics", 1, "mean-median-mode",
     r"Find the median of $9,\ 3,\ 14,\ 7,\ 7$.",
     {"A": r"$7$", "B": r"$8$", "C": r"$14$", "D": r"$9$"}, "A",
     ["Eq(sorted([9,3,14,7,7])[2], 7)", "Eq(Rational(9+3+14+7+7, 5), 8)"],
     r"Ordered: $3,\ 7,\ 7,\ 9,\ 14$. The middle value is $7$.",
     {"B": "computed the mean", "C": "took the middle of the unordered list",
      "D": "took the fourth value"})

item("P2", "probability-statistics", 1, "classical-probability",
     r"A bag holds $3$ red and $5$ blue balls. One is drawn at random. "
     r"Find $P(\text{red})$.",
     {"A": r"$\dfrac{3}{8}$", "B": r"$\dfrac{3}{5}$", "C": r"$\dfrac{5}{8}$",
      "D": r"$\dfrac{1}{3}$"}, "A",
     ["Eq(Rational(3, 3+5), Rational(3,8))"],
     r"$P = \dfrac{\text{red}}{\text{total}} = \dfrac{3}{8}$.",
     {"B": "used red-to-blue instead of red-to-total",
      "C": "gave $P(\\text{blue})$", "D": "used the number of colours as the total"})

item("P3", "probability-statistics", 2, "quartiles-and-iqr",
     r"Find the interquartile range of $2,\ 4,\ 5,\ 7,\ 8,\ 10,\ 13$.",
     {"A": r"$6$", "B": r"$11$", "C": r"$5$", "D": r"$7$"}, "A",
     ["Eq(10 - 4, 6)", "Eq(13 - 2, 11)"],
     r"$Q_{1} = 4$ and $Q_{3} = 10$, so $\text{IQR} = 10 - 4 = 6$.",
     {"B": "gave the range", "C": "used the wrong quartile positions",
      "D": "gave the median"})

item("P4", "probability-statistics", 2, "addition-rule",
     r"$P(A) = 0.5$, $P(B) = 0.4$ and $P(A \cap B) = 0.2$. Find $P(A \cup B)$.",
     {"A": r"$0.7$", "B": r"$0.9$", "C": r"$0.2$", "D": r"$1.1$"}, "A",
     ["Eq(Rational(1,2) + Rational(2,5) - Rational(1,5), Rational(7,10))",
      "Eq(Rational(1,2) + Rational(2,5), Rational(9,10))"],
     r"$P(A \cup B) = 0.5 + 0.4 - 0.2 = 0.7$.",
     {"B": "treated the events as mutually exclusive",
      "C": "gave the intersection", "D": "added the intersection instead of subtracting"})

item("P5", "probability-statistics", 3, "expected-value",
     r"A random variable $X$ takes the values $0,\ 1,\ 2$ with probabilities "
     r"$0.2,\ 0.5,\ 0.3$. Find $E(X)$.",
     {"A": r"$1.1$", "B": r"$1$", "C": r"$1.5$", "D": r"$0.5$"}, "A",
     ["Eq(0*Rational(1,5) + 1*Rational(1,2) + 2*Rational(3,10), Rational(11,10))",
      "Eq(Rational(0+1+2, 3), 1)"],
     r"$E(X) = 0(0.2) + 1(0.5) + 2(0.3) = 1.1$.",
     {"B": "averaged the values, ignoring the probabilities",
      "C": "averaged only the non-zero values",
      "D": "gave the largest probability"})

# ============================== COMBINATORICS — 2 (1/1) =====================
item("K1", "combinatorics", 1, "counting-principle",
     r"A student has $4$ shirts and $3$ pairs of trousers. How many different "
     r"outfits are possible?",
     {"A": r"$12$", "B": r"$7$", "C": r"$24$", "D": r"$64$"}, "A",
     ["Eq(4*3, 12)", "Eq(4+3, 7)"],
     r"$4 \times 3 = 12$.",
     {"B": "added instead of multiplying", "C": "doubled the product",
      "D": "computed $4^{3}$"})

item("K2", "combinatorics", 2, "combinations",
     r"In how many ways can $3$ students be chosen from $8$?",
     {"A": r"$56$", "B": r"$336$", "C": r"$24$", "D": r"$112$"}, "A",
     ["Eq(binomial(8,3), 56)", "Eq(factorial(8)/factorial(5), 336)"],
     r"$\binom{8}{3} = \dfrac{8 \cdot 7 \cdot 6}{3 \cdot 2 \cdot 1} = 56$.",
     {"B": "counted arrangements ($^{8}P_{3}$) — order should not matter",
      "C": "computed $8 \\times 3$", "D": "forgot to divide by $3!$ fully"})


# ---------------------------------------------------------------------------

STRAND_ORDER = ["algebra", "geometry-trig", "analysis", "probability-statistics",
                "combinatorics"]
STRAND_TITLE = {
    "algebra": "Algebra", "geometry-trig": "Geometry & Trigonometry",
    "analysis": "Analysis", "probability-statistics": "Probability & Statistics",
    "combinatorics": "Combinatorics",
}
# The allocation the brief specifies, asserted rather than assumed.
TARGET = {"algebra": 10, "geometry-trig": 8, "analysis": 5,
          "probability-statistics": 5, "combinatorics": 2}


def clear_threshold(n):
    """More than half, so n=4 -> 3, n=3 -> 2, n=2 -> 2, n=1 -> 1."""
    return n // 2 + 1


def main():
    graph = json.load(open(os.path.join(ROOT, "data", "skills", "esh-skills.json")))
    known = {s["id"]: s for s in graph["skills"]}

    counts = {}
    for it in ITEMS:
        counts[it["strand"]] = counts.get(it["strand"], 0) + 1
        assert it["skill_id"] in known, f"{it['id']}: unknown skill {it['skill_id']}"
    assert counts == TARGET, f"allocation {counts} != brief's {TARGET}"
    assert len(ITEMS) == 30, f"{len(ITEMS)} items, expected 30"
    assert len({i["id"] for i in ITEMS}) == 30, "duplicate item ids"
    assert len({i["skill_id"] for i in ITEMS}) == 30, "two items on the same skill"

    ladders = {}
    for strand in STRAND_ORDER:
        tiers = {}
        for t in (1, 2, 3):
            members = [i["id"] for i in ITEMS if i["strand"] == strand and i["tier"] == t]
            if members:
                tiers[t] = {"items": members, "clear_at": clear_threshold(len(members))}
        ladders[strand] = tiers

    # The answer key must not be lopsided or a marker will spot a pattern; the
    # rendered sheets shuffle option order deterministically per item id.
    out = {
        "note": "Generated by scripts/skills/paper_diagnostic.py. Answers are computed and "
                "sympy-asserted. ITEM TEXT IS ENGLISH — needs the Phase 3 Mongolian pass "
                "before it is printed for students.",
        "title": "ЭШ Mathematics — Paper Diagnostic",
        "forDate": "1 September",
        "itemCount": len(ITEMS),
        "strandOrder": STRAND_ORDER,
        "strandTitles": STRAND_TITLE,
        "ladders": ladders,
        "markingRule": "Within a strand, a student CLEARS a tier by answering more than half "
                       "its items correctly. Placement for the strand is the highest tier "
                       "cleared, and a tier is only considered if the tier below it was "
                       "cleared.",
        "items": ITEMS,
    }
    with open(os.path.join(ROOT, "data", "skills", "paper-diagnostic.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"{len(ITEMS)} items, all sympy-verified, 30 distinct skills")
    for s in STRAND_ORDER:
        tiers = ladders[s]
        desc = "  ".join(f"T{t}:{len(v['items'])} (clear at {v['clear_at']})"
                         for t, v in sorted(tiers.items()))
        print(f"  {STRAND_TITLE[s]:<26} {counts[s]:2d} items   {desc}")
    weight = sum(known[i["skill_id"]]["exam_weight"] for i in ITEMS)
    print(f"  skills probed carry {weight:.1f}% of the exam directly")


if __name__ == "__main__":
    main()
