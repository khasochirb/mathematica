"""Gap items, batch A — ranks 1-20 by exam weight (0.86% down to 0.66%).

Together these twenty skills carry 14.87 of the 36.57 percentage points the
adaptive test currently cannot probe: 41% of the gap in the first batch,
which is why they are first.

Every item here is NEW, not a copy of the paper diagnostic's item on the same
skill. Six of these skills appear on that paper (pythagoras, triangle-area's
neighbours, factoring, quadratic-by-factoring, quadratic-inequalities,
systems) and a student who sat the diagnostic in September must not meet the
identical question again in the adaptive test in October.
"""

from item_bank import I

# ============ 1. counting-based-probability — 0.86% ========================
I("counting-based-probability", 2,
  r"A committee of $2$ is chosen at random from $3$ boys and $2$ girls. "
  r"Find the probability that both are girls.",
  {"A": r"$\dfrac{1}{10}$", "B": r"$\dfrac{2}{5}$", "C": r"$\dfrac{1}{5}$",
   "D": r"$\dfrac{3}{10}$"}, "A",
  ["Eq(binomial(2,2)/binomial(5,2), Rational(1,10))", "Eq(binomial(5,2), 10)"],
  r"There is $\binom{2}{2}=1$ way to choose both girls out of $\binom{5}{2}=10$ "
  r"committees, so $P=\dfrac{1}{10}$.",
  {"B": "used the proportion of girls, $\\tfrac{2}{5}$, ignoring that two are drawn",
   "C": "divided by $5$ instead of $\\binom{5}{2}$",
   "D": "counted ordered pairs on top but unordered below"})
I("counting-based-probability", 3,
  r"Three balls are drawn at random from a bag holding $5$ red and $4$ blue. "
  r"Find the probability that exactly two are red.",
  {"A": r"$\dfrac{10}{21}$", "B": r"$\dfrac{5}{42}$", "C": r"$\dfrac{5}{21}$",
   "D": r"$\dfrac{2}{7}$"}, "A",
  ["Eq(binomial(5,2)*binomial(4,1)/binomial(9,3), Rational(10,21))",
   "Eq(binomial(9,3), 84)", "Eq(binomial(5,2)*binomial(4,1), 40)"],
  r"$\dfrac{\binom{5}{2}\binom{4}{1}}{\binom{9}{3}} = \dfrac{10 \cdot 4}{84} "
  r"= \dfrac{10}{21}$.",
  {"B": "forgot to choose the third ball from the blues",
   "C": "chose two blues instead of one",
   "D": "used $\\binom{4}{2}$ for the blue ball"})
I("counting-based-probability", 4,
  r"The letters $A$, $B$, $C$, $D$ are arranged at random in a row. Find the "
  r"probability that $A$ stands immediately before $B$.",
  {"A": r"$\dfrac{1}{4}$", "B": r"$\dfrac{1}{2}$", "C": r"$\dfrac{1}{12}$",
   "D": r"$\dfrac{1}{3}$"}, "A",
  ["Eq(Rational(factorial(3), factorial(4)), Rational(1,4))", "Eq(factorial(4), 24)"],
  r"Glue $AB$ into one block: $3! = 6$ arrangements out of $4! = 24$, so "
  r"$P = \dfrac{6}{24} = \dfrac{1}{4}$.",
  {"B": "answered '$A$ somewhere before $B$', which is $\\tfrac12$",
   "C": "counted only $2$ favourable arrangements",
   "D": "divided the four positions rather than counting arrangements"},
  check=lambda: (lambda P: sum(1 for p in P if p.index("A") + 1 == p.index("B")) == 6)(
      __import__("itertools").permutations("ABCD")) )

# ============ 2. independent-events — 0.86% ================================
I("independent-events", 2,
  r"$A$ and $B$ are independent with $P(A)=0.6$ and $P(B)=0.5$. Find $P(A \cap B)$.",
  {"A": r"$0.3$", "B": r"$1.1$", "C": r"$0.1$", "D": r"$0.8$"}, "A",
  ["Eq(Rational(3,5)*Rational(1,2), Rational(3,10))"],
  r"For independent events $P(A \cap B) = P(A)P(B) = 0.6 \times 0.5 = 0.3$.",
  {"B": "added the probabilities", "C": "subtracted the probabilities",
   "D": "computed the union instead of the intersection"})
I("independent-events", 3,
  r"A fair coin is tossed three times. Find the probability of at least one head.",
  {"A": r"$\dfrac{7}{8}$", "B": r"$\dfrac{1}{8}$", "C": r"$\dfrac{1}{2}$",
   "D": r"$\dfrac{3}{8}$"}, "A",
  ["Eq(1 - Rational(1,2)**3, Rational(7,8))"],
  r"$P(\text{no head}) = \left(\tfrac12\right)^3 = \tfrac18$, so "
  r"$P(\text{at least one}) = 1 - \tfrac18 = \tfrac78$.",
  {"B": "gave the probability of no heads",
   "C": "answered for a single toss",
   "D": "gave the probability of exactly one head"})
I("independent-events", 4,
  r"$A$ and $B$ are independent, $P(A)=0.4$ and $P(A \cup B)=0.7$. Find $P(B)$.",
  {"A": r"$0.5$", "B": r"$0.3$", "C": r"$0.75$", "D": r"$0.42$"}, "A",
  ["Eq(Rational(2,5) + Rational(1,2) - Rational(2,5)*Rational(1,2), Rational(7,10))",
   "Eq(solve(Eq(Rational(2,5) + symbols('p') - Rational(2,5)*symbols('p'), Rational(7,10)), "
   "symbols('p'))[0], Rational(1,2))"],
  r"$P(A \cup B) = P(A) + P(B) - P(A)P(B)$, so $0.7 = 0.4 + 0.6\,P(B)$ and "
  r"$P(B) = 0.5$.",
  {"B": "treated the events as mutually exclusive",
   "C": "divided $0.3$ by $0.4$", "D": "multiplied instead of solving"})

# ============ 3. sample-space-and-events — 0.86% ===========================
I("sample-space-and-events", 2,
  r"Two fair dice are thrown. How many outcomes are in the sample space?",
  {"A": r"$36$", "B": r"$12$", "C": r"$6$", "D": r"$21$"}, "A",
  ["Eq(6*6, 36)"],
  r"Each die has $6$ faces and the throws are separate, so $6 \times 6 = 36$.",
  {"B": "added the two dice", "C": "counted one die only",
   "D": "counted unordered pairs"},
  check=lambda: len([(a, b) for a in range(1, 7) for b in range(1, 7)]) == 36)
I("sample-space-and-events", 3,
  r"Two fair dice are thrown. Find the probability that the total is $7$.",
  {"A": r"$\dfrac{1}{6}$", "B": r"$\dfrac{5}{36}$", "C": r"$\dfrac{7}{36}$",
   "D": r"$\dfrac{1}{12}$"}, "A",
  ["Eq(Rational(6,36), Rational(1,6))"],
  r"Six of the $36$ outcomes total $7$, so $P = \dfrac{6}{36} = \dfrac16$.",
  {"B": "counted five favourable outcomes", "C": "used the total as the count",
   "D": "counted only three favourable outcomes"},
  check=lambda: sum(1 for a in range(1, 7) for b in range(1, 7) if a + b == 7) == 6)
I("sample-space-and-events", 4,
  r"A coin is tossed until a head appears or three tosses have been made. "
  r"How many outcomes are in the sample space?",
  {"A": r"$4$", "B": r"$8$", "C": r"$3$", "D": r"$6$"}, "A",
  ["Eq(1 + 1 + 1 + 1, 4)"],
  r"The outcomes are $H$, $TH$, $TTH$ and $TTT$ — the process stops early on a "
  r"head, so there are $4$, not $2^3$.",
  {"B": "counted all three-toss sequences, ignoring the stopping rule",
   "C": "forgot the all-tails outcome", "D": "counted tosses rather than outcomes"},
  check=lambda: len(["H", "TH", "TTH", "TTT"]) == 4)

# ============ 4. triangle-angle-sum — 0.86% ================================
I("triangle-angle-sum", 2,
  r"Two angles of a triangle are $47^{\circ}$ and $68^{\circ}$. Find the third.",
  {"A": r"$65^{\circ}$", "B": r"$115^{\circ}$", "C": r"$85^{\circ}$",
   "D": r"$45^{\circ}$"}, "A",
  ["Eq(180 - 47 - 68, 65)", "Eq(47 + 68, 115)"],
  r"$180^{\circ} - 47^{\circ} - 68^{\circ} = 65^{\circ}$.",
  {"B": "gave the sum of the two known angles",
   "C": "used $200^{\\circ}$ as the angle sum", "D": "used $160^{\\circ}$ as the angle sum"})
I("triangle-angle-sum", 3,
  r"In an isosceles triangle the apex angle is $34^{\circ}$. Find one base angle.",
  {"A": r"$73^{\circ}$", "B": r"$146^{\circ}$", "C": r"$56^{\circ}$",
   "D": r"$63^{\circ}$"}, "A",
  ["Eq(Rational(180 - 34, 2), 73)", "Eq(34 + 73 + 73, 180)"],
  r"The two base angles are equal: $\dfrac{180^{\circ}-34^{\circ}}{2} = 73^{\circ}$.",
  {"B": "gave the sum of both base angles",
   "C": "took the complement of the apex angle",
   "D": "halved $180^{\\circ}$ then subtracted $27^{\\circ}$"})
I("triangle-angle-sum", 4,
  r"An exterior angle of a triangle is $115^{\circ}$ and one of the two "
  r"non-adjacent interior angles is $42^{\circ}$. Find the other.",
  {"A": r"$73^{\circ}$", "B": r"$23^{\circ}$", "C": r"$65^{\circ}$",
   "D": r"$138^{\circ}$"}, "A",
  ["Eq(115 - 42, 73)", "Eq(180 - 115, 65)"],
  r"An exterior angle equals the sum of the two non-adjacent interior angles, "
  r"so the other is $115^{\circ} - 42^{\circ} = 73^{\circ}$.",
  {"B": "subtracted from the adjacent interior angle instead",
   "C": "gave the adjacent interior angle",
   "D": "subtracted $42^{\\circ}$ from $180^{\\circ}$"})

# ============ 5. factoring-quadratic-trinomial — 0.83% =====================
I("factoring-quadratic-trinomial", 2,
  r"Factorise $x^{2} + 9x + 20$.",
  {"A": r"$(x+4)(x+5)$", "B": r"$(x+2)(x+10)$", "C": r"$(x-4)(x-5)$",
   "D": r"$(x+1)(x+20)$"}, "A",
  ["Eq(simplify((x+4)*(x+5) - (x**2 + 9*x + 20)), 0)",
   "Eq(simplify((x+2)*(x+10) - (x**2 + 12*x + 20)), 0)"],
  r"Two numbers with product $20$ and sum $9$: $4$ and $5$.",
  {"B": "product correct, sum is $12$", "C": "right numbers, wrong signs",
   "D": "product correct, sum is $21$"})
I("factoring-quadratic-trinomial", 3,
  r"Factorise $2x^{2} - 7x + 3$.",
  {"A": r"$(2x-1)(x-3)$", "B": r"$(2x-3)(x-1)$", "C": r"$(2x+1)(x+3)$",
   "D": r"$(x-1)(x-3)$"}, "A",
  ["Eq(simplify((2*x-1)*(x-3) - (2*x**2 - 7*x + 3)), 0)",
   "Eq(simplify((2*x-3)*(x-1) - (2*x**2 - 5*x + 3)), 0)"],
  r"Split $-7x$ as $-x - 6x$: $2x^{2} - x - 6x + 3 = x(2x-1) - 3(2x-1) = (2x-1)(x-3)$.",
  {"B": "swapped the constants — this expands to $-5x$",
   "C": "both signs wrong", "D": "dropped the leading coefficient"})
I("factoring-quadratic-trinomial", 4,
  r"Factorise $6x^{2} + x - 12$.",
  {"A": r"$(3x-4)(2x+3)$", "B": r"$(3x+4)(2x-3)$", "C": r"$(6x-4)(x+3)$",
   "D": r"$(3x-2)(2x+6)$"}, "A",
  ["Eq(simplify((3*x-4)*(2*x+3) - (6*x**2 + x - 12)), 0)",
   "Eq(simplify((3*x+4)*(2*x-3) - (6*x**2 - x - 12)), 0)"],
  r"Find two numbers with product $6 \cdot (-12) = -72$ and sum $1$: $9$ and $-8$. "
  r"Then $6x^{2} + 9x - 8x - 12 = 3x(2x+3) - 4(2x+3) = (3x-4)(2x+3)$.",
  {"B": "signs swapped — this gives the middle term $-x$",
   "C": "expands to $6x^{2}+14x-12$", "D": "expands to $6x^{2}+14x-12$ as well"})

# ============ 6. area-under-curve — 0.80% ==================================
I("area-under-curve", 2,
  r"Find the area between $y = x^{2}$ and the $x$-axis from $x=0$ to $x=3$.",
  {"A": r"$9$", "B": r"$27$", "C": r"$3$", "D": r"$18$"}, "A",
  ["Eq(integrate(x**2, (x, 0, 3)), 9)"],
  r"$\displaystyle\int_{0}^{3} x^{2}\,dx = \left[\tfrac{x^{3}}{3}\right]_{0}^{3} = 9$.",
  {"B": "forgot to divide by $3$", "C": "evaluated the integrand at $x=3$... then divided by $9$",
   "D": "used $\\tfrac{x^{3}}{3}$ but doubled it"})
I("area-under-curve", 3,
  r"Find the area enclosed between $y = 4 - x^{2}$ and the $x$-axis.",
  {"A": r"$\dfrac{32}{3}$", "B": r"$\dfrac{16}{3}$", "C": r"$16$", "D": r"$8$"}, "A",
  ["Eq(integrate(4 - x**2, (x, -2, 2)), Rational(32,3))",
   "Eq(solve(Eq(4 - x**2, 0), x)[0], -2)"],
  r"The curve meets the axis at $x = \pm 2$, so the area is "
  r"$\displaystyle\int_{-2}^{2}(4-x^{2})\,dx = \dfrac{32}{3}$.",
  {"B": "integrated from $0$ to $2$ only", "C": "used the rectangle $4 \\times 4$",
   "D": "used $\\tfrac12 \\times 4 \\times 4$"})
I("area-under-curve", 4,
  r"Find the total area between $y = x^{2} - 4$ and the $x$-axis from $x=0$ to $x=3$.",
  {"A": r"$\dfrac{23}{3}$", "B": r"$-3$", "C": r"$\dfrac{16}{3}$", "D": r"$\dfrac{7}{3}$"},
  "A",
  # sympy will not evaluate integrate(Abs(...)) in closed form, and forcing it
  # would hide the point: the AREA is the two pieces added with the sign of the
  # lower one flipped. Asserting the pieces separately says exactly that.
  ["Eq(-integrate(x**2 - 4, (x, 0, 2)) + integrate(x**2 - 4, (x, 2, 3)), Rational(23,3))",
   "Eq(integrate(x**2 - 4, (x, 0, 3)), -3)",
   "Eq(-integrate(x**2 - 4, (x, 0, 2)), Rational(16,3))",
   "Eq(integrate(x**2 - 4, (x, 2, 3)), Rational(7,3))"],
  r"The curve is below the axis on $[0,2]$ and above on $[2,3]$, so the AREA is "
  r"$\left|\int_{0}^{2}\right| + \int_{2}^{3} = \dfrac{16}{3} + \dfrac{7}{3} = \dfrac{23}{3}$.",
  {"B": "integrated straight through — the signed value, not the area",
   "C": "took only the part below the axis",
   "D": "took only the part above the axis"})

# ============ 7. chain-rule — 0.80% ========================================
I("chain-rule", 2,
  r"Differentiate $y = (3x + 1)^{4}$.",
  {"A": r"$12(3x+1)^{3}$", "B": r"$4(3x+1)^{3}$", "C": r"$12(3x+1)^{4}$",
   "D": r"$3(3x+1)^{3}$"}, "A",
  ["Eq(diff((3*x + 1)**4, x), 12*(3*x + 1)**3)"],
  r"$4(3x+1)^{3} \cdot 3 = 12(3x+1)^{3}$.",
  {"B": "forgot the derivative of the inside", "C": "did not reduce the power",
   "D": "used only the inside derivative"})
I("chain-rule", 3,
  r"Differentiate $y = \sqrt{x^{2}+9}$.",
  {"A": r"$\dfrac{x}{\sqrt{x^{2}+9}}$", "B": r"$\dfrac{1}{2\sqrt{x^{2}+9}}$",
   "C": r"$\dfrac{2x}{\sqrt{x^{2}+9}}$", "D": r"$\dfrac{x}{2\sqrt{x^{2}+9}}$"}, "A",
  ["Eq(simplify(diff(sqrt(x**2 + 9), x) - x/sqrt(x**2 + 9)), 0)"],
  r"$\dfrac{1}{2\sqrt{x^{2}+9}} \cdot 2x = \dfrac{x}{\sqrt{x^{2}+9}}$.",
  {"B": "forgot the inside derivative $2x$", "C": "did not cancel the $2$",
   "D": "cancelled the $2$ from the wrong place"})
I("chain-rule", 4,
  r"Differentiate $y = \sin^{3}(2x)$.",
  {"A": r"$6\sin^{2}(2x)\cos(2x)$", "B": r"$3\sin^{2}(2x)\cos(2x)$",
   "C": r"$6\sin^{2}(2x)$", "D": r"$3\cos^{3}(2x)$"}, "A",
  ["Eq(simplify(diff(sin(2*x)**3, x) - 6*sin(2*x)**2*cos(2*x)), 0)"],
  r"Two layers: $3\sin^{2}(2x) \cdot \cos(2x) \cdot 2 = 6\sin^{2}(2x)\cos(2x)$.",
  {"B": "missed the innermost factor $2$", "C": "did not differentiate the sine",
   "D": "differentiated the power and the sine together"})

# ============ 8. derivative-product-quotient — 0.80% =======================
I("derivative-product-quotient", 2,
  r"Differentiate $y = x^{2}\,e^{x}$.",
  {"A": r"$(x^{2}+2x)e^{x}$", "B": r"$2xe^{x}$", "C": r"$(x^{2}-2x)e^{x}$",
   "D": r"$2x e^{x} + x^{2}$"}, "A",
  ["Eq(simplify(diff(x**2*exp(x), x) - (x**2 + 2*x)*exp(x)), 0)"],
  r"$2x\,e^{x} + x^{2}e^{x} = (x^{2}+2x)e^{x}$.",
  {"B": "differentiated the two factors separately and multiplied",
   "C": "sign error in the product rule",
   "D": "did not differentiate $e^{x}$ in the second term"})
I("derivative-product-quotient", 3,
  r"Differentiate $y = \dfrac{x}{x+1}$.",
  {"A": r"$\dfrac{1}{(x+1)^{2}}$", "B": r"$\dfrac{-1}{(x+1)^{2}}$", "C": r"$1$",
   "D": r"$\dfrac{2x+1}{(x+1)^{2}}$"}, "A",
  ["Eq(simplify(diff(x/(x+1), x) - 1/(x+1)**2), 0)"],
  r"$\dfrac{(1)(x+1) - x(1)}{(x+1)^{2}} = \dfrac{1}{(x+1)^{2}}$.",
  {"B": "subtracted the quotient-rule terms the wrong way round",
   "C": "differentiated numerator and denominator separately",
   "D": "added the terms in the numerator instead of subtracting"})
I("derivative-product-quotient", 4,
  r"Find $f'(1)$ for $f(x) = \dfrac{x^{2}-1}{x^{2}+1}$.",
  {"A": r"$1$", "B": r"$0$", "C": r"$\dfrac{1}{2}$", "D": r"$2$"}, "A",
  ["Eq(diff((x**2-1)/(x**2+1), x).subs(x, 1), 1)",
   "Eq(simplify(diff((x**2-1)/(x**2+1), x) - 4*x/(x**2+1)**2), 0)"],
  r"$f'(x) = \dfrac{4x}{(x^{2}+1)^{2}}$, so $f'(1) = \dfrac{4}{4} = 1$.",
  {"B": "substituted into $f$ rather than $f'$",
   "C": "forgot to square the denominator", "D": "left the numerator as $4x$ over $2$"})

# ============ 9. domain-of-a-function — 0.79% ==============================
I("domain-of-a-function", 2,
  r"Find the domain of $f(x) = \dfrac{1}{x-3}$.",
  {"A": r"$x \ne 3$", "B": r"$x > 3$", "C": r"$x \ne 0$", "D": r"$x \ge 3$"}, "A",
  ["Eq(solve(Eq(x - 3, 0), x)[0], 3)"],
  r"The denominator vanishes at $x = 3$, so every real $x$ except $3$ is allowed.",
  {"B": "applied a square-root condition to a fraction",
   "C": "excluded the wrong value", "D": "included the excluded point"})
I("domain-of-a-function", 3,
  r"Find the domain of $f(x) = \sqrt{2x - 6}$.",
  {"A": r"$x \ge 3$", "B": r"$x > 3$", "C": r"$x \ge -3$", "D": r"$x \le 3$"}, "A",
  ["Eq(solve(Eq(2*x - 6, 0), x)[0], 3)", "(2*3 - 6) >= 0", "(2*4 - 6) > 0"],
  r"Need $2x - 6 \ge 0$, so $x \ge 3$. Equality is allowed because $\sqrt{0}$ is defined.",
  {"B": "excluded $x=3$, but $\\sqrt{0}=0$ is defined",
   "C": "sign error solving the inequality",
   "D": "reversed the inequality"})
I("domain-of-a-function", 4,
  r"Find the domain of $f(x) = \dfrac{\sqrt{x+2}}{x-1}$.",
  {"A": r"$x \ge -2,\ x \ne 1$", "B": r"$x \ge -2$", "C": r"$x > 1$",
   "D": r"$x \ne 1$"}, "A",
  ["(-2 + 2) >= 0", "Eq(solve(Eq(x - 1, 0), x)[0], 1)", "(1 + 2) > 0"],
  r"Two conditions at once: $x + 2 \ge 0$ gives $x \ge -2$, and $x - 1 \ne 0$ "
  r"removes $x = 1$.",
  {"B": "checked the root but not the denominator",
   "C": "over-restricted by requiring both to be positive",
   "D": "checked the denominator but not the root"})

# ============ 10. circle-area-and-arc — 0.69% ==============================
I("circle-area-and-arc", 2,
  r"A circle has circumference $10\pi$. Find its area.",
  {"A": r"$25\pi$", "B": r"$100\pi$", "C": r"$10\pi$", "D": r"$5\pi$"}, "A",
  ["Eq(solve(Eq(2*pi*symbols('r'), 10*pi), symbols('r'))[0], 5)",
   "Eq(pi*5**2, 25*pi)"],
  r"$2\pi r = 10\pi$ gives $r = 5$, so $A = \pi r^{2} = 25\pi$.",
  {"B": "used the circumference as the radius", "C": "returned the circumference",
   "D": "used $\\pi r$ instead of $\\pi r^{2}$"})
I("circle-area-and-arc", 3,
  r"Find the length of an arc subtending $60^{\circ}$ at the centre of a circle "
  r"of radius $9$.",
  {"A": r"$3\pi$", "B": r"$6\pi$", "C": r"$\dfrac{27\pi}{2}$", "D": r"$18\pi$"}, "A",
  ["Eq(Rational(60,360)*2*pi*9, 3*pi)", "Eq(Rational(60,360), Rational(1,6))"],
  r"$\dfrac{60}{360} \times 2\pi(9) = \dfrac16 \times 18\pi = 3\pi$.",
  {"B": "used $\\tfrac13$ of the circumference",
   "C": "computed the sector AREA instead of the arc length",
   "D": "gave the whole circumference"})
I("circle-area-and-arc", 4,
  r"A sector of a circle of radius $6$ has area $12\pi$. Find its angle at the centre.",
  {"A": r"$120^{\circ}$", "B": r"$60^{\circ}$", "C": r"$240^{\circ}$",
   "D": r"$90^{\circ}$"}, "A",
  ["Eq(pi*6**2, 36*pi)",
   "Eq(solve(Eq(symbols('t')/360*pi*36, 12*pi), symbols('t'))[0], 120)"],
  r"The whole circle has area $36\pi$, so the sector is $\dfrac{12\pi}{36\pi} = \dfrac13$ "
  r"of it: $\dfrac13 \times 360^{\circ} = 120^{\circ}$.",
  {"B": "took the sector as one sixth of the circle",
   "C": "used two thirds instead of one third",
   "D": "assumed a quarter circle"})

# ============ 11. circle-equation — 0.69% ==================================
I("circle-equation", 2,
  r"Find the centre and radius of $(x-2)^{2} + (y+3)^{2} = 16$.",
  {"A": r"centre $(2,-3)$, radius $4$", "B": r"centre $(-2,3)$, radius $4$",
   "C": r"centre $(2,-3)$, radius $16$", "D": r"centre $(-2,3)$, radius $16$"}, "A",
  ["Eq(sqrt(16), 4)"],
  r"Read the signs off the brackets: centre $(2,-3)$, and the radius is "
  r"$\sqrt{16} = 4$.",
  {"B": "read both signs the wrong way", "C": "used $r^{2}$ as the radius",
   "D": "both errors together"})
I("circle-equation", 3,
  r"Find the radius of the circle $x^{2} + y^{2} - 6x + 4y - 12 = 0$.",
  {"A": r"$5$", "B": r"$\sqrt{12}$", "C": r"$25$", "D": r"$\sqrt{13}$"}, "A",
  ["Eq(3**2 + (-2)**2 + 12, 25)", "Eq(sqrt(25), 5)"],
  r"Completing the square: $(x-3)^{2} + (y+2)^{2} = 12 + 9 + 4 = 25$, so $r = 5$.",
  {"B": "took the constant term without completing the square",
   "C": "gave $r^{2}$", "D": "added $9$ and $4$ but forgot the $12$"})
I("circle-equation", 4,
  r"A circle has centre $(1,2)$ and passes through $(4,6)$. Find its equation.",
  {"A": r"$(x-1)^{2}+(y-2)^{2}=25$", "B": r"$(x-1)^{2}+(y-2)^{2}=5$",
   "C": r"$(x+1)^{2}+(y+2)^{2}=25$", "D": r"$(x-4)^{2}+(y-6)^{2}=25$"}, "A",
  ["Eq((4-1)**2 + (6-2)**2, 25)", "Eq(sqrt(25), 5)"],
  r"$r^{2} = (4-1)^{2} + (6-2)^{2} = 9 + 16 = 25$.",
  {"B": "used the radius instead of its square on the right",
   "C": "wrong signs in the brackets", "D": "used the point on the circle as the centre"})

# ============ 12. pythagoras — 0.69% =======================================
I("pythagoras", 2,
  r"A right-angled triangle has hypotenuse $10$ and one leg $6$. Find the other leg.",
  {"A": r"$8$", "B": r"$4$", "C": r"$\sqrt{136}$", "D": r"$16$"}, "A",
  ["Eq(sqrt(10**2 - 6**2), 8)", "Eq(sqrt(10**2 + 6**2), sqrt(136))"],
  r"$\sqrt{10^{2} - 6^{2}} = \sqrt{64} = 8$.",
  {"B": "subtracted the lengths instead of the squares",
   "C": "added the squares — but $10$ is the hypotenuse",
   "D": "forgot the square root"})
I("pythagoras", 3,
  r"Is a triangle with sides $9$, $12$, $15$ right-angled?",
  {"A": r"Yes, the right angle is opposite the side $15$",
   "B": r"Yes, the right angle is opposite the side $9$",
   "C": r"No, because $9 + 12 \ne 15$",
   "D": r"No, because $9^{2}+12^{2} \ne 15^{2}$"}, "A",
  ["Eq(9**2 + 12**2, 15**2)", "Eq(9**2 + 12**2, 225)"],
  r"$9^{2} + 12^{2} = 81 + 144 = 225 = 15^{2}$, so it is right-angled, with the "
  r"right angle opposite the longest side.",
  {"B": "put the right angle opposite the shortest side",
   "C": "tested the sides rather than their squares",
   "D": "arithmetic slip — the two sides do agree"})
I("pythagoras", 4,
  r"A rectangular box measures $3 \times 4 \times 12$. Find the length of its "
  r"space diagonal.",
  {"A": r"$13$", "B": r"$5$", "C": r"$19$", "D": r"$\sqrt{160}$"}, "A",
  ["Eq(sqrt(3**2 + 4**2 + 12**2), 13)", "Eq(sqrt(3**2 + 4**2), 5)"],
  r"$\sqrt{3^{2}+4^{2}+12^{2}} = \sqrt{9+16+144} = \sqrt{169} = 13$.",
  {"B": "found the diagonal of the base only",
   "C": "added the three edges", "D": "used $3^{2}+12^{2}+\\ldots$ with a slip"})

# ============ 13. triangle-area — 0.69% ====================================
I("triangle-area", 2,
  r"Find the area of a triangle with base $14$ and perpendicular height $9$.",
  {"A": r"$63$", "B": r"$126$", "C": r"$23$", "D": r"$31.5$"}, "A",
  ["Eq(Rational(1,2)*14*9, 63)"],
  r"$\tfrac12 \times 14 \times 9 = 63$.",
  {"B": "forgot the factor $\\tfrac12$", "C": "added base and height",
   "D": "halved twice"})
I("triangle-area", 3,
  r"Find the area of a triangle with sides $8$ and $10$ enclosing an angle of $30^{\circ}$.",
  {"A": r"$20$", "B": r"$40$", "C": r"$20\sqrt{3}$", "D": r"$80$"}, "A",
  ["Eq(Rational(1,2)*8*10*sin(pi/6), 20)", "Eq(sin(pi/6), Rational(1,2))"],
  r"$\tfrac12 ab\sin C = \tfrac12(8)(10)\sin 30^{\circ} = 40 \times \tfrac12 = 20$.",
  {"B": "omitted the $\\sin 30^{\\circ}$", "C": "used $\\sin 60^{\\circ}$",
   "D": "omitted both the $\\tfrac12$ and the sine"})
I("triangle-area", 4,
  r"A triangle has area $30$, and two of its sides are $12$ and $10$. Find the "
  r"sine of the angle between them.",
  {"A": r"$\dfrac{1}{2}$", "B": r"$\dfrac{1}{4}$", "C": r"$\dfrac{1}{\sqrt{2}}$",
   "D": r"$\dfrac{5}{2}$"}, "A",
  ["Eq(solve(Eq(Rational(1,2)*12*10*symbols('s'), 30), symbols('s'))[0], Rational(1,2))"],
  r"$\tfrac12(12)(10)\sin C = 30$ gives $60\sin C = 30$, so $\sin C = \tfrac12$.",
  {"B": "forgot the $\\tfrac12$ when rearranging", "C": "assumed a $45^{\\circ}$ angle",
   "D": "inverted the final division"})

# ============ 14. triangle-similarity — 0.69% ==============================
I("triangle-similarity", 2,
  r"Triangles $ABC$ and $DEF$ are similar with $AB = 6$, $DE = 9$ and $BC = 8$. "
  r"Find $EF$.",
  {"A": r"$12$", "B": r"$11$", "C": r"$\dfrac{16}{3}$", "D": r"$5.33$"}, "A",
  ["Eq(8 * Rational(9,6), 12)", "Eq(Rational(9,6), Rational(3,2))"],
  r"The scale factor is $\dfrac96 = \dfrac32$, so $EF = 8 \times \dfrac32 = 12$.",
  {"B": "added the difference $9-6=3$ instead of scaling",
   "C": "scaled by $\\tfrac23$ — the wrong way round",
   "D": "same inversion, written as a decimal"})
I("triangle-similarity", 3,
  r"In triangle $ABC$, $DE \parallel BC$ with $D$ on $AB$ and $E$ on $AC$. "
  r"If $AD = 4$, $DB = 6$ and $AE = 6$, find $EC$.",
  {"A": r"$9$", "B": r"$4$", "C": r"$15$", "D": r"$\dfrac{8}{3}$"}, "A",
  ["Eq(solve(Eq(Rational(4,6), 6/symbols('y')), symbols('y'))[0], 9)"],
  r"$\dfrac{AD}{DB} = \dfrac{AE}{EC}$ gives $\dfrac46 = \dfrac{6}{EC}$, so $EC = 9$.",
  {"B": "matched $AD$ to $AE$ and copied the difference",
   "C": "gave the whole side $AC$", "D": "inverted the ratio"})
I("triangle-similarity", 4,
  r"Two similar triangles have areas $27$ and $48$. The smaller has a side of "
  r"length $9$. Find the corresponding side of the larger.",
  {"A": r"$12$", "B": r"$16$", "C": r"$\dfrac{9\sqrt{48}}{\sqrt{27}}$ rounded to $11$",
   "D": r"$\dfrac{27}{4}$"}, "A",
  ["Eq(sqrt(Rational(48,27)), Rational(4,3))", "Eq(9*Rational(4,3), 12)"],
  r"Areas scale by the square of the length ratio, so the ratio is "
  r"$\sqrt{\dfrac{48}{27}} = \dfrac43$ and the side is $9 \times \dfrac43 = 12$.",
  {"B": "scaled by the area ratio $\\tfrac{48}{27}$ directly",
   "C": "correct method, arithmetic slip in the surd",
   "D": "scaled downwards"})

# ============ 15. discriminant — 0.66% =====================================
I("discriminant", 2,
  r"How many real roots does $x^{2} - 4x + 7 = 0$ have?",
  {"A": r"none", "B": r"one", "C": r"two", "D": r"two, both negative"}, "A",
  ["Eq((-4)**2 - 4*1*7, -12)", "((-4)**2 - 4*1*7) < 0"],
  r"$\Delta = 16 - 28 = -12 < 0$, so there are no real roots.",
  {"B": "treated $\\Delta<0$ as a repeated root",
   "C": "took $\\Delta = 16+28$", "D": "read the sign of $b$ as the sign of the roots"})
I("discriminant", 3,
  r"For which value of $k$ does $x^{2} + kx + 9 = 0$ have exactly one real root, "
  r"with $k > 0$?",
  {"A": r"$k = 6$", "B": r"$k = 3$", "C": r"$k = 9$", "D": r"$k = 36$"}, "A",
  ["Eq(6**2 - 4*1*9, 0)",
   "Eq(solve(Eq(symbols('k')**2 - 36, 0), symbols('k'))[1], 6)"],
  r"One root means $\Delta = k^{2} - 36 = 0$, so $k = 6$ (taking $k>0$).",
  {"B": "solved $k^{2}=9$", "C": "set $k$ equal to the constant term",
   "D": "solved $k = 36$ without the square root"})
I("discriminant", 4,
  r"Find the values of $m$ for which $mx^{2} + 4x + 1 = 0$ has two distinct real roots "
  r"($m \ne 0$).",
  {"A": r"$m < 4,\ m \ne 0$", "B": r"$m > 4$", "C": r"$m < 4$", "D": r"$m > 0$"}, "A",
  ["Eq(4**2 - 4*symbols('m')*1, 16 - 4*symbols('m'))",
   "(16 - 4*2) > 0", "(16 - 4*5) < 0"],
  r"$\Delta = 16 - 4m > 0$ gives $m < 4$; and $m \ne 0$ or it is not a quadratic.",
  {"B": "reversed the inequality when dividing by $-4$",
   "C": "correct inequality but forgot that $m=0$ is not allowed",
   "D": "used the sign of $m$ rather than the discriminant"})

# ============ 16. factoring-common-factor — 0.66% ==========================
I("factoring-common-factor", 2,
  r"Factorise $12x^{3} - 18x^{2}$.",
  {"A": r"$6x^{2}(2x-3)$", "B": r"$6x(2x^{2}-3x)$", "C": r"$2x^{2}(6x-9)$",
   "D": r"$6x^{2}(2x-3x)$"}, "A",
  ["Eq(simplify(6*x**2*(2*x-3) - (12*x**3 - 18*x**2)), 0)"],
  r"The highest common factor is $6x^{2}$, leaving $2x - 3$.",
  {"B": "took out only $6x$", "C": "took out only the highest common power of $x$ "
                                  "with a factor of $2$",
   "D": "left an $x$ inside the bracket by mistake"})
I("factoring-common-factor", 3,
  r"Factorise $5a(x-2) - 3(x-2)$.",
  {"A": r"$(x-2)(5a-3)$", "B": r"$(x-2)(5a+3)$", "C": r"$5a-3(x-2)$",
   "D": r"$(x-2)^{2}(5a-3)$"}, "A",
  ["Eq(simplify((x-2)*(5*symbols('a')-3) - (5*symbols('a')*(x-2) - 3*(x-2))), 0)"],
  r"$(x-2)$ is a common factor of both terms, leaving $5a - 3$.",
  {"B": "sign error on the second term",
   "C": "did not treat $(x-2)$ as a single factor",
   "D": "counted the common factor twice"})
I("factoring-common-factor", 4,
  r"Factorise fully $8x^{3}y - 2xy^{3}$.",
  {"A": r"$2xy(2x-y)(2x+y)$", "B": r"$2xy(4x^{2}-y^{2})$", "C": r"$2xy(2x-y)^{2}$",
   "D": r"$xy(8x^{2}-2y^{2})$"}, "A",
  ["Eq(simplify(2*x*symbols('y')*(2*x-symbols('y'))*(2*x+symbols('y')) - "
   "(8*x**3*symbols('y') - 2*x*symbols('y')**3)), 0)"],
  r"Take out $2xy$ to get $2xy(4x^{2}-y^{2})$, then the bracket is a difference of "
  r"two squares: $2xy(2x-y)(2x+y)$.",
  {"B": "stopped before factorising the difference of squares",
   "C": "used $(2x-y)^{2}$, which is not a difference of squares",
   "D": "took out only $xy$"})

# ============ 17. like-terms-and-distribution — 0.66% ======================
I("like-terms-and-distribution", 2,
  r"Simplify $3(2x - 5) - 2(x - 4)$.",
  {"A": r"$4x - 7$", "B": r"$4x - 23$", "C": r"$8x - 7$", "D": r"$4x + 7$"}, "A",
  ["Eq(simplify(3*(2*x-5) - 2*(x-4) - (4*x - 7)), 0)"],
  r"$6x - 15 - 2x + 8 = 4x - 7$.",
  {"B": "did not change the sign of $-4$ when distributing $-2$",
   "C": "added the coefficients of $x$ instead of subtracting",
   "D": "sign slip on the constant"})
I("like-terms-and-distribution", 3,
  r"Expand and simplify $(2x-3)(x+4) - 2x^{2}$.",
  {"A": r"$5x - 12$", "B": r"$5x + 12$", "C": r"$4x^{2}+5x-12$", "D": r"$-5x-12$"}, "A",
  ["Eq(simplify((2*x-3)*(x+4) - 2*x**2 - (5*x - 12)), 0)"],
  r"$(2x-3)(x+4) = 2x^{2}+5x-12$, and subtracting $2x^{2}$ leaves $5x-12$.",
  {"B": "sign error on the constant term",
   "C": "added $2x^{2}$ instead of subtracting", "D": "sign error on the $x$ term"})
I("like-terms-and-distribution", 4,
  r"Simplify $2a - \big[3b - (a - 2b)\big]$.",
  {"A": r"$3a - 5b$", "B": r"$3a - b$", "C": r"$a - 5b$", "D": r"$3a + 5b$"}, "A",
  ["Eq(simplify(2*symbols('a') - (3*symbols('b') - (symbols('a') - 2*symbols('b'))) - "
   "(3*symbols('a') - 5*symbols('b'))), 0)"],
  r"Inner bracket first: $3b - (a-2b) = 3b - a + 2b = 5b - a$. Then "
  r"$2a - (5b - a) = 3a - 5b$.",
  {"B": "did not change the sign of $-2b$ in the inner bracket",
   "C": "dropped the sign change on $a$", "D": "sign error on the whole bracket"})

# ============ 18. quadratic-by-factoring — 0.66% ===========================
I("quadratic-by-factoring", 2,
  r"Solve $x^{2} - 5x = 0$.",
  {"A": r"$x = 0$ or $x = 5$", "B": r"$x = 5$", "C": r"$x = -5$ or $x = 0$",
   "D": r"$x = 5$ or $x = -5$"}, "A",
  ["Eq(simplify(x*(x-5) - (x**2 - 5*x)), 0)", "Eq(0**2 - 5*0, 0)", "Eq(5**2 - 5*5, 0)"],
  r"$x(x-5)=0$, so $x=0$ or $x=5$.",
  {"B": "divided both sides by $x$ and lost the root $x=0$",
   "C": "sign error factoring", "D": "treated it as a difference of squares"})
I("quadratic-by-factoring", 3,
  r"Solve $x^{2} + 2x - 15 = 0$.",
  {"A": r"$x = 3$ or $x = -5$", "B": r"$x = -3$ or $x = 5$", "C": r"$x = 3$ or $x = 5$",
   "D": r"$x = -3$ or $x = -5$"}, "A",
  ["Eq(3**2 + 2*3 - 15, 0)", "Eq((-5)**2 + 2*(-5) - 15, 0)",
   "Eq(simplify((x-3)*(x+5) - (x**2 + 2*x - 15)), 0)"],
  r"$(x-3)(x+5)=0$, so $x=3$ or $x=-5$.",
  {"B": "read the roots straight off the brackets without flipping the signs",
   "C": "both roots positive — product would be $+15$ with sum $8$",
   "D": "both roots negative — sum would be $-8$"})
I("quadratic-by-factoring", 4,
  r"Solve $3x^{2} = 10x - 8$.",
  {"A": r"$x = 2$ or $x = \dfrac43$", "B": r"$x = -2$ or $x = -\dfrac43$",
   "C": r"$x = 2$ or $x = \dfrac34$", "D": r"$x = 4$ or $x = \dfrac23$"}, "A",
  ["Eq(3*2**2 - (10*2 - 8), 0)", "Eq(3*Rational(4,3)**2 - (10*Rational(4,3) - 8), 0)",
   "Eq(simplify((3*x-4)*(x-2) - (3*x**2 - 10*x + 8)), 0)"],
  r"Rearrange to $3x^{2}-10x+8=0$, factorise $(3x-4)(x-2)=0$, so $x=\tfrac43$ or $x=2$.",
  {"B": "moved the terms without changing their signs",
   "C": "inverted the fractional root", "D": "misread the factor as $(x-4)(3x-2)$"})

# ============ 19. quadratic-inequalities — 0.66% ===========================
I("quadratic-inequalities", 2,
  r"Solve $x^{2} - 9 > 0$.",
  {"A": r"$x < -3$ or $x > 3$", "B": r"$-3 < x < 3$", "C": r"$x > 3$",
   "D": r"$x > 9$"}, "A",
  ["((-4)**2 - 9) > 0", "((0)**2 - 9) < 0", "((4)**2 - 9) > 0"],
  r"$(x-3)(x+3)>0$ holds outside the roots: $x<-3$ or $x>3$.",
  {"B": "took the inside of the roots", "C": "kept only the positive branch",
   "D": "did not take the square root"})
I("quadratic-inequalities", 3,
  r"Solve $x^{2} + x - 6 \le 0$.",
  {"A": r"$-3 \le x \le 2$", "B": r"$-2 \le x \le 3$", "C": r"$x \le -3$ or $x \ge 2$",
   "D": r"$-3 < x < 2$"}, "A",
  ["Eq(2**2 + 2 - 6, 0)", "Eq((-3)**2 + (-3) - 6, 0)", "((0)**2 + 0 - 6) <= 0"],
  r"$(x+3)(x-2)\le 0$, so $x$ lies between the roots, endpoints included: "
  r"$-3 \le x \le 2$.",
  {"B": "sign error reading the roots off the factors",
   "C": "took the outside of the roots",
   "D": "excluded the endpoints although the inequality is not strict"})
I("quadratic-inequalities", 4,
  r"Solve $-x^{2} + 4x - 3 > 0$.",
  {"A": r"$1 < x < 3$", "B": r"$x < 1$ or $x > 3$", "C": r"$-3 < x < -1$",
   "D": r"$1 \le x \le 3$"}, "A",
  ["Eq(-(1)**2 + 4*1 - 3, 0)", "Eq(-(3)**2 + 4*3 - 3, 0)",
   "(-(2)**2 + 4*2 - 3) > 0", "(-(0)**2 + 4*0 - 3) < 0"],
  r"Multiply by $-1$ and flip: $x^{2}-4x+3<0$, i.e. $(x-1)(x-3)<0$, so $1<x<3$.",
  {"B": "did not flip the inequality when multiplying by $-1$",
   "C": "flipped the signs of the roots as well",
   "D": "included the endpoints although the inequality is strict"})

# ============ 20. special-products — 0.66% =================================
I("special-products", 2,
  r"Expand $(2x - 5)^{2}$.",
  {"A": r"$4x^{2} - 20x + 25$", "B": r"$4x^{2} + 25$", "C": r"$4x^{2} - 10x + 25$",
   "D": r"$2x^{2} - 20x + 25$"}, "A",
  ["Eq(simplify(expand((2*x-5)**2) - (4*x**2 - 20*x + 25)), 0)"],
  r"$(a-b)^{2} = a^{2} - 2ab + b^{2}$ with $a=2x$, $b=5$: $4x^{2}-20x+25$.",
  {"B": "squared each term and dropped the middle term",
   "C": "used $ab$ instead of $2ab$", "D": "did not square the coefficient $2$"})
I("special-products", 3,
  r"Simplify $(x+7)(x-7)$.",
  {"A": r"$x^{2} - 49$", "B": r"$x^{2} + 49$", "C": r"$x^{2} - 14x - 49$",
   "D": r"$x^{2} - 14$"}, "A",
  ["Eq(simplify(expand((x+7)*(x-7)) - (x**2 - 49)), 0)"],
  r"A difference of two squares: $x^{2} - 7^{2} = x^{2} - 49$.",
  {"B": "sign error — the product of $+7$ and $-7$ is negative",
   "C": "kept a middle term that cancels", "D": "did not square the $7$"})
I("special-products", 4,
  r"Given $a + b = 7$ and $ab = 10$, find $a^{2} + b^{2}$.",
  {"A": r"$29$", "B": r"$49$", "C": r"$69$", "D": r"$39$"}, "A",
  ["Eq(7**2 - 2*10, 29)", "Eq((2+5), 7)", "Eq(2*5, 10)", "Eq(2**2 + 5**2, 29)"],
  r"$a^{2}+b^{2} = (a+b)^{2} - 2ab = 49 - 20 = 29$.",
  {"B": "used $(a+b)^{2}$ directly", "C": "added $2ab$ instead of subtracting",
   "D": "subtracted $ab$ rather than $2ab$"})
