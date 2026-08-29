# MN authoring brief — Numbers to 1000

**Topic** `2/numbers-to-1000` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `2/numbers-to-1000`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `hundreds-tens-and-ones`

**Able to:** Say what each digit of a three-digit number is worth, split a number into hundreds, tens and ones, and build a number back from its parts.

**The idea that carries it:** A digit's value is its place. Read a three-digit number as three counts — so many hundreds, so many tens, so many ones — and a zero in a column means that column is empty, not missing.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading every digit as its bare shape — calling the 3 in 342 "three".
- Dropping the zero when writing four hundred and six, giving 46.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3nt-l1-we1` — The flock has $342$ sheep. How many bundles of one hundred, bundles of ten, and loose sheep is that?
- `g3nt-l1-we2` — In the number $353$, what is each $3$ worth?

**2 try-it problems**, same freedom and same condition.

### 2. `reading-and-writing-numbers`

**Able to:** Read a three-digit number aloud in words, write a number from its words, and place a number correctly when the words skip a column.

**The idea that carries it:** Words and digits carry the same three counts. Read left to right, and whenever the words are silent about a column, write a zero there rather than nothing at all.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the teens backwards — hearing "fourteen" and writing 41.
- Writing "six hundred and three" as 63, leaving the empty tens column out.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3nt-l2-we1` — Write "two hundred and seventy-five" in digits.
- `g3nt-l2-we2` — Write "one hundred and fourteen" in digits, and say why it is not $141$.

**2 try-it problems**, same freedom and same condition.

### 3. `comparing-and-ordering`

**Able to:** Compare two three-digit numbers by walking the columns from the left, use the $>$, $<$ and $=$ signs correctly, and put a list of numbers in order.

**The idea that carries it:** Compare from the left and stop at the first column where the digits differ — that column decides, no matter what follows it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Picking the number with the biggest single digit — calling 349 larger than 376 because of the 9.
- Turning the sign the wrong way — writing 258 > 463.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3nt-l3-we1` — Compare $463$ and $258$ with the correct sign.
- `g3nt-l3-we2` — Compare $376$ and $349$.

**2 try-it problems**, same freedom and same condition.

### 4. `counting-in-steps`

**Able to:** Count on and back in steps of $2$, $5$, $10$ and $100$, continue a step pattern, and use the endings of the numbers to check that a count is right.

**The idea that carries it:** Every step count is repeated addition, and every step size leaves a pattern in the digits — so the pattern is a free check on whether your count is right.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Losing a step in the middle of a count — going 5, 10, 20, 25.
- Changing the tens digit when counting on in hundreds — going 246, 356, 466.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3nt-l4-we1` — Count on in fives from $0$, five steps. What do you notice about the endings?
- `g3nt-l4-we2` — Count on in hundreds from $246$, three steps.

**2 try-it problems**, same freedom and same condition.

### 5. `rounding-to-the-nearest-ten`

**Able to:** Round a two- or three-digit number to the nearest ten by finding the tens on either side, decide ties with the halfway rule, and say when a rounded answer is good enough.

**The idea that carries it:** Rounding to the nearest ten means choosing between the two tens a number sits between — the nearer one wins, and an exact halfway goes up by agreement.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Rounding down whenever the ones digit is small-looking, including 5 — turning 35 into 30.
- Changing the hundreds digit when rounding to the nearest ten — turning 362 into 400.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3nt-l5-we1` — Round $47$ to the nearest ten.
- `g3nt-l5-we2` — Round $362$ to the nearest ten.

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
| count | **тоолох** | ministry standard |
| size | **хэмжээ** | ministry standard |
| tens | **аравт** | already on the site |
| hundreds | **зуут** | already on the site |
| mean | **дундаж** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| counting | **тоолох** | ministry standard |
| addition | **нэмэх** | ministry standard |
| side | **тал** | ministry standard |
| hundred | **зуу** | already on the site |
| part | **хэсэг** | ministry standard |
| answer | **хариулт** | already on the site |
| digit | **цифр** | already on the site |
| column | **багана** | already on the site |
| ones | **нэгж** | ministry standard |
| pattern | **хэв маяг** | already on the site |
| sign | **тэмдэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

**hundreds** — proposed **зуут**

> POLYSEMOUS. As a place value, hundreds = зуут, "the hundreds place" = зуутын орон — the ЭШ papers give the full series «зуутын, аравтын, нэгжийн орон», which is the authority to follow. The quantity phrase "hundreds of X" is not зуут but хэдэн зуун / олон зуун: shipped "hundreds of thousands of inequalities" → «хэдэн зуун мянган тэнцэтгэл биш», "many hundreds of rolls" → «олон зуун хаялт». (зуут also turns up in the percent etymology line «зуут ногдох» = per hundred, which is unrelated.)

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
## hundreds-tens-and-ones

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g3nt-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g3nt-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## reading-and-writing-numbers

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g3nt-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g3nt-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g3nt-l1-we1` and so on) exactly
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

