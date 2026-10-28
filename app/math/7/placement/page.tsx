"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade7PlacementBank } from "@/lib/placement-bank";
import { getPlacementBankMn } from "@/lib/placement-bank-mn";
import ContentGate from "@/components/genmath/ContentGate";

export default function Grade7PlacementPage() {
  return (
    <ContentGate backHref="/math/7" backLabel="Back to Grade 7">
      <PlacementRunner
        config={{
          bank: getGrade7PlacementBank(),
          bankMn: getPlacementBankMn("7"),
          namespace: "grade7",
          crumb: "Courses · Grade 7 · Placement",
          crumbMn: "Курсууд · 7-р анги · Түвшин тогтоох шалгалт",
          homeHref: "/math/7",
          homeLabel: "topics",
          homeLabelMn: "Сэдвүүд рүүгээ очих",
          subjectNoun: "Grade-7 topic",
          subjectNounMn: "7-р ангийн сэдэв",
          topicHref: (slug) => `/math/7/${slug}`,
          title: "Find your Grade 7 starting point",
          titleMn: "7-р ангид хаанаас эхлэхээ олоорой",
        }}
      />
    </ContentGate>
  );
}
