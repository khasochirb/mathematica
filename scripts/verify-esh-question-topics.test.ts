// Every ЭЕШ question — the 20 past papers and the 14 Premium tests — carries
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

describe("ЭЕШ question taxonomy (5 main topics × 14 subtopics)", () => {
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
