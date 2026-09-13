# MN authoring brief — Sets & Operations

**Topic** `esh/sets-and-operations` · **4 lessons** · 8 worked examples · 10 practice · 7 test-yourself

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

A student finishes this topic holding these ideas. Everything else in the
brief serves them.

1. **Two levels, and the exam lives on the boundary.** `∈` speaks about one element; `⊆` speaks about a whole set. `2 ∈ {2,4}` and `{2} ⊆ {2,4}` are both true, `{2} ∈ {2,4}` is false — and ЭШ papers offer that third form as a distractor constantly. A student who cannot say which level a claim is on will lose marks they understood the maths for.

2. **Counting an inclusive run is a scoring skill, not a concept.** From a to b there are b − a + 1 integers, and the +1 is where fast solvers drop a point. It is worth more exam marks than anything else in the lesson, so it should be drilled to reflex rather than derived once.

3. **An operation is a sentence.** or → нэгдэл, and → огтлолцол, but-not → ялгавар, everything-else → гүйцээлт. Students who read the symbol as a sentence solve word-shaped problems directly; students who memorise four symbols translate twice and lose the thread.

**The error to design against:** Confusing the element claim with the subset claim — writing {2} ∈ {2,4}. It is the single most-offered wrong option in this topic on real papers, and it is a reasoning error about levels, not a slip.

If your Mongolian version lands those and a student can do the practice
set, the topic is right — however you got there.

Each lesson, and what the student must end up able to do:

### 1. `sets-and-membership`

**Able to:** Read and write sets in roster and set-builder notation, decide membership and subset claims, and count a set's elements.

**The idea that carries it:** A set is decided by membership alone — no order, no repeats. Element claims use $\in$, subset claims use $\subseteq$, and $|A|$ counts.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing $\{2\} \in \{2, 4\}$ because '2 is in the set'.
- Counting $\{5, 6, \ldots, 20\}$ as $20 - 5 = 15$ elements.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `esh-sets-l1-we1` — List the elements of $A = \{x \in \mathbb{Z} : -2 \le x < 4\}$ and state $|A|$.
- `esh-sets-l1-we2` — How many positive multiples of $3$ are less than $50$? Write the set in set-builder notation first.

**2 try-it problems**, same freedom and same condition.

### 2. `union-intersection-difference`

**Able to:** Compute $A \cup B$, $A \cap B$, $A \setminus B$ and $A'$ for concrete sets, and read each operation as a plain-language condition.

**The idea that carries it:** Or $\to \cup$, and $\to \cap$, but-not $\to \setminus$, everything-else $\to$ complement. The operation IS the sentence.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing $|A \cup B|$ as $|A| + |B|$.
- Treating $A \setminus B$ and $B \setminus A$ as the same set.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `esh-sets-l2-we1` — Let $A = \{1, 2, 3, 4, 5, 6\}$ and $B = \{4, 5, 6, 7, 8\}$. Find $|A \cup B|$, $|A \cap B|$ and $|A \setminus B|$.
- `esh-sets-l2-we2` — With universal set $U = \{1, 2, \ldots, 30\}$, let $E$ be the multiples of $2$ and $T$ the multiples of $3$. How many elements are even but NOT multip

**2 try-it problems**, same freedom and same condition.

### 3. `subsets-and-power-sets`

**Able to:** Count all subsets, proper subsets, and subsets constrained to contain or avoid particular elements.

**The idea that carries it:** Subsets are binary choices: $2^n$ total, and every constraint just pins switches — count $2^{\text{free}}$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting that $\varnothing$ and $A$ itself are subsets.
- Counting subsets that contain $a$ as $2^n - 1$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `esh-sets-l3-we1` — A set has $6$ elements. How many subsets does it have, and how many are proper?
- `esh-sets-l3-we2` — How many subsets of $\{1, 2, 3, 4, 5, 6, 7\}$ contain both $1$ and $2$?

**2 try-it problems**, same freedom and same condition.

### 4. `set-identities`

**Able to:** Apply De Morgan's laws and the distributive laws to rewrite and count complements of unions and intersections.

**The idea that carries it:** Complement swaps $\cup$ and $\cap$ (De Morgan). 'Neither' means $|U| - |A \cup B|$ — always.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Distributing the complement without flipping: $(A \cup B)' = A' \cup B'$.
- Reading 'not both' as 'neither'.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `esh-sets-l4-we1` — In $U = \{1, \ldots, 20\}$, $A$ = multiples of $4$, $B$ = multiples of $5$. Verify De Morgan by counting: $|(A \cup B)'|$ and $|A' \cap B'|$.
- `esh-sets-l4-we2` — Of $32$ students, $18$ passed algebra and the set of students who failed BOTH algebra and geometry has $6$ students. How many passed at least one subj

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
| half | **хагас** | already on the site |
| mean | **дундаж** | ministry standard |
| probability | **магадлал** | ministry standard |
| counting | **тоолох** | ministry standard |
| algebra | **алгебр** | ministry standard |
| difference | **ялгавар** | ministry standard |
| total | **нийт** | already on the site |
| power | **зэрэг** | ministry standard |
| intersection | **огтлолцол** | ministry standard |
| integer | **бүхэл тоо** | ministry standard |
| operation | **үйлдэл** | ministry standard |
| subset | **дэд олонлог** | already on the site |
| union | **нэгдэл** | already on the site |
| condition | **нөхцөл** | ministry standard |
| membership | **олонлогт харьяалагдах** | **proposed — tell us if it is wrong** |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## sets-and-membership

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED esh-sets-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY esh-sets-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## union-intersection-difference

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED esh-sets-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY esh-sets-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`esh-sets-l1-we1` and so on) exactly
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

