"""Local knowledge engine for Coffee Flavourlab. Reads data/coffee and answers questions. No UI code."""
import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data" / "coffee"

ROASTS = ["Light", "Medium", "Dark"]
ROAST_WORDS = {"light": "Light", "medium": "Medium", "dark": "Dark"}
METHOD_ALIASES = {
    "pour_over": ["v60", "pour over", "pour-over", "pourover", "kalita", "origami"],
    "espresso": ["espresso", "shot", "ristretto", "lungo", "doppio", "normale"],
    "aeropress": ["aeropress", "aero press"],
    "french_press": ["french press"],
    "cold_brew": ["cold brew", "cold drip", "toddy"],
    "siphon": ["siphon", "vac pot", "vacuum pot"],
    "chemex": ["chemex"],
    "moka": ["moka", "stovetop"],
}
METHODS = list(METHOD_ALIASES)

TARGET_KEY = {
    "pour_over": "pour_over_v60_general",
    "aeropress": "aeropress_hoffmann",
    "french_press": "french_press_hoffmann",
    "cold_brew": "cold_brew",
    "siphon": "siphon",
    "chemex": "chemex",
}
GRIND_KEY = {
    "pour_over": "v60",
    "espresso": "espresso_vendor",
    "aeropress": "aeropress",
    "french_press": "french_press",
    "cold_brew": "cold_brew",
    "siphon": "siphon",
    "moka": "moka_pot",
}
BRIEF_GRIND_KEY = {
    "pour_over": "brief_v60",
    "espresso": "brief_espresso",
    "aeropress": "brief_aeropress",
    "french_press": "brief_french_press",
    "cold_brew": "brief_cold_brew",
    "chemex": "brief_chemex",
    "moka": "brief_moka_pot",
}
ROAST_TEMP = {
    "pour_over": {"Light": "95-96", "Medium": "93-94", "Dark": "91-93"},
    "espresso": {"Light": "94-96", "Medium": "93", "Dark": "90-92"},
}
ROAST_TEMP_LABEL = {"pour_over": "secondary", "espresso": "snippet"}
WATER_KEY = {
    "Light": "third_wave_classic_light_roast",
    "Medium": "third_wave_medium_roast",
    "Dark": "third_wave_dark_roast",
    "espresso": "third_wave_espresso_machine",
}
ROAST_CUP = {
    "Light": "brighter acidity, lighter body (inferred)",
    "Medium": "balanced sweetness; caramel and chocolate notes (inferred)",
    "Dark": "lower acidity, heavier body, roasty or bitter notes (inferred)",
}
RANK = {
    "primary": 5, "secondary": 4, "medium": 3, "snippet": 3, "low": 2, "inferred": 2,
    "conflict": 2, "very low": 1, "unverified": 1, "unverified-bg": 1, "unverified-brief": 1, "none": 0,
}
MISSING_DRINKS = ["affogato", "breve", "red eye", "gibraltar", "galao", "cafe au lait"]
TROUBLE_WORDS = [
    "sour", "bitter", "channel", "fast", "slow", "stall", "crater", "bloom", "watery", "weak",
    "muddy", "drift", "crema", "thin", "dry", "burnt", "ashy", "astringent", "gush", "clump",
]
MILK_WORDS = ["milk", "steam", "froth", "foam", "oat", "soy", "almond", "dairy"]
WATER_WORDS = ["water", "tds", "alkalinity", "hardness", "mineral"]
GRIND_WORDS = ["grind", "micron", "um", "click"]
FRESH_WORDS = ["fresh", "degas", "rest", "stale", "storage", "shelf"]
CUP_WORDS = ["cva", "cupping", "affective", "descriptive", "score"]
COMPOUND_WORDS = ["compound", "aroma", "furaneol", "pyrazine", "guaiacol", "linalool", "furfurylthiol"]
BITTER_CHEM_WORDS = ["bitterness", "bitter compound", "quinide"]
ODORANT_WORDS = ["odorant", "key aroma", "robusta aroma", "arabica aroma"]
DEFECT_WORDS = ["defect", "off-flavour", "off-flavor", "off flavour", "off flavor", "rio", "tca", "musty", "peasy", "medicinal"]
CHEM_WORDS = {"espresso_sensory_attributes": ["attribute", "sensory profile"], "aroma_precursors": ["precursor", "carotenoid"],
              "furfurylthiol": ["furfurylthiol", "stale coffee"], "bitterness": BITTER_CHEM_WORDS}
HEALTH_WORDS = {
    "caffeine": ["half-life", "half life", "withdrawal", "pregnant", "pregnancy", "how much caffeine", "caffeine limit",
                 "too much caffeine", "safe caffeine", "caffeine content"],
    "sleep": ["sleep", "sleeping", "insomnia", "bedtime", "before bed"],
    "blood_pressure": ["blood pressure", "hypertension"],
    "cancer": ["cancer", "carcinogen", "carcinogenic", "very hot drink", "very hot coffee", "too hot to drink",
               "drinking temperature"],
}
ALT_WORDS = ["altitude","masl", "metre", "meter", "elevation", "grade", "shb", "shg"]
PRODUCTION_WORDS = ["production", "bags", "how much", "volume", "harvest"]
AUCTION_WORDS = ["auction", "price", "lot", "record"]
STOP = {"about", "which", "what", "tell", "give", "show", "should", "could", "would", "there", "their", "with", "from"}

HELP = (
    "Ask about:\n"
    "- brew settings: 'espresso dark roast', 'v60 medium', 'aeropress light'\n"
    "- recipes: 'v60 recipe', 'aeropress recipe'\n"
    "- problems: 'sour and fast shot', 'bitter pour over', 'channeling'\n"
    "- milk and drinks: 'oat milk temperature', 'cappuccino', 'flat white'\n"
    "- water, grind, freshness, decaf, processing (washed, honey, anaerobic)\n"
    "- origins: 'ethiopia altitude', 'colombia production', 'kenya auction'\n"
    "- varieties and species: 'geisha', 'sl28', 'robusta'\n"
    "- cupping: 'cva scores', 'flavor wheel', 'aroma compounds'\n"
    "- flavour chemistry: 'coffee bitterness', 'key odorants', 'rio defect', 'aroma precursors'\n"
    "- caffeine and health, if that table is installed: 'caffeine and sleep', 'coffee and blood pressure', 'coffee cancer'\n"
    "Answers come from the local data files and show their confidence label, plus a source link where there is one."
)


def _has(text, phrase):
    return re.search(r"(?<![a-z])" + re.escape(phrase) + r"(?:s|es)?(?![a-z])", text) is not None


def rank(label):
    if label in RANK:
        return RANK[label]
    if label and str(label).startswith("unverified"):
        return 1
    return 3 if label else 0


def weakest(labels):
    present = [label for label in labels if label]
    return min(present, key=rank) if present else "none"


def _fmt(row, fields):
    parts = [f"{f}: {row[f]}" for f in fields if row.get(f) not in (None, "", [])]
    line = "- " + " | ".join(parts)
    conf = row.get("confidence") or row.get("mapping_confidence") or ""
    if conf:
        line += f"  [{conf}]"
    url = row.get("source_url") or ""
    if url:
        line += f"\n    {url}"
    return line


def _vname(row):
    return re.sub(r"\(.*?\)", "", str(row["variety"])).strip().lower().replace("_", " ")


class Knowledge:
    def __init__(self, data_dir=DATA_DIR):
        self.data = {}
        for path in sorted(Path(data_dir).glob("*.json")):
            try:
                self.data[path.stem] = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                self.data[path.stem] = []
        self.processes = [r["process"] for r in self.table("processing_methods") if r.get("process")]
        self.countries = sorted({r["country"] for r in self.table("origins_regions") if r.get("country")})
        self.drinks = [r["drink"] for r in self.table("espresso_drinks") if r.get("drink")]
        self.varieties = []
        for name in ("varieties_wcr", "varieties_secondary"):
            for r in self.table(name):
                self.varieties.append({**r, "source_set": name})

    def table(self, name):
        return self.data.get(name) or []

    def health_lines(self, topics):
        """Current guidance first, then older findings. Replaced and unclear rows are left out of answers."""
        rows = self.table("coffee_health")
        if topics:
            rows = [r for r in rows if r.get("topic") in topics]
        current = [r for r in rows if r.get("status") == "current-guidance"]
        older = [r for r in rows if r.get("status") not in ("current-guidance", "replaced", "unclear")] if topics else []
        if not current and not older:
            return []
        fields = ["finding", "value", "population", "evidence", "status", "status_note"]
        lines = [_fmt(r, fields) for r in current]
        if topics - {r.get("topic") for r in current}:
            lines.append("- No current official guidance has been checked for: "
                         + ", ".join(sorted(topics - {r.get("topic") for r in current})).replace("_", " "))
        if older:
            lines.append("- Older research follows. 'not-rechecked' means it was not compared with current evidence.")
            lines += [_fmt(r, fields) for r in older]
        if not topics:
            lines.append("- For older research, ask about caffeine limits, sleep, blood pressure or cancer.")
        return lines

    def find(self, name, field, value):
        return next((r for r in self.table(name) if r.get(field) == value), None)

    def find_all(self, name, pred):
        return [r for r in self.table(name) if pred(r)]

    @staticmethod
    def _part(value, label, url):
        if value in (None, ""):
            return (None, "none", None)
        return (value, label, url)

    def _method_parts(self, method, roast):
        parts = {key: (None, "none", None) for key in ("ratio", "time_s", "temp_c", "grind_um", "water")}
        if method == "espresso":
            row = self.find("espresso_styles", "style", "normale_baseline") or {}
            label, url = row.get("confidence"), row.get("source_url")
            parts["ratio"] = self._part(row.get("ratio"), label, url)
            parts["time_s"] = self._part(row.get("time_s"), label, url)
            parts["temp_c"] = self._part(ROAST_TEMP["espresso"].get(roast), ROAST_TEMP_LABEL["espresso"], url)
        elif method in TARGET_KEY:
            row = self.find("brew_targets", "method", TARGET_KEY[method]) or {}
            label, url = row.get("confidence"), row.get("source_url")
            parts["ratio"] = self._part(row.get("ratio"), label, url)
            parts["time_s"] = self._part(row.get("time_s"), label, url)
            if method in ROAST_TEMP and roast in ROAST_TEMP[method]:
                parts["temp_c"] = self._part(ROAST_TEMP[method][roast], ROAST_TEMP_LABEL[method], url)
            else:
                parts["temp_c"] = self._part(row.get("temp_c"), label, url)
        grind = None
        if method in GRIND_KEY:
            grind = self.find("grind_sizes", "method", GRIND_KEY[method])
        if grind is None and method in BRIEF_GRIND_KEY:
            grind = self.find("grind_sizes", "method", BRIEF_GRIND_KEY[method])
        if grind:
            text = f"{grind.get('grind_um_min')}-{grind.get('grind_um_max')} um"
            parts["grind_um"] = self._part(text, grind.get("confidence"), grind.get("source_url"))
        water = self.find("water_profiles", "profile", WATER_KEY["espresso" if method == "espresso" else roast]) or {}
        if water:
            text = f"TDS {water.get('tds_mgl')}, alkalinity {water.get('alkalinity_mgl_caco3')} as CaCO3"
            if water.get("minerals_or_recipe"):
                text += f" ({water['minerals_or_recipe']})"
            parts["water"] = self._part(text, water.get("confidence"), water.get("source_url"))
        return parts

    def summary(self, method, roast="Medium"):
        parts = self._method_parts(method, roast)
        present = [label for value, label, _ in parts.values() if value is not None]
        return {
            "method": method,
            "roast": roast,
            "process": "",
            "ratio": parts["ratio"][0],
            "time_s": parts["time_s"][0],
            "temp_c": parts["temp_c"][0],
            "grind_um": parts["grind_um"][0],
            "water": parts["water"][0],
            "cup": ROAST_CUP[roast],
            "missing": [key for key, (value, _, _) in parts.items() if value is None],
            "confidence": weakest(present),
            "sources": sorted({url for value, _, url in parts.values() if value is not None and url}),
        }

    def combo(self, method, roast, process=None):
        s = self.summary(method, roast)
        conf = s["confidence"]
        cup = s["cup"]
        sources = list(s["sources"])
        if process:
            pr = self.find("processing_methods", "process", process)
            if pr:
                cup = (
                    f"{process} ({pr.get('effect_acidity') or 'n/s'} acidity, "
                    f"{pr.get('effect_body') or 'n/s'} body, "
                    f"{pr.get('effect_sweetness') or 'n/s'} sweetness); roast: {cup}"
                )
                conf = weakest([conf, pr.get("confidence")])
                if pr.get("source_url"):
                    sources.append(pr["source_url"])
        s.update(process=process or "", cup=cup, confidence=conf, sources=sorted(set(sources)))
        return s

    def grid(self):
        processes = [None] + self.processes
        return [self.combo(m, r, p) for m in METHODS for r in ROASTS for p in processes]

    def recipes(self, method):
        return self.find_all("brew_recipes", lambda r: r.get("method") == method)

    def origins(self, country=None, process=None):
        def keep(r):
            if country and country.lower() not in (r.get("country") or "").lower():
                return False
            if process and process.lower() not in (r.get("processing") or "").lower():
                return False
            return True
        return [r for r in self.table("origins_regions") if keep(r)]

    def _summary_line(self, s):
        vals = [
            f"ratio {s['ratio'] or 'not sourced'}",
            f"temp {s['temp_c'] or 'not sourced'} C",
            f"time {s['time_s'] or 'not sourced'} s",
            f"grind {s['grind_um'] or 'not sourced'}",
            f"water {s['water'] or 'not sourced'}",
        ]
        line = f"- {s['method']}, {s['roast']} roast: " + "; ".join(vals) + f"  [{s['confidence']}]"
        if s["missing"]:
            line += f"\n    missing: {', '.join(s['missing'])}"
        for url in s["sources"][:3]:
            line += f"\n    {url}"
        return line

    def answer(self, question):
        text = (question or "").lower().replace("gesha", "geisha")
        q = " " + re.sub(r"[^a-z0-9%./\- ]+", " ", text) + " "
        if not q.strip() or _has(q, "help"):
            return HELP
        sections = []

        def add(title, lines):
            if lines:
                sections.append(f"== {title} ==\n" + "\n".join(lines))

        methods = [m for m, aliases in METHOD_ALIASES.items() if any(_has(q, a) for a in aliases)]
        roasts = [ROAST_WORDS[w] for w in ROAST_WORDS if _has(q, w)]

        trouble = [w for w in TROUBLE_WORDS if _has(q, w)]
        if trouble:
            rows = self.find_all(
                "troubleshooting",
                lambda r: any(w in (r.get("symptom") or "") or w in (r.get("diagnosis") or "") for w in trouble)
                and (not methods or r.get("method") in methods),
            )
            add("Troubleshooting", [_fmt(r, ["method", "symptom", "time_or_flow", "diagnosis", "action"]) for r in rows[:10]])

        if methods:
            lines = [self._summary_line(self.summary(m, r)) for m in methods for r in (roasts or ROASTS)]
            add("Brew settings", lines)
            if _has(q, "recipe") or _has(q, "pour") or _has(q, "dose"):
                rows = [r for m in methods for r in self.recipes(m)][:8]
                add("Named recipes", [_fmt(r, ["name", "author", "dose_g", "water_g", "ratio", "temp_c", "grind",
                                               "bloom_g", "bloom_s", "pours_raw", "total_time_s"]) for r in rows])

        drink_hits = [d for d in self.drinks if _has(q, d.replace("_", " "))]
        if drink_hits:
            rows = [r for r in self.table("espresso_drinks") if r.get("drink") in drink_hits]
            add("Drinks", [_fmt(r, ["drink", "espresso_shots", "espresso_ml", "milk_ml", "foam_cm", "cup_ml",
                                    "ratio_espresso_to_milk", "notes"]) for r in rows])
        missing = [m for m in MISSING_DRINKS if _has(q, m)]
        if missing:
            add("Drinks with no sourced numbers", [f"- {m}: no numeric source in the data. Do not populate." for m in missing])

        if any(_has(q, w) for w in MILK_WORDS):
            specific = [k for k in ("oat", "soy", "almond", "dairy") if _has(q, k)]
            rows = [r for r in self.table("milk_temps") if not specific or any(k in r["milk"] for k in specific)]
            add("Milk", [_fmt(r, ["milk", "target_temp_c", "max_temp_c", "note"]) for r in rows])

        if any(_has(q, w) for w in WATER_WORDS):
            add("Brewing water", [_fmt(r, ["profile", "tds_mgl", "alkalinity_mgl_caco3", "calcium_hardness_mgl_caco3",
                                           "total_hardness_gh_mgl_caco3", "ph", "minerals_or_recipe"])
                                  for r in self.table("water_profiles")])
            if _has(q, "convert") or _has(q, "mg") or _has(q, "ppm"):
                add("Conversions", [_fmt(r, ["item", "formula", "factor", "notes"]) for r in self.table("water_conversions")])

        if any(_has(q, w) for w in GRIND_WORDS):
            keys = set()
            for m in methods:
                keys.update(k for k in (GRIND_KEY.get(m), BRIEF_GRIND_KEY.get(m)) if k)
            rows = [r for r in self.table("grind_sizes") if not keys or r.get("method") in keys]
            add("Grind size (microns)", [_fmt(r, ["method", "grind_um_min", "grind_um_max", "range_type", "notes"])
                                         for r in rows[:12]])

        if any(_has(q, w) for w in FRESH_WORDS):
            add("Freshness and rest", [_fmt(r, ["rule_key", "value_min", "value_max", "unit", "applies_to", "notes"])
                                       for r in self.table("freshness_rules")])

        if _has(q, "decaf"):
            add("Decaf", [_fmt(r, ["method", "steps", "caffeine_removed_pct_claimed", "us_label_threshold_pct", "notes"])
                          for r in self.table("decaf_methods")])

        proc_rows = [r for r in self.table("processing_methods") if _has(q, r["process"].split("_")[0])]
        if proc_rows:
            add("Processing", [_fmt(r, ["process", "steps_summary", "fermentation_hours", "drying_days_typical",
                                        "effect_acidity", "effect_body", "effect_sweetness", "funk_risk", "defect_risks"])
                               for r in proc_rows])

        countries_hit = [c for c in self.countries if _has(q, c.lower())]
        var_hits = [r for r in self.varieties if _has(q, _vname(r))]
        if not var_hits:
            var_hits = [r for r in self.varieties
                        if len(_vname(r).split()) > 1 and len(_vname(r).split()[0]) >= 5
                        and _has(q, _vname(r).split()[0]) and _vname(r).split()[0] not in [c.lower() for c in self.countries]]
        if var_hits:
            add("Varieties", [_fmt(r, ["variety", "species", "group", "origin_country", "altitude_wcr_triplet_masl",
                                       "rust_resistance", "cup_notes", "coffee_review_avg_score"]) for r in var_hits[:8]])

        species = [r for r in self.table("species") if r.get("common_name") and _has(q, r["common_name"].lower())]
        if species:
            add("Species", [_fmt(r, ["species", "common_name", "ploidy_2n", "caffeine_pct_min", "caffeine_pct_max",
                                     "share_world_production", "cup_profile", "rust_disease_note"]) for r in species])

        for country in countries_hit[:3]:
            if any(_has(q, w) for w in ALT_WORDS):
                add(f"{country}: altitude and grades",
                    [_fmt(r, ["region", "altitude_min_masl", "altitude_max_masl", "processing", "flavor_notes"])
                     for r in self.origins(country)[:6]]
                    + [_fmt(r, ["grade", "elevation_masl_min", "elevation_masl_max", "note"])
                       for r in self.table("altitude_grades") if r.get("country", "").lower() == country.lower()])
            if any(_has(q, w) for w in PRODUCTION_WORDS):
                rows = sorted([r for r in self.table("production_60kg") if r.get("country", "").lower() == country.lower()],
                              key=lambda r: str(r.get("production_year")), reverse=True)[:4]
                add(f"{country}: production", [_fmt(r, ["production_year", "total_60kg_bags", "arabica_60kg_bags",
                                                        "robusta_60kg_bags", "conflict_note"]) for r in rows])
            if any(_has(q, w) for w in AUCTION_WORDS):
                rows = [r for r in self.table("auctions_origins") if r.get("country", "").lower() == country.lower()]
                add(f"{country}: auctions", [_fmt(r, ["auction", "year", "lot_or_variety", "process",
                                                      "price_usd_per_lb", "price_usd_per_kg", "conflict_note"])
                                             for r in rows[:6]])
            if not any(_has(q, w) for w in ALT_WORDS + PRODUCTION_WORDS + AUCTION_WORDS):
                add(f"{country}: origin regions", [_fmt(r, ["region", "altitude_min_masl", "altitude_max_masl", "varieties",
                                                            "processing", "harvest_months", "flavor_notes", "conflict_note"])
                                                   for r in self.origins(country)[:6]])

        if not countries_hit and any(_has(q, w) for w in AUCTION_WORDS + ["geisha"]):
            add("Gesha and Panama auctions", [_fmt(r, ["year", "estate", "process", "price_usd_per_kg",
                                                       "price_usd_per_lb", "score", "conflict_note"])
                                              for r in self.table("gesha_auctions")[:8]])

        if any(_has(q, w) for w in CUP_WORDS):
            add("Cupping (CVA)", [_fmt(r, ["assessment", "item", "scale_min", "scale_max", "anchor_or_unit", "notes"])
                                  for r in self.table("cva_scales")[:12]])

        if _has(q, "wheel") or _has(q, "descriptor"):
            tokens = [t for t in re.findall(r"[a-z]{4,}", q) if t not in {"wheel", "flavor", "flavour", "descriptor", "what", "does", "show", "give", "sca"}]
            rows = [r for r in self.table("flavor_wheel")
                    if any(t in f"{r.get('wheel_tier2') or ''} {r.get('wheel_tier3') or ''}".lower() for t in tokens)]
            if rows:
                add("Flavour wheel", [_fmt(r, ["wheel_tier1", "wheel_tier2", "wheel_tier3", "mapping_confidence"]) for r in rows[:12]])
            else:
                tier1 = sorted({r["wheel_tier1"] for r in self.table("flavor_wheel")})
                add("Flavour wheel", ["- Families: " + ", ".join(tier1)])

        if any(_has(q, w) for w in COMPOUND_WORDS):
            tokens = re.findall(r"[a-z]{4,}", q)
            rows = [r for r in self.table("aroma_compounds") if any(t in r["compound"].lower() for t in tokens)]
            add("Aroma compounds", [_fmt(r, ["compound", "odor_descriptor", "wheel_tier1_inferred", "fd_factor_range",
                                             "oav_range"]) for r in (rows or self.table("aroma_compounds"))[:6]])

        notes = [r for r in self.table("coffee_flavor_chemistry")
                 if any(_has(q, w) for w in CHEM_WORDS.get(r.get("topic"), []))]
        if notes:
            add("Flavour chemistry", [_fmt(r, ["finding"]) for r in notes])
        if any(_has(q, w) for w in BITTER_CHEM_WORDS):
            rows = sorted(self.table("coffee_bitter_compounds"), key=lambda r: -r["dose_over_threshold"])[:5]
            add("Bitter compounds (above 1 = above taste threshold in the tested brew)",
                [_fmt(r, ["compound", "threshold_mg_per_l", "concentration_mg_per_l", "dose_over_threshold"]) for r in rows])
        if any(_has(q, w) for w in ODORANT_WORDS):
            wanted = [s for s in ("arabica", "robusta") if _has(q, s)]
            rows = [r for r in self.table("coffee_key_odorants") if not wanted or r.get("species") in wanted]
            add("Key odorants", [_fmt(r, ["compound", "odor_descriptor", "species", "role"]) for r in rows])
        if any(_has(q, w) for w in DEFECT_WORDS):
            rows = self.table("coffee_defects")
            named = [r for r in rows if any(_has(q, w) and w in f"{r['id']} {r['compound']} {r['off_note']}".lower()
                                            for w in ("rio", "tca", "peasy", "musty", "medicinal"))]
            add("Defects", [_fmt(r, ["compound", "off_note", "found_in", "threshold", "notes"]) for r in named or rows])

        topics = {topic for topic, words in HEALTH_WORDS.items() if any(_has(q, w) for w in words)}
        if not topics and _has(q, "caffeine") and not (species or var_hits or _has(q, "decaf") or sections):
            topics = {"caffeine"}
        if topics or _has(q, "health") or _has(q, "healthy"):
            add("Caffeine and health (information only, not medical advice)", self.health_lines(topics))

        if not sections:
            tokens = {t for t in re.findall(r"[a-z]{5,}", q) if t not in STOP}
            hits = []
            for name, rows in self.data.items():
                if name == "coffee_health":      # only shown with its status, through the section above
                    continue
                for r in rows:
                    blob = json.dumps(r, ensure_ascii=False).lower()
                    if tokens and any(t in blob for t in tokens):
                        hits.append((name, r))
                        if len(hits) >= 6:
                            break
                if len(hits) >= 6:
                    break
            if hits:
                add("Closest matches", [f"- {name}: " + _fmt(r, list(r.keys())[:5])[2:] for name, r in hits])
            else:
                return "No match in the local data.\n\n" + HELP

        return "\n\n".join(sections)
