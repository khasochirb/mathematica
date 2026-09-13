# MN authoring brief — Probability

**Topic** `integrated-2/probability` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-2/probability`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `sample-spaces-and-events`

**Able to:** List a sample space, describe events as subsets of it, and compute probabilities of unions, intersections and complements.

**The idea that carries it:** List the sample space, describe events as subsets, and remember that $P(A \cup B)$ always subtracts the overlap — unless the events cannot overlap at all.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating the eleven dice SUMS as equally likely.
- Adding probabilities without subtracting the overlap.
- Counting 'at least one' case by case when the complement is one line.
- Reading 'or' as exclusive.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u8-l1-we1` — Two fair six-sided dice are rolled. Find the probability that the sum is $7$, and the probability that the sum is $2$. Why are they different?
- `im2-u8-l1-we2` — One card is drawn from a standard $52$-card deck. Find the probability it is a king OR a heart.
- `im2-u8-l1-we3` — A fair coin is tossed four times. Find the probability of getting at least one head.
- `im2-u8-l1-we4` — In a class of $30$ students, $18$ study French, $15$ study German, and $7$ study both. Find how many study neither, and the probability a randomly cho

**2 try-it problems**, same freedom and same condition.

### 2. `two-way-tables-and-conditional-probability`

**Able to:** Read joint, marginal and conditional probabilities from a two-way table, and use the conditional-probability formula.

**The idea that carries it:** Conditional probability changes the denominator: $P(A \mid B)$ divides by $B$ instead of by everything, which in a table means restricting to one row.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing by the grand total when the question says 'given'.
- Swapping $P(A \mid B)$ for $P(B \mid A)$.
- Using the same probability for both draws without replacement.
- Forgetting to check that a conditional row sums to $1$.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u8-l2-we1` — A survey of $200$ students records whether they cycle to school and whether they live within $2$ km. Cyclists living near: $60$. Cyclists living far: 
- `im2-u8-l2-we2` — Using the same survey ($60$ near cyclists, $20$ far cyclists, $40$ near non-cyclists, $80$ far non-cyclists), verify the conditional-probability formu
- `im2-u8-l2-we3` — A test for a condition affecting $2\%$ of a population is $95\%$ accurate on those who have it and $90\%$ accurate on those who do not. In a group of 
- `im2-u8-l2-we4` — Two cards are drawn from a standard deck WITHOUT replacement. Find the probability both are hearts, and the probability the second is a heart given th

**2 try-it problems**, same freedom and same condition.

### 3. `independence`

**Able to:** Test independence using both the product rule and the conditional definition, and distinguish independence from mutual exclusivity.

**The idea that carries it:** Independent means $P(A \cap B) = P(A)P(B)$, equivalently $P(A \mid B) = P(A)$ — and it is nearly the opposite of mutually exclusive, not a synonym.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating 'independent' and 'mutually exclusive' as the same thing.
- Assuming independence because the events 'feel unrelated'.
- Multiplying probabilities for draws without replacement.
- Believing a coin is 'due' after a run of heads.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u8-l3-we1` — A card is drawn from a standard deck. Are the events 'the card is a king' and 'the card is a heart' independent?
- `im2-u8-l3-we2` — A survey of $400$ people finds $240$ own a smartphone and $150$ subscribe to a streaming service; $90$ do both. Are ownership and subscription indepen
- `im2-u8-l3-we3` — Explain why 'the card is red' and 'the card is a spade' are mutually exclusive but NOT independent, and why no two events with non-zero probability ca
- `im2-u8-l3-we4` — A machine produces components with a $3\%$ defect rate, independently. Find the probability that a batch of $10$ contains no defects, and that it cont

**2 try-it problems**, same freedom and same condition.

### 4. `combining-the-probability-rules`

**Able to:** Choose the appropriate rule from a problem's wording, build and read tree diagrams, and combine rules across multi-stage situations.

**The idea that carries it:** Multiply along a path, add across paths — and check that every set of branches from a node sums to one.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding along a tree path instead of multiplying.
- Repeating the first-stage probabilities on the second stage without replacement.
- Reversing a conditional by simply swapping the events.
- Assuming independence to multiply, when the data says otherwise.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im2-u8-l4-we1` — A bag holds $4$ red and $6$ green counters. Two are drawn without replacement. Draw the tree and find the probability that the two counters are differ
- `im2-u8-l4-we2` — Factory A makes $60\%$ of a company's output with a $2\%$ defect rate; factory B makes the remaining $40\%$ with a $5\%$ defect rate. Find the overall
- `im2-u8-l4-we3` — In a school, $70\%$ of students take mathematics, $50\%$ take physics, and $40\%$ take both. Find the probability a student takes at least one, takes 
- `im2-u8-l4-we4` — A student answers a multiple-choice question with $4$ options. They know the answer with probability $0.7$; otherwise they guess. Find the probability

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
| mean | **дундаж** | ministry standard |
| probability | **магадлал** | ministry standard |
| product | **үржвэр** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| sample | **түүвэр** | already on the site |
| addition | **нэмэх** | ministry standard |
| formula | **томьёо** | ministry standard |
| table | **хүснэгт** | ministry standard |
| problem | **бодлого** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| model | **загвар** | ministry standard |
| multiply | **үржүүлэх** | ministry standard |
| divide | **хуваах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

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
## sample-spaces-and-events

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u8-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u8-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## two-way-tables-and-conditional-probability

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im2-u8-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im2-u8-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im2-u8-l1-we1` and so on) exactly
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

