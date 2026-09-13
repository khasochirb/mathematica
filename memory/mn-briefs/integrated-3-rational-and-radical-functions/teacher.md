# MN authoring brief — Rational & Radical Functions

**Topic** `integrated-3/rational-and-radical-functions` · **4 lessons** · 15 worked examples · 16 practice · 8 test-yourself

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
> `integrated-3/rational-and-radical-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `rational-functions-and-asymptotes`

**Able to:** Find the domain of a rational function, distinguish a hole from a vertical asymptote, and read the horizontal asymptote off the degrees.

**The idea that carries it:** Factor before you conclude anything. A cancelled factor is a hole; a surviving one is a vertical asymptote; and the degrees — not the graph — decide the horizontal asymptote.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling every zero of the denominator a vertical asymptote.
- Reading the horizontal asymptote off the constant terms.
- Assuming a graph can never cross its horizontal asymptote.
- Cancelling a factor and forgetting the point is still excluded.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u2-l1-we1` — Find the domain of $f(x) = \dfrac{x + 3}{x^2 - 5x + 6}$.
- `im3-u2-l1-we2` — Identify every hole and vertical asymptote of $g(x) = \dfrac{x^2 - 9}{x^2 - 2x - 3}$.
- `im3-u2-l1-we3` — Find the horizontal asymptote of each: (a) $\dfrac{2x + 1}{x^2 - 4}$, (b) $\dfrac{3x^2 - x}{5x^2 + 2}$, (c) $\dfrac{x^3}{x^2 + 1}$.

**3 try-it problems**, same freedom and same condition.

### 2. `operations-on-rational-expressions`

**Able to:** Multiply, divide, add and subtract rational expressions, and state the restrictions the operations require.

**The idea that carries it:** Factor first, every time. Cancelling is only legal on FACTORS, the LCD is built from factors, and the restrictions are read off factors.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Cancelling a term instead of a factor.
- Subtracting only the first term of the second numerator.
- Dropping restrictions that the simplified form hides.
- Multiplying all denominators together every time.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u2-l2-we1` — Simplify $\dfrac{x^2 - 4}{x^2 + 6x + 9} \cdot \dfrac{x + 3}{x - 2}$.
- `im3-u2-l2-we2` — Simplify $\dfrac{x^2 - 1}{x + 4} \div \dfrac{x - 1}{x^2 - 16}$.
- `im3-u2-l2-we3` — Add $\dfrac{3}{x - 2} + \dfrac{5}{x + 1}$ and state the restrictions.
- `im3-u2-l2-we4` — Subtract $\dfrac{4}{x^2 - 9} - \dfrac{1}{x + 3}$.

**3 try-it problems**, same freedom and same condition.

### 3. `solving-rational-equations`

**Able to:** Solve rational equations by clearing denominators, and identify which candidate solutions are extraneous and why.

**The idea that carries it:** Clearing denominators can only ADD candidate solutions, never lose them. So every candidate must be checked against the original domain — the check is part of the method, not a formality.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Checking the candidate in the cleared equation instead of the original.
- Concluding 'no solution' means an error was made.
- Adding the times instead of the rates in a work problem.
- Forgetting to factor before finding the LCD.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u2-l3-we1` — Solve $\dfrac{1}{x} + \dfrac{1}{2} = \dfrac{3}{4}$.
- `im3-u2-l3-we2` — Solve $\dfrac{x}{x - 3} = \dfrac{3}{x - 3} + 2$.
- `im3-u2-l3-we3` — Solve $\dfrac{2}{x - 1} + \dfrac{1}{x + 1} = \dfrac{4}{x^2 - 1}$.
- `im3-u2-l3-we4` — Two pipes fill a tank in $4$ and $12$ hours. How long do they take together?

**3 try-it problems**, same freedom and same condition.

### 4. `radical-functions-and-equations`

**Able to:** State the domain and range of a square-root function, solve radical equations by squaring, and reject the extraneous roots squaring creates.

**The idea that carries it:** Squaring, like clearing denominators, is a one-way step. It never loses a solution and it may invent one, so checking in the original equation is compulsory.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Squaring before isolating the radical.
- Treating √(a + b) as √a + √b.
- Keeping every candidate the squared equation produces.
- Missing that √u = (negative) has no solution.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u2-l4-we1` — State the domain and range of $f(x) = \sqrt{x - 4} + 1$.
- `im3-u2-l4-we2` — Solve $\sqrt{2x + 3} = 5$.
- `im3-u2-l4-we3` — Solve $\sqrt{x + 6} = x$.
- `im3-u2-l4-we4` — Solve $\sqrt{3x + 1} + 5 = 2$.

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
| range | **далайц** | ministry standard |
| factor | **хуваагч** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| square | **квадрат** | ministry standard |
| rational | **рационал** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| asymptote | **асимптот** | already on the site |
| radical | **язгуур** | ministry standard |
| vertical | **босоо** | ministry standard |
| hole | **нүх** | already on the site |
| graph | **график** | ministry standard |
| form | **хэлбэр** | ministry standard |

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
## rational-functions-and-asymptotes

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u2-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u2-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## operations-on-rational-expressions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u2-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u2-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u2-l1-we1` and so on) exactly
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

