import { CourseExamListPage } from "@/components/course/CourseExamPages";

// The High school band's EXIT exams (resource blueprint): three disjoint
// papers over every Grade 12 topic, with a per-topic breakdown.
export default function Page() {
  return <CourseExamListPage course="12" />;
}
