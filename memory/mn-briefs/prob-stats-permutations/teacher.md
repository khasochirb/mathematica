# MN authoring brief — Permutations & Arrangements

**Topic** `prob-stats/permutations` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/permutations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `factorials`

**Able to:** Count arrangements of ALL n objects with n!, compute and simplify factorials, and explain why 0! = 1.

**The idea that carries it:** n! = n × (n−1) × ⋯ × 1 counts the arrangements of all n distinct objects — and factorials cancel, they don't get computed.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing giant factorials digit by digit.
- Assuming 0! = 0.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l1-w1` — Five friends line up for a photo. How many different orders are possible?
- `pm-l1-w2` — Compute $\frac{9!}{7!}$ without a calculator.
- `pm-l1-w3` — A bookshelf holds $4$ novels and you also have $1$ atlas that must stay in your bag. How many ways can the shelf be arranged — and what does $0!$ have

**2 try-it problems**, same freedom and same condition.

### 2. `permutations-of-some`

**Able to:** Count ordered selections of r objects from n with P(n, r) = n!/(n−r)!, and recognize when a problem is a permutation.

**The idea that carries it:** P(n, r) = n!/(n−r)! — r shrinking slots from n; use it when order genuinely matters.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing by r! out of habit.
- Writing n!/(n−r)! as n! − (n−r)! or n!/r!.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l2-w1` — Eight sprinters race for gold, silver, and bronze. How many different podiums are possible?
- `pm-l2-w2` — A club of $10$ people elects a president, a secretary, and a treasurer (no one holds two jobs). How many outcomes are possible?
- `pm-l2-w3` — How many $4$-letter codes (no repeated letters) can be formed from the $7$ letters A–G?

**2 try-it problems**, same freedom and same condition.

### 3. `repeated-letters`

**Able to:** Count arrangements of objects with repeats using n! divided by the factorial of each repeat count.

**The idea that carries it:** Identical objects overcount by their own arrangements: divide n! by k! for every symbol repeated k times.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing by the repeat COUNT instead of its factorial.
- Only dividing out ONE of several repeated symbols.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l3-w1` — How many distinct arrangements does the word MOON have?
- `pm-l3-w2` — How many distinct arrangements does MISSISSIPPI have?
- `pm-l3-w3` — A city walk goes $3$ blocks east and $2$ blocks north. How many different shortest routes are there?

**2 try-it problems**, same freedom and same condition.

### 4. `circular-arrangements`

**Able to:** Count circular arrangements with (n−1)!, by fixing one person or dividing rotations out.

**The idea that carries it:** A circle kills rotations: fix one person and arrange the rest — (n−1)! seatings.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using n! at a round table.
- Anchoring TWO people to "be extra safe".

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l4-w1` — Five friends sit around a round table. How many genuinely different seatings are there?
- `pm-l4-w2` — Six knights sit at a round table, but Sir Ana and Sir Bat must sit together. How many seatings?
- `pm-l4-w3` — Eight charms go on a bracelet that can be rotated AND flipped over. How many distinct bracelets?

**2 try-it problems**, same freedom and same condition.

### 5. `arrangements-with-restrictions`

**Able to:** Combine factorial tools with Unit 1's restriction tricks: ends, blocks, separations, and alternating patterns.

**The idea that carries it:** Every arrangement restriction is ends-first, a glue block, a subtraction, or a pattern skeleton — usually in combination.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the 2 ways to assign the two ends.
- Counting only one alternating skeleton.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l5-w1` — Six students line up, and the two class captains must take the two END positions. How many lineups?
- `pm-l5-w2` — Five friends line up for a photo. Two of them just argued and refuse to stand next to each other. How many lineups?
- `pm-l5-w3` — Three boys and three girls line up so that boys and girls alternate. How many lineups?

**2 try-it problems**, same freedom and same condition.

### 6. `choosing-the-right-tool`

**Able to:** Diagnose a counting problem — repeats? order? identical objects? circle? — and dispatch it to the right formula.

**The idea that carries it:** Diagnose before computing: repeats → n^r; ordered no-repeat → P(n,r) or n!; identical copies → divide; circle → (n−1)!.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reaching for the most recent formula instead of the right one.
- Skipping the shrink test on a shaky diagnosis.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l6-w1` — Diagnose and count: how many $4$-digit ATM codes are possible (digits $0$–$9$, repeats allowed)?
- `pm-l6-w2` — Diagnose and count: a relay team of $4$ runners must choose their running ORDER. How many orders?
- `pm-l6-w3` — Diagnose and count: how many distinct arrangements does the word TATTOO have?

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
| circle | **тойрог** | ministry standard |
| counting | **тоолох** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| subtraction | **хасалт** | already on the site |
| formula | **томьёо** | ministry standard |
| table | **хүснэгт** | ministry standard |
| problem | **бодлого** | ministry standard |
| divide | **хуваах** | ministry standard |
| pattern | **хэв маяг** | already on the site |
| test | **шалгалт** | ministry standard |
| dividing | **хуваах** | ministry standard |
| combination | **хэсэглэл** | ministry standard |
| factorial | **факториал** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## factorials

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pm-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pm-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## permutations-of-some

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pm-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pm-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pm-l1-w1` and so on) exactly
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

