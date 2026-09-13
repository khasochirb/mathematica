# MN authoring brief — Rational Functions

**Topic** `algebra-2/rational-functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/rational-functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `direct-and-inverse-variation`

**Able to:** Model direct (y = kx) and inverse (y = k/x) variation, find k from one data point, and predict new values.

**The idea that carries it:** Direct: y/x constant (line through origin). Inverse: xy constant (hyperbola). One point determines k; k determines everything.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Modeling 'y varies inversely with x' as $y = k - x$.
- Direct variation with an intercept: 'pay varies directly with hours' as $y = kx + b$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a271-we1` — $y$ varies inversely with $x$, and $y = 12$ when $x = 5$. Find $y$ when $x = 20$.
- `a271-we2` — Six painters finish a job in 10 days. Assuming inverse variation, how long for 4 painters?

**2 try-it problems**, same freedom and same condition.

### 2. `graphs-asymptotes-and-holes`

**Able to:** Find domains, vertical asymptotes, holes, and horizontal asymptotes of rational functions, and sketch their graphs.

**The idea that carries it:** Factor first: cancelled factors are holes, surviving denominator zeros are vertical asymptotes, and the degree comparison sets the horizontal asymptote.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling every denominator zero a vertical asymptote.
- Treating the horizontal asymptote as untouchable.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a272-we1` — Analyze $f(x) = \dfrac{x^2 - 4}{x^2 - x - 6}$: domain, holes, vertical and horizontal asymptotes.
- `a272-we2` — Find all asymptotes of $g(x) = \dfrac{3x^2 + 1}{x^2 + 4}$ and $h(x) = \dfrac{5}{x - 2}$.

**2 try-it problems**, same freedom and same condition.

### 3. `operations-on-rational-expressions`

**Able to:** Multiply, divide, add, and subtract rational expressions, factoring first and stating excluded values.

**The idea that carries it:** Factor everything first; cancel only whole factors; divide = flip and multiply; add via the factored LCD — and the original's excluded values survive simplification.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Slashing matching TERMS: $\frac{x^2 - 9}{x^2 + 5x} \to \frac{-9}{5x}$ by cancelling the $x^2$'s.
- Distributing a subtraction into only the first term of the second numerator: $\frac{5}{x} - \frac{x - 2}{3x}$ becoming $\frac{15 - x - 2}{3x}$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a273-we1` — Simplify $\dfrac{x^2 - 9}{x^2 + 5x} \div \dfrac{x - 3}{x + 5}$.
- `a273-we2` — Combine $\dfrac{3}{x^2 - 4} + \dfrac{2}{x + 2}$.

**2 try-it problems**, same freedom and same condition.

### 4. `rational-equations`

**Able to:** Solve rational equations by multiplying through by the LCD, reject solutions that zero a denominator, and model combined work and mixture problems.

**The idea that carries it:** Multiply every term by the LCD to reach polynomial land; audit candidates against the original denominators; and remember work adds by RATES: 1/a + 1/b = 1/t.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying only the fraction terms by the LCD, skipping lone constants.
- Averaging times in work problems: hoses of 3 h and 6 h 'together take 4.5 h.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a274-we1` — Solve $\dfrac{3}{x - 2} + \dfrac{1}{x} = \dfrac{4}{x(x - 2)}$.
- `a274-we2` — Pipe A fills a tank in 4 hours; with pipe B helping, it takes 2.4 hours. How long would B alone take?

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
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| fraction | **бутархай** | ministry standard |
| division | **хуваалт** | ministry standard |
| line | **шулуун** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| rate | **хурдац** | already on the site |
| domain | **тодорхойлогдох муж** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| zero | **тэг** | ministry standard |
| rational | **рационал** | ministry standard |
| asymptote | **асимптот** | already on the site |
| vertical | **босоо** | ministry standard |

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
## direct-and-inverse-variation

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a271-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a271-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## graphs-asymptotes-and-holes

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a272-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a272-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a271-we1` and so on) exactly
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

