# MN authoring brief — The Unit Circle

**Topic** `precalculus/the-unit-circle` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `precalculus/the-unit-circle`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `radians`

**Able to:** Define the radian via arc length, convert between degrees and radians, and compute arc lengths with s = rθ.

**The idea that carries it:** One radian = arc of one radius; full turn = 2π; convert via 180° = π; and in radians, arc length is simply s = rθ.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating π as 180 ('π = 180, so π/2 = 90').
- Using s = rθ with θ in degrees.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc61-we1` — Convert $135°$ to radians and $\dfrac{5\pi}{6}$ to degrees.
- `pc61-we2` — A pendulum of length 2 m swings through $\dfrac{\pi}{6}$ radians. How long is the arc its tip traces? What would the same swing be in degrees?

**2 try-it problems**, same freedom and same condition.

### 2. `sine-and-cosine-on-the-circle`

**Able to:** Define cos θ and sin θ as the coordinates of the point at angle θ on the unit circle, extend trig beyond 90°, and derive the Pythagorean identity.

**The idea that carries it:** The point at angle θ on the unit circle is (cos θ, sin θ) — cosine is x, sine is y, for any θ — and living on x² + y² = 1 forces cos²θ + sin²θ = 1.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Refusing sin 150° because 'a right triangle can't have a 150° angle.'
- Writing cos²θ + sin²θ = 1 only for acute θ, or 'fixing' signs: cos²θ − sin²θ.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc62-we1` — Evaluate $\cos\pi$, $\sin\pi$, $\cos\tfrac{3\pi}{2}$, and $\sin\tfrac{3\pi}{2}$ from the circle.
- `pc62-we2` — An angle $\theta$ in the second quadrant has $\sin\theta = \tfrac{3}{5}$. Find $\cos\theta$.

**2 try-it problems**, same freedom and same condition.

### 3. `special-angles-and-exact-values`

**Able to:** Derive the exact sine/cosine values at 30°, 45°, 60° from the two special triangles, place them on the first-quadrant circle, and use the size ordering to self-check.

**The idea that carries it:** Two triangles give three values — 1/2, √2/2, √3/2; sine climbs the list as the angle grows, cosine descends it, and 30°/60° swap each other's values.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping the pair at 30°: sin 30° = √3/2.
- Writing √2/2 as '1/√2 simplified to 2/√2' or other mangled forms.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc63-we1` — Derive $\cos 30°$ and $\sin 30°$ from the equilateral triangle, exactly.
- `pc63-we2` — Give the exact coordinates of the unit-circle point at $\theta = \tfrac{\pi}{4}$, and verify it lies on the circle.

**2 try-it problems**, same freedom and same condition.

### 4. `reference-angles-and-all-quadrants`

**Able to:** Find reference angles in every quadrant, attach signs via quadrant reasoning, and evaluate sine and cosine exactly for any special-family angle, including negative and oversized angles.

**The idea that carries it:** Size from the reference angle (acute gap to the x-axis), sign from the quadrant, and oversized/negative angles come home first via full laps.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the reference angle from the y-axis: calling 150°'s reference 60°.
- Letting the reference angle carry the sign: sin 210° = sin 30° because 'reference angles are equal.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc64-we1` — Evaluate $\sin 150°$, $\cos 225°$, and $\sin\tfrac{5\pi}{3}$ exactly.
- `pc64-we2` — Evaluate $\cos 495°$ and $\sin\left(-\tfrac{\pi}{6}\right)$ exactly.

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
| size | **хэмжээ** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| unit | **нэгж** | ministry standard |
| identity | **адилтгал** | ministry standard |
| radius | **радиус** | ministry standard |
| table | **хүснэгт** | ministry standard |
| point | **цэг** | ministry standard |
| coordinate | **координат** | ministry standard |
| length | **урт** | ministry standard |
| degree | **зэрэг** | ministry standard |
| sign | **тэмдэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

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
## radians

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc61-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc61-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## sine-and-cosine-on-the-circle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc62-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc62-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc61-we1` and so on) exactly
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

