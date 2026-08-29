# MN authoring brief — Addition & Subtraction

**Topic** `3/addition-and-subtraction` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `3/addition-and-subtraction`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `column-addition`

**Able to:** Add three- and four-digit numbers in columns — lining up places, adding from the ones, carrying past nine — and check every sum by adding the other way.

**The idea that carries it:** Line up the places, add from the right, and trade every ten upward — then add the other way and make the total repeat.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Lining numbers up on the left — writing the 4 of 47 under the 3 of 385.
- Writing a two-digit column total straight down — a 15 squeezed into the ones column.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4as-l1-we1` — Add $358 + 467$ in columns, then check by adding the other way.
- `g4as-l1-we2` — Add $785 + 649$.

**2 try-it problems**, same freedom and same condition.

### 2. `column-subtraction`

**Able to:** Subtract three- and four-digit numbers with regrouping — including tops with zeros like $503 - 168$ and $3\,005 - 1\,428$ — and prove every answer with the add-back check.

**The idea that carries it:** When the top digit runs short, open the next place — and prove every difference by adding it back: answer plus what you took away must rebuild what you started with.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Flipping a column to bigger-minus-smaller — for 634 − 278 computing 8 − 4 in the ones.
- Jumping over a zero when borrowing — in 503 − 168, taking ones straight from the hundreds and leaving the tens untouched.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4as-l2-we1` — Compute $634 - 278$, then sign the receipt.
- `g4as-l2-we2` — Compute $503 - 168$.

**2 try-it problems**, same freedom and same condition.

### 3. `mental-strategies`

**Able to:** Add and subtract in your head using make-ten, near-doubles, and compensation — moving amounts between numbers and giving back overshoots — with a number-line picture of every jump.

**The idea that carries it:** Slide the sum to round ground — fill tens, lean on doubles, overshoot to hundreds — and always settle the difference you moved.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Moving an amount without taking it from anywhere — 48 + 27 computed as 50 + 27.
- Settling the wrong way after subtracting — 725 − 98 finished as 625 − 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4as-l3-we1` — Compute $48 + 27$ in your head with the make-ten strategy.
- `g4as-l3-we2` — Compute $356 + 99$ with compensation.

**2 try-it problems**, same freedom and same condition.

### 4. `missing-numbers`

**Able to:** Read a fact family as four faces of one fact, and solve box equations like $\square + 38 = 91$ with the inverse operation — always checking by substitution.

**The idea that carries it:** A fact family is one fact wearing four outfits — so a box equation is solved by the family member that undoes it, and proved by substitution.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding whatever two numbers appear — solving □ + 38 = 91 as 91 + 38 = 129.
- Subtracting on □ − 47 = 129 because the equation shows a minus sign.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4as-l4-we1` — Write the four facts of the family $53$, $38$, $91$.
- `g4as-l4-we2` — Solve $\square - 47 = 129$, and check by substitution.

**2 try-it problems**, same freedom and same condition.

### 5. `word-problems`

**Able to:** Solve one- and two-step word problems inside 10 000 — reading the story's shape to choose addition or subtraction, finding hidden numbers first, and receipting every answer.

**The idea that carries it:** Read the story's shape, find the hidden number first, and receipt every answer — two roads to the same number make it true.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Grabbing the two numbers and adding, whatever the question asks.
- Stopping after step one of a two-step problem.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4as-l5-we1` — A herder's flock holds $1\,250$ sheep and $860$ goats. How many animals altogether?
- `g4as-l5-we2` — Bilguun saves $3\,600$ togrog. At the market he buys a notebook for $1\,250$ and a pen for $850$. How much is left?

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
| tens | **аравт** | already on the site |
| hundreds | **зуут** | already on the site |
| amount | **хэмжээ** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| line | **шулуун** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| square | **квадрат** | ministry standard |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| substitution | **орлуулга** | ministry standard |
| difference | **ялгавар** | ministry standard |
| problem | **бодлого** | ministry standard |
| hundred | **зуу** | already on the site |
| total | **нийт** | already on the site |
| answer | **хариулт** | already on the site |
| subtract | **хасах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

**hundreds** — proposed **зуут**

> POLYSEMOUS. As a place value, hundreds = зуут, "the hundreds place" = зуутын орон — the ЭШ papers give the full series «зуутын, аравтын, нэгжийн орон», which is the authority to follow. The quantity phrase "hundreds of X" is not зуут but хэдэн зуун / олон зуун: shipped "hundreds of thousands of inequalities" → «хэдэн зуун мянган тэнцэтгэл биш», "many hundreds of rolls" → «олон зуун хаялт». (зуут also turns up in the percent etymology line «зуут ногдох» = per hundred, which is unrelated.)

**amount** — proposed **хэмжээ**

> POLYSEMOUS, and the shipped mirrors genuinely disagree, which is why this is medium. хэмжээ is the dominant choice for "amount" as a quantity of something (three of the four lines given with this term, plus the decimal-division unit throughout) and is what this entry proposes. But when "amounts" means measurable numerical quantities in the data-type sense, shipped switches to хэмжигдэхүүн: "**Numerical** data: amounts you can add and average" → «**Тоон** өгөгдөл: нэмж, дундажилж болох хэмжигдэхүүн», and "Category labels are not amounts" → «Ангиллын шошго бол хэмжигдэхүүн биш». That is the same word the ministry uses as the title of its measurement strand (MoE 10.12 «Хэмжигдэхүүн»). Suggested split: хэмжээ for a concrete amount in a problem, хэмжигдэхүүн for "quantity" as a category of data. Note хэмжээ is also this batch's "size".

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
## column-addition

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g4as-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g4as-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## column-subtraction

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g4as-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g4as-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g4as-l1-we1` and so on) exactly
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

