# The review pile — what is still uncertain after the glossary and the voice reference

**For Khas. Built 16 Sep 2026, after drafting all eight `algebra-1` topics.
Updated 22 Sep 2026. The geometry strand is complete, and the queue has
switched to ЭШ-first: this file now covers **sixty-two drafts**, fifty-five
of which feed the ЭШ course** (re-measured 23 Sep against `lib/esh-course.ts`;
the figure carried until then, thirty-eight, was one low).

> **ЭШ progress, 23 Sep: 59 of 72 units covered · 12 of 14 topics** — counting
> shipped mirrors as well as drafts, which earlier figures in this file did not
> (review pile 6q). Both numbers are re-measured against `lib/esh-course.ts`
> each time, never incremented. Covered: Олонлог (3/3), Тэгшитгэл тэнцэтгэл
> биш (8/8), Илтгэгч ба логарифм функц (3/3), Дараалал цуваа (1/1), Геометр ба
> хэмжигдэхүүн (12/12), Комплекс тоо (2/2), **Комбинаторик (4/4, closed 22
> Sep)**, **Магадлал (4/4, closed 23 Sep)**, **Өгөгдлийн шинжилгээ (4/4, closed
> 23 Sep)**, **Функц ба график (7/7, closed 23 Sep)**, **Тригонометр (6/6,
> closed 23 Sep)**, and Тоо ба үсэгт илэрхийлэл (4/4,
> entirely from shipped mirrors — it never needed drafting).
>
> Remaining, by distance-to-complete: Анализын эхлэл (5 — unit 1 drafted
> 23 Sep), Вектор ба матриц (8).

His instruction: *"let's push through most of the contents and then make it
ready for review. review as in the stuff that you're not sure even after using
the md's you sent."* This file is that list and nothing else. Anything the
dictionary, the voice reference or ministry order А/492 settled is **not** here
— it is settled, and recorded in the draft it belongs to.

**Voice reference §9 is fully applied and no longer a question.** All
sixty-two drafts carry zero em-dash parentheticals in shipping prose, and
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

### 2d. Math-mode decimals — **not applied. Surveyed: 1,538 of them.**

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

Counted across the sixty-two drafts, 23 Sep 2026 — drafts 40–43 contributed none; **draft 44 (`prob-stats/probability-models`) contributes 52**, **draft 45 (`conditional-probability`) 144**, **draft 46 (`random-variables`) 83** **draft 47 (`binomial-distribution`) 190**, **draft 48 (`describing-data`) 100**, **draft 49 (`distributions-and-position`) 126**, **draft 50 (`two-variable-data`) 101**, **draft 51 (`inference-and-studies`) 99** **draft 52 (`9/piecewise-and-absolute-value-graphs`) 47** **draft 53 (`algebra-2/functions-and-transformations`) 11** **draft 54 (`algebra-2/polynomial-functions`) 0** **draft 55 (`algebra-2/rational-functions`) 3** **draft 56 (`trigonometry/right-triangle-trigonometry`) 20** **draft 57 (`special-triangles-and-exact-values`) 29** **draft 58 (`radians-and-the-unit-circle`) 9** **draft 59 (`graphs-of-trig-functions`) 5** **draft 60 (`identities-and-equations`) 12** **draft 61 (`laws-of-sines-and-cosines`) 35** and **draft 62 (`calculus/limits-and-continuity`) 32**, taking the total from 440 to 1,538. Probability is where the decimals live. Neither complex-numbers
draft adds any.

> **Second correction, 20 Sep: the number was 412 and it should have been 398.**
> The stored command counts a whole draft file, and six drafts *quote* decimal
> values inside their own **Notes for Khas** sections while documenting a
> finding. Those 22 quotations were never subtracted, so every figure this
> section has carried — 205, then 412 — was a file count wearing a shipping
> count's label.
>
> Splitting the file at the Notes heading gives **398 shipping · 22 notes ·
> 420 file**. The table below is shipping only, and the command underneath is
> the corrected one. Nothing about the decision changes; the number you would
> be ruling on is 398.
>
> The contaminated drafts are `algebra-2/exponentials-and-logarithms` (8),
> `11/sequences-and-series` (5), `solid-geometry/lines-and-planes-in-space`
> (3), `11/logarithms` (2), `9/introduction-to-functions` (2) and
> `algebra-2/systems-and-nonlinear-models` (2).

| Draft | Math-mode decimals |
|---|---|
| `10/exponential-functions` | 144 |
| `9/equations-and-formulas` | 44 |
| `solid-geometry/cylinders-and-cones` | 26 |
| `solid-geometry/spheres` | 16 |
| `algebra-2/exponentials-and-logarithms` | 38 |
| `algebra-1/linear-equations` | 20 |
| `11/sequences-and-series` | 18 |
| `geometry/coordinate-geometry` | 14 |
| `geometry/relationships-in-triangles` | 14 |
| `11/logarithms` | 13 |
| `geometry/circles` | 12 |
| `geometry/similarity` | 11 |
| `algebra-1/inequalities` | 10 |
| `9/introduction-to-functions` | 9 |
| `algebra-1/systems-of-equations` | 8 |
| `10/quadratic-functions` | 7 |
| `algebra-1/linear-functions` | 7 |
| `geometry/foundations` | 5 |
| `geometry/right-triangles-and-trig` | 5 |
| `geometry/transformations` | 5 |
| `esh/number-sets-and-intervals` | 3 |
| `geometry/quadrilaterals-and-polygons` | 3 |
| `solid-geometry/lines-and-planes-in-space` | 3 |
| `geometry/area-and-perimeter` | 2 |
| `10/rational-expressions` | 1 |
| `algebra-1/functions` | 1 |
| `geometry/parallel-and-perpendicular` | 1 |
| **total** | **440** |

> **This table is regenerated, not maintained.** It read 205 across nineteen
> drafts until 18 Sep, when re-running the count found three geometry drafts
> had been written after the survey and never added — the number drifts every
> time a draft lands. Regenerate before acting on it:
>
> ```
> python3 - <<'PY'
> import re, pathlib
> tot = 0
> for p in sorted(pathlib.Path('memory/mn-drafts').glob('*.md')):
>     if p.name in ('README.md', 'GEOMETRY-TERMS.md'): continue
>     # shipping prose only — everything before the Notes heading, which
>     # quotes decimal values while documenting findings (see the correction)
>     t = re.split(r'\n#+ *Notes for Khas',
>                  p.read_text(encoding='utf-8'), maxsplit=1)[0]
>     n = sum(len(re.findall(r'\d\.\d', m.group(1)))
>             for m in re.finditer(r'(?<!\\)\$([^$\n]+?)(?<!\\)\$', t))
>     if n: print(f'{p.name:55} {n}'); tot += n
> print(f'{"TOTAL":55} {tot}')
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

**Where the risk concentrates: approximations — now measured.**
`solid-geometry/cylinders-and-cones` contributes 26, the third-largest of any
draft, and **25 of the 26 are `\approx` values**; the single exception is an
exact quarter. The house style of every solid-geometry solution is π-exact
answer plus decimal gloss (`$= 48\pi \approx 150.8$`), so a ruling either way
lands hardest there. Separately, four times now a draft has
applied the decimal comma *inside* `$...$` by mistake, and every instance was a
`\approx` value inherited from the English ($27.5$, $22.31$, $6.9$, $7.07$,
$75.96$). The habit fires on the prose rule and the maths-mode context does not
register. `mn_draft_check.py`'s `MATH DECIMAL COMMA` check catches them, and
has now done so before a re-read twice running — but it is worth knowing that
in the geometry and trigonometry strands nearly every math-mode decimal is an
approximation, so that is where a ruling either way will bite.

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

#### It happened again the very next draft

`algebra-2/systems-and-nonlinear-models` needed a word for the **elimination
method**. `8-mn/systems-of-linear-equations` ships **«устгах арга»** (4 uses,
including the lesson body «Устгах аргаар бод»). My candidates would have been
«нэмэх арга» or «арилгах арга», **both zero in all three sources**.

А/492 names Gauss's method (11.2г) and Cramer's rule (11.2е) — the grade 11
matrix machinery — but never the plain elimination a grade 8 student does,
for the same structural reason as the roots vocabulary: **the standard starts
where the technique is already assumed.** Meanwhile the *substitution* method
in the same lesson is ministry-verbatim (10.5д, 11.2б) and agrees with the
mirror, so the two sit side by side in one lesson with completely different
provenance.

Two consecutive drafts, five terms, one cause. **The grade 6–9 shipped mirrors
are not a tie-breaker; for this material they are the only Mongolian that
exists.**

#### And once more, 22 Sep — across strands, and **half of it was my own error**

`prob-stats/counting-principles` (ЭШ Комбинаторик unit 1) takes **two** core
terms from `7-mn/probability`: «гүйцээлт» (*complement*, 15 uses) and
«боломжит үр дүнгийн орон» (*sample space*, 11). А/492 is genuinely silent on
both, checked under every phrasing I could construct.

> **I first wrote four, and two of those were not 2g cases at all.** I also
> claimed «тооллын зарчим» for *counting principle* and «мод диаграмм» for
> *tree diagram* under 2g. The ministry has a word for both — «үржвэрийн
> зарчим»/«нийлбэрийн зарчим» (10.6в, 10.6г) and «модны схем» (10.15б, 11.13д,
> 12.15а) — so the authority order never reached the mirror. The draft is
> corrected; the cause was a case-sensitive keyword sweep of А/492 that could
> not have matched «Факториалын» or «модны схем», whose negative result I then
> read as "the ministry is silent". Full account in that draft's Notes 8, and
> the method change is there too: **read the topic's ministry section in full
> rather than grepping it.**

What is new in the two that survive is the **direction**. The five earlier
cases were all vertical — a grade 9 or ЭШ unit borrowing from the grade 8
mirror of *the same subject*. These cross from **probability into
combinatorics**: a counting unit that teaches no probability at all inherits
vocabulary from the probability mirror, because counting is where probability's
own machinery was first named in Mongolian on this site.

That widens the rule rather than repeating it: **2g is not "look one grade
down", it is "look wherever this site first said it in Mongolian"** — and that
can be a different strand. I applied it on that reading. If you want 2g scoped
to same-subject borrowing only, these two need re-grounding and I have no other
source for them, since А/492's seven combinatorics lines (6s) cover neither
complement nor sample space.

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

#### Update, 20 Sep: «солбисон» was cashed in, and a fifth collision arrived

**`solid-geometry/lines-and-planes-in-space` is the topic «солбисон» was kept
free for**, and it uses the word exactly as the ministry does, in А/492's own
trichotomy:

> 12.5б: «Огторгуй дахь хоёр шулууны харилцан байршлыг тодорхойлох
> (параллель, **огтлолцох**, **солбисон**)»

One ministry line supplies all three of that topic's lesson-2 classifications
verbatim. **This is the first time a reservation made in this file has been
collected**, and it is worth recording because the cost was paid in one draft
(`parallel-and-perpendicular` gave up the obvious calque for *alternate*) and
the benefit landed in another two days later. That is exactly the kind of trade
that gets silently reversed when nobody writes it down.

**The fifth collision is «налуу», and it is the first that comes from the exam
rather than the ministry.** *Oblique* (Russian наклонная) wants «налуу». But:

| source | uses | sense |
|---|---|---|
| ЭШ papers | **19** | **slope**, every one — «$A$, $B$ цэгүүдийн налуу $\frac{4}{5}$» |
| А/492 | 6 («налалт») | **slope** — 10.8в «шулууны налалтыг олох» |
| shipped mirrors | 20 | slope |

Zero uses anywhere for an oblique segment. And this is an **in-strand**
collision by 4e's own test: ЭШ Geometry unit 8 is `coordinate-geometry`, which
teaches slope, and unit 10 is this topic. Two units apart in one block.

The exam even produces «**Налуу** перпендикуляр $-1/3$» meaning *the slope of
the perpendicular*, which in unit 10's vocabulary would read as *the oblique
perpendicular* — a contradiction in terms.

4e's rule says in-strand ⟹ the word is unavailable. I could not make it
unavailable: there is no other candidate («ташуу» 1, «хазгай» 4, «хэвгий» 0,
none in any authority). **So the draft manages it instead, as «налуу хэрчим»
(*oblique segment*), never bare** — the «гурвалжны медиан» pattern, which 4e
reserves for cross-strand cases. That is a deliberate departure from the rule,
and I would rather you saw it than found it.

**With five instances, 4e has outgrown being a list.** Four kinds now appear:
ministry-vs-ministry (солбисон, огтлогч), cross-strand (медиан),
ours-and-fixable (эсрэг өнцөг), and now exam-vs-topic with no alternative
available (налуу). A standing rule would be cheaper than a sixth entry.

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

### 4j. The ministry and the ЭШ papers name the same object differently — **three times, and the third points the other way**

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

#### Third instance, 22 Sep — and the first that points the OTHER way

**`11/complex-numbers`.** *Conjugate*:

| source | wording | count |
|---|---|---|
| А/492 | «**хосмог**» | **3** — 12.4г twice, 12.4з once |
| ЭШ papers | «**нөхөр тоо**» | **2** — both in solution prose |

Both exam uses are squarely in this topic — «Хуваагчийн **нөхөр тоогоор**
үржүүлбэл» (division) and «комплекс шийдүүд **нөхөр тоонууд**» (the
conjugate-root theorem) — so it is a real conflict, not a near-miss.

**The draft uses «хосмог», which is the first time I have recommended the
ministry over the exam in this item.** The reason is that 4j's real argument
has never been *the exam is the authority*; it has been *the exam's word is
commoner by an order of magnitude and is what the student reads on the paper*.
Here:

- the gap is **3 against 2**, not 78:3 (volume) or 31:2 (range);
- the ministry's three sit in **objectives** — what a student must learn —
  while the exam's two are one author's phrasing in two solutions;
- «хосмог» appears in a *defining* line («хосмог тоонууд байна гэсэн үр дүнг
  гаргах»), which is where a term is coined rather than used.

**This sharpens what 4j is asking, and I think it settles the wording.** If the
rule is "the exam wins for ЭШ topics", this case hands the decision to two
lines of solution prose over three ministry objectives, which I doubt anyone
intends. If the rule is **"the commoner, more student-facing word wins"**, this
case goes to the ministry and *all four earlier instances still go to the
exam*. **That second reading is the only one that survives all five**, and it
is what I would suggest you adopt if you rule on 4j.

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

> **Update 20 Sep: see 6h.** Six more of these turned up, in three topics, and
> the sweep that found them also vindicates the reading above — the
> flounder-as-device genre is real and used on purpose elsewhere in the corpus,
> which is why item 2 here should stay a judgement call and not be "fixed" by a
> blanket rule.

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

### 6h. Leaked authoring notes are a pattern, not accidents — six of them, in three topics, two of which I have never drafted

**Found 20 Sep 2026, drafting `algebra-2/systems-and-nonlinear-models`.** Four
English strings in one topic contain the author's own visible floundering,
shipped as finished prose:

| id | the English says |
|---|---|
| `a232-t1` | «(1)+(2): **wait —** kill $z$… **cleaner:** … **Let's verify integer path instead: actually** …» |
| `a23-pr-4` | «$x = \frac{13}{7}$**... cleaner:** $-7x = -13$» |
| `a23-ty-3` | «$y = \frac{5}{3}$**... check:** $-3y = -5$» |
| `a234-we1` | «under the line $x + y = 6$, and **under... above?** $y \le 2x$ keeps…» |

**The mathematics is correct in all four.** I re-solved the three systems with
sympy and they match the stored answers exactly (`a232-t1` → $(11/7, 8/7,
-5/7)$; `a23-pr-4` → $(13/7, 17/7, -2/7)$; `a23-ty-3` → $(11/3, 5/3, 14/3)$),
and `a234-we1`'s corners $(0,0), (6,0), (2,4)$ are right. **This is a prose
leak, not a wrong answer** — the author found the right result by a route they
narrated while walking it, and never cleaned the narration up.

**So I went looking for the rest of them, and there are two more topics.**

My first instinct was that this is trivially greppable. It is not: `...`,
«wait», «cleaner» and «actually» across all English genmath fields return
**202 hits in 42,819 strings**, and a large share are legitimate — including a
whole deliberate genre where a *fictional* student flounders and the reader
must audit them («A classmate claims … 'because $c^2 = 9 - 16$… wait, $16 - 9
= 7$'. Audit the reasoning.»). That device is exactly what 6c's second item
turned out to be, and a naive check would condemn it.

**What separates the bugs is whose voice it is in, not the words.** Restricting
to `solution` and `correction` fields — where the text speaks as the course,
not as a character — and dropping strings that quote a third party gives
**6 hits in 11,188 strings**:

| topic | id | the English says |
|---|---|---|
| `algebra-2/systems-and-nonlinear-models` | `a232-t1` | «(1)+(2): **wait —** kill $z$… **cleaner:** (2)+2×(… **Let's verify integer path instead: actually** …» |
| ″ | `a234-we1` | «and **under... above?** $y \le 2x$ keeps…» |
| ″ | `a23-pr-4` | «$x = \frac{13}{7}$**... cleaner:** $-7x = -13$» |
| ″ | `a23-ty-3` | «$y = \frac{5}{3}$**... check:** $-3y = -5$» |
| **`prob-stats/binomial-theorem`** | `bt-l4-t1` | «**$10 - $ wait —** $n = 4$: want $4 - k = 2$…» |
| **`trigonometry/laws-of-sines-and-cosines`** | `trig6-pr-8` | «$= 10\sqrt2 + \frac{10\sqrt6}{3}$**... cleaner:** …» |

**The last two are in topics I have not drafted and would not have seen.**
`bt-l4-t1` is the worst of the six: it opens mid-error, with a discarded «$10
-$» still on the page before the correct work starts.

**All six are mathematically correct**, verified with sympy — the three
systems, the trig value ($10\sqrt2 + \frac{10\sqrt6}{3} \approx 22.31$, which
equals the printed $\frac{10(\sqrt6+\sqrt2)}{\sqrt3}$), and the binomial
coefficient (coefficient of $x^2$ in $(x+5)^4$ is $\binom{4}{2}\cdot 5^2 =
150$). Every one is a prose leak, not a wrong answer.

**The viable check**, then, is narrower than I first thought and correspondingly
worth having: *self-correction markers in `solution`/`correction` fields, minus
quoted speech*. Precision on today's corpus is 6 in 11,188 with no false
positives I can see. I have not written it — it is a gate change and this is a
content session — but it is the one concrete follow-on I would suggest, and it
is the difference between six known bugs and the seventh nobody finds.

**Three of the four are solutions to three-variable systems**, which is where
the arithmetic is heaviest and a student is most likely reading closely for a
method to copy. «wait —» in a worked solution teaches that the method is
guesswork.

**What the Mongolian does.** I wrote all four clean, reconstructing the path
the author actually took as a finished derivation. **So the MN and EN read
differently for these four items — deliberately, and for the first time.** If
you would rather the mirror preserve the English's shape, the English needs
fixing first; I would rather repair the source than reproduce the floundering,
but that is your call and it is four strings either way.

#### Correction, 22 Sep: the scan was not complete — there are at least twelve

Drafting `prob-stats/combinations` turned up a leak in a **`correction`**
field — «…$3·11·5·9$/... **wait, cancel systematically**…» — which is inside
the scope above and which the scan did not report. So I rescanned: course-voice
fields (`solution`, `correction`, `explanation`, `body`, `teach`, `text`,
`concept`, `concreteComparison`, `keyIdea`), markers widened to include
«hmm», and every hit read in context rather than counted.

**Six more**, for twelve in all:

| topic | id / field | the English says | status in Mongolian |
|---|---|---|---|
| `prob-stats/combinations` | l2 commonMistake, `correction` | «leaving 3·11·5·9/... **wait, cancel systematically**» | draft 42, written clean |
| ″ | l2 tip, `body` | «the $6$ eats $10 \cdot 9$'s $\dots$" **wait**, $6$ divides $9 \times 10 = 90$? Check:» | draft 42, written clean |
| `8/the-real-number-system` | `rns6-we3`, `solution` | «$2^2=4<8<9=3^2$**? No,** $9>8$ so…» | **already clean in the shipped mirror** — its translator fixed it silently |
| `algebra-2/radicals-and-rational-exponents` | commonMistake, `text` | «$8^{2/3}$ as the square root of $8^3$**... wait,** as $(\sqrt{8})^3$» | **already clean in my draft 33** — I fixed it silently and did not record it |
| `11/statistics-and-data` | quick-check `explanation` | «$50 − 34 = 16\%$ below**... wait:** BELOW $-1σ$ is 16%» | not mirrored |
| `integrated-1/systems-of-equations-and-inequalities` | `im1-u5-l3-t3`, `solution` | «$19x = 137$**... let us instead** eliminate $x$ … **Hmm — check against the other route**» | not mirrored |

All six are mathematically correct; I re-solved the two systems-shaped ones.

**Two of the six are in `solution`/`correction` fields**, which is exactly the
scope I called complete with "no false positives I can see". Precision was
fine; **recall was not**, and I reported it as if it were. I cannot reconstruct
from the record why the first scan dropped `rns6-we3` («actually» was on its
list). The honest statement is: twelve known, found by two scans that
disagree, so assume more.

**And two had already been fixed silently in Mongolian** — once by the grade 8
translator, once by me. Silent fixes are the right output and the wrong
record: the English stays broken, and the next person to read the EN/MN
difference sees drift where there is a repair. From here I note every such
repair in the draft's Notes.

#### And a third scan, 23 Sep: leaks in *question statements*

Neither scan above looked at `statement` fields — the text a student reads
**before** answering. Draft 45 found one there, and a scan of every English
`statement` finds:

| topic | id | the English says |
|---|---|---|
| `prob-stats/conditional-probability` | `cd-l4-t1` | «…$90\%$ of dry days**... wait —** find $P(\ldots)$» |
| `algebra-2/rational-functions` | `a274-t1` | «$= \frac{4x+2}{x(x+1)}$**... wait — simplify smartly:** solve…» |
| `vectors-matrices/vector-arithmetic` | `vm24-we3` | «$B(6, 7)$**... wait — check it,** then find $AP : PB$» — *borderline*: it may be deliberate |

Plus one in draft 44's source, an explanation that trails off mid-thought:
«3, 5, 7... — 3 and 5 are odd primes» on a six-sided die.

**So the honest count is 14 or 15, in three field classes, found by three scans
that each missed something the next one caught.** Statement leaks are the
worst class: a student meets «wait —» in the question itself. `cd-l4-t1` is
written clean in draft 45; the other two are in topics not yet drafted.

#### And a fourth, 23 Sep: read every statement with an ellipsis, not the markers

Draft 47 found `prob-stats/binomial-distribution` `bd-p-6`, a **statement**:

> «A $10$-question multiple-choice quiz has $5$ options each. **A guesser needs
> at most...** find $P(\text{exactly } 2 \text{ correct})$ with $p = 0.2$.»

A sentence abandoned mid-thought, carrying none of the marker words. So instead
of widening the marker list again I read **every English `statement` that
contains an ellipsis: 27 of 8,702.** Sixteen are legitimate (fill-in stems
ending «is…», a truncated decimal, two deliberate student-voice audits, one
stylistic pause). The
rest:

| topic | id | the English says | |
|---|---|---|---|
| `prob-stats/binomial-distribution` | `bd-p-6` | «A guesser needs at most**...** find…» | new · draft 47, written clean |
| `prob-stats/inference-and-studies` | `in-p-7` | «A city poll ($n = 1111$**... use** $1100$) **— actually:** compute…» | new · not drafted |
| `solid-geometry/lines-and-planes-in-space` | `sg1-pr-3` | «(b) $AB'$ and $DC'$**... just (a), plus:** how many edges…» | new · **my draft 35 had silently asked a different question** and dropped the half `check[]` tests; corrected 23 Sep, its Notes 8 |
| `trigonometry/laws-of-sines-and-cosines` | `trig62-t2` | «$b = 8\sqrt{2} \cdot \frac{\sqrt3}{2}$**... simpler:** $b = 4\sqrt{6}$» | new · not drafted |
| ″ | `trig64-we2` | «sighted with $\angle QPR = 30°$**... simpler classic:** from two points…» | new · not drafted |
| `8/linear-functions` | `lf5-we2` | «double the cost of $3.5$**…** of $14$ pounds vs $7$?» | new · **already clean in the shipped grade 8 mirror** — another silent fix |
| `prob-stats/distributions-and-position` | `dp-l2-t1` | «$6$th from the top, $3$rd from the bottom**...** compute her percentile…» | borderline in the statement — **but its solution is also wrong** («faster than $62.5\%$»; she beats $25\%$). Draft 49, written clean, its Notes 1 |
| `trigonometry/identities-and-equations` | `trig5-ty-4` | «on $[0, 2\pi)$**...** then give the GENERAL solution» | borderline |
| plus the three already listed above | `cd-l4-t1`, `a274-t1`, `vm24-we3` | | |

**Six new clear leaks and two borderline**, all in the class that matters most:
the question itself. `in-p-7` contains «actually», which was on the marker
list, and the third scan still did not report it. **The count of 14 or 15
becomes 20 or 21, plus two more borderline, found by four passes** — and this one is the first I would call
complete for its class, because it reads every candidate rather than searching
for words. Leaks without an ellipsis or a marker remain unbounded.

---

### 6i. One ЭШ lesson teaches material the exam does not test — the only one in eight units

**Found 20 Sep 2026, drafting `algebra-2/systems-and-nonlinear-models`**, the
last unit of ЭШ Algebra. Its lesson 4 is *Systems of Inequalities & the Corner
Principle*, and the two halves have completely different standing:

| half | ministry | exam bank |
|---|---|---|
| graphing a system of inequalities | **10.5г, verbatim**: «Хоёр хувьсагчтай шугаман тэнцэтгэл биш зохиох, тэнцэтгэл бишийн системийг бодох, шийдийг координатын хавтгайд дүрслэх» | present |
| the corner principle, optimization, linear programming | **absent** | **absent** |

The standard covers the drawing and stops before the optimizing. The exam bank
agrees: «шугаман програмчлал», «боломжит муж» and «зорилгын функц» score
**zero occurrences each**, in 54 past papers.

**So this is the only lesson in eight ЭШ Algebra units teaching content the
exam will not ask about** — and, not coincidentally, the only lesson in the
block whose terminology is entirely ungrounded (three coinages, all in this
half; details in that draft's Notes 3).

The three options, none of which I have built:

- **keep it** — what the draft does. Good mathematics, strong English, and
  rule 7's legacy tier does not forbid extra content;
- **mark it** beyond-syllabus in the Mongolian, for which the ЭШ course has no
  mechanism today;
- **cut it** from the ЭШ unit while keeping it in the `algebra-2` course.

The second and third are edits to `lib/esh-course.ts` — ship-mode work, not
this session's. **The reason to decide is that the three coinages are only
worth your review time if the lesson stays**, and they are the only ungrounded
terms in an otherwise fully-grounded eight-unit block.

---

### 6j. Three CORE ministry objectives are claimed by a unit that teaches none of them

**Found 20 Sep 2026, drafting `solid-geometry/lines-and-planes-in-space`.**
This is a ship-mode finding about `lib/esh-course.ts`, and I think it is the
most consequential one in section 6.

That file maps ЭШ Geometry unit 10 as:

```
"lines-and-planes-in-space": ["10.12в", "11.5в", "11.5г"],
```

All three are **non-elective (core)**. The topic teaches none of them:

| code | asks for | this topic has |
|---|---|---|
| 10.12в | «Биетүүдийн хавтгай огтлол байгуулах, огтлолын талбайг тооцоолох (диагональ, огтлол, тэнхлэг огтлол, суурьтай параллел огтлол)» | **0** mentions of a cross-section |
| 11.5в | «Огторгуйн координатын систем, цэгийн координатыг ойлгох…» | **0** mentions of a coordinate |
| 11.5г | «…хоёр цэгийн хоорондох зай, хэрчмийн дундаж цэг» (in space) | **0** |

The topic is purely synthetic: axioms of a plane, skew lines, ⊥ to a plane,
angles in space.

**Two of the three are merely mis-attributed.** `vectors-matrices/vectors-in-
space` opens with `coordinates-in-3d` and includes `the-box-diagonal`, which
between them cover 11.5в and 11.5г — but that unit claims 11.8а–е instead. So
those two codes are attached to the wrong unit rather than uncovered.
Bookkeeping, and cheap to fix.

**10.12в is the real one.** Nothing in the 72-topic course teaches constructing
plane cross-sections of solids and computing their areas. The topic that does —
`solid-geometry/cross-sections-and-similar-solids`, whose first lesson is
literally `cross-sections-of-solids` — **is not in the ЭШ course at all**.
Partial coverage exists only in `spheres` (sections of a sphere, 4 mentions)
and one mention in `cylinders-and-cones`.

**Why this is worse than an ordinary gap.** `MOE_NOT_YET_COVERED`'s own
docstring is emphatic:

> «The core list is empty, and lib/esh-course.test.ts asserts that… A core
> objective may not silently reappear here. Silence about a gap is the thing
> the list exists to prevent.»

That list is rigorous and test-asserted — but the test can only check that a
code is not *both* mapped and listed as missing. **It cannot check whether a
mapping is truthful.** So a core objective can go uncovered by being falsely
claimed, which is precisely the failure the list was built to prevent, reached
by the one route the test does not watch. The gap list says the core list is
empty; on this evidence it is not.

**Two things would close it**, neither of which I have done:

- a check that validates mappings against topic *content*, not just against the
  gap list — even a keyword sanity check would have caught all three; and
- a decision on 10.12в itself: either add
  `solid-geometry/cross-sections-and-similar-solids` to the Geometry block, or
  move 10.12в into `MOE_NOT_YET_COVERED` and accept a non-empty core list.

Adding a unit to the course is a curriculum call and rule 4's route budget does
not cover it, so it is yours. I changed nothing.

---

### 6k. Production ships *volume* spelled two ways — and my drafts picked the minority form 126 times

**Found 20 Sep 2026, drafting `solid-geometry/cylinders-and-cones`.** Part live
content bug, part drafting error, and the two have to be untangled before
either can be fixed.

| source | «эзлэхүүн» | «эзэлхүүн» |
|---|---|---|
| **ЭШ papers** | **78** | 3 |
| А/492 | 1 — **10.12б**, the solid-geometry line | 1 — 11.10к, the calculus volume-of-revolution line |
| **shipped mirrors** | **40** | **10** |
| my drafts | 12 | **126** |

**The live bug.** Three shipped mirrors, two spellings:
`6-mn/geometry-area-volume`'s **topic title** is «Геометр: Талбай ба
**эзлэхүүн**»; `8-mn/roots` writes «эзлэхүүн» eleven times;
`7-mn/geometry-scale-and-circles` writes «эзэлхүүн» ten times. A student moving
from grade 6 to grade 7 meets the word respelled, and one of the two is a page
title. **No gate catches it** — `scripts/i18n/mn_terms.py` contains neither
form.

**The drafting error.** `geometry/surface-area-and-volume` (ЭШ Geometry unit 9,
the topic whose whole subject is volume) uses «эзэлхүүн» 110 times and
«эзлэхүүн» 7 — internally inconsistent, and on the minority side of the exam by
78 to 3.

**Why I cannot just decide it.** This is a *spelling* split, and
`docs/MONGOLIAN.md` explicitly carves spelling out of the ministry's authority
(the recurring orthography carve-out). The ministry uses both forms in
different sections, so it does not break the tie either. The exam does, 78:3,
and А/492's own solid-geometry line — 10.12б, the objective ЭШ Geometry units 9
and 11 are both mapped to — writes «эзлэхүүн».

**`solid-geometry/cylinders-and-cones` uses «эзлэхүүн»** on that basis, which
means it currently disagrees with unit 9.

**The cost of each ruling:**

- **«эзлэхүүн»** (my recommendation): 126 replacements across drafts, 110 of
  them in one file, plus a production fix to `7-mn/geometry-scale-and-circles`.
- **«эзэлхүүн»**: 12 replacements in drafts, plus production fixes to
  **two** mirrors including a page title, and divergence from the exam by 78:3.

Either way **the production inconsistency needs fixing and a term-gate entry**,
and that half is Build ship-mode work rather than a translation decision.

---

### 6l. Four terms where an earlier draft coined a word an authority already had

**Same draft, same cause as 6k, but these are unambiguous — the exam has the
word and unit 9 invented a different one.** Unlike 6k there is no spelling
carve-out in play, so these need a yes rather than a ruling.

| concept | unit 9 (`geometry/surface-area-and-volume`) | ЭШ bank | uses |
|---|---|---|---|
| lateral surface area | «хажуугийн талбай» — *compositional*, **0 everywhere** | **«хажуу гадаргуугийн талбай»** | **9** |
| total surface area | *(not named)* | **«бүтэн гадаргуугийн талбай»** | **4** |
| slant height of a cone | «налуу өндөр» — *compositional*, **0 everywhere** | **«байгуулагч»** | **8** |

The exam's sentences are essentially unit 11's worked examples: «Конусын
суурийн радиус 6 бол **хажуу гадаргуун талбайг** ол», «Конусын **байгуулагч**
нь 12 нэгж, суурийн радиус нь 8 нэгж урттай байв».

**Adopting «байгуулагч» also dissolves a collision.** «налуу өндөр» carried
4e's fifth instance — «налуу» means *slope* in all 19 exam uses — so the
exam's word removes a coinage and a collision together.

This does **not** disturb «гадаргуугийн талбай» for surface area in general,
which the shipped mirrors use 22 times and 2g protects.

#### Fourth instance, 22 Sep — two senses, not one wrong word

**`algebra-2/quadratics-and-complex-numbers`.** *Completing the square*.

**I first wrote this entry as "ministry and mirrors say «ялгах», only my draft
says «болгох», seven instances". That was wrong, and the real picture is more
useful.** Reading the shipped mirror's contexts instead of counting them shows
it uses **both, for different jobs**:

| use | shipped `algebra-1-mn/quadratic-equations` |
|---|---|
| **the method's name** | «бүтэн квадрат **ялгах**» — «$x^2 + 6x - 7 = 0$-ийг бүтэн квадрат ялгаж бод», «(бүтэн квадрат ялгах эсвэл томьёогоор)» |
| **turning an expression into a square** | «бүтэн квадрат **болгох**» — «$x^2 - 10x$-г бүтэн квадрат болгохын тулд нэмэх нь» |

That distinction is real and worth keeping: «ялгах» *separates out* a complete
square (the technique), «болгох» *makes something into* one (what you do to an
expression). The ministry's 10.5б names the technique and uses «ялгах»:

> «Квадрат тэгшитгэлийг **бүтэн квадрат ялгах** аргаар бодох»

**So the defect in `algebra-1/quadratic-equations` is narrower than I said.**
Of its seven «болгох», most are the legitimate "turn into" sense — including
one that matches the shipped mirror's sentence almost verbatim. What is wrong
is that it names **the method** «болгох»: its terminology table row, its
method list, and its test-yourself item `al8-ty-3`, whose shipped counterpart
says «ялгах» in the same sentence.

**Roughly three uses to change, not seven, and a terminology-table row** — and
the row is the one that matters, since it is what the next draft would copy.

The new draft uses «бүтэн квадрат ялгах» for the method throughout and does not
need the other sense.

> **The common cause of 6k and 6l is worth more than the three terms.**
> `geometry/surface-area-and-volume` was drafted **before the ЭШ-first
> redirect**, when the exam bank was not consulted first. It is the only
> geometry topic in the ЭШ course whose subject the exam covers densely, and it
> was drafted as though the exam were silent. **The other twelve geometry
> drafts share that provenance** — they are simply luckier, because the exam
> says little about plane-geometry proof. Worth knowing before the pre-redirect
> geometry drafts are reviewed: the question to ask each one is not "is this
> well-formed Mongolian" but "did the exam already have a word".

---

### 6m. The exam's subtopic labels are a term source I had not been using — and missing it cost a term the same day

**Found 20 Sep 2026, drafting `solid-geometry/spheres`.** A method finding
rather than a content one, but it corrected a draft committed an hour earlier
and it will keep paying.

`solid-geometry/cylinders-and-cones` recorded **«таслагдсан конус»** for
*truncated cone* as its one ungrounded term, noting I had searched
«таслагдсан», «таславсан» and «тайрсан» and found nothing. All three searches
were real; all three came back empty. **I did not search «огтлогдсон».**

The ЭШ bank carries it as a subtopic label:

> `"subtopic": "Огтлогдсон конус"` — **12 questions**, all from the **2025A/B/C
> papers**, all Section 2 fill-ins, all tier **hard**.

That makes truncated cones one of the three most-tested solids in the bank. The
term was not ungrounded; I had looked for it with the wrong three words.

**What actually fixes this is not "search harder".** The bank's `subtopic`
field is a **small controlled vocabulary naming exactly what the exam thinks
its own topics are** — for `solid_geometry` the whole list is:

| subtopic | count |
|---|---|
| Гурвалжин пирамид | 16 |
| Тэгш өнцөгт параллелепипед | 12 |
| Огтлогдсон конус | 12 |
| Параллелепипед, пирамидын эзлэхүүн | 12 |
| Конус | 6 |
| the rest | 16 |

Reading that list takes one command and would have supplied the term without
guessing a synonym. **I had never used it as a term source in thirty-seven
drafts**, and it is strictly better than free-text search for exactly the terms
an ЭШ draft most needs: the names of the things the exam tests.

**Added to the drafting loop** in `memory/mn-drafts/README.md`: dump the
bank's subtopic labels for the topic's `skill_tag` before the grounding pass.

> Note this is the **third** distinct search-method failure recorded in two
> days: substring false positives («их тойрог» inside «орших тойрог», «ул»
> inside «улам»), the decimal-survey over-count (2d), and now the wrong-synonym
> miss. All three produced confident wrong statements that a second check
> caught. The common lesson is that a bare count is not evidence — the contexts
> or the controlled vocabulary have to be read.

#### One caveat on the subtopic field, found the first time I leaned on it

Dumping the four combinatorics `skill_tag`s on 22 Sep returned **18 distinct
labels for 52 questions**, and the vocabulary is much noisier than
`solid_geometry`'s was:

- **Case-only duplicates**: «тоолол»/«Тоолол», «тоолох»/«Тоолох» — four labels,
  two concepts.
- **Two labels are English**: `stars_and_bars` (3 questions) and
  `Permutations with restrictions` (3). Whoever tagged these had no Mongolian
  for them, which is itself a finding — they are the two subtopics my draft had
  to coin around.
- **«сэлгэл» once against «сэлгэмэл» five times** — and «сэлгэмэл» is the
  ministry's word (10.14б), so the singleton is a typo, not a variant.

So the field is still the best term source for ЭШ drafts and I am keeping it in
the loop, but **it is a tagger's free text with a small vocabulary, not a
controlled one**. Read it case-folded, treat singletons as suspect, and do not
take a label's *spelling* as authority the way 6m's «Огтлогдсон конус» invited
— that one happened to agree with the ministry. Cleaning the labels is Build
ship-mode work on the bank, not a translation decision; noting it here only.

---

### 6n. The exam does not test spheres at all, while the ministry requires them

**Found 20 Sep 2026, drafting `solid-geometry/spheres`** — ЭШ Geometry unit 12,
the last unit of the block.

А/492's **10.12б is core (non-elective)** and names the sphere explicitly:

> «Пирамид, цилиндр, призм, **бөмбөрцөг**, конусын гадаргуун талбай,
> эзлэхүүнийг олох томьёог мэдэх, хэрэглэх»

The exam bank contains **zero** occurrences of «бөмбөрцөг», «бөмбөрцг…»,
«сфер» or «бөөрөнхий», and no sphere surface-area or volume question anywhere.
(The 98 hits for «бөмбөг» are all probability urns and basketballs.) Of 74
`solid_geometry` questions, the sphere's share is **0**, while truncated cones
get 12 — see 6m's table.

**This is the inverse of every 4j instance so far.** Those were all *the exam
has a better word than the ministry*. This is *the ministry requires content
the exam does not test*, which does not have the same answer, and it sits
opposite 6i, where an ЭШ Algebra lesson taught content the exam does not test
and the **ministry** was silent too.

**I am not proposing to cut unit 12.** 10.12б is core; 54 papers is a sample,
not the whole history; and a student who cannot do a sphere has a gap the
syllabus says is real. But it is worth your eye, because:

- it makes **«бөмбөрцөг» the only term in that draft with a single authority**
  — the ministry line above — with no exam register to check it against, where
  every other term in the topic had two or three sources; and
- the pair {6i, 6n} is the shape of a question you may eventually want to
  answer once: **when the exam and the syllabus disagree about what matters,
  which one does the ЭШ course follow?** Today the course follows the syllabus
  for coverage and the exam for wording, which is defensible but has never been
  stated.

---

### 6o. A second false mapping — and the exam tests this one 33 times

**Found 22 Sep 2026, drafting `algebra-2/quadratics-and-complex-numbers`.**
Same class as 6j, worse consequences.

Ministry **11.1б** and **11.1в** are both **core** and both about quadratic
inequalities:

> 11.1б «Квадрат тэнцэтгэл биш бодох (шийдийг тоон шулуун дээр дүрслэх)»
> 11.1в «Квадрат тэнцэтгэл бишийг графикийн аргаар бодох, квадрат гурван
> гишүүнт үргэлж эерэг (сөрөг) утгатай байх нөхцөлийг мэдэх»

`lib/esh-course.ts` assigns both to **`algebra-1/inequalities`**, ЭШ Algebra
unit 2:

```
"inequalities": ["10.5а", "10.5г", "11.1б", "11.1в", "12.1а"],
```

**That topic has no quadratic content.** Its lessons are
`solving-and-graphing-inequalities`, `multi-step-inequalities`,
`compound-inequalities`, `absolute-value-equations-and-inequalities`, and the
file contains **zero** occurrences of "quadratic", "parabola" or "$x^2$".

**The exam tests this 33 times** — `skill_tag: quadratic_inequality`, plus 3
more under `quadratic_inequality_parameter`. It is one of the most-tested tags
in the bank.

**Why this is worse than 6j's case.** There, 10.12в was genuinely uncovered but
rarely tested. Here:

- the content **does** exist — in `algebra-2/quadratics-and-complex-numbers`
  lesson 4, which claims only `12.4г` and so never shows up against these
  codes;
- so a student working the **Algebra** block to learn inequalities reaches unit
  2, which promises 11.1б/в and does not deliver, while the real teaching sits
  in **Комплекс тоо** — a topic they may never open;
- and it is heavily examined.

**Two fixes, neither of which I have made.** Moving 11.1б/11.1в onto
`quadratics-and-complex-numbers` is honest bookkeeping and cheap. Moving the
*lesson* into the Algebra block is a curriculum call and yours.

> **Both 6j and 6o were found the same way**: reading a unit's actual content
> against its claimed objectives, while drafting it. Neither is visible to
> `lib/esh-course.test.ts`, which can only check that a code is not both mapped
> and listed as missing. **Two instances in three days is enough to say the
> check I suggested under 6j — validate mappings against topic content — would
> pay for itself.** A keyword sanity check would have caught both.

---

### 6p. Комплекс тоо teaches complex numbers twice — in a two-unit topic

**Found 22 Sep 2026.** Same family as 6g (one ЭШ topic teaching logarithms
three times), but sharper in one respect: **this topic has exactly two units
and both introduce $i$ from scratch.**

| ЭШ unit | source topic | complex numbers? |
|---|---|---|
| 1 | `11/complex-numbers` | **six lessons** — i, a+bi, multiplying, conjugates & division, complex roots, the complex plane |
| 2 | `algebra-2/quadratics-and-complex-numbers` | **one 13-step lesson** covering powers of i, arithmetic, conjugates and division — plus a third lesson on complex roots |

Unit 2's lesson 2 opens «$x^2 = -1$ бодит шийдгүй» as though the reader had
never met $i$ — after unit 1 has already done powers of $i$, the complex plane
and the conjugate-root theorem. Its lesson 3 then re-teaches unit 1's lesson 5.

**Three of unit 2's four lessons are revision**, in fact: lesson 1 re-teaches
`10/quadratic-functions` and `algebra-1/quadratic-equations`. **Only lesson 4
(quadratic inequalities) teaches something no other drafted topic does** — and
that is the lesson whose objectives are mis-filed, per 6o.

**What I did:** made the Mongolian consistent across both units, copying every
overlapping term from `11/complex-numbers` rather than re-deciding it — the 6g
remedy. **What I did not do:** touch the repetition, which is an English-content
call. If the spiral is deliberate, unit 2's lesson 2 should acknowledge unit 1
instead of re-introducing $i$; if it is not, the cheaper cut is obvious at 13
steps against 54.

---

### 6q. The ЭШ queue has been counting my drafts, not Mongolian coverage — one topic needed no work, and one topic was drafted twice

**Found 22 Sep 2026, choosing the next target.** Not a translation question; a
correction to how I have been reporting progress, and it changes what happens
next.

Every progress figure I have given — "30 of 72 units", "six of fourteen
topics" — counted **drafts in `memory/mn-drafts/`**. It ignored the twenty-five
`data/genmath/*-mn/` mirrors that have been **live in Mongolian for months**.
Some ЭШ units draw on grade 6–8 topics that are already mirrored, so they were
never work to begin with.

Counting *coverage* instead — a unit is covered if its source topic has a
shipped mirror **or** a draft:

| | units |
|---|---|
| already shipped in MN | **5** |
| drafted | 31 |
| neither | 36 |
| **total** | 72 |

**So the course is 36 of 72 covered, and 7 of 14 topics — not 6.**

**Тоо ба үсэгт илэрхийлэл needs no drafts at all.** All four of its units —
`8/the-real-number-system`, `8/exponents-and-scientific-notation`, `8/roots`,
`7/percent-applications` — already ship in Mongolian. It has been sitting in my
queue at "4 units left" for days and the correct number is zero.

**And one topic was drafted that was already live.** ЭШ Algebra unit 5 is
`algebra-1/quadratic-equations`, which has shipped as
`algebra-1-mn/quadratic-equations.json`. I drafted it on **18 September** — the
day *before* the shipped-mirror check was added to the drafting loop (19 Sep,
per `README.md`). Its header makes no mention of a mirror, because the check
did not exist yet.

**That draft is therefore a retranslation of live Mongolian**, which is exactly
what 2g exists to prevent, and the 6l entry above is the first divergence found
between them. There may be more; nobody has diffed them.

**Two things worth your call:**

- **Should `algebra-1/quadratic-equations`'s draft be reconciled against the
  shipped mirror, or discarded in favour of it?** 2g's logic says the shipped
  wording wins wherever they differ, which would make the draft a list of
  corrections rather than a translation. That is a smaller job than it sounds
  and I would rather do it than leave two Mongolian versions of one topic.
- **The remaining queue is five topics, not six**, and the four-unit tier is
  now Комбинаторик, Функц ба график, Магадлал and Өгөгдлийн шинжилгээ.

> **The general lesson is about the check, not the count.** The shipped-mirror
> step added on 19 Sep asks *does a mirror teach this material?* — a question
> about terminology. It does not ask *is this unit already mirrored?* — a
> question about whether to draft at all. The first question saved four terms
> in `solid-geometry/cylinders-and-cones`; the second would have saved a whole
> draft. I have added it to the loop.

---

### 6r. A held-back file keeps an *already-ruled* term wrong in production — and the gate prints "clean"

**Found 22 Sep 2026, drafting `prob-stats/counting-principles`**, while
checking whether *tree diagram* is spelled «мод диаграмм» or «мод диаграм».

The spelling split is real and live:

| source | «диаграмм» | «диаграм» |
|---|---|---|
| А/492 | **4** | 0 |
| ЭШ papers | **13** | 0 |
| shipped mirrors | **35** | **25** |

All 25 minority-form uses sit in **one file**,
`data/genmath/8-mn/scatter-plots-and-bivariate-data.json` — the topic whose
entire subject is scatter plots. `8-mn/systems-of-linear-equations`, one grade
and one shelf away, writes «диаграмм».

**Unlike 6k, this is not an open ruling.** `scripts/i18n/mn_terms.py` already
carries the correction, grounded on the ministry's four uses:

```
(r"диаграм(?!м)", "диаграмм", "10.13в, 11.11а", ...)
```

**So why is it still wrong in production?** Because that file is held back
*whole*. It contains three inflected forms of «хэв маяг» — the word you ruled
against on 13 Sep (*"pattern is зүй тогтол period. never хэв маяг."*) — whose
declensions have no ruling yet, so they sit in `PENDING_FORMS` and the file is
skipped entirely rather than half-converted. The skip is the right call on its
own terms; the side effect is that **an unrelated, fully-decided term stays
wrong in 25 places, and `npm run verify:mn-terms` still ends with "clean"**.
The hold-back is reported one line above that word, which is how I found it,
but nothing marks it as a *regression* rather than a deferral.

**Unblocking it is eight words.** Five forms, across two files:

| pending form | uses | my proposal |
|---|---|---|
| `хэв маягаас` | 3 (scatter-plots) | зүй тогтлоос |
| `хэв маягт` | 1 (scatter-plots) | зүй тогтолд |
| `хэв маяггүй` | 1 + 1 (both files) | зүй тогтолгүй |
| `хэв маягаар` | 1 (real-number-system) | зүй тогтлоор |
| `хэв маяггүйгээр` | 1 (real-number-system) | зүй тогтолгүйгээр |

The pattern behind the proposal — and the thing I actually need you to check —
is that the stem's final о **drops before vowel-initial suffixes and stays
before consonant-initial ones**, which is what your own accusative ruling
(«хэв маягийг» → **«зүй тогтлыг»**, already in the file) does. I have applied
nothing; this is a language call, not a lookup.

**The same ruling was being broken in the drafts, and nothing was watching.**
Checking the drafts for it on 22 Sep found **«хэв маяг» eleven times across
seven drafts**, all in shipping prose, months after you ruled it out. One of
them sits in `geometry-reasoning-and-proof`, whose own terminology table
records the correct answer («pattern | **зүй тогтол** | corpus 6 · «хэв маяг»
corpus 24»). The draft knew and used the banned word anyway.

The cause is structural: `mn_terms.py` enforces `OWNER_CORRECTIONS` against
`data/genmath/*-mn/` only, and `mn_draft_check.py` does not know the owner
corrections exist. **So a ruling binds the shipped mirror but not the draft
that is going to become one** — the drafts are where the wording is actually
being decided, and they are the unguarded half.

I have applied the ruling to all eleven (nominative and genitive from your own
accusative «зүй тогтлыг»; the dative is the `хэв маягт` form pending below).
All affected drafts still pass their gate. One instance was not a mathematical
*pattern* at all — `geometry-quadrilaterals-and-polygons` used it for "these
marked configurations", where «зүй тогтол» reads wrong in either direction, so
that sentence is rephrased to drop the noun rather than substitute it.

**Third ask, cheapest of the three: teach `mn_draft_check.py` the owner
corrections** so a ruling cannot be re-broken in a draft. That is ship-mode
work and I have not done it.

Two separable asks, and the second does not depend on the first:

1. **Rule the five declensions** (or correct them) — unblocks both files.
2. **Independently: should a hold-back that strands a ruled term report as
   clean?** This is Build ship-mode work, so I am only writing it down: the
   check could list "held back, N ruled corrections not applied" and exit
   non-zero, or apply the ruled terms and hold back only the pending ones.
   Today a second such collision would be equally invisible.

---

### 6s. Every combinatorics objective in А/492 is **elective** — and the exam asks 52 questions on it

**Found 22 Sep 2026, grounding ЭШ Комбинаторик.** The exact mirror image of
6n (the exam does not test spheres at all, while the ministry requires them),
and it lands on the same seam from the other side.

The standard has **seven** combinatorics lines, and all seven are elective:

| code | elective | text |
|---|---|---|
| 10.6в | **yes** | Комбинаторикийн үржвэрийн зарчмыг мэдэх, хэрэглэх |
| 10.6г | **yes** | Комбинаторикийн нийлбэрийн зарчмыг мэдэх, хэрэглэх |
| 10.14а | **yes** | Факториалын томьёог мэдэх, хэрэглэх |
| 10.14б | **yes** | Сэлгэмэл, хэсэглэлийн томьёог мэдэх, хэрэглэх |
| 11.13а | **yes** | Сэлгэмэл, хэсэглэлийн томьёо хэрэглэн үзэгдлийн магадлалыг тооцоолох |
| 12.14а | **yes** | Тодорхой зааглал өгсөн үед боломж тоолох |
| 12.14б | **yes** | Давталттай хэсэглэлийг тооцоолох |

> **Corrected within the hour of first writing this.** I published it as three
> lines. The other four were missed by a case-sensitive keyword sweep — the
> same error that put two wrong terms into the draft (2g above, and that
> draft's Notes 8). The headline conclusion is unchanged: all of them, however
> many, are elective.

The ЭШ bank, meanwhile, carries **52 questions** across the topic's four
units — `counting_principle` 20, `permutation_arrangement` 16,
`binomial_theorem` 10, `combination_selection` 6.

**Why this matters for drafting, not just for planning.** The seven lines
supply seven words — факториал, сэлгэмэл, хэсэглэл, үржвэрийн зарчим,
нийлбэрийн зарчим, давталттай хэсэглэл, зааглал — and then stop. There is no
*sample space*, no *complement*, no *overcounting*, no *inclusion–exclusion*:
an elective line gets one sentence, not a vocabulary. So for a topic the exam
tests 52 times, the authority order runs dry after seven terms, which is what
forces the surviving cross-strand 2g cases above and the two coinages in the
draft («давхар тоолол», «оруулах-хасах зарчим»).

Note what that means for the next three units, and it is the useful part: the
ministry's seven words are **front-loaded onto units 1 and 3** (factorial,
permutation, combination, the two principles). Units 2 and 4 — arrangements and
the binomial theorem — will be thinner still, and I expect to be asking you
about coinages there rather than reporting groundings.

**Unit 4 shows the topic spans two sections of А/492, not one.** The binomial
theorem is not in the combinatorics block at all: it sits in **11.4**, the
sequences block — **11.4г** «(a+b)ⁿ бином задаргааны томьёо ашиглах» and
**11.4е** «Биномын задаргааны гишүүний $C_n^k a^{n-k} b^k$, $0 \le k \le n$
томьёог хэрэглэх» — with the rational-exponent extension at **12.9ж**. All
three are elective too, so the conclusion stands with ten lines instead of
seven. A keyword sweep of the combinatorics section would never have found
them; reading the drafts' topic against the whole standard did.

**No action needed on the curriculum mapping** — unlike 6j and 6o this is not a
false claim, it is an honest gap, and `MOE_NOT_YET_COVERED` is not implicated.
I am flagging it because it predicts where the next four drafts will be
thinnest on grounding, and because **"the ministry calls it elective" is not a
reason to thin the content** when the exam asks 52 questions. I drafted it at
full weight.

---

### 6t. The real exam and our own authored tests write binomial coefficients differently — 83 uses, three notations

**Found 22 Sep 2026, grounding ЭШ Комбинаторик units 2–4.** This is the
biggest open decision in the strand, and it has to be settled before
`prob-stats/combinations` and `prob-stats/binomial-theorem` are drafted,
because it changes every formula on the page.

| notation | real past papers (2021–2025) | our authored `test*` papers |
|---|---|---|
| $C_n^k$ — the Russian/Mongolian school form | **26** | 8 |
| $C(n,r)$ | **15** | 3 |
| `\binom{n}{k}` — the international form | 5 | **23** (26 before three misrendered vectors were excluded — 6z) |

For permutations the same split exists with almost no data: the real papers
write $A_n^k$ (2023a, 2023c — «$A_3^2 = 6$»), and `\binom`-style $P(n,r)$
appears once, in an authored test. А/492 uses **no notation at all** for these
— it names the formulas in words and never prints a symbol, so the standard
cannot settle it.

Three things follow, and they are separable:

1. **The real papers and our authored papers disagree, and ours drifted.** The
   exam a Mongolian student actually sits leads with $C_n^k$; our own generated
   tests lead with `\binom`, 23 to 8. Whatever you rule for the lessons, the
   authored tests should match the real papers — that is a `practice-test-authoring`
   fidelity bug, not a translation question, and it is Build ship-mode work.
   I am recording it, not fixing it.
2. **The English source teaches the international form**, `P(n,r)` and
   `\binom{n}{k}`, throughout `prob-stats`. A Mongolian rewrite that keeps it
   teaches a notation the ЭШ paper mostly does not print.
3. **The argument order is a genuine trap.** $C_5^2 = 10$ puts the *pool* in
   the subscript and the *chosen* in the superscript — the reverse of what a
   student who has seen $\binom{n}{k}$ vertically might assume, and the reverse
   of the order in `\binom`'s own rendering. Teaching both without saying this
   explicitly would be worse than teaching either alone.

**What I would do, if you want a recommendation:** lead with $C_n^k$ and
$A_n^k$ in the Mongolian ЭШ units, introduce `\binom{n}{k}` and $P(n,r)$ once
per topic as «олон улсын бичлэг» with the argument-order warning, and leave the
English `prob-stats` source untouched. That is the 5d move — rebuild for the
audience rather than transliterate — and it is reversible, since notation is
mechanical to swap.

**Unit 2 (`permutations`) is drafted and did exactly that** — $P(n,r)$
throughout, with every switch location listed in that draft's Notes 3 (about
thirty, all mechanical). One sentence of lesson 2's tip names $A_n^k$, states
that $A_8^3 = P(8,3) = 336$, and warns which index is which. I think that
sentence survives either ruling.

**Unit 3 (`combinations`) is drafted the same way**, and the stakes are now
concrete: **237** $C(n,r)$ occurrences would move, counted. Two strings name
$C_n^k$ with the index warning (lesson 1's notation beat, lesson 2's formula
fact). **Lesson 7 keeps `\binom` on the exam's own evidence** — the real 2021
papers' stars-and-bars solutions are the five `\binom` uses in the real
papers, so that lesson already matches. The trap if you switch: $C(n,r) \to
C_n^r$ moves the arguments into index positions, so it has to be done by
pattern, not by eye.

---

### 6u. The rewrite cannot add anything — only replace, string for string

**Found 22 Sep 2026 in the same draft**, when the gate rejected a lesson I had
given an extra teach step.

`mn_walk.py` walks the English source and the Mongolian mirror in the same
order and `mn_apply.py` hard-fails on a count mismatch, so the mirror must
carry **the same number of lessons, step kinds, beats, options, concepts, facts
and recap points** — in the same order. A rewrite may change what any string
says, which is the whole point, but never how many strings there are.

This has not bitten in forty drafts because until now every draft only ever
*replaced*. It bit here because the Mongolian version had something to say that
the English has no reason to say — that the ЭШ paper prints $A_n^k$. English
readers do not sit ЭШ, so no English step exists to carry it.

**I fitted it into the tip's body**, which is one free-prose string with no
length contract, and recorded the constraint in `memory/mn-drafts/README.md`.

Worth your eye because it will recur, and because the workaround has a ceiling:
the next time a Mongolian rewrite needs a genuinely new *step* rather than a
sentence, the honest answer is that the English source is missing one, and
adding it to both sides is a content change to the English course. That is
ship-mode work and a different decision from any in this file. I would rather
raise it than keep hiding additions inside tips.

---

### 6v. A live English funFact states the arithmetic backwards

**Found 22 Sep 2026, drafting `prob-stats/combinations`.** Every earlier
source bug in this file was messy prose around correct maths (6h). This one is
a wrong fact, live in English now.

Lesson 1's funFact, on a 6-of-45 lottery with $C(45,6) = 8{,}145{,}060$
tickets: *«The division by 6! is not your friend here; without it you'd
"only" wait 30 years.»*

Dividing by $6!$ makes the ticket count **smaller**, so it is exactly your
friend. Without it the count is $P(45,6) = 5{,}864{,}443{,}200$ — about
**16 million years** at one ticket a day. «30 years» is what you get by
dividing by $6!$ a *second* time ($8{,}145{,}060 / 720 / 365 \approx 31$).
Verified by computation. A student who follows the sentence learns the
reverse of the lesson it closes.

The Mongolian (draft 42) says the true thing. **The English needs the same
fix** — ship-mode, one string.

Same topic, smaller, all recorded in draft 42's Notes 1:

- **lesson 6 funFact title contradicts its body**: «The \$1.5 million comma»
  over a body that says \$5 million (the real settlement);
- **lesson 5's lock-in question has two distractors worth the same**:
  $C(14,6) = C(15,5) = 3003$, so a student can eliminate both without doing
  the problem;
- **`cb-l4-w3`** calls a thirteen-question bank «a 5-question quiz bank».

A second live English error of the same kind, found in draft 46
(`prob-stats/random-variables`, lesson 3 funFact): **"European roulette pays
36-to-1 odds on a wheel with 37 pockets … expected net = −1/37"**. At 36-to-1
the expected net is exactly $0$ — the game would be fair, contradicting the
sentence's own conclusion. The real single-number payout is **35-to-1**, which
gives $-\frac{1}{37}$. Verified by computation; the Mongolian says 35.

And one in **our own exam solution text**, not the English course:
`data/questions/2021a.json` calls the zero-allowed solutions of
$x+y+z=7$ «тогтворгүй шийд» — *unstable* solutions. It reads as a slip for
«сөрөг биш бүхэл шийд», which is what draft 42 uses.

---

### 6w. Our own ЭШ solution text spells «томьёо» with a hard sign, 41 times

**Found 22 Sep 2026, reading the ten binomial questions for draft 43.** A third
live spelling split, after 6k (эзлэхүүн) and 6r (диаграм) — and unlike both,
this one is entirely in text **we** wrote.

| source | «томьёо» (ь) | «томъёо» (ъ) |
|---|---|---|
| А/492 | **33** | 0 |
| shipped mirrors | **89** | 0 |
| drafts | **377** | 0 in shipping prose |
| app code | 5 | 0 |
| **`data/questions/`** | 11 | **41**, in 19 files |

Every «томъёо» is in a field we authored: **37 in `solution`**, 4 in our own
`test*` question bodies, **none in a transcribed exam question**. So this is
not the exam's spelling; it is ours, and it disagrees with the ministry, the
mirrors and the app.

The same four 2025 solutions also contain an **untranslated English word**:
«**multinomial** томъёогоор олно» (2025a–d).

Both are fixes to `data/questions/` — ship-mode, under `esh-practice-test`, and
not mine to make in a content session. `mn_terms.py` would catch the first if
it scanned `data/questions/` as well as `data/genmath/*-mn/`; it currently does
not, which is the same blind spot 6r found for the drafts.

---

### 6x. One notation change is not cosmetic, and I made it: $T_{k+1}$, not $T_k$

**Draft 43, `prob-stats/binomial-theorem`.** 6t is about two spellings of one
number ($C(n,r)$ against $C_n^k$) and I have left it to you. This one I
changed, because the symbol means a *different term* under each convention.

The English writes the general term $T_k = \binom{n}{k}a^{n-k}b^k$ with $k$
from $0$, so the fifth term is $T_4$. Our own ЭШ solutions (test6a, test6b)
write **$T_{k+1}$** and call the fifth term $T_5$, which is the Mongolian
school convention. A student taught the English's form who reads «$T_5$-ыг ол»
computes the sixth term. The English's own `bt-l4-w3` already strains against
it: «the middle is the fifth, $k = 4$».

The draft writes $T_{k+1}$ and names the ordinal wherever a term is found.
**No number changes**; every $k$ and coefficient is the English's. Reversing
it is five strings. I am flagging it because it is the first place I departed
from the English's mathematical notation rather than its wording.

---

### 6y. *Independent*: the ministry says «үл хамаарах», the shipped grade 7 mirror says «хараат бус»

**Found 23 Sep 2026, grounding `prob-stats/probability-models`** (Магадлал
unit 1).

| source | «үл хамаарах» | «хараат бус» |
|---|---|---|
| А/492 | **3** — 10.15б (core), 11.13б, 11.13г | 0 |
| `scripts/i18n/mn_terms.py` GLOSSARY | **1** | 0 |
| `.claude/skills/mn-translation` glossary | 0 | **1** |
| `7-mn/probability` (shipped) | 0 | **13** |

The ministry outranks the shipped corpus and 2g only fills silence, so ЭШ
drafts use **«үл хамаарах»** — named once in draft 44, used throughout the next
unit. **Two things follow, and only one is a question for you:**

1. **Grade 7 and ЭШ will name independence differently.** I am not proposing
   to change the grade 7 mirror: А/492 is the grades 10–12 standard and does
   not rule on grade 7, and a student meets the two words years apart. But it
   is a vocabulary step the course takes without saying so; if you want it
   said, one sentence in the ЭШ lesson would do it.
2. **The two glossaries in the repo contradict each other** — the skill file
   every session reads says «хараат бус» with no caveat, `mn_terms.py` beside
   it says «үл хамаарах». The skill file is the one a future session will
   trust. That is a one-line fix to a skill, which a content session should not
   make unasked; I am flagging it.

The same unit shows the order working without conflict for *mutually
exclusive*: the ministry's «**нийцгүй**» (10.15а, core) over the other
mirrors' descriptive «давхцахгүй үзэгдэл» (6 uses).

---

### 6z. **Live in production:** six ЭШ practice solutions defer to "the corpus" instead of solving — and three are mathematically wrong

**Found 23 Sep 2026, grounding `prob-stats/random-variables`. This is the most
serious item in this file**: it is not a draft, not English source, and not a
wording question. It is student-facing Mongolian text on the live ЭШ practice
hub, and in three places it contradicts the answer key printed beneath it.

Every one of these is a site-authored `**Бодолт.**` solution in
`data/questions/`. **All six answer keys are correct** — I re-derived each by
computation — so a student who checks their answer is marked right. The
problem is what they read when they open the solution:

| file · Q | what the solution does | the truth |
|---|---|---|
| **2022b Q10** | misreads its own denominator as $a+2b$, gets $\frac{8}{11}$, writes «**Хм**, … хариу D-тэй (=8/15) **тохирохгүй**», speculates the *question* must be different, tries two more denominators, then «Хариу: **D**» | the question as printed gives $\frac{12t-4t}{3t+12t} = \frac{8}{15}$ in one line. **The solution tells a student the answer key is suspect when it is right.** |
| **test1a Q35** | solves the *equation* $x^2 - 3x - 4 = 0$ instead of the inequality, gets sum $3$, then «**харин корпусаас 6**» | $(x-4)(x+1) < 0$ gives $x \in \{0,1,2,3\}$, sum $6$. **Wrong method, then an appeal to authority.** |
| **2022b Q30** | computes with $\sum y = 23$ and $\sum y^2 = 110$ — **numbers that are not in its question** ($25$ and $171$) — gets $0.75$, then «**корпусын хариу** $\sqrt{5.01}$ тул $\sigma^2 \approx 5.01$» | with the printed data: $\frac{271}{10} - 4.7^2 = 5.01$, $\sigma = \sqrt{5.01}$. **Arithmetic on a different problem.** |
| **2022b Q18** | «Тархалтын магадлалуудыг ашиглавал $E(X)$-ийг тооцоолно. (**Корпусаас** $E = \frac{5}{2}$ хариу гарна.)» — no solution at all | $a = \frac{1}{6}$, $E = \frac{1}{6} + \frac{2}{6} + 2 = \frac{5}{2}$ |
| **test3a Q15** | correct, but hedges the obvious: «III хувилбар нь **корпусаар** тэнцүү байх боломжтой» | $k(x) = 2^{2x} = 4^x$ exactly |
| **test3a Q32** | «**Корпусын** асуултын тэгшитгэлийг хангах хос $(r, s) = (6, 2)$» — and **the question itself is broken**: a vector equation typeset as binomial coefficients, $\binom{8}{46} = r \binom{1}{9} + s \binom{1}{-4}$ | $r(1,9) + s(1,-4) = (8, 46)$ at $(6,2)$ — but a student sees $\binom{8}{46}$, which as printed is $0$ |

**How this happened is visible in the text:** the solutions were written
*towards* a known key ("the corpus") by an author who sometimes could not
derive it, and the working — including the doubt — was shipped. It is the 6h
pattern (leaked authoring notes) in its most harmful form: in Mongolian, in the
live ЭШ bank, and in three cases teaching a wrong method.

**Scope of what I checked:** the word «корпус»/«corpus» in every `solution` in
`data/questions/` — six hits, all listed. Solutions that went wrong *without*
naming the corpus would not show up in this search, so treat six as a floor.

**What it needs, none of which is mine to do in a content session:** rewrite
the six solutions and fix test3a Q32's typesetting (`pmatrix`, not `\binom`),
under `esh-practice-test` — ship-mode, and each is short. Then a gate:
`scripts/verify-practice-test.py` checks answer keys by sympy but not whether
the prose solution reaches them; a check for «корпус», «Хм», «тохирохгүй» and
the other self-doubt markers in `solution` fields would have caught all six.

(6t's count moves slightly: three of the authored papers' `\binom` uses are
these misrendered vectors, so authored `\binom` is 23, not 26. The conclusion
— real papers prefer $C_n^k$, our authored tests prefer `\binom` — is
unchanged.)


### 6aa. Coins and dice: the exam says «орхих» and «тоотой тал» — the whole probability strand says «шидэх» and «зураас»

**Found 23 Sep 2026, drafting `prob-stats/binomial-distribution` (draft 47).
One ruling for the whole strand, wanted before any of drafts 40–47 ships.**

Measured across `data/questions/`:

| | the exam | shipped `7-mn/probability` | drafts 40–47 |
|---|---|---|---|
| heads | «сүлдтэй тал» (2025b, 2025d) | «сүлд» | «сүлд» |
| tails | **«тоотой тал»** (2025a, 2025c) · «зураас» **0** | «зураас» 5 | coin-sense «зураас» **22** |
| toss / roll | **«орхих»** in **18** papers — coin (2025a–d), die (2022a–d §2, 2023a–d, 2024a–d, test5a–b), knucklebone (2024a–d) · «шид-» for a coin or die **0** | «шид-» 45 | «шид-» **150** |

A Mongolian coin has the Soyombo on one face and the **number** on the other;
the exam names the faces for what is on them. «зураас» (a stripe, a dash) names
nothing on the coin, and draft 42 also uses it **39 times** for the *bars* of
stars and bars, so one word carries two meanings two units apart. «тоотой тал»
removes that collision for free.

**Why this is not a search and replace.** The 150 «шид-» forms mix coin and die
tosses with basketball free throws, and free throws keep «шидэлт» under any
ruling — the exam itself writes «3 онооны шидэлт» (test2a–b). The conversion
is item-by-item reading. I have not given a coin/ball split, because I have not
made one.

**Why nothing is converted yet.** 6r: half a conversion is worse than none.
Drafts 40–47 are mutually consistent today. The `mn-translation` skill's
«H = сүлд, T = зураас» gloss and the grade 7 mirror are separate decisions
(А/492 does not rule on grade 7), and the skill is ship-mode.

**The ruling wanted:** (a) the exam's «орхих» and «сүлдтэй / тоотой тал»
across drafts 40–47, in one pass; (b) keep «шидэх» and «сүлд / зураас»; or
(c) the faces from the exam, the verb unchanged. I lean (a): it is what the
student will read on the day, and 6m already made the exam's own labels a
term source.

### 6ab. The ЭШ divides by $n$; our standard-deviation lesson teaches $n - 1$

**Found 23 Sep 2026, drafting `prob-stats/describing-data` (draft 48).** Lesson
4 (`standard-deviation`) defines $s = \sqrt{\sum (x_i - \bar{x})^2 / (n - 1)}$,
the sample convention, and all its worked answers use it. **Every variance
and standard-deviation question in the ЭШ bank divides by $n$**, ten of them:

| papers | question | by $n$ (keyed) | by $n - 1$ |
|---|---|---|---|
| 2023a, 2023d | Q26, variance of $4, 6, 15, 11, 24$ | $50.8$ | $63.5$ — **not an option** |
| 2023b, 2023c | Q26, variance of $3, 7, 12, 13, 20$ | $33.2$ | $41.5$ — **not an option** |
| 2022a–d | Q30, pooled $\sum x$, $\sum x^2$ | $\sigma^2 = \frac{\sum x^2}{n} - \bar{x}^2$ | — |
| 2024a, 2024c | §2.3.3, grouped data | $\sigma^2 = \sum p_i (m_i - \bar{x})^2$ | — |

A student who learned lesson 4 and meets 2023a finds no option that matches.
Lesson 7 of the same unit teaches the $n$ version without saying it differs.

**In draft 48**, inside 6u, I added one sentence to each lesson: lesson 4
now says the ЭШ divides by $n$ and points at lesson 7, and lesson 7 says its
formula is the one the ЭШ uses. Nothing numerical changed.

**The question that is yours:** whether the ЭШ course should teach $n$ in
lesson 4 at all. That is an English-source change (answers and `check[]`
move: $\sqrt{2/3} \to \sqrt{1/2}$ and so on), ship-mode, and it would make the
ЭШ unit disagree with the `prob-stats` course it borrows from. The two
sentences are the cheap alternative; they do not remove the trap, they name
it.

### 6ac. «цэгэн диаграмм» is a dot plot in grade 6 and a scatter plot in А/492

**Found 23 Sep 2026, grounding draft 48.** Three sources, two meanings:

| source | «цэгэн диаграмм» / «цэгэн график» means |
|---|---|
| shipped `6-mn/data-and-statistics` | **dot plot** — lesson «Цэгэн диаграмм ба давтамжийн хүснэгт», 15 uses |
| shipped `7-mn/sampling-and-statistics`, `mn-translation` glossary | dot plot, as «цэгэн график» |
| **А/492 10.13в** | **scatter plot** — «Цэгэн диаграмм, түүний хандлагын шулууныг баримжаалан зурах, корреляцыг таних» |
| `mn-translation` glossary, grade 8 | scatter plot as «хамаарлын график» |

The ministry outranks the rest, so in upper-secondary ЭШ material «цэгэн
диаграмм» should mean the scatter plot. Draft 48 needs *dot plot* once and
writes «цэгэн график», which keeps the two apart. **`two-variable-data`, the
next-but-one ЭШ unit, is where it has to be decided**, because that unit is
about scatter plots and 10.13в is its only ministry code. Grade 6 is shipped
and is not this rewrite's to change.

**Update, same day, drafting `two-variable-data` (draft 50):** grade 8 adds a
third name. `8-mn/scatter-plots-and-bivariate-data` calls the scatter plot
**«тархалтын диаграм»**, 15 times including its title, where «тархалт» is also
this topic's word for *distribution*. Draft 50 follows А/492 with «цэгэн
диаграмм» (12 uses) and draft 49's closing tip does the same. So the state is:

| phrase | grade 6 | grade 7 / glossary | grade 8 | А/492 | drafts 48–50 |
|---|---|---|---|---|---|
| dot plot | «цэгэн диаграмм» | «цэгэн график» | — | — | «цэгэн график» |
| scatter plot | — | «хамаарлын график» (glossary) | «тархалтын диаграм» | **«цэгэн диаграмм»** | «цэгэн диаграмм» |

The same unit found the outlier's third shipped name: grade 6 «онцгой утга»,
grade 7 «хэт утга», grade 8 «гаж цэг». The drafts use «хэт утга» throughout.
Neither is this rewrite's to change in shipped mirrors; both want one line
from you so the next grade-level pass knows which way to go.

### 6ad. A live English concept contains a Cyrillic-corrupted word — the only one in 212 files

**Found 23 Sep 2026, drafting `prob-stats/distributions-and-position`.**
Lesson 6 (`position-capstone`), concept 3, student-visible in English now:

> «Technical audiences take z; parents, patients, and **памятlets** take
> percentiles.»

*Pamphlets*, with its first half replaced by Cyrillic. I scanned every string
in the 212 English `data/genmath/` files for Cyrillic: 27 hits, and **26 are
deliberate** (ЭШ, «БАЯРЛАЛАА» as a letter-drawing example, «самбар тоолуур»,
the Mongolian number names in grade 4). **This is the only word that mixes
scripts.** One string, one word, ship-mode: `data/genmath/prob-stats/
distributions-and-position.json`, `lessons[5].concept[2]`. Draft 49 writes
«ухуулах хуудас».

A mixed-script check (any word containing both Latin and Cyrillic letters) on
the English corpus would have caught it and has, today, zero false positives.

### 6ae. *Bias* is «хазайлт» by the glossary — and «стандарт хазайлт» shares the page

**Found 23 Sep 2026, drafting `prob-stats/inference-and-studies` (draft 51).**
The `mn-translation` glossary and the shipped grade 7 mirror (14 uses) give
*bias* as «хазайлт». In this unit lesson 2 is *about* bias and lessons 4–6 are
about the *standard deviation* of $\hat{p}$, so sentences need both. With
А/492's «хазайлтууд» (spread measures, 11.11в) and *deviation* $x - \bar{x}$,
the word now carries four meanings in one ЭШ topic; *skew* would have been a
fifth, which draft 48 avoided with the participle «хазайсан».

**Draft 51 follows the glossary** (34 bias-sense uses) and never lets
*standard deviation* appear as a bare «хазайлт». The option, if you want it:
**«өрөөсгөл»** (*one-sided*), the everyday word for a biased judgement,
ungrounded in our sources, which would free «хазайлт» for deviation. It would
reach the shipped grade 7 mirror. One ruling; nothing converted.

### 6af. A second claimed-but-untaught code (12.3е), and two drafts disagreeing on open/closed dots

**Found 23 Sep 2026, drafting `9/piecewise-and-absolute-value-graphs`
(draft 52).**

**12.3е.** `lib/esh-course.ts` maps ЭШ Функц ба график unit 4 to 12.3е
(elective): «Функцийн модул, $y = f(x)$ функцийн (тэгшитгэлийн) график өгсөн
үед $y = |f(x)|$, $y = f(|x|)$ функцийн графикийг байгуулах». The topic
teaches $|x|$, $a|x - h| + k$, piecewise and step functions, and **neither
$|f(x)|$ nor $f(|x|)$**. 6j's pattern on an elective code, so no test notices.
Ship-mode: a lesson (the two constructions are one lesson's worth) or a
mapping change.

**Open and closed dots.** Draft 52 writes **«битүү / задгай цэг»**, grounded
twice: the dictionary's «битүү / задгай завсар» and the shipped grade 7
mirror's «битүү / задгай тойрог». `algebra-1/inequalities` (13 Sep) wrote
«будсан / будаагүй цэг» (9 uses) and called it uncertain in its own Notes 3.
Two drafts, one idea, two pairs. I would align the older draft; one ruling.

### 6ag. Live: three English statements use a bare `$` for dollars; and three core/elective codes attached to the wrong unit

**Found 23 Sep 2026, drafting `algebra-2/functions-and-transformations`
(draft 53).**

**Rendering bug, live.** `a214-we2` («A taxi charges a $4 flag fee … then
$1.50 per km»), `a214-t2` («$10 for up to 5 GB, then $2 per extra GB») and
`a21-ty-6` («$30/month … plus $4 per extra visit») write the dollar sign
unescaped. MathText pairs them into a maths span, so the student reads «4 flag
fee covering the first 2 km, then» as italic maths with its spaces gone. A
scan of every maths span in all 212 English files for four or more plain words
finds **these three and nothing else** (the other hits are variable names such
as $PA \cdot PB$). Fix: `\$` in three strings. The scan would make a cheap
gate.

**Mis-attributed codes.** The unit is mapped to 11.3д (composite function,
core), 11.3е (inverse function, core), 11.3и and 11.3к. It teaches only
11.3и. Composition and inverses are taught in
`algebra-2/radicals-and-rational-exponents` lesson 4 («Inverse Functions»),
which is ЭШ Тэгшитгэл unit 7 and is mapped only to 10.2а. The same shape as
6j's two bookkeeping codes: move 11.3д, 11.3е, 11.3к to that unit.

### 6ah. 12.2 is taught in a unit mapped elsewhere; three wrong facts in `algebra-2/polynomial-functions`

**Found 23 Sep 2026, drafting `algebra-2/polynomial-functions` (draft 54).**

**Mis-attributed codes, the third case after 6j and 6ag.** The unit is mapped
to 10.3в (y = axⁿ from a value table, n = −2…3) and 11.3б (power functions)
and teaches neither: no table, no negative exponent. It teaches 12.2б
(division, quotient, remainder), 12.2в (Bezout, degree 3 and 4 equations,
unknown coefficient), 10.2д (cube formulas) and 10.5в (biquadratic). 12.2б,
12.2в and 10.2д are mapped to `algebra-1/polynomials-and-factoring`, whose
English has 0 hits for remainder, synthetic or cube. Move them here.

**Three wrong facts in live English** (corrected inside the Mongolian strings,
draft Notes 2):
- Lesson 1 teach [2]: "the cubic term is 97% of the total". At x = 100 the
  term is 2,000,000 and the total 1,950,093, so the term is 102.6% of the total.
- Lesson 4 concept 3: the box x(10 − 2x)(8 − 2x) = 48 "may have three
  algebraic roots but one physical answer". Its roots are 1, 2, 6; **two** lie
  in 0 < x < 4.
- Lesson 3 teach [5]: a² ± ab + b² "almost never factors further over the
  reals". For b ≠ 0 it never does (discriminant −3b²).

Also: tapQuestion [6] in lesson 4 offers a box cubic with roots 1, 6, −2; no
corner-cut box has a negative root product. And the funFact says Gauss was 21
in 1799; he was 22.

### 6ai. `buildsOn` is walked but never dumped: 42 drafts lack it, and the ЭШ spine shows English

**Found 23 Sep 2026, drafting `algebra-2/polynomial-functions` (draft 54).**

**The draft gap.** `mn_walk.py` line 114 walks the topic's `buildsOn` string,
so `mn_apply.py` will hard-fail on a missing index for every topic that has
one. `mn_topic_dump.py` never prints it, so the drafts never saw it: of the 43
earlier drafts whose English topic carries `buildsOn`, **42 have no Mongolian
for it**. Only `geometry/reasoning-and-proof` writes it. (`esh/sets-and-operations`
lists `buildsOn` as structural, but its English has none, so nothing is lost
there.) Draft 54 writes it.

**Backfilled 23 Sep, in the commit after draft 54.** All 42 now carry a
`**buildsOn:**` line after their BLURB. The audit also found that the four
earliest drafts (`10/quadratic-functions`, `algebra-1/inequalities`,
`algebra-1/linear-equations`, `algebra-1/systems-of-equations`) had **no topic
TITLE or BLURB either**. Both are walked strings, so both are now written. The
lines keep the home-course unit numbers («7-р нэгж»), as the shipped
`algebra-1-mn/quadratic-equations` mirror does: the string renders only on
home-course pages, because the ЭШ spine replaces it. What would stop this
recurring: make the dump print `buildsOn` and make `mn_draft_check.py` require
the three topic-level strings. That is a small tooling change for a ship
session.

**The live gap, ship-mode.** On the ЭШ hub, `getEshUnit` replaces the data's
`buildsOn` with the spine's (`lib/esh-course.ts`, `live()`'s fourth argument),
and `CourseShell` prints it under the Mongolian label «Тулгуур сэдэв нь:».
Five spine entries hard-code **English** there: «Factoring from Unit 4.»,
«Set operations and complements from Unit 1.», «Set operations from Unit 1;
the counting habits of Unit 2.», «The log laws from Unit 2.», «Combinations
from Unit 3.». An ЭШ student sees English under a Mongolian heading on those
five units. They are not in any mirror or draft, so the pipeline cannot reach
them: they need Mongolian written into `lib/esh-course.ts`, or a localized
field. The label is Khas's; the five lines under it are ordinary content, and
Mongolian for them can be drafted in a content session and written in by a ship
session.

### 6aj. «пропорционал» or «пропорциональ»; and three more leaked-working strings

**Found 23 Sep 2026, drafting `algebra-2/rational-functions` (draft 55).**

**The spelling is split, and the ministry is silent.** Measured:

| source | «пропорционал» | «пропорциональ» |
|---|---|---|
| ministry А/492 | 0 | 0 |
| exam bank | **3** (subtopic labels, incl. «урвуу пропорционал функц») | 0 |
| shipped mirrors | 0 | **97** |
| drafts before 55 | 27 | 3 |
| `mn-translation` skill glossary | | «пропорциональ хамаарал», «пропорциональ тогтмол» |

By the authority order the exam decides when the ministry is silent, and draft
55 writes «пропорционал». If you agree, the 97 mirror uses, the 3 draft uses
and the skill glossary want a `mn_terms.py` sweep. If you prefer the mirrors'
spelling, it is 30 draft uses the other way. One ruling either way.

**Four leaked-working strings in `algebra-2/rational-functions`**, all written
clean in draft 55 (its Notes 3): the `a274-t1` statement (already in 6h), and
three new ones: the `a274-we1` solution («**... verify numerically:**»), the
`a274-t2` solution («$1 = 3$**?? More carefully:**»), and lesson 3
tapQuestion [6] option 4 («$\dfrac{4}{x}$**... after cancelling the $x$'s**»,
an option that names its own error). 6h's count rises by three.

### 6ak. `\tan` or «tg»: the ministry and the exam bank disagree on notation

**Found 23 Sep 2026, drafting `trigonometry/right-triangle-trigonometry`
(draft 56), the first unit of ЭШ Тригонометр.**

| source | `\tan`, arctan | «tg», «arctg», «ctg» |
|---|---|---|
| ministry А/492 | 0 | **11.7д** writes tg, arctg |
| exam bank | **44** `\tan`, 4 `\cot` | 6–8 «tg», 1 «ctg» |
| drafts, incl. `geometry/right-triangles-and-trig` | all | 0 |

The ministry's «tg» is the Russian-school convention Mongolian textbooks
inherit; the bank mostly writes `\tan`, and every draft follows the bank. It
is not a vocabulary question the pipeline can fix after the fact: it changes
LaTeX inside answer options (`\tan 30°` vs `\operatorname{tg} 30°`), so it
wants a ruling **before the trigonometry topic ships**. Five more trig units
follow; each will carry the same choice.

### 6al. Two more leaked-working solutions, in `trigonometry/special-triangles-and-exact-values`

**Found 23 Sep 2026, drafting it (draft 57).** `trig24-t1` («…makes each half
an equilateral**... more directly:** area $= s^2\sin\theta$») and `trig2-ty-4`
(«…and $8\sin 30° = 4$**... assembling:**»). Both written clean in the draft
(its Notes 1); the first finishes the route the statement's own hint asks for.
6h's count rises by two, to 25–26. The same draft hedges an unconfirmed fun
fact (Prony's tables, "4,000 pages", "dozens of volumes") and corrects
«$1.41 + 1.73 = 3.15$» (it is 3.14; $\sqrt2 + \sqrt3 \approx 3.15$).

### 6am. `trigonometry/radians-and-the-unit-circle`: a wrong count, a leak, and two coinages

**Found 23 Sep 2026, drafting it (draft 58).**

- **Live English, wrong arithmetic**: lesson 4 teach [0] says symmetry hands
  you «all sixty-four (16 angles × 4 functions**...** minus the undefined
  tangents)». The lesson uses three functions: 16 × 3 − 2 = **46**. The
  Mongolian says 46.
- **Leak**: `trig3-ty-3` solution, «…mirror across the x-axis**... precisely:**
  they're supplement-and-reflection partners». Written clean. 6h's count
  rises by one, to 26–27.
- **Coinages to rule on**: «жишиг өнцөг» (reference angle: no source names
  it) and **Б · С · Т · К** for ASTC, which stands or falls with the
  Э/Г · Н/Г · Э/Н ruling.
- **Half-taught code**: 11.6б pairs arc length with sector area
  $S = \frac{1}{2}r^2\theta$; the unit never teaches sector area.

### 6an. 12.6а claimed but untaught; «далайц» means two things; two coinages

**Found 23 Sep 2026, drafting `trigonometry/graphs-of-trig-functions` (draft 59).**

- **12.6а** (secant, cosecant, cotangent and the graphs of all six functions)
  is mapped to this unit, which mentions them **zero** times; the whole
  trigonometry course mentions them **once**. The reciprocal functions are
  taught nowhere on the ЭШ spine. Elective, but the bank carries 4 `\cot` and
  1 «ctg». Same class as 6af.
- **«далайц»** is the physics word for amplitude and the ministry's word for
  the statistical range (11.11в). No clash inside a topic (a function's range
  is «утгын муж»), but across the ЭШ course one word means two things, as
  «хазайлт» does in 6ae.
- **Coinages**: «тэнцвэрийн шугам» (midline; «дундаж шугам» is taken by the
  geometry midsegment, 63 uses) and «фазын шилжилт» (phase shift, 0 in the
  corpus).

### 6ao. The auxiliary-angle formula is named by two codes and taught nowhere; the general solution is taught against 11.7е

**Found 23 Sep 2026, drafting `trigonometry/identities-and-equations` (draft 60).**

- **12.6б** and **12.6г** name the auxiliary-angle formula («туслах өнцгийн
  томьёо», $a\sin x + b\cos x = R\sin(x + \alpha)$) as a required method.
  The unit has **0** hits for it. Elective, but a named method with no lesson,
  the third such gap in trigonometry after 6am (sector area) and 6an
  (sec/csc/cot).
- **11.7е** excludes the general form of solutions; the unit teaches it (with
  `+ \pi k`). Extra content rather than wrong content. The draft adds
  «$k \in \mathbb{Z}$», the bank's notation (5 uses), where the English leaves
  $k$ undeclared.
- `trig5-ty-4` (6h, borderline) is written clean.

### 6ap. Trigonometry closed: three more leaks, two overclaims, and a mixed-script sweep of every draft

**Found 23 Sep 2026, drafting `trigonometry/laws-of-sines-and-cosines` (draft 61).**

- **Leaks**: the known statements `trig62-t2` («**... simpler:**») and
  `trig64-we2` («**... simpler classic:**»), both from 6h, plus a new one in
  the `trig6-pr-8` solution («**... cleaner:**»). All written clean. 6h's
  count rises by one, to 27–28, with every trigonometry item now drafted.
- **Overclaims toned down**: a funFact says France was measured "to meter
  precision in the 1700s" (the metre dates from the 1790s); teach [5] calls
  the unit set "the full trigonometry of the ЭШ", which 6am, 6an and 6ao
  contradict.
- **Mixed-script sweep.** Draft 61 briefly carried «Уулзварaас» with a Latin
  «a», the class of bug 6ad found in live English. A scan of all sixty-one
  drafts (prose outside maths and code spans) found **one more**: «харaарай»
  in `algebra-1/expressions-and-operations` (lesson 1, orderOfOps teach). Both
  fixed. The check is cheap and belongs in `mn_draft_check.py` (ship-mode).

### 6aq. Limits: in neither the ministry standard nor the ЭШ bank, and the unit's two codes are taught next door

**Found 23 Sep 2026, drafting `calculus/limits-and-continuity` (draft 62),
the first unit of ЭШ Анализын эхлэл.**

- **А/492 never uses «хязгаар»** in the calculus sense; its calculus starts at
  the tangent's slope (10.3д, 11.9а).
- **The ЭШ bank has no limit question**: 0 uses of `\lim`. Its calculus
  subtopics are «уламжлал», «шүргэгч шулуун», «шүргэгч ба нормал»,
  «интеграл», «Тодорхой интеграл», «Талбай, интеграл», «Антиуламжлал».
- So the whole unit is foundation the exam never tests: 6i's question (keep,
  mark, or cut) at the scale of a unit. Keeping it is defensible, since
  the derivative lessons use limits.
- **Mapping**: the unit's codes, 10.3д and 11.9а, are not taught in it (0 hits
  for tangent or slope); `the-derivative` teaches both. Move them.
- **Vocabulary is all compositional** (limit, one-sided limit, indeterminate
  form, the three discontinuity types, the Intermediate Value Theorem); the
  draft's Notes 3 lists them for correction.

---

## 7. Style decisions I made without asking, listed so you can veto cheaply

- **«хамгийн их / хамгийн бага утга», not «максимум / минимум».** Corpus 92/87.
- **«олон гишүүнт» written apart**, against the book's solid «олонгишүүнт» —
  the ministry writes it apart 14 times and the book concedes the point at
  p. 222.
- **The freshman's-dream funFact describes the nickname** instead of saying
  «оюутан», which the voice reference's smell test §3 reserves for university
  students.
- **Every English spelling-word in `prob-stats/permutations` is now a
  Mongolian one**, and this is the least cheap veto in this list because seven
  answers change with it. MOON, MISSISSIPPI, BANANA, LEVEL, BALLOON, SEEDED and
  TATTOO are chosen for their repeated letters; translated literally they make a
  Mongolian lesson about English spelling. The exam does this with Mongolian
  words («ДЭВТЭР», «ШАТАР», «ТОЙРОГ»), so I replaced all seven — АЛАГ,
  МИССИСИПИ, ХУРУУ, БАНАН, ХООЛООР, ТОГТООХ, БОЛОРМАА — kept each slot's role
  and recomputed every count. All seven verified mechanically, along with the
  exam's own three as a control.
  **One replacement changed the question, not just the word:** the drill slot's
  error model needs the wrong method to give a wrong answer, and «БАНАН»
  (А×2, Н×2) makes $\frac{5!}{2\cdot2}$ and $\frac{5!}{2!\,2!}$ both $30$, so
  the distractor collapses. «ХУРУУ» (У×3) separates $20$ from $40$. Full table
  in that draft's Notes 2. The word I am least sure of is «БОЛОРМАА», a given
  name rather than a common noun.
- **Mongolian-native images replace English ones** where they land better:
  таван хошуу мал for sorting like terms, цагаан сарын золголт for
  everyone-meets-everyone. This is the rewrite rule doing its job, but it is
  the most visible place a reader will feel my hand rather than yours.
