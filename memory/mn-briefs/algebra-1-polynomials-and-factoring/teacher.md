# MN authoring brief — Polynomials & Factoring

**Topic** `algebra-1/polynomials-and-factoring` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/polynomials-and-factoring`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `polynomial-arithmetic`

**Able to:** Add, subtract, and multiply polynomials, tracking signs through subtraction and pairing every term in products.

**The idea that carries it:** Add by sorting like terms, subtract by flipping every sign of the second polynomial, multiply by pairing every term with every term.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Subtracting only the first term: $(4x^2 \ldots) - (x^2 + 5x - 2) = 3x^2 + 5x - 2 \ldots$
- Multiplying binomials as first×first + last×last: $(x+3)(x+5) = x^2 + 15$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al71-we1` — Subtract: $(4x^2 - 3x + 6) - (x^2 + 5x - 2)$.
- `al71-we2` — Multiply: $(x + 3)(2x^2 - x + 4)$.

**2 try-it problems**, same freedom and same condition.

### 2. `special-products`

**Able to:** Expand (a+b)², (a−b)², and (a+b)(a−b) by formula, and use them for mental arithmetic and later factoring.

**The idea that carries it:** (a ± b)² = a² ± 2ab + b², and (a + b)(a − b) = a² − b² — three products fast enough to be reflexes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- $(a + b)^2 = a^2 + b^2$.
- $(a - b)^2 = a^2 - b^2$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al72-we1` — Expand $(3x + 4)^2$ and $(2x - 5)^2$.
- `al72-we2` — Compute $102 \times 98$ without a calculator.

**2 try-it problems**, same freedom and same condition.

### 3. `gcf-and-factoring-trinomials`

**Able to:** Factor out the greatest common factor, and factor trinomials x² + bx + c by the product-sum puzzle, using signs to narrow the search.

**The idea that carries it:** GCF first, always; then x² + bx + c = (x + p)(x + q) where pq = c and p + q = b — let the signs of b and c tell you where to look.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Skipping the GCF: factoring $2x^2 + 10x + 12$ straight into $(2x + 4)(x + 3)$ or getting stuck.
- Ignoring signs in the puzzle: factoring $x^2 - 2x - 15$ with $+5, -3$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al73-we1` — Factor $x^2 + 7x + 12$ and $x^2 - 9x + 20$.
- `al73-we2` — Factor completely: $3x^3 - 3x^2 - 36x$.

**2 try-it problems**, same freedom and same condition.

### 4. `factoring-ax2-and-special-patterns`

**Able to:** Factor ax² + bx + c by splitting the middle term (ac-method), factor differences of squares and perfect-square trinomials, and combine tools to factor completely.

**The idea that carries it:** For a ≠ 1: split bx using two numbers with product ac and sum b, then group; keep the reversed special products loaded, and factor until nothing budges.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- 'Factoring' a sum of squares: $x^2 + 16 = (x + 4)(x - 4)$ or $(x+4)^2$.
- Declaring a perfect square from the ends alone: $x^2 + 7x + 25 = (x+5)^2$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al74-we1` — Factor $3x^2 - 10x + 8$.
- `al74-we2` — Factor completely: $50x^2 - 8$ and $4x^2 + 12x + 9$.

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
| factor | **хуваагч** | ministry standard |
| product | **үржвэр** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| number | **тоо** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| square | **квадрат** | ministry standard |
| subtraction | **хасалт** | already on the site |
| formula | **томьёо** | ministry standard |
| difference | **ялгавар** | ministry standard |
| second | **хоёр дахь** | ministry standard |
| subtracting | **хасах** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| pair | **хос** | ministry standard |
| subtract | **хасах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## polynomial-arithmetic

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al71-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al71-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## special-products

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al72-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al72-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al71-we1` and so on) exactly
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

