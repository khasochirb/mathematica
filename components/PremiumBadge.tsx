"use client";

import { Lock, Sparkles } from "lucide-react";

type Variant = "inline" | "corner" | "pill";

interface Props {
  variant?: Variant;
  label?: string;
  icon?: "lock" | "sparkles";
  className?: string;
}

export default function PremiumBadge({
  variant = "pill",
  label = "Premium",
  icon = "lock",
  className = "",
}: Props) {
  const Icon = icon === "lock" ? Lock : Sparkles;

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
        background: "var(--accent-wash)",
        border: "1px solid var(--accent-line)",
        color: "var(--accent)",
        letterSpacing: "0.08em",
      }}
    >
      <Icon className="h-[10px] w-[10px]" />
      {label}
    </span>
  );
}
