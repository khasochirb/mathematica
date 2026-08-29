# MN authoring brief — Geometry — Shapes & Area

**Topic** `4/geometry-shapes-and-area` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `4/geometry-shapes-and-area`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `angles`

**Able to:** Measure and classify angles in degrees against the right-angle benchmark, and find missing angles on a straight line and around a point.

**The idea that carries it:** An angle measures turn, judged against the 90-degree right angle; straight lines carry 180 degrees and full turns 360, and missing angles fall out by subtraction.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Judging an angle by the length of its drawn arms.
- Using 360 for a straight line (or 180 for a full turn).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5ge-l1-we1` — Two angles share a straight line; one measures $65^\circ$. Find the other, and classify both.
- `g5ge-l1-we2` — Three angles meet around a point: $140^\circ$, $90^\circ$, and one unknown. Find it.

**2 try-it problems**, same freedom and same condition.

### 2. `triangles-and-quadrilaterals`

**Able to:** Classify triangles by sides and by angles, know the quadrilateral family, and use the angle budgets — 180 for triangles, 360 for quadrilaterals — to find missing angles.

**The idea that carries it:** Shapes carry fixed angle budgets — 180 degrees for triangles, 360 for quadrilaterals — and their names describe how sides and angles spend it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Refusing to call a square a rectangle.
- Using the 360 budget on a triangle.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5ge-l2-we1` — A right triangle has one angle of $35^\circ$. Find the third angle and classify the triangle by its angles.
- `g5ge-l2-we2` — A quadrilateral has angles $90^\circ$, $90^\circ$ and $110^\circ$. Find the fourth.

**2 try-it problems**, same freedom and same condition.

### 3. `perimeter`

**Able to:** Find perimeters of rectangles, squares and composite shapes by walking the boundary, use the rectangle shortcut, and work backwards to a missing side.

**The idea that carries it:** Perimeter walks the whole boundary once — rectangles shortcut it as twice length-plus-width, and missing sides come from running the shortcut backwards.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding only the two labelled sides — P of an 8 × 5 rectangle as 13.
- Forgetting to halve when working backwards — w = 30 − 9 = 21.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5ge-l3-we1` — Find the perimeter of an $8$ m by $5$ m paddock, and of a square pen with $7$ m sides.
- `g5ge-l3-we2` — A rectangle has perimeter $30$ cm and length $9$ cm. Find its width.

**2 try-it problems**, same freedom and same condition.

### 4. `area-of-rectangles`

**Able to:** Find areas of rectangles and squares in square units, keep area's units distinct from perimeter's, work back to a missing side, and see that equal perimeters can hold different areas.

**The idea that carries it:** Area is the count of unit squares — length times width, answered in square units — and rectangles sharing a perimeter can hold very different areas.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Answering area in linear units — "the area is 40 m".
- Assuming equal perimeters mean equal areas.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5ge-l4-we1` — A room is $8$ m by $5$ m. How many $1$ m² carpet tiles cover it — and what are the room's area and perimeter, with correct units?
- `g5ge-l4-we2` — Compare the $6 \times 4$ and $8 \times 2$ rectangles: perimeter and area of each.

**2 try-it problems**, same freedom and same condition.

### 5. `composite-areas`

**Able to:** Find areas of L-shaped and composite rectilinear figures by splitting into rectangles or subtracting the missing piece, recover unlabelled side lengths, and keep composite area and perimeter separate.

**The idea that carries it:** Composite areas travel two roads — split-and-add or fill-and-subtract — and the roads must agree; missing edges are differences of the labelled ones.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying the two biggest labels — the L-shape as 8 × 6 = 48.
- Double-counting the overlap when splitting.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5ge-l5-we1` — An L-shaped room is an $8 \times 6$ m rectangle with a $3 \times 2$ m bite out of one corner. Find its area by BOTH roads.
- `g5ge-l5-we2` — A T-shaped stage is a $10 \times 3$ m bar on top of a $4 \times 5$ m stem. Find its area, and note which road you used.

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
| count | **тоолох** | ministry standard |
| measure | **хэмжих** | ministry standard |
| edge | **ирмэг** | already on the site |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| geometry | **геометр** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| square | **квадрат** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| subtraction | **хасалт** | already on the site |
| perimeter | **периметр** | already on the site |
| formula | **томьёо** | ministry standard |
| rectangle | **тэгш өнцөгт** | ministry standard |
| difference | **ялгавар** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

**edge** — proposed **ирмэг**

> POLYSEMOUS, mildly. ирмэг is the edge of a solid (shipped and ЭШ alike) and, by extension, the edge of a histogram bin («ирмэг: $20$ нь $20$–$29$-ийг эхлүүлнэ») — that is the sense proposed here. Where "edge" means the margin of something written or laid out, shipped uses зах: "Line up the decimal points, not the right edges" → «Аравтын цэгүүдийг зэрэгцүүл, баруун захыг биш». So: ирмэг for geometry and bins, зах for the right-hand edge of a written column.

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
## angles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5ge-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5ge-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## triangles-and-quadrilaterals

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5ge-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5ge-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g5ge-l1-we1` and so on) exactly
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

