# MN authoring brief — Measurement & Units

**Topic** `4/measurement-and-units` · **5 lessons** · 10 worked examples · 8 practice · 6 test-yourself

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
> `4/measurement-and-units`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `units-of-length`

**Able to:** Know the metric length ladder (mm, cm, m, km), choose the sensible unit for a task, and convert in both directions — including mixed forms like 3 m 45 cm.

**The idea that carries it:** A measurement is a count of units. Converting re-counts the same length: down the ladder multiplies (more, smaller units), up the ladder divides.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Converting metres to centimetres by ×10 — 3 m = 30 cm.
- Multiplying when going UP the ladder — 2,500 m = 2,500,000 km.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5me-l1-we1` — A plank measures $3$ m $45$ cm. Express it in centimetres, and in metres as a decimal.
- `g5me-l1-we2` — A trail is $2\,500$ m long. Write it in kilometres-and-metres, and as a decimal of kilometres.

**2 try-it problems**, same freedom and same condition.

### 2. `mass-and-capacity`

**Able to:** Convert between grams, kilograms and tonnes, and between millilitres and litres, including mixed forms and how-many-fit problems.

**The idea that carries it:** Mass and capacity reuse the length ladder's design — thousand-steps between units. Convert to one unit, then count, add, or divide as usual.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Converting kg to g by ×100 because metres did that.
- Dividing mixed units directly — "2 L ÷ 250 ml = 0.008".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5me-l2-we1` — A parcel weighs $2$ kg $350$ g. Express it in grams, and as a decimal of kilograms.
- `g5me-l2-we2` — How many $250$ ml cups does a $2$ L jug fill?

**2 try-it problems**, same freedom and same condition.

### 3. `units-of-time`

**Able to:** Convert between seconds, minutes, hours and days — including mixed forms and fraction-of-an-hour amounts — without importing base-ten reflexes.

**The idea that carries it:** Time trades by sixties (and twenty-fours), not tens: convert with the rung's own factor, use division with remainders for mixed forms, and never let 1.5 h become 150 minutes.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Converting 1.5 h to 150 min — the ×100 reflex on a ×60 ladder.
- Writing 200 s as 2 min 00 s — dividing by 100.

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5me-l3-we1` — Convert $2$ h $15$ min to minutes, and $200$ s to minutes-and-seconds.
- `g5me-l3-we2` — A film lasts $1.5$ hours. How many minutes is that — and why is $150$ wrong?

**2 try-it problems**, same freedom and same condition.

### 4. `elapsed-time`

**Able to:** Find elapsed time by counting up through round hours, find end times from a start and a duration, and read simple timetables.

**The idea that carries it:** Elapsed time is a climb through round hours — count up to the next hour, across the whole hours, then the loose minutes. Minutes trade at sixty, never at a hundred.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Subtracting clock readings like base-ten numbers — 11:20 − 9:45 with a hundred-borrow.
- Leaving 90 minutes unconverted in an end time — "9:90".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5me-l4-we1` — A train leaves at $9{:}45$ and arrives at $11{:}20$. How long is the journey?
- `g5me-l4-we2` — A lesson starts at $8{:}40$ and lasts $1$ h $50$ min. When does it end?

**2 try-it problems**, same freedom and same condition.

### 5. `measurement-word-problems`

**Able to:** Solve multi-step measurement problems across length, mass, capacity and time, converting to a common unit BEFORE any arithmetic, and reporting answers in sensible units.

**The idea that carries it:** One unit before any arithmetic, familiar arithmetic in the middle, and a sensible unit at the end — the three-part shape of every measurement problem.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Computing across mixed units — 2 L − 750 ml = 1.25 by luck, or 748 by disaster.
- Reporting raw ladder-bottom answers — "the parcels weigh 3,600 g".

**2 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `g5me-l5-we1` — A board of $1.2$ m and a ledge of $45$ cm are joined end to end. How long is the whole, in centimetres and in metres?
- `g5me-l5-we2` — Three parcels each weigh $1$ kg $200$ g. What is the total mass, in a sensible unit?

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
| factor | **хуваагч** | ministry standard |
| count | **тоолох** | ministry standard |
| base | **суурь** | ministry standard |
| tens | **аравт** | already on the site |
| amount | **хэмжээ** | ministry standard |
| fraction | **бутархай** | ministry standard |
| division | **хуваалт** | ministry standard |
| counting | **тоолох** | ministry standard |
| time | **цаг** | already on the site |
| unit | **нэгж** | ministry standard |
| remainder | **үлдэгдэл** | ministry standard |
| problem | **бодлого** | ministry standard |
| form | **хэлбэр** | ministry standard |
| hundred | **зуу** | already on the site |
| second | **хоёр дахь** | ministry standard |
| part | **хэсэг** | ministry standard |
| length | **урт** | ministry standard |
| answer | **хариулт** | already on the site |
| divide | **хуваах** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**shape** — proposed **дүрс**

> Production splits the word by sense: «дүрс» for a geometric shape (73×) and «хэлбэр» for the shape of a distribution ("Center, spread, shape" → «Төв, тархалт, хэлбэр»). «хэлбэр» is also this site's word for "form". Needs two keys — geometric shape vs. distribution shape.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

**base** — proposed **суурь**

> English "base" is polysemous but Mongolian does NOT split it: суурь covers the base of a power (shipped, ~10 lines in the exponents unit), the base of a triangle/parallelogram/prism (shipped, the whole area unit), the base of a solid in the ministry text (10.12), and the base of a logarithm. It is also the word in суурь вектор = basis vector (MoE 10.9, 11.8, and the glossary) — a different concept sharing the word, so in vector lessons write суурь вектор in full and never let a bare суурь stand for a basis. Genitive суурийн, instrumental суурийг per shipped («Суурийг илтгэгчээр үржүүлэх»).

**tens** — proposed **аравт**

> POLYSEMOUS. As a place value, tens = аравт and "the tens place" = аравтын орон — attested both in the shipped mirror and in the ЭШ papers, which is as settled as this family gets. Two traps. (a) The genitive аравтын also heads аравтын бутархай = decimal fraction, so «аравтын орон» (tens place) and «аравтын бутархайн орон» (decimal place) sit one word apart — always keep бутархай when you mean the decimal. (b) "tens of thousands" and similar quantity phrases are not аравт but хэдэн арван: shipped "already tens of thousands" → «аль хэдийн хэдэн арван мянга».

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
## units-of-length

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5me-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5me-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## mass-and-capacity

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED g5me-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY g5me-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`g5me-l1-we1` and so on) exactly
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

