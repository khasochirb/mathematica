import CourseProgressView from "@/components/progress/CourseProgressView";
import { allCourseLessonTotals } from "@/lib/genmath-lessons";

// SERVER shell: reads the course registry here (where the corpus is free)
// and hands the client only the ~20 lesson totals its progress tiles need.
export default function CourseProgressPage() {
  return <CourseProgressView lessonTotals={allCourseLessonTotals()} />;
}
