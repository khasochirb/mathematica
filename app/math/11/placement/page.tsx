"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade11PlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade11PlacementPage() {
  return (
    <ContentGate backHref="/math/11" backLabel="Back to Grade 11">
      <PlacementRunner
        config={{
          bank: getGrade11PlacementBank(),
          namespace: "grade11",
          crumb: "General Math · Grade 11 · Placement",
          homeHref: "/math/11",
          homeLabel: "topics",
          subjectNoun: "Grade-11 topic",
          topicHref: (slug) => `/math/11/${slug}`,
          title: "Find your Grade 11 starting point",
        }}
      />
    </ContentGate>
  );
}
