import DashboardHome from "@/components/dashboard/DashboardHome";
import { allCourseLessonTotals } from "@/lib/genmath-lessons";

// SERVER shell: reads the course registry here (where the corpus is free)
// and hands the client only the ~20 lesson totals its progress bars need.
export default function DashboardPage() {
  return <DashboardHome lessonTotals={allCourseLessonTotals()} />;
}
