# MN authoring brief — Multiplication & Division

**Topic** `4/multiplication-and-division` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `4/multiplication-and-division`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `multiplying-by-one-digit`

**Able to:** Multiply multi-digit numbers by a one-digit number using expanded form and the column method, and multiply by tens, hundreds and thousands using the trailing-zeros shortcut.

**The idea that carries it:** One factor visits every place of the other: multiply each part, add the results. The column method is this idea written tightly, and trailing zeros just shift places.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to ADD the carry into the next column's product.
- Dropping trailing zeros — 4 × 700 = 28.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5md-l1-we1` — Compute $4 \times 2\,357$ by multiplying the parts.
- `g5md-l1-we2` — Compute $6 \times 1\,845$ with the column method.

**2 try-it problems**, same freedom and same condition.

### 2. `multiplying-by-two-digits`

**Able to:** Multiply two multi-digit numbers using partial products and the column layout, multiplying by the tens digit with its place shift.

**The idea that carries it:** Split the second factor into tens and ones, multiply by each (the tens product shifted one place), and add the two partial products.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting the shift on the tens row — writing 24 × 3 instead of 24 × 30.
- Multiplying tens by tens and ones by ones only — 24 × 36 as 20×30 + 4×6.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5md-l2-we1` — Compute $24 \times 36$ with partial products.
- `g5md-l2-we2` — Compute $138 \times 26$.

**2 try-it problems**, same freedom and same condition.

### 3. `division-with-remainders`

**Able to:** Divide with remainders, state answers as quotient and remainder, verify with the receipt (quotient × divisor + remainder = dividend), and insist the remainder stays smaller than the divisor.

**The idea that carries it:** Division finds how many whole shares fit and what's left: quotient × divisor + remainder = dividend, with the remainder always smaller than the divisor.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Leaving a remainder as big as the divisor — 50 ÷ 6 = 7 r 8.
- Checking with multiplication but forgetting the remainder — 9 × 8 = 72 ≠ 75, "so it's wrong".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5md-l3-we1` — Compute $75 \div 8$ and check the answer.
- `g5md-l3-we2` — A claim says $50 \div 6 = 7$ remainder $8$. Judge it.

**2 try-it problems**, same freedom and same condition.

### 4. `long-division`

**Able to:** Divide multi-digit numbers by a one-digit divisor with the long-division cycle, keep the zeros a quotient needs, and carry remainders correctly.

**The idea that carries it:** Divide-multiply-subtract-bring-down, one place at a time, leftovers sliding right — and every quotient digit gets written, zeros included.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Skipping the zero when a step divides to nothing — 3,048 ÷ 6 = 58.
- Losing a step's remainder instead of sliding it into the next place.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5md-l4-we1` — Compute $5\,208 \div 4$ by long division.
- `g5md-l4-we2` — Compute $3\,675 \div 7$.

**2 try-it problems**, same freedom and same condition.

### 5. `choosing-the-operation`

**Able to:** Choose multiplication or division (or both, with addition and subtraction) from a story's structure, and interpret remainders: round up, drop, or report.

**The idea that carries it:** Structure picks the operation — repeated equal groups multiply, sharing and grouping divide — and the story, not the arithmetic, decides what the remainder means.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Answering the bare division when the story needs the remainder interpreted — "3 buses" for 130 students.
- Multiplying whenever numbers look big and dividing when they look small.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5md-l5-we1` — A school orders $12$ boxes of $145$ pencils and shares them equally among $29$ classes. How many pencils does each class receive?
- `g5md-l5-we2` — $130$ students travel by $40$-seat buses. How many buses are needed?

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
| factor | **хуваагч** | ministry standard |
| tens | **аравт** | already on the site |
| hundreds | **зуут** | already on the site |
| thousands | **мянгат** | already on the site |
| mean | **дундаж** | ministry standard |
| division | **хуваалт** | ministry standard |
| product | **үржвэр** | ministry standard |
| multiplication | **үржүүлэх** | ministry standard |
| number | **тоо** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| zero | **тэг** | ministry standard |
| time | **цаг** | already on the site |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| remainder | **үлдэгдэл** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| quotient | **ногдвор** | ministry standard |
| form | **хэлбэр** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

**hundreds** — proposed **зуут**

> POLYSEMOUS. As a place value, hundreds = зуут, "the hundreds place" = зуутын орон — the ЭШ papers give the full series «зуутын, аравтын, нэгжийн орон», which is the authority to follow. The quantity phrase "hundreds of X" is not зуут but хэдэн зуун / олон зуун: shipped "hundreds of thousands of inequalities" → «хэдэн зуун мянган тэнцэтгэл биш», "many hundreds of rolls" → «олон зуун хаялт». (зуут also turns up in the percent etymology line «зуут ногдох» = per hundred, which is unrelated.)

**thousands** — proposed **мянгат**

> POLYSEMOUS, and the one genuinely unsupported entry in this batch — treat it as a proposal to confirm with the owner. (1) As a place value, "thousands" should be мянгат by regular formation from the attested нэгж / аравт / зуут series (мянгатын орон = the thousands place), but no published source in this repo actually writes it, hence low. (2) The only shipped evidence given with this term is a different sense — "(in thousands)" as a reporting unit — where the mirror writes the instrumental «(мянгаар)»: "Nine salaries of $300$ (in thousands)" → «$300$ (мянгаар)-ийн есөн цалин». Do not promote мянгаар to the term; it is a case form, not the place. (3) "thousands of X" is again хэдэн мянган («хэдэн зуун мянган тэнцэтгэл биш»). Note the decimal counterpart мянганы (thousandths) IS attested and is a different word — see "tenths"/"hundredths".

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
## multiplying-by-one-digit

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5md-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5md-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## multiplying-by-two-digits

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5md-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5md-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g5md-l1-we1` and so on) exactly
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

