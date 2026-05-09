// Section 2 (Part 2) content loader — see memory/section2-design.md.
//
// Section 2 is the EYSH multi-part fill-in section: 4 problems (2.1-2.4),
// 28 points total per test. Content lives in
// `data/questions/<testKey>-section2.json`.
//
// Currently authored: 2021/2022/2023/2024/2025 × A/B/C/D (20 files).
// `getTestSection2` returns undefined for any unauthored key.

import data2021A from "@/data/questions/2021a-section2.json";
import data2021B from "@/data/questions/2021b-section2.json";
import data2021C from "@/data/questions/2021c-section2.json";
import data2021D from "@/data/questions/2021d-section2.json";
import data2022A from "@/data/questions/2022a-section2.json";
import data2022B from "@/data/questions/2022b-section2.json";
import data2022C from "@/data/questions/2022c-section2.json";
import data2022D from "@/data/questions/2022d-section2.json";
import data2023A from "@/data/questions/2023a-section2.json";
import data2023B from "@/data/questions/2023b-section2.json";
import data2023C from "@/data/questions/2023c-section2.json";
import data2023D from "@/data/questions/2023d-section2.json";
import data2024A from "@/data/questions/2024a-section2.json";
import data2024B from "@/data/questions/2024b-section2.json";
import data2024C from "@/data/questions/2024c-section2.json";
import data2024D from "@/data/questions/2024d-section2.json";
import data2025A from "@/data/questions/2025a-section2.json";
import data2025B from "@/data/questions/2025b-section2.json";
import data2025C from "@/data/questions/2025c-section2.json";
import data2025D from "@/data/questions/2025d-section2.json";

export type Section2ProblemId = "2.1" | "2.2" | "2.3" | "2.4";

export type SlotType = "digit" | "integer";

export interface Slot {
  label: string;
  type: SlotType;
  answer: string;
}

export interface Section2Item {
  source: string;
  test: string;
  section: 2;
  problem: Section2ProblemId;
  subproblem: number;
  type: "fill_in";
  context: string;
  instruction: string;
  slots: Slot[];
  points: number;
  solution: string;
}

const SECTION2_BY_KEY: Record<string, Section2Item[]> = {
  "2021A": data2021A as Section2Item[],
  "2021B": data2021B as Section2Item[],
  "2021C": data2021C as Section2Item[],
  "2021D": data2021D as Section2Item[],
  "2022A": data2022A as Section2Item[],
  "2022B": data2022B as Section2Item[],
  "2022C": data2022C as Section2Item[],
  "2022D": data2022D as Section2Item[],
  "2023A": data2023A as Section2Item[],
  "2023B": data2023B as Section2Item[],
  "2023C": data2023C as Section2Item[],
  "2023D": data2023D as Section2Item[],
  "2024A": data2024A as Section2Item[],
  "2024B": data2024B as Section2Item[],
  "2024C": data2024C as Section2Item[],
  "2024D": data2024D as Section2Item[],
  "2025A": data2025A as Section2Item[],
  "2025B": data2025B as Section2Item[],
  "2025C": data2025C as Section2Item[],
  "2025D": data2025D as Section2Item[],
};

export const SECTION2_AUTHORED_KEYS: readonly string[] = Object.freeze(
  Object.keys(SECTION2_BY_KEY),
);

export function getTestSection2(testKey: string): Section2Item[] | undefined {
  return SECTION2_BY_KEY[testKey.toUpperCase()];
}

export function hasSection2(testKey: string): boolean {
  return testKey.toUpperCase() in SECTION2_BY_KEY;
}

// Parse a slot label into a literal-digit prefix and the variable letter
// portion. Used by the renderer to distinguish `1e=10` (prefix "1", varPart
// "e") from plain `bc=18` (prefix "", varPart "bc"). Currently only 2024B
// and 2024C 2.4.2 use the literal-prefix shape.
export function parseSlotLabel(label: string): {
  prefix: string;
  varPart: string;
} {
  const match = /^(\d*)([A-Za-z]+)$/.exec(label);
  if (!match) return { prefix: "", varPart: label };
  return { prefix: match[1] ?? "", varPart: match[2] };
}
