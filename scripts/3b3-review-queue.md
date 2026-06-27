# Phase 3b.3 Manual Spot-Check Review Queue

Generated 2026-05-13 after Phase 3b.2 classification pass (commit `092a79f`). 115 unique rows for review across 4 sections.

## Workflow

Review in chunks of 25 rows. After each chunk, mark decisions inline and send back. The assistant will apply changes to `scripts/skill-tag-classification.csv` and pull the next chunk.

For each row, choose ONE of:
- **`approve`** — current classification stays as-is
- **`change to: <new_tag>`** — re-tag (and optionally adjust difficulty_tier/confidence)
- **`flag escalation`** — needs broader discussion (new tag candidate, taxonomy gap, etc.)

## Watchouts to call out

Three specific patterns to look for during review:

**1. 3D vs 2D coordinate geometry split.** Three rows were force-fit from 3D analytic geometry (parametric lines, planes from points/normals) to `coordinate_geometry` because the taxonomy's coordinate_geometry scope is 2D-focused. If you judge these substantively different from 2D coordinate problems (distance/midpoint/slope/line-equation), they may need to split out as `solid_geometry_analytic` (or similar). Watch for:
- Test-2025D-Q8 (line ∩ plane in ℝ³)
- Test-6A-Q34 (plane equation from point + normal)
- Test-6B-Q34 (plane equation from 3 points)

**2. linear_inequality cohort honesty.** `linear_inequality` ended up at only 2 rows (taxonomy estimate was ~11). Most 'тэнцэтгэл биш' questions routed to `quadratic_inequality` because that tag's scope explicitly covers absolute-value + rational inequalities. During the auto-trigger sample for `quadratic_inequality`, verify the pool doesn't contain pure linear inequalities that should have been routed to linear_inequality.

**3. Parity disposition decision.** Two rows currently sit at `needs_human_review` (Test-1A-Q22, Test-1B-Q22). Final disposition options:
- **(a) Keep as needs_human_review** — punt to 3b.4+ when textbook extraction may surface more parity questions.
- **(b) Force-fit to exponent_rules** — the parity argument hinges on (odd)^n parity preservation; acceptable noise at confidence ≤0.50.
- **(c) Add 52nd tag `parity_arithmetic`** — only 2 questions currently; would be sparse.

---

## Section index

- **needs_human_review (parity disposition)**: 2 rows
- **new tag (basic_probability + number_theory)**: 17 rows
- **low-confidence (<0.70)**: 43 rows
- **auto-trigger sample (5 random per high-loop-impact tag)**: 53 rows

---

## Section: needs_human_review (parity disposition)  (2 rows)

### 1. Test-1A-Q22 — *parity disposition*
**Body:** $a$ нь тэгш тоо бөгөөд $[(3a+7)^{30} - (9a+4)^{100}](7a-9) = b$ бол дараах өгүүлбэрүүдээс аль нь $b$-ийн хувьд үнэн бэ?
**Options:** **A)** $b$ сондгой  **B)** $b$ тэгш  **C)** $b$ заавал 4-д хуваагдана  **D)** $b$ тэгш ч, сондгой ч байж болно  **E)** $b$ тодорхойлох боломжгүй
**Correct answer:** A
**Current classification:** skill_tag=`needs_human_review` · difficulty=`medium` · confidence=`0.3` · classifier=`in-chat`
**Rationale:** Parity reasoning: a even ⇒ b odd via (odd)^n=odd, (even)^n=even, odd−even=odd. Parity is the core skill, not exponent computation — exponent_rules drill cohort wouldn't teach this. Flag for 3b.3 review; may justify parity_arithmetic tag if Phase 2b textbook extraction surfaces more such questions.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 2. Test-1B-Q22 — *parity disposition*
**Body:** $a$ нь тэгш тоо бөгөөд $[(5a + 7)^{20} - (3a + 4)^{300}](8a - 101) = b$ бол дараах өгүүлбэрүүдээс аль нь $b$-ийн хувьд үнэн бэ?
**Options:** **A)** $b$ сондгой  **B)** $b$ тэгш  **C)** $b$ нь $4$-д хуваагдана  **D)** $b$ тэгш ч, сондгой ч байж болно  **E)** $b$ тодорхойлох боломжгүй
**Correct answer:** A
**Current classification:** skill_tag=`needs_human_review` · difficulty=`medium` · confidence=`0.3` · classifier=`in-chat`
**Rationale:** Variant of Q1A-Q22: parity reasoning with different powers. Same flag rationale — parity is the core skill, not exponent computation.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

---

## Section: new tag (basic_probability + number_theory)  (17 rows)

### 3. Test-2021D-Q4 — *basic_probability*
**Body:** $P(A) = \frac{3}{4}$ бол $A$ үзэгдлийн эсрэг үзэгдлийн магадлалыг олоорой.
**Options:** **A)** $-\frac{3}{4}$  **B)** $\frac{1}{4}$  **C)** $1$  **D)** $0$  **E)** $\frac{4}{3}$
**Correct answer:** B
**Current classification:** skill_tag=`basic_probability` · difficulty=`easy` · confidence=`0.9` · classifier=`in-chat`
**Rationale:** P(A')=1-P(A)=1/4. Complement of single event.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 4. Test-1A-Q16 — *basic_probability*
**Body:** 1-ээс 20 хүртэлх тооноос нэг тоог санамсаргүйгээр авахад тэр тоо анхны тоо байх магадлалыг ол.
**Options:** **A)** $\frac{2}{5}$  **B)** $\frac{9}{20}$  **C)** $\frac{4}{5}$  **D)** $\frac{3}{4}$  **E)** $\frac{5}{6}$
**Correct answer:** A
**Current classification:** skill_tag=`basic_probability` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** P(prime in 1-20) = 8/20 — single-event probability via favorable/total counting. New basic_probability tag added 2026-05-13.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 5. Test-1B-Q16 — *basic_probability*
**Body:** $1$-ээс $20$ хүртэлх тооноос нэг тоог санамсаргүйгээр авахад тэр тоо зохиомол тоо байх магадлалыг ол.
**Options:** **A)** $\frac{11}{20}$  **B)** $\frac{4}{5}$  **C)** $\frac{3}{5}$  **D)** $\frac{3}{4}$  **E)** $\frac{9}{20}$
**Correct answer:** A
**Current classification:** skill_tag=`basic_probability` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** P(composite in 1-20). Single-event probability via favorable/total counting.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 6. Test-2A-Q26 — *basic_probability*
**Body:** Анги 14 хүү, 7 охинтой. Санамсаргүйгээр 2 сурагч сонгоход 1 хүү, 1 охин сонгогдох магадлалыг ол.
**Options:** **A)** $\frac{1}{2}$  **B)** $\frac{7}{30}$  **C)** $\frac{7}{15}$  **D)** $\frac{2}{9}$  **E)** $\frac{4}{9}$
**Correct answer:** C
**Current classification:** skill_tag=`basic_probability` · difficulty=`medium` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Combination probability.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 7. Test-2B-Q26 — *basic_probability*
**Body:** Анги 8 охин, 13 хүүтэй. Санамсаргүйгээр 3 сурагч сонгоход 1 охин, 2 хүү сонгогдох магадлалыг ол.
**Options:** **A)** $\frac{312}{665}$  **B)** $\frac{1}{2}$  **C)** $\frac{312}{585}$  **D)** $\frac{2}{3}$  **E)** $\frac{301}{515}$
**Correct answer:** A
**Current classification:** skill_tag=`basic_probability` · difficulty=`medium` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Combination probability.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 8. Test-4A-Q25 — *basic_probability*
**Body:** Хоёр оронтой тооны цифрүүдийн үржвэр 12 байх магадлалыг ол.
**Options:** **A)** $\frac{1}{45}$  **B)** $\frac{2}{45}$  **C)** $\frac{1}{15}$  **D)** $\frac{4}{45}$  **E)** $\frac{1}{9}$
**Correct answer:** B
**Current classification:** skill_tag=`basic_probability` · difficulty=`medium` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Digit product probability.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 9. Test-4B-Q25 — *basic_probability*
**Body:** Хоёр оронтой тооны цифрүүдийн үржвэр 6 байх магадлалыг ол.
**Options:** **A)** $\frac{1}{45}$  **B)** $\frac{2}{45}$  **C)** $\frac{1}{15}$  **D)** $\frac{4}{45}$  **E)** $\frac{1}{9}$
**Correct answer:** B
**Current classification:** skill_tag=`basic_probability` · difficulty=`medium` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Digit product variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 10. Test-5A-Q23 — *basic_probability*
**Body:** 10 талт шоог орхиход анхны тоо буух магадлалыг ол.
**Options:** **A)** $\frac{1}{2}$  **B)** $\frac{3}{10}$  **C)** $\frac{3}{5}$  **D)** $\frac{7}{10}$  **E)** $\frac{2}{5}$
**Correct answer:** E
**Current classification:** skill_tag=`basic_probability` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** P(prime on d10)=4/10=2/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 11. Test-5B-Q23 — *basic_probability*
**Body:** 12 талст шоог орхиход анхны тоо буух магадлалыг ол.
**Options:** **A)** $\frac{1}{2}$  **B)** $\frac{7}{12}$  **C)** $\frac{3}{4}$  **D)** $\frac{5}{12}$  **E)** $\frac{1}{3}$
**Correct answer:** D
**Current classification:** skill_tag=`basic_probability` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** P(prime on d12).
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 12. Test-2A-Q14 — *number_theory*
**Body:** Бүтэн куб болдог гурван оронтой хэдэн тоо бий вэ?
**Options:** **A)** $5$  **B)** $6$  **C)** $7$  **D)** $8$  **E)** $9$
**Correct answer:** A
**Current classification:** skill_tag=`number_theory` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Count 3-digit perfect cubes: 5³=125 through 9³=729 ⇒ 5 numbers. Reclassified from number_representation to number_theory (new tag added 2026-05-13).
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 13. Test-2B-Q14 — *number_theory*
**Body:** Бүтэн квадрат болдог гурван оронтой хэдэн тоо бий вэ?
**Options:** **A)** $31$  **B)** $21$  **C)** $22$  **D)** $23$  **E)** $20$
**Correct answer:** C
**Current classification:** skill_tag=`number_theory` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Count 3-digit perfect squares: 10² through 31² ⇒ 22 numbers. Reclassified from number_representation to number_theory.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 14. Test-4A-Q7 — *number_theory*
**Body:** Ямар $n \in \mathbb{N}$ хувьд $\frac{2n^2 + n + 11}{n + 2}$ илэрхийлэл натурал тоо байх вэ?
**Options:** **A)** $-1$  **B)** $-19$  **C)** $15$  **D)** $13$  **E)** $17$
**Correct answer:** C
**Current classification:** skill_tag=`number_theory` · difficulty=`hard` · confidence=`0.9` · classifier=`in-chat`
**Rationale:** (2n²+n+11)/(n+2) natural ⇒ (n+2)|17 ⇒ n=15. Integer-divisibility reasoning is the binding skill (polynomial division is the technique to expose it). Reclassified from polynomial_remainder to number_theory per new tag scope: 'distinct from polynomial_remainder (polynomial not integer divisibility)'.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 15. Test-4A-Q12 — *number_theory*
**Body:** Үржвэр нь 864 бөгөөд ХИЕХ нь 6 байх хоёр тоог ол.
**Options:** **A)** $24; 36$  **B)** $144; 12$  **C)** $12; 72$  **D)** $13; 288$  **E)** $18; 48$
**Correct answer:** E
**Current classification:** skill_tag=`number_theory` · difficulty=`medium` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Product=864, GCD=6 ⇒ coprime pair mn=24, (m,n)=(3,8), numbers (18,48). GCD/LCM pair enumeration. Reclassified from number_representation.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 16. Test-4B-Q7 — *number_theory*
**Body:** Ямар $n \in \mathbb{N}$ хувьд $\frac{3n^2 + 7n - 11}{n + 2}$ илэрхийлэл натурал тоо байх вэ?
**Options:** **A)** $-1$  **B)** $-15$  **C)** $7$  **D)** $13$  **E)** $11$
**Correct answer:** E
**Current classification:** skill_tag=`number_theory` · difficulty=`hard` · confidence=`0.9` · classifier=`in-chat`
**Rationale:** (3n²+7n-11)/(n+2) natural ⇒ (n+2)|13 ⇒ n=11. Integer-divisibility reasoning. number_theory (new tag).
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 17. Test-4B-Q12 — *number_theory*
**Body:** Үржвэр нь 4800 бөгөөд ХИЕХ нь 20 байх хоёр тоог ол.
**Options:** **A)** $60; 80$  **B)** $40; 120$  **C)** $30; 160$  **D)** $5; 980$  **E)** $48; 100$
**Correct answer:** A
**Current classification:** skill_tag=`number_theory` · difficulty=`medium` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Product=4800, GCD=20 ⇒ coprime pair mn=12, (m,n)=(3,4), numbers (60,80). Reclassified from number_representation.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 18. Test-5A-Q8 — *number_theory*
**Body:** $k!$ нь 100-д хуваагдахгүй хэдэн натурал $k$ тоо байх вэ?
**Options:** **A)** $19$  **B)** $4$  **C)** $14$  **D)** $9$  **E)** $15$
**Correct answer:** D
**Current classification:** skill_tag=`number_theory` · difficulty=`hard` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** k! divisible by 100 requires ≥2 factors of 5. Count=9 for k=1..9. Factorial divisibility.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 19. Test-5B-Q8 — *number_theory*
**Body:** $k!$ нь 25-д хуваагдахгүй хэдэн натурал $k$ тоо байх вэ?
**Options:** **A)** $19$  **B)** $4$  **C)** $14$  **D)** $9$  **E)** $15$
**Correct answer:** D
**Current classification:** skill_tag=`number_theory` · difficulty=`hard` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Factorial divisibility by 25.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

---

## Section: low-confidence (<0.70)  (43 rows)

### 20. Test-2021D-Q22 — *conf 0.55*
**Body:** $|2x - 1| + |x + 5| = 10$ тэгшитгэлийн шийдийг олоорой.
**Options:** **A)** $\left\{-4,\ 2,\ -\frac{14}{3}\right\}$  **B)** $\{-4,\ 2\}$  **C)** $\left\{-4,\ -\frac{14}{3}\right\}$  **D)** $\left\{2,\ -\frac{14}{3}\right\}$  **E)** $\{2\}$
**Correct answer:** B
**Current classification:** skill_tag=`linear_equation` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** |2x-1|+|x+5|=10 via case analysis; each case is linear. No abs-value-equation tag; force-fit. SURVEILLANCE: abs-value equation pattern (1 of 5 needed).
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 21. Test-2022A-Q11 — *conf 0.6*
**Body:** $(3x + 9) \cdot \sqrt{x - 2} = 0$ тэгшитгэл бодоорой.
**Options:** **A)** $-2,\ 3$  **B)** $-3,\ 2$  **C)** $2$  **D)** $-3$  **E)** $-2,\ -3$
**Correct answer:** C
**Current classification:** skill_tag=`radical_expression` · difficulty=`easy` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Radical equation with domain check. Force-fit; partial transfer.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 22. Test-2023A-Q36 — *conf 0.65*
**Body:** $A = \begin{pmatrix}3 & b \\ c & -1\end{pmatrix}$ матрицын тодорхойлогч нь 1 бол $A^3 = pA + qE$ байх $(p,\ q)$ тоог олоорой. $E = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}$ нэгж матриц.
**Options:** **A)** $p=3,\ q=-2$  **B)** $p=3,\ q=-1$  **C)** $p=-3,\ q=1$  **D)** $p=-3,\ q=2$  **E)** $p=3,\ q=1$
**Correct answer:** A
**Current classification:** skill_tag=`matrix_operation` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Cayley-Hamilton: A²=2A-E ⇒ A³=3A-2E. matrix_operation as umbrella; rare topic.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 23. Test-2023B-Q19 — *conf 0.6*
**Body:** Тэнцүү тоог олж, харгалзуулаарай. I. $2^{-3}$\quad II. $9^x = 27$ бол $x = ?$\quad III. $\log_8 4$\quad a. $\dfrac{3}{2}$\quad b. $\dfrac{1}{8}$\quad c. $\dfrac{2}{3}$
**Options:** **A)** Ic, IIb, IIIa  **B)** Ic, IIa, IIIb  **C)** Ib, IIc, IIIa  **D)** Ia, IIb, IIIc  **E)** Ib, IIa, IIIc
**Correct answer:** E
**Current classification:** skill_tag=`exponent_rules` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Matching exponent/log values. Force-fit; SURVEILLANCE for multi-skill matching pattern.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 24. Test-2023C-Q19 — *conf 0.6*
**Body:** Тэнцүү тоог олж, харгалзуулаарай. I. $3^{-2}$\quad II. $27^x = 9$ бол $x = ?$\quad III. $\log_4 8$\quad a. $\dfrac{3}{2}$\quad b. $\dfrac{2}{3}$\quad c. $\dfrac{1}{9}$
**Options:** **A)** Ic, IIb, IIIa  **B)** Ic, IIa, IIIb  **C)** Ib, IIc, IIIa  **D)** Ia, IIb, IIIc  **E)** Ib, IIa, IIIc
**Correct answer:** A
**Current classification:** skill_tag=`exponent_rules` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Variant of 2023B-Q19.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 25. Test-2023D-Q19 — *conf 0.6*
**Body:** Тэнцүү тоог олж, харгалзуулаарай. I. $2^{-3}$\quad II. $9^x = 27$ бол $x = ?$\quad III. $\log_8 4$\quad a. $\dfrac{3}{2}$\quad b. $\dfrac{1}{8}$\quad c. $\dfrac{2}{3}$
**Options:** **A)** Ib, IIc, IIIa  **B)** Ic, IIa, IIIb  **C)** Ib, IIa, IIIc  **D)** Ia, IIb, IIIc  **E)** Ic, IIb, IIIa
**Correct answer:** C
**Current classification:** skill_tag=`exponent_rules` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Variant of 2023B-Q19.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 26. Test-2025A-Q21 — *conf 0.65*
**Body:** Дараах нийлбэрийг тооцоолоорой. $\displaystyle\sum_{k=1}^{2025}(k^2+1) - \sum_{k=5}^{2025}(k^2+1)$
**Options:** **A)** $121$  **B)** $30$  **C)** $14$  **D)** $101$  **E)** $34$
**Correct answer:** E
**Current classification:** skill_tag=`progression` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Sum cancellation. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 27. Test-2025B-Q21 — *conf 0.65*
**Body:** Дараах нийлбэрийг тооцоолоорой. $\displaystyle\sum_{k=1}^{2025}(k^2-1) - \sum_{k=5}^{2025}(k^2-1)$
**Options:** **A)** $30$  **B)** $26$  **C)** $6$  **D)** $99$  **E)** $100$
**Correct answer:** B
**Current classification:** skill_tag=`progression` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Sum cancellation. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 28. Test-2025C-Q21 — *conf 0.65*
**Body:** Дараах нийлбэрийг тооцоолоорой. $\displaystyle\sum_{k=1}^{2025}(k^2+1) - \sum_{k=5}^{2025}(k^2+1)$
**Options:** **A)** $14$  **B)** $30$  **C)** $34$  **D)** $101$  **E)** $121$
**Correct answer:** C
**Current classification:** skill_tag=`progression` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 29. Test-2025D-Q8 — *conf 0.65*
**Body:** $\frac{x-1}{1}=\frac{y+1}{1}=\frac{z-1}{2}$ шулуун $Oxz$ хавтгайтай огтлолцох цэгийн координатыг олоорой.
**Options:** **A)** $(3,0,2)$  **B)** $(2,3,0)$  **C)** $(2,0,3)$  **D)** $(0,0,-1)$  **E)** $(-1,0,-2)$
**Correct answer:** C
**Current classification:** skill_tag=`coordinate_geometry` · difficulty=`medium` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** 3D parametric line + plane intersection. Force-fit; surveillance 1/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 30. Test-1A-Q18 — *conf 0.55*
**Body:** $\frac{1}{1 \cdot 3} + \frac{1}{3 \cdot 5} + \frac{1}{5 \cdot 7} + \ldots + \frac{1}{2015 \cdot 2017}$ нийлбэрийг ол.
**Options:** **A)** $\frac{2016}{2017}$  **B)** $\frac{4032}{2017}$  **C)** $\frac{2015}{2017}$  **D)** $\frac{1008}{2017}$  **E)** $\frac{504}{2017}$
**Correct answer:** D
**Current classification:** skill_tag=`progression` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Telescoping sum 1/(2k-1)(2k+1) via partial fractions. Routed to progression (sequences/series umbrella, sum-formula scope) per <5 systemic-gap rule — telescoping cohort = 4 total. Imperfect fit: AP/GP drill cohort overlaps with series-summation practice.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 31. Test-1A-Q21 — *conf 0.65*
**Body:** Хүснэгтийг ашиглан $X$ ба $Y$ хоорондох хамаарлыг ол.
**Options:** **A)** $Y = \frac{X^2}{6}$  **B)** $Y = \frac{3X}{2}$  **C)** $Y = 2X$  **D)** $Y = \frac{2X^2}{9}$  **E)** $Y = \frac{2X}{3}$
**Correct answer:** E
**Current classification:** skill_tag=`function_graph` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Identify Y=f(X) rule from table of (X,Y) pairs. Tabular analogue of function_graph's 'identify the graph' — same identification skill, different representation.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 32. Test-1A-Q25 — *conf 0.65*
**Body:** Сурагч хоёр оронтой тоог түүний цифрүүдийн байрыг солисон тоогоор нь үржүүлэхэд аравтын оронд нь 2 нэгжээр алдаж жинхэнэ үржвэрээс бага 2924 гэсэн тоо гаргажээ. Өгөгдсөн тооноос цифрүүдийн байрыг солисон тоог хасахад 18 гарах байсан бол анх хэд гэсэн тоо байсан бэ?
**Options:** **A)** $53$  **B)** $64$  **C)** $97$  **D)** $86$  **E)** $68$
**Correct answer:** B
**Current classification:** skill_tag=`system_of_equations` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Digit-swap word problem reducing to two-variable linear system in (a,b): original−swap=18 plus multiplication-error condition. System solving is the math kernel; word_problem_arithmetic scope is mixtures/proportions, doesn't fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 33. Test-1A-Q31 — *conf 0.55*
**Body:** $x = 8.7 \pm 0.4$ бол дараах тоонуудаас $x$-ийн оронд авч болох утгыг сонго. $M = 8.223$, $N = 8.341$, $P = 9.023$, $Q = 9.2$
**Options:** **A)** $M$ ба $N$  **B)** $N$ ба $P$  **C)** $N$ ба $Q$  **D)** $P$ ба $Q$  **E)** $M$ ба $Q$
**Correct answer:** B
**Current classification:** skill_tag=`number_representation` · difficulty=`easy` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Tolerance interval x=8.7±0.4 ⇒ x∈[8.3,9.1], pick values inside. Force-fit per refined rule: number_representation drill cohort (rounding/approximation/comparing reals) does teach tolerance-band reasoning. Near-neighbor fit, not exact.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 34. Test-1A-Q36 — *conf 0.6*
**Body:** $y = \frac{5}{2+x}$, $y = 5\sqrt{2-x}$, $y = -5x^2 - 2$ функцүүдээс $[-10; -3]$ завсарт буурах нь аль нь вэ?
**Options:** **A)** $y = \frac{5}{2+x}$  **B)** $y = 5\sqrt{2-x}$  **C)** $y = -5x^2 - 2$  **D)** $y = 5\sqrt{2-x}$ ба $y = -5x^2-2$  **E)** $y = \frac{5}{2+x}$ ба $y = 5\sqrt{2-x}$
**Correct answer:** E
**Current classification:** skill_tag=`function_graph` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Identify which of three named functions are decreasing on [−10,−3]. Qualitative monotonicity per function family — no derivative computation expected. function_graph (function-behavior identification) over derivative_application.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 35. Test-1B-Q18 — *conf 0.55*
**Body:** $\frac{1}{2 \cdot 4} + \frac{1}{4 \cdot 6} + \frac{1}{6 \cdot 8} + \ldots + \frac{1}{2016 \cdot 2018}$ нийлбэрийг ол.
**Options:** **A)** $\frac{1007}{2018}$  **B)** $\frac{504}{1009}$  **C)** $\frac{252}{1009}$  **D)** $\frac{509}{2018}$  **E)** $\frac{252}{509}$
**Correct answer:** C
**Current classification:** skill_tag=`progression` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Telescoping sum 1/(2k)(2k+2). Same telescoping technique as Q1A-Q18; same force-fit rationale.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 36. Test-1B-Q21 — *conf 0.65*
**Body:** Хүснэгтийг ашиглан $X$ ба $Y$ хоорондох хамаарлыг ол.
**Options:** **A)** $Y = X$  **B)** $Y = \frac{X+1}{2}$  **C)** $Y = \frac{X+2}{3}$  **D)** $Y = \frac{X^2+2}{3}$  **E)** $Y = \frac{2X+1}{3}$
**Correct answer:** E
**Current classification:** skill_tag=`function_graph` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Variant of Q1A-Q21: identify Y=f(X) from table of pairs. Tabular identification.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 37. Test-1B-Q25 — *conf 0.65*
**Body:** Сурагч хоёр оронтой тоог түүний цифрүүдийн байрыг сольсон тоогоор нь үржүүлэхэд аравтын оронд нь $3$ нэгжээр алдаж жинхэнэ үржвэрээс их $2974$ гэсэн тоо гаргажээ. Өгөгдсөн тоо ба цифрүүдийн байрыг сольсон тоо хоёрын нийлбэр $110$ бол анх хэд гэсэн тоо байсан бэ?
**Options:** **A)** $28$  **B)** $64$  **C)** $55$  **D)** $73$  **E)** $91$
**Correct answer:** B
**Current classification:** skill_tag=`system_of_equations` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Variant of Q1A-Q25: digit-swap with multiplication-error + sum conditions. Two-variable linear system after setup.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 38. Test-1B-Q31 — *conf 0.55*
**Body:** Бүлүүний хайрцаг дээр бүлүүний жин $500 \pm 12.3$ г гэж бичжээ. Бүлүүний авч болох утгыг сонго. $M = 487.5$, $N = 489.5$, $P = 512.01$, $Q = 513.4$
**Options:** **A)** $M$ ба $N$  **B)** $N$ ба $P$  **C)** $N$ ба $Q$  **D)** $P$ ба $Q$  **E)** $M$ ба $Q$
**Correct answer:** B
**Current classification:** skill_tag=`number_representation` · difficulty=`easy` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Tolerance interval 500±12.3 ⇒ [487.7,512.3]. CSV topic is statistics (subtopic 'алдаа'/error) but the math is approximation/tolerance, not statistical dispersion (variance/SD). Same near-neighbor concern as Q1A-Q31.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 39. Test-1B-Q36 — *conf 0.6*
**Body:** $y = \frac{6}{x}$, $y = (1 - x)^2$, $y = \sqrt{x - 3}$ функцүүдээс график нь $[5; 8]$ завсарт өсдөг нь аль нь вэ?
**Options:** **A)** $y = \sqrt{x - 3}$  **B)** $y = \frac{6}{x}$  **C)** $y = (1 - x)^2$  **D)** $y = (1 - x)^2; y = \sqrt{x-3}$  **E)** $y = \frac{6}{x}; y = \sqrt{x - 3}$
**Correct answer:** D
**Current classification:** skill_tag=`function_graph` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Variant of Q1A-Q36: identify which of y=6/x, (1-x)², √(x-3) increase on [5,8]. Qualitative monotonicity identification.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 40. Test-2A-Q10 — *conf 0.55*
**Body:** $a \mathbin{./} b = a^b$ ба $a \otimes b = 2a + b$ гэсэн хоёр шинэ үйлдэл тодорхойлъё. $(16 \mathbin{./} \frac{1}{2}) \otimes (2 \mathbin{./} 3) = ?$
**Options:** **A)** $14$  **B)** $16$  **C)** $22$  **D)** $24$  **E)** Аль нь ч биш
**Correct answer:** B
**Current classification:** skill_tag=`function_inverse_composite` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Custom operators. Surveillance 1/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 41. Test-2A-Q16 — *conf 0.65*
**Body:** $(2 - x^2)^{2015}$-олон гишүүнтийн бүх коэффициентүүдийн нийлбэрийг ол.
**Options:** **A)** $-2^{2015}$  **B)** $-1$  **C)** $1$  **D)** $2^{2015}$  **E)** Аль нь ч биш
**Correct answer:** C
**Current classification:** skill_tag=`polynomial_remainder` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** P(1) trick. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 42. Test-2A-Q35 — *conf 0.6*
**Body:** Санамсаргүй хэмжигдэхүүн $X$-ийн тархалтын функц $F(x) = \begin{cases} 0, & x \leq 0 \\ \frac{x}{4}, & 0 < x \leq 4 \\ 1, & x > 4 \end{cases}$ томъёогоор өгөгдөв. $P(3 < x \leq 4)$ магадлалыг ол.
**Options:** **A)** $\frac{3}{4}$  **B)** $\frac{1}{4}$  **C)** $1$  **D)** $\frac{1}{2}$  **E)** $0$
**Correct answer:** B
**Current classification:** skill_tag=`discrete_distribution` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Continuous CDF. Force-fit; surveillance 1/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 43. Test-2B-Q10 — *conf 0.55*
**Body:** $a \mathbin{./} b = b^{a}$ ба $a \otimes b = 2a - b$ гэсэн хоёр шинэ үйлдэл тодорхойлъё. $(\frac{1}{4} \mathbin{./} 81) \otimes (2 \mathbin{./} 3) = ?$
**Options:** **A)** $-3$  **B)** $3$  **C)** $-2$  **D)** $9$  **E)** $12$
**Correct answer:** A
**Current classification:** skill_tag=`function_inverse_composite` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Custom operators variant. Surveillance 2/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 44. Test-2B-Q16 — *conf 0.65*
**Body:** $(x^{2}-2)^{2015}$-олон гишүүнтийн бүх коэффициентүүдийн нийлбэрийг ол.
**Options:** **A)** $1$  **B)** $-2^{2015}$  **C)** $0$  **D)** $2^{2015}$  **E)** $-1$
**Correct answer:** E
**Current classification:** skill_tag=`polynomial_remainder` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** P(1) coefficient sum.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 45. Test-2B-Q35 — *conf 0.6*
**Body:** Санамсаргүй хэмжигдэхүүн $X$-ийн тархалтын функц
$F(x) = \begin{cases} 0, & x \leq 0 \\ \frac{x}{3}, & 0 < x \leq 3 \\ 1, & x > 3 \end{cases}$
томъёогоор өгөгдөв. $P(1 < x \leq 3)$ магадлалыг ол.
**Options:** **A)** $\frac{1}{3}$  **B)** $\frac{2}{3}$  **C)** $\frac{1}{4}$  **D)** $\frac{1}{2}$  **E)** $\frac{3}{4}$
**Correct answer:** B
**Current classification:** skill_tag=`discrete_distribution` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Continuous CDF. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 46. Test-3A-Q1 — *conf 0.5*
**Body:** $-3 - |-7|$-н утгыг ол.
**Options:** **A)** $-10$  **B)** $4$  **C)** $-4$  **D)** $10$  **E)** $-21$
**Correct answer:** A
**Current classification:** skill_tag=`number_representation` · difficulty=`easy` · confidence=`0.5` · classifier=`in-chat`
**Rationale:** Basic abs-value eval. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 47. Test-3A-Q4 — *conf 0.65*
**Body:** Хамар өнцгүүд $(7x - 1)°$, $(2x + 1)°$ бол $x$-г ол.
**Options:** **A)** $10°$  **B)** $40°$  **C)** $20°$  **D)** $30°$  **E)** $5°$
**Correct answer:** C
**Current classification:** skill_tag=`linear_equation` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Supplementary angles. Surveillance 1/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 48. Test-3A-Q25 — *conf 0.65*
**Body:** $x > 0$ үед $f(x) = f(x - 2)$ ба $x \leq 0$ бол $f(x) = |x|$ гэж тодорхойлогдсон функц өгөгдөв. $f(2.7) - f(5)$-ийг ол.
**Options:** **A)** $2.3$  **B)** $-0.7$  **C)** $-2.3$  **D)** $0.3$  **E)** $1.7$
**Correct answer:** D
**Current classification:** skill_tag=`function_domain_range` · difficulty=`medium` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Recursive function evaluation.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 49. Test-3B-Q1 — *conf 0.5*
**Body:** $-5 - |-9|$-н утгыг ол.
**Options:** **A)** $-14$  **B)** $4$  **C)** $-4$  **D)** $14$  **E)** $13$
**Correct answer:** A
**Current classification:** skill_tag=`number_representation` · difficulty=`easy` · confidence=`0.5` · classifier=`in-chat`
**Rationale:** Basic abs-value eval.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 50. Test-3B-Q4 — *conf 0.65*
**Body:** Хамар өнцгүүд $(7x - 3)^\circ$, $(11x + 3)^\circ$ бол $x$-г ол.
**Options:** **A)** $10^\circ$  **B)** $5^\circ$  **C)** $20^\circ$  **D)** $30^\circ$  **E)** $15^\circ$
**Correct answer:** A
**Current classification:** skill_tag=`linear_equation` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Supplementary angles variant. Surveillance 2/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 51. Test-5A-Q28 — *conf 0.65*
**Body:** $f(x) = \frac{-6x^2 + 5x}{4x + 5} + \frac{12x^3 + 7x + 1}{8x^2 + 6x - 5}$ функцийн графикийн хэвтээ асимптотыг ол.
**Options:** **A)** $y = \frac{1}{2}$  **B)** $y = 0$  **C)** $y = -\frac{5}{4}$  **D)** $y = 2$  **E)** Хэвтээ асимптотгүй
**Correct answer:** D
**Current classification:** skill_tag=`function_domain_range` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Horizontal asymptote of sum of rational functions: slants cancel, constants=2.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 52. Test-5B-Q28 — *conf 0.65*
**Body:** $f(x) = \frac{-4x^2 + 3x}{3x + 4} + \frac{8x^3 + 9x - 1}{6x^2 + 5x - 4}$ функцийн графикийн хэвтээ асимптотыг ол.
**Options:** **A)** $y = 0$  **B)** $y = \frac{4}{3}$  **C)** $y = -\frac{4}{3}$  **D)** $y = \frac{5}{3}$  **E)** $\frac{3}{5}$
**Correct answer:** D
**Current classification:** skill_tag=`function_domain_range` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Horizontal asymptote.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 53. Test-6A-Q31 — *conf 0.6*
**Body:** $Y$-санамсаргүй хэмжигдэхүүний нягтын функц $f(y) = \begin{cases} 4y^k, & 0 \leq y \leq 1 \\ 0, & \text{бусад} \end{cases}$ $(k > 0)$ өгөгдөв. $k$-ийн утгыг ол.
**Options:** **A)** $4$  **B)** $1$  **C)** $2$  **D)** $3$  **E)** Аль нь ч биш
**Correct answer:** D
**Current classification:** skill_tag=`discrete_distribution` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Continuous density k. Force-fit. Surveillance 3/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 54. Test-6A-Q33 — *conf 0.65*
**Body:** $(3x - \frac{2}{x})^8$ задаргааны $x$ агуулаагүй гишүүнийг ол.
**Options:** **A)** $3^4 \cdot C_8^4$  **B)** $4 \cdot 3^6 \cdot C_8^2$  **C)** $6^4 \cdot C_8^4$  **D)** $C_8^4$  **E)** $-6^4 \cdot C_8^4$
**Correct answer:** C
**Current classification:** skill_tag=`combination_selection` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Binomial expansion x-free term. Force-fit. Surveillance 1/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 55. Test-6A-Q34 — *conf 0.65*
**Body:** $\vec{n} = 2\vec{i} - 3\vec{j} + \vec{k}$-нормальтай $A(2, 1, 1)$ цэгийг дайрсан хавтгайн тэгшитгэлийг зaa.
**Options:** **A)** $2x - 3y + z = 0$  **B)** $2x - 3y + z - 1 = 0$  **C)** $2x - 3y + z + 2 = 0$  **D)** $2x - 3y + z - 2 = 0$  **E)** Аль нь ч биш
**Correct answer:** D
**Current classification:** skill_tag=`coordinate_geometry` · difficulty=`medium` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** 3D plane equation. Force-fit. Surveillance 2/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 56. Test-6B-Q31 — *conf 0.6*
**Body:** $X$-санамсаргүй хэмжигдэхүүний нягтын функц $f(x) = \begin{cases} \frac{5x^4}{31}, & 1 \leq x \leq 2 \\ 0, & \text{бусад} \end{cases}$ өгөгдөв. $p(1 < x < 1.5)$-ийн утгыг ол.
**Options:** **A)** $\frac{31}{32}$  **B)** $\frac{211}{243}$  **C)** $\frac{211}{992}$  **D)** $\frac{243}{992}$  **E)** $\frac{243}{1024}$
**Correct answer:** C
**Current classification:** skill_tag=`discrete_distribution` · difficulty=`medium` · confidence=`0.6` · classifier=`in-chat`
**Rationale:** Continuous PDF integral. Surveillance 4/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 57. Test-6B-Q33 — *conf 0.65*
**Body:** $(x^2 - \frac{1}{x})^6$ задаргааны $x$ агуулаагүй гишүүнийг ол.
**Options:** **A)** $30$  **B)** $15$  **C)** $4$  **D)** $-15$  **E)** $-30$
**Correct answer:** B
**Current classification:** skill_tag=`combination_selection` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Binomial x-free term. Force-fit. Surveillance 2/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 58. Test-6B-Q34 — *conf 0.65*
**Body:** $A(1, 3, 0)$, $B(-2, 1, 2)$ ба $C(1, -2, -1)$ цэгүүдийг агуулсан хавтгайн тэгшитгэл бич.
**Options:** **A)** $4x + y + 5z - 1 = 0$  **B)** $4x + y - 5z - 1 = 0$  **C)** $4x - y + 5z + 1 = 0$  **D)** $4x - y + 5z + 2 = 0$  **E)** $4x - y + 5z - 1 = 0$
**Correct answer:** E
**Current classification:** skill_tag=`coordinate_geometry` · difficulty=`hard` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** 3D plane through 3 points. Force-fit. Surveillance 3/5.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 59. Test-7A-Q16 — *conf 0.65*
**Body:** Дараах тоонуудаас модулиараа хамгийн бага тоог ол.
**Options:** **A)** $-4.1$  **B)** $-5\frac{1}{3}$  **C)** $3.2$  **D)** $7.8$  **E)** $-19.2$
**Correct answer:** C
**Current classification:** skill_tag=`number_representation` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** Compare |·|. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 60. Test-7A-Q34 — *conf 0.55*
**Body:** $\frac{1}{1\cdot 2}+\frac{1}{2\cdot 3}+\frac{1}{3\cdot 4}+...+\frac{1}{(n-1)\cdot n}<\frac{3}{4}$ бол $n$-г ол. $n \in \mathbb{N}$
**Options:** **A)** $1$  **B)** $2$  **C)** $3$  **D)** $4$  **E)** шийдгүй
**Correct answer:** C
**Current classification:** skill_tag=`progression` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Telescoping inequality.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 61. Test-7B-Q16 — *conf 0.65*
**Body:** Дараах тоонуудаас модулиараа хамгийн бага тоог ол.
**Options:** **A)** $-2\frac{1}{2}$  **B)** $3.2$  **C)** $-12.3$  **D)** $-6\frac{1}{2}$  **E)** $7.5$
**Correct answer:** A
**Current classification:** skill_tag=`number_representation` · difficulty=`easy` · confidence=`0.65` · classifier=`in-chat`
**Rationale:** |·| variant. Force-fit.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 62. Test-7B-Q34 — *conf 0.55*
**Body:** $\frac{1}{1\cdot 2}+\frac{1}{2\cdot 3}+\frac{1}{3\cdot 4}+...+\frac{1}{(n-1)\cdot n}<\frac{1}{2}$ бол $n$-г ол. $n \in \mathbb{N}$
**Options:** **A)** $1$  **B)** $2$  **C)** $3$  **D)** $4$  **E)** шийдгүй
**Correct answer:** E
**Current classification:** skill_tag=`progression` · difficulty=`medium` · confidence=`0.55` · classifier=`in-chat`
**Rationale:** Telescoping inequality variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

---

## Section: auto-trigger sample (5 random per high-loop-impact tag)  (53 rows)

### 63. Test-2023B-Q32 — *derivative_application*
**Body:** $y = x^2$ параболыг шүргэх бөгөөд $A(1, 0)$ цэгийг дайрах эрэг налалтай шулууны тэгшитгэл бичээрэй.
**Options:** **A)** $y = 2x - 2$  **B)** $y = 2x - 1$  **C)** $y = 4x - 4$  **D)** $y = 4x - 2$  **E)** $y = x - 1$
**Correct answer:** C
**Current classification:** skill_tag=`derivative_application` · difficulty=`easy` · confidence=`0.75` · classifier=`rule`
**Rationale:** keyword: derivative application (subtopic='tangent line to curve')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 64. Test-2021B-Q24 — *derivative_application*
**Body:** $f(x)=x^2-4x+5$ функцийн $x=1$ цэгт татсан нормаль шулууны тэгшитгэлийг бичээрэй.
**Options:** **A)** $y=-2x+4$  **B)** $y=\dfrac{1}{2}x+\dfrac{3}{2}$  **C)** $y=-\dfrac{1}{2}x+\dfrac{5}{2}$  **D)** $y=2x$  **E)** $y=2x-4$
**Correct answer:** B
**Current classification:** skill_tag=`derivative_application` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='normal_line')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 65. Test-2024C-Q34 — *derivative_application*
**Body:** $f(x)$ функцийн уламжлал болох $f'(x)$ функцийн график нь зурагт үзүүлсэн парабол байв. Хэрэв $f(0) = -\frac{14}{3}$ бол $f(x)$ функцийн максимум утгыг олоорой.
**Options:** **A)** $10\frac{2}{3}$  **B)** $5$  **C)** $4$  **D)** $6$  **E)** $-4\frac{2}{3}$
**Correct answer:** D
**Current classification:** skill_tag=`derivative_application` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='экстремум')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 66. Test-2024A-Q34 — *derivative_application*
**Body:** $f(x)$ функцийн уламжлал болох $f'(x)$ функцийн график нь зурагт үзүүлсэн парабол байв. Хэрэв $f(0)=-4$ бол $f(x)$ функцийн максимум утгыг олоорой.
**Options:** **A)** $-5\frac{2}{3}$  **B)** $4$  **C)** $3$  **D)** $9$  **E)** $5$
**Correct answer:** E
**Current classification:** skill_tag=`derivative_application` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='экстремум')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 67. Test-2023D-Q35 — *derivative_application*
**Body:** $f(x) = 2x^3 - bx^2 - cx + d$ функц $x = -1$, $x = 2$ цэгүүдэд экстремумтэй ба минимум утга нь $-15$ бол максимум утгыг ол.
**Options:** **A)** 15  **B)** -42  **C)** 12  **D)** 18  **E)** 9
**Correct answer:** C
**Current classification:** skill_tag=`derivative_application` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** keyword: extrema (subtopic='extrema of cubic function')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 68. Test-2022C-Q8 — *derivative_rules*
**Body:** $y=\sin 3x$ функцийн уламжлалыг олоорой.
**Options:** **A)** $\cos 3x$  **B)** $3\cos 3x$  **C)** $-\cos 3x$  **D)** $-3\cos 3x$  **E)** $3\cos x$
**Correct answer:** B
**Current classification:** skill_tag=`derivative_rules` · difficulty=`easy` · confidence=`0.75` · classifier=`rule`
**Rationale:** keyword: derivative (subtopic='derivative_trig')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 69. Test-2022B-Q15 — *derivative_rules*
**Body:** $f(x)=\ln(x+4)$ функцийн графикийн $x=2$ цэгт татсан шүргэгч шулууны налалтыг олоорой.
**Options:** **A)** $\frac{1}{4}$  **B)** $\frac{1}{2}$  **C)** $\frac{1}{\ln 6}$  **D)** $\frac{1}{6}$  **E)** $\frac{1}{\ln 2}$
**Correct answer:** D
**Current classification:** skill_tag=`derivative_rules` · difficulty=`easy` · confidence=`0.75` · classifier=`rule`
**Rationale:** keyword: derivative (subtopic='derivative_log')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 70. Test-2022B-Q8 — *derivative_rules*
**Body:** $y=\sin 3x$ функцийн уламжлалыг олоорой.
**Options:** **A)** $-3\cos 3x$  **B)** $\cos 3x$  **C)** $-\cos 3x$  **D)** $3\cos 3x$  **E)** $3\cos x$
**Correct answer:** D
**Current classification:** skill_tag=`derivative_rules` · difficulty=`easy` · confidence=`0.75` · classifier=`rule`
**Rationale:** keyword: derivative (subtopic='derivative_trig')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 71. Test-5B-Q33 — *derivative_rules*
**Body:** $8x^3 + y^3 = 16$ тэгшитгэлийн хувьд $\frac{dy}{dx}$-ийг ол.
**Options:** **A)** $\frac{dy}{dx} = -\frac{8x^2}{y^2}$  **B)** $y' = \frac{2}{\sqrt[3]{(2 - x^3)^2}}$  **C)** $\frac{dy}{dx} = \frac{y^2}{8x^2}$  **D)** $\frac{dy}{dx} = \frac{8x^2}{y^2}$  **E)** Аль нь ч биш
**Correct answer:** A
**Current classification:** skill_tag=`derivative_rules` · difficulty=`medium` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Implicit differentiation.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 72. Test-2021C-Q10 — *derivative_rules*
**Body:** $f(x)=\dfrac{2}{\sqrt{x}}$ функцийн хувьд $f'(4)$-ийн утгыг олоорой.
**Options:** **A)** $-\dfrac{1}{4}$  **B)** $-\dfrac{1}{8}$  **C)** $-\dfrac{3}{8}$  **D)** $-2$  **E)** $8$
**Correct answer:** B
**Current classification:** skill_tag=`derivative_rules` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Variant. Power-rule derivative.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 73. Test-2022A-Q33 — *circle_geometry*
**Body:** Координатын эхэд тэвтэй бөгөөд $2x + \sqrt{5}\,y - 2\sqrt{5} = 0$ шулуунд шүргэгч тойргийн тэгшитгэл бичээрэй.
**Options:** **A)** $x^2 + y^2 = \dfrac{20}{9}$  **B)** $x^2 + y^2 = \dfrac{16}{7}$  **C)** $x^2 + y^2 = \dfrac{49}{25}$  **D)** $x^2 + y^2 = \dfrac{12}{5}$  **E)** $x^2 + y^2 = \dfrac{25}{16}$
**Correct answer:** A
**Current classification:** skill_tag=`circle_geometry` · difficulty=`easy` · confidence=`0.75` · classifier=`rule`
**Rationale:** keyword: circle (subtopic='circle tangent to line')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 74. Test-2023A-Q8 — *circle_geometry*
**Body:** $AB$ диаметр ба $\angle BAC = 58°$ бол $\angle ABC = ?$
**Options:** **A)** $58°$  **B)** $29°$  **C)** $32°$  **D)** $42°$  **E)** $90°$
**Correct answer:** C
**Current classification:** skill_tag=`circle_geometry` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='тойрог')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 75. Test-2024C-Q5 — *circle_geometry*
**Body:** Зурагт үзүүлсэн $O$ цэгт төвтэй тойргийн шүргэгч $BA$ бөгөөд $BO$ хэрчим тойргийг $C$ цэгт огтлов. Хэрэв $\angle AOB = 70°$ бол $\angle BAC$ өнцгийг ол.
**Options:** **A)** $20°$  **B)** $35°$  **C)** $30°$  **D)** $55°$  **E)** $70°$
**Correct answer:** B
**Current classification:** skill_tag=`circle_geometry` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='тойрог')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 76. Test-2024C-Q27 — *circle_geometry*
**Body:** $x^2 + y^2 = 4$ тойргийн цэгүүдээс $A(4,\ 3)$ цэгт хамгийн ойрхон байх цэгийн $x$ координатыг ол.
**Options:** **A)** $1.75$  **B)** $1.7$  **C)** $1.65$  **D)** $1.5$  **E)** $1.6$
**Correct answer:** E
**Current classification:** skill_tag=`circle_geometry` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='тойрог')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 77. Test-4B-Q35 — *circle_geometry*
**Body:** $x^2 + y^2 = 25$ муруйн $(3, -4)$ цэгт татсан нормал шулууны тэгшитгэл нь
**Options:** **A)** $y = \frac{3}{4}x$  **B)** $y = -\frac{4}{3}x$  **C)** $y = \frac{3}{4}x - 6\frac{1}{4}$  **D)** $y = \frac{3}{4}x + \frac{7}{4}$  **E)** $y = \frac{3}{4}x + 6\frac{1}{4}$
**Correct answer:** B
**Current classification:** skill_tag=`circle_geometry` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='тойрог')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 78. Test-2024C-Q25 — *solid_geometry*
**Body:** Конусын байгуулагч суурийн хавтгайтай үүсгэх өнцгийн синус $\frac{12}{13}$ байв. Конусын суурийн радиус 5 бол хажуу гадаргуун талбайг ол.
**Options:** **A)** $85\pi$  **B)** $100\pi$  **C)** $65\pi$  **D)** $60\pi$  **E)** $90\pi$
**Correct answer:** C
**Current classification:** skill_tag=`solid_geometry` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match — 3D solid (subtopic='конус')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 79. Test-2021A-Q20 — *solid_geometry*
**Body:** Конусын байгуулагч нь 12 нэгж, суурийн радиус нь 8 нэгж урттай байв. Энэ конусын хажуу гадаргуугийн дэлгээс болох секторын өнцгийг олоорой.
**Options:** **A)** $540^\circ$  **B)** $120^\circ$  **C)** $240^\circ$  **D)** $270^\circ$  **E)** $\arccos\dfrac{1}{9}$
**Correct answer:** C
**Current classification:** skill_tag=`solid_geometry` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match — 3D solid (subtopic='cone_sector_angle')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 80. Test-2024B-Q25 — *solid_geometry*
**Body:** Конусын байгуулагч суурийн хавтгайтай үүсгэх өнцгийн синус $\frac{4}{5}$ байв. Конусын суурийн радиус 6 бол хажуу гадаргуун талбайг ол.
**Options:** **A)** $36\pi$  **B)** $60\pi$  **C)** $96\pi$  **D)** $48\pi$  **E)** $80\pi$
**Correct answer:** B
**Current classification:** skill_tag=`solid_geometry` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match — 3D solid (subtopic='конус')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 81. Test-2021D-Q20 — *solid_geometry*
**Body:** Конусын байгуулагч нь 8 нэж, суурийн радиус нь 6 нэж урттай байв. Энэ конусын хажуу гадаргуугийн дэлгээс болох секторын өнцгийг олоорой.
**Options:** **A)** $240^\circ$  **B)** $90^\circ$  **C)** $480^\circ$  **D)** $270^\circ$  **E)** $\arccos\!\left(-\frac{1}{8}\right)$
**Correct answer:** D
**Current classification:** skill_tag=`solid_geometry` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match — 3D solid (subtopic='конус')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 82. Test-2025A-Q8 — *solid_geometry*
**Body:** $\frac{x-1}{1} = \frac{y+1}{1} = \frac{z-1}{2}$ шулуун $Oxz$ хавтгайтай огтолцох цэгийн координатыг олоорой.
**Options:** **A)** $(2,\ 0,\ 3)$  **B)** $(2,\ 3,\ 0)$  **C)** $(3,\ 0,\ 2)$  **D)** $(0,\ 0,\ -1)$  **E)** $(-1,\ 0,\ -2)$
**Correct answer:** A
**Current classification:** skill_tag=`solid_geometry` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** keyword: spatial geometry (subtopic='орон зайн геометр')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 83. Test-6B-Q5 — *triangle_geometry*
**Body:** Дараах гуравтуудын аль нь Пифагорын гурвал үүсгэхгүй вэ?
**Options:** **A)** $6, 8, 10$  **B)** $16, 30, 34$  **C)** $18, 25, 27$  **D)** $5, 12, 13$  **E)** $7, 24, 25$
**Correct answer:** C
**Current classification:** skill_tag=`triangle_geometry` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** keyword: Pythagorean theorem (subtopic='пифагорын теорем')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 84. Test-4A-Q17 — *triangle_geometry*
**Body:** $(6, 8, 10); (10, 24, 26); (3, 3, 3\sqrt{2}); (1, 2, \sqrt{5}); (4, 7, 8)$ эдгээр гуравтуудаас аль нь тэгш өнцөгт гурвалжин үүсгэхгүй вэ?
**Options:** **A)** $6, 8, 10$  **B)** $10, 24, 26$  **C)** $3, 3, 3\sqrt{2}$  **D)** $1, 2, \sqrt{5}$  **E)** $4, 7, 8$
**Correct answer:** E
**Current classification:** skill_tag=`triangle_geometry` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** subtopic match — needs body check for trig_triangle override (subtopic='гурвалжин')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 85. Test-2024D-Q12 — *triangle_geometry*
**Body:** Зурагт өгсөн $ABC$ гурвалжны $AN = 9$, $BM = 12$ байх медианууд перпендикуляр ба $O$ цэгт огтлолцох бол $ONCM$ дөрвөн өнцгтийн талбайг ол.
**Options:** **A)** $13.5$  **B)** $18$  **C)** $28.8$  **D)** $24$  **E)** $27$
**Correct answer:** D
**Current classification:** skill_tag=`triangle_geometry` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** subtopic match — needs body check for trig_triangle override (subtopic='гурвалжин')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 86. Test-4B-Q17 — *triangle_geometry*
**Body:** $(3, 4, 5); (5, 12, 13); (2, 2, 2\sqrt{2}); (4, 8, 4\sqrt{5}); (3, 5, \sqrt{23})$ эдгээр гуравтуудаас аль нь тэгш өнцөгт гурвалжин үүсгэхгүй вэ?
**Options:** **A)** $3, 4, 5$  **B)** $5, 12, 13$  **C)** $2, 2, 2\sqrt{2}$  **D)** $4, 8, 4\sqrt{5}$  **E)** $3, 5, \sqrt{23}$
**Correct answer:** E
**Current classification:** skill_tag=`triangle_geometry` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** subtopic match — needs body check for trig_triangle override (subtopic='гурвалжин')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 87. Test-7B-Q7 — *triangle_geometry*
**Body:** Зургаас $\angle CAB$-ийн хэмжээг ол.
**Options:** **A)** $50°$  **B)** $60°$  **C)** $70°$  **D)** $80°$  **E)** $40°$
**Correct answer:** A
**Current classification:** skill_tag=`triangle_geometry` · difficulty=`easy` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Angle variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 88. Test-2A-Q2 — *exponent_rules*
**Body:** $\frac{3^5 \cdot (27^2)^3 \cdot \sqrt{3}}{81 \cdot 9^{\frac{5}{4}}}$ илэрхийллийг хялбарчил.
**Options:** **A)** $3^{14.5}$  **B)** $3^{16}$  **C)** $3^{17}$  **D)** $3^{18.25}$  **E)** Аль нь ч биш
**Correct answer:** C
**Current classification:** skill_tag=`exponent_rules` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='зэрэг')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 89. Test-2021D-Q5 — *exponent_rules*
**Body:** $2^{\frac{2}{3}}$ зэргийг язгуур хэрэглэн бичээрэй.
**Options:** **A)** $\sqrt{2}$  **B)** $\sqrt{8}$  **C)** $\sqrt[3]{2}$  **D)** $\sqrt[3]{4}$  **E)** $\sqrt[3]{8}$
**Correct answer:** D
**Current classification:** skill_tag=`exponent_rules` · difficulty=`easy` · confidence=`0.8` · classifier=`rule`
**Rationale:** keyword: exponent rules (subtopic='зэрэг ба язгуур')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 90. Test-2024C-Q4 — *exponent_rules*
**Body:** Үйлдлийг гүйцэтгэ. $\sqrt[3]{9^2} \cdot 3^{\frac{2}{3}}$
**Options:** **A)** $6 \cdot 3^{\frac{1}{3}}$  **B)** $3^{\frac{8}{3}}$  **C)** $9$  **D)** $3^{\frac{11}{3}}$  **E)** $27$
**Correct answer:** C
**Current classification:** skill_tag=`exponent_rules` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='зэрэг')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 91. Test-7B-Q26 — *exponent_rules*
**Body:** $(1-\frac{1}{4^x}):(1-\frac{1}{2^x})=7$ бол $2^{-x}=$?
**Options:** **A)** $4$  **B)** $6$  **C)** $2$  **D)** $\frac{1}{4}$  **E)** $\frac{1}{6}$
**Correct answer:** B
**Current classification:** skill_tag=`exponent_rules` · difficulty=`medium` · confidence=`0.85` · classifier=`rule`
**Rationale:** subtopic match — exponential equation (subtopic='экспоненциал тэгшитгэл')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 92. Test-4B-Q10 — *exponent_rules*
**Body:** $\frac{2^{19} \cdot 27^3 + 15 \cdot 4^9 \cdot 9^4}{6^9 \cdot 2^{10} + 12^{10}} = ?$
**Options:** **A)** $\frac{3}{7}$  **B)** $\frac{3}{2}$  **C)** $\frac{1}{14}$  **D)** $\frac{1}{6}$  **E)** $\frac{1}{2}$
**Correct answer:** E
**Current classification:** skill_tag=`exponent_rules` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='зэрэг')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 93. Test-2023C-Q1 — *radical_expression*
**Body:** Утгыг олоорой. $\sqrt{1\dfrac{64}{225}} =$
**Options:** **A)** $1\dfrac{8}{25}$  **B)** $1\dfrac{8}{15}$  **C)** $\dfrac{8}{15}$  **D)** $1\dfrac{2}{15}$  **E)** $1\dfrac{4}{25}$
**Correct answer:** D
**Current classification:** skill_tag=`radical_expression` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** keyword: radicals (subtopic='radicals')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 94. Test-2023A-Q1 — *radical_expression*
**Body:** Утгыг олоорой. $\sqrt{1\dfrac{64}{225}} =$
**Options:** **A)** $1\dfrac{2}{15}$  **B)** $1\dfrac{8}{15}$  **C)** $\dfrac{8}{15}$  **D)** $1\dfrac{8}{25}$  **E)** $1\dfrac{4}{25}$
**Correct answer:** A
**Current classification:** skill_tag=`radical_expression` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='язгуур')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 95. Test-2022C-Q11 — *radical_expression*
**Body:** $(3x+9)\cdot\sqrt{x-2}=0$ тэгшитгэл бодоорой.
**Options:** **A)** $-2,\ 3$  **B)** $-3,\ 2$  **C)** $2$  **D)** $-3$  **E)** $-2,\ -3$
**Correct answer:** C
**Current classification:** skill_tag=`radical_expression` · difficulty=`easy` · confidence=`0.8` · classifier=`rule`
**Rationale:** keyword: radical (subtopic='radical_equations')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 96. Test-7B-Q11 — *radical_expression*
**Body:** $(3\sqrt{2}-\sqrt{3})(4\sqrt{2}+2\sqrt{3})-\sqrt{24}$ хялбарчил.
**Options:** **A)** $15$  **B)** $16$  **C)** $17$  **D)** $18$  **E)** $19$
**Correct answer:** D
**Current classification:** skill_tag=`radical_expression` · difficulty=`medium` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Radical simplify variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 97. Test-5A-Q13 — *quadratic_equation*
**Body:** $x^2 - 4\sqrt{7} + \frac{28}{x^2} = 0$ тэгшитгэлийн ялгаатай шийдүүдийн үржвэрийг ол.
**Options:** **A)** $-14$  **B)** $4\sqrt{7}$  **C)** $-4\sqrt{7}$  **D)** $2\sqrt{7}$  **E)** $-2\sqrt{7}$
**Correct answer:** E
**Current classification:** skill_tag=`quadratic_equation` · difficulty=`hard` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** x²+28/x²=4√7; substitute u=x²; double root, product of x values = -2√7.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 98. Test-1B-Q8 — *quadratic_equation*
**Body:** $x^2 - x - 2 = 0$ тэгшитгэлийн бага шийдээс $4$-өөр их тоог ол.
**Options:** **A)** $2$  **B)** $3$  **C)** $4$  **D)** $6$  **E)** Аль нь ч биш
**Correct answer:** B
**Current classification:** skill_tag=`quadratic_equation` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='квадрат тэгшитгэл')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 99. Test-1A-Q24 — *quadratic_equation*
**Body:** $-x^2 + 2.5x - 0.5 = 0$ тэгшитгэлийн шийдүүдийн урвуу нь шийд болох квадрат тэгшитгэлийг ол.
**Options:** **A)** $2x^2 - 5x + 1 = 0$  **B)** $x^2 - 20x + 8 = 0$  **C)** $x^2 - 5x + 2 = 0$  **D)** $x^2 - 2x + 2 = 0$  **E)** $6x^2 - x + 5 = 0$
**Correct answer:** C
**Current classification:** skill_tag=`quadratic_equation` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='квадрат тэгшитгэл')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 100. Test-5B-Q19 — *quadratic_equation*
**Body:** $y = mx + 1$ шулуун $y = x^2 + 2x + 5$ параболтой ганц ерөнхий цэгтэй байх $m$-н утгууд $m_1$ ба $m_2$ байв. $m_1^2 + m_2^2$ утгыг ол.
**Options:** **A)** $8$  **B)** $40$  **C)** $25$  **D)** $24$  **E)** $68$
**Correct answer:** B
**Current classification:** skill_tag=`quadratic_equation` · difficulty=`medium` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Tangent to parabola.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 101. Test-5A-Q19 — *quadratic_equation*
**Body:** $y = mx + 3$ шулуун $y = x^2 + 2x + 7$ параболтой ганц ерөнхий цэгтэй байх $m$-н утгууд $m_1$ ба $m_2$ байв. $m_1^2 + m_2^2$ утгыг ол.
**Options:** **A)** $8$  **B)** $40$  **C)** $25$  **D)** $24$  **E)** $68$
**Correct answer:** B
**Current classification:** skill_tag=`quadratic_equation` · difficulty=`medium` · confidence=`0.85` · classifier=`in-chat`
**Rationale:** Line tangent to parabola: discriminant=0, m=-2 or 6; m₁²+m₂²=40.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 102. Test-2022D-Q31 — *definite_integral*
**Body:** Параболуудаар хүрээлэгдсэн дүрсийн талбайг олоорой. (Графикаар өгөгдсөн)
**Options:** **A)** $3\dfrac{1}{6}$  **B)** $2\dfrac{4}{5}$  **C)** $2\dfrac{5}{6}$  **D)** $3$  **E)** $2\dfrac{2}{3}$
**Correct answer:** E
**Current classification:** skill_tag=`definite_integral` · difficulty=`easy` · confidence=`0.85` · classifier=`rule`
**Rationale:** keyword: area between curves (subtopic='area_between_curves')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 103. Test-2024D-Q15 — *definite_integral*
**Body:** $\int_2^6 \frac{dx}{\sqrt{4x+1}}$ тодорхой интеграл бод.
**Options:** **A)** $1$  **B)** $4$  **C)** $\frac{1}{4}$  **D)** $16\frac{1}{3}$  **E)** $\frac{2}{15}$
**Correct answer:** A
**Current classification:** skill_tag=`definite_integral` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='тодорхой интеграл')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 104. Test-2022C-Q28 — *definite_integral*
**Body:** $\displaystyle\int_0^1 \frac{e^x-1}{e^x}\,dx$ интегралыг бодоорой.
**Options:** **A)** $\dfrac{1}{e}$  **B)** $\dfrac{1}{e}+2$  **C)** $2-\dfrac{1}{e}$  **D)** $1+\dfrac{1}{e}$  **E)** $-\dfrac{1}{e}$
**Correct answer:** A
**Current classification:** skill_tag=`definite_integral` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='definite_integral')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 105. Test-5B-Q36 — *definite_integral*
**Body:** $y = x + 1, y = 7 - x^2$ муруйнуудаар хүрээлэгдсэн дүрсийн талбайг ол.
**Options:** **A)** $15\frac{5}{6}$  **B)** $20\frac{5}{6}$  **C)** $8\frac{1}{6}$  **D)** $16\frac{5}{6}$  **E)** $19\frac{5}{6}$
**Correct answer:** B
**Current classification:** skill_tag=`definite_integral` · difficulty=`medium` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Area between curves.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 106. Test-2021B-Q32 — *definite_integral*
**Body:** $\displaystyle\int_1^4 |x-3|\,dx$ тодорхой интегралыг бодоорой.
**Options:** **A)** $\dfrac{3}{2}$  **B)** $\dfrac{5}{2}$  **C)** $-\dfrac{3}{2}$  **D)** $1$  **E)** $3$
**Correct answer:** B
**Current classification:** skill_tag=`definite_integral` · difficulty=`easy` · confidence=`0.7` · classifier=`rule`
**Rationale:** keyword: integral (defaulting to definite) (subtopic='definite_integral_absolute_value')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 107. Test-2024D-Q35 — *matrix_inverse*
**Body:** $A = \begin{pmatrix}x & -4 \\ 1 & y\end{pmatrix}$ матрицын урвуу $A^{-1}$ ба $E$ нь нэгж матриц байв. Хэрэв $A + 9A^{-1} = 6E$ нөхцөл биелэх бол $x^2 + y^2$-ийн утгыг ол.
**Options:** **A)** $25$  **B)** $13$  **C)** $20$  **D)** $26$  **E)** $37$
**Correct answer:** D
**Current classification:** skill_tag=`matrix_inverse` · difficulty=`medium` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='урвуу матриц')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 108. Test-2025C-Q35 — *matrix_inverse*
**Body:** $\begin{cases} ax + by = 3 \\ cx + dy = -3 \end{cases}$ системийн матриц $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ ба түүний урвуу нь $\begin{pmatrix} 4 & -2 \\ 2 & 7 \end{pmatrix}$ бол $x - y$ ялгаврын утгыг олоорой.
**Options:** **A)** $-26$  **B)** $15$  **C)** $-3$  **D)** $22$  **E)** $33$
**Correct answer:** E
**Current classification:** skill_tag=`matrix_inverse` · difficulty=`medium` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 109. Test-2021D-Q14 — *matrix_inverse*
**Body:** $M = \begin{pmatrix}10 & 6\\3 & 2\end{pmatrix}$ бол $M^{-1}$ матрицыг олоорой.
**Options:** **A)** $\begin{pmatrix}2 & -6\\-3 & 10\end{pmatrix}$  **B)** $\begin{pmatrix}-5 & 1.5\\3 & -1\end{pmatrix}$  **C)** $\begin{pmatrix}10 & 3\\6 & 2\end{pmatrix}$  **D)** $\begin{pmatrix}1 & -3\\-1.5 & 5\end{pmatrix}$  **E)** $\begin{pmatrix}1 & 3\\-1.5 & -5\end{pmatrix}$
**Correct answer:** D
**Current classification:** skill_tag=`matrix_inverse` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Compute M^(-1) for 2×2. det=2 then formula.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 110. Test-2024B-Q35 — *matrix_inverse*
**Body:** $A=\begin{pmatrix}x&-4\\1&y\end{pmatrix}$ матрицын урвуу $A^{-1}$ ба $E$ нь нэгж матриц байв. Хэрэв $A+9A^{-1}=6E$ нөхцөл биелэх бол $x^2+y^2$-ийн утгыг ол.
**Options:** **A)** $25$  **B)** $13$  **C)** $20$  **D)** $26$  **E)** $37$
**Correct answer:** D
**Current classification:** skill_tag=`matrix_inverse` · difficulty=`hard` · confidence=`0.9` · classifier=`in-chat`
**Rationale:** A + 9A^(-1) = 6E variant.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 111. Test-2021C-Q14 — *matrix_inverse*
**Body:** $M=\begin{pmatrix}-4 & -3 \\ 6 & 4\end{pmatrix}$ бол $M^{-1}$ матрицыг олоорой.
**Options:** **A)** $\begin{pmatrix}4 & 3 \\ -6 & -4\end{pmatrix}$  **B)** $\begin{pmatrix}-4 & 6 \\ -3 & 4\end{pmatrix}$  **C)** $\begin{pmatrix}2 & 3 \\ -1.5 & -2\end{pmatrix}$  **D)** $\begin{pmatrix}2 & -1.5 \\ -3 & 2\end{pmatrix}$  **E)** $\begin{pmatrix}2 & 1.5 \\ -3 & -2\end{pmatrix}$
**Correct answer:** E
**Current classification:** skill_tag=`matrix_inverse` · difficulty=`easy` · confidence=`0.9` · classifier=`rule`
**Rationale:** subtopic match (subtopic='matrix_inverse')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 112. Test-2022A-Q5 — *matrix_operation*
**Body:** $A = \begin{pmatrix} 3 & 1 \end{pmatrix}$ ба $B = \begin{pmatrix} 2 & 3 \\ -3 & -8 \end{pmatrix}$ бол $A \times B$ үржвэр матрицын хэмжээсийг олоорой.
**Options:** **A)** $3 \times 1$  **B)** $1 \times 1$  **C)** $2 \times 1$  **D)** $2 \times 2$  **E)** $1 \times 2$
**Correct answer:** E
**Current classification:** skill_tag=`matrix_operation` · difficulty=`easy` · confidence=`0.8` · classifier=`rule`
**Rationale:** keyword: matrix op (subtopic='matrix dimensions')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 113. Test-1B-Q32 — *matrix_operation*
**Body:** $A = \begin{pmatrix} -3 & x \\ y+2 & 4 \end{pmatrix}$ ба $B = \begin{pmatrix} x-2 & 1 \\ y & -3 \end{pmatrix}$ матрицууд өгөгдөв. $A - B$ матрицыг ол.
**Options:** **A)** $\begin{pmatrix} x-5 & x-1 \\ 2 & 7 \end{pmatrix}$  **B)** $\begin{pmatrix} -x-1 & x-1 \\ 2 & 1 \end{pmatrix}$  **C)** $\begin{pmatrix} -x-5 & x-1 \\ -2 & 7 \end{pmatrix}$  **D)** $\begin{pmatrix} -x-1 & x-1 \\ 2 & 7 \end{pmatrix}$  **E)** $\begin{pmatrix} -x-1 & x+1 \\ 2 & 7 \end{pmatrix}$
**Correct answer:** D
**Current classification:** skill_tag=`matrix_operation` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Compute A−B element-wise. Variant of Q1A-Q32.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 114. Test-1A-Q32 — *matrix_operation*
**Body:** $A = \begin{pmatrix} -2 & x \\ y-1 & 3 \end{pmatrix}$ ба $B = \begin{pmatrix} x+1 & x-3 \\ 4 & y-2 \end{pmatrix}$ матрицууд өгөгдөв. $A+B$ матрицыг ол.
**Options:** **A)** $\begin{pmatrix} x-1 & x-3 \\ y+2 & y+1 \end{pmatrix}$  **B)** $\begin{pmatrix} x-1 & 2x-3 \\ y+3 & y \end{pmatrix}$  **C)** $\begin{pmatrix} x-1 & 2x-3 \\ y+3 & y+1 \end{pmatrix}$  **D)** $\begin{pmatrix} x-2 & x-3 \\ y+2 & y \end{pmatrix}$  **E)** $\begin{pmatrix} x-1 & 2x-3 \\ y+2 & y \end{pmatrix}$
**Correct answer:** C
**Current classification:** skill_tag=`matrix_operation` · difficulty=`easy` · confidence=`0.95` · classifier=`in-chat`
**Rationale:** Compute A+B element-wise for two 2×2 matrices with variable entries. No determinant, no inverse — matrix_operation by definition.
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation

### 115. Test-2022B-Q5 — *matrix_operation*
**Body:** $A=\begin{pmatrix}1 & -2\\2 & -3\end{pmatrix}$ ба $B=\begin{pmatrix}3\\1\end{pmatrix}$ бол $A\times B$ үржвэр матрицын хэмжээсийг олоорой.
**Options:** **A)** $2\times 2$  **B)** $1\times 1$  **C)** $1\times 2$  **D)** $2\times 1$  **E)** $1\times 3$
**Correct answer:** D
**Current classification:** skill_tag=`matrix_operation` · difficulty=`easy` · confidence=`0.8` · classifier=`rule`
**Rationale:** keyword: matrix op (subtopic='matrix_dimensions')
**Decision:** ☐ approve · ☐ change to: `_______` · ☐ flag escalation
