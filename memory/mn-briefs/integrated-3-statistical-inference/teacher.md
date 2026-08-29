# MN authoring brief — Statistical Inference

**Topic** `integrated-3/statistical-inference` · **4 lessons** · 12 worked examples · 16 practice · 8 test-yourself

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
> `integrated-3/statistical-inference`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `populations-samples-and-study-types`

**Able to:** Distinguish population from sample and parameter from statistic, recognise biased sampling methods, classify surveys, observational studies and experiments, and explain why only a randomised experiment supports a causal conclusion.

**The idea that carries it:** A random sample is a stirred spoonful: its statistic estimates the population's parameter. And only a randomised experiment — where chance assigns the treatment — can turn "goes together" into "causes".

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling the sample's number a parameter.
- Trusting a big sample over a random one.
- Reading causation off an observational study.
- Confusing random sampling with random assignment.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u7-l1-we1` — A school has $1200$ students. A random sample of $50$ is asked whether school should start later; $32$ say yes. Identify the population, the sample, t
- `im3-u7-l1-we2` — Asked about sports funding, $36$ of the $40$ students polled at the gym door said yes; in a random sample of $50$, only $21$ did. Compute both proport
- `im3-u7-l1-we3` — Classify each study, and state which one could justify the claim "the supplement CAUSES taller seedlings": (a) $200$ gardeners are asked whether they 

**3 try-it problems**, same freedom and same condition.

### 2. `the-normal-model`

**Able to:** Use the mean and standard deviation of a normal distribution with the 68–95–99.7 rule to estimate percentages and counts, and use z-scores to place and compare values from different distributions.

**The idea that carries it:** Two numbers describe a whole normal population: 68% of it lies within one standard deviation of the mean, 95% within two, 99.7% within three — and the z-score converts any value onto that shared ruler.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying the empirical rule to skewed data.
- Forgetting to halve the tail.
- Comparing raw scores from different tests.
- Thinking a z-score must be positive.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u7-l2-we1` — Student heights are approximately normal with mean $170$ cm and standard deviation $8$ cm. What fraction of students stand between $162$ and $178$ cm?
- `im3-u7-l2-we2` — Ana scored $82$ on a maths test with mean $70$ and standard deviation $8$, and $75$ on a history test with mean $60$ and standard deviation $12$. Whic
- `im3-u7-l2-we3` — A machine fills bottles with mean $500$ ml and standard deviation $5$ ml, approximately normally. Out of $2000$ bottles, about how many hold more than

**3 try-it problems**, same freedom and same condition.

### 3. `simulation-and-sampling-variability`

**Able to:** Recognise that statistics vary from sample to sample, design simulations with random digits, and use the results of many simulated trials to judge whether an observed result is consistent with a claimed model.

**The idea that carries it:** To judge a claim, assume it, simulate it, and see where the real result lands: if outcomes that extreme almost never occur in the simulation, doubt the claim — not your luck.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Expecting a sample to match the population exactly.
- Judging a result with no reference distribution.
- Assigning digits that don't match the probability.
- Running a handful of trials and calling it a distribution.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u7-l3-we1` — A coin claimed fair lands heads $62$ times in $100$ flips. In $200$ simulated rounds of $100$ genuinely fair flips, only $4$ rounds reached $62$ or mo
- `im3-u7-l3-we2` — A sweet company claims $40\%$ of its sweets are red. A random bag of $25$ has only $5$ red ($20\%$). Fifty simulated bags at the claimed rate containe
- `im3-u7-l3-we3` — A basketball player claims to make $30\%$ of three-pointers. Design a random-digit simulation of $5$ shots, and use it to decide whether making $3$ of

**3 try-it problems**, same freedom and same condition.

### 4. `margin-of-error-and-conclusions`

**Able to:** Attach a margin of error to a sample proportion, read polls as intervals rather than points, shrink the margin by growing the sample, and judge whether an experiment's difference between treatments exceeds what chance re-assignment produces.

**The idea that carries it:** A poll's number is an interval, not a point — about 1/sqrt(n) wide on each side. And an experiment's gap means something only when it beats the gaps that random re-shuffling of the same data routinely makes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading a poll as an exact number.
- Doubling the sample to halve the margin.
- Declaring a winner inside the margin.
- Using the margin of error to excuse a biased sample.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u7-l4-we1` — A poll of $400$ voters finds $52\%$ support candidate A. Attach a margin of error, give the interval, and say whether the poll shows A ahead.
- `im3-u7-l4-we2` — How many voters must be polled to cut the margin of error from $5$ points to $2.5$ points? Then check the quick rule against the refined margin $2\sqr
- `im3-u7-l4-we3` — Eighty seedlings are randomly split $40$–$40$; the fertilised group has $28$ thrive, the control $16$. Re-randomising the same $44$ thrive/$36$ fail l

**3 try-it problems**, same freedom and same condition.

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
| size | **хэмжээ** | ministry standard |
| mean | **дундаж** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| number | **тоо** | ministry standard |
| sample | **түүвэр** | already on the site |
| proportion | **пропорц** | already on the site |
| interval | **завсар** | ministry standard |
| difference | **ялгавар** | ministry standard |
| point | **цэг** | ministry standard |
| side | **тал** | ministry standard |
| model | **загвар** | ministry standard |
| digit | **цифр** | already on the site |
| statistic | **статистик** | ministry standard |
| distribution | **тархалт** | ministry standard |
| outcome | **үр дүн** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## populations-samples-and-study-types

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u7-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u7-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-normal-model

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u7-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u7-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u7-l1-we1` and so on) exactly
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

