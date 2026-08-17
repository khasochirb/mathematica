"use client";

import CommonMistakesList from "@/components/lesson/CommonMistakesList";
import { type Lesson } from "@/lib/esh-lessons";

// ЭШ adapter over the shared common-mistakes list.
export default function LessonCommonMistakes({ lesson }: { lesson: Lesson }) {
  return <CommonMistakesList mistakes={lesson.commonMistakes} />;
}
