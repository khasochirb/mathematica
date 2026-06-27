"use client";

// A stacked add/subtract with the decimal points in a vertical line. Both
// numbers are padded to the same number of places; the padding zeros render
// faded so "fill missing places with zeros to line up" is visible. Monospace
// + ch widths keep every column (and the decimal point) aligned.
function origPlaces(x: number): number {
  const s = String(x);
  const i = s.indexOf(".");
  return i < 0 ? 0 : s.length - i - 1;
}

export default function DecimalColumnView({
  a,
  b,
  op,
  showAnswer,
  color = "#e8913c",
}: {
  a: number;
  b: number;
  op: "add" | "sub";
  showAnswer: boolean;
  color?: string;
}) {
  const places = Math.max(origPlaces(a), origPlaces(b));
  const scale = Math.pow(10, places);
  const ansNum = op === "add"
    ? (Math.round(a * scale) + Math.round(b * scale)) / scale
    : (Math.round(a * scale) - Math.round(b * scale)) / scale;
  const aStr = a.toFixed(places);
  const bStr = b.toFixed(places);
  const ansStr = ansNum.toFixed(places);
  const width = Math.max(aStr.length, bStr.length, ansStr.length);
  const opSym = op === "add" ? "+" : "−";

  // Split off the faded trailing zeros that were padded onto a/b.
  const split = (x: number, str: string): [string, string] => {
    const pad = places - origPlaces(x);
    if (pad <= 0) return [str, ""];
    return [str.slice(0, str.length - pad), str.slice(str.length - pad)];
  };
  const [aMain, aFade] = split(a, aStr);
  const [bMain, bFade] = split(b, bStr);

  const cell = { fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace", fontSize: 26, lineHeight: 1.5 } as const;

  const Row = ({ main, fade, lead, accent }: { main: string; fade?: string; lead?: string; accent?: boolean }) => (
    <div className="flex justify-end" style={cell}>
      <span style={{ width: "1.6ch", textAlign: "left", color: "var(--fg-3)" }}>{lead ?? ""}</span>
      <span style={{ width: `${width}ch`, textAlign: "right", color: accent ? color : "var(--fg)", fontWeight: accent ? 600 : 400 }}>
        {main}
        {fade ? <span style={{ color: "var(--fg-3)", opacity: 0.5 }}>{fade}</span> : null}
      </span>
    </div>
  );

  return (
    <div className="inline-block">
      <Row main={aMain} fade={aFade} />
      <Row main={bMain} fade={bFade} lead={opSym} />
      <div style={{ height: 2, background: "var(--fg-2)", width: `${width + 1.6}ch`, margin: "3px 0 4px auto" }} />
      {showAnswer ? (
        <div className="gm-fade">
          <Row main={ansStr} accent />
        </div>
      ) : (
        <div className="flex justify-end" style={cell}>
          <span style={{ width: "1.6ch" }} />
          <span style={{ width: `${width}ch`, textAlign: "right", color: "var(--fg-3)" }}>?</span>
        </div>
      )}
    </div>
  );
}
