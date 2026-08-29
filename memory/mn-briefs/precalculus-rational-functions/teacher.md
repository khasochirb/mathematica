# MN authoring brief — Rational Functions

**Topic** `precalculus/rational-functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `precalculus/rational-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `vertical-asymptotes-and-domain`

**Able to:** Find the domain of a rational function, locate vertical asymptotes from the reduced denominator, and determine the sign of the blow-up on each side.

**The idea that carries it:** Domain excludes denominator zeros; where the reduced denominator dies (numerator alive), the graph blows up along a vertical asymptote — sign-test each side separately.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Setting the NUMERATOR to zero to find asymptotes.
- Assuming the graph goes up on both sides of every vertical asymptote.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc41-we1` — Find the domain and vertical asymptotes of $f(x) = \dfrac{x + 1}{x^2 - x - 6}$.
- `pc41-we2` — For $f(x) = \dfrac{2}{x - 4}$, determine the behavior on each side of the asymptote $x = 4$.

**2 try-it problems**, same freedom and same condition.

### 2. `holes-vs-asymptotes`

**Able to:** Detect common factors in numerator and denominator, classify each domain exclusion as a hole or a vertical asymptote, and compute hole coordinates from the reduced function.

**The idea that carries it:** Shared factors cancel into holes (missing single points at the reduced function's height); factors surviving in the denominator make true asymptotes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Cancelling the shared factor and then declaring x = 2 back in the domain.
- Calling every denominator zero an asymptote without factoring the top.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc42-we1` — Analyze $f(x) = \dfrac{x^2 - 4}{x - 2}$: domain, and the exact nature of the exclusion.
- `pc42-we2` — Classify every domain exclusion of $g(x) = \dfrac{(x - 1)(x + 4)}{(x - 1)(x - 6)}$.

**2 try-it problems**, same freedom and same condition.

### 3. `horizontal-asymptotes-and-end-behavior`

**Able to:** Determine horizontal asymptotes by comparing degrees, understand why via leading-term division, and handle the slant case when the top is one degree heavier.

**The idea that carries it:** Compare degrees: bottom wins → y = 0; tie → y = ratio of leading coefficients; top wins → none (one degree over: slant asymptote from the division quotient).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating a horizontal asymptote like a fence the graph can never touch.
- Reading the tie case from the constant terms: giving y = 1/5 for (6x² − x)/(2x² + 5).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc43-we1` — Find the horizontal asymptote of each: $f(x) = \dfrac{3x + 1}{x^2 - 4}$, $g(x) = \dfrac{6x^2 - x}{2x^2 + 5}$, $h(x) = \dfrac{x^3}{x + 1}$.
- `pc43-we2` — Find the slant asymptote of $f(x) = \dfrac{x^2 - 3x + 7}{x - 1}$.

**2 try-it problems**, same freedom and same condition.

### 4. `graphing-rational-functions`

**Able to:** Combine intercepts, holes, vertical and horizontal asymptotes, and sign tests into a complete graph of a rational function.

**The idea that carries it:** Factor, exclude, intercept, asymptote, sign-test: five clues carve the plane, and each branch has exactly one way to thread them.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing a branch that crosses a vertical asymptote to reach an intercept on the other side.
- Skipping the y-intercept because 'asymptotes matter more.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc44-we1` — Fully analyze $f(x) = \dfrac{2x - 4}{x + 1}$ and describe its graph.
- `pc44-we2` — Analyze $g(x) = \dfrac{x^2 - 1}{x^2 - 4}$: intercepts, asymptotes, and the sign chart.

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
| factor | **хуваагч** | ministry standard |
| function | **функц** | ministry standard |
| fraction | **бутархай** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| division | **хуваалт** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| zero | **тэг** | ministry standard |
| rational | **рационал** | ministry standard |
| plane | **хавтгай** | ministry standard |
| asymptote | **асимптот** | already on the site |
| vertical | **босоо** | ministry standard |
| hole | **нүх** | already on the site |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## vertical-asymptotes-and-domain

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc41-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc41-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## holes-vs-asymptotes

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc42-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc42-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc41-we1` and so on) exactly
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

