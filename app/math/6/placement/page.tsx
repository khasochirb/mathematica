"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getPlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

function PlacementPageInner() {
  return (
    <PlacementRunner
      config={{
        bank: getPlacementBank(),
        bankMn: getPlacementBankMn("6"),
        namespace: "grade6",
        crumb: "Courses · Grade 6 · Placement",
        crumbMn: "Курсууд · 6-р анги · Түвшин тогтоох шалгалт",
        homeHref: "/math/6",
        homeLabel: "topics",
        homeLabelMn: "Сэдвүүд рүүгээ очих",
        subjectNoun: "Grade-6 topic",
        subjectNounMn: "6-р ангийн сэдэв",
        topicHref: (slug) => `/math/6/${slug}`,
        title: "Find your starting point",
        titleMn: "6-р ангид хаанаас эхлэхээ олоорой",
      }}
    />
  );
}

// Content requires an account; the hub pages above stay public.
export default function PlacementPage() {
  return (
    <ContentGate backHref={"/math/6"} backLabel="Back to Grade 6">
      <PlacementPageInner />
    </ContentGate>
  );
}
