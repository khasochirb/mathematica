"use client";

// A 10×10 grid that stands for ONE whole (100 hundredths). Cells fill
// column-by-column so completed tenths read as solid full columns and the
// leftover hundredths read as single cells in the next column — making the
// place-value split ("3 tenths + 7 hundredths") literal. Presentational only;
// shared by the interactive DecimalGrid and the static decimalGrid figure.
export default function DecimalGridView({
  hundredths,
  color = "#e8913c",
  size = 200,
}: {
  hundredths: number;
  color?: string;
  size?: number;
}) {
  const n = Math.max(0, Math.min(100, Math.round(hundredths)));
  const fullTenths = Math.floor(n / 10); // number of completely-filled columns
  const loose = n % 10; // leftover hundredths, filling down the next column
  const cell = size / 10;

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
      aria-label={`${n} of 100 squares shaded — ${(n / 100).toFixed(2)}`}
    >
      {Array.from({ length: 100 }).map((_, i) => {
        const r = Math.floor(i / 10); // 0..9 top → bottom
        const c = i % 10; // 0..9 left → right
        const isTenth = c < fullTenths; // part of a completed tenth column
        const isLoose = c === fullTenths && r < loose; // a leftover hundredth
        const fill = isTenth ? color : isLoose ? `${color}80` : "transparent";
        return (
          <div
            key={i}
            style={{
              width: cell,
              height: cell,
              background: fill,
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
