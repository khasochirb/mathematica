# Mongol Potential — working agreement

Four Claude Code chats work on this repo in parallel. You are one of them.
You cannot see the others' conversations. This file and the status files are
the only shared memory that exists.

## Who owns what

| Chat | Owns | Never touches |
|---|---|---|
| Design and structure | routes, nav, migrations, schema | lesson/problem content |
| Content Creation | `data/`, `scripts/skills/`, the skill graph, items | routes, migrations |
| Website security audit | RLS specs, policy review, audits | applying migrations, app logic |
| QA and release | tests, smoke checks, the deploy gate | features, refactors |

## THE DATABASE RULE

**Only "Design and structure" applies migrations to production.** No
exceptions, no matter how small the change.

Everyone else writes migrations and hands them over. If you are not Design
and structure and you are about to run a migration, stop.

*Why this rule exists: on 15 Aug 2026 two chats applied the same
client-write lockdown eight minutes apart without knowing, and a third
reported a teammate's migration as unexplained database drift.*

> **Supersedes:** `.claude/skills/release-deploy` §Database changes and
> `.claude/skills/ops-flags` both say the *owner* applies migrations by
> hand. That is now out of date — chats apply them via the Supabase MCP,
> and this rule decides which chat. The ops-flag protocol still holds:
> every new migration still raises a flag in `memory/flags.md`.

## Start every session with this

```bash
git checkout main && git pull
cat memory/status/*.md            # what everyone else did
git log --all --oneline -30       # what actually landed
git branch -a                     # where the work lives
```

Then, before writing any migration, check what already exists:

```sql
select version, name from supabase_migrations.schema_migrations
order by version;
```

> Two caveats on that query. The ledger records migrations applied through
> the Supabase MCP; anything pasted into the dashboard SQL editor by hand
> never reaches it, so `000`–`009` are largely absent and their absence is
> not evidence they never ran. And the ledger stores the *name*, not the
> file number — for numbering, `supabase/migrations/NUMBERING.md` is the
> authority and `git ls-tree --name-only origin/main supabase/migrations/`
> is the check.

## End every session with this

Update `memory/status/<your-stream>.md` — write only your own file, read all
of them — then push to main.

**Push the status file only.** On this repo a push to `main` *is* a
production deploy: Vercel auto-deploys from `main`, and
`.claude/skills/company-handbook` golden rule 2 and
`.claude/skills/release-deploy` Rule Zero both say that happens only when
the owner says "deploy". So at session end, commit `memory/status/*.md` to
main on its own; your feature work stays on your branch until the owner
asks for it. Concretely:

```bash
git checkout main && git pull
# edit memory/status/<your-stream>.md
git add memory/status/<your-stream>.md
git commit -m "status: <stream> <date>"
git push -u origin main
git checkout <your-branch>        # work continues here
```

```markdown
## <date> <time>
**Did:** one line each
**Landed where:** branch / merged to main / applied to production
**Blocked on:** who or what, or "nothing"
**Others should know:** anything that changes their work
```

One file per stream, never a shared one: four agents appending to a single
file produces constant merge conflicts; one file each produces none.

## Rules that exist because they were broken

1. **"Merged and deployed" ≠ "migration applied."** Separate steps. Verify
   by row count or the migration ledger, never by the file existing. This
   has been conflated twice.
2. **A migration you didn't write appearing in production is a teammate,
   not drift.** Check the ledger before reporting an anomaly.
3. **Check the ledger before choosing a migration number.** Two chats have
   already picked the same one. `supabase/migrations/NUMBERING.md` records
   that collision and states the check: claim your number against
   `origin/main` when you create the file, and re-check before you merge.
4. **Never leave a policy behind a revoked grant. Drop both.** A policy
   sitting behind a revoked grant silently re-permits when someone
   re-grants later. That is how the free-premium hole was created.
5. **RLS gates rows, never columns.** `USING (auth.uid() = id)` proves you
   own the row — it does not stop you rewriting any column in it. If a
   column must not be client-writable, revoke the privilege.
6. **Row counts, not planner estimates, before anything destructive.**
   `list_tables` has reported 0 rows for tables that held real data.
7. **If the plan docs and the repo disagree, the repo is right.** The docs
   in `/docs/plan/` contain invented route names (`/eysh` does not exist;
   it is `/practice/esh`). Report the conflict — never rename real routes
   to match a document.
8. **Test the exploit, not the patch.** A fix is verified when the attack
   fails, not when the code looks correct.

## Product rules

The full architecture lives in `/docs/plan/01-ARCHITECTURE.md`. The seven
rules there are binding and override local judgement about what would be
cleaner. In brief:

1. Every piece of content attaches to exactly one `skill_id`. **Orphan
   content is listed, never deleted.** (Amended 17 Aug 2026.)
2. Every attempt writes `skill_id`, never a free-text topic name.
3. Every hub has the same five tabs: Plan · Learn · Practice · Tests ·
   Progress.
4. **No new top-level route. The route budget is fixed at what exists
   today. Existing routes stay. Adding one requires Khas's explicit call.**
   (Replaces "no new top-level route without deleting one", 17 Aug 2026.)
5. Max two levels: Hub → Skill.
6. All mastery, recommendation and prediction logic lives in one module and
   reads `skill_state`.
7. **Every door declares which brain it is on. Nothing is promoted until it
   is graph-backed. Two tiers: graph-backed (attached to `skill_id`, writes
   `skill_state`; eligible for Today, recommendations, prediction, parent
   reports) and legacy (still on the old free-text model; stays visible,
   stays honest, never recommended by the engine, never counted as
   evidence). Half-built things are legacy, not hidden. A door leaves
   navigation only on Khas's explicit call.** (Replaces "nothing enters
   navigation until it is attached to the graph and has content",
   17 Aug 2026 — that wording is what justified the Phase 0 cut, now
   reversed.)

> **Rules 4 and 7 were rewritten on 17 Aug 2026, and rule 1 amended.** The
> owner's canonical text lives in `/docs/plan/01-ARCHITECTURE.md`, which is
> **not in this repository** (see the note above). The verbatim replacements
> are reproduced here because this file is the working copy every session
> actually reads. Two corrections the owner still needs to make in their own
> copy of that document:
>
> - Its **"Dropped — all zero rows"** section is wrong and currently reads as
>   an instruction to delete live data. `topics` = 13 rows, `problems` = 20
>   rows, `streaks` = 2 rows. All three are **live and kept**: the legacy
>   course pages run on `topics`/`problems` until each door is migrated.
>   Any pending drop migration for them is **cancelled**.
> - Rule 1's amendment (orphans listed, never removed) needs the same edit
>   there.

> **`/docs/plan/` is not in this repository** — checked on 16 Aug 2026
> against every branch on `origin`, including `main`. The document is held
> by the owner and reaches sessions as pasted extracts. Treat the seven
> rules above as the working copy, and ask the owner for the full text
> rather than hunting for a file that is not there. (Rule 7 above still
> applies to the extracts you are given.)

**Not building, by decision:** school admin accounts, class rosters, bulk
licensing, mobile app, AI tutor chat, IB/AP (until 2027).

## Where the manuals live

This file is the working agreement between the four chats. The operating
manuals — how to actually do each job — are skills in `.claude/skills/`,
auto-discovered by Claude Code:

- `company-handbook` — read first; the org chart, the golden rules, the
  tech-stack orientation, and which manual to open for what.
- `qa-verification` — the verification gate matrix. Nothing ships
  unverified.
- `release-deploy` — deploy procedure, rollback, and "deploy only on
  explicit request".
- `cybersecurity` — auth, secrets, student-data privacy (users are minors).
- `ops-flags` — external dependencies the owner must complete; registry in
  `memory/flags.md`.
- `code-reviewer`, `content-reviewer`, `figures-reviewer` — the review
  rubrics.
- Authoring manuals per hub: `practice-test-authoring`,
  `esh-practice-test`, `sat-practice-test`, `ib-practice-test`,
  `sat-course`, `ib-course`, `skill-taxonomy`, `mn-translation`,
  `figures-creator`, `brand-designer`, `mascot-animator`,
  `performance-analytics`, `student-ops`, `mobile-app`.

Longer-form memory lives in `memory/` (`flags.md` is the ops registry;
the rest is design history). When two manuals disagree, the more specific
one wins for its domain, this file wins on who-does-what, and
`company-handbook` wins on process.
