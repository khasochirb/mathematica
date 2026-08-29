# MN authoring brief — Integrals

**Topic** `calculus/integrals` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `calculus/integrals`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `antiderivatives`

**Able to:** Find antiderivatives of powers and library functions, use the +C correctly, and pin down C from an initial condition.

**The idea that carries it:** Antiderivative: raise the power, divide by the new power, add C — a family of parallel curves; an initial condition picks the one member.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the +C — or attaching it to only some of a sum's terms.
- Reversing the power rule as 'divide by the OLD exponent': ∫x³dx = x⁴/3.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal51-we1` — Find $\int (6x^2 - 4x + 5)\,dx$ and verify by differentiating.
- `cal51-we2` — Find $F(x)$ with $F'(x) = 3x^2 - 2$ and $F(2) = 7$.

**2 try-it problems**, same freedom and same condition.

### 2. `the-area-problem-and-the-definite-integral`

**Able to:** Approximate areas with Riemann sums, define the definite integral as their limit, and interpret signed area.

**The idea that carries it:** Slice, sample, sum, and take the limit: ∫ₐᵇ f dx is the exact signed area — above the axis positive, below negative.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating the definite integral as always-positive area.
- Confusing ∫f(x)dx (a family of functions) with ∫ₐᵇf(x)dx (a number).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal52-we1` — Approximate the area under $f(x) = x^2$ on $[0, 2]$ with 4 right-endpoint rectangles, and compare with the exact value $\frac{8}{3}$.
- `cal52-we2` — Compute $\int_0^4 x \, dx$ from geometry, and check that the integral agrees.

**2 try-it problems**, same freedom and same condition.

### 3. `the-fundamental-theorem`

**Able to:** Evaluate definite integrals with the Fundamental Theorem: find an antiderivative, subtract its endpoint values.

**The idea that carries it:** ∫ₐᵇ f dx = F(b) − F(a) for any antiderivative F — accumulate by subtracting the odometer at both ends; the +C cancels itself.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Subtracting in the wrong order: F(a) − F(b).
- Evaluating only at the top limit: ∫₀³ … = F(3), forgetting F(0).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal53-we1` — Evaluate $\int_1^2 3x^2\,dx$ and $\int_0^5 2x\,dx$.
- `cal53-we2` — Evaluate $\int_0^{\pi/2} \cos x \, dx$ and $\int_0^3 (x^2 - 4)\,dx$, interpreting the second result.

**2 try-it problems**, same freedom and same condition.

### 4. `substitution`

**Able to:** Integrate composite expressions by substituting u for the inner function, including changing the limits of definite integrals.

**The idea that carries it:** Spot the inner function whose derivative is on scene, rename it u, swap completely, integrate, return — and definite integrals convert their limits along the way.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Leaving a stray x in the u-integral and integrating anyway.
- Keeping the old x-limits on the new u-integral.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal54-we1` — Evaluate $\int 2x(x^2 + 1)^3\,dx$ and verify by differentiating.
- `cal54-we2` — Evaluate $\int_0^1 2x(x^2 + 1)^3\,dx$ by converting the limits.

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
| area | **талбай** | ministry standard |
| function | **функц** | ministry standard |
| parallel | **параллель** | ministry standard |
| limit | **хязгаар** | already on the site |
| sample | **түүвэр** | already on the site |
| derivative | **уламжлал** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| problem | **бодлого** | ministry standard |
| subtracting | **хасах** | ministry standard |
| divide | **хуваах** | ministry standard |
| constant | **тогтмол** | ministry standard |
| subtract | **хасах** | ministry standard |
| positive | **эерэг** | ministry standard |
| pattern | **хэв маяг** | already on the site |

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
## antiderivatives

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal51-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal51-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-area-problem-and-the-definite-integral

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal52-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal52-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cal51-we1` and so on) exactly
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

- **Интеграл (12-р анги)** (primary)
- **Интеграл (12-р анги)** (primary)
- **Интеграл (12-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

