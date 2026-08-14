"use client";

// Dev-only preview for the diagnostic placement. The real placement pages sit
// behind ContentGate, so eyeballing a sitting — the question flow, the
// "looking at your answer" pause, the results screen with the tutor's findings
// — otherwise means signing a real account in. This mounts the SAME
// PlacementRunner, ungated, against a real bank.
//
// It runs the real engine, so what you see here is what a student sees. With
// no ANTHROPIC_API_KEY (or signed out) the endpoint answers `fallback` and the
// deterministic path drives, which is exactly the case worth being able to
// walk deliberately.
//
// Gated to non-production via NODE_ENV, matching app/dev/gamification.

import { notFound } from "next/navigation";
import PlacementRunner from "@/components/placement/PlacementRunner";
import { getGrade11PlacementBank } from "@/lib/placement-bank";

const isDev = process.env.NODE_ENV !== "production";

export default function PlacementPreviewPage() {
  if (!isDev) notFound();
  return (
    <PlacementRunner
      config={{
        bank: getGrade11PlacementBank(),
        namespace: "dev-preview",
        crumb: "Dev · Grade 11 · Placement preview",
        homeHref: "/math/11",
        homeLabel: "topics",
        subjectNoun: "Grade-11 topic",
        topicHref: (slug) => `/math/11/${slug}`,
        title: "Find your Grade 11 starting point",
      }}
    />
  );
}
