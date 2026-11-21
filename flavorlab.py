#!/usr/bin/env python3
"""
FlavorLab - visual flavor design toolkit (static PNG charts + JSON for agents).

First module: hot / chili sauce design.

    python flavorlab.py card recipes/mango_habanero.json          # full "sauce card"
    python flavorlab.py card recipes/x.json --optimize 4          # + greedy improvement
    python flavorlab.py quick "habanero:120,mango:250,lime juice:30:finish,salt:12" --style fruity_caribbean
    python flavorlab.py pair habanero --with mango                 # pairing wheel + explanation
    python flavorlab.py bridge habanero "espresso"                 # ingredients that link two others
    python flavorlab.py map --highlight habanero,mango             # flavor map of all ingredients
    python flavorlab.py compare a.json b.json                      # overlay radars
    python flavorlab.py list | info NAME | families | styles | preps
    add --json to card/quick/pair/bridge for machine-readable output (for agents)

Data: ingredients*.csv packs (same folder, or --db PATHS). Model: model.py. All numbers are heuristic
0-10 intensities - edit / extend the CSV freely. See README.md / FLAVOR_GUIDE.md.
"""
import argparse
import json
import math
import os
import sys
import textwrap

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

from model import *  # noqa: E402,F401,F403  (data + model live in model.py)

# ----------------------------------------------------------------------------
# Visual system (validated categorical order - see README)
# ----------------------------------------------------------------------------
CAT_COLOR = {"chili": "#e34948", "fruit": "#eda100", "veg": "#1baf7a", "acid": "#eb6834",
             "savory": "#6250d6", "sweet": "#e87ba4", "herb": "#008300", "spice": "#2a78d6"}
CAT_MARKER = {"chili": "o", "fruit": "s", "veg": "^", "acid": "D", "savory": "v",
              "sweet": "P", "herb": "X", "spice": "*"}
SERIES = ["#2a78d6", "#eb6834", "#1baf7a"]          # compare: first 3 slots (all-pairs safe)
SURFACE, PAGE = "#fcfcfb", "#fcfcfb"
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, NEUTRAL = "#e1e0d9", "#c3c2b7", "#f0efec"
BLUE, RED, ORANGE, GREEN = "#2a78d6", "#e34948", "#eb6834", "#1baf7a"
SEQ = ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 9, "text.color": INK,
    "axes.edgecolor": AXIS, "axes.labelcolor": INK2, "xtick.color": MUTED, "ytick.color": INK2,
    "axes.facecolor": SURFACE, "figure.facecolor": PAGE, "savefig.facecolor": PAGE,
    "axes.spines.top": False, "axes.spines.right": False, "axes.titleweight": "bold",
    "axes.titlesize": 11, "axes.titlelocation": "left", "axes.titlepad": 10,
})


# ----------------------------------------------------------------------------
# Drawing helpers
# ----------------------------------------------------------------------------
def dl(d):
    return DIM_LABEL.get(d, d)


def radar(ax, dims, layers, title):
    """layers: list of (values_dict, kind, label, color)."""
    ang = np.linspace(0, 2 * np.pi, len(dims), endpoint=False)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels(["2", "4", "6", "8", "10"], color=MUTED, fontsize=7)
    ax.set_rlabel_position(180 / len(dims))
    ax.set_xticks(ang)
    ax.set_xticklabels([dl(d) for d in dims], fontsize=9, color=INK)
    ax.tick_params(axis="x", pad=6)
    ax.grid(color=GRID, linewidth=0.8)
    ax.spines["polar"].set_color(AXIS)
    ax.set_facecolor(SURFACE)
    for vals, kind, label, color in layers:
        v = np.array([vals.get(d, np.nan) for d in dims] + [vals.get(dims[0], np.nan)])
        a = np.append(ang, ang[0])
        if kind == "fill":
            ax.fill(a, np.nan_to_num(v), color=color, alpha=0.16, zorder=2)
            ax.plot(a, np.nan_to_num(v), color=color, lw=2, zorder=3, label=label)
            ax.scatter(ang, np.nan_to_num(v[:-1]), s=22, color=color, edgecolor=SURFACE, linewidth=1.5, zorder=4)
        elif kind == "target":
            m = ~np.isnan(v)
            ax.plot(a, np.where(m, v, np.nan), color=INK2, lw=1.4, ls=(0, (4, 2)), zorder=3, label=label)
            ax.scatter(a[m][:-1] if m[-1] else a[m], v[m][:-1] if m[-1] else v[m], s=14, marker="o",
                       facecolor=SURFACE, edgecolor=INK2, linewidth=1.2, zorder=4)
        elif kind == "raw":
            ax.plot(a, np.nan_to_num(v), color=MUTED, lw=1, ls=(0, (1, 2)), zorder=2, label=label)
        else:  # line (compare)
            ax.plot(a, np.nan_to_num(v), color=color, lw=2, zorder=3, label=label)
            ax.scatter(ang, np.nan_to_num(v[:-1]), s=20, color=color, edgecolor=SURFACE, linewidth=1.5, zorder=4)
    ax.set_title(title, pad=22, loc="center")


# Commonly cited (approximate, marketing-sourced) SHU of commercial sauces - for orientation only.
HEAT_REFS = [("Frank's RedHot", 450, 0.3), ("Sriracha", 2200, 0.3), ("Tabasco", 3750, 0.62),
             ("El Yucateco red", 5790, 0.94), ("Da Bomb", 135600, 0.3)]


def heat_strip(ax, shu):
    ax.set_xscale("log")
    ax.set_xlim(30, 1e6)
    ax.set_ylim(-1, 1)
    ax.minorticks_off()
    bands = [(30, 1000, "mild"), (1000, 5000, "medium"), (5000, 30000, "hot"), (30000, 1e6, "extreme")]
    for k, (lo, hi, lab) in enumerate(bands):
        ax.axvspan(lo, hi, ymin=0.4, ymax=0.6, color=SEQ[(0, 1, 3, 5)[k]], zorder=0, lw=0)
        ax.text(math.sqrt(lo * hi), 0, lab, ha="center", va="center", fontsize=8,
                color=INK if k < 2 else "#ffffff", zorder=1)
    for n, v, h in HEAT_REFS:
        ax.plot([v, v], [0.2, h], color=MUTED, lw=0.8, zorder=1)
        ax.text(v, h + 0.02, n, ha="center", va="bottom", fontsize=7.5, color=INK2)
    s = max(shu, 31)
    ax.plot([s], [0], marker="D", ms=14, color=RED, mec=SURFACE, mew=2, zorder=5)
    ax.annotate(f"this sauce ≈ {shu:,.0f} SHU", (s, 0), xytext=(0, -22), textcoords="offset points",
                ha="center", va="top", fontsize=10.5, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="-", color=INK2, lw=1))
    ax.set_yticks([])
    for sp in ("left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_xticks([])
    ax.set_title("Heat (Scoville, estimated: pods × dry matter × mass share)", fontsize=10)


def heat_timeline(ax, A):
    hp = A["heat_profile"]
    shown = False
    if hp["cap"].max() > 0.05:
        ax.fill_between(HT, hp["cap"], color=RED, alpha=0.12, lw=0, zorder=1)
        ax.plot(HT, hp["cap"], color=RED, lw=2, label="chili heat (capsaicinoids)", zorder=3)
        pk, half = hp["peak_s"], hp["half_s"]
        ax.annotate(f"peak ~{pk:.0f}s", (pk, hp["cap"].max()), xytext=(6, 6), textcoords="offset points",
                    fontsize=8, color=INK)
        if half:
            ax.axvline(half, color=AXIS, lw=1, ls=(0, (3, 3)), zorder=0)
            ax.text(half + 3, 0.3, f"half gone ~{half:.0f}s", fontsize=7.5, color=INK2, rotation=90, va="bottom")
        shown = True
    for key, color, ls, label in (("bite", ORANGE, (0, (5, 2)), "pepper bite (piperine / gingerol)"),
                                  ("sinus", BLUE, (0, (1, 1.5)), "sinus (mustard / wasabi)"),
                                  ("numbing", GREEN, (0, (6, 2, 1, 2)), "numbing tingle (sanshool)")):
        if hp[key].max() > 0.3:
            ax.plot(HT, hp[key], color=color, lw=2, ls=ls, label=label, zorder=2)
            shown = True
    if not shown:
        ax.text(0.5, 0.5, "no heat sources", transform=ax.transAxes, ha="center", color=MUTED)
    ax.set_xlim(0, 300)
    ax.set_ylim(0, 10)
    ax.set_xticks([0, 30, 60, 120, 180, 240, 300])
    ax.set_xticklabels(["0", "30s", "1 min", "2", "3", "4", "5 min"], fontsize=7.5)
    ax.grid(axis="y", color=GRID, lw=0.6, zorder=0)
    ax.set_ylabel("intensity", fontsize=8)
    z = hp["zones"]
    where = "  ·  ".join(f"{k} {100 * v:.0f}%" for k, v in z.items() if v > 0.005)
    ax.set_title("Heat over time" + (f"  (hits: {where})" if where else ""), fontsize=10)
    ax.legend(fontsize=7, frameon=False, loc="upper right")


def mouthfeel_panel(fig, cell, A):
    sub = cell.subgridspec(2, 1, height_ratios=[2.3, 1], hspace=0.9)
    ax = fig.add_subplot(sub[0])
    labels = [dl(d) for d in TRIG] + ["fat coating"]
    vals = [A["perceived"][d] for d in TRIG] + [A["fat_level"]]
    y = np.arange(len(vals))[::-1]
    ax.barh(y, [10] * len(vals), height=0.6, color=NEUTRAL, zorder=1)
    ax.barh(y, vals, height=0.6, color=BLUE, zorder=2)
    for yy, v in zip(y, vals):
        ax.text(v + 0.15, yy, f"{v:.1f}", va="center", fontsize=8, color=INK, zorder=3)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.set_xlim(0, 10.8)
    ax.set_xticks([])
    ax.tick_params(axis="y", length=0)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_title("Mouthfeel & trigeminal (0-10)", fontsize=10)
    ax2 = fig.add_subplot(sub[1])
    segs = [(0, 1, "thin"), (1, 2.5, "pourable"), (2.5, 4, "thick"), (4, 6, "paste")]
    for k, (lo, hi, lab) in enumerate(segs):
        ax2.barh(0, hi - lo, left=lo, height=0.8, color=SEQ[(0, 1, 3, 5)[k]], edgecolor=SURFACE, lw=2)
        ax2.text((lo + hi) / 2, 0, lab, ha="center", va="center", fontsize=8, color=INK if k < 2 else "#ffffff")
    b = A["body"]
    ax2.plot([min(b, 5.9)], [0.62], marker="v", ms=12, color=RED, mec=SURFACE, mew=1.5, clip_on=False, zorder=5)
    name, ex = body_class(b)
    ax2.set_xlim(0, 6)
    ax2.set_ylim(-0.5, 0.8)
    ax2.axis("off")
    ax2.set_title(f"Body: {name} ({ex}), index {b:.1f}", fontsize=10, loc="left")


def pyramid_panel(ax, A):
    py = A["pyramid"]
    states = [("fresh", "fresh blend"),
              ("processed", "after cooking" if A["process"] == "cooked" else "as made (raw)"),
              ("aged", "after ~3 months")]
    cols = {"top": SEQ[1], "middle": SEQ[3], "base": SEQ[5]}
    y = np.arange(len(states))[::-1]
    for yy, (k, lab) in zip(y, states):
        left = 0.0
        for c in ("top", "middle", "base"):
            w = py[k][c]
            ax.barh(yy, w, left=left, height=0.6, color=cols[c], edgecolor=SURFACE, lw=1.5, zorder=2)
            if w >= 9:
                ax.text(left + w / 2, yy, f"{w:.0f}%", ha="center", va="center", fontsize=7.5,
                        color=INK if c == "top" else "#ffffff", zorder=3)
            left += w
        ax.text(left + 1.5, yy, f"{left:.0f}%", va="center", fontsize=8, color=INK)
    ax.set_yticks(y)
    ax.set_yticklabels([s[1] for s in states], fontsize=8.5)
    ax.set_xlim(0, 118)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color=GRID, lw=0.6, zorder=0)
    ax.set_xlabel("aroma remaining, % of fresh blend", fontsize=8, color=INK2)
    ax.legend(handles=[Patch(color=cols[c], label=f"{c} notes") for c in cols], fontsize=7.5, frameon=False,
              loc="lower right", bbox_to_anchor=(1.0, 1.0), ncol=3)
    fragile = [r["ing"].name for r in sorted(A["rows"], key=lambda r: -r["frac"] * r["ing"].potency)
               if r["ing"].vol == "t" and r["keep"] < 1][:3]
    if fragile:
        ax.text(0, -0.24, "fragile top notes: " + ", ".join(fragile) + "  →  add at the finish",
                transform=ax.transAxes, fontsize=7.5, color=INK2)
    ax.set_title("Aroma staying power", fontsize=10)


def families_panel(ax, A, n=12):
    rows = A["rows"]
    fc = A["fam_contrib"]
    tot = fc.sum(axis=0)
    idx = [i for i in np.argsort(-tot) if tot[i] > 0][:n]
    if not idx:
        ax.axis("off")
        return
    vals = 10 * tot[idx] / tot[idx[0]]
    y = np.arange(len(idx))[::-1]
    ax.barh(y, vals, height=0.62, color=BLUE, zorder=2)
    for yy, i, v in zip(y, idx, vals):
        top = [rows[k]["ing"].name for k in np.argsort(-fc[:, i])[:2] if fc[k, i] > 0]
        ax.text(v + 0.2, yy, ", ".join(short(t, 16) for t in top), va="center", fontsize=7.2, color=INK2)
    ax.set_yticks(y)
    ax.set_yticklabels([f"{FAMILIES[FAM[i]][1]}" for i in idx], fontsize=8)
    ax.set_xlim(0, 17)
    ax.set_xticks([])
    ax.tick_params(axis="y", length=0)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_visible(False)
    ax.set_title("Aroma families (relative) & main sources", fontsize=10)


def contribution(ax, A):
    rows = A["rows"]
    dims = TASTE + AROMA
    order = sorted(range(len(rows)), key=lambda i: (CATEGORIES.index(rows[i]["ing"].category), -A["impact"][i]))
    y = np.arange(len(dims))[::-1]
    for k, d in enumerate(dims):
        j = DIMS.index(d)
        left = 0.0
        for i in order:
            w = A["shares"][i, j]
            if w <= 0.01:
                continue
            c = CAT_COLOR[rows[i]["ing"].category]
            ax.barh(y[k], w, left=left, height=0.72, color=c, edgecolor=SURFACE, linewidth=1.5, zorder=2)
            if w >= 1.15:
                txt = "#0b0b0b" if rows[i]["ing"].category == "fruit" else "#ffffff"
                ax.text(left + w / 2, y[k], short(rows[i]["ing"].name, max(4, int(w * 2.6))), ha="center",
                        va="center", fontsize=6.8, color=txt, zorder=3)
            left += w
        ax.text(left + 0.12, y[k], f"{A['perceived'][d]:.1f}", va="center", fontsize=8, color=INK)
    ax.axhline(y[len(TASTE) - 1] - 0.5, color=AXIS, lw=0.8, ls=(0, (3, 3)))
    ax.set_yticks(y)
    ax.set_yticklabels([dl(d) for d in dims], fontsize=9)
    ax.set_xlim(0, 10.8)
    ax.set_xticks(range(0, 11, 2))
    ax.grid(axis="x", color=GRID, lw=0.6, zorder=0)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("perceived intensity (0-10) - segment = ingredient's share", fontsize=8, color=INK2)
    cats = [c for c in CATEGORIES if any(r["ing"].category == c for r in rows)]
    ax.legend(handles=[Patch(color=CAT_COLOR[c], label=CAT_LABEL[c]) for c in cats], loc="lower right",
              fontsize=7.5, frameon=False, ncol=1)
    ax.set_title("Who drives each flavor?  (taste above dashed line, aroma below)")


def gap_chart(ax, A):
    gaps = A["gaps"]
    dims = [d for d in DIMS if d in gaps]
    y = np.arange(len(dims))[::-1]
    lim = max(4, max(abs(g["diff"]) for g in gaps.values()) + 1)
    for k, d in enumerate(dims):
        g = gaps[d]
        ax.barh(y[k], 2 * g["tol"], left=-g["tol"], height=0.8, color=NEUTRAL, zorder=1)
        c = AXIS if g["status"] == "ok" else (RED if g["diff"] > 0 else BLUE)
        ax.barh(y[k], g["diff"], height=0.5, color=c, zorder=2)
        off = 0.15 if g["diff"] >= 0 else -0.15
        ax.text(g["diff"] + off, y[k], f"{g['diff']:+.1f}", va="center", ha="left" if g["diff"] >= 0 else "right",
                fontsize=7.5, color=INK)
    ax.axvline(0, color=INK2, lw=1, zorder=3)
    ax.set_xlim(-lim, lim)
    ax.set_yticks(y)
    ax.set_yticklabels([dl(d) for d in dims], fontsize=8.5)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.text(0.02, -0.1, "◀ too little", transform=ax.transAxes, fontsize=8, color=BLUE, va="top")
    ax.text(0.98, -0.1, "too much ▶", transform=ax.transAxes, fontsize=8, color=RED, va="top", ha="right")
    ax.text(0.5, -0.1, "gray band = OK zone", transform=ax.transAxes, fontsize=7.5, color=MUTED, va="top",
            ha="center")
    ax.set_title(f"Gap to target: {A['style_label']}  (fit {A['fit']:.0f}/100)")


def pair_heatmap(ax, A, max_n=12):
    rows = A["rows"]
    idx = [i for i in np.argsort(-A["impact"]) if not rows[i]["ing"].neutral][:max_n]
    idx = sorted(idx, key=lambda i: (CATEGORIES.index(rows[i]["ing"].category), -A["impact"][i]))
    if len(idx) < 2:
        ax.axis("off")
        ax.text(0.5, 0.5, "Need 2+ aromatic ingredients", ha="center", va="center", color=MUTED)
        return
    M = A["pair_matrix"][np.ix_(idx, idx)]
    cmap = LinearSegmentedColormap.from_list("seq", SEQ)
    ax.imshow(np.ma.masked_invalid(M), cmap=cmap, vmin=0, vmax=100)
    for a in range(len(idx)):
        for b in range(len(idx)):
            if a != b and not np.isnan(M[a, b]):
                ax.text(b, a, f"{M[a, b]:.0f}", ha="center", va="center", fontsize=7.5,
                        color="#ffffff" if M[a, b] > 55 else INK)
    names = [short(rows[i]["ing"].name, 14) for i in idx]
    ax.set_xticks(range(len(idx)))
    ax.set_yticks(range(len(idx)))
    ax.set_xticklabels(names, rotation=45, ha="right", fontsize=7.5)
    ax.set_yticklabels(names, fontsize=7.5)
    ax.tick_params(length=0)
    for s in ax.spines.values():
        s.set_visible(False)
    for i_, i in enumerate(idx):  # category chip next to label
        ax.add_patch(plt.Rectangle((-0.5 - 0.35, i_ - 0.4), 0.25, 0.8, color=CAT_COLOR[rows[i]["ing"].category],
                                   clip_on=False))
    ax.set_xlim(-0.95, len(idx) - 0.5)
    ax.set_title(f"Pairing matrix  (harmony {A['harmony']:.0f}/100)", pad=20)
    neutral = [r["ing"].name for r in rows if r["ing"].neutral]
    if neutral:
        ax.text(1.0, 1.01, "not scored (neutral): " + ", ".join(neutral), transform=ax.transAxes, fontsize=7,
                color=MUTED, va="bottom", ha="right")


def moves_chart(ax, moves):
    if not moves:
        ax.axis("off")
        ax.set_title("Next best moves")
        ax.text(0.02, 0.8, "No single change improves the score -\nthis is a local optimum for the style.",
                transform=ax.transAxes, color=INK2, va="top")
        return
    m = moves[:8]
    y = np.arange(len(m))[::-1]
    vals = [x["d_overall"] for x in m]
    ax.barh(y, vals, height=0.6, color=BLUE, zorder=2)
    for yy, x in zip(y, m):
        ax.text(x["d_overall"] + max(vals) * 0.02, yy,
                f"+{x['d_overall']:.1f}   (fit {x['d_fit']:+.1f}, harmony {x['d_harmony']:+.1f})",
                va="center", fontsize=7.5, color=INK2)
    ax.set_yticks(y)
    ax.set_yticklabels([x["move"] for x in m], fontsize=8.5)
    ax.set_xlim(0, max(vals) * 1.9)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.grid(axis="x", color=GRID, lw=0.6, zorder=0)
    ax.set_xlabel("overall score gain", fontsize=8, color=INK2)
    ax.set_title("Next best single moves")


def formula_panel(ax, A):
    ax.axis("off")
    ax.set_title("Formula & checks")
    rows = sorted(A["rows"], key=lambda r: -r["g"])
    yy = 0.97
    ax.text(0.0, yy, "ingredient", fontsize=7.5, color=MUTED, transform=ax.transAxes)
    ax.text(0.62, yy, "g", fontsize=7.5, color=MUTED, ha="right", transform=ax.transAxes)
    ax.text(0.78, yy, "%", fontsize=7.5, color=MUTED, ha="right", transform=ax.transAxes)
    step = min(0.05, 0.5 / max(1, len(rows)))
    for r in rows:
        yy -= step
        ax.add_patch(plt.Rectangle((0.0, yy - 0.008), 0.018, 0.03, color=CAT_COLOR[r["ing"].category],
                                   transform=ax.transAxes, clip_on=False))
        tags = r["prep"] + (["finish"] if r["stage"] == "finish" else [])
        prep = f" ({'+'.join(tags)})" if tags else ""
        ax.text(0.03, yy, short(r["ing"].name + prep, 34), fontsize=8, transform=ax.transAxes)
        ax.text(0.62, yy, f"{r['g']:g}", fontsize=8, ha="right", transform=ax.transAxes)
        ax.text(0.78, yy, f"{100 * r['frac']:.1f}", fontsize=8, ha="right", transform=ax.transAxes)
    yy -= step * 1.2
    ax.plot([0, 0.8], [yy + step * 0.5] * 2, color=GRID, lw=0.8, transform=ax.transAxes)
    ax.text(0.03, yy, f"total  ·  process: {A['process']}", fontsize=8, fontweight="bold", transform=ax.transAxes)
    ax.text(0.62, yy, f"{A['total_g']:g}", fontsize=8, fontweight="bold", ha="right", transform=ax.transAxes)
    yy -= step * 1.4
    for w in A["warnings"]:
        txt = textwrap.fill("⚠ " + w, 66)
        ax.text(0.0, yy, txt, fontsize=7.5, color=INK2, transform=ax.transAxes, va="top")
        yy -= 0.045 * (txt.count("\n") + 1) + 0.012


def save(fig, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def slug(s):
    return "".join(c if c.isalnum() else "_" for c in s.lower()).strip("_")


# ----------------------------------------------------------------------------
# Figures
# ----------------------------------------------------------------------------
def sauce_card(db, A, moves, out):
    fig = plt.figure(figsize=(20, 23))
    gs = fig.add_gridspec(4, 3, height_ratios=[1.0, 1.05, 0.95, 0.95], hspace=0.42, wspace=0.38,
                          left=0.06, right=0.97, top=0.9, bottom=0.04)
    fig.text(0.06, 0.968, A["name"], fontsize=22, fontweight="bold", color=INK)
    fig.text(0.06, 0.952, f"{A['style_label']}  ·  {A['total_g']:g} g batch  ·  "
             f"overall {A['overall']:.0f}  ·  style fit {A['fit']:.0f}  ·  harmony {A['harmony']:.0f}  ·  "
             f"FlavorLab v{VERSION}", fontsize=11, color=INK2)
    tgt = STYLES[A["style"]]["target"]
    ax = fig.add_subplot(gs[0, 0], projection="polar")
    radar(ax, TASTE, [(A["raw"], "raw", "raw (before interactions)", None), (tgt, "target", "style target", None),
                      (A["perceived"], "fill", "this sauce (perceived)", BLUE)], "Taste")
    ax = fig.add_subplot(gs[0, 1], projection="polar")
    radar(ax, AROMA, [(A["raw"], "raw", "raw", None), (tgt, "target", "target", None),
                      (A["perceived"], "fill", "perceived", BLUE)], "Aroma")
    handles = [Line2D([], [], color=BLUE, lw=2, marker="o", label="this sauce (perceived)"),
               Line2D([], [], color=INK2, lw=1.4, ls=(0, (4, 2)), marker="o", mfc=SURFACE, label="style target"),
               Line2D([], [], color=MUTED, lw=1, ls=(0, (1, 2)), label="raw sum (before taste interactions)")]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.055, 0.944), ncol=3, frameon=False,
               fontsize=8.5)
    gap_chart(fig.add_subplot(gs[0, 2]), A)
    contribution(fig.add_subplot(gs[1, 0:2]), A)
    formula_panel(fig.add_subplot(gs[1, 2]), A)
    sub = gs[2, 0].subgridspec(2, 1, height_ratios=[1, 2.4], hspace=0.75)
    heat_strip(fig.add_subplot(sub[0]), A["shu"])
    heat_timeline(fig.add_subplot(sub[1]), A)
    mouthfeel_panel(fig, gs[2, 1], A)
    pyramid_panel(fig.add_subplot(gs[2, 2]), A)
    families_panel(fig.add_subplot(gs[3, 0]), A)
    pair_heatmap(fig.add_subplot(gs[3, 1]), A)
    moves_chart(fig.add_subplot(gs[3, 2]), moves)
    return save(fig, out)


def pair_wheel(db, name, top, out):
    a = db.get(name)
    scores = []
    for b in db.items.values():
        if b.name == a.name or b.neutral:
            continue
        scores.append((pair_score(db, a, b), b))
    scores.sort(key=lambda t: -t[0])
    best = scores[:top]
    best.sort(key=lambda t: (CATEGORIES.index(t[1].category), -t[0]))
    fig = plt.figure(figsize=(11, 11))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ang = np.linspace(0, 2 * np.pi, len(best), endpoint=False)
    ax.set_ylim(0, 112)
    ax.set_yticks([])
    ax.set_xticks([])
    smax, smin = max(t[0] for t in best), min(t[0] for t in best)
    ax.grid(color=GRID, lw=0.8)
    ax.spines["polar"].set_visible(False)
    for th, (s, b) in zip(ang, best):
        r = 30 + 62 * (smax - s) / max(1e-9, smax - smin)
        ax.plot([th, th], [0, r], color=AXIS, lw=1 + 3 * s / 100, zorder=1)
        ax.scatter([th], [r], s=170, color=CAT_COLOR[b.category], marker=CAT_MARKER[b.category],
                   edgecolor=SURFACE, lw=2, zorder=3)
        classic = frozenset((a.name, b.name)) in db.classic
        ax.text(th, r + 9, f"{b.name}\n{s:.0f}{' ★' if classic else ''}", ha="center", va="center", fontsize=8,
                color=INK)
    ax.scatter([0], [0], s=3200, color=CAT_COLOR[a.category], zorder=4, edgecolor=SURFACE, lw=3)
    ax.text(0, 0, a.name.replace(" ", "\n"), ha="center", va="center", fontsize=9, fontweight="bold",
            color="#0b0b0b" if a.category == "fruit" else "#ffffff", zorder=5)
    cats = sorted({b.category for _, b in best}, key=CATEGORIES.index)
    ax.legend(handles=[Line2D([], [], ls="", marker=CAT_MARKER[c], color=CAT_COLOR[c], ms=9, label=CAT_LABEL[c])
                       for c in cats], loc="upper left", bbox_to_anchor=(-0.08, 1.06), frameon=False, fontsize=8)
    fam = ", ".join(FAMILIES[FAM[i]][1] for i in np.argsort(-a.fam)[:3] if a.fam[i] > 0)
    fig.text(0.5, 0.965, f"Best partners for {a.name}", ha="center", fontsize=17, fontweight="bold")
    fig.text(0.5, 0.94, f"top {len(best)} by score ({smin:.0f}-{smax:.0f}); closer to the center = stronger  ·  "
             f"★ = classic pairing  ·  its aroma: {fam or 'neutral'}", ha="center", fontsize=8.5, color=INK2)
    save(fig, out)
    return out, [(b.name, round(s, 1)) for s, b in sorted(best, key=lambda t: -t[0])]


def flavor_map(db, out, highlight=(), categories=None):
    names = [n for n, i in db.items.items() if not i.neutral and (not categories or i.category in categories)]
    X = []
    for n in names:
        i = db.items[n]
        X.append(list(i.vec / 10) + [heat_index(i.eff_shu) / 10] + list(0.25 * i.fam))
    X = np.array(X)
    Xc = X - X.mean(axis=0)
    U, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    P = Xc @ Vt[:2].T
    ev = S ** 2 / (S ** 2).sum()
    fig, ax = plt.subplots(figsize=(19, 15))
    hl = {db.get(h).name for h in highlight}
    for c in CATEGORIES:
        m = [k for k, n in enumerate(names) if db.items[n].category == c]
        if m:
            ax.scatter(P[m, 0], P[m, 1], s=60, marker=CAT_MARKER[c], color=CAT_COLOR[c], edgecolor=SURFACE,
                       lw=1.2, label=CAT_LABEL[c], zorder=3)
    texts = []
    for k, n in enumerate(names):
        bold = n in hl
        t = ax.text(P[k, 0], P[k, 1] + 0.012, n, fontsize=9 if bold else 6.5, ha="center", va="bottom",
                    fontweight="bold" if bold else "normal", color=INK if bold else INK2, zorder=4)
        texts.append(t)
        if bold:
            ax.scatter(P[k, 0], P[k, 1], s=320, facecolor="none", edgecolor=INK, lw=1.5, zorder=5)
    _repel(fig, ax, texts)
    feats = VEC_DIMS + ["heat"] + FAM      # axis meaning: top loading features
    for comp, axis in ((0, "x"), (1, "y")):
        load = Vt[comp]
        hi = [feats[i] for i in np.argsort(-load)[:3]]
        lo = [feats[i] for i in np.argsort(load)[:3]]
        lab = f"PC{comp + 1} ({ev[comp]:.0%}):  ← {', '.join(lo)}   ·   {', '.join(hi)} →"
        (ax.set_xlabel if axis == "x" else ax.set_ylabel)(lab, fontsize=9, color=INK2)
    ax.grid(color=GRID, lw=0.6, zorder=0)
    ax.legend(frameon=False, fontsize=9, loc="best")
    ax.set_title("Flavor map - nearby ingredients share taste/aroma character (PCA of the database)", fontsize=14)
    return save(fig, out)


def _repel(fig, ax, texts, iters=60):
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    inv = ax.transData.inverted()
    for _ in range(iters):
        moved = False
        bbs = [t.get_window_extent(r).expanded(1.02, 1.1) for t in texts]
        for i in range(len(texts)):
            for j in range(i + 1, len(texts)):
                if bbs[i].overlaps(bbs[j]):
                    dy = 1.5 if bbs[i].y0 >= bbs[j].y0 else -1.5
                    for t, s in ((texts[i], dy), (texts[j], -dy)):
                        x, y = ax.transData.transform(t.get_position())
                        t.set_position(inv.transform((x, y + s)))
                    moved = True
        if not moved:
            break


def compare_fig(db, analyses, out):
    fig = plt.figure(figsize=(21, 8.5))
    gs = fig.add_gridspec(1, 3, left=0.04, right=0.97, top=0.8, bottom=0.08, wspace=0.4)
    for k, (dims, title) in enumerate(((TASTE, "Taste"), (AROMA, "Aroma"), (TRIG, "Mouthfeel"))):
        ax = fig.add_subplot(gs[0, k], projection="polar")
        layers = [(A["perceived"], "line", A["name"], SERIES[i]) for i, A in enumerate(analyses[:3])]
        radar(ax, dims, layers, title)
    fig.text(0.04, 0.95, "Recipe comparison", fontsize=18, fontweight="bold")
    handles = [Line2D([], [], color=SERIES[i], lw=2, marker="o",
                      label=f"{A['name']}  ·  {A['style_label']} fit {A['fit']:.0f}  ·  "
                            f"harmony {A['harmony']:.0f}  ·  ≈{A['shu']:,.0f} SHU  ·  body {body_class(A['body'])[0]}")
               for i, A in enumerate(analyses[:3])]
    fig.legend(handles=handles, loc="upper left", bbox_to_anchor=(0.04, 0.93), frameon=False, fontsize=9)
    return save(fig, out)


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------
def run_card(db, recipe, args):
    A = analyze(db, recipe)
    moves = [] if args.no_suggest else suggest(db, recipe, base=A)
    os.makedirs(args.out, exist_ok=True)
    path = sauce_card(db, A, moves, os.path.join(args.out, f"{slug(A['name'])}_card.png"))
    result = {"card": path, "analysis": summary(db, A, moves)}
    if args.optimize:
        new, log = optimize(db, recipe, steps=args.optimize)
        B = analyze(db, new)
        bmoves = [] if args.no_suggest else suggest(db, new, base=B)
        p2 = sauce_card(db, B, bmoves, os.path.join(args.out, f"{slug(A['name'])}_optimized_card.png"))
        p3 = compare_fig(db, [A, B], os.path.join(args.out, f"{slug(A['name'])}_vs_optimized.png"))
        rp = os.path.join(args.out, f"{slug(A['name'])}_optimized.json")
        with open(rp, "w", encoding="utf-8") as f:
            json.dump(new, f, indent=2, ensure_ascii=False)
        result.update({"optimized_card": p2, "comparison": p3, "optimized_recipe": rp,
                       "optimized": summary(db, B, bmoves, log)})
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        s = result["analysis"]["scores"]
        print(f"{A['name']}: overall {s['overall']} | fit {s['style_fit']} | harmony {s['harmony']} | "
              f"≈{A['shu']:,.0f} SHU | body {body_class(A['body'])[0]}")
        for k in ("card", "optimized_card", "comparison", "optimized_recipe"):
            if k in result:
                print(f"  {k}: {result[k]}")
        for m in moves[:5]:
            print(f"  suggestion: {m['move']}  (+{m['d_overall']})")
    return result


def main(argv=None):
    ap = argparse.ArgumentParser(description="FlavorLab - visualize flavor profiles & interactions")
    ap.add_argument("--db", nargs="+", default=DEFAULT_DB, help="ingredient CSV(s); default: all ingredients*.csv")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def common(p):
        p.add_argument("--out", default="out", help="output folder")
        p.add_argument("--json", action="store_true", help="print machine-readable JSON")
        p.add_argument("--no-suggest", action="store_true")
        p.add_argument("--optimize", type=int, default=0, metavar="N", help="greedy-improve N steps")

    p = sub.add_parser("card", help="sauce card from a recipe JSON")
    p.add_argument("recipe")
    p.add_argument("--style", help="override style")
    common(p)
    p = sub.add_parser("quick", help="sauce card from an inline spec 'name:g[:prep+prep|finish],...'")
    p.add_argument("spec")
    p.add_argument("--style", default="balanced")
    p.add_argument("--name", default="Quick sauce")
    p.add_argument("--fermented", action="store_true")
    p.add_argument("--raw", action="store_true", help="uncooked sauce (no aroma loss)")
    p.add_argument("--save", help="also save recipe JSON here")
    common(p)
    p = sub.add_parser("pair", help="pairing wheel for one ingredient")
    p.add_argument("name")
    p.add_argument("--top", type=int, default=18)
    p.add_argument("--with", dest="with_", help="explain score vs this ingredient")
    p.add_argument("--out", default="out")
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("bridge", help="ingredients that pair with both A and B")
    p.add_argument("a")
    p.add_argument("b")
    p.add_argument("--top", type=int, default=10)
    p.add_argument("--json", action="store_true")
    p = sub.add_parser("map", help="PCA flavor map of the database")
    p.add_argument("--highlight", default="")
    p.add_argument("--categories", default="")
    p.add_argument("--out", default="out")
    p = sub.add_parser("compare", help="overlay up to 3 recipes")
    p.add_argument("recipes", nargs="+")
    p.add_argument("--out", default="out")
    p = sub.add_parser("list", help="list ingredients")
    p.add_argument("--category")
    p = sub.add_parser("info", help="ingredient details")
    p.add_argument("name")
    sub.add_parser("families", help="list aroma families with top ingredients")
    sub.add_parser("styles", help="list target styles")
    sub.add_parser("preps", help="list prep modifiers")

    args = ap.parse_args(argv)
    db = DB(args.db)

    if args.cmd == "card":
        r = load_recipe(args.recipe)
        if args.style:
            r["style"] = args.style
        return run_card(db, r, args)
    if args.cmd == "quick":
        r = normalize_recipe({"name": args.name, "style": args.style, "fermented": args.fermented,
                              "process": "raw" if args.raw else "cooked", "ingredients": parse_quick(args.spec)})
        if args.save:
            with open(args.save, "w", encoding="utf-8") as f:
                json.dump(r, f, indent=2, ensure_ascii=False)
        return run_card(db, r, args)
    if args.cmd == "pair":
        path, best = pair_wheel(db, args.name, args.top, os.path.join(args.out, f"pair_{slug(args.name)}.png"))
        res = {"wheel": path, "top": best}
        if args.with_:
            res["explain"] = pair_score(db, db.get(args.name), db.get(args.with_), explain=True)
        if args.json:
            print(json.dumps(res, indent=2, ensure_ascii=False))
        else:
            print(path)
            for n, s in best:
                print(f"  {s:5.1f}  {n}")
            if "explain" in res:
                print("  explain:", res["explain"])
        return res
    if args.cmd == "bridge":
        a, b = db.get(args.a), db.get(args.b)
        res = {"a": a.name, "b": b.name, "direct": round(pair_score(db, a, b), 1),
               "bridges": bridges(db, a, b, top=args.top)}
        if args.json:
            print(json.dumps(res, indent=2, ensure_ascii=False))
        else:
            print(f"{a.name} + {b.name}: direct score {res['direct']}")
            for n, s in res["bridges"]:
                print(f"  {s:5.1f}  {n}")
        return res
    if args.cmd == "map":
        hl = [h for h in args.highlight.split(",") if h.strip()]
        cats = [c for c in args.categories.split(",") if c.strip()] or None
        print(flavor_map(db, os.path.join(args.out, "flavor_map.png"), hl, cats))
        return
    if args.cmd == "compare":
        As = [analyze(db, load_recipe(p)) for p in args.recipes]
        print(compare_fig(db, As, os.path.join(args.out, "compare.png")))
        return
    if args.cmd == "list":
        for c in CATEGORIES:
            if args.category and c != args.category:
                continue
            names = sorted(n for n, i in db.items.items() if i.category == c)
            print(f"{CAT_LABEL[c]} ({c}, {len(names)}): " + ", ".join(names))
        return
    if args.cmd == "info":
        print(json.dumps(db.get(args.name).to_dict(), indent=2, ensure_ascii=False))
        return
    if args.cmd == "families":
        for f, (g, desc, comp) in FAMILIES.items():
            top = sorted(db.items.values(), key=lambda i: -i.fam[FI[f]])
            top = [i.name for i in top if i.fam[FI[f]] >= 2][:8]
            print(f"{f:16s} [{g}] {desc} - {comp}\n{'':16s} e.g. {', '.join(top)}")
        return
    if args.cmd == "styles":
        for k, s in STYLES.items():
            print(f"{k:18s} {s['label']}  target={s['target']}")
        return
    if args.cmd == "preps":
        for k, v in PREP.items():
            print(f"{k:12s} {v}")
        print("finish       stage: added after cooking - keeps top notes & sinus kick")
        return


if __name__ == "__main__":
    try:
        main()
    except (KeyError, ValueError) as e:
        sys.exit(f"error: {e}")
