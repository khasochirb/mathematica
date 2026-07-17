# -*- coding: utf-8 -*-
"""Problem-bank subject: Probability & Statistics — mirrors the /math/prob-stats course units.

All content is authored here (no legacy exam-topic forms to remap). Every
form carries a `unit` field matching the course spine, ~12 variants for the
reroll/retry pool, and an independent RESOLVERS re-solver used by
scripts/audit_problembank.py. Run `python3 scripts/pb/prob_stats.py` to
self-check.
"""
import re

from sympy import Rational, sympify

SLUG = "prob-stats"
TITLE = "Probability & Statistics"
TITLE_MN = "Магадлал ба статистик"
BLURB = ("Unit-by-unit practice for the Probability & Statistics course — counting to inference, every unit with its own exercise set.")

UNITS = [
    {"id": "counting-principles", "title": "Counting Principles",
     "blurb": "The multiplication and addition principles, complementary counting, and organized lists — how to count without counting."},
    {"id": "permutations", "title": "Permutations & Arrangements",
     "blurb": "Factorials, arrangements of all or some objects, repeated letters, and seating with restrictions."},
    {"id": "combinations", "title": "Combinations",
     "blurb": "Choosing without order: nCr, committees, at-least and at-most counts, and when order matters vs when it doesn't."},
    {"id": "binomial-theorem", "title": "Pascal's Triangle & the Binomial Theorem",
     "blurb": "The triangle that counts everything: binomial coefficients, expanding powers, and finding specific terms."},
    {"id": "probability-models", "title": "Probability Models",
     "blurb": "Sample spaces, events, equally-likely outcomes, complements, and the addition rule with Venn diagrams."},
    {"id": "conditional-probability", "title": "Conditional Probability & Independence",
     "blurb": "How information changes chance: P(A|B), the multiplication rule, independence, weighted trees, and Bayes by table."},
    {"id": "random-variables", "title": "Random Variables & Expected Value",
     "blurb": "Turning outcomes into numbers: probability distributions, expected value, variance, and what makes a game fair."},
    {"id": "binomial-distribution", "title": "The Binomial Distribution",
     "blurb": "Repeated independent trials: binomial probabilities, expected count np, shape, and simulation."},
    {"id": "describing-data", "title": "Describing Data",
     "blurb": "Center and spread done right: mean, median, IQR, standard deviation, boxplots, and the 1.5×IQR outlier fence."},
    {"id": "distributions-and-position", "title": "Distribution Shape & Position",
     "blurb": "Histograms and shape, percentiles, z-scores, and the normal curve with the 68–95–99.7 rule."},
    {"id": "two-variable-data", "title": "Two-Variable Data",
     "blurb": "Scatterplots, the correlation coefficient, the least-squares line, and why correlation is not causation."},
    {"id": "inference-and-studies", "title": "Sampling, Studies & Inference",
     "blurb": "Random sampling, bias, experiments vs observation, simulation-based inference, and margin of error — the capstone."},
]

# No legacy forms: this subject is authored fresh.
REMAP = {}
SOURCES = []

# form id -> fn(statement) -> ("num", sympy value) | ("opt", exact option str)
RESOLVERS = {}


def new_forms():
    """Unit-specific forms (filled by the authoring pass)."""
    return []


def build():
    unit_order = {u["id"]: i for i, u in enumerate(UNITS)}
    forms = new_forms()
    for f in forms:
        assert f["unit"] in unit_order, "%s: unknown unit %r" % (f["id"], f["unit"])
    forms.sort(key=lambda f: (unit_order[f["unit"]], f["level"], f["id"]))
    return {"slug": SLUG, "title": TITLE, "titleMn": TITLE_MN, "blurb": BLURB,
            "units": UNITS, "forms": forms}


if __name__ == "__main__":
    data = build()
    total = sum(len(f["variants"]) for f in data["forms"])
    per_unit = {u["id"]: 0 for u in UNITS}
    for f in data["forms"]:
        per_unit[f["unit"]] += len(f["variants"])
    ids = [v["id"] for f in data["forms"] for v in f["variants"]]
    assert len(ids) == len(set(ids)), "variant ids not unique"
    empty = [u for u, n in per_unit.items() if n == 0]
    print("SELFCHECK OK  forms=%d  total=%d  units=%d  empty_units=%s"
          % (len(data["forms"]), total, len(UNITS), ",".join(empty) or "none"))
