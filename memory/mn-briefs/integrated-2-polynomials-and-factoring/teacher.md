# MN authoring brief — Polynomials & Factoring

**Topic** `integrated-2/polynomials-and-factoring` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/polynomials-and-factoring`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-polynomial-system`

**Able to:** Name the parts of a polynomial, state its degree, add and subtract polynomials, and explain what it means for the polynomials to be CLOSED under an operation.

**The idea that carries it:** Polynomials are closed under addition, subtraction and multiplication — the same three operations the integers are closed under, and for the same structural reason.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding the exponents when adding like terms: $3x^{2} + 5x^{2} = 8x^{4}$.
- Distributing a subtraction only onto the first term of the second polynomial.
- Calling $\frac{3}{x} + x$ a polynomial because it 'has no roots or decimals'.
- Reading the leading coefficient of $-4x^3 + 2x$ as $4$.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u2-l1-we1` — Write $6 - 4x^{3} + x - 9x^{2}$ in standard form, then state its degree, leading coefficient and constant term.
- `im2-u2-l1-we2` — Add $(3x^{2} - 7x + 2)$ and $(5x^{2} + 4x - 9)$.
- `im2-u2-l1-we3` — Subtract: $(4x^{3} + x^{2} - 6x) - (x^{3} - 5x^{2} + 6x - 11)$.
- `im2-u2-l1-we4` — Decide which of these are polynomials, and give the degree of those that are: (a) $4x^{2} - \sqrt{3}x + 1$; (b) $\dfrac{5}{x} + 2$; (c) $x^{3}\sqrt{x}

**2 try-it problems**, same freedom and same condition.

### 2. `multiplying-polynomials`

**Able to:** Multiply polynomials by distributing every term over every term, and recognise the two special products that will be run backwards in Lesson 4.

**The idea that carries it:** Multiplication is one rule — every term times every term — and the two special products are just the cases where the cross terms behave in a way worth remembering.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing $(a + b)^{2} = a^{2} + b^{2}$.
- Using FOIL on a binomial times a trinomial and stopping after four products.
- Losing the sign when distributing a negative term.
- Expecting $(a - b)^2$ to end in $-b^2$.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u2-l2-we1` — Expand $(x + 3)(x + 5)$, and explain where the middle term comes from.
- `im2-u2-l2-we2` — Expand $(2x - 3)(x^{2} + 4x - 1)$.
- `im2-u2-l2-we3` — Expand $(x + 7)(x - 7)$ and $(3x - 2)(3x + 2)$, and say what the two have in common.
- `im2-u2-l2-we4` — Expand $(x + 6)^{2}$ and $(2x - 5)^{2}$. Then explain why $(x + 6)^{2}$ is not $x^{2} + 36$.

**2 try-it problems**, same freedom and same condition.

### 3. `factoring-basics`

**Able to:** Pull out the greatest common factor, factor $x^{2} + bx + c$ by finding two numbers with the right sum and product, and factor four-term expressions by grouping.

**The idea that carries it:** To factor $x^{2} + bx + c$, find two numbers whose product is $c$ and whose sum is $b$ — because that is precisely what expanding $(x + p)(x + q)$ produced.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Factoring the trinomial first and forgetting the common factor.
- Getting the signs backwards on $x^2 - 5x - 36$, writing $(x - 4)(x + 9)$.
- Declaring an expression prime after checking only two factor pairs.
- Giving up on grouping when the first pairing fails.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u2-l3-we1` — Factor $12x^{3} - 18x^{2} + 30x$ completely.
- `im2-u2-l3-we2` — Factor $x^{2} + 11x + 24$.
- `im2-u2-l3-we3` — Factor $x^{2} - 5x - 36$.
- `im2-u2-l3-we4` — Factor $2x^{3} + 6x^{2} + 5x + 15$ by grouping.

**2 try-it problems**, same freedom and same condition.

### 4. `special-factoring-forms`

**Able to:** Factor a difference of squares and a perfect-square trinomial on sight, factor $ax^{2} + bx + c$ when $a \neq 1$ using the ac-method, and know when to stop.

**The idea that carries it:** Identify the shape before you search: difference of squares, perfect square, or neither — and when $a \neq 1$, split the middle term using product $ac$ and sum $b$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Factoring $x^{2} + 25$ as $(x + 5)(x + 5)$ or $(x + 5)(x - 5)$.
- Calling $x^{2} + 13x + 36$ a perfect square because $36 = 6^{2}$.
- Stopping after one pass on $x^{4} - 16$.
- Using product $c$ instead of product $ac$ when the leading coefficient is not 1.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u2-l4-we1` — Factor $49x^{2} - 81$ and $x^{4} - 16$ completely.
- `im2-u2-l4-we2` — Decide whether $x^{2} + 12x + 36$ and $x^{2} + 13x + 36$ are perfect-square trinomials, and factor both.
- `im2-u2-l4-we3` — Factor $6x^{2} + 19x + 10$ using the ac-method.
- `im2-u2-l4-we4` — Factor $8x^{3} - 18x$ completely, and then $3x^{2} - 14x + 8$.

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
| mean | **дундаж** | ministry standard |
| product | **үржвэр** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| number | **тоо** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| square | **квадрат** | ministry standard |
| system | **систем** | ministry standard |
| time | **цаг** | already on the site |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| difference | **ялгавар** | ministry standard |
| form | **хэлбэр** | ministry standard |
| part | **хэсэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## the-polynomial-system

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u2-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u2-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## multiplying-polynomials

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u2-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u2-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u2-l1-we1` and so on) exactly
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

- **Олон гишүүнт ба задаргаа (10-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

