# MN authoring brief — Solving Quadratic Equations

**Topic** `integrated-2/solving-quadratic-equations` · **5 lessons** · 19 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/solving-quadratic-equations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `solving-by-factoring-and-roots`

**Able to:** Solve a quadratic equation by factoring using the zero-product property, and solve equations of the form $a(x - h)^{2} = c$ by taking square roots.

**The idea that carries it:** Get zero on one side, factor, then set each factor to zero — because a product is zero exactly when one of its factors is.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Factoring before moving everything to one side.
- Dividing both sides by $x$ to solve $3x^{2} = 12x$.
- Writing only the positive root when taking a square root.
- Reporting a double root as two different solutions.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u4-l1-we1` — Solve $x^{2} + 5x = 24$.
- `im2-u4-l1-we2` — Solve $3x^{2} - 12x = 0$ and $2x^{2} = 50$.
- `im2-u4-l1-we3` — Solve $2(x - 3)^{2} - 32 = 0$.
- `im2-u4-l1-we4` — Solve $x^{2} - 10x + 25 = 0$ and $6x^{2} + x - 15 = 0$.

**2 try-it problems**, same freedom and same condition.

### 2. `completing-the-square`

**Able to:** Complete the square to rewrite a quadratic in vertex form, solve any quadratic equation this way, and see why the method works geometrically.

**The idea that carries it:** To complete $x^{2} + bx$, add $\left(\frac{b}{2}\right)^{2}$ — halve the middle coefficient, then square it — and balance the equation by adding the same amount to the other side.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Squaring the middle coefficient before halving it.
- Adding the completing constant to only one side.
- Completing the square without dividing out the leading coefficient.
- Forgetting that a constant added INSIDE a bracket is multiplied.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u4-l2-we1` — Solve $x^{2} + 6x - 7 = 0$ by completing the square.
- `im2-u4-l2-we2` — Solve $x^{2} - 8x + 3 = 0$ by completing the square, leaving the answers in exact form.
- `im2-u4-l2-we3` — Solve $2x^{2} + 12x - 14 = 0$ by completing the square.
- `im2-u4-l2-we4` — Rewrite $f(x) = 3x^{2} - 12x + 5$ in vertex form by completing the square, and state the minimum value.

**2 try-it problems**, same freedom and same condition.

### 3. `the-quadratic-formula`

**Able to:** Derive the quadratic formula by completing the square on the general equation, apply it, and use the discriminant to predict the number and type of roots before solving.

**The idea that carries it:** $x = \frac{-b \pm \sqrt{b^{2} - 4ac}}{2a}$ is completing the square done once on the general equation, and the sign of $b^{2} - 4ac$ tells you what kind of answer to expect before you compute it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Substituting $b$ without its sign.
- Dividing only the radical by $2a$.
- Applying the formula without moving everything to one side.
- Reading $D < 0$ as 'no solutions'.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u4-l3-we1` — Derive the quadratic formula by completing the square on $ax^{2} + bx + c = 0$.
- `im2-u4-l3-we2` — Solve $2x^{2} - 7x - 4 = 0$ with the quadratic formula, and confirm with factoring.
- `im2-u4-l3-we3` — Use the discriminant to describe the roots of each, without solving: (a) $x^{2} - 6x + 9 = 0$; (b) $2x^{2} + 3x - 4 = 0$; (c) $x^{2} + x + 5 = 0$; (d)
- `im2-u4-l3-we4` — A ball is kicked from ground level and its height in metres after $t$ seconds is $h(t) = -5t^{2} + 17t$. Find when it is $12$ metres high, and when it

**2 try-it problems**, same freedom and same condition.

### 4. `complex-numbers`

**Able to:** Define $i$, write numbers in the form $a + bi$, add, subtract and multiply complex numbers, and solve quadratic equations with a negative discriminant.

**The idea that carries it:** $i^{2} = -1$ is the only new fact; every negative discriminant then yields a conjugate pair $a \pm bi$, so every quadratic has exactly two roots.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing $\sqrt{-9} \cdot \sqrt{-4} = \sqrt{36} = 6$.
- Dividing only one term of the numerator by $2a$.
- Leaving $i^{2}$ in an answer.
- Saying a negative discriminant means 'no solutions'.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u4-l4-we1` — Simplify $\sqrt{-49}$, $\sqrt{-18}$ and $i^{2} + i^{4}$.
- `im2-u4-l4-we2` — Compute $(3 + 5i) + (2 - 8i)$, $(3 + 5i) - (2 - 8i)$, and $(3 + 5i)(2 - 8i)$.
- `im2-u4-l4-we3` — Solve $x^{2} + 4x + 13 = 0$.
- `im2-u4-l4-we4` — Solve $2x^{2} - 4x + 5 = 0$, and explain what the answer means about the graph of $y = 2x^{2} - 4x + 5$.

**2 try-it problems**, same freedom and same condition.

### 5. `linear-and-quadratic-systems`

**Able to:** Solve a system of one linear and one quadratic equation algebraically by substitution, interpret the solutions as intersection points, and use the discriminant to count them in advance — including the tangent case.

**The idea that carries it:** Substitute the line into the curve to get one quadratic in $x$, then let the discriminant count the intersections: positive two, zero tangent, negative none. Finish by putting each $x$ back into the LINE to get its $y$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting the x values and stopping.
- Substituting back into the quadratic instead of the line.
- Treating a zero discriminant as 'no solution'.
- Solving the tangency condition by trial and error.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u4-l5-we1` — Solve the system $y = x^2 - 2x - 3$ and $y = x + 1$.
- `im2-u4-l5-we2` — Show that the line $y = 2x - 5$ is tangent to the parabola $y = x^2 - 4$, and find the point of contact.
- `im2-u4-l5-we3` — For which value of $k$ is the line $y = 4x + k$ tangent to the parabola $y = x^2 + 2x + 7$?

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
| tangent | **шүргэгч** | ministry standard |
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| amount | **хэмжээ** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| square | **квадрат** | ministry standard |
| system | **систем** | ministry standard |
| counting | **тоолох** | ministry standard |
| rational | **рационал** | ministry standard |
| unit | **нэгж** | ministry standard |
| parabola | **парабол** | already on the site |
| formula | **томьёо** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| halve | **хагаслах** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**amount** — proposed **хэмжээ**

> POLYSEMOUS, and the shipped mirrors genuinely disagree, which is why this is medium. хэмжээ is the dominant choice for "amount" as a quantity of something (three of the four lines given with this term, plus the decimal-division unit throughout) and is what this entry proposes. But when "amounts" means measurable numerical quantities in the data-type sense, shipped switches to хэмжигдэхүүн: "**Numerical** data: amounts you can add and average" → «**Тоон** өгөгдөл: нэмж, дундажилж болох хэмжигдэхүүн», and "Category labels are not amounts" → «Ангиллын шошго бол хэмжигдэхүүн биш». That is the same word the ministry uses as the title of its measurement strand (MoE 10.12 «Хэмжигдэхүүн»). Suggested split: хэмжээ for a concrete amount in a problem, хэмжигдэхүүн for "quantity" as a category of data. Note хэмжээ is also this batch's "size".

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
## solving-by-factoring-and-roots

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u4-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u4-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## completing-the-square

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u4-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u4-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u4-l1-we1` and so on) exactly
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

