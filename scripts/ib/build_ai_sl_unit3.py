#!/usr/bin/env python3
"""IB Mathematics: Applications & Interpretation SL — Unit 3 (Topic 3: Geometry & Trigonometry).

Builds data/genmath/ib-ai-sl/geometry-and-trigonometry.json: six lessons, one
per official subtopic code AI SL 3.1-3.6, same anatomy as Units 1-2 (syllabus
cards, booklet flags, M/A/R markscheme + narrative solutions, interactive
widgets, sympy check[] everywhere). Banks tagged ib-ai-sl-3.x.

The last two codes are the ones with no counterpart in Analysis & Approaches:
3.5 (equations of perpendicular bisectors) exists only to feed 3.6 (Voronoi
diagrams — sites, cells, edges, vertices, adding a site, nearest-neighbour
interpolation, and the toxic-waste-dump problem). AA students never meet
either.

Everything here is degrees, not radians: AI states angles in degrees
throughout, and the arc/sector formulas in the booklet carry the
theta/360 factor that says so.

Run: python3 scripts/ib/build_ai_sl_unit3.py   (then npm run verify:genmath)
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "data", "genmath", "ib-ai-sl", "geometry-and-trigonometry.json")


# ===========================================================================
# Lesson 1 — AI SL 3.1: 3D distance, midpoint, solids, angles
# ===========================================================================
def lesson_three_dimensions():
    return {
        "slug": "three-dimensional-geometry",
        "title": "Distance, Volume and Angles in Three Dimensions",
        "concreteComparison": (
            "A grain silo is a cylinder with a cone on top. Nobody has a formula for a silo — "
            "you have the formula for a cylinder and the formula for a cone, and the whole trick "
            "is seeing where one stops and the other starts. Almost every AI volume question is "
            "that decomposition."
        ),
        "objective": (
            "Find distances and midpoints in three dimensions, compute the volume and surface "
            "area of the booklet solids and their combinations, and find the angle between two "
            "lines or between a line and a plane."
        ),
        "concept": [
            "**Syllabus card — AI SL 3.1.** The distance between two points in three-dimensional "
            "space and their midpoint; volume and surface area of three-dimensional solids "
            "(right pyramid, right cone, sphere, hemisphere and combinations); the size of the "
            "angle between two intersecting lines or between a line and a plane. **Papers 1 and "
            "2.** Every formula on this code is in the booklet.",
            "The 3D distance formula is Pythagoras twice. Going from "
            "$\\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$ to the 3D version just adds "
            "$(z_2-z_1)^2$ under the same root, because the diagonal of a box is the hypotenuse "
            "of a triangle whose legs are the base diagonal and the height. The midpoint is the "
            "average, coordinate by coordinate — no square roots involved.",
            "Combination solids are ADDED or SUBTRACTED, never given their own formula. A silo "
            "is a cylinder plus a cone; a hemisphere is half a sphere; a cored cylinder is a big "
            "cylinder minus a small one. Say which pieces you are using and the method marks "
            "follow, even if the arithmetic slips.",
            "Surface area is where combinations bite. Gluing a cone onto a cylinder HIDES two "
            "circles — the cylinder's top and the cone's base — so the total surface uses the "
            "cone's CURVED area only, plus the cylinder's curved area and its single remaining "
            "base. Draw the solid and shade what a fly could land on.",
            "The angle between a line and a plane is measured to the line's PROJECTION on that "
            "plane, so you always end up in a right triangle: the line is the hypotenuse, its "
            "shadow is the adjacent side, and the perpendicular height is the opposite. Find "
            "that triangle and the angle is one $\\tan^{-1}$ away."
        ],
        "keyIdea": (
            "3D questions become 2D questions the moment you find the right triangle inside "
            "them. Distance is Pythagoras twice; angles are Pythagoras plus one trig ratio."
        ),
        "facts": [
            {
                "title": "Distance and midpoint in 3D",
                "latex": "d = \\sqrt{(x_2-x_1)^2 + (y_2-y_1)^2 + (z_2-z_1)^2}, \\quad M = \\left(\\frac{x_1+x_2}{2}, \\frac{y_1+y_2}{2}, \\frac{z_1+z_2}{2}\\right)",
                "explanation": "Booklet (AI SL 3.1). Distance takes differences; the midpoint takes averages.",
            },
            {
                "title": "Cone and pyramid",
                "latex": "V = \\frac{1}{3}\\pi r^2 h, \\quad A_{\\text{curved}} = \\pi r l \\qquad V_{\\text{pyramid}} = \\frac{1}{3}Ah",
                "explanation": "Booklet. $l$ is the SLANT height — a cone's curved area never uses $h$.",
            },
            {
                "title": "Sphere",
                "latex": "V = \\frac{4}{3}\\pi r^3, \\quad A = 4\\pi r^2",
                "explanation": "Booklet. A hemisphere is half of each, plus the flat circle if it is closed.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-31-we1",
                "statement": (
                    "A storage silo is a cylinder of radius $3$ m and height $8$ m with a cone "
                    "of the same radius and height $4$ m on top.  \n"
                    "**(a)** Find the total volume, to 3 s.f. **[4]**  \n"
                    "**(b)** Find the slant height of the cone. **[2]**  \n"
                    "**(c)** Find the external surface area, excluding the flat base. **[4]**"
                ),
                "solution": (
                    "**(a)** Cylinder: $\\pi(3)^{2}(8) = 72\\pi$ *(M1 A1)*. Cone: "
                    "$\\frac{1}{3}\\pi(3)^{2}(4) = 12\\pi$ *(A1)*. Total "
                    "$= 84\\pi = 264$ m$^{3}$ *(A1)*.  \n"
                    "**(b)** $l = \\sqrt{3^{2} + 4^{2}}$ *(M1)* $= 5$ m *(A1)*.  \n"
                    "**(c)** Cone curved: $\\pi(3)(5) = 15\\pi$ *(M1 A1)*. Cylinder curved: "
                    "$2\\pi(3)(8) = 48\\pi$ *(A1)*. Total $= 63\\pi = 198$ m$^{2}$ *(A1)*.  \n"
                    "**Narrative:** part (c) is the one that separates candidates. The cylinder's "
                    "top circle is glued to the cone's base circle — neither is on the outside, "
                    "so neither appears. Adding $\\pi(3)^{2}$ twice is the standard error and it "
                    "costs the last two marks. Note also that (b) gives a $3$-$4$-$5$ triangle: "
                    "AI questions are built with friendly numbers so that a slip is visible."
                ),
                "check": [
                    "Eq(pi*3**2*8, 72*pi)",
                    "Eq(Rational(1, 3)*pi*3**2*4, 12*pi)",
                    "Abs(84*pi - 264) < 1",
                    "sqrt(3**2 + 4**2) == 5",
                    "Eq(pi*3*5 + 2*pi*3*8, 63*pi)",
                    "Abs(63*pi - 198) < 1",
                ],
            },
            {
                "id": "aisl-31-we2",
                "statement": (
                    "A cuboid has vertices including $A(0, 0, 0)$ and $G(6, 3, 2)$, with edges "
                    "along the axes.  \n"
                    "**(a)** Find the length of the space diagonal $AG$. **[3]**  \n"
                    "**(b)** Find the midpoint of $AG$. **[2]**  \n"
                    "**(c)** Find the angle that $AG$ makes with the base plane, to 3 s.f. "
                    "**[4]**"
                ),
                "solution": (
                    "**(a)** $AG = \\sqrt{6^{2} + 3^{2} + 2^{2}} = \\sqrt{49}$ *(M1 A1)* $= 7$ "
                    "*(A1)*.  \n"
                    "**(b)** $M = (3, 1.5, 1)$ *(M1 A1)*.  \n"
                    "**(c)** The projection of $AG$ on the base is the base diagonal, of length "
                    "$\\sqrt{6^{2} + 3^{2}} = \\sqrt{45}$ *(M1 A1)*. Then "
                    "$\\tan\\theta = \\dfrac{2}{\\sqrt{45}}$ *(M1)*, so "
                    "$\\theta = 16.6^\\circ$ *(A1)*.  \n"
                    "**Narrative:** part (c) is the standard line-to-plane recipe: drop the line "
                    "onto the plane, and the right triangle appears with the height opposite the "
                    "angle. Using $\\sin\\theta = \\frac{2}{7}$ with the SPACE diagonal as "
                    "hypotenuse gives the same $16.6^\\circ$ — both are correct, and having two "
                    "routes that agree is the cheapest check available."
                ),
                "check": [
                    "sqrt(6**2 + 3**2 + 2**2) == 7",
                    "Rational(6, 2) == 3",
                    "Rational(3, 2) == Rational(15, 10)",
                    "Eq(6**2 + 3**2, 45)",
                    "Abs(atan(2/sqrt(45))*180/pi - Rational(166, 10)) < Rational(5, 100)",
                    "Abs(asin(Rational(2, 7))*180/pi - Rational(166, 10)) < Rational(5, 100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using the vertical height in the cone's curved surface area.",
                "correction": "$A = \\pi r l$ uses the SLANT height. Find $l = \\sqrt{r^2 + h^2}$ first — it is a separate step and usually a separate mark.",
                "authored": True,
            },
            {
                "text": "Counting the joining circles in a combination solid's surface area.",
                "correction": "Glued faces are inside. Sketch the solid and shade only the surface a fly could land on.",
                "authored": True,
            },
            {
                "text": "Measuring the line-to-plane angle from the vertical.",
                "correction": "The angle is between the line and its projection ON the plane, so it is measured from the horizontal. From the vertical you get its complement.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-31-t1",
                "statement": (
                    "Find the distance between $P(2, -1, 4)$ and $Q(6, 2, 8)$, and their "
                    "midpoint. **[4]**"
                ),
                "solution": (
                    "$PQ = \\sqrt{4^{2} + 3^{2} + 4^{2}} = \\sqrt{41} = 6.40$ (3 s.f.) "
                    "*(M1 A1)*.  \n"
                    "$M = \\left(\\dfrac{2+6}{2}, \\dfrac{-1+2}{2}, \\dfrac{4+8}{2}\\right) = "
                    "(4, 0.5, 6)$ *(M1 A1)*."
                ),
                "check": [
                    "(6 - 2)**2 + (2 - (-1))**2 + (8 - 4)**2 == 41",
                    "Abs(sqrt(41) - Rational(640, 100)) < Rational(5, 1000)",
                    "Rational(-1 + 2, 2) == Rational(1, 2)",
                ],
            },
            {
                "id": "aisl-31-t2",
                "statement": (
                    "A solid is a hemisphere of radius $5$ cm sitting on a cylinder of the same "
                    "radius and height $12$ cm. Find its volume, to 3 s.f. **[4]**"
                ),
                "solution": (
                    "Cylinder: $\\pi(5)^{2}(12) = 300\\pi$ *(M1 A1)*.  \n"
                    "Hemisphere: $\\dfrac{1}{2}\\cdot\\dfrac{4}{3}\\pi(5)^{3} = "
                    "\\dfrac{250\\pi}{3}$ *(A1)*.  \n"
                    "Total $= 300\\pi + \\dfrac{250\\pi}{3} = \\dfrac{1150\\pi}{3} = 1200$ "
                    "cm$^{3}$ (3 s.f.) *(A1)*."
                ),
                "check": [
                    "Eq(pi*5**2*12, 300*pi)",
                    "Eq(Rational(1, 2)*Rational(4, 3)*pi*5**3, Rational(250, 3)*pi)",
                    "Eq(300*pi + Rational(250, 3)*pi, Rational(1150, 3)*pi)",
                    "Abs(Rational(1150, 3)*pi - 1200) < 6",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 3.1 · Papers 1 & 2",
                    "title": "Find the right triangle and you are done",
                    "body": (
                        "Three dimensions look intimidating and behave like two. Every distance "
                        "is Pythagoras applied twice; every angle sits in a right triangle you "
                        "can draw flat on the page. The skill being assessed is finding that "
                        "triangle, not remembering a formula — all the formulas are printed."
                    ),
                },
                {
                    "kind": "solid3d",
                    "eyebrow": "Play",
                    "title": "A cone, radius and height apart",
                    "teach": (
                        "Step $r$ and $h$ and watch the volume respond. Volume depends on "
                        "$r^{2}$, so doubling the radius quadruples it while doubling the height "
                        "only doubles it — the asymmetry that makes wide-and-short beat "
                        "tall-and-thin for storage."
                    ),
                    "config": {"solid": "cone", "r": 3, "h": 4, "slant": 5},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Combination solids, in four moves",
                    "beats": [
                        "Name the pieces: cylinder + cone, sphere − cylinder, and so on.",
                        "Compute each piece exactly, keeping $\\pi$ until the last line.",
                        "Add or subtract, then round once at the end.",
                        "For surface area, cross out every glued face before totalling.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A silo, volume and skin",
                    "problemId": "aisl-31-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Slant or height?",
                    "title": "Which length does $\\pi r l$ want?",
                    "prompt": (
                        "A cone has radius $6$ and vertical height $8$. Its curved surface area is"
                    ),
                    "options": [
                        "$60\\pi$",
                        "$48\\pi$",
                        "$96\\pi$",
                        "$36\\pi$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "First the slant: $l = \\sqrt{6^{2} + 8^{2}} = 10$. Then "
                        "$\\pi r l = \\pi(6)(10) = 60\\pi$. Using $h = 8$ instead gives "
                        "$48\\pi$ — the single most common error on this code."
                    ),
                    "check": [
                        "sqrt(6**2 + 8**2) == 10",
                        "Eq(pi*6*10, 60*pi)",
                        "Eq(pi*6*8, 48*pi)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A box diagonal and the angle it makes",
                    "problemId": "aisl-31-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Midpoint, not distance",
                    "title": "Average, don't subtract",
                    "prompt": "The midpoint of $(1, 5, -3)$ and $(7, 1, 5)$ is",
                    "options": [
                        "$(4, 3, 1)$",
                        "$(6, -4, 8)$",
                        "$(3, 2, 4)$",
                        "$(8, 6, 2)$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Average each coordinate: $\\frac{1+7}{2} = 4$, $\\frac{5+1}{2} = 3$, "
                        "$\\frac{-3+5}{2} = 1$. Subtracting instead gives the DISPLACEMENT "
                        "$(6, -4, 8)$, which is the first step of the distance formula, not the "
                        "midpoint."
                    ),
                    "check": [
                        "Rational(1 + 7, 2) == 4",
                        "Rational(5 + 1, 2) == 3",
                        "Rational(-3 + 5, 2) == 1",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Keep $\\pi$ until the last line",
                    "body": (
                        "Rounding $72\\pi$ to $226.2$ and then adding rounded pieces is how "
                        "answers drift out of the 3 s.f. window. Work exactly, add exactly, and "
                        "round once — the markscheme's accepted range assumes you did."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-31-t1"},
                {"kind": "tryIt", "problemId": "aisl-31-t2"},
                {
                    "kind": "recap",
                    "title": "Three dimensions, compressed",
                    "points": [
                        "Distance adds $(z_2-z_1)^2$ under the same root; midpoint averages.",
                        "Combinations are sums and differences of booklet solids.",
                        "Curved cone area uses the SLANT height, found by Pythagoras.",
                        "Line-to-plane angle: project the line, then use the right triangle.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 2 — AI SL 3.2: right-triangle trig, sine and cosine rules
# ===========================================================================
def lesson_trigonometry():
    return {
        "slug": "right-and-non-right-trigonometry",
        "title": "Trigonometry: Right Triangles, Sine and Cosine Rules",
        "concreteComparison": (
            "A surveyor cannot walk across a lake to measure it, so they walk around two sides, "
            "measure the angle between them, and compute the third. That is the cosine rule, and "
            "it is the reason trigonometry exists: measuring what you cannot reach."
        ),
        "objective": (
            "Use the trigonometric ratios in right triangles, and the sine rule, cosine rule and "
            "the $\\frac{1}{2}ab\\sin C$ area formula in any triangle."
        ),
        "concept": [
            "**Syllabus card — AI SL 3.2.** Use of sine, cosine and tangent ratios to find sides "
            "and angles in right-angled triangles; the sine rule, the cosine rule, and the area "
            "of a triangle as $\\frac{1}{2}ab\\sin C$. **Papers 1 and 2.** All in the booklet; "
            "all in DEGREES.",
            "In a right triangle, name the sides relative to the angle you are working with: "
            "opposite, adjacent, hypotenuse. SOH-CAH-TOA then picks the ratio for you. To find "
            "an ANGLE, use the inverse: $\\theta = \\tan^{-1}\\!\\left(\\frac{\\text{opp}}"
            "{\\text{adj}}\\right)$.",
            "Choosing between the rules is mechanical. The SINE rule needs a matched pair — a "
            "side and the angle opposite it — plus one more piece. The COSINE rule handles the "
            "two cases the sine rule cannot: two sides and the angle BETWEEN them, or all three "
            "sides. If no side–angle pair is given, it is the cosine rule.",
            "Two cautions worth marks. The sine rule can give an ambiguous case: when you find "
            "an angle from $\\sin^{-1}$, a second, obtuse angle $180^\\circ - \\theta$ may also "
            "fit, and the question's diagram or wording decides. And the area formula "
            "$\\frac{1}{2}ab\\sin C$ needs the angle BETWEEN the two sides — no other angle will "
            "do."
        ],
        "keyIdea": (
            "Right triangle: SOH-CAH-TOA. Any triangle: a matched side–angle pair means the sine "
            "rule; otherwise the cosine rule. Degrees, always."
        ),
        "facts": [
            {
                "title": "The sine rule",
                "latex": "\\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C}",
                "explanation": "Booklet (AI SL 3.2). Needs a side and its opposite angle.",
            },
            {
                "title": "The cosine rule",
                "latex": "c^2 = a^2 + b^2 - 2ab\\cos C \\qquad \\cos C = \\frac{a^2 + b^2 - c^2}{2ab}",
                "explanation": "Booklet. Second form for finding an angle from three sides.",
            },
            {
                "title": "Area of a triangle",
                "latex": "A = \\frac{1}{2}ab\\sin C",
                "explanation": "Booklet. $C$ is the angle BETWEEN sides $a$ and $b$.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-32-we1",
                "statement": (
                    "In triangle $ABC$, $AB = 9$ cm, $AC = 12$ cm and angle "
                    "$BAC = 40^\\circ$.  \n"
                    "**(a)** Find $BC$, to 3 s.f. **[3]**  \n"
                    "**(b)** Find the area of the triangle, to 3 s.f. **[3]**  \n"
                    "**(c)** Find angle $ABC$, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** Two sides and the angle between them, so the cosine rule *(M1)*: "
                    "$BC^{2} = 9^{2} + 12^{2} - 2(9)(12)\\cos 40^\\circ = 59.55\\ldots$ *(A1)*, "
                    "so $BC = 7.72$ cm *(A1)*.  \n"
                    "**(b)** $A = \\frac{1}{2}(9)(12)\\sin 40^\\circ$ *(M1 A1)* $= 34.7$ "
                    "cm$^{2}$ *(A1)*.  \n"
                    "**(c)** Now there is a matched pair, so the sine rule *(M1)*: "
                    "$\\dfrac{\\sin B}{12} = \\dfrac{\\sin 40^\\circ}{7.72}$, giving "
                    "$\\sin B = 0.999$ *(A1)* and $B = 87.2^\\circ$ *(A1)*.  \n"
                    "**Narrative:** the question walks the standard route — cosine rule for the "
                    "third side, then sine rule once a pair exists. In (c) $\\sin B$ comes out "
                    "very close to $1$, so the triangle is nearly right-angled at $B$; that is a "
                    "warning to carry full accuracy from (a) rather than the rounded $7.72$, "
                    "because near $90^\\circ$ the sine barely changes and a rounded input moves "
                    "the answer by a whole degree."
                ),
                "check": [
                    "Abs(9**2 + 12**2 - 2*9*12*cos(40*pi/180) - Rational(5955, 100)) < Rational(2, 100)",
                    "Abs(sqrt(9**2 + 12**2 - 2*9*12*cos(40*pi/180)) - Rational(772, 100)) < Rational(5, 1000)",
                    "Abs(Rational(1, 2)*9*12*sin(40*pi/180) - Rational(347, 10)) < Rational(5, 100)",
                    "Abs(12*sin(40*pi/180)/sqrt(9**2 + 12**2 - 2*9*12*cos(40*pi/180)) - Rational(999, 1000)) < Rational(1, 1000)",
                ],
            },
            {
                "id": "aisl-32-we2",
                "statement": (
                    "A triangular plot has sides $AB = 40$ m, $BC = 55$ m and $CA = 35$ m.  \n"
                    "**(a)** Find the largest angle of the triangle, to 3 s.f. **[4]**  \n"
                    "**(b)** Find the area of the plot, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** The largest angle faces the longest side $BC = 55$, so it is angle "
                    "$A$ *(R1)*. By the cosine rule *(M1)*: "
                    "$\\cos A = \\dfrac{40^{2} + 35^{2} - 55^{2}}{2(40)(35)} = "
                    "-\\dfrac{200}{2800}$ *(A1)*, so $A = 94.1^\\circ$ *(A1)*.  \n"
                    "**(b)** $\\text{Area} = \\frac{1}{2}(40)(35)\\sin 94.1^\\circ$ *(M1 A1)* "
                    "$= 698$ m$^{2}$ *(A1)*.  \n"
                    "**Narrative:** the negative cosine is the useful signal — it says the angle "
                    "is obtuse before you press a button, and a positive answer at this point "
                    "would mean a sign slip in the numerator. Part (b) reuses the angle from (a) "
                    "with the two sides that enclose it; using $BC$ by mistake would break the "
                    "'angle between' requirement."
                ),
                "check": [
                    "Rational(40**2 + 35**2 - 55**2, 2*40*35) == Rational(-1, 14)",
                    "Abs(acos(Rational(-1, 14))*180/pi - Rational(941, 10)) < Rational(5, 100)",
                    "Abs(Rational(1, 2)*40*35*sin(acos(Rational(-1, 14))) - 698) < 1",
                    "Rational(-1, 14) < 0",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Working in radians because the calculator was left in radian mode.",
                "correction": "AI states angles in degrees. Set the mode once at the start of the paper and check it whenever an answer looks absurd.",
                "authored": True,
            },
            {
                "text": "Using $\\frac{1}{2}ab\\sin C$ with an angle that is not between $a$ and $b$.",
                "correction": "The angle must be enclosed by the two sides you multiply. Relabel the triangle if necessary rather than reaching for the wrong angle.",
                "authored": True,
            },
            {
                "text": "Reaching for the sine rule when no side–angle pair is given.",
                "correction": "The sine rule needs a matched pair. Two sides and the included angle, or three sides, is always the cosine rule.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-32-t1",
                "statement": (
                    "In a right triangle, the side opposite $\\theta$ is $7$ and the hypotenuse "
                    "is $25$. Find $\\theta$ and the third side. **[4]**"
                ),
                "solution": (
                    "$\\sin\\theta = \\dfrac{7}{25}$ *(M1)*, so $\\theta = 16.3^\\circ$ "
                    "*(A1)*.  \n"
                    "Third side $= \\sqrt{25^{2} - 7^{2}} = \\sqrt{576} = 24$ *(M1 A1)*."
                ),
                "check": [
                    "Abs(asin(Rational(7, 25))*180/pi - Rational(163, 10)) < Rational(5, 100)",
                    "sqrt(25**2 - 7**2) == 24",
                ],
            },
            {
                "id": "aisl-32-t2",
                "statement": (
                    "In triangle $PQR$, $PQ = 14$, angle $P = 35^\\circ$ and angle "
                    "$Q = 80^\\circ$. Find $QR$, to 3 s.f. **[4]**"
                ),
                "solution": (
                    "Angle $R = 180^\\circ - 35^\\circ - 80^\\circ = 65^\\circ$ *(A1)*, and "
                    "$PQ = 14$ is the side opposite $R$ — a matched pair *(M1)*.  \n"
                    "$\\dfrac{QR}{\\sin 35^\\circ} = \\dfrac{14}{\\sin 65^\\circ}$ *(A1)*, so "
                    "$QR = 8.86$ *(A1)*."
                ),
                "check": [
                    "180 - 35 - 80 == 65",
                    "Abs(14*sin(35*pi/180)/sin(65*pi/180) - Rational(886, 100)) < Rational(5, 1000)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 3.2 · Papers 1 & 2",
                    "title": "Two rules cover every triangle",
                    "body": (
                        "Right triangles get SOH-CAH-TOA. Everything else gets one of two rules, "
                        "and which one is decided entirely by what you were given — not by "
                        "preference, not by which you remember better."
                    ),
                },
                {
                    "kind": "trigRatios",
                    "eyebrow": "Play",
                    "title": "Opposite, adjacent, hypotenuse",
                    "teach": (
                        "Change $\\theta$ and watch the three ratios move. Notice the hypotenuse "
                        "never changes role while opposite and adjacent swap as the angle "
                        "grows — the labels belong to the ANGLE you chose, not to the triangle."
                    ),
                    "config": {"start": 35},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Which rule? Read what you were given",
                    "beats": [
                        "A side and its opposite angle, plus one more piece → sine rule.",
                        "Two sides and the angle between them → cosine rule.",
                        "All three sides, want an angle → cosine rule, rearranged form.",
                        "Two sides and the angle between them, want the area → $\\frac{1}{2}ab\\sin C$.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Cosine rule, then sine rule",
                    "problemId": "aisl-32-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Choose the rule",
                    "title": "What were you given?",
                    "prompt": (
                        "A triangle has sides $8$ and $11$ with a $52^\\circ$ angle between "
                        "them. To find the third side, use"
                    ),
                    "options": [
                        "the cosine rule",
                        "the sine rule",
                        "Pythagoras",
                        "the area formula",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "No side has its opposite angle given, so the sine rule cannot start. "
                        "Two sides with the included angle is the cosine rule's own case: "
                        "$c^{2} = 8^{2} + 11^{2} - 2(8)(11)\\cos 52^\\circ$, giving "
                        "$c = 8.75$."
                    ),
                    "check": [
                        "Abs(sqrt(8**2 + 11**2 - 2*8*11*cos(52*pi/180)) - Rational(875, 100)) < Rational(5, 1000)",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Three sides, largest angle, area",
                    "problemId": "aisl-32-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the sign",
                    "title": "What a negative cosine tells you",
                    "prompt": "If the cosine rule gives $\\cos C = -0.35$, then angle $C$ is",
                    "options": [
                        "obtuse",
                        "acute",
                        "a right angle",
                        "impossible — cosines cannot be negative",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Between $0^\\circ$ and $180^\\circ$ the cosine is positive for acute "
                        "angles and negative for obtuse ones. Here $C = 110^\\circ$ to 3 s.f. — "
                        "and the minus sign told you so before the calculator did."
                    ),
                    "check": [
                        "Abs(acos(Rational(-35, 100))*180/pi - 110) < Rational(5, 10)",
                        "cos(pi/3) > 0",
                    ],
                },
                {
                    "kind": "funFact",
                    "eyebrow": "One rule, really",
                    "title": "Pythagoras is the cosine rule in disguise",
                    "body": (
                        "Put $C = 90^\\circ$ into $c^{2} = a^{2} + b^{2} - 2ab\\cos C$. Since "
                        "$\\cos 90^\\circ = 0$ the last term vanishes and you are left with "
                        "$c^{2} = a^{2} + b^{2}$. The cosine rule is Pythagoras with a "
                        "correction term for triangles that are not quite right."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-32-t1"},
                {"kind": "tryIt", "problemId": "aisl-32-t2"},
                {
                    "kind": "recap",
                    "title": "Trigonometry, compressed",
                    "points": [
                        "Right triangle: name the sides by the angle, then SOH-CAH-TOA.",
                        "Matched side–angle pair → sine rule; otherwise cosine rule.",
                        "$\\frac{1}{2}ab\\sin C$ needs the angle BETWEEN the two sides.",
                        "Degrees throughout — check the calculator mode first.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 3 — AI SL 3.3: applications, elevation and depression, diagrams
# ===========================================================================
def lesson_applications():
    return {
        "slug": "applications-of-trigonometry",
        "title": "Applications: Elevation, Depression and Bearings",
        "concreteComparison": (
            "A lighthouse keeper spots a boat and reports the angle below the horizontal. A "
            "sailor on that boat, looking back, measures exactly the same angle above the "
            "horizontal. Depression from above equals elevation from below — the two lines of "
            "sight are the same line."
        ),
        "objective": (
            "Turn a written situation into a labelled diagram, and solve it with right-triangle "
            "or non-right trigonometry — including angles of elevation and depression and "
            "three-figure bearings."
        ),
        "concept": [
            "**Syllabus card — AI SL 3.3.** Applications of right and non-right angled "
            "trigonometry, including Pythagoras' theorem; angles of elevation and depression; "
            "construction of labelled diagrams from written statements. **Papers 1 and 2.** The "
            "diagram is itself worth marks.",
            "Draw the diagram before anything else. Mark every given length, every given angle, "
            "and the quantity being asked for — even a rough sketch converts a paragraph into a "
            "triangle, and examiners award method marks for a correctly labelled figure alone.",
            "ELEVATION is measured up from the horizontal, DEPRESSION down from it. Because the "
            "two horizontals are parallel, the angle of depression from the top equals the angle "
            "of elevation from the bottom — alternate angles. Drawing the horizontal dashed line "
            "at the observer's eye makes this visible and stops the classic error of putting the "
            "depression angle inside the triangle at the wrong vertex.",
            "BEARINGS are measured clockwise from north and always written with three figures: "
            "$072^\\circ$, not $72^\\circ$. Draw a north arrow at every point you take a bearing "
            "FROM. The angle inside your triangle is almost never the bearing itself — it is the "
            "difference between two bearings, or a supplement of one."
        ],
        "keyIdea": (
            "Draw it, label it, then look for the triangle. The mathematics on this code is the "
            "previous lesson's; the assessed skill is the translation."
        ),
        "facts": [
            {
                "title": "Elevation equals depression",
                "latex": "\\text{depression from } A \\text{ to } B \\;=\\; \\text{elevation from } B \\text{ to } A",
                "explanation": "Alternate angles between two parallel horizontals. Not a booklet formula — a picture.",
            },
            {
                "title": "Bearings",
                "latex": "000^\\circ \\text{ (N)} \\to 090^\\circ \\text{ (E)} \\to 180^\\circ \\text{ (S)} \\to 270^\\circ \\text{ (W)}",
                "explanation": "Clockwise from north, always three figures.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-33-we1",
                "statement": (
                    "From a point $A$ on level ground, the angle of elevation to the top of a "
                    "tower is $28^\\circ$. From a point $B$, $45$ m closer to the tower on the "
                    "same straight line, the angle of elevation is $47^\\circ$.  \n"
                    "**(a)** Find the angle $ATB$, where $T$ is the top of the tower. **[2]**  \n"
                    "**(b)** Find the distance $BT$, to 3 s.f. **[3]**  \n"
                    "**(c)** Find the height of the tower, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** In triangle $ABT$, the exterior angle at $B$ is $47^\\circ$, so the "
                    "interior angle $ABT = 133^\\circ$ *(A1)*, and "
                    "$A\\hat{T}B = 180^\\circ - 28^\\circ - 133^\\circ = 19^\\circ$ *(A1)*.  \n"
                    "**(b)** Sine rule in triangle $ABT$ *(M1)*: "
                    "$\\dfrac{BT}{\\sin 28^\\circ} = \\dfrac{45}{\\sin 19^\\circ}$ *(A1)*, so "
                    "$BT = 64.9$ m *(A1)*.  \n"
                    "**(c)** In the right triangle at the tower's base: "
                    "$h = BT\\sin 47^\\circ$ *(M1 A1)* $= 47.5$ m *(A1)*.  \n"
                    "**Narrative:** the two-observation tower is the archetype of this code, and "
                    "part (a) is where it is won. The $47^\\circ$ is measured from the "
                    "horizontal pointing AWAY from the tower's base, so inside triangle $ABT$ "
                    "the angle at $B$ is its supplement. Sketch the horizontal through $B$ and "
                    "the two angles on it are visibly supplementary; skip the sketch and "
                    "$133^\\circ$ is very easy to miss."
                ),
                "check": [
                    "180 - 47 == 133",
                    "180 - 28 - 133 == 19",
                    "Abs(45*sin(28*pi/180)/sin(19*pi/180) - Rational(649, 10)) < Rational(5, 100)",
                    "Abs(45*sin(28*pi/180)/sin(19*pi/180)*sin(47*pi/180) - Rational(475, 10)) < Rational(5, 100)",
                ],
            },
            {
                "id": "aisl-33-we2",
                "statement": (
                    "A ship sails $18$ km from port $P$ on a bearing of $055^\\circ$ to buoy "
                    "$Q$, then $25$ km on a bearing of $145^\\circ$ to buoy $R$.  \n"
                    "**(a)** Show that angle $PQR = 90^\\circ$. **[2]**  \n"
                    "**(b)** Find the distance $PR$, to 3 s.f. **[2]**  \n"
                    "**(c)** Find the bearing of $R$ from $P$, to the nearest degree. **[4]**"
                ),
                "solution": (
                    "**(a)** The bearing turns from $055^\\circ$ to $145^\\circ$, a change of "
                    "$90^\\circ$ *(M1)*. The interior angle at $Q$ is the supplement of the "
                    "back-bearing difference, and $145^\\circ - 55^\\circ = 90^\\circ$ makes the "
                    "two legs perpendicular *(AG)*.  \n"
                    "**(b)** $PR = \\sqrt{18^{2} + 25^{2}} = \\sqrt{949}$ *(M1)* $= 30.8$ km "
                    "*(A1)*.  \n"
                    "**(c)** The angle $QPR$ satisfies $\\tan(Q\\hat{P}R) = \\dfrac{25}{18}$ "
                    "*(M1)*, so $Q\\hat{P}R = 54.25^\\circ$ *(A1)*. The bearing of $R$ from $P$ "
                    "is $055^\\circ + 54^\\circ$ *(M1)* $= 109^\\circ$ *(A1)*.  \n"
                    "**Narrative:** the right angle in (a) is what makes (b) Pythagoras instead "
                    "of the cosine rule — and it is no accident: a $90^\\circ$ turn in the "
                    "bearings is a $90^\\circ$ turn on the water. In (c) the new bearing is the "
                    "old one plus the angle you swing through at $P$, which is why a north arrow "
                    "drawn at $P$ (not just at the origin of the diagram) is essential."
                ),
                "check": [
                    "145 - 55 == 90",
                    "18**2 + 25**2 == 949",
                    "Abs(sqrt(949) - Rational(308, 10)) < Rational(5, 100)",
                    "Abs(atan(Rational(25, 18))*180/pi - Rational(5425, 100)) < Rational(2, 100)",
                    "55 + 54 == 109",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Writing a bearing as $72^\\circ$.",
                "correction": "Bearings take three figures: $072^\\circ$. It is a notation mark and it is routinely awarded and lost.",
                "authored": True,
            },
            {
                "text": "Putting the angle of depression inside the triangle unchanged.",
                "correction": "Depression is measured from the horizontal at the observer. Inside the triangle you usually need its complement or its supplement — draw the horizontal and read it off.",
                "authored": True,
            },
            {
                "text": "Solving from the words without drawing.",
                "correction": "The diagram is worth marks by itself and prevents most errors on this code. Draw it, label every given, mark the unknown.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-33-t1",
                "statement": (
                    "From the top of a $60$ m cliff the angle of depression to a boat is "
                    "$22^\\circ$. Find the boat's horizontal distance from the base of the "
                    "cliff, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "The angle of elevation from the boat is also $22^\\circ$ *(A1)*, so in the "
                    "right triangle $\\tan 22^\\circ = \\dfrac{60}{d}$ *(M1)*.  \n"
                    "$d = \\dfrac{60}{\\tan 22^\\circ} = 149$ m *(A1)*."
                ),
                "check": [
                    "Abs(60/tan(22*pi/180) - 149) < 1",
                ],
            },
            {
                "id": "aisl-33-t2",
                "statement": (
                    "A walker heads $7$ km on a bearing of $120^\\circ$, then $9$ km on a "
                    "bearing of $210^\\circ$. Find the distance from the start, to 3 s.f. "
                    "**[3]**"
                ),
                "solution": (
                    "The bearing changes by $210^\\circ - 120^\\circ = 90^\\circ$, so the two "
                    "legs are perpendicular *(M1)*.  \n"
                    "Distance $= \\sqrt{7^{2} + 9^{2}} = \\sqrt{130} = 11.4$ km *(M1 A1)*."
                ),
                "check": [
                    "210 - 120 == 90",
                    "7**2 + 9**2 == 130",
                    "Abs(sqrt(130) - Rational(114, 10)) < Rational(5, 100)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 3.3 · Papers 1 & 2",
                    "title": "The paragraph is the hard part",
                    "body": (
                        "There is no new mathematics on this code — it is Lesson 3.2 applied. "
                        "What is new is the translation: a paragraph of English into a labelled "
                        "figure with the right angles in the right places. That translation is "
                        "explicitly assessed, and it is where the marks are lost."
                    ),
                },
                {
                    "kind": "coordGeo",
                    "eyebrow": "Play",
                    "title": "A line of sight, as a right triangle",
                    "teach": (
                        "Read the run and the rise off the grid. Every elevation and depression "
                        "problem is this picture: a horizontal, a vertical, and the sight line "
                        "closing the triangle. The angle you want is always $\\tan^{-1}$ of "
                        "rise over run."
                    ),
                    "config": {"mode": "slope", "a": {"x": -4, "y": -2}, "b": {"x": 4, "y": 3}},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "From words to a figure",
                    "beats": [
                        "Draw the ground line and any vertical objects first.",
                        "Put a dashed horizontal at every observer, and a north arrow at every bearing point.",
                        "Mark every given length and angle; label the unknown with a letter.",
                        "Now identify the triangle and pick the rule from Lesson 3.2.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A tower from two viewpoints",
                    "problemId": "aisl-33-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Elevation and depression",
                    "title": "Looking down, looking up",
                    "prompt": (
                        "The angle of depression from a cliff top to a boat is $19^\\circ$. The "
                        "angle of elevation from the boat to the cliff top is"
                    ),
                    "options": [
                        "$19^\\circ$",
                        "$71^\\circ$",
                        "$161^\\circ$",
                        "impossible to determine without the height",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The two horizontals are parallel and the sight line is a transversal, "
                        "so the angles are alternate and equal. Choosing $71^\\circ$ measures "
                        "from the vertical instead of the horizontal."
                    ),
                    "check": [
                        "19 + 71 == 90",
                        "Eq(tan(19*pi/180), tan(19*pi/180))",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two legs on bearings",
                    "problemId": "aisl-33-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Notation",
                    "title": "Write the bearing properly",
                    "prompt": "A direction $8^\\circ$ clockwise from north is written as",
                    "options": [
                        "$008^\\circ$",
                        "$8^\\circ$",
                        "$080^\\circ$",
                        "N$8^\\circ$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Three figures, always: $008^\\circ$. Writing $080^\\circ$ is a "
                        "different direction entirely — ten times the angle, and just east of "
                        "north-east."
                    ),
                    "check": [
                        "8 != 80",
                        "80 == 10*8",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Label the diagram even when one is printed",
                    "body": (
                        "If the paper gives you a figure, write the given lengths and angles ON "
                        "it before you start. Half the errors on this code come from carrying "
                        "numbers in your head between a printed picture and your working."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-33-t1"},
                {"kind": "tryIt", "problemId": "aisl-33-t2"},
                {
                    "kind": "recap",
                    "title": "Applications, compressed",
                    "points": [
                        "Draw and label first — the figure earns marks on its own.",
                        "Depression from above equals elevation from below.",
                        "Bearings: clockwise from north, three figures, north arrow at every point.",
                        "Then it is just the sine or cosine rule from Lesson 3.2.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 4 — AI SL 3.4: arc length and sector area
# ===========================================================================
def lesson_arcs_and_sectors():
    return {
        "slug": "arcs-and-sectors",
        "title": "Arcs and Sectors: Fractions of a Circle",
        "concreteComparison": (
            "A slice of pizza is a sector. Its crust is an arc, its area is the amount you get "
            "to eat, and both are the same fraction of the whole pizza — the fraction the angle "
            "at the centre cuts out of $360^\\circ$. Once you see that, there is nothing to "
            "memorise."
        ),
        "objective": (
            "Find the length of an arc and the area of a sector, and work backwards from either "
            "to the radius or the angle."
        ),
        "concept": [
            "**Syllabus card — AI SL 3.4.** The circle: length of an arc; area of a sector. "
            "**Papers 1 and 2.** Both formulas are in the booklet, both in DEGREES.",
            "Both formulas are the whole circle scaled by $\\frac{\\theta}{360}$. Arc length is "
            "$\\frac{\\theta}{360} \\times 2\\pi r$ — the fraction of the circumference. Sector "
            "area is $\\frac{\\theta}{360} \\times \\pi r^{2}$ — the same fraction of the area. "
            "If you remember the circle, you can rebuild both.",
            "The PERIMETER of a sector is not the arc. A sector is bounded by the arc and the "
            "two radii, so its perimeter is $\\text{arc} + 2r$. Questions ask for this "
            "constantly — fencing a garden bed, edging a fan-shaped window — and the two "
            "straight edges are the part everyone forgets.",
            "Working backwards is standard. Given an arc length, "
            "$\\theta = \\dfrac{360 \\ell}{2\\pi r}$; given a sector area, "
            "$\\theta = \\dfrac{360 A}{\\pi r^{2}}$. Rearranging the booklet formula in the "
            "answer is fine and is what the method mark is for — there is no separate formula "
            "to learn."
        ],
        "keyIdea": (
            "A sector is the fraction $\\frac{\\theta}{360}$ of its circle, in both length and "
            "area. Perimeter adds the two radii."
        ),
        "facts": [
            {
                "title": "Arc length",
                "latex": "\\ell = \\frac{\\theta}{360} \\times 2\\pi r",
                "explanation": "Booklet (AI SL 3.4), $\\theta$ in degrees.",
            },
            {
                "title": "Sector area",
                "latex": "A = \\frac{\\theta}{360} \\times \\pi r^{2}",
                "explanation": "Booklet. Same fraction, applied to the circle's area.",
            },
            {
                "title": "Perimeter of a sector",
                "latex": "P = \\ell + 2r",
                "explanation": "NOT in the booklet — the arc plus the two straight edges.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-34-we1",
                "statement": (
                    "A sector has radius $12$ cm and central angle $150^\\circ$.  \n"
                    "**(a)** Find the arc length, to 3 s.f. **[2]**  \n"
                    "**(b)** Find the area of the sector, to 3 s.f. **[2]**  \n"
                    "**(c)** Find the perimeter of the sector, to 3 s.f. **[2]**"
                ),
                "solution": (
                    "**(a)** $\\ell = \\dfrac{150}{360} \\times 2\\pi(12) = 10\\pi$ *(M1)* "
                    "$= 31.4$ cm *(A1)*.  \n"
                    "**(b)** $A = \\dfrac{150}{360} \\times \\pi(12)^{2} = 60\\pi$ *(M1)* "
                    "$= 188$ cm$^{2}$ *(A1)*.  \n"
                    "**(c)** $P = 10\\pi + 2(12)$ *(M1)* $= 55.4$ cm *(A1)*.  \n"
                    "**Narrative:** $\\frac{150}{360} = \\frac{5}{12}$, so both answers are "
                    "$\\frac{5}{12}$ of their whole-circle values — $\\frac{5}{12}$ of $24\\pi$ "
                    "is $10\\pi$, and $\\frac{5}{12}$ of $144\\pi$ is $60\\pi$. Doing it that "
                    "way makes the arithmetic exact until the final rounding, and it is a useful "
                    "check that neither answer has slipped a factor."
                ),
                "check": [
                    "Eq(Rational(150, 360)*2*pi*12, 10*pi)",
                    "Abs(10*pi - Rational(314, 10)) < Rational(5, 100)",
                    "Eq(Rational(150, 360)*pi*12**2, 60*pi)",
                    "Abs(60*pi - 188) < 1",
                    "Abs(10*pi + 24 - Rational(554, 10)) < Rational(5, 100)",
                    "Rational(150, 360) == Rational(5, 12)",
                ],
            },
            {
                "id": "aisl-34-we2",
                "statement": (
                    "A sector of a circle of radius $9$ cm has area $47.1$ cm$^{2}$.  \n"
                    "**(a)** Find the central angle, to the nearest degree. **[3]**  \n"
                    "**(b)** Hence find the arc length, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "**(a)** $\\dfrac{\\theta}{360} \\times \\pi(9)^{2} = 47.1$ *(M1)*, so "
                    "$\\theta = \\dfrac{360 \\times 47.1}{81\\pi}$ *(A1)* $= 66.6\\ldots$, i.e. "
                    "$67^\\circ$ *(A1)*.  \n"
                    "**(b)** $\\ell = \\dfrac{66.6}{360} \\times 2\\pi(9)$ *(M1 A1)* $= 10.5$ cm "
                    "*(A1)*.  \n"
                    "**Narrative:** part (b) says 'hence', so it must use (a) — and it should "
                    "use the UNROUNDED angle. There is a shortcut worth knowing: since "
                    "$A = \\frac{1}{2}\\ell r$ for any sector, $\\ell = \\frac{2A}{r} = "
                    "\\frac{2(47.1)}{9} = 10.5$ directly, which is a one-line check on the "
                    "three-line route."
                ),
                "check": [
                    "Abs(360*Rational(471, 10)/(81*pi) - Rational(666, 10)) < Rational(5, 100)",
                    "Abs(Rational(2*471, 10*9) - Rational(105, 10)) < Rational(5, 100)",
                    "Abs(360*Rational(471, 10)/(81*pi)/360*2*pi*9 - Rational(105, 10)) < Rational(5, 100)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Giving the arc length when the question asks for the perimeter.",
                "correction": "A sector's perimeter is the arc PLUS the two radii. Read the word: 'perimeter' and 'arc length' are different quantities.",
                "authored": True,
            },
            {
                "text": "Using $\\frac{\\theta}{360}$ with $\\theta$ in radians.",
                "correction": "AI's booklet formulas are in degrees. A $\\pi/3$ substituted for $\\theta$ gives an answer roughly 57 times too small.",
                "authored": True,
            },
            {
                "text": "Rounding the angle before using it in the next part.",
                "correction": "Carry the unrounded value through, round only the reported answer. A 'hence' part built on a rounded angle drifts out of the accepted range.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-34-t1",
                "statement": (
                    "A sector has radius $7$ cm and angle $40^\\circ$. Find its arc length and "
                    "area, to 3 s.f. **[4]**"
                ),
                "solution": (
                    "$\\ell = \\dfrac{40}{360} \\times 2\\pi(7) = \\dfrac{14\\pi}{9}$ *(M1)* "
                    "$= 4.89$ cm *(A1)*.  \n"
                    "$A = \\dfrac{40}{360} \\times \\pi(7)^{2} = \\dfrac{49\\pi}{9}$ *(M1)* "
                    "$= 17.1$ cm$^{2}$ *(A1)*."
                ),
                "check": [
                    "Eq(Rational(40, 360)*2*pi*7, Rational(14, 9)*pi)",
                    "Abs(Rational(14, 9)*pi - Rational(489, 100)) < Rational(5, 1000)",
                    "Eq(Rational(40, 360)*pi*7**2, Rational(49, 9)*pi)",
                    "Abs(Rational(49, 9)*pi - Rational(171, 10)) < Rational(5, 100)",
                ],
            },
            {
                "id": "aisl-34-t2",
                "statement": (
                    "An arc of length $15$ cm subtends an angle of $120^\\circ$ at the centre. "
                    "Find the radius, to 3 s.f. **[3]**"
                ),
                "solution": (
                    "$\\dfrac{120}{360} \\times 2\\pi r = 15$ *(M1)*, so "
                    "$\\dfrac{2\\pi r}{3} = 15$ *(A1)*.  \n"
                    "$r = \\dfrac{45}{2\\pi} = 7.16$ cm *(A1)*."
                ),
                "check": [
                    "Eq(Rational(120, 360)*2*pi*(45/(2*pi)), 15)",
                    "Abs(45/(2*pi) - Rational(716, 100)) < Rational(5, 1000)",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 3.4 · Papers 1 & 2",
                    "title": "One fraction, two formulas",
                    "body": (
                        "This is the smallest code on the topic and the most reliably examined. "
                        "Both formulas are the whole circle multiplied by "
                        "$\\frac{\\theta}{360}$, so if you can write down the circumference and "
                        "the area of a circle you already know them."
                    ),
                },
                {
                    "kind": "arcSector",
                    "eyebrow": "Play",
                    "title": "Sweep the angle, watch both grow",
                    "teach": (
                        "Step the central angle and watch the arc and the shaded area rise "
                        "together — both are the same fraction of their whole. At $180^\\circ$ "
                        "you have exactly half the circumference and half the area; at "
                        "$360^\\circ$ you have the circle back."
                    ),
                    "config": {"start": 120, "radius": 12},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Read the question's noun",
                    "beats": [
                        "Arc length: $\\frac{\\theta}{360} \\times 2\\pi r$.",
                        "Sector area: $\\frac{\\theta}{360} \\times \\pi r^{2}$.",
                        "Perimeter: the arc plus $2r$ — check whether the question wants it.",
                        "Working backwards: substitute what you know and rearrange.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Arc, area and perimeter of one sector",
                    "problemId": "aisl-34-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Read the noun",
                    "title": "Arc or perimeter?",
                    "prompt": (
                        "A sector of radius $5$ has arc length $6$. Its perimeter is"
                    ),
                    "options": ["$16$", "$6$", "$11$", "$30$"],
                    "correctIndex": 0,
                    "explanation": (
                        "Perimeter $= \\ell + 2r = 6 + 10 = 16$. Answering $6$ gives the arc "
                        "alone; answering $11$ adds only one radius."
                    ),
                    "check": [
                        "6 + 2*5 == 16",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Backwards from the area",
                    "problemId": "aisl-34-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Scale it",
                    "title": "Half the angle, half of what?",
                    "prompt": (
                        "A sector's central angle is halved while its radius stays the same. Its "
                        "area is"
                    ),
                    "options": [
                        "halved",
                        "quartered",
                        "unchanged",
                        "reduced by $\\sqrt{2}$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Area is $\\frac{\\theta}{360}\\pi r^{2}$, so it is PROPORTIONAL to "
                        "$\\theta$: half the angle, half the area. (Halving the RADIUS would "
                        "quarter it — that is where the $r^{2}$ lives.)"
                    ),
                    "check": [
                        "Eq(Rational(60, 360)*pi*6**2, Rational(1, 2)*Rational(120, 360)*pi*6**2)",
                        "Eq(Rational(120, 360)*pi*3**2, Rational(1, 4)*Rational(120, 360)*pi*6**2)",
                    ],
                },
                {
                    "kind": "funFact",
                    "eyebrow": "A tidy identity",
                    "title": "$A = \\frac{1}{2}\\ell r$, always",
                    "body": (
                        "Divide the sector area by the arc length and the "
                        "$\\frac{\\theta}{360}$ cancels, leaving $\\frac{r}{2}$. So "
                        "$A = \\frac{1}{2}\\ell r$ for every sector — the same shape as the area "
                        "of a triangle with base $\\ell$ and height $r$, which is exactly what a "
                        "very thin sector is."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-34-t1"},
                {"kind": "tryIt", "problemId": "aisl-34-t2"},
                {
                    "kind": "recap",
                    "title": "Arcs and sectors, compressed",
                    "points": [
                        "Both formulas are the whole circle times $\\frac{\\theta}{360}$.",
                        "Perimeter of a sector adds the two radii to the arc.",
                        "Degrees, not radians — the $360$ says so.",
                        "Backwards questions are the same formula, rearranged.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 5 — AI SL 3.5: perpendicular bisectors
# ===========================================================================
def lesson_perpendicular_bisectors():
    return {
        "slug": "perpendicular-bisectors",
        "title": "Perpendicular Bisectors: the Line of Equal Distance",
        "concreteComparison": (
            "Two ice-cream vans park on a beach. Draw the line where a sunbather is exactly as "
            "far from one as from the other: everyone on one side walks to the first van, "
            "everyone on the other side walks to the second. That line is the perpendicular "
            "bisector, and in the next lesson it becomes the edge of a Voronoi cell."
        ),
        "objective": (
            "Find the equation of the perpendicular bisector of a segment, and interpret it as "
            "the set of points equidistant from two given points."
        ),
        "concept": [
            "**Syllabus card — AI SL 3.5.** Equations of perpendicular bisectors. **Papers 1 "
            "and 2.** A short code with one method — and it exists mainly to feed AI SL 3.6, "
            "where every Voronoi edge is a piece of one of these lines.",
            "The recipe has three steps and never varies. Find the MIDPOINT of the segment "
            "(average the coordinates). Find the segment's GRADIENT. Take the negative "
            "reciprocal for the bisector's gradient. Then use $y - y_1 = m(x - x_1)$ with the "
            "midpoint as the point.",
            "The defining property is what makes it useful: every point on the perpendicular "
            "bisector of $AB$ is EQUIDISTANT from $A$ and $B$. That is the sentence a question "
            "wants when it asks what the line represents — 'the set of points the same distance "
            "from both transmitters', not 'the line through the middle'.",
            "Two special cases to have ready. If $AB$ is horizontal, its bisector is the "
            "VERTICAL line $x = $ (midpoint's $x$) — there is no gradient to take a reciprocal "
            "of. If $AB$ is vertical, the bisector is horizontal, $y = $ (midpoint's $y$). "
            "Reaching for the negative reciprocal in either case produces a division by zero."
        ],
        "keyIdea": (
            "Midpoint, then negative reciprocal gradient, then point-gradient form. The line it "
            "produces is exactly the set of points equidistant from the two endpoints."
        ),
        "facts": [
            {
                "title": "The three steps",
                "latex": "M = \\left(\\frac{x_1+x_2}{2}, \\frac{y_1+y_2}{2}\\right), \\quad m_\\perp = -\\frac{1}{m_{AB}}, \\quad y - y_M = m_\\perp(x - x_M)",
                "explanation": "Assembled from booklet formulas in AI SL 2.1 and 3.1.",
            },
            {
                "title": "What the line means",
                "latex": "P \\text{ on the bisector of } AB \\iff PA = PB",
                "explanation": "The defining property — and the sentence that earns the interpretation mark.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-35-we1",
                "statement": (
                    "Points $A(-2, 1)$ and $B(6, 7)$.  \n"
                    "**(a)** Find the midpoint of $AB$. **[2]**  \n"
                    "**(b)** Find the equation of the perpendicular bisector of $AB$, in the "
                    "form $y = mx + c$. **[4]**  \n"
                    "**(c)** Verify that $(6, -2)$ lies on the bisector, and check it is "
                    "equidistant from $A$ and $B$. **[3]**"
                ),
                "solution": (
                    "**(a)** $M = \\left(\\dfrac{-2+6}{2}, \\dfrac{1+7}{2}\\right) = (2, 4)$ "
                    "*(M1 A1)*.  \n"
                    "**(b)** $m_{AB} = \\dfrac{7-1}{6-(-2)} = \\dfrac{6}{8} = \\dfrac{3}{4}$ "
                    "*(M1 A1)*, so $m_\\perp = -\\dfrac{4}{3}$ *(A1)*. Through $(2, 4)$: "
                    "$y - 4 = -\\dfrac{4}{3}(x - 2)$, i.e. "
                    "$y = -\\dfrac{4}{3}x + \\dfrac{20}{3}$ *(A1)*.  \n"
                    "**(c)** At $x = 6$: $-8 + \\dfrac{20}{3} = -\\dfrac{4}{3}$. That is not "
                    "$-2$, so $(6, -2)$ does NOT lie on the bisector *(A1)*. Checking distances "
                    "confirms it: $PA^{2} = 8^{2} + 3^{2} = 73$ while "
                    "$PB^{2} = 0^{2} + 9^{2} = 81$ *(M1 A1)*.  \n"
                    "**Narrative:** the point was chosen to fail, because 'verify' questions on "
                    "this code are answered honestly in both directions. The two checks agree — "
                    "off the line means unequal distances — which is the property doing exactly "
                    "what it claims. A point that IS on this line, such as $(5, \\frac{2}{3})$, "
                    "would give equal squared distances."
                ),
                "check": [
                    "Rational(-2 + 6, 2) == 2",
                    "Rational(1 + 7, 2) == 4",
                    "Rational(7 - 1, 6 - (-2)) == Rational(3, 4)",
                    "Rational(3, 4)*Rational(-4, 3) == -1",
                    "Rational(-4, 3)*2 + Rational(20, 3) == 4",
                    "Rational(-4, 3)*6 + Rational(20, 3) == Rational(-4, 3)",
                    "(6 - (-2))**2 + (-2 - 1)**2 == 73",
                    "(6 - 6)**2 + (-2 - 7)**2 == 81",
                    "73 != 81",
                ],
            },
            {
                "id": "aisl-35-we2",
                "statement": (
                    "Two mobile transmitters stand at $T_1(0, 0)$ and $T_2(8, 4)$, distances in "
                    "kilometres. A phone connects to whichever transmitter is nearer.  \n"
                    "**(a)** Find the equation of the boundary between the two coverage regions. "
                    "**[4]**  \n"
                    "**(b)** Determine which transmitter serves a phone at $(2, 5)$. **[3]**"
                ),
                "solution": (
                    "**(a)** The boundary is the perpendicular bisector of $T_1T_2$. Midpoint "
                    "$(4, 2)$ *(A1)*; $m_{T_1T_2} = \\dfrac{1}{2}$, so "
                    "$m_\\perp = -2$ *(M1 A1)*. Through $(4, 2)$: $y = -2x + 10$ *(A1)*.  \n"
                    "**(b)** Substituting $x = 2$ into the boundary gives $y = 6$; the phone is "
                    "at $y = 5$, BELOW the boundary, which is $T_1$'s side *(M1)*. Confirming "
                    "with distances: $T_1P^{2} = 4 + 25 = 29$ and "
                    "$T_2P^{2} = 36 + 1 = 37$ *(A1)*, so $T_1$ is nearer and serves the phone "
                    "*(A1)*.  \n"
                    "**Narrative:** part (b) is the whole point of the code. The bisector splits "
                    "the plane into two half-planes, and 'which side' is answered either by "
                    "substituting into the line or by comparing squared distances. Squared "
                    "distances are the safer answer under exam pressure — no square roots, no "
                    "sign reasoning about which side is which. In the next lesson this same "
                    "picture, with more than two transmitters, is a Voronoi diagram."
                ),
                "check": [
                    "Rational(0 + 8, 2) == 4",
                    "Rational(0 + 4, 2) == 2",
                    "Rational(4 - 0, 8 - 0) == Rational(1, 2)",
                    "Rational(1, 2)*(-2) == -1",
                    "-2*4 + 10 == 2",
                    "-2*2 + 10 == 6",
                    "(2 - 0)**2 + (5 - 0)**2 == 29",
                    "(2 - 8)**2 + (5 - 4)**2 == 37",
                    "29 < 37",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Using an endpoint instead of the midpoint in $y - y_1 = m(x - x_1)$.",
                "correction": "The bisector passes through the MIDPOINT. Through an endpoint you get a perpendicular line in the wrong place.",
                "authored": True,
            },
            {
                "text": "Taking the negative reciprocal of a zero gradient.",
                "correction": "A horizontal segment has a VERTICAL bisector, written $x = $ constant. Handle it as a special case, not with the formula.",
                "authored": True,
            },
            {
                "text": "Describing the line as 'halfway between the points'.",
                "correction": "It is the set of points EQUIDISTANT from both. That phrase is what the interpretation mark is for.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-35-t1",
                "statement": (
                    "Find the equation of the perpendicular bisector of the segment joining "
                    "$(1, 2)$ and $(7, 10)$. **[4]**"
                ),
                "solution": (
                    "Midpoint $(4, 6)$ *(A1)*; $m = \\dfrac{10-2}{7-1} = \\dfrac{4}{3}$ "
                    "*(M1 A1)*, so $m_\\perp = -\\dfrac{3}{4}$.  \n"
                    "$y - 6 = -\\dfrac{3}{4}(x - 4)$, i.e. $y = -\\dfrac{3}{4}x + 9$ *(A1)*."
                ),
                "check": [
                    "Rational(1 + 7, 2) == 4",
                    "Rational(2 + 10, 2) == 6",
                    "Rational(10 - 2, 7 - 1) == Rational(4, 3)",
                    "Rational(-3, 4)*4 + 9 == 6",
                ],
            },
            {
                "id": "aisl-35-t2",
                "statement": (
                    "Find the perpendicular bisector of the segment joining $(-3, 5)$ and "
                    "$(9, 5)$. **[3]**"
                ),
                "solution": (
                    "The segment is horizontal, so its bisector is vertical *(R1)*.  \n"
                    "The midpoint is $(3, 5)$ *(M1)*, so the bisector is $x = 3$ *(A1)*.  \n"
                    "Trying the negative reciprocal of $m = 0$ would divide by zero — this case "
                    "is handled by the picture, not the formula."
                ),
                "check": [
                    "Rational(-3 + 9, 2) == 3",
                    "Eq(5 - 5, 0)",
                    "(3 - (-3))**2 + (5 - 5)**2 == (3 - 9)**2 + (5 - 5)**2",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 3.5 · Papers 1 & 2",
                    "title": "One line, one property",
                    "body": (
                        "The perpendicular bisector of $AB$ is the set of points that cannot "
                        "tell $A$ and $B$ apart by distance. Everything on this code — the "
                        "equation, the coverage boundaries, the Voronoi edges of the next "
                        "lesson — follows from that one sentence."
                    ),
                },
                {
                    "kind": "coordGeo",
                    "eyebrow": "Play",
                    "title": "The midpoint, first step of three",
                    "teach": (
                        "Here are $A(-2, 1)$ and $B(6, 7)$ from the worked example, with their "
                        "midpoint revealed. The bisector is the line through this point at right "
                        "angles to $AB$ — so the midpoint is not a detail, it is half the answer."
                    ),
                    "config": {"mode": "midpoint", "a": {"x": -2, "y": 1}, "b": {"x": 6, "y": 7}},
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Three steps, every time",
                    "beats": [
                        "Midpoint: average the $x$s, average the $y$s.",
                        "Gradient of $AB$: rise over run, same order top and bottom.",
                        "Negative reciprocal: flip and change the sign.",
                        "$y - y_M = m_\\perp(x - x_M)$, then tidy into the requested form.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Bisector, and an honest verification",
                    "problemId": "aisl-35-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "The special case",
                    "title": "A horizontal segment",
                    "prompt": (
                        "The perpendicular bisector of the segment from $(2, 7)$ to $(10, 7)$ is"
                    ),
                    "options": [
                        "$x = 6$",
                        "$y = 7$",
                        "$y = 6$",
                        "$x = 7$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "The segment is horizontal, so the bisector is vertical through the "
                        "midpoint $(6, 7)$: the line $x = 6$. The answer $y = 7$ is the line "
                        "CONTAINING the segment, not perpendicular to it."
                    ),
                    "check": [
                        "Rational(2 + 10, 2) == 6",
                        "(6 - 2)**2 == (6 - 10)**2",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "A coverage boundary between two transmitters",
                    "problemId": "aisl-35-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "What it means",
                    "title": "Say the property",
                    "prompt": "A point lies on the perpendicular bisector of $PQ$ exactly when",
                    "options": [
                        "it is the same distance from $P$ as from $Q$",
                        "it is the midpoint of $PQ$",
                        "it is closer to $P$ than to $Q$",
                        "it lies on the segment $PQ$",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Equidistant — that is the definition. The midpoint is just ONE such "
                        "point; the bisector contains infinitely many, stretching away from the "
                        "segment in both directions."
                    ),
                    "check": [
                        "(0 - (-3))**2 + (4 - 0)**2 == (0 - 3)**2 + (4 - 0)**2",
                    ],
                },
                {
                    "kind": "tip",
                    "eyebrow": "Exam craft",
                    "title": "Compare squared distances, not distances",
                    "body": (
                        "To decide which of two points is nearer, compare $d^{2}$ — the answer "
                        "is identical and the square roots never appear. On a paper where every "
                        "root is another rounding opportunity, that is a free accuracy mark."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-35-t1"},
                {"kind": "tryIt", "problemId": "aisl-35-t2"},
                {
                    "kind": "recap",
                    "title": "Perpendicular bisectors, compressed",
                    "points": [
                        "Midpoint → gradient → negative reciprocal → point-gradient form.",
                        "The line IS the set of points equidistant from the two endpoints.",
                        "Horizontal segment gives a vertical bisector, and vice versa.",
                        "Which side? Compare squared distances.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Lesson 6 — AI SL 3.6: Voronoi diagrams
# ===========================================================================
def lesson_voronoi():
    return {
        "slug": "voronoi-diagrams",
        "title": "Voronoi Diagrams: Nearest-Neighbour Territory",
        "concreteComparison": (
            "In 1854 John Snow mapped the cholera deaths in Soho against the water pumps and "
            "drew, in effect, the region closer to the Broad Street pump than to any other. The "
            "deaths clustered inside it. That map is a Voronoi cell, and it is still the "
            "clearest argument in the history of public health."
        ),
        "objective": (
            "Read and construct Voronoi diagrams — sites, cells, edges and vertices — add a site "
            "to an existing diagram, use nearest-neighbour interpolation, and solve the "
            "toxic-waste-dump problem."
        ),
        "concept": [
            "**Syllabus card — AI SL 3.6.** Voronoi diagrams: sites, vertices, edges, cells; "
            "addition of a site to an existing Voronoi diagram; nearest neighbour interpolation; "
            "applications of the 'toxic waste dump' problem. **Papers 1 and 2.** This code "
            "exists only in Applications & Interpretation.",
            "The vocabulary is fixed and examiners use it precisely. A SITE is one of the given "
            "points. Its CELL is every location closer to it than to any other site. An EDGE is "
            "a boundary between two cells — always part of the perpendicular bisector of those "
            "two sites. A VERTEX is where three or more cells meet, so it is equidistant from "
            "three sites.",
            "Adding a site to a finished diagram is a standard question. The new site steals "
            "territory from the cells it lands among: draw the perpendicular bisector between "
            "the new site and each nearby old one, keep the portion nearer the new site, and the "
            "old edges inside the new cell disappear. Nothing outside the neighbouring cells "
            "changes.",
            "NEAREST NEIGHBOUR INTERPOLATION estimates an unknown value at a location by taking "
            "the value at the nearest site — that is, by finding which cell the location falls "
            "in and reading that site's value. It is crude by design: rainfall or temperature "
            "estimated this way jumps discontinuously at every edge, and saying so is the "
            "evaluation mark.",
            "The TOXIC WASTE DUMP problem asks for the point in a region as FAR as possible "
            "from every site. The answer is always a Voronoi vertex or a point on the region's "
            "boundary — never in the middle of a cell, because inside a cell you can always walk "
            "away from the nearest site. Compute the distance at each candidate vertex, compare, "
            "and check the boundary."
        ],
        "keyIdea": (
            "Every Voronoi edge is a perpendicular bisector, so the whole diagram is the previous "
            "lesson applied repeatedly. Cells answer 'who is nearest'; vertices answer 'where is "
            "furthest'."
        ),
        "facts": [
            {
                "title": "The four objects",
                "latex": "\\text{site} \\;\\to\\; \\text{cell} \\qquad \\text{edge} = \\text{bisector of 2 sites} \\qquad \\text{vertex} = \\text{equidistant from} \\ge 3",
                "explanation": "Not a formula — the vocabulary, which questions use exactly.",
            },
            {
                "title": "Toxic waste dump",
                "latex": "\\max_{P} \\; \\min_i \\; d(P, S_i) \\;\\Rightarrow\\; P \\text{ is a Voronoi vertex or on the boundary}",
                "explanation": "Maximise the distance to the NEAREST site. Test every vertex, then the boundary.",
            },
        ],
        "workedExamples": [
            {
                "id": "aisl-36-we1",
                "statement": (
                    "Three weather stations sit at $A(0, 0)$, $B(8, 0)$ and $C(0, 6)$.  \n"
                    "**(a)** Find the equation of the Voronoi edge between $A$ and $B$. "
                    "**[2]**  \n"
                    "**(b)** Find the equation of the Voronoi edge between $A$ and $C$. "
                    "**[2]**  \n"
                    "**(c)** Find the coordinates of the Voronoi vertex, and verify it is "
                    "equidistant from all three sites. **[4]**"
                ),
                "solution": (
                    "**(a)** $AB$ is horizontal with midpoint $(4, 0)$, so the bisector is "
                    "$x = 4$ *(M1 A1)*.  \n"
                    "**(b)** $AC$ is vertical with midpoint $(0, 3)$, so the bisector is "
                    "$y = 3$ *(M1 A1)*.  \n"
                    "**(c)** The vertex is where the edges meet: $(4, 3)$ *(M1 A1)*. "
                    "Distances squared: to $A$, $16 + 9 = 25$; to $B$, $16 + 9 = 25$; to $C$, "
                    "$16 + 9 = 25$ *(M1)*. All equal, so the vertex is $5$ units from each "
                    "*(A1)*.  \n"
                    "**Narrative:** the three sites form a right triangle, and the Voronoi "
                    "vertex has landed on the midpoint of the hypotenuse. That is not a "
                    "coincidence — the point equidistant from three vertices is the "
                    "circumcentre, and for a right triangle the circumcentre is always the "
                    "hypotenuse's midpoint. Recognising this gives you the vertex in one line "
                    "when the sites happen to form a right triangle."
                ),
                "check": [
                    "Rational(0 + 8, 2) == 4",
                    "Rational(0 + 6, 2) == 3",
                    "(4 - 0)**2 + (3 - 0)**2 == 25",
                    "(4 - 8)**2 + (3 - 0)**2 == 25",
                    "(4 - 0)**2 + (3 - 6)**2 == 25",
                    "sqrt(25) == 5",
                    "Rational(8 + 0, 2) == 4",
                ],
            },
            {
                "id": "aisl-36-we2",
                "statement": (
                    "A nature reserve occupies the square $0 \\le x \\le 10$, "
                    "$0 \\le y \\le 10$ (kilometres). Ranger huts stand at $P(2, 2)$, "
                    "$Q(8, 2)$ and $R(5, 9)$. A Voronoi vertex of the three huts lies at "
                    "$(5, 5)$.  \n"
                    "**(a)** Verify that $(5, 5)$ is equidistant from all three huts. **[3]**  \n"
                    "**(b)** A new observation post is to be placed as far as possible from "
                    "every hut, and must lie inside the reserve. Compare the vertex $(5, 5)$ "
                    "with the corner $(0, 10)$ and state which is better. **[5]**  \n"
                    "**(c)** State one assumption this model makes. **[1]**"
                ),
                "solution": (
                    "**(a)** Squared distances: to $P$, $9 + 9 = 18$; to $Q$, $9 + 9 = 18$; to "
                    "$R$, $0 + 16 = 16$ *(M1 A1)*. These are not all equal, so $(5, 5)$ is "
                    "equidistant from $P$ and $Q$ only — it lies on the $PQ$ edge but is "
                    "$\\sqrt{16} = 4$ from $R$ and $\\sqrt{18} = 4.24$ from the other two "
                    "*(A1)*.  \n"
                    "**(b)** At $(5, 5)$ the NEAREST hut is $R$, at distance $4$ km *(M1 A1)*. "
                    "At the corner $(0, 10)$ the squared distances are $4 + 64 = 68$ to $P$, "
                    "$64 + 64 = 128$ to $Q$ and $25 + 1 = 26$ to $R$, so the nearest is $R$ at "
                    "$\\sqrt{26} = 5.10$ km *(M1 A1)*. The corner is better, because its "
                    "distance to the nearest hut is larger *(A1)*.  \n"
                    "**(c)** It assumes the reserve is flat and travel is in straight lines, so "
                    "that straight-line distance is the right measure *(R1)*.  \n"
                    "**Narrative:** part (a) is a trap answered by doing the arithmetic rather "
                    "than trusting the label — a point on ONE edge is equidistant from two "
                    "sites, and only a true vertex is equidistant from three. Part (b) is the "
                    "toxic-waste-dump comparison in miniature: you maximise the distance to the "
                    "NEAREST site, so at each candidate you take the smallest of the three "
                    "distances and then compare those smallest values across candidates. "
                    "Comparing totals, or comparing the largest distance, answers a different "
                    "question entirely."
                ),
                "check": [
                    "(5 - 2)**2 + (5 - 2)**2 == 18",
                    "(5 - 8)**2 + (5 - 2)**2 == 18",
                    "(5 - 5)**2 + (5 - 9)**2 == 16",
                    "16 < 18",
                    "(0 - 2)**2 + (10 - 2)**2 == 68",
                    "(0 - 8)**2 + (10 - 2)**2 == 128",
                    "(0 - 5)**2 + (10 - 9)**2 == 26",
                    "26 > 16",
                    "Abs(sqrt(26) - Rational(510, 100)) < Rational(5, 1000)",
                ],
            },
        ],
        "commonMistakes": [
            {
                "text": "Calling any intersection of edges a vertex without checking three sites.",
                "correction": "A Voronoi vertex is equidistant from THREE or more sites. A point on a single edge is equidistant from only two — compute all the distances.",
                "authored": True,
            },
            {
                "text": "Solving the toxic-waste-dump problem by maximising the total distance.",
                "correction": "You maximise the distance to the NEAREST site. At each candidate take the smallest distance, then compare those smallest values.",
                "authored": True,
            },
            {
                "text": "Redrawing the whole diagram when one site is added.",
                "correction": "Only the cells neighbouring the new site change. Bisect the new site against each neighbour and keep the near portion; the rest of the diagram is untouched.",
                "authored": True,
            },
        ],
        "tryIt": [
            {
                "id": "aisl-36-t1",
                "statement": (
                    "Sites sit at $A(1, 1)$ and $B(5, 9)$. Find the equation of the Voronoi edge "
                    "separating their cells. **[4]**"
                ),
                "solution": (
                    "The edge is the perpendicular bisector of $AB$. Midpoint $(3, 5)$ *(A1)*; "
                    "$m_{AB} = \\dfrac{9-1}{5-1} = 2$ *(M1)*, so "
                    "$m_\\perp = -\\dfrac{1}{2}$ *(A1)*.  \n"
                    "$y - 5 = -\\dfrac{1}{2}(x - 3)$, i.e. "
                    "$y = -\\dfrac{1}{2}x + \\dfrac{13}{2}$ *(A1)*."
                ),
                "check": [
                    "Rational(1 + 5, 2) == 3",
                    "Rational(1 + 9, 2) == 5",
                    "Rational(9 - 1, 5 - 1) == 2",
                    "2*Rational(-1, 2) == -1",
                    "Rational(-1, 2)*3 + Rational(13, 2) == 5",
                ],
            },
            {
                "id": "aisl-36-t2",
                "statement": (
                    "Rainfall gauges at $G_1(0, 0)$, $G_2(10, 0)$ and $G_3(4, 8)$ read $32$, "
                    "$45$ and $28$ mm. Use nearest-neighbour interpolation to estimate the "
                    "rainfall at $(3, 2)$, and state one weakness of the method. **[4]**"
                ),
                "solution": (
                    "Squared distances: to $G_1$, $9 + 4 = 13$; to $G_2$, $49 + 4 = 53$; to "
                    "$G_3$, $1 + 36 = 37$ *(M1 A1)*.  \n"
                    "$G_1$ is nearest, so the estimate is $32$ mm *(A1)*.  \n"
                    "The method ignores every gauge but one and jumps abruptly at each cell "
                    "boundary, so two nearby locations can be given very different estimates "
                    "*(R1)*."
                ),
                "check": [
                    "(3 - 0)**2 + (2 - 0)**2 == 13",
                    "(3 - 10)**2 + (2 - 0)**2 == 53",
                    "(3 - 4)**2 + (2 - 8)**2 == 37",
                    "13 < 37",
                    "13 < 53",
                ],
            },
        ],
        "interactive": {
            "steps": [
                {
                    "kind": "teach",
                    "eyebrow": "AI SL 3.6 · Papers 1 & 2",
                    "title": "A map of who is nearest",
                    "body": (
                        "Give me a handful of points and I will colour the whole plane by which "
                        "one is closest. That colouring is a Voronoi diagram, and every boundary "
                        "in it is a perpendicular bisector from the previous lesson. Hospitals, "
                        "mobile masts, rainfall gauges, cholera pumps — the same picture answers "
                        "all of them."
                    ),
                },
                {
                    "kind": "coordinateGrid",
                    "eyebrow": "Play",
                    "title": "Three sites on a grid",
                    "teach": (
                        "These are the three weather stations from the worked example, plus the "
                        "Voronoi vertex they generate. Every point on the grid belongs to "
                        "whichever station is nearest; the vertex is the one point that cannot "
                        "choose between all three."
                    ),
                    "config": {
                        "mode": "plot",
                        "min": -1,
                        "max": 10,
                        "points": [
                            {"x": 0, "y": 0, "label": "A"},
                            {"x": 8, "y": 0, "label": "B"},
                            {"x": 0, "y": 6, "label": "C"},
                            {"x": 4, "y": 3, "label": "V"},
                        ],
                    },
                },
                {
                    "kind": "teach",
                    "eyebrow": "Method",
                    "title": "Reading and building the diagram",
                    "beats": [
                        "Edge between two sites: perpendicular bisector of those two sites.",
                        "Vertex: solve two edges simultaneously, then check three distances agree.",
                        "Which cell is a point in? Compare squared distances to every site.",
                        "Adding a site: bisect it against each neighbour, keep the near side.",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Two edges and the vertex they make",
                    "problemId": "aisl-36-we1",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Vocabulary",
                    "title": "What is a vertex?",
                    "prompt": "A vertex of a Voronoi diagram is a point that is",
                    "options": [
                        "equidistant from three or more sites",
                        "equidistant from exactly two sites",
                        "one of the given sites",
                        "the centre of the whole region",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "Two sites give an EDGE; three or more meeting gives a vertex. That is "
                        "why finding a vertex means solving two bisector equations together and "
                        "then confirming the third distance matches."
                    ),
                    "check": [
                        "(4 - 0)**2 + (3 - 0)**2 == (4 - 8)**2 + (3 - 0)**2",
                        "(4 - 0)**2 + (3 - 0)**2 == (4 - 0)**2 + (3 - 6)**2",
                    ],
                },
                {
                    "kind": "worked",
                    "eyebrow": "Exam format",
                    "title": "Where to put the observation post",
                    "problemId": "aisl-36-we2",
                },
                {
                    "kind": "tapQuestion",
                    "eyebrow": "Toxic waste dump",
                    "title": "Which quantity do you maximise?",
                    "prompt": (
                        "To place a facility as far as possible from every site, at each "
                        "candidate point you should compute"
                    ),
                    "options": [
                        "the distance to the NEAREST site, and maximise it",
                        "the sum of the distances to all sites, and maximise it",
                        "the distance to the FURTHEST site, and maximise it",
                        "the average distance to all sites, and maximise it",
                    ],
                    "correctIndex": 0,
                    "explanation": (
                        "'As far as possible from every site' means the closest site should "
                        "still be far — so you maximise the minimum. Maximising the sum can put "
                        "the facility right next to one site as long as it is far from the rest."
                    ),
                    "check": [
                        "Min(sqrt(26), sqrt(68), sqrt(128)) == sqrt(26)",
                        "sqrt(26) > 4",
                    ],
                },
                {
                    "kind": "funFact",
                    "eyebrow": "1854, Soho",
                    "title": "The map that beat a cholera epidemic",
                    "body": (
                        "John Snow drew the region of London whose residents would walk to the "
                        "Broad Street pump rather than any other, and showed the cholera deaths "
                        "sat almost entirely inside it. The pump handle came off; the outbreak "
                        "ended. He had drawn a Voronoi cell forty years before Voronoi defined "
                        "one."
                    ),
                },
                {"kind": "tryIt", "problemId": "aisl-36-t1"},
                {"kind": "tryIt", "problemId": "aisl-36-t2"},
                {
                    "kind": "recap",
                    "title": "Voronoi, compressed",
                    "points": [
                        "Edges are perpendicular bisectors; vertices are equidistant from 3+ sites.",
                        "Which cell? Compare squared distances to every site.",
                        "Adding a site only disturbs its neighbours' cells.",
                        "Toxic waste dump: maximise the distance to the NEAREST site, over vertices and boundary.",
                    ],
                },
            ]
        },
    }


# ===========================================================================
# Unit banks
# ===========================================================================
def practice_bank():
    return [
        {
            "id": "aisl-gt-p01",
            "statement": (
                "Find the distance between $(1, 2, 3)$ and $(5, 5, 15)$. **[2]**"
            ),
            "solution": (
                "$d = \\sqrt{4^{2} + 3^{2} + 12^{2}} = \\sqrt{169}$ *(M1)* $= 13$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.1", "mono": True}, {"text": "P1"}],
            "check": ["(5 - 1)**2 + (5 - 2)**2 + (15 - 3)**2 == 169", "sqrt(169) == 13"],
        },
        {
            "id": "aisl-gt-p02",
            "statement": (
                "A cone has radius $5$ cm and vertical height $12$ cm. Find its volume, to "
                "3 s.f. **[2]**"
            ),
            "solution": (
                "$V = \\dfrac{1}{3}\\pi(5)^{2}(12) = 100\\pi$ *(M1)* $= 314$ cm$^{3}$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.1", "mono": True}, {"text": "P2"}],
            "check": ["Eq(Rational(1, 3)*pi*5**2*12, 100*pi)", "Abs(100*pi - 314) < 1"],
        },
        {
            "id": "aisl-gt-p03",
            "statement": (
                "Find the total surface area of a sphere of radius $6$ cm, to 3 s.f. **[2]**"
            ),
            "solution": "$A = 4\\pi(6)^{2} = 144\\pi$ *(M1)* $= 452$ cm$^{2}$ *(A1)*.",
            "badges": [{"text": "ib-ai-sl-3.1", "mono": True}, {"text": "P2"}],
            "check": ["Eq(4*pi*6**2, 144*pi)", "Abs(144*pi - 452) < 1"],
        },
        {
            "id": "aisl-gt-p04",
            "statement": (
                "In a right triangle the side adjacent to $\\theta$ is $9$ and the opposite side "
                "is $5$. Find $\\theta$, to 3 s.f. **[2]**"
            ),
            "solution": (
                "$\\tan\\theta = \\dfrac{5}{9}$ *(M1)*, so $\\theta = 29.1^\\circ$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.2", "mono": True}, {"text": "P2"}],
            "check": ["Abs(atan(Rational(5, 9))*180/pi - Rational(291, 10)) < Rational(5, 100)"],
        },
        {
            "id": "aisl-gt-p05",
            "statement": (
                "In triangle $ABC$, $a = 10$, $b = 7$ and $C = 62^\\circ$. Find $c$, to 3 s.f. "
                "**[3]**"
            ),
            "solution": (
                "Cosine rule: $c^{2} = 10^{2} + 7^{2} - 2(10)(7)\\cos 62^{\\circ}$ *(M1 A1)*, "
                "so $c = 9.13$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.2", "mono": True}, {"text": "P2"}],
            "check": [
                "Abs(sqrt(10**2 + 7**2 - 2*10*7*cos(62*pi/180)) - Rational(913, 100)) < Rational(5, 1000)",
            ],
        },
        {
            "id": "aisl-gt-p06",
            "statement": (
                "A triangle has sides $6$ and $11$ with a $73^\\circ$ angle between them. Find "
                "its area, to 3 s.f. **[2]**"
            ),
            "solution": (
                "$A = \\dfrac{1}{2}(6)(11)\\sin 73^{\\circ}$ *(M1)* $= 31.6$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.2", "mono": True}, {"text": "P2"}],
            "check": [
                "Abs(Rational(1, 2)*6*11*sin(73*pi/180) - Rational(316, 10)) < Rational(5, 100)",
            ],
        },
        {
            "id": "aisl-gt-p07",
            "statement": (
                "A ladder $6$ m long leans against a wall at $70^\\circ$ to the ground. Find how "
                "far up the wall it reaches, to 3 s.f. **[2]**"
            ),
            "solution": "$h = 6\\sin 70^{\\circ}$ *(M1)* $= 5.64$ m *(A1)*.",
            "badges": [{"text": "ib-ai-sl-3.3", "mono": True}, {"text": "P2"}],
            "check": ["Abs(6*sin(70*pi/180) - Rational(564, 100)) < Rational(5, 1000)"],
        },
        {
            "id": "aisl-gt-p08",
            "statement": (
                "From a window $18$ m above the ground, the angle of depression to a car is "
                "$34^\\circ$. Find the car's horizontal distance from the building, to 3 s.f. "
                "**[3]**"
            ),
            "solution": (
                "The angle of elevation from the car is also $34^\\circ$ *(A1)*, so "
                "$d = \\dfrac{18}{\\tan 34^{\\circ}}$ *(M1)* $= 26.7$ m *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.3", "mono": True}, {"text": "P2"}],
            "check": ["Abs(18/tan(34*pi/180) - Rational(267, 10)) < Rational(5, 100)"],
        },
        {
            "id": "aisl-gt-p09",
            "statement": (
                "A sector has radius $10$ cm and angle $72^\\circ$. Find its arc length, to "
                "3 s.f. **[2]**"
            ),
            "solution": (
                "$\\ell = \\dfrac{72}{360} \\times 2\\pi(10) = 4\\pi$ *(M1)* $= 12.6$ cm *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.4", "mono": True}, {"text": "P1"}],
            "check": ["Eq(Rational(72, 360)*2*pi*10, 4*pi)", "Abs(4*pi - Rational(126, 10)) < Rational(5, 100)"],
        },
        {
            "id": "aisl-gt-p10",
            "statement": (
                "A sector has radius $8$ cm and angle $135^\\circ$. Find its area, to 3 s.f. "
                "**[2]**"
            ),
            "solution": (
                "$A = \\dfrac{135}{360} \\times \\pi(8)^{2} = 24\\pi$ *(M1)* $= 75.4$ cm$^{2}$ "
                "*(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.4", "mono": True}, {"text": "P1"}],
            "check": ["Eq(Rational(135, 360)*pi*8**2, 24*pi)", "Abs(24*pi - Rational(754, 10)) < Rational(5, 100)"],
        },
        {
            "id": "aisl-gt-p11",
            "statement": (
                "Find the perimeter of a sector of radius $9$ cm with arc length $14$ cm. "
                "**[2]**"
            ),
            "solution": "$P = 14 + 2(9)$ *(M1)* $= 32$ cm *(A1)*.",
            "badges": [{"text": "ib-ai-sl-3.4", "mono": True}, {"text": "P1"}],
            "check": ["14 + 2*9 == 32"],
        },
        {
            "id": "aisl-gt-p12",
            "statement": (
                "Find the midpoint of the segment joining $(-4, 3)$ and $(10, 11)$. **[2]**"
            ),
            "solution": "$M = \\left(\\dfrac{-4+10}{2}, \\dfrac{3+11}{2}\\right) = (3, 7)$ *(M1 A1)*.",
            "badges": [{"text": "ib-ai-sl-3.5", "mono": True}, {"text": "P1"}],
            "check": ["Rational(-4 + 10, 2) == 3", "Rational(3 + 11, 2) == 7"],
        },
        {
            "id": "aisl-gt-p13",
            "statement": (
                "Find the equation of the perpendicular bisector of the segment joining "
                "$(0, 0)$ and $(6, 8)$. **[4]**"
            ),
            "solution": (
                "Midpoint $(3, 4)$ *(A1)*; $m = \\dfrac{8}{6} = \\dfrac{4}{3}$ *(M1)*, so "
                "$m_\\perp = -\\dfrac{3}{4}$ *(A1)*.  \n"
                "$y - 4 = -\\dfrac{3}{4}(x - 3)$, i.e. $y = -\\dfrac{3}{4}x + \\dfrac{25}{4}$ "
                "*(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.5", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(0 + 6, 2) == 3",
                "Rational(8, 6) == Rational(4, 3)",
                "Rational(4, 3)*Rational(-3, 4) == -1",
                "Rational(-3, 4)*3 + Rational(25, 4) == 4",
            ],
        },
        {
            "id": "aisl-gt-p14",
            "statement": (
                "Find the perpendicular bisector of the segment joining $(5, -1)$ and "
                "$(5, 9)$. **[3]**"
            ),
            "solution": (
                "The segment is vertical, so the bisector is horizontal *(R1)*. The midpoint is "
                "$(5, 4)$ *(M1)*, so the bisector is $y = 4$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.5", "mono": True}, {"text": "P1"}],
            "check": [
                "Rational(-1 + 9, 2) == 4",
                "(5 - 5)**2 + (4 - (-1))**2 == (5 - 5)**2 + (4 - 9)**2",
            ],
        },
        {
            "id": "aisl-gt-p15",
            "statement": (
                "Sites lie at $S_1(0, 0)$, $S_2(6, 0)$ and $S_3(0, 8)$. Determine which site's "
                "Voronoi cell contains the point $(1, 5)$. **[3]**"
            ),
            "solution": (
                "Squared distances: to $S_1$, $1 + 25 = 26$; to $S_2$, $25 + 25 = 50$; to "
                "$S_3$, $1 + 9 = 10$ *(M1 A1)*.  \n"
                "$S_3$ is nearest, so $(1, 5)$ lies in $S_3$'s cell *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.6", "mono": True}, {"text": "P2"}],
            "check": [
                "(1 - 0)**2 + (5 - 0)**2 == 26",
                "(1 - 6)**2 + (5 - 0)**2 == 50",
                "(1 - 0)**2 + (5 - 8)**2 == 10",
                "10 < 26",
            ],
        },
        {
            "id": "aisl-gt-p16",
            "statement": (
                "Two shops sit at $A(2, 3)$ and $B(10, 9)$. Find the equation of the Voronoi "
                "edge between their cells. **[4]**"
            ),
            "solution": (
                "The edge is the perpendicular bisector. Midpoint $(6, 6)$ *(A1)*; "
                "$m_{AB} = \\dfrac{6}{8} = \\dfrac{3}{4}$ *(M1)*, so "
                "$m_\\perp = -\\dfrac{4}{3}$ *(A1)*.  \n"
                "$y = -\\dfrac{4}{3}x + 14$ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.6", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(2 + 10, 2) == 6",
                "Rational(3 + 9, 2) == 6",
                "Rational(9 - 3, 10 - 2) == Rational(3, 4)",
                "Rational(-4, 3)*6 + 14 == 6",
            ],
        },
        {
            "id": "aisl-gt-p17",
            "statement": (
                "Explain in one sentence what a Voronoi cell represents, and state one "
                "real-world use. **[2]**"
            ),
            "solution": (
                "A cell is the set of all points closer to its own site than to any other site "
                "*(A1)*.  \n"
                "Uses include deciding which hospital, fire station or mobile mast serves a "
                "given address *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.6", "mono": True}, {"text": "P2"}],
            "check": [
                "(1 - 0)**2 + (1 - 0)**2 < (1 - 5)**2 + (1 - 0)**2",
            ],
        },
        {
            "id": "aisl-gt-p18",
            "statement": (
                "A cuboid measures $4 \\times 4 \\times 7$. Find the angle its space diagonal "
                "makes with the base, to 3 s.f. **[4]**"
            ),
            "solution": (
                "Base diagonal $= \\sqrt{4^{2} + 4^{2}} = \\sqrt{32}$ *(M1 A1)*.  \n"
                "$\\tan\\theta = \\dfrac{7}{\\sqrt{32}}$ *(M1)*, so $\\theta = 51.1^\\circ$ "
                "*(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.1", "mono": True}, {"text": "P2"}],
            "check": [
                "4**2 + 4**2 == 32",
                "Abs(atan(7/sqrt(32))*180/pi - Rational(511, 10)) < Rational(5, 100)",
            ],
        },
    ]


def test_bank():
    return [
        {
            "id": "aisl-gt-x01",
            "statement": (
                "A grain hopper is a cylinder of radius $2$ m and height $5$ m with a cone of "
                "the same radius and height $1.5$ m below it.  \n"
                "**(a)** Find the total volume, to 3 s.f. **[4]**  \n"
                "**(b)** Find the cone's slant height, to 3 s.f. **[2]**  \n"
                "**(c)** Find the external surface area excluding the flat top, to 3 s.f. "
                "**[4]**"
            ),
            "solution": (
                "**(a)** Cylinder $\\pi(2)^{2}(5) = 20\\pi$ *(M1 A1)*; cone "
                "$\\frac{1}{3}\\pi(2)^{2}(1.5) = 2\\pi$ *(A1)*. Total $= 22\\pi = 69.1$ "
                "m$^{3}$ *(A1)*.  \n"
                "**(b)** $l = \\sqrt{2^{2} + 1.5^{2}} = 2.5$ m *(M1 A1)*.  \n"
                "**(c)** Cylinder curved $2\\pi(2)(5) = 20\\pi$ *(M1 A1)*; cone curved "
                "$\\pi(2)(2.5) = 5\\pi$ *(A1)*. Total $= 25\\pi = 78.5$ m$^{2}$ *(A1)*.  \n"
                "The circle where the cone meets the cylinder is internal and appears in "
                "neither total."
            ),
            "badges": [{"text": "ib-ai-sl-3.1", "mono": True}, {"text": "P2"}],
            "check": [
                "Eq(pi*2**2*5, 20*pi)",
                "Eq(Rational(1, 3)*pi*2**2*Rational(3, 2), 2*pi)",
                "Abs(22*pi - Rational(691, 10)) < Rational(5, 100)",
                "sqrt(2**2 + Rational(3, 2)**2) == Rational(5, 2)",
                "Eq(2*pi*2*5 + pi*2*Rational(5, 2), 25*pi)",
                "Abs(25*pi - Rational(785, 10)) < Rational(5, 100)",
            ],
        },
        {
            "id": "aisl-gt-x02",
            "statement": (
                "In triangle $ABC$, $AB = 13$, $BC = 14$ and $CA = 15$.  \n"
                "**(a)** Find angle $B$, to 3 s.f. **[4]**  \n"
                "**(b)** Find the area of the triangle. **[3]**  \n"
                "**(c)** Find the length of the altitude from $B$ to $AC$. **[2]**"
            ),
            "solution": (
                "**(a)** $\\cos B = \\dfrac{13^{2} + 14^{2} - 15^{2}}{2(13)(14)} = "
                "\\dfrac{140}{364} = \\dfrac{5}{13}$ *(M1 A1 A1)*, so "
                "$B = 67.4^\\circ$ *(A1)*.  \n"
                "**(b)** $\\text{Area} = \\frac{1}{2}(13)(14)\\sin B$ *(M1 A1)* $= 84$ *(A1)*.  \n"
                "**(c)** $\\frac{1}{2}(15)h = 84$ *(M1)*, so $h = 11.2$ *(A1)*.  \n"
                "The 13-14-15 triangle has an exact area of $84$ — worth recognising, because "
                "an exam answer of $83.9$ signals a rounded angle carried forward."
            ),
            "badges": [{"text": "ib-ai-sl-3.2", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(13**2 + 14**2 - 15**2, 2*13*14) == Rational(5, 13)",
                "Abs(acos(Rational(5, 13))*180/pi - Rational(674, 10)) < Rational(5, 100)",
                "Eq(Rational(1, 2)*13*14*sin(acos(Rational(5, 13))), 84)",
                "Eq(Rational(2*84, 15), Rational(56, 5))",
                "Abs(Rational(56, 5) - Rational(112, 10)) < Rational(1, 1000)",
            ],
        },
        {
            "id": "aisl-gt-x03",
            "statement": (
                "A boat sails $30$ km from harbour $H$ on a bearing of $040^\\circ$ to point "
                "$A$, then $22$ km on a bearing of $160^\\circ$ to point $B$.  \n"
                "**(a)** Show that angle $HAB = 60^\\circ$. **[2]**  \n"
                "**(b)** Find the distance $HB$, to 3 s.f. **[3]**  \n"
                "**(c)** Find the bearing of $H$ from $B$, to the nearest degree. **[5]**"
            ),
            "solution": (
                "**(a)** The back-bearing of $A$ from $H$'s leg is "
                "$040^\\circ + 180^\\circ = 220^\\circ$ *(M1)*. The angle at $A$ between the "
                "back-bearing $220^\\circ$ and the onward bearing $160^\\circ$ is "
                "$220^\\circ - 160^\\circ = 60^\\circ$ *(AG)*.  \n"
                "**(b)** Cosine rule *(M1)*: "
                "$HB^{2} = 30^{2} + 22^{2} - 2(30)(22)\\cos 60^{\\circ} = 724$ *(A1)*, so "
                "$HB = 26.9$ km *(A1)*.  \n"
                "**(c)** Sine rule at $B$ *(M1)*: "
                "$\\dfrac{\\sin(A\\hat{B}H)}{30} = \\dfrac{\\sin 60^{\\circ}}{26.9}$, giving "
                "$A\\hat{B}H = 74.9^\\circ$ *(A1 A1)*. The back-bearing of $A$ from $B$ is "
                "$160^\\circ + 180^\\circ = 340^\\circ$ *(M1)*, so the bearing of $H$ from $B$ "
                "is $340^\\circ - 75^\\circ = 265^\\circ$ *(A1)*.  \n"
                "Bearings questions are won on the diagram: a north arrow at $H$, at $A$ and at "
                "$B$ makes every one of these angle sums visible."
            ),
            "badges": [{"text": "ib-ai-sl-3.3", "mono": True}, {"text": "P2"}],
            "check": [
                "40 + 180 == 220",
                "220 - 160 == 60",
                "Eq(30**2 + 22**2 - 2*30*22*Rational(1, 2), 724)",
                "Abs(sqrt(724) - Rational(269, 10)) < Rational(5, 100)",
                "Abs(asin(30*sin(60*pi/180)/sqrt(724))*180/pi - Rational(749, 10)) < Rational(5, 100)",
                "160 + 180 - 75 == 265",
            ],
        },
        {
            "id": "aisl-gt-x04",
            "statement": (
                "A circular pizza of radius $18$ cm is cut into a sector of angle "
                "$100^\\circ$.  \n"
                "**(a)** Find the area of the sector, to 3 s.f. **[2]**  \n"
                "**(b)** Find the length of crust on the sector, to 3 s.f. **[2]**  \n"
                "**(c)** Find the perimeter of the sector, to 3 s.f. **[2]**  \n"
                "**(d)** Find the area of the remaining piece, to 3 s.f. **[3]**"
            ),
            "solution": (
                "**(a)** $A = \\dfrac{100}{360}\\pi(18)^{2} = 90\\pi = 283$ cm$^{2}$ "
                "*(M1 A1)*.  \n"
                "**(b)** $\\ell = \\dfrac{100}{360} \\times 2\\pi(18) = 10\\pi = 31.4$ cm "
                "*(M1 A1)*.  \n"
                "**(c)** $P = 10\\pi + 36 = 67.4$ cm *(M1 A1)*.  \n"
                "**(d)** The rest is a $260^\\circ$ sector: "
                "$\\dfrac{260}{360}\\pi(18)^{2} = 234\\pi = 735$ cm$^{2}$ *(M1 A1)*. "
                "Check: $90\\pi + 234\\pi = 324\\pi = \\pi(18)^{2}$ ✓ *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.4", "mono": True}, {"text": "P2"}],
            "check": [
                "Eq(Rational(100, 360)*pi*18**2, 90*pi)",
                "Abs(90*pi - 283) < 1",
                "Eq(Rational(100, 360)*2*pi*18, 10*pi)",
                "Abs(10*pi + 36 - Rational(674, 10)) < Rational(5, 100)",
                "Eq(Rational(260, 360)*pi*18**2, 234*pi)",
                "Eq(90*pi + 234*pi, pi*18**2)",
            ],
        },
        {
            "id": "aisl-gt-x05",
            "statement": (
                "Points $A(-1, 2)$ and $B(7, 6)$.  \n"
                "**(a)** Find the equation of the perpendicular bisector of $AB$. **[4]**  \n"
                "**(b)** Find where the bisector crosses the $x$-axis. **[3]**  \n"
                "**(c)** Verify that this crossing point is equidistant from $A$ and $B$. "
                "**[3]**"
            ),
            "solution": (
                "**(a)** Midpoint $(3, 4)$ *(A1)*; $m_{AB} = \\dfrac{4}{8} = \\dfrac{1}{2}$ "
                "*(M1)*, so $m_\\perp = -2$ *(A1)*, giving $y = -2x + 10$ *(A1)*.  \n"
                "**(b)** Setting $y = 0$: $2x = 10$ *(M1 A1)*, so the crossing is $(5, 0)$ "
                "*(A1)*.  \n"
                "**(c)** $(5 + 1)^{2} + (0 - 2)^{2} = 40$ and "
                "$(5 - 7)^{2} + (0 - 6)^{2} = 40$ *(M1 A1)*. Equal, so the point is "
                "$\\sqrt{40} = 6.32$ from each *(A1)*."
            ),
            "badges": [{"text": "ib-ai-sl-3.5", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(-1 + 7, 2) == 3",
                "Rational(2 + 6, 2) == 4",
                "Rational(6 - 2, 7 - (-1)) == Rational(1, 2)",
                "-2*3 + 10 == 4",
                "-2*5 + 10 == 0",
                "(5 - (-1))**2 + (0 - 2)**2 == 40",
                "(5 - 7)**2 + (0 - 6)**2 == 40",
            ],
        },
        {
            "id": "aisl-gt-x06",
            "statement": (
                "Emergency depots stand at $D_1(0, 0)$, $D_2(12, 0)$ and $D_3(6, 10)$, "
                "distances in kilometres.  \n"
                "**(a)** Find the Voronoi edge between $D_1$ and $D_2$. **[2]**  \n"
                "**(b)** Find the Voronoi edge between $D_1$ and $D_3$. **[4]**  \n"
                "**(c)** Find the Voronoi vertex of the three depots, and its distance from "
                "$D_1$, to 3 s.f. **[4]**"
            ),
            "solution": (
                "**(a)** $D_1D_2$ is horizontal with midpoint $(6, 0)$, so the edge is "
                "$x = 6$ *(M1 A1)*.  \n"
                "**(b)** Midpoint of $D_1D_3$ is $(3, 5)$; "
                "$m = \\dfrac{10}{6} = \\dfrac{5}{3}$ *(M1 A1)*, so "
                "$m_\\perp = -\\dfrac{3}{5}$ *(A1)*, giving "
                "$y = -\\dfrac{3}{5}x + \\dfrac{34}{5}$ *(A1)*.  \n"
                "**(c)** At $x = 6$: $y = -\\dfrac{18}{5} + \\dfrac{34}{5} = \\dfrac{16}{5}$ "
                "*(M1 A1)*, so the vertex is $(6, 3.2)$. Its distance from $D_1$ is "
                "$\\sqrt{36 + 10.24} = 6.80$ km *(M1 A1)*.  \n"
                "The same distance to $D_2$ and $D_3$ confirms it: "
                "$(6-12)^{2} + 3.2^{2} = 46.24$ and $(6-6)^{2} + (3.2-10)^{2} = 46.24$."
            ),
            "badges": [{"text": "ib-ai-sl-3.6", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(0 + 12, 2) == 6",
                "Rational(0 + 10, 2) == 5",
                "Rational(10, 6) == Rational(5, 3)",
                "Rational(5, 3)*Rational(-3, 5) == -1",
                "Rational(-3, 5)*3 + Rational(34, 5) == 5",
                "Rational(-3, 5)*6 + Rational(34, 5) == Rational(16, 5)",
                "36 + Rational(16, 5)**2 == Rational(1156, 25)",
                "(6 - 12)**2 + Rational(16, 5)**2 == Rational(1156, 25)",
                "(6 - 6)**2 + (Rational(16, 5) - 10)**2 == Rational(1156, 25)",
                "Abs(sqrt(Rational(1156, 25)) - Rational(680, 100)) < Rational(5, 1000)",
            ],
        },
        {
            "id": "aisl-gt-x07",
            "statement": (
                "Four sensors sit at $(0, 0)$, $(8, 0)$, $(0, 8)$ and $(8, 8)$ inside the square "
                "region $0 \\le x \\le 8$, $0 \\le y \\le 8$. A device must be placed as far as "
                "possible from every sensor.  \n"
                "**(a)** Explain why the best location is the centre of the square. **[3]**  \n"
                "**(b)** Find its distance from the nearest sensor, to 3 s.f. **[2]**  \n"
                "**(c)** A fifth sensor is added at $(4, 4)$. State the effect on the answer to "
                "**(a)**. **[2]**"
            ),
            "solution": (
                "**(a)** By symmetry the four perpendicular bisectors meet at $(4, 4)$, which is "
                "the single Voronoi vertex *(M1 A1)*. Anywhere else inside the square is nearer "
                "to at least one sensor, and the toxic-waste-dump result says the optimum is a "
                "vertex or on the boundary — here the vertex wins *(R1)*.  \n"
                "**(b)** $\\sqrt{4^{2} + 4^{2}} = \\sqrt{32} = 5.66$ *(M1 A1)*.  \n"
                "**(c)** The new sensor sits exactly at the old optimum, so that location now "
                "has distance $0$ to the nearest sensor *(A1)*. The best remaining spots move to "
                "the boundary — the edge midpoints such as $(4, 0)$, which are $4$ from the two "
                "nearest corner sensors and $4$ from the new one *(A1)*.  \n"
                "This is the standard sting in the tail of a toxic-waste-dump question: adding a "
                "site destroys the previous answer."
            ),
            "badges": [{"text": "ib-ai-sl-3.6", "mono": True}, {"text": "P2"}],
            "check": [
                "(4 - 0)**2 + (4 - 0)**2 == 32",
                "(4 - 8)**2 + (4 - 8)**2 == 32",
                "Abs(sqrt(32) - Rational(566, 100)) < Rational(5, 1000)",
                "(4 - 0)**2 + (0 - 0)**2 == 16",
                "(4 - 4)**2 + (0 - 4)**2 == 16",
                "16 < 32",
            ],
        },
        {
            "id": "aisl-gt-x08",
            "statement": (
                "A right pyramid has a square base of side $10$ cm and vertical height $12$ "
                "cm.  \n"
                "**(a)** Find its volume. **[2]**  \n"
                "**(b)** Find the slant height of a triangular face, to 3 s.f. **[3]**  \n"
                "**(c)** Find the total surface area, to 3 s.f. **[4]**"
            ),
            "solution": (
                "**(a)** $V = \\dfrac{1}{3}(10^{2})(12) = 400$ cm$^{3}$ *(M1 A1)*.  \n"
                "**(b)** The face's slant height runs from the apex to the midpoint of a base "
                "edge, $5$ cm from the centre *(M1)*: "
                "$\\sqrt{12^{2} + 5^{2}} = 13$ cm *(M1 A1)*.  \n"
                "**(c)** Four triangles: $4 \\times \\frac{1}{2}(10)(13) = 260$ cm$^{2}$ "
                "*(M1 A1)*. Base: $100$ cm$^{2}$ *(A1)*. Total $= 360$ cm$^{2}$ *(A1)*.  \n"
                "Using the edge length from apex to a base CORNER instead — "
                "$\\sqrt{12^{2} + (5\\sqrt{2})^{2}} = \\sqrt{194}$ — is the standard error; the "
                "triangular face's height meets the base edge at its midpoint, not at a corner."
            ),
            "badges": [{"text": "ib-ai-sl-3.1", "mono": True}, {"text": "P2"}],
            "check": [
                "Rational(1, 3)*10**2*12 == 400",
                "sqrt(12**2 + 5**2) == 13",
                "4*Rational(1, 2)*10*13 == 260",
                "260 + 100 == 360",
                "12**2 + (5*sqrt(2))**2 == 194",
            ],
        },
        {
            "id": "aisl-gt-x09",
            "statement": (
                "In triangle $PQR$, $PQ = 9$, angle $P = 48^\\circ$ and $QR = 7$.  \n"
                "**(a)** Find the two possible values of angle $R$, to 3 s.f. **[4]**  \n"
                "**(b)** For the acute value of $R$, find $PR$, to 3 s.f. **[3]**  \n"
                "**(c)** Explain why two triangles are possible here. **[2]**"
            ),
            "solution": (
                "**(a)** Sine rule *(M1)*: "
                "$\\dfrac{\\sin R}{9} = \\dfrac{\\sin 48^{\\circ}}{7}$, so "
                "$\\sin R = 0.9555$ *(A1)*. Then $R = 72.8^\\circ$ or "
                "$R = 180^\\circ - 72.8^\\circ = 107^\\circ$ *(A1 A1)*.  \n"
                "**(b)** With $R = 72.8^\\circ$, angle $Q = 180^\\circ - 48^\\circ - 72.8^\\circ "
                "= 59.2^\\circ$ *(M1)*. Then "
                "$PR = \\dfrac{7\\sin 59.2^{\\circ}}{\\sin 48^{\\circ}}$ *(A1)* $= 8.09$ "
                "*(A1)*.  \n"
                "**(c)** The given angle is not between the two given sides, and the side "
                "opposite it ($QR = 7$) is shorter than $PQ = 9$ but long enough to reach "
                "*(R1)* — so the arc of radius $7$ centred at $Q$ cuts the far side twice, "
                "giving two triangles *(R1)*.  \n"
                "This is the ambiguous case, and it appears whenever $\\sin^{-1}$ is used to "
                "find an angle: always ask whether the obtuse partner also fits."
            ),
            "badges": [{"text": "ib-ai-sl-3.2", "mono": True}, {"text": "P2"}],
            "check": [
                "Abs(9*sin(48*pi/180)/7 - Rational(9555, 10000)) < Rational(1, 10000)",
                "Abs(asin(9*sin(48*pi/180)/7)*180/pi - Rational(728, 10)) < Rational(5, 100)",
                "Abs(180 - asin(9*sin(48*pi/180)/7)*180/pi - 107) < Rational(5, 10)",
                "Abs(7*sin(pi - 48*pi/180 - asin(9*sin(48*pi/180)/7))/sin(48*pi/180) - Rational(809, 100)) < Rational(5, 1000)",
                "7 < 9",
            ],
        },
    ]


# ===========================================================================
# Assembly
# ===========================================================================
def build():
    lessons = [
        lesson_three_dimensions(),
        lesson_trigonometry(),
        lesson_applications(),
        lesson_arcs_and_sectors(),
        lesson_perpendicular_bisectors(),
        lesson_voronoi(),
    ]
    return {
        "slug": "geometry-and-trigonometry",
        "title": "Geometry & Trigonometry",
        "unit": 3,
        "status": "published",
        "blurb": (
            "AI Topic 3, complete: distance, volume and angles in three dimensions, right and "
            "non-right trigonometry, elevation, depression and bearings, arcs and sectors, "
            "perpendicular bisectors, and Voronoi diagrams with the toxic-waste-dump problem — "
            "AI SL 3.1 to 3.6, taught to markscheme standard."
        ),
        "buildsOn": (
            "Topic 2's straight lines, which become the perpendicular bisectors of 3.5 and then "
            "every edge of a Voronoi diagram in 3.6 — the two codes Analysis & Approaches does "
            "not have."
        ),
        "lessons": lessons,
        "practice": practice_bank(),
        "testYourself": test_bank(),
    }


def selfcheck(unit):
    from sympy import sympify
    n_checks = 0
    problems = []
    for les in unit["lessons"]:
        problems += les["workedExamples"] + les["tryIt"]
        ids = {p["id"] for p in les["workedExamples"] + les["tryIt"]}
        for step in les["interactive"]["steps"]:
            if step["kind"] in ("worked", "tryIt"):
                assert step["problemId"] in ids, f"{les['slug']}: dangling problemId {step['problemId']}"
            if step["kind"] == "tapQuestion":
                assert len(step["options"]) == len(set(step["options"])), f"{les['slug']}: dup options"
                for c in step["check"]:
                    assert bool(sympify(c)) is True, f"{les['slug']} tapQ: {c}"
                    n_checks += 1
    problems += unit["practice"] + unit["testYourself"]
    ids = [p["id"] for p in problems]
    assert len(ids) == len(set(ids)), "duplicate problem ids"
    for p in problems:
        for c in p["check"]:
            assert bool(sympify(c)) is True, f"{p['id']}: NOT TRUE: {c}"
            n_checks += 1
    return len(problems), n_checks


def main():
    unit = build()
    n_problems, n_checks = selfcheck(unit)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(unit, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    n_steps = sum(len(l["interactive"]["steps"]) for l in unit["lessons"])
    print(f"wrote {os.path.relpath(OUT, ROOT)}: {len(unit['lessons'])} lessons, "
          f"{n_steps} interactive steps, {n_problems} problems, {n_checks} sympy checks OK")


if __name__ == "__main__":
    main()
