# MN authoring brief — Systems in Three Unknowns

**Topic** `vectors-matrices/systems-in-three-unknowns` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

---

## You are not translating. You are teaching.

Do not open the English topic and render it sentence by sentence — that
produces the stiff textbook Mongolian this whole programme exists to avoid.
Read this brief, decide how **you** would teach these lessons to a Mongolian
student, and write that.

A different sentence count is expected. Different worked examples are
allowed. A different order *inside* a lesson is yours to choose. A different
explanation, a different analogy, a different joke — that is the point.

What you may not change is in the Build brief, and Build enforces it. You do
not need to read that document.

---

## What this topic must teach

> **← the argument for what matters most in this topic is not written yet.**
> Two or three ideas that carry the topic, and the place students reliably
> break, go in `data/i18n/mn-brief-theses.json` under the key
> `vectors-matrices/systems-in-three-unknowns`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `augmented-matrices-and-row-operations`

**Able to:** Write a three-unknown system as an augmented matrix, apply the three elementary row operations, and read what a row of zeros is telling you.

**The idea that carries it:** A three-unknown system is a 3×4 grid; swap, scale and add rows freely — the solution set never changes; a zero row reports 'no solution' or 'infinitely many'.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the zero for a missing unknown.
- Multiplying a row by zero to make an entry vanish.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm81-we1` — Write the system $\begin{cases} 2x + 3y - z = 7 \\ x - y + 4z = -2 \\ 3x + 2z = 5 \end{cases}$ as an augmented matrix.
- `vm81-we2` — Starting from $\left(\begin{array}{ccc|c} 1 & 2 & -1 & 3 \\ 2 & 5 & 1 & 8 \\ 0 & 1 & 3 & 5 \end{array}\right)$, use the first row to clear the $x$ fro
- `vm81-we3` — Two rows of a reduced system read $\left(\begin{array}{ccc|c} 0 & 1 & 3 & 2 \\ 0 & 1 & 3 & 5 \end{array}\right)$. What does the system say, and what d

**2 try-it problems**, same freedom and same condition.

### 2. `gaussian-elimination`

**Able to:** Solve a three-unknown linear system by forward elimination to triangular form and back substitution, and recognise systems with no solution or infinitely many.

**The idea that carries it:** Clear column one, then column two, then back-substitute from the bottom row; a zero row reports no solution or a free unknown.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying a row operation to the coefficients but not the constant.
- Checking the solution in an equation you already used to find it.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm82-we1` — Solve $\begin{cases} x + 2y + z = 9 \\ 2x + y - z = 3 \\ 3x - y + 2z = 8 \end{cases}$ by Gauss's method.
- `vm82-we2` — Solve $\begin{cases} x + y + z = 6 \\ 2x - y + 3z = 9 \\ x + 4y - z = 3 \end{cases}$.
- `vm82-we3` — Solve $\begin{cases} x - y + 2z = 3 \\ 2x - 2y + 4z = 7 \\ x + y - z = 1 \end{cases}$, or show that no solution exists.

**2 try-it problems**, same freedom and same condition.

### 3. `determinants-of-3x3-matrices`

**Able to:** Compute a 3x3 determinant by expansion along a row or column, and find a 3x3 inverse by row-reducing the matrix beside the identity.

**The idea that carries it:** Expand a 3×3 determinant into three 2×2 minors with signs + − +; det ≠ 0 ⇔ an inverse exists; find it by row-reducing (A | I).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the minus sign on the middle term.
- Computing a minor from the wrong four entries.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm83-we1` — Compute $\det A$ for $A = \begin{pmatrix} 2 & -1 & 3 \\ 0 & 4 & 1 \\ 5 & 2 & -2 \end{pmatrix}$ by expanding along the first row.
- `vm83-we2` — Expand $\det B$ for $B = \begin{pmatrix} 3 & 0 & 0 \\ 7 & -2 & 5 \\ 1 & 6 & 4 \end{pmatrix}$ along the row or column that makes the work smallest.
- `vm83-we3` — Find the inverse of $A = \begin{pmatrix} 1 & 0 & 2 \\ 2 & -1 & 3 \\ 4 & 1 & 8 \end{pmatrix}$ by row-reducing $(A \mid I)$.

**2 try-it problems**, same freedom and same condition.

### 4. `cramers-rule-in-three-unknowns`

**Able to:** Solve a three-unknown system with Cramer's rule, and know precisely when the rule applies and when elimination is the only way through.

**The idea that carries it:** x = Dx/D, y = Dy/D, z = Dz/D, where Dx replaces the x-column with the constants — and only when D ≠ 0.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Replacing a row instead of a column.
- Reading D = 0 as 'no solution'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm84-we1` — Solve $\begin{cases} 2x + y - z = 5 \\ x - y + 2z = 3 \\ 3x + 2y + z = 14 \end{cases}$ by Cramer's rule.
- `vm84-we2` — For $\begin{cases} x + 2y + z = 4 \\ 2x - y + 3z = 1 \\ 3x + y + 4z = 5 \end{cases}$, compute the coefficient determinant and say what Cramer's rule c
- `vm84-we3` — Find only $z$ for the system $\begin{cases} x + y + z = 6 \\ 2x - y + z = 3 \\ x + 2y - z = 2 \end{cases}$.

**2 try-it problems**, same freedom and same condition.

---

## What you owe for every example you change

A worked example or try-it problem with different numbers needs a new
**check** — a line of maths that says what must be true, so we can verify it
mechanically without a second person re-solving it.

**You do not write these.** Write the example and its answer in plain
Mongolian, and Build turns it into the assertion. If an example's answer
cannot be stated exactly, the example is not ready.

**Practice and test-yourself problems are different: do not change their
numbers.** Those are graded against a stored answer key and every student's
history is keyed to them. Rewrite the *wording* freely; leave the maths.

---

## Money

Worked examples and try-it problems use **₮ (tögrög)** with realistic
Mongolian amounts. Rewrite the numbers to suit; Build rewrites the check.

Practice and test-yourself keep their original currency and figures,
because they are graded.

---

## Terms that are not yours to choose

Fixed by ministry order А/492 or by Mongolian already shipped on the site.
Using a different word for one of these is the fastest way to make the site
feel like two different products.

| English | Use | Why |
|---|---|---|
| scale | **томсгох** | already on the site |
| zero | **тэг** | ministry standard |
| system | **систем** | ministry standard |
| identity | **адилтгал** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| linear | **шугаман** | ministry standard |
| form | **хэлбэр** | ministry standard |
| constant | **тогтмол** | ministry standard |
| column | **багана** | already on the site |
| pattern | **хэв маяг** | already on the site |
| no solution | **шийдгүй** | already on the site |
| inverse | **урвуу** | ministry standard |
| sign | **тэмдэг** | ministry standard |
| change | **өөрчлөлт** | ministry standard |
| grid | **тор** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**Section headings** are fixed too, because the shipped lessons already use
them and a student should meet the same words in every lesson:

**Бодсон жишээнүүд** · **Өөрөө туршиж үз** · **Түргэн шалгалт** · **Тоглож үз** · **Сонирхолтой баримт** · **Эргэн дүгнэлт** · **Юу сурснаа эргэн харъя**

Introducing a term that is not here? Tell us — it goes in the glossary so the
next topic uses the same word.

---

## What to hand back

Plain text or a document — **not** JSON, and nothing needs to look like
code. One block per lesson, in the order above. Use the lesson’s slug as
its heading so Build can match it up; everything else is prose.

```
## augmented-matrices-and-row-operations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm81-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm81-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## gaussian-elimination

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm82-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm82-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm81-we1` and so on) exactly
as they appear. They are how the site connects your example to the student
who answered it; the numbers inside are yours to change, the id is not.

**The ANSWER line matters more than it looks.** Build turns it into a check
the computer runs, so it has to be exact — write $\frac{3}{4}$ or
$2\sqrt{5}$ rather than 0.75 or 4.47, unless the answer really is a
rounded decimal, in which case say so.

For the practice and test-yourself sets at the end of the topic, hand back
**only the wording** — their numbers and answers stay as they are.

---

## How it should sound

**«та», formal.** A student on this product is a customer, and «чи» is not
suitable for one. Formal is not the same as stiff — the English has jokes and
energy, and that should survive. Do not flatten it into textbook prose.

Quotes take «...». Proper names take their standard Mongolian forms. Product
names and symbols stay Latin.

> Note if you have seen earlier material: grades 6 and 7 are written in «чи»,
> which is now the wrong register. Do not copy their tone.

---

## Writing maths

Only the rules that change what you type:

1. **Do not put Mongolian words inside a formula.** Write the formula in
   symbols and the words outside it. (If a word truly must sit inside one,
   mark it and Build will wrap it correctly.)
2. **Letters stay Latin** — `x`, `h`, point names, function names — even in
   Mongolian prose. Gloss one on first use if it helps.
3. **Bold is `**like this**`.** Single asterisks do not work and will appear
   on screen as asterisks.
4. **Units:** см, кг, мл read fine in a sentence.

