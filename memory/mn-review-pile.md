# The review pile — what is still uncertain after the glossary and the voice reference

**For Khas. Built 16 Sep 2026, after drafting all eight `algebra-1` topics.**

His instruction: *"let's push through most of the contents and then make it
ready for review. review as in the stuff that you're not sure even after using
the md's you sent."* This file is that list and nothing else. Anything the
dictionary, the voice reference or ministry order А/492 settled is **not** here
— it is settled, and recorded in the draft it belongs to.

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

**Scale if it changes:** ten drafts, and roughly 1,400 problem statements.

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

### 2d. Math-mode decimals — **not applied, not yet surveyed**

§7 says "every number a student reads", but the checks deliberately skip
`$...$` because the decimal point there is LaTeX. So `$x = 3.4$` in an answer
option still shows a point. If §7 governs maths mode too, this is a bank-wide
sweep and wants its own pass.

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

### 4b. `absolute value` — open since 13 Sep

The book's «абсолют хэмжигдэхүүн» against 53 live uses of «абсолют утга».
Ministry silent. Does not touch any topic drafted since.

---

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

## 6. Two English content bugs found while drafting

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
