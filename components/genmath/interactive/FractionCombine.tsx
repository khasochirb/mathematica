"use client";

import { useState } from "react";
import { type FractionCombineConfig, gcd } from "@/lib/genmath-interactive";
import FractionBar from "@/components/genmath/interactive/FractionBar";

const A_COLOR = "#e8913c";
const B_COLOR = "#3f78d7";

export default function FractionCombine({ config }: { config: FractionCombineConfig }) {
  const { left, right, op, color } = config;
  const [matched, setMatched] = useState(false);
  const aColor = color ?? A_COLOR;

  const lcd = (left.den / gcd(left.den, right.den)) * right.den;
  const sL = lcd / left.den;
  const sR = lcd / right.den;
  const numL = matched ? left.num * sL : left.num;
  const denL = matched ? lcd : left.den;
  const numR = matched ? right.num * sR : right.num;
  const denR = matched ? lcd : right.den;

  const resultNum = op === "add" ? left.num * sL + right.num * sR : left.num * sL - right.num * sR;
  const opSym = op === "add" ? "+" : "−";

  // simplest form of the result
  const g = gcd(Math.abs(resultNum) || 1, lcd);
  const simpNum = resultNum / g;
  const simpDen = lcd / g;
  const simplified = simpDen !== lcd && resultNum !== 0;

  return (
    <div className="rounded-2xl p-4 sm:p-5" style={{ background: "var(--bg-1)", border: "1px solid var(--line)" }}>
      <div className="space-y-2.5">
        <div>
          <div className="mb-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
            <span className="serif tabular" style={{ fontSize: 15, color: "var(--fg)" }}>{numL}/{denL}</span>
          </div>
          <FractionBar num={numL} den={denL} color={aColor} height={34} />
        </div>
        <div className="text-center text-[18px]" style={{ color: "var(--fg-3)" }}>{opSym}</div>
        <div>
          <div className="mb-1 text-[12px]" style={{ color: "var(--fg-2)" }}>
            <span className="serif tabular" style={{ fontSize: 15, color: "var(--fg)" }}>{numR}/{denR}</span>
          </div>
          <FractionBar num={numR} den={denR} color={B_COLOR} height={34} />
        </div>
      </div>

      {matched && (
        <div className="gm-fade mt-3 border-t pt-3" style={{ borderColor: "var(--line)" }}>
          <div className="mb-1 text-[12px]" style={{ color: "var(--accent)" }}>
            = <span className="serif tabular" style={{ fontSize: 16 }}>{resultNum}/{lcd}</span>
            {simplified && <> = <span className="serif tabular" style={{ fontSize: 16 }}>{simpNum}/{simpDen}</span></>}
          </div>
          <FractionBar num={Math.max(resultNum, 0)} den={lcd} color="#2f9e6e" height={34} />
        </div>
      )}

      <div
        role="status"
        aria-live="polite"
        className="gm-fade mt-3 rounded-xl px-4 py-3 text-center text-[13px]"
        style={{
          background: matched ? "var(--accent-wash)" : "var(--bg-2)",
          border: matched ? "1px solid var(--accent-line)" : "1px solid var(--line)",
          color: "var(--fg-1)",
          transition: "background .3s, border-color .3s",
        }}
      >
        {matched ? (
          <span>
            Pieces match ({lcd}ths). {op === "add" ? "Add" : "Subtract"} the shaded pieces: {left.num * sL} {opSym} {right.num * sR} = <b>{resultNum}</b> →{" "}
            <b style={{ color: "var(--accent)" }}>{simplified ? `${simpNum}/${simpDen}` : `${resultNum}/${lcd}`}</b>.
          </span>
        ) : (
          <span>You can only {op === "add" ? "add" : "subtract"} pieces of the <b>same size</b>. Match the pieces first.</span>
        )}
      </div>

      <div className="mt-3 flex justify-center">
        <button
          type="button"
          onClick={() => setMatched((v) => !v)}
          aria-pressed={matched}
          className="gm-press inline-flex items-center gap-2 rounded-full px-6 py-3 text-[14px] font-medium"
          style={{
            background: matched ? "var(--bg-2)" : "var(--accent)",
            color: matched ? "var(--fg-2)" : "var(--accent-ink, #fff)",
            border: matched ? "1px solid var(--line)" : "1px solid var(--accent)",
            transition: "background .2s, color .2s",
          }}
        >
          {matched ? "Reset" : "Make the pieces match"}
        </button>
      </div>
    </div>
  );
}
