# MN authoring brief — Linear Equations & Inequalities

**Topic** `integrated-1/linear-equations-and-inequalities` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/linear-equations-and-inequalities`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `solving-linear-equations`

**Able to:** Solve a multi-step linear equation, name the property that justifies each step, and verify the solution by substituting it back into the original equation.

**The idea that carries it:** Simplify each side, gather the variable terms on one side, then undo the operations in reverse order — doing the same thing to both sides every time. Check by substituting into the original.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doing something to one side only — subtracting 4 from the left and forgetting the right.
- Moving a term out of brackets: from 3(x + 2) = 15 writing 3x = 15 − 2.
- Dividing by the variable to 'cancel' it — from 4x = 2x + 6 dividing by x.
- Checking against a middle line instead of the original equation.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u2-l1-we1` — Solve $3x + 4 = 19$, naming the property used at each step.
- `im1-u2-l1-we2` — Solve $5(x - 2) + 3x = 30$.
- `im1-u2-l1-we3` — Solve $7x - 5 = 3x + 11$.
- `im1-u2-l1-we4` — Solve $2(3x - 1) = 4(x + 3) - 2$.

**3 try-it problems**, same freedom and same condition.

### 2. `fractions-and-special-cases`

**Able to:** Clear fractions from an equation by multiplying through by the LCD, and interpret an equation whose variable cancels as either no solution or all real numbers.

**The idea that carries it:** Multiply every term by the LCD to clear fractions. If the variable cancels, look at what is left: a true statement means every number works, a false statement means none do.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying only the fractional terms by the LCD: from x/4 + 3 = 7 writing x + 3 = 28.
- Losing the brackets when clearing a fraction with a multi-term numerator.
- Writing 'x = 0' or 'no answer' when the variable cancels and 6 = 6 remains.
- Writing 'x = 5' from a leftover statement like 5 = 8.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u2-l2-we1` — Solve $\dfrac{x}{3} + \dfrac{1}{2} = \dfrac{5}{6}$.
- `im1-u2-l2-we2` — Solve $\dfrac{2x - 1}{5} = \dfrac{x + 4}{3}$.
- `im1-u2-l2-we3` — Solve $4(x - 3) + 2 = 4x - 10$ and describe its solution set.
- `im1-u2-l2-we4` — Solve $6x + 1 = 2(3x + 5)$ and describe its solution set.

**3 try-it problems**, same freedom and same condition.

### 3. `linear-inequalities`

**Able to:** Solve a linear inequality, apply the flip rule correctly when multiplying or dividing by a negative, graph the solution set on a number line, and read the answer back into a real context.

**The idea that carries it:** Solve an inequality exactly like an equation, with one exception: multiplying or dividing both sides by a negative flips the symbol. Then graph the set, and clamp it to what the situation allows.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to flip when dividing by a negative: from −2x < 8 writing x < −4.
- Flipping when only ADDING or subtracting a negative number.
- Drawing a filled circle for a strict > or <.
- Reporting 'at most 8.33 tickets' as a final answer.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u2-l3-we1` — Solve $3x - 7 \le 8$ and graph the solution.
- `im1-u2-l3-we2` — Solve $-2x < 8$ and graph the solution.
- `im1-u2-l3-we3` — Solve $8 - 3x > 2$ two ways: once with a flip, once without.
- `im1-u2-l3-we4` — A delivery van weighs $1400$ kg empty and may not exceed $2600$ kg loaded. Each crate weighs $75$ kg. How many crates can it carry?

**3 try-it problems**, same freedom and same condition.

### 4. `compound-and-absolute-value`

**Able to:** Solve and graph compound inequalities joined by *and* and by *or*, and convert an absolute-value equation or inequality into the compound statement it stands for.

**The idea that carries it:** AND is an overlap (one interval), OR is two separate pieces. Absolute value means distance from zero: $|A| < b$ is an AND, $|A| > b$ is an OR, and $|A| = b$ splits into two equations.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Turning |x| > 3 into −3 < x < 3.
- Solving only the positive case of |x − 4| = 6 and reporting x = 10.
- Operating on only two of the three parts: from −4 < 2x < 6 writing −4 < x < 3.
- Distributing a coefficient into the bars: writing |2x − 1| as 2|x| − 1.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u2-l4-we1` — Solve $-1 < 2x + 3 < 9$ and graph the solution.
- `im1-u2-l4-we2` — Solve $|x - 4| = 6$.
- `im1-u2-l4-we3` — Solve $|2x - 1| \le 7$ and graph the solution.
- `im1-u2-l4-we4` — A machine cuts rods to $50$ cm with a tolerance of $0.4$ cm. Write this as an absolute-value inequality, and find the acceptable range of lengths.

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
| absolute value | **абсолют утга** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| fraction | **бутархай** | ministry standard |
| line | **шулуун** | ministry standard |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| zero | **тэг** | ministry standard |
| time | **цаг** | already on the site |
| identity | **адилтгал** | ministry standard |
| interval | **завсар** | ministry standard |
| graph | **график** | ministry standard |
| linear | **шугаман** | ministry standard |
| inequality | **тэнцэтгэл биш** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**absolute value** — proposed **абсолют утга**

> SENSE SPLIT, per Khas, 26 Aug 2026. These are not three renderings of one term — they are different things:
  • the VALUE  → «абсолют утга» or «үнэмлэхүй утга» (both correct)
  • the straight brackets | | → «модул» (the notation itself)
  • an absolute-value EQUATION → «модулт тэгшитгэл»
  • taking |x| of a number → «тооноос модул авах»
So the site's 'three ways' is not an inconsistency and needs no sweep. The earlier finding that ministry 12.1's «модул» should replace «абсолют утга» was WRONG: 12.1 is about modulus equations, which is the bracket sense.
  → this entry: the value. «үнэмлэхүй утга» is equally correct.

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
## solving-linear-equations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u2-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u2-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## fractions-and-special-cases

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u2-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u2-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u2-l1-we1` and so on) exactly
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

