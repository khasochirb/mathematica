# MN authoring brief — Radicals & Rational Exponents

**Topic** `algebra-2/radicals-and-rational-exponents` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/radicals-and-rational-exponents`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `rational-exponents`

**Able to:** Convert between radical and exponent notation, evaluate rational powers, and simplify using the exponent laws.

**The idea that carries it:** a^(m/n) = (n-th root of a)^m — denominator roots, numerator powers, root first for small numbers — and every exponent law applies unchanged.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $a^{m/n}$ upside down: $8^{2/3}$ as the square root of $8^3$... wait, as $(\sqrt{8})^3$.
- Treating the negative in $16^{-3/4}$ as making the answer negative.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a251-we1` — Evaluate $8^{2/3}$, $16^{-3/4}$, and $25^{3/2}$.
- `a251-we2` — Simplify $x^{1/2} \cdot x^{1/3}$ and $\left(x^{2/3}\right)^{3/4} \cdot x^{-1/6}$ (for $x > 0$).

**2 try-it problems**, same freedom and same condition.

### 2. `simplifying-radicals-and-operations`

**Able to:** Simplify radicals by extracting perfect powers, add/subtract/multiply radical expressions, and rationalize denominators.

**The idea that carries it:** Extract the largest perfect power, combine only like radicals (simplify first to expose them), and rationalize denominators — with conjugates when a binomial blocks the way.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding under the root: $\sqrt{9} + \sqrt{16} = \sqrt{25} = 5$.
- Stopping extraction early: $\sqrt{72} = \sqrt{4 \cdot 18} = 2\sqrt{18}$, done.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a252-we1` — Simplify $\sqrt{50} + \sqrt{18} - \sqrt{8}$.
- `a252-we2` — Rationalize $\dfrac{6}{\sqrt{12}}$ and $\dfrac{4}{\sqrt{7} - \sqrt{3}}$.

**2 try-it problems**, same freedom and same condition.

### 3. `radical-equations`

**Able to:** Solve radical equations by isolating and raising to powers, and detect extraneous solutions by checking the original.

**The idea that carries it:** Isolate, raise to the power, solve — then CHECK every candidate in the original: squaring forgets signs, so phantoms are routine, not rare.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Squaring term-by-term: from $\sqrt{x} + 2 = 5$ writing $x + 4 = 25$.
- Skipping the check because the algebra was careful.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a253-we1` — Solve $\sqrt{x + 7} = x - 5$.
- `a253-we2` — Solve $\sqrt[3]{4x - 7} = 3$ and explain why no check drama arises.

**2 try-it problems**, same freedom and same condition.

### 4. `inverse-functions`

**Able to:** Find inverse functions algebraically, verify by composition, restrict domains where needed, and read the y = x reflection.

**The idea that carries it:** Inverse = the machine run backwards: swap x and y and re-solve, verify with f(f⁻¹(x)) = x, and restrict to one-to-one pieces when outputs repeat.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f^{-1}(x)$ as $\frac{1}{f(x)}$.
- Verifying with one composition only.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a254-we1` — Find the inverse of $f(x) = \dfrac{3x - 1}{2}$ and verify by composition.
- `a254-we2` — For $f(x) = x^2 - 4$ with domain $x \ge 0$, find $f^{-1}$ and state its domain.

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
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| product | **үржвэр** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| number | **тоо** | ministry standard |
| rational | **рационал** | ministry standard |
| unit | **нэгж** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| radical | **язгуур** | ministry standard |
| root | **язгуур** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| subtract | **хасах** | ministry standard |
| numerator | **хүртвэр** | ministry standard |
| inverse | **урвуу** | ministry standard |

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
## rational-exponents

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a251-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a251-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## simplifying-radicals-and-operations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a252-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a252-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a251-we1` and so on) exactly
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

- **Язгуур ба рационал илтгэгч (10-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

