"""Batch D — the last 20 thin skills, 0.36% down to 0.07% exam weight.

These are the cheapest skills in the worklist, which is exactly why they come
last: if the batch had stopped early, this is the part it would have been
right to leave.

Difficulty is the ENGINE scale: 1 easy, 2 medium, 3 hard.
"""

from sympy import sqrt

from rung_bank import R

# ---------------------------------------------------------------- 0.36%
R("cosine-rule", 1,
  r"In triangle $ABC$, $a=5$, $b=7$ and $C=60^\circ$. Find $c$.",
  {"A": r"$\sqrt{39}$", "B": r"$\sqrt{74}$", "C": r"$\sqrt{109}$", "D": r"$39$"},
  "A",
  ["Eq(cos(pi/3), Rational(1,2))",
   "Eq(5**2 + 7**2 - 2*5*7*cos(pi/3), 39)",
   "Eq(5**2 + 7**2, 74)",
   "Eq(5**2 + 7**2 + 2*5*7*cos(pi/3), 109)"],
  r"$$c^2=a^2+b^2-2ab\cos C=25+49-2(5)(7)\left(\tfrac12\right)=74-35=39,$$ "
  r"so $c=\sqrt{39}$.",
  {"B": r"used Pythagoras, which needs a right angle — this triangle has none",
   "C": r"added the $2ab\cos C$ term instead of subtracting it",
   "D": r"stopped at $c^2$ and forgot the square root"})

R("cosine-rule", 3,
  r"A triangle has sides $5$, $6$ and $7$. Find the cosine of the angle "
  r"opposite the side of length $7$.",
  {"A": r"$\dfrac15$", "B": r"$-\dfrac15$", "C": r"$\dfrac25$", "D": r"$\dfrac{6}{35}$"},
  "A",
  ["Eq(Rational(25+36-49, 2*5*6), Rational(1,5))",
   "Eq(Rational(49-25-36, 2*5*6), Rational(-1,5))",
   "Eq(Rational(12, 5*6), Rational(2,5))",
   "Eq(Rational(12, 2*5*7), Rational(6,35))"],
  r"Rearrange the cosine rule for the angle opposite $c=7$: "
  r"$$\cos C=\frac{a^2+b^2-c^2}{2ab}=\frac{25+36-49}{2(5)(6)}"
  r"=\frac{12}{60}=\frac15.$$",
  {"B": r"wrote $c^2-a^2-b^2$ on top, reversing the sign",
   "C": r"divided by $ab=30$ instead of $2ab=60$",
   "D": r"used the sides $5$ and $7$ in the denominator; they must be the two sides ENCLOSING the angle"})

R("exact-trig-values", 3,
  r"Find the exact value of $\tan 240^\circ-\sin 300^\circ$.",
  {"A": r"$\dfrac{3\sqrt3}{2}$", "B": r"$\dfrac{\sqrt3}{2}$",
   "C": r"$\sqrt3$", "D": r"$-\dfrac{\sqrt3}{2}$"},
  "A",
  ["Eq(tan(4*pi/3), sqrt(3))",
   "Eq(sin(5*pi/3), -sqrt(3)/2)",
   "Eq(simplify(tan(4*pi/3) - sin(5*pi/3) - 3*sqrt(3)/2), 0)"],
  r"$240^\circ$ is in the third quadrant where tangent is positive, and its "
  r"reference angle is $60^\circ$, so $\tan 240^\circ=\sqrt3$. "
  r"$300^\circ$ is in the fourth quadrant where sine is negative, with the "
  r"same reference angle, so $\sin 300^\circ=-\tfrac{\sqrt3}{2}$. Then "
  r"$$\sqrt3-\left(-\tfrac{\sqrt3}{2}\right)=\sqrt3+\tfrac{\sqrt3}{2}"
  r"=\tfrac{3\sqrt3}{2}.$$",
  {"B": r"took $\tan 240^\circ$ as $\tfrac{\sqrt3}{2}$ — that is a sine value, not a tangent",
   "C": r"treated $\sin 300^\circ$ as positive, so the two terms cancelled to $\sqrt3$",
   "D": r"subtracted the wrong way round and lost the tangent term"})

R("sine-rule", 1,
  r"In triangle $ABC$, $A=30^\circ$, $B=90^\circ$ and $a=5$. Find $b$.",
  {"A": r"$10$", "B": r"$\dfrac52$", "C": r"$20$", "D": r"$5\sqrt3$"},
  "A",
  ["Eq(sin(pi/6), Rational(1,2))",
   "Eq(sin(pi/2), 1)",
   "Eq(5*sin(pi/2)/sin(pi/6), 10)",
   "Eq(5*sin(pi/6)/sin(pi/2), Rational(5,2))"],
  r"$$\frac{b}{\sin B}=\frac{a}{\sin A}\ \Longrightarrow\ "
  r"b=\frac{a\sin B}{\sin A}=\frac{5\times 1}{\tfrac12}=10.$$",
  {"B": r"inverted the ratio, computing $a\sin A/\sin B$",
   "C": r"doubled twice",
   "D": r"used the third angle $60^\circ$ instead of $B=90^\circ$"})

R("sine-rule", 3,
  r"In triangle $ABC$, $a=6$, $b=8$ and $A=30^\circ$. How many triangles "
  r"satisfy this data?",
  {"A": r"two", "B": r"one", "C": r"none", "D": r"infinitely many"},
  "A",
  ["Eq(Rational(8,1)*Rational(1,2)/6, Rational(2,3))",
   "Rational(2,3) < 1",
   "6 > 8*Rational(1,2)",
   "6 < 8"],
  r"This is the ambiguous (SSA) case. The sine rule gives "
  r"$$\sin B=\frac{b\sin A}{a}=\frac{8\times\tfrac12}{6}=\frac23,$$ which is "
  r"less than $1$, so $B$ exists. Because $a<b$ AND $a>b\sin A$ "
  r"(that is, $6>4$), the side $a$ is long enough to reach the base in two "
  r"places: both the acute $B$ and its obtuse partner $180^\circ-B$ give a "
  r"valid triangle.",
  {"B": r"took only the acute value of $B$ and missed the obtuse one",
   "C": r"$\sin B=\tfrac23\le 1$, so a triangle certainly exists",
   "D": r"the data fixes the triangle up to two possibilities, not infinitely many"})

R("trig-equations", 1,
  r"Solve $\sin x=\tfrac12$ for $0\le x<2\pi$.",
  {"A": r"$x=\dfrac{\pi}{6}$ or $x=\dfrac{5\pi}{6}$",
   "B": r"$x=\dfrac{\pi}{6}$ only",
   "C": r"$x=\dfrac{\pi}{6}$ or $x=\dfrac{7\pi}{6}$",
   "D": r"$x=\dfrac{\pi}{3}$ or $x=\dfrac{2\pi}{3}$"},
  "A",
  ["Eq(sin(pi/6), Rational(1,2))",
   "Eq(sin(5*pi/6), Rational(1,2))",
   "Eq(sin(7*pi/6), Rational(-1,2))",
   "Eq(sin(pi/3), sqrt(3)/2)"],
  r"$\sin\tfrac{\pi}{6}=\tfrac12$, and sine is also positive in the second "
  r"quadrant, where the solution is $\pi-\tfrac{\pi}{6}=\tfrac{5\pi}{6}$. "
  r"Both lie in $[0,2\pi)$.",
  {"B": r"stopped at the first quadrant; sine is positive in the second as well",
   "C": r"used $\pi+\tfrac{\pi}{6}$, which is where sine is NEGATIVE",
   "D": r"solved $\sin x=\tfrac{\sqrt3}{2}$ instead"})

R("trig-equations", 3,
  r"Solve $2\cos^2x-\cos x-1=0$ for $0\le x<2\pi$.",
  {"A": r"$x=0,\ \dfrac{2\pi}{3},\ \dfrac{4\pi}{3}$",
   "B": r"$x=\dfrac{2\pi}{3},\ \dfrac{4\pi}{3}$",
   "C": r"$x=0,\ \dfrac{\pi}{3},\ \dfrac{5\pi}{3}$",
   "D": r"$x=\pi,\ \dfrac{2\pi}{3},\ \dfrac{4\pi}{3}$"},
  "A",
  ["Eq(factor(2*c**2-c-1), (c-1)*(2*c+1))",
   "Eq(cos(0), 1)",
   "Eq(cos(2*pi/3), Rational(-1,2))",
   "Eq(cos(4*pi/3), Rational(-1,2))",
   "Eq(cos(pi), -1)"],
  r"Treat it as a quadratic in $c=\cos x$: "
  r"$$2c^2-c-1=(c-1)(2c+1)=0,$$ so $\cos x=1$ or $\cos x=-\tfrac12$. "
  r"$\cos x=1$ gives $x=0$; $\cos x=-\tfrac12$ gives "
  r"$x=\tfrac{2\pi}{3}$ and $x=\tfrac{4\pi}{3}$.",
  {"B": r"solved $\cos x=-\tfrac12$ but dropped the root $\cos x=1$",
   "C": r"used $\cos x=\tfrac12$ instead of $-\tfrac12$",
   "D": r"took $\cos x=1$ to give $x=\pi$; $\cos\pi=-1$, not $1$"})

R("trig-simplification", 1,
  r"Simplify $\sin^2x+\cos^2x$.",
  {"A": r"$1$", "B": r"$0$", "C": r"$\sin 2x$", "D": r"$2$"},
  "A",
  ["Eq(simplify(sin(x)**2+cos(x)**2), 1)",
   "Eq(simplify(sin(x)**2-cos(x)**2 + cos(2*x)), 0)"],
  r"This is the Pythagorean identity: $\sin^2x+\cos^2x=1$ for every $x$.",
  {"B": r"that is $\sin^2x-\cos^2x$ only when $x=\tfrac{\pi}{4}$, and it is not an identity",
   "C": r"$\sin 2x=2\sin x\cos x$ — a product, not a sum of squares",
   "D": r"the identity gives $1$, not $2$"})

R("trig-simplification", 2,
  r"Simplify $\dfrac{1-\cos^2x}{\sin x}$, where $\sin x\ne 0$.",
  {"A": r"$\sin x$", "B": r"$\cos x$", "C": r"$\tan x$", "D": r"$\dfrac{1}{\sin x}$"},
  "A",
  ["Eq(simplify((1-cos(x)**2)/sin(x) - sin(x)), 0)",
   "Eq(simplify(1-cos(x)**2 - sin(x)**2), 0)"],
  r"By the Pythagorean identity $1-\cos^2x=\sin^2x$, so "
  r"$$\frac{1-\cos^2x}{\sin x}=\frac{\sin^2x}{\sin x}=\sin x.$$",
  {"B": r"used $1-\cos^2x=\cos^2 x$",
   "C": r"cancelled as though the numerator were $\sin x\cos x$",
   "D": r"inverted the fraction after cancelling"})

# ---------------------------------------------------------------- 0.34%
R("solid-of-revolution-geometric", 1,
  r"A rectangle is rotated a full turn about one of its sides. What solid "
  r"is generated?",
  {"A": r"a cylinder", "B": r"a cone", "C": r"a sphere", "D": r"a prism"},
  "A",
  [],
  r"Every point of the rectangle sweeps a circle centred on the axis. The "
  r"side along the axis stays fixed and the opposite side sweeps out a "
  r"circle of constant radius, so the surface is a cylinder of radius equal "
  r"to the other side.",
  {"B": r"a cone comes from rotating a right TRIANGLE about a leg",
   "C": r"a sphere comes from rotating a semicircle about its diameter",
   "D": r"a prism has flat sides; rotation always produces circular cross-sections"})

R("solid-of-revolution-geometric", 3,
  r"A right-angled triangle with legs $3$ and $4$ is rotated a full turn "
  r"about the leg of length $3$. Find the volume of the solid.",
  {"A": r"$16\pi$", "B": r"$12\pi$", "C": r"$48\pi$", "D": r"$\dfrac{25\pi}{3}$"},
  "A",
  ["Eq(Rational(1,3)*pi*4**2*3, 16*pi)",
   "Eq(Rational(1,3)*pi*3**2*4, 12*pi)",
   "Eq(pi*4**2*3, 48*pi)",
   "Eq(sqrt(3**2+4**2), 5)"],
  r"Rotating about the leg of length $3$ makes that leg the AXIS, so it is "
  r"the height; the other leg, $4$, sweeps out the base circle and is "
  r"therefore the radius. "
  r"$$V=\tfrac13\pi r^2h=\tfrac13\pi(4)^2(3)=16\pi.$$",
  {"B": r"swapped radius and height — the leg on the axis is the height",
   "C": r"used the cylinder formula, dropping the factor $\tfrac13$",
   "D": r"used the hypotenuse $5$ as the radius"})

# ---------------------------------------------------------------- 0.30%
R("integer-powers", 2,
  r"Evaluate $2^{-3}$.",
  {"A": r"$\dfrac18$", "B": r"$-8$", "C": r"$-6$", "D": r"$8$"},
  "A",
  ["Eq(2**(-3), Rational(1,8))", "Eq(2**3, 8)"],
  r"A negative exponent means a reciprocal, not a negative value: "
  r"$$2^{-3}=\frac{1}{2^3}=\frac18.$$",
  {"B": r"made the RESULT negative; the minus sign belongs to the exponent",
   "C": r"multiplied $2\times(-3)$",
   "D": r"ignored the minus sign entirely"})

R("integer-powers", 3,
  r"Simplify $\dfrac{2^{-2}\cdot 3^{3}}{2^{-4}\cdot 3}$.",
  {"A": r"$36$", "B": r"$4$", "C": r"$9$", "D": r"$\dfrac{1}{36}$"},
  "A",
  ["Eq((2**(-2)*3**3)/(2**(-4)*3), 36)",
   "Eq(2**(-2+4), 4)",
   "Eq(3**(3-1), 9)"],
  r"Subtract exponents on matching bases: "
  r"$$2^{-2-(-4)}\cdot 3^{3-1}=2^{2}\cdot 3^{2}=4\times 9=36.$$ "
  r"Note $-2-(-4)=+2$ — the double negative raises the power.",
  {"B": r"handled the powers of $2$ and dropped the powers of $3$",
   "C": r"handled the powers of $3$ and dropped the powers of $2$",
   "D": r"subtracted the exponents the wrong way round on both bases"})

R("percent-and-proportion", 2,
  r"Find $15\%$ of $240$.",
  {"A": r"$36$", "B": r"$16$", "C": r"$3.6$", "D": r"$360$"},
  "A",
  ["Eq(Rational(15,100)*240, 36)",
   "Eq(Rational(240,15), 16)",
   "Eq(Rational(15,1000)*240, Rational(18,5))"],
  r"$$15\%\text{ of }240=\frac{15}{100}\times 240=36.$$",
  {"B": r"divided $240$ by $15$ instead of taking $15\%$ of it",
   "C": r"divided by $1000$ rather than $100$",
   "D": r"multiplied by $15$ and divided by $10$"})

R("percent-and-proportion", 3,
  r"A price rises by $20\%$ and then falls by $20\%$. What is the net "
  r"change?",
  {"A": r"a $4\%$ decrease", "B": r"no change",
   "C": r"a $4\%$ increase", "D": r"a $40\%$ increase"},
  "A",
  ["Eq(Rational(120,100)*Rational(80,100), Rational(24,25))",
   "Eq(1-Rational(24,25), Rational(1,25))",
   "Eq(Rational(1,25), Rational(4,100))"],
  r"Multiply the two factors: "
  r"$$1.20\times 0.80=0.96,$$ so the final price is $96\%$ of the original — "
  r"a $4\%$ decrease. The second percentage is taken of the LARGER amount, "
  r"so the fall outweighs the rise.",
  {"B": r"assumed the two $20\%$ changes cancel; they are percentages of different amounts",
   "C": r"got the size right but the direction wrong",
   "D": r"added the percentages instead of compounding them"})

R("radicals-simplification", 3,
  r"Simplify $\sqrt{50}-\sqrt{18}+\sqrt{8}$.",
  {"A": r"$4\sqrt2$", "B": r"$6\sqrt2$", "C": r"$\sqrt{40}$", "D": r"$10\sqrt2$"},
  "A",
  ["Eq(simplify(sqrt(50) - 5*sqrt(2)), 0)",
   "Eq(simplify(sqrt(18) - 3*sqrt(2)), 0)",
   "Eq(simplify(sqrt(8) - 2*sqrt(2)), 0)",
   "Eq(simplify(sqrt(50)-sqrt(18)+sqrt(8) - 4*sqrt(2)), 0)"],
  r"Reduce each surd to a multiple of $\sqrt2$: "
  r"$$\sqrt{50}=5\sqrt2,\quad\sqrt{18}=3\sqrt2,\quad\sqrt8=2\sqrt2.$$ "
  r"Then $5\sqrt2-3\sqrt2+2\sqrt2=4\sqrt2$.",
  {"B": r"added all three instead of subtracting the middle term",
   "C": r"added the numbers under the roots, $50-18+8$; surds do not combine that way",
   "D": r"used $\sqrt{50}=5\sqrt2$ but $\sqrt{18}=\sqrt2$ and $\sqrt8=4\sqrt2$"})

# ---------------------------------------------------------------- 0.27%
R("stars-and-bars", 1,
  r"How many solutions in non-negative integers does $x+y=4$ have?",
  {"A": r"$5$", "B": r"$4$", "C": r"$3$", "D": r"$10$"},
  "A",
  ["Eq(binomial(4+1, 1), 5)", "Eq(binomial(5,2), 10)"],
  r"Choose $x$ freely from $0$ to $4$; $y$ is then forced. That is $5$ "
  r"solutions: $(0,4),(1,3),(2,2),(3,1),(4,0)$.",
  {"B": r"forgot that $x=0$ is allowed",
   "C": r"counted only the solutions with both parts positive and distinct",
   "D": r"used $\binom{5}{2}$, the formula for THREE unknowns"},
  check=lambda: sum(1 for i in range(5) for j in range(5) if i + j == 4) == 5)

R("stars-and-bars", 3,
  r"How many solutions in non-negative integers does $x+y+z=8$ have?",
  {"A": r"$45$", "B": r"$36$", "C": r"$21$", "D": r"$28$"},
  "A",
  ["Eq(binomial(8+2, 2), 45)",
   "Eq(binomial(9,2), 36)",
   "Eq(binomial(7,2), 21)",
   "Eq(binomial(8,2), 28)"],
  r"Place $8$ stars and $2$ bars in a row; each arrangement is one solution. "
  r"There are $8+2=10$ positions and the bars occupy $2$ of them: "
  r"$$\binom{8+3-1}{3-1}=\binom{10}{2}=45.$$",
  {"B": r"used $\binom{9}{2}$ — one star short",
   "C": r"used $\binom{7}{2}$, as though the parts had to be positive",
   "D": r"used $\binom{8}{2}$, forgetting to add the bars to the total"},
  check=lambda: sum(1 for i in range(9) for j in range(9 - i)) == 45)

R("trig-sum-difference", 1,
  r"Which expression equals $\cos(A+B)$?",
  {"A": r"$\cos A\cos B-\sin A\sin B$",
   "B": r"$\cos A\cos B+\sin A\sin B$",
   "C": r"$\sin A\cos B+\cos A\sin B$",
   "D": r"$\cos A+\cos B$"},
  "A",
  ["Eq(simplify(cos(x+y) - (cos(x)*cos(y) - sin(x)*sin(y))), 0)",
   "Eq(simplify(cos(x-y) - (cos(x)*cos(y) + sin(x)*sin(y))), 0)",
   "Eq(simplify(sin(x+y) - (sin(x)*cos(y) + cos(x)*sin(y))), 0)"],
  r"$$\cos(A+B)=\cos A\cos B-\sin A\sin B.$$ The sign flips relative to the "
  r"$+$ in the bracket — that is the part worth memorising.",
  {"B": r"that is $\cos(A-B)$",
   "C": r"that is $\sin(A+B)$",
   "D": r"cosine is not additive; $\cos(A+B)\ne\cos A+\cos B$"})

R("trig-sum-difference", 2,
  r"Find the exact value of $\sin 75^\circ$.",
  {"A": r"$\dfrac{\sqrt6+\sqrt2}{4}$", "B": r"$\dfrac{\sqrt6-\sqrt2}{4}$",
   "C": r"$\dfrac{\sqrt2+1}{2}$", "D": r"$\dfrac{\sqrt3+1}{2}$"},
  "A",
  ["Eq(simplify(sin(5*pi/12) - (sqrt(6)+sqrt(2))/4), 0)",
   "Eq(simplify(sin(pi/12) - (sqrt(6)-sqrt(2))/4), 0)",
   "Eq(sin(pi/4), sqrt(2)/2)",
   "Eq(cos(pi/6), sqrt(3)/2)"],
  r"Write $75^\circ=45^\circ+30^\circ$ and expand: "
  r"$$\sin 75^\circ=\sin45\cos30+\cos45\sin30"
  r"=\frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}+\frac{\sqrt2}{2}\cdot\frac12"
  r"=\frac{\sqrt6+\sqrt2}{4}.$$",
  {"B": r"that is $\sin 15^\circ$ — the difference $45^\circ-30^\circ$",
   "C": r"added $\sin45$ and $\sin30$ directly",
   "D": r"used $\cos30+\sin30$ without the $\tfrac{\sqrt2}{2}$ factors"})

# ---------------------------------------------------------------- 0.21%
R("geometric-sequence", 1,
  r"A geometric sequence has first term $3$ and common ratio $2$. Find the "
  r"fourth term.",
  {"A": r"$24$", "B": r"$12$", "C": r"$48$", "D": r"$9$"},
  "A",
  ["Eq(3*2**3, 24)", "Eq(3*2**2, 12)", "Eq(3*2**4, 48)", "Eq(3+3*2, 9)"],
  r"$$u_n=ar^{n-1}\ \Longrightarrow\ u_4=3\cdot 2^{3}=3\times 8=24.$$",
  {"B": r"used $r^{2}$ — off by one in the exponent",
   "C": r"used $r^{4}$ instead of $r^{n-1}=r^{3}$",
   "D": r"added the ratio each time, treating it as an arithmetic sequence"})

# ---------------------------------------------------------------- 0.20%
R("real-number-sets", 3,
  r"Which of these numbers is irrational?",
  {"A": r"$\sqrt8$", "B": r"$\sqrt9$", "C": r"$\dfrac{22}{7}$", "D": r"$0.25$"},
  "A",
  ["Eq(sqrt(9), 3)",
   "Eq(simplify(sqrt(8) - 2*sqrt(2)), 0)",
   "Eq(Rational(25,100), Rational(1,4))"],
  r"$\sqrt9=3$ and $\tfrac{22}{7}$ and $0.25=\tfrac14$ are all ratios of "
  r"integers, so all three are rational. $\sqrt8=2\sqrt2$, and $\sqrt2$ "
  r"cannot be written as such a ratio, so $\sqrt8$ is irrational.",
  {"B": r"$\sqrt9=3$ exactly — a square root is only irrational when the number is not a perfect square",
   "C": r"$\tfrac{22}{7}$ is a common approximation to $\pi$, but it is itself a ratio of integers",
   "D": r"$0.25$ terminates, so it equals $\tfrac14$"},
  check=lambda: (sqrt(8).is_rational is False and sqrt(9).is_rational is True))

R("repeating-decimal-to-fraction", 3,
  r"Write $0.4\overline{27}$ (that is, $0.4272727\ldots$) as a fraction in "
  r"lowest terms.",
  {"A": r"$\dfrac{47}{110}$", "B": r"$\dfrac{423}{999}$",
   "C": r"$\dfrac{427}{990}$", "D": r"$\dfrac{47}{99}$"},
  "A",
  ["Eq(Rational(423,990), Rational(47,110))",
   "Eq(Rational(47,110)*990, 423)",
   "Eq(1000-10, 990)"],
  r"Let $x=0.4272727\ldots$. Shift past the non-repeating digit and past one "
  r"full period: "
  r"$$10x=4.272727\ldots,\qquad 1000x=427.272727\ldots$$ "
  r"Subtract: $990x=423$, so "
  r"$$x=\frac{423}{990}=\frac{47}{110}.$$",
  {"B": r"used $999$, which is the denominator only when ALL digits repeat",
   "C": r"used $427$ on top, forgetting to subtract the $4$ from the shifted copy",
   "D": r"used $99$, ignoring the non-repeating digit $4$"})

# ---------------------------------------------------------------- 0.16%
R("arithmetic-series", 3,
  r"Find the sum of all multiples of $7$ between $100$ and $300$.",
  {"A": r"$5586$", "B": r"$5481$", "C": r"$5985$", "D": r"$2793$"},
  "A",
  ["Eq(7*15, 105)", "Eq(7*42, 294)", "Eq(42-15+1, 28)",
   "Eq(Rational(28*(105+294), 2), 5586)",
   "Eq(Rational(5586,2), 2793)"],
  r"The first multiple of $7$ above $100$ is $105=7(15)$ and the last below "
  r"$300$ is $294=7(42)$, so there are $42-15+1=28$ terms. Then "
  r"$$S=\frac{n(a+l)}{2}=\frac{28(105+294)}{2}=14\times 399=5586.$$",
  {"B": r"used $27$ terms — the classic off-by-one from $42-15$",
   "C": r"included $301$ as a term",
   "D": r"forgot to halve, or halved twice"},
  check=lambda: sum(range(105, 295, 7)) == 5586)

# ---------------------------------------------------------------- 0.09%
R("exponent-rules", 3,
  r"Simplify $\dfrac{\left(x^{3}y^{-2}\right)^{2}}{x^{-1}y^{3}}$.",
  {"A": r"$\dfrac{x^{7}}{y^{7}}$", "B": r"$x^{7}y^{7}$",
   "C": r"$\dfrac{x^{5}}{y^{7}}$", "D": r"$\dfrac{x^{7}}{y}$"},
  "A",
  ["Eq(simplify(((x**3*y**(-2))**2/(x**(-1)*y**3)) - x**7/y**7), 0)",
   "Eq(simplify((x**3*y**(-2))**2 - x**6*y**(-4)), 0)"],
  r"Apply the power to each factor first: $(x^3y^{-2})^2=x^6y^{-4}$. Then "
  r"subtract the denominator's exponents: "
  r"$$x^{6-(-1)}y^{-4-3}=x^{7}y^{-7}=\frac{x^{7}}{y^{7}}.$$",
  {"B": r"treated $y^{-7}$ as $y^{7}$",
   "C": r"subtracted the $x$ exponents as $6-1$ instead of $6-(-1)$",
   "D": r"subtracted only the $3$ from the $y$ exponent, forgetting the $-4$"})

R("logarithm-definition", 1,
  r"Evaluate $\log_2 8$.",
  {"A": r"$3$", "B": r"$4$", "C": r"$2$", "D": r"$\dfrac13$"},
  "A",
  ["Eq(simplify(log(8,2)), 3)", "Eq(2**3, 8)", "Eq(simplify(log(16,2)), 4)"],
  r"$\log_2 8$ asks: to what power must $2$ be raised to give $8$? Since "
  r"$2^3=8$, the answer is $3$.",
  {"B": r"answered $\log_2 16$",
   "C": r"gave the base rather than the exponent",
   "D": r"inverted the answer"})

R("logarithm-definition", 3,
  r"If $\log_a 8=\tfrac32$, find $a$.",
  {"A": r"$4$", "B": r"$2$", "C": r"$16$", "D": r"$12$"},
  "A",
  ["Eq(4**Rational(3,2), 8)",
   "Eq(simplify(log(8,4) - Rational(3,2)), 0)",
   "Eq(2**Rational(3,2), 2*sqrt(2))"],
  r"Rewrite in exponential form: $a^{3/2}=8$. Raise both sides to the power "
  r"$\tfrac23$: "
  r"$$a=8^{2/3}=\left(\sqrt[3]{8}\right)^{2}=2^{2}=4.$$",
  {"B": r"gave $\sqrt[3]{8}$ without squaring it",
   "C": r"multiplied $8$ by $2$ instead of raising to the power $\tfrac23$",
   "D": r"computed $8\times\tfrac32$"})

R("logarithmic-equations", 1,
  r"Solve $\log_3 x=2$.",
  {"A": r"$x=9$", "B": r"$x=6$", "C": r"$x=8$", "D": r"$x=\dfrac32$"},
  "A",
  ["Eq(3**2, 9)", "Eq(simplify(log(9,3) - 2), 0)"],
  r"Convert to exponential form: $x=3^2=9$.",
  {"B": r"multiplied the base by the exponent",
   "C": r"computed $3^2-1$",
   "D": r"divided the base by the exponent"})

R("logarithmic-equations", 3,
  r"Solve $\log x+\log(x-3)=1$ (logarithms base $10$).",
  {"A": r"$x=5$", "B": r"$x=5$ or $x=-2$", "C": r"$x=-2$", "D": r"$x=10$"},
  "A",
  ["Eq(factor(x**2-3*x-10), (x-5)*(x+2))",
   "Eq(5*(5-3), 10)",
   "Eq((-2)*(-2-3), 10)"],
  r"Combine the logarithms: $\log\bigl(x(x-3)\bigr)=1$, so $x(x-3)=10$ and "
  r"$$x^2-3x-10=0\ \Longrightarrow\ (x-5)(x+2)=0.$$ "
  r"Now check the domain: a logarithm needs a positive argument. $x=-2$ "
  r"makes $\log x$ undefined, so it is rejected. Only $x=5$ survives.",
  {"B": r"solved the quadratic but never checked that both logarithms are defined",
   "C": r"kept the rejected root and discarded the valid one",
   "D": r"set $x-3=10$, applying the $1$ to only one logarithm"})

# ---------------------------------------------------------------- 0.07%
R("logarithmic-inequalities", 3,
  r"Solve $\log_2(x-1)<3$.",
  {"A": r"$1<x<9$", "B": r"$x<9$", "C": r"$x>9$", "D": r"$0<x<8$"},
  "A",
  ["Eq(2**3, 8)", "Eq(simplify(log(8,2)), 3)", "Eq(8+1, 9)"],
  r"The logarithm is only defined when $x-1>0$, so $x>1$ from the start. "
  r"Since base $2$ is greater than $1$, the function increases and the "
  r"inequality keeps its direction: "
  r"$$x-1<2^3=8\ \Longrightarrow\ x<9.$$ Combining, $1<x<9$.",
  {"B": r"solved the inequality but ignored the domain restriction $x>1$",
   "C": r"reversed the inequality, which only happens for a base below $1$",
   "D": r"forgot to add the $1$ back after solving for $x-1$"})

R("rational-exponents", 3,
  r"Evaluate $27^{-2/3}$.",
  {"A": r"$\dfrac19$", "B": r"$9$", "C": r"$-9$", "D": r"$\dfrac{1}{729}$"},
  "A",
  ["Eq(27**Rational(-2,3), Rational(1,9))",
   "Eq(27**Rational(1,3), 3)",
   "Eq(27**Rational(2,3), 9)"],
  r"The denominator of the exponent is the root and the numerator is the "
  r"power; the minus sign inverts: "
  r"$$27^{-2/3}=\frac{1}{\left(\sqrt[3]{27}\right)^{2}}=\frac{1}{3^{2}}=\frac19.$$",
  {"B": r"ignored the minus sign",
   "C": r"made the result negative instead of taking a reciprocal",
   "D": r"squared $27$ before taking the cube root, then inverted"})
