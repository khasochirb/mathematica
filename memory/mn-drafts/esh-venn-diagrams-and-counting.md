# Draft — `esh/venn-diagrams-and-counting`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

Second ЭШ topic. Complete: four lessons, ten practice items, seven
test-yourself items, topic-level strings.

Terminology follows R9 (`memory/mn-rulings.md`) and the conventions in
`memory/mn-drafts/README.md` — «та» register, polite imperative «олоорой»,
complement as $\overline{A}$, empty set as $\emptyset$. Those are settled and
are not re-argued here.

**What the corpus gave this topic.** One line of a real ЭШ solution supplied
four words I would otherwise have invented:

> «$A \cap \overline{B}$ нь $A$-д орших боловч $B$-д орохгүй цэгүүдийн олонлог.
> Венн диаграммд $A$ **дугуй**гаас $B$-тэй **огтлолцох хэсэг**ийг хасч авсан
> хүрэн **муж**.» (test4a)

So: «Венн диаграмм», «дугуй» for a circle, «огтлолцох хэсэг» for the overlap,
«муж» for a region. All four are the exam's own words, not mine.

**One caveat on «муж».** It is polysemous in this very course: the ЭШ bank uses
it far more often for a function's domain and range («тодорхойлогдох муж»,
«утгын муж»). Both senses are attested, and this topic is where the diagram
sense belongs, so I have used it — but a student meets both inside the ЭШ
course and the word is doing two jobs. Flagged below rather than silently
chosen.

---

## Topic-level strings

**TITLE:** Венн диаграмм ба тоолол

**BLURB:** Хоёр олонлогийн дөрвөн муж, нэмэх–хасах зарчим хоёр чигт, гурван
олонлогийн найман муж, гурван олонлогийн томьёо. ЭШ-ийн судалгааны бодлого
бүхэлдээ эдгээр дээр тогтдог.

---

## Lesson 1 — `reading-a-two-set-venn`

**What makes this a rewrite.** The English lesson treats the diagram as one
skill: decompose a survey into four regions and count them. **The ЭШ paper
tests two.** Alongside the counting items there is a diagram-reading item —

> «Аль нь $A \cap \overline{B}$ олонлогийг дүрсэлсэн байна вэ?» (test4a)

— which gives you a set expression and four shaded pictures and asks which
picture it is. No counting at all. The English lesson never prepares for it.

So this version teaches the region ↔ expression dictionary **in both
directions**: expression → which region is shaded (for the identification
items), and region → count (for the counting items). The tap-question is
rebuilt to the exam's own «аль нь ... вэ?» shape rather than a word-matching
question, and the four regions get their set expressions attached from the
start, so the two skills are one dictionary rather than two topics.

**TITLE:** Хоёр олонлогийн Венн диаграмм: дөрвөн муж

**COMPARISON:** Тайзан дээрх хоёр гэрлийн туяа: зөвхөн зүүн туяанд, зөвхөн
баруун туяанд, хоёуланд нь, эсвэл харанхуйд. Хүн бүр яг нэг бүсэд байна —
диаграммын бүх агуулга үүгээр дуусна.

**OBJECTIVE:** Хоёр олонлогийн бодлогыг огтлолцолгүй дөрвөн муж болгон задлах,
муж бүрийг олонлогийн бичиглэлээр нэрлэх, мужийн тоо ба олонлогийн тооны
хооронд чөлөөтэй шилжих.

**KEY IDEA:** Дөрвөн муж, огтлолцлоос гадагш дүүргэнэ. Мужийн тоонууд нэмэгдэнэ;
олонлогийн тоо нь мужуудын нийлбэр. Муж бүр өөрийн бичиглэлтэй.

**TEACHING:**

Хоёр олонлогийн Венн диаграмм орчлонг огтлолцолгүй **дөрвөн муж** болгон
хуваана. Муж бүрд нэр ба бичиглэл хоёулаа бий:

- зөвхөн $A$ — $A \setminus B$
- хоёуланд нь — $A \cap B$
- зөвхөн $B$ — $B \setminus A$
- аль нь ч биш — $\overline{A \cup B}$

Огтлолцолгүй гэдэг нь мужийн тоонууд зүгээр л **нэмэгдэнэ** гэсэн үг. Диаграммын
бүх хүч тэндээс гарна.

Энэ хүснэгтийг хоёр чигт нь уншиж сурах хэрэгтэй, учир нь ЭШ хоёуланг нь
асуудаг. **Нэг чиг нь тоолол**: олонлогийн тоо бол мужуудын нийлбэр тул
$|A| = (\text{зөвхөн } A) + |A \cap B|$, эндээс
$\text{зөвхөн } A = |A| - |A \cap B|$. **Нөгөө чиг нь таних**: «Аль нь
$A \cap \overline{B}$ олонлогийг дүрсэлсэн байна вэ?» гэсэн хэлбэрээр бичиглэл
өгөөд зурагт аль муж будагдсаныг асууна. Хариу нь дээрх хүснэгтийн хоёр дахь
мөр — $A$ дугуйгаас огтлолцох хэсгийг хасч авсан муж.

Дүүргэх дараалал үргэлж нэг: **эхлээд огтлолцол**, дараа нь зөвхөн-мужууд,
хамгийн сүүлд гадна тал. Огтлолцлыг мэдэхгүйгээр зөвхөн-мужийг олох арга байхгүй.

Шалгалтын өгүүлбэрүүд мужид шууд буудаг: «зөвхөн алгебр» нэг муж, «хоёуланд нь»
огтлолцол, «дор хаяж нэг нь» гурван муж, «аль нь ч биш» гадна тал.

**FACTS:**

1. **Мужид задлах** — $|A| = |A \setminus B| + |A \cap B|$ —
   Олонлогийн тоо нь өөрийн ганцаарчилсан муж дээр огтлолцлыг нэмсэн нь.
2. **Бүгд тоологдсон** —
   $|U| = |A \setminus B| + |A \cap B| + |B \setminus A| + |\overline{A \cup B}|$ —
   Дөрвөн муж орчлонг бүрэн хучна, тул тоонууд нь $|U|$ болж нийлэх ёстой.

**MISTAKES:**

- Зөвхөн-$A$ мужид $|A| - |A \cap B|$-ийн оронд $|A|$-г бичих. Дугуйн бүтэн тоо
  огтлолцлыг агуулж байгаа. Эхлээд огтлолцлоо бичээд дараа нь хасна.
- «Аль нь ч биш» муж байдгийг мартах. Хоёр дугуй орчлонг ховор дүүргэдэг тул
  үлдэгдлээ $|U|$-тэй үргэлж тулгаж шалгана.

**WORKED esh-venn-l1-we1:**

- **PROBLEM:** $30$ сурагчтай ангид $18$ нь сагсан бөмбөг, $14$ нь волейбол,
  $8$ нь хоёуланг нь тоглодог. Дөрвөн мужийг дүүргээрэй.
- **WORKING:** Эхлээд огтлолцол: хоёуланг нь $= 8$. Зөвхөн сагсан бөмбөг:
  $18 - 8 = 10$; зөвхөн волейбол: $14 - 8 = 6$. Дугуйнуудад хамрагдсан нь
  $10 + 8 + 6 = 24$; аль нь ч биш: $30 - 24 = 6$.
- **ANSWER:** $10$, $8$, $6$, $6$

**WORKED esh-venn-l1-we2:**

- **PROBLEM:** $40$ сурагчийн $12$ нь зөвхөн франц хэл, $9$ нь франц, герман
  хоёуланг нь, $11$ нь аль нь ч үздэггүй. Герман хэл үздэг сурагч хэд вэ?
- **WORKING:** Дөрвөн муж $40$ болж нийлэх ёстой тул зөвхөн герман
  $= 40 - 12 - 9 - 11 = 8$. Герман дугуйн бүтэн тоо нь зөвхөн-муж дээр
  огтлолцлыг нэмсэн нь: $|G| = 8 + 9 = 17$.
- **ANSWER:** $17$

**TRY esh-venn-l1-t1:**

- **PROBLEM:** $|U| = 50$, $|A| = 27$, $|B| = 22$, хоёуланд нь $= 13$. Аль нь ч
  биш муж хэдэн элементтэй вэ?
- **ANSWER:** $14$
- **WORKING:** Зөвхөн $A$: $14$; зөвхөн $B$: $9$; дугуйнуудад хамрагдсан нь
  $14 + 13 + 9 = 36$; аль нь ч биш $= 50 - 36 = 14$.

**TRY esh-venn-l1-t2:**

- **PROBLEM:** $45$ хүнээс асуухад $16$ нь зөвхөн цай, $21$ нь зөвхөн кофе
  дуртай бөгөөд хүн бүр дор хаяж нэгэнд нь дуртай байв. Хоёуланд нь дуртай нь
  хэд вэ?
- **ANSWER:** $8$
- **WORKING:** Гадна талд хэн ч байхгүй тул дотор талын гурван муж бүх бүлгийг
  хучна: хоёуланд нь $= 45 - 16 - 21 = 8$.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Зураг · **title** Дөрвөн бүс, давхар тоолол үгүй<br>**body** Дөрвөн муж бүтцээрээ огтлолцолгүй — хүн бүр яг нэгд нь оноогдоно. Тийм учраас мужийн арифметик бол энгийн нэмэх үйлдэл, мөн тийм учраас хоёр олонлогийн аливаа бодлогын эхний алхам нэг: огтлолцлоо бичих. |
| 1 | vennCounts | **eyebrow** Тоглоом · **title** Тоог нь чирээд нийлбэрийг нь ажигла<br>**teach** Дөрвөн мужийн тоог тохируулаад $\|A\|$, $\|B\|$, нэгдэл, орчлон хэрхэн дахин тооцоологдохыг ажиглаарай. «Хоёуланд нь» өөрчлөгдөхөд $\|A\|$ мөн өөрчлөгдөж байгааг анзаараарай — дугуйн бүтэн тоо огтлолцлыг үргэлж агуулна.<br>**config** unchanged (`mode: regions`, `onlyA: 10`, `both: 8`, `onlyB: 6`, `neither: 6`); `labelA`/`labelB` stay Latin `A`/`B` |
| 2 | worked | **title** Эхлээд огтлолцол, дараа нь гадагш — `esh-venn-l1-we1` |
| 3 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Аль муж вэ?<br>**prompt** Аль нь $F \cap \overline{G}$ олонлогийг дүрсэлсэн байна вэ?<br>**options** `$F$ дугуйгаас огтлолцох хэсгийг хассан муж` · `$F$ дугуй бүтнээрээ` · `огтлолцох хэсэг` · `$G$-ээс гадна бүх зүйл` — **correctIndex 0**<br>**explanation** $F \cap \overline{G}$ гэдэг нь $F$-д орших боловч $G$-д орохгүй хэсэг, өөрөөр хэлбэл зөвхөн-$F$ муж: $\|F\| - \|F \cap G\|$. Дугуй бүтнээрээ бол давхар үздэг хүмүүсийг мөн агуулна. |
| 4 | worked | **title** Дугуй руу ухраад бодох — `esh-venn-l1-we2` |
| 5 | tryIt | **title** Гадна талынхныг олох — `esh-venn-l1-t1` |
| 6 | tryIt | **title** Нөхцөлөө анхааралтай уншаарай — `esh-venn-l1-t2` |
| 7 | recap | **title** Санаж үлдэх зүйл<br>**points** Огтлолцолгүй дөрвөн муж; тоонууд нь нэмэгдэнэ · Эхлээд огтлолцол; «зөвхөн» гэдэг нь дугуй хасах огтлолцол · Муж бүр бичиглэлтэй: $A \setminus B$, $A \cap B$, $B \setminus A$, $\overline{A \cup B}$ · Тулгаж шалга: мужууд $\|U\|$ болж нийлнэ |

---

## Lesson 2 — `inclusion-exclusion`

**What makes this a rewrite.** The English presents one equation,
$|A \cup B| = |A| + |B| - |A \cap B|$, and drills it. But the hardest real set
item in the bank does not give you $|A|$ or $|B|$ at all:

> «$A$ ба $B$ нь $U$ олонлогийн дэд олонлогууд. $|U| = 30$, $|A \cup B| = 21$,
> $|A \setminus B| = 10$, $|B \setminus A| = 5$ бол $|B \cap A| = ?$»
> (Test-2A Q34, hard tier)

and its published solution uses a different identity:
$|A \cup B| = |A \setminus B| + |B \setminus A| + |A \cap B|$. A student drilled
only on the English form has to derive the marker's line under time pressure.

So this version teaches **both forms as one idea** — the union is a sum of
disjoint regions, and $|A| + |B| - |A \cap B|$ is that same sum with the
overlap's double count repaired — and gives the region form equal billing,
because that is the one the hard item wants. The bounds paragraph stays third,
as in English.

**TITLE:** Нэмэх–хасах зарчим: хоёр олонлог

**COMPARISON:** Хоёр жагсаалтыг нийлүүлэхэд хоёуланд нь бичигдсэн хүмүүс хоёр
удаа тоологдоно — тиймээс нэг удаа хасна. Тэр засвар нь өөрөө томьёо юм.

**OBJECTIVE:** $|A \cup B| = |A| + |B| - |A \cap B|$ болон мужийн нийлбэр
хэлбэрийг хоёуланг нь чөлөөтэй, аль ч чигт хэрэглэх; огтлолцол буюу олонлогийн
тоог тэндээс гаргаж авах.

**KEY IDEA:** Нэгдэл бол огтлолцолгүй мужуудын нийлбэр. Үүнийг хоёр янзаар
бичиж болно, ЭШ хоёуланг нь хэрэглэдэг.

**TEACHING:**

$|A|$ ба $|B|$-г шууд нэмэхэд огтлолцлыг хоёр удаа тоолно, тиймээс нэг удаа
хасна:

$$|A \cup B| = |A| + |B| - |A \cap B|.$$

Дөрвөн хэмжигдэхүүн, нэг тэгшитгэл — ЭШ дурын гурвыг нь өгөөд дөрөв дэх нь
асууна.

Гэхдээ **хоёр дахь хэлбэр нь ижил чухал**. Нэгдэл бол огтлолцолгүй гурван
мужийн нийлбэр:

$$|A \cup B| = |A \setminus B| + |A \cap B| + |B \setminus A|.$$

ЭШ-ийн хамгийн хэцүү олонлогийн бодлого яг үүнийг шаарддаг: $|U|$, $|A \cup B|$,
$|A \setminus B|$, $|B \setminus A|$ өгөөд $|A \cap B|$-г асуудаг бөгөөд $|A|$,
$|B|$ огт өгөгддөггүй. Эхний хэлбэрээр орох гарц байхгүй. Хоёулаа нэг санааны
хоёр бичлэг гэдгийг ойлгосон хүн аль ч өгөгдөлтэй тулгарахад гацахгүй.

Орчлонтой хослуулбал: $|\text{аль нь ч биш}| = |U| - |A \cup B|$. Ихэнх
судалгааны бодлого энэ хоёр мөрийг дараалуулан ажиллуулсан хэрэг.

Хилийн асуулт мөн ижил тэгшитгэлээс гарна: огтлолцол хамгийн их байх нь нэг
олонлог нөгөөгийнхөө дотор бүтнээрээ багтсан үе ($\min(|A|, |B|)$), хамгийн бага
байх нь нэгдэл орчлоныг бүхэлд нь дүүргэсэн үе ($|A| + |B| - |U|$, сөрөг гарвал
$0$).

**FACTS:**

1. **Нэмэх–хасах зарчим** — $|A \cup B| = |A| + |B| - |A \cap B|$ —
   Хоёуланг нь нэм, давхар тоологдсон огтлолцлыг хас.
2. **Мужийн хэлбэр** —
   $|A \cup B| = |A \setminus B| + |A \cap B| + |B \setminus A|$ —
   Ижил нэгдэл, огтлолцолгүй гурван мужаар. ЭШ-ийн хэцүү бодлого үүнийг нэхдэг.

**MISTAKES:**

- Олонлогууд огтлолцолгүй гэж хаана ч заагаагүй байхад $|A| + |B|$-г нэгдэл
  болгон хэрэглэх. Зөвхөн огтлолцолгүй олонлогууд цэвэр нэмэгдэнэ. Огтлолцох
  боломж байвал томьёонд $- |A \cap B|$ гишүүн зайлшгүй хэрэгтэй.
- Багадаа олонлогоос нь том огтлолцол хариулах. $|A \cap B| \le \min(|A|, |B|)$
  үргэлж биелнэ — $15$ ба $30$ хэмжээтэй хоёр олонлогийн огтлолцол $20$ байх
  боломжгүй. Хариугаа хилтэй нь тулгаж шалгана.

**WORKED esh-venn-l2-we1:**

- **PROBLEM:** $60$ хүний $38$ нь гар утастай, $27$ нь зөөврийн компьютертэй,
  $12$ нь хоёуланг нь эзэмшдэг. Аль нь ч байхгүй хүн хэд вэ?
- **WORKING:** $|A \cup B| = 38 + 27 - 12 = 53$; аль нь ч биш $= 60 - 53 = 7$.
- **ANSWER:** $7$

**WORKED esh-venn-l2-we2:**

- **PROBLEM:** $52$ сурагчийн бүгд нь хоёр сэтгүүлийн дор хаяж нэгийг уншдаг.
  $31$ нь эхнийхийг, $35$ нь хоёр дахийг уншдаг бол хоёуланг нь уншдаг нь хэд вэ?
- **WORKING:** «Дор хаяж нэг» гэдэг нь $|A \cup B| = 52$ гэсэн үг. Тэгшитгэлээс:
  $|A \cap B| = 31 + 35 - 52 = 14$.
- **ANSWER:** $14$

**TRY esh-venn-l2-t1:**

- **PROBLEM:** $|A| = 45$, $|B| = 30$, $|A \cup B| = 63$ бол $|A \cap B|$ ба
  $|A \setminus B|$-г олоорой.
- **ANSWER:** $12$ ба $33$
- **WORKING:** $|A \cap B| = 45 + 30 - 63 = 12$; $|A \setminus B| = 45 - 12 = 33$.

**TRY esh-venn-l2-t2:**

- **PROBLEM:** $28$ сурагчтай ангид хүн бүр англи эсвэл орос хэл үздэг. $19$ нь
  англи, $16$ нь орос хэл үздэг бол зөвхөн орос хэл үздэг нь хэд вэ?
- **ANSWER:** $9$
- **WORKING:** Хоёуланг нь $= 19 + 16 - 28 = 7$; зөвхөн орос $= 16 - 7 = 9$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Засвар · **title** Хоёр удаа тоологдож, нэг удаа хасагдана<br>**body** $\|A\| + \|B\|$ гэдэг нь хоёр дугуйг тойрч явахдаа огтлолцол дээр хоёр удаа гишгэж байгаа хэрэг. Нэг хасалт үүнийг засна. Үүнийг мужаар бичвэл $\|A \setminus B\| + \|A \cap B\| + \|B \setminus A\|$ — ижил нэгдэл, засвар шаардагдахгүй хэлбэр. |
| 1 | worked | **title** Нэгдэл, дараа нь аль нь ч биш — `esh-venn-l2-we1` |
| 2 | worked | **title** Огтлолцлыг тэгшитгэлээс гаргах — `esh-venn-l2-we2` |
| 3 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Боломжтой юу, үгүй юу<br>**prompt** $\|A\| = 15$, $\|B\| = 30$ бөгөөд хэн нэгэн $\|A \cap B\| = 20$ гэж мэдэгдэв. Боломжтой юу?<br>**options** `Үгүй — огтлолцол $15$-аас хэтэрч чадахгүй` · `Тийм` · `Зөвхөн $\|U\| = 45$ үед` · `Зөвхөн олонлогууд тэнцүү үед` — **correctIndex 0**<br>**explanation** Огтлолцол нь ХОЁУЛАНГИЙНХ нь дотор оршдог тул хамгийн ихдээ $\min(15, 30) = 15$. Мэдэгдсэн $20$ шууд унана. |
| 4 | tryIt | **title** Огтлолцол, дараа нь ялгавар — `esh-venn-l2-t1` |
| 5 | tryIt | **title** Хүн бүр хамрагдсан — `esh-venn-l2-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** $\|A \cup B\| = \|A\| + \|B\| - \|A \cap B\|$ — дутууг нь ол · Мужийн хэлбэр: $\|A \setminus B\| + \|A \cap B\| + \|B \setminus A\|$; хэцүү бодлого үүнийг нэхдэг · «Аль нь ч биш» бол $\|U\| - \|A \cup B\|$ · Огтлолцол багадаа олонлогоосоо хэзээ ч том биш |

---

## Lesson 3 — `three-set-venn`

**What makes this a rewrite.** The English lesson is already built the right way
round — center outward — so the structure survives. What it lacks is a **name**
for the move it keeps performing. The sets topic gave the $+1$ rule the name
«нэгийг нэм» so it would become a reflex; the same trick applies here, and the
peel is the single most-repeated step in three-set problems: every pairwise
total the exam states already contains the center, and every one of them must
have it subtracted. So the move is named «**төвийг хас**» and drilled under that
name, matching the sets topic's «нэгийг нэм» so the ЭШ unit builds a small
vocabulary of named reflexes rather than a list of unnamed steps.

**TITLE:** Гурван олонлог, найман муж

**COMPARISON:** Гурван гэрлийн туяа найман бүс үүсгэнэ — голын гурвалсан
огтлолцлоос эхлээд гадна талын харанхуй хүртэл. Голоос нь эхлээд гадагш
дүүргэнэ, бай онилохтой яг адил.

**OBJECTIVE:** Гурван олонлогийн диаграммын найман мужийг өгөгдлөөс нь бүрэн
дүүргэх, гурвалсан огтлолцлоос эхлээд гадагш ажиллах.

**KEY IDEA:** Найман муж, голоос нь гадагш дүүргэнэ. Хосын огтлолцол нь голыг
ҮРГЭЛЖ агуулна — «яг хоёрт нь» мужийг олохын тулд төвийг хас.

**TEACHING:**

Гурван олонлог орчлонг огтлолцолгүй **найман муж** болгон хуваана: гурван
«зөвхөн» муж, гурван «яг хоёрт нь» муж, голын гурвалсан огтлолцол, гадна тал.
Өмнөх шигээ мужийн тоонууд нэмэгдэнэ.

Дүүргэх дараалал бол бүх зүйл. **Голоос** эхэлнэ:
$|A \cap B \cap C|$. Дараа нь хосуудыг арилгана — энэ алхмыг нэрлэе:
**төвийг хас**. Хэлж өгсөн $|A \cap B|$ нь голыг агуулж байгаа тул «яг $A$ ба
$B$-д, $C$-д үгүй» муж нь $|A \cap B| - |A \cap B \cap C|$ болно. Дараа нь
зөвхөн-мужууд, хамгийн сүүлд гадна тал.

Энэ нэг зуршил гурван олонлогийн бодлогын алдааны дийлэнхийг устгана: ЭШ хосын
бүтэн огтлолцлыг өгдөг, харин асуултаа «яг хоёрт нь» гэж тавьдаг. Хоёрын хооронд
яг нэг тоо — гол — байна.

Энэ хичээлээр дамжуулан ашиглах судалгааны жишээ: зөвхөн-тоонууд $9$, $6$, $5$;
«яг хоёрт нь» мужууд $4$, $3$, $2$; гол $1$; гадна тал $10$. Тэгвэл
$|A| = 9 + 4 + 3 + 1 = 17$ — дугуйн бүтэн тоо нь өөрийн дөрвөн мужийн нийлбэр.

**FACTS:**

1. **«Яг хоёрт нь» муж** —
   $|A \cap B \setminus C| = |A \cap B| - |A \cap B \cap C|$ —
   Хэлж өгсөн хосын огтлолцол гурвалсныг агуулна — төвийг хас.
2. **Дугуйн бүтэн тоо** —
   $|A| = |A \setminus (B \cup C)| + |A \cap B \setminus C| + |A \cap C \setminus B| + |A \cap B \cap C|$ —
   Дугуй бүр яг дөрвөн мужаас бүрдэнэ.

**MISTAKES:**

- Хэлж өгсөн хосын огтлолцлыг «яг хоёрт нь» муж гэж авах. $|A \cap B|$ нь
  гурвалсан огтлолцлыг агуулна. «Яг хоёрт нь» муж бол
  $|A \cap B| - |A \cap B \cap C|$ — төвийг хассан нь.
- Голыг дүүргэхээс өмнө дугуйнуудыг дүүргэх. Огтлолцож буй бүх зүйл голтой
  холбоотой тул $|A \cap B \cap C|$-г эхэлж бичихгүй бол дараагийн хасалт бүр
  буруу гарна.

**WORKED esh-venn-l3-we1:**

- **PROBLEM:** Судалгаанд $|A \cap B| = 5$, $|A \cap C| = 4$, $|B \cap C| = 3$,
  $|A \cap B \cap C| = 1$ байв. «Яг хоёр олонлогт» харьяалагдах гурван мужийн
  тоог олоорой.
- **WORKING:** Хосын бүтэн тоо бүрээс төвийг хасна: $AB$ зөвхөн $= 5 - 1 = 4$;
  $AC$ зөвхөн $= 4 - 1 = 3$; $BC$ зөвхөн $= 3 - 1 = 2$.
- **ANSWER:** $4$, $3$, $2$

**WORKED esh-venn-l3-we2:**

- **PROBLEM:** Үргэлжлүүлье: $|A| = 17$ бөгөөд $A$ дугуйн огтлолцлын мужуудад
  $4$, $3$, $1$ хүн байна. Зөвхөн $A$-д хэд байгаа вэ? Мөн аль нь ч биш нь $10$,
  үлдсэн зөвхөн-мужууд $6$ ба $5$ бол судалгаанд нийт хэдэн хүн оролцсон бэ?
- **WORKING:** Зөвхөн $A$ $= 17 - 4 - 3 - 1 = 9$. Найман мужийг бүгдийг нь
  нэмбэл: $9 + 6 + 5 + 4 + 3 + 2 + 1 + 10 = 40$.
- **ANSWER:** $9$ ба $40$

**TRY esh-venn-l3-t1:**

- **PROBLEM:** $|B| = 13$, гол $1$, $AB$-зөвхөн $4$, $BC$-зөвхөн $2$ бол зөвхөн
  $B$-д хэд байгаа вэ?
- **ANSWER:** $6$
- **WORKING:** Зөвхөн $B$ $= 13 - 4 - 2 - 1 = 6$.

**TRY esh-venn-l3-t2:**

- **PROBLEM:** Мөнөөх судалгаанд ЯГ нэг олонлогт, мөн яг хоёр олонлогт
  харьяалагдах хүн тус бүр хэд байна вэ?
- **ANSWER:** $20$ ба $9$
- **WORKING:** Яг нэгд нь: $9 + 6 + 5 = 20$. Яг хоёрт нь: $4 + 3 + 2 = 9$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Газрын зураг · **title** Эхлээд бай<br>**body** Дүүргэх дарааллаа тогтоох хүртэл найман муж эмх замбараагүй санагдана: гол, дараа нь гурван «яг хоёрт нь» муж, дараа нь зөвхөн-мужууд, эцэст нь гадна тал. Алхам бүр нь аль хэдийн мэдэгдсэн зүйлээс хийх нэг хасалт. |
| 1 | worked | **title** Хосын огтлолцлоос төвийг хасах — `esh-venn-l3-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Голыг агуулна<br>**prompt** $\|A \cap B\| = 9$ ба $\|A \cap B \cap C\| = 4$. $A$, $B$-д байгаа боловч $C$-д БАЙХГҮЙ хүн хэд вэ?<br>**options** `$5$` · `$9$` · `$13$` · `$4$` — **correctIndex 0**<br>**explanation** Хосын бүтэн тоо голыг агуулна, тиймээс төвийг хасна: $9 - 4 = 5$. $9$-ийг шууд авбал $C$-д мөн хамаарах дөрвөн хүнийг андуурч оруулна. |
| 3 | worked | **title** Дугуй бол дөрвөн муж — `esh-venn-l3-we2` |
| 4 | tryIt | **title** Өөр дугуй, ижил хасалт — `esh-venn-l3-t1` |
| 5 | tryIt | **title** Яг нэгд нь, яг хоёрт нь — `esh-venn-l3-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** Дараалал: гол → «яг хоёрт нь» мужууд → зөвхөн-мужууд → гадна тал · Хосын огтлолцол голыг агуулна: төвийг хас · Найман муж бүгдээрээ $\|U\|$ болж нийлнэ — эцсийн шалгалт болгон ашиглана |

---

## Lesson 4 — `three-set-inclusion-exclusion`

**What makes this a rewrite.** The English opens with the formula and verifies
it against the survey. This version opens with **the two-step shape the exam
always uses** — compute the union, then subtract it from $|U|$ to answer «аль нь
ч биш» — because in every survey item on the paper that is the actual question,
and the formula is only the first of the two lines.

The second change is that the full-overlap vs exclusive-region distinction is
promoted from a common-mistake note into the lesson's spine. It is the one
error that destroys a whole three-set answer, it is invisible when it happens
(the arithmetic still works, it just answers a different question), and lesson 3
has just spent its whole length teaching the student to compute exclusive
regions — which is precisely what makes them likely to feed those numbers into
this formula's pairwise slots.

**TITLE:** Нэмэх–хасах зарчим: гурван олонлог

**COMPARISON:** Гурван жагсаалтыг нийлүүлэхэд хосоороо давхцсан хүмүүс хоёр
удаа, гурвуулаа давхцсан хүмүүс гурван удаа тоологдоно. Гурван хосыг нь хасахад
гурвуулаа давхцсан хүмүүс бүрмөсөн алга болно — тиймээс нэг удаа буцааж нэмнэ.
Тэр нэмэх-хасах бүжиг нь өөрөө томьёо юм.

**OBJECTIVE:** Гурван олонлогийн нэмэх–хасах зарчмыг судалгааны бодлогод
хэрэглэх, «дор хаяж нэг» ба «аль нь ч биш» асуултыг хоёуланг нь хариулах.

**KEY IDEA:** Ганцаарчилсан хас хос нэм гурвалсан: элемент бүр яг нэг удаа
тоологдоно. «Аль нь ч биш» бол орчлоноос нэгдлийг хассан нь.

**TEACHING:**

ЭШ-ийн судалгааны бодлого бараг үргэлж хоёр мөрөөс бүрдэнэ. **Нэгдүгээр мөр** —
нэгдлийг олох:

$$|A \cup B \cup C| = |A| + |B| + |C| - |A \cap B| - |A \cap C| - |B \cap C| + |A \cap B \cap C|.$$

**Хоёрдугаар мөр** — асуултад хариулах:
$|\text{аль нь ч биш}| = |U| - |A \cup B \cup C|$. Бодлогын нөхцөл ихэвчлэн
«аль нь ч сонгоогүй хэдэн хүн байв?» гэж асуудаг тул нэгдлээ олоод зогсох нь
хагас хариу.

Томьёо яагаад ажилладаг вэ. Гурвуулаа давхцсан нэг хүнийг дагаж үзье:
ганцаарчилсан гурван тоонд гурван удаа нэмэгдэж, гурван хосын огтлолцолд гурван
удаа хасагдаж, тэгээр үлдэнэ — эцсийн $+|A \cap B \cap C|$ гишүүн түүнийг
буцааж оруулна. Хоёр олонлогт харьяалагдах хүн хоёр удаа нэмэгдээд нэг удаа
хасагдана. Хүн бүр яг нэг удаа тоологдоно — энэ нь өөрөө томьёоны баталгаа.

**Хамгийн үнэтэй алдаа энд байна.** Томьёо нь хосын **бүтэн** огтлолцлыг
шаарддаг, өөрөөр хэлбэл голыг агуулсан $|A \cap B|$-г. Өмнөх хичээлд бид «яг
хоёрт нь» мужийг олж сурсан бөгөөд яг тэр тоонуудыг энэ томьёоны хосын нүдэнд
хийх нь хамгийн байнга гардаг алдаа. Хоёр арга хоёулаа зөв боловч тэдгээрийг
бодолтын дунд холих нь болохгүй: диаграмм огтлолцолгүй мужаар, томьёо бүтэн
огтлолцлоор ажиллана.

Судалгааны өгөгдөл дээр шалгавал: $17 + 13 + 11 - 5 - 4 - 3 + 1 = 30$, энэ нь
мужийн нийлбэртэй яг таарна. Томьёо ба диаграмм зөрвөл арифметик буруу байгаа
хэрэг — тэд нэг ижил тоог тоолж байгаа.

**FACTS:**

1. **Гурван олонлогийн нэмэх–хасах зарчим** —
   $|A \cup B \cup C| = \Sigma|A| - \Sigma|A \cap B| + |A \cap B \cap C|$ —
   Ганцаарчилсныг нэм, хосыг хас, гурвалсныг буцааж нэм.
2. **Аль нь ч биш** —
   $|\overline{A \cup B \cup C}| = |U| - |A \cup B \cup C|$ —
   Судалгааны бодлогын хаалтын мөр: нэгдлээ олоод нийтээс хас.

**MISTAKES:**

- «Ганцаарчилсан хас хос» дээр зогсоод гурвалсныг буцааж нэмэхээ мартах. Гурван
  хосын огтлолцлыг хасахад гурвуулаа давхцсан хүмүүс гурван удаа нэмэгдээд
  гурван удаа хасагдаж тэг болно. $+|A \cap B \cap C|$ гишүүн тэднийг сэргээнэ.
- «Яг хоёрт нь» мужийн тоог томьёоны хосын нүдэнд хийх. Томьёо БҮТЭН огтлолцлыг
  (гол оруулсан) шаардана. Мужийн тоо нь диаграммын аргад харьяалагдана —
  хоёрыг бодолтын дунд холихгүй.

**WORKED esh-venn-l4-we1:**

- **PROBLEM:** Судалгааны өгөгдөл дээр томьёог шалгаарай: $|A| = 17$,
  $|B| = 13$, $|C| = 11$, $|A \cap B| = 5$, $|A \cap C| = 4$, $|B \cap C| = 3$,
  $|A \cap B \cap C| = 1$.
- **WORKING:** $17 + 13 + 11 - 5 - 4 - 3 + 1 = 30$ — энэ нь найман мужийн
  нийлбэрээс гадна талыг хассантай яг тэнцүү ($40 - 10 = 30$).
- **ANSWER:** $30$

**WORKED esh-venn-l4-we2:**

- **PROBLEM:** $100$ сурагчийн $55$ нь математик, $44$ нь физик, $35$ нь химид
  дуртай; $20$ нь математик, физик хоёуланд, $15$ нь математик, хими, $12$ нь
  физик, химид дуртай; $5$ нь гурвуулаанд нь дуртай. Аль нь ч дургүй сурагч хэд
  вэ?
- **WORKING:** Эхний мөр — нэгдэл:
  $55 + 44 + 35 - 20 - 15 - 12 + 5 = 92$. Хоёрдугаар мөр — асуултын хариу:
  $100 - 92 = 8$.
- **ANSWER:** $8$

**TRY esh-venn-l4-t1:**

- **PROBLEM:** $|A| = 30$, $|B| = 25$, $|C| = 20$, хосын огтлолцлууд $10$, $8$,
  $6$, гурвалсан нь $3$ бол $|A \cup B \cup C|$-г олоорой.
- **ANSWER:** $54$
- **WORKING:** $30 + 25 + 20 - 10 - 8 - 6 + 3 = 54$.

**TRY esh-venn-l4-t2:**

- **PROBLEM:** Өмнөх бодлогод $|U| = 60$ бол гурван олонлогийн аль нь ч биш
  элемент хэд байх вэ?
- **ANSWER:** $6$
- **WORKING:** $60 - 54 = 6$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Хоёр мөр · **title** Нэгдлээ ол, дараа нь нийтээс хас<br>**body** ЭШ-ийн судалгааны бодлого бараг үргэлж хоёр мөр: томьёогоор $\|A \cup B \cup C\|$-г олоод, дараа нь $\|U\|$-аас хасч «аль нь ч биш»-ийг гаргана. Нэгдлээ олоод зогсох нь хагас хариу — асуулт бараг хэзээ ч нэгдлийг өөрийг нь асуудаггүй. |
| 1 | worked | **title** Томьёо ба диаграмм тулгарах нь — `esh-venn-l4-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Нэг хүнийг дагаж үз<br>**prompt** Нэг хүн $A$, $B$-д харьяалагддаг ч $C$-д үгүй. Томьёо түүнийг хэдэн удаа тоолох вэ?<br>**options** `нэг удаа` · `хоёр удаа` · `тэг удаа` · `гурван удаа` — **correctIndex 0**<br>**explanation** Хоёр удаа нэмэгдэж ($\|A\|$, $\|B\|$), нэг удаа хасагдана ($\|A \cap B\|$): цэвэр дүнгээр $2 - 1 = 1$. Хүн бүр нэг болж цөвөрнө — энэ нь өөрөө томьёоны баталгаа. |
| 3 | worked | **title** Сонгодог судалгаа — `esh-venn-l4-we2` |
| 4 | tryIt | **title** Шууд хэрэглээ — `esh-venn-l4-t1` |
| 5 | tryIt | **title** Гадна талынхан — `esh-venn-l4-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** Ганцаарчилсан $-$ хос $+$ гурвалсан — элемент бүр яг нэг удаа · «Аль нь ч биш» $= \|U\| -$ нэгдэл; «дор хаяж нэг» $=$ нэгдэл өөрөө · Томьёо БҮТЭН огтлолцол хэрэглэнэ, диаграмм огтлолцолгүй муж — хоёрыг холихгүй |

---

## Practice — ten items, same ids, same `check[]`

**esh-venn-p1** — $|U| = 55$, $|A| = 31$, $|B| = 24$, $|A \cap B| = 12$. Дөрвөн
мужийг бүгдийг нь дүүргээрэй.
> Зөвхөн $A$: $31 - 12 = 19$; зөвхөн $B$: $24 - 12 = 12$; хоёуланд нь: $12$;
> дугуйнуудад хамрагдсан нь $19 + 12 + 12 = 43$, тул аль нь ч биш:
> $55 - 43 = 12$.

**esh-venn-p2** — Сурагч бүр хоёр шалгалтын дор хаяж нэгд нь тэнцжээ. $70\%$ нь
эхнийхэд, $60\%$ нь хоёрдугаарт тэнцсэн бол хэдэн хувь нь хоёуланд нь тэнцсэн бэ?
> «Дор хаяж нэг» тул нэгдэл нь $100\%$. Эндээс $70 + 60 - 100 = 30$ хувь.

**esh-venn-p3** — $|A| = 26$, $|A \cup B| = 41$, $|A \cap B| = 9$ бол $|B|$-г
олоорой.
> Нэмэх–хасах зарчмыг $|B|$-ийн хувьд бодвол $|B| = 41 - 26 + 9 = 24$.

**esh-venn-p4** — $80$ хүний $45$ нь цай, $38$ нь кофе уудаг; $10$ нь аль нь ч
уудаггүй. Хоёуланг нь уудаг нь хэд вэ?
> Нэгдэл $= 80 - 10 = 70$; хоёуланг нь $= 45 + 38 - 70 = 13$.

**esh-venn-p5** — $|A \cap B| = 11$, $|A \cap B \cap C| = 4$, $|A| = 29$,
$|A \cap C| = 9$. $A$-д харьяалагдах боловч $B$, $C$-ийн аль нь ч биш элемент
хэд вэ?
> $A$ дугуйг мужаар нь салгана. Хосын огтлолцол бүрээс төвийг хасна:
> $11 - 4 = 7$ ба $9 - 4 = 5$. Иймд зөвхөн $A$ $= 29 - 7 - 5 - 4 = 13$.

**esh-venn-p6** — $90$ хүний спортын судалгаа: хөл бөмбөг $50$, сагсан бөмбөг
$40$, шатар $30$; хөл+сагсан $18$, хөл+шатар $14$, сагсан+шатар $10$; гурвуулаа
$6$. Юу ч тоглодоггүй хүн хэд вэ?
> Нэгдэл $= 50 + 40 + 30 - 18 - 14 - 10 + 6 = 84$; аль нь ч биш $= 90 - 84 = 6$.

**esh-venn-p7** — Өмнөх бодлогын судалгаанд ЯГ хоёр төрлийн спорт тоглодог хүн
хэд вэ?
> Хосын бүтэн тоо бүрээс гурвалсныг хасна: $(18-6) + (14-6) + (10-6)
> = 12 + 8 + 4 = 24$.

**esh-venn-p8** — $|A| = 17$, $|B| = 13$, $|U| = 25$. $|A \cap B|$-ийн хамгийн
бага ба хамгийн их утга хэд вэ?
> Хамгийн их: $\min(17, 13) = 13$, өөрөөр хэлбэл $B$ бүтнээрээ $A$-д багтсан үе.
> Хамгийн бага: $17 + 13 - 25 = 5$ — $25$ элементтэй орчлонд энэ хоёр олонлог
> дор хаяж $5$ элемент хуваалцахаас өөр аргагүй.

**esh-venn-p9** — $200$ уншигчийн $120$ нь мэдээ, $90$ нь спорт уншдаг, $40$ нь
хоёуланг нь уншдаг. Яг нэг булан уншдаг хүн хэд вэ?
> Зөвхөн мэдээ $= 120 - 40 = 80$; зөвхөн спорт $= 90 - 40 = 50$. Яг нэг
> $= 80 + 50 = 130$.

**esh-venn-p10** — Гурван олонлогийн нэгдэл $71$, $|U| = 84$; ганцаарчилсан
тоонуудын нийлбэр $95$, гурвалсан огтлолцол $7$. Хосын огтлолцлуудын нийлбэр
хэд вэ?
> Нэмэх–хасах зарчмаас: $95 - \Sigma_{\text{хос}} + 7 = 71$, иймд
> $\Sigma_{\text{хос}} = 95 + 7 - 71 = 31$.

---

## Test yourself — seven items, same ids, same `check[]`

**esh-venn-q1** — $|A| = 34$, $|B| = 21$, $|A \cap B| = 8$ бол $|A \cup B|$-г
олоорой.
> $34 + 21 - 8 = 47$.

**esh-venn-q2** — $32$ сурагчтай ангид $20$ нь математик, $15$ нь физикт дуртай,
$4$ нь аль нь ч дургүй. Хоёуланд нь дуртай нь хэд вэ?
> Нэгдэл $= 32 - 4 = 28$; хоёуланд нь $= 20 + 15 - 28 = 7$.

**esh-venn-q3** — $|A \cap B| = 14$, $|A \cap B \cap C| = 5$. $A$, $B$-д байгаа
боловч $C$-д байхгүй элемент хэд вэ?
> Төвийг хасна: $14 - 5 = 9$.

**esh-venn-q4** — Ганцаарчилсан $28, 24, 19$; хосын огтлолцлууд $9, 7, 5$;
гурвалсан $2$. Нэгдлийг олоорой.
> $28 + 24 + 19 - 9 - 7 - 5 + 2 = 52$.

**esh-venn-q5** — Өмнөх өгөгдөл дээр $|U| = 60$ бол аль олонлогт ч
харьяалагдахгүй элемент хэд вэ?
> $60 - 52 = 8$.

**esh-venn-q6** — $75$ сурагчийн $40$ нь зөвхөн англи хэл, $25$ нь англи, герман
хоёуланг нь үздэг. Хүн бүр дор хаяж нэг хэл үздэг бол герман хэл үздэг нь хэд вэ?
> Зөвхөн герман $= 75 - 40 - 25 = 10$; $|G| = 10 + 25 = 35$.

**esh-venn-q7** — $|U| = 26$ доторх $|A| = 12$, $|B| = 20$. $|A \cap B|$-ийн
хамгийн бага утга хэд вэ?
> $12 + 20 - 26 = 6$ — орчлон нь хоёуланг нь багтаахад хэтэрхий жижиг тул
> үүнээс бага хуваалцах боломжгүй.

---

## Notes for Build

- **`check[]`: no changes required for this topic.** Every English assertion
  survives, and every number the rewritten solutions quote is already asserted.
  I checked the three places where the rewrite spells out a step the English
  left implicit — `p1` ($31 - 12$, $24 - 12$), `p2` (the union is the given
  $100\%$, not a derived value) and `p9` ($120 - 40$, $90 - 40$) — and all are
  covered by the existing arrays. The sets topic needed two additions; this one
  needs none, because the region method the rewrite promotes is already the
  method the English solutions used.
- **Notation** per R9: $\overline{A}$ for complements, $\emptyset$ for the empty
  set. The English source for this topic uses neither symbol, so nothing to
  convert — but lesson 1's fact 2 and the recap introduce
  $\overline{A \cup B}$ for the outside region, which the English wrote as the
  word "neither". That is new notation in the MN version and it is deliberate:
  it ties this topic to the notation the sets topic just taught.
- The `vennCounts` widget `config` is untouched — only its `teach` prose is
  rewritten. `labelA` / `labelB` stay Latin `A` / `B` per the symbols rule.
- No Cyrillic inside `$...$`; `$\Sigma_{\text{хос}}$` wraps its Cyrillic in
  `\text{}`.
- The `$\|A\|$` forms in the step tables are escaped for the markdown tables
  only; the JSON carries single pipes.

## Notes for Khas

1. **«муж» is doing two jobs in this course.** It is the exam's own word for a
   Venn region («хүрэн муж», test4a) — so using it here is grounded, not
   invented — but the ЭШ bank uses it far more often for a function's domain
   and range («тодорхойлогдох муж», «утгын муж»). A student meets both senses
   inside the ЭШ course. I kept it because the exam uses it; «хэсэг» or «бүс»
   would separate the senses at the cost of diverging from the paper. Your call
   and it affects this topic plus every function topic.
2. **«нэмэх–хасах зарчим»** for *inclusion–exclusion* is mine — 0 hits in both
   sources, like the four terms you approved in R9. The bank's own solution
   just says «томъёогоор» (by the formula) and never names the principle.
3. **«төвийг хас»** as the name for the peel is mine, coined to match «нэгийг
   нэм» from the sets topic. If naming these moves is not something you want the
   product doing, say so once and I will stop — there are now two of them and it
   is becoming a house style rather than a one-off.
4. **One context changed to avoid a collision.** Lesson 2's worked example is
   phones and laptops, where the English had bicycles. «Дугуй» is the word for a
   bicycle *and* the word for a Venn circle, and this topic says «дугуй» in the
   circle sense constantly. The arithmetic is untouched ($38$, $27$, $12$), so
   `check[]` is unaffected.
5. Lesson 1 opens with a stage-lighting image and lesson 3 reuses it for three
   beams. Both are the English author's metaphor, kept because they carry.
