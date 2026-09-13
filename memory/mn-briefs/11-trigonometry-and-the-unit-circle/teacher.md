# MN authoring brief — Trigonometry & the Unit Circle

**Topic** `11/trigonometry-and-the-unit-circle` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `11/trigonometry-and-the-unit-circle`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `radians`

**Able to:** Convert between degrees and radians using $180° = \pi$ rad, and know the key angles in both units.

**The idea that carries it:** 1 radian = radius-length of arc; 180° = π rad. Convert by ×π/180 or ×180/π; arc length s = rθ.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Memorizing '1 rad = 57.3°' and converting through it.
- Dropping the π from radian answers.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr1-we1` — Convert $30°$, $90°$, and $270°$ to radians.
- `tr1-we2` — Convert $\tfrac{\pi}{4}$ and $\tfrac{2\pi}{3}$ to degrees.
- `tr1-we3` — A pendulum of length 3 m swings through 2 radians. Arc length?

**2 try-it problems**, same freedom and same condition.

### 2. `the-unit-circle`

**Able to:** Use the unit-circle definition — $(\cos\theta, \sin\theta)$ is the point at angle $\theta$ — including axis angles and quadrant signs.

**The idea that carries it:** The point at angle θ is (cos θ, sin θ): cosine is x, sine is y. Signs come from the quadrant; cos² + sin² = 1 always.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assigning sine to x and cosine to y.
- Measuring the angle from the y-axis, or clockwise.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr2-we1` — Read $\cos$ and $\sin$ at $180°$ and at $270°$.
- `tr2-we2` — In which quadrant is $\theta = 200°$, and what are the signs of its cosine and sine?
- `tr2-we3` — Verify $\cos^2 60° + \sin^2 60° = 1$ exactly.

**2 try-it problems**, same freedom and same condition.

### 3. `special-angles`

**Able to:** Know the exact sine and cosine of 30°, 45°, 60° (π/6, π/4, π/3) and extend them to all quadrants via reference angles.

**The idea that carries it:** √1/2, √2/2, √3/2 — the sine ladder at 30°, 45°, 60°. Reference angle gives the size; quadrant gives the sign.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping the 30°/60° values.
- Getting the reference angle's SIZE right but forgetting the quadrant sign.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr3-we1` — Exact values: $\sin 30°$, $\cos 45°$, $\sin 60°$.
- `tr3-we2` — Evaluate $\sin 150°$ and $\cos 150°$ exactly.
- `tr3-we3` — Evaluate $\cos 225°$ and $\sin 300°$ exactly.

**2 try-it problems**, same freedom and same condition.

### 4. `sine-and-cosine-waves`

**Able to:** Connect the unit circle to the graphs of sin and cos: shape, period 2π, amplitude 1, intercepts and peaks.

**The idea that carries it:** Sine = the circling point's height, unrolled: period 2π, amplitude 1. Cosine = the same wave starting at its peak.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing the sine wave starting at its peak.
- Thinking the wave eventually flattens or drifts.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr4-we1` — Where in $[0, 2\pi]$ does $\sin\theta$ peak, cross zero, and trough?
- `tr4-we2` — Verify the periodicity: compare $\sin\tfrac{\pi}{6}$ and $\sin\tfrac{13\pi}{6}$.
- `tr4-we3` — Verify the quarter-turn shift at $\theta = 0$ and $\theta = \tfrac{\pi}{3}$: $\cos\theta = \sin(\theta + \tfrac{\pi}{2})$.

**2 try-it problems**, same freedom and same condition.

### 5. `transforming-waves`

**Able to:** Read amplitude |a|, period 2π/b, and midline k from $y = a\sin(b\theta) + k$, and evaluate such functions exactly.

**The idea that carries it:** y = a·sin(bθ) + k: amplitude |a|, period 2π/b, midline k; range [k−|a|, k+|a|].

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading b itself as the period.
- Taking max − min as the amplitude.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr5-we1` — Amplitude, period, midline of $y = 3\sin(2\theta) + 5$?
- `tr5-we2` — Evaluate $y = 3\sin(2\theta) + 5$ at $\theta = \tfrac{\pi}{4}$.
- `tr5-we3` — A wave has max 10 and min 2. Find its amplitude and midline.

**2 try-it problems**, same freedom and same condition.

### 6. `periodic-models`

**Able to:** Build and use sinusoidal models: match midline to center, amplitude to radius/half-swing, period to the cycle time.

**The idea that carries it:** Midline = center; amplitude = radius (half the swing); b = 2π/period. Cycles of any kind, one template.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Setting b equal to the period.
- Using the wheel's TOP height as the midline.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr6-we1` — Ferris wheel: center 10 m, radius 8 m, period 60 s. Write $h(t)$ and find the max/min heights.
- `tr6-we2` — Evaluate that wheel at $t = 15$ s.
- `tr6-we3` — Tide: $d = 5 + 2\sin(\tfrac{\pi}{6}t)$ ($t$ in hours). Average depth, swing, and period?

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
| range | **далайц** | ministry standard |
| shape | **дүрс** | ministry standard |
| half | **хагас** | already on the site |
| size | **хэмжээ** | ministry standard |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| circle | **тойрог** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| period | **үе** | **proposed — tell us if it is wrong** |
| radius | **радиус** | ministry standard |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |
| model | **загвар** | ministry standard |
| coordinate | **координат** | ministry standard |
| height | **өндөр** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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

WORKED tr1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY tr1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-unit-circle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED tr2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY tr2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`tr1-we1` and so on) exactly
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

- **Нэгж тойрог (11-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

