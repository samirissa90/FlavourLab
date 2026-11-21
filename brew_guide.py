"""Interactive brew guide engine for Coffee Flavourlab. No UI code.

Takes a coffee (method, origin, altitude, variety, process, roast, age) plus the user's equipment and returns
settings with a confidence label and the reason behind each one. Also turns a pulled shot into the next
adjustment. Anything the data does not support is said to be unsupported and is never filled in.
"""
import json
import re
from pathlib import Path

from coffee_knowledge import (
    GRIND_KEY, ROAST_TEMP, ROAST_TEMP_LABEL, ROASTS, Knowledge, rank, weakest,
)

CONFIG_PATH = Path(__file__).resolve().parent / "coffee_equipment.json"

METHOD_LABELS = {
    "espresso": "Espresso", "pour_over": "Pour over / V60", "aeropress": "AeroPress", "french_press": "French press",
    "cold_brew": "Cold brew", "siphon": "Siphon", "chemex": "Chemex", "moka": "Moka pot",
}
STYLE_ROWS = {"ristretto": "ristretto", "normale": "normale_baseline", "lungo": "lungo"}
STYLES = list(STYLE_ROWS)
TASTES = ["sour / thin", "balanced / sweet", "bitter / harsh", "burnt / ashy", "weak / watery", "muddy / heavy"]
UNKNOWN = "(unknown)"

# Equipment questions the UI asks. key -> (prompt, choices or None for free text, where it is stored)
MACHINE_QUESTIONS = [
    ("preset", "Which espresso machine do you have?"),
    ("boiler_type", "What boiler system is it? (single boiler, heat exchanger, dual boiler)"),
    ("pump", "What pump does it use? (vibration or rotary)"),
    ("temp_control", "How is brew temperature controlled? (PID, cooling flush, none)"),
    ("temp_step_c", "How small a temperature step can you set, in degrees C?"),
    ("brew_pressure_adjust", "Can you adjust brew pressure, and where?"),
    ("preinfusion", "Do you have pre-infusion or flow control?"),
    ("basket_g", "What is your basket's rated dose in grams?"),
    ("temp_offset_c", "Measured offset between PID setting and water in the cup, in degrees C (0 if unknown)"),
]
GRINDER_QUESTIONS = [
    ("preset", "Which grinder do you have?"),
    ("burr_mm", "Burr diameter in mm?"),
    ("adjustment", "Stepless or stepped adjustment?"),
    ("finer_direction", "Which way is finer? (clockwise or anticlockwise)"),
    ("dial_note", "How is your dial marked? (e.g. numbers, marks per turn)"),
]
OTHER_QUESTIONS = [
    ("kettle", "For filter methods: what kettle do you use?"),
    ("scale_g", "Scale resolution in grams (0.1 or 0.01)?"),
    ("water_note", "What water do you brew with? (tap, filtered, bottled, remineralised)"),
]
KETTLES = ["variable temperature gooseneck", "fixed boil kettle", "other"]

DEFAULT_CONFIG = {
    "machine": {"preset": "ecm_classika_pid", "overrides": {"temp_offset_c": 0, "basket_g": 18}},
    "grinder": {"preset": "eureka_mignon_other", "overrides": {}},
    "kettle": KETTLES[0],
    "scale_g": "0.1",
    "water_note": "",
    "shots": [],
}


# -- small parsers -----------------------------------------------------------------------------------------------
def num(value, default=None):
    """Parse a number typed by a user; fall back to `default` when it is blank or not a number."""
    try:
        return float(str(value).strip().replace(",", "."))
    except (TypeError, ValueError):
        return default


def _nums(text):
    return [float(x) for x in re.findall(r"\d+(?:\.\d+)?", str(text or ""))]


def ratio_range(text):
    """'1:15 to 1:17' -> (15, 17); '1:2' -> (2, 2). Water grams per gram of coffee."""
    found = [float(x) for x in re.findall(r"1\s*:\s*(\d+(?:\.\d+)?)", str(text or ""))]
    if not found:
        return None
    return (min(found), max(found))


def span(text):
    """'25-30' -> (25, 30); '93' -> (93, 93)."""
    found = _nums(str(text or "").replace("+/-", " "))
    if not found:
        return None
    return (found[0], found[1]) if len(found) > 1 and "-" in str(text) else (found[0], found[0])


def altitude_band(masl):
    """Our own cut points, loosely based on WCR altitude triplets (1600/1300/1000) and grade cutoffs (about 1200)."""
    if masl is None:
        return None
    if masl < 1200:
        return "low"
    if masl < 1600:
        return "mid"
    return "high"


def _fmt_range(lo, hi, unit=""):
    f = lambda v: f"{v:g}"
    return f"{f(lo)}{unit}" if lo == hi else f"{f(lo)}-{f(hi)}{unit}"


def _setting(key, label, value, basis, confidence, sources=None, detail=""):
    return {"key": key, "label": label, "value": value, "basis": basis, "confidence": confidence,
            "sources": [s for s in (sources or []) if s], "detail": detail}


# -- equipment ----------------------------------------------------------------------------------------------------
def load_config(path=CONFIG_PATH):
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))
    try:
        saved = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return cfg
    for key, value in saved.items():
        if isinstance(value, dict) and isinstance(cfg.get(key), dict):
            cfg[key].update(value)
        else:
            cfg[key] = value
    return cfg


def save_config(cfg, path=CONFIG_PATH):
    Path(path).write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve(kb, cfg):
    """Merge each preset row with the user's overrides. Returns (machine, grinder)."""
    machine = dict(kb.find("equipment_machines", "id", cfg["machine"]["preset"]) or {})
    machine.update({k: v for k, v in cfg["machine"].get("overrides", {}).items() if v not in (None, "")})
    grinder = dict(kb.find("equipment_grinders", "id", cfg["grinder"]["preset"]) or {})
    grinder.update({k: v for k, v in cfg["grinder"].get("overrides", {}).items() if v not in (None, "")})
    return machine, grinder


def describe_equipment(machine, grinder):
    lines = [
        f"Machine: {machine.get('name', 'not set')} [{machine.get('confidence', 'none')}]",
        f"  boiler {machine.get('boiler_type') or 'n/s'}"
        + (f" {machine['boiler_l']} L" if machine.get("boiler_l") else "")
        + f", pump {machine.get('pump') or 'n/s'}, group {machine.get('group') or 'n/s'}, "
        f"temperature control: {machine.get('temp_control') or 'n/s'}, "
        f"pressure adjust: {machine.get('brew_pressure_adjust') or 'n/s'}, "
        f"pre-infusion: {machine.get('preinfusion') or 'n/s'}",
    ]
    if machine.get("conflict_note"):
        lines.append(f"  note: {machine['conflict_note']}")
    lines.append(f"Grinder: {grinder.get('name', 'not set')} [{grinder.get('confidence', 'none')}]")
    lines.append(
        f"  burrs {grinder.get('burr_mm') or 'n/s'} mm, adjustment {grinder.get('adjustment') or 'n/s'}, "
        f"finer = {grinder.get('finer_direction') or 'n/s'}, dial: {grinder.get('dial_marks') or grinder.get('dial_note') or 'n/s'}"
    )
    if grinder.get("conflict_note"):
        lines.append(f"  note: {grinder['conflict_note']}")
    return "\n".join(lines)


# -- the guide ----------------------------------------------------------------------------------------------------
class BrewGuide:
    def __init__(self, kb=None, cfg=None):
        self.kb = kb or Knowledge()
        self.cfg = cfg or load_config()

    # lookups the UI needs
    def regions(self, country):
        return [r for r in self.kb.table("origins_regions") if r.get("country") == country and r.get("region")]

    def region_altitude(self, country, region):
        row = next((r for r in self.regions(country) if r["region"] == region), None)
        if row and row.get("altitude_min_masl") is not None and row.get("altitude_max_masl") is not None:
            return (row["altitude_min_masl"], row["altitude_max_masl"], row)
        return None

    def equipment(self):
        return resolve(self.kb, self.cfg)

    # -- main entry --------------------------------------------------------------------------------------------
    def plan(self, profile):
        machine, grinder = self.equipment()
        method = profile.get("method", "espresso")
        roast = profile.get("roast", "Medium")
        masl = profile.get("altitude_masl")
        band = altitude_band(masl)
        settings, warnings, steps, questions = [], [], [], []

        self._coffee_notes(profile, band, settings, warnings)
        if method == "espresso":
            self._espresso(profile, roast, band, machine, grinder, settings, warnings, steps, questions)
        else:
            self._filter(profile, method, roast, band, grinder, settings, warnings, steps, questions)
        self._freshness(profile, method, warnings)

        if machine.get("confidence", "").startswith("unverified") and method == "espresso":
            questions.append("Your machine settings are generic category defaults. Confirm the details in My equipment.")
        conf = weakest([s["confidence"] for s in settings if s["confidence"]])
        return {"profile": profile, "settings": settings, "warnings": warnings, "steps": steps,
                "questions": questions, "confidence": conf, "machine": machine, "grinder": grinder,
                "targets": self._targets(settings)}

    @staticmethod
    def _targets(settings):
        out = {}
        for s in settings:
            if s["key"] in ("dose", "yield", "time", "temp", "pressure"):
                out[s["key"]] = s["value"]
        return out

    # coffee: variety, species, process, altitude
    def _coffee_notes(self, p, band, settings, warnings):
        masl = p.get("altitude_masl")
        country, region = p.get("country"), p.get("region")
        if masl is not None and (masl < 300 or masl > 2800):
            warnings.append(f"{masl} masl is outside the range seen in the data (about 300-2800); check the number.")
        if country and region:
            alt = self.region_altitude(country, region)
            if alt and masl is not None and not (alt[0] - 100 <= masl <= alt[1] + 100):
                warnings.append(f"{region}, {country} is listed at {alt[0]}-{alt[1]} masl; you entered {masl}. "
                                f"Check the label on the bag [{alt[2].get('confidence')}].")
        if band:
            text = {"low": "Below 1200 m: expect lower density and softer acidity.",
                    "mid": "1200-1600 m: mid-range density.",
                    "high": "1600 m and above: expect dense beans with higher acidity that resist extraction."}[band]
            settings.append(_setting("altitude", "Altitude band", f"{masl} masl ({band})",
                                     text + " The direction of the effect comes from studies (bean density and acidity rise with altitude); "
                                     "the size per 100 m was not retrieved, and the band cut points are this tool's own.", "inferred"))
        proc = p.get("process")
        if proc and proc != UNKNOWN:
            row = self.kb.find("processing_methods", "process", proc) or {}
            bits = [f"{k.replace('effect_', '')} {row[k]}" for k in ("effect_acidity", "effect_body", "effect_sweetness") if row.get(k)]
            settings.append(_setting("process", "Process", proc.replace("_", " "),
                                     "Cup effect: " + (", ".join(bits) or "n/s")
                                     + (f". Watch for: {row['defect_risks']}" if row.get("defect_risks") else ""),
                                     row.get("confidence") or "unverified", [row.get("source_url")]))
            if row.get("confidence") in ("low", "very low") or str(row.get("confidence", "")).startswith("unverified"):
                warnings.append(f"Process data for {proc.replace('_', ' ')} is {row.get('confidence')}: treat the cup expectation as a guess.")
        variety = p.get("variety")
        if variety and variety != UNKNOWN:
            row = next((r for r in self.kb.varieties if str(r["variety"]) == variety), None)
            if row:
                settings.append(_setting("variety", "Variety", variety.replace("_", " "),
                                         f"{row.get('group') or ''}; {row.get('cup_notes') or 'no cup notes'}; "
                                         f"WCR altitude bands (best / mid / low): {row.get('altitude_wcr_triplet_masl') or 'n/s'}",
                                         row.get("confidence") or "unverified", [row.get("source_url")]))
                if "robusta" in str(row.get("species", "")).lower() or "canephora" in str(row.get("species", "")).lower():
                    warnings.append("No sourced brew parameters exist for robusta; arabica settings are shown.")
        if p.get("species") == "robusta":
            warnings.append("No sourced brew parameters exist for robusta; arabica settings are shown.")

    def _freshness(self, p, method, warnings):
        days = p.get("days_since_roast")
        if days is None:
            return
        rules = {r["rule_key"]: r for r in self.kb.table("freshness_rules")}
        gassy = rules.get("gassy_fresh_days", {})
        rest = rules.get("espresso_rest_days", {}) if method == "espresso" else rules.get({
            "Light": "rest_days_light", "Medium": "rest_days_medium", "Dark": "rest_days_dark"}.get(p.get("roast"), ""), {})
        if gassy and days <= (gassy.get("value_max") or 4):
            warnings.append(f"{days:g} days off roast is very fresh: gassy, channel-prone, fast shots expected "
                            f"({gassy.get('value_min'):g}-{gassy.get('value_max'):g} days) [{gassy.get('confidence')}]. "
                            "Grind slightly finer than your usual until it settles.")
        elif rest and days < (rest.get("value_min") or 0):
            warnings.append(f"Rest window for this brew is {rest['value_min']:g}-{rest['value_max']:g} days [{rest.get('confidence')}]; "
                            f"you are at {days:g}.")
        whole = rules.get("whole_bean_fresh_days", {})
        if whole and days > 35:
            warnings.append(f"{days:g} days off roast: past the roughly 3 weeks SCA calls fresh plus the 2-4 week peak window "
                            "[inferred]. Older beans need a coarser grind (troubleshooting data).")

    # espresso -----------------------------------------------------------------------------------------------------
    def _espresso(self, p, roast, band, machine, grinder, settings, warnings, steps, questions):
        style = p.get("style", "normale")
        row = self.kb.find("espresso_styles", "style", STYLE_ROWS[style]) or {}
        baseline = self.kb.find("espresso_styles", "style", "normale_baseline") or {}
        breville = self.kb.find("espresso_styles", "style", "normale_breville") or {}
        basket = num(machine.get("basket_g"), 18)
        dose = p.get("dose_g") or basket
        src = row.get("source_url")

        settings.append(_setting("dose", "Dose", f"{dose:g} g", "Your basket's rated dose" if not p.get("dose_g") else "Your dose",
                                 "secondary", [baseline.get("source_url")],
                                 detail=f"Sourced doses: 18 g baseline (snippet) and 18-22 g (Breville). Stay inside the basket's rating."))
        if dose < 14 or dose > 22:
            warnings.append(f"{dose:g} g is outside the 18-22 g in the sources; the numbers below assume a standard basket.")

        rr = ratio_range(row.get("ratio")) or (2, 2)
        y_lo, y_hi = dose * rr[0], dose * rr[1]
        settings.append(_setting("yield", "Liquid in the cup", f"{_fmt_range(round(y_lo), round(y_hi), ' g')}",
                                 f"{style} ratio 1:{rr[0]:g}" + (f" to 1:{rr[1]:g}" if rr[1] != rr[0] else ""),
                                 row.get("confidence") or "snippet", [src],
                                 detail="Weigh the liquid on a scale, not the volume."))
        t = span(row.get("time_s")) or (25, 30)
        settings.append(_setting("time", "Shot time", f"{_fmt_range(t[0], t[1], ' s')}", f"{style} time window",
                                 row.get("confidence") or "snippet", [src],
                                 detail="Time is the signal you adjust the grind against."))

        self._temperature(p, roast, band, "espresso", machine, settings, warnings, steps)

        settings.append(_setting("pressure", "Pump pressure at the group", "9 bar (certified Italian espresso: 9 +/- 1)",
                                 "Breville and the Italian Espresso National Institute figures", "secondary",
                                 [breville.get("source_url"), "https://en.wikipedia.org/wiki/Espresso"]))
        adj = machine.get("brew_pressure_adjust")
        if adj and str(adj).lower() not in ("unknown", "no", "none", "n/s"):
            steps.append(f"Pressure: watch the gauge during a shot. If it is not near 9 bar, adjust at: {adj}. "
                         "The target bar value for the valve setting was not stated in the sources.")
        elif str(adj).lower() in ("no", "none"):
            warnings.append("You said brew pressure is not adjustable, so rely on grind, dose and temperature.")
        else:
            questions.append("Can you adjust brew pressure on your machine, and where?")
        pre = str(machine.get("preinfusion") or "")
        if pre.lower().startswith(("none", "no")) and "valve" not in pre.lower():
            steps.append("No pre-infusion on your machine, so there is no pre-infusion setting to give.")
        elif pre:
            steps.append(f"Pre-infusion: {pre}. No sourced pre-infusion time or pressure exists in the data, so none is given; "
                         "first stabilise grind, dose, puck preparation and yield (Coffeedant's advice before using flow control).")

        self._grind_espresso(p, roast, band, grinder, settings, steps, questions)
        water = self.kb.find("water_profiles", "profile", "third_wave_espresso_machine") or {}
        if water:
            settings.append(_setting("water", "Brewing water", f"TDS {water.get('tds_mgl')}, alkalinity {water.get('alkalinity_mgl_caco3')} as CaCO3",
                                     "Third Wave Water espresso machine profile", water.get("confidence") or "secondary",
                                     [water.get("source_url")]))
        steps.append("Order: grind and weigh the dose, distribute evenly (WDT), level the tamp, start the pump and timer together, "
                     "stop at the target liquid weight, then taste and record the shot in the Dial-in tab.")

    def _temperature(self, p, roast, band, method, machine, settings, warnings, steps):
        table = ROAST_TEMP.get(method, {})
        rng = span(table.get(roast, ""))
        if not rng:
            return
        lo, hi = rng
        if band == "high":
            pick, why = hi, "dense high-altitude beans: top of the roast's range"
        elif band == "low":
            pick, why = lo, "lower-altitude beans: bottom of the roast's range"
        else:
            pick, why = round((lo + hi) / 2), "mid altitude or unknown: middle of the roast's range"
        label = ROAST_TEMP_LABEL[method]
        sources = [(self.kb.find("espresso_styles", "style", "normale_baseline") or {}).get("source_url")] if method == "espresso" else \
                  [(self.kb.find("brew_targets", "method", "pour_over_v60_general") or {}).get("source_url")]
        settings.append(_setting("temp", "Water temperature", f"{pick:g} C",
                                 f"{roast} roast range {_fmt_range(lo, hi, ' C')} [{label}]"
                                 + (f"; picked {why} [inferred]" if lo != hi else ""),
                                 label if lo == hi else "inferred", sources))
        if method != "espresso":
            return
        ctl = str(machine.get("temp_control") or "").lower()
        step = num(machine.get("temp_step_c"), 1)
        offset = num(machine.get("temp_offset_c"), 0)
        if "pid" in ctl:
            setpoint = pick + offset
            settings.append(_setting("setpoint", "PID setting on your machine", f"{setpoint:g} C",
                                     f"target {pick:g} C {'+' if offset >= 0 else '-'} your measured offset {abs(offset):g} C; "
                                     f"your PID moves in {step:g} C steps",
                                     "inferred", [],
                                     detail="Whether the PID reads boiler or group-head water is not stated in the sources read. "
                                            "Measure water in the cup once and enter the offset under My equipment."))
            if machine.get("boiler_type") == "single_boiler":
                steps.append("Single boiler: pull the shot first, then steam. After steaming, cool and refill the boiler before the next shot "
                             "(Whole Latte Love). No sourced cooling flush volume or time exists, so judge by the PID reading returning to your setting.")
            steps.append("Let the machine and group warm fully before the first shot (official fast heat-up is about 11 minutes; "
                         "the full group warm-up time was not sourced), flush the group, then pull.")
        elif "flush" in ctl:
            settings.append(_setting("setpoint", "Temperature control", "cooling flush",
                                     "Heat exchanger: temperature is set by how long you flush before the shot. No sourced flush times.",
                                     "unverified-bg", []))
            warnings.append("No sourced flush time for a heat exchanger machine: measure the water temperature and adjust the flush.")
        elif ctl in ("none", ""):
            warnings.append(f"Your machine cannot set brew temperature, so the {pick:g} C target cannot be applied. "
                            "Use roast level and grind to compensate.")

    def _grind_espresso(self, p, roast, band, grinder, settings, steps, questions):
        g = self.kb.find("grind_sizes", "method", "espresso_vendor") or {}
        alt = self.kb.find("grind_sizes", "method", "espresso") or {}
        settings.append(_setting("grind_target", "Grind target", f"{g.get('grind_um_min')}-{g.get('grind_um_max')} um",
                                 f"Vendor figure; another chart says {alt.get('grind_um_min')}-{alt.get('grind_um_max')} um. "
                                 "No peer-reviewed espresso micron standard was found. Use shot time, not microns, to set the grinder.",
                                 g.get("confidence") or "snippet", [g.get("source_url")]))
        finer = grinder.get("finer_direction") or "unknown"
        kind = str(grinder.get("adjustment") or "")
        dial = grinder.get("dial_note") or grinder.get("dial_marks") or "not sourced"
        text = (f"{grinder.get('name', 'your grinder')}: {kind or 'adjustment n/s'}; finer = {finer}; dial scale: {dial}")
        settings.append(_setting("grinder", "Grinder setting", "no absolute number is given",
                                 text + ". No sourced starting position exists for this grinder, so this tool gives a direction "
                                 "and a method, never an invented dial number.", "unverified-bg" if not grinder.get("confidence") else grinder["confidence"],
                                 [s.strip() for s in str(grinder.get("source_url") or "").split("|") if s.strip()]))
        steps.append("Starting the grind: use your last good espresso setting. With none, start at a fine table-salt texture (Breville) "
                     "and move finer or coarser until 18 g gives about 36 g in 25-30 s.")
        if band == "high":
            steps.append("High-altitude, dense beans usually need a finer grind or a longer shot to reach the same extraction [inferred].")
        if "stepless" in kind.lower():
            steps.append("Stepless grinder: move in the smallest visible mark of your dial and re-time the shot. "
                         "The size of one mark in microns is not sourced for this grinder.")
        if "unknown" in finer.lower() or "assumed" in finer.lower():
            questions.append("Which way is finer on your grinder? Confirm and enter it under My equipment.")

    # filter methods ------------------------------------------------------------------------------------------------
    def _filter(self, p, method, roast, band, grinder, settings, warnings, steps, questions):
        s = self.kb.summary(method, roast)
        dose = p.get("dose_g") or 20
        settings.append(_setting("dose", "Dose", f"{dose:g} g", "Your dose", "secondary", []))
        rr = ratio_range(s["ratio"]) if s["ratio"] else None
        if rr:
            lo, hi = dose * rr[0], dose * rr[1]
            settings.append(_setting("yield", "Water", f"{_fmt_range(round(lo), round(hi), ' g')}",
                                     f"ratio {s['ratio']}", "secondary", s["sources"]))
        else:
            settings.append(_setting("yield", "Water", "not sourced", "No sourced ratio for this method.", "none"))
        if s["time_s"]:
            settings.append(_setting("time", "Total time", f"{s['time_s']} s", "method target window", "secondary", s["sources"]))
        if method in ROAST_TEMP:
            self._temperature(p, roast, band, method, {}, settings, warnings, [])
        elif s["temp_c"]:
            settings.append(_setting("temp", "Water temperature", f"{s['temp_c']} C", "method target", "secondary", s["sources"]))
        else:
            settings.append(_setting("temp", "Water temperature", "not sourced", "No sourced temperature for this method.", "none"))
        settings.append(_setting("pressure", "Pressure", "not applicable", "Immersion or gravity method, so no pump pressure", "inferred"))
        g = s["grind_um"]
        grind_row = self.kb.find("grind_sizes", "method", GRIND_KEY.get(method, ""))
        settings.append(_setting("grind_target", "Grind target", g or "not sourced",
                                 "Honest Coffee Guide chart; conflicts with the developer brief value" if method == "pour_over" else "Method chart",
                                 (grind_row or {}).get("confidence") or "none", [(grind_row or {}).get("source_url")]))
        settings.append(_setting("grinder", "Grinder setting", "no absolute number is given",
                                 f"{grinder.get('name', 'your grinder')}: finer = {grinder.get('finer_direction') or 'unknown'}. "
                                 "Dial from the drawdown time and the taste (see the troubleshooting rows).", "unverified-bg"))
        if s["water"]:
            settings.append(_setting("water", "Brewing water", s["water"], "Third Wave Water profile for this roast", "secondary", s["sources"]))
        bloom = (self.kb.find("brew_targets", "method", "pour_over_v60_general") or {}).get("bloom") if method == "pour_over" else None
        if bloom:
            steps.append(f"Bloom: {bloom}.")
        kettle = str(self.cfg.get("kettle") or "")
        if kettle.startswith("fixed"):
            warnings.append("A fixed-boil kettle cannot hit the sourced temperature range for darker roasts; let the water rest and measure it.")
        steps.append("Rinse the filter, bloom, pour in stages, then taste and use the Troubleshoot rows to adjust one thing at a time.")
        for m in s["missing"]:
            warnings.append(f"No sourced {m.replace('_', ' ')} for {METHOD_LABELS.get(method, method)}.")

    # -- dial-in --------------------------------------------------------------------------------------------------
    @staticmethod
    def calibrate(points):
        """Seconds of shot time per dial unit, measured from the user's own shots.

        points: dicts with dial, time_s, dose_g. Uses the two most recent shots with different dial readings and
        about the same dose. Returns None until there are two such shots.
        """
        usable = [p for p in points if num(p.get("dial")) is not None and num(p.get("time_s")) is not None]
        for i in range(len(usable) - 1, 0, -1):
            a, b = usable[i], usable[i - 1]
            if num(a["dial"]) == num(b["dial"]):
                continue
            if abs(num(a.get("dose_g"), 0) - num(b.get("dose_g"), 0)) > 0.5:
                continue
            slope = (num(a["time_s"]) - num(b["time_s"])) / (num(a["dial"]) - num(b["dial"]))
            if abs(slope) >= 0.1:
                return {"s_per_unit": slope, "from": (b, a)}
        return None

    def advise(self, plan, shot, history=None):
        """Turn a pulled espresso shot into the next single adjustment.

        history: earlier shots, used to measure how many seconds one dial unit moves this grinder.
        """
        machine, grinder = plan["machine"], plan["grinder"]
        dose, out, t = shot.get("dose_g"), shot.get("yield_g"), shot.get("time_s")
        taste = shot.get("taste", "balanced / sweet")
        targets = {s["key"]: s for s in plan["settings"]}
        style = plan["profile"].get("style", "normale")
        tgt_t = span(targets["time"]["value"].replace(" s", "")) if "time" in targets else (25, 30)
        finer = str(grinder.get("finer_direction") or "unknown").split()[0].lower()
        coarser = {"clockwise": "anticlockwise", "anticlockwise": "clockwise", "counterclockwise": "clockwise"}.get(finer)
        kind = str(grinder.get("adjustment", "")).lower()
        stepped = "stepped" in kind and "stepless" not in kind
        unit = "setting(s)" if stepped else "smallest dial mark(s)"
        way = lambda direction: f" ({direction})" if direction else ""
        notes = []

        def row_for(symptom_word, band_time):
            for r in self.kb.table("troubleshooting"):
                if r.get("method") != "espresso" or symptom_word not in (r.get("symptom") or ""):
                    continue
                band = self._time_band(r.get("time_or_flow"))
                if band and band[0] <= band_time <= band[1]:
                    return r
            return None

        key = taste.split()[0]
        word = {"sour": "sour", "balanced": "balanced", "bitter": "bitter", "burnt": "ashy", "weak": "sour", "muddy": "bitter"}[key]
        r = row_for(word, t) if t is not None else None
        action, diag, conf, src = "", "", "inferred", []
        if r:
            action, diag, conf, src = r["action"], r["diagnosis"], r.get("confidence") or "secondary", [r.get("source_url")]
        elif key == "balanced":
            diag, action = "balanced cup outside the usual time window", "keep the settings: taste wins over time. Record this dial position and recipe"
        elif key == "sour" and t is not None and t > tgt_t[1]:
            r2 = self.kb.find("troubleshooting", "diagnosis", "channeling or uneven extraction") or {}
            diag = "sour although the shot ran long: uneven extraction or low water temperature [inferred]"
            action = "check distribution (WDT) and level the tamp before touching the grind; if the puck is even, raise temperature one step"
            src = [r2.get("source_url")]
        else:
            diag, action = "no matching row in the data for this combination of time and taste", "change one variable and re-taste"

        dial = ""
        a = action.lower()
        n = re.search(r"(\d)(?:-(\d))?\s+setting", a)
        steps_text = (n.group(1) + (f"-{n.group(2)}" if n.group(2) else "")) if n else "1"
        if "finer" in a and "grind" in a:
            dial = f"Move the grinder {steps_text} {unit} finer{way(finer if finer != 'unknown' else '')}."
        elif "coarser" in a and "grind" in a:
            dial = f"Move the grinder {steps_text} {unit} coarser{way(coarser)}."
        if dial and not stepped:
            dial += (" The sources count 'settings' on stepped grinders; on a stepless dial treat one smallest mark as one setting, "
                     "re-time, and tell me how much it moved the time.")

        temp_hint = ""
        if key == "sour" and t is not None and tgt_t[0] <= t <= tgt_t[1]:
            temp_hint = f"If yield change does not fix it, raise the PID setting one step ({machine.get('temp_step_c') or 1} C) [inferred]."
        elif key in ("bitter", "burnt") and t is not None and tgt_t[0] <= t <= tgt_t[1]:
            temp_hint = f"If the lower yield does not fix it, lower the PID setting one step ({machine.get('temp_step_c') or 1} C) [inferred]."

        if dose and out:
            ratio = out / dose
            want = ratio_range(self.kb.find("espresso_styles", "style", STYLE_ROWS.get(style, "normale_baseline")).get("ratio")) or (2, 2)
            notes.append(f"Ratio 1:{ratio:.2f} (target 1:{want[0]:g}" + (f" to 1:{want[1]:g}" if want[1] != want[0] else "") + ").")
            if ratio < want[0] - 0.3 or ratio > want[1] + 0.3:
                notes.append("Your yield is off target: stop the shot at the target weight before judging taste.")
        if t is not None:
            where = "inside" if tgt_t[0] <= t <= tgt_t[1] else ("faster than" if t < tgt_t[0] else "slower than")
            notes.append(f"Time {t:g} s is {where} the {tgt_t[0]:g}-{tgt_t[1]:g} s window.")
        days = plan["profile"].get("days_since_roast")
        if days is not None and days <= 4 and t is not None and t < tgt_t[0]:
            notes.append("Fresh beans: grind finer than your dialled-in setting (troubleshooting data).")

        calibration = ""
        cal = self.calibrate(list(history or []) + [shot])
        dial_now = num(shot.get("dial"))
        if cal and dial_now is not None and t is not None and not (tgt_t[0] <= t <= tgt_t[1]) and (dial or "grind" in a):
            goal = (tgt_t[0] + tgt_t[1]) / 2
            new_dial = dial_now + (goal - t) / cal["s_per_unit"]
            b, a2 = cal["from"]
            calibration = (f"Measured from your shots: dial {num(b['dial']):g} gave {num(b['time_s']):g} s and dial {num(a2['dial']):g} gave "
                           f"{num(a2['time_s']):g} s, so about {cal['s_per_unit']:+.1f} s per dial unit. To reach {goal:g} s, try dial about "
                           f"{new_dial:.1f} (this assumes the same dose, coffee and temperature) [measured from your shots, inferred]. "
                           + ("On your dial, LOWER numbers give longer shots, so lower = finer." if cal["s_per_unit"] < 0
                              else "On your dial, HIGHER numbers give longer shots, so higher = finer."))
        elif dial and dial_now is None:
            calibration = ("Enter your dial reading with each shot. After two shots at different readings I can measure how many seconds "
                           "one dial unit moves your grinder and give you a number to dial to.")
        return {"diagnosis": diag, "action": action, "dial": dial, "temp_hint": temp_hint, "notes": notes,
                "calibration": calibration,
                "confidence": conf, "sources": [s for s in src if s], "one_change": "Change one thing per shot, then re-taste [inferred]."}

    @staticmethod
    def _time_band(text):
        t = str(text or "").lower()
        m = re.match(r"under (\d+)", t)
        if m:
            return (0, float(m.group(1)) - 0.01)
        m = re.match(r"over (\d+)", t)
        if m:
            return (float(m.group(1)) + 0.01, 999)
        m = re.match(r"(\d+)-(\d+) s", t)
        if m:
            return (float(m.group(1)), float(m.group(2)))
        return None


def render(plan):
    """Plain-text version of a plan, used by the chat box and tests."""
    lines = []
    for s in plan["settings"]:
        lines.append(f"{s['label']}: {s['value']}  [{s['confidence']}]\n    {s['basis']}")
    for w in plan["warnings"]:
        lines.append(f"Warning: {w}")
    for q in plan["questions"]:
        lines.append(f"Question: {q}")
    return "\n".join(lines)
