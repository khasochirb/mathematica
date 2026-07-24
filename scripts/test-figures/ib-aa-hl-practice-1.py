"""Figures for AA HL Practice Papers 1 & 2 (testId ib-hl-practice-1).

matplotlib from the SAME parameters as the builder scripts, pure
black-on-white line art (dark mode inverts), exact geometry, dpi=200,
tight bbox, <= 50 KB each.

Output: public/ib-figures/ib-aahl-p1-t1-q9.png  (curve x e^{-x}, region 0..1)
        public/ib-figures/ib-aahl-p2-t1-q1.png  (triangle AB=8, AC=11, A=37 deg)
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


# ── P1 Q9: y = x e^{-x} for x in [0, 4], region under curve on [0, 1] ────
def p1_q9():
    fig, ax = plt.subplots(figsize=(4.6, 2.9))
    xs = np.linspace(0, 4.0, 500)
    ys = xs * np.exp(-xs)
    ax.plot(xs, ys, color=BLACK, lw=1.6)
    xr = np.linspace(0, 1.0, 120)
    ax.fill_between(xr, xr * np.exp(-xr), color=LIGHT, edgecolor=BLACK,
                    lw=0.8, hatch="///")
    ax.plot([1, 1], [0, 1 * np.exp(-1)], color=BLACK, lw=1.0)
    ax.text(0.5, 0.055, "$R$", ha="center", va="center", fontsize=13,
            color=BLACK)
    ax.text(1.0, -0.035, "$1$", ha="center", va="top", fontsize=12,
            color=BLACK)
    ax.text(2.6, 0.30, "$y = x e^{-x}$", ha="left", va="center",
            fontsize=13, color=BLACK)
    arrow_axes(ax, (-0.35, 4.25), (-0.08, 0.48))
    save(fig, "ib-aahl-p1-t1-q9.png")


# ── P2 Q1: triangle ABC, AB = 8, AC = 11, angle A = 37 degrees ───────────
def p2_q1():
    A = np.array([0.0, 0.0])
    B = np.array([8.0, 0.0])
    th = np.deg2rad(37.0)
    C = 11.0 * np.array([np.cos(th), np.sin(th)])
    fig, ax = plt.subplots(figsize=(4.4, 3.0))
    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], color=BLACK, lw=1.5)
    # angle arc at A
    arc = np.linspace(0, th, 60)
    ax.plot(1.3 * np.cos(arc), 1.3 * np.sin(arc), color=BLACK, lw=1.0)
    ax.text(1.85, 0.62, "$37°$", ha="left", va="center", fontsize=12,
            color=BLACK)
    ax.text(-0.25, -0.05, "$A$", ha="right", va="top", fontsize=13, color=BLACK)
    ax.text(8.15, -0.05, "$B$", ha="left", va="top", fontsize=13, color=BLACK)
    ax.text(C[0] + 0.1, C[1] + 0.1, "$C$", ha="left", va="bottom",
            fontsize=13, color=BLACK)
    ax.text(4.0, -0.35, "$8$ cm", ha="center", va="top", fontsize=12,
            color=BLACK)
    mid_ac = (A + C) / 2
    ax.text(mid_ac[0] - 0.35, mid_ac[1] + 0.25, "$11$ cm", ha="right",
            va="bottom", fontsize=12, color=BLACK)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_xlim(-1.2, 9.6)
    ax.set_ylim(-1.2, 7.6)
    save(fig, "ib-aahl-p2-t1-q1.png")


if __name__ == "__main__":
    p1_q9()
    p2_q1()
