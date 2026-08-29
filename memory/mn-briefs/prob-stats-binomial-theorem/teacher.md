# MN authoring brief — Pascal's Triangle & the Binomial Theorem

**Topic** `prob-stats/binomial-theorem` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/binomial-theorem`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `pascals-triangle`

**Able to:** Build Pascal's triangle, read C(n,r) from row n, and prove the addition rule with a committee argument.

**The idea that carries it:** Pascal's triangle is the choose numbers arranged so that Pascal's identity C(n,r) = C(n−1,r−1) + C(n−1,r) builds each row from the last.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Counting rows and positions from 1.
- Treating the triangle and nCr as separate facts to memorize.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bt-l1-w1` — Build rows $0$ through $5$ of Pascal's triangle, and read off $C(5,2)$.
- `bt-l1-w2` — Verify Pascal's identity for $\binom{6}{3}$, then explain it with committees.
- `bt-l1-w3` — Without building all earlier rows, compute the entry of row $10$, position $3$.

**2 try-it problems**, same freedom and same condition.

### 2. `row-sums-and-subsets`

**Able to:** Count all subsets of an n-set with 2^n, explain why row n of Pascal's triangle sums to 2^n, and use the identity both ways.

**The idea that carries it:** Row n sums to 2^n: subsets counted by size (the row) equal subsets counted by yes/no decisions (the power).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting that 2^n includes the empty set.
- Case-summing C(n,1) + C(n,2) + ... by hand when the power was available.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bt-l2-w1` — A pizzeria offers $4$ toppings; any subset is allowed. Count the possible topping sets two ways.
- `bt-l2-w2` — A study group of $7$ students will send SOME of its members (at least one) to a conference. How many delegations are possible?
- `bt-l2-w3` — Compute $\binom{6}{0} + \binom{6}{1} + \cdots + \binom{6}{6}$ without computing a single choose.

**2 try-it problems**, same freedom and same condition.

### 3. `binomial-expansion`

**Able to:** Expand (a + b)^n with binomial coefficients from Pascal's triangle, and explain why the coefficients are chooses.

**The idea that carries it:** (a+b)^n = Σ C(n,k) a^(n−k) b^k — each coefficient counts which factors donated a b.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Distributing the power over the sum: (a+b)^n = a^n + b^n.
- Forgetting that b's coefficient rides along in the powers.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bt-l3-w1` — Expand $(a+b)^4$.
- `bt-l3-w2` — Expand $(x+2)^3$.
- `bt-l3-w3` — Expand $(y-1)^5$ — mind the signs.

**2 try-it problems**, same freedom and same condition.

### 4. `the-general-term`

**Able to:** Use the general term C(n,k) a^(n−k) b^k to find specific terms and coefficients without full expansion.

**The idea that carries it:** T_k = C(n,k) a^(n−k) b^k: set the exponent you want, solve for k, evaluate one term.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting the choose as the whole coefficient.
- Losing the sign when b is negative.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bt-l4-w1` — Find the coefficient of $x^7$ in $(x+2)^{10}$.
- `bt-l4-w2` — Find the coefficient of $x^4$ in $(2x-3)^6$.
- `bt-l4-w3` — Find the middle term of $(a+b)^8$.

**2 try-it problems**, same freedom and same condition.

### 5. `paths-and-the-triangle`

**Able to:** Count grid and peg-board paths with binomial coefficients, and read the triangle as accumulated route counts.

**The idea that carries it:** An m-east, k-north path is choosing which steps go north: C(m+k, k) — and the triangle's entries are route counts that add like Pascal's identity.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Choosing from the wrong total: C(m, k) instead of C(m+k, k).
- Adding path segments through a checkpoint.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bt-l5-w1` — How many shortest paths run from corner $A$ to corner $B$ of a $4 \times 3$ block grid ($4$ east, $3$ north)?
- `bt-l5-w2` — On the same grid, the coffee shop $C$ sits $2$ east, $1$ north of $A$. How many shortest $A$-to-$B$ paths pass through $C$?
- `bt-l5-w3` — A ball falls through $6$ rows of pegs, bouncing left or right at each. How many routes end exactly $2$ rights from the far-left cup — and which triang

**2 try-it problems**, same freedom and same condition.

### 6. `combinatorics-capstone`

**Able to:** Solve multi-part counting problems by decomposing into stages and dispatching each stage to the right tool.

**The idea that carries it:** Decompose into THEN/OR clauses, dispatch each clause to its tool, multiply and add accordingly — then verify by a second route.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Doing arithmetic before decomposition.
- Gluing OR-cases with multiplication (or THEN-stages with addition).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bt-l6-w1` — The café setup: pick $3$ featured drinks from $9$ (no order), arrange $4$ pastries left-to-right, and choose a $7$-day sequence of the two-sided sign.
- `bt-l6-w2` — A $5$-person study group forms from $6$ girls and $5$ boys, needing at least $3$ girls — and then elects one member as note-taker. How many outcomes?
- `bt-l6-w3` — How many $6$-character codes use $3$ A's and $3$ B's, OR consist of $6$ different letters chosen from C–J ($8$ letters) in some order?

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
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| size | **хэмжээ** | ministry standard |
| mean | **дундаж** | ministry standard |
| triangle | **гурвалжин** | ministry standard |
| number | **тоо** | ministry standard |
| counting | **тоолох** | ministry standard |
| exponent | **илтгэгч** | ministry standard |
| identity | **адилтгал** | ministry standard |
| addition | **нэмэх** | ministry standard |
| problem | **бодлого** | ministry standard |
| second | **хоёр дахь** | ministry standard |
| part | **хэсэг** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| equal | **тэнцүү** | ministry standard |
| at least | **дор хаяж** | already on the site |
| power | **зэрэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

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
## pascals-triangle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED bt-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY bt-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## row-sums-and-subsets

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED bt-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY bt-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`bt-l1-w1` and so on) exactly
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

