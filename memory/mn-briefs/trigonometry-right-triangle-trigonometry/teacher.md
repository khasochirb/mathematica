# MN authoring brief — Right-Triangle Trigonometry

**Topic** `trigonometry/right-triangle-trigonometry` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `trigonometry/right-triangle-trigonometry`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-three-ratios`

**Able to:** Name the sides of a right triangle relative to an angle, and compute sine, cosine, and tangent from side lengths.

**The idea that carries it:** Sides are named relative to θ (opposite, adjacent, hypotenuse); SOH-CAH-TOA gives three size-proof ratios that belong to the angle itself.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Fixing 'opposite' and 'adjacent' to the picture instead of the angle.
- Using the hypotenuse in tan, or a leg-over-leg ratio in sin.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig11-we1` — In right triangle $ABC$, the right angle is at $C$, $AC = 4$, $BC = 3$, $AB = 5$. Find $\sin A$, $\cos A$, and $\tan A$.
- `trig11-we2` — A right triangle has legs $5$ and $12$. Find the hypotenuse, then all three ratios of the angle $\theta$ opposite the side of length $5$.

**2 try-it problems**, same freedom and same condition.

### 2. `finding-missing-sides`

**Able to:** Solve for unknown sides of right triangles using the appropriate trig ratio, multiplying or dividing as the unknown's position demands.

**The idea that carries it:** Name the known and wanted sides, pick the ratio that uses both, then multiply (unknown upstairs) or divide (unknown downstairs).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Always multiplying: x = 6 sin 30° when the equation was sin 30° = 6/x.
- Picking the ratio by habit (always sine) instead of by the two sides in play.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig12-we1` — In right triangle $ABC$ (right angle at $C$), $\angle A = 30°$ and the hypotenuse $AB = 10$. Find $BC$, the side opposite $A$.
- `trig12-we2` — A ladder leans at $60°$ to the ground, and its base sits $3$ m from the wall. How long is the ladder?

**2 try-it problems**, same freedom and same condition.

### 3. `finding-missing-angles`

**Able to:** Find unknown acute angles from two known sides using inverse trigonometric functions.

**The idea that carries it:** Inverse trig answers 'which angle has this ratio?': build the ratio from two known sides, apply arcsin/arccos/arctan — and the acute angles must sum to 90°.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading sin⁻¹ x as 1/sin x and computing a reciprocal.
- Building the ratio upside-down: tan θ = adj/opp.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig13-we1` — Right angle at $C$; the side opposite $A$ is $5$ and the hypotenuse is $10$. Find $\angle A$.
- `trig13-we2` — A ramp rises $3$ m over a horizontal run of $4$ m. Find its angle of incline to the nearest degree.

**2 try-it problems**, same freedom and same condition.

### 4. `elevation-and-depression`

**Able to:** Translate elevation/depression descriptions into right triangles and solve them for heights and distances.

**The idea that carries it:** Elevation and depression are tilts from the HORIZONTAL; draw the horizontal, complete the right triangle — and depression at the top equals elevation at the bottom (alternate interior angles).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the angle of depression from the cliff face or tower instead of the horizontal.
- Placing the depression angle inside the triangle at the top vertex without the swap.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig14-we1` — From a point $30$ m from a tower's base, the angle of elevation of the top is $60°$. Find the tower's height exactly.
- `trig14-we2` — From the top of a $40$ m cliff, a boat is seen at an angle of depression of $30°$. How far is the boat from the cliff's base, exactly?

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
| size | **хэмжээ** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| proof | **баталгаа** | already on the site |
| distance | **зай** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| opposite | **эсрэг** | already on the site |
| side | **тал** | ministry standard |
| height | **өндөр** | already on the site |
| interior | **дотоод** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

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
## the-three-ratios

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig11-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig11-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## finding-missing-sides

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig12-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig12-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`trig11-we1` and so on) exactly
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

