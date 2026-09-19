# The review pile — what is still uncertain after the glossary and the voice reference

**For Khas. Built 16 Sep 2026, after drafting all eight `algebra-1` topics.
Updated 19 Sep 2026, after the first twelve geometry topics.**

His instruction: *"let's push through most of the contents and then make it
ready for review. review as in the stuff that you're not sure even after using
the md's you sent."* This file is that list and nothing else. Anything the
dictionary, the voice reference or ministry order А/492 settled is **not** here
— it is settled, and recorded in the draft it belongs to.

**Voice reference §9 is fully applied and no longer a question.** All twenty-five
drafts carry zero em-dash parentheticals in shipping prose, and the check is
fatal rather than advisory, so the state cannot rot back.

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

### 2d. Math-mode decimals — **not applied. Surveyed: 267 of them.**

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
> rather than 178. **It is 267 as of 19 Sep** — see the note under the table;
> the figure grows with every draft that lands.

§7 says "every number a student reads", but the checks deliberately skip
`$...$` because the decimal point there is LaTeX, not Mongolian punctuation.
So `$x = 3.4$` in an answer option still renders a point.

Counted across the twenty-five drafts, 19 Sep 2026:

| Draft | Math-mode decimals |
|---|---|
| `10/exponential-functions` | 144 |
| `algebra-1/linear-equations` | 20 |
| `geometry/coordinate-geometry` | 14 |
| `geometry/relationships-in-triangles` | 14 |
| `geometry/circles` | 12 |
| `geometry/similarity` | 11 |
| `algebra-1/inequalities` | 10 |
| `algebra-1/systems-of-equations` | 8 |
| `10/quadratic-functions` | 7 |
| `algebra-1/linear-functions` | 7 |
| `geometry/foundations` | 5 |
| `geometry/right-triangles-and-trig` | 5 |
| `esh/number-sets-and-intervals` | 3 |
| `geometry/quadrilaterals-and-polygons` | 3 |
| `geometry/area-and-perimeter` | 2 |
| `algebra-1/functions` | 1 |
| `geometry/parallel-and-perpendicular` | 1 |
| **total** | **267** |

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

Exponential functions carries three fifths of them because growth factors
(`$b = 1.05$`, `$V = 800(0.75)^t$`) are decimals by nature.

**Why this is your call and not a mechanical follow-on from 2b.** In KaTeX the
change is `1.05` → `1{,}05`, which renders «1,05» correctly but makes every
formula noisier to read and to edit, and it diverges from the English mirror in
267 places rather than eight. It also touches `check[]` neighbourhoods, though
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
