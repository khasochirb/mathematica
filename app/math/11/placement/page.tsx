"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade11PlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade11PlacementPage() {
  return (
    <ContentGate backHref="/math/11" backLabel="Back to Grade 11">
      <PlacementRunner
        config={{
          bank: getGrade11PlacementBank(),
          bankMn: getPlacementBankMn("11"),
          namespace: "grade11",
          crumb: "Courses · Grade 11 · Placement",
          crumbMn: "Курсууд · 11-р анги · Түвшин тогтоох шалгалт",
          homeHref: "/math/11",
          homeLabel: "topics",
          homeLabelMn: "Сэдвүүд рүүгээ очих",
          subjectNoun: "Grade-11 topic",
          subjectNounMn: "11-р ангийн сэдэв",
          topicHref: (slug) => `/math/11/${slug}`,
          title: "Find your Grade 11 starting point",
          titleMn: "11-р ангид хаанаас эхлэхээ олоорой",
        }}
      />
    </ContentGate>
  );
}
