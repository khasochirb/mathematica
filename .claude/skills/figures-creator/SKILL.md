---
name: figures-creator
description: >
  Manual for creating every visual on Mongol Potential — lesson diagrams,
  interactive SVG primitives, practice-test figures, graphs, and data
  visualizations. Read BEFORE building any figure, chart, geometric diagram,
  or interactive widget. Covers the primitive library, SVG conventions,
  theme-safe color, math-accuracy rules, and the static-figure pipeline for
  practice tests.
---

# Figure & Graph Creator — Operating Manual

A figure that contradicts its problem statement teaches wrong math faster
than wrong prose does — students trust pictures. Every figure here is
either **generated from the same numbers as the problem** or **checked
against them by the figures reviewer**. Never draw "roughly right".

## Choose the right medium (decision tree)

1. **Lesson interactive** (student manipulates it) → React SVG primitive
   in `components/genmath/interactive/`. ~100 exist — REUSE FIRST:
   grep the directory before writing a new one. Circles → `CircleFigure`,
   `ArcSector`, `CircleUnroll`; triangles → `TriangleCenters`,
   `SpecialTriangle`, `CongruentTriangles`; grids/graphs →
   `CoordinateGrid`, `AreaGraph`, `ExpGraph`, `ConicGraph`; fractions/
   decimals → the `Fraction*`/`Decimal*` families; general geometry →
   `GeoDiagram`/`GeoCanvas`.
2. **Static lesson diagram** (no interaction) → still an SVG component or
   a `figure` config consumed by an existing primitive — never a raster.
3. **Practice-test figure** (ЭЕШ/SAT/IB) → static SVG/PNG under
   `public/section1-figures/` or `public/section2-figures/`, wired by the
   question's figure field and validated by `verify:figures-wired` /
   `verify:figure-extraction`. Follow `practice-test-authoring` for
   naming.
4. **Data chart** (statistics lessons, dashboards) → follow the `dataviz`
   skill for form/color rules, rendered as an inline SVG primitive so it
   themes correctly.

## Build rules for interactive primitives

- **Math out, pixels in.** All geometry/computation lives in `lib/geo.ts`
  (pure, vitest-tested). The component receives computed points and only
  renders. If your component contains `Math.atan2`, move it.
- **SVG skeleton:** `viewBox` with generous padding, no hardcoded width;
  parent controls size. Must be legible at 320px (phone) — test by
  narrowing the window, not by squinting.
- **Coordinates:** define a world→screen transform once at the top;
  never sprinkle magic pixel offsets. Y flips (screen y grows downward) —
  centralize the flip or every angle will mirror.
- **Labels:** every named point/side/angle in the problem statement
  appears in the figure with the SAME name. Label placement must not
  collide at any slider position — compute label anchors from geometry.
- **Color:** theme tokens only (`var(--accent)`, `var(--fg-2)`,
  `var(--warn)`, Tailwind `primary`/`surface` scales). Both themes are
  first-class; verify in dark AND light. Never encode meaning by color
  alone — pair with pattern, label, or shape (color-blind students).
- **Interaction:** draggables get ≥44px hit targets (use an invisible
  fat `<circle>` over the visible dot), keyboard operability where
  feasible, and clamped ranges so students can't drag into degenerate
  states unless the degenerate state IS the lesson (triangle inequality's
  collapse is a feature — clamp everything else).
- **Motion:** any autonomous animation respects
  `prefers-reduced-motion` (see `mascot-animator` for the shared
  pattern).
- **Wire-up:** new primitive = component + kind registered in
  `lib/genmath-interactive.ts` types + LessonPlayer switch + a
  `verify:genmath-interactive` case. Unwired components are dead code.

## Accuracy rules (the ones that bite)

- **Draw to the numbers.** If the problem says radius 3 in a 10×8 lawn,
  the SVG ratio is 3:10 — compute coordinates from the given values.
  "Not to scale" is allowed ONLY when the problem tests reasoning that a
  true-scale figure would give away, and then the figure must say so.
- **Angles:** an angle labeled 35° must measure 35° in the rendering.
  Compute with `lib/geo.ts` helpers; never eyeball arc endpoints.
- **Graphs:** axis ticks at honest intervals, origin marked, no truncated
  y-axis in lesson charts (statistics lessons about misleading graphs are
  the sanctioned exception — and they must label the trick).
- **π-exact vs decimal:** figure annotations match the problem's
  convention ($9\pi$ vs $\approx 28.3$) — don't mix within one figure.
- **Randomized/interactive states:** every reachable state must remain
  true (labels recompute, arcs re-measure). Test the extremes of every
  slider.

## Static practice-test figures

- Source of truth is the question JSON; the figure is derived. Keep the
  generation script (Python/matplotlib or hand-SVG) in `scripts/` or the
  scratchpad commit message so figures are regenerable.
- File naming per hub convention (`<test-id>-q<n>.svg/png`), referenced
  from the question, and `npm run verify:figures-wired` must pass —
  it catches orphan figures and figure-less questions that declare one.
- Mongolian tests get Mongolian figure labels; SAT/IB figures are
  English. Text inside static figures counts as content for the
  translation parity rules (`mn-translation`).

## Definition of done

- [ ] Reused an existing primitive, or justified the new one in a line
- [ ] Math in `lib/geo.ts` with a vitest case; component render-only
- [ ] Labels match statement names; all values drawn to the numbers
- [ ] Light + dark verified; 320px verified; reduced-motion respected
- [ ] Wired: types + player + verify script (or figures-wired for static)
- [ ] Handed to `figures-reviewer` (or self-reviewed against that skill)
