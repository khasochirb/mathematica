# MN authoring brief — Linear Functions & Modelling

**Topic** `integrated-1/linear-functions` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/linear-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `slope-as-rate-of-change`

**Able to:** Compute slope from two points, from a table, and from a graph; interpret it as a rate of change with units; and recognise a constant rate of change as the signature of a linear relationship.

**The idea that carries it:** Slope = change in output ÷ change in input, with units attached. A relationship is linear exactly when that ratio is the same for every pair of points.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reversing only the numerator: writing (y₂ − y₁)/(x₁ − x₂).
- Computing run over rise instead of rise over run.
- Calling a vertical line's slope zero.
- Declaring a table linear after checking only one pair of rows.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u4-l1-we1` — Find the slope of the line through $(2, 5)$ and $(6, 17)$.
- `im1-u4-l1-we2` — A taxi's fare is $3200$₮ after $2$ km and $8600$₮ after $8$ km. Find the rate per kilometre and state its units.
- `im1-u4-l1-we3` — Decide whether each table is linear. Table A: $(0, 4), (1, 7), (2, 10), (3, 13)$. Table B: $(0, 2), (1, 4), (2, 8), (3, 16)$.
- `im1-u4-l1-we4` — A tank drains from $450$ litres at time $0$ to $210$ litres after $20$ minutes. Find the rate of change, interpret its sign, and predict the volume at

**3 try-it problems**, same freedom and same condition.

### 2. `slope-intercept-form`

**Able to:** Read the slope and $y$-intercept from $y = mx + b$, graph a line from them, find both intercepts, and write the equation of a line from its graph.

**The idea that carries it:** In $y = mx + b$, plot $(0, b)$ and then step by the slope. The $y$-intercept is the value at $x = 0$; the $x$-intercept is found by setting $y = 0$ and solving.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading b as the x-intercept.
- Stepping a negative slope leftward and upward.
- Reading m straight off 3x + 2y = 12 as 3.
- Reading slope off a graph using points the line does not pass through exactly.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u4-l2-we1` — Graph $y = \frac{3}{4}x - 2$ by identifying its slope and $y$-intercept, and give a third point as a check.
- `im1-u4-l2-we2` — Find both intercepts of $y = -2x + 10$ and say what each would mean if $x$ were hours worked and $y$ were litres of fuel remaining.
- `im1-u4-l2-we3` — A line passes through $(0, 7)$ and $(4, -1)$. Write its equation in slope-intercept form.
- `im1-u4-l2-we4` — Rewrite $3x + 2y = 12$ in slope-intercept form, then find both intercepts.

**3 try-it problems**, same freedom and same condition.

### 3. `point-slope-and-standard-form`

**Able to:** Write the equation of a line from a point and a slope, or from two points, using point-slope form; convert between point-slope, slope-intercept and standard form; and choose the form that fits the information available.

**The idea that carries it:** Point-slope $y - y_1 = m(x - x_1)$ is the slope formula with the fraction cleared. Use it whenever you have a point that is not the $y$-intercept, then simplify to $y = mx + b$ if you want to graph.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing y − 5 = m(x − 3) for a line through (−3, 5).
- Checking the answer against the point you already used.
- Leaving fractions in standard form.
- Trying to write a vertical line as y = mx + b.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u4-l3-we1` — Write the equation of the line through $(2, -1)$ with slope $4$, in point-slope form and then in slope-intercept form.
- `im1-u4-l3-we2` — Write the equation of the line through $(-3, 5)$ and $(1, -7)$.
- `im1-u4-l3-we3` — Convert $y = \frac{2}{5}x - 3$ to standard form with integer coefficients.
- `im1-u4-l3-we4` — A student sells notebooks at $3000$₮ and pens at $1200$₮, taking $60\,000$₮ in total. Write the relationship in standard form, find both intercepts, a

**3 try-it problems**, same freedom and same condition.

### 4. `interpreting-linear-models`

**Able to:** Interpret the slope, intercepts and domain of a linear model in the language of the situation; use the model to predict and to solve backwards; and judge when a prediction has left the range the model can support.

**The idea that carries it:** Intercept = the starting value; slope = the change per unit, with units and a sign; $x$-intercept = when the quantity hits zero. Predict inside your data, and be honest about extrapolation.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Describing the slope as 'steepness' instead of a rate in context.
- Dropping the sign when interpreting a negative slope.
- Reporting an extrapolated value with no caveat.
- Answering 'they are equal at 1200 pages' and stopping.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u4-l4-we1` — A gym charges a joining fee plus a monthly rate, modelled by $C = 25\,000m + 60\,000$ where $m$ is months. Interpret both numbers, find the cost of a 
- `im1-u4-l4-we2` — A candle's height is $h = 24 - 4t$ (cm, hours). Interpret each number, find when it burns out, and state the valid domain and range.
- `im1-u4-l4-we3` — A child's height between ages $5$ and $10$ fits $H = 6a + 80$ (cm, years). Predict the height at age $8$, then at age $40$, and comment on both.
- `im1-u4-l4-we4` — Printer A costs $40\,000$₮ plus $80$₮ per page; printer B costs $100\,000$₮ plus $30$₮ per page. Which is cheaper, and when?

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
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| fraction | **бутархай** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| line | **шулуун** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| rate | **хурдац** | already on the site |
| domain | **тодорхойлогдох муж** | ministry standard |
| slope | **налалт** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| formula | **томьёо** | ministry standard |
| table | **хүснэгт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

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
## slope-as-rate-of-change

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u4-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u4-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## slope-intercept-form

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u4-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u4-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u4-l1-we1` and so on) exactly
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

