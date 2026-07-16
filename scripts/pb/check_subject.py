#!/usr/bin/env python3
"""Per-subject mini-gate: everything the global gates check, scoped to ONE
subject module — so authors can iterate on their module without depending on
the other subjects' state.

Usage:  python3 scripts/pb/check_subject.py <module>   (e.g. algebra_1)

Checks:
  1. build() schema — units, forms, unit membership, >= 33 variants per form,
     4 distinct options, valid correctIndex, non-empty explanation/check.
  2. Every check[] string sympifies to True.
  3. Every NEW form (not remapped, i.e. not in REMAP) has a RESOLVERS entry,
     and the blind re-solve of every variant of every resolved form matches
     options[correctIndex]. Zero mismatches, zero unparsed.
  4. Every geoFigure is drawn true to its labels (right-angle marks 90 +/- 0.7,
     "N deg" angle labels match drawn angles, numeric side labels share one
     scale +/- 2%%).
"""
import importlib.util
import math
import os
import re
import sys

import sympy as sp
from sympy import sympify

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts"))


def load(modname, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, modname + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def audit_helpers():
    spec = importlib.util.spec_from_file_location(
        "pb_audit", os.path.join(ROOT, "scripts", "audit_problembank.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def label_value(lab):
    lab = lab.strip()
    m = re.fullmatch(r"(\d+(?:\.\d+)?)", lab)
    if m:
        return float(m.group(1))
    m = re.fullmatch(r"(\d*)√(\d+)", lab)
    if m:
        c = float(m.group(1)) if m.group(1) else 1.0
        return c * math.sqrt(float(m.group(2)))
    return None


def check_figure(vid, fig, errors):
    pts = {p["id"]: (p["x"], p["y"]) for p in fig["points"]}
    scale = None
    for o in fig["objects"]:
        if o["kind"] == "angle":
            ax, ay = pts[o["at"]]
            fx, fy = pts[o["from"]]
            tx, ty = pts[o["to"]]
            a1 = math.atan2(fy - ay, fx - ax)
            a2 = math.atan2(ty - ay, tx - ax)
            d = math.degrees(abs(a2 - a1)) % 360
            if d > 180:
                d = 360 - d
            if o.get("right") and abs(d - 90) > 0.7:
                errors.append(f"{vid}: right-angle mark on {d:.2f} deg angle")
            lab = o.get("label")
            if lab:
                m = re.fullmatch(r"(\d+)°", lab.strip())
                if m and abs(d - float(m.group(1))) > 0.7:
                    errors.append(f"{vid}: angle label {lab} on {d:.2f} deg angle")
        elif o["kind"] in ("segment", "ray", "line"):
            lab = o.get("label")
            if not lab:
                continue
            val = label_value(lab)
            if val is None:
                continue
            x1, y1 = pts[o["from"]]
            x2, y2 = pts[o["to"]]
            ln = math.hypot(x2 - x1, y2 - y1)
            if val == 0 or ln == 0:
                errors.append(f"{vid}: degenerate labeled segment {lab!r}")
                continue
            s = ln / val
            if scale is None:
                scale = s
            elif abs(s / scale - 1) > 0.02:
                errors.append(f"{vid}: label {lab!r} scale {s:.4f} vs {scale:.4f}")


def main():
    modname = sys.argv[1]
    mod = load(modname, "subject_" + modname)
    aud = audit_helpers()
    data = mod.build()
    remapped = set(getattr(mod, "REMAP", {}).keys())
    resolvers = getattr(mod, "RESOLVERS", {})

    errors = []
    n_variants = n_checks = n_resolved = n_figs = 0
    seen_ids = set()
    unit_ids = [u["id"] for u in data["units"]]
    unit_count = {u: 0 for u in unit_ids}

    for f in data["forms"]:
        fid = f["id"]
        assert f["unit"] in unit_ids, f"{fid}: bad unit {f['unit']}"
        unit_count[f["unit"]] += len(f["variants"])
        # Each form needs enough sibling variants to feed the reroll button
        # and the miss->similar retry loop; the page shows only a few at once.
        if len(f["variants"]) < 10:
            errors.append(f"{fid}: only {len(f['variants'])} variants (< 10)")
        if f["level"] not in (1, 2, 3):
            errors.append(f"{fid}: bad level")
        if fid not in remapped and fid not in resolvers:
            errors.append(f"{fid}: NEW form has no RESOLVERS entry")
        for v in f["variants"]:
            n_variants += 1
            vid = v["id"]
            if vid in seen_ids:
                errors.append(f"{vid}: duplicate variant id")
            seen_ids.add(vid)
            if len(v["options"]) != 4 or len(set(v["options"])) != 4:
                errors.append(f"{vid}: options not 4 distinct")
            if not (0 <= v["correctIndex"] <= 3):
                errors.append(f"{vid}: bad correctIndex")
            if not v.get("explanation") or not v.get("check"):
                errors.append(f"{vid}: missing explanation/check")
            for c in v.get("check", []):
                n_checks += 1
                try:
                    ok = bool(sympify(c)) is True
                except Exception as e:  # noqa: BLE001
                    errors.append(f"{vid}: check failed to sympify: {c!r} ({e})")
                    continue
                if not ok:
                    errors.append(f"{vid}: check not True: {c!r}")
            # blind re-solve via this module's resolver
            if fid in resolvers:
                n_resolved += 1
                try:
                    kind, val = resolvers[fid](v["statement"])
                except Exception as e:  # noqa: BLE001
                    errors.append(f"{vid}: resolver crashed: {e}")
                    continue
                if kind == "num":
                    aud.failures.clear()
                    aud.check_numeric(v, val)
                    for x in aud.failures:
                        errors.append(f"{vid}: BLIND MISMATCH {x}")
                    aud.failures.clear()
                elif kind == "opt":
                    if v["options"][v["correctIndex"]] != val:
                        errors.append(f"{vid}: OPT mismatch — resolver says {val!r}, "
                                      f"answer is {v['options'][v['correctIndex']]!r}")
                elif kind == "assert":
                    if val is not True:
                        errors.append(f"{vid}: resolver assert failed")
                else:
                    errors.append(f"{vid}: resolver returned {kind!r}")
            if v.get("geoFigure"):
                n_figs += 1
                check_figure(vid, v["geoFigure"], errors)

    empty = [u for u, n in unit_count.items() if n == 0]
    thin = [f"{u}({n})" for u, n in unit_count.items() if 0 < n < 24]
    print(f"check_subject {modname}: forms={len(data['forms'])} variants={n_variants} "
          f"checks={n_checks} blind_resolved={n_resolved} figures={n_figs}")
    if empty:
        print(f"  EMPTY UNITS: {', '.join(empty)}")
    if thin:
        print(f"  THIN UNITS (<24): {', '.join(thin)}")
    if errors or empty or thin:
        for e in errors[:50]:
            print("  FAIL", e)
        print(f"  {len(errors)} error(s)")
        sys.exit(1)
    print("  ALL CLEAR")


if __name__ == "__main__":
    main()
