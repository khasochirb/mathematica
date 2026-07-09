#!/usr/bin/env python3
"""MN pipeline applier: python3 scripts/i18n/mn_apply.py <grade> <slug>

Re-walks data/genmath/<grade>/<slug>.json in the identical walker order,
swaps in MN[i] from <workdir>/mn_<grade>_<slug>_tr.py, and writes
data/genmath/<grade>-mn/<slug>.json.

Safety asserts (all hard failures):
  - translation count == extracted count, full index coverage
  - exact EN match at every position (order-drift protection)
  - single-asterisk emphasis scan (MathText renders **bold** only)
  - CYR-IN-MATH scan: Cyrillic inside $...$ outside \\text{...} means a
    bare-$ pair swallowed prose — always a translation bug

Work dir: $MN_WORKDIR if set, else ./i18n-work. Run from repo root.
See .claude/skills/mn-translation/SKILL.md for the full workflow.
"""
import json, os, re, sys, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from mn_walk import walk  # noqa: E402

GRADE, SLUG = sys.argv[1], sys.argv[2]
WORK = os.environ.get("MN_WORKDIR", os.path.join(REPO, "i18n-work"))
SRC = os.path.join(REPO, "data", "genmath", GRADE, f"{SLUG}.json")
SRC_LIST = os.path.join(WORK, f"mn_{GRADE}_{SLUG}_src.json")
TR = os.path.join(WORK, f"mn_{GRADE}_{SLUG}_tr.py")
OUT_DIR = os.path.join(REPO, "data", "genmath", f"{GRADE}-mn")
OUT = os.path.join(OUT_DIR, f"{SLUG}.json")

spec = importlib.util.spec_from_file_location("tr", TR)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
MN = mod.MN

src_entries = json.load(open(SRC_LIST))
assert len(MN) == len(src_entries), f"translation count {len(MN)} != extracted {len(src_entries)}"
for e in src_entries:
    assert e["i"] in MN, f"missing translation for index {e['i']}: {e['en'][:60]}"

state = {"idx": 0}
def visit(obj, key):
    i = state["idx"]
    expected = src_entries[i]["en"]
    got = obj[key]
    assert got == expected, f"order drift at {i}: got {got[:50]!r} expected {expected[:50]!r}"
    obj[key] = MN[i]
    state["idx"] += 1

topic = json.load(open(SRC))
walk(topic, visit)
assert state["idx"] == len(src_entries), f"consumed {state['idx']} of {len(src_entries)}"

MATH_SPLIT = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)")
CYR = re.compile(r"[А-Яа-яЁёӨөҮү]")
# EN itself uses *italics* in some prose; a faithful MN carry-over is fine.
# Only flag single-asterisk strings whose EN counterpart had none.
EN_HAS_STAR = {MN[e["i"]] for e in src_entries if "*" in e["en"].replace("**", "")}
def scan(o):
    hits = []
    def w(v):
        if isinstance(v, str):
            if "*" in v.replace("**", "") and CYR.search(v) and v not in EN_HAS_STAR and "==" not in v and "!=" not in v and "<" not in v and ">" not in v:
                hits.append("ASTERISK: " + v[:70])
            s2 = v.replace("\\$", "\x00")
            for part in MATH_SPLIT.findall(s2):
                if part.startswith("$"):
                    body = re.sub(r"\\text\{[^}]*\}", "", part)
                    if CYR.search(body):
                        hits.append("CYR-IN-MATH: " + v[:70])
        elif isinstance(v, dict):
            for x in v.values(): w(x)
        elif isinstance(v, list):
            for x in v: w(x)
    w(o)
    return hits

bad = scan(topic)
if bad:
    print("SCAN FAIL:", bad); sys.exit(1)

os.makedirs(OUT_DIR, exist_ok=True)
json.dump(topic, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"WROTE {OUT} ({state['idx']} strings translated)")
