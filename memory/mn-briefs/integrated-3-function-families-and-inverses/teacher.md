# MN authoring brief — Function Families & Inverses

**Topic** `integrated-3/function-families-and-inverses` · **4 lessons** · 12 worked examples · 16 practice · 8 test-yourself

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
> `integrated-3/function-families-and-inverses`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `transformations-of-functions`

**Able to:** Predict how the graph of any function changes under vertical and horizontal shifts, stretches, and reflections, and write the transformed formula from a description.

**The idea that carries it:** Outside the function acts on outputs (vertical, behaves as written); inside acts on inputs (horizontal, behaves in reverse). Those two sentences transform every function family there is.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading f(x - 3) as a shift LEFT because of the minus sign.
- Applying a vertical stretch to only part of the formula.
- Confusing f(-x) with -f(x).
- Moving the vertex but forgetting the flip reverses max and min.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u5-l1-we1` — Describe the transformations that turn $f(x) = |x|$ into $g(x) = -2|x - 3| + 4$, and find the vertex of $g$.
- `im3-u5-l1-we2` — Write the formula for $\sqrt{x}$ shifted left $2$, reflected across the $x$-axis, and raised $5$. Then evaluate it at $x = 2$.
- `im3-u5-l1-we3` — Starting from $f(x) = x^2$, one student stretches vertically by $3$ THEN shifts down $1$; another shifts down $1$ THEN stretches by $3$. Write both fo

**3 try-it problems**, same freedom and same condition.

### 2. `even-and-odd-functions`

**Able to:** Test any formula for even or odd symmetry by computing the function at the opposite input, and connect each outcome to its graph: mirror in the y-axis, or half-turn about the origin.

**The idea that carries it:** Feed the function the opposite input. Same output back: even, a y-axis mirror. Opposite output back: odd, a half-turn about the origin. Anything else: neither.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Testing one value, finding it works, and declaring symmetry.
- Believing every function is either even or odd.
- Dropping the sign when substituting -x into an odd power.
- Confusing odd symmetry with 'the graph looks decreasing'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u5-l2-we1` — Classify $f(x) = x^4 - 3x^2 + 1$ as even, odd, or neither.
- `im3-u5-l2-we2` — Classify $g(x) = x^3 - 5x$ as even, odd, or neither.
- `im3-u5-l2-we3` — Classify $h(x) = x^2 + x$ as even, odd, or neither.

**3 try-it problems**, same freedom and same condition.

### 3. `composition-of-functions`

**Able to:** Evaluate and simplify compositions of two functions, in both orders, and decompose a complicated function into an inner and an outer part.

**The idea that carries it:** A composition is a chain of machines: $(f \circ g)(x) = f(g(x))$, inner first, outer second. Substitute the whole inner formula — in parentheses — and never expect the two orders to agree.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading (f ∘ g) left to right and applying f first.
- Substituting without parentheses.
- Treating (f ∘ g)(x) as f(x) times g(x).
- Assuming f ∘ g = g ∘ f after checking one convenient input.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u5-l3-we1` — For $f(x) = 2x - 3$ and $g(x) = x^2 + 1$, evaluate $(f \circ g)(2)$ and $(g \circ f)(2)$.
- `im3-u5-l3-we2` — For the same $f(x) = 2x - 3$ and $g(x) = x^2 + 1$, find formulas for $(f \circ g)(x)$ and $(g \circ f)(x)$.
- `im3-u5-l3-we3` — Write $h(x) = \sqrt{3x + 4}$ as a composition $f(g(x))$ of two simpler functions, and use the decomposition to evaluate $h(4)$.

**3 try-it problems**, same freedom and same condition.

### 4. `inverse-functions`

**Able to:** Find the inverse of a function algebraically, verify it by composition, read it graphically as a reflection across the line through the origin at $45^\circ$, and decide when an inverse exists.

**The idea that carries it:** An inverse runs the machine backwards: solve for the input, and verify with composition — both $f^{-1}(f(x))$ and $f(f^{-1}(x))$ must simplify all the way to $x$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading f⁻¹(x) as 1 divided by f(x).
- Verifying only one composition order.
- Inverting a function that is not one-to-one without restricting.
- Swapping letters first and then solving for y sloppily.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im3-u5-l4-we1` — Find the inverse of $f(x) = 2x - 5$ and verify it by composition.
- `im3-u5-l4-we2` — Find the inverse of $f(x) = x^3 + 1$, and use it to solve $f(x) = 9$.
- `im3-u5-l4-we3` — Explain why $f(x) = x^2$ has no inverse on all real numbers, and fix it by restricting the domain.

**3 try-it problems**, same freedom and same condition.

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
| half | **хагас** | already on the site |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| polynomial | **олон гишүүнт** | ministry standard |
| symmetry | **тэгш хэм** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| even | **тэгш** | ministry standard |
| formula | **томьёо** | ministry standard |
| vertical | **босоо** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| graph | **график** | ministry standard |
| opposite | **эсрэг** | already on the site |
| second | **хоёр дахь** | ministry standard |
| stretch | **сунгалт** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**half** — proposed **хагас**

> POLYSEMOUS. хагас is the noun "a half" (the quantity 1/2) and is what this entry proposes. But when "half" means one of two parts of a set or a figure, shipped Mongolian uses тал: "half at or below, half at or above" → «тал нь түүнээс дээшгүй, тал нь доошгүй»; "each exactly half the slice" → «тус бүр нь талхны яг тал»; "The triangle is exactly half of it" → «Гурвалжин чинь яг тал нь». Rule of thumb: хагас for the computed amount, тал for one of the two portions. тал is also "side" (of a shape, of an equation), so it carries real ambiguity — prefer хагас wherever the amount is meant.

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
## transformations-of-functions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u5-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u5-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## even-and-odd-functions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im3-u5-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im3-u5-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im3-u5-l1-we1` and so on) exactly
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

