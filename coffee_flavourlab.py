"""Coffee Flavourlab: combination grid, origin and variety explorer, recipes, troubleshooter, data browser and chat box."""
import json
import tkinter as tk
from tkinter import ttk

from brew_guide import (
    KETTLES, METHOD_LABELS, STYLES, TASTES, UNKNOWN, BrewGuide, describe_equipment, load_config, num, render, save_config,
)
from coffee_knowledge import METHODS, ROASTS, Knowledge, rank

GRID_COLUMNS = ["method", "roast", "process", "ratio", "time_s", "temp_c", "grind_um", "water", "cup", "confidence", "missing"]
ORIGIN_COLUMNS = ["country", "region", "altitude_min_masl", "altitude_max_masl", "processing", "harvest_months", "flavor_notes", "confidence"]
VARIETY_COLUMNS = ["source_set", "variety", "species", "group", "origin_country", "altitude_wcr_triplet_masl",
                   "rust_resistance", "cup_notes", "coffee_review_avg_score", "confidence"]
RECIPE_COLUMNS = ["id", "name", "author", "dose_g", "water_g", "ratio", "temp_c", "grind", "bloom_g", "bloom_s",
                  "total_time_s", "confidence"]
TROUBLE_COLUMNS = ["method", "symptom", "time_or_flow", "diagnosis", "action", "confidence"]
SHOT_COLUMNS = ["n", "dose_g", "yield_g", "ratio", "time_s", "taste", "dial", "diagnosis"]

MACHINE_FIELDS = [
    ("boiler_type", "Boiler system", ["single_boiler", "heat_exchanger", "dual_boiler", "thermoblock_or_fixed"]),
    ("pump", "Pump", ["vibration", "rotary", "vibration or rotary"]),
    ("temp_control", "Temperature control", ["PID on boiler", "PID on brew boiler", "cooling flush only", "none"]),
    ("temp_step_c", "Smallest temperature step (C)", None),
    ("brew_pressure_adjust", "Where do you adjust brew pressure?", None),
    ("preinfusion", "Pre-infusion or flow control", None),
    ("basket_g", "Basket rated dose (g)", None),
    ("temp_offset_c", "Measured offset: water in cup minus PID setting (C)", None),
]
GRINDER_FIELDS = [
    ("burr_mm", "Burr diameter (mm)", None),
    ("adjustment", "Adjustment type", ["stepless micrometric", "stepless", "stepped"]),
    ("finer_direction", "Which way is finer?", ["clockwise", "anticlockwise", "unknown"]),
    ("dial_note", "How is your dial marked?", None),
]
CONF_COLOR = {5: "#1b6e3c", 4: "#1b6e3c", 3: "#9a6700", 2: "#9a6700", 1: "#b3261e", 0: "#b3261e"}


def _cell(value):
    if value is None:
        return ""
    if isinstance(value, (list, dict)):
        return json.dumps(value, ensure_ascii=False)
    return str(value)


class Table(ttk.Frame):
    def __init__(self, master, on_select):
        super().__init__(master)
        self.tree = ttk.Treeview(self, show="headings", selectmode="browse")
        ys = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        xs = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=ys.set, xscrollcommand=xs.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        ys.grid(row=0, column=1, sticky="ns")
        xs.grid(row=1, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rows = []
        self.on_select = on_select
        self.tree.bind("<<TreeviewSelect>>", self._selected)

    def load(self, rows, columns):
        self.rows = list(rows)
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = columns
        for column in columns:
            self.tree.heading(column, text=column)
            wide = column in ("diagnosis", "action", "cup", "flavor_notes", "cup_notes", "symptom")
            self.tree.column(column, width=260 if wide else max(90, min(260, 9 * len(column) + 40)), stretch=False, anchor="w")
        for i, row in enumerate(self.rows):
            self.tree.insert("", "end", iid=str(i), values=[_cell(row.get(c)) for c in columns])

    def _selected(self, _event):
        selection = self.tree.selection()
        if selection:
            self.on_select(self.rows[int(selection[0])])


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Flavourlab")
        self.geometry("1280x880")
        self.kb = Knowledge()
        self.guide = BrewGuide(self.kb, load_config())
        self._loading = True
        self._pending = None
        self.plan = None
        self._build_chat()
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(side="top", fill="both", expand=True, padx=6, pady=(6, 0))
        self._build_guide()
        self._build_equipment()
        self._build_dialin()
        self._loading = False
        self._fill_equipment()
        self._regen()
        self._build_grid()
        self._build_origins()
        self._build_varieties()
        self._build_recipes()
        self._build_troubleshoot()
        self._build_browser()

    # helpers
    def _tab(self, title):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text=title)
        return frame

    def _detail(self, parent):
        box = tk.Text(parent, height=8, wrap="word", state="disabled", background="#f7f7f2")
        box.pack(side="bottom", fill="x", padx=6, pady=(0, 6))
        return box

    def _show(self, box, row):
        lines = [f"{key}: {_cell(value)}" for key, value in row.items() if value not in (None, "", [])]
        box.configure(state="normal")
        box.delete("1.0", "end")
        box.insert("end", "\n".join(lines))
        box.configure(state="disabled")

    def _filter_bar(self, parent):
        bar = ttk.Frame(parent)
        bar.pack(side="top", fill="x", padx=6, pady=4)
        return bar

    def _combo(self, parent, label, values, command, default=None):
        ttk.Label(parent, text=label).pack(side="left", padx=(6, 2))
        box = ttk.Combobox(parent, values=values, state="readonly", width=16)
        box.set(default if default is not None else values[0])
        box.pack(side="left", padx=(0, 10))
        box.bind("<<ComboboxSelected>>", lambda _e: command())
        return box

    def _entry(self, parent, label, command):
        ttk.Label(parent, text=label).pack(side="left", padx=(6, 2))
        entry = ttk.Entry(parent, width=22)
        entry.pack(side="left", padx=(0, 10))
        entry.bind("<KeyRelease>", lambda _e: command())
        return entry

    # -- shared form helpers for the guided tabs ----------------------------------------------------------------------
    def _field(self, parent, row, label, widget):
        ttk.Label(parent, text=label, wraplength=170, justify="left").grid(row=row, column=0, sticky="w", padx=(6, 6), pady=2)
        widget.grid(row=row, column=1, sticky="ew", padx=(0, 6), pady=2)
        parent.columnconfigure(1, weight=1)
        return widget

    def _var_combo(self, parent, row, label, values, var, state="readonly"):
        box = ttk.Combobox(parent, values=values, textvariable=var, state=state, width=24)
        return self._field(parent, row, label, box)

    def _var_entry(self, parent, row, label, var, width=26):
        return self._field(parent, row, label, ttk.Entry(parent, textvariable=var, width=width))

    def _result_text(self, parent):
        frame = ttk.Frame(parent)
        text = tk.Text(frame, wrap="word", state="disabled", background="#fbfbf7", padx=10, pady=8, font=("Segoe UI", 10))
        bar = ttk.Scrollbar(frame, orient="vertical", command=text.yview)
        text.configure(yscrollcommand=bar.set)
        text.pack(side="left", fill="both", expand=True)
        bar.pack(side="right", fill="y")
        text.tag_configure("title", font=("Segoe UI", 14, "bold"), spacing3=6)
        text.tag_configure("card", font=("Segoe UI", 12, "bold"), background="#efe6d8", foreground="#3b2a14", spacing1=4, spacing3=6,
                           lmargin1=6, lmargin2=6)
        text.tag_configure("section", font=("Segoe UI", 11, "bold"), spacing1=12, spacing3=3, foreground="#3b3b36")
        text.tag_configure("label", font=("Segoe UI", 10), foreground="#555")
        text.tag_configure("value", font=("Segoe UI", 12, "bold"))
        text.tag_configure("basis", foreground="#555", lmargin1=18, lmargin2=18, spacing3=4)
        text.tag_configure("warn", foreground="#8a4b00", lmargin1=12, lmargin2=24)
        text.tag_configure("ask", foreground="#0b57d0", lmargin1=12, lmargin2=24)
        for rk, color in CONF_COLOR.items():
            text.tag_configure(f"conf{rk}", foreground=color, font=("Segoe UI", 9, "bold"))
        return frame, text

    @staticmethod
    def _put(text, *pieces):
        text.configure(state="normal")
        for chunk, tag in pieces:
            text.insert("end", chunk, tag)
        text.configure(state="disabled")

    @staticmethod
    def _clear(text):
        text.configure(state="normal")
        text.delete("1.0", "end")
        text.configure(state="disabled")

    def _conf_tag(self, label):
        return f"conf{min(rank(label), 5)}"

    # -- tab 1: the interactive brew guide ----------------------------------------------------------------------------
    def _build_guide(self):
        frame = self._tab("Brew guide")
        panes = ttk.PanedWindow(frame, orient="horizontal")
        panes.pack(fill="both", expand=True, padx=6, pady=6)
        left = ttk.Frame(panes, width=380)
        panes.add(left, weight=0)

        self.v_method = tk.StringVar(value=METHOD_LABELS["espresso"])
        self.v_style = tk.StringVar(value="normale")
        self.v_country = tk.StringVar(value=UNKNOWN)
        self.v_region = tk.StringVar(value=UNKNOWN)
        self.v_altitude = tk.StringVar(value="")
        self.v_variety = tk.StringVar(value=UNKNOWN)
        self.v_process = tk.StringVar(value=UNKNOWN)
        self.v_roast = tk.StringVar(value="Medium")
        self.v_days = tk.StringVar(value="")
        self.v_dose = tk.StringVar(value="")

        what = ttk.LabelFrame(left, text="1. What are you making?")
        what.pack(fill="x", pady=(0, 6))
        self._var_combo(what, 0, "Brew method", list(METHOD_LABELS.values()), self.v_method)
        self.c_style = self._var_combo(what, 1, "Espresso style", STYLES, self.v_style)
        self._var_entry(what, 2, "Dose in grams (blank = basket)", self.v_dose, 10)

        coffee = ttk.LabelFrame(left, text="2. The coffee")
        coffee.pack(fill="x", pady=(0, 6))
        countries = [UNKNOWN] + self.kb.countries
        self.c_country = self._var_combo(coffee, 0, "Country", countries, self.v_country)
        self.c_region = self._var_combo(coffee, 1, "Region", [UNKNOWN], self.v_region)
        spin = ttk.Spinbox(coffee, from_=0, to=3000, increment=50, textvariable=self.v_altitude, width=10)
        self._field(coffee, 2, "Growing altitude (masl)", spin)
        self.l_alt_hint = ttk.Label(coffee, text="", foreground="#555", wraplength=330, justify="left")
        self.l_alt_hint.grid(row=3, column=0, columnspan=2, sticky="w", padx=6)
        varieties = [UNKNOWN] + sorted({str(r["variety"]) for r in self.kb.varieties})
        self._var_combo(coffee, 4, "Variety", varieties, self.v_variety)
        self._var_combo(coffee, 5, "Process", [UNKNOWN] + self.kb.processes, self.v_process)
        self._var_combo(coffee, 6, "Roast", ROASTS, self.v_roast)
        self._field(coffee, 7, "Days since roasting", ttk.Spinbox(coffee, from_=0, to=120, increment=1, textvariable=self.v_days, width=10))

        gear = ttk.LabelFrame(left, text="3. Your equipment")
        gear.pack(fill="x")
        self.l_gear = ttk.Label(gear, text="", wraplength=340, justify="left")
        self.l_gear.pack(fill="x", padx=6, pady=4)
        ttk.Button(gear, text="Answer equipment questions...", command=lambda: self.notebook.select(1)).pack(anchor="w", padx=6, pady=(0, 6))

        right, self.guide_text = self._result_text(panes)
        panes.add(right, weight=1)

        self.c_country.bind("<<ComboboxSelected>>", lambda _e: self._country_changed())
        self.c_region.bind("<<ComboboxSelected>>", lambda _e: self._region_changed())
        for var in (self.v_method, self.v_style, self.v_altitude, self.v_variety, self.v_process, self.v_roast, self.v_days, self.v_dose):
            var.trace_add("write", lambda *_a: self._schedule())

    def _country_changed(self):
        names = [UNKNOWN] + [r["region"] for r in self.guide.regions(self.v_country.get())]
        self.c_region.configure(values=names)
        self.v_region.set(UNKNOWN)
        self._schedule()

    def _region_changed(self):
        alt = self.guide.region_altitude(self.v_country.get(), self.v_region.get())
        if alt:
            self.v_altitude.set(str(round((alt[0] + alt[1]) / 2 / 50) * 50))
            self.l_alt_hint.configure(text=f"{self.v_region.get()} is listed at {alt[0]}-{alt[1]} masl. "
                                           "Altitude was set to the middle; change it to the figure on your bag.")
        else:
            self.l_alt_hint.configure(text="No altitude range is listed for this region. Enter the figure from your bag.")
        self._schedule()

    def _profile(self):
        method = next((k for k, v in METHOD_LABELS.items() if v == self.v_method.get()), "espresso")
        pick = lambda var: None if var.get() in ("", UNKNOWN) else var.get()
        alt = num(self.v_altitude.get())
        return {
            "method": method, "style": self.v_style.get() or "normale", "roast": self.v_roast.get() or "Medium",
            "altitude_masl": int(alt) if alt is not None else None, "country": pick(self.v_country), "region": pick(self.v_region),
            "variety": pick(self.v_variety), "process": pick(self.v_process),
            "days_since_roast": num(self.v_days.get()), "dose_g": num(self.v_dose.get()),
        }

    def _schedule(self):
        if self._loading:
            return
        if self._pending:
            self.after_cancel(self._pending)
        self._pending = self.after(150, self._regen)

    def _regen(self):
        self._pending = None
        profile = self._profile()
        self.c_style.configure(state="readonly" if profile["method"] == "espresso" else "disabled")
        self.plan = self.guide.plan(profile)
        machine, grinder = self.plan["machine"], self.plan["grinder"]
        self.l_gear.configure(text=f"{machine.get('name', 'no machine')}  +  {grinder.get('name', 'no grinder')}"
                                   + ("" if profile["method"] == "espresso" else "\n(machine settings apply to espresso only)"))
        self._write_plan(self.plan)
        if hasattr(self, "dial_target"):
            self._refresh_dial_target()

    def _write_plan(self, plan):
        t, p = self.guide_text, plan["profile"]
        self._clear(t)
        bits = [METHOD_LABELS[p["method"]]] + ([p["style"]] if p["method"] == "espresso" else []) + [f"{p['roast']} roast"]
        if p["altitude_masl"] is not None:
            bits.append(f"{p['altitude_masl']} masl")
        self._put(t, (" · ".join(bits) + "\n", "title"))
        card = {s["key"]: s["value"] for s in plan["settings"]}
        if p["method"] == "espresso":
            line = f"{card.get('dose')} in  →  {card.get('yield')} out  in  {card.get('time')}   ·   {card.get('temp')}"
            if "setpoint" in card:
                line += f" (set PID to {card['setpoint']})"
            line += f"   ·   {card.get('pressure', '').split(' (')[0]}"
        else:
            line = f"{card.get('dose')} coffee  +  {card.get('yield')} water   ·   {card.get('temp')}   ·   {card.get('time', 'time n/s')}"
        self._put(t, (line + "\n", "card"))
        self._put(t, ("Every value below carries a confidence label; grey text says where it came from.\n", "label"))
        self._put(t, ("Settings\n", "section"))
        for s in plan["settings"]:
            if s["key"] in ("altitude", "process", "variety"):
                continue
            self._put(t, (f"{s['label']}   ", "label"), (f"{s['value']}   ", "value"), (f"[{s['confidence']}]\n", self._conf_tag(s["confidence"])),
                      (f"{s['basis']}\n", "basis"))
        about = [s for s in plan["settings"] if s["key"] in ("altitude", "process", "variety")]
        if about:
            self._put(t, ("What your coffee tells us\n", "section"))
            for s in about:
                self._put(t, (f"{s['label']}   ", "label"), (f"{s['value']}   ", "value"), (f"[{s['confidence']}]\n", self._conf_tag(s["confidence"])),
                          (f"{s['basis']}\n", "basis"))
        if plan["steps"]:
            self._put(t, ("On your equipment, step by step\n", "section"))
            for i, step in enumerate(plan["steps"], 1):
                self._put(t, (f"{i}. {step}\n", "basis"))
        if plan["warnings"]:
            self._put(t, ("Check these\n", "section"))
            for w in plan["warnings"]:
                self._put(t, (f"! {w}\n", "warn"))
        if plan["questions"]:
            self._put(t, ("Questions for you\n", "section"))
            for q in plan["questions"]:
                self._put(t, (f"? {q}\n", "ask"))

    # -- tab 2: equipment questions -----------------------------------------------------------------------------------
    def _build_equipment(self):
        frame = self._tab("My equipment")
        ttk.Label(frame, text="Answer these so the guide fits your gear. Pick a preset, then correct anything that differs on your unit. "
                              "Changes save automatically.", wraplength=1100).pack(anchor="w", padx=10, pady=(8, 4))
        cols = ttk.Frame(frame)
        cols.pack(fill="both", expand=True, padx=6, pady=4)
        cols.columnconfigure(0, weight=1)
        cols.columnconfigure(1, weight=1)
        self.eq_vars = {}

        m_box = ttk.LabelFrame(cols, text="Espresso machine")
        m_box.grid(row=0, column=0, sticky="nsew", padx=(0, 6))
        self.machine_names = {r["name"]: r["id"] for r in self.kb.table("equipment_machines")}
        self.v_machine = tk.StringVar()
        self._var_combo(m_box, 0, "Which machine do you have?", list(self.machine_names), self.v_machine)
        for i, (key, label, values) in enumerate(MACHINE_FIELDS, 1):
            var = self.eq_vars[("machine", key)] = tk.StringVar()
            if values:
                self._var_combo(m_box, i, label, values, var, state="normal")
            else:
                self._var_entry(m_box, i, label, var)
            var.trace_add("write", lambda *_a: self._equip_changed())
        self.l_machine_src = ttk.Label(m_box, text="", wraplength=470, justify="left", foreground="#555")
        self.l_machine_src.grid(row=len(MACHINE_FIELDS) + 1, column=0, columnspan=2, sticky="w", padx=6, pady=6)

        g_box = ttk.LabelFrame(cols, text="Grinder")
        g_box.grid(row=0, column=1, sticky="nsew", padx=(6, 0))
        self.grinder_names = {r["name"]: r["id"] for r in self.kb.table("equipment_grinders")}
        self.v_grinder = tk.StringVar()
        self._var_combo(g_box, 0, "Which grinder do you have?", list(self.grinder_names), self.v_grinder)
        for i, (key, label, values) in enumerate(GRINDER_FIELDS, 1):
            var = self.eq_vars[("grinder", key)] = tk.StringVar()
            if values:
                self._var_combo(g_box, i, label, values, var, state="normal")
            else:
                self._var_entry(g_box, i, label, var)
            var.trace_add("write", lambda *_a: self._equip_changed())
        self.l_grinder_src = ttk.Label(g_box, text="", wraplength=470, justify="left", foreground="#555")
        self.l_grinder_src.grid(row=len(GRINDER_FIELDS) + 1, column=0, columnspan=2, sticky="w", padx=6, pady=6)

        o_box = ttk.LabelFrame(frame, text="Filter brewing and water")
        o_box.pack(fill="x", padx=6, pady=6)
        self.v_kettle = tk.StringVar(value=self.guide.cfg.get("kettle", KETTLES[0]))
        self.v_scale = tk.StringVar(value=str(self.guide.cfg.get("scale_g", "0.1")))
        self.v_water = tk.StringVar(value=self.guide.cfg.get("water_note", ""))
        self._var_combo(o_box, 0, "Kettle", KETTLES, self.v_kettle)
        self._var_combo(o_box, 1, "Scale resolution (g)", ["0.1", "0.01", "1"], self.v_scale)
        self._var_entry(o_box, 2, "Brewing water (tap, filtered, bottled...)", self.v_water, 40)
        for var in (self.v_kettle, self.v_scale, self.v_water):
            var.trace_add("write", lambda *_a: self._equip_changed())
        self.l_eq_status = ttk.Label(frame, text="", foreground="#1b6e3c")
        self.l_eq_status.pack(anchor="w", padx=10, pady=(0, 8))
        self.v_machine.trace_add("write", lambda *_a: self._preset_changed("machine"))
        self.v_grinder.trace_add("write", lambda *_a: self._preset_changed("grinder"))

    def _preset_changed(self, which):
        if self._loading:
            return
        names = self.machine_names if which == "machine" else self.grinder_names
        var = self.v_machine if which == "machine" else self.v_grinder
        if var.get() not in names:
            return
        keep = {"machine": {"temp_offset_c": 0, "basket_g": 18}, "grinder": {}}[which]
        self.guide.cfg[which] = {"preset": names[var.get()], "overrides": dict(keep)}
        self._fill_equipment()
        self._equip_saved()

    def _fill_equipment(self):
        self._loading = True
        try:
            machine, grinder = self.guide.equipment()
            self.v_machine.set(machine.get("name", ""))
            self.v_grinder.set(grinder.get("name", ""))
            for (which, key), var in self.eq_vars.items():
                row = machine if which == "machine" else grinder
                value = row.get(key)
                var.set("" if value is None else str(value))
            self.l_machine_src.configure(text=self._source_text(machine))
            self.l_grinder_src.configure(text=self._source_text(grinder))
        finally:
            self._loading = False

    @staticmethod
    def _source_text(row):
        parts = [f"Source confidence: {row.get('confidence') or 'none'}."]
        if row.get("notes"):
            parts.append(row["notes"])
        if row.get("conflict_note"):
            parts.append("Conflict: " + row["conflict_note"])
        if row.get("source_url"):
            parts.append("Sources: " + row["source_url"])
        return "  ".join(parts)

    def _equip_changed(self):
        if self._loading:
            return
        for which in ("machine", "grinder"):
            preset = self.kb.find(f"equipment_{which}s", "id", self.guide.cfg[which]["preset"]) or {}
            overrides = {}
            for (w, key), var in self.eq_vars.items():
                if w == which and var.get() != ("" if preset.get(key) is None else str(preset.get(key))):
                    overrides[key] = var.get()
            self.guide.cfg[which]["overrides"] = overrides
        self.guide.cfg.update(kettle=self.v_kettle.get(), scale_g=self.v_scale.get(), water_note=self.v_water.get())
        self._equip_saved()
        self._schedule()

    def _equip_saved(self):
        try:
            save_config(self.guide.cfg)
            self.l_eq_status.configure(text="Saved.", foreground="#1b6e3c")
        except OSError as exc:
            self.l_eq_status.configure(text=f"Could not save equipment: {exc}", foreground="#b3261e")
        self._schedule()

    # -- tab 3: dial-in loop ------------------------------------------------------------------------------------------
    def _build_dialin(self):
        frame = self._tab("Dial-in")
        panes = ttk.PanedWindow(frame, orient="horizontal")
        panes.pack(fill="both", expand=True, padx=6, pady=6)
        left = ttk.Frame(panes, width=380)
        panes.add(left, weight=0)
        self.dial_target = ttk.Label(left, text="", wraplength=350, justify="left", font=("Segoe UI", 10, "bold"))
        self.dial_target.pack(fill="x", padx=6, pady=(4, 8))
        form = ttk.LabelFrame(left, text="The shot you just pulled")
        form.pack(fill="x")
        self.s_dose, self.s_yield, self.s_time, self.s_dial = (tk.StringVar() for _ in range(4))
        self.s_taste = tk.StringVar(value=TASTES[1])
        self._var_entry(form, 0, "Dose in (g)", self.s_dose, 10)
        self._var_entry(form, 1, "Liquid out (g)", self.s_yield, 10)
        self._var_entry(form, 2, "Time (s)", self.s_time, 10)
        self._var_combo(form, 3, "How does it taste?", TASTES, self.s_taste)
        self._var_entry(form, 4, "Grinder dial reading (a number, optional)", self.s_dial, 10)
        btns = ttk.Frame(left)
        btns.pack(fill="x", pady=8)
        ttk.Button(btns, text="Record shot and advise", command=self._record_shot).pack(side="left", padx=6)
        ttk.Button(btns, text="Clear history", command=self._clear_shots).pack(side="left")
        ttk.Label(left, text="Change one thing per shot. Two shots at different dial readings let the tool measure how many seconds one "
                             "dial unit moves your grinder.", wraplength=350, foreground="#555").pack(fill="x", padx=6)
        right = ttk.Frame(panes)
        panes.add(right, weight=1)
        out, self.dial_text = self._result_text(right)
        out.pack(fill="both", expand=True)
        self.shot_table = Table(right, on_select=lambda _row: None)
        self.shot_table.pack(fill="x", pady=(6, 0))
        self.shot_table.tree.configure(height=6)
        self._reload_shots()

    def _refresh_dial_target(self):
        tg = self.plan["targets"]
        if self.plan["profile"]["method"] != "espresso":
            self.dial_target.configure(text="Dial-in advice covers espresso. For filter methods use the Troubleshoot tab.")
            return
        self.dial_target.configure(text=f"Target: {tg.get('dose', '?')} in, {tg.get('yield', '?')} out, {tg.get('time', '?')}")

    def _record_shot(self):
        if self.plan["profile"]["method"] != "espresso":
            self._clear(self.dial_text)
            self._put(self.dial_text, ("Switch the Brew guide to espresso first.\n", "warn"))
            return
        dose, out, t = num(self.s_dose.get()), num(self.s_yield.get()), num(self.s_time.get())
        if dose is None or out is None or t is None:
            self._clear(self.dial_text)
            self._put(self.dial_text, ("Enter dose, liquid out and time as numbers.\n", "warn"))
            return
        shot = {"dose_g": dose, "yield_g": out, "time_s": t, "taste": self.s_taste.get(), "dial": num(self.s_dial.get())}
        history = list(self.guide.cfg["shots"])
        advice = self.guide.advise(self.plan, shot, history)
        shot["diagnosis"] = advice["diagnosis"]
        self.guide.cfg["shots"].append(shot)
        self._equip_saved()
        self._reload_shots()
        self._write_advice(shot, advice)

    def _write_advice(self, shot, a):
        t = self.dial_text
        self._clear(t)
        self._put(t, ("Next step\n", "title"))
        self._put(t, ("What the shot says   ", "label"), (f"{a['diagnosis']}   ", "value"), (f"[{a['confidence']}]\n", self._conf_tag(a["confidence"])))
        self._put(t, ("Do this   ", "label"), (f"{a['action']}\n", "value"))
        if a["dial"]:
            self._put(t, (a["dial"] + "\n", "basis"))
        if a["calibration"]:
            self._put(t, ("Your grinder\n", "section"), (a["calibration"] + "\n", "basis"))
        if a["temp_hint"]:
            self._put(t, ("Temperature\n", "section"), (a["temp_hint"] + "\n", "basis"))
        if a["notes"]:
            self._put(t, ("Reading your numbers\n", "section"))
            for n in a["notes"]:
                self._put(t, (f"- {n}\n", "basis"))
        self._put(t, (a["one_change"] + "\n", "basis"))
        for url in a["sources"]:
            self._put(t, (url + "\n", "basis"))

    def _reload_shots(self):
        rows = []
        for i, s in enumerate(self.guide.cfg["shots"], 1):
            ratio = f"1:{s['yield_g'] / s['dose_g']:.2f}" if s.get("dose_g") and s.get("yield_g") else ""
            rows.append({**s, "n": i, "ratio": ratio, "dial": "" if s.get("dial") is None else s["dial"]})
        self.shot_table.load(rows, SHOT_COLUMNS)

    def _clear_shots(self):
        self.guide.cfg["shots"] = []
        self._equip_saved()
        self._reload_shots()
        self._clear(self.dial_text)

    # -- reference tabs -----------------------------------------------------------------------------------------------
    def _build_grid(self):
        frame = self._tab("Combination grid")
        bar = self._filter_bar(frame)
        self.grid_all = self.kb.grid()
        processes = ["all", "none"] + self.kb.processes
        self.g_method = self._combo(bar, "Method", ["all"] + METHODS, self._refresh_grid)
        self.g_roast = self._combo(bar, "Roast", ["all"] + ROASTS, self._refresh_grid)
        self.g_process = self._combo(bar, "Process", processes, self._refresh_grid)
        self.g_count = ttk.Label(bar, text="")
        self.g_count.pack(side="left", padx=10)
        detail = self._detail(frame)
        self.grid_table = Table(frame, on_select=lambda row: self._show(detail, row))
        self.grid_table.pack(side="top", fill="both", expand=True, padx=6)
        self._refresh_grid()

    def _refresh_grid(self):
        method, roast, process = self.g_method.get(), self.g_roast.get(), self.g_process.get()
        rows = []
        for row in self.grid_all:
            if method != "all" and row["method"] != method:
                continue
            if roast != "all" and row["roast"] != roast:
                continue
            if process == "none" and row["process"]:
                continue
            if process not in ("all", "none") and row["process"] != process:
                continue
            rows.append({**row, "missing": ", ".join(row["missing"]) or "none"})
        self.grid_table.load(rows, GRID_COLUMNS)
        self.g_count.configure(text=f"{len(rows)} combinations")

    def _build_origins(self):
        frame = self._tab("Origins")
        bar = self._filter_bar(frame)
        self.o_country = self._entry(bar, "Country", self._refresh_origins)
        self.o_process = self._entry(bar, "Processing contains", self._refresh_origins)
        detail = self._detail(frame)
        self.origin_table = Table(frame, on_select=lambda row: self._show(detail, row))
        self.origin_table.pack(side="top", fill="both", expand=True, padx=6)
        self._refresh_origins()

    def _refresh_origins(self):
        rows = self.kb.origins(self.o_country.get().strip() or None, self.o_process.get().strip() or None)
        self.origin_table.load(rows, ORIGIN_COLUMNS)

    def _build_varieties(self):
        frame = self._tab("Varieties")
        bar = self._filter_bar(frame)
        self.v_search = self._entry(bar, "Search", self._refresh_varieties)
        detail = self._detail(frame)
        self.variety_table = Table(frame, on_select=lambda row: self._show(detail, row))
        self.variety_table.pack(side="top", fill="both", expand=True, padx=6)
        self._refresh_varieties()

    def _refresh_varieties(self):
        term = self.v_search.get().strip().lower()
        rows = [r for r in self.kb.varieties
                if not term or any(term in _cell(r.get(k)).lower() for k in ("variety", "group", "origin_country", "cup_notes"))]
        self.variety_table.load(rows, VARIETY_COLUMNS)

    def _build_recipes(self):
        frame = self._tab("Recipes")
        bar = self._filter_bar(frame)
        methods = sorted({r["method"] for r in self.kb.table("brew_recipes")})
        self.r_method = self._combo(bar, "Method", ["all"] + methods, self._refresh_recipes)
        detail = self._detail(frame)
        self.recipe_table = Table(frame, on_select=lambda row: self._show(detail, row))
        self.recipe_table.pack(side="top", fill="both", expand=True, padx=6)
        self._refresh_recipes()

    def _refresh_recipes(self):
        method = self.r_method.get()
        rows = [r for r in self.kb.table("brew_recipes") if method == "all" or r.get("method") == method]
        self.recipe_table.load(rows, RECIPE_COLUMNS)

    def _build_troubleshoot(self):
        frame = self._tab("Troubleshoot")
        bar = self._filter_bar(frame)
        self.t_method = self._combo(bar, "Method", ["all", "espresso", "pour_over"], self._refresh_trouble)
        self.t_search = self._entry(bar, "Symptom contains", self._refresh_trouble)
        detail = self._detail(frame)
        self.trouble_table = Table(frame, on_select=lambda row: self._show(detail, row))
        self.trouble_table.pack(side="top", fill="both", expand=True, padx=6)
        self._refresh_trouble()

    def _refresh_trouble(self):
        method, term = self.t_method.get(), self.t_search.get().strip().lower()
        rows = [r for r in self.kb.table("troubleshooting")
                if (method == "all" or r.get("method") == method)
                and (not term or term in (r.get("symptom") or "").lower() or term in (r.get("diagnosis") or "").lower())]
        self.trouble_table.load(rows, TROUBLE_COLUMNS)

    def _build_browser(self):
        frame = self._tab("Data browser")
        bar = self._filter_bar(frame)
        names = sorted(name for name, rows in self.kb.data.items() if rows)
        self.b_dataset = self._combo(bar, "Dataset", names, self._refresh_browser, default=names[0] if names else None)
        self.b_search = self._entry(bar, "Search", self._refresh_browser)
        detail = self._detail(frame)
        self.browser_table = Table(frame, on_select=lambda row: self._show(detail, row))
        self.browser_table.pack(side="top", fill="both", expand=True, padx=6)
        self._refresh_browser()

    def _refresh_browser(self):
        name = self.b_dataset.get()
        rows = self.kb.table(name)
        term = self.b_search.get().strip().lower()
        if term:
            rows = [r for r in rows if term in json.dumps(r, ensure_ascii=False).lower()]
        columns = list(self.kb.table(name)[0].keys()) if self.kb.table(name) else []
        self.browser_table.load(rows, columns)

    # chat box, always visible at the bottom
    def _build_chat(self):
        box = ttk.LabelFrame(self, text="Ask the agent (answers come from the local coffee data, no online model)")
        box.pack(side="bottom", fill="x", padx=6, pady=6)
        log_frame = ttk.Frame(box)
        log_frame.pack(fill="x", padx=4, pady=(4, 2))
        self.chat_log = tk.Text(log_frame, height=6, wrap="word", state="disabled", background="#fbfbf7")
        scroll = ttk.Scrollbar(log_frame, orient="vertical", command=self.chat_log.yview)
        self.chat_log.configure(yscrollcommand=scroll.set)
        self.chat_log.pack(side="left", fill="x", expand=True)
        scroll.pack(side="right", fill="y")
        row = ttk.Frame(box)
        row.pack(fill="x", padx=4, pady=(0, 4))
        self.chat_entry = ttk.Entry(row)
        self.chat_entry.pack(side="left", fill="x", expand=True)
        self.chat_entry.bind("<Return>", lambda _e: self._ask())
        ttk.Button(row, text="Send", command=self._ask).pack(side="left", padx=(4, 0))
        self._say("Agent", "Hi. Use the Brew guide tab for settings, My equipment for your machine and grinder, and Dial-in after each shot. "
                           "Ask me anything else here: 'my machine', 'sour and fast espresso', 'ethiopia altitude', 'help'.")

    def _say(self, who, text):
        self.chat_log.configure(state="normal")
        self.chat_log.insert("end", f"{who}: {text}\n\n")
        self.chat_log.configure(state="disabled")
        self.chat_log.see("end")

    def _ask(self):
        question = self.chat_entry.get().strip()
        if not question:
            return
        self._say("You", question)
        low = question.lower()
        if any(k in low for k in ("my machine", "my grinder", "my equipment", "my setup", "classika", "mignon", "my guide", "my plan")):
            reply = describe_equipment(*self.guide.equipment())
            if self.plan:
                reply += "\n\nCurrent guide:\n" + render(self.plan)
        else:
            reply = self.kb.answer(question)
        self._say("Agent", reply)
        self.chat_entry.delete(0, "end")


if __name__ == "__main__":
    App().mainloop()
