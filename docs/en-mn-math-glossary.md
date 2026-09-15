# English → Mongolian mathematics glossary

Transcribed from **«Математикийн англи-монгол нэр томьёо, үг, хэллэгийн лавлах толь»** (Д.Пүрэвдорж) — the English–Mongolian reference dictionary of mathematical terms, words and phrases.

- **Source pages:** 13–223 (200 photographs, latest batch transcribed 2026-09-13)
- **Entries:** 3937 (653 carry a usage note)
- **Alphabetical coverage:** `a` → `jointly variable` — all of **A–I**, and into **J**

> **This file is the guide. The data is in `en-mn-math-glossary.tsv`.**
> At 3937 entries a full Markdown table is no longer something anyone reads, so this file
> carries the core terms and the entries that need a judgement call; the TSV carries everything
> and is what you should grep.

## How to look a term up

```bash
grep -i -P "^angle\t"  docs/en-mn-math-glossary.tsv   # exact headword
grep -i    "angle"      docs/en-mn-math-glossary.tsv   # anything containing it
```

Search the **whole phrase** you need — `alternate interior angles`, `common denominator`,
`inverse function` — not just the head noun. The book's phrase-level renderings often differ
from the sum of the parts, and there are well over a thousand of them.

The Mongolian column lists the dictionary's equivalents; the first is the default unless the
note says otherwise. Where an entry appears on more than one page the variants are separated
by `;`.

## Coverage — what is and isn't here

Letters **A through I are complete**, and J has begun (it stops at `jointly variable`, p.223).
Beyond J the file holds only multi-word phrases whose first word falls earlier in the alphabet.

Now covered, which the earlier batches were missing: *factor, formula, fraction, function,
geometry, gradient, graph, histogram, hypotenuse, identity, index, inequality, infinity,
integer, integral, intersect, interval, inverse, irrational number*.

Still **not** covered: *line, mean, median, multiply, number, parallel, percent, perimeter,
polygon, prime, probability, quadratic, radius, ratio, rectangle, root, sequence, square,
subtract, tangent, triangle, vertex, volume*.

**A term missing from this file is not permission to invent a translation.** See the
"Term not found" rule in `CLAUDE.md`.

---

## Core terms — quick reference

The 121 terms most likely to appear in site copy, lesson text and question banks.

| English | Монгол | Тэмдэглэл |
|---|---|---|
| `add` | нэмэх, нийлбэр болгох |  |
| `addend` | нэмэгдэхүүн | in 3 + 5 = 8, 3 and 5 are addends |
| `addition` | нэмэх, нэмэх үйлдэл, нийлбэр болгох, өөрчлөлт (утгын) |  |
| `algebra` | алгебр |  |
| `algebraic expression` | алгебрын илэрхийлэл, алгебрийн илэрхийлэл | book prints both -ын and -ийн spellings; printed as plural 'algebraic expressions' |
| `altitude` | өндөр |  |
| `angle` | өнцөг |  |
| `acute angle` | хурц өнцөг |  |
| `a right angle` | тэгш өнцөг |  |
| `an obtuse angle` | мохоо өнцөг |  |
| `adjacent angles` | залгаа хоёр өнцөг, ерөнхий талтай хоёр өнцөг |  |
| `alternate interior angles` | дотоод солбисон хоёр өнцөг |  |
| `angle bisector` | өнцгийн биссектрис |  |
| `answer` | хариу, хариулт, хариулах, тохирох, харгалзах, хангах |  |
| `approximate` | ойролцоо утга, ойролцоо илэрхийлэх, ойролцоо тэнцэх |  |
| `area` | талбай, муж, хүрээ (үйлчлэх), салбар |  |
| `arithmetic` | арифметик, арифметикийн үйлдэл | 'арифметик дундаж' нь arithmetic mean-д хамаарна |
| `arithmetic mean` | арифметикийн дундаж, арифметик дундаж |  |
| `arrange` | байрлал, жагсаалт, эрэмбэлсэн байрлал, дэс дараалан байрлуулах, эрэмбэлэн байрлуулах, гэж үзэх, эрэмбэлэх, ангилах |  |
| `ascending` | өсөлт, дээшлэлт, өсөж байгаа, дээшилж байгаа |  |
| `associative` | бүлэглэх | of an operation: бүлэглэх чанартай |
| `average` | дундаж, дундаж тоо гаргах |  |
| `axiom` | аксиом |  |
| `axis (axes)` | тэнхлэг (тэнхлэгүүд) |  |
| `abscissa` | абсцисс | x-coordinate; first coordinate of an ordered pair |
| `absolute value` | абсолют хэмжигдэхүүн |  |
| `base` | үндэс, суурь, үндэслэх, суурилах, тулгуурлах |  |
| `bar graph(s)` | баганан диаграмм |  |
| `bisector` | тэнцүү (хагаслан) хуваагч (шулуун буюу хавтгай), биссектрис |  |
| `binomial` | хоёргишүүнт, бином |  |
| `brackets []` | дөрвөлжин (дунд) хаалт [] |  |
| `calculate` | тооцоолох, тооцоолон бодох, тоолох, бодох, гэж үзэх |  |
| `cancel` | хураах, зурах, устгах, солих, эмхэтгэх, зайлуулах |  |
| `center, centre` | төв, дундаж | label (Англид) marks centre as the British spelling |
| `chord` | хөвч |  |
| `circle` | тойрог, дугуй, эргэлдэх, эргэх, тойргоор хөдлөх |  |
| `circumference` | тойрог, тойргийн урт, битүү муруйн (хүрээний) урт |  |
| `coefficient` | коэффициент, индекс, үржигдэхүүн, илтгэгч |  |
| `combination` | хэсэглэл, хослол, нийлүүлэл, эвлүүлэг |  |
| `common denominator` | ерөнхий хуваарь |  |
| `common factor` | ерөнхий үржигдэхүүн |  |
| `common multiple` | еренхий хуваагдагч | printed "еренхий"; book typo for "ерөнхий" |
| `commutative` | байр солих (сэлгэх) |  |
| `complementary angles` | гүйцээлт хоёр өнцөг |  |
| `composite number` | зохиомол (нийлмэл) тоо |  |
| `cone` | конус, конус гадаргуу |  |
| `congruent` | тэнцүү, ижил, конгруэнт, давхацдаг, жишигдэх (модулаар) |  |
| `constancy, constant` | тогтмол тоо, тогтмол хэмжигдэхүүн, коэффициент | printed as one headword pair |
| `continuous` | тасралтгүй, үргэлжилсэн |  |
| `coordinate` | 1. координат; 2. зохицуулах, уялдуулах | sense 1 noun, sense 2 verb |
| `cube` | куб (зэрэг, дүрс), куб зэрэг дэвшүүлэх |  |
| `curve` | муруй, тахир шугам, график, муруйх, нугалах |  |
| `cylinder` | цилиндр, цилиндр гадаргуу |  |
| `data` | 1. мэдээ (тоон), мэдээлэл (тоон), баримт. 2. үзүүлэлт 3. хэмжсэн хэмжигдэхүүн, үр дүн | entry notes [datum–ын олон тоо; ганц тоо мэт хэрэглэдэг] |
| `decimal` | аравтын бутархай, арвын |  |
| `decimal place` | аравтын бутархайн бутархай хэсгийн орон, таслалын арын орон |  |
| `definition` | тодорхойлолт, томьёолол, загвар бүтээх, хилийг нь тодорхойлох |  |
| `degree` | градус, хуваарь, хэм, зэрэг, үе (бутархайн), түвшин, нэггишүүнт буюу олонгишүүнтийн зэрэг |  |
| `denominator` | бутархайн хуваарь |  |
| `dependent variable` | хамаарах хувьсагч; хамааран хувьсагч | output |
| `derivative` | уламжлал, уламжлал тоо |  |
| `diagonal` | диагонал |  |
| `diameter` | диаметр, голч шугам |  |
| `difference` | 1. ялгавар, ялгаа, ялгавар олох, 2. өөрчлөлт |  |
| `differentiate` | уламжлал олох, дифференциалчилах |  |
| `digit` | 1. цифр, тооны тэмдэг; нэг оронтой тоо, орон. 2. тэмдэг, тэмдэглэл |  |
| `distance` | зай, завсар, зам, хазайлт, ялгааны хэмжээ | sense 1 зай, завсар, зам; sense 2 хазайлт, ялгааны хэмжээ |
| `divide` | хуваах, хуваагдах, бүхэл хуваагдах, жижиглэн хуваах, бутаргах | sense 2 is жижиглэн хуваах, бутаргах |
| `dividend` | хуваагдагч | printed as the pair dividend, divident |
| `divisible` | хуваагдах, бүхэл хуваагдах |  |
| `division` | хуваах, хуваалт, үлдэгдэлгүй хуваах, үлдэгдэлгүй хуваагдаж байгаа | sense 2 is үлдэгдэлгүй хуваах |
| `divisor` | хуваагч |  |
| `domain` | муж, тодорхойлогдох муж, тодорхойлсон муж, завсар (интервал) | sense 2 is завсар (интервал); rendering taken from the parallel Mongolian definition |
| `edge` | ирмэг, хил |  |
| `element` | элемент, бүрэлдэхүүн, бүрэлдэхүүн хэсэг, схем, байгууламж, эхлэл | three numbered senses in the book |
| `ellipse` | эллипс |  |
| `equal` | тэнцүү, тэнцэх, тэнцүүлэх |  |
| `equation` | тэнцэтгэл, тэгшитгэл |  |
| `equivalent` | тэнцүү, тэнцүү чанартай, эквивалент |  |
| `estimate` | ойролцоо үнэлгээ, баримжаа үнэлгээ, үнэлгээ, тооцоо, үнэлэх, үнэлгээ тогтоох, боломжит утга | Book numbers three senses: 1. noun, 2. verb, 3. value |
| `evaluate` | утгыг олох, тооцоолон бодох, тоогоор илэрхийлэх, үнэлэх |  |
| `even number` | тэгш тоо |  |
| `event` | үзэгдэл, үр дүн, тохиолдол |  |
| `expand` | задлах, хаалт нээх (задлах), нийлбэрийг үржүүлэх, өргөтгөх, дэлгэрүүлэх |  |
| `experiment` | туршилт, туршлага, туршилт хийх, турших |  |
| `exponent` | илтгэгч, зэргийн илтгэгч |  |
| `expression` | илэрхийлэл, дүрслэл, томьёо |  |
| `exterior angle` | гадаад өнцөг |  |
| `factor` | үржигдэхүүн, коэффициент, хуваагч, үржигдэхүүн (үржвэр) болгон задлах |  |
| `factorial` | үржвэр |  |
| `formula (formulae)` | томьёо, илэрхийлэл, томьёолол | plural formulae printed in the headword |
| `fraction` | бутархай, энгийн бутархай, тооны бутархай хэсэг |  |
| `frequency` | давтамж | given in the histogram entry |
| `function` | 1. функц 2. үүрэг, үйлчилгээ, зориулалт, ажиллах | senses numbered in the book |
| `geometry` | геометр, геометр байгуулалт, хэлбэр, төрх байрлал, байгуулалт, схем | senses 1./2./3. |
| `gradient formula` | өнцгийн коэффициентийн томьёо, уламжлал |  |
| `graph` | график, дүрслэл, диаграмм, граф, координатын систем тогтоосон хавтгай, график байгуулах, дүрслэх, зурах, диаграмм зурах, диаграмм болгон дүрслэх; координаттай шулуун дээрх дүрслэл | column heading of the interval table; representation on a coordinate line |
| `half (halves)` | хагас, тал |  |
| `height` | өндөр, хамгийн дээд цэг, максимум | 2 senses: 1 өндөр; 2 хамгийн дээд цэг, максимум |
| `hexagon` | зургаанөнцөгт |  |
| `histogram` | гистограм |  |
| `horizontal` | хөндлөн, хэвтээ, хөндлөн шулуун (хавтгай) |  |
| `hypotenuse` | гипотенуз | printed in the cosine-ratio diagram, not as a headword |
| `hypothesis (hypotheses)` | таамаглал, урьдчилсан дүгнэлт, нөхцөл |  |
| `identity` | 1. адилтгал, тэнцүү, адилтгал болох (нь) 2. нэгж элемент, нэгж (алгебрт) |  |
| `image` | 1. дүр, буулгалт, буулгах 2. дүрслэл, дүрслэх 3. загварчлах |  |
| `improper fraction` | засагдах бутархай, зөв бус бутархай |  |
| `increase` | өсөлт, өсөх, нэмэгдэх, дээшлэх, нэмэгдүүлэх |  |
| `independent variable` | үлхамааран хувьсагч; үлхамаарах хувьсагч | printed үлхамааран as one word; input; printed as one word; variant spelling on this page; also printed үл хамааран; printed as one word үлхамаарах |
| `index (indices)` | илтгэгч, зэргийн илтгэгч, зэрэг, коэффициент, судлагдахууны хэлхээ, үзүүлэлт, индекс, судлагдахууны хэлхээ хийх, судлагдахууны хэлхээнд оруулах |  |
| `inequality (inequalities)` | тэнцэтгэлбиш |  |
| `infinity` | төгсгөлгүй, төгсгөлгүй болох (нь) |  |
| `integer` | бүхэл тоо |  |
| `integral` | интеграл, бүхэл тоон, бүхэл |  |
| `intersect` | огтлолцох, огтлох, дайрах |  |
| `interval` | завсар, задгай завсар, хэрчим, муж |  |
| `inverse` | 1. урвуу хэмжигдэхүүн, урвуу, урвуу функц, 2. инверсийн дүр, 3. урвуу элемент, урвуу үйлдэл, 4. инверс (хувиргалт) | four numbered senses as printed |
| `inverse function` | урвуу функц |  |
| `irrational number` | иррационал тоо |  |
| `isosceles triangle` | адил хажуут гурвалжин | the definition below spells it адилхажуут |
| `iterate` | давтах |  |

---

## Terms that need a judgement call

653 entries where the dictionary distinguishes senses, expands an abbreviation, flags a
domain, or where the printed book contains a typo. **Read the note before choosing a rendering.**

| English | Монгол | Тэмдэглэл | p. |
|---|---|---|---|
| `0.01 one handredth` | зууны нэг, 0,01 | printed "handredth"; typo for hundredth | 99 |
| `1 is the multiplicative identity; that is, (1)a=a(1)=a for all a in R, and 1 is the only element in R with this property` | 1 нь үржүүлэхийн нөлөөгүй элемент: R-ийн бүх a тооны хувьд 1 • a=a • 1=a ба 1 нь ийм чанартай R-ийн цорын ганц элемент | rendering ends on p. 194 | 193 |
| `1.3 read: one point three or one and three tenths` | 1.3 бутархайг нэг цэг гурав буюу нэг ба аравны гурав (нэг бүхэл аравны гурав) гэж уншдаг (1,3) | entry runs over onto page 100 | 99 |
| `27C°` | цельсийн 27° дулаан | degrees Celsius | 106 |
| `a` | зарим, нэг, эхний | symbol for a known number/quantity; prefix a- is negating | 13 |
| `A and A', P and A', Q and Q' are corresponding points.` | A, A' хоёр; P, P' хоёр; Q, Q' хоёр нь харгалзах хос цэг | figure caption; book prints "P and A'" for "P and P'" | 89 |
| `A circular region is the union of a circle and it is interior` | Тойрог түүний дотор (дотоод муж) хоёрын нэгдэл нь дугуй юм | printed "it is interior"; typo for "its interior" | 62 |
| `a contraria` | урвуу, урвуугаар | Latin | 18 |
| `A corner point of a solution region is a point in the solution region that is the intersection of two boundary lines.` | Шийдийн мужийн хилийн хоёр шулууны огтлолцлолын цэгийг оройн (булангийн) цэг гэнэ | book prints "огтлолцлолын" for "огтлолцлын" | 88 |
| `a fortiori` | тэх тусмаа | Latin; printed 'тэх' (std. тэр тусмаа) | 22 |
| `a is greater than b` | a нь b–гээс их | printed as a>b: a is greater than b | 183 |
| `A polygon is convex if and only if any line containing a side of the polygon does not contain a point in the interior of the polygon.` | Хэрэв олонөнцөгтийн тал агуулсан шулуун нь уг олонөнцөгтийнхээ дотоод цэг агуулаагүй л бол гүдгэр олонөнцөгт гэнэ | Mongolian rendering printed on page 86 | 85 |
| `a posteriori distribution` | апостериор магадлал, туршилтын дараах магадлал | 'Bayes' formula'-гын орчуулгыг хар | 31 |
| `A shape is convex if the line joining any two point on the shape stays inside the shape.` | Хэрэв дүрсийн аливаа хоёр цэгийг холбосон хэрчим нь дүрсийнхээ дотор оршиж байвал түүнийг гүдгэр дүрс гэнэ | book prints "two point" for "two points" | 85 |
| `AAA` | өнцөг – өнцөг – өнцөг, ӨӨӨ | angle-angle-angle; abbreviation for triangle similarity criterion | 13 |
| `AAS` | өнцөг – өнцөг – тал, ӨӨТ | angle-angle-side; triangle congruence criterion | 13 |
| `ab initio` | бүр эхнээс нь | Latin | 13 |
| `ab ovo` | бүр эхнээс нь | Latin | 14 |
| `abacus` | сампин | тайлбар өгүүлбэрт 'абак' хэлбэрийг бас хэрэглэсэн | 13 |
| `abbreviate` | товчлох, хураангуйлах | shorten a word by letters or syllables | 13 |
| `abbreviation` | товчилол, хураангуйлал, үсэг хураалт, товчилсон үг | e.g. AAA, AAS | 13 |
| `about` | ойролцоо, ойролцоогоор, орчим, орчин (цэгийн) хажууд, бараг, хувьд, тухай, тойруулсан эргүүлэлт | sometimes left untranslated | 13 |
| `about a line` | шулууны хувь дахь тэгшхэм | symmetry with respect to a line | 13 |
| `about-face` | 180°–ын эргүүлэлт | printed as about – face | 13 |
| `above` | –ийн дээр, дээр, дээр нь, өмнө (хугацаа) | өмнө in the time sense | 13 |
| `abridge` | товчлох, товч өгүүлэх, хязгаарлах | 1. shorten 2. limit | 14 |
| `abscissa` | абсцисс | x-coordinate; first coordinate of an ordered pair | 14 |
| `absense` | байхгүй (байх) | printed absense; = absence | 14 |
| `absense of certion orders` | тодорхой орны нэгж байхгүйг | printed certion; = certain | 14 |
| `absolute error` | абсолют зөрөө | difference between real value and estimated value | 14,146 |
| `absolute value equations and inequalities` | абсолют хэмжигдэхүүнтэй тэгшитгэл ба тэнцэтгэлбиш | e.g. \|x\| = 3, \|x\| ≥ 5 | 15 |
| `abstract` | хийсвэр, хийсвэр ухагдахуун, товч агуулга, товч танилцуулга, онолын хийсвэрлэл, товч дүгнэлт, хийсвэрлэх | 1. abstract (adj) 2. summary 3. theoretical abstraction | 15 |
| `abstraction of actual infinity` | бодит төгсгөлгүйн хийсвэрлэл | translation continues on p.16 | 15 |
| `acceleration` | хурдатгал | change in speed per unit of time | 16 |
| `according to` | ёсоор, харгалзан, -аар (-ээр, -оор, -өөр) | also rendered by the instrumental suffix | 17 |
| `accumulution of data` | мэдээний цуглуулга, мэдээ хуримтлагдах | printed accumulution; = accumulation of data | 17 |
| `accurate to` | хүртэп нарийвчлалтай | printed хүртэп; read хүртэл | 17 |
| `achieveable` | хүрч болох | printed achieveable; = achievable | 18 |
| `actual speedy` | бодит хурд, өөрийн хурд | printed speedy; = actual speed | 18 |
| `acute triangle` | хурц өнцөгт гурвалжин | also printed as acute-angled triangle | 18 |
| `ad absurdum` | утгагүйд шилжүүлэх, зөрчилд хүргэх, эсрэгээс нь батлах баталгаа | Latin | 18 |
| `ad infinitum` | төгсгөлгүй хүртэл | Latin | 21 |
| `add the ones` | нэгжүүдийг нь нэм, нэгжийг нь нэм | when adding two whole numbers | 18 |
| `addend` | нэмэгдэхүүн | in 3 + 5 = 8, 3 and 5 are addends | 19 |
| `addition and multiplication properties of equality` | тэнцэтгэлийн нэмэх болон үржүүлэх чанар | printed in italics inside the equivalent equations entry | 142 |
| `addition of whole numbers` | сөрөгбус бүхэл тоо нэмэх | printed сөрөгбус = сөрөг бус (non-negative) | 19 |
| `additive identity` | нэмэхийн нөлөөгүй тоо (тэгийн өөр нэр) | 0 is the additive identity: a+0=0+a | 19 |
| `additive inverse` | эсрэг тоо, эсрэг матриц; нэмэхийн эсрэг хоёр тоо, эсрэг тоо, сөрөг тоо | entry runs on from p.19; vectors/matrices: эсрэг элемент | 19,20 |
| `adjacent side` | налсан катет | printed in the cosine-ratio diagram, not as a headword | 90 |
| `adjoint` | хосмог, нэгтгэсэн, хосмог хувиргалт | matrix/operator sense | 21 |
| `adjust` | уялдуулах, дагуу хийх, тооцоолох, тохируулах, засварлах, засвар хийх, тоймлох | e.g. adjust the compass | 21 |
| `advanced cours` | ахиу түвшний сурах бичиг | printed 'cours' (= course) | 21 |
| `affirmation` | нотломж | logic | 22 |
| `affix` | аффикс | math sense: комплекс тоонд харгалзаж буй комплекс хавтгайн цэг | 22 |
| `aggregate of simple events` | эгэл үзэгдлийн олонлог | probability | 22 |
| `ahead, to be ahead` | хожих, давуу байх (тоглоомонд) | in games | 22 |
| `aleph` | алеф, кардинал тоо | first Hebrew letter ℵ; cardinal of an infinite set | 22 |
| `alfin` | заан (шатрын) | chess bishop | 22 |
| `algebra of events` | үзэгдлийн алгебр | probability | 23 |
| `algebra of logik` | логикийн алгебр | printed 'logik' (= logic) | 23 |
| `algebraic expression` | алгебрын илэрхийлэл, алгебрийн илэрхийлэл | book prints both -ын and -ийн spellings; printed as plural 'algebraic expressions' | 23,155 |
| `algebraic number` | алгебрын тоо | root of an integer-coefficient polynomial | 23 |
| `algebraic step` | алгебрын алхам (тэгшитгэл бодох зэргийн) | step in solving an equation | 23 |
| `all A's are B's` | Бүх A нь B | logic statement pattern | 25 |
| `almost everywhere` | бараг хааяагүй | as printed | 25 |
| `alpha` | альф, үсэгт | first Greek letter α | 25 |
| `alphabet` | цагаан толгой, цагаан топгойн үсгийн дэс дараагаар байрлуулах | 2nd sense = to alphabetize; misprint топгойн = толгойн | 25 |
| `alphabetically` | цагаан толгойн үсгээр дугаарлах | numbering а), б) etc. | 25 |
| `alternate events` | нэгдэл үзэгдэл | probability | 25 |
| `alternate exterior angles` | гадаад солбисон хоёр өнцөг | book cross-refers to the figure on p.24 | 25,156 |
| `alternate interior angles are congurent` | дотоод солбисон хоёр өнцөг тэнцүү | printed 'congurent' (= congruent) | 26 |
| `alternation` | сөөлжилт, үелж өөрчлөгдөх, дизъюнкц | logic sense: disjunction | 26 |
| `altitude drawn to the hypotenuse` | гипотенузд буулгасан өндөр | printed unbolded inside the draw entry | 128 |
| `always - falsehood` | ямагт худал | logic | 26 |
| `always - truth` | ямагт үнэн | logic | 26 |
| `amicable numbers` | нөхөрсөг хоёр тоо | e.g. 220 and 284; gloss completed on p.27 | 26 |
| `amount` | нийлбэр, хэмжээ, утга, мөнгөний дүн, мөнгөний нийт хэмжээ, мөнгөний хэмжээ, бүгд хүрэх, тэнцэх | finance sense: дүн мөнгө = principal + interest | 27 |
| `amplitude` | далайц, модул (комплекс тооны) | modulus of a complex number; амплитуд for x=Asin(wt+a) | 27 |
| `an altitude of a triangle` | гурвалжны өндөр | perpendicular from vertex to opposite side | 26 |
| `analogical inference` | адил төстэйгээр дүгнэлт хийх | printed together with "inference by analogy" | 205 |
| `analysis` | анализ, математик анализ, задлан шинжилгээ | plural analyses; entry continues on p.28 | 27 |
| `and` | ба, бөгөөд, хоёр | Олон юм тоочихдоо сүүлчийнх нь өмнө тавина; заримдаа орчуулахгүй | 28 |
| `and over or` | «ба»-г «буюу» - гаар илэрхийлэх чанар | distributive property for statements p, q, r | 124 |
| `angle bisector, bisector of angle` | өнцгийн биссектрис, өнцгийг тэнцүү хуваагч | printed as one entry | 48 |
| `angle of depression` | доошоо харах өнцөг | depression үгийн орчуулгыг хар | 29 |
| `angle of elevation` | дээшээ харах өнцөг | elevation үгийн орчуулгыг хар | 29 |
| `angle-chasing` | өнцөг хөөх | Евклидийн геометрт өнцгүүдийг тооцоолох арга | 29 |
| `annex a zero to` | … –ын ард тэг бич | жишээ: 1,3–ын ард тэг бич | 29 |
| `annotation` | товч танилцуулга (өгүүлэл, ном, гар бичмэлийн) | Өгүүлэл, ном, гар бичмэлийн | 29 |
| `answer following` | дараах асуултанд хариул | Номд 'the' үггүй хэвлэгдсэн (= answer the following) | 30 |
| `antecedent` | эхний гишүүн, өмнөх | Логикт (p ⇒ q)-ийн p нөхцөл | 30 |
| `anticosine` | арккосинус | cos⁻¹x | 30 |
| `anticotangent` | арккотангенс | ctg⁻¹x | 30 |
| `antisine` | арксинус | sin⁻¹x | 30 |
| `antitangent` | арктангенс | tg⁻¹x | 30 |
| `anywhere` | хаа нэг, аль нэг | Зарим үед орчуулахгүй | 31 |
| `apothem` | апофем | Зөв олонөнцөгтийн төвөөс талд нь буулгасан перпиндикуляр хэрчим | 31 |
| `apper bound` | дээд хил (4,55) | apper as printed; typo for upper | 49 |
| `applicate axis` | босоо тэнхлэг (огторгуйд) | z-axis in 3D space; (огторгуйд) = in space | 42 |
| `applications of diffentiation` | уламжлалын хэрэглээ | printed "diffentiation", typo for differentiation | 115 |
| `arabic system` | араб тооллын систем | 0,1,2,...,9 цифр ашиглан тоо бичдэг систем | 33 |
| `arc cosine` | арккосинус; арк косинус | cos⁻¹x | 33,90 |
| `arc cotangent` | арккотангенс | ctg⁻¹x | 33 |
| `arc secant` | арксеканс | sec⁻¹x | 33 |
| `arc sine` | арксинус | sin⁻¹x | 33 |
| `arc tangent` | арктангенс | tg⁻¹x | 33 |
| `Archimedes` | Архимед | МЭӨ 287-212 он | 34 |
| `are` | ар | Талбайн нэгж; 1a = 100 м² | 34 |
| `Argand diagram` | Аргандын диаграмм | a+bi тоог (a,b) цэг болгон дүрсэлсэн зураг | 34 |
| `argumentum` | баталгаа | Латин үг | 34 |
| `Aristotelian` | Арестотелийн | Номд ийнхүү хэвлэгдсэн; доор нь Аристотелийн гэж бичсэн | 34 |
| `arithmetic` | арифметик, арифметикийн үйлдэл | 'арифметик дундаж' нь arithmetic mean-д хамаарна | 34 |
| `armithmetic series` | арифметик цуваа (арифметикийн прогрессээс зохиосон цуваа) | printed 'armithmetic' (= arithmetic) | 35 |
| `arrangement of n elements taken m at a time` | n элементээс нэг, нэгээр авсан m элементийн байрлал, n элементээс авсан (сонгосон) m элементийн байрлал, n элементийн m элементэй гүйлгэмэл | combinatorics: arrangements of m out of n | 36 |
| `arrow` | сум | vector/segment arrow | 36 |
| `artificial exersize` | зохиомол (нүсэр төвөгтэй) дасгал | printed spelling; = artificial exercise | 37 |
| `Artistotle` | Аристотель (МЭӨ 384-322 он) | printed 'Artistotle' (= Aristotle) | 34 |
| `as follows` | доорх мэт, дараах (доорх) байдлаар, зохих есоор | book prints есоор; apparent typo for ёсоор | 164 |
| `as soon as` | -нгуут | verbal suffix | 38 |
| `ASA rule` | гурвалжны тэнцүүгийн өнцөг тал өнцгийн (ӨТӨ) шинжийн дүрэм, ӨТӨ шинж | angle-side-angle triangle congruence | 38 |
| `associative` | бүлэглэх | of an operation: бүлэглэх чанартай | 39 |
| `Assume that the statement is true for n=k.` | n=k үед нотломжоо үнэн гэж үзье | induction | 39 |
| `Assume the contrary.` | Эсрэгийг нь биелнэ гэж үзье | proof by contradiction | 39 |
| `assumption (1) leads to a conradiction` | (1) эсрэг дүгнэлт нь зөрчилд хүргэлээ | printed "conradiction" for contradiction | 39 |
| `at` | -аар (-ээр), -д (-т), -дахь, -аас (-ээс) | зарим үед орчуулахгүй - sometimes left untranslated | 40 |
| `atomic proposition` | дан хэллэг, энгийн хэллэг | logic | 41 |
| `attack` | бодолт, бодох арга, бодож эхлэх | of a problem | 41 |
| `augend` | эхний нэмэгдэхүүн | first addend in an addition | 41 |
| `automaton` | автомат | plural: automata | 41 |
| `awkward` | нүсэр (илэрхийлэл) | of an expression; sense marker (илэрхийлэл) = of an expression | 42 |
| `axiamatic conception` | аксиомын үзэл санаа | printed "axiamatic"; typo for "axiomatic" | 75 |
| `azimuth` | азимут (хөдөлгөөний өгсөн чиглэл, хойд зүг хоёрын хоорондох өнцөг) | хөдөлгөөний өгсөн чиглэл, хойд зүг хоёрын хоорондох өнцөг | 42 |
| `b` | мэдэгдэж байгаа тоо, хэмжигдэхүүний тэмдэглэл | symbol for a known number or quantity; мэдэгдэж байгаа тоо, хэмжигдэхүүний тэмдэглэл | 42 |
| `back` | ар, ар тал, урвуу, урвуу чигпэл, өмнө, буцах, эргэн үзэх, ахин авч үзэх, дэмжих | "чигпэл" as printed; read чиглэл; чигпэл printed for чиглэл (typo) | 42 |
| `bar chart` | баганан диаграмм | given in the histogram entry | 43,59,188 |
| `barrel` | торх, торхонд хийх (шингэнийг), баррел (шингэн хэмжих нэгж) | 1 баррел = 163,65 л (Англид), 119 л (Америкт); 1 баррел = 163,65 л (англид), 119 л (америкт) | 43 |
| `base of system of nymeration` | тооллын системийн суурь | nymeration as printed; typo for numeration | 44 |
| `BASIC` | микрокомпьютер эхлэн суралцагчийн программын хэл | expands Beginners All purpose Symbolic Instruction Code | 44 |
| `Bayesion` | Байесийн | Bayesion as printed; typo for Bayesian | 44 |
| `Bayes's theorem, Bayes' formula` | Байесийн томьёо (магадлалын) | printed as one entry; магадлалын = of probability | 44 |
| `Baysesian formula` | Байесын (Бейсийн) томьёо | printed Baysesian; typo for Bayesian | 166 |
| `behaviour` | төлөв байдал, төлөв, онцлог, өөрчлөлтийн онцлог | variant behavior noted; marked (Англид) | 45 |
| `belonging` | харъяалагдах, харъяалагдаж байна | printed with ъ (харъяалагдах) | 45 |
| `bends upwords` | параболын салаа нь дээшээ харсан | upwords as printed; typo for upwards | 45 |
| `bent` | нугалсан | bend үйл үгийн өнгөрсөн цаг | 45 |
| `Bernoulli inequaiity` | Бернуллийн тэнцэтгэлбиш | book typo: "inequaiity" for "inequality" | 204 |
| `best answer` | зөв хариу (сорилын) | сорилын = of a test | 45 |
| `beta` | бета | грек цагаан толгойн үсэг: β | 45 |
| `betweenness of points` | хоёр цэгийн хооронд орших нь | entry runs across pages 45-46 | 45 |
| `beyond F4F4` | F4F4-өөс цааших | subscripts printed as F with subscript 4 | 46 |
| `biconditional implication` | давхар импликац, эквиваленц | (p⇔q) | 196 |
| `binary numbers` | хоёртын тооллын системийн тоо | жишээ: 1101_two = 5_ten (1101_хоёр = 5_арав) as printed | 47 |
| `binomial coefficient` | биномын коэффициент, хоёргишүүнтийн n зэргийн задаргааны коэффициент; хоёргишүүнтийн (биномын) задаргааны коэффициент | C_{n,k} = C_n^k = n!/(k!(n–k)!), n≥k≥0 | 47,66 |
| `binomial formula` | биномын томъёо; хоёргишүүнтийг натурал зэрэг дэвшүүлэх томьёо, Ньютоны бином | томъёо printed with ъ | 47,166 |
| `bit` | 0,1 хоёр цифр, ТБЭМ-ын үндсэн нэгж, хоёртын, хоёр оронт | ТБЭМ = computer | 48 |
| `blackboard, board` | самбар | printed as one entry | 48 |
| `block, blocs` | бүлэг, цуглуулга, бүлэг элемент | printed as one entry | 49 |
| `borrow` | зээлэх (хасахад) | хасахад = in subtraction | 49 |
| `bottom line` | доод мөр (хүснэгтийн) | хүснэгтийн = of a table | 49 |
| `bound` | хил хязгаар, зааг, талс, зааглах, хязгаарлах, холбоотой, холбогдсон | жишээ: 4.45 ≤ x ≤ 4.55 | 49 |
| `bracket (brakets)` | бага хаалт буюу дөрвөлжин хаалт | plural printed "brakets" - typo for "brackets" | 50 |
| `c` | (мэдэгдэж буй хэмжигдэхүүний тэмдэглэл) | symbol c; gloss printed in parentheses | 51 |
| `calculus` | тоолол, математик анализ, дифференциал тоолол, интеграл тоолол | plural calculi given in the entry | 52 |
| `can (could)` | 1. чадах, болох. 2. бидоон (сав) | sense 2 is the noun can, a container | 52 |
| `cancellation rule` | Энгийн бутархайг хураах дүрэм k≠0, ka/kb=a/b | printed with the formula ka/kb = a/b, k≠0 | 53 |
| `caolition` | холбоо | printed "caolition" - typo for "coalition" | 53 |
| `Cartesian coordinate system, coordinate system in plane` | хавтгай дээрх декартын координатын систем | entry runs from page 53 onto page 54 | 53 |
| `Cartesion equation of a plane` | Огторгуй дахь декартын координатын системийн хавтгайн тэгшитгэл | printed "Cartesion"; formula Ax+By+Cz+D=0; spans pages 54-55 | 55 |
| `Cartesion plane` | Декартын хавтгай | printed "Cartesion" - typo for "Cartesian" | 54 |
| `categorical proposition` | айн хэллэг | printed with the domain label (логик), i.e. logic | 55 |
| `CCW-counter clockwise` | цагийн зүүний эсрэг, нар буруу | CCW = counter clockwise | 65 |
| `center, centre` | төв, дундаж | label (Англид) marks centre as the British spelling | 55 |
| `center radius–form of the eqiation of a circle` | тойргийн төв, радиустай тэгшитгэл [(x–h)² + (y–k)² = r²] | printed "eqiation" - typo for "equation" | 56 |
| `centerfugal` | төвөөс зугтах | printed "centerfugal"; entry also gives "centrifugal" | 56 |
| `centimeter (centimetre)` | сантиметр, центметр | "центметр" as printed - apparent typo | 56 |
| `Ceva's Theorem` | Чевагийн теорем | stated twice, in two equivalent forms | 57 |
| `chain of arcs` | ирмэгийн гинж | graph theory; marked (граф) | 58 |
| `chain rule` | гинжин дүрэм, давхар функцийн уламжлал авах дүрэм; гинжин дүрэм, импликацын дамжих чанар | calculus sense; formula (f(g(x))' = f'(g(x))g'(x)) printed; logic sense: transitivity of implication | 58 |
| `Change 0.345 to a fraction` | 0,(345)-ыг энгийн бутархай болго | 0.345 printed with repeating-decimal overbar | 58 |
| `change 30 kilometers to meters` | 30км–ийг метрээр илэрхийл, 30 км–ийг метрээр соль | printed with (30km=□m) | 58 |
| `chi` | хи | Greek letter χ | 60 |
| `Chinese remainder theorem` | Хятадын үлдэгдлийн тухай теорем | body text spells it Хятадын үлдэгдэлийн тухай теорем | 60 |
| `cinq` | тавын тоо, таван оноо | of cards or dominoes: (хөзөр, даалуу гэх мэт) | 62 |
| `circular measere` | өнцгийн радиан хэмжээ | printed "measere"; typo for "measure" | 62 |
| `circular rung` | дугуй цагираг | printed "rung"; apparently a typo for "ring" | 62 |
| `circulus vitiosus` | эргүүлэг, баталгааны алдаа | Latin; vicious circle | 62 |
| `circumscribes` | багтаасан | in "One geometric shape circumscribes another"; bold Mongolian багтаасан дүрс | 63 |
| `circumscribing a circle about a traingle` | гурвалжин багтаасан тойрог зурах | printed "traingle"; typo for "triangle" | 63 |
| `class bounderies` | ангийн хил | printed "bounderies"; typo for "boundaries"; headword split across p.63-64 | 64 |
| `class intervals` | завсарын анги | in "groups called class intervals" | 63 |
| `classes` | анги | in "divide the data into groups, called classes" | 63 |
| `closed interval` | битүү завсар | set form {x\|a ≤ x ≤ b} | 65,213 |
| `closure property of addition (a+b is unique element in R)` | нэмэхийн битүү чанар | parenthetical rendered (a+b нь R дэх цорын ганц элемент) | 65 |
| `collision` | зөрчил, мөргөлдөөн (магадлал) | (магадлал) marks the probability sense | 67 |
| `column of demerminant` | тодорхойлогчийн багана | printed "demerminant"; book typo for "determinant" | 67 |
| `combination of n objects taken r at a time` | n элементээс нэг нэгээр нь r элемент авсан r элементтэй хэсэглэл, n элементээс авсан r элементтэй хэсэглэл | headword begins at the foot of p.67 as "combination of" | 68 |
| `combination of n things r at a time` |  | only a Russian equivalent is printed; no Mongolian given | 67 |
| `command` | команд (ТБМ), тушаал, тушаах, командлах, дарга, захирагч | entry runs over onto p.69; (ТБМ) marks the computing sense | 68 |
| `commenly` | ер нь, ерөөс | printed "commenly"; book typo for "commonly" | 69 |
| `common difference` | арифметик прогрессийн ялгавар | Арифметик прогрессийн дараалсан хоёр гишүүний ялгавар | 35,69 |
| `common multiple` | еренхий хуваагдагч | printed "еренхий"; book typo for "ерөнхий" | 69 |
| `common ratio` | геометр прогрессийн хуваарь | of a geometric progression | 69,178 |
| `complement of a event` | -ийн эсрэг үзэгдэл | printed "a event"; book typo for "an event" | 70 |
| `complement of a set F` | F олонлогийн гүйцээлт | entry also gives F'={x\|x∈U and x∉F} | 70 |
| `completely defined` | хааяагүй тодорхойлогдсон | printed "хааяагүй"; apparently a typo | 103 |
| `composite of two reflextions` | тэнхлэгийн хувь дахь хоёр тэгшхэмийн угсраа хувиргалт (композиц) | printed "reflextions"; book typo for "reflections" | 73 |
| `compound statement` | нийлмэл хэллэг, нийлмэл нотломж | forms listed: p ба q, p буюу q, хэрэв p бол q, p биш | 74 |
| `concave figura` | хотгор дүрс | printed "figura"; typo for "figure" | 74 |
| `concept content` | ухагдахууны агуулга | marked (logic) | 81 |
| `conception` | 1. ухагдахуун, төсөөлөл, үзэл санаа, үзэл бодол. 2. ухагдахуун, үзэл санаа үүсэх (төлөвших) явц. 3. зарчим, систем | three numbered senses | 75 |
| `conclusio ad absurdum` | дүгнэлт, эсрэгээс нь баталсан баталгаа | Latin | 76 |
| `conclusion` | дүгнэлт, оюун дүгнэлт, гаргалгаа, мөрдлөг, төгсгөл, үр дүн | the q clause of a compound «if p, then q» statement | 76 |
| `conditio sine qua non` | зайлшгүй нөхцөл | Latin | 77 |
| `conditional equation` | нөхцөлт тэгшитгэл | book adds: шийдийн олонлог нь хоосон бус, адилтгал бус тэгшитгэл | 140 |
| `conditional statements` | нөхцөлт хэллэг (нотломж) | entry runs on to p.77: «if p, then q» хэллэг | 76 |
| `conflict` | мөргөлдөөн (тоглоомын онол) | game theory | 77 |
| `confortable` | харгалзах, харгалзсан | printed "confortable"; typo for "conformable" | 77 |
| `conjugate imaginarys` | хосмог комплекс тоо | printed imaginarys; typo for imaginaries | 196 |
| `conquer` | хожих (тоглоомын онол) | game theory | 79 |
| `consecutive interior angles` | дотоод өрөөл хоёр өнцөг | in the figure angles 7,2 and 8,1 | 79 |
| `consequent` | 1. хуваарь (харьцааны хоёр дахь тоо) 2. пропорцын хоёр дахь гишүүн 3. консеквент ((p ⇒ q)–ийн q) | three numbered senses | 80 |
| `constancy, constant` | тогтмол тоо, тогтмол хэмжигдэхүүн, коэффициент | printed as one headword pair | 80 |
| `content` | 1. агуулга; 2. талбай, эзлэхүүн, багтаамж, урт | two numbered senses | 81 |
| `continuons on the left` | зүүн тасралтгүй | printed "continuons"; typo for "continuous" | 81 |
| `continuous quantities` | тасралтгүй хэмжигдэхүүн | plural form of continuous quantity | 82 |
| `contra` | эсрэг | marked (лат) = Latin | 83 |
| `contradiction` | зөрчил, харшил, няцаалт; зөрчилт тэгшитгэл | second sense: equation false for every value of the variable | 83 |
| `contraposition` | урвуугийн эсрэг импликац | domain marker printed: логик (logic) | 83 |
| `contraposition implication` | урвуугийн эсрэг импликац | (q̄ ⇒ p̄) | 196 |
| `convenience` | зохистой, тохиромжтой | printed jointly as one entry: convenience, convenient | 84 |
| `convenient` | зохистой, тохиромжтой | printed jointly as one entry: convenience, convenient | 84 |
| `converse implication` | урвуу импликац | (q⇒p) | 196 |
| `convex figura` | гүдгэр дүрс | book prints "figura" for "figure" | 85 |
| `convex upward` | гүдгэр | cross-reference: definition of гүдгэр graph given under concave | 86 |
| `coordinate` | 1. координат; 2. зохицуулах, уялдуулах | sense 1 noun, sense 2 verb | 86 |
| `coordination` | зохицуулалт, уялдуупалт | book prints "уялдуупалт" for "уялдуулалт" | 87 |
| `corallary fact` | мөрдлөг | book prints corallary; typo for corollary | 157 |
| `corner point` | оройн (булангийн) цэг | domain marker printed: шугаман програмчилал (linear programming) | 87 |
| `corollary` | мөрдлөг, дүгнэлт, гаргалгаа (логикт), үр дүн | marked (лат) = Latin; гаргалгаа marked as logic sense | 88 |
| `correlation coefficcient` | корреляцын коэффициент | book prints "coefficcient" for "coefficient" | 88 |
| `corresponding ponts` | харгалзах хос цэг | book prints "ponts" for "points" | 89 |
| `cosecant, cose` | косеканс | abbreviation printed as "cose"; standard form is cosec | 90 |
| `cosine formula` | косинусын томъёо | printed "томъёо" with ъ; standard spelling is томьёо | 90 |
| `coupled of points` | хос цэг | printed "coupled of points"; apparently for couple of points | 92 |
| `Cramer's rule for 3×3 Systems` | Гурван хувьсагчтай гурван шугаман тэгшитгэлийн систэм бодох Крамерийн дүрэм | printed "систэм" here, "систем" in the 2x2 entry | 92 |
| `credibility` | итгэл | domain marker "(статистик)" printed after the gloss | 93 |
| `criterion (criteria)` | шалгуур, шинж, шинжүүр, түлхүүр үг | plural criteria given in the entry | 93 |
| `cross product` | хэрээс үржвэр | worked example printed: 4,0/2,1 = 3,5/2,4 | 94 |
| `cross-section` | хөндлөн огтлол, огтлогч хавтгай | gloss continues onto page 94 | 93 |
| `cubernetics` | кибернетик | printed "cubernetics" for cybernetics | 95 |
| `cuboid` | тэгш өнцөгт параллелепепид, нэг оройгоос гарсан гурван ирмэг нь хос хосоороо перпендикуляр тетраэдр | printed "параллелепепид"; spelled "параллелепипед" two lines later | 95 |
| `cutting` | 1.огтлол 2. таслах (цуваа) 3. хөзөр сугалах. 4. хураах, бууруулах | numbered senses as printed | 96 |
| `cyclic quadrilateral` | багтсан дөрвөнөнцөгт | printed as one word дөрвөнөнцөгт | 96 |
| `cypher (cipher)` | цифр, тооны тэмдэг, тэг,шифр, кодлох, шифрлэх, тооцоолох | printed "тэг,шифр" without a space | 97 |
| `d` | мэдэгдэж байгаа хэмжигдэхүүний тэмдэглэл | whole gloss printed in parentheses | 97 |
| `data` | 1. мэдээ (тоон), мэдээлэл (тоон), баримт. 2. үзүүлэлт 3. хэмжсэн хэмжигдэхүүн, үр дүн | entry notes [datum–ын олон тоо; ганц тоо мэт хэрэглэдэг] | 97 |
| `data handling` | мэдээний анхан шатны боловсруулалт, мэдээнд анхан шатны боловсруулалт хийх | entry runs over onto p.186 | 185 |
| `date` | сарын өдөр, сар өдөр, он сар, хугацаа, он сар өдөр тогтоох, үе, хугацаа | two senses: calendar date; span of time | 98 |
| `datum (data)` | өгсөн хэмжигдэхүүн, тооллын эхлэл (эх), үзүүлэлт, баримт буюу мэдээ | four numbered senses | 98 |
| `deal (dealt)` | авч үзэх, тараах (хөзөр), тоо хэмжээ, хувь | first sense marked (хөзөр), of cards | 98 |
| `dealer` | тараагч (хөзөр) | (хөзөр) = of cards | 98 |
| `deca` | арав, арван | prefix: "deca-" нь арав гэсэн утгатай угтвар | 98 |
| `decade` | арав, аравт, аравтын (арвын) орон, аравтын, арван жил | three numbered senses | 98 |
| `deceleratiag at constant rate` | хурдын тогтмол удаашралт | printed "deceleratiag"; typo for decelerating | 98 |
| `decelerating` | сааралт, удаашрал саарах, буурах, удаашрах | comma missing after удаашрал as printed | 98 |
| `deci` | арваны нэг, 0,1 | prefix: deci- нь аравны гэсэн утгатай угтвар | 99 |
| `decillion` | 10³³ эрхэт (АНУ), 10⁶⁰ хэмжээлшгүй (Их британи) | US and British values differ | 99 |
| `decimalize` | аравтын тооллын системд шилжүүлэх, энгийн бутархайг аравтын бутархай болгох | two numbered senses | 100 |
| `decimally` | аравтын тооллын системд, аравтын бутархай хэлбэр (ээр) | two numbered senses | 100 |
| `decimation` | арав дахь юм бүрийг зайлуулах, арав дахь юм бүрийг сонгох | two numbered senses | 100 |
| `decimeter` | метрийн аравны нэг | given inside the deci entry | 99 |
| `decision variables` | шийдэх хувьсагчтай (шугаман програмчилал) | linear programming | 100 |
| `deck` | багц (хөзөр) | (хөзөр) = of cards | 100 |
| `decompose` | үржигдэхүүн болгон задлах, үржвэр болгох, нийлбэр болгох | entry runs over onto page 101 | 100 |
| `Deductive reasoning, a logical sequence of steps that a justified by postulates, theorems, and definitions, is the process usually employed to prove mathematical statements.` | Математикийн хэллэг батлах үйл ажиллагааны постулат (аксиом), теорем, тодорхойлолт ашиглан нотлох алхамын логик дараалал нь дедукц ургуулан бодолт юм | printed "that a justified"; typo for that are justified | 102 |
| `defeat` | ялах, хожих (тоглоомын онол) | game theory | 103 |
| `define` | тодорхойлох, тодорхойлолт томьёолох, хилийг нь тогтоох, хязгаарлах | two numbered senses | 103 |
| `deflate` | 1. эрэмбэ бууруулах (матрицын), 2. шавхан дуусах (алг), 3. хураангуйлж хуваах (олонгишүүнт), буурах, бууруулах (үнэ) | three numbered senses: matrix; algorithm; polynomial and price | 106 |
| `degree of the polynominal 0 has no degree` | тэггишүүнт зэрэггүй | printed "polynominal"; typo for polynomial | 106 |
| `degrees Fahrenheit` | Фарангейтийн градус (хуваарь) | formula printed: F=9/5• C + 32 | 159 |
| `deka-` | арав гэсэн утгатай угтвар | prefix meaning ten | 106 |
| `delineatoin` | зураг, төлөвлөгөө, дүрслэл | printed "delineatoin"; typo for delineation | 107 |
| `delta` | делт, хэмжигдэхүүний маш бага өөрчлөлт тэмдэглэдэг үсэг | Greek alphabet letter Δ, δ | 107 |
| `demerminer` | тодорхойлогч үзэгдэл (магадлалд) | printed "demerminer"; typo for determiner | 111 |
| `denial` | үгүйсгэл | logic | 107 |
| `dependent variable` | хамаарах хувьсагч; хамааран хувьсагч | output | 108,172,173 |
| `dependent variables` | хамаарах хувьсагч | bold inside the independent-variable example | 200 |
| `derivation` | 1. гаргалгаа (логик), гаргах (томьёо), 2. уламжлал авах | sense 2 = differentiation | 109 |
| `descend` | буух, уруудах, доошлох, буурах, ерөнхийгөөс тухайд шилжих, уламжлах | entry runs over onto page 110 | 109 |
| `determinant` | тодорхойлогч | of a matrix | 110 |
| `determinant of second order` | хоёрдугаар эрэмбийн тодорхойлогч | given as \|a b; c d\| = ad-bc | 111 |
| `diagnosis (diagnoses)` | оношлогоо, оношлолт, алдаа илрүүлэх, оношлох | diagnoses is the plural | 112 |
| `diamond` | 1. ромбо, 2. ромбо хэлбэртэй дүрс, 3. бундан (хөзөр) | sense 3 printed with bold "diamond" repeated; card suit | 113 |
| `difference of squares formula` | квадратын ялгаврын томьёо | a2-b2=(a-b)(a+b) | 113 |
| `difference of two cubes` | хоёр кубийн ялгавар [(x³–y³)] | given as a3-b3 | 94,113 |
| `difference of two squares` | квадратын ялгавар | given as a2-b2 | 113 |
| `digital device` | цифрэн төхөөрөмж | entry runs over onto page 112 | 111 |
| `dijital arithmetic` | тооны арифметикийн үйлдэл | Номд dijital гэж хэвлэгдсэн | 35 |
| `direct implication` | шууд импликац | (p⇒q) | 196 |
| `disjuntive` | дизъюнкцын, дизъюнкц | printed "disjuntive", typo for disjunctive | 120 |
| `dissymmetry` | тэгшхэмгүй, тэгшхэмгүй болох (нь), толины тэгшхэм | entry runs over onto p.123 | 122 |
| `distance` | зай, завсар, зам, хазайлт, ялгааны хэмжээ | sense 1 зай, завсар, зам; sense 2 хазайлт, ялгааны хэмжээ | 122 |
| `distinct` | тов тодорхой, тод, эрс тод илэрхийлсэн, ялгаатай, онцгой, үл давхцах | sense 2 is ялгаатай, онцгой, үл давхцах | 123 |
| `distinguished` | тэмдэглэсэн, ялгасан, гарамгай нэрт | sense 2 is гарамгай нэрт | 123 |
| `distribtion of primes` | анхны тооны тархалт | printed distribtion; typo for distribution | 123 |
| `distribution` | тархалт (магадлал, статистик), хуваарилалт | тархалт marked for probability and statistics | 123 |
| `distributive property of multipication over addition` | үржвэрийг нийлбэрээр илэрхийлэх чанар | printed multipication; typo for multiplication | 123 |
| `distributive property of multipication over substraction` | үржвэрийг ялгавраар илэрхийлэх чанар | printed multipication, substraction; both typos | 123 |
| `divide` | хуваах, хуваагдах, бүхэл хуваагдах, жижиглэн хуваах, бутаргах | sense 2 is жижиглэн хуваах, бутаргах | 124 |
| `dividend` | хуваагдагч | printed as the pair dividend, divident | 125 |
| `divident` | хуваагдагч | printed beside dividend; apparent typo variant | 125 |
| `dividers` | хэмжигч гортиг | drawing dividers/compasses | 125 |
| `dividing fractions, division of fractions` | энгийн бутархайг хуваах | two variants printed on one line | 167 |
| `division` | хуваах, хуваалт, үлдэгдэлгүй хуваах, үлдэгдэлгүй хуваагдаж байгаа | sense 2 is үлдэгдэлгүй хуваах | 125 |
| `division algorithm` | үлдэгдэлтэй хуваахын теорем; үлдэгдэлтэй хуваах теорем | a = b·q + r, 0 <= r < b; Mongolian theorem name Үлдэгдэлтэй хуваах теорем | 24,125 |
| `division rule for positive indices` | эерэг илтгэгчтэй зэрэг хуваах дүрэм (тодорхойлолт) | Mongolian printed at top of p.126 | 125 |
| `do (did, done)` | хийх, гүйцэтгэх, дуусгах, төгсгөх, дюжина (арван хоёртын тооллын системд) | sense 3 дюжина = dozen, base twelve | 126 |
| `dodecagon` | арванхоёрөнцөгт | (сүүлийн гурван зураг) = the last three figures | 126 |
| `dodecahedron` | арванхоёрталст | (эхний зураг) = the first figure | 126 |
| `domain` | муж, тодорхойлогдох муж, тодорхойлсон муж, завсар (интервал) | sense 2 is завсар (интервал); rendering taken from the parallel Mongolian definition | 126,170 |
| `dominance` | тэргүүлэх, манлайлах давуу, илүү | (тоглоомын онол) game theory | 127 |
| `dominate` | тэргүүлэх, манлайлах | (тоглоомын онол) game theory | 127 |
| `dot` | цэг, цэг тавих, тасархай шугам татах, тасархай шугамаар тэмдэглэх | sense 2 is тасархай шугам татах | 127 |
| `dotted` | цэгийн, цэгэн, тасархай шугам | sense 2 is тасархай шугам | 127 |
| `double` | давхар, хоёр дахин, хоёрлох (хоёр удаа авах), хоёулаа, хоёроор үржүлэх, хоёр дахин өсгөх | printed үржүлэх, not үржүүлэх | 127 |
| `double angle formulae` | давхар өнцгийн томьёонууд | e.g. sin2A=2sinAcosA | 128 |
| `double inequality` | давхар тэнцэтгэлбиш: a≤x≤b; давхар тэнцэтгэл биш | printed as double inequality: a≤x≤b; of the form a<x<b; Mongolian printed as two words | 127,204 |
| `double the origin a number n` | Эх тоо n-ийг хоёроор үржүүл | English printed exactly so; wording garbled in the book | 128 |
| `down` | доошоо чиглэсэн, доошоо, эцэс (төгсгөл) хүртэл | sense 2 is эцэс (төгсгөл) хүртэл | 128 |
| `draught` | хүү (даам) | the game of draughts | 128 |
| `draw (drew, drawn)` | хайна, тэнцээ, зурах, татах, босгох, дүгнэлт гаргах (хийх), гаргалгаа хийх, хөзөр сугалах, шодох, буулгах (перпендикуляр) | five numbered senses in the entry | 128 |
| `drawing` | шугам зураг, зураг, схем, дүрслэл, түүвэр (статистик), сонгох, сугалах, дүгнэлт гаргах | түүвэр marked for statistics | 128 |
| `e` | e тоо, неперийн тоо, натурал логарифмын суурь | heads the letter E section | 129 |
| `e contra` | урвуугаар, эсрэгээр | marked (лат) = Latin | 83 |
| `Earth's axis` | дэлхийн тэнхлэг | book gloss: дэлхийн бөмбөрцөгийн хойт, урд туйлыг холбосон хэрчим; зургийн NS хэрчим | 130 |
| `Egyption numeration system` | Египетийн тооллын (тоо бичих) систем | printed 'Egyption'; typo for Egyptian | 131 |
| `either a=b or a>b or a<b` | эсвэл a=b эсвэл a>b эсвэл a<b | book adds: (a=b, a<b, a>b гурвын нэг нь биелнэ) | 131 |
| `elapced time` | зарцуулсан хугацаа, явсан цаг | printed 'elapced'; typo for elapsed | 131 |
| `element` | элемент, бүрэлдэхүүн, бүрэлдэхүүн хэсэг, схем, байгууламж, эхлэл | three numbered senses in the book | 131 |
| `element that belong to both set A and B` | A,B хоёр олонлогт хоёуланд нь харьяалагдаж буй элемент | belong as printed; typo for belongs | 49 |
| `elements` | суурь, анхан шатны мэдлэг, үндэс (шинжлэх ухааны) | plural sense: rudiments of a science | 131 |
| `elimination` | зайлуулах (үлмэдэгдэхийг), холтгох, холдуулах | two numbered senses in the book | 132 |
| `end` | төгсгөл, эхлэл, төгсгөлийн, төгсөх, зах, хил, хилийн | two numbered senses in the book | 134 |
| `enlargment` | сунгалт | printed 'enlargment'; typo for enlargement | 134 |
| `ensemble` | олонлог, бүлэг, систем, цуглуулга, түүвэр (стат), ансамбль | four numbered senses; стат = statistics | 135 |
| `entire` | бүхэл, бүхлээрээ, бүрэн, бүхэл хэсгийг ялгах | two numbered senses in the book | 135 |
| `enumeration` | тоочих, тооцоо, мэдээ цуглуулах, хуулан бичих, хувилбар сонгох | two numbered senses in the book | 136 |
| `eo ipso` | түүгээр | marked (лат) - Latin | 136 |
| `epsilon` | эпсилон | грек цагаан толгойн үсэг: E, ε | 136 |
| `equals sets` | тэнцүү хоёр олонлог | printed 'equals sets'; read as equal sets | 136 |
| `equation does not out` | тэгшитгэл тохирохгүй байна | printed "does not out"; apparently for "does not hold" | 140 |
| `equation in n unknowns` | n үлмэдэгдэхтэй тэгшитгэл | printed as one word үлмэдэгдэхтэй; typo for үл мэдэгдэхтэй | 140 |
| `equation of an ellipse` | эллипсийн тэгшитгэл | printed 'equation of an Ellipse' | 133 |
| `equations involving modulus, absolute value equation` | абсолют хэмжигдэхүүнтэй тэгшитгэл | book adds: [\|x\|=3 мэтийн тэгшитгэл \|x\|=3 ⇔ x=3 буюу x=−3] | 137 |
| `equavalent systems` | тэнцүү чанартай хоёр систем | printed "equavalent"; typo for equivalent | 145 |
| `equi` | адил, тэнцүү гэсэн утгатай үгийн угтвар | a prefix denoting equality | 141 |
| `equilateral traingle` | адил талт гурвалжин | printed "traingle"; typo for triangle | 141 |
| `equipose` | тэнцвэр, тэнцүүлэх | printed "equipose"; typo for equipoise | 141 |
| `equivalent decimals` | тэнцүү аравтын бутархайнууд | book example: 0,2=0,20=0,200 | 141 |
| `equivalent fractions` | тэнцүү бутархай | book example: 2/5=4/10=6/15 | 141,167 |
| `equivalent inequaltities` | тэнцүү чанартай хоёр тэнцэтгэлбиш | book typo: "inequaltities" for "inequalities" | 204 |
| `estimate` | ойролцоо үнэлгээ, баримжаа үнэлгээ, үнэлгээ, тооцоо, үнэлэх, үнэлгээ тогтоох, боломжит утга | Book numbers three senses: 1. noun, 2. verb, 3. value | 146 |
| `eta` | эта | Greek alphabet letter; η | 147 |
| `Euclidean algorithm` | Евклидийн алгоритм | Glossed as finding the GCD of two numbers | 24,147 |
| `Euclideen elements` | Евклидийн эхлэл | printed 'Euclideen'; typo for Euclidean | 131 |
| `Euler's formula` | Эйлерийн томьёо | V + F – E = 2 for vertices, edges, faces | 148 |
| `Euler's function` | Эйлерийн функц | Written Euler's function φ (n) | 148 |
| `evaluate each of the following if a = –1, b = –2 and c=4` | Хэрэв a = –1, b = –2, c = 4 бол доорх илэрхийлэл бүрийн утгыг ол | Followed by exercises 23. 9a–5b + 4c. 24. – 4(2a + 5b) | 148 |
| `even` | тэгш, тэнцүүлэх | Book numbers two senses | 148 |
| `evenly` | тэнцүү, адил, ижил, жигд | Book numbers two senses | 149 |
| `evenness` | тэгш, тэгш болох нь, жигд | Book numbers two senses | 149 |
| `everywhere` | хааяагүй | Printed хааяагүй; typo for хаяагүй | 149 |
| `evidence` | туршилтын мэдээ, үр дүн, үндэслэл, гэрч, гэрчилгээ, баталгаа, баталгаа болох | Book numbers three senses | 149 |
| `evolution` | язгуур гаргах, хөгжил | Book numbers two senses | 149 |
| `ex adverso` | эсрэгээс нь баталсан баталгаа | Latin (лат) | 149 |
| `ex contrario` | эсрэгээс батлах баталгаа | Latin (лат) | 150 |
| `ex falso quodlibet` | худлаас юу ч гарч болно | Latin (лат) | 151 |
| `ex hypothesi` | таамаглал ёсоор | Latin (лат) | 151 |
| `exact division` | нарийн хуваах (хуваалт), бүхэл хуваагдах, үлдэгдэлгүй хуваагдах | sense 2 is бүхэл хуваагдах, үлдэгдэлгүй хуваагдах | 126 |
| `example` | жишээ, дасгал | worked-example label | 150,174 |
| `excep` | -аас бусад, -ыг оролцуулахгүйгээр, зайлуулах | Printed excep; typo for except | 150 |
| `exclude` | зайлуулах, үл авч үзэх, үл зөвшөөрөх | Second, shorter entry for this headword | 150,152 |
| `exclusive disjunction` | тусгаарлах дизъюнкц, "эсвэл" холбоостой хэллэг | English notation given as p ⊻ q | 150 |
| `exemplification` | жишээгээр тайлбарпах, тайлбар жишээ | Book numbers two senses; printed тайлбарпах, typo for тайлбарлах | 150 |
| `existense of local extrema` | орчны (завсрын) экстремум оршин байх нь | Printed existense; typo for existence | 151 |
| `existential quantifier` | оршин байхуйн квантор | Short symbol given as ∃, (∃x) | 151 |
| `expancive` | өргөтгөсөн, задалсан, дэлгэрүүлсэн | Printed expancive; typo for expansive | 153 |
| `expand the following` | Дараах илэрхийллийн хаалт нээ (дараах үржвэрийг ол); дараах илэрхийллийг үржүүл | Example a) 4(x+5); Example a) (x+3)(x+5) | 152 |
| `expection` | зайлуулах | Printed expection; typo for exception | 150 |
| `expence` | зарлага, үрлэг, үнэ | Printed expence; typo for expense | 153 |
| `explement, explementary` | гүйцээлт | headword printed as two variants on one line | 154 |
| `exploratory` | шинжлэн судлах, шинжпэх, судлах | book prints шинжпэх; apparent typo for шинжлэх | 154 |
| `exponential function properties` | Илтгэгч функцийн чанар | display heading; Mongolian rendering printed on p.155 | 154 |
| `exposition` | тодорхойлон бичих, өгүүлэх, нотломж, сэтгэмж (логикт) | sense 1: тодорхойлон бичих, өгүүлэх; sense 2: нотломж, сэтгэмж (логикт) | 155 |
| `expressis verbis` | үгчилэн | marked (лат) in the book: Latin | 155 |
| `extended form of the factor theorem` | Шугаман хуваагчийн теоремийн өргөтгөсөн хэлбэр | printed as an example phrase, not bold | 156 |
| `extension` | өргөтгөл, ерөнхийлөл, суналт, уртасгап, үргэлжлэл | book prints уртасгап; apparent typo for уртасгал | 156 |
| `externally tangent of a circles` | тойргуудын гадаад шүргэгч | English printed as of a circles in the book | 156 |
| `extra` | үүнээс гадна, нэмэлт, онцгой | marked (лат) in the book: Latin | 156 |
| `extremum (extrema)` | экстремүм, захын утга, их буюу бага утга | extrema is the plural form; extrema is the printed plural form | 157 |
| `factor out side x` | x–ийн өмнөх үржигдэхүүн | printed as two words; apparently for factor outside | 158 |
| `factored completely` | гүйцэд үржвэр болгосон | rendering taken from the example sentence | 158 |
| `factorization formulas` | үржигдэхүүн болгон задлах томьёо | printed in the worked example, not bold | 159 |
| `falce coin` | хуурамч зоос | printed "falce"; book typo for "false" | 66 |
| `fall (fall, fallen)` | уналт, бууралт, доошлолт, уруудалт, унах, буурах, доошлох, уруудах | headword printed with its past forms | 159 |
| `falsi regula` | худал дүгнэлтийн арга | Latin; f(x)=0 тэгшитгэлийн ойролцоо язгуур олох арга | 160 |
| `feasible region` | боломжит шийдийн муж (шугаман програмчилал) | linear programming | 160 |
| `feeble, feebly` | сул | two headword forms printed on one line | 161 |
| `fifthieth` | тавины нэг, тавины хувь (хэсэг), тавь дугаар, тавь дахь | book prints fifthieth; typo for fiftieth | 161 |
| `figure` | дүрс, бие (геометрийн), зураг (номын), цифр, тоо, цифрээр тэмдэглэх, тэмдэглэж буй тэмдэг, дүрслэх (графикаар); логикийн A,E,O,I нотломжийн холбоог харуулсан зураг | logic sense, given as a second figure entry | 161,162 |
| `finance` | санхүү, санхүүжүүлэх, санхүү эрхлэх, санхүүгийн шинжпэх ухаан, санхүүгийн ухаан | book prints шинжпэх; apparent typo for шинжлэх | 162 |
| `find (found)` | олох, зохиох, авах, тодруулах, илрүүлэх, хайх, тодорхойлох, тооцоолох | headword printed with its past form | 162 |
| `finding the equation of an inverse functions` | урвуу функцийн томьёо (y=f⁻¹(x)) тодорхойлох | printed functions; typo for function | 217 |
| `finiterness` | төгсгөлөг болох (нь), төгсгөлөг хязгаартай болох (нь) | book prints finiterness; typo for finiteness | 162 |
| `first coordinate` | нэгдүгээр координат (абсцисс) | gloss runs over onto p. 163 | 162 |
| `five- term` | тавангишүүнтэй | printed with a space after five-; Mongolian printed as one word | 163 |
| `five-place, five-unit` | таван оронтой | two headwords printed on one line | 163 |
| `floating decimal point` | аравтын бутархайн хөвөгч цэг (ТБЭМ) | ТБЭМ marks the computing sense | 163 |
| `focus (foci)` | фокус | foci is the printed plural form | 164 |
| `focus of a ellipse` | эллипсийн фокус | printed a ellipse; cross-ref 132-р нүүрийн зураг | 164 |
| `FOIL metod` | Хоёрхоёргишүүнт үржүүлэх арга | book prints metod, and Хоёр хоёргишүүнт without a space | 163 |
| `fold (fould)` | нугалаа, нугарапт, нугалах | book prints fould and нугарапт; typos for folded and нугаралт | 164 |
| `foot` | цэг, фуут | entry begins on p.164; book adds 1foot = 1фуут ≈ 30,5 см | 165 |
| `foot (feet)` | перпендикулярын суурь, цэгийн проекц | sense 1; the list runs on to p. 165 | 164 |
| `formula (formulae)` | томьёо, илэрхийлэл, томьёолол | plural formulae printed in the headword | 166 |
| `found` | үндэслэх, тулгуурлах үндэслэсэн, олсон, гаргасан | book brackets ["find"-ийн өнгөрсөн цаг] | 166 |
| `foundations of mathematics` | математикийн үндэслэл | gloss printed at the top of p.167 | 166 |
| `foxi` | фокус | printed 'foxi'; typo for foci (singular focus) | 132 |
| `fraction in lowes terms` | үл хураагдах бутархай | printed lowes; typo for lowest | 167 |
| `fractional power rule` | бутархай илтгэгчтэй зэргийн тодорхойлолт | x^(m/n)=(ⁿ√x)^m [n∈N, m∈Z]; gloss printed at top of p.168 | 167 |
| `frame` | 1. тооллын систем 2. координатын систем 3. түүврийн суурь 4. тайлбар | senses numbered in the book | 168 |
| `frequency` | давтамж | given in the histogram entry | 168,188 |
| `frequency polygon` | давтамжийн олонөнцөгт | printed as one word олонөнцөгт | 168 |
| `frequent, frequently` | байнга | two headwords printed on one line | 169 |
| `frequeuntly encountered functions` | байнга тохиолддог функцүүд | printed frequeuntly; typo for frequently | 169 |
| `Fs` | худлууд, худал | truth-table F entries; Mongolian uses Х (худал) | 169 |
| `function` | 1. функц 2. үүрэг, үйлчилгээ, зориулалт, ажиллах | senses numbered in the book | 169 |
| `function onto itself` | өөрий нь өөр дээр нь буулгадаг функц | book prints өөрий нь; apparent typo for өөрийг нь | 170 |
| `functions expressed by formulas` | томьёогоор илэрхийсэн функц | book prints илэрхийсэн; apparent typo for илэрхийлсэн | 170 |
| `fundamantal theorem of calculus` | тодорхой интеграл бодох үндсэн теорем (Ньютон – Лейбницийн томьёо) | printed fundamantal — typo for fundamental | 175 |
| `f(x) is increases` | f(x) өсөж байна | printed "is increases" | 200 |
| `game` | тоглоом, тоглох, санаа, төлөвлөгөө | senses 1. тоглоом, тоглох 2. санаа, төлөвлөгөө | 176 |
| `gamma` | гамма | Greek letter γ | 176 |
| `Gauss-Jordan elemination` | Гаусс Жорданы үлмэдэгдэхийг дараалан зайлуулах арга | printed elemination — typo for elimination | 176 |
| `general` | ерөнхий, гол, үндсэн, суурь, ердийн бүтэн, бүрэн, ерөнхий дүгнэлт | senses 1. and 2.; sense 2 printed on p.177 | 176 |
| `general form of the equation of a circle` | тойргийн ерөнхий тэгшитгэл | (x²+y²+cx+dy+c=0) | 177 |
| `general power rule` | зэрэгт давхар функцээс уламжлал авах ерөнхий дүрэм | ([Dₓu(x)]ⁿ=n[u(x)]ⁿ⁻¹u'(x)) | 177 |
| `general solution` | ерөнхий шийд | of a differential equation | 177 |
| `geometrical constraction` | геометрийн (геометр) байгуулалт, байгуулах бодлого | printed "constraction"; typo for "construction" | 81 |
| `geometry` | геометр, геометр байгуулалт, хэлбэр, төрх байрлал, байгуулалт, схем | senses 1./2./3. | 179 |
| `Given a conditional statement, a new statement can be formed by interchanging the hypothesis and conclusion. This new statement is called the converse of the conditional.` | Өгсөн нөхцөлт хэллэгийн нөхцөл, дүгнэлт хоёрын байрыг солиход гарсан хэллэгийг уг нөхцөлт хэллэгийн урвуу хэллэг гэж нэрлэдэг | Mongolian rendering runs over onto page 85 | 84 |
| `given line ℓ and point P not on ℓ` | Өгсөн нь: ℓ шулуун, түүн дээр үл орших D цэг | book prints D where the English has P | 179 |
| `go (went, gone)` | явах, байх, хөдлөх, болох, хийх, шилжих, тэнцэх, хөдөлгөөн | senses 1.–5. | 180 |
| `goal` | зорилго, зорилт, өгсөн хэмжигдэхүүн, тухайн түвшин | senses 1./2. | 180 |
| `grade` | зэрэг, хуваарь, градус, налалт, налалтын өнцөг, анги, ангилах, тархалтын функцийн утга | 3 senses: 1 grade/scale; 2 slope; 3 class, value of distribution function | 181 |
| `gradient formule` | өнцгийн коэффициентийн томьёо | printed "formule"; typo for gradient formula | 181 |
| `gradient of a line = slope of a line` | шулууны өнцгийн коэффициент = шулууны налалт | entry adds: "slope of a line" тайлбар хар | 181 |
| `gradient traingle` | өнцгийн коэффициентийн гурвалжин | printed "traingle"; typo for triangle; (дээрх зураг хар) | 181 |
| `graph` | график, дүрслэл, диаграмм, граф, координатын систем тогтоосон хавтгай, график байгуулах, дүрслэх, зурах, диаграмм зурах, диаграмм болгон дүрслэх; координаттай шулуун дээрх дүрслэл | column heading of the interval table; representation on a coordinate line | 182,213 |
| `graph each number on a number line` | тоо бүрийг тоон шулуун дээр дүрсэл | example printed: 5,1,-2,0,-4 | 182 |
| `graphically` | графикаар, нүдэнд харагдах, дүрслэл | 2 senses: 1 графикаар; 2 нүдэнд харагдах, дүрслэл | 183 |
| `grid` | координатын тор, шугаман тор | 2 senses: 1 координатын тор; 2 шугаман тор | 184 |
| `Guassian elimination` | үл мэдэгдэхийг дараалан зайлуулах Гауссын арга | printed 'Guassian'; typo for Gaussian | 132 |
| `guess` | таавар, таамаглал, урьдчилсан дүгнэлт, ойролцоо үнэлгээ, гэж үзэх, тооцох | 2 senses: 1 noun таавар etc.; 2 verb гэж үзэх, тооцох | 184 |
| `gyrate` | тойргоор хөдлөх, ороомог замаар хөдлөх, эргэлдэх, дугуй, гүдгэр | 2 senses; sense 2 (дугуй, гүдгэр) runs over onto p.185 | 184 |
| `half open interval` | хагас задгай завсар | set form {x\|a < x ≤ b} буюу {x\| a ≤ x < b} | 213 |
| `halving` | хагаслан хуваах, хоёр дахин ихэсгэх | "ихэсгэх" as printed, though halving reduces | 185 |
| `has a global maximum` | хамгийн их утгатай | rendering used in the worked sentence | 180 |
| `heart` | бундан (хөзөр) | playing-card suit | 186 |
| `hectare` | гектар, га (талбайн нэгж) | 1га=100а=10000м² | 187 |
| `height` | өндөр, хамгийн дээд цэг, максимум | 2 senses: 1 өндөр; 2 хамгийн дээд цэг, максимум | 187 |
| `hendecahedron` | арваннэгэн- талст | hyphen and space as printed | 187 |
| `highest common factor (HCF)` | хамгийн их ерөнхий хуваагч | printed inflected as хуваагчийг inside the example | 159,188 |
| `horizontal line` | хөндлөн шулуун | book refers to back-cover figure y = 1 | 190 |
| `horizontal parabola` | хөндлөн парабол | book refers to back-cover second figure x = y² | 190 |
| `house` | тоглоомын байшин (тоглоомын онолд), казино | game theory sense | 191 |
| `hump at integer values of x` | x-ийн бүхэл утганд үсэрч байна | book refers to y=[x] graph on p. 160 | 191 |
| `hundred thousandths` | зуумянганы нэг, зуунмянганы хувь, зуумянгадугаар, зуумянга дахь | printed with both зуумянга- and зуунмянга- spellings | 191 |
| `hyperboloid of one sheet` | нэг хөндийт гиперболоид | phrase spans pp. 191–192 | 191 |
| `hypotenuse` | гипотенуз | printed in the cosine-ratio diagram, not as a headword | 90,192 |
| `idem` | бас, мөнхүү, адилаар | Latin | 193 |
| `Identify the set to which the term belongs.` | Тодорхойлж буй нэр томьёо харьяалагдах олонлогийг тодорхойл | guideline 3 | 105 |
| `Identity equation` | адилтгал тэгшитгэл | book adds [3x+4x=5x+2x хэлбэрийн адилтгал үүсгэдэг тэгшитгэл] | 193 |
| `If a deductive argument is to succeed in establishing the truth of its conclusion, two quite distinct conditions must be met: first, the conclusion must really follow from the premises – i.e., the deduction of the conclusion from the premises must be logically correct – and, second, the premises themselves must be true. An argument meeting both these conditions is called sound.` | Хэрэв үнэнийг тогтоосон дедукц гаргалгаа доорх хоёр тэс өөр нөхцөл хангаж байвал зөв. Үүнд 1-рт, дүгнэлт нь үнэхээр эх дүгнэлтийн зөв логик мөрдлөг байх ёстой. Тодруулж хэлбэл, эх дүгнэлтээс дүгнэлт гаргасан гаргалгаа нь логикийн хувьд зөв байх ёстой. 2-рт эх дүгнэлт нь өөрөө үнэн байх ёстой. Энэ хоёр нөхцөл хангасан гаргалгаа нь зөв гаргалгаа болно | sentence begins on page 101 | 102 |
| `if not` | эсрэг тохиолдолд, урвууг нь хүчинтэй гэе | rendering ends on p. 195 | 194 |
| `If the sides of a triangle have length a, b, and c such that c²=a²+b², then the triangle is a rigth triangle.` | гурвалжны гурван талын урт a, b, c-гийн хувьд: хэрэв c²=a²+b² бол уг гурвалжин тэгш өнцөгт гурвалжин | book prints "rigth" for "right" | 85 |
| `ill-designed` | хангалтгүй төлөвлөсөн | statistics | 195 |
| `imaginary part` | комплекс тооны хуурмаг хэсэг | Im (a + bi) | 72,196 |
| `imcomparable` | жишигдэхгүй | printed imcomparable; typo for incomparable | 196 |
| `imcomparably` | жишишгүй | printed imcomparably; typo for incomparably | 196 |
| `implicit equaton` | далд функцийн тэгшитгэл | printed equaton; typo for equation; e.g. 3x–2y+4 = 0 | 196 |
| `in-` | арын үгээ үгүйсгэсэн утгатай болгодог угтвар | negating prefix; book cites inequality | 197 |
| `in a simple space` | түүвэр огторгуйд | printed "simple"; sense is sample space | 198 |
| `in abstracto` | хийсвэр, ерөнхийдөө | Latin | 198 |
| `in corpore` | бүрэн хэмжээгээр | Latin | 199 |
| `in medias res` | хэргийн учир, мөн чанартаа | marked (лат), i.e. Latin | 206 |
| `In order to establish a statement in a deductive system, you must show that the statement is a logical consequence of some previously established statements.` | Онолын тогтолцоонд хэллэг үнэн болохыг тогтоохын тулд тухайн хэллэгийг өмнө үнэн болохыг тогтоосон хэллэгийн логик мөрдлөг болохыг харуулах ёстой | sentence begins "In order" on page 102 | 103 |
| `in residuo` | үлдэгдэл | marked (лат), i.e. Latin | 207 |
| `inch` | инч, дюйм | английн уртыг хэмжих нэгж; 1инч=1дюйм=2,54см | 198 |
| `incommensurable` | харилцан хэмжилгүй | equivalent printed only inside the example sentence | 199 |
| `inconsistence, inconsistency` | 1. зөрчилтэй болох (нь), үл нийцэх (нь) 2. үл тохирох, уялдаагүй болох (нь), зөрчил | two numbered senses | 199 |
| `incorrect solution` | илүү шийд | printed илүү; apparently a typo for буруу | 200 |
| `independent variable` | үлхамааран хувьсагч; үлхамаарах хувьсагч | printed үлхамааран as one word; input; printed as one word; variant spelling on this page; also printed үл хамааран; printed as one word үлхамаарах | 172,173,174,200 |
| `indexing` | 1. индекслэх 2. дугаарлах 3. тойргийг хэсгүүд болгох | three numbered senses | 201 |
| `indirect reasoning` | дам ургуулан бодолт, дам баталгаа, эсэргээс баталсан баталгаа | book cross-refers to pp.316-319 | 203 |
| `inductive reasoning` | индукцын ургуулан бодолт | spelled индукцийн in the examples that follow | 203 |
| `inference by analogy` | адил төстэйгээр дүгнэлт хийх | printed together with "analogical inference" | 205 |
| `infinite geometric sequence` | геометрийн төгсгөлгүй прогресс | printed with capital I | 205 |
| `inflection point` | нугаралтын цэг | Mongolian taken from the definition printed with it | 205 |
| `influeuce of Greek geometers` | Грекийн геометрчидийн нөлөө | book typo: "influeuce" for "influence" | 205 |
| `informal` | албан бус, хэлбэрийн бус, агуулгат, жирийн, энгийн | printed together with "informally" | 206 |
| `informally` | албан бус, хэлбэрийн бус, агуулгат, жирийн, энгийн | printed together with "informal" | 206 |
| `initial condition` | эхний нөхцөл | of a differential equation | 206 |
| `input` | оролт; 1. оруулалт, оруулах 2. орох мэдээ (мэдээлэл), эх мэдээ | rendering taken from the parallel Mongolian sentence | 172,206 |
| `inscribed polygon` | багтсан олонөнцөгт | Mongolian printed as one word | 207 |
| `integer valued` | бүхэл тоон | printed together with "integer-valued" | 208 |
| `integer-valued` | бүхэл тоон | printed together with "integer valued" | 208 |
| `integral part of the numbers a` | a тооны бүхэл хэсэг | printed "numbers a"; read "number a" | 209 |
| `integration by parts` | хэсэгчилэн интегралчилах, хэсэглэн интеграл авах | printed together with "to integrate by parts" | 209 |
| `interaquartile range = upper quartile - lower quartile` | квартил хоорондын далайц = дээд квартил – доод квартил | book typo: "Interaquartile" for "Interquartile" | 211 |
| `intersection` | огтлолцоо, огтлолцол, огтлолцлын цэг (шулууны) | (шулууны) qualifies the last sense, point of intersection of lines | 212 |
| `interval notation` | завсрын бичлэг (тэмдэглэл); завсрын бичлэг ((a,b) мэтийн) | sub-entry printed twice in the entry; see second rendering; second occurrence of the sub-entry in the same entry | 213 |
| `invalid` | хүчингүй, зохисгүй, бодьтой бус, үндэсгүй, үндэслэлгүй, тохирохгүй, худал | бодьтой printed thus in the book; standard spelling бодит | 214 |
| `invalidity` | зохисгүй болох (нь), үндэслэлгүй болох (нь), бодьтой бус болох (нь), худал болох (нь) | бодьтой printed thus in the book | 214 |
| `invariant by` | -ийн хувьд инвариант | printed jointly as invariant by, invariant under | 215 |
| `invariant under` | -ийн хувьд инвариант | printed jointly as invariant by, invariant under | 215 |
| `inverse` | 1. урвуу хэмжигдэхүүн, урвуу, урвуу функц, 2. инверсийн дүр, 3. урвуу элемент, урвуу үйлдэл, 4. инверс (хувиргалт) | four numbered senses as printed | 215 |
| `inverse implication` | эсрэг импликац | (p̄ ⇒ q̄) | 196 |
| `inverse of M` | M матрицын урвуу матриц | relative to multiplication; M⁻¹M=MM⁻¹=I | 215 |
| `inverse proportion` | урвуу пропорционал хамаарал | printed jointly as inverse proportion, inverse variation | 219 |
| `inverse variation` | урвуу пропорционал хамаарал | printed jointly as inverse proportion, inverse variation | 219 |
| `iota` | йота | Greek alphabet letter I ι | 220 |
| `ipso facto` | баримт ёсоор, түүгээр | marked (лат), i.e. Latin | 220 |
| `irreducible polynomial` | үл задрах олонгишүүнт | printed "олонгишүүнт" set solid; usually олон гишүүнт | 222 |
| `irregular figure` | зөв бус дүрс | listed twice on the page, once with a definition | 222 |
| `irrespective` | харьцангуй, үлхамаарах | printed "үлхамаарах" set solid; usually үл хамаарах | 222 |
| `Ø is identity for set union` | Ø нь олонлогийн нэгдлийн нөлөөгүй элемент | A∪Ø = Ø∪A = A | 194 |
| `isometry (isometries)` | зай хадгалдаг, хувиргалт буюу хөдөлгөөн | comma as printed; likely зай хадгалдаг хувиргалт буюу хөдөлгөөн | 223 |
| `isosceles triangle` | адил хажуут гурвалжин | the definition below spells it адилхажуут | 223 |
| `issue` | 1. үр дүн, үр дүнд гарах 2. асуулт, сэдэв | two numbered senses: result; question or topic | 223 |
| `iterated iterative` | давтсан | printed "iterated iterative"; likely "iterated, iterative" | 223 |
| `jack` | бундан (хөзөр) | playing cards | 223 |
| `jointly variable` | хамтын хамаарал | entry runs over onto page 224 | 223 |
| `law of absorption` | шингээлтийн хууль | set theory: A ∪ (A∩B) = A | 15 |
| `law of cosinus, cosine rule` | косинусын теорем | printed "cosinus" for cosines | 91 |
| `law of excluded middle` | гуравдахыг үгүйсгэх хууль | Illustrated as p ∨ ~p нь үнэн | 150 |
| `lawer bound` | доод хил (4,45) | lawer as printed; typo for lower | 49 |
| `laws indices` | зэргийн чанар | printed "laws indices"; rules aᵐ·aⁿ=aᵐ⁺ⁿ, aᵐ:aⁿ=aᵐ⁻ⁿ, (aᵐ)ⁿ=aᵐⁿ | 201 |
| `Liar's antinomy` | худалчийн зөрчил | paradox үгийн орчуулгад бий | 30 |
| `limit (informal definition)` | хязгаарын албан бус тодорхойлолт | printed "limit (in formal definition)" across a line break | 206 |
| `local extremum` | функцийн тухайн засвар дахь экстремүм, функцийн тухайн завсар дахь хамгийн их буюу бага утга | book prints засвар first, завсар second; the first is a typo; book prints засвар, apparent typo for завсар; cross-ref 208-р нүүр | 157 |
| `look back at the definintion of a polynomial` | Олон гишүүнтийн тодорхойлолтыг эргэж хар | printed "definintion" for definition | 42 |
| `major axis` | их тэнхлэг | of an ellipse | 133 |
| `Make it concise.` | Эквиваленц болгон томьёол | guideline 6 | 105 |
| `Make it reversible.` | Урвуу нотломж томьёол | guideline 5 | 105 |
| `many to many correspondence` | олонд олныг харгалзуулсан харгалзаа | figure caption | 89 |
| `many to one correspondence` | олонд нэгийг харгалзуулсан харгалзаа | figure caption | 89 |
| `mappings` | буулгалт | rendering taken from the parallel Mongolian sentence | 169 |
| `matematical development` | математикийн гаргалгаа | printed "matematical"; typo for mathematical | 111 |
| `minor axis` | бага тэнхлэг | of an ellipse | 133 |
| `mutually exclusive events` | харилцан нийцгүй хоёр үзэгдэл | A∩B=∅ байх A, B үзэгдэл | 150 |
| `n factorial` | n үржвэр | printed with n!=1•2•3•4• ... (n–1)•n | 158 |
| `Name the term being defined.` | Тодорхойлох нэр томьёогоо нэрлэ | guideline 1 for writing a definition | 105 |
| `natural logarithms` | натурал логарифм | from Logarithms to the base e are sometimes called natural logarithms | 129 |
| `negation bar` | үгүйсгэлийн тэмдэг (зураас) | logic: overbar for NOT | 43 |
| `negative` | сөрөг | of a scale factor | 135 |
| `Newton binomail` | Ньютоны бином (хоёргишүүнтийг n зэрэг дэвшүүлэх томьёо) | binomail as printed; typo for binomial | 47 |
| `number of congruent sides` | тэнцүү талын тоогоор | in "Triangles can be classified according to..." | 64 |
| `odd and even` | тэгш ба сондгой | Glossed as a game (тоглоом) | 149 |
| `one and thirthy four thousandths` | нэг бүхэл мянганы гучин дөрөв (1,034) | printed thirthy; typo for thirty | 167 |
| `one card is drawn from a deck of 52 card` | Багц 52 хөзрөөс нэг хөзөр сугалсан | printed 52 card, not 52 cards | 128 |
| `one to many correspondence` | нэгд олныг харгалзуулсан харгалзаа | figure caption | 89 |
| `one to one correspondence` | нэгийг нэгд харгалзуулсан харгалзаа | figure caption | 89 |
| `or over and` | «буюу» -г «ба» - гаар илэрхийлэх чанар | distributive property for statements p, q, r | 124 |
| `ordered pair` | эрэмбэлсэн хос | rendering taken from the parallel Mongolian text | 170 |
| `output` | гаралт | rendering taken from the parallel Mongolian sentence | 172 |
| `particular affirmative` | тухайн нотолсон нотломж (бодомж) | logic: particular affirmative proposition | 22 |
| `polynomial in completely factored form` | гүйцэд үржигдэхүүн болгон задалсан олон гишүүнт | example printed: 3x²–3=3(x–1)(x+1) | 158 |
| `range` | утгын муж | rendering taken from the parallel Mongolian definition | 170 |
| `relatively prime` | харилцан анхны хоёр тоо | given as synonym of coprime; example [2;15 мэт] | 87 |
| `repeating decimal` | үет аравтай бутархай | printed "аравтай"; apparently a typo for аравтын | 100 |
| `sequental halving` | дараалан хагаслан хуваах | printed "sequental"; typo for sequential | 185 |
| `set` | олонлог | column heading of the interval table | 213 |
| `set of a data` |  | no Mongolian gloss printed for this bold phrase | 97 |
| `sguare foot` | квадрат фуут | printed sguare; typo for square foot | 165 |
| `sides of the angle` | өнцгийн тал | Өнцгийн цацрагийг тал гэж нэрлэдэг | 28 |
| `solution is immeddiate` | шийдийг шууд олно | printed immeddiate; typo for immediate | 196 |
| `solution set of a inequality` | тэнцэтгэлбишийн шийдийн олонлог | book prints "a inequality" for "an inequality" | 204 |
| `solutions` | бодолт | worked-example label | 174 |
| `square of sum` | нийлбэрийн квадрат | printed in the worked example, not bold | 159 |
| `square root of x` | x-ийн квадрат язгуур | from the mapping diagram | 169 |
| `squared difference` | ялгаврын квадрат | given as (a-b)2 | 113 |
| `State the properties that distinguish the term from others in the set.` | Тодорхойлж буй нэр томьёоны харьяалагдах олонлогийн бусад элементээс ялгагдах онцлог шинжийг томьёол | guideline 4 | 105 |
| `ten cubed` | арвын куб (зэрэг) | printed "10cubed = I0³" with capital I for 1 | 95 |
| `the absolute value of a number` | тооны абсолют хэмжигдэхүүн | distance on the number line from the number to 0 | 15 |
| `The characteristic is the whole number part of a logarithm` | Тооны логарифмын сөрөг бус бүхэл хэсэг нь характеристик (үзүүлэлт) юм | logarithm sense; example lg400=2,6021 given | 59 |
| `the circle with center at (−1 2)` | (−1,2) цэгт төвтэй тойрог | entry runs from page 55 onto page 56 | 55 |
| `the circumference of a circle is the distance right around the circle` | Тойргийг бүтэн яг нэг тойрсон уртыг тойргийн урт гэнэ | phrase begins on p.62 | 63 |
| `the complement of A relative to B` | A олонлогийн B олонлог хүртэлх гүйцээлт | also given as the set difference of B and A | 113 |
| `the continuum hypothesis of Cantor` | Канторын континуумын таамаглал | domain marker printed: (олонлогийн онол) = set theory | 83 |
| `The definite integral of a continuous function f over an interval from x=a to x=b is the net change of an antiderivative of f over the interval.` | Тасралтгүй f(x) функцийн [a,b] завсар дээрх тодорхой интеграл нь эх функцийн мөнхүү завсар дээрх цэвэр өөрчлөлт юм | sentence begins on page 103 | 104 |
| `The distributive property holds` | гишүүнчилэн үржүүлэх чанар биелдэг | printed гишүүнчилэн; elsewhere гишүүнчлэн | 190 |
| `the golden ratio` | алтан пропорц | rendering used in the worked passage | 180 |
| `the graph of the inequality` | тэнцэтгэлбишийн график, тэнцэтгэлбишийн шийдийн олонлогийн дүрслэл | interval for one variable, Cartesian region for two | 204 |
| `The greatest common divisor (GCD) of the numbers a, b` | a, b хоёр тооны хамгийн их ерөнхий хуваагч (ХИЕХ) | ХИЕХ = хамгийн их ерөнхий хуваагч | 183 |
| `The greatest integer tunction` | бүхэл хэсгийн функц | printed "tunction"; typo for function; [y=[x] график хар] | 183 |
| `the grouping does not alter the result` | бүлэглэх (хаалтанд хийх) нь үйлдлийн үр дүнг өөрчлөхгүй | associative property | 25 |
| `the highest point on the graph, is (0,4)` | y =4 –x² функцийн графикийн хамгийн өндөр цэг нь (0;4) цэг юм | (13-р нүүрийн эхний зураг хар) | 188 |
| `The imaginary number i is defines i=√-1` | хуурмаг i тоог i=√-1 гэж тодорхойлдог | printed is defines; typo for is defined; begins p. 195 | 196 |
| `the leg adjacent to the acute angle` | хурц өнцөгт налсан катет | right triangle | 21 |
| `The order of the addends can be changed without changing the sum` | Нэмэгдэхүүний дэс дарааг өөрчлөхөд нийлбэр өөрчлөгдөхгүй, нэмэгдэхүүний байрыг солиход нийлбэр хувирахгүй | second rendering printed in square brackets | 59 |
| `the probability that a ball drawn at random` | Бөмбөг таамгаар сугалах магадлал | printed unbolded inside the draw entry | 128 |
| `the ratio of the measure of the leg adjacent to the acute angle to the measure of the hypotenuse` | хурц өнцөгт налсан катетын уртыг гипотенузын уртад харьцуулсан харьцаа | i.e. cosine ratio | 21 |
| `the set of all possible values of the independent variable is the domain of the relation` | Харьцааны (функцийн) үл хамааран хувьсагчийн бүх боломжит утгын олонлог нь тодорхойлогдох (тодорхойлсон) муж юм | Mongolian runs over onto p.127 | 126 |
| `the size of an angle` | өнцгийн хэмжээ | Нэг талыг нөгөө талтай давхацтал эргүүлсэн дүн | 28 |
| `the vertex of the angle` | өнцгийн орой | Цацрагуудын ерөнхий цэг | 28 |
| `There are four ways of a choosing a president` | Дарга сонгох дөрвөн арга байна, Даргыг 4 янзаар сонгож болно | phrase begins on p.61; second rendering in parentheses | 62 |
| `These relations ARE mappengs.` | Энэ хоёр харьцаа (харгалзаа) нь буулгалт мөн | book prints "mappengs" for "mappings" | 89 |
| `These relations are NOT mappengs.` | Энэ хоёр харьцаа (харгалзаа) нь буулгалт биш | book prints "mappengs" for "mappings" | 89 |
| `they may be hard find` | тэдгээрийг олоход хүнд байж болно | printed "hard find"; typo for hard to find | 186 |
| `This compound statement can be written as p↔q and usually is read "if and only if"` | энэхүү нийлмэл хэллэгийг p⇔q гэж бичдэг бөгөөд ерөөс "хэрэв p л бол q" гэж уншдаг | of (p→q) ∧ (q→p) | 195 |
| `this condition is violated` | Энэ нөхцөл биелэхгүй байна | same Mongolian as "is ruled out" | 76 |
| `this parahola, which opens downward` | энэ параболын салаа нь доошоо харсан байна | printed parahola; typo for parabola | 128 |
| `to carry out (to make, to run) experiment` | туршилт хийх | Mongolian completes on p.154 | 153 |
| `to chek for errors` | алдаа засах | printed "chek"; typo for "check" | 60 |
| `to chek out` | нотлогдох, зөвдөх | printed "chek"; typo for "check" | 60 |
| `to differentiate with respect x` | x–ээр уламжлал авах | printed "with respect x"; the "to" is missing | 114 |
| `to eliminate of unknown` | үлмэдэгдэхийг зайлуулах, үлмэдэгдэхийг устгах | printed 'үлмэдэгдэхийг' as one word | 132 |
| `to increase by` | аар өсгөх (нэмэгдүүпэх) | book prints нэмэгдүүпэх for нэмэгдүүлэх | 200 |
| `to increase with out bound` | хязгааргүй өсөх | printed "with out" as two words | 200 |
| `to integrate by parts` | хэсэгчилэн интегралчилах, хэсэглэн интеграл авах | printed together with "integration by parts" | 209 |
| `to play a cards` | хөзөр тоглох | printed "a cards" - article typo | 53 |
| `to reduse fractions by factor of` | бутархайг...-д хураах | printed reduse; typo for reduce | 167 |
| `to test hypothesis with expertiment` | таамаглалыг туршилтаар шалгах | printed expertiment; typo for experiment | 192 |
| `truth assignment` | үнэний утгын оноолт | logic | 39 |
| `two adjacent terms` | зэрэгцээ (хөрш) хоёр гишүүн | terms of a sequence/series | 21 |
| `two-column proof` | хоёр баганат баталгаа | rendering taken from the parallel Mongolian sentence | 165 |
| `type of interval` | завсрын хэв | column heading of the interval table | 213 |
| `U is identity for set intersection` | U нь олонлогийн огтлолцлын нөлөөгүй элемент | for every set A and universe U: A∩U = U∩A = A | 194 |
| `under certain conditions` | тодорхой нөхцөлд, мэдээжийн нөхцөлд | entry runs from page 56 onto page 57 | 56 |
| `universal affirmative` | ерөнхий нотолсон нотломж (бодомж) | logic: universal affirmative proposition | 22 |
| `upper and lower values` | дээд утга, доод утга | of a class interval; rendered завсрын хил as class boundaries | 64 |
| `Use only undefined terms or previously defined terms.` | Зөвхөн үл тодорхойлсон ухагдахуун буюу өмнө тодорхойлсон нэр томьёо ашигла | guideline 2 | 105 |
| `use the order of operations to evaluate each of the following` | Үйлдлийн дараалал ашиглан доорх илэрхийлэп бүрийн утгыг ол | Printed илэрхийлэп; typo for илэрхийлэл | 148 |
| `vertical axis` | гулд (босоо) тэнхлэг | гулд as printed; likely typo | 42 |
| `vertices` | орой | of an ellipse | 133 |
| `without loss of generalities` | ерөнхий байдлыг алдагдуулахгүйгээр | printed generalities for generality | 177 |
| `Worked example` | жишээ | marks the book's worked problem; printed Жишээ | 189 |
| `write as a decimal` | аравтын бутархай болгон бич | from the worked example 7 and 43 hundredths = 7,43 | 100 |
| `x-coordinate` | x координат; x-координат | in a Cartesian coordinate system; the abscissa | 14,72,86 |
| `XY does intersect AB` | XY хэрчим AB хэрчмийг огтолсон | XY and AB printed with segment bars | 126 |
| `y against x` | y нь x-ээс хамаарсан функц | plotting y versus x | 22 |
| `y is to be find` | y–ийг олох хэрэгтэй | printed is to be find; for is to be found | 162 |

---

## Transcription conventions

- Russian parentheticals printed after the English headword (`аксиальный`, `группа`,
  `гистограмма` …) are the book's Russian equivalents, not Mongolian — excluded throughout.
- Bold multi-word English phrases inside an entry are recorded as **their own rows**.
- Mongolian is transcribed **exactly as printed**, including the book's own typos, which are
  flagged in the note column (`чигпэл` for `чиглэл`, `нугарапт` for `нугаралт`, `үлхамаарах`
  and `олонгишүүнт` set solid). English headwords misprinted in the book (`armithmetic`,
  `Artistotle`, `divident`, `fundamantal`, `imcomparable`) are likewise kept as printed and flagged.
- Decimal commas are reproduced as the book prints them (`0,01`, `2,6021`) — see rule 5 in
  `CLAUDE.md`.
- `source_page` is the printed page number, for checking against the original.

## Adding the next batch (K onwards)

The pipeline is set up. Photograph the pages, drop them in the same folder, and the process
appends: convert → transcribe in parallel → merge into this TSV → regenerate this guide →
re-derive the voice patterns in `mn-voice-reference.md`. Nothing here needs rebuilding by hand.
