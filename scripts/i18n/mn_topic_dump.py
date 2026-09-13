#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump one topic's every translatable string, compactly, in one read.

WHY. Drafting a topic used to take five or six separate reads — lesson prose,
then facts, then worked examples, then try-it, then the interactive steps, one
lesson at a time — because the raw JSON is too large to print whole. Six round
trips per topic times sixty topics is most of a working week spent re-reading
files. This prints everything once, in draft order, with the noise stripped.

WHAT IS STRIPPED, and why it is safe:
  - `check[]` sympy assertions. They are maths, not language; the mirror keeps
    the English source's copies untouched and `verify:genmath` re-runs them.
  - ids are kept, because mn_draft_check counts them.
  - widget `config` blocks are summarised, not printed: a draft records them as
    "unchanged" and never rewrites a numeric config.

    python3 scripts/i18n/mn_topic_dump.py <corpus> <slug>
    python3 scripts/i18n/mn_topic_dump.py --terms <corpus> <slug>

`--terms` additionally counts every candidate maths term in the topic against
the ministry standard and the Mongolian corpus, which is the grounding pass
every draft opens with.
"""
import json
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def load(corpus, slug):
    return json.load(open(os.path.join(ROOT, "data", "genmath", corpus, slug + ".json"), encoding="utf-8"))


def line(label, value, width=None):
    if value is None or value == "":
        return
    s = str(value).replace("\n", " ")
    if width:
        s = s[:width]
    print(f"{label}{s}")


def dump_items(tag, items, keys):
    for it in items or []:
        parts = []
        for k in keys:
            v = it.get(k)
            if v:
                parts.append(f"{k}={v}" if k == "id" else f"{k}: {v}")
        print(f"  [{tag}] " + " | ".join(str(p).replace("\n", " ") for p in parts))


def dump_step(i, s):
    kind = s.get("kind", "?")
    head = f"  [{i}] {kind}"
    bits = []
    for k in ("eyebrow", "title"):
        if s.get(k):
            bits.append(f"{k}={s[k]}")
    print(head + "  " + " · ".join(bits))
    for k in ("body", "teach", "intro", "prompt", "explanation"):
        if s.get(k):
            line(f"        {k}: ", s[k])
    for b in s.get("beats", []) or []:
        line("        beat: ", b)
    for p in s.get("points", []) or []:
        line("        point: ", p)
    if s.get("options"):
        print(f"        options: {s['options']}  correctIndex={s.get('correctIndex')}")
    for ex in s.get("examples", []) or []:
        line("        ex.prompt: ", ex.get("prompt"))
        for st in ex.get("steps", []) or []:
            line("          step: ", st)
        line("        ex.answer: ", ex.get("answer"))
    for pr in s.get("problems", []) or []:
        line("        p.prompt: ", pr.get("prompt"))
        if pr.get("options"):
            print(f"        p.options: {pr['options']}  correctIndex={pr.get('correctIndex')}")
        line("        p.explanation: ", pr.get("explanation"))
    if s.get("problemId"):
        print(f"        problemId: {s['problemId']}")
    if s.get("config"):
        print(f"        config: unchanged {json.dumps(s['config'], ensure_ascii=False)}")


def dump(corpus, slug):
    d = load(corpus, slug)
    print(f"===== {corpus}/{slug} =====")
    line("TITLE: ", d.get("title"))
    line("BLURB: ", d.get("blurb"))
    for i, l in enumerate(d.get("lessons", []), 1):
        print(f"\n----- LESSON {i}: {l.get('title')}  (`{l.get('slug')}`)")
        line("  concreteComparison: ", l.get("concreteComparison"))
        line("  objective: ", l.get("objective"))
        for c in l.get("concept", []) or []:
            line("  concept: ", c)
        line("  keyIdea: ", l.get("keyIdea"))
        for f in l.get("facts", []) or []:
            print(f"  [fact] title: {f.get('title')} | latex: {f.get('latex')} | explanation: {f.get('explanation')}")
        dump_items("we", l.get("workedExamples"), ["id", "statement", "solution"])
        dump_items("cm", l.get("commonMistakes"), ["text", "correction"])
        dump_items("try", l.get("tryIt"), ["id", "statement", "solution"])
        steps = (l.get("interactive") or {}).get("steps", []) or []
        if steps:
            print(f"  --- interactive: {len(steps)} steps")
            for j, s in enumerate(steps):
                dump_step(j, s)
    print("\n----- PRACTICE")
    dump_items("pr", d.get("practice"), ["id", "statement", "solution"])
    print("----- TEST YOURSELF")
    dump_items("ty", d.get("testYourself"), ["id", "statement", "solution"])


# --- grounding -------------------------------------------------------------

_MIN = None
_COR = None


def corpora():
    global _MIN, _COR
    if _MIN is None:
        _MIN = open(os.path.join(ROOT, "data/esh/moe-curriculum.json"), encoding="utf-8").read()
        files = glob.glob(os.path.join(ROOT, "data/questions/*.json")) + glob.glob(
            os.path.join(ROOT, "data/genmath/*-mn/*.json")
        )
        _COR = "".join(open(f, encoding="utf-8").read() for f in files)
    return _MIN, _COR


def ground(terms):
    """Count each Mongolian term in the ministry standard and the MN corpus."""
    m, c = corpora()
    print(f"{'term':<34}{'ministry':>9}{'corpus':>8}")
    for t in terms:
        print(f"{t:<34}{len(re.findall(re.escape(t), m, re.I)):>9}{len(re.findall(re.escape(t), c, re.I)):>8}")


def main():
    args = sys.argv[1:]
    if args and args[0] == "--terms":
        # read terms from stdin, one per line, after dumping
        corpus, slug = args[1], args[2]
        dump(corpus, slug)
        terms = [t.strip() for t in sys.stdin.read().splitlines() if t.strip()]
        if terms:
            print("\n----- GROUNDING")
            ground(terms)
        return 0
    if len(args) != 2:
        raise SystemExit(__doc__)
    dump(*args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
