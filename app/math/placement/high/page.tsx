"use client";

import PlacementRunner from "@/components/placement/PlacementRunner";
import ContentGate from "@/components/genmath/ContentGate";
import { BANDS, bandTopicHref, bandVerdict, getBandPlacementBank } from "@/lib/band-placement";

// The High school band's ENTRY test (resource blueprint): samples topics from
// every grade 10–12 and ends with a "start in Grade N" verdict.
export default function HighBandPlacementPage() {
  return (
    <ContentGate backHref="/math#high-school" backLabel="Back to Courses">
      <PlacementRunner
        config={{
          bank: getBandPlacementBank("high"),
          namespace: BANDS.high.namespace,
          crumb: "Courses · High school · Placement",
          homeHref: "/math#high-school",
          homeLabel: "grades",
          subjectNoun: "grade of High school (10–12)",
          topicHref: (slug) => bandTopicHref("high", slug),
          title: "Find your High school grade",
          verdict: (result) => {
            const v = bandVerdict("high", result);
            return v.clearedBand
              ? {
                  title: "You've cleared High school material",
                  body: "Every grade we sampled was solid. You're in ЭЕШ territory — the exam hub's tests and prep courses are the right next step.",
                  href: "/practice/esh",
                  cta: "Open the ЭЕШ hub",
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
