# FlavourLab: user guide

Your kitchen and coffee assistant. Two tools in one project:

| | What it does | Start it with |
|---|---|---|
| **Sauce lab** (FlavorLab) | Design a sauce from ingredients, see its taste, aroma and heat profile, find pairings, and get suggestions to improve it | `python flavorlab_ui.py` |
| **Coffee lab** (Coffee Flavourlab) | A guided brewing assistant: tell it your coffee and your machine, get settings, then fine-tune shot by shot | `python coffee_flavourlab.py` |

**Contents:** [Install](#1-install) · [Sauce lab](#2-sauce-lab) · [Coffee lab](#3-coffee-lab) · [Trusting the numbers](#4-trusting-the-numbers) · [Troubleshooting](#5-troubleshooting) · [Reference](#6-reference)

---

## 1. Install

1. Install **Python 3.9 or newer** (the coffee lab was tested on 3.12). Tkinter comes with Python on Windows and macOS.
2. Download this repository:
   ```bash
   git clone https://github.com/samirissa90/FlavourLab.git
   cd FlavourLab
   ```
3. Install the packages the **sauce lab** needs. The coffee lab needs nothing extra.
   ```bash
   pip install numpy matplotlib Pillow
   ```

To check the coffee lab, run its tests:
```bash
python -m unittest test_brew_guide test_coffee_flavourlab
```
The sauce lab has a smoke test:
```bash
python test_flavorlab.py
```

---

## 2. Sauce lab

### Start
```bash
python flavorlab_ui.py
```
The window has six tabs.

| Tab | Use it to |
|---|---|
| **Recipe Designer** | Build a recipe and watch its scores update live |
| **Sauce Card** | See the full one-page analysis of your recipe (zoomable) |
| **Pairing & Bridge** | Find what goes with an ingredient, or what links two ingredients |
| **Flavor Map** | See where ingredients sit relative to each other |
| **Compare** | Put up to 3 recipes side by side |
| **Ingredient Browser** | Look through the 300+ ingredients |

Every chart tab has an **Export PNG** button.

### Your first sauce, step by step
1. Open **Recipe Designer**.
2. Search for an ingredient on the left (for example `habanero`) and press **Add to recipe**. Add a few more, such as `mango`, `apple cider vinegar` and `salt`.
3. **Double-click the grams** of any row to set the amount.
4. **Click the prep** of a row to set it to roasted, smoked, charred and so on.
5. To add something after cooking (lime juice, fresh herbs), tick **finish (added after cooking)** in that row's dialog. Finishing ingredients keep their top notes and sinus kick.
6. Pick a **Style** at the top (for example `fruity_caribbean`) and a **Process** (cooked or raw).
7. Read **Live analysis** on the right: the overall score and the main warnings.
8. Press **Suggest** to get the single changes that help most, or **Auto-optimize** to let it try several steps for you.
9. Press **Render full sauce card** to open the full analysis in the **Sauce Card** tab.
10. Use **New**, **Load…** and **Save…** above the recipe to start over, open a saved recipe or save yours. Saved recipes also work from the command line.

Press **Del** to remove the selected row.

### Pairings
Open **Pairing & Bridge**, choose an ingredient, and press **Show pairing wheel** to see its best partners and why they work. Fill in a second ingredient to see which ingredients link the two (a "bridge"), for example `kenyan coffee` and `chipotle`.

### Reading the sauce card
| Panel | What it tells you |
|---|---|
| Taste and aroma radars | Your sauce against the style target. "Gap to target" shows what is too much or too little |
| Who drives each flavor | Which ingredient contributes what |
| Formula and checks | Grams, process, and warnings (pH, salt, astringency, lost top notes) |
| Heat panel | Estimated heat (SHU), how it builds over time, and where in the mouth it hits |
| Mouthfeel | Astringency, cooling, numbing, sinus heat, bite, and body from thin to paste |
| Aroma staying power | Top, middle and base notes: fresh, after cooking, after about 3 months |
| Aroma families | Which of the 30 aroma families dominate the nose |
| Pairing matrix | How well the ingredients pair with each other |
| Next best moves | The changes that would improve the score most |

> **Safety:** all values are estimates for designing, not lab results. Always measure the real pH of a sauce you plan to keep: aim for **3.5 to 4.0** and treat **4.6 as the limit**.

### Adding your own ingredients
The app reads every `ingredients*.csv` file in the folder and rechecks them about every 3 seconds, so edits show up without a restart. To add ingredients, drop in a new file named `ingredients_<yourname>.csv` with the same columns as the existing ones. A bad row is skipped and counted at the bottom right of the window (click the count to see why).

### Command line (optional)
```bash
python flavorlab.py card recipes/mango_habanero.json       # sauce card image
python flavorlab.py quick "habanero:120,mango:250,apple cider vinegar:200,lime juice:30:finish,salt:12" --style fruity_caribbean
python flavorlab.py pair habanero --with mango             # pairing wheel
python flavorlab.py bridge "kenyan coffee" chipotle        # what links two ingredients
python flavorlab.py lookup TERM                            # search the optional reference tables, if installed
python flavorlab.py map --highlight "habanero,mango"       # flavor map
python flavorlab.py compare a.json b.json                  # side-by-side radars
python flavorlab.py list                                   # all ingredients (also: info NAME, families, styles, preps)
```
Images are written to the `out/` folder (change it with `--out DIR`). Add `--json` to `card`, `quick`, `pair` or `bridge` for machine-readable output.

---

## 3. Coffee lab

### Start
```bash
python coffee_flavourlab.py
```
Use the tabs from left to right: **Brew guide**, **My equipment**, **Dial-in**. The tabs after those (Combination grid, Origins, Varieties, Recipes, Troubleshoot, Data browser) are reference tables. The chat box at the bottom is always available.

### Step 1: tell it about your equipment (My equipment tab)
The app starts with an **ECM Classika PID** espresso machine and a **Eureka Mignon** grinder as examples.

1. Choose your **machine** and **grinder** from the lists.
2. Correct anything that differs on your unit: boiler system, pump, temperature control, how you adjust pressure, pre-infusion, basket size, and which way is finer on your grinder.
3. **Measured offset** is the difference between your machine's temperature setting and the real water temperature in the cup. Leave it at `0` until you have measured it with a thermometer.

Changes save automatically to `coffee_equipment.json`.

### Step 2: describe the coffee (Brew guide tab)
On the left, choose:
- **Brew method** (espresso, V60 and pour over, AeroPress, French press, cold brew, siphon, Chemex, moka pot) and, for espresso, the **style** (ristretto, normale, lungo)
- **Country and region.** Picking a region fills in its typical altitude. Overwrite it with the number on your bag if you have one.
- **Variety, process** (washed, natural, honey, anaerobic and others), **roast** and **days since roasting**
- **Dose** in grams. Leave it blank to use your basket size.

The right side updates as you change anything:
- A **recipe card** at the top with dose in, liquid out, time, temperature and pressure
- Each setting with a **confidence label** and the reason for it
- **Step-by-step instructions for your equipment**
- **Check these** warnings, such as beans that are too fresh, or an altitude that does not match the region
- **Questions for you**, which you can answer in My equipment

**Example.** Ethiopia, Sidama, washed, light roast, 9 days off roast, on the Classika PID:
- 18 g in, 36 g out in 25 to 30 seconds
- Water at 96 C. At high altitude the guide picks the top of the light-roast range (94 to 96 C), and it labels that choice `inferred`
- 9 bar pump pressure
- Because the Classika is a single-boiler machine, the steps tell you to pull the shot first and to cool and refill the boiler after steaming milk

### Step 3: fine-tune after each shot (Dial-in tab)
1. Pull a shot with the guide's settings.
2. Enter **dose in**, **liquid out**, **time**, and **how it tastes** (sour, balanced, bitter and so on).
3. Enter your **grinder dial reading** as a number if your dial has one.
4. Press **Record shot and advise**. You get one change to make, such as "grind 1 setting finer", in the direction your grinder turns.

Change **one thing per shot**. After two shots at different dial readings, the app measures how many seconds one dial unit changes your shot time and tells you what dial number to try next. It never invents a dial number for a grinder it has no data for. For example, it measured -5 seconds per dial unit from a shot at dial 12 (17 s) and one at dial 11 (22 s), and suggested dial 9.9 to reach 27.5 s.

Your shots are listed in the table and saved to `coffee_equipment.json`. **Clear history** empties it. Dial-in advice covers espresso. For filter coffee, use the Troubleshoot tab.

### The chat box
Type a question at the bottom, for example `sour and fast espresso`, `ethiopia altitude`, `oat milk temperature`, `geisha` or `help`. Type `my machine` or `my guide` to see your equipment and current settings. It answers from the local data files. **It is not an online AI model.**

### What it does not know
- **No absolute grinder numbers.** No source for Eureka Mignon dial settings was found, so you get a direction and a measured method, not a made-up starting number.
- **The ECM Classika PID details come from reviews and retailers.** ECM's own page could not be read, and sources disagree on the boiler size (0.75 L or half a litre). Check your machine's manual.
- **Robusta, moka pot and Chemex** have little or no sourced brewing data, and the guide says so instead of guessing.
- **Temperature within a range** (for example 94 to 96 C) is chosen by altitude using a rule of this project. It is labelled `inferred`.

---

## 4. Trusting the numbers

The coffee data (`data/coffee/`, `research_notes/`, `reports/`) is a **user collection** compiled with AI-assisted web research from public pages, studies and trade sources. **It has not been verified.** Check the original source before relying on a number. The sources keep their own copyright and terms.

Every coffee value carries a label:

| Label | Meaning |
|---|---|
| `primary` | Read on an official or peer-reviewed page |
| `secondary` | Read on a trade, roaster or retailer page |
| `snippet` | Seen only in a search summary. Treat as provisional |
| `inferred` | Worked out from other numbers or by this project's rules |
| `conflict` | Sources disagree. The data shows both values |
| `unverified` | No source was read. Do not treat as fact |
| `reference-checked` | Reference material with no published source here. Compared with the original page |
| `unverified-reference` | Reference material with no published source here, not checked against an original. Provisional |

The sauce data in `ingredients*.csv` is made of estimates, not lab data. For the base pack `ingredients.csv`, `data/ingredient_value_sources.csv` records where the mouthfeel, body, heat-timing, volatility and re-split "pungent" values came from: `guide` (stated in `FLAVOR_GUIDE.md`), `similar` (copied from a named ingredient), `rule`, or `estimate`. Most are estimates.

### Optional reference tables

The apps can read extra local tables from `data/flavor_science/` and `data/coffee/coffee_*.csv`. They are **not included** in this repository. When present, they add key aroma compounds to ingredient details, results to `lookup` and the coffee chat, and advisory notes on recipes. Without them everything else works the same. Their rows carry no source link: `reference-checked` was compared with an original, `unverified-reference` was not, and `conflict` means the original disagrees with itself. If the coffee health table is installed, the chat also answers caffeine and health questions. It shows current official statements first (labelled `primary`, with a link) and marks older research. This is information, not medical advice.

---

## 5. Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: numpy` (sauce lab) | `pip install numpy matplotlib Pillow` |
| The window does not open on Linux | Install Tkinter: `sudo apt install python3-tk` |
| An ingredient row is "skipped" | Click the count at the bottom right of the sauce lab for the reason |
| Coffee app shows odd equipment | Delete `coffee_equipment.json`. The app recreates the default (ECM Classika PID + Eureka Mignon) |
| You edited a coffee CSV | Rebuild the JSON files: `python tools/csv_to_json.py data/coffee`. It reports any row with the wrong number of columns |
| Your own shots appear in git | `coffee_equipment.json` is tracked as an example and the app rewrites it. Do not commit your own shots |

---

## 6. Reference

### Files
| File | Purpose |
|---|---|
| `flavorlab_ui.py` | Sauce lab desktop app |
| `flavorlab.py` | Sauce lab charts and command line |
| `model.py` | Sauce model: data, perception, pairing and JSON summary. No plotting, so other programs can `import model` |
| `ingredients.csv`, `ingredients_v02.csv`, `ingredients_v03.csv` | Ingredient packs (311 ingredients). Later files override earlier ones |
| `data/ingredient_value_sources.csv` | Where the base pack's mouthfeel, body, heat and volatility values came from |
| `FLAVOR_GUIDE.md` | The flavor science behind the numbers |
| `coffee_flavourlab.py` | Coffee lab desktop app |
| `brew_guide.py` | Coffee guide engine (settings, equipment, dial-in). No UI code |
| `coffee_knowledge.py` | Coffee data lookup and chat answers. No UI code |
| `coffee_equipment.json` | Example equipment profile, rewritten by the app |
| `data/coffee/` | Coffee datasets as CSV with a matching JSON file |
| `tools/csv_to_json.py` | Converts and checks the coffee CSV files |
| `reports/`, `research_notes/` | The research behind the coffee data |
| `.claude/skills/` | Claude Code skills: barista, flavorlab, coffee-expert |
| `test_*.py` | Tests |

### Recipe file format (sauce)
```json
{"name": "Mango Habanero", "style": "fruity_caribbean",
 "process": "cooked",
 "fermented": false,
 "ingredients": [{"item": "habanero", "g": 120},
                 {"item": "garlic", "g": 20, "prep": "roasted"},
                 {"item": "lime juice", "g": 30, "stage": "finish"}]}
```
- `process` is `cooked` or `raw` and controls aroma loss.
- `fermented` is `true` (ferment the chili, fruit, veg and herbs) or a list of names.
- **Preps:** raw, roasted, charred, smoked, toasted, caramelized, fermented. Combine them with a list in JSON or with `+` in quick mode.
- `"stage": "finish"` (or `:finish` in quick mode) means the ingredient goes in after cooking.

### How the sauce model works
These are heuristics you can edit, not lab data.
- **Intensity:** Σ(mass share × potency × vector), compressed with `10·(1−e^(−x/3))` to model saturation. It applies to 6 tastes, 9 aroma axes and 5 trigeminal axes.
- **Heat:** Σ(mass share × pod SHU × solids), mapped to a 0-10 log scale. Heat character comes from each chili's onset, length and zone.
- **Interactions:** sugar rounds acid and damps heat. Salt suppresses bitterness and boosts umami. Acid sharpens heat and saltiness. Fat damps heat, bite and astringency. Sugar softens astringency. Menthol takes the edge off capsaicin. Big heat masks fruity and floral notes.
- **Volatility:** each ingredient is a top, middle or base note. Cooking keeps 40%, 75% and 100% of those aromas. Three months of storage keeps a further 60%, 85% and 100%.
- **Body** = Σ(mass share × body). Xanthan gum is rated 500, so 0.2% adds about 1 point.
- **Pairing score** (0-100) combines aroma-family similarity, aroma-axis similarity, taste and trigeminal contrast, how often the two categories work together, a bonus for classic pairings, minus clashes.
- **Overall score** = 0.75 × style fit + 0.25 × harmony.

To retune, edit `STYLES`, `PREP` and `CLASSIC` in `model.py`, or the functions `perceive()` (interactions), `pair_score()` (pairing), `VOL_KEEP` and `AGE_KEEP` (aroma loss), and `ONSET_S` and `LENGTH_S` (heat curve).

### How the coffee guide decides
- Dose, yield, time and pressure come from the sourced espresso style rows (baseline 18 g to 36 g in 25 to 30 s, 9 bar).
- Temperature is a point inside the sourced roast range (espresso light 94-96, medium 93, dark 90-92 C), picked by altitude band: below 1200 m the bottom of the range, 1200 to 1600 m the middle, above 1600 m the top.
- The machine setting is the target plus your measured offset.
- Dial-in advice comes from the troubleshooting table and is converted into your grinder's direction.

### Changelog
- **v0.4:** Completed the base ingredient pack: mouthfeel, body, heat timing and volatility (mostly estimates), and re-split the old "pungent" score into aroma, sinus heat and bite, so heat timing, aroma staying power and pairing scores differ from v0.3. Added broccoli, cauliflower, hazelnuts and jambu; fixed Sichuan peppercorn having no numbing. The bitter × astringent pairing penalty now counts only when one ingredient is more bitter and the other more astringent, so what both share is not penalised again; some bitter pairs score higher. Support for optional local reference tables, with a `lookup` command.
- **v0.3:** Coffee Flavourlab: interactive brew guide, equipment questions, dial-in loop, coffee datasets and research, Claude Code skills. This user guide.
- **v0.2:** 30 refined aroma families, trigeminal axes, heat character, body and volatility, 164 new ingredients, new sauce card panels, `bridge` and `families` commands, the `sichuan_mala` style.
- **v0.1:** first release.

Colors use a palette validated for color vision deficiency (CVD-safe).
