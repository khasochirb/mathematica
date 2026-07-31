"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import ContentGate from "@/components/genmath/ContentGate";
import { BANDS, bandTopicHref, bandVerdict, getBandPlacementBank } from "@/lib/band-placement";

// The Mid school band's ENTRY test (resource blueprint): samples topics from
// every grade 6–9 and ends with a "start in Grade N" verdict.
export default function MidBandPlacementPage() {
  return (
    <ContentGate backHref="/math#mid-school" backLabel="Back to Courses">
      <PlacementRunner
        config={{
          bank: getBandPlacementBank("mid"),
          namespace: BANDS.mid.namespace,
          crumb: "Courses · Mid school · Placement",
          homeHref: "/math#mid-school",
          homeLabel: "grades",
          subjectNoun: "grade of Mid school (6–9)",
          topicHref: (slug) => bandTopicHref("mid", slug),
          title: "Find your Mid school grade",
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
        }}
      />
    </ContentGate>
  );
}
