# MN authoring brief — Exponentials & Logarithms

**Topic** `algebra-2/exponentials-and-logarithms` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/exponentials-and-logarithms`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `exponential-growth-and-decay`

**Able to:** Model repeated-multiplication situations with f(x) = a·bˣ, distinguish growth from decay, and read a, b from stories and graphs.

**The idea that carries it:** f(x) = a·bˣ multiplies by b each step: b = 1 + r encodes percent change, growth above 1, decay below, asymptote at zero, never touching.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Encoding '+5% per year' as $b = 0.05$.
- Modeling 15% decay as subtracting 15% of the ORIGINAL each year (linear).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a261-we1` — A town of 20,000 grows 5% per year. Write the model and find the population after 3 years.
- `a261-we2` — A car worth \$24{,}000 loses 15% of its value each year. Model it and find the value after 2 years.

**2 try-it problems**, same freedom and same condition.

### 2. `logarithms-and-their-meaning`

**Able to:** Convert between exponential and logarithmic form, evaluate logs mentally, and graph log functions as reflected exponentials.

**The idea that carries it:** log_b x is the exponent b needs to reach x — the exponential's inverse: log of 1 is 0, only positives allowed, graph mirrored across y = x with a wall at x = 0.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Evaluating $\log_2 8$ as 4 ('because $8 \div 2 = 4$').
- Accepting $\log_3(-9)$ as $-2$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a262-we1` — Evaluate $\log_2 32$, $\log_9 3$, and $\log_4 \frac{1}{16}$.
- `a262-we2` — Convert $5^3 = 125$ to log form and $\log_7 x = 2$ to exponential form; solve the latter.

**2 try-it problems**, same freedom and same condition.

### 3. `properties-of-logarithms`

**Able to:** Apply the product, quotient, and power rules to expand and condense log expressions, and use the change-of-base formula.

**The idea that carries it:** Logs are exponents, so products add, quotients subtract, and powers pull out front; change of base rewrites any log as a ratio in a friendlier base.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting the log of a SUM: $\log(x + y) = \log x + \log y$.
- Turning $\frac{\log M}{\log N}$ into $\log M - \log N$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a263-we1` — Expand $\log_2 \dfrac{8x^3}{y}$ fully.
- `a263-we2` — Condense $2\log_5 x + \log_5 3 - \log_5 y$ into one logarithm, and evaluate $\log_8 32$ by change of base.

**2 try-it problems**, same freedom and same condition.

### 4. `solving-exponential-and-log-equations`

**Able to:** Solve exponential equations (matching bases or taking logs) and log equations (condensing and unwrapping), checking domains throughout.

**The idea that carries it:** Same base → equate exponents; different bases → log both sides and pull the power down; log equations condense then unwrap — and every candidate must keep all log insides positive.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- From $\log x + \log(x-6) = 4$ jumping to $x + (x - 6) = 10^4$... or worse, $= 4$.
- Keeping $x = -2$ because it solves the quadratic.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a264-we1` — Solve $5 \cdot 2^{3t} = 80$ exactly.
- `a264-we2` — Solve $\log_2(x) + \log_2(x - 6) = 4$.

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
| half | **хагас** | already on the site |
| base | **суурь** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| product | **үржвэр** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| zero | **тэг** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| growth | **өсөлт** | already on the site |
| asymptote | **асимптот** | already on the site |
| formula | **томьёо** | ministry standard |
| graph | **график** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

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

WORKED a261-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a261-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## logarithms-and-their-meaning

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a262-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a262-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a261-we1` and so on) exactly
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

