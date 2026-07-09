---
name: student-ops
description: >
  Student operations manual — provisioning student accounts in batch,
  roster handling, credential delivery to parents, the student_profiles
  personalization model, and account lifecycle (grade change, reset,
  deletion). Read when creating student accounts, when the owner sends a
  roster, when parents report login problems, or when touching
  supabase/migrations/008_student_profiles.sql or scripts/create-students.mjs.
---

# Student Operations — Operating Manual

Students get full-access accounts created FOR them; parents receive the
credentials and the website link. Every student is a minor — the privacy
rules in `cybersecurity` apply to every step here.

## The provisioning system (already built)

- **Migration:** `supabase/migrations/008_student_profiles.sql` —
  `student_profiles` table (user id, full name, grade, focus/notes) with
  RLS so each student reads only their own row.
  **Standing status: committed but NOT yet applied to the live Supabase
  project.** Until the owner applies it, batch provisioning cannot run.
  Check before promising account creation.
- **Batch script:** `scripts/create-students.mjs` — reads a roster JSON,
  creates Supabase auth users (service-role key from env, never
  committed), generates per-student passwords, upserts profiles, writes
  a credentials CSV for the owner. Roster/credential artifacts are
  gitignored (`scripts/my-roster.json`,
  `scripts/student-credentials*.csv`) — verify `git status` shows them
  untracked after every run.
- **Roster format:** `scripts/students-roster.example.json` is the
  template (name, grade, focus, parent contact). The owner fills it;
  never invent student data.
- **Docs:** `scripts/README-student-accounts.md` is the owner-facing
  runbook — keep it in sync with any script change.
- **Personalization:** the app reads the profile (grade, focus) to
  personalize the dashboard/landing per student.

## Running a provisioning batch

1. Preconditions: migration 008 applied (verify the table exists —
   don't assume), service-role key available in env, roster validated
   (every row has name + grade in range 6–12/geometry; emails
   well-formed if provided).
2. Dry-run mode first if the script supports it; otherwise run against
   ONE test student ("Тест Сурагч") and verify login end-to-end (login
   → dashboard shows the right grade) before the full batch.
3. Run the batch; capture the credentials CSV path for the owner.
4. Verify: row count in `student_profiles` matches roster; spot-login
   one real account in a private window; check the personalized
   dashboard renders that student's grade.
5. Hand off: credentials go to the OWNER, who distributes to each parent
   individually. Never post credentials in a group channel, commit them,
   or leave them in the container (session storage is ephemeral, but
   delete the CSV after handoff anyway).

## Credential & password policy

- Generated passwords: readable-random (avoid ambiguous 0/O, l/1),
  unique per student, meant to be CHANGED — but assume parents won't:
  they must still be strong enough to stand alone.
- Password resets: owner-initiated through Supabase dashboard, or a
  re-run of the script's reset mode for a single student. Verify the
  student can log in after reset before closing the request.
- A student sharing a device with siblings is the normal case — no
  "remember me" promises beyond the standard 7/30-day token windows
  (see `cybersecurity`).

## Account lifecycle

- **Grade promotion (new school year):** batch-update `grade` in
  student_profiles; personalization follows automatically. Take a
  roster from the owner, don't guess who advanced.
- **Focus updates:** owner sends per-student notes; update the profile
  row — this drives "important for you" style personalization.
- **Departure/deletion:** on parent request, delete fully — Supabase
  auth user + profile + attempt/progress rows. Confirm cascades, then
  confirm to the owner in plain language what was removed.
- **Inactivity:** we do not auto-delete; education data stays until a
  human decides.

## Parent-facing communication (drafting for the owner)

When asked to draft the message parents receive with credentials:
- Mongolian first (parents' language), short, warm; include: the site
  URL, the child's login, the password, "you can change the password",
  and one sentence on what the child should do first (placement test
  for their grade).
- No marketing tone, no jargon, no tracking links.
- One message per family — never a broadcast containing multiple
  children's credentials.

## Support playbook (common tickets)

- "Can't log in": check exact email/username in Supabase auth, reset
  password, test in private window. 90% are typos or old cached tokens —
  have them log out fully (`/api/auth/logout` clears both cookies).
- "Wrong grade shown": fix `student_profiles.grade`, have them reload.
- "Child sees English": `mp_lang` toggle in the header; content follows
  the per-hub language rules (see `mn-translation`).
- Log every incident pattern here when it repeats — this list is the
  institutional memory.
