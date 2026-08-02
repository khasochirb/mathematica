#!/usr/bin/env python3
"""Integrated Mathematics 3 — Unit 4: Trigonometric Functions.

CCSS Integrated Math III: F-TF.1 (radian measure as the arc length subtended
on the unit circle), F-TF.2 (the unit circle extends the trigonometric
functions to ALL real numbers), F-TF.5 (choose trigonometric functions to
model periodic phenomena with specified amplitude, frequency and midline),
F-TF.8 (prove the Pythagorean identity and use it to find sin, cos or tan
given one of them and the quadrant).

The unit's through-line: TRIGONOMETRY LEAVES THE TRIANGLE. IM2's sine and
cosine were ratios locked inside a right triangle, defined only for acute
angles. Wrap the number line around the unit circle and the same two names
become COORDINATES — defined for every real number, positive or negative,
however many times around. Everything new in this unit falls out of that one
move: the signs by quadrant are just the signs of coordinates, the exact
values are old friends reflected into new quadrants, the graphs are what the
coordinates trace as the point travels, and the Pythagorean identity is
nothing but the circle's own equation x^2 + y^2 = 1 wearing trig notation.

Run: python3 scripts/im/build_im3_unit4.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from imbuild import fact, lesson, mistake, problem, tap, write_unit  # noqa: E402

COURSE = "integrated-3"


# ===========================================================================
# Lesson 1 — F-TF.1/2: the unit circle
# ===========================================================================

def lesson_unit_circle():
    return lesson(
        slug="the-unit-circle",
        title="The Unit Circle",
        concrete=(
            "A Ferris wheel car's height depends on the angle the wheel has turned — and "
            "the wheel does not stop at $90^\\circ$. It turns past a quarter, past a half, "
            "all the way around and keeps going. Right-triangle trigonometry has no answer "
            "for $\\sin 200^\\circ$; the wheel clearly does. The unit circle is where that "
            "answer lives."
        ),
        objective=(
            "Define sine and cosine as coordinates on the unit circle, measure angles in "
            "radians in every quadrant, and evaluate the new definitions at the axis "
            "angles."
        ),
        concept=[
            "Draw a circle of radius $1$ centred at the origin and stand an angle "
            "$\\theta$ at the positive $x$-axis, opening counterclockwise. The angle's "
            "terminal side crosses the circle at exactly one point — and that point's "
            "coordinates are DEFINED to be $(\\cos\\theta, \\sin\\theta)$. For an acute "
            "$\\theta$ this agrees perfectly with IM2's triangle ratios: drop a "
            "perpendicular from the point and the hypotenuse is the radius, $1$.",

            "The gain is enormous: a point on the circle exists for EVERY angle. "
            "$200^\\circ$, $-45^\\circ$ (clockwise), $750^\\circ$ (twice around and a "
            "bit) — each lands somewhere on the circle, so each has a sine and cosine. "
            "The triangle definition was a special case; the circle definition is the "
            "function.",

            "Radians measure the angle by the ARC it cuts on this circle: a full turn is "
            "the whole circumference, $2\\pi$; a half turn is $\\pi$; a right angle "
            "$\\frac{\\pi}{2}$. Converting is one proportion — multiply degrees by "
            "$\\frac{\\pi}{180}$ — and the payoff, visible in this unit's graphs, is that "
            "angle and arc length become the SAME number, so the horizontal axis of a "
            "trig graph is just distance travelled around the circle.",

            "The axis angles come free. At $\\theta = 0$ the point is $(1, 0)$: "
            "$\\cos 0 = 1$, $\\sin 0 = 0$. At $\\frac{\\pi}{2}$ it is $(0, 1)$; at "
            "$\\pi$, $(-1, 0)$; at $\\frac{3\\pi}{2}$, $(0, -1)$. And because "
            "$2\\pi$ lands back on $(1, 0)$, the functions REPEAT: "
            "$\\sin(\\theta + 2\\pi) = \\sin\\theta$ for every $\\theta$. Periodicity is "
            "built into the definition, not discovered later.",
        ],
        key_idea=(
            "On the unit circle, cosine IS the x-coordinate and sine IS the "
            "y-coordinate of the point the angle reaches. Every fact in this unit is "
            "that sentence read off the picture."
        ),
        facts=[
            fact("The definition", "(\\cos\\theta,\\ \\sin\\theta)",
                 "The coordinates of the point where the angle's terminal side meets the "
                 "unit circle."),
            fact("Radian conversion", "\\text{rad} = \\text{deg} \\times \\tfrac{\\pi}{180}",
                 "A full turn is 2π radians = 360°."),
            fact("Axis values", "\\cos 0 = 1,\\ \\sin\\tfrac{\\pi}{2} = 1,\\ \\cos\\pi = -1",
                 "Read straight off the points (1,0), (0,1), (-1,0), (0,-1)."),
            fact("Periodicity", "\\sin(\\theta + 2\\pi) = \\sin\\theta",
                 "A full extra turn lands on the same point, so nothing changes."),
            fact("Negative angles", "\\theta < 0 \\text{ turns clockwise}",
                 "The circle handles them the same way — one point, two coordinates."),
        ],
        worked=[
            problem(
                "im3-u4-l1-we1",
                "Convert $150^\\circ$ and $270^\\circ$ to radians, and "
                "$\\dfrac{7\\pi}{4}$ to degrees.",
                "**Degrees to radians: multiply by pi over 180.** "
                "$150 \\cdot \\frac{\\pi}{180} = \\frac{150\\pi}{180} = \\frac{5\\pi}{6}$."
                "**Again.** $270 \\cdot \\frac{\\pi}{180} = \\frac{3\\pi}{2}$."
                "**Radians to degrees: multiply by 180 over pi.** "
                "$\\frac{7\\pi}{4} \\cdot \\frac{180}{\\pi} = \\frac{7 \\cdot 180}{4} = "
                "315$, so $\\frac{7\\pi}{4} = 315^\\circ$."
                "**Keep the landmarks.** $\\pi$ is half a turn and $\\frac{\\pi}{2}$ a "
                "quarter; every conversion should land sensibly among them — "
                "$\\frac{5\\pi}{6}$ is just short of a half turn, as $150^\\circ$ "
                "should be.",
                [
                    "Eq(150*pi/180, 5*pi/6)",
                    "Eq(270*pi/180, 3*pi/2)",
                    "Eq(Rational(7*180, 4), 315)",
                ],
            ),
            problem(
                "im3-u4-l1-we2",
                "Using coordinates, evaluate $\\cos\\pi$, $\\sin\\dfrac{3\\pi}{2}$ and "
                "$\\cos\\dfrac{\\pi}{2}$.",
                "**Walk to each point.** A half turn ($\\pi$) lands at $(-1, 0)$; "
                "three quarters ($\\frac{3\\pi}{2}$) lands at $(0, -1)$; a quarter "
                "($\\frac{\\pi}{2}$) lands at $(0, 1)$."
                "**Read the coordinate the question names.** Cosine is the "
                "$x$-coordinate: $\\cos\\pi = -1$ and $\\cos\\frac{\\pi}{2} = 0$. Sine is "
                "the $y$-coordinate: $\\sin\\frac{3\\pi}{2} = -1$."
                "**No triangle appeared.** None of these angles is acute, and none of "
                "these values needs one — the coordinates ARE the answer.",
                [
                    "Eq(simplify(cos(pi)), -1)",
                    "Eq(simplify(sin(3*pi/2)), -1)",
                    "Eq(simplify(cos(pi/2)), 0)",
                ],
            ),
            problem(
                "im3-u4-l1-we3",
                "Find an angle between $0$ and $2\\pi$ that lands on the same point as "
                "(a) $\\dfrac{13\\pi}{6}$, (b) $-\\dfrac{\\pi}{3}$, and evaluate "
                "$\\sin$ of each.",
                "**(a) Strip the full turns.** $\\frac{13\\pi}{6} = 2\\pi + "
                "\\frac{\\pi}{6}$ — one full turn plus a bit, so it lands where "
                "$\\frac{\\pi}{6}$ does, and $\\sin\\frac{13\\pi}{6} = "
                "\\sin\\frac{\\pi}{6} = \\frac{1}{2}$."
                "**(b) Add a turn to come around.** $-\\frac{\\pi}{3} + 2\\pi = "
                "\\frac{5\\pi}{3}$ — a clockwise third-of-a-quarter is the same point as "
                "$\\frac{5\\pi}{3}$ counterclockwise, in quadrant IV where sine is "
                "negative: $\\sin\\left(-\\frac{\\pi}{3}\\right) = -\\frac{\\sqrt{3}}{2}$."
                "**The principle.** Adding or subtracting $2\\pi$ never changes the "
                "point — coterminal angles share every trig value.",
                [
                    "Eq(13*pi/6 - 2*pi, pi/6)",
                    "Eq(simplify(sin(13*pi/6) - Rational(1, 2)), 0)",
                    "Eq(-pi/3 + 2*pi, 5*pi/3)",
                    "Eq(simplify(sin(-pi/3) + sqrt(3)/2), 0)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Treating sin and cos as undefined past 90 degrees.",
                "That is the TRIANGLE definition's limit, not the function's. On the "
                "unit circle every angle reaches a point, so every angle has both "
                "values — sin 200° exists and is simply that point's y-coordinate.",
            ),
            mistake(
                "Mixing the coordinates up: sine first because it sounds first.",
                "The point is (cos θ, sin θ) — cosine is x, sine is y. Anchor it at "
                "θ = 0: the point is (1, 0), and indeed cos 0 = 1, sin 0 = 0.",
            ),
            mistake(
                "Converting radians with 360 instead of 180.",
                "π radians is a HALF turn: multiply degrees by π/180. Using π/360 makes "
                "every angle half its true size — 90° would come out as π/4.",
            ),
            mistake(
                "Thinking a negative angle gives negative values automatically.",
                "Negative means CLOCKWISE, nothing more. -π/3 lands in quadrant IV, "
                "where cosine is positive: cos(-π/3) = 1/2. The quadrant decides signs, "
                "not the direction of travel.",
            ),
        ],
        try_it=[
            problem(
                "im3-u4-l1-t1",
                "Convert $120^\\circ$ to radians and $\\dfrac{5\\pi}{4}$ to degrees.",
                "$120 \\cdot \\frac{\\pi}{180} = \\frac{2\\pi}{3}$, and "
                "$\\frac{5\\pi}{4} \\cdot \\frac{180}{\\pi} = 225^\\circ$.",
                ["Eq(120*pi/180, 2*pi/3)", "Eq(Rational(5*180, 4), 225)"],
            ),
            problem(
                "im3-u4-l1-t2",
                "Evaluate $\\sin\\pi$ and $\\cos\\dfrac{3\\pi}{2}$.",
                "The half-turn point is $(-1, 0)$, so $\\sin\\pi = 0$. The "
                "three-quarter point is $(0, -1)$, so $\\cos\\frac{3\\pi}{2} = 0$.",
                ["Eq(simplify(sin(pi)), 0)", "Eq(simplify(cos(3*pi/2)), 0)"],
            ),
            problem(
                "im3-u4-l1-t3",
                "Which angle in $[0, 2\\pi)$ is coterminal with $\\dfrac{9\\pi}{4}$?",
                "$\\frac{9\\pi}{4} - 2\\pi = \\frac{\\pi}{4}$ — one full turn plus an "
                "eighth. Every trig value of the two angles agrees.",
                [
                    "Eq(9*pi/4 - 2*pi, pi/4)",
                    "Eq(simplify(sin(9*pi/4) - sin(pi/4)), 0)",
                ],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "The triangle's ratios become coordinates", "body": "Stand an angle at the positive $x$-axis, opening counterclockwise, and mark where its terminal side crosses the circle of radius $1$. That point's coordinates are DEFINED to be $(\\cos\\theta, \\sin\\theta)$. For acute angles this agrees with the right-triangle ratios — but now EVERY angle has a point, so every angle has a sine and cosine.", "beats": ["Cosine = the $x$-coordinate", "Sine = the $y$-coordinate", "Defined for every angle, not just acute"]},
            {"kind": "worked", "title": "Converting between degrees and radians", "problemId": "im3-u4-l1-we1"},
            
            tap(
                "Read the point",
                "The angle $\\pi$ lands at the point $(-1, 0)$. Therefore $\\cos\\pi$ "
                "equals:",
                ["$-1$", "$0$", "$1$", "undefined"],
                0,
                "Cosine is the $x$-coordinate of the point — here $-1$. Sine is the "
                "$y$-coordinate, $0$.",
                ["Eq(simplify(cos(pi)), -1)", "Eq(simplify(sin(pi)), 0)"],
            ),
            {"kind": "worked", "title": "Axis angles, read straight off the point", "problemId": "im3-u4-l1-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Radians measure the arc", "body": "A full turn is the full circumference, $2\\pi$ — so converting is one proportion: multiply degrees by $\\frac{\\pi}{180}$. Sanity-check against landmarks: $\\pi$ is half a turn, $\\frac{\\pi}{2}$ a quarter. A conversion that lands nowhere near its landmark is wrong."},
            tap(
                "Quarter turns",
                "$90^\\circ$ in radians is:",
                ["$\\frac{\\pi}{2}$", "$\\frac{\\pi}{4}$", "$\\pi$", "$\\frac{\\pi}{90}$"],
                0,
                "A full turn is $2\\pi$, so a quarter turn is $\\frac{2\\pi}{4} = "
                "\\frac{\\pi}{2}$. Equivalently $90 \\cdot \\frac{\\pi}{180}$.",
                ["Eq(90*pi/180, pi/2)"],
            ),
            {"kind": "worked", "title": "Coterminal angles share everything", "problemId": "im3-u4-l1-we3"},
            {"kind": "teach", "title": "Around again changes nothing", "body": "Adding or subtracting $2\\pi$ lands on the same point, so it changes no trig value — the functions repeat, by construction. Negative angles just travel clockwise: $-\\frac{\\pi}{3}$ and $\\frac{5\\pi}{3}$ are the same point. Periodicity isn't discovered later; it is built into the definition.", "beats": ["$\\theta \\pm 2\\pi$: same point, same values", "Negative = clockwise", "$\\sin(\\theta + 2\\pi) = \\sin\\theta$, always"]},
            {"kind": "tryIt", "title": "Convert both ways", "problemId": "im3-u4-l1-t1"},
            {"kind": "tryIt", "title": "Evaluate at the axes", "problemId": "im3-u4-l1-t2"},
            {"kind": "tryIt", "title": "A coterminal angle", "problemId": "im3-u4-l1-t3"},
            tap(
                "Going around again",
                "$\\sin\\left(\\dfrac{\\pi}{6} + 2\\pi\\right)$ equals:",
                ["$\\sin\\frac{\\pi}{6}$", "$\\sin\\frac{\\pi}{6} + 1$",
                 "$-\\sin\\frac{\\pi}{6}$", "$2\\sin\\frac{\\pi}{6}$"],
                0,
                "A full extra turn lands on the SAME point, so nothing about the "
                "coordinates changes. This is the periodicity every graph in Lesson 3 "
                "inherits.",
                ["Eq(simplify(sin(pi/6 + 2*pi) - sin(pi/6)), 0)"],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["The point is $(\\cos\\theta, \\sin\\theta)$ — cosine is $x$, sine is $y$", "Radians: multiply degrees by $\\frac{\\pi}{180}$; $\\pi$ is a half turn", "Axis values come free from $(1,0), (0,1), (-1,0), (0,-1)$", "Coterminal angles (differing by $2\\pi$) share every value", "The quadrant decides signs — not the direction of travel"]},
        ],
    )


# ===========================================================================
# Lesson 2 — reference angles and exact values
# ===========================================================================

def lesson_reference():
    return lesson(
        slug="reference-angles-and-exact-values",
        title="Reference Angles & Exact Values",
        concrete=(
            "Fold a paper circle along its vertical axis, then its horizontal one: all "
            "four quadrants land on the first. Every point on the circle is a "
            "first-quadrant point with some signs flipped — which means the handful of "
            "exact values IM2 knew for $30^\\circ$, $45^\\circ$ and $60^\\circ$ is "
            "already the complete list. The circle has no new numbers, only new signs."
        ),
        objective=(
            "Find the reference angle and quadrant of any angle, and combine them to "
            "evaluate sine, cosine and tangent exactly at the special angles."
        ),
        concept=[
            "The REFERENCE ANGLE of $\\theta$ is the acute angle between its terminal "
            "side and the $x$-axis — the first-quadrant angle it folds onto. "
            "$\\frac{5\\pi}{6}$ leans $\\frac{\\pi}{6}$ short of the half turn, so its "
            "reference angle is $\\frac{\\pi}{6}$; $\\frac{4\\pi}{3}$ pokes "
            "$\\frac{\\pi}{3}$ past it, so its reference angle is $\\frac{\\pi}{3}$.",

            "Folding flips signs but never sizes: $|\\sin\\theta|$ and "
            "$|\\cos\\theta|$ equal the sine and cosine of the reference angle. The "
            "signs come from the quadrant, and they are just coordinate signs — "
            "quadrant II has $x < 0, y > 0$, so cosine is negative and sine positive "
            "there. Quadrant III makes both negative; quadrant IV flips only the sine.",

            "So every exact evaluation is a two-step: NAME the reference angle, then "
            "SIGN the first-quadrant value by quadrant. $\\cos\\frac{2\\pi}{3}$: "
            "reference $\\frac{\\pi}{3}$, quadrant II, cosine negative — "
            "$-\\frac{1}{2}$. No new memorisation happened; the quadrant did all the "
            "new work.",

            "Tangent rides along as the ratio $\\tan\\theta = "
            "\\frac{\\sin\\theta}{\\cos\\theta}$ — on the circle, the slope of the "
            "terminal side. Its sign is the quotient of the two coordinate signs "
            "(positive in quadrants I and III, negative in II and IV), and it is "
            "undefined exactly where cosine vanishes, at $\\frac{\\pi}{2}$ and "
            "$\\frac{3\\pi}{2}$ — a vertical terminal side has no slope.",
        ],
        key_idea=(
            "Reference angle for the SIZE, quadrant for the SIGN. Every exact value on "
            "the circle is a first-quadrant value wearing its quadrant's signs."
        ),
        facts=[
            fact("Reference angle", "\\text{acute angle to the } x\\text{-axis}",
                 "The first-quadrant angle the terminal side folds onto."),
            fact("Quadrant signs", "\\text{II: } \\sin +,\\ \\text{III: } \\tan +,\\ \\text{IV: } \\cos +",
                 "All three are positive in quadrant I — the coordinate signs decide."),
            fact("The three sizes", "\\tfrac{1}{2},\\ \\tfrac{\\sqrt{2}}{2},\\ \\tfrac{\\sqrt{3}}{2}",
                 "The only magnitudes sine and cosine take at the special angles."),
            fact("Tangent", "\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}",
                 "The slope of the terminal side; undefined where cosine is 0."),
        ],
        worked=[
            problem(
                "im3-u4-l2-we1",
                "Evaluate $\\sin\\dfrac{5\\pi}{6}$ and $\\cos\\dfrac{5\\pi}{6}$ exactly.",
                "**Name the reference angle.** $\\frac{5\\pi}{6}$ is $\\frac{\\pi}{6}$ "
                "short of $\\pi$, so the reference angle is $\\frac{\\pi}{6}$."
                "**Recall the first-quadrant sizes.** $\\sin\\frac{\\pi}{6} = "
                "\\frac{1}{2}$ and $\\cos\\frac{\\pi}{6} = \\frac{\\sqrt{3}}{2}$."
                "**Sign by quadrant.** Quadrant II: $y > 0$, $x < 0$. So "
                "$\\sin\\frac{5\\pi}{6} = \\frac{1}{2}$ and $\\cos\\frac{5\\pi}{6} = "
                "-\\frac{\\sqrt{3}}{2}$.",
                [
                    "Eq(pi - 5*pi/6, pi/6)",
                    "Eq(simplify(sin(5*pi/6) - Rational(1, 2)), 0)",
                    "Eq(simplify(cos(5*pi/6) + sqrt(3)/2), 0)",
                ],
            ),
            problem(
                "im3-u4-l2-we2",
                "Evaluate $\\cos\\dfrac{4\\pi}{3}$, $\\sin\\dfrac{4\\pi}{3}$ and "
                "$\\tan\\dfrac{4\\pi}{3}$ exactly.",
                "**Reference angle.** $\\frac{4\\pi}{3} - \\pi = \\frac{\\pi}{3}$: it "
                "pokes a third-of-a-quarter past the half turn, into quadrant III."
                "**Sizes.** $\\cos\\frac{\\pi}{3} = \\frac{1}{2}$, "
                "$\\sin\\frac{\\pi}{3} = \\frac{\\sqrt{3}}{2}$."
                "**Signs.** Quadrant III makes both coordinates negative: "
                "$\\cos\\frac{4\\pi}{3} = -\\frac{1}{2}$, $\\sin\\frac{4\\pi}{3} = "
                "-\\frac{\\sqrt{3}}{2}$."
                "**Tangent is their ratio.** Two negatives divide to a positive: "
                "$\\tan\\frac{4\\pi}{3} = \\sqrt{3}$ — quadrant III is tangent's other "
                "positive home.",
                [
                    "Eq(4*pi/3 - pi, pi/3)",
                    "Eq(simplify(cos(4*pi/3) + Rational(1, 2)), 0)",
                    "Eq(simplify(sin(4*pi/3) + sqrt(3)/2), 0)",
                    "Eq(simplify(tan(4*pi/3) - sqrt(3)), 0)",
                ],
            ),
            problem(
                "im3-u4-l2-we3",
                "Find every angle $\\theta$ in $[0, 2\\pi)$ with "
                "$\\sin\\theta = -\\dfrac{\\sqrt{2}}{2}$.",
                "**Size first.** The magnitude $\\frac{\\sqrt{2}}{2}$ belongs to the "
                "reference angle $\\frac{\\pi}{4}$."
                "**Then location.** Sine is negative below the $x$-axis — quadrants III "
                "and IV."
                "**Build each angle from its reference.** Quadrant III: $\\pi + "
                "\\frac{\\pi}{4} = \\frac{5\\pi}{4}$. Quadrant IV: $2\\pi - "
                "\\frac{\\pi}{4} = \\frac{7\\pi}{4}$."
                "**Check one.** $\\sin\\frac{5\\pi}{4} = -\\frac{\\sqrt{2}}{2}$ ✓. Two "
                "answers, because the horizontal line $y = -\\frac{\\sqrt{2}}{2}$ cuts "
                "the circle twice.",
                [
                    "Eq(pi + pi/4, 5*pi/4)",
                    "Eq(2*pi - pi/4, 7*pi/4)",
                    "Eq(simplify(sin(5*pi/4) + sqrt(2)/2), 0)",
                    "Eq(simplify(sin(7*pi/4) + sqrt(2)/2), 0)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Measuring the reference angle from the y-axis.",
                "It is always the acute angle to the X-axis. For 5π/6 the reference is "
                "π/6 (the gap to π), not π/3 (the gap to π/2).",
            ),
            mistake(
                "Letting the reference angle carry the sign.",
                "The reference angle is a SIZE — always acute, always positive. The "
                "quadrant alone decides signs. Compute size and sign separately, then "
                "combine.",
            ),
            mistake(
                "Assuming tangent is negative wherever sine is.",
                "Tangent is the RATIO of sine to cosine, so two negatives make it "
                "positive: in quadrant III, sin and cos are both negative and tan is "
                "positive.",
            ),
            mistake(
                "Giving one answer to sin θ = c on a full turn.",
                "A horizontal line at height c (with |c| < 1) crosses the circle "
                "TWICE, so there are two angles per turn. One answer is only correct "
                "at the extremes c = ±1.",
            ),
        ],
        try_it=[
            problem(
                "im3-u4-l2-t1",
                "State the reference angle of $\\dfrac{7\\pi}{6}$ and evaluate "
                "$\\sin\\dfrac{7\\pi}{6}$.",
                "$\\frac{7\\pi}{6} - \\pi = \\frac{\\pi}{6}$, quadrant III, sine "
                "negative: $\\sin\\frac{7\\pi}{6} = -\\frac{1}{2}$.",
                [
                    "Eq(7*pi/6 - pi, pi/6)",
                    "Eq(simplify(sin(7*pi/6) + Rational(1, 2)), 0)",
                ],
            ),
            problem(
                "im3-u4-l2-t2",
                "Evaluate $\\cos\\dfrac{11\\pi}{6}$ exactly.",
                "Reference angle $2\\pi - \\frac{11\\pi}{6} = \\frac{\\pi}{6}$, quadrant "
                "IV where cosine is positive: $\\cos\\frac{11\\pi}{6} = "
                "\\frac{\\sqrt{3}}{2}$.",
                [
                    "Eq(2*pi - 11*pi/6, pi/6)",
                    "Eq(simplify(cos(11*pi/6) - sqrt(3)/2), 0)",
                ],
            ),
            problem(
                "im3-u4-l2-t3",
                "Evaluate $\\tan\\dfrac{5\\pi}{4}$.",
                "Reference $\\frac{\\pi}{4}$ in quadrant III, where tangent is "
                "positive: $\\tan\\frac{5\\pi}{4} = 1$.",
                ["Eq(5*pi/4 - pi, pi/4)", "Eq(simplify(tan(5*pi/4)), 1)"],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "Fold every angle into the first quadrant", "body": "The reference angle of $\\theta$ is the acute angle between its terminal side and the $x$-axis — the first-quadrant angle it folds onto. Folding flips signs but never sizes: the magnitudes of $\\sin\\theta$ and $\\cos\\theta$ equal those of the reference angle.", "beats": ["Reference angle: measured to the $x$-axis", "Sizes survive the fold", "Signs come from the quadrant"]},
            {"kind": "worked", "title": "A second-quadrant fold", "problemId": "im3-u4-l2-we1"},
            
            tap(
                "Fold it back",
                "The reference angle of $\\dfrac{2\\pi}{3}$ is:",
                ["$\\frac{\\pi}{3}$", "$\\frac{\\pi}{6}$", "$\\frac{2\\pi}{3}$", "$\\frac{\\pi}{2}$"],
                0,
                "$\\frac{2\\pi}{3}$ sits $\\frac{\\pi}{3}$ short of the half turn "
                "$\\pi$, so it folds onto $\\frac{\\pi}{3}$.",
                ["Eq(pi - 2*pi/3, pi/3)"],
            ),
            {"kind": "worked", "title": "All three functions in quadrant III", "problemId": "im3-u4-l2-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Measure to the x-axis, never the y-axis", "body": "$\\frac{5\\pi}{6}$ leans $\\frac{\\pi}{6}$ away from the NEGATIVE $x$-axis — that's its reference angle. Measuring to the $y$-axis gives $\\frac{\\pi}{3}$ and every value that follows is wrong. The fold is always onto the horizontal."},
            tap(
                "Sign check",
                "In which quadrants is cosine NEGATIVE?",
                ["II and III", "I and II", "III and IV", "II and IV"],
                0,
                "Cosine is the $x$-coordinate, negative on the left half of the "
                "circle — quadrants II and III.",
                ["Eq(simplify(cos(2*pi/3) + Rational(1, 2)), 0)",
                 "Eq(simplify(cos(4*pi/3) + Rational(1, 2)), 0)"],
            ),
            {"kind": "worked", "title": "Running the machine backwards", "problemId": "im3-u4-l2-we3"},
            {"kind": "teach", "title": "Every evaluation is a two-step", "body": "NAME the reference angle, then SIGN the first-quadrant value by quadrant. Tangent rides along as $\\frac{\\sin\\theta}{\\cos\\theta}$ — the slope of the terminal side — its sign the quotient of the two. And an equation like $\\sin\\theta = c$ has TWO answers per turn: one in each quadrant where the sign fits.", "beats": ["Step 1: reference angle", "Step 2: quadrant sign", "$\\sin\\theta = c$: expect two angles per turn"]},
            {"kind": "tryIt", "title": "Name and evaluate", "problemId": "im3-u4-l2-t1"},
            {"kind": "tryIt", "title": "Fourth-quadrant cosine", "problemId": "im3-u4-l2-t2"},
            {"kind": "tryIt", "title": "Tangent in quadrant III", "problemId": "im3-u4-l2-t3"},
            tap(
                "Assemble a value",
                "$\\cos\\dfrac{3\\pi}{4}$ equals:",
                ["$-\\frac{\\sqrt{2}}{2}$", "$\\frac{\\sqrt{2}}{2}$",
                 "$-\\frac{1}{2}$", "$\\frac{\\sqrt{3}}{2}$"],
                0,
                "Reference angle $\\frac{\\pi}{4}$ gives the size "
                "$\\frac{\\sqrt{2}}{2}$; quadrant II makes cosine negative.",
                ["Eq(simplify(cos(3*pi/4) + sqrt(2)/2), 0)"],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["Reference angle for the SIZE, quadrant for the SIGN", "Fold onto the $x$-axis — never measure from the $y$-axis", "Only three magnitudes to memorise: those of $\\tfrac{\\pi}{6}, \\tfrac{\\pi}{4}, \\tfrac{\\pi}{3}$", "Tangent = sine over cosine = slope of the terminal side", "$\\sin\\theta = c$ on a full turn: two answers, one per matching quadrant"]},
        ],
    )


# ===========================================================================
# Lesson 3 — F-TF.5: the graphs of sine and cosine
# ===========================================================================

def lesson_graphs():
    return lesson(
        slug="graphs-of-sine-and-cosine",
        title="Graphs of Sine & Cosine",
        concrete=(
            "Watch one Ferris wheel car and plot only its HEIGHT against time: up, over "
            "the top, down, under the bottom, up again — a smooth, endlessly repeating "
            "wave. Every periodic thing (tides, daylight hours, a heartbeat trace) draws "
            "a curve of this family, and the family has just three dials: how high it "
            "swings, how long a lap takes, and where its centreline sits."
        ),
        objective=(
            "Graph transformations of sine and cosine, reading amplitude, period and "
            "midline from the equation — and write the equation of a wave from its "
            "description."
        ),
        concept=[
            "Let $\\theta$ run along the horizontal axis and plot $y = \\sin\\theta$: "
            "the $y$-coordinate of the circling point, unrolled. It rises from $0$ to "
            "$1$ at $\\frac{\\pi}{2}$, falls through $0$ at $\\pi$ to $-1$ at "
            "$\\frac{3\\pi}{2}$, and closes the lap at $2\\pi$. Cosine draws the SAME "
            "wave started at its peak — it is the $x$-coordinate, which begins at $1$.",

            "In $y = a\\sin(bx) + k$, each parameter turns one dial. The AMPLITUDE "
            "$|a|$ is the half-height of the swing — the wave reaches $k + |a|$ and "
            "$k - |a|$. The MIDLINE $y = k$ is the horizontal centre the wave "
            "oscillates about. Negative $a$ flips the wave upside down without "
            "changing its size.",

            "The PERIOD is $\\frac{2\\pi}{b}$: the factor $b$ counts how many full "
            "circles fit in a $2\\pi$-wide window, so bigger $b$ means a tighter, "
            "faster wave. $y = \\sin 2x$ completes a lap in $\\pi$; "
            "$y = \\sin\\frac{x}{2}$ takes $4\\pi$. The radian choice of Lesson 1 pays "
            "off here — angle and axis-distance are the same number, so the period "
            "formula has no conversion factor in it.",

            "Modelling runs the reading backwards. From a maximum of $14$ and a "
            "minimum of $2$: the midline is their average, $k = 8$, and the amplitude "
            "their half-difference, $a = 6$. A period of $12$ hours forces "
            "$b = \\frac{2\\pi}{12} = \\frac{\\pi}{6}$. Choose sine or cosine by where "
            "the story STARTS — at the midline going up, sine; at a peak, cosine.",
        ],
        key_idea=(
            "Three dials: $|a|$ sets the swing, $y = k$ sets the centreline, and "
            "$\\frac{2\\pi}{b}$ sets the lap time. Read them off an equation, or set "
            "them from max, min and period when building one."
        ),
        facts=[
            fact("Amplitude", "|a|",
                 "Half the vertical swing: from midline to peak."),
            fact("Period", "\\frac{2\\pi}{b}",
                 "The horizontal length of one full lap of the circle."),
            fact("Midline", "y = k",
                 "The horizontal centre; max = k + |a|, min = k - |a|."),
            fact("From max and min", "k = \\tfrac{M + m}{2},\\ |a| = \\tfrac{M - m}{2}",
                 "Average for the midline, half-difference for the amplitude."),
            fact("Cosine's head start", "\\cos 0 = 1",
                 "Cosine is the sine wave started at its peak — pick it when the story "
                 "starts at a maximum."),
        ],
        worked=[
            problem(
                "im3-u4-l3-we1",
                "State the amplitude, period and midline of "
                "$y = 3\\sin(2x) - 1$, and its maximum and minimum values.",
                "**Amplitude.** $|a| = |3| = 3$."
                "**Period.** $\\frac{2\\pi}{b} = \\frac{2\\pi}{2} = \\pi$ — two full "
                "waves fit where $\\sin x$ draws one."
                "**Midline.** $y = -1$."
                "**Extremes.** Maximum $-1 + 3 = 2$, minimum $-1 - 3 = -4$. The wave "
                "lives entirely between those two lines, touching each once per lap.",
                [
                    "Eq(Abs(3), 3)",
                    "Eq(2*pi/2, pi)",
                    "Eq(-1 + 3, 2)",
                    "Eq(-1 - 3, -4)",
                ],
            ),
            problem(
                "im3-u4-l3-we2",
                "Describe how $y = -2\\cos\\left(\\dfrac{x}{2}\\right)$ differs from "
                "$y = \\cos x$, and give its value at $x = 0$.",
                "**Amplitude.** $|-2| = 2$: the swing doubles."
                "**The flip.** The negative sign reflects the wave in its midline — "
                "this curve STARTS at its minimum, not its maximum."
                "**Period.** $b = \\frac{1}{2}$ gives $\\frac{2\\pi}{1/2} = 4\\pi$: the "
                "wave stretches to double length, one lap where $\\cos x$ makes two."
                "**Value at zero.** $-2\\cos 0 = -2 \\cdot 1 = -2$ — confirming the "
                "start at the bottom of the swing.",
                [
                    "Eq(Abs(-2), 2)",
                    "Eq(2*pi/Rational(1, 2), 4*pi)",
                    "Eq(-2*1, -2)",
                    "Eq(simplify(cos(0)), 1)",
                ],
            ),
            problem(
                "im3-u4-l3-we3",
                "The depth of water at a pier oscillates between a high tide of $14$ m "
                "and a low tide of $2$ m, with $12$ hours between highs. Write a model "
                "for the depth $t$ hours after a high tide.",
                "**Midline from the average.** $k = \\frac{14 + 2}{2} = 8$."
                "**Amplitude from the half-difference.** $a = \\frac{14 - 2}{2} = 6$."
                "**Period sets b.** $\\frac{2\\pi}{b} = 12$ gives $b = \\frac{\\pi}{6}$."
                "**Cosine, because the clock starts at a HIGH.** "
                "$$d(t) = 8 + 6\\cos\\left(\\frac{\\pi}{6}t\\right)$$"
                "**Check the landmarks.** $d(0) = 8 + 6 = 14$ ✓ (high), "
                "$d(6) = 8 + 6\\cos\\pi = 2$ ✓ (low, half a period later).",
                [
                    "Eq(Rational(14 + 2, 2), 8)",
                    "Eq(Rational(14 - 2, 2), 6)",
                    "Eq(2*pi/(pi/6), 12)",
                    "Eq(8 + 6*1, 14)",
                    "Eq(simplify(8 + 6*cos(pi)), 2)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Calling the full swing the amplitude.",
                "Amplitude is measured from the MIDLINE to a peak — half the "
                "max-to-min distance. A wave running between 2 and 14 has amplitude "
                "6, not 12.",
            ),
            mistake(
                "Reading b itself as the period.",
                "b counts laps per 2π of axis; the period is 2π/b. In sin(2x) the 2 "
                "makes the wave FASTER — period π — not slower.",
            ),
            mistake(
                "Treating the negative in -2 cos x as a negative amplitude.",
                "Amplitude is a distance, always positive: |−2| = 2. The sign is a "
                "reflection — the wave starts at its minimum instead of its maximum.",
            ),
            mistake(
                "Choosing sine when the story starts at a peak.",
                "sin 0 = 0: sine starts at the midline heading up. A model clocked "
                "from a maximum wants cosine, or it needs a phase shift sine was "
                "chosen to avoid.",
            ),
        ],
        try_it=[
            problem(
                "im3-u4-l3-t1",
                "State the amplitude and period of $y = 5\\cos(4x)$.",
                "Amplitude $|5| = 5$; period $\\frac{2\\pi}{4} = \\frac{\\pi}{2}$.",
                ["Eq(Abs(5), 5)", "Eq(2*pi/4, pi/2)"],
            ),
            problem(
                "im3-u4-l3-t2",
                "A wave has maximum $11$ and minimum $3$. Find its midline and "
                "amplitude.",
                "Midline $y = \\frac{11 + 3}{2} = 7$; amplitude "
                "$\\frac{11 - 3}{2} = 4$.",
                ["Eq(Rational(11 + 3, 2), 7)", "Eq(Rational(11 - 3, 2), 4)"],
            ),
            problem(
                "im3-u4-l3-t3",
                "Write a sine model with amplitude $3$, period $\\pi$ and midline "
                "$y = 2$.",
                "Period $\\pi$ needs $b = \\frac{2\\pi}{\\pi} = 2$: "
                "$y = 3\\sin(2x) + 2$.",
                ["Eq(2*pi/pi, 2)", "Eq(3*1 + 2, 5)", "Eq(2 - 3, -1)"],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "Unroll the circle", "body": "Let the angle run along a horizontal axis and plot the circling point's $y$-coordinate: that is $y = \\sin\\theta$, the circle unrolled into a wave. It rises to $1$, falls through $0$ to $-1$, and returns — then repeats forever, because the circle does.", "beats": ["The wave IS the circle, unrolled", "Sine starts at 0; cosine starts at 1", "Period $2\\pi$: one full lap"]},
            {"kind": "worked", "title": "Reading the three dials", "problemId": "im3-u4-l3-we1"},
            
            tap(
                "The three dials",
                "For $y = 4\\sin(3x) + 1$, the amplitude, period and midline are:",
                ["$4$, $\\frac{2\\pi}{3}$, $y = 1$", "$4$, $3$, $y = 1$",
                 "$3$, $\\frac{2\\pi}{3}$, $y = 4$", "$5$, $2\\pi$, $y = 1$"],
                0,
                "Amplitude $|4| = 4$; period $\\frac{2\\pi}{3}$ (three laps per "
                "$2\\pi$); midline $y = 1$. Max $5$, min $-3$.",
                ["Eq(Abs(4), 4)", "Eq(1 + 4, 5)", "Eq(1 - 4, -3)"],
            ),
            {"kind": "worked", "title": "A flipped, slowed cosine", "problemId": "im3-u4-l3-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "b is not the period", "body": "In $y = \\sin(bx)$ the number $b$ counts how many full waves fit in a $2\\pi$ window; the period itself is $\\frac{2\\pi}{b}$. Bigger $b$ means a FASTER, tighter wave. Read $b = 4$ as \"four laps per $2\\pi$\", never as \"period $4$\"."},
            tap(
                "Faster or slower",
                "Compared with $y = \\cos x$, the graph of $y = \\cos(3x)$ is:",
                ["compressed — period $\\frac{2\\pi}{3}$", "stretched — period $6\\pi$",
                 "three times taller", "shifted up by $3$"],
                0,
                "$b = 3$ fits three laps where one fitted before: the period shrinks "
                "to $\\frac{2\\pi}{3}$. Height is untouched — that is $a$'s dial.",
                ["Eq(2*pi/3, 2*pi/3)", "Eq(Abs(1), 1)"],
            ),
            {"kind": "worked", "title": "Building a tide model from max and min", "problemId": "im3-u4-l3-we3"},
            {"kind": "teach", "title": "Modelling runs the reading backwards", "body": "From a maximum and minimum: the midline is their average, the amplitude their half-difference, and the period is read off the story's clock. Choose cosine to start at a peak, sine to start on the midline — the choice is a starting point, not a different physics.", "beats": ["Midline $k$ = average of max and min", "Amplitude $|a|$ = half the difference", "Cosine starts at a peak; sine at the midline"]},
            {"kind": "tryIt", "title": "Amplitude and period", "problemId": "im3-u4-l3-t1"},
            {"kind": "tryIt", "title": "Midline from max and min", "problemId": "im3-u4-l3-t2"},
            {"kind": "tryIt", "title": "Build the sine model", "problemId": "im3-u4-l3-t3"},
            tap(
                "Build the model",
                "A wave oscillates between $0$ and $10$ with period $8$, starting at "
                "its maximum. Its model is:",
                ["$y = 5 + 5\\cos\\left(\\frac{\\pi}{4}x\\right)$",
                 "$y = 10\\cos(8x)$",
                 "$y = 5 + 5\\sin\\left(\\frac{\\pi}{4}x\\right)$",
                 "$y = 5 + 10\\cos\\left(\\frac{\\pi}{4}x\\right)$"],
                0,
                "Midline $\\frac{0 + 10}{2} = 5$, amplitude $5$, and period $8$ forces "
                "$b = \\frac{2\\pi}{8} = \\frac{\\pi}{4}$. Cosine, because the story "
                "starts at the top: $y(0) = 5 + 5 = 10$ ✓.",
                [
                    "Eq(Rational(0 + 10, 2), 5)",
                    "Eq(2*pi/(pi/4), 8)",
                    "Eq(5 + 5*1, 10)",
                ],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["Three dials: $|a|$ swing, $k$ centreline, $\\frac{2\\pi}{b}$ lap time", "Amplitude is the HALF-height: $\\frac{\\text{max} - \\text{min}}{2}$", "$b$ counts waves per $2\\pi$; the period is $\\frac{2\\pi}{b}$", "A negative $a$ flips the wave; amplitude stays $|a|$", "Model from a story: midline, amplitude, period, then pick sine or cosine by the start"]},
        ],
    )


# ===========================================================================
# Lesson 4 — F-TF.8: the Pythagorean identity
# ===========================================================================

def lesson_identity():
    return lesson(
        slug="the-pythagorean-identity",
        title="The Pythagorean Identity",
        concrete=(
            "Every point on the unit circle satisfies the circle's own equation, "
            "$x^2 + y^2 = 1$ — that is what being on the circle MEANS. But the "
            "coordinates of the angle's point are named $\\cos\\theta$ and "
            "$\\sin\\theta$. Substitute the names and the equation becomes "
            "$\\sin^2\\theta + \\cos^2\\theta = 1$: the most-used identity in "
            "trigonometry, and it was never anything but the circle introducing itself."
        ),
        objective=(
            "Prove the Pythagorean identity from the unit circle, and use it with "
            "quadrant reasoning to find sine, cosine or tangent given one of them."
        ),
        concept=[
            "The proof is one substitution. A point $(x, y)$ lies on the unit circle "
            "exactly when $x^2 + y^2 = 1$; the point reached by $\\theta$ has "
            "$x = \\cos\\theta$ and $y = \\sin\\theta$; therefore "
            "$\\sin^2\\theta + \\cos^2\\theta = 1$ for EVERY $\\theta$ — acute, obtuse, "
            "negative, enormous. An identity is an equation that is always true, and "
            "this one inherits 'always' from the definition itself.",

            "Its everyday use is trading one value for the other. Given "
            "$\\sin\\theta = \\frac{3}{5}$, the identity forces "
            "$\\cos^2\\theta = 1 - \\frac{9}{25} = \\frac{16}{25}$, so "
            "$\\cos\\theta = \\pm\\frac{4}{5}$. The identity is a statement about "
            "SQUARES, so it can never see the sign — squaring erased it, exactly the "
            "asymmetry Unit 2 met when squaring radical equations.",

            "The quadrant supplies what the algebra lost. If the same $\\theta$ is "
            "known to sit in quadrant II, cosine is negative there and the answer "
            "sharpens to $\\cos\\theta = -\\frac{4}{5}$. Every problem of this type has "
            "the same two movements: the identity for the magnitude, the quadrant for "
            "the sign.",

            "Tangent then comes free as the quotient: $\\tan\\theta = "
            "\\frac{\\sin\\theta}{\\cos\\theta} = \\frac{3/5}{-4/5} = -\\frac{3}{4}$. "
            "The familiar $3$–$4$–$5$ triangle is hiding inside — the identity is "
            "Pythagoras on a hypotenuse of $1$, which is why the classic triples keep "
            "surfacing whenever the values are rational.",
        ],
        key_idea=(
            "$\\sin^2\\theta + \\cos^2\\theta = 1$ is the unit circle's equation with "
            "the coordinates renamed. It recovers any value from any other — up to a "
            "sign that only the quadrant can supply."
        ),
        facts=[
            fact("The identity", "\\sin^2\\theta + \\cos^2\\theta = 1",
                 "The circle equation x² + y² = 1 with the coordinates renamed."),
            fact("Recovering cosine", "\\cos\\theta = \\pm\\sqrt{1 - \\sin^2\\theta}",
                 "The identity gives the magnitude; the quadrant picks the sign."),
            fact("Tangent from both", "\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}",
                 "Once both coordinates are known, tangent is their ratio."),
            fact("Why ±", "\\text{squares forget signs}",
                 "The same lost-information asymmetry as squaring an equation in "
                 "Unit 2."),
        ],
        worked=[
            problem(
                "im3-u4-l4-we1",
                "Given $\\sin\\theta = \\dfrac{3}{5}$ with $\\theta$ in quadrant II, "
                "find $\\cos\\theta$ and $\\tan\\theta$.",
                "**The identity gives the magnitude.** $\\cos^2\\theta = 1 - "
                "\\left(\\frac{3}{5}\\right)^2 = 1 - \\frac{9}{25} = \\frac{16}{25}$, "
                "so $\\cos\\theta = \\pm\\frac{4}{5}$."
                "**The quadrant gives the sign.** Quadrant II is the upper-left: "
                "$x < 0$, so $\\cos\\theta = -\\frac{4}{5}$."
                "**Tangent is the ratio.** $\\tan\\theta = \\frac{3/5}{-4/5} = "
                "-\\frac{3}{4}$ — negative, as tangent always is in quadrant II.",
                [
                    "Eq(1 - Rational(9, 25), Rational(16, 25))",
                    "Eq(Rational(3, 5)**2 + Rational(4, 5)**2, 1)",
                    "Eq(Rational(3, 5)/Rational(-4, 5), Rational(-3, 4))",
                ],
            ),
            problem(
                "im3-u4-l4-we2",
                "Given $\\cos\\theta = -\\dfrac{5}{13}$ with $\\pi < \\theta < "
                "\\dfrac{3\\pi}{2}$, find $\\sin\\theta$.",
                "**Locate the angle.** $\\pi < \\theta < \\frac{3\\pi}{2}$ is quadrant "
                "III — both coordinates negative."
                "**Identity for the magnitude.** $\\sin^2\\theta = 1 - "
                "\\frac{25}{169} = \\frac{144}{169}$, so $\\sin\\theta = "
                "\\pm\\frac{12}{13}$."
                "**Quadrant for the sign.** Quadrant III: $\\sin\\theta = "
                "-\\frac{12}{13}$."
                "**The hidden triple.** $5$–$12$–$13$ on a unit hypotenuse — the "
                "identity is Pythagoras scaled down.",
                [
                    "Eq(1 - Rational(25, 169), Rational(144, 169))",
                    "Eq(Rational(5, 13)**2 + Rational(12, 13)**2, 1)",
                ],
            ),
            problem(
                "im3-u4-l4-we3",
                "Prove that $(1 - \\cos\\theta)(1 + \\cos\\theta) = \\sin^2\\theta$ "
                "for every $\\theta$, and verify it at $\\theta = \\dfrac{\\pi}{6}$.",
                "**Expand the left side.** A difference of squares: "
                "$(1 - \\cos\\theta)(1 + \\cos\\theta) = 1 - \\cos^2\\theta$."
                "**Apply the identity.** $\\sin^2\\theta + \\cos^2\\theta = 1$ "
                "rearranges to $1 - \\cos^2\\theta = \\sin^2\\theta$. Done — both "
                "steps are identities, so the equation holds for every $\\theta$."
                "**Verify at one angle as a sanity check.** At $\\frac{\\pi}{6}$: left "
                "side $\\left(1 - \\frac{\\sqrt{3}}{2}\\right)\\left(1 + "
                "\\frac{\\sqrt{3}}{2}\\right) = 1 - \\frac{3}{4} = \\frac{1}{4}$, and "
                "$\\sin^2\\frac{\\pi}{6} = \\left(\\frac{1}{2}\\right)^2 = "
                "\\frac{1}{4}$ ✓ — one instance never proves an identity, but it "
                "catches a wrong one fast.",
                [
                    "Eq(expand((1 - c)*(1 + c)), 1 - c**2)",
                    "Eq(1 - Rational(3, 4), Rational(1, 4))",
                    "Eq(Rational(1, 2)**2, Rational(1, 4))",
                    "Eq(simplify(sin(pi/6)**2 + cos(pi/6)**2), 1)",
                ],
            ),
        ],
        mistakes=[
            mistake(
                "Writing sin²θ + cos²θ = 1 only for acute θ.",
                "The proof used nothing but 'the point is on the circle', which is "
                "true for EVERY angle. The identity holds at 200°, at -π/3, "
                "everywhere.",
            ),
            mistake(
                "Forgetting the ± when un-squaring.",
                "cos²θ = 16/25 gives cosθ = ±4/5, not just +4/5. The square erased "
                "the sign; only the quadrant can restore it. Same trap as squaring "
                "radical equations in Unit 2.",
            ),
            mistake(
                "Reading sin²θ as sin(θ²).",
                "sin²θ means (sin θ)² — square the VALUE, not the angle. At π/2: "
                "sin²(π/2) = 1, while sin((π/2)²) is the sine of about 2.47, an "
                "entirely different number.",
            ),
            mistake(
                "Verifying at one angle and calling it proved.",
                "One instance can only DISPROVE an identity. The proof must use "
                "identities all the way — here, difference of squares plus the "
                "Pythagorean identity, no numbers involved.",
            ),
        ],
        try_it=[
            problem(
                "im3-u4-l4-t1",
                "Given $\\sin\\theta = \\dfrac{8}{17}$ with $\\theta$ in quadrant I, "
                "find $\\cos\\theta$.",
                "$\\cos^2\\theta = 1 - \\frac{64}{289} = \\frac{225}{289}$, and "
                "quadrant I keeps it positive: $\\cos\\theta = \\frac{15}{17}$.",
                [
                    "Eq(1 - Rational(64, 289), Rational(225, 289))",
                    "Eq(Rational(8, 17)**2 + Rational(15, 17)**2, 1)",
                ],
            ),
            problem(
                "im3-u4-l4-t2",
                "Given $\\cos\\theta = \\dfrac{4}{5}$ with $\\theta$ in quadrant IV, "
                "find $\\tan\\theta$.",
                "$\\sin\\theta = -\\frac{3}{5}$ (negative in quadrant IV), so "
                "$\\tan\\theta = \\frac{-3/5}{4/5} = -\\frac{3}{4}$.",
                [
                    "Eq(Rational(3, 5)**2 + Rational(4, 5)**2, 1)",
                    "Eq(Rational(-3, 5)/Rational(4, 5), Rational(-3, 4))",
                ],
            ),
            problem(
                "im3-u4-l4-t3",
                "Simplify $1 - \\sin^2\\theta$.",
                "Rearranging the identity: $1 - \\sin^2\\theta = \\cos^2\\theta$.",
                [
                    "Eq(simplify(1 - sin(pi/3)**2 - cos(pi/3)**2), 0)",
                    "Eq(simplify(sin(pi/4)**2 + cos(pi/4)**2), 1)",
                ],
            ),
        ],
        steps=[
                        {"kind": "teach", "title": "The circle's equation, renamed", "body": "A point $(x, y)$ lies on the unit circle exactly when $x^2 + y^2 = 1$. The point reached by $\\theta$ has $x = \\cos\\theta$ and $y = \\sin\\theta$ — substitute, and $\\sin^2\\theta + \\cos^2\\theta = 1$ for EVERY angle. The proof is that one substitution; the identity is geometry wearing trig notation.", "beats": ["$x^2 + y^2 = 1$ with coordinates renamed", "True for every $\\theta$, all four quadrants", "One value recovers the other — up to sign"]},
            {"kind": "worked", "title": "From sine to cosine and tangent", "problemId": "im3-u4-l4-we1"},
            
            tap(
                "Where it comes from",
                "The identity $\\sin^2\\theta + \\cos^2\\theta = 1$ is a renaming of:",
                ["the unit circle's equation $x^2 + y^2 = 1$",
                 "the quadratic formula",
                 "the distance between two circles",
                 "the definition of a radian"],
                0,
                "The point's coordinates are $(\\cos\\theta, \\sin\\theta)$, and every "
                "point on the unit circle satisfies $x^2 + y^2 = 1$. Substitute the "
                "names and the identity appears.",
                ["Eq(simplify(sin(pi/5)**2 + cos(pi/5)**2), 1)"],
            ),
            {"kind": "worked", "title": "Quadrant III does the signing", "problemId": "im3-u4-l4-we2"},
            {"kind": "tip", "eyebrow": "Watch out", "title": "Un-squaring costs a ±", "body": "The identity hands you $\\cos^2\\theta$; taking the square root gives $\\pm\\cos\\theta$, and the algebra cannot choose. The QUADRANT chooses. Never write $\\cos\\theta = \\sqrt{1 - \\sin^2\\theta}$ without asking where $\\theta$ lives."},
            tap(
                "Magnitude then sign",
                "$\\sin\\theta = \\dfrac{5}{13}$ and $\\theta$ is in quadrant II. "
                "$\\cos\\theta$ equals:",
                ["$-\\frac{12}{13}$", "$\\frac{12}{13}$", "$-\\frac{8}{13}$", "$\\frac{5}{12}$"],
                0,
                "$\\cos^2\\theta = 1 - \\frac{25}{169} = \\frac{144}{169}$ gives "
                "$\\pm\\frac{12}{13}$; quadrant II makes cosine negative.",
                [
                    "Eq(1 - Rational(25, 169), Rational(144, 169))",
                    "Eq(Rational(5, 13)**2 + Rational(12, 13)**2, 1)",
                ],
            ),
            {"kind": "worked", "title": "Proving an identity, not just checking it", "problemId": "im3-u4-l4-we3"},
            {"kind": "teach", "title": "Familiar triangles, hiding on the circle", "body": "With $\\sin\\theta = \\frac{3}{5}$ the identity forces $\\cos\\theta = \\pm\\frac{4}{5}$ — the $3$–$4$–$5$ triangle scaled onto the unit circle. Tangent then comes free as the quotient of the two. A verification at one angle ILLUSTRATES an identity; only algebra that never picks a value PROVES it.", "beats": ["Pythagorean triples reappear as trig values", "$\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}$", "Verify at a point; prove with algebra"]},
            {"kind": "tryIt", "title": "Quadrant I warm-up", "problemId": "im3-u4-l4-t1"},
            {"kind": "tryIt", "title": "Tangent from cosine", "problemId": "im3-u4-l4-t2"},
            {"kind": "tryIt", "title": "The identity in disguise", "problemId": "im3-u4-l4-t3"},
            tap(
                "Notation check",
                "$\\sin^2\\theta$ means:",
                ["$(\\sin\\theta)^2$", "$\\sin(\\theta^2)$", "$2\\sin\\theta$", "$\\sin(2\\theta)$"],
                0,
                "The exponent binds to the VALUE: square the sine, not the angle. The "
                "identity would be false under any of the other readings.",
                ["Eq(Rational(1, 2)**2, Rational(1, 4))"],
            ),
            {"kind": "recap", "title": "What to carry forward", "points": ["$\\sin^2\\theta + \\cos^2\\theta = 1$ — the unit circle's own equation", "It recovers either value from the other, up to a sign", "The quadrant supplies the sign the algebra lost", "$\\sin^2\\theta$ means $(\\sin\\theta)^2$, never $\\sin(\\theta^2)$", "One-angle checks illustrate; only general algebra proves"]},
        ],
    )


# ===========================================================================
# Practice bank
# ===========================================================================

def practice_bank():
    return [
        problem(
            "im3-u4-p1",
            "Convert $60^\\circ$ and $225^\\circ$ to radians.",
            "$60 \\cdot \\frac{\\pi}{180} = \\frac{\\pi}{3}$ and $225 \\cdot "
            "\\frac{\\pi}{180} = \\frac{5\\pi}{4}$.",
            ["Eq(60*pi/180, pi/3)", "Eq(225*pi/180, 5*pi/4)"],
        ),
        problem(
            "im3-u4-p2",
            "Convert $\\dfrac{11\\pi}{6}$ to degrees.",
            "$\\frac{11\\pi}{6} \\cdot \\frac{180}{\\pi} = \\frac{11 \\cdot 180}{6} = "
            "330^\\circ$.",
            ["Eq(Rational(11*180, 6), 330)"],
        ),
        problem(
            "im3-u4-p3",
            "Evaluate $\\sin\\dfrac{\\pi}{2} + \\cos\\pi + \\sin 0$.",
            "$1 + (-1) + 0 = 0$ — all three read straight off the axis points.",
            [
                "Eq(simplify(sin(pi/2) + cos(pi) + sin(0)), 0)",
                "Eq(1 - 1 + 0, 0)",
            ],
        ),
        problem(
            "im3-u4-p4",
            "Which angle in $[0, 2\\pi)$ is coterminal with $\\dfrac{17\\pi}{6}$?",
            "$\\frac{17\\pi}{6} - 2\\pi = \\frac{5\\pi}{6}$.",
            ["Eq(17*pi/6 - 2*pi, 5*pi/6)"],
        ),
        problem(
            "im3-u4-p5",
            "State the reference angle of $\\dfrac{5\\pi}{4}$ and of $\\dfrac{11\\pi}{6}$.",
            "$\\frac{5\\pi}{4} - \\pi = \\frac{\\pi}{4}$ (quadrant III), and "
            "$2\\pi - \\frac{11\\pi}{6} = \\frac{\\pi}{6}$ (quadrant IV).",
            ["Eq(5*pi/4 - pi, pi/4)", "Eq(2*pi - 11*pi/6, pi/6)"],
        ),
        problem(
            "im3-u4-p6",
            "Evaluate $\\cos\\dfrac{2\\pi}{3}$ exactly.",
            "Reference angle $\\frac{\\pi}{3}$, quadrant II, cosine negative: "
            "$-\\frac{1}{2}$.",
            ["Eq(pi - 2*pi/3, pi/3)", "Eq(simplify(cos(2*pi/3) + Rational(1, 2)), 0)"],
        ),
        problem(
            "im3-u4-p7",
            "Evaluate $\\sin\\dfrac{7\\pi}{4}$ exactly.",
            "Reference angle $\\frac{\\pi}{4}$, quadrant IV, sine negative: "
            "$-\\frac{\\sqrt{2}}{2}$.",
            ["Eq(2*pi - 7*pi/4, pi/4)", "Eq(simplify(sin(7*pi/4) + sqrt(2)/2), 0)"],
        ),
        problem(
            "im3-u4-p8",
            "Evaluate $\\tan\\dfrac{2\\pi}{3}$ exactly.",
            "Reference $\\frac{\\pi}{3}$ gives size $\\sqrt{3}$; quadrant II makes "
            "tangent negative: $-\\sqrt{3}$.",
            ["Eq(simplify(tan(2*pi/3) + sqrt(3)), 0)"],
        ),
        problem(
            "im3-u4-p9",
            "Find every $\\theta$ in $[0, 2\\pi)$ with $\\cos\\theta = \\dfrac{1}{2}$.",
            "Reference angle $\\frac{\\pi}{3}$; cosine is positive in quadrants I and "
            "IV: $\\theta = \\frac{\\pi}{3}$ or $\\theta = 2\\pi - \\frac{\\pi}{3} = "
            "\\frac{5\\pi}{3}$.",
            [
                "Eq(simplify(cos(pi/3) - Rational(1, 2)), 0)",
                "Eq(simplify(cos(5*pi/3) - Rational(1, 2)), 0)",
                "Eq(2*pi - pi/3, 5*pi/3)",
            ],
        ),
        problem(
            "im3-u4-p10",
            "State the amplitude, period and midline of $y = 2\\sin(3x) + 4$.",
            "Amplitude $2$; period $\\frac{2\\pi}{3}$; midline $y = 4$. The wave runs "
            "between $2$ and $6$.",
            ["Eq(Abs(2), 2)", "Eq(4 + 2, 6)", "Eq(4 - 2, 2)"],
        ),
        problem(
            "im3-u4-p11",
            "A wave has maximum $9$ and minimum $1$, and completes one cycle in "
            "$\\pi$. Write a cosine model starting at the maximum.",
            "Midline $\\frac{9 + 1}{2} = 5$, amplitude $\\frac{9 - 1}{2} = 4$, and "
            "period $\\pi$ needs $b = 2$: $y = 5 + 4\\cos(2x)$. Check: $y(0) = 9$ ✓.",
            [
                "Eq(Rational(9 + 1, 2), 5)",
                "Eq(Rational(9 - 1, 2), 4)",
                "Eq(2*pi/2, pi)",
                "Eq(5 + 4*1, 9)",
            ],
        ),
        problem(
            "im3-u4-p12",
            "What are the maximum and minimum values of $y = -3\\cos x + 2$, and at "
            "what $x$ in $[0, 2\\pi)$ does the maximum occur?",
            "Amplitude $3$ about midline $2$: max $5$, min $-1$. The flip means the "
            "wave starts at its MINIMUM; the maximum comes half a lap later, at "
            "$x = \\pi$, where $y = -3(-1) + 2 = 5$.",
            [
                "Eq(2 + Abs(-3), 5)",
                "Eq(2 - Abs(-3), -1)",
                "Eq(simplify(-3*cos(pi) + 2), 5)",
            ],
        ),
        problem(
            "im3-u4-p13",
            "Given $\\sin\\theta = \\dfrac{12}{13}$ with $\\theta$ in quadrant II, "
            "find $\\cos\\theta$.",
            "$\\cos^2\\theta = 1 - \\frac{144}{169} = \\frac{25}{169}$; quadrant II "
            "makes it negative: $-\\frac{5}{13}$.",
            [
                "Eq(1 - Rational(144, 169), Rational(25, 169))",
                "Eq(Rational(12, 13)**2 + Rational(5, 13)**2, 1)",
            ],
        ),
        problem(
            "im3-u4-p14",
            "Given $\\cos\\theta = -\\dfrac{3}{5}$ with $\\theta$ in quadrant III, "
            "find $\\tan\\theta$.",
            "$\\sin\\theta = -\\frac{4}{5}$ (quadrant III), so $\\tan\\theta = "
            "\\frac{-4/5}{-3/5} = \\frac{4}{3}$ — positive, as quadrant III demands.",
            [
                "Eq(Rational(3, 5)**2 + Rational(4, 5)**2, 1)",
                "Eq(Rational(-4, 5)/Rational(-3, 5), Rational(4, 3))",
            ],
        ),
        problem(
            "im3-u4-p15",
            "Simplify $\\dfrac{1 - \\cos^2\\theta}{\\sin\\theta}$ for "
            "$\\sin\\theta \\ne 0$.",
            "$1 - \\cos^2\\theta = \\sin^2\\theta$, so the quotient is "
            "$\\frac{\\sin^2\\theta}{\\sin\\theta} = \\sin\\theta$.",
            [
                "Eq(simplify((1 - cos(pi/3)**2)/sin(pi/3) - sin(pi/3)), 0)",
                "Eq(simplify(sin(pi/5)**2 + cos(pi/5)**2), 1)",
            ],
        ),
    ]


# ===========================================================================
# Test-yourself bank
# ===========================================================================

def test_bank():
    return [
        problem(
            "im3-u4-x1",
            "Convert $240^\\circ$ to radians and $\\dfrac{3\\pi}{2}$ to degrees.",
            "$240 \\cdot \\frac{\\pi}{180} = \\frac{4\\pi}{3}$, and "
            "$\\frac{3\\pi}{2} \\cdot \\frac{180}{\\pi} = 270^\\circ$.",
            ["Eq(240*pi/180, 4*pi/3)", "Eq(Rational(3*180, 2), 270)"],
        ),
        problem(
            "im3-u4-x2",
            "Evaluate $\\sin\\dfrac{4\\pi}{3}$ and $\\cos\\dfrac{7\\pi}{6}$ exactly.",
            "Both are quadrant III angles. References $\\frac{\\pi}{3}$ and "
            "$\\frac{\\pi}{6}$; both coordinates negative there: "
            "$\\sin\\frac{4\\pi}{3} = -\\frac{\\sqrt{3}}{2}$ and "
            "$\\cos\\frac{7\\pi}{6} = -\\frac{\\sqrt{3}}{2}$.",
            [
                "Eq(simplify(sin(4*pi/3) + sqrt(3)/2), 0)",
                "Eq(simplify(cos(7*pi/6) + sqrt(3)/2), 0)",
            ],
        ),
        problem(
            "im3-u4-x3",
            "Find every $\\theta$ in $[0, 2\\pi)$ with $\\sin\\theta = -\\dfrac{1}{2}$.",
            "Reference angle $\\frac{\\pi}{6}$; sine is negative in quadrants III and "
            "IV: $\\theta = \\pi + \\frac{\\pi}{6} = \\frac{7\\pi}{6}$ or "
            "$\\theta = 2\\pi - \\frac{\\pi}{6} = \\frac{11\\pi}{6}$.",
            [
                "Eq(pi + pi/6, 7*pi/6)",
                "Eq(2*pi - pi/6, 11*pi/6)",
                "Eq(simplify(sin(7*pi/6) + Rational(1, 2)), 0)",
                "Eq(simplify(sin(11*pi/6) + Rational(1, 2)), 0)",
            ],
        ),
        problem(
            "im3-u4-x4",
            "State the amplitude, period, midline, maximum and minimum of "
            "$y = -4\\sin\\left(\\dfrac{x}{3}\\right) + 1$.",
            "Amplitude $|-4| = 4$; period $\\frac{2\\pi}{1/3} = 6\\pi$; midline "
            "$y = 1$; maximum $5$ and minimum $-3$. The negative sign flips the wave "
            "but changes none of those numbers except the starting direction.",
            [
                "Eq(Abs(-4), 4)",
                "Eq(2*pi/Rational(1, 3), 6*pi)",
                "Eq(1 + 4, 5)",
                "Eq(1 - 4, -3)",
            ],
        ),
        problem(
            "im3-u4-x5",
            "A Ferris wheel's lowest car is $2$ m above the ground and its highest is "
            "$22$ m; one revolution takes $40$ seconds. Write a model for a car's "
            "height $t$ seconds after passing the BOTTOM.",
            "Midline $\\frac{22 + 2}{2} = 12$, amplitude $\\frac{22 - 2}{2} = 10$, "
            "period $40$ gives $b = \\frac{2\\pi}{40} = \\frac{\\pi}{20}$. Starting at "
            "the bottom wants an upside-down cosine: "
            "$h(t) = 12 - 10\\cos\\left(\\frac{\\pi}{20}t\\right)$. Check: "
            "$h(0) = 2$ ✓ and $h(20) = 12 - 10\\cos\\pi = 22$ ✓.",
            [
                "Eq(Rational(22 + 2, 2), 12)",
                "Eq(Rational(22 - 2, 2), 10)",
                "Eq(2*pi/(pi/20), 40)",
                "Eq(12 - 10*1, 2)",
                "Eq(simplify(12 - 10*cos(pi)), 22)",
            ],
        ),
        problem(
            "im3-u4-x6",
            "Given $\\cos\\theta = \\dfrac{8}{17}$ with $\\dfrac{3\\pi}{2} < \\theta "
            "< 2\\pi$, find $\\sin\\theta$ and $\\tan\\theta$.",
            "The interval is quadrant IV. $\\sin^2\\theta = 1 - \\frac{64}{289} = "
            "\\frac{225}{289}$, and sine is negative there: $\\sin\\theta = "
            "-\\frac{15}{17}$. Then $\\tan\\theta = \\frac{-15/17}{8/17} = "
            "-\\frac{15}{8}$.",
            [
                "Eq(1 - Rational(64, 289), Rational(225, 289))",
                "Eq(Rational(8, 17)**2 + Rational(15, 17)**2, 1)",
                "Eq(Rational(-15, 17)/Rational(8, 17), Rational(-15, 8))",
            ],
        ),
        problem(
            "im3-u4-x7",
            "Prove that $\\dfrac{\\sin^2\\theta}{1 + \\cos\\theta} = 1 - \\cos\\theta$ "
            "whenever $\\cos\\theta \\ne -1$.",
            "Replace $\\sin^2\\theta$ by $1 - \\cos^2\\theta$ and factor the "
            "difference of squares: $\\frac{(1 - \\cos\\theta)(1 + \\cos\\theta)}"
            "{1 + \\cos\\theta} = 1 - \\cos\\theta$, cancelling the nonzero factor. "
            "Every step is an identity, so the equation holds for every allowed "
            "$\\theta$ — the excluded $\\cos\\theta = -1$ is exactly where the "
            "cancelled factor would have been zero.",
            [
                "Eq(expand((1 - c)*(1 + c)), 1 - c**2)",
                "Eq(simplify(sin(pi/3)**2/(1 + cos(pi/3)) - (1 - cos(pi/3))), 0)",
                "Eq(simplify(sin(2*pi/3)**2/(1 + cos(2*pi/3)) - (1 - cos(2*pi/3))), 0)",
            ],
        ),
        problem(
            "im3-u4-x8",
            "The angle $\\theta = \\dfrac{29\\pi}{6}$ has been wound more than twice "
            "around the circle. Evaluate $\\cos\\theta$ exactly, showing the "
            "unwinding.",
            "Strip full turns: $\\frac{29\\pi}{6} - 2\\pi = \\frac{17\\pi}{6}$, and "
            "again: $\\frac{17\\pi}{6} - 2\\pi = \\frac{5\\pi}{6}$. So the point is "
            "that of $\\frac{5\\pi}{6}$: reference angle $\\frac{\\pi}{6}$ in quadrant "
            "II, cosine negative — $\\cos\\frac{29\\pi}{6} = -\\frac{\\sqrt{3}}{2}$.",
            [
                "Eq(29*pi/6 - 4*pi, 5*pi/6)",
                "Eq(simplify(cos(29*pi/6) + sqrt(3)/2), 0)",
                "Eq(simplify(cos(29*pi/6) - cos(5*pi/6)), 0)",
            ],
        ),
    ]


def main():
    write_unit(
        course=COURSE,
        slug="trigonometric-functions",
        title="Trigonometric Functions",
        unit_number=4,
        blurb=(
            "Radian measure and the unit circle, extending the ratios beyond acute "
            "angles, the graphs of sine and cosine with amplitude and period, and the "
            "Pythagorean identity."
        ),
        builds_on=(
            "Right-triangle trigonometry from IM2 Unit 6 and radians from IM2 Unit 7 — "
            "the triangle's ratios become coordinates on the unit circle, and suddenly "
            "every angle has a sine and cosine."
        ),
        lessons=[
            lesson_unit_circle(),
            lesson_reference(),
            lesson_graphs(),
            lesson_identity(),
        ],
        practice=practice_bank(),
        test=test_bank(),
    )


if __name__ == "__main__":
    main()
