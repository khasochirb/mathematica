# MN authoring brief — Quantities & the Structure of Expressions

**Topic** `integrated-1/quantities-and-expressions` · **4 lessons** · 16 worked examples · 12 practice · 7 test-yourself

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
> `integrated-1/quantities-and-expressions`. That is a judgement call per topic and a template
> cannot fake it — the outcomes below are the raw material for it, not a
> substitute.

Each lesson, and what the student must end up able to do:

### 1. `units-and-quantities`

**Able to:** Attach units to every quantity, convert between units by multiplying by a fraction equal to $1$, use units to decide which operation a problem calls for, and report an answer to a precision the measurements actually support.

**The idea that carries it:** Multiply by a fraction that equals $1$, arranged so the unit you want to lose cancels. Then round the final answer to the precision your measurements support — not to the precision your calculator offers.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Flipping the conversion factor — multiplying by 3.6 to turn km/h into m/s.
- Converting an area with the LINEAR factor: writing 1 m² = 100 cm².
- Reporting every digit the calculator shows — 632.7000 m² from three-digit data.
- Adding quantities with different units — 2 hours + 30 minutes = 32.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u1-l1-we1` — A bus travels at $90$ km/h. Express this speed in metres per second.
- `im1-u1-l1-we2` — A car's fuel use is rated at $7.5$ litres per $100$ km. How much fuel does a $340$ km trip need?
- `im1-u1-l1-we3` — A rectangular plot is measured as $34.2$ m by $18.5$ m. Report its area with an appropriate precision.
- `im1-u1-l1-we4` — A room's floor measures $4.5\text{ m} \times 3.2\text{ m}$. Express its area in square centimetres.

**3 try-it problems**, same freedom and same condition.

### 2. `structure-of-expressions`

**Able to:** Break an expression into its terms, factors and coefficients, interpret each part in the context it models, and read a compound part as a single object when doing so makes the structure clearer.

**The idea that carries it:** Split at $+$ and $-$ to find the terms; inside a term the pieces multiplied together are the factors and the number in front is the coefficient. Then ask what each part MEANS in the situation — a starting value, a rate, a growth factor, a count.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Reading the coefficient of x in 7 − 4x as 4.
- Treating x as having coefficient 0 because no number is written.
- Calling 3(x + 5) a single term with coefficient 3 and then adding 5 separately.
- Reading P(1 + r)ⁿ as P + rⁿ or as P(1) + rⁿ.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u1-l2-we1` — For the expression $7x^2 - 4x + 9$, list the terms, and give the coefficient of each variable term.
- `im1-u1-l2-we2` — A phone plan costs $12\,000$₮ per month plus $45$₮ for each minute of calls. The monthly bill is $B = 45m + 12\,000$. Interpret each part, and find ho
- `im1-u1-l2-we3` — In the savings model $A = P(1 + r)^{n}$, identify the role of each part when $P = 500\,000$₮, $r = 0.08$ and $n = 3$. Then compute $A$.
- `im1-u1-l2-we4` — Show that $15n + 400$ and $5(3n + 80)$ are equivalent, and say what each form makes obvious.

**3 try-it problems**, same freedom and same condition.

### 3. `creating-equations`

**Able to:** Define a variable with its unit, translate a described situation into a one-variable equation or inequality, or into a two-variable equation relating two quantities, and check the model against a case you can verify by hand.

**The idea that carries it:** Define the variable and its unit, translate the sentence phrase by phrase into symbols, state the constraint the situation imposes, and then test the model on one case you can verify without it.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Starting to write symbols before defining what the letter means.
- Reading "9 more 500₮ coins than 100₮ coins" as n + 9 = the 100₮ count.
- Solving the algebra and reporting d = −4 km or 3.5 tickets.
- Using = when the sentence says "at most" or "no more than".

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u1-l3-we1` — A taxi charges $1500$₮ to start and $900$₮ per kilometre. You have $12\,000$₮. Write an inequality for the distance you can afford, and solve it.
- `im1-u1-l3-we2` — A theatre sells adult tickets at $8000$₮ and child tickets at $3000$₮. One evening the takings were $604\,000$₮. Write an equation relating the two ti
- `im1-u1-l3-we3` — A water tank holds $450$ litres and is draining at $12$ litres per minute. Write a two-variable equation for the volume $V$ remaining after $t$ minute
- `im1-u1-l3-we4` — A student has $9$ more $500$₮ coins than $100$₮ coins, and the coins are worth $16\,500$₮ altogether. How many of each does the student have?

**3 try-it problems**, same freedom and same condition.

### 4. `rearranging-formulas`

**Able to:** Solve a literal equation for any variable it contains, using the same operations that solve a numerical equation, and recognise that the letters change nothing about the method.

**The idea that carries it:** Peel operations off the target variable in reverse order, doing the same thing to both sides. If the target appears more than once, gather those terms and factor it out — then divide by what is left.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Undoing operations in the wrong order — dividing by a before subtracting u in v = u + at.
- Dividing only part of a side: from 2A = bh writing h = 2A/b but from v − u = at writing t = v − u/a.
- Solving ax + b = cx + d by dividing before collecting the x-terms.
- Dropping the ± when taking a square root, with no reason given — or keeping a negative radius.

**4 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `im1-u1-l4-we1` — The area of a triangle is $A = \frac{1}{2}bh$. Solve for $h$, then find $h$ when $A = 84$ and $b = 12$.
- `im1-u1-l4-we2` — The formula $v = u + at$ gives velocity after time $t$. Solve for $t$, then find $t$ when $v = 47$, $u = 5$ and $a = 6$.
- `im1-u1-l4-we3` — A circle's area is $A = \pi r^{2}$. Solve for $r$, stating why you keep only one sign, and find $r$ when $A = 49\pi$.
- `im1-u1-l4-we4` — Solve $5x + 3 = 2x + 18$ for $x$ — then solve the general form $ax + b = cx + d$ for $x$.

**3 try-it problems**, same freedom and same condition.

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
| count | **тоолох** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| area | **талбай** | ministry standard |
| equation | **тэгшитгэл** | ministry standard |
| mean | **дундаж** | ministry standard |
| fraction | **бутархай** | ministry standard |
| rate | **хурдац** | already on the site |
| number | **тоо** | ministry standard |
| multiplying | **үржүүлэх** | ministry standard |
| unit | **нэгж** | ministry standard |
| growth | **өсөлт** | already on the site |
| formula | **томьёо** | ministry standard |
| linear | **шугаман** | ministry standard |
| problem | **бодлого** | ministry standard |
| inequality | **тэнцэтгэл биш** | ministry standard |
| side | **тал** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**factor** — proposed **хуваагч**

> One English key, two live Mongolian terms: a number's factor/divisor is «хуваагч» (164× in production, not in the ministry standard), while an algebraic factor is «үржигдэхүүн» (ministry 10.2 «үржигдэхүүн болгон задлах»; 80× in production). Needs two keys — and note «хуваагдагч» (105×) is the multiple/dividend, easy to confuse.

**count** — proposed **тоолох**

> POLYSEMOUS. Verb "to count" = тоолох (ministry 12.14, and shipped throughout). Noun "the count" = тоо when it means how many items («Mean = sum ÷ count» → «Дундаж = нийлбэр ÷ тоо»), but тооллого when it means the tally/inventory itself («the small raised exponent is the count» → «илтгэгч нь тооллого»; "take inventory" → «Тооллого хий»). This entry proposes the verb. Do not write тоолол.

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
## units-and-quantities

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u1-l1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u1-l1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## structure-of-expressions

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED im1-u1-l2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY im1-u1-l2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`im1-u1-l1-we1` and so on) exactly
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

