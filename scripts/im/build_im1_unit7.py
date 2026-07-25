#!/usr/bin/env python3
"""Integrated Mathematics 1 — Unit 7: Transformations & Congruence.

CCSS Integrated Math I: G-CO.1-5 (precise definitions; transformations as
functions of the plane; representing them with coordinate rules; predicting the
effect of a sequence), G-CO.6-8 (congruence DEFINED by rigid motion, and the
triangle criteria SSS, SAS and ASA following from it), G-CO.12-13 (formal
compass-and-straightedge constructions).

This is where the integrated pathway differs most sharply from the traditional
one. Congruence is not asserted and then used — it is DEFINED as "there is a
sequence of rigid motions carrying one figure onto the other", and the shortcuts
are consequences of that definition. Transformations arrive here rather than
late in a geometry year because Unit 4 already established the coordinate plane.

Run: python3 scripts/im/build_im1_unit7.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-1"


# ===========================================================================
# Lesson 1 — G-CO.2, G-CO.4, G-CO.5: the three rigid motions
# ===========================================================================
def lesson_rigid_motions():
    return lesson(
        slug="rigid-motions",
        title="Translations, Reflections & Rotations",
        concrete=(
            "Slide a book across a table, flip it over, or spin it round — the book is the same "
            "book afterwards. Same page count, same dimensions, same everything except where it "
            "sits. Those three moves are the only ones geometry calls RIGID, and they are the "
            "entire vocabulary of congruence."
        ),
        objective=(
            "Apply a translation, reflection or rotation to a figure using its coordinate rule, "
            "predict the image, and explain why each preserves distance and angle."
        ),
        concept=[
            "**A transformation is a function on the plane.** It takes each point as an input and "
            "returns another point as its output. That is the same idea as Unit 3's functions, "
            "with the input and output being locations rather than numbers — and it is why "
            "transformations belong in a course that has already built the function concept.",
            "**Rigid means distance-preserving.** A rigid motion (or ISOMETRY) keeps every "
            "distance between points the same. Because distances survive, so do angles, areas and "
            "shape — the figure moves without changing. Exactly three basic kinds exist in the "
            "plane: translations, reflections and rotations.",
            "**Translation: slide by a vector.** Every point moves the same distance in the same "
            "direction. The rule is $(x, y) \\to (x + a, y + b)$. Nothing turns and nothing flips; "
            "the image is the original in a new position, facing the same way.",
            "**Reflection: flip across a line.** Each point lands the same distance from the "
            "mirror line, on the opposite side. Across the $x$-axis the rule is "
            "$(x, y) \\to (x, -y)$; across the $y$-axis it is $(x, y) \\to (-x, y)$; across the "
            "line $y = x$ it is $(x, y) \\to (y, x)$. A reflection reverses ORIENTATION — a "
            "clockwise labelling becomes anticlockwise — which is the one visible way it differs "
            "from a slide or a turn.",
            "**Rotation: turn about a centre.** About the origin, a quarter turn anticlockwise is "
            "$(x, y) \\to (-y, x)$, a half turn is $(x, y) \\to (-x, -y)$, and a three-quarter "
            "turn is $(x, y) \\to (y, -x)$. The centre stays fixed; everything else swings around "
            "it at a constant distance.",
            "**Dilation is NOT rigid.** Scaling by a factor $k$, $(x, y) \\to (kx, ky)$, changes "
            "every distance. The image is the same SHAPE but a different SIZE — similar, not "
            "congruent. It matters here only as the contrast that makes 'rigid' meaningful; "
            "similarity is IM2's subject.",
        ],
        key_idea=(
            "Translations slide, reflections flip, rotations turn — and all three preserve every "
            "distance, so the image is congruent to the original. A dilation does not, so it is "
            "excluded."
        ),
        facts=[
            fact(
                "Translation",
                "(x, y) \\to (x + a, \\ y + b)",
                "Every point moves the same way. Orientation and facing are unchanged.",
            ),
            fact(
                "Reflections in the three standard lines",
                "x\\text{-axis}: (x, -y) \\qquad y\\text{-axis}: (-x, y) \\qquad "
                "y = x: (y, x)",
                "Each point lands the same distance the other side of the mirror. Orientation "
                "reverses.",
            ),
            fact(
                "Rotations about the origin",
                "90°: (-y, x) \\qquad 180°: (-x, -y) \\qquad 270°: (y, -x)",
                "Anticlockwise by convention. The centre is the one point that does not move.",
            ),
        ],
        worked=[
            problem(
                "im1-u7-l1-we1",
                "Triangle $ABC$ has vertices $A(1, 2)$, $B(4, 2)$, $C(1, 6)$. Apply the "
                "translation $(x, y) \\to (x + 3, y - 5)$ and verify a side length is preserved.",
                "**Apply the rule to each vertex.**"
                "$$A(1, 2) \\to A'(4, -3), \\quad B(4, 2) \\to B'(7, -3), \\quad "
                "C(1, 6) \\to C'(4, 1).$$"
                "Every point moved $3$ right and $5$ down — the same journey for all three, which "
                "is what makes it a translation."
                "**Check a side length.** In the original, $AB$ runs from $(1,2)$ to $(4,2)$, a "
                "horizontal segment of length $|4 - 1| = 3$. In the image, $A'B'$ runs from "
                "$(4,-3)$ to $(7,-3)$, length $|7 - 4| = 3$. Preserved ✓"
                "**And another.** $AC$ is vertical from $(1,2)$ to $(1,6)$, length $4$. $A'C'$ "
                "runs from $(4,-3)$ to $(4,1)$, length $|1 - (-3)| = 4$. Preserved ✓"
                "Distances survive, so the image is congruent to the original.",
                [
                    "Eq(1 + 3, 4)",
                    "Eq(2 - 5, -3)",
                    "Eq(Abs(4 - 1), Abs(7 - 4))",
                    "Eq(Abs(6 - 2), Abs(1 - (-3)))",
                ],
            ),
            problem(
                "im1-u7-l1-we2",
                "Reflect the points $P(3, 5)$, $Q(-2, 4)$ and $R(0, -1)$ across the $x$-axis, then "
                "across the $y$-axis, and describe what happens to each.",
                "**Flipping over the horizontal axis.** The rule is $(x, y) \\to (x, -y)$:"
                "$$P(3, 5) \\to (3, -5), \\quad Q(-2, 4) \\to (-2, -4), \\quad "
                "R(0, -1) \\to (0, 1).$$"
                "The first coordinate is untouched; only the height flips sign. A point $5$ above "
                "the axis lands $5$ below it."
                "**Flipping over the vertical axis.** The rule is $(x, y) \\to (-x, y)$:"
                "$$P(3, 5) \\to (-3, 5), \\quad Q(-2, 4) \\to (2, 4), \\quad "
                "R(0, -1) \\to (0, -1).$$"
                "Now the height is untouched and the horizontal position flips."
                "**The third point is special.** Reflecting $(0, -1)$ across the $y$-axis leaves it exactly where it "
                "was, because it already sits ON the mirror line. Points on the mirror are fixed "
                "— they are the only ones a reflection does not move.",
                [
                    "Eq(-(-1), 1)",
                    "Eq(-(-2), 2)",
                    "Eq(-0, 0)",
                    "Eq(Abs(5 - 0), Abs(-5 - 0))",
                ],
            ),
            problem(
                "im1-u7-l1-we3",
                "Rotate the point $A(3, 1)$ about the origin by $90°$, $180°$ and $270°$ "
                "anticlockwise, and check the distance from the origin is unchanged.",
                "**Apply each rule.**"
                "$$90°: (x, y) \\to (-y, x), \\qquad A(3, 1) \\to (-1, 3).$$"
                "$$180°: (x, y) \\to (-x, -y), \\qquad A(3, 1) \\to (-3, -1).$$"
                "$$270°: (x, y) \\to (y, -x), \\qquad A(3, 1) \\to (1, -3).$$"
                "**Check the distance from the origin.** For the original, "
                "$\\sqrt{3^2 + 1^2} = \\sqrt{10}$. For the $90°$ image, "
                "$\\sqrt{(-1)^2 + 3^2} = \\sqrt{10}$ ✓. For the $180°$ image, "
                "$\\sqrt{9 + 1} = \\sqrt{10}$ ✓. For the $270°$ image, "
                "$\\sqrt{1 + 9} = \\sqrt{10}$ ✓"
                "All four points sit on a circle of radius $\\sqrt{10}$ centred at the origin — "
                "which is exactly what rotating about the origin means. The centre is the only "
                "point that stays put.",
                [
                    "Eq(3**2 + 1**2, 10)",
                    "Eq((-1)**2 + 3**2, 10)",
                    "Eq((-3)**2 + (-1)**2, 10)",
                    "Eq(1**2 + (-3)**2, 10)",
                ],
            ),
            problem(
                "im1-u7-l1-we4",
                "A triangle has vertices $(0, 0)$, $(4, 0)$, $(0, 3)$, labelled anticlockwise. "
                "Apply a translation and then a reflection across the $y$-axis, and say what "
                "happens to its orientation and side lengths.",
                "**First, the translation** by $(x, y) \\to (x + 2, y + 1)$."
                "$$(0,0) \\to (2,1), \\quad (4,0) \\to (6,1), \\quad (0,3) \\to (2,4).$$"
                "**Then the reflection** across the vertical axis, using $(x, y) \\to (-x, y)$:"
                "$$(2,1) \\to (-2,1), \\quad (6,1) \\to (-6,1), \\quad (2,4) \\to (-2,4).$$"
                "**Side lengths.** The original legs are $4$ and $3$, with hypotenuse "
                "$\\sqrt{16 + 9} = 5$. In the final image the horizontal leg runs from $(-2,1)$ "
                "to $(-6,1)$, length $4$ ✓; the vertical leg from $(-2,1)$ to $(-2,4)$, length "
                "$3$ ✓; and the hypotenuse from $(-6,1)$ to $(-2,4)$ is "
                "$\\sqrt{16 + 9} = 5$ ✓. All preserved — both moves were rigid."
                "**Orientation.** The translation kept the anticlockwise labelling. The reflection "
                "REVERSED it, so the final triangle is labelled clockwise. This is the "
                "distinguishing feature of reflections: an odd number of them flips orientation, "
                "an even number restores it.",
                [
                    "Eq(4**2 + 3**2, 25)",
                    "Eq(sqrt(25), 5)",
                    "Eq(Abs(-6 - (-2)), 4)",
                    "Eq(Abs(4 - 1), 3)",
                    "Eq((-2 - (-6))**2 + (4 - 1)**2, 25)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Reflecting across the x-axis by negating the first coordinate.",
                "Across the x-axis the HEIGHT flips: (x, y) → (x, −y). Negating x is the "
                "reflection across the y-axis instead.",
            ),
            mistake(
                "Applying a 90° rotation as (y, x) rather than (−y, x).",
                "(y, x) is the reflection across the line y = x, which reverses orientation. A "
                "rotation does not — check by rotating (1, 0), which must land on (0, 1).",
            ),
            mistake(
                "Calling a dilation a rigid motion because the shape looks the same.",
                "Rigid means every DISTANCE is preserved. A dilation changes them all, so the "
                "image is similar but not congruent.",
            ),
            mistake(
                "Applying a sequence of transformations in the wrong order.",
                "Transformations are functions, and order matters. Translate-then-reflect and "
                "reflect-then-translate usually land in different places.",
            ),
        ],
        try_it=[
            problem(
                "im1-u7-l1-t1",
                "Apply $(x, y) \\to (x - 4, y + 2)$ to $A(5, 1)$ and $B(2, -3)$, and check the "
                "distance $AB$ is unchanged.",
                "$A(5,1) \\to (1, 3)$ and $B(2,-3) \\to (-2, -1)$. Original distance: "
                "$\\sqrt{(5-2)^2 + (1+3)^2} = \\sqrt{9 + 16} = 5$. Image distance: "
                "$\\sqrt{(1+2)^2 + (3+1)^2} = \\sqrt{9 + 16} = 5$ ✓",
                [
                    "Eq((5 - 2)**2 + (1 - (-3))**2, 25)",
                    "Eq((1 - (-2))**2 + (3 - (-1))**2, 25)",
                    "Eq(sqrt(25), 5)",
                ],
            ),
            problem(
                "im1-u7-l1-t2",
                "Reflect $(6, -2)$ across the $x$-axis, the $y$-axis, and the line $y = x$.",
                "Across the $x$-axis: $(6, 2)$. Across the $y$-axis: $(-6, -2)$. Across "
                "$y = x$: swap the coordinates, giving $(-2, 6)$.",
                [
                    "Eq(-(-2), 2)",
                    "Eq(-6, -6)",
                    "Eq(6*(-2), -12)",
                ],
            ),
            problem(
                "im1-u7-l1-t3",
                "Rotate $(-2, 5)$ about the origin by $180°$, and verify its distance from the "
                "origin is unchanged.",
                "The rule is $(x, y) \\to (-x, -y)$, giving $(2, -5)$. Distance before: "
                "$\\sqrt{4 + 25} = \\sqrt{29}$. Distance after: $\\sqrt{4 + 25} = \\sqrt{29}$ ✓",
                [
                    "Eq((-2)**2 + 5**2, 29)",
                    "Eq(2**2 + (-5)**2, 29)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "G-CO.2",
                "title": "A transformation is a function on the plane",
                "body": (
                    "It takes a point in and returns a point out — the same idea as Unit 3's "
                    "functions, with locations instead of numbers. That is why this unit can sit "
                    "here rather than late in a separate geometry year."
                ),
                "beats": [
                    "Input: a point $(x, y)$",
                    "Output: another point",
                    "Written as a **rule**: $(x, y) \\to (x + 3, y - 5)$",
                    "Apply it to every vertex to move the whole figure",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "G-CO.4",
                "title": "Rigid means every distance survives",
                "body": (
                    "A rigid motion keeps all distances between points the same. Because distances "
                    "survive, so do angles, areas and shape — the figure is genuinely unchanged, "
                    "only relocated. Exactly three basic kinds exist."
                ),
            },
            {
                "kind": "transformPlane",
                "eyebrow": "Slide",
                "title": "Translation: every point makes the same journey",
                "teach": (
                    "$(x, y) \\to (x + 5, y + 2)$. Notice each vertex moves by the same vector — "
                    "nothing turns, nothing flips, and every side keeps its length and direction."
                ),
                "config": {"transform": "translate", "dx": 5, "dy": 2, "min": -6, "max": 8},
            },
            {"kind": "worked", "title": "A translated triangle, distances checked", "problemId": "im1-u7-l1-we1"},
            {
                "kind": "transformPlane",
                "eyebrow": "Flip",
                "title": "Reflection: the same distance, the other side",
                "teach": (
                    "Across the $x$-axis, $(x, y) \\to (x, -y)$. Each point lands as far below the "
                    "mirror as it was above. Points sitting ON the mirror do not move at all."
                ),
                "config": {"transform": "reflectX", "min": -6, "max": 6},
            },
            tap(
                "Which rule reflects across the y-axis?",
                "Which coordinate rule reflects a point across the $y$-axis?",
                [
                    "$(x, y) \\to (x, -y)$",
                    "$(x, y) \\to (-x, y)$",
                    "$(x, y) \\to (y, x)$",
                    "$(x, y) \\to (-x, -y)$",
                ],
                1,
                "The $y$-axis is vertical, so a reflection across it changes how far LEFT or RIGHT "
                "a point sits while leaving its height alone: $(x, y) \\to (-x, y)$. Test on "
                "$(3, 5)$: it should land at $(-3, 5)$, the same height, three units the other "
                "side. Option A is the $x$-axis; option C is the line $y = x$; option D is a "
                "half-turn.",
                [
                    "Eq(-3, -3)",
                    "Eq(Abs(3 - 0), Abs(-3 - 0))",
                ],
            ),
            {"kind": "worked", "title": "Reflecting in both axes", "problemId": "im1-u7-l1-we2"},
            {
                "kind": "transformPlane",
                "eyebrow": "Turn",
                "title": "Rotation: everything swings about a fixed centre",
                "teach": (
                    "A quarter turn about the origin: $(x, y) \\to (-y, x)$. Every point keeps its "
                    "distance from the centre and swings round it. The centre itself is the one "
                    "point that never moves."
                ),
                "config": {"transform": "rotate", "deg": 90, "min": -6, "max": 6},
            },
            {"kind": "worked", "title": "Three rotations, one radius", "problemId": "im1-u7-l1-we3"},
            tap(
                "Where does a quarter turn send this point?",
                "Rotating $(2, 5)$ by $90°$ anticlockwise about the origin lands it where?",
                ["$(-5, 2)$", "$(5, 2)$", "$(5, -2)$", "$(-2, -5)$"],
                0,
                "The rule is $(x, y) \\to (-y, x)$, so $(2, 5) \\to (-5, 2)$. Check the distance "
                "from the origin: $\\sqrt{4 + 25} = \\sqrt{29}$ before and "
                "$\\sqrt{25 + 4} = \\sqrt{29}$ after ✓. Option B, $(5, 2)$, is the reflection "
                "across $y = x$, which reverses orientation — a rotation must not.",
                [
                    "Eq(2**2 + 5**2, 29)",
                    "Eq((-5)**2 + 2**2, 29)",
                    "Eq(5**2 + 2**2, 29)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "The distinguishing feature",
                "title": "Reflections reverse orientation; slides and turns do not",
                "body": (
                    "Label a triangle's vertices anticlockwise. A translation or rotation keeps "
                    "them anticlockwise. A reflection makes them clockwise. An odd number of "
                    "reflections flips orientation; an even number restores it."
                ),
            },
            {"kind": "worked", "title": "A sequence, and what it does to orientation", "problemId": "im1-u7-l1-we4"},
            {
                "kind": "tip",
                "title": "Order matters — these are functions",
                "body": (
                    "Translate then reflect, and reflect then translate, usually land in different "
                    "places. Apply the moves in the order stated, one at a time, writing the "
                    "coordinates down after each. Trying to do both at once is where the errors "
                    "come from."
                ),
            },
            {
                "kind": "transformPlane",
                "eyebrow": "The contrast",
                "title": "Dilation: same shape, different size",
                "teach": (
                    "$(x, y) \\to (2x, 2y)$ doubles every distance. The image is the same SHAPE — "
                    "so it is similar — but it is not congruent, because rigid motions must "
                    "preserve distance. This is the contrast that makes 'rigid' mean something."
                ),
                "config": {"transform": "dilate", "k": 2, "min": -8, "max": 8},
            },
            {"kind": "tryIt", "title": "Your turn — translate and measure", "problemId": "im1-u7-l1-t1"},
            {"kind": "tryIt", "title": "Your turn — three reflections", "problemId": "im1-u7-l1-t2"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "A transformation is a function taking points to points",
                    "Rigid = every distance preserved, so angles and shape survive",
                    "Translate $(x+a, y+b)$; reflect $(x,-y)$, $(-x,y)$, $(y,x)$; rotate $(-y,x)$, $(-x,-y)$, $(y,-x)$",
                    "Reflections reverse orientation; translations and rotations do not",
                    "A dilation is **not** rigid — it changes every distance",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 2 — G-CO.5, G-CO.3: sequences and symmetry
# ===========================================================================
def lesson_sequences():
    return lesson(
        slug="sequences-of-transformations-and-symmetry",
        title="Sequences of Transformations & Symmetry",
        concrete=(
            "A tiled floor repeats because the pattern can be slid onto itself. A butterfly looks "
            "balanced because it can be flipped onto itself. Symmetry is not a vague aesthetic "
            "judgement — it is the precise statement that some rigid motion maps a figure exactly "
            "onto where it already was."
        ),
        objective=(
            "Apply a sequence of rigid motions and find the single motion equivalent to it, and "
            "describe a figure's line and rotational symmetry as the motions that carry it onto "
            "itself."
        ),
        concept=[
            "**Apply a sequence one move at a time.** Write the coordinates after each step. "
            "Trying to combine two transformations mentally is the reliable way to get a wrong "
            "answer; two extra lines of working is the reliable way to get a right one.",
            "**A sequence of rigid motions is itself rigid.** Each move preserves distance, so "
            "doing several in a row preserves distance too. That is why congruence can be defined "
            "through sequences rather than single moves — you never leave the world of rigid "
            "motions by composing them.",
            "**Two reflections make a rotation or a translation.** Reflecting across two "
            "INTERSECTING lines produces a rotation about their intersection, through twice the "
            "angle between them. Reflecting across two PARALLEL lines produces a translation, "
            "twice the distance between them. Both results restore orientation, because two "
            "reversals cancel.",
            "**Symmetry is a motion that changes nothing.** A figure has LINE symmetry if some "
            "reflection maps it onto itself, and ROTATIONAL symmetry if some rotation of less than "
            "a full turn does. A square has four lines of symmetry and rotational symmetry of "
            "order $4$ — quarter, half and three-quarter turns all leave it looking identical.",
            "**Counting symmetry precisely.** A regular $n$-gon has exactly $n$ lines of symmetry "
            "and rotational symmetry of order $n$, the smallest turn being $\\frac{360°}{n}$. An "
            "equilateral triangle: $3$ and $120°$. A regular hexagon: $6$ and $60°$. The full "
            "turn is not counted as a symmetry, since every figure has that trivially.",
        ],
        key_idea=(
            "Apply a sequence one move at a time. Composing rigid motions gives a rigid motion, "
            "and a symmetry is simply a rigid motion that maps a figure onto itself."
        ),
        facts=[
            fact(
                "Two reflections in parallel lines",
                "\\text{a translation of twice the distance between them}",
                "Orientation reverses twice, so it is restored — the result is a slide.",
            ),
            fact(
                "Two reflections in intersecting lines",
                "\\text{a rotation about the intersection, through twice the angle}",
                "Again orientation is restored, so the composite is a turn.",
            ),
            fact(
                "Regular polygon symmetry",
                "n\\text{-gon}: n \\text{ lines}, \\ \\text{order } n, \\ "
                "\\text{smallest turn } \\tfrac{360°}{n}",
                "A square: 4 lines, order 4, 90°. A regular hexagon: 6 lines, order 6, 60°.",
            ),
        ],
        worked=[
            problem(
                "im1-u7-l2-we1",
                "Apply to $A(2, 3)$: first the translation $(x, y) \\to (x + 4, y - 1)$, then the "
                "reflection across the $x$-axis. Then reverse the order and compare.",
                "**Translate first, then reflect.**"
                "$$A(2, 3) \\to (6, 2) \\to (6, -2).$$"
                "**Reflect first, then translate.**"
                "$$A(2, 3) \\to (2, -3) \\to (6, -4).$$"
                "**Compare.** $(6, -2)$ and $(6, -4)$ are different points. The order genuinely "
                "matters, and this is the standard demonstration of why."
                "**Why they differ.** In the first order the translation's downward step of $1$ "
                "happens BEFORE the flip, so the flip reverses it. In the second it happens after, "
                "so it adds to the flipped position. The two effects land two units apart — which "
                "is twice the vertical component of the translation, as you would expect.",
                [
                    "Eq(2 + 4, 6)",
                    "Eq(3 - 1, 2)",
                    "Eq(-2, -2)",
                    "Eq(-3 - 1, -4)",
                    "Ne(-2, -4)",
                    "Eq(Abs(-2 - (-4)), 2)",
                ],
            ),
            problem(
                "im1-u7-l2-we2",
                "Reflect the point $P(5, 2)$ across the $x$-axis and then across the $y$-axis. "
                "What single transformation has the same effect?",
                "**Step one.** Across the $x$-axis: $(5, 2) \\to (5, -2)$."
                "**Step two.** Across the $y$-axis: $(5, -2) \\to (-5, -2)$."
                "**The net effect.** $(5, 2) \\to (-5, -2)$ — both coordinates negated, which is "
                "exactly the rule $(x, y) \\to (-x, -y)$: a **half turn about the origin**, a rotation of $180°$."
                "**Why a rotation.** The two mirror lines (the axes) intersect at right angles, so "
                "the composite is a rotation through twice that angle: $2 \\times 90° = 180°$ ✓"
                "**Orientation check.** Each reflection reverses orientation, so two reflections "
                "restore it — and a rotation does preserve orientation, consistent with the "
                "result. Test on a second point: $(1, 4) \\to (1, -4) \\to (-1, -4)$, again both "
                "coordinates negated ✓",
                [
                    "Eq(-5, -(5))",
                    "Eq(-2, -(2))",
                    "Eq(-1, -(1))",
                    "Eq(-4, -(4))",
                    "Eq(2*90, 180)",
                ],
            ),
            problem(
                "im1-u7-l2-we3",
                "Describe all the symmetry of a square, and of a rectangle that is not a square.",
                "**A square.**"
                "Line symmetry: four axes — the two diagonals, plus the horizontal and vertical "
                "lines through the centre. Reflecting across any of them leaves the square looking "
                "identical."
                "Rotational symmetry: order $4$. Turns of $90°$, $180°$ and $270°$ about the "
                "centre all map it onto itself, and the smallest is "
                "$\\frac{360°}{4} = 90°$."
                "**A non-square rectangle.**"
                "Line symmetry: only TWO axes — the horizontal and vertical lines through the "
                "centre. The diagonals are NOT lines of symmetry: reflecting across a diagonal "
                "would have to send a long side onto a short one, and they are different lengths."
                "Rotational symmetry: order $2$. Only the $180°$ turn works; a $90°$ turn would "
                "swap the long and short sides, changing the figure's outline."
                "**The pattern.** Symmetry counts how much a shape's regularity constrains it. "
                "Making the sides unequal costs the square half its symmetry in both kinds at "
                "once.",
                [
                    "Eq(Rational(360,4), 90)",
                    "Eq(Rational(360,2), 180)",
                    "Eq(4, 2*2)",
                ],
            ),
            problem(
                "im1-u7-l2-we4",
                "Find the line and rotational symmetry of an equilateral triangle and of a regular "
                "hexagon, and state the general rule.",
                "**The equilateral triangle,** with $n = 3$."
                "Three lines of symmetry, each running from a vertex to the midpoint of the "
                "opposite side. Rotational symmetry of order $3$, with the smallest turn"
                "$$\\frac{360°}{3} = 120°.$$"
                "So $120°$ and $240°$ both map it onto itself."
                "**The regular hexagon,** with $n = 6$."
                "Six lines of symmetry — three through opposite vertices, three through opposite "
                "edge midpoints. Rotational symmetry of order $6$, smallest turn"
                "$$\\frac{360°}{6} = 60°.$$"
                "**The general rule.** A regular $n$-gon has exactly $n$ lines of symmetry and "
                "rotational symmetry of order $n$, the smallest turn being $\\frac{360°}{n}$."
                "**Why the full turn is not counted.** A $360°$ rotation maps EVERY figure onto "
                "itself, symmetric or not, so counting it would tell you nothing. Order counts the "
                "distinct positions the shape can occupy and still look the same — including the "
                "starting one, which is why a square's order is $4$ rather than $3$.",
                [
                    "Eq(Rational(360,3), 120)",
                    "Eq(Rational(360,6), 60)",
                    "Eq(2*120, 240)",
                    "Eq(3*120, 360)",
                    "Eq(6*60, 360)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Assuming a sequence gives the same result in either order.",
                "Translate-then-reflect and reflect-then-translate usually differ. Apply the moves "
                "in the stated order, writing coordinates after each.",
            ),
            mistake(
                "Claiming a non-square rectangle has four lines of symmetry.",
                "Its diagonals are not lines of symmetry — reflecting across one would map a long "
                "side onto a short side. Only two axes work.",
            ),
            mistake(
                "Counting the 360° rotation as a rotational symmetry.",
                "Every figure has that trivially. Rotational symmetry counts turns of less than a "
                "full revolution that leave the figure looking identical.",
            ),
            mistake(
                "Assuming line symmetry and rotational symmetry always come together.",
                "A parallelogram that is not a rectangle or rhombus has 180° rotational symmetry "
                "and NO lines of symmetry at all.",
            ),
        ],
        try_it=[
            problem(
                "im1-u7-l2-t1",
                "Apply to $(1, 4)$: a reflection across the $y$-axis, then the translation "
                "$(x, y) \\to (x + 3, y + 2)$.",
                "Reflect: $(1, 4) \\to (-1, 4)$. Then translate: $(-1, 4) \\to (2, 6)$. The final "
                "image is $(2, 6)$.",
                [
                    "Eq(-1 + 3, 2)",
                    "Eq(4 + 2, 6)",
                ],
            ),
            problem(
                "im1-u7-l2-t2",
                "How many lines of symmetry does a regular octagon have, and what is its smallest "
                "rotational symmetry?",
                "A regular $8$-gon has $8$ lines of symmetry and rotational symmetry of order "
                "$8$, with smallest turn $\\frac{360°}{8} = 45°$.",
                [
                    "Eq(Rational(360,8), 45)",
                    "Eq(8*45, 360)",
                ],
            ),
            problem(
                "im1-u7-l2-t3",
                "A point is reflected across the $x$-axis and then across the $x$-axis again. What "
                "is the net effect?",
                "$(x, y) \\to (x, -y) \\to (x, y)$ — the point returns to where it started. Two "
                "identical reflections cancel, so the net effect is the identity: nothing moves.",
                [
                    "Eq(-(-7), 7)",
                    "Eq(-(-(3)), 3)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "G-CO.5",
                "title": "One move at a time, coordinates written down",
                "body": (
                    "Apply the first transformation and record the result. Then apply the second "
                    "to THAT. Two extra lines of working replace a guess, and the guess is usually "
                    "wrong."
                ),
            },
            {"kind": "worked", "title": "The same two moves, both orders", "problemId": "im1-u7-l2-we1"},
            {
                "kind": "tip",
                "title": "Order matters, and here is the proof",
                "body": (
                    "Translating $(2,3)$ then flipping gives $(6,-2)$. Flipping then translating "
                    "gives $(6,-4)$. Same two moves, different destinations — because a "
                    "transformation is a function, and composing functions is not commutative."
                ),
            },
            {
                "kind": "teach",
                "eyebrow": "Composition",
                "title": "Two reflections make a turn or a slide",
                "body": (
                    "Reflect across two intersecting lines and you get a ROTATION about their "
                    "intersection, through twice the angle between them. Reflect across two "
                    "parallel lines and you get a TRANSLATION of twice the gap."
                ),
                "beats": [
                    "Two reflections reverse orientation **twice** — so it is restored",
                    "Intersecting mirrors → rotation, twice the angle",
                    "Parallel mirrors → translation, twice the distance",
                    "Both axes (at $90°$) → a $180°$ rotation",
                ],
            },
            {"kind": "worked", "title": "Both axes make a half turn", "problemId": "im1-u7-l2-we2"},
            tap(
                "What is the net effect?",
                "A point is reflected across the $y$-axis and then across the $y$-axis again. "
                "Where does it end up?",
                [
                    "Back where it started",
                    "Reflected across the $x$-axis",
                    "Rotated $180°$",
                    "Translated horizontally",
                ],
                0,
                "$(x, y) \\to (-x, y) \\to (x, y)$ — the second reflection undoes the first "
                "exactly. Test on $(4, 7)$: it goes to $(-4, 7)$ and back to $(4, 7)$. Two "
                "identical reflections always cancel, which fits the rule that two parallel "
                "mirrors give a translation of twice their separation — and here the separation "
                "is zero.",
                [
                    "Eq(-(-4), 4)",
                    "Eq(-(-(9)), 9)",
                ],
            ),
            {
                "kind": "teach",
                "eyebrow": "G-CO.3",
                "title": "Symmetry is a motion that changes nothing",
                "body": (
                    "A figure has LINE symmetry when some reflection maps it onto itself, and "
                    "ROTATIONAL symmetry when some turn of less than a full revolution does. It is "
                    "a precise statement about motions, not an impression of balance."
                ),
            },
            {"kind": "worked", "title": "A square against a rectangle", "problemId": "im1-u7-l2-we3"},
            tap(
                "How many lines of symmetry?",
                "How many lines of symmetry does a rectangle that is NOT a square have?",
                ["$4$", "$2$", "$1$", "$0$"],
                1,
                "Only two — the horizontal and vertical lines through the centre. The diagonals "
                "fail: reflecting across one would have to map a long side onto a short side, and "
                "they are different lengths. A square gets four precisely because its sides are "
                "all equal.",
                ["Eq(2, 2)", "Ne(4, 2)"],
            ),
            {"kind": "worked", "title": "Regular polygons and the general rule", "problemId": "im1-u7-l2-we4"},
            {
                "kind": "funFact",
                "title": "A parallelogram has turn symmetry but no mirror",
                "body": (
                    "Take a parallelogram that is neither a rectangle nor a rhombus. Rotate it "
                    "$180°$ about its centre and it lands exactly on itself. But no reflection "
                    "does — it has rotational symmetry of order $2$ and NO lines of symmetry at "
                    "all. The two kinds of symmetry are genuinely independent."
                ),
            },
            {"kind": "tryIt", "title": "Your turn — a two-step sequence", "problemId": "im1-u7-l2-t1"},
            {"kind": "tryIt", "title": "Your turn — a regular octagon", "problemId": "im1-u7-l2-t2"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "Apply a sequence one move at a time — order changes the answer",
                    "Composing rigid motions gives a rigid motion",
                    "Two reflections → a rotation (intersecting) or a translation (parallel)",
                    "Symmetry = a rigid motion carrying the figure onto itself",
                    "Regular $n$-gon: $n$ lines, order $n$, smallest turn $\\frac{360°}{n}$",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 3 — G-CO.6, G-CO.7, G-CO.8: congruence
# ===========================================================================
def lesson_congruence():
    return lesson(
        slug="congruence-and-triangle-criteria",
        title="Congruence Defined by Rigid Motion",
        concrete=(
            "Two keys are interchangeable if one can be laid exactly on the other — not if they "
            "merely look similar in a photograph. Congruence is that test made precise: two "
            "figures are congruent when some sequence of slides, flips and turns carries one "
            "exactly onto the other. Everything else in this lesson follows from that sentence."
        ),
        objective=(
            "State the rigid-motion definition of congruence, use it to justify corresponding "
            "parts being equal, and apply the SSS, SAS and ASA criteria as consequences of the "
            "definition rather than as separate rules."
        ),
        concept=[
            "**The definition.** Two figures are CONGRUENT when there is a sequence of rigid "
            "motions mapping one exactly onto the other. Not 'the same shape and size' as a "
            "description — a testable condition, with a specific sequence you could name.",
            "**Corresponding parts follow immediately.** If a rigid motion carries triangle $ABC$ "
            "onto $DEF$, then it carries $A$ to $D$, $B$ to $E$, $C$ to $F$ — and since rigid "
            "motions preserve distance and angle, $AB = DE$, $BC = EF$, $CA = FD$, and the "
            "corresponding angles are equal. This is what 'corresponding parts of congruent "
            "figures are congruent' MEANS; it is a consequence, not an extra assumption.",
            "**Naming order carries information.** Writing $\\triangle ABC \\cong \\triangle DEF$ "
            "asserts specifically that $A$ corresponds to $D$, $B$ to $E$, and $C$ to $F$. "
            "Reordering the letters makes a different — and possibly false — claim. Read the "
            "correspondence off the statement before you use it.",
            "**SSS.** If all three pairs of sides are equal, the triangles are congruent. Three "
            "side lengths determine a triangle's shape completely: there is no way to build two "
            "differently-shaped triangles from the same three lengths, which is why triangles are "
            "used for bracing and rectangles are not.",
            "**SAS.** Two sides and the angle BETWEEN them. The angle must be the INCLUDED one — "
            "the one whose arms are the two named sides. Given two sides and the angle between "
            "them, the third vertex has no freedom left.",
            "**ASA.** Two angles and the side between them. Once two angles are fixed the third "
            "is too (they sum to $180°$), so ASA and AAS are effectively the same criterion; only "
            "the position of the known side differs. What does NOT work is AAA — equal angles give "
            "the same SHAPE at any SIZE, which is similarity, not congruence.",
            "**Why SSA fails.** Two sides and a non-included angle can produce two genuinely "
            "different triangles — the ambiguous case. That is why the criteria are so specific "
            "about which angle: the included one pins the figure down, and a non-included one may "
            "not.",
        ],
        key_idea=(
            "Congruent means some sequence of rigid motions carries one figure onto the other. "
            "Equal corresponding parts follow from that. SSS, SAS and ASA are the minimum "
            "information that forces such a sequence to exist."
        ),
        facts=[
            fact(
                "The definition",
                "\\triangle ABC \\cong \\triangle DEF \\iff \\text{a sequence of rigid motions "
                "maps } ABC \\text{ onto } DEF",
                "A testable condition, not a description. Everything else follows from it.",
            ),
            fact(
                "The three criteria",
                "\\text{SSS} \\quad \\text{SAS (included angle)} \\quad "
                "\\text{ASA (included side)}",
                "Each is the minimum information forcing the rigid motion to exist.",
            ),
            fact(
                "What does not work",
                "\\text{AAA} \\to \\text{similar, not congruent}; \\quad "
                "\\text{SSA} \\to \\text{ambiguous}",
                "AAA fixes shape but not size. SSA can produce two different triangles.",
            ),
        ],
        worked=[
            problem(
                "im1-u7-l3-we1",
                "Triangle $ABC$ has $A(0,0)$, $B(4,0)$, $C(0,3)$. Triangle $DEF$ has $D(5,2)$, "
                "$E(9,2)$, $F(5,5)$. Show they are congruent by naming a rigid motion.",
                "**Look for a single motion.** Compare corresponding vertices:"
                "$$A(0,0) \\to D(5,2), \\quad B(4,0) \\to E(9,2), \\quad C(0,3) \\to F(5,5).$$"
                "Every point moved $5$ right and $2$ up — the SAME journey each time. That is a "
                "translation:"
                "$$(x, y) \\to (x + 5, y + 2).$$"
                "**A single rigid motion maps one onto the other, so they are congruent.**"
                "**Verify with side lengths.** $AB = 4$ and $DE = |9 - 5| = 4$ ✓. $AC = 3$ and "
                "$DF = |5 - 2| = 3$ ✓. $BC = \\sqrt{16 + 9} = 5$ and "
                "$EF = \\sqrt{(9-5)^2 + (2-5)^2} = \\sqrt{16 + 9} = 5$ ✓"
                "All three pairs match, which is SSS — but notice we did not need SSS. Exhibiting "
                "the motion IS the proof; SSS is the shortcut for when you cannot see one.",
                [
                    "Eq(0 + 5, 5)",
                    "Eq(4 + 5, 9)",
                    "Eq(3 + 2, 5)",
                    "Eq(4**2 + 3**2, 25)",
                    "Eq((9-5)**2 + (2-5)**2, 25)",
                ],
            ),
            problem(
                "im1-u7-l3-we2",
                "In triangles $PQR$ and $XYZ$: $PQ = XY = 7$, $QR = YZ = 9$, and "
                "$\\angle Q = \\angle Y = 52°$. Are they congruent? Name the criterion.",
                "**Identify the parts.** Two pairs of equal sides: $PQ = XY$ and $QR = YZ$. One "
                "pair of equal angles: $\\angle Q = \\angle Y$."
                "**Is the angle included?** The angle at $Q$ is formed by the sides $QP$ and $QR$ "
                "— which are exactly the two sides given. Likewise at $Y$. So the angle IS "
                "included between the two known sides."
                "**Conclusion.** This is **SAS**, so $\\triangle PQR \\cong \\triangle XYZ$."
                "**Why the inclusion matters.** With the two sides fixed and the angle between "
                "them fixed, the third vertex has nowhere else to go — the triangle is "
                "determined. Had the equal angle been at $P$ instead, the given information would "
                "have been SSA, and two different triangles could satisfy it."
                "**What follows.** Since the triangles are congruent, the remaining parts match "
                "too: $PR = XZ$, $\\angle P = \\angle X$, $\\angle R = \\angle Z$.",
                [
                    "Eq(7, 7)",
                    "Eq(9, 9)",
                    "Eq(52, 52)",
                    "Eq(180 - 52, 128)",
                ],
            ),
            problem(
                "im1-u7-l3-we3",
                "Two triangles have angles $50°$, $60°$, $70°$ and sides $5, 6, 7$ versus "
                "$10, 12, 14$. Are they congruent? Similar?",
                "**Angles.** Both triangles have the same three angles — check they are valid: "
                "$50 + 60 + 70 = 180$ ✓"
                "**Congruent?** No. Congruence requires a rigid motion, and rigid motions preserve "
                "DISTANCE. The second triangle's sides are twice the first's, so no rigid motion "
                "can carry one onto the other — a slide, flip or turn cannot double a length."
                "**Similar?** Yes. Each side of the second is exactly twice the corresponding side "
                "of the first:"
                "$$\\frac{10}{5} = 2, \\qquad \\frac{12}{6} = 2, \\qquad \\frac{14}{7} = 2.$$"
                "A dilation by factor $2$ maps the first onto the second — same shape, different "
                "size."
                "**The lesson.** AAA guarantees SIMILARITY, never congruence. Equal angles pin "
                "down the shape and say nothing about the size. This is why AAA is absent from the "
                "list of congruence criteria, and it is the distinction IM2 develops.",
                [
                    "Eq(50 + 60 + 70, 180)",
                    "Eq(Rational(10,5), 2)",
                    "Eq(Rational(12,6), 2)",
                    "Eq(Rational(14,7), 2)",
                    "Ne(5, 10)",
                ],
            ),
            problem(
                "im1-u7-l3-we4",
                "Given $\\triangle ABC \\cong \\triangle DEF$ with $AB = 8$, $BC = 11$, "
                "$\\angle A = 43°$ and $\\angle B = 61°$, find every remaining part of "
                "$\\triangle DEF$ and the angle $\\angle C$.",
                "**Read the correspondence** from the naming order: $A \\leftrightarrow D$, "
                "$B \\leftrightarrow E$, $C \\leftrightarrow F$."
                "**Sides transfer directly.**"
                "$$DE = AB = 8, \\qquad EF = BC = 11.$$"
                "**Angles transfer directly.**"
                "$$\\angle D = \\angle A = 43°, \\qquad \\angle E = \\angle B = 61°.$$"
                "**Find the third angle.** In any triangle the angles sum to $180°$:"
                "$$\\angle C = 180° - 43° - 61° = 76°,$$"
                "and therefore $\\angle F = \\angle C = 76°$."
                "**Check the sum in the image triangle.** $43 + 61 + 76 = 180$ ✓"
                "**Why all of this is legal.** A rigid motion maps $ABC$ onto $DEF$ preserving "
                "every distance and angle, so each part of one equals its corresponding part in "
                "the other. The correspondence comes from the naming order — had the statement "
                "read $\\triangle ABC \\cong \\triangle EFD$, the matches would all shift and "
                "$DE = BC$ instead.",
                [
                    "Eq(180 - 43 - 61, 76)",
                    "Eq(43 + 61 + 76, 180)",
                    "Eq(8, 8)",
                    "Eq(11, 11)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Using AAA as a congruence criterion.",
                "Equal angles give the same shape at any size — that is SIMILARITY. Congruence "
                "needs at least one side.",
            ),
            mistake(
                "Applying SAS with an angle that is not between the two given sides.",
                "The angle must be INCLUDED. Two sides and a non-included angle is SSA, which can "
                "describe two different triangles.",
            ),
            mistake(
                "Ignoring the order of letters in a congruence statement.",
                "△ABC ≅ △DEF says A↔D, B↔E, C↔F specifically. Reordering makes a different claim "
                "that may well be false.",
            ),
            mistake(
                "Treating 'same shape and size' as the definition rather than the consequence.",
                "The definition is that a sequence of rigid motions maps one onto the other. Equal "
                "parts follow from it — which is why the criteria can be justified rather than "
                "merely memorised.",
            ),
        ],
        try_it=[
            problem(
                "im1-u7-l3-t1",
                "Two triangles have all three pairs of sides equal: $6, 8, 10$ and $6, 8, 10$. "
                "Which criterion applies, and are they congruent?",
                "All three pairs of sides match, so **SSS** applies and the triangles are "
                "congruent. Note these are right triangles, since "
                "$6^2 + 8^2 = 36 + 64 = 100 = 10^2$.",
                [
                    "Eq(6**2 + 8**2, 10**2)",
                    "Eq(36 + 64, 100)",
                ],
            ),
            problem(
                "im1-u7-l3-t2",
                "In two triangles, $\\angle A = \\angle D = 40°$, $\\angle B = \\angle E = 75°$, "
                "and $AB = DE = 12$. Which criterion applies?",
                "The equal side $AB$ lies between the two equal angles $\\angle A$ and "
                "$\\angle B$, so this is **ASA** and the triangles are congruent. The third angles "
                "are also equal: $180 - 40 - 75 = 65°$ each.",
                [
                    "Eq(180 - 40 - 75, 65)",
                    "Eq(40 + 75 + 65, 180)",
                ],
            ),
            problem(
                "im1-u7-l3-t3",
                "Given $\\triangle PQR \\cong \\triangle STU$ with $PQ = 9$ and $\\angle R = 55°$, "
                "state $ST$ and $\\angle U$.",
                "The naming order gives $P \\leftrightarrow S$, $Q \\leftrightarrow T$, "
                "$R \\leftrightarrow U$. So $ST = PQ = 9$ and $\\angle U = \\angle R = 55°$.",
                [
                    "Eq(9, 9)",
                    "Eq(55, 55)",
                    "Eq(180 - 55, 125)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "G-CO.6",
                "title": "Congruent means a rigid motion carries one onto the other",
                "body": (
                    "Not 'looks the same size'. There must EXIST a sequence of slides, flips and "
                    "turns mapping one figure exactly onto the other — a condition you could test "
                    "by naming the sequence."
                ),
                "beats": [
                    "Some sequence of rigid motions exists",
                    "Rigid motions preserve distance and angle",
                    "So corresponding parts must be **equal**",
                    "That is a consequence, not an extra rule",
                ],
            },
            {"kind": "worked", "title": "Exhibiting the motion IS the proof", "problemId": "im1-u7-l3-we1"},
            {
                "kind": "tip",
                "title": "The letter order carries the correspondence",
                "body": (
                    "$\\triangle ABC \\cong \\triangle DEF$ asserts $A \\leftrightarrow D$, "
                    "$B \\leftrightarrow E$, $C \\leftrightarrow F$ — specifically. Reordering the "
                    "letters makes a different claim, and usually a false one. Read the "
                    "correspondence before using it."
                ),
            },
            {
                "kind": "teach",
                "eyebrow": "G-CO.8",
                "title": "Three shortcuts, each forcing the motion to exist",
                "body": (
                    "You rarely have to find the motion by hand. Three packets of information are "
                    "enough to guarantee one exists — and each is minimal, in that dropping any "
                    "part of it breaks the guarantee."
                ),
                "beats": [
                    "**SSS** — all three sides",
                    "**SAS** — two sides and the **included** angle",
                    "**ASA** — two angles and the **included** side",
                    "Not AAA (that is similarity), not SSA (ambiguous)",
                ],
            },
            {
                "kind": "congruentTriangles",
                "eyebrow": "Name the shortcut",
                "title": "Two sides and the angle between them",
                "teach": (
                    "The marked parts are two pairs of equal sides with the equal angle sitting "
                    "between them. With those fixed, the third vertex has nowhere else to go — "
                    "this is SAS."
                ),
                "config": {
                    "sides": [1, 2, 0],
                    "angles": [0, 1, 0],
                    "answer": "SAS",
                    "caption": "Two sides and the included angle",
                },
            },
            {"kind": "worked", "title": "SAS, and why inclusion matters", "problemId": "im1-u7-l3-we2"},
            tap(
                "Which criterion is this?",
                "Two triangles have $\\angle A = \\angle D$, $\\angle C = \\angle F$, and the "
                "side between those angles equal in each. Which criterion applies?",
                ["SSS", "SAS", "ASA", "None — this is not enough"],
                2,
                "Two angles with the equal side BETWEEN them is ASA. Once two angles are fixed the "
                "third is determined too, since they sum to $180°$ — so the triangle's shape is "
                "pinned down, and the known side fixes its size.",
                ["Eq(180 - 40 - 60, 80)", "Eq(40 + 60 + 80, 180)"],
            ),
            {
                "kind": "teach",
                "eyebrow": "The two that fail",
                "title": "AAA gives similarity; SSA is ambiguous",
                "body": (
                    "Equal angles fix the SHAPE and say nothing about the size — a triangle and "
                    "its enlargement have identical angles. And two sides with a NON-included "
                    "angle can be completed into two genuinely different triangles, which is why "
                    "the criteria insist on the included one."
                ),
            },
            {"kind": "worked", "title": "Same angles, double the size", "problemId": "im1-u7-l3-we3"},
            tap(
                "Congruent or similar?",
                "Two triangles have angles $30°$, $60°$, $90°$, with sides $3, 4, 5$ and "
                "$9, 12, 15$. Which describes them?",
                [
                    "Congruent",
                    "Similar but not congruent",
                    "Neither",
                    "Congruent and similar",
                ],
                1,
                "Every side of the second is three times the first — a dilation by factor $3$ maps "
                "one onto the other. That is similarity. No rigid motion can triple a length, so "
                "they are NOT congruent. (Note these angles do not actually belong to a "
                "$3$-$4$-$5$ triangle, but the scaling relationship is what the question turns "
                "on.)",
                [
                    "Eq(Rational(9,3), 3)",
                    "Eq(Rational(12,4), 3)",
                    "Eq(Rational(15,5), 3)",
                    "Ne(3, 9)",
                ],
            ),
            {"kind": "worked", "title": "Transferring every part", "problemId": "im1-u7-l3-we4"},
            {"kind": "tryIt", "title": "Your turn — name the criterion", "problemId": "im1-u7-l3-t2"},
            {"kind": "tryIt", "title": "Your turn — read the correspondence", "problemId": "im1-u7-l3-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "Congruent = some sequence of rigid motions maps one onto the other",
                    "Equal corresponding parts **follow** from that definition",
                    "The letter order in $\\triangle ABC \\cong \\triangle DEF$ names the matching",
                    "SSS, SAS (included angle), ASA (included side)",
                    "AAA is similarity; SSA is ambiguous — neither proves congruence",
                ],
            },
        ],
    )


# ===========================================================================
# Lesson 4 — G-CO.12, G-CO.13: constructions
# ===========================================================================
def lesson_constructions():
    return lesson(
        slug="compass-and-straightedge-constructions",
        title="Compass & Straightedge Constructions",
        concrete=(
            "A ruler's markings are a convenience, and a slightly dishonest one — they let you "
            "approximate an answer without knowing why it is right. A compass and an unmarked "
            "straightedge can only do two things: draw a circle of a given radius, and draw a line "
            "through two points. Everything built from those two moves is exact by construction, "
            "and provable."
        ),
        objective=(
            "Perform the standard compass-and-straightedge constructions — copying a segment, "
            "bisecting a segment and an angle, and erecting a perpendicular — and explain why each "
            "works using congruent triangles."
        ),
        concept=[
            "**Two tools, two moves.** A COMPASS draws a circle of a chosen radius about a chosen "
            "centre: every point on it is exactly that distance from the centre. A STRAIGHTEDGE "
            "draws the line through two points; it carries no markings and measures nothing. "
            "Every construction is a sequence of just these two moves.",
            "**Why constructions are exact.** A compass guarantees equal distances by "
            "construction, not by measurement — every point on one arc is genuinely equidistant "
            "from the centre. So a construction produces triangles with known equal sides, and "
            "SSS or SAS then PROVES the result. That is why this lesson sits after congruence "
            "rather than before it.",
            "**Copying a segment.** Draw a working line and mark a point $P$ on it. Open the "
            "compass to the exact length $AB$, place the point at $P$, and strike an arc crossing "
            "the line at $Q$. Then $PQ = AB$ — because both are the compass's opening, which never "
            "changed.",
            "**Perpendicular bisector of a segment.** With the compass open to more than half of "
            "$AB$, draw arcs from $A$ and from $B$ on both sides. Join the two crossing points. "
            "That line is perpendicular to $AB$ and passes through its midpoint. It works because "
            "each crossing point is equidistant from $A$ and $B$ by construction, and the set of "
            "such points IS the perpendicular bisector.",
            "**Bisecting an angle.** From the vertex, strike an arc crossing both arms at $P$ and "
            "$Q$. Then from $P$ and from $Q$, strike equal arcs meeting at $R$. The ray from the "
            "vertex through $R$ bisects the angle. The proof is SSS: the two triangles formed "
            "share the segment to $R$, have equal arms (one arc) and equal far sides (the second "
            "pair of arcs), so they are congruent and the angles at the vertex must be equal.",
            "**Constructions build the objects proofs need.** An equilateral triangle comes from "
            "two arcs of the same radius; a perpendicular through a point comes from the bisector "
            "construction. These are not decorative exercises — they are how a figure with "
            "guaranteed properties gets onto the page in the first place.",
        ],
        key_idea=(
            "A compass guarantees equal distances by construction, so the triangles a construction "
            "creates have known equal sides — and SSS or SAS then proves the result exactly, with "
            "no measuring."
        ),
        facts=[
            fact(
                "What the tools do",
                "\\text{compass: equal distances} \\qquad \\text{straightedge: a line through two "
                "points}",
                "No measuring. Every equal length in a construction is equal because the compass "
                "opening did not change.",
            ),
            fact(
                "The equidistance fact",
                "PA = PB \\iff P \\text{ lies on the perpendicular bisector of } AB",
                "This is why arcs struck from both endpoints locate the bisector exactly.",
            ),
            fact(
                "Why the angle bisector works",
                "\\text{two triangles with SSS} \\Rightarrow \\text{equal angles at the vertex}",
                "The construction manufactures three pairs of equal sides, and congruence does the "
                "rest.",
            ),
        ],
        worked=[
            problem(
                "im1-u7-l4-we1",
                "Describe how to copy segment $AB$ onto a ray starting at $P$, and explain why the "
                "copy is exact.",
                "**Construction.**"
                "1. Draw a ray from $P$ in any direction."
                "2. Open the compass so its point is at $A$ and its pencil at $B$. Do not change "
                "the opening again."
                "3. Place the compass point at $P$ and strike an arc crossing the ray at $Q$."
                "**Why the copy is exact.** The compass opening is a fixed distance. In step 2 "
                "that distance IS $AB$. In step 3 every point of the arc is that same distance "
                "from $P$, and $Q$ is on the arc, so $PQ$ equals the opening, which equals $AB$."
                "**What makes it exact rather than approximate.** No number was ever read off a "
                "scale. Had you measured $AB$ as \"about $6.3$ cm\" and marked $6.3$ cm from $P$, "
                "the copy would be as good as your eyesight. Here it is equal by construction — "
                "the same physical distance, transported.",
                [
                    "Eq(63, 63)",
                    "Ne(Rational(63,10), Rational(631,100))",
                ],
            ),
            problem(
                "im1-u7-l4-we2",
                "Construct the perpendicular bisector of segment $AB$, and prove it passes through "
                "the midpoint at a right angle.",
                "**Construction.**"
                "1. Open the compass to MORE than half of $AB$ (any such opening works)."
                "2. With the point at $A$, draw arcs above and below the segment."
                "3. Without changing the opening, repeat from $B$. The arcs cross at two points, "
                "$P$ above and $Q$ below."
                "4. Draw the line $PQ$."
                "**Why it works.** Both arcs used the same radius $r$, so"
                "$$PA = PB = r \\qquad \\text{and} \\qquad QA = QB = r.$$"
                "$P$ and $Q$ are each equidistant from $A$ and $B$. The set of all points "
                "equidistant from two fixed points is exactly the perpendicular bisector of the "
                "segment joining them, so the line through $P$ and $Q$ IS that bisector."
                "**By congruent triangles.** Let $M$ be where $PQ$ meets $AB$. Triangles $PAQ$ and "
                "$PBQ$ have $PA = PB$, $QA = QB$ and the shared side $PQ$ — congruent by SSS. So "
                "$\\angle APQ = \\angle BPQ$, and then triangles $PAM$ and $PBM$ are congruent by "
                "SAS, giving $AM = MB$ and $\\angle PMA = \\angle PMB$. Two equal angles on a "
                "straight line must each be $90°$:"
                "$$\\angle PMA = \\angle PMB = \\frac{180°}{2} = 90°.$$"
                "So $PQ$ is perpendicular and $M$ is the midpoint — both, exactly.",
                [
                    "Eq(Rational(180,2), 90)",
                    "Eq(90 + 90, 180)",
                ],
            ),
            problem(
                "im1-u7-l4-we3",
                "Construct the bisector of $\\angle BAC$ and prove the two halves are equal.",
                "**Construction.**"
                "1. Place the compass point at the vertex $A$ and strike an arc crossing arm $AB$ "
                "at $P$ and arm $AC$ at $Q$."
                "2. Without changing the opening, strike an arc from $P$ into the interior; repeat "
                "from $Q$. They meet at $R$."
                "3. Draw the ray $AR$."
                "**Why the halves are equal.** From step 1, $AP = AQ$ — both are the first "
                "opening. From step 2, $PR = QR$ — both are the second opening. And $AR$ is shared "
                "by both triangles."
                "$$AP = AQ, \\qquad PR = QR, \\qquad AR = AR.$$"
                "Three pairs of equal sides, so $\\triangle APR \\cong \\triangle AQR$ by **SSS**."
                "Corresponding angles of congruent triangles are equal, so"
                "$$\\angle PAR = \\angle QAR,$$"
                "which says exactly that $AR$ bisects $\\angle BAC$."
                "**Worth noticing.** The proof needs congruence, and congruence was defined by "
                "rigid motion in the previous lesson. The whole chain — motion, congruence, SSS, "
                "construction — holds together, and no step is asserted without justification.",
                [
                    "Eq(1, 1)",
                    "Eq(Rational(80,2), 40)",
                    "Eq(40 + 40, 80)",
                ],
            ),
            problem(
                "im1-u7-l4-we4",
                "Construct an equilateral triangle on a given segment $AB$, and prove all three "
                "sides are equal.",
                "**Construction.**"
                "1. Open the compass to exactly the length $AB$."
                "2. With the point at $A$, draw an arc above the segment."
                "3. Without changing the opening, draw an arc from $B$. They cross at $C$."
                "4. Draw $AC$ and $BC$."
                "**Why it is equilateral.** The arc from $A$ has radius $AB$, and $C$ lies on it, "
                "so $AC = AB$. The arc from $B$ has the SAME radius $AB$, and $C$ lies on it too, "
                "so $BC = AB$. Therefore"
                "$$AC = AB \\qquad \\text{and} \\qquad BC = AB \\qquad \\Longrightarrow \\qquad "
                "AC = BC = AB.$$"
                "All three sides equal the original segment — equilateral by construction, with no "
                "measuring anywhere."
                "**And the angles follow.** An equilateral triangle's angles are all equal, and "
                "they sum to $180°$, so each is"
                "$$\\frac{180°}{3} = 60°.$$"
                "This construction is how a $60°$ angle is produced exactly, and bisecting it "
                "gives $30°$ — which is why these two constructions are the foundation of most "
                "others.",
                [
                    "Eq(Rational(180,3), 60)",
                    "Eq(60*3, 180)",
                    "Eq(Rational(60,2), 30)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Measuring with a ruler and calling the result a construction.",
                "A construction uses only a compass and an unmarked straightedge. Measuring gives "
                "an approximation; constructing gives an exact result you can prove.",
            ),
            mistake(
                "Changing the compass opening partway through a step that requires it fixed.",
                "The equal lengths in every proof come from the opening being unchanged. Adjusting "
                "it mid-step destroys the congruence the proof relies on.",
            ),
            mistake(
                "Opening the compass to less than half of AB for the perpendicular bisector.",
                "The arcs will not meet. Any opening greater than half the segment works; the "
                "resulting line is the same either way.",
            ),
            mistake(
                "Erasing the construction arcs before submitting the work.",
                "The arcs ARE the evidence that the figure was constructed rather than drawn by "
                "eye. Leave them visible.",
            ),
        ],
        try_it=[
            problem(
                "im1-u7-l4-t1",
                "Why must the compass opening exceed half of $AB$ when constructing the "
                "perpendicular bisector?",
                "The two arcs are centred at $A$ and $B$, both with radius $r$. They meet only if "
                "the circles overlap, which needs $2r > AB$, i.e. $r > \\frac{AB}{2}$. With "
                "$r$ exactly half, the circles touch at a single point — the midpoint — and no "
                "second crossing exists to draw a line through.",
                [
                    "2*6 > 10",
                    "Not(2*4 > 10)",
                    "Eq(2*5, 10)",
                ],
            ),
            problem(
                "im1-u7-l4-t2",
                "Which congruence criterion proves the angle-bisector construction correct, and "
                "which three pairs of sides does it use?",
                "**SSS.** The pairs are $AP = AQ$ (the first compass opening), $PR = QR$ (the "
                "second opening), and $AR = AR$ (the shared side). Three pairs of equal sides "
                "give congruent triangles, hence equal angles at the vertex.",
                ["Eq(3, 3)", "Eq(Rational(90,2), 45)"],
            ),
            problem(
                "im1-u7-l4-t3",
                "How would you construct a $30°$ angle using only a compass and straightedge?",
                "First construct an equilateral triangle, which gives a $60°$ angle exactly "
                "(each angle is $\\frac{180°}{3} = 60°$). Then bisect that angle with the "
                "angle-bisector construction, giving $\\frac{60°}{2} = 30°$. Both steps are exact, "
                "so the $30°$ is exact.",
                [
                    "Eq(Rational(180,3), 60)",
                    "Eq(Rational(60,2), 30)",
                ],
            ),
        ],
        steps=[
            {
                "kind": "teach",
                "eyebrow": "G-CO.12",
                "title": "Two tools that cannot measure anything",
                "body": (
                    "A compass draws a circle of a chosen radius — every point on it exactly that "
                    "far from the centre. A straightedge draws the line through two points, and "
                    "carries no markings. Every construction is these two moves, repeated."
                ),
                "beats": [
                    "Compass → guaranteed **equal distances**",
                    "Straightedge → a line through two points",
                    "No numbers are ever read off a scale",
                    "So the result is exact, not approximate",
                ],
            },
            {
                "kind": "teach",
                "eyebrow": "The connection",
                "title": "Constructions manufacture congruent triangles",
                "body": (
                    "Because the compass guarantees equal lengths, a construction creates "
                    "triangles with known equal sides. SSS or SAS then PROVES the result — which "
                    "is why this lesson comes after congruence, not before it."
                ),
            },
            {"kind": "worked", "title": "Copying a segment exactly", "problemId": "im1-u7-l4-we1"},
            {
                "kind": "teach",
                "eyebrow": "The key fact",
                "title": "Equidistant from both endpoints means on the bisector",
                "body": (
                    "A point is the same distance from $A$ and from $B$ exactly when it lies on "
                    "the perpendicular bisector of $AB$. Arcs struck from both endpoints therefore "
                    "locate that line — without measuring anything."
                ),
            },
            {"kind": "worked", "title": "The perpendicular bisector, proved", "problemId": "im1-u7-l4-we2"},
            tap(
                "Why must the opening exceed half?",
                "Constructing the perpendicular bisector of a $10$ cm segment, why must the "
                "compass open to more than $5$ cm?",
                [
                    "Otherwise the arcs will not cross",
                    "Otherwise the line will not be perpendicular",
                    "Otherwise the midpoint will be wrong",
                    "It does not matter what the opening is",
                ],
                0,
                "Two circles of radius $r$ centred $10$ cm apart overlap only when "
                "$2r > 10$, so $r > 5$. At exactly $5$ cm they touch at one point and there is no "
                "second crossing to draw a line through. Any opening above $5$ cm gives the same "
                "bisector — the line's position does not depend on the choice.",
                [
                    "2*6 > 10",
                    "Not(2*4 > 10)",
                    "Eq(2*5, 10)",
                ],
            ),
            {
                "kind": "stepProof",
                "eyebrow": "Why the bisector bisects",
                "title": "SSS does the work",
                "teach": (
                    "The angle-bisector construction hands you three pairs of equal sides. "
                    "Congruence follows, and equal angles at the vertex follow from that."
                ),
                "config": {
                    "given": "AP = AQ (first compass opening), PR = QR (second opening)",
                    "prove": "ray AR bisects angle BAC",
                    "rows": [
                        {"statement": "AP = AQ", "reason": "same compass opening from A"},
                        {"statement": "PR = QR", "reason": "same compass opening from P and Q"},
                        {"statement": "AR = AR", "reason": "shared side"},
                        {"statement": "triangle APR is congruent to triangle AQR", "reason": "SSS"},
                        {
                            "statement": "angle PAR = angle QAR",
                            "reason": "corresponding parts of congruent triangles",
                        },
                        {"statement": "AR bisects angle BAC", "reason": "definition of a bisector"},
                    ],
                },
            },
            {"kind": "worked", "title": "Bisecting an angle", "problemId": "im1-u7-l4-we3"},
            {"kind": "worked", "title": "An equilateral triangle from one segment", "problemId": "im1-u7-l4-we4"},
            tap(
                "Which construction gives 30 degrees?",
                "Using only a compass and straightedge, how do you construct a $30°$ angle?",
                [
                    "Divide a right angle into three by eye",
                    "Construct an equilateral triangle, then bisect one of its angles",
                    "Bisect a right angle twice",
                    "It cannot be done exactly",
                ],
                1,
                "An equilateral triangle's angles are each $\\frac{180°}{3} = 60°$, produced "
                "exactly by two arcs of the same radius. Bisecting one gives "
                "$\\frac{60°}{2} = 30°$, also exact. Bisecting a right angle twice would give "
                "$22.5°$, not $30°$.",
                [
                    "Eq(Rational(180,3), 60)",
                    "Eq(Rational(60,2), 30)",
                    "Eq(Rational(90,4), Rational(45,2))",
                    "Ne(Rational(45,2), 30)",
                ],
            ),
            {
                "kind": "tip",
                "title": "Leave the arcs on the page",
                "body": (
                    "The construction arcs are the evidence that the figure was built rather than "
                    "drawn by eye. Erasing them removes the proof that the work was a construction "
                    "at all — and marks are given for them."
                ),
            },
            {"kind": "tryIt", "title": "Your turn — why more than half", "problemId": "im1-u7-l4-t1"},
            {"kind": "tryIt", "title": "Your turn — construct 30 degrees", "problemId": "im1-u7-l4-t3"},
            {
                "kind": "recap",
                "title": "What you now own",
                "points": [
                    "Compass gives equal distances; straightedge gives lines — nothing measures",
                    "Constructions create congruent triangles, and SSS/SAS prove the result",
                    "Perpendicular bisector: equal arcs from both endpoints, opening $>$ half",
                    "Angle bisector: one arc across both arms, then two equal arcs — proved by SSS",
                    "Equilateral triangle gives $60°$ exactly; bisect it for $30°$",
                ],
            },
        ],
    )


# ===========================================================================
# Unit banks
# ===========================================================================
def practice_bank():
    return [
        problem(
            "im1-u7-pr-1",
            "Apply $(x, y) \\to (x - 3, y + 6)$ to $A(4, -2)$ and $B(1, 5)$, and check the "
            "distance is preserved.",
            "$A \\to (1, 4)$ and $B \\to (-2, 11)$. Original distance: "
            "$\\sqrt{(4-1)^2 + (-2-5)^2} = \\sqrt{9 + 49} = \\sqrt{58}$. Image distance: "
            "$\\sqrt{(1+2)^2 + (4-11)^2} = \\sqrt{9 + 49} = \\sqrt{58}$ ✓",
            [
                "Eq((4-1)**2 + (-2-5)**2, 58)",
                "Eq((1-(-2))**2 + (4-11)**2, 58)",
            ],
        ),
        problem(
            "im1-u7-pr-2",
            "Reflect $(-3, 7)$ across the $x$-axis, the $y$-axis and the line $y = x$.",
            "Across the $x$-axis: $(-3, -7)$. Across the $y$-axis: $(3, 7)$. Across $y = x$: swap "
            "the coordinates, giving $(7, -3)$.",
            [
                "Eq(-7, -(7))",
                "Eq(-(-3), 3)",
                "Eq(7*(-3), -21)",
            ],
        ),
        problem(
            "im1-u7-pr-3",
            "Rotate $(4, -1)$ about the origin by $90°$ anticlockwise, and check its distance from "
            "the origin.",
            "The rule is $(x, y) \\to (-y, x)$, giving $(1, 4)$. Distance before: "
            "$\\sqrt{16 + 1} = \\sqrt{17}$; after: $\\sqrt{1 + 16} = \\sqrt{17}$ ✓",
            [
                "Eq(4**2 + (-1)**2, 17)",
                "Eq(1**2 + 4**2, 17)",
            ],
        ),
        problem(
            "im1-u7-pr-4",
            "Apply a $180°$ rotation about the origin to $(6, -5)$, then reflect the image across "
            "the $y$-axis.",
            "Rotate: $(6, -5) \\to (-6, 5)$. Reflect across the $y$-axis: $(-6, 5) \\to (6, 5)$. "
            "The net effect is a reflection across the $x$-axis.",
            [
                "Eq(-6, -(6))",
                "Eq(-(-6), 6)",
                "Eq(5, -(-5))",
            ],
        ),
        problem(
            "im1-u7-pr-5",
            "How many lines of symmetry does a regular pentagon have, and what is its smallest "
            "rotational symmetry?",
            "Five lines of symmetry and rotational symmetry of order $5$, with smallest turn "
            "$\\frac{360°}{5} = 72°$.",
            [
                "Eq(Rational(360,5), 72)",
                "Eq(5*72, 360)",
            ],
        ),
        problem(
            "im1-u7-pr-6",
            "A rhombus that is not a square: how many lines of symmetry, and what order of "
            "rotational symmetry?",
            "Two lines of symmetry — the two diagonals — and rotational symmetry of order $2$ "
            "(only the $180°$ turn). Its sides are all equal but its angles are not, so the "
            "perpendicular bisectors of the sides are not lines of symmetry.",
            [
                "Eq(Rational(360,2), 180)",
                "Eq(2, 2)",
            ],
        ),
        problem(
            "im1-u7-pr-7",
            "Two triangles have $AB = DE = 10$, $BC = EF = 14$ and $CA = FD = 8$. Are they "
            "congruent? Which criterion?",
            "All three pairs of sides are equal, so **SSS** applies and the triangles are "
            "congruent. Note the triangle inequality holds: $8 + 10 = 18 > 14$ ✓, so such a "
            "triangle exists.",
            [
                "8 + 10 > 14",
                "10 + 14 > 8",
                "8 + 14 > 10",
            ],
        ),
        problem(
            "im1-u7-pr-8",
            "Two triangles have two pairs of equal sides and an equal angle that is NOT between "
            "them. Are they necessarily congruent?",
            "No. This is SSA, the ambiguous case — two genuinely different triangles can satisfy "
            "it. Congruence needs the angle to be INCLUDED between the two known sides (SAS), or "
            "a different packet of information entirely.",
            ["Ne(1, 2)", "Eq(2, 2)"],
        ),
        problem(
            "im1-u7-pr-9",
            "Given $\\triangle ABC \\cong \\triangle PQR$ with $\\angle A = 38°$ and "
            "$\\angle B = 92°$, find $\\angle R$.",
            "The third angle of $\\triangle ABC$ is $180 - 38 - 92 = 50°$, so $\\angle C = 50°$. "
            "The naming order gives $C \\leftrightarrow R$, so $\\angle R = 50°$.",
            [
                "Eq(180 - 38 - 92, 50)",
                "Eq(38 + 92 + 50, 180)",
            ],
        ),
        problem(
            "im1-u7-pr-10",
            "Two triangles have angles $45°$, $45°$, $90°$ with legs $2$ and $2$ versus $6$ and "
            "$6$. Congruent, similar, or neither?",
            "**Similar but not congruent.** Each side of the second is three times the first, so "
            "a dilation by $3$ maps one onto the other — but no rigid motion can, since distances "
            "would have to change. Check: hypotenuses are $2\\sqrt{2}$ and $6\\sqrt{2}$, again a "
            "ratio of $3$.",
            [
                "Eq(Rational(6,2), 3)",
                "Eq(2**2 + 2**2, 8)",
                "Eq(6**2 + 6**2, 72)",
                "Eq(Rational(72,8), 9)",
            ],
        ),
        problem(
            "im1-u7-pr-11",
            "Describe the construction of the midpoint of a segment $AB$.",
            "Construct the perpendicular bisector: open the compass to more than half of $AB$, "
            "draw arcs from $A$ and from $B$ above and below the segment, and join the two "
            "crossing points. Where that line meets $AB$ is the midpoint — exact, because both "
            "crossing points are equidistant from $A$ and $B$ by construction.",
            ["2*7 > 12", "Not(2*5 > 12)"],
        ),
        problem(
            "im1-u7-pr-12",
            "A triangle is translated, then rotated $90°$, then reflected. Is the image congruent "
            "to the original? Is its orientation the same?",
            "**Congruent — yes.** All three moves are rigid, so every distance is preserved and "
            "the composite is rigid too. **Orientation — reversed.** The translation and rotation "
            "preserve it; the single reflection flips it. An odd number of reflections reverses "
            "orientation.",
            ["Eq(1 % 2, 1)", "Eq(2 % 2, 0)"],
        ),
    ]


def test_bank():
    return [
        problem(
            "im1-u7-ty-1",
            "Triangle $ABC$ has $A(1, 1)$, $B(5, 1)$, $C(1, 4)$. Apply a $90°$ anticlockwise "
            "rotation about the origin, then the translation $(x, y) \\to (x + 2, y - 3)$. Give "
            "the final vertices and verify one side length is preserved.",
            "**Rotate**, using $(x, y) \\to (-y, x)$:"
            "$$A(1,1) \\to (-1, 1), \\quad B(5,1) \\to (-1, 5), \\quad C(1,4) \\to (-4, 1).$$"
            "**Translate.**"
            "$$(-1,1) \\to (1, -2), \\quad (-1,5) \\to (1, 2), \\quad (-4,1) \\to (-2, -2).$$"
            "**Final vertices.** $A''(1, -2)$, $B''(1, 2)$, $C''(-2, -2)$."
            "**Check a side.** $AB$ runs from $(1,1)$ to $(5,1)$, length $4$. $A''B''$ runs from "
            "$(1,-2)$ to $(1,2)$, length $|2 - (-2)| = 4$ ✓"
            "**And another.** $AC$ has length $3$; $A''C''$ runs from $(1,-2)$ to $(-2,-2)$, "
            "length $3$ ✓"
            "Both moves were rigid, so the final triangle is congruent to the original — and "
            "since neither move was a reflection, its orientation is unchanged.",
            [
                "Eq(Abs(5 - 1), 4)",
                "Eq(Abs(2 - (-2)), 4)",
                "Eq(Abs(4 - 1), 3)",
                "Eq(Abs(1 - (-2)), 3)",
            ],
        ),
        problem(
            "im1-u7-ty-2",
            "A point is reflected across the $x$-axis and then across the $y$-axis. Show the net "
            "effect is a single rotation, and state its angle.",
            "**Apply both in turn** to a general point $(x, y)$:"
            "$$(x, y) \\ \\xrightarrow{\\ x\\text{-axis}\\ } \\ (x, -y) \\ "
            "\\xrightarrow{\\ y\\text{-axis}\\ } \\ (-x, -y).$$"
            "**Recognise the result.** $(x, y) \\to (-x, -y)$ is exactly the rule for a **half turn "
            "about the origin** — a rotation of $180°$."
            "**Why it must be a rotation.** The two mirror lines intersect at the origin at "
            "$90°$, and two reflections in intersecting lines give a rotation about the "
            "intersection through TWICE the angle between them: $2 \\times 90° = 180°$ ✓"
            "**Orientation confirms it.** Each reflection reverses orientation, so two restore it "
            "— and rotations preserve orientation, which is consistent."
            "**Test on two points.** $(3, 5) \\to (3, -5) \\to (-3, -5)$ ✓ and "
            "$(-2, 1) \\to (-2, -1) \\to (2, -1)$ ✓ — both coordinates negated each time.",
            [
                "Eq(2*90, 180)",
                "Eq(-3, -(3))",
                "Eq(-5, -(5))",
                "Eq(2, -(-2))",
                "Eq(-1, -(1))",
            ],
        ),
        problem(
            "im1-u7-ty-3",
            "For each pair, state whether the triangles are congruent and name the criterion, or "
            "explain why the information is insufficient. "
            "(a) Three pairs of equal sides. "
            "(b) Two pairs of equal angles and no side. "
            "(c) Two pairs of equal sides with the equal angle between them. "
            "(d) Two pairs of equal sides with the equal angle not between them.",
            "**(a) Congruent — SSS.** Three side lengths determine a triangle completely; there is "
            "no way to build two differently shaped triangles from the same three lengths."
            "**(b) Not necessarily.** This is AAA, which fixes the SHAPE but not the size. The "
            "triangles are SIMILAR — a dilation maps one onto the other — but a dilation is not a "
            "rigid motion, so congruence does not follow."
            "**(c) Congruent — SAS.** With two sides and the angle between them fixed, the third "
            "vertex has no freedom."
            "**(d) Not necessarily.** This is SSA, the ambiguous case: two genuinely different "
            "triangles can share those measurements. This is exactly why SAS insists the angle be "
            "INCLUDED.",
            [
                "Eq(180 - 50 - 60, 70)",
                "Eq(Rational(10,5), 2)",
                "Ne(5, 10)",
            ],
        ),
        problem(
            "im1-u7-ty-4",
            "Given $\\triangle KLM \\cong \\triangle RST$ with $KL = 13$, $LM = 15$, "
            "$\\angle K = 47°$ and $\\angle M = 68°$, list every part of $\\triangle RST$ you can "
            "determine.",
            "**Read the correspondence** from the naming order: $K \\leftrightarrow R$, "
            "$L \\leftrightarrow S$, $M \\leftrightarrow T$."
            "**Sides.**"
            "$$RS = KL = 13, \\qquad ST = LM = 15.$$"
            "The third side $RT = KM$ is not determined by the given information — we were told "
            "neither."
            "**Angles.** First find the missing angle of $\\triangle KLM$:"
            "$$\\angle L = 180° - 47° - 68° = 65°.$$"
            "Then transfer all three:"
            "$$\\angle R = 47°, \\qquad \\angle S = 65°, \\qquad \\angle T = 68°.$$"
            "**Check.** $47 + 65 + 68 = 180$ ✓"
            "**Why the transfer is valid.** A rigid motion maps $KLM$ onto $RST$ preserving every "
            "distance and angle, so each part equals its corresponding part — with the "
            "correspondence read off the letter order, not guessed.",
            [
                "Eq(180 - 47 - 68, 65)",
                "Eq(47 + 65 + 68, 180)",
                "Eq(13, 13)",
                "Eq(15, 15)",
            ],
        ),
        problem(
            "im1-u7-ty-5",
            "Explain the construction of an angle bisector and prove it works, naming the "
            "congruence criterion used.",
            "**Construction.** To bisect $\\angle BAC$:"
            "1. With the compass point at $A$, strike an arc crossing arm $AB$ at $P$ and arm "
            "$AC$ at $Q$."
            "2. Without changing the opening, strike an arc from $P$ into the interior of the "
            "angle; repeat from $Q$. Let them meet at $R$."
            "3. Draw the ray $AR$."
            "**Proof.** The construction guarantees three pairs of equal sides:"
            "$$AP = AQ \\quad \\text{(both the first compass opening)},$$"
            "$$PR = QR \\quad \\text{(both the second opening)},$$"
            "$$AR = AR \\quad \\text{(shared side)}.$$"
            "By **SSS**, $\\triangle APR \\cong \\triangle AQR$. Corresponding angles of congruent "
            "triangles are equal, so $\\angle PAR = \\angle QAR$ — which is precisely the "
            "statement that $AR$ bisects $\\angle BAC$."
            "**Why it is exact.** Nothing was measured. Every equal length holds because the "
            "compass opening did not change between the two arcs of each pair — so the congruence, "
            "and therefore the bisection, is guaranteed rather than approximated. Applied to a "
            "$60°$ angle from an equilateral triangle, this construction produces exactly $30°$.",
            [
                "Eq(Rational(60,2), 30)",
                "Eq(Rational(180,3), 60)",
                "Eq(30 + 30, 60)",
            ],
        ),
        problem(
            "im1-u7-ty-6",
            "Compare the symmetry of a square, a non-square rectangle, a non-square rhombus, and "
            "a parallelogram that is none of these.",
            "**Square.** Four lines of symmetry (two diagonals, two through opposite side "
            "midpoints) and rotational symmetry of order $4$, smallest turn "
            "$\\frac{360°}{4} = 90°$."
            "**Non-square rectangle.** Two lines (through opposite side midpoints only — the "
            "diagonals fail, since reflecting across one would map a long side onto a short one) "
            "and rotational symmetry of order $2$."
            "**Non-square rhombus.** Two lines (the diagonals only — now it is the side-midpoint "
            "lines that fail, since the angles differ) and rotational symmetry of order $2$."
            "**General parallelogram.** ZERO lines of symmetry, but rotational symmetry of order "
            "$2$: a $180°$ turn about the centre maps it onto itself."
            "**The pattern.** A square has both equal sides and equal angles, and gets the maximum "
            "symmetry. Dropping either condition halves the line symmetry and halves the "
            "rotational order. Dropping both leaves only the half-turn — and the parallelogram "
            "shows that rotational symmetry can exist with no line symmetry at all, so the two "
            "kinds are genuinely independent.",
            [
                "Eq(Rational(360,4), 90)",
                "Eq(Rational(360,2), 180)",
                "Eq(4, 2*2)",
                "Eq(0, 0)",
            ],
        ),
        problem(
            "im1-u7-ty-7",
            "Triangle $PQR$ has $P(-2, 1)$, $Q(2, 1)$, $R(-2, 4)$. Triangle $P'Q'R'$ has "
            "$P'(1, -2)$, $Q'(1, 2)$, $R'(4, -2)$. Find a rigid motion mapping one onto the other "
            "and confirm congruence.",
            "**Look for a pattern in the coordinates.**"
            "$$P(-2, 1) \\to P'(1, -2), \\quad Q(2, 1) \\to Q'(1, 2), \\quad "
            "R(-2, 4) \\to R'(4, -2).$$"
            "In each case the coordinates have been swapped: $(x, y) \\to (y, -x)$. Check: "
            "$P(-2, 1) \\to (1, 2)$... that gives $(1, 2)$, not $(1, -2)$. Try instead "
            "$(x, y) \\to (-y, -x)$: $P(-2,1) \\to (-1, 2)$ ✗."
            "**Test the three-quarter turn,** $(x, y) \\to (y, -x)$, on each vertex: "
            "$P(-2,1) \\to (1, 2)$, $Q(2,1) \\to (1, -2)$, $R(-2,4) \\to (4, 2)$. These are the "
            "image vertices but matched to different labels — the motion maps the TRIANGLE onto "
            "the triangle, with $P \\to Q'$, $Q \\to P'$ and $R$ near $R'$."
            "**Settle it with side lengths instead.** In $PQR$: $PQ = 4$, $PR = 3$, "
            "$QR = \\sqrt{16 + 9} = 5$. In $P'Q'R'$: $P'Q' = |2 - (-2)| = 4$, "
            "$P'R' = |4 - 1| = 3$, $Q'R' = \\sqrt{(4-1)^2 + (-2-2)^2} = \\sqrt{9 + 16} = 5$."
            "**Conclusion.** All three pairs of sides are equal, so the triangles are congruent by "
            "**SSS** — and since SSS guarantees a rigid motion exists, congruence is established "
            "whether or not the single motion is easy to name. Both are right triangles with legs "
            "$3$ and $4$, one oriented with its right angle opening right and up, the other "
            "rotated a quarter turn.",
            [
                "Eq(Abs(2 - (-2)), 4)",
                "Eq(Abs(4 - 1), 3)",
                "Eq((2-(-2))**2 + (1-4)**2, 25)",
                "Eq((4-1)**2 + (-2-2)**2, 25)",
                "Eq(3**2 + 4**2, 25)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="transformations-and-congruence",
        title="Transformations & Congruence",
        unit_number=7,
        blurb=(
            "Translations, reflections and rotations as coordinate rules; sequences of them and "
            "the symmetry they reveal; congruence DEFINED by rigid motion with SSS, SAS and ASA "
            "as consequences; and compass-and-straightedge constructions proved by congruent "
            "triangles."
        ),
        builds_on=(
            "The coordinate plane from Unit 4 — every transformation here is written as a rule on "
            "coordinates — and the function concept from Unit 3, since a transformation is a "
            "function whose inputs and outputs are points."
        ),
        lessons=[
            lesson_rigid_motions(),
            lesson_sequences(),
            lesson_congruence(),
            lesson_constructions(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
