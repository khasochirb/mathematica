# Draft — `solid-geometry/cylinders-and-cones`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**ЭШ Geometry unit 11 of 12.** One unit left (`spheres`) and then
*Геометр ба хэмжигдэхүүн* closes as the sixth ЭШ topic.

**Four lessons, 30 items, 33 interactive steps, 12 nested tryItSet problems.**
(8 workedExamples + 8 tryIt + 8 practice + 6 testYourself; the other 17 `id`
fields are figure `points`.)

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. Written to `docs/mn-voice-reference.md` from the first
line: no em-dash parentheticals (§9), decimal comma in prose (§7), hyphenated
case suffixes (§8), condition before thing (§1).

**Base vocabulary is `GEOMETRY-TERMS.md`.** This table lists what this topic
adds — **and four corrections to `geometry/surface-area-and-volume`**, which is
ЭШ Geometry unit 9 and teaches the same solids. See Notes 1–4.

> **Amended the same day.** Notes 5 originally recorded «таслагдсан конус» as a
> coinage. The exam has the word — «Огтлогдсон конус», a 12-question subtopic
> label on the 2025 papers — and the draft now uses it. See Notes 5 and review
> pile 6m.

**Shipped-mirror check:** no slug overlap, but `6-mn/geometry-area-volume` and
`7-mn/geometry-scale-and-circles` both ship volume and surface-area Mongolian,
and **they disagree with each other about how to spell *volume***. That is
Notes 1, and it is the largest finding in this draft.

> **This is the best-grounded topic in the geometry strand.** The ЭШ bank
> contains almost this exact material: «цилиндрийн **тэнхлэг огтлол** нь
> квадрат бол», «Конусын **байгуулагч** нь 12 нэгж», «конусын **хажуу
> гадаргуугийн дэлгээс** болох **секторын** өнцгийг олоорой». Four of this
> topic's key terms come from the exam verbatim, in sentences that are
> essentially its worked examples.

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| cylinder | **цилиндр** | ministry 1 · exam 8 |
| cone | **конус** | ministry 1 · **exam 48** |
| volume | **эзлэхүүн** | **exam 78 : 3** · ministry 10.12б · shipped 40 — **correction, Notes 1** |
| lateral surface area | **хажуу гадаргуугийн талбай** | **exam 9, verbatim** — **correction, Notes 2** |
| total surface area | **бүтэн гадаргуугийн талбай** | **exam 4, verbatim** — Notes 2 |
| slant height (of a cone) | **байгуулагч** | **exam 8, verbatim** — **correction, Notes 3** |
| axial section | **тэнхлэг огтлол** | **ministry 10.12в + exam 4, both verbatim** |
| net, unrolled development | **дэлгээс** | **exam 3, verbatim** · shipped 11 |
| sector | **сектор** | ministry 2 · exam 11 |
| axis | **тэнхлэг** | ministry 6 · exam 102 |
| apex | **орой** | ministry 1 · exam |
| truncated cone | **огтлогдсон конус** | **exam 12, verbatim subtopic label** — corrected, Notes 5 |
| oblique cylinder | **налуу цилиндр** | qualified per 4e — Notes 4 |
| capacity | **багтаамж** | shipped 3 |

---

## Topic-level strings

**TITLE:** Цилиндр ба конус

**BLURB:** Дэлгэж болдог бөөрөнхий биетүүд: цилиндрийн нууц тэгш өнцөгт,
конусын нууц бялууны зүсэм, зайрмагны конус бүрт нуугдаж байдаг 3-4-5
гурвалжин, мөн таны кофены аяга болох огтлогдсон конус.

**buildsOn:** Дугуйн талбай ба тойргийн урт; 2-р нэгжийн призм (цилиндр бол дугуй суурьтай призм), 3-р нэгжийн пирамид (конус бол дугуй суурьтай пирамид).

---

## Lesson 1 — Цилиндр (`the-cylinder`)

**concreteComparison**

Лаазны шошгыг бүтнээр нь хуулж аваад тэгшлэвэл: төгс тэгш өнцөгт. Түүний өндөр
нь лаазны өндөр; өргөн нь лаазыг ТОЙРСОН зай буюу тойргийн урт. Цилиндр бүр
бол ороосон тэгш өнцөгт дээр нэмээд хоёр дугуй тагтай нь юм.

**objective**

Цилиндрийн бүтцийг (тэнхлэг, радиус, өндөр, тэнхлэг огтлол) мэдэж, дэлгэсэн
шошгоноос гадаргуугийн талбайг тооцоолох.

**concept**

1. **Цилиндр** бол шууд дээш гулсуулсан тойрог: $r$ радиустай, параллель хоёр
   дугуй суурь, тэднийг холбосон $h$ өндөртэй муруй хажуу хана. Энэ бол суурь
   нь тойрог болсон призмийн санаа, мөн **тэнхлэг** нь хоёр төвийг холбоно;
   шулуун цилиндрийн хувьд тэнхлэг суурьтаа перпендикуляр.

2. Ханыг дэлгээрэй: $2\pi r$ өргөнтэй (тэгшилсэн тойргийн урт), $h$ өндөртэй
   тэгш өнцөгт. Тэгэхээр $S_{\text{хаж}} = 2\pi r h$ буюу шошгоны талбай. Бүтэн
   гадаргуу дээр нь хоёр таг нэмнэ:
   $S = 2\pi r h + 2\pi r^2 = 2\pi r(h + r)$.

3. Цилиндрийг тэнхлэгээр нь зүсвэл огтлол (**тэнхлэг огтлол**) нь $2r$
   өргөнтэй, $h$ өндөртэй тэгш өнцөгт. Тэнхлэгт перпендикуляр зүсвэл: үргэлж
   ижил тойрог. Энэ хоёр харагдац цилиндрийн бүх хэмжээсийг агуулна.

**keyIdea**

Цилиндр = ороосон тэгш өнцөгт + 2 таг: S_хаж = 2πrh, S = 2πr(h + r). Тэнхлэг
огтлол нь 2r × h тэгш өнцөгт.

**facts**

| title | latex | explanation |
|---|---|---|
| Хажуу гадаргуу | `S_{\text{хаж}} = 2\pi r h` | Шошго: тойргийн урт × өндөр. |
| Бүтэн гадаргуу | `S = 2\pi r(h + r)` | Шошго дээр хоёр дугуй таг. |
| Тэнхлэг огтлол | `2r \times h \text{ тэгш өнцөгт}` | Тэнхлэгээр нь хийсэн зүсэлт. |

**workedExamples**

- `sg41-we1` — **statement:** Цилиндрийн радиус $3$, өндөр $5$. Хажуу ба бүтэн
  гадаргуугийн талбайг яг тааруулж олоорой.
  **solution:** $S_{\text{хаж}} = 2\pi \cdot 3 \cdot 5 = 30\pi$. Бүтэн:
  $30\pi + 2\pi \cdot 9 = 48\pi \approx 150.8$.
- `sg41-we2` — **statement:** Цилиндрийн тэнхлэг огтлол нь талбай нь $36$
  байх КВАДРАТ. Цилиндрийн бүтэн гадаргуугийн талбайг олоорой.
  **solution:** Квадратын тал $6$: тэгэхээр $2r = 6$ ($r = 3$) ба $h = 6$.
  $S = 2\pi r(h + r) = 2\pi \cdot 3 \cdot 9 = 54\pi$. (Тэнхлэг огтлол нь
  квадрат байх цилиндрийг тэгш талт гэдэг, өргөнөөрөө яг өндөртэй.)

**commonMistakes**

- **text:** Дэлгэсэн шошгоны өргөнд $2\pi r$ (тойргийн урт)-ийн оронд $\pi r^2$
  (талбай) хэрэглэх.
  **correction:** Шошго ИРМЭГИЙГ тойрч ороодог тул түүний өргөн нь ирмэгийн
  урт $2\pi r$. Талбайн томьёо «тойрогт хэр их багтах вэ» гэдэгт хариулдаг;
  шошго «хэр хол тойрох вэ» гэдгийг асууж байна.
- **text:** Хоёрын оронд нэг таг нэмэх (эсвэл хоолойд хоёрыг нэмэх).
  **correction:** Саваа уншаарай: битүү лааз = 2 таг, аяга = 1, хоолой = 0.
  $2\pi r(h+r)$ томьёо бол БИТҮҮ хувилбар, ухамсартайгаар тохируулаарай.

**tryIt**

- `sg41-t1` — Радиус $4$, өндөр $6$: хажуу ба бүтэн гадаргуу?
  **solution:** $S_{\text{хаж}} = 2\pi \cdot 4 \cdot 6 = 48\pi$; бүтэн
  $= 48\pi + 32\pi = 80\pi \approx 251.3$.
- `sg41-t2` — Лаазны шошго (зөвхөн хажуу гадаргуу) $20\pi$ талбайтай бөгөөд
  лаазны өндөр $5$. Радиус ба тэнхлэг огтлолын талбайг олоорой.
  **solution:** $2\pi r \cdot 5 = 20\pi$ тул $r = 2$. Тэнхлэг огтлол:
  $2r \times h = 4 \times 5 = 20$, π байхгүй; энэ бол хавтгай тэгш өнцөгт.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Бүтэц · **title** Шууд дээш гулсуулсан тойрог<br>**body** Радиус $r$, өндөр $h$, хоёр төвийг холбосон тэнхлэг. Цилиндр призмийн бүлгээс бүгдийг өвлөнө: ижил гулсуулах байгууламж, «зүсэлт бүр нь суурь» гэсэн ижил чанар, зөвхөн олон өнцөгтийн оронд тойрогтой. Бөөрөнхий боловч хачирхалтай биш. |
| 1 | solid3d | **eyebrow** Тоглож үз · **title** Лаазыг татаж сунгаарай<br>**teach** $r$ ба $h$-г алхмаар өөрчлөөд гадаргуу ба эзлэхүүн π-гийн яг үржвэр болж хэрхэн хариулахыг ажиглаарай. Өсөх хоёр арга бий: өндөр нэмбэл шошго нэмэгдэнэ ($2\pi r h$ гишүүн); өргөн нэмбэл шошго БА таг хоёул нэмэгдэнэ ($r$ гишүүн бүрд байна), өөрөөр хэлбэл өргөн нь илүү үнэтэй.<br>**config** unchanged (`solid: cylinder`, `r: 3`, `h: 5`) |
| 2 | solidNet | **eyebrow** Дэлгээрэй · **title** Шошго бол тэгш өнцөгт<br>**teach** Дэлгэе: нэг тэгш өнцөгт ($2\pi r$ өргөн, $h$ өндөр) дээр нэмээд хоёр дугуй таг. Тэгш өнцөгтийн өргөн нь ТОЙРГИЙН УРТ байх нь, диаметр ч биш, талбай ч биш, цилиндрийн гадаргуугийн талбайн бүх нууц юм.<br>**config** unchanged (`solid: cylinder`, `r: 3`, `h: 5`) |
| 3 | tapQuestion | **eyebrow** Шалгая · **title** Шошгоны тоо<br>**prompt** Радиус $3$, өндөр $5$: дэлгэсэн шошго нь ямар хэмжээтэй тэгш өнцөгт вэ?<br>**options** `$6\pi \times 5$` · `$9\pi \times 5$` · `$3 \times 5$` · `$6 \times 5$` — **correctIndex 0**<br>**explanation** Өргөн = тойргийн урт $= 2\pi r = 6\pi \approx 18.8$; өндөр $5$. Талбай $30\pi$ ✓. $9\pi$ бол суурийн ТАЛБАЙ, огт өөр асуулт. |
| 4 | teach | **eyebrow** Хоёр харагдац · **title** Тэнхлэг огтлол: цилиндрийн үнэмлэх<br>**body** Тэнхлэгээр нь шулуун доош зүсээрэй: $2r$ өргөнтэй, $h$ өндөртэй тэгш өнцөгт ($r = 3$, $h = 5$-ийн хувьд доор жинхэнэ хэмжээгээр зурагдсан). Сонгодог цилиндрийн бодлого бүр энэ тэгш өнцөгтөд амьдардаг: түүний диагональ $\sqrt{(2r)^2 + h^2} = \sqrt{61}$ нь цилиндр доторх хамгийн урт хэрчим бөгөөд «тэнхлэг огтлол нь квадрат» гэдэг нь шууд $h = 2r$ болж хөрвөнө. |
| 5 | workedSet | **eyebrow** Бодсон жишээ · **title** Лааз ба квадрат<br>**intro** Бүгд $r$ ба $h$-гээс, эсвэл тэнхлэг огтлолын тэгш өнцөгтөөс уншигдана.<br>**ex1** $r = 3$, $h = 5$: бүтэн гадаргуу? · алхам: Шошго: $2\pi \cdot 3 \cdot 5 = 30\pi$. · алхам: Таг: $2 \cdot 9\pi$; бүтэн $48\pi$. · **хариу** $48\pi \approx 150.8$<br>**ex2** Тэнхлэг огтлол нь талтай нь $6$ байх квадрат: бүтэн гадаргуу? · алхам: $2r = 6, h = 6$: $r = 3$. · алхам: $S = 2\pi \cdot 3 \cdot 9 = 54\pi$. · **хариу** $54\pi \approx 169.6$ |
| 6 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Ороож, дэлгэ<br>**intro** Шошгоны өргөн = 2πr. Тагаа тоолоорой.<br>**p1** $r = 2$, $h = 7$: хажуу гадаргуу? — **choices** `$28\pi$` · `$14\pi$` · `$36\pi$` — **answerIndex 0** — $2\pi \cdot 2 \cdot 7 = 28\pi$.<br>**p2** ТАГГҮЙ цилиндр аяга, $r = 3$, $h = 4$: хэр их материал хэрэгтэй вэ? — **choices** `$33\pi$` · `$42\pi$` · `$24\pi$` — **answerIndex 0** — Хана $24\pi$ + ёроол $9\pi$ = $33\pi$. Ганцхан таг, дутуугаар нь та уудаг.<br>**p3** $r = 3$, $h = 8$ цилиндр доторх хамгийн урт саваа хэр урт вэ? — **choices** `$10$` · `$8$` · `$\sqrt{73}$` — **answerIndex 0** — Тэнхлэг огтлолын диагональ: $\sqrt{6^2 + 8^2} = 10$, лааз дотор хэвтэж байгаа 6-8-10 гурвал. |
| 7 | recap | **eyebrow** Эргэн дүгнэлт · **title** Цилиндр |

---

## Lesson 2 — Цилиндрийн эзлэхүүн (`volume-of-cylinders`)

**concreteComparison**

100 ижил зоосны багц бол цилиндр бөгөөд түүний эзлэхүүн ойлгомжтой: нэг зоосны
талбайг багцын өндрөөр үржүүлнэ. Багцыг түлхэж хазайлгаарай, ижил зоос, ижил
эзлэхүүн. Кавальери үүнийг бидэнд аль хэдийн заасан; тойрог зүгээр л бүлэгт
нэгдэж байгаа юм.

**objective**

V = πr²h-ээр цилиндрийн эзлэхүүнийг, түүний дотор хазайсан (налуу) цилиндрийн
эзлэхүүнийг тооцоолж, багтаамжийн бодлого бодох.

**concept**

1. Цилиндрийн эзлэхүүн = зүсэлтийн талбай × өндөр: $V = \pi r^2 h$. Энэ бол
   суурь нь тойрог болсон призмийн $V = Bh$ томьёо, зоосны багц бүгдийг
   хэлж байна.

2. Кавальери дахин: налуу цилиндр (хазайсан багц) ижил ЖИНХЭНЭ өндөртэй
   шулуун цилиндртэй яг тэнцүү хэмжээ багтаана. Мөн хэмжээсийг хоёр дахин
   нэмэгдүүлэх нь тэгш хэмтэй биш: $h$-г хоёр дахин нэмэгдүүлбэл $V$ хоёр
   дахин; $r$-г хоёр дахин нэмэгдүүлбэл ДӨРӨВ ДАХИН ($r$ квадратад байна).
   Өргөн нь өндрийг дийлнэ.

3. Бодит нэгж дэх багтаамж: $1$ литр $= 1000$ см³. $r = 3$ см, $h = 10$ см
   лааз $90\pi \approx 283$ см³ буюу ойролцоогоор $0,28$ литр багтаана. Үгэн
   бодлогыг асуултын шаардсан нэгжээр нь дуусгаарай.

**keyIdea**

V = πr²h (зүсэлт × өндөр). r-г хоёр дахин нэмэгдүүлбэл V дөрөв дахин; h-г
хоёр дахин нэмэгдүүлбэл зөвхөн хоёр дахин. Налуу цилиндр: ижил томьёо,
ЖИНХЭНЭ өндөр.

**facts**

| title | latex | explanation |
|---|---|---|
| Эзлэхүүн | `V = \pi r^2 h` | Тойрог зүсэлт × багцын өндөр. |
| Масштаблалт | `r \to 2r \Rightarrow V \to 4V` | Радиус квадратад байна; өндөр биш. |
| Багтаамж | `1 \text{ л} = 1000 \text{ см}^3` | Эзлэхүүний хариу ихэвчлэн бодит нэгж хүсдэг. |

**workedExamples**

- `sg42-we1` — **statement:** Радиус $3$, өндөр $10$: эзлэхүүнийг яг таг, мөн
  аравтын нэг орны нарийвчлалтай олоорой.
  **solution:** $V = \pi \cdot 9 \cdot 10 = 90\pi \approx 282.7$.
- `sg42-we2` — **statement:** Хоёр лааз: A нь $r = 4, h = 5$; B нь
  $r = 5, h = 4$ (хэмжээсийг нь сольсон). Аль нь илүү их багтаах вэ, хэдээр вэ?
  **solution:** A: $\pi \cdot 16 \cdot 5 = 80\pi$.
  B: $\pi \cdot 25 \cdot 4 = 100\pi$.
  B нь $20\pi \approx 62.8$-аар хожиж байна, учир нь радиус квадрат
  агуулдаг тул том тоог $r$-д өгөх нь илүү ашигтай. Өргөн нь өндрийг дийлнэ.

**commonMistakes**

- **text:** Диаметрийг $r$ гэж хэрэглэх.
  **correction:** Бодлогууд диаметр зарлах дуртай. $V = \pi r^2 h$ нь радиус
  хүснэ, эхлээд хоёр хуваагаарай. Радиусын оронд диаметр тавих нь эзлэхүүнийг
  4 дахин хөөрөгдөх бөгөөд энэ бол том алдалт.
- **text:** Дурын хэмжээсийг хоёр дахин нэмэгдүүлбэл эзлэхүүн хоёр дахин
  нэмэгдэнэ гэж бодох.
  **correction:** Зөвхөн $h$ шугаман масштаблана. $r$ квадратаараа ордог:
  радиусыг хоёр дахин = эзлэхүүн дөрөв дахин. Аяганы өргөний «бага зэргийн»
  өсөлт хамаагүй их кофе багтаадгийн учир нь энэ.

**tryIt**

- `sg42-t1` — Диаметр $8$, өндөр $7$: эзлэхүүн?
  **solution:** $r = 4$: $V = \pi \cdot 16 \cdot 7 = 112\pi \approx 351.9$.
- `sg42-t2` — $2$ м радиустай цилиндр сав $36\pi$ м³ багтаах ёстой. Хэр өндөр
  байх вэ? Хэрэв радиусыг хоёр дахин нэмэгдүүлбэл ямар өндөр хангалттай вэ?
  **solution:** $h = \frac{36\pi}{\pi \cdot 4} = 9$ м. Хоёр дахин нэмэгдсэн
  радиус ($r = 4$): $h = \frac{36\pi}{16\pi} = \frac{9}{4} = 2.25$ м, өөрөөр
  хэлбэл өндрийн дөрөвний нэг, учир нь суурь дөрөв дахин болсон.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Зоосны багц · **title** V = πr²h, багцлах замаар<br>**body** Нэг зоос: талбай $\pi r^2$. $h$ өндөртэй багц: эзлэхүүн $\pi r^2 h$. Гарган авалт нь бүхэлдээ энэ, цилиндр бол призмийн гэр бүлийн хамгийн бөөрөнхий гишүүн бөгөөд гэр бүлийн $V = Bh$ дүрмийг дагадаг. |
| 1 | solid3d | **eyebrow** Тоглож үз · **title** Өргөн нь өндрийг дийлнэ<br>**teach** Алхамчаар ийм туршилт хийгээрэй: $r=3, h=5$-аас эхлээд эхлээд өндөрт 1 нэмээрэй, дараа нь оронд нь радиуст 1 нэмээрэй. Эзлэхүүний үсрэлтийг харьцуулаарай, радиусын алхам том зөрүүгээр хожино, учир нь $\pi r^2 h$-д $r$ квадратад байна.<br>**config** unchanged (`solid: cylinder`, `r: 3`, `h: 5`) |
| 2 | tapQuestion | **eyebrow** Шалгая · **title** Баристагийн нууц<br>**prompt** Аяганы радиус $3$-аас $6$ болж өсөв (өндөр тогтмол). Эзлэхүүн нь:<br>**options** `дөрөв дахин нэмэгдэнэ` · `хоёр дахин нэмэгдэнэ` · `8 дахин нэмэгдэнэ` · `π-гээр нэмэгдэнэ` — **correctIndex 0**<br>**explanation** $V \propto r^2$: $(6/3)^2 = 4$. Радиусыг хоёр дахин, кофег дөрөв дахин, харин ӨНДРИЙГ хоёр дахин нэмэгдүүлбэл ердөө хоёр дахин болно. |
| 3 | teach | **eyebrow** Хазайсан цамхаг · **title** Налуу цилиндр: Кавальерийн давтан тоглолт<br>**body** Зоосны багцыг хажуу тийш түлхээрэй: налуу цилиндр. Зоос бүр талбайгаа хадгална; овоолго (босоо) өндрөө хадгална; эзлэхүүн хөндөгдөхгүй: $V = \pi r^2 h$, энд $h$ нь ЖИНХЭНЭ өндөр. Хэрэв бодлогод хазайсан талын урт $\ell$ ба суурьтай үүсгэх $\theta$ өнцгийг өгвөл эхлээд $h = \ell \sin\theta$-г гаргаж аваарай, налуу призмтэй ижил алхам. |
| 4 | workedSet | **eyebrow** Бодсон жишээ · **title** Сав ба солилцоо<br>**intro** πr²h, мөн $r$-г заль мэх диаметрийн эсрэг давхар шалгаарай.<br>**ex1** $r = 3$, $h = 10$: эзлэхүүн? · алхам: $B = 9\pi$. · алхам: $V = 90\pi \approx 283$. · **хариу** $90\pi$<br>**ex2** Налуу цилиндр: $r = 2$, хажуу тал $\ell = 10$, суурьтай $30°$. Эзлэхүүн? · алхам: Жинхэнэ өндөр: $h = 10\sin 30° = 5$. · алхам: $V = \pi \cdot 4 \cdot 5 = 20\pi$. · **хариу** $20\pi \approx 62.8$ |
| 5 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Лаазыг дүүргэ<br>**intro** Эхлээд радиус (диаметрээс болгоомжил), дараа нь πr²h.<br>**p1** $r = 5$, $h = 12$: эзлэхүүн? — **choices** `$300\pi$` · `$120\pi$` · `$60\pi$` — **answerIndex 0** — $\pi \cdot 25 \cdot 12 = 300\pi \approx 942$.<br>**p2** Эзлэхүүн $54\pi$, өндөр $6$: радиус? — **choices** `$3$` · `$9$` · `$\sqrt{6}$` — **answerIndex 0** — $r^2 = \frac{54\pi}{6\pi} = 9$ тул $r = 3$.<br>**p3** Цилиндрийн тэнхлэг огтлол нь талтай нь $4$ байх квадрат. Эзлэхүүн? — **choices** `$16\pi$` · `$32\pi$` · `$64\pi$` — **answerIndex 0** — $2r = 4$ тул $r = 2$; $h = 4$: $V = \pi \cdot 4 \cdot 4 = 16\pi$. |
| 6 | funFact | **eyebrow** Сонирхолтой баримт · **title** Лааз яагаад ийм хэлбэртэй вэ<br>**body** Тогтмол эзлэхүүний хувьд хамгийн бага төмөр зарцуулдаг цилиндр нь $h = 2r$ байх нь, өөрөөр хэлбэл яг тэнхлэг огтлол нь квадрат байх «тэгш талт» цилиндр. Бодит ундааны лааз арай өндөр байдаг (маркетинг өндөр дуртай), харин хүнсний лааз математик оновчтой цэгтээ ойрхон сууна. Энэ хамгийн багыг анализын хичээл дээр баталдаг; та аль хэдийн нэг нэр дэвшигч хөршүүдээ дийлж байгааг цэвэр $2\pi r(h+r)$ арифметикээр шалгаж чадна. |
| 7 | recap | **eyebrow** Эргэн дүгнэлт · **title** Цилиндрийн эзлэхүүн |

---

## Lesson 3 — Конус (`the-cone`)

**concreteComparison**

Цаасан дугуй тайраад бялууны зүсэм хасаж, тайрсан ирмэгүүдийг нааж
наалдуулаарай: хавтгай дугуй нь баярын малгай болж үсэрнэ. Конус бүр бол ямар
нэгэн илүү том тойргийн бялууны зүсэм бөгөөд тэр том тойргийн радиус нь
конусын байгуулагч. Юүлүүр, малгай, чийдэнгийн бүрхүүлийг үнэндээ яг ингэж
ХИЙДЭГ.

**objective**

Конусын бүтэц (r, h, байгуулагч ℓ, ℓ² = r² + h²), гадаргуугийн талбай
S = πr² + πrℓ, мөн дэлгэсэн секторын зургийг эзэмших.

**concept**

1. **Конус**: $r$ радиустай дугуй суурь, түүний төвөөс дээш $h$ өндөрт орой.
   **Байгуулагч** $\ell$ нь оройноос ирмэг хүртэл явах бөгөөд тэнхлэг огтлолын
   тэгш өнцөгт гурвалжин тэднийг холбоно: $\ell^2 = r^2 + h^2$. $r=3, h=4$
   конус бүрийн дотор 3-4-5 гурвалжин зогсож байна.

2. Хажуу гадаргууг дэлгээрэй: $\ell$ радиустай **сектор** (байгуулагч нь
   секторын радиус болж байна!), нумын урт нь $2\pi r$ (ирмэг). Түүний талбай
   $\pi r \ell$ тул бүтэн гадаргуу
   $S = \pi r^2 + \pi r \ell = \pi r(r + \ell)$.

3. Секторын төв өнцөг: $\varphi = \frac{r}{\ell} \cdot 360°$, өөрөөр хэлбэл
   бүтэн тойргоос амьд үлдэх хувь нь $\frac{r}{\ell}$. $r = 3, \ell = 5$ конус
   $216°$ сектор болж дэлгэгдэнэ; дутуу байгаа $144°$ нь таны тайрч авсан
   бялууны зүсэм.

**keyIdea**

Тэнхлэг огтлолын гурвалжин: ℓ² = r² + h². Дэлгэвэл: ℓ радиустай, 2πr нумтай,
πrℓ талбайтай, (r/ℓ)·360° өнцөгтэй сектор.

**facts**

| title | latex | explanation |
|---|---|---|
| Байгуулагч | `\ell^2 = r^2 + h^2` | Тэнхлэг огтлолын тэгш өнцөгт гурвалжин, r=3, h=4 конус бүрд 3-4-5. |
| Гадаргуугийн талбай | `S = \pi r^2 + \pi r \ell` | Суурийн дугуй + дэлгэсэн сектор. |
| Секторын өнцөг | `\varphi = \frac{r}{\ell}\cdot 360°` | Дэлгэсэн конус бүтэн тойргийн r/ℓ хувийг хадгална. |

**workedExamples**

- `sg43-we1` — **statement:** Конус $r = 3$, $h = 4$. Байгуулагч ба бүтэн
  гадаргуугийн талбайг олоорой.
  **solution:** $\ell = \sqrt{9 + 16} = 5$.
  $S = \pi r(r + \ell) = \pi \cdot 3 \cdot 8 = 24\pi \approx 75.4$.
- `sg43-we2` — **statement:** $r = 3$, $\ell = 5$ конусыг тайрч дэлгэв.
  Секторын төв өнцгийг олоод, түүний нумын урт ирмэгтэй тэнцэж байгааг
  шалгаарай.
  **solution:** $\varphi = \frac{3}{5} \cdot 360° = 216°$. Нумын шалгалт:
  радиус нь $5$ байх $216°$ нумын урт
  $\frac{216}{360} \cdot 2\pi \cdot 5 = 6\pi$, яг ирмэг $2\pi \cdot 3$ ✓.

**commonMistakes**

- **text:** Хажуу гадаргууг $\pi r h$ гэж бичих.
  **correction:** Хана БАЙГУУЛАГЧИЙН дагуу налж байна:
  $S_{\text{хаж}} = \pi r \ell$, хэзээ ч $\pi r h$ биш. $\ell > h$ үргэлж биелдэг тул
  $h$ хувилбар дутуу ороодог, пирамидын талстуудтай ижил урхи.
- **text:** Конусыг $r$ радиустай сектор болгон дэлгэх.
  **correction:** Баярын малгайг хавтгай тавиарай: шулуун ирмэгүүд нь
  БАЙГУУЛАГЧ. Секторын радиус $= \ell$, нум $= 2\pi r$. Тэднийг хольж
  андуурвал талбай ба өнцгийн томьёо хоёул эвдэрнэ.

**tryIt**

- `sg43-t1` — $r = 6$, $h = 8$: байгуулагч ба бүтэн гадаргуу?
  **solution:** $\ell = \sqrt{36 + 64} = 10$;
  $S = \pi \cdot 6 \cdot 16 = 96\pi \approx 301.6$.
- `sg43-t2` — $r = 5$, $h = 12$: дэлгэсэн конус ямар төв өнцөг эзлэх вэ?
  **solution:** $\ell = 13$ (5-12-13):
  $\varphi = \frac{5}{13} \cdot 360° = \frac{1800°}{13} \approx 138.5°$.

### Interactive — same nine steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Бүтэц · **title** Тэнхлэг огтлолын гурвалжин: r, h, ℓ<br>**body** Конусыг тэнхлэгээр нь зүсээрэй: тэгш хажуут гурвалжин гарах бөгөөд түүний тал нь $r$–$h$–$\ell$ ТЭГШ ӨНЦӨГТ гурвалжин ($r = 3, h = 4, \ell = 5$-ийн хувьд доор жинхэнэ хэмжээгээр зурагдсан). Конусын асуулт бүр энэ гурвын хоёрыг олоод гурав дахийг Пифагороор гаргахаас эхэлнэ. |
| 1 | solid3d | **eyebrow** Тоглож үз · **title** Конус, амьдаар<br>**teach** $r$ ба $h$-г алхмаар өөрчлөөрэй; заалтууд π-гийн яг үржвэр хэвээр үлдэнэ. Эзлэхүүнийг ажиглаарай, тэр аль хэдийн пирамидын ⅓-ийг өмсөж байна (дараагийн хичээл үүнийг албан ёсны болгоно).<br>**config** unchanged (`solid: cone`, `r: 3`, `h: 4`, `slant: 5`) |
| 2 | teach | **eyebrow** Дэлгээрэй · **title** Конус бүр бол бялууны зүсэм<br>**body** Конусыг ирмэгээс орой хүртэл тайраад хавтгайруулж дараарай: радиус нь БАЙГУУЛАГЧ $\ell$, муруй ирмэг нь конусын ирмэг $2\pi r$ байх сектор гарна. Секторын талбай $= \pi r \ell$, энэ бол хажуу гадаргуу. Суурийн дугуй ($\pi r^2$) бүтэн гадаргуунд хамт явна: $S = \pi r(r + \ell)$. |
| 3 | arcSector | **eyebrow** Тоглож үз · **title** Дэлгэсэн конус<br>**teach** Энэ сектор БОЛ байгуулагч нь $5$ байх хавтгайруулсан конус: $216°$ төв өнцөгт түүний нум $\frac{216}{360} \cdot 2\pi \cdot 5 = 6\pi$, яг $r = 3$ конусын ирмэг. Өнцгийг чирээд малгай чангарч (өнцөг бага = конус шовх) эсвэл хавтгайрч (өнцөг их = конус намхан) байгааг төсөөлөөрэй.<br>**config** unchanged (`start: 216`, `radius: 5`) |
| 4 | tapQuestion | **eyebrow** Шалгая · **title** Өндөр биш, байгуулагч<br>**prompt** $r = 6$, $h = 8$. Хажуу гадаргуу?<br>**options** `$60\pi$` · `$48\pi$` · `$96\pi$` · `$36\pi$` — **correctIndex 0**<br>**explanation** $\ell = 10$: $S_{\text{хаж}} = \pi \cdot 6 \cdot 10 = 60\pi$. $48\pi$ бол $\pi r h$ урхи; $96\pi$ бол БҮТЭН (суурийн дугуйтай нь). |
| 5 | workedSet | **eyebrow** Бодсон жишээ · **title** Малгайг тоогоор нь<br>**intro** Үргэлж эхлээд ℓ.<br>**ex1** $r = 3$, $h = 4$: бүтэн гадаргуу? · алхам: $\ell = 5$. · алхам: $S = \pi \cdot 3 \cdot (3 + 5) = 24\pi$. · **хариу** $24\pi$<br>**ex2** Дэлгэсэн нь: радиус $5$, өнцөг $216°$ сектор. Аль конус болж эргэж ороох вэ? · алхам: Байгуулагч $= 5$; нум $= \frac{216}{360} \cdot 10\pi = 6\pi$. · алхам: Ирмэг $2\pi r = 6\pi$ тул $r = 3$ (мөн $h = 4$). · **хариу** $r = 3$, $h = 4$, $\ell = 5$ |
| 6 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Тэднийг ороож үз<br>**intro** ℓ² = r² + h², дараа нь πr(r + ℓ), эсвэл секторын хувь r/ℓ.<br>**p1** $r = 5$, $h = 12$: бүтэн гадаргуу? — **choices** `$90\pi$` · `$65\pi$` · `$85\pi$` — **answerIndex 0** — $\ell = 13$: $\pi \cdot 5 \cdot 18 = 90\pi$.<br>**p2** Конус ХАГАС дугуй (180°) болж дэлгэгдэв. Тэгвэл ℓ нь: — **choices** `$2r$` · `$r$` · `$r\sqrt2$` — **answerIndex 0** — $\frac{r}{\ell} = \frac{180}{360} = \frac12$ тул $\ell = 2r$. (Түүний өндөр: $h = \sqrt{4r^2 - r^2} = r\sqrt3$, 30-60-90 конус.)<br>**p3** $r = 8$, $\ell = 17$: өндөр нь — **choices** `$15$` · `$\sqrt{353}$` · `$9$` — **answerIndex 0** — $h = \sqrt{289 - 64} = 15$, 8-15-17 гурвал. |
| 7 | funFact | **eyebrow** Сонирхолтой баримт · **title** Чийдэнгийн бүрхүүл бол инженерийн баримт бичиг<br>**body** Төмөрчинөөс юүлүүр эсвэл чийдэнгийн бүрхүүл хийж өгөхийг хүсвэл тэдний зурах анхны зүйл бол дэлгэсэн сектор; тэд үүнийг «дэлгээс» гэж нэрлэдэг. Хоёр шулуун ирмэгийг нь хооронд нь битүүмжилдэг бөгөөд секторын өнцгийг яг таны $\varphi = \frac{r}{\ell} \cdot 360°$-ээр тооцдог. Таны гэрийн даалгавар бол хэн нэгний өдөр тутмын ажил юм. |
| 8 | recap | **eyebrow** Эргэн дүгнэлт · **title** Конус |

---

## Lesson 4 — Конусын эзлэхүүн ба огтлогдсон конус (`cone-volume-and-the-truncated-cone`)

**concreteComparison**

Зайрмагны шалгалт: нэг халбага хайлаад конусыг яг амсар хүртэл нь дүүргэх нь
зөвхөн халбаганы эзлэхүүн ⅓πr²h-тэй тэнцүү үед л болно, мөн доороосоо дээшээ
өргөссөн таны кофены аяга бол огтлогдсон конус бөгөөд баристагийн машин
түүний эзлэхүүнийг миллилитр хүртэл мэддэг.

**objective**

Конусын (V = ⅓πr²h) ба огтлогдсон конусын эзлэхүүнийг пирамидын ⅓ ба
огтлогдсон биетийн холимог томьёог дахин ашиглаж тооцоолох.

**concept**

1. Конус бол дугуй пирамид бөгөөд ⅓-ийг өвлөнө: $V = \frac13 \pi r^2 h$,
   өөрөөр хэлбэл түүнийг тойрсон цилиндрийн гуравны нэг. Ижил ус хийх
   туршилт, ижил үр дүн.

2. **Огтлогдсон конус** (суурьтай параллель зүсвэл, радиусууд нь $R$ ба $r$):
   $V = \frac{\pi h}{3}\left(R^2 + Rr + r^2\right)$, өөрөөр хэлбэл тойрогтой
   болсон огтлогдсон биетийн холимог. Түүний байгуулагч:
   $\ell^2 = h^2 + (R - r)^2$, мөн хажуу гадаргуу нь
   $S_{\text{хаж}} = \pi (R + r) \ell$.

3. Эрүүл ухааны зангуу: $r = R$ тавибал огтлогдсон томьёонууд цилиндрийнх рүү
   нурна ($\pi R^2 h$ ба $2\pi R \ell$); $r = 0$ тавибал конусынх руу нурна.
   Огтлогдсон конус хоёрын хооронд интерполяци хийж байна, яг 3-р бүлэгтэй
   адил.

**keyIdea**

Конус: V = ⅓πr²h. Огтлогдсон конус: V = (πh/3)(R² + Rr + r²), байгуулагч
ℓ² = h² + (R−r)², S_хаж = π(R+r)ℓ.

**facts**

| title | latex | explanation |
|---|---|---|
| Конусын эзлэхүүн | `V = \tfrac{1}{3}\pi r^2 h` | Өөрийн цилиндрийн гуравны нэг, бөөрөнхий болсон пирамидын ⅓. |
| Огтлогдсон эзлэхүүн | `V = \tfrac{\pi h}{3}(R^2 + Rr + r^2)` | Хоёр дугуй дээр нэмээд Rr холимог гишүүн. |
| Огтлогдсон хана | `S_{\text{хаж}} = \pi(R + r)\ell, \quad \ell^2 = h^2 + (R-r)^2` | Дундаж ирмэг × байгуулагч. |

**workedExamples**

- `sg44-we1` — **statement:** Конус $r = 3$, $h = 4$. Түүний эзлэхүүн, мөн
  ижил суурь, ижил өндөртэй цилиндрийн эзлэхүүнийг олоорой.
  **solution:** Конус: $V = \frac13 \pi \cdot 9 \cdot 4 = 12\pi \approx 37.7$.
  Цилиндр: $36\pi$, гурван конус түүнийг яг дүүргэнэ.
- `sg44-we2` — **statement:** Огтлогдсон конусын радиусууд $R = 5$, $r = 2$,
  өндөр нь $4$. Байгуулагч, хажуу гадаргуу ба эзлэхүүнийг олоорой.
  **solution:** Байгуулагч: $\ell = \sqrt{4^2 + (5-2)^2} = \sqrt{25} = 5$
  (дахин 3-4-5). Хана: $\pi(5 + 2) \cdot 5 = 35\pi$. Эзлэхүүн:
  $\frac{4\pi}{3}(25 + 10 + 4) = \frac{4\pi}{3} \cdot 39 = 52\pi \approx 163.4$.

**commonMistakes**

- **text:** Конусаас ⅓-ийг унагах (эсвэл цилиндрт нь үлдээх).
  **correction:** Шовх биетүүд (конус, пирамид) ⅓ агуулна; хавтгай оройтой нь
  (цилиндр, призм) агуулахгүй. Хэрэв таны конус ямар нэгэн байдлаар өөрийн
  цилиндрээ дийлсэн бол ␓ алга болсон байна.
- **text:** Огтлогдсон конусын эзлэхүүнд радиусуудыг дундажлах:
  $\pi((R+r)/2)^2 h$.
  **correction:** Эзлэхүүн ингэж дундажлагддаггүй, зөв холимог нь
  $\frac{\pi h}{3}(R^2 + Rr + r^2)$. Товчлол нь хязгаар дээр унадаг: $r = 0$
  үед конусын $\frac{\pi R^2 h}{3}$-ийн оронд $\frac{\pi R^2 h}{4}$ өгнө.

**tryIt**

- `sg44-t1` — $r = 6$, $h = 8$: конусын эзлэхүүн?
  **solution:** $V = \frac13 \pi \cdot 36 \cdot 8 = 96\pi \approx 301.6$.
- `sg44-t2` — Хувин бол огтлогдсон конус: ёроолын радиус $2$, амсрын радиус
  $5$, өндөр $4$ (бүгд дм-ээр). Хэдэн ЛИТР багтаах вэ? ($1$ дм³ $= 1$ л;
  $\pi \approx 3.14$ аваарай.)
  **solution:** $V = \frac{4\pi}{3}(4 + 10 + 25) = 52\pi$ дм³
  $\approx 163.4$ л. Маш том хувин, шалгаарай: ёроолын дугуй нь дангаараа ч
  $4\pi \approx 12.6$ дм² эзэлнэ.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** ⅓ буцаж ирлээ · **title** Конус бол дугуй пирамид<br>**body** 3-р бүлэгтэй ижил туршилт: дүүрэн конусыг түүнийг тойрсон цилиндр рүү юүлээрэй, гурван юүлэлт, нэг дүүрэлт. $V = \frac13 \pi r^2 h$. Кавальери үүнийг нарийвчилж баталгаажуулна: конусыг суурийн талбай ба өндөр нь тохирсон дурын пирамидтай зүсэлт зүсэлтээр нь харьцуулаарай. |
| 1 | solid3d | **eyebrow** Тоглож үз · **title** Конус ба цилиндр<br>**teach** $r = 3, h = 4$ тавиад $V = 12\pi$-г уншаарай; ижил хэмжээтэй цилиндр $36\pi$ багтаана. Хэмжээсүүдийг алхмаар өөрчлөөрэй, 1:3 харьцаа хэзээ ч хөдлөхгүй. Шовх = үргэлж гуравны нэг.<br>**config** unchanged (`solid: cone`, `r: 3`, `h: 4`, `slant: 5`) |
| 2 | tapQuestion | **eyebrow** Шалгая · **title** Халбаганы шалгалт<br>**prompt** $r = 3$, $h = 4$: конусын эзлэхүүн нь<br>**options** `$12\pi$` · `$36\pi$` · `$24\pi$` · `$16\pi$` — **correctIndex 0**<br>**explanation** $\frac13 \pi \cdot 9 \cdot 4 = 12\pi \approx 37.7$. ⅓-гүйгээр та цилиндрийн $36\pi$-г нэхэх байсан, гурав дахин өгөөмөр. |
| 3 | teach | **eyebrow** Оройг нь тайрах · **title** Огтлогдсон конус<br>**body** Суурьтай параллель зүсээрэй: радиусууд $R$ (доод) ба $r$ (дээд). Байгуулагчийн гурвалжин, жинхэнэ хэлбэрээр нь зурагдсан: дээш өндөр $h = 4$, хөндлөн радиусын зөрүү $R - r = 3$, ханын дагуу байгуулагч $\ell = 5$. Ханын талбай $\pi(R + r)\ell$ буюу дундаж ирмэгийг байгуулагчаар; эзлэхүүн $\frac{\pi h}{3}(R^2 + Rr + r^2)$ буюу 3-р бүлгийн гурван гишүүнт холимогийн тойрог хувилбар. |
| 4 | workedSet | **eyebrow** Бодсон жишээ · **title** Конус, бүтэн ба тайрсан<br>**intro** Бүтэнд нь ⅓; тайрсанд нь гурван гишүүнт холимог.<br>**ex1** $R = 5$, $r = 2$, $h = 4$: огтлогдсон эзлэхүүн? · алхам: $R^2 + Rr + r^2 = 25 + 10 + 4 = 39$. · алхам: $V = \frac{4\pi}{3} \cdot 39 = 52\pi$. · **хариу** $52\pi \approx 163.4$<br>**ex2** Ижил биет: хажуу гадаргуу? · алхам: $\ell = \sqrt{16 + 9} = 5$. · алхам: $S_{\text{хаж}} = \pi(5 + 2) \cdot 5 = 35\pi$. · **хариу** $35\pi \approx 110$ |
| 5 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Хувин ба аяга<br>**intro** Хязгаарыг шалгаарай: r = R бол цилиндр, r = 0 бол конус.<br>**p1** $r = 5$, $h = 12$: конусын эзлэхүүн? — **choices** `$100\pi$` · `$300\pi$` · `$60\pi$` — **answerIndex 0** — $\frac13 \pi \cdot 25 \cdot 12 = 100\pi$.<br>**p2** Огтлогдсон конус $R = 4$, $r = 1$, $h = 4$: байгуулагч? — **choices** `$5$` · `$4$` · `$\sqrt{17}$` — **answerIndex 0** — $\ell = \sqrt{16 + (4-1)^2} = \sqrt{25} = 5$.<br>**p3** Огтлогдсон конус $R = 4$, $r = 1$, $h = 4$: эзлэхүүн? — **choices** `$28\pi$` · `$21\pi$` · `$\dfrac{68\pi}{3}$` — **answerIndex 0** — $\frac{4\pi}{3}(16 + 4 + 1) = \frac{4\pi}{3} \cdot 21 = 28\pi$. |
| 6 | funFact | **eyebrow** Сонирхолтой баримт · **title** Архимедийн бэлтгэл дасгал<br>**body** Архимед конус = цилиндрийн ⅓ гэдгийг өөрийн шилдэг бүтээл рүү (бөмбөрцөг, дараагийн бүлэг) хүрэх алхам болгон баталсан. Үр дүнг зуун жилийн өмнө Евдокс «шавхалтын арга»-аар мэдчихсэн байсан: конусыг дотор талаас нь ба гадна талаас нь нимгэн цилиндрийн багцуудын хооронд зай нь арилтал шахна. Тэр шахалт НЬ орчин үеийн хязгаарын тодорхойлолт юм; Грекчүүд «хязгааргүй» гэдгийг чангаар хэлэхээс л татгалзсан хэрэг. |
| 7 | recap | **eyebrow** Эргэн дүгнэлт · **title** Конусын эзлэхүүн |

---

## PRACTICE

- `sg4-pr-1` — Цилиндрийн радиус $5$, өндөр $8$. Хажуу гадаргуу, бүтэн
  гадаргуу, эзлэхүүнийг нь олоорой.
  **solution:** $S_{\text{хаж}} = 2\pi \cdot 5 \cdot 8 = 80\pi$;
  $S = 80\pi + 50\pi = 130\pi$; $V = \pi \cdot 25 \cdot 8 = 200\pi$.
- `sg4-pr-2` — Цилиндрийн тэнхлэг огтлол нь диагональ нь $8\sqrt{2}$ байх
  квадрат. Цилиндрийн эзлэхүүнийг олоорой.
  **solution:** Квадратын тал $8$: $r = 4$, $h = 8$.
  $V = \pi \cdot 16 \cdot 8 = 128\pi \approx 402$.
- `sg4-pr-3` — Конусын радиус $8$, байгуулагч $17$. Өндөр, бүтэн гадаргуу,
  эзлэхүүнийг олоорой.
  **solution:** $h = \sqrt{289 - 64} = 15$ (8-15-17).
  $S = \pi \cdot 8 (8 + 17) = 200\pi$.
  $V = \frac13 \pi \cdot 64 \cdot 15 = 320\pi$.
- `sg4-pr-4` — Радиус $9$, байгуулагч $15$ конусыг дэлгэв. Секторын төв өнцөг
  ба конусын эзлэхүүнийг олоорой.
  **solution:** Өнцөг: $\frac{9}{15} \cdot 360° = 216°$. Өндөр:
  $\sqrt{225 - 81} = 12$ (9-12-15). $V = \frac13\pi \cdot 81 \cdot 12 = 324\pi$.
- `sg4-pr-5` — Радиус $3$ м, өндөр $7$ м таггүй цилиндр сав хийхэд хэр их
  төмөр хуудас (хажуу + ёроол, таггүй) хэрэгтэй вэ, мөн хэр их ус багтах вэ?
  **solution:** Төмөр:
  $2\pi \cdot 3 \cdot 7 + \pi \cdot 9 = 42\pi + 9\pi = 51\pi \approx 160.2$ м².
  Ус: $\pi \cdot 9 \cdot 7 = 63\pi \approx 197.9$ м³.
- `sg4-pr-6` — Огтлогдсон конусын радиусууд $10$ ба $4$, өндөр $8$.
  Байгуулагч ба хажуу гадаргуугийн талбайг олоорой.
  **solution:** $\ell = \sqrt{64 + 36} = 10$;
  $S_{\text{хаж}} = \pi(10 + 4) \cdot 10 = 140\pi \approx 439.8$.
- `sg4-pr-7` — Мөн тэр огтлогдсон конусын ($R = 10$, $r = 4$, $h = 8$)
  эзлэхүүнийг олоорой.
  **solution:**
  $V = \frac{8\pi}{3}(100 + 40 + 16) = \frac{8\pi}{3} \cdot 156 = 416\pi \approx 1306.9$.
- `sg4-pr-8` — Цилиндр шилний ($r = 3$, $h = 10$) дүүрэн байна. Түүнийг
  $r = 3$, $h = 5$ конус хэлбэртэй баярын аяганд юүлнэ. Хэдэн аяга дүүргэх вэ?
  **solution:** Шил: $90\pi$. Аяга: $\frac13 \pi \cdot 9 \cdot 5 = 15\pi$.
  Аяга: $\frac{90\pi}{15\pi} = 6$ яг таг.

---

## TEST YOURSELF

- `sg4-ty-1` — Радиус $4$, өндөр $3$: цилиндрийн эзлэхүүн ба бүтэн гадаргуу?
  **solution:** $V = 48\pi$; $S = 2\pi \cdot 4 \cdot 7 = 56\pi$.
- `sg4-ty-2` — Конус $r = 12$, $h = 5$. Байгуулагч ба хажуу гадаргуугийн
  талбайг олоорой.
  **solution:** $\ell = \sqrt{144 + 25} = 13$;
  $S_{\text{хаж}} = \pi \cdot 12 \cdot 13 = 156\pi$.
- `sg4-ty-3` — Конусын эзлэхүүн $96\pi$, радиус нь $6$. Өндөр ба байгуулагчийг
  олоорой.
  **solution:** $h = \frac{3 \cdot 96\pi}{36\pi} = 8$;
  $\ell = \sqrt{36 + 64} = 10$.
- `sg4-ty-4` — Тэгш талт цилиндрийн (тэнхлэг огтлол нь квадрат) эзлэхүүн
  $54\pi$. Радиусыг нь олоорой.
  **solution:** $h = 2r$: $\pi r^2 \cdot 2r = 54\pi$ тул $r^3 = 27$, $r = 3$.
- `sg4-ty-5` — Огтлогдсон конус: $R = 7$, $r = 3$, $h = 3$. Байгуулагч ба
  эзлэхүүнийг олоорой.
  **solution:** $\ell = \sqrt{9 + 16} = 5$.
  $V = \frac{3\pi}{3}(49 + 21 + 9) = 79\pi \approx 248.2$.
- `sg4-ty-6` — Конус нь радиус нь $8$ байх дөрөвний нэг дугуй ($90°$) болж
  дэлгэгдэв. Конусын суурийн радиусыг олоорой.
  **solution:** $\frac{r}{\ell} = \frac{90}{360} = \frac14$, $\ell = 8$:
  $r = 2$. (Нумын шалгалт: $\frac14 \cdot 16\pi = 4\pi = 2\pi \cdot 2$ ✓.)

---

## Notes for Khas

### 1. *Volume* is spelled two ways in production, and my drafts picked the wrong one 126 times

**The largest finding in this draft, and it is not really a translation
question — it is a live content bug plus a drafting error on top of it.**

| source | «эзлэхүүн» | «эзэлхүүн» |
|---|---|---|
| **ЭШ papers** | **78** | 3 |
| А/492 | 1 — **10.12б**, the solid-geometry line | 1 — 11.10к, the calculus volume-of-revolution line |
| **shipped mirrors** | **40** | **10** |
| my drafts | 12 | **126** |

**Production ships both.** `6-mn/geometry-area-volume`'s own topic **title** is
«Геометр: Талбай ба **эзлэхүүн**», `8-mn/roots` uses «эзлэхүүн» eleven times,
and `7-mn/geometry-scale-and-circles` uses «эзэлхүүн» ten times. Three live
Mongolian mirrors, two spellings of one word, one of them in a page title. No
gate catches it: `mn_terms.py` contains neither form.

**And my own drafts are worse.** `geometry/surface-area-and-volume` — ЭШ
Geometry unit 9, the topic that teaches these exact solids — uses «эзэлхүүн»
110 times and «эзлэхүүн» 7 times, so it is internally inconsistent too.

**This draft uses «эзлэхүүн»**, on three grounds: the exam prefers it 78 to 3;
А/492's own solid-geometry line (10.12б, the objective this very unit is mapped
to) writes it; and two of the three shipped mirrors use it, including the one
whose whole subject is volume.

**But I am not treating that as settled, because this is a spelling split and
`docs/MONGOLIAN.md` carves spelling out of the ministry's authority.** The
ministry uses both, in different sections, so it does not decide it either.
This needs you.

**What it costs to rule:** «эзлэхүүн» ⟹ 126 replacements across my drafts (110
of them in one file) and a fix to `7-mn/geometry-scale-and-circles` in
production. «эзэлхүүн» ⟹ 12 replacements in drafts, a fix to two shipped
mirrors including a page title, and divergence from the exam by 78 to 3. **I
think the exam settles it, but the production inconsistency needs fixing either
way** — and that part is a Build ship-mode job, not a translation one.

### 2. *Lateral* and *total* surface area: the exam has words and unit 9 coined different ones

`geometry/surface-area-and-volume` (unit 9) records:

> | lateral face / lateral area | **хажуугийн тал / хажуугийн талбай** | compositional, «хажуу» + «тал» both solid |

The ЭШ bank does not say that. It says:

> «Конусын суурийн радиус 6 бол **хажуу гадаргуун талбайг** ол.» (9 uses)
> «Пирамидын **бүтэн гадаргуун талбай** $[de]$ байна.» (4 uses)

So *lateral surface area* is **«хажуу гадаргуугийн талбай»** and *total surface
area* is **«бүтэн гадаргуугийн талбай»**, both exam-verbatim, and both in
sentences that are almost word for word this topic's worked examples.

Unit 9's «хажуугийн талбай» scores **zero** everywhere. This draft uses the
exam's forms. **Unit 9 should follow** — it is one find-and-replace in a file
that has not shipped, and the two units are adjacent in the same ЭШ block.

Note this does **not** disturb «гадаргуугийн талбай» for surface area in
general, which the shipped mirrors use 22 times and 2g protects.

### 3. *Slant height* is «байгуулагч», which also dissolves the «налуу» collision

Unit 9 coined **«налуу өндөр»** for slant height (17 uses across drafts),
compositionally, with zero grounding. The exam has a word:

> «Конусын **байгуулагч** нь 12 нэгж, суурийн радиус нь 8 нэгж урттай байв.»
> «Конусын **байгуулагч** суурийн хавтгайтай үүсгэх өнцгийн синус $\frac{12}{13}$»

Eight uses, all in cone problems, all of which are this topic's subject matter.

**This is a double win, because «налуу өндөр» was also carrying the collision I
flagged yesterday** (review pile 4e's fifth instance: «налуу» means *slope* in
all 19 exam uses). Adopting «байгуулагч» removes a coinage and a collision at
once, and replaces them with an exam-verbatim term.

**Unit 9 should follow here too.** Same file, same find-and-replace.

> The three corrections in Notes 1–3 all point one way: **unit 9 was drafted
> before the ЭШ-first redirect, when the exam bank was not being consulted
> first.** It is the only geometry topic in the ЭШ course whose subject the
> exam covers densely, and it was drafted as though the exam were silent. That
> is worth knowing before the remaining pre-redirect geometry drafts are
> reviewed.

### 4. «налуу цилиндр» keeps the qualified form

Per 4e's managed-collision pattern and yesterday's «налуу хэрчим»: *oblique
cylinder* is **«налуу цилиндр»**, never bare «налуу». Consistent with the
previous draft; noted only so the pattern is visible as a pattern.

### 5. «огтлогдсон конус» — corrected the same day, from a coinage to the exam's own label

**This section originally read "the one ungrounded term" and recorded the
coinage «таслагдсан конус». It was wrong, and the correction is worth keeping
visible.**

What I wrote: *truncated cone scores zero in the ministry, the exam and the
shipped mirrors — I searched «таслагдсан», «таславсан», «тайрсан» and found
nothing anywhere.* All three searches were real and all three came back empty.

**I did not search «огтлогдсон», which is the word.** The ЭШ bank carries it as
a subtopic label:

> `"subtopic": "Огтлогдсон конус"` — **12 questions**, all from the **2025A/B/C
> papers**, all Section 2 fill-ins (Q2.4.2, Q2.4.3), all tier **hard**.

Twelve questions makes it one of the three most-tested solids in the bank, tied
with rectangular parallelepipeds and behind only triangular pyramids. It is the
opposite of ungrounded.

I found this the next hour, drafting `solid-geometry/spheres`, by listing the
bank's `solid_geometry` subtopic labels — and **that list is a term source I
had never used**. It is a small controlled vocabulary stating exactly what the
exam thinks its own topics are, which is precisely the register an ЭШ draft
should match. Review pile 6m.

The draft now uses «огтлогдсон конус» throughout. Unit 9 does not cover
frustums, so nothing else needs to follow.

### 6. The exam contains this topic almost verbatim

Worth saying plainly because it is unusual: four of this draft's terms came
from ЭШ question stems that *are* its worked examples.

| draft item | ЭШ bank |
|---|---|
| `sg41-we2` «тэнхлэг огтлол нь квадрат» | «цилиндрийн **тэнхлэг огтлол** нь квадрат бол цилиндрийн өндрийг олоорой» |
| `sg43-we2` sector angle of an unrolled cone | «конусын **хажуу гадаргуугийн дэлгээс** болох **секторын** өнцгийг олоорой» |
| `sg43-t1`, `sg4-ty-2` slant height | «Конусын **байгуулагч** нь 8 нэгж, суурийн радиус нь 6 нэгж» |

This is the strongest argument yet for review pile 4j's direction: for an ЭШ
topic whose material the exam tests directly, the bank is not "corpus" — it is
the register the student will be examined in.

### 7. Decimals

**Twenty-six** — I wrote "twelve" here from memory and then counted, which is
the second time in two drafts that guessing this number was wrong. All are
inherited from the English and all are left as decimal **points** inside
`$...$` per review pile 2d, which is not applied. Gate: clean.

**Twenty-five of the twenty-six are `\approx` values** ($150.8$, $282.7$,
$301.6$, $163.4$…). That is the pattern I recorded in 2d yesterday, and this
draft confirms it about as hard as it can be confirmed: the single exception is
$h = \frac{9}{4} = 2.25$, an exact quarter.

The reason is structural rather than stylistic. **π-exact answer plus decimal
gloss is the house style of every solid-geometry solution here** — every
worked example ends `$= 48\pi \approx 150.8$` — so a ruling on 2d touches this
topic and `spheres` harder than anything outside
`10/exponential-functions`. At 26 this is the **third-largest** contributor to
2d of the thirty-six drafts, behind only `10/exponential-functions` (144) and
`9/equations-and-formulas` (44).

**2d stands at 424 shipping across 36 drafts.**
