// Every ЭШ question — the 20 past papers and the 14 Premium tests — carries
// two marks: a MAIN topic (one of the five ministry strands) and a SUBTOPIC
// (one of the 14 canonical topic keys, each of which is a course in the
// learn hub). This gate holds three claims at once:
//
//   1. The stored data is canonical. Until 2026-08-12 the files held 57
//      different spellings ("Алгебр", "Matrices", "linear algebra", None)
//      and the runtime papered over it with TOPIC_ALIASES. The alias map is
//      now a safety net for future imports, not something the shipped data
//      leans on — scripts/esh/normalize_question_topics.py is the fixer.
//   2. The five domains PARTITION the 14 topics — every topic in exactly
//      one domain, so a question's two marks can never disagree.
//   3. The learn hub can route every mark: each topic key is a course.
import { describe, it, expect } from "vitest";
import fs from "node:fs";
import path from "node:path";
import {
  ESH_DOMAINS,
  DOMAIN_OF_TOPIC,
  TOPICS,
  canonicalizeTopic,
  eshDomainOf,
} from "@/lib/esh-questions";
import { eshCoursesByDomain, getEshTopicCourse } from "@/lib/esh-course";
import moeCurriculum from "@/data/esh/moe-curriculum.json";

const QDIR = path.join(process.cwd(), "data", "questions");
const CANONICAL = new Set(TOPICS.map((t) => t.value));

function allQuestions(): { file: string; source: string; topic: unknown }[] {
  const out: { file: string; source: string; topic: unknown }[] = [];
  for (const file of fs.readdirSync(QDIR).filter((f) => f.endsWith(".json"))) {
    const questions = JSON.parse(fs.readFileSync(path.join(QDIR, file), "utf-8"));
    for (const q of questions) {
      out.push({ file, source: q.source, topic: q.topic });
    }
  }
  return out;
}

describe("ЭШ question taxonomy (5 main topics × 14 subtopics)", () => {
  it("partitions the 14 subtopics across the 5 main topics", () => {
    expect(ESH_DOMAINS.map((d) => d.key)).toEqual([
      "algebra",
      "geometry_trig",
      "analysis",
      "probability_stats",
      "combinatorics",
    ]);
    const claimed = ESH_DOMAINS.flatMap((d) => d.topics);
    expect(claimed.length).toBe(new Set(claimed).size); // no topic in two domains
    expect(new Set(claimed)).toEqual(CANONICAL); // none missing, none invented
  });

  it("routes every subtopic to a live course in the learn hub", () => {
    for (const topic of Array.from(CANONICAL)) {
      expect(getEshTopicCourse(topic), `no course for topic ${topic}`).toBeTruthy();
    }
    const grouped = eshCoursesByDomain();
    const seen = grouped.flatMap((g) => g.courses.map((c) => c.topic));
    expect(seen.length).toBe(14); // every course appears...
    expect(new Set(seen).size).toBe(14); // ...exactly once
    for (const { domain, courses } of grouped) {
      expect(courses.length, `${domain.key} has no courses`).toBeGreaterThan(0);
    }
  });

  it("stores a canonical subtopic on every question — no aliasing needed", () => {
    const questions = allQuestions();
    expect(questions.length).toBeGreaterThanOrEqual(1484);
    const bad = questions.filter(
      (q) => typeof q.topic !== "string" || !CANONICAL.has(q.topic as string),
    );
    expect(
      bad.map((q) => `${q.file} ${q.source}: ${JSON.stringify(q.topic)}`),
      "run scripts/esh/normalize_question_topics.py (and classify any new residuals)",
    ).toEqual([]);
  });

  it("follows the ministry's strand for every course, with three named exceptions", () => {
    // The five main topics ARE the strands of curriculum А/492
    // (data/esh/moe-curriculum.json, parsed from the ministry PDF). This
    // asserts each course's domain equals the strand of every ministry
    // section it teaches. The exceptions, each deliberate and documented:
    //  - combinatorics: the document files 10.14/11.12/12.14 under
    //    МАГАДЛАЛ, СТАТИСТИК; the hub promotes counting to a main topic
    //    (owner decision, 2026-08-12).
    //  - linear_algebra: mixed IN THE DOCUMENT (matrices 10.4 and systems
    //    11.2 are АЛГЕБР; vectors 10.9/11.8 and transformations 10.11 are
    //    ГЕОМЕТР) — one course needs one home; majority of sections wins.
    //  - sequences: 11.4 (дараалал) is АЛГЕБР but 12.9 (цуваа) is АНАЛИЗЫН
    //    ЭХЛЭЛ in the document; the course lives with its core exam
    //    content, the progressions of 11.4.
    const strandToDomain: Record<string, string> = {
      algebra: "algebra",
      "geometry-trigonometry": "geometry_trig",
      analysis: "analysis",
      "probability-statistics": "probability_stats",
    };
    const strandOf = new Map<string, string>(
      moeCurriculum.sections.map((s: { code: string; strand: string }) => [s.code, s.strand]),
    );
    const MIXED_OK = new Set(["combinatorics", "linear_algebra", "sequences"]);
    for (const { domain, courses } of eshCoursesByDomain()) {
      for (const course of courses) {
        if (MIXED_OK.has(course.topic)) continue;
        for (const sec of course.moeSections) {
          expect(
            strandToDomain[strandOf.get(sec)!],
            `${course.topic}: ministry section ${sec} is strand ${strandOf.get(sec)}, ` +
              `but the course sits in domain ${domain.key}`,
          ).toBe(domain.key);
        }
      }
    }
    // The exceptions still anchor where claimed — a majority of
    // linear_algebra's sections really are geometry, and sequences really
    // does carry the algebra-strand section it is filed under.
    const la = eshCoursesByDomain().find((g) => g.domain.key === "geometry_trig")!
      .courses.find((c) => c.topic === "linear_algebra")!;
    const geoSections = la.moeSections.filter((s) => strandOf.get(s) === "geometry-trigonometry");
    expect(geoSections.length * 2).toBeGreaterThan(la.moeSections.length);
  });

  it("ships exam weights that match the tagged past papers", () => {
    // data/esh/exam-weights.json is what /practice/esh/topics displays as
    // "% of exam". It is generated (scripts/esh/build_exam_weights.py), so
    // this recomputes the same counts from the question files and fails if
    // the shipped numbers have gone stale — invented weights are exactly
    // what this page was rebuilt to eliminate.
    const weights = JSON.parse(
      fs.readFileSync(path.join(process.cwd(), "data", "esh", "exam-weights.json"), "utf-8"),
    );
    const isPastPaper = (f: string) => /^20\d\d[a-z](-section2)?\.json$/.test(f);
    const perTopic = new Map<string, number>();
    let total = 0;
    for (const q of allQuestions().filter((q) => isPastPaper(q.file))) {
      perTopic.set(q.topic as string, (perTopic.get(q.topic as string) ?? 0) + 1);
      total++;
    }
    expect(weights.basedOn.questions).toBe(total);
    for (const d of weights.domains) {
      const domain = ESH_DOMAINS.find((x) => x.key === d.key)!;
      expect(domain, `unknown domain ${d.key} in weights`).toBeTruthy();
      const count = domain.topics.reduce((n, t) => n + (perTopic.get(t) ?? 0), 0);
      expect(d.count, `${d.key} count stale — rerun build_exam_weights.py`).toBe(count);
      expect(d.sharePct).toBeCloseTo((100 * count) / total, 1);
      for (const row of d.topics) {
        expect(row.count, `${row.topic} stale`).toBe(perTopic.get(row.topic) ?? 0);
      }
    }
  });

  it("derives a main topic for every question", () => {
    for (const q of allQuestions()) {
      const domain = DOMAIN_OF_TOPIC[q.topic as string];
      expect(domain, `${q.file} ${q.source}`).toBeTruthy();
    }
    // and the helper agrees with the raw map, including through aliases
    expect(eshDomainOf("Matrices")?.key).toBe("geometry_trig");
    expect(eshDomainOf("тоон онол")?.key).toBe("algebra");
    expect(eshDomainOf("nonsense")).toBeNull();
    expect(canonicalizeTopic("number theory")).toBe("arithmetic");
  });
});
