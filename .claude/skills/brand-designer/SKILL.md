---
name: brand-designer
description: >
  Brand design manual for Mongol Potential — logo usage, mascot design
  brief, color system (the oklch CSS-variable palette), typography, and
  asset production rules. Read before creating or modifying any logo,
  mascot, icon, marketing image, or brand color; before adding images to
  public/; and as the base document for the mascot-animator skill.
---

# Brand Designer — Operating Manual

Mongol Potential's brand promise: serious math, warm delivery — a
Mongolian platform that feels world-class AND ours. Every asset should
read instantly as "friendly expert", never "corporate exam factory" and
never "babyish".

## Current brand inventory (ground truth)

- Logos: `public/images/logo.png`, `public/images/mp.png` (mark),
  used by `components/layout/Header.tsx`. Other photos in
  `public/images/` are page content, not brand assets.
- Color system: CSS variables in `app/globals.css`, oklch-based, dark
  theme default + light theme, consumed through `tailwind.config.ts`
  (`primary`, `accent`, `surface`, `navy`, `gray` scales). The accent is
  hue-parameterized (`--accent-h`) — the brand can retune its hue in ONE
  place.
- Typography: Inter (`--font-inter`) via next/font, system-ui fallback.
  Math is KaTeX and exempt from brand typography.
- Mascot: **does not exist yet.** Its design brief is below; treat this
  section as the source of truth when it gets created.

## Color rules

1. **Never hardcode.** All UI color goes through the CSS vars / Tailwind
   tokens. A hex literal in a component is a review MAJOR — it will
   break one of the two themes. (Raster/SVG brand ASSETS may embed
   color, but must be checked on both `--bg` values.)
2. **Both themes are first-class.** Dark (`--bg: oklch(0.16 …)` deep
   navy) is the default; light is `oklch(0.985 …)` warm paper. Every
   asset gets viewed on both before ship.
3. Accent (`--accent`) carries interaction and highlights; `--warn`
   (gold) is for caution/premium moments. Don't invent new semantic
   colors — extend `globals.css` deliberately if a real need appears.
4. Contrast: text meets WCAG AA (4.5:1) on its background in BOTH
   themes. oklch L-difference of ~0.5 between fg and bg is the working
   heuristic; verify questionable pairs with a checker.

## Logo usage

- Clear space: one "M"-height around the mark; never stretch, recolor
  outside theme tokens, or place on low-contrast photography.
- Header uses the horizontal lockup; favicons/app icons use the `mp.png`
  mark. Mobile app icons (see `mobile-app`) derive from the mark with
  proper padding per platform (iOS: no transparency; Android adaptive:
  keep the mark inside the 66% safe zone).
- If regenerating logo assets: export SVG master + PNG at 1x/2x/3x,
  optimize (svgo / squoosh), keep masters in `public/images/` with
  suffixed sizes.

## Mascot — design brief (build to this)

- **Concept direction:** a young, friendly animal with Mongolian
  identity. Strongest candidates: a **takhi (Przewalski's horse) foal**
  — uniquely Mongolian, energetic, "growth" symbolism — or a **snow
  leopard cub** — clever, calm under pressure. Pick ONE; do not ship a
  menagerie. (Eagles read too fierce for grade-6 comfort; avoid generic
  owls — every edu brand has one.)
- **Personality:** curious study-buddy, not teacher. It struggles and
  succeeds WITH the student: it scratches its head at hard problems and
  celebrates solved ones. It is never smug and never disappointed in
  the student.
- **Visual spec:** simple geometric construction (circles + rounded
  shapes) so it stays crisp at 24px and animates cheaply; 2–3 brand
  colors + neutrals, flat with minimal shading; bold readable silhouette
  (the silhouette test: recognizable filled solid black).
- **Required pose set (v1):** idle/neutral, thinking (head-scratch),
  celebrating (jump/confetti), encouraging (thumbs-up / нударга),
  sleeping (empty states), pointing (calls attention to a hint).
- **Format:** author as SVG with named layers/groups per limb so
  `mascot-animator` can animate parts (see that skill for rigging
  conventions). Master file + optimized per-pose exports under
  `public/images/mascot/`.
- **Naming:** the mascot gets a short Mongolian name decided by the
  owner (offer 3 options with meanings when proposing designs — e.g.,
  Тэмүүлэл "aspiration" shortened to Тэмүү; Од "star"; Хүслэн "wish").
  Never ship a placeholder name into UI copy.

## Asset production checklist

- [ ] Vector master (SVG) committed; rasters exported from it
- [ ] Optimized (SVG < 20KB per pose; PNG under 200KB, 2x for retina)
- [ ] Checked on dark AND light `--bg`
- [ ] Silhouette test passed (mascot) / clear-space respected (logo)
- [ ] Licensing clean: 100% original work or verified-license sources;
      no traced characters, no AI-generated lookalikes of existing IP
- [ ] Alt text written for every content image placement

## Voice (micro-copy that ships with design)

Encouraging, concrete, bilingual-aware: every user-facing string a
design introduces needs its Mongolian counterpart at design time, not
retrofitted (see `mn-translation` UI glossary for established section
names). Exclamation marks: maximum one per screen. The mascot's speech
bubbles follow lesson voice: «Бодоод үзье!», never "Oops, you failed!".
