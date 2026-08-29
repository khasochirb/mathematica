# MN authoring brief — Spheres

**Topic** `solid-geometry/spheres` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `solid-geometry/spheres`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-sphere-and-its-sections`

**Able to:** Use the definition of the sphere, and compute section radii with r² = R² − d² (the sphere's master triangle).

**The idea that carries it:** Every section is a circle with r² = R² − d². Great circle: d = 0, r = R. Tangent plane: d = R, r = 0.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Expecting oval or polygonal cross-sections from tilted cuts.
- Writing r² = R² + d² (adding instead of subtracting).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg51-we1` — A sphere of radius $5$ is cut by a plane at distance $3$ from the center. Find the section's radius and area.
- `sg51-we2` — A plane cuts a sphere of radius $13$ in a circle of radius $12$. How far is the plane from the center?

**2 try-it problems**, same freedom and same condition.

### 2. `surface-area-of-a-sphere`

**Able to:** Use S = 4πR² for spheres, hemispheres, and painted-planet problems.

**The idea that carries it:** S = 4πR² — four great circles, or the label of the snuggest can. Closed hemisphere: 2πR² dome + πR² floor = 3πR².

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing 4πR² (surface) with πR² (great circle) or with the volume formula.
- Hemisphere surface = half of 4πR², i.e. 2πR², in every problem.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg52-we1` — Find the surface area of a sphere with radius $6$, exactly and approximately.
- `sg52-we2` — A sphere's surface area is $100\pi$. Find its radius and the area of its great circle.

**2 try-it problems**, same freedom and same condition.

### 3. `volume-of-a-sphere`

**Able to:** Use V = ⁴⁄₃πR³ for spheres, hemispheres, and comparison problems; see Cavalieri's bowl argument.

**The idea that carries it:** V = ⁴⁄₃πR³ — proved by slice-matching (Cavalieri); the sphere is exactly ⅔ of its snug cylinder.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Squaring instead of cubing (or using the volume 4/3 with R²).
- Thinking double radius = double volume.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg53-we1` — Find the volume of a sphere with radius $3$, and notice something about the number.
- `sg53-we2` — A sphere sits snugly in a cylinder (touching top, bottom, sides), $R = 3$. Find both volumes and their ratio.

**2 try-it problems**, same freedom and same condition.

### 4. `inscribed-and-circumscribed-solids`

**Able to:** Relate spheres to cubes and cylinders they inscribe in or circumscribe around: which length equals 2R, and why.

**The idea that carries it:** Inscribed sphere touches faces: 2R = edge/height. Circumscribed sphere reaches corners: 2R = space diagonal (cube) or axial diagonal (cylinder).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the edge for a CIRCUMSCRIBED sphere (or the diagonal for an inscribed one).
- For a cylinder in a sphere, setting 2R = h or 2R = 2r alone.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg54-we1` — A cube has edge $6$. Find the radii of its inscribed and circumscribed spheres, and the ratio of the two spheres' volumes.
- `sg54-we2` — A cylinder with $r = 3$ and $h = 8$ is inscribed in a sphere. Find the sphere's radius.

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
| edge | **ирмэг** | already on the site |
| volume | **эзлэхүүн** | ministry standard |
| area | **талбай** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| cylinder | **цилиндр** | ministry standard |
| plane | **хавтгай** | ministry standard |
| sphere | **бөмбөрцөг** | ministry standard |
| radius | **радиус** | ministry standard |
| surface area | **гадаргуугийн талбай** | ministry standard |
| cube | **шоо** | already on the site |
| problem | **бодлого** | ministry standard |
| solid | **биет** | ministry standard |
| corner | **булан** | already on the site |
| height | **өндөр** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

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
## the-sphere-and-its-sections

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg51-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg51-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## surface-area-of-a-sphere

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg52-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg52-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sg51-we1` and so on) exactly
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

