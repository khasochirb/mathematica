# MN authoring brief — Applications of Integrals

**Topic** `calculus/applications-of-integrals` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `calculus/applications-of-integrals`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `area-between-curves`

**Able to:** Compute areas between curves by integrating (top − bottom), finding intersection points for the limits when needed.

**The idea that carries it:** Area between curves = ∫ (top − bottom) dx, walls at the given limits or at the intersections — and check who's on top before you integrate.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Integrating (bottom − top) and reporting a negative 'area.'
- Using the axis as one wall out of habit.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal61-we1` — Find the area enclosed between $y = x$ and $y = x^2$.
- `cal61-we2` — Find the area enclosed between $y = 4 - x^2$ and $y = x + 2$.

**2 try-it problems**, same freedom and same condition.

### 2. `motion-and-net-change`

**Able to:** Recover displacement and total distance from velocity, and apply the net-change idea to any rate.

**The idea that carries it:** ∫v dt = displacement (signed); ∫|v| dt = total distance (split at the turnarounds); and in general, the integral of any rate is the net change.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reporting displacement when the question asked how far the particle traveled.
- Computing total distance by |∫v| — absolute value OUTSIDE the integral.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal62-we1` — A particle moves with $v(t) = 6 - 2t$ m/s on $[0, 4]$. Find its displacement and its total distance.
- `cal62-we2` — Water flows into a tank at $R(t) = 2t$ liters per minute. How much water accumulates in the first 5 minutes — and why is this an integral?

**2 try-it problems**, same freedom and same condition.

### 3. `average-value`

**Able to:** Compute the average value of a function on an interval and interpret it geometrically.

**The idea that carries it:** f_avg = (1/(b−a)) ∫ₐᵇ f dx — the level the area would settle to; continuous functions genuinely attain it somewhere on the interval.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Averaging the endpoint values: (f(a) + f(b))/2.
- Forgetting the 1/(b − a): reporting the integral as the average.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal63-we1` — Find the average value of $f(x) = x^2$ on $[0, 3]$, and the point where $f$ attains it.
- `cal63-we2` — A particle's velocity is $v(t) = 6t^2$ m/s. Show its average VALUE on $[0, 2]$ equals the average VELOCITY computed from positions.

**2 try-it problems**, same freedom and same condition.

### 4. `the-capstone`

**Able to:** Chain the full course — limits, derivatives, curve analysis, and integrals — through complete multi-part problems.

**The idea that carries it:** Limits → f′ → f″ → sketch → integrate: one pipeline; and every chained answer cross-checks another.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Answering a 'how much accumulates' question with a derivative (or 'where is it largest' with an integral).
- Carrying an early arithmetic error through the whole chain unchecked.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal64-we1` — For $f(x) = 4x - x^2$: find where $f$ is largest, the area under its arch (between its roots), and its average value there. Then run the audit: does m
- `cal64-we2` — A particle has velocity $v(t) = t^2 - 4t + 3$ on $[0, 3]$. When does it change direction, what is its displacement, and what total distance does it co

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
| area | **талбай** | ministry standard |
| function | **функц** | ministry standard |
| rate | **хурдац** | already on the site |
| limit | **хязгаар** | already on the site |
| distance | **зай** | ministry standard |
| derivative | **уламжлал** | ministry standard |
| formula | **томьёо** | ministry standard |
| interval | **завсар** | ministry standard |
| point | **цэг** | ministry standard |
| problem | **бодлого** | ministry standard |
| part | **хэсэг** | ministry standard |
| total | **нийт** | already on the site |
| answer | **хариулт** | already on the site |
| average | **дундаж** | ministry standard |

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
## area-between-curves

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal61-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal61-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## motion-and-net-change

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal62-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal62-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cal61-we1` and so on) exactly
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

