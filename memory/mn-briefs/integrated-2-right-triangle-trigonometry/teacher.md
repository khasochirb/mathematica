# MN authoring brief — Right-Triangle Trigonometry

**Topic** `integrated-2/right-triangle-trigonometry` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/right-triangle-trigonometry`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-trigonometric-ratios`

**Able to:** Define sine, cosine and tangent as side ratios, explain why they depend only on the angle, and compute them from a labelled right triangle.

**The idea that carries it:** For a right triangle the three side ratios depend only on the acute angle, because any two such triangles are similar by AA.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Keeping 'opposite' and 'adjacent' fixed when switching angles.
- Accepting a sine or cosine greater than $1$.
- Treating a percentage gradient as an angle in degrees.
- Using the tangent when the given distance is along the slope.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u6-l1-we1` — A right triangle has legs $3$ and $4$ and hypotenuse $5$. Let $\theta$ be the angle opposite the side of length $3$. Find $\sin\theta$, $\cos\theta$ a
- `im2-u6-l1-we2` — Two right triangles share an acute angle $\theta$. The first has opposite $6$ and hypotenuse $10$; the second has opposite $9$. Find the second triang
- `im2-u6-l1-we3` — In a right triangle, $\sin\theta = \frac{7}{25}$. Find $\cos\theta$ and $\tan\theta$ exactly, without a calculator.
- `im2-u6-l1-we4` — A road sign says the gradient is $12\%$. Express this as a tangent, find the angle to the nearest degree, and find how much height is gained over $500

**2 try-it problems**, same freedom and same condition.

### 2. `special-right-triangles`

**Able to:** Derive the side ratios of the $45$-$45$-$90$ and $30$-$60$-$90$ triangles and use them to write exact trigonometric values.

**The idea that carries it:** Half a square gives $1 : 1 : \sqrt{2}$ and half an equilateral triangle gives $1 : \sqrt{3} : 2$ — every exact trigonometric value at $30°$, $45°$ and $60°$ comes from those two pictures.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Putting the $\sqrt{3}$ opposite the $30°$ angle.
- Multiplying the hypotenuse by $\sqrt{2}$ in a 45-45-90 triangle.
- Rounding to decimals mid-problem.
- Assuming the given side is always the shortest one.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u6-l2-we1` — Derive the $45$-$45$-$90$ ratio from a square, then find the hypotenuse of such a triangle whose legs are $7$.
- `im2-u6-l2-we2` — Derive the $30$-$60$-$90$ ratio from an equilateral triangle, and write the exact values of $\sin 30°$, $\cos 30°$ and $\tan 60°$.
- `im2-u6-l2-we3` — A $30$-$60$-$90$ triangle has its shorter leg equal to $9$. Find the other two sides. Then a second such triangle has HYPOTENUSE $9$; find its sides.
- `im2-u6-l2-we4` — A ladder leans against a wall at $60°$ to the ground, reaching $4.5$ m up the wall. Find the ladder's length and how far its foot is from the wall, ex

**2 try-it problems**, same freedom and same condition.

### 3. `complements-and-inverse-ratios`

**Able to:** Explain and use $\sin\theta = \cos(90° - \theta)$, and use inverse trigonometric functions to find an angle from a ratio.

**The idea that carries it:** The sine of an angle is the cosine of its complement, because one angle's opposite side is the other's adjacent side; and inverse functions run the ratios backwards to recover the angle.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $\sin^{-1}(x)$ as $\frac{1}{\sin x}$.
- Computing a third side when the inverse ratio would use the two you have.
- Writing $\sin\theta = \cos\theta$ instead of $\cos(90° - \theta)$.
- Using the distance along the ground as the hypotenuse in an elevation problem.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u6-l3-we1` — In a right triangle the legs are $5$ and $12$. Find both acute angles to one decimal place, and verify they are complementary.
- `im2-u6-l3-we2` — Explain why $\sin 35° = \cos 55°$, without computing either, and use the relationship to solve $\sin(2x) = \cos(3x + 10°)$ for an acute $x$.
- `im2-u6-l3-we3` — A $6$ m ladder leans against a wall with its foot $2$ m from the base. Find the angle it makes with the ground, and how high it reaches.
- `im2-u6-l3-we4` — From a point $80$ m from the base of a tower, the angle of elevation to the top is $32°$. From a point further back the elevation is $19°$. Find the t

**2 try-it problems**, same freedom and same condition.

### 4. `solving-right-triangles`

**Able to:** Solve a right triangle completely from two given parts, and translate elevation, depression and bearing problems into triangles.

**The idea that carries it:** Sketch the triangle, label opposite and adjacent relative to the angle you want, pick the ratio that uses two known parts, and round only at the end.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Measuring the angle of depression from the vertical.
- Using the full span instead of half in a roof-pitch problem.
- Building later answers on earlier rounded ones.
- Reporting more precision than the data supports.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u6-l4-we1` — Solve the right triangle with hypotenuse $20$ and one acute angle $37°$. Give all six parts.
- `im2-u6-l4-we2` — From the top of a $45$ m cliff, the angle of depression to a boat is $23°$. Find the boat's distance from the base of the cliff, and its distance from
- `im2-u6-l4-we3` — A ship sails $30$ km on a bearing of $062°$, then turns and sails on a bearing of $152°$ for $40$ km. How far is it from its starting point, and on wh
- `im2-u6-l4-we4` — A roof has a span of $12$ m and a pitch (the angle between the rafter and the horizontal) of $28°$. Find the ridge height above the wall plate, the ra

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
| tangent | **шүргэгч** | ministry standard |
| half | **хагас** | already on the site |
| translate | **хөрвүүлэх** | already on the site |
| area | **талбай** | ministry standard |
| function | **функц** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| slope | **налалт** | ministry standard |
| square | **квадрат** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| identity | **адилтгал** | ministry standard |
| problem | **бодлого** | ministry standard |
| opposite | **эсрэг** | already on the site |
| side | **тал** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## the-trigonometric-ratios

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u6-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u6-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## special-right-triangles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u6-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u6-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u6-l1-we1` and so on) exactly
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

