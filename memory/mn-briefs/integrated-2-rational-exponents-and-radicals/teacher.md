# MN authoring brief — Rational Exponents & Radicals

**Topic** `integrated-2/rational-exponents-and-radicals` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/rational-exponents-and-radicals`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `rational-exponents`

**Able to:** Explain why $x^{1/n}$ must equal $\sqrt[n]{x}$ if the exponent rules are to survive, convert between radical and rational-exponent form, and evaluate rational powers of numbers.

**The idea that carries it:** $x^{1/n} = \sqrt[n]{x}$ is forced, not chosen: it is the only value for which $(x^{a})^{b} = x^{ab}$ keeps working. Then $x^{m/n} = (\sqrt[n]{x})^{m}$ — take the root first.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading x^(1/2) as half of x.
- Flipping the root and the power: reading x^(2/3) as the square root of x cubed.
- Treating a negative exponent as making the answer negative.
- Evaluating an even root of a negative base.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u1-l1-we1` — Show that if the rule $(x^{a})^{b} = x^{ab}$ is to hold for fractional exponents, then $25^{1/2}$ must be $5$.
- `im2-u1-l1-we2` — Evaluate $8^{2/3}$, $16^{3/4}$ and $32^{2/5}$, taking the root first each time.
- `im2-u1-l1-we3` — Rewrite in radical form: $x^{3/5}$ and $y^{-1/2}$. Rewrite with rational exponents: $\sqrt[4]{t^{3}}$ and $\dfrac{1}{\sqrt{w}}$.
- `im2-u1-l1-we4` — Simplify $\dfrac{x^{3/4} \cdot x^{1/2}}{x^{1/4}}$, and evaluate it at $x = 16$.

**3 try-it problems**, same freedom and same condition.

### 2. `simplifying-radicals`

**Able to:** Simplify a radical by extracting perfect-power factors, using the product and quotient properties, and recognise when an expression is in simplest radical form.

**The idea that carries it:** $\sqrt{ab} = \sqrt{a}\sqrt{b}$ lets you split off the largest perfect square and extract it. Prime-factorise when the square is not obvious, and pull out one factor per pair.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting a radical across addition: writing √(9 + 16) as 3 + 4.
- Pulling out a single factor instead of a pair.
- Stopping before the radicand is fully reduced.
- Using pairs when simplifying a cube root.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u1-l2-we1` — Simplify $\sqrt{72}$ two ways: by spotting the largest perfect square, and by prime factorisation.
- `im2-u1-l2-we2` — Simplify $\sqrt{200}$, $\sqrt[3]{54}$ and $\sqrt{\dfrac{50}{9}}$.
- `im2-u1-l2-we3` — Simplify $\sqrt{48x^{5}y^{2}}$, assuming $x$ and $y$ are non-negative.
- `im2-u1-l2-we4` — Decide whether each is in simplest radical form, and simplify if not: $3\sqrt{20}$, $\sqrt{\dfrac{3}{4}}$, $2\sqrt{15}$.

**3 try-it problems**, same freedom and same condition.

### 3. `operations-with-radicals`

**Able to:** Add and subtract like radicals, multiply radical expressions including binomials, and rationalise a denominator using a conjugate.

**The idea that carries it:** Like radicals add like like terms — simplify first so more of them match. Multiply radicands directly. Clear a denominator by multiplying by the radical, or by the conjugate when there are two terms.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding unlike radicals: writing √2 + √3 as √5.
- Declaring terms uncombinable before simplifying them.
- Adding the radicands when multiplying: √6 · √10 = √16.
- Using the same sign for the conjugate.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u1-l3-we1` — Simplify $\sqrt{8} + \sqrt{18} - \sqrt{50}$.
- `im2-u1-l3-we2` — Multiply and simplify: $2\sqrt{6} \cdot 5\sqrt{10}$, and $\sqrt{3}\left(\sqrt{12} + \sqrt{27}\right)$.
- `im2-u1-l3-we3` — Expand $\left(\sqrt{5} + 3\right)\left(\sqrt{5} - 2\right)$.
- `im2-u1-l3-we4` — Rationalise the denominators: $\dfrac{6}{\sqrt{3}}$ and $\dfrac{4}{\sqrt{7} - 2}$.

**3 try-it problems**, same freedom and same condition.

### 4. `rational-and-irrational-numbers`

**Able to:** Classify numbers as rational or irrational, explain why the rationals are closed under the four operations, and prove that a rational plus an irrational is always irrational.

**The idea that carries it:** The rationals are closed under the four operations. That closure is what proves a rational plus an irrational must be irrational — if the sum were rational, subtracting would make the irrational rational.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling every square root irrational.
- Calling 22/7 irrational because it approximates π.
- Assuming two irrationals always combine to something irrational.
- Forgetting the non-zero condition in 'rational × irrational is irrational'.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u1-l4-we1` — Classify each as rational or irrational: $\sqrt{16}$, $\sqrt{20}$, $0.\overline{45}$, $\frac{22}{7}$, $\pi$.
- `im2-u1-l4-we2` — Prove that the sum of two rational numbers is rational.
- `im2-u1-l4-we3` — Prove that a rational number plus an irrational number is always irrational.
- `im2-u1-l4-we4` — Decide whether each is rational or irrational, with a reason: (a) $5 + \sqrt{7}$; (b) $\sqrt{2} \cdot \sqrt{8}$; (c) $3\sqrt{5}$; (d) $0 \cdot \pi$; (

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
| factor | **хуваагч** | ministry standard |
| mean | **дундаж** | ministry standard |
| product | **үржвэр** | ministry standard |
| number | **тоо** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| square | **квадрат** | ministry standard |
| rational | **рационал** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| radical | **язгуур** | ministry standard |
| quotient | **ногдвор** | ministry standard |
| form | **хэлбэр** | ministry standard |
| root | **язгуур** | ministry standard |
| subtracting | **хасах** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| pair | **хос** | ministry standard |

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
## rational-exponents

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u1-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u1-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## simplifying-radicals

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u1-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u1-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u1-l1-we1` and so on) exactly
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

