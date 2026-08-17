# Status — Design and structure

Owns routes, nav, migrations, schema. Never touches lesson/problem content.
Still the only stream that applies migrations (THE DATABASE RULE).

Write **only this file**; read all of them. Newest entry at the top. Format
is the template in `CLAUDE.md` § "End every session with this".

(Renamed from `design.md` on 2026-08-17 when the chat structure went to
three streams. Same stream, same file, history preserved through `git mv`.)

---

## 2026-08-17 05:40 UTC — HANDOVER (this chat is closing)

**Did:** Nothing new this session beyond this handover — I was closed part-way
through a three-item work order. Item 1 (reverse the navigation cut) was
already delivered and deployed earlier today as `90002a9`; items 2 and 3 were
NOT started. Everything below is state, not plan.

**Landed where:** everything is on `main` and deployed. `main` and
`claude/problem-bank-premium-design-osj7de` are identical at `90002a9`, both
pushed, working tree clean, no stashes, no unpushed branch anywhere.

**Blocked on:** two files the incoming chat will be told exist and which do
NOT exist in this repository. See "Things you will not find in a file".

---

### 1. Navigation state, exactly as it stands

The cut is already reversed. `90002a9` (deployed, verified on production
17 Aug) restored the menu and republished everything except one route.

**Live in navigation** — top bar reads
`Home · [Dashboard] · 1-on-1 Tutoring · Resources ▾ · About ▾`
(Dashboard renders only when signed in):

| Menu position | Route | Badge |
|---|---|---|
| Resources → Math hubs | `/practice/esh` | Live |
| Resources → Math hubs | `/practice/sat` | Live |
| Resources → Math hubs | `/practice/ib` | Live |
| Resources → Math hubs | `/practice/ap` | **Soon** |
| Resources → Courses | `/math` | — |
| Top bar | `/`, `/dashboard`, `/tutoring` | — |
| About ▾ | `/about#about`, `/contact` | — |

`/practice/ap` keeps the "Soon" badge because the page is literally seven
lines — `<ComingSoonHub slug="ap" />` — with no curriculum behind it. It is
IN navigation and reachable, which is what the owner asked for; the badge is
honesty about what is behind the door, not a soft cut. Under the new rule 7
this is the "legacy" tier, not a hidden thing. Promote the badge when AP has
lessons.

**Out of navigation: exactly one route, and it is not a product decision.**
`/practice/session` — the orphaned legacy runner. Migration 010 DROPPED its
three tables (`practice_sessions`, `session_answers`, `topic_progress`), so
the route throws on load. It is the sole entry in
`data/unpublished-routes.json`. **Do not republish it to satisfy "nothing
gets cut"** — it is cut by a dropped schema, not by the navigation decision.
Rebuild it on the skill graph, then publish.

**`noindex`: one route.** `/practice/session` serves
`x-robots-tag: noindex, nofollow` (verified on production 17 Aug). Every
previously-cut route now serves **200 with no `x-robots-tag`** — spot-checked
on production for `/math/geometry` and `/practice/ap`, and on the shipped
build locally for `/math`, `/math/6`, `/math/geometry`, `/math/algebra-1`,
`/math/ib-sl`, `/practice/ib`, `/practice/ap`, `/ib-analytics`, `/math/9`.

**Internal links: already restored, automatically.** Three catalogs had been
filtering their own lists — the homepage hub cards, the `/math` course hub,
and the dashboard placement list. They filter through
`publishedOnly()`/`isUnpublished()` (`lib/unpublished.ts`), which now excludes
only `/practice/session`, so they show everything again with no per-file edit.
Confirmed: the `/math` catalog lists Geometry and Algebra again.

**Sitemap: THERE IS NO SITEMAP.** This is the one part of the owner's
question whose honest answer is not a list of routes. There is no
`app/sitemap.ts`, no `public/sitemap.xml`, and **no `robots.txt` either** —
I searched `app/` and `public/`. So "which routes are missing from the
sitemap" is *all of them*, because the file does not exist. IB and the
courses are not specifically excluded from anything. If the owner wants the
republished routes discoverable by search, someone has to CREATE a sitemap;
lifting `noindex` (done) only stops active suppression. Next.js generates one
from `app/sitemap.ts` — that is a new file, not a new route, so rule 4 does
not bite.

**Do not re-run the restore.** Items 2, 3 and 5 of Stream A in
`04-WORK-ORDERS.md` are withdrawn per the owner, and the withdrawal is
already reflected in the repo. The three tests that used to encode the cut
now encode the reversal (`lib/hub-tabs.test.ts`): the prefix list is asserted
to be exactly `["/practice/session"]` with the dropped-tables reason inline,
and a second test asserts IB, AP, the courses and grades 6–7 are all
published. The rule-7 scan ("no live file links into an unpublished area") is
untouched and passing — that is what proves the restore is complete rather
than half-done.

### 2. Real route names, where the plan docs are wrong

`/docs/plan/` uses names that do not exist. The repo is right (CLAUDE.md rule
7). The ones I hit:

| Doc says | Reality |
|---|---|
| `/eysh` | **`/practice/esh`** (and the DB hub value is `'eysh'` — the route and the column genuinely differ; this is not a typo to "fix") |
| — | `/practice/sat`, `/practice/ib`, `/practice/ap` |
| — | `/math` is the Courses hub; courses are `/math/<slug>` (`/math/6`, `/math/geometry`, `/math/ib-sl`, …) |
| — | `/ib-analytics` and `/sat-analytics` are top-level, not under a hub |
| — | Today and Me **do not exist as routes at all** |

The `hub` CHECK constraint in `010_skill_graph.sql` accepts only `'eysh'` and
`'sat'`. Content Creation lost a generation pass to writing `'esh'`; if you
add a hub you must widen that constraint first.

### 3. FLAG-010 — the health probe lies, full diagnosis

`/api/health/flags` answers `"migration_011_seed_esh_graph":"missing"` for a
table holding 184 rows, with an **empty `details` map** so it does not even
report a code. The seed is fine; the probe is wrong. Do not re-apply 011 on
the strength of that endpoint.

**Ruled out, all checked directly against production:**

- Row count is **184** for `hub='eysh'` — as superuser *and* under
  `set role` for `service_role`, `anon` and `authenticated` separately. All
  three can read it.
- RLS is on, with a permissive `skills_select_all` SELECT policy (no `TO`
  clause, so it applies to PUBLIC).
- `service_role` holds `SELECT` on the table and `rolbypassrls = true`.
- No second `skills` table in another schema — `information_schema.tables`
  returns exactly one, in `public`, 8 columns.
- `notify pgrst, 'reload schema'` issued; re-probed after; no change.
- The deployed build is correct. `a532ae4` carries the right sentinel
  (`table: skills`, `column: id`, `where hub='eysh'`, `atLeast: 150`). Its
  sibling `migration_010_skill_graph` sentinel exists **only** in that build
  and reports `applied` — which also proves the app is pointed at this
  Supabase project and not another one.

**The lead, and it is a sharp one — the failing probes split by table:**

| Sentinel | Table | Verdict |
|---|---|---|
| `migration_009_attempts_context` | `attempts` | applied ✅ |
| `migration_010_skill_graph` | `attempts` | applied ✅ |
| `migration_008_student_profiles` | `profiles` | **unknown**, no code |
| `migration_011_seed_esh_graph` | `skills` | **missing**, no code |

Both passing probes are on `attempts`. Both failing probes are on some other
table. That is unlikely to be coincidence and is where I would start.

Note what "unknown with no code" means in `classifyProbe` (`lib/flags.ts`):
an error object whose `code` is falsy AND whose `message` matched none of the
column-absent patterns. And "missing with no code" can arrive two ways — a
real count below 150, or an error whose message matched the column-absent
regex while carrying no code. **You cannot tell which from the current
output, which is exactly the bug.**

**Why I could not finish it:** the sandbox proxy answers 403 to CONNECT for
both `www.mongolpotential.com` and `*.supabase.co`, so the PostgREST call
cannot be reproduced from a Claude cloud session. The only view of the probe
is its own verdict. Hence the owner's item 3: make it report observed
evidence (the count and the raw PostgREST `message`) in `details` for any
non-`applied` result, **without touching the pass/fail logic yet**. That is
~10 lines in `app/api/health/flags/route.ts` plus a wider `details` type, and
the answer arrives in the next response from the endpoint. That work was NOT
started.

### 4. Migration 011 — verified applied, and the false alarm

**Applied 17 Aug. Do not re-apply.** `skills` = 184, `skill_prerequisites`
= 367.

I verified past the row counts because the SQL had to be retyped through an
MCP tool parameter — there is no psql or connection string in this sandbox —
and a mistyped `strength` or `exam_weight` seeds a subtly wrong graph while
the counts still read 184/367. Both tables were hashed against the file:

```
md5(skill ids, ordered)         332919b9f7c0bee9c5875547aba1eddc   file == db
md5(edge pairs, ordered)        58cdc43a41defba848a7fd37346aff2a   file == db
sum(exam_weight)  99.8983   sum(strength) 316.4
sum(typical_difficulty) 505 sum(display_order) 5257                 all match
```

plus 0 dangling endpoints, 0 self-edges, 0 rows off `hub='eysh'`, `name_mn`
NULL on all 184 (Phase 3 writes it), and the file's own post-conditions ran
without raising. `skill_state` was empty before and after, so the
`ON DELETE CASCADE` the file warns about was never in play.

**THE SORT-ORDER FALSE ALARM — read this before you panic at a hash
mismatch.** My first edge-hash comparison did not match, and it looked like
a transcription error in 367 rows. It was not. It was my own hashing
convention:

- Python sorted the **concatenated strings** `"skill>requires"`.
- Postgres sorted by the **tuple** `(skill_id, requires_id)`.

`-` (0x2D) sorts before `>` (0x3E), so wherever one skill id is a prefix of
another — `cone` vs `cone-x`, and there are several — the two orders diverge
and produce different digests over identical data. Re-sorted by tuple, the
file reproduces `58cdc43a…` exactly. **The data was never wrong.** If you
hash-compare anything against Postgres, match its collation and its ORDER BY
before concluding the data differs.

### 5. Migrations: applied, not applied, and cancelled

Files are `000`–`017`, no duplicates. The **ledger stores the migration
*name*, not the file number**, so read it accordingly.

**A trap I created and could not close.** `011_seed_esh_graph.sql` is
applied and verified, but it is **NOT in `supabase_migrations.schema_migrations`**
— I applied it with `execute_sql`, not `apply_migration`, so no ledger row
was written. Combined with FLAG-010's false `missing`, that means **both**
mechanical checks for 011 currently read as "never ran", and both are wrong.
Verify it by row count (`select count(*) from skills` → 184), never by the
ledger or the health endpoint, until FLAG-010 is fixed. Consider writing the
ledger row.

**Written but never applied:** `012_profiles_column_grants.sql` (Security's
file). It is redundant — my `profiles_update_lockdown` (now `016`) did the
same job harder. Production has **no** UPDATE grant on `profiles` at any
column; that file would grant three. Live consequence worth knowing:
`profiles_update_own` still exists as a **policy with no grant behind it** —
inert today, and exactly the shape CLAUDE.md rule 4 warns about if someone
re-grants later. Security flagged it; the delete-or-keep call is Design's.

**Numbering:** mine were renumbered `012`/`013` → **`016`/`017`** when
Security's renumbered `012`–`015` landed on main first, per
`supabase/migrations/NUMBERING.md` ("the late branch renames"). Both were
already applied to production under their *names*, so the rename changed the
repo's record only — the database needed nothing.

**CANCELLED — the drop of `topics` and `problems`.** Per the owner these are
load-bearing: the legacy course pages run on them until each door is
migrated. The drop still sits **commented out** at the bottom of
`010_skill_graph.sql` (lines ~203–212) with a row-count guard. I never ran
it. **Delete those lines outright** so nobody uncomments them — I was closed
before I could. Last verified counts (2026-08-14, by runtime `count(*)`
inside 010's guard, and restated by the owner today): `topics`=13,
`problems`=20, `streaks`=2. I did **not** re-verify this session — my query
was interrupted — so re-count before trusting the numbers, per rule 6. Note
`list_tables` reported 0 rows for all three and was wrong about all three.

**Others should know:**

- **The navigation cut is reversed and no door is to be removed.** IB, AP,
  the standalone topic courses and the grade courses all stay in navigation
  and get upgraded over time. Khas's explicit call; it overrides Stream A
  items 2, 3 and 5 in `04-WORK-ORDERS.md`, which are withdrawn. A door leaves
  navigation only on Khas's explicit call. `/practice/session` is the sole
  exception and is excluded by a dropped schema, not by a product decision.
- **The health endpoint's output shape is ABOUT to change and has not yet.**
  The owner asked for `/api/health/flags` to include the observed row count
  and the raw PostgREST message in `details` for any non-`applied` result.
  That work was not started. When it lands, anything parsing `details` as a
  `Record<string, string>` of codes will see longer, human-readable strings —
  `scripts/verify-flags.mjs` reads `checks`, not `details`, so it is safe, but
  check anything else that consumes it.
- `topics` and `problems` are **not** to be dropped. Any pending drop is
  cancelled.

### Things you will not find in a file

Not written down anywhere else. Several of these will actively mislead you.

1. **There is no new `CLAUDE.md`.** I was told a three-stream version (Pricing
   having left Claude Code) was at the repo root. It is not — not in the
   working tree, not on any branch. The only `CLAUDE.md` is the four-chat one
   I wrote in `550fd74`; it says "Four Claude Code chats" and never mentions
   Pricing. Ask the owner to paste or commit the new one. Until then the
   ownership table you are reading is out of date by one stream.
2. **`/docs/plan/` is in no branch of this repository.** Not
   `01-ARCHITECTURE.md`, not `04-WORK-ORDERS.md`. Checked against every
   remote branch, twice, on 16 and 17 Aug. The owner holds them and pastes
   extracts. **You cannot "update `01-ARCHITECTURE.md`" by editing a file** —
   there is nothing to edit. Do not fabricate the document to have something
   to edit; the seven rules in `CLAUDE.md` § Product rules are the repo's
   working copy, and that is the honest place to apply rule changes. Hand the
   owner the verbatim replacement text for their held copy.
3. **The owner's rule 4 and rule 7 rewrites were given to me and never
   applied anywhere.** They are, verbatim, for whoever lands them:
   *Rule 4 — No new top-level route. The route budget is fixed at what exists
   today. Existing routes stay. Adding one requires Khas's explicit call.*
   *Rule 7 — Every door declares which brain it is on. Nothing is promoted
   until it is graph-backed. Two tiers: graph-backed (attached to skill_id,
   writes skill_state; eligible for Today, recommendations, prediction,
   parent reports) and legacy (still on the old free-text model; stays
   visible, stays honest, never recommended by the engine, never counted as
   evidence). Half-built things are legacy, not hidden. A door leaves
   navigation only on Khas's explicit call.*
   Also owed: the doc's "Dropped — all zero rows" section is **wrong and
   dangerous** — `topics`=13, `problems`=20, `streaks`=2 are live and kept;
   as written it reads as an instruction to delete real data. And rule 1
   needs amending to: orphan content is **listed, never deleted**.
   `CLAUDE.md` § Product rules still shows the OLD rules 4 and 7, and its
   "Not building, by decision" line still says "IB/AP (until 2027)", which
   now contradicts the owner's call. All three need updating.
4. **Verification cannot reach production from this sandbox.** The proxy
   answers 403 to CONNECT for `www.mongolpotential.com` *and* `*.supabase.co`.
   `npm run verify:flags -- https://...` will report a bogus HTTP 403. Fetch
   prod through the Vercel MCP (`web_fetch_vercel_url`) and read the JSON.
5. **Tailwind purges anything outside its `content` globs, silently.**
   `lib/` was missing, so every class in `lib/upgrade-modal-context.tsx` was
   stripped — the upgrade modal shipped with no max-width, no z-index and an
   unreachable close button, and nothing errored. `lib/` is in the globs now;
   if you add a component outside `app/` or `components/`, check.
6. **`currentColor` does not resolve through `<img src="...svg">`.** An
   `<img>`-loaded SVG is its own document. The logo mark and lockup are
   inlined as React components (`LogoMark`, `LogoLockup`) for exactly this
   reason; loaded via `<img>` the wordmark renders black and vanishes on the
   dark theme. Both are GENERATED by `scripts/gen-logo-assets.py` from
   `assets/brand/lockup-master.png` — edit the master and re-run, never the
   component. Then re-run `scripts/gen-pwa-icons.py`.
7. **The Resources dropdown opens on hover; a click TOGGLES it shut.**
   Playwright's `.click()` hovers first, so it opens then immediately closes
   the menu and your test sees an empty dropdown. Use `.hover()`. This cost
   me a false failure.
8. **`npm run verify:links` does not finish inside a sane timeout** — it
   crawls ~2000 pages and blew a 4-minute bound. `npm run verify:ptest` with
   no args is a **usage error, not a failure**; it needs `--all-esh`.
9. **The favicon is the full figure and is mush below ~20px** — measured at
   16/32/64px, the eyes merge into the head stroke and the legs close up. The
   designer owes a head-only drawing; drop it at
   `assets/brand/favicon-master.png` and point the favicon block at it.
10. **`main` and `claude/problem-bank-premium-design-osj7de` are identical.**
    The branch is not carrying anything main lacks. Continue on either.

## 2026-08-17 05:05 UTC

**Did:** Applied `011_seed_esh_graph.sql` to production — 184 ЭЕШ skills and
367 prerequisite edges.

**Landed where:** applied to production. (Code from this session is already
on main as `a532ae4`.)

**Blocked on:** nothing. Phase 1 is unblocked — the graph is in the database.

**Others should know:**
- **The ЭЕШ graph is live.** `skills`=184, `skill_prerequisites`=367, 0
  dangling endpoints, 0 self-edges, `name_mn` NULL on every row (Phase 3
  writes it). Verified by row count AND by content hash against the file,
  because the SQL had to be retyped through a tool parameter and a mistyped
  weight would seed a wrong graph in silence. `skill_state` was empty before
  and after, so no learner state was ever at risk.
- **Do not trust `/api/health/flags` on 011 right now.** It still answers
  `missing` for a table holding 184 rows — a false negative, raised as
  FLAG-010 with everything already ruled out on the database side (counts
  under every role, RLS, grants, bypassrls, schema-cache reload, no
  duplicate table, right sentinel in the deployed build). If you read that
  endpoint and conclude the seed never ran, you will re-apply a migration
  that is already applied. The re-run is safe (upserts, never deletes) but
  the conclusion is wrong. `migration_008_student_profiles` reports
  `unknown` with no code in the same response; both failing probes are on
  `profiles`/`skills` and both passing ones are on `attempts` — that split
  is the lead worth pulling.
- `015_attempts_server_delete.sql` is unblocked: its stated precondition was
  a live deploy carrying `/api/attempts/erase`, and that shipped in
  `a532ae4`.

## 2026-08-17 04:25 UTC

**Did:** New logo shipped — the designer's lockup replaces the old mascot
(which had "MP ACADEMY" baked into the artwork); every asset is now derived
from one master by `scripts/gen-logo-assets.py`, the mark and wordmark are
traced SVG so they follow `--accent`/`--fg` in both themes, and the site has
a real favicon for the first time. Renumbered my two lockdown migrations to
016/017. Merged main twice and deployed.

**Landed where:** merged to main and deployed to production.

**Blocked on:** nothing.

**Others should know:**
- **The 012/013 collision is cleared.** My `012_profiles_update_lockdown`
  and `013_client_write_lockdown` are now **016** and **017**, per
  NUMBERING.md's "the late branch renames" rule — the security audit's
  012–015 were on main first. Both were applied to production long ago and
  are in the ledger under their *names*, so the database needed nothing.
  Migrations are now a clean 000–017 with no duplicates.
- **`scripts/verify-account-delete-inventory.test.ts` had a false positive**
  (security stream's file — flagging it here rather than editing quietly).
  Its `ALTER TABLE … ADD CONSTRAINT` regex used an unbounded `[\s\S]*?`,
  which walked past the statement end to the next `profiles(id)` anywhere in
  the corpus. The moment `010_skill_graph.sql` merged to main it reported
  `skills` — the content graph, no user column — as user-scoped, and the
  "fix" it demanded was adding a content table to the deletion inventory.
  Bounded to `[^;]*?`. `skill_state` and the other 12 real user tables are
  still found. Worth a look if you have other regexes shaped like that.
- **`scripts/verify-flags.mjs` was not gating 010 or 011.** Its HEALTHY map
  is a hand-kept mirror of the one in `lib/flags.ts` and had drifted, so the
  two newest migrations were reported by the endpoint and checked by nothing.
  Both added.
- If you add a component outside `app/` or `components/`, remember Tailwind's
  content globs — `lib/` was missing and every class in it was silently
  purged.

## 2026-08-16 09:43 UTC

**Did:** Problem bank made Premium-only and answer-first (commit, then check
— no solution shown before an answer); bank results feed the ratings card as
credit-only evidence, so a wrong answer never deducts; Phase 0 landed
(per-question timing wired, IB/AP/topic courses and grades 6–7 unpublished,
nav collapsed to ЭЕШ · SAT · Tutoring · About, five-tab contract enforced);
applied migrations `010_skill_graph`, `012_profiles_update_lockdown`,
`013_client_write_lockdown`; fixed the upgrade modal, which could not be
scrolled or closed.

**Landed where:** branch `claude/problem-bank-premium-design-osj7de`; the
bank + Phase 0 work merged to main via PR #4; `010`, `012`, `013` applied to
production and present in the ledger.

**Blocked on:** nothing. `011_seed_esh_graph.sql` has landed on main, so
item 5 (folding grades 8–12 into the ЭЕШ hub as foundation skills) is
unblocked and is the next piece of work.

**Others should know:**
- **Migration numbers 012 and 013 are double-booked.** This branch carries
  `012_profiles_update_lockdown.sql` and `013_client_write_lockdown.sql`;
  `origin/main` carries the security audit's `012_profiles_column_grants.sql`
  and `013_deletion_cascade.sql`. Both sets are already applied to
  production — the database is fine, the filenames are not. Mine get
  renumbered before this branch merges. Do not take 016 or 017.
- The `profiles` free-premium hole is closed: a student could set their own
  `subscription_status`. RLS gated the row, never the column; the fix was to
  revoke the privilege, not to write a better policy. Same shape was found
  and closed on `daily_problem_counts` (the AI quota, real money) and
  `streaks`. TRUNCATE is revoked from `anon` and `authenticated`
  schema-wide.
- `skill_state` is server-write only by construction: RLS on, select-own
  policy, no write policy at all.
- Tailwind's `content` globs now include `lib/`. They did not, and every
  Tailwind class in `lib/upgrade-modal-context.tsx` was silently purged. If
  you add a component outside `app/` or `components/`, check the globs.
- Known and unresolved, owner's call: `attempts` DELETE-own lets a student
  erase wrong answers (privacy right vs mastery integrity).
