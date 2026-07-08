# Creating student accounts (teacher guide)

Provision student logins in a batch, hand the credentials to parents, and
each student gets a personalized start with full access to the whole site.

## What a provisioned account gets

- **Immediate login** — email is pre-confirmed, so parents sign in right
  away at `/sign-in` with the email + password you hand them (no
  confirmation email to click).
- **Full access** — `is_subscribed = true` with no expiry (lifetime), so
  every hub, past paper, practice test, and worked solution is unlocked to
  explore freely.
- **Personalized dashboard** — their grade and a "Focus on" shortcut show
  up on `/dashboard`. It's a suggested starting point only; nothing is
  locked off.

## One-time setup

1. Apply the migration that adds the grade/focus fields (only once, and
   only if not already applied):

   ```sh
   # in the Supabase SQL editor, or via the CLI:
   psql "$SUPABASE_DB_URL" -f supabase/migrations/008_student_profiles.sql
   ```

2. Make the service-role key available to the script. It's the same secret
   the app uses — never commit it. A local `.env.local` with
   `NEXT_PUBLIC_SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` works:

   ```sh
   set -a; source .env.local; set +a
   ```

## Each time you add students

1. Copy the example roster and fill in your students:

   ```sh
   cp scripts/students-roster.example.json scripts/my-roster.json
   ```

   Per student (see the example for the shape):

   | field | required | notes |
   |---|---|---|
   | `displayName` | yes | Shown in the app greeting |
   | `grade` | yes | `"6"`..`"12"` or a track like `"ЭЕШ"`, `"SAT"`, `"IB"` |
   | `focus` | no | Human label, e.g. `"Geometry · circles"` |
   | `focusHref` | no | In-app link for the shortcut, e.g. `"/math/geometry"` |
   | `username` | no | Defaults to a slug of the name |
   | `email` | no | Defaults to `<username>@students.mongolpotential.com` |
   | `password` | no | Defaults to a readable one like `brave-eagle-42` |
   | `notes` | no | Private teacher note, not shown to the student |

2. Dry-run first to preview the emails/passwords without touching the DB:

   ```sh
   node scripts/create-students.mjs scripts/my-roster.json --dry-run
   ```

3. Provision for real. It writes a credentials sheet you can send to
   parents:

   ```sh
   node scripts/create-students.mjs scripts/my-roster.json --out scripts/creds.csv
   ```

   Output columns: Student, Grade, Focus, Login (email), Password, Status.
   Send each parent their student's **email + password**.

## Notes

- **Re-running is safe.** Accounts are matched by email; an existing one is
  updated (and its password only reset if the roster supplies a new one).
- Keep the generated `creds.csv` out of git — it holds plaintext
  passwords. (It lands in `scripts/` which you should not commit; delete it
  after sending.)
- `focusHref` values that exist today: `/math/6`…`/math/12`,
  `/math/geometry`, `/practice/esh`, `/practice/sat`, `/practice/ib`,
  `/courses`.
- To change a student's grade/focus later, edit the roster and re-run, or
  update their `profiles` row directly in Supabase.
