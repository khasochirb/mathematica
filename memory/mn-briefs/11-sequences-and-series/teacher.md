# MN authoring brief — Sequences & Series

**Topic** `11/sequences-and-series` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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

1. **Arithmetic adds, geometric multiplies.** Every formula in the topic follows from which of the two it is. A student who identifies the type correctly has done most of the work; one who does not applies the wrong formula perfectly.

2. **A sequence is the list, a series is the sum.** They are constantly confused because they are constantly next to each other. Keep the distinction explicit in the wording every time.

3. **An infinite geometric series only converges when |r| < 1.** This is the topic's one genuinely surprising result and it deserves the time: adding infinitely many positive numbers can give a finite answer, but only when the terms shrink fast enough.

**The error to design against:** Off-by-one in the nth-term formula — using a + nd instead of a + (n−1)d. The first term needs zero steps, not one, and saying that once fixes it.

If your Mongolian version lands those and a student can do the practice
set, the topic is right — however you got there.

Each lesson, and what the student must end up able to do:

### 1. `meet-sequences`

**Able to:** Use subscript notation $a_n$, generate terms from recursive and explicit rules, and tell the two rule types apart.

**The idea that carries it:** aₙ = the term at position n. Recursive rules step from the previous term; explicit rules teleport to any position.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $a_4$ as '$a$ times 4'.
- Using a recursive rule like an explicit one: '$a_{100} = a_{99} + 5$, done!'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sq1-we1` — For the sequence $20, 25, 30, 35, \ldots$: find $a_2$ and $a_6$.
- `sq1-we2` — Generate the first 4 terms of $a_1 = 3$, $a_n = 2a_{n-1} + 1$.
- `sq1-we3` — For the explicit rule $a_n = n^2 + 1$: find $a_3$ and $a_{10}$.

**2 try-it problems**, same freedom and same condition.

### 2. `arithmetic-sequences`

**Able to:** Recognize arithmetic sequences by their common difference and use $a_n = a_1 + (n-1)d$ to find terms, differences, and positions.

**The idea that carries it:** Same difference every step: aₙ = a₁ + (n−1)d — n−1 steps from the start. Fence posts and gaps.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using $n$ steps instead of $n-1$: $a_{10} = a_1 + 10d$.
- Testing 'arithmetic' with just one difference.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sq2-we1` — For $7, 11, 15, 19, \ldots$: find $d$ and $a_{10}$.
- `sq2-we2` — An arithmetic sequence has $a_1 = 100$ and $d = -6$. Find $a_{12}$.
- `sq2-we3` — Given $a_1 = 5$ and $a_{20} = 81$: find $d$.

**2 try-it problems**, same freedom and same condition.

### 3. `geometric-sequences`

**Able to:** Recognize geometric sequences by their common ratio and use $a_n = a_1 \cdot r^{n-1}$ in both directions.

**The idea that carries it:** Same ratio every step: aₙ = a₁·r^(n−1). Growth, decay, or sign-flipping — by where r sits.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Testing with differences instead of ratios.
- Computing $a_n = (a_1 r)^{n-1}$ — gluing the start onto the ratio.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sq3-we1` — For $2, 6, 18, 54, \ldots$: find $r$ and $a_7$.
- `sq3-we2` — For $80, 40, 20, \ldots$: find $r$ and $a_6$.
- `sq3-we3` — Given $a_1 = 5$ and $a_4 = 135$: find $r$.

**2 try-it problems**, same freedom and same condition.

### 4. `arithmetic-series`

**Able to:** Sum arithmetic series with $S_n = \frac{n(a_1+a_n)}{2}$, finding the last term first when necessary.

**The idea that carries it:** Sₙ = n(a₁ + aₙ)/2 — count times the average of first and last. Compute the last term first if needed.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the first and SECOND terms instead of first and last.
- Summing '20 terms' but stopping the last-term chain at $a_{19}$.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sq4-we1` — Compute $1 + 2 + \cdots + 100$ Gauss's way.
- `sq4-we2` — Sum the first 20 terms of $3, 7, 11, \ldots$.
- `sq4-we3` — A theater's rows hold $14, 17, 20, \ldots$ seats for 10 rows. Total seats?

**2 try-it problems**, same freedom and same condition.

### 5. `geometric-series`

**Able to:** Sum geometric series with $S_n = \frac{a_1(r^n - 1)}{r - 1}$, and understand the multiply-and-subtract derivation.

**The idea that carries it:** Multiply by r, subtract, and the middle cancels: Sₙ = a₁(rⁿ−1)/(r−1). The last term dominates.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the arithmetic pairing on a geometric list.
- Computing $r^n$ with $n-1$ (the term formula's habit).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sq5-we1` — Sum $2 + 6 + 18 + 54 + 162$ by formula, then verify directly.
- `sq5-we2` — Sum the first 10 terms of $1, 2, 4, 8, \ldots$.
- `sq5-we3` — Sum the first 6 terms of $100, 50, 25, \ldots$ (exactly).

**2 try-it problems**, same freedom and same condition.

### 6. `infinite-geometric-series`

**Able to:** Sum infinite geometric series with $S = \frac{a_1}{1-r}$ when $|r| < 1$, and recognize when no finite sum exists.

**The idea that carries it:** |r| < 1: the tail dies and S = a₁/(1−r). |r| ≥ 1: no finite sum. Repeating decimals are these series in disguise.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Summing a divergent series: $S = \tfrac{1}{1-2} = -1$ for $1+2+4+\cdots$.
- Thinking $0.999\ldots$ is 'just under' 1.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sq6-we1` — Sum $\tfrac12 + \tfrac14 + \tfrac18 + \cdots$
- `sq6-we2` — Sum $9 + 3 + 1 + \tfrac13 + \cdots$
- `sq6-we3` — Show $0.999\ldots = 1$ as a geometric series.

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
| ratio | **харьцаа** | ministry standard |
| sequence | **дараалал** | ministry standard |
| time | **цаг** | already on the site |
| growth | **өсөлт** | already on the site |
| formula | **томьёо** | ministry standard |
| difference | **ялгавар** | ministry standard |
| finite | **төгсгөлөг** | ministry standard |
| infinite | **төгсгөлгүй** | ministry standard |
| position | **байрлал** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| subtract | **хасах** | ministry standard |
| average | **дундаж** | ministry standard |
| chain | **давхар функцийн уламжлалын дүрэм** | **proposed — tell us if it is wrong** |
| direction | **чиглэл** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## meet-sequences

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sq1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sq1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## arithmetic-sequences

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sq2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sq2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sq1-we1` and so on) exactly
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

