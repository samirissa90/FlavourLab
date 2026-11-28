---
name: coffee-expert
description: Coffee brewing and origin knowledge for the FlavorLab expert barista tool. Use for questions about V60 and pour-over recipes, espresso parameters and troubleshooting, milk temperatures and drink specs, other brew methods, grind sizes in microns, brewing water, coffee species and varieties, origins by altitude, processing, production volume, roast levels, freshness, the SCA flavor wheel, aroma compounds, key odorants, sources of bitterness, coffee defects (Rio taint), cupping (CVA), and caffeine and health (limits, sleep, blood pressure, cancer). Triggers: 'caffeine limit', 'caffeine and sleep', 'coffee blood pressure', 'coffee cancer', 'caffeine pregnancy', 'coffee bitterness', 'rio defect', 'key odorants', 'V60', 'pour over', 'espresso recipe', 'sour shot', 'bitter shot', 'grind size', 'brew water', 'Geisha', 'Gesha', 'variety', 'origin', 'altitude', 'SHB', 'washed or natural', 'roast level', 'Agtron', 'degassing', 'cupping score', 'CVA', 'flavor wheel'.
---

# Coffee Expert Data

Structured coffee data lives in `data/coffee/` (relative to the FlavorLab project root). Each dataset is a CSV with a same-named JSON file generated from it. Edit the CSV, then run the converter, which checks every row's column count:

```bash
python tools/csv_to_json.py data/coffee
```

The converter turns each CSV into a JSON array and parses `pours` into `{t_s, cum_g}` objects. It exits non-zero if any row has the wrong number of columns.

## Datasets

| File | Holds |
|---|---|
| `brew_recipes.csv` | Named recipes: V60 and pour-over, Kalita, Origami, WBC champions 2016-2025, AeroPress (WAC 2018-2025), French press |
| `brew_targets.csv` | Method-level ratio, temperature, time, TDS and EY envelopes (pour-over, SCA Golden Cup, AeroPress, French press, cold brew, siphon, Chemex) |
| `espresso_styles.csv` | Dose, yield, ratio, time, temperature, pressure by espresso style |
| `espresso_drinks.csv` | Drink specs: shots, milk volume, foam depth, cup size |
| `milk_temps.csv` | Steaming targets and caps by milk type |
| `troubleshooting.csv` | Symptom to diagnosis to action, for espresso and pour-over |
| `grind_sizes.csv` | Grind micron ranges by method, plus competition anchors |
| `water_profiles.csv`, `water_conversions.csv` | SCA and Third Wave profiles; mg/L conversion factors |
| `decaf_methods.csv` | Decaf methods and label thresholds |
| `species.csv` | Arabica, robusta, liberica, excelsa and others: ploidy, caffeine, altitude, rust, cup |
| `varieties_wcr.csv` | 24 arabica varieties from the World Coffee Research catalogue |
| `varieties_secondary.csv` | Varieties outside WCR (Sidra, Pink Bourbon, Castillo, JARC lines) and single lots |
| `gesha_auctions.csv` | Best of Panama Gesha top-lot prices by year |
| `origins_regions.csv`, `production_60kg.csv`, `auctions_origins.csv` | Origin regions, production volume and auction records (being built; check the file exists) |
| `altitude_grades.csv`, `altitude_quality_studies.csv`, `altitude_effects.csv` | Grade cutoffs by country, altitude studies, direction of altitude effects |
| `roast_levels.csv`, `roast_names.csv` | Agtron bands, drop temperatures, development ratios, roast-name mapping |
| `freshness_rules.csv` | Degassing and rest windows, storage notes |
| `processing_methods.csv` | Washed, natural, honey, anaerobic and related methods |
| `aroma_compounds.csv` | Odour-active compounds with wheel category and OAV |
| `flavor_wheel.csv` | SCA flavour wheel, one row per descriptor |
| `wcr_reference_standards.csv` | WCR lexicon reference standards |
| `cva_scales.csv` | CVA descriptive and affective scales, defect ratios, legacy 2004 values |
| `equipment_machines.csv`, `equipment_grinders.csv` | Machine and grinder presets (ECM Classika PID, Eureka Mignon, generic categories) with source and conflict notes |

**Optional local tables** (`coffee_*.csv`, not part of the repository; check they exist): key odorants, bitter compounds, defects, flavour chemistry, and caffeine and health (`coffee_health.csv`, see [Health questions](#health-questions)). Rows are labelled `reference-checked` or `unverified-reference` and carry no source: give the label and do not invent a source. The exception is current official rows in the health table, which are labelled `primary` and have a link. Read a row's `notes`, `brew_tested` or full `finding` before quoting a number, because some apply to one test only. None of them changes brew settings. Do not copy their contents into files that are committed. Search with `python flavorlab.py lookup TERM` or the chat box.

The full write-up is in `reports/Coffee brewing expert data.md`. Read it before changing a dataset.

The desktop app `coffee_flavourlab.py` has three guided tabs and a set of reference tables. Run it with `python coffee_flavourlab.py`; test with `python -m unittest test_brew_guide test_coffee_flavourlab`.

- **Brew guide** (`brew_guide.py`): the user picks method, origin, altitude, variety, process, roast and age. The engine returns dose, yield, time, temperature, pressure and grind guidance for their machine and grinder, each with a label and the reason.
- **My equipment**: asks about the machine and grinder (preset, then corrections). Saved in `coffee_equipment.json`.
- **Dial-in**: the user enters a pulled shot (dose, yield, time, taste, dial reading). The engine picks one change from `troubleshooting.csv` and, after two shots at different dial readings, measures seconds per dial unit for that grinder.

Rules the guide follows:
- Temperature is a point inside the sourced roast range, chosen by altitude band (label `inferred`). It never leaves the range.
- No absolute grinder dial number is ever invented. Mignon dial scales were not found in any source.
- The PID setting equals the target plus the user's measured offset. Whether the Classika's PID reads boiler or group water is not stated in the sources.
- Robusta has no sourced brew parameters; the guide warns and shows arabica values.

The chat box uses the same equipment, so its answers follow the rules below.

## Label rules

Every value carries a `confidence` (or `label`) field. Keep these rules when answering or building UI:

- **primary**: an official or peer-reviewed page was read (WCR, SCA forms, the WAC page, USDA, Smrke et al.).
- **secondary**: a trade, roaster or compilation page was read. Most recipes are here.
- **snippet**: the value came only from a search summary. Show it as provisional.
- **inferred**: derived from other numbers, or a tasting description turned into a score. Never show as a source rating.
- **unverified** or **unverified-bg**: no fetched source, or background knowledge. Do not present as fact.
- **reference-checked**: from reference material with no published source in this project, compared with the original page.
- **unverified-reference**: from the same kind of material, not compared with an original. Show it as provisional.
- **conflict**: sources disagree. Keep every value and show the conflict. Do not pick a winner silently.

## Health questions

Applies to caffeine, sleep, blood pressure, cancer, pregnancy and any other health question.

- **Information only.** Do not diagnose, set a personal dose, or advise on medicines or treatment. For someone's own condition, pregnancy, medicines or symptoms, tell them to ask a doctor or pharmacist.
- If `coffee_health.csv` is not installed, say the data is not available. Do not answer from memory as if it came from the data.
- **Lead with `current-guidance` rows** and give their link. They show what the page said when it was read; they may have changed since.
- Every other row is older research. Say so, and follow its `status`:
  - `agrees-with-current`: may be given alongside the current row.
  - `not-rechecked`: older evidence not compared with current research. Present it as that, with its `evidence` type and who was studied.
  - `use-current-caution`: give only together with the current caution. Never use it to reassure someone that an amount or timing is safe.
  - `replaced`: do not present as a finding. Mention only as history, after the current statement.
  - `unclear`: do not quote a direction or a number as a result.
- An association is not proof that coffee causes or prevents anything.

## Things the data does not support

- **No TDS for named recipes.** Only Rao publishes extraction yield (22-24.5%). Do not invent a per-recipe TDS.
- **No 100-point conversion for CVA.** The total-score formula was not retrieved. Show CVA affective scores as 1-9 per attribute.
- **Acidity, body and sweetness on origins are estimates.** No source gives numeric ratings.
- **Gesha 88-94 auction range is unsourced.** The 2025 record is 98 points at $13,705/lb.
- **Grind micron ranges conflict** with the brief's own ranges. The sourced V60 range is 400-700 um; the brief's 600-900 um is unverified.
- **Drink specs are missing** for affogato, breve, red eye, gibraltar, galao and cafe au lait.
- **Espresso dose:** the 14 g figure for Cameron et al. is unconfirmed; sources say 15 g.

## Answering

1. Look up the dataset that matches the question, and filter on the method or variety.
2. Give the value with its label, e.g. "Hoffmann 30 g / 500 g, 1:16.7 (inferred), secondary".
3. If the row has a conflict group, show all values.
4. For a brew problem, use `troubleshooting.csv` and say which variable to change first.
