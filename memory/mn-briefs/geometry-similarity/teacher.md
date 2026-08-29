# MN authoring brief — Similarity

**Topic** `geometry/similarity` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/similarity`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `ratio-proportion-scale-factor`

**Able to:** Write and simplify ratios, solve proportions using cross products, and use a scale factor to relate two sizes of the same shape.

**The idea that carries it:** A proportion sets two ratios equal; its cross products are equal (ad = bc), which solves for a missing term. A scale factor (image ÷ original) resizes every length by the same multiple.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding to compare instead of dividing.
- Cross-multiplying across an equals sign the wrong way.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rp-we1` — Simplify the ratio $12 : 8$.
- `rp-we2` — Solve the proportion $\tfrac{3}{4} = \tfrac{9}{x}$.

**2 try-it problems**, same freedom and same condition.

### 2. `similar-polygons`

**Able to:** Identify similar polygons (corresponding angles congruent and corresponding sides proportional), read a similarity statement, and use the scale factor to find a missing side.

**The idea that carries it:** Similar polygons have congruent corresponding angles AND proportional corresponding sides (a common scale factor). The similarity statement lists vertices in matching order; use a proportion to find missing sides.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assuming equal angles alone make polygons similar.
- Pairing sides in the wrong order.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sp-we1` — $\triangle ABC \sim \triangle DEF$ with $AB = 6$, $DE = 9$. Find the scale factor from $ABC$ to $DEF$.
- `sp-we2` — $\triangle ABC \sim \triangle DEF$, $\tfrac{AB}{DE} = \tfrac{4}{6}$, and $BC = 5$. Find $EF$.

**2 try-it problems**, same freedom and same condition.

### 3. `proving-triangles-similar`

**Able to:** Use the AA, SSS, and SAS similarity shortcuts to decide whether two triangles are similar.

**The idea that carries it:** Three shortcuts prove triangles similar: AA (two equal angle pairs), SSS~ (three sides in the same ratio), and SAS~ (two sides in ratio with congruent included angles). Similarity allows any scale factor; congruence forces factor 1.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking you need all three angles for AA.
- Calling similar triangles congruent.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ps-we1` — Two triangles have angle pairs $50^\circ, 60^\circ$ in common. Are they similar?
- `ps-we2` — Triangle 1 has sides $3, 4, 5$; triangle 2 has $6, 8, 10$. Similar?

**2 try-it problems**, same freedom and same condition.

### 4. `triangle-proportionality`

**Able to:** Use the Triangle Proportionality (Side-Splitter) Theorem — a line parallel to one side of a triangle divides the other two sides proportionally — together with its converse.

**The idea that carries it:** A line parallel to one side of a triangle splits the other two sides in the same ratio (AD/DB = AE/EC), because it creates a smaller similar triangle by AA. The converse proves parallelism from a proportional split.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting the WHOLE side against a piece.
- Forgetting the line must be parallel.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ss-we1` — In $\triangle ABC$, $DE \parallel BC$ with $AD = 4$, $DB = 6$, $AE = 6$. Find $EC$.
- `ss-we2` — $DE \parallel BC$; $AD = 5$, $DB = 10$, $AE = 4$. Find $EC$.

**2 try-it problems**, same freedom and same condition.

### 5. `perimeters-and-areas-of-similar-figures`

**Able to:** Use the fact that similar figures with scale factor k have perimeters in the ratio k and areas in the ratio k².

**The idea that carries it:** Similar figures with scale factor k have perimeters in ratio k and areas in ratio k². To recover k from an area ratio, take the square root.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling area by $k$ instead of $k^2$.
- Forgetting to square-root when going from area ratio to scale factor.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pa-we1` — Two similar triangles have scale factor $3$. If the small perimeter is $12$, find the large perimeter.
- `pa-we2` — Scale factor $2$; the small area is $5$. Find the large area.

**2 try-it problems**, same freedom and same condition.

### 6. `dilations-and-indirect-measurement`

**Able to:** Describe a dilation by its center and scale factor, and use similar triangles for indirect measurement (shadows and mirrors).

**The idea that carries it:** A dilation enlarges (k>1) or reduces (0<k<1) a figure from a center, producing a similar image with lengths ×k. Similar triangles from shadows or mirrors let you measure heights indirectly with a proportion.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking a dilation changes the shape's angles.
- Setting up the shadow proportion inconsistently.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `di-we1` — A triangle is dilated from the origin by scale factor $2$. A side of length $5$ becomes —
- `di-we2` — A $6$-ft person casts a $4$-ft shadow; a nearby tree casts a $20$-ft shadow. Find the tree's height $h$.

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
| size | **хэмжээ** | ministry standard |
| scale | **томсгох** | already on the site |
| measure | **хэмжих** | ministry standard |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| square | **квадрат** | ministry standard |
| perimeter | **периметр** | already on the site |
| proportion | **пропорц** | already on the site |
| root | **язгуур** | ministry standard |
| side | **тал** | ministry standard |
| height | **өндөр** | already on the site |
| length | **урт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

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
## ratio-proportion-scale-factor

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED rp-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY rp-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## similar-polygons

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED sp-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY sp-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`rp-we1` and so on) exactly
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

