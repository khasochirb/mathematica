# The review pile — what is still uncertain after the glossary and the voice reference

**For Khas. Built 16 Sep 2026, after drafting all eight `algebra-1` topics.
Updated 17 Sep 2026, after the first two geometry topics.**

His instruction: *"let's push through most of the contents and then make it
ready for review. review as in the stuff that you're not sure even after using
the md's you sent."* This file is that list and nothing else. Anything the
dictionary, the voice reference or ministry order А/492 settled is **not** here
— it is settled, and recorded in the draft it belongs to.

**Voice reference §9 is fully applied and no longer a question.** All fifteen
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

**Scale if it changes:** fifteen drafts, and roughly 1,850 problem statements
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

Reversing it is a find-and-replace in one file. I followed the ministry because
a student who meets $m$ here and $k$ on the ЭШ paper is being mis-prepared.

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

### 2d. Math-mode decimals — **not applied. Surveyed: 205 of them.**

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
> rather than 178.

§7 says "every number a student reads", but the checks deliberately skip
`$...$` because the decimal point there is LaTeX, not Mongolian punctuation.
So `$x = 3.4$` in an answer option still renders a point.

Counted across the fifteen drafts:

| Draft | Math-mode decimals |
|---|---|
| `10/exponential-functions` | 144 |
| `algebra-1/linear-equations` | 20 |
| `algebra-1/inequalities` | 10 |
| `algebra-1/systems-of-equations` | 8 |
| `10/quadratic-functions` | 7 |
| `algebra-1/linear-functions` | 7 |
| `geometry/foundations` | 5 |
| `esh/number-sets-and-intervals` | 3 |
| `algebra-1/functions` | 1 |
| **total** | **205** |

Exponential functions carries four fifths of them because growth factors
(`$b = 1.05$`, `$V = 800(0.75)^t$`) are decimals by nature.

**Why this is your call and not a mechanical follow-on from 2b.** In KaTeX the
change is `1.05` → `1{,}05`, which renders «1,05» correctly but makes every
formula noisier to read and to edit, and it diverges from the English mirror in
205 places rather than eight. It also touches `check[]` neighbourhoods, though
not `check[]` itself. If §7 governs maths mode, it is one scripted pass plus a
render QA walk; if it governs prose only, nothing changes. **Prose decimals
(item 2b) are already done either way** — this is only about the inside of
`$...$`.

---

## 3. Terms I coined — ungrounded, and I know it

Each is built from grounded parts, defined on first use, and flagged in its
draft. None is in the dictionary's a–i range or in А/492 or the corpus.

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

## 5. Things you said to ask about, which I have not decided

### 5a. The English term on first use

Your uploaded CLAUDE.md lists this as an open decision and says to ask before
adopting either convention site-wide: «өнцгийн биссектрис (angle bisector)».
**Not used anywhere.** Worth settling soon — every draft has terms an
English-medium exam will show in English.

### 5b. Two English acronyms dropped, not translated

**FOIL** and **PEMDAS**. Both spell English sentences and spell nothing in
Mongolian. The lessons teach the rule and drop the acronym — for FOIL the
English itself says "the rule is just double distribution". The book does carry
FOIL («Хоёр хоёргишүүнт үржүүлэх арга», p. 163), so this is a choice, not a
gap. Flagging it because dropping a mnemonic a student may meet in an
English-medium exam is a content decision, not a translation one.

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

Three of the four are in one topic. The Mongolian drafts coin all four and flag
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
