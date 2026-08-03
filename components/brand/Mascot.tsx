// The mascot rig and the brand marks built from it. Pages never inline
// mascot SVG themselves (mascot-animator rule) — they render these.
//
// Color: everything draws in currentColor and defaults to the accent, so
// the mascot themes itself and "more colours" is a style={{ color }} away.
// The mascot is decorative everywhere it appears: aria-hidden, and any
// meaning it accompanies must also exist as text.

import { CSSProperties } from "react";
import {
  MARK_VIEWBOX,
  POSE_NAMES,
  VIEWBOX,
  markMarkup,
  mascotMarkup,
  type PoseName,
} from "@/components/brand/mascot-geometry.mjs";

export type { PoseName };
export { POSE_NAMES };

interface MascotProps {
  pose?: PoseName;
  /** Rendered height in px (the figure is taller than wide). */
  size?: number;
  className?: string;
  style?: CSSProperties;
}

export function Mascot({ pose = "idle", size = 96, className, style }: MascotProps) {
  return (
    <svg
      viewBox={VIEWBOX}
      height={size}
      width={(size * 120) / 150}
      aria-hidden="true"
      className={className}
      style={{ color: "var(--accent)", ...style }}
      dangerouslySetInnerHTML={{ __html: mascotMarkup(pose, "currentColor") }}
    />
  );
}

interface HeadMarkProps {
  /** Rendered size in px (the mark is square). */
  size?: number;
  className?: string;
  style?: CSSProperties;
  /** Spin the rays (loading states). Reduced motion disables it via CSS. */
  spinning?: boolean;
}

// The logo mark — the radiant head on its own. With `spinning`, the rays
// orbit the head (the owner's loading-page idea); the animation lives in
// globals.css on `.mp-mark-spin #rays` so prefers-reduced-motion can kill
// it in one place.
export function HeadMark({ size = 32, className, style, spinning = false }: HeadMarkProps) {
  return (
    <svg
      viewBox={MARK_VIEWBOX}
      height={size}
      width={size}
      aria-hidden="true"
      className={`${spinning ? "mp-mark-spin " : ""}${className ?? ""}`}
      style={{ color: "var(--accent)", ...style }}
      dangerouslySetInnerHTML={{ __html: markMarkup("currentColor") }}
    />
  );
}

// Loading indicator: the mark with its halo spinning. Meaning must also
// exist as text for screen readers — pass what the wrapped state says.
export function MascotSpinner({ size = 36, className, style }: HeadMarkProps) {
  return <HeadMark size={size} spinning className={className} style={style} />;
}
