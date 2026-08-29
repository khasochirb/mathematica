# MN authoring brief — The Binomial Distribution

**Topic** `prob-stats/binomial-distribution` · **6 lessons** · 18 worked examples · 8 practice · 6 test-yourself

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
> `prob-stats/binomial-distribution`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `bernoulli-trials`

**Able to:** Model yes/no experiments as Bernoulli trials and verify the four binomial-setting conditions before using any formula.

**The idea that carries it:** Bernoulli trial = one yes/no with probability p; binomial setting = BINS (binary, independent, fixed n, same p) — verify before you compute.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying binomial formulas to without-replacement draws from small pools.
- Letting 'success' mean 'good'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bd-l1-w1` — A basketball player hits free throws with $p = 0.8$, and attempts exactly $10$ in practice. Check BINS for $X = $ number of makes.
- `bd-l1-w2` — Five cards are dealt WITHOUT replacement; $X = $ number of hearts. Is this binomial?
- `bd-l1-w3` — A factory line produces parts with a $3\%$ defect rate; an inspector samples $20$ parts from a huge batch. Model $X = $ defect count.

**2 try-it problems**, same freedom and same condition.

### 2. `the-binomial-formula`

**Able to:** Derive and apply P(X = k) = C(n,k) p^k (1−p)^(n−k), understanding each factor's job.

**The idea that carries it:** P(X=k) = C(n,k) p^k (1−p)^(n−k): the choose counts the scripts, the powers price one script.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the choose factor.
- Mismatched exponents.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bd-l2-w1` — Five free throws at $p = 0.8$: find $P(\text{exactly } 2 \text{ makes})$.
- `bd-l2-w2` — A fair coin is flipped $6$ times. Find $P(\text{exactly } 3 \text{ heads})$.
- `bd-l2-w3` — A die is rolled $4$ times. Find $P(\text{exactly one six})$.

**2 try-it problems**, same freedom and same condition.

### 3. `binomial-in-action`

**Able to:** Answer at-least/at-most/between binomial questions efficiently, choosing between direct terms and the complement.

**The idea that carries it:** Cumulative = sum of exact terms; compute the smaller side, reach for 1 − P(none) on every 'at least one', and read inclusive/exclusive twice.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Complementing 'at least one' as 'at least one failure'.
- Off-by-one on 'more than' vs 'at least'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bd-l3-w1` — A die is rolled $5$ times. Find $P(\text{at least one six})$.
- `bd-l3-w2` — A batch passes inspection if a $10$-part sample contains AT MOST $1$ defective. With true defect rate $p = 0.1$, find $P(\text{pass})$.
- `bd-l3-w3` — The airline: $52$ tickets, $50$ seats, show-up $p = 0.95$. Which terms give $P(\text{overbooked})$, and what's the expected number of shows?

**2 try-it problems**, same freedom and same condition.

### 4. `mean-and-shape`

**Able to:** Use E(X) = np and Var(X) = np(1−p), and predict a binomial's shape (symmetric vs skewed) from p.

**The idea that carries it:** E = np, Var = np(1−p): atoms add. Shape follows p (symmetric at ½, skewed toward the rare side), and μ ± 2σ frames what's 'usual'.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using np(1−p) as the SD.
- Judging percentages without n.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bd-l4-w1` — Ten free throws at $p = 0.8$: find the mean, SD, and usual range of makes.
- `bd-l4-w2` — A fair coin flipped $100$ times: mean, SD, and the usual range of heads.
- `bd-l4-w3` — Compare shapes: $n = 10$ with $p = 0.1$, $p = 0.5$, $p = 0.9$. Where does each pile its probability?

**2 try-it problems**, same freedom and same condition.

### 5. `simulation-and-surprise`

**Able to:** Design simulations of binomial experiments, and judge surprising claims by computing how often chance alone matches them.

**The idea that carries it:** Model faithfully, repeat plenty, and judge claims by P(at least this extreme | boring explanation) — computed exactly when you can, simulated when you can't.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Judging by P(exact outcome).
- Simulating with the wrong p.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bd-l5-w1` — Compute the psychic's tail exactly: $P(X \ge 8)$ for $n = 10$ fair-coin calls.
- `bd-l5-w2` — Design a simulation (random digits $0$–$9$) for: a $30\%$ free-throw shooter attempts $5$ shots; estimate $P(\text{at least } 3 \text{ makes})$. Then 
- `bd-l5-w3` — A factory's defect rate is supposedly $2\%$. Today's sample of $50$ contains $4$ defects. Frame the surprise computation — is the line drifting?

**2 try-it problems**, same freedom and same condition.

### 6. `binomial-capstone`

**Able to:** Solve full-stack binomial problems end to end: verify the setting, compute the relevant terms, frame with mean/SD, and state honest conclusions.

**The idea that carries it:** BINS → n, p, success → term list → compute → frame with μ ± 2σ → conclude in context. The same six steps run clinics, call centers, and exams.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting a probability without framing it.
- Staffing/planning for the mean.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `bd-l6-w1` — A test has $20$ questions, $4$ options each, pass mark $12$. Show why guessing can't pass: compute $\mu$, $\sigma$, and locate $12$.
- `bd-l6-w2` — A call center takes $200$ calls; $5\%$ escalate. How many escalations should staffing plan for?
- `bd-l6-w3` — A loot box drops a rare item $10\%$ of the time. A player opens $20$ boxes. Find $P(\text{no rare item at all})$ — and the expected count.

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
| complement | **нэмэлт** | already on the site |
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| mean | **дундаж** | ministry standard |
| probability | **магадлал** | ministry standard |
| spread | **тархалт** | ministry standard |
| number | **тоо** | ministry standard |
| formula | **томьёо** | ministry standard |
| proportion | **пропорц** | already on the site |
| problem | **бодлого** | ministry standard |
| direct | **шууд** | already on the site |
| side | **тал** | ministry standard |
| model | **загвар** | ministry standard |
| none | **ямар ч үгүй** | already on the site |
| answer | **хариулт** | already on the site |
| distribution | **тархалт** | ministry standard |
| at least | **дор хаяж** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## bernoulli-trials

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED bd-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY bd-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-binomial-formula

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED bd-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY bd-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`bd-l1-w1` and so on) exactly
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

