"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getPlacementBank } from "@/lib/placement-bank";

export default function PlacementPage() {
  return (
    <PlacementRunner
      config={{
        bank: getPlacementBank(),
        namespace: "grade6",
        crumb: "General Math · Grade 6 · Placement",
        homeHref: "/math/6",
        homeLabel: "topics",
        subjectNoun: "Grade-6 topic",
        topicHref: (slug) => `/math/6/${slug}`,
        title: "Find your starting point",
      }}
    />
  );
}
