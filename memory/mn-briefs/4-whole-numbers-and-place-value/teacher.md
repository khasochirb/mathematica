# MN authoring brief — Whole Numbers & Place Value

**Topic** `4/whole-numbers-and-place-value` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `4/whole-numbers-and-place-value`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `reading-and-writing-large-numbers`

**Able to:** Read and write numbers up to millions using digit groups (periods), and translate between numerals, words, and expanded form.

**The idea that carries it:** Split a big number into groups of three from the right, read each group like a small number, and say the group's name. Expanded form shows what every digit is worth.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Dropping the zeros that hold empty places — writing "seventy thousand fifty" as 7050.
- Reading digits one at a time ("four, seven, zero, eight...") instead of by groups.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5pv-l1-we1` — Write the numeral for *three hundred forty-five thousand, six hundred two*.
- `g5pv-l1-we2` — Write $4\,708\,215$ in words.

**2 try-it problems**, same freedom and same condition.

### 2. `the-value-of-a-digit`

**Able to:** Name the place of any digit up to millions, state its value, and use the ten-times relationship between neighbouring places.

**The idea that carries it:** A digit's value is the digit times its place, and each step left multiplies that value by ten. Place decides worth.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Giving the digit itself as its value — "the 7 in 4,708 is worth 7".
- Naming places from the left instead of the right.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5pv-l2-we1` — What is the value of the digit $7$ in $4\,708$? And in $7\,048$?
- `g5pv-l2-we2` — In $5\,352$, how many times the value of the right-hand $5$ is the left-hand $5$?

**2 try-it problems**, same freedom and same condition.

### 3. `comparing-and-ordering-numbers`

**Able to:** Compare whole numbers using digit count and left-to-right digit comparison, write the result with $<$ and $>$, and order lists of numbers.

**The idea that carries it:** Compare digit counts first — more digits wins. Same count: scan from the left and the first differing digit decides.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Comparing from the right because that's where arithmetic starts.
- Letting a big right-hand digit win — thinking 56,297 beats 56,342 because 9 > 4.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5pv-l3-we1` — Compare $56\,342$ and $56\,297$.
- `g5pv-l3-we2` — Order from smallest to largest: $23\,502$, $9\,999$, $23\,089$, $102\,000$.

**2 try-it problems**, same freedom and same condition.

### 4. `rounding-whole-numbers`

**Able to:** Round whole numbers to any place — tens through hundred-thousands — using the nearest-landmark idea and the digit rule, including the halfway case.

**The idea that carries it:** Round = jump to the nearest landmark multiple. The digit one place right tells you which way: 0–4 down, 5–9 up.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Looking at the wrong digit — rounding 4,683 to the nearest hundred by checking the ones digit.
- Rounding in two hops: 4,449 → 4,450 → 4,500.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5pv-l4-we1` — Round $4\,683$ to the nearest hundred, and to the nearest thousand.
- `g5pv-l4-we2` — Round $349\,502$ to the nearest ten-thousand.

**2 try-it problems**, same freedom and same condition.

### 5. `estimating-with-rounded-numbers`

**Able to:** Estimate sums and differences by rounding first, judge whether an exact answer is reasonable, and know when an estimate over- or under-shoots.

**The idea that carries it:** Round first, compute second — a seconds-long estimate that catches wrong answers and guides safe decisions.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing exactly first and rounding the answer, calling it an estimate.
- Treating the estimate as the answer.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5pv-l5-we1` — Estimate $4\,683 + 2\,298$ by rounding to the nearest hundred, then compare with the exact sum.
- `g5pv-l5-we2` — A student computes $8\,132 - 4\,905 = 4\,227$. Use an estimate to judge the answer.

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
| thousands | **мянгат** | already on the site |
| translate | **хөрвүүлэх** | already on the site |
| number | **тоо** | ministry standard |
| time | **цаг** | already on the site |
| period | **үе** | **proposed — tell us if it is wrong** |
| difference | **ялгавар** | ministry standard |
| form | **хэлбэр** | ministry standard |
| hundred | **зуу** | already on the site |
| second | **хоёр дахь** | ministry standard |
| answer | **хариулт** | already on the site |
| digit | **цифр** | already on the site |
| direction | **чиглэл** | ministry standard |
| arithmetic | **арифметик** | ministry standard |
| rounding | **тоймлох** | ministry standard |
| multiple | **хуваагдагч** | ministry standard |
| including | **оролцуулан** | already on the site |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

**thousands** — proposed **мянгат**

> POLYSEMOUS, and the one genuinely unsupported entry in this batch — treat it as a proposal to confirm with the owner. (1) As a place value, "thousands" should be мянгат by regular formation from the attested нэгж / аравт / зуут series (мянгатын орон = the thousands place), but no published source in this repo actually writes it, hence low. (2) The only shipped evidence given with this term is a different sense — "(in thousands)" as a reporting unit — where the mirror writes the instrumental «(мянгаар)»: "Nine salaries of $300$ (in thousands)" → «$300$ (мянгаар)-ийн есөн цалин». Do not promote мянгаар to the term; it is a case form, not the place. (3) "thousands of X" is again хэдэн мянган («хэдэн зуун мянган тэнцэтгэл биш»). Note the decimal counterpart мянганы (thousandths) IS attested and is a different word — see "tenths"/"hundredths".

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
## reading-and-writing-large-numbers

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5pv-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5pv-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## the-value-of-a-digit

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5pv-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5pv-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g5pv-l1-we1` and so on) exactly
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

