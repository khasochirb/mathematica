"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade9PlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade9PlacementPage() {
  return (
    <ContentGate backHref="/math/9" backLabel="Back to Grade 9">
      <PlacementRunner
        config={{
          bank: getGrade9PlacementBank(),
          bankMn: getPlacementBankMn("9"),
          namespace: "grade9",
          crumb: "Courses · Grade 9 · Placement",
          crumbMn: "Курсууд · 9-р анги · Түвшин тогтоох шалгалт",
          homeHref: "/math/9",
          homeLabel: "topics",
          homeLabelMn: "Сэдвүүд рүүгээ очих",
          subjectNoun: "Grade-9 topic",
          subjectNounMn: "9-р ангийн сэдэв",
          topicHref: (slug) => `/math/9/${slug}`,
          title: "Find your Grade 9 starting point",
          titleMn: "9-р ангид хаанаас эхлэхээ олоорой",
        }}
      />
    </ContentGate>
  );
}
