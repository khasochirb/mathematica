# MN authoring brief — Pyramids

**Topic** `solid-geometry/pyramids` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `solid-geometry/pyramids`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `pyramid-anatomy`

**Able to:** Name the parts of a pyramid, count its elements, and master the two right triangles inside a regular pyramid (height–apothem–slant and height–half-diagonal–edge).

**The idea that carries it:** Regular pyramid = regular base + apex over the center. Two Pythagorean triangles inside: m² = h² + r² (slant) and ℓ² = h² + R² (edge).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing slant height (to an edge's MIDPOINT) with lateral edge (to a VERTEX).
- Placing the apex over a vertex or edge and still using the regular-pyramid formulas.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg31-we1` — A regular square pyramid has base side $6$ and height $4$. Find its slant height $m$ and lateral edge $\ell$.
- `sg31-we2` — A pyramid has $10$ faces. What is its base, and how many edges and vertices does it have?

**2 try-it problems**, same freedom and same condition.

### 2. `surface-area-of-pyramids`

**Able to:** Compute lateral and total surface area of regular pyramids: S_lat = ½ P·m.

**The idea that carries it:** S_lat = ½ P·m (P = base perimeter, m = slant height); total adds the single base. Find m via m² = h² + r² first.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the pyramid's height h in ½P·m.
- Adding two bases like a prism.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg32-we1` — A regular square pyramid has base side $10$ and height $12$. Find its total surface area.
- `sg32-we2` — A regular square pyramid's lateral surface is twice its base area, with base side $6$. Find the slant height and then the height.

**2 try-it problems**, same freedom and same condition.

### 3. `volume-of-pyramids`

**Able to:** Compute pyramid volumes with V = ⅓Bh and solve inverse problems.

**The idea that carries it:** V = ⅓Bh — exactly a third of the prism, with h the perpendicular height (convert from slant/edge if needed).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the ⅓ — computing a prism volume by reflex.
- Plugging the slant height (or lateral edge) in as h.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg33-we1` — A regular square pyramid has base side $10$ and height $12$. Find its volume.
- `sg33-we2` — A regular square pyramid has base side $6$ and SLANT height $5$. Find its volume.

**2 try-it problems**, same freedom and same condition.

### 4. `the-frustum`

**Able to:** Compute surface area and volume of a frustum (truncated pyramid), using similarity of the two bases.

**The idea that carries it:** Frustum = pyramid minus similar top. V = (h/3)(B₁ + B₂ + √(B₁B₂)); S_lat = ½(P₁+P₂)m with m² = h² + (r₁−r₂)².

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the two base areas: V = h·(B₁+B₂)/2.
- Using the height h as the slant m in the trapezoid-wall formula.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg34-we1` — A frustum has square bases with sides $6$ and $3$, and height $2$. Find its volume.
- `sg34-we2` — A regular square frustum has bases $10$ and $4$ and height $4$. Find its slant height and lateral surface area.

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
| edge | **ирмэг** | already on the site |
| volume | **эзлэхүүн** | ministry standard |
| area | **талбай** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| square | **квадрат** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| surface area | **гадаргуугийн талбай** | ministry standard |
| perimeter | **периметр** | already on the site |
| problem | **бодлого** | ministry standard |
| height | **өндөр** | already on the site |
| part | **хэсэг** | ministry standard |
| total | **нийт** | already on the site |
| prism | **призм** | ministry standard |
| inverse | **урвуу** | ministry standard |
| pyramid | **пирамид** | ministry standard |

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
## pyramid-anatomy

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg31-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg31-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## surface-area-of-pyramids

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg32-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg32-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sg31-we1` and so on) exactly
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

