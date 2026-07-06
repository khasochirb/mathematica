"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade12PlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade12PlacementPage() {
  return (
    <ContentGate backHref="/math/12" backLabel="Back to Grade 12">
      <PlacementRunner
        config={{
          bank: getGrade12PlacementBank(),
          namespace: "grade12",
          crumb: "General Math · Grade 12 · Placement",
          homeHref: "/math/12",
          homeLabel: "topics",
          subjectNoun: "Grade-12 topic",
          topicHref: (slug) => `/math/12/${slug}`,
          title: "Find your Grade 12 starting point",
        }}
      />
    </ContentGate>
  );
}
