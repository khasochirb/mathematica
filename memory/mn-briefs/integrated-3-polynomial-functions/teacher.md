# MN authoring brief — Polynomial Functions

**Topic** `integrated-3/polynomial-functions` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-3/polynomial-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `degree-and-end-behaviour`

**Able to:** Predict a polynomial's end behaviour from its degree and leading coefficient, and bound the number of zeros and turning points.

**The idea that carries it:** The degree's parity decides whether the ends agree, the leading coefficient's sign decides which way — and everything else about the graph lives in the middle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading end behaviour off the constant term or a middle term.
- Assuming a degree-5 polynomial must have five real zeros.
- Forgetting that a negative leading coefficient flips BOTH ends.
- Claiming a zero from a sign change without continuity.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u1-l1-we1` — Describe the end behaviour of $f(x) = -2x^{3} + 5x^{2} - x + 7$, and say how many real zeros and turning points it could have.
- `im3-u1-l1-we2` — Compare the end behaviour of $g(x) = x^{4} - 3x^{2}$ and $h(x) = -x^{4} + 3x^{2}$, and explain why an even-degree polynomial can have no real zeros at
- `im3-u1-l1-we3` — A polynomial graph falls from the top left, turns three times, and rises to the top right, crossing the horizontal axis four times. What is the smalle
- `im3-u1-l1-we4` — Show that $p(x) = x^{3} - 4x + 1$ has a zero between $0$ and $1$, and another between $1$ and $2$, without solving it.

**2 try-it problems**, same freedom and same condition.

### 2. `zeros-and-multiplicity`

**Able to:** Find zeros from a factorisation, use multiplicity to decide crossing or bouncing, and sketch a polynomial from its factored form.

**The idea that carries it:** Each factor gives a zero and its exponent gives the multiplicity — odd multiplicity crosses, even multiplicity bounces.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the zeros of $(x + 4)^2$ as $x = 4$.
- Assuming every zero is a crossing.
- Forgetting the leading coefficient when building from zeros.
- Adding the number of DISTINCT zeros to get the degree.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u1-l2-we1` — For $f(x) = (x - 2)^{2}(x + 1)(x - 4)$, list the zeros with multiplicities, state the degree and end behaviour, and describe the graph's behaviour at 
- `im3-u1-l2-we2` — Compare the behaviour of $g(x) = x(x - 3)$ and $h(x) = x(x - 3)^{2}$ near $x = 3$, using sign tests.
- `im3-u1-l2-we3` — Write a polynomial of degree $4$ with zeros at $-3$ (multiplicity $1$), $1$ (multiplicity $2$) and $2$ (multiplicity $1$), passing through $(0, 12)$.
- `im3-u1-l2-we4` — Sketch $f(x) = -x^{3}(x - 2)^{2}(x + 1)$ by finding its zeros, multiplicities, degree, end behaviour and the sign on each interval.

**2 try-it problems**, same freedom and same condition.

### 3. `division-and-the-remainder-theorem`

**Able to:** Divide polynomials, state the division algorithm, and use the Remainder and Factor Theorems to test factors and find zeros.

**The idea that carries it:** The remainder on dividing by $x - a$ is $p(a)$ — so testing a factor is one substitution, and finding one zero drops the degree by one.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using $a = -3$ when dividing by $x - 3$.
- Omitting a zero coefficient in synthetic division.
- Concluding a polynomial has no zeros when the rational candidates all fail.
- Dividing when a substitution would answer the question.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u1-l3-we1` — Divide $p(x) = 2x^{3} - 5x^{2} + 3x - 7$ by $x - 3$ using synthetic division, and confirm the remainder with the Remainder Theorem.
- `im3-u1-l3-we2` — Prove the Remainder Theorem, then use it to decide whether $x + 2$ is a factor of $q(x) = x^{4} + 3x^{3} - x - 6$.
- `im3-u1-l3-we3` — Factor $p(x) = x^{3} - 6x^{2} + 11x - 6$ completely, and find all its zeros.
- `im3-u1-l3-we4` — Find the value of $k$ for which $x - 2$ is a factor of $f(x) = x^{3} + kx^{2} - 4x + 12$, and then factor the result completely.

**2 try-it problems**, same freedom and same condition.

### 4. `polynomial-operations-and-identities`

**Able to:** Multiply and factor higher-degree polynomials using the sum and difference of cubes and structural substitution, and build and interpret polynomial models.

**The idea that carries it:** The cube identities and structural substitution extend factoring past degree two — and every polynomial MODEL carries a domain narrower than the polynomial's own.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing $a^3 - b^3 = (a - b)(a^2 - ab + b^2)$.
- Trying to factor the quadratic from a cube identity further.
- Stopping a quartic factorisation at $(x^2 - 4)(x^2 - 9)$.
- Reporting a model's optimum outside its physical domain.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u1-l4-we1` — Factor $8x^{3} - 27$ and $x^{3} + 64$ completely.
- `im3-u1-l4-we2` — Factor $x^{4} - 13x^{2} + 36$ completely, and find all its zeros.
- `im3-u1-l4-we3` — An open box is made from a $20$ cm by $16$ cm sheet by cutting a square of side $x$ from each corner and folding up the sides. Write the volume as a p
- `im3-u1-l4-we4` — Factor $x^{3} - 2x^{2} - 9x + 18$ by grouping, and confirm the zeros against the Factor Theorem.

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
| function | **функц** | ministry standard |
| division | **хуваалт** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| rational | **рационал** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| even | **тэгш** | ministry standard |
| cube | **шоо** | already on the site |
| remainder | **үлдэгдэл** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| vertical | **босоо** | ministry standard |
| graph | **график** | ministry standard |

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
## degree-and-end-behaviour

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u1-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u1-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## zeros-and-multiplicity

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u1-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u1-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u1-l1-we1` and so on) exactly
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

