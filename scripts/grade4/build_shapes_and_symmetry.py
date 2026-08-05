#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Grade 4 — Topic: Shapes & Symmetry.

Naming 2-D shapes by their sides, the right angle as a quarter turn,
sorting quadrilaterals by their rules (and why every square is a
rectangle), the fold test for line symmetry, and the faces, edges and
vertices of 3-D solids — with the faces-plus-vertices-minus-edges
receipt that catches every miscount.

Through-line: A SHAPE KEEPS ITS PROMISES — count the sides, test the
corners, try the fold. Every lesson is one promise and one test: the
side count names the shape, the page corner tests the angle, the fold
tests the mirror, and the counting receipt tests the solid.

Same construction as every Grade 4 builder: figures are built from the
SAME variables as the statements (a square is DRAWN square, a symmetry
line passes through the computed axis), and every check is
sympy-asserted with exact integers before the JSON is written.

Run: python3 scripts/grade4/build_shapes_and_symmetry.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from g4build import (withprobfig, funfact, prob, recap, tapq, teach, tip, tp,  # noqa: E402
                     tryitset, wex, workedset, write_topic, withfig,
                     fig_groups, fig_geo, P, seg, ang, poly,
                     C_ACCENT, C_WARM, C_GREEN, C_NEUTRAL)


def reg_poly_pts(n, cx=5.0, cy=5.2, r=4.0, start=90.0):
    """Vertices of a regular n-gon — honest coordinates, equal sides."""
    pts = []
    for i in range(n):
        a = math.radians(start + 360.0 * i / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def named(pts, prefix="A"):
    """Turn (x, y) tuples into labelled P() points A, B, C, ..."""
    letters = "ABCDEFGHJK"
    return [P(letters[i], x, y) for i, (x, y) in enumerate(pts)]


def side_lengths(pts):
    """Length of every side of the closed polygon, in order."""
    n = len(pts)
    return [math.hypot(pts[(i + 1) % n][0] - pts[i][0],
                       pts[(i + 1) % n][1] - pts[i][1]) for i in range(n)]


def corner_angles(pts):
    """Interior angle at every vertex, in degrees."""
    n = len(pts)
    out = []
    for i in range(n):
        (px, py), (cx, cy), (qx, qy) = pts[i - 1], pts[i], pts[(i + 1) % n]
        ux, uy = px - cx, py - cy
        vx, vy = qx - cx, qy - cy
        cos = ((ux * vx + uy * vy)
               / (math.hypot(ux, uy) * math.hypot(vx, vy)))
        out.append(math.degrees(math.acos(max(-1.0, min(1.0, cos)))))
    return out


def assert_no_equal_sides_no_right_angles(pts):
    """Guard the shape the text calls 'no equal sides, no right angles'.

    A student runs the two tests this topic teaches on the PICTURE, so the
    picture has to survive them: every pair of sides must differ by a
    margin you can see, and no corner may come near the page corner's 90
    degrees. Fails the build rather than shipping a figure that argues
    with its own stem."""
    sides = side_lengths(pts)
    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            assert abs(sides[i] - sides[j]) > 0.5, (
                "sides %d and %d read equal: %.3f vs %.3f"
                % (i, j, sides[i], sides[j]))
    for i, a in enumerate(corner_angles(pts)):
        assert abs(a - 90.0) > 15.0, (
            "corner %d is %.2f degrees — the page-corner test would call "
            "it right" % (i, a))


# ==========================================================================
# Lesson 1 — 2-D Shapes
# ==========================================================================

def lesson_two_d_shapes():
    # Real-coordinate polygons: a triangle, a quadrilateral, a regular
    # pentagon and a regular hexagon.
    tri_pts = named([(1.5, 1.5), (8.5, 1.5), (5, 7.5)])
    fig_tri = fig_geo(tri_pts, poly(["A", "B", "C"], color=C_ACCENT),
                      height=190)
    quad_pts = named([(1.5, 2), (9, 1.5), (8, 7), (3, 8)])
    fig_quad = fig_geo(quad_pts, poly(["A", "B", "C", "D"], color=C_WARM),
                       height=200)
    pent_pts = named(reg_poly_pts(5))
    fig_pent = fig_geo(pent_pts, poly(["A", "B", "C", "D", "E"],
                                      color=C_GREEN), height=200)
    hex_pts = named(reg_poly_pts(6))
    fig_hex = fig_geo(hex_pts, poly(["A", "B", "C", "D", "E", "F"],
                                    color=C_ACCENT), height=200)
    hex2_pts = named(reg_poly_pts(6, start=60.0))
    fig_hex2 = fig_geo(hex2_pts, poly(["A", "B", "C", "D", "E", "F"],
                                      color=C_WARM), height=200)
    tri2_pts = named([(2, 1.5), (9, 3), (4, 7.5)])
    fig_tri2 = fig_geo(tri2_pts, poly(["A", "B", "C"], color=C_GREEN),
                       height=190)
    return {
        "slug": "two-d-shapes",
        "title": "2-D Shapes",
        "concreteComparison": (
            "Lay three straight sticks on the ground so they close up "
            "into a ring: a triangle. Add a fourth stick: a "
            "quadrilateral. Five sticks: a pentagon. Six: a hexagon. "
            "A shape's name is nothing more than a COUNT of its "
            "straight sides — and wherever two sticks meet, a corner "
            "appears, so the corners always match the sides, one for "
            "one."),
        "objective": (
            "Name 2-D shapes by counting their straight sides — "
            "triangle, quadrilateral, pentagon, hexagon — and check "
            "that every shape has exactly as many corners (vertices) "
            "as sides."),
        "concept": [
            "**The name is a count.** Three straight sides make a "
            "triangle, four a quadrilateral, five a pentagon, six a "
            "hexagon. Nothing else about the shape — big or small, "
            "tall or squashed, tilted or upright — changes its name.",
            "**Sides come with corners.** Walk around the boundary: "
            "every side ends exactly where the next one starts, at a "
            "corner (a VERTEX). So a pentagon has $5$ corners, a "
            "hexagon $6$ — the two counts can never differ.",
            "**Only straight sides count.** A circle has no straight "
            "sides at all, so it earns no side-count name — it is not "
            "a polygon. And a shape must CLOSE: sticks that leave a "
            "gap make no shape yet.",
        ],
        "keyIdea": (
            "Count the straight sides: three is a triangle, four a "
            "quadrilateral, five a pentagon, six a hexagon — and the "
            "corners always match the count, side for side."),
        "facts": [
            {"title": "Names by side count",
             "latex": "3 \\to \\text{triangle} \\quad 4 \\to \\text{quadrilateral} \\quad 5 \\to \\text{pentagon} \\quad 6 \\to \\text{hexagon}",
             "explanation": "The name is the count — nothing more, nothing less."},
            {"title": "Sides = corners",
             "latex": "\\text{hexagon: } 6 \\text{ sides and } 6 \\text{ vertices}",
             "explanation": "Each side ends at the corner where the next one starts, so the counts match."},
        ],
        "workedExamples": [
            {"id": "g4sh-l1-we1",
             "statement": "A shape has $5$ straight sides. Name it, and count its corners without looking at it.",
             "note": "Every side has two ends; every corner joins exactly two ends.",
             "solution": ("Five sides: a PENTAGON. Its $5$ sides have $5 \\times 2 "
                          "= 10$ ends, and every corner is a meeting of exactly "
                          "$2$ ends: $10 \\div 2 = 5$ corners. Sides and corners "
                          "always match."),
             "badges": [{"text": "core"}],
             "check": ["Eq(5*2, 10)", "Eq(Rational(10,2), 5)"]},
            {"id": "g4sh-l1-we2",
             "statement": "A triangle and a hexagon are drawn side by side. How many sides in total — and how many corners in total?",
             "note": "Count each shape, then add.",
             "solution": ("Sides: $3 + 6 = 9$. Corners match sides shape by "
                          "shape ($3$ and $6$), so the corner total is the same "
                          "$9$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3 + 6, 9)"]},
        ],
        "commonMistakes": [
            {"text": "Calling every four-sided shape a square.",
             "correction": "Quadrilateral is the family name for ANY four straight sides. A square is one strict member of that family — most quadrilaterals are not squares.",
             "authored": True},
            {"text": "Thinking a triangle standing on its point is a different shape.",
             "correction": "The name counts sides, not which way is up. Turn a triangle any way you like — three sides, three corners, still a triangle.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4sh-l1-t1",
             "statement": "A hexagon and a quadrilateral stand together. How many sides do they have between them?",
             "solution": "$6 + 4 = 10$ sides (and $10$ corners too, since each shape's corners match its sides).",
             "check": ["Eq(6 + 4, 10)"]},
            {"id": "g4sh-l1-t2",
             "statement": "A shape has $6$ corners. Name it and count its sides.",
             "solution": "Six corners means six sides: a HEXAGON. Receipt: $6$ sides have $6 \\times 2 = 12$ ends, and $12 \\div 2 = 6$ corners — the counts agree.",
             "check": ["Eq(6*2, 12)", "Eq(Rational(12,2), 6)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Count the straight sides", [
                "A shape keeps its promises — and the first promise is its NAME: count the straight sides. Three sides: triangle. Four: quadrilateral. Five: pentagon. Six: hexagon.",
                "Nothing else matters for the name — not the size, not the colour, not which way up it sits. A squashed triangle and a tall one are both triangles.",
                "Only STRAIGHT sides count, and the shape must close into a ring. A circle has no straight sides, so it takes no side-count name.",
            ]), fig_tri),
            workedset("Naming shapes",
                      "Count the sides; the count is the name.", [
                withfig(wex("Name the shape in the picture, and count its corners.",
                    ["Five straight sides: a pentagon.",
                     "Corners match sides: $5 \\times 2 = 10$ side-ends, $10 \\div 2 = 5$ corners."],
                    "pentagon — $5$ sides, $5$ corners",
                    ["Eq(5*2, 10)", "Eq(Rational(10,2), 5)"]), fig_pent),
                wex("A triangle road sign and a hexagon tile: how many sides in total?",
                    ["Count each: $3$ and $6$.",
                     "Together: $3 + 6 = 9$ sides — and $9$ corners too."],
                    "$9$ sides",
                    ["Eq(3 + 6, 9)"]),
            ]),
            tryitset("Count and name", "Sides first, name second.", [
                withfig(tp("The shape in the picture has $4$ straight sides. It is a:",
                   ["quadrilateral", "pentagon", "triangle"],
                   "Four straight sides: a quadrilateral — the family name for every four-sided shape. Receipt: $4 \\times 2 = 8$ side-ends, $8 \\div 2 = 4$ corners.",
                   ["Eq(4*2, 8)", "Eq(Rational(8,2), 4)"]), fig_quad),
                tp("A pentagon has how many more sides than a triangle?",
                   ["$2$", "$1$", "$5$"],
                   "$5 - 3 = 2$ more sides. Check by adding back: $2 + 3 = 5$ ✓.",
                   ["Eq(5 - 3, 2)", "Eq(2 + 3, 5)"]),
                tp("Which shape has the MOST corners?",
                   ["hexagon", "pentagon", "quadrilateral"],
                   "Corners match sides, so compare side counts: $6 > 5 > 4$ — the hexagon wins.",
                   ["6 > 5", "5 > 4"]),
            ]),
            tapq("Corners without counting", "A polygon has $8$ straight sides. How many vertices must it have?",
                 ["$8$", "$16$", "$4$", "$6$"],
                 "Sides and vertices always match: $8$ sides have $8 \\times 2 = 16$ ends, and each vertex joins exactly $2$ ends — $16 \\div 2 = 8$ vertices. ($16$ counts the side-ENDS, not the corners.)",
                 ["Eq(8*2, 16)", "Eq(Rational(16,2), 8)"]),
            funfact("The names tell on themselves",
                    "POLYGON is Greek for \"many angles\" — and the shape names carry their counts openly: TRIangle is three angles, PENTAgon five, HEXAgon six. QUADRILATERAL switches to Latin and counts sides instead: four of them. Say the name slowly and it counts itself for you."),
            withfig(teach("Concept B", "Corners match sides — the receipt", [
                "Here is why the counts can never differ. Every side has $2$ ends. A hexagon's $6$ sides have $6 \\times 2 = 12$ ends.",
                "Every corner is a meeting place of exactly $2$ ends — one side arriving, the next one leaving. So the corners number $12 \\div 2 = 6$: the same as the sides.",
                "This works for every polygon: double the sides, halve the ends, and you have counted the corners without touching the picture.",
            ]), fig_hex),
            workedset("The side-ends receipt",
                      "Double the sides, halve the result — that counts the corners.", [
                withfig(wex("Count the sides and vertices of the hexagon in the picture.",
                    ["Six straight sides. Ends: $6 \\times 2 = 12$.",
                     "Vertices: $12 \\div 2 = 6$ — sides and corners match."],
                    "$6$ sides, $6$ vertices",
                    ["Eq(6*2, 12)", "Eq(Rational(12,2), 6)"]), fig_hex2),
                wex("A polygon has $9$ sides. How many corners?",
                    ["Ends: $9 \\times 2 = 18$.",
                     "Corners: $18 \\div 2 = 9$ — always the same as the sides."],
                    "$9$ corners",
                    ["Eq(9*2, 18)", "Eq(Rational(18,2), 9)"]),
            ]),
            tryitset("Receipt the corners", "Sides and vertices — one count, two names.", [
                tp("A hexagon has how many vertices?",
                   ["$6$", "$12$", "$5$"],
                   "Same as its sides: $6$. The $12$ counts side-ends ($6 \\times 2$) — halve it to land on the corners.",
                   ["Eq(6*2, 12)", "Eq(Rational(12,2), 6)"]),
                tp("Two pentagons stand side by side. Total vertices:",
                   ["$10$", "$5$", "$25$"],
                   "Each pentagon carries $5$ vertices: $2 \\times 5 = 10$.",
                   ["Eq(2*5, 10)"]),
                withfig(tp("For the triangle in the picture, sides plus vertices makes:",
                   ["$6$", "$3$", "$9$"],
                   "Three sides and three matching vertices: $3 + 3 = 6$.",
                   ["Eq(3 + 3, 6)"]), fig_tri2),
            ]),
            tapq("One count, two names", "A quadrilateral's sides and vertices together number:",
                 ["$8$", "$4$", "$6$", "$16$"],
                 "Four sides, four matching vertices: $4 + 4 = 8$. (Answering $4$ counts only one of the two; $16$ doubles everything.)",
                 ["Eq(4 + 4, 8)"]),
            recap([
                "The name is a count: 3 triangle, 4 quadrilateral, 5 pentagon, 6 hexagon.",
                "Size, colour and which-way-up never change the name.",
                "Corners (vertices) always match sides — every side ends where the next begins.",
                "The receipt: sides times 2 ends, divided by 2, counts the corners.",
                "Only straight sides count, and the shape must close — a circle is not a polygon.",
            ]),
            tip("For every shape below, touch each side as you count it — then say the name. Count first, name second, every time."),
            tryitset("Mixed practice", "Names, counts, and the receipt together.", [
                tp("A hexagon has how many more sides than a pentagon?",
                   ["$1$", "$2$", "$11$"],
                   "$6 - 5 = 1$; adding back, $1 + 5 = 6$ ✓.",
                   ["Eq(6 - 5, 1)", "Eq(1 + 5, 6)"]),
                withfig(tp("The picture shows a shape with $4$ straight sides. Its name is:",
                   ["quadrilateral", "hexagon", "pentagon"],
                   "Four sides — a quadrilateral, whatever its slant. Receipt: $4 \\times 2 = 8$ ends, $8 \\div 2 = 4$ corners.",
                   ["Eq(4*2, 8)", "Eq(Rational(8,2), 4)"]), fig_quad),
                tp("One triangle, one quadrilateral, one pentagon and one hexagon: total sides?",
                   ["$18$", "$15$", "$20$"],
                   "$3 + 4 + 5 + 6 = 18$ sides — and $18$ corners across the four shapes too.",
                   ["Eq(3 + 4 + 5 + 6, 18)"]),
                tp("Which of these is NOT a polygon?",
                   ["a circle", "a triangle", "a hexagon"],
                   "A polygon needs at least $3$ straight sides; a circle has $0$ straight sides — no straight sides, no side-count name.",
                   ["0 < 3"]),
                tp("A polygon has $10$ sides. Its vertices number:",
                   ["$10$", "$20$", "$5$"],
                   "The receipt: $10 \\times 2 = 20$ side-ends, $20 \\div 2 = 10$ vertices — corners match sides, always.",
                   ["Eq(10*2, 20)", "Eq(Rational(20,2), 10)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"2-D Shapes\"",
                    "Count the sides and the shape names itself — the first promise a shape keeps. Next: the corner every builder trusts — the right angle, a quarter of a full turn.",
                    eyebrow="Chapter complete"),
        ]},
    }


# ==========================================================================
# Lesson 2 — Right Angles
# ==========================================================================

def lesson_right_angles():
    # A true right angle: rays from O along (7,0) and (0,6).
    fig_right = fig_geo(
        [P("O", 2, 2), P("A", 9, 2), P("B", 2, 8)],
        [seg("O", "A", color=C_ACCENT), seg("O", "B", color=C_ACCENT),
         ang("O", "A", "B", right=True)],
        height=200)
    # An angle smaller than a right angle: ray at 45 degrees (direction 6,6).
    fig_small = fig_geo(
        [P("O", 2, 2), P("A", 9, 2), P("B", 8, 8)],
        [seg("O", "A", color=C_WARM), seg("O", "B", color=C_WARM),
         ang("O", "A", "B")],
        height=200)
    # An angle bigger than a right angle: direction (-2,5) from O(3,2).
    fig_big = fig_geo(
        [P("O", 3, 2), P("A", 9, 2), P("B", 1, 7)],
        [seg("O", "A", color=C_GREEN), seg("O", "B", color=C_GREEN),
         ang("O", "A", "B")],
        height=200)
    # Four right angles filling a full turn around O.
    fig_cross = fig_geo(
        [P("O", 5, 5), P("N", 5, 9), P("E", 9, 5), P("S", 5, 1), P("W", 1, 5)],
        [seg("O", "N", color=C_ACCENT), seg("O", "E", color=C_ACCENT),
         seg("O", "S", color=C_ACCENT), seg("O", "W", color=C_ACCENT),
         ang("O", "N", "E", right=True), ang("O", "E", "S", right=True),
         ang("O", "S", "W", right=True), ang("O", "W", "N", right=True)],
        height=210)
    # A window corner passing the page-corner test.
    fig_window = fig_geo(
        [P("A", 2, 2), P("B", 8, 2), P("C", 8, 7), P("D", 2, 7)],
        poly(["A", "B", "C", "D"], color=C_NEUTRAL) +
        [ang("A", "B", "D", right=True), ang("B", "C", "A", right=True),
         ang("C", "D", "B", right=True), ang("D", "A", "C", right=True)],
        height=200)
    return {
        "slug": "right-angles",
        "title": "Right Angles",
        "concreteComparison": (
            "Stand facing the ger door, then turn until you face the "
            "wall beside it: a QUARTER of a full spin. That turn has "
            "a name — the RIGHT angle — and you carry a tester "
            "everywhere: the corner of this page. Slide the page "
            "corner into any corner of the room; if it fits exactly, "
            "the corner is right. Four quarter turns bring you back "
            "to the door: four right angles fill a full turn."),
        "objective": (
            "Recognise a right angle as a quarter turn, test corners "
            "with the page corner, and sort angles as smaller than, "
            "equal to, or bigger than a right angle."),
        "concept": [
            "**A right angle is a quarter turn.** A full spin measures "
            "$360$ degrees, and a quarter of it is $90$: $4 \\times 90 "
            "= 360$. The page's corner, the window's corner, the cross "
            "on squared paper — all right angles.",
            "**The page corner is your tester.** Slide it into a "
            "corner: fits exactly — right angle; a gap is left over — "
            "the angle is SMALLER than right; the page corner sinks in "
            "with room to spare — BIGGER than right.",
            "**Two right angles make a straight line.** Half a spin: "
            "$2 \\times 90 = 180$. So a straight line holds two page "
            "corners, and a full turn holds four.",
        ],
        "keyIdea": (
            "A right angle is a quarter of a full turn — 90 degrees; "
            "two of them make a straight line (180) and four fill the "
            "whole turn (360). Test the corners with the page corner."),
        "facts": [
            {"title": "The quarter turn",
             "latex": "4 \\times 90^\\circ = 360^\\circ",
             "explanation": "Four page corners around one point fill a complete spin."},
            {"title": "The straight line",
             "latex": "2 \\times 90^\\circ = 180^\\circ",
             "explanation": "Two right angles side by side flatten into a straight line — half a turn."},
        ],
        "workedExamples": [
            {"id": "g4sh-l2-we1",
             "statement": "Four streets meet at a crossing, and every corner passes the page-corner test. Show that the four corners together make one full turn.",
             "note": "A right angle is a quarter turn; count the quarters.",
             "solution": ("Each corner is a right angle: $90$ degrees, a quarter "
                          "turn. Four quarters: $4 \\times 90 = 360$ degrees — "
                          "one complete spin, exactly. And $360 \\div 4 = 90$ "
                          "confirms each corner's share."),
             "badges": [{"text": "core"}],
             "check": ["Eq(4*90, 360)", "Eq(Rational(360,4), 90)"]},
            {"id": "g4sh-l2-we2",
             "statement": "Two right angles sit side by side. What do they make together?",
             "note": "Quarter plus quarter is half.",
             "solution": ("$90 + 90 = 180$ degrees — half a full turn, which is a "
                          "STRAIGHT line. That is why a straight edge holds "
                          "exactly two page corners: $180 \\div 90 = 2$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(90 + 90, 180)", "Eq(Rational(180,90), 2)"]},
        ],
        "commonMistakes": [
            {"text": "Thinking a right angle tilted on its side stops being right.",
             "correction": "A quarter turn is a quarter turn whichever way the arms point. Test with the page corner, not with \"does it look like an upright L\".",
             "authored": True},
            {"text": "Judging an angle by the length of its arms — long arms, big angle.",
             "correction": "An angle is the TURN between the arms, not their length. The page-corner test ignores arm length completely — that is why it works.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4sh-l2-t1",
             "statement": "How many right angles fit along a straight line? And in a full turn?",
             "solution": "A straight line is half a turn: $2 \\times 90 = 180$, so $2$ right angles. A full turn: $4 \\times 90 = 360$, so $4$.",
             "check": ["Eq(2*90, 180)", "Eq(4*90, 360)"]},
            {"id": "g4sh-l2-t2",
             "statement": "An angle is bigger than the page corner but smaller than a straight line. How much room lies between those two landmarks?",
             "solution": "Between the quarter turn ($90$) and the half turn ($180$) lies $180 - 90 = 90$ degrees — a whole extra quarter turn of room. Check: $90 + 90 = 180$ ✓.",
             "check": ["Eq(180 - 90, 90)", "Eq(90 + 90, 180)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The quarter turn and its tester", [
                "Test the corners — that is this lesson's promise. A full spin is $360$ degrees; a QUARTER of it is the RIGHT angle: $90$ degrees, because $4 \\times 90 = 360$.",
                "Your tester travels with you: the page's corner. Fits a corner exactly — right angle. Gap left over — smaller than right. Sinks in with room to spare — bigger than right.",
                "The arms' length never votes: an angle is TURN, not ink. A tiny drawn corner can hold a bigger turn than a huge one.",
            ]), fig_right),
            workedset("Testing corners",
                      "Fit the page corner; read the result.", [
                withfig(wex("The angle at $O$ in the picture fits the page corner exactly. Name it — and say how many like it fill a full turn.",
                    ["An exact fit: a RIGHT angle, $90$ degrees.",
                     "A full turn is $360$: $360 \\div 90 = 4$ of them fill it, since $4 \\times 90 = 360$."],
                    "a right angle; $4$ fill a full turn",
                    ["Eq(Rational(360,90), 4)", "Eq(4*90, 360)"]), fig_right),
                wex("The hands of a clock at 3:00 — what angle do they make?",
                    ["The minute hand points straight up, the hour hand a quarter of the way round.",
                     "A quarter of the full face: $360 \\div 4 = 90$ degrees — a right angle."],
                    "a right angle",
                    ["Eq(Rational(360,4), 90)"]),
            ]),
            tryitset("Quarter-turn thinking", "Fit the tester, count the quarters.", [
                tp("Four right angles together make:",
                   ["a full turn", "a straight line", "half a right angle"],
                   "Four quarters make one whole spin: $4 \\times 90 = 360$ degrees.",
                   ["Eq(4*90, 360)"]),
                withfig(tp("You slide the page corner into the angle at $O$ in the picture, and a gap is left over. The angle is:",
                   ["smaller than a right angle", "bigger than a right angle", "exactly a right angle"],
                   "A leftover gap means the angle did not use the whole quarter turn — it is smaller than right. (This one is half a right angle: $90 \\div 2 = 45$, and $45 < 90$.)",
                   ["Eq(Rational(90,2), 45)", "45 < 90"]), fig_small),
                tp("Two right angles side by side make:",
                   ["a straight line", "a full turn", "another right angle"],
                   "$90 + 90 = 180$ degrees — half a turn, flat as a stretched rope.",
                   ["Eq(90 + 90, 180)"]),
            ]),
            tapq("The page-corner test", "You slide the page's corner into a door-frame corner and it fits exactly. The door frame's corner is:",
                 ["a right angle — a quarter turn", "half a turn", "a full turn", "too big to test"],
                 "An exact fit IS the definition: the corner holds exactly one quarter of a spin, $360 \\div 4 = 90$ degrees. Door frames are built that way on purpose — doors only swing cleanly in right-angled frames.",
                 ["Eq(Rational(360,4), 90)"]),
            funfact("Why \"RIGHT\"?",
                    "The name comes from Latin RECTUS — upright. A post standing properly on flat ground makes this angle with it, so it became the \"upright\" angle. Builders still check it constantly: a wall that misses the right angle by even a little leans, and a leaning wall is a falling wall on a slow schedule."),
            withfig(teach("Concept B", "Smaller, bigger, and the two landmarks", [
                "Every angle can be sorted against the quarter turn: smaller than $90$, exactly $90$, or bigger. The page corner sorts them without measuring.",
                "The landmarks stack: two right angles make a straight line ($2 \\times 90 = 180$), and four fill the full turn ($4 \\times 90 = 360$). The picture shows all four quarters around one point.",
                "So an angle bigger than right but smaller than straight lives between the landmarks — the room between them is exactly one more quarter: $180 - 90 = 90$.",
            ]), fig_cross),
            workedset("Between the landmarks",
                      "Quarter, half, whole — sort every angle against them.", [
                wex("A gate swings from closed through a quarter turn, then onward to a half turn. How much more did it turn after the quarter?",
                    ["From $90$ to $180$: the extra is $180 - 90 = 90$ degrees.",
                     "Another whole quarter turn — check: $90 + 90 = 180$ ✓."],
                    "$90$ degrees more — one more quarter turn",
                    ["Eq(180 - 90, 90)", "Eq(90 + 90, 180)"]),
                wex("At 6:00 the clock's hands point opposite ways — a straight angle. How many right angles is that?",
                    ["A straight angle is $180$ degrees.",
                     "$180 \\div 90 = 2$ — two page corners, laid flat together."],
                    "$2$ right angles",
                    ["Eq(Rational(180,90), 2)", "Eq(2*90, 180)"]),
            ]),
            tryitset("Sort against the landmarks", "Smaller than 90, exactly 90, or between 90 and 180?", [
                tp("A straight line holds how many right angles?",
                   ["$2$", "$4$", "$1$"],
                   "$180 \\div 90 = 2$. (Four is the FULL turn's count.)",
                   ["Eq(Rational(180,90), 2)"]),
                withfig(tp("The page corner sinks fully into the angle at $O$ in the picture, with room to spare — yet the angle is not flat. The angle is:",
                   ["bigger than a right angle, smaller than a straight one", "smaller than a right angle", "exactly a right angle"],
                   "Room to spare means more than the quarter turn; not yet flat means less than the half. It lives between the landmarks — and the room between them is one more quarter: $180 - 90 = 90$.",
                   ["Eq(180 - 90, 90)", "Eq(90 + 90, 180)"]), fig_big),
                tp("Three quarters of a full turn are used up. What remains?",
                   ["one right angle", "two right angles", "half a turn"],
                   "$360 - 3 \\times 90 = 360 - 270 = 90$ — exactly one more quarter. Check: $270 + 90 = 360$ ✓.",
                   ["Eq(3*90, 270)", "Eq(360 - 270, 90)", "Eq(270 + 90, 360)"]),
            ]),
            tapq("Quarter by quarter", "A dancer makes a quarter turn four times, always the same way. She now faces:",
                 ["the way she started — a full turn", "the opposite way", "a quarter turn from the start", "halfway between start and opposite"],
                 "Four quarters make one whole: $4 \\times 90 = 360$ degrees, a complete spin back to the start. (Two quarters would face her the opposite way: $2 \\times 90 = 180$.)",
                 ["Eq(4*90, 360)", "Eq(2*90, 180)"]),
            recap([
                "A right angle is a quarter of a full turn: 90 degrees, since 4 × 90 = 360.",
                "The page corner tests any corner: exact fit, gap (smaller), or room to spare (bigger).",
                "Two right angles make a straight line: 2 × 90 = 180.",
                "Arm length never votes — an angle is turn, not ink.",
                "Tilting a right angle does not un-right it; the tester works at any slant.",
            ]),
            tip("For every angle below, say the tester's verdict first — fits, gap, or room to spare — then pick the answer. The verdict IS the answer."),
            tryitset("Mixed practice", "Quarters, halves, and the tester's verdicts.", [
                tp("The hands of a clock make a right angle at:",
                   ["3:00", "6:00", "12:00"],
                   "At 3:00 the hands are a quarter of the face apart: $360 \\div 4 = 90$ degrees. (6:00 makes a straight angle; at 12:00 the hands lie together.)",
                   ["Eq(Rational(360,4), 90)"]),
                tp("Two right angles plus one more right angle make:",
                   ["three quarters of a turn", "a full turn", "a straight line"],
                   "$3 \\times 90 = 270$ degrees — three quarters. One more quarter would close the spin: $270 + 90 = 360$.",
                   ["Eq(3*90, 270)", "Eq(270 + 90, 360)"]),
                withfig(tp("Every corner of the window in the picture passes the page-corner test. All four corners together make:",
                   ["a full turn", "a straight line", "two full turns"],
                   "Four right angles: $4 \\times 90 = 360$ degrees — one full turn shared out among the window's corners.",
                   ["Eq(4*90, 360)"]), fig_window),
                tp("An angle smaller than a right angle is ALWAYS smaller than a straight angle too, because:",
                   ["the quarter turn is smaller than the half turn", "all angles are smaller than straight ones", "small angles have short arms"],
                   "Under $90$ means under $180$ as well — the landmarks sit in order, quarter before half: $90 < 180$, and the gap between them is $180 - 90 = 90$.",
                   ["90 < 180", "Eq(180 - 90, 90)"]),
                tp("How many quarter turns fit in TWO full turns?",
                   ["$8$", "$4$", "$2$"],
                   "Two spins: $2 \\times 360 = 720$ degrees; $720 \\div 90 = 8$ quarters.",
                   ["Eq(2*360, 720)", "Eq(Rational(720,90), 8)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Right Angles\"",
                    "The quarter turn, the tester in every book's corner, and the landmarks at 90, 180 and 360. Next: the shapes those corners build — the quadrilateral family, sorted by its rules.",
                    eyebrow="Chapter complete"),
        ]},
    }

# ==========================================================================
# Lesson 3 — Sorting Quadrilaterals
# ==========================================================================

def lesson_sorting_quadrilaterals():
    # A true square: corners (2,2), (8,2), (8,8), (2,8) — side 8 - 2 = 6.
    sq_lo, sq_hi = 2, 8
    sq_side = sq_hi - sq_lo
    fig_square = fig_geo(
        [P("A", sq_lo, sq_lo), P("B", sq_hi, sq_lo),
         P("C", sq_hi, sq_hi), P("D", sq_lo, sq_hi)],
        poly(["A", "B", "C", "D"], color=C_ACCENT) +
        [ang("A", "B", "D", right=True), ang("B", "C", "A", right=True),
         ang("C", "D", "B", right=True), ang("D", "A", "C", right=True)],
        height=210)
    # A true rectangle: (1,1), (9,1), (9,5), (1,5) — width 8, height 4.
    rx0, rx1, ry0, ry1 = 1, 9, 1, 5
    r_w, r_h = rx1 - rx0, ry1 - ry0
    fig_rect = fig_geo(
        [P("A", rx0, ry0), P("B", rx1, ry0), P("C", rx1, ry1), P("D", rx0, ry1)],
        poly(["A", "B", "C", "D"], color=C_WARM) +
        [ang("A", "B", "D", right=True), ang("B", "C", "A", right=True),
         ang("C", "D", "B", right=True), ang("D", "A", "C", right=True)],
        height=190)
    # A second rectangle for chapter practice: (2,3), (9,3), (9,7), (2,7).
    qx0, qx1, qy0, qy1 = 2, 9, 3, 7
    fig_rect2 = fig_geo(
        [P("A", qx0, qy0), P("B", qx1, qy0), P("C", qx1, qy1), P("D", qx0, qy1)],
        poly(["A", "B", "C", "D"], color=C_GREEN) +
        [ang("A", "B", "D", right=True), ang("B", "C", "A", right=True),
         ang("C", "D", "B", right=True), ang("D", "A", "C", right=True)],
        height=190)
    # A square standing on its corner — still a square: side-vectors (4,4)
    # and (4,-4) are equal in length and meet at right angles. All FOUR
    # corners carry the mark, because the stem claims all four were tested.
    fig_tilted = fig_geo(
        [P("A", 5, 1), P("B", 9, 5), P("C", 5, 9), P("D", 1, 5)],
        poly(["A", "B", "C", "D"], color=C_ACCENT) +
        [ang("A", "B", "D", right=True), ang("B", "A", "C", right=True),
         ang("C", "D", "B", right=True), ang("D", "C", "A", right=True)],
        height=210)
    # A quadrilateral with no equal sides and no right angles — the
    # coordinates are TESTED here (sides 4.00, 7.32, 5.24, 6.02; corners
    # 71.7, 114.5, 55.1, 118.7 degrees), so the drawing survives both
    # tests this topic teaches and cannot contradict its own stem.
    plain_pts = [(1.8, 1.4), (5.8, 1.6), (8.5, 8.4), (3.4, 7.2)]
    assert_no_equal_sides_no_right_angles(plain_pts)
    fig_plain = fig_geo(
        [P(nm, x, y) for nm, (x, y) in zip("ABCD", plain_pts)],
        poly(["A", "B", "C", "D"], color=C_NEUTRAL),
        height=190)
    return {
        "slug": "sorting-quadrilaterals",
        "title": "Sorting Quadrilaterals",
        "concreteComparison": (
            "Four-sided shapes are one big family. The square window, "
            "the long rectangular door, the leaning fence panel — all "
            "quadrilaterals. The square is the STRICTEST member: four "
            "equal sides AND four right angles. The rectangle keeps "
            "the right angles but lets opposite sides pair up long-"
            "and-short. The leaning panel keeps only the count of "
            "four. Stricter rules make a smaller club — and since the "
            "square obeys every rectangle rule, every square IS a "
            "rectangle."),
        "objective": (
            "Sort quadrilaterals by their rules — four equal sides "
            "and four right angles for a square, right angles with "
            "opposite sides equal for a rectangle — and explain why "
            "every square is also a rectangle."),
        "concept": [
            "**Quadrilateral is the family name.** Any closed shape "
            "with $4$ straight sides belongs — leaning, stretched, or "
            "neat. Four sides, four corners, no other requirement.",
            "**A rectangle passes two tests.** All four corners pass "
            "the page-corner test ($4 \\times 90 = 360$, a full turn "
            "of right angles), and opposite sides are equal — the top "
            "matches the bottom, the left matches the right.",
            "**A square is a rectangle with a bonus.** It passes both "
            "rectangle tests AND makes all four sides equal. Stricter "
            "rules, smaller club: every square is a rectangle, but "
            "most rectangles are not squares.",
        ],
        "keyIdea": (
            "Sort by rules, not by looks: four straight sides makes a "
            "quadrilateral, right angles with opposite sides equal "
            "makes a rectangle, and equal sides on top of that makes "
            "a square — so every square is a rectangle."),
        "facts": [
            {"title": "The rectangle's two tests",
             "latex": "4 \\times 90^\\circ = 360^\\circ \\quad \\text{and opposite sides equal}",
             "explanation": "Four page-corner angles, and sides matching in opposite pairs."},
            {"title": "The square's bonus",
             "latex": "\\text{square} = \\text{rectangle} + \\text{all sides equal}",
             "explanation": "Every square passes every rectangle test — membership nests one way."},
        ],
        "workedExamples": [
            {"id": "g4sh-l3-we1",
             "statement": "A square is drawn with corners at $(2, 2)$, $(8, 2)$, $(8, 8)$ and $(2, 8)$. Show that its bottom side and its left side really are equal.",
             "note": "Read each side's length off the coordinates.",
             "solution": ("Bottom: from $2$ across to $8$ is $8 - 2 = 6$. Left: "
                          "from $2$ up to $8$ is the same $8 - 2 = 6$. Equal — "
                          "and the add-back check $6 + 2 = 8$ signs the receipt. "
                          "With all four corners right, the shape earns its name."),
             "badges": [{"text": "core"}],
             "check": ["Eq(8 - 2, 6)", "Eq(6 + 2, 8)", "Eq(4*90, 360)"]},
            {"id": "g4sh-l3-we2",
             "statement": "A rectangle is drawn with corners at $(1, 1)$, $(9, 1)$, $(9, 5)$ and $(1, 5)$. Show its opposite sides are equal — and say why it is NOT a square.",
             "note": "Compare bottom with top, then long side with short.",
             "solution": ("Bottom and top both run from $1$ to $9$: $9 - 1 = 8$ "
                          "each (add back: $8 + 1 = 9$ ✓). Left and right both "
                          "run from $1$ to $5$: $5 - 1 = 4$ each ($4 + 1 = 5$ "
                          "✓). Opposite sides equal, four right angles: a "
                          "rectangle. But $8 > 4$ — neighbouring sides differ, "
                          "so it is not a square."),
             "badges": [{"text": "core"}],
             "check": ["Eq(9 - 1, 8)", "Eq(8 + 1, 9)", "Eq(5 - 1, 4)",
                       "Eq(4 + 1, 5)", "8 > 4"]},
        ],
        "commonMistakes": [
            {"text": "Saying a square is not a rectangle.",
             "correction": "The rectangle test asks only for right angles and opposite sides equal. A square passes both — its equal sides are a bonus, not a disqualification. Every square is a rectangle.",
             "authored": True},
            {"text": "Calling a square standing on its corner a \"diamond\" — a different shape.",
             "correction": "Turning a shape changes nothing it promised: the sides stay equal, the corners stay right. A tilted square is a square.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4sh-l3-t1",
             "statement": "A quadrilateral has four right angles and sides $7$, $3$, $7$, $3$. Which family member is it — and why not a square?",
             "solution": "Right angles ($4 \\times 90 = 360$) and opposite sides equal: a RECTANGLE. Not a square, because neighbouring sides differ: $7 > 3$.",
             "check": ["Eq(4*90, 360)", "7 > 3"]},
            {"id": "g4sh-l3-t2",
             "statement": "True or false: every square is a rectangle.",
             "solution": "True. The rectangle test has $2$ parts — right angles, opposite sides equal — and a square passes $1 + 1 = 2$ of them, both. The bonus (ALL sides equal) breaks no rule.",
             "check": ["Eq(1 + 1, 2)", "Eq(4*90, 360)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The family and the rectangle's rules", [
                "Count the sides, test the corners — both promises work together here. Any $4$ straight sides make a QUADRILATERAL: the family name. The picture's leaning shape belongs, with no equal sides and no right angles at all.",
                "The RECTANGLE is the family's tidy member. Two tests: every corner passes the page-corner test ($4 \\times 90 = 360$ — a full turn of right angles), and opposite sides are equal, top matching bottom, left matching right.",
                "Sort by RULES, never by looks. A long thin rectangle and a nearly-square one pass exactly the same two tests.",
            ]), fig_plain),
            workedset("Running the tests",
                      "Right angles first, then match the opposite sides.", [
                withfig(wex("The rectangle in the picture has corners $(1, 1)$, $(9, 1)$, $(9, 5)$, $(1, 5)$. Check its opposite sides.",
                    ["Bottom and top: $9 - 1 = 8$ each (add back $8 + 1 = 9$ ✓).",
                     "Left and right: $5 - 1 = 4$ each ($4 + 1 = 5$ ✓). Opposite pairs match — rectangle confirmed."],
                    "opposite sides $8$ and $8$, $4$ and $4$ — a rectangle",
                    ["Eq(9 - 1, 8)", "Eq(8 + 1, 9)", "Eq(5 - 1, 4)", "Eq(4 + 1, 5)"]), fig_rect),
                wex("A fence panel has four equal sides of $5$, but its corners fail the page-corner test. Is it a square?",
                    ["The square test has two parts: equal sides AND right angles — $1 + 1 = 2$ tests.",
                     "This panel passes only the sides test: $1$ of $2$. Not a square — just a leaning equal-sided quadrilateral."],
                    "no — equal sides alone pass only $1$ of the $2$ tests",
                    ["Eq(1 + 1, 2)", "Eq(2 - 1, 1)"]),
            ]),
            tryitset("Which member?", "Rules decide, looks distract.", [
                withfig(tp("The shape in the picture has four right angles, long sides $8$ and short sides $4$. It is a:",
                   ["rectangle", "square", "pentagon"],
                   "Right angles ($4 \\times 90 = 360$) and opposite sides equal: rectangle. Not a square — $8 > 4$, the neighbouring sides differ.",
                   ["Eq(4*90, 360)", "8 > 4"]), fig_rect),
                tp("Which rule does EVERY quadrilateral obey?",
                   ["four straight sides", "four right angles", "four equal sides"],
                   "The family asks only for the count: $4$ sides (and the matching $4$ corners — $4 \\times 2 = 8$ side-ends, $8 \\div 2 = 4$). Right angles and equal sides are extra rules for stricter members.",
                   ["Eq(4*2, 8)", "Eq(Rational(8,2), 4)"]),
                tp("A rectangle's bottom side is $9$ cm. Its top side is:",
                   ["$9$ cm", "$4$ cm", "impossible to tell"],
                   "Opposite sides of a rectangle are equal, so the top copies the bottom exactly: $9$ cm. The two differ by nothing at all — $9 - 9 = 0$, and adding back, $0 + 9 = 9$ ✓.",
                   ["Eq(9 - 9, 0)", "Eq(0 + 9, 9)"]),
            ]),
            tapq("Rules, not looks", "A quadrilateral has four page-corner angles, opposite sides equal, long side $7$, short side $4$. It is:",
                 ["a rectangle", "a square", "a pentagon", "not a real shape"],
                 "Both rectangle tests pass: rectangle. The square would demand equal neighbours, but $7 > 4$. And with four sides it is certainly no pentagon — $4 < 5$.",
                 ["Eq(4*90, 360)", "7 > 4", "4 < 5"]),
            funfact("The chessboard's square of squares",
                    "A chessboard is a square cut into $8$ rows of $8$ squares: $8 \\times 8 = 64$ little squares sitting inside one big one. Squares tile perfectly — right angles meeting right angles, $4 \\times 90 = 360$ around every inner corner, no gaps anywhere. That is why floors, windows and game boards love them."),
            withfig(teach("Concept B", "The square — strictest of the family", [
                "The SQUARE passes the rectangle's two tests and adds a bonus: ALL four sides equal. In the picture the bottom is $8 - 2 = 6$ and the left is the same $8 - 2 = 6$ — drawn honestly square.",
                "Because it passes every rectangle test, every square IS a rectangle. The reverse fails: a rectangle with sides $8$ and $4$ is no square, since $8 > 4$.",
                "And tilting changes nothing: stand a square on its corner and its sides are still equal, its corners still right. Rules travel with the shape.",
            ]), fig_square),
            workedset("Membership runs one way",
                      "Squares pass rectangle tests; rectangles may fail the square's.", [
                wex("A student says: \"a square is not a rectangle.\" Test the square against the rectangle's rules.",
                    ["Right angles? Yes — all four, $360 \\div 90 = 4$ of them.",
                     "Opposite sides equal? Yes — ALL its sides are equal, so opposite pairs certainly match. Both tests passed: $1 + 1 = 2$. The student is wrong."],
                    "the square passes both tests — it IS a rectangle",
                    ["Eq(Rational(360,90), 4)", "Eq(1 + 1, 2)"]),
                wex("A rectangle has sides $8$, $4$, $8$, $4$. Does it pass the square's test?",
                    ["The square demands all sides equal — but $8 > 4$.",
                     "It stays a rectangle. Membership runs one way only: squares into rectangles, not back."],
                    "no — $8 > 4$, so it is a rectangle but not a square",
                    ["8 > 4", "Eq(4*90, 360)"]),
            ]),
            tryitset("The strictest member", "Two tests plus a bonus.", [
                tp("Every square is a rectangle because:",
                   ["it passes both rectangle tests", "it has five sides", "rectangles must have equal sides"],
                   "Right angles — check. Opposite sides equal — check (all of them are). $1 + 1 = 2$ tests passed; the bonus breaks nothing.",
                   ["Eq(1 + 1, 2)"]),
                withfig(tp("The shape in the picture stands on its corner: four equal sides, four page-corner angles. It is:",
                   ["a square", "a diamond — a new shape", "a triangle"],
                   "Equal sides AND right angles: a square, whichever way it stands. Turning a shape cancels none of its promises — $4 \\times 90 = 360$ still.",
                   ["Eq(4*90, 360)"]), fig_tilted),
                tp("A quadrilateral has four equal sides but NO right angles. Is it a square?",
                   ["no — a square needs right angles too", "yes — equal sides are enough", "yes, if it is drawn neatly"],
                   "The square test has $2$ parts; equal sides pass only $1$ of them, and $2 - 1 = 1$ test still fails. No right angles, no square.",
                   ["Eq(1 + 1, 2)", "Eq(2 - 1, 1)"]),
            ]),
            tapq("One-way membership", "Every square is a rectangle. Is every rectangle a square?",
                 ["no — its neighbouring sides may differ", "yes — same family, same shape", "only tilted rectangles", "no rectangle is ever a square"],
                 "A rectangle with sides $8$ and $4$ passes both rectangle tests yet fails the square's bonus: $8 > 4$. Membership nests one way — the strictest member fits inside every looser club, never the reverse.",
                 ["8 > 4", "Eq(4*90, 360)"]),
            recap([
                "Quadrilateral is the family name: any 4 straight sides.",
                "Rectangle: four right angles (4 × 90 = 360) and opposite sides equal.",
                "Square: a rectangle whose sides are ALL equal — the strictest member.",
                "Every square is a rectangle; a rectangle with unequal neighbours is not a square.",
                "Sort by rules, never by looks — and tilting changes nothing.",
            ]),
            tip("For each shape below, run the tests out loud in order: sides straight and four? corners right? opposite sides equal? all sides equal? Stop at the strictest test it passes."),
            tryitset("Mixed practice", "The whole family, sorted by rules.", [
                tp("Which shape does NOT belong to the quadrilateral family?",
                   ["a triangle", "a rectangle", "a square"],
                   "The family badge is four sides — a triangle carries only $3$, and $3 < 4$. Rectangles and squares are members in good standing.",
                   ["3 < 4"]),
                withfig(tp("The rectangle in the picture has corners $(2, 3)$, $(9, 3)$, $(9, 7)$, $(2, 7)$. Its top side measures:",
                   ["$7$", "$4$", "$9$"],
                   "The top runs from $2$ to $9$: $9 - 2 = 7$ (add back: $7 + 2 = 9$ ✓) — equal to the bottom, as a rectangle promises. The short sides measure $7 - 3 = 4$ each ($4 + 3 = 7$ ✓).",
                   ["Eq(9 - 2, 7)", "Eq(7 + 2, 9)", "Eq(7 - 3, 4)", "Eq(4 + 3, 7)"]), fig_rect2),
                tp("A square has sides of $6$; a rectangle has sides $8$ and $4$. Which statement is right?",
                   ["both are rectangles; only the first is a square", "both are squares", "neither is a rectangle"],
                   "The square passes both rectangle tests ($1 + 1 = 2$) plus its bonus. The $8$-by-$4$ shape is a rectangle only: $8 > 4$.",
                   ["Eq(1 + 1, 2)", "8 > 4"]),
                tp("The four right angles of a rectangle together make:",
                   ["a full turn", "a straight line", "three quarters of a turn"],
                   "$4 \\times 90 = 360$ degrees — the same full turn the crossing's corners made in the last lesson.",
                   ["Eq(4*90, 360)"]),
                withfig(tp("The leaning shape in the picture has $4$ straight sides, no equal sides, no right angles. Its best name is:",
                   ["quadrilateral", "rectangle", "square"],
                   "It passes only the family test: four sides (receipt: $4 \\times 2 = 8$ side-ends, $8 \\div 2 = 4$ corners). No stricter club will take it.",
                   ["Eq(4*2, 8)", "Eq(Rational(8,2), 4)"]), fig_plain),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Sorting Quadrilaterals\"",
                    "Rules, not looks — and the strictest member fits inside every looser club. Next promise to test: the fold. Some shapes hide a mirror down their middle.",
                    eyebrow="Chapter complete"),
        ]},
    }

# ==========================================================================
# Lesson 4 — Line Symmetry
# ==========================================================================

def lesson_line_symmetry():
    # Isosceles triangle A(2,2) B(8,2) C(5,8): the true axis is the
    # vertical through x = (2 + 8) / 2 = 5 — through the apex.
    fig_iso = fig_geo(
        [P("A", 2, 2), P("B", 8, 2), P("C", 5, 8),
         P("M", 5, 1, ""), P("N", 5, 9, "")],
        poly(["A", "B", "C"], color=C_ACCENT) +
        [seg("M", "N", dashed=True, color=C_WARM)],
        height=210)
    # Second isosceles triangle (3,1) (9,1) (6,7): axis x = (3 + 9) / 2 = 6.
    fig_iso2 = fig_geo(
        [P("A", 3, 1), P("B", 9, 1), P("C", 6, 7),
         P("M", 6, 0.4, ""), P("N", 6, 7.9, "")],
        poly(["A", "B", "C"], color=C_GREEN) +
        [seg("M", "N", dashed=True, color=C_WARM)],
        height=200)
    # Rectangle (1,2)-(9,6): the two TRUE mirror lines are x = 5 and y = 4.
    fig_rect_sym = fig_geo(
        [P("A", 1, 2), P("B", 9, 2), P("C", 9, 6), P("D", 1, 6),
         P("M", 5, 1.2, ""), P("N", 5, 6.8, ""),
         P("U", 0.4, 4, ""), P("V", 9.6, 4, "")],
        poly(["A", "B", "C", "D"], color=C_ACCENT) +
        [seg("M", "N", dashed=True, color=C_WARM),
         seg("U", "V", dashed=True, color=C_WARM)],
        height=200)
    # Second rectangle for chapter practice — standing tall, (2,1)-(8,9),
    # so BOTH middles are whole numbers: across 2 + 8 = 10, 10 / 2 = 5;
    # up 1 + 9 = 10, 10 / 2 = 5.
    fig_rect_sym2 = fig_geo(
        [P("A", 2, 1), P("B", 8, 1), P("C", 8, 9), P("D", 2, 9),
         P("M", 5, 0.4, ""), P("N", 5, 9.6, ""),
         P("U", 1.2, 5, ""), P("V", 8.8, 5, "")],
        poly(["A", "B", "C", "D"], color=C_GREEN) +
        [seg("M", "N", dashed=True, color=C_WARM),
         seg("U", "V", dashed=True, color=C_WARM)],
        height=200)
    # Square (2,2)-(8,8) with all four true mirror lines: x = 5, y = 5,
    # and the two diagonals through opposite corners.
    fig_square_sym = fig_geo(
        [P("A", 2, 2), P("B", 8, 2), P("C", 8, 8), P("D", 2, 8),
         P("M", 5, 1.2, ""), P("N", 5, 8.8, ""),
         P("U", 1.2, 5, ""), P("V", 8.8, 5, "")],
        poly(["A", "B", "C", "D"], color=C_ACCENT) +
        [seg("M", "N", dashed=True, color=C_WARM),
         seg("U", "V", dashed=True, color=C_WARM),
         seg("A", "C", dashed=True, color=C_WARM),
         seg("B", "D", dashed=True, color=C_WARM)],
        height=210)
    # Scalene triangle with sides 8, 6, 4 — no fold works, so NO dashed
    # line is drawn. Third vertex computed from the side lengths.
    fig_scalene = fig_geo(
        [P("A", 0.5, 1), P("B", 8.5, 1), P("C", 5.75, 3.905)],
        poly(["A", "B", "C"], color=C_NEUTRAL),
        height=180)
    # Rhombus (5,1) (8,5) (5,9) (2,5): each side has length 5 (legs 3 and
    # 4), and its TWO mirror lines are the diagonals — drawn dashed.
    fig_rhombus = fig_geo(
        [P("A", 5, 1), P("B", 8, 5), P("C", 5, 9), P("D", 2, 5)],
        poly(["A", "B", "C", "D"], color=C_GREEN) +
        [seg("A", "C", dashed=True, color=C_WARM),
         seg("B", "D", dashed=True, color=C_WARM)],
        height=210)
    return {
        "slug": "line-symmetry",
        "title": "Line Symmetry",
        "concreteComparison": (
            "Cut a shape out of paper and fold it down the middle. If "
            "the two halves lie EXACTLY on top of each other — every "
            "edge on an edge, no overhang anywhere — the fold line is "
            "a LINE OF SYMMETRY: the shape's hidden mirror. Butterfly "
            "wings match this way, and so do the felt patterns sewn "
            "on a ger door. The fold test never lies: exact match, or "
            "no mirror."),
        "objective": (
            "Use the fold test to find lines of symmetry, draw mirror "
            "lines through the true middle of a shape, and count the "
            "lines a shape has — 0 for a scalene triangle, 1 for an "
            "isosceles triangle, 2 for a rectangle, 4 for a square."),
        "concept": [
            "**The fold test.** Fold the shape along a line: halves "
            "match exactly — the line is a line of symmetry; any "
            "overhang at all — it is not. Try the fold, and the shape "
            "answers.",
            "**The mirror line is exact.** It must pass through the "
            "TRUE middle. For a shape sitting from $2$ across to $8$, "
            "the vertical mirror stands at the halfway mark: $2 + 8 = "
            "10$, and $10 \\div 2 = 5$. A line drawn roughly nearby "
            "fails the fold.",
            "**Shapes carry counts.** A scalene triangle: $0$ lines. "
            "An isosceles triangle: $1$. A rectangle: $2$ (NOT its "
            "diagonals). A square: the rectangle's $2$ plus $2$ "
            "diagonals $= 4$. The count is a property you can check "
            "fold by fold.",
        ],
        "keyIdea": (
            "Try the fold: halves matching exactly make a line of "
            "symmetry, the line passes the true middle, and counting "
            "the folds that work gives each shape its symmetry "
            "number: scalene triangle 0, isosceles 1, rectangle 2, "
            "square 4."),
        "facts": [
            {"title": "The fold test",
             "latex": "\\text{fold on the line} \\Rightarrow \\text{halves match exactly}",
             "explanation": "Each matching half is one half of the whole — and two exact halves rebuild it."},
            {"title": "Symmetry counts",
             "latex": "\\text{rectangle: } 2 \\qquad \\text{square: } 2 + 2 = 4",
             "explanation": "The square keeps the rectangle's two lines and adds its two diagonals."},
        ],
        "workedExamples": [
            {"id": "g4sh-l4-we1",
             "statement": "A rectangle (longer than it is wide) — how many lines of symmetry, and why are its diagonals NOT among them?",
             "note": "Try all the folds; keep only exact matches.",
             "solution": ("Two folds work: side-middle to side-middle, across "
                          "and down. The diagonal fold makes the two triangle "
                          "halves stick out past each other — overhang, so it "
                          "fails. Count: $2$. (A square would add its $2$ "
                          "diagonals: $2 + 2 = 4$.)"),
             "badges": [{"text": "core"}],
             "check": ["Eq(1 + 1, 2)", "Eq(2 + 2, 4)"]},
            {"id": "g4sh-l4-we2",
             "statement": "Count the lines of symmetry of the block letters A, H and F — and give the total.",
             "note": "Fold each letter in your head; count exact matches only.",
             "solution": ("A: one vertical mirror — $1$. H: vertical AND "
                          "horizontal — $2$. F: no fold matches — $0$. Total: "
                          "$1 + 2 + 0 = 3$."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1 + 2 + 0, 3)", "2 > 1"]},
        ],
        "commonMistakes": [
            {"text": "Folding a rectangle along its diagonal and calling it a line of symmetry.",
             "correction": "Fold it with real paper once: the halves overhang. A rectangle has exactly 2 lines, both through the middles of its sides. Only the SQUARE earns diagonal mirrors.",
             "authored": True},
            {"text": "Drawing the mirror line roughly near the middle.",
             "correction": "The fold test is exact: the line must pass the true middle (halfway between 2 and 8 is exactly 5, not \"about there\"). A line slightly off fails the fold.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4sh-l4-t1",
             "statement": "How many lines of symmetry has a square?",
             "solution": "The rectangle's $2$ (through side-middles) plus its own $2$ diagonals: $2 + 2 = 4$.",
             "check": ["Eq(2 + 2, 4)"]},
            {"id": "g4sh-l4-t2",
             "statement": "Block letter H has $2$ lines of symmetry; block letter M has $1$. How many more has H?",
             "solution": "$2 - 1 = 1$ more (the horizontal fold that M fails). Add back: $1 + 1 = 2$ ✓.",
             "check": ["Eq(2 - 1, 1)", "Eq(1 + 1, 2)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "The fold test", [
                "Try the fold — this lesson's promise. Fold a shape along a line: if the halves lie exactly edge on edge, the line is a LINE OF SYMMETRY. Any overhang, however small, and it is not.",
                "The dashed line in the picture is the triangle's one true mirror: it stands at the halfway mark of the base, $2 + 8 = 10$, $10 \\div 2 = 5$, and rises through the apex.",
                "Exact is the whole rule: two matching halves are each one half of the shape, and $\\frac{1}{2} + \\frac{1}{2} = 1$ — they rebuild it perfectly with nothing left over.",
            ]), fig_iso),
            workedset("Finding the fold",
                      "The mirror stands at the true middle — compute it, then fold.", [
                withfig(wex("The triangle in the picture has base corners at $2$ and $8$, apex above the middle. Where is its mirror line, and how many does it have?",
                    ["Halfway between $2$ and $8$: $2 + 8 = 10$, $10 \\div 2 = 5$ — the dashed vertical through the apex.",
                     "Fold there: the two slanted sides swap places exactly. No other fold matches: $1$ line."],
                    "one line — the vertical through $5$",
                    ["Eq(2 + 8, 10)", "Eq(Rational(10,2), 5)"]), fig_iso),
                withfig(wex("The rectangle in the picture runs from $1$ to $9$ across and $2$ to $6$ up. Find both mirror lines.",
                    ["Vertical: halfway between $1$ and $9$ — $1 + 9 = 10$, $10 \\div 2 = 5$.",
                     "Horizontal: halfway between $2$ and $6$ — $2 + 6 = 8$, $8 \\div 2 = 4$. Two lines, both dashed in the picture — and no diagonal fold matches."],
                    "the vertical at $5$ and the horizontal at $4$ — $2$ lines",
                    ["Eq(1 + 9, 10)", "Eq(Rational(10,2), 5)",
                     "Eq(2 + 6, 8)", "Eq(Rational(8,2), 4)"]), fig_rect_sym),
            ]),
            tryitset("Fold and judge", "Exact match or nothing.", [
                tp("You fold a shape on a line and one half sticks out past the other. The line is:",
                   ["not a line of symmetry", "a line of symmetry anyway", "a line of symmetry if the overhang is small"],
                   "The fold test is exact: a true mirror splits the shape into two matching halves, $\\frac{1}{2} + \\frac{1}{2} = 1$, with NOTHING left over. Overhang means the halves differ — test failed.",
                   ["Eq(Rational(1,2) + Rational(1,2), 1)"]),
                withfig(tp("The triangle in the picture has sides $8$, $6$ and $4$ — all different. Its lines of symmetry number:",
                   ["$0$", "$1$", "$3$"],
                   "A fold must swap two EQUAL sides onto each other, but here no two sides match: $4 < 6$ and $6 < 8$. No fold works — a scalene triangle has no mirror.",
                   ["4 < 6", "6 < 8"]), fig_scalene),
                withfig(tp("The triangle in the picture has base corners at $3$ and $9$ and two equal slanted sides. Its mirror line stands at:",
                   ["$6$", "$5$", "$4$"],
                   "The true middle of the base: $3 + 9 = 12$, $12 \\div 2 = 6$ — exactly where the dashed line is drawn. One line of symmetry.",
                   ["Eq(3 + 9, 12)", "Eq(Rational(12,2), 6)"]), fig_iso2),
            ]),
            tapq("Exact or nothing", "The fold test passes only when:",
                 ["the two halves match exactly, edge on edge", "most of each half matches", "the fold line is vertical", "the shape is a polygon"],
                 "Symmetry is an exact promise: each half is precisely one half, and $2 \\times \\frac{1}{2} = 1$ — the two rebuild the whole with no overhang. Direction never matters: mirrors can stand upright, lie flat, or lean.",
                 ["Eq(2*Rational(1,2), 1)"]),
            funfact("You are built on a mirror line",
                    "Most animals are: biologists call it BILATERAL symmetry. A butterfly's wing patterns match across its body line, left wing mirroring right — and your own face, hands and skeleton pair up across a line down your middle. Nature discovered the fold test long before geometry named it."),
            withfig(teach("Concept B", "Counting the lines", [
                "Each shape carries a COUNT of working folds. The square in the picture has all four drawn: the vertical at $2 + 8 = 10$, $10 \\div 2 = 5$, the horizontal at the same $5$ — and both diagonals, corner to corner.",
                "That is the rectangle's $2$ plus the square's bonus $2$: $2 + 2 = 4$. Equal sides are what let the diagonal folds match.",
                "Counts to remember: scalene triangle $0$, isosceles triangle $1$, rectangle $2$, square $4$. More rules kept, more mirrors earned.",
            ]), fig_square_sym),
            workedset("Symmetry numbers",
                      "Count the folds that pass; the count is the shape's property.", [
                wex("Count the square's lines of symmetry.",
                    ["Side-middle folds: vertical and horizontal — $2$, the rectangle's pair.",
                     "Diagonal folds: both match, because all sides are equal — $2$ more. Total: $2 + 2 = 4$."],
                    "$4$ lines",
                    ["Eq(2 + 2, 4)"]),
                wex("How many MORE lines has a square than a (non-square) rectangle?",
                    ["Square $4$, rectangle $2$: the difference is $4 - 2 = 2$ — exactly the two diagonals.",
                     "Add back: $2 + 2 = 4$ ✓."],
                    "$2$ more — the diagonals",
                    ["Eq(4 - 2, 2)", "Eq(2 + 2, 4)"]),
            ]),
            tryitset("Count the mirrors", "Fold by fold — count only the folds that pass.", [
                tp("Block letter H has how many lines of symmetry?",
                   ["$2$", "$1$", "$0$"],
                   "A vertical fold matches its two uprights, and a horizontal fold matches top to bottom: $1 + 1 = 2$ lines.",
                   ["Eq(1 + 1, 2)"]),
                tp("Which block letter has NO line of symmetry?",
                   ["F", "A", "T"],
                   "A and T each pass one vertical fold ($1$ line each); F fails every fold — $0$. Their three counts: $0 + 1 + 1 = 2$ lines among them.",
                   ["Eq(0 + 1 + 1, 2)"]),
                withfig(tp("The four-equal-sided shape in the picture (not a square) has its mirror lines along:",
                   ["its two corner-to-corner diagonals", "its two side-middle lines", "all four of those lines"],
                   "Fold corner to corner and the equal sides swap exactly — both diagonals pass, standing at the true middles: across, $2 + 8 = 10$, $10 \\div 2 = 5$; and up, $1 + 9 = 10$, $10 \\div 2 = 5$. The side-middle folds fail because its corners are not right angles: $2$ lines, not $4$.",
                   ["Eq(2 + 8, 10)", "Eq(1 + 9, 10)", "Eq(Rational(10,2), 5)",
                    "Eq(1 + 1, 2)"]), fig_rhombus),
            ]),
            tapq("Where the extra mirrors come from", "A rectangle has 2 lines of symmetry and a square has 4. The square's two extra lines run:",
                 ["corner to corner — its diagonals", "side-middle to side-middle", "outside the shape", "nowhere — squares also have just 2"],
                 "Equal sides let the diagonal folds match: $4 - 2 = 2$ extra lines, and $2 + 2 = 4$ in all. The rectangle's unequal neighbours make its diagonal folds overhang.",
                 ["Eq(4 - 2, 2)", "Eq(2 + 2, 4)"]),
            recap([
                "The fold test: halves match exactly — line of symmetry; any overhang — not.",
                "The mirror line passes the TRUE middle: halfway between 2 and 8 is exactly 5.",
                "Counts: scalene 0, isosceles 1, rectangle 2, square 2 + 2 = 4.",
                "A rectangle's diagonals are NOT mirror lines — only the square earns those.",
                "Letters carry counts too: F 0, A 1, H 2.",
            ]),
            tip("For each shape below, fold it in your head one line at a time and say pass or fail — then count the passes. The count is the answer."),
            tryitset("Mixed practice", "Fold, judge, count.", [
                tp("An isosceles triangle (two equal sides) has how many lines of symmetry?",
                   ["$1$", "$2$", "$0$"],
                   "One fold — through the apex and the base's middle — swaps the two equal sides exactly. A scalene triangle, whose sides all differ, has no fold that works at all: $0 < 1$. So this one earns exactly $1$ line.",
                   ["0 < 1"]),
                tp("A square, a rectangle and a scalene triangle: total lines of symmetry?",
                   ["$6$", "$4$", "$8$"],
                   "$4 + 2 + 0 = 6$ lines among the three shapes.",
                   ["Eq(4 + 2 + 0, 6)"]),
                withfig(tp("The rectangle in the picture shows its mirror lines dashed. How many are there — and are the diagonals included?",
                   ["$2$ — and the diagonals are not", "$4$ — including the diagonals", "$1$ — the vertical only"],
                   "Both side-middle folds pass, standing at the true middles: across, $2 + 8 = 10$ and $10 \\div 2 = 5$; up, $1 + 9 = 10$ and $10 \\div 2 = 5$ — exact, not roughly. Diagonal folds overhang: $2$ lines.",
                   ["Eq(2 + 8, 10)", "Eq(1 + 9, 10)",
                    "Eq(Rational(10,2), 5)"]), fig_rect_sym2),
                tp("The word MOM is written in block capitals. Total lines of symmetry, letter by letter?",
                   ["$4$", "$3$", "$0$"],
                   "M has $1$ (vertical), O has $2$ (vertical and horizontal), M has $1$: $1 + 2 + 1 = 4$. That vertical mirror in every letter is why MOM reads the same in an actual mirror.",
                   ["Eq(1 + 2 + 1, 4)"]),
                tp("A shape's mirror line must pass through:",
                   ["the exact middle of what it splits", "roughly the middle", "a corner, always"],
                   "Exact, always: for a base from $3$ to $9$ the mirror stands at $3 + 9 = 12$, $12 \\div 2 = 6$ — one number, not a neighbourhood. (Some mirrors DO pass corners, like the square's diagonals, but only when the corner sits on the true middle line.)",
                   ["Eq(3 + 9, 12)", "Eq(Rational(12,2), 6)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"Line Symmetry\"",
                    "The fold test, the true middle, and each shape's symmetry number. One promise left to test — and it needs all three dimensions: faces, edges and vertices of the solids in your hands.",
                    eyebrow="Chapter complete"),
        ]},
    }

# ==========================================================================
# Lesson 5 — 3-D Solids
# ==========================================================================

def make_cube_fig():
    """An honest cube drawing: front square, back square shifted, the
    12 edges — hidden ones dashed. 4 + 4 + 4 = 12 edges, 4 + 4 = 8
    vertices, and 3 pairs of faces = 6."""
    front = [P("A", 2, 2), P("B", 6, 2), P("C", 6, 6), P("D", 2, 6)]
    back = [P("E", 4, 3.5), P("F", 8, 3.5), P("G", 8, 7.5), P("H", 4, 7.5)]
    edges = [
        seg("A", "B", color=C_ACCENT), seg("B", "C", color=C_ACCENT),
        seg("C", "D", color=C_ACCENT), seg("D", "A", color=C_ACCENT),
        seg("F", "G", color=C_ACCENT), seg("G", "H", color=C_ACCENT),
        seg("B", "F", color=C_ACCENT), seg("C", "G", color=C_ACCENT),
        seg("D", "H", color=C_ACCENT),
        seg("A", "E", dashed=True, color=C_NEUTRAL),
        seg("E", "F", dashed=True, color=C_NEUTRAL),
        seg("E", "H", dashed=True, color=C_NEUTRAL),
    ]
    assert len(edges) == 12, "cube figure must draw exactly 12 edges"
    assert len(front) + len(back) == 8, "cube figure must have 8 vertices"
    return fig_geo(front + back, edges, height=210)


def make_pyramid_fig():
    """A square pyramid: 4 base corners + 1 apex = 5 vertices, 4 base
    edges + 4 slant edges = 8 — hidden base edges dashed."""
    pts = [P("A", 2, 2), P("B", 8, 2), P("C", 9.3, 4.4), P("D", 3.3, 4.4),
           P("T", 5.6, 8.6)]
    edges = [
        seg("A", "B", color=C_WARM), seg("B", "C", color=C_WARM),
        seg("T", "A", color=C_WARM), seg("T", "B", color=C_WARM),
        seg("T", "C", color=C_WARM),
        seg("C", "D", dashed=True, color=C_NEUTRAL),
        seg("D", "A", dashed=True, color=C_NEUTRAL),
        seg("T", "D", dashed=True, color=C_NEUTRAL),
    ]
    assert len(edges) == 8, "pyramid figure must draw exactly 8 edges"
    assert len(pts) == 5, "pyramid figure must have 5 vertices"
    return fig_geo(pts, edges, height=210)


def lesson_three_d_solids():
    fig_cube = make_cube_fig()
    fig_cube2 = make_cube_fig()
    fig_pyr = make_pyramid_fig()
    fig_pyr2 = make_pyramid_fig()
    # Count pictures built from the same numbers as the text.
    fig_cube_counts = fig_groups(
        (6, "faces", C_ACCENT), (12, "edges", C_WARM), (8, "vertices", C_GREEN))
    fig_pyr_faces = fig_groups(
        (1, "square base", C_ACCENT), (4, "triangle faces", C_WARM))
    return {
        "slug": "three-d-solids",
        "title": "3-D Solids",
        "concreteComparison": (
            "A dice, a brick, a ball, a tin can, an ice-cream cone "
            "and a point-topped tower: six solids you can hold. Flat "
            "shapes live on paper; solids fill your hand — so they "
            "need three counts, not one. FACES are the flat surfaces "
            "you can press a palm against, EDGES the lines where two "
            "faces meet, VERTICES the corner points. A dice: $6$ "
            "faces, $12$ edges, $8$ vertices — count one tonight."),
        "objective": (
            "Name the six common solids — cube, cuboid, sphere, "
            "cylinder, cone, square pyramid — count faces, edges and "
            "vertices, and say which 2-D shape each flat face is."),
        "concept": [
            "**Three counts describe a solid.** Faces (flat surfaces), "
            "edges (lines where two faces meet), vertices (corner "
            "points). The cube: $6$ faces in $3$ opposite pairs, $12$ "
            "edges ($4$ around the top, $4$ around the bottom, $4$ "
            "upright), $8$ vertices ($4$ up, $4$ down).",
            "**Faces wear 2-D names.** A cube's faces are squares; a "
            "cuboid's are rectangles; a square pyramid wears $1$ "
            "square and $4$ triangles. The cylinder has $2$ circle "
            "faces and a curved wrap; the cone $1$ circle and a "
            "curved slope; the sphere is all curve — no flat face, no "
            "edge, no vertex.",
            "**The counting receipt.** For solids with flat faces, "
            "faces plus vertices beats edges by exactly $2$: cube "
            "$6 + 8 - 12 = 2$, square pyramid $5 + 5 - 8 = 2$. "
            "Miscount anything and the receipt refuses to balance — "
            "it catches errors like a checksum.",
        ],
        "keyIdea": (
            "Count three things — faces, edges, vertices — name each "
            "flat face with its 2-D shape, and receipt the count: "
            "faces plus vertices minus edges always makes 2."),
        "facts": [
            {"title": "The cube's numbers",
             "latex": "F + V - E = 6 + 8 - 12 = 2",
             "explanation": "Faces plus vertices minus edges makes 2 — the receipt that audits your counting."},
            {"title": "Faces wear 2-D names",
             "latex": "\\text{square pyramid: } 1 \\text{ square} + 4 \\text{ triangles} = 5 \\text{ faces}",
             "explanation": "Every flat face of a solid is a 2-D shape you already know how to name."},
        ],
        "workedExamples": [
            {"id": "g4sh-l5-we1",
             "statement": "Count a dice: faces, edges, vertices — then run the receipt.",
             "note": "Count in groups: pairs of faces; top, bottom and upright edges.",
             "solution": ("Faces: $3$ opposite pairs — $3 \\times 2 = 6$. Edges: "
                          "$4$ around the top, $4$ around the bottom, $4$ "
                          "upright — $4 + 4 + 4 = 12$. Vertices: $4$ up, $4$ "
                          "down — $4 + 4 = 8$. Receipt: $6 + 8 = 14$, and $14 - "
                          "12 = 2$ ✓ — the count balances."),
             "badges": [{"text": "core"}],
             "check": ["Eq(3*2, 6)", "Eq(4 + 4 + 4, 12)", "Eq(4 + 4, 8)",
                       "Eq(6 + 8, 14)", "Eq(14 - 12, 2)", "Eq(2 + 12, 14)"]},
            {"id": "g4sh-l5-we2",
             "statement": "Count a square pyramid: faces, edges, vertices — and receipt it.",
             "note": "One base below, triangles rising to one apex.",
             "solution": ("Faces: $1$ square base $+ 4$ triangles $= 5$. "
                          "Vertices: $4$ base corners $+ 1$ apex $= 5$. Edges: "
                          "$4$ around the base $+ 4$ rising to the apex $= 8$. "
                          "Receipt: $5 + 5 = 10$, and $10 - 8 = 2$ ✓."),
             "badges": [{"text": "core"}],
             "check": ["Eq(1 + 4, 5)", "Eq(4 + 1, 5)", "Eq(4 + 4, 8)",
                       "Eq(5 + 5, 10)", "Eq(10 - 8, 2)", "Eq(2 + 8, 10)"]},
        ],
        "commonMistakes": [
            {"text": "Counting only the faces you can see in a drawing — calling a cube \"3 faces\".",
             "correction": "A drawing hides the back, the bottom and one side. Count in opposite PAIRS — front-back, left-right, top-bottom: 3 × 2 = 6 — and the hidden ones stop escaping.",
             "authored": True},
            {"text": "Mixing up edges and vertices.",
             "correction": "An edge is a LINE where two faces meet; a vertex is a POINT where edges meet. Run a finger along a dice: the finger slides along an edge and STOPS at a vertex.",
             "authored": True},
        ],
        "tryIt": [
            {"id": "g4sh-l5-t1",
             "statement": "A brick (a cuboid) — count its faces, edges and vertices, and run the receipt.",
             "solution": "Same counts as the cube: $3 \\times 2 = 6$ faces, $4 + 4 + 4 = 12$ edges, $4 + 4 = 8$ vertices. Receipt: $6 + 8 - 12 = 2$ ✓ — only the face SHAPES differ (rectangles, not squares).",
             "check": ["Eq(3*2, 6)", "Eq(4 + 4 + 4, 12)", "Eq(4 + 4, 8)",
                       "Eq(6 + 8 - 12, 2)"]},
            {"id": "g4sh-l5-t2",
             "statement": "Which 2-D shapes are a cuboid's faces? And how many FLAT faces has a cylinder?",
             "solution": "A cuboid wears $6$ rectangles (in $3$ equal pairs: $3 \\times 2 = 6$). A cylinder has $1 + 1 = 2$ flat faces — both circles — plus one curved wrap that is not flat.",
             "check": ["Eq(3*2, 6)", "Eq(1 + 1, 2)"]},
        ],
        "interactive": {"steps": [
            withfig(teach("Concept A", "Faces, edges, vertices", [
                "Solids need THREE counts. FACES: the flat surfaces (a drawing hides some — the dashed lines in the picture mark hidden edges). EDGES: lines where two faces meet. VERTICES: points where edges meet.",
                "Count the cube in groups, and the hidden parts cannot escape: faces in opposite pairs, $3 \\times 2 = 6$; edges as top ring, bottom ring, uprights, $4 + 4 + 4 = 12$; vertices as $4$ up and $4$ down, $4 + 4 = 8$.",
                "Then RECEIPT the count: faces plus vertices minus edges must make $2$. Cube: $6 + 8 = 14$, $14 - 12 = 2$ ✓. If your receipt says anything else, a count is wrong.",
            ]), fig_cube),
            workedset("Counting solids",
                      "Groups first, then the receipt.", [
                withfig(wex("A dice: count faces, edges and vertices, and receipt the count.",
                    ["Faces $3 \\times 2 = 6$; edges $4 + 4 + 4 = 12$; vertices $4 + 4 = 8$.",
                     "Receipt: $6 + 8 = 14$, $14 - 12 = 2$ ✓."],
                    "$6$ faces, $12$ edges, $8$ vertices",
                    ["Eq(3*2, 6)", "Eq(4 + 4 + 4, 12)", "Eq(4 + 4, 8)",
                     "Eq(6 + 8, 14)", "Eq(14 - 12, 2)"]), fig_cube_counts),
                wex("A cuboid brick — same counts as the cube?",
                    ["Yes: $6$ faces, $12$ edges, $8$ vertices — the receipt balances the same way, $6 + 8 - 12 = 2$.",
                     "The difference is the face SHAPES: rectangles instead of squares."],
                    "$6$, $12$, $8$ — rectangles for faces",
                    ["Eq(6 + 8 - 12, 2)", "Eq(3*2, 6)"]),
            ]),
            tryitset("Count the dice", "Pairs, rings, and the receipt.", [
                tp("A cube has how many faces?",
                   ["$6$", "$4$", "$8$"],
                   "Three opposite pairs: $3 \\times 2 = 6$. (Answering $4$ counts only what a drawing shows; $8$ counts the vertices.)",
                   ["Eq(3*2, 6)"]),
                tp("A cube has how many edges?",
                   ["$12$", "$6$", "$8$"],
                   "Top ring $4$, bottom ring $4$, uprights $4$: $4 + 4 + 4 = 12$.",
                   ["Eq(4 + 4 + 4, 12)"]),
                tp("For a cuboid, faces plus vertices minus edges makes:",
                   ["$2$", "$0$", "$26$"],
                   "$6 + 8 = 14$, and $14 - 12 = 2$ (add back: $2 + 12 = 14$ ✓). The $26$ is what you get ADDING all three counts instead.",
                   ["Eq(6 + 8, 14)", "Eq(14 - 12, 2)", "Eq(2 + 12, 14)"]),
            ]),
            tapq("The hidden faces", "In a drawing of a dice you can see 3 faces. How many are hidden?",
                 ["$3$", "$0$", "$6$", "$1$"],
                 "The dice has $6$ in all: $6 - 3 = 3$ hidden (back, bottom and one side). Add back: $3 + 3 = 6$ ✓ — count in pairs and the hidden ones stop escaping.",
                 ["Eq(6 - 3, 3)", "Eq(3 + 3, 6)"]),
            funfact("The dice's secret sevens",
                    "On a standard dice, opposite faces always add to $7$: $1 + 6$, $2 + 5$, $3 + 4$. Three pairs of opposite faces, three sums, one answer. Pick up any board-game dice and check — and notice the pairing uses each number from $1$ to $6$ exactly once."),
            withfig(teach("Concept B", "Round solids and the pyramid", [
                "Not every solid is a box. The SPHERE (ball) is all curve: $0$ flat faces, $0$ edges, $0$ vertices. The CYLINDER (tin can): $2$ circle faces and a curved wrap. The CONE (ice-cream cone): $1$ circle face and a curved slope to a point.",
                "The SQUARE PYRAMID in the picture is flat-faced through and through: $1$ square base $+ 4$ triangles $= 5$ faces, $4 + 1 = 5$ vertices, $4 + 4 = 8$ edges.",
                "Its receipt balances too: $5 + 5 = 10$, $10 - 8 = 2$ ✓. Every flat-faced solid signs the same receipt — the round ones play by their own curved rules.",
            ]), fig_pyr),
            workedset("Pyramids and round solids",
                      "Name the faces, then receipt the flat-faced solids.", [
                withfig(wex("The square pyramid: which 2-D shapes are its faces, and does the receipt balance?",
                    ["$1$ square (the base) $+ 4$ triangles (the slopes) $= 5$ faces.",
                     "Vertices $4 + 1 = 5$, edges $4 + 4 = 8$: receipt $5 + 5 = 10$, $10 - 8 = 2$ ✓."],
                    "$1$ square $+ 4$ triangles; receipt balances at $2$",
                    ["Eq(1 + 4, 5)", "Eq(4 + 1, 5)", "Eq(4 + 4, 8)",
                     "Eq(5 + 5, 10)", "Eq(10 - 8, 2)"]), fig_pyr_faces),
                wex("Flat faces of the round solids: cylinder, cone, sphere — total?",
                    ["Cylinder $2$ circles, cone $1$ circle, sphere none.",
                     "Total: $2 + 1 + 0 = 3$ flat faces among the three of them."],
                    "$3$ flat faces in all",
                    ["Eq(2 + 1 + 0, 3)"]),
            ]),
            tryitset("Round and pointed", "Faces wear 2-D names.", [
                tp("A square pyramid's faces are:",
                   ["$1$ square and $4$ triangles", "$5$ squares", "$4$ squares and $1$ triangle"],
                   "One square base below, four triangle slopes meeting at the apex: $1 + 4 = 5$ faces.",
                   ["Eq(1 + 4, 5)"]),
                tp("Which solid has NO flat face, NO edge and NO vertex?",
                   ["the sphere", "the cylinder", "the cube"],
                   "The ball is all curve. The cylinder keeps $1 + 1 = 2$ flat circle faces; the cube is flat everywhere.",
                   ["Eq(1 + 1, 2)", "0 < 2"]),
                tp("A square pyramid has how many vertices?",
                   ["$5$", "$4$", "$8$"],
                   "$4$ base corners $+ 1$ apex $= 5$. ($4$ forgets the apex; $8$ counts the edges.) Receipt: $5 + 5 - 8 = 2$ ✓.",
                   ["Eq(4 + 1, 5)", "Eq(5 + 5 - 8, 2)"]),
            ]),
            tapq("The receipt catches it", "A student counts a cuboid: 6 faces, 8 vertices, 11 edges. What does the receipt say?",
                 ["recount — $6 + 8 - 11$ makes $3$, not $2$", "the count is fine", "receipts work only for cubes", "the faces must be wrong"],
                 "$6 + 8 = 14$, and $14 - 11 = 3$ (add back: $3 + 11 = 14$). A balanced count makes exactly $2$, so something was miscounted — it is the edges: a cuboid has $12$, and $6 + 8 - 12 = 2$ ✓.",
                 ["Eq(6 + 8, 14)", "Eq(14 - 11, 3)", "Eq(3 + 11, 14)",
                  "Eq(6 + 8 - 12, 2)"]),
            recap([
                "Three counts describe a solid: faces (flat surfaces), edges (meeting lines), vertices (corner points).",
                "Cube and cuboid: 6 faces, 12 edges, 8 vertices — count in pairs and rings.",
                "Faces wear 2-D names: squares, rectangles, the pyramid's 1 square + 4 triangles.",
                "Sphere: no face, edge or vertex; cylinder: 2 circle faces; cone: 1.",
                "The receipt: faces + vertices − edges = 2 for every flat-faced solid — it audits your count.",
            ]),
            tip("For every solid below, count in groups — pairs of faces, rings of edges — then run the receipt before you answer. If it makes anything but 2, recount."),
            tryitset("Mixed practice", "All six solids, all three counts.", [
                withfig(tp("Faces, edges and vertices of a cube, all added together:",
                   ["$26$", "$24$", "$20$"],
                   "$6 + 12 + 8 = 26$. (The receipt is different arithmetic: $6 + 8 - 12 = 2$.)",
                   ["Eq(6 + 12 + 8, 26)", "Eq(6 + 8 - 12, 2)"]), fig_cube2),
                tp("Which solid rolls AND has two flat circle faces?",
                   ["the cylinder", "the cone", "the sphere"],
                   "The tin can: $1 + 1 = 2$ circle faces and a curved wrap between them. The cone has just $1$ circle; the sphere none.",
                   ["Eq(1 + 1, 2)", "1 < 2"]),
                withfig(tp("The square pyramid in the picture has how many edges?",
                   ["$8$", "$5$", "$4$"],
                   "$4$ around the base $+ 4$ rising to the apex $= 8$. Receipt: $5 + 5 - 8 = 2$ ✓.",
                   ["Eq(4 + 4, 8)", "Eq(5 + 5 - 8, 2)"]), fig_pyr2),
                tp("A cuboid brick's faces are which 2-D shape?",
                   ["rectangles", "triangles", "circles"],
                   "Six rectangles, in $3$ equal opposite pairs: $3 \\times 2 = 6$. (A cube is the special cuboid whose rectangles are all squares.)",
                   ["Eq(3*2, 6)"]),
                tp("The cube's receipt and the pyramid's receipt both make:",
                   ["$2$", "$0$", "different numbers"],
                   "Cube: $6 + 8 - 12 = 2$. Pyramid: $5 + 5 - 8 = 2$. Same answer from different counts — that is what makes the receipt worth running.",
                   ["Eq(6 + 8 - 12, 2)", "Eq(5 + 5 - 8, 2)"]),
            ], eyebrow="Chapter practice"),
            funfact("You've finished \"3-D Solids\" — and the topic",
                    "Count the sides, test the corners, try the fold — and now count the faces, edges and vertices too. Every promise a shape makes came with a test, and every test came with a receipt. Grade 5 geometry picks up from here: measuring the boundary and counting the inside.",
                    eyebrow="Chapter complete"),
        ]},
    }

# ==========================================================================
# Practice & test banks
# ==========================================================================

def practice_bank():
    fig_pent = fig_geo(named(reg_poly_pts(5, start=270.0)),
                       poly(["A", "B", "C", "D", "E"], color=C_ACCENT),
                       height=200)
    # Rectangle (1,1)-(8,5): width 8 - 1 = 7, height 5 - 1 = 4.
    fig_rect = fig_geo(
        [P("A", 1, 1), P("B", 8, 1), P("C", 8, 5), P("D", 1, 5)],
        poly(["A", "B", "C", "D"], color=C_WARM) +
        [ang("A", "B", "D", right=True), ang("B", "C", "A", right=True),
         ang("C", "D", "B", right=True), ang("D", "A", "C", right=True)],
        height=190)
    # Square (2,2)-(8,8) with all 4 true mirror lines dashed.
    fig_sq_sym = fig_geo(
        [P("A", 2, 2), P("B", 8, 2), P("C", 8, 8), P("D", 2, 8),
         P("M", 5, 1.2, ""), P("N", 5, 8.8, ""),
         P("U", 1.2, 5, ""), P("V", 8.8, 5, "")],
        poly(["A", "B", "C", "D"], color=C_GREEN) +
        [seg("M", "N", dashed=True, color=C_WARM),
         seg("U", "V", dashed=True, color=C_WARM),
         seg("A", "C", dashed=True, color=C_WARM),
         seg("B", "D", dashed=True, color=C_WARM)],
        height=210)
    fig_cube = make_cube_fig()
    return [
        withprobfig(prob("g4sh-pr1",
             "The shape in the picture has $5$ straight sides. Name it, and count its vertices with the side-ends receipt.",
             "Five sides: a PENTAGON. Ends: $5 \\times 2 = 10$; each vertex joins $2$ ends: $10 \\div 2 = 5$ vertices — corners match sides.",
             ["Eq(5*2, 10)", "Eq(Rational(10,2), 5)"]), fig_pent),
        prob("g4sh-pr2",
             "How many right angles fill a straight line? A full turn? Show both with the quarter-turn arithmetic.",
             "A straight line is half a turn: $2 \\times 90 = 180$, so $2$ right angles. A full turn: $4 \\times 90 = 360$, so $360 \\div 90 = 4$.",
             ["Eq(2*90, 180)", "Eq(4*90, 360)", "Eq(Rational(360,90), 4)"]),
        withprobfig(prob("g4sh-pr3",
             "The rectangle in the picture has corners $(1, 1)$, $(8, 1)$, $(8, 5)$, $(1, 5)$. Check its opposite sides are equal, and say why it is not a square.",
             "Bottom and top: $8 - 1 = 7$ each (add back $7 + 1 = 8$ ✓). Left and right: $5 - 1 = 4$ each ($4 + 1 = 5$ ✓). Opposite pairs match: a rectangle. But $7 > 4$ — neighbouring sides differ, so it is not a square.",
             ["Eq(8 - 1, 7)", "Eq(7 + 1, 8)", "Eq(5 - 1, 4)", "Eq(4 + 1, 5)",
              "7 > 4"]), fig_rect),
        prob("g4sh-pr4",
             "A student says a square is not a rectangle. Run the rectangle's two tests on a square and settle it.",
             "Test 1 — four right angles: yes, $4 \\times 90 = 360$, a full turn of page corners. Test 2 — opposite sides equal: yes, ALL its sides are equal. Both passed: $1 + 1 = 2$. Every square IS a rectangle; the equal sides are a bonus, not a fault.",
             ["Eq(4*90, 360)", "Eq(1 + 1, 2)"]),
        withprobfig(prob("g4sh-pr5",
             "The square in the picture shows its mirror lines dashed. How many are there, and where does the vertical one stand?",
             "Four: the rectangle's $2$ side-middle lines plus the square's $2$ diagonals — $2 + 2 = 4$. The vertical stands at the true middle: $2 + 8 = 10$, $10 \\div 2 = 5$.",
             ["Eq(2 + 2, 4)", "Eq(2 + 8, 10)", "Eq(Rational(10,2), 5)"]), fig_sq_sym),
        prob("g4sh-pr6",
             "Count the lines of symmetry of the block letters M, O, M — and the total for the word MOM.",
             "M: $1$ vertical line. O: $2$ — vertical and horizontal. M: $1$. Total: $1 + 2 + 1 = 4$ — and the shared vertical mirror is why MOM survives a real mirror unchanged.",
             ["Eq(1 + 2 + 1, 4)"]),
        withprobfig(prob("g4sh-pr7",
             "Count the cube in the picture — faces, edges, vertices — and run the receipt.",
             "Faces in opposite pairs: $3 \\times 2 = 6$. Edges as rings and uprights: $4 + 4 + 4 = 12$. Vertices: $4 + 4 = 8$. Receipt: $6 + 8 = 14$, $14 - 12 = 2$ ✓ (add back: $2 + 12 = 14$).",
             ["Eq(3*2, 6)", "Eq(4 + 4 + 4, 12)", "Eq(4 + 4, 8)",
              "Eq(6 + 8, 14)", "Eq(14 - 12, 2)", "Eq(2 + 12, 14)"]), fig_cube),
        prob("g4sh-pr8",
             "A square pyramid: name its faces with their 2-D shapes, count everything, and receipt the count.",
             "Faces: $1$ square base $+ 4$ triangles $= 5$. Vertices: $4$ base corners $+ 1$ apex $= 5$. Edges: $4 + 4 = 8$. Receipt: $5 + 5 = 10$, $10 - 8 = 2$ ✓.",
             ["Eq(1 + 4, 5)", "Eq(4 + 1, 5)", "Eq(4 + 4, 8)",
              "Eq(5 + 5, 10)", "Eq(10 - 8, 2)"]),
    ]


def test_bank():
    fig_hex = fig_geo(named(reg_poly_pts(6, start=30.0)),
                      poly(["A", "B", "C", "D", "E", "F"], color=C_ACCENT),
                      height=200)
    # Rectangle (1,2)-(9,6) with right-angle marks: width 8, height 4.
    fig_rect = fig_geo(
        [P("A", 1, 2), P("B", 9, 2), P("C", 9, 6), P("D", 1, 6)],
        poly(["A", "B", "C", "D"], color=C_GREEN) +
        [ang("A", "B", "D", right=True), ang("B", "C", "A", right=True),
         ang("C", "D", "B", right=True), ang("D", "A", "C", right=True)],
        height=190)
    fig_pyr = make_pyramid_fig()
    return [
        withprobfig(prob("g4sh-x1",
             "Name the shape in the picture, and use the side-ends receipt to count its vertices.",
             "Six straight sides: a HEXAGON. Ends: $6 \\times 2 = 12$; vertices: $12 \\div 2 = 6$ — the corners match the sides.",
             ["Eq(6*2, 12)", "Eq(Rational(12,2), 6)"]), fig_hex),
        prob("g4sh-x2",
             "A dancer makes three quarter turns, always the same way. How much of a full turn is that — and how much more would close the spin?",
             "Three quarters: $3 \\times 90 = 270$ degrees. The full turn is $360$, so one more quarter closes it: $360 - 270 = 90$, and $270 + 90 = 360$ ✓.",
             ["Eq(3*90, 270)", "Eq(360 - 270, 90)", "Eq(270 + 90, 360)"]),
        withprobfig(prob("g4sh-x3",
             "The shape in the picture has corners $(1, 2)$, $(9, 2)$, $(9, 6)$, $(1, 6)$, all right angles. Sort it: quadrilateral, rectangle, or square?",
             "Opposite sides: $9 - 1 = 8$ and $8$ ($8 + 1 = 9$ ✓); $6 - 2 = 4$ and $4$ ($4 + 2 = 6$ ✓). Right angles and matching opposite pairs: a RECTANGLE. Not a square: $8 > 4$. (It is also a quadrilateral — the family holds all its members.)",
             ["Eq(9 - 1, 8)", "Eq(8 + 1, 9)", "Eq(6 - 2, 4)", "Eq(4 + 2, 6)",
              "8 > 4"]), fig_rect),
        prob("g4sh-x4",
             "A rectangle has $2$ lines of symmetry and a square has $4$. How many more has the square, and where do the extra ones run?",
             "$4 - 2 = 2$ more (add back: $2 + 2 = 4$ ✓) — the two diagonals, corner to corner. The rectangle's diagonal folds overhang, because its neighbouring sides differ.",
             ["Eq(4 - 2, 2)", "Eq(2 + 2, 4)"]),
        prob("g4sh-x5",
             "Count a cuboid's faces, edges and vertices, and prove the count balanced with the receipt.",
             "Faces: $3 \\times 2 = 6$; edges: $4 + 4 + 4 = 12$; vertices: $4 + 4 = 8$. Receipt: $6 + 8 = 14$, $14 - 12 = 2$ ✓ — a balanced count.",
             ["Eq(3*2, 6)", "Eq(4 + 4 + 4, 12)", "Eq(4 + 4, 8)",
              "Eq(6 + 8, 14)", "Eq(14 - 12, 2)"]),
        withprobfig(prob("g4sh-x6",
             "The square pyramid in the picture wears $1$ square face and $4$ triangle faces. Count the faces — and then count the SIDES of all five faces put together.",
             "Faces: $1 + 4 = 5$. Sides of the faces: the square brings $4$, each triangle brings $3$ — $4 + 4 \\times 3 = 4 + 12 = 16$ sides drawn across the five faces. (Fewer edges than that — $8$ — because on the solid, faces share their edges in pairs: $16 \\div 2 = 8$.)",
             ["Eq(1 + 4, 5)", "Eq(4*3, 12)", "Eq(4 + 12, 16)",
              "Eq(Rational(16,2), 8)"]), fig_pyr),
    ]


def main():
    topic = {
        "slug": "shapes-and-symmetry",
        "title": "Shapes & Symmetry",
        "grade": 4,
        "status": "published",
        "blurb": ("Naming 2-D shapes by their sides, right angles as "
                  "quarter turns, sorting quadrilaterals, the fold test for "
                  "line symmetry, and the faces, edges and vertices of 3-D "
                  "solids."),
        "lessons": [
            lesson_two_d_shapes(),
            lesson_right_angles(),
            lesson_sorting_quadrilaterals(),
            lesson_line_symmetry(),
            lesson_three_d_solids(),
        ],
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }
    write_topic(topic, "shapes-and-symmetry.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
