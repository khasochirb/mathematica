# MN authoring brief — Counting Principles

**Topic** `prob-stats/counting-principles` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/counting-principles`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `lists-and-tree-diagrams`

**Able to:** Count outcomes by building organized lists and tree diagrams, and read the total from the structure instead of tallying one by one.

**The idea that carries it:** Fix the first choice, cycle the last — an organized list can't miss and can't repeat, and a tree's leaves count themselves.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Listing outcomes in whatever order they come to mind.
- Counting tree BRANCHES instead of tree LEAVES.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-l1-w1` — A sandwich shop offers $2$ breads (white, rye) and $3$ fillings (turkey, cheese, veggie). List every possible sandwich and count them.
- `cp-l1-w2` — You flip a coin and then roll a standard die. Draw the tree in your head: how many outcomes are there in total?
- `cp-l1-w3` — How many two-digit numbers can you build from the digits $1, 2, 3$ if no digit repeats? List them all.

**2 try-it problems**, same freedom and same condition.

### 2. `the-multiplication-principle`

**Able to:** Count multi-stage choices with the multiplication principle, using the slot method for codes, plates, and passwords.

**The idea that carries it:** Stages in sequence multiply: one slot per decision, the option count in each slot, multiply across.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding stage counts instead of multiplying.
- Forgetting slots shrink when repeats are banned.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-l2-w1` — You own $4$ shirts, $3$ pants, and $2$ pairs of shoes. How many different outfits (one of each) can you wear?
- `cp-l2-w2` — A license plate has $2$ letters followed by $3$ digits, repeats allowed. How many plates are possible?
- `cp-l2-w3` — How many $4$-digit PIN codes use four DIFFERENT digits (0–9)?

**2 try-it problems**, same freedom and same condition.

### 3. `the-addition-principle`

**Able to:** Add counts for exclusive alternatives, split hard problems into non-overlapping cases, and combine addition with multiplication in one problem.

**The idea that carries it:** "Or" adds, "then" multiplies — split into non-overlapping cases, multiply within each, add across.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying alternatives that should add.
- Splitting into cases that overlap.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-l3-w1` — A town offers $3$ bus routes and $2$ train lines to the city. You take exactly one. How many ways can you travel?
- `cp-l3-w2` — Friday options: the cinema shows $3$ movies at $4$ times each; the theater shows $2$ plays at $3$ times each. How many different evenings out are poss
- `cp-l3-w3` — How many two-digit numbers have BOTH digits odd or BOTH digits even? (A two-digit number can't start with $0$.)

**2 try-it problems**, same freedom and same condition.

### 4. `counting-with-restrictions`

**Able to:** Count arrangements under restrictions by seating the fussiest requirement first, and count must-sit-together problems with the block trick.

**The idea that carries it:** Seat the fussiest first; glue must-be-together items into a block and multiply by the block's internal arrangements.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Filling the easy slots first and hitting a contradiction.
- Forgetting the block's internal arrangements.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-l4-w1` — Five books go on a shelf. The dictionary must be on the far left. How many arrangements are there?
- `cp-l4-w2` — Four friends sit in a row, and Ana and Bat insist on sitting next to each other. How many seatings are possible?
- `cp-l4-w3` — How many $3$-digit EVEN numbers use the digits $1$–$5$ with no digit repeated?

**2 try-it problems**, same freedom and same condition.

### 5. `complementary-counting`

**Able to:** Count "at least one" and other sprawling events by counting the complement and subtracting from the total.

**The idea that carries it:** Want = total − don't want; "at least one X" is the complement of "no X at all".

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Taking the complement of only part of the condition.
- Subtracting from the wrong total.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-l5-w1` — Three coins are flipped. How many outcomes contain at least one head?
- `cp-l5-w2` — How many $4$-digit PIN codes (digits 0–9, repeats allowed) have at least one repeated digit?
- `cp-l5-w3` — Two dice are rolled. How many outcomes show at least one $6$?

**2 try-it problems**, same freedom and same condition.

### 6. `overcounting-and-inclusion-exclusion`

**Able to:** Correct overlapping counts with the two-set inclusion-exclusion formula, and divide out symmetric double-counting.

**The idea that carries it:** |A or B| = |A| + |B| − |A and B|; and when every outcome is counted k times by symmetry, divide by k.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding overlapping lists and stopping.
- Subtracting the overlap twice.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cp-l6-w1` — In a class, $18$ students play soccer, $12$ play basketball, and $7$ play both. How many students play at least one of the two sports?
- `cp-l6-w2` — How many integers from $1$ to $100$ are divisible by $2$ or by $5$?
- `cp-l6-w3` — Six people at a meeting each shake hands with everyone else exactly once. How many handshakes happen?

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
| count | **тоолох** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| sequence | **дараалал** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| counting | **тоолох** | ministry standard |
| time | **цаг** | already on the site |
| addition | **нэмэх** | ministry standard |
| formula | **томьёо** | ministry standard |
| problem | **бодлого** | ministry standard |
| subtracting | **хасах** | ministry standard |
| total | **нийт** | already on the site |
| multiply | **үржүүлэх** | ministry standard |
| divide | **хуваах** | ministry standard |
| subtract | **хасах** | ministry standard |
| at least | **дор хаяж** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

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
## lists-and-tree-diagrams

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cp-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cp-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-multiplication-principle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cp-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cp-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cp-l1-w1` and so on) exactly
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

