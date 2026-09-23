# Draft — `vectors-matrices/vector-arithmetic`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**ЭШ Вектор ба матриц, unit 1 of 8 (the home course's unit 2).** It is built on
`vectors-and-coordinates` (draft 68), which the ЭШ spine lists after it (6aw).
References to that unit name it, «Вектор ба координат» нэгж, instead of
numbering it: Notes 4.

**Four lessons, 34 items, 48 interactive steps, no nested tryItSet problems.**
(12 workedExamples + 8 tryIt + 8 practice + 6 testYourself.)

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. No em-dash parentheticals (§9), decimal comma in prose
(§7), hyphenated case suffixes (§8), condition before thing (§1). Objectives as
plain text (6d). Imperatives soft in prose that addresses the student, bare in
beats, recaps, titles and fact shorthand. Vector coordinates keep the comma, as
in the bank.

**Mirror pre-check** (6q): no `vectors-matrices-mn` mirror. Draft it.

**Ministry sections read in full first**: 10.8, 10.9. The unit is mapped
(`lib/esh-course.ts:226`) to **10.9а, 10.9б**. It teaches 10.9а whole and 10.9б
in the composing direction; it also teaches 10.9г (operations in coordinates,
mapped to unit 2): Notes 1.

**Exam check** (6m): «харьцаагаар хуваах» (8), «дундаж цэг» (23), «медиан» (37,
most of them statistical) adopted.

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| tip-to-tail (triangle) rule · parallelogram rule | **гурвалжны дүрэм · параллелограммын дүрэм** | not in the sources: Notes 3 |
| resultant (force) | **тэнцүү үйлчлэгч хүч** | physics usage: Notes 3 |
| scalar multiplication | **векторыг тоогоор үржүүлэх** | ministry 10.9а |
| linear combination | **шугаман эвлүүлэг** | coined: Notes 3 |
| midpoint | **дундаж цэг** | ministry 10.8б · bank 23 |
| median (of a triangle) | **медиан** | ministry · bank |
| section formula | **хэрчмийг харьцаагаар хуваах томьёо** | bank «харьцаагаар хуваа» 8 |
| centroid | **медиануудын огтлолцлын цэг** | compositional |

---

## Topic-level strings

**TITLE:** Векторын үйлдлүүд

**BLURB:** Гурвалжны дүрмээр нэмэх, тоогоор үржүүлэх, хасах, гурвалжин ба
параллелограмм доторх векторууд, мөн хэрчмийг харьцаагаар хуваах томьёо.

**buildsOn:** «Вектор ба координат» нэгжийн координат ба урт.

---

## Lesson 1 — Векторуудыг нэмэх (`adding-vectors`)

**concreteComparison**

Зүүн тийш 3 км, дараа нь хойш 4 км алхаарай. Та хаана байна? Эхэлсэн газраасаа
нэг 5 км-ийн шилжилтэд: хоёр хэсэг НЭМЭГДЭЖ ганц аялал болно. Векторын нийлбэр
бол аяллыг гинжлэх: зурагт гурвалжны дүрмээр (нэгийн төгсгөлд нөгөөгийн эхлэл),
арифметикт координат координатаар.

**objective**

Векторуудыг координатаар нэмж, шилжилтүүдийг гурвалжны дүрмээр гинжилж,
нийлбэрийн гурвалжин ба параллелограммын зургийг унших.

**concept**

1. Координатаар нэмэх нь хамгийн энгийн:
   $(x_1, y_1) + (x_2, y_2) = (x_1 + x_2,\; y_1 + y_2)$. Зүүн нь зүүнтэйгээ,
   хойд нь хойдтойгоо нэмэгдэнэ.

2. Геометрээр бол **гурвалжны дүрэм**: $\vec{u}$ векторыг зураад, $\vec{v}$
   векторыг $\vec{u}$ дууссан газраас эхлүүлээрэй; нийлбэр нь эхний эхлэлээс
   сүүлийн төгсгөл хүртэл явна. Хүссэн хэмжээгээрээ гинжилж болно: нийлбэр бүх
   аяллыг хаана.

3. Үүний оронд $\vec{v}$ векторын эхлэлийг $\vec{u}$ векторын эхлэл рүү
   гулсуулбал хоёр сум **параллелограмм** үүсгэх ба нийлбэр нь түүний диагональ
   болно (**параллелограммын дүрэм**). Гурвалжны зураг ба параллелограммын зураг
   бол ижил нийлбэр: физик параллелограммыг илүүд үздэг (хүчнүүд нэг цэгээс
   татна), навигаци гурвалжныг (хэсгүүд дараалан болно).

4. Замыг хаах адилтгал
   $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$ бол
   векторын нийлбэрийн хамгийн их хэрэглэгддэг үр дүн: дундах үсэг хорогдоно.
   Энэ нь геометрийн баталгааг үсгийн бүртгэл болгоно.

**keyIdea**

Координатуудыг нэмээрэй; гурвалжны (нэгийн төгсгөлд нөгөөгийн эхлэл) эсвэл
параллелограммын (нийтлэг эхлэл) дүрмээр зураарай; AB + BC = AC: дундах үсэг
хорогдоно.

**facts**

- **title** Координатаар · **latex**
  `(x_1, y_1) + (x_2, y_2) = (x_1 + x_2, y_1 + y_2)` · **explanation** Зүүн нь
  зүүнтэйгээ, хойд нь хойдтойгоо.
- **title** Гинжлэх · **latex**
  `\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}` ·
  **explanation** Дундах үсэг хорогдоно: аяллууд залгагдана.
- **title** Хоёр зураг · **latex**
  `\text{гурвалжны дүрэм} \;=\; \text{параллелограммын диагональ}` ·
  **explanation** Ижил нийлбэр, хоёр янзаар зурсан.

**workedExamples**

- `vm21-we1` — **statement:** $(2, 3) + (4, -1)$ нийлбэр ба нийлбэрийн уртыг
  олоорой. **solution:** $(2 + 4,\; 3 + (-1)) = (6, 2)$;
  $|(6,2)| = \sqrt{40} = 2\sqrt{10}$.
- `vm21-we2` — **statement:** Явган аялагч зүүн тийш $3$ км, дараа нь хойш $4$
  км алхав. Нийлбэр шилжилт ба түүний уртыг олоорой. **solution:**
  $(3, 0) + (0, 4) = (3, 4)$: нэг $5$ км-ийн шилжилт. Хоёр хэсэг ба нийлбэр нь
  $3$–$4$–$5$ гурвалжин үүсгэнэ.
- `vm21-we3` — **statement:** Нэг биед $(5, 0)$ ба $(-2, 6)$ хүчнүүд үйлчилнэ.
  Тэнцүү үйлчлэгч хүч ба түүний уртыг олоорой. **solution:** Тэнцүү үйлчлэгч
  $= (3, 6)$; $|(3,6)| = \sqrt{45} = 3\sqrt{5}$. Параллелограммын зурагт тэнцүү
  үйлчлэгч хүч бол нийтлэг эхлэлээс гарах диагональ.

**commonMistakes**

- **text** Векторуудын оронд уртуудыг нэмэх. · **correction** Векторууд ижил
  чиглэлтэй биш бол |u + v| нь |u| + |v| БИШ. Зүүн тийш 3 ба хойш 4 нийлээд 7
  биш, 5: чиглэл үргэлж үг хэлэх эрхтэй.
- **text** Гурвалжны дүрмийн гинжийг тасалдуулах. · **correction** Хоёр дахь
  вектор эхнийх нь ДУУССАН газраас эхэлнэ. Хоёуланг нь координатын эхээс
  эхлүүлбэл параллелограммын зураг гарна: зүгээр, гэхдээ тэр үед нийлбэр нь хоёр
  дахь сум биш, диагональ.

**tryIt**

- `vm21-t1` — **statement:** $(-1, 4) + (5, -2)$ нийлбэрийг бодоорой.
  **solution:** $(4, 2)$.
- `vm21-t2` — **statement:**
  $\overrightarrow{PQ} + \overrightarrow{QR} + \overrightarrow{RS}$ илэрхийллийг
  хялбарчилаарай. **solution:** Дундах үсгүүд дараалан хорогдоно:
  $\overrightarrow{PS}$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Санаа · **title** Аялал гинжлэгдэнэ<br>**body** Нэг шилжилтийг, дараа нь өөр нэгийг яваарай: нийт үр дүн нь ганц шилжилт. Векторын нийлбэр аяллыг гинжлэхийг л албан ёсны болгодог бөгөөд арифметик нь хамгийн энгийн: зүүн тийшхийг нэмээд, хойш тийшхийг нэмнэ. |
| 1 | vectorGraph | **eyebrow** Ажигла · **title** Гурвалжны дүрэм, амьдаар<br>**teach** Хоёр дахь сум эхнийх нь дууссан газраас эхэлж, нийлбэр эхний эхлэлээс сүүлийн төгсгөл рүү гарна. Оронд нь хоёуланг нь нийтлэг эхлэлтэй болгон гулсуулбал ижил нийлбэр параллелограммын диагональ болж харагдана: хоёр зураг, нэг нийлбэр.<br>**config** unchanged |
| 2 | tapQuestion | **eyebrow** Санааг шалга · **title** Координатаар<br>**prompt** $(7, -3) + (-2, 8) = $ ?<br>**explanation** $(7 - 2,\; -3 + 8) = (5, 5)$: координатууд хэзээ ч эгнээ солихгүй.<br>**options** `$(5, 5)$` · `$(9, 5)$` · `$(5, -11)$` · `$(9, -11)$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Нийлбэр ба түүний урт<br>**problemId** `vm21-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Аялагчийн гурвалжин<br>**problemId** `vm21-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Дундах үсэг хорогдоно<br>**prompt** $\overrightarrow{AB} + \overrightarrow{BC} = $ ?<br>**explanation** A→B, дараа нь B→C: цэвэр аялал A→C. Нийтлэг дундах B үсэг хорогдоно: векторын геометрийн гол ажилчин адилтгал.<br>**options** `$\overrightarrow{AC}$` · `$\overrightarrow{CA}$` · `$\overrightarrow{BB}$` · `$\vec{0}$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Тэнцүү үйлчлэгч хүч<br>**problemId** `vm21-we3` |
| 7 | tip | **eyebrow** Дадал · **title** Эхлээд диагоналийг таамагла<br>**body** Бодохоосоо өмнө параллелограммыг нүдээр үнэлээрэй: нийлбэр хоёр чиглэлийн ХООРОНД, урт сум руу ойр байх ёстой. Арифметик өөрөөр хэлбэл тэмдэг алдагдсан байна. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Энгийн нийлбэр<br>**problemId** `vm21-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Гурвын гинж<br>**problemId** `vm21-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Векторын хамгийн эртний хууль<br>**body** Хүчний параллелограммын дүрмийг Симон Стевин 1580-аад онд томьёолжээ: «вектор» гэдэг үгийг хэн нэгэн бичихээс 250 гаруй жилийн өмнө (энэ үгийг Гамильтон 1846 онд оруулсан). Далайчид, инженерүүд математикчдыг нэрлэхээс нэлээд өмнө сумнуудыг нэмж байжээ. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Координатаар нэм; зүгээр уртуудыг хэзээ ч бүү нэм. · Гурвалжны (дараалал) ба параллелограммын (нийтлэг эхлэл) дүрэм ижил нийлбэр зурна. · $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$: дундах үсгийг хорогдуул. |

---

## Lesson 2 — Тоогоор үржүүлэх ба хасах (`scalars-and-subtraction`)

**concreteComparison**

Жорыг хоёр дахин ихэсгэвэл орц бүр хоёр дахин ихэснэ. Векторыг тоогоор
үржүүлэхэд ХОЁР координат хоёулаа үржинэ: сум сунах ба чиглэл хөндөгдөхгүй (тоо
сөрөг бол эргэнэ). Харин хасах нь шинэ юм биш: $\vec{u} - \vec{v}$ бол зүгээр л
$\vec{u} + (-\vec{v})$, эргэлтийг нэмэх.

**objective**

Векторыг тоогоор үржүүлж, үржүүлэхийг нэмэхтэй хослуулж, векторуудыг хасаж,
энгийн векторын тэгшитгэл бодох.

**concept**

1. Тоогоор үржүүлэх нь сунгана: $k(x, y) = (kx, ky)$. Урт нь $|k|$ дахин
   өөрчлөгдөнө; сөрөг $k$ сумыг бас эргүүлнэ. Энэ бол «Вектор ба координат»
   нэгжийн коллинеар шалгуурыг урагш нь уншсан нь.

2. Хасах нь хувцас өмссөн нэмэх: $\vec{u} - \vec{v} = \vec{u} + (-\vec{v})$,
   өөрөөр хэлбэл координатаар хасна. Геометрээр хоёулаа нэг цэгээс эхлэх үед
   $\vec{u} - \vec{v}$ нь **$\vec{v}$ векторын төгсгөлөөс $\vec{u}$ векторын
   төгсгөл рүү** явна: «зорилт хасах эхлэл» гэж санаарай.

3. $3\vec{u} - 2\vec{v}$ мэтийн **шугаман эвлүүлэг** бол өдөр тутмын мөнгөн
   тэмдэгт: эхлээд үржүүлж, дараа нь нэмнэ. Векторын тэгшитгэл энгийн алгебр шиг
   бодогдоно: $2\vec{x} + (3, -1) = (7, 5)$ нэг нэг үйлдлээр задарна, учир нь
   таны хүсэж болох бүх дүрэм (байр солих, хаалт задлах) үнэхээр биелнэ.

**keyIdea**

k(x, y) = (kx, ky); u − v = u + (−v), v-ийн төгсгөлөөс u-ийн төгсгөл рүү зурна;
векторын тэгшитгэл энгийн алгебр шиг бодогдоно.

**facts**

- **title** Үржүүлэх · **latex** `k(x, y) = (kx, ky)` · **explanation** Урт |k|
  дахин; сөрөг k эргүүлнэ.
- **title** Хасах · **latex** `\vec{u} - \vec{v} = (x_1 - x_2,\; y_1 - y_2)` ·
  **explanation** Координатаар; геометрээр v-ийн төгсгөлөөс u-ийн төгсгөл рүү.
- **title** Алгебр биелнэ · **latex**
  `k(\vec{u} + \vec{v}) = k\vec{u} + k\vec{v}` · **explanation** Хаалт задал,
  цуглуул, бод: тоон дээрх шиг, координат координатаар.

**workedExamples**

- `vm22-we1` — **statement:** $3(2, -1) - 2(1, 4)$ илэрхийллийг бодоорой.
  **solution:** Үржүүлбэл: $(6, -3)$ ба $(2, 8)$. Хасвал:
  $(6 - 2,\; -3 - 8) = (4, -11)$.
- `vm22-we2` — **statement:** Нэг цэгээс зурсан $\vec{u} = (5, 2)$ ба
  $\vec{v} = (1, 3)$ векторуудын хувьд $\vec{v}$ векторын төгсгөлөөс $\vec{u}$
  векторын төгсгөл хүртэлх векторыг олоорой. **solution:** Энэ бол яг
  $\vec{u} - \vec{v} = (4, -1)$: зорилт хасах эхлэл.
- `vm22-we3` — **statement:** $\vec{x}$ векторыг олоорой:
  $\;2\vec{x} + (3, -1) = (7, 5)$. **solution:** $2\vec{x} = (4, 6)$, тиймээс
  $\vec{x} = (2, 3)$: векторын алгебр тооны алгебр шиг яг задарна.

**commonMistakes**

- **text** Зөвхөн нэг координатыг үржүүлэх. · **correction** 3·(2, −1) = (6,
  −3), хоёр эгнээ хоёулаа. Нэг координатыг үржүүлэх нь сумыг сунгахгүй: өөр
  чиглэл рүү нугална.
- **text** u − v-г u-ийн төгсгөлөөс v-ийн төгсгөл рүү зурах. · **correction** u
  − v нь u РУУ заана: v-ийн төгсгөлөөс u-ийн төгсгөл рүү. «Зорилт хасах эхлэл»:
  хариу эхэлж нэрлэгдсэн вектор руу онилно.

**tryIt**

- `vm22-t1` — **statement:** $-2(3, -4)$ вектор ба түүний уртыг олоорой.
  **solution:** $(-6, 8)$; урт нь $2 \cdot 5 = 10$.
- `vm22-t2` — **statement:** $(8, 1) - (3, 5)$ ялгаврыг бодоорой. **solution:**
  $(5, -4)$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Санаа · **title** Сунга, эргүүл, хослуул<br>**body** Векторыг $k$ тоогоор үржүүлбэл хоёр координат хоёулаа үржинэ: сум $|k|$ дахин сунаж, $k < 0$ бол эргэнэ. Нэмэхтэй хослуулбал $3\vec{u} - 2\vec{v}$ мэт **шугаман эвлүүлэг** гарна: векторын ажлын өдөр тутмын мөнгөн тэмдэгт. |
| 1 | teach | **eyebrow** Хасалтын тайлал · **title** Зорилт хасах эхлэл<br>**body** $\vec{u} - \vec{v}$ бол зүгээр л $\vec{u} + (-\vec{v})$: координатаар хасна. Зураг нь: хоёуланг нэг цэгээс зурахад $\vec{u} - \vec{v}$ нь $\vec{v}$ векторын төгсгөлөөс $\vec{u}$ векторын төгсгөл рүү, эхэлж нэрлэгдсэн вектор РУУ заана. Энэ бол «Вектор ба координат» нэгжийн төгсгөл хасах эхлэл ӨӨРӨӨ: $\overrightarrow{AB} = B - A$.<br>**beats** k(x,y) = (kx, ky); сөрөг k = эргэлт · u − v: координатаар, сум u руу заана · векторын тэгшитгэл тооны алгебр шиг бодогдоно |
| 2 | tapQuestion | **eyebrow** Санааг шалга · **title** Үржүүл<br>**prompt** $-3(2, -5) = $ ?<br>**explanation** Хоёр координат хоёулаа $-3$ үржигдэхүүнийг авна: $(-6, 15)$. Сум гурав дахин урт, эргэсэн.<br>**options** `$(-6, 15)$` · `$(-6, -15)$` · `$(6, 15)$` · `$(-1, -8)$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Шугаман эвлүүлэг<br>**problemId** `vm22-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Төгсгөлөөс төгсгөл рүү<br>**problemId** `vm22-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Хас<br>**prompt** $(4, -2) - (-1, 3) = $ ?<br>**explanation** $(4 - (-1),\; -2 - 3) = (5, -5)$. Эхний эгнээний давхар хасах дээр хуруу хальтирдаг.<br>**options** `$(5, -5)$` · `$(3, 1)$` · `$(-5, 5)$` · `$(5, 1)$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Векторыг ол<br>**problemId** `vm22-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Нэмэхээсээ өмнө үржүүл<br>**body** $3\vec{u} - 2\vec{v}$ илэрхийлэлд хослуулахаасаа ӨМНӨ хоёр үржүүлэлтээ дуусгаарай: үржүүлсэн хоёр векторыг тодорхой бичихэд таван секунд зарцуулагдах бөгөөд бүтэн бодлогыг алдуулдаг хагас үржүүлсэн эрлийз алдаанаас сэргийлнэ. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Сунгаад эргүүл<br>**problemId** `vm22-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Энгийн ялгавар<br>**problemId** `vm22-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Яагаад «скаляр» гэж?<br>**body** Энэ үг латины scala, «шат, хуваарь» гэсэн үгнээс гаралтай. Скаляр векторыг МАСШТАБЛАНА: энэ бол түүний ажлын бүх тодорхойлолт бөгөөд нэр нь үүнийг мартахыг хэзээ ч зөвшөөрөхгүй. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** $k(x, y) = (kx, ky)$: $|k|$ дахин сунга, сөрөг бол эргүүл. · $\vec{u} - \vec{v}$: координатаар; сум $\vec{u}$ руу заана. · Векторын тэгшитгэл энгийн алгебр шиг задарна. |

---

## Lesson 3 — Гурвалжин ба параллелограмм дахь векторууд (`vectors-in-figures`)

**concreteComparison**

Параллелограмм бол векторын машин: $A$ оройг сонгоод, талуудыг
$\vec{u} = \overrightarrow{AB}$ ба $\vec{v} = \overrightarrow{AD}$ гэж нэрлэвэл
дүрсийн БҮХ зүйл (хоёр диагональ, дундаж цэг бүр, медиан бүр) $\vec{u}$ ба
$\vec{v}$ векторуудын ямар нэг эвлүүлэг болно. Шалгалт танд дүрс өгөөд түүний
векторын хэлээр ярихыг хүснэ.

**objective**

Гурвалжин ба параллелограммын диагональ, дундаж цэг, медианыг хоёр талын
вектороор илэрхийлж, уртыг нь координатаас бодох.

**concept**

1. $\vec{u} = \overrightarrow{AB}$ ба $\vec{v} = \overrightarrow{AD}$ байх
   $ABCD$ параллелограммд: $A$ оройгоос гарах диагональ
   $\overrightarrow{AC} = \vec{u} + \vec{v}$ (нэг талаар, дараа нь нөгөөгөөр
   яв), нөгөө диагональ $\overrightarrow{BD} = \vec{v} - \vec{u}$ ($B$ оройгоос
   $\vec{u}$ векторыг буцааж, $\vec{v}$ векторыг явна). Нийлбэр ба ялгавар: хоёр
   диагональ.

2. Дундаж цэг дундажлана: $BC$ хэрчмийн $M$ дундаж цэг
   $\overrightarrow{AM} = \tfrac{1}{2}(\overrightarrow{AB} + \overrightarrow{AC})$
   тэнцэтгэлийг хангана. Энэ бол $ABC$ гурвалжны $A$ оройгоос татсан **медиан**
   вектор ч мөн: нэг томьёо, хоёр нэр.

3. Дүрсийн бодлого бүрийн ард байгаа арга: (1) суурь цэг сонгох, (2) коллинеар
   биш хоёр талын векторыг нэрлэх, (3) дүрсийн ирмэгүүдийн дагуу зорилт руу
   алхаж, алхам бүрийг нэрлэсэн векторын $\pm$ эсвэл түүний хэсэг гэж бичих.
   Алхалт бол хариу ӨӨРӨӨ.

**keyIdea**

Хоёр талын векторыг нэрлээд дүрсээр алхаарай: диагональууд нь u + v ба v − u;
дундаж цэг ба медиан дундажлана: AM = ½(AB + AC).

**facts**

- **title** Параллелограммын диагональ · **latex**
  `\overrightarrow{AC} = \vec{u} + \vec{v},\quad \overrightarrow{BD} = \vec{v} - \vec{u}`
  · **explanation** A оройгоос гарах хоёр талын векторын нийлбэр ба ялгавар.
- **title** Медиан, дундаж цэг · **latex**
  `\overrightarrow{AM} = \tfrac{1}{2}(\overrightarrow{AB} + \overrightarrow{AC})`
  · **explanation** BC-ийн дундаж цэг рүү: хоёр талын аяллыг дундажил.
- **title** Арга · **latex**
  `\vec{u}, \vec{v} \text{ нэрлэх} \to \text{ирмэгээр алхах}` · **explanation**
  Дүрс дэх хэрчим бүр нэрлэсэн талуудын ± эвлүүлэг.

**workedExamples**

- `vm23-we1` — **statement:** $ABCD$ параллелограммд
  $\overrightarrow{AB} = (4, 1)$ ба $\overrightarrow{AD} = (1, 3)$.
  $\overrightarrow{AC}$ диагональ ба түүний уртыг олоорой. **solution:**
  $\overrightarrow{AC} = \overrightarrow{AB} + \overrightarrow{AD} = (5, 4)$;
  $|\overrightarrow{AC}| = \sqrt{25 + 16} = \sqrt{41}$.
- `vm23-we2` — **statement:** Мөн тэр параллелограмм: нөгөө
  $\overrightarrow{BD}$ диагональ ба түүний уртыг олоорой. **solution:**
  $\overrightarrow{BD} = \overrightarrow{AD} - \overrightarrow{AB} = (1 - 4,\; 3 - 1) = (-3, 2)$;
  $|\overrightarrow{BD}| = \sqrt{9 + 4} = \sqrt{13}$.
- `vm23-we3` — **statement:** $ABC$ гурвалжинд $\overrightarrow{AB} = (6, 2)$ ба
  $\overrightarrow{AC} = (2, 4)$. $BC$ тал руу татсан $\overrightarrow{AM}$
  медиан вектор ба түүний уртыг олоорой. **solution:**
  $\overrightarrow{AM} = \tfrac{1}{2}\big((6,2) + (2,4)\big) = (4, 3)$;
  $|\overrightarrow{AM}| = 5$.

**commonMistakes**

- **text** BD = v − u байхын оронд BD = u − v гэж бичих. · **correction** BD нь
  B-ээс D руу явна: AB-г буцаах (−u), дараа нь AD-г явах (+v), тиймээс BD = v −
  u. Цээжилсэн томьёог биш, алхалтыг мөрдөөрэй.
- **text** Суурь цэгээс гарах векторуудын оронд үзүүрүүдийг дундажлах. ·
  **correction** A оройгоос татсан медиан A оройгоос гарах векторуудыг ашиглана:
  AM = ½(AB + AC). Бусад оройноос гарах векторуудыг холих нь бүртгэлийг эвдэнэ.

**tryIt**

- `vm23-t1` — **statement:** $ABCD$ параллелограмм:
  $\overrightarrow{AB} = (3, 3)$, $\overrightarrow{AD} = (2, -1)$.
  $\overrightarrow{AC}$ векторыг олоорой. **solution:**
  $(3 + 2,\; 3 - 1) = (5, 2)$.
- `vm23-t2` — **statement:** $ABC$ гурвалжин: $\overrightarrow{AB} = (8, 0)$,
  $\overrightarrow{AC} = (2, 6)$. $\overrightarrow{AM}$ медиан векторыг олоорой.
  **solution:** $\tfrac{1}{2}(10, 6) = (5, 3)$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Бэлтгэл · **title** Хоёр вектор бүх дүрсийг удирдана<br>**body** Дүрсийн нэг оройг сонгоод, түүнээс гарах хоёр талын векторыг ($\vec{u}$ ба $\vec{v}$) нэрлэвэл бусад хэрчим бүр тэр хоёрын $\pm$ эвлүүлэг болно. Энэ бол шалгалтын векторын дуртай төрөл: дүрсийн хэлээр ярих. |
| 1 | teach | **eyebrow** Каталог · **title** Диагональ ба медиан<br>**body** $A$ оройгоос харвал параллелограммын диагональууд: $\overrightarrow{AC} = \vec{u} + \vec{v}$, $\overrightarrow{BD} = \vec{v} - \vec{u}$: нийлбэр ба ялгавар. $BC$-ийн дундаж цэг рүү татсан гурвалжны медиан: $\overrightarrow{AM} = \tfrac{1}{2}(\overrightarrow{AB} + \overrightarrow{AC})$: аяллуудыг дундажилна. Тус бүрийг АЛХАЖ гаргаарай: $B$ оройгоос $\vec{u}$ векторыг буцааж, $\vec{v}$ векторыг явбал $BD$ гарна.<br>**beats** AC = u + v: нэг тал, дараа нь нөгөө · BD = v − u: u-г буцаа, v-г яв · медиан: AM = ½(AB + AC) |
| 2 | tapQuestion | **eyebrow** Алхалтыг шалга · **title** B-ээс D рүү<br>**prompt** $\vec{u} = \overrightarrow{AB}$, $\vec{v} = \overrightarrow{AD}$ байх $ABCD$ параллелограммд $\overrightarrow{BD}$ диагональ нь…<br>**explanation** Алхаж үзээрэй: B-ээс A руу буцах нь $-\vec{u}$, дараа нь A-аас D руу $+\vec{v}$. Нийт: $\vec{v} - \vec{u}$.<br>**options** `$\vec{v} - \vec{u}$` · `$\vec{u} + \vec{v}$` · `$\vec{u} - \vec{v}$` · `$\tfrac{1}{2}(\vec{u} + \vec{v})$` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Урт диагональ<br>**problemId** `vm23-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Богино диагональ<br>**problemId** `vm23-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Аяллуудыг дундажил<br>**prompt** $ABC$ гурвалжинд $\overrightarrow{AB} = (4, 2)$, $\overrightarrow{AC} = (0, 6)$. $\overrightarrow{AM}$ медиан вектор нь…<br>**explanation** $\overrightarrow{AM} = \tfrac{1}{2}\big((4,2) + (0,6)\big) = (2, 4)$.<br>**options** `$(2, 4)$` · `$(4, 8)$` · `$(2, 2)$` · `$(4, 4)$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** 3–4–5 медиан<br>**problemId** `vm23-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Цээжлэх биш: алх<br>**body** $BD = \vec{v} - \vec{u}$ мэт томьёог дүрсийн ирмэгээр алхаж гурван секундэд дахин гаргаж болно. Шахалтын дор алхалт ой санамжаас найдвартай. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Нийлбэр диагональ<br>**problemId** `vm23-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Нэг медиан<br>**problemId** `vm23-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Медиануудын огтлолцол, нэг мөрөнд<br>**body** Векторын тусламжтайгаар гурвалжны гурван медиан нэг цэгт (тус бүрийн гуравны хоёрт) огтлолцдог баримт ганц тооцоо болж хураагдана: медиануудын огтлолцлын цэг $\tfrac{1}{3}(\vec{a} + \vec{b} + \vec{c})$, гурван оройд төгс тэгш хэмтэй. Сонгодог геометрт нэг хуудас хэрэгтэй; векторт нэг мөр. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** Нэг оройд $\vec{u}, \vec{v}$ векторуудыг нэрлэ; бусад бүх зүйл алхалт. · Диагональууд: $\vec{u} + \vec{v}$ ба $\vec{v} - \vec{u}$. · Медиан, дундаж цэг: $\overrightarrow{AM} = \tfrac{1}{2}(\overrightarrow{AB} + \overrightarrow{AC})$. |

---

## Lesson 4 — Хэрчмийг харьцаагаар хуваах (`the-section-formula`)

**concreteComparison**

Дундаж цэг бол 50–50 хуваалт. Харин $P$ цэг $AB$ дээр $AP : PB = 2 : 1$ байхаар
оршдог гэж бодъё: 2-ыг 1-д харьцуулсан хуваалт, замын гуравны хоёрт. Хуваах
томьёо аливаа хуваалтыг үнэлнэ: үзүүрүүдийн жинлэсэн дундаж бөгөөд үзүүр бүрийн
жин нь харьцааны ЦААД талын хэсэг.

**objective**

Хэрчмийг өгсөн харьцаагаар хуваах цэгийг олж, дундаж цэгийг 1:1 тохиолдол гэж
таньж, мэдэгдэх хуваах цэгээс харьцааг сэргээх.

**concept**

1. $P$ нь $AB$ хэрчмийг $AP : PB = m : n$ харьцаагаар хуваадаг бол $$P = \frac{n
   \cdot A + m \cdot B}{m + n}.$$ Жин загалмайлж байгааг анхаараарай: $B$ цэг
   $m$ жин, $A$ цэг $n$ жин авна. Хэзээ ч алдахгүй санамж: ОЙР байгаа үзүүр ИХ
   жин авах ба ойр эсэхийг харьцаа шийднэ.

2. Дундаж цэг бол томьёоны баярын хувцастай хувилбар: $m : n = 1 : 1$ бол
   $P = \tfrac{1}{2}(A + B)$: координатуудыг дундажлана.

3. Харьцааг ОЛОХЫН тулд урвуугаар гүйлгээрэй: $P$ нь $AB$ дээр оршдог нь
   мэдэгдэж байвал $\overrightarrow{AP}$ ба $\overrightarrow{PB}$ векторуудыг
   координатаар харьцуулаарай; тэдгээрийн скаляр харьцаа нь $m : n$. (Хоёр
   вектор коллинеар биш бол $P$ шулуун дээр огт байгаагүй: суурилуулсан худал
   илрүүлэгч.)

4. Энд байгаа бүх зүйл бол коллинеар шалгуур нэмэх нийлбэр: шинэ хэрэгсэл алга,
   зүгээр л түүний шалгалтад хамгийн их гардаг савлагаа.

**keyIdea**

AP : PB = m : n ⇒ P = (n·A + m·B)/(m + n); дундаж цэг бол 1:1 тохиолдол;
харьцааг сэргээхдээ AP ба PB векторуудыг харьцуулаарай.

**facts**

- **title** Хуваах томьёо · **latex** `P = \frac{n \cdot A + m \cdot B}{m + n}`
  · **explanation** AP : PB = m : n үед: цаад хэсэг нь үзүүр бүрийг жинлэнэ.
- **title** Дундаж цэг · **latex** `M = \tfrac{1}{2}(A + B)` · **explanation** 1
  : 1 тухайн тохиолдол: энгийн дундаж.
- **title** Харьцааг сэргээх · **latex**
  `\overrightarrow{AP} = \tfrac{m}{n}\,\overrightarrow{PB}` · **explanation**
  Хоёр хэсгийг координатаар харьцуулж m : n харьцааг унш.

**workedExamples**

- `vm24-we1` — **statement:** $A(1, 2)$ ба $B(7, 8)$ бол $P$ цэг $AB$ хэрчмийг
  $AP : PB = 2 : 1$ харьцаагаар хуваана. $P$ цэгийг олоорой. **solution:**
  $P = \dfrac{1 \cdot A + 2 \cdot B}{3} = \left(\dfrac{1 + 14}{3}, \dfrac{2 + 16}{3}\right) = (5, 6)$:
  2:1 хуваалтын шаардсанаар $B$ хүртэлх замын гуравны хоёрт.
- `vm24-we2` — **statement:** $A(-4, 3)$ ба $B(6, -1)$ цэгүүдийн дундаж цэгийг
  олоорой. **solution:**
  $M = \tfrac{1}{2}(A + B) = \left(\tfrac{2}{2}, \tfrac{2}{2}\right) = (1, 1)$.
- `vm24-we3` — **statement:** $A(1, 2)$, $B(6, 7)$ бол $P(3, 4)$ цэг $AB$ хэрчим
  дээр оршдог эсэхийг шалгаад, $AP : PB$ харьцааг олоорой. **solution:**
  $\overrightarrow{AP} = (2, 2)$ ба $\overrightarrow{PB} = (3, 3)$: коллинеар ✓
  (тиймээс $P$ үнэхээр шулуун дээр), мөн
  $\overrightarrow{AP} = \tfrac{2}{3}\overrightarrow{PB}$. Харьцаа:
  $AP : PB = 2 : 3$.

**commonMistakes**

- **text** Үзүүр бүрийг өөрийн харьцааны хэсгээр жинлэх. · **correction** Жин
  ЗАГАЛМАЙЛНА: AP:PB = m:n үед A нь n, B нь m жин авна. Туйлын тохиолдлоор
  шалгаарай: AP:PB = 100:1 бол P бараг B дээр буух ёстой.
- **text** m + n-д хуваахаа мартах. · **correction** Жингүүд зүгээр нэмэгдэх
  биш, дундажлагдах ёстой: $m + n$ хуваарь л P-г A ба B-ийн хооронд барина.

**tryIt**

- `vm24-t1` — **statement:** $A(0, 0)$, $B(8, 4)$ бол $P$ цэг $AB$ хэрчмийг
  $AP : PB = 1 : 3$ харьцаагаар хуваана. $P$ цэгийг олоорой. **solution:**
  $P = \dfrac{3A + 1B}{4} = (2, 1)$: $B$ хүртэлх замын дөрөвний нэгт.
- `vm24-t2` — **statement:** $(5, -3)$ ба $(-1, 7)$ цэгүүдийн дундаж цэгийг
  олоорой. **solution:** $(2, 2)$.

### Interactive — 12 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** 50–50 биш хуваалтууд<br>**body** Дундаж цэгийг та мэднэ. Гэвч геометрт гуравны хоёрт байх цэг, эсвэл $1 : 3$ хуваалт байнга хэрэгтэй: медиануудын огтлолцол, төсөөтэй гурвалжны хэсгүүд, шалгалтын асуултууд. Нэг томьёо бүх хуваалтыг үнэлнэ. |
| 1 | teach | **eyebrow** Томьёо · **title** Загалмайлсан жинтэй жинлэсэн дундаж<br>**body** $AP : PB = m : n$ үед: $$P = \frac{n \cdot A + m \cdot B}{m + n}$$ Жин ЗАГАЛМАЙЛНА: ойр байгаа үзүүр их жин авна. Туйлын тохиолдлуудыг шалгаарай: $m : n = 1 : 1$ бол энгийн дундаж (дундаж цэг); маш их $m$ бол $P$ цэгийг $B$ дээр чирнэ.<br>**beats** P = (n·A + m·B)/(m + n) · жин загалмайлна: ойр үзүүр, их жин · дундаж цэг = 1:1 тохиолдол |
| 2 | tapQuestion | **eyebrow** Санааг шалга · **title** Жин аль тийш явах вэ?<br>**prompt** $AP : PB = 3 : 1$. Хуваах томьёонд аль үзүүр $3$ жин авах вэ?<br>**explanation** $P = \frac{1 \cdot A + 3 \cdot B}{4}$. $3:1$ хуваалт $P$ цэгийг замын дөрөвний гуравт тавина: $B$-д ойр, тиймээс $B$ их жин авна.<br>**options** `$B$` · `$A$` · `Хоёулаа` · `Аль нь ч биш: 3 зөвхөн хуваарьт орно` — **correctIndex 0** |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Гуравны хоёрт<br>**problemId** `vm24-we1` |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** 1:1 тохиолдол<br>**problemId** `vm24-we2` |
| 5 | tapQuestion | **eyebrow** Шуурхай шалгалт · **title** Дөрөвний нэгийн цэг<br>**prompt** $A(0,0)$, $B(12, 8)$ ба $AP : PB = 1 : 3$. Тэгвэл $P = $ ?<br>**explanation** $P = \frac{3A + B}{4} = (3, 2)$: замын дөрөвний нэгт, $A$-д хамгийн ойр.<br>**options** `$(3, 2)$` · `$(9, 6)$` · `$(4, 8/3)$` · `$(6, 4)$` — **correctIndex 0** |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Харьцааг сэргээ<br>**problemId** `vm24-we3` |
| 7 | tip | **eyebrow** Шалгалтын дадал · **title** Итгэхээсээ өмнө туйлын тохиолдлыг турш<br>**body** Томьёондоо $m : n = 1 : 0$ гэж орлуулаарай: $PB = 0$ тул $P = B$ гарах ёстой. $A$ гарвал жингээ буруу талаар нь загалмайлсан байна. Туйлын шалгалт загалмайлалтыг таван секундэд, үргэлж шийднэ. |
| 8 | tryIt | **eyebrow** Туршаад үз · **title** Дөрөвний нэгт<br>**problemId** `vm24-t1` |
| 9 | tryIt | **eyebrow** Туршаад үз · **title** Энгийн дундаж цэг<br>**problemId** `vm24-t2` |
| 10 | funFact | **eyebrow** Сонирхолтой баримт · **title** Хөшүүрэг түрүүлж мэдсэн<br>**body** Хуваах томьёо бол координатаар бичсэн Архимедийн хөшүүргийн хууль: $A$ дээрх $n$ масс ба $B$ дээрх $m$ масс яг $P$ цэг дээр тэнцвэрждэг. Физик ба геометр тулгуур цэг хаана байхыг санал нэгтэй хэлнэ. |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу үлдэх вэ<br>**points** $AP : PB = m : n \Rightarrow P = \frac{nA + mB}{m + n}$: жин загалмайлна. · Дундаж цэг = $1 : 1$ тохиолдол: координатуудыг дундажил. · Харьцааг сэргээхдээ $\overrightarrow{AP}$ ба $\overrightarrow{PB}$ векторуудыг харьцуул. |

---

## PRACTICE

- `vm2-pr-1` — **statement:** $(3, -2) + (-7, 6)$ нийлбэрийг бодоорой.
  **solution:** $(-4, 4)$.
- `vm2-pr-2` — **statement:** $4(1, -2) - 3(2, 1)$ илэрхийллийг бодоорой.
  **solution:** $(4 - 6,\; -8 - 3) = (-2, -11)$.
- `vm2-pr-3` — **statement:** $\vec{x}$ векторыг олоорой:
  $3\vec{x} - (2, 5) = (7, -2)$. **solution:** $3\vec{x} = (9, 3)$,
  $\vec{x} = (3, 1)$.
- `vm2-pr-4` — **statement:** $ABCD$ параллелограмм:
  $\overrightarrow{AB} = (5, 2)$, $\overrightarrow{AD} = (-1, 4)$. Хоёр
  диагоналийн векторыг олоорой. **solution:** $\overrightarrow{AC} = (4, 6)$,
  $\overrightarrow{BD} = (-6, 2)$.
- `vm2-pr-5` — **statement:** $ABC$ гурвалжин: $\overrightarrow{AB} = (10, 2)$,
  $\overrightarrow{AC} = (2, 8)$. $\overrightarrow{AM}$ медиан вектор ба түүний
  уртыг олоорой. **solution:** $\overrightarrow{AM} = (6, 5)$;
  $|\overrightarrow{AM}| = \sqrt{61}$.
- `vm2-pr-6` — **statement:** $A(0, 5)$, $B(10, 0)$ бол $P$ цэг $AB$ хэрчмийг
  $AP : PB = 3 : 2$ харьцаагаар хуваана. $P$ цэгийг олоорой. **solution:**
  $P = \frac{2A + 3B}{5} = (6, 2)$.
- `vm2-pr-7` — **statement:** Нэг цэгт $(7, -1)$ ба $(-3, 5)$ хүчнүүд үйлчилнэ.
  Тэнцүү үйлчлэгч хүчний уртыг олоорой. **solution:** Нийлбэр $(4, 4)$; урт нь
  $4\sqrt{2}$.
- `vm2-pr-8` — **statement:** $A(2, 1)$, $B(8, 7)$ бол $P(4, 3)$ цэг $AB$ дээр
  оршино. $AP : PB$ харьцааг олоорой. **solution:**
  $\overrightarrow{AP} = (2, 2)$, $\overrightarrow{PB} = (4, 4)$: харьцаа
  $1 : 2$.

---

## TEST YOURSELF

- `vm2-ty-1` — **statement:** $2(3, -1) + 3(-2, 4)$ вектор ба түүний уртыг
  олоорой. **solution:** $(6 - 6,\; -2 + 12) = (0, 10)$; урт нь $10$.
- `vm2-ty-2` — **statement:**
  $\overrightarrow{AB} + \overrightarrow{BC} - \overrightarrow{DC}$ илэрхийллийг
  нэрлэсэн цэгүүдийн хоорондох ганц вектор болгон хялбарчилаарай. **solution:**
  $\overrightarrow{AB} + \overrightarrow{BC} = \overrightarrow{AC}$, мөн
  $-\overrightarrow{DC} = \overrightarrow{CD}$: нийт
  $\overrightarrow{AC} + \overrightarrow{CD} = \overrightarrow{AD}$.
- `vm2-ty-3` — **statement:** $ABCD$ параллелограммд
  $\overrightarrow{AC} = (8, 2)$ ба $\overrightarrow{BD} = (-2, 6)$.
  $\overrightarrow{AB}$ ба $\overrightarrow{AD}$ векторуудыг сэргээгээрэй.
  **solution:** $\vec{u} + \vec{v} = (8,2)$, $\vec{v} - \vec{u} = (-2,6)$.
  Нэмбэл: $2\vec{v} = (6, 8)$, $\vec{v} = \overrightarrow{AD} = (3, 4)$; тэгвэл
  $\vec{u} = \overrightarrow{AB} = (5, -2)$.
- `vm2-ty-4` — **statement:** $A(-1, 4)$, $B(9, -6)$ бол $P$ цэг $AB$ хэрчмийг
  $AP : PB = 2 : 3$ харьцаагаар хуваана. $P$ цэгийг олоорой. **solution:**
  $P = \frac{3A + 2B}{5} = \left(\frac{-3 + 18}{5}, \frac{12 - 12}{5}\right) = (3, 0)$.
- `vm2-ty-5` — **statement:** $A(0,0)$, $B(6, 0)$, $C(0, 6)$ оройтой $ABC$
  гурвалжны медиануудын огтлолцлын цэгийг $G = \tfrac{1}{3}(A + B + C)$
  томьёогоор олоорой. **solution:** $G = (2, 2)$.
- `vm2-ty-6` — **statement:** $\vec{x}$ векторыг олж, $|\vec{x}|$ уртыг өгөөрэй:
  $\;2\vec{x} + (1, -3) = 5(1, 1)$. **solution:** $2\vec{x} = (4, 8)$,
  $\vec{x} = (2, 4)$; $|\vec{x}| = 2\sqrt{5}$.

---

## Notes for Khas

### 1. Order and mapping

- **Order** (6aw): this unit depends on `vectors-and-coordinates` and the ЭШ
  spine puts it first. The drafts name that unit instead of numbering it.
- **Mapping** (`lib/esh-course.ts:226`: 10.9а, 10.9б):
- 10.9а (add, subtract, multiply by a number, recognise collinear vectors):
taught whole.
- 10.9б (decompose a vector along two given directions): taught in the composing
direction. Lesson 3 writes every segment in terms of two side vectors, and
`vm2-ty-3` recovers two sides from two diagonals. No item asks "write w as αu +
βv" for given u, v, w.
  - 10.9г (operations in coordinates): taught here, though mapped to unit 2.
- The section formula (lesson 4) has no ministry code of its own; 10.8б covers
only the midpoint.

### 2. Four things in the English

- **(a) A wrong exam tip** (lesson 4, step 7). It says to plug in m : n = 1 : 0
  because "it must return P = A... it returns B?! Then your weights are
  crossed". This is backwards. AP : PB = 1 : 0 means PB = 0, so P must be B, and
  the correct formula (n·A + m·B)/(m + n) gives B. A student who follows the
  English tip will "fix" a correct formula into a wrong one. The Mongolian says
  the check must return B.
- **(b) Leaked authoring text** (`vm24-we3`). The statement reads "$P(3, 4)$
  lies on segment $AB$ with $A(1, 2)$, $B(6, 7)$... wait — check it, then find
  $AP : PB$." That is the author's note to themself, shipped to students (the 6h
  family). The Mongolian statement is clean: check that P is on AB, then find
  the ratio.
- **(c) A muddled sentence** (lesson 4, concept 1): "Note the cross-over: $B$'s
  weight is $m$ (the part NEAR $A$'s side of the ratio)… the mnemonic that never
  fails". The parenthesis and the ellipsis don't parse. The Mongolian says
  plainly that B carries m and A carries n, and that the nearer endpoint carries
  the bigger weight.
- **(d) "Three centuries before anyone wrote the word 'vector'"** (lesson 1
  funFact). Stevin's parallelogram is from 1586; Hamilton coined "vector" in
  1846. That is 260 years. The Mongolian says «250 гаруй жил» and names
  Hamilton.

### 3. Terms

- **«гурвалжны дүрэм · параллелограммын дүрэм»** (tip-to-tail and parallelogram
  rules). These are in none of the sources, but they are the standard names in
  Russian-school texts («правило треугольника / параллелограмма»), and I expect
  Mongolian textbooks to use them. The English "tip-to-tail" is explained once
  as «нэгийн төгсгөлд нөгөөгийн эхлэл».
- **«тэнцүү үйлчлэгч хүч»** (resultant force): physics usage
  («равнодействующая»).
- **«шугаман эвлүүлэг»** (linear combination): coined. «шугаман комбинац» is the
  other candidate.
- **«хэрчмийг харьцаагаар хуваах томьёо»** (section formula), from the bank's
  «харьцаагаар хуваах» (8).
- **«медиануудын огтлолцлын цэг»** (centroid): compositional. «хүндийн төв» is
  the physics name.

### 4. Course framing

"Unit 1" appears three times: in `buildsOn`, and twice in lesson 2 (concept 1
and step 1). All three become «Вектор ба координат» нэгж, by name, because in
the ЭШ spine that unit is unit 2 (6aw).

### 5. Decimals

**0** inside `$...$` and none in prose. 2d stands at **1,567** across sixty-nine
drafts.
