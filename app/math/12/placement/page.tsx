"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade12PlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade12PlacementPage() {
  return (
    <ContentGate backHref="/math/12" backLabel="Back to Grade 12">
      <PlacementRunner
        config={{
          bank: getGrade12PlacementBank(),
          bankMn: getPlacementBankMn("12"),
          namespace: "grade12",
          crumb: "Courses · Grade 12 · Placement",
          crumbMn: "Курсууд · 12-р анги · Түвшин тогтоох шалгалт",
          homeHref: "/math/12",
          homeLabel: "topics",
          homeLabelMn: "Сэдвүүд рүүгээ очих",
          subjectNoun: "Grade-12 topic",
          subjectNounMn: "12-р ангийн сэдэв",
          topicHref: (slug) => `/math/12/${slug}`,
          title: "Find your Grade 12 starting point",
          titleMn: "12-р ангид хаанаас эхлэхээ олоорой",
        }}
      />
    </ContentGate>
  );
}
