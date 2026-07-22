"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Calculus, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("calculus"),
        namespace: "calculus",
        crumb: "Calculus · Placement",
        homeHref: "/math/calculus",
        homeLabel: "units",
        subjectNoun: "Calculus unit",
        topicHref: (slug) => `/math/calculus/${slug}`,
        title: "Place into the Calculus course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/calculus"} backLabel="Back to Calculus">
      <PlacementInner />
    </ContentGate>
  );
}
