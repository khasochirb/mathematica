#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 3 — Topic: Shapes, Sides & Corners.

Naming the flat shapes a child meets first; counting sides and corners
and discovering they always match; recognising a square corner by
holding a page corner against it; the solid shapes and what each one
does when you push it — roll, stack or slide; and repeating shape
patterns.

Through-line: A SHAPE IS DESCRIBED BY WHAT YOU CAN COUNT ON IT. Sides
and corners give a flat shape its name, square corners tell a square
from a lopsided four-sided shape, flat faces and curved surfaces decide
whether a solid rolls or stacks, and a pattern is a count that repeats.

Grade discipline: circle, triangle, square and rectangle only among flat
shapes; cube, sphere, cylinder and cone among solids. No area, no
perimeter formulas, no symmetry and no quarter-turn language — Grade 4
owns those, along with hexagons, quadrilateral sorting and the
face/edge/vertex count. Nothing above 1000; every check is
sympy-asserted BEFORE the JSON is written, and every right-angle mark
sits on a genuine right angle because the gate measures it.

Run: python3 scripts/grade2/build_shapes_sides_and_corners.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g3build import (funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, withfig, withprobfig, workedset,
                     write_topic, fig_geo, fig_groups, P, seg, ang, poly,
                     C_ACCENT, C_WARM, C_GREEN)


def shape(points_xy, labels=None, right_at=None, color=C_ACCENT, height=190):
    """A closed flat shape through the given (x, y) corners, in order.

    Corners are drawn without letter labels by default — at this age the
    shape is the object of attention, not its vertex names. `right_at` is
    an index whose corner gets a square right-angle mark; the gate
    re-measures that angle from these very coordinates, so a mark can
    never sit on a corner that is not truly square.
    """
    n = len(points_xy)
    assert n >= 3, "shape: need at least 3 corners"
    ids = ["p%d" % i for i in range(n)]
    lbl = labels or [""] * n
    pts = [P(ids[i], points_xy[i][0], points_xy[i][1], lbl[i]) for i in range(n)]
    objs = poly(ids, color=color)
    if right_at is not None:
        i = right_at
        objs.append(ang(ids[i], ids[(i - 1) % n], ids[(i + 1) % n], right=True))
    return fig_geo(pts, objs, height=height)


# Reusable shapes, built once from exact coordinates.
TRIANGLE = [(0, 0), (6, 0), (3, 5)]
SQUARE = [(0, 0), (5, 0), (5, 5), (0, 5)]
RECTANGLE = [(0, 0), (8, 0), (8, 4), (0, 4)]
SLANTED = [(1, 0), (7, 0), (8, 4), (2, 4)]  # a four-sided shape with NO square corner


# ==========================================================================
# Lesson 1 — Naming Flat Shapes
# ==========================================================================

def lesson_naming():
    fig_tri = shape(TRIANGLE)
    fig_sq = shape(SQUARE, right_at=0)
    fig_rect = shape(RECTANGLE, color=C_WARM, right_at=0)
    return {
        "slug": "naming-flat-shapes",
        "title": "Naming Flat Shapes",
        "concreteComparison": (
            "A ger door is a rectangle, a slice of aaruul is a triangle, "
            "a coin is a circle. Shapes get their names from what you can "
            "count on them — and a circle gets its name from having "
            "nothing to count at all."),
        "objective": (
            "Name a circle, triangle, square and rectangle, say what "
            "makes each one different, and pick a shape out of a picture "
            "by its name."),
        "concept": [
            "**A triangle has three straight sides.** That is the whole "
            "definition — three sides and three corners, whatever it "
            "looks like otherwise. Tall and thin or wide and flat, if it "
            "has three straight sides it is a triangle.",
            "**Squares and rectangles have four straight sides.** A "
            "rectangle has four square corners and its opposite sides "
            "match. A square is a rectangle whose four sides are ALL the "
            "same length — so every square is a rectangle, but most "
            "rectangles are not squares.",
            "**A circle has no sides and no corners.** It is one curved "
            "line all the way round, always the same distance from the "
            "middle. There is nothing to count, which is exactly what "
            "makes it a circle.",
        ],
        "keyIdea": (
            "Flat shapes are named by their straight sides: three for a "
            "triangle, four for a square or rectangle, and none at all "
            "for a circle."),
        "facts": [
            {"title": "Three sides, three corners",
             "latex": "3 + 3 = 6",
             "explanation": "A triangle has three sides and three corners — six things to count in all."},
            {"title": "Four sides, four corners",
             "latex": "4 + 4 = 8",
             "explanation": "A square or rectangle has four of each."},
        ],
        "workedExamples": [
            {"id": "g3sh-l1-we1",
             "statement": "A shape has three straight sides. What is it called, and how many corners does it have?",
             "note": "The sides give the name.",
             "solution": ("Three straight sides makes it a triangle. Every "
                          "straight side meets another at a corner, so it has "
                          "three corners too — $3$ sides and $3$ corners, "
                          "$3 + 3 = 6$ things to count altogether."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3 + 3, 6)", "Eq(3*2, 6)"]},
            {"id": "g3sh-l1-we2",
             "statement": "What is the difference between a square and a rectangle?",
             "note": "Both have four sides — look at the lengths.",
             "solution": ("Both have $4$ straight sides and $4$ square corners. "
                          "In a rectangle the opposite sides match, but the long "
                          "sides may differ from the short ones. In a square all "
                          "$4$ sides are the same length. So every square is a "
                          "rectangle, but a rectangle is only a square when its "
                          "sides all agree."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4 + 4, 8)", "Eq(4*2, 8)"]},
        ],
        "commonMistakes": [
            {"text": "Only recognising a triangle when it points upwards and sits flat.",
             "correction": "A triangle is any shape with three straight sides, whichever way round it is drawn. Turning it upside down changes nothing about its three sides and three corners.",
             "authored": True},
            {"text": "Saying a square is not a rectangle.",
             "correction": "A rectangle needs four sides and four square corners, and a square has both — so every square IS a rectangle. It is simply the special one whose four sides are all equal.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3sh-l1-t1",
             "statement": "How many sides and corners does a rectangle have altogether?",
             "solution": ("Four sides and four corners: $4 + 4 = 8$ things to "
                          "count."),
             "check": ["Eq(4 + 4, 8)"]},
            {"id": "g3sh-l1-t2",
             "statement": "Why does a circle have no corners?",
             "solution": ("A corner is where two straight sides meet, and a "
                          "circle has no straight sides at all — just one curved "
                          "line all the way round. No sides means no corners."),
             "check": ["Eq(0 + 0, 0)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Counting the sides", [
                "The shape below has three straight sides — that makes it a triangle, and nothing else about it matters.",
                "Tall and thin, wide and flat, tipped on its point: all triangles, because all of them have three straight sides.",
                "Every side meets another at a corner, so the corners always match the sides. A triangle has $3$ of each, which is $3 + 3 = 6$ things you could count on it.",
            ]), fig_tri),
            workedset("Name it by its sides", "Count the straight sides first.", [
                wex("A shape has three straight sides. Name it.",
                    ["Three straight sides means a triangle.",
                     "It also has three corners: $3 + 3 = 6$ to count."],
                    "a triangle",
                    ["Eq(3 + 3, 6)"]),
                wex("A shape has four straight sides and four square corners, with all sides the same length. Name it.",
                    ["Four sides and square corners means a rectangle.",
                     "All four sides equal makes it the special one — a square."],
                    "a square",
                    ["Eq(4 + 4, 8)", "Eq(4*2, 8)"]),
            ]),
            tryitset("Which shape?", "Count the straight sides.", [
                withfig(tp("The shape below has four equal sides and four square corners. It is:",
                   ["a square", "a triangle", "a circle"],
                   "Four straight sides with square corners and all sides equal: a square. A triangle would have three sides and a circle none.",
                   ["Eq(4 + 4, 8)", "Eq(3 + 3, 6)"]), fig_sq),
                tp("A shape with three straight sides is:",
                   ["a triangle", "a rectangle", "a circle"],
                   "Three straight sides always makes a triangle, whichever way it is turned. Rectangles have four and circles have none.",
                   ["Eq(3 + 3, 6)", "Eq(4 + 4, 8)"]),
                tp("A coin has:",
                   ["no sides and no corners", "four sides", "one corner"],
                   "A coin is a circle — one curved line all the way round, with no straight sides at all, and therefore no corners either.",
                   ["Eq(0 + 0, 0)"]),
            ]),
            tapq("Sides and corners", "How many things are there to count on a triangle — sides and corners together?",
                 ["$6$", "$3$", "$9$", "$4$"],
                 "Three sides and three corners: $3 + 3 = 6$. The two counts always match, because every corner is where two sides meet.",
                 ["Eq(3 + 3, 6)", "Eq(3*2, 6)"]),
            funfact("Why the ger is round",
                    "A round wall has no corners for the wind to catch, which matters a great deal on the steppe. It also encloses more floor space than any four-sided wall of the same length — a circle is the shape that gets the most room for the least wall. Nomadic builders worked that out long before anyone proved it."),
            withfig(teach("Concept B", "Squares among the rectangles", [
                "The shape below has four straight sides and four square corners — a rectangle. Its opposite sides match: long with long, short with short.",
                "A square has all that AND one extra condition: its four sides are all the same length. So a square is a rectangle that happens to be equal-sided.",
                "That is worth saying plainly: every square is a rectangle, but most rectangles are not squares. The square is the special case, not a different family.",
            ]), fig_rect),
            workedset("Square or rectangle?", "Check whether all four sides match.", [
                wex("A shape has four square corners, two long sides and two short ones. Name it.",
                    ["Four sides with square corners: a rectangle.",
                     "The sides are not all equal, so it is not a square."],
                    "a rectangle",
                    ["Eq(4 + 4, 8)"]),
                wex("Is a square a rectangle?",
                    ["A rectangle needs four sides and four square corners.",
                     "A square has both, so yes — it is the special rectangle with all sides equal."],
                    "yes",
                    ["Eq(4*2, 8)", "Eq(4 + 4, 8)"]),
            ]),
            tryitset("Squares and rectangles", "All sides equal, or only the opposite ones?", [
                tp("A shape with four square corners and sides of $3$, $5$, $3$, $5$ is:",
                   ["a rectangle but not a square",
                    "a square", "a triangle"],
                   "Opposite sides match ($3$ with $3$, $5$ with $5$) so it is a rectangle, but the sides are not ALL equal, so it is not a square. Its four sides total $3 + 5 + 3 + 5 = 16$.",
                   ["Eq(3 + 5 + 3 + 5, 16)", "Ne(3, 5)"]),
                tp("A shape with four square corners and sides of $4$, $4$, $4$, $4$ is:",
                   ["a square", "a triangle", "not a rectangle"],
                   "All four sides equal with square corners: a square — which is also a rectangle. Its sides total $4 \\times 4 = 16$.",
                   ["Eq(4*4, 16)", "Eq(4 + 4 + 4 + 4, 16)"]),
                tp("Which statement is TRUE?",
                   ["every square is a rectangle",
                    "every rectangle is a square",
                    "no square is a rectangle"],
                   "A square meets every condition a rectangle has, plus one more, so every square is a rectangle. The reverse fails whenever the long and short sides differ.",
                   ["Eq(4 + 4, 8)", "Ne(3, 5)"]),
            ]),
            tapq("The special rectangle", "What makes a square different from other rectangles?",
                 ["all four of its sides are equal",
                  "it has four corners and they do not",
                  "it has more sides",
                  "nothing — the words mean the same thing"],
                 "Both have four sides and four square corners; the square adds that all four sides are the same length. So $4 \\times 4 = 16$ describes a square's sides, while a $3$ by $5$ rectangle totals $3 + 5 + 3 + 5 = 16$ from unequal ones.",
                 ["Eq(4*4, 16)", "Eq(3 + 5 + 3 + 5, 16)", "Ne(3, 5)"]),
            recap([
                "A triangle has three straight sides and three corners.",
                "Squares and rectangles have four straight sides and four square corners.",
                "A square is the rectangle whose four sides are all equal — every square is a rectangle.",
                "A circle has no straight sides, so it has no corners at all.",
            ]),
            tip("When naming a shape, count its straight sides out loud and touch each one. Counting by eye is where shapes get miscounted, and touching is what stops it."),
            tryitset("Chapter practice", "Sides first, then the corners.", [
                tp("A shape has $4$ straight sides. It could be:",
                   ["a square or a rectangle", "a triangle", "a circle"],
                   "Four straight sides rules out triangles (three) and circles (none). Whether it is a square depends on whether all four sides are equal.",
                   ["Eq(4 + 4, 8)", "Eq(3 + 3, 6)"]),
                tp("Two triangles together have how many sides in all?",
                   ["$6$", "$3$", "$8$"],
                   "Each triangle has three sides: $2 \\times 3 = 6$ sides altogether.",
                   ["Eq(2*3, 6)"]),
                tp("Which shape has NO corners?",
                   ["a circle", "a triangle", "a rectangle"],
                   "A corner is where two straight sides meet, and a circle has no straight sides — just one curved line all the way round.",
                   ["Eq(0 + 0, 0)", "Eq(3 + 3, 6)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Naming Flat Shapes\"",
                    "You can now name a shape from what you can count on it. The next lesson looks harder at the corners themselves — because four sides alone do not make a rectangle, and telling the difference needs nothing more than the corner of a page.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Square Corners
# ==========================================================================

def lesson_square_corners():
    fig_sq = shape(SQUARE, right_at=0, color=C_GREEN)
    fig_slant = shape(SLANTED, color=C_WARM)
    fig_rt_tri = shape([(0, 0), (6, 0), (0, 4)], right_at=0)
    return {
        "slug": "square-corners",
        "title": "Square Corners",
        "concreteComparison": (
            "Hold the corner of this page against the corner of a table. "
            "If they match exactly, the table has a square corner. That "
            "test — no measuring, no instruments — is all you need to "
            "tell a rectangle from a shape that merely has four sides."),
        "objective": (
            "Test a corner for squareness by matching it against a known "
            "square corner, and use square corners to tell rectangles "
            "from other four-sided shapes."),
        "concept": [
            "**A square corner is the corner of a page.** Every sheet of "
            "paper has four of them, and they are all identical. To test "
            "any corner, hold the page corner against it: an exact match "
            "means a square corner.",
            "**A rectangle needs FOUR square corners.** Four straight "
            "sides are not enough. A shape can have four sides and lean "
            "over like a pushed-over box — its corners are then two "
            "sharper than square and two blunter, and it is not a "
            "rectangle.",
            "**Square corners turn up elsewhere too.** A triangle can "
            "have one — never more, since two would make its other two "
            "sides run alongside each other forever and never meet. Look "
            "for square corners in door frames, window panes and the "
            "squares of a grid.",
        ],
        "keyIdea": (
            "A square corner is the corner of a page, and a rectangle is "
            "a four-sided shape with four of them."),
        "facts": [
            {"title": "Four square corners",
             "latex": "4 \\times 1 = 4",
             "explanation": "A rectangle has one square corner at each of its four corners."},
            {"title": "A triangle can have one",
             "latex": "3 - 2 = 1",
             "explanation": "At most one of a triangle's three corners can be square."},
        ],
        "workedExamples": [
            {"id": "g3sh-l2-we1",
             "statement": "How can you check whether a table corner is a square corner, without measuring?",
             "note": "Use something you know is square.",
             "solution": ("Hold the corner of a sheet of paper against it. Paper "
                          "corners are square, so an exact match — no gap, no "
                          "overlap — means the table corner is square too. A "
                          "rectangle table has all $4$ of its corners pass this "
                          "test."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*1, 4)", "Eq(4 + 4, 8)"]},
            {"id": "g3sh-l2-we2",
             "statement": "A four-sided shape leans over like a pushed box. Is it a rectangle?",
             "note": "Count its square corners.",
             "solution": ("No. It has $4$ straight sides, but its corners are not "
                          "square — two are sharper than a page corner and two "
                          "are blunter. A rectangle needs all $4$ corners square, "
                          "and this shape has $0$ of them."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*1, 4)", "Eq(2 + 2, 4)"]},
        ],
        "commonMistakes": [
            {"text": "Calling any four-sided shape a rectangle.",
             "correction": "Four sides is only half the requirement. A leaning four-sided shape has no square corners at all, and a rectangle needs four of them — test with a page corner.",
             "authored": True},
            {"text": "Deciding a corner is square by eye, from across the desk.",
             "correction": "Corners a little off square look square from a distance. Hold a page corner against it: the test takes a second and it does not guess.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3sh-l2-t1",
             "statement": "How many square corners does a rectangle have?",
             "solution": ("All four: $4 \\times 1 = 4$. That is exactly what "
                          "separates a rectangle from a leaning four-sided "
                          "shape, which has none."),
             "check": ["Eq(4*1, 4)"]},
            {"id": "g3sh-l2-t2",
             "statement": "Can a triangle have two square corners? Explain.",
             "solution": ("No. With two square corners the two sides leaving "
                          "them would run alongside each other and never meet, "
                          "so the triangle could not close. At most $3 - 2 = 1$ "
                          "of its corners is square."),
             "check": ["Eq(3 - 2, 1)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The page-corner test", [
                "The shape below is a square, and the little mark in its bottom-left corner is how we show that a corner is SQUARE.",
                "You can test any corner in the room without a single instrument: hold the corner of a sheet of paper against it. Paper corners are square, and every sheet has four identical ones.",
                "An exact match — no gap and no overlap — means the corner is square. This is a real test, not a guess, and it takes about a second.",
            ]), fig_sq),
            workedset("Test the corner", "Match it against a page corner.", [
                wex("How do you check whether a table corner is square?",
                    ["Hold a page corner against it.",
                     "An exact match means square. A rectangle table passes at all $4$ corners."],
                    "match it to a page corner",
                    ["Eq(4*1, 4)"]),
                wex("A shape has four sides. How many corners must be square for it to be a rectangle?",
                    ["Every one of them.",
                     "That is $4 \\times 1 = 4$ square corners."],
                    "$4$",
                    ["Eq(4*1, 4)", "Eq(4 + 4, 8)"]),
            ]),
            tryitset("Square or not?", "Would a page corner fit exactly?", [
                withfig(tp("The four-sided shape below leans over. It is:",
                   ["not a rectangle — no square corners",
                    "a rectangle", "a square"],
                   "It has four straight sides, but a page corner would not fit any of its corners: two are sharper than square and two blunter. A rectangle needs all four square.",
                   ["Eq(2 + 2, 4)", "Eq(4*1, 4)"]), fig_slant),
                tp("A window pane with four square corners and unequal sides is:",
                   ["a rectangle", "a square", "a triangle"],
                   "Four sides and four square corners make a rectangle. It is not a square, because its sides are not all equal.",
                   ["Eq(4*1, 4)", "Ne(3, 5)"]),
                tp("The best way to test a corner is to:",
                   ["hold a page corner against it",
                    "look at it from a distance",
                    "count the sides of the shape"],
                   "Corners slightly off square look square from a distance, so the eye is not enough. A page corner either fits or it does not.",
                   ["Eq(4*1, 4)"]),
            ]),
            tapq("Four sides is not enough", "A shape has four straight sides but no square corners. Is it a rectangle?",
                 ["no — a rectangle needs four square corners",
                  "yes — four sides is what matters",
                  "yes, if the opposite sides match",
                  "only if it is standing upright"],
                 "Four sides is half the requirement; the other half is that all $4 \\times 1 = 4$ corners are square. A leaning four-sided shape has none of them, so it is not a rectangle however it is turned.",
                 ["Eq(4*1, 4)", "Eq(2 + 2, 4)"]),
            funfact("The oldest tool for a square corner",
                    "Builders have needed square corners for as long as there have been walls, and long before rulers they used a loop of rope knotted into $12$ equal lengths. Pulled into a triangle with sides of $3$, $4$ and $5$ knots, the corner between the short sides comes out exactly square — every time, with nothing but rope."),
            withfig(teach("Concept B", "Square corners in other shapes", [
                "Square corners are not only for rectangles. The triangle below has one — the mark sits at the corner where its two straight sides meet at a page-corner angle.",
                "A triangle can have at most ONE. If it had two, the sides leaving those corners would run alongside each other forever and never meet, so the triangle could never close: $3 - 2 = 1$ is the most it can manage.",
                "Once you start testing, square corners appear everywhere — door frames, window panes, the squares of a grid, the corner of every book on the shelf.",
            ]), fig_rt_tri),
            workedset("Square corners elsewhere",
                      "Count how many a shape can have.", [
                wex("How many square corners can a triangle have?",
                    ["Two would stop the sides ever meeting.",
                     "So at most one: $3 - 2 = 1$."],
                    "at most $1$",
                    ["Eq(3 - 2, 1)"]),
                wex("A rectangular door has how many square corners, and a triangular gable above it at most how many?",
                    ["The door: $4$ square corners.",
                     "The gable: at most $1$.",
                     "Together at most $4 + 1 = 5$."],
                    "$4$ and at most $1$",
                    ["Eq(4*1, 4)", "Eq(3 - 2, 1)", "Eq(4 + 1, 5)"]),
            ]),
            tryitset("How many square corners?", "Count them, and check the shape can close.", [
                tp("A triangle can have at most how many square corners?",
                   ["$1$", "$2$", "$3$"],
                   "Two square corners would send the other two sides alongside each other, never to meet, so the triangle could not close: $3 - 2 = 1$.",
                   ["Eq(3 - 2, 1)"]),
                tp("A rectangle has how many square corners?",
                   ["$4$", "$2$", "$1$"],
                   "All four of them — that is precisely what makes it a rectangle rather than a leaning four-sided shape.",
                   ["Eq(4*1, 4)"]),
                tp("Two rectangles side by side have how many square corners in total?",
                   ["$8$", "$4$", "$16$"],
                   "Each has four: $2 \\times 4 = 8$ square corners between them.",
                   ["Eq(2*4, 8)", "Eq(4 + 4, 8)"]),
            ]),
            tapq("Why not two?", "Why can a triangle not have two square corners?",
                 ["the other two sides would never meet",
                  "because three is an odd number",
                  "it can — a triangle may have two",
                  "because triangles are always pointy"],
                 "Two square corners send the sides leaving them alongside each other, so they never meet to close the shape. At most $3 - 2 = 1$ corner of a triangle is square.",
                 ["Eq(3 - 2, 1)", "Eq(3 + 3, 6)"]),
            recap([
                "A square corner is the corner of a page — test any corner by matching one against it.",
                "A rectangle is a four-sided shape with all FOUR corners square.",
                "Four sides alone is not enough: a leaning four-sided shape has no square corners.",
                "A triangle can have at most one square corner.",
            ]),
            tip("Keep a small square of paper in your pencil case. It is a corner tester you can use on anything — desks, books, tiles — and it never disagrees with itself."),
            tryitset("Chapter practice", "Would a page corner fit?", [
                tp("A shape with four sides and four square corners is:",
                   ["a rectangle", "a triangle", "never a square"],
                   "That is exactly the description of a rectangle — and if all four sides are also equal, it is the special rectangle we call a square.",
                   ["Eq(4*1, 4)", "Eq(4 + 4, 8)"]),
                tp("A page has how many square corners?",
                   ["$4$", "$2$", "$1$"],
                   "Every sheet of paper is a rectangle, so all four of its corners are square — which is why any of them works as a tester.",
                   ["Eq(4*1, 4)"]),
                tp("Three rectangles have how many square corners altogether?",
                   ["$12$", "$4$", "$9$"],
                   "Four corners each: $3 \\times 4 = 12$.",
                   ["Eq(3*4, 12)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Square Corners\"",
                    "A sheet of paper turned out to be a measuring instrument. Next the shapes leave the page altogether — solids you can hold, which are sorted not by counting but by what they do when you push them.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 3 — Solid Shapes
# ==========================================================================

def lesson_solids():
    fig_flat = fig_groups((6, "cube: 6 flat faces", C_ACCENT),
                          (0, "sphere: no flat faces", C_WARM))
    fig_cyl = fig_groups((2, "cylinder: 2 flat faces", C_GREEN),
                         (1, "cone: 1 flat face", C_WARM))
    fig_stack = fig_groups((6, "stacks: cube", C_ACCENT),
                           (0, "rolls: sphere", C_WARM))
    return {
        "slug": "solid-shapes",
        "title": "Solid Shapes",
        "concreteComparison": (
            "A dice, a ball, a tin of tea and a paper cone. Put each on a "
            "slope and watch: the ball rolls, the tin rolls but only one "
            "way, the cone rolls in a circle, and the dice does not roll "
            "at all. What a solid DOES tells you what it is."),
        "objective": (
            "Name the cube, sphere, cylinder and cone, count the flat "
            "faces of each, and predict whether a solid will roll, stack "
            "or slide."),
        "concept": [
            "**Flat faces are what you can stack on.** A cube has $6$ "
            "flat faces, all squares — so it stacks whichever way up you "
            "put it. A sphere has $0$ flat faces, so it stacks on "
            "nothing at all.",
            "**Curved surfaces are what roll.** A sphere is curved all "
            "over and rolls in any direction. A cylinder has $2$ flat "
            "faces (its ends) and a curved side, so it rolls one way and "
            "stands still on its ends. A cone has $1$ flat face and rolls "
            "round in a circle.",
            "**So a solid can both roll and stack.** A tin of tea stands "
            "on its end and rolls on its side — it depends which surface "
            "is touching the table. Only the sphere, with no flat face at "
            "all, can never be stood up.",
        ],
        "keyIdea": (
            "Flat faces let a solid stack; curved surfaces let it roll — "
            "and a solid with both can do either, depending on which part "
            "is touching the table."),
        "facts": [
            {"title": "The cube's faces",
             "latex": "6 \\times 1 = 6",
             "explanation": "Six flat square faces — a cube stacks whichever way up."},
            {"title": "Cylinder and cone",
             "latex": "2 - 1 = 1",
             "explanation": "A cylinder has two flat faces, a cone one — the cylinder has one more."},
        ],
        "workedExamples": [
            {"id": "g3sh-l3-we1",
             "statement": "How many flat faces has a cube, and what does that let it do?",
             "note": "Count the faces you could stand it on.",
             "solution": ("A cube has $6$ flat faces, all of them squares. Any "
                          "one of them can sit on the table, so a cube stacks "
                          "whichever way up you put it — and it never rolls, "
                          "because it has no curved surface anywhere."),
             "badges": [{"text": "core"}],
             "check": ["Eq(6*1, 6)", "Eq(6 - 0, 6)"]},
            {"id": "g3sh-l3-we2",
             "statement": "A tin of tea both rolls and stands up. Explain how.",
             "note": "Which surface touches the table?",
             "solution": ("A tin is a cylinder: $2$ flat faces at the ends and a "
                          "curved side. Stood on an end, a flat face touches the "
                          "table and it stays put; laid on its side, the curved "
                          "surface touches and it rolls. Same solid, different "
                          "surface in contact."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2 - 1, 1)", "Eq(2 + 1, 3)"]},
        ],
        "commonMistakes": [
            {"text": "Deciding a solid either rolls or stacks, never both.",
             "correction": "A cylinder does both: it stands on its two flat ends and rolls on its curved side. Which one happens depends on the surface touching the table.",
             "authored": True},
            {"text": "Calling a ball a circle.",
             "correction": "A circle is flat — you could draw it on paper. A ball is a solid you can hold, and its name is a sphere. Its shadow is a circle, but the ball itself is not.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3sh-l3-t1",
             "statement": "How many flat faces has a sphere, and what does that mean for stacking?",
             "solution": ("None: a sphere is curved all over, so it has $0$ flat "
                          "faces and nothing can be stacked on it — nor can it "
                          "be stood up. It only rolls."),
             "check": ["Eq(0*6, 0)", "Eq(6 - 6, 0)"]},
            {"id": "g3sh-l3-t2",
             "statement": "How many more flat faces has a cylinder than a cone?",
             "solution": ("A cylinder has $2$ (its two ends) and a cone has $1$ "
                          "(its base), so the cylinder has $2 - 1 = 1$ more."),
             "check": ["Eq(2 - 1, 1)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Flat faces and stacking", [
                "A dice is a cube. Count the faces you could stand it on and you get $6$ — every face is a flat square.",
                "That is why a cube stacks whichever way up you put it, and why boxes are cube-like: flat faces sit still, and things that sit still can be piled.",
                "A ball is a sphere, and the picture below shows the contrast — $6$ flat faces against $0$. With no flat face anywhere, a sphere cannot be stood up or stacked on. It can only roll.",
            ]), fig_flat),
            workedset("Count the flat faces", "Which surfaces could sit on a table?", [
                wex("How many flat faces has a cube?",
                    ["Every face is a flat square.",
                     "There are $6$ of them: $6 \\times 1 = 6$."],
                    "$6$",
                    ["Eq(6*1, 6)"]),
                wex("How many flat faces has a sphere?",
                    ["A sphere is curved all over.",
                     "So $0$ flat faces — it cannot be stood up."],
                    "$0$",
                    ["Eq(6 - 6, 0)", "Eq(0*6, 0)"]),
            ]),
            tryitset("Roll or stack?", "Count the flat faces first.", [
                tp("A cube has $6$ flat faces, so it:",
                   ["stacks, and never rolls", "rolls, and never stacks",
                    "does neither"],
                   "Every face is flat, so it sits still whichever way up — and with no curved surface anywhere, there is nothing for it to roll on.",
                   ["Eq(6*1, 6)", "Eq(6 - 6, 0)"]),
                tp("A ball is:",
                   ["a sphere, which only rolls",
                    "a circle, which only rolls",
                    "a cylinder, which rolls one way"],
                   "A ball is a sphere — a solid you can hold. A circle is flat and could be drawn on paper. With $0$ flat faces the sphere rolls in any direction.",
                   ["Eq(0*6, 0)"]),
                tp("Which solid can BOTH roll and stand up?",
                   ["a cylinder", "a sphere", "a cube"],
                   "A cylinder has two flat ends and a curved side, so it stands on an end and rolls on its side. The sphere never stands and the cube never rolls.",
                   ["Eq(2 - 1, 1)", "Eq(2 + 1, 3)"]),
            ]),
            withfig(tapq("What lets a solid stack?", "Why can a sphere never be stacked?",
                 ["it has no flat faces", "it is too round to be heavy",
                  "it has too many faces", "it can be — with care"],
                 "Stacking needs a flat surface to sit on, and a sphere has $0$ of them — it is curved all over. A cube, with its $6$ flat faces, stacks whichever way up.",
                 ["Eq(0*6, 0)", "Eq(6*1, 6)"]), fig_stack),
            funfact("Why tins are cylinders",
                    "A cylinder is the shape that gets the most inside for the least metal round the outside, among shapes you can easily roll off a machine. It also stacks neatly on its ends and rolls along a shelf when you want it to. Very few shapes are good at both, which is why almost every tin in the shop is the same shape."),
            withfig(teach("Concept B", "Cylinders and cones", [
                "A tin of tea is a cylinder: $2$ flat faces — the two ends — and a curved surface joining them, as the picture below shows.",
                "That is why it does both things. Stand it on an end and a flat face touches the table, so it stays put. Lay it down and the curved side touches, so it rolls — but only in one direction, straight along.",
                "A cone has just $1$ flat face, its base. Stood on that base it stays; laid on its side it rolls round in a circle, because one end of it is wider than the other.",
            ]), fig_cyl),
            workedset("Cylinders and cones",
                      "Count flat faces, then predict what it does.", [
                wex("How many flat faces has a cylinder, and what can it do?",
                    ["Two flat ends and a curved side.",
                     "So $2$ flat faces: it stands on an end and rolls on its side."],
                    "$2$",
                    ["Eq(2 + 1, 3)", "Eq(2 - 1, 1)"]),
                wex("How many more flat faces has a cylinder than a cone?",
                    ["Cylinder $2$, cone $1$.",
                     "So $2 - 1 = 1$ more."],
                    "$1$ more",
                    ["Eq(2 - 1, 1)"]),
            ]),
            tryitset("Which solid?", "Match the flat-face count to the behaviour.", [
                tp("A solid with $1$ flat face that rolls round in a circle is:",
                   ["a cone", "a cylinder", "a cube"],
                   "One flat base and a curved surface that narrows to a point: a cone. A cylinder has $2$ flat faces and rolls straight.",
                   ["Eq(2 - 1, 1)"]),
                tp("A tin standing on its end does not roll because:",
                   ["a flat face is touching the table",
                    "tins are too heavy to roll",
                    "it has no curved surface"],
                   "The curved surface is still there — it is simply not touching. A flat end is on the table, and flat faces sit still.",
                   ["Eq(2 + 1, 3)"]),
                tp("Four cubes have how many flat faces altogether?",
                   ["$24$", "$6$", "$10$"],
                   "Six faces each: $4 \\times 6 = 24$ flat faces in all.",
                   ["Eq(4*6, 24)", "Eq(6*1, 6)"]),
            ]),
            tapq("Same solid, two behaviours", "A tin rolls on its side but not on its end. Why?",
                 ["a different surface touches the table each time",
                  "the tin changes shape when you turn it",
                  "it is heavier on its end",
                  "it should roll both ways"],
                 "A cylinder has $2$ flat faces and a curved side. Stood on an end, a flat face is in contact and it stays; on its side the curved surface is in contact and it rolls. The tin never changed — only what is touching the table.",
                 ["Eq(2 + 1, 3)", "Eq(2 - 1, 1)"]),
            recap([
                "A cube has $6$ flat faces and stacks whichever way up; it never rolls.",
                "A sphere has $0$ flat faces — it only rolls and cannot be stood up.",
                "A cylinder has $2$ flat faces: it stands on an end and rolls on its side.",
                "A cone has $1$ flat face and rolls round in a circle.",
            ]),
            tip("Pick the object up and turn it over in your hands before answering. Which faces are flat, and which are curved? Solids are much easier to sort by touch than by picture."),
            tryitset("Chapter practice", "Flat faces stack; curved surfaces roll.", [
                tp("Which solid has NO flat faces?",
                   ["a sphere", "a cube", "a cone"],
                   "A sphere is curved all over: $0$ flat faces. A cone has one and a cube has six.",
                   ["Eq(0*6, 0)", "Eq(6*1, 6)"]),
                tp("A cylinder has how many flat faces?",
                   ["$2$", "$1$", "$6$"],
                   "Its two ends are flat and the side is curved — which is exactly why it both stands and rolls.",
                   ["Eq(2 - 1, 1)", "Eq(2 + 1, 3)"]),
                tp("Two cubes and one cone have how many flat faces in total?",
                   ["$13$", "$12$", "$7$"],
                   "Cubes: $2 \\times 6 = 12$. Cone: $1$. Together $12 + 1 = 13$.",
                   ["Eq(2*6, 12)", "Eq(12 + 1, 13)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Solid Shapes\"",
                    "Flat faces and curved surfaces explain every rolling, stacking and sliding thing in the room. The last lesson goes back to flat shapes and puts them in a line — because a pattern is one more thing you can count.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 4 — Shape Patterns
# ==========================================================================

def lesson_patterns():
    fig_ab = fig_groups((3, "triangles", C_ACCENT), (3, "squares", C_WARM),
                        (3, "triangles again", C_ACCENT))
    fig_abc = fig_groups((2, "circle", C_ACCENT), (2, "square", C_WARM),
                         (2, "triangle", C_GREEN))
    fig_grow = fig_groups((1, "step 1", C_GREEN), (2, "step 2", C_GREEN),
                          (3, "step 3", C_GREEN), (4, "step 4", C_GREEN))
    return {
        "slug": "shape-patterns",
        "title": "Shape Patterns",
        "concreteComparison": (
            "The border round a felt rug repeats: triangle, square, "
            "triangle, square. Once you have spotted the piece that "
            "repeats, you can say what comes next without looking — and "
            "you could carry the border round the whole rug."),
        "objective": (
            "Find the repeating unit in a shape pattern, continue the "
            "pattern, and tell a repeating pattern from a growing one."),
        "concept": [
            "**A repeating pattern is one small piece said over and "
            "over.** Triangle, square, triangle, square — the repeating "
            "piece is \"triangle, square\", just $2$ shapes long. Find "
            "that piece and the whole pattern is known.",
            "**The length of the repeat lets you count ahead.** With a "
            "repeat of $2$, shapes $1, 3, 5$ are all triangles and shapes "
            "$2, 4, 6$ are all squares. With a repeat of $3$ — circle, "
            "square, triangle — every third shape is the same.",
            "**A growing pattern is different: it changes by the same "
            "amount each time.** $1, 2, 3, 4$ dots is a growing pattern "
            "adding one each step, not a repeating one. Repeating "
            "patterns come back to where they started; growing patterns "
            "never do.",
        ],
        "keyIdea": (
            "Find the piece that repeats and count its length — that is "
            "all you need to continue a pattern or say what sits at any "
            "position."),
        "facts": [
            {"title": "A repeat of two",
             "latex": "2 \\times 3 = 6",
             "explanation": "Three copies of a two-shape repeat make six shapes."},
            {"title": "A growing pattern",
             "latex": "1 + 1 = 2",
             "explanation": "Each step adds the same amount — it never comes back to the start."},
        ],
        "workedExamples": [
            {"id": "g3sh-l4-we1",
             "statement": "A border goes triangle, square, triangle, square, triangle. What is the repeating piece, and what comes next?",
             "note": "Look for the shortest piece that repeats.",
             "solution": ("The repeating piece is \"triangle, square\" — $2$ "
                          "shapes long. Five shapes have been laid, which is two "
                          "full repeats ($2 \\times 2 = 4$) plus one more, so the "
                          "next shape completes the third repeat: a square."),
             "badges": [{"text": "core"}],
             "check": ["Eq(2*2, 4)", "Eq(4 + 1, 5)", "Eq(5 + 1, 6)",
                       "Eq(2*3, 6)"]},
            {"id": "g3sh-l4-we2",
             "statement": "A pattern goes circle, square, triangle, circle, square, triangle. How long is the repeat, and what is the $7$th shape?",
             "note": "Count the repeat, then count on.",
             "solution": ("The repeat is $3$ shapes long. Six shapes make two "
                          "full repeats ($3 \\times 2 = 6$), so the $7$th shape "
                          "starts a new repeat — a circle, the same as the "
                          "first."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*2, 6)", "Eq(6 + 1, 7)"]},
        ],
        "commonMistakes": [
            {"text": "Taking the repeating piece to be longer than it is — calling \"triangle, square, triangle, square\" a four-shape repeat.",
             "correction": "The repeating piece is the SHORTEST one that works, and \"triangle, square\" already does. Reading it as four makes counting ahead twice as hard for no reason.",
             "authored": True},
            {"text": "Calling a growing pattern a repeating one.",
             "correction": "1, 2, 3, 4 dots never returns to where it started — each step adds one more. A repeating pattern always comes back round to its first shape.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3sh-l4-t1",
             "statement": "A pattern goes square, square, circle, square, square, circle. How long is the repeat?",
             "solution": ("The repeating piece is \"square, square, circle\" — "
                          "$3$ shapes long. Six shapes is exactly two repeats: "
                          "$3 \\times 2 = 6$."),
             "check": ["Eq(3*2, 6)"]},
            {"id": "g3sh-l4-t2",
             "statement": "Is $2, 4, 6, 8$ a repeating pattern or a growing one?",
             "solution": ("Growing — each step adds $2$ and it never comes back "
                          "to $2$: $2 + 2 = 4$, $4 + 2 = 6$, $6 + 2 = 8$. A "
                          "repeating pattern would return to its first term."),
             "check": ["Eq(2 + 2, 4)", "Eq(6 + 2, 8)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Finding the piece that repeats", [
                "The border below goes triangles, squares, triangles — a run of one shape, then the other, then back again.",
                "The piece that repeats is \"triangle, square\", just $2$ shapes long. Say it over and over and you have rebuilt the whole border.",
                "That is the whole skill: find the SHORTEST piece that repeats. Once you have it, you never have to look at the pattern again to continue it.",
            ]), fig_ab),
            workedset("Find the repeat", "Look for the shortest piece that works.", [
                wex("Triangle, square, triangle, square, triangle. What is the repeat, and what comes next?",
                    ["The repeat is \"triangle, square\" — $2$ long.",
                     "Five shapes is two repeats ($2 \\times 2 = 4$) plus one.",
                     "The $6$th shape completes the third repeat: a square."],
                    "a square",
                    ["Eq(2*2, 4)", "Eq(4 + 1, 5)", "Eq(2*3, 6)"]),
                wex("Circle, square, triangle, circle, square, triangle. What is the repeat?",
                    ["Three shapes go by before the circle returns.",
                     "The repeat is $3$ long, and $3 \\times 2 = 6$ shapes are two full repeats."],
                    "$3$ shapes",
                    ["Eq(3*2, 6)"]),
            ]),
            tryitset("What comes next?", "Say the repeating piece to yourself.", [
                withfig(tp("The border repeats triangles and squares. After three triangles and three squares, the next group is:",
                   ["triangles", "squares", "circles"],
                   "The repeat is \"triangles, squares\", so after a group of squares the pattern returns to triangles — exactly as the picture shows.",
                   ["Eq(2*3, 6)", "Eq(3 + 3, 6)"]),
                   fig_ab),
                tp("Square, circle, square, circle, $\\ldots$ The next shape is:",
                   ["a square", "a circle", "a triangle"],
                   "The repeat is \"square, circle\", $2$ long. Four shapes is two full repeats, so the $5$th starts a new one with a square.",
                   ["Eq(2*2, 4)", "Eq(4 + 1, 5)"]),
                tp("In a pattern with a repeat of $2$, shapes $1$, $3$ and $5$ are:",
                   ["all the same", "all different", "always circles"],
                   "With a repeat of two, every other shape matches: positions $1, 3, 5$ all hold the first shape of the repeat, and $2, 4, 6$ the second.",
                   ["Eq(2*2, 4)", "Eq(4 + 1, 5)"]),
            ]),
            tapq("How long is the repeat?", "Circle, square, triangle, circle, square, triangle. How long is the repeating piece?",
                 ["$3$ shapes", "$6$ shapes", "$2$ shapes", "$1$ shape"],
                 "The circle returns after three shapes, so the repeat is $3$ long — and the six shapes shown are exactly two copies of it: $3 \\times 2 = 6$.",
                 ["Eq(3*2, 6)"]),
            funfact("Patterns are how a rug remembers",
                    "The borders on Mongolian felt rugs repeat because a repeating pattern can be carried by memory rather than by drawing. A maker who knows a four-shape repeat can run a border round a rug of any size, in any order, and it will still close up correctly. The pattern IS the instructions."),
            withfig(teach("Concept B", "Repeating against growing", [
                "Not every pattern repeats. The one below goes $1$, $2$, $3$, $4$ — each step adds one more than the last.",
                "That is a GROWING pattern. It never comes back to where it started, because every step is bigger than the one before: $1 + 1 = 2$, $2 + 1 = 3$, $3 + 1 = 4$.",
                "The test is simple. A repeating pattern eventually returns to its first shape; a growing pattern never does. Ask \"does it come back?\" and you have sorted the two.",
            ]), fig_grow),
            workedset("Repeating or growing?", "Does the pattern come back round?", [
                wex("Is $2, 4, 6, 8$ repeating or growing?",
                    ["Each step adds $2$: $2 + 2 = 4$, $6 + 2 = 8$.",
                     "It never returns to $2$, so it is growing."],
                    "growing",
                    ["Eq(2 + 2, 4)", "Eq(6 + 2, 8)"]),
                wex("Is circle, square, circle, square repeating or growing?",
                    ["The circle comes back after two shapes.",
                     "It returns to its start, so it is repeating — repeat length $2$."],
                    "repeating",
                    ["Eq(2*2, 4)"]),
            ]),
            tryitset("Which kind of pattern?", "Does it return, or keep growing?", [
                tp("$1, 2, 3, 4, 5$ is:",
                   ["a growing pattern", "a repeating pattern",
                    "not a pattern at all"],
                   "Each step adds one and it never comes back to $1$: $4 + 1 = 5$. Growing patterns move away from the start forever.",
                   ["Eq(4 + 1, 5)", "Eq(1 + 1, 2)"]),
                tp("Triangle, triangle, circle, triangle, triangle, circle is:",
                   ["a repeating pattern of length $3$",
                    "a growing pattern",
                    "a repeating pattern of length $2$"],
                   "The piece \"triangle, triangle, circle\" repeats, so the repeat is $3$ long — and six shapes is two copies: $3 \\times 2 = 6$.",
                   ["Eq(3*2, 6)"]),
                tp("$5, 10, 15, 20$ is a growing pattern that adds:",
                   ["$5$ each step", "$10$ each step", "$1$ each step"],
                   "Each step adds five: $5 + 5 = 10$ and $15 + 5 = 20$. It is the five times table, which is a growing pattern rather than a repeating one.",
                   ["Eq(5 + 5, 10)", "Eq(15 + 5, 20)"]),
            ]),
            tapq("The test", "How can you tell a repeating pattern from a growing one?",
                 ["a repeating pattern comes back to its first shape",
                  "a repeating pattern is always shorter",
                  "a growing pattern uses only numbers",
                  "you cannot tell them apart"],
                 "Repeating patterns return to where they started — a repeat of $3$ brings the first shape back at position $4$, since $3 + 1 = 4$. Growing patterns move away forever: $1, 2, 3, 4$ never returns to $1$.",
                 ["Eq(3 + 1, 4)", "Eq(1 + 1, 2)"]),
            recap([
                "A repeating pattern is one short piece said over and over — find the SHORTEST piece that works.",
                "The length of the repeat lets you say what sits at any position without drawing the rest.",
                "A growing pattern changes by the same amount each step and never returns to its start.",
                "Ask \"does it come back?\" to tell the two kinds apart.",
            ]),
            tip("Say the pattern out loud and listen for where your voice starts over. The point at which you repeat yourself is exactly where the repeating piece ends."),
            tryitset("Chapter practice", "Find the repeat, then count on.", [
                tp("Circle, triangle, circle, triangle, $\\ldots$ The $5$th shape is:",
                   ["a circle", "a triangle", "a square"],
                   "The repeat is $2$ long, and four shapes is two full repeats, so the $5$th starts a new one: a circle again.",
                   ["Eq(2*2, 4)", "Eq(4 + 1, 5)"]),
                tp("A pattern with a repeat of $4$ shapes uses how many shapes in three full repeats?",
                   ["$12$", "$7$", "$4$"],
                   "Three copies of a four-shape repeat: $4 \\times 3 = 12$ shapes.",
                   ["Eq(4*3, 12)"]),
                tp("Which of these is a REPEATING pattern?",
                   ["square, circle, square, circle",
                    "$1, 2, 3, 4$",
                    "$10, 20, 30, 40$"],
                   "Only the first comes back to its start. The other two grow by a fixed amount every step and never return.",
                   ["Eq(2*2, 4)", "Eq(10 + 10, 20)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Shape Patterns\"",
                    "Finding the repeating piece is the same habit as finding the step in a number count — and it is the beginning of algebra, where a pattern gets written down as a rule instead of drawn.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 5 — Sorting Shapes
# ==========================================================================

def lesson_sorting():
    fig_sort = fig_groups((3, "3 sides: triangles", C_ACCENT),
                          (4, "4 sides: squares and rectangles", C_WARM),
                          (0, "no sides: circles", C_GREEN))
    fig_two_ways = fig_groups((4, "sorted by sides", C_ACCENT),
                              (4, "sorted by square corners", C_WARM))
    return {
        "slug": "sorting-shapes",
        "title": "Sorting Shapes",
        "concreteComparison": (
            "Tip out a box of shape tiles and you have to decide how to "
            "sort them. By number of sides? By whether the corners are "
            "square? Both are good answers — and the same tile can land "
            "in a different pile depending on the question you asked."),
        "objective": (
            "Sort shapes by a stated rule, describe the rule a sorting "
            "used, and see that one shape can belong to different groups "
            "under different rules."),
        "concept": [
            "**Sorting starts with a rule.** \"Three sides here, four "
            "sides there, no sides in the last pile\" is a rule, and "
            "every tile has exactly one home under it. A sorting without "
            "a stated rule is just a mess.",
            "**Different rules give different piles.** Sort by number of "
            "sides and squares sit with rectangles. Sort by \"are all the "
            "sides equal?\" and the square moves away from the rectangle "
            "to sit with the equal-sided triangle instead.",
            "**A shape can be in several groups at once.** A square has "
            "$4$ sides, $4$ square corners AND $4$ equal sides, so it "
            "belongs in all three of those piles. Which pile it lands in "
            "depends entirely on the question being asked.",
        ],
        "keyIdea": (
            "A sorting is only as clear as its rule — state the rule "
            "first, and remember that a different rule will move the "
            "shapes into different piles."),
        "facts": [
            {"title": "Sorting by sides",
             "latex": "3 + 4 = 7",
             "explanation": "A triangle and a square between them have seven sides."},
            {"title": "One shape, several groups",
             "latex": "4 \\times 1 = 4",
             "explanation": "A square has four sides, four square corners and four equal sides."},
        ],
        "workedExamples": [
            {"id": "g3sh-l5-we1",
             "statement": "Sort a triangle, a square, a rectangle and a circle by number of sides. Which piles result?",
             "note": "State the rule, then place every shape.",
             "solution": ("Three sides: the triangle. Four sides: the square and "
                          "the rectangle together. No sides: the circle. Every "
                          "shape has exactly one home, and the four-sided pile "
                          "holds $2$ of the $4$ shapes."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3 + 4, 7)", "Eq(1 + 2 + 1, 4)"]},
            {"id": "g3sh-l5-we2",
             "statement": "Now sort the same four shapes by \"are all the sides equal?\". What changes?",
             "note": "Watch where the square goes.",
             "solution": ("The square has four equal sides, so it goes in the "
                          "\"yes\" pile. The rectangle's long and short sides "
                          "differ, so it goes in \"no\" — and the two shapes "
                          "that sat together under the last rule are now apart. "
                          "The shapes never changed; the question did."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*1, 4)", "Ne(3, 5)"]},
        ],
        "commonMistakes": [
            {"text": "Sorting without saying what the rule is, so nobody can check the piles.",
             "correction": "State the rule first — \"three sides here, four there\". Without it, two people sorting the same tiles will disagree and neither can be shown to be wrong.",
             "authored": True},
            {"text": "Thinking a shape belongs to only one group forever.",
             "correction": "A square has four sides, four square corners and four equal sides, so it belongs in all three of those piles. Which one it lands in depends on the rule being used.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g3sh-l5-t1",
             "statement": "Two triangles and one rectangle are sorted by sides. How many sides are in each pile?",
             "solution": ("Three-sided pile: two triangles, $2 \\times 3 = 6$ "
                          "sides. Four-sided pile: one rectangle, $4$ sides. "
                          "Altogether $6 + 4 = 10$ sides."),
             "check": ["Eq(2*3, 6)", "Eq(6 + 4, 10)"]},
            {"id": "g3sh-l5-t2",
             "statement": "Under which rule do a square and a rectangle sit in DIFFERENT piles?",
             "solution": ("\"Are all the sides equal?\" separates them — the "
                          "square says yes, the rectangle no. Sorting by number "
                          "of sides or by square corners would keep them "
                          "together, since both have $4$ of each."),
             "check": ["Eq(4*1, 4)", "Ne(3, 5)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "A sorting needs a rule", [
                "Tip out a box of tiles and the first question is not \"where does this go?\" but \"what is the rule?\".",
                "Sort by number of sides and three piles appear, as the picture below shows: three sides, four sides, and no sides at all.",
                "Under that rule every tile has exactly one home, and anyone else sorting the same box would build the same piles. That is what makes a rule worth stating.",
            ]), fig_sort),
            workedset("Sort by the rule", "Say the rule, then place every shape.", [
                wex("Sort a triangle, a square, a rectangle and a circle by number of sides.",
                    ["Three sides: the triangle.",
                     "Four sides: the square and the rectangle.",
                     "No sides: the circle. All $1 + 2 + 1 = 4$ shapes are placed."],
                    "three piles",
                    ["Eq(1 + 2 + 1, 4)", "Eq(3 + 4, 7)"]),
                wex("Sort two triangles and one rectangle by sides, and count the sides in each pile.",
                    ["Three-sided pile: $2 \\times 3 = 6$ sides.",
                     "Four-sided pile: $4$ sides.",
                     "Altogether $6 + 4 = 10$."],
                    "$6$ and $4$",
                    ["Eq(2*3, 6)", "Eq(6 + 4, 10)"]),
            ]),
            tryitset("Which pile?", "Apply the stated rule exactly.", [
                tp("Sorting by number of sides, a square goes with:",
                   ["the rectangle", "the triangle", "the circle"],
                   "Both the square and the rectangle have four straight sides, so that rule puts them together. The triangle has three and the circle none.",
                   ["Eq(4 + 4, 8)", "Eq(3 + 3, 6)"]),
                tp("Sorting by \"has square corners\", a circle goes in the:",
                   ["\"no\" pile", "\"yes\" pile",
                    "\"yes\" pile, because it is round"],
                   "A circle has no corners at all, so it certainly has no square ones: $0 + 0 = 0$.",
                   ["Eq(0 + 0, 0)", "Eq(4*1, 4)"]),
                tp("Three triangles sorted into the three-sided pile contribute how many sides?",
                   ["$9$", "$3$", "$6$"],
                   "Three sides each: $3 \\times 3 = 9$ sides in that pile.",
                   ["Eq(3*3, 9)"]),
            ]),
            tapq("The missing piece", "Two people sort the same box of tiles and get different piles. The most likely reason is:",
                 ["they used different rules",
                  "one of them counted wrongly",
                  "the tiles changed shape",
                  "sorting always gives different answers"],
                 "A stated rule gives every tile exactly one home, so the same rule gives the same piles every time. Different piles almost always means the rule was different — sorting by sides puts a square with a rectangle, sorting by equal sides does not.",
                 ["Eq(4 + 4, 8)", "Ne(3, 5)"]),
            funfact("Sorting is how libraries work",
                    "Every library in the world faces your tile problem on a much bigger scale, and solves it the same way: choose a rule and state it clearly enough that a stranger can find the book. The rule matters more than the shelves — change it, and every book moves."),
            withfig(teach("Concept B", "Change the rule, move the shapes", [
                "Now sort the same tiles by a different rule: \"are all the sides equal?\"",
                "The square says yes; the rectangle, with its long and short sides, says no. Two shapes that sat happily together under the first rule are now in different piles — the picture below shows the same tiles landing two different ways.",
                "Nothing about the shapes changed. Only the question did. That is why a square can be in the four-sided pile, the square-corner pile AND the equal-sides pile — it depends entirely on what you asked.",
            ]), fig_two_ways),
            workedset("One shape, several groups",
                      "Ask what the rule is before deciding.", [
                wex("Under which rule do a square and a rectangle sit apart?",
                    ["Both have $4$ sides and $4$ square corners, so those rules keep them together.",
                     "\"All sides equal?\" separates them: the square yes, the rectangle no."],
                    "all sides equal",
                    ["Eq(4*1, 4)", "Ne(3, 5)"]),
                wex("Name three piles a square could belong to.",
                    ["Four sides; four square corners; all sides equal.",
                     "It qualifies for all three, because it has $4$ of each."],
                    "three piles",
                    ["Eq(4*1, 4)", "Eq(4 + 4, 8)"]),
            ]),
            tryitset("Which rule?", "The rule decides where a shape lands.", [
                tp("Which rule puts a square and a rectangle in DIFFERENT piles?",
                   ["are all the sides equal?", "how many sides?",
                    "does it have square corners?"],
                   "Both have four sides and four square corners, so only the equal-sides rule separates them.",
                   ["Eq(4 + 4, 8)", "Ne(3, 5)"]),
                tp("A square can belong to:",
                   ["several piles, depending on the rule",
                    "only the four-sided pile",
                    "no pile at all"],
                   "It has four sides, four square corners and four equal sides, so it qualifies for each of those piles. The rule in use decides which one it lands in.",
                   ["Eq(4*1, 4)"]),
                tp("Sorting by \"rolls or does not roll\", a circle drawn on paper is:",
                   ["not being sorted — it is a flat shape, not a solid",
                    "in the \"rolls\" pile",
                    "in the \"does not roll\" pile"],
                   "Rolling is something SOLIDS do. A circle is flat and stays on the page; the solid that rolls is the sphere, which has $0$ flat faces.",
                   ["Eq(0 + 0, 0)", "Eq(0*6, 0)"]),
            ]),
            tapq("Same tiles, two answers", "Under \"number of sides\" a square sits with the rectangle; under \"all sides equal\" it does not. What changed?",
                 ["the rule", "the square", "the rectangle",
                  "the number of sides"],
                 "Neither shape changed at all — the square still has $4$ sides and $4$ square corners. Only the question being asked moved it, which is why a sorting is worth nothing without its rule stated.",
                 ["Eq(4*1, 4)", "Eq(4 + 4, 8)", "Ne(3, 5)"]),
            recap([
                "Every sorting begins with a stated rule; without one the piles cannot be checked.",
                "Different rules put the same shapes into different piles.",
                "A square belongs to the four-sided, square-cornered AND equal-sided groups.",
                "When two sortings disagree, the rule is almost always the difference.",
            ]),
            tip("Before you sort anything, write the rule at the top of the page. It is the only way to check your own work afterwards — and the only way anyone else can agree with you."),
            tryitset("Chapter practice", "Rule first, then the piles.", [
                tp("Sorting by sides, which two shapes share a pile?",
                   ["a square and a rectangle", "a square and a circle",
                    "a triangle and a rectangle"],
                   "Squares and rectangles both have four straight sides. Triangles have three and circles none.",
                   ["Eq(4 + 4, 8)", "Eq(3 + 3, 6)"]),
                tp("Four triangles contribute how many sides to their pile?",
                   ["$12$", "$4$", "$7$"],
                   "Three sides each: $4 \\times 3 = 12$ sides.",
                   ["Eq(4*3, 12)"]),
                tp("Two people sort the same tiles and get different piles. You should first ask:",
                   ["what rule each one used",
                    "who counted faster",
                    "how many tiles there were"],
                   "The same rule always gives the same piles, so a disagreement points at the rule before it points at anyone's counting.",
                   ["Eq(4*1, 4)", "Ne(3, 5)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Sorting Shapes\" — and the topic",
                    "Naming, square corners, solids, patterns and sorting. Every one of them came down to what you can count on a shape and what rule you are counting it for. Next comes measuring, where counting turns into units.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pr1 = shape(RECTANGLE, right_at=0)
    fig_pr5 = shape(SLANTED, color=C_WARM)
    return [
        withprobfig(prob("g3sh-pr1", "Name the shape shown, count its sides and corners, and say how many of its corners are square.",
             "Four straight sides with four square corners and opposite sides matching: a rectangle. It has $4$ sides and $4$ corners, so $4 + 4 = 8$ things to count, and all $4 \\times 1 = 4$ corners are square.",
             ["Eq(4 + 4, 8)", "Eq(4*1, 4)"]), fig_pr1),
        prob("g3sh-pr2", "Explain why every square is a rectangle but most rectangles are not squares.",
             "A rectangle needs four straight sides and four square corners, and a square has both — so every square qualifies. A square adds one more condition, that all four sides are equal, and most rectangles fail it: a $3$ by $5$ rectangle has sides totalling $3 + 5 + 3 + 5 = 16$ from unequal lengths, while a square of side $4$ reaches the same $4 \\times 4 = 16$ from equal ones.",
             ["Eq(3 + 5 + 3 + 5, 16)", "Eq(4*4, 16)", "Ne(3, 5)"]),
        prob("g3sh-pr3", "How would you check whether a door frame has square corners, using only a sheet of paper?",
             "Hold a corner of the paper against each corner of the frame. Paper corners are square, so an exact fit — no gap, no overlap — means the frame corner is square too. A properly built frame passes at all $4 \\times 1 = 4$ corners.",
             ["Eq(4*1, 4)", "Eq(4 + 4, 8)"]),
        prob("g3sh-pr4", "A cube, a sphere and a cylinder are put on a sloping board. Say what each does and why.",
             "The cube has $6$ flat faces and no curved surface, so it slides or stays put but never rolls. The sphere has $0$ flat faces and is curved all over, so it rolls in any direction. The cylinder has $2$ flat faces and a curved side: on its end it stays, on its side it rolls straight. What a solid does depends on which surface touches the board.",
             ["Eq(6*1, 6)", "Eq(0*6, 0)", "Eq(2 - 1, 1)"]),
        withprobfig(prob("g3sh-pr5", "The shape shown has four straight sides. Explain why it is not a rectangle.",
             "A rectangle needs all four corners square, and a page corner would fit none of this shape's corners — two are sharper than square and two blunter, $2 + 2 = 4$ corners that all fail the test. Four sides alone is only half of what a rectangle requires.",
             ["Eq(2 + 2, 4)", "Eq(4*1, 4)"]), fig_pr5),
        prob("g3sh-pr6", "A pattern goes square, circle, circle, square, circle, circle. Give the repeat length and the $8$th shape.",
             "The repeating piece is \"square, circle, circle\", $3$ shapes long. Six shapes make two full repeats ($3 \\times 2 = 6$), so the $7$th is a square and the $8$th is a circle.",
             ["Eq(3*2, 6)", "Eq(6 + 1, 7)", "Eq(7 + 1, 8)"]),
        prob("g3sh-pr7", "Sort a triangle, a square, a rectangle and a circle first by number of sides, then by whether all sides are equal. Say which shape moves.",
             "By sides: triangle alone; square and rectangle together; circle alone. By equal sides: triangle and square in the \"yes\" pile, rectangle in \"no\", circle in neither since it has $0 + 0 = 0$ sides and corners. The square is what moves — it leaves the rectangle and joins the triangle.",
             ["Eq(1 + 2 + 1, 4)", "Eq(0 + 0, 0)", "Ne(3, 5)"]),
        prob("g3sh-pr8", "Two cubes, one cone and one sphere sit on a table. How many flat faces are there altogether, and how many of the four solids can be stacked on?",
             "Cubes: $2 \\times 6 = 12$ flat faces. Cone: $1$. Sphere: $0$. Altogether $12 + 1 + 0 = 13$. Three of the four can be stacked on — both cubes and the cone, each of which has at least one flat face upward; the sphere cannot, having none.",
             ["Eq(2*6, 12)", "Eq(12 + 1, 13)", "Eq(0*6, 0)"]),
    ]


def test_bank():
    return [
        prob("g3sh-x1", "A shape has three straight sides. Name it, count its corners, and say the most square corners it could have.",
             "Three straight sides makes it a triangle, and it has three corners to match — $3 + 3 = 6$ things to count. At most $3 - 2 = 1$ of those corners can be square: two square corners would send the remaining sides alongside each other so they never met, and the shape could not close.",
             ["Eq(3 + 3, 6)", "Eq(3 - 2, 1)"]),
        prob("g3sh-x2", "Describe two different ways to sort a square, a rectangle, a triangle and a circle, and say which shapes change pile between them.",
             "By number of sides: triangle ($3$), square and rectangle together ($4$ each), circle ($0$). By whether all sides are equal: square and triangle in \"yes\", rectangle in \"no\", circle apart with $0 + 0 = 0$ sides and corners. The square moves — it leaves the rectangle and joins the triangle, because the rule changed and the shapes did not.",
             ["Eq(3 + 3, 6)", "Eq(4 + 4, 8)", "Eq(0 + 0, 0)"]),
        prob("g3sh-x3", "Why does a cylinder both roll and stand still, while a sphere only rolls?",
             "A cylinder has $2$ flat faces at its ends and a curved side. Stood on an end, a flat face touches the table and it stays put; on its side, the curved surface touches and it rolls. A sphere has $0$ flat faces — it is curved everywhere — so there is no surface that could hold it still.",
             ["Eq(2 - 1, 1)", "Eq(2 + 1, 3)", "Eq(0*6, 0)"]),
        prob("g3sh-x4", "A pattern goes triangle, square, square, triangle, square, square. Give the repeat, the $9$th shape, and explain how you knew without drawing.",
             "The repeat is \"triangle, square, square\", $3$ long. Nine shapes is exactly three full repeats ($3 \\times 3 = 9$), so the $9$th shape is the LAST of a repeat — a square. Knowing the repeat length lets you count ahead instead of drawing.",
             ["Eq(3*3, 9)", "Eq(3*2, 6)"]),
        prob("g3sh-x5", "How many square corners have three rectangles between them, and how many sides?",
             "Each rectangle has four square corners and four sides. Corners: $3 \\times 4 = 12$. Sides: $3 \\times 4 = 12$ as well, since sides and corners always match on a flat shape — $12 + 12 = 24$ things to count in all.",
             ["Eq(3*4, 12)", "Eq(12 + 12, 24)"]),
        prob("g3sh-x6", "Bat says a shape with four sides must be a rectangle. Give a counterexample and explain the test he skipped.",
             "A leaning four-sided shape has four straight sides but no square corners — a page corner fits none of them, two being sharper than square and two blunter. Bat checked only the sides; the missing test is holding a page corner against each corner, and a rectangle must pass all $4 \\times 1 = 4$ times.",
             ["Eq(2 + 2, 4)", "Eq(4*1, 4)", "Eq(4 + 4, 8)"]),
    ]


def main():
    topic = {
        "slug": "shapes-sides-and-corners",
        "title": "Shapes, Sides & Corners",
        "grade": 3,
        "status": "published",
        "blurb": ("Naming circles, triangles, squares and rectangles by what "
                  "you can count on them, testing a square corner with the "
                  "corner of a page, the solid shapes and whether each rolls "
                  "or stacks, repeating shape patterns, and sorting by a "
                  "stated rule."),
        "lessons": [
            lesson_naming(),
            lesson_square_corners(),
            lesson_solids(),
            lesson_patterns(),
            lesson_sorting(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "shapes-sides-and-corners.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
