# Practice-test authoring — pointer

**The operating manual for generating practice tests lives in
`.claude/skills/` (added 2026-07-08):**

- `.claude/skills/practice-test-authoring/SKILL.md` — core manual, read
  FIRST: zero-mistake pipeline (builder scripts → sympy `verify[]` →
  figures-from-code → gate → adversarial blind re-solve → render QA),
  distractor doctrine, solution standard, MathText rendering contract,
  figure standard (monochrome, dark-mode-invert-safe).
- `.claude/skills/esh-practice-test/SKILL.md` — ЭЕШ hub: Section 1
  (36 MCQ A–E) + Section 2 (4×7 pts fill-in) blueprints measured from
  the 20 real past papers, schemas, MN style guide + glossary, 51-tag
  taxonomy, slot grammar, wiring into `lib/esh-questions.ts` /
  `lib/esh-section2.ts`.
- `.claude/skills/sat-practice-test/SKILL.md` — Digital SAT Math:
  2×22-question adaptive modules, MCQ A–D + SPR entry rules, domain
  weights, data layout `data/sat/<testId>.json` (hub is Coming Soon —
  the skill fixes the format ahead of the build).
- `.claude/skills/ib-practice-test/SKILL.md` — IB Math AA/AI SL/HL:
  paper tables (80/110/55 marks), command terms, M/A/R/AG markscheme
  standard, data layout `data/ib/<course>-<level>/<testId>/paperN.json`.

**Mechanical gate:** `scripts/verify-practice-test.py`
(alias `npm run verify:ptest -- <files>`; `--all-esh` sweeps the bank;
`--strict` for newly authored tests, requires `verify[]` sympy
assertions on every question; `--strip` emits a blind copy for the
adversarial re-solve). The existing 54-file ЭЕШ bank passes with 0
errors; `Test-3B-Q20`'s duplicate option (audit open item) is
allowlisted in `KNOWN_ISSUES` inside the script.

Locked policies the manual encodes (from `expansion-vision.md` §4):
100% self-authored content (emulate format, never transcribe real
questions); ЭЕШ content Mongolian-only, SAT/IB content English-only.
