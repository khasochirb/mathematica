# MN authoring brief — Cylinders & Cones

**Topic** `solid-geometry/cylinders-and-cones` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `solid-geometry/cylinders-and-cones`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-cylinder`

**Able to:** Know the cylinder's anatomy (axis, radius, height, axial section) and compute its surface area from the unrolled label.

**The idea that carries it:** Cylinder = rolled rectangle + 2 lids: S_lat = 2πrh, S = 2πr(h + r). Axial section: a 2r × h rectangle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using πr² (area) instead of 2πr (circumference) for the unrolled label's width.
- Adding one lid instead of two (or two when the tube is open).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg41-we1` — A cylinder has radius $3$ and height $5$. Find its lateral and total surface area, exactly.
- `sg41-we2` — A cylinder's axial section is a SQUARE of area $36$. Find the cylinder's total surface area.

**2 try-it problems**, same freedom and same condition.

### 2. `volume-of-cylinders`

**Able to:** Compute cylinder volumes with V = πr²h, including leaning (oblique) cylinders, and solve capacity problems.

**The idea that carries it:** V = πr²h (slice × height). Doubling r quadruples V; doubling h only doubles it. Oblique cylinders: same formula, TRUE height.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the diameter as r.
- Thinking doubling any dimension doubles the volume.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg42-we1` — Radius $3$, height $10$: find the volume exactly and to one decimal.
- `sg42-we2` — Two cans: A has $r = 4, h = 5$; B has $r = 5, h = 4$ (dimensions swapped). Which holds more, and by how much?

**2 try-it problems**, same freedom and same condition.

### 3. `the-cone`

**Able to:** Master cone anatomy (r, h, slant ℓ with ℓ² = r² + h²), surface area S = πr² + πrℓ, and the unrolled-sector picture.

**The idea that carries it:** Axial triangle: ℓ² = r² + h². Unrolled: a sector of radius ℓ, arc 2πr, area πrℓ, angle (r/ℓ)·360°.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the lateral surface as πrh.
- Unrolling the cone into a sector of radius r.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg43-we1` — A cone has $r = 3$ and $h = 4$. Find the slant height and total surface area.
- `sg43-we2` — A cone with $r = 3$, $\ell = 5$ is cut open and unrolled. Find the sector's central angle and check its arc length equals the rim.

**2 try-it problems**, same freedom and same condition.

### 4. `cone-volume-and-the-truncated-cone`

**Able to:** Compute volumes of cones (V = ⅓πr²h) and truncated cones (frustums of cones), reusing the pyramid's ⅓ and the frustum blend.

**The idea that carries it:** Cone: V = ⅓πr²h. Truncated cone: V = (πh/3)(R² + Rr + r²), slant ℓ² = h² + (R−r)², S_lat = π(R+r)ℓ.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the ⅓ from the cone (or keeping it for the cylinder).
- Averaging the radii for truncated-cone volume: π((R+r)/2)²h.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg44-we1` — A cone has $r = 3$ and $h = 4$. Find its volume, and the volume of the cylinder with the same base and height.
- `sg44-we2` — A truncated cone has radii $R = 5$, $r = 2$ and height $4$. Find its slant height, lateral surface, and volume.

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
| volume | **эзлэхүүн** | ministry standard |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| cylinder | **цилиндр** | ministry standard |
| cone | **конус** | ministry standard |
| sector | **сектор** | ministry standard |
| radius | **радиус** | ministry standard |
| surface area | **гадаргуугийн талбай** | ministry standard |
| formula | **томьёо** | ministry standard |
| rectangle | **тэгш өнцөгт** | ministry standard |
| problem | **бодлого** | ministry standard |
| solid | **биет** | ministry standard |
| height | **өндөр** | already on the site |

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
## the-cylinder

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg41-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg41-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## volume-of-cylinders

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg42-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg42-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sg41-we1` and so on) exactly
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

