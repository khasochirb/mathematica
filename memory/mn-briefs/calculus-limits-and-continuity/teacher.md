# MN authoring brief — Limits & Continuity

**Topic** `calculus/limits-and-continuity` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `calculus/limits-and-continuity`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-idea-of-a-limit`

**Able to:** Read limits from graphs and tables, write limit notation, and separate what f approaches from what f equals.

**The idea that carries it:** The limit is the value the outputs squeeze toward as x approaches a from both sides — independent of f(a), and it exists only when left and right approaches agree.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Answering the limit question by plugging in: 'f(2) is undefined, so the limit doesn't exist.'
- Reporting a two-sided limit when only one side was checked.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal11-we1` — For $f(x) = \dfrac{x^2 - 4}{x - 2}$, evaluate $f(2.1)$ and $f(1.99)$ exactly, then state $\lim_{x \to 2} f(x)$.
- `cal11-we2` — The graph of $g$ follows $y = x + 2$ for $x < 1$ and $y = 5 - x$ for $x > 1$. Find both one-sided limits at $x = 1$ and decide whether $\lim_{x \to 1}

**2 try-it problems**, same freedom and same condition.

### 2. `computing-limits`

**Able to:** Evaluate limits by direct substitution, and resolve 0/0 forms by factoring or by multiplying by a conjugate.

**The idea that carries it:** Substitute first; a 0/0 answer means a hidden (x − a) factor — expose it by factoring or by conjugate, cancel, substitute again.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating 0/0 as an answer: 'the limit is 0' or 'the limit is undefined.'
- Cancelling (x − a) and worrying it was illegal division by zero.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal12-we1` — Evaluate $\lim_{x \to 4} (x^2 - 3x + 1)$ and $\lim_{x \to 1} \dfrac{x^2 + 2x}{x + 1}$.
- `cal12-we2` — Evaluate $\lim_{x \to 2} \dfrac{x^2 + x - 6}{x - 2}$.

**2 try-it problems**, same freedom and same condition.

### 3. `limits-at-infinity`

**Able to:** Evaluate limits as x → ±∞ by comparing leading terms, connect them to horizontal asymptotes, and recognize infinite limits at vertical asymptotes.

**The idea that carries it:** At infinity, leading terms rule: compare degrees for 0, coefficient ratio, or ±∞; a finite answer is a horizontal asymptote, and c/0 (c ≠ 0) marks a vertical one.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating c/0 like 0/0 and trying to factor.
- Averaging all the coefficients instead of racing the leading terms.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal13-we1` — Evaluate $\lim_{x \to \infty} \dfrac{3x^2 + 5x}{x^2 + 1}$, $\lim_{x \to \infty} \dfrac{2x + 7}{x^2 + 1}$, and $\lim_{x \to \infty} \dfrac{x^3 + 1}{x^2
- `cal13-we2` — Describe the behavior of $f(x) = \dfrac{1}{(x - 3)^2}$ near $x = 3$ and as $x \to \infty$.

**2 try-it problems**, same freedom and same condition.

### 4. `continuity`

**Able to:** Test continuity at a point with the three-part definition, classify discontinuities, and choose parameters that glue piecewise functions together.

**The idea that carries it:** Continuous at a: f(a) exists, the limit exists, and they match. Breaks classify as removable (hole), jump, or infinite — and piecewise seams glue by equating the pieces at the boundary.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling a function continuous because it's defined everywhere.
- Gluing a seam by setting the two pieces equal as formulas for all x.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal14-we1` — Where is $f(x) = \dfrac{x^2 - 1}{x - 1}$ discontinuous, and what kind of break is it? What single value would repair it?
- `cal14-we2` — Find $k$ so that $g(x) = \begin{cases} kx - 5 & x \le 3 \\ x^2 - 2x & x > 3 \end{cases}$ is continuous at $x = 3$.

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
| limit | **хязгаар** | already on the site |
| multiplying | **үржүүлэх** | ministry standard |
| asymptote | **асимптот** | already on the site |
| table | **хүснэгт** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| vertical | **босоо** | ministry standard |
| hole | **нүх** | already on the site |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |
| direct | **шууд** | already on the site |
| form | **хэлбэр** | ministry standard |

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

WORKED cal11-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal11-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## computing-limits

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal12-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal12-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cal11-we1` and so on) exactly
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

