# MN authoring brief — Probability & Counting

**Topic** `10/probability-and-counting` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `10/probability-and-counting`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `the-counting-principle`

**Able to:** Count multi-stage choices with the multiplication principle, with and without repetition allowed.

**The idea that carries it:** Stages multiply: m × n × p total outcomes. Repetition keeps stages full; no-repetition shrinks them by one each time.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding the stages: 3 shirts + 2 pants = 5 outfits.
- Forgetting stages shrink when repetition is banned.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc1-we1` — A cafe offers 4 mains, 3 drinks, and 2 desserts. How many different meals?
- `pc1-we2` — How many 4-digit PINs are possible? How many with no repeated digit?
- `pc1-we3` — License plates: 2 letters then 3 digits. How many plates?

**2 try-it problems**, same freedom and same condition.

### 2. `permutations`

**Able to:** Count ordered arrangements with factorials and the permutation formula $_nP_r = \frac{n!}{(n-r)!}$.

**The idea that carries it:** n! arranges everything; nPr = n!/(n−r)! arranges r of n. Use when ORDER MATTERS.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing $_nP_r$ as $n \cdot r$ or $n^r$.
- Believing $0! = 0$.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc2-we1` — How many ways can 5 books be arranged on a shelf?
- `pc2-we2` — 8 sprinters, 3 medals (gold/silver/bronze): how many podiums?
- `pc2-we3` — A club of 10 picks a president, then a vice-president. How many outcomes?

**2 try-it problems**, same freedom and same condition.

### 3. `combinations`

**Able to:** Count unordered selections with $_nC_r = \frac{n!}{r!(n-r)!}$, and choose correctly between permutations and combinations.

**The idea that carries it:** nCr = n! / (r!(n−r)!): permutations with the r! orderings divided out. Use when order doesn't matter.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using a permutation for an order-blind choice.
- Forgetting to divide by $r!$ (not $2$, not $r$).

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc3-we1` — How many ways to choose 2 of 5 friends?
- `pc3-we2` — A team of 4 from a class of 10: how many teams?
- `pc3-we3` — From 8 candidates: (a) president + VP, (b) two equal reps. Count each.

**2 try-it problems**, same freedom and same condition.

### 4. `probability-basics`

**Able to:** Compute probabilities as favorable/total for equally likely outcomes, use the 0-to-1 scale, and apply the complement rule.

**The idea that carries it:** P = favorable/total (equally likely!), lives in [0,1]; P(not A) = 1 − P(A).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using favorable/UNfavorable instead of favorable/total.
- Applying favorable/total to outcomes that are NOT equally likely.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc4-we1` — One die: find $P(5)$ and $P(\text{even})$.
- `pc4-we2` — A standard deck (52 cards): $P(\text{heart})$? $P(\text{not a heart})$?
- `pc4-we3` — A bag holds 3 red, 5 blue, 2 green marbles. $P(\text{blue})$? $P(\text{not green})$?

**2 try-it problems**, same freedom and same condition.

### 5. `compound-events`

**Able to:** Multiply probabilities of independent events, adjust for dependence (without replacement), and use the complement for 'at least one'.

**The idea that carries it:** Independent: multiply. Without replacement: update the fractions. 'At least one': 1 − P(none).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding probabilities for 'and': $P(\text{two sixes}) = \tfrac16 + \tfrac16 = \tfrac13$.
- Forgetting to update fractions without replacement.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc5-we1` — Two dice: $P(\text{both sixes})$?
- `pc5-we2` — Bag: 5 red, 3 blue. Two draws, no replacement: $P(\text{both red})$?
- `pc5-we3` — Two rolls: $P(\text{at least one six})$?

**2 try-it problems**, same freedom and same condition.

### 6. `probability-meets-counting`

**Able to:** Compute probabilities whose favorable and total counts come from the counting principle, permutations, and combinations.

**The idea that carries it:** P = favorable/total with both counts from counting formulas — and the chain rule cross-checks the answer.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Mixing an ordered total with an unordered favorable (or vice versa).
- Forgetting that only EQUALLY LIKELY totals work.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc6-we1` — Mini-lottery: choose 3 of 10 numbers. $P(\text{jackpot})$?
- `pc6-we2` — From 4 girls and 3 boys, a random pair is chosen. $P(\text{both girls})$?
- `pc6-we3` — Four people sit in a random row. $P(\text{Ana and Bat sit together})$?

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
| fraction | **бутархай** | ministry standard |
| probability | **магадлал** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| counting | **тоолох** | ministry standard |
| time | **цаг** | already on the site |
| formula | **томьёо** | ministry standard |
| none | **ямар ч үгүй** | already on the site |
| total | **нийт** | already on the site |
| answer | **хариулт** | already on the site |
| multiply | **үржүүлэх** | ministry standard |
| chain | **давхар функцийн уламжлалын дүрэм** | **proposed — tell us if it is wrong** |
| at least | **дор хаяж** | already on the site |
| definition | **тодорхойлолт** | ministry standard |

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
## the-counting-principle

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## permutations

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc1-we1` and so on) exactly
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

