# Phase 2 — Section 1 JSON corruption audit report

**Generated:** 2026-05-13
**Author:** Claude Opus 4.7 (Phase 2 Step 1; no edits yet — hard stop after this report per Khas's rule)

This is the planning artifact for the Phase 2 rebuild of Section 1 JSON content. Reading order:

1. What the existing audit memory already told us (`memory/practice-test-audit.md`)
2. Inventory: every Section 1 JSON file + the source PDFs that should ground them
3. What the two prior "fix" commits actually touched (revert target list)
4. Per-file rebuild strategy with effort estimates
5. Open risks before we proceed

---

## 1. What `memory/practice-test-audit.md` already told us

### Headline
**The JSON files are corrupted against the textbook source.** Wrong option text, wrong question bodies, shuffled options. The headline corruption pattern was confirmed on Test-2A; other tests have not been verified at the same depth.

### Confirmed corruptions in Test-2A (verified against textbook pages 11–13)
- **Q2 body** — `/5⁴` denominator wrong; textbook: `(3⁵·(27²)³·√3) / (81·9^(5/4))`
- **Q6 exponent** — corrupted as `(x²-x-4)^{3/4 - 2}`; textbook: `(x²-x-4)^(3/4) − 2 = 6` (the `−2` is OUTSIDE the exponent)
- **Q7 option D text** — off by factor of 2; textbook D = `5√2+2√6`
- **Q13 option C text** — textbook C = `1 + √2`
- **Q22 options C/D** — duplicate in JSON; textbook C = `20^(13^(10^(2^y)))`
- **Q26 options B/C/D text** — textbook C = `7/15`
- **Q27 option ordering** — shuffled; textbook B = `[[1,6],[0,1]]`

### Confirmed bad fixes shipped in earlier commits
- **Test-2A-Q7**: shipped commit `42ce741` flipped stored D→A. Textbook says **D is correct** — the JSON option D text was wrong, not the stored answer. **Must revert.**
- **Test-2A-Q27**: shipped commit `42ce741` flipped stored B→C. Textbook says **B is correct** — the JSON options were shuffled, not the stored answer. **Must revert.**

### Other fixes from `42ce741` / `413ab59` — NOT yet verified against source
The memory file flags these as needing verification before we can trust them:
- `Test-2B-Q17` (answer flip A→D)
- `Test-5A-Q34` (option text 2731/4096 → 2732/4096)
- `Test-4B-Q31` (option E swapped)
- `Test-7B-Q21` (option D swapped)
- `Test-2B-Q2` (solution prose rewrite)
- `Test-2B-Q6` (solution prose rewrite)
- `Test-3A-Q22` (solution prose rewrite)

### Open items the prior audit never verified
- `Test-3B-Q20` (option D)
- `Test-1B-Q28` (precision; stored A may actually be the textbook answer)
- `Test-7A/7B` numbering anomaly (was Q2-Q37; "renumbered" to Q1-Q36 — may have been an extraction artifact, not a real renumber)
- `Test-3B-Q15` (duplicate statements I and III)
- `Test-4B-Q31` (duplicate options C and E)
- `Test-7B-Q21` (duplicate options B and D)

### The misleading "Resolved 2026-05-08" banner at the top of the memory file
The memory file's banner claims the audit was resolved with 9 fixes shipped. **This is premature.** The 9-fix commit itself contains at least 2 wrong fixes (Q7 and Q27 above), and the broader corruption pattern (estimated double-digit-percentage of questions in test2a) has not been addressed for any OTHER test variant. The "resolved" banner should be flipped or removed at the end of Phase 2.

---

## 2. Inventory

### Section 1 JSON files in scope (34 files, 1,224 questions)

| File | Questions | Source PDF | Status |
|---|---|---|---|
| `data/questions/test1a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test1b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test2a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | **partially audited, known corruption** |
| `data/questions/test2b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified; 2 prose rewrites from `413ab59` |
| `data/questions/test3a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified; 1 prose rewrite from `413ab59` |
| `data/questions/test3b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test4a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test4b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified; 1 option-E fix from `42ce741` |
| `data/questions/test5a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified; 1 numerator fix from `42ce741` |
| `data/questions/test5b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test6a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test6b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified |
| `data/questions/test7a.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified; renumbered Q2-Q37 → Q1-Q36 in `42ce741` (may be artifact) |
| `data/questions/test7b.json` | 36 (Q1–Q36) | `~/Desktop/ESH-nom.pdf` | unverified; 1 option-D fix from `42ce741` |
| `data/questions/2021a.json` | 36 | `~/Desktop/prev_tests/2021A.pdf` (scanned, OCR needed) | unverified |
| `data/questions/2021b.json` | 36 | `~/Desktop/prev_tests/2021B.pdf` (scanned) | unverified |
| `data/questions/2021c.json` | 36 | `~/Desktop/prev_tests/2021C.pdf` (scanned) | unverified |
| `data/questions/2021d.json` | 36 | `~/Desktop/prev_tests/2021D.pdf` (scanned) | unverified |
| `data/questions/2022a.json` | 36 | `~/Desktop/prev_tests/2022A.pdf` | unverified |
| `data/questions/2022b.json` | 36 | `~/Desktop/prev_tests/2022B.pdf` | unverified |
| `data/questions/2022c.json` | 36 | `~/Desktop/prev_tests/2022C.pdf` | unverified |
| `data/questions/2022d.json` | 36 | `~/Desktop/prev_tests/2022D.pdf` | unverified |
| `data/questions/2023a.json` | 36 | `~/Desktop/prev_tests/2023A.pdf` | unverified |
| `data/questions/2023b.json` | 36 | `~/Desktop/prev_tests/2023B.pdf` | unverified |
| `data/questions/2023c.json` | 36 | `~/Desktop/prev_tests/2023C.pdf` | unverified |
| `data/questions/2023d.json` | 36 | `~/Desktop/prev_tests/2023D.pdf` | unverified |
| `data/questions/2024a.json` | 36 | `~/Desktop/prev_tests/2024A.pdf` | unverified |
| `data/questions/2024b.json` | 36 | `~/Desktop/prev_tests/2024B.pdf` | unverified |
| `data/questions/2024c.json` | 36 | `~/Desktop/prev_tests/2024C.pdf` | unverified; Q16 / Q17 / Q24 topic-recat 2026-05-12 (not corruption) |
| `data/questions/2024d.json` | 36 | `~/Desktop/prev_tests/2024D.pdf` | unverified; Q17 / Q24 topic-recat 2026-05-12 |
| `data/questions/2025a.json` | 36 | `~/Desktop/prev_tests/ЭШ-2025-Математик-A-хувилбар.pdf` | unverified; Q3 / Q15 / Q23 / Q32 / Q35 / Q24 topic-recat 2026-05-12 |
| `data/questions/2025b.json` | 36 | `~/Desktop/prev_tests/ЭШ-2025-Математик-B-хувилбар.pdf` | unverified; same topic-recat |
| `data/questions/2025c.json` | 36 | `~/Desktop/prev_tests/ЭШ-2025-Математик-C-хувилбар.pdf` | unverified; same topic-recat + Q11 answer correction 2026-05-12 |
| `data/questions/2025d.json` | 36 | `~/Desktop/prev_tests/ЭШ-2025-Математик-D-хувилбар.pdf` | unverified; Q11 answer + Q13 solution rewrite + Q29 typo+answer correction 2026-05-12 |

### Source PDFs

**Past papers — `~/Desktop/prev_tests/` (20 PDFs):**
- `2021A.pdf` (537 KB) through `2021D.pdf` (1.7 MB) — **scanned**, per the figures-workstream memory; need OCR pipeline
- `2022A.pdf` (455 KB) through `2022D.pdf` (465 KB) — text-extractable
- `2023A.pdf` (364 KB) through `2023D.pdf` (419 KB) — text-extractable
- `2024A.pdf` (577 KB) through `2024D.pdf` (568 KB) — text-extractable
- `ЭШ-2025-Математик-{A,B,C,D}-хувилбар.pdf` (~670 KB each) — text-extractable

Also present (out of scope for body extraction, kept as reference for Section 2 answer keys): `2021 part 2 answer key.png`, `2022 part 2 answer key.png`, `2023 answer key.png`, `2024 part 2 answer key.png`.

**Practice tests — `~/Desktop/ESH-nom.pdf` (4.5 MB, 1 file):**
Single textbook ("ЭЕШ-д бэлтгэх МАТЕМАТИКИЙН ТЕСТ, ДЭВТЭР" 6th ed., 2022). Contains all 14 practice tests. Per the prior audit, page 11 ≈ Test 2A start, page 12 ≈ Test 2A mid, page 13 ≈ Test 2A end + Test 2B start. Full per-test page mapping is partial in the memory file — completing it is part of Step 3.

Alternate source observed at `~/Desktop/testbook/` — directories `1b/`, `2a/` … `11b/` with 4 PNG screenshots each. Covers tests beyond the 14 in JSON (8a/8b through 11b are unwired). **Out of scope for Phase 2** — recording its existence in case Phase 3 expands the test catalogue.

---

## 3. Commits to revert in Phase 2 Step 2

### `42ce741` — six "answer-key + duplicate-option" fixes
Touched: `data/questions/test2a.json` (Q7 + Q27), `test2b.json` (Q17), `test4b.json` (Q31), `test5a.json` (Q34), `test7b.json` (Q21). Plus `JOURNAL.md` and `PHASES.md` notes.

**Of these:**
- Q7 + Q27 fixes are **proven wrong** against the textbook — must revert
- Q17 + Q31 + Q34 + Q21 fixes are **unverified** — should also revert and re-derive from source rather than carry forward unconfirmed corrections

### `413ab59` — three solution-prose rewrites
Touched: `data/questions/test2b.json` (Q2 + Q6), `test3a.json` (Q22). Plus `JOURNAL.md` and `PHASES.md` notes.

**Of these:**
- All three are **unverified** prose changes — should revert and re-derive prose from source

### Revert strategy
A single revert commit that restores the pre-commit JSON state for the 9 questions listed above. JOURNAL.md and PHASES.md notes from those commits will be left intact (they're history, not content). The revert commit's message will list each question + reason.

---

## 4. Per-file rebuild strategy & effort estimate

### Past papers — text-extractable PDFs (2022 / 2023 / 2024 / 2025, 16 files, 576 questions)

**Approach:**
1. `pdftotext -layout` extraction (already proven in the figures workstream)
2. Parser that segments the extracted text by question-number anchors (`1.`, `2.`, …, `36.` and `A)`, `B)`, …, `E)` for options)
3. Per-question record built: body + 5 options + answer letter (answer keys are at the end of each PDF — separate parsing)
4. Diff against current JSON, surface mismatches

**Effort estimate:** 4–6 hours of pipeline work to nail the parser on one PDF (likely 2024A as a clean reference), then ~30 min per remaining file for shake-out fixes. **Total: 12–18 hours of automated + ~1 hour per file review = 28–34 hours.**

**Risk:** Math typeset with `\sqrt`, `\frac`, etc. extracts as raw glyph/font codes that need normalization back to LaTeX. The figures workstream already solved part of this; expect to extend that toolkit.

### Past papers — scanned PDFs (2021 A/B/C/D, 4 files, 144 questions)

**Approach:** OCR-then-review. The figures workstream already noted "2021B/C/D scanned PDFs — pdfimages returned page-sized JPEGs only, no figure-level extraction." Same issue here for text.

**Options:**
- **A. Tesseract OCR** on the rasterized pages. Mongolian Cyrillic + math symbol coverage is mixed. Probably ≥70% accurate, needs heavy review.
- **B. Hand-verify against the existing JSON.** Since the JSON was presumably typed from a hand-transcription, the existing JSON may already be close to source — the corruption observed was on the textbook practice tests (test*), not the past-paper PDFs.
- **C. Defer 2021 to a Phase 2.5** — fix 2022–2025 first, verify the corruption pattern is/isn't present in past papers, decide on 2021 separately.

**Recommendation: Option C** for the 2021 scanned set. The audit memory specifically called out the practice-test books as the corruption source; past papers may be clean by comparison. Proving that cheaply before sinking OCR hours into 2021 is the right sequencing.

**Effort estimate (if we do them):** 1–2 hours OCR per file + 1 hour manual cleanup = 8–12 hours total. Or 0 hours if we defer.

### Practice tests — `ESH-nom.pdf` (14 files, 504 questions)

**Approach:** the harder case. One PDF contains all 14 tests, page boundaries are not in JSON. Pipeline:
1. Render every page of `ESH-nom.pdf` to PNG (already done — `output_pages/page_*.png` per the audit memory)
2. OCR or text-extract each page
3. Identify test-number markers ("Тест 1A", "Тест 1B", etc. — confirm exact pattern)
4. Per-test, segment by question number, build records
5. Diff against current JSON

**Risk:** the textbook itself may have OCR artifacts in the existing 504-question JSON if the original extraction used a lossy pipeline. Re-extraction may surface dozens of new corrections per test, not just the 7 known in Test-2A.

**Effort estimate:** 6–8 hours pipeline work, then ~45 min per test for review. **Total: 17–25 hours.**

### Stretch: extraction-fidelity test (Step 4 deliverable)

A new `scripts/verify-source-fidelity.test.ts` that:
- Re-runs the extractor against every PDF
- Asserts the JSON body / options / answer match the extraction (with a tolerance for whitespace normalization)
- Becomes the regression guard so future hand-edits to JSON don't silently drift from source

**Effort:** 2–3 hours after the extractor is stable.

---

## 5. Open risks & decisions needed before Step 2

### 1. Scope for the 2021 scanned PDFs
Per the recommendation above, propose deferring 2021 to a Phase 2.5 OCR pass. Want my recommendation confirmed before we lock in scope.

### 2. ESH-nom.pdf — does the existing extraction-to-JSON pipeline exist anywhere?
The current `data/questions/test*.json` came from somewhere. If a former extraction script lives in git history or in `outputs/audit-results/`, we may be able to inspect its output style and decide whether to forward-port that pipeline or replace it entirely. Worth a quick `git log -- scripts/` check before writing the extractor from scratch.

### 3. Source-fidelity vs. cosmetic correction
The audit memory notes "cosmetic option-order on Test-2A-Q19/Q27" as deferred. Cosmetic option reorderings (where the answer letter still points to the correct value) are technically corruption against the source but don't change correctness. **Question:** treat these as required fixes in Phase 2 or punt to a separate pass?

### 4. Answer-key extraction
For past papers, the answer keys are separate from the question pages (last page of each PDF, or a separate PNG for Part 2). Parsing both halves and joining by question number adds complexity. Worth the effort upfront; flagging now.

### 5. PDF tooling language
The audit memory doesn't dictate Python vs TypeScript for the extractor. The figures workstream used Python (PyMuPDF + pdfimages). I'd lean Python for parity with that toolkit. Confirm preference before I start writing.

---

## 6. Total estimated effort

| Bucket | Hours (low) | Hours (high) |
|---|---|---|
| Step 2 revert commit | 1 | 2 |
| Step 3 extractor pipeline (text-extractable PDFs) | 12 | 18 |
| Step 3 extractor pipeline (ESH-nom textbook) | 6 | 8 |
| Step 3 diff report generation | 2 | 3 |
| Step 4 per-question review + apply (16 past + 14 practice = 30 files) | 15 | 30 |
| Step 4 fidelity test | 2 | 3 |
| Step 5 smoke + push + spot checks | 1 | 2 |
| 2021 OCR (if NOT deferred) | 8 | 12 |
| **Total (excluding 2021 OCR)** | **39** | **66** |
| **Total (including 2021 OCR)** | **47** | **78** |

Wide range because (a) the per-question review rate depends entirely on how many false-positive diffs the extractor surfaces, and (b) math-typesetting extraction quality on each PDF is unknown until I run it.

---

## Hard stop here

Per your rule: no edits, no commits, no extractor work yet. The next move is yours. Specifically, I need answers to:
- (1) Is the 2021-deferral recommendation OK?
- (2) Python or TS for the extractor?
- (3) Cosmetic option-reorder corrections — in scope or out?
- (4) Anything to add to the revert list in Step 2 beyond the 9 questions from `42ce741` + `413ab59`?

Once those are answered, I move to Step 2 (the revert commit) and then Step 3 (the extractor + diff report — which is the next hard stop).
