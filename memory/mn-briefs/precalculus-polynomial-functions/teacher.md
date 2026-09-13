# MN authoring brief — Polynomial Functions

**Topic** `precalculus/polynomial-functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `precalculus/polynomial-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `power-functions-and-end-behavior`

**Able to:** Determine the end behavior of any polynomial from its degree (even/odd) and leading coefficient (sign), using power functions y = ±xⁿ as models.

**The idea that carries it:** Only the leading term axⁿ speaks at long range: even n = arms together, odd n = arms opposite; negative a flips both.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Judging end behavior from the biggest COEFFICIENT: reading 40x³ as the boss of −3x⁵ + 40x³.
- Saying an odd-degree polynomial 'rises to the right' without checking the sign.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc31-we1` — Describe the end behavior of $f(x) = -3x^5 + 40x^3 - 7x + 100$.
- `pc31-we2` — A degree-4 polynomial has both arms pointing down and passes through $(0, 5)$. What can you conclude about its leading coefficient and its number of x

**2 try-it problems**, same freedom and same condition.

### 2. `zeros-and-factors`

**Able to:** Convert between zeros and linear factors, build polynomials from prescribed zeros, and use the Factor Theorem to test and find factors.

**The idea that carries it:** f(c) = 0 ⟺ (x − c) is a factor: zeros are x-intercepts are roots of factors; a family a(x−r₁)(x−r₂)… shares the same zeros until one more point fixes a.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the zero of (x + 5) as x = 5.
- Believing the zeros alone determine the polynomial.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc32-we1` — Is $(x - 3)$ a factor of $f(x) = x^3 - 2x^2 - 5x + 6$? Find all zeros if so.
- `pc32-we2` — Find the cubic with zeros $-1, 2, 4$ passing through $(0, 16)$.

**2 try-it problems**, same freedom and same condition.

### 3. `multiplicity-and-graph-shape`

**Able to:** Use the multiplicity of each zero to predict cross / bounce / flatten behavior, sketch polynomials from factored form, and recover factored form from a graph.

**The idea that carries it:** (x − c)^m: odd m crosses (m ≥ 3 flattens first), even m bounces; multiplicities sum to the degree.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing a bounce as a sharp V-corner.
- Counting a double zero once against the degree.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc33-we1` — Describe the graph of $f(x) = (x + 1)^2 (x - 2)$ at each intercept, and give its end behavior.
- `pc33-we2` — A polynomial bounces off the x-axis at $x = -3$, crosses with a flattened S-bend at $x = 1$, and passes through $(0, -9)$. Find the lowest-degree poly

**2 try-it problems**, same freedom and same condition.

### 4. `division-and-the-remainder-theorem`

**Able to:** Divide polynomials by linear divisors (long division and synthetic division), and use the Remainder Theorem to evaluate and to connect remainders with factors.

**The idea that carries it:** f(x) = (x − c)q(x) + r forces r = f(c); synthetic division computes q and r in one pass, and r = 0 recovers the Factor Theorem.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using c = 1 in synthetic division when dividing by (x + 1).
- Forgetting a zero placeholder for a missing term: dividing x³ + 5 with coefficients 1, 5.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc34-we1` — Divide $f(x) = x^3 - 4x^2 + x + 6$ by $(x - 2)$ using synthetic division, and state the conclusion.
- `pc34-we2` — Without dividing, find the remainder when $f(x) = 2x^4 - 3x^2 + 5x - 1$ is divided by $(x + 1)$.

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
| factor | **хуваагч** | ministry standard |
| function | **функц** | ministry standard |
| division | **хуваалт** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| zero | **тэг** | ministry standard |
| identity | **адилтгал** | ministry standard |
| even | **тэгш** | ministry standard |
| remainder | **үлдэгдэл** | ministry standard |
| graph | **график** | ministry standard |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| root | **язгуур** | ministry standard |
| model | **загвар** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

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
## power-functions-and-end-behavior

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc31-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc31-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## zeros-and-factors

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc32-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc32-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc31-we1` and so on) exactly
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

