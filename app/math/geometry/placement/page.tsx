"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGeometryPlacementBank } from "@/lib/placement-bank";
import ContentGate from "@/components/genmath/ContentGate";

function GeometryPlacementPageInner() {
  return (
    <PlacementRunner
      config={{
        bank: getGeometryPlacementBank(),
        namespace: "geometry",
        crumb: "Geometry · Placement",
        homeHref: "/math/geometry",
        homeLabel: "units",
        subjectNoun: "Geometry unit",
        topicHref: (slug) => `/math/geometry/${slug}`,
        title: "Place into the Geometry course",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function GeometryPlacementPage() {
  return (
    <ContentGate backHref={"/math/geometry"} backLabel="Back to Geometry">
      <GeometryPlacementPageInner />
    </ContentGate>
  );
}
