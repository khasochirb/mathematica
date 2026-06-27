"use client";

// An area model on the unit square: factor `a` runs across (columns of tenths),
// factor `b` runs up (rows of tenths). The overlap rectangle is the product in
// hundredths — 0.3 × 0.4 fills a 3×4 = 12-square corner = 0.12. The two factor
// bands are tinted so the rectangle reads as "a across × b up". Presentational.
export default function DecimalAreaView({
  aTenths,
  bTenths,
  color = "#e8913c",
  size = 200,
}: {
  aTenths: number;
  bTenths: number;
  color?: string;
  size?: number;
}) {
  const a = Math.max(0, Math.min(10, Math.round(aTenths)));
  const b = Math.max(0, Math.min(10, Math.round(bTenths)));
  const cell = size / 10;
  const BLUE = "#3b82f6";

  return (
    <div
      className="overflow-hidden rounded-md"
      style={{
        display: "grid",
        gridTemplateColumns: `repeat(10, ${cell}px)`,
        gridTemplateRows: `repeat(10, ${cell}px)`,
        border: "1.5px solid var(--fg-3)",
        width: size + 3,
      }}
      role="img"
      aria-label={`Area model: ${(a / 10).toFixed(1)} across by ${(b / 10).toFixed(1)} up, product ${(a * b / 100).toFixed(2)}`}
    >
      {Array.from({ length: 100 }).map((_, i) => {
        const r = Math.floor(i / 10); // 0..9 top → bottom
        const c = i % 10; // 0..9 left → right
        const rowFromBottom = 9 - r; // build the product up from the bottom
        const inA = c < a; // first `a` columns (across)
        const inB = rowFromBottom < b; // first `b` rows (up)
        let bg = "transparent";
        if (inA && inB) bg = color; // product rectangle
        else if (inA) bg = `${color}26`;
        else if (inB) bg = `${BLUE}26`;
        return (
          <div
            key={i}
            style={{
              width: cell,
              height: cell,
              background: bg,
              borderRight: "0.5px solid rgba(127,127,127,0.30)",
              borderBottom: "0.5px solid rgba(127,127,127,0.30)",
              transition: "background 140ms ease",
            }}
          />
        );
      })}
    </div>
  );
}
