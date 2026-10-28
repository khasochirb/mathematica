import CoursePlacement from "@/components/placement/CoursePlacement";
import { getCoursePlacementBank, getCoursePlacementBankMn, getCourseTitleMn } from "@/lib/placement-course-bank";

// SERVER page: harvests the placement bank from the corpus here, so only
// the ~40 questions cross to the client (see lib/placement-course-bank.ts).
// The result seeds a provisional attribute rating and marks the units most
// important for this student.
export default function CoursePlacementPage() {
  return (
    <CoursePlacement
      bank={getCoursePlacementBank("solid-geometry")}
      bankMn={getCoursePlacementBankMn("solid-geometry")}
      courseSlug="solid-geometry"
      courseTitle="Solid Geometry"
      courseTitleMn={getCourseTitleMn("solid-geometry")}
    />
  );
}
