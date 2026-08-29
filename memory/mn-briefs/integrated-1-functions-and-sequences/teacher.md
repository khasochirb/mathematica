# MN authoring brief — Functions & Sequences

**Topic** `integrated-1/functions-and-sequences` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/functions-and-sequences`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `what-is-a-function`

**Able to:** Decide whether a relation given as a set of pairs, a table, a graph or a rule is a function, and justify the decision with the one-output rule or the vertical line test.

**The idea that carries it:** One input, exactly one output. On a graph that means no vertical line meets the curve twice. Outputs may repeat freely; inputs may not.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Calling {(1,5), (2,5), (3,5)} 'not a function' because the output repeats.
- Applying a horizontal line test to decide whether a graph is a function.
- Assuming any equation in x and y defines y as a function of x.
- Listing a repeated value twice in the range.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u3-l1-we1` — Is the relation $\{(1, 4), (2, 7), (3, 4), (5, 9)\}$ a function? Give its domain and range.
- `im1-u3-l1-we2` — Is the relation $\{(2, 3), (4, 1), (2, 8), (6, 5)\}$ a function?
- `im1-u3-l1-we3` — Does the equation $x = y^2$ define $y$ as a function of $x$?
- `im1-u3-l1-we4` — A shop records $(\text{kg of rice bought}, \text{price paid})$ at $3000$₮ per kg: $(1, 3000), (2, 6000), (3, 9000)$. Is price a function of mass? Is m

**3 try-it problems**, same freedom and same condition.

### 2. `function-notation-domain-and-range`

**Able to:** Read and write function notation, evaluate a function at a numerical or algebraic input, and determine the domain and range from a rule, a graph, or a real situation.

**The idea that carries it:** $f(3)$ is the output at input $3$, never $f$ times $3$. Substitute in brackets. The domain is what may go in — restricted by the arithmetic and, in a model, by the situation; the range is what comes out.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading f(3) as f multiplied by 3.
- Substituting a negative without brackets: writing f(−3) = 2·−3² − 5 = −23.
- Giving a model's domain as 'all real numbers' because the formula allows it.
- Replacing only the first x when evaluating f(x + 1).

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u3-l2-we1` — For $f(x) = 2x^2 - 5$, find $f(3)$, $f(-3)$ and $f(0)$.
- `im1-u3-l2-we2` — For $g(x) = 3x - 4$, find $g(x + 1)$ and simplify. Then find $g(x+1) - g(x)$.
- `im1-u3-l2-we3` — State the domain of $f(x) = \dfrac{1}{x - 2}$ and of $g(x) = \sqrt{x - 5}$.
- `im1-u3-l2-we4` — A candle is $24$ cm tall and burns $4$ cm per hour, so $h(t) = 24 - 4t$. Find $h(3)$, and state the domain and range that the situation allows.

**3 try-it problems**, same freedom and same condition.

### 3. `arithmetic-sequences`

**Able to:** Recognise an arithmetic sequence by its constant difference, write it both recursively and explicitly, find any term without listing the ones before it, and read the sequence as a linear function on the whole numbers.

**The idea that carries it:** Constant difference $d$. Recursive: $a_n = a_{n-1} + d$. Explicit: $a_n = a_1 + (n-1)d$ — $n-1$ steps, because the first term has taken none. It is a linear function with slope $d$.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using aₙ = a₁ + nd instead of a₁ + (n−1)d.
- Computing d as a₉ − a₄ without dividing by the number of steps.
- Applying the arithmetic formula to a sequence with changing differences.
- Treating the recursive rule as a way to reach a distant term.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u3-l3-we1` — For the sequence $80, 89, 98, 107, \dots$, find the common difference, write the recursive and explicit rules, and find the $12$th term.
- `im1-u3-l3-we2` — An arithmetic sequence has $a_4 = 23$ and $a_9 = 48$. Find $d$, $a_1$, and the explicit rule.
- `im1-u3-l3-we3` — A theatre has $18$ seats in row $1$ and $3$ more in each row after. How many seats in row $20$, and which row first has at least $60$ seats?
- `im1-u3-l3-we4` — Show that $2, 6, 18, 54$ is NOT arithmetic, and identify what kind of pattern it is.

**3 try-it problems**, same freedom and same condition.

### 4. `geometric-sequences`

**Able to:** Recognise a geometric sequence by its constant ratio, write it recursively and explicitly, find any term directly, and see it as the exponential counterpart to the arithmetic sequence.

**The idea that carries it:** Constant ratio $r$. Recursive: $a_n = r\,a_{n-1}$. Explicit: $a_n = a_1 r^{\,n-1}$ — the exponent counts multiplications, and the first term has had none. $r > 1$ grows, $0 < r < 1$ decays.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Using aₙ = a₁ · rⁿ instead of a₁ · r^(n−1).
- Reading 'loses 25% each year' as a ratio of 0.25.
- Testing only the first pair of terms before declaring a sequence geometric.
- Assuming a sequence that grows fast must be geometric.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u3-l4-we1` — For $2, 6, 18, 54, \dots$ find the common ratio, write both rules, and find the $8$th term.
- `im1-u3-l4-we2` — A bacterial culture starts at $500$ cells and doubles every hour. Write the explicit rule for the count after $n$ hours and find the count after $9$ h
- `im1-u3-l4-we3` — A car worth $24\,000\,000$₮ loses a quarter of its value each year. Write the sequence rule and find its value after $3$ years.
- `im1-u3-l4-we4` — Compare $a_n = 3n + 5$ (arithmetic) with $b_n = 3 \cdot 2^{\,n-1}$ (geometric) at $n = 1, 3, 6$ and $10$. Which is bigger, and does that change?

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
| range | **далайц** | ministry standard |
| count | **тоолох** | ministry standard |
| function | **функц** | ministry standard |
| mean | **дундаж** | ministry standard |
| ratio | **харьцаа** | ministry standard |
| exponential | **илтгэгч** | ministry standard |
| line | **шулуун** | ministry standard |
| domain | **тодорхойлогдох муж** | ministry standard |
| slope | **налалт** | ministry standard |
| sequence | **дараалал** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| number | **тоо** | ministry standard |
| time | **цаг** | already on the site |
| exponent | **илтгэгч** | ministry standard |
| table | **хүснэгт** | ministry standard |
| vertical | **босоо** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## what-is-a-function

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u3-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u3-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## function-notation-domain-and-range

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u3-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u3-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u3-l1-we1` and so on) exactly
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

