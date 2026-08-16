"""Gap items, batch B — ranks 21-40 by exam weight (0.66% down to 0.50%).

These twenty carry a further 11.14 points, taking the closed share of the gap
past 70%.
"""

from item_bank import I

# ============ 21. systems-two-linear — 0.66% ===============================
I("systems-two-linear", 2,
  r"Solve $\begin{cases} 3x + 2y = 16 \\ x = 2y \end{cases}$",
  {"A": r"$(4,\ 2)$", "B": r"$(2,\ 4)$", "C": r"$(4,\ 4)$", "D": r"$(8,\ 4)$"}, "A",
  ["Eq(3*4 + 2*2, 16)", "Eq(4, 2*2)"],
  r"Substituting $x=2y$: $6y + 2y = 16$, so $y = 2$ and $x = 4$.",
  {"B": "wrote the pair in the wrong order",
   "C": "solved for $y$ then reused it as $x$",
   "D": "doubled $x$ a second time after substituting"})
I("systems-two-linear", 3,
  r"Solve $\begin{cases} 4x - 3y = 5 \\ 2x + y = 5 \end{cases}$",
  {"A": r"$(2,\ 1)$", "B": r"$(1,\ 2)$", "C": r"$(2,\ -1)$", "D": r"$(3,\ -1)$"}, "A",
  ["Eq(4*2 - 3*1, 5)", "Eq(2*2 + 1, 5)"],
  r"From the second equation $y = 5 - 2x$; substituting gives $10x = 20$, so "
  r"$x = 2$ and $y = 1$.",
  {"B": "wrote the pair in the wrong order",
   "C": "sign slip substituting back for $y$",
   "D": "solved $10x = 30$"})
I("systems-two-linear", 4,
  r"For which value of $k$ does $\begin{cases} kx + 2y = 6 \\ 3x + y = 4 \end{cases}$ "
  r"have NO solution?",
  {"A": r"$k = 6$", "B": r"$k = \dfrac{3}{2}$", "C": r"$k = 3$", "D": r"$k = 12$"}, "A",
  ["Eq(6*1 - 2*3, 0)", "Ne(6*4 - 6*3, 0)", "Ne(3*1 - 2*3, 0)"],
  r"No solution means the lines are parallel but not identical: "
  r"$\dfrac{k}{3} = \dfrac{2}{1}$ gives $k=6$, and the constants then disagree.",
  {"B": "inverted the ratio of the coefficients",
   "C": "matched $k$ to the coefficient of $x$ in the other equation",
   "D": "matched the constant terms instead of the coefficients"})

# ============ 22. vieta-formulas — 0.66% ===================================
I("vieta-formulas", 2,
  r"The equation $x^{2} - 7x + 12 = 0$ has roots $x_{1}$, $x_{2}$. Find $x_{1}x_{2}$.",
  {"A": r"$12$", "B": r"$7$", "C": r"$-12$", "D": r"$-7$"}, "A",
  ["Eq(Rational(12,1), 12)", "Eq(3*4, 12)", "Eq(3+4, 7)"],
  r"The product of the roots is $\dfrac{c}{a} = 12$.",
  {"B": "gave the sum instead of the product",
   "C": "used $-\\dfrac{c}{a}$", "D": "used $-\\dfrac{b}{a}$ with the wrong sign"})
I("vieta-formulas", 3,
  r"The equation $3x^{2} + 5x - 2 = 0$ has roots $x_{1}$, $x_{2}$. Find $x_{1}+x_{2}$.",
  {"A": r"$-\dfrac{5}{3}$", "B": r"$\dfrac{5}{3}$", "C": r"$-\dfrac{2}{3}$",
   "D": r"$\dfrac{2}{3}$"}, "A",
  ["Eq(Rational(-5,3), -Rational(5,3))",
   "Eq(Rational(1,3) + (-2), Rational(-5,3))",
   "Eq(3*Rational(1,3)**2 + 5*Rational(1,3) - 2, 0)",
   "Eq(3*(-2)**2 + 5*(-2) - 2, 0)"],
  r"Sum of roots $= -\dfrac{b}{a} = -\dfrac{5}{3}$ (the roots are $\tfrac13$ and $-2$).",
  {"B": "dropped the minus sign in $-\\tfrac{b}{a}$",
   "C": "gave the product $\\tfrac{c}{a}$", "D": "gave the product with the wrong sign"})
I("vieta-formulas", 4,
  r"The roots of $x^{2} - 6x + k = 0$ satisfy $x_{1}^{2} + x_{2}^{2} = 20$. Find $k$.",
  {"A": r"$8$", "B": r"$16$", "C": r"$-8$", "D": r"$28$"}, "A",
  ["Eq(6**2 - 2*8, 20)",
   "Eq(solve(Eq(36 - 2*symbols('k'), 20), symbols('k'))[0], 8)"],
  r"$x_{1}^{2}+x_{2}^{2} = (x_{1}+x_{2})^{2} - 2x_{1}x_{2} = 36 - 2k = 20$, so $k = 8$.",
  {"B": "solved $36 - k = 20$", "C": "sign error rearranging",
   "D": "added $2k$ instead of subtracting"})

# ============ 23. binomial-distribution — 0.64% ============================
I("binomial-distribution", 2,
  r"A fair coin is tossed $4$ times. Find the probability of exactly $2$ heads.",
  {"A": r"$\dfrac{3}{8}$", "B": r"$\dfrac{1}{4}$", "C": r"$\dfrac{1}{2}$",
   "D": r"$\dfrac{3}{16}$"}, "A",
  ["Eq(binomial(4,2)*Rational(1,2)**4, Rational(3,8))", "Eq(binomial(4,2), 6)"],
  r"$\binom{4}{2}\left(\tfrac12\right)^{4} = \dfrac{6}{16} = \dfrac38$.",
  {"B": "used $\\tfrac{2}{4}$ of the tosses as the probability",
   "C": "assumed exactly half is as likely as not",
   "D": "forgot the factor $\\binom{4}{2}$ and used $3$"})
I("binomial-distribution", 3,
  r"A biased die shows a six with probability $\tfrac13$. It is rolled $5$ times. "
  r"Find the probability of exactly two sixes.",
  {"A": r"$\dfrac{80}{243}$", "B": r"$\dfrac{40}{243}$", "C": r"$\dfrac{10}{243}$",
   "D": r"$\dfrac{80}{81}$"}, "A",
  ["Eq(binomial(5,2)*Rational(1,3)**2*Rational(2,3)**3, Rational(80,243))",
   "Eq(binomial(5,2), 10)"],
  r"$\binom{5}{2}\left(\tfrac13\right)^{2}\left(\tfrac23\right)^{3} "
  r"= 10 \cdot \tfrac19 \cdot \tfrac{8}{27} = \dfrac{80}{243}$.",
  {"B": "used $\\binom{5}{1}$ instead of $\\binom{5}{2}$, halving the count",
   "C": "omitted the $\\left(\\tfrac23\\right)^{3}$ factor",
   "D": "used the wrong power of the denominator"})
I("binomial-distribution", 4,
  r"A fair die is rolled $4$ times. Find the probability of at least one six.",
  {"A": r"$\dfrac{671}{1296}$", "B": r"$\dfrac{625}{1296}$", "C": r"$\dfrac{2}{3}$",
   "D": r"$\dfrac{1}{1296}$"}, "A",
  ["Eq(1 - Rational(5,6)**4, Rational(671,1296))", "Eq(Rational(5,6)**4, Rational(625,1296))"],
  r"$1 - \left(\tfrac56\right)^{4} = 1 - \dfrac{625}{1296} = \dfrac{671}{1296}$.",
  {"B": "gave the probability of NO six", "C": "added $\\tfrac16$ four times",
   "D": "gave the probability of four sixes"})

# ============ 24. conditional-probability — 0.64% ==========================
I("conditional-probability", 2,
  r"$P(A \cap B) = 0.12$ and $P(B) = 0.4$. Find $P(A \mid B)$.",
  {"A": r"$0.3$", "B": r"$0.048$", "C": r"$0.28$", "D": r"$0.52$"}, "A",
  ["Eq(Rational(12,100)/Rational(4,10), Rational(3,10))"],
  r"$P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{0.12}{0.4} = 0.3$.",
  {"B": "multiplied instead of dividing", "C": "subtracted instead of dividing",
   "D": "added instead of dividing"})
I("conditional-probability", 3,
  r"Two cards are drawn without replacement from a standard pack of $52$. "
  r"Find the probability that both are aces.",
  {"A": r"$\dfrac{1}{221}$", "B": r"$\dfrac{1}{169}$", "C": r"$\dfrac{3}{676}$",
   "D": r"$\dfrac{1}{26}$"}, "A",
  ["Eq(Rational(4,52)*Rational(3,51), Rational(1,221))",
   "Eq(Rational(4,52)*Rational(4,52), Rational(1,169))"],
  r"$\dfrac{4}{52} \times \dfrac{3}{51} = \dfrac{1}{221}$ — the second draw sees "
  r"one fewer ace and one fewer card.",
  {"B": "treated the draws as WITH replacement",
   "C": "reduced the aces but not the pack size",
   "D": "gave the probability of one ace"})
I("conditional-probability", 4,
  r"A bag holds $3$ red and $2$ blue balls. Two are drawn without replacement. "
  r"Given that the first is red, find the probability that the second is red.",
  {"A": r"$\dfrac{1}{2}$", "B": r"$\dfrac{3}{5}$", "C": r"$\dfrac{2}{5}$",
   "D": r"$\dfrac{3}{10}$"}, "A",
  ["Eq(Rational(2,4), Rational(1,2))", "Eq(Rational(3,5)*Rational(2,4), Rational(3,10))"],
  r"After a red is removed, $2$ of the remaining $4$ balls are red, so the "
  r"probability is $\tfrac24 = \tfrac12$.",
  {"B": "ignored the conditioning and used the original proportion",
   "C": "used the blue proportion", "D": "gave $P(\\text{both red})$, not the conditional"})

# ============ 25. antiderivative-trig-exp — 0.60% ==========================
I("antiderivative-trig-exp", 2,
  r"Find $\displaystyle\int \cos x\,dx$.",
  {"A": r"$\sin x + C$", "B": r"$-\sin x + C$", "C": r"$-\cos x + C$",
   "D": r"$\tan x + C$"}, "A",
  ["Eq(integrate(cos(x), x), sin(x))"],
  r"$\dfrac{d}{dx}(\sin x) = \cos x$, so the antiderivative is $\sin x + C$.",
  {"B": "used the derivative rule for cosine instead",
   "C": "integrated $\\sin x$ by mistake", "D": "confused with $\\sec^{2}x$"})
I("antiderivative-trig-exp", 3,
  r"Find $\displaystyle\int \left(2e^{x} - 3\sin x\right)dx$.",
  {"A": r"$2e^{x} + 3\cos x + C$", "B": r"$2e^{x} - 3\cos x + C$",
   "C": r"$e^{x} + 3\cos x + C$", "D": r"$2e^{x} - 3\sin x + C$"}, "A",
  ["Eq(simplify(integrate(2*exp(x) - 3*sin(x), x) - (2*exp(x) + 3*cos(x))), 0)"],
  r"$\int \sin x\,dx = -\cos x$, so $-3\int\sin x\,dx = +3\cos x$.",
  {"B": "missed the sign change when integrating $\\sin x$",
   "C": "divided the exponential term by $2$",
   "D": "did not integrate the sine at all"})
I("antiderivative-trig-exp", 4,
  r"Evaluate $\displaystyle\int_{0}^{\pi/2} \sin x\,dx$.",
  {"A": r"$1$", "B": r"$0$", "C": r"$-1$", "D": r"$\dfrac{\pi}{2}$"}, "A",
  ["Eq(integrate(sin(x), (x, 0, pi/2)), 1)"],
  r"$\left[-\cos x\right]_{0}^{\pi/2} = -0 - (-1) = 1$.",
  {"B": "evaluated $\\left[\\cos x\\right]$ and got the difference wrong",
   "C": "kept the minus sign from $-\\cos x$",
   "D": "integrated as if the integrand were $1$"})

# ============ 26. limit-concept — 0.60% ====================================
I("limit-concept", 2,
  r"Evaluate $\displaystyle\lim_{x \to 2} \frac{x^{2}-4}{x-2}$.",
  {"A": r"$4$", "B": r"$0$", "C": r"$2$", "D": r"the limit does not exist"}, "A",
  ["Eq(limit((x**2 - 4)/(x - 2), x, 2), 4)"],
  r"$\dfrac{(x-2)(x+2)}{x-2} = x+2 \to 4$.",
  {"B": "substituted and read $\\tfrac00$ as $0$",
   "C": "cancelled to $x$ instead of $x+2$",
   "D": "stopped at $\\tfrac00$ without factorising"})
I("limit-concept", 3,
  r"Evaluate $\displaystyle\lim_{x \to 3} \frac{x^{2}-9}{x^{2}-2x-3}$.",
  {"A": r"$\dfrac{3}{2}$", "B": r"$1$", "C": r"$3$", "D": r"$0$"}, "A",
  ["Eq(limit((x**2 - 9)/(x**2 - 2*x - 3), x, 3), Rational(3,2))",
   "Eq(simplify((x-3)*(x+1) - (x**2 - 2*x - 3)), 0)"],
  r"$\dfrac{(x-3)(x+3)}{(x-3)(x+1)} = \dfrac{x+3}{x+1} \to \dfrac{6}{4} = \dfrac32$.",
  {"B": "cancelled the whole numerator against the denominator",
   "C": "substituted only into the numerator's factor",
   "D": "read $\\tfrac00$ as $0$"})
I("limit-concept", 4,
  r"Evaluate $\displaystyle\lim_{x \to \infty} \frac{3x^{2}+2x}{5x^{2}-1}$.",
  {"A": r"$\dfrac{3}{5}$", "B": r"$0$", "C": r"$\infty$", "D": r"$3$"}, "A",
  ["Eq(limit((3*x**2 + 2*x)/(5*x**2 - 1), x, oo), Rational(3,5))"],
  r"Divide top and bottom by $x^{2}$: $\dfrac{3 + 2/x}{5 - 1/x^{2}} \to \dfrac35$.",
  {"B": "assumed the denominator grows faster",
   "C": "assumed the numerator grows faster",
   "D": "kept the leading coefficient of the numerator only"})

# ============ 27. optimisation — 0.60% =====================================
I("optimisation", 2,
  r"A rectangle has perimeter $20$. Find its greatest possible area.",
  {"A": r"$25$", "B": r"$24$", "C": r"$100$", "D": r"$20$"}, "A",
  ["Eq(diff(x*(10 - x), x).subs(x, 5), 0)", "Eq((x*(10-x)).subs(x, 5), 25)"],
  r"With $x + y = 10$ the area is $x(10-x)$, greatest at $x = 5$, giving $25$.",
  {"B": "used a $4 \\times 6$ rectangle without checking it is the maximum",
   "C": "squared the perimeter", "D": "confused area with perimeter"})
I("optimisation", 3,
  r"Two positive numbers add to $12$. Find their greatest possible product.",
  {"A": r"$36$", "B": r"$32$", "C": r"$12$", "D": r"$35$"}, "A",
  ["Eq(diff(x*(12 - x), x).subs(x, 6), 0)", "Eq((x*(12-x)).subs(x, 6), 36)"],
  r"$P = x(12-x)$, and $P' = 12 - 2x = 0$ at $x = 6$, giving $6 \times 6 = 36$.",
  {"B": "used $4$ and $8$", "C": "gave the sum", "D": "used $5$ and $7$"})
I("optimisation", 4,
  r"Equal squares of side $x$ are cut from the corners of a $12 \times 12$ sheet "
  r"and the sides folded up. Find the greatest volume of the open box.",
  {"A": r"$128$", "B": r"$144$", "C": r"$108$", "D": r"$64$"}, "A",
  ["Eq(diff(x*(12 - 2*x)**2, x).subs(x, 2), 0)",
   "Eq((x*(12 - 2*x)**2).subs(x, 2), 128)",
   "Eq((x*(12 - 2*x)**2).subs(x, 1), 100)"],
  r"$V = x(12-2x)^{2}$ and $V' = (12-2x)(12-6x) = 0$ gives $x = 2$ (as $x=6$ "
  r"collapses the box), so $V = 2 \times 8^{2} = 128$.",
  {"B": "used $x = 3$", "C": "used $x = 1$ and mis-multiplied",
   "D": "forgot to square the base edge"})

# ============ 28. exponential-and-log-graphs — 0.59% =======================
I("exponential-and-log-graphs", 2,
  r"Through which point does the graph of $y = 2^{x}$ pass?",
  {"A": r"$(0,\ 1)$", "B": r"$(1,\ 0)$", "C": r"$(0,\ 0)$", "D": r"$(0,\ 2)$"}, "A",
  ["Eq(2**0, 1)"],
  r"$2^{0} = 1$, so the curve passes through $(0,1)$.",
  {"B": "swapped the coordinates", "C": "assumed it passes through the origin",
   "D": "used the base as the $y$-intercept"})
I("exponential-and-log-graphs", 3,
  r"State the horizontal asymptote of $y = 3^{x-1} + 2$.",
  {"A": r"$y = 2$", "B": r"$y = 0$", "C": r"$y = 3$", "D": r"$x = 1$"}, "A",
  ["Eq(limit(3**(x-1) + 2, x, -oo), 2)"],
  r"As $x \to -\infty$, $3^{x-1} \to 0$, so $y \to 2$.",
  {"B": "gave the asymptote before the vertical shift",
   "C": "used the base as the asymptote",
   "D": "gave the horizontal shift as a vertical asymptote"})
I("exponential-and-log-graphs", 4,
  r"State the domain of $y = \log_{2}(x-3)$ and its vertical asymptote.",
  {"A": r"$x > 3$, asymptote $x = 3$", "B": r"$x > 0$, asymptote $x = 0$",
   "C": r"$x > -3$, asymptote $x = -3$", "D": r"$x \ge 3$, asymptote $x = 3$"}, "A",
  ["(4 - 3) > 0", "Eq(solve(Eq(x - 3, 0), x)[0], 3)"],
  r"The argument must be positive: $x - 3 > 0$, so $x > 3$, and the curve runs "
  r"down the line $x = 3$.",
  {"B": "ignored the horizontal shift",
   "C": "shifted the wrong way", "D": "included $x=3$, where the logarithm is undefined"})

# ============ 29. inverse-functions — 0.59% ================================
I("inverse-functions", 2,
  r"$f(x) = 3x - 6$. Find $f^{-1}(x)$.",
  {"A": r"$\dfrac{x+6}{3}$", "B": r"$\dfrac{x-6}{3}$", "C": r"$3x + 6$",
   "D": r"$\dfrac{1}{3x-6}$"}, "A",
  ["Eq(simplify(((x + 6)/3)*3 - 6 - x), 0)"],
  r"Swap and solve: $x = 3y - 6$ gives $y = \dfrac{x+6}{3}$.",
  {"B": "subtracted instead of adding when undoing $-6$",
   "C": "undid the operations without swapping",
   "D": "took the reciprocal instead of the inverse function"})
I("inverse-functions", 3,
  r"$f(x) = \dfrac{x+2}{x-1}$. Find $f^{-1}(3)$.",
  {"A": r"$\dfrac{5}{2}$", "B": r"$\dfrac{5}{4}$", "C": r"$5$", "D": r"$\dfrac{3}{2}$"},
  "A",
  ["Eq((Rational(5,2) + 2)/(Rational(5,2) - 1), 3)",
   "Eq(solve(Eq((x + 2)/(x - 1), 3), x)[0], Rational(5,2))"],
  r"$f^{-1}(3)$ is the $x$ with $f(x)=3$: $x+2 = 3x-3$, so $x = \tfrac52$.",
  {"B": "solved $x + 2 = 3(x+1)$", "C": "solved $x+2=3x-3$ but dropped the $2$",
   "D": "evaluated $f(3)$ instead"})
I("inverse-functions", 4,
  r"$f(x) = x^{2}+1$ for $x \ge 0$. Find $f^{-1}(x)$.",
  {"A": r"$\sqrt{x-1}$", "B": r"$\sqrt{x}-1$", "C": r"$\sqrt{x+1}$",
   "D": r"$(x-1)^{2}$"}, "A",
  ["Eq(simplify((sqrt(x-1))**2 + 1 - x), 0)", "Eq(sqrt(5-1), 2)", "Eq(2**2 + 1, 5)"],
  r"$x = y^{2}+1$ gives $y = \sqrt{x-1}$, taking the positive root because "
  r"$x \ge 0$ was imposed.",
  {"B": "subtracted outside the root instead of inside",
   "C": "added instead of subtracting", "D": "squared instead of taking the root"})

# ============ 30. angles-and-parallel-lines — 0.52% ========================
I("angles-and-parallel-lines", 2,
  r"Angles $3x$ and $2x + 30^{\circ}$ lie on a straight line. Find $x$.",
  {"A": r"$30^{\circ}$", "B": r"$36^{\circ}$", "C": r"$25^{\circ}$", "D": r"$15^{\circ}$"},
  "A",
  ["Eq(solve(Eq(3*x + 2*x + 30, 180), x)[0], 30)", "Eq(3*30 + (2*30 + 30), 180)"],
  r"$3x + 2x + 30 = 180$, so $5x = 150$ and $x = 30^{\circ}$.",
  {"B": "used $5x = 180$", "C": "used $5x + 30 = 155$",
   "D": "used $90^{\\circ}$ instead of $180^{\\circ}$"})
I("angles-and-parallel-lines", 3,
  r"Two parallel lines are cut by a transversal. One angle is $(2x+10)^{\circ}$ and "
  r"its corresponding angle is $(3x-20)^{\circ}$. Find $x$.",
  {"A": r"$30$", "B": r"$6$", "C": r"$38$", "D": r"$2$"}, "A",
  ["Eq(solve(Eq(2*x + 10, 3*x - 20), x)[0], 30)", "Eq(2*30 + 10, 3*30 - 20)"],
  r"Corresponding angles are equal: $2x+10 = 3x-20$, so $x = 30$.",
  {"B": "set the two expressions to sum to $180$ and slipped",
   "C": "solved $2x + 10 + 3x - 20 = 180$", "D": "subtracted the constants only"})
I("angles-and-parallel-lines", 4,
  r"Four angles $x$, $2x$, $3x$ and $4x$ meet at a point and fill it completely. "
  r"Find $x$.",
  {"A": r"$36^{\circ}$", "B": r"$18^{\circ}$", "C": r"$45^{\circ}$", "D": r"$60^{\circ}$"},
  "A",
  ["Eq(solve(Eq(x + 2*x + 3*x + 4*x, 360), x)[0], 36)", "Eq(36 + 72 + 108 + 144, 360)"],
  r"$10x = 360^{\circ}$, so $x = 36^{\circ}$.",
  {"B": "used $180^{\\circ}$ instead of $360^{\\circ}$",
   "C": "divided $360^{\\circ}$ by the number of angles",
   "D": "used $600^{\\circ}$ as the total"})

# ============ 31. chords-and-power-of-a-point — 0.52% ======================
I("chords-and-power-of-a-point", 2,
  r"Two chords of a circle cross inside it. One is cut into lengths $3$ and $8$, "
  r"the other into $4$ and $x$. Find $x$.",
  {"A": r"$6$", "B": r"$24$", "C": r"$7$", "D": r"$12$"}, "A",
  ["Eq(3*8, 4*6)"],
  r"The products of the two parts are equal: $3 \times 8 = 4x$, so $x = 6$.",
  {"B": "gave the product $3 \\times 8$ itself",
   "C": "added rather than using the product rule",
   "D": "divided $24$ by $2$"})
I("chords-and-power-of-a-point", 3,
  r"From an external point a tangent of length $6$ touches a circle, and a secant "
  r"from the same point meets the circle first at distance $4$. Find the length of "
  r"the FAR segment of the secant.",
  {"A": r"$5$", "B": r"$9$", "C": r"$8$", "D": r"$2$"}, "A",
  ["Eq(6**2, 4*9)", "Eq(9 - 4, 5)"],
  r"$6^{2} = 4 \times (\text{whole secant})$ gives a whole secant of $9$, so the "
  r"far segment is $9 - 4 = 5$.",
  {"B": "gave the whole secant rather than the far segment",
   "C": "used $6^{2} = 4 + x$", "D": "divided $6^{2}$ by $4$ then halved"})
I("chords-and-power-of-a-point", 4,
  r"Chords $AB$ and $CD$ meet at $P$ inside a circle with $AP = x$, $PB = x+2$, "
  r"$CP = 3$ and $PD = 8$. Find $x$.",
  {"A": r"$4$", "B": r"$6$", "C": r"$-6$", "D": r"$3$"}, "A",
  ["Eq(4*(4+2), 3*8)", "Eq(simplify((x+6)*(x-4) - (x**2 + 2*x - 24)), 0)"],
  r"$x(x+2) = 24$, so $x^{2}+2x-24=0$ and $(x+6)(x-4)=0$. Only $x=4$ is a length.",
  {"B": "took the wrong root's magnitude", "C": "kept the negative root as a length",
   "D": "solved $x + 2 = 8 - 3$"})

# ============ 32. coordinate-midpoint — 0.52% ==============================
I("coordinate-midpoint", 2,
  r"Find the midpoint of $(-3,\ 5)$ and $(7,\ 1)$.",
  {"A": r"$(2,\ 3)$", "B": r"$(5,\ 2)$", "C": r"$(2,\ -2)$", "D": r"$(10,\ 6)$"}, "A",
  ["Eq(Rational(-3+7, 2), 2)", "Eq(Rational(5+1, 2), 3)"],
  r"$\left(\dfrac{-3+7}{2},\ \dfrac{5+1}{2}\right) = (2,\ 3)$.",
  {"B": "halved the differences instead of the sums",
   "C": "subtracted the $y$-coordinates", "D": "added without halving"})
I("coordinate-midpoint", 3,
  r"$M(4,-1)$ is the midpoint of $A(1,3)$ and $B$. Find $B$.",
  {"A": r"$(7,\ -5)$", "B": r"$(2.5,\ 1)$", "C": r"$(7,\ -1)$", "D": r"$(-2,\ 7)$"}, "A",
  ["Eq(Rational(1+7, 2), 4)", "Eq(Rational(3+(-5), 2), -1)"],
  r"$B = (2 \times 4 - 1,\ 2 \times (-1) - 3) = (7,\ -5)$.",
  {"B": "found the midpoint of $A$ and $M$",
   "C": "doubled the $x$ but copied the $y$ from $M$",
   "D": "reflected $A$ in the origin instead"})
I("coordinate-midpoint", 4,
  r"$P$ divides $AB$ in the ratio $1:3$, where $A(2,1)$ and $B(10,9)$. Find $P$.",
  {"A": r"$(4,\ 3)$", "B": r"$(8,\ 7)$", "C": r"$(6,\ 5)$", "D": r"$(4.5,\ 3.5)$"}, "A",
  ["Eq(2 + Rational(1,4)*(10-2), 4)", "Eq(1 + Rational(1,4)*(9-1), 3)"],
  r"$P = A + \tfrac14(B-A) = (2+2,\ 1+2) = (4,\ 3)$.",
  {"B": "used the ratio $3:1$ — measured from the wrong end",
   "C": "used the midpoint", "D": "used $\\tfrac13$ instead of $\\tfrac14$"})

# ============ 33. line-circle-intersection — 0.52% =========================
I("line-circle-intersection", 2,
  r"How many points does the line $y = 1$ share with the circle $x^{2}+y^{2}=25$?",
  {"A": r"$2$", "B": r"$1$", "C": r"$0$", "D": r"infinitely many"}, "A",
  ["Eq(25 - 1**2, 24)", "(25 - 1**2) > 0"],
  r"Substituting gives $x^{2} = 24 > 0$, so there are two values of $x$.",
  {"B": "treated the line as a tangent", "C": "thought $y=1$ lies outside the circle",
   "D": "confused the line with the circle itself"})
I("line-circle-intersection", 3,
  r"For which values of $c$ is $y = x + c$ tangent to $x^{2}+y^{2}=8$?",
  {"A": r"$c = \pm 4$", "B": r"$c = \pm 2\sqrt{2}$", "C": r"$c = \pm 8$",
   "D": r"$c = \pm 4\sqrt{2}$"}, "A",
  ["Eq(simplify(expand(2*x**2 + 2*4*x + 4**2 - 8)), simplify(expand(2*(x+2)**2)))",
   "Eq((2*4)**2 - 4*2*(4**2 - 8), 0)"],
  r"Substituting gives $2x^{2}+2cx+c^{2}-8=0$; tangency needs $\Delta = 0$, "
  r"i.e. $4c^{2}-8(c^{2}-8)=0$, so $c^{2}=16$ and $c=\pm4$.",
  {"B": "used the radius $2\\sqrt{2}$ as the intercept",
   "C": "solved $c^{2}=64$", "D": "multiplied the radius by $2$"})
I("line-circle-intersection", 4,
  r"Find the point(s) where $y = 2x - 5$ meets $x^{2}+y^{2}=5$.",
  {"A": r"$(2,\ -1)$ only", "B": r"$(2,\ -1)$ and $(-2,\ -9)$", "C": r"$(1,\ -3)$ only",
   "D": r"they do not meet"}, "A",
  ["Eq(2**2 + (-1)**2, 5)", "Eq(2*2 - 5, -1)",
   "Eq(simplify(5*x**2 - 20*x + 20 - 5*(x-2)**2), 0)"],
  r"$x^{2}+(2x-5)^{2}=5$ reduces to $5(x-2)^{2}=0$, a repeated root at $x=2$: "
  r"the line is a tangent, touching at $(2,-1)$.",
  {"B": "assumed a quadratic always gives two distinct points",
   "C": "arithmetic slip solving for $x$", "D": "read the repeated root as no solution"})

# ============ 34. parallel-perpendicular-lines — 0.52% =====================
I("parallel-perpendicular-lines", 2,
  r"Find the gradient of a line perpendicular to $y = 3x + 1$.",
  {"A": r"$-\dfrac{1}{3}$", "B": r"$3$", "C": r"$\dfrac{1}{3}$", "D": r"$-3$"}, "A",
  ["Eq(3*Rational(-1,3), -1)"],
  r"Perpendicular gradients multiply to $-1$, so it is $-\tfrac13$.",
  {"B": "gave the parallel gradient", "C": "took the reciprocal but not the negative",
   "D": "took the negative but not the reciprocal"})
I("parallel-perpendicular-lines", 3,
  r"Find the equation of the line through $(2,5)$ parallel to $2x + y = 7$.",
  {"A": r"$y = -2x + 9$", "B": r"$y = 2x + 1$", "C": r"$y = -2x + 5$",
   "D": r"$y = \tfrac12 x + 4$"}, "A",
  ["Eq(-2*2 + 9, 5)", "Eq(solve(Eq(2*x + symbols('y'), 7), symbols('y'))[0], 7 - 2*x)"],
  r"The gradient is $-2$, so $y - 5 = -2(x-2)$, i.e. $y = -2x+9$.",
  {"B": "used $+2$ as the gradient", "C": "used the $y$-coordinate as the intercept",
   "D": "used the perpendicular gradient"})
I("parallel-perpendicular-lines", 4,
  r"For which $k$ are $kx + 4y = 3$ and $2x - 3y = 1$ perpendicular?",
  {"A": r"$k = 6$", "B": r"$k = -6$", "C": r"$k = \dfrac{8}{3}$",
   "D": r"$k = \dfrac{3}{2}$"}, "A",
  ["Eq(Rational(-6,4)*Rational(2,3), -1)"],
  r"The gradients are $-\dfrac{k}{4}$ and $\dfrac23$; their product is $-1$ when "
  r"$k = 6$.",
  {"B": "sign slip solving for $k$", "C": "set the gradients equal instead",
   "D": "inverted the second gradient"})

# ============ 35. quadrilateral-properties — 0.52% =========================
I("quadrilateral-properties", 2,
  r"One angle of a parallelogram is $65^{\circ}$. Find an adjacent angle.",
  {"A": r"$115^{\circ}$", "B": r"$65^{\circ}$", "C": r"$25^{\circ}$",
   "D": r"$130^{\circ}$"}, "A",
  ["Eq(180 - 65, 115)"],
  r"Adjacent angles of a parallelogram are supplementary: $180^{\circ}-65^{\circ}$.",
  {"B": "gave the opposite angle, which is the equal one",
   "C": "used the complement", "D": "doubled the given angle"})
I("quadrilateral-properties", 3,
  r"A rhombus has diagonals of length $6$ and $8$. Find its side length.",
  {"A": r"$5$", "B": r"$10$", "C": r"$7$", "D": r"$\sqrt{14}$"}, "A",
  ["Eq(sqrt(3**2 + 4**2), 5)"],
  r"The diagonals bisect at right angles, so the side is $\sqrt{3^{2}+4^{2}} = 5$.",
  {"B": "used the full diagonals instead of their halves",
   "C": "averaged the halves", "D": "added the halves before squaring"})
I("quadrilateral-properties", 4,
  r"A rectangle has perimeter $34$ and diagonal $13$. Find its area.",
  {"A": r"$60$", "B": r"$120$", "C": r"$72$", "D": r"$30$"}, "A",
  ["Eq(17**2 - 13**2, 120)", "Eq(Rational(120,2), 60)", "Eq(5+12, 17)",
   "Eq(5**2 + 12**2, 13**2)", "Eq(5*12, 60)"],
  r"$l+w = 17$ and $l^{2}+w^{2}=169$, so $2lw = 17^{2}-169 = 120$ and the area "
  r"$lw = 60$ (the sides are $5$ and $12$).",
  {"B": "stopped at $2lw$", "C": "guessed $6 \\times 12$",
   "D": "halved the area a second time"})

# ============ 36. rotation — 0.52% =========================================
I("rotation", 2,
  r"Rotate the point $(3,0)$ by $90^{\circ}$ anticlockwise about the origin.",
  {"A": r"$(0,\ 3)$", "B": r"$(0,\ -3)$", "C": r"$(-3,\ 0)$", "D": r"$(3,\ 0)$"}, "A",
  ["Eq(Matrix([[0,-1],[1,0]])*Matrix([3,0]), Matrix([0,3]))"],
  r"$(x,y) \mapsto (-y,\ x)$, so $(3,0) \mapsto (0,3)$.",
  {"B": "rotated clockwise instead", "C": "rotated by $180^{\\circ}$",
   "D": "left the point unchanged"})
I("rotation", 3,
  r"Rotate the point $(2,5)$ by $180^{\circ}$ about the origin.",
  {"A": r"$(-2,\ -5)$", "B": r"$(5,\ 2)$", "C": r"$(-5,\ -2)$", "D": r"$(2,\ -5)$"}, "A",
  ["Eq(Matrix([[-1,0],[0,-1]])*Matrix([2,5]), Matrix([-2,-5]))"],
  r"$(x,y) \mapsto (-x,-y)$.",
  {"B": "swapped the coordinates instead", "C": "swapped and negated",
   "D": "reflected in the $x$-axis"})
I("rotation", 4,
  r"Rotate the point $(1,2)$ by $90^{\circ}$ clockwise about the origin.",
  {"A": r"$(2,\ -1)$", "B": r"$(-2,\ 1)$", "C": r"$(2,\ 1)$", "D": r"$(-1,\ 2)$"}, "A",
  ["Eq(Matrix([[0,1],[-1,0]])*Matrix([1,2]), Matrix([2,-1]))"],
  r"Clockwise: $(x,y) \mapsto (y,\ -x)$, so $(1,2) \mapsto (2,-1)$.",
  {"B": "rotated anticlockwise", "C": "swapped without changing a sign",
   "D": "negated the wrong coordinate"})

# ============ 37. special-right-triangles — 0.52% ==========================
I("special-right-triangles", 2,
  r"A right-angled isosceles triangle has legs of length $7$. Find the hypotenuse.",
  {"A": r"$7\sqrt{2}$", "B": r"$14$", "C": r"$7\sqrt{3}$", "D": r"$\dfrac{7}{\sqrt{2}}$"},
  "A",
  ["Eq(sqrt(7**2 + 7**2), 7*sqrt(2))"],
  r"$\sqrt{7^{2}+7^{2}} = 7\sqrt{2}$.",
  {"B": "doubled the leg", "C": "used the $30$–$60$–$90$ ratio",
   "D": "divided by $\\sqrt{2}$ instead of multiplying"})
I("special-right-triangles", 3,
  r"In a $30^{\circ}$–$60^{\circ}$–$90^{\circ}$ triangle the shortest side is $5$. "
  r"Find the hypotenuse.",
  {"A": r"$10$", "B": r"$5\sqrt{3}$", "C": r"$5\sqrt{2}$", "D": r"$10\sqrt{3}$"}, "A",
  ["Eq(5*2, 10)", "Eq(5**2 + (5*sqrt(3))**2, 10**2)"],
  r"The sides are in the ratio $1 : \sqrt3 : 2$, so the hypotenuse is $2 \times 5 = 10$.",
  {"B": "gave the middle side", "C": "used the isosceles ratio",
   "D": "multiplied the middle side by $2$"})
I("special-right-triangles", 4,
  r"An equilateral triangle has side $6$. Find its height.",
  {"A": r"$3\sqrt{3}$", "B": r"$6\sqrt{3}$", "C": r"$3$", "D": r"$3\sqrt{2}$"}, "A",
  ["Eq(sqrt(6**2 - 3**2), 3*sqrt(3))"],
  r"The height splits the base in half: $\sqrt{6^{2}-3^{2}} = \sqrt{27} = 3\sqrt3$.",
  {"B": "used the full side as the base of the right triangle",
   "C": "halved the side and stopped", "D": "used the isosceles ratio"})

# ============ 38. trapezoid-properties — 0.52% =============================
I("trapezoid-properties", 2,
  r"A trapezoid has parallel sides $7$ and $11$ and height $5$. Find its area.",
  {"A": r"$45$", "B": r"$90$", "C": r"$55$", "D": r"$40$"}, "A",
  ["Eq(Rational(1,2)*(7+11)*5, 45)"],
  r"$\tfrac12(7+11)(5) = 45$.",
  {"B": "omitted the factor $\\tfrac12$", "C": "used $11 \\times 5$",
   "D": "used the difference of the parallel sides"})
I("trapezoid-properties", 3,
  r"A trapezoid has area $60$ and parallel sides $8$ and $12$. Find its height.",
  {"A": r"$6$", "B": r"$3$", "C": r"$12$", "D": r"$\dfrac{20}{3}$"}, "A",
  ["Eq(solve(Eq(Rational(1,2)*(8+12)*symbols('h'), 60), symbols('h'))[0], 6)"],
  r"$\tfrac12(20)h = 60$ gives $10h = 60$, so $h = 6$.",
  {"B": "forgot the $\\tfrac12$ when rearranging", "C": "divided by the smaller side",
   "D": "divided $60$ by $9$"})
I("trapezoid-properties", 4,
  r"An isosceles trapezoid has parallel sides $10$ and $4$ and legs of length $5$. "
  r"Find its height.",
  {"A": r"$4$", "B": r"$5$", "C": r"$3$", "D": r"$\sqrt{21}$"}, "A",
  ["Eq(Rational(10-4, 2), 3)", "Eq(sqrt(5**2 - 3**2), 4)"],
  r"Each end overhangs by $\dfrac{10-4}{2}=3$, so the height is "
  r"$\sqrt{5^{2}-3^{2}} = 4$.",
  {"B": "used the leg as the height", "C": "gave the overhang instead of the height",
   "D": "used an overhang of $2$"})

# ============ 39. data-representation — 0.50% ==============================
I("data-representation", 2,
  r"A frequency table records the values $1$, $2$, $3$ with frequencies $4$, $6$, "
  r"$10$. Find the mean.",
  {"A": r"$2.3$", "B": r"$2$", "C": r"$6\tfrac23$", "D": r"$15\tfrac13$"}, "A",
  ["Eq(Rational(1*4 + 2*6 + 3*10, 4+6+10), Rational(23,10))"],
  r"$\dfrac{1(4)+2(6)+3(10)}{20} = \dfrac{46}{20} = 2.3$.",
  {"B": "averaged the values, ignoring the frequencies",
   "C": "averaged the frequencies", "D": "divided by the number of values, not the total"})
I("data-representation", 3,
  r"A histogram has three bars, each of width $10$, with frequency densities "
  r"$0.4$, $1.2$ and $0.9$. Find the total frequency.",
  {"A": r"$25$", "B": r"$2.5$", "C": r"$250$", "D": r"$30$"}, "A",
  ["Eq(10*(Rational(4,10) + Rational(12,10) + Rational(9,10)), 25)"],
  r"Frequency is density times width: $10(0.4+1.2+0.9) = 25$.",
  {"B": "added the densities without multiplying by the width",
   "C": "multiplied by $100$", "D": "used a width of $12$"})
I("data-representation", 4,
  r"A bar chart has four categories whose frequencies are in the ratio "
  r"$2:3:4:1$, with total $60$. Find the largest frequency.",
  {"A": r"$24$", "B": r"$6$", "C": r"$18$", "D": r"$30$"}, "A",
  ["Eq(Rational(4,10)*60, 24)", "Eq(2+3+4+1, 10)"],
  r"There are $2+3+4+1 = 10$ parts, so one part is $6$ and the largest is "
  r"$4 \times 6 = 24$.",
  {"B": "gave the size of one part", "C": "used the ratio $3$",
   "D": "halved the total"})

# ============ 40. absolute-value-equations — 0.50% =========================
I("absolute-value-equations", 2,
  r"Solve $|x - 3| = 7$.",
  {"A": r"$x = 10$ or $x = -4$", "B": r"$x = 10$", "C": r"$x = 4$ or $x = -4$",
   "D": r"$x = 10$ or $x = 4$"}, "A",
  ["Eq(Abs(10 - 3), 7)", "Eq(Abs(-4 - 3), 7)"],
  r"$x-3 = 7$ or $x-3 = -7$, giving $x = 10$ or $x = -4$.",
  {"B": "took only the positive case", "C": "solved $|x| = \\pm 7$ then subtracted",
   "D": "sign slip on the negative case"})
I("absolute-value-equations", 3,
  r"Solve $|2x + 1| = 9$.",
  {"A": r"$x = 4$ or $x = -5$", "B": r"$x = 4$", "C": r"$x = 4$ or $x = 5$",
   "D": r"$x = -4$ or $x = 5$"}, "A",
  ["Eq(Abs(2*4 + 1), 9)", "Eq(Abs(2*(-5) + 1), 9)"],
  r"$2x+1 = 9$ gives $x=4$; $2x+1 = -9$ gives $x = -5$.",
  {"B": "took only the positive case", "C": "sign slip on the negative case",
   "D": "negated both roots"})
I("absolute-value-equations", 4,
  r"Solve $|x - 2| = 3x - 6$.",
  {"A": r"$x = 2$ only", "B": r"$x = 2$ or $x = 1$", "C": r"$x = 1$",
   "D": r"no solution"}, "A",
  ["Eq(Abs(2 - 2), 3*2 - 6)", "Ne(Abs(1 - 2), 3*1 - 6)"],
  r"The right side is $3(x-2)$, so with $u = x-2$: $|u| = 3u$, which forces "
  r"$u \ge 0$ and then $u = 3u$, i.e. $u = 0$ and $x = 2$.",
  {"B": "kept a root that makes the right-hand side negative",
   "C": "solved the negative case without checking it",
   "D": "rejected every root, including the valid one"})
