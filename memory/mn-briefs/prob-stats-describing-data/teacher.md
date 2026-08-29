# MN authoring brief — Describing Data

**Topic** `prob-stats/describing-data` · **7 lessons** · 21 worked examples · 10 practice · 7 test-yourself

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
> `prob-stats/describing-data`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `mean-and-median`

**Able to:** Compute mean and median, understand each one's relationship to the data, and predict how outliers move them.

**The idea that carries it:** Mean = balance point (every value pulls); median = positional middle (resistant). Pick the center that answers the question asked.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Taking the median without sorting.
- Reporting the mean for skewed data without comment.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l1-w1` — Village incomes (millions ₮): nine values of $1$ and one of $91$. Compute both centers.
- `dd-l1-w2` — Quiz scores: $6, 9, 4, 7, 9$. Find the mean and the median.
- `dd-l1-w3` — Delivery times (min): $22, 25, 27, 30$. Find the median, then recompute both centers after one disaster delivery of $110$ minutes joins the data.

**2 try-it problems**, same freedom and same condition.

### 2. `quartiles-and-iqr`

**Able to:** Find quartiles and the five-number summary, and compute the IQR as a resistant measure of spread.

**The idea that carries it:** Q1, median, Q3 cut sorted data into quarters; IQR = Q3 − Q1 measures the middle half's span — spread that outliers can't distort.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing quartiles on unsorted data.
- Reporting IQR as an interval.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l2-w1` — Scores: $4, 7, 8, 10, 12, 15, 21$ (already sorted, $n = 7$). Find the five-number summary and IQR.
- `dd-l2-w2` — Class A: $65, 67, 69, 71, 73, 75$. Class B: $30, 50, 65, 75, 90, 100$. Both medians are $70$. Compare IQRs.
- `dd-l2-w3` — Delivery times: $22, 25, 27, 30, 110$. Compare the range and the IQR as spread reports.

**2 try-it problems**, same freedom and same condition.

### 3. `boxplots-and-outliers`

**Able to:** Draw and read boxplots, apply the 1.5×IQR fence to flag outliers, and compare groups side by side.

**The idea that carries it:** Fences at Q1 − 1.5·IQR and Q3 + 1.5·IQR flag outliers; the boxplot draws box, median, whiskers-to-last-inlier, and outlier dots.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing whiskers to the fences (or to the outliers).
- Deleting flagged outliers automatically.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l3-w1` — Deliveries: five-number summary $22, 24, 27, 32, 110$ (with $Q_1 = 24$, $Q_3 = 32$). Fence the outliers.
- `dd-l3-w2` — Test scores: $Q_1 = 60$, median $= 75$, $Q_3 = 82$. What does the median's position inside the box say about shape?
- `dd-l3-w3` — Plants under two fertilizers, heights (cm) as five-number summaries — A: $12, 15, 18, 21, 24$; B: $10, 18, 22, 24, 26$. Compare the groups from the (m

**2 try-it problems**, same freedom and same condition.

### 4. `standard-deviation`

**Able to:** Compute the standard deviation of a dataset, interpret it as typical distance from the mean, and know when it (vs IQR) is the right spread.

**The idea that carries it:** s = √[Σ(x−x̄)²/(n−1)]: typical distance from the mean. Pair mean↔SD and median↔IQR — sensitive with sensitive, resistant with resistant.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the deviations without squaring.
- Pairing the median with the SD (or mean with IQR).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l4-w1` — Ana's arrows: $7, 8, 8, 9$. Compute $\bar{x}$ and $s$.
- `dd-l4-w2` — Bat's arrows: $4, 6, 10, 12$. Compute $\bar{x}$ and $s$, and compare with Ana.
- `dd-l4-w3` — A dataset has $\bar{x} = 50$, $s = 4$. Every value gets $10$ added (a scoring correction), then everything is doubled. Track $\bar{x}$ and $s$.

**2 try-it problems**, same freedom and same condition.

### 5. `shape-and-choosing-summaries`

**Able to:** Classify distribution shapes (symmetric, skewed, uniform, bimodal), predict mean-median order from shape, and choose the right summary pair.

**The idea that carries it:** The tail drags the mean: skew right → mean > median. Symmetric → mean±SD; skewed → median+IQR; bimodal → split before summarizing.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing before looking.
- Memorizing 'skew = where the hump is'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l5-w1` — Reaction times: median $0.32$s, mean $0.51$s. Infer the shape and choose the summary pair.
- `dd-l5-w2` — Exam scores where most students did well but a few bombed: predict the shape and the mean-median order.
- `dd-l5-w3` — Heights of a mixed group of adults and their young children form two humps. What goes wrong if you report one mean, and what's the right move?

**2 try-it problems**, same freedom and same condition.

### 6. `describing-data-capstone`

**Able to:** Produce complete SCSO descriptions and side-by-side comparisons, choosing summaries deliberately and connecting them to decisions.

**The idea that carries it:** SCSO in context, matched pairs, fence-flagged outliers with dispositions, and a closing 'so what' — that's a complete description; comparisons run it in parallel.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Describing numbers instead of the situation.
- Comparing only the centers.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l6-w1` — Commute times (min): $18, 22, 24, 25, 26, 28, 30, 31, 34, 62$. Produce a complete description.
- `dd-l6-w2` — Two suppliers' delivery delays (days): S1 mean $3.1$, SD $0.4$, symmetric. S2 mean $2.8$, SD $1.9$, right-skewed with flagged $9$- and $11$-day delays
- `dd-l6-w3` — The two exam sections (both median $74$; S2 left-skewed with three scores below $30$). Write the two sentences the principal actually needs.

**2 try-it problems**, same freedom and same condition.

### 7. `frequency-tables-and-grouped-data`

**Able to:** Compute mean, median, and mode from frequency tables; estimate the mean of grouped data with midpoints; solve for unknown frequencies; and use the sum-of-squares shortcut for the standard deviation.

**The idea that carries it:** Frequencies weight everything: mean = Σfx/Σf, mode = biggest f, and σ² = Σx²/n − (Σx/n)² — the two-sums shortcut that also pools groups.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing Σx by the number of ROWS instead of Σf.
- Averaging two groups' standard deviations to pool them.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd-l7-w1` — Scores and frequencies: $2$ appears $4$ times, $3$ appears $7$ times, $4$ appears $6$ times, $5$ appears $3$ times. Find the mean and the mode.
- `dd-l7-w2` — $19$ students' ages fall in groups $[8;10[, [10;12[, [12;14[, [14;16[$ with frequencies $8, a, b, 1$. The mean age is $11$. How many students are in $
- `dd-l7-w3` — Five players on team A scored with $\sum x = 20$, $\sum x^2 = 90$; five on team B with $\sum y = 30$, $\sum y^2 = 190$. Find the standard deviation of

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
| shape | **дүрс** | ministry standard |
| half | **хагас** | already on the site |
| measure | **хэмжих** | ministry standard |
| mean | **дундаж** | ministry standard |
| median | **медиан** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| spread | **тархалт** | ministry standard |
| parallel | **параллель** | ministry standard |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| square | **квадрат** | ministry standard |
| sample | **түүвэр** | already on the site |
| table | **хүснэгт** | ministry standard |
| mode | **моод** | ministry standard |
| midpoint | **дундаж цэг** | ministry standard |
| outlier | **онцгой утга** | already on the site |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

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
## mean-and-median

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dd-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dd-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## quartiles-and-iqr

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dd-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dd-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`dd-l1-w1` and so on) exactly
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

