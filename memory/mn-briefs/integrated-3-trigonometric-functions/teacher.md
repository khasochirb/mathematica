# MN authoring brief — Trigonometric Functions & General Triangles

**Topic** `integrated-3/trigonometric-functions` · **6 lessons** · 18 worked examples · 21 practice · 10 test-yourself

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
> `integrated-3/trigonometric-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-unit-circle`

**Able to:** Define sine and cosine as coordinates on the unit circle, measure angles in radians in every quadrant, and evaluate the new definitions at the axis angles.

**The idea that carries it:** On the unit circle, cosine IS the x-coordinate and sine IS the y-coordinate of the point the angle reaches. Every fact in this unit is that sentence read off the picture.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating sin and cos as undefined past 90 degrees.
- Mixing the coordinates up: sine first because it sounds first.
- Converting radians with 360 instead of 180.
- Thinking a negative angle gives negative values automatically.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u4-l1-we1` — Convert $150^\circ$ and $270^\circ$ to radians, and $\dfrac{7\pi}{4}$ to degrees.
- `im3-u4-l1-we2` — Using coordinates, evaluate $\cos\pi$, $\sin\dfrac{3\pi}{2}$ and $\cos\dfrac{\pi}{2}$.
- `im3-u4-l1-we3` — Find an angle between $0$ and $2\pi$ that lands on the same point as (a) $\dfrac{13\pi}{6}$, (b) $-\dfrac{\pi}{3}$, and evaluate $\sin$ of each.

**3 try-it problems**, same freedom and same condition.

### 2. `reference-angles-and-exact-values`

**Able to:** Find the reference angle and quadrant of any angle, and combine them to evaluate sine, cosine and tangent exactly at the special angles.

**The idea that carries it:** Reference angle for the SIZE, quadrant for the SIGN. Every exact value on the circle is a first-quadrant value wearing its quadrant's signs.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the reference angle from the y-axis.
- Letting the reference angle carry the sign.
- Assuming tangent is negative wherever sine is.
- Giving one answer to sin θ = c on a full turn.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u4-l2-we1` — Evaluate $\sin\dfrac{5\pi}{6}$ and $\cos\dfrac{5\pi}{6}$ exactly.
- `im3-u4-l2-we2` — Evaluate $\cos\dfrac{4\pi}{3}$, $\sin\dfrac{4\pi}{3}$ and $\tan\dfrac{4\pi}{3}$ exactly.
- `im3-u4-l2-we3` — Find every angle $\theta$ in $[0, 2\pi)$ with $\sin\theta = -\dfrac{\sqrt{2}}{2}$.

**3 try-it problems**, same freedom and same condition.

### 3. `graphs-of-sine-and-cosine`

**Able to:** Graph transformations of sine and cosine, reading amplitude, period and midline from the equation — and write the equation of a wave from its description.

**The idea that carries it:** Three dials: $|a|$ sets the swing, $y = k$ sets the centreline, and $\frac{2\pi}{b}$ sets the lap time. Read them off an equation, or set them from max, min and period when building one.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling the full swing the amplitude.
- Reading b itself as the period.
- Treating the negative in -2 cos x as a negative amplitude.
- Choosing sine when the story starts at a peak.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u4-l3-we1` — State the amplitude, period and midline of $y = 3\sin(2x) - 1$, and its maximum and minimum values.
- `im3-u4-l3-we2` — Describe how $y = -2\cos\left(\dfrac{x}{2}\right)$ differs from $y = \cos x$, and give its value at $x = 0$.
- `im3-u4-l3-we3` — The depth of water at a pier oscillates between a high tide of $14$ m and a low tide of $2$ m, with $12$ hours between highs. Write a model for the de

**3 try-it problems**, same freedom and same condition.

### 4. `the-pythagorean-identity`

**Able to:** Prove the Pythagorean identity from the unit circle, and use it with quadrant reasoning to find sine, cosine or tangent given one of them.

**The idea that carries it:** $\sin^2\theta + \cos^2\theta = 1$ is the unit circle's equation with the coordinates renamed. It recovers any value from any other — up to a sign that only the quadrant can supply.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing sin²θ + cos²θ = 1 only for acute θ.
- Forgetting the ± when un-squaring.
- Reading sin²θ as sin(θ²).
- Verifying at one angle and calling it proved.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u4-l4-we1` — Given $\sin\theta = \dfrac{3}{5}$ with $\theta$ in quadrant II, find $\cos\theta$ and $\tan\theta$.
- `im3-u4-l4-we2` — Given $\cos\theta = -\dfrac{5}{13}$ with $\pi < \theta < \dfrac{3\pi}{2}$, find $\sin\theta$.
- `im3-u4-l4-we3` — Prove that $(1 - \cos\theta)(1 + \cos\theta) = \sin^2\theta$ for every $\theta$, and verify it at $\theta = \dfrac{\pi}{6}$.

**3 try-it problems**, same freedom and same condition.

### 5. `the-law-of-sines`

**Able to:** Derive the Law of Sines from an altitude, use it to solve triangles given two angles and a side or two sides and a non-included angle, recognise the ambiguous case, and compute a triangle's area from two sides and the angle between them.

**The idea that carries it:** In any triangle $\dfrac{a}{\sin A} = \dfrac{b}{\sin B} = \dfrac{c}{\sin C}$. Use it whenever you know a side together with the angle across from it — and check SSA for a second triangle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Pairing a side with the angle next to it.
- Using the Law of Sines when no opposite pair is known.
- Taking the calculator's inverse sine as the only answer.
- Panicking when sin B comes out bigger than 1.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u4-l5-we1` — In triangle $ABC$, $A = 45°$, $B = 60°$ and $a = 10$. Find $b$ exactly.
- `im3-u4-l5-we2` — A triangular plot has two sides of length $8$ m and $10$ m with an angle of $30°$ between them. Find its area.
- `im3-u4-l5-we3` — In triangle $ABC$, $a = 6$, $b = 10$ and $A = 30°$. How many triangles fit this data?

**3 try-it problems**, same freedom and same condition.

### 6. `the-law-of-cosines`

**Able to:** State and apply the Law of Cosines to solve triangles given two sides and the included angle (SAS) or all three sides (SSS), and recognise it as a generalisation of the Pythagorean theorem.

**The idea that carries it:** $c^2 = a^2 + b^2 - 2ab\cos C$ is the Pythagorean theorem with a correction term for the corner not being square. Use it for SAS and SSS — the two cases the Law of Sines cannot start.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing c² = a² + b² - 2ab cos C with C not the included angle.
- Computing 2ab cos C as (2ab cos)·C, or subtracting before multiplying.
- Forgetting that c² is the answer, not c.
- Reaching for the Law of Cosines when a matched pair is already known.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u4-l6-we1` — In triangle $ABC$, $a = 5$, $b = 8$ and the angle between them is $C = 60°$. Find $c$.
- `im3-u4-l6-we2` — A triangle has sides $7$, $8$ and $13$. Find its largest angle.
- `im3-u4-l6-we3` — Two roads leave a junction at an angle of $120°$. A cyclist rides $6$ km along one and $10$ km along the other. How far apart are the two endpoints?

**3 try-it problems**, same freedom and same condition.

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
| size | **хэмжээ** | ministry standard |
| measure | **хэмжих** | ministry standard |
| area | **талбай** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| square | **квадрат** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| period | **үе** | **proposed — tell us if it is wrong** |
| identity | **адилтгал** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

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
## the-unit-circle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u4-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u4-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## reference-angles-and-exact-values

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u4-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u4-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u4-l1-we1` and so on) exactly
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

