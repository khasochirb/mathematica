# MN authoring brief — Modelling with Functions

**Topic** `integrated-3/modelling-with-functions` · **4 lessons** · 12 worked examples · 16 practice · 8 test-yourself

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
> `integrated-3/modelling-with-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `choosing-a-function-family`

**Able to:** Decide from a table or a situation which function family fits — linear, exponential, or quadratic — using constant differences, constant ratios, and constant second differences, and justify the choice.

**The idea that carries it:** Over equal x-steps, the family shows itself: constant first differences mean linear, constant ratios mean exponential, constant second differences mean quadratic. Compute all three and believe the one that holds still.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Testing ratios or differences on unequal x-steps.
- Reading "grows fast" as exponential.
- Calling percent growth linear.
- Forgetting that second differences give 2a, not a.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u8-l1-we1` — For equal steps $x = 0, 1, 2, 3, 4$ a table reads $y = 7, 10, 13, 16, 19$. Identify the family and write the function.
- `im3-u8-l1-we2` — For $x = 0, 1, 2, 3$ a table reads $y = 5, 10, 20, 40$. Identify the family and write the function.
- `im3-u8-l1-we3` — For $x = 0, 1, 2, 3, 4$ a table reads $y = 3, 8, 17, 30, 47$. Identify the family and write the function.

**3 try-it problems**, same freedom and same condition.

### 2. `building-models-from-data`

**Able to:** Construct a linear function from two points, an exponential function from two points, and a quadratic function from its vertex and one point — and use each model to predict.

**The idea that carries it:** Each family is pinned by a minimal kit: two points for a line, two points for an exponential (ratios isolate the base), vertex plus one point for a parabola. Identify the kit you hold, and the equation assembles itself.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the two y-values to find a line.
- Subtracting instead of dividing for an exponential.
- Using vertex form with the vertex sign flipped.
- Solving for the base but forgetting the root.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u8-l2-we1` — A ski lift ticket costs $11$ after $2$ uses of a punch-card top-up and $26$ after $5$ uses (cost in thousands). Build the linear model and predict the
- `im3-u8-l2-we2` — A bacteria culture measures $6$ (thousand) at time $0$ hours and $48$ at $3$ hours. Build the exponential model and predict the count at $2$ hours.
- `im3-u8-l2-we3` — A drone's altitude follows a parabola whose lowest point — the vertex — is $(3, 2)$: two metres up, three seconds in. It also passes through $(5, 10)$

**3 try-it problems**, same freedom and same condition.

### 3. `residuals-and-goodness-of-fit`

**Able to:** Compute residuals, use their sizes to compare competing models, and read their pattern to detect a wrong function family — including why a residual sum of zero proves nothing.

**The idea that carries it:** A residual is actual minus predicted — the leftover the model couldn't explain. Judge models by the SIZE of their leftovers and the PATTERN: small and patternless wins; any systematic curve or trend means the wrong family was chosen.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing predicted minus actual.
- Judging fit by the residual SUM.
- Ignoring a pattern because residuals are small.
- Keeping a model that nails four points and misses one badly.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u8-l3-we1` — The model $\hat{y} = 3x + 2$ predicts a plant's height. Measurements: $16$ cm at $x = 4$ weeks and $18$ cm at $x = 6$. Compute both residuals and say 
- `im3-u8-l3-we2` — Two models predict the same four measurements. Model A leaves residuals $1, -1, 2, -2$; model B leaves $4, -3, 5, -4$. Which fits better, and by what 
- `im3-u8-l3-we3` — Data: $(1, 5), (2, 8), (3, 13), (4, 20)$. The line through the endpoints, $\hat{y} = 5x$, is proposed as a model. Compute the residuals, read their pa

**3 try-it problems**, same freedom and same condition.

### 4. `domains-and-model-breakdown`

**Able to:** Restrict a model to the domain where it means something, distinguish interpolation from extrapolation, and recognise when a model's predictions stop describing reality — however correct the algebra.

**The idea that carries it:** A model is a local law: the situation, not the formula, sets its domain. Interpolation is backed by data; extrapolation is a bet that grows wilder with distance — and every family eventually breaks, the formula never says when, and stating the border is part of the model.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Trusting the formula outside the situation.
- Treating interpolation and extrapolation as equals.
- Graphing count data as a continuous line.
- Expecting the model to announce its own breakdown.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u8-l4-we1` — A ball thrown upward has height $h = 20t - 5t^2$ metres after $t$ seconds. State the model's appropriate domain, and explain what $h(5) = -25$ does an
- `im3-u8-l4-we2` — A pine grows $0.3$ m per year and stands $2$ m today: $h = 0.3t + 2$. Evaluate the model at $t = 10$ and $t = 100$, and judge each prediction.
- `im3-u8-l4-we3` — A culture of $1000$ bacteria doubles every hour: $N = 1000 \cdot 2^t$. Evaluate at $t = 4$ hours and comment on $t = 72$ hours (three days).

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
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| base | **суурь** | ministry standard |
| size | **хэмжээ** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| line | **шулуун** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| distance | **зай** | ministry standard |
| zero | **тэг** | ministry standard |
| counting | **тоолох** | ministry standard |
| parabola | **парабол** | already on the site |
| formula | **томьёо** | ministry standard |
| table | **хүснэгт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

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
## choosing-a-function-family

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u8-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u8-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## building-models-from-data

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u8-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u8-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u8-l1-we1` and so on) exactly
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

