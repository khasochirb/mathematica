"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Algebra 2, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("algebra-2"),
        namespace: "algebra-2",
        crumb: "Algebra 2 · Placement",
        homeHref: "/math/algebra-2",
        homeLabel: "units",
        subjectNoun: "Algebra 2 unit",
        topicHref: (slug) => `/math/algebra-2/${slug}`,
        title: "Place into the Algebra 2 course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/algebra-2"} backLabel="Back to Algebra 2">
      <PlacementInner />
    </ContentGate>
  );
}
