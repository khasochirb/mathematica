# MN authoring brief — Functions & Their Graphs

**Topic** `precalculus/functions-and-their-graphs` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `precalculus/functions-and-their-graphs`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `domain-range-and-graph-features`

**Able to:** Read domain, range, intercepts, intervals of increase/decrease, and maxima/minima directly off a graph, and compute domains from formulas.

**The idea that carries it:** Domain = the graph's shadow on the x-axis, range = its shadow on the y-axis; increase/decrease intervals are always named by x.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing 'increasing on $(-4, \infty)$' using the y-values of the climb.
- Giving the domain of $\sqrt{x-3}$ as $x > 3$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc11-we1` — Find the domain of $f(x) = \dfrac{\sqrt{x+2}}{x-5}$.
- `pc11-we2` — For $f(x) = x^2 - 4$: find the intercepts, the range, and where $f$ is decreasing.

**2 try-it problems**, same freedom and same condition.

### 2. `composition-of-functions`

**Able to:** Evaluate and simplify compositions (f∘g)(x) = f(g(x)), compare f∘g with g∘f, and decompose a function into simpler layers.

**The idea that carries it:** f∘g means g first, then f — substitute g's whole formula into f's x; order changes the result.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $(f \circ g)(x)$ as 'f first, then g' because f is written first.
- Substituting without parentheses: $f(x) = x^2$, $g(x) = x+3$, writing $f(g(x)) = x + 3^2$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc12-we1` — For $f(x) = x^2 - 1$ and $g(x) = 3x + 2$, compute $(f \circ g)(1)$ and $(g \circ f)(1)$.
- `pc12-we2` — For the same $f, g$, simplify $(f \circ g)(x)$ as a polynomial.

**2 try-it problems**, same freedom and same condition.

### 3. `inverse-functions`

**Able to:** Find inverse functions algebraically, verify inverses by composition, recognize the y = x mirror symmetry, and use the horizontal line test for invertibility.

**The idea that carries it:** The inverse swaps every (a, b) into (b, a): algebraically swap x and y and re-solve; graphically mirror across y = x; only one-to-one functions (horizontal line test) qualify.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing $f^{-1}(x)$ as $\frac{1}{f(x)}$ because of the $-1$.
- Undoing operations in the same order they were applied: for $f(x) = 3x - 5$, dividing by 3 first, then adding 5, to get $\frac{x}{3} + 5$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc13-we1` — Find $f^{-1}(x)$ for $f(x) = 3x - 5$, and verify by composition.
- `pc13-we2` — Find the inverse of $f(x) = \dfrac{2x + 1}{x - 3}$.

**2 try-it problems**, same freedom and same condition.

### 4. `symmetry-even-and-odd`

**Able to:** Test functions for even/odd symmetry algebraically via f(−x), recognize the two symmetries on graphs, and use symmetry to halve graphing work.

**The idea that carries it:** Compute f(−x): equal to f(x) means even (mirror over the y-axis); equal to −f(x) means odd (half-turn about the origin); neither means no symmetry.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Concluding 'odd' the moment a function is not even.
- Calling $f(x) = x^2 + 1$ odd because it has the odd-looking +1, or testing only one point.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc14-we1` — Classify $f(x) = x^4 - 3x^2$ as even, odd, or neither.
- `pc14-we2` — Classify $g(x) = x^3 - 5x$ as even, odd, or neither.

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
| half | **хагас** | already on the site |
| increase | **өсөх** | ministry standard |
| feature | **шинж** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| parabola | **парабол** | already on the site |
| even | **тэгш** | ministry standard |
| formula | **томьёо** | ministry standard |
| halve | **хагаслах** | already on the site |
| interval | **завсар** | ministry standard |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |
| pair | **хос** | ministry standard |
| ones | **нэгж** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

**increase** — proposed **өсөх**

> POLYSEMOUS by form. The intransitive "increase / be increasing" is өсөх — ministry, glossary and shipped all agree, and its opposite is буурах. But the noun "an increase" is өсөлт, which is what the percent unit actually ships: «Хувиар өсөлт ба бууралт» = Percent Increase & Decrease, «$25\%$-ийн өсөлт» = a 25% increase. And the transitive "increase something" is ихэсгэх/өсгөх («гурав дахин ихэсгэвэл»). So: өсөх for a quantity rising or a function increasing, өсөлт for the measured increase, ихэсгэх when a person increases a value. Do not use нэмэгдэх (which shipped uses for parts adding up across the origin) as a synonym for the function property.

**feature** — proposed **шинж**

> Split by sense in production: "шинж" where it means a property of the data, but "That sensitivity is a feature AND a warning" → "давуу тал" (advantage). As a term label "шинж" is the one to keep; the "давуу тал" line is prose, not a term, and needs no change.

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
## domain-range-and-graph-features

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc11-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc11-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## composition-of-functions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc12-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc12-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc11-we1` and so on) exactly
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

