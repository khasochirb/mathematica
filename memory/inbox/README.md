# Inbox — documents Khas sent that are not repo policy

Files here were uploaded into a session and parked rather than installed,
because installing them would have contradicted something. Each one needs a
ruling from Khas before it means anything.

## `khas-CLAUDE-md-2026-09-15.md`

A CLAUDE.md for "mongolpotential.com" carrying the Mongolian translation
rules. **It does not describe this repository**, so it is not installed:

| It says | This repo |
|---|---|
| Create React App | Next.js 14.2.35, app router |
| copy in `src/pages/`, `src/components/` | `app/`, `components/` — there is no `src/` |
| question banks in `src/data/*.json` | `data/genmath/`, `data/esh/`, `data/questions/` |
| `docs/mn-voice-corpus.tsv` | not supplied |
| ЭЕШ | ЭШ — Khas corrected this on 15 Sep |
| "IB and AP stay legacy until 2027" absent; AP Calculus listed as a target | rule 7, amended 17 Aug |

Its *content* rules are good and mostly already ours. What was taken from it:

- §B voice rules → installed as `docs/mn-voice-reference.md` and encoded in
  `scripts/i18n/mn_draft_check.py`.
- §A term-not-found rule → already in `docs/MONGOLIAN.md`, and this file
  confirms the coverage is "A through I complete, and into J".
- Rule 11 («сурагч», never «оюутан») → now a check.
- Rule 12 (translate copy, not machinery) → why the checks skip `$...$`
  and backticked config.

What was **not** taken, and why:

- **It is a CLAUDE.md.** The repo's own `CLAUDE.md` says it is the master and
  is Khas's to amend, not Claude's. Replacing it from a file describing a
  different codebase would be exactly the drift it was written to stop.
- **§B rule 8, bare imperative task wording** — contradicts the standing «та»
  ruling. Open; see `docs/MONGOLIAN.md` § "the register contradiction".
- **Its "Open decision"** — whether to gloss the English term on first use,
  «өнцгийн биссектрис (angle bisector)». It says to ask before adopting either
  convention site-wide. Not adopted, not used in any draft.
