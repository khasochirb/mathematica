import Link from "next/link";
import { notFound } from "next/navigation";
import { ArrowLeft } from "lucide-react";
import ExamRunner from "@/components/course/ExamRunner";
import ExamList from "@/components/course/ExamList";
import { getCourseExam, getCourseExams } from "@/lib/course-exam";
import ContentGate from "@/components/genmath/ContentGate";
import { isExamFree } from "@/lib/course-access";

// Server components for the two exam routes. The runner itself is a client
// component; these only resolve the exam and render chrome, which keeps the
// 204-question payload off every course page that merely LINKS to an exam.

export function generateExamParams(course: string) {
  return getCourseExams(course).map((e) => ({ examId: e.meta.examId }));
}

export function CourseExamListPage({ course }: { course: string }) {
  const exams = getCourseExams(course);
  if (exams.length === 0) notFound();
  const title = exams[0].meta.courseTitle;

  return (
    <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
      <div className="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 pt-10 pb-16">
        <div className="flex items-center gap-3 mb-6">
          <Link
            className="p-2 rounded-md transition-colors"
            style={{ background: "var(--bg-2)", border: "1px solid var(--line)", color: "var(--fg-2)" }}
            href={`/math/${course}`}
          >
            <ArrowLeft className="w-4 h-4" />
          </Link>
          <div className="eyebrow">{title}</div>
        </div>

        <h1
          className="serif"
          style={{ fontWeight: 400, fontSize: "clamp(30px,5vw,50px)", letterSpacing: "-0.04em", lineHeight: 1.05, color: "var(--fg)" }}
        >
          Practice Exams
        </h1>
        <p className="mt-4 mb-8" style={{ color: "var(--fg-1)", fontSize: 17, maxWidth: "56ch" }}>
          {exams[0].meta.intro} The three papers share no questions, so you can sit all of them.
        </p>

        <ExamList course={course} exams={exams} />
      </div>
    </div>
  );
}

export function CourseExamPage({ examId }: { examId: string }) {
  const exam = getCourseExam(examId);
  if (!exam) notFound();
  // Paper 1 of each course is the free sample; papers 2+ are Premium
  // (policy: lib/course-access.ts).
  return (
    <ContentGate
      free={isExamFree(examId)}
      backHref={`/math/${exam.meta.course}/exam`}
      backLabel="Back to exams"
    >
      <div className="min-h-screen pt-20" style={{ background: "var(--bg)" }}>
        <ExamRunner exam={exam} />
      </div>
    </ContentGate>
  );
}
