"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import ContentGate from "@/components/genmath/ContentGate";
import type { PlacementQuestion } from "@/lib/placement-bank";

// Client half of a course placement page. The SERVER page harvests the bank
// (lib/placement-course-bank.ts — corpus access, server-only) and passes the
// ~40 questions here as props; this side builds the config, because
// functions like topicHref cannot cross the server→client boundary.
export default function CoursePlacement({
  bank,
  courseSlug,
  courseTitle,
}: {
  bank: PlacementQuestion[];
  courseSlug: string;
  courseTitle: string;
}) {
  return (
    <ContentGate backHref={`/math/${courseSlug}`} backLabel={`Back to ${courseTitle}`}>
      <PlacementRunner
        config={{
          bank,
          namespace: courseSlug,
          crumb: `${courseTitle} · Placement`,
          homeHref: `/math/${courseSlug}`,
          homeLabel: "units",
          subjectNoun: `${courseTitle} unit`,
          topicHref: (slug) => `/math/${courseSlug}/${slug}`,
          title: `Place into the ${courseTitle} course`,
        }}
      />
    </ContentGate>
  );
}
