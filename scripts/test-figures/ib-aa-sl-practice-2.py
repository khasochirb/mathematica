"""Figures for AA SL Practice Papers 1 & 2 (testId ib-practice-2).

House rules (practice-test-authoring §8): matplotlib from the SAME parameters
as the builder scripts, pure black-on-white line art (dark mode inverts),
exact geometry, dpi=200, tight bbox, target <= 50 KB each.

Output: public/ib-figures/ib-aasl-p1-t2-q7.png   (triangle + sector)
        public/ib-figures/ib-aasl-p1-t2-q9.png   (cubic, shaded region R)
        public/ib-figures/ib-aasl-p2-t2-q3.png   (non-right triangle, cos rule)
        public/ib-figures/ib-aasl-p2-t2-q9.png   (x e^{-0.5x}, shaded area)
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


# ── P1 Q7: triangle ABC (AB=10, AC=6, A=pi/3) + sector centre A radius 6 ──
def p1_q7():
    AB, AC, angA = 10.0, 6.0, np.pi / 3          # same parameters as the builder
    A = np.array([0.0, 0.0])
    B = np.array([AB, 0.0])
    C = np.array([AC * np.cos(angA), AC * np.sin(angA)])

    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    ax.set_aspect("equal")
    ax.axis("off")

    # sector fill (light, hatched) then triangle edges on top
    th = np.linspace(0.0, angA, 200)
    sx = np.concatenate([[A[0]], AC * np.cos(th), [A[0]]])
    sy = np.concatenate([[A[1]], AC * np.sin(th), [A[1]]])
    ax.fill(sx, sy, facecolor=LIGHT, edgecolor=BLACK, lw=1.0, hatch="///")

    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.6)

    ax.text(A[0] - 0.3, A[1] - 0.15, "$A$", fontsize=14, ha="right", va="top")
    ax.text(B[0] + 0.25, B[1] - 0.1, "$B$", fontsize=14, ha="left", va="top")
    ax.text(C[0] - 0.1, C[1] + 0.25, "$C$", fontsize=14, ha="center", va="bottom")

    # side labels — only the GIVEN lengths (never BC: it is asked in part a)
    ax.text((A[0] + B[0]) / 2, -0.55, "$10$ cm", fontsize=13, ha="center")
    mid_ac = (A + C) / 2
    ax.text(mid_ac[0] - 0.35, mid_ac[1] + 0.1, "$6$ cm", fontsize=13,
            ha="right", va="bottom", rotation=60)

    # angle mark at A
    tha = np.linspace(0.0, angA, 60)
    ax.plot(1.15 * np.cos(tha), 1.15 * np.sin(tha), color=BLACK, lw=1.0)
    ax.text(1.75 * np.cos(angA / 2), 1.75 * np.sin(angA / 2),
            r"$\frac{\pi}{3}$", fontsize=14, ha="center", va="center")

    ax.set_xlim(-1.2, 11.0)
    ax.set_ylim(-1.3, 6.2)
    save(fig, "ib-aasl-p1-t2-q7.png")


# ── P1 Q9: y = x^3 - 6x^2 + 9x with region R shaded on [0, 3] ─────────────
def p1_q9():
    def f(t):
        return t**3 - 6 * t**2 + 9 * t

    xs = np.linspace(-0.55, 4.25, 500)
    fig, ax = plt.subplots(figsize=(6.0, 4.4))
    arrow_axes(ax, (-1.0, 4.7), (-3.2, 5.6))

    xr = np.linspace(0.0, 3.0, 300)
    ax.fill_between(xr, 0, f(xr), facecolor=LIGHT, edgecolor="none")
    ax.plot(xs, f(xs), color=BLACK, lw=1.8)
    ax.text(1.4, 1.15, "$R$", fontsize=15, ha="center", va="center")
    ax.text(-0.12, -0.15, "$O$", fontsize=13, ha="right", va="top")
    ax.text(3.05, -0.2, "$3$", fontsize=12, ha="center", va="top")
    ax.text(4.0, 4.9, "$C$", fontsize=13, ha="center", va="center")
    save(fig, "ib-aasl-p1-t2-q9.png")


# ── P2 Q3: non-right triangle PQR, PQ=8, QR=7, angle Q = 112° (cos rule) ──
def p2_q3():
    PQ, QR, angQ = 8.0, 7.0, np.radians(112)     # same parameters as the builder
    Q = np.array([0.0, 0.0])
    P = np.array([PQ, 0.0])                       # PQ along the base
    R = np.array([QR * np.cos(angQ), QR * np.sin(angQ)])

    fig, ax = plt.subplots(figsize=(5.8, 4.4))
    ax.set_aspect("equal")
    ax.axis("off")
    tri = np.array([P, Q, R, P])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.6)

    ax.text(Q[0] - 0.25, Q[1] - 0.15, "$Q$", fontsize=14, ha="right", va="top")
    ax.text(P[0] + 0.25, P[1] - 0.1, "$P$", fontsize=14, ha="left", va="top")
    ax.text(R[0] - 0.1, R[1] + 0.25, "$R$", fontsize=14, ha="center", va="bottom")

    ax.text((Q[0] + P[0]) / 2, -0.5, "$8$ cm", fontsize=13, ha="center")
    mid_qr = (Q + R) / 2
    ax.text(mid_qr[0] - 0.35, mid_qr[1], "$7$ cm", fontsize=13,
            ha="right", va="center")

    # angle mark at Q
    tha = np.linspace(0.0, angQ, 60)
    ax.plot(1.0 * np.cos(tha), 1.0 * np.sin(tha), color=BLACK, lw=1.0)
    ax.text(1.55 * np.cos(angQ / 2), 1.55 * np.sin(angQ / 2), "$112°$",
            fontsize=12, ha="center", va="center")

    ax.set_xlim(-3.4, 9.0)
    ax.set_ylim(-1.2, 7.4)
    save(fig, "ib-aasl-p2-t2-q3.png")


# ── P2 Q9: f(x) = x e^{-0.5x}, area shaded on [0, 4], dashed x = 4 ────────
def p2_q9():
    def f(t):
        return t * np.exp(-0.5 * t)              # same parameters as the builder

    xs = np.linspace(0.0, 7.6, 500)
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    arrow_axes(ax, (-0.7, 8.2), (-0.18, 0.95), ylabel="$y$")

    xr = np.linspace(0.0, 4.0, 300)
    ax.fill_between(xr, 0, f(xr), facecolor=LIGHT, edgecolor="none")
    ax.plot(xs, f(xs), color=BLACK, lw=1.8)
    ax.plot([4, 4], [0, f(4.0)], color=BLACK, lw=1.2, ls=(0, (5, 4)))
    ax.text(4.0, -0.04, "$4$", fontsize=13, ha="center", va="top")
    ax.text(-0.08, -0.04, "$O$", fontsize=13, ha="right", va="top")
    ax.text(6.9, 0.28, "$y = f(x)$", fontsize=13, ha="left", va="center")
    save(fig, "ib-aasl-p2-t2-q9.png")


if __name__ == "__main__":
    p1_q7()
    p1_q9()
    p2_q3()
    p2_q9()
