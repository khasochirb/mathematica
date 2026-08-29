# MN authoring brief — Conditional Probability & Independence

**Topic** `prob-stats/conditional-probability` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/conditional-probability`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `shrinking-the-universe`

**Able to:** Compute conditional probabilities P(A|B) by restricting the sample space, from counts and from two-way tables.

**The idea that carries it:** P(A|B) = P(A and B)/P(B): the given event becomes the new universe; A's chance is its share of it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the original universe's denominator after conditioning.
- Swapping P(A|B) for P(B|A).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cd-l1-w1` — Two dice are rolled; you learn the sum is $8$. Find $P(\text{both dice show } 4 \mid \text{sum} = 8)$.
- `cd-l1-w2` — From the Unit 5 survey ($100$ students: bike-only $35$, both $25$, skateboard-only $20$, neither $20$): find $P(\text{skateboard} \mid \text{bike})$.
- `cd-l1-w3` — Same survey: find $P(\text{bike} \mid \text{skateboard})$, and compare with the previous answer.

**2 try-it problems**, same freedom and same condition.

### 2. `the-multiplication-rule`

**Able to:** Compute joint probabilities with P(A and B) = P(A)·P(B|A), and organize multi-stage experiments as weighted trees.

**The idea that carries it:** P(A and B) = P(A) · P(B|A): multiply along tree branches, each weighted by what's already happened; leaves sum to 1.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Freezing the bag after the first draw.
- Adding branch probabilities along a path.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cd-l2-w1` — A bag holds $3$ red and $2$ blue marbles; two are drawn without replacement. Find $P(\text{both red})$.
- `cd-l2-w2` — Same bag, same draw. Build all four leaves of the tree and verify they sum to $1$.
- `cd-l2-w3` — Three cards are drawn from a deck without replacement. Find $P(\text{all three are hearts})$.

**2 try-it problems**, same freedom and same condition.

### 3. `independence`

**Able to:** Define independence via P(A|B) = P(A), test it numerically, and multiply plain probabilities only when it holds.

**The idea that carries it:** Independent means P(A|B) = P(A) — equivalently P(A and B) = P(A)P(B); check it, don't assume it, and never confuse it with mutually exclusive.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying plain probabilities for dependent events.
- Calling mutually exclusive events independent.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cd-l3-w1` — A coin is flipped and a die is rolled. Find $P(\text{heads and a } 6)$, justifying the shortcut.
- `cd-l3-w2` — In a class of $36$: $18$ like math, $12$ like art, $6$ like both. Are "likes math" and "likes art" independent?
- `cd-l3-w3` — A machine has three independent safety sensors, each failing with probability $0.1$. Find $P(\text{at least one sensor works})$.

**2 try-it problems**, same freedom and same condition.

### 4. `total-probability`

**Able to:** Compute total probabilities by multiplying along each branch of a scenario tree and adding across the branches.

**The idea that carries it:** P(A) = Σ P(scenario) · P(A | scenario) — multiply along branches, add across them; the answer is a weighted average of the conditionals.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the conditionals without weights.
- Scenarios that don't partition.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cd-l4-w1` — The old bus runs $70\%$ of mornings (late $10\%$ of the time); the new bus runs $30\%$ (late $2\%$). Find $P(\text{late})$.
- `cd-l4-w2` — Factory line A makes $60\%$ of output with $3\%$ defects; line B makes $40\%$ with $8\%$ defects. What fraction of all output is defective?
- `cd-l4-w3` — A student guesses on $30\%$ of quiz questions (correct $25\%$ of the time when guessing) and knows the rest (correct $95\%$ of the time). What's the o

**2 try-it problems**, same freedom and same condition.

### 5. `bayes-by-table`

**Able to:** Reverse conditional probabilities with the natural-frequency table method — from P(evidence|cause) to P(cause|evidence).

**The idea that carries it:** Run 1000 imaginary people through the base rate and the test; P(cause|evidence) = true positives over ALL positives.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting the test's accuracy as your probability of being sick.
- Dividing true positives by the sick count instead of the positive count.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cd-l5-w1` — Disease rate $1\%$; test sensitivity $90\%$ (catches the sick); false-positive rate $9\%$ (flags the healthy). You test positive. Find $P(\text{sick} 
- `cd-l5-w2` — From Lesson 4's inbox: $25\%$ of mail is spam; "free" appears in $60\%$ of spam and $8\%$ of real mail. An email says "free". Find $P(\text{spam} \mid
- `cd-l5-w3` — Two jars: jar A ($3$ red, $1$ blue), jar B ($1$ red, $3$ blue). A fair coin picks the jar; a red marble is drawn. Find $P(\text{jar A} \mid \text{red}

**2 try-it problems**, same freedom and same condition.

### 6. `conditional-reasoning-capstone`

**Able to:** Deploy the full conditional toolkit — trees, tables, independence tests, Bayes — on problems where intuition fails.

**The idea that carries it:** When intuition and the tree disagree, trust the tree — and know WHICH conditional direction a claim states before believing it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating the host's reveal as fresh randomness.
- Accepting any quoted conditional without checking its direction.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cd-l6-w1` — Monty Hall: you pick door 1; the informed host opens an empty door and offers a switch. Compute $P(\text{win} \mid \text{switch})$ by cases.
- `cd-l6-w2` — A DNA profile matches $1$ in a million innocent people. In a city of $10$ million, a suspect matches. Estimate $P(\text{innocent} \mid \text{match})$ 
- `cd-l6-w3` — A basketball player hits $50\%$ of shots. Over many games, someone counts: after a made shot she hits $50\%$; after a miss she hits $50\%$. What do th

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
| base | **суурь** | ministry standard |
| mean | **дундаж** | ministry standard |
| probability | **магадлал** | ministry standard |
| rate | **хурдац** | already on the site |
| multiplication | **үржүүлэх** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| sample | **түүвэр** | already on the site |
| table | **хүснэгт** | ministry standard |
| problem | **бодлого** | ministry standard |
| form | **хэлбэр** | ministry standard |
| total | **нийт** | already on the site |
| answer | **хариулт** | already on the site |
| multiply | **үржүүлэх** | ministry standard |
| positive | **эерэг** | ministry standard |
| average | **дундаж** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## shrinking-the-universe

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cd-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cd-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-multiplication-rule

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cd-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cd-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cd-l1-w1` and so on) exactly
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

