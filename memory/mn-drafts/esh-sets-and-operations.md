# Draft — `esh/sets-and-operations`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

Khas reads this before anything touches `data/genmath/esh-mn/`. That review is
step 3 of the order of operations in the Build brief and is not optional — the
gates check the maths and the glossary, and nothing checks whether the prose is
good.

**What I can and cannot vouch for.** The terminology is grounded: every term
below is taken from ministry order А/492 (§10.6 «Олонлог») or from the ЭШ
question bank, which is Mongolian-first and where «олонлог» appears 68 times,
«дэд олонлог» 25, «элемент» 39, «огтлолцол» 16. The exam's own phrasing
patterns («... олонлог өгөгдөв», «... аль нь вэ?») are followed deliberately, so
a student meets the same wording here as on the paper. **What I cannot judge is
whether it reads naturally.** That is the whole reason for the review step.

Register is «та», per the ruling of 26 Aug.

---

## What makes this a rewrite and not a translation

The English lesson opens with a formal definition of a set, mentions the
element-vs-subset trap second, and reaches the counting rule third.

**This version reverses that**, because the students are different. The ЭШ
course assumes ~650/800 — they already know what a set is. What loses them
marks is the two-level distinction and the `+1`. So:

- the lesson opens with the **exam trap**, not the definition
- the definition arrives as a *reminder*, compressed into one paragraph where
  English used three
- the counting rule gets its own beat and a name — «нэгийг нэм» — so it is
  drilled as a reflex rather than derived once
- the worked examples keep their contexts. The brief permits changing them, but
  both here are bare number problems with no cultural setting to localise, and
  changing the arithmetic would cost a rewritten `check` for nothing

Different paragraph count, different order, different framing. The skeleton —
lesson slug, the two worked-example ids, the two try-it ids, the nine
interactive steps and their kinds — is untouched.

---

## sets-and-membership

**TITLE:** Олонлог, харьяалал, элементийн тоо

**OBJECTIVE:** Олонлогийг жагсаалтаар болон нөхцөлөөр бичих, «элемент мөн үү»
гэдгийг «дэд олонлог мөн үү» гэдгээс ялгах, элементийн тоог алдаагүй тоолох.

**KEY IDEA:** Олонлогийг зөвхөн харьяалал тодорхойлно — дараалал ч үгүй,
давталт ч үгүй. Нэг элементийн тухай $\in$, бүхэл олонлогийн тухай $\subseteq$
өгүүлнэ.

**TEACHING:**

Шалгалтын хамгийн олон оноо алддаг зүйл бол олонлогийн тодорхойлолт биш,
харин **хоёр түвшнийг хооронд нь андуурах** явдал юм. Үүнээс эхэлье.

$\{2, 4\}$ гэсэн олонлогийг авъя. $2$ бол түүний **элемент** тул
$2 \in \{2, 4\}$ үнэн. $\{2\}$ бол нэг элементтэй **олонлог** тул
$\{2\} \subseteq \{2, 4\}$ мөн үнэн. Харин $\{2\} \in \{2, 4\}$ нь **худал** —
учир нь $\{2, 4\}$-ийн элементүүд бол $2$ ба $4$ гэсэн тоонууд, олонлог биш.
ЭШ-ийн хувилбарууд энэ гурав дахь хэлбэрийг сонголт болгон байнга тавьдаг.

Ялгааг богиноор: $\in$ нэг элементийн тухай, $\subseteq$ бүхэл олонлогийн
тухай ярина.

Тэгвэл олонлог гэж юу вэ. Олонлог нь ялгаатай зүйлсийн эмх цэгцгүй цуглуулга
бөгөөд зөвхөн «юу нь дотор байна вэ» гэдгээр тодорхойлогдоно. Тиймээс
$\{1, 2, 3\}$, $\{3, 2, 1\}$, $\{1, 1, 2, 3\}$ гурав нь **нэг ижил** олонлог.
Бичих хоёр арга бий: жагсаалтаар — $A = \{2, 4, 6, 8\}$, эсвэл нөхцөлөөр —
$A = \{x \in \mathbb{Z} : -2 \le x < 4\}$, энэ нь «$-2$-оос $4$ хүртэлх, $4$-ийг
оруулахгүй бүхэл тоонууд» гэсэн үг.

Хоосон олонлог $\varnothing$ нь ямар ч элементгүй бөгөөд **аль ч олонлогийн**
дэд олонлог болно.

Одоо оноо шууд авчирдаг дадал руу орьё: **нэгийг нэм**. $a$-аас $b$ хүртэлх
бүхэл тоонуудын тоо нь $b - a + 1$. Хоёр захыг нь хоёуланг нь тоолж байгаа тул
хасаад зогсохгүй нэгийг нэмнэ. Хурдан бодогчид яг энэ нэгэн дээр оноо алддаг —
$\{5, 6, \ldots, 20\}$ дотор $15$ биш, $16$ элемент бий.

Элементийн тоог $|A|$ (эсвэл $n(A)$) гэж тэмдэглэнэ.

**MISTAKES:**

- $\{2\} \in \{2, 4\}$ гэж бичих. «$2$ нь олонлогт байгаа» гэдэг үнэн боловч
  тэр нь $2 \in \{2, 4\}$ гэсэн үг. $\{2\}$ бол олонлог тул $\subseteq$ хэрэглэнэ.
- $\{5, 6, \ldots, 20\}$-ийг $20 - 5 = 15$ элементтэй гэж тоолох. Хоёр захыг нь
  оруулж тоолж байгаа тул $20 - 5 + 1 = 16$ болно.

**WORKED esh-sets-l1-we1:**

- **PROBLEM:** $A = \{x \in \mathbb{Z} : -2 \le x < 4\}$ олонлогийн элементүүдийг
  жагсааж, $|A|$-г ол.
- **WORKING:** Нөхцөл нь $-2$-оос эхэлж, $4$-ийг оруулахгүй тул хамгийн их
  элемент нь $3$. Иймд $A = \{-2, -1, 0, 1, 2, 3\}$. Тоолохдоо нэгийг нэмэх
  дүрмээр: $3 - (-2) + 1 = 6$.
- **ANSWER:** $|A| = 6$

**WORKED esh-sets-l1-we2:**

- **PROBLEM:** $50$-аас бага, $3$-т хуваагддаг натурал тоо хэд байх вэ? Эхлээд
  олонлогийг нөхцөлөөр бич.
- **WORKING:** $M = \{x \in \mathbb{N} : x < 50,\ 3 \mid x\} = \{3, 6, \ldots, 48\}$.
  Хамгийн их нь $48 = 3 \cdot 16$ тул элементүүд нь $3 \cdot 1$-ээс
  $3 \cdot 16$ хүртэл. Өөрөөр хэлбэл $16$ ширхэг.
- **ANSWER:** $16$

**TRY esh-sets-l1-t1:**

- **PROBLEM:** $B = \{x \in \mathbb{Z} : -7 < x \le 5\}$ бол $|B|$ хэд вэ?
- **ANSWER:** $12$
- **WORKING:** $-7$ өөрөө хатуу тэнцэтгэл бишээр хасагдах тул $-6$-аас $5$
  хүртэл: $5 - (-6) + 1 = 12$.

**TRY esh-sets-l1-t2:**

- **PROBLEM:** $7$-д хуваагддаг хоёр оронтой тоо хэд байх вэ?
- **ANSWER:** $13$
- **WORKING:** Хоёр оронтой, $7$-д хуваагддаг тоонууд $14 = 7 \cdot 2$-оос
  $98 = 7 \cdot 14$ хүртэл. Иймд $14 - 2 + 1 = 13$.

---

## Interactive steps — same nine, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Хоёр түвшин · **title** Элемент үү, дэд олонлог уу?<br>**body** $\in$ нэг элементийн тухай, $\subseteq$ бүхэл олонлогийн тухай өгүүлнэ. $2 \in \{2, 4\}$ ба $\{2\} \subseteq \{2, 4\}$ хоёулаа үнэн, харин $\{2\} \in \{2, 4\}$ худал — шалгалт яг үүнийг санал болгодог. |
| 1 | teach | **eyebrow** Хэлний дүрэм · **title** Зочны жагсаалт, дараалал биш<br>**body** Олонлог зөвхөн харьяалалд ач холбогдол өгнө. $\{1, 2, 3\}$, $\{3, 2, 1\}$, $\{1, 1, 2, 3\}$ гурав нь нэг ижил олонлог — дараалал ба давталтыг тооцохгүй. |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Аль нь үнэн бэ?<br>**prompt** $A = \{1, \{2\}, 3\}$ бол аль нь ҮНЭН вэ?<br>**options** `$\{2\} \in A$` · `$2 \in A$` · `$\{1, 2\} \subseteq A$` · `$|A| = 2$` — **correctIndex 0**<br>**explanation** $A$-гийн элементүүд нь $1$, $\{2\}$ гэсэн ОЛОНЛОГ, ба $3$. Тиймээс $\{2\} \in A$ үнэн, харин $2$ гэсэн тоо өөрөө элемент биш. $\|A\| = 3$. |
| 3 | worked | **title** Нөхцөлөөс жагсаалт руу — `esh-sets-l1-we1` |
| 4 | worked | **title** Хуваагдах тоо тоолох — `esh-sets-l1-we2` |
| 5 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Нэгийг нэмэх дадал<br>**prompt** $-4 \le x \le 9$ нөхцөлийг хангах бүхэл тоо хэд вэ?<br>**options** `$13$` · `$14$` · `$12$` · `$9$` — **correctIndex 1**<br>**explanation** Хоёр захыг нь оруулж тоолно: $9 - (-4) + 1 = 14$. Нэгийг нэмэхээ мартвал $13$ гэсэн сонирхол татам буруу хариу гарна. |
| 6 | tryIt | **title** Нэг тал нь хатуу — `esh-sets-l1-t1` |
| 7 | tryIt | **title** Хоёр оронтой хуваагдагч — `esh-sets-l1-t2` |
| 8 | recap | **title** Санаж үлдэх зүйл<br>**points** Олонлогийг зөвхөн харьяалал тодорхойлно — дараалал ч, давталт ч биш · $\in$ элементэд, $\subseteq$ олонлогт; $\varnothing$ нь бүх олонлогийн дэд олонлог · $a$-аас $b$ хүртэл: $b - a + 1$ |

---

## Notes for Build

- `check[]` for both worked examples and both try-its is **unchanged** — the
  arithmetic is identical, only the wording moved. `we2` keeps
  `Eq(floor(Rational(49,3)), 16)` and `Eq(3*16, 48)`; `t2` keeps its three.
- No currency appears in this lesson, so the ₮ rule does not bite here.
- No Cyrillic inside `$...$` anywhere above. `$\|A\| = 3$` in step 2 is escaped
  for the table only; the JSON carries `$|A| = 3$`.

## Notes for Khas

1. **«нэгийг нэм»** as the name for the +1 rule is mine. It needs to be
   memorable enough to become a reflex — if it sounds clumsy, the whole point
   of naming it is lost and it should just be described.
2. **«эмх цэгцгүй цуглуулга»** for "unordered collection" is mine and I am least
   sure of it.
3. **«зочны жагсаалт»** (guest list) renders the English step title "Guest
   lists, not queues". The metaphor may not carry; a Mongolian one would be
   better and is yours to pick.
4. `esh-sets-l1-we2` keeps the multiples-of-3 context rather than moving to a
   local one. The brief permits changing it, but the `check` verifies this exact
   arithmetic, so changing the context here buys nothing and costs a rewritten
   assertion.
5. **The problem statements use bare imperatives — «ол», «бич».** That is the
   traditional Mongolian exam-question form and it is what the ЭШ bank uses, but
   it is grammatically the informal command, and the register ruling said «та».
   I have followed exam convention over the ruling on the assumption that a
   problem statement is not the product addressing a student. **If that is
   wrong, it is wrong in every problem statement across all 177 topics**, so it
   is worth settling now rather than at topic fifty.
