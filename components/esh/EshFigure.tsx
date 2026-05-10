"use client";

import Image from "next/image";
import { useLang } from "@/lib/lang-context";

export interface EshFigureProps {
  src: string;
  alt_mn: string;
  alt_en: string;
  width: number;
  height: number;
  // Optional className escape hatch for callers that need extra layout.
  className?: string;
}

/**
 * Renders a question figure (Section 1 or Section 2). Wrapped in a
 * styled container with light/dark-mode handling per the design:
 *   - Light: white bg, subtle gray border, rounded corners
 *   - Dark: invert(1) hue-rotate(180deg) filter on the image so
 *     black-on-white line art reads as white-on-dark
 *
 * Layout:
 *   - max-width 480px on desktop (matches the question card content
 *     width), full-width on mobile
 *   - Uses next/image with intrinsic dims for lazy-loading + responsive
 *     sizing. The `style.width="100%"` + `style.height="auto"` pair is
 *     the recommended Next.js shape for raster figures with intrinsic
 *     dims (avoids the aspect-ratio warning).
 *
 * See memory/figures.md for the file naming + variant-share story.
 */
export default function EshFigure({
  src,
  alt_mn,
  alt_en,
  width,
  height,
  className = "",
}: EshFigureProps) {
  const { lang } = useLang();
  const alt = lang === "mn" ? alt_mn : alt_en;
  return (
    <div className={`esh-figure-container ${className}`}>
      <Image
        src={src}
        alt={alt}
        width={width}
        height={height}
        className="esh-figure-image"
        style={{ width: "100%", height: "auto" }}
        // Figures are small (≤ 50KB each) and light-weight; eager loading
        // keeps the visual context together with the question. Test
        // runner pages render one question at a time so this isn't a
        // bandwidth concern.
        priority={false}
      />
    </div>
  );
}
