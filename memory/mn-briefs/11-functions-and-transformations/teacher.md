# MN authoring brief — Functions & Transformations

**Topic** `11/functions-and-transformations` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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
> `11/functions-and-transformations`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `function-notation`

**Able to:** Read and evaluate function notation $f(x)$, including expression inputs like $f(a+2)$ and chained evaluations.

**The idea that carries it:** f(x) = the machine f run on input x — one output per input; substitute the whole input everywhere x appears.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f(x)$ as $f \cdot x$ and $f(3)$ as $3f$.
- Substituting an expression input into only ONE of the x's.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fn1-we1` — For $f(x) = 2x + 1$: find $f(3)$, $f(0)$, and $f(-2)$.
- `fn1-we2` — For $f(x) = x^2 - 3x$: find $f(5)$ and $f(a+1)$ (check your formula at $a = 4$).
- `fn1-we3` — With $f(x) = 2x+1$ and $g(x) = x^2$: compute $f(g(3))$ and $g(f(1))$.

**2 try-it problems**, same freedom and same condition.

### 2. `domain-and-range`

**Able to:** Find the domain of a function by excluding division-by-zero and negative-even-root inputs, and read off simple ranges.

**The idea that carries it:** Domain = legal inputs (no ÷0, no √negative). Range = achievable outputs. Read both from the rule's shape.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Excluding values that zero the TOP of a fraction.
- Writing the domain of $\sqrt{x-2}$ as $x > 2$.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fn2-we1` — Domain of $f(x) = \frac{5}{x-3}$?
- `fn2-we2` — Domain of $f(x) = \sqrt{x-2}$?
- `fn2-we3` — Range of $f(x) = x^2 + 3$?

**2 try-it problems**, same freedom and same condition.

### 3. `shifts`

**Able to:** Shift any function's graph with $f(x) + k$ (vertical) and $f(x-h)$ (horizontal), predicting points before plotting.

**The idea that carries it:** Outside = vertical, moves as written; inside = horizontal, moves opposite the sign. Track a point to be sure.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f(x+3)$ as a shift RIGHT 3.
- Mixing floors: treating $f(x) + 3$ as horizontal.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fn3-we1` — $f(x) = x^2$. Where does the vertex land under $g(x) = f(x) + 3$ and $h(x) = f(x-4)$?
- `fn3-we2` — $(2, 5)$ sits on $y = f(x)$. Find its image on $y = f(x) - 2$ and on $y = f(x+1)$.
- `fn3-we3` — Write $y = x^2$ shifted right 2 and up 5, and give one point on it.

**2 try-it problems**, same freedom and same condition.

### 4. `stretches-and-reflections`

**Able to:** Stretch, squash, and reflect graphs with $a \cdot f(x)$ and $f(-x)$, tracking points through each move.

**The idea that carries it:** a·f(x): outputs ×a (stretch/squash/flip-down when negative). f(−x): mirror over the y-axis. Points tell the story.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Scaling x too: sending $(3, 2)$ to $(6, 4)$ under $2f(x)$.
- Confusing the two minus signs.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fn4-we1` — $(3, 2)$ is on $y = f(x)$. Find its image on $y = 4f(x)$ and $y = \tfrac12 f(x)$.
- `fn4-we2` — $(3, 2)$ is on $y = f(x)$. Find its image on $y = -f(x)$ and $y = f(-x)$.
- `fn4-we3` — Show $f(x) = x^2$ is even and $g(x) = x^3$ is odd (test at $x = 2$).

**2 try-it problems**, same freedom and same condition.

### 5. `combining-transformations`

**Able to:** Read and build the full form $y = a\,f(x-h) + k$, applying transformations in a correct order and tracking points through the whole stack.

**The idea that carries it:** y = a·f(x−h) + k: slide (h), scale (a), lift (k) — in that order. Track one point through the whole stack.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Lifting before scaling: computing $2f(x)+1$ as $2(f(x)+1)$.
- Describing $2f(x-3)+1$ as 'right 3, up 1, stretch 2' and stretching the +1.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fn5-we1` — Describe $y = 2(x-3)^2 + 1$ as transformations of $y = x^2$, and give the vertex.
- `fn5-we2` — $(1, 4)$ is on $f$. Track it through $y = 2f(x-3) + 1$.
- `fn5-we3` — Write $\sqrt{x}$ flipped over the x-axis, shifted left 2 and up 5, then evaluate at $x = 2$.

**2 try-it problems**, same freedom and same condition.

### 6. `inverse-functions`

**Able to:** Find inverses of linear (and simple root/quadratic-piece) functions by swap-and-solve, verify by composition, and read the y = x mirror.

**The idea that carries it:** f⁻¹ undoes f: swap x and y, solve for y. Verify with f(f⁻¹(x)) = x; the graphs mirror across y = x.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading $f^{-1}(x)$ as $\tfrac{1}{f(x)}$.
- Undoing operations in the same order they were applied.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `fn6-we1` — Find $f^{-1}$ for $f(x) = 2x + 3$, and verify at $x = 5$.
- `fn6-we2` — Find $f^{-1}$ for $f(x) = \tfrac{x}{4} - 1$.
- `fn6-we3` — $f(x) = x^2$ for $x \ge 0$: find $f^{-1}$ and compute $f^{-1}(49)$.

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
| scale | **томсгох** | already on the site |
| function | **функц** | ministry standard |
| division | **хуваалт** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| zero | **тэг** | ministry standard |
| even | **тэгш** | ministry standard |
| vertical | **босоо** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| graph | **график** | ministry standard |
| linear | **шугаман** | ministry standard |
| point | **цэг** | ministry standard |
| quadratic | **квадрат** | ministry standard |
| opposite | **эсрэг** | already on the site |
| form | **хэлбэр** | ministry standard |
| root | **язгуур** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

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
## function-notation

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED fn1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY fn1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## domain-and-range

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED fn2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY fn2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`fn1-we1` and so on) exactly
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

