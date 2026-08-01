#!/usr/bin/env python3
"""One-time repair: give IM3 units 2-6 their teaching steps.

Twenty lessons across build_im3_unit{2..6}.py shipped with interactive
steps = [tap, tap, tap] — three quiz questions and no instruction. The
lesson route renders ONLY the interactive player, so students saw a
"course" that was three questions long (owner caught it 2026-08-01; the
verify-genmath teaching-steps gate now blocks the pattern).

The worked examples, tryIt problems, facts and mistakes were authored and
sympy-verified all along — they just were never referenced from the step
list. This script rewrites each lesson's steps to the unit-1 house shape:

  teach -> worked -> TAP -> worked -> tip -> TAP -> worked [-> worked]
        -> teach -> tryIt -> tryIt -> TAP -> recap

keeping the existing three taps in place and adding teach/tip/recap prose
authored per lesson below. Insertion is mechanical: each lesson's block is
located by slug, the three tap( calls inside its steps=[...] are located,
and the new steps are spliced around them as json.dumps literals. Run the
five builders afterwards to regenerate the JSONs; the imbuild render-
safety sweep re-checks every new string.

Run: python3 scripts/im/add_im3_lesson_steps.py   (idempotent-ish: refuses
     to touch a lesson whose steps already contain a "kind": "teach")
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

def T(title, body, beats=None, eyebrow=None):
    d = {"kind": "teach", "title": title, "body": body}
    if beats: d["beats"] = beats
    if eyebrow: d["eyebrow"] = eyebrow
    return d

def W(title, pid):
    return {"kind": "worked", "title": title, "problemId": pid}

def TRY(title, pid):
    return {"kind": "tryIt", "title": title, "problemId": pid}

def TIP(title, body, eyebrow="Watch out"):
    return {"kind": "tip", "eyebrow": eyebrow, "title": title, "body": body}

def R(points):
    return {"kind": "recap", "title": "What to carry forward", "points": points}

# PLAN[file][slug] = dict(pre=[...], mid1=[...], mid2=[...], post=[...])
# pre  -> before tap 1        mid1 -> between taps 1 and 2
# mid2 -> between taps 2 and 3   post -> after tap 3
PLAN = {
    "build_im3_unit2.py": {
        "rational-functions-and-asymptotes": dict(
            pre=[
                T("Division by zero writes the map",
                  "A rational function is one polynomial over another, and everything interesting about it comes from the places the bottom is zero. But being thrown out of the domain is not the same as having an asymptote — FACTOR first. A factor that cancels leaves a hole; a factor that survives forces a vertical asymptote.",
                  ["Domain: bottom ≠ 0", "Cancelled factor → hole", "Surviving factor → vertical asymptote"]),
                W("Reading the domain off the denominator", "im3-u2-l1-we1"),
            ],
            mid1=[
                W("Hole or asymptote — factor and see", "im3-u2-l1-we2"),
                TIP("A hole still empties the domain",
                    "Cancelling $(x - 3)$ from top and bottom removes the asymptote, not the exclusion. The simplified formula is a different function unless you carry the restriction $x \\ne 3$ along with it."),
            ],
            mid2=[
                W("Three horizontal-asymptote races", "im3-u2-l1-we3"),
                T("The ends are a race between degrees",
                  "As $|x|$ grows, only the leading terms matter — so compare degrees. Bottom wins: the fraction is squeezed to $y = 0$. A tie: $y$ levels off at the ratio of leading coefficients. Top wins: no horizontal asymptote at all.",
                  ["Bottom wins → $y = 0$", "Tie → ratio of leading coefficients", "Top wins → none"]),
                TRY("Domain drill", "im3-u2-l1-t1"),
                TRY("Hole or asymptote?", "im3-u2-l1-t2"),
            ],
            post=[
                R(["Domain: every zero of the denominator is excluded",
                   "Factor first — cancelled factor is a hole, surviving factor is a vertical asymptote",
                   "Horizontal asymptote: compare degrees, not constants",
                   "A graph may cross its horizontal asymptote in the middle; it describes the ENDS",
                   "The excluded point survives every simplification"]),
            ],
        ),
        "operations-on-rational-expressions": dict(
            pre=[
                T("Fractions, grown up",
                  "Rational expressions behave exactly like fractions of integers, because they are built the same way. Multiply tops and bottoms; divide by flipping; add over a common denominator. The one discipline that makes all three legal: factor FIRST, because cancelling is only ever allowed on factors.",
                  ["Multiply → cancel factors", "Divide → flip, then multiply", "Add → build the LCD from factors"]),
                W("Multiply, then cancel factors", "im3-u2-l2-we1"),
            ],
            mid1=[
                W("Division is multiplication by the reciprocal", "im3-u2-l2-we2"),
                TIP("Cancel factors, never terms",
                    "In $\\frac{x + 3}{x^2 + 3}$ nothing cancels: the $3$s are TERMS, glued on by addition. Only a factor — something multiplying the whole top and the whole bottom — can be struck out."),
            ],
            mid2=[
                W("Adding over the least common denominator", "im3-u2-l2-we3"),
                W("Subtraction distributes over the whole numerator", "im3-u2-l2-we4"),
                T("The LCD is built from factors, not products",
                  "Factor every denominator, then take each distinct factor at its greatest power. Multiplying all the denominators together always works but bloats the algebra — the LEAST common denominator keeps the numerators small and the restrictions readable.",
                  ["Factor each denominator", "Each factor once, at its highest power", "Restrictions come from every factor you used"]),
                TRY("Multiply and simplify", "im3-u2-l2-t1"),
                TRY("Add with an LCD", "im3-u2-l2-t2"),
            ],
            post=[
                R(["Factor first, every time",
                   "Cancelling is legal only on factors",
                   "Divide = multiply by the reciprocal; the flipped numerator adds a restriction",
                   "LCD: each distinct factor at its greatest power",
                   "When subtracting, the minus applies to the WHOLE second numerator"]),
            ],
        ),
        "solving-rational-equations": dict(
            pre=[
                T("Clear the denominators — carefully",
                  "Multiply both sides by the LCD and every fraction disappears, leaving a polynomial equation you already know how to solve. But the LCD contains the variable, so for some $x$ you just multiplied the equation by ZERO — and that step can quietly invent solutions.",
                  ["Multiply through by the LCD", "Solve the polynomial that remains", "Then check every candidate"]),
                W("A clean clearing, no surprises", "im3-u2-l3-we1"),
            ],
            mid1=[
                W("The candidate that betrays you", "im3-u2-l3-we2"),
                TIP("Check in the ORIGINAL equation",
                    "A candidate can satisfy the cleared equation perfectly and still be illegal in the original — that is what extraneous means. The check is against the original denominators, and it is part of the method, not a courtesy."),
            ],
            mid2=[
                W("Two fractions, one factored LCD", "im3-u2-l3-we3"),
                W("Work problems: rates add, times don't", "im3-u2-l3-we4"),
                T("Extraneous roots are a feature of the method",
                  "You cannot avoid them by being careful; multiplying by something that can be zero is simply not reversible. The upside: candidates can only go wrong at the EXCLUDED values, so note those before you start and the check takes seconds.",
                  ["Excluded values first", "Candidates equal to an excluded value die", "'No solution' can be the right answer"]),
                TRY("Clear and solve", "im3-u2-l3-t1"),
                TRY("Spot the extraneous root", "im3-u2-l3-t2"),
            ],
            post=[
                R(["Multiply both sides by the LCD to clear every fraction",
                   "Clearing can ADD candidates, never lose them",
                   "Check candidates against the ORIGINAL equation's domain",
                   "The bad candidates are exactly the excluded values",
                   "In work problems, add the RATES, then invert"]),
            ],
        ),
        "radical-functions-and-equations": dict(
            pre=[
                T("Half a parabola, on its side",
                  "$\\sqrt{x}$ is defined only for $x \\ge 0$ and returns only the non-negative root — so its graph is a half-parabola lying on its side. Shifts work exactly as they did for parabolas: in $y = \\sqrt{x - h} + k$ the domain starts where the inside turns non-negative, at $x = h$.",
                  ["Domain: inside $\\ge 0$", "Range: outputs from $k$ up", "Shifts move the endpoint $(h, k)$"]),
                W("Domain and range from the shift", "im3-u2-l4-we1"),
            ],
            mid1=[
                W("Isolate, square, solve", "im3-u2-l4-we2"),
                TIP("Isolate the radical BEFORE squaring",
                    "Squaring $\\sqrt{2x + 3} + 1$ as it stands creates a cross-term that still contains the root — you gain nothing. Move everything else to the other side first, THEN square: one clean step, radical gone."),
            ],
            mid2=[
                W("Squaring invents a candidate", "im3-u2-l4-we3"),
                W("When the radical can't reach", "im3-u2-l4-we4"),
                T("Squaring is a one-way street",
                  "$a = b$ implies $a^2 = b^2$, but not the reverse: $-3 \\ne 3$ while their squares agree. So squaring can only ADD candidates — the same asymmetry as clearing denominators, wearing a new costume. A square root can never equal a negative number, and no amount of algebra changes that.",
                  ["Squaring never loses a solution", "It may invent one", "$\\sqrt{u} = $ negative has NO solution"]),
                TRY("Read the domain", "im3-u2-l4-t1"),
                TRY("Solve a radical equation", "im3-u2-l4-t2"),
            ],
            post=[
                R(["$y = \\sqrt{x - h} + k$: domain $x \\ge h$, range $y \\ge k$",
                   "Isolate the radical, then square both sides",
                   "Squaring can only add candidates — check in the original",
                   "$\\sqrt{u}$ is never negative, so $\\sqrt{u} = -3$ has no solution",
                   "Same lesson as rational equations: one-way steps demand a check"]),
            ],
        ),
    },
    "build_im3_unit3.py": {
        "the-logarithm-as-an-inverse": dict(
            pre=[
                T("The question that asks for the exponent",
                  "\"$2$ to WHAT power gives $32$?\" — that question's answer is what $\\log_2 32$ MEANS. A logarithm is not a new kind of number; it is an exponent, hunted from the other side. $\\log_b x$ is the power you put on $b$ to reach $x$.",
                  ["$\\log_b x$ = the needed exponent", "$\\log_2 32 = 5$ because $2^5 = 32$", "Log form and exponential form say the same thing"]),
                W("Evaluate by asking the exponential question", "im3-u3-l1-we1"),
            ],
            mid1=[
                W("Unknown in two different places", "im3-u3-l1-we2"),
                TIP("Say it out loud",
                    "$\\log_2 8$ reads \"$2$ to what power is $8$?\" — answer $3$. Reading it as \"$2$ to the power $8$\" gives $256$ and is the single most common log error. The log ASKS for the exponent; it doesn't apply one."),
            ],
            mid2=[
                W("Where a log function lives", "im3-u3-l1-we3"),
                T("The graph is the exponential, reflected",
                  "$y = \\log_b x$ is $y = b^x$ flipped across the line $y = x$ — inputs and outputs trade places. The exponential's horizontal asymptote becomes the log's VERTICAL asymptote at $x = 0$, and only positive numbers have logarithms, because $b^y$ is always positive.",
                  ["Reflection of $b^x$ across $y = x$", "Vertical asymptote where the inside hits 0", "Inputs must be positive"]),
                TRY("One evaluation", "im3-u3-l1-t1"),
                TRY("Solve for x", "im3-u3-l1-t2"),
            ],
            post=[
                R(["$\\log_b x$ is the exponent you put on $b$ to get $x$",
                   "$\\log_b x = y$ and $b^y = x$ are the same sentence",
                   "Base restrictions: $b > 0$, $b \\ne 1$; inputs must be positive",
                   "Graph: the exponential reflected across $y = x$, vertical asymptote at the domain edge",
                   "Logarithmic growth is slow by design — it counts doublings"]),
            ],
        ),
        "the-laws-of-logarithms": dict(
            pre=[
                T("Exponent laws in inverse costume",
                  "Multiply powers of $b$ and the exponents ADD — so when logs (which ARE exponents) meet a product, they add: $\\log_b(xy) = \\log_b x + \\log_b y$. Quotients subtract for the same reason. Each law of logarithms is an exponent law you already know, read through the inverse.",
                  ["Product → sum", "Quotient → difference", "Power → multiplier out front"]),
                W("Expanding a compound log", "im3-u3-l2-we1"),
            ],
            mid1=[
                W("Condensing to a single log", "im3-u3-l2-we2"),
                TIP("There is NO law for log(x + y)",
                    "The laws convert MULTIPLICATIVE structure. $\\log(x + y)$ has no expansion — it is not $\\log x + \\log y$ (that would be $\\log(xy)$). When you see a sum inside a log, stop: the laws have nothing to say."),
            ],
            mid2=[
                W("Change of base, exactly", "im3-u3-l2-we3"),
                T("The workhorse and the escape hatch",
                  "The power law $\\log_b(x^n) = n\\log_b x$ is what will later pull an unknown out of an exponent — it is the workhorse of the next lesson. And change of base, $\\log_b x = \\frac{\\log x}{\\log b}$, means any log can be computed in any base you like.",
                  ["Power law pulls exponents down", "Change of base: a ratio of logs in ANY base", "Laws run both directions: expand and condense"]),
                TRY("Condense and evaluate", "im3-u3-l2-t1"),
                TRY("Expand", "im3-u3-l2-t2"),
            ],
            post=[
                R(["Product → sum, quotient → difference, power → multiplier",
                   "Every law is an exponent law read through the inverse",
                   "No law exists for $\\log(x + y)$",
                   "$(\\log x)^2$ and $\\log(x^2)$ are different objects",
                   "Change of base: $\\log_b x = \\frac{\\log x}{\\log b}$, any base"]),
            ],
        ),
        "solving-exponential-and-logarithmic-equations": dict(
            pre=[
                T("Three doors, one test",
                  "Every equation in this lesson opens one of three ways. Same base possible? Match the bases and equate exponents. Bases refuse to match? Take a log of both sides and let the power law pull the unknown down. Log wrapped around the unknown? Condense, then convert to exponential form.",
                  ["Match bases → equate exponents", "Can't match → take a log", "Log equation → condense, convert"]),
                W("Matching the bases", "im3-u3-l3-we1"),
            ],
            mid1=[
                W("Isolate, then log both sides", "im3-u3-l3-we2"),
                TIP("Isolate the exponential FIRST",
                    "Logging $3 \\cdot 2^t = 96$ as it stands drags a $\\log 3$ through every later line. Divide by $3$ first — $2^t = 32$ — and the equation may even solve by recognition. Isolate, then log."),
            ],
            mid2=[
                W("A log equation and its impostor root", "im3-u3-l3-we3"),
                T("The unit's warning, wearing new clothes",
                  "Condensing $\\log_2 x + \\log_2(x-2)$ ASSUMED both logs existed — assumed $x > 0$ and $x > 2$. The quadratic you solve afterwards knows nothing of those assumptions, so it may hand back a root the original equation cannot accept. Same disease as rational and radical equations; same cure: check.",
                  ["Condensing assumes every log exists", "Check candidates in the ORIGINAL", "Rejecting a root is a result, not an error"]),
                TRY("Match the bases", "im3-u3-l3-t1"),
                TRY("Convert and solve", "im3-u3-l3-t2"),
            ],
            post=[
                R(["$b^A = b^B$ forces $A = B$ — exponentials never repeat a value",
                   "Unmatchable bases: log both sides, power law pulls the unknown down",
                   "Log equations: condense to one log, rewrite in exponential form",
                   "Candidates must satisfy the ORIGINAL logs' domains",
                   "Exact answers like $\\frac{\\log 32}{\\log 2}$ are finished answers"]),
            ],
        ),
        "modelling-growth-and-decay": dict(
            pre=[
                T("Name the factor",
                  "Every exponential model is $A(t) = A_0 \\cdot b^t$: a starting amount and a constant multiplier per time step. The multiplier hides inside the story — growth of $5\\%$ means $b = 1.05$, decay of $10\\%$ means $b = 0.9$, doubling means $2$, half-life means $\\frac{1}{2}$.",
                  ["Growth $r\\%$: $b = 1 + r$", "Decay $r\\%$: $b = 1 - r$", "Doubling / half-life: $b = 2$ or $\\tfrac{1}{2}$, clock rescaled"]),
                W("Percent growth, compounded", "im3-u3-l4-we1"),
            ],
            mid1=[
                W("Half-life: count the halvings", "im3-u3-l4-we2"),
                TIP("The clock divides by the doubling time",
                    "In $A_0 \\cdot 2^{t/d}$ the exponent counts DOUBLINGS, not hours: $t$ hours is $t/d$ doublings. Twenty hours with a $5$-hour half-life is $4$ halvings — divide by the period first, then apply the power."),
            ],
            mid2=[
                W("Solving for time with a logarithm", "im3-u3-l4-we3"),
                T("Evaluating is substitution; solving for time is new",
                  "To find WHEN, isolate the exponential factor and reach the exponent — by recognising the power when the numbers are kind, or with a logarithm when they are not. That is precisely the tool this unit built. And remember a model is a claim about a pattern, trustworthy over the range it was measured on.",
                  ["Isolate the factor: $b^{t/d} = $ ratio", "Recognise the power, or take a log", "Extrapolate with humility"]),
                TRY("Decay by percent", "im3-u3-l4-t1"),
                TRY("Half-life drill", "im3-u3-l4-t2"),
            ],
            post=[
                R(["Model: $A(t) = A_0 \\cdot b^t$ — name the factor first",
                   "$5\\%$ growth is $b = 1.05$, never $b = 0.05$",
                   "Doubling/half-life clocks: exponent $t/d$ counts the periods",
                   "Solving for time = reaching the exponent with a log",
                   "Exponential change multiplies; linear change adds — don't mix them"]),
            ],
        ),
    },
    "build_im3_unit4.py": {
        "the-unit-circle": dict(
            pre=[
                T("The triangle's ratios become coordinates",
                  "Stand an angle at the positive $x$-axis, opening counterclockwise, and mark where its terminal side crosses the circle of radius $1$. That point's coordinates are DEFINED to be $(\\cos\\theta, \\sin\\theta)$. For acute angles this agrees with the right-triangle ratios — but now EVERY angle has a point, so every angle has a sine and cosine.",
                  ["Cosine = the $x$-coordinate", "Sine = the $y$-coordinate", "Defined for every angle, not just acute"]),
                W("Converting between degrees and radians", "im3-u4-l1-we1"),
            ],
            mid1=[
                W("Axis angles, read straight off the point", "im3-u4-l1-we2"),
                TIP("Radians measure the arc",
                    "A full turn is the full circumference, $2\\pi$ — so converting is one proportion: multiply degrees by $\\frac{\\pi}{180}$. Sanity-check against landmarks: $\\pi$ is half a turn, $\\frac{\\pi}{2}$ a quarter. A conversion that lands nowhere near its landmark is wrong."),
            ],
            mid2=[
                W("Coterminal angles share everything", "im3-u4-l1-we3"),
                T("Around again changes nothing",
                  "Adding or subtracting $2\\pi$ lands on the same point, so it changes no trig value — the functions repeat, by construction. Negative angles just travel clockwise: $-\\frac{\\pi}{3}$ and $\\frac{5\\pi}{3}$ are the same point. Periodicity isn't discovered later; it is built into the definition.",
                  ["$\\theta \\pm 2\\pi$: same point, same values", "Negative = clockwise", "$\\sin(\\theta + 2\\pi) = \\sin\\theta$, always"]),
                TRY("Convert both ways", "im3-u4-l1-t1"),
                TRY("Evaluate at the axes", "im3-u4-l1-t2"),
            ],
            post=[
                R(["The point is $(\\cos\\theta, \\sin\\theta)$ — cosine is $x$, sine is $y$",
                   "Radians: multiply degrees by $\\frac{\\pi}{180}$; $\\pi$ is a half turn",
                   "Axis values come free from $(1,0), (0,1), (-1,0), (0,-1)$",
                   "Coterminal angles (differing by $2\\pi$) share every value",
                   "The quadrant decides signs — not the direction of travel"]),
            ],
        ),
        "reference-angles-and-exact-values": dict(
            pre=[
                T("Fold every angle into the first quadrant",
                  "The reference angle of $\\theta$ is the acute angle between its terminal side and the $x$-axis — the first-quadrant angle it folds onto. Folding flips signs but never sizes: the magnitudes of $\\sin\\theta$ and $\\cos\\theta$ equal those of the reference angle.",
                  ["Reference angle: measured to the $x$-axis", "Sizes survive the fold", "Signs come from the quadrant"]),
                W("A second-quadrant fold", "im3-u4-l2-we1"),
            ],
            mid1=[
                W("All three functions in quadrant III", "im3-u4-l2-we2"),
                TIP("Measure to the x-axis, never the y-axis",
                    "$\\frac{5\\pi}{6}$ leans $\\frac{\\pi}{6}$ away from the NEGATIVE $x$-axis — that's its reference angle. Measuring to the $y$-axis gives $\\frac{\\pi}{3}$ and every value that follows is wrong. The fold is always onto the horizontal."),
            ],
            mid2=[
                W("Running the machine backwards", "im3-u4-l2-we3"),
                T("Every evaluation is a two-step",
                  "NAME the reference angle, then SIGN the first-quadrant value by quadrant. Tangent rides along as $\\frac{\\sin\\theta}{\\cos\\theta}$ — the slope of the terminal side — its sign the quotient of the two. And an equation like $\\sin\\theta = c$ has TWO answers per turn: one in each quadrant where the sign fits.",
                  ["Step 1: reference angle", "Step 2: quadrant sign", "$\\sin\\theta = c$: expect two angles per turn"]),
                TRY("Name and evaluate", "im3-u4-l2-t1"),
                TRY("Fourth-quadrant cosine", "im3-u4-l2-t2"),
            ],
            post=[
                R(["Reference angle for the SIZE, quadrant for the SIGN",
                   "Fold onto the $x$-axis — never measure from the $y$-axis",
                   "Only three magnitudes to memorise: those of $\\tfrac{\\pi}{6}, \\tfrac{\\pi}{4}, \\tfrac{\\pi}{3}$",
                   "Tangent = sine over cosine = slope of the terminal side",
                   "$\\sin\\theta = c$ on a full turn: two answers, one per matching quadrant"]),
            ],
        ),
        "graphs-of-sine-and-cosine": dict(
            pre=[
                T("Unroll the circle",
                  "Let the angle run along a horizontal axis and plot the circling point's $y$-coordinate: that is $y = \\sin\\theta$, the circle unrolled into a wave. It rises to $1$, falls through $0$ to $-1$, and returns — then repeats forever, because the circle does.",
                  ["The wave IS the circle, unrolled", "Sine starts at 0; cosine starts at 1", "Period $2\\pi$: one full lap"]),
                W("Reading the three dials", "im3-u4-l3-we1"),
            ],
            mid1=[
                W("A flipped, slowed cosine", "im3-u4-l3-we2"),
                TIP("b is not the period",
                    "In $y = \\sin(bx)$ the number $b$ counts how many full waves fit in a $2\\pi$ window; the period itself is $\\frac{2\\pi}{b}$. Bigger $b$ means a FASTER, tighter wave. Read $b = 4$ as \"four laps per $2\\pi$\", never as \"period $4$\"."),
            ],
            mid2=[
                W("Building a tide model from max and min", "im3-u4-l3-we3"),
                T("Modelling runs the reading backwards",
                  "From a maximum and minimum: the midline is their average, the amplitude their half-difference, and the period is read off the story's clock. Choose cosine to start at a peak, sine to start on the midline — the choice is a starting point, not a different physics.",
                  ["Midline $k$ = average of max and min", "Amplitude $|a|$ = half the difference", "Cosine starts at a peak; sine at the midline"]),
                TRY("Amplitude and period", "im3-u4-l3-t1"),
                TRY("Midline from max and min", "im3-u4-l3-t2"),
            ],
            post=[
                R(["Three dials: $|a|$ swing, $k$ centreline, $\\frac{2\\pi}{b}$ lap time",
                   "Amplitude is the HALF-height: $\\frac{\\text{max} - \\text{min}}{2}$",
                   "$b$ counts waves per $2\\pi$; the period is $\\frac{2\\pi}{b}$",
                   "A negative $a$ flips the wave; amplitude stays $|a|$",
                   "Model from a story: midline, amplitude, period, then pick sine or cosine by the start"]),
            ],
        ),
        "the-pythagorean-identity": dict(
            pre=[
                T("The circle's equation, renamed",
                  "A point $(x, y)$ lies on the unit circle exactly when $x^2 + y^2 = 1$. The point reached by $\\theta$ has $x = \\cos\\theta$ and $y = \\sin\\theta$ — substitute, and $\\sin^2\\theta + \\cos^2\\theta = 1$ for EVERY angle. The proof is that one substitution; the identity is geometry wearing trig notation.",
                  ["$x^2 + y^2 = 1$ with coordinates renamed", "True for every $\\theta$, all four quadrants", "One value recovers the other — up to sign"]),
                W("From sine to cosine and tangent", "im3-u4-l4-we1"),
            ],
            mid1=[
                W("Quadrant III does the signing", "im3-u4-l4-we2"),
                TIP("Un-squaring costs a ±",
                    "The identity hands you $\\cos^2\\theta$; taking the square root gives $\\pm\\cos\\theta$, and the algebra cannot choose. The QUADRANT chooses. Never write $\\cos\\theta = \\sqrt{1 - \\sin^2\\theta}$ without asking where $\\theta$ lives."),
            ],
            mid2=[
                W("Proving an identity, not just checking it", "im3-u4-l4-we3"),
                T("Familiar triangles, hiding on the circle",
                  "With $\\sin\\theta = \\frac{3}{5}$ the identity forces $\\cos\\theta = \\pm\\frac{4}{5}$ — the $3$–$4$–$5$ triangle scaled onto the unit circle. Tangent then comes free as the quotient of the two. A verification at one angle ILLUSTRATES an identity; only algebra that never picks a value PROVES it.",
                  ["Pythagorean triples reappear as trig values", "$\\tan\\theta = \\frac{\\sin\\theta}{\\cos\\theta}$", "Verify at a point; prove with algebra"]),
                TRY("Quadrant I warm-up", "im3-u4-l4-t1"),
                TRY("Tangent from cosine", "im3-u4-l4-t2"),
            ],
            post=[
                R(["$\\sin^2\\theta + \\cos^2\\theta = 1$ — the unit circle's own equation",
                   "It recovers either value from the other, up to a sign",
                   "The quadrant supplies the sign the algebra lost",
                   "$\\sin^2\\theta$ means $(\\sin\\theta)^2$, never $\\sin(\\theta^2)$",
                   "One-angle checks illustrate; only general algebra proves"]),
            ],
        ),
    },
    "build_im3_unit5.py": {
        "transformations-of-functions": dict(
            pre=[
                T("Outside acts on outputs; inside acts on inputs",
                  "Adding OUTSIDE the function raises every output: a vertical slide, exactly as written. Adding INSIDE shifts horizontally — and backwards from the sign, because $f(x - 3)$ makes the input $3$ behave the way $0$ used to. Those two sentences, plus their multiplying twins, transform every family there is.",
                  ["Outside: vertical, as written", "Inside: horizontal, in reverse", "Same rules for every function family"]),
                W("Reading a formula as a recipe", "im3-u5-l1-we1"),
            ],
            mid1=[
                W("Building a formula from words", "im3-u5-l1-we2"),
                TIP("Inside changes run backwards",
                    "$f(x - 3)$ slides RIGHT, $f(x + 3)$ slides LEFT, and $f(2x)$ COMPRESSES. Before trusting a sign, test one point: where does the old $x = 0$ behaviour now happen? That single check catches every direction error."),
            ],
            mid2=[
                W("Why order matters", "im3-u5-l1-we3"),
                T("Stacked moves, read inside-out",
                  "$g(x) = -2f(x - 3) + 4$ is a whole recipe: shift right 3, stretch by 2, flip across the $x$-axis, raise 4 — the order the machine itself computes. Order matters exactly where arithmetic says it does: a stretch scales everything done before it, so stretch-then-shift and shift-then-stretch differ.",
                  ["Read the formula inside-out", "A reflection turns max into min", "Different order → different graph"]),
                TRY("Vertex from a formula", "im3-u5-l1-t1"),
                TRY("Words to formula", "im3-u5-l1-t2"),
            ],
            post=[
                R(["Outside the function: vertical, behaves as written",
                   "Inside the function: horizontal, behaves in reverse",
                   "Negative outside flips over the $x$-axis; negative inside over the $y$-axis",
                   "Read stacked transformations inside-out",
                   "The same four moves work on every family — $|x|$, $\\sqrt{x}$, $2^x$, all of them"]),
            ],
        ),
        "even-and-odd-functions": dict(
            pre=[
                T("Feed it the opposite input",
                  "A function is EVEN when opposite inputs give equal outputs — $f(-x) = f(x)$ — a mirror in the $y$-axis. It is ODD when opposite inputs give opposite outputs — $f(-x) = -f(x)$ — a half-turn about the origin. One substitution decides which, if either.",
                  ["Even: $f(-x) = f(x)$, mirror", "Odd: $f(-x) = -f(x)$, half-turn", "Most functions: neither"]),
                W("An even quartic, tested honestly", "im3-u5-l2-we1"),
            ],
            mid1=[
                W("An odd cubic and its half-turn", "im3-u5-l2-we2"),
                TIP("Parentheses around every -x",
                    "$(-x)^3 = -x^3$ but $(-x)^4 = x^4$ — the sign survives odd powers and dies in even ones. Every symmetry error traces back to substituting $-x$ without parentheses. Write them, every time."),
            ],
            mid2=[
                W("When both tests fail", "im3-u5-l2-we3"),
                T("The polynomial shortcut, and its limits",
                  "For polynomials the names are literal: all exponents even → even; all odd → odd; mixed → neither, which is the common case. One matching pair of outputs proves nothing — symmetry is a claim about EVERY input — but a single failing pair settles 'neither' for good.",
                  ["All-even exponents → even; all-odd → odd", "Mixed parity → neither", "One counterexample ends the test; one success doesn't"]),
                TRY("Absolute value", "im3-u5-l2-t1"),
                TRY("A pure power", "im3-u5-l2-t2"),
            ],
            post=[
                R(["Even: $f(-x) = f(x)$ — mirror in the $y$-axis",
                   "Odd: $f(-x) = -f(x)$ — half-turn about the origin",
                   "Polynomial glance test: exponent parity, constant counts as even",
                   "An odd function defined at $0$ has $f(0) = 0$",
                   "Neither is the default — prove symmetry with algebra, not one example"]),
            ],
        ),
        "composition-of-functions": dict(
            pre=[
                T("Chain the machines",
                  "Composition feeds the output of one function into the next: $(f \\circ g)(x) = f(g(x))$, read RIGHT to left — $g$ acts first. To evaluate at a number, work inside-out: find $g(2)$, then hand the result to $f$.",
                  ["$(f \\circ g)(x) = f(g(x))$", "Inner first, outer second", "Not multiplication — substitution"]),
                W("Both orders, at one input", "im3-u5-l3-we1"),
            ],
            mid1=[
                W("Both orders, as formulas", "im3-u5-l3-we2"),
                TIP("Substitute the WHOLE inner formula",
                    "Composing $f(x) = 2x - 3$ with $g(x) = x^2 + 1$ means $2(x^2 + 1) - 3$ — parentheses around all of $g$. Dropping them loses the doubling of the $+1$ and quietly produces a different function."),
            ],
            mid2=[
                W("Decomposing a complicated function", "im3-u5-l3-we3"),
                T("Order matters; decomposition runs it backwards",
                  "$f \\circ g$ and $g \\circ f$ are as different as socks-then-shoes and shoes-then-socks — never assume they agree. Decomposition is the reverse skill: in $h(x) = \\sqrt{3x + 4}$, the inner function is what the formula computes FIRST ($3x + 4$), the outer is what happens to that result.",
                  ["The two orders rarely agree", "Inner function = first computation", "Decomposition turns one hard function into two easy ones"]),
                TRY("Evaluate both chains", "im3-u5-l3-t1"),
                TRY("Compose as a formula", "im3-u5-l3-t2"),
            ],
            post=[
                R(["$(f \\circ g)(x) = f(g(x))$ — right to left, inner first",
                   "Formulas: substitute the whole inner expression, in parentheses",
                   "$f \\circ g \\ne g \\circ f$ in general",
                   "Composition is substitution, never multiplication",
                   "To decompose, name what the formula computes first"]),
            ],
        ),
        "inverse-functions": dict(
            pre=[
                T("The machine, run backwards",
                  "The inverse $f^{-1}$ undoes $f$: if $f$ sends $6$ to $7$, $f^{-1}$ sends $7$ back to $6$. In symbols, both compositions collapse: $f^{-1}(f(x)) = x$ and $f(f^{-1}(x)) = x$. That collapse is also how you CHECK any claimed inverse.",
                  ["Do, then undo: back to $x$", "Find it: solve for the input", "Check it: both compositions give $x$"]),
                W("Find and verify a linear inverse", "im3-u5-l4-we1"),
            ],
            mid1=[
                W("An inverse that solves equations", "im3-u5-l4-we2"),
                TIP("f⁻¹ is not 1/f",
                    "The superscript names the inverse FUNCTION, not a reciprocal. For $f(x) = 2x - 5$: $f^{-1}(7) = 6$, while $\\frac{1}{f(7)} = \\frac{1}{9}$ — unrelated numbers. Say \"f-inverse\", never \"f to the minus one\"."),
            ],
            mid2=[
                W("When no inverse exists — and the repair", "im3-u5-l4-we3"),
                T("Mirrors and the one-to-one test",
                  "Inverting swaps inputs and outputs, so the graph of $f^{-1}$ is the graph of $f$ reflected across the line $y = x$ — every point $(a, b)$ pairs with $(b, a)$. And only ONE-TO-ONE functions qualify: if two inputs share an output, undoing has no single answer. The repair is restricting the domain, which is exactly why $\\sqrt{x}$ exists.",
                  ["Graphs mirror across $y = x$", "Horizontal line test = invertibility", "Restrict the domain to rescue $x^2$"]),
                TRY("An easy undo", "im3-u5-l4-t1"),
                TRY("Solve-and-swap", "im3-u5-l4-t2"),
            ],
            post=[
                R(["$f^{-1}$ undoes $f$: both compositions simplify to $x$",
                   "Find it by solving for the input, then swapping letters",
                   "Graphs of $f$ and $f^{-1}$ mirror across $y = x$",
                   "Only one-to-one functions have inverses; restrict the domain otherwise",
                   "$f^{-1}(x)$ is the inverse function, never $\\frac{1}{f(x)}$"]),
            ],
        ),
    },
    "build_im3_unit6.py": {
        "arithmetic-sequences-and-series": dict(
            pre=[
                T("From listing to adding",
                  "An arithmetic sequence climbs by a constant difference: $a_n = a_1 + (n-1)d$, with $n - 1$ because the first term has taken zero steps. A SERIES is what you get when you add the terms — and the sum has a two-hundred-year-old shortcut found by a schoolboy.",
                  ["$a_n = a_1 + (n-1)d$", "Series = the terms, added", "$S_n$ names the sum of the first $n$"]),
                W("The theater, row by row", "im3-u6-l1-we1"),
            ],
            mid1=[
                W("Gauss's pairing", "im3-u6-l1-we2"),
                TIP("n terms make n/2 pairs",
                    "Pairing uses each term ONCE: a hundred terms form fifty pairs, not a hundred. Multiplying the pair total by $n$ double-counts the entire series — the answer comes out exactly twice too big."),
            ],
            mid2=[
                W("Solving for the number of terms", "im3-u6-l1-we3"),
                T("Why the pairing never fails",
                  "Step one term in from each end: the left gains $d$, the right loses $d$ — the pair total is untouched. So $S_n = \\frac{n}{2}(a_1 + a_n)$, and when the last term isn't handy, substitute its formula to get $S_n = \\frac{n}{2}(2a_1 + (n-1)d)$. Same fact, two outfits.",
                  ["Pair total is constant — that's the whole proof", "Know the last term: use $\\frac{n}{2}(a_1 + a_n)$", "Don't know it: use $\\frac{n}{2}(2a_1 + (n-1)d)$"]),
                TRY("Term and sum", "im3-u6-l1-t1"),
                TRY("The first 50 even numbers", "im3-u6-l1-t2"),
            ],
            post=[
                R(["$a_n = a_1 + (n-1)d$ — the first term has taken zero steps",
                   "Pair the ends: every pair adds to the same total",
                   "$S_n = \\frac{n}{2}(a_1 + a_n)$ — half the count times (first + last)",
                   "No last term? $S_n = \\frac{n}{2}(2a_1 + (n-1)d)$",
                   "Pairing needs a constant difference — geometric series need a different trick"]),
            ],
        ),
        "geometric-sequences-and-series": dict(
            pre=[
                T("Multiply, don't add",
                  "A geometric sequence multiplies by a constant ratio: $a_n = a_1 r^{n-1}$ — the multiplicative twin of the arithmetic formula. These are Unit 3's exponential functions sampled at whole numbers, which is why their sums grow so violently.",
                  ["Constant RATIO $r$, found by dividing neighbours", "$a_n = a_1 r^{n-1}$", "Geometric = exponential at whole numbers"]),
                W("Rice on a chessboard", "im3-u6-l2-we1"),
            ],
            mid1=[
                W("Shift, subtract, collapse", "im3-u6-l2-we2"),
                TIP("Gauss's pairing fails here",
                    "The pairs of a geometric series give DIFFERENT totals, so the arithmetic shortcut is useless. The geometric trick is its own: multiply the whole sum by $r$, subtract, and watch every middle term cancel."),
            ],
            mid2=[
                W("A decaying total", "im3-u6-l2-we3"),
                T("The formula is the argument, prepackaged",
                  "Run shift-and-subtract with letters: $S_n - rS_n = a_1 - a_1 r^n$, so $S_n = a_1\\frac{1 - r^n}{1 - r}$ for $r \\ne 1$. The chessboard's near-miss is this formula at work: a doubling total is always one less than the next term. When $r = 1$ every term is equal — just multiply.",
                  ["$S_n = a_1 \\frac{1 - r^n}{1 - r}$, $r \\ne 1$", "$1 + 2 + \\cdots + 2^{n-1} = 2^n - 1$", "Parentheses around the whole ratio in $r^n$"]),
                TRY("Term and sum", "im3-u6-l2-t1"),
                TRY("A fractional ratio", "im3-u6-l2-t2"),
            ],
            post=[
                R(["$a_n = a_1 r^{n-1}$ — $n-1$ multiplications by $r$",
                   "Shift-and-subtract: multiply by $r$, subtract, the middle cancels",
                   "$S_n = a_1\\frac{1 - r^n}{1 - r}$ for $r \\ne 1$; $S_n = na_1$ when $r = 1$",
                   "Doubling totals are one short of the next term",
                   "The newest term of a growing geometric series outweighs all the others combined"]),
            ],
        ),
        "infinite-geometric-series": dict(
            pre=[
                T("Infinitely many terms, one finite number",
                  "Add $\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\cdots$ and the partial sums run $\\frac{1}{2}, \\frac{3}{4}, \\frac{7}{8}, \\ldots$ — each halves the gap to $1$ and none crosses it. When $|r| < 1$ the leftover $r^n$ in the finite formula dies out, and the whole infinite sum settles at a limit.",
                  ["Partial sums close a gap", "$|r| < 1$: the $r^n$ term evaporates", "$S = \\frac{a_1}{1 - r}$"]),
                W("The wall walk, made rigorous", "im3-u6-l3-we1"),
            ],
            mid1=[
                W("A repeating decimal unmasked", "im3-u6-l3-we2"),
                TIP("Check |r| < 1 BEFORE the formula",
                    "For $1 + 2 + 4 + \\cdots$ the formula outputs $-1$, which is absurd — because with $r = 2$ there IS no sum; the partial sums pass every bound. The condition $|r| < 1$ is the difference between a number and nonsense."),
            ],
            mid2=[
                W("A bouncing ball's total journey", "im3-u6-l3-we3"),
                T("The sum IS the limit",
                  "No partial sum ever equals $1$; the SUM is defined as the number the partial sums approach — and that number is exactly $1$, the same way $0.999\\ldots$ equals $1$. Repeating decimals are this machinery in disguise, which is why every one of them is a fraction.",
                  ["The infinite sum is the limit of partial sums", "It EQUALS its value; partial sums merely approach", "Every repeating decimal is geometric with $r$ a power of $\\frac{1}{10}$"]),
                TRY("A one-line sum", "im3-u6-l3-t1"),
                TRY("Decimal to fraction", "im3-u6-l3-t2"),
            ],
            post=[
                R(["Converges exactly when $|r| < 1$",
                   "$S = \\frac{a_1}{1 - r}$ — the finite formula with $r^n$ evaporated",
                   "$|r| \\ge 1$: no sum exists, and the formula's output is garbage",
                   "Repeating decimals are infinite geometric series — hence fractions",
                   "In travel problems, bounce heights count twice: up and down"]),
            ],
        ),
        "the-binomial-theorem": dict(
            pre=[
                T("Coefficients count choices",
                  "Expanding $(a + b)^n$ means choosing, in each factor, the $a$ or the $b$. The term $a^3b^2$ (from $n = 5$) appears once for every way to pick WHICH two factors donate a $b$ — that is $\\binom{5}{2} = 10$ ways. Expansion coefficients are the combinations from IM2, back in a new job.",
                  ["Each factor donates $a$ or $b$", "Coefficient of $a^{n-k}b^k$ = $\\binom{n}{k}$", "Exponents in every term add to $n$"]),
                W("A full expansion from row 4", "im3-u6-l4-we1"),
            ],
            mid1=[
                W("One term, extracted alone", "im3-u6-l4-we2"),
                TIP("Raise the WHOLE piece",
                    "In $(2x - 3)^5$ the pieces are $2x$ and $-3$, signs and coefficients included: $(2x)^3 = 8x^3$ and $(-3)^2 = 9$. Substituting bare $x$ and $3$ into $\\binom{n}{k}a^{n-k}b^k$ is where every binomial error lives."),
            ],
            mid2=[
                W("Building Pascal's next row", "im3-u6-l4-we3"),
                T("The triangle is a theorem about choices",
                  "Pascal's rule $\\binom{n}{k} = \\binom{n-1}{k-1} + \\binom{n-1}{k}$ says: a choice of $k$ items either uses the newest item or it doesn't. That's why each entry is the sum of the two above — combinations computed without a single factorial. Symmetry comes free: choosing $k$ to keep is choosing $n - k$ to leave out.",
                  ["Pascal's rule: use the new item, or don't", "Rows are symmetric: $\\binom{n}{k} = \\binom{n}{n-k}$", "Row $n$ sums to $2^n$ — all the choices there are"]),
                TRY("Alternating signs", "im3-u6-l4-t1"),
                TRY("A single coefficient", "im3-u6-l4-t2"),
            ],
            post=[
                R(["$(a+b)^n = \\sum \\binom{n}{k} a^{n-k} b^k$ — coefficients count choices",
                   "Pascal's triangle: each entry is the sum of the two above",
                   "Extract one term without expanding the rest",
                   "Substitute whole pieces — signs and coefficients included",
                   "$(a+b)^n$ is NOT $a^n + b^n$; the cross terms carry most of the value"]),
            ],
        ),
    },
}


def dict_src(d, indent="            "):
    """Render a step dict as a python-source literal (json is valid python
    for these shapes; ensure_ascii=False keeps math strings readable)."""
    return indent + json.dumps(d, ensure_ascii=False) + ","


def find_lesson_steps_span(src, slug):
    """Return (steps_open_idx, steps_close_idx, tap_positions) for the lesson
    with this slug. tap_positions are indices of the 'tap(' tokens inside the
    steps block, in order."""
    m = re.search(r'slug="%s"' % re.escape(slug), src)
    if not m:
        raise SystemExit(f"slug {slug!r} not found")
    steps_open = src.index("steps=[", m.end())
    # walk brackets from the '[' to find the matching ']'
    i = src.index("[", steps_open)
    depth = 0
    for j in range(i, len(src)):
        if src[j] == "[":
            depth += 1
        elif src[j] == "]":
            depth -= 1
            if depth == 0:
                close = j
                break
    else:
        raise SystemExit(f"{slug}: unbalanced steps block")
    block = src[i:close]
    taps = [i + mm.start() for mm in re.finditer(r"\btap\(", block)]
    if len(taps) != 3:
        raise SystemExit(f"{slug}: expected 3 taps in steps, found {len(taps)}")
    if '"kind": "teach"' in block or "'kind': 'teach'" in block:
        raise SystemExit(f"{slug}: steps already contain teaching steps — refusing to double-insert")
    return i, close, taps


def tap_end(src, tap_start):
    """Index just past the closing ')' of the tap( call starting at tap_start,
    including a trailing comma if present."""
    i = src.index("(", tap_start)
    depth = 0
    in_str = False
    for j in range(i, len(src)):
        c = src[j]
        if in_str:
            if c == '"' and src[j-1] != "\\":
                in_str = False
            continue
        if c == '"':
            in_str = True
        elif c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                k = j + 1
                if k < len(src) and src[k] == ",":
                    k += 1
                return k
    raise SystemExit("unterminated tap(")


def main():
    total = 0
    for fname, lessons in PLAN.items():
        path = os.path.join(HERE, fname)
        src = open(path, encoding="utf-8").read()
        for slug, plan in lessons.items():
            _, _, taps = find_lesson_steps_span(src, slug)
            t1, t2, t3 = taps
            e1, e2, e3 = tap_end(src, t1), tap_end(src, t2), tap_end(src, t3)
            pre = "\n" + "\n".join(dict_src(d) for d in plan["pre"]) + "\n            "
            mid1 = "\n" + "\n".join(dict_src(d) for d in plan["mid1"])
            mid2 = "\n" + "\n".join(dict_src(d) for d in plan["mid2"])
            post = "\n" + "\n".join(dict_src(d) for d in plan["post"])
            # splice back-to-front so earlier indices stay valid
            src = src[:e3] + post + src[e3:]
            src = src[:e2] + mid2 + src[e2:]
            src = src[:e1] + mid1 + src[e1:]
            src = src[:t1] + pre.lstrip("\n") + "\n            " + src[t1:]
            total += 1
        open(path, "w", encoding="utf-8").write(src)
        print(f"patched {fname}: {len(lessons)} lessons")
    print(f"done — {total} lessons re-stepped; now re-run the unit builders")


if __name__ == "__main__":
    main()
