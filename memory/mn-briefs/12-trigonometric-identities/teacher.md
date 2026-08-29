# MN authoring brief — Trigonometric Identities

**Topic** `12/trigonometric-identities` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `12/trigonometric-identities`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-pythagorean-identity`

**Able to:** Derive sin²θ + cos²θ = 1 from the unit circle, generate the tan/sec and cot/csc versions, and recover missing trig values (with the right sign for the quadrant).

**The idea that carries it:** sin²θ + cos²θ = 1 for every angle — the unit circle's radius written as an equation. It converts one known trig value into all the others, up to a quadrant sign.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing $\sin\theta = \tfrac{4}{5}$ from $\cos\theta = \tfrac{3}{5}$ without checking the quadrant.
- Treating $\sin^2\theta$ as $\sin(\theta^2)$.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti1-we1` — Given $\sin\theta = \tfrac{3}{5}$ with $\theta$ in Quadrant I, find $\cos\theta$ and $\tan\theta$.
- `ti1-we2` — Given $\cos\theta = -\tfrac{5}{13}$ with $\theta$ in Quadrant II, find $\sin\theta$.
- `ti1-we3` — Verify the identity numerically at $\theta = \tfrac{\pi}{6}$.

**2 try-it problems**, same freedom and same condition.

### 2. `sum-and-difference-formulas`

**Able to:** Use sin(A±B) and cos(A±B) to compute exact values at non-special angles and to rewrite expressions.

**The idea that carries it:** sin(A±B) = sinAcosB ± cosAsinB; cos(A±B) = cosAcosB ∓ sinAsinB. Sine mixes and keeps the sign; cosine matches kinds and flips it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Distributing: $\sin(A+B) = \sin A + \sin B$.
- Forgetting that cosine flips the middle sign.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti2-we1` — Compute $\sin 75°$ exactly.
- `ti2-we2` — Compute $\cos 15°$ exactly.
- `ti2-we3` — Simplify $\sin\theta\cos\tfrac{\pi}{3} + \cos\theta\sin\tfrac{\pi}{3}$.

**2 try-it problems**, same freedom and same condition.

### 3. `double-angle-formulas`

**Able to:** Derive and use sin 2θ = 2sinθcosθ and the three forms of cos 2θ; choose the convenient form.

**The idea that carries it:** sin 2θ = 2sinθcosθ; cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ. Pick the form that matches what you know.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doubling through the function: $\sin 2\theta = 2\sin\theta$.
- Grinding through $\cos^2 - \sin^2$ when you only know sine.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti3-we1` — Given $\sin\theta = \tfrac{3}{5}$, $\theta$ in QI: find $\sin 2\theta$.
- `ti3-we2` — Same $\theta$: find $\cos 2\theta$ using the sine-only form.
- `ti3-we3` — Verify $\sin 60° = 2\sin 30°\cos 30°$.

**2 try-it problems**, same freedom and same condition.

### 4. `proving-identities`

**Able to:** Prove identities by transforming one side: convert to sines and cosines, combine fractions, factor, and substitute known identities.

**The idea that carries it:** Prove by rewriting one side only: convert to sin/cos, run normal algebra, and substitute the Pythagorean identity to trade squares.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Moving terms across the equals sign while 'proving'.
- Never converting to sin and cos, then stalling.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti4-we1` — Prove: $\tan\theta\cos\theta = \sin\theta$.
- `ti4-we2` — Prove: $\tan\theta + \cot\theta = \dfrac{1}{\sin\theta\cos\theta}$.
- `ti4-we3` — Prove: $\dfrac{1 - \cos^2\theta}{\cos^2\theta} = \tan^2\theta$.

**2 try-it problems**, same freedom and same condition.

### 5. `solving-trig-equations`

**Able to:** Solve basic trig equations on [0, 2π) using the unit circle, and describe the full solution set with + 2πk.

**The idea that carries it:** Isolate the trig function, find the reference spots on the unit circle (sine: two heights; cosine: two widths; tangent: half-lap repeats), then add + 2πk for the infinite family.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting only the calculator's one answer for $\sin x = \tfrac12$.
- Adding $2\pi k$ to tangent solutions only.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti5-we1` — Solve $\sin x = \tfrac{1}{2}$ on $[0, 2\pi)$.
- `ti5-we2` — Solve $2\cos x + \sqrt{3} = 0$ on $[0, 2\pi)$.
- `ti5-we3` — Solve $\tan x = 1$ on $[0, 2\pi)$.

**2 try-it problems**, same freedom and same condition.

### 6. `quadratic-trig-equations`

**Able to:** Solve trig equations that are quadratics in disguise: substitute, factor, solve each value with the unit circle, and use identities to unify mixed functions.

**The idea that carries it:** Substitute u for the trig function, factor the Grade 10 quadratic, solve each root on the unit circle, and unify mixed functions with the Pythagorean identity first.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing both sides of $\sin x\cos x = \cos x$ by $\cos x$.
- Keeping $\sin x = 3$ as a solution branch.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti6-we1` — Solve $2\sin^2 x - \sin x - 1 = 0$ on $[0, 2\pi)$.
- `ti6-we2` — Solve $2\cos^2 x + \sin x - 1 = 0$ on $[0, 2\pi)$ (mixed functions).
- `ti6-we3` — Solve $\cos^2 x = \tfrac{1}{4}$ on $[0, 2\pi)$.

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
| factor | **хуваагч** | ministry standard |
| half | **хагас** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| fraction | **бутархай** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| circle | **тойрог** | ministry standard |
| square | **квадрат** | ministry standard |
| unit | **нэгж** | ministry standard |
| identity | **адилтгал** | ministry standard |
| radius | **радиус** | ministry standard |
| formula | **томьёо** | ministry standard |
| algebra | **алгебр** | ministry standard |
| difference | **ялгавар** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## the-pythagorean-identity

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ti1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ti1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## sum-and-difference-formulas

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ti2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ti2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`ti1-we1` and so on) exactly
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

- **Тригонометрийн адилтгал (12-р анги)** (primary)
- **Тригонометрийн адилтгал (12-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

