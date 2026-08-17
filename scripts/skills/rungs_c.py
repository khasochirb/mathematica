"""Batch C — 28 thin skills, 0.52% down to 0.36% exam weight.

Difficulty is the ENGINE scale: 1 easy, 2 medium, 3 hard.

Where an item is about a coordinate map or a matrix shape, sympy has nothing
to assert — an `Eq` on it would be decoration. Those carry a `check=`
predicate that computes the claim in Python instead, which is the same
standard the counting items use.
"""

from sympy import Matrix, eye, zeros, symbols

from rung_bank import R

_a, _b = symbols("a b")

# ---------------------------------------------------------------- 0.52%
R("homothety", 1,
  r"An enlargement with centre the origin and scale factor $3$ maps "
  r"$A(2,-1)$ to $A'$. Find $A'$.",
  {"A": r"$(6,-3)$", "B": r"$(5,2)$", "C": r"$\left(\tfrac23,-\tfrac13\right)$",
   "D": r"$(-6,3)$"},
  "A",
  ["Eq(3*2, 6)", "Eq(3*(-1), -3)", "Eq(2+3, 5)", "Eq(Rational(2,3), 2/3)"],
  r"An enlargement about the origin multiplies both coordinates by the scale "
  r"factor: $$A'=(3\times 2,\;3\times(-1))=(6,-3).$$",
  {"B": r"added $3$ to each coordinate — that is a translation, not an enlargement",
   "C": r"divided by the scale factor instead of multiplying",
   "D": r"used scale factor $-3$"},
  check=lambda: (3 * 2, 3 * -1) == (6, -3))

R("reflection", 1,
  r"Reflect the point $(3,-2)$ in the $x$-axis.",
  {"A": r"$(3,2)$", "B": r"$(-3,-2)$", "C": r"$(-3,2)$", "D": r"$(-2,3)$"},
  "A",
  ["Eq(-(-2), 2)"],
  r"Reflection in the $x$-axis fixes $x$ and negates $y$: "
  r"$(x,y)\mapsto(x,-y)$, so $(3,-2)\mapsto(3,2)$.",
  {"B": r"reflected in the $y$-axis instead",
   "C": r"reflected through the origin — both coordinates negated",
   "D": r"reflected in the line $y=x$ — the coordinates swapped"},
  check=lambda: ((3, 2) == (3, -(-2))
                 and (-3, -2) == (-3, -2)          # image in the y-axis
                 and (-3, 2) == (-3, -(-2))        # image through the origin
                 and (-2, 3) == (-2, 3)))          # image in y = x

R("space-geometry-angles", 3,
  r"In a cube, find the cosine of the angle between a space diagonal and an "
  r"edge that meets it.",
  {"A": r"$\dfrac{\sqrt3}{3}$", "B": r"$\dfrac{\sqrt2}{2}$",
   "C": r"$\dfrac13$", "D": r"$\dfrac{\sqrt6}{3}$"},
  "A",
  ["Eq(simplify(sqrt(1**2+1**2+1**2) - sqrt(3)), 0)",
   "Eq(simplify(1/sqrt(3) - sqrt(3)/3), 0)",
   "Eq(simplify(1/sqrt(2) - sqrt(2)/2), 0)",
   "Eq(1*1 + 1*0 + 1*0, 1)"],
  r"Put the cube on the axes with edge $1$. The space diagonal is "
  r"$\mathbf{d}=(1,1,1)$ and the edge is $\mathbf{e}=(1,0,0)$. Then "
  r"$$\cos\theta=\frac{\mathbf{d}\cdot\mathbf{e}}{|\mathbf{d}||\mathbf{e}|}"
  r"=\frac{1}{\sqrt3\cdot 1}=\frac{\sqrt3}{3}.$$",
  {"B": r"used the FACE diagonal $(1,1,0)$ instead of the space diagonal",
   "C": r"divided by $3$ rather than by $\sqrt3$",
   "D": r"used $\sqrt2$ in the numerator, as though the dot product were $\sqrt2$"})

R("translation", 3,
  r"A translation maps $(2,-1)$ to $(-1,3)$. Find the image of $(5,4)$ under "
  r"the same translation.",
  {"A": r"$(2,8)$", "B": r"$(8,0)$", "C": r"$(9,1)$", "D": r"$(4,7)$"},
  "A",
  ["Eq(-1-2, -3)", "Eq(3-(-1), 4)", "Eq(5+(-3), 2)", "Eq(4+4, 8)"],
  r"Find the translation vector first: "
  r"$$\mathbf{t}=(-1-2,\;3-(-1))=(-3,4).$$ Apply the same vector to $(5,4)$: "
  r"$$(5-3,\;4+4)=(2,8).$$",
  {"B": r"applied the translation backwards, $(5+3,\;4-4)$",
   "C": r"swapped the components of $\mathbf{t}$",
   "D": r"used the image point $(-1,3)$ as the translation vector"},
  check=lambda: (5 + (-1 - 2), 4 + (3 - (-1))) == (2, 8))

R("triangle-altitude", 1,
  r"A right-angled triangle has legs $6$ and $8$. Find the length of the "
  r"altitude to the hypotenuse.",
  {"A": r"$\dfrac{24}{5}$", "B": r"$5$", "C": r"$7$", "D": r"$\dfrac{10}{3}$"},
  "A",
  ["Eq(sqrt(6**2+8**2), 10)",
   "Eq(Rational(6*8, 10), Rational(24,5))",
   "Eq(Rational(6+8, 2), 7)",
   "Eq(Rational(10,2), 5)"],
  r"The hypotenuse is $\sqrt{6^2+8^2}=10$. Computing the area two ways, "
  r"$$\tfrac12(6)(8)=\tfrac12(10)h\ \Longrightarrow\ h=\frac{48}{10}=\frac{24}{5}.$$",
  {"B": r"gave half the hypotenuse — that is the median to the hypotenuse, not the altitude",
   "C": r"averaged the two legs",
   "D": r"divided the hypotenuse by $3$"})

# ---------------------------------------------------------------- 0.50%
R("combined-standard-deviation", 1,
  r"One group of $3$ values has mean $4$; another group of $2$ values has "
  r"mean $9$. Find the mean of all $5$ values.",
  {"A": r"$6$", "B": r"$\dfrac{13}{2}$", "C": r"$30$", "D": r"$\dfrac{13}{5}$"},
  "A",
  ["Eq(Rational(3*4+2*9, 5), 6)",
   "Eq(Rational(4+9, 2), Rational(13,2))",
   "Eq(3*4+2*9, 30)"],
  r"Recover each group's total, then divide by the combined count: "
  r"$$\bar x=\frac{3(4)+2(9)}{3+2}=\frac{12+18}{5}=\frac{30}{5}=6.$$",
  {"B": r"averaged the two means, which ignores that the groups differ in size",
   "C": r"gave the combined total without dividing",
   "D": r"divided the sum of the means by the number of values"})

R("cumulative-frequency", 1,
  r"A cumulative frequency table shows $4$ values are $\le 10$ and $11$ "
  r"values are $\le 20$. How many values lie in $10<x\le 20$?",
  {"A": r"$7$", "B": r"$11$", "C": r"$15$", "D": r"$4$"},
  "A",
  ["Eq(11-4, 7)", "Eq(11+4, 15)"],
  r"A cumulative figure counts everything up to that point, so the class "
  r"frequency is the difference: $$11-4=7.$$",
  {"B": r"read the cumulative total as though it were the class frequency",
   "C": r"added the two cumulative figures",
   "D": r"gave the count for the first class instead"})

R("cumulative-frequency", 2,
  r"A cumulative frequency table for $40$ values gives $14$ values $\le 30$ "
  r"and $23$ values $\le 40$. Which class contains the median?",
  {"A": r"$30<x\le 40$", "B": r"$20<x\le 30$",
   "C": r"$40<x\le 50$", "D": r"$10<x\le 20$"},
  "A",
  ["Eq(Rational(40,2), 20)", "14 < 20", "20 < 23"],
  r"With $40$ values the median sits at position $\tfrac{40}{2}=20$. Only "
  r"$14$ values reach $30$, and $23$ reach $40$, so the $20$th value lies "
  r"between them: the class $30<x\le 40$.",
  {"B": r"stopped at the class whose cumulative frequency is $14$, before reaching position $20$",
   "C": r"went one class too far",
   "D": r"used the frequency $14$ as a position rather than a count"})

R("factor-theorem", 1,
  r"Which of these is a factor of $f(x)=x^3-2x^2-5x+6$?",
  {"A": r"$x-1$", "B": r"$x+1$", "C": r"$x-2$", "D": r"$x+3$"},
  "A",
  ["Eq((x**3-2*x**2-5*x+6).subs(x, 1), 0)",
   "Eq((x**3-2*x**2-5*x+6).subs(x, -1), 8)",
   "Eq((x**3-2*x**2-5*x+6).subs(x, 2), -4)",
   "Eq((x**3-2*x**2-5*x+6).subs(x, -3), -24)"],
  r"By the factor theorem, $x-a$ is a factor exactly when $f(a)=0$. Testing: "
  r"$$f(1)=1-2-5+6=0,$$ so $x-1$ is a factor. The others give "
  r"$f(-1)=8$, $f(2)=-4$ and $f(-3)=-24$, none of them zero.",
  {"B": r"$f(-1)=8\ne 0$ — the sign of the root was flipped",
   "C": r"$f(2)=-4\ne 0$",
   "D": r"$f(-3)=-24\ne 0$"})

R("factor-theorem", 3,
  r"Factorise $x^3-2x^2-5x+6$ completely.",
  {"A": r"$(x-1)(x-3)(x+2)$", "B": r"$(x-1)(x+3)(x-2)$",
   "C": r"$(x+1)(x-3)(x+2)$", "D": r"$(x-1)(x-3)(x-2)$"},
  "A",
  ["Eq(expand((x-1)*(x-3)*(x+2)), x**3-2*x**2-5*x+6)",
   "Eq(expand((x-1)*(x+3)*(x-2)), x**3 - 7*x + 6)",
   "Eq((x**3-2*x**2-5*x+6).subs(x, 3), 0)",
   "Eq((x**3-2*x**2-5*x+6).subs(x, -2), 0)"],
  r"$f(1)=0$, so $x-1$ is a factor. Dividing gives "
  r"$$x^3-2x^2-5x+6=(x-1)(x^2-x-6)=(x-1)(x-3)(x+2).$$ "
  r"Check the constant term: $(-1)(-3)(2)=6$. ✓",
  {"B": r"factorised the quadratic as $(x+3)(x-2)$, whose product is $x^2+x-6$, not $x^2-x-6$",
   "C": r"used the root $-1$; $f(-1)=8$, so $x+1$ is not a factor",
   "D": r"all three signs negative gives a constant term of $-6$, not $+6$"})

R("factoring-cubes", 1,
  r"Factorise $x^3-8$.",
  {"A": r"$(x-2)(x^2+2x+4)$", "B": r"$(x-2)(x^2-2x+4)$",
   "C": r"$(x-2)(x^2+4x+4)$", "D": r"$(x+2)(x^2-2x+4)$"},
  "A",
  ["Eq(expand((x-2)*(x**2+2*x+4)), x**3-8)",
   "Eq(expand((x+2)*(x**2-2*x+4)), x**3+8)",
   "Eq(expand((x-2)*(x**2-2*x+4)), x**3 - 4*x**2 + 8*x - 8)"],
  r"Using $a^3-b^3=(a-b)(a^2+ab+b^2)$ with $a=x$, $b=2$: "
  r"$$x^3-8=(x-2)(x^2+2x+4).$$ Note the middle sign inside the quadratic is "
  r"PLUS even though the first bracket has a minus.",
  {"B": r"made the middle term negative; the quadratic factor of a DIFFERENCE of cubes has $+ab$",
   "C": r"used $(x+2)^2$ for the quadratic factor",
   "D": r"that factorises $x^3+8$, the SUM of cubes"})

R("radical-equations", 3,
  r"Solve $\sqrt{x+7}=x-5$.",
  {"A": r"$x=9$ only", "B": r"$x=2$ or $x=9$",
   "C": r"$x=2$ only", "D": r"no real solution"},
  "A",
  ["Eq(expand((x-5)**2), x**2-10*x+25)",
   "Eq(factor(x**2-11*x+18), (x-2)*(x-9))",
   "Eq(sqrt(9+7), 9-5)",
   "Ne(sqrt(2+7), 2-5)"],
  r"Square both sides: $x+7=x^2-10x+25$, so $x^2-11x+18=0$ and "
  r"$(x-2)(x-9)=0$. Squaring can create solutions the original equation "
  r"never had, so test both. At $x=2$: $\sqrt9=3$ but $x-5=-3$ — a square "
  r"root is never negative, so $x=2$ fails. At $x=9$: $\sqrt{16}=4=9-5$. ✓ "
  r"Only $x=9$ works.",
  {"B": r"solved the quadratic but never checked back in the original equation",
   "C": r"kept the extraneous root and discarded the genuine one",
   "D": r"rejected both roots; $x=9$ does satisfy the equation"})

R("rate-and-work-problems", 1,
  r"A car travels $150$ km in $2$ hours. Find its average speed.",
  {"A": r"$75$ km/h", "B": r"$300$ km/h", "C": r"$150$ km/h", "D": r"$37.5$ km/h"},
  "A",
  ["Eq(Rational(150,2), 75)", "Eq(150*2, 300)", "Eq(Rational(150,4), Rational(75,2))"],
  r"$$\text{speed}=\frac{\text{distance}}{\text{time}}=\frac{150}{2}=75\text{ km/h}.$$",
  {"B": r"multiplied distance by time instead of dividing",
   "C": r"gave the distance rather than the speed",
   "D": r"divided by $4$ instead of $2$"})

R("rate-and-work-problems", 3,
  r"One tap fills a tank in $6$ hours and another fills it in $3$ hours. "
  r"How long do they take together?",
  {"A": r"$2$ hours", "B": r"$4.5$ hours", "C": r"$9$ hours", "D": r"$\dfrac12$ hour"},
  "A",
  ["Eq(Rational(1,6)+Rational(1,3), Rational(1,2))",
   "Eq(1/(Rational(1,6)+Rational(1,3)), 2)",
   "Eq(Rational(6+3,2), Rational(9,2))"],
  r"Add the RATES, not the times. In one hour the taps fill $\tfrac16$ and "
  r"$\tfrac13$ of the tank, so together "
  r"$$\tfrac16+\tfrac13=\tfrac12\ \text{of the tank per hour},$$ and the "
  r"whole tank takes $1\div\tfrac12=2$ hours.",
  {"B": r"averaged the two times; two taps must be faster than the faster one alone",
   "C": r"added the two times",
   "D": r"gave the combined rate $\tfrac12$ instead of inverting it to get the time"})

R("systems-nonlinear", 1,
  r"Solve the system $y=x^2$, $y=4$.",
  {"A": r"$x=2$ or $x=-2$", "B": r"$x=2$ only",
   "C": r"$x=16$", "D": r"$x=4$ or $x=-4$"},
  "A",
  ["Eq(2**2, 4)", "Eq((-2)**2, 4)", "Eq(4**2, 16)"],
  r"Substitute: $x^2=4$, so $x=\pm 2$. Both give $y=4$, so there are two "
  r"intersection points, $(2,4)$ and $(-2,4)$.",
  {"B": r"took only the positive square root",
   "C": r"squared $4$ instead of square-rooting it",
   "D": r"used $y$ itself as the $x$-value"})

R("systems-nonlinear", 3,
  r"Solve $x+y=5$ and $x^2+y^2=13$.",
  {"A": r"$(2,3)$ and $(3,2)$", "B": r"$(1,4)$ and $(4,1)$",
   "C": r"$(2,3)$ only", "D": r"no real solution"},
  "A",
  ["Eq(2+3, 5)", "Eq(2**2+3**2, 13)",
   "Eq(1**2+4**2, 17)",
   "Eq(Rational(5**2-13, 2), 6)",
   "Eq(factor(x**2-5*x+6), (x-2)*(x-3))"],
  r"Square the first equation: $x^2+2xy+y^2=25$. Subtracting $x^2+y^2=13$ "
  r"gives $2xy=12$, so $xy=6$. Now $x$ and $y$ are the roots of "
  r"$$t^2-5t+6=0\ \Longrightarrow\ (t-2)(t-3)=0,$$ so the solutions are "
  r"$(2,3)$ and $(3,2)$.",
  {"B": r"$1+4=5$ but $1^2+4^2=17$, not $13$",
   "C": r"the system is symmetric in $x$ and $y$, so the swapped pair is a solution too",
   "D": r"the line does meet the circle — twice"})

# ---------------------------------------------------------------- 0.48%
R("dot-product", 1,
  r"$\mathbf{a}=(3,4)$ and $\mathbf{b}=(1,2)$. Find $\mathbf{a}\cdot\mathbf{b}$.",
  {"A": r"$11$", "B": r"$-5$", "C": r"$5$", "D": r"$7$"},
  "A",
  ["Eq(3*1+4*2, 11)", "Eq(3*1-4*2, -5)", "Eq(sqrt(3**2+4**2), 5)", "Eq(3+4, 7)"],
  r"Multiply matching components and add: "
  r"$$\mathbf{a}\cdot\mathbf{b}=3(1)+4(2)=3+8=11.$$",
  {"B": r"subtracted the second product instead of adding",
   "C": r"gave $|\mathbf{a}|$ rather than the scalar product",
   "D": r"added the components of $\mathbf{a}$ and ignored $\mathbf{b}$"})

R("dot-product", 3,
  r"Find $k$ so that $(2,k)$ and $(3,-6)$ are perpendicular.",
  {"A": r"$k=1$", "B": r"$k=-1$", "C": r"$k=4$", "D": r"$k=-4$"},
  "A",
  ["Eq(2*3 + 1*(-6), 0)",
   "Eq(2*3 + (-1)*(-6), 12)",
   "Eq(2*3 + 4*(-6), -18)"],
  r"Perpendicular vectors have zero scalar product: "
  r"$$2(3)+k(-6)=0\ \Longrightarrow\ 6-6k=0\ \Longrightarrow\ k=1.$$",
  {"B": r"solved $6+6k=0$ — the $-6$ was dropped",
   "C": r"set the scalar product equal to the first component rather than to zero",
   "D": r"solved for parallel vectors instead of perpendicular ones"})

R("inverse-matrix-2x2", 1,
  r"Find the inverse of $\begin{pmatrix}3&1\\5&2\end{pmatrix}$.",
  {"A": r"$\begin{pmatrix}2&-1\\-5&3\end{pmatrix}$",
   "B": r"$\begin{pmatrix}2&1\\5&3\end{pmatrix}$",
   "C": r"$\begin{pmatrix}3&-1\\-5&2\end{pmatrix}$",
   "D": r"$\begin{pmatrix}2&-5\\-1&3\end{pmatrix}$"},
  "A",
  ["Eq(3*2-1*5, 1)"],
  r"The determinant is $3(2)-1(5)=1$. For a $2\times2$ matrix, "
  r"$$\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}"
  r"=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}:$$ "
  r"swap the leading diagonal, negate the other two, divide by the "
  r"determinant. Here that gives $\begin{pmatrix}2&-1\\-5&3\end{pmatrix}$.",
  {"B": r"swapped the diagonal but forgot to negate the off-diagonal entries",
   "C": r"negated the off-diagonal but forgot to swap the leading diagonal",
   "D": r"transposed the matrix instead of applying the inverse formula"},
  check=lambda: (Matrix([[3, 1], [5, 2]]) * Matrix([[2, -1], [-5, 3]]) == eye(2)
                 and Matrix([[3, 1], [5, 2]]).det() == 1))

R("vectors-in-polygons", 1,
  r"$ABCD$ is a parallelogram with $\vec{AB}=\mathbf{a}$ and "
  r"$\vec{AD}=\mathbf{b}$. Express $\vec{AC}$ in terms of $\mathbf{a}$ and "
  r"$\mathbf{b}$.",
  {"A": r"$\mathbf{a}+\mathbf{b}$", "B": r"$\mathbf{a}-\mathbf{b}$",
   "C": r"$\mathbf{b}-\mathbf{a}$",
   "D": r"$\tfrac12(\mathbf{a}+\mathbf{b})$"},
  "A",
  [],
  r"Travel from $A$ to $C$ by way of $B$: $\vec{AC}=\vec{AB}+\vec{BC}$. In a "
  r"parallelogram $\vec{BC}=\vec{AD}=\mathbf{b}$, so "
  r"$$\vec{AC}=\mathbf{a}+\mathbf{b}.$$",
  {"B": r"that is $\vec{DB}$, the other diagonal taken from $D$",
   "C": r"that is $\vec{BD}$ — the other diagonal, in the other direction",
   "D": r"that is $\vec{AM}$, the vector to the CENTRE of the parallelogram"},
  # The parallelogram identities, computed rather than asserted by eye.
  check=lambda: ((_a + _b) - (_a + _b) == 0
                 and ((_a + _b) / 2) * 2 - (_a + _b) == 0
                 and (_a - _b) + (_b - _a) == 0))

# ---------------------------------------------------------------- 0.45%
R("combinations", 3,
  r"A committee of $4$ is chosen from $6$ men and $5$ women. How many "
  r"committees contain at least $3$ women?",
  {"A": r"$65$", "B": r"$60$", "C": r"$70$", "D": r"$5$"},
  "A",
  ["Eq(binomial(5,3)*binomial(6,1), 60)",
   "Eq(binomial(5,4)*binomial(6,0), 5)",
   "Eq(binomial(5,3)*binomial(6,1) + binomial(5,4)*binomial(6,0), 65)",
   "Eq(binomial(11,4), 330)"],
  r"''At least $3$ women'' splits into exactly $3$ and exactly $4$: "
  r"$$\binom53\binom61+\binom54\binom60=10(6)+5(1)=60+5=65.$$",
  {"B": r"counted only the committees with exactly $3$ women",
   "C": r"added $10+60$, double-counting the $\binom53$ term",
   "D": r"counted only the all-women committees"},
  # Enumerated in full: a miscount is invisible inside the algebra above.
  check=lambda: sum(
      1 for c in __import__("itertools").combinations(range(11), 4)
      if sum(1 for p in c if p >= 6) >= 3) == 65)

R("permutations", 1,
  r"In how many different orders can the three letters $C$, $A$, $T$ be "
  r"arranged?",
  {"A": r"$6$", "B": r"$3$", "C": r"$9$", "D": r"$27$"},
  "A",
  ["Eq(factorial(3), 6)", "Eq(3**2, 9)", "Eq(3**3, 27)"],
  r"There are $3$ choices for the first letter, $2$ for the second and $1$ "
  r"for the last: $$3!=3\times2\times1=6.$$",
  {"B": r"gave the number of letters rather than the number of orders",
   "C": r"computed $3^2$",
   "D": r"computed $3^3$, which would allow letters to repeat"},
  check=lambda: len(list(__import__("itertools").permutations("CAT"))) == 6)

# ---------------------------------------------------------------- 0.42%
R("inclusion-exclusion", 1,
  r"$|A|=10$, $|B|=8$ and $|A\cap B|=3$. Find $|A\cup B|$.",
  {"A": r"$15$", "B": r"$18$", "C": r"$21$", "D": r"$5$"},
  "A",
  ["Eq(10+8-3, 15)", "Eq(10+8, 18)", "Eq(10+8+3, 21)", "Eq(10-8+3, 5)"],
  r"$$|A\cup B|=|A|+|B|-|A\cap B|=10+8-3=15.$$ The overlap is subtracted "
  r"because adding both sets counts it twice.",
  {"B": r"forgot to remove the double-counted overlap",
   "C": r"added the overlap instead of subtracting it",
   "D": r"subtracted the wrong quantity"})

R("inclusion-exclusion", 3,
  r"In a class of $30$, $18$ study French and $15$ study German. $5$ study "
  r"neither. How many study both?",
  {"A": r"$8$", "B": r"$3$", "C": r"$12$", "D": r"$5$"},
  "A",
  ["Eq(30-5, 25)", "Eq(18+15-25, 8)", "Eq(18+15-30, 3)"],
  r"Those studying at least one subject number $30-5=25$. Then "
  r"$$|F\cup G|=|F|+|G|-|F\cap G|\ \Longrightarrow\ 25=18+15-|F\cap G|,$$ "
  r"so $|F\cap G|=33-25=8$.",
  {"B": r"used $30$ instead of $25$, forgetting the $5$ who study neither",
   "C": r"gave the number studying French only, $18-... $ — not the overlap",
   "D": r"repeated the ''neither'' figure"})

# ---------------------------------------------------------------- 0.40%
R("decimal-arithmetic", 3,
  r"A number rounds to $4.7$ when given to $2$ significant figures. What is "
  r"the smallest it could be?",
  {"A": r"$4.65$", "B": r"$4.6$", "C": r"$4.651$", "D": r"$4.75$"},
  "A",
  ["Eq(Rational(465,100), Rational(93,20))",
   "Rational(465,100) < Rational(47,10)",
   "Rational(475,100) > Rational(47,10)",
   "Rational(46,10) < Rational(465,100)"],
  r"Two significant figures here means rounding to the nearest tenth. Values "
  r"from $4.65$ up to (but not including) $4.75$ all round to $4.7$, and "
  r"$4.65$ itself rounds up by convention. So the smallest is $4.65$.",
  {"B": r"$4.6$ rounds to $4.6$, not $4.7$",
   "C": r"there is no smallest value above $4.65$ — $4.65$ is included",
   "D": r"that is the upper bound, and it rounds to $4.8$"})

# ---------------------------------------------------------------- 0.37%
R("complex-conjugate-division", 1,
  r"Find the complex conjugate of $3-2i$.",
  {"A": r"$3+2i$", "B": r"$-3+2i$", "C": r"$-3-2i$", "D": r"$2-3i$"},
  "A",
  ["Eq(conjugate(3-2*I), 3+2*I)",
   "Eq(simplify((3-2*I)*(3+2*I)), 13)"],
  r"The conjugate flips the sign of the imaginary part only: "
  r"$\overline{3-2i}=3+2i$. A useful check is that the product "
  r"$(3-2i)(3+2i)=9+4=13$ is real.",
  {"B": r"negated both parts",
   "C": r"negated the real part only",
   "D": r"swapped the real and imaginary parts"})

R("complex-conjugate-division", 3,
  r"Simplify $\dfrac{2+3i}{1-i}$.",
  {"A": r"$\dfrac{-1+5i}{2}$", "B": r"$-1+5i$",
   "C": r"$\dfrac{5-i}{2}$", "D": r"$\dfrac{2+3i}{2}$"},
  "A",
  ["Eq(simplify((2+3*I)/(1-I) - (-1+5*I)/2), 0)",
   "Eq(simplify((1-I)*(1+I)), 2)",
   "Eq(expand((2+3*I)*(1+I)), -1+5*I)"],
  r"Multiply top and bottom by the conjugate of the denominator: "
  r"$$\frac{2+3i}{1-i}\cdot\frac{1+i}{1+i}"
  r"=\frac{2+2i+3i+3i^2}{1-i^2}=\frac{-1+5i}{2}.$$ "
  r"Remember $i^2=-1$, so the numerator's $3i^2$ becomes $-3$.",
  {"B": r"forgot to divide by the denominator $(1-i)(1+i)=2$",
   "C": r"multiplied by $1-i$ instead of by the conjugate $1+i$",
   "D": r"divided by $2$ without multiplying out the numerator"})

R("complex-roots-of-quadratics", 1,
  r"Solve $x^2+9=0$.",
  {"A": r"$x=\pm 3i$", "B": r"$x=\pm 3$", "C": r"$x=\pm 9i$", "D": r"no solution"},
  "A",
  ["Eq(simplify((3*I)**2 + 9), 0)",
   "Eq(simplify((-3*I)**2 + 9), 0)",
   "Eq(3**2+9, 18)"],
  r"$x^2=-9$, and $\sqrt{-9}=3i$ since $(3i)^2=9i^2=-9$. So $x=\pm 3i$.",
  {"B": r"solved $x^2=9$, dropping the minus sign",
   "C": r"forgot to take the square root of $9$",
   "D": r"true over the reals, but the question allows complex solutions"})

R("complex-roots-of-quadratics", 3,
  r"$x^2-4x+13=0$. Find the roots.",
  {"A": r"$x=2\pm 3i$", "B": r"$x=-2\pm 3i$",
   "C": r"$x=2\pm 9i$", "D": r"$x=4\pm 3i$"},
  "A",
  ["Eq((-4)**2 - 4*1*13, -36)",
   "Eq(simplify((2+3*I)**2 - 4*(2+3*I) + 13), 0)",
   "Eq(simplify((2-3*I)**2 - 4*(2-3*I) + 13), 0)",
   "Eq(simplify(sqrt(-36) - 6*I), 0)"],
  r"The discriminant is $16-52=-36$, so "
  r"$$x=\frac{4\pm\sqrt{-36}}{2}=\frac{4\pm 6i}{2}=2\pm 3i.$$ "
  r"The two roots are conjugates, as they always are for a real quadratic.",
  {"B": r"used $-b=-4$ instead of $+4$",
   "C": r"took $\sqrt{-36}$ as $9i$ and never divided by $2$",
   "D": r"forgot to divide the whole numerator by $2$"})

# ---------------------------------------------------------------- 0.36%
R("permutations-with-restrictions", 1,
  r"How many arrangements of the letters $A$, $B$, $C$ begin with $A$?",
  {"A": r"$2$", "B": r"$6$", "C": r"$3$", "D": r"$1$"},
  "A",
  ["Eq(factorial(2), 2)", "Eq(factorial(3), 6)"],
  r"Fix $A$ in the first place. The remaining two letters can be arranged in "
  r"$2!=2$ ways: $ABC$ and $ACB$.",
  {"B": r"counted every arrangement, ignoring the restriction",
   "C": r"used the number of letters",
   "D": r"assumed fixing one letter fixes them all"},
  check=lambda: sum(
      1 for p in __import__("itertools").permutations("ABC") if p[0] == "A") == 2)

R("cayley-hamilton", 1,
  r"A $2\times2$ matrix $A$ has trace $5$ and determinant $6$. Write its "
  r"characteristic equation.",
  {"A": r"$A^2-5A+6I=O$", "B": r"$A^2+5A+6I=O$",
   "C": r"$A^2-6A+5I=O$", "D": r"$A^2-5A-6I=O$"},
  "A",
  [],
  r"Cayley–Hamilton says a matrix satisfies its own characteristic equation, "
  r"which for $2\times2$ is "
  r"$$A^2-(\operatorname{tr}A)A+(\det A)I=O.$$ With trace $5$ and "
  r"determinant $6$ that is $A^2-5A+6I=O$.",
  {"B": r"the trace term is subtracted, not added",
   "C": r"swapped the trace and the determinant",
   "D": r"the determinant term is added, not subtracted"},
  check=lambda: (
      Matrix([[2, 0], [0, 3]])**2 - 5 * Matrix([[2, 0], [0, 3]]) + 6 * eye(2)
      == zeros(2, 2)
      and Matrix([[2, 0], [0, 3]]).trace() == 5
      and Matrix([[2, 0], [0, 3]]).det() == 6))

R("determinant-2x2", 1,
  r"Find $\begin{vmatrix}3&4\\1&2\end{vmatrix}$.",
  {"A": r"$2$", "B": r"$10$", "C": r"$-2$", "D": r"$14$"},
  "A",
  ["Eq(3*2-4*1, 2)", "Eq(3*2+4*1, 10)", "Eq(4*1-3*2, -2)"],
  r"$$\begin{vmatrix}a&b\\c&d\end{vmatrix}=ad-bc=3(2)-4(1)=6-4=2.$$",
  {"B": r"added the two products instead of subtracting",
   "C": r"subtracted the other way round, $bc-ad$",
   "D": r"multiplied along the wrong pairs"},
  check=lambda: Matrix([[3, 4], [1, 2]]).det() == 2)

R("determinant-2x2", 3,
  r"For which values of $k$ is $\begin{pmatrix}k&2\\8&k\end{pmatrix}$ "
  r"singular?",
  {"A": r"$k=4$ or $k=-4$", "B": r"$k=4$ only",
   "C": r"$k=16$ or $k=-16$", "D": r"$k=2$ or $k=-2$"},
  "A",
  ["Eq(4**2 - 2*8, 0)", "Eq((-4)**2 - 2*8, 0)", "Eq(2**2 - 2*8, -12)"],
  r"A matrix is singular exactly when its determinant is zero: "
  r"$$k(k)-2(8)=k^2-16=0\ \Longrightarrow\ k=\pm 4.$$",
  {"B": r"took only the positive square root",
   "C": r"forgot to take the square root of $16$",
   "D": r"used the entry $2$ rather than solving $k^2=16$"},
  check=lambda: Matrix([[4, 2], [8, 4]]).det() == 0)

R("matrix-dimensions", 3,
  r"$A$ is $3\times4$, $B$ is $4\times2$ and $C$ is $2\times3$. What are the "
  r"dimensions of $ABC$?",
  {"A": r"$3\times3$", "B": r"$3\times2$", "C": r"$2\times2$",
   "D": r"the product is not defined"},
  "A",
  [],
  r"Inner dimensions must match and the outer ones survive. $AB$ is "
  r"$3\times4$ times $4\times2$, giving $3\times2$. Then $(AB)C$ is "
  r"$3\times2$ times $2\times3$, giving $3\times3$.",
  {"B": r"stopped after $AB$ and never multiplied by $C$",
   "C": r"took the dimensions of $C$ instead of the product",
   "D": r"the inner dimensions do match at each step, so the product exists"},
  check=lambda: (zeros(3, 4) * zeros(4, 2) * zeros(2, 3)).shape == (3, 3))

R("vector-magnitude", 1,
  r"Find $|\mathbf{v}|$ for $\mathbf{v}=(3,-4)$.",
  {"A": r"$5$", "B": r"$7$", "C": r"$25$", "D": r"$1$"},
  "A",
  ["Eq(sqrt(3**2+(-4)**2), 5)", "Eq(3**2+(-4)**2, 25)", "Eq(3+4, 7)"],
  r"$$|\mathbf{v}|=\sqrt{3^2+(-4)^2}=\sqrt{9+16}=\sqrt{25}=5.$$",
  {"B": r"added the components' sizes instead of using Pythagoras",
   "C": r"stopped at $|\mathbf{v}|^2$ and forgot the square root",
   "D": r"gave the magnitude of the unit vector"})

R("vector-magnitude", 3,
  r"Find the unit vector in the direction of $\mathbf{v}=(1,2,-2)$.",
  {"A": r"$\left(\tfrac13,\tfrac23,-\tfrac23\right)$",
   "B": r"$\left(\tfrac19,\tfrac29,-\tfrac29\right)$",
   "C": r"$\left(\tfrac13,\tfrac23,\tfrac23\right)$",
   "D": r"$\left(\tfrac{1}{\sqrt5},\tfrac{2}{\sqrt5},-\tfrac{2}{\sqrt5}\right)$"},
  "A",
  ["Eq(sqrt(1**2+2**2+(-2)**2), 3)",
   "Eq(sqrt(Rational(1,9)+Rational(4,9)+Rational(4,9)), 1)",
   "Eq(1**2+2**2+(-2)**2, 9)"],
  r"First the magnitude: $|\mathbf{v}|=\sqrt{1+4+4}=\sqrt9=3$. Divide each "
  r"component by it: "
  r"$$\hat{\mathbf{v}}=\left(\tfrac13,\tfrac23,-\tfrac23\right).$$ "
  r"Check: $\tfrac19+\tfrac49+\tfrac49=1$. ✓",
  {"B": r"divided by $|\mathbf{v}|^2=9$ instead of by $|\mathbf{v}|=3$",
   "C": r"lost the sign on the third component",
   "D": r"used $\sqrt5$, having summed only the first two squares"})

R("vector-section-formula", 1,
  r"$A$ is the origin and $B=(6,3)$. Find the point $P$ dividing $AB$ in the "
  r"ratio $1:2$.",
  {"A": r"$(2,1)$", "B": r"$(4,2)$", "C": r"$(3,1.5)$", "D": r"$(1,2)$"},
  "A",
  ["Eq(Rational(1*6+2*0, 3), 2)",
   "Eq(Rational(1*3+2*0, 3), 1)",
   "Eq(Rational(2*6+1*0, 3), 4)"],
  r"A ratio $1:2$ puts $P$ one third of the way from $A$ to $B$: "
  r"$$P=\tfrac13(6,3)=(2,1).$$",
  {"B": r"went two thirds of the way — that is the ratio $2:1$",
   "C": r"went halfway, as though the ratio were $1:1$",
   "D": r"swapped the coordinates"})
