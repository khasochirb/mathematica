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
}

const TESTS: TestInfo[] = [
  { key: "1A", label: "Тест 1А", data: test1aData as Question[] },
  { key: "1B", label: "Тест 1Б", data: test1bData as Question[] },
  { key: "2A", label: "Тест 2А", data: test2aData as Question[] },
  { key: "2B", label: "Тест 2Б", data: test2bData as Question[] },
  { key: "3A", label: "Тест 3А", data: test3aData as Question[] },
  { key: "3B", label: "Тест 3Б", data: test3bData as Question[] },
  { key: "4A", label: "Тест 4А", data: test4aData as Question[] },
  { key: "4B", label: "Тест 4Б", data: test4bData as Question[] },
  { key: "5A", label: "Тест 5А", data: test5aData as Question[] },
  { key: "5B", label: "Тест 5Б", data: test5bData as Question[] },
  { key: "6A", label: "Тест 6А", data: test6aData as Question[] },
  { key: "6B", label: "Тест 6Б", data: test6bData as Question[] },
  { key: "7A", label: "Тест 7А", data: test7aData as Question[] },
  { key: "7B", label: "Тест 7Б", data: test7bData as Question[] },
];

const PREVIOUS_YEAR_TESTS: TestInfo[] = [
  { key: "2024A", label: "ЭЕШ 2024 · Хувилбар А", data: test2024aData as Question[] },
  { key: "2024B", label: "ЭЕШ 2024 · Хувилбар Б", data: test2024bData as Question[] },
  { key: "2024C", label: "ЭЕШ 2024 · Хувилбар В", data: test2024cData as Question[] },
  { key: "2024D", label: "ЭЕШ 2024 · Хувилбар Г", data: test2024dData as Question[] },
  { key: "2025A", label: "ЭЕШ 2025 · Хувилбар А", data: test2025aData as Question[] },
  { key: "2025B", label: "ЭЕШ 2025 · Хувилбар Б", data: test2025bData as Question[] },
  { key: "2025C", label: "ЭЕШ 2025 · Хувилбар В", data: test2025cData as Question[] },
  { key: "2025D", label: "ЭЕШ 2025 · Хувилбар Г", data: test2025dData as Question[] },
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

export function getAllTests(): TestInfo[] {
  return TESTS;
}

export function getPreviousYearTests(): TestInfo[] {
  return PREVIOUS_YEAR_TESTS;
}

const ALL_TESTS_LOOKUP: TestInfo[] = [...TESTS, ...PREVIOUS_YEAR_TESTS];

export function getTestInfo(testKey: string): TestInfo | undefined {
  return ALL_TESTS_LOOKUP.find((t) => t.key === testKey.toUpperCase());
}

export function getTestQuestions(testKey: string): Question[] {
  return getTestInfo(testKey)?.data || [];
}

export function getAllQuestions(): Question[] {
  return TESTS.flatMap((t) => t.data);
}

export function getQuestionsByTopic(topic: string): Question[] {
  return getAllQuestions().filter((q) => q.topic === topic);
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
