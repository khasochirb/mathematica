#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 5 — Topic 7: Geometry — Shapes & Area.

Angles as amounts of turn (with the right angle as benchmark and the
180/360 sums that find missing angles), classifying triangles and
quadrilaterals (and their angle sums), perimeter as the walk around,
area as the count of unit squares — and composite figures, where two
different roads (split, or subtract) must reach the same answer.

Through-line: MEASURE THE BOUNDARY, COUNT THE INSIDE. Perimeter walks
the edge in linear units; area tiles the inside in square units. Half
the errors in school geometry are these two ideas swapping places —
so this topic keeps them side by side and names the difference in
every lesson that touches them.

Same construction as the other Grade 5 builders: every check is
sympy-asserted with exact integers before the JSON is written. Angle
sums, perimeter walks and area tilings all carry their arithmetic as
checks; composite areas are checked down BOTH roads (split and
subtract), so the two methods are proven to agree before shipping.

Run: python3 scripts/grade4/build_geometry.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g5build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic)


# ==========================================================================
# Lesson 1 — Angles
# ==========================================================================

def lesson_angles():
    return {
        "slug": "angles",
        "title": "Angles",
        "concreteComparison": (
            "A ger door swings from closed to wide open — and how far "
            "it swung is an ANGLE: an amount of turn. The corner of "
            "this page turns a quarter of a full spin; we call that a "
            "right angle and give it $90$ degrees. Every other angle "
            "is measured against it: less than the corner is acute, "
            "more is obtuse, and half a full spin — the flat line — "
            "is $180^\\circ$."),
        "objective": (
            "Measure and classify angles in degrees against the "
            "right-angle benchmark, and find missing angles on a "
            "straight line and around a point."),
        "concept": [
            "**An angle is turn, not length.** Degrees count how far "
            "something turned: a full spin is $360^\\circ$, half a "
            "spin (a straight line) $180^\\circ$, a quarter (the "
            "page's corner) $90^\\circ$ — the RIGHT angle, geometry's "
            "benchmark.",
            "**Classify against the benchmark.** Acute: less than "
            "$90^\\circ$ (a sharp wedge). Obtuse: between $90^\\circ$ "
            "and $180^\\circ$ (a lazy recliner). The arms' LENGTH "
            "never matters — a tiny drawn angle of $120^\\circ$ still "
            "beats a huge drawn one of $45^\\circ$.",
            "**The two great sums.** Angles that fill a straight line "
            "total $180^\\circ$; angles that fill a full turn total "
            "$360^\\circ$. Both work as subtraction machines: a "
            "missing angle is the total minus the known ones — "
            "$180 - 65 = 115$.",
        ],
        "keyIdea": (
            "An angle measures turn, judged against the 90-degree "
            "right angle; straight lines carry 180 degrees and full "
            "turns 360, and missing angles fall out by subtraction."),
        "facts": [
            {"title": "The benchmarks",
             "latex": "\\text{right} = 90^\\circ \\quad \\text{straight} = 180^\\circ \\quad \\text{full turn} = 360^\\circ",
             "explanation": "Quarter, half, and whole of one spin — everything is measured against these."},
            {"title": "The subtraction machines",
             "latex": "\\text{on a line: } 180 - \\text{known} \\qquad \\text{around a point: } 360 - \\text{known}",
             "explanation": "Missing angles are totals minus the angles you can see."},
        ],
        "workedExamples": [
            {"id": "g5ge-l1-we1",
             "statement": "Two angles share a straight line; one measures $65^\\circ$. Find the other, and classify both.",
             "note": "The line carries 180 in total.",
             "solution": ("$180 - 65 = 115^\\circ$. The $65^\\circ$ angle is acute "
                          "(under $90$); the $115^\\circ$ angle is obtuse (between "
                          "$90$ and $180$). Check: $65 + 115 = 180$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(180 - 65, 115)", "65 < 90", "115 > 90", "115 < 180"]},
            {"id": "g5ge-l1-we2",
             "statement": "Three angles meet around a point: $140^\\circ$, $90^\\circ$, and one unknown. Find it.",
             "note": "A full turn carries 360.",
             "solution": ("$360 - 140 - 90 = 130^\\circ$ — obtuse. Check: $140 + 90 "
                          "+ 130 = 360$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(360 - 140 - 90, 130)", "Eq(140 + 90 + 130, 360)"]},
        ],
        "commonMistakes": [
            {"text": "Judging an angle by the length of its drawn arms.",
             "correction": "The arms are just rays — only the TURN between them counts. A 120° angle drawn small still beats a 45° angle drawn across the page.",
             "authored": True},
            {"text": "Using 360 for a straight line (or 180 for a full turn).",
             "correction": "A straight line is HALF a spin: 180°. Ask 'line or full turn?' before subtracting — the wrong total doubles or halves every answer.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5ge-l1-t1",
             "statement": "Classify: $38^\\circ$, $90^\\circ$, $155^\\circ$, $180^\\circ$.",
             "solution": "$38^\\circ$ acute; $90^\\circ$ right; $155^\\circ$ obtuse; $180^\\circ$ straight.",
             "check": ["38 < 90", "155 > 90", "155 < 180"]},
            {"id": "g5ge-l1-t2",
             "statement": "On a straight line, two equal angles sit side by side. How big is each?",
             "solution": "They share $180^\\circ$ equally: $180 \\div 2 = 90^\\circ$ each — two right angles, which is exactly what a perpendicular crossing makes.",
             "check": ["Eq(Rational(180,2), 90)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Turn, measured in degrees", [
                "An angle is an amount of TURN — the ger door swinging open, the clock hand sweeping. Degrees count the turn: a full spin is $360^\\circ$.",
                "The benchmarks: quarter spin $= 90^\\circ$ (the RIGHT angle — the page's corner), half spin $= 180^\\circ$ (a straight line).",
                "Classify against them: acute $< 90^\\circ$, obtuse between $90^\\circ$ and $180^\\circ$. Arm length is irrelevant — only the turn counts.",
            ]),
            workedset("Naming turns",
                      "Compare with 90 and 180; the arms' length never votes.", [
                wex("Classify $38^\\circ$, $90^\\circ$, $155^\\circ$, $180^\\circ$.",
                    ["$38 < 90$: acute. $90$: right, exactly.",
                     "$90 < 155 < 180$: obtuse. $180$: straight."],
                    "acute, right, obtuse, straight",
                    ["38 < 90", "155 > 90", "155 < 180"]),
                wex("Which is bigger: a $120^\\circ$ angle drawn with short arms, or a $45^\\circ$ angle drawn with long arms?",
                    ["Only the turn counts: $120 > 45$.",
                     "The short-armed angle wins — drawing size is a costume."],
                    "the $120^\\circ$ angle",
                    ["120 > 45"]),
            ]),
            tryitset("Benchmark judgments", "Under 90, exactly 90, or between 90 and 180?", [
                tp("An angle of $89^\\circ$ is:",
                   ["acute", "right", "obtuse"],
                   "One degree under the benchmark — still acute. Classification is exact, not approximate.",
                   ["89 < 90"]),
                tp("A clock's hands at 3:00 make an angle of:",
                   ["$90^\\circ$", "$180^\\circ$", "$60^\\circ$"],
                   "Quarter of the face — a right angle. (The full face is $360^\\circ$; each hour mark is $30^\\circ$, and three of them make $90$.)",
                   ["Eq(3*30, 90)", "Eq(Rational(360,12), 30)"]),
                tp("Half of a right angle measures:",
                   ["$45^\\circ$", "$60^\\circ$", "$25^\\circ$"],
                   "$90 \\div 2 = 45^\\circ$ — the diagonal-fold angle.",
                   ["Eq(Rational(90,2), 45)"]),
            ]),
            tapq("Costume check", "Two angles are drawn: one tiny with $130^\\circ$ of turn, one huge with $70^\\circ$. The bigger ANGLE is:",
                 ["the tiny drawing — $130^\\circ$ of turn",
                  "the huge drawing",
                  "they are equal",
                  "impossible to tell"],
                 "Angles measure turn, not ink: $130 > 70$, whatever the arm lengths. The drawing's size is a costume the angle wears.",
                 ["130 > 70"]),
            funfact("Why 360?",
                    "The Babylonians again (time's sixty-traders): $360$ divides cleanly by $2, 3, 4, 5, 6, 8, 9, 10, 12$ and more — so halves, thirds, quarters and fifths of a turn all come out whole. A decimal circle of $100^\\circ$ would make a third of a turn $33.33\\ldots$ — forever."),
            teach("Concept B", "The two great sums", [
                "Angles filling a STRAIGHT LINE total $180^\\circ$ — so a missing one is $180$ minus the known: $180 - 65 = 115^\\circ$.",
                "Angles filling a FULL TURN total $360^\\circ$: $360 - 140 - 90 = 130^\\circ$.",
                "Ask 'line or turn?' before subtracting — the totals are the whole method, and picking the wrong one doubles or halves everything.",
            ]),
            workedset("Subtraction machines",
                      "Total minus known = missing.", [
                wex("Two angles on a line; one is $65^\\circ$. The other?",
                    ["$180 - 65 = 115^\\circ$ — obtuse.",
                     "Check: $65 + 115 = 180$ ✓."],
                    "$115^\\circ$",
                    ["Eq(180 - 65, 115)"]),
                wex("Around a point: $140^\\circ$, $90^\\circ$, and one unknown.",
                    ["$360 - 140 - 90 = 130^\\circ$.",
                     "Check: the three total $360$ ✓."],
                    "$130^\\circ$",
                    ["Eq(360 - 140 - 90, 130)"]),
            ]),
            tryitset("Find the missing turn", "Line = 180; point = 360.", [
                tp("On a straight line, next to a $48^\\circ$ angle:",
                   ["$132^\\circ$", "$312^\\circ$", "$42^\\circ$"],
                   "$180 - 48 = 132^\\circ$. ($312$ used the full-turn total on a line.)",
                   ["Eq(180 - 48, 132)"]),
                tp("Around a point sit $100^\\circ$, $120^\\circ$, $85^\\circ$ and one more:",
                   ["$55^\\circ$", "$45^\\circ$", "$155^\\circ$"],
                   "$360 - 100 - 120 - 85 = 55^\\circ$.",
                   ["Eq(360 - 100 - 120 - 85, 55)"]),
                tp("Two equal angles fill a straight line. Each is:",
                   ["$90^\\circ$", "$180^\\circ$", "$45^\\circ$"],
                   "$180 \\div 2 = 90$ — a perpendicular crossing.",
                   ["Eq(Rational(180,2), 90)"]),
            ]),
            tapq("Line or turn?", "Four equal angles meet around a point. Each measures:",
                 ["$90^\\circ$", "$45^\\circ$", "$180^\\circ$", "$60^\\circ$"],
                 "The point carries $360$: $360 \\div 4 = 90^\\circ$ — four right angles, like the corners meeting at a window's cross-frame.",
                 ["Eq(Rational(360,4), 90)"]),
            recap([
                "An angle measures TURN in degrees; arm length never votes.",
                "Benchmarks: right 90°, straight 180°, full turn 360°.",
                "Acute is under 90; obtuse sits between 90 and 180.",
                "Missing angles: total (180 on a line, 360 at a point) minus the known.",
            ]),
            tip("For every missing angle, first say which total applies — 'line, 180' or 'point, 360' — then subtract. The naming is the method."),
            tryitset("Mixed practice", "Classifying and the two sums together.", [
                tp("An angle of $91^\\circ$ is:",
                   ["obtuse", "acute", "right"],
                   "One degree past the benchmark — obtuse. Exact boundaries, no rounding.",
                   ["91 > 90", "91 < 180"]),
                tp("On a line beside a right angle sits:",
                   ["another right angle", "an acute angle", "a straight angle"],
                   "$180 - 90 = 90^\\circ$ — right angles come in pairs on a line.",
                   ["Eq(180 - 90, 90)"]),
                tp("A pizza is cut into $8$ equal slices. Each slice's tip angle is:",
                   ["$45^\\circ$", "$60^\\circ$", "$36^\\circ$"],
                   "$360 \\div 8 = 45^\\circ$ per slice.",
                   ["Eq(Rational(360,8), 45)"]),
                tp("Around a point, three angles are $150^\\circ$, $150^\\circ$, and:",
                   ["$60^\\circ$", "$30^\\circ$", "$90^\\circ$"],
                   "$360 - 300 = 60^\\circ$.",
                   ["Eq(360 - 150 - 150, 60)"]),
                tp("The hands of a clock at 6:00 form:",
                   ["a straight angle — $180^\\circ$", "a right angle", "a full turn"],
                   "Opposite directions along one line: half a spin, $180^\\circ$ ($6 \\times 30$).",
                   ["Eq(6*30, 180)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Angles\"",
                    "Turn, benchmarks, and two subtraction machines. Next: the shapes those angles build — triangles and quadrilaterals, each carrying a fixed angle budget.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Triangles & Quadrilaterals
# ==========================================================================

def lesson_shapes():
    return {
        "slug": "triangles-and-quadrilaterals",
        "title": "Triangles & Quadrilaterals",
        "concreteComparison": (
            "Tear the three corners off ANY paper triangle and lay "
            "them side by side: they always build a straight line — "
            "$180^\\circ$, every triangle, every time. Shapes carry "
            "fixed angle budgets: triangles get $180^\\circ$ to share "
            "among three corners, quadrilaterals get $360^\\circ$ "
            "among four. Classifying shapes is reading how they spend "
            "it."),
        "objective": (
            "Classify triangles by sides and by angles, know the "
            "quadrilateral family, and use the angle budgets — 180 for "
            "triangles, 360 for quadrilaterals — to find missing "
            "angles."),
        "concept": [
            "**Triangles, by sides and by angles.** Sides: equilateral "
            "(all three equal), isosceles (two equal), scalene (none). "
            "Angles: right (one $90^\\circ$), acute (all under $90$), "
            "obtuse (one over). Every triangle earns one name from "
            "each list.",
            "**The 180 budget.** A triangle's three angles always "
            "total $180^\\circ$ — so the third is $180$ minus the two "
            "known: $180 - 90 - 35 = 55^\\circ$. An equilateral "
            "triangle splits the budget evenly: $60^\\circ$ each.",
            "**The quadrilateral family and its 360.** Squares are "
            "special rectangles; rectangles and rhombuses are special "
            "parallelograms; a trapezoid has just one parallel pair. "
            "All of them spend exactly $360^\\circ$: $360 - 90 - 90 - "
            "110 = 70^\\circ$.",
        ],
        "keyIdea": (
            "Shapes carry fixed angle budgets — 180 degrees for "
            "triangles, 360 for quadrilaterals — and their names "
            "describe how sides and angles spend it."),
        "facts": [
            {"title": "The budgets",
             "latex": "\\triangle: 180^\\circ \\qquad \\square: 360^\\circ",
             "explanation": "Three corners share 180; four corners share 360 — always."},
            {"title": "The family tree",
             "latex": "\\text{square} \\subset \\text{rectangle} \\subset \\text{parallelogram}",
             "explanation": "Every square is a rectangle; every rectangle is a parallelogram — special cases nest."},
        ],
        "workedExamples": [
            {"id": "g5ge-l2-we1",
             "statement": "A right triangle has one angle of $35^\\circ$. Find the third angle and classify the triangle by its angles.",
             "note": "Spend the 180 budget.",
             "solution": ("$180 - 90 - 35 = 55^\\circ$. One angle is exactly "
                          "$90^\\circ$, so it is a RIGHT triangle (the other two, "
                          "$35^\\circ$ and $55^\\circ$, are both acute — as they "
                          "must be, since only $90$ remains for them together)."),
             "badges": [{"text": "core"}],
             "check": ["Eq(180 - 90 - 35, 55)", "Eq(35 + 55, 90)"]},
            {"id": "g5ge-l2-we2",
             "statement": "A quadrilateral has angles $90^\\circ$, $90^\\circ$ and $110^\\circ$. Find the fourth.",
             "note": "Four corners share 360.",
             "solution": ("$360 - 90 - 90 - 110 = 70^\\circ$. Check: $90 + 90 + 110 "
                          "+ 70 = 360$ ✓. (Two right angles but not four — so this "
                          "is not a rectangle.)"),
             "badges": [{"text": "core"}],
             "check": ["Eq(360 - 90 - 90 - 110, 70)", "Eq(90 + 90 + 110 + 70, 360)"]},
        ],
        "commonMistakes": [
            {"text": "Refusing to call a square a rectangle.",
             "correction": "A rectangle needs four right angles — a square has them (plus equal sides as a bonus). Special cases BELONG to the family: every square is a rectangle, every rectangle a parallelogram.",
             "authored": True},
            {"text": "Using the 360 budget on a triangle.",
             "correction": "Three corners share 180, four share 360. Count the corners before subtracting — the wrong budget makes angles that cannot close.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5ge-l2-t1",
             "statement": "A triangle has angles $70^\\circ$ and $70^\\circ$. Find the third, and classify by sides and by angles.",
             "solution": "$180 - 70 - 70 = 40^\\circ$. Two equal angles mean two equal sides: isosceles; and all angles under $90$: acute.",
             "check": ["Eq(180 - 70 - 70, 40)", "70 < 90", "40 < 90"]},
            {"id": "g5ge-l2-t2",
             "statement": "Every angle of an equilateral triangle measures the same. How big is each?",
             "solution": "The budget splits three ways: $180 \\div 3 = 60^\\circ$ each.",
             "check": ["Eq(Rational(180,3), 60)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Triangles and their 180", [
                "Tear the corners off any paper triangle and line them up: a straight line — $180^\\circ$, always. That's the triangle's angle budget.",
                "Missing angles fall out by subtraction: a right triangle with a $35^\\circ$ corner keeps $180 - 90 - 35 = 55^\\circ$ for the third.",
                "Names: by sides — equilateral (three equal), isosceles (two), scalene (none); by angles — right, acute, obtuse. Every triangle gets one of each.",
            ]),
            workedset("Spending the 180",
                      "Budget minus known corners.", [
                wex("A right triangle has a $35^\\circ$ angle. The third?",
                    ["$180 - 90 - 35 = 55^\\circ$.",
                     "The two non-right corners always share exactly $90$: here $35 + 55$ ✓."],
                    "$55^\\circ$",
                    ["Eq(180 - 90 - 35, 55)"]),
                wex("An isosceles triangle has two $70^\\circ$ angles. The third — and the full classification?",
                    ["$180 - 140 = 40^\\circ$.",
                     "Isosceles (two equal sides) and acute (all corners under $90$)."],
                    "$40^\\circ$; isosceles acute",
                    ["Eq(180 - 70 - 70, 40)"]),
            ]),
            tryitset("Triangle budgets", "180, minus what you can see.", [
                tp("A triangle has angles $25^\\circ$ and $115^\\circ$. The third is:",
                   ["$40^\\circ$", "$50^\\circ$", "$220^\\circ$"],
                   "$180 - 25 - 115 = 40^\\circ$ — and the $115$ makes it an obtuse triangle.",
                   ["Eq(180 - 25 - 115, 40)", "115 > 90"]),
                tp("Each angle of an equilateral triangle is:",
                   ["$60^\\circ$", "$90^\\circ$", "$120^\\circ$"],
                   "$180 \\div 3 = 60^\\circ$ — the budget shared perfectly evenly.",
                   ["Eq(Rational(180,3), 60)"]),
                tp("Can a triangle have TWO right angles?",
                   ["no — they alone would spend the whole $180$, leaving nothing",
                    "yes — a rectangle-triangle", "only if it is isosceles"],
                   "$90 + 90 = 180$ uses the entire budget before the third corner exists. One right angle is the maximum.",
                   ["Eq(90 + 90, 180)"]),
            ]),
            tapq("Read the sides", "A triangle with sides $7$, $7$ and $4$ cm is:",
                 ["isosceles — exactly two sides equal", "equilateral", "scalene", "right"],
                 "Two sevens and a four: isosceles. (Side names and angle names are separate — this one could be acute or obtuse; the sides alone can't say.)",
                 ["Eq(7, 7)", "7 > 4"]),
            funfact("The torn-corners proof",
                    "The corner-tearing trick isn't just a demonstration — it IS the idea behind the real proof: the three angles reassemble along a straight line through the top vertex. You can do honest mathematics with a piece of paper and torn corners."),
            teach("Concept B", "The quadrilateral family", [
                "Four sides, four corners, $360^\\circ$ to spend. Missing angles: $360$ minus the rest — $360 - 90 - 90 - 110 = 70^\\circ$.",
                "The family nests: a PARALLELOGRAM has two parallel pairs; make its angles right and it's a RECTANGLE; make a rectangle's sides equal and it's a SQUARE. A RHOMBUS is a parallelogram with equal sides; a TRAPEZOID has just one parallel pair.",
                "Nesting means membership: every square IS a rectangle and IS a parallelogram — special cases don't leave the family, they lead it.",
            ]),
            workedset("Four corners, 360",
                      "Budgets and family memberships.", [
                wex("Angles $90^\\circ$, $90^\\circ$, $110^\\circ$ — the fourth?",
                    ["$360 - 290 = 70^\\circ$.",
                     "Not a rectangle: only two of the four corners are right."],
                    "$70^\\circ$",
                    ["Eq(360 - 90 - 90 - 110, 70)"]),
                wex("A parallelogram has one angle of $65^\\circ$. Its neighbour angle?",
                    ["Neighbouring angles of a parallelogram sit on a line of parallels: they total $180$.",
                     "$180 - 65 = 115^\\circ$ (and the opposite corner repeats the $65$)."],
                    "$115^\\circ$",
                    ["Eq(180 - 65, 115)", "Eq(2*65 + 2*115, 360)"]),
            ]),
            tryitset("Family business", "Budgets of 360; memberships that nest.", [
                tp("A quadrilateral has angles $80^\\circ$, $100^\\circ$, $95^\\circ$ and:",
                   ["$85^\\circ$", "$95^\\circ$", "$105^\\circ$"],
                   "$360 - 275 = 85^\\circ$.",
                   ["Eq(360 - 80 - 100 - 95, 85)"]),
                tp("Which statement is TRUE?",
                   ["every square is a rectangle", "every rectangle is a square", "no square is a parallelogram"],
                   "A square has four right angles — a rectangle's only requirement. The reverse fails: rectangles needn't have equal sides.",
                   ["Eq(4*90, 360)"]),
                tp("A shape with exactly ONE pair of parallel sides is a:",
                   ["trapezoid", "parallelogram", "rhombus"],
                   "One pair: trapezoid. (Two pairs makes the parallelogram family.)",
                   ["Eq(1 + 1, 2)"]),
            ]),
            tapq("The nested names", "A rhombus with four right angles is also called:",
                 ["a square", "a trapezoid", "impossible", "a scalene"],
                 "Equal sides (rhombus) + right angles (rectangle) = square — the shape at the top of the family tree wears every name below it.",
                 ["Eq(4*90, 360)"]),
            recap([
                "Triangle budget: 180°; quadrilateral budget: 360° — count corners first.",
                "Triangles take one name by sides (equilateral/isosceles/scalene) and one by angles (right/acute/obtuse).",
                "The family nests: square ⊂ rectangle ⊂ parallelogram; rhombus joins at the parallelogram level; trapezoid keeps one parallel pair.",
                "Two right angles use a triangle's whole budget — so at most one per triangle.",
            ]),
            tip("For each shape, name the budget aloud before subtracting — and for each family question, ask what the shape's requirements are, not what it looks like."),
            tryitset("Mixed practice", "Budgets, names, and the family tree.", [
                tp("A triangle has a $102^\\circ$ angle and a $39^\\circ$ angle. The third:",
                   ["$39^\\circ$ — it is isosceles", "$49^\\circ$", "$219^\\circ$"],
                   "$180 - 102 - 39 = 39^\\circ$: two equal angles — isosceles, and obtuse thanks to the $102$.",
                   ["Eq(180 - 102 - 39, 39)", "102 > 90"]),
                tp("Which triangle CANNOT exist?",
                   ["one with angles $90^\\circ, 50^\\circ, 50^\\circ$",
                    "one with angles $60^\\circ, 60^\\circ, 60^\\circ$",
                    "one with angles $20^\\circ, 30^\\circ, 130^\\circ$"],
                   "$90 + 50 + 50 = 190 \\ne 180$ — the budget doesn't close. The others total $180$ exactly.",
                   ["Eq(90 + 50 + 50, 190)", "Ne(190, 180)", "Eq(20 + 30 + 130, 180)"]),
                tp("A rectangle's four angles total:",
                   ["$360^\\circ$", "$180^\\circ$", "$400^\\circ$"],
                   "Four right angles: $4 \\times 90 = 360$ — the quadrilateral budget, spent entirely on corners.",
                   ["Eq(4*90, 360)"]),
                tp("A parallelogram has one angle of $70^\\circ$. Its four angles are:",
                   ["$70, 110, 70, 110$", "$70, 70, 70, 70$", "$70, 90, 70, 130$"],
                   "Opposites repeat, neighbours complete $180$: $70 + 110 + 70 + 110 = 360$ ✓.",
                   ["Eq(180 - 70, 110)", "Eq(70 + 110 + 70 + 110, 360)"]),
                tp("True or false: some trapezoids are parallelograms.",
                   ["false — one parallel pair, by definition, is not two",
                    "true — all of them are",
                    "true — the tall ones"],
                   "A trapezoid's defining feature is exactly ONE parallel pair; a parallelogram needs two. The definitions part ways.",
                   ["Ne(1, 2)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Triangles & Quadrilaterals\"",
                    "Angle budgets and a family tree — the naming half of geometry. Next: measuring the shapes themselves, starting with the walk around the edge.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Perimeter
# ==========================================================================

def lesson_perimeter():
    return {
        "slug": "perimeter",
        "title": "Perimeter",
        "concreteComparison": (
            "A herder fencing a rectangular paddock $8$ m by $5$ m "
            "doesn't need to guess the wire: walk the boundary — $8 + "
            "5 + 8 + 5 = 26$ m. Perimeter is exactly that walk, and "
            "the rectangle's shortcut $2 \\times (8 + 5)$ is just the "
            "walk noticing that opposite sides match."),
        "objective": (
            "Find perimeters of rectangles, squares and composite "
            "shapes by walking the boundary, use the rectangle "
            "shortcut, and work backwards to a missing side."),
        "concept": [
            "**Perimeter is the walk around.** Add EVERY side once — "
            "the fence's length, the frame's wood. Units are linear: "
            "metres, centimetres.",
            "**Rectangles shortcut it.** Opposite sides match, so $P = "
            "2 \\times (l + w)$: the $8 \\times 5$ paddock takes $2 "
            "\\times 13 = 26$ m. Squares compress further: $P = 4s$.",
            "**Backwards to a missing side.** Know $P = 30$ and $l = "
            "9$? Halve first — $l + w = 15$ — then $w = 15 - 9 = 6$. "
            "And on composite (L-shaped) walks, count EVERY edge, "
            "notches included: the walk doesn't skip the dent.",
        ],
        "keyIdea": (
            "Perimeter walks the whole boundary once — rectangles "
            "shortcut it as twice length-plus-width, and missing sides "
            "come from running the shortcut backwards."),
        "facts": [
            {"title": "The shortcuts",
             "latex": "P_{\\text{rect}} = 2(l + w) \\qquad P_{\\text{square}} = 4s",
             "explanation": "Opposite sides match; the walk folds in half (or quarters)."},
            {"title": "Backwards",
             "latex": "P = 30,\\ l = 9 \\ \\Rightarrow\\ w = \\tfrac{30}{2} - 9 = 6",
             "explanation": "Halve the perimeter to get one length-plus-width; subtract the known side."},
        ],
        "workedExamples": [
            {"id": "g5ge-l3-we1",
             "statement": "Find the perimeter of an $8$ m by $5$ m paddock, and of a square pen with $7$ m sides.",
             "note": "Walk it, then shortcut it.",
             "solution": ("Paddock: $8 + 5 + 8 + 5 = 26$ m — or the shortcut, $2 "
                          "\\times (8 + 5) = 26$ m. Square pen: $4 \\times 7 = 28$ "
                          "m."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8 + 5 + 8 + 5, 26)", "Eq(2*(8 + 5), 26)", "Eq(4*7, 28)"]},
            {"id": "g5ge-l3-we2",
             "statement": "A rectangle has perimeter $30$ cm and length $9$ cm. Find its width.",
             "note": "Halve first.",
             "solution": ("Half the walk covers one length and one width: $30 \\div "
                          "2 = 15$, so $w = 15 - 9 = 6$ cm. Check: $2 \\times (9 + "
                          "6) = 30$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(Rational(30,2), 15)", "Eq(15 - 9, 6)", "Eq(2*(9 + 6), 30)"]},
        ],
        "commonMistakes": [
            {"text": "Adding only the two labelled sides — P of an 8 × 5 rectangle as 13.",
             "correction": "The walk passes FOUR sides: 8 + 5 + 8 + 5. The shortcut 2(l + w) has the ×2 precisely because labels show only half the boundary.",
             "authored": True},
            {"text": "Forgetting to halve when working backwards — w = 30 − 9 = 21.",
             "correction": "P covers TWO lengths and TWO widths. Halve first (l + w = 15), then subtract: w = 6. A 21-wide rectangle would need P = 60.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5ge-l3-t1",
             "statement": "A photo frame is $24$ cm by $18$ cm. How much wooden edging does it need?",
             "solution": "$2 \\times (24 + 18) = 2 \\times 42 = 84$ cm of edging.",
             "check": ["Eq(2*(24 + 18), 84)"]},
            {"id": "g5ge-l3-t2",
             "statement": "A square garden takes $36$ m of fence. How long is each side?",
             "solution": "$36 \\div 4 = 9$ m per side. Check: $4 \\times 9 = 36$ ✓.",
             "check": ["Eq(Rational(36,4), 9)", "Eq(4*9, 36)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Walk the boundary", [
                "Perimeter is the walk around the edge — every side once, in linear units (m, cm).",
                "Rectangles shortcut the walk: opposite sides match, so $P = 2(l + w)$ — the $8 \\times 5$ paddock takes $2 \\times 13 = 26$ m of fence.",
                "Squares compress it further: four equal sides, $P = 4s$.",
            ]),
            workedset("Fences and frames",
                      "Walk, or shortcut — same wire.", [
                wex("Perimeter of an $8 \\times 5$ paddock and a $7$ m square pen.",
                    ["Paddock: $2(8 + 5) = 26$ m.",
                     "Pen: $4 \\times 7 = 28$ m."],
                    "$26$ m and $28$ m",
                    ["Eq(2*(8 + 5), 26)", "Eq(4*7, 28)"]),
                wex("Edging for a $24 \\times 18$ cm frame.",
                    ["$2 \\times (24 + 18) = 2 \\times 42 = 84$ cm."],
                    "$84$ cm",
                    ["Eq(2*(24 + 18), 84)"]),
            ]),
            tryitset("Boundary walks", "Every side once; shortcut when sides repeat.", [
                tp("A $12 \\times 7$ m garden's perimeter is:",
                   ["$38$ m", "$19$ m", "$84$ m"],
                   "$2(12 + 7) = 38$ m. ($19$ walked only half; $84$ multiplied — that's the area's business.)",
                   ["Eq(2*(12 + 7), 38)"]),
                tp("A square tile of side $15$ cm has perimeter:",
                   ["$60$ cm", "$30$ cm", "$225$ cm"],
                   "$4 \\times 15 = 60$ cm. ($225$ is the area again, sneaking in.)",
                   ["Eq(4*15, 60)", "Eq(15*15, 225)"]),
                tp("A triangle with sides $9$, $12$ and $15$ cm has perimeter:",
                   ["$36$ cm", "$27$ cm", "$54$ cm"],
                   "No shortcut for scalene sides — walk all three: $9 + 12 + 15 = 36$ cm.",
                   ["Eq(9 + 12 + 15, 36)"]),
            ]),
            tapq("Half a walk", "A student finds the perimeter of an $8 \\times 5$ rectangle as $8 + 5 = 13$. The slip:",
                 ["only half the boundary was walked — four sides make $26$",
                  "the sides were multiplied",
                  "nothing — $13$ is right",
                  "the units are wrong"],
                 "The label shows one length and one width, but the walk passes TWO of each: $2 \\times 13 = 26$. The shortcut's $\\times 2$ exists exactly for this.",
                 ["Eq(2*(8 + 5), 26)", "Ne(13, 26)"]),
            funfact("The fence-post problem",
                    "Fencing a $26$ m perimeter with posts every metre needs exactly $26$ posts, not $27$ — on a CLOSED loop the last post is the first one. On a straight $26$ m fence you'd need $27$. Boundary problems care whether the walk comes home."),
            teach("Concept B", "Backwards, and around the notch", [
                "Missing sides run the shortcut backwards: $P = 30$, $l = 9$ — halve first ($l + w = 15$), then $w = 6$.",
                "Squares: $P = 36$ gives $s = 9$ in one division.",
                "Composite shapes have no shortcut — walk EVERY edge, notches included. An L-shaped walk turns six corners, and each little edge counts.",
            ]),
            workedset("Running it backwards",
                      "Halve, subtract; or divide by four.", [
                wex("$P = 30$ cm, length $9$ cm — the width?",
                    ["Halve: $l + w = 15$.",
                     "$w = 15 - 9 = 6$ cm; check $2(9 + 6) = 30$ ✓."],
                    "$6$ cm",
                    ["Eq(15 - 9, 6)", "Eq(2*(9 + 6), 30)"]),
                wex("A square garden takes $36$ m of fence. Each side?",
                    ["$36 \\div 4 = 9$ m."],
                    "$9$ m",
                    ["Eq(Rational(36,4), 9)"]),
            ]),
            tryitset("Missing pieces", "Halve for rectangles; quarter for squares.", [
                tp("$P = 44$ m, width $8$ m. The length is:",
                   ["$14$ m", "$36$ m", "$28$ m"],
                   "$44 \\div 2 = 22$; $22 - 8 = 14$ m. ($36$ forgot to halve.)",
                   ["Eq(Rational(44,2) - 8, 14)", "Eq(2*(14 + 8), 44)"]),
                tp("A square with perimeter $52$ cm has sides of:",
                   ["$13$ cm", "$26$ cm", "$48$ cm"],
                   "$52 \\div 4 = 13$ cm.",
                   ["Eq(Rational(52,4), 13)"]),
                tp("An L-shaped path has six edges: $10, 4, 6, 3, 4, 7$ m. Its perimeter is:",
                   ["$34$ m", "$30$ m", "$27$ m"],
                   "Walk them all: $10 + 4 + 6 + 3 + 4 + 7 = 34$ m — the notch's little edges count too.",
                   ["Eq(10 + 4 + 6 + 3 + 4 + 7, 34)"]),
            ]),
            tapq("The forgotten halving", "$P = 40$ and $l = 12$: a student writes $w = 40 - 12 = 28$. The check $2(12 + 28)$ gives:",
                 ["$80$ — twice the stated perimeter, so the halving was skipped",
                  "$40$ — the answer stands",
                  "$56$",
                  "$28$"],
                 "$2 \\times 40 = 80 \\ne 40$: the receipt fails. Halve first: $l + w = 20$, so $w = 8$ (and $2 \\times 20 = 40$ ✓).",
                 ["Eq(2*(12 + 28), 80)", "Ne(80, 40)", "Eq(2*(12 + 8), 40)"]),
            recap([
                "Perimeter walks every side once — linear units.",
                "Rectangle shortcut: 2(l + w); square: 4s.",
                "Backwards: halve the perimeter, then subtract the known side.",
                "Composite shapes: no shortcut — walk every edge, notches included.",
            ]),
            tip("Receipt every backwards answer by rebuilding the perimeter — the forgotten halving fails its receipt instantly."),
            tryitset("Mixed practice", "Walks, shortcuts, and backwards runs.", [
                tp("A $30 \\times 20$ m yard needs how much fencing?",
                   ["$100$ m", "$50$ m", "$600$ m"],
                   "$2(30 + 20) = 100$ m. ($600$ is the area trying to buy fence.)",
                   ["Eq(2*(30 + 20), 100)"]),
                tp("An equilateral triangle of side $14$ cm has perimeter:",
                   ["$42$ cm", "$28$ cm", "$196$ cm"],
                   "$3 \\times 14 = 42$ cm.",
                   ["Eq(3*14, 42)"]),
                tp("$P = 50$ cm and the length is $15$ cm. The width:",
                   ["$10$ cm", "$35$ cm", "$20$ cm"],
                   "$25 - 15 = 10$ cm; receipt $2(15 + 10) = 50$ ✓.",
                   ["Eq(Rational(50,2) - 15, 10)", "Eq(2*(15 + 10), 50)"]),
                tp("A running track goes around a $90 \\times 60$ m field. Four laps cover:",
                   ["$1\\,200$ m", "$300$ m", "$600$ m"],
                   "One lap: $2(90 + 60) = 300$ m; four: $1\\,200$ m — 1.2 km.",
                   ["Eq(2*(90 + 60), 300)", "Eq(4*300, 1200)"]),
                tp("Which rectangle does NOT have perimeter $24$?",
                   ["$8 \\times 3$", "$7 \\times 5$", "$10 \\times 2$"],
                   "$2(8+3) = 22$ — short by two. The others: $2(7+5) = 24$ ✓ and $2(10+2) = 24$ ✓.",
                   ["Eq(2*(8 + 3), 22)", "Eq(2*(7 + 5), 24)", "Eq(2*(10 + 2), 24)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Perimeter\"",
                    "The boundary is measured; next we count what's INSIDE it — and discover that two rectangles with the same fence can hold very different fields.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Area of Rectangles
# ==========================================================================

def lesson_area():
    return {
        "slug": "area-of-rectangles",
        "title": "Area of Rectangles",
        "concreteComparison": (
            "Tiling a floor with $1$-metre-square carpet tiles: an $8 "
            "\\times 5$ room takes $8$ tiles per row, $5$ rows — $40$ "
            "tiles. AREA is that count of unit squares, and $l \\times "
            "w$ is just rows-times-row-length: multiplication's array "
            "picture laid on the floor."),
        "objective": (
            "Find areas of rectangles and squares in square units, "
            "keep area's units distinct from perimeter's, work back to "
            "a missing side, and see that equal perimeters can hold "
            "different areas."),
        "concept": [
            "**Area counts unit squares.** An $8 \\times 5$ m room "
            "holds $8 \\times 5 = 40$ one-metre squares: $40$ m². The "
            "formula IS the tiling — rows times row-length.",
            "**Square units, not linear ones.** Perimeter answers in "
            "m (a length of fence); area answers in m² (a count of "
            "tiles). Writing $40$ m for an area is the units trap — "
            "the little $^2$ records that tiles are squares.",
            "**Same fence, different fields.** $6 \\times 4$ and $8 "
            "\\times 2$ both take $20$ m of fence — but hold $24$ m² "
            "and $16$ m². Perimeter does not determine area; among "
            "rectangles with equal perimeter, the SQUARE holds the "
            "most.",
        ],
        "keyIdea": (
            "Area is the count of unit squares — length times width, "
            "answered in square units — and rectangles sharing a "
            "perimeter can hold very different areas."),
        "facts": [
            {"title": "The tiling formula",
             "latex": "A_{\\text{rect}} = l \\times w \\qquad A_{\\text{square}} = s^2",
             "explanation": "Rows times row-length — multiplication's array on the floor."},
            {"title": "Same fence, different fields",
             "latex": "6 \\times 4: P = 20,\\ A = 24 \\qquad 8 \\times 2: P = 20,\\ A = 16",
             "explanation": "Equal perimeters, unequal areas — the squarer shape holds more."},
        ],
        "workedExamples": [
            {"id": "g5ge-l4-we1",
             "statement": "A room is $8$ m by $5$ m. How many $1$ m² carpet tiles cover it — and what are the room's area and perimeter, with correct units?",
             "note": "Keep the two measures side by side.",
             "solution": ("Tiles: $8$ per row, $5$ rows — $8 \\times 5 = 40$ tiles, "
                          "so the area is $40$ m². The perimeter is $2(8 + 5) = 26$ "
                          "m — metres of skirting board, not tiles. Two different "
                          "questions, two different units."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*5, 40)", "Eq(2*(8 + 5), 26)"]},
            {"id": "g5ge-l4-we2",
             "statement": "Compare the $6 \\times 4$ and $8 \\times 2$ rectangles: perimeter and area of each.",
             "note": "Same fence, different fields.",
             "solution": ("Perimeters: $2(6+4) = 20$ and $2(8+2) = 20$ — identical "
                          "fences. Areas: $24$ m² against $16$ m² — the squarer "
                          "shape holds $8$ m² more. Perimeter does not decide "
                          "area."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*(6 + 4), 20)", "Eq(2*(8 + 2), 20)",
                       "Eq(6*4, 24)", "Eq(8*2, 16)", "24 > 16"]},
        ],
        "commonMistakes": [
            {"text": "Answering area in linear units — \"the area is 40 m\".",
             "correction": "Area counts SQUARES: 40 m². The exponent isn't decoration — it says what kind of thing was counted (tiles, not fence).",
             "authored": True},
            {"text": "Assuming equal perimeters mean equal areas.",
             "correction": "6 × 4 and 8 × 2 share a 20 m fence but hold 24 and 16 m². Fence length constrains, it doesn't determine — the squarer rectangle always holds more.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5ge-l4-t1",
             "statement": "A courtyard is $12$ m by $9$ m. Find its area and its perimeter, with units.",
             "solution": "Area: $12 \\times 9 = 108$ m². Perimeter: $2(12 + 9) = 42$ m.",
             "check": ["Eq(12*9, 108)", "Eq(2*(12 + 9), 42)"]},
            {"id": "g5ge-l4-t2",
             "statement": "A rectangle has area $72$ cm² and length $9$ cm. Find its width.",
             "solution": "$w = 72 \\div 9 = 8$ cm. Receipt: $9 \\times 8 = 72$ ✓.",
             "check": ["Eq(Rational(72,9), 8)", "Eq(9*8, 72)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Count the tiles", [
                "Cover a floor with $1$-metre squares: $8$ per row, $5$ rows — $40$ tiles. AREA is that count: $A = l \\times w = 40$ m².",
                "The unit is a SQUARE metre — a tile one metre on each side. The little $^2$ records what was counted.",
                "Squares tile as $s \\times s = s^2$: a $15$ cm square tile covers $225$ cm².",
            ]),
            workedset("Tiling floors",
                      "Rows times row-length; units squared.", [
                wex("Area and perimeter of an $8 \\times 5$ m room.",
                    ["Area: $8 \\times 5 = 40$ m² — forty tiles.",
                     "Perimeter: $2(8+5) = 26$ m — skirting board. Different questions, different units."],
                    "$40$ m², $26$ m",
                    ["Eq(8*5, 40)", "Eq(2*(8 + 5), 26)"]),
                wex("Area of a $12 \\times 9$ m courtyard.",
                    ["$12 \\times 9 = 108$ m²."],
                    "$108$ m²",
                    ["Eq(12*9, 108)"]),
            ]),
            tryitset("Tile counts", "Multiply; answer in square units.", [
                tp("A $7 \\times 6$ m floor has area:",
                   ["$42$ m²", "$26$ m²", "$42$ m"],
                   "$7 \\times 6 = 42$ — square metres, because tiles were counted. ($26$ m is the perimeter crashing the party; $42$ m wears the wrong unit.)",
                   ["Eq(7*6, 42)", "Eq(2*(7 + 6), 26)"]),
                tp("A square window of side $9$ dm has area:",
                   ["$81$ dm²", "$36$ dm²", "$18$ dm²"],
                   "$9^2 = 81$ dm². ($36$ is its perimeter.)",
                   ["Eq(9*9, 81)", "Eq(4*9, 36)"]),
                tp("A rectangle of area $72$ cm² and length $9$ cm has width:",
                   ["$8$ cm", "$63$ cm", "$27$ cm"],
                   "$72 \\div 9 = 8$; receipt $9 \\times 8 = 72$ ✓ — division undoes the tiling.",
                   ["Eq(Rational(72,9), 8)"]),
            ]),
            tapq("The units trap", "\"The garden's area is $54$ m\" — what's wrong?",
                 ["areas count squares: it should be $54$ m²",
                  "the number is too big",
                  "areas need kilometres",
                  "nothing"],
                 "$54$ METRES is a length — a fence, a walk. The garden's inside was counted in square-metre tiles: $54$ m². The exponent is the receipt for WHAT was counted.",
                 ["Eq(6*9, 54)"]),
            funfact("A hectare is a square you can see",
                    "Land is measured in hectares: one hectare is a $100 \\times 100$ m square — $10\\,000$ m², about a large sports field. A herder family's winter pasture might span hundreds of them."),
            teach("Concept B", "Same fence, different fields", [
                "Two rectangles can share a fence and disagree about their fields: $6 \\times 4$ and $8 \\times 2$ both take $20$ m — but hold $24$ m² and $16$ m².",
                "Stretch a rectangle thinner at fixed perimeter and its area DRAINS: $9 \\times 1$ holds just $9$ m² of the same $20$ m fence.",
                "Among equal-perimeter rectangles the SQUARE holds the most: $5 \\times 5 = 25$ m² tops them all. Fence constrains; shape decides.",
            ]),
            workedset("The 20-metre family",
                      "One fence, many fields.", [
                wex("Compare $6 \\times 4$ and $8 \\times 2$ on a $20$ m fence.",
                    ["Both: $P = 20$ m. Areas: $24$ and $16$ m².",
                     "The squarer shape holds $8$ m² more."],
                    "$24$ m² beats $16$ m²",
                    ["Eq(2*(6 + 4), 20)", "Eq(2*(8 + 2), 20)", "24 > 16"]),
                wex("Best rectangle on that same fence?",
                    ["$5 \\times 5$: still $P = 20$, area $25$ m².",
                     "The square — always the biggest field for the fence."],
                    "the $5 \\times 5$ square, $25$ m²",
                    ["Eq(2*(5 + 5), 20)", "Eq(5*5, 25)", "25 > 24"]),
            ]),
            tryitset("Fence economics", "Fix the perimeter; watch the area move.", [
                tp("Which holds MORE on a $24$ m fence: $8 \\times 4$ or $10 \\times 2$?",
                   ["$8 \\times 4$ — $32$ m² against $20$ m²", "$10 \\times 2$", "equal"],
                   "Both walk $24$ m; the fields differ: $32$ vs $20$ m².",
                   ["Eq(2*(8 + 4), 24)", "Eq(2*(10 + 2), 24)", "Eq(8*4, 32)",
                    "Eq(10*2, 20)", "32 > 20"]),
                tp("The BIGGEST rectangular field a $24$ m fence can hold is:",
                   ["$6 \\times 6 = 36$ m²", "$8 \\times 4 = 32$ m²", "$11 \\times 1 = 11$ m²"],
                   "The square again: $2(6+6) = 24$ and $36$ m² — more than any longer-thinner cousin.",
                   ["Eq(2*(6 + 6), 24)", "Eq(6*6, 36)", "36 > 32"]),
                tp("Two rectangles have the same AREA of $36$ cm²: $6 \\times 6$ and $12 \\times 3$. Their perimeters:",
                   ["differ — $24$ cm against $30$ cm", "are equal", "cannot be found"],
                   "Same field, different fences: the thin one walks farther. (The coin has two sides.)",
                   ["Eq(6*6, 36)", "Eq(12*3, 36)", "Eq(2*(6 + 6), 24)", "Eq(2*(12 + 3), 30)"]),
            ]),
            tapq("Fence vs field", "A farmer with $40$ m of fence wants the biggest rectangular plot. She should build:",
                 ["a $10 \\times 10$ square — $100$ m²",
                  "a $15 \\times 5$ rectangle — $75$ m²",
                  "an $18 \\times 2$ strip — $36$ m²",
                  "any shape — they're all equal"],
                 "All three use the $40$ m fence, but the square's field crushes the strip's: $100$ vs $36$ m². Squareness pays.",
                 ["Eq(2*(10 + 10), 40)", "Eq(10*10, 100)", "Eq(18*2, 36)", "100 > 36"]),
            recap([
                "Area = count of unit squares = l × w, answered in square units.",
                "Perimeter is fence (m); area is tiles (m²) — the exponent is the receipt.",
                "Missing side: divide the area by the known side.",
                "Equal fences can hold unequal fields; the square holds the most.",
            ]),
            tip("Write the unit BEFORE computing each answer — deciding 'm or m²?' first makes the fence/field confusion impossible."),
            tryitset("Mixed practice", "Fields, fences, and the difference.", [
                tp("A $15 \\times 4$ m corridor has area:",
                   ["$60$ m²", "$38$ m²", "$19$ m²"],
                   "$15 \\times 4 = 60$ m². ($38$ m is its perimeter.)",
                   ["Eq(15*4, 60)", "Eq(2*(15 + 4), 38)"]),
                tp("A square field of area $49$ m² has sides of:",
                   ["$7$ m", "$12.25$ m", "$24.5$ m"],
                   "$7 \\times 7 = 49$: seven metres.",
                   ["Eq(7*7, 49)"]),
                tp("Compare a $9 \\times 4$ board and an $8 \\times 5$ board. Which statement is true?",
                   ["$9 \\times 4$ has more area",
                    "the two boards have equal areas",
                    "$8 \\times 5$ has more area for the same perimeter"],
                   "Areas: $36$ vs $40$ — $8 \\times 5$ paints more. Perimeters: $26$ vs $26$ — equal tape! Same fence, different fields, live on a workbench.",
                   ["Eq(9*4, 36)", "Eq(8*5, 40)", "Eq(2*(9 + 4), 26)", "Eq(2*(8 + 5), 26)"],
                   correct=2),
                tp("A room of $5 \\times 4$ m is carpeted with $1$ m² tiles costing $8\\,000$ tögrög each. The carpet costs:",
                   ["$160\\,000$ tögrög", "$144\\,000$ tögrög", "$72\\,000$ tögrög"],
                   "$20$ tiles at $8\\,000$: $160\\,000$ tögrög.",
                   ["Eq(5*4, 20)", "Eq(20*8000, 160000)"]),
                tp("Doubling BOTH sides of a $6 \\times 3$ rectangle multiplies its area by:",
                   ["$4$", "$2$", "$8$"],
                   "$6 \\times 3 = 18$; doubled, $12 \\times 6 = 72 = 4 \\times 18$. Two doublings compound — one per direction.",
                   ["Eq(6*3, 18)", "Eq(12*6, 72)", "Eq(72, 4*18)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Area of Rectangles\"",
                    "Tiles counted, units disciplined, and the fence/field distinction earned. Finale: shapes made of several rectangles — where two different roads must meet at one answer.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Composite Areas
# ==========================================================================

def lesson_composite():
    return {
        "slug": "composite-areas",
        "title": "Composite Areas",
        "concreteComparison": (
            "An L-shaped room — a rectangle with a corner bitten out — "
            "has no single formula. But two roads reach its area: CUT "
            "it into two rectangles and add, or take the FULL rectangle "
            "and subtract the bite. Both roads must land on the same "
            "number; when they do, you've proof-read your own answer."),
        "objective": (
            "Find areas of L-shaped and composite rectilinear figures "
            "by splitting into rectangles or subtracting the missing "
            "piece, recover unlabelled side lengths, and keep composite "
            "area and perimeter separate."),
        "concept": [
            "**Road one: split and add.** Cut the L into two "
            "rectangles, area each, add. An $8 \\times 6$ room with a "
            "$3 \\times 2$ corner bite splits into $8 \\times 4$ and "
            "$5 \\times 2$: $32 + 10 = 42$ m².",
            "**Road two: fill and subtract.** Restore the full $8 "
            "\\times 6$ rectangle ($48$ m²), subtract the bite ($3 "
            "\\times 2 = 6$): $48 - 6 = 42$ m². Two roads, one "
            "answer — and the agreement is your receipt.",
            "**Unlabelled sides come from the labels.** Opposite "
            "spans must match: if the top edge is $8$ and one lower "
            "piece is $3$, the other is $8 - 3 = 5$. Every missing "
            "edge is a difference of labelled ones.",
        ],
        "keyIdea": (
            "Composite areas travel two roads — split-and-add or "
            "fill-and-subtract — and the roads must agree; missing "
            "edges are differences of the labelled ones."),
        "facts": [
            {"title": "Two roads",
             "latex": "\\text{split: } 32 + 10 = 42 \\qquad \\text{subtract: } 48 - 6 = 42",
             "explanation": "Add the pieces, or remove the bite — agreement is the receipt."},
            {"title": "Missing edges",
             "latex": "8 - 3 = 5",
             "explanation": "Opposite spans match; unlabelled sides are differences of labelled ones."},
        ],
        "workedExamples": [
            {"id": "g5ge-l5-we1",
             "statement": ("An L-shaped room is an $8 \\times 6$ m rectangle with a "
                           "$3 \\times 2$ m bite out of one corner. Find its area by "
                           "BOTH roads."),
             "note": "Split-and-add, then fill-and-subtract.",
             "solution": ("Split: a full-width $8 \\times 4$ strip ($32$) plus the "
                          "remaining $5 \\times 2$ strip ($10$ — its width is $8 - "
                          "3 = 5$): $42$ m². Subtract: $8 \\times 6 = 48$ minus the "
                          "$3 \\times 2 = 6$ bite: $42$ m². The roads agree — "
                          "that's the receipt."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8*4, 32)", "Eq(8 - 3, 5)", "Eq(5*2, 10)",
                       "Eq(32 + 10, 42)", "Eq(8*6 - 3*2, 42)"]},
            {"id": "g5ge-l5-we2",
             "statement": ("A T-shaped stage is a $10 \\times 3$ m bar on top of a "
                           "$4 \\times 5$ m stem. Find its area, and note which road "
                           "you used."),
             "note": "This one splits naturally — there's no simple surrounding rectangle.",
             "solution": ("Split: bar $10 \\times 3 = 30$; stem $4 \\times 5 = 20$; "
                          "total $50$ m². (Fill-and-subtract works too but needs a "
                          "$10 \\times 8$ surround minus two $3 \\times 5$ "
                          "shoulders: $80 - 30 = 50$ — same answer, longer road.)"),
             "badges": [{"text": "core"}],
             "check": ["Eq(10*3, 30)", "Eq(4*5, 20)", "Eq(30 + 20, 50)",
                       "Eq(10*8 - 2*3*5, 50)"]},
        ],
        "commonMistakes": [
            {"text": "Multiplying the two biggest labels — the L-shape as 8 × 6 = 48.",
             "correction": "48 is the FULL rectangle; the bite must leave. Either subtract it (48 − 6) or split honestly — the L holds 42.",
             "authored": True},
            {"text": "Double-counting the overlap when splitting.",
             "correction": "The cut pieces must not overlap: an 8 × 4 strip plus a 5 × 2 strip tile the L exactly. If your pieces share squares, the sum overshoots.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g5ge-l5-t1",
             "statement": ("A $9 \\times 7$ m yard has a $4 \\times 3$ m shed in one "
                           "corner. How much OPEN yard remains?"),
             "solution": "Fill-and-subtract: $63 - 12 = 51$ m² of open yard.",
             "check": ["Eq(9*7, 63)", "Eq(4*3, 12)", "Eq(63 - 12, 51)"]},
            {"id": "g5ge-l5-t2",
             "statement": ("An L-shape's top edge is $12$ m; the lower-right piece's "
                           "top is $7$ m. How long is the unlabelled upper-left "
                           "span?"),
             "solution": "Opposite spans match: $12 - 7 = 5$ m.",
             "check": ["Eq(12 - 7, 5)"]},
        ],
        "interactive": {"steps": [
            teach("Concept A", "Two roads to one answer", [
                "An L-shape has no formula — but two roads reach it. SPLIT: cut into rectangles, add the pieces: $8 \\times 4$ plus $5 \\times 2$ gives $32 + 10 = 42$ m².",
                "FILL AND SUBTRACT: restore the whole $8 \\times 6$ ($48$), remove the $3 \\times 2$ bite ($6$): $42$ m².",
                "The roads MUST agree — and when they do, you've proof-read your own answer. Take both roads whenever the stakes are real.",
            ]),
            workedset("Both roads, every time",
                      "Split-and-add against fill-and-subtract.", [
                wex("The $8 \\times 6$ room with a $3 \\times 2$ bite.",
                    ["Split: $32 + 10 = 42$ m² (the $10$-strip's width is $8 - 3 = 5$).",
                     "Subtract: $48 - 6 = 42$ m². Agreement ✓."],
                    "$42$ m²",
                    ["Eq(32 + 10, 42)", "Eq(8*6 - 3*2, 42)"]),
                wex("A $9 \\times 7$ yard minus a $4 \\times 3$ shed.",
                    ["$63 - 12 = 51$ m² of open ground."],
                    "$51$ m²",
                    ["Eq(9*7 - 4*3, 51)"]),
            ]),
            tryitset("Pick a road", "Either works; agreement is the receipt.", [
                tp("A $10 \\times 8$ hall with a $4 \\times 2$ alcove REMOVED has area:",
                   ["$72$ m²", "$80$ m²", "$64$ m²"],
                   "$80 - 8 = 72$ m². ($80$ forgot the alcove ever left.)",
                   ["Eq(10*8 - 4*2, 72)"]),
                tp("An L-shape splits into $6 \\times 3$ and $4 \\times 2$ pieces. Its area is:",
                   ["$26$ m²", "$24$ m²", "$48$ m²"],
                   "$18 + 8 = 26$ m².",
                   ["Eq(6*3 + 4*2, 26)"]),
                tp("A U-shaped counter is a $12 \\times 5$ slab with a $6 \\times 3$ notch cut from one long side. Its area:",
                   ["$42$ m²", "$60$ m²", "$18$ m²"],
                   "$60 - 18 = 42$ m².",
                   ["Eq(12*5 - 6*3, 42)"]),
            ]),
            tapq("The lazy rectangle", "A student answers the L-shape (an $8 \\times 6$ with a $3 \\times 2$ bite) as $48$ m². The slip:",
                 ["the bite never left — $48$ is the FULL rectangle; the L holds $42$",
                  "the multiplication is wrong",
                  "nothing — $48$ stands",
                  "areas of L-shapes cannot be found"],
                 "$8 \\times 6$ measures the restored rectangle. The room is missing its bite: $48 - 6 = 42$ m² — or split it and see the same.",
                 ["Eq(8*6, 48)", "Eq(48 - 6, 42)"]),
            funfact("Architects live in composite figures",
                    "Almost no real floor plan is a single rectangle — kitchens notch into living rooms, closets bite corners. Architects compute floor areas exactly as you just did: split into rectangles, add, and cross-check by subtracting from the outline. Same two roads, drawn to scale."),
            teach("Concept B", "Missing edges, and keeping perimeter separate", [
                "Composite figures hide some labels — but opposite spans must MATCH: if the whole top is $8$ and one bottom piece is $3$, the other is $8 - 3 = 5$.",
                "Recover every edge before computing; each missing one is a difference of labelled ones.",
                "And keep the two measures apart: cutting a bite from a rectangle REDUCES its area but (for a corner bite) the perimeter stays the same walk — the boundary just turns more corners. Area and perimeter move independently.",
            ]),
            workedset("Recovering the hidden labels",
                      "Differences first, areas second.", [
                wex("Top edge $12$; lower-right piece spans $7$. The unlabelled span?",
                    ["Opposite spans match: $12 - 7 = 5$ m."],
                    "$5$ m",
                    ["Eq(12 - 7, 5)"]),
                wex("Corner bite of $3 \\times 2$ from the $8 \\times 6$: what happens to the perimeter?",
                    ["The bite's two new edges ($3$ and $2$) replace the two removed spans ($3$ and $2$) — the walk is unchanged: $2(8 + 6) = 28$ m.",
                     "Area fell to $42$; perimeter stayed $28$. The measures move independently."],
                    "still $28$ m",
                    ["Eq(2*(8 + 6), 28)", "Eq(8*6 - 3*2, 42)"]),
            ]),
            tryitset("Hidden labels", "Match opposite spans; then compute.", [
                tp("An L-shape's left side is $9$; the upper piece's height is $4$. The lower piece's height is:",
                   ["$5$", "$13$", "$4$"],
                   "$9 - 4 = 5$ — heights along one side must add to the whole.",
                   ["Eq(9 - 4, 5)"]),
                tp("An L-shape has whole width $7$; the labelled piece is $4$ wide. The unlabelled strip beside it is $6$ tall. The strip's area is:",
                   ["$18$", "$42$", "$24$"],
                   "Strip width $7 - 4 = 3$; area $3 \\times 6 = 18$.",
                   ["Eq(7 - 4, 3)", "Eq(3*6, 18)"]),
                tp("A corner bite is cut from a rectangle. Which changes?",
                   ["the area only — the corner-bite walk keeps the same perimeter",
                    "the perimeter only",
                    "both, always"],
                   "The bite's new edges exactly replace the removed spans, so the walk's length survives; the field, though, shrinks by the bite.",
                   ["Eq(3 + 2, 2 + 3)"]),
            ]),
            tapq("Split without overlap", "Splitting an L into pieces that OVERLAP by a $2 \\times 1$ patch makes the sum:",
                 ["$2$ m² too big — the patch was counted twice",
                  "$2$ m² too small",
                  "exactly right",
                  "half right"],
                 "Overlapping tiles get counted in both pieces: the sum overshoots by the overlap's area. Splits must tile the shape exactly — edge to edge, no sharing.",
                 ["Eq(2*1, 2)"]),
            recap([
                "Split-and-add or fill-and-subtract — take both roads; agreement is the receipt.",
                "Missing edges are differences of labelled ones; recover them all first.",
                "Splits must tile exactly — overlaps double-count.",
                "A corner bite shrinks the area but leaves the perimeter's walk unchanged.",
            ]),
            tip("For every figure below, travel BOTH roads (or check spans twice) before answering — the agreement habit is the whole lesson."),
            tryitset("Mixed practice", "Composite figures, both roads open.", [
                tp("A $14 \\times 6$ m hall with a $5 \\times 2$ storage nook walled off leaves an open area of:",
                   ["$74$ m²", "$84$ m²", "$64$ m²"],
                   "$84 - 10 = 74$ m².",
                   ["Eq(14*6 - 5*2, 74)"]),
                tp("An L-shape of pieces $9 \\times 5$ and $4 \\times 3$ has area:",
                   ["$57$ m²", "$45$ m²", "$108$ m²"],
                   "$45 + 12 = 57$ m².",
                   ["Eq(9*5 + 4*3, 57)"]),
                tp("A picture $30 \\times 20$ cm sits centred on a $40 \\times 30$ cm mount. Visible mount:",
                   ["$600$ cm²", "$1\\,200$ cm²", "$100$ cm²"],
                   "$1\\,200 - 600 = 600$ cm² of visible border.",
                   ["Eq(40*30, 1200)", "Eq(30*20, 600)", "Eq(1200 - 600, 600)"]),
                tp("A staircase-shaped figure: steps of $2 \\times 2$, $4 \\times 2$ and $6 \\times 2$ stacked. Total area:",
                   ["$24$", "$12$", "$36$"],
                   "$4 + 8 + 12 = 24$ — three strips, no overlaps.",
                   ["Eq(2*2 + 4*2 + 6*2, 24)"]),
                tp("A T-stage ($10 \\times 3$ bar on a $4 \\times 5$ stem) is painted with cans that each cover $50$ m². How many cans does one coat need?",
                   ["$1$ can — the stage is exactly $50$ m²", "$2$ cans", "$5$ cans"],
                   "Bar $30$ + stem $20$ = $50$ m² — one can, to the brim.",
                   ["Eq(10*3 + 4*5, 50)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Geometry — Shapes & Area\" — the whole topic",
                    "Angles, shape families, the boundary walk, the tile count, and figures built from pieces — with two-road receipts throughout. One topic remains in Grade 5: reading and drawing data.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    return [
        prob("g5ge-pr1", "On a straight line, three angles measure $40^\\circ$, $90^\\circ$ and one more. Find it.",
             "$180 - 40 - 90 = 50^\\circ$; check $40 + 90 + 50 = 180$ ✓.",
             ["Eq(180 - 40 - 90, 50)", "Eq(40 + 90 + 50, 180)"]),
        prob("g5ge-pr2", "A triangle has angles $48^\\circ$ and $64^\\circ$. Find the third and classify by angles.",
             "$180 - 48 - 64 = 68^\\circ$ — all three under $90$: an acute triangle.",
             ["Eq(180 - 48 - 64, 68)", "68 < 90", "64 < 90", "48 < 90"]),
        prob("g5ge-pr3", "A parallelogram has one angle of $75^\\circ$. List all four angles.",
             "Neighbours complete $180$, opposites repeat: $75, 105, 75, 105$ — total $360$ ✓.",
             ["Eq(180 - 75, 105)", "Eq(75 + 105 + 75 + 105, 360)"]),
        prob("g5ge-pr4", "Find the perimeter and area of a $16$ m by $9$ m sports court, with correct units.",
             "Perimeter $2(16 + 9) = 50$ m; area $16 \\times 9 = 144$ m².",
             ["Eq(2*(16 + 9), 50)", "Eq(16*9, 144)"]),
        prob("g5ge-pr5", "A rectangle has perimeter $54$ cm and width $12$ cm. Find its length and its area.",
             "$54 \\div 2 = 27$; $l = 27 - 12 = 15$ cm. Area $15 \\times 12 = 180$ cm².",
             ["Eq(Rational(54,2) - 12, 15)", "Eq(15*12, 180)", "Eq(2*(15 + 12), 54)"]),
        prob("g5ge-pr6", "Show that a $9 \\times 3$ and a $6 \\times 6$ rectangle share a perimeter but not an area.",
             "Perimeters: $2(9+3) = 24$ and $2(6+6) = 24$ — equal. Areas: $27$ and $36$ m² — the square holds $9$ m² more.",
             ["Eq(2*(9 + 3), 24)", "Eq(2*(6 + 6), 24)", "Eq(9*3, 27)", "Eq(6*6, 36)", "36 > 27"]),
        prob("g5ge-pr7", "An L-shaped patio is a $7 \\times 6$ m rectangle with a $3 \\times 2$ m bite. Find the area by both roads.",
             "Subtract: $42 - 6 = 36$ m². Split: $7 \\times 4 = 28$ plus $(7-3) \\times 2 = 8$: $36$ m². Roads agree ✓.",
             ["Eq(7*6 - 3*2, 36)", "Eq(7*4, 28)", "Eq((7 - 3)*2, 8)", "Eq(28 + 8, 36)"]),
        prob("g5ge-pr8", "A $12 \\times 10$ m garden holds a $4 \\times 4$ m pond. Grass covers the rest; how much?",
             "$120 - 16 = 104$ m² of grass.",
             ["Eq(12*10 - 4*4, 104)"]),
    ]


def test_bank():
    return [
        prob("g5ge-x1", "Around a point sit angles of $110^\\circ$, $85^\\circ$, $75^\\circ$ and one more. Find it and classify it.",
             "$360 - 110 - 85 - 75 = 90^\\circ$ — a right angle exactly.",
             ["Eq(360 - 110 - 85 - 75, 90)"]),
        prob("g5ge-x2", "An isosceles triangle has a $100^\\circ$ angle at its top. Find the two base angles.",
             "The base pair shares $180 - 100 = 80$ equally: $40^\\circ$ each. Check: $100 + 40 + 40 = 180$ ✓.",
             ["Eq(Rational(180 - 100, 2), 40)", "Eq(100 + 40 + 40, 180)"]),
        prob("g5ge-x3", "Which of these can NOT be a triangle's angles: $(60, 60, 60)$, $(90, 45, 45)$, $(100, 50, 40)$? Why?",
             "$100 + 50 + 40 = 190 \\ne 180$ — the third set overspends the budget. The others close exactly.",
             ["Eq(60 + 60 + 60, 180)", "Eq(90 + 45 + 45, 180)", "Eq(100 + 50 + 40, 190)", "Ne(190, 180)"]),
        prob("g5ge-x4", "A square courtyard takes $60$ m of fencing. Find its side and its area.",
             "Side $60 \\div 4 = 15$ m; area $15^2 = 225$ m².",
             ["Eq(Rational(60,4), 15)", "Eq(15*15, 225)"]),
        prob("g5ge-x5", "A room is $11$ m by $4$ m. Give its area and perimeter — and name which one carpet needs and which one skirting board needs.",
             "Area $44$ m² (carpet); perimeter $2(11 + 4) = 30$ m (skirting). Tiles inside, walk around.",
             ["Eq(11*4, 44)", "Eq(2*(11 + 4), 30)"]),
        prob("g5ge-x6", ("A T-shaped stage is a $12 \\times 4$ m bar atop a $6 \\times 5$ m stem. "
                         "Find its area by splitting, and check by surrounding it with a "
                         "$12 \\times 9$ rectangle and subtracting the two shoulders."),
             "Split: $48 + 30 = 78$ m². Surround: $12 \\times 9 = 108$, shoulders $2 \\times (3 \\times 5) = 30$: $108 - 30 = 78$ m² — roads agree ✓.",
             ["Eq(12*4, 48)", "Eq(6*5, 30)", "Eq(48 + 30, 78)",
              "Eq(12*9 - 2*3*5, 78)"]),
    ]


def main():
    topic = {
        "slug": "geometry-shapes-and-area",
        "title": "Geometry — Shapes & Area",
        "grade": 5,
        "status": "published",
        "blurb": ("Angles and their sums, triangles and the quadrilateral "
                  "family, perimeter as the boundary walk, area as the tile "
                  "count, and composite figures solved down two agreeing "
                  "roads."),
        "lessons": [
            lesson_angles(),
            lesson_shapes(),
            lesson_perimeter(),
            lesson_area(),
            lesson_composite(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "geometry-shapes-and-area.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
