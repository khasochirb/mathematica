# Draft — `vectors-matrices/matrices-and-operations`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**ЭШ Вектор ба матриц, unit 5 of 8.** Both spines number this unit 5; 6aw swaps
only units 1 and 2. The unit names no other unit by number. It points back to
the vector units as a group, and to the geometry course's «Хувиргалт» topic
(Notes 4).

**Four lessons, 34 items, 48 interactive steps, no nested tryItSet problems.**
(12 workedExamples + 8 tryIt + 8 practice + 6 testYourself.)

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. No em-dash parentheticals (§9), decimal comma in prose
(§7), hyphenated case suffixes (§8), condition before thing (§1). Objectives as
plain text (6d). Imperatives soft in prose that addresses the student, bare in
beats, recaps, titles and fact shorthand. Vector coordinates keep the comma, as
in the bank.

**Mirror pre-check** (6q): no `vectors-matrices-mn` mirror. Draft it.

**Ministry sections read in full first**: 10.4. The unit is mapped
(`lib/esh-course.ts:230`) to **10.4а–г**; all four are taught. 10.4д–е
(determinant and inverse) belong to unit 6.

**Exam check** (6m): «матриц» 107 in the bank, «нэгж матриц» 8, «элемент» 42,
«мөр» 8, «багана» 6, «хэмжээсийг / хэмжээтэй» 7. «тэг матриц» 0 in the bank, but
the ministry names it (10.4г). The bank writes the identity as **$E$**, never
$I$ (Notes 3).

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| matrix | **матриц** | ministry 10.4 · bank 107 |
| row · column | **мөр · багана** | bank 8 · 6 |
| entry | **элемент** | bank 42 |
| dimension | **хэмжээс** («2 × 3 хэмжээтэй матриц») | ministry 10.4д «2x2 хэмжээстэй» · bank 7 |
| square · diagonal matrix | **квадрат · диагональ матриц** | compositional |
| zero matrix | **тэг матриц** | ministry 10.4г |
| identity matrix | **нэгж матриц** | ministry 10.4г · bank 8 |
| main diagonal | **гол диагональ** | compositional |
| scalar multiplication | **тоогоор үржүүлэх** | ministry 10.4б, exactly this |
| matrix multiplication | **матрицыг матрицаар үржүүлэх** | ministry 10.4в |
| commutative | **байр солих чанартай** | Notes 3 |
| power of a matrix | **матрицын зэрэг** | bank («матрицын зэрэгт») |
| rotation | **эргүүлэлт** | as in `geometry-transformations` |

---

## Topic-level strings

**TITLE:** Матриц ба үйлдлүүд

**BLURB:** Тоон хүснэгт ба түүний арифметик: элемент ба хэмжээс, нэмэх ба
тоогоор үржүүлэх, мөн бүгдийг хөдөлгөдөг мөрийг баганаар үржүүлэх үйлдэл.

**buildsOn:** Векторын нэгжүүдийн координатаар сэтгэх арга: матриц бол
векторуудын баганууд.

---

## Lesson 1 — Матриц гэж юу вэ? (`what-is-a-matrix`)

**concreteComparison**

Дэлгүүрийн долоо хоногийн борлуулалтын хүснэгтийг бодоорой: мөр нь бараа, багана
нь өдөр, нүд бүрт нэг тоо. Тэр хүснэгт бол МАТРИЦ. Математик үүн дээр хаягийн
систем нэмдэг ($a_{23}$ элемент 2-р мөр, 3-р баганад байрлана). Хамгийн чухал нь
бүтэн хүснэгтүүдийг нэг дор бодох арифметик нэмдэг.

**objective**

Матрицын хэмжээс ба элементийг уншиж, мөр, баганын хаягийг хэрэглэж, хоёр матриц
хэзээ тэнцүү болохыг тогтоох.

**concept**

1. **Матриц** бол тоонуудын тэгш өнцөгт хүснэгт. Түүний **хэмжээс** нь мөр ×
   багана: $2 \times 3$ хэмжээтэй матриц 2 мөр, 3 баганатай. Үргэлж мөр
   түрүүлнэ: $a_{ij}$ хаяг $i$-р мөр, $j$-р багана гэсэн үг.

2. Хоёр матриц хэмжээс нь ижил БӨГӨӨД харгалзах элемент бүр нь тэнцүү үед л
   **тэнцүү**. Тэнцүү байдлыг элемент бүрээр шалгана: хаа нэгтээ ганц элемент
   зөрвөл тэнцүү биш. Иймээс матрицын тэгшитгэл энгийн тэгшитгэлүүдийн систем
   болж хувирна.

3. Одоо нэрлээд авах онцгой матрицууд: **квадрат** матриц (мөрийн тоо = баганын
   тоо), **тэг матриц** $O$ (бүх элемент нь тэг: нэмэхэд юу ч өөрчлөхгүй) ба
   **нэгж матриц** $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ (гол
   диагональ дээрээ нэгүүдтэй: үржүүлэхэд юу ч өөрчлөхгүй). Нэгж матрицтай хоёр
   хичээлийн дараа сайтар танилцана. ЭШ-ийн бодлогод нэгж матрицыг $E$ гэж
   тэмдэглэдэг.

**keyIdea**

Матриц бол мөр × багана хүснэгт; a_ij нь i-р мөр, j-р баганын элемент; тэнцүү
гэдэг нь хэмжээс ижил, элемент бүр тэнцүү гэсэн үг.

**facts**

- **title** Хэмжээс · **latex** `m \times n = \text{мөр} \times \text{багана}` ·
  **explanation** Эхлээд мөр: нийтээр мөрддөг дүрэм.
- **title** Хаяг · **latex** `a_{ij}: \; i \text{-р мөр}, \; j \text{-р багана}`
  · **explanation** Эхний индекс мөрийг, хоёр дахь нь баганыг сонгоно.
- **title** Тэнцүү байх · **latex**
  `A = B \iff \text{хэмжээс ижил, } a_{ij} = b_{ij} \; \forall i,j` ·
  **explanation** Элемент бүрээр: нэг матрицын тэгшитгэл бол олон тоон
  тэгшитгэл.

**workedExamples**

- `vm51-we1` — **statement:**
  $A = \begin{pmatrix} 5 & -1 & 3 \\ 0 & 7 & 2 \end{pmatrix}$ матрицын хэмжээс,
  $a_{12}$ ба $a_{23}$ элементүүдийг олоорой. **solution:** $A$ нь $2 \times 3$
  хэмжээтэй (2 мөр, 3 багана). $a_{12}$ нь 1-р мөр, 2-р баганад байрлах $-1$;
  $a_{23}$ нь 2-р мөр, 3-р баганад байрлах $2$.
- `vm51-we2` — **statement:**
  $\begin{pmatrix} x + 1 & 4 \\ 3 & 2y \end{pmatrix} = \begin{pmatrix} 6 & 4 \\ 3 & 10 \end{pmatrix}$
  байх $x$ ба $y$-г олоорой. **solution:** Элементүүдийг тулгавал: $x + 1 = 6$
  тул $x = 5$; $2y = 10$ тул $y = 5$.
- `vm51-we3` — **statement:** Дэлгүүр A ба B барааг бямба, ням гарагт зарсан:
  $S = \begin{pmatrix} 12 & 9 \\ 5 & 8 \end{pmatrix}$ (мөр нь бараа, багана нь
  өдөр). Ням гарагт B бараа хэд зарагдсаныг, A барааны амралтын өдрүүдийн нийт
  борлуулалтыг уншаарай. **solution:** B бараа, ням гараг: $s_{22} = 8$. A
  барааны нийт: $12 + 9 = 21$. Мөрийн нийлбэр нэг барааг бүх өдрөөр нь нэгтгэнэ.

**commonMistakes**

- **text** Хэмжээс дэх мөр, баганыг солих. · **correction** 2 × 3 гэдэг нь 2
  МӨР, 3 багана. «Эхлээд мөр, дараа нь багана» гэдэг дүрмийг хаа сайгүй мөрддөг,
  a_ij хаягт ч мөн адил.
- **text** Хэдэн элемент таарсныг хараад матрицуудыг тэнцүү гэж зарлах. ·
  **correction** Тэнцүү байдал бүрэн байх ёстой: хэмжээс ижил, элемент БҮР
  тэнцүү. Нэг нүд зөрвөл тэнцүү биш.

**tryIt**

- `vm51-t1` — **statement:**
  $B = \begin{pmatrix} 4 & 0 \\ -2 & 6 \\ 1 & 9 \end{pmatrix}$ матрицын хэмжээс
  ба $b_{31}$ элементийг олоорой. **solution:** $3 \times 2$; $b_{31} = 1$ (3-р
  мөр, 1-р багана).
- `vm51-t2` — **statement:**
  $\begin{pmatrix} 3t & 1 \\ 0 & 5 \end{pmatrix} = \begin{pmatrix} 12 & 1 \\ 0 & 5 \end{pmatrix}$
  байх $t$-г олоорой. **solution:** $3t = 12$, тиймээс $t = 4$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Объект · **title** Хаягийн системтэй хүснэгт<br>**body** Борлуулалтын хүснэгт, хичээлийн хуваарь, зургийн пикселийн блок: тоон хүснэгт хаа сайгүй бий. **Матриц** бол математикийн хүснэгт: хэмжээсийг мөр × багана гэж тоолж, элемент бүрийг $a_{ij}$ гэж хаяглана: $i$-р мөр, $j$-р багана, үргэлж мөр түрүүлнэ. |
| 1 | teach | **eyebrow** Клубын дүрэм · **title** Тэнцүү байдлыг элемент бүрээр шалгана<br>**body** $A = B$ байхын тулд хэмжээс ижил, БҮХ элемент тэнцүү байх ёстой. Тиймээс нэг матрицын тэгшитгэл дотроо олон тоон тэгшитгэл нуудаг бөгөөд шалгалт яг үүнийг ашигладаг: нэг элементэд $x$, нөгөөд $y$ нууж, тэнцүү байдлаар байцаана. Мөн тэг матриц $O$ ба нэгж матриц $I$ (диагональ дээрээ нэгүүдтэй) бол матрицын ертөнцийн 0 ба 1.<br>**beats** хэмжээс: мөр × багана, эхлээд мөр · a_ij: i-р мөр, j-р багана · тэнцүү ⇔ хэмжээс ижил + элемент бүр тэнцүү |
| 2 | tapQuestion | **eyebrow** Хаягийг шалга · **title** Элементийг ол<br>**prompt** $\begin{pmatrix} 7 & 2 & -3 \\ 4 & 0 & 9 \end{pmatrix}$ матрицын $a_{21}$ элемент аль нь вэ?<br>**explanation** 2-р мөр, 1-р багана: $4$. ($a_{12} = 2$ бол мөр, баганыг нь сольсон ихэр нь: сонгодог андуурал.)<br>**options** `$4$` · `$2$` · `$7$` · `$0$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Хэмжээс ба хаяг<br>**problemId** `vm51-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Тэнцүү байдлаар байцаах<br>**problemId** `vm51-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Тэнцүү үү, үгүй юү?<br>**prompt** $2 \times 3$ хэмжээтэй матриц $3 \times 2$ хэмжээтэй матрицтай хэзээ нэгэн цагт тэнцүү байж болох уу?<br>**explanation** Элементүүдийг харьцуулахаас ӨМНӨ хэмжээс ижил байх ёстой. Хэмжээс өөр бол яриа тэндээ дуусна.<br>**options** `Хэзээ ч үгүй: хэмжээс өөр` · `Тийм, бүх элемент таарвал` · `Хоёулаа тэг матриц байвал л` · `Мөр, баганыг нь сольсон матрицууд байвал л` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Өгөгдлийн матрицыг унших<br>**problemId** `vm51-we3` |
| 7 | tip | **eyebrow** Дадал · **title** Хэмжээсийг чангаар хэл<br>**body** Матрицын аливаа үйлдлийн өмнө матриц бүрийн хэмжээсийг нэрлээрэй («2 × 3»). Матрицын бараг бүх алдаа, ялангуяа удахгүй ирэх үржүүлэх үйлдэлд, хэтэрхий оройтож баригдсан хэмжээсийн алдаа байдаг. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Өндөр матриц<br>**problemId** `vm51-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Тэнцүү байдлаар бод<br>**problemId** `vm51-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Нэр нь хэрэгслээсээ түрүүлсэн<br>**body** Жеймс Сильвестр 1850 онд «matrix» гэдэг нэрийг зохиосон. Латинаар «умай» гэсэн үг: тэр энэ хүснэгтийг тодорхойлогчид ТӨРДӨГ эх гэж харжээ. Түүний найз Артур Кэли дараа нь таны одоо сурах гэж буй алгебрыг бүтээсэн. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Хэмжээс = мөр × багана, эхлээд мөр; $a_{ij}$ нь $i$-р мөр, $j$-р багана. · Тэнцүү: хэмжээс ижил, элемент бүр тэнцүү: нууцалсан систем. · $O$ ба $I$ бол матрицын ертөнцийн 0 ба 1. |

---

## Lesson 2 — Матрицыг нэмэх ба тоогоор үржүүлэх (`adding-and-scaling-matrices`)

**concreteComparison**

Хоёр долоо хоногийн борлуулалтын хүснэгт байна уу? Хоёр долоо хоногийн нийтийг
олохын тулд нүд нүдээр нь нэмнэ. Үнэ 10%-иар өсөв үү? Үнийн хүснэгтийг бүхэлд нь
1,1-ээр үржүүлнэ. Матрицыг нэмэх, тоогоор үржүүлэх нь таны өөрөө зохиох байсан
хүснэгтийн нүүдлүүд яг мөн: элемент бүрээр, гэнэтийн зүйлгүй.

**objective**

Матрицуудыг элемент бүрээр нэмж, хасаж, тоогоор үржүүлээд, энгийн матрицын
тэгшитгэл бодох.

**concept**

1. **Нэмэх** үйлдлийг элемент бүрээр хийх бөгөөд зөвхөн ИЖИЛ хэмжээстэй
   матрицуудын хооронд боломжтой: $(A + B)_{ij} = a_{ij} + b_{ij}$. Хасах нь мөн
   адил. Хэмжээс өөр бол нэмэх боломжгүй: хос болох нүд байхгүй.

2. **Тоогоор үржүүлэх** үйлдэл элемент бүрд үйлчилнэ: $(kA)_{ij} = k \, a_{ij}$.
   Нэмэхтэй хамт хэрэглэвэл $2A - 3B$ шиг эвлүүлгийг элемент бүрээр бодно.

3. Танил хуулиуд хүчинтэй: $A + B = B + A$, $k(A + B) = kA + kB$. Тиймээс энэ
   түвшний матрицын тэгшитгэл векторын тэгшитгэлтэй яг адил бодогдоно:
   үйлдлүүдийг нэг нэгээр нь хуулж аваад, элемент бүрээр дуусгаарай. (Дараагийн
   хичээлд амьд үлдэхгүй ганц хууль бол үржүүлэхийн байр солих чанар. Дараалал
   хамаагүй байгаа энэ үеэ таашаагаарай.)

**keyIdea**

Элемент бүрээр нэмж, тоогоор үржүүлнэ, зөвхөн ижил хэмжээстэй матрицуудад; 2A −
3B ба матрицын тэгшитгэл векторын хувилбартайгаа яг адил.

**facts**

- **title** Нэмэх · **latex** `(A + B)_{ij} = a_{ij} + b_{ij}` · **explanation**
  Нүд нүдээр: хэмжээс таарах ёстой.
- **title** Тоогоор үржүүлэх · **latex** `(kA)_{ij} = k\,a_{ij}` ·
  **explanation** Элемент бүр үржигдэхүүнээ авна.
- **title** Танил хуулиуд · **latex** `A + B = B + A,\quad k(A + B) = kA + kB` ·
  **explanation** Нэмэхийн алгебр зөв ажиллана; үржүүлэх нь тэгэхгүй.

**workedExamples**

- `vm52-we1` — **statement:**
  $\begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix} + \begin{pmatrix} 4 & 5 \\ -2 & 1 \end{pmatrix}$
  нийлбэрийг бодоорой. **solution:** Элемент бүрээр:
  $\begin{pmatrix} 6 & 4 \\ -2 & 4 \end{pmatrix}$.
- `vm52-we2` — **statement:**
  $A = \begin{pmatrix} 1 & 2 \\ 3 & 0 \end{pmatrix}$,
  $B = \begin{pmatrix} 0 & 1 \\ -1 & 2 \end{pmatrix}$ бол $2A - 3B$-г бодоорой.
  **solution:** $2A = \begin{pmatrix} 2 & 4 \\ 6 & 0 \end{pmatrix}$,
  $3B = \begin{pmatrix} 0 & 3 \\ -3 & 6 \end{pmatrix}$. Ялгавар нь:
  $\begin{pmatrix} 2 & 1 \\ 9 & -6 \end{pmatrix}$.
- `vm52-we3` — **statement:**
  $\;2X + \begin{pmatrix} 1 & 0 \\ 4 & -2 \end{pmatrix} = \begin{pmatrix} 7 & 6 \\ 0 & 4 \end{pmatrix}$
  тэгшитгэлээс $X$ матрицыг олоорой. **solution:**
  $2X = \begin{pmatrix} 6 & 6 \\ -4 & 6 \end{pmatrix}$, тиймээс
  $X = \begin{pmatrix} 3 & 3 \\ -2 & 3 \end{pmatrix}$.

**commonMistakes**

- **text** Өөр хэмжээстэй матрицуудыг нэмэх. · **correction** 2×2 дээр 2×3 нэмэх
  нь тодорхойлогдоогүй: зарим нүдэнд хос байхгүй. Элементэд хүрэхээсээ өмнө
  хэмжээсийг шалгаарай.
- **text** Зөвхөн эхний мөрийг үржүүлэх. · **correction** kA нь элемент БҮРИЙГ
  үржүүлнэ. Хагас үржүүлсэн матриц бол хагас үржүүлсэн векторын алдааны хүснэгт
  хувилбар бөгөөд яг адил хор хөнөөлтэй.

**tryIt**

- `vm52-t1` — **statement:** $3\begin{pmatrix} 2 & -1 \\ 4 & 0 \end{pmatrix}$-г
  бодоорой. **solution:** $\begin{pmatrix} 6 & -3 \\ 12 & 0 \end{pmatrix}$.
- `vm52-t2` — **statement:**
  $\begin{pmatrix} 5 & 2 \\ 1 & -3 \end{pmatrix} - \begin{pmatrix} 2 & 4 \\ -1 & 1 \end{pmatrix}$
  ялгаврыг бодоорой. **solution:**
  $\begin{pmatrix} 3 & -2 \\ 2 & -4 \end{pmatrix}$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Нүүдлүүд · **title** Хүснэгтийн арифметик<br>**body** Хоёр борлуулалтын хүснэгт нүд нүдээрээ нэмэгдэнэ; үнийн 10%-ийн өсөлт нүд бүрийг үржүүлнэ. Матрицыг нэмэх, тоогоор үржүүлэх нь эдгээр нүүдлийн албан ёсны хэлбэр: $(A+B)_{ij} = a_{ij} + b_{ij}$ ба $(kA)_{ij} = k\,a_{ij}$. Зөвхөн ижил хэмжээстэй матрицууд, элемент бүр оролцоно. |
| 1 | teach | **eyebrow** Алгебр · **title** Танил бүхэн ажилласаар (одоохондоо)<br>**body** $A + B = B + A$, $k(A+B) = kA + kB$, мөн матрицын тэгшитгэлийг векторынх шиг хуулж бодно: $2X + B = C$-ээс $X = \tfrac{1}{2}(C - B)$ гарна. Энэ тав тухыг таашаагаарай: дараагийн хичээлд үржүүлэх үйлдэл орж ирж, ДАРААЛАЛ чухал болж эхэлнэ.<br>**beats** элемент бүрээр нэмэх, хасах; хэмжээс таарах ёстой · kA элемент бүрийг үржүүлнэ · матрицын тэгшитгэлийг хуулж бодоод, элемент бүрээр дуусга |
| 2 | tapQuestion | **eyebrow** Нүүдлийг шалга · **title** Нэг элемент<br>**prompt** $2\begin{pmatrix} 3 & -2 \\ 1 & 5 \end{pmatrix} + \begin{pmatrix} 0 & 4 \\ -1 & 1 \end{pmatrix}$ илэрхийллийн 1-р мөр, 2-р баганын элемент нь…<br>**explanation** $2 \cdot (-2) + 4 = 0$. Нүд бүрийг бие даан бодно: нэг элементийн тухай хариулахад бүтэн матриц хэрэггүй.<br>**options** `$0$` · `$2$` · `$-4$` · `$4$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Энгийн нэмэх<br>**problemId** `vm52-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Эвлүүлэг<br>**problemId** `vm52-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Эхлээд хэмжээс<br>**prompt** $A$ нь $2 \times 3$, $B$ нь $3 \times 2$ хэмжээтэй. $A + B$ юу вэ?<br>**explanation** Нэмэх үйлдэл нүднүүдийг хослуулна; хэмжээс өөр бол зарим нүд хосгүй үлдэнэ. (Үржүүлэх бол өөр түүх: дараагийн хичээлд.)<br>**options** `Тодорхойлогдоогүй: хэмжээс өөр` · `$2 \times 2$ матриц` · `$3 \times 3$ матриц` · `$2 \times 3$ матриц` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** X-г ол<br>**problemId** `vm52-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Нэг элемент хэрэгтэй юу? Нэгийг л бод<br>**body** Асуулт 3A − 2B-ийн ганц элементийг асуувал хоёр үржүүлсэн матрицыг бүтнээр нь бүү байгуулаарай: эвлүүлгийг тэр ганц нүдэн дээр хийгээрэй. Хурдан, бас алдах газар цөөн. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Нэгийг үржүүл<br>**problemId** `vm52-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Нэгийг хас<br>**problemId** `vm52-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Зургийн шүүлтүүр бол матрицын нийлбэр<br>**body** Хоёр зургийг уусгаж холих нь тэдгээрийн пикселийн матрицууд дээрх яг $\alpha A + (1-\alpha)B$ эвлүүлэг: зураг засах програм бүрийн уусгах гулсуур энэ хичээлийг секундэд олон удаа гүйцэтгэдэг. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Элемент бүрээр нэмж, хас: зөвхөн ижил хэмжээстэй. · $kA$ элемент бүрийг үржүүлнэ; эвлүүлгийг нүд нүдээр бод. · Матрицын тэгшитгэлийг векторын тэгшитгэл шиг хуулж бод. |

---

## Lesson 3 — Матрицыг матрицаар үржүүлэх (`matrix-multiplication`)

**concreteComparison**

Геометрийн «Хувиргалт» сэдвийг үзсэн бол хөдөлгүүр аль хэдийн танд бий: тэнд
матрицыг цэгээр үржүүлэх нь хоёр удаагийн мөр, баганын гар барилт байсан.
Матрицыг бүтнээр нь үржүүлэх нь тэр гар барилтыг мөр, баганын ХОС БҮРД давтах
явдал: $(AB)_{ij}$ элемент бол $A$-ийн $i$-р мөрийг $B$-ийн $j$-р баганаар
скаляр үржүүлсэн тоо. Эхнээсээ эцэс хүртэл скаляр үржвэр.

**objective**

Матрицуудыг мөр · баганын скаляр үржвэрээр үржүүлж, хэмжээс нийцэж буйг шалгаад,
дараалал чухал (AB ≠ BA) гэдгийг шалгаж харах.

**concept**

1. Жор:
   $$(AB)_{ij} = (A \text{-ийн } i \text{-р мөр}) \cdot (B \text{-ийн } j \text{-р багана})$$
   хариуны нүд бүрт нэг скаляр үржвэр. $2\times 2$ матрицуудын хувьд энэ нь
   дөрвөн скаляр үржвэр.

2. Хэмжээсүүд ГАР БАРИХ ёстой: $(m \times n)(n \times p) = m \times p$. Дотоод
   хэмжээсүүд тэнцүү байж, дараа нь алга болно; гадаад хос үлдэнэ. $2\times 3$
   матрицыг $3\times 2$ матрицаар үржүүлбэл $2 \times 2$; эсрэг дарааллаар бол
   $3 \times 3$: огт өөр амьтад.

3. Мөн гол анхааруулга: **матрицын үржвэр байр солих чанаргүй**. Ерөнхийдөө
   $AB \ne BA$, хоёр үржвэр хоёулаа оршин, ижил хэмжээстэй байсан ч. Дараалал
   аль хувиргалт түрүүлж хийгдэхийг заадаг бөгөөд геометрт дараалал чухал:
   эргүүлээд тэгш хэмтэй буулгах нь тэгш хэмтэй буулгаад эргүүлэхтэй ижил биш.

**keyIdea**

(AB)_ij = i-р мөр · j-р багана; хэмжээс (m×n)(n×p) = m×p; AB ≠ BA: дараалал бол
мэдээлэл.

**facts**

- **title** Жор · **latex** `(AB)_{ij} = \sum_k a_{ik} b_{kj}` · **explanation**
  A-ийн i-р мөрийг B-ийн j-р баганаар скаляр үржүүл: хариуны нүд бүрт нэг скаляр
  үржвэр.
- **title** Гар барих дүрэм · **latex** `(m \times n)(n \times p) = m \times p`
  · **explanation** Дотоод хэмжээсүүд тэнцүү байж алга болно; гадаад хос үлдэнэ.
- **title** Байр солихгүй · **latex** `AB \ne BA \text{ (ерөнхийдөө)}` ·
  **explanation** Дараалал аль үйлдэл түрүүлж хийгдэхийг заана.

**workedExamples**

- `vm53-we1` — **statement:**
  $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$,
  $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$ бол $AB$-г бодоорой.
  **solution:** Дөрвөн скаляр үржвэр: зүүн дээд $1\cdot5 + 2\cdot7 = 19$, баруун
  дээд $1\cdot6 + 2\cdot8 = 22$, зүүн доод $3\cdot5 + 4\cdot7 = 43$, баруун доод
  $3\cdot6 + 4\cdot8 = 50$.
  $AB = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$.
- `vm53-we2` — **statement:** Ижил $A, B$ матрицуудын хувьд $BA$-г бодоод
  $AB$-тэй харьцуулаарай. **solution:**
  $BA = \begin{pmatrix} 5\cdot1 + 6\cdot3 & 5\cdot2 + 6\cdot4 \\ 7\cdot1 + 8\cdot3 & 7\cdot2 + 8\cdot4 \end{pmatrix} = \begin{pmatrix} 23 & 34 \\ 31 & 46 \end{pmatrix} \ne AB$.
  Дараалал чухал, үүрд.
- `vm53-we3` — **statement:** Матрицыг баганаар үржүүлэх:
  $\begin{pmatrix} 2 & -1 \\ 0 & 3 \end{pmatrix}\begin{pmatrix} 4 \\ 5 \end{pmatrix}$
  үржвэрийг бодоорой. **solution:** Хоёр скаляр үржвэр:
  $\binom{2\cdot4 + (-1)\cdot5}{0\cdot4 + 3\cdot5} = \binom{3}{15}$. «Хувиргалт»
  сэдвийн матрицыг цэгээр үржүүлэх нь яг энэ, зөвхөн $2\times1$ хамтрагчтай.

**commonMistakes**

- **text** Нэмэх шиг элемент бүрээр үржүүлэх. · **correction** (AB)₁₁ нь a₁₁b₁₁
  БИШ. Энэ бол A-ийн эхний мөрийг бүтнээр нь B-ийн эхний баганаар бүтнээр нь
  скаляр үржүүлсэн тоо. Үржүүлэх нь нүд хослуулах биш, скаляр үржвэр.
- **text** AB = BA гэж үзэх. · **correction** Бараг хэзээ ч үнэн биш.
  «Хялбарчлах» гэж дарааллыг чимээгүй сольсон бол та хариуг, геометрт бол
  хувиргалтыг өөрчилсөн байна.

**tryIt**

- `vm53-t1` — **statement:**
  $\begin{pmatrix} 1 & 0 \\ 2 & 3 \end{pmatrix}\begin{pmatrix} 4 & 1 \\ 0 & 5 \end{pmatrix}$
  үржвэрийг бодоорой. **solution:**
  $\begin{pmatrix} 4 & 1 \\ 8 & 17 \end{pmatrix}$.
- `vm53-t2` — **statement:** $A$ нь $2 \times 3$, $B$ нь $3 \times 4$ хэмжээтэй.
  $AB$ ямар хэмжээстэй вэ? $BA$ оршин байх уу? **solution:** $AB$ нь
  $2 \times 4$ (дотоод 3-ууд гар барина). $BA$ оршихын тулд $4 = 2$ байх ёстой:
  оршихгүй.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Хөдөлгүүр · **title** Эхнээсээ эцэс хүртэл скаляр үржвэр<br>**body** Матрицыг цэгээр үржүүлэх нь мөр · багана, хоёр удаа. Бүтэн үржвэр тэр гар барилтыг хос бүрд давтана: $(AB)_{ij}$ = ($A$-ийн $i$-р мөр) · ($B$-ийн $j$-р багана). $2\times2$ үржвэр бол дөрвөн жижиг скаляр үржвэр: хэцүү биш, зүгээр л цэгцтэй. |
| 1 | teach | **eyebrow** Хоёр анхааруулга · **title** Хэмжээсүүд гар барина; дараалал ариун<br>**body** $(m \times n)(n \times p) = m \times p$: дотоод хэмжээсүүд ТЭНЦҮҮ байж, алга болно. Мөн том анхааруулга: ерөнхийдөө $AB \ne BA$. Дараалал аль үйлдэл түрүүлж хийгдэхийг заана: эргүүлээд тэгш хэмтэй буулгах нь тэгш хэмтэй буулгаад эргүүлэхээс өөр аялал бөгөөд алгебр үүнийг санаж байдаг.<br>**beats** (AB)_ij = i-р мөр · j-р багана · (m×n)(n×p) = m×p: дотоод нь тэнцүү, гадаад нь үлдэнэ · AB ≠ BA: дараалал бол мэдээлэл |
| 2 | tapQuestion | **eyebrow** Хөдөлгүүрийг шалга · **title** Ганц нүд<br>**prompt** $A = \begin{pmatrix} 2 & 3 \\ 1 & 0 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 4 \\ 5 & 2 \end{pmatrix}$ бол $(AB)_{12}$ элемент нь…<br>**explanation** $A$-ийн 1-р мөр · $B$-ийн 2-р багана: $2 \cdot 4 + 3 \cdot 2 = 14$.<br>**options** `$14$` · `$12$` · `$17$` · `$8$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Дөрвөн скаляр үржвэр<br>**problemId** `vm53-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Сольж хар<br>**problemId** `vm53-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Гар барилт<br>**prompt** $P$ нь $3 \times 2$, $Q$ нь $2 \times 5$ хэмжээтэй. $PQ$ үржвэр нь…<br>**explanation** Дотоод 2-ууд гар бариад алга болно; гадаад $3$ ба $5$ үлдэнэ: $3 \times 5$.<br>**options** `$3 \times 5$` · `$2 \times 2$` · `$5 \times 3$` · `тодорхойлогдоогүй` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Матрицыг баганаар үржүүлэх<br>**problemId** `vm53-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Нэг хуруу мөрөнд, нөгөө нь баганад<br>**body** Бодитоор мөрдөөрэй: зүүн хуруу A-ийн мөрийг, баруун хуруу B-ийн баганыг дагаж, хамт алхах зуураа үржүүлнэ. Механик ажил, гэхдээ гишүүн алгасахыг бараг боломжгүй болгоно. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Найрсаг үржвэр<br>**problemId** `vm53-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Зөвхөн хэмжээс<br>**problemId** `vm53-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Хиймэл оюуны хөдөлгүүр<br>**body** Нейрон сүлжээ тооцооллын хувьд давхарласан матрицын үржвэрүүд юм. Хиймэл оюуны чипийн гол үзүүлэлтүүдийн нэг нь секундэд хийх үржүүлж нэмэх үйлдлийн тоо бөгөөд эдгээр нь яг ЭНЭ хичээлийн мөр · баганын үржвэрийн дотор хийгддэг. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** $(AB)_{ij}$ = $A$-ийн $i$-р мөр · $B$-ийн $j$-р багана. · Хэмжээс: дотоод хэмжээсүүд тэнцүү байж алга болно. · $AB \ne BA$: дарааллыг хэзээ ч чимээгүй бүү соль. |

---

## Lesson 4 — Нэгж матриц ба матрицын зэрэг (`identity-and-powers`)

**concreteComparison**

Тоог 1-ээр үржүүлэхэд юу ч өөрчлөгдөхгүй. Матрицын ертөнцийн 1 бол нэгж матриц
$I$: диагональ дээрээ нэгүүд, бусад газар тэгүүд, $AI = IA = A$ үргэлж. Матрицыг
өөрөөр нь үржүүлэх нь утгатай болсон тул зэрэг ч утгатай болно: $A^2 = AA$, мөн
шалгалтын нуух дуртай хэв маягууд.

**objective**

Нэгж матрицыг хэрэглэж, A² ба A³-ийг бодоод, матрицын зэргийн хэв маягийг
ашиглах.

**concept**

1. **Нэгж матриц** $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ бол
   үржүүлэхэд юу ч хийдэггүй матриц: нийцтэй бүх $A$-ийн хувьд $AI = IA = A$.
   Түүний баганууд нь $(1,0)$ ба $(0,1)$ цэгүүд: юуг ч хөдөлгөдөггүй хувиргалт.
   (ЭШ-ийн бодлогод $E$ гэж тэмдэглэнэ.)

2. **Зэрэг** хуулбаруудыг давхарлана: $A^2 = AA$, $A^3 = A^2A$. Матриц ӨӨРТЭЙГӨӨ
   үргэлж байр солих тул зэргүүд зөв ажиллана: $A^m A^n = A^{m+n}$. (Дарааллыг
   эвддэг нь өөр өөр матрицуудыг холих явдал.)

3. Шалгалтын хэв маягууд: диагональ матрицыг элемент бүрээр нь зэрэгт дэвшүүлнэ:
   $\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}^n = \begin{pmatrix} a^n & 0 \\ 0 & b^n \end{pmatrix}$;
   зарим матриц ДАВТАГДАНА ($90°$-ын эргүүлэлт дөрвөн алхамд $I$ руу буцна:
   $R^4 = I$); зарим нь «үхнэ»: $A^2 = O$ байх тэг биш матриц оршдог. Энэ бол
   тоонд хэзээ ч байгаагүй, зөвхөн матрицад л байдаг үзэгдэл.

**keyIdea**

I бол үржүүлэхийн 1 (AI = IA = A); зэрэг хуулбаруудыг давхарлаж, өөртэйгөө байр
солино; диагональ матрицын зэрэг элемент бүрээр, эргүүлэлт давтагдана.

**facts**

- **title** Нэгж матриц · **latex**
  `I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix},\quad AI = IA = A` ·
  **explanation** Юу ч хийдэггүй хувиргалт; матрицын ертөнцийн 1.
- **title** Диагональ матрицын зэрэг · **latex**
  `\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}^n = \begin{pmatrix} a^n & 0 \\ 0 & b^n \end{pmatrix}`
  · **explanation** Диагональ бол хялбар зам: элементүүд бие даан зэрэгт
  дэвшинэ.
- **title** Давталт · **latex** `R_{90°}^4 = I` · **explanation** Дөрвөн удаа
  дөрөвний нэг эргэлт хийвэл гэртээ ирнэ; эргүүлэлтийн зэрэг 4 үетэйгээр
  давтагдана.

**workedExamples**

- `vm54-we1` — **statement:** $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
  матрицын хувьд $A^2$-г бодоод, $A^3$-ийг таамаглаж, шалгаарай. **solution:**
  $A^2 = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$; буланд хуулбарын тоо
  бичигдэнэ. Үнэхээр $A^3 = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$:
  ерөнхийдөө $A^n$-ийн буланд $n$ байна.
- `vm54-we2` — **statement:**
  $D = \begin{pmatrix} 2 & 0 \\ 0 & -1 \end{pmatrix}$ бол $D^5$-г бодоорой.
  **solution:** Диагональ тул элемент бүрээр зэрэгт дэвшүүлнэ:
  $D^5 = \begin{pmatrix} 32 & 0 \\ 0 & -1 \end{pmatrix}$.
- `vm54-we3` — **statement:**
  $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ ($90°$-ын эргүүлэлт).
  $R^2$-г бодоод, $R^{2026}$-г гаргаарай. **solution:**
  $R^2 = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$ ($180°$-ын
  эргүүлэлт). Тиймээс $R^4 = I$ бөгөөд $2026 = 4 \cdot 506 + 2$:
  $R^{2026} = R^2 = -I$.

**commonMistakes**

- **text** Элемент бүрээр квадрат зэрэгт дэвшүүлэх. · **correction** A² гэдэг нь
  A-г A-ГААР үржүүлэх: бүтэн мөр · баганын үржвэр. Элемент бүрээр дэвшүүлэх
  товчлол зөвхөн диагональ матрицад ажиллана.
- **text** (A + B)² = A² + 2AB + B² гэж задлах. · **correction** Дунд гишүүн нь
  AB + BA бөгөөд ерөнхийдөө тэдгээр ялгаатай. Хоёр гишүүнтийн квадратын томьёо
  байр солих чанар шаарддаг: матрицууд ихэвчлэн татгалзана.

**tryIt**

- `vm54-t1` — **statement:** $\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}^3$-г
  бодоорой. **solution:** $\begin{pmatrix} 27 & 0 \\ 0 & 8 \end{pmatrix}$.
- `vm54-t2` — **statement:** $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$
  матриц $A^2 = O$ нөхцөлийг хангахыг шалгаарай. **solution:** Мөр · багана:
  $A^2$-ийн элемент бүр $0$. Квадрат нь тэг болох тэг биш матриц: тоонууд
  ингэдэггүй.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Матрицын 1 · **title** Юу ч хийдэггүй матриц<br>**body** $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ бүх цэгийг байранд нь үлдээнэ: түүний баганууд нь гэртээ суугаа $(1,0)$ ба $(0,1)$ л. Алгебрын хувьд энэ бол үржүүлэхийн 1: $AI = IA = A$, дараалал хамаагүй ховор үржвэр. |
| 1 | teach | **eyebrow** Зэрэг · **title** Хуулбаруудыг давхарлаж, хэв маяг хай<br>**body** $A^2 = AA$, $A^3 = A^2A$; матриц өөртэйгөө байр солих тул $A^mA^n = A^{m+n}$ аюулгүй. Шалгалтын тоглоом бол хэв маяг хайх: диагональ матрицын зэрэг элемент бүрээр, $90°$-ын эргүүлэлт $R^4 = I$-ээр давтагдана, асар том зэрэг үлдэгдлээр хумигдана.<br>**beats** AI = IA = A · диагональ матриц: элемент бүрийг зэрэгт дэвшүүл · эргүүлэлт давтагдана: R⁴ = I, 4-т хуваасан үлдэгдлийг ашигла |
| 2 | tapQuestion | **eyebrow** 1-ийг шалга · **title** I-ээр үржүүл<br>**prompt** $\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 7 & -2 \\ 3 & 5 \end{pmatrix} = $ ?<br>**explanation** Нэгж матриц юу ч өөрчлөхгүй. Аль ч нүдийг шалгаарай: $I$-ийн 1-р мөр · 1-р багана нь $1 \cdot 7 + 0 \cdot 3 = 7$.<br>**options** `$\begin{pmatrix} 7 & -2 \\ 3 & 5 \end{pmatrix}$` · `$\begin{pmatrix} 7 & 0 \\ 0 & 5 \end{pmatrix}$` · `$I$` · `$\begin{pmatrix} 7 & 3 \\ -2 & 5 \end{pmatrix}$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Тоолдог булан<br>**problemId** `vm54-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Диагональын хөнгөлөлт<br>**problemId** `vm54-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Давталтыг ашигла<br>**prompt** $R$ бол $90°$-ын эргүүлэлтийн матриц, $R^4 = I$. Тэгвэл $R^{101} = $ ?<br>**explanation** $101 = 4 \cdot 25 + 1$ тул $R^{101} = (R^4)^{25}R = R$. Том зэрэг үлдэгдлийн өмнө бууж өгнө.<br>**options** `$R$` · `$I$` · `$R^2$` · `$R^3$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** R-ийн квадрат нь −I<br>**problemId** `vm54-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Мөрөөдөхөөсөө өмнө A²-г бод<br>**body** «A-ийн их зэргийг ол» гэсэн асуулт бүр ижилхэн эхэлнэ: A²-г шударгаар бодоод, түүнийг ХАРААРАЙ. Диагональ уу? I-ийг тоогоор үржүүлсэн үү? A өөрөө юу? Хэв маяг нэг үржүүлэхэд өөрийгөө зарлана. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Кубын зэрэгт диагональ<br>**problemId** `vm54-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Алга болдог квадрат<br>**problemId** `vm54-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Фибоначчи матрицад амьдардаг<br>**body** $\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$ матрицыг зэрэгт дэвшүүлбэл элементүүдэд нь Фибоначчийн тоонууд гарч ирнэ: $A^n$-д $F_{n+1}, F_n, F_{n-1}$ байна. Матрицыг дахин дахин квадрат зэрэгт дэвшүүлбэл мянга дахь Фибоначчийн тоо мянган алхмаар биш, арваад матрицын үржвэрээр гарна. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** $AI = IA = A$: юу ч хийдэггүй хувиргалт. · Диагональ матрицын зэрэг элемент бүрээр; эргүүлэлт давтагдана ($R^4 = I$). · $(A+B)^2 \ne A^2 + 2AB + B^2$: байр солих чанар үнэгүй биш. |

---

## PRACTICE

- `vm5-pr-1` — **statement:**
  $A = \begin{pmatrix} 3 & -2 & 0 \\ 1 & 4 & 7 \end{pmatrix}$ матрицын хэмжээс,
  $a_{13}$ ба $a_{22}$-г олоорой. **solution:** $2 \times 3$; $a_{13} = 0$,
  $a_{22} = 4$.
- `vm5-pr-2` — **statement:**
  $\begin{pmatrix} 2x & 3 \\ 1 & y - 2 \end{pmatrix} = \begin{pmatrix} 8 & 3 \\ 1 & 5 \end{pmatrix}$
  байх $x, y$-г олоорой. **solution:** $x = 4$, $y = 7$.
- `vm5-pr-3` — **statement:**
  $3\begin{pmatrix} 1 & -1 \\ 2 & 0 \end{pmatrix} - 2\begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$-г
  бодоорой. **solution:** $\begin{pmatrix} -1 & -5 \\ 8 & -6 \end{pmatrix}$.
- `vm5-pr-4` — **statement:**
  $\begin{pmatrix} 2 & 1 \\ 3 & 0 \end{pmatrix}\begin{pmatrix} 1 & -2 \\ 4 & 5 \end{pmatrix}$
  үржвэрийг бодоорой. **solution:**
  $\begin{pmatrix} 6 & 1 \\ 3 & -6 \end{pmatrix}$.
- `vm5-pr-5` — **statement:**
  $\begin{pmatrix} 1 & 2 \\ -1 & 3 \end{pmatrix}\begin{pmatrix} 5 \\ -2 \end{pmatrix}$
  үржвэрийг бодоорой. **solution:** $\binom{1}{-11}$.
- `vm5-pr-6` — **statement:** $A$ нь $4 \times 2$, $B$ нь $2 \times 3$
  хэмжээтэй. $AB$ ба $BA$ ямар хэмжээстэй вэ? **solution:** $AB$ нь
  $4 \times 3$; $BA$ оршихгүй ($3 \ne 4$).
- `vm5-pr-7` — **statement:** $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$
  бол $A^2$-г бодоорой. **solution:**
  $\begin{pmatrix} 4 & 4 \\ 0 & 4 \end{pmatrix}$.
- `vm5-pr-8` — **statement:**
  $\begin{pmatrix} -1 & 0 \\ 0 & 3 \end{pmatrix}^4$-г бодоорой. **solution:**
  Диагональ: $\begin{pmatrix} 1 & 0 \\ 0 & 81 \end{pmatrix}$.

---

## TEST YOURSELF

- `vm5-ty-1` — **statement:**
  $\;3X - \begin{pmatrix} 2 & 1 \\ 0 & 4 \end{pmatrix} = \begin{pmatrix} 7 & -4 \\ 6 & 2 \end{pmatrix}$
  тэгшитгэлээс $X$-г олоорой. **solution:**
  $3X = \begin{pmatrix} 9 & -3 \\ 6 & 6 \end{pmatrix}$:
  $X = \begin{pmatrix} 3 & -1 \\ 2 & 2 \end{pmatrix}$.
- `vm5-ty-2` — **statement:**
  $A = \begin{pmatrix} 1 & 0 \\ 2 & 1 \end{pmatrix}$,
  $B = \begin{pmatrix} 1 & 3 \\ 0 & 1 \end{pmatrix}$ бол $AB$ ба $BA$-г хоёуланг
  нь бодоорой. Тэд тэнцүү юү? **solution:**
  $AB = \begin{pmatrix} 1 & 3 \\ 2 & 7 \end{pmatrix}$,
  $BA = \begin{pmatrix} 7 & 3 \\ 2 & 1 \end{pmatrix}$: тэнцүү биш.
- `vm5-ty-3` — **statement:**
  $\begin{pmatrix} 2 & k \\ 1 & 3 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 10 \\ 7 \end{pmatrix}$
  байх $k$-г олоорой. **solution:** Дээд мөр: $2 + 2k = 10$, $k = 4$ (доод
  мөрөөр шалгавал: $1 + 6 = 7$ ✓).
- `vm5-ty-4` — **statement:**
  $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. $R^{50}$-г бодоорой.
  **solution:** $R^4 = I$ ба $50 = 4 \cdot 12 + 2$:
  $R^{50} = R^2 = -I = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}$.
- `vm5-ty-5` — **statement:** $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$
  матрицын хувьд хэв маягийг ашиглан $A^{10}$-г олоорой. **solution:**
  $A^n = \begin{pmatrix} 1 & n \\ 0 & 1 \end{pmatrix}$:
  $A^{10} = \begin{pmatrix} 1 & 10 \\ 0 & 1 \end{pmatrix}$.
- `vm5-ty-6` — **statement:** Зөвхөн нэг элемент:
  $M = \begin{pmatrix} 3 & -1 \\ 2 & 5 \end{pmatrix}$,
  $N = \begin{pmatrix} 0 & 2 \\ 4 & 1 \end{pmatrix}$ бол $(MN)_{21}$-г олоорой.
  **solution:** $M$-ийн 2-р мөр · $N$-ийн 1-р багана:
  $2 \cdot 0 + 5 \cdot 4 = 20$.

---

## Notes for Khas

### 1. Mapping

`lib/esh-course.ts:230` maps this unit to **10.4а–г**, and all four are taught:

- 10.4а (information in matrix form): the sales sheet in `vm51-we3`.
- 10.4б (add, subtract, multiply by a number): lesson 2.
- 10.4в (multiply a matrix by a matrix): lesson 3.
- 10.4г (the zero and identity matrices): lesson 1, concept 3, and lesson 4.

No gaps. 10.4д–е (the 2×2 determinant and inverse) are mapped to unit 6.

### 2. Three overclaims in the English

- **Fibonacci (lesson 4 funFact).** "Fast matrix powering is how computers get
  the trillionth Fibonacci number in microseconds" is false. The trillionth
  Fibonacci number has about 2.09 × 10¹¹ digits: no computer even writes that
  many digits in microseconds. The draft says the thousandth Fibonacci number
  comes from «арваад» (ten-odd) matrix products instead of a thousand steps.
  That is true: 1000 is 1111101000 in binary, so repeated squaring takes nine
  squarings and five further products, fourteen in all. The English wants the
  same fix (ship mode, 6az).
- **AI chips (lesson 3 funFact).** "Judged by one number" becomes "one of the
  main figures". Chips are rated on several figures (memory bandwidth among
  them). The multiply-add rate is the one this lesson explains.
- **Photo blending (lesson 2 funFact).** "At 60 frames a second" becomes
  «секундэд олон удаа». The frame rate belongs to the display, not the blend.

### 3. Terms

- **The identity is $E$ on the exam, $I$ here. This needs a ruling.** The bank
  writes «$E$ нь нэгж матриц» in four questions and $A^3 = pA + qE$ in four
  more. It never uses $I$ for the identity. $E$ is the convention in Mongolian
  schools, as in Russian ones. The draft keeps $I$, because the maths and the
  tapQuestion options match the English. It glosses $E$ twice: lesson 1, concept
  3, and lesson 4, concept 1. The other option is to write $E$ throughout the
  Mongolian: $E$, $AE = EA = A$, $R^4 = E$. A rewrite may change the maths
  strings, since the walker swaps whole strings. My lean is **$E$**, for an
  exam-first course. Units 6 and 7 face the same choice, because the bank's
  inverse questions use $E$ too.
- **«тоогоор үржүүлэх»** (scalar multiplication): the ministry's own phrase
  (10.4б). «скаляраар үржүүлэх» is avoided on purpose. «скаляр үржвэр» is the
  dot product (unit 3), and the two would collide.
- **«хэмжээс»** (dimension): the ministry writes «2x2 хэмжээстэй», the bank
  «хэмжээсийг» and «хэмжээтэй». The draft uses «2 × 3 хэмжээтэй матриц» and the
  noun «хэмжээс».
- **«байр солих чанар»** (commutativity): the standard school phrase. It is in
  neither the ministry text nor the bank.
- **«гар барих»** (the "handshake" rule for dimensions): an image, not a term.
- **«тэг матриц»**: the ministry's word (10.4г); the bank never uses it.

### 4. Course framing

"The transformations chapter" (lesson 3, the concreteComparison and `vm53-we3`)
is the geometry course's `transformations` topic. That topic does teach matrix ×
point: `geometry-transformations` draft, lines 639–659. The draft names it
«Хувиргалт» сэдэв.

The English opens lesson 3 with "You already own the engine". On the ЭШ spine
that is not safe. The spine's own transformations unit
(`transformation-matrices`) is unit 7, after this one, and an ЭШ student need
not have taken the geometry course. The draft makes the claim conditional:
«Геометрийн «Хувиргалт» сэдвийг үзсэн бол…». Teach step 0 states the matrix ×
point handshake instead of assuming it. `vm53-we3` teaches matrix × column in
full anyway, so nothing is missing; only the "you've seen this" claim was
unsafe.

### 5. Decimals

**0** inside `$...$`. One in prose: lesson 2's "1.1" (the 10% price rise)
becomes «1,1». 2d stays at **1,567** across seventy-two drafts.
