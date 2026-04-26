#!/usr/bin/env bash
# Manual snapshot of prod Supabase Postgres. Use ad-hoc before risky
# migrations. NOT the production backup plan — Supabase Pro's automated
# daily backups are. See PHASES.md "Launch trigger items".
#
# Setup (one-time):
#   1. brew install libpq && brew link --force libpq   # gets pg_dump
#   2. Get prod connection string from Supabase dashboard:
#      Project Settings → Database → Connection string → URI (use the
#      "Session" or "Direct connection" variant, NOT the pooler).
#   3. Save it to ~/.mp-backup-env (chmod 600), one line:
#      DATABASE_URL="postgres://postgres:<password>@<host>:5432/postgres"
#
# Usage: bash scripts/backup-prod.sh
set -euo pipefail

ENV_FILE="${HOME}/.mp-backup-env"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "ERROR: missing $ENV_FILE — see header for setup steps" >&2
  exit 1
fi
# shellcheck disable=SC1090
source "$ENV_FILE"

if [[ -z "${DATABASE_URL:-}" ]]; then
  echo "ERROR: DATABASE_URL not set in $ENV_FILE" >&2
  exit 1
fi

if ! command -v pg_dump >/dev/null 2>&1; then
  echo "ERROR: pg_dump not in PATH — brew install libpq && brew link --force libpq" >&2
  exit 1
fi

LOCAL_DIR="${HOME}/Backups/mongolpotential"
ICLOUD_DIR="${HOME}/Library/Mobile Documents/com~apple~CloudDocs/MongolPotential-Backups"
mkdir -p "$LOCAL_DIR" "$ICLOUD_DIR"

STAMP="$(date +%Y-%m-%d-%H%M%S)"
LOCAL_FILE="${LOCAL_DIR}/prod-${STAMP}.sql.gz"

echo "[backup] dumping prod → $LOCAL_FILE"
pg_dump --no-owner --no-acl "$DATABASE_URL" | gzip > "$LOCAL_FILE"

# Sanity check — empty/tiny dump means something went wrong silently
SIZE=$(stat -f%z "$LOCAL_FILE")
if [[ "$SIZE" -lt 1024 ]]; then
  echo "ERROR: dump is suspiciously small ($SIZE bytes); check connection" >&2
  exit 1
fi

echo "[backup] copying to iCloud Drive"
cp "$LOCAL_FILE" "${ICLOUD_DIR}/prod-${STAMP}.sql.gz"

echo "[backup] done. ${SIZE} bytes."
echo "  local:  $LOCAL_FILE"
echo "  icloud: ${ICLOUD_DIR}/prod-${STAMP}.sql.gz"
