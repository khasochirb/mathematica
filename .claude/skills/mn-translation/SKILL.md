---
name: mn-translation
description: >
  Operating manual for Mongolian localization — the extract/translate/apply
  pipeline, the terminology glossary, math-notation rules, and the per-topic
  workflow. Read before translating any topic to Mongolian, fixing any MN
  mirror, or reviewing bilingual parity. The pipeline lives in scripts/i18n/;
  never hand-edit a data/genmath/*-mn/*.json.
---

# Mongolian Translation — Operating Manual

Mongolian is half the product: ЭЕШ prep is Mongolian-first, and General
Math mirrors serve students who learn better in their own language.
Status: Grades 6, 7, 8 fully mirrored; Grades 9–12 and Geometry pending.

## The iron rule

**MN mirror JSON is generated, never hand-edited.** The pipeline
guarantees structural parity with the English source (same lessons, same
problems, same `check[]`, same figures). A hand edit desyncs the mirror
and gets silently destroyed on the next regeneration. Fixes go into the
translation table, then re-apply.

## The pipeline (scripts/i18n/)

- `mn_walk.py` — the shared walker. Visits every translatable string of
  a topic JSON in one deterministic order (titles, blurbs, lesson prose,
  facts incl. latex/note fields, widget-config prose, figure group
  labels, problems, options, solutions). Extract and apply use the SAME
  walker, so index i in the source list is index i at apply time.
- `mn_extract.py <grade> <slug>` — emits
  `i18n-work/mn_<grade>_<slug>_src.json` as `[{"i": n, "en": "..."}]`.
- `mn_apply.py <grade> <slug>` — loads `i18n-work/mn_<grade>_<slug>_tr.py`
  (a Python file exporting `MN = {index: "translation"}`), re-walks the
  EN source, swaps every string, and writes
  `data/genmath/<grade>-mn/<slug>.json`. Hard-fails on: count mismatch,
  missing index, order drift (EN text at position i must match the
  extracted text exactly), stray single-asterisk emphasis, and
  CYR-IN-MATH (see below).

Work dir is `./i18n-work/` (gitignored) or `$MN_WORKDIR`. Translation
tables for big topics split into `_tr_a.py` / `_tr_b.py` (`MN_A`/`MN_B`
dicts) merged by a small `_tr.py` loader — keeps any single file
editable.

## Per-topic workflow (the proven loop)

1. `python3 scripts/i18n/mn_extract.py <grade> <slug>` → note the count.
2. Read ALL source strings in chunks before translating any — you need
   the whole topic's context to keep terminology consistent.
3. Write the translation table(s). Verify coverage:
   every index 0..N-1 present, no gaps (a 3-line python check).
4. `python3 scripts/i18n/mn_apply.py <grade> <slug>` — must print WROTE.
5. Register in `lib/genmath-lessons.ts`: add the import
   (`import gXFooMn from "@/data/genmath/<grade>-mn/<slug>.json";`) AND
   the `GENMATH_TOPICS_MN` map entry (`"<slug>": gXFooMn as GenMathTopic`).
   The map is slug-keyed and grade-agnostic — a Grade 9 slug colliding
   with a Grade 7 slug would shadow it; check before registering.
6. Gate: `npm run verify:genmath` (check count grows) + `npx tsc --noEmit`.
7. Commit ONE topic per commit: `Grade <g> MN: <slug> mirror (<k>/<n>)`.
8. After a grade completes: `npm run build` + a Playwright walk of the
   MN routes (see `qa-verification`).

Routes already call `getGenMathTopicLocalized(slug, lang)` — no page
wiring is needed for grades 6–9; check the grade's pages once before
starting a new grade.

## Math-notation rules (each one is a shipped-bug scar)

1. **CYR-IN-MATH:** No Cyrillic inside `$...$` except inside
   `\text{...}`. Formula words localize as
   `$\text{хувийн алдаа} = ...$`; bare Cyrillic in math mode breaks
   KaTeX and fails the apply scan.
2. **Symbols stay Latin.** Coin outcomes (HH, HT, TH, TT), point names
   (A, B, C), variables (x, P, r, t), function letters — Latin even in
   Mongolian prose. Gloss once when first introduced:
   `HH, HT, TH, TT (H = сүлд, T = зураас)`.
3. **Escaping:** the tables are Python string literals — `\\times`,
   `\\frac`, `\\$` for a literal dollar sign. In single-quoted Python
   strings never end in `\\'` (apostrophe-after-backslash parse bug we
   hit — avoid apostrophes near escapes entirely).
4. **Numbers and units:** keep `$1{,}200$` thousand-separators, keep
   units as in EN (см, м, кг, мл are fine in prose; inside math use
   `\text{см}`), keep π-exact vs decimal convention per problem.
5. **Emphasis:** only `**bold**` renders. Single `*italics*` in EN may
   carry over only where EN had it; never introduce new single-asterisk.
6. **Currency:** worked examples use \\$ (dollars) as in EN source —
   don't convert to ₮ (changes the arithmetic difficulty and desyncs
   check[] plausibility).

## Terminology glossary (canonical — do not improvise synonyms)

Core: тэгшитгэл (equation) · тэнцэтгэл бус (inequality) · пропорц,
пропорциональ хамаарал · пропорциональ тогтмол (constant of
proportionality) · үржүүлэгч (multiplier) · хувь (percent) · хувийн
өөрчлөлт (percent change) · хувийн алдаа (percent error) · нэмэгдэл
(markup) · хямдрал (discount) · татвар (tax) · цайны мөнгө (tip) ·
шимтгэл (commission) · энгийн хүү (simple interest) · үндсэн дүн
(principal) · рационал тоо (rational number).

Geometry: масштаб (scale) · масштабын коэффициент (scale factor) ·
нэмэлт өнцөг (complementary) · дүүргэгч өнцөг (supplementary) · эсрэг
өнцөг (vertical angles) · зэргэлдээ өнцөг (adjacent) · гурвалжны
тэнцэтгэл бус (triangle inequality) · тойргийн урт (circumference) ·
диаметр, радиус (Latin-derived, keep) · нийлмэл дүрс (composite
figure) · призм (prism) · эзэлхүүн (volume) · гадаргуугийн талбай
(surface area) · дэлгээс (net).

Probability: магадлал (probability) · боломжит үр дүнгийн орон (sample
space) · онолын/туршилтын магадлал (theoretical/experimental) ·
гүйцээлт (complement) · нийлмэл үзэгдэл (compound event) · хараат бус
(independent) · буцааж тавихгүй (without replacement) · тооллын зарчим
(counting principle) · мод диаграм (tree diagram) · загварчлал
(simulation) · хүлээгдэх тоо (expected count).

Statistics: популяци (population) · түүвэр (sample) · бүрэн тооллого
(census) · хазайлт (bias) · хялбар түүвэр (convenience) · сайн дурын
хариу (voluntary response) · дутуу хамрах (undercoverage) · дүгнэлт
(inference) · барих–дахин барих (capture–recapture) · дундаж (mean) ·
медиан (median) · хэт утга (outlier) · далайц (range) · ДАХ — дундаж
абсолют хазайлт (MAD) · тархалт (spread) · цэгэн график (dot plot).

Grade 8 anchors: бодит тооны систем, зэрэг ба стандарт бичлэг, язгуур,
шугаман функц, хамаарлын график (scatter plot).

UI/recurring section names: Бодсон жишээнүүд (Worked examples) · Өөрөө
туршиж үз (Try it yourself) · Түргэн шалгалт (Quick check) · Тоглож үз
(Play with it) · Сонирхолтой баримт (Fun fact) · Эргэн дүгнэлт (Recap) ·
Юу сурснаа эргэн харъя (What you learned).

When a topic introduces a new term, add it to this glossary in the same
commit — the glossary is the contract for the next 40 topics.

## Style

- Register: friendly-instructional «чи» (matching the EN "you"), not
  formal «та». Keep the EN's energy — jokes translate, don't flatten.
- Guillemets «...» for quotes (matches existing mirrors).
- Proper names stay as-is (Паскаль, Ферма, Галилео get standard
  Mongolian Cyrillic renderings; product names like RAND stay Latin).
- Translate meaning, not word order — Mongolian SOV will reorder most
  sentences; that's correct, not drift. Drift protection is structural
  (the walker), not literal.
