# MN authoring brief — Laws of Sines & Cosines

**Topic** `trigonometry/laws-of-sines-and-cosines` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `trigonometry/laws-of-sines-and-cosines`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `area-of-any-triangle`

**Able to:** Compute triangle areas with Area = ½ab·sin C, including obtuse included angles.

**The idea that carries it:** Area = ½ab·sin C — two sides and the INCLUDED angle; the height h = a sin C is computed, not measured, and obtuse wedges work because supplements share sines.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using an angle that is NOT between the two sides.
- Halving twice — writing ¼ab sin C 'because triangles are half.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig61-we1` — Two sides of a triangle are $6$ and $8$, meeting at $60°$. Find the area exactly.
- `trig61-we2` — Sides $5$ and $8$ meet at $150°$. Find the area exactly, and compare with the same sides at $30°$.

**2 try-it problems**, same freedom and same condition.

### 2. `the-law-of-sines`

**Able to:** Use a/sin A = b/sin B = c/sin C to find missing sides and angles when a side-opposite-angle pair is known.

**The idea that carries it:** Side over sine-of-opposite-angle is one shared constant; a known pair unlocks the triangle — and bigger angles must face longer sides.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Pairing a side with a NON-opposite angle in the proportion.
- Hunting for a law-of-sines setup when no side-opposite-angle pair exists.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig62-we1` — In triangle $ABC$: $\angle A = 30°$, $\angle B = 45°$, and $a = 10$ (opposite $A$). Find $b$ exactly.
- `trig62-we2` — In triangle $ABC$: $\angle A = 60°$, $\angle B = 45°$, $b = 6$. Find $a$ and the third angle.

**2 try-it problems**, same freedom and same condition.

### 3. `the-law-of-cosines`

**Able to:** Apply c² = a² + b² − 2ab cos C to find the third side (SAS) or any angle (SSS).

**The idea that carries it:** c² = a² + b² − 2ab cos C: Pythagoras with a tilt correction — SAS gives the third side, SSS (rearranged) gives any angle, and the cosine's sign classifies it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Pairing the formula's c with a side ADJACENT to the angle.
- Sign slips with obtuse angles: treating −2ab cos 120° as a subtraction.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig63-we1` — Sides $5$ and $8$ meet at $60°$. Find the third side exactly.
- `trig63-we2` — A triangle has sides $5$, $7$, $8$. Find the angle opposite the side of length $7$, exactly.

**2 try-it problems**, same freedom and same condition.

### 4. `solving-any-triangle`

**Able to:** Choose the right law from the given facts and fully solve triangles, including area as a finishing step.

**The idea that carries it:** Inventory the three givens: pair ⟹ Sines; SAS/SSS ⟹ Cosines; and audit with angle-sum, side-order, and two-way area checks.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Starting the Law of Sines from SAS givens.
- Grinding all three angles with the Law of Cosines when two are already known.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `trig64-we1` — Solve the triangle with $a = 5$, $b = 8$, included angle $C = 60°$ — all sides, all angles, and the area.
- `trig64-we2` — A surveyor stands at $P$; a river's far-bank landmarks $Q$ and $R$ are sighted with $\angle QPR = 30°$... simpler classic: from two points $A$ and $B$

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
| area | **талбай** | ministry standard |
| angle | **өнцөг** | ministry standard |
| sine | **синус** | ministry standard |
| cosine | **косинус** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| formula | **томьёо** | ministry standard |
| table | **хүснэгт** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| side | **тал** | ministry standard |
| height | **өндөр** | already on the site |
| pair | **хос** | ministry standard |
| constant | **тогтмол** | ministry standard |
| face | **нүүр** | already on the site |

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
## area-of-any-triangle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig61-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig61-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-law-of-sines

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED trig62-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY trig62-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`trig61-we1` and so on) exactly
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

