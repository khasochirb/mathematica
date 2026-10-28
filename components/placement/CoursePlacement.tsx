"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import ContentGate from "@/components/genmath/ContentGate";
import type { PlacementQuestion } from "@/lib/placement-bank";

// Client half of a course placement page. The SERVER page harvests the bank
// (lib/placement-course-bank.ts — corpus access, server-only) and passes the
// ~40 questions here as props; this side builds the config, because
// functions like topicHref cannot cross the server→client boundary.
//
// `bankMn` is the same sitting from the Mongolian bank mirror (null when the
// course has none); the runner shows it on mn pages and runs on `bank`.
export default function CoursePlacement({
  bank,
  bankMn,
  courseSlug,
  courseTitle,
  courseTitleMn,
}: {
  bank: PlacementQuestion[];
  bankMn?: PlacementQuestion[] | null;
  courseSlug: string;
  courseTitle: string;
  courseTitleMn?: string | null;
}) {
  const titleMn = courseTitleMn ?? courseTitle;
  return (
    <ContentGate backHref={`/math/${courseSlug}`} backLabel={`Back to ${courseTitle}`}>
      <PlacementRunner
        config={{
          bank,
          bankMn,
          namespace: courseSlug,
          crumb: `${courseTitle} · Placement`,
          crumbMn: `${titleMn} · Түвшин тогтоох шалгалт`,
          homeHref: `/math/${courseSlug}`,
          homeLabel: "units",
          homeLabelMn: "Бүлгүүд рүүгээ очих",
          subjectNoun: `${courseTitle} unit`,
          subjectNounMn: "бүлэг",
          topicHref: (slug) => `/math/${courseSlug}/${slug}`,
          title: `Place into the ${courseTitle} course`,
          titleMn: `${titleMn}: түвшин тогтоох шалгалт`,
        }}
      />
    </ContentGate>
  );
}
