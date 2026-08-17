# Status — Build

The single code-writing chat. Owns routes, nav, pages, app logic, migrations,
schema, health probes, `data/`, `scripts/`, the skill graph and items.
Security reviews and gates but never applies.

Supersedes `memory/status/design.md` and `memory/status/content.md`, both of
which stay in the repo as history. Write **only this file**; read all of them.
Newest entry at the top.

---

## 2026-08-17 06:45 UTC — mode: ship

**Did:** Took the handover from Design and structure. Reported the nav state
(nothing left to undo — Design's last commit already reversed the cut), wrote
the two rule changes and the rule-1 amendment into the working copy, cancelled
the `topics`/`problems` drop in writing, and shipped the FLAG-010 honesty fix
so the health probe reports what it saw instead of a bare verdict.

**Landed where:** branch `claude/grade-6-math-verify-xe1tak`. Not deployed —
no deploy was requested.

**Blocked on:** **production database access.** The Supabase MCP needs
interactive approval and this session is non-interactive, so
`select count(*) from skills;` could not run and the new endpoint output could
not be fetched from production. I have never applied a migration and could not
prove I can. Nothing this session required it, but the next thing that does
will stop dead. Needs an interactive session or standing approval.

**Others should know:**

- **SECURITY — four things changed under you.**
  1. **Design and structure is closed.** I am now the only chat that writes
     code, and the chat that applies migrations. Your review-and-gate role is
     unchanged; you still never apply.
  2. **The navigation cut is reversed** (Khas's call). IB, AP, the topic
     courses and the grade courses stay in navigation permanently and get
     upgraded one at a time. Architecture rules 4 and 7 were rewritten and
     rule 1 amended — see `CLAUDE.md` § Product rules for the verbatim text.
  3. **`/api/health/flags` changed shape.** `details` was `key → "42501"`, a
     flat string map; it is now `key → { code, rowCount, unfilteredRowCount,
     expectedAtLeast, message, table, column, filter, migration }`. `checks`
     is untouched, so `scripts/verify-flags.mjs`'s pass/fail is unaffected —
     but its *printing* was reading `details[key]` as a string and would have
     rendered `[object Object]`; that is fixed in the same commit. Any other
     consumer you know of needs the same look.
  4. **The endpoint now returns raw PostgREST messages** on non-applied
     probes, unauthenticated. I judged this within the existing rationale —
     these sentinels only ever touch table and column names, which is schema
     metadata, the same reasoning that already makes the endpoint public, and
     the probe stays HEAD-only so no row ever transits. But it is a widening
     of a public surface and it is your call, not mine. Say the word and I
     will gate `details` behind a header or an env flag.

- **FLAG-010 is now honest, not yet fixed.** That was the instruction and the
  distinction matters: pass/fail logic is byte-for-byte the same, and a test
  (`"pass/fail logic is UNCHANGED"`) pins every verdict so that a later
  threshold change has to be deliberate. What changed is that a non-"applied"
  verdict must now carry its evidence. On the next production read, the same
  `"missing"` will come with `rowCount`, `unfilteredRowCount`,
  `expectedAtLeast` and the raw message — which separates the three causes
  that currently collapse into one word: the probe saw zero rows, or it saw
  184 and the floor is wrong, or `hub=eysh` matched nothing while the table is
  full. **The endpoint has not been re-read from production** (see Blocked
  on), so FLAG-010 stays OPEN and the diagnosis is still Design's, untested.

- **The `topics` / `problems` drop is cancelled in writing.**
  `010_skill_graph.sql` §5 still contains a commented-out drop that tells the
  reader to "uncomment as its own migration (011)". Two traps in that: 011 is
  taken by the ЭЕШ seed, and the Stream B sign-off it waits on no longer
  exists as a chat. I did not edit 010 — it is applied, and applied files are
  not rewritten after the fact — so the cancellation is recorded in
  `supabase/migrations/NUMBERING.md`. `topics`=13, `problems`=20, `streaks`=2
  are live and load-bearing: the legacy course pages run on them until each
  door is migrated.

- **`/docs/plan/` still does not exist in this repository.** Checked again
  today against every branch on `origin`. `01-ARCHITECTURE.md` and
  `04-WORK-ORDERS.md` are owner-held. The two rewritten rules are therefore in
  `CLAUDE.md`, which that file itself designates as the working copy, with a
  note recording the two corrections the owner still needs to make in their
  own copy — including that its "Dropped — all zero rows" section names three
  tables that hold live rows and currently reads as an instruction to delete
  real data.

- **`CLAUDE.md` on `origin/main` is still the four-chat version** (`550fd74`).
  It does not mention ship/content modes, does not close Design, and lists
  IB/AP under "Not building, by decision (until 2027)". I worked from Khas's
  message, not the file, and have amended the product rules. The ownership
  table and the mode protocol still need writing by whoever holds the master.

- **Grades 2–4 remain out of navigation, and I left them there.** That is a
  separate and older owner call (2026-08-13, "elementary is the last thing we
  worry about"), not part of the Phase 0 cut being reversed. `ALL_GRADES` in
  `lib/genmath-spines.ts` marks 1–5 inactive. If "the grade courses all stay
  live" was meant to include them, it is one line plus the catalog section —
  say so and it is a ten-minute job.

- Nav state as found, before I changed anything: **nothing was left to undo.**
  All four hubs are in the header, `/math` links the twelve topic and
  integrated courses plus every active grade, `/practice/ib` links its three
  courses, and `data/unpublished-routes.json` is down to `/practice/session`
  alone — so nothing carries `noindex` any more except that one route, which
  is correct (its tables were dropped by 010; it would throw on load). The one
  real finding is that **there is no sitemap and no robots.txt anywhere in the
  repo** — no `app/sitemap.ts`, no `public/sitemap.xml`. So "missing from the
  sitemap" is true of every route on the site equally, and always has been.
  Nothing was cut from a sitemap that never existed. Building one is new work,
  not an undo, so I have not done it.
