# MN authoring brief — Determinants, Inverses & Systems

**Topic** `vectors-matrices/determinants-and-inverses` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `vectors-matrices/determinants-and-inverses`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-determinant`

**Able to:** Compute 2×2 determinants, interpret det as the area scale factor, and use det = 0 as the singularity/parallel-columns test.

**The idea that carries it:** det = ad − bc: the area scale factor (sign = orientation flip); det = 0 ⇔ parallel columns ⇔ no inverse.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding instead of subtracting: ad + bc.
- Forgetting the absolute value for areas.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm61-we1` — Compute $\det\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$.
- `vm61-we2` — A triangle of area $9$ is transformed by $M = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}$. Find the image's area.
- `vm61-we3` — For which $k$ is $\begin{pmatrix} 2 & k \\ 3 & 6 \end{pmatrix}$ singular (determinant zero)?

**2 try-it problems**, same freedom and same condition.

### 2. `the-inverse-matrix`

**Able to:** Compute 2×2 inverses via the swap-negate-divide recipe, verify with AA⁻¹ = I, and use det ≠ 0 as the existence test.

**The idea that carries it:** A⁻¹ = (1/det)·(swap diagonal, negate anti-diagonal); exists ⇔ det ≠ 0; verify with AA⁻¹ = I.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping the anti-diagonal and negating the main one.
- Forgetting to divide by the determinant.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm62-we1` — Find the inverse of $A = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$.
- `vm62-we2` — Find the inverse of $B = \begin{pmatrix} 4 & 7 \\ 1 & 2 \end{pmatrix}$.
- `vm62-we3` — Does $C = \begin{pmatrix} 2 & 6 \\ 3 & 9 \end{pmatrix}$ have an inverse? Solve, then explain geometrically.

**2 try-it problems**, same freedom and same condition.

### 3. `solving-systems-with-matrices`

**Able to:** Rewrite 2×2 systems as AX = B, solve via X = A⁻¹B, and use Cramer's rule as the determinant shortcut.

**The idea that carries it:** System = AX = B; solve X = A⁻¹B, or Cramer: x = det Aₓ/det A, y = det A_y/det A; det = 0 flags no-unique-solution.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying by A⁻¹ on the wrong side.
- Replacing the wrong column in Cramer's rule.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm63-we1` — Solve with an inverse: $\begin{cases} 3x + 5y = 1 \\ x + 2y = 0 \end{cases}$
- `vm63-we2` — Solve by Cramer's rule: $\begin{cases} 2x + y = 7 \\ x - 3y = -7 \end{cases}$
- `vm63-we3` — For which $k$ does $\begin{cases} 2x + 3y = 5 \\ 4x + ky = 7 \end{cases}$ FAIL to have a unique solution?

**2 try-it problems**, same freedom and same condition.

### 4. `matrices-as-transformations`

**Able to:** Move fluently between the four readings: matrix as transformation, product as composition, determinant as area factor, inverse as undo.

**The idea that carries it:** Columns = where (1,0),(0,1) go; BA = A then B; det multiplies under composition; inverse = the undo when det ≠ 0.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading BA as 'B first, then A'.
- Adding determinants under composition.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm64-we1` — Build the matrix that rotates $90°$ counter-clockwise and then doubles every length.
- `vm64-we2` — $A$ reflects over the $x$-axis, $B$ rotates $90°$ CCW. Compute $BA$ and $AB$ applied to $(1, 0)$ — same?
- `vm64-we3` — $T = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$ maps a square of area $2$; then $S$ with $\det S = \tfrac{1}{2}$ is applied. Find the final area, a

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
| factor | **хуваагч** | ministry standard |
| scale | **томсгох** | already on the site |
| area | **талбай** | ministry standard |
| product | **үржвэр** | ministry standard |
| parallel | **параллель** | ministry standard |
| system | **систем** | ministry standard |
| formula | **томьёо** | ministry standard |
| form | **хэлбэр** | ministry standard |
| divide | **хуваах** | ministry standard |
| column | **багана** | already on the site |
| inverse | **урвуу** | ministry standard |
| test | **шалгалт** | ministry standard |
| sign | **тэмдэг** | ministry standard |
| transformation | **хувиргалт** | ministry standard |
| capstone | **нэгтгэх хичээл** | already on the site |
| determinant | **тодорхойлогч** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## the-determinant

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm61-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm61-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-inverse-matrix

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm62-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm62-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm61-we1` and so on) exactly
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

