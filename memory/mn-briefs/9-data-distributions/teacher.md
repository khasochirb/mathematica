# MN authoring brief — Data Distributions

**Topic** `9/data-distributions` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `9/data-distributions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `dot-plots-and-histograms`

**Able to:** Build and read dot plots and histograms, choosing sensible bins.

**The idea that carries it:** Dot plots show individuals; histograms bin them into shape. Bin width is a choice that changes the picture.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading a histogram bar as one data value.
- Using unequal bin widths.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd1-we1` — Quiz scores: $7, 8, 8, 9, 8, 7, 10, 8$. Describe the dot plot.
- `dd1-we2` — Commute minutes for 20 workers, binned by 10: $[0,10)$: 3, $[10,20)$: 8, $[20,30)$: 6, $[30,40)$: 3. How many commute under 20 minutes, and what fract
- `dd1-we3` — A histogram of 60 values uses bins of width 5 from 0 to 40. How many bars, and what's lost compared to a dot plot?

**2 try-it problems**, same freedom and same condition.

### 2. `shape-of-distributions`

**Able to:** Describe distribution shapes (symmetric, skewed, uniform, bimodal), spot outliers, and match shape to the right center.

**The idea that carries it:** Name the shape first; the shape picks the center — tails drag means, medians hold their ground.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Naming the skew after the peak's side.
- Reporting the mean for skewed data without comment.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd2-we1` — Incomes (thousands): $30, 35, 38, 40, 42, 45, 250$. Compute the mean and median; explain the gap.
- `dd2-we2` — A histogram of 500 fair die rolls shows six bars of heights $84, 80, 86, 83, 82, 85$. Shape?
- `dd2-we3` — A gym's arrival-time histogram peaks at 7 AM and again at 6 PM. Shape and story?

**2 try-it problems**, same freedom and same condition.

### 3. `quartiles-and-iqr`

**Able to:** Compute the five-number summary (min, Q1, median, Q3, max) and the IQR.

**The idea that carries it:** Sort, split, split again: five numbers summarize everything, and Q3 − Q1 measures outlier-proof spread.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Finding quartiles before sorting.
- Including the median in both halves (odd counts).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd3-we1` — Find the five-number summary of $3, 5, 7, 8, 9, 12, 13, 15$.
- `dd3-we2` — Compute the IQR of that data.
- `dd3-we3` — Replace the max $15$ with $150$. What happens to the range and the IQR?

**2 try-it problems**, same freedom and same condition.

### 4. `box-plots`

**Able to:** Construct box plots from five-number summaries and read center, spread, and skew from them.

**The idea that carries it:** Box = middle 50%, wall = median, whiskers = tails; every section holds a quarter of the data.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading a long section as 'more data'.
- Marking the mean inside the box.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd4-we1` — Draw the box plot of the summary $3, 6, 8.5, 12.5, 15$: describe each piece.
- `dd4-we2` — A box plot: min $10$, $Q_1 = 30$, median $35$, $Q_3 = 40$, max $85$. Diagnose the shape.
- `dd4-we3` — In that plot, what fraction of values exceed $40$?

**2 try-it problems**, same freedom and same condition.

### 5. `outliers-and-fences`

**Able to:** Apply the 1.5·IQR rule to identify outliers and draw fenced box plots.

**The idea that carries it:** Fences at Q1 − 1.5·IQR and Q3 + 1.5·IQR; beyond them, dots — and an investigation, not an automatic deletion.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Drawing whiskers to the fences themselves.
- Deleting every outlier automatically.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd5-we1` — Data with $Q_1 = 210$, $Q_3 = 240$: build the fences.
- `dd5-we2` — Marathon times ran $195$ to $302$. Which values are outliers under those fences?
- `dd5-we3` — Where does the fenced plot's right whisker end if the largest inside value is $258$?

**2 try-it problems**, same freedom and same condition.

### 6. `comparing-distributions`

**Able to:** Compare two or more distributions using aligned box plots and histograms: center, spread, shape, and outliers.

**The idea that carries it:** One axis, then centers → spreads → shapes → outliers; overlap tempers every verdict.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing plots drawn on different axes.
- Declaring victory on medians alone.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dd6-we1` — Fertilizer A: summary $2, 5, 7, 10, 14$ (kg). B: $6, 7.5, 9, 10, 12$. Compare centers and spreads.
- `dd6-we2` — Do A and B's boxes overlap much?
- `dd6-we3` — A's min is $2$ kg (a struggling plant); B's is $6$. What does the LOW tail say?

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
| measure | **хэмжих** | ministry standard |
| mean | **дундаж** | ministry standard |
| median | **медиан** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| spread | **тархалт** | ministry standard |
| proof | **баталгаа** | already on the site |
| number | **тоо** | ministry standard |
| outlier | **онцгой утга** | already on the site |
| skew | **хазайсан** | ministry standard |
| width | **өргөн** | already on the site |
| test | **шалгалт** | ministry standard |
| distribution | **тархалт** | ministry standard |
| change | **өөрчлөлт** | ministry standard |
| quarter | **дөрөвний нэг** | ministry standard |
| histogram | **гистограмм** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

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
## dot-plots-and-histograms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dd1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dd1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## shape-of-distributions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dd2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dd2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`dd1-we1` and so on) exactly
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

