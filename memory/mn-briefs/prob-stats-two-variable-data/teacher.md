# MN authoring brief — Two-Variable Data

**Topic** `prob-stats/two-variable-data` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/two-variable-data`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `scatterplots`

**Able to:** Plot paired data as scatterplots, and describe associations by direction, form, and strength.

**The idea that carries it:** One point per individual, explanatory on x; describe direction, form, strength — and flag points off the pattern.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Plotting the response on x.
- Describing only the direction.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tv-l1-w1` — Hours studied vs exam score for $20$ students: the cloud drifts up-right, roughly straight, moderately tight. Describe the association — and who goes 
- `tv-l1-w2` — Outdoor temperature vs hot-chocolate sales at a kiosk: describe the expected cloud.
- `tv-l1-w3` — Height vs age for people aged $2$ to $40$: why does 'linear' fail as a description?

**2 try-it problems**, same freedom and same condition.

### 2. `correlation`

**Able to:** Interpret r: sign, magnitude, unitlessness, and its blind spots (nonlinearity, outlier sensitivity).

**The idea that carries it:** r ∈ [−1, 1]: sign = direction, magnitude = linear tightness; unit-free — but blind to curves and fragile to outliers, so plot first.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading r = 0 as 'no relationship'.
- Treating r as a slope or a percentage.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tv-l2-w1` — Match the descriptions to $r$ values $\{-0.9, -0.3, 0.05, 0.6\}$: (a) tight downhill cloud; (b) loose downhill mist; (c) shapeless blob; (d) clear but
- `tv-l2-w2` — Height-vs-weight gives $r = 0.65$ measured in cm and kg. The researchers convert to inches and pounds. What happens to $r$ — and to the claim it makes
- `tv-l2-w3` — Speed vs fuel efficiency: efficiency RISES up to $\sim 80$ km/h then FALLS beyond — a clean inverted U. A student computes $r \approx 0.02$ and report

**2 try-it problems**, same freedom and same condition.

### 3. `the-regression-line`

**Able to:** Interpret and use the least-squares line ŷ = a + bx: slope and intercept in context, and predictions within range.

**The idea that carries it:** ŷ = a + bx minimizes squared vertical misses; slope = predicted change per unit of x (in context), intercept = the x = 0 anchor, and the line passes through the cloud's center.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the slope as a guarantee per student.
- Predicting outside the data's x-range.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tv-l3-w1` — The study line: $\hat{y} = 42 + 5.2x$ (score from hours). Interpret both coefficients and predict the score for $6$ hours.
- `tv-l3-w2` — Ana studied $5$ hours and scored $75$. The line predicts $\hat{y} = 42 + 26 = 68$. Compute and interpret her residual.
- `tv-l3-w3` — The hours in the data run from $0$ to $8$. A classmate plugs in $x = 25$ hours and announces $\hat{y} = 172$ points on a $100$-point exam. Name the cr

**2 try-it problems**, same freedom and same condition.

### 4. `how-good-is-the-line`

**Able to:** Judge fit quality with residuals: typical miss size, leftover patterns, r² as explained variation, and influential points.

**The idea that carries it:** Judge the line by its leftovers: typical miss size, no leftover pattern, r² as the share of variation explained, and lever points checked with/without.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading r² = 0.64 as '64% accurate' or 'correct 64% of the time'.
- Judging fit by r alone, skipping the residual plot.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tv-l4-w1` — The study line has $r = 0.8$. Compute and interpret $r^2$.
- `tv-l4-w2` — Two models predict delivery time. Model 1: typical residual $\pm 3$ min. Model 2: typical residual $\pm 15$ min. Same slope sentences. Which do you sh
- `tv-l4-w3` — A growth line fits age-vs-height for children $2$–$16$, but its residuals curve: positive at both ends, negative in the middle. Diagnose and prescribe

**2 try-it problems**, same freedom and same condition.

### 5. `correlation-is-not-causation`

**Able to:** Explain why correlation alone can't establish causation, identify lurking variables and other explanations, and know what evidence CAN support causal claims.

**The idea that carries it:** Four explanations for every correlation: A→B, B→A, lurking C, or chance. Only randomized assignment can cut through — until then, say 'associated'.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Letting a big r settle a causal argument.
- Overcorrecting into 'correlation means nothing'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tv-l5-w1` — Ice-cream sales and drownings: $r \approx 0.9$ across weeks. Name the lurking variable and the test that would expose it.
- `tv-l5-w2` — "Students with tutors score higher — tutoring works!" Give the lurking-variable and reverse-causation counter-stories.
- `tv-l5-w3` — A hospital's data: patients given the strongest medication die more often. Should the medication be banned?

**2 try-it problems**, same freedom and same condition.

### 6. `two-variable-capstone`

**Able to:** Run complete two-variable analyses: plot → describe → r → line → residuals → prediction with range limits → honest causal framing.

**The idea that carries it:** Plot → describe → r → fit → interpret → residuals → bounded predictions → honest causal language: eight gated steps, one actionable paragraph.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Skipping steps because the data 'looks fine'.
- Delivering the equation instead of the paragraph.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `tv-l6-w1` — Café data ($60$ days, temps $18$–$36$°C): cloud positive-linear-strong, $r = 0.88$, line $\hat{y} = -50 + 9x$ (drinks from °C), residuals patternless,
- `tv-l6-w2` — Midway through the analysis, one day shows $35°$ and only $12$ drinks (a pipe burst; the café closed early). It sits far below the line. Apply the pip
- `tv-l6-w3` — The owner asks: "So heat CAUSES my sales — should I install heaters outside in winter?" Answer with the unit's full honesty.

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
| size | **хэмжээ** | ministry standard |
| scale | **томсгох** | already on the site |
| line | **шулуун** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| slope | **налалт** | ministry standard |
| limit | **хязгаар** | already on the site |
| square | **квадрат** | ministry standard |
| unit | **нэгж** | ministry standard |
| vertical | **босоо** | ministry standard |
| outlier | **онцгой утга** | already on the site |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |
| form | **хэлбэр** | ministry standard |
| second | **хоёр дахь** | ministry standard |
| pattern | **хэв маяг** | already on the site |
| direction | **чиглэл** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

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
## scatterplots

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED tv-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY tv-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## correlation

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED tv-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY tv-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`tv-l1-w1` and so on) exactly
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

