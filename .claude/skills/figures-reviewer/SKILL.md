---
name: figures-reviewer
description: >
  Review manual for every visual on Mongol Potential — interactive
  primitives, lesson diagrams, practice-test figures, and charts. Read
  before approving any figure for ship, when a figure-related bug is
  reported, or as the second half of any figures-creator task. Defines the
  measure-don't-eyeball verification method and the ship/block rubric.
---

# Figure & Graph Reviewer — Operating Manual

The creator drew it; you now try to break it. A figure review that only
*looks* at the figure is not a review — you MEASURE it against the
problem's numbers and you EXERCISE its states.

## The method: measure, don't eyeball

For each figure, extract the problem's given values, then verify the
rendering encodes them:

1. **Recompute coordinates.** Open the component/SVG source. For each
   labeled length/angle/area, check the coordinate math (or the
   `lib/geo.ts` call) reproduces the stated value. A 35° angle whose arc
   spans 40° of screen angle is a BLOCKER even if it "looks fine".
2. **Cross-check labels ↔ statement.** Every name in the statement
   (point A, side x, the 8 m side) appears once in the figure, spelled
   identically, attached to the right element. Orphan labels and
   mismatched names are MAJOR.
3. **Exercise all states.** For interactives: drag every handle to both
   extremes, hit every toggle. At each state, do the labels still tell
   the truth? Do elements collide/overflow the viewBox? Degenerate
   states must be either clamped out or pedagogically intentional.
4. **Theme + size sweep.** Render (or reason through the token usage)
   in dark AND light; verify contrast of strokes/labels on both
   backgrounds. Narrow to 320px: labels must not overlap or truncate.
5. **Meaning without color.** Cover the colors (imagine grayscale):
   can you still distinguish the series/regions? If meaning is
   color-only, MAJOR (color-blind students).
6. **Motion audit.** Anything that animates by itself must honor
   `prefers-reduced-motion` and must not loop distractingly next to
   problem text.

## Chart-specific checks (statistics content)

- Axis starts at 0 for bar/area charts; truncation only in the
  "misleading graphs" lessons where the trick is labeled.
- Tick intervals uniform; units on axes; sample data in the figure
  matches the data in the problem text EXACTLY (we compare digit by
  digit — a dot plot with 24 dots for a "25 students" problem is the
  classic miss).
- Dot plots / histograms: count the marks. Seriously — count them.
- Legends only when two+ series; otherwise label directly on the mark.

## Practice-test static figures

- Run `npm run verify:figures-wired` and `verify:figure-extraction` —
  both must pass; they catch orphans and missing wires mechanically.
- Figure language matches hub language (ЭЕШ figures Mongolian, SAT/IB
  English). Mixed-language figures are MAJOR.
- The figure must not leak the answer (a diagram drawn so precisely that
  measuring it with a ruler solves the problem is a MAJOR for
  reasoning questions — require "not to scale" annotation or a redraw).
- Raster figures: minimum 2x resolution for retina, under 200KB.

## Pipeline checks

- New interactive primitive: registered in `lib/genmath-interactive.ts`,
  rendered by the LessonPlayer switch, covered by
  `verify:genmath-interactive`. Unwired = BLOCKER (dead code shipping).
- Geometry math lives in `lib/geo.ts` with a vitest case, not inline in
  the component. Inline math = MAJOR (see `figures-creator`).
- For EN/MN mirrored topics: figure configs byte-identical between
  mirrors except translated label strings (see `mn-translation`).

## Verdict format

`SHIP` / `SHIP AFTER FIXES` / `BLOCK`, then findings ordered by severity
with file:line, the measured value vs the stated value, and the fix.
Close with the evidence: which states you exercised, which verify
scripts you ran and their output, which themes/sizes you checked.
"Looked correct" is not evidence; "arc endpoints compute to 35.0° at
both slider extremes; verify:genmath-interactive 214 cases green" is.
