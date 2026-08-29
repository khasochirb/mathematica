# MN authoring brief — Describing Data

**Topic** `integrated-1/data-and-statistics` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/data-and-statistics`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `centre-and-spread`

**Able to:** Compute the mean, median, range and interquartile range of a data set, choose the measure of centre that suits the distribution's shape, and identify outliers by the $1.5 \times \text{IQR}$ rule.

**The idea that carries it:** Mean uses every value and is dragged by outliers; median ignores extremes and is robust. IQR measures the middle half, and the $1.5 \times \text{IQR}$ fences flag outliers for investigation — not deletion.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Finding the median without sorting the data first.
- Taking a single middle value when the count is even.
- Reporting the mean for a badly skewed data set.
- Deleting an outlier because it is inconvenient.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u9-l1-we1` — Find the mean and median of $4, 7, 7, 9, 13$. Then add the value $61$ and recompute both.
- `im1-u9-l1-we2` — For the data $12, 15, 18, 22, 25, 28, 31, 35$, find the five-number summary, the range and the IQR.
- `im1-u9-l1-we3` — For the data $3, 5, 6, 6, 7, 8, 9, 10, 25$, find the IQR and use the $1.5 \times \text{IQR}$ rule to identify any outliers.
- `im1-u9-l1-we4` — A company reports a mean salary of $2\,400\,000$₮ but a median of $1\,100\,000$₮ across $9$ employees. Explain what this tells you, and decide which f

**3 try-it problems**, same freedom and same condition.

### 2. `comparing-distributions`

**Able to:** Compare two data sets by centre, spread and shape; read a dot plot, histogram and box plot; and describe a distribution as symmetric, skewed or clustered.

**The idea that carries it:** Compare centre, spread AND shape. Mean above median means right-skewed. Dot plots show every value, histograms show shape (at a chosen bin width), box plots compare groups.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing two data sets by their means alone.
- Reading 'skewed right' as the bulk of the data being on the right.
- Treating a histogram's shape as a property of the data.
- Assuming a box plot shows everything.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u9-l2-we1` — Bus A's journey times (minutes): $18, 22, 26, 28, 30, 34, 38, 44, 50$. Bus B's: $28, 29, 29, 30, 30, 30, 31, 31, 32$. Compare them fully.
- `im1-u9-l2-we2` — A data set has mean $46$ and median $61$. Describe its likely shape and sketch what it looks like.
- `im1-u9-l2-we3` — Class X scores: $55, 60, 62, 65, 68, 70, 72, 75, 80$. Class Y: $40, 45, 62, 66, 68, 70, 88, 92, 95$. Both have median $68$. Compare and advise which c
- `im1-u9-l2-we4` — Explain how changing the bin width of a histogram can change the story the data appears to tell.

**3 try-it problems**, same freedom and same condition.

### 3. `two-way-tables`

**Able to:** Read a two-way frequency table; compute joint, marginal and conditional relative frequencies; and use conditional frequencies to judge whether two variables appear associated.

**The idea that carries it:** Joint divides by the grand total, marginal divides a margin by the grand total, conditional divides by a ROW or COLUMN total. The denominator is what the question asks about.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dividing by the grand total when the question asks about a subgroup.
- Treating 'X% of A are B' and 'X% of B are A' as the same statement.
- Building a table whose margins do not agree.
- Concluding causation from a difference in conditional frequencies.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u9-l3-we1` — A survey of $200$ students records travel to school. Of $110$ girls, $66$ walk and $44$ take the bus. Of $90$ boys, $36$ walk and $54$ take the bus. B
- `im1-u9-l3-we2` — Using that table, find: (a) the joint relative frequency of being a girl who walks; (b) the marginal relative frequency of walking; (c) the conditiona
- `im1-u9-l3-we3` — Using the same table, compare the conditional frequency of walking for girls and for boys, and say whether travel method appears associated with gende
- `im1-u9-l3-we4` — In a town, $180$ people were asked about owning a bicycle and cycling to work. $120$ own a bicycle, of whom $84$ cycle to work. Of the $60$ non-owners

**3 try-it problems**, same freedom and same condition.

### 4. `scatter-plots-and-lines-of-fit`

**Able to:** Describe the association in a scatter plot, fit and interpret a line of best fit, read the correlation coefficient, and distinguish correlation from causation.

**The idea that carries it:** Describe direction, form, strength and outliers. The fitted line's slope is a predicted change per unit. $r$ measures LINEAR strength only — and no value of $r$, however close to $1$, establishes causation.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Concluding that one variable causes the other from a strong correlation.
- Reading r ≈ 0 as 'no relationship at all'.
- Interpreting the intercept of a fitted line when input zero is meaningless.
- Extrapolating a fitted line far beyond the data.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u9-l4-we1` — Study hours and test scores for six students: $(2, 55), (3, 60), (5, 70), (6, 72), (8, 85), (9, 88)$. Describe the association and estimate a line of 
- `im1-u9-l4-we2` — A line of fit for shoe size against height (cm) is $h = 3.2s + 130$. Interpret both parameters, predict the height for size $42$, and comment on the i
- `im1-u9-l4-we3` — For the line $y = 2x + 5$ fitted to data including the points $(3, 13)$, $(4, 12)$ and $(6, 18)$, compute the residuals and comment on the fit.
- `im1-u9-l4-we4` — A study finds a strong positive correlation ($r = 0.87$) between the number of firefighters sent to a fire and the damage caused. Should fire departme

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
| range | **далайц** | ministry standard |
| shape | **дүрс** | ministry standard |
| half | **хагас** | already on the site |
| measure | **хэмжих** | ministry standard |
| mean | **дундаж** | ministry standard |
| median | **медиан** | ministry standard |
| line | **шулуун** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| spread | **тархалт** | ministry standard |
| slope | **налалт** | ministry standard |
| centre | **төв** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| table | **хүснэгт** | ministry standard |
| outlier | **онцгой утга** | already on the site |
| linear | **шугаман** | ministry standard |
| skew | **хазайсан** | ministry standard |
| form | **хэлбэр** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

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
## centre-and-spread

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u9-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u9-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## comparing-distributions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u9-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u9-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u9-l1-we1` and so on) exactly
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

