"""Gap items, batch C — ranks 41-60 by exam weight (0.50% down to 0.32%).

A further 8.09 points, taking the closed share of the gap past 93%.
"""

from item_bank import I

# ============ 41. absolute-value-inequalities — 0.50% ======================
I("absolute-value-inequalities", 2,
  r"Solve $|x| < 5$.",
  {"A": r"$-5 < x < 5$", "B": r"$x < 5$", "C": r"$x < -5$ or $x > 5$",
   "D": r"$-5 \le x \le 5$"}, "A",
  ["Abs(4) < 5", "Abs(-4) < 5", "Not(Abs(6) < 5)"],
  r"$|x|<5$ means $x$ is within $5$ of zero: $-5<x<5$.",
  {"B": "kept only the positive half", "C": "solved $|x|>5$ instead",
   "D": "included the endpoints although the inequality is strict"})
I("absolute-value-inequalities", 3,
  r"Solve $|x - 4| \ge 3$.",
  {"A": r"$x \le 1$ or $x \ge 7$", "B": r"$1 \le x \le 7$", "C": r"$x \ge 7$",
   "D": r"$-7 \le x \le -1$"}, "A",
  ["Abs(1 - 4) >= 3", "Abs(7 - 4) >= 3", "Not(Abs(4 - 4) >= 3)"],
  r"$x-4 \ge 3$ or $x-4 \le -3$, giving $x \ge 7$ or $x \le 1$.",
  {"B": "solved the '<' version — this is the inside of the interval",
   "C": "kept only the positive case", "D": "negated the endpoints"})
I("absolute-value-inequalities", 4,
  r"Solve $|2x - 1| < 5$.",
  {"A": r"$-2 < x < 3$", "B": r"$-3 < x < 2$", "C": r"$x < -2$ or $x > 3$",
   "D": r"$-2 \le x \le 3$"}, "A",
  ["Abs(2*0 - 1) < 5", "Not(Abs(2*3 - 1) < 5)", "Not(Abs(2*(-2) - 1) < 5)"],
  r"$-5 < 2x-1 < 5$ gives $-4 < 2x < 6$, so $-2 < x < 3$.",
  {"B": "divided before adding $1$", "C": "solved the '>' version",
   "D": "included the endpoints although the inequality is strict"})

# ============ 42. completing-the-square — 0.50% ============================
I("completing-the-square", 2,
  r"Write $x^{2} + 6x + 5$ in the form $(x+p)^{2}+q$.",
  {"A": r"$(x+3)^{2} - 4$", "B": r"$(x+3)^{2} + 5$", "C": r"$(x+6)^{2} - 31$",
   "D": r"$(x+3)^{2} - 9$"}, "A",
  ["Eq(simplify(expand((x+3)**2 - 4) - (x**2 + 6*x + 5)), 0)"],
  r"$(x+3)^{2} = x^{2}+6x+9$, so $x^{2}+6x+5 = (x+3)^{2} - 9 + 5 = (x+3)^{2}-4$.",
  {"B": "did not subtract the $9$ that was added",
   "C": "halved nothing — used the whole coefficient of $x$",
   "D": "subtracted the $9$ but forgot the $+5$"})
I("completing-the-square", 3,
  r"Write $x^{2} - 8x + 3$ in the form $(x+p)^{2}+q$.",
  {"A": r"$(x-4)^{2} - 13$", "B": r"$(x-4)^{2} + 3$", "C": r"$(x-8)^{2} - 61$",
   "D": r"$(x-4)^{2} - 19$"}, "A",
  ["Eq(simplify(expand((x-4)**2 - 13) - (x**2 - 8*x + 3)), 0)"],
  r"$(x-4)^{2} = x^{2}-8x+16$, so the expression is $(x-4)^{2} - 16 + 3 = (x-4)^{2}-13$.",
  {"B": "did not subtract the $16$", "C": "used the whole coefficient instead of half",
   "D": "subtracted $16$ and $3$ instead of adding the $3$"})
I("completing-the-square", 4,
  r"Write $2x^{2} + 12x + 7$ in the form $a(x+p)^{2}+q$.",
  {"A": r"$2(x+3)^{2} - 11$", "B": r"$2(x+3)^{2} + 7$", "C": r"$(x+3)^{2} - 11$",
   "D": r"$2(x+6)^{2} - 65$"}, "A",
  ["Eq(simplify(expand(2*(x+3)**2 - 11) - (2*x**2 + 12*x + 7)), 0)"],
  r"Take out the $2$ first: $2(x^{2}+6x)+7 = 2\big[(x+3)^{2}-9\big]+7 = 2(x+3)^{2}-11$.",
  {"B": "forgot that the $-9$ inside is multiplied by $2$",
   "C": "dropped the leading factor $2$",
   "D": "did not halve the coefficient after factoring out the $2$"})

# ============ 43. factoring-by-grouping — 0.50% ============================
I("factoring-by-grouping", 2,
  r"Factorise $x^{3} + 2x^{2} + 3x + 6$.",
  {"A": r"$(x+2)(x^{2}+3)$", "B": r"$(x+2)(x^{2}-3)$", "C": r"$(x-2)(x^{2}+3)$",
   "D": r"$(x+3)(x^{2}+2)$"}, "A",
  ["Eq(simplify(expand((x+2)*(x**2+3)) - (x**3 + 2*x**2 + 3*x + 6)), 0)"],
  r"$x^{2}(x+2) + 3(x+2) = (x+2)(x^{2}+3)$.",
  {"B": "sign error in the second group", "C": "sign error in the common factor",
   "D": "grouped the terms in the wrong pairs"})
I("factoring-by-grouping", 3,
  r"Factorise $2ax - 3ay + 2bx - 3by$.",
  {"A": r"$(2x-3y)(a+b)$", "B": r"$(2x+3y)(a+b)$", "C": r"$(2x-3y)(a-b)$",
   "D": r"$(2x-3y)ab$"}, "A",
  ["Eq(simplify(expand((2*x - 3*symbols('y'))*(symbols('a')+symbols('b'))) - "
   "(2*symbols('a')*x - 3*symbols('a')*symbols('y') + 2*symbols('b')*x - "
   "3*symbols('b')*symbols('y'))), 0)"],
  r"$a(2x-3y) + b(2x-3y) = (2x-3y)(a+b)$.",
  {"B": "sign error inside the first bracket",
   "C": "sign error inside the second bracket",
   "D": "multiplied $a$ and $b$ instead of adding them"})
I("factoring-by-grouping", 4,
  r"Factorise $xy - 3x - 2y + 6$.",
  {"A": r"$(y-3)(x-2)$", "B": r"$(y-3)(x+2)$", "C": r"$(y+3)(x-2)$",
   "D": r"$(y-3)(x-6)$"}, "A",
  ["Eq(simplify(expand((symbols('y')-3)*(x-2)) - (x*symbols('y') - 3*x - "
   "2*symbols('y') + 6)), 0)"],
  r"$x(y-3) - 2(y-3) = (y-3)(x-2)$.",
  {"B": "did not change the sign when factoring out $-2$",
   "C": "sign error in the first group", "D": "used $-6$ instead of $-2$"})

# ============ 44. polynomial-division — 0.50% ==============================
I("polynomial-division", 2,
  r"Divide: $\dfrac{x^{2}+5x+6}{x+2}$.",
  {"A": r"$x+3$", "B": r"$x+2$", "C": r"$x-3$", "D": r"$x^{2}+3$"}, "A",
  ["Eq(simplify((x**2 + 5*x + 6)/(x + 2) - (x + 3)), 0)"],
  r"$x^{2}+5x+6 = (x+2)(x+3)$, so the quotient is $x+3$.",
  {"B": "copied the divisor", "C": "sign error in the quotient",
   "D": "did not reduce the degree"})
I("polynomial-division", 3,
  r"Divide $2x^{3}+3x^{2}-5$ by $x+2$. Give the quotient and remainder.",
  {"A": r"$2x^{2}-x+2$, remainder $-9$", "B": r"$2x^{2}+x+2$, remainder $-9$",
   "C": r"$2x^{2}-x+2$, remainder $9$", "D": r"$2x^{2}-x-2$, remainder $9$"}, "A",
  ["Eq(simplify(expand((x+2)*(2*x**2 - x + 2) - 9) - (2*x**3 + 3*x**2 - 5)), 0)",
   "Eq((2*x**3 + 3*x**2 - 5).subs(x, -2), -9)"],
  r"Long division gives $2x^{2}-x+2$ with remainder $-9$; check with "
  r"$p(-2) = -16+12-5 = -9$.",
  {"B": "sign slip on the middle term of the quotient",
   "C": "sign slip on the remainder", "D": "two sign slips"})
I("polynomial-division", 4,
  r"Simplify $\dfrac{x^{3}-1}{x-1}$ for $x \ne 1$.",
  {"A": r"$x^{2}+x+1$", "B": r"$x^{2}-x+1$", "C": r"$x^{2}+1$", "D": r"$x^{2}-1$"}, "A",
  ["Eq(simplify((x**3 - 1)/(x - 1) - (x**2 + x + 1)), 0)"],
  r"$x^{3}-1 = (x-1)(x^{2}+x+1)$.",
  {"B": "used the sum-of-cubes factorisation",
   "C": "dropped the middle term", "D": "treated it as a difference of squares"})

# ============ 45. rational-equations — 0.50% ===============================
I("rational-equations", 2,
  r"Solve $\dfrac{3}{x} = 6$.",
  {"A": r"$x = \dfrac{1}{2}$", "B": r"$x = 2$", "C": r"$x = 18$",
   "D": r"$x = -\dfrac{1}{2}$"}, "A",
  ["Eq(3/Rational(1,2), 6)"],
  r"$3 = 6x$, so $x = \tfrac12$.",
  {"B": "inverted the final division", "C": "multiplied instead of dividing",
   "D": "sign slip"})
I("rational-equations", 3,
  r"Solve $\dfrac{1}{x} + \dfrac{1}{2x} = 3$.",
  {"A": r"$x = \dfrac{1}{2}$", "B": r"$x = \dfrac{1}{6}$", "C": r"$x = 2$",
   "D": r"$x = \dfrac{3}{2}$"}, "A",
  ["Eq(1/Rational(1,2) + 1/(2*Rational(1,2)), 3)"],
  r"$\dfrac{2}{2x} + \dfrac{1}{2x} = \dfrac{3}{2x} = 3$, so $2x = 1$ and $x = \tfrac12$.",
  {"B": "added the denominators instead of finding a common one",
   "C": "inverted at the last step", "D": "used $\\tfrac{3}{x} = 3$"})
I("rational-equations", 4,
  r"Solve $\dfrac{x}{x-3} = \dfrac{3}{x-3} + 2$.",
  {"A": r"no solution", "B": r"$x = 3$", "C": r"$x = 0$", "D": r"$x = 3$ or $x = 0$"},
  "A",
  ["Eq(3 - 3, 0)",
   "Eq(solve(Eq(x, 3 + 2*(x - 3)), x)[0], 3)"],
  r"Multiplying by $x-3$ gives $x = 3 + 2(x-3)$, so $x = 3$. But $x=3$ makes both "
  r"denominators zero, so it is extraneous and the equation has no solution.",
  {"B": "did not check the root against the denominator",
   "C": "solved a mis-expanded bracket", "D": "kept both an extraneous and a false root"})

# ============ 46. rearranging-formulas — 0.50% =============================
I("rearranging-formulas", 2,
  r"Make $a$ the subject of $v = u + at$.",
  {"A": r"$a = \dfrac{v-u}{t}$", "B": r"$a = \dfrac{v+u}{t}$", "C": r"$a = v-u-t$",
   "D": r"$a = t(v-u)$"}, "A",
  ["Eq(solve(Eq(symbols('v'), symbols('u') + symbols('a')*symbols('t')), symbols('a'))[0], "
   "(symbols('v') - symbols('u'))/symbols('t'))"],
  r"$v - u = at$, so $a = \dfrac{v-u}{t}$.",
  {"B": "moved $u$ across without changing its sign",
   "C": "subtracted $t$ instead of dividing", "D": "multiplied by $t$ instead of dividing"})
I("rearranging-formulas", 3,
  r"Make $r$ the subject of $A = \pi r^{2}$, taking $r > 0$.",
  {"A": r"$r = \sqrt{\dfrac{A}{\pi}}$", "B": r"$r = \dfrac{A}{\pi}$",
   "C": r"$r = \sqrt{A\pi}$", "D": r"$r = \left(\dfrac{A}{\pi}\right)^{2}$"}, "A",
  ["Eq(simplify(pi*(sqrt(symbols('A')/pi))**2 - symbols('A')), 0)"],
  r"$r^{2} = \dfrac{A}{\pi}$, so $r = \sqrt{\dfrac{A}{\pi}}$.",
  {"B": "forgot to take the square root",
   "C": "multiplied by $\\pi$ instead of dividing", "D": "squared instead of rooting"})
I("rearranging-formulas", 4,
  r"Make $l$ the subject of $S = \dfrac{n(a+l)}{2}$.",
  {"A": r"$l = \dfrac{2S}{n} - a$", "B": r"$l = \dfrac{2S}{n} + a$",
   "C": r"$l = \dfrac{S}{n} - a$", "D": r"$l = \dfrac{2S-a}{n}$"}, "A",
  ["Eq(solve(Eq(symbols('S'), symbols('n')*(symbols('a') + symbols('l'))/2), "
   "symbols('l'))[0], 2*symbols('S')/symbols('n') - symbols('a'))"],
  r"$2S = n(a+l)$, so $a+l = \dfrac{2S}{n}$ and $l = \dfrac{2S}{n} - a$.",
  {"B": "sign error moving $a$", "C": "forgot to multiply by $2$",
   "D": "subtracted $a$ before dividing by $n$"})

# ============ 47. vector-components — 0.48% ================================
I("vector-components", 2,
  r"$A(1,2)$ and $B(5,7)$. Find $\overrightarrow{AB}$ in component form.",
  {"A": r"$\begin{pmatrix}4\\5\end{pmatrix}$", "B": r"$\begin{pmatrix}6\\9\end{pmatrix}$",
   "C": r"$\begin{pmatrix}-4\\-5\end{pmatrix}$", "D": r"$\begin{pmatrix}5\\14\end{pmatrix}$"},
  "A",
  ["Eq(Matrix([5-1, 7-2]), Matrix([4,5]))"],
  r"$\overrightarrow{AB} = B - A = (5-1,\ 7-2)$.",
  {"B": "added the coordinates instead of subtracting",
   "C": "computed $\\overrightarrow{BA}$", "D": "multiplied the coordinates"})
I("vector-components", 3,
  r"$\vec{a} = \begin{pmatrix}2\\-1\end{pmatrix}$ and "
  r"$\vec{b} = \begin{pmatrix}-3\\5\end{pmatrix}$. Find $2\vec{a} + \vec{b}$.",
  {"A": r"$\begin{pmatrix}1\\3\end{pmatrix}$", "B": r"$\begin{pmatrix}-1\\3\end{pmatrix}$",
   "C": r"$\begin{pmatrix}1\\4\end{pmatrix}$", "D": r"$\begin{pmatrix}4\\3\end{pmatrix}$"},
  "A",
  ["Eq(2*Matrix([2,-1]) + Matrix([-3,5]), Matrix([1,3]))"],
  r"$2\vec{a} = (4,-2)$, and adding $\vec{b}$ gives $(1,3)$.",
  {"B": "sign slip on the first component", "C": "did not double the second component",
   "D": "doubled $\\vec{a}$ but forgot to add $\\vec{b}$'s first component"})
I("vector-components", 4,
  r"$\vec{a} = \begin{pmatrix}x\\3\end{pmatrix}$, $\vec{b} = \begin{pmatrix}2\\y\end{pmatrix}$ "
  r"and $\vec{a} + \vec{b} = \begin{pmatrix}5\\-1\end{pmatrix}$. Find $x$ and $y$.",
  {"A": r"$x=3,\ y=-4$", "B": r"$x=7,\ y=2$", "C": r"$x=3,\ y=4$",
   "D": r"$x=-3,\ y=-4$"}, "A",
  ["Eq(Matrix([3,3]) + Matrix([2,-4]), Matrix([5,-1]))"],
  r"Componentwise: $x+2=5$ so $x=3$; and $3+y=-1$ so $y=-4$.",
  {"B": "subtracted in the wrong direction", "C": "sign slip solving for $y$",
   "D": "sign slip solving for $x$"})

# ============ 48. concavity-and-inflection — 0.40% =========================
I("concavity-and-inflection", 2,
  r"Find $f''(x)$ for $f(x) = x^{3}$.",
  {"A": r"$6x$", "B": r"$3x^{2}$", "C": r"$6$", "D": r"$6x^{2}$"}, "A",
  ["Eq(diff(x**3, x, 2), 6*x)"],
  r"$f'(x)=3x^{2}$ and $f''(x)=6x$.",
  {"B": "stopped at the first derivative", "C": "differentiated three times",
   "D": "did not reduce the power on the second step"})
I("concavity-and-inflection", 3,
  r"Find the point of inflection of $y = x^{3} - 3x^{2} + 2$.",
  {"A": r"$(1,\ 0)$", "B": r"$(0,\ 2)$", "C": r"$(2,\ -2)$", "D": r"$(1,\ 2)$"}, "A",
  ["Eq(simplify(diff(x**3 - 3*x**2 + 2, x, 2) - (6*x - 6)), 0)",
   "Eq(solve(Eq(6*x - 6, 0), x)[0], 1)",
   "Eq((x**3 - 3*x**2 + 2).subs(x, 1), 0)"],
  r"$y'' = 6x-6 = 0$ at $x=1$, and $y(1) = 1-3+2 = 0$.",
  {"B": "used $x=0$", "C": "used a stationary point instead",
   "D": "found $x=1$ but read $y$ off the constant term"})
I("concavity-and-inflection", 4,
  r"For $y = x^{4} - 6x^{2}$, find where the curve is concave up.",
  {"A": r"$x < -1$ or $x > 1$", "B": r"$-1 < x < 1$", "C": r"$x > 1$",
   "D": r"all real $x$"}, "A",
  ["Eq(simplify(diff(x**4 - 6*x**2, x, 2) - (12*x**2 - 12)), 0)",
   "(12*2**2 - 12) > 0", "(12*0**2 - 12) < 0"],
  r"$y'' = 12x^{2}-12 > 0$ when $x^{2} > 1$, i.e. outside $[-1,1]$.",
  {"B": "took the interval where $y''<0$", "C": "kept only the positive branch",
   "D": "assumed a quartic is always concave up"})

# ============ 49. derivative-definition — 0.40% ============================
I("derivative-definition", 2,
  r"Using $f'(x) = \displaystyle\lim_{h \to 0}\frac{f(x+h)-f(x)}{h}$, find $f'(x)$ "
  r"for $f(x) = x^{2}$.",
  {"A": r"$2x$", "B": r"$x$", "C": r"$2$", "D": r"$x^{2}$"}, "A",
  ["Eq(limit(((x + symbols('h'))**2 - x**2)/symbols('h'), symbols('h'), 0), 2*x)"],
  r"$\dfrac{(x+h)^{2}-x^{2}}{h} = 2x+h \to 2x$.",
  {"B": "halved the result", "C": "differentiated twice",
   "D": "returned the function unchanged"})
I("derivative-definition", 3,
  r"For $f(x) = 3x+1$, simplify $\dfrac{f(x+h)-f(x)}{h}$.",
  {"A": r"$3$", "B": r"$3h$", "C": r"$3x+1$", "D": r"$3 + h$"}, "A",
  ["Eq(simplify(((3*(x + symbols('h')) + 1) - (3*x + 1))/symbols('h')), 3)"],
  r"$\dfrac{3(x+h)+1-(3x+1)}{h} = \dfrac{3h}{h} = 3$.",
  {"B": "did not cancel the $h$", "C": "returned the original function",
   "D": "kept a stray $h$ from the numerator"})
I("derivative-definition", 4,
  r"For $f(x) = x^{2}$, simplify $\dfrac{f(x+h)-f(x)}{h}$ BEFORE taking the limit.",
  {"A": r"$2x + h$", "B": r"$2x$", "C": r"$2x + h^{2}$", "D": r"$x + h$"}, "A",
  ["Eq(simplify(((x + symbols('h'))**2 - x**2)/symbols('h') - (2*x + symbols('h'))), 0)"],
  r"$\dfrac{x^{2}+2xh+h^{2}-x^{2}}{h} = \dfrac{2xh+h^{2}}{h} = 2x+h$.",
  {"B": "took the limit early", "C": "did not divide $h^{2}$ by $h$",
   "D": "cancelled an $x$ as well as the $h$"})

# ============ 50. volume-of-revolution — 0.40% =============================
I("volume-of-revolution", 2,
  r"The region under $y = 2$ from $x=0$ to $x=3$ is rotated about the $x$-axis. "
  r"Find the volume.",
  {"A": r"$12\pi$", "B": r"$6\pi$", "C": r"$4\pi$", "D": r"$36\pi$"}, "A",
  ["Eq(pi*integrate(2**2, (x, 0, 3)), 12*pi)"],
  r"$\pi\displaystyle\int_{0}^{3} 2^{2}\,dx = \pi(4)(3) = 12\pi$.",
  {"B": "forgot to square the radius", "C": "omitted the length of the interval",
   "D": "squared the whole product"})
I("volume-of-revolution", 3,
  r"The region under $y = x$ from $x=0$ to $x=2$ is rotated about the $x$-axis. "
  r"Find the volume.",
  {"A": r"$\dfrac{8\pi}{3}$", "B": r"$4\pi$", "C": r"$8\pi$", "D": r"$\dfrac{2\pi}{3}$"},
  "A",
  ["Eq(pi*integrate(x**2, (x, 0, 2)), Rational(8,3)*pi)"],
  r"$\pi\displaystyle\int_{0}^{2} x^{2}\,dx = \pi\left[\tfrac{x^{3}}{3}\right]_{0}^{2} "
  r"= \dfrac{8\pi}{3}$.",
  {"B": "integrated $x$ rather than $x^{2}$", "C": "forgot to divide by $3$",
   "D": "used an upper limit of $1$"})
I("volume-of-revolution", 4,
  r"The region under $y = \sqrt{x}$ from $x=0$ to $x=4$ is rotated about the "
  r"$x$-axis. Find the volume.",
  {"A": r"$8\pi$", "B": r"$16\pi$", "C": r"$4\pi$", "D": r"$\dfrac{32\pi}{3}$"}, "A",
  ["Eq(pi*integrate(x, (x, 0, 4)), 8*pi)"],
  r"$\pi\displaystyle\int_{0}^{4}\left(\sqrt{x}\right)^{2}dx "
  r"= \pi\int_{0}^{4} x\,dx = 8\pi$.",
  {"B": "did not halve when integrating $x$", "C": "used an upper limit of $2$",
   "D": "integrated $x^{2}$ instead of $x$"})

# ============ 51. piecewise-functions — 0.40% ==============================
I("piecewise-functions", 2,
  r"$f(x) = \begin{cases} 2x, & x < 1 \\ x+3, & x \ge 1 \end{cases}$. Find $f(1)$.",
  {"A": r"$4$", "B": r"$2$", "C": r"$5$", "D": r"undefined"}, "A",
  ["Eq(1 + 3, 4)"],
  r"At $x=1$ the second branch applies (the condition is $x \ge 1$), so $f(1)=4$.",
  {"B": "used the branch for $x<1$", "C": "used $x=2$",
   "D": "assumed the two branches conflict at $x=1$"})
I("piecewise-functions", 3,
  r"With the same $f$, find $f(-2) + f(3)$.",
  {"A": r"$2$", "B": r"$10$", "C": r"$-10$", "D": r"$4$"}, "A",
  ["Eq(2*(-2) + (3 + 3), 2)"],
  r"$f(-2) = 2(-2) = -4$ and $f(3) = 3+3 = 6$, so the sum is $2$.",
  {"B": "used $x+3$ for both inputs", "C": "used $2x$ for both inputs",
   "D": "took the difference instead of the sum"})
I("piecewise-functions", 4,
  r"$f(x) = \begin{cases} x^{2}, & x < 2 \\ kx, & x \ge 2 \end{cases}$. "
  r"Find $k$ so that $f$ is continuous at $x = 2$.",
  {"A": r"$k = 2$", "B": r"$k = 4$", "C": r"$k = \dfrac{1}{2}$", "D": r"$k = 8$"}, "A",
  ["Eq(solve(Eq(2**2, symbols('k')*2), symbols('k'))[0], 2)"],
  r"The two branches must agree at $x=2$: $2^{2} = 2k$, so $k=2$.",
  {"B": "set $k$ equal to the value $f(2)$ rather than solving $2k=4$",
   "C": "inverted the division", "D": "solved $k = 2^{3}$"})

# ============ 52. determinant-3x3 — 0.36% ==================================
I("determinant-3x3", 2,
  r"Find $\begin{vmatrix} 1 & 2 & 0 \\ 0 & 3 & 0 \\ 0 & 0 & 4 \end{vmatrix}$.",
  {"A": r"$12$", "B": r"$24$", "C": r"$7$", "D": r"$0$"}, "A",
  ["Eq(Matrix([[1,2,0],[0,3,0],[0,0,4]]).det(), 12)"],
  r"The matrix is upper triangular, so the determinant is the product of the "
  r"diagonal: $1 \times 3 \times 4 = 12$.",
  {"B": "included the off-diagonal $2$ as a factor",
   "C": "added the diagonal instead of multiplying",
   "D": "assumed the zeros force the determinant to zero"})
I("determinant-3x3", 3,
  r"Find $\begin{vmatrix} 1 & 2 & 3 \\ 0 & 1 & 4 \\ 5 & 6 & 0 \end{vmatrix}$.",
  {"A": r"$1$", "B": r"$-1$", "C": r"$49$", "D": r"$0$"}, "A",
  ["Eq(Matrix([[1,2,3],[0,1,4],[5,6,0]]).det(), 1)"],
  r"Expanding along the first row: $1(0-24) - 2(0-20) + 3(0-5) = -24+40-15 = 1$.",
  {"B": "sign error in the cofactor expansion",
   "C": "added the three products instead of alternating signs",
   "D": "assumed the zero entry makes the determinant zero"})
I("determinant-3x3", 4,
  r"For which $k$ is $\begin{vmatrix} 2 & 0 & 1 \\ 1 & 3 & 2 \\ 4 & 1 & k \end{vmatrix} = 0$?",
  {"A": r"$k = \dfrac{5}{2}$", "B": r"$k = -\dfrac{5}{2}$", "C": r"$k = 15$",
   "D": r"$k = \dfrac{2}{5}$"}, "A",
  ["Eq(Matrix([[2,0,1],[1,3,2],[4,1,Rational(5,2)]]).det(), 0)"],
  r"Expanding gives $6k - 15 = 0$, so $k = \dfrac{5}{2}$ — the value that makes "
  r"the matrix singular.",
  {"B": "sign slip solving $6k=15$", "C": "solved $k = 15$ without dividing",
   "D": "inverted the fraction"})

# ============ 53. matrix-addition-scalar — 0.36% ===========================
I("matrix-addition-scalar", 2,
  r"$A = \begin{pmatrix}1&2\\3&4\end{pmatrix}$, $B = \begin{pmatrix}0&-1\\2&1\end{pmatrix}$. "
  r"Find $A+B$.",
  {"A": r"$\begin{pmatrix}1&1\\5&5\end{pmatrix}$", "B": r"$\begin{pmatrix}1&3\\1&3\end{pmatrix}$",
   "C": r"$\begin{pmatrix}1&1\\5&3\end{pmatrix}$", "D": r"$\begin{pmatrix}0&-2\\6&4\end{pmatrix}$"},
  "A",
  ["Eq(Matrix([[1,2],[3,4]]) + Matrix([[0,-1],[2,1]]), Matrix([[1,1],[5,5]]))"],
  r"Add entry by entry.",
  {"B": "subtracted instead of adding", "C": "slip in the bottom-right entry",
   "D": "multiplied the entries"})
I("matrix-addition-scalar", 3,
  r"$A = \begin{pmatrix}2&-1\\0&4\end{pmatrix}$. Find $3A$.",
  {"A": r"$\begin{pmatrix}6&-3\\0&12\end{pmatrix}$", "B": r"$\begin{pmatrix}6&-1\\0&4\end{pmatrix}$",
   "C": r"$\begin{pmatrix}5&2\\3&7\end{pmatrix}$", "D": r"$\begin{pmatrix}6&-3\\3&12\end{pmatrix}$"},
  "A",
  ["Eq(3*Matrix([[2,-1],[0,4]]), Matrix([[6,-3],[0,12]]))"],
  r"Every entry is multiplied by $3$.",
  {"B": "scaled only the first column", "C": "added $3$ to every entry",
   "D": "turned the zero entry into $3$"})
I("matrix-addition-scalar", 4,
  r"$A = \begin{pmatrix}1&3\\2&0\end{pmatrix}$, $B = \begin{pmatrix}4&1\\0&5\end{pmatrix}$. "
  r"Find $2A - B$.",
  {"A": r"$\begin{pmatrix}-2&5\\4&-5\end{pmatrix}$", "B": r"$\begin{pmatrix}6&7\\4&5\end{pmatrix}$",
   "C": r"$\begin{pmatrix}-2&5\\4&5\end{pmatrix}$", "D": r"$\begin{pmatrix}2&5\\4&-5\end{pmatrix}$"},
  "A",
  ["Eq(2*Matrix([[1,3],[2,0]]) - Matrix([[4,1],[0,5]]), Matrix([[-2,5],[4,-5]]))"],
  r"$2A = \begin{pmatrix}2&6\\4&0\end{pmatrix}$, then subtract $B$ entry by entry.",
  {"B": "added $B$ instead of subtracting", "C": "sign slip in the bottom-right entry",
   "D": "sign slip in the top-left entry"})

# ============ 54. right-triangle-ratios — 0.36% ============================
I("right-triangle-ratios", 2,
  r"In a right-angled triangle the side opposite $\theta$ is $3$ and the hypotenuse "
  r"is $5$. Find $\sin\theta$.",
  {"A": r"$\dfrac{3}{5}$", "B": r"$\dfrac{4}{5}$", "C": r"$\dfrac{3}{4}$",
   "D": r"$\dfrac{5}{3}$"}, "A",
  ["Eq(Rational(3,5), Rational(3,5))", "Eq(sqrt(5**2 - 3**2), 4)"],
  r"$\sin\theta = \dfrac{\text{opposite}}{\text{hypotenuse}} = \dfrac35$.",
  {"B": "gave $\\cos\\theta$", "C": "gave $\\tan\\theta$",
   "D": "inverted the ratio"})
I("right-triangle-ratios", 3,
  r"A right-angled triangle has legs $5$ and $12$. Find the tangent of the angle "
  r"opposite the side of length $5$.",
  {"A": r"$\dfrac{5}{12}$", "B": r"$\dfrac{12}{5}$", "C": r"$\dfrac{5}{13}$",
   "D": r"$\dfrac{12}{13}$"}, "A",
  ["Eq(Rational(5,12), Rational(5,12))", "Eq(sqrt(5**2 + 12**2), 13)"],
  r"$\tan = \dfrac{\text{opposite}}{\text{adjacent}} = \dfrac{5}{12}$.",
  {"B": "inverted the ratio", "C": "gave the sine", "D": "gave the cosine"})
I("right-triangle-ratios", 4,
  r"In a right-angled triangle $\cos\theta = \dfrac{8}{17}$. Find $\tan\theta$.",
  {"A": r"$\dfrac{15}{8}$", "B": r"$\dfrac{8}{15}$", "C": r"$\dfrac{15}{17}$",
   "D": r"$\dfrac{17}{8}$"}, "A",
  ["Eq(sqrt(17**2 - 8**2), 15)", "Eq(Rational(15,8), Rational(15,8))"],
  r"The opposite side is $\sqrt{17^{2}-8^{2}} = 15$, so $\tan\theta = \dfrac{15}{8}$.",
  {"B": "inverted the ratio", "C": "gave the sine", "D": "gave the secant"})

# ============ 55. unit-circle-and-radians — 0.36% ==========================
I("unit-circle-and-radians", 2,
  r"Convert $120^{\circ}$ to radians.",
  {"A": r"$\dfrac{2\pi}{3}$", "B": r"$\dfrac{3\pi}{2}$", "C": r"$\dfrac{\pi}{6}$",
   "D": r"$\dfrac{3\pi}{4}$"}, "A",
  ["Eq(120*pi/180, 2*pi/3)"],
  r"$120 \times \dfrac{\pi}{180} = \dfrac{2\pi}{3}$.",
  {"B": "inverted the fraction", "C": "divided by $720$",
   "D": "converted $135^{\\circ}$ instead"})
I("unit-circle-and-radians", 3,
  r"In which quadrant does the angle $210^{\circ}$ lie?",
  {"A": r"third", "B": r"second", "C": r"fourth", "D": r"first"}, "A",
  ["(210 > 180)", "(210 < 270)"],
  r"$210^{\circ}$ is between $180^{\circ}$ and $270^{\circ}$, so it is in the "
  r"third quadrant, where sine and cosine are both negative.",
  {"B": "used the range $90^{\\circ}$–$180^{\\circ}$",
   "C": "used the range $270^{\\circ}$–$360^{\\circ}$",
   "D": "reduced modulo $180^{\\circ}$"})
I("unit-circle-and-radians", 4,
  r"Find $\sin 210^{\circ}$.",
  {"A": r"$-\dfrac{1}{2}$", "B": r"$\dfrac{1}{2}$", "C": r"$-\dfrac{\sqrt{3}}{2}$",
   "D": r"$\dfrac{\sqrt{3}}{2}$"}, "A",
  ["Eq(sin(210*pi/180), Rational(-1,2))"],
  r"The reference angle is $30^{\circ}$ and sine is negative in the third "
  r"quadrant, so $\sin 210^{\circ} = -\tfrac12$.",
  {"B": "used the reference angle but kept the sign positive",
   "C": "used $\\cos$ of the reference angle", "D": "both errors together"})

# ============ 56. polygon-angles — 0.34% ===================================
I("polygon-angles", 2,
  r"Find the sum of the interior angles of a hexagon.",
  {"A": r"$720^{\circ}$", "B": r"$1080^{\circ}$", "C": r"$360^{\circ}$",
   "D": r"$540^{\circ}$"}, "A",
  ["Eq((6-2)*180, 720)"],
  r"$(n-2) \times 180^{\circ} = 4 \times 180^{\circ} = 720^{\circ}$.",
  {"B": "used $n \\times 180^{\\circ}$", "C": "gave the exterior-angle sum",
   "D": "used a pentagon"})
I("polygon-angles", 3,
  r"Each interior angle of a regular polygon is $156^{\circ}$. Find the number of sides.",
  {"A": r"$15$", "B": r"$12$", "C": r"$24$", "D": r"$10$"}, "A",
  ["Eq(180 - 156, 24)", "Eq(Rational(360, 24), 15)", "Eq(Rational((15-2)*180, 15), 156)"],
  r"The exterior angle is $180^{\circ}-156^{\circ} = 24^{\circ}$, and "
  r"$\dfrac{360^{\circ}}{24^{\circ}} = 15$.",
  {"B": "divided $360^{\\circ}$ by $30^{\\circ}$", "C": "gave the exterior angle itself",
   "D": "divided $360^{\\circ}$ by $36^{\\circ}$"})
I("polygon-angles", 4,
  r"In a regular polygon each interior angle exceeds each exterior angle by "
  r"$100^{\circ}$. Find the number of sides.",
  {"A": r"$9$", "B": r"$6$", "C": r"$10$", "D": r"$18$"}, "A",
  ["Eq(140 + 40, 180)", "Eq(140 - 40, 100)", "Eq(Rational(360, 40), 9)"],
  r"With $i+e=180$ and $i-e=100$: $i=140$, $e=40$, so $n = \dfrac{360}{40} = 9$.",
  {"B": "used $e = 60^{\\circ}$", "C": "used $e = 36^{\\circ}$",
   "D": "used $e = 20^{\\circ}$"})

# ============ 57. sphere — 0.34% ===========================================
I("sphere", 2,
  r"Find the volume of a sphere of radius $3$.",
  {"A": r"$36\pi$", "B": r"$12\pi$", "C": r"$27\pi$", "D": r"$9\pi$"}, "A",
  ["Eq(Rational(4,3)*pi*3**3, 36*pi)"],
  r"$V = \tfrac43\pi r^{3} = \tfrac43\pi(27) = 36\pi$.",
  {"B": "used $4\\pi r$", "C": "used $r^{3}$ without the $\\tfrac43$",
   "D": "used the surface-area formula divided by $4$"})
I("sphere", 3,
  r"Find the surface area of a sphere of radius $5$.",
  {"A": r"$100\pi$", "B": r"$25\pi$", "C": r"$50\pi$",
   "D": r"$\dfrac{500\pi}{3}$"}, "A",
  ["Eq(4*pi*5**2, 100*pi)"],
  r"$S = 4\pi r^{2} = 100\pi$.",
  {"B": "used $\\pi r^{2}$ — the area of a circle",
   "C": "used $2\\pi r^{2}$", "D": "gave the volume"})
I("sphere", 4,
  r"A sphere has volume $288\pi$. Find its radius.",
  {"A": r"$6$", "B": r"$8$", "C": r"$12$", "D": r"$72$"}, "A",
  ["Eq(Rational(4,3)*pi*6**3, 288*pi)"],
  r"$\tfrac43\pi r^{3} = 288\pi$ gives $r^{3} = 216$, so $r = 6$.",
  {"B": "solved $r^{3} = 512$", "C": "doubled the radius",
   "D": "gave $r^{3}$ divided by $3$"})

# ============ 58. box-plots — 0.34% ========================================
I("box-plots", 2,
  r"A box plot shows minimum $3$, $Q_{1}=7$, median $10$, $Q_{3}=15$, maximum $22$. "
  r"Find the interquartile range.",
  {"A": r"$8$", "B": r"$19$", "C": r"$5$", "D": r"$12$"}, "A",
  ["Eq(15 - 7, 8)", "Eq(22 - 3, 19)"],
  r"$\text{IQR} = Q_{3}-Q_{1} = 15-7 = 8$.",
  {"B": "gave the range", "C": "used the median minus $Q_{1}$",
   "D": "used the maximum minus the median"})
I("box-plots", 3,
  r"Which of these can a box plot NOT tell you?",
  {"A": r"the mean", "B": r"the median", "C": r"the range",
   "D": r"the interquartile range"}, "A",
  ["Eq(1, 1)"],
  r"A box plot shows the five-number summary — minimum, $Q_{1}$, median, $Q_{3}$, "
  r"maximum — so the range and IQR follow, but the mean needs every data value.",
  {"B": "the median is the line inside the box",
   "C": "the range is maximum minus minimum, both shown",
   "D": "the IQR is the width of the box"})
I("box-plots", 4,
  r"A data set has $Q_{1}=12$ and $Q_{3}=20$. Using the $1.5 \times \text{IQR}$ rule, "
  r"above which value is a point an outlier?",
  {"A": r"$32$", "B": r"$28$", "C": r"$20$", "D": r"$40$"}, "A",
  ["Eq(20 - 12, 8)", "Eq(20 + Rational(3,2)*8, 32)"],
  r"$\text{IQR}=8$, so the upper fence is $Q_{3} + 1.5(8) = 20 + 12 = 32$.",
  {"B": "used $1.0 \\times \\text{IQR}$", "C": "used $Q_{3}$ itself as the fence",
   "D": "used $2.5 \\times \\text{IQR}$"})

# ============ 59. systems-three-linear — 0.33% =============================
I("systems-three-linear", 2,
  r"Solve for $x$: $\begin{cases} x+y+z=6 \\ y=2 \\ z=3 \end{cases}$",
  {"A": r"$x = 1$", "B": r"$x = 6$", "C": r"$x = 5$", "D": r"$x = 0$"}, "A",
  ["Eq(1 + 2 + 3, 6)"],
  r"$x = 6 - 2 - 3 = 1$.",
  {"B": "ignored the other two equations", "C": "subtracted only one of them",
   "D": "subtracted $6$ as well"})
I("systems-three-linear", 3,
  r"Solve for $x$: $\begin{cases} x+y+z=9 \\ x-y=1 \\ z=2 \end{cases}$",
  {"A": r"$x = 4$", "B": r"$x = 3$", "C": r"$x = 5$", "D": r"$x = 4.5$"}, "A",
  ["Eq(4 + 3 + 2, 9)", "Eq(4 - 3, 1)"],
  r"With $z=2$: $x+y=7$; combined with $x-y=1$ this gives $2x=8$, so $x=4$.",
  {"B": "solved for $y$ instead", "C": "used $x+y=9$",
   "D": "halved $9$ without using the second equation"})
I("systems-three-linear", 4,
  r"Solve for $y$: $\begin{cases} x+y+z=6 \\ x-y+z=2 \\ 2x+y-z=1 \end{cases}$",
  {"A": r"$y = 2$", "B": r"$y = 1$", "C": r"$y = 3$", "D": r"$y = 4$"}, "A",
  ["Eq(1 + 2 + 3, 6)", "Eq(1 - 2 + 3, 2)", "Eq(2*1 + 2 - 3, 1)"],
  r"Subtracting the second equation from the first gives $2y = 4$, so $y = 2$ "
  r"(the full solution is $x=1$, $y=2$, $z=3$).",
  {"B": "gave $x$", "C": "gave $z$", "D": "added the equations instead of subtracting"})

# ============ 60. interval-notation — 0.32% ================================
I("interval-notation", 2,
  r"Write $\{x : -2 < x \le 5\}$ in interval notation.",
  {"A": r"$(-2,\ 5]$", "B": r"$[-2,\ 5)$", "C": r"$[-2,\ 5]$", "D": r"$(-2,\ 5)$"}, "A",
  ["Not(-2 > -2)", "(5 <= 5)"],
  r"A round bracket excludes the endpoint, a square bracket includes it: $(-2,\ 5]$.",
  {"B": "swapped which endpoint is included", "C": "included both endpoints",
   "D": "excluded both endpoints"})
I("interval-notation", 3,
  r"What does $(-\infty,\ 3) \cup (3,\ \infty)$ describe?",
  {"A": r"all real numbers except $3$", "B": r"all real numbers",
   "C": r"$x > 3$", "D": r"$x < 3$"}, "A",
  ["Eq(1, 1)"],
  r"The two pieces cover everything below and everything above $3$, but $3$ itself "
  r"is in neither.",
  {"B": "overlooked that $3$ is excluded from both pieces",
   "C": "took only the second piece", "D": "took only the first piece"})
I("interval-notation", 4,
  r"Find $(-1,\ 4] \cap [2,\ 7)$.",
  {"A": r"$[2,\ 4]$", "B": r"$(2,\ 4)$", "C": r"$[2,\ 4)$", "D": r"$(-1,\ 7)$"}, "A",
  ["(2 >= 2)", "(4 <= 4)", "Not(4 < 4)"],
  r"The overlap runs from $2$ to $4$. Both endpoints are included: $2$ is in "
  r"$[2,7)$ and inside $(-1,4]$; $4$ is in $(-1,4]$ and inside $[2,7)$.",
  {"B": "excluded both endpoints", "C": "excluded $4$, which $(-1,4]$ includes",
   "D": "gave the union instead of the intersection"})
