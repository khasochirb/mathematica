"""Batch A — the 20 heaviest thin skills, 1.58% down to 0.79% exam weight.

Each item exists to give a skill the rung it is missing, nothing more. Where
a skill already has twelve hard questions, the easy item here is what lets
the engine tell "has not learned this" from "has not been asked yet".

Read with scripts/skills/rung_bank.py. Difficulty is the ENGINE scale:
1 easy, 2 medium, 3 hard.
"""

from sympy import Matrix, Rational

from rung_bank import R

# ---------------------------------------------------------------- 1.58%
R("quadratic-function-vertex", 1,
  r"Find the vertex of the parabola $y=(x-3)^2+4$.",
  {"A": r"$(3,\,4)$", "B": r"$(-3,\,4)$", "C": r"$(3,\,-4)$", "D": r"$(4,\,3)$"},
  "A",
  ["Eq(diff((x-3)**2+4, x).subs(x, 3), 0)",
   "Eq(((x-3)**2+4).subs(x, 3), 4)",
   "((x-3)**2+4).subs(x, 2) > 4"],
  r"In the form $y=(x-h)^2+k$ the vertex is $(h,k)$. Here $h=3$ and $k=4$, "
  r"so the vertex is $(3,4)$. Check: at $x=3$ the squared term is $0$, which "
  r"is as small as it can get, and $y=4$.",
  {"B": "read $h$ straight off the bracket as $-3$ instead of solving $x-3=0$",
   "C": "flipped the sign of $k$ as well as the sign inside the bracket",
   "D": "wrote the coordinates the wrong way round"})

# ---------------------------------------------------------------- 1.07%
R("discrete-random-variable", 3,
  r"A discrete random variable $X$ takes the values $1,2,3$ with "
  r"$P(X=k)=\dfrac{c}{2^k}$. Find $P(X\ge 2)$.",
  {"A": r"$\dfrac{3}{7}$", "B": r"$\dfrac{4}{7}$",
   "C": r"$\dfrac{3}{8}$", "D": r"$\dfrac{6}{7}$"},
  "A",
  ["Eq(Rational(8,7)*(Rational(1,2)+Rational(1,4)+Rational(1,8)), 1)",
   "Eq(Rational(8,7)*(Rational(1,4)+Rational(1,8)), Rational(3,7))",
   "Eq(Rational(8,7)*Rational(1,2), Rational(4,7))"],
  r"The probabilities must total $1$: "
  r"$$c\left(\tfrac12+\tfrac14+\tfrac18\right)=c\cdot\tfrac78=1,$$ so "
  r"$c=\tfrac87$. Then "
  r"$$P(X\ge 2)=c\left(\tfrac14+\tfrac18\right)=\tfrac87\cdot\tfrac38=\tfrac37.$$",
  {"B": r"computed $P(X=1)=\tfrac47$ — the complement of the answer, i.e. read $\ge$ as $<$",
   "C": r"forgot to find $c$ and added $\tfrac14+\tfrac18$ raw",
   "D": r"used $c=\tfrac87$ but summed all three probabilities instead of the last two"})

R("expected-value", 1,
  r"$X$ takes the value $1$ with probability $\tfrac12$, $2$ with probability "
  r"$\tfrac{3}{10}$ and $5$ with probability $\tfrac15$. Find $E(X)$.",
  {"A": r"$\dfrac{21}{10}$", "B": r"$\dfrac{8}{3}$", "C": r"$1$", "D": r"$5$"},
  "A",
  ["Eq(Rational(1,2)+Rational(3,10)+Rational(1,5), 1)",
   "Eq(1*Rational(1,2)+2*Rational(3,10)+5*Rational(1,5), Rational(21,10))",
   "Eq(Rational(1+2+5,3), Rational(8,3))"],
  r"Multiply each value by its probability and add: "
  r"$$E(X)=1\cdot\tfrac12+2\cdot\tfrac{3}{10}+5\cdot\tfrac15"
  r"=\tfrac12+\tfrac35+1=\tfrac{21}{10}.$$",
  {"B": "averaged the three values and ignored the probabilities",
   "C": "gave the most likely value instead of the mean",
   "D": "gave the largest value instead of the mean"})

# ---------------------------------------------------------------- 1.03%
R("transformation-matrices", 1,
  r"Which matrix represents a reflection in the $x$-axis?",
  {"A": r"$\begin{pmatrix}1&0\\0&-1\end{pmatrix}$",
   "B": r"$\begin{pmatrix}-1&0\\0&1\end{pmatrix}$",
   "C": r"$\begin{pmatrix}0&1\\1&0\end{pmatrix}$",
   "D": r"$\begin{pmatrix}-1&0\\0&-1\end{pmatrix}$"},
  "A",
  [],
  r"Reflecting in the $x$-axis keeps $x$ and negates $y$: $(x,y)\mapsto(x,-y)$. "
  r"The matrix whose columns are the images of $(1,0)$ and $(0,1)$ is therefore "
  r"$\begin{pmatrix}1&0\\0&-1\end{pmatrix}$. Test it on $(3,5)$: it gives $(3,-5)$.",
  {"B": r"that is reflection in the $y$-axis — it negates $x$ instead",
   "C": r"that is reflection in the line $y=x$ — it swaps the coordinates",
   "D": r"that is a half-turn about the origin — it negates both coordinates"},
  # Matrix equality is not something sympify can be handed as a string, so the
  # claim is checked as a Python predicate instead of faked into an Eq.
  check=lambda: (Matrix([[1, 0], [0, -1]]) * Matrix([[3], [5]]) == Matrix([[3], [-5]])
                 and Matrix([[-1, 0], [0, 1]]) * Matrix([[3], [5]]) == Matrix([[-3], [5]])
                 and Matrix([[0, 1], [1, 0]]) * Matrix([[3], [5]]) == Matrix([[5], [3]])
                 and Matrix([[-1, 0], [0, -1]]) * Matrix([[3], [5]]) == Matrix([[-3], [-5]])))

# ---------------------------------------------------------------- 1.01%
R("quartiles-and-iqr", 3,
  r"Find the interquartile range of "
  r"$$4,\;6,\;7,\;9,\;12,\;13,\;15,\;18,\;22.$$",
  {"A": r"$10$", "B": r"$11$", "C": r"$18$", "D": r"$12$"},
  "A",
  ["Eq(Rational(6+7,2), Rational(13,2))",
   "Eq(Rational(15+18,2), Rational(33,2))",
   "Eq(Rational(33,2)-Rational(13,2), 10)",
   "Eq(22-4, 18)"],
  r"There are nine values, so the median is the fifth, $12$. Exclude it and "
  r"take the median of each half. Lower half $4,6,7,9$ gives "
  r"$Q_1=\tfrac{6+7}{2}=6.5$; upper half $13,15,18,22$ gives "
  r"$Q_3=\tfrac{15+18}{2}=16.5$. Hence "
  r"$$\text{IQR}=16.5-6.5=10.$$",
  {"B": r"kept the median $12$ inside both halves, giving $Q_1=7$, $Q_3=18$",
   "C": r"that is the range, $22-4$, not the interquartile range",
   "D": r"gave the median instead of the spread"},
  check=lambda: sorted([4, 6, 7, 9, 12, 13, 15, 18, 22])[4] == 12)

# ---------------------------------------------------------------- 1.00%
R("antiderivative-power", 1,
  r"Find $\displaystyle\int 6x^2\,dx$.",
  {"A": r"$2x^3+C$", "B": r"$12x+C$", "C": r"$6x^3+C$", "D": r"$3x^3+C$"},
  "A",
  ["Eq(integrate(6*x**2, x), 2*x**3)",
   "Eq(diff(2*x**3, x), 6*x**2)",
   "Eq(diff(6*x**2, x), 12*x)"],
  r"Raise the power by one and divide by the new power: "
  r"$$\int 6x^2\,dx=\frac{6x^{3}}{3}+C=2x^3+C.$$ "
  r"Check by differentiating: $\frac{d}{dx}(2x^3)=6x^2$.",
  {"B": "differentiated instead of integrating",
   "C": "raised the power but forgot to divide by the new power",
   "D": "divided by the old power $2$ instead of the new power $3$"})

R("antiderivative-power", 3,
  r"$F$ is an antiderivative of $f(x)=3x^2-4x+1$ and $F(1)=5$. Find $F(2)$.",
  {"A": r"$7$", "B": r"$2$", "C": r"$5$", "D": r"$8$"},
  "A",
  ["Eq(integrate(3*x**2-4*x+1, x), x**3-2*x**2+x)",
   "Eq((x**3-2*x**2+x+5).subs(x, 1), 5)",
   "Eq((x**3-2*x**2+x+5).subs(x, 2), 7)",
   "Eq((3*x**2-4*x+1).subs(x, 2), 5)"],
  r"Integrate first: $F(x)=x^3-2x^2+x+C$. Use the given value to pin $C$: "
  r"$$F(1)=1-2+1+C=C=5.$$ So $F(x)=x^3-2x^2+x+5$ and "
  r"$$F(2)=8-8+2+5=7.$$",
  {"B": r"integrated correctly but dropped the constant, giving $F(2)=2$",
   "C": r"evaluated $f(2)$ instead of $F(2)$",
   "D": r"integrated only the leading term, $3x^2\to x^3$, and stopped at $2^3$"})

R("stationary-points-and-extrema", 1,
  r"Find the $x$-coordinate of the stationary point of $f(x)=x^2-6x+5$.",
  {"A": r"$3$", "B": r"$-3$", "C": r"$6$", "D": r"$5$"},
  "A",
  ["Eq(diff(x**2-6*x+5, x), 2*x-6)",
   "Eq(diff(x**2-6*x+5, x).subs(x, 3), 0)",
   "Eq((x**2-6*x+5).subs(x, 3), -4)"],
  r"A stationary point is where $f'(x)=0$. Here $f'(x)=2x-6$, so "
  r"$$2x-6=0\quad\Longrightarrow\quad x=3.$$",
  {"B": "solved $2x+6=0$ — sign slip on the $-6x$ term",
   "C": "set the derivative equal to the constant instead of to zero",
   "D": "quoted the constant term of $f$"})

# ---------------------------------------------------------------- 0.99%
R("graph-transformations", 1,
  r"The graph of $y=x^2$ is translated $3$ units in the positive $x$-direction. "
  r"What is the equation of the new graph?",
  {"A": r"$y=(x-3)^2$", "B": r"$y=(x+3)^2$", "C": r"$y=x^2-3$", "D": r"$y=x^2+3$"},
  "A",
  ["Eq(((x-3)**2).subs(x, 3), 0)",
   "Eq(((x-3)**2).subs(x, 0), 9)",
   "Eq(((x+3)**2).subs(x, -3), 0)"],
  r"A horizontal translation of $a$ to the right replaces $x$ by $x-a$, so "
  r"$y=x^2$ becomes $y=(x-3)^2$. Check where the vertex went: it was at $x=0$, "
  r"and $(x-3)^2$ is zero at $x=3$ — three units right, as required.",
  {"B": r"replaced $x$ by $x+3$, which moves the graph three units LEFT",
   "C": r"translated down instead of right",
   "D": r"translated up instead of right"})

# ---------------------------------------------------------------- 0.86%
R("addition-rule", 1,
  r"$A$ and $B$ are mutually exclusive with $P(A)=\tfrac25$ and $P(B)=\tfrac12$. "
  r"Find $P(A\cup B)$.",
  {"A": r"$\dfrac{9}{10}$", "B": r"$\dfrac{1}{5}$",
   "C": r"$\dfrac{1}{10}$", "D": r"$\dfrac{7}{10}$"},
  "A",
  ["Eq(Rational(2,5)+Rational(1,2), Rational(9,10))",
   "Eq(Rational(2,5)*Rational(1,2), Rational(1,5))",
   "Eq(Rational(1,2)-Rational(2,5), Rational(1,10))"],
  r"Mutually exclusive means $P(A\cap B)=0$, so the addition rule loses its "
  r"last term: "
  r"$$P(A\cup B)=P(A)+P(B)=\tfrac25+\tfrac12=\tfrac{9}{10}.$$",
  {"B": r"multiplied the probabilities — that is for independent events, and it answers a different question",
   "C": r"subtracted instead of adding",
   "D": r"subtracted a non-zero intersection; for mutually exclusive events there is none"})

R("addition-rule", 3,
  r"$P(A)=\tfrac35$, $P(B)=\tfrac12$ and $P(A\cup B)=\tfrac45$. Find the "
  r"probability that exactly one of $A$ and $B$ occurs.",
  {"A": r"$\dfrac{1}{2}$", "B": r"$\dfrac{3}{10}$",
   "C": r"$\dfrac{4}{5}$", "D": r"$\dfrac{1}{5}$"},
  "A",
  ["Eq(Rational(3,5)+Rational(1,2)-Rational(4,5), Rational(3,10))",
   "Eq(Rational(4,5)-Rational(3,10), Rational(1,2))",
   "Eq(1-Rational(4,5), Rational(1,5))"],
  r"First recover the intersection from the addition rule: "
  r"$$P(A\cap B)=P(A)+P(B)-P(A\cup B)=\tfrac35+\tfrac12-\tfrac45=\tfrac{3}{10}.$$ "
  r"''Exactly one'' is the union with the overlap removed: "
  r"$$P(A\cup B)-P(A\cap B)=\tfrac45-\tfrac{3}{10}=\tfrac12.$$",
  {"B": r"stopped at $P(A\cap B)$ — that is ''both'', not ''exactly one''",
   "C": r"gave $P(A\cup B)$, which counts the overlap as well",
   "D": r"gave the probability that neither occurs"})

R("geometric-probability", 1,
  r"A point is chosen at random on a segment of length $10$ cm. Find the "
  r"probability that it lies within $3$ cm of the left-hand end.",
  {"A": r"$\dfrac{3}{10}$", "B": r"$\dfrac{3}{5}$",
   "C": r"$\dfrac{1}{3}$", "D": r"$\dfrac{7}{10}$"},
  "A",
  ["Eq(Rational(3,10)*10, 3)",
   "Eq(1-Rational(3,10), Rational(7,10))",
   "Eq(Rational(6,10), Rational(3,5))"],
  r"For a uniform choice on a segment the probability is the ratio of lengths: "
  r"$$P=\frac{3}{10}.$$",
  {"B": r"counted $3$ cm at BOTH ends, which the question did not ask for",
   "C": r"compared $3$ with the remaining $7$ instead of with the whole $10$",
   "D": r"gave the probability of the complement — further than $3$ cm away"})

R("variance-of-random-variable", 1,
  r"$X$ takes the value $0$ or $1$, each with probability $\tfrac12$. Find "
  r"$\operatorname{Var}(X)$.",
  {"A": r"$\dfrac{1}{4}$", "B": r"$\dfrac{1}{2}$",
   "C": r"$\dfrac{1}{8}$", "D": r"$0$"},
  "A",
  ["Eq(0*Rational(1,2)+1*Rational(1,2), Rational(1,2))",
   "Eq(0**2*Rational(1,2)+1**2*Rational(1,2), Rational(1,2))",
   "Eq(Rational(1,2)-Rational(1,2)**2, Rational(1,4))"],
  r"$E(X)=0\cdot\tfrac12+1\cdot\tfrac12=\tfrac12$ and "
  r"$E(X^2)=0\cdot\tfrac12+1\cdot\tfrac12=\tfrac12$, so "
  r"$$\operatorname{Var}(X)=E(X^2)-\bigl(E(X)\bigr)^2=\tfrac12-\tfrac14=\tfrac14.$$",
  {"B": r"gave $E(X^2)$ and forgot to subtract $\bigl(E(X)\bigr)^2$",
   "C": r"halved the variance once too often",
   "D": r"assumed no spread; $X$ does vary, so the variance is not zero"})

R("variance-and-sd", 1,
  r"Find the variance of the data set $1,\;2,\;3,\;4,\;5$.",
  {"A": r"$2$", "B": r"$10$", "C": r"$\sqrt{2}$", "D": r"$\dfrac{5}{2}$"},
  "A",
  ["Eq(Rational(1+2+3+4+5, 5), 3)",
   "Eq(Rational(4+1+0+1+4, 5), 2)",
   "Eq(Rational(4+1+0+1+4, 4), Rational(5,2))"],
  r"The mean is $\bar x=\tfrac{15}{5}=3$. The squared deviations are "
  r"$4,1,0,1,4$, which total $10$, so "
  r"$$\sigma^2=\frac{10}{5}=2.$$",
  {"B": r"gave the total of the squared deviations without dividing by $5$",
   "C": r"gave the standard deviation $\sqrt{2}$, not the variance",
   "D": r"divided by $n-1=4$; the population variance divides by $n$"})

# ---------------------------------------------------------------- 0.83%
R("linear-equation-one-variable", 3,
  r"Solve $\dfrac{2x-1}{3}-\dfrac{x+2}{4}=\dfrac12$.",
  {"A": r"$x=\dfrac{16}{5}$", "B": r"$x=2$",
   "C": r"$x=\dfrac{4}{5}$", "D": r"$x=\dfrac{21}{10}$"},
  "A",
  ["Eq(solve(Eq((2*x-1)/3-(x+2)/4, Rational(1,2)), x)[0], Rational(16,5))",
   "Eq(((2*x-1)/3-(x+2)/4).subs(x, Rational(16,5)), Rational(1,2))",
   "Eq(4*(2*x-1)-3*(x+2), 5*x-10)"],
  r"Multiply every term by $12$: "
  r"$$4(2x-1)-3(x+2)=6.$$ Expand carefully — the $-3$ multiplies both terms in "
  r"the bracket: "
  r"$$8x-4-3x-6=6\quad\Longrightarrow\quad 5x-10=6,$$ so $5x=16$ and "
  r"$x=\tfrac{16}{5}$.",
  {"B": r"solved $5x-10=0$, forgetting the right-hand side",
   "C": r"distributed $-3$ over only the first term, getting $8x-4-3x+6=6$",
   "D": r"multiplied only the left-hand side by $12$ and left $\tfrac12$ alone"})

R("remainder-theorem", 1,
  r"Find the remainder when $x^3+2x-5$ is divided by $x-1$.",
  {"A": r"$-2$", "B": r"$2$", "C": r"$-5$", "D": r"$-8$"},
  "A",
  ["Eq((x**3+2*x-5).subs(x, 1), -2)",
   "Eq((x**3+2*x-5).subs(x, -1), -8)"],
  r"By the remainder theorem the remainder on division by $x-a$ is $f(a)$. "
  r"Here $a=1$: "
  r"$$f(1)=1^3+2(1)-5=1+2-5=-2.$$",
  {"B": r"got the magnitude right but lost the sign",
   "C": r"substituted $x=0$ and read off the constant term",
   "D": r"used $x=-1$; the divisor $x-1$ is zero at $x=+1$"})

# ---------------------------------------------------------------- 0.80%
R("area-between-curves", 1,
  r"Find the area of the region between $y=x+2$ and $y=x$ for $0\le x\le 3$.",
  {"A": r"$6$", "B": r"$3$", "C": r"$12$", "D": r"$2$"},
  "A",
  ["Eq(integrate((x+2)-x, (x, 0, 3)), 6)",
   "Eq(integrate(x+2, (x, 0, 3)), Rational(21,2))",
   "Eq(integrate(x, (x, 0, 3)), Rational(9,2))"],
  r"Integrate (upper $-$ lower). The lines are parallel, so the gap is the "
  r"constant $2$: "
  r"$$\int_0^3\bigl[(x+2)-x\bigr]dx=\int_0^3 2\,dx=6.$$",
  {"B": r"integrated the gap over a width of $\tfrac32$ — halved the interval",
   "C": r"added the two areas under the lines instead of subtracting",
   "D": r"gave the vertical gap between the lines, not the area"})

R("monotonicity-from-derivative", 1,
  r"For $f(x)=x^2-4x$, on which interval is $f$ increasing?",
  {"A": r"$x>2$", "B": r"$x<2$", "C": r"$x>0$", "D": r"$x>4$"},
  "A",
  ["Eq(diff(x**2-4*x, x), 2*x-4)",
   "diff(x**2-4*x, x).subs(x, 3) > 0",
   "diff(x**2-4*x, x).subs(x, 1) < 0",
   "Eq(diff(x**2-4*x, x).subs(x, 2), 0)"],
  r"$f'(x)=2x-4$, which is positive exactly when $2x-4>0$, i.e. $x>2$. "
  r"Check either side of $2$: $f'(1)=-2<0$ and $f'(3)=2>0$.",
  {"B": r"read the inequality the wrong way — that is where $f$ decreases",
   "C": r"used the root of $f$ rather than the root of $f'$",
   "D": r"solved $2x-4>4$ instead of $2x-4>0$"})

R("monotonicity-from-derivative", 3,
  r"For $f(x)=x^3-3x^2-9x+5$, on which interval is $f$ decreasing?",
  {"A": r"$-1<x<3$", "B": r"$-3<x<1$",
   "C": r"$x<-1$ or $x>3$", "D": r"$1<x<3$"},
  "A",
  ["Eq(diff(x**3-3*x**2-9*x+5, x), 3*x**2-6*x-9)",
   "Eq(simplify(3*x**2-6*x-9 - 3*(x-3)*(x+1)), 0)",
   "diff(x**3-3*x**2-9*x+5, x).subs(x, 0) < 0",
   "diff(x**3-3*x**2-9*x+5, x).subs(x, 4) > 0",
   "diff(x**3-3*x**2-9*x+5, x).subs(x, -2) > 0"],
  r"Differentiate and factorise: "
  r"$$f'(x)=3x^2-6x-9=3(x-3)(x+1).$$ This is negative between its roots, so "
  r"$f$ decreases on $-1<x<3$. Check the middle: $f'(0)=-9<0$.",
  {"B": r"factorised to $(x+3)(x-1)$ — the signs inside the brackets are swapped",
   "C": r"gave where $f$ INCREASES, i.e. outside the roots",
   "D": r"used $x=1$ (the vertex of $f'$) as an endpoint instead of the root $x=-1$"})

R("tangent-line", 1,
  r"Find the gradient of the tangent to $y=x^2$ at the point where $x=1$.",
  {"A": r"$2$", "B": r"$1$", "C": r"$\dfrac12$", "D": r"$4$"},
  "A",
  ["Eq(diff(x**2, x), 2*x)",
   "Eq(diff(x**2, x).subs(x, 1), 2)",
   "Eq((x**2).subs(x, 1), 1)"],
  r"The gradient of the tangent is the derivative at that point. "
  r"$\frac{dy}{dx}=2x$, so at $x=1$ the gradient is $2$.",
  {"B": r"gave the $y$-value $1$ instead of the gradient",
   "C": r"gave the gradient of the NORMAL, $-\tfrac1{2}$ in size",
   "D": r"substituted $x=2$ rather than $x=1$"})

R("composite-functions", 1,
  r"$f(x)=2x+1$ and $g(x)=x^2$. Find $(f\circ g)(3)$.",
  {"A": r"$19$", "B": r"$49$", "C": r"$13$", "D": r"$37$"},
  "A",
  ["Eq((2*(x**2)+1).subs(x, 3), 19)",
   "Eq(((2*x+1)**2).subs(x, 3), 49)",
   "Eq((2*x+1).subs(x, 3), 7)"],
  r"$(f\circ g)(3)=f\bigl(g(3)\bigr)$. Work inside out: $g(3)=9$, then "
  r"$f(9)=2(9)+1=19$.",
  {"B": r"computed $g\bigl(f(3)\bigr)=g(7)=49$ — the functions in the wrong order",
   "C": r"added the two outputs, $f(3)+g(3)-3$, rather than composing",
   "D": r"squared only part of the expression, using $2(3^2)+19$"})

R("increasing-decreasing-intervals", 3,
  r"On which interval is $f(x)=\dfrac{x}{x^2+1}$ increasing?",
  {"A": r"$-1<x<1$", "B": r"$x<-1$ or $x>1$", "C": r"$x>0$", "D": r"$x>1$"},
  "A",
  ["Eq(simplify(diff(x/(x**2+1), x) - (1-x**2)/(x**2+1)**2), 0)",
   "diff(x/(x**2+1), x).subs(x, 0) > 0",
   "diff(x/(x**2+1), x).subs(x, 2) < 0",
   "diff(x/(x**2+1), x).subs(x, -2) < 0",
   "Eq(diff(x/(x**2+1), x).subs(x, 1), 0)"],
  r"By the quotient rule "
  r"$$f'(x)=\frac{(x^2+1)-x(2x)}{(x^2+1)^2}=\frac{1-x^2}{(x^2+1)^2}.$$ "
  r"The denominator is always positive, so the sign is the sign of $1-x^2$, "
  r"which is positive exactly for $-1<x<1$.",
  {"B": r"gave where $1-x^2<0$ — that is where $f$ decreases",
   "C": r"assumed the function rises for all positive $x$; it turns at $x=1$",
   "D": r"used only the positive root and dropped the interval below $x=-1$"})

R("range-of-a-function", 1,
  r"Find the range of $f(x)=x^2+3$ for real $x$.",
  {"A": r"$y\ge 3$", "B": r"$y>3$", "C": r"$y\ge 0$", "D": r"$y\le 3$"},
  "A",
  ["Eq((x**2+3).subs(x, 0), 3)",
   "(x**2+3).subs(x, 5) > 3",
   "(x**2+3).subs(x, -5) > 3"],
  r"$x^2\ge 0$ for every real $x$, and $x^2=0$ is actually attained at $x=0$. "
  r"Adding $3$ gives $f(x)\ge 3$, with the value $3$ reached. So the range is "
  r"$y\ge 3$.",
  {"B": r"excluded $3$, but $f(0)=3$ so the endpoint IS attained",
   "C": r"gave the range of $x^2$ and forgot to shift it up by $3$",
   "D": r"treated the parabola as opening downwards"})

R("range-of-a-function", 3,
  r"Find the range of $f(x)=\dfrac{2x+1}{x-3}$.",
  {"A": r"all real $y$ except $y=2$", "B": r"all real $y$ except $y=3$",
   "C": r"all real $y$ except $y=-\tfrac13$", "D": r"all real $y$"},
  "A",
  ["Eq(limit((2*x+1)/(x-3), x, oo), 2)",
   "Eq(simplify((2*x+1)/(x-3) - (2 + 7/(x-3))), 0)",
   "Eq(((2*x+1)/(x-3)).subs(x, 0), Rational(-1,3))"],
  r"Rewrite by division: "
  r"$$\frac{2x+1}{x-3}=2+\frac{7}{x-3}.$$ The fraction $\tfrac{7}{x-3}$ is "
  r"never zero, so $f(x)$ is never exactly $2$; every other value is reached "
  r"by choosing $x$ suitably. The range is all reals except $2$.",
  {"B": r"$3$ is excluded from the DOMAIN, not the range",
   "C": r"that is $f(0)$, a value the function does take",
   "D": r"missed the horizontal asymptote $y=2$, which is never attained"},
  # "no solution" is a claim about an empty solution set; sympify cannot be
  # handed a list, so it is enumerated as a predicate instead.
  check=lambda: __import__("sympy").solve(
      __import__("sympy").Eq(2 * __import__("sympy").Symbol("x") + 1,
                             2 * (__import__("sympy").Symbol("x") - 3)),
      __import__("sympy").Symbol("x")) == [])
