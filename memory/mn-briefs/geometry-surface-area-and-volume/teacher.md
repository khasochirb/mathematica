# MN authoring brief — Surface Area & Volume

**Topic** `geometry/surface-area-and-volume` · **6 lessons** · 12 worked examples · 11 practice · 7 test-yourself

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
> `geometry/surface-area-and-volume`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `prisms-surface-area-and-volume`

**Able to:** Find the volume (base area × height) and the surface area of a prism, using a net to see all the faces.

**The idea that carries it:** Prism volume = base area × height (cubic units). Surface area = the sum of all faces; for a box, SA = 2(lw + lh + wh).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Mixing up cubic and square units.
- Forgetting a pair of faces in surface area.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pr-we1` — A box is $2 \times 3 \times 4$. Find its volume.
- `pr-we2` — Find the surface area of the same $2 \times 3 \times 4$ box.

**2 try-it problems**, same freedom and same condition.

### 2. `cylinders`

**Able to:** Find the volume (πr²h) and surface area (2πr² + 2πrh) of a cylinder.

**The idea that carries it:** Cylinder volume = πr²h (circle base × height). Surface area = 2πr² (two circles) + 2πrh (the wrapped label of width 2πr, height h).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to square the radius in the volume.
- Leaving out the two circle ends in surface area.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cy-we1` — A cylinder has radius $3$ and height $5$. Find its volume (in terms of π).
- `cy-we2` — Find its surface area (in terms of π).

**2 try-it problems**, same freedom and same condition.

### 3. `pyramids`

**Able to:** Find the volume of a pyramid (⅓ × base area × height) and describe its surface area (base + triangular faces).

**The idea that carries it:** Pyramid volume = ⅓ × base area × height — one third of the matching prism. Surface area = base + the triangular lateral faces.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the $\tfrac13$.
- Using the slant edge as the height.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `py-we1` — A pyramid has a square base of side $6$ and height $10$. Find its volume.
- `py-we2` — A pyramid with base area $27$ and height $5$. Find its volume.

**2 try-it problems**, same freedom and same condition.

### 4. `cones`

**Able to:** Find the volume (⅓πr²h) and surface area (πr² + πrℓ) of a cone, and find the slant height with the Pythagorean theorem.

**The idea that carries it:** Cone volume = ⅓πr²h — a third of its cylinder. Surface area = πr² + πrℓ, where the slant height ℓ = √(r² + h²).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the $\tfrac13$ in the cone volume.
- Using the height instead of the slant height for surface area.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `co-we1` — A cone has radius $3$ and height $4$. Find its volume (in terms of π).
- `co-we2` — The same cone (radius $3$, height $4$). Find its slant height, then its surface area.

**2 try-it problems**, same freedom and same condition.

### 5. `spheres`

**Able to:** Find the volume (4⁄3πr³) and surface area (4πr²) of a sphere, and handle a hemisphere as half a sphere.

**The idea that carries it:** Sphere volume = 4⁄3πr³ (radius cubed). Surface area = 4πr² (four circles). A hemisphere is half a sphere: ⅔πr³.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Squaring the radius in the volume instead of cubing it.
- Forgetting the $4$ in the surface area.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sp-we1` — A sphere has radius $3$. Find its volume (in terms of π).
- `sp-we2` — The same sphere (radius $3$). Find its surface area.

**2 try-it problems**, same freedom and same condition.

### 6. `composite-solids`

**Able to:** Find the volume and surface area of composite solids by decomposing them into prisms, cylinders, pyramids, cones, and spheres.

**The idea that carries it:** Break a composite solid into simple pieces, find each volume, and add — or subtract a removed piece. For surface area, count only the outside faces.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Counting a hidden face where two solids join.
- Adding when you should subtract.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cs-we1` — A silo is a cylinder of radius $3$ and height $10$ topped by a hemisphere of radius $3$. Find the total volume (in terms of π).
- `cs-we2` — A block is a $5 \times 4 \times 6$ box with a $2 \times 4 \times 6$ rectangular notch cut out. Find the remaining volume.

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
| count | **тоолох** | ministry standard |
| half | **хагас** | already on the site |
| base | **суурь** | ministry standard |
| volume | **эзлэхүүн** | ministry standard |
| area | **талбай** | ministry standard |
| circle | **тойрог** | ministry standard |
| cylinder | **цилиндр** | ministry standard |
| unit | **нэгж** | ministry standard |
| cone | **конус** | ministry standard |
| sphere | **бөмбөрцөг** | ministry standard |
| radius | **радиус** | ministry standard |
| surface area | **гадаргуугийн талбай** | ministry standard |
| solid | **биет** | ministry standard |
| height | **өндөр** | already on the site |
| subtract | **хасах** | ministry standard |
| face | **нүүр** | already on the site |
| width | **өргөн** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## prisms-surface-area-and-volume

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pr-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pr-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## cylinders

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cy-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cy-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pr-we1` and so on) exactly
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

- **Гадаргуу ба эзлэхүүн** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

