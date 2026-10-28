"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGeometryPlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

function GeometryPlacementPageInner() {
  return (
    <PlacementRunner
      config={{
        bank: getGeometryPlacementBank(),
        bankMn: getPlacementBankMn("geometry"),
        namespace: "geometry",
        crumb: "Geometry · Placement",
        crumbMn: "Геометр · Түвшин тогтоох шалгалт",
        homeHref: "/math/geometry",
        homeLabel: "units",
        homeLabelMn: "Бүлгүүд рүүгээ очих",
        subjectNoun: "Geometry unit",
        subjectNounMn: "Геометрийн бүлэг",
        topicHref: (slug) => `/math/geometry/${slug}`,
        title: "Place into the Geometry course",
        titleMn: "Геометрийн курсын түвшин тогтоох шалгалт",
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
