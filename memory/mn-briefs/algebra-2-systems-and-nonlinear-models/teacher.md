# MN authoring brief — Systems & Nonlinear Models

**Topic** `algebra-2/systems-and-nonlinear-models` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/systems-and-nonlinear-models`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `linear-systems-and-modeling`

**Able to:** Solve 2×2 linear systems fluently by substitution and elimination, classify special cases, and translate two-condition stories into systems.

**The idea that carries it:** Substitute when a variable is alone, eliminate otherwise; 0 = false means parallel (none), 0 = 0 means same line (infinite) — and always check the pair in both equations.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding equations without scaling first: $2x + 3y = 12$ plus $4x - y = 10$ gives $6x + 2y = 22$ — nothing cancelled.
- Checking the solution in only one equation.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a231-we1` — Solve the system $2x + 3y = 12$, $4x - y = 10$.
- `a231-we2` — Tickets: adults \$8, children \$5. A show sells 120 tickets for \$786. How many of each?

**2 try-it problems**, same freedom and same condition.

### 2. `three-variable-systems`

**Able to:** Solve 3×3 linear systems by staged elimination, organizing work to avoid arithmetic chaos.

**The idea that carries it:** Evict one variable twice to shrink 3×3 → 2×2, solve, then climb back up by substitution — and check the triple in all three originals.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Eliminating x from (1)&(2), then y from (2)&(3) — and stalling with two equations in different pairs of unknowns.
- Checking the final triple in just one equation.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a232-we1` — Solve: $x + y + z = 6$; $\;2x - y + z = 3$; $\;x + 2y - z = 2$.
- `a232-we2` — Three sizes: small $s$, medium $m$, large $l$ (dollars). Day 1: $2s + m + l = 13$. Day 2: $s + 2m + l = 14$. Day 3: $s + m + 2l = 17$. Find the prices

**2 try-it problems**, same freedom and same condition.

### 3. `nonlinear-systems`

**Able to:** Solve systems mixing a line with a parabola or circle by substitution, and predict the number of intersections.

**The idea that carries it:** Substitute the line into the curve: the resulting quadratic's roots are the crossing x's, and its discriminant counts them — 2, 1 (tangent), or 0.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting only the x-values as 'the solution.'
- Pairing every x with every y: roots $x = 3, -4$ and values $y = 4, -3$ becoming four points.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a233-we1` — Solve the system $y = x^2 - 2x - 3$, $\;y = x + 1$.
- `a233-we2` — For which $k$ is the line $y = 2x + k$ TANGENT to the parabola $y = x^2 + 4x + 7$?

**2 try-it problems**, same freedom and same condition.

### 4. `systems-of-inequalities`

**Able to:** Graph systems of linear inequalities as feasible regions, find corner points, and optimize a linear objective over the region.

**The idea that carries it:** Each inequality keeps a half-plane; the system keeps the overlap; and a linear objective is optimized by evaluating it at the region's corner points.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Shading the wrong side by reading the symbol off the coefficients ('$\le$ means below').
- Optimizing by trying interior points.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a234-we1` — Graph the system $x + y \le 6$, $x \ge 0$, $y \ge 0$, $y \le 2x$ and list its corner points.
- `a234-we2` — Maximize $P = 30x + 20y$ over the region with corners $(0, 0)$, $(6, 0)$, $(2, 4)$.

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
| tangent | **шүргэгч** | ministry standard |
| count | **тоолох** | ministry standard |
| half | **хагас** | already on the site |
| translate | **хөрвүүлэх** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| circle | **тойрог** | ministry standard |
| parallel | **параллель** | ministry standard |
| number | **тоо** | ministry standard |
| system | **систем** | ministry standard |
| parabola | **парабол** | already on the site |
| plane | **хавтгай** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| graph | **график** | ministry standard |
| algebra | **алгебр** | ministry standard |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

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
## linear-systems-and-modeling

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a231-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a231-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## three-variable-systems

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a232-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a232-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a231-we1` and so on) exactly
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

