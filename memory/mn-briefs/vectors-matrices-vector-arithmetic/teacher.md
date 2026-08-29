# MN authoring brief — Vector Arithmetic

**Topic** `vectors-matrices/vector-arithmetic` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `vectors-matrices/vector-arithmetic`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `adding-vectors`

**Able to:** Add vectors componentwise, chain displacements tip-to-tail, and read the triangle and parallelogram pictures of a sum.

**The idea that carries it:** Add components; picture it tip-to-tail (triangle) or tail-to-tail (parallelogram); AB + BC = AC — middle letters cancel.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding magnitudes instead of vectors.
- Breaking the tip-to-tail chain.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm21-we1` — Compute $(2, 3) + (4, -1)$ and the magnitude of the sum.
- `vm21-we2` — A hiker walks $3$ km east, then $4$ km north. Find the resultant displacement and its magnitude.
- `vm21-we3` — Forces $(5, 0)$ and $(-2, 6)$ act on one object. Find the net force and its magnitude.

**2 try-it problems**, same freedom and same condition.

### 2. `scalars-and-subtraction`

**Able to:** Scale vectors, combine scaling with addition, subtract vectors, and solve simple vector equations.

**The idea that carries it:** k(x, y) = (kx, ky); u − v = u + (−v), drawn tip-of-v to tip-of-u; vector equations solve like ordinary algebra.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling only one component.
- Drawing u − v from u's tip to v's tip.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm22-we1` — Compute $3(2, -1) - 2(1, 4)$.
- `vm22-we2` — With $\vec{u} = (5, 2)$ and $\vec{v} = (1, 3)$ drawn from one point, find the vector from $\vec{v}$'s tip to $\vec{u}$'s tip.
- `vm22-we3` — Solve for $\vec{x}$: $\;2\vec{x} + (3, -1) = (7, 5)$.

**2 try-it problems**, same freedom and same condition.

### 3. `vectors-in-figures`

**Able to:** Express diagonals, midpoints, and medians of triangles and parallelograms in terms of two side vectors, and compute their lengths from components.

**The idea that carries it:** Name two side vectors, then walk the figure: diagonals are u + v and v − u; midpoints and medians average: AM = ½(AB + AC).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing BD = u − v instead of v − u.
- Averaging endpoints instead of vectors from the base point.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm23-we1` — In parallelogram $ABCD$, $\overrightarrow{AB} = (4, 1)$ and $\overrightarrow{AD} = (1, 3)$. Find the diagonal $\overrightarrow{AC}$ and its length.
- `vm23-we2` — Same parallelogram: find the other diagonal $\overrightarrow{BD}$ and its length.
- `vm23-we3` — In triangle $ABC$, $\overrightarrow{AB} = (6, 2)$ and $\overrightarrow{AC} = (2, 4)$. Find the median vector $\overrightarrow{AM}$ to side $BC$ and it

**2 try-it problems**, same freedom and same condition.

### 4. `the-section-formula`

**Able to:** Find the point dividing a segment in a given ratio, recognize the midpoint as the 1:1 case, and recover the ratio from a known dividing point.

**The idea that carries it:** AP : PB = m : n ⇒ P = (n·A + m·B)/(m + n); midpoint is the 1:1 case; ratios recover by comparing AP with PB.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Weighting each endpoint by its own ratio part.
- Forgetting to divide by m + n.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm24-we1` — $P$ divides $AB$ with $AP : PB = 2 : 1$, where $A(1, 2)$ and $B(7, 8)$. Find $P$.
- `vm24-we2` — Find the midpoint of $A(-4, 3)$ and $B(6, -1)$.
- `vm24-we3` — $P(3, 4)$ lies on segment $AB$ with $A(1, 2)$, $B(6, 7)$... wait — check it, then find $AP : PB$.

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
| scale | **томсгох** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| median | **медиан** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallelogram | **параллелограмм** | ministry standard |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| formula | **томьёо** | ministry standard |
| midpoint | **дундаж цэг** | ministry standard |
| algebra | **алгебр** | ministry standard |
| point | **цэг** | ministry standard |
| segment | **хэрчим** | already on the site |
| side | **тал** | ministry standard |
| subtracting | **хасах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

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
## adding-vectors

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm21-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm21-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## scalars-and-subtraction

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm22-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm22-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm21-we1` and so on) exactly
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

