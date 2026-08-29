# MN authoring brief — Exponential Functions & Growth

**Topic** `integrated-1/exponential-functions` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/exponential-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `exponential-growth-and-decay`

**Able to:** Recognise a constant percent rate of change, convert a percent to a growth or decay factor, write the model $y = a \cdot b^{x}$, and interpret $a$ and $b$ in context.

**The idea that carries it:** $y = a \cdot b^{x}$: $a$ is the starting value, $b$ is the factor per step. Growth of $p\%$ gives $b = 1 + p/100$; decay gives $b = 1 - p/100$. The factor is what survives, and repeated steps compound.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using 0.15 as the factor for a 15% loss.
- Treating five years of 3% growth as a 15% rise.
- Applying the arithmetic-sequence formula to a table with constant ratios.
- Assuming a 40% rise followed by a 40% fall returns to the start.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u6-l1-we1` — A town of $40\,000$ people grows $3\%$ a year. Write the model and find the population after $5$ years.
- `im1-u6-l1-we2` — A car bought for $32\,000\,000$₮ loses $18\%$ of its value each year. Write the model and find its value after $4$ years.
- `im1-u6-l1-we3` — Decide whether each table is linear or exponential, and give its model. Table A: $(0, 5), (1, 8), (2, 11), (3, 14)$. Table B: $(0, 5), (1, 15), (2, 45
- `im1-u6-l1-we4` — A model reads $N = 250 \cdot (1.4)^{t}$. State the starting value, the percent growth per period, and the value after $3$ periods. Then say how the an

**3 try-it problems**, same freedom and same condition.

### 2. `graphs-of-exponential-functions`

**Able to:** Graph $y = a \cdot b^{x}$ from a table of values, identify the $y$-intercept and the horizontal asymptote, and describe the end behaviour of a growth curve and a decay curve.

**The idea that carries it:** $y = a \cdot b^{x}$ crosses the vertical axis at $a$, never crosses the horizontal axis, and approaches $y = 0$ at one end while growing without bound at the other.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Claiming an exponential graph has an x-intercept.
- Reading 2⁻³ as a negative number.
- Thinking a bigger base moves the y-intercept.
- Drawing an exponential curve as a straight line through the plotted points.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u6-l2-we1` — Make a table for $y = 2^{x}$ at $x = -2, -1, 0, 1, 2, 3$ and describe the graph.
- `im1-u6-l2-we2` — Describe the graph of $y = 5 \cdot \left(\frac{1}{2}\right)^{x}$, including its intercept, asymptote and end behaviour.
- `im1-u6-l2-we3` — Two functions: $f(x) = 3 \cdot 2^{x}$ and $g(x) = 3 \cdot 4^{x}$. Compare their graphs.
- `im1-u6-l2-we4` — A cup of tea cools so that its temperature above room temperature is $T = 60 \cdot (0.8)^{m}$ degrees, with $m$ in minutes and room temperature $20°$C

**3 try-it problems**, same freedom and same condition.

### 3. `linear-versus-exponential`

**Able to:** Compare linear and exponential models numerically and graphically, locate the crossover, and state why an exponential quantity eventually exceeds any linear one.

**The idea that carries it:** An exponential with base above $1$ eventually exceeds ANY linear function, because its step size grows while the line's stays fixed. It may start far behind, and the crossover is found by table or graph.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Concluding the linear model wins because it leads over the range you checked.
- Reading '7% per year' as a constant amount and modelling it linearly.
- Trying to solve 2ˣ = 1000x algebraically in IM1.
- Assuming a steeper line must beat a shallow curve.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u6-l3-we1` — Compare $L(x) = 100x + 50$ with $E(x) = 2 \cdot 3^{x}$ at $x = 1, 3, 5$ and $7$. Where does the exponential overtake?
- `im1-u6-l3-we2` — A job pays $1$₮ on day $1$, doubling each day. Another pays $1\,000\,000$₮ flat per day. Compare the DAILY pay on days $10$, $20$, $25$ and $31$.
- `im1-u6-l3-we3` — Decide whether each situation is linear or exponential, and say why. (a) A phone plan charges $18\,000$₮ plus $40$₮ a minute. (b) A savings account pa
- `im1-u6-l3-we4` — Investment A starts at $5\,000\,000$₮ and adds $400\,000$₮ a year. Investment B starts at $3\,000\,000$₮ and grows $12\%$ a year. Which is worth more 

**3 try-it problems**, same freedom and same condition.

### 4. `modelling-with-exponentials`

**Able to:** Construct $y = a \cdot b^{x}$ from a description, a table, or two data points; handle doubling time and half-life; and use the model to predict and to solve backwards by table.

**The idea that carries it:** $a$ is the value at $x = 0$; $b$ is the factor per step, found by dividing consecutive values — or by taking the $n$-th root when the points are $n$ steps apart. Check the finished model on every data point.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the ratio between two points that are several steps apart as b.
- Writing y = a·(0.5)ᵗ for a quantity that halves every 4 hours.
- Fitting to two points and never checking the rest of the data.
- Reporting a long extrapolation with no caveat.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u6-l4-we1` — A table shows $(0, 6), (1, 18), (2, 54), (3, 162)$. Build the exponential model and predict the value at $x = 6$.
- `im1-u6-l4-we2` — An exponential model passes through $(0, 5)$ and $(3, 40)$. Find $b$ and write the model.
- `im1-u6-l4-we3` — A drug's concentration starts at $200$ mg and halves every $4$ hours. Write the model and find the concentration after $10$ hours.
- `im1-u6-l4-we4` — A town's population was $18\,000$ in $2015$ and $22\,500$ in $2020$. Assuming exponential growth, find the annual rate and predict $2030$.

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
| shape | **дүрс** | ministry standard |
| factor | **хуваагч** | ministry standard |
| half | **хагас** | already on the site |
| base | **суурь** | ministry standard |
| size | **хэмжээ** | ministry standard |
| function | **функц** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| line | **шулуун** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| rate | **хурдац** | already on the site |
| time | **цаг** | already on the site |
| exponent | **илтгэгч** | ministry standard |
| growth | **өсөлт** | already on the site |
| asymptote | **асимптот** | already on the site |
| table | **хүснэгт** | ministry standard |
| vertical | **босоо** | ministry standard |
| graph | **график** | ministry standard |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## exponential-growth-and-decay

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u6-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u6-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## graphs-of-exponential-functions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u6-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u6-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u6-l1-we1` and so on) exactly
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

