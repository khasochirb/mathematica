# MN authoring brief — Introduction to Functions

**Topic** `algebra-1/functions` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/functions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `relations-and-functions`

**Able to:** Decide whether a relation (as a set of pairs, a table, a mapping, or a graph) is a function, using the one-output rule and the vertical line test.

**The idea that carries it:** Function = every input gets exactly one output; on a graph, no vertical line may hit the curve twice.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Rejecting $\{(1, 4), (2, 4)\}$ because the output 4 repeats.
- Applying a horizontal line test to check for a function.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al41-we1` — Is $\{(2, 3), (5, 7), (2, 9), (8, 3)\}$ a function?
- `al41-we2` — A table pairs each student ID with that student's height. Is height a function of ID? Is ID a function of height?

**2 try-it problems**, same freedom and same condition.

### 2. `function-notation`

**Able to:** Evaluate functions written in f(x) notation (at numbers and at expressions) and solve f(x) = k for the input.

**The idea that carries it:** f(3) means 'run machine f on input 3'; f(x) = k asks which input produces output k — evaluating and solving are the two directions of one notation.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f(3)$ as '$f$ times 3.'
- Answering $f(x) = 29$ with the output ('29') instead of the input.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al42-we1` — For $g(x) = x^2 - 3x + 1$, find $g(-2)$ and $g(0)$.
- `al42-we2` — For $f(x) = 4x - 7$, solve $f(x) = 29$.

**2 try-it problems**, same freedom and same condition.

### 3. `domain-and-range`

**Able to:** Find the domain and range of a function from a set of pairs, a graph, or a real-world context, and spot inputs a formula must exclude.

**The idea that carries it:** Domain = allowed inputs (watch zero denominators, negative radicands, and context); range = outputs actually produced — the graph's shadows on the two axes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Swapping the two: reporting outputs as the 'domain.'
- Giving the range of $y = x^2$ as 'all real numbers.'

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al43-we1` — Find the domain of $f(x) = \dfrac{5}{2x - 8}$.
- `al43-we2` — A drone flies for at most 25 minutes on a full battery, and its height is modeled by $h(t)$ for $0 \le t \le 25$, with heights from 0 up to a peak of 

**2 try-it problems**, same freedom and same condition.

### 4. `interpreting-graphs`

**Able to:** Read function graphs qualitatively: intercepts, increasing/decreasing intervals, maxima/minima, and translate features into real-world sentences.

**The idea that carries it:** Intercepts, rising/falling stretches, and peaks are the vocabulary; the axes' units turn them into true sentences about the situation.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading a rising distance–time graph as 'going uphill.'
- Confusing where the maximum IS with what it EQUALS.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al44-we1` — A water tank's volume $V(t)$ (liters, $t$ in minutes) starts at $V(0) = 200$, falls to 80 at $t = 6$, stays flat until $t = 10$, then falls to 0 at $t
- `al44-we2` — For $f(x) = x^2 - 4x + 3$: find $f(0)$, the $x$-intercepts, and the minimum point.

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
| translate | **хөрвүүлэх** | already on the site |
| feature | **шинж** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| formula | **томьёо** | ministry standard |
| table | **хүснэгт** | ministry standard |
| vertical | **босоо** | ministry standard |
| interval | **завсар** | ministry standard |
| graph | **график** | ministry standard |
| algebra | **алгебр** | ministry standard |
| stretch | **сунгалт** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

**feature** — proposed **шинж**

> Split by sense in production: "шинж" where it means a property of the data, but "That sensitivity is a feature AND a warning" → "давуу тал" (advantage). As a term label "шинж" is the one to keep; the "давуу тал" line is prose, not a term, and needs no change.

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
## relations-and-functions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al41-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al41-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## function-notation

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al42-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al42-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al41-we1` and so on) exactly
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

