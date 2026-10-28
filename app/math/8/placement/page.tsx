"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade8PlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade8PlacementPage() {
  return (
    <ContentGate backHref="/math/8" backLabel="Back to Grade 8">
      <PlacementRunner
        config={{
          bank: getGrade8PlacementBank(),
          bankMn: getPlacementBankMn("8"),
          namespace: "grade8",
          crumb: "Courses · Grade 8 · Placement",
          crumbMn: "Курсууд · 8-р анги · Түвшин тогтоох шалгалт",
          homeHref: "/math/8",
          homeLabel: "topics",
          homeLabelMn: "Сэдвүүд рүүгээ очих",
          subjectNoun: "Grade-8 topic",
          subjectNounMn: "8-р ангийн сэдэв",
          topicHref: (slug) => `/math/8/${slug}`,
          title: "Find your Grade 8 starting point",
          titleMn: "8-р ангид хаанаас эхлэхээ олоорой",
        }}
      />
    </ContentGate>
  );
}
