"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Solid Geometry, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("solid-geometry"),
        namespace: "solid-geometry",
        crumb: "Solid Geometry · Placement",
        homeHref: "/math/solid-geometry",
        homeLabel: "units",
        subjectNoun: "Solid Geometry unit",
        topicHref: (slug) => `/math/solid-geometry/${slug}`,
        title: "Place into the Solid Geometry course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/solid-geometry"} backLabel="Back to Solid Geometry">
      <PlacementInner />
    </ContentGate>
  );
}
