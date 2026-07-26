import { CourseExamPage, generateExamParams } from "@/components/course/CourseExamPages";

export function generateStaticParams() {
  return generateExamParams("integrated-2");
}

export default function Page({ params }: { params: { examId: string } }) {
  return <CourseExamPage examId={params.examId} />;
}
