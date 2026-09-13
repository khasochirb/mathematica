# MN authoring brief — Area & Perimeter

**Topic** `geometry/area-and-perimeter` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/area-and-perimeter`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `area-of-parallelograms-and-triangles`

**Able to:** Find the area of a parallelogram (base × height) and a triangle (½ × base × height), using the perpendicular height rather than a slanted side.

**The idea that carries it:** Parallelogram area = base × height; triangle area = ½ × base × height. The height is the perpendicular distance to the base, never the slanted side.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the slanted side as the height.
- Forgetting the $\tfrac12$ for a triangle.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pt-we1` — A parallelogram has base $8$ and height $5$. Find its area.
- `pt-we2` — A triangle has base $10$ and height $6$. Find its area.

**2 try-it problems**, same freedom and same condition.

### 2. `area-of-trapezoids-rhombi-kites`

**Able to:** Find the area of a trapezoid using ½(b₁+b₂)·h and the area of a rhombus or kite using ½·d₁·d₂.

**The idea that carries it:** Trapezoid area = ½(b₁+b₂)·h (average base × height). Rhombus/kite area = ½·d₁·d₂ (half the product of the diagonals).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to average the two bases.
- Multiplying the full diagonals for a rhombus.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr-we1` — A trapezoid has bases $6$ and $10$ and height $4$. Find its area.
- `tr-we2` — A rhombus has diagonals $8$ and $6$. Find its area.

**2 try-it problems**, same freedom and same condition.

### 3. `area-of-regular-polygons`

**Able to:** Find the area of a regular polygon using ½ × apothem × perimeter.

**The idea that carries it:** A regular polygon splits into n triangles from the center, each with base = side and height = apothem. Total area = ½ · apothem · perimeter.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using a full side or a diagonal instead of the apothem.
- Forgetting to find the perimeter first.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rp-we1` — A regular polygon has apothem $6$ and perimeter $40$. Find its area.
- `rp-we2` — A regular hexagon has side $10$ and apothem $9$ (rounded). Find its area.

**2 try-it problems**, same freedom and same condition.

### 4. `circumference-circle-area-sectors`

**Able to:** Find the circumference (2πr), the area of a circle (πr²), and the area of a sector ((θ/360)·πr²), leaving answers in terms of π.

**The idea that carries it:** Circumference = 2πr; circle area = πr². A sector is the θ/360 fraction of the circle, so its area is (θ/360)·πr².

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the diameter as $r$ in the area formula.
- Squaring in the circumference formula.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ca-we1` — A circle has radius $5$. Find its circumference and area (in terms of π).
- `ca-we2` — A $90^\circ$ sector of a circle of radius $8$. Find its area.

**2 try-it problems**, same freedom and same condition.

### 5. `composite-figures`

**Able to:** Find the area of a composite figure by decomposing it into rectangles, triangles, and semicircles, then adding the parts.

**The idea that carries it:** To find a composite area, split the figure into simple shapes, find each area, and add them up.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Double-counting an overlapping length.
- Mixing up a piece's own base and height.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cf-we1` — A figure is a rectangle $12 \times 5$ with a triangle (base $12$, height $3$) on top. Find the total area.
- `cf-we2` — An L-shape is a $6 \times 4$ rectangle plus a $3 \times 2$ rectangle. Find the total area.

**2 try-it problems**, same freedom and same condition.

### 6. `shaded-regions-and-applications`

**Able to:** Find the area of a shaded region by subtracting an inner shape from an outer one, including rings (annuli), and apply area to real problems.

**The idea that carries it:** A shaded region = outer area − inner area. A ring is πR² − πr². Real 'leftover' area problems are subtractions.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding when you should subtract.
- Subtracting the radii instead of the areas.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sr-we1` — A square of side $10$ has a circle of radius $3$ cut out. Find the shaded area (in terms of π).
- `sr-we2` — A ring has outer radius $5$ and inner radius $3$. Find its area (in terms of π).

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
| half | **хагас** | already on the site |
| base | **суурь** | ministry standard |
| area | **талбай** | ministry standard |
| fraction | **бутархай** | ministry standard |
| product | **үржвэр** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| parallelogram | **параллелограмм** | ministry standard |
| distance | **зай** | ministry standard |
| sector | **сектор** | ministry standard |
| subtraction | **хасалт** | already on the site |
| perimeter | **периметр** | already on the site |
| rectangle | **тэгш өнцөгт** | ministry standard |
| problem | **бодлого** | ministry standard |
| side | **тал** | ministry standard |
| height | **өндөр** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## area-of-parallelograms-and-triangles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pt-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pt-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## area-of-trapezoids-rhombi-kites

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED tr-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY tr-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pt-we1` and so on) exactly
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

