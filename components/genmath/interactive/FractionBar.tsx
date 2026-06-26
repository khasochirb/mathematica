"use client";

// A bar representing one whole, split into `den` equal pieces with `num` shaded.
// The shaded WIDTH is num/den of the bar — so 1/2, 2/4, 3/6 all shade the same
// width, just with more dividing lines. That is what makes equivalence visible.
export default function FractionBar({
  num,
  den,
  color = "#e8913c",
  height = 46,
}: {
  num: number;
  den: number;
  color?: string;
  height?: number;
}) {
  return (
    <div
      className="flex w-full overflow-hidden rounded-lg"
      style={{ height, border: "1px solid var(--line)", background: "var(--bg-2)" }}
    >
      {Array.from({ length: den }).map((_, i) => (
        <div
          key={i}
          style={{
            flex: 1,
            background: i < num ? color : "transparent",
            borderRight: i < den - 1 ? "1px solid var(--bg)" : "none",
            transition: "background .3s ease",
          }}
        />
      ))}
    </div>
  );
}
