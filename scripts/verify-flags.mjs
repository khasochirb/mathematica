#!/usr/bin/env node
// verify:flags — mechanical check of the ops-flags registry (memory/flags.md).
//
// Hits GET <base>/api/health/flags and compares every reported check against
// its healthy value (lib/flags.ts HEALTHY). Exit 0 = every flag closed;
// exit 1 = at least one flag open or unverifiable.
//
// Usage:
//   node scripts/verify-flags.mjs                          # local dev server
//   node scripts/verify-flags.mjs https://www.mongolpotential.com
//   BASE_URL=https://www.mongolpotential.com npm run verify:flags
//
// From a Claude cloud session the sandbox proxy blocks direct egress to prod
// — fetch the same URL through the Vercel MCP (web_fetch_vercel_url) and
// read the JSON by eye instead.

const HEALTHY = {
  anthropic_api_key: "configured",
  migration_008_student_profiles: "applied",
  migration_009_attempts_context: "applied",
};

const base = (process.argv[2] || process.env.BASE_URL || "http://localhost:3000").replace(/\/$/, "");
const url = `${base}/api/health/flags`;

let payload;
try {
  const res = await fetch(url, { headers: { accept: "application/json" } });
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  payload = await res.json();
} catch (err) {
  console.error(`verify:flags — could not reach ${url}: ${err.message ?? err}`);
  console.error("Is the server running? For prod, note the endpoint exists only after the first deploy that includes it.");
  process.exit(1);
}

const checks = payload?.checks ?? {};
const details = payload?.details ?? {};
let open = 0;

console.log(`verify:flags — ${url} (generated ${payload.generatedAt ?? "?"})`);
for (const [key, healthy] of Object.entries(HEALTHY)) {
  const actual = checks[key] ?? "(absent)";
  const ok = actual === healthy;
  if (!ok) open += 1;
  // On a non-healthy probe the endpoint reports the error code it saw
  // ("42703", "PGRST205", "42501", …). Printing it here is the difference
  // between "unknown" and knowing which runbook to open.
  const why = !ok && details[key] ? `, code ${details[key]}` : "";
  console.log(`  ${ok ? "✓" : "✗"} ${key}: ${actual}${ok ? "" : `  (healthy: ${healthy}${why})`}`);
}

// Surface any checks the endpoint reports that this script doesn't know —
// a new sentinel was added without updating HEALTHY here.
for (const key of Object.keys(checks)) {
  if (!(key in HEALTHY)) console.log(`  ? ${key}: ${checks[key]}  (not in HEALTHY — update scripts/verify-flags.mjs)`);
}

if (open > 0) {
  console.log(`\n${open} flag(s) OPEN — runbooks in memory/flags.md`);
  process.exit(1);
}
console.log("\nall flags closed");
