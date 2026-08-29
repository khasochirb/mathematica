# MN authoring brief — Applications of Derivatives

**Topic** `calculus/applications-of-derivatives` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `calculus/applications-of-derivatives`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `tangent-and-normal-lines`

**Able to:** Write equations of tangent and normal lines to a curve at a given point.

**The idea that carries it:** Tangent at a: y − f(a) = f′(a)(x − a); normal swaps the slope for its negative reciprocal — and slope requests are solved by setting f′(x) equal to them.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using f′(x) — the whole formula — as the tangent's slope.
- Building the tangent through the wrong point: (a, 0) or (a, f′(a)).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal41-we1` — Find the tangent line to $f(x) = x^2 - 3x$ at $x = 2$.
- `cal41-we2` — Find the normal line to $f(x) = x^2$ at $(1, 1)$.

**2 try-it problems**, same freedom and same condition.

### 2. `increasing-decreasing-and-critical-points`

**Able to:** Use the sign of f′ to find where a function increases and decreases, locate critical points, and classify them with the First Derivative Test.

**The idea that carries it:** f′'s sign chart tells the whole rise/fall story; peaks and valleys hide only at critical points, and the sign CHANGE across each one classifies it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Declaring every f′ = 0 point a max or min.
- Building the sign chart of f instead of f′.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal42-we1` — For $f(x) = x^3 - 3x$: find the critical points, the intervals of increase/decrease, and classify each critical point.
- `cal42-we2` — Show that $f(x) = x^3$ has a critical point at $x = 0$ that is neither a max nor a min.

**2 try-it problems**, same freedom and same condition.

### 3. `concavity-and-the-second-derivative-test`

**Able to:** Determine concavity and inflection points from f″, and classify critical points with the Second Derivative Test.

**The idea that carries it:** f″ reads the bend: positive cups up, negative domes down, sign-flip = inflection; at a critical point, f″'s sign delivers an instant max/min verdict.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Declaring an inflection point wherever f″ = 0.
- Confusing concave down with decreasing.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal43-we1` — Find the intervals of concavity and the inflection point of $f(x) = x^3 - 6x^2 + 5$.
- `cal43-we2` — Use the Second Derivative Test to classify the critical points of $f(x) = x^3 - 3x$.

**2 try-it problems**, same freedom and same condition.

### 4. `optimization`

**Able to:** Translate word problems into a function of one variable, then find and certify its maximum or minimum with derivatives.

**The idea that carries it:** Name the target, spend the constraint to reach one variable, solve f′ = 0 in the sensible domain, certify with f″ or endpoints — then answer the question actually asked.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Differentiating a formula that still has two variables.
- Reporting the x-value when the question asked for the maximum area (or cost, or volume).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `cal44-we1` — A farmer has 40 m of fence for a rectangular pen. What dimensions maximize the area, and what is that area?
- `cal44-we2` — Find the minimum value of $S = x + \dfrac{100}{x}$ for $x > 0$.

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
| tangent | **шүргэгч** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| increase | **өсөх** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| line | **шулуун** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| slope | **налалт** | ministry standard |
| derivative | **уламжлал** | ministry standard |
| interval | **завсар** | ministry standard |
| point | **цэг** | ministry standard |
| problem | **бодлого** | ministry standard |
| second | **хоёр дахь** | ministry standard |
| answer | **хариулт** | already on the site |
| positive | **эерэг** | ministry standard |
| equal | **тэнцүү** | ministry standard |
| test | **шалгалт** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tangent** — proposed **шүргэгч**

> One English key, two ministry terms: the tangent line is «шүргэгч» (10.7, 11.9; glossary «хөвч, шүргэгч, огтлогч») and the trig function is «тангенс» (11.7, 12.6). Neither appears in production yet, so this can be split cleanly now.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

**increase** — proposed **өсөх**

> POLYSEMOUS by form. The intransitive "increase / be increasing" is өсөх — ministry, glossary and shipped all agree, and its opposite is буурах. But the noun "an increase" is өсөлт, which is what the percent unit actually ships: «Хувиар өсөлт ба бууралт» = Percent Increase & Decrease, «$25\%$-ийн өсөлт» = a 25% increase. And the transitive "increase something" is ихэсгэх/өсгөх («гурав дахин ихэсгэвэл»). So: өсөх for a quantity rising or a function increasing, өсөлт for the measured increase, ихэсгэх when a person increases a value. Do not use нэмэгдэх (which shipped uses for parts adding up across the origin) as a synonym for the function property.

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
## tangent-and-normal-lines

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal41-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal41-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## increasing-decreasing-and-critical-points

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED cal42-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY cal42-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`cal41-we1` and so on) exactly
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

- **Уламжлалын хэрэглээ (12-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

