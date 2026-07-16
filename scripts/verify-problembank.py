#!/usr/bin/env python3
"""Problem-bank integrity gate.

For every subject in data/problembank/*.json asserts:
  - subject has slug/title/titleMn/blurb, a non-empty units[] (course spine),
    and >= 1 form;
  - every form has id/title/skill, level in {1,2,3}, a `unit` that exists in
    units[], and >= 4 variants (the miss->similar mechanic needs siblings);
  - every unit in units[] has >= 1 form and >= 24 variants (a unit page must
    be a real collection, not a stub);
  - every variant has a unique id, statement, exactly 4 DISTINCT options,
    a valid correctIndex, a non-empty explanation, and a NON-EMPTY check[];
  - every check string sympifies to True.

No bank problem ships without a passing sympy hard-assert.
Run: npm run verify:bank
"""
import glob
import json
import os
import sys

from sympy import sympify

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = sorted(glob.glob(os.path.join(ROOT, "data", "problembank", "*.json")))

failures = []
topics = forms = variants = checks_run = 0
seen_ids = set()

for path in FILES:
    with open(path) as fh:
        t = json.load(fh)
    topics += 1
    slug = t.get("slug", os.path.basename(path))
    for field in ("slug", "title", "titleMn", "blurb"):
        if not t.get(field):
            failures.append(f"{slug}: missing topic field '{field}'")
    units = t.get("units") or []
    if not units:
        failures.append(f"{slug}: missing units[] — subjects must mirror the course spine")
    unit_ids = [u.get("id") for u in units]
    for u in units:
        if not u.get("id") or not u.get("title"):
            failures.append(f"{slug}: unit missing id/title: {u!r}")
    unit_variant_count = {uid: 0 for uid in unit_ids}
    unit_form_count = {uid: 0 for uid in unit_ids}
    if not t.get("forms"):
        failures.append(f"{slug}: no forms")
        continue
    for f in t["forms"]:
        forms += 1
        fid = f"{slug}/{f.get('id', '<no-id>')}"
        for field in ("id", "title", "skill"):
            if not f.get(field):
                failures.append(f"{fid}: missing form field '{field}'")
        if f.get("level") not in (1, 2, 3):
            failures.append(f"{fid}: level must be 1..3, got {f.get('level')!r}")
        if f.get("unit") not in unit_ids:
            failures.append(f"{fid}: unit {f.get('unit')!r} not in subject units[]")
        else:
            unit_form_count[f["unit"]] += 1
            unit_variant_count[f["unit"]] += len(f.get("variants", []))
        vs = f.get("variants", [])
        if len(vs) < 4:
            failures.append(f"{fid}: needs >= 4 variants for miss->similar, has {len(vs)}")
        for v in vs:
            variants += 1
            vid = f"{fid}/{v.get('id', '<no-id>')}"
            if not v.get("id"):
                failures.append(f"{vid}: missing id")
            elif v["id"] in seen_ids:
                failures.append(f"{vid}: duplicate variant id")
            else:
                seen_ids.add(v["id"])
            if not v.get("statement"):
                failures.append(f"{vid}: missing statement")
            opts = v.get("options")
            if not isinstance(opts, list) or len(opts) != 4:
                failures.append(f"{vid}: needs exactly 4 options")
            elif len(set(opts)) != 4:
                failures.append(f"{vid}: options not distinct: {opts}")
            ci = v.get("correctIndex")
            if not isinstance(ci, int) or not (0 <= ci <= 3):
                failures.append(f"{vid}: bad correctIndex {ci!r}")
            if not v.get("explanation"):
                failures.append(f"{vid}: missing explanation")
            chks = v.get("check")
            if not isinstance(chks, list) or len(chks) == 0:
                failures.append(f"{vid}: empty check[] — every answer must be sympy-verified")
                continue
            for expr in chks:
                checks_run += 1
                try:
                    result = sympify(expr)
                except Exception as e:  # noqa: BLE001
                    failures.append(f"{vid}: check did not sympify: {expr!r} ({e})")
                    continue
                try:
                    ok = bool(result) is True
                except TypeError:
                    ok = False
                if not ok:
                    failures.append(f"{vid}: check is NOT True: {expr!r} -> {result!r}")
    for uid in unit_ids:
        if unit_form_count.get(uid, 0) == 0:
            failures.append(f"{slug}/{uid}: unit has NO forms — every unit needs a collection")
        elif unit_variant_count.get(uid, 0) < 24:
            failures.append(f"{slug}/{uid}: unit has only {unit_variant_count[uid]} problems (< 24)")

print(f"verify:bank — subjects: {topics}, forms: {forms}, variants: {variants}, sympy checks run: {checks_run}")
if failures:
    for f in failures:
        print(f"  ✗ {f}")
    print(f"  {len(failures)} FAILURE(S)")
    sys.exit(1)
print("  ✓ all checks passed")
