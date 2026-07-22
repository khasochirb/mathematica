"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Precalculus, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("precalculus"),
        namespace: "precalculus",
        crumb: "Precalculus · Placement",
        homeHref: "/math/precalculus",
        homeLabel: "units",
        subjectNoun: "Precalculus unit",
        topicHref: (slug) => `/math/precalculus/${slug}`,
        title: "Place into the Precalculus course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/precalculus"} backLabel="Back to Precalculus">
      <PlacementInner />
    </ContentGate>
  );
}
