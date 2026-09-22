# Draft — `algebra-2/quadratics-and-complex-numbers`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**This closes an ЭШ topic.** *Комплекс тоо* is a two-unit block and this is
unit 2.

> **Corrected 22 Sep, review pile 6q.** This first said "six of fourteen topics
> and 32 of 72 units", which counted drafts only. Counting shipped mirrors too,
> the course is **36 of 72 units and 7 of 14 topics** — Тоо ба үсэгт илэрхийлэл
> was already fully mirrored and never needed drafting.

**Four lessons, 30 items, 49 interactive steps, no nested tryItSet problems** —
the thin-interactive `algebra-2` shape.

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. Written to `docs/mn-voice-reference.md` from the first
line: no em-dash parentheticals (§9), decimal comma in prose (§7), hyphenated
case suffixes (§8), condition before thing (§1).

**Shipped-mirror check:** no overlap. But the *draft* overlap is the heaviest
in the programme — **three of these four lessons re-teach material already
drafted**, and one of them compresses a whole six-lesson ЭШ unit into a single
lesson. Notes 1.

**Exam subtopic check** (review pile 6m): the bank's `quadratic_inequality`
tag returns **33 questions**, plus 3 more under `quadratic_inequality_parameter`
— and that turned into Notes 5, which I think is the most consequential finding
in this draft.

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| vertex (of a parabola) | **оройн цэг** | **exam subtopic «параболын оройн цэг»** · ministry 1 |
| vertex form | **оройн хэлбэр** | compositional on the above; 0 as a phrase |
| completing the square | **бүтэн квадрат ялгах** | **ministry 10.5б, verbatim** · shipped 5 — **correction, Notes 3** |
| quadratic inequality | **квадрат тэнцэтгэл биш** | **ministry 11.1б and 11.1в, verbatim** |
| quadratic trinomial | **квадрат гурван гишүүнт** | **ministry 11.1в** · exam 3 |
| number line | **тоон шулуун** | **ministry 11.1б** · exam 12 |
| sign region | **тэмдгийн муж** | compositional; «муж» exam 83 |
| empty solution set | **хоосон олонлог** | settled in `esh/sets-and-operations` |

> **Carried in unchanged from `11/complex-numbers`:** комплекс тоо, хуурмаг
> нэгж, бодит хэсэг, хуурмаг хэсэг, **хосмог**, модул. And from
> `algebra-1/quadratic-equations` and `10/quadratic-functions`: парабол,
> квадрат тэгшитгэл, дискриминант, шийд, тэгш хэмийн тэнхлэг, хамгийн их /
> хамгийн бага утга.

---

## Topic-level strings

**TITLE:** Квадрат тэгшитгэл ба комплекс тоо

**BLURB:** Параболын төрөлх хэл болох оройн хэлбэр, i нэртэй шинэ тоо, эхэлсэн
тэгшитгэл бүрээ дуусгадаг квадрат тэгшитгэлийн томьёо, мөн графикаас шууд
уншигддаг тэнцэтгэл биш.

---

## Lesson 1 — Оройн хэлбэр ба бүтэн квадрат ялгах (`vertex-form-and-completing-the-square`)

**concreteComparison**

GPS координат нь «олтлоо тойроод яв» гэдгээс дээр. Стандарт хэлбэр ax² + bx + c
оройг нуудаг бол оройн хэлбэр a(x − h)² + k НЬ өөрөө координат юм. Бүтэн
квадрат ялгах бол энэ хоёрын хоорондох хөрвүүлэгч.

**objective**

Бүтэн квадрат ялгаж стандарт ба оройн хэлбэрийн хооронд хөрвүүлэх, мөн орой,
тэнхлэг, хамгийн их эсвэл бага утгыг шууд унших.

**concept**

1. **Оройн хэлбэр** $y = a(x - h)^2 + k$ бол 1-р бүлгийн хувиргалтын жор:
   орой нь $(h, k)$, тэнхлэг нь $x = h$, $a$-гийн тэмдгээр нээгдэнэ.
   $y = 2(x - 3)^2 - 8$: орой $(3, -8)$, хамгийн бага утга $-8$, нэг харцаар.

2. **Хөрвүүлэх**: $y = x^2 + 6x + 1$. 6-гийн хагасыг аваад квадратдана (9),
   түүнийг НЭМЭЭД мөн ХАСНА: $y = (x^2 + 6x + 9) + 1 - 9 = (x + 3)^2 - 8$.
   Орой $(-3, -8)$. Тэргүүлэх коэффициенттэй үед эхлээд түүнийг $x$-ийн
   гишүүдээс гаргаж аваарай:
   $y = 2x^2 - 12x + 5 = 2(x^2 - 6x) + 5 = 2(x - 3)^2 - 13$.

3. Яагаад ингэх хэрэгтэй вэ? Оновчлол. Орой НЬ хамгийн их эсвэл бага утга:
   $P(x) = -2x^2 + 80x - 300$ ашгийн загвар яг оройдоо дээд цэгтээ хүрэх
   бөгөөд бүтэн квадрат ялгах (эсвэл $x_v = -\frac{b}{2a}$) хамгийн сайн үнийг
   олж, оройн хэлбэр хамгийн сайн ашгийг харуулна.

**keyIdea**

Оройн хэлбэр оройг харуулна; бүтэн квадрат ялгах нь (b/2)²-ийг нэмээд хасаж,
шаардлагатай бол эхлээд a-г гаргаж аваад дурын квадрат гурван гишүүнтийг тэр
хэлбэрт хөрвүүлнэ.

**facts**

| title | latex | explanation |
|---|---|---|
| Хоёр хэлбэр | `ax^2 + bx + c \;\longleftrightarrow\; a(x - h)^2 + k` | Ижил парабол; баруун тал орой $(h, k)$-г шууд харуулна. |
| Хөрвүүлэгч | `x^2 + bx = \left(x + \tfrac{b}{2}\right)^2 - \left(\tfrac{b}{2}\right)^2` | $(b/2)^2$-ийг нэмээд хасна, юу ч өөрчлөгдөхгүй, бүхэн дахин зохион байгуулагдана. |

**workedExamples**

- `a221-we1` — **statement:** $y = x^2 - 8x + 11$-ийг оройн хэлбэрт бичээд
  орой ба хамгийн бага утгыг хэлээрэй.
  **solution:** $-8$-ын хагас нь $-4$; квадрат нь 16.
  $y = (x^2 - 8x + 16) + 11 - 16 = (x - 4)^2 - 5$. Орой $(4, -5)$; хамгийн
  бага утга $-5$ ($a = 1 > 0$).
- `a221-we2` — **statement:** $y = 2x^2 - 12x + 5$-ийг оройн хэлбэрт
  хөрвүүлээрэй.
  **solution:** $x$-ийн гишүүдээс 2-ыг гаргая: $y = 2(x^2 - 6x) + 5$. Дотор нь
  гүйцээе: $x^2 - 6x = (x-3)^2 - 9$. Тэгэхээр
  $y = 2[(x-3)^2 - 9] + 5 = 2(x-3)^2 - 13$. Орой $(3, -13)$. Хассан 9 хаалтнаас
  гарахдаа ХОЁР ДАХИН болсон, энэ бол сонгодог урхи.

**commonMistakes**

- **text:** Тэргүүлэх коэффициентийг хальслахгүйгээр бүтэн квадрат ялгах:
  $2x^2 - 12x$-аас $36$ нэмэх.
  **correction:** ЭХЛЭЭД 2-ыг гаргаж аваарай: $2(x^2 - 6x)$, дотор нь 9-өөр
  гүйцээгээд, тэр 9 хаалтнаас $2 \times 9 = 18$ болж гардгийг санаарай.
- **text:** $y = (x + 3)^2 - 8$-гийн оройг $(3, -8)$ гэж унших.
  **correction:** Доторх тэмдэг худал хэлдэг (1-р бүлэг): $x + 3 = x - (-3)$
  тул $h = -3$. Орой $(-3, -8)$.

**tryIt**

- `a221-t1` — $y = x^2 + 10x + 30$-ийг оройн хэлбэрт бичээрэй.
  **solution:** $(x + 5)^2 + 30 - 25 = (x + 5)^2 + 5$. Орой $(-5, 5)$, энэ
  парабол $x$ тэнхлэгт хэзээ ч хүрэхгүй.
- `a221-t2` — Пуужингийн өндөр $h(t) = -5t^2 + 40t + 2$. Бүтэн квадрат ялгаж
  дээд өндөр ба түүнд хүрэх хугацааг олоорой.
  **solution:** $h = -5(t^2 - 8t) + 2 = -5[(t-4)^2 - 16] + 2 = -5(t-4)^2 + 82$.
  Дээд цэг: $t = 4$ с-д 82 м.

### Interactive — same twelve steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Нуугдсан орой<br>**body** $y = x^2 - 8x + 11$, эргэх цэг нь хаана вэ? Харагдахгүй. $y = (x - 4)^2 - 5$, ЯГ ижил парабол бөгөөд орой $(4, -5)$ нь бичлэгт нь сууж байна. Энэ хичээл бол нуудаг хэлбэр ба харуулдаг хэлбэрийн хоорондох хөрвүүлэгчийн тухай. |
| 1 | parabolaGraph | **eyebrow** Тоглож үз · **title** Оройн хэлбэр, амьдаар<br>**teach** $a$, $h$, $k$-г жолоодоод $y = a(x-h)^2 + k$ хэрхэн хариулахыг ажиглаарай. Орой $(h, k)$-г яг таг дагана, эдгээр нь байрлалын эрэг, харин $a$ түүний эргэн тойронд хэлбэрийг өөрчилнө. Энэ хэлбэр НЬ $y = x^2$ дээр хэрэглэсэн 1-р бүлгийн хувиргалтын жор юм.<br>**config** unchanged (`mode: vertex`, `a: 2`, `h: 3`, `k: -8`) |
| 2 | parabolaGraph | **eyebrow** Харьцуулъя · **title** Стандарт хэлбэр түүнийг нуудаг<br>**teach** Ижил параболын гэр бүл, стандарт хэлбэрийн эрэг: $b$ ба $c$-г алхмаар өөрчлөөд оройг таамаглаж үзээрэй… тэр диагоналиар гулсах бөгөөд юу ч шууд уншигдахгүй. Стандарт хэлбэр нь $y$ тэнхлэгтэй огтлолцох цэгт ($c$) болон квадрат тэгшитгэлийн томьёонд гайхалтай, харин оройд аймшигтай. Тиймээс хөрвүүлэгч хэрэгтэй.<br>**config** unchanged (`mode: standard`, `b: -8`, `c: 11`) |
| 3 | teach | **eyebrow** Хөрвүүлэгч · **title** Шидэт квадратыг нэмээд хас<br>**body** $x^2 + 6x$ нь $(x + 3)^2 = x^2 + 6x + 9$ болохыг хүсэж байна. Тэгэхээр дутуу байгаа 9-ийг НЭМЭЭД тэр дороо ХАСаарай, юу ч өөрчлөгдөхгүй: $x^2 + 6x + 1 = (x^2 + 6x + 9) + 1 - 9 = (x+3)^2 - 8$. Нэг илэрхийлэл, дахин зохион байгуулагдсан нь. Тэргүүлэх коэффициенттэй үед: эхлээд түүнийг $x$-ийн гишүүдээс гаргаж аваад, дотор нь гүйцээгээд, болгоомжтой буцааж үржүүлээрэй. |
| 4 | worked | **eyebrow** Бодсон жишээ · **title** Цэвэр хөрвүүлэлт<br>**problemId** a221-we1 |
| 5 | tapQuestion | **eyebrow** Алхмаа шалгая · **title** Шидэт тоо<br>**prompt** $x^2 + 12x + 7$-г оройн хэлбэрт бичихийн тулд нэмээд хасах тоо нь:<br>**options** `$36$` · `$144$` · `$12$` · `$6$` — **correctIndex 0**<br>**explanation** 12-ын хагас нь 6; квадрат нь 36: $(x+6)^2 + 7 - 36 = (x+6)^2 - 29$. |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Тэргүүлэх коэффициент оролцож байна<br>**problemId** a221-we2 |
| 7 | tapQuestion | **eyebrow** Урхийг шалгая · **title** Хаалтнаас юу гарах вэ<br>**prompt** $y = 3(x^2 - 4x) + 1 = 3[(x-2)^2 - 4] + 1 = $ ?<br>**options** `$3(x-2)^2 - 11$` · `$3(x-2)^2 - 3$` · `$3(x-2)^2 - 4 + 1$… тэгвэл $3(x-2)^2 - 3$ гэж үү?` · `$3(x-2)^2 + 13$` — **correctIndex 0**<br>**explanation** Доторх $-4$ гарахдаа 3-аар үржигдэнэ: $-12 + 1 = -11$. Тэр үржүүлэлтийг мартах нь бүтэн квадрат ялгахын ГОЛ алдаа. |
| 8 | tip | **eyebrow** Зуршил · **title** Буцааж задалж шалгаарай<br>**body** Оройн хэлбэрийн мэдэгдэл хоёр секундын зайд баттай болно: хариугаа задлаад эхнийхтэй нь харьцуулаарай. $(x-4)^2 - 5 \to x^2 - 8x + 16 - 5 = x^2 - 8x + 11$ ✓. Үүнийг зуршил болгоорой, энэ нь найдварыг шалгалт болгож хувиргана. |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Хөрвүүлэгчийн дасгал<br>**problemId** a221-t1 |
| 10 | tryIt | **eyebrow** Туршиж үз · **title** Пуужингийн дээд цэг<br>**problemId** a221-t2 |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** Оройн хэлбэр $a(x-h)^2 + k$ нь орой, тэнхлэг, хамгийн их эсвэл бага утгыг харуулна. · Хөрвүүлэх: $(b/2)^2$-ийг нэмээд хас; эхлээд $a$-г $x$-ийн гишүүдээс гаргаж ав. · Хассан квадрат хаалтнаас $a$-гаар ҮРЖИГДЭЖ гарна, буцааж задалж шалгаарай. |

---

## Lesson 2 — Комплекс тоо (`complex-numbers`)

**concreteComparison**

Сөрөг тоо нэгэн цагт утгагүй сонсогддог байсан («5 хонины өр гэж юу вэ?»),
зайлшгүй хэрэгтэй нь батлагдтал. $-1$-ийн квадрат язгуур ижил намтартай:
«хуурмаг» гэж шоологдоод, дараа нь электроник, долгион, квант физикийн ажлын
хэл болж чимээгүйхэн хувирсан.

**objective**

i-тэй тооцоолол хийх (зэрэг, нэмэх, хасах, үржүүлэх, хосмог ба хуваах), мөн
сөрөг тооны квадрат язгуурыг хялбарчлах.

**concept**

1. $i$-г $i^2 = -1$-ээр тодорхойлно. Тэгвэл $\sqrt{-25} = 5i$, мөн **комплекс
   тоо** бүр $a + bi$ хэлбэртэй (бодит хэсэг $a$, хуурмаг хэсэг $b$). $i$-гийн
   зэрэг 4 үетэй эргэлдэнэ: $i, -1, -i, 1$, тэгэхээр
   $i^{37} = i^{36} \cdot i = i$.

2. **Арифметик** нь $i$-гийн олон гишүүнт шиг ажиллана: нэмэхдээ ижил
   хэсгүүдийг нийлүүлж, үржүүлэхдээ задлаад дараа нь $i^2$ бүрийг $-1$ болгож
   хөрвүүлнэ. $(2 + 3i)(4 - i) = 8 - 2i + 12i - 3i^2 = 8 + 10i + 3 = 11 + 10i$.

3. **Хосмог** $a + bi$ ба $a - bi$ үржихдээ $a^2 + b^2$ бодит тоо өгнө. Тэр нь
   хуваарийг $i$-гээс цэвэрлэнэ:
   $\frac{3 + i}{2 - i} = \frac{(3+i)(2+i)}{(2-i)(2+i)} = \frac{5 + 5i}{5} = 1 + i$.

**keyIdea**

i² = −1 бөгөөд бусад бүхэн нь олон гишүүнтийн арифметик: ижил хэсгүүд
нэмэгдэж, задлалт үржүүлж, хосмог хуваарийг бодит болгож, i-гийн зэрэг 4
тутамд эргэлдэнэ.

**facts**

| title | latex | explanation |
|---|---|---|
| Тодорхойлолт | `i^2 = -1, \qquad \sqrt{-k} = i\sqrt{k} \;(k > 0)` | Бусад язгуурын алгебраас ӨМНӨ $i$-г гаргаж аваарай. |
| Хосмогийн үржвэр | `(a + bi)(a - bi) = a^2 + b^2` | Үргэлж бодит, үргэлж эерэг (0-оос бусад үед), хуваарь цэвэрлэгч. |

**workedExamples**

- `a222-we1` — **statement:** $(5 - 2i) - (3 + 4i)$ ба $(2 + 3i)(4 - i)$-ийг
  хялбарчлаарай.
  **solution:** Ижил хэсгүүдийг хасая: $(5-3) + (-2-4)i = 2 - 6i$. Үржүүлье:
  $8 - 2i + 12i - 3i^2 = 8 + 10i + 3 = 11 + 10i$.
- `a222-we2` — **statement:** $\dfrac{3 + i}{2 - i}$-ийг $a + bi$ хэлбэрт
  бичээрэй.
  **solution:** Хүртвэр, хуваарийг хосмог $2 + i$-гээр үржүүлье: хүртвэр
  $(3+i)(2+i) = 6 + 3i + 2i + i^2 = 5 + 5i$; хуваарь $(2-i)(2+i) = 4 + 1 = 5$.
  Үр дүн: $\frac{5 + 5i}{5} = 1 + i$.

**commonMistakes**

- **text:** $\sqrt{-4} \cdot \sqrt{-9} = \sqrt{36} = 6$.
  **correction:** ЭХЛЭЭД $i$ рүү хөрвүүлээрэй: $2i \cdot 3i = 6i^2 = -6$.
  $\sqrt{a}\sqrt{b} = \sqrt{ab}$ дүрэм зөвхөн сөрөг бус $a, b$-гийн хувьд
  биелдэг.
- **text:** Хариунд $i^2$-ийг амьдаар нь үлдээх:
  $(2+3i)(4-i) = 8 + 10i - 3i^2$, болоо.
  **correction:** $i^2$ нь тодорхойлолтоороо $-1$, үргэлж хөрвүүлээрэй:
  $-3i^2 = +3$, тэгвэл $11 + 10i$. Эцсийн хариу $a + bi$ хэлбэртэй бөгөөд
  $i$-гийн 1-ээс дээш зэрэггүй байна.

**tryIt**

- `a222-t1` — $\sqrt{-49} + \sqrt{-16}$-ийг хялбарчлаад $(3 + 2i)^2$-ийг
  тооцоолоорой.
  **solution:** $7i + 4i = 11i$. Квадрат:
  $9 + 12i + 4i^2 = 9 + 12i - 4 = 5 + 12i$.
- `a222-t2` — $\dfrac{10}{1 + 3i}$-ийг $a + bi$ хэлбэрт бичээрэй.
  **solution:** $\frac{1 - 3i}{1 - 3i}$-гээр: хүртвэр $10 - 30i$; хуваарь
  $1 + 9 = 10$. Үр дүн: $1 - 3i$.

### Interactive — same thirteen steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Хариугүй тэгшитгэл гэж үү?<br>**body** $x^2 = -1$ бодит шийдгүй, квадрат хэзээ ч сөрөг байдаггүй. Олон зууны турш хариулт нь «тэгэхээр шийдгүй» байсан. Дараа нь алгебрчид анзаарчээ: хэрэв квадрат нь $-1$ байх тоог ЗОХИОГООД цааш нь тооцоолсоор байвал юу ч эвдрэхгүй бөгөөд өмнө нь боломжгүй байсан бодлогууд нээгдэнэ. Тэр тоо бол $i$, мөн дараагийн хичээлд тэр квадрат тэгшитгэлийн томьёог дуусгана. |
| 1 | teach | **eyebrow** Дүрмүүд · **title** Нэг шинэ баримт, хуучин арифметик<br>**body** Комплекс тооны талаарх бүхэн $i^2 = -1$ дээр нэмээд ердийн алгебраас урган гарна. $\sqrt{-25} = \sqrt{25}\,\sqrt{-1} = 5i$. $a + bi$ комплекс тоо бол хоёр хэсэгтэй объект буюу бодит хэсэг, хуурмаг хэсэгтэй бөгөөд $a + bx$ хоёр гишүүнттэй яг адилаар харьцана. Нэг зуршил: язгуур доорх сөрөг тоог бусад хялбарчлалаас ӨМНӨ $i$ хэлбэрт хөрвүүлээрэй. |
| 2 | worked | **eyebrow** Бодсон жишээ · **title** Хасаад задлаарай<br>**problemId** a222-we1 |
| 3 | tapQuestion | **eyebrow** Хөрвүүлэлтээ шалгая · **title** Сөрөг тооны язгуур<br>**prompt** $\sqrt{-4} \cdot \sqrt{-9} = $ ?<br>**options** `$-6$` · `$6$` · `$6i$` · `$-6i$` — **correctIndex 0**<br>**explanation** Эхлээд хөрвүүлээрэй: $2i \cdot 3i = 6i^2 = -6$. Язгуур дор үржүүлэх нь ($\sqrt{36} = 6$) зөвхөн сөрөг бус тооны хувьд хүчинтэй дүрэм хэрэглэж байна, энд тэр нь ил эвдэрч байна. |
| 4 | teach | **eyebrow** Мөчлөг · **title** i-гийн зэрэг<br>**body** $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$, дараа нь үүрд давтана. Дурын зэргийг илтгэгчийг 4-т хуваагаад үлдэгдлийг нь авч хураана: $i^{37}$: $37 = 4(9) + 1$ тул $i^{37} = i^1 = i$. Дөрвөн утга, эргэлдэж байна, энэ бол таны алгебр дахь анхны үечилсэн хэв маяг бөгөөд эргэлт хэрхэн ажилладгийн урьдчилсан амт. |
| 5 | tapQuestion | **eyebrow** Мөчлөгөө шалгая · **title** Том илтгэгч, жижиг хариу<br>**prompt** $i^{50} = $ ?<br>**options** `$-1$` · `$1$` · `$i$` · `$-i$` — **correctIndex 0**<br>**explanation** $50 = 4(12) + 2$: үлдэгдэл 2 тул $i^{50} = i^2 = -1$. |
| 6 | teach | **eyebrow** Хуваах · **title** Хосмогийн заль<br>**body** $\frac{3+i}{2-i}$ нь $a + bi$ хэлбэрт биш, доор нь $i$ байна. Засвар: хүртвэр, хуваарийг хуваарийн **хосмог** $2 + i$-гээр үржүүлээрэй. Доод тал нь $(2-i)(2+i) = 4 + 1 = 5$ болно, дунд гишүүд хорогдож $-i^2$ эерэг болно. Энэ бол хуваарийг иррационалаас чөлөөлөхтэй ижил, зөвхөн язгуурын үүргийг $i$ гүйцэтгэж байна. |
| 7 | worked | **eyebrow** Бодсон жишээ · **title** Хуваарийг цэвэрлээрэй<br>**problemId** a222-we2 |
| 8 | tip | **eyebrow** Зуршил · **title** Бодит хэсэг, хуурмаг хэсэг, үргэлж<br>**body** Эцсийн хариу бүр $a + bi$ хэлбэрт буудаг: $i^2$ байхгүй, хуваарьт $i$ байхгүй, ижил хэсгүүд нийлүүлэгдсэн. Түүнийг бутархайн «бүрэн хураасан» гэдэгтэй ижил хандаарай, энэ бол нийтийн гар барилтын хэлбэр. |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Хөрвүүлж квадратдаарай<br>**problemId** a222-t1 |
| 10 | tryIt | **eyebrow** Туршиж үз · **title** Комплекс тоонд хуваах<br>**problemId** a222-t2 |
| 11 | funFact | **eyebrow** Сонирхолтой баримт · **title** Нэр нь доромжлол байсан<br>**body** Декарт эдгээр тоог зохиомол зүйл гэж үгүйсгэхийн тулд «хуурмаг» гэж нэрлэсэн. Хошигнол муугаар хөгширчээ: таны утасны дохионы боловсруулалт, эрчим хүчний сүлжээний хувьсах гүйдлийн шинжилгээ, мөн квант механик өөрөө бүгд комплекс арифметик дээр ажилладаг. «Хуурмаг» тоонууд ачаа даадаг болж хувирсан. |
| 12 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** $i^2 = -1$; $\sqrt{-k} = i\sqrt{k}$, бусад язгуурын алгебраас өмнө хөрвүүлээрэй. · Ижил хэсгүүдийг нэмээрэй; задлаад $i^2$-ийг хөрвүүлээрэй; $i$-гийн зэрэг 4 тутамд эргэлдэнэ. · Хосмогоор үржүүлж хуваарай: $(a+bi)(a-bi) = a^2 + b^2$. |

---

## Lesson 3 — Квадрат тэгшитгэлийн томьёо ба комплекс шийд (`the-quadratic-formula-and-complex-roots`)

**concreteComparison**

Алгебр 1-д сөрөг дискриминант «шийдгүй, зогс» гэсэн үг байсан. $i$ гартаа
байхад ижил квадрат язгуур одоо тооцоологдоно. Квадрат тэгшитгэл бүр яг хоёр
шийдтэй (давтагдсаныг тооцвол); зарим нь зүгээр л бодит шулуунаас гадна
амьдардаг.

**objective**

Дурын квадрат тэгшитгэлийг томьёогоор бодох, дискриминантаар шийдийг ангилах,
мөн комплекс шийдийг x тэнхлэгт хүрдэггүй графиктай холбох.

**concept**

1. $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ томьёо одоо НӨХЦӨЛГҮЙГЭЭР
   ажиллана. $x^2 - 4x + 13 = 0$-ийн хувьд: $D = 16 - 52 = -36$ тул
   $x = \frac{4 \pm 6i}{2} = 2 \pm 3i$, хосмог хос.

2. **Дискриминант, шинэчилсэн**: $D > 0$ бол хоёр бодит шийд (график хоёр удаа
   огтолно); $D = 0$ бол нэг давтагдсан бодит шийд (орой тэнхлэгийг үнсэнэ);
   $D < 0$ бол хоёр КОМПЛЕКС ХОСМОГ шийд (график тэнхлэгт огт хүрэхгүй; шийд нь
   бодит зурагт үл үзэгдэнэ).

3. Бодит квадрат тэгшитгэлийн комплекс шийд үргэлж $p \pm qi$ хосмог хосоор
   ирнэ, томьёон дахь $\pm$ үүнийг баталгаажуулна. Ашигтай урвуу арга: шийд нь
   $2 \pm 3i$ байх квадрат тэгшитгэл нь $(x - 2)^2 + 9 = x^2 - 4x + 13$, энд
   нийлбэр $= 4$, үржвэр $= 13$.

**keyIdea**

i-тэй бол квадрат тэгшитгэлийн томьёо хэзээ ч унахгүй: D < 0 бол p ± qi хосмог
хос өгөх бөгөөд график үүнийг x тэнхлэгээс хөндий хөвж харуулна.

**facts**

| title | latex | explanation |
|---|---|---|
| Нөхцөлгүй томьёо | `x = \frac{-b \pm \sqrt{D}}{2a}, \quad D = b^2 - 4ac` | $D < 0$: $\sqrt{D} = i\sqrt{|D|}$ гэж бичээд үргэлжлүүлнэ. |
| Хосмог хос | `D < 0 \Rightarrow x = p \pm qi` | Бодит коэффициент комплекс шийдийг толин хос болгоно. |

**workedExamples**

- `a223-we1` — **statement:** $x^2 - 4x + 13 = 0$-ийг бодоорой.
  **solution:** $D = 16 - 52 = -36$.
  $x = \frac{4 \pm \sqrt{-36}}{2} = \frac{4 \pm 6i}{2} = 2 \pm 3i$. $2 + 3i$-г
  шалгая: $(2+3i)^2 = -5 + 12i$; $-5 + 12i - 8 - 12i + 13 = 0$ ✓.
- `a223-we2` — **statement:** $2x^2 + 2x + 5 = 0$-ийг бодоод шийд нь хосмог
  болохыг шалгаарай.
  **solution:** $D = 4 - 40 = -36$.
  $x = \frac{-2 \pm 6i}{4} = -\frac{1}{2} \pm \frac{3}{2}i$. Нийлбэр:
  $-1 = -\frac{b}{a}$ ✓; үржвэр:
  $\frac{1}{4} + \frac{9}{4} = \frac{5}{2} = \frac{c}{a}$ ✓.

**commonMistakes**

- **text:** $D < 0$ дээр «шийдгүй» гээд зогсох.
  **correction:** БОДИТ шийдгүй, харин комплекс хос оршдог бөгөөд бодлого
  ихэвчлэн түүнийг хүсдэг: $\sqrt{-36} = 6i$ бөгөөд томьёо хэвийн дуусна.
- **text:** Хоёулангийнх нь $2a$-д хуваахаа мартах:
  $\frac{4 \pm 6i}{2} = 2 \pm 6i$.
  **correction:** Зураас бүгдийг хамарна:
  $\frac{4}{2} \pm \frac{6}{2}i = 2 \pm 3i$. Хялбарчлахаасаа өмнө бутархайг
  салгаарай.

**tryIt**

- `a223-t1` — $x^2 + 6x + 25 = 0$-ийг бодоорой.
  **solution:** $D = 36 - 100 = -64$. $x = \frac{-6 \pm 8i}{2} = -3 \pm 4i$.
- `a223-t2` — Шийд нь $1 \pm 2i$ байх (тэргүүлэх коэффициент 1) квадрат
  тэгшитгэл бичээрэй.
  **solution:** Нийлбэр $= 2$, үржвэр $= 1 + 4 = 5$: $x^2 - 2x + 5 = 0$.
  Эсвэл шууд: $(x - 1)^2 + 4$.

### Interactive — same twelve steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Алгебр 1-ийн эхэлсэн ажлыг дуусгах нь<br>**body** Өнгөрсөн жил $x^2 - 4x + 13 = 0$ мөрөө хавчиж дууссан: $D = -36$, «шийдгүй». Гэвч та квадрат нь сөрөг байх тоог сая барьсан. Томьёог $i$-тэйгээр дахин ажиллуулбал хариу гарч ирнэ, дурын бодит шийдтэй адил хууль ёсны хоёр комплекс тоо. |
| 1 | parabolaGraph | **eyebrow** Тоглож үз · **title** Шийд алга болохыг ажиглаарай<br>**teach** $c$-г дээш алхамчлаад парабол $x$ тэнхлэгээс хөөрөхийг ажиглаарай. Хоёр огтлолцол → нэг үнсэлт → байхгүй. Хөндий хөвж эхлэх мөч нь яг $D = 0$; түүнээс цааш бодит зураг юу ч харуулахгүй, гэвч шийдүүд үхээгүй, тэд хосмог хос болж комплекс хавтгай руу нүүсэн.<br>**config** unchanged (`mode: standard`, `b: -4`, `c: 3`) |
| 2 | teach | **eyebrow** Шинэчлэлт · **title** √(сөрөг) одоо тооцоологдоно<br>**body** $D = -36$: $\sqrt{-36} = 6i$ гэж бичээд өмнөхтэй яг адилаар үргэлжлүүлээрэй: $x = \frac{4 \pm 6i}{2} = 2 \pm 3i$. Хариуны хэлбэрийг анзаараарай: бодит хэсэг $\pm$ хуурмаг хэсэг буюу **хосмог хос**. Бодит коэффициенттэй квадрат тэгшитгэл ганц бие комплекс шийд гаргаж чадахгүй; $\pm$ бүрд ихэр төрүүлнэ. |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Хосмог хос, шалгагдсан<br>**problemId** a223-we1 |
| 4 | tapQuestion | **eyebrow** Төгсгөлөө шалгая · **title** Томьёог гүйцээгээрэй<br>**prompt** $x^2 - 2x + 10 = 0$-ийн хувьд $D = -36$. Шийдүүд нь:<br>**options** `$1 \pm 3i$` · `$-1 \pm 3i$` · `$2 \pm 6i$` · `шийд оршихгүй` — **correctIndex 0**<br>**explanation** $x = \frac{2 \pm 6i}{2} = 1 \pm 3i$, ХОЁУЛАНГ нь 2-т хуваана. Шалгая: нийлбэр $= 2$ ✓, үржвэр $= 1 + 9 = 10$ ✓. |
| 5 | teach | **eyebrow** Гурван тэнгэр, эцсийн хэлбэр · **title** Дискриминантын бүрэн түүх<br>**body** $D > 0$: хоёр бодит шийд, парабол хоёр удаа огтолно. $D = 0$: нэг давтагдсан шийд, орой тэнхлэг дээр. $D < 0$: $p \pm qi$ хосмог хос, парабол тэнхлэгээс хөндий, шийд тайзны гадна. Давхардлыг тоолж комплексийг зөвшөөрвөл квадрат тэгшитгэл бүр яг хоёр шийдтэй, ямар ч үл хамаарах зүйлгүйгээр. (4-р бүлэг үүнийг БҮХ олон гишүүнт рүү өргөжүүлнэ.) |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Тэргүүлэх коэффициент 2<br>**problemId** a223-we2 |
| 7 | tapQuestion | **eyebrow** Шийдээс буцааж байгуулахаа шалгая · **title** Урвуу байгуулалт<br>**prompt** Тэргүүлэх коэффициент нь 1 байх квадрат тэгшитгэлийн шийд нь $3 \pm i$. Түүний сул гишүүн нь:<br>**options** `$10$` · `$9$` · `$8$` · `$6$` — **correctIndex 0**<br>**explanation** Шийдүүдийн үржвэр: $(3+i)(3-i) = 9 + 1 = 10 = c$. (Мөн $b = -(\text{нийлбэр}) = -6$: тэгшитгэл нь $x^2 - 6x + 10$.) |
| 8 | tip | **eyebrow** Зуршил · **title** Нийлбэр, үржвэрийн шалгалт<br>**body** $ax^2 + bx + c$-гийн $r_1, r_2$ шийдийн хувьд: нийлбэр $= -\frac{b}{a}$, үржвэр $= \frac{c}{a}$, бодит ч бай, комплекс ч бай ялгаагүй. Томьёог ажиллуулсны дараа шийдүүдээ нэмж үржүүлэх хоёр секунд нь буцааж орлуулбал минут зарцуулах тэмдгийн алдааг барьж авна. |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Томьёо, комплекс төгсгөлтэй<br>**problemId** a223-t1 |
| 10 | tryIt | **eyebrow** Туршиж үз · **title** Шийдээс байгуулаарай<br>**problemId** a223-t2 |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** $D < 0$: $\sqrt{D} = i\sqrt{|D|}$ бөгөөд томьёо дуусна, $p \pm qi$ хосмог хос. · Графикийн түүх: $D<0$ гэдэг нь парабол $x$ тэнхлэгт хэзээ ч хүрэхгүй гэсэн үг. · Шийдээ нийлбэр $= -b/a$, үржвэр $= c/a$-гаар шалгаарай. |

---

## Lesson 4 — Квадрат тэнцэтгэл биш (`quadratic-inequalities`)

**concreteComparison**

Дрон хоёр хяналтын цэгийн хооронд 30 м-ээс дээш байх ёстой, 30-д БИШ, түүнээс
дээш. «Парабол шулуунаас хаана дээгүүр байна вэ?» гэдэг нь шийдүүдийн хоорондох
асуулт бөгөөд график түүнд ямар ч алгебраас хурдан хариулна.

**objective**

Шийдийг нь олоод шийдүүдийн хооронд ба гадна дахь параболын тэмдгийг уншиж
квадрат тэнцэтгэл биш бодох.

**concept**

1. $x^2 - 2x - 8 < 0$-ийг бодохын тулд: эхлээд ТЭГШИТГЭЛИЙН шийдийг олоорой
   ($x = 4, -2$), дараа нь зургийг уншаарай. Дээшээ нээлттэй парабол шийдийнхээ
   хооронд СӨРӨГ, гадна нь ЭЕРЭГ байна. Тэгэхээр: $-2 < x < 4$.

2. Зааглах цэг нь тэмдгийг дагана: $\le$ шийдийг оруулна, $<$ хасна. Доошоо
   нээлттэй парабол ($a < 0$) уншилтыг эргүүлнэ: хооронд нь эерэг, гадна нь
   сөрөг, эсвэл зүгээр л $-1$-ээр үржүүлээд (тэнцэтгэл бишийг эргүүлээд)
   дээшээ нээлттэй болгоорой.

3. Бодит шийдгүй бол огтлолцол байхгүй: парабол бүхэлдээ нэг талд амьдарна.
   $x^2 + 2x + 5 > 0$ ($D = -16$): үргэлж үнэн (дээшээ нээлттэй, дээгүүр
   хөвнө); $x^2 + 2x + 5 < 0$: хэзээ ч үнэн биш, шийдийн олонлог хоосон.

**keyIdea**

Эхлээд шийд, дараа нь зураг: дээшээ нээлттэй парабол шийдийнхээ хооронд сөрөг,
гадна нь эерэг; шийдгүй бол үүрд нэг талдаа.

**facts**

| title | latex | explanation |
|---|---|---|
| Тэмдгийн зураглал | `a > 0: \;\; +\;|\;-\;|\;+ \;\text{ (гадна, хооронд, гадна)}` | Шийд бол параболын цорын ганц тэмдэг солих цэг. |
| Огтлолцолгүй | `D < 0: \text{ хаана ч ижил тэмдэгтэй (} a \text{-гийн тэмдэг)}` | Дурын нэг цэгийг шалгаарай, 0 хамгийн амар. |

**workedExamples**

- `a224-we1` — **statement:** $x^2 - 2x - 8 \le 0$-ийг бодоорой.
  **solution:** Шийд: $(x-4)(x+2) = 0 \to x = 4, -2$. Дээшээ нээлттэй парабол:
  хооронд нь сөрөг. $\le$ тул шийдийг хадгална: $-2 \le x \le 4$. $x = 0$-г
  шалгая: $-8 \le 0$ ✓.
- `a224-we2` — **statement:** Бөмбөгийн өндөр $h(t) = -5t^2 + 30t$ м. Ямар
  хугацаанд 40 м-ээс дээш байх вэ?
  **solution:** $-5t^2 + 30t > 40 \to -5t^2 + 30t - 40 > 0$; $-5$-д хуваая
  (эргүүлнэ!): $t^2 - 6t + 8 < 0 \to (t-2)(t-4) < 0$. Шийдийн хооронд:
  $2 < t < 4$, хоёр секундын цонх.

**commonMistakes**

- **text:** $x^2 < 9$-ийг $x < 3$ гэж бодох.
  **correction:** Хоёр шийд: $\pm 3$; тэдний хооронд сөрөг: $-3 < x < 3$.
  Тэнцэтгэл бишийн «хоёр талаас нь квадрат язгуур авах» нь зүүн сүүлийг
  чимээгүйхэн унагана.
- **text:** Тэнцэтгэл бишийг сөрөг тоонд хуваахдаа эргүүлэхгүй байх:
  $-5t^2 + 30t - 40 > 0 \to t^2 - 6t + 8 > 0$.
  **correction:** $-5$-д хуваах нь тэмдгийг ЭРГҮҮЛНЭ:
  $t^2 - 6t + 8 < 0$. (Эсвэл сөрөг тэргүүлэх коэффициентийг хэвээр нь үлдээж
  доошоо нээлттэй параболыг уншаарай.)

**tryIt**

- `a224-t1` — $x^2 + 3x - 10 > 0$-ийг бодоорой.
  **solution:** Шийд: $(x+5)(x-2) = 0 \to x = -5, 2$. Дээшээ нээлттэй, ГАДНА
  нь эерэг: $x < -5$ эсвэл $x > 2$.
- `a224-t2` — $x^2 + 4x + 7 < 0$-ийг бодоорой.
  **solution:** $D = 16 - 28 = -12 < 0$: огтлолцолгүй, дээшээ нээлттэй, парабол
  ХААНА Ч эерэг. Тэнцэтгэл биш хэзээ ч хангагдахгүй: шийдгүй.

### Interactive — same twelve steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Цэг биш, муж<br>**body** Тэгшитгэл агшинг тогтооно, бөмбөг $t = 2$ ба $t = 4$-д 40 м-Д байна. Бодит хязгаарлалт нь муж байдаг: хэзээ түүнээс ДЭЭШ байна вэ? Квадратын хувьд энэ бол завсрын асуулт бөгөөд шийдүүдээ барьсан бол параболын зураг нэг харцаар хариулна. |
| 1 | parabolaGraph | **eyebrow** Тоглож үз · **title** Тэмдгийн мужийг уншаарай<br>**teach** Энэ параболын шийдүүд эрэг дээр байна. Муруй шийдүүдийнхээ дунд чанд тэнхлэгээс ДООГУУР, гадна нь ДЭЭГҮҮР байна, шийдүүдийг чирээд хэв маяг хэзээ ч өөрчлөгддөггүйг (дээшээ нээлттэй байх зуур) баталгаажуулаарай. Тэмдгийн муж шийдүүдэд наалдсан байдаг.<br>**config** unchanged (`mode: roots`, `a: 1`, `k: -4`) |
| 2 | teach | **eyebrow** Арга · **title** Шийд, зураг, тэмдэг<br>**body** Гурван алхам. (1) $ax^2 + bx + c = 0$ ТЭГШИТГЭЛИЙГ бодоорой, үржигдэхүүнд задлах эсвэл томьёогоор. (2) Параболыг төсөөлөөрэй: $a$-гийн тэмдгээр дээш эсвэл доош; дээшээ бол шийдүүдийн хооронд сөрөг. (3) Тэмдгийг тааруулаарай: $< 0$ нь сөрөг мужийг, $> 0$ нь эерэгийг хүснэ; $\le/\ge$ зааглах шийдийг хадгалж, чанд тэмдэг хаяна. |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Шийдүүдийн хооронд<br>**problemId** a224-we1 |
| 4 | tapQuestion | **eyebrow** Мужуудаа шалгая · **title** Аль муж вэ?<br>**prompt** $x^2 - 9 > 0$ яг хэзээ биелэх вэ:<br>**options** `$x < -3$ эсвэл $x > 3$` · `$-3 < x < 3$` · `зөвхөн $x > 3$` · `$x \ne \pm 3$` — **correctIndex 0**<br>**explanation** Шийд $\pm 3$, дээшээ нээлттэй: ГАДНА нь эерэг. Ганц сүүлт хариу $(-4)^2 - 9 = 7 > 0$ гэдгийг мартаж байна. |
| 5 | worked | **eyebrow** Бодсон жишээ · **title** Дроны цонх<br>**problemId** a224-we2 |
| 6 | tapQuestion | **eyebrow** Эргүүлэлтээ шалгая · **title** −2-т хуваах<br>**prompt** $-2x^2 + 8 \ge 0$ нь дараахтай эквивалент:<br>**options** `$x^2 - 4 \le 0$` · `$x^2 - 4 \ge 0$` · `$x^2 + 4 \le 0$` · `$x^2 \ge 4$` — **correctIndex 0**<br>**explanation** $-2$-т хуваах нь тэмдгийг эргүүлнэ: $x^2 - 4 \le 0$, өөрөөр хэлбэл $-2 \le x \le 2$. Анхны доошоо нээлттэй параболыг ӨӨРИЙНХ нь шийдүүдийн хооронд уншсантай ижил хариу. |
| 7 | teach | **eyebrow** Онцгой тохиолдол · **title** Шийдгүй бол нэг хариу<br>**body** $D < 0$ гэдэг нь парабол хэзээ ч огтлохгүй гэсэн үг, тэр бүхэлдээ эерэг (дээшээ нээлттэй) эсвэл бүхэлдээ сөрөг (доошоо нээлттэй). Тэгвэл тэнцэтгэл биш ҮРГЭЛЖ үнэн эсвэл ХЭЗЭЭ Ч үнэн биш. Хийсвэрээр бүү бодоорой: $x = 0$-г шалгаад шийдвэрийг уншаад дуусгаарай. |
| 8 | tip | **eyebrow** Зуршил · **title** Нэг цэгийг шалгаарай<br>**body** Шийдийн завсар бичсэнийхээ дараа түүний доторх нэг цэг, гаднах нэг цэгийг АНХНЫ тэнцэтгэл бишид шалгаарай. Арван секунд, мөн энэ нь эргүүлсэн тэмдэг, унагасан сүүл, зааглах цэгийн алдаа, өөрөөр хэлбэл энэ сэдвийн алдааны бүх каталогийг барьж авна. |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Шийдүүдийн гадна<br>**problemId** a224-t1 |
| 10 | tryIt | **eyebrow** Туршиж үз · **title** Огтлолцолгүй<br>**problemId** a224-t2 |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** Эхлээд шийд, дараа нь параболыг уншаарай: дээш → хооронд нь сөрөг, гадна нь эерэг. · Сөрөг тоонд хуваах нь тэмдгийг эргүүлнэ; $\le$ шийдийг хадгалж, $<$ хаяна. · $D < 0$: үргэлж эсвэл хэзээ ч үгүй, нэг цэгийг шалгаарай. |

---

## PRACTICE

- `a22-pr-1` — $y = x^2 + 4x - 1$-ийг оройн хэлбэрт бичээрэй.
  **solution:** $(x + 2)^2 - 5$. Орой $(-2, -5)$.
- `a22-pr-2` — $y = 3x^2 + 6x + 7$-г оройн хэлбэрт хөрвүүлээрэй.
  **solution:** $3(x^2 + 2x) + 7 = 3(x+1)^2 + 4$. Орой $(-1, 4)$.
- `a22-pr-3` — $(4 - 3i) + (2 + 7i)$ ба $(1 + 2i)(3 - 2i)$-ийг хялбарчлаарай.
  **solution:** $6 + 4i$; мөн $3 - 2i + 6i - 4i^2 = 7 + 4i$.
- `a22-pr-4` — $i^{23}$-ийг хялбарчлаарай.
  **solution:** $23 = 4(5) + 3$: $i^{23} = i^3 = -i$.
- `a22-pr-5` — $\dfrac{4 + 2i}{1 - i}$-ийг $a + bi$ хэлбэрт бичээрэй.
  **solution:** $\frac{1+i}{1+i}$-гээр:
  $\frac{4 + 4i + 2i + 2i^2}{2} = \frac{2 + 6i}{2} = 1 + 3i$.
- `a22-pr-6` — $x^2 + 2x + 5 = 0$-ийг бодоорой.
  **solution:** $D = 4 - 20 = -16$: $x = \frac{-2 \pm 4i}{2} = -1 \pm 2i$.
- `a22-pr-7` — $x^2 - 5x - 14 > 0$-ийг бодоорой.
  **solution:** Шийд $7, -2$; гадна нь эерэг: $x < -2$ эсвэл $x > 7$.
- `a22-pr-8` — $x^2 - 6x + 9 \le 0$-ийг бодоорой.
  **solution:** $(x - 3)^2 \le 0$: квадрат хэзээ ч сөрөг байдаггүй тул зөвхөн
  $x = 3$ тохирно.

---

## TEST YOURSELF

- `a22-ty-1` — $y = -2x^2 + 8x - 3$-ийг оройн хэлбэрт хөрвүүлээд хамгийн их
  утгыг хэлээрэй.
  **solution:** $-2(x^2 - 4x) - 3 = -2(x-2)^2 + 5$. Хамгийн их утга $x = 2$-д
  5.
- `a22-ty-2` — $(2 - 5i)^2$-ийг тооцоолж $a + bi$ хэлбэрт бичээрэй.
  **solution:** $4 - 20i + 25i^2 = -21 - 20i$.
- `a22-ty-3` — $\dfrac{7 - i}{3 + i}$-ийг $a + bi$ хэлбэрт бичээрэй.
  **solution:** Хосмогоор:
  $\frac{(7-i)(3-i)}{10} = \frac{21 - 7i - 3i + i^2}{10} = \frac{20 - 10i}{10} = 2 - i$.
- `a22-ty-4` — $4x^2 - 4x + 5 = 0$-ийг бодоорой.
  **solution:** $D = 16 - 80 = -64$:
  $x = \frac{4 \pm 8i}{8} = \frac{1}{2} \pm i$.
- `a22-ty-5` — Шийд нь $-2 \pm 5i$ байх, тэргүүлэх коэффициент нь 1 байх
  квадрат тэгшитгэл бичээрэй.
  **solution:** Нийлбэр $-4$, үржвэр $4 + 25 = 29$: $x^2 + 4x + 29$.
- `a22-ty-6` — Салютын өндөр $h(t) = -5t^2 + 40t$. Ямар хугацаанд 60 м-ээс
  дээш байх вэ?
  **solution:** $-5t^2 + 40t - 60 > 0 \to t^2 - 8t + 12 < 0 \to (t-2)(t-6) < 0$:
  $2 < t < 6$.

---

## Notes for Khas

### 1. The heaviest draft overlap in the programme — and one lesson replaces a six-lesson unit

**Three of these four lessons re-teach material already drafted**, and the
fourth is the only genuinely new one:

| lesson | already drafted in |
|---|---|
| L1 Оройн хэлбэр | `10/quadratic-functions` L2 `vertex-form` **and** `algebra-1/quadratic-equations` L2 |
| **L2 Комплекс тоо** | **`11/complex-numbers` — the entire six-lesson topic, in one 13-step lesson** |
| L3 Томьёо ба комплекс шийд | `algebra-1/quadratic-equations` L2 **and** `11/complex-numbers` L5 |
| L4 Квадрат тэнцэтгэл биш | **nothing — see Notes 5** |

**L2 is the sharpest case in this file.** Review pile 6g recorded an ЭШ topic
teaching logarithms three times across three units. This is worse in one
respect: **the ЭШ topic Комплекс тоо has exactly two units, and both of them
teach complex numbers from scratch.** Unit 1 spends six lessons on it; unit 2
opens its lesson 2 with «$x^2 = -1$ бодит шийдгүй» as though the reader had
never met $i$ — after unit 1 has done powers of $i$, the complex plane, and the
conjugate-root theorem.

**I have made the Mongolian consistent across both**, which is the 6g remedy:
every overlapping term is copied from `11/complex-numbers`, not re-decided. But
consistency is not the issue here — **the repetition is**, and it is an
English-content call I have not touched.

If the spiral is deliberate, unit 2's lesson 2 should acknowledge unit 1 rather
than re-introducing $i$. If it is not, one of the two is redundant, and the
cheaper cut is obvious: unit 2's L2 is 13 steps against unit 1's 54.

### 2. «хосмог» is now used in three drafts, all consistently

The commitment made in `algebra-2/radicals-and-rational-exponents` (Notes 4 of
that draft) said `algebra-2/quadratics-and-complex-numbers` **must** use
«хосмог» or the radical-conjugate cross-reference fails retroactively.

**It does.** All three drafts now agree:

| draft | sense | uses |
|---|---|---|
| `algebra-2/radicals-and-rational-exponents` | radical conjugate | the borrowing |
| `11/complex-numbers` | complex conjugate (ministry's home sense) | the grounding |
| this draft, L2 | complex conjugate, and L2 explicitly names the radical link | both |

L2's division step says the trick is «хуваарийг иррационалаас чөлөөлөхтэй
ижил, зөвхөн язгуурын үүргийг $i$ гүйцэтгэж байна» — which is the English's own
sentence and now lands on vocabulary the student has already met in the
radicals unit. **That is the cross-reference working as intended**, and it is
the first time a borrowing made three drafts ago has paid off in the text
rather than in a note.

Review pile 4j's third instance still applies: if you rule for «нөхөр тоо», it
is three drafts, not one.

### 3. A correction: *completing the square* is «бүтэн квадрат ялгах»

`algebra-1/quadratic-equations` records it as **«бүтэн квадрат болгох»**,
grounded as "corpus 1". The ministry has the phrase:

> **10.5б**: «Квадрат тэгшитгэлийг **бүтэн квадрат ялгах** аргаар бодох,
> ерөнхий томьёо гаргах, шийдийг шинжлэх»

| form | ministry | exam | shipped mirrors | my drafts |
|---|---|---|---|---|
| «бүтэн квадрат **ялгах**» | **1, verbatim** | 0 | **5** | 0 |
| «бүтэн квадрат **болгох**» | 0 | 0 | 1 | **7** (all in that one draft) |

So the ministry *and* the shipped mirrors point the same way, 5 against 1, and
only my draft uses the other form. **This is 6l and 2g agreeing**, which has
not happened before — the earlier 6l cases had the ministry silent and the
mirrors silent too.

This draft uses «бүтэн квадрат ялгах». `algebra-1/quadratic-equations` should
follow; it is a seven-instance find-and-replace in an unshipped draft.

### 4. «оройн хэлбэр» is the one coinage, and it sits on grounded ground

*Vertex form* scores zero as a phrase. But *vertex* is solid: the exam has
**«параболын оройн цэг»** as a subtopic label and in question bodies
(«$y = x^2 - 6x + 11$ параболын оройн цэгийн координатыг ол»), and
`10/quadratic-functions` already settled «орой / оройн цэг» on 602 corpus uses.

«оройн хэлбэр» is compositional on that, parallel to «стандарт хэлбэр», and
reads unambiguously. Low risk, but it is a coinage and this is where they go.

### 5. A second 6j — and this one the exam tests 33 times

**The most consequential finding in this draft, and it is about
`lib/esh-course.ts` rather than about Mongolian.**

Lesson 4 teaches quadratic inequalities. The ministry requires them in two
**core** objectives:

> **11.1б** «Квадрат тэнцэтгэл биш бодох (шийдийг тоон шулуун дээр дүрслэх)»
> **11.1в** «Квадрат тэнцэтгэл бишийг графикийн аргаар бодох, квадрат гурван
> гишүүнт үргэлж эерэг (сөрөг) утгатай байх нөхцөлийг мэдэх»

Both are claimed by **`algebra-1/inequalities`** — ЭШ Algebra unit 2:

```
"inequalities": ["10.5а", "10.5г", "11.1б", "11.1в", "12.1а"],
```

**That topic contains no quadratic content at all.** Its four lessons are
`solving-and-graphing-inequalities`, `multi-step-inequalities`,
`compound-inequalities`, `absolute-value-equations-and-inequalities`, and the
file has **zero** occurrences of "quadratic", "parabola" or "$x^2$".

**Meanwhile the exam tests this 33 times** (`skill_tag: quadratic_inequality`,
plus 3 more under `quadratic_inequality_parameter`) — one of the most-tested
tags in the bank.

**Why this is worse than the geometry 6j.** There the uncovered objective
(10.12в, cross-sections) is tested rarely. Here:

- the content **does** exist in the course, in this unit's L4 — so it is not
  missing, it is **filed under the wrong topic entirely**;
- a student working the **Algebra** block to learn inequalities reaches unit 2,
  which claims 11.1б/в and does not teach them, and the actual teaching sits in
  **Комплекс тоо**, a topic they may never open;
- and the exam tests it 33 times.

So the mapping is wrong in a way that misroutes students on a heavily-tested
objective. **Two fixes, neither of which I have made:** move 11.1б/11.1в onto
`quadratics-and-complex-numbers`, which is merely honest bookkeeping; or move
the *lesson* into the Algebra block, which is a curriculum call and yours.

This is the second instance of the same class, and both were found by reading a
unit's actual content against its claimed objectives. **The check I suggested
under the first one — validate mappings against content — would have caught
both.** Recorded as review pile 6o.

### 6. Decimals

**Zero.** Counted with 2d's command, not estimated. Every value is an exact
integer, fraction or complex number.

**2d stands at 440 shipping across 39 drafts** — unchanged, and this is the
fourth draft in seven to add none.

### 7. Two bare-imperative advisories, judged and kept

Both are the same word, «хас», in lesson 1's converter title «Шидэт квадратыг
нэмээд хас» and its recap point «$(b/2)^2$-ийг нэмээд хас». This is the
drill-chant pattern kept in `10/rational-expressions`, `11/logarithms` and
`algebra-2/systems-and-nonlinear-models`: a two-verb staccato pair mirroring
the English's own «Add and subtract the magic square», in a title rather than
in task wording. Review pile 1a.

---

**ЭШ status:** **Комплекс тоо is complete — two of two.** That makes **six of
fourteen** ЭШ topics fully drafted and **32 of 72 units**. Remaining topics by
distance-to-complete: Комбинаторик, Функц ба график, Тоо ба үсэгт илэрхийлэл,
Магадлал, Өгөгдлийн шинжилгээ (4 each); Анализын эхлэл, Тригонометр (6 each);
Вектор ба матриц (8).
