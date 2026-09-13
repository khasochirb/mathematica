# MN authoring brief — Expressions & Operations

**Topic** `algebra-1/expressions-and-operations` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/expressions-and-operations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `variables-and-expressions`

**Able to:** Read algebraic expressions as recipes, evaluate them by substituting values (including negatives), and identify terms and coefficients.

**The idea that carries it:** An expression is a recipe for a number; evaluate it by substituting in parentheses, and read its structure through terms and coefficients.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Evaluating $-x^2$ at $x = -3$ as $9$.
- Dropping the sign of a coefficient: reading the coefficient of $-5x$ in $3x^2 - 5x + 7$ as $5$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al11-we1` — Evaluate $3x^2 - 2x + 1$ at $x = 4$.
- `al11-we2` — Evaluate $-a^2 + 5a$ at $a = -2$.

**2 try-it problems**, same freedom and same condition.

### 2. `like-terms-and-the-distributive-property`

**Able to:** Combine like terms, expand with the distributive property (including a leading minus), and simplify multi-step expressions.

**The idea that carries it:** Distribute to every term (a leading minus flips every sign), then combine terms with identical variable parts by adding coefficients.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Distributing to the first term only: $4(2x - 3) = 8x - 3$.
- Combining unlike terms: $3x + 5x^2 = 8x^3$ or $8x^2$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al12-we1` — Simplify $5x + 2(3x - 4) - 7$.
- `al12-we2` — Simplify $7a - (2a - 9) + 3$.

**2 try-it problems**, same freedom and same condition.

### 3. `exponents-and-order-of-operations`

**Able to:** Evaluate powers, apply the product/quotient/power rules for exponents with numeric bases, and evaluate multi-step expressions in the correct order.

**The idea that carries it:** Exponents count copies of the base (laws: add, subtract, multiply exponents), and every expression is evaluated in the fixed order P–E–MD–AS, left to right within a rank.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- $3 + 4 \times 2 = 14$.
- $2^3 \cdot 2^4 = 4^7$ — multiplying the bases too.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al13-we1` — Evaluate $5 + 3(8 - 6)^2$.
- `al13-we2` — Simplify $\dfrac{2^5 \cdot 2^3}{2^6}$ as a single power, then evaluate.

**2 try-it problems**, same freedom and same condition.

### 4. `from-words-to-algebra`

**Able to:** Translate verbal phrases into expressions, define a variable precisely, and build expressions for real quantities (costs, ages, perimeters).

**The idea that carries it:** Define the variable with units, translate phrase by phrase — and watch reversing phrases like 'less than', which flip the order.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Translating '5 less than $x$' as $5 - x$.
- Leaving the variable undefined ('let $x$ = Nara').

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al14-we1` — A taxi charges a \$4 flat fee plus \$2 per km. Write the cost of a $k$-km ride, and evaluate it for a 7-km ride.
- `al14-we2` — The width of a rectangle is $w$; the length is 3 more than twice the width. Write the perimeter in terms of $w$ and simplify.

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
| base | **суурь** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| product | **үржвэр** | ministry standard |
| rate | **хурдац** | already on the site |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| perimeter | **периметр** | already on the site |
| algebra | **алгебр** | ministry standard |
| quotient | **ногдвор** | ministry standard |
| part | **хэсэг** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| subtract | **хасах** | ministry standard |
| sign | **тэмдэг** | ministry standard |
| power | **зэрэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

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
## variables-and-expressions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al11-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al11-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## like-terms-and-the-distributive-property

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al12-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al12-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al11-we1` and so on) exactly
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

