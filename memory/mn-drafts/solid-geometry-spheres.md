# Draft — `solid-geometry/spheres`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**This closes an ЭШ topic.** *Геометр ба хэмжигдэхүүн* is a twelve-unit block
and this is unit 12, so with it Geometry becomes the **sixth of fourteen** ЭШ
topics fully drafted.

**Four lessons, 30 items, 28 interactive steps, 12 nested tryItSet problems.**
(8 workedExamples + 8 tryIt + 8 practice + 6 testYourself; the other 22 `id`
fields are figure `points`.)

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. Written to `docs/mn-voice-reference.md` from the first
line: no em-dash parentheticals (§9), decimal comma in prose (§7), hyphenated
case suffixes (§8), condition before thing (§1).

**Base vocabulary is `GEOMETRY-TERMS.md`**, plus the corrections recorded as
review pile 6k and 6l: **эзлэхүүн**, **хажуу / бүтэн гадаргуугийн талбай**.

**Shipped-mirror check:** no overlap. No `*-mn` mirror teaches spheres.

> **The finding that frames this whole draft: the ЭШ bank does not test
> spheres.** Not once, in 54 papers. Details and the evidence in Notes 1 — it
> matters because unit 12 is the last unit of the heaviest geometry block, and
> because it is the exact inverse of the situation in unit 11.

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| sphere (the solid) | **бөмбөрцөг** | **ministry 10.12б** · exam **0** — Notes 1 |
| sphere (the surface) | **бөмбөрцгийн гадаргуу** | compositional — Notes 2 |
| ball | *(rendered «бөмбөрцөг»)* | **«бөмбөг» is unavailable** — Notes 2 |
| great circle | **их тойрог** | **ungrounded** — Notes 3 |
| hemisphere | **хагас бөмбөрцөг** | compositional; settled in unit 9 |
| section (of a solid) | **огтлол** | ministry 11 · exam 82 |
| tangent plane | **шүргэгч хавтгай** | «шүргэгч» ministry 4 · exam 54 |
| inscribed in | **…-д багтсан** | **exam 47, verbatim construction** — Notes 4 |
| circumscribed about | **…-г багтаасан** | **exam 9, verbatim construction** · dictionary p. 63 |
| space diagonal | **огторгуйн диагональ** | ministry «диагональ» 10.12в |
| snug (cylinder/box) | **багтаах хамгийн бага** | descriptive |

> **Carried in from review pile 6k/6l, not re-decided here:** volume is
> **эзлэхүүн**; lateral and total surface area are **хажуу / бүтэн
> гадаргуугийн талбай**. This draft is written to the corrected forms, so it
> and `cylinders-and-cones` agree with each other and both differ from unit 9
> until you rule.

---

## Topic-level strings

**TITLE:** Бөмбөрцөг

**BLURB:** Төгс биет: зүсэлт бүр нь тойрог, гадаргуу нь яг дөрвөн сүүдэр
тойрог, эзлэхүүн нь өөрийн лаазныхаа гуравны хоёр, мөн Архимед сүүлчийн
баримтдаа дурлаж булшныхаа чулуун дээр сийлүүлжээ.

---

## Lesson 1 — Бөмбөрцөг ба түүний огтлол (`the-sphere-and-its-sections`)

**concreteComparison**

Жүржийг хаанаас ч зүсээрэй, голоор нь ч, оройд нь ойр ч, ямар ч налуугаар,
зүсэгдсэн тал нь үргэлж төгс тойрог байна. Голд ойр том зүсэлт, ирмэгт ойр
жижиг таг, гэхдээ хэзээ ч зууван биш, хэзээ ч булантай биш. Жүрж ганцхан
огтлол мэднэ.

**objective**

Бөмбөрцгийн тодорхойлолтыг хэрэглэж, r² = R² − d² (бөмбөрцгийн гол гурвалжин)-
ээр огтлолын радиусыг тооцоолох.

**concept**

1. $R$ радиустай **бөмбөрцөг**: төвөөсөө яг $R$ зайд орших бүх цэг. (Биет
   хувилбар нь, өөрөөр хэлбэл $R$ зайн дотор байгаа бүхэн, мөн бөмбөрцөг
   гэж нэрлэгдэнэ.) Ганц тоо $R$ түүний талаарх бүхнийг захирна.

2. Бөмбөрцгийн хавтгай огтлол БҮР тойрог байна. Төвөөр нь дайруулсан зүсэлт
   нь $R$ радиустай **их тойрог** буюу боломжит хамгийн том нь (Дэлхийн
   экватор). Төвөөс $d$ зайд хийсэн зүсэлт жижиг: түүний радиус
   $r^2 = R^2 - d^2$-ыг дагана, учир нь төвөөс зүсэх хавтгай руу буулгасан
   перпендикуляр (1-р бүлэг!) $R$-г гипотенуз болгосон тэгш өнцөгт гурвалжин
   үүсгэнэ.

3. Шүргэгч хавтгай яг нэг цэгт хүрэх бөгөөд $d = R$ зайд байна (огтлолын
   радиус 0 болж агшина). {$d$, $r$, $R$} гол гурвалжин «зүсэлт хэр том вэ»
   гэсэн асуулт бүрд хариулна, энэ бол тойргийн геометрийн хөвч-зайн
   гурвалжны 3D ихэр юм.

**keyIdea**

Огтлол бүр нь r² = R² − d² байх тойрог. Их тойрог: d = 0, r = R. Шүргэгч
хавтгай: d = R, r = 0.

**facts**

| title | latex | explanation |
|---|---|---|
| Бөмбөрцөг | `\{P : |PO| = R\}` | Нэг төв, нэг радиус, бүрэн тэгш хэм. |
| Огтлолын радиус | `r^2 = R^2 - d^2` | d = төвөөс зүсэх хавтгай хүртэлх зай. |
| Их тойрог | `d = 0 \Rightarrow r = R` | Хамгийн том огтлол, экваторын зүсэлт. |

**workedExamples**

- `sg51-we1` — **statement:** $5$ радиустай бөмбөрцгийг төвөөсөө $3$ зайд
  байрлах хавтгайгаар зүслээ. Огтлолын радиус ба талбайг олоорой.
  **solution:** $r = \sqrt{25 - 9} = 4$ (бөмбөрцөг доторх 3-4-5 гурвалжин).
  Огтлолын талбай: $\pi r^2 = 16\pi \approx 50.3$.
- `sg51-we2` — **statement:** Хавтгай $13$ радиустай бөмбөрцгийг $12$
  радиустай тойргоор зүслээ. Хавтгай төвөөс хэр хол вэ?
  **solution:** $d = \sqrt{R^2 - r^2} = \sqrt{169 - 144} = 5$, өөрөөр хэлбэл
  гурвалжинг ухраан ажиллуулсан 5-12-13 гурвал.

**commonMistakes**

- **text:** Налуу зүсэлтээс зууван эсвэл олон өнцөгт огтлол гарна гэж хүлээх.
  **correction:** Бөмбөрцөгт «налуу» гэж байхгүй, тэр бүх зүгээс ижил
  харагддаг тул хавтгай зүсэлт бүр тойрог байна. (Зууван огтлол нь өнцгөөр
  зүссэн цилиндр, конусынх болохоос бөмбөрцгийнх биш.)
- **text:** $r^2 = R^2 + d^2$ гэж бичих (хасахын оронд нэмэх).
  **correction:** $R$ бол гол гурвалжны ГИПОТЕНУЗ буюу төвөөс огтлолын ирмэг
  хүртэлх налуу зам. Огтлолын радиус бол катет: $r^2 = R^2 - d^2$, мөн огтлол
  их тойргийг хэзээ ч дийлж чадахгүй ($r \le R$).

**tryIt**

- `sg51-t1` — Бөмбөрцгийн радиус $10$, зүсэх хавтгай $6$ зайд: огтлолын
  радиус ба талбай?
  **solution:** $r = \sqrt{100 - 36} = 8$ (6-8-10); талбай
  $= 64\pi \approx 201$.
- `sg51-t2` — $d$ зайд байгаа огтлол их тойргийн талбайн ХАГАСТАЙ тэнцүү
  талбайтай. $d$-г $R$-ээр илэрхийлээрэй.
  **solution:** $\pi r^2 = \frac12 \pi R^2$ тул $r^2 = \frac{R^2}{2}$,
  тэгэхээр $d^2 = R^2 - \frac{R^2}{2} = \frac{R^2}{2}$:
  $d = \frac{R}{\sqrt2} = \frac{R\sqrt2}{2} \approx 0.71R$. (Яг хагас замд нь
  биш! Талбай төвийн ойролцоо удаан агшдаг.)

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Тодорхойлолт · **title** Нэг төв, нэг зай<br>**body** Бөмбөрцөг = $O$ төвөөс $R$ зайд орших бүх цэг. Ирмэг ч үгүй, орой ч үгүй, давуу чиглэл ч үгүй, цорын ганц төгс тэгш хэмтэй гадаргуу. Хавтгайд зурахдаа: гүнийг илэрхийлэхийн тулд тасархай «экватор» зууван бүхий тойрог; математикт зөвхөн $O$ ба $R$ хэрэгтэй. |
| 1 | solid3d | **eyebrow** Тоглож үз · **title** Бөмбөрцөг, амьдаар<br>**teach** Ганц алхамч, энэ бол бүтэн бөмбөрцөг. Гадаргуу ба эзлэхүүн π-гийн яг үржвэр болохыг ажиглаарай. Хоёр томьёо дараагийн хичээлүүдэд ирнэ; одоохондоо тэдний өсөх хурдыг анзаараарай: радиус 2 дахин ⟹ гадаргуу 4 дахин, эзлэхүүн 8 дахин.<br>**config** unchanged (`solid: sphere`, `r: 3`) |
| 2 | teach | **eyebrow** Огтлол · **title** Гол гурвалжин: d, r, R<br>**body** Төвөөс $d$ зайд зүсээрэй: зүсэх хавтгай руу $OF = d$ перпендикулярыг буулгаад (1-р бүлгийн алхам) огтлолын ирмэг рүү хүрээрэй, тэр нь $R$ гипотенуз. Огтлолын радиус бол нөгөө катет, $R = 5$, $d = 3$-ын хувьд доор жинхэнэ хэмжээгээр зурагдсан: $r = \sqrt{25 - 9} = 4$. Огтлолын асуулт бүр энэ ганц гурвалжин. |
| 3 | tapQuestion | **eyebrow** Шалгая · **title** Жүржийг зүсээрэй<br>**prompt** Бөмбөрцөг $R = 13$, төвөөс $d = 5$ зайд зүслээ. Огтлолын радиус?<br>**options** `$12$` · `$\sqrt{194}$` · `$8$` · `$13$` — **correctIndex 0**<br>**explanation** $r = \sqrt{169 - 25} = 12$, 5-12-13 гурвалжин. Хасахын оронд нэмбэл боломжгүй $\sqrt{194} > R$ гарна; огтлол их тойргийг хэзээ ч дийлэхгүй. |
| 4 | workedSet | **eyebrow** Бодсон жишээ · **title** Урагш ба ухраа<br>**intro** Гурвалжин ямар ч чиглэлд бодогдоно: {d, r, R}-ээс хоёрыг өгвөл гурав дахь нь гарна.<br>**ex1** $R = 5$, $d = 3$: огтлолын радиус ба талбай? · алхам: $r = \sqrt{25 - 9} = 4$. · алхам: Талбай $= 16\pi$. · **хариу** $r = 4$, талбай $16\pi$<br>**ex2** Огтлолын радиус $12$, зай $5$: бөмбөрцгийн радиус? · алхам: Одоо $R$ нь үл мэдэгдэх гипотенуз. · алхам: $R = \sqrt{144 + 25} = 13$. · **хариу** $R = 13$ |
| 5 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Огтлолын дасгал<br>**intro** Эхлээд d–r–R гурвалжныг зураарай; мэдэж байгаагаа шошголоорой.<br>**p1** $R = 10$, $d = 8$: огтлолын радиус? — **choices** `$6$` · `$2$` · `$\sqrt{164}$` — **answerIndex 0** — $\sqrt{100 - 64} = 6$, 6-8-10.<br>**p2** $R$ радиустай бөмбөрцгийн шүргэгч хавтгай төвөөс хэр зайд байрлах вэ? — **choices** `яг $R$` · `$0$` · `$R$-ээс их` — **answerIndex 0** — Нэг цэгт хүрнэ гэдэг нь огтлолын тойрог 0 радиус болж агшсан гэсэн үг: $d = R$. Үүнээс хол бол огт алдана; ойр бол жинхэнэ тойрог зүснэ.<br>**p3** Дэлхийг ($R \approx 6371$ км) 60 дахь параллелиар зүсэв, энд $d = \frac{R\sqrt3}{2}$. Параллелийн радиус нь — **choices** `$R/2$` · `$R\sqrt3/2$` · `$R/\sqrt3$` — **answerIndex 0** — $r = \sqrt{R^2 - \frac{3R^2}{4}} = \frac{R}{2}$. 60° өргөрөгт тогтмол өргөрөгийн тойрог экваторын яг ХАГАС, хойшоо явах тусам цагийн бүсүүд хурдан нарийсдаг. |
| 6 | recap | **eyebrow** Эргэн дүгнэлт · **title** Бөмбөрцгийн огтлол |

---

## Lesson 2 — Бөмбөрцгийн гадаргуугийн талбай (`surface-area-of-a-sphere`)

**concreteComparison**

Жүржийг болгоомжтой хальсалж, хальсыг нь тэгшлээрэй: тэр жүржийн хамгийн
өргөн хэсгийг тойруулан зурсан яг дөрвөн тойргийг бүрхэнэ. Гурван хагас ч
биш, ойролцоогоор дөрөв ч биш, яг дөрвөн сүүдэр тойрог хальс. Тэр 4 бол бүхэл
томьёо юм.

**objective**

Бөмбөрцөг, хагас бөмбөрцөг, мөн гараг будах бодлогод S = 4πR²-г хэрэглэх.

**concept**

1. $S = 4\pi R^2$: бөмбөрцгийн гадаргуу яг **дөрвөн их тойрогтой** тэнцүү.
   Мөн үүнтэй адилаар түүнийг багтаах хамгийн бага цилиндрийн ХАЖУУ гадаргуутай
   тэнцүү ($2\pi R \cdot 2R = 4\pi R^2$), өөрөөр хэлбэл Архимед бөмбөрцөг ба
   түүний лааз ижил ханын цаастай гэдгийг баталсан.

2. Масштаблалт: гадаргуу радиусын КВАДРАТААР өснө. $R$-г хоёр дахин: 4 дахин
   их будаг. Том гаригуудыг жижиг саруудаас хамаагүй хэцүү зурагладгийн учир
   нь энэ.

3. **Хагас бөмбөрцөг** бол сонгодог урхи: БӨМБӨГӨР ТАГ нь $2\pi R^2$ боловч
   битүү хагас бөмбөрцөгт шал хэрэгтэй, өөрөөр хэлбэл их тойргийн дугуй
   $\pi R^2$, нийлээд $3\pi R^2$. Бодлогын бөмбөгөр таг нээлттэй юу, битүү юу
   гэдгийг уншаарай.

**keyIdea**

S = 4πR², өөрөөр хэлбэл дөрвөн их тойрог, эсвэл багтаах хамгийн бага лаазны
шошго. Битүү хагас бөмбөрцөг: 2πR² бөмбөгөр таг + πR² шал = 3πR².

**facts**

| title | latex | explanation |
|---|---|---|
| Бөмбөрцгийн гадаргуу | `S = 4\pi R^2` | Яг дөрвөн их тойргийн дугуй хальс. |
| Архимедийн лааз | `S_{\text{бөмб}} = S_{\text{хаж, цил}}` | Бөмбөрцгийн гадаргуу = түүнийг багтаах лаазны шошго. |
| Битүү хагас бөмбөрцөг | `2\pi R^2 + \pi R^2 = 3\pi R^2` | Бөмбөгөр таг дээр нэмээд шалны дугуй. |

**workedExamples**

- `sg52-we1` — **statement:** Радиус нь $6$ байх бөмбөрцгийн гадаргуугийн
  талбайг яг таг ба ойролцоогоор олоорой.
  **solution:** $S = 4\pi \cdot 36 = 144\pi \approx 452.4$.
- `sg52-we2` — **statement:** Бөмбөрцгийн гадаргуугийн талбай $100\pi$.
  Радиус ба их тойргийн талбайг олоорой.
  **solution:** $4\pi R^2 = 100\pi$ тул $R^2 = 25$, $R = 5$. Их тойрог:
  $\pi R^2 = 25\pi$, өөрөөр хэлбэл 4 амласны дагуу гадаргуугийн дөрөвний нэг.

**commonMistakes**

- **text:** $4\pi R^2$ (гадаргуу)-г $\pi R^2$ (их тойрог) эсвэл эзлэхүүний
  томьёотой хутгах.
  **correction:** Бүртгэлээ хөтлөөрэй: их тойрог $\pi R^2$ (2D дугуй),
  гадаргуу $4\pi R^2$ (ороодог), эзлэхүүн $\frac43\pi R^3$ (дүүргэдэг).
  Гадаргуу 4 ба КВАДРАТ агуулна; эзлэхүүн 4/3 ба КУБ агуулна.
- **text:** Хагас бөмбөрцгийн гадаргуу бол бодлого бүрд $4\pi R^2$-ын хагас
  буюу $2\pi R^2$.
  **correction:** Энэ нь зөвхөн нээлттэй бөмбөгөр таг. БИТҮҮ хагас бөмбөрцөг
  (биет хагас бөмбөрцөг) хавтгай дугуйг нэмнэ: $2\pi R^2 + \pi R^2 = 3\pi R^2$.
  Планетарийн дээвэр: нээлттэй. Хагас жүрж: битүү.

**tryIt**

- `sg52-t1` — Радиус $3$: бөмбөрцгийн гадаргуу, нээлттэй бөмбөгөр таг, битүү
  хагас бөмбөрцөг?
  **solution:** Бөмбөрцөг: $36\pi$. Бөмбөгөр таг: $18\pi$. Битүү:
  $18\pi + 9\pi = 27\pi$.
- `sg52-t2` — B гараг A гаригаас хоёр дахин том радиустай. B-ийн гадаргууд
  хэдэн дахин их будаг хэрэгтэй вэ? Мөн A-д $80\pi$ хэрэгтэй бол B-д хэд вэ?
  **solution:** $S \propto R^2$: $2^2 = 4$ дахин. B-д $320\pi$ хэрэгтэй.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Дөрөв · **title** Дөрвөн их тойрог хальс<br>**body** $S = 4\pi R^2$. Тэр 4 нь яг таг бөгөөд эртний: Архимед бөмбөрцгийн гадаргуу нь түүнийг багтаах хамгийн бага лаазны хажуу гадаргуутай тэнцүү гэдгийг харуулсан, өндөр нь $2R$, тойргийн урт нь $2\pi R$, шошгоны талбай $4\pi R^2$. Бөмбөрцгийн хэсэг бүрийг хажуу тийш лаазан дээр буулгаарай: талбайнууд хэсэг хэсгээрээ таарна. (Тэр буулгалт нь зарим дэлхийн зураг хийх арга юм, Ламбертын цилиндр зураг яг энэ шалтгаанаар талбайг хадгалдаг.) |
| 1 | teach | **eyebrow** Лааз · **title** Лаазан доторх бөмбөрцөг: ижил ханын цаас<br>**body** $R$ радиустай бөмбөрцгийг багтаах хамгийн бага лааз, огтлолоор зурагдсан: тойрог хоёр хана, шал, тагт хүрнэ. Лаазны шошго: $2\pi R \times 2R = 4\pi R^2$, яг бөмбөрцгийн гадаргуу. Энэ ижил зураг дараагийн хичээлд ЭЗЛЭХҮҮНД өөр харьцаатай (2/3) буцаж ирнэ; хоёулаа хамтдаа Архимедийн хамгийн бахархалтай теорем байв. |
| 2 | tapQuestion | **eyebrow** Шалгая · **title** Дөрөвний нэгийн бүртгэл<br>**prompt** Бөмбөрцгийн гадаргуугийн талбай $64\pi$. Түүний их тойргийн талбай нь<br>**options** `$16\pi$` · `$32\pi$` · `$8\pi$` · `$64\pi/3$` — **correctIndex 0**<br>**explanation** Их тойрог нь гадаргуугийн яг ДӨРӨВНИЙ НЭГ: $\frac{64\pi}{4} = 16\pi$ (энд $R = 4$). $4\pi R^2$-ын 4 нь шууд утгаараа «дөрвөн их тойрог» гэсэн үг. |
| 3 | workedSet | **eyebrow** Бодсон жишээ · **title** Гараг ороох нь<br>**intro** Радиусыг квадратлаад $4\pi$-гээр үржүүлээрэй; хагас бөмбөрцгийн шалнаас болгоомжлоорой.<br>**ex1** $R = 6$: гадаргуу? · алхам: $R^2 = 36$. · алхам: $S = 144\pi$. · **хариу** $144\pi \approx 452$<br>**ex2** Битүү хагас бөмбөрцөг, $R = 4$: бүтэн гадаргуу? · алхам: Бөмбөгөр таг: $2\pi \cdot 16 = 32\pi$. · алхам: Шал: $16\pi$; нийт $48\pi$. · **хариу** $48\pi \approx 150.8$ |
| 4 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Будгийн ажил<br>**intro** 4πR², мөн шалнуудаа тоолоорой.<br>**p1** $R = 5$: бөмбөрцгийн гадаргуу? — **choices** `$100\pi$` · `$25\pi$` · `$500\pi/3$` — **answerIndex 0** — $4\pi \cdot 25 = 100\pi$.<br>**p2** Гадаргуу $36\pi$: радиус? — **choices** `$3$` · `$6$` · `$9$` — **answerIndex 0** — $4\pi R^2 = 36\pi$ тул $R^2 = 9$.<br>**p3** Нээлттэй планетарийн бөмбөгөр тагийг ($R = 10$ м) дотор талаас нь будна. Талбай? — **choices** `$200\pi$` · `$300\pi$` · `$400\pi$` — **answerIndex 0** — Нээлттэй бөмбөгөр таг = бөмбөрцгийн гадаргуугийн хагас: $2\pi \cdot 100 = 200\pi$ м². Тэнгэрт шал байхгүй. |
| 5 | funFact | **eyebrow** Сонирхолтой баримт · **title** Дөрөв яагаад тооцоог хөнгөвчилдөг вэ<br>**body** Дэлхийн гадаргуу $4\pi R^2 \approx 510$ сая км², мөн 4 нь толгойн тооцоог амар болгоно: сансраас харагдах Дэлхийн дугуй ($\pi R^2$) нь бүтэн гадаргуугийн яг дөрөвний нэг. Хиймэл дагуулын бүлгүүд бүрэн хамрах зориулалтаар яг ийм учраас дор хаяж дөрвөн сайн байрлуулсан дагуул шаарддаг: тус бүр нь нэг удаад хамгийн ихдээ нэг их тойргийн дугуй төдий гаригийг «хардаг». |
| 6 | recap | **eyebrow** Эргэн дүгнэлт · **title** Бөмбөрцгийн гадаргуу |

---

## Lesson 3 — Бөмбөрцгийн эзлэхүүн (`volume-of-a-sphere`)

**concreteComparison**

Яг багтах бөмбөгийг түүнд яг таарах цилиндр шилэнд хийгээрэй (ёроол, тагны
түвшин, хананд хүрнэ): бөмбөг шилний зайны яг гуравны хоёрыг эзэлж, усанд
гуравны нэгийг үлдээнэ. Архимед тэр 2:3-ыг маш их үнэлсэн тул
цилиндр-доторх-бөмбөрцөг зургийг булшныхаа чулуун дээр сийлүүлжээ.

**objective**

Бөмбөрцөг, хагас бөмбөрцөг, харьцуулах бодлогод V = ⁴⁄₃πR³-г хэрэглэх, мөн
Кавальерийн аяганы аргументыг үзэх.

**concept**

1. $V = \frac{4}{3}\pi R^3$. Алдартай гарган авалт (Кавальери): өндөр бүр дээр
   бөмбөрцгийн зүсэлтийн талбай нь цилиндрээс хоёр конус хассан биетийн
   зүсэлттэй тэнцүү. Хоёр зүсэлтийн багц түвшин түвшнээрээ таарах тул
   эзлэхүүн нь таарна:
   $\pi R^2 \cdot 2R - 2 \cdot \frac13 \pi R^2 \cdot R = \frac43 \pi R^3$.

2. Архимедийн 2:3: бөмбөрцөг нь түүнийг багтаах хамгийн бага цилиндрийн яг
   $\frac{2}{3}$-ыг дүүргэнэ ($\frac{4/3 \pi R^3}{2\pi R^3} = \frac23$).
   Гадаргуу БА эзлэхүүн хоёул бөмбөрцгийг лаазтай нь цэвэрхэн харьцаагаар
   холбоно, энэ бол булшны чулууны теорем.

3. Масштаблалт: эзлэхүүн КУБААР өснө. Радиусыг хоёр дахин: 8 дахин их зайрмаг.
   Хагас бөмбөрцөг: $\frac23 \pi R^3$.

**keyIdea**

V = ⁴⁄₃πR³, зүсэлт тааруулах аргаар (Кавальери) батлагдсан; бөмбөрцөг нь
түүнийг багтаах хамгийн бага цилиндрийн яг ⅔.

**facts**

| title | latex | explanation |
|---|---|---|
| Бөмбөрцгийн эзлэхүүн | `V = \tfrac{4}{3}\pi R^3` | Радиусыг кубдаад дөрөвний гурван π. |
| Архимедийн 2:3 | `V_{\text{бөмб}} = \tfrac{2}{3} V_{\text{цил}}` | Багтаах хамгийн бага лааз яг 1,5 бөмбөрцөг багтаана. |
| Хагас бөмбөрцөг | `V = \tfrac{2}{3}\pi R^3` | Бөмбөгний хагас. |

**workedExamples**

- `sg53-we1` — **statement:** Радиус нь $3$ байх бөмбөрцгийн эзлэхүүнийг олоод,
  тоон дээр нь нэг зүйл анзаараарай.
  **solution:** $V = \frac43 \pi \cdot 27 = 36\pi \approx 113.1$. Хөгжилтэй
  давхцал: түүний ГАДАРГУУ ч мөн $36\pi$, радиус нь 3 байх бөмбөрцөг бол энэ
  хоёр тоо таарах цорын ганц бөмбөрцөг.
- `sg53-we2` — **statement:** Бөмбөрцөг цилиндрт яг багтаж байна (дээд, доод,
  хананд хүрнэ), $R = 3$. Хоёр эзлэхүүн ба тэдний харьцааг олоорой.
  **solution:** Бөмбөрцөг: $36\pi$. Цилиндр: $\pi \cdot 9 \cdot 6 = 54\pi$.
  Харьцаа: $\frac{36}{54} = \frac{2}{3}$, Архимедийн булшны чулуу.

**commonMistakes**

- **text:** Кубдахын оронд квадратлах (эсвэл 4/3-ыг $R^2$-тэй хэрэглэх).
  **correction:** Эзлэхүүн бол 3D: $R^3$. Хосууд нь гадаргууд (4, квадрат),
  эзлэхүүнд (4/3, куб). Радиус нь 10 бөмбөрцөг: гадаргуу $400\pi$, эзлэхүүн
  $\frac{4000\pi}{3}$, R/3 үржүүлэгчээр ялгаатай.
- **text:** Радиусыг хоёр дахин = эзлэхүүн хоёр дахин гэж бодох.
  **correction:** Куб: $2^3 = 8$ дахин. Зайрмагны лангуун дээр нэг хэмжээ
  дээшлэх нь харагдахаасаа хамаагүй ашигтай, 2 см том халбага хоёр дахин их
  зайрмаг байж мэднэ.

**tryIt**

- `sg53-t1` — Радиус $6$: бөмбөрцгийн эзлэхүүн?
  **solution:** $V = \frac43\pi \cdot 216 = 288\pi \approx 904.8$.
- `sg53-t2` — Бөмбөрцгийн эзлэхүүн $\frac{500\pi}{3}$. Радиус ба гадаргуугийн
  талбайг олоорой.
  **solution:** $\frac43 R^3 = \frac{500}{3}$ тул $R^3 = 125$, $R = 5$.
  Гадаргуу: $100\pi$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Аяганы заль · **title** Кавальери 4/3-ыг баталж байна<br>**body** Хагас бөмбөрцөг ($R$)-ийг оройгоороо доош харсан конус өрөмдөж гаргасан цилиндр ($R$, өндөр $R$)-тэй харьцуулаарай. $y$ өндөрт: хагас бөмбөрцгийн зүсэлт $= \pi(R^2 - y^2)$; өрөмдсөн зүсэлт $= \pi R^2 - \pi y^2$. ТҮВШИН БҮРД тэнцүү тул эзлэхүүн тэнцүү: хагас бөмбөрцөг тутамд $\pi R^3 - \frac{\pi R^3}{3} = \frac{2\pi R^3}{3}$, тэгэхээр бөмбөрцөг тутамд $\frac{4\pi R^3}{3}$. 1-р хичээлийн гол гурвалжин зүсэлтийн талбайг нийлүүлж өгсөн. |
| 1 | solid3d | **eyebrow** Тоглож үз · **title** Куб ажиллаж байна<br>**teach** Радиусыг алхмаар өөрчлөөрэй: 1 → 2 эзлэхүүнийг 8-аар үржүүлнэ; 2 → 4 дахин 8-аар. Гадаргуу удаа бүр ердөө ×4. Эзлэхүүн гадаргуунаас зугтаж байна, том амьтад хэт халж, том гаригууд дотроо геологийн хувьд халуун хэвээр байдгийн учир нь энэ.<br>**config** unchanged (`solid: sphere`, `r: 3`) |
| 2 | tapQuestion | **eyebrow** Шалгая · **title** Булшны чулууны харьцаа<br>**prompt** Багтаах хамгийн бага цилиндр $81\pi$ багтаана. Дотор нь байгаа бөмбөрцөг<br>**options** `$54\pi$` · `$40.5\pi$` · `$27\pi$` · `$60.75\pi$` — **correctIndex 0**<br>**explanation** Яг $\frac23$: $\frac23 \cdot 81\pi = 54\pi$. (Энд $2\pi R^3 = 81\pi$ нь $R^3 = 40.5$ өгнө, сайхан $R$ биш, гэвч ХАРЬЦААНД хамаагүй.) |
| 3 | workedSet | **eyebrow** Бодсон жишээ · **title** Бөмбөгийг дүүргээрэй<br>**intro** Эхлээд кубдаад дараа нь 4π/3.<br>**ex1** $R = 3$: эзлэхүүн? · алхам: $R^3 = 27$. · алхам: $V = \frac43 \cdot 27\pi = 36\pi$. · **хариу** $36\pi \approx 113$<br>**ex2** Хагас бөмбөрцөг аяга, $R = 6$: багтаамж? · алхам: Бүтэн бөмбөг: $288\pi$. · алхам: Хагас: $144\pi$. · **хариу** $144\pi \approx 452$ |
| 4 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Халбага ба гараг<br>**intro** ⁴⁄₃πR³; харьцааг масштабын коэффициентийг кубдаж гаргана.<br>**p1** $R = 2$: эзлэхүүн? — **choices** `$\dfrac{32\pi}{3}$` · `$16\pi$` · `$\dfrac{16\pi}{3}$` — **answerIndex 0** — $\frac43\pi \cdot 8 = \frac{32\pi}{3} \approx 33.5$.<br>**p2** Эзлэхүүн $288\pi$: радиус? — **choices** `$6$` · `$12$` · `$4$` — **answerIndex 0** — $R^3 = \frac{3 \cdot 288}{4} = 216$ тул $R = 6$.<br>**p3** Нэг тарвас нөгөөгөөсөө 3 дахин том радиустай. Тэр ___ дахин их жимс агуулна. — **choices** `$27$` · `$9$` · `$3$` — **answerIndex 0** — $3^3 = 27$. (Мөн хальс нь ердөө $9$ дахин, том тарвас хальс-жимсний харьцаагаараа илүү ашигтай.) |
| 5 | funFact | **eyebrow** Сонирхолтой баримт · **title** Булшны чулуу<br>**body** Архимед булшин дээрээ цилиндр-доторх-бөмбөрцөг дүрсийг тавихыг хүссэн, дайны машинуудаасаа ч, π-гийн хязгаараасаа ч илүү 2:3 харьцаагаараа бахархаж байжээ. МЭӨ 75 онд Цицерон Сицилийн квестор байхдаа (Архимед нас барснаас хойш 137 жилийн дараа) Сиракузын хаалганы ойролцоо булшийг нь «өргөс бударганад дарагдсан» байхад олж, яг тэр жижигхэн бөмбөрцөг ба цилиндрээр нь таньжээ. Эртний математикчийн булшийг хөшөө мэт эргэж очсон тухай бидэнд байгаа бараг цорын ганц түүх энэ юм. |
| 6 | recap | **eyebrow** Эргэн дүгнэлт · **title** Бөмбөрцгийн эзлэхүүн |

---

## Lesson 4 — Багтсан ба багтаасан биет (`inscribed-and-circumscribed-solids`)

**concreteComparison**

Хайрцагтаа байгаа сагсан бөмбөг: бөмбөг зургаан ханд бүгдэд нь хүрдэг тул
хайрцгийн ирмэг НЬ бөмбөгний диаметр, дотор нь соронзон хэмжигч хийх
шаардлагагүй. Харин хайрцгийг БҮРХСЭН бөмбөг (шоог тойрсон бөмбөлөг) хайрцгийн
булангуудад хүрэх ёстой бөгөөд булангийн хүрэлт нь огторгуйн диагональ. Талст
хүрэх ба булан хүрэх: өөр өөр хоёр диаметр.

**objective**

Бөмбөрцгийг түүний багтдаг эсвэл багтаадаг куб, цилиндртэй холбох: аль урт нь
2R-тэй тэнцэх вэ, яагаад вэ.

**concept**

1. **Кубэд багтсан бөмбөрцөг** (хайрцаг доторх бөмбөг): зургаан талстын төвд
   хүрнэ, тэгэхээр $2R = a$ буюу ИРМЭГ. Харьцаа нь мөрдөнө: бөмбөг хайрцгийн
   $\frac{4/3 \pi (a/2)^3}{a^3} = \frac{\pi}{6} \approx 52\%$-ийг дүүргэнэ.

2. **Кубыг багтаасан бөмбөрцөг** (бөмбөг доторх куб): 8 булангаар дайрна,
   тэгэхээр $2R = a\sqrt{3}$ буюу ОГТОРГУЙН ДИАГОНАЛЬ (2-р бүлэг өгөөжөө
   өгч байна). Санах дүрэм: багтсан нь талстад хүрнэ (ирмэг эсвэл өндрийг
   аваарай); багтаасан нь оройнуудад хүрнэ (диагоналийг аваарай).

3. Цилиндрт ижил логик: цилиндрт яг багтсан бөмбөрцөгт $2R = h = 2r_{\text{цил}}$;
   бөмбөрцөгт багтсан цилиндрийн тэнхлэг огтлолын тэгш өнцөгтийн ДИАГОНАЛЬ нь
   бөмбөрцгийн диаметр болно: $(2r)^2 + h^2 = (2R)^2$.

**keyIdea**

Багтсан бөмбөрцөг талстад хүрнэ: 2R = ирмэг эсвэл өндөр. Багтаасан бөмбөрцөг
булангуудад хүрнэ: 2R = огторгуйн диагональ (куб) эсвэл тэнхлэг огтлолын
диагональ (цилиндр).

**facts**

| title | latex | explanation |
|---|---|---|
| Кубэд багтсан бөмбөг | `2R = a` | Талстын төвд хүрнэ, ирмэг = диаметр. |
| Бөмбөгт багтсан куб | `2R = a\sqrt{3}` | Булангуудад хүрнэ, огторгуйн диагональ = диаметр. |
| Бөмбөгт багтсан цилиндр | `(2r)^2 + h^2 = (2R)^2` | Тэнхлэг огтлолын диагональ бөмбөрцгийг гатална. |

**workedExamples**

- `sg54-we1` — **statement:** Кубын ирмэг $6$. Түүнд багтсан ба түүнийг
  багтаасан бөмбөрцгийн радиусууд, мөн хоёр бөмбөрцгийн эзлэхүүний харьцааг
  олоорой.
  **solution:** Багтсан: $R_{\text{дот}} = 3$. Багтаасан:
  $R_{\text{гад}} = \frac{6\sqrt3}{2} = 3\sqrt{3}$. Радиусын харьцаа $\sqrt3$ тул
  эзлэхүүний харьцаа $(\sqrt3)^3 = 3\sqrt{3} \approx 5.2$, өөрөөр хэлбэл
  булан хүрдэг бөмбөг тавь дахин илүү биш ч таваас илүү дахин том.
- `sg54-we2` — **statement:** $r = 3$, $h = 8$ цилиндр бөмбөрцөгт багтжээ.
  Бөмбөрцгийн радиусыг олоорой.
  **solution:** Тэнхлэг огтлолын тэгш өнцөгт $6 \times 8$, диагональ
  $= \sqrt{36 + 64} = 10 = 2R$ тул $R = 5$. 6-8-10 гурвалжин дахин цохилоо.

**commonMistakes**

- **text:** БАГТААСАН бөмбөрцөгт ирмэгийг (эсвэл багтсанд диагоналийг)
  хэрэглэх.
  **correction:** Бөмбөрцөг юунд хүрч байгааг асуугаарай. Талст (багтсан) ⟹
  хамгийн богино гаталт: ирмэг. Орой (багтаасан) ⟹ хамгийн урт гаталт:
  огторгуйн диагональ. Хүрэлт нь диаметрийг тодорхойлно.
- **text:** Бөмбөрцөгт багтсан цилиндрт $2R = h$ эсвэл $2R = 2r$ гэж дангаар
  нь тавих.
  **correction:** Бөмбөрцөг хоёр тагны ИРМЭГТ хүрэх ёстой, өөрөөр хэлбэл
  тэнхлэг огтлолын тэгш өнцөгтийн булан дахь хамгийн хол цэгүүдэд. Хоёр
  хэмжээс хоюулаа ордог: $(2r)^2 + h^2 = (2R)^2$. Зөвхөн доройтсон тохиолдолд
  нэг хэмжээс рүү нурна.

**tryIt**

- `sg54-t1` — Радиус $2$ бөмбөрцөг кубэд яг багтжээ. Кубын эзлэхүүн ба бөмбөг
  эзлэх хэсгийг (яг таг) олоорой.
  **solution:** $a = 2R = 4$: куб $= 64$. Бөмбөг: $\frac{32\pi}{3}$. Хэсэг:
  $\frac{32\pi/3}{64} = \frac{\pi}{6} \approx 0.524$.
- `sg54-t2` — Куб $3\sqrt{3}$ радиустай бөмбөрцөгт багтжээ. Кубын ирмэг ба
  эзлэхүүнийг олоорой.
  **solution:** $a\sqrt3 = 2R = 6\sqrt3$ тул $a = 6$; эзлэхүүн $216$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Хүрэлтийн шалгалт · **title** Талст уу, булан уу?<br>**body** Бүх зүйл бөмбөрцөг юунд хүрч байгаагаас шалтгаална. Кубэд БАГТСАН: 6 талстын төвийг үнсэнэ, хамгийн чанга гаталт, $2R = a$. Кубыг БАГТААСАН: 8 булангаар дайрна, хамгийн өргөн гаталт, $2R = a\sqrt3$. Нэг куб, хоёр бөмбөрцөг, мөн тэдний хоорондох зай нь яг ирмэг ба огторгуйн диагоналийн хоорондох зай юм. |
| 1 | teach | **eyebrow** Огтлол · **title** Хавтгайгаар нь хараарай: багтсан бөмбөг<br>**body** Бөмбөгтэй кубыг голоор нь, талсттай параллель зүсээрэй: $a = 6$ талтай квадрат ба түүнд багтсан тойрог дөрвөн талд нь дунджаар хүрнэ, $2R = 6$, доор жинхэнэ хэмжээгээр зурагдсан. Оронд нь ДИАГОНАЛЬ хавтгайгаар зүсвэл ижил бөмбөг булангуудад хүрэхээ болино: тэр зай нь багтаасан бөмбөрцгийн нэхэж байгаа зай юм. |
| 2 | tapQuestion | **eyebrow** Шалгая · **title** Хайрцган доторх сагсан бөмбөг<br>**prompt** $R = 12$ см радиустай бөмбөг боломжит хамгийн жижиг куб хайрцагт савлагдана. Хайрцгийн ирмэг нь<br>**options** `$24$ см` · `$12$ см` · `$24\sqrt{3}$ см` · `$12\sqrt{3}$ см` — **correctIndex 0**<br>**explanation** Багтсан бөмбөг: ирмэг = диаметр = $24$. $\sqrt3$ хувилбарууд нь НӨГӨӨ байрлалынх (бөмбөг доторх куб), өөрөөр хэлбэл талст биш булан. |
| 3 | workedSet | **eyebrow** Бодсон жишээ · **title** Хоёр чиглэл<br>**intro** Талстад хүрвэл ирмэг. Булангуудад хүрвэл диагональ.<br>**ex1** Кубын ирмэг $6$: хоёр бөмбөрцгийн радиус? · алхам: Дотор: $R = 3$ (талстын төв). · алхам: Гадна: $R = 3\sqrt3$ ($6\sqrt3$ диагоналиар, булангууд). · **хариу** $3$ ба $3\sqrt{3}$<br>**ex2** $r = 3$, $h = 8$ цилиндр бөмбөрцөгт: $R$? · алхам: Тэнхлэг огтлолын диагональ: $\sqrt{6^2 + 8^2} = 10$. · алхам: $R = 5$. · **хариу** $R = 5$ |
| 4 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Яг таарах байрлал<br>**intro** 2R бичихээсээ өмнө юу юунд хүрч байгааг нэрлээрэй.<br>**p1** Ирмэг нь $10$ кубэд багтсан бөмбөрцөг: эзлэхүүн? — **choices** `$\dfrac{500\pi}{3}$` · `$\dfrac{4000\pi}{3}$` · `$500\pi$` — **answerIndex 0** — $R = 5$: $V = \frac43\pi \cdot 125 = \frac{500\pi}{3}$.<br>**p2** $R = \sqrt{3}$ радиустай бөмбөрцөгт багтсан куб: ирмэг? — **choices** `$2$` · `$\sqrt{3}$` · `$2\sqrt{3}$` — **answerIndex 0** — $a\sqrt3 = 2\sqrt3$ тул $a = 2$.<br>**p3** $3$ радиустай бөмбөрцгийг багтаасан хамгийн бага цилиндрийн эзлэхүүн — **choices** `$54\pi$` · `$36\pi$` · `$27\pi$` — **answerIndex 0** — $r = 3$, $h = 6$: $V = \pi \cdot 9 \cdot 6 = 54\pi$. (Мөн доторх бөмбөрцөг: $36\pi = \frac23 \cdot 54\pi$, дахин булшны чулуу.) |
| 5 | funFact | **eyebrow** Сонирхолтой баримт · **title** Хайрцгийн хувьд 52% бол таазны хязгаар<br>**body** Хайрцагтаа яг багтсан бөмбөг зайны 48%-ийг үрдэг (π/6 ≈ 52% дүүргэнэ). Оронд нь жүржийг дэлгүүрийн ухаалаг аргаар өрвөл π/√18 ≈ 74%-д хүрнэ, Кеплер 1611 онд үүнийг юу ч дийлэхгүй гэж таамаглаж, баталгаа нь (Хейлс, 1998–2014) 300 хуудас дээр нэмээд компьютерийн шалгалтын төсөл шаардсан. Огторгуйн геометр жимс өрөх талаар судалгааны түвшний бодлоготой хэвээрээ байна. |
| 6 | recap | **eyebrow** Эргэн дүгнэлт · **title** Багтсан ба багтаасан |

---

## PRACTICE

- `sg5-pr-1` — $17$ радиустай бөмбөрцгийг төвөөс $15$ зайд байрлах хавтгайгаар
  зүслээ. Огтлолын радиус ба талбайг олоорой.
  **solution:** $r = \sqrt{289 - 225} = 8$ (8-15-17); талбай
  $64\pi \approx 201$.
- `sg5-pr-2` — Радиус нь $6$ байх бөмбөрцгийн гадаргуугийн талбай ба
  эзлэхүүнийг олоорой.
  **solution:** $S = 4\pi \cdot 36 = 144\pi$;
  $V = \frac43\pi \cdot 216 = 288\pi$.
- `sg5-pr-3` — Бөмбөрцгийн их тойргийн урт $10\pi$. Бөмбөрцгийн гадаргуугийн
  талбай ба эзлэхүүнийг олоорой.
  **solution:** $2\pi R = 10\pi$ тул $R = 5$. $S = 100\pi$;
  $V = \frac{500\pi}{3} \approx 523.6$.
- `sg5-pr-4` — Битүү хагас бөмбөрцөг бөмбөгөр тагны радиус $9$. Бүтэн
  гадаргуугийн талбай (бөмбөгөр таг + шал) ба эзлэхүүнийг олоорой.
  **solution:** Гадаргуу: $2\pi \cdot 81 + \pi \cdot 81 = 243\pi$. Эзлэхүүн:
  $\frac23\pi \cdot 729 = 486\pi$.
- `sg5-pr-5` — Ирмэг нь $4$ кубэд нэг бөмбөрцөг багтсан, өөр нэг бөмбөрцөг
  түүнийг багтаасан байна. Хоёр радиус ба хоёр эзлэхүүнийг олоорой.
  **solution:** Дотор: $R = 2$, $V = \frac{32\pi}{3}$. Гадна: $R = 2\sqrt{3}$,
  $V = \frac43\pi(2\sqrt3)^3 = 32\sqrt{3}\pi \approx 174$.
- `sg5-pr-6` — Радиус $5$, өндөр $24$ цилиндр бөмбөрцөгт багтжээ. Бөмбөрцгийн
  радиус ба эзлэхүүнийг олоорой.
  **solution:** Тэнхлэг огтлолын диагональ: $\sqrt{10^2 + 24^2} = 26$ тул
  $R = 13$. $V = \frac43\pi \cdot 2197 = \frac{8788\pi}{3} \approx 9202$.
- `sg5-pr-7` — $R = 6$ радиустай бөмбөгийг $d$ зайд зүсэхэд огтлолын талбай
  $27\pi$ болов. $d$-г олоорой.
  **solution:** $\pi r^2 = 27\pi$ тул $r = 3\sqrt{3}$.
  $d = \sqrt{36 - 27} = 3$. (30-60-90 нуугдаж байна: яг $d = R/2$.)
- `sg5-pr-8` — Зайрмагны дэлгүүр бөмбөрцөг халбаганыхаа радиусыг $3$ см-ээс
  $6$ см болгож хоёр дахин нэмэгдүүлээд үнийг гурав дахин нэмэгдүүлэв. См³
  тутамд илүү ашигтай юу, ашиггүй юу?
  **solution:** Эзлэхүүн $36\pi \to 288\pi$ болно: 3 дахин үнээр 8 дахин их
  зайрмаг, өөрөөр хэлбэл см³ тутамд хамаагүй ашигтай (эзлэхүүн тутмын үнэ
  өмнөхийнхөө $\frac38$ болж буурна).

---

## TEST YOURSELF

- `sg5-ty-1` — Бөмбөрцгийн радиус $4$: гадаргуугийн талбай ба эзлэхүүн?
  **solution:** $S = 64\pi$; $V = \frac{256\pi}{3} \approx 268.1$.
- `sg5-ty-2` — Хавтгай $25$ радиустай бөмбөрцгийг $7$ зайд зүслээ. Огтлолын
  радиус?
  **solution:** $r = \sqrt{625 - 49} = 24$ (7-24-25 гурвал).
- `sg5-ty-3` — Бөмбөрцгийн гадаргуу $144\pi$. Эзлэхүүнийг нь олоорой.
  **solution:** $R = 6$; $V = 288\pi$.
- `sg5-ty-4` — Бөмбөг өөрийг нь багтаах хамгийн бага цилиндр лаазны хэдэн
  хувийг дүүргэх вэ? Мөн хамгийн бага куб хайрцгийн?
  **solution:** Лааз: яг $\frac{2}{3}$. Хайрцаг:
  $\frac{\pi}{6} \approx 52.4\%$. Лааз хоёр дахин бага зай үрдэг, цилиндр
  илүү сайн тэвэрдэг.
- `sg5-ty-5` — Куб $6$ радиустай бөмбөрцөгт багтжээ. Кубын ирмэг ба
  эзлэхүүнийг олоорой.
  **solution:** $a = \frac{2R}{\sqrt3} = \frac{12}{\sqrt3} = 4\sqrt{3}$;
  $V = (4\sqrt3)^3 = 192\sqrt{3} \approx 332.6$.
- `sg5-ty-6` — Хагас бөмбөрцөг ба конус $R = 3$ радиусыг хуваалцаж байгаа
  бөгөөд конусын өндөр нь $3$. Аль нь илүү их багтаах вэ?
  **solution:** Хагас бөмбөрцөг: $\frac23\pi \cdot 27 = 18\pi$. Конус:
  $\frac13\pi \cdot 9 \cdot 3 = 9\pi$. Хагас бөмбөрцөг конусаас яг ХОЁР дахин
  их багтаана, Кавальерийн аяганы аргументын урьдчилсан харуулалт.

---

## Notes for Khas

### 1. The ЭШ bank does not test spheres. Not once.

**The finding that frames this draft, and the sharpest "does the exam agree
with the ministry" data point yet.**

А/492's **10.12б is core (non-elective)** and names the sphere explicitly:

> «Пирамид, цилиндр, призм, **бөмбөрцөг**, конусын гадаргуун талбай,
> эзлэхүүнийг олох томьёог мэдэх, хэрэглэх»

The exam bank contains **zero** occurrences of «бөмбөрцөг», «бөмбөрцг…»,
«сфер» or «бөөрөнхий». The 98 hits for «бөмбөг» are all probability urns and
basketballs («цагаан бөмбөгтэй», «уутнаас бөмбөгнүүдийг», «Сагсан бөмбөгийн»).
There is no sphere surface-area or sphere-volume question anywhere.

The 74 `solid_geometry` questions break down like this:

| subtopic | count |
|---|---|
| Гурвалжин пирамид | 16 |
| Тэгш өнцөгт параллелепипед | 12 |
| **Огтлогдсон конус** | **12** |
| Параллелепипед, пирамидын эзлэхүүн | 12 |
| Конус | 6 |
| the rest (cylinder, solid of revolution, prism ratios…) | 16 |
| **бөмбөрцөг** | **0** |

**So the exam tests truncated cones twelve times and spheres never**, while the
ministry lists the sphere in the same breath as the cone and the cylinder.

**Why this matters beyond one topic.** Review pile 4j asks whether the exam
outranks А/492 for ЭШ topics, and every instance so far has been *the exam has
a better word*. This is the first where **the ministry requires content the
exam does not test**, which is the opposite direction and does not have the
same answer. I do not think it argues for cutting unit 12: 10.12б is core, the
bank is 54 papers rather than the whole history, and a student who cannot do a
sphere has a gap the syllabus says is real. But it is worth your eye next to
6i, which found the reverse in ЭШ Algebra.

**It also means «бөмбөрцөг» has exactly one authority** — the ministry line
above — and no exam register to check it against. Every other term in this
draft had two or three sources.

### 2. «бөмбөг» is unavailable, so *sphere* and *ball* collapse into one word

The English carefully distinguishes the **sphere** (the surface, $|PO| = R$)
from the **ball** (the solid, $|PO| \le R$), and lesson 1 makes the distinction
explicitly in a parenthesis.

Mongolian cannot follow it here. «бөмбөг» — the natural word for the solid — is
**taken by probability**, 98 uses in the exam bank, and the ЭШ probability
strand is a topic this same course teaches. That is 4e's in-strand rule: the
word is unavailable.

So the draft uses **«бөмбөрцөг» for both**, which is what А/492 does (10.12б
speaks of the бөмбөрцөг's *volume*, so its бөмбөрцөг is the solid), and renders
*the sphere's surface* as **«бөмбөрцгийн гадаргуу»** where the distinction
actually matters. Lesson 1's parenthesis becomes a note that the solid version
carries the same name rather than a new term.

**What is lost:** one sentence of English precision. **What is gained:** no
collision with a strand the same student studies. If you want the distinction
kept, the candidate is «бөмбөлөг» for the solid, which shipped mirrors use 5
times — **for bubbles**, so it would be a fresh coinage in a new sense.

### 3. «их тойрог» for *great circle* is ungrounded — and I nearly recorded it as grounded

Worth flagging as a method note. My first search returned «их тойрог» **exam
4**, which I was about to record as grounding. Checking the contexts showed all
four are false positives: the substring sits inside «ор**ших тойрог**» («тэгш
өнцөгт дотор ор**ших тойрог**»). The real count is **zero**.

«их тойрог» is the standard calque (большой круг) and «том тойрог» appears 4
times in my own earlier drafts, so the strand is not consistent with itself
either. I used «их тойрог» as the more standard of the two and because «том»
reads as informal size rather than a technical maximum. One term, cheap to
reverse, but it is a coinage and this section is where coinages go.

**The method note:** this is the second substring false positive in two days
(«ул» inside «улам» last week, «их тойрог» inside «орших тойрог» today). A bare
`len(re.findall(term, corpus))` is not evidence for a short Mongolian term —
the contexts have to be read. I have been doing that for decisive terms and not
always for confirmatory ones.

### 4. Inscribed and circumscribed are a verb pair in the exam, not two nouns

Pleasingly clean grounding, and it resolves a construction I had expected to
have to invent:

| exam | means |
|---|---|
| «гурвалжин**д багтсан** тойрог» | the circle inscribed **in** the triangle |
| «тойрог**т багтсан** тэгш өнцөгт» | the rectangle inscribed in the circle |
| «тойрог**ийг багтаасан** трапец» | the trapezoid circumscribed **about** the circle |
| «гурвалжны**г багтаасан** тойрог» | the circumcircle of the triangle |

So the pattern is **A-д багтсан B** (B inscribed in A) and **A-г багтаасан B**
(B circumscribed about A) — 47 and 9 uses respectively, and consistent with
`GEOMETRY-TERMS.md`'s «багтаасан тойрог» from the dictionary.

Lesson 4 uses exactly that: «кубэд багтсан бөмбөрцөг», «кубыг багтаасан
бөмбөрцөг». **No coinage needed for the lesson's central pair**, which is
unusual for this strand.

### 5. A correction to yesterday's draft: *truncated cone* is «огтлогдсон конус»

**`solid-geometry/cylinders-and-cones`, committed about an hour ago, is
wrong**, and I found it while searching this topic's solid-geometry subtopics.

That draft's Notes 5 recorded «таслагдсан конус» as ungrounded, saying I had
searched «таслагдсан», «таславсан» and «тайрсан» and found nothing anywhere.
All true — and I did not search **«огтлогдсон»**, which is the word:

> `"subtopic": "Огтлогдсон конус"` — **12 questions**, all from the **2025A/B/C
> papers**, all Section 2 fill-ins (Q2.4.2, Q2.4.3), all tier **hard**.

So the exam has a subtopic label for it, on the current papers, and it is one
of the three most-tested solids in the bank.

**This is 6l's failure mode repeating in a draft I wrote after documenting 6l**
— but the cause is different and worth separating. 6l was *the exam bank was
not consulted*. This was *the exam bank was consulted with three wrong search
terms*. The fix for the first is a habit; the fix for the second is to search
the **subtopic labels**, which are a small controlled vocabulary listing
exactly what the exam thinks its own topics are, and which I had never used as
a term source until today.

**I have corrected that draft** — the term was flagged in its own Notes as
ungrounded and "cheap to reverse", and the exam settles it unambiguously — and
recorded it in the review pile so the change is visible rather than silent.

### 6. Decimals

**Sixteen**, all left as decimal **points** inside `$...$` per 2d, which is not
applied. Gate: clean.

**I wrote "fourteen" here, claimed I had counted rather than estimated, and had
not.** Running 2d's command gives 16. That is the third wrong decimal count in
three drafts, and the first where I asserted the method as well as the number —
which makes it worse than the other two, not better. The number below is the
command's output, pasted.

Same structural cause as `cylinders-and-cones` (26): π-exact answer plus
decimal gloss in every worked example. The two solid-geometry drafts together
contribute **42**, behind only `10/exponential-functions` (144) and
`9/equations-and-formulas` (44) among individual drafts.

**2d stands at 440 shipping across 37 drafts.**

---

**ЭШ status:** **Геометр ба хэмжигдэхүүн is complete — twelve of twelve.**
That makes **six of fourteen** ЭШ topics fully drafted: Sets, Algebra,
Exponentials & Logarithms, Functions (partial per its own note), Geometry, and
the Algebra block's five. The next target is queue item 5.
