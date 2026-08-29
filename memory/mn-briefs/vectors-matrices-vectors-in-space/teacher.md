# MN authoring brief — Vectors in Space

**Topic** `vectors-matrices/vectors-in-space` · **4 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `vectors-matrices/vectors-in-space`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `coordinates-in-3d`

**Able to:** Work with 3D components: read vectors between points, compute magnitudes, and solve for unknown components.

**The idea that carries it:** Space = one more lane: AB = B − A and |v| = √(x² + y² + z²); everything else transfers verbatim.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Leaving the z-term out of the magnitude.
- Sign chaos in three subtractions.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm41-we1` — Find $|(2, 3, 6)|$.
- `vm41-we2` — $A(1, 2, 3)$ and $B(3, 0, -1)$. Find $\overrightarrow{AB}$ and its magnitude.
- `vm41-we3` — The vector $(x, 4, 12)$ has magnitude $14$. Find every possible $x$.

**2 try-it problems**, same freedom and same condition.

### 2. `arithmetic-and-dot-in-3d`

**Able to:** Add, scale, and dot vectors in 3D; test perpendicularity; and find exact angles in space.

**The idea that carries it:** All Unit-3 machinery + one more term: u·v = x₁x₂ + y₁y₂ + z₁z₂; angles and perpendicularity work verbatim in space.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the z-term from the dot product.
- Testing parallel with only two of the three ratios.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm42-we1` — Compute $(1, 2, 3) \cdot (4, -5, 6)$.
- `vm42-we2` — Find $k$ so that $(2, 1, k) \perp (3, -2, 2)$.
- `vm42-we3` — Find the exact angle between $\vec{u} = (1, 1, 0)$ and $\vec{v} = (0, 1, 1)$.

**2 try-it problems**, same freedom and same condition.

### 3. `the-box-diagonal`

**Able to:** Compute the space diagonal of a rectangular box and a cube, and solve for an unknown edge from a known diagonal.

**The idea that carries it:** Space diagonal d = √(a² + b² + c²); cube: a√3 (face: a√2); run it backwards for a missing edge.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the face diagonal when the problem wants the space diagonal.
- Cube confusion: a√2 vs a√3.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm43-we1` — Find the space diagonal of a $3 \times 4 \times 12$ box.
- `vm43-we2` — Find the space diagonal of a cube with edge $5$.
- `vm43-we3` — A box has space diagonal $25$ and two edges $9$ and $12$. Find the third edge.

**2 try-it problems**, same freedom and same condition.

### 4. `normals-and-planes`

**Able to:** Read the normal vector off a plane's equation, and test planes (and lines) for parallelism and perpendicularity via their normals.

**The idea that carries it:** ax + by + cz = d has normal (a, b, c); planes compare by their normals — parallel normals ⇒ parallel planes, zero dot ⇒ perpendicular planes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking d changes the plane's direction.
- Testing plane-parallelism with a dot product.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `vm44-we1` — Write the normal vector of the plane $2x - 3y + 6z = 12$ and find its magnitude.
- `vm44-we2` — Are the planes $2x - y + z = 3$ and $4x - 2y + 2z = 9$ parallel?
- `vm44-we3` — Show the planes $x + 2y - z = 4$ and $3x - y + z = 7$ are perpendicular.

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
| edge | **ирмэг** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| parallel | **параллель** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| plane | **хавтгай** | ministry standard |
| cube | **шоо** | already on the site |
| point | **цэг** | ministry standard |
| coordinate | **координат** | ministry standard |
| face | **нүүр** | already on the site |
| test | **шалгалт** | ministry standard |
| arithmetic | **арифметик** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**edge** — proposed **ирмэг**

> POLYSEMOUS, mildly. ирмэг is the edge of a solid (shipped and ЭШ alike) and, by extension, the edge of a histogram bin («ирмэг: $20$ нь $20$–$29$-ийг эхлүүлнэ») — that is the sense proposed here. Where "edge" means the margin of something written or laid out, shipped uses зах: "Line up the decimal points, not the right edges" → «Аравтын цэгүүдийг зэрэгцүүл, баруун захыг биш». So: ирмэг for geometry and bins, зах for the right-hand edge of a written column.

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
## coordinates-in-3d

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm41-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm41-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## arithmetic-and-dot-in-3d

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED vm42-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY vm42-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`vm41-we1` and so on) exactly
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

