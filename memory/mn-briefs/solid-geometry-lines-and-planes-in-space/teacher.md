# MN authoring brief — Lines & Planes in Space

**Topic** `solid-geometry/lines-and-planes-in-space` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `solid-geometry/lines-and-planes-in-space`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `planes-and-how-they-meet`

**Able to:** Use the axioms of space: what determines a plane, and the three ways a line or another plane can meet it.

**The idea that carries it:** Three non-collinear points fix a plane; a line meets a plane in 0, 1, or infinitely many points; two non-parallel planes always meet in a line.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking two planes can intersect in a single point, the way two lines do.
- Assuming any 3 points determine a plane — forgetting the collinear exception.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg11-we1` — How many distinct planes are determined by $4$ points in space, no $3$ of them collinear and not all $4$ in one plane?
- `sg11-we2` — A cube has $6$ faces. Each pair of ADJACENT faces meets in an edge (a line segment). Count the edges by counting adjacent face-pairs.

**2 try-it problems**, same freedom and same condition.

### 2. `parallel-and-skew-lines`

**Able to:** Classify pairs of lines in space (intersecting, parallel, skew) and recognize when a line is parallel to a plane.

**The idea that carries it:** In space, non-meeting lines split into parallel (same plane, same direction) and skew (no common plane). A line is parallel to a plane iff it's parallel to a line inside it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling any two non-meeting lines 'parallel'.
- Trusting the drawing: two segments that cross on PAPER must intersect in space.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg12-we1` — In cube $ABCDA'B'C'D'$, classify each pair: (a) $AB$ and $A'B'$; (b) $AB$ and $CC'$; (c) $AB$ and $BC$.
- `sg12-we2` — A cube has $12$ edges. Pick edge $AB$. Of the other $11$ edges, how many are parallel to $AB$, how many intersect it, and how many are skew to it?

**2 try-it problems**, same freedom and same condition.

### 3. `perpendicular-to-a-plane`

**Able to:** Use the definition and criterion of line ⊥ plane, and compute distances via the perpendicular-and-oblique right triangle.

**The idea that carries it:** ⊥ to two intersecting lines of a plane ⟹ ⊥ to the whole plane. Distance from a point = the perpendicular, and perpendicular + oblique always form a right triangle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Checking perpendicularity against just ONE line of the plane and concluding ⊥ to the plane.
- Taking an oblique segment as 'the distance' to the plane.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg13-we1` — $PF \perp \alpha$ with $PF = 4$. Point $A$ lies in $\alpha$ with $FA = 3$. Find the oblique $PA$.
- `sg13-we2` — From point $P$, two obliques of length $10$ and an unknown one reach plane $\alpha$. The perpendicular is $PF = 6$. The feet of the length-10 obliques

**2 try-it problems**, same freedom and same condition.

### 4. `angles-in-space`

**Able to:** Measure the angle between a line and a plane (via the projection) and between two planes (the dihedral angle, via two perpendiculars to the edge).

**The idea that carries it:** Line-plane angle = angle between the line and its projection (sin θ = height/oblique). Plane-plane angle = angle between two rays ⊥ to the edge, one in each plane.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the line-plane angle between the line and some random line of the plane.
- Measuring a dihedral angle with rays that aren't perpendicular to the edge.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg14-we1` — An oblique $PA = 6$ meets plane $\alpha$; the perpendicular from $P$ is $PF = 3$. Find the angle between $PA$ and the plane.
- `sg14-we2` — At point $M$ on the edge of a dihedral angle, ray $MK \perp$ edge is drawn in plane $\alpha$ and ray $MN \perp$ edge in plane $\beta$, with $MK = MN =

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
| range | **далайц** | ministry standard |
| measure | **хэмжих** | ministry standard |
| edge | **ирмэг** | already on the site |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| distance | **зай** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| plane | **хавтгай** | ministry standard |
| point | **цэг** | ministry standard |
| skew | **хазайсан** | ministry standard |
| form | **хэлбэр** | ministry standard |
| height | **өндөр** | already on the site |
| pair | **хос** | ministry standard |
| direction | **чиглэл** | ministry standard |
| the whole | **бүхэл** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

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
## planes-and-how-they-meet

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg11-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg11-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## parallel-and-skew-lines

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg12-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg12-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sg11-we1` and so on) exactly
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

