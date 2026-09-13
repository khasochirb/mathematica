# MN authoring brief — Derivatives

**Topic** `12/derivatives` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `12/derivatives`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-derivative-as-a-limit`

**Able to:** Define the derivative f'(a) as the limit of the difference quotient, compute it for simple functions, and read it as the slope of the tangent line.

**The idea that carries it:** f'(a) = lim of (f(a+h) − f(a))/h as h → 0: the secant slope's limit, the tangent's slope, the curve's instantaneous rate — all one number.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Plugging h = 0 straight into the difference quotient.
- Treating the derivative as 'the y-value at the point'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dv1-we1` — From the definition, compute $f'(3)$ for $f(x) = x^2$.
- `dv1-we2` — From the definition, compute $f'(2)$ for $f(x) = x^2 - 3x$.
- `dv1-we3` — $f(x) = 5x + 2$ (a line). Compute $f'(a)$ at any $a$ and interpret.

**2 try-it problems**, same freedom and same condition.

### 2. `the-derivative-function`

**Able to:** Compute f'(x) as a function from the definition, use the dy/dx notation, and read the sign of f' as rising/falling behavior of f.

**The idea that carries it:** Run the difference quotient with x as a letter: f'(x) is a function reporting the slope at every point. Its sign narrates f: positive = rising, negative = falling, zero = flat.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing f'(x) = 2x with 'the slope is 2x' as a single number.
- Reading dy/dx as a fraction to cancel.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dv2-we1` — From the definition, find $f'(x)$ for $f(x) = x^2$.
- `dv2-we2` — From the definition, find $f'(x)$ for $f(x) = x^3$.
- `dv2-we3` — $f(x) = x^2 - 4x$. Where is $f'(x) = 0$, and what does the sign of $f'$ say either side?

**2 try-it problems**, same freedom and same condition.

### 3. `the-power-rule`

**Able to:** Differentiate powers with d/dx xⁿ = nxⁿ⁻¹, plus the constant, constant-multiple, and sum rules — every polynomial on sight.

**The idea that carries it:** xⁿ → nxⁿ⁻¹; constants vanish, coefficients ride, sums split term by term. Every polynomial differentiates on sight.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Leaving the exponent unchanged: d/dx x³ = 3x³.
- Differentiating the constant term into itself.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dv3-we1` — Differentiate $y = x^5$.
- `dv3-we2` — Differentiate $f(x) = 2x^3 - 5x^2 + 4x - 9$.
- `dv3-we3` — Differentiate $g(x) = \sqrt{x} + \dfrac{1}{x}$ (rewrite as powers first).

**2 try-it problems**, same freedom and same condition.

### 4. `product-and-quotient-rules`

**Able to:** Differentiate products with (fg)' = f'g + fg' and quotients with the low-d-high minus high-d-low formula.

**The idea that carries it:** (fg)' = f'g + fg' — each factor takes a turn. (f/g)' = (f'g − fg')/g²: low d-high minus high d-low, over low squared; order matters.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting products: (fg)' = f'g'.
- Flipping the quotient rule's numerator.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dv4-we1` — Differentiate $y = (x^2 + 1)(x^3 - 2)$ with the product rule.
- `dv4-we2` — Differentiate $y = \dfrac{x^2}{x + 1}$.
- `dv4-we3` — Show the trap concretely: for $f = x^2, g = x^3$, compare $(fg)'$ with $f'g'$.

**2 try-it problems**, same freedom and same condition.

### 5. `the-chain-rule`

**Able to:** Differentiate compositions with the chain rule: outer derivative at the inner function, times the inner derivative.

**The idea that carries it:** d/dx f(g(x)) = f'(g(x)) · g'(x): differentiate the outside (keeping the inside), then multiply by the inside's derivative. Rates multiply through a chain.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the inner derivative.
- Differentiating the inside INSIDE the outer function.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dv5-we1` — Differentiate $y = (3x + 1)^2$, then verify by expanding.
- `dv5-we2` — Differentiate $y = (x^2 + 1)^3$.
- `dv5-we3` — Differentiate $y = \sqrt{5x^2 + 4}$.

**2 try-it problems**, same freedom and same condition.

### 6. `sine-cosine-and-motion`

**Able to:** Differentiate sin and cos (with the chain rule), and read position → velocity → acceleration as repeated differentiation.

**The idea that carries it:** (sin x)' = cos x, (cos x)' = −sin x — the wave-scroll fact, formalized. Position, velocity, acceleration: each is the previous one's derivative.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing (cos x)' = sin x — dropping the minus.
- Forgetting the chain toll on sin(3x).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dv6-we1` — Differentiate $y = 3\sin x - 2\cos x$ and evaluate the slope at $x = 0$.
- `dv6-we2` — Differentiate $y = \sin(4x)$ and $y = \cos(x^2)$.
- `dv6-we3` — A stone dropped off a cliff falls $s(t) = 5t^2$ meters in $t$ seconds. Find its velocity and acceleration at $t = 3$.

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
| tangent | **шүргэгч** | ministry standard |
| factor | **хуваагч** | ministry standard |
| secant | **огтлогч** | ministry standard |
| function | **функц** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| geometry | **геометр** | ministry standard |
| rate | **хурдац** | already on the site |
| slope | **налалт** | ministry standard |
| limit | **хязгаар** | already on the site |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| time | **цаг** | already on the site |
| derivative | **уламжлал** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**secant** — proposed **огтлогч**

> Circle sense only. The trig function sec is «секанс» (MoE 12.6 «Секанс, косеканс, котангенс») — one English word, two Mongolian terms; tag the sense on each use.

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
## the-derivative-as-a-limit

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dv1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dv1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-derivative-function

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dv2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dv2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`dv1-we1` and so on) exactly
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

- **Уламжлал (12-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

