# Session journal

Reverse-chronological log of major work sessions. Each entry captures the arc — what shipped, what was decided, what surfaced, what's deferred — in tighter form than commit messages alone. PHASES.md holds the queue; this holds the narrative.

## 2026-04-26 — Pre-launch hardening, day 1

**Shipped:**
- **Prod Supabase service role key rotation** via the new `sb_publishable_*` / `sb_secret_*` system. Zero-downtime path: new keys generated, Vercel env updated, prod verified, legacy JWT-based keys disabled. Leaked legacy service_role key from earlier chat history is now invalid.
- **Profiles auto-create trigger** end-to-end on staging + prod (commit `aaf6d6a`). Closes the FK 23503 gap for users provisioned outside the sign-up form (Supabase dashboard "Add User", future OAuth, admin scripts). Migration 005 = trigger + handle_new_user() function (SECURITY DEFINER, locked search_path) + idempotent backfill. Register route changed from INSERT→UPDATE since the trigger now creates the row first inside the same transaction. 4/4 staging smoke pass: dashboard add-user, attempts insert (no FK 23503), form sign-up overwrites placeholder, anon migration preserves 3 attempts with original timestamps. Prod cutover green (timed migration apply against Vercel-Ready window).

**Verified:**
- **RTR on prod**: Refresh Token Rotation toggle ON, reuse interval 10s, detect-and-revoke compromised tokens enabled.

**Designed (ready for implementation tomorrow):**
- **P1 sign-up email confirmation contract bug.** Six design decisions locked + three bonus concerns captured (see PHASES.md P1 entry). Implementation tomorrow starts with a plan outline (file changes, smoke test sequence, staging-first Site URL config order) before any code.

**Deferred:**
- **Supabase Pro upgrade** ($25/mo). Free-tier carried risks documented explicitly (zero backups = survival risk; 3/hr signup rate limit = growth risk). Hard launch trigger: before public launch announcement OR first paying user, whichever comes first.
- **Manual weekly pg_dump backup setup**. Workflow friction too high (~45 min wrestling with `nano` + URI handling) for a non-daily-terminal user. Pro upgrade is the production backup plan; the script at `scripts/backup-prod.sh` stays in the repo for opportunistic snapshots before risky migrations.

**Surfaced during this session:**
- **P1**: sign-up route/client contract bug (designed today; implementing tomorrow)
- **P2**: dashboard greeting truncation — `display_name = "Anon Migrate Test"` renders "Сайн уу, Anon" (probably `display_name.split(' ')[0]` somewhere)
- **P2**: dashboard renders "ON THIS DEVICE • ACCOUNT SYNC COMING SOON" anon-mode messaging despite an authed user with synced attempts

**Vercel deploys this session:** `378f86a` (Suspense fix), `d9bdf1c` (Step 2.5 logout cleanup), `aaf6d6a` (profiles trigger), `10fb784` (PHASES.md update post-trigger). All green.

**Tomorrow's pickup**: P1 implementation. Plan outline → 5 min review → code.
