"use client";

import { Clock } from "lucide-react";

type Variant = "inline" | "corner" | "pill";

interface Props {
  variant?: Variant;
  label?: string;
  className?: string;
}

export default function ComingSoonBadge({
  variant = "pill",
  label = "Удахгүй",
  className = "",
}: Props) {
  const base =
    "inline-flex items-center gap-1 mono uppercase rounded-full font-semibold";
  const size =
    variant === "inline"
      ? "text-[9px] px-1.5 py-[2px]"
      : variant === "corner"
        ? "text-[9px] px-1.5 py-[3px]"
        : "text-[10px] px-2 py-[3px]";

  return (
    <span
      className={`${base} ${size} ${className}`}
      style={{
        background: "var(--bg-2)",
        border: "1px solid var(--line-strong)",
        color: "var(--fg-2)",
        letterSpacing: "0.08em",
      }}
    >
      <Clock className="h-[10px] w-[10px]" />
      {label}
    </span>
  );
}
