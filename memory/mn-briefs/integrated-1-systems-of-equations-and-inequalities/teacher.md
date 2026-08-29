# MN authoring brief — Systems of Equations & Inequalities

**Topic** `integrated-1/systems-of-equations-and-inequalities` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/systems-of-equations-and-inequalities`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `solving-systems-by-graphing`

**Able to:** Interpret the solution of a two-variable system as the intersection point of two graphs, solve a system graphically, and classify a system as having one solution, no solution, or infinitely many by comparing slopes and intercepts.

**The idea that carries it:** The solution of a system is the point lying on BOTH lines. Different slopes → one solution; same slope, different intercept → none; identical equations → infinitely many.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting a single number as the solution of a two-variable system.
- Checking the answer in only one of the two equations.
- Reading a crossing off a graph and reporting it as exact.
- Calling a system with the same slope 'no solution' without checking intercepts.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u5-l1-we1` — Solve the system graphically and check: $y = 2x - 1$ and $y = -x + 5$.
- `im1-u5-l1-we2` — Classify the system $y = 3x + 1$ and $6x - 2y = -2$ without graphing.
- `im1-u5-l1-we3` — Classify the system $y = -2x + 5$ and $4x + 2y = 3$, and explain what its graph looks like.
- `im1-u5-l1-we4` — Firm X charges $2000$₮ plus $800$₮ per km. Firm Y charges $5000$₮ plus $500$₮ per km. Set up the system, find where they agree, and say which is cheap

**3 try-it problems**, same freedom and same condition.

### 2. `substitution`

**Able to:** Solve a linear system by substitution, choosing the variable that is cheapest to isolate, and recognise the algebraic signatures of no solution and infinitely many.

**The idea that carries it:** Isolate the variable with coefficient $1$ or $-1$, substitute that whole expression in brackets into the other equation, solve, then back-substitute — and check the pair in both originals.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Substituting without brackets: writing 3·9 − 4y for 3(9 − 4y).
- Solving for one variable and stopping.
- Isolating the variable with the ugliest coefficient.
- Reporting 'no solution' when the leftover statement is TRUE.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u5-l2-we1` — Solve by substitution: $y = 3x - 4$ and $2x + y = 11$.
- `im1-u5-l2-we2` — Solve by substitution: $x + 4y = 9$ and $3x - 2y = 1$.
- `im1-u5-l2-we3` — Solve by substitution: $y = 2x + 3$ and $6x - 3y = 5$.
- `im1-u5-l2-we4` — A cinema sells adult tickets at $12\,000$₮ and student tickets at $7000$₮. One screening sold $80$ tickets and took $760\,000$₮. How many of each?

**3 try-it problems**, same freedom and same condition.

### 3. `elimination`

**Able to:** Solve a linear system by elimination, scale one or both equations to create opposite coefficients, and justify why adding two true equations produces a third true equation with the same solutions.

**The idea that carries it:** Scale one or both equations until a variable's coefficients are opposites, add to eliminate it, solve, then back-substitute. Adding equals to equals preserves the solution set.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling only the left side of an equation.
- Adding when the coefficients have the same sign.
- Eliminating a variable and forgetting to find it.
- Reporting a fractional count of physical objects as the final answer.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u5-l3-we1` — Solve by elimination: $3x + 2y = 16$ and $5x - 2y = 8$.
- `im1-u5-l3-we2` — Solve by elimination: $4x + 3y = 10$ and $2x + 5y = 16$.
- `im1-u5-l3-we3` — Solve by elimination: $2x + 3y = 12$ and $5x - 2y = 1$.
- `im1-u5-l3-we4` — A workshop makes chairs and tables. Each chair needs $3$ hours of labour and $2$ kg of timber; each table needs $5$ hours and $8$ kg. In one week it u

**3 try-it problems**, same freedom and same condition.

### 4. `systems-of-inequalities`

**Able to:** Graph the solution set of a linear inequality in two variables, find the region satisfying a system of them, and interpret that region as the set of viable options in a real constraint problem.

**The idea that carries it:** Each inequality shades a half-plane — solid edge for $\le$ or $\ge$, dashed for strict. A system's solution is the overlap, and in a real problem it is clipped by the constraints the situation imposes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Shading above whenever the symbol is > without testing.
- Drawing a solid boundary for a strict inequality.
- Shading each half-plane and calling the union the answer.
- Forgetting the x ≥ 0 and y ≥ 0 constraints in a counting problem.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u5-l4-we1` — Graph the solution set of $y \le 2x + 1$.
- `im1-u5-l4-we2` — Graph the solution set of $2x + 3y > 12$ and identify whether $(6, 1)$ belongs.
- `im1-u5-l4-we3` — Find the region satisfying $y \ge x - 2$ and $y \le -x + 6$, and give the corner where the boundaries meet.
- `im1-u5-l4-we4` — A student has $60\,000$₮ and at most $8$ hours. Each maths workbook costs $9000$₮ and takes $1$ hour to work through; each practice test costs $5000$₮

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
| half | **хагас** | already on the site |
| scale | **томсгох** | already on the site |
| edge | **ирмэг** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| line | **шулуун** | ministry standard |
| slope | **налалт** | ministry standard |
| system | **систем** | ministry standard |
| plane | **хавтгай** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| graph | **график** | ministry standard |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |
| problem | **бодлого** | ministry standard |
| opposite | **эсрэг** | already on the site |
| solid | **биет** | ministry standard |
| inequality | **тэнцэтгэл биш** | ministry standard |
| none | **ямар ч үгүй** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**edge** — proposed **ирмэг**

> POLYSEMOUS, mildly. ирмэг is the edge of a solid (shipped and ЭШ alike) and, by extension, the edge of a histogram bin («ирмэг: $20$ нь $20$–$29$-ийг эхлүүлнэ») — that is the sense proposed here. Where "edge" means the margin of something written or laid out, shipped uses зах: "Line up the decimal points, not the right edges" → «Аравтын цэгүүдийг зэрэгцүүл, баруун захыг биш». So: ирмэг for geometry and bins, зах for the right-hand edge of a written column.

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
## solving-systems-by-graphing

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u5-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u5-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## substitution

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u5-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u5-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u5-l1-we1` and so on) exactly
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

