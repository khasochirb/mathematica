"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Combinatorics, Probability & Statistics, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("prob-stats"),
        namespace: "prob-stats",
        crumb: "Combinatorics, Probability & Statistics · Placement",
        homeHref: "/math/prob-stats",
        homeLabel: "units",
        subjectNoun: "Combinatorics, Probability & Statistics unit",
        topicHref: (slug) => `/math/prob-stats/${slug}`,
        title: "Place into the Combinatorics, Probability & Statistics course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/prob-stats"} backLabel="Back to Combinatorics, Probability & Statistics">
      <PlacementInner />
    </ContentGate>
  );
}
