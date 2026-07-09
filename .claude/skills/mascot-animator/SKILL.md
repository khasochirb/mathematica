---
name: mascot-animator
description: >
  Motion design manual for Mongol Potential — how to animate the mascot and
  UI across the website (and later the mobile app): technique choice
  (CSS/SVG/Lottie), rigging conventions, performance budgets, accessibility
  (prefers-reduced-motion), and where mascot moments belong in the learning
  flow. Read before adding ANY animation to the site, and together with
  brand-designer for the mascot itself.
---

# Mascot Animator — Operating Manual

Animation here has one job: make effort feel rewarded. A student who
just solved a hard problem gets a moment of delight; a student who is
struggling gets calm encouragement — never noise. The site is used on
cheap Android phones over slow connections: every animation must earn
its bytes and its milliseconds.

## Where the mascot appears (the sanctioned moments)

| Moment | Pose (see brand-designer) | Trigger | Duration |
|---|---|---|---|
| Correct answer / quick-check pass | celebrating | answer submit | ≤ 1.2s, once |
| Lesson complete / recap reached | celebrating + confetti | step advance | ≤ 2s, once |
| Wrong answer | encouraging (NOT sad) | answer submit | ≤ 0.8s |
| Long think (no input 30s+ on a problem) | thinking | idle timer | subtle loop, dismiss on input |
| Empty states (no results, offline) | sleeping | render | static or 2-frame breathe |
| Placement test start / finish | pointing / celebrating | route | ≤ 1.5s |
| Loading over 400ms | idle bounce | suspense | loop until loaded |

Anti-placements (never): during problem reading, next to KaTeX being
studied, over figure diagrams, during test-mode timed sections (ЭЕШ/SAT
mock exams get ZERO mascot — exam mode is sacred), or any autoplaying
loop beside body text.

## Technique decision tree

1. **UI micro-interactions** (buttons, cards, progress dots): CSS
   transitions/keyframes on `transform` and `opacity` ONLY. Never
   animate layout properties (width/height/top) — compositor or bust.
2. **Mascot poses swaps + simple gestures** (wave, bounce, head tilt):
   inline SVG + CSS keyframes on named groups. This is the default: no
   new dependencies, themes automatically, ~0 bytes over the asset.
3. **Rich mascot scenes** (celebration with confetti, multi-limb
   sequences): SMIL is out (Safari quirks); if CSS keyframes get
   unmanageable, propose Lottie (`lottie-react` + .lottie files) as a
   deliberate dependency decision — requires owner sign-off per the
   `cybersecurity` dependency policy, lazy-loaded ONLY on routes that
   use it.
4. **Never:** GIFs (huge, unthemeable), video for UI, JS rAF loops for
   things CSS can do.

## Rigging conventions (SVG)

- The mascot master SVG (see `brand-designer`) uses named groups:
  `#head`, `#ear-l/#ear-r`, `#arm-l/#arm-r`, `#tail`, `#eyes`, `#mouth`,
  `#body`. Animations target groups by id/class — never restructure the
  tree per pose, or every animation breaks.
- Every group sets its own `transform-origin` (e.g., arm rotates from
  shoulder, not viewBox origin — the #1 SVG animation bug).
- Poses are CSS class states on the same rig where feasible
  (`.mascot--thinking`), full separate exports only when geometry truly
  differs.
- Component: one `<Mascot pose="..." animate />` client component in
  `components/` wraps the rig; pages never inline mascot SVG themselves.

## Performance budget (hard limits)

- Animated mascot on screen: ≤ 1 at a time, site-wide.
- Asset weight: ≤ 20KB per SVG pose, ≤ 50KB per Lottie scene.
- No animation may run while a KaTeX-heavy problem list is rendering
  (jank window) — delay celebratory moments ~150ms after layout settles.
- Loops idle at ≤ 12 updates/sec equivalent (gentle breathe, not a
  sprite storm); everything pauses when tab is hidden (CSS animations
  do this free; Lottie needs `visibilitychange` wiring).
- Test on CPU 4x throttle in devtools before shipping any new scene.

## Accessibility (non-negotiable)

- Global rule already expected by reviewers:
  ```css
  @media (prefers-reduced-motion: reduce) {
    .mascot-anim, .celebrate { animation: none; transition: none; }
  }
  ```
  Reduced motion shows the END state (static celebrating pose) — users
  still get the reward, minus the motion.
- No flashing > 3 times/sec, ever (photosensitivity).
- Mascot is decorative: `aria-hidden="true"` on the SVG, and any
  meaning it conveys ("correct!") must ALSO exist as text/state for
  screen readers.
- Confetti and celebration must not obscure the Next button or the
  solution text — students replaying a solution outrank the party.

## Definition of done for any animation PR

- [ ] Compositor-only properties (transform/opacity) or justified
- [ ] Reduced-motion fallback verified (toggle it in devtools)
- [ ] Both themes checked; no hardcoded colors in the rig
- [ ] One-mascot rule and anti-placement list respected
- [ ] Exam/test routes untouched by celebratory motion
- [ ] Weight within budget; CPU-throttled smoke test done
- [ ] `figures-reviewer` pass if the animation sits near any figure
