---
name: practice-test-authoring
description: >
  Core operating manual for generating practice tests (ЭЕШ, SAT, IB) with
  zero mistakes — questions, solutions, and figures. Read this FIRST, then
  the hub-specific skill (esh-practice-test, sat-practice-test,
  ib-practice-test). Use when authoring, editing, or verifying any practice
  test content for the Mongol Potential platform.
---

# Practice-Test Authoring — Core Operating Manual

This is the shared protocol for generating practice tests on Mongol
Potential. It exists so that **any model, in any session, can produce a
test where every answer, every solution step, and every figure is
provably correct** — not "probably correct."

Read this file completely, then read the hub skill for the test you are
building:

| Hub | Skill | Fidelity target |
|---|---|---|
| ЭЕШ (`/practice/esh`) | `.claude/skills/esh-practice-test/SKILL.md` | As rich as the 20 real past papers on the site, same difficulty curve |
| SAT (`/practice/sat`) | `.claude/skills/sat-practice-test/SKILL.md` | Indistinguishable in format/difficulty from the real Digital SAT Math section |
| IB (`/practice/ib`) | `.claude/skills/ib-practice-test/SKILL.md` | Indistinguishable in format/marking from real IB Mathematics papers |

---

## 1. Non-negotiable principles

1. **100% self-authored content.** (Locked decision, `memory/expansion-vision.md` §4.3.)
   Emulate the *format, topic distribution, and difficulty* of the real
   exam. NEVER transcribe, translate, or lightly paraphrase an actual
   released question from College Board, IBO, or any textbook. Write new
   problems. This is both a copyright requirement and a product decision.
2. **Content language is a property of the hub, not the user's toggle.**
   (Locked decision, `memory/expansion-vision.md` §4.7.)
   - ЭЕШ hub: ALL content in Mongolian (problems, options, solutions).
   - SAT / IB hubs: ALL content in English — realism is the point.
   - Navigation chrome is what the EN/MN toggle controls, never content.
3. **No unverified math ships.** Every answer and every numeric claim in
   every solution must be verified mechanically (sympy) before commit.
   "I checked it by hand" is not verification.
4. **Figures are generated from code, never drawn by eye.** The figure
   generator consumes the *same parameter variables* as the question
   text, so figure and statement cannot disagree.
5. **The gate must pass before commit:**
   `python3 scripts/verify-practice-test.py <files...>` (alias
   `npm run verify:ptest -- <files...>`). Then `npx tsc --noEmit`,
   `npx vitest run`, and a render QA pass (§8).

---

## 2. The generation pipeline (always in this order)

```
1. BLUEPRINT   Pick the exact per-test allocation (topics × difficulty ×
               figure count) from the hub skill's blueprint table. Write
               it down as a table before writing any question.
2. BUILDER     Author the test as a Python builder script in
               scripts/test-builders/<testkey>.py. Questions are built
               from named parameter variables; the correct answer is
               COMPUTED (sympy/fractions), never typed as a literal.
3. VERIFY[]    Every question carries a "verify" array of sympy assertion
               strings covering the answer and each intermediate value
               used in the solution. The builder asserts them itself
               before writing JSON (fail = crash, nothing written).
4. FIGURES     scripts/test-figures/<testkey>.py generates every figure
               (matplotlib) from the same variables. Commit the script.
5. GATE        python3 scripts/verify-practice-test.py <json files>
               — schema, delimiters, options, answer keys, blueprint,
               figures on disk, sympy re-check of verify[].
6. ADVERSARIAL Blind re-solve (see §7). A fresh pass solves every
   RE-SOLVE    question WITHOUT seeing the stored answer/solution and
               diffs its answers against the key. Any mismatch = stop.
7. RENDER QA   Walk every question in the browser (dev server +
               Playwright/screenshots): KaTeX renders (no red error
               text), figures load and match the statement, options
               align. Then wire, tsc, vitest, build, commit, push.
```

Do not reorder. In particular: figures come *after* verify[] passes
(so you never illustrate a broken problem), and the adversarial re-solve
comes *after* the gate (so it spends effort on math, not typos).

## 3. Builder-script conventions

- Location: `scripts/test-builders/<testkey>.py` (committed — the test
  must be reproducible and auditable).
- Every question is constructed by a helper that *requires* the verify
  block, mirroring the genmath house style:

```python
from sympy import (Rational, sqrt, pi, Eq, sympify, simplify, solve,
                   symbols, sin, cos, tan, log, factorial, binomial)

def assert_verified(qid, verify):
    for expr in verify:
        try:
            ok = sympify(expr)
        except Exception as e:
            raise SystemExit(f"{qid}: verify does not sympify: {expr!r} ({e})")
        if ok is not True:
            raise SystemExit(f"{qid}: verify not True: {expr!r} -> {ok}")

def mcq(qid, body, options, answer, solution, verify, **extra):
    assert answer in options, f"{qid}: answer letter {answer} not in options"
    vals = list(options.values())
    assert len(set(vals)) == len(vals), f"{qid}: duplicate option text"
    assert_verified(qid, verify)
    return {"id_": qid, "body": body, "options": options, "answer": answer,
            "solution": solution, "verify": verify, **extra}
```

- **Parameters are variables.** If the problem says "a cone of radius 6
  and height 8", then `r, h = 6, 8` appear once, and the body string,
  the verify block, the distractor computations, AND the figure script
  all interpolate `r` and `h`. Changing a parameter can never desync
  the artifacts.
- **Distractors are computed from named error models**, never invented:

```python
correct   = Rational(7, 15)
d_swap    = Rational(15, 7)        # inverted the ratio
d_forgot  = Rational(7, 30)        # forgot to double count
d_offby1  = Rational(8, 15)        # off-by-one in numerator
```

  Then assert all options are pairwise distinct *as mathematical values*
  (`len({simplify(o) for o in opts}) == 5`) — string-distinct is not
  enough; `\frac{2}{4}` and `\frac{1}{2}` are a duplicate.
- The builder ends by dumping JSON with
  `json.dump(data, f, ensure_ascii=False, indent=2)`.

## 4. The `verify[]` micro-language

Same semantics as `scripts/verify-genmath.py`: each entry is a string
that must `sympify(...)` to `True`.

- Use `Eq(lhs, rhs)` for equalities, plain relational strings for
  inequalities: `"Eq(3*Rational(1,2), Rational(3,2))"`, `"7*2 > 13"`.
- Use exact objects: `Rational(1,3)` not `0.3333`, `sqrt(2)` not
  `1.414`, `pi` not `3.14`. If the shipped answer is a rounded decimal,
  assert the rounding: `"Abs(sqrt(2) - 1.41) < 0.005"`.
- Cover: (a) the final answer, (b) every intermediate value quoted in
  the solution text, (c) key distractor-vs-answer distinctness when the
  distractor is "close" (e.g. `"Rational(7,15) != Rational(7,30)"`).
- Degrees: sympy trig is radian — write `sin(pi/6)` for sin 30°.
- No floats where exactness matters; no `random`; no statefulness.

## 5. Distractor doctrine (MCQ)

1. Exactly one option is correct — assert it, don't assume it.
2. Every wrong option encodes ONE specific, plausible student error
   (sign slip, squared instead of doubled, used diameter as radius,
   forgot the restriction, computed P(A∩B) instead of P(A|B), …).
   Name the error in a builder comment.
3. Options are pairwise distinct after `simplify`.
4. Formatting parity: all options in the same form (all fractions
   reduced, same units, same precision). A student must not be able to
   pick the answer by format alone (e.g. the only simplified one).
5. No "all/none of the above", no "cannot be determined" (unless the
   real exam uses it — it doesn't, in any of our three hubs).
6. Numeric options sorted per hub convention (see hub skills — SAT
   sorts ascending; ЭЕШ past papers do not sort consistently).
7. The answer key across a full test must be roughly balanced across
   letters, with no run of 4+ identical letters. The gate warns on
   imbalance.

## 6. Solution-writing standard

A solution must let a student who got the question wrong reconstruct
the full path:

1. State the plan in one clause, then execute step by step. One
   equation-level step per `$$...$$` or sentence — no "after some
   algebra".
2. Every number that appears must be derivable from the previous line
   and covered by `verify[]`.
3. End by restating the result and the key:
   - ЭЕШ: `Хариу: **D**.` (solution starts `**Бодолт.**`)
   - SAT: `The correct answer is **C**.` (or the SPR value)
   - IB: final line matches the markscheme's final A-mark.
4. Mention the trap when a distractor is popular ("Хэрэв ... гэж
   андуурвал B гарна" / "Choosing the diameter instead of the radius
   gives choice B").
5. Solutions are in the hub's content language, full sentences, exam
   register — match the richness of the existing 2021–2025 ЭЕШ
   solutions (multi-step, displayed equations), not one-liners.

## 7. Adversarial re-solve protocol

After the gate passes, run a blind re-solve:

1. Produce a stripped file (body + options only — no answer, no
   solution, no verify) — the gate script can emit it:
   `python3 scripts/verify-practice-test.py --strip <file> > /tmp/blind.json`.
2. In a FRESH context (subagent with no access to the answer key),
   solve every question and output an answer vector.
3. Diff against the key. Every mismatch is investigated to ground
   truth with sympy — either the key is wrong (fix the builder and
   regenerate) or the re-solver erred (record why; if the error is one
   a strong student would also make, consider whether the question is
   ambiguous and reword).
4. Target: 100% agreement before ship. Never ship with an open
   mismatch.

## 8. Figure standard (applies to every hub)

The site renders figures with `components/esh/EshFigure.tsx`:
**dark mode applies `invert(1) hue-rotate(180deg)` to the image.**
Figures must therefore be pure black-on-white line art.

Rules:

1. **Generated by matplotlib from the question's parameter variables**,
   in `scripts/test-figures/<testkey>.py`, committed. Never hand-drawn,
   never AI-image-generated, never screenshot.
2. Monochrome: black strokes/text on white (`#000` on `#fff`). No color,
   no gray fills darker than `0.85`, no alpha. Hatching is fine.
3. Geometry is EXACT: plot the actual coordinates. If the problem says
   the triangle has sides 5, 6, 7 — compute the vertex coordinates from
   those lengths and plot them. Never sketch "roughly". If a figure is
   deliberately not to scale, the statement must say so (IB: "diagram
   not to scale"), and even then keep topology/ordering exact.
4. Function graphs: sample the true function (`numpy.linspace`, ≥400
   points), correct intercepts/asymptotes/extrema by construction. Draw
   axes with arrowheads, label them ($x$/$y$), tick the values the
   problem references, use `ax.set_aspect("equal")` when slopes/angles
   matter.
5. Labels: `usetex=False` mathtext is fine; font size ≥ 12 at final
   size; label every point/length the statement references, and nothing
   the student is supposed to find (don't print the answer on the
   figure — the #1 figure bug).
6. Output PNG at 2x (e.g. `dpi=200`), tight bbox, white facecolor:
   `plt.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")`.
   Target ≤ 50 KB per figure; record intrinsic `width`/`height` px in
   the JSON `figure` object (read them back with PIL, don't guess).
7. Naming + location per hub skill (ЭЕШ: `public/section1-figures/`,
   `public/section2-figures/`). `alt_mn`/`alt_en` describe the figure
   ("Radius 6 cone with slant height labeled l"), not the answer.
8. **Figure–statement consistency check**: after generating, re-read
   the statement and the figure script side by side and confirm every
   number/label matches. Because both interpolate the same variables,
   a mismatch means a hardcoded literal sneaked in — remove it.

## 9. Math rendering contract (MathText)

Question `body`, `options`, `solution`, Section-2 `context`/
`instruction` are rendered by `components/esh/MathText.tsx`:

- Supported: inline `$...$`, display `$$...$$`, bold `**...**`, literal
  dollar `\$` (write `\\$` inside JSON strings). Nothing else — no
  italics, no lists, no headers, no links, no HTML.
- The splitter regex forbids a `$` INSIDE math. Never nest, never leave
  an empty `$$`, always close delimiters. The gate checks parity.
- KaTeX renders with `throwOnError: false` — a bad macro shows as red
  code in production. Stick to the safe subset: `\frac \dfrac \sqrt[n]{}
  \left( \right) \cdot \times \div \pm \le \ge \ne \approx \infty \pi
  \alpha... \sin \cos \tan \log \ln \lim \to \int \sum \binom \vec
  \overline \angle \triangle \parallel \perp \circ \begin{pmatrix}
  \begin{vmatrix} \begin{cases}` (KaTeX supports these). Avoid
  `\begin{align}`, `\tag`, `\label`, custom macros.
- Newlines in `solution` do not create paragraphs; structure long
  solutions with display math `$$...$$` between sentences.
- JSON escaping: LaTeX backslashes double in JSON source
  (`"$\\sqrt{2}$"`). The builder writes strings through `json.dump`, so
  in Python author `r"$\sqrt{2}$"` raw strings.

## 10. Difficulty calibration

Each hub skill defines its scale and placement rules. Shared doctrine:

- Difficulty = number of distinct ideas chained + obscurity of the
  entry point, NOT bigger numbers or messier arithmetic.
  - Easy: one concept, one step, standard form.
  - Medium: two concepts chained, or one concept in an unfamiliar dress.
  - Hard: three+ chained ideas, a non-obvious setup, or a required
    insight (clever substitution, case split, construction).
- Arithmetic stays humane at every tier: exact answers, small radicals,
  fractions with small denominators. Hard ≠ ugly numbers.
- Calibrate against the real anchors: before authoring, read 5–10
  questions of the same topic × tier in the existing bank
  (`data/questions/`) and match their footprint (steps, notation
  density, solution length).

## 11. Ship checklist (copy into your worklog and tick every box)

```
[ ] Blueprint table written and matches hub skill (topics × difficulty × figures)
[ ] Builder script committed; answers COMPUTED, not typed
[ ] Every question has verify[]; builder ran clean
[ ] All options pairwise distinct under simplify; exactly one correct
[ ] Answer-letter histogram balanced; no 4-run
[ ] Figures generated from shared variables; monochrome; ≤50KB; dims read via PIL
[ ] alt_mn/alt_en written; figure files exist at referenced paths
[ ] Gate passes: python3 scripts/verify-practice-test.py <files>
[ ] Adversarial blind re-solve: 100% agreement
[ ] Render QA: every question walked in browser, KaTeX clean, figures load
[ ] Wiring done per hub skill; npx tsc --noEmit; npx vitest run; npm run build
[ ] Commit + push (never deploy to main without explicit user request)
```

## 12. Known failure modes (learned the hard way — don't repeat)

- **Transcription corruption** (`memory/practice-test-audit.md`): the 14
  legacy tests were hand-transcribed and corrupted (wrong option text,
  shuffled letters). This is exactly what the builder-script pipeline
  prevents. Never hand-edit a question JSON directly; regenerate from
  the builder.
- **Figure printed the answer** or used values from an earlier draft of
  the problem. Prevented by shared parameter variables (§8.8).
- **Distractor equal to the answer** after simplification (e.g. author
  wrote `\frac{2}{4}` as a distractor for `\frac{1}{2}`). Prevented by
  the simplify-distinctness assert.
- **KaTeX red-error in production** from an unsupported macro — caught
  only by render QA, so never skip it.
- **Impossible problems** (e.g. "three consecutive integers sum to 91").
  The verify[] block catches these because the assertion cannot be made
  true. If you find yourself unable to write the verify entry, the
  problem is broken — fix the problem, never soften the check.
- **Positional difficulty drift**: question 3 that needs three chained
  ideas. Blueprint first, then author into slots.
