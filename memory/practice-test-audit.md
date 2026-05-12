# Practice-test audit (2026-05-07)

> **Resolved 2026-05-08.** The 9 confirmed fixes from this audit (Part A answer-key restore, Part B test7a/test7b renumber, Part C test2a Q2/Q6/Q13/Q22/Q26 body+option corrections, Part E test7b Q21 swap) shipped in a single source-aligned cleanup commit. The headline finding still applies: future patches must verify against `Desktop/ESH-nom.pdf` before editing JSON. See JOURNAL `2026-05-08` entry and PHASES `Recently shipped` for the full diff list. Open items (34 image-dependent questions, test7a Q34 inequality recheck, cosmetic option-order on Test-2A-Q19/Q27, full Cyrillic re-extraction) remain deferred.

## What this is
A 504-question hand-audit of the 14 paid practice tests (`data/questions/test1a.json` through `test7b.json`), compared against the original textbook source (`output_pages/page_*.png`, scraped from "ЭЕШ-д бэлтгэх МАТЕМАТИКИЙН ТЕСТ, ДЭВТЭР" 6th ed., 2022, by Т.Түвшинжаргал & Ш.Уранчимэг).

## The headline finding
**The JSON files are corrupted against the textbook source.** Many "stored answer wrong" findings from the initial audit pass were actually JSON transcription errors — the textbook answer keys are correct, but the JSON has wrong option text, wrong question bodies, and shuffled option order.

This means:
- The math I did during the audit was correct.
- BUT — when JSON had wrong option text under a given letter, I'd compute the right answer, see it didn't match JSON's letter-X text, and conclude "stored answer X is wrong." In reality the stored answer was right; only the JSON's option text was wrong.

## Examples (verified against textbook page 11, 12, 13)

| Question | What audit said | What textbook actually has |
|---|---|---|
| Test-2A-Q2 | Body has `/5⁴` denominator → 3²⁶/5⁴ doesn't match any option | Textbook body: `(3⁵·(27²)³·√3) / (81·9^(5/4))` → simplifies to 3¹⁷ → stored C correct |
| Test-2A-Q6 | Exponent corrupted as `(x²-x-4)^{3/4 - 2}` | Textbook: `(x²-x-4)^(3/4) − 2 = 6` (the `−2` is OUTSIDE the exponent) → 41 → stored D correct |
| Test-2A-Q7 | Stored D `(5√2+2√6)/2` off by factor 2; "fix to A" | Textbook D is `5√2+2√6` (no /2) → matches the correct slope → **stored D was always correct** |
| Test-2A-Q13 | Hexagon area = 1+√2 doesn't match any option (closest stored C = 1+√2/2) | Textbook C is `1 + √2` → matches → **stored C was always correct** |
| Test-2A-Q22 | Options C and D both "2^(10^(13^(20^y)))" — duplicate | Textbook C is `20^(13^(10^(2^y)))` (inverted tower) → no duplicate → stored D correct |
| Test-2A-Q26 | P=7/15 not in options (stored C=7/30 wrong) | Textbook C is `7/15` → matches → **stored C was always correct** |
| Test-2A-Q27 | M³=[[1,6],[0,1]]=option C, not stored B | Textbook B is `[[1,6],[0,1]]` (options shuffled in JSON) → **stored B was always correct** |

## What the shipped commits got wrong

`42ce741` (fix answer-key + duplicate-option errors) and `413ab59` (rewrite muddled solution prose) shipped 9 fixes before this textbook verification was done. **At least 2 are actively wrong against the source:**

- **Test-2A-Q7** flipped stored D→A. Textbook says D is correct. Need to revert + fix JSON option D text.
- **Test-2A-Q27** flipped stored B→C. Textbook says B is correct. Need to revert + fix JSON option B text + restore correct option order.

The other 7 fixes (Test-2B-Q17, Test-5A-Q34, Test-4B-Q31, Test-7B-Q21, plus 3 prose rewrites) haven't been verified against the textbook yet. Some may be fine, some may be similarly wrong. **Need page-by-page verification before trusting.**

## The right approach (next time)

The JSON-vs-source corruption rate is high enough that **patching individual JSON entries based on the JSON alone makes things worse, not better.** Two viable paths:

**A. Re-extract the JSON from the textbook source.** Better OCR/parse pipeline. Eliminates transcription errors at the root. Most rigorous.

**B. Per-question source verification.** For each flagged question, look up the textbook page, compare option-by-option, then patch the JSON to match the source. Slow (504 questions × ~5 min each = ~40 hours).

**C. Hybrid.** Trust stored answers (the math checks out at the source level). Patch only the JSON option/body text where it's visibly wrong, on a per-test basis as users surface confusions. Doesn't fix systemic issue but unblocks launch.

## Reference materials

- Per-test audit reports (now superseded by this finding): `outputs/audit-results/test*-report.md` and `AUDIT-SUMMARY.md`
- Textbook source pages: `output_pages/page_*.png` (472 PNG renders, ~236 unique pages)
- Page-to-test mapping (partial, from this session):
  - Page 3-5: Test 1A
  - Page 6-9: Test 1B (approx)
  - Page 11: Test 2A questions 1-12
  - Page 12: Test 2A questions 13-26
  - Page 13: Test 2A questions 27-36 (start)
- Practice Test 1 reference (text, English): `practice_test_1_solutions.md` — was used to validate test1a (35/36 match modulo translation)

## Open follow-up questions for Khas

Pending decisions from the AskUserQuestion round before the textbook re-check changed everything:
- Test-2A-Q2 (body): user provided correction `(3⁵·(27²)³·√3)/(81·9^(5/4))` ✓ verified against textbook
- Test-2A-Q13 (option C): user said "1+√2" ✓ verified against textbook
- Test-3B-Q20 (option D): user said "log₃(1/(xy^(2/3)))" — NOT YET verified against textbook
- Test-2A-Q22 (duplicate options C/D): user said C should be "20^(13^(10^(2^y)))" ✓ verified against textbook
- Test-1B-Q28 (precision): user picked "Flip to D (2.2)" — but stored A might actually be the textbook answer; needs verification
- Test-7A/7B numbering anomaly (Q2-Q37 instead of Q1-Q36): user picked "Renumber to Q1-Q36" — but might be a JSON-extraction artifact too

Also still open from Part 2 (never asked):
- Test-2A-Q26 — actually, now confirmed: textbook C is 7/15. Stored C is correct. Just need to fix JSON options B/C/D text.
- Test-3B-Q15 (duplicate statements I and III) — need textbook verification
- Test-4B-Q31 (duplicate options C and E) — need textbook verification
- Test-7B-Q21 (duplicate options B and D) — need textbook verification
- Test-2A-Q6 (corrupted exponent) — confirmed against textbook: `(x²-x-4)^(3/4) − 2 = 6`

## TL;DR for next session

If "continue audit" or "fix the practice tests" comes up: **don't patch the JSON without verifying each change against the corresponding textbook source page.** The previous audit pass produced 9 commits, of which at least 2 are actively wrong. Revert path is open via `git revert 42ce741 413ab59` if needed.

---

# Topic canonicalization audit (2026-05-12)

## Trigger
Q35 (matrix system + inverse) and similar questions were showing up as **БУСАД** on the analytics topic table, hiding real curriculum categories. Audit traced 204 of 720 Section 1 questions (≈28%) being classified as "other" because the raw `topic` field used non-canonical strings (`vectors`, `matrices`, `алгебр`, `coordinate geometry`, etc.) or because the question genuinely fell outside the 10 canonical topics.

## Decisions

**Added 4 new canonical topics** (Шугаман алгебр includes vectors per Khas's directive):
| Key | MN label | Covers |
|---|---|---|
| `arithmetic` | Арифметик | Rounding, scientific notation, fraction arithmetic, mixture problems |
| `set_theory` | Олонлог | Set unions/intersections, irrational-number subsets, inclusion-exclusion |
| `linear_algebra` | Шугаман алгебр | Matrices (transformation, inverse, Cayley-Hamilton), determinants, vectors in ℝⁿ |
| `complex_numbers` | Комплекс тоо | Complex arithmetic, complex roots of quadratics |

**Aliased to existing canonical keys** (no new topic; `canonicalizeTopic` handles 181 questions via the alias map without touching their JSON):
- MN-cased: `алгебр`→algebra, `геометр`→geometry, `анализ`→calculus, `статистик`→statistics, `магадлал`→probability, `тригонометр`→trigonometry, `функц`→functions, `дараалал`→sequences, `комбинаторик`→combinatorics, `аналитик геометр`→geometry
- EN aliases: `coordinate geometry`→geometry, `solid geometry`→geometry, `polynomials`→algebra, `equations`→algebra, `sequences and series`→sequences, `exponents and logarithms`→logarithms, `exponents`→logarithms

**Directly updated 24 question JSON entries** (raw `topic` was `"other"` or `"Логик"` — couldn't be inferred from alias alone):
- Q3 ×4 variants (irrational-numbers set): `other` → `set_theory`
- Q15 ×4 (set intersection): `other` → `set_theory`
- Q16 ×2 (2024C/D complex quadratic): `other` → `complex_numbers`
- Q23 ×3 (2025A/B/C 3D vectors): `other` → `linear_algebra`
- Q32 ×5 (transformation matrices): `other` → `linear_algebra`
- Q35 ×5 (matrix system + inverse — Khas's original example): `other` → `linear_algebra`
- Test-2021D-Q18 (raw `Логик`, set-theory body): `Логик` → `set_theory`

## Outcome
- `БУСАД` count: 204 → 1 (`Test-2021D-Q18` fully resolved → 0 after the final edit)
- New topic distribution surfaces 14 distinct topics on the analytics topic mastery table instead of the prior 10 + a massive "other" bucket
- `verify:canonicalize` expanded from 10 cases to 24, all pass
- Q35 now correctly labeled `Шугаман алгебр` — addresses Khas's surfaced example

## How to extend
- New raw-topic value seen in JSON: prefer adding to `TOPIC_ALIASES` in `lib/esh-questions.ts` rather than touching every test file
- New canonical topic: add to `TOPIC_LABELS` + `TOPICS` array
- Update `scripts/verify-canonicalize.ts` with a regression case

## Topic label fixes (2026-05-12, follow-up)
- `Линейн алгебр` → `Шугаман алгебр`. "Линейн" is a Russian loanword; "шугаман" is the modern Mongolian. Khas's decision after the 2026-05-12 review.
- `Тригнометр` → `Тригонометр`. Was a typo missing the middle "о"; the rest of the codebase + question data already used the corrected spelling.

