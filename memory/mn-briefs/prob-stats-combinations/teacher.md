# MN authoring brief — Combinations

**Topic** `prob-stats/combinations` · **7 lessons** · 21 worked examples · 10 practice · 7 test-yourself

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
> `prob-stats/combinations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `choosing-without-order`

**Able to:** Count unordered selections by dividing the permutation count by r!, and recognize when a selection is a combination.

**The idea that carries it:** C(n,r) = P(n,r)/r! — count ordered lineups, then divide out the r! internal orderings of each group.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing by r! when the picks have roles.
- Not dividing when the picks are equals.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l1-w1` — A teacher picks $3$ of $8$ students to represent the class (equal representatives, no roles). How many different trios are possible?
- `cb-l1-w2` — How many different pairs of toppings can you pick from $6$ pizza toppings?
- `cb-l1-w3` — Decide — permutation or combination — then count: a librarian picks $4$ of $10$ new books to display side by side in the front window, arranged left t

**2 try-it problems**, same freedom and same condition.

### 2. `computing-ncr`

**Able to:** Compute nCr efficiently with the factorial formula, cancellation, and the symmetry C(n,r) = C(n,n−r).

**The idea that carries it:** C(n,r) = n!/(r!(n−r)!): r factors over r!, cancel first — and flip to the smaller side with C(n,r) = C(n,n−r).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Multiplying the whole numerator before canceling.
- Treating C(n,0) as 0.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l2-w1` — Compute $C(9,3)$ by cancellation.
- `cb-l2-w2` — Compute $C(20, 18)$.
- `cb-l2-w3` — A pizzeria brags: "choose any $0$ to $3$ toppings from our $8$!" How many topping selections is that in total?

**2 try-it problems**, same freedom and same condition.

### 3. `committees-and-teams`

**Able to:** Apply nCr to committees, teams, and card hands, and multiply combinations for multi-group selections.

**The idea that carries it:** One group: C(n,r). Several groups or quotas: choose each part, multiply the parts.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding quota parts instead of multiplying.
- Choosing quota'd members from the whole pool.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l3-w1` — A club of $11$ members forms a $4$-person events committee. How many committees are possible?
- `cb-l3-w2` — From $7$ boys and $6$ girls, how many ways can a coach pick a mixed doubles squad of exactly $2$ boys and $2$ girls?
- `cb-l3-w3` — How many $5$-card hands from a standard deck contain EXACTLY two hearts?

**2 try-it problems**, same freedom and same condition.

### 4. `at-least-and-at-most`

**Able to:** Count at-least/at-most selection problems by exclusive cases or the complement, choosing whichever is shorter.

**The idea that carries it:** Split at-least/at-most by exact counts and add — or count the forbidden counts and subtract; take whichever route has fewer cases.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing "at least one woman" as C(6,1) × C(10,3).
- Case lists that skip an allowed count.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l4-w1` — A $4$-person committee from $6$ women and $5$ men must include at least one woman. How many committees?
- `cb-l4-w2` — Same club: how many $4$-person committees have at least THREE women?
- `cb-l4-w3` — A $5$-question quiz bank has $9$ easy and $4$ hard questions. A teacher builds a $5$-question quiz with at most one hard question. How many quizzes?

**2 try-it problems**, same freedom and same condition.

### 5. `combinations-with-conditions`

**Able to:** Handle must-include, must-exclude, and not-both conditions by adjusting the pool or splitting cases before choosing.

**The idea that carries it:** Conditions edit the pool before the choose: lock-ins shrink pool and quota, exclusions shrink the pool, and 'not both' subtracts the both-case.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Locking someone in but forgetting to shrink the quota.
- Treating "not both" as "neither".

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l5-w1` — A $5$-person committee from $12$ students must include the class president. How many committees?
- `cb-l5-w2` — A $6$-song setlist is chosen from $14$ songs, but the band refuses to play "Wonderwall". How many setlists (as unordered song sets)?
- `cb-l5-w3` — A $4$-person team from $10$ players cannot contain BOTH rivals R1 and R2. How many teams?

**2 try-it problems**, same freedom and same condition.

### 6. `permutation-or-combination`

**Able to:** Reliably classify counting problems as permutations, combinations, or multi-stage hybrids, and count them.

**The idea that carries it:** One swap test classifies everything; hybrids choose then arrange, gluing stages with multiplication.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Letting the story's drama pick the tool.
- Using nCr and then also multiplying by r! "to be safe".

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l6-w1` — From $9$ runners: (a) how many gold-silver-bronze outcomes? (b) how many ways can $3$ qualify for nationals (equal qualifiers)?
- `cb-l6-w2` — A crew of $4$ is chosen from $10$ sailors, and one of the four is then named captain. How many outcomes?
- `cb-l6-w3` — From $12$ paintings a gallery selects $5$ for a show, and hangs $2$ of those $5$ in the window, left and right. How many outcomes?

**2 try-it problems**, same freedom and same condition.

### 7. `stars-and-bars`

**Able to:** Count the ways to split n identical objects among k distinct groups by placing bars among stars, in both the empty-allowed and nobody-empty versions.

**The idea that carries it:** Identical objects into k distinct groups = arrangements of stars and bars: C(n+k−1, k−1) free, C(n−1, k−1) with nobody empty.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using k bars instead of k − 1.
- Mixing up the positive and free formulas.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cb-l7-w1` — How many solutions does $x + y + z = 10$ have in **positive** whole numbers?
- `cb-l7-w2` — $12$ identical candies are shared among $4$ kids; a kid may get none. How many ways?
- `cb-l7-w3` — How many whole-number solutions does $x + y + z + w = 15$ have if every variable is at least $2$?

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
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| counting | **тоолох** | ministry standard |
| formula | **томьёо** | ministry standard |
| problem | **бодлого** | ministry standard |
| side | **тал** | ministry standard |
| part | **хэсэг** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| divide | **хуваах** | ministry standard |
| subtract | **хасах** | ministry standard |
| test | **шалгалт** | ministry standard |
| at least | **дор хаяж** | already on the site |
| dividing | **хуваах** | ministry standard |
| at most | **дээд тал нь** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

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
## choosing-without-order

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cb-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cb-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## computing-ncr

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cb-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cb-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cb-l1-w1` and so on) exactly
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

