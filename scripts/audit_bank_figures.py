#!/usr/bin/env python3
"""Coordinate audit of every geoFigure in data/problembank/*.json.

Checks, per figure:
  1. every angle object with right:true really is 90° (±0.7°)
  2. every angle label "N°" matches the drawn angle (±0.7°)
  3. every numeric segment label (incl. "n√2" forms) is proportional to the
     drawn length at ONE consistent scale per figure (±2%)
"""
import glob
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad = []
n_figs = n_right = n_anglabels = n_sidelabels = 0


def label_value(lab):
    lab = lab.strip()
    m = re.fullmatch(r"(\d+(?:\.\d+)?)", lab)
    if m:
        return float(m.group(1))
    m = re.fullmatch(r"(\d*)√(\d+)", lab)
    if m:
        c = float(m.group(1)) if m.group(1) else 1.0
        return c * math.sqrt(float(m.group(2)))
    return None  # "?", letters — not numeric


for path in sorted(glob.glob(os.path.join(ROOT, "data/problembank/*.json"))):
    topic = json.load(open(path))
    for form in topic["forms"]:
        for v in form["variants"]:
            fig = v.get("geoFigure")
            if not fig:
                continue
            n_figs += 1
            pts = {p["id"]: (p["x"], p["y"]) for p in fig["points"]}
            scale = None  # length-per-label-unit, fixed per figure
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
                    if o.get("right"):
                        n_right += 1
                        if abs(d - 90) > 0.7:
                            bad.append((v["id"], "right-angle mark on %.2f° angle" % d))
                    lab = o.get("label")
                    if lab:
                        m = re.fullmatch(r"(\d+)°", lab.strip())
                        if m:
                            n_anglabels += 1
                            if abs(d - float(m.group(1))) > 0.7:
                                bad.append((v["id"], "angle label %s on %.2f° angle" % (lab, d)))
                elif o["kind"] in ("segment", "ray", "line"):
                    lab = o.get("label")
                    if not lab:
                        continue
                    val = label_value(lab)
                    if val is None:
                        continue
                    n_sidelabels += 1
                    x1, y1 = pts[o["from"]]
                    x2, y2 = pts[o["to"]]
                    ln = math.hypot(x2 - x1, y2 - y1)
                    if val == 0 or ln == 0:
                        bad.append((v["id"], "degenerate labeled segment %r" % lab))
                        continue
                    s = ln / val
                    if scale is None:
                        scale = s
                    elif abs(s / scale - 1) > 0.02:
                        bad.append((v["id"], "label %r scale %.4f vs figure scale %.4f" % (lab, s, scale)))

print("figures audited: %d  (right-angle marks %d, angle labels %d, numeric side labels %d)"
      % (n_figs, n_right, n_anglabels, n_sidelabels))
if bad:
    for vid, msg in bad[:40]:
        print("FAIL", vid, "-", msg)
    print("TOTAL FAILURES:", len(bad))
    sys.exit(1)
print("✓ every figure is drawn true to its labels")
