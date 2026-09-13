# Draft — `esh/sets-and-operations`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

Khas reads this before anything touches `data/genmath/esh-mn/`. That review is
step 3 of the order of operations in the Build brief and is not optional — the
gates check the maths and the glossary, and nothing checks whether the prose is
good.

**Complete topic**: all four lessons, ten practice items, seven test-yourself
items, and the topic-level strings. Nothing in this topic is left half-drafted.

**What I can and cannot vouch for.** The terminology is grounded: every term
below is taken from ministry order А/492 (§10.6 «Олонлог») or from the ЭШ
question bank, which is Mongolian-first. Frequencies in the bank: «олонлог» 96,
«элемент» 42, «дэд олонлог» 27, «ялгавар» 23, «огтлолцол» 16, «нэгдэл» 8. The
exam's own phrasing patterns («... олонлог өгөгдөв», «... аль нь вэ?»,
«$|X|$ − $X$ олонлогийн чадал буюу элементийн тоо») are followed deliberately,
so a student meets the same wording here as on the paper. **What I cannot judge
is whether it reads naturally.** That is the whole reason for the review step.

Register is «та», per the ruling of 26 Aug.

---

## Three decisions the corpus forced, before any prose

These are changes to what lesson 1 said when it was drafted alone. Each one came
out of reading the ЭШ bank rather than out of taste, and each one applies to the
whole topic.

### 1. The complement is $\overline{A}$, not $A'$ — in both languages

Counted across the 54 real past papers:

| complement written as | count |
|---|---|
| $\overline{A}$ (overline) | 13 |
| $A'$ (prime) | 0 |

All four primes that do appear in the bank are reflected points
($A' = 2F - A$), never complements.

**The argument is exam fidelity, not symbol collision.** A student who learns
complement as $A'$ and meets $\overline{A}$ on the paper has to translate under
time pressure, and that is the only cost that matters here. I first argued this
on the grounds that $A'$ collides with $f'$ for *derivative* in the same course;
that point is weaker than I made it sound — context separates $f'(x)$ from a
bare capital, and textbooks live with the overlap routinely. It is not the
reason. The reason is that this is the notation the exam uses.

Worth stating honestly: **the exam overloads the overline too.** In the same
bank it also means digit concatenation ($\overline{ab} = 10a + b$, 12 uses) and
a repeating decimal ($0.\overline{3}$, 4 uses) — together *more* frequent than
the complement sense. That is not an argument against matching it. We are not
designing the notation, we are preparing students for it, and reading the
overline in context is part of what they have to be able to do.

**This is now applied to the English source as well**, not just the Mongolian.
The notation argument does not depend on the prose language: the English ЭШ
lesson teaches the same students sitting the same exam. So
`data/genmath/esh/sets-and-operations.json` moved to the overline in the same
change — 23 strings, no other edit, `check[]` untouched. There is no EN/MN
divergence.

### 2. The empty set is $\emptyset$

The bank writes `\emptyset`. The English source writes `\varnothing`. Same
symbol family, and the bank's spelling is free to adopt.

### 3. «олоорой», not «ол»

Lesson 1 was drafted with the bare imperative «ол», and I flagged that it
conflicts with the «та» ruling. **I went and counted.** Across the 54 papers:

| form | count |
|---|---|
| «олоорой» (polite) | 383 |
| «ол» (bare) | 352 |
| «бичээрэй» (polite) | 36 |
| «бич» (bare) | 17 |

The polite imperative is not a concession to register — it is *the more common
form on the real exam*, and decisively so for «бич». That resolves the conflict
instead of deferring it: «олоорой» satisfies the «та» ruling and matches exam
convention at the same time, so there is nothing left to trade off. Lesson 1 is
changed to match, and this topic uses the polite imperative throughout.

If you would rather have the bare form, it is one substitution across the topic
and no other wording moves — but I could not find an argument for it once the
counts came back this way.

---

## Topic-level strings

**TITLE:** Олонлог ба үйлдэл

**BLURB:** Олонлогийн тэмдэглэгээ, харьяалал ба дэд олонлог, дөрвөн үйлдэл,
дэд олонлогийн тоо, Де Морганы хууль. ЭШ-ийн олонлогийн бодлого бүхэлдээ
эдгээр дээр тогтдог бөгөөд магадлалын бүлэг ч мөн энэ хэлээр бичигдсэн.

`unit`, `status`, `buildsOn` are structural — untouched.

---

## Lesson 1 — `sets-and-membership`

**What makes this a rewrite.** The English lesson opens with a formal definition
of a set, mentions the element-vs-subset trap second, and reaches the counting
rule third. **This version reverses that**, because the students are different.
The ЭШ course assumes ~650/800 — they already know what a set is. What loses
them marks is the two-level distinction and the `+1`. So the lesson opens with
the **exam trap**, the definition arrives as a *reminder* compressed into one
paragraph where English used three, and the counting rule gets its own beat and
a name — «нэгийг нэм» — so it is drilled as a reflex rather than derived once.

**TITLE:** Олонлог, харьяалал, элементийн тоо

**COMPARISON:** Олонлог бол ангийн нэрсийн жагсаалт: нэрийг ямар дарааллаар
бичсэн нь, нэг нэр хоёр удаа бичигдсэн эсэх нь хамаагүй — хэн байгаа нь л
чухал. $\{1, 2, 3\}$ ба $\{3, 1, 2, 2\}$ бол яг нэг анги.

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

Хоосон олонлог $\emptyset$ нь ямар ч элементгүй бөгөөд **аль ч олонлогийн**
дэд олонлог болно.

Одоо оноо шууд авчирдаг дадал руу орьё: **нэгийг нэм**. $a$-аас $b$ хүртэлх
бүхэл тоонуудын тоо нь $b - a + 1$. Хоёр захыг нь хоёуланг нь тоолж байгаа тул
хасаад зогсохгүй нэгийг нэмнэ. Хурдан бодогчид яг энэ нэгэн дээр оноо алддаг —
$\{5, 6, \ldots, 20\}$ дотор $15$ биш, $16$ элемент бий.

Элементийн тоог $|A|$ (эсвэл $n(A)$) гэж тэмдэглэнэ. ЭШ-ийн хувилбарууд үүнийг
олонлогийн **чадал** гэж нэрлэдэг ба бодлогын нөхцөлд «$|X|$ — $X$ олонлогийн
чадал буюу элементийн тоо» гэсэн тайлбарыг нь өгсөн байдаг тул хоёр нэрийг
хоёуланг нь таньж байх хэрэгтэй.

**FACTS:**

1. **Харьяалал ба дэд олонлог** — $x \in A, \qquad B \subseteq A$ —
   ЭЛЕМЕНТ нь $\in$-ээр, бүхэл ОЛОНЛОГ нь $\subseteq$-ээр орно.
2. **Дараалсан бүхэл тоог тоолох** — $|\{a, a+1, \ldots, b\}| = b - a + 1$ —
   Хоёр захыг нь оруулж тоолохдоо хасаад дараа нь нэгийг нэмнэ.

**MISTAKES:**

- $\{2\} \in \{2, 4\}$ гэж бичих. «$2$ нь олонлогт байгаа» гэдэг үнэн боловч
  тэр нь $2 \in \{2, 4\}$ гэсэн үг. $\{2\}$ бол олонлог тул $\subseteq$ хэрэглэнэ.
- $\{5, 6, \ldots, 20\}$-ийг $20 - 5 = 15$ элементтэй гэж тоолох. Хоёр захыг нь
  оруулж тоолж байгаа тул $20 - 5 + 1 = 16$ болно.

**WORKED esh-sets-l1-we1:**

- **PROBLEM:** $A = \{x \in \mathbb{Z} : -2 \le x < 4\}$ олонлогийн элементүүдийг
  жагсааж, $|A|$-г олоорой.
- **WORKING:** Нөхцөл нь $-2$-оос эхэлж, $4$-ийг оруулахгүй тул хамгийн их
  элемент нь $3$. Иймд $A = \{-2, -1, 0, 1, 2, 3\}$. Тоолохдоо нэгийг нэмэх
  дүрмээр: $3 - (-2) + 1 = 6$.
- **ANSWER:** $|A| = 6$

**WORKED esh-sets-l1-we2:**

- **PROBLEM:** $50$-аас бага, $3$-т хуваагддаг натурал тоо хэд байх вэ? Эхлээд
  олонлогийг нөхцөлөөр бичээрэй.
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

### Interactive — same nine steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Хоёр түвшин · **title** Элемент үү, дэд олонлог уу?<br>**body** $\in$ нэг элементийн тухай, $\subseteq$ бүхэл олонлогийн тухай өгүүлнэ. $2 \in \{2, 4\}$ ба $\{2\} \subseteq \{2, 4\}$ хоёулаа үнэн, харин $\{2\} \in \{2, 4\}$ худал — шалгалт яг үүнийг санал болгодог. |
| 1 | teach | **eyebrow** Хэлний дүрэм · **title** Нэрсийн жагсаалт, дараалал биш<br>**body** Олонлог зөвхөн харьяалалд ач холбогдол өгнө. $\{1, 2, 3\}$, $\{3, 2, 1\}$, $\{1, 1, 2, 3\}$ гурав нь нэг ижил олонлог — дараалал ба давталтыг тооцохгүй. |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Аль нь үнэн бэ?<br>**prompt** $A = \{1, \{2\}, 3\}$ бол аль нь ҮНЭН вэ?<br>**options** `$\{2\} \in A$` · `$2 \in A$` · `$\{1, 2\} \subseteq A$` · `$|A| = 2$` — **correctIndex 0**<br>**explanation** $A$-гийн элементүүд нь $1$, $\{2\}$ гэсэн ОЛОНЛОГ, ба $3$. Тиймээс $\{2\} \in A$ үнэн, харин $2$ гэсэн тоо өөрөө элемент биш. $\|A\| = 3$. |
| 3 | worked | **title** Нөхцөлөөс жагсаалт руу — `esh-sets-l1-we1` |
| 4 | worked | **title** Хуваагдах тоо тоолох — `esh-sets-l1-we2` |
| 5 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Нэгийг нэмэх дадал<br>**prompt** $-4 \le x \le 9$ нөхцөлийг хангах бүхэл тоо хэд вэ?<br>**options** `$13$` · `$14$` · `$12$` · `$9$` — **correctIndex 1**<br>**explanation** Хоёр захыг нь оруулж тоолно: $9 - (-4) + 1 = 14$. Нэгийг нэмэхээ мартвал $13$ гэсэн сонирхол татам буруу хариу гарна. |
| 6 | tryIt | **title** Нэг тал нь хатуу — `esh-sets-l1-t1` |
| 7 | tryIt | **title** Хоёр оронтой хуваагдагч — `esh-sets-l1-t2` |
| 8 | recap | **title** Санаж үлдэх зүйл<br>**points** Олонлогийг зөвхөн харьяалал тодорхойлно — дараалал ч, давталт ч биш · $\in$ элементэд, $\subseteq$ олонлогт; $\emptyset$ нь бүх олонлогийн дэд олонлог · $a$-аас $b$ хүртэл: $b - a + 1$ |

---

## Lesson 2 — `union-intersection-difference`

**What makes this a rewrite.** The English organises the lesson around four
verbs — or, and, but-not, everything-else — and tells the student to translate
the sentence into an operation. That is a fine lesson for a first meeting, but
it is not what the ЭШ paper asks. The real item (Test-2A Q34, hard tier) reads:

> «$A$ ба $B$ нь $U$ олонлогийн дэд олонлогууд. $|U| = 30$, $|A \cup B| = 21$,
> $|A \setminus B| = 10$, $|B \setminus A| = 5$ бол $|B \cap A| = ?$»

and its own published solution is
$|A \cup B| = |A \setminus B| + |B \setminus A| + |A \cap B|$. The exam gives you
region counts and asks for a region count. So **this version is organised around
the four disjoint regions**, and the four operations arrive second, as names for
sums of regions. The region formula is promoted to a stated fact — the English
does not have it at all — because it is literally what the marker's solution
uses, and because a student who thinks in regions cannot double-count.

**TITLE:** Нэгдэл, огтлолцол, ялгавар, гүйцээлт

**COMPARISON:** Сургуулийн хоёр дугуйлан: нэгдэл нь ядаж нэгэнд нь бүртгүүлсэн
бүх хүүхэд, огтлолцол нь хоёуланд нь явдаг хүүхдүүд, ялгавар нь нэг
дугуйлангаас давхар явагчдыг хассан нь, гүйцээлт нь аль алинд нь ороогүй
үлдсэн бүх хүүхэд.

**OBJECTIVE:** $A \cup B$, $A \cap B$, $A \setminus B$, $\overline{A}$-г
тодорхой олонлогууд дээр олох, өгүүлбэрээр бичсэн нөхцөлийг зөв үйлдэл болгон
хөрвүүлэх, мужийн тоог хооронд нь гаргаж авах.

**KEY IDEA:** Хоёр олонлог $U$-г огтлолцолгүй дөрвөн мужид хуваана: зөвхөн $A$,
хоёулаа, зөвхөн $B$, аль нь ч биш. Асуултын хариу бүр эдгээр мужуудын нийлбэр.

**TEACHING:**

Хоёр олонлогийн бодлогыг бүгдийг нь нэг зурагт багтааж болно. $U$ доторх
аливаа элемент дараах дөрвөн мужийн яг **нэгэнд** нь харьяална: зөвхөн $A$-д
($A \setminus B$), хоёуланд нь ($A \cap B$), зөвхөн $B$-д ($B \setminus A$),
аль алинд нь үгүй ($\overline{A \cup B}$). Дөрвөн муж давхцахгүй тул тоонууд нь
$|U|$ болж нийлнэ. ЭШ-ийн бодлогод ихэвчлэн эдгээрийн хоёр гурвыг өгөөд
үлдсэнийг нь асуудаг.

Нэрлэвэл: **нэгдэл** $A \cup B$ нь ядаж нэгэнд нь байгаа бүх элемент буюу
эхний гурван муж. **Огтлолцол** $A \cap B$ нь хоёуланд нь байгаа нь буюу дунд
муж. **Ялгавар** $A \setminus B$ нь $A$-д байгаа боловч $B$-д байхгүй нь; энэ
нь тэгш хэмтэй биш тул $A \setminus B$ ба $B \setminus A$ хоёр өөр муж.
**Гүйцээлт** $\overline{A} = U \setminus A$ нь $A$-д ороогүй бүх зүйл, иймд
$|\overline{A}| = |U| - |A|$. Огтлолцол нь хоосон бол ($A \cap B = \emptyset$)
хоёр олонлогийг огтлолцолгүй гэнэ.

Мужаар бодох нь томьёо цээжлэхээс найдвартай:
$|A \cup B| = |A \setminus B| + |A \cap B| + |B \setminus A|$ гэдэг нь зүгээр л
гурван мужийг нэмж байгаа хэрэг бөгөөд давхар тоолох алдаа гарах газаргүй.
Өгүүлбэрийг мужид буулгаж сурах нь чухал: «эсвэл» нь нэгдэл, «ба» нь
огтлолцол, «... боловч ... биш» нь ялгавар, «аль нь ч биш» нь гүйцээлт.

**FACTS:**

1. **Дөрвөн үйлдэл** —
   $A \cup B,\quad A \cap B,\quad A \setminus B,\quad \overline{A} = U \setminus A$ —
   Эсвэл, ба, боловч-биш, үлдсэн бүх зүйл: үг тус бүр өөрийн үйлдлээ заана.
2. **Мужийн нийлбэр** —
   $|A \cup B| = |A \setminus B| + |A \cap B| + |B \setminus A|$ —
   Огтлолцолгүй гурван мужийг нэмнэ; ЭШ-ийн бодолт яг үүнийг хэрэглэдэг.

**MISTAKES:**

- $|A \cup B|$-г $|A| + |B|$ гэж бодох. Ингэвэл дунд мужийг хоёр удаа тоолно.
  Мужаар нэмэх, эсвэл $|A| + |B| - |A \cap B|$ гэж бичих нь зөв — дараагийн
  бүлэгт үүнийг бүрэн томьёо болгоно.
- $A \setminus B$ ба $B \setminus A$-г ижил гэж үзэх. Ялгавар чиглэлтэй:
  $\{1,2,3\} \setminus \{3\} = \{1,2\}$ боловч
  $\{3\} \setminus \{1,2,3\} = \emptyset$. Зурагт эдгээр нь зүүн ба баруун
  талын өөр өөр муж.

**WORKED esh-sets-l2-we1:**

- **PROBLEM:** $A = \{1, 2, 3, 4, 5, 6\}$, $B = \{4, 5, 6, 7, 8\}$ бол
  $|A \cup B|$, $|A \cap B|$, $|A \setminus B|$-г олоорой.
- **WORKING:** Дунд муж: $A \cap B = \{4, 5, 6\}$, иймд $|A \cap B| = 3$.
  Зөвхөн $A$: $A \setminus B = \{1, 2, 3\}$ буюу $6 - 3 = 3$. Зөвхөн $B$:
  $\{7, 8\}$ буюу $5 - 3 = 2$. Гурван мужийг нэмэхэд $3 + 3 + 2 = 8$. Хэрэв
  $|A| + |B| - |A \cap B| = 6 + 5 - 3 = 8$ гэж бодвол мөн ижил хариу — дунд
  мужийг нэг л удаа тоолсны хэрэг.
- **ANSWER:** $|A \cup B| = 8$, $|A \cap B| = 3$, $|A \setminus B| = 3$

**WORKED esh-sets-l2-we2:**

- **PROBLEM:** $U = \{1, 2, \ldots, 30\}$ бөгөөд $E$ нь $2$-т, $T$ нь $3$-т
  хуваагдах тоонуудын олонлог. $3$-т хуваагдахгүй тэгш тоо хэд байх вэ?
- **WORKING:** $|E| = 15$. Хоёуланд нь хуваагдана гэдэг нь $6$-д хуваагдана
  гэсэн үг тул $|E \cap T| = 5$. Асуулт зөвхөн $E$-ийн мужийг хайж байна:
  $|E \setminus T| = 15 - 5 = 10$.
- **ANSWER:** $10$

**TRY esh-sets-l2-t1:**

- **PROBLEM:** $A = \{2, 4, 6, 8, 10, 12\}$, $B = \{3, 6, 9, 12\}$ бол
  $|A \cap B|$ ба $|A \cup B|$-г олоорой.
- **ANSWER:** $|A \cap B| = 2$, $|A \cup B| = 8$
- **WORKING:** Хоёуланд нь байгаа нь $6$ ба $12$ тул $|A \cap B| = 2$. Иймд
  $|A \cup B| = 6 + 4 - 2 = 8$.

**TRY esh-sets-l2-t2:**

- **PROBLEM:** $U = \{1, \ldots, 40\}$ дотор $5$-д хуваагддаггүй тоо хэд байх вэ?
- **ANSWER:** $32$
- **WORKING:** $5$-д хуваагддаг нь $8$ ширхэг. Гүйцээлт: $40 - 8 = 32$.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Дөрвөн муж · **title** Нэг зураг, дөрвөн муж<br>**body** $U$ доторх элемент бүр яг нэг мужид харьяална: зөвхөн $A$, хоёулаа, зөвхөн $B$, аль нь ч биш. Нэгдэл нь эхний гурав, огтлолцол нь дунд нь, ялгавар нь зөвхөн $A$, гүйцээлт нь үлдсэн нь. Үйлдэл цээжлэхийн оронд мужаа тоолоорой. |
| 1 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Үйлдлээ сонгоорой<br>**prompt** «Физик үздэг боловч хими үздэггүй сурагчид» гэдэг аль олонлог вэ?<br>**options** `$P \setminus C$` · `$P \cap C$` · `$P \cup C$` · `$C \setminus P$` — **correctIndex 0**<br>**explanation** «Боловч ... биш» гэдэг нь ялгавар бөгөөд ФИЗИКЭЭС хасч байна: $P \setminus C$. Чиглэл чухал — $C \setminus P$ бол хими үздэг атлаа физик үздэггүй сурагчид, өөр муж. |
| 2 | worked | **title** Гурван тоог нэг зурагнаас — `esh-sets-l2-we1` |
| 3 | worked | **title** Тэгш боловч гуравт хуваагдахгүй — `esh-sets-l2-we2` |
| 4 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Огтлолцолгүй эсэх<br>**prompt** $A$ нь сондгой тоонууд, $B$ нь $4$-т хуваагдах тоонууд. $A \cap B$ юу вэ?<br>**options** `$\emptyset$` · `$\{4\}$` · `$4$-т хуваагддаг сондгой тоонууд` · `$A$` — **correctIndex 0**<br>**explanation** $4$-т хуваагддаг тоо бүр тэгш тул сондгой тоо $B$-д орох боломжгүй. Хоёр олонлог огтлолцолгүй бөгөөд огтлолцол нь хоосон. |
| 5 | tryIt | **title** Эхлээд огтлолцол, дараа нь нэгдэл — `esh-sets-l2-t1` |
| 6 | tryIt | **title** Гүйцээлтээр тоол — `esh-sets-l2-t2` |
| 7 | recap | **title** Санаж үлдэх зүйл<br>**points** Дөрвөн муж: зөвхөн $A$, хоёулаа, зөвхөн $B$, аль нь ч биш — бүх тоо эдгээрийн нийлбэр · $\cup$ эсвэл, $\cap$ ба, $\setminus$ боловч-биш (чиглэлтэй!), $\overline{A}$ үлдсэн бүх зүйл · $\|\overline{A}\| = \|U\| - \|A\|$ — хэцүү тоололтыг хасалт болгоно |

---

## Lesson 3 — `subsets-and-power-sets`

**What makes this a rewrite.** The English teaches the switchboard picture and
then counts forwards: given $n$, find $2^n$. **The ЭШ bank almost never asks it
that way.** Two real items:

> «$n$ элементтэй $A$ олонлогийн $n - 2$ элементтэй дэд олонлогийн тоо 28 бол
> $A$-ийн дэд олонлогийн тоог ол.» → $n = 8$, хариу $2^8 = 256$

> «Нэг олонлог $63$ жинхэнэ дэд олонлогтой бол хэдэн элементтэй вэ?» → $n = 6$

Both run **backwards**: you are handed a count and asked for $n$. So the forward
rule is stated quickly here and the second concept paragraph is given over to
reading it in reverse, including the memorise-your-powers-of-two advice that
actually saves seconds in the hall. The fun-fact step, which in English is a
note about $2^0 = 1$, is replaced by the $\binom{n}{n-2} = \binom{n}{2}$ route
the first item above needs — a real exam shape rather than an aside.

**TITLE:** Дэд олонлогийн тоог олох

**COMPARISON:** Таван сурах бичгээс цүнхэндээ юу хийхээ сонгож байна гэж
төсөөлье. Ном тус бүр дээр «авах уу, үгүй юу» гэсэн хоёрхон хариулт. Таван унтраалга
$2^5 = 32$ өөр цүнх өгнө — юу ч аваагүй хоосон цүнх ч нэг хувилбар. Дэд
олонлог тоолох гэдэг унтраалга тоолохтой яг адил.

**OBJECTIVE:** Бүх дэд олонлог, жинхэнэ дэд олонлог, тодорхой элемент агуулсан
буюу агуулаагүй дэд олонлогийн тоог олох, мөн тоог нь мэдээд элементийн тоог
буцааж олох.

**KEY IDEA:** Дэд олонлог гэдэг унтраалганы хослол: нийт $2^n$. Нөхцөл бүр нэг
унтраалгыг тогтоох тул хариу нь үргэлж $2^{\text{чөлөөт}}$. ЭШ ихэвчлэн үүнийг
урвуугаар асууна.

**TEACHING:**

$n$ элементтэй олонлогийн дэд олонлог бүр нь «элемент бүрийг авах уу, үгүй юу»
гэсэн $n$ ширхэг бие даасан сонголтоор тодорхойлогдоно. Иймд нийт $2^n$ дэд
олонлог байна. Энэ тоонд хоосон олонлог $\emptyset$ (бүх унтраалга унтарсан) ба
олонлог өөрөө (бүгд асаастай) хоёулаа орно.

ЭШ-д энэ дүрэм ихэвчлэн **урвуугаар** ирдэг: «нэг олонлог $63$ жинхэнэ дэд
олонлогтой бол хэдэн элементтэй вэ?» Ийм үед $2^n$ хүртэл нь нөхөж бодно —
$63 + 1 = 64 = 2^6$, иймд $n = 6$. Хоёрын зэргүүдийг $2^{10} = 1024$ хүртэл
цээжээр мэдэж байвал энэ төрлийн бодлого хормын дотор бодогдоно.

Нэр томьёо ба нөхцөл. **Жинхэнэ дэд олонлог** нь олонлог өөрөө орохгүй тул
$2^n - 1$; зарим бодлого дээр хоосон олонлогийг мөн хасдаг тул нөхцөлөө
анхааралтай уншина. Тодорхой элементийг заавал агуулах ёстой бол тэр
унтраалгыг асаалттай тогтооно — үлдсэн $n-1$ нь чөлөөтэй тул $2^{n-1}$.
Агуулахгүй байх ёстой бол унтраалгыг унтраана — мөн л $2^{n-1}$. Тогтоосон
унтраалгаа тоолоод, чөлөөтэй үлдсэнийг нь зэрэгт өргөнө.

**FACTS:**

1. **Дэд олонлогийн тоо** —
   $\#\{\text{дэд олонлог}\} = 2^n$ —
   Элемент бүр дээр авах/авахгүй; хоосон олонлог ба олонлог өөрөө хоёул
   тоологдоно.
2. **Тогтоосон элемент** —
   $\#\{S : a \in S\} = 2^{n-1}$ —
   Нэг элементийг албадан оруулах (эсвэл гаргах) нь нэг чөлөөт сонголтыг
   устгах тул тоо яг хоёр дахин багасна.

**MISTAKES:**

- $\emptyset$ ба олонлог өөрөө дэд олонлог болохыг мартах. Хоёул $2^n$ дотор
  тоологдоно. Зөвхөн «жинхэнэ» (мөн нөхцөлд заасан бол «хоосон биш») гэсэн үг
  тэдгээрийг хасна.
- $a$-г агуулсан дэд олонлогийн тоог $2^n - 1$ гэж бодох. $a$-г тогтоовол
  $n-1$ элемент чөлөөтэй үлдэнэ: $2^{n-1}$ буюу яг хагас. $a$ нь бүх дэд
  олонлогийн яг хагаст нь байдаг тул үүнээс өөр байх боломжгүй.

**WORKED esh-sets-l3-we1:**

- **PROBLEM:** $6$ элементтэй олонлог хэдэн дэд олонлогтой вэ? Тэдгээрийн хэд
  нь жинхэнэ дэд олонлог вэ?
- **WORKING:** Нийт: $2^6 = 64$. Жинхэнэ дэд олонлогт олонлог өөрөө орохгүй:
  $64 - 1 = 63$.
- **ANSWER:** $64$ ба $63$

**WORKED esh-sets-l3-we2:**

- **PROBLEM:** $\{1, 2, 3, 4, 5, 6, 7\}$-ийн хэдэн дэд олонлог $1$ ба $2$-ыг
  хоёуланг нь агуулах вэ?
- **WORKING:** $1$ ба $2$-ын унтраалгыг асаалттай тогтооно; үлдсэн таван
  элемент чөлөөтэй: $2^{7-2} = 2^5 = 32$.
- **ANSWER:** $32$

**TRY esh-sets-l3-t1:**

- **PROBLEM:** $|A| = 8$ бол $A$ хэдэн хоосон биш жинхэнэ дэд олонлогтой вэ?
- **ANSWER:** $254$
- **WORKING:** Нийт $2^8 = 256$. $\emptyset$ ба $A$ өөрийг нь хасна:
  $256 - 2 = 254$.

**TRY esh-sets-l3-t2:**

- **PROBLEM:** $6$ элементтэй олонлогийн хэдэн дэд олонлог нь сонгосон $a$
  элементийг агуулж, сонгосон $b$ элементийг агуулахгүй вэ?
- **ANSWER:** $16$
- **WORKING:** $a$ асаалттай, $b$ унтраалттай тогтсон — дөрвөн элемент
  чөлөөтэй: $2^4 = 16$.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Унтраалганы самбар · **title** $n$ элемент, $n$ унтраалга<br>**body** Дэд олонлог зохиох гэдэг элементийн жагсаалтыг дагаж явахдаа «авах/авахгүй» гэсэн унтраалга дарж байгаа хэрэг. $n$ бие даасан унтраалга, $2^n$ үр дүн. Энэ бүлгийн бүх бодлого энэ нэг зурагт багтана. |
| 1 | worked | **title** Нийт ба жинхэнэ — `esh-sets-l3-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Яг хагас<br>**prompt** $n$ элементтэй олонлогийн бүх дэд олонлогийн хэдэн хувь нь тогтоосон $a$ элементийг агуулах вэ?<br>**options** `яг хагас нь` · `$1/n$ нь` · `$n$-ээс хамаарна` · `нэгээс бусад бүгд` — **correctIndex 0**<br>**explanation** Дэд олонлог бүрийг $a$-г нь эсрэгээр нь сольсон хувилбартай нь хослуулбал хос тутмын яг нэг нь $a$-г агуулна. Иймд яг хагас — $2^n$-ийн $2^{n-1}$. |
| 3 | worked | **title** Хоёр тогтоосон унтраалга — `esh-sets-l3-we2` |
| 4 | tryIt | **title** Хоосон биш, жинхэнэ — `esh-sets-l3-t1` |
| 5 | tryIt | **title** Нэг нь дотор, нэг нь гадна — `esh-sets-l3-t2` |
| 6 | funFact | **eyebrow** Сонирхолтой баримт · **title** ЭШ энэ дүрмийг урвуугаар асуудаг<br>**body** Жинхэнэ ЭШ-ийн хувилбарт «$n$ элементтэй $A$ олонлогийн $n-2$ элементтэй дэд олонлогийн тоо $28$ бол $A$-ийн дэд олонлогийн тоог ол» гэсэн бодлого гарч байсан. $n-2$ элемент СОНГОНО гэдэг нь хаях хоёр элементээ сонгохтой адил тул $\binom{n}{n-2} = \binom{n}{2} = 28$, эндээс $n = 8$ ба хариу нь $2^8 = 256$. Урвуу асуулт нь ижил дүрэм, зөвхөн нөгөө талаасаа. |
| 7 | recap | **title** Санаж үлдэх зүйл<br>**points** $2^n$ дэд олонлог; $2^n - 1$ жинхэнэ; $2^n - 2$ хоосон биш жинхэнэ · Тогтоосон элемент бүр тоог хоёр дахин багасгана: $2^{\text{чөлөөт}}$ · Нөхцөлөө уншина: «жинхэнэ» ба «хоосон биш» гэсэн үг тус бүр хариуг нэгээр өөрчилнө |

---

## Lesson 4 — `set-identities`

**What makes this a rewrite.** The English leads with the laws and reaches their
use in the third paragraph. Here the order is inverted, because on the ЭШ paper
the laws are never the question — the question is a sentence, and the marks are
lost in reading it. So this version leads with the **three sentences the exam
actually writes** («аль нь ч биш», «хоёулаа биш», «дор хаяж нэг нь»), maps each
to a count, and then introduces De Morgan as the reason the mapping is legal.
The distributive laws stay third, as in English, since they are genuinely the
tail of the lesson.

Worked example 2 also gains a sentence the English does not have: it points out
that the $18$ in the stem is **never used**. Planting an unused number is a
standard ЭШ move and noticing it is a transferable skill.

**TITLE:** Де Морганы хууль ба олонлогийн алгебр

**COMPARISON:** «Хямд БА хурдан» гэдгийг үгүйсгэвэл «үнэтэй ЭСВЭЛ удаан» болно
— үгүйсгэл дотогшоо тарж, холбоос нь эргэдэг. Де Морганы хууль бол яг энэ өдөр
тутмын үгүйсгэлийг олонлогийн хэлээр бичсэн нь.

**OBJECTIVE:** «Аль нь ч биш», «хоёулаа биш», «дор хаяж нэг нь» гэсэн ЭШ-ийн
нөхцөлүүдийг тоолж болох олонлог болгон хөрвүүлэх, Де Морган ба хуваарилах
хуулиудыг хэрэглэх.

**KEY IDEA:** «Аль нь ч биш» $= |U| - |A \cup B|$, «хоёулаа биш»
$= |U| - |A \cap B|$. Гүйцээлт нь $\cup$ ба $\cap$-г солино — энэ л Де Морган.

**TEACHING:**

ЭШ-ийн олонлогийн бодлогод хамгийн олон тохиолддог гурван өгүүлбэр бий,
тэдгээрийг андуурвал бүх тооцоо буруу явна. **«Аль нь ч биш»** — хоёуланд нь
ороогүй, өөрөөр хэлбэл $\overline{A \cup B}$, тоо нь $|U| - |A \cup B|$.
**«Хоёулаа биш»** — ядаж нэгэнд нь ороогүй, өөрөөр хэлбэл
$\overline{A \cap B}$, тоо нь $|U| - |A \cap B|$. **«Дор хаяж нэг нь»** —
энгийн нэгдэл $A \cup B$. Эхний хоёр нь ойролцоо сонсогддог ч яг нэг мужаар,
нэг л талд нь байгаа элементүүдээр ялгаатай.

«Аль нь ч биш» яагаад $\overline{A} \cap \overline{B}$ болохыг **Де Морганы
хууль** тайлбарлана: $\overline{A \cup B} = \overline{A} \cap \overline{B}$ ба
$\overline{A \cap B} = \overline{A} \cup \overline{B}$. Гүйцээлт хаалтыг
задлаад холбоосыг эсрэгээр нь эргүүлнэ. Үгээр хэлбэл: «аль нэгэнд нь БАЙХГҮЙ»
гэдэг нь «хоёуланд нь ч байхгүй»; «хоёуланд нь БАЙХГҮЙ» гэдэг нь «ядаж нэгэнд
нь байхгүй».

**Хуваарилах хууль** нь арифметикийн адилтгалыг давтана:
$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$. Хоёр дахь хэлбэр нь
$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$ — арифметикт ийм зүйл
байдаггүй тул буруу мэт санагддаг бөгөөд яг тийм учраас шалгалтад тавигддаг.
Эргэлзвэл гурван дугуйтай Венн диаграмм зурж мужаа шалгах нь хамгийн
найдвартай.

**FACTS:**

1. **Де Морганы хууль** —
   $\overline{A \cup B} = \overline{A} \cap \overline{B}, \qquad \overline{A \cap B} = \overline{A} \cup \overline{B}$ —
   Гүйцээлтийн зураас хаалт дээр тасарч, үйлдлээ эргүүлнэ.
2. **«Аль нь ч биш»-ийн тоо** —
   $|\overline{A \cup B}| = |U| - |A \cup B|$ —
   Нэгдлээ мэдмэгц нэг хасалт л үлдэнэ.

**MISTAKES:**

- Гүйцээлтийг задлахдаа үйлдлээ эргүүлэхгүй байх, өөрөөр хэлбэл
  $\overline{A \cup B} = \overline{A} \cup \overline{B}$ гэж бичих. Үйлдэл
  эргэнэ: $\overline{A \cup B} = \overline{A} \cap \overline{B}$. Жижиг
  жишээгээр шалгаж болно — $U = \{1,2\}$, $A = \{1\}$, $B = \{2\}$ гэвэл
  эргүүлээгүй хувилбар нурна.
- «Хоёулаа биш»-ийг «аль нь ч биш» гэж унших. «Хоёулаа биш» бол
  $\overline{A \cap B}$ — ядаж нэгэнд нь алга. «Аль нь ч биш» бол
  $\overline{A \cup B}$ — хоёуланд нь алга. Ялгаа нь яг нэг талд нь байгаа бүх
  элемент.

**WORKED esh-sets-l4-we1:**

- **PROBLEM:** $U = \{1, \ldots, 20\}$ бөгөөд $A$ нь $4$-т, $B$ нь $5$-д
  хуваагдах тоонуудын олонлог. $|\overline{A \cup B}|$ ба
  $|\overline{A} \cap \overline{B}|$-г тус тусад нь тоолж Де Морганыг
  шалгаарай.
- **WORKING:** $|A| = 5$, $|B| = 4$, $A \cap B$ нь $20$-д хуваагдах тоонууд
  тул $|A \cap B| = 1$. Иймд $|A \cup B| = 5 + 4 - 1 = 8$, эндээс
  $|\overline{A \cup B}| = 20 - 8 = 12$. Нөгөө талаас
  $\overline{A} \cap \overline{B}$ гэдэг нь $4$-т ч, $5$-д ч хуваагдахгүй
  тоонууд — тэдгээрийг шууд тоолоход мөн $12$ гарна. Хоёр зам ижил хариу
  өгсөн нь Де Морганы амласан зүйл.
- **ANSWER:** Хоёулаа $12$

**WORKED esh-sets-l4-we2:**

- **PROBLEM:** $32$ сурагчийн $18$ нь алгебрт тэнцжээ. Алгебр, геометрийн аль
  алинд нь тэнцээгүй сурагч $6$ байв. Дор хаяж нэг хичээлд тэнцсэн сурагч хэд
  байх вэ?
- **WORKING:** «Аль алинд нь тэнцээгүй» гэдэг нь Де Морганаар
  $\overline{A \cup G}$. Иймд $|A \cup G| = 32 - 6 = 26$. Анхаараарай: $18$
  гэсэн тоо энд огт хэрэггүй — асуулт зөвхөн гүйцээлтээс шалтгаалж байна. ЭШ
  ийм илүүц тоог зориуд тавьдаг.
- **ANSWER:** $26$

**TRY esh-sets-l4-t1:**

- **PROBLEM:** $|U| = 50$, $|A| = 23$, $|B| = 19$, $|A \cap B| = 8$ бол
  $|\overline{A} \cap \overline{B}|$-г олоорой.
- **ANSWER:** $16$
- **WORKING:** $|A \cup B| = 23 + 19 - 8 = 34$. Де Морганаар зорилтот олонлог
  маань $\overline{A \cup B}$ болох тул $50 - 34 = 16$.

**TRY esh-sets-l4-t2:**

- **PROBLEM:** Мөнөөх өгөгдлөөр $\overline{A} \cup \overline{B}$ хэдэн
  элементтэй вэ?
- **ANSWER:** $42$
- **WORKING:** Де Морган: $\overline{A} \cup \overline{B} = \overline{A \cap B}$,
  иймд $50 - 8 = 42$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Эргэлт · **title** Үгүйсгэл хаалтыг задалж, үйлдлийг эргүүлнэ<br>**body** «$A$ эсвэл $B$-д байгаа» гэдгийг үгүйсгэвэл «$A$-д ч, $B$-д ч байхгүй» болно. «Хоёуланд нь байгаа» гэдгийг үгүйсгэвэл «ядаж нэгэнд нь байхгүй» болно. Де Морганы бүх агуулга энэ хоёр өгүүлбэрт багтана — тэмдэглэгээ нь зүгээр л үүнийг бичиж авдаг. |
| 1 | worked | **title** Де Морганыг тоолж шалгах — `esh-sets-l4-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Аль нь ч биш үү, хоёулаа биш үү?<br>**prompt** $\|U\| = 40$, $\|A \cap B\| = 9$. Хоёуланд нь БАЙХГҮЙ элемент хэд вэ?<br>**options** `$31$` · `$9$` · `$40 - \|A \cup B\|$` · `Тодорхойлох боломжгүй` — **correctIndex 0**<br>**explanation** «Хоёуланд нь байхгүй» гэдэг нь огтлолцлын гүйцээлт: $40 - 9 = 31$. («Аль нь ч биш» байсан бол нэгдэл хэрэгтэй болно — өөр асуулт.) |
| 3 | worked | **title** Аль алинд нь тэнцээгүй — `esh-sets-l4-we2` |
| 4 | tryIt | **title** Аль нь ч биш — Де Морганаар — `esh-sets-l4-t1` |
| 5 | tryIt | **title** Ядаж нэгэнд нь алга — `esh-sets-l4-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** $\overline{A \cup B} = \overline{A} \cap \overline{B}$, $\overline{A \cap B} = \overline{A} \cup \overline{B}$ · «Аль нь ч биш» $= \|U\| - \|A \cup B\|$; «хоёулаа биш» $= \|U\| - \|A \cap B\|$ · Гүйцээлт хэцүү санагдвал Де Морганаар хасалт болгон хувиргана |

---

## Practice — ten items, same ids, same `check[]`

**esh-sets-p1** — $A = \{x \in \mathbb{Z} : x^2 < 10\}$ олонлогийн элементүүдийг
бичээд $|A|$-г олоорой.
> Квадрат нь $10$-аас бага бүхэл тоонууд:
$\{-3, -2, -1, 0, 1, 2, 3\}$. ($4^2 = 16 > 10$ тул $\pm 4$ орохгүй.) Тоолоход
$3 - (-3) + 1 = 7$, иймд $|A| = 7$.

**esh-sets-p2** — $1$-ээс $100$ хүртэлх (хоёр захыг нь оруулаад) бүхэл тооны
дотор $6$-д хуваагддаг нь хэд вэ?
> $6$-аас $96 = 6 \cdot 16$ хүртэл: $\lfloor 100/6 \rfloor = 16$.

**esh-sets-p3** — $A = \{1,3,5,7,9,11\}$, $B = \{3,6,9,12\}$ бол $|A \cup B|$
ба $|B \setminus A|$-г олоорой.
> $A \cap B = \{3, 9\}$ тул $|A \cup B| = 6 + 4 - 2 = 8$. Зөвхөн
$B$-ийн муж: $|B \setminus A| = 4 - 2 = 2$.

**esh-sets-p4** — Нэг олонлогийн дэд олонлогийн тоо $2^n = 128$ байв. $n$-ийг
болон хоосон биш дэд олонлогийн тоог олоорой.
> $2^7 = 128$ тул $n = 7$. Хоосон биш: $128 - 1 = 127$.

**esh-sets-p5** — $\{a, b, c, d, e\}$-ийн хэдэн дэд олонлог $a$ эсвэл $b$-г
(ядаж нэгийг нь) агуулах вэ?
> Гүйцээлтээр тоолох нь хялбар: $a$-г ч, $b$-г ч агуулаагүй дэд
олонлогууд нь үлдсэн гурван элементийн дэд олонлогууд — $2^3 = 8$. Иймд
$2^5 - 8 = 32 - 8 = 24$.

**esh-sets-p6** — $U = \{1, \ldots, 60\}$ дотор $4$-т ч, $6$-д ч
хуваагддаггүй тоо хэд вэ?
> $|A| = 15$, $|B| = 10$. Хоёуланд нь хуваагдана гэдэг нь
$\mathrm{lcm}(4,6) = 12$-д хуваагдана гэсэн үг тул $|A \cap B| = 5$. Нэгдэл:
$15 + 10 - 5 = 20$; аль нь ч биш: $60 - 20 = 40$.

**esh-sets-p7** — $A = \{2, \{3\}\}$ бол дараах өгүүлбэрүүдээс хэд нь үнэн бэ?
(i) $3 \in A$; (ii) $\{3\} \in A$; (iii) $\{\{3\}\} \subseteq A$.
> (i) худал — $A$-ийн элементүүд нь $2$ ба $\{3\}$ гэсэн ОЛОНЛОГ
бөгөөд $3$ гэсэн тоо өөрөө элемент биш. (ii) үнэн. (iii) үнэн, учир нь түүний
цорын ганц элемент $\{3\}$ нь $A$-д хамаарна. Гурвын хоёр нь үнэн.

**esh-sets-p8** — $|U| = 45$, $|A| = 21$, $|B| = 17$,
$|\overline{A} \cap \overline{B}| = 15$ бол $|A \cap B|$-г олоорой.
> Де Морганаар $\overline{A} \cap \overline{B} = \overline{A \cup B}$
тул $|A \cup B| = 45 - 15 = 30$. Эндээс $|A \cap B| = 21 + 17 - 30 = 8$.

**esh-sets-p9** — $8$ элементтэй олонлогийн хэдэн дэд олонлог нь тогтоосон $a$
элементийг агуулж, $a$-аас өөр тогтоосон $b$ элементийг агуулахгүй вэ?
> Хоёр унтраалга тогтсон, зургаа нь чөлөөтэй: $2^6 = 64$.

**esh-sets-p10** — $A \subseteq B$, $|A| = 5$, $|B| = 9$ бол $|A \cup B|$,
$|A \cap B|$, $|B \setminus A|$-г олоорой.
> $A$ нь $B$-ийн дотор байгаа тул нэгдэл нь $B$ өөрөө ($9$), огтлолцол
нь $A$ өөрөө ($5$), $|B \setminus A| = 9 - 5 = 4$.

---

## Test yourself — seven items, same ids, same `check[]`

**esh-sets-q1** — $A = \{x \in \mathbb{Z} : -5 \le x < 12\}$ бол $|A|$-г
олоорой.
> $-5$-аас $11$ хүртэл: $11 - (-5) + 1 = 17$.

**esh-sets-q2** — $A = \{1,2,3,4,5\}$, $B = \{4,5,6,7\}$ бол
$|A \cup B| + |A \cap B|$-г олоорой.
> $|A \cap B| = 2$, $|A \cup B| = 5 + 4 - 2 = 7$; нийлбэр нь
$7 + 2 = 9$. Энэ нь $|A| + |B| = 5 + 4 = 9$-тэй яг тэнцүү бөгөөд санамсаргүй
зүйл биш: нэгдлээс хассан огтлолцлыг буцааж нэмж байгаа хэрэг.

**esh-sets-q3** — Нэг олонлог $63$ жинхэнэ дэд олонлогтой бол хэдэн элементтэй
вэ?
> $2^n - 1 = 63 \Rightarrow 2^n = 64 = 2^6$, иймд $n = 6$.

**esh-sets-q4** — $\{1, \ldots, 7\}$-ийн хэдэн дэд олонлог $7$ гэсэн элементийг
агуулах вэ?
> $7$-г тогтооно; зургаан сонголт чөлөөтэй: $2^6 = 64$.

**esh-sets-q5** — $U = \{1, \ldots, 100\}$ дотор $2$-т ч, $5$-д ч
хуваагддаггүй тоо хэд вэ?
> $|A| = 50$, $|B| = 20$, $10$-д хуваагддаг нь $10$. Нэгдэл
$= 50 + 20 - 10 = 60$; аль нь ч биш $= 100 - 60 = 40$.

**esh-sets-q6** — $|U| = 36$, $|A \cap B| = 7$ бол
$\overline{A} \cup \overline{B}$ хэдэн элементтэй вэ?
> Де Морган: $\overline{A} \cup \overline{B} = \overline{A \cap B}$,
иймд $36 - 7 = 29$.

**esh-sets-q7** — $B \subseteq A$, $|A| = 12$, $|A \setminus B| = 8$ бол $B$
хэдэн дэд олонлогтой вэ?
> $|B| = 12 - 8 = 4$ тул $B$-ийн дэд олонлогийн тоо $2^4 = 16$.

---

## Notes for Build

- **`check[]` changes.** Every assertion in the English source survives
  unchanged. Two lessons gain assertions, because the rewritten solution quotes
  a number the English one did not:
  - `esh-sets-l2-we1` — the region route quotes $3 + 3 + 2 = 8$ and
    $5 - 3 = 2$. Add `Eq(3 + 3 + 2, 8)` and `Eq(5 - 3, 2)`.
  - lesson 3, interactive step 6 (`funFact`) — the ЭШ item quotes
    $\binom{8}{2} = 28$ and $2^8 = 256$. A `funFact` step **may** carry a
    `check` array (`data/genmath/6/integers.json` has two that do), so add
    `check: ["Eq(binomial(8, 2), 28)", "Eq(2**8, 256)"]` rather than shipping
    an unverified numeric claim in a step that has no slot for one.
- **Notation.** $A'$ → $\overline{A}$ and `\varnothing` → `\emptyset`
  throughout, per the decision recorded at the top. Both are in the KaTeX safe
  subset. This is the only place the MN and EN JSON diverge in notation, and it
  is deliberate.
- No Cyrillic inside `$...$` anywhere above. Cyrillic that must sit in a
  formula is wrapped: `$2^{\text{чөлөөт}}$`, `$\#\{\text{дэд олонлог}\} = 2^n$`.
- The `$\|A\|$` and `$\|U\|$` forms in the step tables are escaped **for this
  markdown table only** — the JSON carries single pipes, `$|A|$`.
- No currency appears anywhere in this topic, so the ₮ rule does not bite.
- No single-asterisk emphasis anywhere; only `**bold**`.

## Notes for Khas

Ordered by how much rides on your answer.

1. **The complement notation switch ($A' \to \overline{A}$)** is settled and
   applied to both languages — you asked for what is correct rather than what
   matches, and the ЭШ papers write the complement as an overline 13 times and
   as a prime never. The English source moved with it, so nothing diverges.
   Details and the honest caveat (the exam overloads the overline) are in the
   section above. Gates re-run green after the English change.
2. **The imperative form is now «олоорой», not «ол»** — the question I flagged
   on lesson 1, now answered from the bank's own counts (383 vs 352, and 36 vs
   17 for бич). This is the one that generalises: whatever you decide holds for
   every problem statement in all 177 topics, so it is worth a moment even
   though I believe the evidence settles it.
3. **Three terms I could not ground in either source.** They are standard as
   far as I know, but the ЭШ bank never uses them and neither does А/492, so
   they are my choice and you should check them:
   - «гүйцээлт» for *complement* — the bank always writes the condition out
     («$A$-д орших боловч $B$-д орохгүй») and never names it. The word comes
     from the existing probability glossary, which you approved.
   - «жинхэнэ дэд олонлог» for *proper subset* — 0 hits.
   - «огтлолцолгүй» for *disjoint* — 0 hits; the bank writes
     $A \cap B = \emptyset$ and leaves it unnamed.
   - «хуваарилах хууль» for *distributive law* and «Де Морганы хууль» — 0 hits
     for both, though the second is just a proper name.
4. **The universal set is never named**, only used: the bank writes «$A$ ба $B$
   нь $U$ олонлогийн дэд олонлогууд». I have followed that and avoided coining
   «универсал олонлог». Confirm that reads as intended.
5. **«нэгийг нэм»** as the name for the +1 rule is mine (from lesson 1). It
   needs to be memorable enough to become a reflex — if it sounds clumsy, the
   point of naming it is lost and it should just be described.
6. **«эмх цэгцгүй цуглуулга»** for *unordered collection* is mine and I am
   least sure of it.
7. **«унтраалга»** (switch) carries lesson 3's whole metaphor. If a Mongolian
   student does not immediately picture a light switch, the lesson loses its
   spine and wants a different image.
8. Lesson 1's guest-list metaphor is now **«ангийн нэрсийн жагсаалт»** (a class
   name list) rather than a party guest list — closer to a Mongolian
   classroom. Still an invented image; yours to replace.
