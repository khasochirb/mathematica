# MN authoring brief — Numbers to 10 000

**Topic** `3/numbers-to-10000` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `3/numbers-to-10000`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `reading-and-writing-numbers`

**Able to:** Read four-digit numerals in words and write word names as numerals, name the thousands, hundreds, tens and ones columns, and use zero to hold a column that is empty.

**The idea that carries it:** Four-digit numbers are four named columns — thousands, hundreds, tens, ones. Reading walks the columns left to right, and zero stands guard in any column that is empty.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Putting the fifty in the wrong column — writing "four thousand and fifty-two" as 4 520.
- Skipping the zero when reading — calling 4 052 "four hundred and fifty-two".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4nu-l1-we1` — Write $3\,482$ in words.
- `g4nu-l1-we2` — Write "four thousand and fifty-two" as a numeral.

**2 try-it problems**, same freedom and same condition.

### 2. `place-value`

**Able to:** Say what each digit of a four-digit number is worth, write numbers in expanded form, and build numbers back from thousands, hundreds, tens and ones.

**The idea that carries it:** Each digit is worth digit times place: expanded form spells the worths out as a sum, and building from parts folds the sum back into a numeral — with zero guarding any missing part.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Saying the 3 in 3 482 "is worth 3".
- Expanded form that invents a part — writing 4 052 as 4 000 + 500 + 2.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4nu-l2-we1` — What is the $7$ worth in $2\,745$? And in $7\,245$?
- `g4nu-l2-we2` — Write $3\,482$ in expanded form.

**2 try-it problems**, same freedom and same condition.

### 3. `comparing-and-ordering`

**Able to:** Compare four-digit numbers place by place from the left, order sets of three or four numbers, and place a number between its neighbouring hundreds on the number line.

**The idea that carries it:** Count digits first, then compare place by place from the left — the first difference decides. On the number line, bigger simply means further right.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Letting a flashy small column decide — 2 895 > 3 014 "because 8 beats 0".
- Comparing first digits across different lengths — 987 > 1 023 "because 9 beats 1".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4nu-l3-we1` — Which herd is larger: $3\,025$ animals or $2\,970$?
- `g4nu-l3-we2` — Order from smallest to largest: $5\,470$, $5\,461$, $5\,504$.

**2 try-it problems**, same freedom and same condition.

### 4. `rounding`

**Able to:** Round four-digit numbers to the nearest 10 and nearest 100 by comparing the two neighbours on the number line, apply the halfway-rounds-up rule, and use rounding to estimate sums.

**The idea that carries it:** Rounding is a two-neighbour contest on the number line: find the round number on each side, measure both gaps, move to the closer one — and when the gaps tie, go up.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Rounding to the wrong place — asked for the nearest 10, answering 3 500 for 3 482.
- Sending halfway numbers down — rounding 645 to 640.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4nu-l4-we1` — Round $3\,482$ to the nearest $10$.
- `g4nu-l4-we2` — Round $7\,258$ to the nearest $100$.

**2 try-it problems**, same freedom and same condition.

### 5. `number-patterns`

**Able to:** Skip count by 25s, 50s and 100s, find a pattern's step by subtracting neighbours, continue and describe patterns, and tell odd from even using the ones digit.

**The idea that carries it:** Subtract neighbours to name the step, then add it to continue — and for odd or even, ask only the ones digit: all the bigger places split evenly by themselves.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Guessing the step from the loudest changing digit — calling 5 650, 5 700, 5 750 "counting by 100s" because the hundreds digit keeps moving.
- Judging odd or even by the first digit — "2 467 is even because it starts with 2".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g4nu-l5-we1` — Continue the pattern with two more numbers, and name its step: $4\,200, 4\,250, 4\,300$.
- `g4nu-l5-we2` — Is $3\,482$ odd or even? And $4\,507$?

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
| measure | **хэмжих** | ministry standard |
| hundreds | **зуут** | already on the site |
| thousands | **мянгат** | already on the site |
| mean | **дундаж** | ministry standard |
| line | **шулуун** | ministry standard |
| number | **тоо** | ministry standard |
| zero | **тэг** | ministry standard |
| counting | **тоолох** | ministry standard |
| time | **цаг** | already on the site |
| even | **тэгш** | ministry standard |
| difference | **ялгавар** | ministry standard |
| form | **хэлбэр** | ministry standard |
| side | **тал** | ministry standard |
| hundred | **зуу** | already on the site |
| subtracting | **хасах** | ministry standard |
| part | **хэсэг** | ministry standard |
| subtract | **хасах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

**measure** — proposed **хэмжих**

> POLYSEMOUS — Mongolian splits what English keeps as one word, so name the sense. (1) The verb "to measure" = хэмжих (this entry). (2) "a measure of centre/spread" = хэмжүүр: shipped «аль төвийн хэмжүүр нөхцөл байдалд тохирохыг сонгоно», «тархалтын хамгийн энгийн хэмжүүр». (3) "a measurement" (one reading taken) = хэмжилт: «ганц хэмжилт, олон янз байдал алга». (4) A measurable quantity = хэмжигдэхүүн, which is the ministry's title for the whole measurement strand (MoE 10.12 «Хэмжигдэхүүн») and also the angle-measure noun хэмжээ (MoE 11.6 «Өнцгийн радиан хэмжээ»). Using хэмжих where хэмжүүр is meant is the likely error in statistics lessons.

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
## reading-and-writing-numbers

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g4nu-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g4nu-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## place-value

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g4nu-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g4nu-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g4nu-l1-we1` and so on) exactly
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

