"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade8PlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade8PlacementPage() {
  return (
    <ContentGate backHref="/math/8" backLabel="Back to Grade 8">
      <PlacementRunner
        config={{
          bank: getGrade8PlacementBank(),
          namespace: "grade8",
          crumb: "General Math · Grade 8 · Placement",
          homeHref: "/math/8",
          homeLabel: "topics",
          subjectNoun: "Grade-8 topic",
          topicHref: (slug) => `/math/8/${slug}`,
          title: "Find your Grade 8 starting point",
        }}
      />
    </ContentGate>
  );
}
