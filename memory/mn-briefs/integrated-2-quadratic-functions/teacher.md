# MN authoring brief — Quadratic Functions

**Topic** `integrated-2/quadratic-functions` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/quadratic-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `introducing-the-parabola`

**Able to:** Recognise a quadratic function from its equation, its table and its graph, and identify the vertex, the axis of symmetry, the intercepts and the direction of opening.

**The idea that carries it:** Every quadratic graph is a parabola with an axis of symmetry through its vertex; the sign of $a$ says which way it opens and the constant term is the $y$-intercept.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting the axis of symmetry as the vertex.
- Forgetting the minus in $x = -\frac{b}{2a}$.
- Concluding a table is quadratic from non-constant first differences alone.
- Saying 'the maximum is at $x = 2$' when asked for the maximum value.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u3-l1-we1` — For $f(x) = x^{2} - 6x + 5$, find the axis of symmetry, the vertex, the $y$-intercept, and say which way the parabola opens.
- `im2-u3-l1-we2` — A table gives $y$ at $x = 0, 1, 2, 3, 4$ as $3, 4, 9, 18, 31$. Show the relationship is quadratic and find the leading coefficient.
- `im2-u3-l1-we3` — For $g(x) = -2x^{2} + 8x - 3$, find the vertex and state the maximum value of the function.
- `im2-u3-l1-we4` — A ball is thrown upward from a $1.5$ m platform; its height in metres after $t$ seconds is $h(t) = -5t^{2} + 20t + 1.5$. Find when it reaches its grea

**2 try-it problems**, same freedom and same condition.

### 2. `the-three-forms`

**Able to:** Read the roots from factored form, the vertex from vertex form, and the $y$-intercept from standard form; and choose the form that answers the question being asked.

**The idea that carries it:** The three forms are the same function wearing different labels; each makes one feature free to read and the others require work.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the roots of $(x + 3)(x - 4)$ as $3$ and $-4$.
- Reading the vertex of $2(x + 5)^{2} - 1$ as $(5, -1)$.
- Assuming two roots determine the parabola uniquely.
- Expanding to standard form before answering a question the other form already answered.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u3-l2-we1` — For $f(x) = 2(x - 3)(x + 5)$, find the roots, the axis of symmetry, the vertex and the $y$-intercept.
- `im2-u3-l2-we2` — For $g(x) = -3(x + 2)^{2} + 12$, state the vertex, the direction of opening, the maximum or minimum value, and find the roots.
- `im2-u3-l2-we3` — A parabola has roots at $x = -1$ and $x = 7$ and passes through $(0, -14)$. Find its equation in factored form, then locate its vertex.
- `im2-u3-l2-we4` — The same parabola is written three ways: $y = x^{2} - 4x - 5$, $y = (x - 5)(x + 1)$, and $y = (x - 2)^{2} - 9$. Confirm they agree, and say which form

**2 try-it problems**, same freedom and same condition.

### 3. `transforming-parabolas`

**Able to:** Describe and apply vertical and horizontal shifts, vertical stretches and reflections to $y = x^{2}$, and write the equation of a transformed parabola.

**The idea that carries it:** $y = a(x - h)^{2} + k$ is an instruction sheet: stretch $y = x^{2}$ by $a$, then move it $h$ right and $k$ up.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $(x - 4)^2$ as a shift four units LEFT.
- Treating $y = (x - 3)^2$ and $y = x^2 - 3$ as the same curve.
- Believing a negative $k$ means the parabola has no maximum.
- Applying the translation before the stretch when writing the equation.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u3-l3-we1` — Describe how $y = (x - 4)^{2} + 3$ is obtained from $y = x^{2}$, and state its vertex.
- `im2-u3-l3-we2` — Describe the transformations in $y = -2(x + 1)^{2} - 5$ and state the vertex, direction of opening and maximum or minimum value.
- `im2-u3-l3-we3` — Write the equation of the parabola obtained by taking $y = x^{2}$, reflecting it in the horizontal axis, stretching it by a factor of $3$, and moving 
- `im2-u3-l3-we4` — Two parabolas: $y = (x - 3)^{2}$ and $y = x^{2} - 3$. Explain why they are different curves, and give a point that lies on one but not the other.

**2 try-it problems**, same freedom and same condition.

### 4. `comparing-growth-rates`

**Able to:** Distinguish linear, quadratic and exponential growth from tables, graphs and equations, compute average rates of change, and explain why exponential growth eventually dominates.

**The idea that carries it:** Constant first differences means linear, constant second differences means quadratic, constant ratios means exponential — and exponential always wins in the end.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling a table quadratic because the values 'grow faster and faster'.
- Treating average rate of change as a property of the function rather than an interval.
- Concluding from a short table that a quadratic beats an exponential.
- Using a linear model for a fixed-percentage situation.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u3-l4-we1` — Three tables at $x = 0, 1, 2, 3, 4$: A gives $5, 8, 11, 14, 17$; B gives $2, 3, 6, 11, 18$; C gives $3, 6, 12, 24, 48$. Identify each type.
- `im2-u3-l4-we2` — For $f(x) = x^{2} + 1$, compute the average rate of change on $[0, 1]$, $[1, 2]$ and $[2, 3]$. What pattern appears, and what does it say about the fu
- `im2-u3-l4-we3` — Compare $q(x) = x^{2}$ and $e(x) = 2^{x}$ at $x = 1, 2, 3, 4, 5, 6$. Find where the exponential overtakes for good, and explain why it must.
- `im2-u3-l4-we4` — Three savings plans start at $100{,}000$ tugriks. Plan A adds $20{,}000$ per year. Plan B follows $100{,}000 + 5{,}000t^{2}$. Plan C grows $15\%$ per 

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
| feature | **шинж** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| product | **үржвэр** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| rate | **хурдац** | already on the site |
| zero | **тэг** | ministry standard |
| parabola | **парабол** | already on the site |
| growth | **өсөлт** | already on the site |
| table | **хүснэгт** | ministry standard |
| vertical | **босоо** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## introducing-the-parabola

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u3-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u3-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-three-forms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u3-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u3-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u3-l1-we1` and so on) exactly
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

- **Квадрат функц (10-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

