"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade9PlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade9PlacementPage() {
  return (
    <ContentGate backHref="/math/9" backLabel="Back to Grade 9">
      <PlacementRunner
        config={{
          bank: getGrade9PlacementBank(),
          namespace: "grade9",
          crumb: "General Math · Grade 9 · Placement",
          homeHref: "/math/9",
          homeLabel: "topics",
          subjectNoun: "Grade-9 topic",
          topicHref: (slug) => `/math/9/${slug}`,
          title: "Find your Grade 9 starting point",
        }}
      />
    </ContentGate>
  );
}
