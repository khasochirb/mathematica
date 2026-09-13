# MN authoring brief — Transformation Matrices

**Topic** `vectors-matrices/transformation-matrices` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `vectors-matrices/transformation-matrices`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-transformation-matrix`

**Able to:** Turn a coordinate rule into a 2x2 matrix and back, and apply a matrix to a point or to every vertex of a figure.

**The idea that carries it:** x' = ax + by, y' = cx + dy IS the matrix (a b; c d) — and its columns are the images of (1,0) and (0,1).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the point as a row on the left of the matrix.
- Reading the matrix ROWS as the images of the unit points.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm71-we1` — A transformation of the plane is given by the rules $x' = 3x - y$ and $y' = 2x + 4y$. Write its matrix, then find the image of $(2; -1)$.
- `vm71-we2` — A transformation sends $(1; 0)$ to $(2; 5)$ and $(0; 1)$ to $(-3; 1)$. Write its matrix and its coordinate rules, then find the image of $(4; 2)$.
- `vm71-we3` — Apply $M = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$ to the triangle with vertices $(0; 0)$, $(3; 0)$ and $(0; 2)$. Find the image triangle and it

**2 try-it problems**, same freedom and same condition.

### 2. `reflections-and-rotations`

**Able to:** Write and use the matrices of reflections (in the axes, in y = x, in the origin) and of rotations about the origin, including a general angle.

**The idea that carries it:** Reflections: read the unit points. Rotations: R(θ) = (cos −sin; sin cos). det = −1 mirrors, det = +1 turns.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the clockwise matrix for a counter-clockwise turn.
- Treating reflection in the origin as a reflection in a line.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm72-we1` — Reflect the triangle with vertices $(2; 1)$, $(5; 1)$, $(2; 3)$ in the line $y = x$. Give the matrix and the image vertices.
- `vm72-we2` — Rotate $(3; -2)$ by $90°$ counter-clockwise about the origin. Then say where a $270°$ counter-clockwise rotation would send the same point.
- `vm72-we3` — Write the matrix of a $60°$ counter-clockwise rotation about the origin and use it to rotate $(2; 0)$.

**2 try-it problems**, same freedom and same condition.

### 3. `enlargement-and-translation`

**Able to:** Write a homothety (enlargement) as a matrix, handle a centre that is not the origin, and express a translation with a 3x3 homogeneous matrix.

**The idea that carries it:** Enlargement = kI (areas ×k²); off-centre = C + k(P − C); translation needs the 3×3 homogeneous matrix, because no 2×2 can move the origin.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling areas by k instead of k squared.
- Hunting for a 2x2 translation matrix.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm73-we1` — A homothety with centre at the origin and ratio $k = 3$ is applied to the triangle $(1; 2)$, $(4; 0)$, $(2; 5)$. Find the image vertices and the facto
- `vm73-we2` — A homothety has centre $C = (2; 1)$ and ratio $k = -2$. Find the image of $P = (5; 3)$.
- `vm73-we3` — Write the $3 \times 3$ homogeneous matrix of the translation by $(4; -3)$ and use it on $(2; 6)$. Then explain why no $2 \times 2$ matrix can perform 

**2 try-it problems**, same freedom and same condition.

### 4. `composing-and-identifying`

**Able to:** Compose transformations by multiplying their matrices in the correct order, and identify the transformation a given matrix performs.

**The idea that carries it:** Do T1 then T2 = M2·M1. To name a matrix: det, then column lengths, then send (1,0).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the composition in reading order.
- Calling every determinant-1 matrix a rotation.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm74-we1` — A figure is reflected in the $x$-axis and then rotated $90°$ counter-clockwise about the origin. Find the single matrix of the combined transformation
- `vm74-we2` — Name the transformation with matrix $\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$.
- `vm74-we3` — Name the transformation for each matrix: $A = \begin{pmatrix} -3 & 0 \\ 0 & -3 \end{pmatrix}$ and $B = \begin{pmatrix} \tfrac{3}{5} & \tfrac{4}{5} \\ 

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
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| number | **тоо** | ministry standard |
| centre | **төв** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| unit | **нэгж** | ministry standard |
| point | **цэг** | ministry standard |
| form | **хэлбэр** | ministry standard |
| vertex | **орой** | ministry standard |
| coordinate | **координат** | ministry standard |
| length | **урт** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |

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
## the-transformation-matrix

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm71-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm71-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## reflections-and-rotations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm72-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm72-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm71-we1` and so on) exactly
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

---

## Who arrives here

The site sends students to this topic when the analytics find a weakness in:

- **Хувиргалтын матриц** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

