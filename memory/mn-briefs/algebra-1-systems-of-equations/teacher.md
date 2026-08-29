# MN authoring brief — Systems of Equations

**Topic** `algebra-1/systems-of-equations` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/systems-of-equations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `solving-by-graphing`

**Able to:** Understand a system's solution as the intersection point, solve simple systems by graphing, and verify by substituting into both equations.

**The idea that carries it:** A system's solution is the point on BOTH graphs — find it as the intersection, then confirm it in both equations.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Accepting a point after checking only one equation.
- Reporting the intersection as two answers ('x = 2 and y = 3' as separate facts about different problems).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al61-we1` — Solve by graphing: $y = x + 1$ and $y = -x + 5$.
- `al61-we2` — Is $(4, -1)$ a solution of the system $x + 2y = 2$ and $3x - y = 10$?

**2 try-it problems**, same freedom and same condition.

### 2. `substitution`

**Able to:** Solve systems by substitution: isolate, substitute with parentheses, solve, back-substitute, and check.

**The idea that carries it:** Isolate one variable, substitute it (in parentheses) into the other equation, solve the collapsed equation, then back-substitute — and check the pair in both originals.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Substituting without parentheses: $3x - 2x - 1$ for $3x - y$ with $y = 2x - 1$.
- Substituting back into the SAME equation you isolated from.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al62-we1` — Solve: $y = 2x - 1$ and $3x + y = 14$.
- `al62-we2` — Solve: $x + 4y = 11$ and $2x - 3y = 0$.

**2 try-it problems**, same freedom and same condition.

### 3. `elimination`

**Able to:** Solve systems by adding or subtracting equations, scaling first when needed, and choose sensibly between substitution and elimination.

**The idea that carries it:** Add or subtract scaled equations so one variable cancels; equal coefficients subtract, opposite coefficients add.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding when coefficients MATCH: $3x + \ldots$ plus $3x + \ldots$ gives $6x$, not zero.
- Scaling only the variable terms: $2x + 3y = 12$ times 2 as '$4x + 6y = 12$'.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al63-we1` — Solve: $3x + 2y = 16$ and $5x - 2y = 8$.
- `al63-we2` — Solve: $2x + 3y = 12$ and $3x - 2y = 5$.

**2 try-it problems**, same freedom and same condition.

### 4. `applications-and-special-systems`

**Able to:** Model word problems as systems (totals, values, break-even), solve them, and interpret no-solution and infinitely-many outcomes in context.

**The idea that carries it:** One equation per fact (count + value is the classic pair), then solve; a false leftover means contradictory demands, a true one means the two facts weren't independent.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing both equations about counts (or both about money).
- Answering a break-even question with just 'x = 2000' and stopping.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al64-we1` — A kiosk sold 12 drinks — colas at \$3 and juices at \$5 — for \$46 total. How many of each?
- `al64-we2` — Printer A costs \$120 plus \$0.05 per page; printer B costs \$60 plus \$0.08 per page. At how many pages do total costs break even?

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
| scale | **томсгох** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| system | **систем** | ministry standard |
| even | **тэгш** | ministry standard |
| substitution | **орлуулга** | ministry standard |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |
| problem | **бодлого** | ministry standard |
| opposite | **эсрэг** | already on the site |
| model | **загвар** | ministry standard |
| infinite | **төгсгөлгүй** | ministry standard |
| subtracting | **хасах** | ministry standard |
| total | **нийт** | already on the site |
| pair | **хос** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## solving-by-graphing

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al61-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al61-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## substitution

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al62-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al62-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al61-we1` and so on) exactly
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

