# Draft — `algebra-2/radicals-and-rational-exponents`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**ЭШ Algebra unit 7 of 8.** One unit left in the block
(`algebra-2/systems-and-nonlinear-models`) and then *Тэгшитгэл, тэнцэтгэл биш*
closes as the fifth complete ЭШ topic. Four lessons, 30 items, 46 interactive
steps, **no nested tryItSet problems** — same thin-interactive shape as
`algebra-2/exponentials-and-logarithms`, whose `worked`/`tryIt` steps also carry
only a `problemId`.

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. Written to `docs/mn-voice-reference.md` from the first
line: no em-dash parentheticals (§9), decimal comma in prose (§7), hyphenated
case suffixes (§8), condition before thing (§1). No English objective in this
topic carries `$...$`, so none of the Mongolian ones do (review pile 6d).

**Shipped-mirror check** (first step per `README.md`): no slug overlap, **but
the conceptual overlap is the heaviest of any algebra draft so far**, and it is
with live Mongolian rather than with another draft.

| this topic | shipped mirror |
|---|---|
| L1 Rational Exponents | `8-mn/exponents-and-scientific-notation` L1–L3 (the exponent laws this lesson extends to fractions) |
| L2 Simplifying Radicals & Operations | `8-mn/roots` L5 `simplifying-square-roots`, verbatim method |
| L2, L3 (cube roots, odd index) | `8-mn/roots` L2 `cube-roots` |
| L3 Radical Equations | `8-mn/roots` L4 `solving-root-equations`, the $x^2 = k$ ancestor |

So review pile 2g governs four of this topic's core words, and **it overrides
the grounding pass on all four** — see Notes 1. This is the first draft where
2g decided more terms than the ministry did.

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| rational exponent | **рационал илтгэгч** | **ministry 4** — 10.1а/10.2а, verbatim |
| power, exponent | **зэрэг**, **илтгэгч** | ministry 9 / 6 |
| index (of a radical) | **индекс** | **shipped mirror 7** — 2g, Notes 1 |
| cube root | **куб язгуур** | **shipped mirror** — *not* «кубын язгуур», Notes 1 |
| perfect square | **гүйцэд квадрат** | **shipped mirror 30** — *not* «бүрэн квадрат», Notes 1 |
| perfect cube | **гүйцэд куб** | **shipped mirror 4** — 2g |
| to simplify | **хялбарчлах** | **ministry 2, verbatim** (10.2а) · shipped mirror 4 · exam 24 |
| radicand | **язгуурын доорх илэрхийлэл** | compositional; 0 as a phrase |
| like radicals | **ижил язгуурт гишүүд** | **ungrounded** — Notes 2 |
| to rationalize the denominator | **хуваарийг иррационалаас чөлөөлөх** | **ЭШ papers, verbatim question stem** — Notes 3 |
| conjugate | **хосмог** | **ministry 3** (complex conjugate) — Notes 4 |
| radical equation | **язгуурт тэгшитгэл** | exam adjectival «Квадрат язгуурт функц» 12 |
| extraneous solution | **хуурамч шийд** | **ungrounded**; settled in `10/rational-expressions`, review pile 4k — Notes 5 |
| inverse function | **урвуу функц** | **ministry 3** (11.3е) · exam 10 |
| one-to-one | **харилцан нэг утгатай** | **ministry 3, verbatim** — **correcting a previous draft**, Notes 6 |
| composition of functions | **давхар функц** | **ministry 1** (11.3д) |
| domain | **тодорхойлогдох муж** | ministry 2 · **exam 25** |
| range | **утгын муж** | **exam 31** vs ministry «дүр» 2 — Notes 7, review pile 4j |
| horizontal line test | **хэвтээ шулууны шалгуур** | compositional; «хэвтээ шулуун» shipped mirror 5 |
| symmetric about the line y = x | **y = x шулууны хувьд тэгш хэмтэй** | **ministry 11.3е**, phrase shape verbatim — Notes 8 |

---

## Topic-level strings

**TITLE:** Язгуур ба рационал илтгэгч

**BLURB:** Бутархай зэрэг нь язгуурын өөр нэр болох нь, язгуурт үйлдлийг
айлгүй гүйцэтгэх арга, хуурамч шийд үйлдвэрлэдэг тэгшитгэлүүд, мөн урвуу функц
буюу дараагийн бүлэгт логарифмын ордог хаалга.

---

## Lesson 1 — Рационал илтгэгч (`rational-exponents`)

**concreteComparison**

8-ыг $\frac{1}{3}$ зэрэгт дэвшүүлнэ гэдэг юу гэсэн үг вэ? 8-ыг өөрөөр нь
гуравны нэг удаа үржүүлэх боломжгүй. Гэвч зэргийн ХУУЛИУД санал нэгтэй
саналаа өгнө: тэр нь юу ч байлаа гэсэн кубдахад 8 гарах ёстой. Тэгэхээр энэ
бол куб язгуур юм, өөрөөр хэлбэл бутархай зэрэг бол өөрийгөө нуусан язгуур.

**objective**

Язгуур ба зэргийн бичлэгийн хооронд хөрвүүлэх, рационал зэргийн утгыг олох,
мөн зэргийн хуулиудаар хялбарчлах.

**concept**

1. $a^{1/n} = \sqrt[n]{a}$ гэж тодорхойлно, учир нь
   $(a^{1/n})^n = a^{n/n} = a$ гэсэн хууль өөр сонголт үлдээхгүй. Дээр нь
   зэрэг нэмбэл $a^{m/n} = (\sqrt[n]{a})^m$: хуваарь нь язгуур, хүртвэр нь
   зэрэг. $8^{2/3} = (\sqrt[3]{8})^2 = 2^2 = 4$.

2. Эхлээд язгуурыг авах нь бараг үргэлж хөнгөн: $27^{4/3}$-ыг
   $(\sqrt[3]{27})^4 = 3^4 = 81$ гэж бодох нь эхлээд $27^4 = 531441$-ийг
   бодохоос хавьгүй амар. Сөрөг илтгэгч урвуу тоо гэсэн утгаа хадгална:
   $16^{-3/4} = \frac{1}{(\sqrt[4]{16})^3} = \frac{1}{8}$.

3. Зэргийн БҮХ хууль амьд үлдэнэ: $x^{1/2} \cdot x^{1/3} = x^{5/6}$,
   $(x^{2/3})^{3/4} = x^{1/2}$. Язгуур ба зэрэг нэг бичлэгтэй болсон нь нэг
   дүрмийн ном үлдээнэ, тодорхойлолтын гол учир нь энэ.

**keyIdea**

a-ийн m/n зэрэг нь a-ийн n дэх язгуурын m зэрэг: хуваарь язгуурлаж, хүртвэр
зэрэгт дэвшүүлнэ, тоог жижиг байхад нь язгуурлаарай, мөн зэргийн хууль бүр
хэвээрээ ажиллана.

**facts**

| title | latex | explanation |
|---|---|---|
| Толь бичиг | `a^{m/n} = \left(\sqrt[n]{a}\right)^m` | Бутархайн доод тал нь язгуурын индекс, дээд тал нь энгийн зэрэг. |
| Хууль хэвээрээ | `x^{p} x^{q} = x^{p+q}, \quad (x^p)^q = x^{pq}` | Бутархай илтгэгч ч мөн адил нэмэгдэж, үржигдэнэ. |

**workedExamples**

- `a251-we1` — **statement:** $8^{2/3}$, $16^{-3/4}$, $25^{3/2}$-ын утгыг
  олоорой.
  **solution:** $8^{2/3} = (\sqrt[3]{8})^2 = 4$.
  $16^{-3/4} = \frac{1}{(\sqrt[4]{16})^3} = \frac{1}{2^3} = \frac{1}{8}$.
  $25^{3/2} = (\sqrt{25})^3 = 125$.
- `a251-we2` — **statement:** $x > 0$ үед $x^{1/2} \cdot x^{1/3}$ болон
  $\left(x^{2/3}\right)^{3/4} \cdot x^{-1/6}$-ийг хялбарчлаарай.
  **solution:** Нэмнэ: $x^{1/2 + 1/3} = x^{5/6}$. Эхлээд үржүүлээд дараа нь
  нэмнэ: $x^{1/2} \cdot x^{-1/6} = x^{1/2 - 1/6} = x^{1/3}$.

**commonMistakes**

- **text:** $a^{m/n}$-ийг доогуур нь уншиж, $8^{2/3}$-ыг $8^3$-ын квадрат
  язгуур гэж бодох.
  **correction:** Язгуурын индекс бол ХУВААРЬ: $8^{2/3}$ нь куб язгуур,
  дараа нь квадрат, өөрөөр хэлбэл 4. Тогтоох арга: язгуур нь модныхтой адил
  доороо байна.
- **text:** $16^{-3/4}$ дахь сөрөг тэмдгийг хариуг сөрөг болгоно гэж ойлгох.
  **correction:** Сөрөг илтгэгч нь зөвхөн урвуу тоо гэсэн үг:
  $\frac{1}{16^{3/4}} = \frac{1}{8}$, эерэг байна. Эерэг суурьтай үед
  ИЛТГЭГЧИЙН тэмдэг ба ХАРИУН тэмдэг хоёр хоорондоо огт хамаагүй.

**tryIt**

- `a251-t1` — $27^{2/3}$, $81^{3/4}$, $4^{-5/2}$-ын утгыг олоорой.
  **solution:** $(\sqrt[3]{27})^2 = 9$; $(\sqrt[4]{81})^3 = 27$;
  $\frac{1}{(\sqrt{4})^5} = \frac{1}{32}$.
- `a251-t2` — $x > 0$ үед $\sqrt[3]{x^2} \cdot \sqrt{x}$-ийг $x$-ийн нэг зэрэг
  болгож бичээрэй.
  **solution:** $x^{2/3} \cdot x^{1/2} = x^{2/3 + 1/2} = x^{7/6}$.

### Interactive — same twelve steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Дээр нь бутархай<br>**body** Илтгэгч тоолохоос эхэлсэн: $2^3$ гэдэг нь гурван 2-ыг үржүүлнэ гэсэн үг. Дараа нь тэг ба сөрөг тоо өргөтгөл шаардсан ($2^0 = 1$, $2^{-1} = \frac{1}{2}$), тэгэхдээ ХУУЛИУД хэвээрээ ажиллахаар сонгосон. Нэг л хил үлдлээ: бутархай. Стратеги нь ижил, $8^{1/3}$ юу байх ёстойг хуулиудаар шийдүүлээрэй. |
| 1 | exponentBuilder | **eyebrow** Дасгал · **title** Тооллын зураг<br>**teach** Бүхэл илтгэгч буюу танил машин: суурь ба тоолол. $2^4$ задарч $2 \cdot 2 \cdot 2 \cdot 2 = 16$ болохыг ажиглаарай. Өргөтгөл бүр буюу тэг, сөрөг, мөн өнөөдрийн бутархай нь ЭНЭ машины хуулиуд хэзээ ч эвдрэхгүй байхаар зохиогдсон юм.<br>**config** unchanged (`base: 2`, `exp: 4`) |
| 2 | teach | **eyebrow** Тодорхойлолт · **title** Хуулиуд шийднэ<br>**body** Зэргийн зэргийн хууль амьд үлдэх ёстой бол $(8^{1/3})^3$ нь $8^{3/3} = 8^1 = 8$-тай тэнцэх ёстой. Тэгэхээр $8^{1/3}$ бол КУБ нь 8 болдог тоо, өөрөөр хэлбэл куб язгуур буюу 2. Ерөнхийд нь: $a^{1/n} = \sqrt[n]{a}$, дээр нь зэрэг нэмбэл $a^{m/n} = (\sqrt[n]{a})^m$. Хуваарь нь язгуур, хүртвэр нь зэрэг. |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Гурван утга<br>**problemId** a251-we1 |
| 4 | tapQuestion | **eyebrow** Толь бичгээ шалгая · **title** Язгуур нь доороо<br>**prompt** $32^{3/5} = $ ?<br>**options** `$8$` · `$2$` · `$96/5$` · `$\sqrt{32^5}$ буюу асар том тоо` — **correctIndex 0**<br>**explanation** Эхлээд тав дахь язгуур: $\sqrt[5]{32} = 2$; дараа нь кубдана: $8$. Язгуур нь доороо, зэрэг нь дээрээ, мөн тоонууд эхнээсээ эцэс хүртэл жижиг байна. |
| 5 | teach | **eyebrow** Стратеги · **title** Эхлээд язгуур<br>**body** $(\sqrt[n]{a})^m$ ба $\sqrt[n]{a^m}$ хоёр тэнцүү боловч тэнцүү тааламжтай биш. $27^{4/3}$-ыг язгуураар нь эхэлбэл $3^4 = 81$. Зэргээр нь эхэлбэл $\sqrt[3]{531441}$. Тоог жижиг байхад нь язгуурлаарай, зэргийг эцэст нь үлдээгээрэй. Сөрөг илтгэгч бол зүгээр л эргүүлнэ: урвуу тоог эхэнд нь ч, эцэст нь ч авч болно. |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Бутархайтай хуулиуд<br>**problemId** a251-we2 |
| 7 | tapQuestion | **eyebrow** Хуулиудаа шалгая · **title** Илтгэгчээ нэмээрэй<br>**prompt** $x > 0$ үед $x^{3/4} \cdot x^{1/2} = $ ?<br>**options** `$x^{5/4}$` · `$x^{3/8}$` · `$x^{4/6}$` · `$x^{2}$` — **correctIndex 0**<br>**explanation** Ижил суурийг үржүүлбэл илтгэгчийг НЭМНЭ: $\frac{3}{4} + \frac{1}{2} = \frac{5}{4}$. (Илтгэгчийг үржүүлэх нь зэргийн зэргийн хууль буюу өөр нөхцөл байдал.) |
| 8 | tip | **eyebrow** Зуршил · **title** Эхлээд хөрвүүлээд дараа нь бодоорой<br>**body** Ямар ч рационал зэрэгтэй тулгарвал тоо руу гар хүрэхээсээ өмнө хөрвүүлэх мөрийг бичээрэй: $16^{3/4} = (\sqrt[4]{16})^3$. Тэр нэг харагдах мөр нь доогуур уншсан алдааг устгана, мөн хуулиудад хэрэгтэй бутархайн үйлдэл толгойд биш цаасан дээр болно. |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Гурвыг бодоорой<br>**problemId** a251-t1 |
| 10 | tryIt | **eyebrow** Туршиж үз · **title** Язгуураас зэрэг рүү<br>**problemId** a251-t2 |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** $a^{m/n} = (\sqrt[n]{a})^m$: хуваарь язгуурлаж, хүртвэр зэрэгт дэвшүүлнэ. · Эхлээд язгуурлавал тоо жижиг үлдэнэ; сөрөг илтгэгч нь урвуу тоо. · Зэргийн бүх хууль хэвээрээ, бутархай ч ердийнхөөрөө нэмэгдэж үржигдэнэ. |

---

## Lesson 2 — Язгуурыг хялбарчлах ба үйлдэл (`simplifying-radicals-and-operations`)

**concreteComparison**

$\sqrt{50}$ ба $5\sqrt{2}$ бол өөр хувцас өмссөн нэг тоо, мөн зөвхөн нэг хувцас
нь $\sqrt{50} + \sqrt{2}$ үнэндээ $6\sqrt{2}$ болохыг харуулна. Хялбаршсан
хэлбэр бол нударга биш, язгуурууд нийлдэг болох арга зам юм.

**objective**

Гүйцэд зэргийг гаргаж язгуурыг хялбарчлах, язгуурт илэрхийллийг нэмэх, хасах,
үржүүлэх, мөн хуваарийг иррационалаас чөлөөлөх.

**concept**

1. **Гаргаж хялбарчлах**: хамгийн том гүйцэд квадрат үржигдэхүүнийг хайгаарай.
   $\sqrt{50} = \sqrt{25 \cdot 2} = 5\sqrt{2}$; $\sqrt{72} = 6\sqrt{2}$. Куб
   язгуур гүйцэд кубыг гаргана:
   $\sqrt[3]{54} = \sqrt[3]{27 \cdot 2} = 3\sqrt[3]{2}$.

2. **Зөвхөн ижил язгуурт гишүүд нэмэгдэнэ**:
   $3\sqrt{2} + 5\sqrt{2} = 8\sqrt{2}$, харин $\sqrt{2} + \sqrt{3}$
   байрандаа үлдэнэ. Хялбарчлах нь ижил болохыг нь ИЛЧЛЭХ тохиолдол олон:
   $\sqrt{50} + \sqrt{18} = 5\sqrt{2} + 3\sqrt{2} = 8\sqrt{2}$.
   Үржүүлэхдээ нэг язгуур дор нийлүүлээрэй:
   $\sqrt{6} \cdot \sqrt{10} = \sqrt{60} = 2\sqrt{15}$.

3. **Хуваарийг иррационалаас чөлөөлөх**: доор язгуур үлдээхгүй. Ганц язгуур
   бол $\frac{5}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$. Язгууртай хоёр гишүүнтийг
   ХОСМОГ-оор нь үржүүлээрэй:
   $\frac{2}{3 - \sqrt{5}} = \frac{2(3 + \sqrt{5})}{9 - 5} = \frac{3 + \sqrt{5}}{2}$.
   Энэ бол 2-р бүлэгт комплекс хуваарийг цэвэрлэсэн яг тэр арга.

**keyIdea**

Хамгийн том гүйцэд зэргийг гаргаж, зөвхөн ижил язгуурт гишүүдийг нийлүүлж,
мөн хуваарийг иррационалаас чөлөөлөөрэй, хоёр гишүүнт саад болбол хосмогоор
нь үржүүлээрэй.

**facts**

| title | latex | explanation |
|---|---|---|
| Үржвэрийн дүрэм | `\sqrt{ab} = \sqrt{a}\sqrt{b} \;\; (a, b \ge 0)` | Гаргах хөдөлгүүр, гүйцэд квадратыг үржигдэхүүн болгон салгана. |
| Хосмогоор цэвэрлэх | `(3 - \sqrt{5})(3 + \sqrt{5}) = 9 - 5 = 4` | Квадратын ялгавар язгуурыг иднэ, комплекс хуваартай ижил арга. |

**workedExamples**

- `a252-we1` — **statement:** $\sqrt{50} + \sqrt{18} - \sqrt{8}$-ийг
  хялбарчлаарай.
  **solution:** Гаргая: $5\sqrt{2} + 3\sqrt{2} - 2\sqrt{2} = 6\sqrt{2}$.
  Хялбарчлаагүй үед юу ч нийлэхээргүй харагдаж байсан бол хялбарчилсны дараа
  бүгд $\sqrt{2}$ болж таарлаа.
- `a252-we2` — **statement:** $\dfrac{6}{\sqrt{12}}$ ба
  $\dfrac{4}{\sqrt{7} - \sqrt{3}}$-ын хуваарийг иррационалаас чөлөөлөөрэй.
  **solution:** Эхлээд хялбарчилъя: $\sqrt{12} = 2\sqrt{3}$ тул
  $\frac{6}{2\sqrt{3}} = \frac{3}{\sqrt{3}} = \sqrt{3}$. Хоёр дахь нь хосмог
  $\sqrt{7} + \sqrt{3}$:
  $\frac{4(\sqrt{7} + \sqrt{3})}{7 - 3} = \sqrt{7} + \sqrt{3}$.

**commonMistakes**

- **text:** Язгуур дор нэмэх: $\sqrt{9} + \sqrt{16} = \sqrt{25} = 5$.
  **correction:** $3 + 4 = 7 \ne 5$. Үржвэрийн дүрэмд нэмэхийн ихэр байхгүй:
  $\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}$. Язгуур зөвхөн үржихэд тархана,
  нэмэхэд хэзээ ч үгүй.
- **text:** Гаргахаа эрт зогсоох:
  $\sqrt{72} = \sqrt{4 \cdot 18} = 2\sqrt{18}$, болоо.
  **correction:** $18$ дотроо 9-ийг нуусан хэвээр:
  $2 \cdot 3\sqrt{2} = 6\sqrt{2}$. ХАМГИЙН ТОМ квадратыг (36) хайгаарай,
  эсвэл язгуурын доорх илэрхийлэл квадратгүй болтол нь гаргасаар байгаарай.

**tryIt**

- `a252-t1` — $\sqrt{75} + 2\sqrt{27}$ ба $\sqrt[3]{16} \cdot \sqrt[3]{4}$-ийг
  хялбарчлаарай.
  **solution:** $5\sqrt{3} + 6\sqrt{3} = 11\sqrt{3}$. Кубууд:
  $\sqrt[3]{64} = 4$.
- `a252-t2` — $\dfrac{10}{2 + \sqrt{3}}$-ын хуваарийг иррационалаас чөлөөлж,
  $(2 + \sqrt{5})(3 - \sqrt{5})$-ийг задлаарай.
  **solution:** Хосмог: $\frac{10(2 - \sqrt{3})}{4 - 3} = 20 - 10\sqrt{3}$.
  Задлая: $6 - 2\sqrt{5} + 3\sqrt{5} - 5 = 1 + \sqrt{5}$.

### Interactive — same eleven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Нэг тоо, өөр хувцас<br>**body** $\sqrt{50}$, $5\sqrt{2}$, мөн $\frac{10}{\sqrt{2}}$ бол гурван хувцас өмссөн нэг тоо. Жишиг хувцасгүй бол гишүүдээ нийлүүлж, хариугаа харьцуулж, бүр хоёр илэрхийлэл тэнцүү болохыг ч анзаарч чадахгүй. Энэ хичээл жишгийг нь тогтооно: дотроо квадрат үлдээхгүй, доороо язгуур үлдээхгүй. |
| 1 | teach | **eyebrow** Гаргах нь · **title** Гүйцэд квадрат гарч явна<br>**body** Сөрөг бус үед $\sqrt{ab} = \sqrt{a}\sqrt{b}$, тэгэхээр язгуурын доорх илэрхийллийг үржигдэхүүн болгоод гүйцэд квадратыг гаргаарай: $\sqrt{50} = \sqrt{25}\sqrt{2} = 5\sqrt{2}$. ХАМГИЙН ТОМ квадрат үржигдэхүүнийг хайгаарай, эсвэл квадратгүй болтол нь дахин дахин гаргаарай. Куб язгуур дээр мөн ижил тоглоом, зөвхөн кубтай: $\sqrt[3]{54} = 3\sqrt[3]{2}$. Анхаар: энэ дүрэм зөвхөн үржихэд хамаатай, $\sqrt{9 + 16}$ нь $7$ биш $5$. |
| 2 | worked | **eyebrow** Бодсон жишээ · **title** Нийлүүлэхийн тулд хялбарчлаарай<br>**problemId** a252-we1 |
| 3 | tapQuestion | **eyebrow** Гаргалтаа шалгая · **title** Хамгийн том квадрат гарна<br>**prompt** $\sqrt{200} = $ ?<br>**options** `$10\sqrt{2}$` · `$2\sqrt{50}$` · `$5\sqrt{8}$` · `$100\sqrt{2}$` — **correctIndex 0**<br>**explanation** $200 = 100 \cdot 2$: 10 гарч ирнэ. B ба C хувилбар квадрат гаргасан боловч хамгийн томыг нь биш, тэдгээр нь буруу тоо биш дуусгаагүй хариу юм. |
| 4 | tapQuestion | **eyebrow** Урхийг шалгая · **title** Нэмэхийн ихэр байхгүй<br>**prompt** $\sqrt{36 + 64} = $ ?<br>**options** `$10$` · `$14$` · `$6 + 8$ буюу $14$... мөн $10$ гэж үү?` · `$48$` — **correctIndex 0**<br>**explanation** Эхлээд нэмээрэй: $\sqrt{100} = 10$. $6 + 8 = 14$ болгож салгах нь хуурамч дүрэм, язгуур нэмэхэд хэзээ ч тархдаггүй. (6-8-10 талтай гурвалжин яг энэ баримт дээр амьдардаг.) |
| 5 | teach | **eyebrow** Доор нь · **title** Иррационалаас чөлөөлөх<br>**body** Жишиг: хуваарьт язгуур байж болохгүй. Ганц язгуур бол өөрөөр нь үржүүлээрэй: $\frac{5}{\sqrt{3}} \cdot \frac{\sqrt{3}}{\sqrt{3}} = \frac{5\sqrt{3}}{3}$. $3 - \sqrt{5}$ мэт хоёр гишүүнт бол **хосмог** $3 + \sqrt{5}$-оор нь үржүүлээрэй: квадратын ялгавар $9 - 5 = 4$-ийг үлдээж язгуур алга болно. Та энэ тоглолтыг өмнө нь яг ингэж гүйцэтгэсэн, 2-р бүлэгт хуваарийн $i$-г цэвэрлэсэн юм. |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Хоёр чөлөөлөлт<br>**problemId** a252-we2 |
| 7 | tip | **eyebrow** Зуршил · **title** Үйлдэл хийхээсээ өмнө хялбарчлаарай<br>**body** Даалгавар юу ч байсан буюу нэмэх, үржүүлэх, иррационалаас чөлөөлөх, эхлээд гүйцэд зэргийг гаргаарай. Язгуурын доорх илэрхийлэл жижгэрвэл тооцоо хөнгөрнө, нуугдсан ижил гишүүд гадаргуу дээр гарна, мөн хагас тохиолдолд «жинхэнэ» ажил эхлэхээс өмнө бодлого нурна ($\frac{6}{\sqrt{12}}$ хоёр алхамд $\sqrt{3}$ болсон). |
| 8 | tryIt | **eyebrow** Туршиж үз · **title** Гаргаад дараа нь нийлүүлээрэй<br>**problemId** a252-t1 |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Хосмог ажиллаж байна<br>**problemId** a252-t2 |
| 10 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** Хамгийн том гүйцэд зэргийг гаргаарай; язгуур зөвхөн үржихэд сална. · Зөвхөн ижил язгуурт гишүүд нэмэгдэнэ, тэднийг илчлэхийн тулд эхлээд хялбарчлаарай. · Иррационалаас чөлөөлөх: ганц язгуурыг өөрөөр нь, хоёр гишүүнтийг хосмогоор нь. |

---

## Lesson 3 — Язгуурт тэгшитгэл ба хуурамч шийд (`radical-equations`)

**concreteComparison**

Тэгшитгэлийн хоёр талыг квадратдах нь «ХҮЧИНГҮЙ» гэсэн ус тэмдгийг нь арилгаад
баримт бичгийг хувилахтай адил, хуулбар нь эх хувь хэзээ ч хэлээгүй зүйлийг
хэлж чадна. Язгуурт тэгшитгэл квадратдахыг албаддаг тул хариу бүрийг эх
тэгшитгэл рүү нь буцааж шалгуулах ёстой.

**objective**

Язгуурыг тусгаарлаж зэрэгт дэвшүүлэн язгуурт тэгшитгэл бодох, мөн эх
тэгшитгэлээр шалгаж хуурамч шийдийг илрүүлэх.

**concept**

1. Дараалал: язгуурыг ТУСГААРЛААД хоёр талыг тохирох зэрэгт дэвшүүлнэ.
   $\sqrt{2x + 3} = 5 \to 2x + 3 = 25 \to x = 11$. Хоёр язгууртай юу? Нэгийг
   нь тусгаарлаж квадратдаад, үлдсэнийг нь тусгаарлаж дахин квадратдаарай.

2. **Хуурамч шийд яагаад гарч ирдэг вэ**: квадратдах нь буцаагдахгүй, учир нь
   $x = 3$-аас ч, $x = -3$-аас ч квадратдахад $x^2 = 9$ гарна. Квадратдсан
   тэгшитгэл цөөн зүйл санадаг тул эх тэгшитгэлийн голж байгаа илүү «шийд»-ийг
   өөртөө багтааж чадна. Эдгээр нь **хуурамч шийд**: квадратдсан хувилбарын
   хувьд зөв, жинхэнэ тэгшитгэлийн хувьд худал.

3. $\sqrt{x + 7} = x - 5$: квадратдахад $x^2 - 11x + 18 = 0 \to x = 9$ эсвэл
   $x = 2$. 9-ийг шалгая: $\sqrt{16} = 4 = 9 - 5$ ✓. 2-ыг шалгая:
   $\sqrt{9} = 3 \ne -3$ ✗, хуурамч шийд (квадрат язгуур $-3$ гаргаж чадахгүй).
   Шийд: зөвхөн $x = 9$.

**keyIdea**

Тусгаарлаж, зэрэгт дэвшүүлж, бодоод дараа нь нэр дэвшигч бүрийг ЭХ тэгшитгэлээр
шалгаарай: квадратдах тэмдгийг мартдаг тул хуурамч шийд ховор биш харин
ердийн үзэгдэл.

**facts**

| title | latex | explanation |
|---|---|---|
| Дараалал | `\text{язгуурыг тусгаарлах} \to \text{квадратдах} \to \text{бодох} \to \text{ШАЛГАХ}` | Шалгалт бол эелдэг үйлдэл биш, заавал биелүүлэх алхам. |
| Хуурамч шийдийн эх үүсвэр | `a = b \Rightarrow a^2 = b^2, \text{ харин эсрэгээрээ үгүй}` | $(-3)^2 = 3^2$: квадратдах нь эх тэгшитгэлийн салгаж байсан тохиолдлуудыг нийлүүлнэ. |

**workedExamples**

- `a253-we1` — **statement:** $\sqrt{x + 7} = x - 5$-ийг бодоорой.
  **solution:** Квадратдая:
  $x + 7 = x^2 - 10x + 25 \to x^2 - 11x + 18 = 0 \to (x - 9)(x - 2) = 0$.
  $x = 9$-ийг шалгая: $\sqrt{16} = 4$ ба
  $9 - 5 = 4$ ✓. $x = 2$-ыг шалгая: $\sqrt{9} = 3$ харин $2 - 5 = -3$ ✗,
  хуурамч шийд. Хариу: $x = 9$.
- `a253-we2` — **statement:** $\sqrt[3]{4x - 7} = 3$-ийг бодоод, яагаад энд
  шалгалтын жүжиг гардаггүйг тайлбарлаарай.
  **solution:** Кубдая: $4x - 7 = 27 \to x = \frac{34}{4} = \frac{17}{2}$.
  Кубдах нь буцаагддаг (тоо бүр яг нэг бодит куб язгууртай бөгөөд тэмдэг нь
  хадгалагдана) тул сондгой зэрэгт тэгшитгэл хуурамч шийд үйлдвэрлэдэггүй,
  шалгалт нь зүгээр л тооцооны хяналт болно:
  $\sqrt[3]{34 - 7} = \sqrt[3]{27} = 3$ ✓.

**commonMistakes**

- **text:** Гишүүн тус бүрийг квадратдах: $\sqrt{x} + 2 = 5$-аас
  $x + 4 = 25$ гэж бичих.
  **correction:** Гишүүнийг биш ТАЛЫГ квадратдаарай:
  $(\sqrt{x} + 2)^2 = x + 4\sqrt{x} + 4$, замбараагүй болно, яг ийм учраас
  эхлээд тусгаарладаг: $\sqrt{x} = 3 \to x = 9$.
- **text:** Алгебр нь нямбай байсан гэж шалгалтыг алгасах.
  **correction:** Хуурамч шийд хайнга байдлаас биш, квадратдах үйлдэл дотроо
  агуулж байдаг. Төгс алгебр ч гэсэн тэднийг гаргана (дээрх $x = 2$).
  Шалгалт бол арга барилын нэг хэсэг.

**tryIt**

- `a253-t1` — $\sqrt{3x + 1} - 4 = 0$-ийг бодоорой.
  **solution:** Тусгаарлая: $\sqrt{3x + 1} = 4 \to 3x + 1 = 16 \to x = 5$.
  Шалгая: $\sqrt{16} = 4$ ✓.
- `a253-t2` — $x = \sqrt{x + 6}$-ийг бодоорой.
  **solution:** Квадратдая:
  $x^2 = x + 6 \to (x - 3)(x + 2) = 0 \to x = 3, -2$.
  3-ыг шалгая: $\sqrt{9} = 3$ ✓. $-2$-ыг шалгая:
  $\sqrt{4} = 2 \ne -2$ ✗. Хариу: $x = 3$.

### Interactive — same eleven steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Язгуур доорх үл мэдэгдэгч<br>**body** Даралтаас гүн, тоормосны мөрнөөс хурд, уртаас дүүжингийн хэлбэлзлийн үе, физикийн томьёо хувьсагчийг квадрат язгуур дор байнга хоригдуулдаг. Түүнийг суллах гэдэг нь квадратдана гэсэн үг, мөн квадратдахад энэ хичээлийн гэрэлд гаргах харанхуй тал бий: тэр нь хэзээ ч байгаагүй шийдийг ҮҮСГЭЖ чадна. |
| 1 | teach | **eyebrow** Дараалал · **title** Тусгаарлаад дараа нь дэвшүүлээрэй<br>**body** Эхлээд язгуурыг нэг талд нь ГАНЦААРАНГ нь үлдээгээрэй, учир нь гадны гишүүд үлдсэн талыг квадратдвал хөндлөн гишүүний замбараагүй байдал үүснэ. Дараа нь хоёр талыг язгуурын индекст нь дэвшүүлээрэй: $\sqrt{\;}$-д квадрат, $\sqrt[3]{\;}$-д куб. Үлдсэн нь таны аль хэдийн эзэмшсэн олон гишүүнтийн газар нутаг.<br>**beats** Язгуурыг тусгаарлаарай (бусад бүхнийг нөгөө тал руу нь шилжүүлээрэй). · Хоёр талыг тохирох зэрэгт дэвшүүлээрэй. · Үлдсэн олон гишүүнт тэгшитгэлийг бодоорой. · Нэр дэвшигч бүрийг ЭХ тэгшитгэлээр шалгаарай. |
| 2 | worked | **eyebrow** Бодсон жишээ · **title** Нэг жинхэнэ, нэг хуурамч<br>**problemId** a253-we1 |
| 3 | teach | **eyebrow** Харанхуй тал · **title** Хуурамч шийд хаанаас ирдэг вэ<br>**body** $x = -3$-ын хоёр талыг квадратдвал $x^2 = 9$ гарна, энэ тэгшитгэл $x = +3$-ыг БАС хүлээж авна. Мэдээлэл буюу тэмдэг устсан, мөн устсан мэдээлэл нь цаашид илүү нэр дэвшигч гэсэн үг. Хуурамч шийд гэдэг бол ердөө тийм зүйл: мартамхай квадратдсан тэгшитгэлийн хүлээж авдаг, харин хурц нүдтэй эх тэгшитгэлийн голдог нэр дэвшигч. Шалгалт бол сэжиглэл биш, алдагдсан мэдээллийн бүртгэл юм. |
| 4 | tapQuestion | **eyebrow** Ойлголтоо шалгая · **title** Хуурамчийг нь олоорой<br>**prompt** $\sqrt{5 - x} = x - 3$-ийг бодоход $x = 4$ ба $x = 1$ нэр дэвшигч гарлаа. Аль нь эх тэгшитгэлээс амьд гарах вэ?<br>**options** `зөвхөн $x = 4$` · `зөвхөн $x = 1$` · `хоёул` · `аль нь ч үгүй` — **correctIndex 0**<br>**explanation** $x = 4$: $\sqrt{1} = 1 = 4 - 3$ ✓. $x = 1$: $\sqrt{4} = 2$ харин $1 - 3 = -2$ ✗, язгуурын гаралт сөрөг байж чадахгүй. Сонгодог хуурамч шийд. |
| 5 | worked | **eyebrow** Бодсон жишээ · **title** Куб язгуур: жүжиггүй<br>**problemId** a253-we2 |
| 6 | tapQuestion | **eyebrow** Ялгааг нь шалгая · **title** Куб яагаад аюулгүй вэ<br>**prompt** Сондгой индекстэй язгуурт тэгшитгэл (куб язгуур, тав дахь язгуур) хуурамч шийд гаргадаггүй, учир нь:<br>**options** `кубдах нь тэмдгийг хадгалдаг буюу буцаагддаг, мэдээлэл алдагддаггүй` · `куб язгуур үргэлж эерэг байдаг` · `тэднийг тусгаарлаж болдоггүй` · `тэд жинхэнэ тэгшитгэл биш` — **correctIndex 0**<br>**explanation** $(-2)^3 = -8 \ne 8 = 2^3$: ялгаатай оролт ялгаатай хэвээр үлдэнэ, тэгэхээр кубдах юу ч мартахгүй, юу ч үүсгэхгүй. Зөвхөн ТЭГШ зэрэг тэмдгийг нийлүүлдэг. |
| 7 | tip | **eyebrow** Зуршил · **title** Утгын мужаар урьдчилан шүүгээрэй<br>**body** $\sqrt{\text{юм}} = x - 5$-ийг бодохоосоо өмнө ажиглаарай: зүүн тал нь $\ge 0$ тул шийд бүр $x \ge 5$ байх ёстой. Үүнийг зөрчсөн нэр дэвшигч ирсэн дороо нас барна, өөрөөр хэлбэл та шалгалтын тооцоо хийхээсээ өмнө хуурамч шийдийг олчихно. 1-р бүлгийн утгын мужийн сэтгэлгээ бодох хэрэгсэл болж байна. |
| 8 | tryIt | **eyebrow** Туршиж үз · **title** Цэвэр бодолт<br>**problemId** a253-t1 |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Хуурамчийг нь барьж аваарай<br>**problemId** a253-t2 |
| 10 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** Язгуурыг тусгаарлаж, индекст нь дэвшүүлж, бодоод, ЭХ тэгшитгэлээр ШАЛГААРАЙ. · Тэгш зэрэг тэмдгийн мэдээллийг устгана → хуурамч шийд бол бүтцийн зүйл. · Сондгой язгуур буцаагддаг: хуурамч шийд гарахгүй. |

---

## Lesson 4 — Урвуу функц (`inverse-functions`)

**concreteComparison**

Аялалын апп бүрт буцаах товч байдаг: эхлэх ба очих цэгээ соливол болно. Урвуу
функц бол математикийн тэр товч юм, машиныг ухраан ажиллуулж гаралтаас оролт
руу явна. Квадратдахын буцаалт нь квадрат язгуур, мөн дараагийн бүлэгт
илтгэгчийн буцаалт нэртэй болно: логарифм.

**objective**

Урвуу функцийг алгебрын аргаар олох, давхар функцээр шалгах, шаардлагатай үед
тодорхойлогдох мужийг хязгаарлах, мөн y = x шулууны тусгалыг унших.

**concept**

1. $f^{-1}$ нь $f$-ийг буцаана: $f(2) = 7$ бол $f^{-1}(7) = 2$, өөрөөр хэлбэл
   $(a, b)$ хос бүр $(b, a)$ болж эргэнэ. Графикийн хувьд урвуу нь $f$-ийн
   $y = x$ шулууны хувьд авсан тусгал. ОЛОХ арга: $y = f(x)$ гэж бичээд,
   $x \leftrightarrow y$-г солиод, $y$-ийн хувьд бодно.

2. $f(x) = 2x + 3$: солиход $x = 2y + 3 \to y = \frac{x - 3}{2}$. **Давхар
   функцээр шалгах**: $f^{-1}(f(x)) = \frac{(2x + 3) - 3}{2} = x$ ✓, хоёр
   дараалал хоёулаа $x$-ийг буцаах ёстой.

3. Зөвхөн **харилцан нэг утгатай** функц (гаралт бүр нь ГАНЦ оролтоос гардаг,
   график нь хэвтээ шулууны шалгуурыг давдаг) цэвэр урвуутай. $f(x) = x^2$
   унана, учир нь 9 нь 3-аас ч, $-3$-аас ч ирсэн, тиймээс хязгаарлана:
   $x \ge 0$ дээр түүний урвуу нь $\sqrt{x}$. $f$ ба $f^{-1}$-ийн
   тодорхойлогдох муж ба утгын муж байраа СОЛИНО.

**keyIdea**

Урвуу нь ухраан ажиллаж байгаа машин: x ба y-г сольж дахин бодоод, f(f⁻¹(x)) =
x-ээр шалгаарай, мөн гаралт давтагдвал харилцан нэг утгатай хэсэг рүү нь
хязгаарлаарай.

**facts**

| title | latex | explanation |
|---|---|---|
| Жор | `y = f(x) \;\to\; x = f(y) \;\to\; \text{y-ийн хувьд бодох}` | Үүргийг нь сольж, дараа нь тайлаарай. |
| Шалгалт | `f(f^{-1}(x)) = x = f^{-1}(f(x))` | Хоёр давхар функц хоёулаа адилтгал байх ёстой, нэг чиглэл бол баталгаа биш. |

**workedExamples**

- `a254-we1` — **statement:** $f(x) = \dfrac{3x - 1}{2}$-ийн урвууг олж,
  давхар функцээр шалгаарай.
  **solution:** Солиё:
  $x = \frac{3y - 1}{2} \to 2x = 3y - 1 \to y = \frac{2x + 1}{3}$. Шалгая:
  $f(f^{-1}(x)) = \frac{3 \cdot \frac{2x+1}{3} - 1}{2} = \frac{2x + 1 - 1}{2} = x$ ✓.
- `a254-we2` — **statement:** $x \ge 0$ тодорхойлогдох мужтай
  $f(x) = x^2 - 4$-ийн хувьд $f^{-1}$-ийг олж, түүний тодорхойлогдох мужийг
  хэлээрэй.
  **solution:** Солиё: $x = y^2 - 4 \to y = \sqrt{x + 4}$ (эерэг язгуур,
  хязгаарлалт нь сонгосон). $f^{-1}$-ийн тодорхойлогдох муж нь $f$-ийн утгын
  муж буюу $[-4, \infty)$: $f^{-1}(x) = \sqrt{x + 4}$, $x \ge -4$. Шалгая:
  $f(2) = 0$ ба $f^{-1}(0) = 2$ ✓.

**commonMistakes**

- **text:** $f^{-1}(x)$-ийг $\frac{1}{f(x)}$ гэж унших.
  **correction:** $-1$ нь УРВУУ (буцаах) гэсэн тэмдэглэгээ болохоос урвуу тоо
  биш. $f(x) = 2x + 3$: урвуу тоо нь $\frac{1}{2x+3}$, харин урвуу функц нь
  $\frac{x-3}{2}$, тэс өөр хоёр объект.
- **text:** Ганц давхар функцээр шалгаад орхих.
  **correction:** Бүрэн оноо (мөн бүрэн үнэн) авахын тулд хоёр дарааллыг
  шалгаарай: $f(f^{-1}(x)) = x$ БА $f^{-1}(f(x)) = x$. Тодорхойлогдох муж
  хязгаарлагдсан үед энэ хоёр шалгалт үнэхээр зөрж магадгүй.

**tryIt**

- `a254-t1` — $f(x) = 5x - 7$-ийн $f^{-1}$-ийг олж, $f^{-1}(8)$-ийг
  тооцоолоорой.
  **solution:** Солиё: $x = 5y - 7 \to y = \frac{x + 7}{5}$.
  $f^{-1}(8) = 3$. Шалгалт: $f(3) = 8$ ✓.
- `a254-t2` — $g(x) = x^3 + 1$ харилцан нэг утгатай юу? Тийм бол урвууг нь
  олоорой.
  **solution:** Куб хэзээ ч гаралтаа давтдаггүй (сондгой зэрэг, чанд өсдөг):
  тийм. Солиё: $x = y^3 + 1 \to y = \sqrt[3]{x - 1}$. Шалгая: $g(2) = 9$,
  $\sqrt[3]{8} = 2$ ✓.

### Interactive — same twelve steps, same kinds, same order

| # | kind | Mongolian |
|---|---|---|
| 0 | teach | **eyebrow** Асуудал · **title** Машиныг ухраан ажиллуулах нь<br>**body** Өнөөг хүртэлх функц бүр «оролт өгвөл гаралт нь юу вэ?» гэдэгт хариулдаг. Бодит асуултууд ЭСРЭГЭЭР ирэх нь олон: үнэ нь ийм бол хэр хол явж чадах вэ? Эзэлхүүн нь ийм бол огтлолын хэмжээ хэд вэ? Урвуу функц бол урагшаа явдаг машиныг ухраан ажиллуулахаар дахин барьсан нь, мөн түүнийг барих нь цэвэр алгебр юм. |
| 1 | coordinateGrid | **eyebrow** Хараарай · **title** Хосууд y = x-ээр эргэнэ<br>**teach** Зурагдсан нь: $f(x) = 2x + 3$-ийн гурван цэг буюу $(0,3), (1,5), (2,7)$ болон тэдний эргүүлсэн ихрүүд $(3,0), (5,1), (7,2)$, эдгээр нь $f^{-1}$-д харьяалагдана. Хос бүр $y = x$ диагоналиар толидоно: оролт ба гаралтыг солино гэдэг нь ЯГ тэр шулууны хувьд тусгал авна гэсэн үг.<br>**config** unchanged (`mode: plot`, 6 points) |
| 2 | teach | **eyebrow** Жор · **title** Сольж, дахин бодоорой<br>**body** Урвуу нь оролт ба гаралтыг солидог тул алгебр нь гайхмаар шулуухан: $y = f(x)$ дотор $x$ ба $y$ үсгийг СОЛИОД, шинэ $y$-ийн хувьд бодоорой. $f(x) = 2x + 3$-ын хувьд: $x = 2y + 3 \to y = \frac{x-3}{2}$. Дараа нь давхар функцээр ШАЛГААРАЙ, нэг машиныг нөгөөдөө хийгээд $x$-ийг буцааж өгөхийг нь хоёр дарааллаар шаардаарай. |
| 3 | worked | **eyebrow** Бодсон жишээ · **title** Сольж, бодож, шалгаарай<br>**problemId** a254-we1 |
| 4 | tapQuestion | **eyebrow** Тэмдэглэгээг шалгая · **title** Урвуу тоо биш<br>**prompt** $f(4) = 10$ бол $f^{-1}(10) = $ ?<br>**options** `$4$` · `$\frac{1}{10}$` · `$\frac{1}{4}$` · `$-10$` — **correctIndex 0**<br>**explanation** Урвуу нь $(4, 10)$ хосыг эргүүлнэ: $f^{-1}$ нь 10-ыг 4 рүү буцаана. $-1$ гэдэг нь «буцаах» гэсэн үг болохоос хэзээ ч «нэгийг хуваах» гэсэн үг биш. |
| 5 | teach | **eyebrow** Бартаа · **title** Харилцан нэг утгатай эсвэл урвуугүй<br>**body** Машин зөвхөн гаралт бүр нь ГАНЦ эх сурвалжтай үед л ухарч ажиллана. $f(x) = x^2$ унана: гаралт 9 нь 3 ба $-3$ хоёулангаас гардаг тул ухрах машин алийг нь хариулахаа мэдэхгүй. Графикийн шалгуур: ХЭВТЭЭ шулуун хоёр удаа огтолбол урвуутай байх боломжийг алдана. Засвар нь мэс заслын шинжтэй: тодорхойлогдох мужийг хязгаарлаад ($x \ge 0$-ийг үлдээгээд) амьд үлдсэн хэсгийг нь урвуулаарай, яг ийм учраас $\sqrt{x}$ нь ЭЕРЭГ язгуурыг хэлдэг. |
| 6 | worked | **eyebrow** Бодсон жишээ · **title** Хязгаарлаад дараа нь урвуулаарай<br>**problemId** a254-we2 |
| 7 | tapQuestion | **eyebrow** Шалгуурыг шалгая · **title** Хэвтээ шулууны шийдвэр<br>**prompt** Аль функц урвуутай болохын өмнө тодорхойлогдох мужийн хязгаарлалт шаарддаг вэ?<br>**options** `$y = \|x\|$` · `$y = x^3$` · `$y = 2x - 5$` · `$y = \sqrt[3]{x}$` — **correctIndex 0**<br>**explanation** $\|3\| = \|-3\|$: тэгээс дээш хэвтээ шулуун V-г хоёр удаа огтолно. Нөгөө гурав нь чанд өсдөг, гаралт бүр нь ганц оролтынх. |
| 8 | tip | **eyebrow** Зуршил · **title** Тодорхойлогдох ба утгын мужийг бас сольж бичээрэй<br>**body** $f$-ийн ГАРАЛТЫН хувьд үнэн байсан бүхэн $f^{-1}$-ийн ОРОЛТЫН хувьд үнэн болно: тодорхойлогдох муж ба утгын муж байраа солино. Бодож эхлэхээсээ өмнө «$f^{-1}$-ийн тодорхойлогдох муж = $f$-ийн утгын муж» гэж бичих нь зорилтын хязгаарлалтыг урьдчилан хэлж өгнө, мөн дараагийн бүлэгт логарифм илтгэгчийн эерэг гаралтаас «зөвхөн эерэг оролт»-оо яг ингэж өвлөн авна. |
| 9 | tryIt | **eyebrow** Туршиж үз · **title** Шугаман функцийн урвуу<br>**problemId** a254-t1 |
| 10 | tryIt | **eyebrow** Туршиж үз · **title** Куб функц бүтнээрээ урвуутай<br>**problemId** a254-t2 |
| 11 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу тогтох вэ<br>**points** Урвуу: $x \leftrightarrow y$-г сольж дахин бодоорой; график нь $y = x$-ээр толидоно. · Хоёр давхар функц хоёулаа $x$-ийг буцаахыг шалгаарай. · Хэвтээ шулууны шалгуур; урвуулахын тулд тодорхойлогдох мужийг хязгаарлаарай; тодорхойлогдох ба утгын муж байраа солино. |

---

## PRACTICE

- `a25-pr-1` — $64^{2/3}$ ба $9^{-1/2}$-ын утгыг олоорой.
  **solution:** $(\sqrt[3]{64})^2 = 16$; $\frac{1}{\sqrt{9}} = \frac{1}{3}$.
- `a25-pr-2` — $\sqrt[4]{x^3}$-ийг рационал илтгэгчээр бичиж, $x>0$ үед
  $x^{3/4} \cdot x^{5/4}$-ийг хялбарчлаарай.
  **solution:** $x^{3/4}$; үржвэр: $x^{8/4} = x^2$.
- `a25-pr-3` — $\sqrt{98}$-ийг хялбарчлаарай.
  **solution:** $\sqrt{49 \cdot 2} = 7\sqrt{2}$.
- `a25-pr-4` — $\sqrt{45} + \sqrt{20}$-ийг хялбарчлаарай.
  **solution:** $3\sqrt{5} + 2\sqrt{5} = 5\sqrt{5}$.
- `a25-pr-5` — $\dfrac{8}{\sqrt{6}}$-ын хуваарийг иррационалаас чөлөөлөөрэй.
  **solution:** $\frac{8\sqrt{6}}{6} = \frac{4\sqrt{6}}{3}$.
- `a25-pr-6` — $\sqrt{2x - 5} = 3$-ийг бодоорой.
  **solution:** $2x - 5 = 9 \to x = 7$. Шалгая: $\sqrt{9} = 3$ ✓.
- `a25-pr-7` — $x = \sqrt{2x + 8}$-ийг бодож, хуурамч шийдийг нь хаяарай.
  **solution:** $x^2 - 2x - 8 = 0 \to (x-4)(x+2) = 0$. 4-ийг шалгая:
  $\sqrt{16} = 4$ ✓; $-2$: язгуур нь $2 \ne -2$ ✗. Хариу $x = 4$.
- `a25-pr-8` — $f(x) = \dfrac{x}{3} + 2$-ийн $f^{-1}$-ийг олоорой.
  **solution:** Солиё: $x = \frac{y}{3} + 2 \to y = 3(x - 2) = 3x - 6$.

---

## TEST YOURSELF

- `a25-ty-1` — $(-27)^{2/3} + 16^{3/4}$-ын утгыг олоорой.
  **solution:** $(\sqrt[3]{-27})^2 = 9$; $(\sqrt[4]{16})^3 = 8$. Нийлбэр: 17.
- `a25-ty-2` — $2\sqrt{75} - \sqrt{48} + \sqrt{12}$-ийг хялбарчлаарай.
  **solution:** $10\sqrt{3} - 4\sqrt{3} + 2\sqrt{3} = 8\sqrt{3}$.
- `a25-ty-3` — $\dfrac{6}{\sqrt{5} - \sqrt{2}}$-ын хуваарийг иррационалаас
  чөлөөлөөрэй.
  **solution:** Хосмог:
  $\frac{6(\sqrt{5} + \sqrt{2})}{5 - 2} = 2\sqrt{5} + 2\sqrt{2}$.
- `a25-ty-4` — $\sqrt{x + 10} = x - 2$-ийг бодоорой.
  **solution:**
  $x + 10 = x^2 - 4x + 4 \to x^2 - 5x - 6 = 0 \to (x-6)(x+1) = 0$.
  6-ыг шалгая: $\sqrt{16} = 4 = 6 - 2$ ✓; $-1$:
  $3 \ne -3$ ✗. Хариу $x = 6$.
- `a25-ty-5` — $\sqrt[3]{2x + 3} = -1$-ийг бодоорой.
  **solution:** Кубдая (буцаагддаг): $2x + 3 = -1 \to x = -2$. Шалгая:
  $\sqrt[3]{-1} = -1$ ✓, сондгой язгуур сөрөг тоог дуртайяа хүлээж авна.
- `a25-ty-6` — $x \ge 3$ үед $f(x) = (x - 3)^2$-ийн хувьд $f^{-1}$, түүний
  тодорхойлогдох муж, мөн $f^{-1}(25)$-ийг олоорой.
  **solution:** Солиё: $x = (y-3)^2 \to y = 3 + \sqrt{x}$ (эерэг салаа).
  Тодорхойлогдох муж: $x \ge 0$. $f^{-1}(25) = 8$; шалгалт: $f(8) = 25$ ✓.

---

## Notes for Khas

### 1. This is the first draft where the shipped mirror decided more than the ministry did

Review pile 2g says a shipped mirror's wording beats the ministry for terms
that overlap. Until now that rule has settled one or two words per draft. Here
it settles four, and three of them are words I would otherwise have got wrong:

| term | `8-mn/roots` says | what the grounding pass alone would have produced |
|---|---|---|
| perfect square | **гүйцэд квадрат** (30 uses) | «бүрэн квадрат» |
| perfect cube | **гүйцэд куб** (4) | «бүрэн куб» |
| cube root | **куб язгуур** | «кубын язгуур» |
| index | **индекс** (7) | «зэрэглэгч» or «үзүүлэлт» |

The ministry has **none** of these four: А/492 is a grade 10–12 standard and
roots are taught in grade 8, so the standard simply never says the words. The
printed dictionary's a–i range does not reach «язгуур» either. Without 2g the
grounding pass would have had nothing to stand on and would have invented four
terms that contradict live Mongolian a student read last year.

**So 2g is not an edge case, and its current phrasing understates it.** It is
written as a tie-breaker for overlapping terms. Here it is the *only* source.
If you rule on 2e/2f/2g together, this draft argues for the strong form:
*a shipped mirror is an authority, not just a tie-breaker* — ranked below the
ministry where both speak, and above everything where the ministry is silent.

### 2. «ижил язгуурт гишүүд» for *like radicals* is ungrounded

Zero hits in all three sources. The phrase is built from «ижил» + the exam's
adjectival «язгуурт» (as in «Квадрат язгуурт функц», 12 uses) + «гишүүн», which
is the standard word for a term and is already all over the algebra drafts.
It parallels «ижил төрлийн гишүүд» for *like terms* in
`algebra-1/expressions-and-operations`, so a student meets a familiar shape.
Low-risk, but it is my construction and you may prefer the like-terms phrasing
extended («ижил төрлийн язгуурт гишүүд»), which is longer but more parallel.

### 3. The best grounding in any draft so far

*Rationalize the denominator* is **«хуваарийг иррационалаас чөлөөлөх»**, and
this is not a reconstruction — the ЭШ bank contains the question

> «$\frac{\sqrt{5}}{\sqrt{2}+\sqrt{5}-\sqrt{7}}$ хуваарийг иррационалаас
> чөлөөлбөл»

as a medium-difficulty item, plus a second one whose solution uses the same
verb. That is lesson 2's third concept, asked in the exam's own words. I have
used the phrase verbatim wherever the English says *rationalize*.

One wrinkle worth your eye: the exam's *body* says «хуваарийг» (denominator)
and the matching *solution* says «Хуваагчийг» (divisor) for the same object.
«хуваарь» is the right word and is what the shipped mirrors use 155 times
against «хуваагдагч» 119 for the numerator side. I have used «хуваарь»
throughout and treated the exam's «хуваагч» as a slip in the bank, not as
evidence. **If you disagree, that is a bank correction, not a draft change.**

### 4. «хосмог» — borrowing the ministry's complex conjugate for radicals

А/492 uses **хосмог** three times, all for the *complex* conjugate (12.4г, and
«хосмогоор үржүүлэх» in 12.4и). It never discusses radical conjugates, because
that is grade 9–10 material the standard skips.

I have used it for the radical conjugate anyway, and the English source is the
reason: lesson 2 says the conjugate trick is *"the same trick that cleared
complex denominators in Unit 2"*, and the fact card makes the same point. One
word for one idea is exactly what the source is arguing. Using a different word
here would break the link the lesson is built to make.

**This does mean the word will arrive in Mongolian before the topic that
grounds it.** `algebra-2/quadratics-and-complex-numbers` is not drafted yet, so
when it is, it must use «хосмог» too — that is the only way the cross-reference
holds. Recording it here so the later draft does not re-decide.

### 5. «хуурамч шийд» lands again, exactly where 4k predicted

`10/rational-expressions` coined it and its Notes 3 said *"the cheapest moment
to rule is now: it lands again in `algebra-2/radicals-and-rational-exponents`,
which is two drafts away."* It has, and harder: this topic uses the term
**17 times** and one of its four lessons is titled with it. Nothing new to
decide — I have kept the coinage and made no attempt to hedge it with a
description, since a lesson title cannot be a description.

The ЭШ bank has no word for it at all (I searched «гадны шийд», «илүүдэл шийд»,
«хуурамч шийд» — zero each), so there is no exam wording to defer to. It stays
review pile 4k, now with the note that **two topics and a lesson title depend
on it**, which makes a late reversal a three-file edit rather than a one-file
one.

### 6. Correcting a previous draft: «харилцан нэг утгат» → «харилцан нэг утгатай»

`algebra-2-exponentials-and-logarithms.md`'s terminology table records
*one-to-one* as **«харилцан нэг утгат»**, grounded as **"ministry 3,
verbatim"**. That grounding is wrong. The ministry writes «харилцан нэг
**утгатай**» all three times, and in two of the three it is attributive, which
is the position where a clipped «-т» form would be most tempting:

> 11.3е «…харилцан нэг **утгатай** функцийг таних, мэдэх»
> 11.3е «…өгсөн функц нь харилцан нэг **утгатай** эсэхийг тодорхойлох»
> 11.3ж «…харилцан нэг **утгатай** функцийн урвууг олох»

So the ministry's own attributive form is `-тай`, and the earlier draft's form
appears nowhere in any source. I have used «харилцан нэг утгатай» here, where
the term carries lesson 4.

**This needs a one-word edit to the earlier draft** — it is still a draft,
nothing has shipped, and the two drafts are adjacent units in the same ЭШ
block, so a student would meet both spellings inside one topic. I have not
touched that file: it is in your review pile and I would rather you see the
correction than find it silently applied. Say the word and it is one line.

*What this costs:* nothing yet, and that is the point. It is the cheapest
possible version of the failure 2g exists to prevent — a term renamed across a
boundary — caught while both sides are still drafts.

### 7. Second instance of 4j: the exam and the ministry disagree about *range*

| | ministry | ЭШ papers |
|---|---|---|
| domain | «тодорхойлогдох муж» (2) | «тодорхойлогдох муж» (25) |
| range | «дүр» (2, as «тодорхойлогдох муж ба дүр») | «утгын муж» (31) |

They agree on domain and split on range. I have used **«утгын муж»**, following
the exam, which is what `algebra-2/exponentials-and-logarithms` already did.

This is the same shape as review pile 4j (ministry «алгебрын бутархай» vs exam
«рационал илэрхийлэл»), and the second one makes the pattern worth naming:
**both times the exam's word is the commoner one by an order of magnitude, and
both times the topic is an ЭШ topic.** 4j asks whether the ЭШ bank outranks
А/492 for ЭШ topics. Two instances now point the same way, and they point the
same way as 2f and 2g do (*what students actually meet beats what a document
counted*). That is four findings arguing for one rule.

I am not treating that as a ruling. But if 2e/2f/2g/4j are ruled separately
they will probably produce four compatible answers, and ruling them together
would be cheaper.

### 8. A data point that may dissolve 4g rather than add to it

Review pile 4g asks whether *reflection* is «тусгал» or «тэгш хэм». Lesson 4
needs both ideas in one sentence, so I looked again, and the shipped mirrors
appear to already distinguish them:

> `6-mn/integers`: «…тэгш хэмтэй — нэг тал нь нөгөөгийнхөө шулуунаар тусгасан
> **тусгал** юм.»

That is **тэгш хэмтэй** for the *property* (being symmetric) and **тусгал** for
the *operation and its image* (the reflection). Counts fit: «тэгш хэмтэй» is
exam 31 / shipped 11 / ministry 1; «тусгал» is exam 0 / shipped 7 / ministry 0
— they do not compete for the same slot, they occupy different ones.

The ministry's inverse-function line supports it: 11.3е says the graph is
«шулууны хувьд **тэгш хэмтэй**» — the property. So in lesson 4 I have written
*symmetric about y = x* as «y = x шулууны хувьд тэгш хэмтэй» and *the
reflection* as «тусгал», in the same lesson, with no conflict.

**If that split is right, 4g is not a conflict to rule on but a distinction to
write down**, and `GEOMETRY-TERMS.md` §3 should record it rather than listing
the two as competitors. I have not edited `GEOMETRY-TERMS.md` — thirteen
geometry drafts cite it and the change should be yours, not mine. It is the
cheapest item in the review pile if the split holds.

### 9. Decimals

This topic adds **nothing** to the review pile 2d survey. It contains no
decimal number at all, in prose or in maths: every value is an integer, a
fraction, or a radical. The 412-across-32-drafts figure stands unchanged at
**412 across 33 drafts**.

Worth one line because it is the first draft to add zero: the exact-value
discipline of a radicals topic is the same discipline 2d is asking about, and
here it costs nothing because the mathematics never produces a decimal.

**Confirmed against 2d's own command, not by eye.** I first checked with a
loose `grep -oE '[0-9][.,][0-9]'`, which reports twelve hits here and made me
think the survey might be over-counting corpus-wide. It is not. That grep is
simply the wrong tool: every one of the twelve is a coordinate pair in the
lesson-4 grid step ($(0,3), (1,5), (2,7)$ and their flips) or a ministry
objective code in the terminology table (10.1а, 11.3е, 11.3д). 2d's actual
command looks only *inside* `$...$` and only for a decimal **point**, so
comma-separated coordinates and out-of-math section codes cannot reach it.

Re-running 2d's command over all 33 drafts returns **412**, unchanged, with
this draft absent from the per-draft list. **The 412 is sound** — the caution
is only that ad-hoc decimal greps on these files are badly noisy, so the review
pile's stored command is the one to use.
