# MN authoring brief — Trig Graphs & Equations

**Topic** `precalculus/trigonometric-graphs-and-equations` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `precalculus/trigonometric-graphs-and-equations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-sine-and-cosine-graphs`

**Able to:** Graph y = sin x and y = cos x from unit-circle values, identify domain, range, zeros, and extremes, and understand period 2π and the cosine head start.

**The idea that carries it:** Sine is the circling point's height unrolled over time; cosine is its x-coordinate — the same 2π-periodic wave with a quarter-lap head start; range always [−1, 1].

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing sine as sharp zigzag teeth.
- Giving sine's period as π because 'it returns to zero at π.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc71-we1` — Using the five anchor points, state where $y = \sin x$ on $[0, 2\pi]$ is zero, maximal, and minimal — and verify each from the circle.
- `pc71-we2` — Does the equation $\sin x = 1.4$ have a solution? What about $\cos x = -0.3$? Explain from the range.

**2 try-it problems**, same freedom and same condition.

### 2. `amplitude-period-and-shifts`

**Able to:** Read amplitude, period, phase shift, and midline from y = A sin(B(x − C)) + D; graph such functions; and write equations from wave descriptions.

**The idea that carries it:** A = height, D = sea level, period = 2π/B, phase = C from the FACTORED inside B(x − C) — four independent dials, all Unit 2 moves.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the phase shift of sin(2x − π/3) as π/3.
- Making a bigger B stretch the wave longer.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc72-we1` — For $y = 3\sin(2x) - 1$: amplitude, period, midline, range, and the first peak's location.
- `pc72-we2` — Find amplitude, period, and phase shift of $y = 2\sin\left(3x - \tfrac{\pi}{2}\right)$, then give its first ascending zero.

**2 try-it problems**, same freedom and same condition.

### 3. `fundamental-identities`

**Able to:** Define tan, cot, sec, csc in terms of sine and cosine; master the three Pythagorean identities and even/odd rules; and simplify or verify trig expressions.

**The idea that carries it:** Everything converts to sine and cosine; the circle equation mints all three Pythagorean identities; cos is even, sin and tan are odd — then it's just algebra.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading sec θ as the inverse function of sine (or csc as inverse cosine) because of the s/c initials.
- Verifying an identity by checking one angle and declaring victory.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc73-we1` — Evaluate all six trig functions at $\theta = \tfrac{\pi}{3}$.
- `pc73-we2` — Simplify $\dfrac{\sec\theta - \cos\theta}{\tan\theta}$ to a single trig function.

**2 try-it problems**, same freedom and same condition.

### 4. `solving-trig-equations`

**Able to:** Solve basic trig equations exactly: find all solutions in [0, 2π), express the general solution with + 2πk, and handle equations requiring isolation or factoring.

**The idea that carries it:** Isolate, size (reference angle), place (quadrants by sign), laps (+2πk): trig equations yield seed solutions plus a periodic pattern — usually two seeds per lap, one at the extremes, none beyond the range.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting only the calculator/QI answer: sin x = ½ ⟹ x = π/6, done.
- Dividing both sides of sin x cos x = cos x by cos x.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc74-we1` — Solve $2\cos x + 1 = 0$ on $[0, 2\pi)$, then give the general solution.
- `pc74-we2` — Solve $2\sin^2 x - \sin x = 0$ on $[0, 2\pi)$.

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
| count | **тоолох** | ministry standard |
| size | **хэмжээ** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| cosine | **косинус** | ministry standard |
| circle | **тойрог** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| limit | **хязгаар** | already on the site |
| zero | **тэг** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| period | **үе** | **proposed — tell us if it is wrong** |
| even | **тэгш** | ministry standard |

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

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## the-sine-and-cosine-graphs

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc71-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc71-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## amplitude-period-and-shifts

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc72-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc72-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc71-we1` and so on) exactly
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

