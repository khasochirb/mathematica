"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade10PlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade10PlacementPage() {
  return (
    <ContentGate backHref="/math/10" backLabel="Back to Grade 10">
      <PlacementRunner
        config={{
          bank: getGrade10PlacementBank(),
          namespace: "grade10",
          crumb: "General Math · Grade 10 · Placement",
          homeHref: "/math/10",
          homeLabel: "topics",
          subjectNoun: "Grade-10 topic",
          topicHref: (slug) => `/math/10/${slug}`,
          title: "Find your Grade 10 starting point",
        }}
      />
    </ContentGate>
  );
}
