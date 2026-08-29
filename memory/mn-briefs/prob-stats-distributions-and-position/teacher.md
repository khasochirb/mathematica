# MN authoring brief — Distribution Shape & Position

**Topic** `prob-stats/distributions-and-position` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/distributions-and-position`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `histograms`

**Able to:** Build and read histograms: choose bins, count frequencies, and extract shape, center, and spread by eye.

**The idea that carries it:** Equal-width bins, touching bars, counts as heights — the histogram turns a number wall into shape, center, and spread you can see.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Leaving gaps between bars of adjacent bins.
- Trusting the shape from one bin width.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dp-l1-w1` — Quiz scores: $4, 7, 8, 8, 9, 11, 12, 13, 13, 14, 16, 21$. Bin by $[0,5), [5,10), [10,15), [15,20), [20,25)$ and give the frequencies.
- `dp-l1-w2` — A histogram of $50$ house prices shows bars (counts): $3, 12, 18, 10, 4$, then a lone bar of $3$ far to the right. Describe the distribution.
- `dp-l1-w3` — The same $200$ commutes are binned two ways: $4$ bins (shape: one smooth hump) and $40$ bins (shape: jagged spikes). Which do you trust, and what's th

**2 try-it problems**, same freedom and same condition.

### 2. `percentiles`

**Able to:** Compute percentile ranks from data, interpret percentile statements, and connect quartiles to the percentile scale.

**The idea that carries it:** Percentile rank = share of the crowd at or below you; quartiles are the 25/50/75 landmarks; equal percentile steps ≠ equal skill steps.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the 85th percentile as a score of 85%.
- Treating percentile steps as equal-sized skill steps.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dp-l2-w1` — Class scores (sorted): $45, 52, 58, 61, 64, 68, 71, 75, 82, 90$. Find the percentile rank of the student who scored $75$.
- `dp-l2-w2` — In the same class, what score sits at the 25th percentile, and what's its Unit 9 name?
- `dp-l2-w3` — Ana moved from the 50th to the 60th percentile on a national exam; Bat moved from the 89th to the 99th. Same 10-point percentile gain — same improveme

**2 try-it problems**, same freedom and same condition.

### 3. `z-scores`

**Able to:** Standardize values with z = (x − mean)/SD, interpret z-scores, and compare across different distributions.

**The idea that carries it:** z = (x − mean)/SD: distance from the mean in SD units — unit-free, sign-carrying, and reversible via x = mean + z·SD.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the sign.
- Comparing raw scores across different scales.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dp-l3-w1` — Ana: $85$ on a test with mean $70$, SD $10$. Bat: $700$ on a test with mean $500$, SD $100$. Standardize both and compare.
- `dp-l3-w2` — Heights: mean $170$ cm, SD $8$. Find the z-scores of a $154$ cm and a $190$ cm person, and interpret.
- `dp-l3-w3` — A scholarship requires $z \ge 1.8$ on an exam with mean $62$ and SD $9$. Find the raw cutoff score.

**2 try-it problems**, same freedom and same condition.

### 4. `the-normal-curve`

**Able to:** Recognize the normal distribution, and apply the empirical rule: 68% within 1 SD, 95% within 2, 99.7% within 3.

**The idea that carries it:** The bell is set by μ and σ alone; 68–95–99.7 within 1–2–3 SDs, sliced by symmetry into tail percentages.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying 68–95–99.7 to skewed data.
- Forgetting to halve the outside.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dp-l4-w1` — Adult heights: normal with mean $170$ cm, SD $8$. What share of adults stands between $162$ and $178$ cm? Between $154$ and $186$?
- `dp-l4-w2` — Same heights: what share is TALLER than $186$ cm?
- `dp-l4-w3` — Exam scores: normal, mean $72$, SD $6$. What share scored between $78$ and $84$?

**2 try-it problems**, same freedom and same condition.

### 5. `normal-applications`

**Able to:** Solve normal-distribution problems end to end: standardize, use the empirical rule at landmarks, and bracket between them.

**The idea that carries it:** Standardize → sketch → slice: exact at the 1-2-3 landmarks, bracket between them, and run backward from shares to cutoffs via z.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Inventing exact percentages between landmarks.
- Losing the direction in backward problems.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dp-l5-w1` — Bottles: normal, mean $503$ ml, SD $2$; label promises $500$ ml. Bracket the fraction of under-filled bottles.
- `dp-l5-w2` — Test scores: normal, mean $250$, SD $40$. A program admits the top $16\%$. Find the cutoff score.
- `dp-l5-w3` — Reaction times: normal, mean $300$ ms, SD $20$. A gamer clocks $260$ ms (lower = better). What percentile is that, and how rare?

**2 try-it problems**, same freedom and same condition.

### 6. `position-capstone`

**Able to:** Combine histograms, percentiles, z-scores, and the empirical rule to locate and compare values across any distributions.

**The idea that carries it:** Shape-check, standardize, slice, translate to percentiles — one pipeline locates any value in any crowd, with caveats attached.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing z-scores without checking the crowds are comparable.
- Using the z-to-percentile bridge on skewed data.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `dp-l6-w1` — Ana: $86$ on Exam A ($\mu = 70$, $\sigma = 8$). Bat: $640$ on Exam B ($\mu = 520$, $\sigma = 80$). Both roughly normal. Run the full pipeline.
- `dp-l6-w2` — A clinic flags patients outside $\mu \pm 2\sigma$ on a blood measure (normal, $\mu = 120$, $\sigma = 10$). What share gets flagged, and what are the f
- `dp-l6-w3` — Bat's coach protests: "Exam B's cohort was national-level; Ana's was one school. The percentiles aren't comparable!" Is the protest statistically soun

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
| count | **тоолох** | ministry standard |
| scale | **томсгох** | already on the site |
| translate | **хөрвүүлэх** | already on the site |
| mean | **дундаж** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| spread | **тархалт** | ministry standard |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| unit | **нэгж** | ministry standard |
| problem | **бодлого** | ministry standard |
| height | **өндөр** | already on the site |
| position | **байрлал** | ministry standard |
| width | **өргөн** | already on the site |
| equal | **тэнцүү** | ministry standard |
| the whole | **бүхэл** | ministry standard |
| sign | **тэмдэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

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
## histograms

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dp-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dp-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## percentiles

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED dp-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY dp-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`dp-l1-w1` and so on) exactly
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

