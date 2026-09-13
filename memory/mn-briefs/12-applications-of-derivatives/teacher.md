# MN authoring brief — Applications of Derivatives

**Topic** `12/applications-of-derivatives` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `12/applications-of-derivatives`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `tangent-lines`

**Able to:** Write the equation of the tangent line to a curve at a point: slope from f', point from f, assembled in point-slope form.

**The idea that carries it:** Tangent at x = a: y = f(a) + f'(a)(x − a). Point from f, slope from f', point-slope from Grade 8 — and near the touch point, the line practically IS the curve.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using f(a) as the slope.
- Writing the tangent through the origin by default.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ad1-we1` — Find the tangent line to $y = x^2$ at $x = 3$.
- `ad1-we2` — Find the tangent line to $y = x^3 - 2x$ at $x = 1$.
- `ad1-we3` — Use the tangent to $y = \sqrt{x}$ at $x = 16$ to estimate $\sqrt{17}$.

**2 try-it problems**, same freedom and same condition.

### 2. `rising-and-falling`

**Able to:** Find the intervals where f increases and decreases by solving f'(x) = 0 and testing the sign of f' on each interval.

**The idea that carries it:** Solve f' = 0 for critical points, test one point per interval, and the sign chart of f' hands you every rising and falling stretch of f.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the sign of f instead of f'.
- Skipping the test points and guessing alternation.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ad2-we1` — Find where $f(x) = x^3 - 3x$ rises and falls.
- `ad2-we2` — Find where $f(x) = x^2 - 8x + 3$ decreases.
- `ad2-we3` — Show $f(x) = x^3 + x$ increases EVERYWHERE.

**2 try-it problems**, same freedom and same condition.

### 3. `peaks-and-valleys`

**Able to:** Classify critical points as local maxima, minima, or neither using the first-derivative test, and find extreme values on closed intervals.

**The idea that carries it:** Extremes hide only where f' = 0. Classify by the sign flip: + to − is a peak, − to + is a valley, no flip is a pause. On [a,b], also audit the endpoints.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Declaring every critical point a max or min.
- Forgetting endpoints on a closed interval.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ad3-we1` — Find and classify the critical points of $f(x) = x^3 - 3x$.
- `ad3-we2` — Find the absolute max and min of $f(x) = x^2 - 4x$ on $[0, 5]$.
- `ad3-we3` — Classify the critical point of $f(x) = x^4$ at $x = 0$… and of $g(x) = x^3$ at $x = 0$.

**2 try-it problems**, same freedom and same condition.

### 4. `concavity-and-the-second-derivative`

**Able to:** Compute second derivatives, read concavity (up/down) and inflection points, and classify critical points with the second-derivative test.

**The idea that carries it:** f'' measures the curl: positive bends up (∪), negative bends down (∩), sign change = inflection. At a critical point, f'' > 0 means valley, f'' < 0 means peak.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing concave down with decreasing.
- Reading f''(a) = 0 as 'neither max nor min'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ad4-we1` — Find $f''$ for $f(x) = x^3 - 6x^2 + 5$ and locate the inflection point.
- `ad4-we2` — Use the second-derivative test on $f(x) = x^3 - 3x$.
- `ad4-we3` — Where does the test go silent? Try $f(x) = x^4$ at its critical point.

**2 try-it problems**, same freedom and same condition.

### 5. `curve-sketching`

**Able to:** Combine intercepts, asymptotes, f' (direction, extremes) and f'' (concavity, inflections) into a complete, justified sketch of a function.

**The idea that carries it:** Five-step checklist — domain/intercepts, end behavior, f' chart, f'' chart, connect. Every tool from four topics, one coherent portrait.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Plotting ten points and connecting the dots.
- Letting the sketch contradict a computed fact.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ad5-we1` — Profile $f(x) = x^3 - 3x^2$: intercepts, extremes, inflection.
- `ad5-we2` — Profile $f(x) = \dfrac{2x}{x - 1}$: asymptotes and direction.
- `ad5-we3` — Two functions have $f' = 3x^2 + 1$ and $g' = -3x^2 - 1$ respectively. Sketch-describe each in one sentence.

**2 try-it problems**, same freedom and same condition.

### 6. `optimization`

**Able to:** Translate word problems into functions of one variable (using the constraint), find the optimum with derivatives, and verify it's the right kind of extreme.

**The idea that carries it:** Target minus constraint = one-variable function; f' = 0 finds the candidate; f'' or endpoints certify it; then answer the actual question.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Differentiating a two-variable target.
- Reporting x when the question asked for the area (or cost, or profit).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ad6-we1` — 100 m of fence, biggest rectangular paddock: dimensions and area?
- `ad6-we2` — Two nonnegative numbers sum to 20. Maximize their product.
- `ad6-we3` — An open-top box: square base $x$, height $h$, volume $32$ cm³. Minimize the material $M = x^2 + 4xh$.

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
| measure | **хэмжих** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| increase | **өсөх** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| slope | **налалт** | ministry standard |
| derivative | **уламжлал** | ministry standard |
| asymptote | **асимптот** | already on the site |
| interval | **завсар** | ministry standard |
| point | **цэг** | ministry standard |
| problem | **бодлого** | ministry standard |
| form | **хэлбэр** | ministry standard |
| second | **хоёр дахь** | ministry standard |
| stretch | **сунгалт** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

**increase** — proposed **өсөх**

> POLYSEMOUS by form. The intransitive "increase / be increasing" is өсөх — ministry, glossary and shipped all agree, and its opposite is буурах. But the noun "an increase" is өсөлт, which is what the percent unit actually ships: «Хувиар өсөлт ба бууралт» = Percent Increase & Decrease, «$25\%$-ийн өсөлт» = a 25% increase. And the transitive "increase something" is ихэсгэх/өсгөх («гурав дахин ихэсгэвэл»). So: өсөх for a quantity rising or a function increasing, өсөлт for the measured increase, ихэсгэх when a person increases a value. Do not use нэмэгдэх (which shipped uses for parts adding up across the origin) as a synonym for the function property.

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
## tangent-lines

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ad1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ad1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## rising-and-falling

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ad2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ad2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`ad1-we1` and so on) exactly
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

- **Уламжлалын хэрэглээ (12-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

