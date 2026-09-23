# Status — Build

The single code-writing chat. Owns routes, nav, pages, app logic, migrations,
schema, health probes, `data/`, `scripts/`, the skill graph and items.
Security reviews and gates but never applies.

Supersedes `memory/status/design-and-structure.md` and
`memory/status/content.md`, both of which stay in the repo as history. Write
**only this file**; read all of them. Newest entry at the top.

Design's closing handover (436 lines, `676c4c2`) is the reference document for
routes, the FLAG-010 diagnosis and the 011 verification. Read it before
touching any of those; it is not summarised here.

---

## 2026-09-23 — mode: content

**Did:** Mongolian rewrite, ЭШ-first queue, as Markdown drafts in
`memory/mn-drafts/` (rewrite, not translation, per `docs/MONGOLIAN.md`).
52 drafts now, 45 of them feeding the ЭШ course. ЭШ coverage, re-measured
against `lib/esh-course.ts`: **49 of 72 units, 10 of 14 topics**;
Комбинаторик, Магадлал and Өгөгдлийн шинжилгээ closed this week, Функц ба
график at unit 4 of 7. Every draft passes `scripts/i18n/mn_draft_check.py`
and every numeric claim was re-computed. Open questions for Khas are in
`memory/mn-review-pile.md`, the only place they live.

**Landed where:** branch `claude/grade-6-math-verify-xe1tak` (last commit
`c131ade`). Drafts only: nothing applied to `data/genmath/*-mn`, nothing
merged, nothing deployed, no migrations.

**Blocked on:** Khas's review of the pile. The rulings that gate the most
text: 6aa (coin and dice vocabulary, «орхих» / «тоотой тал» vs the drafts'
«шидэх» / «зураас»), 6ab (the ЭШ divides by $n$, our SD lesson teaches
$n - 1$), 6ac (dot plot vs scatter plot naming), 6ae (*bias* = «хазайлт»
beside «стандарт хазайлт»), 6af (open/closed dots).

**Others should know:** ship-mode findings, written down and not done:

- **6z** — six live ЭШ practice solutions in `data/questions/` defer to "the
  corpus" instead of solving; three teach a wrong method or wrong data.
- **6ad** — `prob-stats/distributions-and-position` lesson 6 concept 3 says
  «памятlets» in live English: the only mixed-script word in 212 files.
- **6j, 6af** — ЭШ units claiming ministry codes they do not teach (10.12в
  core; 12.3е elective).
- **6h** — 20–21 leaked authoring notes, most in question *statements*; one
  (`dp-l2-t1`) with a wrong solution too.
- Nothing here touches auth, RLS or student data.

---

## 2026-09-04 04:20 UTC — mode: ship

**Did:** Visual polish pass across the whole site on the owner's request
("upgrade the design, don't change it entirely, premium like big tech /
new startups"). Structure, routes, nav and copy untouched; only the visual
layer. One `.btn` system (top-lit gradient primary, lift/press on every
variant), top-lit `.card-edit` with hover lift, depth tokens per theme
(`--hi`, `--shadow-*`, `--glow`, `--glass`, `--card-grad`), dot-grid + orb
hero atmosphere, `data-reveal` scroll reveal (fails open, reduced-motion
off), glass header pill with segmented theme/lang control, footer with
accent hairline. Hubs pick it up through HubKit/HubTabs. Fixed six
hardcoded rgba colours that broke the light theme (auth error banners,
/math gold chip, badge-warn/danger, card-glass). Removed dead legacy CSS
utilities (zero call sites).

**Landed where:** branch `claude/website-design-upgrade-174y3l`, commit
`4dc5c60`. **Not merged, not deployed** — owner asked to see a preview
first. Vercel preview:
`imathhub-git-claude-web-eeea05-khas-ochir-bayarjargals-projects.vercel.app`
(SSO-protected; owner must be logged into Vercel to view).

**Blocked on:** owner review of the preview. Merge to main only on "deploy".

**Others should know:**

- `.btn-primary` used to be defined twice — once in `@layer components`
  (px-6 py-3 rounded-xl, from the old design) and once unlayered. The
  layered one is gone; anything that looked like a big pill button was
  getting its size from the unlayered `.btn` anyway.
- `a.card-edit:hover` and `button.card-edit:hover` now lift and take an
  accent border in CSS. `app/math/page.tsx`'s `cardHover` inline handlers
  are a no-op object left in place so the call sites did not change.
- New primitives available to anyone: `.card-accent`, `.icon-tile`,
  `.rule-fade`, `.rule-accent`, `.bg-dots`, `.orb`, `.glass`,
  `.display-grad`, `.link-draw`, `.btn-lg`, `.side-link`, and the
  `data-reveal` attribute (optional `--reveal-delay`).
- Verified: tsc clean, 879 vitest green, `next build` green, Playwright
  screenshots of home/about/tutoring/contact/esh/sat/math/sign-in in both
  themes and mobile.

---

## 2026-08-26 08:45 UTC — mode: content

**Did:** Opened the Mongolian programme. Committed `docs/MONGOLIAN.md` (Khas's
standing programme — read it with `CLAUDE.md` at the start of every session
from now on). Started group 0, the vocabulary: swept the corpus to 622 maths
terms plus 37 operational terms the title-driven sweep had missed, parsed all
184 ЭШ skill names out of `011_seed_esh_graph.sql` (every `name_mn` NULL,
strands 76/60/23/20/5 matching Khas's figures), and built
`scripts/i18n/mn_ground.py` to check every provenance label against the source
it claims.

**Landed where:** branch `claude/grade-6-math-verify-xe1tak` —
`7bf6dba` (programme), `b5e28d6` (grounding checker), `c126dea` (ЭШ bank as
evidence). Nothing deployed; nothing Mongolian is wired.

**Blocked on:** Khas — group 0 ends in a hard stop for glossary approval, and
nothing downstream can start until the terms are locked. Group 2 (voice) and
group 3 (lesson prose) are blocked by design.

**Others should know:**

- **The mode rule is dropped.** Khas dropped it explicitly on 26 Aug. This
  entry is marked `content` for legibility, not because the rule still binds.

- **The grounding checker's failure mode is grounding too much, and it is
  silent.** Its first version matched stems as raw substrings and reported all
  100 glossary terms as present in the grade 10–12 ministry standard —
  including "tip" and "tree diagram", which are primary-school concepts. It
  passed a smoke test at the time. `--selftest` now asserts in both directions
  (out-of-scope terms absent, core terms present) and is wired into
  `npx vitest run` via `scripts/verify-mn-ground.test.ts`. If you touch the
  matcher, that test is the one that matters.

- **`data/questions/` is the best Mongolian evidence on the site and was being
  ignored.** 20 real ЭШ past papers, 4,543 Mongolian strings, ~449k characters,
  Mongolian-FIRST rather than translated. It is now part of the shipped corpus
  the checker reads. Anyone reasoning about Mongolian terminology should reach
  for it before the translated mirrors.

- **The 25 shipped MN mirrors can be walked in lockstep with their English.**
  `mn_walk.py`'s `pure_math()` skips any string with no Latin letters, which on
  the Mongolian side is every translated string — so a naive parallel walk
  desyncs. With a script-symmetric predicate all 25 align exactly, yielding
  14,003 EN→MN string pairs. That is reusable evidence, not a one-off.

- **58 of the 184 skill names are imperative clauses** ("Solve a quadratic by
  factoring"). They are descriptive, not persuasive, so they are not voice —
  but it does raise a live style question for Khas: should skill labels follow
  the ministry's verbal-noun pattern («…-ыг мэдэх, хэрэглэх») or be pure noun
  phrases? It affects all 184 and belongs in the group-0 question list.

- **Group 0 is complete and awaiting approval.** 659 terms (622 corpus + 37
  operational) and all 184 ЭШ skill names, in `data/i18n/`. Question list in
  `memory/mn-group0-questions.md`. 508 rows are quoted verbatim from a named
  source; 99 are genuinely novel; 171 are low confidence.

- **Eleven terminology bugs are live in shipped Mongolian**, found while
  checking proposals against what the site already says. Section A of the
  question list. They are independent of the approval decision: absolute value
  ships three ways, "reflect" uses a word absent from the ministry standard
  across a whole unit, and "spread" and "distribution" are the same word inside
  one sentence.

- **The glossary contradicts the ministry on "tree diagram".** The standard
  covers it three times (10.15б, 11.13д, 12.15а) and calls it «модны схем»;
  `mn-translation`'s glossary says «мод диаграм». Same shape as the
  тэнцэтгэл бус/биш correction. It surfaced only after the grounding checker
  learned to require phrase adjacency — before that, «модны» in one objective
  and «диаграмм» in another were being stitched into a false match.

- **The rewrite gate exists now: `scripts/i18n/mn_skeleton.py`.** It was the
  true blocker for group 3 — `mn_apply.py` asserts string parity, so the first
  rewritten topic would have failed it for being correct. Structure is
  enforced (lesson count/slugs/order, problem ids, step kind sequences,
  option counts, correctIndex, check[] presence, CYR-IN-MATH); prose never is.
  All 25 shipped mirrors pass. `npm run verify:mn-skeleton`.

- **Single-asterisk emphasis is a live display bug in BOTH languages.**
  MathText renders `**bold**` only (`MathText.tsx:24`), so a single `*` reaches
  the reader literally — **1,032 English strings** against 36 Mongolian,
  including IB markscheme annotations like `*(A1 A1)*`. It is advisory in the
  gate rather than fatal, because failing on a pre-existing English habit would
  make it red from birth. Nobody has recorded this before.

- **There are two registers in production and nobody declared the line.**
  Grade 7 is pure «чи» (0 formal). Grade 8 is «та»-dominant in its teaching
  prose (40 strings). The app UI is formal throughout (73 across 31 files).
  Grade 6's 55 formal hits are 47 instances of ONE completion template plus 8
  prose strings — not a re-register. May well be deliberate; it is not written
  down. `memory/mn-group1-audits.md` §1.

- **Runtime string composition: 53 sites, 2 certain bugs.** `lib/ratings.ts`
  builds `${u.title}-ийг эзэмших` where the accusative must agree with the
  title's final vowel and 215 titles can reach it; the chrome batch's
  `Factors of `/`Multiples of ` are the same class. 46 sites are safe (number +
  uninflected noun). Two need a Mongolian-speaker call, not a code one.

- **Nine chrome strings moved to Khas's voice pile** and are marked
  `src: "VOICE"` with `mn: ""` in `lib/i18n/chrome.ts`. My earlier Mongolian
  for them is withdrawn. 82 labels stay.

- **Judge long labels differently from short terms.** A six-word skill name is
  COMPOSED from source vocabulary, not quoted from it. Without that split, 99
  legitimate compositions read as overclaims. Anyone extending
  `mn_ground.py` should keep that distinction.

## 2026-08-17 08:30 UTC — mode: ship

**Did:** Finished `CLAUDE.md` as the master (two-chat ownership, one mode per
session). Removed the `/practice` landing and retargeted the home page's four
primary CTAs, which all pointed at it. Moved contact details to Ulaanbaatar.
Found and fixed BOTH lead forms silently discarding submissions. Wrote
migration 018 for the contact backlog — **written, not applied**.

**Landed where:** merged to main and deployed. Production is `29925f0`.
Migration 018 is on main and **not applied to production** — FLAG-011.

**Blocked on:** **MCP approval.** `apply_migration`, `execute_sql` and the
Vercel URL fetch all return `MCP tool call requires approval`, which arrives
as a tool error, not a prompt — this session is non-interactive, so nothing
can reach the owner to click. I own migrations now and still cannot apply
one. Everything else this session was unblocked; the next database task is
not.

**Others should know:**

- **SECURITY — your deletion-inventory gate caught a real mistake of mine,
  and I want that on the record.** I gave `contact_messages.user_id`
  `ON DELETE SET NULL`, reasoning that erasing an account should not destroy
  a conversation. Wrong: the row holds the sender's name, email and message
  body, so nulling the link would have unlinked the account and left every
  piece of personal data behind — an erase that erases nothing anyone cares
  about. `verify-account-delete-inventory` rejected it before it shipped. It
  is `CASCADE` now, matching `premium_waitlist`, and registered in
  `SERVER_USER_TABLES`. The table is RLS-on with no policy AND grants revoked
  from `anon`/`authenticated`, both locks per the rule, asserted inside the
  migration's own post-conditions.

- **TWO FORMS WERE LOSING LEADS, in the same shape, and neither could be
  seen from outside.** The contact form's submit handler was
  `await new Promise(r => setTimeout(r, 1000))` followed by the success
  screen — no request, no storage. Every message ever sent through that page
  was discarded while its sender was thanked. And `/api/waitlist` ran its
  upsert, discarded the result, and returned `success: true` unconditionally,
  so a failed Premium purchase request was indistinguishable from a
  successful one. **That is why "premium_waitlist has 2 rows since May"
  cannot be read either way** — the modal does call the API and the table is
  correct, so the row count alone cannot separate "nobody asked" from "every
  request failed". Both now check and surface their errors.

- **The `events` table is the outstanding cross-check.**
  `select name, count(*) from events where name in ('purchase_request',
  'upgrade_modal_opened') and created_at > '2026-05-31' group by name;`
  Events with no matching waitlist rows would prove requests were lost.

- **Contact details are now split on purpose, and it will look like a bug.**
  `+976 8862 7927` leads in the footer and on the contact page — the
  Ulaanbaatar centre is the local business and Google cross-checks that
  number against the Business Profile. `/tutoring` keeps
  `+1 (415) 981-8165` because 1-on-1 lessons are the online business sold
  across timezones. Two numbers, deliberately, with a comment on the constant
  saying so. Do not "fix" the tutoring page to match the footer.

- **`hello@mongolpotential.com` replaced `imathhub@gmail.com`** in its three
  places (contact page, footer ×2). Privacy and terms already used the new
  address; there is no structured data or email template anywhere holding a
  stale one. `khasochir@uni.minerva.edu` and the WhatsApp number on
  `/tutoring` are untouched at the owner's instruction.

- **The Mongolian SLA string was deliberately left without a timezone.**
  Adding one is Mongolian copy, and Mongolian copy is written by a human
  teacher, never translated by me. Queued for that pass alongside the
  diagnostic rewrite.

- **FLAG-010's filter hypothesis was wrong, and the misleading field was
  mine.** `details.filter` printed `hub=eysh`, which is not a PostgREST
  filter — a reader took it for the query and concluded the syntax was the
  root cause. The query was always right: `.eq("hub","eysh")` serialises to
  `hub=eq.eysh`, proved by building the request and reading its URL. The
  field now prints what goes on the wire. **FLAG-010 still has no root
  cause** — the endpoint read that would give it one is blocked with
  everything else.

- **The Vercel deployment API lies about `state`.** It reported `BUILDING`
  for 30–45 minutes on three deploys today that had each finished in under
  four. I called one of them stalled and had to retract it. Do not diagnose a
  deploy from `state` alone; `lambdaRuntimeStats` appearing in the response
  is the reliable tell that it is nearly done, and the alias list flipping to
  `www.mongolpotential.com` is proof it landed.

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

- **011 is applied but NOT in the migration ledger, and that is a second
  false negative.** From Design's handover: it was applied with `execute_sql`
  rather than `apply_migration`, so no row was written to
  `supabase_migrations.schema_migrations`. Combined with FLAG-010, **both**
  mechanical checks for 011 currently read "never ran" and both are wrong —
  which is precisely the shape `CLAUDE.md` rule 1 warns about ("verify by row
  count or the ledger, never by the file existing"), except here the ledger is
  the thing lying. Writing that ledger row is mine to do and is blocked on
  database access. Until it exists, the only trustworthy evidence that 011 ran
  is Design's content hash: `md5(skill ids) = 332919b9…`,
  `md5(edge pairs) = 58cdc43a…`, both file-equals-db.

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

- Nav state as found, before I changed anything: **nothing was left to undo**,
  and I reached that independently before reading Design's handover — the two
  reports agree route for route, including the no-sitemap finding.
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
