# MN authoring brief — Sequences & Series

**Topic** `algebra-2/sequences-and-series` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/sequences-and-series`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `arithmetic-sequences-and-series`

**Able to:** Write explicit formulas for arithmetic sequences, find terms and term counts, and sum series with the Gauss formula.

**The idea that carries it:** aₙ = a₁ + (n−1)d — a discrete line with slope d — and Sₙ = n/2 · (first + last): pair the ends and every pair matches.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing $a_n = a_1 + nd$ — one hop too many.
- Summing with the formula but the wrong count: 'terms 5 through 20' as $n = 20$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a281-we1` — For the sequence $7, 12, 17, 22, \ldots$: find $a_{20}$, and determine which term equals 92.
- `a281-we2` — A theater has 20 seats in row 1, each row 3 more than the last, 15 rows total. How many seats altogether?

**2 try-it problems**, same freedom and same condition.

### 2. `geometric-sequences-and-series`

**Able to:** Write explicit formulas for geometric sequences, and sum finite geometric series with the ratio formula.

**The idea that carries it:** aₙ = a₁·rⁿ⁻¹ — the exponential in list form — and Sₙ = a₁(1 − rⁿ)/(1 − r), born from the telescoping of S − rS.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using $n$ multiplications: $a_{10} = 5 \cdot 2^{10}$.
- Declaring $1, 4, 9, 16, \ldots$ geometric ('it grows fast').

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a282-we1` — For $5, 10, 20, 40, \ldots$: find $a_{10}$ and the first term exceeding 5000.
- `a282-we2` — Compute $2 + 6 + 18 + 54 + 162 + 486$.

**2 try-it problems**, same freedom and same condition.

### 3. `infinite-geometric-series`

**Able to:** Determine when an infinite geometric series converges, compute S = a₁/(1 − r), and convert repeating decimals to fractions.

**The idea that carries it:** When |r| < 1 the tail rⁿ dies and S = a₁/(1 − r); when |r| ≥ 1 the series diverges — and repeating decimals are this formula in disguise.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying $S = \frac{a_1}{1-r}$ to $2 + 3 + 4.5 + \cdots$ ($r = 1.5$) and reporting $S = -4$.
- Treating 'infinitely many terms' as automatically infinite in total.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a283-we1` — Evaluate $12 + 6 + 3 + \frac{3}{2} + \cdots$ or explain why it diverges.
- `a283-we2` — Write $0.\overline{45} = 0.454545\ldots$ as a fraction.

**2 try-it problems**, same freedom and same condition.

### 4. `sigma-notation-and-recursion`

**Able to:** Read and write sigma notation, expand and evaluate sums, and convert between recursive and explicit definitions.

**The idea that carries it:** Σ compresses 'run k, apply, add'; recursion defines by start + step-law; and the two great families translate freely between recursive and explicit forms.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Counting $\sum_{k=5}^{20}$ as 15 terms.
- Reading $a_{n+1} = 3a_n$ as 'the sequence is $3, 6, 9, \ldots$'.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a284-we1` — Evaluate $\sum_{k=1}^{20} (3k + 1)$ and $\sum_{k=1}^{6} 2 \cdot 3^{k-1}$.
- `a284-we2` — A sequence is defined by $a_1 = 5$, $a_{n+1} = a_n + 3$. Write the explicit formula and find $a_{100}$; then express $7, 14, 28, 56, \ldots$ recursive

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
| count | **тоолох** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| fraction | **бутархай** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| line | **шулуун** | ministry standard |
| slope | **налалт** | ministry standard |
| sequence | **дараалал** | ministry standard |
| number | **тоо** | ministry standard |
| formula | **томьёо** | ministry standard |
| algebra | **алгебр** | ministry standard |
| form | **хэлбэр** | ministry standard |
| finite | **төгсгөлөг** | ministry standard |
| infinite | **төгсгөлгүй** | ministry standard |
| pair | **хос** | ministry standard |
| test | **шалгалт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## arithmetic-sequences-and-series

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a281-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a281-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## geometric-sequences-and-series

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a282-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a282-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a281-we1` and so on) exactly
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

- **Дараалал ба цуваа (11-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

