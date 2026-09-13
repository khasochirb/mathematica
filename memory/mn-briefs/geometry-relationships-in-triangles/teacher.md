# MN authoring brief — Relationships in Triangles

**Topic** `geometry/relationships-in-triangles` · **7 lessons** · 15 worked examples · 8 practice · 6 test-yourself

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
> `geometry/relationships-in-triangles`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `perpendicular-bisectors-and-circumcenter`

**Able to:** Identify the perpendicular bisector of a segment, apply the Perpendicular Bisector Theorem (a point is equidistant from the two endpoints exactly when it lies on their perpendicular bisector), and locate the circumcenter where a triangle's three perpendicular bisectors meet.

**The idea that carries it:** A point is equidistant from a segment's two endpoints exactly when it lies on their perpendicular bisector. A triangle's three perpendicular bisectors are concurrent at the circumcenter, which is equidistant from all three vertices.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking the perpendicular bisector of a side must pass through the opposite vertex.
- Assuming the circumcenter is always inside the triangle.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-we1` — Point $P$ lies on the perpendicular bisector of $\overline{AB}$. If $PA = 2x + 1$ and $PB = 11$, find $x$.
- `pb-we2` — The circumcenter of a right triangle lands on the midpoint of the hypotenuse. If the hypotenuse is $10$, find the circumradius (distance from the circ

**2 try-it problems**, same freedom and same condition.

### 2. `angle-bisectors-and-incenter`

**Able to:** Apply the Angle Bisector Theorem (a point on an angle's bisector is equidistant from the two sides of the angle), and locate the incenter where a triangle's three angle bisectors meet.

**The idea that carries it:** A point is equidistant from an angle's two sides exactly when it lies on the angle bisector. A triangle's three angle bisectors are concurrent at the incenter, equidistant from all three sides — the centre of the inscribed circle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the distance to a side along a slanted line.
- Mixing up the incenter and circumcenter.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ab-we1` — Point $P$ is on the bisector of $\angle A$. Its perpendicular distances to the two sides are $2x$ and $10$. Find $x$.
- `ab-we2` — The incenter $I$ is $4$ from side $\overline{AB}$. How far is $I$ from side $\overline{BC}$?

**2 try-it problems**, same freedom and same condition.

### 3. `medians-and-centroid`

**Able to:** Draw the medians of a triangle, locate the centroid where they meet, and use the fact that the centroid divides each median in a 2 : 1 ratio (twice as far from the vertex as from the midpoint).

**The idea that carries it:** A median joins a vertex to the midpoint of the opposite side. The three medians meet at the centroid — the balance point — which cuts each median in a 2 : 1 ratio (vertex piece : midpoint piece), so the vertex-to-centroid part is ⅔ of the median.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking the median hits the opposite side at a right angle.
- Splitting the median in half at the centroid.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `mc-we1` — A median is $18$ long. The centroid divides it $2:1$ from the vertex. Find the vertex-to-centroid distance.
- `mc-we2` — The centroid-to-midpoint part of a median is $5$. Find the vertex-to-centroid part.

**2 try-it problems**, same freedom and same condition.

### 4. `altitudes-and-orthocenter`

**Able to:** Draw the altitudes of a triangle, locate the orthocenter where they meet, connect an altitude to the area formula, and recognize that altitudes (and the orthocenter) can fall outside the triangle.

**The idea that carries it:** An altitude is a perpendicular segment from a vertex to the opposite side (the triangle's height). The three altitudes meet at the orthocenter, which lies inside an acute triangle, on the right-angle vertex of a right triangle, and outside an obtuse triangle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing an altitude with a median.
- Assuming the orthocenter is always inside.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ao-we1` — A triangle has base $8$ and the altitude to that base is $6$. Find the area.
- `ao-we2` — A triangle has area $30$ and base $10$. Find the altitude to that base.

**2 try-it problems**, same freedom and same condition.

### 5. `the-midsegment-theorem`

**Able to:** Use the Triangle Midsegment Theorem — a midsegment is parallel to the third side and half its length — to find missing lengths, and recognize the medial triangle.

**The idea that carries it:** A midsegment joins the midpoints of two sides; it is parallel to the third side and exactly half its length. The three midsegments form the medial triangle, splitting the original into four congruent triangles.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doubling when you should halve (or vice-versa).
- Thinking a midsegment connects a vertex to a midpoint.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ms-we1` — A midsegment is parallel to a side of length $14$. How long is the midsegment?
- `ms-we2` — A midsegment measures $9$. How long is the side it is parallel to?

**2 try-it problems**, same freedom and same condition.

### 6. `inequalities-in-one-triangle`

**Able to:** Order a triangle's sides and angles (largest angle opposite the longest side, and the converse), and apply the triangle inequality to find the possible range of a third side.

**The idea that carries it:** Sides and angles of a triangle rank in the same order: longest side opposite the largest angle. A missing third side lies strictly between the difference and the sum of the other two.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Matching the largest angle to the side next to it.
- Letting the third side equal the sum or the difference.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-we1` — A triangle has angles $50^\circ$, $60^\circ$, and $70^\circ$. Which side is longest?
- `in-we2` — Two sides of a triangle are $6$ and $10$. Find the range of the third side $x$.

**2 try-it problems**, same freedom and same condition.

### 7. `incircles-circumcircles-and-area`

**Able to:** Compute the inradius via A = rs and the circumradius via R = abc/4A, use the right-triangle shortcut r = (a + b − c)/2, and extend A = rs to any polygon with an inscribed circle.

**The idea that carries it:** r = A/s and R = abc/4A; right triangles shortcut to r = (a+b−c)/2 and R = c/2; A = rs works for every polygon that owns an incircle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the full perimeter in A = rs.
- Applying R = c/2 to a triangle that isn't right-angled.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `icc-we1` — Find the inradius and circumradius of the $3$–$4$–$5$ right triangle.
- `icc-we2` — A triangle has sides $13$, $14$, $15$. Find $r$ and $R$.
- `icc-we3` — A trapezoid has an inscribed circle of radius $4$ and area $72$. Find its perimeter and the sum of its two parallel sides.

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
| range | **далайц** | ministry standard |
| half | **хагас** | already on the site |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| median | **медиан** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| parallel | **параллель** | ministry standard |
| centre | **төв** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| formula | **томьёо** | ministry standard |
| midpoint | **дундаж цэг** | ministry standard |
| difference | **ялгавар** | ministry standard |
| point | **цэг** | ministry standard |
| segment | **хэрчим** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## perpendicular-bisectors-and-circumcenter

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pb-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pb-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## angle-bisectors-and-incenter

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ab-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ab-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pb-we1` and so on) exactly
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

