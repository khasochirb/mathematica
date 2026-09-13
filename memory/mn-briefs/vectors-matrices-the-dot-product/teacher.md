# MN authoring brief — The Dot Product

**Topic** `vectors-matrices/the-dot-product` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `vectors-matrices/the-dot-product`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `multiplying-vectors`

**Able to:** Compute u·v from components, connect it to |u||v|cos θ, and use v·v = |v|².

**The idea that carries it:** u·v = x₁x₂ + y₁y₂ = |u||v|cos θ — one number, two recipes; and v·v = |v|².

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting the dot product as a vector like (8, −3).
- Using the angle formula with the wrong angle.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm31-we1` — Compute $(2, 3) \cdot (4, -1)$.
- `vm31-we2` — Verify $\vec{v} \cdot \vec{v} = |\vec{v}|^2$ for $\vec{v} = (3, 4)$.
- `vm31-we3` — Find the angle between $\vec{u} = (1, 0)$ and $\vec{v} = (1, 1)$.

**2 try-it problems**, same freedom and same condition.

### 2. `angles-between-vectors`

**Able to:** Compute cos θ from components, classify angles by the dot product's sign, and recover exact angles for the standard cosine values.

**The idea that carries it:** cos θ = u·v / (|u||v|); the sign of u·v alone calls acute / right / obtuse.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the lengths in the denominator.
- Rationalizing errors with the surds.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm32-we1` — Find $\cos\theta$ for $\vec{u} = (3, 4)$ and $\vec{v} = (4, 3)$.
- `vm32-we2` — Find the exact angle between $\vec{u} = (1, 2)$ and $\vec{v} = (3, 1)$.
- `vm32-we3` — Classify the angle between $\vec{u} = (1, 1)$ and $\vec{v} = (-2, 1)$, then compute $\cos\theta$.

**2 try-it problems**, same freedom and same condition.

### 3. `perpendicularity`

**Able to:** Use u·v = 0 as the perpendicularity test, solve for unknown components, and verify right angles in figures with vectors.

**The idea that carries it:** u ⊥ v ⇔ u·v = 0; unknown components fall out of one linear equation; right angles in figures are zero dots of tip-minus-tail vectors.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the parallel test for perpendicularity.
- Checking the right angle at the wrong vertex.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm33-we1` — Find $k$ so that $(2, k) \perp (3, 4)$.
- `vm33-we2` — Find $k$ so that $(k, 3)$ is perpendicular to $(2, k - 5)$.
- `vm33-we3` — Triangle $ABC$ has $A(0, 0)$, $B(4, 2)$, $C(-1, 2)$. Show the right angle sits at $A$.

**2 try-it problems**, same freedom and same condition.

### 4. `dot-product-toolbox`

**Able to:** Expand |u ± v|² via the dot product, and solve length-and-angle problems where components are never given.

**The idea that carries it:** |u ± v|² = |u|² ± 2u·v + |v|² — lengths of combinations without ever seeing a component.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing |u + v| = |u| + |v|.
- Sign slip on the minus expansion.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm34-we1` — Given $|\vec{u}| = 3$, $|\vec{v}| = 5$, and $\vec{u} \cdot \vec{v} = -2$, find $|\vec{u} + \vec{v}|$.
- `vm34-we2` — $|\vec{u}| = 2$, $|\vec{v}| = 3$, and the angle between them is $60°$. Find $|\vec{u} - \vec{v}|$.
- `vm34-we3` — A force $\vec{F} = (8, 6)$ moves an object along the displacement $\vec{d} = (3, 0)$. Compute the work $W = \vec{F} \cdot \vec{d}$.

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
| angle | **өнцөг** | ministry standard |
| cosine | **косинус** | ministry standard |
| product | **үржвэр** | ministry standard |
| geometry | **геометр** | ministry standard |
| number | **тоо** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| zero | **тэг** | ministry standard |
| formula | **томьёо** | ministry standard |
| linear | **шугаман** | ministry standard |
| problem | **бодлого** | ministry standard |
| length | **урт** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| test | **шалгалт** | ministry standard |

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
## multiplying-vectors

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm31-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm31-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## angles-between-vectors

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm32-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm32-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm31-we1` and so on) exactly
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

