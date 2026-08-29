# MN authoring brief — Probability Models

**Topic** `prob-stats/probability-models` · **7 lessons** · 21 worked examples · 10 practice · 7 test-yourself

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
> `prob-stats/probability-models`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `probability-as-counting`

**Able to:** Compute probabilities of equally-likely outcomes as favorable-count over total-count, using the Act One toolkit for both counts.

**The idea that carries it:** P = favorable/total for equally likely outcomes — two Act One counts of the SAME universe, stacked.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Counting the numerator and denominator in different universes.
- Trusting 'two outcomes, so 50-50'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-l1-w1` — A random $2$-topping pizza is built from $8$ toppings. What is the probability it includes mushrooms?
- `pb-l1-w2` — Two dice are rolled. What is the probability the sum is $8$?
- `pb-l1-w3` — A $4$-digit PIN is chosen at random (digits $0$–$9$, repeats allowed). What is the probability all four digits are different?

**2 try-it problems**, same freedom and same condition.

### 2. `events-and-complements`

**Able to:** Treat events as sets of outcomes, and compute P(not A) = 1 − P(A), especially for at-least-one events.

**The idea that carries it:** Events are outcome-sets; P(not A) = 1 − P(A), and 'at least one' flips to the single count 'none'.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Complementing only part of the description.
- Subtracting from the wrong side: P(A) − 1.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-l2-w1` — Two dice are rolled. Find $P(\text{at least one six})$.
- `pb-l2-w2` — A family plans $4$ children. Assuming boy/girl equally likely, find $P(\text{at least one girl})$.
- `pb-l2-w3` — A $5$-card hand is dealt. Find $P(\text{at least one ace})$ as a formula and evaluate it as a fraction of hands.

**2 try-it problems**, same freedom and same condition.

### 3. `the-addition-rule`

**Able to:** Compute P(A or B) with the addition rule, recognizing when the overlap term vanishes (mutually exclusive events).

**The idea that carries it:** P(A or B) = P(A) + P(B) − P(A and B); the overlap term is 0 exactly when the events are mutually exclusive.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding probabilities of overlapping events.
- Assuming events with probabilities summing over 1 are impossible.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-l3-w1` — One card is drawn. Find $P(\text{king or heart})$.
- `pb-l3-w2` — One die is rolled. Find $P(\text{even or greater than } 4)$.
- `pb-l3-w3` — In a class, $P(\text{plays music}) = 0.45$, $P(\text{plays sport}) = 0.60$, and $P(\text{plays both}) = 0.25$. Find the probability a random student p

**2 try-it problems**, same freedom and same condition.

### 4. `tables-and-venn`

**Able to:** Organize joint information in Venn diagrams and two-way tables, then read off any probability — unions, overlaps, 'only's, and neithers.

**The idea that carries it:** Fill the overlap first; the four regions sum to the total, and every probability becomes a region lookup.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the full set size into the 'only' region.
- Confusing 'exactly one' with 'or'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-l4-w1` — Of $100$ students: $60$ have a bike, $45$ a skateboard, $25$ both. Build the Venn regions and find $P(\text{neither})$.
- `pb-l4-w2` — From the same survey, find $P(\text{exactly one of the two})$.
- `pb-l4-w3` — A school of $200$: $110$ study English, $80$ study Japanese, $150$ study at least one. Fill the table and find how many study BOTH.

**2 try-it problems**, same freedom and same condition.

### 5. `combinatorial-probability`

**Able to:** Compute probabilities of unordered draws using combinations in both layers of the fraction, including quota and at-least events.

**The idea that carries it:** Unordered draws: chooses upstairs and down — quota products for exact counts, complement for at-least, and exact-counts sum to 1.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Mixing an unordered numerator with an ordered denominator.
- Computing 'at least one defective' by locking one defective in.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-l5-w1` — A box holds $8$ good and $4$ defective phones. Three are drawn at random. Find $P(\text{all good})$.
- `pb-l5-w2` — Same box, same draw. Find $P(\text{exactly one defective})$.
- `pb-l5-w3` — A $5$-card hand is dealt. Find $P(\text{all five are the same suit — a flush, counting straight flushes too})$.

**2 try-it problems**, same freedom and same condition.

### 6. `odds-and-the-long-run`

**Able to:** Convert between odds and probability, and interpret probability as long-run relative frequency with expected counts.

**The idea that carries it:** Odds a:b ↔ P = a/(a+b); probability is a long-run frequency — expected count ≈ nP, with no memory and no due-ness.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading odds a:b as probability a/b.
- Believing a result is 'due'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pb-l6-w1` — A horse's odds are $3$:$1$ against. Find the implied probability of winning — and of losing.
- `pb-l6-w2` — One die: express $P(\text{roll a } 6)$ as odds in favor.
- `pb-l6-w3` — A basketball player makes $70\%$ of her free throws. In a season of $250$ attempts, how many makes should the team expect — and should anyone panic if

**2 try-it problems**, same freedom and same condition.

### 7. `geometric-probability`

**Able to:** Compute probabilities for uniformly random positions as ratios of lengths or areas, including composite shaded regions.

**The idea that carries it:** For a uniformly random position, probability = favorable measure ÷ total measure — length on a line, area in the plane.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing radii instead of areas.
- Forgetting what the total region is.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pm-l7-w1` — A bus passes every $12$ minutes and you arrive at a random moment. What is the probability you wait at most $3$ minutes?
- `pm-l7-w2` — Two circles share a centre, with radii $4$ and $6$. A point is chosen at random inside the big circle. Find the probability it lies inside the small c
- `pm-l7-w3` — Concentric circles of radii $4$ and $6$ are cut into quarters by two perpendicular diameters. One quarter of the inner disk and the opposite quarter o

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
| complement | **нэмэлт** | already on the site |
| count | **тоолох** | ministry standard |
| scale | **томсгох** | already on the site |
| measure | **хэмжих** | ministry standard |
| area | **талбай** | ministry standard |
| fraction | **бутархай** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| probability | **магадлал** | ministry standard |
| line | **шулуун** | ministry standard |
| product | **үржвэр** | ministry standard |
| sample | **түүвэр** | already on the site |
| counting | **тоолох** | ministry standard |
| plane | **хавтгай** | ministry standard |
| addition | **нэмэх** | ministry standard |
| table | **хүснэгт** | ministry standard |
| model | **загвар** | ministry standard |
| none | **ямар ч үгүй** | already on the site |
| position | **байрлал** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**complement** — proposed **нэмэлт**

> Two live senses in production and neither is in the ministry standard: an angle's complement is «нэмэлт» (21×, with supplement = «дүүргэгч», 13×), an event's complement is «гүйцээлт» (7×, «$A$ үзэгдлийн **гүйцээлт**»). Needs two keys. Also note «нэмэлт» is what one shipped string uses for "addition" — see that entry.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

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
## probability-as-counting

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pb-l1-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pb-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## events-and-complements

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pb-l2-w1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pb-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pb-l1-w1` and so on) exactly
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

