# FlavourLab

Your kitchen and Coffee assistant.

## Coffee Flavourlab
An interactive brewing guide: pick the method, origin, altitude, variety, process and roast, tell it about your machine and grinder, and it gives settings (dose, yield, time, temperature, pressure) with a confidence label on each value. A dial-in tab turns each shot you pull into the next adjustment.
```bash
python coffee_flavourlab.py                                  # the app (Tkinter, no extra packages)
python -m unittest test_brew_guide test_coffee_flavourlab    # headless tests
python tools/csv_to_json.py data/coffee                      # rebuild the JSON files after editing a CSV
```
- `brew_guide.py` is the guide engine and `coffee_knowledge.py` the data lookup. Neither has UI code.
- `coffee_equipment.json` is an **example equipment profile** (ECM Classika PID and a Eureka Mignon). The app rewrites it when you change equipment or log shots, so edit it to match your own gear.
- `data/coffee/` holds the datasets as CSV with a matching JSON file. `reports/` and `research_notes/` hold the research behind them.

### Data sources: please read
The coffee data (`data/coffee/`, `research_notes/`, `reports/`) is a **user collection** compiled with AI-assisted web research from public pages, studies and trade sources. **It has not been verified.** Each row carries a `confidence` label (`primary`, `secondary`, `snippet`, `inferred`, `conflict`, `unverified`) and a source link where one was found, and some values are labelled `unverified` or `inferred` or are known to conflict between sources. Check the original source before relying on a number. The sources keep their own copyright and terms. The equipment presets (ECM, Eureka) come from retailer and review pages, not manufacturer specifications. The values in `ingredients*.csv` are estimates, not lab data.

## FlavorLab v0.2: visual flavor design

FlavorLab is a static chart generator plus a JSON analysis tool for designing dishes. Its first module covers **hot sauces**.
Requires Python 3.9+ with `numpy` and `matplotlib`.

Files:
- `flavorlab.py`: charts and CLI
- `model.py`: data, perception model, pairing and JSON summary. It has no plotting, so agents can `import model` directly.
- `ingredients.csv` + `ingredients_v02.csv`: ingredient packs, 307 ingredients in total. Every `ingredients*.csv` in the folder is loaded, and later files override earlier ones.
- `FLAVOR_GUIDE.md`: the flavor science behind the numbers
- `test_flavorlab.py`: smoke checks

## Desktop UI
```bash
python flavorlab_ui.py        # needs numpy, matplotlib, Pillow (Tkinter ships with Python)
python test_flavorlab_ui.py   # headless smoke test (uses a temp fixture pack, never your CSVs)
```
Tabs: **Recipe Designer** (pick ingredients, set grams / preps / finish, live scores, suggestions, auto-optimize, save/load recipe JSON), **Sauce Card** (zoomable), **Pairing & Bridge**, **Flavor Map**, **Compare**, **Ingredient Browser**. Every chart view has Export PNG.
- Ingredients are read from every `ingredients*.csv` and re-checked every ~3 s, so edited or new packs appear without a restart. An invalid row is skipped and counted at the bottom right (click it for details); an unreadable file keeps the last good list.
- Recipes saved from the UI use the CLI format (`python flavorlab.py card recipes/x.json` works on them).

## Commands
```bash
python flavorlab.py card recipes/mango_habanero.json             # sauce card PNG
python flavorlab.py card recipes/x.json --optimize 3             # + improved recipe, card, before/after radars
python flavorlab.py quick "habanero:120,mango:250,apple cider vinegar:200,lime juice:30:finish,salt:12" --style fruity_caribbean
python flavorlab.py quick "..." --raw                            # uncooked sauce (no aroma loss)
python flavorlab.py pair habanero --with mango                   # pairing wheel + why they pair
python flavorlab.py bridge "kenyan coffee" chipotle              # ingredients that link two others
python flavorlab.py map --highlight "habanero,mango"             # PCA flavor map of the whole database
python flavorlab.py compare a.json b.json [c.json]               # taste / aroma / mouthfeel radars
python flavorlab.py list | info NAME | families | styles | preps
python test_flavorlab.py                                         # model smoke checks
```
Add `--json` to `card`, `quick`, `pair` or `bridge` to get machine-readable output for agents. Use `--out DIR` to choose the output folder (default `out/`).

## Recipe format
```json
{"name": "Mango Habanero", "style": "fruity_caribbean",
 "process": "cooked",                      // or "raw" - controls aroma loss
 "fermented": false,                       // true = ferment chili/fruit/veg/herb, or a list of names
 "ingredients": [{"item": "habanero", "g": 120},
                 {"item": "garlic", "g": 20, "prep": "roasted"},
                 {"item": "lime juice", "g": 30, "stage": "finish"}]}
```
- **Preps:** raw, roasted, charred, smoked, toasted, caramelized, fermented. Combine them with a list in JSON or with `+` in quick mode.
- **Finish stage:** `"stage": "finish"` (or `:finish` in quick mode) means the ingredient goes in after cooking, so its top notes and sinus kick survive.

## What the sauce card shows
1. **Taste and aroma radars** compare the perceived profile, the style target and the raw sum. **Gap to target** shows what is too much or too little for the style.
2. **Who drives each flavor** splits each bar into each ingredient's share. **Formula and checks** lists grams, the process and the warnings: pH, salt, astringency, lost top notes and cooked-off mustard heat.
3. **Heat panel:**
   - estimated SHU against commercial sauces
   - **heat over time**: capsaicin curve built from each chili's onset and length, plus pepper bite, sinus heat and numbing curves, and where in the mouth it hits (front, mid, back)
4. **Mouthfeel and trigeminal:** astringency, cooling, numbing, sinus heat, pepper bite and fat coating, plus a **body gauge** (thin, pourable, thick, paste).
5. **Aroma staying power:** top, middle and base notes in the fresh blend, after cooking and after about 3 months.
6. **Aroma families:** which of the 30 families dominate the nose, and which ingredients they come from.
7. **Pairing matrix:** harmony is the impact-weighted mean of the pair scores.
8. **Next best moves:** the single additions, increases, decreases or removals that most improve the overall score.

## The model (heuristic: edit and extend)
- **Intensity.** The mix is Σ(mass share × potency × vector), compressed with `10·(1−e^(−x/3))` to model saturation. This applies to 6 tastes, 9 aroma axes and 5 trigeminal axes.
- **Heat.** Σ(mass share × pod SHU × solids), mapped to a 0-10 log scale. **Heat character** comes from each chili's onset (1-5), length (1-5) and zone.
- **Interactions:**
  - Sugar rounds acid and damps heat.
  - Salt suppresses bitterness and boosts umami.
  - Acid sharpens heat and saltiness.
  - Fat damps heat, bite and astringency.
  - Sugar softens astringency.
  - Menthol takes the edge off capsaicin, and capsaicin overrides menthol's cooling.
  - Big heat masks fruity and floral notes.
- **Volatility.** Each ingredient is a top (t), middle (m) or base (b) note. Cooking keeps 40%, 75% and 100% of those aromas. Three months of storage keeps a further 60%, 85% and 100%.
- **Body** = Σ(mass share × body). Xanthan gum is rated 500, so 0.2% adds about 1 point.
- **Pairing score** (0-100) is built from:
  - aroma-family similarity (exact family plus same family group)
  - aroma-axis similarity
  - taste and trigeminal contrast
  - how often the two categories work together
  - a bonus for classic pairings
  - minus clashes
- **Overall score** = 0.75 × style fit + 0.25 × harmony.

All values are **estimates to guide design, not lab data**. Always measure pH: aim for 3.5-4.0, and treat 4.6 as the limit.

## Upgrading
- **Ingredients:** add rows to any pack, or drop in a new `ingredients_<name>.csv` with the same columns. Write the `aroma` column as `family:weight;family:weight`, using weights 1-3 and families from `families`.
- **Styles, preps and classic pairings:** edit `STYLES`, `PREP` and `CLASSIC` in `model.py`. Style targets can include trigeminal axes (see `sichuan_mala`).
- **Retune:** `perceive()` (interactions), `pair_score()` (pairing), `VOL_KEEP` / `AGE_KEEP` (aroma loss), `ONSET_S` / `LENGTH_S` (heat curve).
- **Roadmap:** coffee brewing module, Brix/pH entry from real measurements, interactive HTML.

### Changelog
- **v0.2:**
  - 30 refined aroma families with weights
  - trigeminal axes, heat character, body and volatility
  - 164 new ingredients (chilis, coffee origins, teas, ferments, Asian, Middle-Eastern and African pantry)
  - non-allium pungency moved from the allium axis to the trigeminal axes
  - new panels on the sauce card
  - `bridge` and `families` commands
  - code split into `model.py` (no plotting) and `flavorlab.py` (charts and CLI); ingredient packs
  - `sichuan_mala` style
- **v0.1:** first release.

Colors use a palette validated for color vision deficiency (CVD-safe).
