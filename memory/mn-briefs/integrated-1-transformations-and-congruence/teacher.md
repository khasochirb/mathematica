# MN authoring brief — Transformations, Congruence & Proof

**Topic** `integrated-1/transformations-and-congruence` · **6 lessons** · 22 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/transformations-and-congruence`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `rigid-motions`

**Able to:** Apply a translation, reflection or rotation to a figure using its coordinate rule, predict the image, and explain why each preserves distance and angle.

**The idea that carries it:** Translations slide, reflections flip, rotations turn — and all three preserve every distance, so the image is congruent to the original. A dilation does not, so it is excluded.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reflecting across the x-axis by negating the first coordinate.
- Applying a 90° rotation as (y, x) rather than (−y, x).
- Calling a dilation a rigid motion because the shape looks the same.
- Applying a sequence of transformations in the wrong order.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u7-l1-we1` — Triangle $ABC$ has vertices $A(1, 2)$, $B(4, 2)$, $C(1, 6)$. Apply the translation $(x, y) \to (x + 3, y - 5)$ and verify a side length is preserved.
- `im1-u7-l1-we2` — Reflect the points $P(3, 5)$, $Q(-2, 4)$ and $R(0, -1)$ across the $x$-axis, then across the $y$-axis, and describe what happens to each.
- `im1-u7-l1-we3` — Rotate the point $A(3, 1)$ about the origin by $90°$, $180°$ and $270°$ anticlockwise, and check the distance from the origin is unchanged.
- `im1-u7-l1-we4` — A triangle has vertices $(0, 0)$, $(4, 0)$, $(0, 3)$, labelled anticlockwise. Apply a translation and then a reflection across the $y$-axis, and say w

**3 try-it problems**, same freedom and same condition.

### 2. `sequences-of-transformations-and-symmetry`

**Able to:** Apply a sequence of rigid motions and find the single motion equivalent to it, and describe a figure's line and rotational symmetry as the motions that carry it onto itself.

**The idea that carries it:** Apply a sequence one move at a time. Composing rigid motions gives a rigid motion, and a symmetry is simply a rigid motion that maps a figure onto itself.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assuming a sequence gives the same result in either order.
- Claiming a non-square rectangle has four lines of symmetry.
- Counting the 360° rotation as a rotational symmetry.
- Assuming line symmetry and rotational symmetry always come together.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u7-l2-we1` — Apply to $A(2, 3)$: first the translation $(x, y) \to (x + 4, y - 1)$, then the reflection across the $x$-axis. Then reverse the order and compare.
- `im1-u7-l2-we2` — Reflect the point $P(5, 2)$ across the $x$-axis and then across the $y$-axis. What single transformation has the same effect?
- `im1-u7-l2-we3` — Describe all the symmetry of a square, and of a rectangle that is not a square.
- `im1-u7-l2-we4` — Find the line and rotational symmetry of an equilateral triangle and of a regular hexagon, and state the general rule.

**3 try-it problems**, same freedom and same condition.

### 3. `congruence-and-triangle-criteria`

**Able to:** State the rigid-motion definition of congruence, use it to justify corresponding parts being equal, and apply the SSS, SAS and ASA criteria as consequences of the definition rather than as separate rules.

**The idea that carries it:** Congruent means some sequence of rigid motions carries one figure onto the other. Equal corresponding parts follow from that. SSS, SAS and ASA are the minimum information that forces such a sequence to exist.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using AAA as a congruence criterion.
- Applying SAS with an angle that is not between the two given sides.
- Ignoring the order of letters in a congruence statement.
- Treating 'same shape and size' as the definition rather than the consequence.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u7-l3-we1` — Triangle $ABC$ has $A(0,0)$, $B(4,0)$, $C(0,3)$. Triangle $DEF$ has $D(5,2)$, $E(9,2)$, $F(5,5)$. Show they are congruent by naming a rigid motion.
- `im1-u7-l3-we2` — In triangles $PQR$ and $XYZ$: $PQ = XY = 7$, $QR = YZ = 9$, and $\angle Q = \angle Y = 52°$. Are they congruent? Name the criterion.
- `im1-u7-l3-we3` — Two triangles have angles $50°$, $60°$, $70°$ and sides $5, 6, 7$ versus $10, 12, 14$. Are they congruent? Similar?
- `im1-u7-l3-we4` — Given $\triangle ABC \cong \triangle DEF$ with $AB = 8$, $BC = 11$, $\angle A = 43°$ and $\angle B = 61°$, find every remaining part of $\triangle DEF

**3 try-it problems**, same freedom and same condition.

### 4. `compass-and-straightedge-constructions`

**Able to:** Perform the standard compass-and-straightedge constructions — copying a segment, bisecting a segment and an angle, and erecting a perpendicular — and explain why each works using congruent triangles.

**The idea that carries it:** A compass guarantees equal distances by construction, so the triangles a construction creates have known equal sides — and SSS or SAS then proves the result exactly, with no measuring.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring with a ruler and calling the result a construction.
- Changing the compass opening partway through a step that requires it fixed.
- Opening the compass to less than half of AB for the perpendicular bisector.
- Erasing the construction arcs before submitting the work.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u7-l4-we1` — Describe how to copy segment $AB$ onto a ray starting at $P$, and explain why the copy is exact.
- `im1-u7-l4-we2` — Construct the perpendicular bisector of segment $AB$, and prove it passes through the midpoint at a right angle.
- `im1-u7-l4-we3` — Construct the bisector of $\angle BAC$ and prove the two halves are equal.
- `im1-u7-l4-we4` — Construct an equilateral triangle on a given segment $AB$, and prove all three sides are equal.

**3 try-it problems**, same freedom and same condition.

### 5. `proving-angle-theorems`

**Able to:** Prove and apply the vertical-angle theorem, the linear-pair relationship, and the corresponding, alternate and co-interior angle relationships formed when a transversal cuts parallel lines; and characterise the perpendicular bisector by equal distances.

**The idea that carries it:** A linear pair sums to $180°$; everything else in this lesson is a short chain of reasons from there. Vertical angles are equal always; corresponding, alternate and co-interior relationships need the lines to be PARALLEL.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using 'alternate angles are equal' without parallel lines.
- Confusing co-interior with alternate.
- Calling two angles vertical when they are not opposite.
- Proving something by measuring the diagram.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u7-l5-we1` — Two lines cross. One of the four angles measures $52°$. Find the other three, giving a reason for each.
- `im1-u7-l5-we2` — Lines $m$ and $n$ are parallel and a transversal crosses both. One co-interior angle measures $115°$. Find the other co-interior angle and the angle a
- `im1-u7-l5-we3` — A transversal cuts two lines. One pair of corresponding angles measures $3x + 10$ and $5x - 30$ degrees. Find $x$ if the lines are parallel, and state

**3 try-it problems**, same freedom and same condition.

### 6. `triangle-and-parallelogram-theorems`

**Able to:** Prove and apply the triangle angle-sum and exterior-angle theorems, the isosceles triangle theorem and its converse, the midsegment theorem, and the defining properties of a parallelogram.

**The idea that carries it:** The triangle angle sum is the parallel-line theorems applied once, and almost everything else here is one congruence away from it. A parallelogram's whole property list comes from drawing a single diagonal.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Making the midsegment equal to the side it is parallel to.
- Adding the exterior angle to all three interior angles.
- Assuming a quadrilateral is a parallelogram because it looks like one.
- Pairing an isosceles triangle's equal sides with the angles beside them.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u7-l6-we1` — A triangle has angles $2x$, $3x$ and $4x$ degrees. Find all three angles and classify the triangle.
- `im1-u7-l6-we2` — In triangle $ABC$, $AB = AC$ and $\angle A = 44°$. Find $\angle B$ and $\angle C$.
- `im1-u7-l6-we3` — In parallelogram $PQRS$, $\angle P = 3y + 15$ and the opposite angle $\angle R = 5y - 25$ degrees. Find $y$, then every angle of the parallelogram.

**3 try-it problems**, same freedom and same condition.

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
| angle | **өнцөг** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| parallelogram | **параллелограмм** | ministry standard |
| sequence | **дараалал** | ministry standard |
| proof | **баталгаа** | already on the site |
| distance | **зай** | ministry standard |
| time | **цаг** | already on the site |
| vertical | **босоо** | ministry standard |
| linear | **шугаман** | ministry standard |
| segment | **хэрчим** | already on the site |

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
## rigid-motions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u7-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u7-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## sequences-of-transformations-and-symmetry

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u7-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u7-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u7-l1-we1` and so on) exactly
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

