# MN authoring brief — Linear Inequalities

**Topic** `algebra-1/inequalities` · **4 lessons** · 8 worked examples · 8 practice · 6 test-yourself

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
> `algebra-1/inequalities`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `solving-and-graphing-inequalities`

**Able to:** Solve one- and two-step inequalities, apply the flip rule when multiplying or dividing by a negative, and graph solutions on a number line.

**The idea that carries it:** Solve inequalities like equations, but FLIP the symbol whenever you multiply or divide both sides by a negative — then graph with open/closed circle and a ray.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the flip: $-2x > 6 \to x > -3$.
- Flipping when merely subtracting a negative-looking term.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al31-we1` — Solve $4x - 7 \le 9$ and describe the graph.
- `al31-we2` — Solve $5 - 2x > 11$.

**2 try-it problems**, same freedom and same condition.

### 2. `multi-step-inequalities`

**Able to:** Solve inequalities with variables on both sides and parentheses, and translate 'at least / at most' situations into inequalities.

**The idea that carries it:** Run the equation pipeline with the flip rule armed, translate 'at least/at most' to ≥/≤, and let the context trim the solution set.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Translating 'at least 8' as $x > 8$.
- Reporting $s \le 6.4$ sessions as the final answer.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al32-we1` — Solve $2(3x - 5) < 4x + 8$.
- `al32-we2` — A tutoring service charges a \$30 registration fee plus \$25 per session. Bilguun's budget is at most \$180. How many sessions can he take?

**2 try-it problems**, same freedom and same condition.

### 3. `compound-inequalities`

**Able to:** Solve 'and' (between) and 'or' compound inequalities and graph their solution sets.

**The idea that carries it:** 'And' = intersection (a segment; operate on all three parts at once); 'or' = union (two outward rays; solve each piece separately).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Operating on only two of the three parts of $-1 \le 2x + 3 < 9$.
- Writing an 'or' answer as a single between-statement: '$x < -3$ or $x \ge 4$' as $4 \le x < -3$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al33-we1` — Solve $-5 \le 3x + 1 < 10$.
- `al33-we2` — Solve: $2x + 1 < -5$ or $3x - 4 \ge 8$.

**2 try-it problems**, same freedom and same condition.

### 4. `absolute-value-equations-and-inequalities`

**Able to:** Solve absolute-value equations and inequalities by translating them into distance statements, and recognize the no-solution cases.

**The idea that carries it:** Read |X| as distance: |X| = k splits into ±k; |X| < k is the segment between; |X| > k is the rays beyond — and a negative right side means no solutions (or all).

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Solving $|2x - 3| = 7$ with only the positive branch.
- Turning $|X| > k$ into $-k < X < k$.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `al34-we1` — Solve $|2x - 3| = 7$.
- `al34-we2` — A machine fills bottles to $v$ ml with target 500 and tolerance 5: $|v - 500| \le 5$. What volumes pass?

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
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| circle | **тойрог** | ministry standard |
| number | **тоо** | ministry standard |
| distance | **зай** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| graph | **график** | ministry standard |
| algebra | **алгебр** | ministry standard |
| linear | **шугаман** | ministry standard |
| segment | **хэрчим** | already on the site |
| side | **тал** | ministry standard |
| part | **хэсэг** | ministry standard |
| answer | **хариулт** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**translate** — proposed **хөрвүүлэх**

> Words→symbols sense only; one shipped string instead says «болго». The geometry verb is «параллель зөөх» (MoE 10.11) and the two must not merge — same English word, two Mongolian verbs.

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
## solving-and-graphing-inequalities

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al31-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al31-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## multi-step-inequalities

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED al32-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY al32-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`al31-we1` and so on) exactly
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

