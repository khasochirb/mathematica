# The review pile — what is still uncertain after the glossary and the voice reference

**For Khas. Built 16 Sep 2026, after drafting all eight `algebra-1` topics.
Updated 20 Sep 2026. The geometry strand is complete, and the queue has
switched to ЭШ-first: this file now covers thirty-three drafts, twenty-five
of which feed the ЭШ course.**

His instruction: *"let's push through most of the contents and then make it
ready for review. review as in the stuff that you're not sure even after using
the md's you sent."* This file is that list and nothing else. Anything the
dictionary, the voice reference or ministry order А/492 settled is **not** here
— it is settled, and recorded in the draft it belongs to.

**Voice reference §9 is fully applied and no longer a question.** All
thirty-three drafts carry zero em-dash parentheticals in shipping prose, and
the check is fatal rather than advisory, so the state cannot rot back.

The two references are `docs/en-mn-math-glossary.md` (a–i, 746 of 3,937
entries) and `docs/mn-voice-reference.md`. Their companion data files,
`en-mn-math-glossary.tsv` beyond row 746 and `mn-voice-corpus.tsv`, have not
been supplied; several items below would probably be answered by them.

---

## 1. Blocking — one ruling, everything downstream waits on it

### 1a. Register: «та» or the bare imperative?

| Source | Says |
|---|---|
| The standing ruling, on ten drafts | **«та», polite imperative** — «бодоорой», not «бод» |
| `mn-voice-reference.md` §5 | **Task wording is a bare imperative** — «Доорх дүрс бүрийг хуулбарлан зур.» Polite `-на уу` appears **twice in 1,147 passages** |

Both came from you. `mn_draft_check.py` currently enforces both at once: it
fails on informal pronouns and also warns on bare imperative stems.

A reading that would let both stand, **not adopted**: §11 of the voice
reference says it describes *expository textbook Mongolian*, and that
"parent-facing and conversational writing takes softer connectors… Match the
register to the reader, not to this file alone." Lesson prose speaks *to* a
student; the book sets *tasks*. That would put bare imperatives on `practice`
and `testYourself` statements — the task wording §5 is actually about — and
keep «та» in teaching prose.

**Scale if it changes:** twenty-five drafts, and roughly 3,900 problem statements
— `geometry/foundations` alone added about 250, being three times the size of
an algebra topic.

---

## 2. Notation — mechanical, and one is already applied

### 2a. $y = kx + b$ versus $y = mx + b$ — **applied, please confirm**

А/492 states the form outright: «Шулууны тэгшитгэлийг **y=kx+b**, ax+by+c=0
хэлбэрт бичих, хэрэглэх». Our own bank already leans that way: `y = kx` 45 uses
against `y = mx` 24, and the ЭШ solutions write «Перпендикуляр шулууны налалт
$k_2 = -\frac{1}{k_1}$».

`algebra-1/linear-functions` follows the ministry, so it diverges from its
English mirror in 24 places. Verified mechanically safe first: **no `check[]`
entry in that topic uses `m` as a symbol.** The gym problem keeps `C(m)` where
$m$ is *months*, deliberately untouched.

I followed the ministry because a student who meets $m$ here and $k$ on the
ЭШ paper is being mis-prepared.

> **Updated 19 Sep 2026: this now spans two files.** `geometry/coordinate-geometry`
> lessons 3–5 are the same material (slope, slope-intercept form,
> parallel/perpendicular by slope), so they use `k` too — otherwise the two
> Mongolian mirrors would disagree with **each other**, which is worse than
> either disagreeing with the English. Verified the same way before writing:
> of that topic's **180 `check[]` entries, none uses a bare `m` as a symbol**.
> Reversing it is now a find-and-replace across two files.

### 2b. The decimal comma on money — **applied, first instance worth seeing**

Voice reference §7 is unambiguous (56 comma-decimals against 5 period ones), so
prices in prose now read «\$0,15» where the English says "\$0.15". Eight
instances so far. It is the first notation divergence from an English mirror
that a student will actually see. If you want prices exempted, say so before
this spreads across the bank.

### 2c. Thousands separators inside maths — **not applied, genuine conflict**

| Source | Says |
|---|---|
| `mn-voice-reference.md` §7 | thousands take a **space**: `78 696`, not `78,696` |
| `.claude/skills/mn-translation` | "keep `1{,}200` thousand-separators" as in the English |

Seven instances, all inside `$...$` in `10/exponential-functions`
(`109{,}350`, `5{,}730`, `20{,}000`). Left alone: inside LaTeX this is a
rendering question (`\,` versus `{,}`), not just a character swap, and the two
manuals disagree outright.

### 2d. Math-mode decimals — **not applied. Surveyed: 412 of them.**

> **Correction, 17 Sep 2026. This section said 178 and said the policy was
> applied nowhere. Both were wrong**, on two independent counts.
>
> - **Nine were already converted.** `algebra-1/linear-functions` (7, four of
>   them inside answer options), `algebra-1/functions` (1) and
>   `geometry/foundations` (1) carried `{,}` inside `$...$`. The survey could
>   not see them because it was counting decimal *points*. All nine are
>   reverted. One instance applied is worse than either policy applied
>   uniformly; that is the second time it has had to be repaired by hand, so
>   `mn_draft_check.py` now fails on any `{,}` inside `$...$` where the English
>   has a period. It tells that apart from item 2c's thousands separators by
>   checking the English rather than the shape, since `109{,}350` and `2{,}5`
>   are the same shape to a regex.
> - **The count itself was low.** The survey regex required a non-word
>   character after the decimal, so every decimal glued to a variable —
>   `$2.5t$`, `$1.05n$` — was skipped. Counting every `\d+\.\d+` inside `$...$`
>   gives **205**. The table below is the corrected one.
>
> Nothing about the decision changes; the number you would be ruling on is 205
> rather than 178. **It is 412 as of 20 Sep** — see the note under the table;
> the figure grows with every draft that lands.

§7 says "every number a student reads", but the checks deliberately skip
`$...$` because the decimal point there is LaTeX, not Mongolian punctuation.
So `$x = 3.4$` in an answer option still renders a point.

Counted across the thirty-three drafts, 20 Sep 2026. The table is unchanged
from the thirty-two-draft run: `algebra-2/radicals-and-rational-exponents`
contributes **zero**, being exact-valued throughout, and is the first draft to
add none.

| Draft | Math-mode decimals |
|---|---|
| `10/exponential-functions` | 144 |
| `algebra-2/exponentials-and-logarithms` | 46 |
| `9/equations-and-formulas` | 44 |
| `11/sequences-and-series` | 23 |
| `algebra-1/linear-equations` | 20 |
| `11/logarithms` | 15 |
| `geometry/coordinate-geometry` | 14 |
| `geometry/relationships-in-triangles` | 14 |
| `geometry/circles` | 12 |
| `9/introduction-to-functions` | 11 |
| `geometry/similarity` | 11 |
| `algebra-1/inequalities` | 10 |
| `algebra-1/systems-of-equations` | 8 |
| `10/quadratic-functions` | 7 |
| `algebra-1/linear-functions` | 7 |
| `geometry/foundations` | 5 |
| `geometry/right-triangles-and-trig` | 5 |
| `geometry/transformations` | 5 |
| `esh/number-sets-and-intervals` | 3 |
| `geometry/quadrilaterals-and-polygons` | 3 |
| `geometry/area-and-perimeter` | 2 |
| `10/rational-expressions` | 1 |
| `algebra-1/functions` | 1 |
| `geometry/parallel-and-perpendicular` | 1 |
| **total** | **412** |

> **This table is regenerated, not maintained.** It read 205 across nineteen
> drafts until 18 Sep, when re-running the count found three geometry drafts
> had been written after the survey and never added — the number drifts every
> time a draft lands. Regenerate before acting on it:
>
> ```
> python3 - <<'PY'
> import re, pathlib
> for p in sorted(pathlib.Path('memory/mn-drafts').glob('*.md')):
>     if p.name in ('README.md', 'GEOMETRY-TERMS.md'): continue
>     t = p.read_text(encoding='utf-8')
>     n = sum(len(re.findall(r'\d\.\d', m.group(1)))
>             for m in re.finditer(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$', t))
>     if n: print(f'{p.name:55} {n}')
> PY
> ```
>
> **Use that command and not a plain grep.** On 20 Sep a loose
> `grep -oE '[0-9][.,][0-9]'` over a draft body returned twelve hits that
> looked like unconverted decimals and were all coordinate pairs ($(0,3)$,
> $(1,5)$) and ministry objective codes (10.1а, 11.3е). Across all drafts that
> grep returns 791 against the stored command's 412 — a 77% false-positive
> rate, because it counts commas as well as points and reads outside `$...$`.
> The stored command is correct; ad-hoc ones on these files are not.

Exponential functions carries the largest share because growth factors
(`$b = 1.05$`, `$V = 800(0.75)^t$`) are decimals by nature.

**Why this is your call and not a mechanical follow-on from 2b.** In KaTeX the
change is `1.05` → `1{,}05`, which renders «1,05» correctly but makes every
formula noisier to read and to edit, and it diverges from the English mirror in
412 places rather than eight. It also touches `check[]` neighbourhoods, though
not `check[]` itself. If §7 governs maths mode, it is one scripted pass plus a
render QA walk; if it governs prose only, nothing changes. **Prose decimals
(item 2b) are already done either way** — this is only about the inside of
`$...$`.

---

### 2e. А/492 contradicts itself, and the authority order has no tie-breaker — **a rule I invented, please rule on it**

**Found 19 Sep 2026, drafting `geometry/coordinate-geometry`.** This is not a
terminology question; it is a question about the rule that decides
terminology, which is why it sits in its own item.

`docs/MONGOLIAN.md` fixes the authority order **ministry А/492 → the printed
dictionary → the shipped corpus**. It says nothing about a source that
disagrees with **itself**. А/492 does:

| Spelling | А/492 | corpus |
|---|---|---|
| **параллел** (no soft sign) | **5** | ~12 |
| **параллель** (soft sign) | **2** | **64** |

Both are in the standard. The short form is in one of the two lines that
`coordinate-geometry` lesson 4 is built on: «Хоёр шулууны **параллел**,
перпендикуляр байх нөхцөлийг налалт ашиглан тодорхойлох».

**What the drafts do:** they keep **«параллель»**, because the corpus is
decisive (64 against ~12) where the ministry is split 5–2. The working rule
that produces that answer is:

> **A split source does not outrank a unanimous one further down the order.**

**That rule is mine, not yours.** The opposite reading — *the ministry's more
frequent form wins, full stop* — is just as defensible from the text of
`MONGOLIAN.md`, and it would flip the spelling in **every geometry draft at
once** (nine of them use «параллель», `parallel-and-perpendicular` throughout).

**Why it matters beyond this word.** The same situation will recur: А/492 is a
long document assembled by several hands, and the next split it contains will
be decided by whichever rule is in force. Ruling once settles all of them.
Recorded in `GEOMETRY-TERMS.md` §1 as the working rule until you say otherwise.

---

### 2f. «эзэлхүүн» or «эзлэхүүн»? — **the corpus says our shipped term is the minority one**

**Found 19 Sep 2026 drafting `geometry/surface-area-and-volume`.** Same shape
as 2e, but this one is sharper: the tie-breaker I proposed in 2e points away
from a term that is **already live in the grade 6–8 mirrors**.

| form | А/492 | shipped mirrors | ЭШ bank | total corpus |
|---|---|---|---|---|
| **эзэлхүүн** | 1 | 18 | 5 | **23** |
| **эзлэхүүн** | 1 | **61** | **79** | **140** |

А/492 writes both, one each: «эзэлхүүн» on the calculus line, «эзлэхүүн» on
the line that names all five solids. So the ministry is split exactly as it is
on «параллел/параллель», and **2e's rule (a split source is broken by the
corpus) says «эзлэхүүн» — by six to one overall, and by sixteen to one in the
ЭШ bank, which is the exam our students actually sit.**

**The drafts keep «эзэлхүүн»**, because it is what shipped and because your
`mn-translation` skill glossary lists it. I want to be plain that this is **the
shipped-term argument overriding the rule I proposed one item earlier**, and I
did not flip it because changing a live term on my own authority is not my
call.

**Either answer creates work, and the second creates a rule:**

- **«эзлэхүүн» wins** → 18 shipped strings change, plus this draft, plus an
  edit to the skill glossary.
- **«эзэлхүүн» wins** → 2e needs an explicit carve-out: *a term that has
  already shipped is not overturned by a corpus count.* That carve-out should
  be written down now rather than improvised at the next split.

**A related one you do not need to rule on, recorded so you can see the
pattern.** The same ministry line spells *surface area* «гадаргуу**н** талбай»
where 32 shipped strings and the skill glossary write «гадаргуу**гийн**
талбай». The drafts keep «гадаргуугийн»: it has shipped, the glossary fixes
it, and «гадаргуун» is most likely a slip, since «гадаргуу» ends in a long
vowel and takes «-гийн». А/492 makes others — it prints «томъёо» with a hard
sign (flagged in unit 8) and «эзлэхүүн» on that same line. **The standard is
authoritative on vocabulary, not on orthography**, and that distinction is
worth stating once.

---

### 2g. The authority order has nothing to say about a term the course already taught — **a rule I invented, and the one I am most confident about**

**Found 19 Sep 2026 drafting `9/equations-and-formulas`.** Third gap in the
same order, after 2e (a source contradicting itself) and 2f (a corpus count
against a shipped term). This one is different from both: here the sources do
not conflict at all, and the question is whether they are even the right place
to look.

Grade 9's `equations-and-formulas` re-teaches four lessons that the grade 8
mirror **already ships in Mongolian**. For *identity* my own coinage would
have been «ижилтгэл» (0 everywhere); А/492 writes **«адилтгал»** six times,
and `data/genmath/8-mn/linear-equations.json` — live, for months — already
teaches this exact concept with it:

> «Тэгшитгэл гэдэг нэг хариутай оньсого төдийгүй **адилтгал** ч, боломжгүй
> зүйл ч байж чадна…»

The same shipped lesson fixes *no solution* as «шийдгүй» and *infinitely many*
as «төгсгөлгүй олон» (I would have written «тоогүй олон», also 0).

**Here ministry and shipped agree, so nothing is at stake today.** The rule is
for the day they don't, and I want it written before that day:

> **When a topic re-teaches material the student has already met in a shipped
> mirror, the shipped wording wins — ahead of the ministry, ahead of the
> dictionary — for the terms that overlap.**

The reason is not authority, it is the student. A course that calls the same
object «адилтгал» in grade 8 and something else in grade 9 has introduced a
second concept where there is one. **The authority order answers "which word
is most correct"; this answers "which word did we already teach them", and
across a grade boundary the second question outranks the first.**

Note this cuts the *opposite* way from 2f, where I kept a shipped term against
a corpus count and asked you for a carve-out. Both point the same direction —
**shipped beats counted** — which suggests one rule rather than two
exceptions. If you accept that, 2e, 2f and this item collapse into: *sources
choose a new word; a word already in front of students is not re-chosen.*

**This will recur.** Grade 9 sits directly on top of the shipped grades 6–8,
so every remaining grade 9 topic should be checked against those mirrors
before its terminology is decided, not after. I have added that step to the
drafting loop.

#### Update, 20 Sep: the first draft where this rule decided more than the ministry did

**`algebra-2/radicals-and-rational-exponents`.** Until now 2g has settled one
or two words per draft, always alongside a ministry that also had a view. Here
it settles four, **the ministry has no view on any of them**, and three of the
four are words the grounding pass would have got wrong:

| term | `8-mn/roots` ships | what grounding alone would have produced |
|---|---|---|
| perfect square | **гүйцэд квадрат** (30 uses) | «бүрэн квадрат» |
| perfect cube | **гүйцэд куб** (4) | «бүрэн куб» |
| cube root | **куб язгуур** | «кубын язгуур» |
| index (of a radical) | **индекс** (7) | «зэрэглэгч» / «үзүүлэлт» |

А/492 contains none of the four, and the reason is structural rather than
accidental: **it is a grade 10–12 standard and roots are taught in grade 8**,
so the standard never says the words. The dictionary's supplied a–i range does
not reach «язгуур» either. Without 2g the grounding pass would have had nothing
to stand on and would have coined four terms contradicting Mongolian a student
read last year.

**This argues the rule is stated too weakly.** 2g is currently written as a
tie-breaker for overlapping terms. Here it is not breaking a tie — it is the
only source there is. The strong form:

> **A shipped mirror is an authority, not a tie-breaker: below the ministry
> where both speak, above everything where the ministry is silent.**

That also covers the structural gap the four terms expose — А/492 starts at
grade 10, so **every grade 6–9 term is outside it by construction**, and a
rule that only breaks ties leaves all of them unsourced.

## 3. Terms I coined — ungrounded, and I know it

Each is built from grounded parts, defined on first use, and flagged in its
draft. None is in the dictionary's a–i range or in А/492 or the corpus.

> **Read this list by WHERE the terms cluster — it is a finding about the
> sources, not about the drafting.** With eleven of thirteen geometry topics
> drafted, the coinages are concentrated almost entirely in six of them:
> `foundations`, `reasoning-and-proof`, `parallel-and-perpendicular`,
> `triangles-and-congruence`, `relationships-in-triangles`,
> `quadrilaterals-and-polygons`. Those six are exactly the **grades 7–9 plane
> geometry and proof** topics. The five that fall outside that band cost
> **one to four coinages each**: `right-triangles-and-trig` 1,
> `area-and-perimeter` 1, `similarity` 2, `coordinate-geometry` 3,
> `circles` 4.
>
> The reason is structural and is now `GEOMETRY-TERMS.md` §6 version 3:
> **А/492 covers grades 10–12, the shipped grade 6–8 mirrors cover grades
> 5–8, and grades 7–9 plane geometry falls in the gap between them.**
>
> So the honest summary of this whole section is: **as far as our three
> sources record it, Mongolian school maths has no settled vocabulary for
> plane-geometry proof.** If you know a source that does — a school textbook
> series, a teachers' handbook — one pointer would retire most of this list
> at once, and would be worth more than ruling on the terms one by one.

| Term | For | Where | Uses |
|---|---|---|---|
| **тэг үржвэрийн чанар** | zero-product property | `quadratic-equations` L2 | titles the lesson's central idea |
| **давхардсан шийд** | repeated root | `quadratic-equations` L4 | 2 |
| **босоо шулууны шалгалт** | vertical line test | `functions` L1 | 7 |
| **цэг-налалтын хэлбэр** | point-slope form | `linear-functions` L3 | 9 |
| **өндөрсөлт / урагшлалт** | rise / run | `linear-functions` L1 | throughout |
| **тогтмол гишүүн** | constant term | `expressions-and-operations` L1 | 2 |
| **онцгой үржвэр** | special products | `polynomials-and-factoring` L2 | lesson title |
| **цацраг** / **эсрэг цацраг** | ray / opposite rays | `geometry/foundations` L2, L5–L8 | throughout |
| **транспортир** | protractor | `geometry/foundations` L5, L6, L8 | 9 |
| **дэлгэсэн өнцөг** | straight angle | `geometry/foundations` L6 | throughout L6 |
| **хэтэрсэн өнцөг** | reflex angle | `geometry/foundations` L6 | 2 |
| **шугаман хос** | linear pair | `geometry/foundations` L7 | throughout L7 |
| **өнцөг нэмэх постулат** | Angle Addition Postulate | `geometry/foundations` practice | 1 |
| **адил талт / элдэв талт гурвалжин** | equilateral / scalene triangle | `geometry/triangles-and-congruence` L1 | throughout |
| **алс дотоод өнцөг** | remote interior angles | `geometry/triangles-and-congruence` L2 | throughout L2 |
| **өөртэйгөө тэнцэх чанар** | Reflexive Property | `geometry/triangles-and-congruence` L6 | 1 |
| **хүндийн төв** | centroid | `geometry/relationships-in-triangles` L3 | throughout L3 |
| **өндрийн огтлолцлын цэг** | orthocenter | `geometry/relationships-in-triangles` L4 | ~15, incl. the lesson title |
| **дундаж шугам** | midsegment | `geometry/relationships-in-triangles` L5 | throughout L5 |
| **эсрэг орших тал / өнцөг** | opposite sides / angles | `geometry/quadrilaterals-and-polygons` | ~40 — see 4e |
| **дельтоид** | kite | `geometry/quadrilaterals-and-polygons` L5 | throughout L5 |
| **дараалсан өнцөг** · **харилцан хуваах** | consecutive angles · bisect each other | `geometry/quadrilaterals-and-polygons` L2–L3 | throughout |
| **шууд бус хэмжилт** | indirect measurement | `geometry/similarity` L6 | a section heading, ~6 |
| **томсголт** · **багасгалт** | enlargement · reduction | `geometry/similarity` L6 | 4 — see below |
| **онцгой тэгш өнцөгт гурвалжин** | special right triangles | `geometry/right-triangles-and-trig` L3 | lesson title |
| **эсрэг орших катет** | opposite leg | `geometry/right-triangles-and-trig` L4–L6 | throughout — the dictionary has only the other half |
| **төвийн өнцөг** | central angle | `geometry/circles` L1, L3, L6 | throughout |
| **харгалзах нум** | intercepted arc | `geometry/circles`, every lesson | **has a rival, see 4f** |
| **бага нум / их нум** | minor / major arc | `geometry/circles` L1 | 4 |
| **зайн томьёо** · **дундаж цэгийн томьёо** | distance / midpoint formula | `geometry/coordinate-geometry` L1–L2 | throughout — the ministry states the task, never names the formula |
| **координатын баталгаа** | coordinate proof | `geometry/coordinate-geometry` L6 | lesson title |
| **будсан муж** | shaded region | `geometry/area-and-perimeter` L6 | throughout — both halves grounded |
| **хатуу хөдөлгөөн** | rigid motion | `geometry/transformations` L1–L6 | throughout — it carries the whole argument of L6 |
| **гулсах тусгал** | glide reflection | `geometry/transformations` PRACTICE | 1, in `geo12-pr-8`'s solution — see below |
| **эхний ялгавар** | first differences | `9/introduction-to-functions` L5 | throughout L5, incl. its keyIdea — the first grade 9 coinage |
| **үсгэн тэгшитгэл** | literal equation | `9/equations-and-formulas` L4 | lesson title, concept 1 and the topic BLURB — the most exposed grade 9 coinage |
| **боломжгүй тэгшитгэл** | contradiction (the species) | `9/equations-and-formulas` L2 | 4 — grown from the shipped «боломжгүй зүйл» |
| **нөхцөлт тэгшитгэл** | conditional equation | `9/equations-and-formulas` L2 | 3 — rides on «нөхцөлт өгүүлбэр», itself flagged |
| **харьцаа** (of a progression) | common ratio | `11/sequences-and-series` L3, L5, L6 | throughout — the only ungrounded term in that topic; Russian says *denominator*, see 4h |
| **нийлэхгүй** | diverge | `11/sequences-and-series` L6 | 5 — negated from the ministry's own «нийлэх» |
| **аравтын · натурал логарифм** | common · natural logarithm | `11/logarithms` L2, and the next draft | Russian calques; **«натурал» means *natural number* in the bank, 29 times** — see 4i |
| **децибел · хүчиллэг · Рихтерийн хэмжүүр** | decibel · acidity · Richter scale | `11/logarithms` L6 | throughout L6 — chemistry and seismology, not maths; a science teacher's eye is worth more than mine |
| **суурь солих томьёо** | change of base | `algebra-2/exponentials-and-logarithms` L3 | a concept, a worked example, a teach step and the facts table |
| **хориотой утга** | excluded value | `10/rational-expressions` L1, L2, L5 | carries L1 entirely |
| **хуурамч шийд** | extraneous solution | `10/rational-expressions` L5 | **21 uses** — and it reverses the two logarithm drafts, see 4k |
| **хорогдуулах** | to cancel a factor | `10/rational-expressions` L2, L3 | corpus 1 — thin, but it cannot be confused with subtraction |

**`geometry/reasoning-and-proof` adds fourteen more, and they are a different
problem.** They are not listed one by one here because they form groups that
should be ruled on together, and `memory/mn-drafts/geometry-reasoning-and-proof.md`
§Notes has them in those groups with the reasoning for each. The summary:

| group | terms |
|---|---|
| the two kinds of reasoning | индуктив сэтгэлгээ · дедуктив сэтгэлгээ |
| conjecture machinery | зүй тогтол (pattern) · эсрэг жишээ (counterexample) |
| conditionals | нөхцөлт өгүүлбэр · урвуу өгүүлбэр · эсрэг урвуу өгүүлбэр · хос нөхцөлт өгүүлбэр · хэрэв бөгөөд зөвхөн хэрэв · силлогизмын хууль |
| the reason column | тэнцэтгэлийн нэмэх / хасах / үржүүлэх / хуваах чанар · шилжих чанар |

**Why logic is emptier than geometry was.** Geometry's plane vocabulary was
thin because А/492 is a grade 10–12 standard. Logic is thin for a different
reason: Mongolian school maths teaches proof *inside* geometry rather than as
a named subject, so there is no settled word list to inherit at all. Every one
of the fourteen scores zero in the ministry order, the dictionary's a–i range
**and** the shipped corpus.

**Two of the fourteen are worth answering before anything else.** «хэрэв
бөгөөд зөвхөн хэрэв» for *if and only if* is a clumsy calque, and if you know
the phrase Mongolian textbooks use, that one answer settles three terms at
once. And the six property-of-equality names are **the reason column of every
proof the course will ever print**, so they will be read more often than
almost any other phrase on the site.

**The geometry rate is three times the algebra rate, and that is the sources
speaking.** А/492 is a grade 10–12 standard, so it is silent on plane geometry;
the dictionary's a–i range holds 20 of the 75 terms this strand needs; the
shipped grade 6–8 mirrors carry almost none of the vocabulary. Counts and the
full inventory are in `memory/mn-drafts/GEOMETRY-TERMS.md`. Two of the seven
above are worth your eye before the other twelve geometry topics are drafted:
**«цацраг»**, because its 10 corpus uses are all *light* rays and it is threaded
through five lessons, and **«дэлгэсэн өнцөг»**, because *straight* and *right*
both want «тэгш» in Mongolian and lesson 6 leans hard on keeping them apart.

### A coinage that grounding overturned — «томсголт» → «гомотет»

**Worth your eye because it says something about the other twenty-odd rows
above.** `GEOMETRY-TERMS.md` had booked **«томсголт»** for *dilation*, marked
«0 everywhere» — a coinage. Drafting `geometry/similarity` grounded it
properly and found the ministry already has the word:

> «Координатын хавтгай дахь дүрсийг **гомотетоор** хувиргах» — А/492, 10-р анги

with the ЭШ bank using it in exactly this unit's shape: «$k=-2$
**коэффициенттэй гомотетоор** хувиргахад». Ministry 1 · corpus 7 against a
coinage at 0, so the drafts and the terms file now say **«гомотет»**. Nothing
shipped on the coinage, so the correction is free.

**«томсголт» was then re-used for what it literally means** — *enlargement*
($k>1$), paired with **«багасгалт»** for *reduction* — which is exactly why it
was wrong for *dilation*, since a dilation with $0<k<1$ shrinks.

**The lesson, and the reason it is here rather than only in the terms file.**
This is the **second** grounding pass to correct that file instead of
confirming it («диагонал» → «диагональ» was the first). Both times the term
had entered from a *lesson's* needs before any topic exercised it. So: **a row
in `GEOMETRY-TERMS.md` is a proposal until a topic grounds it**, and the rows
marked «0 everywhere» — which is most of §3 above — are the ones most likely
to have a real Mongolian word waiting behind them. That is an argument for
ruling on the list rather than letting it ship by default, not an argument
that the list is wrong.

**It has now happened four times, and the last topic did it twice in one
pass.** Drafting `geometry/transformations` (19 Sep) found *translation* →
**«параллель зөөлт»** sitting in А/492 verbatim, against the file's coinage
«шилжүүлэлт» at 0, and found the dictionary's **«угсраа хувиргалт
(композиц)»** (p. 73) for *composition*, which the file had no entry for at
all. The same pass caught **«тодорхойлогч»** for *determinant* (ministry 2,
verbatim) one draft *before* I would have coined «детерминант» — the first
time the order has run that way rather than a unit late.

**So the headline number above is now measured, not guessed.** Of the seven
«0 everywhere» rows `GEOMETRY-TERMS.md` §3 carried before this unit, a source
answered three. That is a hit rate high enough that the remaining four, and
the twenty-odd coinages in the table above, are worth an hour of your time
rather than a default ship. **The strongest form the evidence supports: a
«0 everywhere» row is not a word this file invented, it is a question this
file has not asked yet.**

**Grade 9 opens at the algebra rate, not the geometry rate.** The first grade 9
topic, `9/introduction-to-functions`, adds fourteen terms and **one** of them is
a coinage — «эхний ялгавар» for *first differences*, above. Everything else
grounded: «өөрчлөлтийн хурд» ministry 1, «шугаман» ministry 9, «график»
ministry 32, «цэгийн координат» ministry 4, «завсар» ministry 2. That is the
sources speaking again, in the other direction this time: А/492 is a grade
10–12 standard and grade 9's function vocabulary is exactly what it covers,
where plane geometry is exactly what it does not. **Expect the remaining six
grade 9 topics to need far less of your time than the thirteen geometry ones
did.**

One grade 9 decision was made rather than asked, and the reason is that you
already made it: *nonlinear* is **«шугаман биш»**, not «шугаман бус», on the
identical evidence that corrected «тэнцэтгэл бус» → «тэнцэтгэл биш» in
`CLAUDE.md` (there: ministry 13 vs 0; here: corpus 1 vs 0). Say the word if
you want the «бус» form anywhere.

**The ЭШ-first queue changes what grounding looks like, and the first topic
under it is the best-grounded in the programme.** `11/sequences-and-series`
adds fourteen terms and **one** is ungrounded (4h). The reason is structural
rather than lucky: А/492 is a grade 10–12 standard, so the ЭШ course's own
subject matter is precisely what it covers, and the ЭШ past papers supply the
rest in the exam's own words. Two terms came from the bank alone — «ялгавар»
for *common difference* (four past papers, verbatim) and «рекуррент» for
*recursive* (two) — neither of which А/492 names.

**It also produced the first case where a source overrides the English's own
vocabulary rather than supplying a word for it.** The English says "arithmetic
sequence"; А/492 and 52 past-paper occurrences say «арифметик **прогресс**».
Both «прогресс» and «дараалал» are ministry words doing different jobs, so
nothing is lost — but a lesson *title* changes, which is new. Details in that
draft's Notes 1.

**Topic 2 of grade 9 pushed the rate back up, and the reason is instructive.** Grade 9's
`equations-and-formulas` adds three coinages — «үсгэн тэгшитгэл», «боломжгүй
тэгшитгэл», «нөхцөлт тэгшитгэл» — after topic 1 added one. All three name the
*abstractions* (a species of equation, a kind of equation) rather than the
*objects*; the objects in that topic were all settled already, three of them
by a mirror that shipped months ago (item 2g). **The pattern across
twenty-eight drafts now looks like this: sources name things, and they are
much thinner on names for kinds of things.** «постулат», «урвуу өгүүлбэр»,
«нөхцөлт өгүүлбэр», «индуктив сэтгэлгээ» and now these three are all the same
shape. If you want to spend one sitting on the highest-leverage group in this
file, it is that one.

**The best-grounded topic in the programme is now
`algebra-2/radicals-and-rational-exponents`**, which adds twenty terms and
leaves **two** ungrounded — «ижил язгуурт гишүүд» (*like radicals*) and
«язгуурын доорх илэрхийлэл» (*radicand*), both compositional and low-risk. The
first is built from the exam's own adjectival «язгуурт» (as in «Квадрат
язгуурт функц», 12 uses) and parallels «ижил төрлийн гишүүд» for *like terms*
in `algebra-1/expressions-and-operations`, so a student meets a familiar shape;
you may prefer the fully parallel «ижил төрлийн язгуурт гишүүд», which is
longer. Everything else in the topic came from a source, and one term came from
the exam **verbatim as a question stem**: *rationalize the denominator* is
«хуваарийг иррационалаас чөлөөлөх», which the ЭШ bank asks in exactly those
words.

> **One term there is a deliberate borrowing you should see, because it makes
> a promise about a topic that does not exist yet.** *Conjugate* is
> **«хосмог»** — an А/492 word (3 uses), but all three are the **complex**
> conjugate (12.4г, «хосмогоор үржүүлэх» in 12.4и). The standard never
> discusses radical conjugates.
>
> I used it for the radical conjugate anyway because the English lesson is
> built on the link: it says the conjugate trick is *"the same trick that
> cleared complex denominators in Unit 2"*, and the fact card repeats it. One
> word for one idea is what the source is arguing; a different word here would
> break the cross-reference the lesson exists to make.
>
> **The cost: the word arrives in Mongolian before the topic that grounds it.**
> `algebra-2/quadratics-and-complex-numbers` is not drafted, and when it is it
> **must** use «хосмог» or the link fails retroactively. That is a constraint
> on a future draft created by this one — flagging it so it is a decision you
> made rather than one a later session inherits silently.

**The one coinage in the last geometry topic that stayed a coinage** is «гулсах тусгал»
for *glide reflection*: zero in А/492, zero in the dictionary's a–i range,
zero in the corpus, in every word order I tried. Both halves are grounded
separately («гулсах» ships as a verb twenty times; «тусгал» ships nine), and
it appears exactly once, naming a composition the student has just computed —
so the exposure is one practice solution, not a lesson.

---

## 4. Wording conflicts where the sources disagree and the ministry is silent

### 4a. «тархах хууль» versus «гишүүнчлэн үржүүлэх чанар» (the distributive law)

The shipped corpus says «тархах хууль», 15 times. The dictionary prints
«гишүүнчлэн үржүүлэх чанар» (p. 190) and «үржвэрийг нийлбэрээр илэрхийлэх
чанар» (p. 123) — and separately reserves «тархалт» for *probability*
distributions (p. 123, marked for those subjects). So our wording makes the
algebraic law and the probability distribution share a root, which the book
deliberately does not.

**Nothing changed.** Both `polynomials-and-factoring` and
`expressions-and-operations` route around it by teaching the move («хаалт
нээх», «гишүүн бүрээр үржүүлэх») without naming the law, so neither needs a
rewrite whichever way you rule. Adopting the dictionary's phrase would be a
corpus-wide rename and should be its own pass.

> **Update, 17 Sep 2026: routing around it has stopped working.** A proof cites
> the Distributive Property **as a reason on a line of a two-column proof**, and
> a reason must have a name. `geometry/reasoning-and-proof` lesson 5 does this
> four times, and every algebraic-proof reason column the course ever writes
> will do it again.
>
> The draft uses **«хаалт нээх чанар»**, which is what the algebra drafts
> already teach, against the dictionary's «гишүүнчлэн үржүүлэх чанар» and the
> corpus's «тархах хууль» (15 uses). So this item now has a concrete cost
> attached rather than being free to leave open.

### 4b. `absolute value` — open since 13 Sep

The book's «абсолют хэмжигдэхүүн» against 53 live uses of «абсолют утга».
Ministry silent. Does not touch any topic drafted since.

---

### 4c. `statement` in a proof: «өгүүлбэр» against the book's «хэллэг»

The printed dictionary uses «хэллэг» for *statement* throughout, including at
p. 84 where *"this new statement is called the converse"* becomes «…урвуу
хэллэг гэж нэрлэдэг». The drafts use **«өгүүлбэр»**, because «хэллэг» reads as
*phrase* or *idiom* in ordinary Mongolian and `geometry/foundations` lesson 8
asks a student to pair a **statement** with a **reason** in two columns.

**This is a live conflict with a printed source and I did not settle it.** It is
cheap now and expensive later: unit 2 is *Reasoning & Proof* and every topic in
it is built on the word.

> **Update, 17 Sep 2026: unit 2 is now drafted, so "later" has started.**
> «өгүүлбэр» appears in every lesson of `geometry/reasoning-and-proof` and will
> appear in every proof of units 3–8. **This is the highest-value ruling in
> this file after the register question**, because unlike the others its cost
> grows with every topic drafted rather than staying fixed.

### 4d. Two dictionary overrides of the `mn-translation` skill glossary

The skill's geometry list calls itself *"canonical — do not improvise
synonyms"*, but two of its angle-pair entries never shipped and the dictionary
prints something else:

| English | skill glossary | shipped uses | dictionary | drafts use |
|---|---|---|---|---|
| complementary angles | нэмэлт өнцөг | 1 | **гүйцээлт хоёр өнцөг** | dictionary |
| adjacent angles | зэргэлдээ өнцөг | **0** | **залгаа хоёр өнцөг** | dictionary |

The authority order in `docs/MONGOLIAN.md` puts the dictionary above the shipped
corpus, so the drafts follow the dictionary and say so where they do. **The skill
file is yours to amend, not mine** — and «гүйцээлт» is also the skill's word for
*complement* in probability, so adopting it here makes one word carry two
meanings. That collision is the reason this is a question rather than a
correction.

### 4e. Two ministry words that are already taken — a new failure mode

**Found 18 Sep 2026, drafting `parallel-and-perpendicular`.** Everything above
in this file is a *gap*: a term scores zero and has to be coined. These two are
the opposite and they are worse, because **the count looks like permission**.
The word scores in А/492 — but in a different sense, one this same course will
need later.

| Word | А/492 uses it for | What wanted it | Done |
|---|---|---|---|
| **солбисон** | **skew lines** (12-р анги) | *alternate* angles — the obvious Russian-tradition calque | **not used**; the pair names state their positions instead |
| **огтлогч** | a circle's **secant** (10-р анги) | *transversal* | full **«огтлогч шулуун»** throughout, never the bare word, so `geometry/circles` keeps «огтлогч» |

**A third one turned up in unit 5, and it needed handling differently** —
which is what turned this from an incident into a rule.

| Word | А/492 uses it for | Wanted by | Kind |
|---|---|---|---|
| **медиан** | the **statistical median** (10-р анги, 4 uses; corpus 146, all statistics) | a triangle's median | **cross-strand** |

A statistics lesson and a geometry lesson never share a page, so unlike the
first two this one is **managed rather than avoided**: the term is introduced
as **«гурвалжны медиан»** and shortened only inside the lesson. The rule the
strand now follows:

> **In-strand collision → the word is unavailable. Cross-strand collision →
> keep the head noun on first use.**

All three, and that rule, are in `memory/mn-drafts/GEOMETRY-TERMS.md` §4 so the
remaining one geometry topic inherits them instead of rediscovering them.

**A fourth one turned up in unit 6, and it is ours rather than the ministry's
— which makes it the only one you can actually fix.** Unit 1 took
**«эсрэг өнцөг»** for *vertical angles* from the `mn-translation` skill
glossary; it had **zero shipped uses**, no dictionary entry, and was flagged
at the time. Unit 6 needs the same phrase for a parallelogram's **opposite
angles** — same strand, four units apart. So unit 6 writes «эсрэг орших тал /
өнцөг» about 40 times.

**Which term should move is the question.** *Opposite* has the better claim on
«эсрэг», because that is what the word means; *vertical angles* never had a
grounded claim on anything. Candidates for vertical angles, all ungrounded:
«оройн эсрэг өнцөг», «огтлолцлын эсрэг өнцөг», «вертикаль өнцөг». **I did not
change it** — that would rewrite a term already settled across four drafts on
my own initiative. But it is cheap now and expensive after seven more topics,
and it is the one place where a flagged ungrounded choice has since cost
something measurable.

**What replaced «солбисон», and the one thing worth your eye.** The four
transversal pair names are built to state their own positions:

| English | this draft | literally |
|---|---|---|
| alternate interior | **эсрэг талын дотоод өнцөг** | opposite-side interior |
| alternate exterior | **эсрэг талын гадаад өнцөг** | opposite-side exterior |
| same-side interior | **нэг талын дотоод өнцөг** | same-side interior |

Lesson 1 of that unit is entirely about naming angles **by position**, and its
English has to stop and explain that *alternate* means *opposite sides*. The
Mongolian names say it, so the lesson teaches itself — this is the rewrite rule
working, not a translation. **The risk:** «эсрэг өнцөг» alone is *vertical
angles* from unit 1, so «эсрэг талын …» must always keep «талын». If a teacher
would hear those as one family, say so before ten more geometry topics use
both.

**Whether to keep «огтлогч шулуун» is a decision for two topics at once**, this
one and `circles`. The collision-free alternative is «хөндлөн шулуун».

### 4f. «харгалзах нум» for *intercepted arc*, against the «нумд тулсан» construction

**`geometry/circles`, every lesson, and lesson 3's theorem is stated with it.**
This is the one term in that topic I am not sure about even after the sources,
which is what this file is for.

The draft writes the intercepted arc as a noun phrase, **«харгалзах нум»**.
«харгалзах» is grounded (corpus 5) and this strand already uses it for
*corresponding* sides and angles, so the compound reads naturally and the head
noun «нум» keeps it distinct from those.

**But Mongolian school geometry, descended from the Russian tradition,
normally expresses this relation from the angle's side**, with «тулсан»
(resting on / subtending): «AB нумд тулсан өнцөг» for the angle, rather than
naming *the intercepted arc* as a thing. If that is what a Mongolian textbook
says, the whole topic should be rewritten around it — the theorem would read
«нумд тулсан өнцөг тэр нумын хагастай тэнцүү» instead of «багтсан өнцөг
харгалзах нумынхаа хагастай тэнцүү».

**Neither scores anything** in А/492, the dictionary's A–I range, or the
corpus, so the sources genuinely do not decide it. **If you know the phrase,
that one answer settles the topic** — it is a find-and-replace in one file,
but it touches every lesson.

---

### 4g. *Reflection*: both sources say «тэгш хэм», and that name is already lesson 4's

**`geometry/transformations`, lessons 2 and 4.** The only term in the last
geometry topic I could not settle from the sources — because here the sources
are clear and following them breaks the topic.

Both authorities call a reflection a kind of **symmetry**:

| source | wording |
|---|---|
| А/492, 10-р анги | «…дүрсийг **тэгш хэмээр (цэгийн, тэнхлэгийн)** хувиргах…» |
| dictionary p. 13, p. 73 | «**тэнхлэгийн хувь дахь тэгшхэм**» |

The topic has seven lessons and two of them are affected. Lesson 2 is
"Reflections (Flips)"; lesson 4 is literally "Symmetry", and its entire content
is that *a reflection can map a figure onto itself*. Name them both «тэгш хэм»
and lesson 4's sentence becomes «тэгш хэм дүрсийг өөр дээр нь буулгавал тэр
дүрс тэгш хэмтэй» — true, circular, and useless as teaching.

**The draft keeps the shipped «тусгал»**, which the grade 6–8 mirrors use nine
times and in all three senses this topic needs («тэнхлэгийн тусгал», «толин
тусгал», «шулуунаар тусгасан тусгал»). Lesson 4 then has «тэгш хэм» to itself
and reads properly: «тусгал дүрсийг өөр дээр нь буулгавал тэр дүрс тэгш
хэмтэй».

**What I need from you.** This is the first time a draft has knowingly declined
a ministry word for a reason other than a spelling split (4e). Either:

- **keep «тусгал»** — the English's distinction survives, and one term in the
  strand diverges from А/492 on purpose; or
- **follow the ministry** — lessons 2 and 4 are rewritten around «тэнхлэгийн
  тэгш хэм» vs «тэгш хэм», which I think is a thinner distinction than the
  English carries, but it is your call and the divergence disappears.

Nothing has shipped either way, so the reversal is one find-and-replace in one
file plus two lesson rewrites if you pick the second.

#### Update, 20 Sep: evidence that this may not be a conflict at all

**`algebra-2/radicals-and-rational-exponents` lesson 4 needs both ideas in one
sentence** (the inverse's graph *is symmetric* about $y = x$; the inverse *is
the reflection* of $f$). That forced another look, and the shipped mirrors turn
out to already draw the line this topic needs:

> `6-mn/integers`: «…**тэгш хэмтэй** — нэг тал нь нөгөөгийнхөө шулуунаар
> тусгасан **тусгал** юм.»

One sentence, both words, different jobs: **«тэгш хэмтэй» for the property**
(being symmetric), **«тусгал» for the operation and its image** (the
reflection). The counts fit a division of labour rather than a competition —
«тэгш хэмтэй» is exam 31 / shipped 11 / ministry 1; «тусгал» is exam 0 /
shipped 7 / ministry 0. They never contend for the same slot.

The ministry's inverse-function line reads the same way: 11.3е says the graph
is «шулууны хувьд **тэгш хэмтэй**» — the property, not the map. So the new
draft writes *symmetric about y = x* as «y = x шулууны хувьд тэгш хэмтэй» and
*the reflection* as «тусгал», in one lesson, with no collision.

**If that split holds, 4g is not a ruling to make but a distinction to write
down**, and `geometry/transformations` is already consistent with it: lesson 2's
«тусгал» is the operation, lesson 4's «тэгш хэм» is the property. That is
exactly the division above — the draft reached it from the English and the
mirrors reached it independently.

I have **not** edited `GEOMETRY-TERMS.md`, which lists the two as competitors
in §3. Thirteen geometry drafts cite that file and the change should be yours.
**This is now the cheapest item in the pile if the split is right**: one
paragraph in one shared file, and 4g closes without rewriting anything.

---

### 4h. A geometric progression's ratio: «харьцаа», or the Russian calque «хуваарь»?

**`11/sequences-and-series`, lessons 3, 5 and 6.** The one term in that topic
no source names — and the topic is otherwise the best-grounded in the
programme, so this single gap stands out.

The draft writes **«харьцаа»** (ratio), compositional on a word the ЭШ bank
uses 55 times, always with the progression attached: «геометр прогрессийн
харьцаа».

**But Russian school maths calls it the progression's DENOMINATOR** —
*знаменатель прогрессии* — and Mongolian school vocabulary follows the Russian
tradition closely elsewhere in this very topic (that is why it says «прогресс»
and not «дараалал» at all). If the textbooks calqued it, the right word is
**«прогрессийн хуваарь»**.

I did not use it because «хуваарь» is already *denominator* in our glossary
(ministry 5 · corpus 176), and lesson 6 is full of fractions like $\tfrac12$
where both senses would sit in one paragraph. That is a real cost, but so is
using a word students have not met.

**This is a one-answer question.** If you know which one Mongolian textbooks
print, it settles three lessons and it is a find-and-replace in one file. The
ЭШ past papers gave no help: they always specify a geometric progression by
two of its terms or by $b_{n+1} = 2b_n$, never by naming the ratio.

---

### 4i. «натурал логарифм», when «натурал» already means *natural number* in the exam

**`11/logarithms` lesson 2, and `algebra-2/exponentials-and-logarithms` next.**
Neither *common logarithm* nor *natural logarithm* is named by А/492 or the
dictionary's a–i range, so both drafts follow the Russian tradition:

| English | draft | the calque | the grounded sense of the adjective |
|---|---|---|---|
| common log | **аравтын логарифм** | *десятичный* | «аравтын» = **decimal** (bank 10: «аравтын бутархай») |
| natural log | **натурал логарифм** | *натуральный* | «натурал» = **natural number** (bank 29: «хэдэн натурал шийдтэй вэ?») |

The first is comfortable. **The second puts a word the exam uses 29 times for
*natural number* in front of a logarithm**, in a course where the same student
meets both. I used it anyway — it is almost certainly what Mongolian textbooks
print, and the collision is only in the adjective, not the noun — but I want to
be plain that I chose a known collision rather than discovered no alternative.

**Rule on this before the next draft if you can.** `algebra-2/exponentials-and-logarithms`
is where $\ln$ and $e$ are actually taught, so the term earns its keep there
rather than here; a ruling now settles both drafts at once instead of one
retroactively.

---

### 4j. The ministry and the ЭШ papers name the same object differently — **now twice**

**`10/rational-expressions`, throughout.** Every earlier conflict in this file
was ministry-vs-dictionary (4d), ministry-vs-itself (2e), or
ministry-vs-shipped-mirror (2f, 2g). This one is **ministry vs the ЭШ exam**,
and nothing has shipped, so 2g does not decide it.

| source | wording | where |
|---|---|---|
| А/492 | «**алгебрын бутархай**» | twice, in the line that *is* lesson 4: «Хуваарь нь шугаман эсвэл квадрат олон гишүүнт байх алгебрын бутархайг нэмэх, хасах» |
| ЭШ papers 2025a/b/c | «**рационал илэрхийлэл**» | three times, as the section label |

**The draft leads with «рационал илэрхийлэл»** and puts «алгебрын бутархай»
beside it on first use, so a student meets both. My reasons: this is an ЭШ
topic and the exam's own label is what the student reads on the paper; it
matches the English's head term; and А/492 itself writes «**рационал**
тэгшитгэл» for lesson 5, so the standard is not avoiding the word.

**But I should be plain that this inverts the stated authority order.**
`docs/MONGOLIAN.md` puts the ministry first and the ЭШ bank inside «corpus».
Read strictly, «алгебрын бутархай» wins. My argument is that **the ЭШ bank is
not ordinary corpus for an ЭШ topic — it is the exam the course exists to
pass** — but that is a case for amending the order, not for quietly ignoring
it.

**So the real question is bigger than one word:** does the ЭШ bank outrank
А/492 *for ЭШ topics*? That would be a fifth clause in the authority order,
alongside 2e, 2f and 2g. Say yes and this draft stands as written; say no and
it is a handful of edits, since both terms are already on the page.

#### Second instance, 20 Sep: *range*

**`algebra-2/radicals-and-rational-exponents`, lesson 4.** The same split, on
a much commoner word:

| | ministry | ЭШ papers |
|---|---|---|
| domain | «тодорхойлогдох муж» (2) | «тодорхойлогдох муж» (25) |
| range | «**дүр**» (2, as «тодорхойлогдох муж ба дүр») | «**утгын муж**» (31) |

They agree on domain and split on range. The draft uses «утгын муж», which is
also what `algebra-2/exponentials-and-logarithms` already used — so this one is
*already* decided in the exam's favour across two drafts, which is the thing
worth flagging rather than the word itself.

**Why two instances matter more than one.** Both times the exam's word is the
commoner by an order of magnitude, and both times the topic is an ЭШ topic. That
is the same direction 2f and 2g point (*what students actually meet beats what a
document counted*). **Four findings now argue for one rule**, and ruling 2e, 2f,
2g and 4j separately will probably produce four compatible answers at four times
the cost. A single clause — *for ЭШ topics the exam bank outranks А/492; where
the ministry is silent the shipped mirrors outrank everything* — would close all
four.

---

### 4k. *Extraneous solution*: I coined «хуурамч шийд» after two drafts described it instead

**Found 20 Sep 2026 across three drafts.** No Mongolian source names this
concept. `11/logarithms` and `algebra-2/exponentials-and-logarithms`
**described** it («тодорхойлогдох мужаас гадуурх нэр дэвшигч»), and I argued
in the second that three topics describing one concept three ways would be
worse than one coinage used consistently.

**`10/rational-expressions` forced the issue: it needs the word twenty-one
times.** Lesson 5 is built on it — the concept, a fact row, a commonMistake, a
tapQuestion, a tryItSet option, the recap. Describing it twenty-one times is
not writing anyone would read. So that draft coins **«хуурамч шийд»**
(*fake solution*), which matches the English's own framing in that very
lesson: "the counterfeit answer", "fake detector", "fake-check".

**This is me reversing my own earlier choice**, and it leaves the three drafts
inconsistent until you rule. Concretely:

- **like «хуурамч шийд»** → two-line change to the logarithm drafts, all three
  agree;
- **prefer another word** → say it once, three drafts follow;
- **prefer the description kept** → `10/rational-expressions` gets much
  clumsier, and I would want to hear that explicitly.

**The cheapest moment to rule is now**: it lands again in
`algebra-2/radicals-and-rational-exponents` (ЭШ Algebra unit 7), which is two
drafts away, and after that in rational equations wherever they recur.

#### Update, 20 Sep: it landed, and it is now a lesson title

`algebra-2/radicals-and-rational-exponents` uses «хуурамч шийд» **17 times**,
and its lesson 3 is *titled* «Язгуурт тэгшитгэл ба хуурамч шийд». A lesson
title cannot be replaced by a description, so the hedge that carried the two
logarithm drafts is no longer available anywhere this concept appears.

I searched the ЭШ bank for an existing word before keeping the coinage —
«хуурамч шийд», «гадны шийд», «илүүдэл шийд» — **zero hits each**. There is no
exam wording to defer to, so 4j's rule would not decide this one either.

**What changed is the cost of a reversal**, not the argument: it is now four
drafts and a lesson title rather than three drafts, and the next two ЭШ Algebra
units are radical and rational equations, so it will keep growing.

---

### 4l. A wrong grounding in an earlier draft: «харилцан нэг утгат» is not what the ministry says

**Found 20 Sep while drafting `algebra-2/radicals-and-rational-exponents`,
whose lesson 4 is Inverse Functions.** This is a correction, not a conflict —
it needs a yes, not a ruling.

`algebra-2-exponentials-and-logarithms.md` records *one-to-one* as
**«харилцан нэг утгат»**, grounded as **"ministry 3, verbatim"**. It is not
verbatim. А/492 writes «харилцан нэг **утгатай**» all three times, and in two
of them the word is attributive — the position where a clipped «-т» would be
most tempting:

> 11.3е «…харилцан нэг **утгатай** функцийг таних, мэдэх»
> 11.3е «…өгсөн функц нь харилцан нэг **утгатай** эсэхийг тодорхойлох»
> 11.3ж «…харилцан нэг **утгатай** функцийн урвууг олох»

So the ministry's own attributive form carries `-тай`, and the earlier draft's
form appears in no source at all — not the standard, not the ЭШ bank, not any
shipped mirror.

The new draft uses «харилцан нэг утгатай», where the term carries lesson 4.
**The two drafts are adjacent units in the same ЭШ Algebra block**, so as
things stand a student would meet two spellings of one term inside one topic.

**I have not edited the earlier draft.** It is in this pile awaiting your read
and I would rather you saw the correction than found it silently applied. It is
a one-word change on one line; say the word.

*What this costs: nothing yet, which is the point.* It is the cheapest possible
version of the failure 2g exists to prevent — a term renamed across a boundary
— caught while both sides are still drafts and neither has shipped.

---

## 5. Things you said to ask about, which I have not decided

### 5a. The English term on first use

Your uploaded CLAUDE.md lists this as an open decision and says to ask before
adopting either convention site-wide: «өнцгийн биссектрис (angle bisector)».
**Not used anywhere.** Worth settling soon — every draft has terms an
English-medium exam will show in English.

### 5b. Three English acronyms dropped, not translated

**FOIL**, **PEMDAS** and now **CPCTC**. All three spell English sentences and spell
nothing in Mongolian. The lessons teach the rule and drop the acronym — for FOIL the
English itself says "the rule is just double distribution". The book does carry
FOIL («Хоёр хоёргишүүнт үржүүлэх арга», p. 163), so this is a choice, not a
gap. Flagging it because dropping a mnemonic a student may meet in an
English-medium exam is a content decision, not a translation one.

---

### 5c. The congruence acronyms are Mongolianised — **applied, and the biggest reversible call so far**

`geometry/triangles-and-congruence` writes **ТТТ · ТӨТ · ӨТӨ · ӨӨТ · ГК** for
SSS · SAS · ASA · AAS · HL (and **ӨӨӨ · ТТӨ** for the two that fail).

These are not names, they are **mnemonics that spell the parts out in order**,
and lessons 4 and 5 are *about* decoding them. «SAS» does none of that work for
a Mongolian reader; «ТӨТ» does all of it on sight. Keeping the Latin would
leave two lessons teaching a decoding skill for letters that cannot be decoded.

**The precedent is yours:** the `mn-translation` skill's statistics glossary
already writes **«ДАХ — дундаж абсолют хазайлт (MAD)»**.

**The case against:** a student in an English-medium exam sees SSS and SAS.
Smaller than it looks — ЭШ is Mongolian-only, and the SAT and IB hubs are
English-only by the locked decision in `memory/expansion-vision.md` §4.7, so
those forms reach that student through those hubs anyway.

**Cost to reverse:** one find-and-replace, about 75 occurrences across two
files — `geometry/similarity` lesson 3 now rides on the same call, writing the
similarity criteria as **ӨӨ · ТТТ · ТӨТ төстэйн шинж**. This is the most
visible divergence from an English mirror in any draft, and it is fully
reversible, which is why I made the call rather than blocking the topics on it.

**One thing survives either ruling: the qualifier.** «ТТТ **тэнцүү**-гийн
шинж» and «ТТТ **төстэй**-н шинж» are different theorems, and the English
distinguishes them only by context ("SSS congruence" vs "SSS similarity"). The
Mongolian says which one every time, whichever alphabet the letters end up in.

### 5d. SOH-CAH-TOA is REBUILT, not dropped and not transliterated — a third kind

**Applied in `geometry/right-triangles-and-trig` lesson 4, 18 Sep 2026.**
Neither precedent above fits, so this is its own call and the most visible one
in that topic.

| Precedent | What was done | Why |
|---|---|---|
| FOIL · PEMDAS · CPCTC (5b) | **dropped**, rule taught without the mnemonic | they spell English sentences and nothing else |
| SSS · SAS · ASA (5c) | **Mongolianised** to ТТТ · ТӨТ · ӨТӨ | they are initials of the parts, and the lessons teach decoding them |
| **SOH-CAH-TOA** | **rebuilt from the Mongolian words**: **Э/Г · Н/Г · Э/Н** | see below |

SOH-CAH-TOA is not initials of a definition the way SSS is. It is three
pronounceable nonsense syllables whose entire value is that they are easy to
chant, and that value does not survive any translation. But dropping it the way
5b drops FOIL would leave lesson 4's "memory hook" step with no memory hook,
and the hook *is* the content of that step.

So the draft builds the Mongolian one from the Mongolian side names —
эсрэг/гипотенуз, налсан/гипотенуз, эсрэг/налсан → **Э/Г · Н/Г · Э/Н**. It
reads as three fractions and decodes on sight.

**The English form is glossed once**, in the last beat of the step that
introduces the rule, so a student meeting it in an English-medium exam has seen
it. The lesson title «Trigonometric Ratios (SOH-CAH-TOA)» drops the
parenthetical and reads «Тригонометрийн харьцаа».

**Cost to reverse:** about a dozen places in one file, the same size of change
as 5c. Say the word and SOH-CAH-TOA goes back in everywhere.

---

## 6. Bugs found while drafting that are not translation questions

### 6a. Single-asterisk italics ship as literal asterisks. 3,024 of them.

`components/esh/MathText.tsx`, which every genmath lesson renders through,
splits on `$$…$$`, `$…$` and `**…**` and nothing else. A single `*word*`
therefore reaches the student with its asterisks visible. Counting prose
strings only (skipping `check[]`, where `*` is multiplication):

| | |
|---|---|
| data files affected | **68** |
| strings affected | **3,024** |
| includes shipped Mongolian mirrors | yes — `6-mn`, `7-mn`, `8-mn` |
| worst single file | `ib-ai-sl/statistics-and-probability.json`, 306 |

**This is a ship-mode fix and I did not start it** — the mode rule in
`CLAUDE.md` says to write the other mode's work down rather than begin it. It
is one alternative in one regex plus an `<em>` branch, not 3,024 edits, and it
is worth doing before the Mongolian geometry strand lands, because those drafts
mirror the English's italics exactly.

The drafts are **not** stripped of italics in the meantime. `geometry/foundations`
carries 7 where its English carries 15; every one mirrors the English. Stripping
them would lose emphasis the English keeps, and would have to be undone when the
renderer is fixed. `mn_draft_check.py` now counts the English's italics and fails
only on italics a draft *introduces*, which is what the `mn-translation` skill
actually asks for.

### 6b. Terms the practice sets use that no lesson teaches

Not translation questions either — gaps in the English. In each case the
practice or test bank asks a student to use a named idea the lessons never
name, so the Mongolian has to coin a term for a word the course never
introduces.

| Term | Asked in | Taught in |
|---|---|---|
| Angle Addition Postulate | `geometry/foundations` `geo1-pr-4` | nowhere |
| contrapositive | `geometry/reasoning-and-proof` `geo2-ty-3` | nowhere |
| biconditional | `geometry/reasoning-and-proof` `geo2-ty-5` | nowhere |
| Law of Syllogism | `geometry/reasoning-and-proof` `geo2-pr-4` | lesson 3 teaches the move, never the name |
| same-side exterior angles | `geometry/parallel-and-perpendicular` `geo3-ty-2` | lesson 1 teaches four pair types, not this fifth one |
| "perpendicular to one of two parallels ⟹ perpendicular to the other" | `geometry/parallel-and-perpendicular` `geo3-ty-4` | nowhere — the only one of these that is a theorem rather than a term |
| Heron's formula, the law of sines, Thales' theorem | `geometry/relationships-in-triangles` lesson 7 | nowhere — the law of sines is unit 8 |

Three of the first four are in one topic. The Mongolian drafts coin all four and flag
them; whether the **English** should introduce them in a lesson, or the
practice items should stop asking for them by name, is your call.

### 6c. Two English content bugs

Not translation questions. Both are on live English pages.

1. **Fixed.** `algebra-1/quadratic-equations` lesson 3 was shipping an
   unfinished authoring note as a real answer option: «$\sqrt{49}$... with
   $b = 5$: also 1?». Now `$25$`, a distinct error model; the obvious repair to
   `$\sqrt{49}$` would have duplicated option B, which is `$7$`.
2. **Not fixed, needs your read.** `algebra-1/functions` lesson 4 opens
   «climbing means speeding up the hill... no — rising means the QUANTITY
   grows.» I read it as a deliberate device and wrote it that way in Mongolian.
   If it was a draft note that escaped, the English wants the same fix.

---

### 6d. Lesson objectives don't render maths. 190 of them contain it, and 20 are live in Mongolian.

**Found 18 Sep 2026 while grounding `geometry/right-triangles-and-trig`, and
it is the worst-looking of the three renderer bugs here** because it is above
the fold on every lesson page.

Every lesson route renders the objective as a bare string:

```tsx
<Section n="02" label={chrome("What you'll learn", lang)}>
  <p …>{lesson.objective}</p>      // app/math/<grade>/[topic]/[lesson]/page.tsx
</Section>
```

while `keyIdea`, seven lines below it in the same file, goes through
`<MathText text={lesson.keyIdea} />`. So an objective containing `$...$` ships
the delimiters and the raw LaTeX to the student. **190 objectives across 69
data files do.** All eleven grade routes and the ЭШ learn page share the bug.

**Twenty of them are already on production in Mongolian**, in the shipped
mirrors. A Grade 8 student opening `/math/8/roots/solving-root-equations`
reads, as the lesson's "What you'll learn":

> `$x^2=k$ хэлбэрийн тэгшитгэлийг (хоёр шийд, $x=\pm\sqrt{k}$) болон $x^3=k$-г…`

| | |
|---|---|
| data files affected | **69** |
| objectives affected | **190** |
| live in shipped MN mirrors | **20** across 9 files (`6-mn`, `7-mn`, `8-mn`, `algebra-1-mn`) |
| worst single file | `ib-sl/number-and-algebra.json`, 9 |

**The fix is one line per route** — wrap the objective in `<MathText>`, exactly
as `keyIdea` already is. **This is ship-mode work and I did not start it**, per
the mode rule in `CLAUDE.md`. It is the same shape as 6a and worth doing in the
same session.

**What I did fix, because it was mine:** seventeen drafted objectives across
eight drafts had `$...$` where the **English objective is plain text** — the
English writes `x² + bx + c` and `90°` and `f(x)` in Unicode precisely because
this field does not render maths, and my drafts had "improved" that into
`$x^2 + bx + c$`. That would have made the Mongolian strictly worse than the
English on those lines: the English renders correctly today, the mirror would
not have. All seventeen are reverted to the English's own plain-text
convention, and `mn_draft_check.py` now fails on an objective that introduces
`$` the English does not have. Same shape as the EMPHASIS check: mirroring the
English is fine, introducing is not.

**Note the division of labour, because it is the point.** The gate stops the
mirror getting worse than the English; it cannot make the English right. The
190 need the renderer.

---

### 6e. How much the green gate is worth — four checker bugs in four days

**Not a question for you; a caveat on the evidence the other items rest on.**
Every draft in this pile ends with `ALL DRAFT CHECKS PASS`, and that line is
worth less than it looks on a topic whose constructions the checker has not
met before. Four times now, a topic has been the first to exercise an edge and
the checker has been wrong at it:

| found | topic that surfaced it | the bug | symptom |
|---|---|---|---|
| 17 Sep | `geometry/right-triangles-and-trig` | grounding counter did not stem | «тойрогт багтсан өнцөг» scored 0 against «…өнцгийн» — a real word looked like a coinage |
| 19 Sep | `geometry/coordinate-geometry` | `$\$3$` prices mis-paired the span | Mongolian prose between two prices reported as Cyrillic-in-maths |
| 19 Sep | `geometry/area-and-perimeter` | id stem matched inside another id | 11 phantom UNKNOWN IDs on a clean draft |
| 19 Sep | `geometry/transformations` | `$$…$$` display maths split into two spans | 6 phantom Cyrillic-in-maths findings in lesson 7 |

Each was fixed in the commit that found it, and all twenty-six drafts re-run
clean after each fix — so the *current* green is real. The pattern is what
matters: **all four were false positives, none was a false negative**, which
is the safe direction to fail, but the fourth arrived on the last topic of the
strand, so there is no reason to think the checker has now seen everything.

**What this means for reading the pile.** The gate is evidence that a draft's
ids, step kinds, counts and notation match the English. It is not evidence
that the Mongolian is good — nothing checks that, which is the whole reason
this file exists — and on a topic with a construction no earlier draft used,
it is not yet evidence that the notation is right either. The three topics
above needed a human to notice the finding was nonsense before the tool could
be fixed.

---

### 6f. Grade 9 re-teaches grade 8, and both are already live in English

**Found 19 Sep 2026 drafting `9/equations-and-formulas`.** A curriculum
observation, not a translation question — same class as 6c.

Four of that topic's six lessons re-teach `8/linear-equations`:

| `9/equations-and-formulas` | `8/linear-equations` |
|---|---|
| Variables on Both Sides | `variables-on-both-sides` |
| No Solution & Infinitely Many | `one-none-or-infinite` |
| The Full Pipeline | `simplify-before-solving` + `equations-with-parentheses` |
| Modeling with Equations | `from-words-to-equations` |

Only *Literal Equations* and *Rate, Time & Mixture* are new at grade 9. The
same pattern is visible, more weakly, between `9/introduction-to-functions`
and `8/linear-functions`.

**This may be exactly what you want** — a deliberate spiral, with grade 9
revisiting grade 8 at higher difficulty, is standard curriculum design and the
grade 9 versions are meaningfully harder. I am flagging it only because a
student who does both hubs meets four lessons twice, and because nobody
sitting in a drafting session can tell an intended spiral from a copy-paste.
**Nothing changed; I did not touch the English.**

The translation consequence is real and is handled: grade 9 copies the shipped
grade 8 Mongolian for every overlapping term (item 2g).

---

### 6g. One ЭШ topic teaches logarithms three times

**Found 20 Sep 2026, drafting `algebra-2/exponentials-and-logarithms`.** Same
class as 6f — a curriculum observation, not a translation question — but
sharper, because here the repetition is *inside a single ЭШ topic* rather than
across two grades.

**Илтгэгч ба логарифм функц** has three units, and this is what they cover:

| ЭШ unit | source topic | logarithms? |
|---|---|---|
| 1 | `10/exponential-functions` | sets up the exponential |
| 2 | `11/logarithms` | six lessons: definition, evaluating, laws, two kinds of equation, log scales |
| 3 | `algebra-2/exponentials-and-logarithms` | four lessons: exponentials again, **definition again, laws again, equations again** |

A student working the topic in order meets the definition of a logarithm
twice, the three log laws twice, and log equations twice, in the same topic,
weeks apart.

**This may well be deliberate** — unit 3 is pitched harder (it adds change of
base and one-to-one reasoning) and spaced repetition is real. But unit 3 does
not *read* as a revisit; it reads as a first teaching, opening with "It's not a
new creature" as though the reader had never met one. **If the spiral is
intended, unit 3's framing should acknowledge unit 2**; if it is not intended,
one of the two is redundant. Either way it is an English-content call and I
changed nothing.

**What I did do** is make the Mongolian consistent across all three, which is
Notes 1 of that draft: the overlapping terms are copied, not re-decided, on
2g's logic one tier down. If you rule against any of them, three drafts change
together.

---

## 7. Style decisions I made without asking, listed so you can veto cheaply

- **«хамгийн их / хамгийн бага утга», not «максимум / минимум».** Corpus 92/87.
- **«олон гишүүнт» written apart**, against the book's solid «олонгишүүнт» —
  the ministry writes it apart 14 times and the book concedes the point at
  p. 222.
- **The freshman's-dream funFact describes the nickname** instead of saying
  «оюутан», which the voice reference's smell test §3 reserves for university
  students.
- **Mongolian-native images replace English ones** where they land better:
  таван хошуу мал for sorting like terms, цагаан сарын золголт for
  everyone-meets-everyone. This is the rewrite rule doing its job, but it is
  the most visible place a reader will feel my hand rather than yours.
