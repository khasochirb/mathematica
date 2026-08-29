# MN authoring brief — Quadratics & Complex Numbers

**Topic** `algebra-2/quadratics-and-complex-numbers` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/quadratics-and-complex-numbers`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `vertex-form-and-completing-the-square`

**Able to:** Convert between standard and vertex form by completing the square, and read the vertex, axis, and max/min directly.

**The idea that carries it:** Vertex form displays the vertex; completing the square — add and subtract (b/2)², factoring a out first if needed — converts any quadratic into it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Completing the square with a leading coefficient still attached: from $2x^2 - 12x$, adding $36$.
- Reading the vertex of $y = (x + 3)^2 - 8$ as $(3, -8)$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a221-we1` — Write $y = x^2 - 8x + 11$ in vertex form and give the vertex and minimum value.
- `a221-we2` — Convert $y = 2x^2 - 12x + 5$ to vertex form.

**2 try-it problems**, same freedom and same condition.

### 2. `complex-numbers`

**Able to:** Compute with i (powers, add/subtract/multiply, conjugates and division), and simplify square roots of negatives.

**The idea that carries it:** i² = −1 and everything else is polynomial arithmetic: like parts add, FOIL multiplies, conjugates turn denominators real, and powers of i cycle every 4.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- $\sqrt{-4} \cdot \sqrt{-9} = \sqrt{36} = 6$.
- Leaving $i^2$ alive in an answer: $(2+3i)(4-i) = 8 + 10i - 3i^2$, done.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a222-we1` — Simplify $(5 - 2i) - (3 + 4i)$ and $(2 + 3i)(4 - i)$.
- `a222-we2` — Write $\dfrac{3 + i}{2 - i}$ in the form $a + bi$.

**2 try-it problems**, same freedom and same condition.

### 3. `the-quadratic-formula-and-complex-roots`

**Able to:** Solve any quadratic with the formula, classify roots by the discriminant, and connect complex roots to a graph that misses the x-axis.

**The idea that carries it:** With i, the quadratic formula never fails: D < 0 yields a conjugate pair p ± qi, and the graph shows it by floating clear of the x-axis.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Halting at $D < 0$ with 'no solutions.'
- Forgetting to divide BOTH terms by $2a$: $\frac{4 \pm 6i}{2} = 2 \pm 6i$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a223-we1` — Solve $x^2 - 4x + 13 = 0$.
- `a223-we2` — Solve $2x^2 + 2x + 5 = 0$ and verify the roots are conjugates.

**2 try-it problems**, same freedom and same condition.

### 4. `quadratic-inequalities`

**Able to:** Solve quadratic inequalities by finding roots and reading the parabola's sign between and beyond them.

**The idea that carries it:** Roots first, picture second: an upward parabola is negative between its roots and positive outside; no roots means one-sided forever.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Solving $x^2 < 9$ as $x < 3$.
- Dividing an inequality by a negative without flipping: $-5t^2 + 30t - 40 > 0 \to t^2 - 6t + 8 > 0$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a224-we1` — Solve $x^2 - 2x - 8 \le 0$.
- `a224-we2` — A ball's height is $h(t) = -5t^2 + 30t$ m. For which times is it above 40 m?

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
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| division | **хуваалт** | ministry standard |
| product | **үржвэр** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| number | **тоо** | ministry standard |
| square | **квадрат** | ministry standard |
| parabola | **парабол** | already on the site |
| formula | **томьёо** | ministry standard |
| graph | **график** | ministry standard |
| quadratic | **квадрат** | ministry standard |
| form | **хэлбэр** | ministry standard |
| root | **язгуур** | ministry standard |
| vertex | **орой** | ministry standard |

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
## vertex-form-and-completing-the-square

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a221-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a221-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## complex-numbers

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a222-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a222-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a221-we1` and so on) exactly
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

