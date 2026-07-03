"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGeometryPlacementBank } from "@/lib/placement-bank";

export default function GeometryPlacementPage() {
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
