"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import ContentGate from "@/components/genmath/ContentGate";
import { BANDS, bandTopicHref, bandVerdict, getBandPlacementBank, getBandPlacementBankMn } from "@/lib/band-placement";

// The Mid school band's ENTRY test (resource blueprint): samples topics from
// every grade 6–9 and ends with a "start in Grade N" verdict.
export default function MidBandPlacementPage() {
  return (
    <ContentGate backHref="/math#mid-school" backLabel="Back to Courses">
      <PlacementRunner
        config={{
          bank: getBandPlacementBank("mid"),
          bankMn: getBandPlacementBankMn("mid"),
          namespace: BANDS.mid.namespace,
          crumb: "Courses · Mid school · Placement",
          crumbMn: "Курсууд · Дунд анги · Түвшин тогтоох шалгалт",
          homeHref: "/math#mid-school",
          homeLabel: "grades",
          homeLabelMn: "Ангиуд руугаа очих",
          subjectNoun: "grade of Mid school (6–9)",
          subjectNounMn: "дунд анги (6–9)",
          topicHref: (slug) => bandTopicHref("mid", slug),
          title: "Find your Mid school grade",
          titleMn: "Дунд ангид аль ангиас эхлэхээ олоорой",
          verdict: (result) => {
            const v = bandVerdict("mid", result);
            return v.clearedBand
              ? {
                  title: "You've cleared Mid school material",
                  body: "Every grade we sampled was solid. Finish the band properly — sit the Grade 9 material at full depth, then step into High school.",
                  href: "/math/9",
                  cta: "Open Grade 9",
                }
              : {
                  title: `Start in Grade ${v.grade}`,
                  body: `Everything before Grade ${v.grade} looked secure, and starting later would build on gaps. Begin there — the topic list below shows what to hit first.`,
                  href: `/math/${v.grade}`,
                  cta: `Open Grade ${v.grade}`,
                };
          },
          verdictMn: (result) => {
            const v = bandVerdict("mid", result);
            return v.clearedBand
              ? {
                  title: "Дунд ангийн хөтөлбөрийг давсан байна",
                  body: "Шалгасан анги бүрийн мэдлэг тань бат бөх байна. Энэ шатаа бүрэн дуусгаарай: 9-р ангийн хөтөлбөрийг бүрэн гүнзгий үзээд, дараа нь ахлах анги руу шилжээрэй.",
                  href: "/math/9",
                  cta: "9-р ангийг нээх",
                }
              : {
                  title: `${v.grade}-р ангиас эхлээрэй`,
                  body: `${v.grade}-р ангиас өмнөх бүх зүйл бат бөх харагдлаа. Үүнээс хойш эхэлбэл цоорхой мэдлэг дээр тулгуурлах болно. Тэндээс эхлээрэй: доорх сэдвийн жагсаалт юуг түрүүлж үзэхийг харуулна.`,
                  href: `/math/${v.grade}`,
                  cta: `${v.grade}-р ангийг нээх`,
                };
          },
        }}
      />
    </ContentGate>
  );
}
