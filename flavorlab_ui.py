#!/usr/bin/env python3
"""
FlavorLab UI - desktop front-end (Tkinter) for flavorlab.py / model.py.

    python flavorlab_ui.py

Tabs: Recipe Designer | Sauce Card | Pairing & Bridge | Flavor Map | Compare | Ingredient Browser

* Ingredients come from every ingredients*.csv next to this file (later files override earlier ones).
  The folder is polled every few seconds, so new packs / edited rows appear without restarting.
* Recipes are designed in the UI. Save / Load use the same JSON format as the CLI (recipes/*.json).
* Charts are rendered with the existing flavorlab.py functions and shown in a zoomable viewer.
"""
import copy
import csv
import glob
import json
import os
import queue
import shutil
import sys
import tempfile
import threading
import time
import tkinter as tk
import traceback
from tkinter import filedialog, messagebox, ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import Image, ImageTk

import flavorlab as fl   # chart functions (forces the Agg backend; we only embed rendered images / Figures)
import model as M

RECIPES_DIR = os.path.join(M.HERE, "recipes")
OUT_DIR = os.path.join(M.HERE, "out")
POLL_DB_MS = 3000
PREPS = [p for p in M.PREP if p != "raw"]
RENDER_LOCK = threading.Lock()          # pyplot is not thread-safe: one chart render at a time


# ----------------------------------------------------------------------------
# Ingredient packs (auto-discovered)
# ----------------------------------------------------------------------------
def pack_files():
    return sorted(glob.glob(os.path.join(M.HERE, "ingredients*.csv")))


def files_signature(files):
    sig = []
    for p in files:
        try:
            st = os.stat(p)
            sig.append((p, st.st_mtime_ns, st.st_size))
        except OSError:
            sig.append((p, 0, 0))
    return tuple(sig)


def load_db(files):
    """-> (DB, {ingredient name: pack file name}, [issue strings]).

    Same result as model.DB(files) (later packs override earlier ones), but a row that fails validation is
    skipped and reported instead of aborting the whole load - the CSVs may be edited by someone else while the
    UI is running. Raises only if a file is unreadable or nothing valid is left."""
    if not files:
        raise ValueError("no ingredients*.csv files found next to flavorlab_ui.py")
    db = M.DB.__new__(M.DB)
    db.path, db.items, db.index = files, {}, {}
    packs, issues = {}, []
    for p in files:
        base = os.path.basename(p)
        with open(p, newline="", encoding="utf-8") as f:
            for line, row in enumerate(csv.DictReader(f), start=2):
                if not (row.get("name") or "").strip():
                    continue
                try:
                    ing = M.Ingredient(row)
                except Exception as e:                       # noqa: BLE001
                    issues.append(f"{base} line {line}: {e}")
                    continue
                db.items[ing.name] = ing
                packs[ing.name] = base
                for key in [ing.name] + ing.aliases:
                    db.index[M.norm(key)] = ing.name
    if not db.items:
        raise ValueError("no valid ingredient rows found\n" + "\n".join(issues[:5]))
    db.classic = set()
    for a, b in M.CLASSIC:
        if M.norm(a) in db.index and M.norm(b) in db.index:
            db.classic.add(frozenset((db.index[M.norm(a)], db.index[M.norm(b)])))
    return db, packs, issues


# ----------------------------------------------------------------------------
# Recipe helpers
# ----------------------------------------------------------------------------
def read_recipe_file(path, db):
    """Load a CLI-format recipe; global 'fermented' flags become per-ingredient preps."""
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    r = M.normalize_recipe(raw, default_name=os.path.splitext(os.path.basename(path))[0])
    ferm = r.get("fermented", False)
    ferm_names = set()
    if isinstance(ferm, list):
        for n in ferm:
            try:
                ferm_names.add(db.get(n).name)
            except KeyError:
                pass
    for it in r["ingredients"]:
        try:
            ing = db.get(it["item"])
        except KeyError:
            continue                                  # stays in the table, flagged as missing
        it["item"] = ing.name
        if (ferm is True and ing.category in M.FERMENTABLE) or ing.name in ferm_names:
            if "fermented" not in it["prep"]:
                it["prep"].append("fermented")
    r["fermented"] = False
    return r


def write_recipe_file(path, recipe):
    items = []
    for it in recipe["ingredients"]:
        d = {"item": it["item"], "g": it["g"]}
        if it.get("prep"):
            d["prep"] = list(it["prep"])
        if it.get("stage") == "finish":
            d["stage"] = "finish"
        items.append(d)
    out = {"name": recipe["name"], "style": recipe["style"], "process": recipe["process"],
           "ingredients": items}
    if recipe.get("notes"):
        out["notes"] = recipe["notes"]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


def bar(v, n=10):
    k = max(0, min(n, int(round(v))))
    return "█" * k + "·" * (n - k)


def ingredient_report(db, packs, name, recipe_names=()):
    """Rich-text description of one ingredient: list of (text, tag)."""
    ing = db.get(name)
    out = [(ing.name + "\n", "h"),
           (f"{M.CAT_LABEL[ing.category]}  ·  pack: {packs.get(ing.name, '?')}\n", "dim")]
    facts = []
    if ing.shu > 0:
        facts.append(f"{ing.shu:,.0f} SHU pod → ≈{ing.eff_shu:,.0f} as used "
                     f"(heat {M.heat_index(ing.eff_shu):.1f}/10; onset {ing.onset}, length {ing.length}, {ing.zone})")
    facts.append(f"potency {ing.potency:g}" + (f" · fat {ing.fat:g}" if ing.fat else "") +
                 (f" · body {ing.body:g}" if ing.body else "") + f" · {M.VOL_LABEL[ing.vol]} note")
    out.append(("\n".join(facts) + "\n\n", "n"))
    lines = []
    for d in M.TASTE[1:] + M.AROMA + M.TRIG:
        v = float(ing.vec[M.VI[d]])
        if v > 0:
            lines.append(f"{fl.dl(d):<16s}{bar(v)} {v:g}")
    if lines:
        out.append(("\n".join(lines) + "\n\n", "mono"))
    fams = [f"{M.FAMILIES[M.FAM[i]][1]} ({ing.fam[i]:g})" for i in sorted(range(len(M.FAM)), key=lambda i: -ing.fam[i])
            if ing.fam[i] > 0]
    if fams:
        out.append(("Aroma: " + ", ".join(fams) + "\n", "n"))
    if ing.aliases:
        out.append(("Also: " + ", ".join(ing.aliases) + "\n", "dim"))
    if ing.notes:
        out.append((ing.notes + "\n", "dim"))
    if ing.impact:
        out.append(("\nKey aroma compounds:\n", "b"))
        seen = dict.fromkeys(r["compound"] + (f" ({r['odor']})" if r["odor"] else "") for r in ing.impact)
        out.append(("\n".join("• " + c for c in seen) + "\n", "n"))
        out.append(("Reference data: " + ", ".join(sorted({r["confidence"] for r in ing.impact})) + "\n", "dim"))
    partners = []
    if not ing.neutral:
        for n in dict.fromkeys(recipe_names):
            try:
                o = db.get(n)
            except KeyError:
                continue
            if o.name != ing.name and not o.neutral:
                star = " ★" if frozenset((ing.name, o.name)) in db.classic else ""
                partners.append((M.pair_score(db, ing, o), o.name + star))
    if partners:
        out.append(("\nPairs with your recipe:\n", "b"))
        out.append(("\n".join(f"{s:5.1f}  {n}" for s, n in sorted(partners, reverse=True)) + "\n", "mono"))
    return out


def fill_text(widget, parts):
    widget.config(state="normal")
    widget.delete("1.0", "end")
    for text, tag in parts:
        widget.insert("end", text, tag)
    widget.config(state="disabled")


def make_text(master, height=10, width=40):
    t = tk.Text(master, height=height, width=width, wrap="word", state="disabled", relief="flat",
                background="#fcfcfb", padx=6, pady=4, font=("Segoe UI", 9))
    t.tag_configure("h", font=("Segoe UI", 12, "bold"))
    t.tag_configure("b", font=("Segoe UI", 9, "bold"))
    t.tag_configure("dim", foreground="#6b6a66")
    t.tag_configure("mono", font=("Consolas", 9))
    t.tag_configure("n")
    return t


# ----------------------------------------------------------------------------
# Widgets
# ----------------------------------------------------------------------------
class SearchCombo(ttk.Combobox):
    """Combobox that narrows its drop-down list while you type."""

    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self._all = []
        self.bind("<KeyRelease>", self._filter)

    def set_values(self, values):
        self._all = list(values)
        self["values"] = self._all

    def _filter(self, e):
        if e.keysym in ("Up", "Down", "Return", "Escape", "Tab", "Left", "Right", "Shift_L", "Shift_R"):
            return
        t = self.get().strip().lower()
        self["values"] = [v for v in self._all if t in v.lower()] if t else self._all


class ZoomView(ttk.Frame):
    """Scrollable / zoomable image viewer. Wheel = scroll, Ctrl+wheel = zoom, drag = pan."""
    MAX_PIXELS = 25e6

    def __init__(self, master, mode="fit", export_name="flavorlab.png", on_export=None):
        super().__init__(master)
        self.mode0, self.auto = mode, None
        self.src, self.z, self.photo = None, 1.0, None
        self.export_name = export_name
        self._after = None
        bar_ = ttk.Frame(self)
        bar_.pack(fill="x", pady=(0, 3))
        ttk.Button(bar_, text="−", width=3, command=lambda: self.zoom_by(1 / 1.25)).pack(side="left")
        self.lbl = ttk.Label(bar_, text="—", width=7, anchor="center")
        self.lbl.pack(side="left")
        ttk.Button(bar_, text="+", width=3, command=lambda: self.zoom_by(1.25)).pack(side="left")
        ttk.Button(bar_, text="Fit", width=5, command=lambda: self.set_auto("fit")).pack(side="left", padx=(8, 0))
        ttk.Button(bar_, text="Width", width=6, command=lambda: self.set_auto("width")).pack(side="left")
        ttk.Button(bar_, text="100%", width=6, command=lambda: self.set_zoom(1.0)).pack(side="left")
        ttk.Button(bar_, text="Export PNG…", command=self.export).pack(side="right")
        body = ttk.Frame(self)
        body.pack(fill="both", expand=True)
        self.cv = tk.Canvas(body, background="#f0efec", highlightthickness=0)
        vs = ttk.Scrollbar(body, orient="vertical", command=self.cv.yview)
        hs = ttk.Scrollbar(body, orient="horizontal", command=self.cv.xview)
        self.cv.configure(yscrollcommand=vs.set, xscrollcommand=hs.set)
        self.cv.grid(row=0, column=0, sticky="nsew")
        vs.grid(row=0, column=1, sticky="ns")
        hs.grid(row=1, column=0, sticky="ew")
        body.rowconfigure(0, weight=1)
        body.columnconfigure(0, weight=1)
        self.cv.bind("<MouseWheel>", lambda e: self.cv.yview_scroll(-1 if e.delta > 0 else 1, "units"))
        self.cv.bind("<Shift-MouseWheel>", lambda e: self.cv.xview_scroll(-1 if e.delta > 0 else 1, "units"))
        self.cv.bind("<Control-MouseWheel>", lambda e: self.zoom_by(1.15 if e.delta > 0 else 1 / 1.15))
        self.cv.bind("<ButtonPress-1>", lambda e: self.cv.scan_mark(e.x, e.y))
        self.cv.bind("<B1-Motion>", lambda e: self.cv.scan_dragto(e.x, e.y, gain=1))
        self.cv.bind("<Configure>", lambda e: self._refit_later() if self.auto else None)
        self._placeholder()

    def _placeholder(self):
        self.cv.delete("all")
        self.cv.create_text(20, 20, anchor="nw", fill="#898781", font=("Segoe UI", 11),
                            text="Nothing rendered yet.")

    def set_image(self, path, name=None):
        self.src = Image.open(path).convert("RGB")
        if name:
            self.export_name = name
        self.set_auto(self.mode0)

    def clear(self):
        self.src = None
        self.lbl.config(text="—")
        self._placeholder()

    @property
    def max_zoom(self):
        return min(4.0, (self.MAX_PIXELS / (self.src.width * self.src.height)) ** 0.5) if self.src else 1.0

    def set_auto(self, mode):
        self.auto = mode
        self._refit_later()

    def _refit_later(self):
        if self._after:
            self.after_cancel(self._after)
        self._after = self.after(120, self._refit)

    def _refit(self):
        self._after = None
        if not self.src or self.cv.winfo_width() < 50:
            return
        cw, ch = self.cv.winfo_width() - 4, self.cv.winfo_height() - 4
        z = cw / self.src.width if self.auto == "width" else min(cw / self.src.width, ch / self.src.height)
        self._render(min(z, 1.0))

    def set_zoom(self, z):
        self.auto = None
        self._render(z)

    def zoom_by(self, f):
        if self.src:
            self.auto = None
            fx, fy = self.cv.xview()[0], self.cv.yview()[0]
            self._render(self.z * f)
            self.cv.xview_moveto(fx)
            self.cv.yview_moveto(fy)

    def _render(self, z):
        if not self.src:
            return
        self.z = max(0.05, min(z, self.max_zoom))
        w, h = max(1, int(self.src.width * self.z)), max(1, int(self.src.height * self.z))
        method = Image.Resampling.LANCZOS if self.z < 1 else Image.Resampling.BILINEAR
        img = self.src if (w, h) == self.src.size else self.src.resize((w, h), method)
        self.photo = ImageTk.PhotoImage(img, master=self.cv)
        self.cv.delete("all")
        self.cv.create_image(0, 0, anchor="nw", image=self.photo)
        self.cv.configure(scrollregion=(0, 0, w, h))
        self.lbl.config(text=f"{self.z * 100:.0f}%")

    def export(self):
        if not self.src:
            messagebox.showinfo("Export PNG", "Nothing to export yet - render something first.")
            return
        os.makedirs(OUT_DIR, exist_ok=True)
        p = filedialog.asksaveasfilename(parent=self, defaultextension=".png", initialdir=OUT_DIR,
                                         initialfile=self.export_name, filetypes=[("PNG image", "*.png")])
        if p:
            self.src.save(p)
            app = self.winfo_toplevel().app
            app.status(f"Exported {p}")


# ----------------------------------------------------------------------------
# Tab: Recipe Designer
# ----------------------------------------------------------------------------
class Designer(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.rows = []              # [{item, g, prep:[...], stage:'main'|'finish'}]
        self.undo_stack = []
        self.dirty = False
        self.version = 0            # bumps on every mutation (guards background results)
        self.sugg, self.sugg_version = [], -1
        self.A = None
        self._recalc_job = None
        self._build()

    # ---- layout -----------------------------------------------------------
    def _build(self):
        pw = ttk.PanedWindow(self, orient="horizontal")
        pw.pack(fill="both", expand=True)
        left, center, right = ttk.Frame(pw), ttk.Frame(pw), ttk.Frame(pw)
        pw.add(left, weight=2)
        pw.add(center, weight=4)
        pw.add(right, weight=3)

        # left: ingredient picker + detail
        top = ttk.Frame(left)
        top.pack(fill="x", padx=4, pady=4)
        self.q = tk.StringVar()
        self.q.trace_add("write", lambda *_: self.refresh_ingredients())
        ttk.Label(top, text="Ingredients").grid(row=0, column=0, sticky="w")
        self.count_lbl = ttk.Label(top, text="", foreground="#6b6a66")
        self.count_lbl.grid(row=0, column=1, sticky="e")
        ttk.Entry(top, textvariable=self.q).grid(row=1, column=0, columnspan=2, sticky="ew", pady=2)
        self.cat = tk.StringVar(value="all categories")
        cb = ttk.Combobox(top, textvariable=self.cat, state="readonly",
                          values=["all categories"] + [f"{c} - {M.CAT_LABEL[c]}" for c in M.CATEGORIES])
        cb.grid(row=2, column=0, columnspan=2, sticky="ew")
        cb.bind("<<ComboboxSelected>>", lambda e: self.refresh_ingredients())
        top.columnconfigure(0, weight=1)
        lf = ttk.Frame(left)
        lf.pack(fill="both", expand=True, padx=4)
        self.ilist = ttk.Treeview(lf, columns=("name", "cat", "pack"), show="headings", selectmode="browse", height=12)
        for c, w, t in (("name", 150, "name"), ("cat", 55, "cat"), ("pack", 90, "pack")):
            self.ilist.heading(c, text=t)
            self.ilist.column(c, width=w, anchor="w")
        sb = ttk.Scrollbar(lf, orient="vertical", command=self.ilist.yview)
        self.ilist.configure(yscrollcommand=sb.set)
        self.ilist.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")
        self.ilist.bind("<<TreeviewSelect>>", lambda e: self.show_detail())
        self.ilist.bind("<Double-1>", lambda e: self.add_selected())
        self.ilist.bind("<Return>", lambda e: self.add_selected())
        ttk.Button(left, text="Add to recipe  ➜", command=self.add_selected).pack(fill="x", padx=4, pady=3)
        self.detail = make_text(left, height=16)
        self.detail.pack(fill="both", expand=True, padx=4, pady=(0, 4))

        # center: recipe header, table, actions, suggestions
        hdr = ttk.Frame(center)
        hdr.pack(fill="x", padx=4, pady=4)
        ttk.Label(hdr, text="Name").grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar(value="New sauce")
        e = ttk.Entry(hdr, textvariable=self.name_var)
        e.grid(row=0, column=1, columnspan=3, sticky="ew", padx=4)
        e.bind("<KeyRelease>", lambda ev: self._mark_dirty())
        ttk.Label(hdr, text="Style").grid(row=1, column=0, sticky="w")
        self.style_var = tk.StringVar()
        self.style_cb = ttk.Combobox(hdr, textvariable=self.style_var, state="readonly",
                                     values=[f"{k} — {v['label']}" for k, v in M.STYLES.items()])
        self.style_cb.grid(row=1, column=1, sticky="ew", padx=4, pady=2)
        self.style_cb.bind("<<ComboboxSelected>>", lambda ev: self._meta_changed())
        ttk.Label(hdr, text="Process").grid(row=1, column=2, sticky="e")
        self.proc_var = tk.StringVar(value="cooked")
        pc = ttk.Combobox(hdr, textvariable=self.proc_var, state="readonly", width=8, values=list(M.VOL_KEEP))
        pc.grid(row=1, column=3, sticky="e", padx=4)
        pc.bind("<<ComboboxSelected>>", lambda ev: self._meta_changed())
        hdr.columnconfigure(1, weight=1)
        self.style_var.set(self._style_label("balanced"))

        bt = ttk.Frame(center)
        bt.pack(fill="x", padx=4)
        for text, cmd in (("New", self.new), ("Load…", self.load), ("Save…", self.save),
                          ("Undo", self.undo), ("Remove row", self.remove_selected),
                          ("Ferment all fermentable", self.ferment_all)):
            ttk.Button(bt, text=text, command=cmd).pack(side="left", padx=(0, 3))

        tf = ttk.Frame(center)
        tf.pack(fill="both", expand=True, padx=4, pady=4)
        self.tree = ttk.Treeview(tf, columns=("item", "g", "pct", "prep"), show="headings", selectmode="browse", height=9)
        for c, w, t, a in (("item", 170, "ingredient", "w"), ("g", 60, "grams", "e"), ("pct", 55, "%", "e"),
                           ("prep", 150, "prep  (click to edit)", "w")):
            self.tree.heading(c, text=t)
            self.tree.column(c, width=w, anchor=a)
        self.tree.tag_configure("bad", foreground="#c0392b")
        sb2 = ttk.Scrollbar(tf, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb2.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb2.pack(side="right", fill="y")
        self.tree.bind("<Double-1>", self._on_double)
        self.tree.bind("<ButtonRelease-1>", self._on_click)
        self.tree.bind("<Delete>", lambda e: self.remove_selected())
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.show_detail(from_recipe=True))
        self.tree.bind("<Control-z>", lambda e: self.undo())
        ttk.Label(center, text="Double-click grams to edit · click prep to set roasted/smoked/… · Del removes a row",
                  foreground="#6b6a66").pack(anchor="w", padx=4)

        sg = ttk.LabelFrame(center, text="Suggestions")
        sg.pack(fill="both", expand=True, padx=4, pady=4)
        sbar = ttk.Frame(sg)
        sbar.pack(fill="x", padx=4, pady=3)
        ttk.Button(sbar, text="Suggest", command=self.suggest).pack(side="left")
        ttk.Button(sbar, text="Auto-optimize", command=self.auto_optimize).pack(side="left", padx=(8, 3))
        self.steps = tk.IntVar(value=3)
        ttk.Spinbox(sbar, from_=1, to=10, width=3, textvariable=self.steps).pack(side="left")
        ttk.Label(sbar, text="steps").pack(side="left", padx=3)
        self.sugg_title = tk.StringVar(value="double-click a suggestion to apply it")
        ttk.Label(sbar, textvariable=self.sugg_title, foreground="#6b6a66").pack(side="left", padx=8)
        sf = ttk.Frame(sg)
        sf.pack(fill="both", expand=True, padx=4, pady=(0, 4))
        self.stree = ttk.Treeview(sf, columns=("move", "gain", "fit", "harm"), show="headings", height=6)
        for c, w, t, a in (("move", 230, "move", "w"), ("gain", 55, "overall", "e"), ("fit", 50, "fit", "e"),
                           ("harm", 60, "harmony", "e")):
            self.stree.heading(c, text=t)
            self.stree.column(c, width=w, anchor=a)
        ss = ttk.Scrollbar(sf, orient="vertical", command=self.stree.yview)
        self.stree.configure(yscrollcommand=ss.set)
        self.stree.pack(side="left", fill="both", expand=True)
        ss.pack(side="right", fill="y")
        self.stree.bind("<Double-1>", self.apply_suggestion)

        # right: live scores
        sc = ttk.LabelFrame(right, text="Live analysis")
        sc.pack(fill="x", padx=4, pady=4)
        self.sv = {k: tk.StringVar(value="—") for k in ("overall", "fit", "harmony", "shu", "heat", "body", "total", "salt")}
        big = ttk.Label(sc, textvariable=self.sv["overall"], font=("Segoe UI", 26, "bold"), foreground="#2a78d6")
        big.grid(row=0, column=0, rowspan=2, padx=10, pady=4)
        ttk.Label(sc, text="overall score", foreground="#6b6a66").grid(row=2, column=0)
        r = 0
        for key, label in (("fit", "style fit"), ("harmony", "harmony"), ("shu", "est. SHU"), ("heat", "heat (0-10)"),
                           ("body", "body"), ("total", "batch"), ("salt", "salt %")):
            ttk.Label(sc, text=label, foreground="#6b6a66").grid(row=r % 4, column=1 + 2 * (r // 4), sticky="w", padx=(12, 4))
            ttk.Label(sc, textvariable=self.sv[key]).grid(row=r % 4, column=2 + 2 * (r // 4), sticky="w")
            r += 1
        self.fig = Figure(figsize=(4.6, 3.9), layout="constrained")
        self.canvas = FigureCanvasTkAgg(self.fig, master=right)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=4)
        self.warn = make_text(right, height=8)
        self.warn.pack(fill="x", padx=4, pady=4)
        ttk.Button(right, text="Render full sauce card  ➜", command=self.app.render_card).pack(fill="x", padx=4, pady=(0, 4))

    # ---- state helpers ----------------------------------------------------
    @staticmethod
    def _style_label(key):
        return f"{key} — {M.STYLES[key]['label']}"

    @property
    def style(self):
        return self.style_var.get().split(" — ")[0] or "balanced"

    def meta(self):
        return {"name": self.name_var.get().strip() or "sauce", "style": self.style,
                "process": self.proc_var.get(), "fermented": False, "notes": ""}

    def recipe(self):
        return dict(self.meta(), ingredients=copy.deepcopy(self.rows))

    def _mark_dirty(self):
        self.dirty = True

    def _snapshot(self):
        return (copy.deepcopy(self.rows), self.style, self.proc_var.get())

    def push_undo(self):
        self.undo_stack.append(self._snapshot())
        del self.undo_stack[:-60]

    def mutate(self):
        self.push_undo()
        self.dirty = True
        self.version += 1

    def undo(self):
        if not self.undo_stack:
            self.app.status("Nothing to undo.")
            return
        rows, style, proc = self.undo_stack.pop()
        self.rows = rows
        self.style_var.set(self._style_label(style))
        self.proc_var.set(proc)
        self.version += 1
        self.dirty = True
        self.clear_suggestions()
        self.refresh_table()
        self.app.status("Undone.")

    def _meta_changed(self):
        self.dirty = True
        self.version += 1
        self.clear_suggestions()
        self.schedule_recalc()

    def confirm_discard(self):
        return (not self.dirty) or messagebox.askyesno("Unsaved changes", "Discard the current recipe's unsaved changes?")

    # ---- ingredient list (left) ------------------------------------------
    def refresh_ingredients(self):
        db = self.app.db
        t = self.q.get().strip().lower()
        c = self.cat.get().split(" - ")[0]
        sel = self.ilist.selection()
        keep = self.ilist.item(sel[0], "values")[0] if sel else None
        self.ilist.delete(*self.ilist.get_children())
        n = 0
        for name in sorted(db.items):
            ing = db.items[name]
            if c in M.CATEGORIES and ing.category != c:
                continue
            if t and t not in name.lower() and not any(t in a.lower() for a in ing.aliases):
                continue
            iid = self.ilist.insert("", "end", iid=name, values=(name, ing.category, self.app.packs.get(name, "")))
            n += 1
            if name == keep:
                self.ilist.selection_set(iid)
        self.count_lbl.config(text=f"{n} of {len(db.items)}")

    def selected_ingredient(self):
        sel = self.ilist.selection()
        return sel[0] if sel else None

    def show_detail(self, from_recipe=False):
        name = None
        if from_recipe:
            sel = self.tree.selection()
            if sel:
                name = self.rows[int(sel[0])]["item"]
        else:
            name = self.selected_ingredient()
        if not name:
            return
        try:
            fill_text(self.detail, ingredient_report(self.app.db, self.app.packs, name, [r["item"] for r in self.rows]))
        except KeyError:
            fill_text(self.detail, [(f"{name}\n", "h"), ("not in the ingredient database (renamed or removed?)", "dim")])

    # ---- recipe table (center) -------------------------------------------
    def default_grams(self, ing):
        total = sum(r["g"] for r in self.rows)
        return 50.0 if total <= 0 else float(M.nice_grams(max(1.0, total * 0.06 / ing.potency)))

    def add_ingredient(self, name, g=None):
        ing = self.app.db.get(name)
        self.mutate()
        self.rows.append({"item": ing.name, "g": float(g if g is not None else self.default_grams(ing)),
                          "prep": [], "stage": "main"})
        self.clear_suggestions()
        self.refresh_table(select=len(self.rows) - 1)
        self.app.status(f"Added {ing.name}.")

    def add_selected(self):
        n = self.selected_ingredient()
        if n:
            self.add_ingredient(n)

    def remove_selected(self):
        sel = self.tree.selection()
        if not sel:
            return
        i = int(sel[0])
        self.mutate()
        gone = self.rows.pop(i)
        self.clear_suggestions()
        self.refresh_table(select=min(i, len(self.rows) - 1) if self.rows else None)
        self.app.status(f"Removed {gone['item']}.")

    def ferment_all(self):
        db = self.app.db
        todo = []
        for r in self.rows:
            try:
                if db.get(r["item"]).category in M.FERMENTABLE and "fermented" not in r["prep"]:
                    todo.append(r)
            except KeyError:
                pass
        if not todo:
            self.app.status("No (more) fermentable chili / fruit / veg / herb rows.")
            return
        self.mutate()
        for r in todo:
            r["prep"].append("fermented")
        self.clear_suggestions()
        self.refresh_table()
        self.app.status(f"Fermenting {len(todo)} ingredient(s). Remember: ferments need 2-3% salt.")

    @staticmethod
    def prep_text(r):
        s = "+".join(r["prep"])
        if r.get("stage") == "finish":
            s = (s + " · " if s else "") + "finish"
        return s

    def refresh_table(self, select=None):
        db = self.app.db
        total = sum(r["g"] for r in self.rows) or 1.0
        self.tree.delete(*self.tree.get_children())
        for i, r in enumerate(self.rows):
            try:
                db.get(r["item"])
                tags = ()
            except KeyError:
                tags = ("bad",)
            self.tree.insert("", "end", iid=str(i), tags=tags,
                             values=(r["item"] + ("  (missing!)" if tags else ""), f"{r['g']:g}",
                                     f"{100 * r['g'] / total:.1f}", self.prep_text(r)))
        if select is not None and 0 <= select < len(self.rows):
            self.tree.selection_set(str(select))
        self.schedule_recalc()

    def _cell(self, event):
        if self.tree.identify_region(event.x, event.y) != "cell":
            return None, None
        return self.tree.identify_row(event.y), self.tree.identify_column(event.x)

    def _on_double(self, event):
        iid, col = self._cell(event)
        if iid and col == "#2":
            self.edit_grams(iid)

    def _on_click(self, event):
        iid, col = self._cell(event)
        if iid and col == "#4":
            self.open_prep_popup(int(iid), event.x_root, event.y_root)

    def edit_grams(self, iid):
        bb = self.tree.bbox(iid, "#2")
        if not bb:
            return
        x, y, w, h = bb
        i = int(iid)
        e = ttk.Entry(self.tree, justify="right")
        e.place(x=x, y=y, width=w, height=h)
        e.insert(0, f"{self.rows[i]['g']:g}")
        e.select_range(0, "end")
        e.focus_set()
        state = {"done": False}

        def finish(commit):
            if state["done"]:
                return
            state["done"] = True
            txt = e.get().replace(",", ".").strip()
            e.destroy()
            if not commit:
                return
            try:
                v = float(txt)
                if v < 0:
                    raise ValueError
            except ValueError:
                self.app.status(f"'{txt}' is not a valid number of grams.")
                return
            if v != self.rows[i]["g"]:
                self.mutate()
                self.rows[i]["g"] = v
                self.clear_suggestions()
                self.refresh_table(select=i)

        e.bind("<Return>", lambda ev: finish(True))
        e.bind("<FocusOut>", lambda ev: finish(True))
        e.bind("<Escape>", lambda ev: finish(False))

    def open_prep_popup(self, i, x, y):
        if i >= len(self.rows):
            return
        r = self.rows[i]
        top = tk.Toplevel(self)
        top.title(f"Prep - {r['item']}")
        top.transient(self.winfo_toplevel())
        top.geometry(f"+{x}+{y}")
        top.resizable(False, False)
        vars_ = {p: tk.BooleanVar(value=p in r["prep"]) for p in PREPS}
        fin = tk.BooleanVar(value=r.get("stage") == "finish")
        ttk.Label(top, text=r["item"], font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=10, pady=(8, 2))
        for p in PREPS:
            ttk.Checkbutton(top, text=p, variable=vars_[p]).pack(anchor="w", padx=14)
        ttk.Separator(top).pack(fill="x", pady=4, padx=8)
        ttk.Checkbutton(top, text="finish (added after cooking)", variable=fin).pack(anchor="w", padx=14)

        def ok():
            new_prep = [p for p in PREPS if vars_[p].get()]
            new_stage = "finish" if fin.get() else "main"
            top.destroy()
            if new_prep != r["prep"] or new_stage != r.get("stage"):
                self.mutate()
                r["prep"], r["stage"] = new_prep, new_stage
                self.clear_suggestions()
                self.refresh_table(select=i)

        bb = ttk.Frame(top)
        bb.pack(fill="x", padx=8, pady=8)
        ttk.Button(bb, text="OK", command=ok).pack(side="right")
        ttk.Button(bb, text="Cancel", command=top.destroy).pack(side="right", padx=4)
        top.bind("<Return>", lambda e: ok())
        top.bind("<Escape>", lambda e: top.destroy())
        top.grab_set()

    # ---- new / load / save ------------------------------------------------
    def set_recipe(self, r):
        self.rows = copy.deepcopy(r["ingredients"])
        self.name_var.set(r["name"])
        style = r["style"] if r["style"] in M.STYLES else "balanced"
        self.style_var.set(self._style_label(style))
        self.proc_var.set(r["process"] if r["process"] in M.VOL_KEEP else "cooked")
        self.undo_stack.clear()
        self.dirty = False
        self.version += 1
        self.clear_suggestions()
        self.refresh_table()

    def new(self):
        if self.confirm_discard():
            self.set_recipe({"name": "New sauce", "style": "balanced", "process": "cooked", "ingredients": []})

    def load(self):
        if not self.confirm_discard():
            return
        os.makedirs(RECIPES_DIR, exist_ok=True)
        p = filedialog.askopenfilename(parent=self, initialdir=RECIPES_DIR, filetypes=[("Recipe JSON", "*.json")])
        if p:
            self.load_path(p)

    def load_path(self, p):
        try:
            r = read_recipe_file(p, self.app.db)
        except Exception as e:                       # noqa: BLE001
            messagebox.showerror("Load recipe", f"Could not read {p}:\n{e}")
            return
        self.set_recipe(r)
        self.app.status(f"Loaded {p}")

    def save(self):
        os.makedirs(RECIPES_DIR, exist_ok=True)
        p = filedialog.asksaveasfilename(parent=self, initialdir=RECIPES_DIR, defaultextension=".json",
                                         initialfile=fl.slug(self.name_var.get() or "sauce") + ".json",
                                         filetypes=[("Recipe JSON", "*.json")])
        if not p:
            return
        write_recipe_file(p, self.recipe())
        self.dirty = False
        self.app.status(f"Saved {p}")

    # ---- analysis ---------------------------------------------------------
    def analysis_recipe(self):
        """-> (recipe with only analysable rows, [problem strings])."""
        db, ok, problems = self.app.db, [], []
        for r in self.rows:
            try:
                db.get(r["item"])
            except KeyError:
                problems.append(f"'{r['item']}' is not in the ingredient database - excluded")
                continue
            if r["g"] <= 0:
                problems.append(f"{r['item']} has 0 g - excluded")
                continue
            ok.append(copy.deepcopy(r))
        return dict(self.meta(), ingredients=ok), problems

    def schedule_recalc(self):
        if self._recalc_job:
            self.after_cancel(self._recalc_job)
        self._recalc_job = self.after(150, self.recalc)

    def recalc(self):
        self._recalc_job = None
        rec, problems = self.analysis_recipe()
        if not rec["ingredients"]:
            self.A = None
            for v in self.sv.values():
                v.set("—")
            self.fig.clear()
            self.canvas.draw_idle()
            fill_text(self.warn, [("Add ingredients from the list on the left.\n" + "\n".join(problems), "dim")])
            return
        try:
            A = M.analyze(self.app.db, rec)
        except Exception as e:                       # noqa: BLE001
            self.A = None
            fill_text(self.warn, [(f"Analysis error: {e}", "n")])
            return
        self.A = A
        self.sv["overall"].set(f"{A['overall']:.0f}")
        self.sv["fit"].set(f"{A['fit']:.0f}")
        self.sv["harmony"].set(f"{A['harmony']:.0f}")
        self.sv["shu"].set(f"{A['shu']:,.0f}")
        self.sv["heat"].set(f"{A['perceived']['heat']:.1f}")
        self.sv["body"].set(f"{M.body_class(A['body'])[0]} ({A['body']:.1f})")
        self.sv["total"].set(f"{A['total_g']:g} g")
        self.sv["salt"].set(f"{A['salt_pct']:.1f}")
        self.fig.clear()
        ax = self.fig.add_subplot(111)
        fl.gap_chart(ax, A)
        ax.set_title(ax.get_title(), fontsize=9)
        self.canvas.draw_idle()
        parts = [("⚠ " + p + "\n", "n") for p in problems] + [("• " + w + "\n", "n") for w in A["warnings"]]
        parts += [("ℹ " + note["text"] + "\n", "dim") for note in A["science_notes"]]
        fill_text(self.warn, parts)
        sel = self.tree.selection()
        if sel or self.selected_ingredient():
            self.show_detail(from_recipe=bool(sel))

    # ---- suggestions ------------------------------------------------------
    def clear_suggestions(self):
        self.sugg, self.sugg_version = [], -1
        self.stree.delete(*self.stree.get_children())
        self.sugg_title.set("double-click a suggestion to apply it")

    def _check_ready(self):
        rec, problems = self.analysis_recipe()
        if problems:
            messagebox.showwarning("Fix the recipe first", "\n".join(problems))
            return None
        if not rec["ingredients"]:
            self.app.status("Add ingredients first.")
            return None
        return rec

    def suggest(self):
        rec = self._check_ready()
        if rec is None:
            return
        db, ver = self.app.db, self.version

        def job():
            return M.suggest(db, rec)

        def done(moves):
            if ver != self.version:
                self.app.status("Recipe changed while computing - press Suggest again.")
                return
            self.sugg, self.sugg_version = moves, ver
            self.stree.delete(*self.stree.get_children())
            for k, m in enumerate(moves):
                self.stree.insert("", "end", iid=str(k), values=(m["move"], f"+{m['d_overall']:.1f}",
                                                                   f"{m['d_fit']:+.1f}", f"{m['d_harmony']:+.1f}"))
            self.sugg_title.set("double-click a suggestion to apply it" if moves
                                else "no single change improves the score (local optimum)")
            self.app.status(f"{len(moves)} suggestions.")

        self.app.bg(job, done, "Computing suggestions…")

    def apply_suggestion(self, event):
        iid = self.stree.identify_row(event.y)
        if iid and iid.isdigit():
            self.apply_suggestion_at(int(iid))

    def apply_suggestion_at(self, k):
        if k >= len(self.sugg) or self.sugg_version != self.version:
            return
        m = self.sugg[k]
        self.mutate()
        self.rows = copy.deepcopy(m["_items"])
        self.clear_suggestions()
        self.refresh_table()
        self.app.status(f"Applied: {m['move']}   (Undo to revert)")

    def auto_optimize(self):
        rec = self._check_ready()
        if rec is None:
            return
        db, ver, steps = self.app.db, self.version, int(self.steps.get() or 3)

        def job():
            return M.optimize(db, rec, steps=steps)

        def done(res):
            new, log = res
            if ver != self.version:
                self.app.status("Recipe changed while optimizing - press Auto-optimize again.")
                return
            if not log:
                self.app.status("Auto-optimize: no improving move found.")
                return
            self.mutate()
            self.rows = copy.deepcopy(new["ingredients"])
            self.clear_suggestions()
            self.refresh_table()
            for k, m in enumerate(log):
                self.stree.insert("", "end", iid=f"a{k}", values=("✔ " + m["move"], f"+{m['d_overall']:.1f}",
                                                                   f"{m['d_fit']:+.1f}", f"{m['d_harmony']:+.1f}"))
            self.sugg_title.set(f"applied {len(log)} step(s) - Undo reverts them all")
            self.app.status(f"Auto-optimize applied {len(log)} step(s).")

        self.app.bg(job, done, f"Optimizing ({steps} steps)…")


# ----------------------------------------------------------------------------
# Tab: Sauce Card
# ----------------------------------------------------------------------------
class CardTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        bar_ = ttk.Frame(self)
        bar_.pack(fill="x", padx=4, pady=4)
        ttk.Button(bar_, text="Render card from designer recipe", command=app.render_card).pack(side="left")
        self.moves = tk.BooleanVar(value=True)
        ttk.Checkbutton(bar_, text="include 'next best moves' (slower)", variable=self.moves).pack(side="left", padx=10)
        self.view = ZoomView(self, mode="width", export_name="sauce_card.png")
        self.view.pack(fill="both", expand=True, padx=4, pady=4)


# ----------------------------------------------------------------------------
# Tab: Pairing & Bridge
# ----------------------------------------------------------------------------
class PairTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        left = ttk.Frame(self, width=340)
        left.pack(side="left", fill="y", padx=6, pady=6)
        ttk.Label(left, text="Ingredient").pack(anchor="w")
        self.a = SearchCombo(left)
        self.a.pack(fill="x")
        ttk.Label(left, text="…and (optional) a second one to compare / bridge").pack(anchor="w", pady=(8, 0))
        self.b = SearchCombo(left)
        self.b.pack(fill="x")
        row = ttk.Frame(left)
        row.pack(fill="x", pady=8)
        ttk.Label(row, text="Partners shown").pack(side="left")
        self.top = tk.IntVar(value=18)
        ttk.Spinbox(row, from_=6, to=40, width=4, textvariable=self.top).pack(side="left", padx=6)
        ttk.Button(left, text="Show pairing wheel", command=self.go).pack(fill="x")
        self.out = make_text(left, height=24, width=42)
        self.out.pack(fill="both", expand=True, pady=8)
        self.view = ZoomView(self, mode="fit", export_name="pairing.png")
        self.view.pack(side="left", fill="both", expand=True, padx=6, pady=6)

    def refresh_ingredients(self):
        names = sorted(self.app.db.items)
        self.a.set_values(names)
        self.b.set_values(names)

    def go(self):
        a, b, top = self.a.get().strip(), self.b.get().strip(), int(self.top.get() or 18)
        if not a:
            self.app.status("Pick an ingredient first.")
            return
        db, path = self.app.db, self.app.tmp_png("pair")

        def job():
            with RENDER_LOCK:
                _, best = fl.pair_wheel(db, a, top, path)
            res = {"best": best, "a": db.get(a).name}
            if b:
                A, B = db.get(a), db.get(b)
                res.update(b=B.name, explain=M.pair_score(db, A, B, explain=True),
                           bridges=M.bridges(db, A, B, top=10))
            return res

        def done(res):
            self.view.set_image(path, f"pair_{fl.slug(res['a'])}.png")
            parts = [(f"Best partners for {res['a']}\n", "b"),
                     ("\n".join(f"{s:5.1f}  {n}" for n, s in res["best"]) + "\n", "mono")]
            if "explain" in res:
                e = res["explain"]
                parts += [(f"\n{res['a']} + {res['b']}: {e['score']}" + ("  ★ classic" if e["classic"] else "") + "\n", "b"),
                          (f"shared aroma: {', '.join(e['shared_families']) or 'none'}\n"
                           f"aroma similarity {e['aroma_similarity']} · profile {e['profile_similarity']}\n"
                           f"taste contrast {e['taste_contrast']} · category affinity {e['category_affinity']} · "
                           f"clash {e['clash']}\n", "n"),
                          (f"\nBridges linking them:\n", "b"),
                          ("\n".join(f"{s:5.1f}  {n}" for n, s in res["bridges"]) + "\n", "mono")]
            fill_text(self.out, parts)
            self.app.status("Pairing wheel ready.")

        self.app.bg(job, done, "Rendering pairing wheel…")


# ----------------------------------------------------------------------------
# Tab: Flavor Map
# ----------------------------------------------------------------------------
class MapTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        left = ttk.Frame(self, width=300)
        left.pack(side="left", fill="y", padx=6, pady=6)
        ttk.Label(left, text="Categories").pack(anchor="w")
        self.cats = {c: tk.BooleanVar(value=True) for c in M.CATEGORIES}
        for c in M.CATEGORIES:
            ttk.Checkbutton(left, text=M.CAT_LABEL[c], variable=self.cats[c]).pack(anchor="w")
        ttk.Label(left, text="Highlight ingredients").pack(anchor="w", pady=(10, 0))
        self.pick = SearchCombo(left)
        self.pick.pack(fill="x")
        self.pick.bind("<Return>", lambda e: self.add_hl())
        rr = ttk.Frame(left)
        rr.pack(fill="x", pady=3)
        ttk.Button(rr, text="Add", command=self.add_hl).pack(side="left")
        ttk.Button(rr, text="Remove", command=self.rm_hl).pack(side="left", padx=4)
        ttk.Button(rr, text="From recipe", command=self.from_recipe).pack(side="left")
        self.hl = tk.Listbox(left, height=8)
        self.hl.pack(fill="x")
        ttk.Button(left, text="Draw flavor map", command=self.go).pack(fill="x", pady=10)
        self.view = ZoomView(self, mode="fit", export_name="flavor_map.png")
        self.view.pack(side="left", fill="both", expand=True, padx=6, pady=6)

    def refresh_ingredients(self):
        self.pick.set_values(sorted(self.app.db.items))

    def add_hl(self):
        n = self.pick.get().strip()
        if not n:
            return
        try:
            n = self.app.db.get(n).name
        except KeyError as e:
            self.app.status(e.args[0])
            return
        if n not in self.hl.get(0, "end"):
            self.hl.insert("end", n)

    def rm_hl(self):
        for i in reversed(self.hl.curselection()):
            self.hl.delete(i)

    def from_recipe(self):
        for r in self.app.designer.rows:
            if r["item"] not in self.hl.get(0, "end"):
                self.hl.insert("end", r["item"])

    def go(self):
        cats = [c for c, v in self.cats.items() if v.get()]
        if not cats:
            self.app.status("Select at least one category.")
            return
        hl, db, path = list(self.hl.get(0, "end")), self.app.db, self.app.tmp_png("map")

        def job():
            with RENDER_LOCK:
                fl.flavor_map(db, path, hl, None if len(cats) == len(M.CATEGORIES) else cats)
            return path

        self.app.bg(job, lambda p: (self.view.set_image(p), self.app.status("Flavor map ready.")),
                    "Drawing flavor map…")


# ----------------------------------------------------------------------------
# Tab: Compare
# ----------------------------------------------------------------------------
class CompareTab(ttk.Frame):
    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.paths = []
        left = ttk.Frame(self, width=320)
        left.pack(side="left", fill="y", padx=6, pady=6)
        self.cur = tk.BooleanVar(value=True)
        ttk.Checkbutton(left, text="Include the recipe open in the designer", variable=self.cur).pack(anchor="w")
        ttk.Label(left, text="Saved recipes (pick up to 3 in total)").pack(anchor="w", pady=(10, 0))
        self.lb = tk.Listbox(left, selectmode="extended", height=14, exportselection=False)
        self.lb.pack(fill="both", expand=True)
        rr = ttk.Frame(left)
        rr.pack(fill="x", pady=4)
        ttk.Button(rr, text="Refresh", command=self.refresh_files).pack(side="left")
        ttk.Button(rr, text="Add file…", command=self.add_file).pack(side="left", padx=4)
        ttk.Button(left, text="Compare", command=self.go).pack(fill="x", pady=6)
        self.view = ZoomView(self, mode="fit", export_name="compare.png")
        self.view.pack(side="left", fill="both", expand=True, padx=6, pady=6)
        self.refresh_files()

    def refresh_files(self):
        keep = {self.paths[i] for i in self.lb.curselection()}
        extra = [p for p in self.paths if os.path.dirname(os.path.abspath(p)) != os.path.abspath(RECIPES_DIR)]
        self.paths = sorted(glob.glob(os.path.join(RECIPES_DIR, "*.json"))) + extra
        self.lb.delete(0, "end")
        for p in self.paths:
            self.lb.insert("end", os.path.basename(p))
        for i, p in enumerate(self.paths):
            if p in keep:
                self.lb.selection_set(i)

    def add_file(self):
        p = filedialog.askopenfilename(parent=self, initialdir=RECIPES_DIR, filetypes=[("Recipe JSON", "*.json")])
        if p and p not in self.paths:
            self.paths.append(p)
            self.lb.insert("end", os.path.basename(p))
            self.lb.selection_set("end")

    def go(self):
        chosen = [self.paths[i] for i in self.lb.curselection()]
        n = len(chosen) + (1 if self.cur.get() else 0)
        if n < 1 or n > 3:
            messagebox.showinfo("Compare", "Pick between 1 and 3 recipes (including the designer's, if ticked).")
            return
        db, path = self.app.db, self.app.tmp_png("compare")
        recipes = []
        if self.cur.get():
            rec, problems = self.app.designer.analysis_recipe()
            if not rec["ingredients"]:
                messagebox.showinfo("Compare", "The designer recipe is empty.")
                return
            recipes.append(rec)

        def job():
            rs = recipes + [read_recipe_file(p, db) for p in chosen]
            As = [M.analyze(db, r) for r in rs]
            with RENDER_LOCK:
                fl.compare_fig(db, As, path)
            return path

        self.app.bg(job, lambda p: (self.view.set_image(p), self.app.status("Comparison ready.")), "Comparing…")


# ----------------------------------------------------------------------------
# Tab: Ingredient Browser
# ----------------------------------------------------------------------------
class BrowserTab(ttk.Frame):
    COLS = ["name", "category", "pack", "shu", "sweet", "sour", "salty", "bitter", "umami", "fruity", "citrus",
            "floral", "herbal", "earthy", "smoky", "warm", "pungent", "funky"]

    def __init__(self, master, app):
        super().__init__(master)
        self.app = app
        self.sort = ("name", False)
        top = ttk.Frame(self)
        top.pack(fill="x", padx=6, pady=6)
        ttk.Label(top, text="Filter").pack(side="left")
        self.q = tk.StringVar()
        self.q.trace_add("write", lambda *_: self.refresh_ingredients())
        ttk.Entry(top, textvariable=self.q, width=28).pack(side="left", padx=4)
        self.cat = tk.StringVar(value="all categories")
        cb = ttk.Combobox(top, textvariable=self.cat, state="readonly", width=24,
                          values=["all categories"] + [f"{c} - {M.CAT_LABEL[c]}" for c in M.CATEGORIES])
        cb.pack(side="left")
        cb.bind("<<ComboboxSelected>>", lambda e: self.refresh_ingredients())
        self.cnt = ttk.Label(top, text="", foreground="#6b6a66")
        self.cnt.pack(side="left", padx=10)
        ttk.Button(top, text="Add to recipe ➜", command=self.add).pack(side="right")
        pw = ttk.PanedWindow(self, orient="horizontal")
        pw.pack(fill="both", expand=True, padx=6, pady=(0, 6))
        tf = ttk.Frame(pw)
        pw.add(tf, weight=4)
        self.tree = ttk.Treeview(tf, columns=self.COLS, show="headings", selectmode="browse")
        for c in self.COLS:
            self.tree.heading(c, text=c, command=lambda c=c: self.sort_by(c))
            self.tree.column(c, width=170 if c == "name" else 95 if c in ("category", "pack") else 52,
                             anchor="w" if c in ("name", "category", "pack") else "e")
        vs = ttk.Scrollbar(tf, orient="vertical", command=self.tree.yview)
        hs = ttk.Scrollbar(tf, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vs.set, xscrollcommand=hs.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vs.grid(row=0, column=1, sticky="ns")
        hs.grid(row=1, column=0, sticky="ew")
        tf.rowconfigure(0, weight=1)
        tf.columnconfigure(0, weight=1)
        self.tree.bind("<<TreeviewSelect>>", lambda e: self.detail_show())
        self.tree.bind("<Double-1>", lambda e: self.add())
        self.detail = make_text(pw, height=10, width=44)
        pw.add(self.detail, weight=2)

    def sort_by(self, col):
        self.sort = (col, (not self.sort[1]) if self.sort[0] == col else False)
        self.refresh_ingredients()

    def refresh_ingredients(self):
        db = self.app.db
        t = self.q.get().strip().lower()
        c = self.cat.get().split(" - ")[0]
        data = []
        for name, ing in db.items.items():
            if c in M.CATEGORIES and ing.category != c:
                continue
            if t and t not in name.lower() and not any(t in a.lower() for a in ing.aliases):
                continue
            vals = [name, ing.category, self.app.packs.get(name, ""), ing.shu]
            vals += [float(ing.vec[M.VI[d]]) for d in self.COLS[4:]]
            data.append(vals)
        k = self.COLS.index(self.sort[0])
        data.sort(key=lambda r: (r[k] if not isinstance(r[k], str) else r[k].lower()), reverse=self.sort[1])
        sel = self.tree.selection()
        self.tree.delete(*self.tree.get_children())
        for r in data:
            self.tree.insert("", "end", iid=r[0], values=[f"{v:g}" if isinstance(v, float) else v for v in r])
        if sel and self.tree.exists(sel[0]):
            self.tree.selection_set(sel[0])
        self.cnt.config(text=f"{len(data)} of {len(db.items)}")

    def detail_show(self):
        sel = self.tree.selection()
        if sel:
            fill_text(self.detail, ingredient_report(self.app.db, self.app.packs, sel[0],
                                                     [r["item"] for r in self.app.designer.rows]))

    def add(self):
        sel = self.tree.selection()
        if sel:
            self.app.designer.add_ingredient(sel[0])


# ----------------------------------------------------------------------------
# Application
# ----------------------------------------------------------------------------
class App:
    def __init__(self, root):
        self.root = root
        root.app = self
        root.title("FlavorLab")
        root.geometry("1560x920")
        root.minsize(1100, 700)
        self.tmpdir = tempfile.mkdtemp(prefix="flavorlab_ui_")
        self._png = 0
        self._busy = 0
        self._q = queue.Queue()
        self.on_error = self._default_error
        self.files = pack_files()
        self.sig = files_signature(self.files)
        self.db, self.packs, self.issues = load_db(self.files)

        style = ttk.Style()
        if "vista" in style.theme_names():
            style.theme_use("vista")
        self.nb = ttk.Notebook(root)
        self.nb.pack(fill="both", expand=True)
        self.designer = Designer(self.nb, self)
        self.card = CardTab(self.nb, self)
        self.pair = PairTab(self.nb, self)
        self.map = MapTab(self.nb, self)
        self.compare = CompareTab(self.nb, self)
        self.browser = BrowserTab(self.nb, self)
        for w, t in ((self.designer, "Recipe Designer"), (self.card, "Sauce Card"), (self.pair, "Pairing & Bridge"),
                     (self.map, "Flavor Map"), (self.compare, "Compare"), (self.browser, "Ingredient Browser")):
            self.nb.add(w, text=t)
        sb = ttk.Frame(root)
        sb.pack(fill="x", side="bottom")
        self.status_var = tk.StringVar()
        ttk.Label(sb, textvariable=self.status_var, anchor="w").pack(side="left", fill="x", expand=True, padx=6)
        self.db_var = tk.StringVar()
        dbl = ttk.Label(sb, textvariable=self.db_var, foreground="#6b6a66")
        dbl.pack(side="right", padx=6)
        dbl.bind("<Button-1>", lambda e: self.show_issues())
        ttk.Button(sb, text="Reload ingredients", command=lambda: self.reload_db(force=True)).pack(side="right", padx=4)
        self.prog = ttk.Progressbar(sb, mode="indeterminate", length=120)
        self._on_db_changed()
        self.designer.refresh_table()
        root.protocol("WM_DELETE_WINDOW", self.close)
        self._timers = {"poll": root.after(80, self._poll), "db": root.after(POLL_DB_MS, self._poll_db)}
        if self.issues:
            self.status(f"Started with {len(self.issues)} invalid ingredient row(s) skipped - click the count at "
                        "the bottom right for details.")

    # ---- status / background work ----------------------------------------
    def status(self, text):
        self.status_var.set(text)

    def tmp_png(self, stem):
        self._png += 1
        return os.path.join(self.tmpdir, f"{stem}_{self._png}.png")

    def bg(self, fn, done, label="Working…"):
        self._busy += 1
        self.status(label)

        def target():
            try:
                self._q.put((done, fn(), None))
            except Exception as e:                    # noqa: BLE001
                self._q.put((done, None, e))

        threading.Thread(target=target, daemon=True).start()

    def _poll(self):
        try:
            while True:
                done, res, err = self._q.get_nowait()
                self._busy -= 1
                if err is not None:
                    self.on_error(err)
                else:
                    try:
                        done(res)
                    except Exception as e:            # noqa: BLE001
                        self.on_error(e)
        except queue.Empty:
            pass
        if self._busy > 0 and not self.prog.winfo_ismapped():
            self.prog.pack(side="right", padx=6)
            self.prog.start(12)
        elif self._busy <= 0 and self.prog.winfo_ismapped():
            self.prog.stop()
            self.prog.pack_forget()
        self._timers["poll"] = self.root.after(80, self._poll)

    def _default_error(self, e):
        if isinstance(e, (KeyError, ValueError)):
            msg = e.args[0] if e.args else str(e)
        else:
            traceback.print_exception(type(e), e, e.__traceback__)
            msg = f"{type(e).__name__}: {e}"
        self.status("Error: " + str(msg).splitlines()[0])
        messagebox.showerror("FlavorLab", str(msg))

    # ---- ingredient auto-reload ------------------------------------------
    def show_issues(self):
        if self.issues:
            shown = "\n".join(self.issues[:25]) + (f"\n… and {len(self.issues) - 25} more" if len(self.issues) > 25 else "")
            messagebox.showwarning("Ingredient rows skipped", shown)

    def _on_db_changed(self):
        skipped = f" · ⚠ {len(self.issues)} row(s) skipped (click)" if self.issues else ""
        self.db_var.set(f"{len(self.db.items)} ingredients · {len(self.files)} pack(s){skipped}")
        self.designer.refresh_ingredients()
        self.pair.refresh_ingredients()
        self.map.refresh_ingredients()
        self.browser.refresh_ingredients()
        self.designer.refresh_table()

    def reload_db(self, force=False):
        files = pack_files()
        sig = files_signature(files)
        if not force and sig == self.sig:
            return
        if not force and time.time() - max((m / 1e9 for _, m, _ in sig), default=0) < 1.0:
            return                                   # a file was just written: wait for it to settle
        try:
            db, packs, issues = load_db(files)
        except Exception as e:                       # noqa: BLE001  (unreadable file / nothing valid: keep last good list)
            self.db_var.set(f"{len(self.db.items)} ingredients · reload failed")
            self.status(f"Ingredient reload failed ({type(e).__name__}: {str(e).splitlines()[0]}) - "
                        "keeping the last good list, will retry.")
            return
        new_issues = len(issues) - len(self.issues)
        self.db, self.packs, self.files, self.sig, self.issues = db, packs, files, sig, issues
        self._on_db_changed()
        self.status(f"Ingredients reloaded: {len(db.items)} from {len(files)} pack(s)."
                    + (f"  {len(issues)} invalid row(s) skipped." if new_issues else ""))

    def _poll_db(self):
        try:
            self.reload_db()
        finally:
            self._timers["db"] = self.root.after(POLL_DB_MS, self._poll_db)

    # ---- sauce card -------------------------------------------------------
    def render_card(self):
        d = self.designer
        rec, problems = d.analysis_recipe()
        if not rec["ingredients"]:
            self.status("Add ingredients before rendering a card.")
            return
        db, ver, path = self.db, d.version, self.tmp_png("card")
        include = self.card.moves.get()
        cached = d.sugg if d.sugg_version == ver else None

        def job():
            A = M.analyze(db, rec)
            moves = [] if not include else (cached if cached is not None else M.suggest(db, rec, base=A))
            with RENDER_LOCK:
                fl.sauce_card(db, A, moves, path)
            return A

        def done(A):
            self.card.view.set_image(path, f"{fl.slug(A['name'])}_card.png")
            self.nb.select(self.card)
            self.status("Sauce card ready." + (f"  ({len(problems)} row(s) excluded)" if problems else ""))

        self.bg(job, done, "Rendering sauce card…")

    def close(self):
        if self.designer.confirm_discard():
            for t in list(self._timers.values()) + [self.designer._recalc_job]:
                if t:
                    try:
                        self.root.after_cancel(t)
                    except tk.TclError:
                        pass
            shutil.rmtree(self.tmpdir, ignore_errors=True)
            try:                                      # matplotlib's Tk canvas can trip Tk's teardown
                self.designer.canvas.get_tk_widget().destroy()
                self.root.destroy()
            except tk.TclError:
                pass


def main():
    try:                                              # crisp text on Windows high-DPI displays
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:                                 # noqa: BLE001
        pass
    root = tk.Tk()
    try:
        App(root)
    except Exception as e:                            # noqa: BLE001
        root.withdraw()
        messagebox.showerror("FlavorLab", f"Could not start: {e}")
        sys.exit(1)
    root.mainloop()


if __name__ == "__main__":
    main()
