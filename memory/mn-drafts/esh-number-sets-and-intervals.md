# Draft — `esh/number-sets-and-intervals`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

Third ЭШ topic, and the last one in the `esh/` corpus — ЭШ hub Unit 1 is
complete with this. Four lessons, ten practice items, seven test-yourself
items, topic-level strings.

Conventions per R9 and `memory/mn-drafts/README.md`: «та» register, polite
imperative «олоорой», $\emptyset$ for the empty set (the English source here
writes `\varnothing` in lesson 3 — converted).

**Terminology is unusually well grounded for this topic.** Every core term is
in the ЭШ bank, most of them heavily:

| term | ЭШ bank | ministry А/492 |
|---|---|---|
| завсар (interval) | 85 | 2 |
| зай (distance) | 77 | 10 |
| тэнцэтгэл биш (inequality) | 73 | 13 |
| рационал | 60 | 12 |
| натурал | 35 | 0 |
| иррационал | 31 | 0 |
| бүхэл тоо | 15 | 1 |
| абсолют | 13 | 0 |
| бодит тоо | 6 | 2 |
| модул | 6 | 4 |
| шийдийн олонлог | 4 | 0 |

The absolute-value words match your ruling exactly: «абсолют утга» for the
value, «модул» for the bars. Two notes on that ruling from the corpus, neither
contradicting it:

- The bank also writes **«абсолют хэмжээ»** for the same thing
  («шийдүүдийн нийлбэрийн абсолют хэмжээг ол», 3 items). A student meets both.
- Every «модул» in the bank is about a **complex number's** modulus
  («комплекс тоонуудыг үржих үед модулийг үржиж»). That is consistent — $|\cdot|$
  is the modulus in both settings — but it means a student's first meeting with
  the word may be in the complex-numbers unit, not here.

---

## The bracket finding — settled by Khas, 13 Sep 2026

**Ruling: the ЭШ hub writes `]2, 7[`.**

The English lesson taught one convention — $(a, b)$ open, $[a, b]$ closed. The
ЭШ papers use two, and among the shapes that actually discriminate (closed
$[a,b]$ is identical in both, and round-round is unusable as evidence because
coordinate pairs share its shape) the reversed one wins:

| form | count | convention |
|---|---|---|
| $]a, b[$ | 66 | reversed (French/Russian) |
| $]a, b]$ | 22 | reversed |
| $[a, b[$ | 17 | reversed |
| $[a, b)$ | 36 | standard |
| $(a, b]$ | 10 | standard |

**105 reversed against 46 standard.** Real: `$]-\infty;\ 3[$`, `$]4;\ +\infty[$`,
`$[10;12[$`, `$]0, 2]$` — with a semicolon separator as often as a comma. А/492
uses «завсар» but fixes no notation, so the papers were the only evidence.

**What changed in this draft.** Every interval in the lesson content is now
written the reversed way, and lesson 2 leads with it: the rule becomes «хаалт
дотогшоо харвал төгсгөл орно, гадагш харвал орохгүй» — a bracket facing inward
includes its endpoint, facing outward excludes it. The standard $(a, b)$ form
is still taught, because SAT, IB and foreign textbooks use it, but it is now
the alternative rather than the default.

Scope is the ЭШ hub only. The SAT and IB hubs keep $(a, b)$ — that is what
College Board and the IB write, and those hubs exist to rehearse their exams.

## Topic-level strings

**TITLE:** Тооны олонлог ба завсар

**BLURB:** $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
гэсэн үүрлэсэн гэр бүл, завсрын хоёр бичиглэл ба доторх бүхэл тоог тоолох,
тооны шулуун дээрх огтлолцол ба нэгдэл, абсолют утгыг зай гэж унших нь — ЭШ-ийн
тэнцэтгэл бишийн хариу бүр энэ хэлээр бичигддэг.

---

## Lesson 1 — `the-family-of-number-sets`

**What makes this a rewrite.** The English teaches the nesting and the rule
«simplify before classifying», and tests it on loose numbers. The exam does not
ask that way. Its item is:

> «Энэ олонлогийн бүх элемент нь иррационал тоо байх **дэд олонлог** аль нь вэ?»

— four candidate subsets, pick the one whose elements are *all* irrational. So
classification on the paper is a **filter applied across a set**, wrapped in the
subset language the sets topic just taught, and one misclassified element kills
an entire option. That changes what to emphasise: not «what is this number», but
«check every element, because one wrong call costs the whole answer».

This version therefore frames classification as a per-element sweep with
propagating cost, and names the disguises the exam actually uses (a root that
simplifies, a fraction that reduces to an integer, a repeating decimal) as a
checklist rather than as three separate observations.

**TITLE:** $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, $\mathbb{R}$ — үүрлэсэн гэр бүл

**COMPARISON:** Матрёшка хүүхэлдэй: натурал тоонууд бүхэл тоонуудын дотор,
бүхэл тоонууд рационал тоонуудын дотор, рационал тоонууд бодит тоонуудын дотор
багтана. Иррационал тоонууд бол сүүлийн хоёр хүүхэлдэйн хоорондох зай.

**OBJECTIVE:** Тоог $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$
гинжид байрлуулах, өөрчилсөн хувцастай гишүүдийг таних, олонлогийн бүх элементэд
шалгуурыг алдаагүй хэрэглэх.

**KEY IDEA:** $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$;
иррационал гэдэг нь бодит боловч рационал биш. Эхлээд хялбарчилж, дараа нь
ангилна.

**TEACHING:**

$\mathbb{N} = \{1, 2, 3, \ldots\}$ натурал тоонууд. $\mathbb{Z}$ бүхэл тоонууд
нь тэг ба сөрөг тоонуудыг нэмнэ. $\mathbb{Q}$ рационал тоонууд бол $q \ne 0$
байхад $p/q$ хэлбэрт бичигдэх бүх тоо — өөрөөр хэлбэл төгсгөлөг эсвэл үет
аравтын бутархай болох бүх тоо. $\mathbb{R}$ бодит тоонууд шулууныг бүрэн
дүүргэнэ. Гинжин дэх олонлог бүр дараагийнхаа дэд олонлог.

**Иррационал тоонууд** нь $\mathbb{R} \setminus \mathbb{Q}$: хэзээ ч төгсдөггүй,
давтагддаггүй аравтын бутархай — $\sqrt{2}$, $\pi$ гэх мэт. Эдгээр нь тавдугаар
хүүхэлдэй БИШ, харин ялгавар олонлог. Тоо нь рационал эсвэл иррационал, хоёулаа
хэзээ ч биш.

Одоо шалгалт үүнийг хэрхэн асуудгийг харъя. ЭШ-д «энэ тоо ямар олонлогийнх вэ»
гэж ганцаарчлан асуухаас илүү дараах хэлбэрээр асуудаг:

> «Энэ олонлогийн бүх элемент нь иррационал тоо байх дэд олонлог аль нь вэ?»

Дөрвөн дэд олонлог өгөөд бүх элемент нь иррационал байгааг нь сонгуулна. Энэ нь
чухал ялгаа гаргана: **элемент бүрийг шалгах ёстой**, учир нь ганц элементийг
буруу ангилвал тэр хувилбар бүхэлдээ унана. Хурдан хийж болох ажил биш.

Тиймээс хувцас тайлах гурван шалгуурыг дадал болгоно. **Язгуур** —
$\sqrt{49} = 7$ натурал тоо; язгуурын тэмдэг байгаа нь иррационал гэсэн үг биш,
харин зөвхөн бүтэн квадрат биш үед иррационал болно. **Бутархай** —
$\frac{18}{6} = 3$ бүхэл тоо. **Үет аравтын бутархай** —
$0.\overline{3} = \frac{1}{3}$ рационал. Гурвуулаа нэг дүрэмд буудаг: эхлээд
хялбарчилж, дараа нь ангилна.

**FACTS:**

1. **Гинж** — $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ —
   Натурал бүр бүхэл, бүхэл бүр рационал, рационал бүр бодит тоо.
2. **Рационал гэдгийн утга** —
   $x = \tfrac{p}{q},\ q \ne 0 \iff \text{аравтын бутархай төгсөх эсвэл давтагдах}$ —
   Хоёр тэнцүү хүчинтэй шалгуур; тооны хувцас аль нь тохирохыг зааж өгнө.

**MISTAKES:**

- Язгуурын тэмдэгтэй учраас $\sqrt{49}$-г иррационал гэж ангилах. Эхлээд
  хялбарчилна: $\sqrt{49} = 7$. Хувцас нь тоо өөрөө биш.
- $\frac{22}{7}$ ойрхон учраас $\pi$-г рационал гэх. $\frac{22}{7}$ бол ойролцоо
  утга болохоос тэнцэл биш. $\pi$-д яг тэнцүү бутархай хэлбэр байхгүй — энэ нь
  өөрөө иррационал гэдгийн тодорхойлолт.

**WORKED esh-int-l1-we1:**

- **PROBLEM:** $\sqrt{49}$, $-\frac{12}{4}$, $0.\overline{3}$, $\sqrt{8}$ тоо
  тус бүрийг хамгийн нарийн олонлогт нь ангилаарай.
- **WORKING:** $\sqrt{49} = 7 \in \mathbb{N}$. $-\frac{12}{4} = -3 \in \mathbb{Z}$
  ($\mathbb{N}$ биш, учир нь сөрөг). $0.\overline{3} = \frac{1}{3} \in \mathbb{Q}$.
  $\sqrt{8} = 2\sqrt{2}$ иррационал — $8$ нь бүтэн квадрат биш.
- **ANSWER:** $\mathbb{N}$, $\mathbb{Z}$, $\mathbb{Q}$, иррационал

**WORKED esh-int-l1-we2:**

- **PROBLEM:** $\frac{\sqrt{50}}{\sqrt{2}}$ нь рационал уу, иррационал уу?
- **WORKING:** Дүгнэхээсээ өмнө хялбарчилна:
  $\frac{\sqrt{50}}{\sqrt{2}} = \sqrt{25} = 5$ — натурал тоо. Иррационал
  хэсгүүд нийлээд рационал үр дүн өгч болно.
- **ANSWER:** Рационал (бүр натурал), $5$

**TRY esh-int-l1-t1:**

- **PROBLEM:** $\sqrt{36}$, $\sqrt{18}$, $-\frac{20}{5}$, $0.121212\ldots$
  тоонуудаас аль нь рационал вэ?
- **ANSWER:** Гурав нь — $\sqrt{36}$, $-\frac{20}{5}$, $0.\overline{12}$
- **WORKING:** $\sqrt{36} = 6$; $-\frac{20}{5} = -4$;
  $0.\overline{12} = \frac{12}{99} = \frac{4}{33}$. Харин $\sqrt{18} = 3\sqrt{2}$
  иррационал. Дөрвөөс гурав нь.

**TRY esh-int-l1-t2:**

- **PROBLEM:** $\sqrt{2} \cdot \sqrt{32}$-ийн утгыг олоод ангилаарай.
- **ANSWER:** $8$, натурал тоо
- **WORKING:** $\sqrt{2} \cdot \sqrt{32} = \sqrt{64} = 8$ — хоёр иррационал
  үржигдэхүүнээс натурал тоо гарлаа.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Хүүхэлдэйнүүд · **title** Дөрвөн үүрлэсэн олонлог, нэг завсар<br>**body** $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$ — хүүхэлдэй бүр дараагийндаа багтана. Иррационал тоонууд хүүхэлдэй биш: тэдгээр нь $\mathbb{Q}$ ба $\mathbb{R}$ хоёрын хоорондох зай бөгөөд рационал БИШ гэдгээрээ тодорхойлогдоно. |
| 1 | worked | **title** Хувцас өмссөн тоонууд — `esh-int-l1-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Хувцсыг нь шалга<br>**prompt** Аль тоо нь иррационал вэ?<br>**options** `$\sqrt{12}$` · `$\sqrt{\frac{16}{25}}$` · `$0.\overline{7}$` · `$-\frac{35}{7}$` — **correctIndex 0**<br>**explanation** $\sqrt{12} = 2\sqrt{3}$ — $12$ нь бүтэн квадрат биш. Бусад нь $\frac{4}{5}$, $\frac{7}{9}$, $-5$ болж хялбарчлагдана: бүгд рационал. |
| 3 | worked | **title** Иррационал хэсгүүд, рационал бүтэн — `esh-int-l1-we2` |
| 4 | tryIt | **title** Дөрвөөс гурав — `esh-int-l1-t1` |
| 5 | tryIt | **title** Рационал үржвэр — `esh-int-l1-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** $\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$; иррационал $= \mathbb{R} \setminus \mathbb{Q}$ · Рационал $\iff$ төгсгөлөг буюу үет аравтын бутархай $\iff$ бутархай хэлбэртэй · Эхлээд ХЯЛБАРЧИЛНА — язгуур ба бутархай хувцаслах дуртай · Дэд олонлог сонгох бодлогод элемент БҮРИЙГ шалгана: нэг алдаа хувилбарыг бүхэлд нь унагана |

---

## Lesson 2 — `interval-notation`

**What makes this a rewrite.** See the bracket finding above — it is the reason
this lesson exists in a different shape. The English teaches $(a, b)$ and
$[a, b]$ and stops. The ЭШ papers write $]a, b[$ more often than $[a, b)$ and
$(a, b]$ combined, and separate the endpoints with a semicolon as readily as a
comma. A student who has only ever seen the English convention can lose an item
to notation alone, having understood the mathematics perfectly.

So the second concept paragraph — which in English is about rays to infinity —
becomes the two-convention dictionary, and the ray material folds into the
first and third paragraphs. The tap-question is rebuilt to test reading the
reversed form, since recognising it is the skill the paper actually demands.

**TITLE:** Завсар ба түүний бичиглэл

**COMPARISON:** Автобусны маршрут дахь буудлууд: хаалт дотогшоо харвал автобус
буудал ДЭЭР зогсоно, гадагш харвал зогсолгүй өнгөрнө гэсэн үг. Хооронд нь байгаа
зам хоёр тохиолдолд ч үйлчилнэ.

**OBJECTIVE:** Тэнцэтгэл биш, тооны шулуун дээрх зураг, завсрын бичиглэл гурвын
хооронд чөлөөтэй хөрвүүлэх; ЭШ-д тохиолддог хоёр өөр хаалтны бичиглэлийг
хоёуланг нь уншиж чадах.

**KEY IDEA:** Дотогшоо харсан хаалт төгсгөлийг оруулна, гадагш харсан нь
оруулахгүй; $\infty$ үргэлж гадагш. Урт нь $b - a$, хаалтнаас хамаарахгүй — харин доторх
бүхэл тооны ТОО хамаарна.

**TEACHING:**

$[a, b]$ хоёр төгсгөлийг хоёуланг нь оруулна ($a \le x \le b$); $]a, b[$
хоёуланг нь хасна ($a < x < b$); $[a, b[$ ба $]a, b]$ холимог. Дүрэм нь ганц:
**хаалт дотогшоо харвал төгсгөл орно, гадагш харвал орохгүй.** Тооны шулуун
дээр дүүрэн цэг ба хоосон цэг.

**Хоёр өөр бичиглэл бий, хоёуланг нь таних хэрэгтэй.** Бид ЭШ-ийн хувилбарууд
шиг **эргүүлсэн дөрвөлжин хаалт** хэрэглэнэ. Гадаадын сурах бичиг, мөн SAT, IB-д
дугуй хаалттай бичлэг тохиолдох тул хоёрын тэнцлийг мэдэж байх хэрэгтэй:

$$]a,\ b[ \;=\; (a, b), \qquad ]a,\ b] \;=\; (a, b], \qquad [a,\ b[ \;=\; [a, b).$$

Өөрөөр хэлбэл хаалт нь завсраас **гадагш** харвал төгсгөл орохгүй. Жинхэнэ
шалгалтын бичлэгүүд: $]-\infty;\ 3[$, $]4;\ +\infty[$, $[10;12[$, $]0, 2]$.
Мөн таслалын оронд **цэг таслал** хэрэглэсэн байхыг анзаараарай. Эдгээр нь
өөр математик биш, зөвхөн өөр бичиглэл — гэхдээ танихгүй бол ойлгосон бодлогоо
бичиглэлээр алдана.

Хязгааргүй рүү сунасан завсар $\infty$ тэмдэг хэрэглэнэ: $x > 3$ нь
$]3, \infty[$, $x \le -1$ нь $]-\infty, -1]$. $\infty$ нь ҮРГЭЛЖ гадагш харсан
хаалттай — энэ нь чиглэл болохоос хүрч болох төгсгөл биш. Бүхэл
шулуун нь $]-\infty, \infty[ = \mathbb{R}$.

Хязгаарлагдмал завсрын урт нь хаалтнаас үл хамааран $b - a$ — төгсгөлийн цэг
өргөнгүй. Харин бүхэл тооны ТОО хаалтнаас хамаарна, тэндээс энэ хичээл нэгдүгээр
бүлгийн тоололтой дахин холбогдоно.

**FACTS:**

1. **Хязгаарлагдмал завсрын дөрвөн хэлбэр** —
   $[a,b],\quad ]a,b[,\quad [a,b[,\quad ]a,b]$ —
   Хаалт нь төгсгөлийн харьяаллыг тэмдэглэнэ; дотор тал нь ижил.
2. **Эргүүлсэн хаалтны бичиглэл** —
   $]a, b[ \;=\; (a, b), \qquad [a, b[ \;=\; [a, b)$ —
   Бид эргүүлсэн хэлбэрийг бичнэ; дугуй хаалттай хэлбэрийг таньж чаддаг байхад
   хангалттай.

**MISTAKES:**

- $x \ge 3$-ыг $[3, \infty]$ гэж бичих. Ямар ч тоо $\infty$-тэй тэнцэхгүй тул
  түүнийг «оруулах» боломжгүй: $[3, \infty[$.
- $]2, 5[$ ба $[2, 5]$ өөр урттай гэж бодох. Хоёулаа $3$ урттай — ганц цэг
  өргөн эзлэхгүй. Зөвхөн бүхэл тооны ТОО хаалтнаас хамаарна.

**WORKED esh-int-l2-we1:**

- **PROBLEM:** $-3 < x \le 7$-г завсрын бичиглэлээр бичээд уртыг нь олоорой.
- **WORKING:** $-3$ дээр нээлттэй, $7$ дээр хаалттай: $]-3, 7]$, эргүүлсэн
  бичиглэлээр $]-3, 7]$. Урт $= 7 - (-3) = 10$.
- **ANSWER:** $]-3, 7]$, урт нь $10$

**WORKED esh-int-l2-we2:**

- **PROBLEM:** $]-3, 7]$ дотор хэдэн БҮХЭЛ тоо байна вэ? $[-3, 7]$ дотор яах вэ?
- **WORKING:** $]-3, 7]$ нь $-2, \ldots, 7$-г агуулна: $7 - (-2) + 1 = 10$ бүхэл
  тоо. Зүүн төгсгөлийг хаавал $-3$ өөрөө нэмэгдэнэ: $11$.
- **ANSWER:** $10$ ба $11$

**TRY esh-int-l2-t1:**

- **PROBLEM:** $\{x : x \ge -4\}$ ба $\{x : x < 6\}$-г завсрын бичиглэлээр
  бичээд, огтлолцлынх нь уртыг олоорой.
- **ANSWER:** $[-4, \infty[$, $]-\infty, 6[$, огтлолцлын урт $10$
- **WORKING:** Огтлолцол нь $[-4, 6[$ бөгөөд урт нь $6 - (-4) = 10$.

**TRY esh-int-l2-t2:**

- **PROBLEM:** $[-5, 5[$ завсарт хэдэн бүхэл тоо байна вэ?
- **ANSWER:** $10$
- **WORKING:** $-5$-аас $4$ хүртэл: $4 - (-5) + 1 = 10$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Хаалтууд · **title** Зогсох уу, өнгөрөх үү<br>**body** Нэг дүрэм бүх хичээлийг үүрнэ: дөрвөлжин хаалт төгсгөл дээр зогсоно, дугуй хаалт өнгөрч явна. Тэнцэтгэл бишийн $\le$ ба $<$-г хаалт болгон хөрвүүлбэл бичиглэл өөрөө бичигдэнэ. |
| 1 | worked | **title** Тэнцэтгэл бишээс завсар руу — `esh-int-l2-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Хоёр бичиглэл, нэг завсар<br>**prompt** ЭШ-ийн хувилбарт $]-\infty;\ 4]$ гэж бичжээ. Энэ юу гэсэн үг вэ?<br>**options** `$x \le 4$` · `$x < 4$` · `$x \ge 4$` · `Ийм завсар байхгүй` — **correctIndex 0**<br>**explanation** Эргүүлсэн бичиглэлд хаалт гадагш харвал төгсгөл орохгүй. Баруун талын $]$ нь дотогш харж байгаа тул $4$ орно; $\infty$ хэзээ ч орохгүй. Стандарт бичиглэлээр $]-\infty, 4]$, өөрөөр хэлбэл $x \le 4$. |
| 3 | worked | **title** Доторх бүхэл тоог тоолох — `esh-int-l2-we2` |
| 4 | tryIt | **title** Хоёр туяа, нэг давхцал — `esh-int-l2-t1` |
| 5 | tryIt | **title** Хагас нээлттэй тоолол — `esh-int-l2-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** $\le, \ge \to$ дөрвөлжин хаалт; $<, > \to$ дугуй хаалт; $\infty$ үргэлж дугуй · $]a, b[$ нь $]a, b[$-тэй ижил — ЭШ хоёуланг нь хэрэглэдэг, цэг таслалтай ч бичдэг · Урт $= b - a$, хаалт нөлөөлөхгүй · Бүхэл тооны тоо хаалтнаас ХАМААРНА — төгсгөлүүдээ дахин тоолно |

---

## Lesson 3 — `combining-intervals`

**What makes this a rewrite.** The English reaches systems of inequalities in
its third paragraph, as an application. On the paper that is not an application,
it is the wrapper: the item reads

> «... $\geq 0$ тэнцэтгэл бишүүдийг нэгэн зэрэг хангах **шийдийн олонлогийг** ол»

— «find the solution set satisfying the inequalities simultaneously». Interval
intersection is the technique *inside* that question, never the question itself.
So this version opens with the system framing and «шийдийн олонлог» (the bank's
own phrase, 4 uses), and the max/min endpoint rule arrives as the tool that
answers it. The two-piece union stays where the English put it, because the
«эсвэл» case genuinely is the smaller half of the lesson.

**TITLE:** Завсруудын огтлолцол ба нэгдэл

**COMPARISON:** Хоёр найзын чөлөөт цаг: хоёулаа сул байхад л уулзаж чадна —
хожуу эхэлсэн нь эхлэл, эрт дууссан нь төгсгөл болно. Хоёрын ядаж нэг нь сул
байх хугацаа бол нэгдэл бөгөөд тэр нь тасарсан хоёр хэсэг байж мэднэ.

**OBJECTIVE:** Тооны шулуун дээр завсруудыг огтлолцуулж, нэгтгэх; нэгдэл хоёр
тасархай хэсэг хэвээр үлдэх, огтлолцол хоосон болох тохиолдлыг таних; тэнцэтгэл
бишийн системийн шийдийн олонлогийг бичих.

**KEY IDEA:** Огтлолцол: $[\max]a,c[, \min]b,d[]$, хоосон байж болно. Нэгдэл:
хүрэлцэж байвал нийлнэ, үгүй бол $\cup$-тэй хоёр хэсэг.

**TEACHING:**

ЭШ дээр энэ хичээл ихэвчлэн «завсрыг огтлолцуул» гэж шууд ирдэггүй. Ирдэг
хэлбэр нь:

> «... тэнцэтгэл бишүүдийг нэгэн зэрэг хангах шийдийн олонлогийг ол»

Хэд хэдэн тэнцэтгэл биш өгөөд бүгдийг нь **нэгэн зэрэг** хангах $x$-үүдийг
асууна. «Нэгэн зэрэг» гэдэг нь огтлолцол. Тэнцэтгэл биш бүр нэг завсар өгөх тул
асуулт нь завсруудын огтлолцлыг олох ажил болж хувирна — $x > -2$ БА $x \le 5$
нь $]-2, 5]$. «Эсвэл» гэсэн нөхцөл байвал нэгдэл болно.

**Огтлолцлын дүрэм** нь хоёрхон харьцуулалт: давхцал нь ТОМ зүүн төгсгөлөөс
эхэлж, ЖИЖИГ баруун төгсгөлд дуусна:
$[a, b] \cap [c, d] = [\max]a,c[, \min]b,d[]$. Хэрэв $\max]a,c[ > \min]b,d[$
бол давхцал огт байхгүй — огтлолцол $\emptyset$.

**Нэгдэл** нь завсрууд хүрэлцэж эсвэл давхцаж байвал нийлнэ; үгүй бол
огтлолцолгүй хоёр хэсэг хэвээр $\cup$-тэй бичигдэнэ.
$]-\infty, 1[ \cup ]3, \infty[$-ийг илүү хялбар болгох хэлбэр байхгүй — хэсгээр
нь үлдээх нь өөрөө хариу.

Бичиглэл рүү орохоосоо өмнө тооны шулуунаа зурах нь энэ хичээлийн бараг бүх
алдааг урьдчилан сэргийлнэ.

**FACTS:**

1. **Завсруудын огтлолцол** — $[a,b] \cap [c,d] = [\max]a,c[, \min]b,d[]$ —
   Хожуу эхлэл, эрт төгсгөл — хөндлөн гарвал хоосон.
2. **Ба, эсвэл** — $\text{ба} \to \cap, \qquad \text{эсвэл} \to \cup$ —
   Нэгдүгээр бүлгийн ижил хөрвүүлэлт, одоо тооны шулуун дээр.

**MISTAKES:**

- Тасарсан хоёр хэсгийн нэгдлийг нэг завсар болгож нийлүүлэх:
  $]-\infty,1[ \cup ]3,\infty[ = ]3,1[$ гэх мэт. Хэсгүүд хүрэлцэхгүй бол
  тусдаа хэвээр үлдэнэ. $]3, 1[$ гэдэг завсар ч биш — нэгдэл $\cup$-гээ хадгална.
- Огтлолцолд ЖИЖИГ зүүн төгсгөлийг авах. Огтлолцол нь ХОЁУЛАА эхэлсэн цэгээс
  эхэлнэ, өөрөөр хэлбэл ТОМ зүүн төгсгөлөөс. Жижиг нь нэгдэлд харьяалагдана.

**WORKED esh-int-l3-we1:**

- **PROBLEM:** $[-4, 6] \cap ]1, 9]$ ба түүний уртыг олоорой.
- **WORKING:** Хожуу эхлэл: $\max]-4, 1[ = 1$ (дугуй хаалтнаас нээлттэй); эрт
  төгсгөл: $\min]6, 9[ = 6$ (хаалттай). Огтлолцол нь $]1, 6]$, урт нь
  $6 - 1 = 5$.
- **ANSWER:** $]1, 6]$, урт нь $5$

**WORKED esh-int-l3-we2:**

- **PROBLEM:** $x \ge -1$, $x < 4$, $x \ne 2$ системийн шийдийн олонлогийг
  завсрын бичиглэлээр бичээрэй.
- **WORKING:** Эхний хоёр нь $[-1, 4[$ өгнө; $2$ гэсэн ганц цэгийг хасахад
  завсар хоёр хуваагдана: $[-1, 2[ \cup ]2, 4[$. Уртууд нь $2 - (-1) = 3$ ба
  $4 - 2 = 2$ — нийлбэр нь $5$, өөрөөр хэлбэл анхны урт хэвээр, учир нь цэг
  өргөнгүй.
- **ANSWER:** $[-1, 2[ \cup ]2, 4[$

**TRY esh-int-l3-t1:**

- **PROBLEM:** $]-\infty, 3] \cap ]-2, \infty[$ ба доторх бүхэл тооны тоог
  олоорой.
- **ANSWER:** $]-2, 3]$, бүхэл тоо нь $5$
- **WORKING:** Давхцал: $]-2, 3]$, доторх бүхэл тоонууд $-1, 0, 1, 2, 3$ буюу
  $3 - (-1) + 1 = 5$ ширхэг.

**TRY esh-int-l3-t2:**

- **PROBLEM:** $[5, 8] \cap [9, 12]$ хоосон юу? Төгсгөлийн дүрмээр
  үндэслээрэй.
- **ANSWER:** Тийм, хоосон
- **WORKING:** $\max]5, 9[ = 9 > \min]8, 12[ = 8$ — хожуу эхлэл нь эрт төгсгөлөөс
  хойно байгаа тул огтлолцол нь $\emptyset$.

### Interactive — same seven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Давхцлын дүрэм · **title** Хожуу эхлэл, эрт төгсгөл<br>**body** Завсруудын огтлолцол бүр ижил хоёр харьцуулалт: давхцал нь том зүүн төгсгөлөөс эхэлж, жижиг баруун төгсгөлд дуусна. Хэрэв тэдгээр нь хөндлөн гарвал давхцал огт байхгүй. ЭШ үүнийг «нэгэн зэрэг хангах шийдийн олонлог» гэсэн нэрээр асуудаг. |
| 1 | worked | **title** Max, min ба хаалтууд — `esh-int-l3-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Эхлээд зур<br>**prompt** $]-\infty, 2[ \cup [2, \infty[$ юутай тэнцүү вэ?<br>**options** `$\mathbb{R}$` · `$\emptyset$` · `$]-\infty, 2[$` · `огтлолцолгүй хоёр хэсэг` — **correctIndex 0**<br>**explanation** Хоёр хэсэг яг $2$ дээр уулзах бөгөөд баруун хэсэг нь $2$-г агуулна — хамтдаа бүхэл шулууныг хучна: $\mathbb{R}$. |
| 3 | worked | **title** Цоорсон завсар — `esh-int-l3-we2` |
| 4 | tryIt | **title** Хоёр туяа уулзана — `esh-int-l3-t1` |
| 5 | tryIt | **title** Давхцал байхгүй үед — `esh-int-l3-t2` |
| 6 | recap | **title** Санаж үлдэх зүйл<br>**points** Огтлолцол $= [\max, \min]$; төгсгөлүүд хөндлөн гарвал $\emptyset$ · Нэгдэл зөвхөн хэсгүүд хүрэлцэж байвал нийлнэ, үгүй бол $\cup$-гээ хадгална · «Нэгэн зэрэг хангах» гэдэг нь огтлолцол; «эсвэл» гэдэг нь нэгдэл · Эхлээд шулуунаа зурна — бичиглэл дараа нь |

---

## Lesson 4 — `absolute-value-as-distance`

**What makes this a rewrite.** The English builds the leash picture and applies
it. The picture is good and stays. What changes is the framing of *why* it is
worth building, because the ЭШ items that involve $|\cdot|$ are mostly
equations, not interval questions — «$(5x-1)(x+2)=3$ тэгшитгэлийн шийдүүдийн
нийлбэрийн абсолют хэмжээг ол» is the shape that recurs. The distance reading
is what makes those tractable, so this version says so and connects the two,
rather than presenting distance as a self-contained trick for interval items.

Your absolute-value ruling is applied exactly: **«абсолют утга»** is the value,
**«модул»** is the bars, and the lesson names both because the bank uses both
(«абсолют хэмжээ» appears too, noted in the header). The fun-fact is pointed at
this course's own calculus units rather than at «university analysis» in the
abstract — the ЭШ course teaches limits and derivatives, so the $\varepsilon$
connection is a forward reference inside the same hub, not a remark about
somewhere else.

**TITLE:** Абсолют утга нь зай

**COMPARISON:** $a$ цэгт хадсан уяа: $|x - a| < r$ гэдэг нь нохой хүрч чадах
бүх газар буюу $a$-г тойрсон $r$ радиустай нээлттэй завсар. Уяаг тасалбал
($> r$) нохой тэр хэсгээс ГАДНА хаана ч байж болно.

**OBJECTIVE:** $|x - a| < r$ ба $|x - a| > r$-г завсар болон туяануудын нэгдэл
болгон хөрвүүлэх, өгсөн завсрыг абсолют утгатай нөхцөл болгон бичих.

**KEY IDEA:** $|x - a| < r \iff a - r < x < a + r$; $>$ хувилбар нь гадна талын
хоёр хэсэг. Завсраас нөхцөл рүү: төв ба радиусаар.

**TEACHING:**

$|x - a|$ гэдэг нь $x$-ээс $a$ хүртэлх **зай**. Босоо зураасыг нь **модул** гэж,
гарч ирэх утгыг нь **абсолют утга** гэж нэрлэнэ (ЭШ-ийн зарим хувилбар «абсолют
хэмжээ» гэж бичсэн байдаг — ижил зүйл).

Зай гэж уншмагц хоёр төрлийн тэнцэтгэл биш геометр болно. $|x - a| < r$ нь
$a$-аас $r$-ээс дотогш байх бүх цэгийг цуглуулна: $]a - r, a + r[$ завсар.
$\le$ бол төгсгөлүүд нь нэгдэнэ: $[a - r, a + r]$.

$|x - a| > r$ бол уяаны цаад тал: $]-\infty, a - r[ \cup ]a + r, \infty[$ —
**үргэлж ХОЁР хэсэг**. Абсолют утгатай «их» тэнцэтгэл биш нэг завсар болж хэзээ
ч хураагддаггүй.

Урвуу чиглэл нь шалгалтын дуртай хэлбэр: $]2, 10[$ завсрын төв нь
$\frac{2 + 10}{2} = 6$, радиус нь $\frac{10 - 2}{2} = 4$, тиймээс энэ нь яг
$|x - 6| < 4$. Төв–радиусын хэлбэр аливаа тэгш хэмтэй нөхцөлийг нэг мөр болгоно.

Энэ зургийг барих нь яагаад үнэ цэнэтэй вэ. ЭШ-д абсолют утга ихэвчлэн завсрын
бодлогод биш, **модулт тэгшитгэл**-д гарч ирдэг — жишээ нь «тэгшитгэлийн
шийдүүдийн нийлбэрийн абсолют хэмжээг ол» гэсэн хэлбэрээр. Тийм бодлогод
модулаас салах гол арга нь яг энэ зай уншлага: $|A| = B$ гэдэг нь $A$-аас
тэгийг хүртэлх зай $B$ гэсэн үг тул $A = B$ эсвэл $A = -B$. Уяаны зураг ба
модулт тэгшитгэл хоёр нэг ижил санаа.

**FACTS:**

1. **Уяаны дотор** — $|x - a| < r \iff x \in ]a - r,\ a + r[$ —
   Зай нь $r$-ээс бага: $a$-г тойрсон нээлттэй завсар.
2. **Төв ба радиус** — $a = \tfrac{p + q}{2}, \qquad r = \tfrac{q - p}{2}$ —
   Аливаа $]p, q[$ завсар нь эдгээр утгатай $|x - a| < r$ болно.

**MISTAKES:**

- $|x - 3| > 5$-г нэг $]-2, 8[$ завсар гэж бодох. «Их» гэдэг нь ГАДНА тал:
  $]-\infty, -2[ \cup ]8, \infty[$. Нэг завсар нь $<$ тохиолдол.
- $|x + 2| < 3$-г $+2$ дээр төвлөрсөн гэж унших.
  $|x + 2| = |x - (-2)|$ — төв нь $-2$. Төвийг уншихаасаа өмнө дотор талыг
  $x - a$ хэлбэрт оруулна.

**WORKED esh-int-l4-we1:**

- **PROBLEM:** $|x - 3| \le 5$-г бодоод шийдийн олонлог дахь бүхэл тооны тоог
  олоорой.
- **WORKING:** $3$-аас хол зай нь ихдээ $5$: $[3 - 5, 3 + 5] = [-2, 8]$. Бүхэл
  тоо: $8 - (-2) + 1 = 11$.
- **ANSWER:** $[-2, 8]$, $11$ бүхэл тоо

**WORKED esh-int-l4-we2:**

- **PROBLEM:** $]-1, 9[$ завсрыг абсолют утгатай тэнцэтгэл биш болгон
  бичээрэй.
- **WORKING:** Төв $\frac{-1 + 9}{2} = 4$, радиус $\frac{9 - (-1)}{2} = 5$:
  $|x - 4| < 5$.
- **ANSWER:** $|x - 4| < 5$

**TRY esh-int-l4-t1:**

- **PROBLEM:** $|x + 2| < 3$-г завсрын бичиглэлээр бодоорой.
- **ANSWER:** $]-5, 1[$
- **WORKING:** Төв $-2$, радиус $3$: $]-2 - 3, -2 + 3[ = ]-5, 1[$.

**TRY esh-int-l4-t2:**

- **PROBLEM:** $[1, 13]$-г $|x - a| \le r$ хэлбэрт бичээрэй.
- **ANSWER:** $|x - 7| \le 6$
- **WORKING:** Төв $\frac{1 + 13}{2} = 7$, радиус $\frac{13 - 1}{2} = 6$.

### Interactive — same eight steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Уяа · **title** Зайг зурагт буулгах<br>**body** $\|x - a\|$-г «$x$ нь $a$-аас хэр хол вэ» гэж уншвал хоёр төрлийн тэнцэтгэл биш геометр болно: $< r$ бол хүрч чадах зай, $> r$ бол түүнээс цааш байгаа бүх зүйл — үргэлж хоёр хэсэг. |
| 1 | worked | **title** Таван нэгжийн уяа — `esh-int-l4-we1` |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Дотор уу, гадна уу<br>**prompt** $\|x - 6\| > 2$-ийн шийдийн олонлог юу вэ?<br>**options** `$]-\infty, 4[ \cup ]8, \infty[$` · `$]4, 8[$` · `$[4, 8]$` · `$]8, \infty[$` — **correctIndex 0**<br>**explanation** $6$-аас хол зай нь $2$-оос их гэдэг нь $x$ зүүн талд $4$-өөс цааш, эсвэл баруун талд $8$-аас цааш байна гэсэн үг — хоёулаа, зөвхөн нэг нь биш. |
| 3 | worked | **title** Завсраас нөхцөл рүү — `esh-int-l4-we2` |
| 4 | tryIt | **title** Шилжсэн төв — `esh-int-l4-t1` |
| 5 | tryIt | **title** Урвуугаар, хаалттайгаар — `esh-int-l4-t2` |
| 6 | funFact | **eyebrow** Сонирхолтой баримт · **title** Дараа нь дахин уулзах $\varepsilon$<br>**body** Энэ курсын хязгаар ба уламжлалын бүлэгт та яг энэ уншлагатай дахин таарна: $\|x - a\| < \varepsilon$ гэдэг нь «$a$-аас $\varepsilon$-ээс дотогш». Өнөөдөр барьсан уяаны зураг тэнд хязгаарын хатуу тодорхойлолт болж хувирна — шинэ санаа биш, ижил санаа. |
| 7 | recap | **title** Санаж үлдэх зүйл<br>**points** $\|x - a\| < r$: $]a - r, a + r[$ завсар; $\le$ бол хаалттай · $\|x - a\| > r$: хоёр хэсэг — нэг завсар хэзээ ч биш · Завсраас нөхцөл рүү: төв $= \frac{p+q}{2}$, радиус $= \frac{q-p}{2}$ · Босоо зураас нь модул, гарах утга нь абсолют утга |

---

## Practice — ten items, same ids, same `check[]`

**esh-int-p1** — $\sqrt{81}$, $-\frac{14}{2}$, $\sqrt{20}$, $0.\overline{45}$-г
натурал, бүхэл, рационал, иррационалын аль нь болохыг (хамгийн нарийн олонлогоор)
тодорхойлоорой.
> $\sqrt{81} = 9 \in \mathbb{N}$; $-\frac{14}{2} = -7 \in \mathbb{Z}$;
> $\sqrt{20} = 2\sqrt{5}$ иррационал;
> $0.\overline{45} = \frac{45}{99} = \frac{5}{11} \in \mathbb{Q}$.

**esh-int-p2** — $-6 \le x < 2$-г завсрын бичиглэлээр бичээд уртыг нь болон
доторх бүхэл тооны тоог олоорой.
> $[-6, 2[$; урт $= 2 - (-6) = 8$; бүхэл тоонууд $-6$-аас $1$ хүртэл:
> $1 - (-6) + 1 = 8$.

**esh-int-p3** — $[-2, 5[ \cap [0, 8]$ ба $[-2, 5[ \cup [0, 8]$-г олоорой.
> Огтлолцол: хожуу эхлэл $\max]-2, 0[ = 0$, эрт төгсгөл $\min]5, 8[ = 5$
> (нээлттэй) — $[0, 5[$. Хэсгүүд давхцаж байгаа тул нэгдэл нийлнэ: $[-2, 8]$.

**esh-int-p4** — $|x - 5| < 3$-г бодоод хэдэн бүхэл тоо хангахыг олоорой.
> $]2, 8[$: бүхэл тоонууд $3$-аас $7$ хүртэл — $7 - 3 + 1 = 5$ ширхэг.

**esh-int-p5** — $|x + 1| \ge 4$-г завсрын бичиглэлээр бодоорой.
> Төв $-1$, радиус $4$. «Их буюу тэнцүү» гэдэг нь гадна тал:
> $]-\infty, -5] \cup [3, \infty[$.

**esh-int-p6** — $\{x : 3 < x < 11\}$ олонлогийг абсолют утгатай тэнцэтгэл биш
болгон бичээрэй.
> Төв $7$, радиус $4$: $|x - 7| < 4$.

**esh-int-p7** — $\frac{\sqrt{27}}{\sqrt{3}}$ рационал уу? Утгыг нь олоорой.
> $\sqrt{27}/\sqrt{3} = \sqrt{9} = 3$ — рационал, бүр натурал тоо.

**esh-int-p8** — $x > -3$, $x \le 6$, $x \ne 0$ системийн шийдийн олонлогийг
завсрын бичиглэлээр бичээрэй.
> $]-3, 6]$-аас $0$ цэгийг хасна: $]-3, 0[ \cup ]0, 6]$.

**esh-int-p9** — $|x - 4| \le 2$ ба $x$ тэгш байх бүхэл $x$ утгууд аль нь вэ?
> $[2, 6]$ завсарт $2, 3, 4, 5, 6$ бүхэл тоонууд байх ба тэгш нь $2, 4, 6$ —
> гурван утга.

**esh-int-p10** — $[a, 10]$ ба $[4, 7]$ завсрын огтлолцлын урт $3$ бол, мөн
$a \le 4$ бол огтлолцлыг олоорой.
> $a \le 4$ үед давхцал нь $[\max]a,4[, \min]10,7[] = [4, 7]$ бөгөөд урт нь
> $7 - 4 = 3$ — нөхцөлтэй таарч байна. Иймд огтлолцол нь $[4, 7]$ өөрөө.

---

## Test yourself — seven items, same ids, same `check[]`

**esh-int-q1** — $\sqrt{64}$, $\sqrt{40}$, $\frac{22}{7}$, $0.1\overline{6}$-аас
аль нь иррационал вэ?
> $\sqrt{40} = 2\sqrt{10}$ — цорын ганц иррационал нь. $\sqrt{64} = 8$, үлдсэн
> хоёр нь хэлбэрээрээ бутархай ($0.1\overline{6} = \frac{1}{6}$).

**esh-int-q2** — $]-4, 9]$ завсарт хэдэн бүхэл тоо байна вэ?
> $-3$-аас $9$ хүртэл: $9 - (-3) + 1 = 13$.

**esh-int-q3** — $]-\infty, 4[ \cap [-1, \infty[$-г олоорой.
> Хожуу эхлэл $-1$ (хаалттай), эрт төгсгөл $4$ (нээлттэй): $[-1, 4[$.

**esh-int-q4** — $|x - 2| \le 7$-г завсрын бичиглэлээр бодоорой.
> $[2 - 7, 2 + 7] = [-5, 9]$.

**esh-int-q5** — $|x + 3| > 1$-г завсрын бичиглэлээр бодоорой.
> Төв $-3$, радиус $1$, гадна тал: $]-\infty, -4[ \cup ]-2, \infty[$.

**esh-int-q6** — $[-9, 1]$-г $|x - a| \le r$ хэлбэрт бичээрэй.
> Төв $\frac{-9 + 1}{2} = -4$, радиус $\frac{1 - (-9)}{2} = 5$:
> $|x + 4| \le 5$.

**esh-int-q7** — $|x| < 6$-г хангаж, харин $|x| < 2$-г хангахгүй бүхэл тоо хэд
вэ?
> $|x| < 6$: $-5$-аас $5$ хүртэл арван нэгэн бүхэл тоо. $|x| < 2$-ынхыг
> ($-1, 0, 1$) хасна: $11 - 3 = 8$.

---

## Notes for Build

- **`check[]`: no additions required.** Every number the rewritten solutions
  quote is already asserted in the English arrays. I checked the places where
  the rewrite spells out a step the English left implicit — `p3` and `q3` name
  the max/min endpoints, which `l3-we1`'s pattern already covers within their
  own items — and none introduces an unasserted value.
- **`\varnothing` → `\emptyset`** in lesson 3 (`t2` solution and the recap), per
  the convention. That is the only notation conversion this topic needs; it uses
  no complements, so the overline rule does not bite here.
- **Lesson 2 introduces `]a, b[` in prose and in fact 2.** It is new notation
  relative to the English source and deliberate — see the bracket finding at the
  top. The lessons still *write* in the standard convention; the reversed form
  is taught as something to read, not adopted as the house style.
- The four blackboard-bold set symbols stay Latin: `\mathbb{N}`, `\mathbb{Z}`,
  `\mathbb{Q}`, `\mathbb{R}`.
- No Cyrillic inside `$...$`; `$\text{ба} \to \cap$` and
  `$\text{аравтын бутархай төгсөх эсвэл давтагдах}$` wrap theirs in `\text{}`.
- The `$\|x - a\|$` forms in the step tables are escaped for the markdown tables
  only; the JSON carries single pipes.

## Notes for Khas

1. **The bracket convention is the decision on this topic** and it is bigger
   than one lesson — see the section near the top. I have taught both and kept
   writing in the standard one. Switching the ЭШ hub to write in `]a, b[`
   throughout would touch every inequality and calculus topic, so I did not do
   it on my own judgement the way I did the complement.
2. **«битүү завсар» / «нээлттэй завсар»** for *closed* / *open interval* have
   **0 hits** in both the ЭШ bank and А/492 — the bank writes the brackets and
   never names the kinds. I have avoided the pair entirely and said
   «төгсгөлийг оруулна / оруулахгүй» instead, which costs a few words but
   invents nothing. If you want the named forms, they are yours to give.
3. **«туяа»** appears twice as a step title for a ray to infinity. «Цацраг» is
   the geometry word but has 0 hits in the bank, and neither is settled. Low
   stakes — it is only in titles — but it is mine.
4. Your absolute-value ruling is applied exactly as given: «модул» for the bars,
   «абсолют утга» for the value, and lesson 4 names both plus «модулт
   тэгшитгэл». The one addition is that I mention the bank's «абсолют хэмжээ»
   as a variant a student will meet; say the word if you would rather the
   lessons show only one.
5. **The matryoshka image** in lesson 1 is the English author's and I kept it.
   It is Russian rather than Mongolian, but it is universally recognised here
   and I could not find a Mongolian nesting object that reads as clearly. Worth
   one look from you.
