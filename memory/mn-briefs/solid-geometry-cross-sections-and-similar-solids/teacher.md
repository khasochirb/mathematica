# MN authoring brief — Cross-Sections & Similar Solids

**Topic** `solid-geometry/cross-sections-and-similar-solids` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `solid-geometry/cross-sections-and-similar-solids`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `cross-sections-of-solids`

**Able to:** Predict and compute cross-sections of cubes, prisms, pyramids, cylinders, and cones — including the diagonal section and the shapes a tilted knife makes.

**The idea that carries it:** Parallel cut copies the base (scaled for pointed solids); axial cut is the ID card (rectangle/triangle); the cube's diagonal section is a × a√2; tilted cuts can even make hexagons.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assuming every cut of a cylinder is a circle (or of a cube, a square).
- Halving the AREA when cutting a pyramid at half-height.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg61-we1` — A cube has edge $4$. Find the area of its diagonal section (the rectangle through two opposite vertical edges).
- `sg61-we2` — A cone has $r = 6$, $h = 4$. Find the area of its axial section, and of the parallel section at half the height.

**2 try-it problems**, same freedom and same condition.

### 2. `similar-solids-k-k2-k3`

**Able to:** Use the scaling laws — lengths ×k, areas ×k², volumes ×k³ — on any solid, forwards and backwards.

**The idea that carries it:** Similar solids: lengths ×k, areas ×k², volumes ×k³. Given any one ratio, root it to k, then re-raise.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling volume by k (or by k²).
- Averaging or adding ratios when going area → volume.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg62-we1` — Two similar bottles: the big one is $1.5\times$ the height of the small. The small holds $400$ mL. The big holds…?
- `sg62-we2` — Two similar cones have surface areas $36\pi$ and $100\pi$. The small one's volume is $54\pi$. Find the big one's volume.

**2 try-it problems**, same freedom and same condition.

### 3. `combined-solids`

**Able to:** Compute volumes and surfaces of solids built by adding or drilling out basic solids, tracking which surfaces survive the gluing.

**The idea that carries it:** Volumes: add glued pieces, subtract drilled ones. Surfaces: glued faces disappear; drilled walls appear. Inventory before computing.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding full surface areas of both pieces at a glue joint.
- Forgetting the inner wall of a drilled solid.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg63-we1` — A silo is a cylinder ($r = 3$, $h = 8$) topped by a hemisphere ($R = 3$). Find its total volume.
- `sg63-we2` — Same silo: find the EXTERIOR surface (walls + dome + floor).

**2 try-it problems**, same freedom and same condition.

### 4. `solid-problem-strategies`

**Able to:** Solve multi-step exam problems by extracting the right flat triangle: the five classic configurations and the checklist that finds them.

**The idea that carries it:** Five flat triangles solve all of stereometry: the climb, the two pyramid triangles, the cone's axial, the sphere's section, the shadow. Find the one holding your unknown; redraw it flat.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing inside the 3D picture — reading slanted drawing lengths as true.
- Attaching a given angle to the wrong triangle (edge angle vs face angle).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg64-we1` — A regular square pyramid's lateral edge is $\ell = 6$, making a $45°$ angle with the base plane. Find the height and the base side.
- `sg64-we2` — A cone's axial section is a RIGHT isosceles triangle with hypotenuse $12$ (the hypotenuse is the base diameter). Find the cone's volume.

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
| base | **суурь** | ministry standard |
| scale | **томсгох** | already on the site |
| volume | **эзлэхүүн** | ministry standard |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| number | **тоо** | ministry standard |
| cylinder | **цилиндр** | ministry standard |
| cone | **конус** | ministry standard |
| sphere | **бөмбөрцөг** | ministry standard |
| even | **тэгш** | ministry standard |
| cube | **шоо** | already on the site |
| rectangle | **тэгш өнцөгт** | ministry standard |
| problem | **бодлого** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

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
## cross-sections-of-solids

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg61-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg61-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## similar-solids-k-k2-k3

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg62-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg62-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sg61-we1` and so on) exactly
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

