# Draft — `vectors-matrices/determinants-and-inverses`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**ЭШ Вектор ба матриц, unit 6 of 8.** Both spines number this unit 6. "Unit 5"
in `buildsOn` keeps its number. "Unit 1", used twice, becomes «Вектор ба
координат» нэгж, by name (6aw). The English calls this unit "the capstone", but
two units follow it in both spines (Notes 4).

**Four lessons, 34 items, 49 interactive steps, no nested tryItSet problems.**
(12 workedExamples + 8 tryIt + 8 practice + 6 testYourself.)

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. No em-dash parentheticals (§9), decimal comma in prose
(§7), hyphenated case suffixes (§8), condition before thing (§1). Objectives as
plain text (6d). Imperatives soft in prose that addresses the student, bare in
beats, recaps, titles and fact shorthand. Vector coordinates keep the comma, as
in the bank. The identity stays $I$, pending the ruling in 6az.

**Mirror pre-check** (6q): no `vectors-matrices-mn` mirror. Draft it.

**Ministry sections read in full first**: 10.4, 11.2. The unit is mapped
(`lib/esh-course.ts:231`) to **10.4д, 10.4е, 11.2в**; all three are taught.

**Exam check** (6m): «тодорхойлогч» 6 in the bank, «урвуу матриц» 2, «урвуугүй»
5, «системийн матриц» 4, «тэгш хэмтэй хувирах / хувиргах» 23, «эргүүлэлт» 16,
«Крамер» 0. **«Кэйли-Гамильтоны теорем» 8**: every 2023 and 2024 variant has
one, and no unit teaches it (Notes 2).

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| determinant | **тодорхойлогч** | ministry 10.4д, 11.2д · bank 6 · `geometry-transformations` |
| inverse matrix | **урвуу матриц** | ministry 10.4е, 11.2в · bank 2 |
| singular (no inverse) | **урвуугүй матриц** | bank 5 («матриц урвуугүй байх») |
| anti-diagonal | **туслах диагональ** | Notes 3 |
| coefficient matrix | **системийн матриц** | bank 4 |
| Cramer's rule | **Крамерын дүрэм** | ministry 11.2е |
| Gaussian elimination | **Гауссын арга** | ministry 11.2г |
| reflection (in a line) | **тэгш хэмтэй хувиргалт** | bank 23 · ministry; Notes 3 |
| composition | **угсраа хувиргалт** | as in `geometry-transformations` |
| orientation | **чиглэл** (чиглэл эсрэгээр солигдоно) | as in `geometry-transformations` |
| area scale factor | **талбайн масштабын коэффициент** | glossary «масштабын коэффициент» |

---

## Topic-level strings

**TITLE:** Тодорхойлогч, урвуу матриц ба систем

**BLURB:** ad − bc тодорхойлогч, 2×2 хэмжээстэй матрицын урвуу, тэгшитгэлийн
системийг матрицаар болон Крамерын дүрмээр бодох, мөн матрицыг хувиргалт гэж
унших.

**buildsOn:** Матрицыг матрицаар үржүүлэх (5-р нэгж) ба Геометрийн хичээлийн
хувиргалтын матрицууд.

---

## Lesson 1 — Тодорхойлогч (`the-determinant`)

**concreteComparison**

$2 \times 2$ хэмжээстэй матриц бүр гурван асуултад нэг дор хариулдаг нэг тоог
нууж байдаг: матриц урвуутай юу, талбайг хэд дахин өөрчлөх вэ, баганууд нь нэг
шулууны дагуу чиглэсэн үү? Тэр тоо бол тодорхойлогч, $ad - bc$: хөндлөн
үржүүлээд, хасна.

**objective**

2×2 хэмжээстэй матрицын тодорхойлогчийг бодож, түүнийг талбайн масштабын
коэффициент гэж тайлбарлаад, det = 0 нөхцөлийг урвуугүй байх, баганууд коллинеар
байх шалгуур болгон хэрэглэх.

**concept**

1. $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ матрицын хувьд:
   $$\det A = ad - bc$$ гол диагоналийн үржвэрээс туслах диагоналийн үржвэрийг
   хасна. Нэг хөндлөн үржүүлэлт, нэг тоо.

2. **Геометр утга**: $A$ матрицаар хувиргасан аливаа дүрсийн талбай $|\det A|$
   дахин өөрчлөгдөнө. Тодорхойлогч $6$ бол талбай зургаа дахин өснө; $\pm 1$ бол
   хатуу хөдөлгөөн (эргүүлэлт, тэгш хэмтэй хувиргалт); СӨРӨГ тэмдэг хавтгайн
   чиглэл эсрэгээр солигдсоныг хэлнэ.

3. $\det A = 0$ бол үхлийн гэрчилгээ: баганууд коллинеар (ганцхан шулууны
   чиглэл), бүх талбай тэг болж хумигдана, мөн дараагийн хичээлийн гол санаа
   болох урвуу матриц оршихгүй. «Вектор ба координат» нэгжтэй холбоог
   анзаараарай: $ad - bc = 0$ бол яг $(a, c)$ ба $(b, d)$ баганууд коллинеар
   байх хөндлөн шалгуур.

**keyIdea**

det = ad − bc: талбайн масштабын коэффициент (тэмдэг нь чиглэл солигдсоныг
заана); det = 0 ⇔ баганууд коллинеар ⇔ урвуу матриц байхгүй.

**facts**

- **title** Томьёо · **latex**
  `\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc` · **explanation**
  Гол диагоналиас туслах диагоналийг хас.
- **title** Талбайн коэффициент · **latex**
  `\text{талбайн коэффициент} = |\det A|` · **explanation** Сөрөг тодорхойлогч:
  чиглэл солигдоно, талбайн коэффициент ижил.
- **title** Урвуугүй · **latex**
  `\det A = 0 \iff \text{баганууд коллинеар} \iff \text{урвуу матриц байхгүй}` ·
  **explanation** Бүгдийг өөрчилдөг тэг.

**workedExamples**

- `vm61-we1` — **statement:**
  $\det\begin{pmatrix} 3 & 5 \\ 1 & 4 \end{pmatrix}$-г бодоорой. **solution:**
  $3 \cdot 4 - 5 \cdot 1 = 7$.
- `vm61-we2` — **statement:** $9$ талбайтай гурвалжныг
  $M = \begin{pmatrix} 2 & 1 \\ 3 & 4 \end{pmatrix}$ матрицаар хувиргав. Дүрсийн
  талбайг олоорой. **solution:** $\det M = 8 - 3 = 5$; дүрсийн талбай
  $|5| \cdot 9 = 45$.
- `vm61-we3` — **statement:** $k$-ийн ямар утгад
  $\begin{pmatrix} 2 & k \\ 3 & 6 \end{pmatrix}$ матриц урвуугүй (тодорхойлогч
  нь тэг) байх вэ? **solution:** $12 - 3k = 0$ тул $k = 4$. $k = 4$ үеийн
  багануудыг шалгавал: $(2, 3)$ ба $(4, 6)$ коллинеар, урвуугүй байх нөхцөл яг
  үүнийг шаардана.

**commonMistakes**

- **text** Хасахын оронд нэмэх: ad + bc. · **correction** Туслах диагональ
  ХАСАГДАНА: ad − bc. Нэмэх тэмдэгтэй бол тэг тодорхойлогчийн шалгуур ч, урвуу
  матриц ч бүгд чимээгүй эвдэрнэ.
- **text** Талбайд абсолют утгыг мартах. · **correction** det = −3 бол талбай −3
  биш, 3 дахин өөрчлөгдөнө. Тэмдэг нь чиглэлийг (тэгш хэмтэй хувиргалт орсныг)
  хэлнэ, сөрөг талбай хэзээ ч биш.

**tryIt**

- `vm61-t1` — **statement:**
  $\det\begin{pmatrix} 7 & 2 \\ 3 & 1 \end{pmatrix}$-г бодоорой. **solution:**
  $7 - 6 = 1$: энэ матриц талбайг хадгална.
- `vm61-t2` — **statement:** $m$-ийн ямар утгад
  $\begin{pmatrix} m & 3 \\ 4 & m \end{pmatrix}$ матрицын тодорхойлогч тэг байх
  вэ? **solution:** $m^2 - 12 = 0$: $m = \pm 2\sqrt{3}$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Нэг тоо · **title** Хөндлөн үржүүлэлт<br>**body** $$\det\begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - bc$$ Гол диагоналийг үржүүлж, туслах диагоналийг үржүүлж, хасна. Арван секундийн арифметик, гэхдээ матриц урвуутай эсэх, талбай хэрхэн өөрчлөгдөх, баганууд нэг шулуун дээр буусан эсэхийг бүгдийг нь хэлнэ. |
| 1 | teach | **eyebrow** Гурван унших арга · **title** Талбай, чиглэл, амь нас<br>**body** Нэгдүгээрт: талбай $|\det|$ дахин өөрчлөгдөнө (Геометрийн «Хувиргалтын матриц» хичээлийг үзсэн бол танил санаа). Хоёрдугаарт: сөрөг тодорхойлогч хавтгайн чиглэл эсрэгээр солигдсоныг хэлнэ. Гуравдугаарт: $\det = 0$ бол баганууд коллинеар: хавтгай шулуун болж хумигдаж, талбай үхэж, үүнийг буцаах урвуу матриц хэзээ ч олдохгүй.<br>**beats** det = ad − bc · |det| = талбайн коэффициент; тэмдэг = чиглэл · det = 0: баганууд коллинеар, урвуу матриц байхгүй |
| 2 | tapQuestion | **eyebrow** Хөндлөн үржүүлэлтийг шалга · **title** Нэгийг бод<br>**prompt** $\det\begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix} = $ ?<br>**explanation** $15 - 14 = 1$. ($29$ бол нэмэх тэмдгийн занга: $15 + 14$.)<br>**options** `$1$` · `$29$` · `$-1$` · `$11$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Арван секунд<br>**problemId** `vm61-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Талбайн үнэ<br>**problemId** `vm61-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Тэмдгийг унш<br>**prompt** Хувиргалтын тодорхойлогч $-2$. Энэ хувиргалт…<br>**explanation** Талбайн коэффициент $|-2| = 2$; сөрөг тэмдэг чиглэл солигдсоныг хэлнэ: дотор нь хаа нэгтээ тэгш хэмтэй хувиргалт нуугдаж байна.<br>**options** `талбайг хоёр дахин ихэсгэж, чиглэлийг солино` · `талбайг багасгаж, чиглэлийг солино` · `талбайг хоёр дахин ихэсгэнэ, чиглэл солигдохгүй` · `урвуугүй` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** k-г тэг рүү тааруулах<br>**problemId** `vm61-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** det = 0 асуулт бол коллинеар байдлын асуулт<br>**body** «$k$-ийн ямар утгад матриц урвуугүй вэ?» гэдэг бол «Вектор ба координат» нэгжийн коллинеар шалгуур, өөр хувцастай. ad − bc = 0 гэж тавибал та багануудыг хөндлөн үржүүлж байна. Ижил рефлекс, шинэ үгс. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Талбай хадгалагч<br>**problemId** `vm61-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Квадрат тэгшитгэлээр урвуугүй<br>**problemId** `vm61-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Тодорхойлогч түрүүлж иржээ<br>**body** Тодорхойлогчийг Японд Сэки, Европт Лейбниц хоёулаа 1680-аад онд судалжээ: матриц нэрээ авахаас бараг 170 жилийн ӨМНӨ. Тоо нь тэгтлээ хэрэгтэй байсан тул түүнийг хадгалах хүснэгтийг зохиосон хэрэг. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** $\det = ad - bc$: хөндлөн үржүүлээд, хас. · $|\det|$ талбайг өөрчилнө; сөрөг бол чиглэл солигдоно. · $\det = 0$: баганууд коллинеар, урвуу матриц байхгүй. |

---

## Lesson 2 — Урвуу матриц (`the-inverse-matrix`)

**concreteComparison**

Хийсэн бүхнийг буцааж болно, хэрэв азтай бол. $A$-г буцаах матриц бол түүний
урвуу $A^{-1}$: хоёуланг нь хэрэглэвэл юу ч хийгээгүйтэй адил, $AA^{-1} = I$.
2×2 хэмжээстэй матрицад бэлэн жор бий (байрыг соль, тэмдгийг өөрчил,
тодорхойлогчид хуваа), азыг тань тодорхойлогч шийднэ: $\det = 0$ бол буцаах арга
байхгүй.

**objective**

2×2 хэмжээстэй матрицын урвууг «байр соль, тэмдэг өөрчил, хуваа» жороор олж,
AA⁻¹ = I-ээр шалгаад, det ≠ 0 нөхцөлийг урвуу матриц оршин байх шалгуур болгон
хэрэглэх.

**concept**

1. Жор:
   $$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$
   гол диагоналийн элементүүдийн БАЙРЫГ СОЛЬ, туслах диагоналийн элементүүдийн
   ТЭМДГИЙГ ӨӨРЧИЛ, тодорхойлогчид ХУВАА.

2. Урвуу матриц яг $\det A \ne 0$ үед оршино. Урвуугүй матриц хавтгайг шулуун
   болгон хумина: мэдээлэл устаж, ямар ч матриц түүнийг сэргээж чадахгүй.

3. Шалгалт бол нэг үржүүлэлт: $AA^{-1}$ нь $I$-тэй тэнцүү байх ёстой (мөн
   $A^{-1}A = I$: урвуу матриц бол дарааллын түгшүүрийн үл хамаарах тохиолдол).
   Шалгалтад шалгах алхмыг үргэлж хийгээрэй: арван таван секундэд урвууг «зөв
   байх гэж найдсан»-аас «зөв нь батлагдсан» болгоно.

**keyIdea**

A⁻¹-г олохдоо гол диагоналийн байрыг сольж, туслах диагоналийн тэмдгийг
өөрчлөөд, det-д хуваана; оршино ⇔ det ≠ 0; AA⁻¹ = I-ээр шалгана.

**facts**

- **title** Жор · **latex**
  `A^{-1} = \frac{1}{ad-bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}` ·
  **explanation** Байрыг соль, тэмдгийг өөрчил, det-д хуваа.
- **title** Оршин байх · **latex** `A^{-1} \text{ оршино} \iff \det A \ne 0` ·
  **explanation** Хумигдсан хавтгайг дахин дэлгэх боломжгүй.
- **title** Шалгалт · **latex** `AA^{-1} = A^{-1}A = I` · **explanation**
  Тодорхойлолт, мөн таны арван таван секундийн баталгаа.

**workedExamples**

- `vm62-we1` — **statement:** $A = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$
  матрицын урвууг олоорой. **solution:** $\det A = 6 - 5 = 1$. Байр соль, тэмдэг
  өөрчил, хуваа: $A^{-1} = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$.
  $AA^{-1}$-ийн нэг нүдийг шалгавал: $3 \cdot 2 + 5 \cdot (-1) = 1$ ✓.
- `vm62-we2` — **statement:** $B = \begin{pmatrix} 4 & 7 \\ 1 & 2 \end{pmatrix}$
  матрицын урвууг олоорой. **solution:** $\det B = 8 - 7 = 1$:
  $B^{-1} = \begin{pmatrix} 2 & -7 \\ -1 & 4 \end{pmatrix}$.
- `vm62-we3` — **statement:** $C = \begin{pmatrix} 2 & 6 \\ 3 & 9 \end{pmatrix}$
  матриц урвуутай юу? Бодоод, геометрээр тайлбарлаарай. **solution:**
  $\det C = 18 - 18 = 0$: урвуу матриц байхгүй. Геометрээр: $(2,3)$ ба $(6,9)$
  баганууд коллинеар тул $C$ бүх хавтгайг тэр шулуун дээр хавтгайруулна;
  хавтгайруулснаа буцааж болохгүй.

**commonMistakes**

- **text** Туслах диагоналийн байрыг сольж, гол диагоналийн тэмдгийг өөрчлөх. ·
  **correction** a ба d-гийн (гол диагональ) БАЙРЫГ СОЛЬ; b ба c-гийн (туслах
  диагональ) ТЭМДГИЙГ ӨӨРЧИЛ. AA⁻¹ = I-г нэг удаа шалгавал андуурал тэр дороо
  илэрнэ.
- **text** Тодорхойлогчид хуваахаа мартах. · **correction** 1/det үржигдэхүүнгүй
  бол AA⁻¹ нь I биш, det·I болно. det = 1 бол танд аз таарсан; бусад тохиолдолд
  хариу чинь масштаб алдсан хог.

**tryIt**

- `vm62-t1` — **statement:** $\begin{pmatrix} 2 & 1 \\ 5 & 3 \end{pmatrix}$
  матрицын урвууг олоорой. **solution:** $\det = 1$: урвуу нь
  $\begin{pmatrix} 3 & -1 \\ -5 & 2 \end{pmatrix}$.
- `vm62-t2` — **statement:** $\begin{pmatrix} 4 & 2 \\ 3 & 2 \end{pmatrix}$
  матрицын урвууг олоорой. **solution:** $\det = 2$: урвуу нь
  $\frac{1}{2}\begin{pmatrix} 2 & -2 \\ -3 & 4 \end{pmatrix} = \begin{pmatrix} 1 & -1 \\ -3/2 & 2 \end{pmatrix}$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Буцаах · **title** AA⁻¹ = I<br>**body** $A$-гийн урвуу бол түүнийг буцаадаг матриц: $A$-г, дараа нь $A^{-1}$-г хэрэглэвэл цэг бүр гэртээ буцаж ирнэ, $AA^{-1} = I$. Матрицын тэгшитгэл бодох, хувиргалтыг тайлах, систем бодох: бүгд урвуу матрицаар дамжина. |
| 1 | teach | **eyebrow** Жор · **title** Байр соль, тэмдэг өөрчил, хуваа<br>**body** $$A^{-1} = \frac{1}{ad - bc}\begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$ Гол диагоналийн байрыг сольж, туслах диагоналийн тэмдгийг өөрчлөөд, бүгдийг тодорхойлогчид хуваагаарай. Тодорхойлогч бол хаалганы манаач: $\det = 0$ бол хавтгай шулуун болж хумигдсан, түүнийг юу ч дэлгэж чадахгүй, урвуу матриц байхгүй.<br>**beats** a↔d байрыг соль, b ба c-гийн тэмдгийг өөрчил · det-д хуваа · det = 0 → урвуу матриц байхгүй, цэг |
| 2 | tapQuestion | **eyebrow** Жорыг шалга · **title** Хуваахаас өмнө<br>**prompt** $A = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$ ($\det = 1$) бол $A^{-1} = $ ?<br>**explanation** $5$ ба $2$-ын байрыг сольж, $3$-уудын тэмдгийг өөрчлөөд, $1$-д хуваана. Шуурхай шалгалт: $5 \cdot 2 + 3 \cdot (-3) = 1$ ✓.<br>**options** `$\begin{pmatrix} 2 & -3 \\ -3 & 5 \end{pmatrix}$` · `$\begin{pmatrix} 5 & -3 \\ -3 & 2 \end{pmatrix}$` · `$\begin{pmatrix} -2 & 3 \\ 3 & -5 \end{pmatrix}$` · `$\begin{pmatrix} 2 & 3 \\ 3 & 5 \end{pmatrix}$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** det = 1-ийн хөнгөлөлт<br>**problemId** `vm62-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Бас нэг цэвэрхэн жишээ<br>**problemId** `vm62-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Хаалганы манаач<br>**prompt** Аль матриц урвуугүй вэ?<br>**explanation** $3 \cdot 4 - 6 \cdot 2 = 0$: урвуугүй. (Түүний $(3,2)$ ба $(6,4)$ баганууд коллинеар.) Бусдынх нь тодорхойлогч $3$, $1$, $-1$: амьд.<br>**options** `$\begin{pmatrix} 3 & 6 \\ 2 & 4 \end{pmatrix}$` · `$\begin{pmatrix} 3 & 6 \\ 2 & 5 \end{pmatrix}$` · `$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$` · `$\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Буцаах арга үхэх үед<br>**problemId** `vm62-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** AA⁻¹-д 15 секунд зарцуул<br>**body** Урвууг олсныхоо дараа буцааж үржүүлээрэй. Яарч байвал зөвхөн зүүн дээд нүдийг: тэр нь 1 байх ёстой. Байр солих, тэмдэг өөрчлөх, хуваах алдаа бүр тэр ганц тоонд баригдана. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** det = 1 тохиолдол<br>**problemId** `vm62-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** 2-т хуваа<br>**problemId** `vm62-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Том матриц, ижил түүх<br>**body** 3×3 ба түүнээс том матрицууд ч урвуутай. Тэдгээрийг ихэвчлэн цэвэрхэн жороор биш, Гауссын аргаар олдог. Харин хаалганы манаач хэзээ ч өөрчлөгдөхгүй: ямар ч хэмжээст det ≠ 0, үүрд. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Гол диагоналийн байрыг соль, туслах диагоналийн тэмдгийг өөрчил, det-д хуваа. · Оршино ⇔ $\det \ne 0$. · Шалга: $AA^{-1} = I$: арван таван секунд, бүрэн итгэл. |

---

## Lesson 3 — Системийг матрицаар бодох (`solving-systems-with-matrices`)

**concreteComparison**

$\begin{cases} 3x + 5y = 1 \\ x + 2y = 0 \end{cases}$ систем нууцаар нэг
матрицын тэгшитгэл: $A\binom{x}{y} = \binom{1}{0}$. Матрицын тэгшитгэлийг нэг
нүүдлээр боддог: хоёр талыг нь $A^{-1}$-ээр үржүүлнэ. Хоёр тэгшитгэл, хоёр үл
мэдэгдэгч: нэг урвуу матриц.

**objective**

2×2 системийг AX = B хэлбэрт бичиж, X = A⁻¹B-ээр бодоод, Крамерын дүрмийг
тодорхойлогчийн товчлол болгон хэрэглэх.

**concept**

1. Хоёр үл мэдэгдэгчтэй аливаа шугаман систем $AX = B$ хэлбэрт багцлагдана:
   коэффициентүүд $A$-д, үл мэдэгдэгчид $X$ баганад, сул гишүүд $B$-д. Хоёр
   талыг $A^{-1}$-ээр ЗҮҮН талаас нь үржүүлээрэй (дараалал ариун):
   $$X = A^{-1}B.$$

2. **Крамерын дүрэм** бол урвуу матрицыг урьдчилан тодорхойлогч болгон зажилсан
   ижил шийд:
   $$x = \frac{\det A_x}{\det A}, \qquad y = \frac{\det A_y}{\det A},$$ энд
   $A_x$ бол $A$-гийн ЭХНИЙ баганыг $B$-ээр сольсон матриц, $A_y$ нь хоёр дахь
   баганыг сольсон матриц. Гурван хөндлөн үржүүлэлт, болоо.

3. $\det A = 0$ бол доройтлын дохио: систем цор ганц шийдгүй. Эсвэл шийдгүй
   (параллель шулуунууд), эсвэл төгсгөлгүй олон шийдтэй (нэг шулуун хоёр удаа).
   Хоёр хичээлийн өмнө сурсан тодорхойлогч яг «энэ систем зөв ажиллах уу?» гэсэн
   шалгуур.

**keyIdea**

Систем = AX = B; X = A⁻¹B-ээр, эсвэл Крамерын дүрмээр бодно: x = det Aₓ/det A,
y = det A_y/det A; det = 0 бол цор ганц шийд байхгүй.

**facts**

- **title** Матриц хэлбэр · **latex** `AX = B \;\Rightarrow\; X = A^{-1}B` ·
  **explanation** Урвуу матрицаар зүүн талаас үржүүл.
- **title** Крамерын дүрэм · **latex**
  `x = \frac{\det A_x}{\det A},\; y = \frac{\det A_y}{\det A}` · **explanation**
  Нэг баганыг B-ээр соль, хөндлөн үржүүл, хуваа.
- **title** Доройтол · **latex**
  `\det A = 0 \Rightarrow \text{цор ганц шийд байхгүй}` · **explanation**
  Параллель эсвэл давхцсан шулуунууд: тодорхойлогч түрүүлж анхааруулна.

**workedExamples**

- `vm63-we1` — **statement:** Урвуу матрицаар бодоорой:
  $\begin{cases} 3x + 5y = 1 \\ x + 2y = 0 \end{cases}$ **solution:**
  $A = \begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}$, $\det = 1$,
  $A^{-1} = \begin{pmatrix} 2 & -5 \\ -1 & 3 \end{pmatrix}$.
  $X = A^{-1}\binom{1}{0} = \binom{2}{-1}$: $x = 2$, $y = -1$. Шалгалт:
  $3(2) + 5(-1) = 1$ ✓.
- `vm63-we2` — **statement:** Крамерын дүрмээр бодоорой:
  $\begin{cases} 2x + y = 7 \\ x - 3y = -7 \end{cases}$ **solution:**
  $\det A = -6 - 1 = -7$.
  $\det A_x = \det\begin{pmatrix} 7 & 1 \\ -7 & -3 \end{pmatrix} = -21 + 7 = -14$:
  $x = 2$.
  $\det A_y = \det\begin{pmatrix} 2 & 7 \\ 1 & -7 \end{pmatrix} = -14 - 7 = -21$:
  $y = 3$.
- `vm63-we3` — **statement:** $k$-ийн ямар утгад
  $\begin{cases} 2x + 3y = 5 \\ 4x + ky = 7 \end{cases}$ систем цор ганц шийдгүй
  болох вэ? **solution:** $\det A = 2k - 12 = 0$ тул $k = 6$. Тэр үед зүүн
  талууд пропорциональ ($4x + 6y = 2(2x + 3y)$), харин баруун талууд
  пропорциональ биш ($7 \ne 10$): параллель шулуунууд, шийд огт байхгүй.

**commonMistakes**

- **text** A⁻¹-ээр буруу талаас үржүүлэх. · **correction** AX = B тэгшитгэлийн
  хоёр талыг A⁻¹-ээр ЗҮҮН талаас нь үржүүлнэ: X = A⁻¹B. BA⁻¹ гэж бичвэл өөр
  үржвэр (оршин байсан ч гэсэн) гарна: дараалал чухал хэвээр.
- **text** Крамерын дүрэмд буруу баганыг солих. · **correction** x-ийн хувьд
  x-ийн БАГАНЫГ (эхнийх) B-ээр, y-ийн хувьд хоёр дахийг нь сольно. Солиод хийвэл
  хоёр хариу байраа солино: үнэмшилтэй харагдах ч буруу.

**tryIt**

- `vm63-t1` — **statement:** Крамерын дүрмээр бодоорой:
  $\begin{cases} x + y = 5 \\ 2x - y = 1 \end{cases}$ **solution:**
  $\det A = -1 - 2 = -3$; $\det A_x = -5 - 1 = -6$: $x = 2$;
  $\det A_y = 1 - 10 = -9$: $y = 3$.
- `vm63-t2` — **statement:** $m$-ийн ямар утгад
  $\begin{cases} 3x + my = 1 \\ 6x + 8y = 5 \end{cases}$ систем цор ганц шийдээ
  алдах вэ? **solution:** $24 - 6m = 0$: $m = 4$.

### Interactive — 13 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Дахин багцлах · **title** Хоёр тэгшитгэл, нэг тэгшитгэл<br>**body** $\begin{cases} 3x + 5y = 1 \\ x + 2y = 0 \end{cases}$ бол $\begin{pmatrix} 3 & 5 \\ 1 & 2 \end{pmatrix}\binom{x}{y} = \binom{1}{0}$: коэффициентүүд, үл мэдэгдэгчид, сул гишүүд: $AX = B$. Хоёр тоон тэгшитгэлийн оронд нэг матрицын тэгшитгэл, мөн одоо матрицын хэрэгслүүд хэрэглэгдэнэ. |
| 1 | systemGraph | **eyebrow** Системийг хар · **title** Хоёр шулуун, нэг огтлолцол<br>**teach** Тэгшитгэл бүр нэг шулуун; шийд нь тэдгээрийн огтлолцох цэг. Хоёр дахь шулууныг хөдөлгөж үзээрэй: налалтууд тэнцүү болмогц огтлолцол төгсгөлгүйд зугтана: яг тэр үед системийн матрицын тодорхойлогч тэг болно. Алгебрын det = 0 ба геометрийн параллель шулуунууд бол нэг л үзэгдэл.<br>**config** unchanged |
| 2 | teach | **eyebrow** Хоёр арга · **title** Урвуу матриц уу, Крамер уу<br>**body** Нэгдүгээр арга: $X = A^{-1}B$: нэг урвуу матриц, нэг үржүүлэлт. Хоёрдугаар арга, **Крамерын дүрэм**: $x = \frac{\det A_x}{\det A}$, $y = \frac{\det A_y}{\det A}$, энд $A_x$ нь $B$-г эхний баганад, $A_y$ нь хоёр дахь баганад оруулсан матриц. Нийт гурван хөндлөн үржүүлэлт: шалгалтын хамгийн хурдан зам.<br>**beats** X = A⁻¹B: урвуу матриц ЗҮҮН талд · Крамер: нэг баганыг B-ээр соль, тодорхойлогчдыг хуваа · det A = 0 → цор ганц шийд байхгүй |
| 3 | tapQuestion | **eyebrow** Бичлэгийг шалга · **title** Багцал<br>**prompt** $\begin{cases} 4x - y = 6 \\ 2x + 3y = 8 \end{cases}$ системийн матриц нь…<br>**explanation** Мөрүүд тэгшитгэлүүдийг тэмдэгтэй нь давтана: эхлээд $(4, -1)$, дараа нь $(2, 3)$. (Хоёр дахь хувилбар бол мөр, баганыг нь сольсон матриц: багцлахдаа гаргадаг сонгодог алдаа.)<br>**options** `$\begin{pmatrix} 4 & -1 \\ 2 & 3 \end{pmatrix}$` · `$\begin{pmatrix} 4 & 2 \\ -1 & 3 \end{pmatrix}$` · `$\begin{pmatrix} 6 \\ 8 \end{pmatrix}$` · `$\begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix}$` — **correctIndex 0** |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Урвуу матрицаар<br>**problemId** `vm63-we1` |
| 5 | worked | **eyebrow** Бодсон жишээ · **title** Крамерын дүрмээр<br>**problemId** `vm63-we2` |
| 6 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Крамер, нэг хувьсагч<br>**prompt** $\begin{cases} x + 2y = 4 \\ 3x + 4y = 10 \end{cases}$ системийн хувьд Крамерын дүрмээр $x = $ ?<br>**explanation** $\det A = 4 - 6 = -2$; $\det A_x = 16 - 20 = -4$; $x = \frac{-4}{-2} = 2$.<br>**options** `$2$` · `$1$` · `$4$` · `$-2$` — **correctIndex 0** |
| 7 | worked | **eyebrow** Бодсон жишээ · **title** Цор ганц шийд үхэх үед<br>**problemId** `vm63-we3` |
| 8 | tip | **eyebrow** Шалгалтын дадал · **title** Хариугаа буцааж орлуул<br>**body** Ямар ч аргаар бодсон бай, (x, y)-г АНХНЫ тэгшитгэлүүдэд орлуулаарай. Арван секунд «магадгүй зөв»-ийг «шалгагдсан» болгоно: шалгалт Крамерын дүрмийн тэмдгийн шалгагдаагүй алдааг өршөөлгүй шийтгэдэг. |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Нэгийг хурдан бод<br>**problemId** `vm63-t1` |
| 10 | tryIt | **eyebrow** Туршаад үз · **title** Цор ганц шийдийг эвд<br>**problemId** `vm63-t2` |
| 11 | funFact | **eyebrow** Сонирхолтой баримт · **title** Крамерын дүрэм томордоггүй<br>**body** Крамер дүрмээ 1750 онд нийтэлсэн бөгөөд 2×2 системд гоё. Харин тодорхойлогч бүрийг сурах бичгийн томьёогоор задалбал 20 хувьсагчтай системд дэлхийн элсний ширхгээс олон үйлдэл шаардана. Жинхэнэ программууд Гауссын аргыг хэрэглэдэг; Крамер бол шалгалтын халаасны хутга. |
| 12 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Багцал: $AX = B$; бод: $X = A^{-1}B$ (урвуу матриц зүүн талд). · Крамер: нэг баганыг $B$-ээр соль, тодорхойлогчдыг хуваа. · $\det A = 0$: параллель эсвэл давхцсан шулуунууд, цор ганц шийд байхгүй. |

---

## Lesson 4 — Матриц хувиргалт болох нь (`matrices-as-transformations`)

**concreteComparison**

Бүх санаа энд нийлнэ: матриц бол хавтгайн ХУВИРГАЛТ (баганууд нь нэгж цэгүүд
хаашаа очихыг хэлнэ), үржүүлэх бол УГСРАА хувиргалт (нэгийг, дараа нь нөгөөг
хийнэ), тодорхойлогч бол талбайн тайлан, урвуу матриц бол буцаах үйлдэл. Нэг
объект, дөрвөн унших арга: матрицын шалгалтын асуулт бүр эдгээрийн аль нэгэнд
амьдардаг.

**objective**

Дөрвөн унших аргын хооронд чөлөөтэй шилжих: матриц бол хувиргалт, үржвэр бол
угсраа хувиргалт, тодорхойлогч бол талбайн коэффициент, урвуу матриц бол буцаах
үйлдэл.

**concept**

1. **Баганууд = очих газрууд.** Матрицын эхний багана $(1, 0)$ цэг хаана буухыг,
   хоёр дахь нь $(0, 1)$ хаана буухыг хэлнэ. Аль ч хувиргалтын матрицыг хоёр
   нэгж цэгээс хаашаа очихыг нь асууж байгуулаарай. Геометрийн «Хувиргалтын
   матриц» хичээлийг үзсэн бол энэ бол тэр санаа, одоо бүрэн хэрэгсэлтэйгээ.

2. **Үржвэр = угсраа хувиргалт, баруунаас зүүн тийш.** $BA$ гэдэг нь «эхлээд
   $A$-г, дараа нь $B$-г хэрэглэ» гэсэн үг: цэгт хамгийн ойр матриц түрүүлж
   үйлчилнэ. Байр солих чанаргүй байх нь геометрт үйлдлийн дараалал чухал
   гэдгийн л илэрхийлэл.

3. **Тодорхойлогч = талбайн коэффициент; урвуу матриц = буцаах.** $|\det|$
   талбайг үнэлж, тэмдэг нь чиглэл солигдсоныг хэлнэ; $A^{-1}$ хувиргалтыг
   буцаана (юу ч хавтгайрч хумигдаагүй үед л оршино). Угсраа хувиргалтад
   тодорхойлогчид үржигдэнэ: $\det(BA) = \det B \cdot \det A$: алхам бүрд буцаах
   боломж өвлөгдөнө эсвэл алдагдана.

**keyIdea**

Баганууд = (1,0), (0,1) цэгүүд хаашаа очих; BA = эхлээд A, дараа нь B; угсраа
хувиргалтад det үржигдэнэ; det ≠ 0 үед урвуу матриц бол буцаах үйлдэл.

**facts**

- **title** Баганууд · **latex**
  `\text{1-р багана} = T(1,0),\; \text{2-р багана} = T(0,1)` · **explanation**
  Матриц бүрийг хоёр цэгээр байгуулж, тайл.
- **title** Угсраа хувиргалт · **latex**
  `BA = \text{эхлээд } A, \text{ дараа нь } B` · **explanation** Цэгт хамгийн
  ойрх нь түрүүлж үйлчилнэ: баруунаас зүүн тийш унш.
- **title** Тодорхойлогч үржигдэнэ · **latex** `\det(BA) = \det B \cdot \det A`
  · **explanation** Талбайн коэффициентүүд үржигдэж нийлнэ.

**workedExamples**

- `vm64-we1` — **statement:** Цагийн зүүний эсрэг $90°$-аар эргүүлээд, дараа нь
  бүх уртыг хоёр дахин ихэсгэдэг матрицыг байгуулаарай. **solution:** Нэгж
  цэгүүдийг мөрдвөл: $(1,0) \to (0,1) \to (0,2)$; $(0,1) \to (-1,0) \to (-2,0)$.
  Багана болгон босгоход: $\begin{pmatrix} 0 & -2 \\ 2 & 0 \end{pmatrix}$,
  өөрөөр хэлбэл
  $2I \cdot R = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
- `vm64-we2` — **statement:** $A$ нь $x$ тэнхлэгийн хувьд тэгш хэмтэй хувиргалт,
  $B$ нь цагийн зүүний эсрэг $90°$-аар эргүүлэлт. $BA$ ба $AB$-г $(1, 0)$ цэгт
  хэрэглээд харьцуулаарай: ижил үү? **solution:** $BA$: эхлээд тэгш хэм,
  $(1,0) \to (1,0)$, дараа нь эргүүлэлт: $(0, 1)$. $AB$: эхлээд эргүүлэлт,
  $(1,0) \to (0,1)$, дараа нь тэгш хэм: $(0, -1)$. Өөр! Дараалал очих газрыг
  өөрчилсөн: энэ бол $AB \ne BA$-гийн зурган хувилбар.
- `vm64-we3` — **statement:** $T = \begin{pmatrix} 3 & 1 \\ 2 & 4 \end{pmatrix}$
  матриц $2$ талбайтай квадратыг хувиргана; дараа нь $\det S = \tfrac{1}{2}$
  байх $S$ матрицыг хэрэглэнэ. Эцсийн талбайг олж, нийлмэл хувиргалт урвуутай
  эсэхийг тогтоогоорой. **solution:** $\det T = 12 - 2 = 10$: талбай $2 \to 20$.
  Дараа нь $\times \tfrac{1}{2}$: эцсийн талбай $10$. Нийлмэл тодорхойлогч
  $= \tfrac{1}{2} \cdot 10 = 5 \ne 0$: урвуутай; буцаах арга бий.

**commonMistakes**

- **text** BA-г «эхлээд B, дараа нь A» гэж унших. · **correction** Цэгт ХАМГИЙН
  ОЙР матриц түрүүлж үйлчилнэ: BA(x) = B(A(x)), эхлээд A. Функцийн нийлмэл шиг
  баруунаас зүүн тийш, учир нь энэ бол яг тэр.
- **text** Угсраа хувиргалтад тодорхойлогчдыг нэмэх. · **correction** Талбайн
  коэффициентүүд ҮРЖИГДЭНЭ: det(BA) = det B · det A. Хоёр дахин ихэсгээд, дараа
  нь гурав дахин ихэсгэвэл талбай 5 биш, 6 дахин өөрчлөгдөнө.

**tryIt**

- `vm64-t1` — **statement:** $3$ дахин томруулаад, дараа нь $180°$-аар эргүүлдэг
  ганц матриц ямар вэ? **solution:** $(1,0) \to (3,0) \to (-3,0)$;
  $(0,1) \to (0,3) \to (0,-3)$: матриц нь
  $\begin{pmatrix} -3 & 0 \\ 0 & -3 \end{pmatrix} = -3I$.
- `vm64-t2` — **statement:** $\det A = 4$, $\det B = -2$. $\det(BA)$-г, нийлмэл
  талбайн коэффициентийг олж, чиглэл солигдох эсэхийг хэлээрэй. **solution:**
  $\det(BA) = -8$: талбай $8$ дахин өөрчлөгдөж, сөрөг тэмдэг нэг тэгш хэмтэй
  хувиргалт орсныг хэлнэ: чиглэл солигдоно.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Нийлэх цэг · **title** Нэг объект, дөрвөн унших арга<br>**body** Матриц нэгэн зэрэг: ХУВИРГАЛТ (баганууд = нэгж цэгүүд буух газар), УГСРАГЧ (үржүүлэх нь хувиргалтуудыг баруунаас зүүн тийш гинжилнэ), ТАЛБАЙН НЯГТЛАН (тодорхойлогч), мөн $\det \ne 0$ үед БУЦААЖ БОЛОХ үйлдэл (урвуу матриц). Шалгалтын асуулт бүр нэг унших аргыг сонгоно; чадвар гэдэг нь бодлогын дундуур тэдгээрийн хооронд шилжих явдал. |
| 1 | transformPlane | **eyebrow** Нэгийг ажигла · **title** Тайлж болох эргэлт<br>**teach** Энэ $90°$-ын эргүүлэлт $(1,0) \to (0,1)$, $(0,1) \to (-1,0)$ болгоно. Тэдгээрийг багана болгон босговол $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ дахин бүтнэ, $\det = 1$: хатуу, чиглэл хадгалагдсан, буцаах нь эргүүлж буцаах ($R^{-1} = R^3$).<br>**config** unchanged |
| 2 | tapQuestion | **eyebrow** Унших аргыг шалга · **title** Баруунаас зүүн тийш<br>**prompt** $BA$-г цэгт хэрэглэх нь…<br>**explanation** $BA(x) = B(A(x))$: цэгт хүрч буй матриц түрүүлнэ. Функцийн нийлмэлийн тэмдэглэгээнээс өвлөсөн.<br>**options** `эхлээд $A$, дараа нь $B$ үйлчилнэ` · `эхлээд $B$, дараа нь $A$ үйлчилнэ` · `дараалал хамаагүй` · `$A$ ба $B$ зэрэг үйлчилнэ` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Хоёр алхамт хувиргалт байгуулах<br>**problemId** `vm64-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Дарааллын гэрэл зураг<br>**problemId** `vm64-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Талбайг нийлүүл<br>**prompt** 1-р хувиргалтын $\det = 3$, 2-р хувиргалтын $\det = -1$. Хоёуланг нь хэрэглэсний дараа $4$ талбайтай дүрсийн талбай…<br>**explanation** Тодорхойлогчид үржигдэнэ: $3 \cdot (-1) = -3$; талбай абсолют утгыг авна: $4 \cdot 3 = 12$ (чиглэл нэг удаа солигдсон).<br>**options** `$12$` · `$-12$` · `$8$` · `$4$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Хоолойгоор дамжих талбай<br>**problemId** `vm64-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Эхлээд унших аргаа нэрлэ<br>**body** Бодохоосоо өмнө асуулт аль унших аргыг хүсэж байгааг хэлээрэй: цэг хаашаа очих (баганууд), нийлмэл хувиргалт (үржвэр), талбай (det), эсвэл буцаах (урвуу матриц). Матрицын шалгалтын алдааны тал нь буруу унших аргаар хариулснаас болдог. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Томруулаад эргүүл<br>**problemId** `vm64-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Тодорхойлогчдыг нийлүүл<br>**problemId** `vm64-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Та шугаман алгебр босгожээ<br>**body** Вектор, скаляр үржвэр, матриц, тодорхойлогч, урвуу матриц, хувиргалт: хамтад нь угсарвал эдгээр нь шугаман алгебрын эхний бүлэг бөгөөд компьютер график, машин сургалт, квант механик, Google-ийн анхны хайлтын эрэмбэлэлтийг ажиллуулдаг математик. Хувиргалтын матриц ба гурван үл мэдэгдэгчтэй систем энэ хаалгаар цааш үргэлжилнэ. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Баганууд $(1,0)$ ба $(0,1)$ хаана буухыг хэлнэ: байгуул, тайл. · $BA$ = эхлээд $A$, дараа нь $B$; $\det(BA) = \det B \cdot \det A$. · $\det \ne 0$ ⇔ буцаах арга бий: энэ бүх нэгжийг холбосон утас. |

---

## PRACTICE

- `vm6-pr-1` — **statement:**
  $\det\begin{pmatrix} 6 & 2 \\ 7 & 3 \end{pmatrix}$-г бодоорой. **solution:**
  $18 - 14 = 4$.
- `vm6-pr-2` — **statement:** $k$-ийн ямар утгад
  $\begin{pmatrix} k & 8 \\ 2 & k \end{pmatrix}$ матриц урвуугүй вэ?
  **solution:** $k^2 - 16 = 0$: $k = \pm 4$.
- `vm6-pr-3` — **statement:** $7$ талбайтай дүрсийг тодорхойлогч нь $-3$
  матрицаар хувиргав. Дүрсийн талбайг олоорой. **solution:** $|-3| \cdot 7 = 21$
  (мөн дүрсийн чиглэл солигдоно).
- `vm6-pr-4` — **statement:** $\begin{pmatrix} 5 & 2 \\ 7 & 3 \end{pmatrix}$
  матрицын урвууг олоорой. **solution:** $\det = 1$:
  $\begin{pmatrix} 3 & -2 \\ -7 & 5 \end{pmatrix}$.
- `vm6-pr-5` — **statement:** $\begin{pmatrix} 6 & 4 \\ 2 & 2 \end{pmatrix}$
  матрицын урвууг олоорой. **solution:** $\det = 4$:
  $\frac{1}{4}\begin{pmatrix} 2 & -4 \\ -2 & 6 \end{pmatrix} = \begin{pmatrix} 1/2 & -1 \\ -1/2 & 3/2 \end{pmatrix}$.
- `vm6-pr-6` — **statement:** Крамерын дүрмээр бодоорой:
  $\begin{cases} 3x + 2y = 8 \\ x - y = 1 \end{cases}$ **solution:**
  $\det A = -3 - 2 = -5$. $\det A_x = 8 \cdot (-1) - 2 \cdot 1 = -10$:
  $x = \frac{-10}{-5} = 2$. $\det A_y = 3 \cdot 1 - 8 \cdot 1 = -5$: $y = 1$.
  Шалгалт: $3(2) + 2(1) = 8$ ✓.
- `vm6-pr-7` — **statement:** $m$-ийн ямар утгад
  $\begin{cases} 2x + 5y = 3 \\ 4x + my = 1 \end{cases}$ систем цор ганц шийдгүй
  вэ? **solution:** $2m - 20 = 0$: $m = 10$ (тэр үед баруун талууд пропорциональ
  байдлыг эвдэнэ: шийдгүй).
- `vm6-pr-8` — **statement:** $\det A = 5$, $\det B = 2$. $\det(AB)$ ба
  $\det(A^{-1})$-г олоорой. **solution:** $\det(AB) = 10$;
  $\det(A^{-1}) = \frac{1}{5}$ (буцаах үйлдэл талбайг буцааж хуваана).

---

## TEST YOURSELF

- `vm6-ty-1` — **statement:**
  $\det\begin{pmatrix} 9 & 6 \\ 6 & 4 \end{pmatrix}$-г бодоод тайлбарлаарай.
  **solution:** $36 - 36 = 0$: урвуугүй. Баганууд коллинеар, хавтгай хавтгайрч,
  урвуу матриц байхгүй.
- `vm6-ty-2` — **statement:** $\begin{pmatrix} 7 & 4 \\ 5 & 3 \end{pmatrix}$
  матрицын урвууг олоод, $AA^{-1}$-ийн зүүн дээд элементийг шалгаарай.
  **solution:** $\det = 21 - 20 = 1$: урвуу нь
  $\begin{pmatrix} 3 & -4 \\ -5 & 7 \end{pmatrix}$. Шалгалт:
  $7 \cdot 3 + 4 \cdot (-5) = 1$ ✓.
- `vm6-ty-3` — **statement:** Урвуу матрицаар бодоорой:
  $\begin{cases} 2x + y = 4 \\ 7x + 4y = 15 \end{cases}$ **solution:**
  $\det = 8 - 7 = 1$; $A^{-1} = \begin{pmatrix} 4 & -1 \\ -7 & 2 \end{pmatrix}$;
  $X = A^{-1}\binom{4}{15} = \binom{1}{2}$: $x = 1, y = 2$.
- `vm6-ty-4` — **statement:** Нэгдүгээр хувиргалт талбайг $3$ дахин өөрчилж,
  хоёр дахь хувиргалтын дараа нийт талбайн коэффициент $12$ болжээ. Хоёр дахь
  хувиргалтын $|\det|$ хэд вэ? Эхнийх нь чиглэлийг сольж, хоёр дахь нь солиогүй
  бол нийлмэл хувиргалт чиглэлийг солих уу? **solution:** $|\det_2| = 12/3 = 4$.
  Нийт нэг удаа солигдсон тул нийлмэл хувиргалт чиглэлийг СОЛИНО (нийлмэл
  тодорхойлогч сөрөг).
- `vm6-ty-5` — **statement:** $x$ тэнхлэгийн хувьд тэгш хэмтэй хувиргаад, дараа
  нь цагийн зүүний эсрэг $90°$-аар эргүүлдэг ганц матрицыг байгуулаарай.
  **solution:** $(1,0) \to (1,0) \to (0,1)$; $(0,1) \to (0,-1) \to (1,0)$.
  Матриц: $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$: $y = x$ шулууны хувьд
  тэгш хэмтэй хувиргалт! Хоёр хувиргалт нийлээд нэг танил царай болсон,
  $\det = -1$.
- `vm6-ty-6` — **statement:** $k$-ийн ямар утгад
  $\begin{pmatrix} 1 & 2 \\ 3 & k \end{pmatrix}$ матриц урвуутай вэ? $k = 8$ үед
  урвуу нь юу вэ? **solution:** $k \ne 6$ үед урвуутай. $k = 8$ үед $\det = 2$,
  урвуу нь
  $\frac{1}{2}\begin{pmatrix} 8 & -2 \\ -3 & 1 \end{pmatrix} = \begin{pmatrix} 4 & -1 \\ -3/2 & 1/2 \end{pmatrix}$.

---

## Notes for Khas

### 1. Mapping

`lib/esh-course.ts:231` maps this unit to **10.4д** (the 2×2 determinant),
**10.4е** (the 2×2 inverse) and **11.2в** (solving a two-variable system with
the inverse). All three are taught, in lessons 1, 2 and 3. Lesson 3 also teaches
2×2 Cramer's rule. The ministry names Cramer only for three unknowns (11.2е,
elective), which unit 8 covers.

### 2. The exam examines a theorem no unit teaches

**Eight bank questions are solved with the Cayley–Hamilton theorem:**
$A^2 - (\operatorname{tr} A)A + (\det A)E = O$ for a 2×2 matrix. They are one
per variant in 2023 (a–d: "$\det A = 1$; find $p, q$ with $A^3 = pA + qE$") and
one per variant in 2024 (a–d: "$A - 3A^{-1} = 5E$; find $x^2 + y^2$"). Every
bank solution names the theorem and uses the trace. The skill graph already
carries the skill (`cayley-hamilton`, exam weight 0.36, "thin"). But no unit
teaches the trace or the theorem: the only "Cayley" anywhere in `data/genmath/`
is the lesson 1 funFact of unit 5. The ministry text does not list it either
(10.4а–е, 11.2).

This unit is the natural home. Lesson 2 already has the inverse, and the 2024
questions need it. A fifth lesson, or a concept and two worked examples in
lesson 2, would cover it. That is ship/content work for the English first; the
Mongolian follows the English. Logged as 6ba.

### 3. Terms

- **«тодорхойлогч»** (determinant): the ministry's word (10.4д, 11.2д), settled
  in `geometry-transformations` Notes 4.
- **«урвуугүй матриц»** (singular): the bank's own phrasing, «матриц урвуугүй
  байх» (5 questions). "Singular" becomes «урвуугүй» throughout; I did not coin
  «өвөрмөц матриц».
- **«туслах диагональ»** (anti-diagonal): the usual school name, calqued from
  the Russian «побочная диагональ». Neither the ministry nor the bank has a word
  for it. «гол диагональ» (main diagonal) is from draft 72.
- **Reflection: «тэгш хэмтэй хувиргалт».** Here I follow the bank, which writes
  «тэнхлэгийн хувьд тэгш хэмтэй хувиргах» and «шулууны хувьд тэгш хэмтэй
  хувиргах» 23 times, and the ministry. 4g's circularity problem does not arise
  here, because this unit has no symmetry lesson. That makes the
  vectors-and-matrices strand and `geometry-transformations` («тусгал») differ
  until 4g is ruled on. If 4g goes to «тэгш хэм», nothing here changes.
- **«угсраа хувиргалт»** (composition) and **«чиглэл»** (orientation): as in
  `geometry-transformations`.
- **«Сэки»** (Seki Takakazu): first appearance. **«Лейбниц»**: as in earlier
  drafts.

### 4. Course framing

- **"The capstone" is stale in both spines.** The blurb says "— the capstone".
  Lesson 4 is titled "Matrices as Transformations — the Capstone" and opens
  "Everything converges here". Its funFact ends "This course was the front
  door". But `transformation-matrices` (unit 7) and `systems-in-three-unknowns`
  (unit 8) follow this unit in the home spine (`lib/genmath-spines.ts:762–777`)
  and in the ЭШ spine alike. The Mongolian drops "capstone" from the blurb and
  the title. It keeps "everything converges here" for lesson 4's own four
  readings, and replaces the last funFact sentence: the next two units carry on
  through this door. The English wants the same edit (ship mode).
- **Lesson 4 overlaps unit 7.** Columns as destinations, composition
  right-to-left, and det as the area factor are all unit 7's subject too. That
  is not a Mongolian problem; I note it for when unit 7 is drafted.
- **"Unit 1"** (lesson 1, concept 3, and the lesson 1 tip) becomes «Вектор ба
  координат» нэгж: the cross test for parallel vectors lives there (6aw).
- **"The geometry course's transformation-matrices lesson"** (lesson 1, teach
  step 1, and lesson 4, concept 1) is real: `geometry/transformations` lesson 7,
  whose recap teaches |det| as the area factor. As in draft 72, the Mongolian
  makes it conditional («…үзсэн бол»), because an ЭШ student need not have taken
  the geometry course.

### 5. Softened claims

- **Leibniz "in the 1680s"** (lesson 1 funFact): kept, after a second look. His
  published statement is the 1693 letter to l'Hôpital, but his unpublished
  manuscripts on determinants (edited by Knobloch) begin in 1678, so the English
  is defensible. Seki's is 1683. "170 years before matrices got their name":
  1850 − 1683 = 167.
- **"Gaussian elimination rather than a neat recipe"** (lesson 2 funFact). There
  is a recipe for 3×3 inverses (the adjugate), and the ministry lists 3×3
  inverses (11.2д, elective). The Mongolian says "usually".
- **Cramer and the grains of sand** (lesson 3 funFact). This is true only if
  each determinant is expanded by the cofactor formula: 21 determinants of order
  20, at 20! terms each, come to about 5 × 10¹⁹ terms, against an estimated 10¹⁹
  grains. Cramer with determinants computed by elimination is cheap. The
  Mongolian adds "by the textbook formula".

### 6. Decimals

**0** inside `$...$` and none in prose. The one decimal in the unit is
`systemGraph`'s `m1: -0.6`, inside a config the draft leaves unchanged. 2d stays
at **1,567** across seventy-three drafts.
