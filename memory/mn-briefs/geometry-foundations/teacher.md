# MN authoring brief — Foundations: Points, Lines & Angles

**Topic** `geometry/foundations` · **8 lessons** · 16 worked examples · 8 practice · 6 test-yourself

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
> `geometry/foundations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `points-lines-planes`

**Able to:** Recognize and name points, lines, and planes; know that two points determine exactly one line; tell when points are collinear.

**The idea that carries it:** Point = a location; line = straight, forever, both ways; plane = flat, forever. Two points → exactly one line.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking the drawn dot IS the point.
- Treating a line as if it stops at the arrows.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `plp-we1` — How many different lines pass through both point $A$ and point $B$?
- `plp-we2` — Points $P$, $Q$, $R$ are noncollinear. How many lines do they determine in pairs?

**2 try-it problems**, same freedom and same condition.

### 2. `segments-and-rays`

**Able to:** Distinguish lines, rays, and segments; use the notations for each; understand that ray AB and ray BA are different objects.

**The idea that carries it:** Segment = between two endpoints. Ray = one endpoint, one direction, forever. The first letter of a ray is its start.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating $\overrightarrow{AB}$ and $\overrightarrow{BA}$ as the same ray.
- Drawing a segment with arrowheads.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sr-we1` — On a number line, $A$ is at $2$ and $B$ is at $5$. Is the point at $9$ on ray $\overrightarrow{AB}$? On ray $\overrightarrow{BA}$?
- `sr-we2` — $A$ is at $1$ and $B$ at $6$. Is the point at $4$ on segment $\overline{AB}$?

**2 try-it problems**, same freedom and same condition.

### 3. `measuring-segments`

**Able to:** Use the Ruler Postulate to find segment lengths as |a − b|, and recognize congruent segments.

**The idea that carries it:** Number the line like a ruler; length = |difference of the end coordinates|. Equal lengths ⇒ congruent segments.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the right-hand number as the length.
- Getting a negative length.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ms-we1` — $A$ is at $2$ and $B$ at $7$. Find $AB$.
- `ms-we2` — $C$ is at $-3$ and $D$ at $4$. Find $CD$.

**2 try-it problems**, same freedom and same condition.

### 4. `segment-addition-midpoint`

**Able to:** Use the Segment Addition Postulate (AB + BC = AC when B is between A and C) to find missing lengths, and use midpoints to halve and double.

**The idea that carries it:** B between A and C ⇒ AB + BC = AC. Midpoint = the point making both halves equal (coordinate = average).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding when a part is missing.
- Using segment addition when B isn't between A and C.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sa-we1` — $B$ is between $A$ and $C$, $AB = 4$ and $BC = 6$. Find $AC$.
- `sa-we2` — $M$ is the midpoint of $\overline{PQ}$ and $PQ = 14$. Find $PM$.

**2 try-it problems**, same freedom and same condition.

### 5. `naming-measuring-angles`

**Able to:** Define an angle as two rays with a common vertex, name it correctly (vertex in the middle), and measure it in degrees with a protractor.

**The idea that carries it:** Angle = two rays + one vertex. Name it with the vertex in the middle; measure in degrees, subtracting protractor readings if needed.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the vertex first or last, like ∠BAC for an angle at B.
- Reading only one protractor number.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `na-we1` — A protractor shows one side of an angle at $20^\circ$ and the other at $75^\circ$. Find the measure.
- `na-we2` — In $\angle PQR$, the protractor reads $25^\circ$ for side $\overrightarrow{QP}$ and $65^\circ$ for side $\overrightarrow{QR}$. Name the vertex and fin

**2 try-it problems**, same freedom and same condition.

### 6. `classifying-angles`

**Able to:** Classify angles as acute, right, obtuse, or straight from their degree measures, with 90° and 180° as exact boundaries.

**The idea that carries it:** Compare to 90 and 180: under 90 acute, exactly 90 right, between right and straight obtuse, exactly 180 straight.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling 90° acute (or obtuse).
- Judging by the drawing's size on the page.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ca-we1` — Classify an angle of $132^\circ$.
- `ca-we2` — Classify an angle of exactly $90^\circ$.

**2 try-it problems**, same freedom and same condition.

### 7. `angle-pairs`

**Able to:** Identify adjacent angles, vertical angles, linear pairs, and complementary/supplementary pairs — knowing which are congruent and which sum to 90° or 180°.

**The idea that carries it:** Vertical = congruent. Linear pair = supplementary (180°). Complementary = 90° total. Supplementary = 180° total.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Saying vertical angles are supplementary.
- Mixing up complementary and supplementary.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ap-we1` — Two lines cross; one angle measures $115^\circ$. Find the other three.
- `ap-we2` — Two angles are complementary; one is $35^\circ$. Find the other.

**2 try-it problems**, same freedom and same condition.

### 8. `bisectors`

**Able to:** Use segment bisectors and angle bisectors to halve and double measures — and read your first two-column proof, built from Unit 1 facts.

**The idea that carries it:** A bisector makes two congruent halves. Halve the whole ÷2; recover the whole ×2. Each claim gets a reason — that's proof.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doubling when you should halve (or the reverse).
- Assuming any ray inside the angle bisects it.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bi-we1` — $\overrightarrow{BD}$ bisects $\angle ABC$ and $m\angle ABC = 84^\circ$. Find $m\angle ABD$.
- `bi-we2` — $\overrightarrow{QS}$ bisects $\angle PQR$ and $m\angle PQS = 33^\circ$. Find $m\angle PQR$.

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
| complement | **нэмэлт** | already on the site |
| measure | **хэмжих** | ministry standard |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| geometry | **геометр** | ministry standard |
| proof | **баталгаа** | already on the site |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| plane | **хавтгай** | ministry standard |
| addition | **нэмэх** | ministry standard |
| formula | **томьёо** | ministry standard |
| vertical | **босоо** | ministry standard |
| halve | **хагаслах** | already on the site |
| midpoint | **дундаж цэг** | ministry standard |
| difference | **ялгавар** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

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
## points-lines-planes

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED plp-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY plp-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## segments-and-rays

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sr-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sr-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`plp-we1` and so on) exactly
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

