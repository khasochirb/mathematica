"""Batch B — the next 20 thin skills, 0.69% down to 0.52% exam weight.

Difficulty is the ENGINE scale: 1 easy, 2 medium, 3 hard.
"""

from rung_bank import R

# ---------------------------------------------------------------- 0.69%
R("cone", 1,
  r"A cone has base radius $3$ and height $4$. Find its volume.",
  {"A": r"$12\pi$", "B": r"$36\pi$", "C": r"$16\pi$", "D": r"$4\pi$"},
  "A",
  ["Eq(Rational(1,3)*pi*3**2*4, 12*pi)",
   "Eq(pi*3**2*4, 36*pi)",
   "Eq(Rational(1,3)*pi*4**2*3, 16*pi)",
   "Eq(Rational(1,3)*pi*3*4, 4*pi)"],
  r"$$V=\tfrac13\pi r^2h=\tfrac13\pi(3)^2(4)=\tfrac13\pi(36)=12\pi.$$",
  {"B": r"used the cylinder formula $\pi r^2h$ and dropped the factor $\tfrac13$",
   "C": r"swapped the radius and the height",
   "D": r"wrote $\tfrac13\pi rh$ — the radius must be squared"})

R("inscribed-circumscribed-circles", 1,
  r"A circle is circumscribed about a right-angled triangle whose hypotenuse "
  r"is $10$. Find the radius of that circle.",
  {"A": r"$5$", "B": r"$10$", "C": r"$\dfrac{10}{3}$", "D": r"$\dfrac{5}{2}$"},
  "A",
  ["Eq(Rational(10,2), 5)",
   "Eq(2*5, 10)",
   "Eq(Rational(10,4), Rational(5,2))"],
  r"By Thales' theorem the hypotenuse of a right-angled triangle is a "
  r"diameter of its circumcircle. So $$R=\frac{10}{2}=5.$$",
  {"B": r"gave the diameter instead of the radius",
   "C": r"used the centroid ratio $\tfrac13$, which belongs to medians, not to this circle",
   "D": r"halved the hypotenuse twice"})

R("line-equation", 3,
  r"A line passes through $(2,-1)$ and is perpendicular to $3x-4y=8$. "
  r"Find its equation.",
  {"A": r"$4x+3y=5$", "B": r"$3x-4y=10$",
   "C": r"$4x-3y=11$", "D": r"$3x+4y=2$"},
  "A",
  ["Eq(solve(Eq(3*x-4*y, 8), y)[0], Rational(3,4)*x - 2)",
   "Eq(Rational(3,4)*Rational(-4,3), -1)",
   "Eq((4*x+3*y).subs([(x,2),(y,-1)]), 5)",
   "Eq(solve(Eq(4*x+3*y, 5), y)[0], Rational(5,3) - Rational(4,3)*x)"],
  r"Rearrange the given line to $y=\tfrac34x-2$, so its gradient is $\tfrac34$. "
  r"A perpendicular line has gradient $-\tfrac43$, since "
  r"$\tfrac34\cdot\left(-\tfrac43\right)=-1$. Through $(2,-1)$: "
  r"$$y+1=-\tfrac43(x-2)\ \Longrightarrow\ 3y+3=-4x+8\ \Longrightarrow\ 4x+3y=5.$$ "
  r"Every option passes through $(2,-1)$, so the point alone cannot decide it "
  r"— only the gradient can.",
  {"B": r"kept the same gradient $\tfrac34$; that is the PARALLEL line",
   "C": r"took the reciprocal but not the negative, giving gradient $\tfrac43$",
   "D": r"swapped the coefficients without negating, giving gradient $-\tfrac34$"})

R("pyramid-volume-surface", 1,
  r"A pyramid has a square base of side $6$ and height $5$. Find its volume.",
  {"A": r"$60$", "B": r"$180$", "C": r"$90$", "D": r"$10$"},
  "A",
  ["Eq(Rational(1,3)*6**2*5, 60)",
   "Eq(6**2*5, 180)",
   "Eq(Rational(1,2)*6**2*5, 90)",
   "Eq(Rational(1,3)*6*5, 10)"],
  r"$$V=\tfrac13\times(\text{base area})\times h=\tfrac13(6^2)(5)=\tfrac13(180)=60.$$",
  {"B": r"used the prism formula and dropped the factor $\tfrac13$",
   "C": r"halved instead of taking a third",
   "D": r"used the side $6$ instead of the base area $36$"})

R("triangle-medians", 3,
  r"In triangle $ABC$, $AB=5$, $AC=7$ and $BC=8$. Find the length of the "
  r"median from $A$.",
  {"A": r"$\sqrt{21}$", "B": r"$\sqrt{53}$",
   "C": r"$4$", "D": r"$\dfrac{2\sqrt{21}}{3}$"},
  "A",
  ["Eq(Rational(2*49+2*25-64, 4), 21)",
   "Eq(Rational(2*49+2*25+64, 4), 53)",
   "Eq(Rational(2,3)*sqrt(21), 2*sqrt(21)/3)",
   "Eq(Rational(8,2), 4)"],
  r"With $a=BC=8$, $b=CA=7$, $c=AB=5$, the median to side $a$ satisfies "
  r"$$m_a^2=\frac{2b^2+2c^2-a^2}{4}=\frac{2(49)+2(25)-64}{4}"
  r"=\frac{98+50-64}{4}=\frac{84}{4}=21,$$ so $m_a=\sqrt{21}$.",
  {"B": r"added $a^2$ instead of subtracting it",
   "C": r"gave half of $BC$ — that is the distance to the midpoint along the side, not the median",
   "D": r"applied the centroid ratio $\tfrac23$, which gives the distance from $A$ to the centroid"})

R("grouped-frequency-mean", 1,
  r"Estimate the mean. Class $0\text{–}10$ has frequency $3$; class "
  r"$10\text{–}20$ has frequency $2$.",
  {"A": r"$9$", "B": r"$10$", "C": r"$14$", "D": r"$5$"},
  "A",
  ["Eq(Rational(3*5+2*15, 5), 9)",
   "Eq(Rational(5+15, 2), 10)",
   "Eq(Rational(3*10+2*20, 5), 14)"],
  r"Use the class midpoints, $5$ and $15$, each weighted by its frequency: "
  r"$$\bar x\approx\frac{3(5)+2(15)}{3+2}=\frac{15+30}{5}=\frac{45}{5}=9.$$",
  {"B": r"averaged the two midpoints and ignored the frequencies",
   "C": r"used the class upper bounds $10$ and $20$ instead of the midpoints",
   "D": r"used the first class only"})

# ---------------------------------------------------------------- 0.66%
R("algebraic-expressions", 1,
  r"Evaluate $3a-2b$ when $a=4$ and $b=-1$.",
  {"A": r"$14$", "B": r"$10$", "C": r"$-14$", "D": r"$12$"},
  "A",
  ["Eq((3*a-2*b).subs([(a,4),(b,-1)]), 14)",
   "Eq((3*a+2*b).subs([(a,4),(b,-1)]), 10)",
   "Eq((3*a).subs(a,4), 12)"],
  r"Substitute, and watch the double negative: "
  r"$$3(4)-2(-1)=12+2=14.$$",
  {"B": r"read $-2(-1)$ as $-2$, losing the double negative",
   "C": r"right size, wrong sign throughout",
   "D": r"dropped the $-2b$ term entirely"})

R("algebraic-expressions", 3,
  r"Simplify $\dfrac{x^2-9}{x^2+x-6}$, where $x\ne 2$ and $x\ne -3$.",
  {"A": r"$\dfrac{x-3}{x-2}$", "B": r"$\dfrac{x+3}{x+2}$",
   "C": r"$\dfrac{x-3}{x+2}$", "D": r"$\dfrac{x+3}{x-2}$"},
  "A",
  ["Eq(factor(x**2-9), (x-3)*(x+3))",
   "Eq(factor(x**2+x-6), (x-2)*(x+3))",
   "Eq(simplify((x**2-9)/(x**2+x-6) - (x-3)/(x-2)), 0)"],
  r"Factorise both parts: "
  r"$$\frac{x^2-9}{x^2+x-6}=\frac{(x-3)(x+3)}{(x+3)(x-2)}.$$ "
  r"The common factor $x+3$ cancels, leaving $\dfrac{x-3}{x-2}$.",
  {"B": r"factorised the denominator as $(x+3)(x+2)$ — the product of those is $x^2+5x+6$, not $x^2+x-6$",
   "C": r"cancelled $x+3$ from the top but $x-2$ from the bottom incorrectly, keeping $+2$",
   "D": r"cancelled the wrong factor, keeping $x+3$ instead of $x-3$"})

R("binomial-theorem", 1,
  r"In the expansion of $(x+2)^3$, find the coefficient of $x^2$.",
  {"A": r"$6$", "B": r"$3$", "C": r"$12$", "D": r"$2$"},
  "A",
  ["Eq(expand((x+2)**3).coeff(x, 2), 6)",
   "Eq(expand((x+2)**3).coeff(x, 1), 12)",
   "Eq(binomial(3,1), 3)"],
  r"The term in $x^2$ is $\binom{3}{1}x^2(2)^1=3\cdot 2\,x^2=6x^2$, so the "
  r"coefficient is $6$.",
  {"B": r"gave $\binom{3}{1}$ and forgot to multiply by the $2$",
   "C": r"gave the coefficient of $x$, which is $12$",
   "D": r"gave the $2$ from the bracket without the binomial coefficient"})

R("polynomial-arithmetic", 1,
  r"Simplify $(2x^2+3x-1)+(x^2-5x+4)$.",
  {"A": r"$3x^2-2x+3$", "B": r"$3x^2+8x+3$",
   "C": r"$3x^2-2x-5$", "D": r"$2x^2-2x+3$"},
  "A",
  ["Eq(expand((2*x**2+3*x-1)+(x**2-5*x+4)), 3*x**2-2*x+3)",
   "Eq(expand((2*x**2+3*x-1)-(x**2-5*x+4)), x**2+8*x-5)"],
  r"Collect like terms: $2x^2+x^2=3x^2$, $3x-5x=-2x$, $-1+4=3$. So the sum is "
  r"$3x^2-2x+3$.",
  {"B": r"subtracted the second bracket instead of adding, then mishandled the signs",
   "C": r"took $-1-4$ for the constant instead of $-1+4$",
   "D": r"forgot to add the $x^2$ terms together"})

R("quadratic-formula", 3,
  r"Solve $2x^2-4x-3=0$.",
  {"A": r"$x=\dfrac{2\pm\sqrt{10}}{2}$", "B": r"$x=\dfrac{2\pm\sqrt{10}}{4}$",
   "C": r"$x=\dfrac{-2\pm\sqrt{10}}{2}$", "D": r"$x=\dfrac{4\pm\sqrt{10}}{4}$"},
  "A",
  ["Eq((-4)**2 - 4*2*(-3), 40)",
   "Eq(simplify((2*x**2-4*x-3).subs(x, (2+sqrt(10))/2)), 0)",
   "Eq(simplify((2*x**2-4*x-3).subs(x, (2-sqrt(10))/2)), 0)",
   "Eq(simplify(sqrt(40) - 2*sqrt(10)), 0)"],
  r"Here $a=2$, $b=-4$, $c=-3$, so the discriminant is "
  r"$(-4)^2-4(2)(-3)=16+24=40$ and "
  r"$$x=\frac{4\pm\sqrt{40}}{4}=\frac{4\pm 2\sqrt{10}}{4}=\frac{2\pm\sqrt{10}}{2}.$$ "
  r"The last step matters: every term of the numerator must be halved, not "
  r"just one of them.",
  {"B": r"cancelled the $2$ from $4\pm 2\sqrt{10}$ but not from the denominator",
   "C": r"used $-b=-4$ instead of $-b=+4$",
   "D": r"cancelled the $2$ inside the surd only, leaving the $4$ untouched"})

R("complementary-events", 3,
  r"A bag holds $5$ red and $3$ blue counters. Two are drawn without "
  r"replacement. Find the probability that at least one is red.",
  {"A": r"$\dfrac{25}{28}$", "B": r"$\dfrac{3}{28}$",
   "C": r"$\dfrac{5}{8}$", "D": r"$\dfrac{15}{28}$"},
  "A",
  ["Eq(Rational(3,8)*Rational(2,7), Rational(3,28))",
   "Eq(1-Rational(3,28), Rational(25,28))",
   "Eq(binomial(3,2)/binomial(8,2), Rational(3,28))",
   "Eq(binomial(5,1)*binomial(3,1)/binomial(8,2), Rational(15,28))"],
  r"''At least one red'' is easier through its complement, ''both blue'': "
  r"$$P(\text{both blue})=\frac38\cdot\frac27=\frac{3}{28}.$$ Therefore "
  r"$$P(\text{at least one red})=1-\frac{3}{28}=\frac{25}{28}.$$",
  {"B": r"gave the complement itself — the probability that NO counter is red",
   "C": r"gave the chance the FIRST counter is red, ignoring the second draw",
   "D": r"counted exactly one red and left out the case of two reds"},
  check=lambda: (
      sum(1 for i in range(8) for j in range(i + 1, 8)
          if i < 5 or j < 5) == 25
      and sum(1 for i in range(8) for j in range(i + 1, 8)) == 28))

# ---------------------------------------------------------------- 0.60%
R("definite-integral-absolute", 1,
  r"Evaluate $\displaystyle\int_{-2}^{2}|x|\,dx$.",
  {"A": r"$4$", "B": r"$0$", "C": r"$2$", "D": r"$8$"},
  "A",
  ["Eq(integrate(x, (x, 0, 2)), 2)",
   "Eq(2*integrate(x, (x, 0, 2)), 4)",
   "Eq(integrate(x, (x, -2, 2)), 0)"],
  r"$|x|$ is symmetric about the $y$-axis, so split at $0$ and double one "
  r"half: "
  r"$$\int_{-2}^{2}|x|\,dx=2\int_0^2 x\,dx=2\left[\tfrac{x^2}{2}\right]_0^2=2(2)=4.$$ "
  r"Geometrically this is two triangles of area $2$ each.",
  {"B": r"integrated $x$ rather than $|x|$; $x$ is odd so it cancels, but $|x|$ never goes below the axis",
   "C": r"found only the right-hand half",
   "D": r"doubled the answer once too often"})

R("derivative-exp-log", 1,
  r"Differentiate $y=e^{2x}$.",
  {"A": r"$2e^{2x}$", "B": r"$e^{2x}$", "C": r"$2e^{x}$", "D": r"$\dfrac{e^{2x}}{2}$"},
  "A",
  ["Eq(diff(exp(2*x), x), 2*exp(2*x))",
   "Eq(diff(exp(x), x), exp(x))",
   "Eq(integrate(exp(2*x), x), exp(2*x)/2)"],
  r"By the chain rule, $\frac{d}{dx}e^{u}=e^{u}\frac{du}{dx}$ with $u=2x$, so "
  r"$$\frac{dy}{dx}=e^{2x}\cdot 2=2e^{2x}.$$",
  {"B": r"forgot the chain-rule factor from the inner function $2x$",
   "C": r"differentiated the exponent as well as bringing it down",
   "D": r"integrated instead of differentiating"})

R("derivative-exp-log", 3,
  r"Differentiate $y=x^2\ln x$ for $x>0$.",
  {"A": r"$2x\ln x+x$", "B": r"$2x\ln x$",
   "C": r"$2x\ln x+x^2$", "D": r"$2x+\dfrac{1}{x}$"},
  "A",
  ["Eq(simplify(diff(x**2*log(x), x) - (2*x*log(x) + x)), 0)",
   "Eq(diff(log(x), x), 1/x)",
   "Eq(diff(x**2, x), 2*x)"],
  r"Product rule with $u=x^2$ and $v=\ln x$: "
  r"$$\frac{dy}{dx}=2x\ln x+x^2\cdot\frac1x=2x\ln x+x.$$",
  {"B": r"differentiated only the first factor",
   "C": r"used $\frac{d}{dx}\ln x=1$ instead of $\tfrac1x$",
   "D": r"differentiated the two factors separately and added, instead of using the product rule"})

R("derivative-trig", 3,
  r"Differentiate $y=\tan(x^2)$.",
  {"A": r"$2x\sec^2(x^2)$", "B": r"$\sec^2(x^2)$",
   "C": r"$2x\tan(x^2)$", "D": r"$2x\sec^2(2x)$"},
  "A",
  ["Eq(simplify(diff(tan(x**2), x) - 2*x/cos(x**2)**2), 0)",
   "Eq(simplify(diff(tan(x), x) - 1/cos(x)**2), 0)",
   "Eq(diff(x**2, x), 2*x)"],
  r"Chain rule with $u=x^2$: $\frac{d}{dx}\tan u=\sec^2 u\cdot\frac{du}{dx}$, so "
  r"$$\frac{dy}{dx}=\sec^2(x^2)\cdot 2x=2x\sec^2(x^2).$$",
  {"B": r"forgot the inner derivative $2x$",
   "C": r"kept $\tan$ instead of differentiating it to $\sec^2$",
   "D": r"differentiated the inner function inside the $\sec^2$ as well as outside"})

R("higher-order-derivatives", 1,
  r"For $f(x)=x^4$, find $f''(x)$.",
  {"A": r"$12x^2$", "B": r"$4x^3$", "C": r"$24x$", "D": r"$12x^3$"},
  "A",
  ["Eq(diff(x**4, x, 2), 12*x**2)",
   "Eq(diff(x**4, x, 1), 4*x**3)",
   "Eq(diff(x**4, x, 3), 24*x)"],
  r"Differentiate twice: $f'(x)=4x^3$, then $f''(x)=12x^2$.",
  {"B": r"stopped after one differentiation",
   "C": r"differentiated three times",
   "D": r"reduced the coefficient but not the power"})

R("higher-order-derivatives", 3,
  r"For $f(x)=\dfrac{x}{x+1}$, find $f''(1)$.",
  {"A": r"$-\dfrac14$", "B": r"$\dfrac14$", "C": r"$-\dfrac12$", "D": r"$-2$"},
  "A",
  ["Eq(simplify(diff(x/(x+1), x) - 1/(x+1)**2), 0)",
   "Eq(simplify(diff(x/(x+1), x, 2) + 2/(x+1)**3), 0)",
   "Eq(diff(x/(x+1), x, 2).subs(x, 1), Rational(-1,4))",
   "Eq(diff(x/(x+1), x).subs(x, 1), Rational(1,4))"],
  r"Quotient rule gives "
  r"$$f'(x)=\frac{(x+1)-x}{(x+1)^2}=\frac{1}{(x+1)^2}=(x+1)^{-2},$$ so "
  r"$$f''(x)=-2(x+1)^{-3}=\frac{-2}{(x+1)^3}.$$ At $x=1$: "
  r"$f''(1)=\frac{-2}{8}=-\tfrac14$.",
  {"B": r"gave $f'(1)$ instead of $f''(1)$",
   "C": r"used $(x+1)^2=4$ in the denominator rather than $(x+1)^3=8$",
   "D": r"stopped at the numerator $-2$ and never substituted"})

R("integration-by-substitution", 1,
  r"Find $\displaystyle\int 2x\,(x^2+5)^3\,dx$.",
  {"A": r"$\dfrac{(x^2+5)^4}{4}+C$", "B": r"$(x^2+5)^4+C$",
   "C": r"$\dfrac{(x^2+5)^4}{8}+C$", "D": r"$\dfrac{2x(x^2+5)^4}{4}+C$"},
  "A",
  ["Eq(simplify(diff((x**2+5)**4/4, x) - 2*x*(x**2+5)**3), 0)",
   "Eq(simplify(diff((x**2+5)**4, x) - 8*x*(x**2+5)**3), 0)"],
  r"Let $u=x^2+5$, so $du=2x\,dx$ — the $2x$ in front is exactly what the "
  r"substitution needs. Then "
  r"$$\int u^3\,du=\frac{u^4}{4}+C=\frac{(x^2+5)^4}{4}+C.$$ "
  r"Check by differentiating: $\frac{d}{dx}\frac{(x^2+5)^4}{4}=2x(x^2+5)^3$.",
  {"B": r"raised the power but never divided by the new power",
   "C": r"divided by $8$, double-counting the $2$ that $du$ had already absorbed",
   "D": r"kept the $2x$ after substituting, so it is counted twice"})

R("normal-line", 1,
  r"Find the gradient of the normal to $y=x^2$ at the point where $x=1$.",
  {"A": r"$-\dfrac12$", "B": r"$2$", "C": r"$\dfrac12$", "D": r"$-2$"},
  "A",
  ["Eq(diff(x**2, x).subs(x, 1), 2)",
   "Eq(Rational(-1,1)/diff(x**2, x).subs(x, 1), Rational(-1,2))",
   "Eq(2*Rational(-1,2), -1)"],
  r"The tangent gradient is $\frac{dy}{dx}=2x=2$ at $x=1$. The normal is "
  r"perpendicular to it, so its gradient is the negative reciprocal: "
  r"$$m_{\text{normal}}=-\frac{1}{2}.$$",
  {"B": r"gave the tangent gradient, not the normal",
   "C": r"took the reciprocal but forgot the negative",
   "D": r"negated the tangent gradient instead of taking the negative reciprocal"})

R("normal-line", 3,
  r"Find the equation of the normal to $y=x^3-2x$ at the point where $x=1$.",
  {"A": r"$y=-x$", "B": r"$y=x-2$",
   "C": r"$y=-\dfrac{x}{3}-\dfrac23$", "D": r"$y=x$"},
  "A",
  ["Eq((x**3-2*x).subs(x, 1), -1)",
   "Eq(diff(x**3-2*x, x).subs(x, 1), 1)",
   "Eq((-x).subs(x, 1), -1)",
   "Eq((x-2).subs(x, 1), -1)"],
  r"At $x=1$ the point is $(1,-1)$. The derivative is $y'=3x^2-2$, so the "
  r"tangent gradient is $3-2=1$ and the normal gradient is $-1$. Then "
  r"$$y-(-1)=-1(x-1)\ \Longrightarrow\ y+1=-x+1\ \Longrightarrow\ y=-x.$$",
  {"B": r"used the tangent gradient $1$ instead of the normal gradient $-1$",
   "C": r"used $-\tfrac{1}{3x^2}$, forgetting the $-2$ in $y'$",
   "D": r"got the gradient sign right but lost the point, drawing the line through the origin with gradient $1$"})

R("rational-function-asymptotes", 1,
  r"Find the vertical asymptote of $y=\dfrac{1}{x-4}$.",
  {"A": r"$x=4$", "B": r"$x=-4$", "C": r"$y=4$", "D": r"$x=0$"},
  "A",
  ["Eq(limit(1/(x-4), x, 4, '+'), oo)",
   "Eq(limit(1/(x-4), x, oo), 0)",
   "Eq((x-4).subs(x, 4), 0)"],
  r"A vertical asymptote sits where the denominator is zero and the numerator "
  r"is not: $x-4=0$, so $x=4$.",
  {"B": r"solved $x+4=0$ — sign slip",
   "C": r"named a horizontal line; the asymptote here is vertical",
   "D": r"gave the $y$-axis, which is where $x$ itself is zero"})

R("rational-function-asymptotes", 3,
  r"Find the horizontal asymptote of $y=\dfrac{2x^2-x}{3x^2+5}$.",
  {"A": r"$y=\dfrac23$", "B": r"$y=0$", "C": r"$y=2$",
   "D": r"there is no horizontal asymptote"},
  "A",
  ["Eq(limit((2*x**2-x)/(3*x**2+5), x, oo), Rational(2,3))",
   "Eq(limit((2*x**2-x)/(3*x**2+5), x, -oo), Rational(2,3))",
   "Eq(limit((2*x-1)/(3*x**2+5), x, oo), 0)"],
  r"Numerator and denominator have the same degree, so divide through by "
  r"$x^2$: "
  r"$$\frac{2-\tfrac1x}{3+\tfrac{5}{x^2}}\longrightarrow\frac{2}{3}"
  r"\quad\text{as }x\to\pm\infty.$$ The horizontal asymptote is $y=\tfrac23$.",
  {"B": r"that is the rule when the denominator has the HIGHER degree; here the degrees match",
   "C": r"used the numerator's leading coefficient alone",
   "D": r"that is the case when the NUMERATOR has the higher degree"})

# ---------------------------------------------------------------- 0.52%
R("coordinate-distance", 3,
  r"The point $(a,3)$ is $5$ units from $(1,-1)$. Find the possible values "
  r"of $a$.",
  {"A": r"$a=4$ or $a=-2$", "B": r"$a=4$ only",
   "C": r"$a=2$ or $a=-4$", "D": r"$a=6$ or $a=-4$"},
  "A",
  ["Eq((4-1)**2 + (3-(-1))**2, 25)",
   "Eq((-2-1)**2 + (3-(-1))**2, 25)",
   "Eq(sqrt(25), 5)"],
  r"Square the distance formula: "
  r"$$(a-1)^2+(3-(-1))^2=5^2\ \Longrightarrow\ (a-1)^2+16=25,$$ so "
  r"$(a-1)^2=9$ and $a-1=\pm 3$. Hence $a=4$ or $a=-2$.",
  {"B": r"took only the positive square root; $(a-1)^2=9$ has two solutions",
   "C": r"solved $a=\pm3-1$ instead of $a=1\pm3$",
   "D": r"used $(3-(-1))^2=9$, mis-subtracting the negative $y$-coordinate"})

R("cylinder", 1,
  r"A cylinder has radius $2$ and height $5$. Find its volume.",
  {"A": r"$20\pi$", "B": r"$80\pi$", "C": r"$10\pi$", "D": r"$40\pi$"},
  "A",
  ["Eq(pi*2**2*5, 20*pi)",
   "Eq(pi*4**2*5, 80*pi)",
   "Eq(pi*2*5, 10*pi)",
   "Eq(2*pi*2**2*5, 40*pi)"],
  r"$$V=\pi r^2h=\pi(2)^2(5)=20\pi.$$",
  {"B": r"used the diameter $4$ as the radius",
   "C": r"forgot to square the radius",
   "D": r"used $2\pi r^2h$, borrowing the $2$ from the surface-area formula"})

R("cylinder", 3,
  r"A cylinder has volume $54\pi$ and height $6$. Find its total surface area.",
  {"A": r"$54\pi$", "B": r"$36\pi$", "C": r"$45\pi$", "D": r"$90\pi$"},
  "A",
  ["Eq(pi*3**2*6, 54*pi)",
   "Eq(2*pi*3**2 + 2*pi*3*6, 54*pi)",
   "Eq(2*pi*3*6, 36*pi)",
   "Eq(pi*3**2 + 2*pi*3*6, 45*pi)",
   "Eq(2*pi*3**2 + 2*pi*6*6, 90*pi)"],
  r"First recover the radius from the volume: $\pi r^2(6)=54\pi$ gives "
  r"$r^2=9$, so $r=3$. Then "
  r"$$A=2\pi r^2+2\pi rh=2\pi(9)+2\pi(3)(6)=18\pi+36\pi=54\pi.$$ "
  r"That the answer equals the volume numerically is a coincidence of these "
  r"numbers, not a rule.",
  {"B": r"gave the curved surface only, leaving out both circular ends",
   "C": r"counted only one circular end",
   "D": r"used the height $6$ as the radius in the curved-surface term"})
