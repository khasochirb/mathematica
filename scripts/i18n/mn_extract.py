#!/usr/bin/env python3
"""MN pipeline extractor: python3 scripts/i18n/mn_extract.py <grade> <slug>

Walks data/genmath/<grade>/<slug>.json with the shared walker (mn_walk.py)
and emits <workdir>/mn_<grade>_<slug>_src.json: [{"i": n, "en": "..."}].

Work dir: $MN_WORKDIR if set, else ./i18n-work (gitignored). Run from repo
root. See .claude/skills/mn-translation/SKILL.md for the full workflow.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from mn_walk import walk  # noqa: E402

GRADE, SLUG = sys.argv[1], sys.argv[2]
WORK = os.environ.get("MN_WORKDIR", os.path.join(REPO, "i18n-work"))
os.makedirs(WORK, exist_ok=True)
SRC = os.path.join(REPO, "data", "genmath", GRADE, f"{SLUG}.json")
OUT = os.path.join(WORK, f"mn_{GRADE}_{SLUG}_src.json")

collected = []
def visit(obj, key):
    collected.append(obj[key])

topic = json.load(open(SRC))
walk(topic, visit)
entries = [{"i": i, "en": s} for i, s in enumerate(collected)]
json.dump(entries, open(OUT, "w"), ensure_ascii=False, indent=0)
print(f"{GRADE}/{SLUG}: {len(entries)} translatable strings -> {OUT}")
