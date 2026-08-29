# MN authoring brief — Prisms & the Cube

**Topic** `solid-geometry/prisms-and-the-cube` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `solid-geometry/prisms-and-the-cube`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `what-is-a-prism`

**Able to:** Name the parts of a prism (bases, lateral faces, edges, height), distinguish right from oblique prisms, and count elements.

**The idea that carries it:** Prism = polygon slid to a parallel copy. Right prism: slide is perpendicular (faces are rectangles). Height = distance between base planes, not necessarily the lateral edge.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the lateral edge as the height of an oblique prism.
- Counting a prism's faces as just the lateral ones and forgetting the two bases.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg21-we1` — A prism has a hexagonal base. Count its vertices, edges, and faces, and verify Euler's formula $V - E + F = 2$.
- `sg21-we2` — An oblique prism has lateral edge $10$ making a $60°$ angle with the base plane. Find the prism's height.

**2 try-it problems**, same freedom and same condition.

### 2. `the-cube-and-its-diagonals`

**Able to:** Compute a cube's face diagonal (a√2) and space diagonal (a√3) by running Pythagoras twice, and extend to the general box diagonal.

**The idea that carries it:** Face diagonal a√2, space diagonal a√3; for any box d = √(l² + w² + h²) — Pythagoras across the floor, then Pythagoras up the wall.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using a√2 for the space diagonal (or a√3 for the face diagonal).
- Adding the three edges' squares only for cubes, but improvising for boxes.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg22-we1` — A cube has edge $6$. Find its face diagonal and space diagonal, exactly.
- `sg22-we2` — A box measures $3 \times 4 \times 12$. Find its space diagonal.

**2 try-it problems**, same freedom and same condition.

### 3. `surface-area-of-prisms`

**Able to:** Compute lateral and total surface area of right prisms via the unfolded net: S_lat = (base perimeter) × height.

**The idea that carries it:** Unroll the walls into one rectangle: S_lat = P·h. Add the two bases for the total: S = P·h + 2B.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the bases (or counting only one).
- Using a slant edge as the height in S_lat = P·h for an oblique prism.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg23-we1` — Find the total surface area of a $3 \times 4 \times 5$ box.
- `sg23-we2` — A right prism of height $10$ stands on a right-triangle base with legs $6$ and $8$. Find its lateral and total surface area.

**2 try-it problems**, same freedom and same condition.

### 4. `volume-of-prisms`

**Able to:** Compute prism volumes with V = B·h, including composite bases, and use Cavalieri's idea for oblique prisms.

**The idea that carries it:** V = B·h — base area times true height, for right AND oblique prisms (Cavalieri: leaning doesn't change slice areas).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying by the lateral edge instead of the true height for oblique prisms.
- Doubling the base area 'because there are two bases' (importing surface-area thinking).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sg24-we1` — A right prism of height $10$ has a right-triangle base with legs $6$ and $8$. Find its volume.
- `sg24-we2` — An oblique prism has base area $30$ and lateral edge $12$ leaning at $30°$ to the base plane. Find its volume.

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
| count | **тоолох** | ministry standard |
| base | **суурь** | ministry standard |
| edge | **ирмэг** | already on the site |
| volume | **эзлэхүүн** | ministry standard |
| area | **талбай** | ministry standard |
| parallel | **параллель** | ministry standard |
| distance | **зай** | ministry standard |
| time | **цаг** | already on the site |
| plane | **хавтгай** | ministry standard |
| surface area | **гадаргуугийн талбай** | ministry standard |
| perimeter | **периметр** | already on the site |
| cube | **шоо** | already on the site |
| rectangle | **тэгш өнцөгт** | ministry standard |
| height | **өндөр** | already on the site |
| part | **хэсэг** | ministry standard |
| total | **нийт** | already on the site |
| face | **нүүр** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

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
## what-is-a-prism

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg21-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg21-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-cube-and-its-diagonals

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sg22-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sg22-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`sg21-we1` and so on) exactly
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

