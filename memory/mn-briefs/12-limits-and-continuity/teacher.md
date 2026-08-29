# MN authoring brief — Limits & Continuity

**Topic** `12/limits-and-continuity` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `12/limits-and-continuity`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-idea-of-a-limit`

**Able to:** Read lim f(x) as 'the value f approaches as x approaches a', estimate limits from tables of nearby values, and understand that the limit ignores what happens AT the point.

**The idea that carries it:** lim f(x) as x → a is the value the outputs squeeze toward as x closes in on a from both sides — regardless of what f(a) is, or whether it exists at all.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing f(a) and calling it the limit.
- Checking only one side of the approach.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lc1-we1` — Estimate $\lim_{x \to 2} \tfrac{x^2}{2}$ from a table: compute $f(1.9), f(1.99), f(2.01), f(2.1)$.
- `lc1-we2` — $g(x) = x + 3$ except $g(1) = 50$ (one rebellious point). Find $\lim_{x \to 1} g(x)$.
- `lc1-we3` — True or false: if $f(3) = 7$, then $\lim_{x \to 3} f(x) = 7$.

**2 try-it problems**, same freedom and same condition.

### 2. `limit-laws-and-substitution`

**Able to:** Use the limit laws to evaluate limits by direct substitution, know when substitution is legal, and recognize the 0/0 signal that demands more work.

**The idea that carries it:** Limits respect arithmetic, so polynomials and safe rational functions surrender to substitution. The exception that matters: 0/0 — a signal to factor, not an answer.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating 0/0 as 0, or as 'undefined, so no limit'.
- Splitting a quotient limit when the denominator limit is 0.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lc2-we1` — Evaluate $\lim_{x \to 2}(x^2 + 3x)$.
- `lc2-we2` — Evaluate $\lim_{x \to 1} \dfrac{x^2 + 3}{x + 1}$.
- `lc2-we3` — Plug $x = 3$ into $\dfrac{x^2 - 9}{x - 3}$ and classify the result.

**2 try-it problems**, same freedom and same condition.

### 3. `holes-and-indeterminate-forms`

**Able to:** Resolve 0/0 limits by factoring and cancelling, connect them to holes in graphs, and evaluate the limit as the y-value of the hole.

**The idea that carries it:** 0/0 means a shared dying factor. Factor, cancel, substitute — the limit is the y-value of the hole the cancellation revealed.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Stopping at 0/0 and declaring 'no limit'.
- Forgetting the x ≠ 2 caveat when cancelling.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lc3-we1` — Evaluate $\lim_{x \to 2} \dfrac{x^2 - 4}{x - 2}$.
- `lc3-we2` — Evaluate $\lim_{x \to 3} \dfrac{x^2 - 5x + 6}{x - 3}$.
- `lc3-we3` — Evaluate $\lim_{h \to 0} \dfrac{(2 + h)^2 - 4}{h}$ — a preview of the derivative.

**2 try-it problems**, same freedom and same condition.

### 4. `one-sided-limits`

**Able to:** Evaluate left-hand and right-hand limits (notation x → a⁻, x → a⁺), decide whether a two-sided limit exists, and handle piecewise functions at their seams.

**The idea that carries it:** x → a⁻ reads the left approach, x → a⁺ the right. The two-sided limit exists iff both sides exist and agree — jumps are where they don't.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the wrong piece's rule for a one-sided limit.
- Saying the limit exists 'because f(1) is defined'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lc4-we1` — $f(x) = x + 1$ for $x < 1$; $f(x) = 4 - x$ for $x \geq 1$. Find both one-sided limits at $1$.
- `lc4-we2` — Evaluate $\lim_{x \to 0^-} \dfrac{|x|}{x}$ and $\lim_{x \to 0^+} \dfrac{|x|}{x}$.
- `lc4-we3` — $g(x) = x^2$ for $x < 2$; $g(x) = 4x - 4$ for $x \geq 2$. Does $\lim_{x \to 2} g(x)$ exist?

**2 try-it problems**, same freedom and same condition.

### 5. `limits-and-infinity`

**Able to:** Evaluate infinite limits (vertical asymptotes) and limits at infinity (horizontal asymptotes / end behavior), including the degree-comparison shortcut for rational functions.

**The idea that carries it:** c/0 blows up (vertical asymptote); 1/x dies at infinity, making rational end behavior a degree comparison: bottom wins → 0, tie → coefficient ratio, top wins → ±∞.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing c/0 with 0/0.
- Calling ∞ 'the limit exists'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lc5-we1` — Evaluate $\lim_{x \to 2} \dfrac{1}{(x-2)^2}$.
- `lc5-we2` — Evaluate $\lim_{x \to \infty} \dfrac{3x^2 + 1}{x^2 + 2}$.
- `lc5-we3` — Evaluate $\lim_{x \to \infty} \dfrac{2x + 5}{x^2 + 1}$ and $\lim_{x \to \infty} \dfrac{x^2 + 1}{2x + 5}$.

**2 try-it problems**, same freedom and same condition.

### 6. `continuity`

**Able to:** State the three-part definition of continuity at a point, classify discontinuities as removable/jump/infinite, and use the Intermediate Value Theorem to trap roots.

**The idea that carries it:** Continuous at a: value exists, limit exists, and they match. Failures come in three flavors — removable (hole), jump, infinite — and continuity buys you the IVT: no skipped values.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Declaring continuity because the limit exists.
- Using the IVT without continuity.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lc6-we1` — $f(x) = \tfrac{x^2 - 4}{x - 2}$ for $x \neq 2$, and $f(2) = 5$. Classify the discontinuity at $2$.
- `lc6-we2` — Is $g(x) = x^2$ ($x < 2$), $g(x) = 4x - 4$ ($x \geq 2$) continuous at $2$?
- `lc6-we3` — Show $f(x) = x^3 + x - 1$ has a root between $0$ and $1$.

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
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| limit | **хязгаар** | already on the site |
| rational | **рационал** | ministry standard |
| asymptote | **асимптот** | already on the site |
| table | **хүснэгт** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| vertical | **босоо** | ministry standard |
| hole | **нүх** | already on the site |
| graph | **график** | ministry standard |
| algebra | **алгебр** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## the-idea-of-a-limit

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED lc1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY lc1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## limit-laws-and-substitution

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED lc2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY lc2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`lc1-we1` and so on) exactly
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

