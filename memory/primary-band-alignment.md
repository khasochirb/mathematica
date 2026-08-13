# Primary band ↔ ministry curriculum (Baga, grades 1–5) — audit & work order

Owner directive (2026-08-13): use the ministry's primary core curriculum
(2014/2019, `data/primary/moe-baga-2019.pdf`, parsed losslessly to
`data/primary/moe-baga-curriculum.json` — 20 sections, 108 objectives, all
core) as the reference for (a) wording, (b) per-grade topic coverage —
"include every topic in each grade; if it is not included yet, add it" —
and (c) FIGURE-FIRST pedagogy: teach with figures, then try-it with
figures, alternating; practice problems built of figures (merge groups for
addition, remove for subtraction); as many figures as possible for young
kids. All three criteria are binding for every unit in this band.

## Audit findings (2026-08-13, data/primary/coverage-audit-2026-08-13.json)

**Coverage** — of 108 ministry objectives, judged against ALL content in
platform grades 3–5: 46 covered, 37 partial, 25 missing.

| Ministry grade | covered | partial | missing | missing codes |
|---|---|---|---|---|
| 1 | 8 | 5 | 2 | 1.1б, 1.3б |
| 2 | 11 | 5 | 2 | 2.3б, 2.4в |
| 3 | 10 | 7 | 3 | 3.1в, 3.3в, 3.4в |
| 4 | 9 | 9 | 9 | 4.1б, 4.1и, 4.2в, 4.2д, 4.3в, 4.3д, 4.3е, 4.4в, 4.4г |
| 5 | 8 | 11 | 9 | 5.1б, 5.1и, 5.1к, 5.2в, 5.3в, 5.3д, 5.3е, 5.4г, 5.4д |

**The numbering shift** (every coverage agent reached it independently):
ministry grades 1–2 content ≈ platform grade 3; ministry 3 ≈ platform 4;
ministry 4 ≈ platform 5; ministry 5 (Roman numerals, GCD, percent,
proportion/масштаб, decimals to 3dp, triangle classification, prisms &
pyramids, mean & range, coordinates, transformations) is largely NOT in
the primary band at all (pieces exist up in grades 6–7). The platform's
primary band runs one to two years above the ministry's labels.

**Recurring genuine gaps** (never taught anywhere in 3–5): spatial
position/direction vocabulary (1.3б/2.3б), Carroll & Euler–Venn diagram
classification (x.4а), tree diagrams / counting possibilities (3.4в,
4.4г), possible/impossible events (4.4в), negative numbers intro (3.1в),
координатын хавтгайн I мөч (4.3в, 5.3в), transformations — translate /
rotate 90° / axial symmetry (4.3д/е, 5.3д/е), proportion & scale (4.1и,
5.1и), percent (5.1к), volume by unit cubes + surface area of a box
(4.2в/д, 5.2в), цаг тооны бичиг, traditional length units (сөөм, төө,
тохой, алд), composing one's own problems from a model (x.1з) — the
ministry asks for it at EVERY grade, we never do.

**Figures** (the owner's central criterion):
- platform grade 3: 119 figure steps / 40 lessons — every lesson has some;
  practice still mostly text (≈2 of 9 items figure-based in the best unit).
- platform grade 4: 73 / 40 — teach steps carry figures, practice ≈ text;
  data lessons narrate charts instead of showing them.
- platform grade 5: **0 figures in the entire course** (g5build has no
  figure helpers — the author literally had no vocabulary for them).
  Worst offenders include a pictograph lesson with no pictograph, a
  bar-graph lesson where bars are described in words, composite-area
  problems described verbally.
- Renderer gaps to close for the band: FigureSpec has no barChart /
  pictograph / tallyChart / clockFace / placeValueBlocks modes (data
  lessons currently fake charts with dot groups). Adding modes to
  RatioFigure + lib/genmath-interactive FigureSpec is component work that
  unlocks the data units.

## Execution order (each step gated like the ЭЕШ alignment)

0. OWNER DECISION (blocking step 1, asked 2026-08-13): renumber the band
   so platform grade N = ministry grade N (recommended; existing G3→G2,
   G4→G3, G5→G4, author new G1 + G5), or keep platform numbering and
   backfill. Everything below is written option-A-first but survives B.
1. FigureSpec new modes: barChart, pictograph, tallyChart, clockFace,
   placeValueBlocks (+ builder helpers in g-build files, + widget contract).
2. Re-figure platform grade 5 (or its renumbered successor) end to end —
   every lesson teach-with-figure → try-with-figure, figure-based practice.
3. Close per-grade objective gaps with new lessons/units, ministry wording
   (Mongolian titles like the ЭЕШ hub's titleMn), coverage map + test
   asserting all 108 objectives → unit mappings (mirror MOE_COVERAGE /
   esh-course.test.ts).
4. Author the missing year(s): ministry G1 (and G5 under option A) as full
   8-topic courses via workflow fan-out, g4build-style figure discipline,
   figure-based practice (merge/remove groups for +/−).
5. Banks/exams re-cut for affected grades; placement updated; mn-terms
   glossary extended with primary vocabulary (баримжаалах, хавтан загвар,
   Карроллын диаграмм, ...).

Standing rule inherited by every step: no lesson ships in this band with a
figure-less teach step, and no practice set ships majority-text — the
document's own хэрэглэгдэхүүн catalog (counting objects, number lines,
hundred squares, tangram, geoboard) is the reference vocabulary.
