"use client";

import { AlertTriangle } from "lucide-react";
import MathText from "@/components/esh/MathText";
import { type Lesson } from "@/lib/esh-lessons";

export default function LessonCommonMistakes({ lesson }: { lesson: Lesson }) {
  const isDev = process.env.NODE_ENV !== "production";
  const items = lesson.commonMistakes.filter((m) => m.authored || isDev);
  if (items.length === 0) return null;

  return (
    <ul className="card-edit p-2" style={{ background: "var(--warn-wash, var(--bg-2))" }}>
      {items.map((m, i) => (
        <li
          key={i}
          className="flex items-start gap-3 px-4 py-3"
          style={{ borderBottom: i < items.length - 1 ? "1px solid var(--line)" : "none" }}
        >
          <AlertTriangle className="w-4 h-4 mt-0.5 flex-shrink-0" style={{ color: "var(--warn, var(--danger))" }} />
          <div>
            <p className="text-[14px] leading-relaxed" style={{ color: "var(--fg-1)" }}>
              <MathText text={m.text} />
              {!m.authored && (
                <span className="mono text-[10px] ml-2" style={{ color: "var(--danger)" }}>TODO(Khas)</span>
              )}
            </p>
            {m.correction && (
              <p className="text-[13px] mt-1" style={{ color: "var(--accent)" }}>
                → <MathText text={m.correction} />
              </p>
            )}
          </div>
        </li>
      ))}
    </ul>
  );
}
