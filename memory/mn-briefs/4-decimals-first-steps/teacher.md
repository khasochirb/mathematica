# MN authoring brief — Decimals — First Steps

**Topic** `4/decimals-first-steps` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `4/decimals-first-steps`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `tenths-and-hundredths`

**Able to:** Read and write tenths and hundredths, name the value of each decimal digit, and tell 0.5 from 0.05 — the zero that holds a decimal place.

**The idea that carries it:** The decimal point marks the ones; the place-value ladder continues right of it, dividing by ten per step — tenths, then hundredths. Digit × place still tells the value.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading 0.35 as "thirty-five" — ignoring the point.
- Treating 0.5 and 0.05 as the same number.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5dc-l1-we1` — Break $1.35$ into wholes, tenths and hundredths, and write it as a single fraction.
- `g5dc-l1-we2` — Compare the values of the $5$ in $0.5$ and in $0.05$.

**2 try-it problems**, same freedom and same condition.

### 2. `decimals-and-fractions`

**Able to:** Convert decimals to fractions and back, using equivalent fractions to reach denominators of 10 or 100, and simplify the results.

**The idea that carries it:** The last decimal place names the denominator (tenths or hundredths); equivalent fractions carry any friendly fraction onto the staircase and back.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing 0.7 as 7/100 — grabbing the wrong denominator.
- Turning 1/4 into 0.14 — writing the fraction's digits into decimal places.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5dc-l2-we1` — Write $0.25$ and $0.6$ as fractions in simplest form.
- `g5dc-l2-we2` — Write $\frac{3}{4}$ and $\frac{7}{20}$ as decimals.

**2 try-it problems**, same freedom and same condition.

### 3. `comparing-and-ordering-decimals`

**Able to:** Compare and order decimals by aligning places (padding with trailing zeros), and place decimals between their neighbours on the number line.

**The idea that carries it:** Pad with trailing zeros until the places match, then compare left to right — the whole-number 'longer is bigger' rule is dead right of the point.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Longer decimal = bigger number — 0.47 > 0.5 "because 47 > 5".
- Comparing decimal parts as whole numbers across different lengths — 0.8 vs 0.75 read as 8 vs 75.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5dc-l3-we1` — Compare $0.5$ and $0.47$.
- `g5dc-l3-we2` — Order from smallest to largest: $3.09$, $3.9$, $3.19$.

**2 try-it problems**, same freedom and same condition.

### 4. `adding-and-subtracting-decimals`

**Able to:** Add and subtract decimals by aligning the decimal point, padding with zeros where needed — including subtracting decimals from whole numbers.

**The idea that carries it:** Align the decimal points, pad to equal length, then add or subtract exactly as with whole numbers — carries and borrows trade by tens on both sides of the point.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Right-aligning the numbers like whole-number addition — 2.35 + 1.4 becoming 2.35 + 0.14.
- Dropping the decimal point from the answer — 2.35 + 1.40 = 375.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5dc-l4-we1` — Add $2.35 + 1.4$, and show what the right-alignment error would have produced.
- `g5dc-l4-we2` — Subtract $5 - 1.36$.

**2 try-it problems**, same freedom and same condition.

### 5. `rounding-and-measuring-with-decimals`

**Able to:** Round decimals to the nearest whole and nearest tenth, convert measurements (metres–centimetres) through decimals, and estimate with rounded decimals.

**The idea that carries it:** Round decimals with the same landmark-and-digit rule, one staircase further down; unit conversions are place shifts; rounded estimates still guard every computation.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Rounding 3.47 to the nearest tenth by looking at the tenths digit itself.
- Converting 1.35 m to 1,035 cm — treating the decimal digits as already-centimetres.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5dc-l5-we1` — Round $3.47$ to the nearest tenth, and to the nearest whole.
- `g5dc-l5-we2` — A board is $1.35$ m long. How many centimetres is that — and how many centimetres short of $2$ m?

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
| tens | **аравт** | already on the site |
| fraction | **бутархай** | ministry standard |
| line | **шулуун** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| shift | **шилжүүлэх** | ministry standard |
| point | **цэг** | ministry standard |
| side | **тал** | ministry standard |
| subtracting | **хасах** | ministry standard |
| length | **урт** | ministry standard |
| subtract | **хасах** | ministry standard |
| digit | **цифр** | already on the site |
| ones | **нэгж** | ministry standard |
| equal | **тэнцүү** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

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
## tenths-and-hundredths

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5dc-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5dc-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## decimals-and-fractions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5dc-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5dc-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g5dc-l1-we1` and so on) exactly
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

