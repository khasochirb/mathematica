# MN authoring brief — Transformations of Graphs

**Topic** `precalculus/transformations-of-graphs` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `precalculus/transformations-of-graphs`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `vertical-and-horizontal-shifts`

**Able to:** Graph f(x) + k and f(x − h) as translations of a parent graph, and read h and k from a formula — including the counterintuitive inside sign.

**The idea that carries it:** Outside the function moves up/down as written; inside the parentheses moves left/right OPPOSITE to the sign: f(x − h) + k puts the landmark at (h, k).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f(x + 5)$ as a shift RIGHT 5 because the sign is positive.
- Shifting the vertex but redrawing the arms at a new steepness.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc21-we1` — Describe how to obtain $g(x) = |x - 4| - 2$ from the parent $f(x) = |x|$, and locate the corner.
- `pc21-we2` — The parabola $y = x^2$ is shifted so its vertex sits at $(-3, 5)$. Write the new equation and find its $y$-intercept.

**2 try-it problems**, same freedom and same condition.

### 2. `stretches-and-reflections`

**Able to:** Graph y = a·f(x) as a vertical stretch/compression, handle the reflections y = −f(x) and y = f(−x), and read |a| and sign separately.

**The idea that carries it:** a·f(x) scales outputs (x-axis points pinned); the sign of a flips over the x-axis, f(−x) flips over the y-axis — sign and size are separate decisions.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Sliding the whole graph when multiplying: moving the roots of y = 2f(x).
- Treating −f(x) and f(−x) as the same flip.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc22-we1` — The point $(2, 6)$ lies on $y = f(x)$. Find its image on $y = \tfrac{1}{2}f(x)$, on $y = -f(x)$, and on $y = f(-x)$.
- `pc22-we2` — Describe $g(x) = -2(x - 1)^2 + 8$ as transformations of $x^2$, and find its $x$-intercepts.

**2 try-it problems**, same freedom and same condition.

### 3. `combining-transformations`

**Able to:** Graph functions of the form a·f(x − h) + k by applying transformations in the correct order, and write equations from described transformations or graphs.

**The idea that carries it:** In a·f(x − h) + k, transform inside-out: shift horizontally, then stretch/flip, then shift vertically; a landmark point maps to (x₀ + h, a·y₀ + k).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding k before multiplying by a: turning −2f(x) + 3 into −2(f(x) + 3).
- Reading a's sign from the vertex position ('vertex is high, so a is positive').

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc23-we1` — Graph $g(x) = -2(x + 1)^2 + 8$ by tracking the vertex and one neighbouring point of $y = x^2$.
- `pc23-we2` — A graph is the parent $|x|$ flipped over the x-axis, stretched by 3, and moved to corner $(2, 5)$. Write $g(x)$ and compute $g(4)$.

**2 try-it problems**, same freedom and same condition.

### 4. `piecewise-and-absolute-value-graphs`

**Able to:** Evaluate and graph piecewise-defined functions with correct open/closed endpoints, and rewrite |x| expressions as piecewise formulas.

**The idea that carries it:** Evaluate piecewise functions by finding which rule owns the input; graph each rule on its own territory with honest open/closed endpoints; |x| is the two-rule function x / −x split at 0.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Evaluating f(1) with every rule and reporting several answers.
- Drawing both boundary dots closed at a jump.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `pc24-we1` — For $f(x) = \begin{cases} 2x + 5 & x < -1 \\ x^2 - 2 & -1 \le x \le 2 \\ 6 - x & x > 2 \end{cases}$, evaluate $f(-3)$, $f(-1)$, $f(2)$, and $f(4)$.
- `pc24-we2` — Rewrite $g(x) = |x - 3|$ as a piecewise formula and evaluate both pieces' expressions at their shared boundary.

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
| shape | **дүрс** | ministry standard |
| size | **хэмжээ** | ministry standard |
| scale | **томсгох** | already on the site |
| absolute value | **абсолют утга** | already on the site |
| equation | **тэгшитгэл** | ministry standard |
| function | **функц** | ministry standard |
| formula | **томьёо** | ministry standard |
| vertical | **босоо** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| graph | **график** | ministry standard |
| point | **цэг** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| vertex | **орой** | ministry standard |
| stretch | **сунгалт** | already on the site |
| sign | **тэмдэг** | ministry standard |
| reflect | **тэгш хэмээр хувиргах** | ministry standard |
| reflection | **тэгш хэмээр хувиргах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

**scale** — proposed **томсгох**

> POLYSEMOUS — three different Mongolian words, so state which you mean. (1) The verb "to scale (up)" = томсгох, which this entry proposes: it is dominant across the ratios, percent and decimal-division units. Its opposite is багасгах (scale down), and shipped once writes өсгөх instead («scale up from a friendly percent» → «нөхөрсөг хувиас өсгө») — a stray; prefer томсгох. (2) The noun "scale" of a map or a scale factor = масштаб: «масштабын коэффициент» = scale factor, «$1:1$ масштабтай» = at scale 1:1. (3) A balance scale = жинлүүр («Тэнцвэрийн жинлүүрийг төсөөл»). Confidence is medium only because of this three-way split, not because томсгох is in doubt.

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
## vertical-and-horizontal-shifts

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc21-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc21-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## stretches-and-reflections

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED pc22-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY pc22-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`pc21-we1` and so on) exactly
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

