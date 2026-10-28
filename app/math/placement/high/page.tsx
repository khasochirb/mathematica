"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import ContentGate from "@/components/genmath/ContentGate";
import { BANDS, bandTopicHref, bandVerdict, getBandPlacementBank, getBandPlacementBankMn } from "@/lib/band-placement";

// The High school band's ENTRY test (resource blueprint): samples topics from
// every grade 10–12 and ends with a "start in Grade N" verdict.
export default function HighBandPlacementPage() {
  return (
    <ContentGate backHref="/math#high-school" backLabel="Back to Courses">
      <PlacementRunner
        config={{
          bank: getBandPlacementBank("high"),
          bankMn: getBandPlacementBankMn("high"),
          namespace: BANDS.high.namespace,
          crumb: "Courses · High school · Placement",
          crumbMn: "Курсууд · Ахлах анги · Түвшин тогтоох шалгалт",
          homeHref: "/math#high-school",
          homeLabel: "grades",
          homeLabelMn: "Ангиуд руугаа очих",
          subjectNoun: "grade of High school (10–12)",
          subjectNounMn: "ахлах анги (10–12)",
          topicHref: (slug) => bandTopicHref("high", slug),
          title: "Find your High school grade",
          titleMn: "Ахлах ангид аль ангиас эхлэхээ олоорой",
          verdict: (result) => {
            const v = bandVerdict("high", result);
            return v.clearedBand
              ? {
                  title: "You've cleared High school material",
                  body: "Every grade we sampled was solid. You're in ЭШ territory — the exam hub's tests and prep courses are the right next step.",
                  href: "/practice/esh",
                  cta: "Open the ЭШ hub",
                }
              : {
                  title: `Start in Grade ${v.grade}`,
                  body: `Everything before Grade ${v.grade} looked secure, and starting later would build on gaps. Begin there — the topic list below shows what to hit first.`,
                  href: `/math/${v.grade}`,
                  cta: `Open Grade ${v.grade}`,
                };
          },
          verdictMn: (result) => {
            const v = bandVerdict("high", result);
            return v.clearedBand
              ? {
                  title: "Ахлах ангийн хөтөлбөрийг давсан байна",
                  body: "Шалгасан анги бүрийн мэдлэг тань бат бөх байна. Та ЭШ-д бэлдэх түвшинд хүрчээ. ЭШ төвийн тестүүд, бэлтгэл курсууд дараагийн зөв алхам болно.",
                  href: "/practice/esh",
                  cta: "ЭШ төвийг нээх",
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
