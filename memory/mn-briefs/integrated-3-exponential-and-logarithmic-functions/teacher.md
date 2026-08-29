# MN authoring brief — Exponential & Logarithmic Functions

**Topic** `integrated-3/exponential-and-logarithmic-functions` · **4 lessons** · 12 worked examples · 16 practice · 8 test-yourself

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
> `integrated-3/exponential-and-logarithmic-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-logarithm-as-an-inverse`

**Able to:** Convert between exponential and logarithmic form, evaluate logarithms exactly, and state the domain of a logarithmic function.

**The idea that carries it:** $\log_b x$ is the exponent you put on $b$ to get $x$. Every evaluation, every law, every equation in this unit is that one sentence applied again.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading log_2 8 as '2 to the power 8'.
- Taking the logarithm of a negative number or of zero.
- Treating log_b x as the fraction b/x or x/b.
- Expecting logarithmic growth to be fast.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u3-l1-we1` — Evaluate exactly: (a) $\log_3 81$, (b) $\log_5 \dfrac{1}{25}$, (c) $\log_{10} 1000$.
- `im3-u3-l1-we2` — Solve for the unknown: (a) $\log_2 x = 5$, (b) $\log_x 49 = 2$.
- `im3-u3-l1-we3` — State the domain of $f(x) = \log_2(x - 3)$ and the equation of its vertical asymptote.

**3 try-it problems**, same freedom and same condition.

### 2. `the-laws-of-logarithms`

**Able to:** Expand and condense logarithmic expressions with the product, quotient and power laws, and evaluate any logarithm with the change-of-base formula.

**The idea that carries it:** Products become sums, quotients become differences, powers become multipliers — because logs are exponents and that is how exponents already behave. There is no law for $\log(x + y)$, and pretending there is one is the unit's most tempting error.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting log(x + y) into log x + log y.
- Confusing (log x)^2 with log(x^2).
- Cancelling logs across a fraction: log a / log b = log(a/b).
- Applying the power law to an exponent on the base.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u3-l2-we1` — Expand fully: $\log_2 \dfrac{8x^3}{y}$.
- `im3-u3-l2-we2` — Condense and evaluate: $2\log_{10} 5 + \log_{10} 4$.
- `im3-u3-l2-we3` — Evaluate $\log_4 8$ exactly, using the change-of-base formula with base $2$.

**3 try-it problems**, same freedom and same condition.

### 3. `solving-exponential-and-logarithmic-equations`

**Able to:** Solve exponential equations by matching bases or by taking logarithms, solve logarithmic equations by converting to exponential form, and reject candidates outside the domain.

**The idea that carries it:** Match the bases if you can; take a log if you cannot; convert to exponential form when the log surrounds the unknown. And check candidates against the original equation — condensing logs can invent solutions the same way squaring a radical does.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Logging both sides before isolating the exponential.
- Equating exponents across DIFFERENT bases.
- Keeping every root of the resulting quadratic.
- Splitting log(a + b) while un-condensing.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u3-l3-we1` — Solve $9^{x-1} = 27^{x}$.
- `im3-u3-l3-we2` — Solve $3 \cdot 2^{t} = 96$.
- `im3-u3-l3-we3` — Solve $\log_2 x + \log_2(x - 2) = 3$.

**3 try-it problems**, same freedom and same condition.

### 4. `modelling-growth-and-decay`

**Able to:** Build exponential models from growth rates, doubling times and half-lives, evaluate them, and solve them for the time variable.

**The idea that carries it:** The base is the per-step multiplier: $1 + r$ growing, $1 - r$ decaying, $2$ per doubling time, $\frac{1}{2}$ per half-life. Build the model by naming its factor; solve for time by reaching the exponent with a logarithm.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using b = r instead of b = 1 + r.
- Adding the same amount each step (linear thinking).
- Dividing the time by the wrong constant.
- Reporting the log-form answer as unfinished.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u3-l4-we1` — A town of $8000$ people grows $5\%$ per year. Write the model and find the population after $3$ years.
- `im3-u3-l4-we2` — A $96$ mg dose of a medicine has a half-life of $5$ hours. How much remains after $20$ hours?
- `im3-u3-l4-we3` — A bacteria culture of $500$ cells doubles every $3$ hours. When does it reach $16{,}000$ cells?

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
| factor | **хуваагч** | ministry standard |
| half | **хагас** | already on the site |
| base | **суурь** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| product | **үржвэр** | ministry standard |
| rate | **хурдац** | already on the site |
| domain | **тодорхойлогдох муж** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| growth | **өсөлт** | already on the site |
| radical | **язгуур** | ministry standard |
| formula | **томьёо** | ministry standard |
| difference | **ялгавар** | ministry standard |
| quotient | **ногдвор** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## the-logarithm-as-an-inverse

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u3-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u3-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-laws-of-logarithms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u3-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u3-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u3-l1-we1` and so on) exactly
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

