// Constructs a representative POST /api/section2/attempts request body
// for a given test key. Useful for staging smoke testing — copy the
// printed JSON and POST it (with auth) to the dev / staging server.
//
// Usage:
//   npm run verify:section2-payload                     # defaults to 2024B
//   npm run verify:section2-payload -- 2025A            # any authored key
//   npm run verify:section2-payload -- 2024B wrong      # mock all-wrong answers
//   npm run verify:section2-payload -- 2024B empty      # mock empty answers
//
// Output: prints a JSON object with sessionId, testKey, attempts[].
// `sessionId` is a randomly-generated UUID for the smoke-run.

import { randomUUID } from "node:crypto";
import {
  getTestSection2,
  parseSlotLabel,
  type Section2Item,
  type Slot,
} from "../lib/esh-section2";

const VARIANT = (process.argv[2] ?? "2024B").toUpperCase();
const MODE = process.argv[3] ?? "perfect"; // "perfect" | "wrong" | "empty"

function decomposePerfect(slot: Slot): Record<string, string> {
  const { prefix, varPart } = parseSlotLabel(slot.label);
  const out: Record<string, string> = {};
  for (let i = 0; i < varPart.length; i++) {
    out[varPart[i]] = slot.answer[prefix.length + i] ?? "";
  }
  return out;
}

function build(item: Section2Item): Record<string, string> {
  if (MODE === "empty") return {};
  const map: Record<string, string> = {};
  for (const slot of item.slots) {
    const perLetter = decomposePerfect(slot);
    if (MODE === "wrong") {
      for (const k of Object.keys(perLetter)) {
        const orig = perLetter[k];
        perLetter[k] = orig === "9" ? "0" : "9";
      }
    }
    Object.assign(map, perLetter);
  }
  return map;
}

const items = getTestSection2(VARIANT);
if (!items) {
  console.error(`Unknown test key: ${VARIANT}`);
  process.exit(1);
}

const payload = {
  sessionId: randomUUID(),
  testKey: VARIANT,
  attempts: items.map((item) => ({
    source: item.source,
    slotAnswers: build(item),
  })),
};

console.log(JSON.stringify(payload, null, 2));
