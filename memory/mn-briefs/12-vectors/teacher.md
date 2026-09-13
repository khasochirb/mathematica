# MN authoring brief — Vectors

**Topic** `12/vectors` · **6 lessons** · 18 worked examples · 10 practice · 7 test-yourself

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

A student finishes this topic holding these ideas. Everything else in the
brief serves them.

1. **A vector is a displacement, not a place.** The same vector can start anywhere; only its direction and length matter. Students who hold it as "an arrow from the origin" struggle the moment vectors are added tail-to-head.

2. **The dot product measures alignment.** Zero means perpendicular — that is the fact worth carrying, more than the formula. It turns geometric questions about angles into arithmetic.

3. **Component form makes it algebra.** Once a vector is a pair or triple of numbers, adding, scaling and dotting are just arithmetic on the components. Move there early.

**The error to design against:** Treating the dot product as producing a vector. It returns a number, and that is exactly why it can answer questions about angle.

If your Mongolian version lands those and a student can do the practice
set, the topic is right — however you got there.

Each lesson, and what the student must end up able to do:

### 1. `what-is-a-vector`

**Able to:** Represent vectors as component pairs ⟨a, b⟩, distinguish them from scalars, compute magnitudes, and find the vector between two points.

**The idea that carries it:** A vector is magnitude + direction, written ⟨a, b⟩ (east-part, north-part). |⟨a,b⟩| = √(a² + b²), and tip-minus-tail builds the vector between two points.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Confusing the vector ⟨3, 4⟩ with the point (3, 4).
- Adding magnitudes componentwise: |⟨3, 4⟩| = 7.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ve1-we1` — Find the magnitude of $\vec{v} = \langle 3, 4 \rangle$.
- `ve1-we2` — Find the vector from $A(2, -1)$ to $B(5, 3)$, and its magnitude.
- `ve1-we3` — Which are vectors: temperature, velocity, mass, force?

**2 try-it problems**, same freedom and same condition.

### 2. `adding-and-scaling`

**Able to:** Add and subtract vectors componentwise (tip-to-tail picture), multiply by scalars, and combine operations.

**The idea that carries it:** Add tip-to-tail in pictures, componentwise in algebra. Scalars stretch, shrink, or reverse; subtraction adds the reverse.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding magnitudes instead of vectors.
- Scaling only one component.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ve2-we1` — $\vec{u} = \langle 3, 1 \rangle$, $\vec{v} = \langle 1, 3 \rangle$: find $\vec{u} + \vec{v}$ and $\vec{u} - \vec{v}$.
- `ve2-we2` — Compute $3\langle 2, -1 \rangle - 2\langle 1, 4 \rangle$.
- `ve2-we3` — The plane: velocity $\langle 0, 700 \rangle$ km/h, wind $\langle 100, 0 \rangle$. Find the true velocity and speed.

**2 try-it problems**, same freedom and same condition.

### 3. `unit-vectors-and-direction`

**Able to:** Normalize vectors to unit length, use the standard basis i and j, and build vectors with a given magnitude and direction.

**The idea that carries it:** v̂ = v/|v| strips a vector to pure direction (length 1). i and j are the axis units; a⟨cos θ, sin θ⟩ builds any size in any heading.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Normalizing by dividing by a component instead of the magnitude.
- Treating i and j as unknowns to solve for.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ve3-we1` — Find the unit vector in the direction of $\vec{v} = \langle 3, 4 \rangle$.
- `ve3-we2` — Write $\langle -2, 7 \rangle$ in $\vec{i}, \vec{j}$ form, and $5\vec{i} - 3\vec{j}$ in bracket form.
- `ve3-we3` — Build the vector of magnitude 26 in the direction of $\langle 5, 12 \rangle$.

**2 try-it problems**, same freedom and same condition.

### 4. `the-dot-product`

**Able to:** Compute dot products from components and from |u||v|cos θ, and read the sign as an agreement meter.

**The idea that carries it:** u · v = uₓvₓ + uᵧvᵧ = |u||v|cos θ: a scalar agreement meter. Positive acute, zero perpendicular, negative obtuse.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Expecting the dot product to be a vector.
- Reading dot = 0 as 'a vector is zero'.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ve4-we1` — Compute $\langle 2, 3 \rangle \cdot \langle 4, 1 \rangle$.
- `ve4-we2` — Show $\langle 2, 3 \rangle \perp \langle 3, -2 \rangle$.
- `ve4-we3` — $|\vec{u}| = 4$, $|\vec{v}| = 5$, angle $60°$: find $\vec{u} \cdot \vec{v}$.

**2 try-it problems**, same freedom and same condition.

### 5. `angles-between-vectors`

**Able to:** Compute the angle between vectors via cos θ = (u·v)/(|u||v|), and use dot products to test alignment precisely.

**The idea that carries it:** cos θ = (u·v)/(|u||v|): three arithmetic quantities produce the angle. The unit-circle chart converts the cosine to degrees.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Forgetting to divide by BOTH magnitudes.
- Reporting the cosine as the angle.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ve5-we1` — Find the angle between $\langle 1, 0 \rangle$ and $\langle 1, 1 \rangle$.
- `ve5-we2` — Find the angle between $\langle 3, 4 \rangle$ and $\langle -4, 3 \rangle$.
- `ve5-we3` — Find the angle between $\langle 1, \sqrt{3} \rangle$ and $\langle 2, 0 \rangle$.

**2 try-it problems**, same freedom and same condition.

### 6. `vectors-in-action`

**Able to:** Solve applied problems — displacement chains, velocity with current/wind, force components, and work — using the full vector toolkit.

**The idea that carries it:** Axes → components → algebra (add displacements/velocities, resolve forces by cos/sin, dot for work) → translate back. Four moves close every applied problem.

**Where students break** — the English warns about these, and they are
worth keeping however you phrase them:
- Adding path lengths to get displacement.
- Using the full force magnitude in work when the pull is angled.

**3 worked examples.** Yours to choose — different numbers, a
different context, a Mongolian setting instead of an American one. What
each must *do* is fixed:
- `ve6-we1` — A delivery drone flies $\langle 6, 2 \rangle$ km, then $\langle -2, 3 \rangle$ km. Net displacement and distance from base?
- `ve6-we2` — A boat aims straight across at 4 m/s; the river flows 3 m/s. Find the true speed and the downstream drift after 20 s.
- `ve6-we3` — A sled is pulled with force 40 N at $60°$ above horizontal, over 10 m of flat ground. Compute the work.

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
| range | **далайц** | ministry standard |
| size | **хэмжээ** | ministry standard |
| translate | **хөрвүүлэх** | already on the site |
| angle | **өнцөг** | ministry standard |
| cosine | **косинус** | ministry standard |
| product | **үржвэр** | ministry standard |
| circle | **тойрог** | ministry standard |
| zero | **тэг** | ministry standard |
| unit | **нэгж** | ministry standard |
| addition | **нэмэх** | ministry standard |
| subtraction | **хасалт** | already on the site |
| formula | **томьёо** | ministry standard |
| algebra | **алгебр** | ministry standard |
| point | **цэг** | ministry standard |
| problem | **бодлого** | ministry standard |
| stretch | **сунгалт** | already on the site |
| part | **хэсэг** | ministry standard |

### Careful — English uses one word where Mongolian uses two

These are the ones that go wrong silently. The word above is the sense
this topic most likely means; check it against what you are actually
writing, and say so if the topic needs the other one.

**range** — proposed **далайц**

> One English key, two unrelated Mongolian terms: the statistical range is «далайц» (10.13, 11.11) but a function's range is «утгын муж; дүр» (glossary; ministry 11.3 «тодорхойлогдох муж ба дүр»). Split into two keys before the calculus hubs land.

**size** — proposed **хэмжээ**

> POLYSEMOUS in one narrow place. хэмжээ is the general word for size/magnitude — ministry for the size of a matrix, shipped for the size of a number, a piece, a group — and is what this entry proposes; the productive forms are ижил хэмжээтэй (of the same size) and ижил хэмжээний + noun. But clothing/shoe size is размер in shipped material («Гутлын размер: $36, 38, ...$», "shoe size and quiz score" → «Гутлын размер ба шалгалтын оноо»), so a data-handling example about shoe sizes keeps размер. Note хэмжээ is also the word this batch's "amount" lands on — that collision is real and intended, do not invent a second word to separate them.

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
## what-is-a-vector

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ve1-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ve1-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

## adding-and-scaling

TITLE:      <the lesson title in Mongolian>
OBJECTIVE:  <what the student can do after it, one sentence>
KEY IDEA:   <the one sentence that carries the lesson>

TEACHING:
<your explanation. As many paragraphs as it takes — more than the
English, fewer, in a different order. Blank line between paragraphs.>

MISTAKES:
- <a mistake students make, and why>

WORKED ve2-we1:
  PROBLEM:  <the question, your numbers>
  WORKING:  <how it is solved, step by step>
  ANSWER:   <the answer, exactly>

TRY ve2-t1:
  PROBLEM:  <the question>
  ANSWER:   <the answer, exactly>

...and so on for the remaining lessons.
```

**Keep the ids** (`ve1-we1` and so on) exactly
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

