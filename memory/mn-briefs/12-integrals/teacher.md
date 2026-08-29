# MN authoring brief — Integrals

**Topic** `12/integrals` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `12/integrals`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `undoing-the-derivative`

**Able to:** Find antiderivatives by reversing the power rule, check by differentiating, and understand why every answer carries + C.

**The idea that carries it:** ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C — up by one, divide by the new one, plus the family constant. Differentiate to check: the answer grades itself.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the + C.
- Reversing the rule the wrong way: dividing by the OLD exponent.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in1-we1` — Find $\int x^4\,dx$ and check by differentiating.
- `in1-we2` — Find $\int (3x^2 - 4x + 1)\,dx$.
- `in1-we3` — A particle has $v(t) = 10t$ and starts at position $s(0) = 3$. Find $s(t)$.

**2 try-it problems**, same freedom and same condition.

### 2. `the-area-problem`

**Able to:** Estimate areas under curves with Riemann sums (rectangle sums), and understand that the exact area is the limit as the slices thin.

**The idea that carries it:** Tile the region with n rectangles, sum, and take n → ∞: the Riemann sums squeeze onto the exact area. Accumulating any rate is this same sum in disguise.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using the wrong edge's height for the chosen scheme.
- Expecting the rectangle sum to BE the area.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in2-we1` — Left-endpoint sum for $f(x) = x^2$ on $[0, 2]$ with $n = 4$ slices.
- `in2-we2` — Right-endpoint sum, same setup.
- `in2-we3` — What are these sums converging to? (Sneak preview with the machinery of lesson 4.)

**2 try-it problems**, same freedom and same condition.

### 3. `the-definite-integral`

**Able to:** Read and use definite integral notation, apply linearity/additivity/orientation properties, and handle signed area.

**The idea that carries it:** ∫ᵃᵇ f dx is the Riemann-sum limit: net signed area. It splits over sums, scales by constants, chains over intervals, flips with orientation — and counts below-axis regions negative.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Treating the integral as always-positive area.
- Ignoring the orientation of the limits.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in3-we1` — Evaluate $\int_0^3 2x\,dx$ by geometry.
- `in3-we2` — Evaluate $\int_0^{2\pi} \sin x\,dx$ and explain the answer.
- `in3-we3` — Given $\int_0^5 f = 12$ and $\int_0^2 f = 4$: find $\int_2^5 f$ and $\int_5^0 f$.

**2 try-it problems**, same freedom and same condition.

### 4. `the-fundamental-theorem`

**Able to:** Evaluate definite integrals with the FTC: antidifferentiate, evaluate at both ends, subtract. Understand why area and antiderivatives are linked.

**The idea that carries it:** ∫ᵃᵇ f dx = F(b) − F(a) for any antiderivative F: area and antidifferentiation are one craft. The accumulating area's growth rate is the curve's height — that's the proof in one sliver.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Evaluating F(b) − F(a) in the wrong order.
- Adding + C to a definite integral's answer.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in4-we1` — Evaluate $\int_0^2 x^2\,dx$ — the staircases' target, at last.
- `in4-we2` — Evaluate $\int_1^3 (2x + 1)\,dx$.
- `in4-we3` — Evaluate $\int_0^{\pi} \sin x\,dx$.

**2 try-it problems**, same freedom and same condition.

### 5. `integration-in-practice`

**Able to:** Integrate polynomials, powers, and sin/cos fluently; rewrite integrands first; reverse simple chains like (ax+b)ⁿ by dividing by the inner derivative.

**The idea that carries it:** Rewrite first, integrate on sight, and reverse linear chains by dividing by the inner slope. Diff-check everything — especially the trig signs.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Getting the trig signs backwards.
- Forgetting to divide by the inner slope.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in5-we1` — Find $\int (2x + 1)^3\,dx$ and verify.
- `in5-we2` — Find $\int \sin(3x)\,dx$.
- `in5-we3` — Evaluate $\int_0^4 \sqrt{x}\,dx$ — rewrite first.

**2 try-it problems**, same freedom and same condition.

### 6. `area-and-motion`

**Able to:** Compute areas between curves (top − bottom), and recover distance/position from velocity using definite integrals.

**The idea that carries it:** Between curves: ∫(top − bottom), crossings as limits. Motion: ∫v = displacement (signed), ∫|v| = distance, ∫a = velocity change — the s-v-a stack integrates up and differentiates down.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Integrating top − bottom without checking which is on top.
- Reporting displacement when the question asks distance.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `in6-we1` — Find the area between $y = x$ and $y = x^2$.
- `in6-we2` — A car: $v(t) = 6t$ m/s. How far does it travel in the first 4 seconds?
- `in6-we3` — A ball: $v(t) = 20 - 10t$. Find the displacement AND the total distance over $[0, 4]$.

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
| area | **талбай** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| rate | **хурдац** | already on the site |
| slope | **налалт** | ministry standard |
| limit | **хязгаар** | already on the site |
| proof | **баталгаа** | already on the site |
| distance | **зай** | ministry standard |
| derivative | **уламжлал** | ministry standard |
| growth | **өсөлт** | already on the site |
| interval | **завсар** | ministry standard |
| rectangle | **тэгш өнцөгт** | ministry standard |
| linear | **шугаман** | ministry standard |
| problem | **бодлого** | ministry standard |
| height | **өндөр** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## undoing-the-derivative

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED in1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY in1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-area-problem

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED in2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY in2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`in1-we1` and so on) exactly
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

---

## Who arrives here

The site sends students to this topic when the analytics find a weakness in:

- **Интеграл (12-р анги)** (primary)
- **Интеграл (12-р анги)** (primary)
- **Интеграл (12-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

