"use client";

// The course-hub placement card, shared by every named course: before a
// result it invites the adaptive test; after, it shows the level + priority
// units and offers a retake. Same look as the original Geometry CTA.

import { useEffect, useState } from "react";
import Link from "next/link";
import { ArrowRight, Sparkles } from "lucide-react";
import { useAuth } from "@/lib/auth-context";
import { loadPlacement, type StoredPlacement } from "@/lib/placement-result";

export default function CoursePlacementCta({
  namespace,
  href,
  unitTitle,
}: {
  namespace: string; // placement namespace == course slug
  href: string; // the placement page
  unitTitle: (slug: string) => string | undefined; // priority slug -> title
}) {
  const { user } = useAuth();
  const [placement, setPlacement] = useState<StoredPlacement | null>(null);

  useEffect(() => {
    setPlacement(loadPlacement(user?.id, namespace));
  }, [user?.id, namespace]);

  const priorityTitles = (placement?.priorityTopics ?? [])
    .map(unitTitle)
    .filter(Boolean) as string[];

  return (
    <Link
      href={href}
      className="card-edit p-4 mb-8 flex items-center gap-4"
      style={{ textDecoration: "none", borderColor: "var(--accent-line)", background: "var(--accent-wash)" }}
    >
      <span
        className="grid h-9 w-9 flex-shrink-0 place-items-center rounded-full"
        style={{ background: "var(--accent)", color: "var(--accent-ink, #fff)" }}
      >
        <Sparkles className="h-4.5 w-4.5" />
      </span>
      {placement ? (
        <>
          <div className="flex-1 min-w-0">
            <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>
              You&apos;re at the <b style={{ color: "var(--accent)" }}>{placement.level}</b> level
            </p>
            <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
              {priorityTitles.length > 0 ? (
                <>
                  Focus first on <b>{priorityTitles.slice(0, 3).join(", ")}</b>.
                </>
              ) : (
                <>You&apos;re strong across the board. Retake anytime.</>
              )}
            </p>
          </div>
          <span className="mono text-[11px] flex-shrink-0" style={{ color: "var(--accent)" }}>
            Retake →
          </span>
        </>
      ) : (
        <>
          <div className="flex-1 min-w-0">
            <p className="serif" style={{ fontSize: 16, color: "var(--fg)" }}>
              Take the placement test
            </p>
            <p className="text-[13px] mt-0.5" style={{ color: "var(--fg-2)" }}>
              A quick adaptive test finds your level, seeds your rating, and shows
              where to start in this course.
            </p>
          </div>
          <ArrowRight className="h-4 w-4 flex-shrink-0" style={{ color: "var(--accent)" }} />
        </>
      )}
    </Link>
  );
}
