---
name: release-deploy
description: >
  Release management manual for Mongol Potential — how production deploys
  work (branch → main → Vercel), the pre-deploy checklist, deploy
  verification, rollback, and the "deploy only on explicit request" rule.
  Read before ANY push to main, when asked to "deploy", when a deploy looks
  unhealthy, or when production needs a rollback.
---

# Release & Deploy — Operating Manual

Production is www.mongolpotential.com, auto-deployed by Vercel from
`main` (project `imathhub`, id `prj_9MqKLH1aOmKCZVofkKd7IAMsnkGq`, team
`team_8bMeaxYVWnyZaWq7iEoPMwbA`). Real students and parents are on it —
a broken deploy is a broken lesson in someone's evening study session.

## Rule zero

**Deploy ONLY when the owner explicitly says so** ("deploy", "push to
main", "ship it"). "The feature is done" is not a deploy trigger.
Day-to-day work lands on the working branch
(`claude/grade-6-math-verify-xe1tak` in the current era) and waits.

## The deploy procedure

1. **Pre-flight (all green or no deploy):**
   - Full gate per `qa-verification`: `verify:genmath`, `verify:ptest`,
     `npx tsc --noEmit`, `npx vitest run`, `npm run build`.
   - Playwright spot-walk of routes affected since last deploy (both
     languages for mirrored content).
   - `git log origin/main..HEAD --oneline` — read every commit that will
     ship; confirm nothing half-finished or experimental rides along.
     If something must not ship, STOP and cherry-pick a release branch
     instead of pushing the working branch wholesale.
   - No secrets/PII in the outgoing diff (`cybersecurity` sweep if auth
     or scripts changed).
2. **Ship:** `git push origin <working-branch>:main`
   (with retry: 2s/4s/8s/16s backoff on network failure).
3. **Watch it land:** poll the Vercel deployment (MCP:
   `mcp__Vercel__get_deployment` / `list_deployments`) until state is
   `READY`. `ERROR` → read `get_deployment_build_logs`, fix forward or
   roll back — never leave it red and walk away.
4. **Verify production:** fetch the live site via
   `mcp__Vercel__web_fetch_vercel_url` (direct fetches 403 through the
   proxy) — check the homepage renders and one changed route serves the
   new content. Check `get_runtime_errors` for fresh exceptions.
5. **Report:** tell the owner what shipped (commit range, user-visible
   changes) and the verification evidence.

## Rollback

Vercel keeps previous deployments warm:
- Fastest: re-push the last-good commit to main
  (`git push origin <good-sha>:main --force-with-lease`) — Vercel
  rebuilds and promotes it. Note it in the session log with the reason.
- Alternative: promote the previous READY deployment from the Vercel
  dashboard (owner action if MCP promote isn't available).
- After rollback: reproduce the failure on the branch, fix, full
  pre-flight, redeploy. Never "quick-fix" directly against main.

## Database changes (Supabase)

Migrations under `supabase/migrations/` do NOT auto-apply on deploy —
the owner applies them in the Supabase dashboard/CLI. Deploys that
depend on un-applied migrations must be sequenced: migration applied
first, verified (table exists), THEN code deploy. Flag this dependency
loudly in the deploy report (current standing example: migration 008
student_profiles is committed but not yet applied — student-account
features are dormant until it is; see `student-ops`).

## Cadence and hygiene

- Prefer small, frequent deploys of verified increments over big-bang
  releases — every historical deploy here was a reviewed content batch.
- Deploy during the owner's waking hours when feasible; a broken evening
  deploy in Ulaanbaatar time hits peak study hours.
- After deploy, the working branch and main are identical — the next
  work cycle continues on the working branch.
- Keep the deploy report format stable:
  `Deployed <sha-range> → READY (<deploy-id>) · prod verified: <routes> ·
  gates: <numbers>`.
