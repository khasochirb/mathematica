# MN authoring brief — Radians & the Unit Circle

**Topic** `trigonometry/radians-and-the-unit-circle` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `trigonometry/radians-and-the-unit-circle`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `radians`

**Able to:** Convert between degrees and radians, know the landmark angles in radian form, and use arc length s = rθ.

**The idea that carries it:** 1 radian = 1 radius of arc; 180° = π converts everything; and s = rθ turns angles into distances with zero fuss.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using s = rθ with the angle in degrees.
- Reading π/6 and π/3 as interchangeable 'small angles.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig31-we1` — Convert $135°$ to radians and $\frac{5\pi}{6}$ to degrees, exactly.
- `trig31-we2` — A pendulum of length $6$ m swings through $\frac{\pi}{3}$ radians. How far does its tip travel, exactly?

**2 try-it problems**, same freedom and same condition.

### 2. `the-unit-circle`

**Able to:** Define cos θ and sin θ as unit-circle coordinates, evaluate them at the axis angles, and extend trig beyond 90°.

**The idea that carries it:** On the radius-1 circle, the rotated point IS (cos θ, sin θ) — a definition that works for every angle, makes the axis values readable, and hands you cos²θ + sin²θ = 1 for free.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assigning sine to x and cosine to y.
- Thinking trig values beyond 90° are undefined because no right triangle exists.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig32-we1` — Evaluate $\cos\pi$, $\sin\pi$, $\cos\frac{3\pi}{2}$, and $\sin\frac{3\pi}{2}$ from the circle.
- `trig32-we2` — The angle $\theta$ puts $P$ at $\left(-\frac{3}{5}, \frac{4}{5}\right)$ on the unit circle. Find $\cos\theta$, $\sin\theta$, and $\tan\theta$, and ver

**2 try-it problems**, same freedom and same condition.

### 3. `reference-angles-and-signs`

**Able to:** Determine the sign of each trig function by quadrant, find reference angles, and reduce any angle's evaluation to a first-quadrant lookup.

**The idea that carries it:** Quadrant gives the sign (All-Sine-Tangent-Cosine), the reference angle gives the magnitude — every evaluation reduces to a first-quadrant lookup.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the reference angle to the y-axis when the arm is 'closer' to it.
- Applying the sign to the reference angle itself instead of the final value.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig33-we1` — Evaluate $\sin\frac{5\pi}{6}$ and $\cos\frac{5\pi}{6}$ exactly.
- `trig33-we2` — Evaluate $\tan\frac{4\pi}{3}$ exactly.

**2 try-it problems**, same freedom and same condition.

### 4. `exact-values-around-the-circle`

**Able to:** Evaluate sin, cos, and tan exactly at any multiple of π/6 or π/4, in any quadrant, including negative angles.

**The idea that carries it:** Any multiple of π/6 or π/4 — negative or huge — reduces to a landmark: strip laps, apply even/odd for minus signs, then quadrant + reference.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating cosine like sine under negation: cos(−θ) = −cos θ.
- Evaluating big angles by feeding them straight into the quadrant recipe.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig34-we1` — Evaluate exactly: $\sin\frac{5\pi}{3}$, $\cos\frac{5\pi}{3}$, $\tan\frac{5\pi}{3}$.
- `trig34-we2` — Evaluate exactly: $\cos\left(-\frac{\pi}{4}\right)$ and $\sin\frac{13\pi}{6}$.

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
| count | **тоолох** | ministry standard |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| circle | **тойрог** | ministry standard |
| distance | **зай** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| even | **тэгш** | ministry standard |
| radius | **радиус** | ministry standard |
| point | **цэг** | ministry standard |
| form | **хэлбэр** | ministry standard |
| coordinate | **координат** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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

WORKED trig31-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig31-t1:
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

WORKED trig32-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig32-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`trig31-we1` and so on) exactly
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

