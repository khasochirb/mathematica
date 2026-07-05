"use client";

import LessonPlayer from "@/components/genmath/interactive/LessonPlayer";
import derivatives from "@/data/genmath/12/derivatives.json";
import type { GenMathTopic } from "@/lib/genmath-lessons";

const topic = derivatives as unknown as GenMathTopic;

export default function DevWidgetCheck() {
  const lesson = topic.lessons.find((l) => l.slug === "the-derivative-as-a-limit")!;
  return (
    <main style={{ maxWidth: 760, margin: "0 auto", padding: 24 }}>
      <LessonPlayer
        lesson={lesson}
        topicSlug={topic.slug}
        topicTitle={topic.title}
        baseHref="/math/12"
        crumb="Grade 12"
      />
    </main>
  );
}
