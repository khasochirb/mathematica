#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify a Mongolian topic against its English source — STRUCTURE ONLY.

    python3 scripts/i18n/mn_skeleton.py <corpus> <slug>      # one topic
    python3 scripts/i18n/mn_skeleton.py --all                # every MN mirror
    python3 scripts/i18n/mn_skeleton.py --selftest           # prove the checks bite

WHY THIS REPLACES THE OLD GATE.

`mn_apply.py` asserts one Mongolian string per English string in the same slot,
in one deterministic walker order. That is a TRANSLATION machine: it can only
express a mirror where sentence i corresponds to sentence i. Under the rewrite
rule in docs/MONGOLIAN.md — "we rewrite, we do not translate; different sentence
count, different examples, different order — expected" — the first rewritten
topic fails it, and would fail it for being correct.

So this checks the skeleton and never the prose:

  KEPT, because these are what the site navigates by and grades against
    lesson count, lesson slugs, lesson order
    problem ids (workedExamples, tryIt, practice, testYourself)
    interactive step KIND sequence
    tapQuestion option counts and correctIndex range
    check[] presence wherever the English has one

  DROPPED, because the rewrite rule frees them
    sentence counts, paragraph counts, fact counts
    the wording of anything
    which worked example teaches what, and with which numbers

  KEPT from the old gate, because neither assumes parity
    CYR-IN-MATH — Cyrillic inside $...$ outside \\text{...} breaks KaTeX
    single-asterisk emphasis — MathText renders **bold** only

WHY IDS ARE THE HARD PART. Interactive steps of kind `worked` and `tryIt` do not
carry their own content — they reference a problem by `problemId`, and every
student attempt is recorded against that same id. A rewritten worked example may
change its numbers entirely, but if it changes its ID the widget points at
nothing and the student's history detaches from the problem it belongs to. That
is why ids are compared as SETS and reported both ways round.

Exit 1 on any violation: this one IS a gate.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MATH_SPLIT = re.compile(r"(\$\$[^$]+\$\$|\$[^$]+\$|\*\*[^*]+\*\*)")
CYR = re.compile(r"[А-Яа-яЁёӨөҮү]")


# ---------------------------------------------------------------------------
# The skeleton
# ---------------------------------------------------------------------------

def _ids(items):
    return [p.get("id") for p in items or []]


def skeleton(topic: dict) -> dict:
    """Everything about a topic that a rewrite may NOT change."""
    lessons = []
    for les in topic.get("lessons", []):
        steps = les.get("interactive", {}).get("steps", []) or []
        lessons.append({
            "slug": les.get("slug"),
            "workedExampleIds": _ids(les.get("workedExamples")),
            "tryItIds": _ids(les.get("tryIt")),
            # The kind sequence IS the lesson's shape on screen: each kind is a
            # different React component. Reordering it is a design change, not a
            # language one.
            "stepKinds": [s.get("kind") for s in steps],
            # worked/tryIt steps are pure references; a dangling one renders nothing.
            "stepProblemIds": [s.get("problemId") for s in steps if "problemId" in s],
            # Option counts must hold or correctIndex can point past the end.
            "optionCounts": [len(s.get("options", [])) for s in steps if s.get("kind") == "tapQuestion"],
            "correctIndexes": [s.get("correctIndex") for s in steps if s.get("kind") == "tapQuestion"],
        })
    return {
        "slug": topic.get("slug"),
        "status": topic.get("status"),
        "lessons": lessons,
        "practiceIds": _ids(topic.get("practice")),
        "testYourselfIds": _ids(topic.get("testYourself")),
    }


def checked_paths(topic: dict):
    """Every item that carries a sympy check[], by a stable path.

    Presence is what is compared, never contents: a rewritten example is
    REQUIRED to bring its own new assertions, and verify:genmath runs them.
    """
    out = set()
    for li, les in enumerate(topic.get("lessons", [])):
        for field in ("workedExamples", "tryIt"):
            for p in les.get(field, []) or []:
                if p.get("check"):
                    out.add(f"lessons[{li}].{field}[{p.get('id')}]")
        for si, s in enumerate(les.get("interactive", {}).get("steps", []) or []):
            if s.get("check"):
                out.add(f"lessons[{li}].steps[{si}:{s.get('kind')}]")
    for field in ("practice", "testYourself"):
        for p in topic.get(field, []) or []:
            if p.get("check"):
                out.add(f"{field}[{p.get('id')}]")
    return out


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------

def compare(en: dict, mn: dict):
    """Structural violations, as readable lines. Empty list = the mirror is sound."""
    bad = []
    a, b = skeleton(en), skeleton(mn)

    if a["slug"] != b["slug"]:
        bad.append(f"topic slug: EN {a['slug']!r} vs MN {b['slug']!r}")
    if a["status"] != b["status"]:
        bad.append(f"topic status: EN {a['status']!r} vs MN {b['status']!r}")

    if len(a["lessons"]) != len(b["lessons"]):
        bad.append(f"lesson count: EN {len(a['lessons'])} vs MN {len(b['lessons'])}")
        return bad  # per-lesson comparison is meaningless once the counts differ

    en_slugs = [l["slug"] for l in a["lessons"]]
    mn_slugs = [l["slug"] for l in b["lessons"]]
    if en_slugs != mn_slugs:
        # Order matters as much as membership — lessons build on each other, and
        # the slug is the URL and the progress key.
        if sorted(en_slugs) == sorted(mn_slugs):
            bad.append(f"lesson ORDER differs:\n    EN {en_slugs}\n    MN {mn_slugs}")
        else:
            for s in sorted(set(en_slugs) - set(mn_slugs)):
                bad.append(f"lesson missing from MN: {s!r}")
            for s in sorted(set(mn_slugs) - set(en_slugs)):
                bad.append(f"lesson only in MN: {s!r}")
        return bad

    for la, lb in zip(a["lessons"], b["lessons"]):
        where = f"lesson {la['slug']!r}"
        for field, label in (("workedExampleIds", "workedExamples"), ("tryItIds", "tryIt")):
            sa, sb = set(la[field]), set(lb[field])
            for i in sorted(sa - sb):
                bad.append(f"{where}: {label} id {i!r} missing from MN — its widget step and every recorded attempt point at it")
            for i in sorted(sb - sa):
                bad.append(f"{where}: {label} id {i!r} invented in MN")
            if len(la[field]) != len(lb[field]):
                bad.append(f"{where}: {label} count EN {len(la[field])} vs MN {len(lb[field])}")
        if la["stepKinds"] != lb["stepKinds"]:
            bad.append(f"{where}: interactive step kinds differ (each kind is a different component)\n    EN {la['stepKinds']}\n    MN {lb['stepKinds']}")
        if la["stepProblemIds"] != lb["stepProblemIds"]:
            bad.append(f"{where}: step problemId references differ\n    EN {la['stepProblemIds']}\n    MN {lb['stepProblemIds']}")
        if la["optionCounts"] != lb["optionCounts"]:
            bad.append(f"{where}: tapQuestion option counts EN {la['optionCounts']} vs MN {lb['optionCounts']}")
        if la["correctIndexes"] != lb["correctIndexes"]:
            bad.append(f"{where}: tapQuestion correctIndex EN {la['correctIndexes']} vs MN {lb['correctIndexes']} — the answer moved")

    for field in ("practiceIds", "testYourselfIds"):
        if a[field] != b[field]:
            bad.append(f"{field}: EN {a[field]} vs MN {b[field]} — these are GRADED and keyed to attempt history")

    missing = checked_paths(en) - checked_paths(mn)
    for m in sorted(missing):
        bad.append(f"check[] lost in MN at {m} — a rewritten item must carry its own sympy assertions")

    return bad


# ---------------------------------------------------------------------------
# Render-safety scans (carried over — neither assumes parity)
# ---------------------------------------------------------------------------

# Fields that are NEVER rendered by MathText and must not be scanned as prose.
# `check` holds sympy assertions where `*` is multiplication and `<`/`>` are
# comparisons — scanning them reported 15,401 "emphasis errors" across the
# English corpus, none of them real. `verify` is the same thing under the
# practice-test schema.
NON_PROSE_KEYS = {"check", "verify"}


def scan(topic: dict):
    """Render-safety only. Neither rule assumes any parity with the English."""
    hits = []

    def walk(v, path="$"):
        if isinstance(v, str):
            body = v.replace("\\$", "\x00")
            for part in MATH_SPLIT.findall(body):
                if part.startswith("$"):
                    inner = re.sub(r"\\text\{[^}]*\}", "", part)
                    if CYR.search(inner):
                        hits.append(f"CYR-IN-MATH at {path}: {v[:70]}")
            # MathText splits on $$...$$, $...$ and **bold** and nothing else
            # (components/esh/MathText.tsx:24), so a single asterisk reaches the
            # reader as a literal asterisk. Only flag it OUTSIDE math, where an
            # asterisk is multiplication rather than emphasis.
            outside = MATH_SPLIT.sub(" ", body)
            if "*" in outside:
                hits.append(f"SINGLE-ASTERISK at {path}: {v[:70]}")
        elif isinstance(v, dict):
            for k, x in v.items():
                if k in NON_PROSE_KEYS:
                    continue
                walk(x, f"{path}.{k}")
        elif isinstance(v, list):
            for i, x in enumerate(v):
                walk(x, f"{path}[{i}]")

    walk(topic)
    return hits


# ---------------------------------------------------------------------------

def split_severity(hits):
    """CYR-IN-MATH breaks KaTeX and ships a red error box to a student — fatal.
    SINGLE-ASTERISK renders as a literal asterisk — wrong, but legible, and it
    is inherited from the English source (1,032 English strings carry it against
    36 Mongolian ones). Failing the gate on a pre-existing English habit would
    make it red from birth, and a gate nobody can get green is a gate nobody
    reads. Reported, not enforced, until the English is cleaned up.
    """
    fatal = [h for h in hits if not h.startswith("SINGLE-ASTERISK")]
    warn = [h for h in hits if h.startswith("SINGLE-ASTERISK")]
    return fatal, warn


def check_topic(corpus: str, slug: str):
    en_path = os.path.join(ROOT, "data", "genmath", corpus, f"{slug}.json")
    mn_path = os.path.join(ROOT, "data", "genmath", f"{corpus}-mn", f"{slug}.json")
    if not os.path.exists(en_path):
        return [f"no English source at {en_path}"]
    if not os.path.exists(mn_path):
        return [f"no Mongolian mirror at {mn_path}"]
    en = json.load(open(en_path, encoding="utf8"))
    mn = json.load(open(mn_path, encoding="utf8"))
    fatal, warn = split_severity(scan(mn))
    return compare(en, mn) + fatal, warn


def selftest() -> int:
    """Mutate a real mirror in each forbidden way; every one must be caught.

    A structural gate that silently passes is worse than none — it certifies
    rewrites nobody checked. So each rule is exercised against real data rather
    than asserted to work.
    """
    import copy

    en = json.load(open(os.path.join(ROOT, "data", "genmath", "6", "percentages.json"), encoding="utf8"))
    base = json.load(open(os.path.join(ROOT, "data", "genmath", "6-mn", "percentages.json"), encoding="utf8"))

    failures = []
    if compare(en, base):
        failures.append(f"clean mirror reported violations: {compare(en, base)[:2]}")

    def mutate(name, fn):
        m = copy.deepcopy(base)
        fn(m)
        if not compare(en, m):
            failures.append(f"NOT CAUGHT: {name}")

    mutate("dropped a lesson", lambda m: m["lessons"].pop())
    mutate("reordered lessons", lambda m: m["lessons"].insert(0, m["lessons"].pop()))
    mutate("renamed a lesson slug", lambda m: m["lessons"][0].__setitem__("slug", "renamed"))
    mutate("changed a workedExample id", lambda m: m["lessons"][0]["workedExamples"][0].__setitem__("id", "zz-1"))
    mutate("dropped a tryIt", lambda m: m["lessons"][0]["tryIt"].pop())
    mutate("renamed a practice id", lambda m: m["practice"][0].__setitem__("id", "pr-999"))
    mutate("dropped a practice item", lambda m: m["practice"].pop())
    mutate("removed a check[]", lambda m: m["practice"][0].pop("check"))
    mutate("changed the topic slug", lambda m: m.__setitem__("slug", "other"))

    def drop_step(m):
        m["lessons"][0]["interactive"]["steps"].pop()
    mutate("dropped an interactive step", drop_step)

    def reorder_steps(m):
        s = m["lessons"][0]["interactive"]["steps"]
        s.insert(0, s.pop())
    mutate("reordered interactive steps", reorder_steps)

    def drop_option(m):
        for s in m["lessons"][0]["interactive"]["steps"]:
            if s.get("kind") == "tapQuestion":
                s["options"].pop()
                return
    mutate("dropped a tapQuestion option", drop_option)

    def move_answer(m):
        for s in m["lessons"][0]["interactive"]["steps"]:
            if s.get("kind") == "tapQuestion":
                s["correctIndex"] = (s["correctIndex"] + 1) % len(s["options"])
                return
    mutate("moved the correct answer", move_answer)

    # And the freedoms the rewrite rule grants must NOT be flagged.
    def allowed(name, fn):
        m = copy.deepcopy(base)
        fn(m)
        v = compare(en, m)
        if v:
            failures.append(f"WRONGLY FLAGGED a permitted rewrite ({name}): {v[0][:90]}")

    allowed("rewrote a lesson title", lambda m: m["lessons"][0].__setitem__("title", "Огт өөр гарчиг"))
    allowed("changed the paragraph count", lambda m: m["lessons"][0]["concept"].append("Нэмэлт тайлбар."))
    allowed("removed a paragraph", lambda m: m["lessons"][0]["concept"].pop())
    allowed("rewrote a worked example's numbers",
            lambda m: m["lessons"][0]["workedExamples"][0].update(
                {"statement": "Өөр тоо", "solution": "Өөр бодолт", "check": ["Eq(1,1)"]}))
    allowed("changed the fact count", lambda m: m["lessons"][0]["facts"].pop())

    if failures:
        print("mn_skeleton selftest FAILED:")
        for f in failures:
            print("  " + f)
        return 1
    print("mn_skeleton selftest ok — 13 forbidden mutations caught, 5 permitted rewrites allowed through")
    return 0


def main() -> int:
    args = sys.argv[1:]
    if not args:
        raise SystemExit(__doc__)
    if args[0] == "--selftest":
        return selftest()

    if args[0] == "--all":
        targets = []
        for d in sorted(glob.glob(os.path.join(ROOT, "data", "genmath", "*-mn"))):
            corpus = os.path.basename(d)[:-3]
            for f in sorted(os.listdir(d)):
                if f.endswith(".json"):
                    targets.append((corpus, f[:-5]))
    else:
        targets = [(args[0], args[1])]

    total = 0
    warned = 0
    for corpus, slug in targets:
        bad, warn = check_topic(corpus, slug)
        warned += len(warn)
        if bad:
            total += len(bad)
            print(f"\n\u2717 {corpus}/{slug}")
            for b in bad:
                print(f"    {b}")
        if warn and len(targets) == 1:
            print(f"\n\u26a0 {corpus}/{slug} \u2014 renders as a literal asterisk (not fatal)")
            for w in warn:
                print(f"    {w}")
    tail = f" \u00b7 {warned} single-asterisk warning(s)" if warned else ""
    if total:
        print(f"\nmn_skeleton: {total} violation(s) across {len(targets)} topic(s){tail}")
        return 1
    print(f"mn_skeleton: {len(targets)} topic(s) structurally sound{tail}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
