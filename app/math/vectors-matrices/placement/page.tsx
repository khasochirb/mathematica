"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Vectors & Matrices, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("vectors-matrices"),
        namespace: "vectors-matrices",
        crumb: "Vectors & Matrices · Placement",
        homeHref: "/math/vectors-matrices",
        homeLabel: "units",
        subjectNoun: "Vectors & Matrices unit",
        topicHref: (slug) => `/math/vectors-matrices/${slug}`,
        title: "Place into the Vectors & Matrices course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/vectors-matrices"} backLabel="Back to Vectors & Matrices">
      <PlacementInner />
    </ContentGate>
  );
}
