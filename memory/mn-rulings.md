# Rulings — decided, not open

Khas's answers, recorded where the next session will find them. Anything here
is **settled**; do not re-raise it.

Each entry says what changed as a result, because a ruling nobody acted on is
the same as no ruling.

---

## 26 August 2026

### R1 · Register is «та», formal — and this reverses the skill

> "чи is usually not used for customers. it is not suitable."

A student on this product is a customer. The voice strings Khas wrote the same
day confirm it: «Танд чухал зүйл», «Таны баталгаажуулах холбоосны хугацаа
дууссан байна».

**This contradicts `mn-translation`'s own style section**, which read
"friendly-instructional «чи» … not formal «та»". That wording is why grades 6
and 7 shipped in «чи» — 267 strings — and why the register audit flagged
grade 8 as the off-register one. **Grade 8 was right; its neighbours are the
problem.**

Changed: the skill's style section, `lib/i18n/chrome.ts`'s header, and the
brief generator (so every future brief says «та»). Briefs regenerated.

**Still open — and it is a cost question, not a language one:** whether the 267
«чи» strings already shipped in grades 6 and 7 get rewritten, or are left as
legacy. Nothing has been changed in them.

### R2 · `reflect` → «тэгш хэмээр хувиргах» · confirmed

Shipped content uses «тусгах» across a whole transformations unit, and that
word appears nowhere in the ministry standard. The term is settled; the shipped
strings are the bug.

Changed: term marked confirmed. The unit's strings are **not yet fixed** —
that sits under the section A go/no-go.

### R3 · `tree diagram` → «модны схем» · confirmed

The `mn-translation` glossary said «мод диаграм». The standard says «модны
схем» in 10.15б, 11.13д and 12.15а.

Changed: the skill's glossary corrected, and the correction recorded there
alongside the `тэнцэтгэл бус` / `тэнцэтгэл биш` one it resembles.

### R4 · Absolute value — **my finding was wrong, withdrawn**

I reported that «абсолют утга» (42×), «үнэмлэхүй утга» (13×) and «модул» (4×)
were three renderings of one term, and that ministry 12.1 meant «модул» should
replace the dominant form across ~59 strings. **That was wrong.** They are
different things:

| | |
|---|---|
| the **value** | «абсолют утга» — and «үнэмлэхүй утга» is equally correct |
| the straight brackets `\| \|` | «модул» — the notation itself |
| an absolute-value **equation** | «модулт тэгшитгэл» |
| taking \|x\| of a number | «тооноос модул авах» |

So ministry 12.1's «модул» is the *bracket* sense, and the site's "three ways"
is not an inconsistency at all. **No sweep is needed and A4 is withdrawn** —
about 59 strings that would have been rewritten for nothing.

Changed: four keys now exist where there was one (`absolute value`,
`absolute-value bars`, `absolute-value equation`, `take the absolute value`,
plus `modulus`), each marked confirmed. The skill name
`absolute-value-equations` became «Модулт тэгшитгэл бодох».

*Worth keeping as a lesson: the grounding checker can prove a term is absent
from a source, but it cannot tell whether two terms mean the same thing. Every
"inconsistency" it finds is a question, not a finding.*

### R5 · Two term corrections

| English | Was | Now |
|---|---|---|
| central angle | «төвийн өнцөг» | **«төв өнцөг»** — no genitive |
| perpendicular bisector | «дундаж перпендикуляр» | **«перпендикуляр таллагч»** |

### R6 · The 22 two-key splits stand

> "the word and the description of when to use seems accurate."

No change needed. The splits in §H of `mn-group0-questions.md` and the
`polysemous` entries in `data/i18n/mn-glossary-proposal.json` are approved as
written.

### R7 · Eight of nine voice strings written

Applied verbatim to `lib/i18n/chrome.ts`, marked `src: "VOICE"`.

| English | Khas's Mongolian |
|---|---|
| Soon | Удахгүй |
| Ready to check yourself? | Өөрийгөө шалгаад үзэх үү? |
| Focus first on | Түрүүнд анхаарах зүйл |
| Important for you | Танд чухал зүйл |
| Choose your level | Өөрийн анги, түвшинээ сонгох |
| Free to join | Үнэгүй нэгд |
| Complete a mock test and your trajectory appears here | Жишиг тестнээс гүйцэтгээд аялалаа эхлүүлээрэй |
| Your confirmation link expired | Таны баталгаажуулах холбоосны хугацаа дууссан байна |

**Two gaps, both left empty rather than filled in:**

1. *Confirmation email sent. Check your inbox.* — not in the batch.
2. The confirmation-link string is **two sentences** in English; the second
   ("Enter your email to resend") is not written. The entry carries the first
   sentence and is marked INCOMPLETE.

### R8 · Two terms paused

> "for the following, pause, i will need to confirm myself since im not sure"

`depression` («доош харах өнцөг») and `reference angle` («жишиг өнцөг») are
marked `ownerStatus: paused` and must not be used until Khas confirms.
