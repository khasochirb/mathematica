# MN authoring brief — Polynomial Functions

**Topic** `algebra-2/polynomial-functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/polynomial-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `polynomial-basics-and-end-behavior`

**Able to:** Identify degree and leading coefficient, and read end behavior and turning-point limits from them.

**The idea that carries it:** The leading term steers both horizons — even degree: arms together; odd: arms opposed; sign flips the picture — and degree n caps turning points at n − 1.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading end behavior from the constant or a middle term.
- Claiming a degree-4 graph must have exactly 3 turning points.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a241-we1` — Describe the end behavior of $f(x) = -2x^4 + 7x^3 - x + 5$ and bound its turning points.
- `a241-we2` — A degree-5 polynomial has positive leading coefficient. What are its ends doing, and can it have exactly zero real zeros?

**2 try-it problems**, same freedom and same condition.

### 2. `polynomial-division-and-the-remainder-theorem`

**Able to:** Divide polynomials by long and synthetic division, and use the Remainder and Factor Theorems to test factors fast.

**The idea that carries it:** f(x) = (x − c)·q(x) + f(c): the remainder IS the evaluation, so zeros and factors are the same discovery — synthetic division just makes the bookkeeping fast.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Synthetic division with the sign unflipped: dividing by $x + 2$ using $c = 2$.
- Skipping placeholder zeros: dividing $x^3 - 7x + 6$ with the row $1, -7, 6$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a242-we1` — Divide $f(x) = x^3 - 4x^2 + x + 6$ by $x - 2$ synthetically, and factor $f$ completely.
- `a242-we2` — Without dividing, find the remainder when $f(x) = 2x^3 + x^2 - 5x + 4$ is divided by $x + 2$, and decide whether $x + 2$ is a factor.

**2 try-it problems**, same freedom and same condition.

### 3. `factoring-and-zeros`

**Able to:** Factor cubics and quartics via the rational root search, grouping, quadratic form, and sum/difference of cubes; connect zeros to x-intercepts with multiplicity.

**The idea that carries it:** Hunt an integer root among the constant's divisors, peel, finish the quadratic; recognize grouping / quadratic form / cubes patterns; and read multiplicity as cross (odd) or bounce (even).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the difference of cubes with a doubled middle term: $a^3 - b^3 = (a - b)(a^2 - 2ab + b^2)$.
- From $x^2 = 4$ concluding $x = 2$ only.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a243-we1` — Factor $f(x) = x^3 - 4x^2 + x + 6$ completely and list its zeros.
- `a243-we2` — Solve $x^4 - 13x^2 + 36 = 0$.

**2 try-it problems**, same freedom and same condition.

### 4. `polynomial-equations-and-modeling`

**Able to:** Solve polynomial equations completely (real and complex roots), apply the Fundamental Theorem's count, and model with cubics.

**The idea that carries it:** Degree n promises exactly n roots (with multiplicity, complex allowed, conjugates paired); solve by factoring down, then let the story discard the impossible ones.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting a cubic 'solved' with one root.
- Accepting $x = 5$ as a cut size for the 10×8 box.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a244-we1` — Solve $x^3 - 2x^2 + 9x - 18 = 0$ completely.
- `a244-we2` — A box is made from a 10×8 sheet by cutting squares of side $x$ from each corner and folding. Its volume is $V(x) = x(10-2x)(8-2x)$. Verify that $x = 1

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
| shape | **дүрс** | ministry standard |
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| division | **хуваалт** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| limit | **хязгаар** | already on the site |
| zero | **тэг** | ministry standard |
| rational | **рационал** | ministry standard |
| parabola | **парабол** | already on the site |
| identity | **адилтгал** | ministry standard |
| even | **тэгш** | ministry standard |
| cube | **шоо** | already on the site |
| remainder | **үлдэгдэл** | ministry standard |
| difference | **ялгавар** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## polynomial-basics-and-end-behavior

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a241-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a241-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## polynomial-division-and-the-remainder-theorem

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a242-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a242-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a241-we1` and so on) exactly
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

- **Олон гишүүнт функц (11-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

