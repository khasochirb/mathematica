"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade10PlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade10PlacementPage() {
  return (
    <ContentGate backHref="/math/10" backLabel="Back to Grade 10">
      <PlacementRunner
        config={{
          bank: getGrade10PlacementBank(),
          bankMn: getPlacementBankMn("10"),
          namespace: "grade10",
          crumb: "Courses · Grade 10 · Placement",
          crumbMn: "Курсууд · 10-р анги · Түвшин тогтоох шалгалт",
          homeHref: "/math/10",
          homeLabel: "topics",
          homeLabelMn: "Сэдвүүд рүүгээ очих",
          subjectNoun: "Grade-10 topic",
          subjectNounMn: "10-р ангийн сэдэв",
          topicHref: (slug) => `/math/10/${slug}`,
          title: "Find your Grade 10 starting point",
          titleMn: "10-р ангид хаанаас эхлэхээ олоорой",
        }}
      />
    </ContentGate>
  );
}
