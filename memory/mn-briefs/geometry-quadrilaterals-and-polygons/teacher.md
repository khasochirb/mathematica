# MN authoring brief — Quadrilaterals & Polygons

**Topic** `geometry/quadrilaterals-and-polygons` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/quadrilaterals-and-polygons`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `angles-of-polygons`

**Able to:** Find the interior angle sum (n − 2)·180° of any polygon, use the fact that the exterior angles of any convex polygon total 360°, and find each interior and exterior angle of a regular polygon.

**The idea that carries it:** An n-gon's interior angles sum to (n − 2)·180° because it splits into n − 2 triangles from one vertex. The exterior angles always total 360°, so a regular n-gon has 360/n at each exterior angle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying $n \times 180$ instead of $(n-2)\times 180$.
- Dividing the interior sum by $n$ for a polygon that isn't regular.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pa-we1` — Find the interior angle sum of a hexagon ($n = 6$).
- `pa-we2` — Find each interior angle of a REGULAR octagon ($n = 8$).

**2 try-it problems**, same freedom and same condition.

### 2. `parallelograms`

**Able to:** Identify a parallelogram and use its four properties: opposite sides congruent, opposite angles congruent, consecutive angles supplementary, and diagonals that bisect each other.

**The idea that carries it:** A parallelogram has both pairs of opposite sides parallel. Then opposite sides and opposite angles are congruent, consecutive angles are supplementary, and the diagonals bisect each other.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking ALL four sides of a parallelogram are equal.
- Treating consecutive angles as congruent.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pg-we1` — In parallelogram $ABCD$, side $AB = 9$. Find the opposite side $DC$.
- `pg-we2` — One angle of a parallelogram is $70^\circ$. Find a consecutive angle.

**2 try-it problems**, same freedom and same condition.

### 3. `proving-parallelograms`

**Able to:** Use the five conditions that prove a quadrilateral is a parallelogram — each the converse of a property from the previous lesson.

**The idea that carries it:** Five converse tests each prove a quadrilateral is a parallelogram: both pairs of opposite sides parallel, or both pairs congruent, or both pairs of opposite angles congruent, or diagonals bisecting each other, or one pair of sides both parallel and congruent.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking one pair of sides merely PARALLEL is enough.
- Requiring all five tests to pass.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pp-we1` — A quadrilateral has both pairs of opposite sides congruent ($AB = DC$ and $BC = AD$). Is it a parallelogram?
- `pp-we2` — In quadrilateral $ABCD$, the diagonals bisect each other, cutting into halves of $5, 5$ and $8, 8$. Parallelogram?

**2 try-it problems**, same freedom and same condition.

### 4. `rectangles-rhombi-squares`

**Able to:** Use the special properties of rectangles (four right angles, congruent diagonals), rhombi (four congruent sides, perpendicular diagonals that bisect the angles), and squares (all of the above).

**The idea that carries it:** Rectangle = parallelogram + 4 right angles (congruent diagonals). Rhombus = parallelogram + 4 equal sides (perpendicular diagonals that bisect the angles). Square = both at once.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking a rhombus has congruent diagonals like a rectangle.
- Believing every rectangle is a square.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sp-we1` — A rectangle's diagonal $AC = 13$. Find the other diagonal $BD$.
- `sp-we2` — A rhombus has side length $7$. Find its perimeter.

**2 try-it problems**, same freedom and same condition.

### 5. `trapezoids-and-kites`

**Able to:** Identify trapezoids (exactly one pair of parallel sides), isosceles trapezoids (congruent legs, congruent base angles and diagonals), the trapezoid midsegment (average of the bases), and kites (two pairs of consecutive congruent sides, perpendicular diagonals).

**The idea that carries it:** A trapezoid has exactly one pair of parallel sides; its midsegment is the average of the two bases. An isosceles trapezoid adds congruent legs, base angles, and diagonals. A kite has two pairs of consecutive equal sides and perpendicular diagonals.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling a parallelogram a trapezoid (or vice versa).
- Thinking a kite's equal sides are opposite each other.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tk-we1` — A trapezoid has bases $8$ and $12$. Find its midsegment.
- `tk-we2` — An isosceles trapezoid has a bottom base angle of $72^\circ$. Find the other bottom base angle.

**2 try-it problems**, same freedom and same condition.

### 6. `the-quadrilateral-family`

**Able to:** Place any quadrilateral in the family hierarchy, name it as specifically as possible, and reason about which properties a shape must, might, or can never have.

**The idea that carries it:** Quadrilaterals form a hierarchy: square ⊂ rectangle & rhombus ⊂ parallelogram ⊂ quadrilateral, with trapezoids and kites on separate branches. A shape inherits every property of every type above it; name it by its most specific type.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Naming a shape by a general type when a specific one fits.
- Saying 'a rectangle is a square'.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `qf-we1` — A quadrilateral has four right angles and four equal sides. Name it as specifically as possible.
- `qf-we2` — True or false: every rhombus is a parallelogram.

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
| shape | **дүрс** | ministry standard |
| base | **суурь** | ministry standard |
| angle | **өнцөг** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| parallelogram | **параллелограмм** | ministry standard |
| square | **квадрат** | ministry standard |
| rectangle | **тэгш өнцөгт** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| vertex | **орой** | ministry standard |
| side | **тал** | ministry standard |
| interior | **дотоод** | already on the site |
| total | **нийт** | already on the site |
| pair | **хос** | ministry standard |
| average | **дундаж** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

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
## angles-of-polygons

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pa-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pa-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## parallelograms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pg-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pg-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pa-we1` and so on) exactly
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

- **Дөрвөн өнцөгт ба олон өнцөгт** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

