import test1aData from "@/data/questions/test1a.json";
import test1bData from "@/data/questions/test1b.json";
import test2aData from "@/data/questions/test2a.json";
import test2bData from "@/data/questions/test2b.json";
import test3aData from "@/data/questions/test3a.json";
import test3bData from "@/data/questions/test3b.json";
import test4aData from "@/data/questions/test4a.json";
import test4bData from "@/data/questions/test4b.json";
import test5aData from "@/data/questions/test5a.json";
import test5bData from "@/data/questions/test5b.json";
import test6aData from "@/data/questions/test6a.json";
import test6bData from "@/data/questions/test6b.json";
import test7aData from "@/data/questions/test7a.json";
import test7bData from "@/data/questions/test7b.json";
import test2021aData from "@/data/questions/2021a.json";
import test2021bData from "@/data/questions/2021b.json";
import test2021cData from "@/data/questions/2021c.json";
import test2021dData from "@/data/questions/2021d.json";
import test2022aData from "@/data/questions/2022a.json";
import test2022bData from "@/data/questions/2022b.json";
import test2022cData from "@/data/questions/2022c.json";
import test2022dData from "@/data/questions/2022d.json";
import test2023aData from "@/data/questions/2023a.json";
import test2023bData from "@/data/questions/2023b.json";
import test2023cData from "@/data/questions/2023c.json";
import test2023dData from "@/data/questions/2023d.json";
import test2024aData from "@/data/questions/2024a.json";
import test2024bData from "@/data/questions/2024b.json";
import test2024cData from "@/data/questions/2024c.json";
import test2024dData from "@/data/questions/2024d.json";
import test2025aData from "@/data/questions/2025a.json";
import test2025bData from "@/data/questions/2025b.json";
import test2025cData from "@/data/questions/2025c.json";
import test2025dData from "@/data/questions/2025d.json";

export interface Question {
  source: string;
  testNumber: number;
  testVariant: string;
  questionNumber: number;
  type: string;
  topic: string;
  subtopic: string;
  difficulty: number;
  body: string;
  options?: Record<string, string>;
  answer: string;
  solution: string;
}

export interface TestInfo {
  key: string;
  label: string;
  data: Question[];
  // Whole test is Premium-gated (click from locked state opens upgrade modal).
  isPremium: boolean;
  // Solutions for this test's questions require Premium. Default true;
  // set false for the free sample tests (2024A, 2025A) that ship full solutions.
  solutionsRequirePremium: boolean;
}

// 14 legacy practice tests. Gated behind Premium in the new gating matrix.
const TESTS: TestInfo[] = [
  { key: "1A", label: "Тест 1А", data: test1aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "1B", label: "Тест 1Б", data: test1bData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "2A", label: "Тест 2А", data: test2aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "2B", label: "Тест 2Б", data: test2bData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "3A", label: "Тест 3А", data: test3aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "3B", label: "Тест 3Б", data: test3bData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "4A", label: "Тест 4А", data: test4aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "4B", label: "Тест 4Б", data: test4bData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "5A", label: "Тест 5А", data: test5aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "5B", label: "Тест 5Б", data: test5bData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "6A", label: "Тест 6А", data: test6aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "6B", label: "Тест 6Б", data: test6bData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "7A", label: "Тест 7А", data: test7aData as Question[], isPremium: true, solutionsRequirePremium: true },
  { key: "7B", label: "Тест 7Б", data: test7bData as Question[], isPremium: true, solutionsRequirePremium: true },
];

// 20 real ЭЕШ past papers (2021–2025). Free for all users.
// Full step-by-step solutions free on every 2024 and 2025 variant (8 tests);
// 2021–2023 solutions require Premium.
const PREVIOUS_YEAR_TESTS: TestInfo[] = [
  { key: "2025A", label: "ЭЕШ 2025 · Хувилбар А", data: test2025aData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2025B", label: "ЭЕШ 2025 · Хувилбар Б", data: test2025bData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2025C", label: "ЭЕШ 2025 · Хувилбар В", data: test2025cData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2025D", label: "ЭЕШ 2025 · Хувилбар Г", data: test2025dData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2024A", label: "ЭЕШ 2024 · Хувилбар А", data: test2024aData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2024B", label: "ЭЕШ 2024 · Хувилбар Б", data: test2024bData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2024C", label: "ЭЕШ 2024 · Хувилбар В", data: test2024cData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2024D", label: "ЭЕШ 2024 · Хувилбар Г", data: test2024dData as Question[], isPremium: false, solutionsRequirePremium: false },
  { key: "2023A", label: "ЭЕШ 2023 · Хувилбар А", data: test2023aData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2023B", label: "ЭЕШ 2023 · Хувилбар Б", data: test2023bData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2023C", label: "ЭЕШ 2023 · Хувилбар В", data: test2023cData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2023D", label: "ЭЕШ 2023 · Хувилбар Г", data: test2023dData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2022A", label: "ЭЕШ 2022 · Хувилбар А", data: test2022aData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2022B", label: "ЭЕШ 2022 · Хувилбар Б", data: test2022bData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2022C", label: "ЭЕШ 2022 · Хувилбар В", data: test2022cData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2022D", label: "ЭЕШ 2022 · Хувилбар Г", data: test2022dData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2021A", label: "ЭЕШ 2021 · Хувилбар А", data: test2021aData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2021B", label: "ЭЕШ 2021 · Хувилбар Б", data: test2021bData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2021C", label: "ЭЕШ 2021 · Хувилбар В", data: test2021cData as Question[], isPremium: false, solutionsRequirePremium: true },
  { key: "2021D", label: "ЭЕШ 2021 · Хувилбар Г", data: test2021dData as Question[], isPremium: false, solutionsRequirePremium: true },
];

export const TOPIC_LABELS: Record<string, string> = {
  algebra: "Алгебр",
  geometry: "Геометр",
  trigonometry: "Тригнометр",
  calculus: "Анализ",
  probability: "Магадлал",
  statistics: "Статистик",
  sequences: "Дараалал",
  functions: "Функц",
  logarithms: "Логарифм",
  combinatorics: "Комбинаторик",
  other: "Бусад",
};

export const TOPICS = [
  { value: "algebra", label: "Алгебр" },
  { value: "geometry", label: "Геометр" },
  { value: "trigonometry", label: "Тригнометр" },
  { value: "functions", label: "Функц" },
  { value: "logarithms", label: "Логарифм" },
  { value: "sequences", label: "Дараалал" },
  { value: "probability", label: "Магадлал" },
  { value: "combinatorics", label: "Комбинаторик" },
  { value: "calculus", label: "Анализ" },
  { value: "statistics", label: "Статистик" },
];

const ALL_TESTS_LOOKUP: TestInfo[] = [...TESTS, ...PREVIOUS_YEAR_TESTS];

/**
 * @deprecated Returns only the 14 legacy Premium tests — misleading name.
 *   Use `getTestsForUser(isSubscribed)` for subscription-aware lists,
 *   or `getAllTestsCombined()` for all 34 tests.
 *   Will be removed after Step 2 migrates all consumers.
 */
export function getAllTests(): TestInfo[] {
  return TESTS;
}

// The 20 real ЭЕШ past papers (2021–2025). Free for all users.
export function getPreviousYearTests(): TestInfo[] {
  return PREVIOUS_YEAR_TESTS;
}

// Free-tier tests only — surfaces past papers for logged-out / non-subscribers
// when the UI needs a "no locks, no badges" list.
export function getFreeTests(): TestInfo[] {
  return ALL_TESTS_LOOKUP.filter((t) => !t.isPremium);
}

// Every test, both past papers and the 14 legacy Premium tests.
export function getAllTestsCombined(): TestInfo[] {
  return ALL_TESTS_LOOKUP;
}

// Subscription-aware: subscribers get every test, free users get past papers only.
export function getTestsForUser(isSubscribed: boolean): TestInfo[] {
  return isSubscribed ? ALL_TESTS_LOOKUP : getFreeTests();
}

export function getTestInfo(testKey: string): TestInfo | undefined {
  return ALL_TESTS_LOOKUP.find((t) => t.key === testKey.toUpperCase());
}

export function getTestQuestions(testKey: string): Question[] {
  return getTestInfo(testKey)?.data || [];
}

// Previously returned the 14 legacy tests only, which silently fed premium
// content into free-user study-by-topic. Now returns every question across
// all 34 tests — callers that need the user-aware pool should use
// getQuestionsForUser() / getQuestionsByTopicForUser() instead.
export function getAllQuestions(): Question[] {
  return ALL_TESTS_LOOKUP.flatMap((t) => t.data);
}

// Only questions from free (past-paper) tests.
export function getFreeQuestions(): Question[] {
  return getFreeTests().flatMap((t) => t.data);
}

// Subscription-aware pool for study-by-topic, weak-topic, and mixed practice.
export function getQuestionsForUser(isSubscribed: boolean): Question[] {
  return isSubscribed ? getAllQuestions() : getFreeQuestions();
}

export function getQuestionsByTopic(topic: string): Question[] {
  return getAllQuestions().filter((q) => q.topic === topic);
}

export function getQuestionsByTopicForUser(
  topic: string,
  isSubscribed: boolean,
): Question[] {
  return getQuestionsForUser(isSubscribed).filter((q) => q.topic === topic);
}

export function getQuestionBySource(source: string): Question | undefined {
  return getAllQuestions().find((q) => q.source === source);
}

export function getSimilarQuestions(
  question: Question,
  count: number = 5,
): Question[] {
  const all = getAllQuestions().filter((q) => q.source !== question.source);

  // Score similarity: same topic +3, same subtopic +2, same difficulty +1
  const scored = all.map((q) => {
    let score = 0;
    if (q.topic === question.topic) score += 3;
    if (q.subtopic === question.subtopic) score += 2;
    if (q.difficulty === question.difficulty) score += 1;
    return { question: q, score };
  });

  scored.sort((a, b) => b.score - a.score);
  return scored.slice(0, count).map((s) => s.question);
}

export function getTopicDistribution(): Record<string, number> {
  const dist: Record<string, number> = {};
  for (const q of getAllQuestions()) {
    dist[q.topic] = (dist[q.topic] || 0) + 1;
  }
  return dist;
}

export function getTopicLabel(topic: string): string {
  return TOPIC_LABELS[topic] || topic;
}
