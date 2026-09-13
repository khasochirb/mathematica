# Mongolian — everything waiting on Khas

Generated 11 Sep 2026 from the repo, not from memory. Ordered by blast radius:
the further down, the cheaper it is to change later.

Nothing below is deployed. Production still serves English on every surface
this touches.

---

## 1 · The 158 chrome entries still in my wording — `lib/i18n/chrome.ts`

234 entries total:

| marker | count | what it means |
|---|---|---|
| `GLOSS` | 25 | locked by ministry А/492 or the glossary — not mine, don't need you |
| `SITE` | 24 | copied verbatim from Mongolian already on the site — not mine |
| **`NEW`** | **127** (8 approved) | **proposed by me. These are the ones to correct.** |
| **`DERIV`** | **39** | **stem is established, the ending is mine** |
| `VOICE` | 19 | yours — see §2 |

An entry carrying `ok: "<date>"` has been read and approved by Khas and is
out of the queue. **158 remain** (NEW + DERIV without `ok`).

**Reviewed 13 Sep 2026 — the nine highest-frequency entries.** Batching by
frequency was the lesson of the «Бүлэг» correction: one wrong word was wrong
in 36 places, so the top of the frequency table is where a review hour buys
the most.

| en | mn | n | outcome |
|---|---|---|---|
| Back to the course | Курс руу буцах | 35 | kept |
| Reset | Дахин эхлэх | 20 | kept |
| Lessons | Хичээлүүд | 15 | kept — plural stands beside the tab's «Хичээл» |
| **Builds on** | **Тулгуур сэдэв нь:** | 12 | **rewritten by Khas** |
| Live | Нээлттэй | 4 | kept |
| What you'll learn | Юу сурах вэ | 3 | kept |
| Watch out | Болгоомжил | 3 | kept — bare form stands; a box label, not speech to a student |
| Key idea / The idea | Гол санаа / Санаа нь | 3 each | kept, deliberately distinct |

**The specific risk: case endings.** Mongolian accusative (-ийг / -ыг / -г) and
directional (руу / рүү) agree with the vowel of the noun they attach to. About
sixty of the widget labels carry one. Assume some are wrong.

Cheapest way to review: open `lib/i18n/chrome.ts` and read only the lines
marked `NEW` and `DERIV`. Each carries a `note` where the reasoning isn't
obvious. Correcting the `mn` string in place is the whole fix — every page
reads from this one file.

Worth a specific look:

- **The widget batch** (section 8, 96 entries) — the densest concentration of
  case endings, and the one I am least able to judge.
- `"Back to unit"` → «Нэгж рүү буцах» — рүү not руу after front-vowel «нэгж».
  Flagged since August, still unconfirmed, and it is the pattern the other
  nine "Back to X" entries copy.
- `"Lessons"` → «Хичээлүүд» vs the site's unmarked «Хичээл».

---

## 2 · Voice strings — one left of eleven

Khas wrote ten on 13 Sep 2026, and they are wired verbatim. **One is still
empty, and its surface renders English until it is filled:**

- `Per-component accuracy and weakest areas, once you start practicing` —
  the IB hub progress banner. It is the twin of the SAT banner he did write
  («Сул сэдвээ тодорхойлж, цагаа хэмнэх. Уг сэдвээ өөрийн болгож эзэмших»),
  so the open question is only whether that SAT wording is reused here or
  the IB banner gets its own sentence.

The footer tagline was also his and is now a VOICE entry, written and wired.

Still outstanding, and **not** dictionary entries because they are
**sentences with a value interpolated into them**, which Mongolian suffixes
cannot survive being dropped into:

- **«Focus first on X — marked below»** on all seven grade hub pages. His
  «Түрүүнд анхаарах зүйл» is a noun phrase; it needs a sentence built around
  the unit names, not a substitution.

---

## 3 · Three decisions that shape everything downstream

**3a. The ЭШ interval bracket convention — SETTLED 13 Sep 2026: `]2, 7[`.**
The past papers use two, and among the shapes that actually discriminate, the
reversed one won 105 to 46. Khas ruled for the papers' convention. Scope is
the ЭШ hub only; SAT and IB keep `(a, b)`. The full table and the conversion
rules are in `memory/mn-drafts/README.md`. No longer a question — left here
because §3b and §3c below still are.

**3b. «муж» is doing two jobs.** It is the exam's own word for a Venn region
(«хүрэн муж», test4a) — but the bank uses it far more often for a function's
domain and range («тодорхойлогдох муж», «утгын муж»). A student meets both
inside the ЭШ course. Keeping the exam's word affects every function topic;
changing it diverges from the paper.

**3c. Coined names for reflexes.** I have invented two — «нэгийг нэм» (the +1
counting rule) and «төвийг хас» (peel the centre from a pairwise overlap).
Two is a house style, not a one-off. Say once whether the product should name
its moves this way; if not I will stop and describe them instead.

---

## 4 · Four topic drafts — 17,000 words of Mongolian prose

Nothing has been applied to a mirror. Each has a **Notes for Khas** section at
the foot with the specific items.

| draft | words | items for you |
|---|---|---|
| `esh-sets-and-operations.md` | 4,400 | 8 |
| `esh-venn-diagrams-and-counting.md` | 3,600 | 5 |
| `esh-number-sets-and-intervals.md` | 3,600 | 5 |
| `10-exponential-functions.md` | 5,400 | 4 |

**This is the one where reading early pays most.** All four are written in one
voice, with one register and one set of coined names, and every one of the
remaining 176 topics will inherit them. Finding out at topic forty costs forty
topics of rework.

Terms across the four I could ground in neither А/492 nor the ЭШ bank, so they
rest on your judgement alone: «хагас задралын хугацаа» (half-life), «нийлмэл
хүү» (compound interest), «нэмэх–хасах зарчим» (inclusion–exclusion), «битүү
/ нээлттэй завсар» (closed/open interval — avoided so far), «цацраг» (ray).

---

## 5 · The glossary backlog — 644 of 667 terms unreviewed

23 have your ruling. The rest have never been looked at.

**The 21 unruled polysemous terms are the dangerous ones** — one Mongolian word
standing in for two English senses, which ships wrong silently:

| term | current | uses |
|---|---|---|
| **`factor`** | «хуваагч» | **3,133** |
| `count` | «тоолох» | 2,393 |
| `half` | «хагас» | 1,468 |
| `base` | «суурь» | 1,405 |
| `row` | «мөр» | 1,346 |
| `shape` | «дүрс» | 1,269 |
| `range` | «далайц» | 1,201 |

`factor` is the urgent one. R9 split `complement` into angle vs set senses and
that split has already earned its keep — the factor *tree* widget needs
«үржигдэхүүн» (prime factors) while the factor *rainbow* needs «хуваагч»
(divisors), and I used both in the widget batch. The glossary's single entry
still says «хуваагч» for all 3,133 uses.

**Still paused, must not be used until you confirm:** `depression`
(«доош харах өнцөг»), `reference angle` («жишиг өнцөг»).

---

## 6 · Two product findings — not translation, but found by doing it

**G1 · A ministry objective nothing teaches.** `lib/esh-course.ts` maps
`exponential-functions` to А/492 objectives 10.3г, 10.3е and **10.5д**. 10.5д
is **non-elective** — «Илтгэгч тэгшитгэлийг графикийн болон орлуулах аргаар
бодох» — it is claimed by that unit and no other, and the words "equation" and
"solve" appear **zero times** in the topic. Three options in
`memory/mn-findings/esh-scope-gaps.md`: extend the unit, re-map the objective,
or accept the gap deliberately.

**The ministry's own chart vocabulary is unsafe.** А/492 gives dot plot «цэгэн
диаграм» and scatter plot «цэгэн диаграмм» — one doubled м apart. I followed
the site's distinguishable «цэгэн график» / «хамаарлын график» instead.
Confirm that is right.

---

## What I would do with an hour of your time

§3a, §3b and the `factor` row of §5 — three decisions, each of which otherwise
gets baked into dozens of topics. Then §2's ten voice strings, which are the
only thing blocking those surfaces from being finishable at all.
