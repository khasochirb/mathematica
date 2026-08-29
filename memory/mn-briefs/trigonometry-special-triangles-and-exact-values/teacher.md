# MN authoring brief — Special Triangles & Exact Values

**Topic** `trigonometry/special-triangles-and-exact-values` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `trigonometry/special-triangles-and-exact-values`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-45-45-90-triangle`

**Able to:** Derive and use the leg-leg-leg√2 pattern of 45-45-90 triangles, and read off the exact trig values of 45°.

**The idea that carries it:** 45-45-90 = half a square: sides x : x : x√2, so sin 45° = cos 45° = √2/2 and tan 45° = 1 — exactly.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying by √2 in both directions — hypotenuse from leg AND leg from hypotenuse.
- Leaving 1/√2 unrationalized and then mis-adding fractions with it.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig21-we1` — A 45-45-90 triangle has legs of length $5$. Find the hypotenuse exactly, and verify with Pythagoras.
- `trig21-we2` — A square's diagonal is $8$. Find the square's side exactly.

**2 try-it problems**, same freedom and same condition.

### 2. `the-30-60-90-triangle`

**Able to:** Derive and use the x : x√3 : 2x pattern of 30-60-90 triangles, and read off the exact trig values of 30° and 60°.

**The idea that carries it:** 30-60-90 = half an equilateral: sides x : x√3 : 2x with the short leg facing 30°; sin 30° = 1/2, cos 30° = √3/2, and the 60° values swap them.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Attaching the √3 to the short leg — or halving the LONG leg to get the short one.
- Treating the 30-60-90 pattern like the 45-45-90 one (equal legs).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig22-we1` — A 30-60-90 triangle has hypotenuse $10$. Find both legs exactly.
- `trig22-we2` — An equilateral triangle has side $8$. Find its altitude and its area, exactly.

**2 try-it problems**, same freedom and same condition.

### 3. `the-exact-value-table`

**Able to:** Command the exact sin/cos/tan values for 0°, 30°, 45°, 60°, 90°, using the √n/2 pattern, and combine them in exact computations.

**The idea that carries it:** Five sines follow √n/2 for n = 0..4; cosine runs the list backwards; tangent = sin/cos (undefined at 90°). Five landmarks, whole subject navigable.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping the sin and cos rows — writing cos 30° = 1/2.
- Writing tan 90° = 1 or ∞ as if it were a number.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig23-we1` — Compute exactly: $\sin 30° \cos 60° + \cos 30° \sin 60°$.
- `trig23-we2` — Compute exactly: $\tan 60° - \tan 30°$, and simplify to a single term.

**2 try-it problems**, same freedom and same condition.

### 4. `exact-values-in-action`

**Able to:** Solve multi-step geometry problems — perimeters, areas, composite figures — exactly, by decomposing them into special triangles.

**The idea that carries it:** Spot the special triangle hiding in the figure, run its pattern, and keep exact form — rationalize, collect like radicals, simplify roots.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding unlike radicals: √2 + √3 = √5.
- Rounding mid-problem and presenting a drifted final answer.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig24-we1` — A trapezoid has parallel sides of $10$ (bottom) and $4$ (top), and both base angles are $45°$. Find its height and area, exactly.
- `trig24-we2` — A regular hexagon has side $4$. Find its area exactly.

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
| area | **талбай** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| geometry | **геометр** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| square | **квадрат** | ministry standard |
| perimeter | **периметр** | already on the site |
| radical | **язгуур** | ministry standard |
| table | **хүснэгт** | ministry standard |
| problem | **бодлого** | ministry standard |
| form | **хэлбэр** | ministry standard |
| root | **язгуур** | ministry standard |
| side | **тал** | ministry standard |
| pattern | **хэв маяг** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## the-45-45-90-triangle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig21-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig21-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-30-60-90-triangle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig22-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig22-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`trig21-we1` and so on) exactly
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

