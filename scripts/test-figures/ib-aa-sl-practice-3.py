"""Figures for AA SL Practice Papers 1 & 2 (testId ib-practice-3).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aasl-p1-t3-q7.png   (sector + shaded segment)
        public/ib-figures/ib-aasl-p1-t3-q9.png   (curve 4x - x^2 vs line y = x)
        public/ib-figures/ib-aasl-p2-t3-q3.png   (rectangular-based pyramid)
        public/ib-figures/ib-aasl-p2-t3-q7.png   (projectile parabola)
"""
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
    ax.text(xlim[1], -0.04 * (ylim[1] - ylim[0]), xlabel, ha="center",
            va="top", fontsize=13, color=BLACK)
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left",
            va="center", fontsize=13, color=BLACK)


# ── P1 Q7: sector of circle, r = 6, angle 2π/3, segment shaded ───────────
def p1_q7():
    r, theta = 6.0, 2 * np.pi / 3               # same parameters as the builder
    a0, a1 = -theta / 2, theta / 2              # symmetric about x-axis
    A = r * np.array([np.cos(a0), np.sin(a0)])
    B = r * np.array([np.cos(a1), np.sin(a1)])

    fig, ax = plt.subplots(figsize=(4.6, 4.1))
    ax.set_aspect("equal")
    ax.axis("off")

    tc = np.linspace(0, 2 * np.pi, 400)
    ax.plot(r * np.cos(tc), r * np.sin(tc), color=BLACK, lw=0.9)

    # segment fill between chord AB and arc AB
    ts = np.linspace(a0, a1, 200)
    seg_x = np.concatenate([r * np.cos(ts), [A[0]]])
    seg_y = np.concatenate([r * np.sin(ts), [A[1]]])
    ax.fill(seg_x, seg_y, facecolor=LIGHT, edgecolor="none", hatch="///")

    ax.plot([0, A[0]], [0, A[1]], color=BLACK, lw=1.5)
    ax.plot([0, B[0]], [0, B[1]], color=BLACK, lw=1.5)
    ax.plot([A[0], B[0]], [A[1], B[1]], color=BLACK, lw=1.5)

    ax.text(-0.35, 0, "$O$", fontsize=14, ha="right", va="center")
    ax.text(A[0] + 0.25, A[1] - 0.2, "$A$", fontsize=14, ha="left", va="top")
    ax.text(B[0] + 0.25, B[1] + 0.2, "$B$", fontsize=14, ha="left", va="bottom")
    mid = A / 2
    ax.text(mid[0] - 0.1, mid[1] - 0.45, "$6$ cm", fontsize=12,
            ha="center", va="top", rotation=np.degrees(a0))

    ta = np.linspace(a0, a1, 60)
    ax.plot(1.1 * np.cos(ta), 1.1 * np.sin(ta), color=BLACK, lw=1.0)
    ax.text(1.9, 0.0, r"$\frac{2\pi}{3}$", fontsize=14, ha="left", va="center")

    ax.set_xlim(-7.0, 7.2)
    ax.set_ylim(-6.9, 6.9)
    save(fig, "ib-aasl-p1-t3-q7.png")


# ── P1 Q9: y = 4x - x^2 and y = x, region R between them shaded ──────────
def p1_q9():
    def f(t):
        return 4 * t - t**2

    xs = np.linspace(-0.5, 4.35, 500)
    fig, ax = plt.subplots(figsize=(5.0, 3.7))
    arrow_axes(ax, (-0.9, 4.9), (-1.6, 4.9))

    xr = np.linspace(0.0, 3.0, 300)
    ax.fill_between(xr, xr, f(xr), facecolor=LIGHT, edgecolor="none")
    ax.plot(xs, f(xs), color=BLACK, lw=1.8)
    xl = np.linspace(-0.6, 4.4, 2)
    ax.plot(xl, xl, color=BLACK, lw=1.3)
    ax.text(1.5, 2.6, "$R$", fontsize=15, ha="center", va="center")
    ax.text(-0.12, -0.15, "$O$", fontsize=13, ha="right", va="top")
    ax.text(4.15, 4.35, "$y = x$", fontsize=12, ha="left", va="center")
    ax.text(3.65, 0.9, "$y = 4x - x^2$", fontsize=12, ha="left", va="center")
    save(fig, "ib-aasl-p1-t3-q9.png")


# ── P2 Q3: pyramid, rectangular base 8 x 6, apex over centre, height 10 ──
def p2_q3():
    # oblique projection: depth direction squashed at 30°, factor 0.45
    W, D, H = 8.0, 6.0, 10.0                     # same parameters as the builder
    dx, dy = 0.45 * np.cos(np.radians(30)), 0.45 * np.sin(np.radians(30))
    A = np.array([0, 0])
    B = np.array([W, 0])
    C = np.array([W + D * dx, D * dy])
    Dp = np.array([D * dx, D * dy])
    centre = (A + C) / 2
    V = centre + np.array([0, H * 0.62])         # foreshortened height

    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    ax.set_aspect("equal")
    ax.axis("off")

    # base: front edges solid, back edges dashed
    ax.plot([A[0], B[0]], [A[1], B[1]], color=BLACK, lw=1.5)
    ax.plot([B[0], C[0]], [B[1], C[1]], color=BLACK, lw=1.5)
    ax.plot([C[0], Dp[0]], [C[1], Dp[1]], color=BLACK, lw=1.0,
            ls=(0, (4, 3)))
    ax.plot([Dp[0], A[0]], [Dp[1], A[1]], color=BLACK, lw=1.0,
            ls=(0, (4, 3)))
    # lateral edges
    for P in (A, B, C):
        ax.plot([P[0], V[0]], [P[1], V[1]], color=BLACK, lw=1.5)
    ax.plot([Dp[0], V[0]], [Dp[1], V[1]], color=BLACK, lw=1.0,
            ls=(0, (4, 3)))
    # height to centre, dashed, with right-angle tick
    ax.plot([centre[0], V[0]], [centre[1], V[1]], color=BLACK, lw=1.0,
            ls=(0, (2, 3)))
    ax.plot([centre[0]], [centre[1]], "o", ms=3, color=BLACK)

    ax.text((A[0] + B[0]) / 2, -0.45, "$8$ cm", fontsize=12, ha="center",
            va="top")
    mid_bc = (B + C) / 2
    ax.text(mid_bc[0] + 0.3, mid_bc[1] - 0.1, "$6$ cm", fontsize=12,
            ha="left", va="center")
    ax.text(centre[0] + 0.25, (centre[1] + V[1]) / 2, "$10$ cm", fontsize=12,
            ha="left", va="center")
    ax.text(V[0], V[1] + 0.3, "$V$", fontsize=14, ha="center", va="bottom")
    ax.text(A[0] - 0.25, A[1] - 0.1, "$A$", fontsize=13, ha="right", va="top")
    ax.text(B[0] + 0.25, B[1] - 0.1, "$B$", fontsize=13, ha="left", va="top")
    ax.text(C[0] + 0.3, C[1], "$C$", fontsize=13, ha="left", va="center")
    ax.text(Dp[0] - 0.3, Dp[1] + 0.05, "$D$", fontsize=13, ha="right",
            va="center")

    ax.set_xlim(-1.4, W + D * dx + 1.5)
    ax.set_ylim(-1.4, V[1] + 1.2)
    save(fig, "ib-aasl-p2-t3-q3.png")


# ── P2 Q7: projectile h(t) = -4.9 t^2 + 19.6 t + 1.5 ────────────────────
def p2_q7():
    def h(t):
        return -4.9 * t**2 + 19.6 * t + 1.5     # same parameters as the builder

    xs = np.linspace(0.0, 4.2, 500)
    fig, ax = plt.subplots(figsize=(5.2, 3.7))
    arrow_axes(ax, (-0.5, 4.8), (-3.2, 24.5), xlabel="$t$", ylabel="$h$")
    ax.plot(xs, h(xs), color=BLACK, lw=1.8)
    ax.plot([2, 2], [0, h(2.0)], color=BLACK, lw=1.0, ls=(0, (5, 4)))
    ax.text(2.0, -0.6, "$2$", fontsize=12, ha="center", va="top")
    ax.text(-0.1, -0.6, "$O$", fontsize=13, ha="right", va="top")
    ax.text(3.6, 12.0, "$h(t)$", fontsize=13, ha="left", va="center")
    save(fig, "ib-aasl-p2-t3-q7.png")


if __name__ == "__main__":
    p1_q7()
    p1_q9()
    p2_q3()
    p2_q7()
