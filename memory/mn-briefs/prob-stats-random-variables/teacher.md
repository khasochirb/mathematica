# MN authoring brief — Random Variables & Expected Value

**Topic** `prob-stats/random-variables` · **7 lessons** · 21 worked examples · 10 practice · 7 test-yourself

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
> `prob-stats/random-variables`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `random-variables-and-distributions`

**Able to:** Define random variables, build their probability distributions from sample spaces, and verify distributions sum to 1.

**The idea that carries it:** A random variable numbers the outcomes; its distribution table (values + probabilities summing to 1) is its complete description.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Listing the VALUES as if equally likely.
- Skipping the sum-to-1 audit.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l1-w1` — Two coins are flipped; $X = $ number of heads. Build the distribution of $X$.
- `rv-l1-w2` — Two dice are rolled; $X = $ the sum. Find $P(X = 7)$, $P(X = 2)$, and $P(X \ge 10)$.
- `rv-l1-w3` — A distribution is proposed: $P(X{=}1) = 0.2$, $P(X{=}2) = 0.5$, $P(X{=}3) = 0.4$. Diagnose it.

**2 try-it problems**, same freedom and same condition.

### 2. `expected-value`

**Able to:** Compute E(X) = Σ x·P(x), interpret it as the long-run average, and locate it as the distribution's balance point.

**The idea that carries it:** E(X) = Σ x·P(x): probability-weighted average = long-run per-play value = the distribution's balance point.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the values without the weights.
- Expecting the expected value.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l2-w1` — Compute the expected value of one fair die roll.
- `rv-l2-w2` — The raffle: $100$ tickets, one $50{,}000$₮ prize. Find the expected winnings per $1000$₮ ticket, and the expected NET.
- `rv-l2-w3` — $X = $ number of heads in two coin flips. Find $E(X)$ from the distribution.

**2 try-it problems**, same freedom and same condition.

### 3. `fair-games`

**Able to:** Price games with expected value: compute expected net, define fairness, and quantify the house edge.

**The idea that carries it:** Fair means E(net) = 0 — fee equals expected winnings; the shortfall is the house edge, and it compounds forever.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Judging a game by its best case.
- Forgetting the fee is paid on every play.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l3-w1` — Carnival game: pay $500$₮, roll a die, win $100$₮ $\times$ roll. Find the player's expected net and the fair fee.
- `rv-l3-w2` — A wheel has $10$ equal sectors: one pays $2000$₮, two pay $500$₮, the rest pay nothing. What entry fee makes the game fair?
- `rv-l3-w3` — A bet pays even money ($+x$ or $-x$) on "at least one six in two dice". Using $P = \frac{11}{36}$, find the player's expected net per $360$₮ staked.

**2 try-it problems**, same freedom and same condition.

### 4. `variance-and-spread`

**Able to:** Compute Var(X) = E[(X−μ)²] and SD, and interpret them as the distribution's risk/spread.

**The idea that carries it:** Var(X) = Σ(x−μ)²P(x) = E(X²) − μ²; σ = √Var puts spread back in the variable's own units.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging raw deviations.
- Reporting variance in place of SD.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l4-w1` — Plan A pays $+100$ always; Plan B pays $+1100$ or $-900$, each with probability $\frac{1}{2}$. Verify equal means, then compute each SD.
- `rv-l4-w2` — $X = $ heads in two coin flips. Compute Var$(X)$ and $\sigma$ via the shortcut.
- `rv-l4-w3` — One fair die: compute Var$(X)$ with the shortcut, given $E(X) = \frac{7}{2}$.

**2 try-it problems**, same freedom and same condition.

### 5. `linearity-of-expectation`

**Able to:** Use linearity — E(aX + b) = aE(X) + b and E(X + Y) = E(X) + E(Y) — to compute expectations without rebuilding distributions.

**The idea that carries it:** E(aX + b) = aE(X) + b and E(X+Y) = E(X) + E(Y) — the latter without ANY independence requirement; counts decompose into indicator sums.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Demanding independence for E(X + Y).
- Pushing expectation through nonlinear formulas.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l5-w1` — Taxi fare: $2000$₮ flag plus $1500$₮/km; ride length $X$ has $E(X) = 6$ km. Find the expected fare.
- `rv-l5-w2` — Find the expected sum of two dice — then of ten dice.
- `rv-l5-w3` — A quiz has $8$ questions; a guesser is right on each with probability $\frac{1}{4}$. Find the expected number correct — via indicators.

**2 try-it problems**, same freedom and same condition.

### 6. `decisions-with-expected-value`

**Able to:** Analyze real decisions — insurance, warranties, lotteries, business choices — with expected value AND spread, and know when EV alone misleads.

**The idea that carries it:** Compute EV to price the choice; check the worst branch to see if EV is even the right judge — repeated & affordable follows EV, ruinous tails justify paying to delete them.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Applying long-run EV logic to a one-shot ruinous bet.
- Buying every negative-EV comfort.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l6-w1` — Insurance: premium $120{,}000$₮/year against a $1\%$-chance $8{,}000{,}000$₮ loss. Compute both sides' expected values, and say why a rational person 
- `rv-l6-w2` — A $25{,}000$₮ extended warranty covers a $2\%$-chance $300{,}000$₮ repair. Analyze it.
- `rv-l6-w3` — A food stall chooses: location A nets $200{,}000$₮/day rain or shine; location B nets $500{,}000$₮ on dry days but $-100{,}000$₮ on rainy ones. With $

**2 try-it problems**, same freedom and same condition.

### 7. `the-distribution-function`

**Able to:** Read and build F(x) = P(X ≤ x), convert between a distribution table and its running totals, and extract interval probabilities via F(b) − F(a).

**The idea that carries it:** F(x) = P(X ≤ x) is the running total of probability; any interval costs one subtraction: P(a < X ≤ b) = F(b) − F(a).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating F(x) as P(X = x).
- Wrong endpoint bookkeeping in F(b) − F(a).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `rv-l7-w1` — $X$ takes the values $1, 2, 3$ with probabilities $\frac{1}{4}, \frac{1}{2}, \frac{1}{4}$. Build the distribution function and read off $P(X \le 2)$.
- `rv-l7-w2` — A random variable has distribution function $F(x) = 0$ for $x \le 0$, $F(x) = \frac{x}{4}$ for $0 < x \le 4$, and $F(x) = 1$ for $x > 4$. Find $P(3 < 
- `rv-l7-w3` — With $F(x) = \frac{x}{3}$ on $0 < x \le 3$ (and $0$ before, $1$ after), find $P(1 < X \le 3)$.

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
| count | **тоолох** | ministry standard |
| scale | **томсгох** | already on the site |
| edge | **ирмэг** | already on the site |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| probability | **магадлал** | ministry standard |
| spread | **тархалт** | ministry standard |
| number | **тоо** | ministry standard |
| sample | **түүвэр** | already on the site |
| unit | **нэгж** | ministry standard |
| even | **тэгш** | ministry standard |
| subtraction | **хасалт** | already on the site |
| table | **хүснэгт** | ministry standard |
| interval | **завсар** | ministry standard |
| point | **цэг** | ministry standard |
| total | **нийт** | already on the site |
| average | **дундаж** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

**edge** — proposed **ирмэг**

> POLYSEMOUS, mildly. ирмэг is the edge of a solid (shipped and ЭШ alike) and, by extension, the edge of a histogram bin («ирмэг: $20$ нь $20$–$29$-ийг эхлүүлнэ») — that is the sense proposed here. Where "edge" means the margin of something written or laid out, shipped uses зах: "Line up the decimal points, not the right edges" → «Аравтын цэгүүдийг зэрэгцүүл, баруун захыг биш». So: ирмэг for geometry and bins, зах for the right-hand edge of a written column.

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
## random-variables-and-distributions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED rv-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY rv-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## expected-value

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED rv-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY rv-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`rv-l1-w1` and so on) exactly
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

