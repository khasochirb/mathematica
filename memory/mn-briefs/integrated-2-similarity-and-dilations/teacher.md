# MN authoring brief — Similarity & Dilations

**Topic** `integrated-2/similarity-and-dilations` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/similarity-and-dilations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `dilations`

**Able to:** Perform a dilation given a centre and a scale factor, describe its effect on lengths, angles and area, and find the scale factor from a pair of figures.

**The idea that carries it:** A dilation multiplies every distance from the centre by $k$, leaves every angle unchanged, and multiplies area by $k^{2}$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dilating about a non-origin centre by multiplying the coordinates directly.
- Scaling area by $k$ instead of $k^{2}$.
- Believing a dilation changes the angles.
- Computing the scale factor as original over image.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u5-l1-we1` — Triangle $ABC$ has vertices $A(2, 1)$, $B(6, 1)$ and $C(2, 4)$. Dilate it about the origin with scale factor $3$ and compare the two triangles.
- `im2-u5-l1-we2` — Dilate the point $P(7, 5)$ about the centre $C(1, 2)$ with scale factor $\frac{1}{3}$.
- `im2-u5-l1-we3` — A rectangle measures $8$ cm by $5$ cm. After a dilation it measures $20$ cm by $12.5$ cm. Find the scale factor and the ratio of the areas.
- `im2-u5-l1-we4` — A dilation about the origin with scale factor $-2$ is applied to $A(3, 1)$ and $B(5, 4)$. Find the images and describe the effect geometrically.

**2 try-it problems**, same freedom and same condition.

### 2. `similarity-and-aa`

**Able to:** Define similarity by transformations, write similarity statements with correct correspondence, apply the AA criterion, and find missing lengths in similar figures.

**The idea that carries it:** Similar means related by dilations and rigid motions; for triangles, two equal angle pairs are enough to guarantee it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the similarity statement with the letters in any order.
- Adding a scale factor to a length instead of multiplying.
- Using AA to claim congruence.
- Scaling perimeter by $k^2$.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u5-l2-we1` — In $\triangle ABC$, $\angle A = 50°$ and $\angle B = 60°$. In $\triangle DEF$, $\angle D = 50°$ and $\angle F = 70°$. Are they similar? Write the simi
- `im2-u5-l2-we2` — $\triangle PQR \sim \triangle STU$ with $PQ = 8$, $QR = 12$, $PR = 10$ and $ST = 20$. Find $TU$ and $SU$, and the ratio of the areas.
- `im2-u5-l2-we3` — A $1.8$ m person casts a $2.4$ m shadow at the same moment a flagpole casts a $14$ m shadow. Find the height of the flagpole.
- `im2-u5-l2-we4` — In the figure, $\angle BAC = \angle EDC$ and points $B$, $C$, $E$ are collinear with $A$ and $D$ on opposite sides of that line. Given $AC = 6$, $CD =

**2 try-it problems**, same freedom and same condition.

### 3. `side-splitter-and-midsegment`

**Able to:** Prove and apply the side-splitter theorem and the triangle midsegment theorem, and use similarity to prove the Pythagorean theorem.

**The idea that carries it:** A line parallel to a side creates a similar triangle, and every proportion in this lesson is that similarity written down.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Mixing the two forms of the side-splitter ratio.
- Thinking the midsegment triangle has half the area.
- Assuming any line across a triangle splits the sides proportionally.
- In the altitude relations, pairing a leg with the wrong hypotenuse piece.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u5-l3-we1` — In $\triangle ABC$, $D$ lies on $AB$ and $E$ on $AC$ with $DE \parallel BC$. Given $AD = 6$, $DB = 4$ and $AE = 9$, find $EC$ and $AC$.
- `im2-u5-l3-we2` — Prove the side-splitter theorem: if $DE \parallel BC$ with $D$ on $AB$ and $E$ on $AC$, then $\frac{AD}{AB} = \frac{AE}{AC}$.
- `im2-u5-l3-we3` — In $\triangle ABC$, $M$ is the midpoint of $AB$ and $N$ is the midpoint of $AC$. Given $BC = 14$, find $MN$ and justify that $MN \parallel BC$.
- `im2-u5-l3-we4` — In right triangle $ABC$ with the right angle at $C$, the altitude from $C$ meets the hypotenuse at $H$, splitting it into $AH = p$ and $HB = q$. Use s

**2 try-it problems**, same freedom and same condition.

### 4. `applying-similarity`

**Able to:** Use similarity to solve indirect-measurement problems, work with scale drawings, and write short proofs that rely on similar triangles.

**The idea that carries it:** Build a measurable triangle similar to the one you cannot reach, state the correspondence, then let the proportion carry the answer across.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling a map area by the scale ratio instead of its square.
- Pairing a height with a base in the proportion.
- Scaling perimeter by $k^2$ or area by $k$.
- Not checking the answer for physical sense.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u5-l4-we1` — A mirror is placed on level ground $12$ m from the base of a building. A person whose eyes are $1.6$ m above the ground stands $2$ m from the mirror o
- `im2-u5-l4-we2` — A map has scale $1 : 25\,000$. Two towns are $8.4$ cm apart on the map, and a forest covers $6$ cm² of it. Find the real distance in kilometres and th
- `im2-u5-l4-we3` — To find the width of a river, a surveyor marks a point $A$ directly across from a tree $T$ on the far bank, walks $30$ m along the bank to $B$, then a
- `im2-u5-l4-we4` — Two similar triangular gardens have perimeters $24$ m and $36$ m. The smaller has area $30$ m². Find the area of the larger, and the length of the sid

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
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| mean | **дундаж** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| line | **шулуун** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| proof | **баталгаа** | already on the site |
| distance | **зай** | ministry standard |
| centre | **төв** | ministry standard |
| perimeter | **периметр** | already on the site |
| proportion | **пропорц** | already on the site |
| problem | **бодлого** | ministry standard |
| side | **тал** | ministry standard |

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
## dilations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u5-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u5-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## similarity-and-aa

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u5-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u5-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u5-l1-we1` and so on) exactly
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

