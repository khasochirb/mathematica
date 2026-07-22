"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Algebra 1, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("algebra-1"),
        namespace: "algebra-1",
        crumb: "Algebra 1 · Placement",
        homeHref: "/math/algebra-1",
        homeLabel: "units",
        subjectNoun: "Algebra 1 unit",
        topicHref: (slug) => `/math/algebra-1/${slug}`,
        title: "Place into the Algebra 1 course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/algebra-1"} backLabel="Back to Algebra 1">
      <PlacementInner />
    </ContentGate>
  );
}
