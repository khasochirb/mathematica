# MN authoring brief — Connecting Algebra & Geometry

**Topic** `integrated-1/coordinate-geometry` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/coordinate-geometry`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `distance-and-midpoint`

**Able to:** Compute the distance between two points and the midpoint of a segment from their coordinates, explain why each formula works, and use them to find the perimeter of a polygon.

**The idea that carries it:** Distance is $\sqrt{(\Delta x)^2 + (\Delta y)^2}$ — Pythagoras on the legs. Midpoint is the average of each coordinate. Distance subtracts; midpoint adds.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to take the square root at the end of the distance formula.
- Subtracting in the midpoint formula instead of adding.
- Adding the squares of the coordinates rather than of their differences.
- Halving only one coordinate when finding a midpoint.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u8-l1-we1` — Find the distance between $A(2, 3)$ and $B(7, 15)$.
- `im1-u8-l1-we2` — Find the midpoint of the segment joining $P(-4, 9)$ and $Q(6, 1)$, then verify it is equidistant from both.
- `im1-u8-l1-we3` — The midpoint of $AB$ is $M(3, -2)$ and $A$ is $(-1, 4)$. Find $B$.
- `im1-u8-l1-we4` — A triangle has vertices $A(0, 0)$, $B(6, 0)$ and $C(6, 8)$. Find its perimeter and area.

**3 try-it problems**, same freedom and same condition.

### 2. `parallel-and-perpendicular-lines`

**Able to:** Determine whether two lines are parallel, perpendicular or neither from their slopes; write the equation of a line parallel or perpendicular to a given line through a given point; and use the criteria to classify quadrilaterals.

**The idea that carries it:** Parallel ⟺ equal slopes. Perpendicular ⟺ slopes are negative reciprocals, product $-1$. Horizontal and vertical are the one perpendicular pair the product test cannot handle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Taking the reciprocal without changing the sign, or the sign without the reciprocal.
- Applying the product test to a horizontal and a vertical line.
- Calling two lines parallel when they are actually the same line.
- Reading a slope off standard form without rearranging.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u8-l2-we1` — Are the lines $y = \frac{2}{3}x + 5$ and $2x - 3y = 12$ parallel, perpendicular, or neither?
- `im1-u8-l2-we2` — Write the equation of the line through $(4, -1)$ perpendicular to $y = \frac{3}{5}x + 2$.
- `im1-u8-l2-we3` — A quadrilateral has vertices $A(1, 1)$, $B(5, 2)$, $C(6, 6)$, $D(2, 5)$. Classify it using slopes and lengths.
- `im1-u8-l2-we4` — Show that the triangle with vertices $P(1, 2)$, $Q(5, 4)$, $R(3, 8)$ is right-angled, and find its area.

**3 try-it problems**, same freedom and same condition.

### 3. `partitioning-a-segment`

**Able to:** Find the point dividing a directed segment in a given ratio, recognise the midpoint as the special case $1:1$, and interpret the ratio correctly as parts of the whole.

**The idea that carries it:** $P = A + t(B - A)$ coordinate-wise, with $t = \frac{m}{m+n}$ for a ratio $m:n$ from $A$ to $B$. The midpoint is $t = \frac{1}{2}$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading a ratio of 1:3 as one third of the way.
- Starting from the wrong endpoint.
- Multiplying the coordinates by t instead of the differences.
- Applying the fraction to only one coordinate.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u8-l3-we1` — Find the point one third of the way from $A(2, 3)$ to $B(11, 15)$.
- `im1-u8-l3-we2` — Find the point $P$ dividing the segment from $A(-3, 2)$ to $B(9, 8)$ in the ratio $1 : 3$.
- `im1-u8-l3-we3` — Find the point dividing $A(1, 6)$ to $B(13, -2)$ in the ratio $3 : 1$, and compare with the point for $1 : 3$.
- `im1-u8-l3-we4` — A pipeline runs from a pump at $(0, 0)$ to a tank at $(20, 15)$. A valve is needed $60\%$ of the way along. Find its position and its distance from th

**3 try-it problems**, same freedom and same condition.

### 4. `coordinate-proof`

**Able to:** Prove a simple geometric theorem by placing a figure on coordinate axes and computing with the distance, midpoint and slope formulas, using variables so the argument covers every case.

**The idea that carries it:** Place the figure conveniently, label with LETTERS so the proof covers every case, compute with distance, midpoint or slope, and finish with a sentence stating what was shown.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Proving the theorem with specific numbers instead of letters.
- Placing the figure awkwardly and drowning in algebra.
- Stopping at the final expression without stating the conclusion.
- Assuming a placement that is more special than the theorem allows.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u8-l4-we1` — Prove that the diagonals of any rectangle are equal in length.
- `im1-u8-l4-we2` — Prove that the diagonals of any parallelogram bisect each other.
- `im1-u8-l4-we3` — Prove that the segment joining the midpoints of two sides of a triangle is parallel to the third side and half its length.
- `im1-u8-l4-we4` — Prove that a triangle with vertices $(0,0)$, $(a, 0)$ and $(0, b)$ has its hypotenuse's midpoint equidistant from all three vertices.

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
| equation | **тэгшитгэл** | ministry standard |
| fraction | **бутархай** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| geometry | **геометр** | ministry standard |
| parallel | **параллель** | ministry standard |
| slope | **налалт** | ministry standard |
| proof | **баталгаа** | already on the site |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| plane | **хавтгай** | ministry standard |
| perimeter | **периметр** | already on the site |
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
## distance-and-midpoint

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u8-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u8-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## parallel-and-perpendicular-lines

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u8-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u8-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u8-l1-we1` and so on) exactly
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

