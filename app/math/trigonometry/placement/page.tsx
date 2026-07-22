"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getCoursePlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

// Placement for Trigonometry, harvested from the problem bank (one form per
// level per unit). The result seeds a provisional attribute rating and marks
// the units most important for this student.
function PlacementInner() {
  return (
    <PlacementRunner
      config={{
        bank: getCoursePlacementBank("trigonometry"),
        namespace: "trigonometry",
        crumb: "Trigonometry · Placement",
        homeHref: "/math/trigonometry",
        homeLabel: "units",
        subjectNoun: "Trigonometry unit",
        topicHref: (slug) => `/math/trigonometry/${slug}`,
        title: "Place into the Trigonometry course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function CoursePlacementPage() {
  return (
    <ContentGate backHref={"/math/trigonometry"} backLabel="Back to Trigonometry">
      <PlacementInner />
    </ContentGate>
  );
}
