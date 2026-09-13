# MN authoring brief — Addition & Subtraction to 1000

**Topic** `2/addition-and-subtraction-to-1000` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `2/addition-and-subtraction-to-1000`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `adding-tens-and-hundreds`

**Able to:** Add and subtract whole hundreds and whole tens mentally, explain which column moves, and handle the case where a column fills up and spills into the next one.

**The idea that carries it:** Adding a whole hundred or a whole ten changes just one column — and if that column would go past nine, ten of it trades up for one of the column to its left.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding a hundred to the wrong column — turning 240 + 300 into 270.
- Writing 12 in the tens column — answering 280 + 40 as 2120.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3as-l1-we1` — Work out $240 + 300$ in your head, and say which digits moved.
- `g3as-l1-we2` — Work out $280 + 40$ in your head.

**2 try-it problems**, same freedom and same condition.

### 2. `column-addition`

**Able to:** Add two three-digit numbers by columns, carry a ten when the ones column passes nine, and check the answer by adding the parts a second way.

**The idea that carries it:** Column addition adds each place separately, and a carry is simply ten of one column arriving in the next as a single unit.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the whole 13 in the ones column, giving 156 + 237 = 3813.
- Forgetting to add the carried 1 into the next column, giving 383.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3as-l2-we1` — Add $156 + 237$ in columns.
- `g3as-l2-we2` — Add $324 + 145$ in columns.

**2 try-it problems**, same freedom and same condition.

### 3. `column-subtraction`

**Able to:** Subtract a three-digit number from another by columns, break a ten or a hundred when a column is short, and prove every answer with a receipt.

**The idea that carries it:** Subtraction breaks bundles down — one ten becomes ten ones — and every answer must pay its receipt: what is left plus what was taken must equal what you started with.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Turning 2 − 8 upside down and writing 6, because "8 take away 2 is easier".
- Breaking a ten but forgetting to reduce the tens digit, subtracting from 4 tens instead of 3.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3as-l3-we1` — Work out $342 - 128$ in columns, and give the receipt.
- `g3as-l3-we2` — Work out $475 - 231$ in columns.

**2 try-it problems**, same freedom and same condition.

### 4. `fact-families-and-missing-numbers`

**Able to:** Write the four facts of a whole-and-parts family, use them to find a missing number in an addition or subtraction, and say which operation undoes which.

**The idea that carries it:** Every pair of parts and their whole make four facts. A missing part is found by subtracting; a missing whole is found by adding.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding when the whole is already known — answering ? + 30 = 140 with 170.
- Writing 140 − 60 = 80 and then claiming 60 − 140 is also in the family.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3as-l4-we1` — Write the four facts of the family for $60$, $80$ and $140$.
- `g3as-l4-we2` — Find the missing number: $? + 30 = 140$.

**2 try-it problems**, same freedom and same condition.

### 5. `word-problems`

**Able to:** Decide from the words whether a problem joins or splits, solve it in one or two steps, and check that the answer makes sense in the story.

**The idea that carries it:** Read the story first and decide whether it joins or splits, then calculate — and finally ask whether an answer that size makes sense for the story.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding every number in the story, so 300, 120 and 50 become 470.
- Stopping at the middle number of a two-step problem and answering 180.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g3as-l5-we1` — A dairy sells $120$ litres of milk in the morning and $90$ in the afternoon. How much altogether?
- `g3as-l5-we2` — Saruul has $300$ tögrög. She spends $120$ on bread, then her aunt gives her $50$. How much does she have now?

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
| size | **хэмжээ** | ministry standard |
| tens | **аравт** | already on the site |
| hundreds | **зуут** | already on the site |
| number | **тоо** | ministry standard |
| unit | **нэгж** | ministry standard |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| problem | **бодлого** | ministry standard |
| hundred | **зуу** | already on the site |
| second | **хоёр дахь** | ministry standard |
| subtracting | **хасах** | ministry standard |
| part | **хэсэг** | ministry standard |
| answer | **хариулт** | already on the site |
| pair | **хос** | ministry standard |
| subtract | **хасах** | ministry standard |
| digit | **цифр** | already on the site |
| column | **багана** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

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
## adding-tens-and-hundreds

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g3as-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g3as-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## column-addition

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g3as-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g3as-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g3as-l1-we1` and so on) exactly
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

