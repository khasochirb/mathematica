---
name: ib-practice-test
description: >
  Generate IB Mathematics practice papers for the /practice/ib hub —
  Analysis & Approaches or Applications & Interpretation, SL/HL, Papers
  1–3, with IB-style multi-part questions and M/A/R markschemes, in
  English, matching real IB exam format and marking exactly. Read
  practice-test-authoring (core manual) first.
---

# IB Mathematics Practice Paper — Hub Skill

Prerequisite: `.claude/skills/practice-test-authoring/SKILL.md`.

**Language: ALL content in English.** **Never reproduce a real IB
question** — emulate structure, command terms, mark allocation, and
difficulty with new problems (`memory/expansion-vision.md` §4.3/§4.7).

The IB hub is currently Coming Soon (`app/practice/ib/page.tsx`). This
skill fixes the paper format and data layout ahead of the UI build. The
site pitches "IB Math HL · IB Math SL"; the default course is
**Analysis & Approaches (AA)** — author AA first, AI later using the
same machinery.

---

## 1. Paper anatomy (current syllabus, first assessment 2021)

| Course·Level | Paper | Time | Marks | Calculator | Shape |
|---|---|---|---|---|---|
| AA SL | Paper 1 | 90 min | 80 | **No** | Section A short (~5–6 q, ≈40 marks) + Section B long (~3 q, ≈40 marks) |
| AA SL | Paper 2 | 90 min | 80 | GDC required | Same A/B split |
| AA HL | Paper 1 | 120 min | 110 | **No** | Section A (~6–9 q) + Section B (~3–4 q) |
| AA HL | Paper 2 | 120 min | 110 | GDC required | Same A/B split |
| AA HL | Paper 3 | 60 min | 55 | GDC required | 2 extended problem-solving questions (~25–30 marks each) |
| AI SL | Paper 1 | 90 min | 80 | GDC required | ALL short questions (no Section B) |
| AI SL | Paper 2 | 90 min | 80 | GDC required | Extended-response questions |
| AI HL | Paper 1 | 120 min | 110 | GDC required | All short |
| AI HL | Paper 2 | 120 min | 110 | GDC required | Extended |
| AI HL | Paper 3 | 60 min | 55 | GDC required | 2 extended investigations |

- AA Paper 1 is the ONLY calculator-free paper. Author its arithmetic
  accordingly: exact values, friendly numbers, answers in exact form
  ($\frac{\pi}{3}$, $2\sqrt{5}$, $\ln 3$).
- Every question header carries `[Maximum mark: N]`; parts are
  (a), (b), (c)…, subparts (i), (ii); each part shows its bracket
  `[2]`, `[3]` and part marks sum to the question maximum.
- Section A questions run ≈4–8 marks, easiest first. Section B
  questions run ≈12–20 marks, scaffolded (early parts feed later
  parts), and the final Section B question is the hardest on the paper.

## 2. Topic blueprint

Spread marks across the five syllabus topics in proportion to their
syllabus weight. Approximate share of assessment marks:

| Topic | AA SL | AA HL | AI SL | AI HL |
|---|---|---|---|---|
| Number & Algebra | ~16% | ~19% | ~13% | ~14% |
| Functions | ~17% | ~15% | ~26% | ~20% |
| Geometry & Trigonometry | ~21% | ~24% | ~15% | ~22% |
| Statistics & Probability | ~22% | ~16% | ~30% | ~25% |
| Calculus | ~24% | ~26% | ~16% | ~19% |

Per paper, every topic appears at least once; a topic's share may swing
±8 pts on a single paper (the pair of papers together should hit the
blueprint). AA leans calculus/trig-proof; AI leans statistics,
modelling, and financial math. HL-only content (AA: complex numbers as
`re^{iθ}`, proof by induction/contradiction, vectors in 3D lines &
planes, advanced integration, Maclaurin; AI: matrices, graph theory,
transformations, further regression/χ², differential equations) may
only appear on HL papers.

## 3. Command terms (use EXACTLY these, with their contracts)

| Term | Contract |
|---|---|
| **Write down** | No working expected — 1–2 marks, answer only |
| **Find / Calculate / Determine** | Working expected; method marks available |
| **Show that** | The result is GIVEN in the stem. Working must derive it without assuming it; final mark is AG (no A mark for the printed answer). The printed target must be EXACTLY correct — verify it with sympy; an error here is fatal |
| **Prove** | Formal argument, every step justified (R marks) |
| **Verify** | Substitute/confirm — cheaper than prove |
| **Hence** | MUST use the previous part's result; a from-scratch method earns no marks — say "hence" only when the link is real |
| **Hence or otherwise** | Previous result is the intended path but alternatives earn full marks |
| **Sketch** | Approximate curve with key features (intercepts, asymptotes, extrema) labeled; not to scale |
| **Draw** | Accurate, to scale, ruler-and-grid quality |
| **State / Comment / Justify / Deduce** | Words, brief; R marks |

## 4. Markscheme standard (this is what makes it IB)

Every part carries a markscheme array whose marks sum to the part's
bracket. Mark codes:

- `M1` — method mark: a valid attempt (define what counts: "attempt to
  apply product rule — at least one term correct").
- `A1` — accuracy/answer mark, usually dependent on the preceding M.
- `R1` — reasoning mark (justification sentence, test conclusion).
- `AG` — "answer given": closes a *show that*; never award A1 for the
  printed target.
- `(M1)` — implied mark (may be awarded if implied by later work).
- `FT` — note follow-through where a wrong earlier answer still earns
  later marks ("FT from (a)").

Conventions to encode:

1. **3 significant figures rule**: unless the answer is exact or the
   question says otherwise, final answers to 3 sf. Markscheme notes
   "accept 2.35 (2.34521…)". Intermediate working keeps ≥4 sf. Author
   answers so 3 sf is unambiguous (avoid values like 2.9996).
2. On GDC papers, "solve by GDC" is a full-marks path — the markscheme
   line reads e.g. `x = 1.86 (M1)(A1)` with a note "award (M1) for a
   sketch/table method". Never require by-hand algebra for marks on a
   GDC paper unless the command term is *show that*/*prove*.
3. Radians are the default for calculus with trig; degree usage is
   penalized where it changes the answer — state units explicitly in
   stems.
4. Only formula-booklet formulas are assumed (quote the booklet section
   in the solution when used). Anything off-booklet must be derived or
   given in the stem.
5. Figures/diagrams: label "diagram not to scale" when true (core §8
   still demands exact topology).

## 5. Question design patterns

- **Section A** items: single-skill, 2–3 parts max, 4–8 marks
  (e.g. "(a) Write down the period [1]; (b) Solve f(x)=1 for
  0 ≤ x < 2π [3]").
- **Section B** items: one context, 4–7 parts, 12–20 marks, difficulty
  ramps within the question; classic frames — curve + tangent + area
  (AA), distribution + probability + expectation + hypothesis flavor
  (AI/stats), 3D triangle/vector setup (HL).
- **Paper 3 (HL)**: an investigation narrative — introduce an object,
  compute small cases, conjecture, prove/generalize. Parts walk the
  student; total ~25–30 marks; it is acceptable (expected) that the
  final parts are genuinely difficult.
- Scaffolding math must be *consistent end-to-end*: if (a) asks to show
  $f'(x) = 3x^2 - 4$, every later part uses exactly that derivative —
  builder-script shared variables (core §3) make this automatic.

## 6. Data layout (fixed by this skill)

```
data/ib/<course>-<level>/<testId>/paper1.json     e.g. data/ib/aa-sl/ib-practice-1/paper1.json
```

```jsonc
{
  "meta": {
    "course": "aa", "level": "sl", "paper": 1,
    "testId": "ib-practice-1",
    "label": "AA SL Practice Paper 1",
    "timeMinutes": 90, "totalMarks": 80, "calculator": false
  },
  "questions": [
    {
      "source": "IB-AASL-P1-T1-Q3",
      "number": 3,
      "section": "A",                       // "A" | "B" (AI: omit — all one section)
      "maximumMark": 6,
      "topic": "calculus",                  // number_algebra | functions | geometry_trig | stats_probability | calculus
      "skill_tag": "differentiation_rules", // per-course tag list, kept in the test's builder script for now
      "contextIntro": "…optional shared stem shown above part (a)…",
      "figure": { "src": "/ib-figures/ib-aasl-p1-t1-q3.png", … },
      "parts": [
        {
          "label": "a",                     // "a" | "a.i" | "a.ii" | "b" …
          "body": "Find $f'(x)$.",
          "marks": 2,
          "markscheme": [
            { "mark": "M1", "note": "attempt to differentiate (any one term correct)" },
            { "mark": "A1", "note": "$f'(x) = 3x^2 - 4$" }
          ],
          "answer": "$f'(x) = 3x^2 - 4$",
          "solution": "…full worked reasoning for the student…",
          "verify": ["Eq(diff(x**3 - 4*x + 1, x), 3*x**2 - 4)"]
        }
      ]
    }
  ]
}
```

Figures live in `public/ib-figures/`. The gate
(`scripts/verify-practice-test.py --hub ib`) validates: meta/paper
shape and totals, part marks sum to `maximumMark`, question marks sum
to `totalMarks`, markscheme marks count = part marks, mark codes from
the legal set, `verify[]` true, `show that`/`hence` contract lint
(a part whose body contains "Show that" must end its markscheme with
`AG`; "hence" must not appear in question 1a), figures on disk.

## 7. Grade guidance (results page)

Report marks and percentage plus an indicative IB grade band. Default
boundaries (typical AA SL May session shape — label as indicative):
7 ≥ 71%, 6 ≥ 59%, 5 ≥ 47%, 4 ≥ 36%, 3 ≥ 25%, 2 ≥ 15%, 1 < 15%.

## 8. Ship checklist deltas

Core §11, plus:

```
[ ] Paper totals: marks sum to 80/110/55; time and calculator flags per §1 table
[ ] Every part: marks == markscheme mark count; codes legal; AG on every show-that
[ ] "Hence" links verified — later parts actually consume earlier results
[ ] AA P1 solvable fully without calculator (exact values throughout)
[ ] 3-sf discipline: no ambiguous roundings; exact answers marked exact
[ ] HL-only content absent from SL papers
[ ] Topic mark shares within blueprint (±8 pts per paper, pair on target)
[ ] Adversarial re-solve per paper (blind), 100% agreement on answers AND mark totals
```
