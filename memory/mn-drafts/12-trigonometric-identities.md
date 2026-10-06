# Draft — `12/trigonometric-identities`

**STATUS: DRAFT. Written by Claude. Not applied, not gated, not shipped.**

**Grade 12, not on the ЭШ spine.** The ЭШ course covers the same ground in
`trigonometry/identities-and-equations` (draft 60), whose ministry-grounded
formula names this draft reuses. First grade 12 draft.

**Six lessons, 47 items, 47 interactive steps, 18 nested tryItSet problems.**
(18 workedExamples + 12 tryIt + 10 practice + 7 testYourself; 12 worked
examples inside workedSets.)

Conventions per R9 and `memory/mn-drafts/README.md`: «та», polite imperative,
written polite-first. No em-dash parentheticals (§9), decimal comma in prose
(§7), hyphenated case suffixes (§8), condition before thing (§1). Objectives as
plain text (6d). Imperatives soft in prose that addresses the student, bare in
beats, recaps, titles, workedSet steps and fact shorthand. Fact cells follow
the English's own (bare LaTeX) form, words inside `\text{}` (6bd). English
shown once at a new term's first use (5a). `\operatorname{tg}`,
`\operatorname{ctg}` by Khas's ruling (6ak), «tg», «ctg» in plain text.
Intervals keep the English's $[0, 2\pi)$: this is a General Math course, not
the ЭШ hub (as in `11-trigonometry-and-the-unit-circle`). Case suffixes on a
degree measure follow «градус» ($75°$-ыг, $30°$-т).

**Mirror pre-check** (6q): `data/genmath/12-mn/trigonometric-identities.json`
does not exist. Draft it.

**Grade-boundary check** (2g): not new, so not in the table below.
- Grade 11 draft (`11-trigonometry-and-the-unit-circle`, the "Grade 11" this
  topic cites throughout): «нэгж тойрог», «мөч», «I мөч … IV мөч», «жишиг
  өнцөг», «яг утга», «онцгой өнцөг», «радиан», «эргэлт», «синус · косинус».
- Shipped `8-mn/linear-equations` and draft `9-equations-and-formulas`:
  «адилтгал» for an equation true for every input, the sense this topic
  teaches. Shipped mirrors also fix «зүүн тал · баруун тал» (13 uses) and
  «ерөнхий хуваарь».
- Grade 10 drafts, by the 6bg grade 9–10 column: «үржигдэхүүнд задлах»,
  «квадратын ялгавар», «орлуулга», «квадрат зэрэгт дэвшүүлэх», «хураах»
  (Khas's ruling), FOIL kept with its gloss (5b), glossed once again here.
- Grade 9: «утгын муж».
- Geometry strand: «гүйцээлт өнцөг» (GEOMETRY-TERMS, dictionary; one shipped
  grade 7 prompt says «нэмэлт өнцөг», recorded there), «гипотенуз», «тэгш хэм»
  for a reflection (Khas's ruling 4g).

**Ministry and exam**: not an ЭШ unit, but А/492 names nearly every object:
**11.7в** «Тригонометрийн үндсэн адилтгалуудыг хэрэглэх», **12.6а** «Секанс,
косеканс, котангенс функцүүд», **12.6б** «Нийлбэр, ялгаврын томьёо», «Давхар
өнцгийн томьёо», **12.6в** «адилтгал батлах», **12.6г** «орлуулга», «зэрэг
бууруулах», equations «өгсөн завсарт». The bank writes «тригонометрийн
тэгшитгэл» (3), «ерөнхий шийд» (5), `\cot` 4 and «ctg» 1, `\sec` 2.

---

## Terminology added by this topic

| English | Mongolian | grounding |
|---|---|---|
| master identity | **үндсэн адилтгал** | **ministry 11.7в** «Тригонометрийн үндсэн адилтгал» |
| Pythagorean identity | **Пифагорын адилтгал** | draft 60 · drafts 57–58 |
| secant · cosecant · cotangent | **секанс · косеканс · котангенс** | **ministry 12.6а, verbatim** |
| tan · cot · sec · csc (notation) | `\operatorname{tg}` · `\operatorname{ctg}` · `\sec` · `\operatorname{cosec}` | **Khas's ruling, 5 Oct 2026** (6ak) for tg, ctg; `\sec` ministry 12.8а; cosec: Notes 2 |
| sum formula | **нийлбэрийн томьёо** | **ministry 12.6б** · draft 60 |
| difference formula | **ялгаврын томьёо** | **ministry 12.6б** · draft 60 |
| counterexample | **эсрэг жишээ** | `geometry/reasoning-and-proof` · draft 60 |
| double-angle formula | **давхар өнцгийн томьёо** | **ministry 12.6б** · dictionary p. 128 |
| projectile range | **нислэгийн алслалт** | school physics |
| proof · prove | **баталгаа · батлах** | GEOMETRY-TERMS (corpus 11) · **ministry 12.6в** «адилтгал батлах» |
| trig equation | **тригонометрийн тэгшитгэл** | exam 3 · ministry 11.7е |
| full solution set | **ерөнхий шийд** | exam 5 · draft 60; ministry «шийдийн ерөнхий хэлбэр» (11.7е) |
| hour angle | **цагийн өнцөг** | astronomy, calque: Notes 2 |
| quadratic trig equation | **квадрат төрлийн тригонометрийн тэгшитгэл** | draft 60 «квадрат төрлийн» |
| power reduction | **зэрэг бууруулах** | **ministry 12.6г, verbatim** |

English shown once at first use (5a, Khas's ruling 5 Oct 2026): 16 terms.

---

## Topic-level strings

**TITLE:** Тригонометрийн адилтгал

**BLURB:** Пифагорын адилтгал, нийлбэрийн ба давхар өнцгийн томьёо, адилтгал батлах, тригонометрийн тэгшитгэл бодох.

---

## Lesson 1 — Пифагорын адилтгал (`the-pythagorean-identity`)

**concreteComparison**

Нэгж тойргийн цэг бүр төвөөсөө яг 1 зайд оршдог: 11-р ангийн бүх зохион байгуулалт үүн дээр тогтсон. Энэ ганц өгүүлбэрийг хоёр цэгийн хоорондох зайн томьёогоор бичвэл $\sin^2\theta + \cos^2\theta = 1$ гарч ирнэ: БҮХ өнцөгт нэг дор хэрэглэсэн Пифагорын теорем. Энэ бол үндсэн адилтгал (master identity): өнцгийн нэг тригонометрийн утгыг мэдвэл энэ тэгшитгэл үлдсэнийг нь танд өгнө.

**objective**

Нэгж тойргоос sin²θ + cos²θ = 1-ийг гаргаж, tg/sec ба ctg/cosec хэлбэрүүдийг үүсгэн, дутуу тригонометрийн утгуудыг (мөчид тохирох тэмдэгтэй нь) сэргээх.

**concept**

1. Нэгж тойрог дээр $\theta$ өнцгийн цэг бол $(\cos\theta, \sin\theta)$ бөгөөд координатын эхээс 1 зайтай. Зайн томьёогоор: $\cos^2\theta + \sin^2\theta = 1$. Энэ бол **Пифагорын адилтгал** (Pythagorean identity): бүх $\theta$-д, нэг ч тохиолдол алгасалгүй үнэн.

2. **Адилтгал** гэдэг нь бодох тэгшитгэл биш, БҮХ оролтод биелдэг тэгшитгэл. $\sin^2\theta + \cos^2\theta = 1$ бол хаана ч орлуулж болох байнгын баримт, яг $x + x = 2x$ шиг.

3. Адилтгалыг $\cos^2\theta$-д хуваавал $\operatorname{tg}^2\theta + 1 = \sec^2\theta$; оронд нь $\sin^2\theta$-д хуваавал $1 + \operatorname{ctg}^2\theta = \operatorname{cosec}^2\theta$ гарна. (Энд $\operatorname{tg}\theta = \frac{\sin\theta}{\cos\theta}$, секанс (secant) $\sec\theta = \frac{1}{\cos\theta}$, косеканс (cosecant) $\operatorname{cosec}\theta = \frac{1}{\sin\theta}$, котангенс (cotangent) $\operatorname{ctg}\theta = \frac{\cos\theta}{\sin\theta}$.) Нэг адилтгал, гурван хувцас.

4. **Утга сэргээх**: $\sin\theta = \tfrac{3}{5}$ бол $\cos^2\theta = 1 - \tfrac{9}{25} = \tfrac{16}{25}$, тиймээс $\cos\theta = \pm\tfrac{4}{5}$. Тэгшитгэл ХЭМЖЭЭГ өгнө; тэмдгийг мөч (11-р ангийн тэмдгийн зураг) сонгоно.

**keyIdea**

sin²θ + cos²θ = 1 бүх өнцөгт үнэн: нэгж тойргийн радиусыг тэгшитгэлээр бичсэн хэлбэр. Нэг мэдэгдэх тригонометрийн утгыг бусад бүх утга болгон хөрвүүлнэ, зөвхөн мөчийн тэмдэг л үлдэнэ.

**facts**

- **title** Үндсэн адилтгал · **latex** `\sin^2\theta + \cos^2\theta = 1` · **explanation** Нэгж тойргийн «радиус нь 1» гэсэн амлалтыг алгебраар бичсэн нь.
- **title** Хоёр хувцас · **latex** `\operatorname{tg}^2\theta + 1 = \sec^2\theta \qquad 1 + \operatorname{ctg}^2\theta = \operatorname{cosec}^2\theta` · **explanation** Үндсэн адилтгалыг cos²-д эсвэл sin²-д хуваа.

**workedExamples**

- `ti1-we1` — **statement:** $\theta$ нь I мөчид, $\sin\theta = \tfrac{3}{5}$ бол $\cos\theta$ ба $\operatorname{tg}\theta$-г олоорой. **solution:** $\cos^2\theta = 1 - \tfrac{9}{25} = \tfrac{16}{25}$, тиймээс $\cos\theta = \tfrac{4}{5}$ (I мөч: эерэг). Тэгвэл $\operatorname{tg}\theta = \tfrac{3/5}{4/5} = \tfrac{3}{4}$.
- `ti1-we2` — **statement:** $\theta$ нь II мөчид, $\cos\theta = -\tfrac{5}{13}$ бол $\sin\theta$-г олоорой. **solution:** $\sin^2\theta = 1 - \tfrac{25}{169} = \tfrac{144}{169}$, тиймээс $\sin\theta = \pm\tfrac{12}{13}$. II мөчид синус эерэг: $\sin\theta = \tfrac{12}{13}$.
- `ti1-we3` — **statement:** $\theta = \tfrac{\pi}{6}$ дээр адилтгалыг тоогоор шалгаарай. **solution:** $\sin\tfrac{\pi}{6} = \tfrac12$, $\cos\tfrac{\pi}{6} = \tfrac{\sqrt3}{2}$: $\tfrac14 + \tfrac34 = 1$. ✓

**commonMistakes**

- **text** $\cos\theta = \tfrac{3}{5}$-аас мөчийг шалгалгүйгээр $\sin\theta = \tfrac{4}{5}$ гэж бичих. · **correction** Адилтгал зөвхөн $\sin^2\theta = \tfrac{16}{25}$ гэдгийг, өөрөөр хэлбэл ХЭМЖЭЭГ өгнө. IV мөчид энэ синус $-\tfrac{4}{5}$. Мөчийн тэмдгээр үргэлж дуусгаарай.
- **text** $\sin^2\theta$-г $\sin(\theta^2)$ гэж ойлгох. · **correction** $\sin^2\theta$ гэдэг нь $(\sin\theta)^2$: өнцгийг биш, ГАРАЛТЫГ квадрат зэрэгт дэвшүүлнэ. Тэмдэглэгээ хуучин боловч хаа сайгүй хэрэглэгддэг.

**tryIt**

- `ti1-t1` — **statement:** $\theta$ нь I мөчид, $\sin\theta = \tfrac{8}{17}$ бол $\cos\theta$-г олоорой. **solution:** $\cos^2\theta = 1 - \tfrac{64}{289} = \tfrac{225}{289}$: $\cos\theta = \tfrac{15}{17}$.
- `ti1-t2` — **statement:** $1 - \cos^2\theta$ илэрхийллийг хялбарчлаарай. **solution:** $\sin^2\theta$: адилтгалыг хувиргаж бичсэн хэлбэр.

### Interactive — 9 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Нэг тойрог, нэг хууль · **title** Бүх өнцгийн Пифагор<br>**beats** 11-р анги өнцөг бүрийг төвөөс нэг нэгжийн зайд, $(\cos\theta, \sin\theta)$ цэгт байрлуулсан. · Эхээс 1 зай, квадрат зэрэгт дэвшүүлбэл: $\cos^2\theta + \sin^2\theta = 1$. · Бодох тэгшитгэл биш: ҮРГЭЛЖ үнэн баримт. · «Адилтгал» гэдэг үг яг үүнийг хэлнэ. Энэ адилтгал бүлгийг бүхэлд нь удирдана. |
| 1 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Туршиж үз<br>**prompt** $\theta = \tfrac{\pi}{3}$ үед $\sin^2 + \cos^2$ = …<br>**explanation** $(\tfrac{\sqrt3}{2})^2 + (\tfrac12)^2 = \tfrac34 + \tfrac14 = 1$. Таны сонгосон ямар ч өнцөг 1 дээр буух болно: адилтгал гэдэг нь энэ.<br>**options** `$1$, бусад бүх өнцгийнх шиг` · `$\tfrac{3}{4}$` · `тооны машинаас хамаарна` — **correctIndex 0** |
| 2 | teach | **eyebrow** Хувцаснууд · **title** Хуваа, ял<br>**beats** $\sin^2 + \cos^2 = 1$ адилтгалыг $\cos^2\theta$-д хуваавал: · $\operatorname{tg}^2\theta + 1 = \sec^2\theta$. · Оронд нь $\sin^2\theta$-д хуваавал: $1 + \operatorname{ctg}^2\theta = \operatorname{cosec}^2\theta$. · Нэгийг цээжлэх үнээр гурван адилтгал. |
| 3 | teach | **eyebrow** Сэргээх нүүдэл · **title** Нэг утга үлдсэнийг нь худалдаж авна<br>**beats** $\sin\theta = \tfrac{3}{5}$ гэдгийг мэдэх үү? Тэгвэл $\cos^2\theta = \tfrac{16}{25}$. · Тиймээс $\cos\theta = \pm\tfrac{4}{5}$: адилтгал ХЭМЖЭЭГ өгнө. · Мөч ТЭМДГИЙГ өгнө: II мөч бол косинус сөрөг. · Хэмжээг адилтгалаас, тэмдгийг мөчөөс. Үргэлж. |
| 4 | tapQuestion | **eyebrow** Тэмдгийн үүрэг · **title** III мөч<br>**prompt** $\sin\theta = -\tfrac{3}{5}$, $\theta$ нь III мөчид. Тэгвэл $\cos\theta$ = …<br>**explanation** Хэмжээ: $\sqrt{1 - \tfrac{9}{25}} = \tfrac45$. III мөчид координат ХОЁУЛАА сөрөг, тиймээс $\cos\theta = -\tfrac45$.<br>**options** `$-\tfrac{4}{5}$` · `$\tfrac{4}{5}$` · `$\pm\tfrac{4}{5}$: хэлэх боломжгүй` — **correctIndex 0** |
| 5 | workedSet | **eyebrow** Бодсон жишээ · **title** Адилтгалын ур<br>**intro** Хэмжээг адилтгалаас, тэмдгийг мөчөөс аваарай.<br>**ex1** $\cos\theta = \tfrac{7}{25}$, $\theta$ нь IV мөчид. $\sin\theta$ ба $\operatorname{tg}\theta$-г олоорой. · алхам: $\sin^2\theta = 1 - \tfrac{49}{625} = \tfrac{576}{625}$. · алхам: IV мөч: синус сөрөг, $\sin\theta = -\tfrac{24}{25}$. · алхам: $\operatorname{tg}\theta = \tfrac{-24/25}{7/25} = -\tfrac{24}{7}$. · **хариу** $\sin\theta = -\tfrac{24}{25}$, $\operatorname{tg}\theta = -\tfrac{24}{7}$<br>**ex2** $\dfrac{\sin^2\theta}{1 - \sin^2\theta}$ илэрхийллийг хялбарчлаарай. · алхам: Хуваарь бол далдлагдсан адилтгал: $1 - \sin^2\theta = \cos^2\theta$. · алхам: $\tfrac{\sin^2\theta}{\cos^2\theta} = \operatorname{tg}^2\theta$. · **хариу** $\operatorname{tg}^2\theta$ |
| 6 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Сэргээж, хялбарчлах<br>**intro** Мөчийн тэмдгийг анхааралтай ажиглаарай.<br>**p1** $\sin\theta = \tfrac{5}{13}$, II мөч. $\cos\theta$ = … — **choices** `$-\tfrac{12}{13}$` · `$\tfrac{12}{13}$` · `$-\tfrac{8}{13}$` — **answerIndex 0** — Хэмжээ $\tfrac{12}{13}$ адилтгалаас гарна; II мөч косинусыг сөрөг болгоно.<br>**p2** $\sec^2\theta - \operatorname{tg}^2\theta$ илэрхийллийг хялбарчлаарай. — **choices** `$1$` · `$\sin^2\theta$` · `$\cos^2\theta$` — **answerIndex 0** — $\operatorname{tg}^2 + 1 = \sec^2$ адилтгалыг хувиргавал ялгавар нь яг 1.<br>**p3** $(\sin\theta + \cos\theta)^2$ илэрхийллийг задлахад… — **choices** `$1 + 2\sin\theta\cos\theta$` · `$1$` · `$\sin^2\theta + \cos^2\theta$` — **answerIndex 0** — FOIL (эхний, гадна, дотор, сүүлийн гишүүдийн үржвэр) $\sin^2 + 2\sin\cos + \cos^2$ нийлбэрийг өгнө; квадратууд адилтгалаар 1 болж нурна. |
| 7 | funFact | **eyebrow** Сонирхолтой баримт · **title** Нэг адилтгал, бараг дөрвөн мянган жил<br>**body** Пифагорын теорем бол Хүрэл зэвсгийн үеийн математик: Пифагороос мянга гаруй жилийн өмнөх Вавилоны шавар хавтан дээр (МЭӨ 1800 оны орчмын «Плимптон 322») бүхэл тоон талтай тэгш өнцөгт гурвалжнуудын жагсаалт гэж ихэвчлэн тайлбарладаг тоонууд бий. Теоремыг 1 радиустай тойрогт ороовол $\sin^2 + \cos^2 = 1$ болно: GPS-ийн байршил тогтоолт, дууны шүүлтүүр, видео тоглоомын эргүүлэлт зэрэг олон тооцооны дотор ажилладаг адилтгал. Хамгийн эртний теорем, хамгийн завгүй хувцас. |
| 8 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу сурснаа эргэн харъя<br>**points** $\sin^2\theta + \cos^2\theta = 1$: нэгж тойргийн радиусыг алгебраар бичсэн нь. · Үүнийг $\cos^2\theta$ эсвэл $\sin^2\theta$-д хувааж tg/sec ба ctg/cosec хэлбэрүүдийг гарга. · Адилтгал дутуу утгын хэмжээг, мөч тэмдгийг нь өгнө. |

---

## Lesson 2 — Нийлбэр ба ялгаврын томьёо (`sum-and-difference-formulas`)

**concreteComparison**

Нэгж тойрог 30-45-60 гэр бүлийн утгуудыг яг бичдэг. Харин $75°$? Хүснэгтэд алга. Гэтэл $75 = 45 + 30$ бөгөөд **нийлбэрийн томьёо** (sum formulas) хуучин яг утгуудаас шинийг бүтээнэ, яг л та мэдэгдэх хэсгүүдээс $\sqrt{50} = 5\sqrt2$-ыг бүтээсэн шиг. Олон тооны машин sin товчийг дарах бүрт дотроо энэ бүжгийг хийдэг.

**objective**

sin(A±B) ба cos(A±B) томьёогоор онцгой биш өнцгүүдийн яг утгыг бодож, илэрхийллийг хувиргаж бичих.

**concept**

1. **Нийлбэрийн синус**: $\sin(A+B) = \sin A\cos B + \cos A\sin B$. Синус холино: sin·cos + cos·sin, дундах тэмдэг нь зүүн талын тэмдэгтэй ТААРНА.

2. **Нийлбэрийн косинус**: $\cos(A+B) = \cos A\cos B - \sin A\sin B$. Косинус төрлөө хадгална: cos·cos ба sin·sin, харин дундах тэмдэг ЭРГЭНЭ: зүүн талын нэмэх баруун талд хасах болно.

3. Ялгаврын томьёо (difference formulas): дундах тэмдэг бүрийг эргүүлээрэй. $\sin(A-B) = \sin A\cos B - \cos A\sin B$ ба $\cos(A-B) = \cos A\cos B + \sin A\sin B$.

4. **Анхааруулга**: $\sin(A+B) \neq \sin A + \sin B$. Туршаад үзээрэй: $\sin 90° = 1$, харин $\sin 45° + \sin 45° = \sqrt2 \approx 1.41$. Синус бол хаалт задалж болох үржвэр биш: эдгээр томьёо ЯГ ТИЙМЭЭС бий.

**keyIdea**

sin(A±B) = sinAcosB ± cosAsinB; cos(A±B) = cosAcosB ∓ sinAsinB. Синус холиод тэмдгээ хадгална; косинус төрлөө тааруулаад тэмдгээ эргүүлнэ.

**facts**

- **title** Нийлбэрийн синус · **latex** `\sin(A \pm B) = \sin A\cos B \pm \cos A\sin B` · **explanation** Холимог үржвэрүүд; дундах тэмдэг таарна.
- **title** Нийлбэрийн косинус · **latex** `\cos(A \pm B) = \cos A\cos B \mp \sin A\sin B` · **explanation** Ижил төрлийн үржвэрүүд; дундах тэмдэг эргэнэ.

**workedExamples**

- `ti2-we1` — **statement:** $\sin 75°$-ыг яг бодоорой. **solution:** $75 = 45 + 30$: $\sin 75° = \sin 45°\cos 30° + \cos 45°\sin 30° = \tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt3}{2} + \tfrac{\sqrt2}{2}\cdot\tfrac12 = \tfrac{\sqrt6 + \sqrt2}{4}$.
- `ti2-we2` — **statement:** $\cos 15°$-ыг яг бодоорой. **solution:** $15 = 45 - 30$: $\cos 15° = \cos 45°\cos 30° + \sin 45°\sin 30° = \tfrac{\sqrt6 + \sqrt2}{4}$. ($\sin 75°$-тай ижил утга: гүйцээлт хоёр өнцгийн нэгнийх нь синус нөгөөгийнх нь косинустай тэнцүү.)
- `ti2-we3` — **statement:** $\sin\theta\cos\tfrac{\pi}{3} + \cos\theta\sin\tfrac{\pi}{3}$ илэрхийллийг хялбарчлаарай. **solution:** Энэ бол урвуугаар уншсан нийлбэрийн синусын хэв: $\sin(\theta + \tfrac{\pi}{3})$.

**commonMistakes**

- **text** Хаалт задлах мэт тараах: $\sin(A+B) = \sin A + \sin B$. · **correction** Синус бол үржүүлэх үйлдэл биш, функц. $\sin 90° = 1 \neq \sin 45° + \sin 45° \approx 1.41$. Томьёог хэрэглээрэй.
- **text** Косинус дундах тэмдгийг эргүүлдгийг мартах. · **correction** $\cos(A+B)$ ХАСАХ тэмдэгтэй: $\cos A\cos B - \sin A\sin B$. Санах арга: косинус бол үргэлж эсрэгээр хийдэг зөрүүд.

**tryIt**

- `ti2-t1` — **statement:** $\sin 15°$-ыг яг бодоорой. **solution:** $15 = 45 - 30$: $\tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt3}{2} - \tfrac{\sqrt2}{2}\cdot\tfrac12 = \tfrac{\sqrt6 - \sqrt2}{4}$.
- `ti2-t2` — **statement:** $\cos 80°\cos 20° + \sin 80°\sin 20°$ илэрхийллийг хялбарчлаарай. **solution:** Урвуугаар уншсан ялгаврын косинус: $\cos(80° - 20°) = \cos 60° = \tfrac12$.

### Interactive — 8 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Хүснэгтээс гадна · **title** 75°-ыг бүтээх<br>**beats** Нэгж тойрог 30, 45, 60-ыг бичдэг, харин 75-ыг биш. · Гэтэл $75 = 45 + 30$. Мэдэгдэх утгуудыг хослуулж болох уу? · Синусуудыг нэмээд болохгүй: $\sin 90° = 1 \neq \sin 45° + \sin 45°$. · Жинхэнэ хэрэгсэл хэрэгтэй. Нийлбэрийн томьёо тайзнаа гарна. |
| 1 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Хаалт задлахгүй<br>**prompt** $\sin(A + B)$ нь $\sin A + \sin B$-тэй тэнцүү…<br>**explanation** $\sin 90° = 1$, харин $\sin 45° + \sin 45° = \sqrt2$. Ганц эсрэг жишээ (counterexample) адилтгал болох гэж буй тэгшитгэлийг унагана.<br>**options** `хэзээ ч итгэж болохгүй: $45° + 45°$ дээр туршаад үз` · `үргэлж` · `зөвхөн хурц өнцгүүдэд` — **correctIndex 0** |
| 2 | teach | **eyebrow** Томьёонууд · **title** Холих ба тааруулах<br>**beats** $\sin(A+B) = \sin A\cos B + \cos A\sin B$: холимог хос, тэмдэг таарна. · $\cos(A+B) = \cos A\cos B - \sin A\sin B$: ижил төрлийн хос, тэмдэг ЭРГЭНЭ. · Ялгаврууд: дундах тэмдэг бүрийг эргүүл. · Синус холино; косинус зөрүүд. Цээжлэх ачаа ердөө л энэ. |
| 3 | workedSet | **eyebrow** Бодсон жишээ · **title** Хуучнаас шинэ утга<br>**intro** Өнцгийг хүснэгтийн өнцгүүдэд хуваагаарай.<br>**ex1** $\sin 75°$-ыг яг утгаар олоорой. · алхам: $75 = 45 + 30$. · алхам: $\sin 45°\cos 30° + \cos 45°\sin 30°$ · алхам: $= \tfrac{\sqrt2}{2}\cdot\tfrac{\sqrt3}{2} + \tfrac{\sqrt2}{2}\cdot\tfrac{1}{2} = \tfrac{\sqrt6 + \sqrt2}{4}$. · **хариу** $\tfrac{\sqrt6 + \sqrt2}{4}$<br>**ex2** $\cos\tfrac{7\pi}{12}$-ийн яг утгыг олоорой. ($\tfrac{7\pi}{12} = \tfrac{\pi}{3} + \tfrac{\pi}{4}$) · алхам: $\cos\tfrac{\pi}{3}\cos\tfrac{\pi}{4} - \sin\tfrac{\pi}{3}\sin\tfrac{\pi}{4}$ · алхам: $= \tfrac12\cdot\tfrac{\sqrt2}{2} - \tfrac{\sqrt3}{2}\cdot\tfrac{\sqrt2}{2}$ · алхам: $= \tfrac{\sqrt2 - \sqrt6}{4}$: II мөчийн косинусын ёсоор сөрөг. · **хариу** $\tfrac{\sqrt2 - \sqrt6}{4}$ |
| 4 | tapQuestion | **eyebrow** Урвуугаар унш · **title** Хэв таних<br>**prompt** $\sin 40°\cos 20° + \cos 40°\sin 20°$ нурвал…<br>**explanation** Энэ бол $A = 40°, B = 20°$ үеийн нийлбэрийн синусын хэв: $\sin(40° + 20°)$. Томьёог УРВУУГААР таних нь тэдний хүчний тал.<br>**options** `$\sin 60° = \tfrac{\sqrt3}{2}$` · `$\sin 20°$` · `$\cos 60°$` — **correctIndex 0** |
| 5 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Нийлбэрийн ур<br>**intro** 30/45/60-ийн хэсгүүдэд хувааж, косинусын эргүүлэлтийг анхаараарай.<br>**p1** $\cos 75°$ = … — **choices** `$\tfrac{\sqrt6 - \sqrt2}{4}$` · `$\tfrac{\sqrt6 + \sqrt2}{4}$` · `$\tfrac{\sqrt2 + \sqrt3}{4}$` — **answerIndex 0** — $\cos 45°\cos 30° - \sin 45°\sin 30° = \tfrac{\sqrt6}{4} - \tfrac{\sqrt2}{4}$.<br>**p2** $\cos 50°\cos 10° - \sin 50°\sin 10°$ = … — **choices** `$\cos 60° = \tfrac12$` · `$\cos 40°$` · `$\sin 60°$` — **answerIndex 0** — Урвуугаар уншсан нийлбэрийн косинусын хэв: $\cos(50° + 10°)$.<br>**p3** $\sin(\theta + \pi)$-г хялбарчилбал… — **choices** `$-\sin\theta$` · `$\sin\theta$` · `$\cos\theta$` — **answerIndex 0** — $\sin\theta\cos\pi + \cos\theta\sin\pi = \sin\theta(-1) + 0$. Хагас эргэлт синусын тэмдгийг эргүүлнэ: томьёо тойргийн зурагтай яг таарч байна. |
| 6 | funFact | **eyebrow** Сонирхолтой баримт · **title** Тооны машин sin 75°-ыг яаж «мэддэг» вэ<br>**body** Хүснэгтээс хардаггүй: тооцоолдог. 1950-аад оны сүүлээр зохиогдсон, олон тооны машинд ажилладаг CORDIC алгоритм цөөн хэдэн хадгалсан өнцгөөс эхэлж, тэдгээрийн нийлбэр, ялгавраар, яг энэ хуудасны томьёогоор эргэсээр таны өнцгөөс тэрбумны нэг орчим зөрүүтэй болтлоо ойртоно. Нийлбэрийн томьёо шалгалтын чимэглэл биш: жинхэнэ хөдөлгүүр. |
| 7 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу сурснаа эргэн харъя<br>**points** $\sin(A\pm B) = \sin A\cos B \pm \cos A\sin B$: холимог, тэмдэг таарна. · $\cos(A\pm B) = \cos A\cos B \mp \sin A\sin B$: ижил төрөл, тэмдэг эргэнэ. · Яг утгыг бүтээ ($75° = 45° + 30°$), урвуугаар уншсан хэвийг нураа. |

---

## Lesson 3 — Давхар өнцгийн томьёо (`double-angle-formulas`)

**concreteComparison**

Нийлбэрийн томьёонд $B = A$ гэж тавибал тэд илүү богино, илүү хурц зүйл болж нурна: $\sin 2\theta = 2\sin\theta\cos\theta$. Давхар өнцгийн томьёо (double-angle formulas) бол өөрийгөө залгисан нийлбэрийн томьёо бөгөөд хаа сайгүй гарч ирнэ. Шидсэн биеийн нислэгийн алслалт (projectile range) $R \sim \sin 2\theta$ байдаг тул $45°$-аар шидсэн нь хамгийн хол очдог; цаашдын анализын бүлэг бүрт ч мөн адил.

**objective**

sin 2θ = 2 sin θ cos θ ба cos 2θ-гийн гурван хэлбэрийг гаргаж хэрэглэн, тохиромжтой хэлбэрийг сонгох.

**concept**

1. **Синусын давхар**: $\sin(A+B)$-д $A = B = \theta$ гэж тавиарай: $\sin 2\theta = \sin\theta\cos\theta + \cos\theta\sin\theta = 2\sin\theta\cos\theta$.

2. **Косинусын давхар**: мөн тэр нүүдэл $\cos 2\theta = \cos^2\theta - \sin^2\theta$-г өгнө. Дараа нь Пифагорын адилтгал үүнийг өөр хоёр янзаар бичнэ: $2\cos^2\theta - 1$ ба $1 - 2\sin^2\theta$.

3. **Хэлбэр сонгох**: зөвхөн $\cos\theta$-г мэдэх үү? $2\cos^2\theta - 1$-ийг хэрэглээрэй. Зөвхөн $\sin\theta$-г мэдэх үү? $1 - 2\sin^2\theta$-г. Хоёуланг нь мэдэх үү? Анхныхыг. Гурван хаалга, нэг өрөө.

4. Давхарлах нь үнэгүй БИШ: $\sin 2\theta \neq 2\sin\theta$ ($\theta = 90°$ дээр туршаарай: $\sin 180° = 0$, харин $2\sin 90° = 2$). $\cos\theta$ үржигдэхүүн бол давхарлахын үнэ.

**keyIdea**

sin 2θ = 2sinθcosθ; cos 2θ = cos²θ − sin²θ = 2cos²θ − 1 = 1 − 2sin²θ. Мэдэж буй зүйлдээ тохирох хэлбэрийг сонгоорой.

**facts**

- **title** Синусын давхар · **latex** `\sin 2\theta = 2\sin\theta\cos\theta` · **explanation** Хоёр өнцөг нь тэнцүү үеийн нийлбэрийн томьёо.
- **title** Косинусын давхар, гурван хэлбэр · **latex** `\cos 2\theta = \cos^2\theta - \sin^2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta` · **explanation** Пифагорын адилтгал хувилбаруудыг үүсгэнэ.

**workedExamples**

- `ti3-we1` — **statement:** $\theta$ нь I мөчид, $\sin\theta = \tfrac{3}{5}$ бол $\sin 2\theta$-г олоорой. **solution:** $\cos\theta = \tfrac45$ (I мөч). $\sin 2\theta = 2\cdot\tfrac35\cdot\tfrac45 = \tfrac{24}{25}$.
- `ti3-we2` — **statement:** Мөн тэр $\theta$-гийн хувьд $\cos 2\theta$-г зөвхөн синустай хэлбэрээр олоорой. **solution:** $\cos 2\theta = 1 - 2\sin^2\theta = 1 - 2\cdot\tfrac{9}{25} = \tfrac{7}{25}$.
- `ti3-we3` — **statement:** $\sin 60° = 2\sin 30°\cos 30°$ гэдгийг шалгаарай. **solution:** Баруун тал: $2\cdot\tfrac12\cdot\tfrac{\sqrt3}{2} = \tfrac{\sqrt3}{2} = \sin 60°$. ✓

**commonMistakes**

- **text** Функцээр дамжуулан давхарлах: $\sin 2\theta = 2\sin\theta$. · **correction** $\theta = 90°$: $\sin 180° = 0 \neq 2$. Давхарлахын зөв үнэ бол $\cos\theta$ үржигдэхүүн: $2\sin\theta\cos\theta$.
- **text** Зөвхөн синусыг мэдэж байхдаа $\cos^2 - \sin^2$-аар зүтгэх. · **correction** Өгөгдөлдөө зориулсан хэлбэрийг хэрэглээрэй: $1 - 2\sin^2\theta$-д косинус огт хэрэггүй. Хэлбэр сонгох нь ӨӨРӨӨ ур чадвар.

**tryIt**

- `ti3-t1` — **statement:** $\cos\theta = \tfrac{5}{13}$, IV мөч. $\cos 2\theta$-г олоорой. **solution:** $2\cos^2\theta - 1 = 2\cdot\tfrac{25}{169} - 1 = -\tfrac{119}{169}$. (Синус хэрэггүй тул тэмдгийн санаа зовнил ч алга.)
- `ti3-t2` — **statement:** $\dfrac{\sin 2\theta}{\sin\theta}$-г ($\sin\theta \neq 0$ үед) хялбарчлаарай. **solution:** $\tfrac{2\sin\theta\cos\theta}{\sin\theta} = 2\cos\theta$.

### Interactive — 7 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Нуралт · **title** B нь A болно<br>**beats** Нийлбэрийн томьёо ДУРЫН хоёр өнцөгт ажиллана: ихрүүдэд ч. · $B = A$ гэж тавь: $\sin(A + A) = \sin A\cos A + \cos A\sin A$. · Хоёр ижил гишүүн: $\sin 2A = 2\sin A\cos A$. · Шинэ томьёо үнэгүй. Косинус ч мөн адил нурна. |
| 1 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Давхарлахын үнэ<br>**prompt** $\sin 2\theta = 2\sin\theta$: үнэн үү, урхи юу?<br>**explanation** $\sin 180° = 0$, харин $2\sin 90° = 2$. Давхарлах нь $\cos\theta$ үржигдэхүүнээр үнэтэй.<br>**options** `Урхи: $\theta = 90°$ үед $0 = 2$ гэж гарна` · `Бүх өнцөгт үнэн` · `$45°$-аас бага өнцөгт үнэн` — **correctIndex 0** |
| 2 | teach | **eyebrow** Косинусын гурван хаалга · **title** Нэг өрөө<br>**beats** $\cos 2\theta = \cos^2\theta - \sin^2\theta$: түүхий нуралт. · $\sin^2 = 1 - \cos^2$ гэж солибол $2\cos^2\theta - 1$ гарна. · $\cos^2 = 1 - \sin^2$ гэж солибол $1 - 2\sin^2\theta$ гарна. · Зөвхөн синус мэдэх үү? Зөвхөн косинус уу? Тус бүрд хаалга бий. |
| 3 | workedSet | **eyebrow** Бодсон жишээ · **title** Давхарлах ур<br>**intro** Өгөгдөлдөө тохирох хэлбэрийг сонгоорой.<br>**ex1** $\sin\theta = \tfrac{8}{17}$, II мөч. $\sin 2\theta$ ба $\cos 2\theta$-г олоорой. · алхам: II мөч: $\cos\theta = -\tfrac{15}{17}$. · алхам: $\sin 2\theta = 2\cdot\tfrac{8}{17}\cdot(-\tfrac{15}{17}) = -\tfrac{240}{289}$. · алхам: $\cos 2\theta = 1 - 2\cdot\tfrac{64}{289} = \tfrac{161}{289}$. · **хариу** $\sin 2\theta = -\tfrac{240}{289}$, $\cos 2\theta = \tfrac{161}{289}$<br>**ex2** $1 - 2\sin^2 15°$-ыг нэг яг утга болгон бичээрэй. · алхам: Энэ бол $\theta = 15°$ үеийн $\cos 2\theta$. · алхам: $\cos 30° = \tfrac{\sqrt3}{2}$. · **хариу** $\tfrac{\sqrt3}{2}$ |
| 4 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Давхар үүрэг<br>**intro** Урвуугаар таних нь давхар оноо авна.<br>**p1** $2\sin 75°\cos 75°$ = … — **choices** `$\sin 150° = \tfrac12$` · `$\sin 75°$-ын квадрат` · `$\cos 150°$` — **answerIndex 0** — Урвуугаар уншсан давхар өнцгийн хэв: $\sin(2 \cdot 75°)$.<br>**p2** $\cos\theta = \tfrac{3}{5}$ (дурын мөч). $\cos 2\theta$ = … — **choices** `$-\tfrac{7}{25}$` · `$\tfrac{7}{25}$` · `мөч хэрэгтэй` — **answerIndex 0** — $2\cdot\tfrac{9}{25} - 1 = -\tfrac{7}{25}$. Зөвхөн косинустай хэлбэр мөчийг хэзээ ч асуудаггүй: квадрат тэмдгийг арилгана.<br>**p3** $\cos^2 22.5° - \sin^2 22.5°$ = … — **choices** `$\tfrac{\sqrt2}{2}$` · `$\tfrac12$` · `$1$` — **answerIndex 0** — $\cos(2 \cdot 22.5°) = \cos 45°$. |
| 5 | funFact | **eyebrow** Физик · **title** Яагаад 45° хамгийн хол шиддэг вэ<br>**body** Агаарын эсэргүүцлийг тооцохгүй, тэгш газар шидсэн биеийн нислэгийн алслалт $\sin 2\theta$ буюу хоёр дахин авсан шидэлтийн өнцгийн синустай пропорционал. $\sin 2\theta$ нь $2\theta = 90°$, өөрөөр хэлбэл $\theta = 45°$ үед хамгийн их утгаа авна: тоглоомын талбайн тэр баримтын АРД байгаа томьёо. 10-р ангийн парабол нислэгийн замыг өгсөн бол давхар өнцөг онилгыг тайлбарлана. |
| 6 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу сурснаа эргэн харъя<br>**points** $\sin 2\theta = 2\sin\theta\cos\theta$: давхарлах нь косинус үржигдэхүүнээр үнэтэй. · $\cos 2\theta$ гурван хэлбэртэй; мэдэгдэх утгадаа тохирохыг нь сонго. · Хэвийг урвуугаар тань: $2\sin\alpha\cos\alpha$ нь $\sin 2\alpha$ болж нурна. |

---

## Lesson 4 — Адилтгал батлах (`proving-identities`)

**concreteComparison**

Тригонометрийн адилтгалын мэдэгдэл бол шүүх хурлын хэрэг: ЗҮҮН ТАЛ $=$ БАРУУН ТАЛ, бүх өнцөгт гэж мэдэгдсэн. Таны ажил бол баталгаа (proof): НЭГ талыг хууль ёсны алхам алхмаар дахин бичсээр нөгөөг нь болгох. Хуулийн ном жижиг (Пифагорын адилтгал, tg ба sec функцийн тодорхойлолт, нийлбэрийн ба давхар өнцгийн томьёо), харин аль хуулийг хэзээ хэрэглэхийг сонгох нь ур чадвар.

**objective**

Нэг талыг хувиргаж адилтгал батлах: синус, косинус руу шилжүүлэх, бутархай нэгтгэх, үржигдэхүүнд задлах, мэдэгдэх адилтгалыг орлуулах.

**concept**

1. **Алтан дүрэм**: НЭГ талыг нөгөөтэйгөө тэнцүү болтол хувиргаарай. Гишүүдийг тэнцүүгийн тэмдгээр бүү шилжүүлээрэй: тэгэх нь батлах гэж буй зүйлээ үнэн гэж үзсэн хэрэг. Илүү төвөгтэй талаас эхлээрэй: хялбарчлах нь төвөгтэй болгохоос амархан.

2. **1-р нүүдэл: бүгдийг sin ба cos руу шилжүүлэх**: $\operatorname{tg}\theta = \tfrac{\sin\theta}{\cos\theta}$, $\sec\theta = \tfrac{1}{\cos\theta}$, $\operatorname{cosec}\theta = \tfrac{1}{\sin\theta}$, $\operatorname{ctg}\theta = \tfrac{\cos\theta}{\sin\theta}$. Төөрсөн үед энэ нүүдэл хэзээ ч хор хийхгүй.

3. **2-р нүүдэл: алгебр ажилласаар л байна**: ерөнхий хуваарь, үржигдэхүүнд задлах, FOIL. Тригонометрийн илэрхийлэл $\sin\theta$-г хувьсагч гэж үзсэн 10-р ангийн алгебрыг дагана. $1 - \sin^2\theta$ нь $(1-\sin\theta)(1+\sin\theta)$ болж задарна.

4. **3-р нүүдэл: Пифагорын адилтгалаар солих**: $\sin^2 + \cos^2$, $1 - \sin^2$ эсвэл $1 - \cos^2$ хаана гарна, тэнд нь солиорой. Энэ бол квадратуудын хоорондох хөрвүүлэлт.

**keyIdea**

Зөвхөн нэг талыг дахин бичиж батлаарай: sin/cos руу шилжүүлж, ердийн алгебр хийж, квадратуудыг Пифагорын адилтгалаар солиорой.

**facts**

- **title** Багаж хэрэгсэл · **latex** `\operatorname{tg} = \tfrac{\sin}{\cos},\ \sec = \tfrac{1}{\cos},\ \sin^2 + \cos^2 = 1` · **explanation** Тодорхойлолтууд ба нэг адилтгал бүлгийн ихэнхийг батална.
- **title** Алтан дүрэм · **latex** `\text{НЭГ талыг хувирга; } = \text{ тэмдгийг хэзээ ч бүү дав}` · **explanation** Гишүүдийг нөгөө тал руу шилжүүлэх нь дүгнэлтийг урьдчилан үнэн гэж үзнэ.

**workedExamples**

- `ti4-we1` — **statement:** Батлаарай: $\operatorname{tg}\theta\cos\theta = \sin\theta$. **solution:** Зүүн тал $= \tfrac{\sin\theta}{\cos\theta}\cdot\cos\theta = \sin\theta$ = баруун тал. ∎
- `ti4-we2` — **statement:** Батлаарай: $\operatorname{tg}\theta + \operatorname{ctg}\theta = \dfrac{1}{\sin\theta\cos\theta}$. **solution:** Зүүн тал $= \tfrac{\sin\theta}{\cos\theta} + \tfrac{\cos\theta}{\sin\theta} = \tfrac{\sin^2\theta + \cos^2\theta}{\sin\theta\cos\theta} = \tfrac{1}{\sin\theta\cos\theta}$. Пифагорын адилтгал баталгааг дуусгалаа. ∎
- `ti4-we3` — **statement:** Батлаарай: $\dfrac{1 - \cos^2\theta}{\cos^2\theta} = \operatorname{tg}^2\theta$. **solution:** Хүртвэр: $1 - \cos^2\theta = \sin^2\theta$. Зүүн тал $= \tfrac{\sin^2\theta}{\cos^2\theta} = \operatorname{tg}^2\theta$. ∎

**commonMistakes**

- **text** «Батлах» явцдаа гишүүдийг тэнцүүгийн тэмдгээр шилжүүлэх. · **correction** Ингэх нь зүүн тал = баруун тал гэдгийг, яг шүүгдэж буй мэдэгдлийг, урьдчилан үнэн гэж үзнэ. Нэг талыг дангаар нь нөгөөтэйгөө тэнцүү болтол хувиргаарай.
- **text** sin ба cos руу огт шилжүүлэлгүй гацах. · **correction** Хоёр алхмын дараа гацсан уу? tg, sec, ctg, cosec бүрийг синус, косинусаар дахин бичээрэй. Энэ нүүдэл ямар ч ухаалаг заль мэхээс олон баталгааг тайлдаг.

**tryIt**

- `ti4-t1` — **statement:** Батлаарай: $\sec\theta - \cos\theta = \sin\theta\operatorname{tg}\theta$. **solution:** Зүүн тал $= \tfrac{1}{\cos\theta} - \cos\theta = \tfrac{1 - \cos^2\theta}{\cos\theta} = \tfrac{\sin^2\theta}{\cos\theta} = \sin\theta\cdot\tfrac{\sin\theta}{\cos\theta}$ = баруун тал. ∎
- `ti4-t2` — **statement:** Батлаарай: $(1 - \sin\theta)(1 + \sin\theta) = \cos^2\theta$. **solution:** Пифагорын адилтгалаар зүүн тал $= 1 - \sin^2\theta = \cos^2\theta$. ∎

### Interactive — 7 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Шүүх хурал · **title** Нэг тал шүүгдэнэ<br>**beats** Адилтгал зүүн тал $=$ баруун тал гэж БҮХ өнцөгт мэдэгдэнэ. · Баталгаа: нэг талыг нөгөө нь БОЛТОЛ дахин бич. · Тэнцүүгийн тэмдгийг давах нь хууль бус: шийдвэрийг урьдчилан үнэн гэж үзнэ. · Төвөгтэй талаас эхэл; хялбарчлах нь төвөгтэй болгохоос дээр. |
| 1 | teach | **eyebrow** Гурван нүүдэл · **title** Жижиг хуулийн ном<br>**beats** 1-р нүүдэл: бүгдийг $\sin$ ба $\cos$ руу. · 2-р нүүдэл: ердийн алгебр: бутархай, үржигдэхүүнд задлах, FOIL. · 3-р нүүдэл: Пифагорын солилт: $1 - \sin^2 \leftrightarrow \cos^2$. · Ихэнх баталгаа эдгээр гурван нүүдлийг ямар нэг дарааллаар хийдэг. |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Хууль бус алхмыг ол<br>**prompt** Адилтгал батлах явцад та…<br>**explanation** Хоёр талд зэрэг хийх үйлдэл мэдэгдлийг аль хэдийн үнэн гэж үздэг. Нэг талыг БАТЛАГДСАН адилтгалуудаар дахин бичих нь цорын ганц хууль ёсны зам.<br>**options** `зүүн талыг мэдэгдэх адилтгалуудаар дахин бичиж болно` · `хоёр талд $\sin\theta$ нэмж болно` · `хоёр талыг квадрат зэрэгт дэвшүүлж болно` — **correctIndex 0** |
| 3 | workedSet | **eyebrow** Бодсон жишээ · **title** Баталгааны ур<br>**intro** Гурван нүүдэл дарааллаараа хэрхэн ажиллахыг ажиглаарай.<br>**ex1** Батлаарай: $\dfrac{\sin\theta}{1 + \cos\theta} + \dfrac{1 + \cos\theta}{\sin\theta} = 2\operatorname{cosec}\theta$. · алхам: Ерөнхий хуваарь: $\tfrac{\sin^2\theta + (1+\cos\theta)^2}{\sin\theta(1+\cos\theta)}$. · алхам: Хүртвэр: $\sin^2 + 1 + 2\cos + \cos^2 = 2 + 2\cos\theta$ (Пифагорын солилт). · алхам: $\tfrac{2(1+\cos\theta)}{\sin\theta(1+\cos\theta)} = \tfrac{2}{\sin\theta} = 2\operatorname{cosec}\theta$. ∎ · **хариу** батлагдлаа: бутархай, дараа нь адилтгал, дараа нь хураах<br>**ex2** Батлаарай: $\dfrac{\cos 2\theta}{\cos\theta - \sin\theta} = \cos\theta + \sin\theta$. · алхам: $\cos 2\theta = \cos^2\theta - \sin^2\theta$: квадратын ялгавар. · алхам: Үржигдэхүүнд задал: $(\cos\theta - \sin\theta)(\cos\theta + \sin\theta)$. · алхам: Ижил үржигдэхүүнийг хураа. ∎ · **хариу** батлагдлаа: тригонометрийн хувцастай 10-р ангийн задаргаа |
| 4 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Шүүгчийн суудалд та<br>**intro** Эргэлзвэл эхлээд sin/cos руу шилжүүлээрэй.<br>**p1** $\operatorname{cosec}\theta\operatorname{tg}\theta$-г хялбарчилбал… — **choices** `$\sec\theta$` · `$\sin\theta$` · `$\operatorname{ctg}\theta$` — **answerIndex 0** — $\tfrac{1}{\sin\theta}\cdot\tfrac{\sin\theta}{\cos\theta} = \tfrac{1}{\cos\theta}$.<br>**p2** $\dfrac{\sin^2\theta - 1}{\cos\theta}$ = … — **choices** `$-\cos\theta$` · `$\cos\theta$` · `$\sin\theta - \sec\theta$` — **answerIndex 0** — $\sin^2 - 1 = -\cos^2$: бутархай нь $\tfrac{-\cos^2\theta}{\cos\theta}$.<br>**p3** $\sec^2\theta(1 - \sin^2\theta) = 1$ адилтгалыг батлахад хамгийн хурдан эхний нүүдэл нь… — **choices** `$1 - \sin^2\theta$-г $\cos^2\theta$ болгон солих` · `$\sec^2$ функцийг цуваа болгон задлах` · `хоёр талыг $\sec^2\theta$-д хуваах` — **answerIndex 0** — Дараа нь $\sec^2\theta\cos^2\theta = \tfrac{\cos^2\theta}{\cos^2\theta} = 1$. (Хоёр талыг хуваах нь хууль бус нүүдэл.) |
| 5 | tip | **eyebrow** Дадлага · **title** Гацаанаас гаргагч<br>**body** Гацсан баталгаа бүрт нэг л жор бий: БҮГДИЙГ синус, косинусаар дахин бичиж, нэг хуваарьт оруулаад, хүртвэрт нуугдсан $\sin^2 + \cos^2$-ыг хайгаарай. Энэ гайхмаар олон удаа гарч ирдэг: Пифагорын адилтгал бол энэ бүлгийн бүх цоожийг тайлах түлхүүр. |
| 6 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу сурснаа эргэн харъя<br>**points** Зөвхөн нэг талыг хувирга: тэнцүүгийн тэмдгийг давах нь шийдвэрийг урьдчилан үнэн гэж үзнэ. · Гурван нүүдэл: sin/cos руу, ердийн алгебр, Пифагорын солилт. · Төвөгтэй талаас эхэлж, цэвэрхэн тал руу хялбарчил. |

---

## Lesson 5 — Тригонометрийн тэгшитгэл бодох (`solving-trig-equations`)

**concreteComparison**

$x^2 = 25$-ыг бодвол хоёр хариу гарна. $\sin x = \tfrac12$-ийг бодвол ТӨГСГӨЛГҮЙ олон хариу гарна: синусын долгион $\tfrac12$ өндрийг эргэлт бүрт хоёр удаа, үүрд огтолно. Тригонометрийн тэгшитгэлийг (trig equation) «тэр ганц» хариуг олж биш, хэвийг олж боддог: нэгж тойргийн аль цэгүүд тохирох вэ, дараа нь түүнээс хойших эргэлт бүр.

**objective**

Тригонометрийн энгийн тэгшитгэлийг нэгж тойрог ашиглан [0, 2π) дээр бодож, + 2πk нэмэгдэхүүнтэй ерөнхий шийдийг (full solution set) бичих.

**concept**

1. **Нэгж тойрог бол хариуны түлхүүр**: $\sin x = \tfrac12$ гэдэг нь «$\tfrac12$ ӨНДӨР хаана байна вэ?» гэж асууна. Эргэлт бүрт хоёр цэг: $x = \tfrac{\pi}{6}$ ба $x = \pi - \tfrac{\pi}{6} = \tfrac{5\pi}{6}$.

2. **Синусын хос шийд босоо тэнхлэгийн хувьд тэгш хэмтэй** ($x$ ба $\pi - x$ ижил өндөртэй); **косинусын хос хэвтээ тэнхлэгийн хувьд тэгш хэмтэй** ($x$ ба $2\pi - x = -x$ ижил хэвтээ байрлалтай); **тангенс хагас эргэлт тутамд давтагдана** ($x$ ба $x + \pi$).

3. **Бүх шийд**: тойрог $2\pi$ тутамд давтагддаг тул суурь шийд бүр бүлэг шийд үүсгэнэ: $x = \tfrac{\pi}{6} + 2\pi k$. Ихэнх бодлого зөвхөн $[0, 2\pi)$, өөрөөр хэлбэл нэг эргэлтийг асууна.

4. **Эхлээд тусгаарлах**: тойрог орж ирэхээс өмнө $2\cos x + \sqrt3 = 0$ нь $\cos x = -\tfrac{\sqrt3}{2}$ болно. Тригонометрийн тэгшитгэл бол төгсгөлд нь тойрогтой 8-р ангийн шугаман тэгшитгэл бодолт.

**keyIdea**

Тригонометрийн функцийг тусгаарлаж, нэгж тойрог дээрх жишиг цэгүүдийг олоорой (синус: хоёр өндөр; косинус: хоёр хэвтээ байрлал; тангенс: хагас эргэлтээр давтагдана), дараа нь төгсгөлгүй бүлэг шийдэд + 2πk нэмээрэй.

**facts**

- **title** Синусын хос · **latex** `\sin x = c \Rightarrow x = \alpha \text{ эсвэл } \pi - \alpha` · **explanation** Ижил өндөр, босоо тэнхлэгийн хувьд тэгш хэмтэй.
- **title** Мөнхийн бүлэг · **latex** `x = \alpha + 2\pi k, \quad k \in \mathbb{Z}` · **explanation** Тойргийн эргэлт бүр шийд бүрийг давтана.

**workedExamples**

- `ti5-we1` — **statement:** $[0, 2\pi)$ дээр $\sin x = \tfrac{1}{2}$-ийг бодоорой. **solution:** $\tfrac12$ өндөр: жишиг өнцөг $\tfrac{\pi}{6}$, I ба II мөч. $x = \tfrac{\pi}{6}, \tfrac{5\pi}{6}$.
- `ti5-we2` — **statement:** $[0, 2\pi)$ дээр $2\cos x + \sqrt{3} = 0$-ийг бодоорой. **solution:** Тусгаарлавал: $\cos x = -\tfrac{\sqrt3}{2}$. Хэвтээ байрлал $-\tfrac{\sqrt3}{2}$: II ба III мөч, жишиг $\tfrac{\pi}{6}$. $x = \tfrac{5\pi}{6}, \tfrac{7\pi}{6}$.
- `ti5-we3` — **statement:** $[0, 2\pi)$ дээр $\operatorname{tg} x = 1$-ийг бодоорой. **solution:** Синус, косинус тэнцүү газар $\operatorname{tg} = 1$: $x = \tfrac{\pi}{4}$, хагас эргэлтийн дараа $x = \tfrac{5\pi}{4}$.

**commonMistakes**

- **text** $\sin x = \tfrac12$-д тооны машины ганц хариуг л бичих. · **correction** Долгион өндөр бүрийг эргэлт бүрт хоёр удаа огтолно: $\tfrac{\pi}{6}$ БА $\tfrac{5\pi}{6}$. Тооны машины нуудаг хосыг тойрог харуулна.
- **text** Тангенсын шийдэд $\pi k$ биш, $2\pi k$ нэмэх. · **correction** Тангенс $2\pi$ биш, $\pi$ тутамд давтагдана: бүлэг шийд нь $\tfrac{\pi}{4} + \pi k$. Хагас эргэлтийн тэгш хэм шийдийг хоёр дахин олон давтамжтай болгоно.

**tryIt**

- `ti5-t1` — **statement:** $[0, 2\pi)$ дээр $\cos x = \tfrac{\sqrt2}{2}$-ыг бодоорой. **solution:** Хэвтээ байрлал $\tfrac{\sqrt2}{2}$: I ба IV мөч. $x = \tfrac{\pi}{4}, \tfrac{7\pi}{4}$.
- `ti5-t2` — **statement:** $[0, 2\pi)$ дээр $2\sin x - \sqrt{3} = 0$-ийг бодоорой. **solution:** $\sin x = \tfrac{\sqrt3}{2}$: $x = \tfrac{\pi}{3}, \tfrac{2\pi}{3}$.

### Interactive — 8 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Төгсгөлгүй олон хариу · **title** Шинэ төрлийн тэгшитгэл<br>**beats** $x^2 = 25$: хоёр хариу, болоо. · $\sin x = \tfrac12$: долгион $\tfrac12$ өндөрт эргэлт БҮРТ хоёр удаа хүрнэ. · Төгсгөлгүй олон шийд, гэхдээ төгс хэвтэй. · Нэг эргэлтийнхийг ол; үлдсэн нь $+2\pi k$. |
| 1 | unitCircle | **eyebrow** Хариуны түлхүүр · **title** Тойрог дээрх ½ өндөр<br>**teach** Өнцгийг тойргоор алхуулаарай: $\sin$ бол цэгийн ӨНДӨР. $\tfrac12$ өндөр $30°$-т ($\tfrac{\pi}{6}$) гарна, дахиад $150°$-т ($\tfrac{5\pi}{6}$): босоо тэнхлэгийн хувьд тэгш хэмтэй цэг. Синусын тэгшитгэл бүр эргэлт бүрт хоёр цэгтэй ийм хэлбэртэй.<br>**config** unchanged (`mode: explore`, `start: 30`) |
| 2 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Хос шийд<br>**prompt** $\sin x = \tfrac{\sqrt2}{2}$-ын нэг шийд нь $\tfrac{\pi}{4}$. $[0, 2\pi)$ дэх нөгөө шийд нь…<br>**explanation** Синус бол өндөр: ижил өндөр $\pi - \tfrac{\pi}{4} = \tfrac{3\pi}{4}$ цэгт оршино. (Хэвтээ тэнхлэгийн хувьд тэгш хэмтэй $\tfrac{7\pi}{4}$ бол КОСИНУСЫН хосын дүрэм.)<br>**options** `$\tfrac{3\pi}{4}$: босоо тэнхлэгийн хувьд тэгш хэм` · `$\tfrac{7\pi}{4}$: хэвтээ тэнхлэгийн хувьд тэгш хэм` · `$\tfrac{5\pi}{4}$: эсрэг цэг` — **correctIndex 0** |
| 3 | teach | **eyebrow** Жор · **title** Тусгаарла, байрлуул, давт<br>**beats** 1. Тусгаарла: $2\cos x + \sqrt3 = 0 \to \cos x = -\tfrac{\sqrt3}{2}$. · 2. Байрлуул: аль мөчид хэвтээ байрлал сөрөг вэ? II ба III. · 3. Утгаас жишиг өнцгийг ол: $\tfrac{\pi}{6}$. · 4. Шаардвал давт: мөнхийн бүлэгт $+2\pi k$. |
| 4 | workedSet | **eyebrow** Бодсон жишээ · **title** Тэгшитгэлийн ур<br>**intro** Тусгаарлаж, байрлуулаад, шаардвал давтаарай.<br>**ex1** $[0, 2\pi)$ дээр $2\sin x + 1 = 0$-ийг бодоорой. · алхам: $\sin x = -\tfrac12$: өндөр сөрөг → III, IV мөч. · алхам: Жишиг $\tfrac{\pi}{6}$: $x = \pi + \tfrac{\pi}{6} = \tfrac{7\pi}{6}$ ба $x = 2\pi - \tfrac{\pi}{6} = \tfrac{11\pi}{6}$. · **хариу** $x = \tfrac{7\pi}{6}, \tfrac{11\pi}{6}$<br>**ex2** $[0, 2\pi)$ дээр $\operatorname{tg} x = -\sqrt3$-ыг бодоорой. · алхам: Жишиг: $\operatorname{tg}\tfrac{\pi}{3} = \sqrt3$. Сөрөг тангенс → II, IV мөч. · алхам: $x = \pi - \tfrac{\pi}{3} = \tfrac{2\pi}{3}$, дараа нь хагас эргэлтийн дараа $\tfrac{2\pi}{3} + \pi = \tfrac{5\pi}{3}$. · **хариу** $x = \tfrac{2\pi}{3}, \tfrac{5\pi}{3}$ |
| 5 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Эргэлт бүрт хоёр цэг<br>**intro** Эхлээд мөч, дараа нь жишиг өнцөг.<br>**p1** $[0, 2\pi)$ дээр $\cos x = -1$ нь… — **choices** `яг нэг шийдтэй: $x = \pi$` · `хоёр шийдтэй` · `шийдгүй` — **answerIndex 0** — $-1$ хэвтээ байрлал зөвхөн тойргийн хамгийн зүүн цэгт л бий. $\pm1$ хязгаарын утгууд эргэлтэд ганц шийдтэй үл хамаарах тохиолдлууд.<br>**p2** $\sin x = 2$ нь… — **choices** `шийдгүй: өндөр $[-1, 1]$-д л байдаг` · `$x = \arcsin 2$` · `эргэлт бүрт хоёр шийдтэй` — **answerIndex 0** — Тойргийн цэгүүд $[-1,1]$ өндрийн мужаас хэзээ ч гардаггүй. Бодохоосоо ӨМНӨ утгын мужийг шалгаарай.<br>**p3** $\cos x = \tfrac12$-ийн бүх шийд нь… — **choices** `$\pm\tfrac{\pi}{3} + 2\pi k$` · `$\tfrac{\pi}{3} + \pi k$` · `зөвхөн $\tfrac{\pi}{3}$` — **answerIndex 0** — Косинусын хоёр цэг бол хэвтээ тэнхлэгийн хувьд тэгш хэмтэй $\pm\tfrac{\pi}{3}$; тус бүр бүтэн эргэлт тутамд давтагдана. |
| 6 | funFact | **eyebrow** Одон орон · **title** Нар мандах тэгшитгэл<br>**body** Нар мандах цагийг таамагладаг өдрийн уртын томьёо бол тригонометрийн тэгшитгэл: $\cos H = -\operatorname{tg}(\text{өргөрөг})\operatorname{tg}(\text{нарны хазайлт})$ тэгшитгэлээс цагийн өнцөг (hour angle) гэж нэрлэгдэх $H$-ийг олно. Эргэлт бүрт хоёр шийд: нэг нь нар мандах, тэгш хэмтэй нөгөө нь нар жаргах. Одон орон судлаачид Птолемейн үеэс хойш эргэлт бүрт хоёр цэгтэй энэ төрлийн бодлогыг бодсоор ирсэн. |
| 7 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу сурснаа эргэн харъя<br>**points** Тригонометрийн тэгшитгэл $+2\pi k$ бүлгүүдээр төгсгөлгүй олон шийдтэй. · Функцийг тусгаарлаад нэгж тойргийг унш: синус = өндөр, косинус = хэвтээ байрлал. · Эргэлт бүрт хоёр цэг (тэгш хэмтэй); тангенс хагас эргэлт тутамд давтагдана; эхлээд утгын мужийг шалга. |

---

## Lesson 6 — Квадрат төрлийн тригонометрийн тэгшитгэл (`quadratic-trig-equations`)

**concreteComparison**

10-р анги танд $2u^2 - u - 1 = 0$-ийг нойрондоо ч задалж сургасан. Одоо түүнд хувцас өмсгөе: $2\sin^2 x - \sin x - 1 = 0$ бол тригонометрийн хувцас өмссөн ЯГ ТЭР тэгшитгэл. $u = \sin x$ орлуулга хийж, үржигдэхүүнд задлаад, язгуур бүрийг нэгж тойрогт өгөөрэй. Хуучин алгебр, шинэ сүүлийн алхам.

**objective**

Квадрат төрлийн тригонометрийн тэгшитгэлийг (quadratic trig equation) бодох: орлуулга хийж, үржигдэхүүнд задлаад, утга бүрийг нэгж тойргоор бодож, холимог функцүүдийг адилтгалаар нэг функц болгох.

**concept**

1. **Квадратыг харах**: $u = \sin x$ үед $2\sin^2 x - \sin x - 1 = 0$ нь $2u^2 - u - 1 = (2u + 1)(u - 1) = 0$: цэвэр 10-р ангийн бодлого.

2. **Дараа нь тойрог**: $u = -\tfrac12$ эсвэл $u = 1$ гэдэг нь $\sin x = -\tfrac12$ (хоёр цэг: $\tfrac{7\pi}{6}, \tfrac{11\pi}{6}$) эсвэл $\sin x = 1$ (нэг цэг: $\tfrac{\pi}{2}$). $[0, 2\pi)$ дээр нийт гурван шийд.

3. **Холимог функц уу? Эхлээд нэгтгээрэй**: $2\cos^2 x + \sin x - 1 = 0$ тэгшитгэлд хоёулаа бий. $\cos^2 x = 1 - \sin^2 x$ гэж соливол цэвэр $\sin x$-ийн квадрат тэгшитгэл болно. Пифагорын адилтгал бол орчуулагч.

4. **Боломжгүйг хаях**: задлахад $\sin x = 3$ гарвал түүнийг хаяарай: өндөр 1-ээс хэтрэхгүй. Алгебрын язгуур бүр автоматаар тойрог дээрх өнцөг болдоггүй.

**keyIdea**

Тригонометрийн функцийн оронд u орлуулж, 10-р ангийн квадрат тэгшитгэлийг задлаад, язгуур бүрийг нэгж тойрог дээр бодоорой; холимог функцүүдийг эхлээд Пифагорын адилтгалаар нэгтгээрэй.

**facts**

- **title** Далдлалт · **latex** `2\sin^2 x - \sin x - 1 = 0 \;\xrightarrow{u = \sin x}\; 2u^2 - u - 1 = 0` · **explanation** 10-р ангийнх шиг задлаад, тойрог дээр дуусга.
- **title** Орчуулагч · **latex** `\cos^2 x = 1 - \sin^2 x` · **explanation** Холимог функцтэй тэгшитгэлийг нэг функцийн квадрат тэгшитгэл болгоно.

**workedExamples**

- `ti6-we1` — **statement:** $[0, 2\pi)$ дээр $2\sin^2 x - \sin x - 1 = 0$-ийг бодоорой. **solution:** Задлавал: $(2\sin x + 1)(\sin x - 1) = 0$. $\sin x = -\tfrac12$: $x = \tfrac{7\pi}{6}, \tfrac{11\pi}{6}$. $\sin x = 1$: $x = \tfrac{\pi}{2}$.
- `ti6-we2` — **statement:** $[0, 2\pi)$ дээр $2\cos^2 x + \sin x - 1 = 0$-ийг бодоорой (холимог функц). **solution:** Нэгтгэвэл: $2(1 - \sin^2 x) + \sin x - 1 = 0$, өөрөөр хэлбэл $-2\sin^2 x + \sin x + 1 = 0$. $-1$-ээр үржүүлбэл: $2\sin^2 x - \sin x - 1 = 0$: өмнөх жишээний квадрат тэгшитгэл. $x = \tfrac{\pi}{2}, \tfrac{7\pi}{6}, \tfrac{11\pi}{6}$.
- `ti6-we3` — **statement:** $[0, 2\pi)$ дээр $\cos^2 x = \tfrac{1}{4}$-ийг бодоорой. **solution:** $\cos x = \pm\tfrac12$: квадрат язгуурын ХОЁУЛАНГ нь. Дөрвөн цэг: $\tfrac{\pi}{3}, \tfrac{2\pi}{3}, \tfrac{4\pi}{3}, \tfrac{5\pi}{3}$.

**commonMistakes**

- **text** $\sin x\cos x = \cos x$-ийн хоёр талыг $\cos x$-т хуваах. · **correction** Ингэвэл $\cos x = 0$ байх бүх шийд арилна, гэтэл $x = \tfrac{\pi}{2}$ шийд МӨН. Бүгдийг зүүн тийш шилжүүлээд ЗАДЛААРАЙ: $\cos x(\sin x - 1) = 0$. 10-р ангийнхтай ижил дүрэм: хувьсагчид хэзээ ч бүү хуваагаарай.
- **text** $\sin x = 3$-ыг шийдийн салаа болгон үлдээх. · **correction** Задлах бол алгебр; тойрог бол геометр. $[-1, 1]$-ээс гадуурх өндөр өнцөггүй: тэр салааг хаяж, бусдыг нь үлдээгээрэй.

**tryIt**

- `ti6-t1` — **statement:** $[0, 2\pi)$ дээр $\sin^2 x - \sin x = 0$-ийг бодоорой. **solution:** $\sin x(\sin x - 1) = 0$ болгон задлавал: $\sin x = 0$ нь $0, \pi$-г; $\sin x = 1$ нь $\tfrac{\pi}{2}$-г өгнө.
- `ti6-t2` — **statement:** $[0, 2\pi)$ дээр $2\cos^2 x - \cos x - 1 = 0$-ийг бодоорой. **solution:** $(2\cos x + 1)(\cos x - 1) = 0$: $\cos x = -\tfrac12 \to \tfrac{2\pi}{3}, \tfrac{4\pi}{3}$; $\cos x = 1 \to 0$.

### Interactive — 8 steps, kinds and order unchanged

| # | kind | content |
|---|---|---|
| 0 | teach | **eyebrow** Хувцас · **title** 10-р анги эргэн ирлээ<br>**beats** $2\sin^2 x - \sin x - 1 = 0$ харь гаригийнх мэт харагдана. · $u = \sin x$ орлуул: $2u^2 - u - 1 = 0$. · Та үүн шиг зуугаад тэгшитгэл задалсан: $(2u+1)(u-1) = 0$. · Шинэ сэдэв, хуучин булчин. Тойрог зөвхөн төгсгөлд орж ирнэ. |
| 1 | tapQuestion | **eyebrow** Түргэн шалгалт · **title** Эхлээд задал<br>**prompt** $u = \sin x$ орлуулга $\sin^2 x - \sin x = 0$ тэгшитгэлийг юу болгох вэ?<br>**explanation** $u^2 - u = u(u-1)$. Задлаарай: $u$-д хэзээ ч бүү хуваагаарай; $u = 0$ салаа бодит өнцгүүдийг ($0$ ба $\pi$) агуулна.<br>**options** `$u(u - 1) = 0$` · `$u^2 = u^2$` · `$u - 1 = 0$` — **correctIndex 0** |
| 2 | teach | **eyebrow** Язгуур бүр тойрогт тусдаа аялна · **title** Хуваагаад дуусга<br>**beats** $(2\sin x + 1)(\sin x - 1) = 0$ хоёр хуваагдана: · $\sin x = -\tfrac12$: III + IV мөч → $\tfrac{7\pi}{6}, \tfrac{11\pi}{6}$. · $\sin x = 1$: тойргийн орой → ганцхан $\tfrac{\pi}{2}$. · Нэгдэл: энэ эргэлтэд гурван шийд. Үржигдэхүүнийг биш, цэгийг тоол. |
| 3 | teach | **eyebrow** Холимог функц · **title** Орчуулагч<br>**beats** $2\cos^2 x + \sin x - 1 = 0$: хоёр өөр функц. Гацав уу? · Пифагорын солилт: $\cos^2 x = 1 - \sin^2 x$. · Одоо БҮГД синус: $2 - 2\sin^2 x + \sin x - 1 = 0$. · Цэгцэлбэл $2\sin^2 x - \sin x - 1 = 0$: нэг алхмын өмнө бодсон. |
| 4 | workedSet | **eyebrow** Бодсон жишээ · **title** Хувцас тайлах<br>**intro** Орлуулж, задлаад, тойрог дээр бодож, боломжгүйг нь хаяарай.<br>**ex1** $[0, 2\pi)$ дээр $2\sin^2 x = 1$-ийг бодоорой. · алхам: $\sin^2 x = \tfrac12$: $\sin x = \pm\tfrac{\sqrt2}{2}$: хоёр язгуур хоёулаа. · алхам: Эерэг: $\tfrac{\pi}{4}, \tfrac{3\pi}{4}$. Сөрөг: $\tfrac{5\pi}{4}, \tfrac{7\pi}{4}$. · алхам: Дөрвөн шийд: квадрат цэгийн тоог хоёр дахин олшруулна. · **хариу** $x = \tfrac{\pi}{4}, \tfrac{3\pi}{4}, \tfrac{5\pi}{4}, \tfrac{7\pi}{4}$<br>**ex2** $[0, 2\pi)$ дээр $\sin x\cos x = \cos x$-ийг ХУВААЛГҮЙГЭЭР бодоорой. · алхам: Бүгдийг зүүн тийш: $\cos x(\sin x - 1) = 0$. · алхам: $\cos x = 0$: $x = \tfrac{\pi}{2}, \tfrac{3\pi}{2}$. $\sin x = 1$: $x = \tfrac{\pi}{2}$ (аль хэдийн тоолсон). · алхам: $\cos x$-т хуваасан бол косинусын хоёр цэгийг хоёуланг нь чимээгүй устгах байсан. · **хариу** $x = \tfrac{\pi}{2}, \tfrac{3\pi}{2}$ |
| 5 | tryItSet | **eyebrow** Өөрөө туршиж үз · **title** Хувцасгүй<br>**intro** u орлуулгыг толгойдоо хийгээрэй; тойрог дуусгана.<br>**p1** $[0, 2\pi)$ дээр $(\sin x - 1)(\sin x + 3) = 0$ нь… — **choices** `нэг шийдтэй: $+3$ салаа боломжгүй` · `гурван шийдтэй` · `хоёр шийдтэй` — **answerIndex 0** — $\sin x = -3$ өнцөггүй (өндөр 1-ээс хэтрэхгүй); $\sin x = 1$ зөвхөн $\tfrac{\pi}{2}$-г өгнө.<br>**p2** $2\sin^2 x - 3\cos x = 3$-ыг бодохын тулд эхлээд… — **choices** `$\sin^2 x = 1 - \cos^2 x$ гэж солих` · `$\sin x$-т хуваах` · `квадрат язгуур гаргах` — **answerIndex 0** — Нэг функц болгож нэгтгээрэй: $2 - 2\cos^2 x - 3\cos x = 3$ бол зөвхөн $\cos x$-ийн квадрат тэгшитгэл.<br>**p3** $[0, 2\pi)$ дээр $\operatorname{tg}^2 x = 3$ хэдэн шийдтэй вэ? — **choices** `дөрөв` · `хоёр` · `нэг` — **answerIndex 0** — $\operatorname{tg} x = \pm\sqrt3$: тэмдэг бүр эргэлт бүрт хоёр удаа таарна (тангенс хагас эргэлтээр давтагдана): $\tfrac{\pi}{3}, \tfrac{2\pi}{3}, \tfrac{4\pi}{3}, \tfrac{5\pi}{3}$. |
| 6 | funFact | **eyebrow** Том зураг · **title** Бүлэг нэг өгүүлбэрт<br>**body** Энд байсан бүхэн дахин ашиглалт байлаа: өмнөх ангиудын Пифагорын теорем үндсэн адилтгал болж, FOIL ба үржигдэхүүнд задлах (10-р анги) батлах, бодоход тусалж, нэгж тойрог (11-р анги) хариуны түлхүүр болсон. 12-р анги шинийг ховор зохиодог: харин НИЙЛҮҮЛДЭГ. Шалгалтын хэмждэг жинхэнэ ур чадвар энэ. |
| 7 | recap | **eyebrow** Эргэн дүгнэлт · **title** Юу сурснаа эргэн харъя<br>**points** Квадрат хэлбэртэй тригонометрийн тэгшитгэл: $u$ орлуул, задал, язгуур бүрийг тойрог дээр бод. · Холимог функц: эхлээд $\cos^2 = 1 - \sin^2$-аар нэгтгэ. · Тригонометрийн үржигдэхүүнд хэзээ ч бүү хуваа: зүүн тийш шилжүүлж задал; $[-1,1]$-ээс гадуурх язгуурыг хая. |

---

## PRACTICE

- `ti-pr1` — **statement:** $\theta$ нь IV мөчид, $\cos\theta = \tfrac{8}{17}$ бол $\sin\theta$ ба $\operatorname{tg}\theta$-г олоорой. **solution:** $\sin\theta = -\tfrac{15}{17}$ (IV мөчид сөрөг); $\operatorname{tg}\theta = -\tfrac{15}{8}$.
- `ti-pr2` — **statement:** $\cos\theta + \sin\theta\operatorname{tg}\theta$ илэрхийллийг хялбарчлаарай. **solution:** $\cos\theta + \tfrac{\sin^2\theta}{\cos\theta} = \tfrac{\cos^2 + \sin^2}{\cos\theta} = \sec\theta$.
- `ti-pr3` — **statement:** $\cos 105°$-ыг яг бодоорой. **solution:** $105 = 60 + 45$: $\cos 60°\cos 45° - \sin 60°\sin 45° = \tfrac{\sqrt2 - \sqrt6}{4}$.
- `ti-pr4` — **statement:** $\sin 3\theta\cos\theta - \cos 3\theta\sin\theta$ илэрхийллийг хялбарчлаарай. **solution:** Урвуугаар уншсан ялгаврын синус: $\sin(3\theta - \theta) = \sin 2\theta$.
- `ti-pr5` — **statement:** $\sin\theta = \tfrac{12}{13}$, II мөч: $\sin 2\theta$-г олоорой. **solution:** $\cos\theta = -\tfrac{5}{13}$; $\sin 2\theta = 2\cdot\tfrac{12}{13}\cdot(-\tfrac{5}{13}) = -\tfrac{120}{169}$.
- `ti-pr6` — **statement:** Батлаарай: $\dfrac{\sin 2\theta}{2\sin^2\theta} = \operatorname{ctg}\theta$. **solution:** $\tfrac{2\sin\theta\cos\theta}{2\sin^2\theta} = \tfrac{\cos\theta}{\sin\theta} = \operatorname{ctg}\theta$. ∎
- `ti-pr7` — **statement:** Батлаарай: $\operatorname{cosec}^2\theta(1 - \cos^2\theta) = 1$. **solution:** $1 - \cos^2 = \sin^2$: зүүн тал $= \tfrac{\sin^2\theta}{\sin^2\theta} = 1$. ∎
- `ti-pr8` — **statement:** $[0, 2\pi)$ дээр $2\cos x - 1 = 0$-ийг бодоорой. **solution:** $\cos x = \tfrac12$: $x = \tfrac{\pi}{3}, \tfrac{5\pi}{3}$.
- `ti-pr9` — **statement:** $[0, 2\pi)$ дээр $\operatorname{tg} x + \sqrt3 = 0$-ийг бодоорой. **solution:** $\operatorname{tg} x = -\sqrt3$: II ба IV мөч, жишиг $\tfrac{\pi}{3}$: $x = \tfrac{2\pi}{3}, \tfrac{5\pi}{3}$.
- `ti-pr10` — **statement:** $[0, 2\pi)$ дээр $2\sin^2 x + 3\sin x + 1 = 0$-ийг бодоорой. **solution:** $(2\sin x + 1)(\sin x + 1) = 0$: $\sin x = -\tfrac12 \to \tfrac{7\pi}{6}, \tfrac{11\pi}{6}$; $\sin x = -1 \to \tfrac{3\pi}{2}$.

---

## TEST YOURSELF

- `ti-ty1` — **statement:** $\sin\theta = -\tfrac{7}{25}$, III мөч: $\cos\theta$ ба $\operatorname{tg}\theta$-г олоорой. **solution:** $\cos\theta = -\tfrac{24}{25}$ (III мөч); $\operatorname{tg}\theta = \tfrac{7}{24}$ (III мөчид эерэг).
- `ti-ty2` — **statement:** $\sin 105°$-ыг яг бодоорой. **solution:** $105 = 60 + 45$: $\sin 60°\cos 45° + \cos 60°\sin 45° = \tfrac{\sqrt6 + \sqrt2}{4}$.
- `ti-ty3` — **statement:** $\cos\theta = -\tfrac{4}{5}$, II мөч: $\cos 2\theta$ ба $\sin 2\theta$-г олоорой. **solution:** $\cos 2\theta = 2\cdot\tfrac{16}{25} - 1 = \tfrac{7}{25}$; $\sin\theta = \tfrac35$ тул $\sin 2\theta = 2\cdot\tfrac35\cdot(-\tfrac45) = -\tfrac{24}{25}$.
- `ti-ty4` — **statement:** Батлаарай: $\dfrac{1 + \cos 2\theta}{2} = \cos^2\theta$. **solution:** $\cos 2\theta = 2\cos^2\theta - 1$: зүүн тал $= \tfrac{1 + 2\cos^2\theta - 1}{2} = \cos^2\theta$. ∎ (Энэ зэрэг бууруулах (power reduction) хэлбэр анализд дахин гарч ирнэ.)
- `ti-ty5` — **statement:** $[0, 2\pi)$ дээр $\sqrt{2}\sin x - 1 = 0$-ийг бодоорой. **solution:** $\sin x = \tfrac{1}{\sqrt2} = \tfrac{\sqrt2}{2}$: $x = \tfrac{\pi}{4}, \tfrac{3\pi}{4}$.
- `ti-ty6` — **statement:** $[0, 2\pi)$ дээр $2\cos^2 x - \sin x - 1 = 0$-ийг бодоорой. **solution:** Нэгтгэвэл: $2(1 - \sin^2 x) - \sin x - 1 = 0 \to 2\sin^2 x + \sin x - 1 = 0 \to (2\sin x - 1)(\sin x + 1) = 0$. $\sin x = \tfrac12 \to \tfrac{\pi}{6}, \tfrac{5\pi}{6}$; $\sin x = -1 \to \tfrac{3\pi}{2}$.
- `ti-ty7` — **statement:** Ангийн нэг сурагч адилтгалыг $\sin\theta$-г тэнцүүгийн тэмдгийн нөгөө тал руу шилжүүлж, дараа нь хоёр талыг ижил зүйл болтол хялбарчилж «баталжээ». Юу буруу вэ, хэрхэн засах вэ? **solution:** Тэнцүүгийн тэмдгийн хоёр талаар үйлдэл хийх нь шүүгдэж буй мэдэгдлийг, зүүн тал = баруун тал гэдгийг, урьдчилан үнэн гэж үзнэ. Засвар: дахин эхэлж, НЭГ талыг дангаар нь (sin/cos руу шилжүүлэх, алгебр, Пифагорын солилт) нөгөө нь болтол хувиргаарай.

---

## Notes for Khas

### 1. English claims checked; three findings for Build, five hedges

Every number in the topic was re-computed by script: **156 assertions** over
all 47 items and every interactive value, distractors included (scratch
`verify.py`, sympy for the identities, a numeric root scan of $[0, 2\pi)$ for
every equation, each root then substituted exactly). All are correct.

**For Build (ship mode), three English-source findings:**

- **sec, csc and cot are used before they are defined.** Lesson 1 concept 3,
  its fact, step 2 and tryItSet p2 all use $\sec$, $\csc$, $\cot$; the
  definitions arrive only in lesson 4 concept 2. The grade 11 topic never
  defines them (it never uses even tangent). The Mongolian puts the four
  definitions in a parenthesis inside lesson 1 concept 3, an addition inside
  an existing string. The English would do well to do the same.
- **Lesson 6 funFact: "Pythagoras (Grade 8)".** Grade 8 in this course never
  teaches the theorem; `8/the-real-number-system` mentions only the
  Pythagoreans, in a √2 funFact. (It is grade 8 in the US Common Core, which is
  presumably where the line came from.) The Mongolian says «өмнөх ангиудын».
- **Lesson 5 commonMistake 2 text, "Adding $2\pi k$ to tangent solutions
  only"**, reads as "only tangent solutions get $2\pi k$". The correction shows
  it means "adding only $2\pi k$". The Mongolian says it plainly: «Тангенсын
  шийдэд $\pi k$ биш, $2\pi k$ нэмэх».

**Hedged:**

- Lesson 1 funFact: "four thousand years" becomes «бараг дөрвөн мянган жил»
  (Plimpton 322, c. 1800 BCE, is about 3,800 years old; "a millennium before
  Pythagoras" is fair, about 1,200 years). "Clay tablets list ... triples" is
  the usual reading of Plimpton 322, but its purpose is argued, so «гэж
  ихэвчлэн тайлбарладаг». "Every GPS fix, every audio filter, every video-game
  rotation" becomes «зэрэг олон тооцоо».
- Lesson 2 cc "Your calculator does this dance every time you press sin" and
  funFact "CORDIC, the algorithm inside most calculators since the 1960s":
  Volder published CORDIC in 1959; the famous calculator case is the HP-35
  (1972). The Mongolian says «олон тооны машин» and «1950-аад оны сүүлээр
  зохиогдсон», dropping the decade it reached calculators.
- Lesson 3 funFact: range $\propto \sin 2\theta$ holds on level ground without
  air resistance; the Mongolian says so in its first clause.
- Lesson 5 funFact: "this exact two-spots-per-circle problem since Ptolemy" is
  «энэ төрлийн бодлого». The Almagest does compute day length by latitude, but
  not by this formula.

### 2. Terms

- **cosecant is written `\operatorname{cosec}`, which no ruling covers.** Your
  6ak ruling chose the Russian-school forms tg, ctg, arctg. The same school
  writes cosec, the dictionary entry says «standard form is cosec», and the
  ministry names the function «косеканс» (12.6а). Writing `\csc` beside
  `\operatorname{ctg}` would mix two conventions on one line (`ti4-t1`,
  tryItSet p1 of lesson 4). Secant stays `\sec`, which both conventions share
  and the ministry prints (12.8а). If you want `\csc` instead, it is one
  replace across 9 LaTeX places (the English's 8 plus the added definition)
  and 4 plain-text «cosec».
- **«хэвтээ байрлал» for "width"** (the cosine as the point's horizontal
  coordinate, paired with «өндөр» for the sine). An image word, not a term;
  «өргөн» was the literal choice and reads oddly when it is negative.
- **«цагийн өнцөг» for hour angle** is a calque of the astronomy term (часовой
  угол); no source in the repository has it. One funFact use.
- **«нислэгийн алслалт»** for a projectile's range is the school physics
  phrase; it keeps «утгын муж» free for the sine's range in lesson 5.
- **Mirrors are «тэгш хэм»** by your 4g ruling: «босоо / хэвтээ тэнхлэгийн
  хувьд тэгш хэм». The English says "vertical / horizontal mirror", so the
  axes are named by direction, not as $x$, $y$, which would collide with the
  variable $x$ on the same line.
- **«гүйцээлт өнцөг»** follows GEOMETRY-TERMS and draft 56 (dictionary). The
  one shipped grade 7 prompt that says «нэмэлт өнцөг» is recorded there.
- Image words carried from the English: «хувцас» (costume), «шүүх хурал»
  (courtroom), «орчуулагч» (translator), «зөрүүд» for "cosine is the
  contrarian", which is the English's own memory aid, not an invented one.

### 3. Fact cells

The English facts are bare LaTeX, so the Mongolian ones are too. Lesson 4's
golden-rule cell keeps its words inside `\text{}` and reorders them around
the bare `=`. Lesson 5's first fact keeps «эсвэл» inside `\text{}`.

### 4. Decimals and intervals

Math-mode decimals stay points (2d): $1.41$ (twice), $22.5°$ (four times). No
prose decimals, no money. Intervals keep the English's $[0, 2\pi)$ and
$[-1, 1]$: General Math, not the ЭШ hub.

### 5. Round 2 (5 Oct 2026)

5a: English shown once at first use, 16 terms (master identity, Pythagorean
identity, secant, cosecant, cotangent, sum formulas, difference formulas,
counterexample, double-angle formulas, projectile range, proof, trig equation,
full solution set, hour angle, quadratic trig equation, power reduction). Not
glossed: tg, ctg, cosec (notation). FOIL carries its Mongolian gloss once
(5b), at lesson 1 tryItSet p3.
