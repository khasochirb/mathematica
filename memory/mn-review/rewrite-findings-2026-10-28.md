# Mongolian rewrite: findings for Khas (27–29 Oct 2026)

Logged by Build while rewriting lessons, the problem bank, exams and placement.
English source errors are listed, not fixed (except where marked FIXED). Terms marked
Review/Khas call need his ruling.

- 8/exponents L2 quick check: wrong option 9^3 equals the answer 3^6 (two correct options, live English and MN). L5 funFact '40-plus powers of ten' vs examples spanning 36.
- 8/linear-equations: 3 rewritten worked items need new check[] lines (draft Notes). Like terms: live «ижил төстэй гишүүд» vs algebra-1 drafts «ижил гишүүд»; break-even «тэнцэх цэг» vs grade 9 «ашиггүй, алдагдалгүй цэг» — reconcile.
- 8/linear-functions: lf5-we2 English statement garbled; vacuous checks (1 != 9, Rational(150,100) != 0); scooter check -> 1500 != 0; rise/run «өсөлт / гүйлт» (g8) vs «өндөрсөлт / урагшлалт» (algebra-1 draft); coordGeo widget shows English and m.
- 8/systems: elimination live «устгах арга» vs algebra-1 «зайлуулах арга»; intercept «огтлол» vs grade 9 «y тэнхлэгтэй огтлолцох цэг»; next-topic title per 6ac must match scatter rewrite; widget label 'slope m₂' English.
- 8/roots English facts wrong: doubling the cube impossibility proved by Wantzel 1837, not the Greeks (live MN repeats it); YBC 7289 accurate to 5 places not 6; 'far fewer than squares' 10 vs 12.
- 8/scatter English: L5 says snap gives y=0.75x+2.5, widget snaps to 0.76x+2.72; L3 funFact '$8 million outlier' unsupported, 2010 fat-finger rumour told as possible. Widgets show m for slope.
- 7/percent-applications: 17 rescaled ₮ problems need new check[] (draft Notes for Build). English: L5 funFact title 2% vs body 8%; máš = young goat not calf; L2 20/60 = 33% should be ≈.
- 7/equations-and-inequalities English: eqi-pr8 at 36 rides costs equal (pass cheaper only from 37); Mariner 1 error was a missing overbar not a minus. Word: «нийтлэг хуваарь» -> «ерөнхий хуваарь» (grade 6 word), needs Khas.
- 7/rational-number-operations English: L6 tryItSet p2 second option also true (two correct answers, live). Words: «абсолют утга» vs mirror «үнэмлэхүй утга»; rno-pr8 unit $ -> мянган төгрөг needs OK.
- 7/sampling English: L2 funFact title wheat/chessboard not in body; L6 ex3 'same mean' but 23 vs 25; L5 Shop B '10–55' vs data 10–50; sas6-t2 '0.2 ≈ 0.22 MADs'. Words: «хазайлт» = bias/deviation/skewed in one topic; sample proportion «түүврийн пропорц» vs prob-stats «түүврийн хувь». 2 new check[] lines (L4 table).
- 7/proportional English: L1 concept 3 'is Grade 6 skill'; live MN L5 fact shows \text{flour}/\text{cookies}; L3 step 5 p3 check[] tests the wrong thing. dealCompare widget shows $. Constant of proportionality: three competing names, kept «пропорционал коэффициент».
- 7/geometry-scale English: 14×3.14 = 43.96 not 43.98; 'smaller scale ratio → longer drawing' reads backwards; Borges map not Manhattan; pizza claim contradicted by own numbers; 3 m window can't take a radius-1 m semicircle. Words: angle pairs «нэмэлт/зэргэлдээ» (live) vs geometry draft «гүйцээлт/залгаа» (4d open); «тойргийн талбай» vs «дугуйн талбай» split.
- 7/probability: thumbtack -> шагай 24/60 needs check[] swap; prb-ty1 word PROBABILITY -> КОЭФФИЦИЕНТ (answer 2/11 kept). English: Grand Duke funFact 9 and 10 'three ways' (six each); L2 beat reads '2 × 1 = 24'; \frac{1}{2}^3 ambiguous. Words: «нийцгүй» (mutually exclusive), «хамаарах» (dependent), «гарцаагүй» vs grade 10 «баталгаатай».
- 6/coordinate-plane LIVE MN bug: L2 renders '3 steps east' as «зүүн тийш» (= left on the grid). English: L4 'across the origin' ×4 should be 'across an axis'; pr-8 asks for area never taught; grid widget captions English. geometry-coordinate-geometry draft lists «квадрант»; live/exam say «мөч» — align.
- IMPORTANT: scripts/i18n/mn_terms.py maps scatter plot -> «цэгэн диаграмм», against ruling 6ac (scatter «хамаарлын график», dot plot «цэгэн диаграмм»). --fix would corrupt dot plots. Fix the script before running verify:mn-terms --fix on any mirror. 6/data-and-statistics English: L3 10-min bins over 85–182 give 11 bars not 6; L2 5{,}000 renders literally; L4 ex3 mixes Team A/B; Playfair apology unconfirmed. Live 6-mn: 15 of 18 fact formulas show English.
- 6/factors-and-multiples: 6 English imprecisions (fixed in MN only: forgets 1, own multiple, factorization only >1, share 1, RSA/Euclid overclaims); widget buttons English ('Test the next number', 'Split once').
- 6/expressions: like terms «ижил гишүүд» (6–7) vs «ижил төстэй гишүүд» (8) — one ruling; live MN tells students to tap Mongolian buttons that don't exist (widgets English); English L4 step 6 'power' title w/o power; rice claim unsourced.
- 6/geometry-area-volume: words «шоо / тэгш өнцөгт параллелепипед / нүүр» (grade 6 live) vs «куб / тэгш өнцөгт призм / тал» (grade 8, geometry) — one ruling. compositeArea widget labels English (pipeline never reaches). English: L6 'can-tenth' garbled; L3 self-correcting step; honeycomb is 2D wall length per area; Mars orbiter ~$125M not 'million-dollar'.
- 6/integers: keep-change-change «хадгал–соль–соль» (g6) vs «хэвээр–солих–солих» (g7) — one ruling. English: L4 '(−12)+7 jump left past zero' wrong (right, stops at −5); L6 'digits'; L5 recap 'up' vs 'right'; adjacent signs without brackets (-12 \div -4, pr-6, pr-8). Added fact: Ulaanbaatar ~+1350 m — Khas to confirm.
- 6/decimals English: L5 practice p4 offers $0.030$ and $0.03$ both correct (two right answers, live); 'All share 0.41' false for 0.409; others minor. Words: «аравтын цэг» vs decimal comma; simplest form «хамгийн энгийн хэлбэр» (g6) vs «үл хураагдах» (g8).
- 6/percentages: widgets and 12 figures in L4–L5 show $50 beside text saying 50 000₮ — need currency ₮, values ×1000, formatter fix. English: test score in dollars; 'pay' inside maths; '$8\% tax' stray $; fact subtracts a percent from a number; % origin wrong.
- 6/fractions English: L3 option 3/6 marked wrong though = 1/2 (two right answers, live); L6 wrong option '4/6 (not simplified)' should be 2/6; L3 tells students to tap 'Combine' (no such button); 4 fraction widgets English buttons; duplicate key _lessonDraft_dividing-fractions in source JSON. Words: reduce «хураах» vs mirror «хялбарчлах»; «буруу бутархай» vs dictionary «зөв бус бутархай»; coined «дохио үг».
- 6/ratios English: L1 concept 2 says 6:2 milk:cocoa differs from 2:6 cocoa:milk (same mix); runner at 60 km/h, plane at 70 km/h. Live MN: 4 tryThis blocks in English; mn_topic_dump skips tryThis/note/figure labels; dealCompare widgets show $. Unit price «нэгж үнэ» (g6) vs «нэгжийн үнэ» (g7).
- 6/fractions: EN multiply expl says 'simplifies to' when already simplest (20/36); compare uses product of denominators even when equal
- 6/integers bank: form g6-multiply-integers titled 'Multiplying and dividing' but all variants multiply; add explanations bracket positive addend $-12 + (7)$
- 7 bank g7-prop-word: 14 variants truncate unit price (250÷3=83) so '83×9=750' false; answers right
- integrated-1 linear-functions L2 step 3 tapQuestion: wrong option C (−1, 7) lies on the line (two correct answers, live)
- DECISION for Khas: bank options use English interval notation [a, b) while 9-mn lessons write ]a; b[. Gate keeps bank maths byte-identical; a notation switch would need a deliberate bank-wide maths transform.
- BANK-WIDE English: unbracketed double minus in statements/explanations (10 quad-functions: (x - -4)^2 in 18 statements; 8 linear-functions, 8 systems, 9 intro-functions, 6 integers). Fix English by bracketing negatives; then regenerate bank mirrors (gate requires identical maths).
- 10 bank quadratic-equations: formula/discriminant explanations write $-5^2$ for (-5)^2 (mathematically wrong: -25) and $\dfrac{--5 \pm 9}{2}$. Fix English + regenerate.
- review: 10 bank exponential-functions compound interest writes «$1000$ мөнгө» (English has no currency)
- 11 bank complex-numbers g11-modulus: $-6^2 + -5^2 = 61$ (needs brackets)
- 11 bank sequences: identify-sequence statements have stray outer delimiters $$2$, $5$…$$ (render bug in English); geometric-term expl $-2^{6}$ for (-2)^6
- 11 bank statistics data-lies: English explanations garbled ('i.t', 't.he', no full stops); pie>100% keyed to weak option
- PLAN after bank: one scripted pass bracketing negative bases/operands in maths ($-3^2$→$(-3)^2$, $a - -b$→$a - (-b)$, $+ -b$) applied identically to data/problembank/*.json AND i18n/bank-tables (gate needs equal maths); then remove writers' 'read −3² as (−3)²' notes (12/limits LC5 has 16). Needs Khas OK (changes English content).
- DECISION (same pass): bank maths keeps \tan/\cot/\csc while lessons write tg/ctg/cosec (\operatorname{tg}). A scripted notation pass on MN tables only (EN stays) would need the gate to allow a whitelisted notation map. 12 trig-identities TI5: 'reference angle gives 210°' wrong in EN.
- NOTATION PASS also: bank writes y = mx + b; Khas ruling 2a is y = kx + b (lessons follow it). Same for slope m→k.
- review: 'roots' = «язгуур» in grade-10 bank vs «шийд» in algebra-1/2 bank+lessons (each follows its own lesson). Pick one?
- integrated-1 transformations ty-7 English solution is leftover authoring notes + wrong motion
- calculus bank CAL-area-v24: \int_0^10 renders as ∫_0^1 0 (needs ^{10}) — real display bug
- ENGLISH DATA BUG (live): duplicate problem ids — integrated-2: 32 ids im2-u8-* shared by geometric-measurement-and-modelling AND probability; integrated-3: im3-u4-p13..p15 duplicated. Attempts keyed by id collide. Renaming detaches history → Khas decides.
- NOTATION PASS also: bank uses ^{n}C_r / \binom{n}{r}; ruling 6t says C_n^r
- review: prob-stats bank permutations PS-repl-v08 keeps English MISSISSIPPI (no Mongolian word with 4,4,2,1 pattern); other words Mongolian with same patterns
- review: prob-stats bank probability-models writes marbles «бөмбөг» (following prob-stats lesson) though ruling says marble = «бөмбөлөг»
- solid-geo bank cut-cone statements end '(Variant N.)' — leaked authoring text in English
- trig bank special-triangles: garbage distractors $1 + 8*sqrt(3)$; 'QIIII'; axis-angle explanation nonsense
- prob-stats bank PS-caus-v06/v11: correct option says causal reading fair, explanation says not safe (contradiction in English)
- integrated-2 RTT draft: l3-we4 145.1/65.1 should be 145.2/65.2; ty-5 0.0798→0.0797. trig bank: 18 cos variants in 'Solving sin x = k'; duplicate variant pairs

## integrated-2 similarity (draft)
- im2-u5-l2-we4 calls angles vertical without stating A, C, D collinear (MN says AD and BE cross at C).
- L4 coordGeo widget measures to (30, 36), not a point in the river figure.
- L1 title "The transformation IM1 left out" inaccurate; MN reworded.
- Review term: «тусгалын өнцөг / ойлтын өнцөг» (incidence/reflection), school-physics wording.
## vectors-matrices bank
- matrices: VM-sqr-v02 says "would give 1" which is also the correct answer; `$5 \cdot -3$` lacks brackets. Coined «хөрвүүлсэн матриц» (transpose).
- determinants, systems-3: no English errors; "1x" coefficients left as in English.
## integrated-2 right-triangle-trig (lesson)
- im2-u6-l3-we4: English 145.1 / 65.1 should be 145.2 / 65.2; MN corrected.
- vectors-matrices transformation-matrices: VM-tms-v06 explanation lists one unit-point destination but says "those two destinations" (MN adds the missing one). Transpose written «мөр, баганыг нь сольсон матриц» here vs coined «хөрвүүлсэн матриц» in matrices unit: Khas to pick one.
## geometry bank
- parallel-and-perpendicular: "proving lines parallel" form v04–v07, v10, v12 angle numbers mismatch lesson numbering (∠2/∠6 called alternate interior; they are corresponding). No figure. Kept.
- triangles-and-congruence: GEO-cshort-v11/v12 explanations ungrammatical; every cshort explanation ends with the SAS-only sentence even when the answer is SSS/ASA/AAS/HL; isosceles vertex-angle explanations name a wrong answer not among the options (v11: 109°).
## integrated-3 modelling (draft)
- "Second differences = 2a" only when x steps by 1; L1 opening promises "three savings plans" but third is a thrown ball; im3-u8-l3-we2 solution corrects itself mid-sentence; 32 m pine "taller than almost any pine on Earth" false; im3-u8-l2-we1 ski-lift question incoherent.
## integrated-3 exp-logs (draft)
- im3-u3-l4-t1 number changed (4 000 000₮ phone → 3 240 000₮): needs new check[] in assembly.
- L1 concept 1 self-contradiction on which equation asks for the exponent; L4 tip/mistake 3 say "doubling time" with half-life example; "base-10 logs run decibel scale" loose.
## integrated-2 solving-quadratics (draft)
- L5 discriminant counts parabola–circle intersections (actually degree 4); "two lines cross at most once" ignores coincident; rational-root test needs integer coeffs; L1 we2 check slip; "every quadratic has exactly two roots" vs double root; ty-5 a²+b² "always positive" fails at 0; algebraTiles widget cannot draw x² tile (ship work).
## geometry relationships-in-triangles bank: no English errors.
- geometry area-and-perimeter: parallelogram explanation calls 2(b+h) "a perimeter" (only true for rectangle). Review: «үржигдэхүүн» used for "the ½".
- geometry quadrilaterals: no English errors. Review: numeral module gives «$180$-г» (acc).
- geometry right-triangles-and-trig: GEO-raot-v12 explanation broken ("so the triangle is no triangle can have these sides"). geometry similarity: none.
- geometry reasoning-and-proof: GEO-cex-v02/v04/v07 keyed counterexample not unique (other options also counterexamples); GEO-cex-v10 keyed kite isn't a counterexample; GEO-around '180° slip' distractor is really −30 shown as 30. Coined «тэнцэтгэлийн тэгш хэмийн чанар» (symmetric property), «эсрэг өгүүлбэр» (inverse).
- solid-geometry lines-and-planes: SOLID-planes-v10/v12/v24 "overcount" figure equals or misstates the answer (8·7=56 is the answer; 9·8=72 < 84); n(n-1) isn't ordered triple count; odd distractor "equal and intersecting". Coined «нийтлэг перпендикуляр».
- trigonometry laws: cos-from-sides "Adding c² … flips the sign" mislabels distractor (69/35 option); ambiguous-case "there is two triangles" grammar and omits a = height (one triangle).
- vectors vector-arithmetic: all 12 parallel-scalar explanations contain leftover placeholder 'Matching the wrong pair gives $\frac{p\,q}{r} = …$'.
- trig right-triangle: "Find the side ADJACENT the 30° angle" missing "to"; hypotenuse-from-angle options float artifacts `$2.50000000000000$`; form "Finding a side with sine" includes cosine variants.
- vectors-and-coordinates: full stop inside maths `= 0. $`; option "parallel but not equal" ambiguous (fits opposite) — MN option reads «тэнцүү ч биш, эсрэг ч биш» (REVIEW: option meaning narrowed); vm-magnitude explanation compares vector with itself when both coords positive (MN rewrote).
## integrated-3 function-families (draft)
- im3-u5-p1 "one step away" from vertex (it's two); L2 one failing example settles "neither" only if same pair fails both tests; im3-u5-p15 one-to-one argued from oddness (doesn't follow); im3-u5-x8 "at x = 3 in both directions" but second starts from 8.
- Term mismatch: mn_terms.py «тэгш хэмээр хувиргах» vs ruling 4g / live mirrors «тэгш хэмтэй хувиргах» (followed ruling) — mn_terms.py should be updated by Khas's call.
- precalc exp-logs bank: REVIEW «хэмжээг $8$ хуваах» (avoids ending on changing number).
- precalc transformations bank: vertex-form says leading number 'stretches the parabola' even when 1/−/negative (MN splits by a); shifted-domain 'Subtracting (-2) instead of adding it' garbled. Options use bare «x тэнхлэг» (can't add maths to option).
- precalc unit-circle bank: quadrant written «$2$-р мөчид» (maths fixed) vs lesson «II мөч» — notation pass.
- precalc polynomial bank: PC-eb-v02 calls leading coefficient "$-$" (should be −1). «язгуур» vs algebra-2 bank «шийд» for roots (review item).
- precalc rational bank: HA v04/v10 constant numerator written `6 + \ldots`.
- precalc conics bank: hyperbola "slope far too steep" wrong when b < a; ellipse foci "radii" should be "semi-axes".
- precalc trig-graphs bank: PC-st-v04..v06 "reference angle is −30°/−45°/−60°" (reference angles are positive; MN states positive one).
## integrated-1 bank
- linear-eq: two-step check `$2\cdot -4$` lacks brackets; special-solution `$x = \frac{1}{-2}$` unsimplified; budget form says "rounds DOWN" even when division exact (MN says exact); two-step says "Undo the addition" for subtraction. Review: «Цэнгэлдэх хүрээлэн» (park), «тоглоомд суух» (ride).
- functions-sequences: im1-recursive-explicit calls wrong option "$2n$ version" when step negative.
## Course exams (new): MN exams generated from bank mirror by id (scripts/i18n/mn_exams.py, i18n/exam-meta.mn.json). New chrome strings for Khas: «Жишиг шалгалт», «{course}: жишиг шалгалт N», «Дүн», «Бүлгээр», «Эндээс эхлээрэй», «Бүлгийг давтах», «Дасгал хийх», «Бүх бодлого», «Зөв хариу:», «Тэмдэглэх/Тэмдэглэсэн», «Шалгалтаа илгээх», «хариулсан», «Өгсөн», exam intros.
- linear-functions: model-breakdown uses $y = -2x + 24$ but t for time; taxi 'per extra k' (km). Review coined fee names «холболтын / бэлтгэл ажлын / бүртгэлийн / зураг авалтын / шугамын хураамж».
- im1 systems: 'A adult one is worth…'; '$4$ pens and $1$ notebooks'; 1y/1x coefficients in maths.
- im1 coordinate-geometry: im1-triangle-perimeter 'Two sides are along the axes' (only parallel); im1-prove-parallelogram 'equal diagonals prove a RECTANGLE' (only for a parallelogram).
- im1 transformations: symmetry form 'for a regular n-gon' remark on rectangle/rhombus variants. Coined «адилтгал хувиргалт» (identity).
- im1 exponential: exp-two-points 'the $2$th/$3$th root'; write-exp-model 'A grow of'; exp-evaluate `\frac{11}{10}^{2}` unbracketed.
- im1 quantities: rear-v02 two correct options (w=P/2−l and w=(P−2l)/2); uconv-v29/v31/v33 "8.6/9.8/7.2 has 3 significant figures" (2). FIXED (live render bug): im1-aun-v01..v12 `\times` was a literal tab (showed "imes") — fixed in scripts/pb/integrated_1_more.py, data/problembank/integrated-1.json and the MN table.
- mn_numerals: fixed зуу instrumental («$100$-гаар», was «-наар»).
## integrated-2 bank
- polynomials: im2-add-polynomials (36) "minus applies to every term" line doesn't flip x-term sign; im2-polynomial-closure says 2/2, 4/2 not integers and (2x+1)/(2x+1) not polynomial; `1x`, `((x + 1))((x - 1))` options.
- solving-quadratics: im2-factor-solve (36) says the pair multiplying to c and adding to b "are −7 and −6" (those are roots; pair is 7, 6) — MN states correct pair. «шийд»/«язгуур» mix in im2-complex-roots.
- radicals: im2-rex-v03 asks 8^{3/3}; rationalise form `\dfrac{1\sqrt{2}}{2}`.
- im2 quadratic-functions: which-form 'The roots is immediate as p and q Getting…'; compare-growth 'doubling beats squaring' where g(x)=3^x; transform options '1 units'.
- im2 similarity: im2-dilation-composition 'two doublings quadruple nothing — but 2×2=4, not 2+2' muddled; im2-scale-factor `\frac{1}{2}^2` unbracketed.
- im2 right-triangle-trig: pick-ratio/ratio-value explanations repeat fraction ($\frac{3}{5} = \frac{3}{5}$); 45° explanation 'only if the angle were 30°' loose.
- im2 circles: im2-ccs-v19 '$… - 0 = 0$'; sector-backwards/arc-length answers include '$1\pi$'. Review «$\pi$-ийн хэдэн дахин бэ?» for fractional answers.
- im1 data-stats: line-of-fit options 'a change of -3 units lost per year' double negative; 'Hours of tv' lowercase.
- im2 measurement bank: im2-crs-v29–v32 pyramid cut "through apex and two opposite base edges" impossible (MN: midpoints of those edges); im2-crs-v33–36 square-base prism cross-section is a square but "a rectangle" keyed. NOTE: the 32 duplicate im2-u8-* ids are LESSON ids (data/genmath/integrated-2), not bank ids.
- im3 exp-logs bank: im3-exp-equation explanations repeat "$x = 2$, so $x = 2$". Review «$10$-ыг» vs «арвыг».
## integrated-3 rational-radical (draft)
- im3-u2-l2-we2 omits restriction x ≠ 4 and calls x − 1 a denominator (full set x ≠ −4, 4, 1) — MN corrected; English needs ship fix.
- Teacher brief terms overridden: hole «цоорхой» (not «нүх»), range «утгын муж» (not «далайц»), factor «үржигдэхүүн» (not «хуваагч»). Khas call: «эргүүлэх» vs ruling «урвуулах» for "flip".
- im3 sequences bank: im3-binomial-coefficient and im3-binomial-term ask identical questions.
- im3 trig-functions bank: quadrant-sign statements/options 'is/are' template leftover; max/min explanations say adding a negative 'lifts' the curve.
- im3 rational-radical bank: written-out coefficient 1 ("1x", "1x ≥ 12"); "dividing the numbers by 1"; "$\dfrac{3}{4} = \frac{3}{4}$"; blurb mentions radical-equation extraneous roots the unit doesn't drill.
- im3 function-families bank: no errors.
- GATE LIMIT (several units): word options can't gain `$x$`, so «x тэнхлэг» appears as bare Latin in options — consider letting the gate allow a single-letter variable in maths in word options.
- im2 probability bank: im2-ss2-v08 'first/second' means one coin vs the other two. Review «тоглоомын чулуу» (counters).
## integrated-3 sequences (draft)
- im3-u6-x4 Plan B smaller in 7 of 12 months, not "eleven"; im3-u6-x8 keeping three terms drops three, not "two"; L1 formula split across two maths spans; "two hundred years old" → "over two hundred". Khas call: «үржүүлээд хасах арга» naming.
## integrated-3 polynomial (draft)
- L3 we2 "none of eight candidates works" tests only five; L3 we3 "every solvable cubic" (needs a rational root); odd-degree real zero needs real coeffs; RRT needs integer coeffs; four rounded values written "=" not "≈"; L4 box-volume graph uses generic widget setting; p11 garbled clause.
- im3 modelling bank: read-model-value/interpret-slope/model-domain write y = …x… but talk about t; candle gets taller and printer 'pages left' goes up (should fall).
- im3 polynomial lesson: L3 step 3 title has $p(a)$ but step titles render plain text (English bug: 'Why the remainder is $p(a)$').
## integrated-3 statistical-inference (draft)
- US standards code "S-IC.5" in a solution; "58 heads is everyday" at ~6.7%; 5000 vs 4000 gym sample; p16 adds two margins for "6 points" (margin of difference ≈ 4.2; verdict right).
- Coined «статистикийн хувьд ач холбогдолтой», «дахин санамсаргүйчлэх», «давталт» (simulation round).
- CONSISTENCY for Khas: lesson draft uses brief's «завсар» / «түүврийн пропорц»; shipped prob-stats and the im3 bank use «интервал» / «түүврийн хувь». Pick one.
## Placement
- Geometry transformations:d3 rotation direction unstated (MN: counterclockwise); parallel-and-perpendicular:d3 never says lines parallel; G9 equations-and-formulas:d2 stray space before period.
- ~30 new placement chrome strings for Khas, incl. level names (Суурь / Хөгжиж буй / Чадварлаг / Ахисан), «Дунд анги / Ахлах анги», «Түвшин тогтоох шалгалт» (approved string elsewhere is «…тест»).
- FIXED: localizeTopic keyed forms by id only; integrated-1 im1-slope-two-points repeats across two units → keyed by unit+id; lib/bank-mn-localize.test.ts guards it (fails on old code).
- FIXED: mn_ground selftest "fabricated" control was real words («хуурмаг» = imaginary) → letter salad. 12-exam intro ЭЕШ → ЭШ.
- Placement G7 probability:d1/d3 and G10 probability-and-counting:d3 had English inside \text{} in maths; placement gate now blanks and requires translating them (fixed G7). G10 probability-and-counting:d3 wrong options 1/3 and 2/6 are the same number; G12 integrals:d3 explanation mentions "the ball" the question never introduces.
## integrated-3 trig-functions (draft)
- Practice ids p13/p14/p15 each twice (DUPLICATE IDS, same class as im2-u8 / im3-u4); "a third of a quarter" turn for π/3 (it's two-thirds); L5 altitude from B (it's A); x9 asks for a exactly but never gives it (a = 10(√6−√2)); L3 mistake 4 garbled.
