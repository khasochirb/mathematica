"""Figures for AA HL Practice Papers 1 & 2 (testId ib-hl-practice-4).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aahl-p1-t4-q9.png   (region under ln(x)/x, 1..e)
        public/ib-figures/ib-aahl-p2-t4-q8.png   (velocity 4 sin t - t)
        public/ib-figures/ib-aahl-p2-t4-q9.png   (triangle with the angle
                                                  bisector AD)
"""
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "public", "ib-figures")
os.makedirs(OUT, exist_ok=True)

BLACK, WHITE, LIGHT = "#000000", "#ffffff", "0.90"


def save(fig, name):
    path = os.path.join(OUT, name)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    kb = os.path.getsize(path) / 1024
    print(f"{name}: {kb:.1f} KB")
    assert kb <= 50, f"{name} exceeds 50 KB"


def arrow_axes(ax, xlim, ylim, xlabel="$x$", ylabel="$y$"):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    ax.annotate("", xy=(xlim[1], 0), xytext=(xlim[0], 0),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2))
    ax.annotate("", xy=(0, ylim[1]), xytext=(0, ylim[0]),
                arrowprops=dict(arrowstyle="-|>", color=BLACK, lw=1.2))
    ax.text(xlim[1], -0.05 * (ylim[1] - ylim[0]), xlabel, ha="center",
            va="top", fontsize=13, color=BLACK)
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left",
            va="center", fontsize=13, color=BLACK)


# ── P1 Q9: region under y = ln(x)/x from x = 1 to x = e ────────────────
def p1_q9():
    # The curve crosses the x-axis at x = 1 and peaks at x = e, so the
    # shaded region runs exactly from the crossing to the maximum.
    assert abs(math.log(1) / 1) < 1e-12
    assert abs((1 - math.log(math.e))) < 1e-12
    fig, ax = plt.subplots(figsize=(4.8, 3.0))
    xs = np.linspace(0.35, 6.0, 500)
    ys = np.log(xs) / xs
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    xr = np.linspace(1, math.e, 300)
    ax.fill_between(xr, np.log(xr) / xr, color=LIGHT, edgecolor=BLACK,
                    lw=0.6, hatch="///")
    peak = 1 / math.e
    ax.plot([math.e, math.e], [0, peak], color=BLACK, lw=1.0)
    ax.text(1, -0.035, "$1$", ha="center", va="top", fontsize=12, color=BLACK)
    ax.text(math.e, -0.035, "$\\mathrm{e}$", ha="center", va="top",
            fontsize=12, color=BLACK)
    ax.text(1.85, 0.11, "$R$", ha="center", va="center", fontsize=13,
            color=BLACK)
    ax.text(3.6, 0.30, "$y = \\dfrac{\\ln x}{x}$", ha="left", va="center",
            fontsize=12, color=BLACK)
    arrow_axes(ax, (-0.4, 6.3), (-0.55, 0.55))
    save(fig, "ib-aahl-p1-t4-q9.png")


# ── P2 Q8: velocity v(t) = 4 sin t - t on 0 <= t <= 4 ─────────────────
def p2_q8():
    # v(0) = 0 and v changes sign once more in (0, 4); the graph must show
    # that single crossing, which is what parts (a) and (d) hang on.
    v = lambda tt: 4 * math.sin(tt) - tt
    assert v(2.0) > 0 > v(3.0)
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    ts = np.linspace(0, 4, 500)
    vs = 4 * np.sin(ts) - ts
    ax.plot(ts, vs, color=BLACK, lw=1.6)
    for gy in (-2, -1, 1, 2):
        ax.plot([0, 4.2], [gy, gy], color="0.88", lw=0.8, zorder=0)
        ax.text(-0.12, gy, str(gy), ha="right", va="center", fontsize=11,
                color=BLACK)
    for gt in (1, 2, 3, 4):
        ax.plot([gt, gt], [-0.09, 0.09], color=BLACK, lw=1.0)
        ax.text(gt, -0.22, str(gt), ha="center", va="top", fontsize=11,
                color=BLACK)
    ax.text(2.1, -3.05, "$t$ (seconds)", ha="center", va="top", fontsize=12,
            color=BLACK)
    ax.text(-0.75, 0.9, "$v$ (m s$^{-1}$)", rotation=90, va="center",
            fontsize=12, color=BLACK)
    arrow_axes(ax, (-0.55, 4.6), (-3.0, 3.2), xlabel="", ylabel="")
    save(fig, "ib-aahl-p2-t4-q8.png")


# ── P2 Q9: triangle ABC with AB = 9, AC = 12, angle A = 70, bisector AD ─
def p2_q9():
    AB, AC, A_deg = 9.0, 12.0, 70.0
    A = np.array([0.0, 0.0])
    B = np.array([AB, 0.0])
    th = math.radians(A_deg)
    C = np.array([AC * math.cos(th), AC * math.sin(th)])
    # AD bisects angle A, so D divides BC with BD : DC = AB : AC = 3 : 4.
    D = B + (AB / (AB + AC)) * (C - B)
    assert abs(np.linalg.norm(B - D) / np.linalg.norm(D - C) - AB / AC) < 1e-9
    fig, ax = plt.subplots(figsize=(4.8, 3.6))
    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.6)
    ax.plot([A[0], D[0]], [A[1], D[1]], color=BLACK, lw=1.2, ls="--")
    for P, lab, off in [(A, "$A$", (-0.5, -0.35)), (B, "$B$", (0.25, -0.35)),
                        (C, "$C$", (0.15, 0.3)), (D, "$D$", (0.3, 0.05))]:
        ax.text(P[0] + off[0], P[1] + off[1], lab, fontsize=13, color=BLACK)
    ax.text(AB / 2, -0.55, "$9$", ha="center", va="top", fontsize=12,
            color=BLACK)
    mAC = (A + C) / 2
    ax.text(mAC[0] - 0.45, mAC[1], "$12$", ha="right", va="center",
            fontsize=12, color=BLACK)
    # the 70 degree angle arc at A
    arc = np.linspace(0, th, 60)
    rr = 1.7
    ax.plot(rr * np.cos(arc), rr * np.sin(arc), color=BLACK, lw=1.0)
    ax.text(rr * 1.45 * math.cos(th / 2), rr * 1.45 * math.sin(th / 2),
            "$70^\\circ$", ha="center", va="center", fontsize=12, color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.6, max(B[0], C[0]) + 1.4)
    ax.set_ylim(-1.5, C[1] + 1.2)
    save(fig, "ib-aahl-p2-t4-q9.png")


if __name__ == "__main__":
    p1_q9()
    p2_q8()
    p2_q9()
