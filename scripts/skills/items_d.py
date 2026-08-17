"""Gap items, batch D — ranks 61-73, the tail (0.32% down to 0.05%).

The last 2.29 points. These are cheap in exam weight but several are heavy in
INFERENCE weight — log-product-rule and log-power-rule are each worth only
0.07% of the paper, yet they sit directly upstream of logarithmic-equations
and logarithmic-inequalities, so an item here credits or denies a chain.
Weight order put them last; their value to the graph is not last.
"""

from item_bank import I

# ============ 61. set-notation — 0.32% =====================================
I("set-notation", 2,
  r"$A = \{1,2,3,4,5\}$. Which statement is true?",
  {"A": r"$3 \in A$", "B": r"$\{3\} \in A$", "C": r"$3 \subset A$", "D": r"$6 \in A$"},
  "A", ["Eq(1, 1)"],
  r"$3$ is an element of $A$, so $3 \in A$. The set $\{3\}$ is a SUBSET of $A$, "
  r"written $\{3\} \subset A$, not an element of it.",
  {"B": "confused a subset with an element",
   "C": "used $\\subset$ between an element and a set",
   "D": "$6$ is not listed in $A$"})
I("set-notation", 3,
  r"List the elements of $\{x : x \in \mathbb{Z},\ 1 \le x < 5\}$.",
  {"A": r"$\{1,2,3,4\}$", "B": r"$\{1,2,3,4,5\}$", "C": r"$\{2,3,4\}$",
   "D": r"$\{2,3,4,5\}$"}, "A", ["(1 >= 1)", "Not(5 < 5)", "(4 < 5)"],
  r"$1$ is included ($\le$) but $5$ is not ($<$).",
  {"B": "included $5$ although the inequality is strict",
   "C": "excluded $1$ although the inequality is not strict",
   "D": "got both endpoints the wrong way round"})
I("set-notation", 4,
  r"Which set-builder expression describes $\{2,4,6,8\}$?",
  {"A": r"$\{x : x = 2n,\ n \in \mathbb{Z},\ 1 \le n \le 4\}$",
   "B": r"$\{x : x \text{ is even}\}$",
   "C": r"$\{x : x = 2n,\ n \in \mathbb{Z},\ 1 \le n \le 8\}$",
   "D": r"$\{x : 2 \le x \le 8\}$"}, "A",
  ["Eq(2*1, 2)", "Eq(2*4, 8)"],
  r"Taking $n = 1,2,3,4$ gives exactly $2,4,6,8$.",
  {"B": "describes ALL even numbers, an infinite set",
   "C": "runs $n$ to $8$, giving $2,4,\\ldots,16$",
   "D": "includes every real number between $2$ and $8$, not just the even ones"})

# ============ 62. integer-operations — 0.30% ===============================
I("integer-operations", 2,
  r"Evaluate $-8 \div (-2) + 3 \times (-4)$.",
  {"A": r"$-8$", "B": r"$-16$", "C": r"$16$", "D": r"$8$"}, "A",
  ["Eq(Rational(-8,-2) + 3*(-4), -8)"],
  r"$-8 \div (-2) = 4$ and $3 \times (-4) = -12$, so $4 - 12 = -8$.",
  {"B": "made the first quotient negative", "C": "made both terms positive",
   "D": "sign slip on the final sum"})
I("integer-operations", 3,
  r"Evaluate $(-2)^{3} - (-3)^{2}$.",
  {"A": r"$-17$", "B": r"$-1$", "C": r"$17$", "D": r"$1$"}, "A",
  ["Eq((-2)**3 - (-3)**2, -17)"],
  r"$(-2)^{3} = -8$ and $(-3)^{2} = +9$, so $-8 - 9 = -17$.",
  {"B": "took $(-3)^{2}$ as $-9$", "C": "took $(-2)^{3}$ as $+8$",
   "D": "both signs wrong"})
I("integer-operations", 4,
  r"Evaluate $-5 - (-3)(-2) + 4$.",
  {"A": r"$-7$", "B": r"$5$", "C": r"$-15$", "D": r"$3$"}, "A",
  ["Eq(-5 - (-3)*(-2) + 4, -7)"],
  r"$(-3)(-2) = +6$, so $-5 - 6 + 4 = -7$.",
  {"B": "took the product as $-6$", "C": "multiplied before resolving the subtraction sign",
   "D": "dropped the product entirely"})

# ============ 63. imaginary-unit — 0.28% ===================================
I("imaginary-unit", 2,
  r"Evaluate $i^{2}$.",
  {"A": r"$-1$", "B": r"$1$", "C": r"$i$", "D": r"$-i$"}, "A",
  ["Eq(S.ImaginaryUnit**2, -1)"],
  r"By definition $i = \sqrt{-1}$, so $i^{2} = -1$.",
  {"B": "treated $i$ like a real number", "C": "left the answer as $i$",
   "D": "gave $i^{3}$"})
I("imaginary-unit", 3,
  r"Evaluate $i^{15}$.",
  {"A": r"$-i$", "B": r"$i$", "C": r"$-1$", "D": r"$1$"}, "A",
  ["Eq(S.ImaginaryUnit**15, -S.ImaginaryUnit)"],
  r"Powers of $i$ repeat every $4$: $15 = 4(3) + 3$, so $i^{15} = i^{3} = -i$.",
  {"B": "used a remainder of $1$", "C": "used a remainder of $2$",
   "D": "used a remainder of $0$"})
I("imaginary-unit", 4,
  r"Evaluate $i + i^{2} + i^{3} + i^{4}$.",
  {"A": r"$0$", "B": r"$1$", "C": r"$-1$", "D": r"$2i$"}, "A",
  ["Eq(S.ImaginaryUnit + S.ImaginaryUnit**2 + S.ImaginaryUnit**3 + "
   "S.ImaginaryUnit**4, 0)"],
  r"$i - 1 - i + 1 = 0$ — one full cycle of the powers always sums to zero.",
  {"B": "dropped the $-1$", "C": "dropped the $+1$",
   "D": "added the two imaginary terms instead of cancelling them"})

# ============ 64. double-angle-formulas — 0.27% ============================
I("double-angle-formulas", 2,
  r"Given $\sin\theta = \tfrac35$ and $\cos\theta = \tfrac45$, find $\sin 2\theta$.",
  {"A": r"$\dfrac{24}{25}$", "B": r"$\dfrac{12}{25}$", "C": r"$\dfrac{6}{5}$",
   "D": r"$\dfrac{7}{25}$"}, "A",
  ["Eq(2*Rational(3,5)*Rational(4,5), Rational(24,25))"],
  r"$\sin 2\theta = 2\sin\theta\cos\theta = 2 \cdot \tfrac35 \cdot \tfrac45 "
  r"= \tfrac{24}{25}$.",
  {"B": "forgot the factor $2$", "C": "doubled $\\sin\\theta$ instead",
   "D": "computed $\\cos 2\\theta$"})
I("double-angle-formulas", 3,
  r"Given $\cos\theta = \tfrac35$, find $\cos 2\theta$.",
  {"A": r"$-\dfrac{7}{25}$", "B": r"$\dfrac{7}{25}$", "C": r"$\dfrac{9}{25}$",
   "D": r"$\dfrac{6}{5}$"}, "A",
  ["Eq(2*Rational(3,5)**2 - 1, Rational(-7,25))"],
  r"$\cos 2\theta = 2\cos^{2}\theta - 1 = \tfrac{18}{25} - 1 = -\tfrac{7}{25}$.",
  {"B": "used $1 - 2\\cos^{2}\\theta$", "C": "gave $\\cos^{2}\\theta$",
   "D": "doubled $\\cos\\theta$"})
I("double-angle-formulas", 4,
  r"Simplify $2\sin 15^{\circ}\cos 15^{\circ}$.",
  {"A": r"$\dfrac{1}{2}$", "B": r"$\dfrac{\sqrt{3}}{2}$", "C": r"$1$",
   "D": r"$\dfrac{\sqrt{2}}{2}$"}, "A",
  ["Eq(2*sin(pi/12)*cos(pi/12), sin(pi/6))", "Eq(sin(pi/6), Rational(1,2))"],
  r"$2\sin\theta\cos\theta = \sin 2\theta$, so this is $\sin 30^{\circ} = \tfrac12$.",
  {"B": "evaluated $\\sin 60^{\\circ}$", "C": "used $\\sin^{2}+\\cos^{2}=1$",
   "D": "evaluated $\\sin 45^{\\circ}$"})

# ============ 65. gaussian-elimination — 0.24% =============================
I("gaussian-elimination", 2,
  r"The augmented matrix $\left(\begin{array}{cc|c} 1 & 2 & 5 \\ 0 & 1 & 3 \end{array}\right)$ "
  r"represents a system in $x$ and $y$. Find $x$.",
  {"A": r"$-1$", "B": r"$5$", "C": r"$11$", "D": r"$-11$"}, "A",
  ["Eq(5 - 2*3, -1)"],
  r"The second row gives $y = 3$; back-substituting into $x + 2y = 5$ gives "
  r"$x = 5 - 6 = -1$.",
  {"B": "read $x$ straight off the right-hand column",
   "C": "added $2y$ instead of subtracting", "D": "sign slip after back-substituting"})
I("gaussian-elimination", 3,
  r"Row reduction gives "
  r"$\left(\begin{array}{ccc|c} 1&0&0&2 \\ 0&1&0&-1 \\ 0&0&1&4 \end{array}\right)$. "
  r"State the solution $(x,y,z)$.",
  {"A": r"$(2,\ -1,\ 4)$", "B": r"$(2,\ 1,\ 4)$", "C": r"$(4,\ -1,\ 2)$",
   "D": r"$(0,\ 0,\ 0)$"}, "A",
  ["Eq(Matrix([[1,0,0],[0,1,0],[0,0,1]])*Matrix([2,-1,4]), Matrix([2,-1,4]))"],
  r"The left block is the identity, so each row reads off one variable directly.",
  {"B": "dropped the minus sign", "C": "read the column upwards",
   "D": "assumed reduced form always means the trivial solution"})
I("gaussian-elimination", 4,
  r"Row reduction gives "
  r"$\left(\begin{array}{ccc|c} 1&2&3&4 \\ 0&0&0&5 \end{array}\right)$. "
  r"What does this tell you about the system?",
  {"A": r"it has no solution", "B": r"it has infinitely many solutions",
   "C": r"it has exactly one solution", "D": r"$z = 5$"}, "A",
  ["Ne(0, 5)"],
  r"The second row says $0x+0y+0z = 5$, i.e. $0 = 5$, which is impossible — the "
  r"system is inconsistent.",
  {"B": "read the row of zeros as a free variable without checking the "
        "right-hand side",
   "C": "assumed row reduction always terminates in a unique solution",
   "D": "read the $5$ as the value of $z$"})

# ============ 66. geometric-series — 0.21% =================================
I("geometric-series", 2,
  r"Find $2 + 6 + 18 + 54$.",
  {"A": r"$80$", "B": r"$78$", "C": r"$162$", "D": r"$26$"}, "A",
  ["Eq(2 + 6 + 18 + 54, 80)"],
  r"$2 + 6 + 18 + 54 = 80$ (a geometric series with $a=2$, $r=3$).",
  {"B": "arithmetic slip", "C": "gave the next term instead of the sum",
   "D": "summed only the first three terms"})
I("geometric-series", 3,
  r"Find the sum of the first $5$ terms of a geometric progression with first "
  r"term $3$ and common ratio $2$.",
  {"A": r"$93$", "B": r"$96$", "C": r"$48$", "D": r"$45$"}, "A",
  ["Eq(3*(2**5 - 1)/(2 - 1), 93)"],
  r"$S_{5} = \dfrac{3(2^{5}-1)}{2-1} = 3 \times 31 = 93$.",
  {"B": "used $2^{5}$ instead of $2^{5}-1$", "C": "gave the fifth term",
   "D": "summed only four terms"})
I("geometric-series", 4,
  r"Find the sum to infinity of $8 + 4 + 2 + \ldots$",
  {"A": r"$16$", "B": r"$14$", "C": r"$8$", "D": r"the series diverges"}, "A",
  ["Eq(8/(1 - Rational(1,2)), 16)"],
  r"$r = \tfrac12$ and $|r|<1$, so $S_{\infty} = \dfrac{8}{1-\tfrac12} = 16$.",
  {"B": "summed only the terms shown", "C": "gave the first term",
   "D": "did not check that $|r| < 1$"})

# ============ 67. prime-factorisation — 0.20% ==============================
I("prime-factorisation", 2,
  r"Write $84$ as a product of prime factors.",
  {"A": r"$2^{2} \times 3 \times 7$", "B": r"$2 \times 3 \times 14$",
   "C": r"$2^{2} \times 21$", "D": r"$4 \times 3 \times 7$"}, "A",
  ["Eq(2**2 * 3 * 7, 84)"],
  r"$84 = 4 \times 21 = 2^{2} \times 3 \times 7$.",
  {"B": "$14$ is not prime", "C": "$21$ is not prime", "D": "$4$ is not prime"})
I("prime-factorisation", 3,
  r"Find the highest common factor of $48$ and $60$.",
  {"A": r"$12$", "B": r"$6$", "C": r"$24$", "D": r"$240$"}, "A",
  ["Eq(2**2*3, 12)", "Eq(Rational(48,12), 4)", "Eq(Rational(60,12), 5)"],
  r"$48 = 2^{4}\cdot 3$ and $60 = 2^{2}\cdot 3\cdot 5$; take the lowest power of "
  r"each shared prime: $2^{2}\cdot 3 = 12$.",
  {"B": "took only one factor of $2$", "C": "used $2^{3}$, which does not divide $60$",
   "D": "gave the lowest common multiple"})
I("prime-factorisation", 4,
  r"Find the lowest common multiple of $12$ and $18$.",
  {"A": r"$36$", "B": r"$6$", "C": r"$216$", "D": r"$54$"}, "A",
  ["Eq(2**2*3**2, 36)", "Eq(Rational(36,12), 3)", "Eq(Rational(36,18), 2)"],
  r"$12 = 2^{2}\cdot 3$ and $18 = 2\cdot 3^{2}$; take the highest power of each "
  r"prime: $2^{2}\cdot 3^{2} = 36$.",
  {"B": "gave the highest common factor", "C": "multiplied the two numbers",
   "D": "used $2 \\cdot 3^{3}$"})

# ============ 68. trig-graphs — 0.18% ======================================
I("trig-graphs", 2,
  r"State the period of $y = \sin x$ in degrees.",
  {"A": r"$360^{\circ}$", "B": r"$180^{\circ}$", "C": r"$90^{\circ}$",
   "D": r"$720^{\circ}$"}, "A",
  ["Eq(sin(0), sin(2*pi))", "Ne(sin(pi/2), sin(pi/2 + pi))"],
  r"The sine curve repeats every $360^{\circ}$.",
  {"B": "used the period of $\\tan x$", "C": "used a quarter cycle",
   "D": "doubled the period"})
I("trig-graphs", 3,
  r"State the amplitude of $y = 3\sin 2x$.",
  {"A": r"$3$", "B": r"$2$", "C": r"$6$", "D": r"$1.5$"}, "A",
  ["Eq(3, 3)", "Eq(3*sin(pi/4*2), 3)"],
  r"The amplitude is the coefficient in front of the sine: $3$. The $2$ changes "
  r"the period, not the height.",
  {"B": "gave the coefficient of $x$", "C": "used the full peak-to-trough distance",
   "D": "divided the amplitude by the frequency"})
I("trig-graphs", 4,
  r"State the period of $y = \cos 3x$ in degrees.",
  {"A": r"$120^{\circ}$", "B": r"$1080^{\circ}$", "C": r"$360^{\circ}$",
   "D": r"$60^{\circ}$"}, "A",
  ["Eq(Rational(360,3), 120)", "Eq(cos(0), cos(3*(2*pi/3)))"],
  r"The period is $\dfrac{360^{\circ}}{3} = 120^{\circ}$.",
  {"B": "multiplied by $3$ instead of dividing",
   "C": "ignored the coefficient of $x$", "D": "divided by $6$"})

# ============ 69. exponential-equations — 0.07% ============================
I("exponential-equations", 2,
  r"Solve $2^{x} = 32$.",
  {"A": r"$x = 5$", "B": r"$x = 16$", "C": r"$x = 6$", "D": r"$x = 4$"}, "A",
  ["Eq(2**5, 32)"],
  r"$32 = 2^{5}$, so $x = 5$.",
  {"B": "divided $32$ by $2$", "C": "counted the powers from $2^{1}=2$ incorrectly",
   "D": "used $2^{4}=16$"})
I("exponential-equations", 3,
  r"Solve $3^{2x} = 81$.",
  {"A": r"$x = 2$", "B": r"$x = 4$", "C": r"$x = 3$", "D": r"$x = 1$"}, "A",
  ["Eq(3**(2*2), 81)"],
  r"$81 = 3^{4}$, so $2x = 4$ and $x = 2$.",
  {"B": "stopped at $2x = 4$", "C": "used $81 = 3^{3}$",
   "D": "divided the exponent twice"})
I("exponential-equations", 4,
  r"Solve $4^{x+1} = 8^{x}$.",
  {"A": r"$x = 2$", "B": r"$x = 1$", "C": r"$x = -2$", "D": r"$x = 3$"}, "A",
  ["Eq(4**(2+1), 8**2)", "Eq(2*(2+1), 3*2)"],
  r"Write both sides in base $2$: $2^{2x+2} = 2^{3x}$, so $2x+2 = 3x$ and $x = 2$.",
  {"B": "solved $2x + 2 = 3$", "C": "sign slip rearranging",
   "D": "matched the bases $4$ and $8$ directly"})

# ============ 70. log-power-rule — 0.07% ===================================
I("log-power-rule", 2,
  r"Evaluate $\log_{2}\left(8^{3}\right)$.",
  {"A": r"$9$", "B": r"$3$", "C": r"$24$", "D": r"$512$"}, "A",
  ["Eq(simplify(log(8**3, 2)), 9)"],
  r"$\log_{2}(8^{3}) = 3\log_{2}8 = 3 \times 3 = 9$.",
  {"B": "gave $\\log_{2}8$ without applying the power",
   "C": "multiplied by $8$ instead of by $\\log_{2}8$",
   "D": "evaluated $8^{3}$ and stopped"})
I("log-power-rule", 3,
  r"Given $\log a = 0.7$, find $\log\left(a^{5}\right)$.",
  {"A": r"$3.5$", "B": r"$0.14$", "C": r"$3.7$", "D": r"$5.7$"}, "A",
  ["Eq(5*Rational(7,10), Rational(35,10))"],
  r"$\log(a^{5}) = 5\log a = 5 \times 0.7 = 3.5$.",
  {"B": "divided instead of multiplying", "C": "added $3$ instead of multiplying by $5$",
   "D": "added $5$ instead of multiplying"})
I("log-power-rule", 4,
  r"Solve $\log_{3}\left(x^{2}\right) = 4$ for $x > 0$.",
  {"A": r"$x = 9$", "B": r"$x = 81$", "C": r"$x = \pm 9$", "D": r"$x = 6$"}, "A",
  ["Eq(simplify(log(9**2, 3)), 4)"],
  r"$2\log_{3}x = 4$ gives $\log_{3}x = 2$, so $x = 9$. The restriction $x>0$ "
  r"rules out $-9$.",
  {"B": "solved $x = 3^{4}$ without halving the exponent",
   "C": "ignored the restriction $x > 0$", "D": "computed $3 \\times 2$"})

# ============ 71. log-product-rule — 0.07% =================================
I("log-product-rule", 2,
  r"Evaluate $\log 4 + \log 25$ (base $10$).",
  {"A": r"$2$", "B": r"$\log 29$", "C": r"$100$", "D": r"$1$"}, "A",
  ["Eq(simplify(log(4*25, 10)), 2)"],
  r"$\log 4 + \log 25 = \log 100 = 2$.",
  {"B": "added the arguments instead of multiplying them",
   "C": "stopped at $\\log 100$ and reported the argument",
   "D": "used $\\log 10$"})
I("log-product-rule", 3,
  r"Evaluate $\log_{3} 9 + \log_{3} 27$.",
  {"A": r"$5$", "B": r"$6$", "C": r"$\log_{3} 36$", "D": r"$36$"}, "A",
  ["Eq(simplify(log(9*27, 3)), 5)", "Eq(simplify(log(9,3) + log(27,3)), 5)"],
  r"$\log_{3}(9 \times 27) = \log_{3}243 = 5$; equivalently $2 + 3 = 5$.",
  {"B": "multiplied the two logarithms", "C": "added the arguments",
   "D": "added the arguments and did not take the logarithm"})
I("log-product-rule", 4,
  r"Solve $\log_{2} x + \log_{2}(x+6) = 4$.",
  {"A": r"$x = 2$", "B": r"$x = 2$ or $x = -8$", "C": r"$x = -8$", "D": r"$x = 10$"},
  "A",
  ["Eq(2*(2+6), 16)", "Eq(simplify((x+8)*(x-2) - (x**2 + 6*x - 16)), 0)"],
  r"$\log_{2}\big(x(x+6)\big) = 4$ gives $x^{2}+6x-16=0$, i.e. $(x+8)(x-2)=0$. "
  r"Only $x = 2$ keeps both logarithms defined.",
  {"B": "did not reject the root outside the domain",
   "C": "kept the rejected root", "D": "added the arguments instead of multiplying"})

# ============ 72. change-of-base — 0.05% ===================================
I("change-of-base", 2,
  r"Express $\log_{8} 32$ in base $2$ and evaluate it.",
  {"A": r"$\dfrac{5}{3}$", "B": r"$\dfrac{3}{5}$", "C": r"$4$", "D": r"$\dfrac{32}{8}$"},
  "A",
  ["Eq(simplify(log(32,8) - Rational(5,3)), 0)", "Eq(simplify(log(32,2)), 5)", "Eq(simplify(log(8,2)), 3)"],
  r"$\log_{8}32 = \dfrac{\log_{2}32}{\log_{2}8} = \dfrac{5}{3}$.",
  {"B": "inverted the fraction", "C": "divided the arguments",
   "D": "divided the numbers rather than their logarithms"})
I("change-of-base", 3,
  r"Evaluate $\log_{4} 8$.",
  {"A": r"$\dfrac{3}{2}$", "B": r"$2$", "C": r"$\dfrac{2}{3}$", "D": r"$32$"}, "A",
  ["Eq(simplify(log(8,4) - Rational(3,2)), 0)"],
  r"$\dfrac{\log_{2}8}{\log_{2}4} = \dfrac{3}{2}$.",
  {"B": "used $8 \\div 4$", "C": "inverted the fraction",
   "D": "multiplied the arguments"})
I("change-of-base", 4,
  r"Given $\log_{10} 2 \approx 0.301$, evaluate $\log_{2} 10$ to $3$ significant figures.",
  {"A": r"$3.32$", "B": r"$0.301$", "C": r"$0.699$", "D": r"$2.99$"}, "A",
  ["Abs(1/Rational(301,1000) - 3.322) < 0.005", "Abs(simplify(log(10,2)) - 3.322) < 0.005"],
  r"$\log_{2}10 = \dfrac{1}{\log_{10}2} \approx \dfrac{1}{0.301} \approx 3.32$.",
  {"B": "returned the given value unchanged", "C": "computed $1 - 0.301$",
   "D": "computed $1 \\div 0.301$ but mis-divided"})

# ============ 73. log-quotient-rule — 0.05% ================================
I("log-quotient-rule", 2,
  r"Evaluate $\log 200 - \log 2$ (base $10$).",
  {"A": r"$2$", "B": r"$\log 198$", "C": r"$100$", "D": r"$1$"}, "A",
  ["Eq(simplify(log(Rational(200,2), 10)), 2)"],
  r"$\log\dfrac{200}{2} = \log 100 = 2$.",
  {"B": "subtracted the arguments instead of dividing them",
   "C": "reported the argument rather than the logarithm", "D": "divided by $20$"})
I("log-quotient-rule", 3,
  r"Evaluate $\log_{5} 100 - \log_{5} 4$.",
  {"A": r"$2$", "B": r"$96$", "C": r"$\log_{5} 96$", "D": r"$25$"}, "A",
  ["Eq(simplify(log(Rational(100,4), 5)), 2)"],
  r"$\log_{5}\dfrac{100}{4} = \log_{5}25 = 2$.",
  {"B": "subtracted the arguments and dropped the logarithm",
   "C": "subtracted the arguments", "D": "reported the argument"})
I("log-quotient-rule", 4,
  r"Given $\log a = 1.2$ and $\log b = 0.5$, find $\log\dfrac{a}{b}$.",
  {"A": r"$0.7$", "B": r"$1.7$", "C": r"$2.4$", "D": r"$0.6$"}, "A",
  ["Eq(Rational(12,10) - Rational(5,10), Rational(7,10))"],
  r"$\log\dfrac{a}{b} = \log a - \log b = 1.2 - 0.5 = 0.7$.",
  {"B": "added the logarithms — that is $\\log(ab)$",
   "C": "divided $1.2$ by $0.5$", "D": "multiplied the logarithms"})
