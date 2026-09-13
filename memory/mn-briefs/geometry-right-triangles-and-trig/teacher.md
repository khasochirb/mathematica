# MN authoring brief — Right Triangles & Trigonometry

**Topic** `geometry/right-triangles-and-trig` · **7 lessons** · 15 worked examples · 8 practice · 6 test-yourself

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
> `geometry/right-triangles-and-trig`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-pythagorean-theorem`

**Able to:** Use a² + b² = c² to find a missing side of a right triangle, and recognize Pythagorean triples.

**The idea that carries it:** In a right triangle, legs a, b and hypotenuse c satisfy a² + b² = c². Find the hypotenuse with √(a²+b²) and a leg with √(c²−b²). Whole-number solutions are Pythagorean triples.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the hypotenuse formula to find a leg.
- Treating a leg as the hypotenuse.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `py-we1` — A right triangle has legs $6$ and $8$. Find the hypotenuse.
- `py-we2` — A right triangle has hypotenuse $13$ and one leg $5$. Find the other leg.

**2 try-it problems**, same freedom and same condition.

### 2. `converse-and-classifying`

**Able to:** Use the converse of the Pythagorean theorem to test whether three sides form a right triangle, and classify a triangle by comparing a² + b² to c².

**The idea that carries it:** Test three sides with the longest as c: a²+b² = c² → right; a²+b² > c² → acute; a²+b² < c² → obtuse.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing with the wrong side as $c$.
- Mixing up which way acute vs obtuse goes.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cv-we1` — Do sides $6, 8, 10$ form a right triangle?
- `cv-we2` — Classify a triangle with sides $4, 5, 6$.

**2 try-it problems**, same freedom and same condition.

### 3. `special-right-triangles`

**Able to:** Use the 45-45-90 ratio (leg : leg : leg√2) and the 30-60-90 ratio (x : x√3 : 2x) to find sides without recomputing.

**The idea that carries it:** 45-45-90: legs equal, hypotenuse = leg·√2. 30-60-90: short leg x, long leg x√3, hypotenuse 2x. Memorize the ratios instead of re-deriving.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying the wrong leg by √3 in a 30-60-90.
- Using √2 for a 30-60-90 or √3 for a 45-45-90.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sr-we1` — A 45-45-90 triangle has legs of $7$. Find the hypotenuse.
- `sr-we2` — A 30-60-90 triangle has short leg $6$. Find the hypotenuse and long leg.

**2 try-it problems**, same freedom and same condition.

### 4. `trigonometric-ratios`

**Able to:** Name the sides of a right triangle relative to an angle (opposite, adjacent, hypotenuse) and compute sine, cosine, and tangent from the side lengths (SOH-CAH-TOA).

**The idea that carries it:** Relative to an acute angle θ: sin θ = opp/hyp, cos θ = adj/hyp, tan θ = opp/adj. The ratios depend only on the angle because same-angle right triangles are similar.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling the hypotenuse the 'adjacent' side.
- Mixing up which ratio is which.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr-we1` — In a right triangle, the side opposite $\theta$ is $6$ and the hypotenuse is $10$. Find $\sin\theta$.
- `tr-we2` — The side adjacent to $\theta$ is $4$, the opposite is $3$. Find $\tan\theta$.

**2 try-it problems**, same freedom and same condition.

### 5. `finding-sides-with-trig`

**Able to:** Use sine, cosine, or tangent to find a missing side of a right triangle from a known side and angle, including the exact values at 30°, 45°, and 60°.

**The idea that carries it:** To find a missing side, pick the ratio (sin/cos/tan) linking the known side, unknown side, and angle; substitute and solve. The 30°/45°/60° values are exact.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Choosing a ratio that uses a side you don't have.
- Forgetting the exact special-angle values.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fs-we1` — A right triangle has hypotenuse $10$ and an angle of $30^\circ$. Find the side opposite the $30^\circ$ angle.
- `fs-we2` — A ramp rises from the ground at $45^\circ$; its horizontal run (adjacent) is $8$. How high does it rise (opposite)?

**2 try-it problems**, same freedom and same condition.

### 6. `elevation-depression-inverse-trig`

**Able to:** Find an unknown angle with inverse trig (arcsin, arccos, arctan), and solve angle-of-elevation and angle-of-depression problems.

**The idea that carries it:** Inverse trig (arcsin/arccos/arctan) turns a side ratio into an angle. Angles of elevation (up) and depression (down) are equal alternate interior angles; model the situation as a right triangle and apply tan or its inverse.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using $\sin$ instead of $\sin^{-1}$ to find an angle.
- Measuring depression from the vertical.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ed-we1` — You stand $10$ m from a flagpole and the top is $10$ m above your eye level ($\text{opp} = 10$, $\text{adj} = 10$). Find the angle of elevation to the
- `ed-we2` — A ramp rises $1$ m over a horizontal run of $\sqrt3$ m. Find its angle of elevation.

**2 try-it problems**, same freedom and same condition.

### 7. `law-of-sines-and-cosines`

**Able to:** Solve any triangle: use the law of sines with an angle-side pair, the law of cosines with two sides and the included angle (or three sides), and the sine area formula.

**The idea that carries it:** Angle–side pair → law of sines (= 2R); two sides + included angle, or three sides → law of cosines; area = ½ab·sin C.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the law of sines with two sides and the included angle.
- Dropping the −2ab·cos C term's sign with obtuse angles.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `lsc-we1` — In a triangle, $A = 30°$, $B = 45°$, and the side opposite $A$ is $a = 10$. Find $b$.
- `lsc-we2` — Two sides measure $5$ and $8$ with a $60°$ angle between them. Find the third side.
- `lsc-we3` — A triangle has sides $7$, $8$, and $13$. Find the angle opposite the side of length $13$.

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
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| number | **тоо** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| formula | **томьёо** | ministry standard |
| problem | **бодлого** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| side | **тал** | ministry standard |
| model | **загвар** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

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
## the-pythagorean-theorem

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED py-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY py-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## converse-and-classifying

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cv-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cv-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`py-we1` and so on) exactly
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

