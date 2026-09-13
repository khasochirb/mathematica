# MN authoring brief — Addition & Subtraction

**Topic** `4/addition-and-subtraction` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `4/addition-and-subtraction`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `adding-with-regrouping`

**Able to:** Add multi-digit numbers with the column method, carrying (regrouping) through any number of places, and add three or more numbers by grouping them cleverly.

**The idea that carries it:** Add place by place from the ones; when a column passes nine, trade ten of it for one of the next place — that's the carry, and it's the whole algorithm.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Writing the whole two-digit column sum in one place — 6 + 7 = 13, so writing "13".
- Lining numbers up by their first digits instead of their last.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5as-l1-we1` — Add $4\,586 + 2\,747$ with the column method.
- `g5as-l1-we2` — A tent costs $12\,485$ tögrög and a stove $9\,635$. What do they cost together?

**2 try-it problems**, same freedom and same condition.

### 2. `subtracting-with-regrouping`

**Able to:** Subtract multi-digit numbers with the column method, borrowing (regrouping) through any place — including across zeros — and check every subtraction by adding back.

**The idea that carries it:** Borrowing is the carry run backwards — break one of the next place into ten of this one — and every answer can be checked by adding back what was subtracted.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Flipping the digits instead of borrowing — reading 2 − 8 as "8 − 2 = 6".
- Forgetting that a borrowed-from digit shrinks by one.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5as-l2-we1` — Subtract $8\,254 - 3\,478$.
- `g5as-l2-we2` — The hall printed $5\,003$ tickets and sold $1\,647$. How many remain?

**2 try-it problems**, same freedom and same condition.

### 3. `mental-addition-and-subtraction`

**Able to:** Add and subtract mentally using compensation (round, then repay), making tens and hundreds, and counting up — and choose the strategy that fits the numbers.

**The idea that carries it:** Trade your problem for a round-number problem, then repay the trade — compensation, making tens, and counting up are all this one idea.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Repaying the compensation in the wrong direction — 499 + 276 = 776 + 1.
- Using the written algorithm in your head for numbers built for a strategy.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5as-l3-we1` — Compute $499 + 276$ in your head.
- `g5as-l3-we2` — Compute $1\,000 - 674$ by counting up.

**2 try-it problems**, same freedom and same condition.

### 4. `fact-families-and-missing-numbers`

**Able to:** Use the inverse relationship between addition and subtraction to write fact families, check computations, and solve missing-number equations.

**The idea that carries it:** Addition and subtraction are one whole-and-parts relationship read in two directions: the unknown whole comes from adding the parts, an unknown part from subtracting the other part from the whole.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Always subtracting when a problem shows a minus sign — solving □ − 456 = 789 as 789 − 456.
- Writing a fact family with the whole in a part's position, like 456 − 1,245 = 789.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5as-l4-we1` — Check the subtraction $7\,254 - 3\,867 = 3\,387$ using its fact family.
- `g5as-l4-we2` — Solve: $\square - 456 = 789$.

**2 try-it problems**, same freedom and same condition.

### 5. `multi-step-word-problems`

**Able to:** Solve word problems needing two or more additions and subtractions: track a changing total, compare amounts, and check the result against an estimate.

**The idea that carries it:** Break the story into events, one operation each, running total after every step — and let a rounded version of the same plan check the answer.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding every number in the story because they're there.
- Answering the wrong question — computing the afternoon takings when the problem asked for the till total.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5as-l5-we1` — A shop's till holds $12\,450$ tögrög. The morning brings in $3\,780$ of takings and the afternoon $4\,265$ more; then the shop pays a supplier $8\,900
- `g5as-l5-we2` — A library owns $8\,540$ books. It receives a donation of $1\,260$ and lends out $2\,375$. How many books are on its shelves?

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
| tens | **аравт** | already on the site |
| hundreds | **зуут** | already on the site |
| amount | **хэмжээ** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| counting | **тоолох** | ministry standard |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| difference | **ялгавар** | ministry standard |
| problem | **бодлого** | ministry standard |
| hundred | **зуу** | already on the site |
| subtracting | **хасах** | ministry standard |
| part | **хэсэг** | ministry standard |
| total | **нийт** | already on the site |
| answer | **хариулт** | already on the site |
| pair | **хос** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## adding-with-regrouping

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5as-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5as-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## subtracting-with-regrouping

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5as-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5as-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g5as-l1-we1` and so on) exactly
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

