# MN authoring brief — Statistics & Data

**Topic** `11/statistics-and-data` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `11/statistics-and-data`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `mean-vs-median`

**Able to:** Compute mean and median, know how outliers pull the mean but not the median, and pick the appropriate center.

**The idea that carries it:** Mean = total/count and follows every value; median = the sorted middle and shrugs at outliers. Skewed data wants the median.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Taking the median without sorting first.
- Reporting the mean for skewed data as 'the typical value'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `st1-we1` — Find the mean and median of $30, 35, 40, 55$.
- `st1-we2` — Append $240$ to that list. New mean and median?
- `st1-we3` — Test scores $60, 70, 80, 90, 100$: mean and median?

**2 try-it problems**, same freedom and same condition.

### 2. `spread-and-standard-deviation`

**Able to:** Compute range and (population) standard deviation, and interpret SD as typical distance from the mean.

**The idea that carries it:** SD = √(average of squared deviations): the typical distance from the mean. Small SD = consistent; large = scattered.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the raw deviations (getting 0) and reporting 'no spread'.
- Forgetting the final square root and reporting the variance.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `st2-we1` — Compute the SD of $2, 4, 4, 4, 5, 5, 7, 9$.
- `st2-we2` — Two archers, five shots' distances from center: A: $1,1,2,2,4$; B: $0,0,1,4,5$. Range of each?
- `st2-we3` — Why do raw deviations always sum to zero? Show it for $2, 5, 8$ (mean 5).

**2 try-it problems**, same freedom and same condition.

### 3. `z-scores`

**Able to:** Compute $z = \frac{x - \mu}{\sigma}$, interpret sign and size, and use z-scores to compare across different scales.

**The idea that carries it:** z = (x − μ)/σ: distance from the mean in SD units. Sign = direction, size = rarity; x = μ + zσ runs it backwards.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing raw scores across different tests.
- Dropping the sign on below-mean values.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `st3-we1` — Math: 85 with $\mu = 70, \sigma = 15$. History: 78 with $\mu = 70, \sigma = 4$. Compute both z-scores.
- `st3-we2` — Heights: $\mu = 170$ cm, $\sigma = 8$. Find $z$ for 154 cm and 186 cm.
- `st3-we3` — A scholarship requires $z \ge 1.5$ on a test with $\mu = 200, \sigma = 20$. Minimum raw score?

**2 try-it problems**, same freedom and same condition.

### 4. `the-normal-curve`

**Able to:** Describe the normal distribution's shape and apply the empirical (68-95-99.7) rule to intervals around the mean.

**The idea that carries it:** The bell: symmetric around μ, width set by σ; 68% within 1σ, 95% within 2σ, 99.7% within 3σ — halve tails by symmetry.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying 68-95-99.7 to non-bell data.
- Forgetting to halve for one-sided questions.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `st4-we1` — Heights: $\mu = 170$ cm, $\sigma = 8$. Between which heights do the middle 68% and 95% fall?
- `st4-we2` — What percent of data lies ABOVE $\mu + 2\sigma$?
- `st4-we3` — Scores: $\mu = 70, \sigma = 5$. What percent scored between 70 and 80?

**2 try-it problems**, same freedom and same condition.

### 5. `working-the-normal-model`

**Able to:** Chain z-scores with the empirical rule to find percentages and percentiles for normal data, in both directions.

**The idea that carries it:** Raw → z → bell zone → percent (and reverse). Percentile = percent below; z = 1, 2 map to the 84th, 97.5th.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing percentile with percent score.
- Adding zone percentages without a sketch.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `st5-we1` — Heights $\mu = 170, \sigma = 8$: what percentile is 178 cm?
- `st5-we2` — Test $\mu = 70, \sigma = 5$: what score marks the 97.5th percentile?
- `st5-we3` — Same test: what fraction scores between 65 and 80?

**2 try-it problems**, same freedom and same condition.

### 6. `lying-with-statistics`

**Able to:** Spot correlation-vs-causation errors, biased samples, misleading graphs, and cherry-picked statistics.

**The idea that carries it:** Four traps: third factors, biased samples, cropped axes, and convenient averages. Five questions expose them all.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Accepting 'studies show a link' as 'X causes Y'.
- Trusting a poll because its sample is LARGE.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `st6-we1` — Cities with more firefighters have more fires. Do firefighters cause fires?
- `st6-we2` — A company: salaries 40, 42, 44, 46, 228 (thousands). The recruiter says 'average = 80'. Check both centers.
- `st6-we3` — A graph shows sales 'doubling' — bars of height 100 and 102 on an axis from 98 to 104. What really happened?

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
| range | **далайц** | ministry standard |
| shape | **дүрс** | ministry standard |
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| size | **хэмжээ** | ministry standard |
| scale | **томсгох** | already on the site |
| mean | **дундаж** | ministry standard |
| median | **медиан** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| spread | **тархалт** | ministry standard |
| distance | **зай** | ministry standard |
| sample | **түүвэр** | already on the site |
| unit | **нэгж** | ministry standard |
| halve | **хагаслах** | already on the site |
| interval | **завсар** | ministry standard |
| outlier | **онцгой утга** | already on the site |
| graph | **график** | ministry standard |
| model | **загвар** | ministry standard |
| total | **нийт** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

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
## mean-vs-median

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED st1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY st1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## spread-and-standard-deviation

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED st2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY st2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`st1-we1` and so on) exactly
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

