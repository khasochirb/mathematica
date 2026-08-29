# MN authoring brief — Graphs of Trig Functions

**Topic** `trigonometry/graphs-of-trig-functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `trigonometry/graphs-of-trig-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-sine-wave`

**Able to:** Graph y = sin x and y = cos x from unit-circle values, and command their anatomy: period, amplitude, zeros, peaks.

**The idea that carries it:** The sine wave is the circle's y-coordinate unrolled: period 2π, amplitude 1, zeros at multiples of π — and cosine is the same wave started at its peak.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing the wave with sharp corners at the peaks, like a zigzag.
- Confusing period with amplitude.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig41-we1` — Using exact values, tabulate $y = \sin\theta$ at $\theta = 0, \frac{\pi}{6}, \frac{\pi}{2}, \frac{5\pi}{6}, \pi$ and describe the wave's first half-la
- `trig41-we2` — Where in $[0, 2\pi]$ does $\cos\theta$ reach its maximum, its minimum, and its zeros?

**2 try-it problems**, same freedom and same condition.

### 2. `amplitude-and-period`

**Able to:** Read and set amplitude and period from y = a sin(bx) or y = a cos(bx), and sketch such waves from their key points.

**The idea that carries it:** In y = a sin(bx): |a| is the vertical swing (amplitude), 2π/b is the repeat length (period) — independent knobs, read separately.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the period AS b — 'y = sin(2θ) has period 2.'
- Calling the amplitude of y = −4 sin θ 'negative 4.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig42-we1` — For $y = 3\sin(2\theta)$: state the amplitude, period, maximum value, and the first $\theta > 0$ where the maximum occurs.
- `trig42-we2` — Write a cosine function with amplitude $5$ and period $\frac{\pi}{2}$, and verify its period.

**2 try-it problems**, same freedom and same condition.

### 3. `shifts-and-the-midline`

**Able to:** Graph and write functions of the form y = a sin(b(x − c)) + d, reading midline, phase shift, and range.

**The idea that carries it:** d sets the midline (range = d ± |a|); c slides the start right by c — but only after factoring b out of the inside.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the phase shift straight off sin(2θ − π/2) as π/2.
- Giving the range as [−|a|, |a|] after a vertical shift.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig43-we1` — For $y = 2\sin(\theta) + 3$: state the midline, range, maximum, and minimum.
- `trig43-we2` — Find the amplitude, period, and phase shift of $y = 4\sin\left(2\theta - \frac{\pi}{2}\right)$, and its value at $\theta = \frac{\pi}{4}$.

**2 try-it problems**, same freedom and same condition.

### 4. `the-tangent-graph`

**Able to:** Graph y = tan θ — period π, asymptotes at odd multiples of π/2 — and contrast its behavior with sine and cosine.

**The idea that carries it:** Tangent is the arm's slope: period π, asymptotes where cos = 0, each branch sweeping all reals — unbounded, so no amplitude exists.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Giving tangent the period 2π like its parents.
- Asking for tangent's amplitude.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig44-we1` — Verify $\tan(\theta + \pi) = \tan\theta$ at $\theta = \frac{\pi}{4}$, and explain the geometry.
- `trig44-we2` — For $y = \tan(2\theta)$: find the period and the two asymptotes closest to $\theta = 0$.

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
| tangent | **шүргэгч** | ministry standard |
| factor | **хуваагч** | ministry standard |
| half | **хагас** | already on the site |
| function | **функц** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| circle | **тойрог** | ministry standard |
| slope | **налалт** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| period | **үе** | **proposed — tell us if it is wrong** |
| asymptote | **асимптот** | already on the site |
| vertical | **босоо** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |
| form | **хэлбэр** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

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
## the-sine-wave

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig41-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig41-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## amplitude-and-period

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig42-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig42-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`trig41-we1` and so on) exactly
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

