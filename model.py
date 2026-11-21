#!/usr/bin/env python3
"""FlavorLab model: data, perception model, pairing, suggestions, JSON summary (no plotting).
Import it directly from agents: `import model; db = model.DB(); model.analyze(db, recipe)`."""
import csv
import difflib
import glob
import json
import math
import os

import numpy as np

VERSION = "0.2.0"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = sorted(glob.glob(os.path.join(HERE, "ingredients*.csv")))   # all packs; later files override

# ----------------------------------------------------------------------------
# Dimensions
# ----------------------------------------------------------------------------
TASTE = ["heat", "sweet", "sour", "salty", "bitter", "umami"]
AROMA = ["fruity", "citrus", "floral", "herbal", "earthy", "smoky", "warm", "pungent", "funky"]
TRIG = ["astringent", "cooling", "numbing", "sinus", "bite"]          # chemesthesis / mouthfeel
DIMS = TASTE + AROMA + TRIG
VEC_DIMS = DIMS[1:]                      # stored in CSV; heat comes from SHU
VI = {d: i for i, d in enumerate(VEC_DIMS)}
AROMA_IDX = [VI[d] for d in AROMA]
TRIG_IDX = [VI[d] for d in TRIG]
FRAGILE_IDX = AROMA_IDX + [VI["cooling"], VI["sinus"]]   # lost to heat / time with volatility
DIM_LABEL = {"warm": "warm spice", "pungent": "pungent/allium", "funky": "funky/ferment",
             "sinus": "sinus (mustard)", "bite": "pepper bite"}

# Refined aroma families: name -> (group, descriptor, marker compounds). Extend freely.
FAMILIES = {
    "ester": ("fruity", "fruity esters", "ethyl butanoate, isoamyl acetate, hexyl esters"),
    "lactone": ("fruity", "peach / coconut / creamy", "γ-decalactone, δ-octalactone"),
    "thiol_trop": ("fruity", "tropical / blackcurrant", "3-mercaptohexanol, 4-MMP"),
    "ionone": ("fruity", "violet / berry / tea", "β-ionone, β-damascenone, raspberry ketone"),
    "citrus_terp": ("citrus", "citrus peel", "limonene, citral, citronellal"),
    "floral_terp": ("floral", "lavender / coriander floral", "linalool, geraniol, linalyl acetate"),
    "rose": ("floral", "rose / honey", "2-phenylethanol, rose oxide"),
    "green_c6": ("green", "cut grass / green leaf", "hexanal, (Z)-3-hexenal"),
    "mpyrazine": ("green", "green bell pepper", "2-methoxy-3-isobutylpyrazine"),
    "fatty_ald": ("green", "waxy / cucumber / cilantro", "(E)-2-decenal, nonadienal"),
    "cineole": ("herbal", "eucalyptus / camphor", "1,8-cineole, camphor"),
    "menthol_carvone": ("herbal", "mint / caraway", "menthol, carvone"),
    "thymol": ("herbal", "thyme / oregano", "thymol, carvacrol"),
    "pine": ("herbal", "pine / resin", "α-pinene, myrcene, terpinolene"),
    "eugenol": ("spice", "clove", "eugenol"),
    "anethole": ("spice", "anise / licorice", "anethole, estragole"),
    "spice_ald": ("spice", "cinnamon / cumin / almond", "cinnamaldehyde, cuminaldehyde, benzaldehyde"),
    "vanillin": ("spice", "vanilla / oak", "vanillin, whisky lactone"),
    "sesqui": ("spice", "woody-peppery", "rotundone, caryophyllene, turmerone"),
    "furanone": ("roast", "caramel / maple / dried fruit", "furaneol, sotolon, maltol"),
    "pyrazine": ("roast", "nutty / roasted", "alkylpyrazines, 2-acetyl-1-pyrroline"),
    "thiol_roast": ("roast", "coffee / roasted sesame", "2-furfurylthiol"),
    "smoke_phenol": ("smoke", "smoke", "guaiacol, 4-methylguaiacol, cresols"),
    "allium": ("sulfur", "garlic / onion", "allicin, diallyl disulfide"),
    "itc": ("sulfur", "mustard / horseradish", "allyl isothiocyanate"),
    "ferm_acid": ("ferment", "cheesy / funky ferment", "butyric, isovaleric acid"),
    "marine": ("ferment", "briny / dried seafood", "trimethylamine, dimethyl sulfide"),
    "acetic": ("ferment", "vinegar", "acetic acid"),
    "earthy_root": ("earthy", "beet / root / soil", "geosmin"),
    "mushroom": ("earthy", "mushroom", "1-octen-3-ol"),
}
FAM = list(FAMILIES)
FI = {f: i for i, f in enumerate(FAM)}
GROUPS = list(dict.fromkeys(g for g, _, _ in FAMILIES.values()))
GMAT = np.array([[1.0 if FAMILIES[f][0] == g else 0.0 for g in GROUPS] for f in FAM])   # family -> group

# Volatility: share of a top / middle / base-note ingredient's aroma that survives
VOL_KEEP = {"cooked": {"t": 0.4, "m": 0.75, "b": 1.0}, "raw": {"t": 1.0, "m": 1.0, "b": 1.0}}
AGE_KEEP = {"t": 0.6, "m": 0.85, "b": 1.0}                                   # ~3 months in the bottle
VOL_LABEL = {"t": "top", "m": "middle", "b": "base"}

# Heat character -> time constants (s) for a rise-and-decay heat curve
ONSET_S = {1: 1.5, 2: 4, 3: 8, 4: 15, 5: 25}
LENGTH_S = {1: 20, 2: 45, 3: 90, 4: 180, 5: 300}
ZONES = ["front", "mid", "back"]
HT = np.linspace(0, 300, 601)

BODY_CLASSES = [(1.0, "thin", "Tabasco-like"), (2.5, "pourable", "Cholula-like"),
                (4.0, "thick", "Sriracha / ketchup"), (math.inf, "paste", "harissa / sambal")]

COMPRESS = 3.0          # psychophysical saturation constant (x -> 10*(1-e^-x/k))
FAT_K = 1.5

CATEGORIES = ["chili", "fruit", "veg", "acid", "savory", "sweet", "herb", "spice"]
CAT_LABEL = {"chili": "Chili", "fruit": "Fruit", "veg": "Veg & allium", "acid": "Acid",
             "savory": "Savory, fat & base", "sweet": "Sweetener", "herb": "Herb", "spice": "Spice & other"}

# ----------------------------------------------------------------------------
# Styles = target perceived profiles (0-10). Extend freely.
# ----------------------------------------------------------------------------
STYLES = {
    "balanced": {"label": "Balanced all-rounder", "tol": 1.5,
                 "target": {"heat": 5, "sweet": 3, "sour": 5.5, "salty": 5, "bitter": 1, "umami": 2}},
    "louisiana": {"label": "Louisiana vinegar sauce", "tol": 1.25,
                  "target": {"heat": 4, "sweet": 0.5, "sour": 8, "salty": 5.5, "bitter": 0.5, "umami": 1,
                             "pungent": 2, "funky": 2, "fruity": 2}},
    "fruity_caribbean": {"label": "Fruity Caribbean", "tol": 1.25,
                         "target": {"heat": 5.5, "sweet": 5, "sour": 6, "salty": 4.5, "bitter": 0.5, "umami": 1,
                                    "fruity": 7.5, "citrus": 4, "floral": 4, "warm": 3, "pungent": 3}},
    "sriracha": {"label": "Sriracha-style garlic chili", "tol": 1.25,
                 "target": {"heat": 4, "sweet": 5, "sour": 4.5, "salty": 5.5, "bitter": 0.5, "umami": 3,
                            "pungent": 6, "funky": 3, "fruity": 2}},
    "smoky_chipotle": {"label": "Smoky chipotle", "tol": 1.25,
                       "target": {"heat": 4.5, "sweet": 4, "sour": 5, "salty": 5, "bitter": 1.5, "umami": 3,
                                  "smoky": 7, "earthy": 5, "fruity": 3, "pungent": 3, "warm": 2}},
    "salsa_verde": {"label": "Green / verde", "tol": 1.25,
                    "target": {"heat": 5, "sweet": 1, "sour": 6.5, "salty": 5, "bitter": 1, "umami": 1.5,
                               "herbal": 7, "citrus": 5, "pungent": 4, "fruity": 2}},
    "salsa_roja": {"label": "Mexican table sauce (roja)", "tol": 1.25,
                   "target": {"heat": 4, "sweet": 1.5, "sour": 6, "salty": 6, "bitter": 1, "umami": 2,
                              "earthy": 5, "pungent": 3, "smoky": 2, "herbal": 1}},
    "superhot_fruity": {"label": "Superhot fruity", "tol": 1.25,
                        "target": {"heat": 9, "sweet": 4, "sour": 6, "salty": 4.5, "bitter": 1, "umami": 1,
                                   "fruity": 7, "floral": 4, "citrus": 3}},
    "fermented_umami": {"label": "Fermented umami (gochujang-ish)", "tol": 1.25,
                        "target": {"heat": 5, "sweet": 5, "sour": 4, "salty": 6, "bitter": 0.5, "umami": 6.5,
                                   "funky": 6, "pungent": 4, "smoky": 2, "earthy": 3}},
    "coffee_mole": {"label": "Coffee-chile / mole-ish", "tol": 1.25,
                    "target": {"heat": 4, "sweet": 4, "sour": 4, "salty": 4.5, "bitter": 3, "umami": 3,
                               "smoky": 5, "earthy": 6, "fruity": 4, "warm": 3}},
    "sichuan_mala": {"label": "Sichuan mala chili oil", "tol": 1.25,
                     "target": {"heat": 4.5, "sweet": 3, "sour": 2.5, "salty": 7, "bitter": 1.5, "umami": 7.5,
                                "numbing": 5, "pungent": 3, "earthy": 6, "smoky": 4, "warm": 3, "funky": 5}},
}

# Preparation modifiers on taste/aroma/trigeminal dims or aroma families:
# ("add", value) or ("mul", factor). Keys are dims (VEC_DIMS) or families (FAM).
PREP = {
    "raw": {},
    "roasted": {"sweet": ("add", 1.5), "smoky": ("add", 2), "earthy": ("add", 1), "pungent": ("mul", 0.5),
                "herbal": ("mul", 0.6), "fruity": ("mul", 0.9), "bite": ("mul", 0.4), "sinus": ("mul", 0.3),
                "furanone": ("add", 1), "pyrazine": ("add", 1), "allium": ("mul", 0.6), "green_c6": ("mul", 0.5)},
    "charred": {"smoky": ("add", 4), "bitter": ("add", 2), "sweet": ("add", 1), "pungent": ("mul", 0.4),
                "herbal": ("mul", 0.5), "bite": ("mul", 0.5), "smoke_phenol": ("add", 2), "pyrazine": ("add", 1),
                "green_c6": ("mul", 0.4)},
    "smoked": {"smoky": ("add", 5), "earthy": ("add", 1), "smoke_phenol": ("add", 3)},
    "toasted": {"earthy": ("add", 1), "smoky": ("add", 1), "warm": ("mul", 1.2), "bitter": ("add", 0.5),
                "pyrazine": ("add", 1)},
    "caramelized": {"sweet": ("add", 3), "pungent": ("mul", 0.2), "earthy": ("add", 1), "umami": ("add", 1),
                    "bitter": ("add", 0.5), "bite": ("mul", 0.2), "furanone": ("add", 2), "allium": ("mul", 0.5)},
    "fermented": {"sweet": ("mul", 0.6), "sour": ("add", 3), "funky": ("add", 3), "umami": ("add", 1),
                  "pungent": ("mul", 0.7), "fruity": ("mul", 0.9), "herbal": ("mul", 0.8), "bite": ("mul", 0.7),
                  "sinus": ("mul", 0.5), "ferm_acid": ("add", 2), "ester": ("add", 1), "acetic": ("add", 1)},
}
FERMENTABLE = {"chili", "fruit", "veg", "herb"}

# Classic / proven pairings get a bonus in the pairing score. Extend freely.
CLASSIC = [
    ("habanero", "mango"), ("habanero", "pineapple"), ("habanero", "passion fruit"), ("habanero", "carrot"),
    ("habanero", "lime juice"), ("habanero", "peach"), ("habanero", "apricot"), ("scotch bonnet", "allspice"),
    ("scotch bonnet", "thyme"), ("scotch bonnet", "mango"), ("scotch bonnet", "pineapple"),
    ("scotch bonnet", "scallion"), ("jalapeno", "cilantro"), ("jalapeno", "lime juice"), ("serrano", "tomatillo"),
    ("serrano", "cilantro"), ("tomatillo", "cilantro"), ("chipotle", "honey"), ("chipotle", "maple syrup"),
    ("chipotle", "garlic"), ("chipotle", "orange juice"), ("chipotle", "espresso"), ("ancho", "cacao nibs"),
    ("ancho", "cinnamon"), ("ancho", "espresso"), ("ancho", "dark chocolate"), ("guajillo", "garlic"),
    ("guajillo", "cumin"), ("chile de arbol", "garlic"), ("ghost pepper", "mango"), ("carolina reaper", "mango"),
    ("ginger", "garlic"), ("ginger", "lime juice"), ("lemongrass", "kaffir lime leaf"), ("lemongrass", "galangal"),
    ("fish sauce", "lime juice"), ("thai bird's eye", "fish sauce"), ("thai bird's eye", "garlic"),
    ("gochugaru", "garlic"), ("gochujang", "toasted sesame oil"), ("cumin", "coriander seed"), ("garlic", "cumin"),
    ("tomato", "basil"), ("strawberry", "black pepper"), ("strawberry", "basil"), ("peach", "ginger"),
    ("sour cherry", "cacao nibs"), ("raspberry", "cacao nibs"), ("mango", "lime juice"), ("pineapple", "cilantro"),
    ("pineapple", "dark rum"), ("tamarind paste", "dates"), ("tamarind paste", "ginger"),
    ("aji amarillo", "lime juice"), ("aji amarillo", "garlic"), ("espresso", "cardamom"),
    ("espresso", "orange zest"), ("espresso", "cacao nibs"), ("honey", "lemon juice"), ("mezcal", "chipotle"),
    ("hibiscus (dried)", "ginger"), ("guava", "habanero"), ("smoked paprika", "garlic"), ("urfa biber", "cacao nibs"),
    ("black garlic", "chipotle"), ("miso", "gochugaru"), ("passion fruit", "lime juice"),
    # v0.2 additions
    ("sichuan peppercorn", "chili crisp"), ("doubanjiang", "sichuan peppercorn"), ("kombu", "katsuobushi"),
    ("yuzu juice", "yuzu kosho"), ("sour orange", "achiote"), ("sour orange", "habanero"), ("datil", "honey"),
    ("aji panca", "aji amarillo"), ("harissa", "preserved lemon"), ("berbere", "fenugreek"),
    ("piri piri", "lemon juice"), ("banana", "scotch bonnet"), ("tamarind paste", "jaggery"),
    ("mulato", "ancho"), ("pepitas", "hatch green chile"), ("dried lime", "fenugreek"),
    ("ethiopian natural coffee", "blueberry"), ("kenyan coffee", "blackcurrant"), ("bourbon", "chipotle"),
    ("lapsang souchong", "dark chocolate"), ("tequila", "lime juice"), ("matcha", "yuzu juice"),
    ("black vinegar", "chili crisp"), ("sansho", "yuzu juice"), ("fish sauce", "palm sugar"),
]


# ----------------------------------------------------------------------------
# Data
# ----------------------------------------------------------------------------
class Ingredient:
    def __init__(self, row):
        self.name = row["name"].strip()
        self.category = row["category"].strip()
        if self.category not in CATEGORIES:
            raise ValueError(f"{self.name}: unknown category {self.category}")
        num = lambda k: float(row.get(k) or 0)  # noqa: E731
        self.shu = num("shu")                        # published pod rating (dry-weight basis)
        self.solids = float(row.get("solids") or 1)  # dry-matter fraction as used (fresh pod ~0.12)
        self.potency = num("potency") or 1.0
        self.fat = num("fat")
        self.body = num("body")                      # thickening power per gram (uncapped; xanthan = 500)
        self.vec = np.array([num(d) for d in VEC_DIMS], dtype=float)
        self.fam = np.zeros(len(FAM))
        for tok in (row.get("aroma") or "").split(";"):
            if tok.strip():
                k, _, w = tok.partition(":")
                if k.strip() not in FI:
                    raise ValueError(f"{self.name}: unknown aroma family '{k}'")
                self.fam[FI[k.strip()]] = float(w or 1)
        self.onset = int(row.get("heat_onset") or 2)
        self.length = int(row.get("heat_length") or 2)
        self.zone = (row.get("heat_zone") or "mid").strip()
        self.vol = (row.get("volatility") or "m").strip()
        if self.zone not in ZONES or self.vol not in VOL_LABEL or not (1 <= self.onset <= 5 and 1 <= self.length <= 5):
            raise ValueError(f"{self.name}: bad heat character / volatility")
        self.aliases = [a.strip() for a in (row.get("aliases") or "").split("|") if a.strip()]
        self.notes = (row.get("notes") or "").strip()

    @property
    def eff_shu(self):
        """SHU of the ingredient as used (fresh pods carry ~88 % water)."""
        return self.shu * self.solids

    @property
    def neutral(self):
        return self.fam.sum() == 0 and self.vec[AROMA_IDX + TRIG_IDX].sum() == 0

    def to_dict(self):
        fams = [{"family": FAM[i], "weight": float(self.fam[i]), "descriptor": FAMILIES[FAM[i]][1]}
                for i in np.argsort(-self.fam) if self.fam[i] > 0]
        d = {"name": self.name, "category": self.category, "shu": self.shu, "potency": self.potency,
             "fat": self.fat, "solids": self.solids, "effective_shu": round(self.eff_shu), "body": self.body,
             "profile": {d: float(self.vec[VI[d]]) for d in VEC_DIMS},
             "heat_index": round(heat_index(self.eff_shu), 2), "aroma_families": fams,
             "volatility": VOL_LABEL[self.vol] + " note", "aliases": self.aliases, "notes": self.notes}
        if self.shu > 0:
            d["heat_character"] = {"onset": self.onset, "length": self.length, "zone": self.zone}
        return d


class DB:
    def __init__(self, path=DEFAULT_DB):
        self.path = path
        self.items, self.index = {}, {}
        for p in [path] if isinstance(path, str) else path:
            with open(p, newline="", encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    if not (row.get("name") or "").strip():
                        continue
                    ing = Ingredient(row)
                    self.items[ing.name] = ing
                    for key in [ing.name] + ing.aliases:
                        self.index[norm(key)] = ing.name
        self.classic = set()
        for a, b in CLASSIC:
            if norm(a) in self.index and norm(b) in self.index:
                self.classic.add(frozenset((self.index[norm(a)], self.index[norm(b)])))

    def get(self, name):
        key = norm(name)
        if key in self.index:
            return self.items[self.index[key]]
        close = difflib.get_close_matches(key, list(self.index), n=4, cutoff=0.6)
        hint = ", ".join(sorted({self.index[c] for c in close})) or "run `list`"
        raise KeyError(f"Unknown ingredient '{name}'. Did you mean: {hint}")


def norm(s):
    return " ".join(s.lower().replace("ñ", "n").replace("_", " ").split())


def heat_index(shu):
    """Effective SHU -> 0-10 (log: ~30 SHU = 0, 1k ≈ 3.8, 5k ≈ 5.5, 30k ≈ 7.5, 300k+ = 10)."""
    if shu <= 32:
        return 0.0
    return float(np.clip(10 * (math.log10(shu) - 1.5) / 4, 0, 10))


def sat(x):
    return 10 * (1 - np.exp(-np.asarray(x) / COMPRESS))


def cosine(x, y):
    n = np.linalg.norm(x) * np.linalg.norm(y)
    return float(x @ y / n) if n > 0 else 0.0


def heat_curve(onset, length):
    c = (1 - np.exp(-HT / ONSET_S[onset])) * np.exp(-HT / LENGTH_S[length])
    return c / c.max()


def apply_prep(vec, fam, preps):
    v, f = vec.copy(), fam.copy()
    for p in preps:
        if p not in PREP:
            raise KeyError(f"Unknown prep '{p}'. Options: {', '.join(PREP)}, finish")
        for k, (op, val) in PREP[p].items():
            arr, i = (v, VI[k]) if k in VI else (f, FI[k])
            arr[i] = arr[i] + val if op == "add" else arr[i] * val
    return np.clip(v, 0, 10), np.clip(f, 0, 4)


# ----------------------------------------------------------------------------
# Recipes
# ----------------------------------------------------------------------------
def load_recipe(path):
    with open(path, encoding="utf-8") as f:
        r = json.load(f)
    return normalize_recipe(r, default_name=os.path.splitext(os.path.basename(path))[0])


def normalize_recipe(r, default_name="sauce"):
    items = r.get("ingredients", [])
    if isinstance(items, dict):
        items = [{"item": k, "g": v} for k, v in items.items()]
    out = []
    for it in items:
        prep = it.get("prep", [])
        prep = [prep] if isinstance(prep, str) else list(prep)
        stage = it.get("stage", "finish" if "finish" in prep else "main")
        out.append({"item": it["item"], "g": float(it["g"]), "prep": [p for p in prep if p != "finish"],
                    "stage": stage})
    return {"name": r.get("name", default_name), "style": r.get("style", "balanced"),
            "process": r.get("process", "cooked"), "fermented": r.get("fermented", False),
            "notes": r.get("notes", ""), "ingredients": out}


def parse_quick(spec):
    """'habanero:120, mango:250:roasted+smoked, lime juice:30:finish' -> list of items."""
    items = []
    for chunk in spec.split(","):
        if not chunk.strip():
            continue
        parts = [p.strip() for p in chunk.split(":")]
        if len(parts) < 2:
            raise ValueError(f"Bad item '{chunk}'. Use name:grams[:prep+prep|finish]")
        prep = parts[2].split("+") if len(parts) > 2 and parts[2] else []
        items.append({"item": parts[0], "g": float(parts[1]), "prep": prep})
    return items


# ----------------------------------------------------------------------------
# Model
# ----------------------------------------------------------------------------
def perceive(I, heat, fat):
    """Mixture interactions (heuristic, from sensory-science directions)."""
    sw, so, sa, bi, um = I["sweet"], I["sour"], I["salty"], I["bitter"], I["umami"]
    p = dict(I)
    f = lambda x: max(0.2, x)  # noqa: E731  never suppress below 20 %
    p["sweet"] = sw * f(1 - 0.035 * so - 0.03 * bi) * (1 + 0.02 * min(sa, 5))   # acid/bitter mask sweet, salt lifts
    p["sour"] = so * f(1 - 0.04 * sw)                                         # sugar rounds acid
    p["bitter"] = bi * f(1 - 0.06 * sa - 0.03 * sw)                           # salt + sugar suppress bitter
    p["salty"] = sa * (1 + 0.015 * so)                                        # acid boosts salt
    p["umami"] = um * (1 + 0.05 * sa)                                         # salt-umami synergy
    p["heat"] = heat * f(1 - 0.03 * sw - 0.04 * fat - 0.02 * I["cooling"]) * (1 + 0.015 * so)  # sugar/fat/menthol tame
    p["astringent"] = I["astringent"] * f(1 - 0.04 * sw - 0.05 * fat) * (1 + 0.02 * so)   # fat & sugar coat tannins
    p["cooling"] = I["cooling"] * f(1 - 0.03 * heat)                          # capsaicin overrides menthol
    p["bite"] = I["bite"] * f(1 - 0.03 * fat)
    mask = f(1 - 0.04 * max(0.0, heat - 6))                                    # big heat drowns delicate aromatics
    for d in ("fruity", "floral", "citrus", "herbal"):
        p[d] *= mask
    p["floral"] *= f(1 - 0.02 * I["pungent"])                                 # raw allium stomps florals
    return {d: float(np.clip(p[d], 0, 10)) for d in DIMS}


def ing_profile(ing, vec):
    d = {k: float(vec[VI[k]]) for k in VEC_DIMS}
    d["heat"] = heat_index(ing.eff_shu)
    d["fat"] = ing.fat
    return d


# How often categories work together in sauces (0-1). Symmetric; extend freely.
_AFF = {
    "chili": {"chili": .7, "fruit": .75, "veg": .85, "acid": .85, "savory": .7, "sweet": .65, "herb": .6, "spice": .6},
    "fruit": {"fruit": .6, "veg": .4, "acid": .8, "savory": .35, "sweet": .6, "herb": .6, "spice": .6},
    "veg": {"veg": .7, "acid": .6, "savory": .75, "sweet": .4, "herb": .7, "spice": .7},
    "acid": {"acid": .3, "savory": .6, "sweet": .7, "herb": .6, "spice": .4},
    "savory": {"savory": .5, "sweet": .6, "herb": .5, "spice": .6},
    "sweet": {"sweet": .2, "herb": .4, "spice": .7},
    "herb": {"herb": .5, "spice": .4},
    "spice": {"spice": .6},
}


def cat_aff(a, b):
    return _AFF.get(a, {}).get(b, _AFF.get(b, {}).get(a, 0.4))


CONTRAST = [("sweet", "sour", 1.0), ("sweet", "heat", 0.8), ("salty", "bitter", 0.8), ("sweet", "salty", 0.6),
            ("umami", "sour", 0.6), ("fruity", "heat", 0.7), ("fat", "heat", 0.6), ("sweet", "bitter", 0.5),
            ("numbing", "heat", 0.6), ("cooling", "heat", 0.4), ("sour", "fat", 0.5), ("sweet", "astringent", 0.4),
            ("fat", "astringent", 0.4)]


def pair_score(db, a, b, va=None, vb=None, fa=None, fb=None, explain=False):
    va = a.vec if va is None else va
    vb = b.vec if vb is None else vb
    fa = a.fam if fa is None else fa
    fb = b.fam if fb is None else fb
    aroma_sim = 0.6 * cosine(fa, fb) + 0.4 * cosine(fa @ GMAT, fb @ GMAT)   # exact family + same family group
    cos = cosine(va[AROMA_IDX], vb[AROMA_IDX])
    pa, pb = ing_profile(a, va), ing_profile(b, vb)
    contrast = min(1.0, sum(w * (pa[x] * pb[y] + pa[y] * pb[x]) for x, y, w in CONTRAST) / 100)
    both = lambda x, y: pa[x] * pb[y] + pa[y] * pb[x]  # noqa: E731
    clash = (0.6 * pa["bitter"] * pb["bitter"] + 0.3 * pa["pungent"] * pb["pungent"]
             + 0.4 * pa["astringent"] * pb["astringent"] + 0.3 * both("smoky", "floral")
             + 0.3 * both("bitter", "astringent") + 0.2 * both("sinus", "floral")) / 100
    classic = 0.2 if frozenset((a.name, b.name)) in db.classic else 0.0
    aff = cat_aff(a.category, b.category)
    raw = 0.25 * aroma_sim + 0.2 * cos + 0.25 * contrast + 0.3 * aff - clash + classic
    s = 100 * float(np.tanh(1.2 * max(0.0, raw)))          # soft ceiling keeps resolution at the top
    if not explain:
        return s
    shared = [f"{FAM[i]} ({FAMILIES[FAM[i]][1]})" for i in np.argsort(-(fa * fb)) if fa[i] * fb[i] > 0]
    return {"score": round(s, 1), "shared_families": shared, "aroma_similarity": round(aroma_sim, 2),
            "profile_similarity": round(cos, 2), "taste_contrast": round(contrast, 2),
            "category_affinity": aff, "clash": round(clash, 2), "classic": bool(classic)}


def bridges(db, a, b, top=6, exclude=()):
    """Ingredients that pair well with BOTH a and b (score = the weaker of the two links)."""
    out = []
    for x in db.items.values():
        if x.neutral or x.name in (a.name, b.name) or x.name in exclude:
            continue
        out.append((min(pair_score(db, a, x), pair_score(db, b, x)), x.name))
    return [(n, round(s, 1)) for s, n in sorted(out, reverse=True)[:top]]


def style_fit(perc, style):
    st = STYLES[style]
    tol_t, tol_a = st["tol"], st["tol"] + 0.5
    gaps, num, den = {}, 0.0, 0.0
    for d, t in st["target"].items():
        tol = tol_t if d in TASTE else tol_a
        w = 1.0 if d in TASTE else 0.7
        diff = perc[d] - t
        exc = max(0.0, abs(diff) - tol)
        gaps[d] = {"target": t, "value": round(perc[d], 2), "diff": round(diff, 2), "tol": tol,
                   "status": "ok" if exc == 0 else ("too much" if diff > 0 else "too little")}
        num += w * exc ** 2
        den += w
    rms = math.sqrt(num / den) if den else 0
    return 100 * math.exp(-rms / 2.5), gaps


def body_class(b):
    return next((name, ex) for lim, name, ex in BODY_CLASSES if b < lim)


def analyze(db, recipe):
    style = recipe.get("style", "balanced")
    if style not in STYLES:
        raise KeyError(f"Unknown style '{style}'. Options: {', '.join(STYLES)}")
    process = recipe.get("process", "cooked")
    if process not in VOL_KEEP:
        raise KeyError(f"Unknown process '{process}'. Options: {', '.join(VOL_KEEP)}")
    ferm = recipe.get("fermented", False)
    ferm_set = {db.get(n).name for n in ferm} if isinstance(ferm, list) else None
    rows = []
    for it in recipe["ingredients"]:
        ing = db.get(it["item"])
        preps = list(it.get("prep", []))
        if (ferm is True and ing.category in FERMENTABLE) or (ferm_set and ing.name in ferm_set):
            if "fermented" not in preps:
                preps.append("fermented")
        v, fam = apply_prep(ing.vec, ing.fam, preps)
        stage = it.get("stage", "main")
        keep = 1.0 if stage == "finish" else VOL_KEEP[process][ing.vol]
        rows.append({"ing": ing, "g": it["g"], "prep": preps, "stage": stage, "vec": v, "fam": fam, "keep": keep})
    total = sum(r["g"] for r in rows)
    if total <= 0:
        raise ValueError("Recipe has no mass")
    for r in rows:
        r["frac"] = r["g"] / total
    fresh = np.array([r["frac"] * r["ing"].potency * r["vec"] for r in rows])        # n x VEC, before losses
    keep = np.array([r["keep"] for r in rows])
    contrib = fresh.copy()
    contrib[:, FRAGILE_IDX] *= keep[:, None]
    fam_contrib = np.array([r["frac"] * r["ing"].potency * r["fam"] * r["keep"] for r in rows])
    x = contrib.sum(axis=0)
    I = {d: float(sat(x[VI[d]])) for d in VEC_DIMS}
    shu_contrib = np.array([r["frac"] * r["ing"].eff_shu for r in rows])
    shu = float(shu_contrib.sum())
    heat = heat_index(shu)
    fat = float(sat(sum(r["frac"] * r["ing"].fat for r in rows) * COMPRESS / FAT_K))
    raw = dict(I, heat=heat)
    perc = perceive(I, heat, fat)
    fit, gaps = style_fit(perc, style)

    # per-ingredient share of each perceived dimension
    shares = np.zeros((len(rows), len(DIMS)))
    for j, d in enumerate(DIMS):
        col = shu_contrib if d == "heat" else contrib[:, VI[d]]
        if col.sum() > 0:
            shares[:, j] = col / col.sum() * perc[d]

    # aroma staying power: top / middle / base share of fresh aroma, after cooking, after ~3 months
    aroma_fresh = fresh[:, AROMA_IDX].sum(axis=1)
    vol = [r["ing"].vol for r in rows]
    age = np.array([AGE_KEEP[v] for v in vol])
    base = aroma_fresh.sum() or 1.0
    pyramid = {}
    for state, mult in (("fresh", np.ones(len(rows))), ("processed", keep), ("aged", keep * age)):
        pyramid[state] = {VOL_LABEL[c]: float(100 * sum(aroma_fresh[i] * mult[i] for i in range(len(rows))
                                                        if vol[i] == c) / base) for c in "tmb"}

    # heat over time & where it hits
    hp = {"cap": np.zeros_like(HT), "zones": {z: 0.0 for z in ZONES}}
    if shu > 0:
        for r, s in zip(rows, shu_contrib):
            if s > 0:
                hp["cap"] += s / shu * heat_curve(r["ing"].onset, r["ing"].length)
                hp["zones"][r["ing"].zone] += s / shu
        hp["cap"] *= perc["heat"] / hp["cap"].max()
    for k, on, ln in (("bite", 1, 2), ("sinus", 1, 1), ("numbing", 3, 4)):
        hp[k] = heat_curve(on, ln) * perc[k]
    pk = int(np.argmax(hp["cap"]))
    below = np.nonzero(hp["cap"][pk:] < 0.5 * hp["cap"][pk])[0]
    hp["peak_s"] = float(HT[pk])
    hp["half_s"] = float(HT[pk + below[0]]) if len(below) else None

    # harmony = impact-weighted mean pairwise score
    impact = np.array([0 if r["ing"].neutral else r["frac"] * r["ing"].potency *
                       (r["vec"].sum() + heat_index(r["ing"].eff_shu)) for r in rows])
    n = len(rows)
    pm = np.full((n, n), np.nan)
    for i in range(n):
        for j in range(i + 1, n):
            if rows[i]["ing"].neutral or rows[j]["ing"].neutral:
                continue
            pm[i, j] = pm[j, i] = pair_score(db, rows[i]["ing"], rows[j]["ing"], rows[i]["vec"], rows[j]["vec"],
                                             rows[i]["fam"], rows[j]["fam"])
    num = den = 0.0
    for i in range(n):
        for j in range(i + 1, n):
            if not np.isnan(pm[i, j]):
                w = impact[i] * impact[j]
                num += w * pm[i, j]
                den += w
    harmony = num / den if den > 0 else 60.0
    overall = 0.75 * fit + 0.25 * harmony

    body = float(sum(r["frac"] * r["ing"].body for r in rows))
    salt_pct = 100 * sum(r["frac"] for r in rows if r["ing"].name == "salt")
    warns = []
    fermented_any = any("fermented" in r["prep"] for r in rows)
    if raw["sour"] < 4.5 and not fermented_any:
        warns.append("Low acidity - likely above pH 4.6. Add acid and verify with a pH meter.")
    if fermented_any and salt_pct < 2:
        warns.append(f"Ferment with {salt_pct:.1f}% salt - 2-3% of mash weight is the usual safe range.")
    if salt_pct > 4.5:
        warns.append(f"Salt {salt_pct:.1f}% is high for a sauce.")
    if perc["heat"] > 8.5:
        warns.append("Extreme heat - aromatics will be masked; consider fruit/sugar/fat carriers.")
    if perc["astringent"] > 4:
        warns.append("Drying / astringent finish - fat, sugar or salt will soften it.")
    lost_sinus = [r["ing"].name for r in rows if r["vec"][VI["sinus"]] >= 5 and r["keep"] < 1]
    if lost_sinus:
        warns.append(f"Cooking kills the sinus kick of {', '.join(lost_sinus)} - add at the finish.")
    top_fresh, top_proc = pyramid["fresh"]["top"], pyramid["processed"]["top"]
    if top_fresh > 25 and top_proc < 0.6 * top_fresh:
        warns.append(f"Cooking loses ~{top_fresh - top_proc:.0f}% of the aroma (top notes) - "
                     "add citrus / fresh herbs at the finish.")
    warns.append("Always measure pH: aim 3.5-4.0 for shelf stability (4.6 = safety limit).")

    return {
        "name": recipe["name"], "style": style, "style_label": STYLES[style]["label"], "process": process,
        "total_g": total, "rows": rows, "raw": raw, "perceived": perc, "fat_level": fat,
        "shu": shu, "fit": fit, "gaps": gaps, "harmony": harmony, "overall": overall,
        "shares": shares, "pair_matrix": pm, "impact": impact, "salt_pct": salt_pct, "warnings": warns,
        "fam_contrib": fam_contrib, "pyramid": pyramid, "heat_profile": hp, "body": body,
        "recipe": recipe,
    }


# ----------------------------------------------------------------------------
# Suggestions / optimization
# ----------------------------------------------------------------------------
def short(name, n=12):
    return name if len(name) <= n else name[: n - 1] + "…"


def nice_grams(g):
    if g < 3:
        return round(g, 1)
    if g < 20:
        return float(round(g))
    return float(5 * round(g / 5))


def _with(recipe, items):
    r = dict(recipe)
    r["ingredients"] = items
    return r


def suggest(db, recipe, base=None, top=8, pool=None):
    base = base or analyze(db, recipe)
    total = base["total_g"]
    present = {db.get(it["item"]).name for it in recipe["ingredients"]}
    moves = []

    def evaluate(label, items, kind, item, grams, keep=True):
        a = analyze(db, _with(recipe, items))
        m = {"move": label, "kind": kind, "item": item, "grams": grams,
             "d_overall": round(a["overall"] - base["overall"], 2),
             "d_fit": round(a["fit"] - base["fit"], 2),
             "d_harmony": round(a["harmony"] - base["harmony"], 2),
             "new_overall": round(a["overall"], 1), "_items": items}
        if keep:
            moves.append(m)
        return m

    # watery fillers (potency < 1) and pure texture agents are skipped: they only "help" by diluting
    cands = pool or [n for n, i in db.items.items() if n not in present and i.potency >= 1 and i.body < 100]
    for name in cands:
        ing = db.items[name]
        best = None
        for mult in (0.33, 1.0, 2.0):           # try a few doses, keep the best
            g = nice_grams(max(0.5, total * 0.06 * mult / ing.potency))
            items = recipe["ingredients"] + [{"item": name, "g": g, "prep": [], "stage": "main"}]
            m = evaluate(f"+ {g:g} g {short(name, 20)}", items, "add", name, g, keep=False)
            if best is None or m["d_overall"] > best["d_overall"]:
                best = m
        best["category"] = ing.category
        moves.append(best)
    for k, it in enumerate(recipe["ingredients"]):
        name = db.get(it["item"]).name
        for factor, word in ((1.3, "more"), (0.7, "less")):
            g = nice_grams(it["g"] * factor)
            if g == it["g"]:
                continue
            items = [dict(x) for x in recipe["ingredients"]]
            items[k]["g"] = g
            evaluate(f"{'▲' if word == 'more' else '▼'} {short(name, 18)} {it['g']:g}→{g:g} g", items, word, name, g)
        if len(recipe["ingredients"]) > 2:
            items = [dict(x) for j, x in enumerate(recipe["ingredients"]) if j != k]
            evaluate(f"✕ remove {short(name, 18)}", items, "remove", name, 0)
    moves.sort(key=lambda m: -m["d_overall"])
    out, per_cat = [], {}
    for m in moves:                              # diversity: max 2 additions per category
        if m["d_overall"] <= 0.05:
            break
        c = m.get("category")
        if c:
            if per_cat.get(c, 0) >= 2:
                continue
            per_cat[c] = per_cat.get(c, 0) + 1
        out.append(m)
        if len(out) >= top:
            break
    return out


def optimize(db, recipe, steps=4, min_gain=0.3):
    log = []
    cur = recipe
    for _ in range(steps):
        moves = suggest(db, cur, top=1)
        if not moves or moves[0]["d_overall"] < min_gain:
            break
        m = moves[0]
        cur = _with(cur, m["_items"])
        log.append({k: v for k, v in m.items() if not k.startswith("_")})
    cur = dict(cur, name=f"{recipe['name']} (optimized)")
    return cur, log


# ----------------------------------------------------------------------------
# JSON for agents
# ----------------------------------------------------------------------------
def summary(db, A, moves=None, opt_log=None):
    r2 = lambda d: {k: round(v, 2) for k, v in d.items()}  # noqa: E731
    rows = A["rows"]
    pm = A["pair_matrix"]
    pairs = []
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            if not np.isnan(pm[i, j]):
                pairs.append({"a": rows[i]["ing"].name, "b": rows[j]["ing"].name, "score": round(pm[i, j], 1)})
    pairs.sort(key=lambda p: p["score"])
    tot = A["fam_contrib"].sum(axis=0)
    hp = A["heat_profile"]
    out = {
        "name": A["name"], "style": A["style"], "process": A["process"], "total_g": A["total_g"],
        "scores": {"overall": round(A["overall"], 1), "style_fit": round(A["fit"], 1),
                   "harmony": round(A["harmony"], 1)},
        "estimated_shu": round(A["shu"]), "salt_pct": round(A["salt_pct"], 2),
        "perceived": r2(A["perceived"]), "raw": r2(A["raw"]), "gaps": A["gaps"],
        "body": {"index": round(A["body"], 2), "class": body_class(A["body"])[0]},
        "fat_level": round(A["fat_level"], 2),
        "heat_profile": {"peak_s": hp["peak_s"], "half_gone_s": hp["half_s"],
                         "zones": {k: round(v, 2) for k, v in hp["zones"].items()}},
        "aroma_staying_power_pct": {k: r2(v) for k, v in A["pyramid"].items()},
        "top_families": [{"family": FAM[i], "descriptor": FAMILIES[FAM[i]][1], "rel": round(tot[i] / tot.max(), 2)}
                         for i in np.argsort(-tot)[:8] if tot[i] > 0],
        "weakest_pairs": pairs[:3], "strongest_pairs": pairs[-3:][::-1],
        "drivers": {d: sorted(((rows[i]["ing"].name, round(A["shares"][i, j], 2)) for i in range(len(rows))
                               if A["shares"][i, j] > 0.3), key=lambda t: -t[1])[:3]
                    for j, d in enumerate(DIMS)},
        "warnings": A["warnings"], "recipe": A["recipe"],
    }
    if pairs:
        w = pairs[0]
        out["bridges_for_weakest_pair"] = {"pair": [w["a"], w["b"]], "bridges": bridges(
            db, db.get(w["a"]), db.get(w["b"]), top=5, exclude={r["ing"].name for r in rows})}
    if moves is not None:
        out["suggestions"] = [{k: v for k, v in m.items() if not k.startswith("_")} for m in moves]
    if opt_log is not None:
        out["optimization_steps"] = opt_log
    return out


