# MN authoring brief — Vectors & Coordinates

**Topic** `vectors-matrices/vectors-and-coordinates` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `vectors-matrices/vectors-and-coordinates`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `what-is-a-vector`

**Able to:** Distinguish vectors from scalars, read a displacement vector between two points, and recognize that vectors with the same components are the same vector.

**The idea that carries it:** A vector = magnitude + direction, encoded as components (tip − tail); same components = same vector, wherever it's drawn.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing tail minus tip.
- Treating vectors at different positions as different.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm11-we1` — A ship sails from $A(1, 2)$ to $B(4, 6)$. Find the displacement vector $\overrightarrow{AB}$ and the distance sailed.
- `vm11-we2` — $\overrightarrow{AB}$ runs from $A(0,0)$ to $B(2,3)$; $\overrightarrow{CD}$ runs from $C(5,1)$ to $D(7,4)$. Show they are the same vector.
- `vm11-we3` — For $\vec{v} = (6, -2)$, write $-\vec{v}$ and compare the two magnitudes.

**2 try-it problems**, same freedom and same condition.

### 2. `components-and-magnitude`

**Able to:** Fluently compute components from points, magnitudes from components, and solve for unknown components given a magnitude.

**The idea that carries it:** Components are everything: subtract points to get them, Pythagoras to measure them, and solve x² + y² = |v|² when a component hides.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting only the positive root when a component is unknown.
- Letting a negative component survive the squaring.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm12-we1` — Find the magnitude of $\vec{v} = (-5, 12)$.
- `vm12-we2` — $A(-2, 3)$ and $B(4, -5)$. Find $\overrightarrow{AB}$ and $|\overrightarrow{AB}|$.
- `vm12-we3` — The vector $(x, 6)$ has magnitude $10$. Find every possible $x$.

**2 try-it problems**, same freedom and same condition.

### 3. `equal-opposite-and-parallel`

**Able to:** Test vectors for equality, oppositeness, and parallelism via scalar multiples and the cross-multiplication test, and use parallelism to prove collinearity.

**The idea that carries it:** Parallel ⇔ scalar multiple ⇔ x₁y₂ = x₂y₁; opposite is k = −1; collinear points come from parallel shared-tail vectors.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Concluding 'not parallel' because the vectors have different lengths.
- Testing collinearity with vectors that share no point.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm13-we1` — Are $(2, -3)$ and $(-6, 9)$ parallel? If so, find the scalar.
- `vm13-we2` — Find $k$ so that $(4, k)$ is parallel to $(6, 9)$.
- `vm13-we3` — Show that $A(1, 1)$, $B(3, 5)$, $C(6, 11)$ are collinear.

**2 try-it problems**, same freedom and same condition.

### 4. `unit-vectors-and-direction`

**Able to:** Normalize a vector to unit length, use the i–j basis notation, and construct a vector of prescribed length in a prescribed direction.

**The idea that carries it:** v̂ = v/|v| is pure direction; every vector = its length × its unit vector; i, j are just (1,0) and (0,1).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing by a component instead of the magnitude.
- Writing 2i − 5j as (2, 5).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm14-we1` — Find the unit vector in the direction of $(3, 4)$.
- `vm14-we2` — Write $\vec{v} = 2\vec{i} - 5\vec{j}$ in component form and find its magnitude.
- `vm14-we3` — Construct the vector of length $20$ in the direction of $(3, -4)$.

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
| measure | **хэмжих** | ministry standard |
| parallel | **параллель** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| number | **тоо** | ministry standard |
| unit | **нэгж** | ministry standard |
| point | **цэг** | ministry standard |
| opposite | **эсрэг** | already on the site |
| coordinate | **координат** | ministry standard |
| length | **урт** | ministry standard |
| subtract | **хасах** | ministry standard |
| direction | **чиглэл** | ministry standard |
| equal | **тэнцүү** | ministry standard |
| test | **шалгалт** | ministry standard |
| vector | **вектор** | ministry standard |
| magnitude | **векторын урт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

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
## what-is-a-vector

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm11-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm11-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## components-and-magnitude

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm12-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm12-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm11-we1` and so on) exactly
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

