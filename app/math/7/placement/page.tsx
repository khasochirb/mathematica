"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade7PlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade7PlacementPage() {
  return (
    <ContentGate backHref="/math/7" backLabel="Back to Grade 7">
      <PlacementRunner
        config={{
          bank: getGrade7PlacementBank(),
          namespace: "grade7",
          crumb: "General Math · Grade 7 · Placement",
          homeHref: "/math/7",
          homeLabel: "topics",
          subjectNoun: "Grade-7 topic",
          topicHref: (slug) => `/math/7/${slug}`,
          title: "Find your Grade 7 starting point",
        }}
      />
    </ContentGate>
  );
}
