# MN authoring brief — Shapes & Symmetry

**Topic** `3/shapes-and-symmetry` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `3/shapes-and-symmetry`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `two-d-shapes`

**Able to:** Name 2-D shapes by counting their straight sides — triangle, quadrilateral, pentagon, hexagon — and check that every shape has exactly as many corners (vertices) as sides.

**The idea that carries it:** Count the straight sides: three is a triangle, four a quadrilateral, five a pentagon, six a hexagon — and the corners always match the count, side for side.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling every four-sided shape a square.
- Thinking a triangle standing on its point is a different shape.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4sh-l1-we1` — A shape has $5$ straight sides. Name it, and count its corners without looking at it.
- `g4sh-l1-we2` — A triangle and a hexagon are drawn side by side. How many sides in total — and how many corners in total?

**2 try-it problems**, same freedom and same condition.

### 2. `right-angles`

**Able to:** Recognise a right angle as a quarter turn, test corners with the page corner, and sort angles as smaller than, equal to, or bigger than a right angle.

**The idea that carries it:** A right angle is a quarter of a full turn — 90 degrees; two of them make a straight line (180) and four fill the whole turn (360). Test the corners with the page corner.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking a right angle tilted on its side stops being right.
- Judging an angle by the length of its arms — long arms, big angle.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4sh-l2-we1` — Four streets meet at a crossing, and every corner passes the page-corner test. Show that the four corners together make one full turn.
- `g4sh-l2-we2` — Two right angles sit side by side. What do they make together?

**2 try-it problems**, same freedom and same condition.

### 3. `sorting-quadrilaterals`

**Able to:** Sort quadrilaterals by their rules — four equal sides and four right angles for a square, right angles with opposite sides equal for a rectangle — and explain why every square is also a rectangle.

**The idea that carries it:** Sort by rules, not by looks: four straight sides makes a quadrilateral, right angles with opposite sides equal makes a rectangle, and equal sides on top of that makes a square — so every square is a rectangle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Saying a square is not a rectangle.
- Calling a square standing on its corner a "diamond" — a different shape.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4sh-l3-we1` — A square is drawn with corners at $(2, 2)$, $(8, 2)$, $(8, 8)$ and $(2, 8)$. Show that its bottom side and its left side really are equal.
- `g4sh-l3-we2` — A rectangle is drawn with corners at $(1, 1)$, $(9, 1)$, $(9, 5)$ and $(1, 5)$. Show its opposite sides are equal — and say why it is NOT a square.

**2 try-it problems**, same freedom and same condition.

### 4. `line-symmetry`

**Able to:** Use the fold test to find lines of symmetry, draw mirror lines through the true middle of a shape, and count the lines a shape has — 0 for a scalene triangle, 1 for an isosceles triangle, 2 for a rectangle, 4 for a square.

**The idea that carries it:** Try the fold: halves matching exactly make a line of symmetry, the line passes the true middle, and counting the folds that work gives each shape its symmetry number: scalene triangle 0, isosceles 1, rectangle 2, square 4.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Folding a rectangle along its diagonal and calling it a line of symmetry.
- Drawing the mirror line roughly near the middle.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4sh-l4-we1` — A rectangle (longer than it is wide) — how many lines of symmetry, and why are its diagonals NOT among them?
- `g4sh-l4-we2` — Count the lines of symmetry of the block letters A, H and F — and give the total.

**2 try-it problems**, same freedom and same condition.

### 5. `three-d-solids`

**Able to:** Name the six common solids — cube, cuboid, sphere, cylinder, cone, square pyramid — count faces, edges and vertices, and say which 2-D shape each flat face is.

**The idea that carries it:** Count three things — faces, edges, vertices — name each flat face with its 2-D shape, and receipt the count: faces plus vertices minus edges always makes 2.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Counting only the faces you can see in a drawing — calling a cube "3 faces".
- Mixing up edges and vertices.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4sh-l5-we1` — Count a dice: faces, edges, vertices — then run the receipt.
- `g4sh-l5-we2` — Count a square pyramid: faces, edges, vertices — and receipt it.

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
| edge | **ирмэг** | already on the site |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| number | **тоо** | ministry standard |
| cylinder | **цилиндр** | ministry standard |
| square | **квадрат** | ministry standard |
| counting | **тоолох** | ministry standard |
| cone | **конус** | ministry standard |
| sphere | **бөмбөрцөг** | ministry standard |
| cube | **шоо** | already on the site |
| halve | **хагаслах** | already on the site |
| rectangle | **тэгш өнцөгт** | ministry standard |
| opposite | **эсрэг** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## two-d-shapes

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g4sh-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g4sh-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## right-angles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g4sh-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g4sh-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g4sh-l1-we1` and so on) exactly
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

