# MN authoring brief — Reasoning & Proof

**Topic** `geometry/reasoning-and-proof` · **6 lessons** · 12 worked examples · 8 practice · 6 test-yourself

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
> `geometry/reasoning-and-proof`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `inductive-reasoning`

**Able to:** Use inductive reasoning to extend patterns and state conjectures — and know that a conjecture is an educated guess, not yet a proven fact.

**The idea that carries it:** Examples → pattern → conjecture. Inductive reasoning suggests rules; it never proves them.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating a conjecture as a proven fact.
- Extending a pattern from too few terms.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ir-we1` — Find the next term: $5, 9, 13, 17, \ldots$
- `ir-we2` — Compute $1+3+5$ and $1+3+5+7$. What conjecture does the pattern suggest?

**2 try-it problems**, same freedom and same condition.

### 2. `counterexamples`

**Able to:** Disprove a false conjecture by producing a counterexample — one case that fits the conjecture's conditions but breaks its conclusion.

**The idea that carries it:** One case that fits the if-part but breaks the then-part kills a conjecture. Disproving takes one; proving takes all.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Thinking you need several counterexamples.
- Offering a counterexample that doesn't fit the conditions.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ce-we1` — Disprove: “Every number divisible by $2$ is divisible by $4$.”
- `ce-we2` — Disprove: “Every odd number greater than $1$ is prime.”

**2 try-it problems**, same freedom and same condition.

### 3. `deductive-reasoning`

**Able to:** Use deductive reasoning to draw guaranteed conclusions from given facts and rules, and tell deductive from inductive reasoning.

**The idea that carries it:** Rules + facts → forced conclusions. Inductive suggests; deductive guarantees.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Mixing up which reasoning is which.
- Applying a rule to a case it doesn't cover.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `de-we1` — Rule: every multiple of $6$ is a multiple of $3$. Fact: $48$ is a multiple of $6$. Conclusion?
- `de-we2` — Chain: multiples of $8$ are multiples of $4$; multiples of $4$ are even. What follows about $40$?

**2 try-it problems**, same freedom and same condition.

### 4. `if-then-statements`

**Able to:** Identify the hypothesis and conclusion of a conditional statement, write its converse, and judge each with truth values and counterexamples.

**The idea that carries it:** If hypothesis, then conclusion. The converse swaps them — and needs its own verdict.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Assuming the converse of a true statement is true.
- Reading a conditional backwards.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `it-we1` — Identify the hypothesis and conclusion: “If a number is a multiple of $4$, then it is even.”
- `it-we2` — Write the converse and judge it: “If a number is a multiple of $4$, then it is even.”

**2 try-it problems**, same freedom and same condition.

### 5. `algebraic-proof`

**Able to:** Justify each step of solving an equation with a named property of equality, turning algebra into two-column proof.

**The idea that carries it:** Every algebra move has a legal name. Naming each move turns a solution into a proof.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Skipping steps in a proof because “it's obvious.”
- Naming the wrong property.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `alg-we1` — Solve $2x + 3 = 11$, naming each step's property.
- `alg-we2` — Solve $4(x + 2) = 28$, naming each property.

**2 try-it problems**, same freedom and same condition.

### 6. `geometric-proofs`

**Able to:** Read and complete two-column geometric proofs — including a full proof that vertical angles are congruent.

**The idea that carries it:** Theorem = proven. Chain definitions, postulates, and equality properties until the claim is forced.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Citing the claim you're proving as its own reason.
- Leaving out the postulate that justifies an equation.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `gp-we1` — $B$ is between $A$ and $C$; $AB = 5$, $AC = 12$. Prove $BC = 7$.
- `gp-we2` — Two lines cross, so $\angle 1$ and $\angle 2$ form a linear pair, as do $\angle 2$ and $\angle 3$. If $m\angle 1 = 115^\circ$, find $m\angle 3$ — with

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
| equation | **тэгшитгэл** | ministry standard |
| angle | **өнцөг** | ministry standard |
| proof | **баталгаа** | already on the site |
| substitution | **орлуулга** | ministry standard |
| vertical | **босоо** | ministry standard |
| algebra | **алгебр** | ministry standard |
| part | **хэсэг** | ministry standard |
| column | **багана** | already on the site |
| pattern | **хэв маяг** | already on the site |
| chain | **давхар функцийн уламжлалын дүрэм** | **proposed — tell us if it is wrong** |
| definition | **тодорхойлолт** | ministry standard |
| converse | **урвуу теорем** | **proposed — tell us if it is wrong** |
| including | **оролцуулан** | already on the site |
| naming | **нэрлэх** | already on the site |

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
## inductive-reasoning

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ir-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ir-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## counterexamples

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ce-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ce-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`ir-we1` and so on) exactly
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

