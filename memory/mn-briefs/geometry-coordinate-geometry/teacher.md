# MN authoring brief — Coordinate Geometry

**Topic** `geometry/coordinate-geometry` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/coordinate-geometry`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `distance-formula`

**Able to:** Find the exact straight-line distance between two points with $d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$, and see it is the Pythagorean theorem applied to the horizontal and vertical gaps.

**The idea that carries it:** Distance IS the hypotenuse of the right triangle whose legs are the horizontal and vertical gaps: d = √((x₂−x₁)² + (y₂−y₁)²) — the Pythagorean theorem solved for c.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding the legs instead of squaring first.
- Stopping at the sum of squares.
- Sign slips on negative coordinates.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `di-we1` — Find the distance from $(0, 0)$ to $(3, 4)$.
- `di-we2` — Find the distance from $(-2, -1)$ to $(6, 5)$.

**2 try-it problems**, same freedom and same condition.

### 2. `midpoint-formula`

**Able to:** Find the midpoint of a segment by averaging the endpoints, $M = \left(\tfrac{x_1+x_2}{2}, \tfrac{y_1+y_2}{2}\right)$, and run it backward to recover a missing endpoint.

**The idea that carries it:** The midpoint is the average of the endpoints: add the x's and halve, add the y's and halve, each coordinate on its own. It ADDS where distance SUBTRACTS.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Subtracting instead of adding.
- Forgetting to divide by 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `mi-we1` — Find the midpoint of $(2, 3)$ and $(8, 7)$.
- `mi-we2` — $A(2,3)$ and midpoint $M(5,5)$ are known. Find endpoint $B$.

**2 try-it problems**, same freedom and same condition.

### 3. `slope`

**Able to:** Compute slope as $m = \dfrac{\text{rise}}{\text{run}} = \dfrac{y_2-y_1}{x_2-x_1}$, and classify it as positive, negative, zero, or undefined.

**The idea that carries it:** Slope = rise/run = (y₂−y₁)/(x₂−x₁), the y-difference on top and the x-difference on the bottom in a matching order. Horizontal → 0; vertical → undefined.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Flipping to run over rise.
- Mismatched subtraction order.
- Calling a vertical line 'slope 0'.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sl-we1` — Find the slope through $(1, 2)$ and $(4, 11)$.
- `sl-we2` — Find the slope through $(2, 7)$ and $(5, 1)$.

**2 try-it problems**, same freedom and same condition.

### 4. `parallel-and-perpendicular-lines`

**Able to:** Use slopes to decide whether two lines are parallel, perpendicular, or neither, and find a perpendicular slope with the negative-reciprocal rule.

**The idea that carries it:** Compare slopes. Equal slopes → parallel. Negative reciprocals (flip and negate, product −1) → perpendicular. A horizontal and a vertical line are perpendicular by sight.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Taking the reciprocal but forgetting the sign.
- Negating without flipping.
- Calling equal-slope lines perpendicular.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pp-we1` — Line $AB$ through $(1,1),(4,3)$ and line $CD$ through $(0,5),(3,7)$. Parallel, perpendicular, or neither?
- `pp-we2` — A line has slope $\tfrac{2}{3}$. What slope is perpendicular to it?

**2 try-it problems**, same freedom and same condition.

### 5. `equations-of-lines`

**Able to:** Write a line as $y = mx + b$ from a slope and a point or from two points, use point-slope form, and apply the parallel/perpendicular conditions.

**The idea that carries it:** Every non-vertical line is y = mx + b. Find the slope m first, then use one known point to solve for b — two numbers fix the whole line.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping $m$ and $b$.
- Stopping at $y = mx$.
- Sign errors in point-slope.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `eq-we1` — Write the equation of the line through $(1, 3)$ and $(4, 9)$.
- `eq-we2` — Write the line through $(2, 5)$ with slope $4$ (point-slope).

**2 try-it problems**, same freedom and same condition.

### 6. `equations-of-circles-and-coordinate-proofs`

**Able to:** Write and read a circle's equation $(x-h)^2 + (y-k)^2 = r^2$, test whether a point lies on it, and write a coordinate proof that fuses distance, midpoint, and slope.

**The idea that carries it:** A circle's equation is 'distance from the center = r' squared: (x−h)² + (y−k)² = r². The same distance–midpoint–slope toolkit proves classic theorems by turning a picture into coordinates.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Getting the center's sign wrong.
- Confusing $r$ with $r^2$.
- Choosing coordinates that assume the conclusion.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-we1` — Write the equation of the circle with center $(2, -3)$ and radius $4$.
- `cp-we2` — Capstone: right triangle $A(0,0)$, $B(6,0)$, $C(0,8)$. Show the midpoint $M$ of hypotenuse $BC$ is the same distance from all three vertices.

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
| equation | **тэгшитгэл** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| geometry | **геометр** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| parallel | **параллель** | ministry standard |
| slope | **налалт** | ministry standard |
| proof | **баталгаа** | already on the site |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| zero | **тэг** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| formula | **томьёо** | ministry standard |

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
## distance-formula

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED di-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY di-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## midpoint-formula

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED mi-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY mi-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`di-we1` and so on) exactly
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

