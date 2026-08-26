# Group 0 — the accumulated question list

Everything from the vocabulary pass that needs Khas. Batched, as
`docs/MONGOLIAN.md` asks, rather than stopping the session per question.

Data: `data/i18n/mn-glossary-proposal.json` (659 terms) ·
`data/i18n/mn-skill-names.json` (184 skill names). Neither is wired, neither
is in `mn_terms.py`.

---

## A. Live terminology bugs already in production

These are not proposals. They are inconsistencies **in shipped Mongolian**,
found by checking each proposed term against what the mirrors and the ЭШ bank
actually say. They are worth fixing whatever you decide about the rest.

| # | What | Evidence | Cost to fix |
|---|---|---|---|
| A1 | **volume** ships two ways | «эзлэхүүн» 37× vs «эзэлхүүн» 9×. The ministry is *itself* inconsistent — эзлэхүүн in 10.12, эзэлхүүн in 11.10 | 9 strings |
| A2 | **"Fraction" rendered as «Хэсэг»** in two strings («Хэсэг $= \frac{13}{40}$») against «бутархай» 463× everywhere else | the term is settled; those two strings are simply wrong | 2 strings |
| A3 | **reflect** — every shipped item uses «тусгах», a word **absent from the ministry standard**. The ministry and glossary both say «тэгш хэмээр хувиргах» | a whole transformations unit | unit-wide |
| A4 | **absolute value ships three ways**: «абсолют утга» 42×, «үнэмлэхүй утга» 13×, «модул» 4×. Ministry 12.1 says **модул** | contradicts the dominant shipped form | ~59 strings |
| A5 | **addition** — "like you do for addition" ships as «Нэмэлт шиг…», and «нэмэлт» is *also* the site's word for an angle's complement (21×) | one word, two unrelated meanings | few strings |
| A6 | **multiplication** ships as «үржүүлэг» 29× and «үржүүлэлт» 14× | the four operations don't match each other | ~43 strings |
| A7 | **combination** — one shipped item says «хослол» where ministry and glossary are firm on «хэсэглэл» | true combinatorics content | 1 string |
| A8 | **spread vs distribution** both ship as «тархалт» — including in the *same sentence* ("A full description of a DISTRIBUTION touches … SPREAD" → «ТАРХАЛТын бүрэн дүрслэл … ТАРХАЛТ») | reads as one word for two ideas | see B2 |
| A9 | **scatter plot vs dot plot** both ship as «цэгэн диаграмм» | two different charts, one name | live |
| A10 | **quantity** — «хэмжигдэхүүн» in two lines, but «тоо» and «тоо хэмжээ» elsewhere for the same English word | inconsistent | few |
| A11 | **tree diagram** — the glossary says «мод диаграм»; the **ministry says «модны схем»** (10.15б, 11.13д, 12.15а) | glossary contradicts the standard | glossary + mirrors |

A11 is the same shape as the `тэнцэтгэл бус`/`тэнцэтгэл биш` correction already
on record: a glossary entry that the standard does not use.

---

## B. Splits — one English word, two Mongolian words

The reconciler found these by comparing across batches. Each needs **two keys**
in the glossary, not one, and picking one form would make two ideas
indistinguishable to a student.

| # | English | The two senses |
|---|---|---|
| B1 | **range** | statistics (max−min) = «далайц» (ministry 10.13, 11.11) · a function's range = «утгын муж / дүр» (ministry 11.3) |
| B2 | **spread / distribution** | distribution = «тархалт», locked by ministry (12.12 бином тархалт, 12.13 хэвийн тархалт). Spread must therefore be something else — the standard files spread measures under «хазайлт» (11.11). Production already uses тархалт 38× and хазайлт 28× |
| B3 | **shape** | geometric shape = «дүрс» (73×) · the shape of a distribution = «хэлбэр» |
| B4 | **complement** | an angle's complement = «нэмэлт» (21×) · an event's complement = «гүйцээлт» (7×). Neither is in the ministry standard |
| B5 | **variation** | the algebra sense (direct/inverse) vs. "proportional relationship" = «пропорциональ хамаарал» |
| B6 | **division** | the operation = «хуваалт» (33×) · but the ministry uses «хуваалт» for a *partition* (11.10, integration). Collides when calculus lands |
| B7 | **modelling / simulation** | all three currently «загварчлал»; simulation is a different concept |
| B8 | **rate** | «хурдац» (106×) — but do **not** substitute into "rate of change", which is «өөрчлөлтийн хурд» |

---

## C. Spelling the ministry itself is inconsistent about

| | Ministry | Production | Note |
|---|---|---|---|
| **parallel** | «параллел» 4× (10.12, 11.5, 11.10, 12.5) · «параллель» 2× (10.11, 12.5) | «параллель» 21×, «параллел» 0× | keeping параллель costs nothing |
| **volume** | «эзлэхүүн» 10.12 · «эзэлхүүн» 11.10 | 37× vs 9× | see A1 |

---

## D. One decision that shapes all 184 skill names

**Should a skill label be a noun phrase or the ministry's verbal-noun form?**

58 of the 184 English names are imperative clauses ("Solve a quadratic by
factoring"). They are descriptive, not persuasive, so I did **not** treat them
as voice. But the ministry writes its own objectives verbally —
«Рационал илтгэгчтэй зэргийн тодорхойлолтыг мэдэх, хэрэглэх» ("know and apply
…"). So there are two defensible house styles:

- **nominal** — «Квадрат тэгшитгэлийн үржигдэхүүнд задлах арга»
- **ministry verbal** — «Квадрат тэгшитгэлийг үржигдэхүүн болгон задлаж бодох»

The proposals currently use the **verbal** form, following the ministry. These
labels appear in the plan, the skill map, progress, and the **parent report** —
a parent who does not read English sees these and nothing else. Worth one
decision now rather than 184 edits later.

---

## E. Phrasal skill names — 4 of 184

Flagged per your instruction. All four are *descriptive* imperatives rather
than persuasion, so I do not think any is voice — but you asked to see them:

- `data-representation` — "Read bar charts, histograms and frequency tables"
- `grouped-frequency-mean` — "Estimate the mean from a grouped frequency table"
- `box-plots` — "Construct and interpret a box plot"
- `combined-standard-deviation` — "Combine the means and standard deviations of
  two groups" · **read this one first**: «Нэгдсэн» is invented and nothing backs
  it; the standard has no objective for pooling two groups

---

## F. Where the confidence sits

| | Terms (659) | Skills (184) |
|---|---|---|
| **quoted** — the named source contains the phrase | 461 | 47 |
| **composed** — long label from ≥80% source vocabulary | 7 | 98 |
| **upgradable** — said "proposal", a source has it | 97 | 2 |
| **novel** — genuinely mine, expect correction | 80 | 19 |
| **unsourced** — named a source that lacks the phrase | 14 | 16 |
| **weak-composition** | 0 | 2 |

**170 rows are marked low confidence.** Those and the 99 `novel` rows are where
your time buys the most.

Three rows name a source that does not contain the word **at all** — `sample`
(«түүвэр»), `period` («үе»), `segment` («хэрчим»), all claimed as ministry. The
terms may still be right; the citation is not.

---

## G. Group 0 is complete

**659 terms** (622 corpus + 37 operational) and **184 skill names**. The
operational batch came back unusually well-sourced — 36 of 37 quoted verbatim
from shipped content or the ministry, none questionable — which is what you
would expect for words the site already uses constantly.

---

## H. Polysemy — English hides a split Mongolian makes

From the operational sweep. These are high-frequency words, so a wrong pick is
wrong in thousands of sentences. **The proposal gives one sense; the other is
named so it does not get silently overwritten.**

| English | Proposed sense | The other sense |
|---|---|---|
| **row** | мөр — a grid, table or matrix row | эгнээ — a row of physical objects; **ministry 11.12** uses эгнээ for the combinatorics arrangement |
| **half** | хагас — the computed amount ½ | тал — one of two portions. тал is *also* “side”, so it carries real ambiguity |
| **count** | тоолох — the verb | тоо (how many) · тооллого (the tally itself). Never тоолол |
| **scale** | томсгох — the verb, to scale up (opposite багасгах) | масштаб — a map’s scale · масштабын коэффициент — scale factor |
| **increase** | өсөх — intransitive, to be increasing (opposite буурах) | өсөлт — the noun, which the percent unit actually ships · ихэсгэх — transitive |
| **edge** | ирмэг — of a solid, and of a histogram bin | зах — the margin of something written or laid out |
| **measure** | хэмжих — the verb | хэмжээ — the noun · хэмжигдэхүүн — a measured quantity |
| **size** | хэмжээ — magnitude | see amount; the two share хэмжээ |
| **amount** | хэмжээ — quantity | collides with size — both ship as хэмжээ |
| **tens** | аравт — the tens place | place-value family: нэгж / аравт / зуут / мянгат |
| **hundreds** | зуут — the hundreds place | same family |
| **thousands** | мянгат — the thousands place | same family |

`row` is the sharpest: the ministry's own combinatorics objective (11.12) uses
**эгнээ**, while every coordinate-plane and table context in shipped content
uses **мөр**. A single glossary key for "row" would put the wrong word into one
of them.

`base` deserves a note of its own: Mongolian does **not** split it — «суурь»
covers the base of a power, of a triangle, of a prism and of a logarithm. But
«суурь вектор» is *basis vector*, a different concept sharing the word, so
vector lessons must write it in full and never let a bare «суурь» stand for a
basis.
