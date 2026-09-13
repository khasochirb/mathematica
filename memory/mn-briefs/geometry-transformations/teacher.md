# MN authoring brief — Transformations

**Topic** `geometry/transformations` · **7 lessons** · 15 worked examples · 8 practice · 6 test-yourself

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
> `geometry/transformations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `translations`

**Able to:** Translate a figure by a vector, writing the rule (x, y) → (x + a, y + b), and see that a slide preserves size and shape.

**The idea that carries it:** A translation slides every point by the same vector ⟨a, b⟩: (x, y) → (x + a, y + b). It is a rigid motion, so the image is congruent to the original.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping the two components of the vector.
- Thinking a slide changes the figure's size.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tr-we1` — Translate the point $(2, 3)$ by the vector $\langle 4, 1 \rangle$.
- `tr-we2` — Translate $(5, -2)$ left $3$ and up $6$ — the vector $\langle -3, 6 \rangle$.

**2 try-it problems**, same freedom and same condition.

### 2. `reflections`

**Able to:** Reflect a figure over the x-axis, the y-axis, and the line y = x, using the coordinate rules, and see that a flip is a rigid motion.

**The idea that carries it:** A reflection flips a figure across a line. Over the x-axis (x, y)→(x, −y); over the y-axis (x, y)→(−x, y); over y = x (x, y)→(y, x). It is a rigid motion.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Negating the wrong coordinate.
- Forgetting to swap for y = x.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rf-we1` — Reflect $(4, 3)$ over the x-axis.
- `rf-we2` — Reflect $(4, 3)$ over the line $y = x$.

**2 try-it problems**, same freedom and same condition.

### 3. `rotations`

**Able to:** Rotate a figure 90°, 180°, and 270° about the origin using the coordinate rules, and see that a turn is a rigid motion.

**The idea that carries it:** A rotation about the origin: 90° → (−y, x); 180° → (−x, −y); 270° → (y, −x). It is a rigid motion, so the image is congruent.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to swap x and y for a 90° turn.
- Only flipping one sign for a 180° turn.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ro-we1` — Rotate $(4, 1)$ by $90°$ about the origin.
- `ro-we2` — Rotate $(4, 1)$ by $180°$ about the origin.

**2 try-it problems**, same freedom and same condition.

### 4. `symmetry`

**Able to:** Identify line (reflection) symmetry and rotational symmetry, count lines of symmetry, and give the order of rotational symmetry.

**The idea that carries it:** Line symmetry: a reflection maps the figure onto itself (count the mirror lines). Rotational symmetry: a turn under 360° maps it onto itself; the order is how many matches in a full turn. A regular n-gon has n of each.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Counting a full 360° turn as rotational symmetry.
- Assuming every figure with line symmetry has the same number of lines.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `sy-we1` — How many lines of symmetry does a square have?
- `sy-we2` — What is the order of rotational symmetry of a regular hexagon?

**2 try-it problems**, same freedom and same condition.

### 5. `dilations`

**Able to:** Dilate a figure from the origin by a scale factor k, using (x, y) → (kx, ky), and see that the image is similar (not congruent) unless k = 1.

**The idea that carries it:** A dilation from the origin multiplies both coordinates by the scale factor k: (x, y) → (kx, ky). k > 1 enlarges, 0 < k < 1 reduces. The image is similar to the original (angles kept, lengths ×k).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding the scale factor instead of multiplying.
- Calling the image congruent.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `di-we1` — Dilate $(3, 2)$ from the origin by scale factor $k = 2$.
- `di-we2` — Dilate $(8, 4)$ from the origin by $k = \tfrac12$.

**2 try-it problems**, same freedom and same condition.

### 6. `compositions`

**Able to:** Apply a composition of two transformations in order, and connect rigid motions to congruence and dilations to similarity.

**The idea that carries it:** A composition does one transformation then another (order matters). Rigid motions compose to a rigid motion → the figures are congruent. Allowing a dilation too → the figures are similar.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doing the transformations in the wrong order.
- Calling figures related by a dilation 'congruent'.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cm-we1` — Translate $(2, 3)$ by $\langle 1, 1 \rangle$, then reflect the result over the x-axis. Final image?
- `cm-we2` — Reflect $(4, 1)$ over the y-axis, then rotate $180°$ about the origin. Final image?

**2 try-it problems**, same freedom and same condition.

### 7. `transformation-matrices`

**Able to:** Apply a 2×2 matrix to a point, recognize the standard rotation/reflection/scaling matrices, and use the determinant as the area scale factor.

**The idea that carries it:** Matrix × column point = image; columns are the images of (1,0) and (0,1); |det| = the area scale factor.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying rows by rows.
- Reading det = −1 as 'area shrinks'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tmx-we1` — Apply $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ to the point $(3, 1)$ and name the transformation.
- `tmx-we2` — Which matrix reflects the plane over the line $y = x$? Apply it to $(5, -2)$.
- `tmx-we3` — The matrix $\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$ is applied to a figure of area $5$. Find the image's area.

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
| count | **тоолох** | ministry standard |
| size | **хэмжээ** | ministry standard |
| scale | **томсгох** | already on the site |
| translate | **хөрвүүлэх** | already on the site |
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| point | **цэг** | ministry standard |
| coordinate | **координат** | ministry standard |
| length | **урт** | ministry standard |
| column | **багана** | already on the site |
| origin | **координатын эх** | ministry standard |
| a line | **шулуун** | ministry standard |
| reflect | **тэгш хэмээр хувиргах** | ministry standard |
| reflection | **тэгш хэмээр хувиргах** | ministry standard |
| vector | **вектор** | ministry standard |
| motion | **хөдөлгөөн** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

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
## translations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED tr-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY tr-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## reflections

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED rf-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY rf-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`tr-we1` and so on) exactly
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

