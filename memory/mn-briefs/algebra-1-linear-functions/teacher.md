# MN authoring brief — Linear Functions & Slope

**Topic** `algebra-1/linear-functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/linear-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `slope`

**Able to:** Compute slope from two points, classify positive/negative/zero/undefined slopes, and read slope as a real-world rate.

**The idea that carries it:** m = (y₂ − y₁)/(x₂ − x₁): rise over run, subtracted in the same order — a rate that's the same between any two points of a line.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Mixing subtraction orders: $\frac{y_2 - y_1}{x_1 - x_2}$.
- Calling a horizontal line's slope 'undefined.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al51-we1` — Find the slope of the line through $(-2, 5)$ and $(4, -7)$.
- `al51-we2` — A climber is at 1200 m at 9:00 and at 1650 m at 12:00. What is the average climbing rate?

**2 try-it problems**, same freedom and same condition.

### 2. `slope-intercept-form`

**Able to:** Read m and b from an equation or a context, graph a line from slope-intercept form, and write the form from a graph.

**The idea that carries it:** y = mx + b: start at (0, b), march by the slope; in applications b is the fixed start and m the per-unit rate.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $y = 4 - 3x$ as slope 4, intercept $-3$.
- Marching the slope backwards: for $m = -\frac{3}{2}$ going right 3, down 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al52-we1` — For $y = -\dfrac{3}{2}x + 4$: state the slope and intercept, and find two more points for the graph.
- `al52-we2` — A gym charges a \$50 joining fee and \$30 per month. Write the total cost $C(m)$ after $m$ months, and find when the total reaches \$290.

**2 try-it problems**, same freedom and same condition.

### 3. `point-slope-and-standard-form`

**Able to:** Write equations with point-slope form from a point and slope or from two points, convert between forms, and use intercepts to graph standard form.

**The idea that carries it:** Point-slope y − y₁ = m(x − x₁) builds a line from any point plus the rate; standard form Ax + By = C graphs fastest through its two intercepts.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Sign slips inside point-slope: through $(-2, 7)$ writing $y - 7 = m(x - 2)$.
- Reading the slope of $2x + 3y = 12$ as 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al53-we1` — Write the equation of the line through $(-2, 7)$ with slope $-3$, in slope-intercept form.
- `al53-we2` — Find the equation of the line through $(2, -1)$ and $(6, 7)$.

**2 try-it problems**, same freedom and same condition.

### 4. `parallel-and-perpendicular-lines`

**Able to:** Use slope criteria for parallel and perpendicular lines, and write the equation of a line through a point parallel or perpendicular to a given line.

**The idea that carries it:** Parallel ⟺ same slope; perpendicular ⟺ slopes multiply to −1 (flip and negate) — then point-slope finishes the job.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Perpendicular = just the opposite sign: taking $-2$ as perpendicular to 2.
- Perpendicular = just the reciprocal: taking $\frac{1}{2}$ for 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al54-we1` — Write the line through $(6, -2)$ parallel to $y = \dfrac{2}{3}x + 5$.
- `al54-we2` — Write the line through $(4, 1)$ perpendicular to $y = 2x - 3$.

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
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| line | **шулуун** | ministry standard |
| rate | **хурдац** | already on the site |
| parallel | **параллель** | ministry standard |
| slope | **налалт** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| formula | **томьёо** | ministry standard |
| graph | **график** | ministry standard |
| algebra | **алгебр** | ministry standard |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |
| form | **хэлбэр** | ministry standard |

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
## slope

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al51-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al51-t1:
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

WORKED al52-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al52-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al51-we1` and so on) exactly
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

