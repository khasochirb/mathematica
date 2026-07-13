"use client";

import { useRouter } from "next/navigation";
import { ArrowLeft } from "lucide-react";

// Browser-style back for report/utility pages that are reachable from many
// places (dashboard, hubs, results). Goes to the PREVIOUS page like the user
// expects; falls back to a sensible parent only when there is no history
// (deep link, new tab).
export default function BackButton({
  fallback,
  className = "gm-press grid h-9 w-9 place-items-center rounded-md",
  label = "Back",
}: {
  fallback: string;
  className?: string;
  label?: string;
}) {
  const router = useRouter();
  return (
    <button
      type="button"
      aria-label={label}
      onClick={() => {
        if (typeof window !== "undefined" && window.history.length > 1) router.back();
        else router.push(fallback);
      }}
      className={className}
      style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
    >
      <ArrowLeft className="h-4 w-4" />
    </button>
  );
}
