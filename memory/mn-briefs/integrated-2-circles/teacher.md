# MN authoring brief — Circles

**Topic** `integrated-2/circles` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/circles`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `central-and-inscribed-angles`

**Able to:** Relate central angles, inscribed angles and their intercepted arcs, prove the inscribed-angle theorem, and apply it to semicircles and cyclic quadrilaterals.

**The idea that carries it:** An inscribed angle is half the central angle on the same arc — and the semicircle right angle, equal angles on one arc, and cyclic quadrilaterals are all corollaries.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doubling instead of halving an inscribed angle.
- Using the wrong arc for an inscribed angle.
- Assuming any quadrilateral has supplementary opposite angles.
- Missing the right angle when a diameter is drawn.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u7-l1-we1` — A central angle of $\;84°$ stands on arc $AB$. Find the arc's measure and the measure of any inscribed angle standing on the same arc.
- `im2-u7-l1-we2` — Prove the inscribed-angle theorem in the case where one side of the angle passes through the centre.
- `im2-u7-l1-we3` — $AB$ is a diameter of a circle and $C$ is another point on it, with $\angle CAB = 34°$. Find $\angle ACB$ and $\angle ABC$.
- `im2-u7-l1-we4` — A quadrilateral $ABCD$ has all four vertices on a circle. Given $\angle A = 76°$ and $\angle B = 105°$, find $\angle C$ and $\angle D$, and explain wh

**2 try-it problems**, same freedom and same condition.

### 2. `chords-tangents-and-secants`

**Able to:** Use the tangent-radius right angle, the perpendicular-bisector property of chords, and the intersecting-chords and secant-tangent length relationships.

**The idea that carries it:** The tangent-radius right angle and the perpendicular bisection of chords convert circle problems into right triangles; the product rules come from similar triangles.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the full chord length in the perpendicular-from-centre triangle.
- Treating the radius as the hypotenuse in a tangent problem.
- Using only the external part of a secant on both sides of the product rule.
- Assuming two chords that cross must be bisected by the crossing.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u7-l2-we1` — A tangent from an external point $P$ touches a circle of radius $9$ at $T$, and $OP = 15$ where $O$ is the centre. Find the tangent length $PT$.
- `im2-u7-l2-we2` — A chord of length $24$ lies in a circle of radius $13$. Find its distance from the centre. Then find the length of a chord that is $12$ from the centr
- `im2-u7-l2-we3` — Two chords intersect inside a circle at $P$. One is divided into pieces $6$ and $x$; the other into $4$ and $9$. Find $x$, and explain why the product
- `im2-u7-l2-we4` — From an external point $P$, a tangent touches a circle at $T$ with $PT = 8$, and a secant through $P$ meets the circle at $A$ (near) and $B$ (far) wit

**2 try-it problems**, same freedom and same condition.

### 3. `arc-length-and-sector-area`

**Able to:** Compute arc length and sector area as fractions of a circle, and understand why arc length is proportional to radius — which is what makes radian measure possible.

**The idea that carries it:** Arc and sector are the same fraction $\frac{\theta}{360}$ of the circumference and of the area — and because arc scales with radius, $\frac{s}{r}$ defines the radian.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing sector with segment.
- Using $\frac{\theta}{360}$ when the angle is already in radians.
- Converting $\pi$ to a decimal early.
- Using the arc-length formula and reporting square units.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u7-l3-we1` — A circle has radius $12$ cm. Find the length of a $75°$ arc and the area of the corresponding sector, exactly and to two decimal places.
- `im2-u7-l3-we2` — Two circles have radii $5$ and $15$. For a central angle of $40°$ in each, find both arc lengths and the ratio $\frac{s}{r}$ in each case. What do you
- `im2-u7-l3-we3` — Convert $135°$ to radians and $\frac{5\pi}{6}$ radians to degrees. Then find the arc length and sector area for a $\frac{5\pi}{6}$ radian angle in a c
- `im2-u7-l3-we4` — A circle has radius $10$. A chord subtends a central angle of $90°$. Find the area of the SEGMENT cut off by that chord.

**2 try-it problems**, same freedom and same condition.

### 4. `the-equation-of-a-circle`

**Able to:** Derive the equation of a circle from the distance formula, read the centre and radius from standard form, and complete the square to convert from general form.

**The idea that carries it:** $(x - h)^{2} + (y - k)^{2} = r^{2}$ is the distance formula squared — so reading a circle's centre and radius is reading a right triangle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the radius directly off the right side.
- Getting the centre's signs backwards.
- Adding the completing constants to only the left side.
- Reporting a circle when the right side came out negative.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u7-l4-we1` — Derive the equation of a circle with centre $(h, k)$ and radius $r$, then write the equation of the circle with centre $(3, -2)$ and radius $7$.
- `im2-u7-l4-we2` — State the centre and radius of $(x + 5)^{2} + (y - 1)^{2} = 20$, and find where it crosses the vertical line through its centre.
- `im2-u7-l4-we3` — Convert $x^{2} + y^{2} - 6x + 10y + 18 = 0$ to standard form, and state the centre and radius.
- `im2-u7-l4-we4` — Classify each equation: (a) $x^{2} + y^{2} + 4x - 8y + 25 = 0$; (b) $x^{2} + y^{2} - 2x + 6y + 10 = 0$; (c) $x^{2} + y^{2} + 8x - 2y - 8 = 0$.

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
| tangent | **шүргэгч** | ministry standard |
| half | **хагас** | already on the site |
| scale | **томсгох** | already on the site |
| measure | **хэмжих** | ministry standard |
| secant | **огтлогч** | ministry standard |
| area | **талбай** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| angle | **өнцөг** | ministry standard |
| fraction | **бутархай** | ministry standard |
| product | **үржвэр** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| distance | **зай** | ministry standard |
| centre | **төв** | ministry standard |
| square | **квадрат** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| sector | **сектор** | ministry standard |
| radius | **радиус** | ministry standard |
| formula | **томьёо** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

**secant** — proposed **огтлогч**

> Circle sense only. The trig function sec is «секанс» (MoE 12.6 «Секанс, косеканс, котангенс») — one English word, two Mongolian terms; tag the sense on each use.

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
## central-and-inscribed-angles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u7-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u7-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## chords-tangents-and-secants

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u7-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u7-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u7-l1-we1` and so on) exactly
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

