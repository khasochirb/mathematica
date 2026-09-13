# MN authoring brief — Solving Linear Equations

**Topic** `algebra-1/linear-equations` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/linear-equations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `one-and-two-step-equations`

**Able to:** Solve one- and two-step linear equations by inverse operations, and check solutions by substitution.

**The idea that carries it:** Equations are balanced scales: undo operations on both sides, in reverse order, until the variable stands alone — then substitute to check.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doing the operation to one side only: $4x - 9 = 19 \to 4x = 19$.
- Dividing before subtracting: $3x + 5 = 20 \to x + 5 = \frac{20}{3}$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al21-we1` — Solve $4x - 9 = 19$.
- `al21-we2` — Solve $\dfrac{x}{5} + 3 = -1$.

**2 try-it problems**, same freedom and same condition.

### 2. `variables-on-both-sides`

**Able to:** Solve equations with variables on both sides, including ones that need distributing first.

**The idea that carries it:** Distribute and tidy each side, then herd the variable terms to one side and constants to the other — two balance moves and a division finish it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Subtracting a variable term from one side only.
- Distributing after moving terms, and losing a term in the shuffle.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al22-we1` — Solve $7x - 6 = 3x + 14$.
- `al22-we2` — Solve $3(2x - 4) = 5x + 1$.

**2 try-it problems**, same freedom and same condition.

### 3. `fractions-decimals-and-special-cases`

**Able to:** Clear fractions and decimals before solving, and recognize equations with no solution or infinitely many solutions.

**The idea that carries it:** Multiply through by the LCD (or a power of 10) to clear fractions and decimals; if the variable cancels, a false leftover means no solution and a true one means all numbers.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying only the fraction terms by the LCD: $\frac{x}{2} + \frac{x}{3} = 5 \to 3x + 2x = 5$.
- Treating '$8 = 8$' as a mistake and forcing $x = 0$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al23-we1` — Solve $\dfrac{x}{2} + \dfrac{x}{3} = 5$.
- `al23-we2` — Solve $2(3x + 4) = 6x + 8$ and $2(3x + 4) = 6x + 5$.

**2 try-it problems**, same freedom and same condition.

### 4. `literal-equations-and-formulas`

**Able to:** Rearrange formulas and literal equations to isolate a chosen variable, treating all other letters as constants.

**The idea that carries it:** Solve for a letter by treating the other letters as numbers — the same inverse-operation moves produce a reusable formula instead of a single answer.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Subtracting a term that's multiplied: solving $d = rt$ for $t$ by computing $t = d - r$.
- Dividing only one term: $P - 2l = 2w \to w = P - \frac{2l}{2}$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al24-we1` — Solve $P = 2l + 2w$ for $w$, then find $w$ when $P = 36$ and $l = 10$.
- `al24-we2` — Solve $C = \dfrac{5}{9}(F - 32)$ for $F$, then convert $C = 25°$.

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
| scale | **томсгох** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| fraction | **бутархай** | ministry standard |
| division | **хуваалт** | ministry standard |
| number | **тоо** | ministry standard |
| formula | **томьёо** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| algebra | **алгебр** | ministry standard |
| linear | **шугаман** | ministry standard |
| side | **тал** | ministry standard |
| answer | **хариулт** | already on the site |
| multiply | **үржүүлэх** | ministry standard |
| divide | **хуваах** | ministry standard |
| constant | **тогтмол** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## one-and-two-step-equations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al21-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al21-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## variables-on-both-sides

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al22-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al22-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al21-we1` and so on) exactly
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

---

## Who arrives here

The site sends students to this topic when the analytics find a weakness in:

- **Шугаман тэгшитгэл (8-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

