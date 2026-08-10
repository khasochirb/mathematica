#!/usr/bin/env python3
"""SAT Math — Geometry and Trigonometry, Units 1-2.

Builds:
  data/genmath/sat/area-and-volume.json
  data/genmath/sat/lines-angles-and-triangles.json

Run: python3 scripts/sat/build_geo_1_2.py   (then npm run verify:genmath)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "sat"
AV_TAG = {"text": "sat-area-volume", "mono": True}
LAT_TAG = {"text": "sat-lines-angles-triangles", "mono": True}


def _b(tag, level):
    return [tag, {"text": level}]


# ===========================================================================
# UNIT 1 — Area and volume formulas
# ===========================================================================

def lesson_area():
    worked = [
        problem(
            "sat-av1-w1",
            "A trapezoid has parallel sides of length $8$ and $14$ and a height of $6$. What "
            "is its area?",
            "**Answer.** $66$.  \n"
            "The trapezoid formula averages the two parallel sides and multiplies by the "
            "height:\n"
            "$$A = \\frac{b_1 + b_2}{2} \\cdot h = \\frac{8 + 14}{2} \\cdot 6 = 11 \\cdot 6 = 66$$\n"
            "The averaging is what makes it work. A trapezoid is a rectangle of width $11$ — "
            "the average of the two bases — with a triangle shaved off one end and pasted onto "
            "the other.  \n"
            "Note the HEIGHT is the perpendicular distance between the parallel sides, not the "
            "length of a slanted side. SAT diagrams routinely label a slanted side as well, "
            "specifically so that using it gives a listed wrong answer.",
            [
                "Eq(Rational(8 + 14, 2)*6, 66)",
                "Eq(Rational(8 + 14, 2), 11)",
            ],
        ),
        problem(
            "sat-av1-w2",
            "A cylinder has radius $3$ and height $10$. What is its volume, in terms of "
            "$\\pi$?",
            "**Answer.** $90\\pi$.  \n"
            "Every prism and cylinder has the same volume rule: the area of the base times the "
            "height.\n"
            "$$V = \\pi r^{2} h = \\pi(3)^{2}(10) = 90\\pi$$\n"
            "The step that costs points is squaring the radius BEFORE multiplying: "
            "$3^{2} = 9$, then $9 \\times 10 = 90$. Multiplying $3 \\times 10$ first and then "
            "squaring gives $900\\pi$, which is on the option list.  \n"
            "This formula is on the SAT's reference sheet, along with the volumes of a cone, a "
            "sphere and a pyramid. There is nothing to memorise — but you do have to know "
            "which sheet entry matches the solid in front of you, and that the sheet gives "
            "$r$, not the diameter.",
            [
                "Eq(3**2*10, 90)",
                "Ne(3*10, 90)",
                "Eq((3*10)**2, 900)",
            ],
        ),
        problem(
            "sat-av1-w3",
            "A rectangular box has dimensions $4$ by $5$ by $6$. Each dimension is doubled. By "
            "what factor does the volume increase?",
            "**Answer.** $8$.  \n"
            "The original volume is $4 \\times 5 \\times 6 = 120$. Doubling every dimension "
            "gives $8 \\times 10 \\times 12 = 960$, and\n"
            "$$\\frac{960}{120} = 8$$\n"
            "The reason is structural, not arithmetic: volume is a product of THREE lengths, "
            "so doubling each one multiplies the result by $2 \\times 2 \\times 2 = 8$.  \n"
            "The same logic covers every scaling question. Area is a product of two lengths, "
            "so scaling by $k$ multiplies area by $k^{2}$; volume scales by $k^{3}$. Tripling "
            "the dimensions of a solid multiplies its volume by $27$, not by $3$ — and $3$ is "
            "always an option.",
            [
                "Eq(4*5*6, 120)",
                "Eq(8*10*12, 960)",
                "Eq(Rational(960,120), 8)",
                "Eq(2**3, 8)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-av1-t1",
            "A triangle has base $12$ and height $7$. What is its area?",
            "**Answer.** $42$. $A = \\frac{1}{2}bh = \\frac{1}{2}(12)(7) = 42$. Forgetting the "
            "half gives $84$, a listed option.",
            ["Eq(Rational(1,2)*12*7, 42)", "Eq(12*7, 84)"],
        ),
        problem(
            "sat-av1-t2",
            "A circle has diameter $10$. What is its area, in terms of $\\pi$?",
            "**Answer.** $25\\pi$. The radius is half the diameter, so $r = 5$ and "
            "$A = \\pi r^{2} = 25\\pi$. Using the diameter in place of the radius gives "
            "$100\\pi$ — the single most common error in circle questions.",
            ["Eq(Rational(10,2), 5)", "Eq(5**2, 25)", "Eq(10**2, 100)"],
        ),
        problem(
            "sat-av1-t3",
            "A cone has radius $6$ and height $5$. What is its volume, in terms of $\\pi$?",
            "**Answer.** $60\\pi$. The reference sheet gives $V = \\frac{1}{3}\\pi r^{2}h$, so "
            "$\\frac{1}{3}\\pi(36)(5) = 60\\pi$. Dropping the third gives $180\\pi$ — the "
            "volume of the cylinder the cone sits inside.",
            ["Eq(Rational(1,3)*6**2*5, 60)", "Eq(6**2*5, 180)"],
        ),
        problem(
            "sat-av1-t4",
            "The side length of a square is multiplied by $5$. By what factor does its area "
            "increase?",
            "**Answer.** $25$. Area is a product of two lengths, so scaling each by $5$ "
            "multiplies the area by $5^{2} = 25$. A square of side $2$ has area $4$; of side "
            "$10$, area $100$.",
            ["Eq(5**2, 25)", "Eq(Rational(10**2, 2**2), 25)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Area and volume formulas",
            "beats": [
                "Domain: Geometry and Trigonometry — 5 to 7 of the 44 questions.",
                "The reference sheet gives you the formulas; it does not tell you which to use.",
                "Prerequisite: solving a linear equation, and squaring.",
                "The scaling rule — area by k², volume by k³ — is the reliably hard part.",
            ],
        },
        {
            "kind": "areaShape",
            "title": "Why a trapezoid averages its bases",
            "teach": "Drag the top base. When it matches the bottom you have a rectangle; when "
                     "it shrinks to nothing you have a triangle. The formula — average the two "
                     "bases, multiply by the height — gives the right answer at both extremes "
                     "and everywhere between.",
            "config": {"shape": "trapezoid", "base": 14, "base2": 8, "height": 6},
        },
        {"kind": "worked", "title": "A trapezoid, and which length is the height", "problemId": "sat-av1-w1"},
        {
            "kind": "tapQuestion",
            "title": "Radius or diameter?",
            "prompt": "A circle has diameter $14$. What is its area, in terms of $\\pi$?",
            "options": ["$49\\pi$", "$196\\pi$", "$14\\pi$", "$28\\pi$"],
            "correctIndex": 0,
            "explanation": "The radius is $7$, so the area is $\\pi(7)^{2} = 49\\pi$. Option B "
                           "squares the diameter instead — the commonest circle error on the "
                           "test. Option D is the circumference, $\\pi d$.",
            "check": ["Eq(Rational(14,2), 7)", "Eq(7**2, 49)", "Eq(14**2, 196)"],
        },
        {
            "kind": "solid3d",
            "title": "Base area, times height",
            "teach": "Every prism and cylinder works the same way: find the area of the base, "
                     "then multiply by how tall it is. Rotate the solid and change its "
                     "dimensions to see which measurement plays which role.",
            "config": {"solid": "cylinder", "r": 3, "h": 10},
        },
        {"kind": "worked", "title": "A cylinder from the reference sheet", "problemId": "sat-av1-w2"},
        {
            "kind": "tip",
            "title": "Scaling: squared for area, cubed for volume",
            "body": "Multiply every length of a figure by $k$ and its area multiplies by "
                    "$k^{2}$, because area is two lengths multiplied together. Volume "
                    "multiplies by $k^{3}$. Doubling a box's dimensions gives eight times the "
                    "volume, not twice — and 'twice' is always an option.",
        },
        {"kind": "worked", "title": "What doubling really does", "problemId": "sat-av1-w3"},
        {"kind": "tryIt", "title": "Your turn: mind the half", "problemId": "sat-av1-t1"},
        {"kind": "tryIt", "title": "Your turn: diameter given", "problemId": "sat-av1-t2"},
        {"kind": "tryIt", "title": "Your turn: a cone", "problemId": "sat-av1-t3"},
        {"kind": "tryIt", "title": "Your turn: scale a square", "problemId": "sat-av1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "The reference sheet has the formulas — your job is picking the right one.",
                "Formulas use the RADIUS; halve any diameter before substituting.",
                "A trapezoid's height is perpendicular to the parallel sides, not a slanted edge.",
                "Prism and cylinder volume is base area times height, every time.",
                "Scale every length by k: area goes up by k², volume by k³.",
            ],
        },
    ]

    return lesson(
        slug="area-and-volume-formulas",
        title="Area, Volume and What Scaling Does",
        concrete=(
            "A pizza twice the diameter of another is not twice the pizza — it is four times "
            "the pizza, for rather less than twice the price. Area grows with the square of "
            "the scaling, and noticing that is worth more on this test than any formula."
        ),
        objective=(
            "Choose and apply the right area or volume formula, distinguish radius from "
            "diameter and height from slant, and predict how area and volume change when "
            "dimensions are scaled."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Area and volume formulas*, in the "
            "**Geometry and Trigonometry** domain — the smallest domain, at 5 to 7 of the 44 "
            "questions. The reference sheet supplies the formulas, so nothing here needs "
            "memorising; what it does not supply is which formula matches the solid in front "
            "of you.",
            "Three habits prevent most of the lost marks. Formulas take the RADIUS, so halve "
            "any diameter before substituting. A height is always perpendicular — the "
            "perpendicular distance between a trapezoid's parallel sides, or from a cone's "
            "apex straight down to its base — and never a slanted edge, which SAT diagrams "
            "helpfully label as well. And square before you multiply: $\\pi r^{2}h$ squares "
            "only the $r$.",
            "Every prism and cylinder shares one rule: volume is the area of the base times "
            "the height. Cones and pyramids are a third of the prism or cylinder they fit "
            "inside, which is why their formulas carry a $\\frac{1}{3}$.",
            "**The test's angle.** Scaling. Multiply every length of a figure by $k$ and its "
            "area multiplies by $k^{2}$, because area is a product of two lengths; volume "
            "multiplies by $k^{3}$. Doubling a box's dimensions gives EIGHT times the volume. "
            "The linear answer — 'twice' — is on every version of this question, and it is the "
            "one most students choose.",
        ],
        key_idea=(
            "Pick the formula, substitute the radius rather than the diameter and the "
            "perpendicular height rather than a slant, and remember that scaling lengths by "
            "$k$ scales area by $k^{2}$ and volume by $k^{3}$."
        ),
        facts=[
            fact(
                "Trapezoid",
                "A = \\frac{b_1 + b_2}{2} \\cdot h",
                "Average the parallel sides, multiply by the perpendicular height.",
            ),
            fact(
                "Prisms and cylinders",
                "V = (\\text{base area}) \\times h, \\qquad V_{\\text{cylinder}} = \\pi r^{2} h",
                "Cones and pyramids are a third of the solid they fit inside.",
            ),
            fact(
                "Scaling",
                "\\text{lengths} \\times k \\;\\Longrightarrow\\; \\text{area} \\times k^{2}, \\;\\; \\text{volume} \\times k^{3}",
                "Two lengths make an area, three make a volume — the exponents are just the "
                "count.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Substituting the diameter where the formula wants the radius.",
                "$\\pi d^{2}$ is four times the true area. Halve first.",
            ),
            mistake(
                "Using a slanted side as the height.",
                "Height is the perpendicular distance. The slant is given for surface area, "
                "not volume.",
            ),
            mistake(
                "Assuming doubling the dimensions doubles the volume.",
                "It multiplies it by $2^{3} = 8$. Area would go up by $4$.",
            ),
            mistake(
                "Dropping the $\\frac{1}{3}$ from a cone or pyramid.",
                "Without it you have computed the cylinder or prism the solid sits inside.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_composite():
    worked = [
        problem(
            "sat-av2-w1",
            "A running track is made of a rectangle $80$ metres long and $40$ metres wide with "
            "a semicircle attached to each of the two shorter ends. What is the total area, in "
            "terms of $\\pi$?",
            "**Answer.** $3200 + 400\\pi$ square metres.  \n"
            "Break the shape into pieces whose formulas you know, compute each, and add.  \n"
            "The rectangle:\n"
            "$$80 \\times 40 = 3200$$\n"
            "The two semicircles are attached to the $40$-metre ends, so each has DIAMETER "
            "$40$ and therefore radius $20$. Two semicircles make one whole circle:\n"
            "$$\\pi(20)^{2} = 400\\pi$$\n"
            "$$\\text{total} = 3200 + 400\\pi$$\n"
            "Two things decide this question. The semicircles sit on the SHORTER sides, so "
            "$40$ is the diameter and $20$ is the radius — using $40$ as the radius gives "
            "$1600\\pi$, four times too much. And two halves make one whole, so there is no "
            "factor of $\\frac{1}{2}$ left anywhere.",
            [
                "Eq(80*40, 3200)",
                "Eq(Rational(40,2), 20)",
                "Eq(20**2, 400)",
                "Eq(2*Rational(1,2), 1)",
                "Eq(40**2, 1600)",
            ],
        ),
        problem(
            "sat-av2-w2",
            "A rectangular sheet of card measures $30$ by $20$ centimetres. A square of side "
            "$4$ is cut from each corner and the flaps are folded up to make an open box. What "
            "is the volume of the box?",
            "**Answer.** $1{,}056$ cubic centimetres.  \n"
            "The folded height is the size of the cut square:\n"
            "$$h = 4$$\n"
            "Each base dimension loses TWO squares — one at each end:\n"
            "$$\\text{length} = 30 - 2(4) = 22, \\qquad \\text{width} = 20 - 2(4) = 12$$\n"
            "$$V = 22 \\times 12 \\times 4 = 1056$$\n"
            "Subtracting only one square from each dimension gives $26 \\times 16 \\times 4 = "
            "1664$, which is a listed option. The corners are cut from both ends of every "
            "side, so the loss is doubled.  \n"
            "This is the SAT's standard composite-solid item: the difficulty is the geometry "
            "of what was removed, not the volume formula.",
            [
                "Eq(30 - 2*4, 22)",
                "Eq(20 - 2*4, 12)",
                "Eq(22*12*4, 1056)",
                "Eq((30 - 4)*(20 - 4)*4, 1664)",
            ],
        ),
        problem(
            "sat-av2-w3",
            "A cylindrical tank of radius $2$ metres and height $5$ metres is being filled at "
            "$3$ cubic metres per minute. How long does it take to fill, to the nearest "
            "minute?",
            "**Answer.** About $21$ minutes.  \n"
            "Find the volume, then divide by the rate:\n"
            "$$V = \\pi r^{2} h = \\pi(4)(5) = 20\\pi \\approx 62.83 \\text{ m}^{3}$$\n"
            "$$t = \\frac{62.83}{3} \\approx 20.9 \\text{ minutes}$$\n"
            "so about $21$ minutes.  \n"
            "The units are the check. Cubic metres divided by cubic metres per minute leaves "
            "minutes, which is what was asked for. If a rate question ever produces the wrong "
            "unit, the division is the wrong way round — multiplying here would give "
            "$188$, a number with no meaning.  \n"
            "Note also that the answer is left as a decimal rather than in terms of $\\pi$, "
            "because the question asked for a number of minutes.",
            [
                "Eq(2**2*5, 20)",
                "Abs(20*pi - 62.83) < 0.01",
                "Abs(20*pi/3 - 20.94) < 0.01",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-av2-t1",
            "A shape is made of a $10$ by $6$ rectangle with a semicircle of diameter $6$ "
            "attached to one short side. What is its area, in terms of $\\pi$?",
            "**Answer.** $60 + 4.5\\pi$. The rectangle is $60$; the semicircle has radius "
            "$3$, so its area is $\\frac{1}{2}\\pi(9) = 4.5\\pi$.",
            ["Eq(10*6, 60)", "Eq(Rational(6,2), 3)", "Eq(Rational(1,2)*3**2, Rational(9,2))"],
        ),
        problem(
            "sat-av2-t2",
            "A square of side $12$ has a circle of radius $4$ cut out of its centre. What area "
            "remains, in terms of $\\pi$?",
            "**Answer.** $144 - 16\\pi$. Subtract the removed piece from the whole: "
            "$12^{2} - \\pi(4)^{2}$.",
            ["Eq(12**2, 144)", "Eq(4**2, 16)"],
        ),
        problem(
            "sat-av2-t3",
            "A rectangular pool $8$ by $5$ metres is $1.5$ metres deep and is filled at $2$ "
            "cubic metres per minute. How long does filling take?",
            "**Answer.** $30$ minutes. The volume is $8 \\times 5 \\times 1.5 = 60$ cubic "
            "metres, and $\\frac{60}{2} = 30$.",
            ["Eq(8*5*Rational(15,10), 60)", "Eq(Rational(60,2), 30)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Split it, compute it, combine it",
            "body": "A composite figure is not a new formula — it is two or three shapes you "
                    "already know, added together or subtracted from each other. Draw the "
                    "dividing line, name each piece, compute each area or volume separately, "
                    "and then add or subtract. The only real work is deciding which "
                    "dimensions each piece actually has.",
        },
        {
            "kind": "compositeArea",
            "title": "One shape, two pieces",
            "teach": "The figure splits into a rectangle and a triangle. Compute each piece "
                     "with its own formula and add — and notice that the pieces do not share "
                     "all their dimensions, which is where composite questions get their "
                     "difficulty.",
            "config": {
                "width": 10,
                "height": 6,
                "parts": [
                    {"kind": "rect", "x": 0, "y": 0, "w": 10, "h": 4, "label": "rectangle"},
                    {"kind": "tri", "x": 0, "y": 4, "w": 10, "h": 2, "label": "triangle"},
                ],
                "total": "40 + 10 = 50",
                "caption": "A rectangle with a triangular roof.",
            },
        },
        {"kind": "worked", "title": "A track: rectangle plus circle", "problemId": "sat-av2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which dimension is the radius?",
            "prompt": "A semicircle is attached to the $12$-metre side of a rectangle. What is "
                      "the semicircle's radius?",
            "options": ["$6$", "$12$", "$24$", "$\\pi \\cdot 12$"],
            "correctIndex": 0,
            "explanation": "The side it sits on is the DIAMETER, so the radius is half of it: "
                           "$6$. Using $12$ as the radius makes the semicircle four times too "
                           "large, and that is the standard error on composite-shape questions.",
            "check": ["Eq(Rational(12,2), 6)", "Eq(6**2*4, 12**2)"],
        },
        {"kind": "worked", "title": "A box folded from a sheet", "problemId": "sat-av2-w2"},
        {
            "kind": "tip",
            "title": "Let the units check the arithmetic",
            "body": "When a volume question ends in a rate, divide and watch the units cancel: "
                    "cubic metres divided by cubic metres per minute leaves minutes. If your "
                    "answer comes out in the wrong unit, the division was the wrong way round "
                    "— and the wrong-way answer is always on the option list.",
        },
        {"kind": "worked", "title": "Volume, then a rate", "problemId": "sat-av2-w3"},
        {"kind": "tryIt", "title": "Your turn: rectangle plus semicircle", "problemId": "sat-av2-t1"},
        {"kind": "tryIt", "title": "Your turn: subtract the hole", "problemId": "sat-av2-t2"},
        {"kind": "tryIt", "title": "Your turn: fill a pool", "problemId": "sat-av2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Split a composite figure into shapes you know, then add or subtract.",
                "A semicircle sitting on a side has that side as its DIAMETER.",
                "Cutting corners from a sheet removes two lengths from every dimension.",
                "Two semicircles of equal radius make one whole circle.",
                "Divide a volume by a rate and check that the units leave you with time.",
            ],
        },
    ]

    return lesson(
        slug="composite-figures-and-volume-in-context",
        title="Composite Figures and Volume in Context",
        concrete=(
            "A running track is a rectangle with a half-circle stuck on each end. Nobody has a "
            "formula for that shape, and nobody needs one — it is two shapes that do have "
            "formulas, added together."
        ),
        objective=(
            "Find areas and volumes of composite figures by splitting them into known shapes, "
            "and combine a volume with a rate to answer a question about time."
        ),
        concept=[
            "**Skill card.** Still *Area and volume formulas*, in the **Geometry and "
            "Trigonometry** domain. Composite figures are how the harder items in this "
            "subtopic are written, because they test whether you can read a diagram rather "
            "than recall a formula.",
            "The method never changes: split the figure into shapes you already have formulas "
            "for, compute each separately, and add — or, when something has been removed, "
            "subtract. Drawing the dividing line on the diagram is the first move.",
            "The difficulty is always in the dimensions rather than the formulas. A semicircle "
            "attached to a side has that side as its DIAMETER, so the radius is half of it. "
            "Squares cut from the corners of a sheet remove two lengths from every dimension, "
            "not one, because there is a corner at each end.",
            "**The test's angle.** Volume combined with a rate. Find the volume, then divide "
            "by the filling or draining rate, and let the units confirm the direction: cubic "
            "metres divided by cubic metres per minute leaves minutes. Multiplying instead "
            "produces a number in the wrong unit entirely — and that number is on the option "
            "list.",
        ],
        key_idea=(
            "Composite figures are known shapes added or subtracted. The formulas are easy; "
            "the dimensions each piece actually has are what the question is testing."
        ),
        facts=[
            fact(
                "Composite area",
                "A_{\\text{total}} = A_1 + A_2 - A_{\\text{removed}}",
                "Split, compute, combine. Nothing new is needed beyond the basic formulas.",
            ),
            fact(
                "A semicircle on a side",
                "\\text{side} = \\text{diameter} \\;\\Longrightarrow\\; r = \\tfrac{1}{2}\\text{side}",
                "Using the side as the radius makes the piece four times too large.",
            ),
            fact(
                "Volume and a rate",
                "t = \\frac{V}{\\text{rate}}",
                "The units cancel to leave time. If they do not, the division is inverted.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Using the side a semicircle sits on as its radius.",
                "That side is the diameter. Halve it first, or the area comes out four times "
                "too big.",
            ),
            mistake(
                "Subtracting one corner square from each dimension instead of two.",
                "Corners are cut from both ends of every side, so each dimension loses twice "
                "the cut length.",
            ),
            mistake(
                "Leaving a half in place after combining two semicircles.",
                "Two semicircles of equal radius make one whole circle, with no fraction left.",
            ),
            mistake(
                "Multiplying a volume by a rate instead of dividing.",
                "The units give it away: the result would be cubic metres squared per minute, "
                "which is not a time.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


AV_PRACTICE = [
    problem(
        "sat-av-p01",
        "A rectangle has length $9$ and width $4$. What is its area?",
        "**Answer.** $36$.",
        ["Eq(9*4, 36)"],
        badges=_b(AV_TAG, "Easy"),
    ),
    problem(
        "sat-av-p02",
        "A circle has radius $8$. What is its circumference, in terms of $\\pi$?",
        "**Answer.** $16\\pi$. Circumference is $2\\pi r$. The area would be $64\\pi$, and "
        "confusing the two is the standard slip.",
        ["Eq(2*8, 16)", "Eq(8**2, 64)"],
        badges=_b(AV_TAG, "Easy"),
    ),
    problem(
        "sat-av-p03",
        "A triangle has area $54$ and base $12$. What is its height?",
        "**Answer.** $9$. From $54 = \\frac{1}{2}(12)h$ we get $54 = 6h$, so $h = 9$.",
        ["Eq(Rational(1,2)*12*9, 54)"],
        badges=_b(AV_TAG, "Easy"),
    ),
    problem(
        "sat-av-p04",
        "A rectangular prism has volume $180$ and a base measuring $5$ by $6$. What is its "
        "height?",
        "**Answer.** $6$. The base area is $30$, and $\\frac{180}{30} = 6$.",
        ["Eq(5*6, 30)", "Eq(Rational(180,30), 6)", "Eq(5*6*6, 180)"],
        badges=_b(AV_TAG, "Medium"),
    ),
    problem(
        "sat-av-p05",
        "A sphere has radius $3$. What is its volume, in terms of $\\pi$?",
        "**Answer.** $36\\pi$. The reference sheet gives $V = \\frac{4}{3}\\pi r^{3}$, so "
        "$\\frac{4}{3}\\pi(27) = 36\\pi$.",
        ["Eq(Rational(4,3)*3**3, 36)"],
        badges=_b(AV_TAG, "Medium"),
    ),
    problem(
        "sat-av-p06",
        "The dimensions of a cylinder are all tripled. By what factor does its volume "
        "increase?",
        "**Answer.** $27$. Volume scales by the cube of the linear factor: $3^{3} = 27$. "
        "Check with $r = 1$, $h = 1$ against $r = 3$, $h = 3$: $\\pi$ against $27\\pi$.",
        ["Eq(3**3, 27)", "Eq(Rational(3**2*3, 1**2*1), 27)"],
        badges=_b(AV_TAG, "Hard"),
    ),
    problem(
        "sat-av-p07",
        "A trapezoid has parallel sides $5$ and $11$ and area $48$. What is its height?",
        "**Answer.** $6$. The average base is $8$, so $8h = 48$ and $h = 6$.",
        ["Eq(Rational(5 + 11, 2), 8)", "Eq(8*6, 48)"],
        badges=_b(AV_TAG, "Medium"),
    ),
    problem(
        "sat-av-p08",
        "A square garden of side $20$ metres has a path $2$ metres wide running around the "
        "inside of its border. What is the area of the path?",
        "**Answer.** $144$ square metres. The inner region is a square of side "
        "$20 - 2(2) = 16$, so the path is $20^{2} - 16^{2} = 400 - 256 = 144$. Subtracting "
        "only one path width from each side — giving an inner side of $18$ — is the standard "
        "error, because the path runs along BOTH opposite edges.",
        ["Eq(20 - 2*2, 16)", "Eq(20**2 - 16**2, 144)", "Ne(20**2 - 18**2, 144)"],
        badges=_b(AV_TAG, "Hard"),
    ),
]

AV_TEST = [
    problem(
        "sat-av-x01",
        "A circle has radius $6$. What is its area, in terms of $\\pi$?",
        "**Answer.** $36\\pi$.",
        ["Eq(6**2, 36)"],
        badges=_b(AV_TAG, "Easy"),
    ),
    problem(
        "sat-av-x02",
        "A cylinder has diameter $8$ and height $7$. What is its volume, in terms of $\\pi$?",
        "**Answer.** $112\\pi$. The radius is $4$, so $V = \\pi(16)(7) = 112\\pi$. Using the "
        "diameter gives $448\\pi$.",
        ["Eq(Rational(8,2), 4)", "Eq(4**2*7, 112)", "Eq(8**2*7, 448)"],
        badges=_b(AV_TAG, "Medium"),
    ),
    problem(
        "sat-av-x03",
        "A pyramid has a square base of side $6$ and height $10$. What is its volume?",
        "**Answer.** $120$. The base area is $36$, and "
        "$V = \\frac{1}{3}(36)(10) = 120$.",
        ["Eq(6**2, 36)", "Eq(Rational(1,3)*36*10, 120)"],
        badges=_b(AV_TAG, "Medium"),
    ),
    problem(
        "sat-av-x04",
        "Two similar rectangles have corresponding sides in the ratio $2 : 5$. What is the "
        "ratio of their areas?",
        "**Answer.** $4 : 25$. Area scales by the square of the linear ratio. Answering "
        "$2 : 5$ is the standard error.",
        ["Eq(2**2, 4)", "Eq(5**2, 25)", "Eq(Rational(4,25), Rational(2,5)**2)"],
        badges=_b(AV_TAG, "Hard"),
    ),
    problem(
        "sat-av-x05",
        "A rectangular tank measures $3$ by $4$ by $2$ metres and is half full. How many cubic "
        "metres of water does it hold?",
        "**Answer.** $12$. The full volume is $24$ cubic metres, and half of that is $12$.",
        ["Eq(3*4*2, 24)", "Eq(Rational(24,2), 12)"],
        badges=_b(AV_TAG, "Easy"),
    ),
    problem(
        "sat-av-x06",
        "A cone and a cylinder have the same radius and the same height. The cylinder's volume "
        "is $150$. What is the cone's?",
        "**Answer.** $50$. A cone is exactly one third of the cylinder it fits inside, "
        "whatever the radius and height are, so no dimensions are needed.",
        ["Eq(Rational(150,3), 50)", "Eq(Rational(1,3)*150, 50)"],
        badges=_b(AV_TAG, "Medium"),
    ),
]


# ===========================================================================
# UNIT 2 — Lines, angles and triangles
# ===========================================================================

def lesson_angles():
    worked = [
        problem(
            "sat-la1-w1",
            "Two parallel lines are cut by a transversal. One of the angles measures "
            "$68^\\circ$. What are the possible measures of the other angles formed?",
            "**Answer.** $68^\\circ$ and $112^\\circ$.  \n"
            "When a transversal crosses two parallel lines it makes eight angles, and there "
            "are only ever TWO different sizes among them. Every angle is either equal to "
            "$68^\\circ$ or supplementary to it:\n"
            "$$180^\\circ - 68^\\circ = 112^\\circ$$\n"
            "Which angles are which is easy to see rather than memorise: angles that look the "
            "same size ARE the same size, and any two that together form a straight line add "
            "to $180^\\circ$.  \n"
            "The formal names — corresponding, alternate interior, alternate exterior, "
            "vertical — all describe pairs that are equal. Same-side interior angles and "
            "linear pairs are the supplementary ones. But on the test the two-sizes fact is "
            "faster and cannot be misremembered.",
            ["Eq(180 - 68, 112)", "Eq(68 + 112, 180)"],
        ),
        problem(
            "sat-la1-w2",
            "In a triangle, one angle measures $43^\\circ$ and another measures $71^\\circ$. "
            "What is the measure of the exterior angle at the third vertex?",
            "**Answer.** $114^\\circ$.  \n"
            "The third interior angle follows from the angle sum:\n"
            "$$180^\\circ - 43^\\circ - 71^\\circ = 66^\\circ$$\n"
            "An exterior angle sits on a straight line with its interior angle, so\n"
            "$$180^\\circ - 66^\\circ = 114^\\circ$$\n"
            "There is a one-step route. An exterior angle always equals the sum of the two "
            "NON-adjacent interior angles:\n"
            "$$43^\\circ + 71^\\circ = 114^\\circ$$\n"
            "That shortcut is worth knowing — it skips the third angle entirely, and it "
            "follows directly from the two facts above, since both routes subtract the same "
            "third angle from $180^\\circ$.  \n"
            "The trap is answering $66^\\circ$, the interior angle, which the first route "
            "computes on the way past.",
            [
                "Eq(180 - 43 - 71, 66)",
                "Eq(180 - 66, 114)",
                "Eq(43 + 71, 114)",
            ],
        ),
        problem(
            "sat-la1-w3",
            "Triangle $ABC$ is isosceles with $AB = AC$, and the angle at $A$ measures "
            "$40^\\circ$. What is the measure of the angle at $B$?",
            "**Answer.** $70^\\circ$.  \n"
            "In an isosceles triangle the angles OPPOSITE the equal sides are equal. Sides "
            "$AB$ and $AC$ are equal, so the angles opposite them — at $C$ and at $B$ — are "
            "equal to each other. Call each of them $x$:\n"
            "$$40 + x + x = 180$$\n"
            "$$2x = 140$$\n"
            "$$x = 70$$\n"
            "So both base angles measure $70^\\circ$.  \n"
            "Getting the pairing right is the whole difficulty. The equal angles are not "
            "adjacent to the equal sides — they are opposite them. Here the equal sides both "
            "meet at $A$, so $A$ is the ODD angle out and the two base angles are the equal "
            "pair. Assuming the $40^\\circ$ is one of the equal pair gives $100^\\circ$, a "
            "listed option.",
            [
                "Eq(40 + 70 + 70, 180)",
                "Eq(Rational(180 - 40, 2), 70)",
                "Eq(180 - 40 - 40, 100)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-la1-t1",
            "Two angles form a linear pair and one measures $37^\\circ$. What is the other?",
            "**Answer.** $143^\\circ$. A linear pair lies along a straight line, so the two "
            "add to $180^\\circ$.",
            ["Eq(180 - 37, 143)"],
        ),
        problem(
            "sat-la1-t2",
            "A triangle has angles measuring $x$, $2x$ and $3x$ degrees. What is the largest "
            "angle?",
            "**Answer.** $90^\\circ$. The angles sum to $180$, so $6x = 180$ and $x = 30$; "
            "the largest is $3x = 90^\\circ$. The triangle is right-angled.",
            ["Eq(6*30, 180)", "Eq(3*30, 90)", "Eq(30 + 60 + 90, 180)"],
        ),
        problem(
            "sat-la1-t3",
            "Parallel lines are cut by a transversal, and two same-side interior angles are "
            "$(3x)^\\circ$ and $(2x + 20)^\\circ$. What is $x$?",
            "**Answer.** $32$. Same-side interior angles are supplementary: "
            "$3x + 2x + 20 = 180$, so $5x = 160$ and $x = 32$. The two angles are $96^\\circ$ "
            "and $84^\\circ$, which do sum to $180^\\circ$.",
            ["Eq(5*32 + 20, 180)", "Eq(3*32, 96)", "Eq(2*32 + 20, 84)", "Eq(96 + 84, 180)"],
        ),
        problem(
            "sat-la1-t4",
            "An isosceles triangle has a base angle of $55^\\circ$. What is the apex angle?",
            "**Answer.** $70^\\circ$. Both base angles measure $55^\\circ$, so the apex is "
            "$180 - 55 - 55 = 70^\\circ$.",
            ["Eq(180 - 55 - 55, 70)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "eyebrow": "Skill card",
            "title": "Lines, angles and triangles",
            "beats": [
                "Domain: Geometry and Trigonometry — 5 to 7 of the 44 questions.",
                "Usually 1 or 2, and they chain two facts rather than testing one.",
                "Prerequisite: solving a linear equation.",
                "Almost every fact here reduces to 180 degrees appearing somewhere.",
            ],
        },
        {
            "kind": "transversal",
            "title": "Only two sizes",
            "teach": "Tilt the transversal and watch every angle change together. Across all "
                     "eight angles there are only ever two different measures, and they add to "
                     "180 degrees. Break the parallelism and that collapses — which is why the "
                     "parallel marks matter.",
            "config": {"acute": 68, "interactive": True, "showParallelToggle": True,
                       "startParallel": True, "showMeasures": True},
        },
        {"kind": "worked", "title": "Two sizes, and nothing else", "problemId": "sat-la1-w1"},
        {
            "kind": "triangleAngles",
            "title": "The angle sum, and the exterior angle",
            "teach": "Drag the vertices. The three interior angles always total 180 degrees, "
                     "and the exterior angle at any vertex always equals the two interior "
                     "angles it is not touching.",
            "config": {"beta": 43, "gamma": 71, "exterior": True},
        },
        {
            "kind": "tapQuestion",
            "title": "Chain two facts",
            "prompt": "A triangle has angles $50^\\circ$ and $60^\\circ$. What is the exterior "
                      "angle at the remaining vertex?",
            "options": ["$110^\\circ$", "$70^\\circ$", "$120^\\circ$", "$130^\\circ$"],
            "correctIndex": 0,
            "explanation": "The exterior angle equals the sum of the two non-adjacent interior "
                           "angles: $50 + 60 = 110$. The long route agrees — the third interior "
                           "angle is $70^\\circ$, and $180 - 70 = 110$. Option B is that "
                           "interior angle, which the long route computes on the way.",
            "check": ["Eq(50 + 60, 110)", "Eq(180 - 50 - 60, 70)", "Eq(180 - 70, 110)"],
        },
        {"kind": "worked", "title": "Interior and exterior together", "problemId": "sat-la1-w2"},
        {
            "kind": "tip",
            "title": "Equal sides face equal angles",
            "body": "In an isosceles triangle the equal angles are OPPOSITE the equal sides, "
                    "not next to them. If the two equal sides meet at the apex, then the apex "
                    "is the odd angle out and the two BASE angles are the equal pair. Getting "
                    "that pairing backwards is the commonest isosceles error, and it produces "
                    "a listed answer every time.",
        },
        {"kind": "worked", "title": "An isosceles triangle", "problemId": "sat-la1-w3"},
        {"kind": "tryIt", "title": "Your turn: a linear pair", "problemId": "sat-la1-t1"},
        {"kind": "tryIt", "title": "Your turn: angles in a ratio", "problemId": "sat-la1-t2"},
        {"kind": "tryIt", "title": "Your turn: same-side interior", "problemId": "sat-la1-t3"},
        {"kind": "tryIt", "title": "Your turn: from base to apex", "problemId": "sat-la1-t4"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "A transversal across parallel lines makes only two different angle sizes.",
                "Those two sizes add to 180 degrees.",
                "The three angles of a triangle add to 180 degrees.",
                "An exterior angle equals the sum of the two non-adjacent interior angles.",
                "In an isosceles triangle the equal angles are opposite the equal sides.",
            ],
        },
    ]

    return lesson(
        slug="angles-and-triangles",
        title="Parallel Lines, Angle Sums and Isosceles Triangles",
        concrete=(
            "Two railway lines and a level crossing. However the crossing is angled, only two "
            "different angles appear anywhere in the picture — and they add to a straight "
            "line. Almost every angle question on the SAT is that one fact, used twice."
        ),
        objective=(
            "Find unknown angles using parallel-line relationships, the triangle angle sum, "
            "the exterior-angle rule and the isosceles-triangle property."
        ),
        concept=[
            "**Skill card.** The College Board calls this *Lines, angles, and triangles*, in "
            "the **Geometry and Trigonometry** domain. It is one or two questions, and they "
            "characteristically chain two facts rather than test one.",
            "A transversal crossing two parallel lines makes eight angles — and only TWO "
            "different sizes among them, which add to $180^\\circ$. Every named "
            "relationship follows from that. Corresponding, alternate interior, alternate "
            "exterior and vertical angles are the equal pairs; same-side interior angles and "
            "linear pairs are the supplementary ones. On the test, recognising 'this one looks "
            "the same size, so it is' beats recalling the names.",
            "The angles of a triangle total $180^\\circ$. An exterior angle, formed by "
            "extending one side, equals the SUM of the two non-adjacent interior angles — "
            "which is a one-step shortcut past computing the third angle first.",
            "**The test's angle.** Isosceles triangles, and which angles are the equal pair. "
            "The equal angles are OPPOSITE the equal sides, not adjacent to them. If $AB = "
            "AC$, the two equal sides meet at $A$, so $A$ is the odd angle out and the base "
            "angles at $B$ and $C$ are the pair. Assuming the given angle is one of the equal "
            "pair when it is actually the apex produces a plausible, listed, wrong answer.",
        ],
        key_idea=(
            "Parallel lines make only two angle sizes and they sum to $180^\\circ$; so do the "
            "three angles of a triangle. Everything else here is those two facts chained "
            "together."
        ),
        facts=[
            fact(
                "Parallel lines",
                "\\text{eight angles, two sizes}, \\qquad \\text{size}_1 + \\text{size}_2 = 180^\\circ",
                "Equal pairs: corresponding, alternate interior and exterior, vertical. "
                "Supplementary: same-side interior, linear pair.",
            ),
            fact(
                "Triangle angle sum",
                "\\alpha + \\beta + \\gamma = 180^\\circ",
                "True for every triangle, however it is drawn.",
            ),
            fact(
                "Exterior angle",
                "\\text{exterior} = \\text{sum of the two non-adjacent interior angles}",
                "A one-step alternative to finding the third interior angle first.",
            ),
            fact(
                "Isosceles",
                "AB = AC \\;\\Longleftrightarrow\\; \\angle B = \\angle C",
                "Equal sides face equal angles. The angle where the equal sides MEET is the "
                "odd one.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Pairing an isosceles triangle's equal angles with the wrong sides.",
                "The equal angles are opposite the equal sides. If the equal sides meet at the "
                "apex, the base angles are the equal pair.",
            ),
            mistake(
                "Answering with the interior angle when the exterior one was asked for.",
                "They are supplementary. The exterior angle is $180^\\circ$ minus the interior "
                "one — or, faster, the sum of the other two interior angles.",
            ),
            mistake(
                "Assuming angles are equal when the lines are not marked parallel.",
                "The whole two-sizes picture depends on parallelism. Without it, nothing "
                "follows.",
            ),
            mistake(
                "Reading a diagram's apparent angles as exact.",
                "SAT diagrams are not to scale unless stated. Use the marked values and the "
                "rules, never the appearance.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


def lesson_similarity():
    worked = [
        problem(
            "sat-la2-w1",
            "Triangle $ABC$ is similar to triangle $DEF$, with $AB = 6$, $BC = 9$ and "
            "$DE = 10$. What is the length of $EF$?",
            "**Answer.** $15$.  \n"
            "Similar triangles have the same shape at different sizes, so every pair of "
            "corresponding sides shares one scale factor. Find it from the pair you know:\n"
            "$$k = \\frac{DE}{AB} = \\frac{10}{6} = \\frac{5}{3}$$\n"
            "Then apply it to the side you want. $EF$ corresponds to $BC$:\n"
            "$$EF = \\frac{5}{3} \\times 9 = 15$$\n"
            "Check the ratios agree: $\\frac{10}{6} = \\frac{15}{9}$, both $\\frac{5}{3}$.  \n"
            "The naming carries the correspondence. In '$ABC$ similar to $DEF$' the letters "
            "line up in order, so $A$ matches $D$, $B$ matches $E$, $C$ matches $F$ — and side "
            "$BC$ therefore matches side $EF$. Pairing the wrong sides is the main error, and "
            "the letter order is what prevents it.",
            [
                "Eq(Rational(10,6), Rational(5,3))",
                "Eq(Rational(5,3)*9, 15)",
                "Eq(Rational(15,9), Rational(5,3))",
            ],
        ),
        problem(
            "sat-la2-w2",
            "A vertical pole $2$ metres tall casts a shadow $3$ metres long. At the same "
            "moment a tree casts a shadow $21$ metres long. How tall is the tree?",
            "**Answer.** $14$ metres.  \n"
            "The sun's rays arrive at the same angle for both objects, so the pole with its "
            "shadow and the tree with its shadow form SIMILAR right triangles. Corresponding "
            "sides are in the same ratio:\n"
            "$$\\frac{\\text{height}}{\\text{shadow}}: \\quad \\frac{2}{3} = \\frac{h}{21}$$\n"
            "$$3h = 42 \\;\\Longrightarrow\\; h = 14$$\n"
            "Check: the tree's shadow is seven times the pole's, so the tree should be seven "
            "times as tall — $7 \\times 2 = 14$. Both routes agree.  \n"
            "The set-up rule is the one that matters: keep the same quantity on top on both "
            "sides. Height over shadow on the left demands height over shadow on the right. "
            "Mixing them gives $\\frac{2}{3} = \\frac{21}{h}$ and the wrong answer $31.5$.",
            [
                "Eq(3*14, 2*21)",
                "Eq(Rational(2,3), Rational(14,21))",
                "Eq(Rational(21,3), 7)",
                "Eq(7*2, 14)",
            ],
        ),
        problem(
            "sat-la2-w3",
            "Two similar triangles have corresponding sides in the ratio $3 : 4$. The smaller "
            "has area $18$. What is the area of the larger?",
            "**Answer.** $32$.  \n"
            "Areas of similar figures scale by the SQUARE of the side ratio, not by the ratio "
            "itself:\n"
            "$$\\left(\\frac{4}{3}\\right)^{2} = \\frac{16}{9}$$\n"
            "$$18 \\times \\frac{16}{9} = 32$$\n"
            "The reason is the same one behind every scaling question: an area is a product of "
            "two lengths, so scaling both by $\\frac{4}{3}$ scales the area by "
            "$\\frac{4}{3} \\times \\frac{4}{3}$.  \n"
            "Applying the ratio once instead gives $18 \\times \\frac{4}{3} = 24$, which is on "
            "the option list. For similar SOLIDS the same logic gives a cube: volumes would "
            "scale by $\\left(\\frac{4}{3}\\right)^{3}$.",
            [
                "Eq(Rational(4,3)**2, Rational(16,9))",
                "Eq(18*Rational(16,9), 32)",
                "Eq(18*Rational(4,3), 24)",
            ],
        ),
    ]

    try_it = [
        problem(
            "sat-la2-t1",
            "Triangle $PQR$ is similar to triangle $STU$, with $PQ = 4$, $ST = 12$ and "
            "$QR = 7$. What is $TU$?",
            "**Answer.** $21$. The scale factor is $\\frac{12}{4} = 3$, and $TU$ corresponds "
            "to $QR$, so $TU = 3 \\times 7 = 21$.",
            ["Eq(Rational(12,4), 3)", "Eq(3*7, 21)"],
        ),
        problem(
            "sat-la2-t2",
            "A $1.5$-metre person casts a $2$-metre shadow. A flagpole casts a $16$-metre "
            "shadow at the same time. How tall is the flagpole?",
            "**Answer.** $12$ metres. The shadow is eight times as long, so the pole is eight "
            "times as tall: $8 \\times 1.5 = 12$. Or by proportion: "
            "$\\frac{1.5}{2} = \\frac{h}{16}$ gives $2h = 24$.",
            [
                "Eq(Rational(16,2), 8)",
                "Eq(8*Rational(15,10), 12)",
                "Eq(2*12, Rational(15,10)*16)",
            ],
        ),
        problem(
            "sat-la2-t3",
            "Two similar rectangles have sides in the ratio $2 : 5$. The smaller has area $12$. "
            "What is the larger's area?",
            "**Answer.** $75$. Areas scale by $\\left(\\frac{5}{2}\\right)^{2} = "
            "\\frac{25}{4}$, and $12 \\times \\frac{25}{4} = 75$.",
            ["Eq(Rational(5,2)**2, Rational(25,4))", "Eq(12*Rational(25,4), 75)"],
        ),
    ]

    steps = [
        {
            "kind": "teach",
            "title": "Similar means one scale factor everywhere",
            "body": "Two figures are similar when one is an enlargement of the other: equal "
                    "angles, and every pair of corresponding sides in the same ratio. That "
                    "single ratio — the scale factor — is what you find first, from the pair "
                    "of sides you know, and then apply to whatever you want.",
        },
        {
            "kind": "similarFigures",
            "title": "One factor, two consequences",
            "teach": "Slide the scale factor and watch the side lengths, the perimeter and the "
                     "area. Perimeter follows the factor; area follows its SQUARE — which is "
                     "the single most tested fact about similarity.",
            "config": {"start": 2, "show": "measures"},
        },
        {"kind": "worked", "title": "Finding and applying the factor", "problemId": "sat-la2-w1"},
        {
            "kind": "tapQuestion",
            "title": "Which sides correspond?",
            "prompt": "If triangle $ABC$ is similar to triangle $XYZ$, which side corresponds "
                      "to $AC$?",
            "options": ["$XZ$", "$XY$", "$YZ$", "It cannot be determined"],
            "correctIndex": 0,
            "explanation": "The letter order carries the correspondence: $A$ matches $X$, $B$ "
                           "matches $Y$, $C$ matches $Z$. So $AC$ matches $XZ$. Reading the "
                           "similarity statement carefully is what stops you pairing the wrong "
                           "sides.",
            "check": ["Eq(1, 1)", "Eq(3, 3)"],
        },
        {
            "kind": "tip",
            "title": "Shadows and mirrors are similar triangles",
            "body": "Whenever two objects are measured under the same conditions — the same "
                    "sunlight, the same sight line, the same mirror — their heights and their "
                    "shadows form similar right triangles. Set up the proportion with the same "
                    "quantity on top on both sides: height over shadow equals height over "
                    "shadow.",
        },
        {"kind": "worked", "title": "The shadow problem", "problemId": "sat-la2-w2"},
        {
            "kind": "teach",
            "title": "What scales, and by how much",
            "beats": [
                "Corresponding lengths and perimeters scale by the factor k.",
                "Areas scale by k².",
                "Volumes of similar solids scale by k³.",
                "Angles do not scale at all — similar figures have identical angles.",
            ],
        },
        {"kind": "worked", "title": "Areas scale by the square", "problemId": "sat-la2-w3"},
        {"kind": "tryIt", "title": "Your turn: apply the factor", "problemId": "sat-la2-t1"},
        {"kind": "tryIt", "title": "Your turn: a flagpole", "problemId": "sat-la2-t2"},
        {"kind": "tryIt", "title": "Your turn: scale an area", "problemId": "sat-la2-t3"},
        {
            "kind": "recap",
            "title": "What to carry into the test",
            "points": [
                "Similar figures share every angle and one scale factor across all sides.",
                "The letter order in 'ABC similar to DEF' tells you which sides correspond.",
                "Find the factor from the known pair, then apply it to the unknown.",
                "Lengths scale by k, areas by k², volumes by k³.",
                "Keep the same quantity on top on both sides of a proportion.",
            ],
        },
    ]

    return lesson(
        slug="similarity-and-proportions",
        title="Similar Triangles and What Scales",
        concrete=(
            "You can measure a tree without climbing it. Stand a metre stick next to it, "
            "compare the two shadows, and the ratio does the rest — because the sun makes the "
            "same angle with both, and that is all similarity needs."
        ),
        objective=(
            "Identify corresponding sides in similar figures, find and apply a scale factor, "
            "and use the fact that areas scale by the square of that factor."
        ),
        concept=[
            "**Skill card.** Still *Lines, angles, and triangles*, in the **Geometry and "
            "Trigonometry** domain. Similarity is where the domain's harder items live, and it "
            "reappears inside right-triangle trigonometry — the trig ratios exist precisely "
            "because similar right triangles have matching side ratios.",
            "Two figures are similar when one is an enlargement of the other: identical "
            "angles, and every pair of corresponding sides in the same ratio. That ratio is "
            "the scale factor. Find it from the pair of sides you know, then apply it to the "
            "side you want.",
            "Correspondence comes from the naming. In 'triangle $ABC$ is similar to triangle "
            "$DEF$' the letters are given in matching order, so $A$ pairs with $D$ and side "
            "$BC$ pairs with side $EF$. Pairing the wrong sides is the main way these "
            "questions are lost, and reading the statement carefully is the whole fix.",
            "**The test's angle.** Areas. Lengths and perimeters scale by the factor $k$, but "
            "areas scale by $k^{2}$ and volumes of similar solids by $k^{3}$. Sides in the "
            "ratio $3 : 4$ means areas in the ratio $9 : 16$. Applying the factor once to an "
            "area is the standard wrong answer, and it appears on every version of the "
            "question.",
        ],
        key_idea=(
            "Similarity is one scale factor applied everywhere. Lengths scale by $k$, areas by "
            "$k^{2}$, volumes by $k^{3}$ — and angles not at all."
        ),
        facts=[
            fact(
                "Similar figures",
                "\\frac{a_1}{a_2} = \\frac{b_1}{b_2} = \\frac{c_1}{c_2} = k",
                "One factor across every pair of corresponding sides. Angles are unchanged.",
            ),
            fact(
                "How measurements scale",
                "\\text{length} \\times k, \\qquad \\text{area} \\times k^{2}, \\qquad \\text{volume} \\times k^{3}",
                "The exponent counts how many lengths are multiplied together.",
            ),
        ],
        worked=worked,
        mistakes=[
            mistake(
                "Pairing sides that do not correspond.",
                "The letter order in the similarity statement gives the pairing. $BC$ matches "
                "$EF$, not $DE$.",
            ),
            mistake(
                "Scaling an area by the side ratio instead of its square.",
                "Sides in ratio $3 : 4$ means areas in ratio $9 : 16$.",
            ),
            mistake(
                "Inverting a proportion by putting different quantities on top.",
                "Height over shadow on one side needs height over shadow on the other.",
            ),
            mistake(
                "Expecting angles to change with the scale factor.",
                "Similar figures have identical angles. Only lengths, areas and volumes "
                "change.",
            ),
        ],
        try_it=try_it,
        steps=steps,
    )


LAT_PRACTICE = [
    problem(
        "sat-la-p01",
        "Two angles of a triangle measure $35^\\circ$ and $85^\\circ$. What is the third?",
        "**Answer.** $60^\\circ$. The three angles total $180^\\circ$.",
        ["Eq(180 - 35 - 85, 60)"],
        badges=_b(LAT_TAG, "Easy"),
    ),
    problem(
        "sat-la-p02",
        "Parallel lines are cut by a transversal. One angle is $115^\\circ$. What is its "
        "corresponding angle?",
        "**Answer.** $115^\\circ$. Corresponding angles are equal. The supplementary size in "
        "the figure is $65^\\circ$.",
        ["Eq(180 - 115, 65)", "Eq(115, 115)"],
        badges=_b(LAT_TAG, "Easy"),
    ),
    problem(
        "sat-la-p03",
        "An isosceles triangle has an apex angle of $80^\\circ$. What is each base angle?",
        "**Answer.** $50^\\circ$. The two base angles are equal and share the remaining "
        "$100^\\circ$.",
        ["Eq(Rational(180 - 80, 2), 50)", "Eq(80 + 50 + 50, 180)"],
        badges=_b(LAT_TAG, "Easy"),
    ),
    problem(
        "sat-la-p04",
        "Triangle $ABC$ is similar to triangle $DEF$ with $AB = 8$, $DE = 20$ and $AC = 6$. "
        "What is $DF$?",
        "**Answer.** $15$. The factor is $\\frac{20}{8} = 2.5$, and $DF$ corresponds to $AC$: "
        "$2.5 \\times 6 = 15$.",
        ["Eq(Rational(20,8), Rational(5,2))", "Eq(Rational(5,2)*6, 15)"],
        badges=_b(LAT_TAG, "Medium"),
    ),
    problem(
        "sat-la-p05",
        "A triangle has an exterior angle of $130^\\circ$ at one vertex. One of the "
        "non-adjacent interior angles is $45^\\circ$. What is the other?",
        "**Answer.** $85^\\circ$. The exterior angle equals the sum of the two non-adjacent "
        "interior angles, so the other is $130 - 45 = 85$.",
        ["Eq(130 - 45, 85)", "Eq(45 + 85, 130)", "Eq(180 - 130, 50)"],
        badges=_b(LAT_TAG, "Medium"),
    ),
    problem(
        "sat-la-p06",
        "Two similar triangles have sides in the ratio $5 : 8$. The larger has area $128$. "
        "What is the smaller's area?",
        "**Answer.** $50$. Areas scale by $\\left(\\frac{5}{8}\\right)^{2} = \\frac{25}{64}$, "
        "and $128 \\times \\frac{25}{64} = 50$.",
        ["Eq(Rational(5,8)**2, Rational(25,64))", "Eq(128*Rational(25,64), 50)"],
        badges=_b(LAT_TAG, "Hard"),
    ),
    problem(
        "sat-la-p07",
        "In a triangle the angles are in the ratio $2 : 3 : 4$. What is the largest angle?",
        "**Answer.** $80^\\circ$. The parts total $9$, so each part is $20^\\circ$, and the "
        "largest takes four parts.",
        ["Eq(2 + 3 + 4, 9)", "Eq(Rational(180,9), 20)", "Eq(4*20, 80)"],
        badges=_b(LAT_TAG, "Medium"),
    ),
    problem(
        "sat-la-p08",
        "A $1.8$-metre person standing $4$ metres from a streetlight casts a shadow $2$ metres "
        "long. How tall is the streetlight?",
        "**Answer.** $5.4$ metres. The person's shadow tip, the person and the light form "
        "similar triangles: the small one has height $1.8$ over base $2$, the large one has "
        "height $h$ over base $4 + 2 = 6$. So $\\frac{1.8}{2} = \\frac{h}{6}$, giving "
        "$h = 5.4$.",
        [
            "Eq(2*Rational(54,10), Rational(18,10)*6)",
            "Eq(4 + 2, 6)",
            "Eq(Rational(18,10)/2, Rational(54,10)/6)",
        ],
        badges=_b(LAT_TAG, "Hard"),
    ),
]

LAT_TEST = [
    problem(
        "sat-la-x01",
        "Two angles of a triangle measure $28^\\circ$ and $47^\\circ$. What is the third?",
        "**Answer.** $105^\\circ$.",
        ["Eq(180 - 28 - 47, 105)"],
        badges=_b(LAT_TAG, "Easy"),
    ),
    problem(
        "sat-la-x02",
        "Parallel lines are cut by a transversal, forming same-side interior angles of "
        "$(4x)^\\circ$ and $(5x + 27)^\\circ$. What is $x$?",
        "**Answer.** $17$. They are supplementary: $9x + 27 = 180$, so $9x = 153$ and "
        "$x = 17$. The angles are $68^\\circ$ and $112^\\circ$.",
        ["Eq(9*17 + 27, 180)", "Eq(4*17, 68)", "Eq(5*17 + 27, 112)", "Eq(68 + 112, 180)"],
        badges=_b(LAT_TAG, "Medium"),
    ),
    problem(
        "sat-la-x03",
        "An isosceles triangle has two sides of length $9$ and one of length $5$. If the angle "
        "opposite the side of length $5$ is $32^\\circ$, what are the other two angles?",
        "**Answer.** $74^\\circ$ each. The two sides of length $9$ are equal, so the angles "
        "opposite them are equal; they share the remaining $148^\\circ$.",
        ["Eq(Rational(180 - 32, 2), 74)", "Eq(32 + 74 + 74, 180)"],
        badges=_b(LAT_TAG, "Medium"),
    ),
    problem(
        "sat-la-x04",
        "Triangle $JKL$ is similar to triangle $MNP$ with $JK = 15$, $MN = 6$ and $KL = 20$. "
        "What is $NP$?",
        "**Answer.** $8$. The factor from $JKL$ to $MNP$ is $\\frac{6}{15} = \\frac{2}{5}$, "
        "and $NP$ corresponds to $KL$: $\\frac{2}{5} \\times 20 = 8$.",
        ["Eq(Rational(6,15), Rational(2,5))", "Eq(Rational(2,5)*20, 8)"],
        badges=_b(LAT_TAG, "Medium"),
    ),
    problem(
        "sat-la-x05",
        "Two similar solids have corresponding edges in the ratio $2 : 3$. What is the ratio "
        "of their volumes?",
        "**Answer.** $8 : 27$. Volumes scale by the cube of the linear ratio.",
        ["Eq(2**3, 8)", "Eq(3**3, 27)"],
        badges=_b(LAT_TAG, "Hard"),
    ),
    problem(
        "sat-la-x06",
        "In triangle $ABC$, the exterior angle at $C$ measures $118^\\circ$ and angle $A$ "
        "measures $53^\\circ$. What is angle $B$?",
        "**Answer.** $65^\\circ$. The exterior angle at $C$ equals the sum of angles $A$ and "
        "$B$, so $B = 118 - 53 = 65$. The interior angle at $C$ is $62^\\circ$, and "
        "$53 + 65 + 62 = 180$ confirms it.",
        [
            "Eq(118 - 53, 65)",
            "Eq(180 - 118, 62)",
            "Eq(53 + 65 + 62, 180)",
        ],
        badges=_b(LAT_TAG, "Hard"),
    ),
]


def main():
    write_unit(
        COURSE,
        "area-and-volume",
        "Area and Volume Formulas",
        1,
        "Choosing the right formula off the reference sheet, telling a radius from a diameter "
        "and a height from a slant, composite shapes — and the scaling rule that multiplies "
        "area by k squared and volume by k cubed.",
        None,
        [lesson_area(), lesson_composite()],
        AV_PRACTICE,
        AV_TEST,
    )
    write_unit(
        COURSE,
        "lines-angles-and-triangles",
        "Lines, Angles, and Triangles",
        2,
        "Two angle sizes across a transversal, the triangle angle sum and the exterior-angle "
        "shortcut, isosceles triangles and which angles are the equal pair, and similarity — "
        "where lengths scale by k and areas by k squared.",
        "The scaling rule from Unit 1, which is the same idea seen through similar figures.",
        [lesson_angles(), lesson_similarity()],
        LAT_PRACTICE,
        LAT_TEST,
    )


if __name__ == "__main__":
    main()
