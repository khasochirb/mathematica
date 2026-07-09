"""Shared deterministic walker for MN translation (v2).

Both mn_extract.py and mn_apply.py import walk() from here, so the
visit order is identical by construction. v2 additions over the v1
grade-8 walker:
  - facts[].latex           (rendered via MathText -> prose/plain text)
  - workedExamples/tryIt/practice/testYourself [].note
  - per-widget-kind config prose (labels, units, notes shown on screen)

Functional config fields are deliberately NOT visited: mode, op, color,
place, varName, reflectAxis, knownSide, points[].label (point names),
dataset, pattern, and everything else not listed in WIDGET_PROSE.
"""
import re

def pure_math(s: str) -> bool:
    stripped = re.sub(r"\$[^$]*\$", "", s)
    return not re.search(r"[A-Za-z]", stripped)

# Per-widget config prose. Paths are dotted; "[]" walks a list.
# token expands to label+plural on that object.
TOKEN = ("label", "plural")
WIDGET_PROSE = {
    # grade 6
    "compareToggle":   ["groupA.token.label", "groupA.token.plural",
                        "groupB.token.label", "groupB.token.plural"],
    "dealCompare":     ["dealA.label", "dealB.label", "unit"],
    "fractionCompare": ["left.label", "right.label"],
    "ratioCompare":    ["left.label", "left.token.label", "left.token.plural",
                        "right.label", "right.token.label", "right.token.plural",
                        "unitNote"],
    "proportionBuilder": ["aLabel", "bLabel",
                          "tokenA.label", "tokenA.plural",
                          "tokenB.label", "tokenB.plural"],
    "rateMeter":       ["topLabel", "topUnit", "bottomLabel", "bottomUnit", "rateUnit"],
    "orderFlip":       ["forwardLabel", "flippedLabel",
                        "tokenA.label", "tokenA.plural",
                        "tokenB.label", "tokenB.plural"],
    "orderOfOps":      ["stages[].did"],
    "scaler":          ["goodLabel",
                        "tokenA.label", "tokenA.plural",
                        "tokenB.label", "tokenB.plural"],
    "notationToggle":  ["tokenA.label", "tokenA.plural",
                        "tokenB.label", "tokenB.plural"],
    "ratioTable":      ["tokenA.label", "tokenA.plural",
                        "tokenB.label", "tokenB.plural"],
    # grade 8
    "scatterPlot":     ["xLabel", "yLabel"],
    "trendLine":       ["xLabel", "yLabel"],
    "trendPredict":    ["xLabel", "yLabel"],
    "outlierSpot":     ["xLabel", "yLabel"],
}

def _config_paths(step, visit):
    """Visit declared prose paths inside step['config'] in declared order."""
    spec = WIDGET_PROSE.get(step.get("kind"))
    cfg = step.get("config")
    if not spec or not isinstance(cfg, dict):
        return
    def follow(obj, parts):
        if obj is None:
            return
        head, rest = parts[0], parts[1:]
        if head.endswith("[]"):
            lst = obj.get(head[:-2])
            if isinstance(lst, list):
                for item in lst:
                    if rest:
                        follow(item, rest)
        elif rest:
            follow(obj.get(head) if isinstance(obj, dict) else None, rest)
        else:
            if isinstance(obj, dict):
                visit(obj, head)
    for path in spec:
        follow(cfg, path.split("."))

def walk(topic, visit):
    """visit(obj, key) is called for every translatable slot in fixed order.
    The callback reads obj[key] and may replace it (apply mode)."""
    def t(obj, key):
        s = obj.get(key) if isinstance(obj, dict) else None
        if isinstance(s, str) and s and not pure_math(s):
            visit(obj, key)
    def t_list(obj, key):
        lst = obj.get(key)
        if isinstance(lst, list):
            for i, s in enumerate(lst):
                if isinstance(s, str) and s and not pure_math(s):
                    visit(lst, i)
    def t_figure(container):
        """On-screen prose inside an item's figure illustration (v3)."""
        fig = container.get("figure")
        if not isinstance(fig, dict):
            return
        for g in fig.get("groups", []):
            t(g, "label")
        for key in ("fraction", "decimal"):
            sub = fig.get(key)
            if isinstance(sub, dict):
                t(sub, "label")
        for m in fig.get("mixes", []):
            t(m, "label")
        nl = fig.get("numberLine")
        if isinstance(nl, dict):
            for p in nl.get("points", []):
                t(p, "label")
    def t_prob(p):
        t(p, "statement"); t(p, "solution"); t(p, "note")
    t(topic, "title"); t(topic, "blurb")
    for les in topic["lessons"]:
        t(les, "title"); t(les, "concreteComparison"); t(les, "objective")
        t_list(les, "concept"); t(les, "keyIdea")
        for f in les.get("facts", []):
            t(f, "title"); t(f, "explanation"); t(f, "latex")
        for p in les.get("workedExamples", []): t_prob(p)
        for m in les.get("commonMistakes", []):
            t(m, "text"); t(m, "correction")
        for p in les.get("tryIt", []): t_prob(p)
        for step in les.get("interactive", {}).get("steps", []):
            k = step["kind"]
            t(step, "eyebrow"); t(step, "title")
            if k == "teach":
                t_list(step, "beats")
                t_figure(step)
            elif k == "tapQuestion":
                t(step, "prompt"); t_list(step, "options"); t(step, "explanation")
                t_figure(step)
            elif k == "workedSet":
                t(step, "intro")
                for e in step.get("examples", []):
                    t(e, "prompt"); t_list(e, "steps"); t(e, "answer"); t(e, "note")
                    t_figure(e)
            elif k == "tryItSet":
                t(step, "intro")
                for p in step.get("problems", []):
                    t(p, "prompt"); t_list(p, "options"); t(p, "explanation"); t(p, "note")
                    t_figure(p)
            elif k in ("funFact", "tip"):
                t(step, "body")
            elif k == "recap":
                t_list(step, "points")
            else:  # widget step: teach line + declared config prose
                t(step, "teach")
                _config_paths(step, lambda obj, key: t(obj, key))
                t_figure(step)
    for p in topic.get("practice", []): t_prob(p)
    for p in topic.get("testYourself", []): t_prob(p)
