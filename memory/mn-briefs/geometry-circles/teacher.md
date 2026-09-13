# MN authoring brief — Circles

**Topic** `geometry/circles` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/circles`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `circle-basics`

**Able to:** Identify the parts of a circle (radius, diameter, chord, secant, tangent), and measure central angles and their intercepted arcs.

**The idea that carries it:** A circle is points at radius r from a center; a diameter is 2r. A central angle equals the measure of the arc it intercepts; the whole circle is 360°.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing a chord, a secant, and a tangent.
- Thinking the radius equals the diameter.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-we1` — A circle has radius $7$. Find its diameter.
- `cb-we2` — A central angle measures $110^\circ$. What is its intercepted arc?

**2 try-it problems**, same freedom and same condition.

### 2. `arcs-and-chords`

**Able to:** Relate congruent chords to congruent arcs, add adjacent arcs, and use the fact that a diameter perpendicular to a chord bisects the chord and its arc.

**The idea that carries it:** Congruent chords intercept congruent arcs (both ways). Adjacent arcs add. A diameter perpendicular to a chord bisects the chord and its arc.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assuming chords of different lengths cut equal arcs.
- Forgetting the perpendicular diameter bisects BOTH.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ac-we1` — Two congruent chords cut arcs; one arc is $80^\circ$. What is the other?
- `ac-we2` — Arc $AB = 50^\circ$ and arc $BC = 70^\circ$ are adjacent. Find arc $ABC$.

**2 try-it problems**, same freedom and same condition.

### 3. `inscribed-angles`

**Able to:** Use the Inscribed Angle Theorem — an inscribed angle is half its intercepted arc (and half the central angle on that arc) — including the semicircle right-angle case.

**The idea that carries it:** An inscribed angle equals half its intercepted arc (and half the central angle on that arc). Same-arc inscribed angles are equal; an angle in a semicircle is 90°.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Setting the inscribed angle equal to the arc.
- Forgetting the semicircle gives $90^\circ$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ia-we1` — An inscribed angle intercepts a $120^\circ$ arc. Find the inscribed angle.
- `ia-we2` — An inscribed angle measures $35^\circ$. Find its intercepted arc.

**2 try-it problems**, same freedom and same condition.

### 4. `tangents-to-a-circle`

**Able to:** Use the tangent–radius right angle (and the Pythagorean theorem) and the fact that two tangents drawn from an external point are congruent.

**The idea that carries it:** A tangent is perpendicular to the radius at the point of tangency, forming a right triangle you can solve with Pythagoras. Two tangents from the same external point are congruent.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the tangent–radius angle is $90^\circ$.
- Adding radius and tangent as if they were the hypotenuse.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tg-we1` — A tangent touches a circle of radius $6$. The distance from the center to the external point is $10$. Find the tangent length.
- `tg-we2` — Two tangents from an external point: one is $12$. Find the other.

**2 try-it problems**, same freedom and same condition.

### 5. `angle-relationships-in-circles`

**Able to:** Find angles formed by two chords meeting inside a circle (half the sum of the intercepted arcs) and by two secants or tangents meeting outside (half the difference).

**The idea that carries it:** Two chords crossing inside a circle make an angle equal to half the sum of the intercepted arcs; two secants/tangents meeting outside make an angle equal to half the difference of the arcs.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the difference inside, or the sum outside.
- Forgetting to divide by 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ar-we1` — Two chords cross inside a circle, intercepting arcs of $80^\circ$ and $40^\circ$. Find the angle.
- `ar-we2` — Two secants from an external point intercept arcs of $100^\circ$ (far) and $40^\circ$ (near). Find the angle.

**2 try-it problems**, same freedom and same condition.

### 6. `arc-length-and-sector-area`

**Able to:** Find the arc length (θ/360 of the circumference) and the sector area (θ/360 of the circle's area) for a given central angle.

**The idea that carries it:** A central angle θ gives the fraction θ/360 of the circle. Arc length = (θ/360)·2πr; sector area = (θ/360)·πr².

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the area formula for arc length (or vice versa).
- Forgetting the θ/360 fraction.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `as-we1` — A circle has radius $6$. Find the arc length of a $90^\circ$ sector.
- `as-we2` — Same circle (radius $6$). Find the area of the $90^\circ$ sector.

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
| measure | **хэмжих** | ministry standard |
| secant | **огтлогч** | ministry standard |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| fraction | **бутархай** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| sector | **сектор** | ministry standard |
| addition | **нэмэх** | ministry standard |
| radius | **радиус** | ministry standard |
| difference | **ялгавар** | ministry standard |
| point | **цэг** | ministry standard |
| form | **хэлбэр** | ministry standard |
| part | **хэсэг** | ministry standard |
| length | **урт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## circle-basics

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cb-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cb-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## arcs-and-chords

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ac-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ac-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cb-we1` and so on) exactly
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

