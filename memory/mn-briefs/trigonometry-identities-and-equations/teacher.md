# MN authoring brief — Identities & Equations

**Topic** `trigonometry/identities-and-equations` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `trigonometry/identities-and-equations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-pythagorean-identity`

**Able to:** Use sin²θ + cos²θ = 1 (and its rearrangements) to find remaining trig values from one given value and a quadrant.

**The idea that carries it:** sin²θ + cos²θ = 1 is the circle's equation for every angle: one value plus a quadrant determines everything else — the root gives magnitude, ASTC gives sign.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Taking the positive square root automatically.
- Writing sin²θ as sin(θ²).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig51-we1` — Given $\sin\theta = \frac{5}{13}$ with $\theta$ in QII, find $\cos\theta$ and $\tan\theta$ exactly.
- `trig51-we2` — Given $\tan\theta = 2$ with $\theta$ in QIII, find $\sin\theta$ and $\cos\theta$ exactly.

**2 try-it problems**, same freedom and same condition.

### 2. `sum-and-difference-formulas`

**Able to:** Apply the sine and cosine sum/difference formulas to compute new exact values and simplify expressions.

**The idea that carries it:** sin(A±B) mixes and keeps the sign; cos(A±B) matches and flips it — manufacture 15° and 75° exactly, and collapse expanded shapes back to single angles.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Distributing: sin(A + B) = sin A + sin B.
- Keeping the sign in the cosine formula: cos(A + B) = cos A cos B + sin A sin B.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig52-we1` — Compute $\sin 75°$ exactly using $75° = 45° + 30°$.
- `trig52-we2` — Compute $\cos 15°$ exactly using $15° = 45° - 30°$, and compare with $\sin 75°$.

**2 try-it problems**, same freedom and same condition.

### 3. `double-angle-formulas`

**Able to:** Derive and apply sin 2θ = 2 sin θ cos θ and the three faces of cos 2θ.

**The idea that carries it:** B = A in the sum formulas: sin 2θ = 2 sin θ cos θ; cos 2θ has three interchangeable faces — choose the one matching what you know.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doubling the value: sin 2θ = 2 sin θ.
- Forgetting the sign of cos θ before computing sin 2θ.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig53-we1` — Verify $\sin 2\theta = 2\sin\theta\cos\theta$ at $\theta = 30°$, then use the formulas to compute $\sin 120°$ and $\cos 120°$ from $60°$'s values.
- `trig53-we2` — Given $\sin\theta = \frac{3}{5}$ with $\theta$ in QII, find $\sin 2\theta$ and $\cos 2\theta$ exactly.

**2 try-it problems**, same freedom and same condition.

### 4. `solving-trig-equations`

**Able to:** Solve trig equations on [0, 2π) — basic, multi-solution, and factorable quadratic types — and describe the general solution.

**The idea that carries it:** Reference angle in the two ASTC quadrants solves sin/cos = k (twice per lap); harder equations factor down to base cases — and dividing by a trig factor loses solutions.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Stopping at the calculator's single answer for sin θ = k.
- Dividing both sides by sin θ (or cos θ).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig54-we1` — Solve $2\cos\theta + 1 = 0$ on $[0, 2\pi)$.
- `trig54-we2` — Solve $2\sin^2\theta - \sin\theta - 1 = 0$ on $[0, 2\pi)$.

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
| shape | **дүрс** | ministry standard |
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| base | **суурь** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| circle | **тойрог** | ministry standard |
| identity | **адилтгал** | ministry standard |
| formula | **томьёо** | ministry standard |
| algebra | **алгебр** | ministry standard |
| difference | **ялгавар** | ministry standard |
| quadratic | **квадрат** | ministry standard |
| root | **язгуур** | ministry standard |
| divide | **хуваах** | ministry standard |
| face | **нүүр** | already on the site |
| chain | **давхар функцийн уламжлалын дүрэм** | **proposed — tell us if it is wrong** |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

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
## the-pythagorean-identity

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig51-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig51-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## sum-and-difference-formulas

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig52-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig52-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`trig51-we1` and so on) exactly
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

