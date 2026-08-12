#!/usr/bin/env python3
"""Vectors & Matrices — Unit 7: Transformation Matrices.

Ministry of Education order А/492 (2019), section 10.11 "Геометр хувиргалт":

  10.11а  transformation in the coordinate plane, the coordinate formulas,
          the transformation MATRIX and its use
  10.11б  symmetry (in a point, in an axis) expressed as a matrix
  10.11в  translation (параллель зөөлт) expressed as a matrix
  10.11г  rotation (эргүүлэлт) expressed as a matrix
  10.11д  homothety (гомотет) expressed as a matrix
  10.11е* consecutive transformations as a matrix product
  10.11ж* recognising and naming a transformation from its matrix

Until 2026-08 this was the largest hole in the platform's coverage of the
national standard: the Geometry course taught rigid motions synthetically
(slide, flip, turn on a grid) and Unit 6 of this course mentioned in passing
that a matrix's columns are destinations, but nowhere did a student write a
reflection, a rotation, an enlargement or a translation AS A MATRIX and use
it — which is exactly how the ministry and the ЭЕШ paper pose the topic.

The unit's through-line: A TRANSFORMATION IS FOUR NUMBERS, AND THE FOUR
NUMBERS ARE TWO DESTINATIONS. Ask where (1,0) and (0,1) go, stand the answers
up as columns, and every transformation in section 10.11 is rebuilt from
scratch in seconds — no memorised table. Translation is the one that refuses,
and refusing is informative: a 2x2 matrix always fixes the origin, so the
plane needs a third coordinate. That is the homogeneous 3x3 form every
graphics engine runs on.

Run: python3 scripts/vecmat/build_unit7.py   (then npm run verify:genmath)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "scripts", "im"))

from imbuild import fact, lesson, mistake, problem, write_unit  # noqa: E402

COURSE = "vectors-matrices"


def M(a, b, c, d):
    """Inline LaTeX for a 2x2 matrix (no surrounding dollars)."""
    return r"\begin{pmatrix} %s & %s \\ %s & %s \end{pmatrix}" % (a, b, c, d)


def M3(rows):
    """Inline LaTeX for a 3x3 matrix (no surrounding dollars)."""
    body = r" \\ ".join(" & ".join(str(x) for x in r) for r in rows)
    return r"\begin{pmatrix} %s \end{pmatrix}" % body


def col(x, y):
    return r"\begin{pmatrix} %s \\ %s \end{pmatrix}" % (x, y)


# ===========================================================================
# Lesson 1 — the transformation matrix (10.11а)
# ===========================================================================

L1_WORKED = [
    problem(
        "vm71-we1",
        r"A transformation of the plane is given by the rules $x' = 3x - y$ and "
        r"$y' = 2x + 4y$. Write its matrix, then find the image of $(2; -1)$.",
        r"The coefficients of $x$ and $y$ in the $x'$ rule are the first ROW, and the "
        r"coefficients in the $y'$ rule are the second row: $M = " + M(3, -1, 2, 4) + r"$. "
        r"Now apply it: $x' = 3 \cdot 2 - 1 \cdot (-1) = 7$ and "
        r"$y' = 2 \cdot 2 + 4 \cdot (-1) = 0$, so $(2; -1) \to (7; 0)$.",
        ["3*2 - 1*(-1) == 7", "2*2 + 4*(-1) == 0"],
    ),
    problem(
        "vm71-we2",
        r"A transformation sends $(1; 0)$ to $(2; 5)$ and $(0; 1)$ to $(-3; 1)$. Write its "
        r"matrix and its coordinate rules, then find the image of $(4; 2)$.",
        r"Stand the two destinations up as COLUMNS: $M = " + M(2, -3, 5, 1) + r"$. Reading the "
        r"rows back gives $x' = 2x - 3y$ and $y' = 5x + y$. So "
        r"$x' = 2 \cdot 4 - 3 \cdot 2 = 2$ and $y' = 5 \cdot 4 + 2 = 22$: the image is "
        r"$(2; 22)$. Nothing was memorised — two destinations were enough.",
        ["2*4 - 3*2 == 2", "5*4 + 1*2 == 22", "2*1 - 3*0 == 2", "5*1 + 1*0 == 5"],
    ),
    problem(
        "vm71-we3",
        r"Apply $M = " + M(1, 2, 0, 1) + r"$ to the triangle with vertices $(0; 0)$, $(3; 0)$ "
        r"and $(0; 2)$. Find the image triangle and its area.",
        r"Transform vertex by vertex. $(0; 0) \to (0; 0)$ — every $2 \times 2$ matrix fixes the "
        r"origin. $(3; 0) \to (1 \cdot 3 + 2 \cdot 0;\; 0 \cdot 3 + 1 \cdot 0) = (3; 0)$: the "
        r"$x$-axis does not move. $(0; 2) \to (1 \cdot 0 + 2 \cdot 2;\; 0 \cdot 0 + 1 \cdot 2) "
        r"= (4; 2)$ — the top vertex slides sideways. The original area is "
        r"$\tfrac{1}{2} \cdot 3 \cdot 2 = 3$, and $\det M = 1 \cdot 1 - 2 \cdot 0 = 1$, so the "
        r"image also has area $3$. This map is a shear: it leans the triangle without "
        r"changing how much paper it covers.",
        [
            "1*3 + 2*0 == 3",
            "1*0 + 2*2 == 4",
            "0*0 + 1*2 == 2",
            "1*1 - 2*0 == 1",
            "Rational(1,2)*3*2 == 3",
        ],
    ),
]

L1_TRY = [
    problem(
        "vm71-t1",
        r"A transformation has rules $x' = 5x + 2y$ and $y' = -x + 3y$. Write its matrix and "
        r"find the image of $(1; 1)$.",
        r"$M = " + M(5, 2, -1, 3) + r"$, and $(1; 1) \to (5 + 2;\; -1 + 3) = (7; 2)$.",
        ["5*1 + 2*1 == 7", "-1*1 + 3*1 == 2"],
    ),
    problem(
        "vm71-t2",
        r"Where do $(1; 0)$ and $(0; 1)$ land under $M = " + M(0, 4, -2, 0) + r"$?",
        r"The columns answer it directly: $(1; 0) \to (0; -2)$ and $(0; 1) \to (4; 0)$. "
        r"Multiplying confirms it: $0 \cdot 1 + 4 \cdot 0 = 0$ and $-2 \cdot 1 + 0 \cdot 0 = -2$.",
        ["0*1 + 4*0 == 0", "-2*1 + 0*0 == -2", "0*0 + 4*1 == 4", "-2*0 + 0*1 == 0"],
    ),
]

L1 = lesson(
    "the-transformation-matrix",
    "The Transformation Matrix",
    "A transformation is a rule that moves every point of the plane at once. Written as two "
    "formulas it looks like homework; written as a matrix it is four numbers — and those four "
    "numbers are nothing more than the destinations of two points you already know.",
    "Turn a coordinate rule into a 2x2 matrix and back, and apply a matrix to a point or to "
    "every vertex of a figure.",
    [
        r"**A linear rule is a matrix.** If a transformation sends $(x; y)$ to $x' = ax + by$, "
        r"$y' = cx + dy$, then the very same rule is $" + col("x'", "y'") + " = " + M("a", "b", "c", "d")
        + " " + col("x", "y") + r"$. Row one builds $x'$, row two builds $y'$ — the matrix is "
        r"the two rules stacked.",
        r"**The columns are destinations.** Put $(x; y) = (1; 0)$ into the product and you get "
        r"the first column $(a; c)$; put in $(0; 1)$ and you get the second column $(b; d)$. So "
        r"the matrix of ANY transformation can be built by asking two questions: where does "
        r"$(1; 0)$ go, and where does $(0; 1)$ go?",
        r"**Transform a figure vertex by vertex.** A polygon is its corners, and straight lines "
        r"stay straight under a matrix, so transforming a triangle means transforming three "
        r"points and reconnecting them. One consequence is worth noticing early: "
        r"$M " + col(0, 0) + " = " + col(0, 0) + r"$ always, so the origin never moves.",
    ],
    "x' = ax + by, y' = cx + dy IS the matrix (a b; c d) — and its columns are the images of "
    "(1,0) and (0,1).",
    [
        fact(
            "Matrix form",
            col("x'", "y'") + " = " + M("a", "b", "c", "d") + " " + col("x", "y"),
            "The point rides as a column on the right; row times column gives each new coordinate.",
        ),
        fact(
            "Columns",
            r"\text{col}_1 = T(1; 0), \qquad \text{col}_2 = T(0; 1)",
            "Build any transformation matrix from two destinations — no table to memorise.",
        ),
        fact(
            "The origin is fixed",
            M("a", "b", "c", "d") + " " + col(0, 0) + " = " + col(0, 0),
            "Every 2x2 transformation keeps the origin. This becomes important in Lesson 3.",
        ),
    ],
    L1_WORKED,
    [
        mistake(
            "Writing the point as a row on the left of the matrix.",
            "The point rides as a COLUMN on the right: M times (x, y) written vertically. Row "
            "times column, in that order. Putting the point on the left computes the "
            "transposed matrix's transformation, which is usually a different map.",
        ),
        mistake(
            "Reading the matrix ROWS as the images of the unit points.",
            "COLUMNS are the destinations. In (a b; c d) the first column (a, c) is where (1,0) "
            "lands; the first ROW (a, b) is only the recipe for the new x-coordinate.",
        ),
    ],
    L1_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "Two rules, one matrix",
            "body": r"A transformation of the plane assigns to each point $(x; y)$ a new point "
                    r"$(x'; y')$. When both new coordinates are built by multiplying and adding "
                    r"— $x' = ax + by$, $y' = cx + dy$ — the transformation is LINEAR, and the "
                    r"four coefficients are all there is to it. Collect them into "
                    r"$" + M("a", "b", "c", "d") + r"$ and the pair of rules becomes one object "
                    r"you can multiply, invert and compose.",
        },
        {
            "kind": "transformPlane",
            "eyebrow": "Watch one",
            "title": "A mirror, and its four numbers",
            "teach": r"Reflecting in the $x$-axis sends $(x; y)$ to $(x; -y)$. Ask the two unit "
                     r"points: $(1; 0) \to (1; 0)$ and $(0; 1) \to (0; -1)$. Stand those up as "
                     r"columns and the matrix is $" + M(1, 0, 0, -1) + r"$ — read the rows back "
                     r"and you recover $x' = x$, $y' = -y$.",
            "config": {"transform": "reflectX"},
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "Where does (1; 0) land?",
            "prompt": r"Under $M = " + M(3, -1, 2, 4) + r"$, the point $(1; 0)$ lands at…",
            "options": [
                r"$(3; 2)$ — the first column",
                r"$(3; -1)$ — the first row",
                r"$(-1; 4)$ — the second column",
                r"$(2; 4)$ — the second row",
            ],
            "correctIndex": 0,
            "explanation": r"$3 \cdot 1 + (-1) \cdot 0 = 3$ and $2 \cdot 1 + 4 \cdot 0 = 2$. The "
                           r"first COLUMN is where $(1; 0)$ goes; the first row only builds $x'$.",
            "check": ["3*1 + (-1)*0 == 3", "2*1 + 4*0 == 2"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Rules to matrix", "problemId": "vm71-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "Two destinations, one matrix", "problemId": "vm71-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "Matrix of a rule",
            "prompt": r"Which matrix carries the rules $x' = 2x + 7y$, $y' = 5y$?",
            "options": [
                "$" + M(2, 7, 0, 5) + "$",
                "$" + M(2, 0, 7, 5) + "$",
                "$" + M(7, 2, 5, 0) + "$",
                "$" + M(2, 7, 5, 0) + "$",
            ],
            "correctIndex": 0,
            "explanation": r"Row one is the $x'$ recipe $(2, 7)$; row two is the $y'$ recipe, and "
                           r"$y' = 5y$ has no $x$ term, so it is $(0, 5)$.",
            "check": ["2*1 + 7*0 == 2", "0*1 + 5*0 == 0", "0*0 + 5*1 == 5"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "A whole triangle", "problemId": "vm71-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Test your matrix on (1; 0)",
            "body": r"Whenever you write down a transformation matrix, spend three seconds "
                    r"multiplying it by $(1; 0)$ and $(0; 1)$. If the answers are not the two "
                    r"destinations you intended, you have transposed the matrix — the single "
                    r"most common slip in this whole section, and the cheapest one to catch.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Your turn: rules to matrix", "problemId": "vm71-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Read the columns", "problemId": "vm71-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "Your screen does this millions of times a second",
            "body": "Every time a character turns in a game or a map rotates under your finger, "
                    "a graphics chip is multiplying coordinates by a small matrix — the same "
                    "operation you just did by hand, run on millions of points per frame. The "
                    "reason hardware can do it so fast is precisely that a transformation is "
                    "only a handful of numbers.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"Two coordinate rules stack into one $2 \times 2$ matrix.",
                r"Columns are destinations: $\text{col}_1 = T(1; 0)$, $\text{col}_2 = T(0; 1)$.",
                r"Transform a figure by transforming its vertices; the origin never moves.",
            ],
        },
    ],
)


# ===========================================================================
# Lesson 2 — reflections and rotations (10.11б, 10.11г)
# ===========================================================================

L2_WORKED = [
    problem(
        "vm72-we1",
        r"Reflect the triangle with vertices $(2; 1)$, $(5; 1)$, $(2; 3)$ in the line $y = x$. "
        r"Give the matrix and the image vertices.",
        r"Ask the unit points: reflecting in $y = x$ swaps coordinates, so $(1; 0) \to (0; 1)$ "
        r"and $(0; 1) \to (1; 0)$. The matrix is $" + M(0, 1, 1, 0) + r"$. Applying it swaps "
        r"each vertex: $(2; 1) \to (1; 2)$, $(5; 1) \to (1; 5)$, $(2; 3) \to (3; 2)$.",
        ["0*2 + 1*1 == 1", "1*2 + 0*1 == 2", "0*5 + 1*1 == 1", "1*5 + 0*1 == 5",
         "0*2 + 1*3 == 3", "1*2 + 0*3 == 2"],
    ),
    problem(
        "vm72-we2",
        r"Rotate $(3; -2)$ by $90°$ counter-clockwise about the origin. Then say where a $270°$ "
        r"counter-clockwise rotation would send the same point.",
        r"A quarter turn counter-clockwise sends $(1; 0) \to (0; 1)$ and $(0; 1) \to (-1; 0)$, "
        r"so its matrix is $" + M(0, -1, 1, 0) + r"$. Then "
        r"$x' = 0 \cdot 3 + (-1)(-2) = 2$ and $y' = 1 \cdot 3 + 0 \cdot (-2) = 3$: the image is "
        r"$(2; 3)$. A $270°$ counter-clockwise turn is the same as $90°$ clockwise, with matrix "
        r"$" + M(0, 1, -1, 0) + r"$, giving $(-2; -3)$.",
        ["0*3 + (-1)*(-2) == 2", "1*3 + 0*(-2) == 3", "0*3 + 1*(-2) == -2", "-1*3 + 0*(-2) == -3"],
    ),
    problem(
        "vm72-we3",
        r"Write the matrix of a $60°$ counter-clockwise rotation about the origin and use it to "
        r"rotate $(2; 0)$.",
        r"Substitute into $R(\theta) = " + M(r"\cos\theta", r"-\sin\theta", r"\sin\theta", r"\cos\theta")
        + r"$ with $\theta = 60°$. Since $\cos 60° = \tfrac{1}{2}$ and "
        r"$\sin 60° = \tfrac{\sqrt{3}}{2}$, the matrix is "
        r"$" + M(r"\tfrac{1}{2}", r"-\tfrac{\sqrt{3}}{2}", r"\tfrac{\sqrt{3}}{2}", r"\tfrac{1}{2}")
        + r"$. Then $x' = \tfrac{1}{2} \cdot 2 = 1$ and "
        r"$y' = \tfrac{\sqrt{3}}{2} \cdot 2 = \sqrt{3}$, so $(2; 0) \to (1; \sqrt{3})$. The "
        r"image is still $2$ from the origin, as a rotation demands: "
        r"$1^2 + (\sqrt{3})^2 = 4 = 2^2$.",
        ["Eq(cos(pi/3), Rational(1,2))", "Eq(sin(pi/3), sqrt(3)/2)",
         "Eq(Rational(1,2)*2, 1)", "Eq(sqrt(3)/2*2, sqrt(3))", "1**2 + (sqrt(3))**2 == 4"],
    ),
]

L2_TRY = [
    problem(
        "vm72-t1",
        r"Find the image of $(-4; 7)$ after a reflection in the $y$-axis, and after a reflection "
        r"in the origin.",
        r"Reflection in the $y$-axis has matrix $" + M(-1, 0, 0, 1) + r"$, giving $(4; 7)$. "
        r"Reflection in the origin (point symmetry) has matrix $" + M(-1, 0, 0, -1) + r"$, "
        r"giving $(4; -7)$.",
        ["-1*(-4) + 0*7 == 4", "0*(-4) + 1*7 == 7", "-1*(-4) == 4", "-1*7 == -7"],
    ),
    problem(
        "vm72-t2",
        r"Which rotation about the origin has matrix $" + M(-1, 0, 0, -1) + r"$, and which other "
        r"transformation of this lesson does the same job?",
        r"Substituting $\theta = 180°$ gives $\cos 180° = -1$, $\sin 180° = 0$, which is exactly "
        r"this matrix — a half turn. It is also the reflection in the origin, so point symmetry "
        r"and the $180°$ rotation are one and the same map.",
        ["Eq(cos(pi), -1)", "Eq(sin(pi), 0)", "(-1)*(-1) - 0*0 == 1"],
    ),
]

L2 = lesson(
    "reflections-and-rotations",
    "Reflections & Rotations",
    "Two of the transformations the exam asks for are rigid: a mirror and a turn. Nothing about "
    "the figure changes except where it sits. Each one is a single matrix, and you can rebuild "
    "either from scratch in ten seconds by asking the two unit points where they go.",
    "Write and use the matrices of reflections (in the axes, in y = x, in the origin) and of "
    "rotations about the origin, including a general angle.",
    [
        r"**Reflections come straight from the unit points.** In the $x$-axis: $(1; 0)$ stays, "
        r"$(0; 1) \to (0; -1)$, so $M = " + M(1, 0, 0, -1) + r"$. In the $y$-axis: "
        r"$M = " + M(-1, 0, 0, 1) + r"$. In the line $y = x$ the coordinates swap: "
        r"$M = " + M(0, 1, 1, 0) + r"$; in $y = -x$ they swap and change sign: "
        r"$M = " + M(0, -1, -1, 0) + r"$.",
        r"**A rotation by any angle has one formula.** Turning counter-clockwise by $\theta$ "
        r"about the origin sends $(1; 0) \to (\cos\theta; \sin\theta)$ and "
        r"$(0; 1) \to (-\sin\theta; \cos\theta)$, giving "
        r"$R(\theta) = " + M(r"\cos\theta", r"-\sin\theta", r"\sin\theta", r"\cos\theta") + r"$. "
        r"The quarter turns fall out of it: $R(90°) = " + M(0, -1, 1, 0) + r"$, "
        r"$R(180°) = " + M(-1, 0, 0, -1) + r"$, $R(270°) = " + M(0, 1, -1, 0) + r"$.",
        r"**Point symmetry is the half turn.** Reflecting in the ORIGIN sends $(x; y)$ to "
        r"$(-x; -y)$ — matrix $-I$ — which is exactly $R(180°)$. Determinants tell the two "
        r"families apart: a line reflection has $\det = -1$ (orientation flips, the figure is "
        r"mirrored), a rotation has $\det = 1$ (orientation is kept).",
    ],
    "Reflections: read the unit points. Rotations: R(θ) = (cos −sin; sin cos). det = −1 mirrors, "
    "det = +1 turns.",
    [
        fact(
            "Reflection in the x-axis",
            M(1, 0, 0, -1) + r",\qquad \det = -1",
            "In the y-axis, negate the other entry; in y = x, swap the coordinates.",
        ),
        fact(
            "Rotation by θ",
            "R(\\theta) = " + M(r"\cos\theta", r"-\sin\theta", r"\sin\theta", r"\cos\theta"),
            "Counter-clockwise is positive; the lower sine is the one that stays positive.",
        ),
        fact(
            "Point symmetry",
            "-I = " + M(-1, 0, 0, -1) + " = R(180°)",
            "Reflection in the origin and the half turn are the same transformation.",
        ),
    ],
    L2_WORKED,
    [
        mistake(
            "Using the clockwise matrix for a counter-clockwise turn.",
            "R(θ) with a positive θ turns COUNTER-clockwise: the sine below the diagonal is the "
            "positive one. A clockwise turn through θ is R(−θ), which swaps the two sine signs.",
        ),
        mistake(
            "Treating reflection in the origin as a reflection in a line.",
            "Point symmetry in the origin sends (x, y) to (−x, −y): determinant +1, orientation "
            "kept, and it equals a 180° rotation. A reflection in a LINE has determinant −1.",
        ),
    ],
    L2_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "Rigid means lengths survive",
            "body": r"Reflections and rotations move a figure without resizing or distorting it: "
                    r"every distance and every angle inside the figure is preserved. In matrix "
                    r"language that shows up as columns of length $1$ that are perpendicular to "
                    r"each other, and a determinant of $\pm 1$ — area is untouched, and only the "
                    r"SIGN records whether the figure was mirrored.",
        },
        {
            "kind": "transformPlane",
            "eyebrow": "Watch one",
            "title": "A quarter turn",
            "teach": r"This $90°$ counter-clockwise rotation sends $(1; 0) \to (0; 1)$ and "
                     r"$(0; 1) \to (-1; 0)$. Columns up: $" + M(0, -1, 1, 0) + r"$, with "
                     r"$\det = 0 \cdot 0 - (-1) \cdot 1 = 1$ — nothing was stretched or mirrored.",
            "config": {"transform": "rotate", "deg": 90},
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "Mirror in y = x",
            "prompt": r"Reflection in the line $y = x$ has which matrix?",
            "options": [
                "$" + M(0, 1, 1, 0) + "$",
                "$" + M(1, 0, 0, -1) + "$",
                "$" + M(0, -1, 1, 0) + "$",
                "$" + M(-1, 0, 0, -1) + "$",
            ],
            "correctIndex": 0,
            "explanation": r"The reflection swaps the coordinates, so $(1; 0) \to (0; 1)$ and "
                           r"$(0; 1) \to (1; 0)$ — those two destinations ARE the columns.",
            "check": ["0*1 + 1*0 == 0", "1*1 + 0*0 == 1", "0*0 - 1*1 == -1"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "A triangle in the mirror", "problemId": "vm72-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "Quarter turns", "problemId": "vm72-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "Mirror or turn?",
            "prompt": r"A transformation matrix has $\det = -1$ and columns of length $1$. It is…",
            "options": [
                "a reflection in a line through the origin",
                "a rotation about the origin",
                "an enlargement",
                "a translation",
            ],
            "correctIndex": 0,
            "explanation": r"Unit-length perpendicular columns mean rigid; the negative "
                           r"determinant means orientation was reversed — a mirror, not a turn.",
            "check": ["1*(-1) - 0*0 == -1", "Eq(cos(pi/2)**2 + sin(pi/2)**2, 1)"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "A rotation by 60°", "problemId": "vm72-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Sketch one point before you trust the matrix",
            "body": r"Pick the simplest point in the question — usually $(1; 0)$ — multiply, and "
                    r"check the answer against a quick sketch. A $90°$ counter-clockwise turn "
                    r"must send a point on the positive $x$-axis up to the positive $y$-axis. If "
                    r"your matrix sends it down, you have the clockwise one.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Two mirrors", "problemId": "vm72-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Name the turn", "problemId": "vm72-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "Two mirrors make a turn",
            "body": "Reflect a figure in one line through the origin, then in another, and the "
                    "result is always a rotation — through twice the angle between the lines. "
                    "That is why kaleidoscopes spin patterns out of flat mirrors, and in matrix "
                    "form it is just the fact that (−1)(−1) = 1: two orientation flips restore "
                    "the original orientation.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"Reflections: in the $x$-axis, $y$-axis, $y = x$, $y = -x$ — read the unit points.",
                r"$R(\theta) = " + M(r"\cos\theta", r"-\sin\theta", r"\sin\theta", r"\cos\theta") + r"$ turns counter-clockwise.",
                r"Point symmetry $= -I = R(180°)$; $\det = -1$ mirrors, $\det = 1$ turns.",
            ],
        },
    ],
)


# ===========================================================================
# Lesson 3 — enlargement and translation (10.11д, 10.11в)
# ===========================================================================

L3_WORKED = [
    problem(
        "vm73-we1",
        r"A homothety with centre at the origin and ratio $k = 3$ is applied to the triangle "
        r"$(1; 2)$, $(4; 0)$, $(2; 5)$. Find the image vertices and the factor by which the area "
        r"grows.",
        r"The matrix is $3I = " + M(3, 0, 0, 3) + r"$, which simply multiplies both coordinates "
        r"by $3$: $(3; 6)$, $(12; 0)$, $(6; 15)$. Areas scale by "
        r"$\det(3I) = 3 \cdot 3 = 9$ — every length tripled, so every area is $9$ times as big.",
        ["3*1 == 3", "3*2 == 6", "3*4 == 12", "3*5 == 15", "3*3 - 0*0 == 9"],
    ),
    problem(
        "vm73-we2",
        r"A homothety has centre $C = (2; 1)$ and ratio $k = -2$. Find the image of $P = (5; 3)$.",
        r"The centre is not the origin, so work with the vector from the centre: "
        r"$P - C = (3; 2)$. Scale it: $-2 \cdot (3; 2) = (-6; -4)$. Add the centre back: "
        r"$P' = (2 - 6;\; 1 - 4) = (-4; -3)$. The negative ratio puts the image on the OPPOSITE "
        r"side of the centre, twice as far — an enlargement combined with a half turn.",
        ["5 - 2 == 3", "3 - 1 == 2", "2 + (-2)*3 == -4", "1 + (-2)*2 == -3"],
    ),
    problem(
        "vm73-we3",
        r"Write the $3 \times 3$ homogeneous matrix of the translation by $(4; -3)$ and use it "
        r"on $(2; 6)$. Then explain why no $2 \times 2$ matrix can perform this translation.",
        r"Write points with a third coordinate $1$. The matrix is "
        r"$" + M3([[1, 0, 4], [0, 1, -3], [0, 0, 1]]) + r"$, and multiplying it by $(2; 6; 1)$ "
        r"gives $x' = 2 + 4 = 6$, $y' = 6 - 3 = 3$, third coordinate $1$: the image is $(6; 3)$. "
        r"A $2 \times 2$ matrix cannot do this, because every such matrix sends $(0; 0)$ to "
        r"$(0; 0)$, whereas this translation must send the origin to $(4; -3)$. The extra row "
        r"and column exist precisely to carry the constants.",
        ["1*2 + 0*6 + 4*1 == 6", "0*2 + 1*6 + (-3)*1 == 3", "0*2 + 0*6 + 1*1 == 1",
         "0*0 + 0*0 == 0"],
    ),
]

L3_TRY = [
    problem(
        "vm73-t1",
        r"Apply the homothety with centre at the origin and ratio $k = -4$ to $(3; -1)$, and "
        r"state the area factor.",
        r"Multiply both coordinates by $-4$: the image is $(-12; 4)$. Areas scale by "
        r"$(-4)^2 = 16$ — the sign only tells you the figure was turned through $180°$ as well.",
        ["-4*3 == -12", "-4*(-1) == 4", "(-4)**2 == 16"],
    ),
    problem(
        "vm73-t2",
        r"A square of area $5$ is enlarged with ratio $k = \tfrac{5}{2}$. Find the new area.",
        r"Areas scale by $k^2 = \tfrac{25}{4}$, so the new area is "
        r"$5 \cdot \tfrac{25}{4} = \tfrac{125}{4} = 31.25$.",
        ["Eq(Rational(5,2)**2, Rational(25,4))", "Eq(5*Rational(25,4), Rational(125,4))",
         "Eq(Rational(125,4), 31.25)"],
    ),
]

L3 = lesson(
    "enlargement-and-translation",
    "Enlargement & Translation",
    "Two more transformations, and one of them breaks the machine. Enlargement is the easiest "
    "matrix in the course. Translation has no 2x2 matrix at all — and the reason it fails tells "
    "you exactly how to fix it, with the same trick every graphics engine on earth uses.",
    "Write a homothety (enlargement) as a matrix, handle a centre that is not the origin, and "
    "express a translation with a 3x3 homogeneous matrix.",
    [
        r"**Homothety is the scalar matrix.** An enlargement centred at the origin with ratio "
        r"$k$ sends $(x; y)$ to $(kx; ky)$, so its matrix is $kI = " + M("k", 0, 0, "k") + r"$. "
        r"Lengths are multiplied by $|k|$ and areas by $\det(kI) = k^2$. A negative $k$ also "
        r"turns the figure through $180°$, landing it on the far side of the centre.",
        r"**A centre away from the origin: shift, scale, shift back.** A $2 \times 2$ matrix "
        r"always fixes the origin, so for a centre $C$ work with the vector from the centre: "
        r"$P' = C + k(P - C)$. Subtracting $C$ moves the problem to the origin, the matrix acts "
        r"there, and adding $C$ puts it back.",
        r"**Translation needs a third coordinate.** No $2 \times 2$ matrix translates, for the "
        r"same reason: it cannot move the origin. The repair is to write each point as "
        r"$(x; y; 1)$ and use $" + M3([[1, 0, "a"], [0, 1, "b"], [0, 0, 1]]) + r"$, whose last "
        r"column carries the shift $(a; b)$. These are called homogeneous coordinates, and they "
        r"let one $3 \times 3$ matrix hold a rotation and a translation together.",
    ],
    "Enlargement = kI (areas ×k²); off-centre = C + k(P − C); translation needs the 3×3 "
    "homogeneous matrix, because no 2×2 can move the origin.",
    [
        fact(
            "Homothety",
            "H_k = " + M("k", 0, 0, "k") + r",\qquad \det H_k = k^2",
            "Lengths scale by |k|, areas by k². Negative k adds a half turn.",
        ),
        fact(
            "Centre not at the origin",
            "P' = C + k(P - C)",
            "Shift to the origin, scale, shift back — the standard repair for any fixed centre.",
        ),
        fact(
            "Translation, homogeneous",
            M3([[1, 0, "a"], [0, 1, "b"], [0, 0, 1]]),
            "Points ride as (x; y; 1); the last column is the shift vector.",
        ),
    ],
    L3_WORKED,
    [
        mistake(
            "Scaling areas by k instead of k squared.",
            "Lengths scale by |k|, areas by k². A homothety with ratio 3 makes a shape 9 times "
            "as large in area, not 3 times.",
        ),
        mistake(
            "Hunting for a 2x2 translation matrix.",
            "There isn't one. Every 2x2 matrix sends the origin to the origin, and a translation "
            "by a non-zero vector must move it. Add the third coordinate 1 and use the 3x3 form.",
        ),
    ],
    L3_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "One transformation that fits, one that doesn't",
            "body": r"Enlargement slots into the $2 \times 2$ machine perfectly: it is the "
                    r"matrix $kI$, and it is the only transformation in this unit that changes "
                    r"the SIZE of a figure. Translation slots in not at all, and it is worth "
                    r"seeing why rather than memorising a table: $M " + col(0, 0) + " = " + col(0, 0)
                    + r"$ for every $2 \times 2$ matrix $M$, so a map that moves the origin is "
                    r"simply not of that form.",
        },
        {
            "kind": "transformPlane",
            "eyebrow": "Watch one",
            "title": "Doubling from the origin",
            "teach": r"This enlargement has centre the origin and ratio $k = 2$, so its matrix "
                     r"is $" + M(2, 0, 0, 2) + r"$. Every length doubles and "
                     r"$\det = 4$, so the area quadruples — watch the triangle's edges and its "
                     r"interior grow at different rates.",
            "config": {"transform": "dilate", "k": 2},
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "Area under enlargement",
            "prompt": r"A homothety with ratio $k = 5$ is applied to a shape of area $3$. The "
                      r"image has area…",
            "options": ["$75$", "$15$", "$25$", "$8$"],
            "correctIndex": 0,
            "explanation": r"Areas scale by $k^2 = 25$, so $3 \cdot 25 = 75$. Multiplying by $k$ "
                           r"alone would be the length rule, not the area rule.",
            "check": ["5**2 == 25", "3*25 == 75"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Tripling a triangle", "problemId": "vm73-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "A centre that isn't the origin", "problemId": "vm73-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "Why translation refuses",
            "prompt": r"Why is there no $2 \times 2$ matrix for the translation by $(4; -3)$?",
            "options": [
                r"every $2 \times 2$ matrix sends the origin to the origin",
                r"the shift vector has a negative entry",
                r"its determinant would be zero",
                r"translations are not transformations",
            ],
            "correctIndex": 0,
            "explanation": r"$M " + col(0, 0) + " = " + col(0, 0) + r"$ always, but this "
                           r"translation must send $(0; 0)$ to $(4; -3)$. Hence the homogeneous "
                           r"$3 \times 3$ form.",
            "check": ["1*0 + 0*0 == 0", "0*0 + 1*0 == 0", "0 + 4 == 4", "0 + (-3) == -3"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Translation in 3x3", "problemId": "vm73-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Name the centre before you compute",
            "body": r"Homothety questions divide cleanly: centre at the origin means multiply "
                    r"both coordinates by $k$ and stop; any other centre means use "
                    r"$P' = C + k(P - C)$. Deciding which case you are in first prevents the "
                    r"most expensive error in this lesson — scaling the coordinates when you "
                    r"should have scaled the displacement from the centre.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "A negative ratio", "problemId": "vm73-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Area after enlargement", "problemId": "vm73-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "The extra 1 that runs 3D graphics",
            "body": "Homogeneous coordinates were invented in the 1820s for projective geometry, "
                    "long before computers. Today every 3D engine stores points as four numbers "
                    "instead of three for exactly the reason you just met: with the extra "
                    "coordinate, rotation, scaling and translation all become matrix multiplies, "
                    "so a whole chain of movements collapses into a single matrix.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"Homothety at the origin is $kI$: lengths $\times |k|$, areas $\times k^2$.",
                r"Any other centre: $P' = C + k(P - C)$.",
                r"Translation needs homogeneous coordinates — the $3 \times 3$ matrix.",
            ],
        },
    ],
)


# ===========================================================================
# Lesson 4 — composing and identifying (10.11е, 10.11ж)
# ===========================================================================

L4_WORKED = [
    problem(
        "vm74-we1",
        r"A figure is reflected in the $x$-axis and then rotated $90°$ counter-clockwise about "
        r"the origin. Find the single matrix of the combined transformation and the image of "
        r"$(1; 2)$.",
        r"Let $F = " + M(1, 0, 0, -1) + r"$ be the reflection and $R = " + M(0, -1, 1, 0)
        + r"$ the rotation. The reflection acts FIRST, so it stands nearest the point and the "
        r"product is $RF$: "
        r"$RF = " + M(0, -1, 1, 0) + M(1, 0, 0, -1) + " = " + M(0, 1, 1, 0) + r"$. "
        r"That is the reflection in the line $y = x$ — two transformations collapsed into one. "
        r"The image of $(1; 2)$ is $(2; 1)$.",
        ["0*1 + (-1)*0 == 0", "0*0 + (-1)*(-1) == 1", "1*1 + 0*0 == 1", "1*0 + 0*(-1) == 0",
         "0*1 + 1*2 == 2", "1*1 + 0*2 == 1"],
    ),
    problem(
        "vm74-we2",
        r"Name the transformation with matrix $" + M(0, 1, -1, 0) + r"$.",
        r"Work through the checklist. First $\det = 0 \cdot 0 - 1 \cdot (-1) = 1$, so area and "
        r"orientation are both kept. Next the columns: $(0; -1)$ and $(1; 0)$ each have length "
        r"$1$ and are perpendicular, so the map is rigid — a rotation. Which one? It sends "
        r"$(1; 0)$ to $(0; -1)$, a quarter turn CLOCKWISE, i.e. a $270°$ counter-clockwise "
        r"rotation about the origin.",
        ["0*0 - 1*(-1) == 1", "0**2 + (-1)**2 == 1", "1**2 + 0**2 == 1",
         "0*1 + (-1)*0 == 0", "Eq(cos(-pi/2), 0)", "Eq(sin(-pi/2), -1)"],
    ),
    problem(
        "vm74-we3",
        r"Name the transformation for each matrix: $A = " + M(-3, 0, 0, -3) + r"$ and "
        r"$B = " + M(r"\tfrac{3}{5}", r"\tfrac{4}{5}", r"\tfrac{4}{5}", r"-\tfrac{3}{5}") + r"$.",
        r"$A$ is $-3I$, a scalar matrix, so it is a homothety with centre the origin and ratio "
        r"$-3$: lengths tripled, the figure turned through $180°$, and areas multiplied by "
        r"$\det A = 9$. For $B$, the determinant is "
        r"$-\tfrac{9}{25} - \tfrac{16}{25} = -1$ and the first column has length "
        r"$\sqrt{\tfrac{9}{25} + \tfrac{16}{25}} = 1$, so $B$ is rigid with orientation "
        r"reversed — a reflection in a line through the origin.",
        ["(-3)*(-3) - 0*0 == 9",
         "Eq(Rational(3,5)*Rational(-3,5) - Rational(4,5)*Rational(4,5), -1)",
         "Eq(Rational(3,5)**2 + Rational(4,5)**2, 1)"],
    ),
]

L4_TRY = [
    problem(
        "vm74-t1",
        r"A figure is rotated $180°$ about the origin and then enlarged with centre the origin "
        r"and ratio $2$. Find the single matrix and its determinant.",
        r"The rotation is $-I$ and the enlargement is $2I$; scalar matrices commute, and the "
        r"product is $-2I = " + M(-2, 0, 0, -2) + r"$, with "
        r"$\det = (-2)(-2) - 0 = 4$. Equivalently: one homothety of ratio $-2$.",
        ["(-2)*(-2) - 0*0 == 4", "2*(-1) == -2"],
    ),
    problem(
        "vm74-t2",
        r"Compute $" + M(1, 0, 0, -1) + M(-1, 0, 0, 1) + r"$ and name the transformation it "
        r"performs.",
        r"Multiplying gives $" + M(-1, 0, 0, -1) + r"$, which is $-I$: a half turn about the "
        r"origin, equivalently the reflection in the origin. Reflecting in the $y$-axis and then "
        r"in the $x$-axis amounts to a single $180°$ rotation.",
        ["1*(-1) + 0*0 == -1", "0*(-1) + (-1)*0 == 0", "0*0 + (-1)*1 == -1",
         "(-1)*(-1) - 0*0 == 1"],
    ),
]

L4 = lesson(
    "composing-and-identifying",
    "Composing & Identifying Transformations",
    "Exams rarely stop at one transformation. They chain two and ask for the single matrix, or "
    "they hand you a matrix and ask what it does. Both directions run on the same two facts: "
    "composition is multiplication right-to-left, and the determinant plus the columns name the "
    "map.",
    "Compose transformations by multiplying their matrices in the correct order, and identify "
    "the transformation a given matrix performs.",
    [
        r"**Composition is a product, read right to left.** Doing $T_1$ and then $T_2$ has "
        r"matrix $M_2 M_1$ — the matrix that acts FIRST stands nearest the point, exactly as in "
        r"$f(g(x))$. Since matrix multiplication is not commutative, swapping the order usually "
        r"gives a genuinely different transformation.",
        r"**Identify with the determinant first.** $\det = 1$ with unit-length perpendicular "
        r"columns means a rotation; $\det = -1$ with unit-length columns means a reflection in a "
        r"line through the origin; a scalar matrix $kI$ is a homothety with ratio $k$ and "
        r"$\det = k^2$; $\det = 0$ means the plane was flattened onto a line and nothing can be "
        r"undone.",
        r"**When in doubt, send the unit points.** Multiply the matrix by $(1; 0)$ and $(0; 1)$ "
        r"and look at where they went. A rotation carries them round together; a reflection "
        r"leaves the mirror line alone and flips across it; an enlargement stretches both along "
        r"their own directions.",
    ],
    "Do T1 then T2 = M2·M1. To name a matrix: det, then column lengths, then send (1,0).",
    [
        fact(
            "Composition",
            r"T_2 \circ T_1 = M_2 M_1",
            "The first transformation is the right-hand factor — nearest the point.",
        ),
        fact(
            "Rotation test",
            M(r"\cos\theta", r"-\sin\theta", r"\sin\theta", r"\cos\theta") + r",\qquad \det = 1",
            "Unit perpendicular columns and determinant 1: a turn through θ.",
        ),
        fact(
            "Reflection in a line at angle α",
            M(r"\cos 2\alpha", r"\sin 2\alpha", r"\sin 2\alpha", r"-\cos 2\alpha") + r",\qquad \det = -1",
            "Unit perpendicular columns and determinant −1: a mirror through the origin.",
        ),
    ],
    L4_WORKED,
    [
        mistake(
            "Writing the composition in reading order.",
            "The FIRST transformation goes on the RIGHT. 'Reflect, then rotate' is R times F, "
            "not F times R, and the two products are usually different matrices.",
        ),
        mistake(
            "Calling every determinant-1 matrix a rotation.",
            "A shear like (1 2; 0 1) also has determinant 1. A rotation additionally needs "
            "columns of length 1 that are perpendicular — check the first column's length before "
            "you name it.",
        ),
    ],
    L4_TRY,
    [
        {
            "kind": "teach",
            "eyebrow": "The idea",
            "title": "Two directions, one toolkit",
            "body": r"Everything in this unit now runs both ways. Given a description, build the "
                    r"matrix from two destinations and multiply the pieces together in the right "
                    r"order. Given a matrix, read it back: the determinant reports area and "
                    r"orientation, the column lengths report rigidity, and the image of $(1; 0)$ "
                    r"pins down the exact angle or ratio.",
        },
        {
            "kind": "transformPlane",
            "eyebrow": "Watch one",
            "title": "Two moves that became one",
            "teach": r"Reflecting in the $x$-axis and then turning $90°$ counter-clockwise gives "
                     r"$" + M(0, -1, 1, 0) + M(1, 0, 0, -1) + " = " + M(0, 1, 1, 0) + r"$ — the "
                     r"mirror in $y = x$ shown here. Two transformations, one matrix, one "
                     r"multiplication.",
            "config": {"transform": "reflectYeqX"},
        },
        {
            "kind": "tapQuestion",
            "eyebrow": "Quick check",
            "title": "Which factor acts first?",
            "prompt": r"A figure is rotated by $A$ and then reflected by $B$. The combined "
                      r"matrix is…",
            "options": ["$BA$", "$AB$", "$A + B$", "$AB^{-1}$"],
            "correctIndex": 0,
            "explanation": r"$BA(x) = B(A(x))$: the matrix touching the point acts first, so the "
                           r"rotation $A$ must be the right-hand factor.",
            "check": ["0*1 + (-1)*0 == 0", "1*1 + 0*0 == 1"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Reflect, then turn", "problemId": "vm74-we1"},
        {"kind": "worked", "eyebrow": "Worked example", "title": "Name this matrix", "problemId": "vm74-we2"},
        {
            "kind": "tapQuestion",
            "eyebrow": "Check the reading",
            "title": "Scalar matrix",
            "prompt": r"The matrix $" + M(4, 0, 0, 4) + r"$ performs…",
            "options": [
                "an enlargement with centre the origin and ratio $4$",
                "a rotation through $4°$",
                "a translation by $(4; 4)$",
                "a reflection in the line $y = 4x$",
            ],
            "correctIndex": 0,
            "explanation": r"It multiplies both coordinates by $4$: a homothety of ratio $4$, "
                           r"with $\det = 16$, so areas grow sixteenfold.",
            "check": ["4*4 - 0*0 == 16", "4*1 == 4", "4*0 == 0"],
        },
        {"kind": "worked", "eyebrow": "Worked example", "title": "Two matrices, two names", "problemId": "vm74-we3"},
        {
            "kind": "tip",
            "eyebrow": "Exam habit",
            "title": "Determinant, columns, unit point — in that order",
            "body": r"Naming a matrix is a three-step routine, and doing the steps in order "
                    r"saves time. The determinant separates the four families in one "
                    r"subtraction. The column lengths then decide rigid or not. Only after that "
                    r"do you need the image of $(1; 0)$, and by then it answers a much narrower "
                    r"question: which angle, or which ratio.",
        },
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Turn, then enlarge", "problemId": "vm74-t1"},
        {"kind": "tryIt", "eyebrow": "Try it", "title": "Two mirrors", "problemId": "vm74-t2"},
        {
            "kind": "funFact",
            "eyebrow": "Fun fact",
            "title": "The transformations form a group",
            "body": "Compose two transformations and you get a transformation; every one of them "
                    "(except the flattening ones) can be undone; and doing nothing is itself a "
                    "transformation, the identity matrix. Those three properties define a GROUP "
                    "— the structure mathematicians use to describe symmetry everywhere, from "
                    "crystal lattices to the Standard Model of particle physics.",
        },
        {
            "kind": "recap",
            "eyebrow": "Recap",
            "title": "What sticks",
            "points": [
                r"Do $T_1$ then $T_2$: multiply as $M_2 M_1$, first map on the right.",
                r"Name by determinant, then column lengths, then the image of $(1; 0)$.",
                r"$kI$ is a homothety; $\det = \pm 1$ with unit columns is a turn or a mirror.",
            ],
        },
    ],
)


# ===========================================================================
# Practice & test
# ===========================================================================

PRACTICE = [
    problem(
        "vm7-pr-1",
        r"Write the matrix of the transformation $x' = 4x - 5y$, $y' = x + 2y$.",
        r"Row one holds the $x'$ coefficients, row two the $y'$ coefficients: "
        r"$" + M(4, -5, 1, 2) + r"$.",
        ["4*1 - 5*0 == 4", "1*1 + 2*0 == 1", "4*0 - 5*1 == -5", "1*0 + 2*1 == 2"],
    ),
    problem(
        "vm7-pr-2",
        r"Find the image of $(-2; 5)$ under $M = " + M(3, 1, 0, -2) + r"$.",
        r"$x' = 3(-2) + 1 \cdot 5 = -1$ and $y' = 0 \cdot (-2) + (-2) \cdot 5 = -10$, so the "
        r"image is $(-1; -10)$.",
        ["3*(-2) + 1*5 == -1", "0*(-2) + (-2)*5 == -10"],
    ),
    problem(
        "vm7-pr-3",
        r"Reflect $(6; -3)$ in the line $y = x$, and then state its image under a reflection in "
        r"the $y$-axis instead.",
        r"Reflection in $y = x$ swaps the coordinates: $(-3; 6)$. Reflection in the $y$-axis "
        r"negates the first coordinate: $(-6; -3)$.",
        ["0*6 + 1*(-3) == -3", "1*6 + 0*(-3) == 6", "-1*6 == -6"],
    ),
    problem(
        "vm7-pr-4",
        r"Rotate $(5; 2)$ by $90°$ counter-clockwise about the origin.",
        r"With $R = " + M(0, -1, 1, 0) + r"$: $x' = -2$ and $y' = 5$, so the image is $(-2; 5)$.",
        ["0*5 + (-1)*2 == -2", "1*5 + 0*2 == 5"],
    ),
    problem(
        "vm7-pr-5",
        r"A homothety with centre the origin has ratio $k = \tfrac{1}{2}$. Find the image of "
        r"$(8; -6)$ and the factor by which areas change.",
        r"Halve both coordinates: $(4; -3)$. Areas scale by $k^2 = \tfrac{1}{4}$ — the image "
        r"covers a quarter of the original area.",
        ["Eq(Rational(1,2)*8, 4)", "Eq(Rational(1,2)*(-6), -3)", "Eq(Rational(1,2)**2, Rational(1,4))"],
    ),
    problem(
        "vm7-pr-6",
        r"A homothety has centre $C = (1; 4)$ and ratio $3$. Find the image of $P = (3; 5)$.",
        r"$P - C = (2; 1)$, tripled gives $(6; 3)$, and adding the centre back gives "
        r"$P' = (7; 7)$.",
        ["3 - 1 == 2", "5 - 4 == 1", "1 + 3*2 == 7", "4 + 3*1 == 7"],
    ),
    problem(
        "vm7-pr-7",
        r"Write the $3 \times 3$ homogeneous matrix of the translation by $(-2; 5)$ and apply it "
        r"to $(7; 1)$.",
        r"The matrix is $" + M3([[1, 0, -2], [0, 1, 5], [0, 0, 1]]) + r"$, and it sends $(7; 1)$ "
        r"to $(7 - 2;\; 1 + 5) = (5; 6)$.",
        ["1*7 + 0*1 + (-2)*1 == 5", "0*7 + 1*1 + 5*1 == 6"],
    ),
    problem(
        "vm7-pr-8",
        r"A figure is reflected in the $y$-axis and then rotated $90°$ counter-clockwise. Find "
        r"the single matrix of the combined transformation.",
        r"The reflection $" + M(-1, 0, 0, 1) + r"$ acts first, so it is the right-hand factor: "
        r"$" + M(0, -1, 1, 0) + M(-1, 0, 0, 1) + " = " + M(0, -1, -1, 0) + r"$ — the reflection "
        r"in the line $y = -x$.",
        ["0*(-1) + (-1)*0 == 0", "0*0 + (-1)*1 == -1", "1*(-1) + 0*0 == -1", "1*0 + 0*1 == 0",
         "0*0 - (-1)*(-1) == -1"],
    ),
]

TEST = [
    problem(
        "vm7-ty-1",
        r"A transformation sends $(1; 0)$ to $(-2; 3)$ and $(0; 1)$ to $(4; 1)$. Write its "
        r"matrix and the image of $(2; 3)$.",
        r"The destinations are the columns: $M = " + M(-2, 4, 3, 1) + r"$. Then "
        r"$x' = -2 \cdot 2 + 4 \cdot 3 = 8$ and $y' = 3 \cdot 2 + 1 \cdot 3 = 9$, so the image "
        r"is $(8; 9)$.",
        ["-2*2 + 4*3 == 8", "3*2 + 1*3 == 9"],
    ),
    problem(
        "vm7-ty-2",
        r"Write the matrix of a $45°$ counter-clockwise rotation about the origin and use it to "
        r"rotate $(\sqrt{2}; 0)$.",
        r"$\cos 45° = \sin 45° = \tfrac{\sqrt{2}}{2}$, so "
        r"$R = " + M(r"\tfrac{\sqrt{2}}{2}", r"-\tfrac{\sqrt{2}}{2}", r"\tfrac{\sqrt{2}}{2}", r"\tfrac{\sqrt{2}}{2}")
        + r"$. Applying it: $x' = \tfrac{\sqrt{2}}{2} \cdot \sqrt{2} = 1$ and "
        r"$y' = \tfrac{\sqrt{2}}{2} \cdot \sqrt{2} = 1$, so the image is $(1; 1)$ — still at "
        r"distance $\sqrt{2}$ from the origin, as a rotation requires.",
        ["Eq(cos(pi/4), sqrt(2)/2)", "Eq(sqrt(2)/2*sqrt(2), 1)", "Eq(sqrt(1**2 + 1**2), sqrt(2))"],
    ),
    problem(
        "vm7-ty-3",
        r"A triangle of area $6$ is enlarged with ratio $k = -\tfrac{3}{2}$ about the origin. "
        r"Find the image of the vertex $(4; -2)$ and the area of the image triangle.",
        r"Multiply the vertex by $-\tfrac{3}{2}$: $(-6; 3)$. Areas scale by "
        r"$k^2 = \tfrac{9}{4}$, so the image has area $6 \cdot \tfrac{9}{4} = \tfrac{27}{2}$. "
        r"The negative ratio turns the triangle through $180°$ but does not affect the area.",
        ["Eq(Rational(-3,2)*4, -6)", "Eq(Rational(-3,2)*(-2), 3)",
         "Eq(Rational(-3,2)**2, Rational(9,4))", "Eq(6*Rational(9,4), Rational(27,2))"],
    ),
    problem(
        "vm7-ty-4",
        r"Explain why the translation by $(3; 7)$ cannot be written as a $2 \times 2$ matrix, "
        r"and write it in homogeneous form.",
        r"Every $2 \times 2$ matrix sends $(0; 0)$ to $(0; 0)$, but this translation must send "
        r"the origin to $(3; 7)$ — so no such matrix exists. Adding a third coordinate fixes it: "
        r"$" + M3([[1, 0, 3], [0, 1, 7], [0, 0, 1]]) + r"$ sends $(x; y; 1)$ to "
        r"$(x + 3;\; y + 7;\; 1)$.",
        ["1*0 + 0*0 + 3*1 == 3", "0*0 + 1*0 + 7*1 == 7", "0*0 + 0*0 == 0"],
    ),
    problem(
        "vm7-ty-5",
        r"Name the transformation with matrix $" + M(0, -1, -1, 0) + r"$, justifying your answer.",
        r"$\det = 0 \cdot 0 - (-1)(-1) = -1$, so orientation is reversed. Both columns have "
        r"length $1$ and are perpendicular, so the map is rigid: a reflection in a line through "
        r"the origin. It sends $(1; 0)$ to $(0; -1)$, which identifies the mirror as the line "
        r"$y = -x$.",
        ["0*0 - (-1)*(-1) == -1", "0**2 + (-1)**2 == 1", "(-1)**2 + 0**2 == 1",
         "0*1 + (-1)*0 == 0", "-1*1 + 0*0 == -1"],
    ),
    problem(
        "vm7-ty-6",
        r"A figure is rotated $90°$ counter-clockwise about the origin and then reflected in the "
        r"$x$-axis. Find the single matrix, and check that reversing the order gives a different "
        r"one.",
        r"The rotation acts first, so it is the right-hand factor: "
        r"$" + M(1, 0, 0, -1) + M(0, -1, 1, 0) + " = " + M(0, -1, -1, 0) + r"$, the reflection "
        r"in $y = -x$. The other order gives "
        r"$" + M(0, -1, 1, 0) + M(1, 0, 0, -1) + " = " + M(0, 1, 1, 0) + r"$, the reflection in "
        r"$y = x$ — a different mirror, so order genuinely matters.",
        ["1*0 + 0*1 == 0", "1*(-1) + 0*0 == -1", "0*0 + (-1)*1 == -1", "0*(-1) + (-1)*0 == 0",
         "0*1 + (-1)*0 == 0", "0*0 + (-1)*(-1) == 1", "1*1 + 0*0 == 1", "1*0 + 0*(-1) == 0"],
    ),
]


write_unit(
    COURSE,
    "transformation-matrices",
    "Transformation Matrices",
    7,
    "Every geometric transformation as four numbers: reflections, rotations, enlargements, the "
    "translation that needs a third coordinate, and how to compose and name them.",
    "The matrix machinery of Units 5-6, now pointed at the plane's geometry.",
    [L1, L2, L3, L4],
    PRACTICE,
    TEST,
)
