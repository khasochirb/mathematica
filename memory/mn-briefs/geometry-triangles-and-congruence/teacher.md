# MN authoring brief — Triangles & Congruence

**Topic** `geometry/triangles-and-congruence` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/triangles-and-congruence`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `triangles-and-their-angles`

**Able to:** Classify triangles by sides and by angles, and use the Triangle Angle-Sum Theorem (the three interior angles total 180°) — which follows from the parallel-line facts of Unit 3.

**The idea that carries it:** Every triangle's three angles total 180°. Classify by sides (scalene/isosceles/equilateral) and by angles (acute/right/obtuse).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking a triangle can have two right angles.
- Confusing the two ways to classify.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ta-we1` — Two angles of a triangle are $50^\circ$ and $60^\circ$. Find the third.
- `ta-we2` — A triangle has angles $90^\circ$, $55^\circ$, and $35^\circ$. Classify it by angles.

**2 try-it problems**, same freedom and same condition.

### 2. `exterior-angle-theorem`

**Able to:** Use the Exterior Angle Theorem: an exterior angle of a triangle equals the sum of its two remote interior angles.

**The idea that carries it:** An exterior angle of a triangle = the sum of the two remote (non-adjacent) interior angles.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding the adjacent interior angle instead of the remote ones.
- Forgetting the exterior + adjacent interior = 180°.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ea-we1` — A triangle's two remote interior angles are $50^\circ$ and $70^\circ$. Find the exterior angle at the third vertex.
- `ea-we2` — An exterior angle is $125^\circ$; one remote interior angle is $60^\circ$. Find the other remote interior angle.

**2 try-it problems**, same freedom and same condition.

### 3. `triangle-inequality`

**Able to:** Use the Triangle Inequality to decide whether three lengths can form a triangle, and find the range of a missing side.

**The idea that carries it:** Two sides always beat the third. Three lengths form a triangle iff the two shorter sum to more than the longest; a missing side lies between |a−b| and a+b.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Checking only one pair of sides.
- Allowing the sum to equal the third side.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ti-we1` — Can sides $5$, $6$, and $9$ form a triangle?
- `ti-we2` — Can sides $3$, $4$, and $8$ form a triangle?

**2 try-it problems**, same freedom and same condition.

### 4. `congruence-sss-sas`

**Able to:** Understand congruent triangles as having all corresponding parts equal, and use the SSS and SAS shortcuts to prove two triangles congruent.

**The idea that carries it:** Congruent = all corresponding parts equal. SSS (three sides) and SAS (two sides + the angle BETWEEN them) each guarantee congruence.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using SAS when the angle isn't between the two sides.
- Listing congruent vertices in the wrong order.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ss-we1` — $\triangle ABC$ and $\triangle DEF$ have $AB = DE$, $BC = EF$, $CA = FD$. Are they congruent, and by what?
- `ss-we2` — Two triangles have two pairs of equal sides with the equal angle between those sides. Which shortcut applies?

**2 try-it problems**, same freedom and same condition.

### 5. `congruence-asa-aas-hl`

**Able to:** Use ASA, AAS, and the right-triangle shortcut HL to prove triangles congruent, and know why AAA and SSA do not.

**The idea that carries it:** ASA (angles + included side), AAS (angles + any side), HL (right triangles: hypotenuse + leg) all work. AAA and SSA do NOT.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Believing AAA proves congruence.
- Using SSA.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `aa-we1` — Two triangles share two pairs of equal angles and the side between those angles. Which shortcut?
- `aa-we2` — Two right triangles have equal hypotenuses and one equal leg. Which shortcut?

**2 try-it problems**, same freedom and same condition.

### 6. `cpctc-and-isosceles`

**Able to:** Use CPCTC to conclude corresponding parts are equal after proving triangles congruent, and apply the Isosceles Triangle Theorem (base angles congruent) and its converse.

**The idea that carries it:** CPCTC: after proving triangles congruent, all corresponding parts are equal. Isosceles triangles have congruent base angles (and the converse holds).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using CPCTC before proving the triangles congruent.
- Assuming ALL angles of an isosceles triangle are equal.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ci-we1` — An isosceles triangle has a vertex angle of $40^\circ$. Find each base angle.
- `ci-we2` — In an isosceles triangle a base angle is $50^\circ$. Find the vertex angle.

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
| base | **суурь** | ministry standard |
| angle | **өнцөг** | ministry standard |
| line | **шулуун** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| parallel | **параллель** | ministry standard |
| right triangle | **тэгш өнцөгт гурвалжин** | already on the site |
| unit | **нэгж** | ministry standard |
| inequality | **тэнцэтгэл биш** | ministry standard |
| form | **хэлбэр** | ministry standard |
| side | **тал** | ministry standard |
| interior | **дотоод** | already on the site |
| part | **хэсэг** | ministry standard |
| length | **урт** | ministry standard |
| total | **нийт** | already on the site |
| equal | **тэнцүү** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

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
## triangles-and-their-angles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ta-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ta-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## exterior-angle-theorem

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ea-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ea-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`ta-we1` and so on) exactly
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

