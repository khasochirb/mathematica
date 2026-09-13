# MN authoring brief — The Derivative

**Topic** `calculus/the-derivative` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `calculus/the-derivative`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `rates-of-change-and-the-derivative`

**Able to:** Compute average rates of change, form the difference quotient, and evaluate the derivative at a point as a limit.

**The idea that carries it:** Average rate = secant slope over [a, a+h]; the derivative f′(a) is its limit as h → 0 — the tangent slope, and the instantaneous rate of change.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Setting h = 0 immediately in the difference quotient.
- Reporting the average rate as 'the' rate of change at a point.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal21-we1` — For $f(x) = x^2$: find the average rate of change from $x = 1$ to $x = 3$, then the derivative $f'(4)$ from the limit definition.
- `cal21-we2` — Compute $f'(2)$ from the definition for $f(x) = x^2 + x$.

**2 try-it problems**, same freedom and same condition.

### 2. `the-derivative-function`

**Able to:** Build f′(x) from the limit definition with x left general, read f and f′ against each other, and spot where a function fails to be differentiable.

**The idea that carries it:** Leave x general in the limit and you get the slope machine f′(x); its height reads f's slope everywhere, and corners, vertical tangents, and breaks are where it fails.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking continuous and differentiable are the same property.
- Confusing the height of f′ with the height of f.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal22-we1` — Use the definition to find $f'(x)$ for $f(x) = x^2 - 5x$, then evaluate $f'(1)$ and $f'(4)$.
- `cal22-we2` — Show from one-sided difference quotients that $f(x) = |x|$ is not differentiable at $0$.

**2 try-it problems**, same freedom and same condition.

### 3. `the-power-rule`

**Able to:** Differentiate powers, constants, sums, and constant multiples instantly — including negative and fractional exponents.

**The idea that carries it:** d/dx xⁿ = n xⁿ⁻¹ for any constant n; constants vanish, coefficients ride, sums split — and rewrite roots/reciprocals as powers before differentiating.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Differentiating 1/x³ to 1/(3x²) — running the power rule on the denominator in place.
- Killing the x along with the constant: d/dx (7x) = 0.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal23-we1` — Differentiate $f(x) = 4x^3 - 7x + 2$ and $g(x) = x^8 - 5x^4 + 6x^2$.
- `cal23-we2` — Differentiate $y = \dfrac{1}{x^3} + 6\sqrt{x}$.

**2 try-it problems**, same freedom and same condition.

### 4. `derivatives-of-sine-cosine-exp-and-ln`

**Able to:** Memorize and apply the derivatives of sin x, cos x, eˣ, and ln x, and differentiate combinations built from them with the sum and constant-multiple rules.

**The idea that carries it:** Four to memorize: (sin x)′ = cos x, (cos x)′ = −sin x, (eˣ)′ = eˣ, (ln x)′ = 1/x — then combine freely with the sum and constant-multiple rules.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Putting the minus on the wrong twin: (sin x)′ = −cos x.
- Applying the power rule to eˣ: (eˣ)′ = x·eˣ⁻¹.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal24-we1` — Differentiate $f(x) = 3\sin x - 2\cos x$ and evaluate $f'(0)$.
- `cal24-we2` — Differentiate $g(x) = 4e^x + x^2 - 3\ln x$ and evaluate $g'(1)$.

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
| secant | **огтлогч** | ministry standard |
| function | **функц** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| line | **шулуун** | ministry standard |
| rate | **хурдац** | already on the site |
| slope | **налалт** | ministry standard |
| limit | **хязгаар** | already on the site |
| exponent | **илтгэгч** | ministry standard |
| derivative | **уламжлал** | ministry standard |
| vertical | **босоо** | ministry standard |
| difference | **ялгавар** | ministry standard |
| point | **цэг** | ministry standard |
| quotient | **ногдвор** | ministry standard |
| corner | **булан** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

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
## rates-of-change-and-the-derivative

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal21-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal21-t1:
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

WORKED cal22-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal22-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cal21-we1` and so on) exactly
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

