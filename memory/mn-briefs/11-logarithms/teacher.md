# MN authoring brief — Logarithms

**Topic** `11/logarithms` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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

A student finishes this topic holding these ideas. Everything else in the
brief serves them.

1. **A logarithm is an exponent.** `log_b(x)` is the answer to "what power of b gives x?" — nothing more. Every law follows from that one sentence, and a student who holds it can derive the laws instead of memorising them. One who does not will confuse all three forever.

2. **The laws are the exponent laws, read backwards.** Multiplication becomes addition, division becomes subtraction, a power becomes a coefficient. Show the pair side by side and three rules become one idea.

3. **The domain is the trap.** You cannot take the log of zero or a negative number, so solving a logarithmic equation always ends with checking the solutions against the original — and the check throws answers away. That step is not optional bookkeeping; it is part of the answer.

**The error to design against:** Treating log(a + b) as log a + log b. There is no law for the log of a sum, and the false symmetry with the product law makes it near-universal. Disprove it with numbers early.

If your Mongolian version lands those and a student can do the practice
set, the topic is right — however you got there.

Each lesson, and what the student must end up able to do:

### 1. `meet-logarithms`

**Able to:** Read and write logarithms as 'what exponent?' questions, converting fluently between $b^y = x$ and $\log_b x = y$.

**The idea that carries it:** log_b x = y ⟺ b^y = x — the log IS the exponent. Only positive inputs have logs.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $\log_2 32$ as $32 \div 2$ or $2 \times 32$.
- Taking the log of a negative number or zero.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lg1-we1` — Evaluate $\log_2 32$ and $\log_3 81$.
- `lg1-we2` — Convert $5^3 = 125$ to log form, and $\log_4 64 = 3$ to exponential form.
- `lg1-we3` — Solve for $x$: $\log_2 x = 6$.

**2 try-it problems**, same freedom and same condition.

### 2. `evaluating-logarithms`

**Able to:** Evaluate logs instantly at the special values (1, the base, powers and reciprocal powers of the base) including negative and fractional answers.

**The idea that carries it:** Anchors: log_b 1 = 0, log_b b = 1; reciprocals negative, roots fractional; bare log = base 10.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Guessing $\log_b 1 = 1$.
- Calling $\log_2 \tfrac18$ 'undefined because it's a fraction'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lg2-we1` — Evaluate $\log_7 1$, $\log_7 7$, and $\log_7 49$.
- `lg2-we2` — Evaluate $\log_2 \tfrac{1}{8}$ and $\log_5 \tfrac{1}{25}$.
- `lg2-we3` — Evaluate $\log_9 3$ and $\log 100000$.

**2 try-it problems**, same freedom and same condition.

### 3. `log-laws`

**Able to:** Apply the product, quotient, and power laws to expand, condense, and evaluate logarithmic expressions.

**The idea that carries it:** Logs turn × into +, ÷ into −, and powers into multipliers — the exponent laws, seen from below.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting a sum: $\log(x+y) = \log x + \log y$.
- Reading $\log x^n$ as $(\log x)^n$.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lg3-we1` — Verify the product law on $\log_2(8 \cdot 4)$.
- `lg3-we2` — Evaluate $\log_3 54 - \log_3 2$.
- `lg3-we3` — Evaluate $2\log 5 + \log 4$ (base 10).

**2 try-it problems**, same freedom and same condition.

### 4. `solving-exponential-equations`

**Able to:** Solve exponential equations by matching bases or by taking logs, isolating the exponential first.

**The idea that carries it:** Match bases if you can; otherwise isolate b^x and apply x = log_b c. Bracket the answer between whole powers.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Logging before isolating: taking logs of $5 \cdot 2^x = 40$ term-by-term.
- Equating exponents across DIFFERENT bases.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lg4-we1` — Solve $2^{x+1} = 32$.
- `lg4-we2` — Solve $5 \cdot 2^x = 40$.
- `lg4-we3` — Solve $9^x = 27$ (match bases through 3).

**2 try-it problems**, same freedom and same condition.

### 5. `solving-log-equations`

**Able to:** Solve logarithmic equations by converting to exponential form (or equating insides), rejecting candidates outside the domain.

**The idea that carries it:** Isolate → exponential clothes (or equate insides). Then check: every log's inside must stay positive — fakes get rejected.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Skipping the domain check after condensing.
- Converting $\log_3(x+2) = 2$ to $x + 2 = 2^3$.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lg5-we1` — Solve $\log_3(x+2) = 2$.
- `lg5-we2` — Solve $\log_5(2x-1) = \log_5(x+3)$.
- `lg5-we3` — Solve $\log_2 x + \log_2(x-2) = 3$.

**2 try-it problems**, same freedom and same condition.

### 6. `log-scales`

**Able to:** Read and compare log-scale measurements (Richter, decibels, pH), converting scale differences into real-world ratios.

**The idea that carries it:** Log scales turn ratios into differences: each step = one ×factor. Difference of d steps = 10^d in reality (Richter, pH; dB use steps of 10).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading scale differences as real differences: 'mag 7 is 2 units worse than mag 5'.
- Doubling the reading to double the quantity: '6 dB is twice 3 dB'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lg6-we1` — How much harder does a magnitude 7 quake shake than a magnitude 5?
- `lg6-we2` — A concert is 90 dB; a conversation 60 dB. Intensity ratio?
- `lg6-we3` — Soda has pH 3, water pH 7. How many times more acidic is the soda?

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
| base | **суурь** | ministry standard |
| scale | **томсгох** | already on the site |
| measure | **хэмжих** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| product | **үржвэр** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| difference | **ялгавар** | ministry standard |
| quotient | **ногдвор** | ministry standard |
| form | **хэлбэр** | ministry standard |
| root | **язгуур** | ministry standard |
| answer | **хариулт** | already on the site |
| positive | **эерэг** | ministry standard |
| inverse | **урвуу** | ministry standard |
| definition | **тодорхойлолт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

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
## meet-logarithms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED lg1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY lg1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## evaluating-logarithms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED lg2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY lg2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`lg1-we1` and so on) exactly
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

- **Логарифм (11-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

