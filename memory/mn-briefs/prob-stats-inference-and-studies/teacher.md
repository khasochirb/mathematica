# MN authoring brief — Sampling, Studies & Inference

**Topic** `prob-stats/inference-and-studies` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/inference-and-studies`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `populations-and-samples`

**Able to:** Distinguish populations from samples, and use random selection methods (SRS, stratified, systematic) that earn a sample the right to speak.

**The idea that carries it:** Population = who you want to know about; sample = who you measured; only a random MECHANISM licenses the leap between them — method beats size.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling any casual selection 'random'.
- Chasing sample size over sample method.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-l1-w1` — A principal wants the average daily screen time of the school's $1{,}200$ students and surveys $80$. Name the population, sample, and a legitimate sel
- `in-l1-w2` — The school is $60\%$ middle-schoolers and $40\%$ high-schoolers, and screen habits likely differ by level. Improve the SRS with stratification — what 
- `in-l1-w3` — A factory samples every $25$th phone from the day's production line of $5{,}000$. How many get tested, and when is this systematic method sound?

**2 try-it problems**, same freedom and same condition.

### 2. `bias-in-sampling`

**Able to:** Recognize the major bias species — convenience, voluntary response, undercoverage, nonresponse, response bias — and predict each one's direction.

**The idea that carries it:** Bias is a method-tilt that data volume can't fix; name the species AND predict the direction.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Believing a big biased sample over a small clean one.
- Stopping at 'that's biased'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-l2-w1` — The call-in tax poll ($84\%$ opposed) vs the proper survey ($50$–$50$). Name the bias and explain the gap's direction.
- `in-l2-w2` — A city studies commute satisfaction by polling at downtown parking garages, 8–9 AM. Diagnose ALL the biases you can, with directions.
- `in-l2-w3` — Two phrasings: "Do you support protecting children from dangerous online content?" vs "Do you support government censorship of the internet?" — same p

**2 try-it problems**, same freedom and same condition.

### 3. `experiments-vs-observation`

**Able to:** Distinguish observational studies from experiments, and use the design pillars: random assignment, control groups, placebo, and blinding.

**The idea that carries it:** Random assignment balances ALL lurkers and buys causation; control + placebo + blinding guard the comparison; random selection separately buys generalization.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling any study with two groups an 'experiment'.
- Confusing the two randomnesses.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-l3-w1` — Design the tutoring experiment properly for $100$ volunteer students.
- `in-l3-w2` — Why does a serious drug trial need a placebo group AND blinding — isn't a no-treatment control enough?
- `in-l3-w3` — "Smokers get lung cancer at many times the non-smoker rate" comes from observational data — no one randomly assigns smoking. Why is the causal conclus

**2 try-it problems**, same freedom and same condition.

### 4. `sampling-variability`

**Able to:** Understand that sample statistics wobble around the population truth, and that the wobble shrinks predictably as 1/√n.

**The idea that carries it:** Sample statistics wobble around the truth — unbiased under random sampling, with spread shrinking as 1/√n: quadruple the sample, halve the wobble.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating one sample's number as the truth.
- Expecting wobble to shrink linearly with n.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-l4-w1` — A population is truly $p = 0.5$. For samples of $n = 25$ and $n = 100$, compute the SD of the sample proportion.
- `in-l4-w2` — Two class samples from the $50\%$-girl school: $11$ of $20$ ($55\%$) and $58$ of $100$ ($58\%$). Which deviation from $50\%$ is more surprising?
- `in-l4-w3` — A pollster with $n = 400$ wants half the current wobble. What sample size — and what does it cost?

**2 try-it problems**, same freedom and same condition.

### 5. `margin-of-error`

**Able to:** Compute the quick margin of error 1/√n, interpret poll intervals, and judge claims of difference against the margin.

**The idea that carries it:** MOE ≈ 1/√n at 95%: estimate ± margin is the plausible range; leads inside the margin are ties; and bias lives outside the ± entirely.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Declaring a leader inside the margin.
- Reading ±3 as a guarantee.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-l5-w1` — Compute the quick margin of error for polls of $n = 400$, $1000$, and $2500$.
- `in-l5-w2` — Poll: A $52\%$, B $48\%$, $n = 1000$ (MOE $\pm 3.2$). Is A's lead real?
- `in-l5-w3` — A shampoo ad: "$90\%$ of users recommend!" — based on $n = 30$ mailed-in warranty cards. Attack with both tools.

**2 try-it problems**, same freedom and same condition.

### 6. `inference-capstone`

**Able to:** Judge real claims end to end: check the sampling method, compute the expected wobble under the claim, locate the evidence, and deliver calibrated verdicts.

**The idea that carries it:** Audit → assume → compute wobble → locate in SDs → calibrated verdict → assumptions stated: the whole course in one recipe.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing the z before auditing the sampling.
- Binary verdicts.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in-l6-w1` — The juice claim: $p = 0.8$; your SRS of $50$ finds $\hat{p} = 0.64$. Run the recipe.
- `in-l6-w2` — A coin used for stadium kickoffs shows $60$ heads in $100$ flips. The groundskeeper wants it destroyed. Verdict?
- `in-l6-w3` — A wellness influencer: "In my poll ($n = 2000$), $78\%$ of followers who bought the supplement report more energy!" Deliver the complete professional 

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
| volume | **эзлэхүүн** | ministry standard |
| data | **өгөгдөл** | ministry standard |
| spread | **тархалт** | ministry standard |
| sample | **түүвэр** | already on the site |
| proportion | **пропорц** | already on the site |
| halve | **хагаслах** | already on the site |
| interval | **завсар** | ministry standard |
| difference | **ялгавар** | ministry standard |
| quadratic | **квадрат** | ministry standard |
| divide | **хуваах** | ministry standard |
| statistic | **статистик** | ministry standard |
| direction | **чиглэл** | ministry standard |
| the whole | **бүхэл** | ministry standard |
| capstone | **нэгтгэх хичээл** | already on the site |

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
## populations-and-samples

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED in-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY in-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## bias-in-sampling

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED in-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY in-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`in-l1-w1` and so on) exactly
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

