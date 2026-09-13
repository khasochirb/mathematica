# MN authoring brief — Functions & Transformations

**Topic** `algebra-2/functions-and-transformations` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-2/functions-and-transformations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `function-notation-domain-and-range`

**Able to:** Evaluate functions fluently (numbers, expressions, and nested calls), and read domain and range restrictions from formulas.

**The idea that carries it:** f(x) is a machine: substitute the whole input, and read domain from what the formula forbids (zero denominators, negative even roots).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing $f(a+1)$ by tacking $+1$ onto $f(a)$.
- Giving the domain of $\sqrt{x-5}$ as $x > 5$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a211-we1` — For $f(x) = 2x^2 - 3x + 1$, compute $f(4)$, $f(-2)$, and $f(a+1)$.
- `a211-we2` — Find the domain of $g(x) = \dfrac{x+1}{x^2 - 9}$ and $h(x) = \sqrt{2x - 8}$.

**2 try-it problems**, same freedom and same condition.

### 2. `transformations-of-functions`

**Able to:** Read h, k, a in g(x) = a·f(x − h) + k as graph moves: horizontal/vertical shifts, reflection, and vertical stretch/compression.

**The idea that carries it:** Inside the parentheses moves the graph horizontally (sign reversed); outside moves it vertically; a out front flips and stretches — one parent shape, four dials.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f(x + 3)$ as a shift RIGHT 3.
- Applying the vertical shift before the stretch in $y = 2f(x) + 1$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a212-we1` — Describe $g(x) = (x + 4)^2 - 3$ as transformations of $y = x^2$, and give its vertex.
- `a212-we2` — The graph of $f(x) = \sqrt{x}$ is flipped over the x-axis, stretched vertically by 2, and shifted right 1 and up 6. Write $g(x)$ and find where it cro

**2 try-it problems**, same freedom and same condition.

### 3. `absolute-value-functions-and-equations`

**Able to:** Graph absolute value functions via transformations, and solve absolute value equations and inequalities by the two-branch method.

**The idea that carries it:** Absolute value is distance: equations split into two branches after isolating, < makes an AND sandwich, > makes two OR tails, and |A| = negative is impossible.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Splitting before isolating: from $2|x-1| + 3 = 11$ writing $2(x-1) + 3 = \pm 11$.
- Solving $|x + 2| = -6$ by splitting into two equations anyway.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a213-we1` — Solve $2|x - 1| + 3 = 11$.
- `a213-we2` — A bolt is acceptable if its diameter $d$ satisfies $|d - 10| \le 0.2$ (mm). Solve the inequality and interpret.

**2 try-it problems**, same freedom and same condition.

### 4. `piecewise-functions`

**Able to:** Evaluate, graph, and write piecewise-defined functions, handling boundary points and open/closed endpoints correctly.

**The idea that carries it:** One function, several territories: check which condition the input satisfies, apply only that rule, and give every boundary to exactly one piece (filled dot owns, open circle disowns).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Evaluating every piece and reporting several outputs.
- Giving a boundary point to both pieces (two filled dots stacked).

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `a214-we1` — For $f(x) = \begin{cases} 2x + 5 & x < 0 \\ 5 - x & 0 \le x \le 4 \\ 1 & x > 4 \end{cases}$, compute $f(-3)$, $f(0)$, $f(4)$, and $f(10)$.
- `a214-we2` — A taxi charges a $4 flag fee covering the first 2 km, then $1.50 per km after. Write the fare $C(d)$ as a piecewise function and price a 7 km ride.

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
| absolute value | **абсолют утга** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| circle | **тойрог** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| even | **тэгш** | ministry standard |
| formula | **томьёо** | ministry standard |
| vertical | **босоо** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**absolute value** — proposed **абсолют утга**

> SENSE SPLIT, per Khas, 26 Aug 2026. These are not three renderings of one term — they are different things:
  • the VALUE  → «абсолют утга» or «үнэмлэхүй утга» (both correct)
  • the straight brackets | | → «модул» (the notation itself)
  • an absolute-value EQUATION → «модулт тэгшитгэл»
  • taking |x| of a number → «тооноос модул авах»
So the site's 'three ways' is not an inconsistency and needs no sweep. The earlier finding that ministry 12.1's «модул» should replace «абсолют утга» was WRONG: 12.1 is about modulus equations, which is the bracket sense.
  → this entry: the value. «үнэмлэхүй утга» is equally correct.

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
## function-notation-domain-and-range

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a211-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a211-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## transformations-of-functions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED a212-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY a212-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`a211-we1` and so on) exactly
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

- **Функц ба хувиргалт (11-р анги)** (primary)

So write for a student meeting this for the first time *and* for an exam
candidate sent back to repair a gap.

