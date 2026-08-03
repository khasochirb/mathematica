// The MONGOL POTENTIAL wordmark, per the owner's sketch: the radiant head
// takes the O of MONGOL, and the whole figure stands in as the I of
// POTENTIAL. Set in the display face (Space Grotesk) so the lockup reads
// as a drawn mark, not body text.
//
// `stacked` gives the two-line poster lockup from the sketch (MONGOL over
// POTENTIAL, offset); default is a single line for headers and footers.

import { CSSProperties } from "react";
import { HeadMark, Mascot } from "@/components/brand/Mascot";

interface WordmarkProps {
  /** Cap height of the text in px; the glyph-marks scale from it. */
  size?: number;
  stacked?: boolean;
  className?: string;
  style?: CSSProperties;
}

export function Wordmark({ size = 20, stacked = false, className, style }: WordmarkProps) {
  const text: CSSProperties = {
    fontFamily: "var(--font-space-grotesk), var(--font-inter), sans-serif",
    fontWeight: 600,
    fontSize: size,
    letterSpacing: "0.06em",
    lineHeight: 1.15,
    color: "var(--fg)",
    whiteSpace: "nowrap",
  };
  // The head sits in for the O: slightly larger than the cap height so the
  // halo overshoots the line the way it does in the sketch.
  const oSize = size * 1.35;
  const mongol = (
    <span className="inline-flex items-center" style={text}>
      M
      <HeadMark size={oSize} style={{ margin: `0 ${size * -0.08}px` }} />
      NGOL
    </span>
  );
  const potential = (
    <span className="inline-flex items-center" style={text}>
      POTENT
      <Mascot pose="idle" size={size * 1.5} style={{ margin: `0 ${size * 0.02}px` }} />
      AL
    </span>
  );

  if (stacked) {
    return (
      <span className={className} style={{ display: "inline-flex", flexDirection: "column", alignItems: "flex-start", gap: size * 0.25, ...style }}>
        {mongol}
        {potential}
      </span>
    );
  }
  return (
    <span className={className} style={{ display: "inline-flex", alignItems: "center", gap: size * 0.45, ...style }}>
      {mongol}
      {potential}
    </span>
  );
}
