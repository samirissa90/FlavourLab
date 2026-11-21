# Other Brew Methods, Grind-Size Reference (microns), and Brewing Water Chemistry

Research date: 2026-11-19. Scope: non-V60 / non-espresso methods, grind microns by method, water chemistry, strength/extraction concepts. Field names for CSV/JSON: method, dose_g, water_g, ratio, temp_c, grind_um_min, grind_um_max, time_s, tds_pct, ey_pct, source_url.

Research limits (read first): many primary pages blocked automated fetch (Barista Hustle 402, SCA PDFs 404, Nature paywall redirect). Where a number comes from a web-search summary rather than a fetched page, it is marked "(search-snippet)". Where I could not find a source, the item is in Gaps and NOT given a value. Numbers the assignment brief supplied (e.g., Chemex 1:15-1:17, Turkish 100-250 um) are listed as "brief-supplied, unverified" and are not presented as sourced.

---

## 1. Brew methods: dose, ratio, temp, grind, time, agitation, TDS/EY, popular recipes

### Takeaway
Solid sourced data exists for AeroPress (Hoffmann recipe plus the full official World AeroPress Championship 2009-2025 recipe table), SCA Golden Cup brewer parameters (92-96 C, 55 g/kg, 1.15-1.35% TDS, 18-22% EY), and rough ratio/shelf-life ranges for cold brew. French press and moka have only secondary write-ups of Hoffmann's methods with conflicting amounts. Chemex, Kalita, Melitta, Clever, flat-bottom drippers, cezve, phin and cupping have no verified numbers in this pass (see Gaps).

### Cited Findings

#### AeroPress - Hoffmann "Ultimate" (CSV-ready)
```csv
method,recipe,author,dose_g,water_g,ratio,temp_c,grind_descriptor,grind_um_min,grind_um_max,time_s,agitation,tds_pct,ey_pct,source_url
aeropress_standard_upright,Ultimate AeroPress,James Hoffmann,11,200,1:18.2,99,finer end of medium (light roast),,,200,"plunger inserted ~1 cm for vacuum, steep 120 s, swirl, wait 30 s, press ~30 s",,,https://aeroprecipe.com/recipes/james-hoffmann-aeropress-recipe
```
- Hoffmann Ultimate AeroPress: 11 g light roast, 200 g water at 99 C, paper filter, standard (upright) position, no rinse or preheat, total 3:20; pour, plunger ~1 cm in, wait 2:00, swirl, wait 0:30, press ~0:30. Page also suggests 90-95 C for medium roasts and 85-90 C for dark (page's own adjustment, not Hoffmann-attributed with certainty) — [aeroprecipe](https://aeroprecipe.com/recipes/james-hoffmann-aeropress-recipe)
- Grind example from same page: Timemore C2 at 11 clicks for light roast (user suggestion) — [aeroprecipe](https://aeroprecipe.com/recipes/james-hoffmann-aeropress-recipe)
- Third-party summaries conflict on Hoffmann timing (2:00 steep, 2.5-3 min, or ~3:30 total) and no Hoffmann primary source was fetched — [search results incl. LAMOSE](https://secure.lamose.com/blogs/recipes/james-hoffmanns-aeropress-recipe-world-champion-method) (search-snippet)
- Another AeroPress recipe note: 14 clicks Comandante C40 or 12 clicks Timemore C2 for light roast at fine-medium grind — [aeroprecipe supersized recipe](https://aeroprecipe.com/recipes/supersized-aeropress-coffee-double-press) (search-snippet)

#### AeroPress - World AeroPress Championship (WAC) official recipes, 2018-2025
All rows from the official WAC recipes page: [https://worldaeropresschampionship.com/pages/recipes](https://worldaeropresschampionship.com/pages/recipes). "water_g" is brewing water before bypass; bypass listed separately. time_s is approximate end-of-press time where the page gives it.
```csv
method,year,place,author,country,position,dose_g,water_g,temp_c,grind_note,time_s,bypass,source_url
aeropress_wac,2025,1,Nemo Pop,Australia,upright,18,100 (+70 g @50C placed in carafe first),84,"Trailmaster x25 31 clicks, sifted 200 um",~70 (stir 25 s; press from 50 s ~20 s),"70 g @50C pre-brew in carafe; water 125 ppm",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2025,2,Jan Ahrend,Switzerland,inverted,18,100,88,"C40 Mk4 24 clicks",~120 (flip 1:30; press to 66 g),"dilute to 152 g total",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2025,3,Dharun Vyas,India,inverted,16,65 then to 208 ml total,88,"C40 Red Clix 52 clicks",~90,"12 ml room temp",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2024,1,George Stanica,Romania,inverted,18,~100 (50+50),96,"C40 Mk4 58 clicks (page states 870 um)",~135 (bloom 30 s; cap 1:20; press 1:35 for 30-40 s),"warm water to 130-135 g total then 20-30 g room temp 0 ppm",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2024,2,Sophan Nugraha,Indonesia,inverted,18,190 total (60 ml room-temp bloom),95,"C40 nitro blade 22 clicks",120,"10 ml room temp",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2024,3,Jamika (Mahmoud),Egypt,inverted,18,150 (50 @80C + 100 @75C),75-80,"MK4 900 um (page states)",~120,"30 ml room temp",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2023,1,Tay Wipvasutt,Thailand,inverted,18,100,89,"ZP6 65 clicks",~125 (flip+press 1:35 ~30 s),"room-temp water to 115 g then hot water to 155 g",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2023,2,Carlo Graf Bulow,Germany,inverted,18,160 (50 g bloom),100,"C40 32 clicks",~110,"room temp to 150 g",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2023,3,Leon Zhang,China,upright,18,100 @93 + 135 @75,75-93,"C40 27 clicks",100,not stated,https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2022,1,Jibbi Little,Australia,inverted,18,94 (setup lists 150),90,"Kinu setting 4",~130,"90C water to 150 g",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2022,2,Simon Derutter,Belgium,upright,18,140 (156 total),85,"Comandante 23 clicks",~105,"to 156 ml total",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2022,3,Jennifer Rui Ping Ho,Singapore,inverted,18,200,84,"Comandante 30 clicks",120,not stated,https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2021,1,Tuomas Merikanto,Finland,inverted,18,200 (50 @80C first),80,"Macap Labo 70D 7.0",~120,not stated,https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2019,1,Wendelien van Bunnik,Netherlands,inverted,30,100,92,"EK43S 7/10",60,"100 g added (120 g total)",https://worldaeropresschampionship.com/pages/recipes
aeropress_wac,2018,1,Carolina Garay,USA,inverted,34.9,100,85,"EK43S 8/10",~90,"60 g @85C + 40 g room temp (200 g total)",https://worldaeropresschampionship.com/pages/recipes
```
Page-stated patterns (derived by me from the table): 2022-2025 winners use 16-18 g doses vs 30-35 g in 2017-2019; 2023-2025 podium positions are mostly inverted with a room-temperature or warm bypass step (Nemo Pop 2025 and Leon Zhang 2023 are upright per the page). Earlier years (2009-2017) are in the same page (e.g., 2017 Paulina Miczka 35 g/150 g @84C inverted; 2016 Filip Kucharczyk 35 g/150 g @81C inverted).
- Conflict on 2024: the official page lists George Stanica at 96 C with ~100 g brew water; a Contour Coffee write-up lists 92 C/200 g/~2 min — [Contour Coffee](https://contour-coffee.pages.dev/journal/2024-george-stanica-aeropress-champion) (search-snippet); Barista Magazine names the winner "George Popescu" — [Barista Magazine](https://www.baristamagazine.com/george-popescu-the-software-engineer-who-brewed-his-way-to-aeropress-victory) (search-snippet). Prefer the official WAC page.
- Conflict on 2025 position: a search summary says 2023-2025 were all inverted; the official WAC page shows Nemo Pop 2025 as upright. Prefer the official page.
- Third Wave Water published a WAC 2025 playbook — [Third Wave Water](https://thirdwavewater.com/blogs/news/here-s-your-third-wave-water-wac-2025-aeropress-playbook) (title only seen; content not read)

#### French press
- Hoffmann "Ultimate French Press Technique" video: one source says uploaded 2016 (the brief says 2018) and is his most-viewed video; plunge is skipped, the filter only holds back grounds — [LAMOSE / search results](https://secure.lamose.com/blogs/recipes/james-hoffmanns-french-press-method-the-better-way) (search-snippet)
- Secondary write-ups of the Hoffmann method disagree on amounts: 30 g coffee / 500 g water, 4 min steep, stir to break crust, 5-8 min settle — [LAMOSE](https://secure.lamose.com/blogs/recipes/james-hoffmanns-french-press-method-the-better-way); 30 g / 450 g (1:15), water ~200 F (~93 C), total 10-12 min — [Fluent in Coffee](https://www.fluentincoffee.com/?p=5034242); 15 g / 225 ml, 4 min, stir and skim — [Volcanica](https://volcanicacoffee.com/blogs/news/video-guide-french-press-technique-3-recipes-tested). All search-snippet; none verified against the video.
- Hoffmann quoted "do nothing at all for at least five minutes" after the stir — [Imbibe](https://imbibemagazine.com/?p=91280) (search-snippet)
```csv
method,recipe,author,dose_g,water_g,ratio,temp_c,grind_descriptor,time_s,agitation,tds_pct,ey_pct,confidence,source_url
french_press,Hoffmann (LAMOSE summary),James Hoffmann,30,500,1:16.7,,coarse,240+300-480 settle,"stir to break crust at 4:00, skim, no plunge",,,secondary,https://secure.lamose.com/blogs/recipes/james-hoffmanns-french-press-method-the-better-way
french_press,Hoffmann (Fluent in Coffee summary),James Hoffmann,30,450,1:15,93,medium-coarse,600-720,"stir, skim foam",,,secondary,https://www.fluentincoffee.com/?p=5034242
```

#### Moka pot
- Hoffmann variation: fill base with water just off the boil (rather than cold) so the pot spends less time on heat and avoids scorching — [HuffPost UK](https://huffingtonpost.co.uk/entry/james-hoffmann-moka-pot-coffee-routine_uk_673b1cc9e4b0ebe12e36b57d) (search-snippet)
- Third-party (unattributed to a specific URL in my notes): 3-cup recipe ~17 g medium-fine, untamped, levelled; ~90 C starting water. Another source says Hoffmann suggested coarser grind plus an AeroPress filter on top of the basket. Sources disagree; treat as unverified — candidate pages: [Home-Barista 3-cup tips](https://www.home-barista.com/brewing/tips-for-3-cup-moka-pot-t94923.html), [xBloom timer](https://bloom-timer-ten.vercel.app/xbloom/moka-hoffmann) (search-snippet)
- Bialetti guidance: medium-fine grind, "feels gritty when rubbed between your fingers, but not powdery" (bialetti.co.nz, as quoted by) — [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/)

#### Batch brew / drip machines (SCA Golden Cup)
- Golden Cup zone: 1.15-1.35% TDS and 18-22% extraction ("ideal" region of the Brewing Control Chart) — [Nature Sci. Reports s41598-020-73341-4](https://www.nature.com/articles/s41598-020-73341-4) (search-snippet; page paywalled)
- Brewer certification: water 92-96 C; must reach 92 C within the first minute, stay >=92 C for the cycle, never exceed 96 C. Same paper states no supporting data is given in the standards for the temperature range — [Nature](https://www.nature.com/articles/s41598-020-73341-4) (search-snippet)
- SCA Standard 310-2021 tests at 55 g coffee per 1.000 kg water; states strength target 1.15-1.55% at that ratio (conflicts with 1.15-1.35% Golden Cup range) — [SCA Standard 310-2021](https://sca.coffee/s/SCA_Standard_310-2021.pdf) (search-snippet; PDF returned 404 on my direct fetch)
- +/-10% ratio tolerance (49.5-60.5 g/L) appears only in a question bank — [open-exam-prep](https://open-exam-prep.com/study-guides/sca-q-grader/brewing-science-water-chemistry/brewing-control-chart) (low-quality, unconfirmed)
- Filter-coffee-machine grind 300-900 um — [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/)
```csv
method,dose_g_per_L,water_g,ratio,temp_c_min,temp_c_max,time_s_min,time_s_max,tds_pct_min,tds_pct_max,ey_pct_min,ey_pct_max,source_url
batch_brew_sca_golden_cup,55,1000,1:18.2,92,96,,,1.15,1.35,18,22,https://www.nature.com/articles/s41598-020-73341-4
batch_brew_sca_310_strength,55,1000,1:18.2,92,96,,,1.15,1.55,,,https://sca.coffee/s/SCA_Standard_310-2021.pdf
```
(time_s is blank: the brief's 4-8 min was NOT found in any source; see Gaps.)

#### Cold brew
- Concentrate ratios 1:4 to 1:6 (high TDS, dilute to serve); Puroast gives 1:4 concentrate diluted 1:1, and 1:8 as standard ready-to-drink; another source puts RTD at 1:12-1:15 — [Puroast cold brew ratio guide](https://puroast.com/blogs/low-acid-coffee/cold-brew-ratio-the-complete-guide-to-getting-it-right), [My Coffee Explorer](https://mycoffeeexplorer.com/reference/cold-brew-ratios) (search-snippet)
- Concentrate fridge shelf life estimates: 7-10 days, up to 14 days, 2-3 weeks (sealed); diluted cold brew 3-5 days — [Complete Home Barista](https://completehomebarista.com/guides/cold-brew-shelf-life/), [Colipse](https://colipsecoffee.com/blogs/coffee/cold-brew-shelf-life) (search-snippet; sources conflict, blog-grade)
- Toddy: unopened 4-6 months, opened 7-14 days refrigerated (brand table, secondary) — [Podfoods listing / search results](https://podfoods.co/single-origin-cold-brew-concentrate-slingshot-coffee-company-p3548.html) (search-snippet, weak)
- Grind: cold brew 800-1400 um; cold drip 820-1270 um — [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/)
- Cold brew profiles from Third Wave Water use Mg sulfate + sodium bicarbonate + potassium bicarbonate (no calcium) — [Third Wave Water support](https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575)

#### Siphon / vacuum pot (low-confidence, blog-grade)
- Ratio guides range ~1:10 to 1:15 (one 1:14; one forum 1:17); water ~93 C (200 F) or 85-95 C; total 3 min (~2 min steep + 1 min drawdown) to 4-5 min; grind medium-fine to medium-coarse (sources disagree) — [HomeGrounds](https://www.homegrounds.co/how-to-use-a-siphon-coffee-maker/), [Texas Coffee School](https://texascoffeeschool.com/the-texas-coffee-school-guide-to-brewing-coffee-with-a-vacuum-siphon-pot-also-known-as-a-vacpot/), [Perfect Daily Grind](https://perfectdailygrind.com/2023/01/what-is-syphon-brewing/) (search-snippet)
- Siphon grind 375-800 um — [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/)

#### Cupping
- SCA cupping grind guidance: "slightly coarser than typically used for paper filter drip brewing" (quoted from sca.coffee by) — [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/); micron range given there: 460-850 (a later line says 470-850) — same URL

### Inferences
- 55 g/kg = 1000/55 = ratio 1:18.2 (my arithmetic). Hoffmann AeroPress 11:200 = 1:18.2 (arithmetic).
- Hoffmann French press 30:500 = 1:16.7; 30:450 = 1:15 (arithmetic).
- No TDS/EY values were found for any AeroPress, French press, moka, siphon or cold brew recipe in this pass. Do not populate tds_pct/ey_pct for those rows from this file; leave null or compute from refractometer data.
- Brief-supplied ranges that I could not source (keep flagged "unverified" in the dataset): Chemex 1:15-1:17 thick filter 4-5 min; French press 1:15-1:17 4 min plus settle (partly echoed by secondary sources above); cupping 8.25 g/150 ml, 93 C, 3 min steep, 4 min break (a model-memory recollection in a search response agreed on 8.25 g/150 ml/93 C and 70-75% passing a #20 sieve, but no fetched source confirms; do not cite).

### Gaps
- Chemex, Kalita Wave, Melitta, Clever Dripper, flat-bottom drippers: no sourced dose/ratio/temp/time found (not researched beyond the one broad search; no manufacturer manuals read).
- Moka pot: no verified Hoffmann dose, grind, or total time; no stovetop heat guidance numbers.
- Cezve/Turkish and Vietnamese phin: search returned no ratio/temp/time figures.
- SCA Golden Cup brew time (4-8 min): no source found. SCA Gold Cup 310-2021 full text not read.
- Cold brew TDS %, Toddy and Kyoto drip brew-time figures: none found (only blog ratios/shelf life, which conflict).
- Cupping protocol numbers: SCA protocol PDF not retrieved.
- Hoffmann French press video date (2016 per one source vs 2018 per brief) unresolved.
- Hoffmann AeroPress video not watched; timings come from third-party sites.
- TDS and EY for every method above: not found.

---

## 2. Grind-size reference by method (microns) and grinder click settings

### Takeaway
No standard micron chart exists; the only chart I could fetch (Honest Coffee Guide) states its ranges come from "original guides and popular recipes" without a primary source, and its ranges are wider than the brief's. Barista Hustle's chart (402) and Coffee ad Astra / Gagne micron figures could not be retrieved. Grinder click settings vary widely between sources (MK3 vs MK4, Red Clix, zero-point), so use them only as starting points.

### Cited Findings
```csv
method,grind_um_min,grind_um_max,source_url,note
turkish,40,220,https://honestcoffeeguide.com/coffee-grind-size-chart/,
espresso,180,380,https://honestcoffeeguide.com/coffee-grind-size-chart/,one search source text says 200-300 but its own table says 600-800 (internally inconsistent)
filter_machine_batch,300,900,https://honestcoffeeguide.com/coffee-grind-size-chart/,
aeropress,320,960,https://honestcoffeeguide.com/coffee-grind-size-chart/,widest range on that chart
moka_pot,360,660,https://honestcoffeeguide.com/coffee-grind-size-chart/,Bialetti: medium-fine
siphon,375,800,https://honestcoffeeguide.com/coffee-grind-size-chart/,
v60,400,700,https://honestcoffeeguide.com/coffee-grind-size-chart/,
pour_over_general,410,930,https://honestcoffeeguide.com/coffee-grind-size-chart/,
steep_and_release,450,825,https://honestcoffeeguide.com/coffee-grind-size-chart/,
cupping,460,850,https://honestcoffeeguide.com/coffee-grind-size-chart/,"later line on same page says 470-850; SCA: slightly coarser than paper-filter drip"
french_press,690,1300,https://honestcoffeeguide.com/coffee-grind-size-chart/,other estimates 800-1100 and 1000-1200 (search-snippet)
cold_brew,800,1400,https://honestcoffeeguide.com/coffee-grind-size-chart/,other estimates 1200-1600 and 1000-1500 (search-snippet)
cold_drip,820,1270,https://honestcoffeeguide.com/coffee-grind-size-chart/,
turkish_alt,100,200,search-snippet (unnamed guide),,
```
- Other quoted ranges (search-snippet, secondary guides): Turkish 100-200 um; espresso 180-380; pour-over 410-930; cold brew 800-1400 / 1200-1600 / 1000-1500; French press 690-1300 / 800-1100 / 1000-1200 — [Beanbox](https://beanbox.com/blog/grind-size-cheat-sheet), [Honest Coffee Guide](https://honestcoffeeguide.com/guides/coffee-grind-size-chart/), [Verena Street](https://www.verenastreet.com/blogs/all-about-coffee/coffee-grind-size-chart), [The Coffee Locator](https://thecoffeelocator.com/guide/coffee-grind-size-chart/). The search summary states "there is no single published micron standard."
- WAC champions published micron-linked figures: George Stanica 2024 Comandante C40 Mk4 at 58 clicks = 870 um; Jamika 2024 MK4 900 um; Nemo Pop 2025 sifted at 200 um (Trailmaster x25, 31 clicks) — [WAC recipes](https://worldaeropresschampionship.com/pages/recipes)

#### Click settings (search-snippet from guide sites; sources disagree)
```csv
grinder,method,clicks_min,clicks_max,source_url,note
Comandante C40,french_press,26,40,https://baristalife.co/blogs/blog/comandante-c40-grind-settings-chart,another guide says 28-34
Comandante C40 Red Clix,french_press,51,80,https://honestcoffeeguide.com/comandante-c40-mk4-with-red-clix-grind-settings,Red Clix scale is different
Comandante C40,aeropress,12,35,https://completehomebarista.com/guides/comandante-c40-grind-settings/,typical standard recipe 16-20 or 18-24
Comandante C40,v60_kalita,18,28,https://completehomebarista.com/guides/comandante-c40-grind-settings/,typical starting point 22-28
Timemore C2,french_press,20,30,https://baristalife.co/blogs/blog/timemore-c2-grind-settings-chart,most cluster 20-24
Timemore C2,aeropress,10,30,https://completehomebarista.com/guides/timemore-c2-grind-settings/,one guide 10-14; another 11-30
Timemore C2,v60,13,22,https://completehomebarista.com/guides/timemore-c2-grind-settings/,another guide 14-18
```
- WAC-linked click anchors: C40 24, 27, 30, 32 clicks (2022-2025 AeroPress); ZP6 65 clicks (2023) — [WAC recipes](https://worldaeropresschampionship.com/pages/recipes)
- Honest Coffee Guide has per-grinder pages (not read for values) for Comandante, 1Zpresso JX/JX-Pro/K-series, Timemore C2/C3, Baratza Encore/Virtuoso: e.g. [1zpresso-jx-pro](https://honestcoffeeguide.com/1zpresso-jx-pro-grind-settings/), [1zpresso-k-pro](https://honestcoffeeguide.com/1zpresso-k-pro-grind-settings/), [timemore-c3](https://honestcoffeeguide.com/timemore-c3-grind-settings/), [baratza-encore](https://honestcoffeeguide.com/baratza-encore-grind-settings/), [baratza-virtuoso](https://honestcoffeeguide.com/baratza-virtuoso-grind-settings/)

### Inferences
- Honest Coffee Guide ranges are broader than the brief's ranges and overlap heavily between methods (e.g., AeroPress 320-960 spans moka to V60). For a dataset, store both a "typical" and "wide" range and flag as non-standard. The brief's targets (Turkish ~100-250, espresso ~200-300, moka ~300-400, AeroPress ~400-800, V60 ~600-900, Chemex ~800-1000, French press ~900-1300, cold brew ~1000-1400) were NOT confirmed by any fetched source; the V60 range in particular (brief 600-900 vs sourced 400-700) conflicts.
- Click anchors only transfer within the same grinder/burr version; store grinder_model + firmware/axle version.

### Gaps
- Barista Hustle grind chart (HTTP 402), Coffee ad Astra micron data, Weber, Option-O, Baratza and Comandante official charts, and Gagne "The Physics of Filter Coffee" micron tables: not retrieved.
- 1Zpresso JX/K-series, Timemore C3, Baratza Encore/Virtuoso click numbers: pages located but values not read.
- Chemex and Kalita micron ranges: no sourced figure.

---

## 3. Brewing water chemistry

### Takeaway
SCA target: TDS ~150 mg/L (75-250), calcium hardness ~68 mg/L as CaCO3 (17-85), alkalinity ~40 mg/L, pH 7.0 (6.5-7.5), Na ~10 mg/L, chlorine 0. Barista Hustle's Rao-like recipe is GH 80 / KH 40 (GH:KH 2:1). Third Wave Water Classic targets ~150 mg/L TDS with ~40 mg/L alkalinity. Hendon/Colonna-Dashwood found magnesium extracts more efficiently than calcium and bicarbonate hurts extraction.

### Cited Findings
```csv
standard,tds_mgl_target,tds_mgl_min,tds_mgl_max,calcium_hardness_mgl_caco3_target,calcium_hardness_min,calcium_hardness_max,alkalinity_mgl_caco3_target,ph_target,ph_min,ph_max,sodium_mgl,chlorine_mgl,source_url
SCA_water_standard,150,75,250,68,17,85,40,7.0,6.5,7.5,10,0,https://field-guides.vercel.app/pour-over/the-sca-water-standard.html
```
- SCA profile as above; that page gives no document title/date, so it is a secondary restatement — [field-guides](https://field-guides.vercel.app/pour-over/the-sca-water-standard.html)
- SCAA sheet revised 21 Nov 2009: calcium hardness 4 grains = 68 mg/L, total alkalinity 40 mg/L, pH 7.0 (6.5-7.5), sodium 10 mg/L; no TDS or chlorine listed; range 17-85 mg/L. TDS 150 (75-250) comes from a study guide — [SCAA water standards PDF](https://cdn.shopify.com/s/files/1/0561/9102/5336/files/water-standards.pdf), [open-exam-prep](https://open-exam-prep.com/study-guides/sca-q-grader/brewing-science-water-chemistry/sca-water-standards) (search-snippet)
- I could not confirm whether the 2018 SCA Water Quality Handbook changes these numbers — [Brewing Gadgets listing](https://www.brewinggadgets.in/product/the-2018-sca-water-quality-handbook/)
- Conflicting hardness band from another guide: 75-150 ppm TDS, 50-80 mg/L CaCO3 hardness — [Coffee Tower](https://coffeetower.pages.dev/coffee/water-chemistry) (search-snippet)
- SCA Handbook (as quoted by Daily Coffee News): alkalinity below 40 ppm (as CaCO3) may be too little buffer to prevent corrosion at boiling; upper range 75 ppm alkalinity for harder water — [Daily Coffee News, Kornman 2018](https://dailycoffeenews.com/2018/08/29/a-practical-water-guide-for-coffee-professionals-part-ii-the-sensory-data)
- Water for Coffee (via same article): ~80 ppm bicarbonate (HCO3-), stated as roughly 130 ppm alkalinity as CaCO3, "could suit harder water"; author's best results at 1 part alkalinity : 2-3 parts hardness (as CaCO3); baking soda 0.1 g/L distilled water ~50 ppm alkalinity, 0.2 g/L ~100 ppm — [Daily Coffee News](https://dailycoffeenews.com/2018/08/29/a-practical-water-guide-for-coffee-professionals-part-ii-the-sensory-data)
- Water for Coffee ranges (secondary table; verify against the book): Ca2+ 10-50 mg/L, Mg2+ 5-30 mg/L, carbonate hardness 40-70 ppm as CaCO3 — [Coffee Circle](https://coffeecircle.com/en/e/coffee-water) (search-snippet)
- Water for Coffee Ch. 6 recipes express Ca/Mg/HCO3 as mg/L of the ion, not as CaCO3 (unit-mixing risk) — [Home-Barista thread](https://www.home-barista.com/water/water-for-coffee-book-discussion-t36639-60.html) (forum, search-snippet)
- Hendon, Colonna-Dashwood & Colonna-Dashwood, J. Agric. Food Chem. 2014, DOI 10.1021/jf501687c: high bicarbonate is bad; high Mg2+ increases extraction; Mg avoids limescale vs Ca — [phys.org summary](https://m.phys.org/news/2014-06-science-coffee.html) (search-snippet)
- Royal Coffee blind tasting could not confirm the Hendon/Colonna-Dashwood claim that higher-GH water raises TDS — [Home-Barista thread](https://www.home-barista.com/water/royal-coffee-blind-tasting-waters-t54215-20.html) (search-snippet)
- Barista Hustle concentrate system: 1 g of concentrate per litre = 1 ppm GH (Mg concentrate) or KH (bicarbonate concentrate). Rao-like recipe: 50.1 g buffer + 75.7 g Mg concentrate + 874.2 g DI water (per 1 kg) = GH 80, KH 40. "Recipe 6 - Hendon Water": 30.8 g buffer, 99.9 g hardness, 869.3 g DI (GH/KH not stated in snippet). Barista Hustle says its recipe is close to Scott Rao's — [Barista Hustle DIY water recipes redux](https://www.baristahustle.com/blog/diy-water-recipes-red) (search-snippet; page returned 402)
- Conflicts on "Rao" recipe: Lotus preset GH 72 / KH 20; Complete Home Barista lists Rao as 2.4 g and 1.8 g per 4 L (~100 ppm) — [Complete Home Barista](https://completehomebarista.com/guides/best-water-recipe-espresso/) (search-snippet)
- Anhydrous MgSO4 is not Epsom salt (heptahydrate); ~2x Epsom mass needed for the same MgSO4 (George Howell recipe forum post) — [Home-Barista](https://www.home-barista.com/water/howell-and-brew-water-t50372.html) (forum, search-snippet)
- Third Wave Water official profiles (mg/L per mineral withheld by the company):
```csv
profile,minerals,tds_mgl,alkalinity_mgl_caco3,source_url
Classic Light Roast,"MgSO4, calcium citrate, NaCl",150,40,https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575
Medium Roast,"MgSO4, calcium citrate, KHCO3",150,80,https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575
Dark Roast,"MgSO4, calcium citrate, NaHCO3",180,135-140,https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575
Espresso Machine,"MgSO4, calcium citrate, KHCO3",150,80,https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575
Cold Brew,"MgSO4, NaHCO3, KHCO3",,,https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575
Low Acid,"MgSO4, NaHCO3, KHCO3",,,https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575
```
- Older forum quote of Classic: ~95 mg/L Mg (as magnesium sulfate), ~45 mg/L Ca (as calcium citrate), ~10 mg/L Na, ~0 alkalinity, pH ~6.6; per sachet ~1100 mg MgSO4, 300 mg calcium citrate, 100 mg NaCl. A commenter computes 95 mg/L MgSO4 = 19.2 mg/L Mg2+. Formulation may have changed since (official page now says ~40 mg/L alkalinity) — [Home-Barista TWW thread](https://www.home-barista.com/water/third-wave-water-t44736-70.html) (forum, search-snippet). A Belgian FAQ giving different figures is self-contradictory; ignore — [expertcafe](https://expertcafe-be.pages.dev/en/faq/s8/third-wave-water-recipe/)
- Flavor effects, from Daily Coffee News panel tasting (Kornman 2018): high bicarbonate lowered perceived acidity and added CO2 that impeded extraction and enlarged bloom; high-alkalinity water tasted flat, chalky, muddled; alkalinity-only water lacked sweetness but did best with dark roasts; calcium consistently favored and accented acidity; magnesium sweet/floral in light roasts but heavy/cloying in dark; distilled water scored highest overall in round 2; hard water had lowest acidity and highest viscosity — [Daily Coffee News](https://dailycoffeenews.com/2018/08/29/a-practical-water-guide-for-coffee-professionals-part-ii-the-sensory-data)
- Water for Coffee GH:KH 2:1 target ratio (secondary) — [Barista Hustle snippet via search](https://www.baristahustle.com/blog/diy-water-recipes-red)

### Inferences
- Unit check (my arithmetic): alkalinity as CaCO3 = HCO3- mg/L x 50/61 = x0.82. So 80 mg/L HCO3- = ~66 mg/L as CaCO3, not the ~130 the article states (130 as CaCO3 would be ~159 mg/L HCO3-). Treat the article's "80 ppm bicarbonate = 130 as CaCO3" as internally inconsistent; the ion-vs-CaCO3 basis must be stored in the dataset (add unit_basis field).
- Baking soda conversion (my arithmetic): NaHCO3 84.0 g/mol, 1 meq per mmol, so 0.1 g/L = ~59.5 mg/L alkalinity as CaCO3 (article says ~50; 0.2 g/L = ~119 vs article ~100). Use 0.595 mg/L alkalinity per mg/L NaHCO3 for calculators; the article's figures are rounded.
- SCA 68 mg/L "calcium hardness" and Barista Hustle GH 80 are both as CaCO3 hardness; GH 80 / KH 40 sits just above the SCA 68 / 40 target and fits the 2:1 GH:KH rule.
- SCA mid-spec water (~150 TDS, KH 40) and Third Wave Classic (150 TDS, ~40 alk) agree; Mg-heavy profiles (TWW, Hendon) are consistent with Hendon's Mg-extracts-more finding.
- DIY mg/L recipes for MgSO4 / NaHCO3 / CaCl2: no authoritative per-litre numbers were retrieved. Stoichiometry for a calculator can be derived (e.g., MgSO4 anhydrous 120.4 g/mol -> 1 mg/L Mg2+ per 4.95 mg/L MgSO4; CaCl2 anhydrous 111.0 g/mol -> 1 mg/L Ca2+ per 2.77 mg/L CaCl2), but these are my arithmetic, not sourced recipes.

### Gaps
- Per-litre DIY recipes (mg/L of MgSO4, NaHCO3, CaCl2) from Barista Hustle, Hendon, Rao, Hoffmann: not retrieved (Barista Hustle fetch 402; no Rao/Hoffmann primary found).
- SCA 2018 Water Quality Handbook text; whether it revised the 2009 values.
- Scott Rao's own published recipe; James Hoffmann's water recipe (Hoffmann's Lotus/Perfect Daily Grind etc. not located).
- Sodium 10 mg/L and chlorine 0 are only in secondary SCA restatements.
- "Low alkalinity = sharp/sour" claim: only implied (alkalinity-only water lacks sweetness; below 40 ppm corrosion risk); no direct sourced sensory statement found.
- Water for Coffee book chapter values not read.

---

## 4. Strength and extraction concepts

### Takeaway
SCA Brewing Control Chart ideal zone: 1.15-1.35% TDS and 18-22% extraction. Flat vs conical burr claims: fines amount differs, but Scott Rao (citing Gagne) argues the "flat = clarity, conical = body" consensus is too simplistic. Most formulas and conventions (EY formula, golden ratio, refractometer practice) had no fetched source.

### Cited Findings
- Ideal zone 1.15-1.35% TDS, 18-22% PE ("extraction yield") on the SCA Brewing Control Chart; the 18-22% figure is extraction yield not TDS (a Moccamaster page wrongly calls it TDS) — [Nature Sci. Reports](https://www.nature.com/articles/s41598-020-73341-4), [Moccamaster](https://us.moccamaster.com/blogs/blog/certified-by-the-sca-moccamaster-and-the-golden-cup-standard) (search-snippet)
- SCA 310-2021 test ratio 55 g/kg — [SCA 310-2021](https://sca.coffee/s/SCA_Standard_310-2021.pdf) (search-snippet)
- Burrs: flat burrs typically produce fewer fines than conicals; professionals often recommend flat for clarity, conical for body; Rao argues low-fines flat burrs beat high-fines flat burrs for filter and the simple rule is too simplistic (citing Gagne) — [Scott Rao, "The happy medium amount of fines"](https://www.scottrao.com/blog/happymediumfines)
- Grind distribution is bimodal (boulders and fines <100 um); finer settings raise the proportion of fines while fines' size stays roughly constant (research paper summarized in search) — [Barista Magazine book review of Gagne](https://www.baristamagazine.com/book-review-the-physics-of-filter-coffee-by-jonathan-gagne/) and [search result set](https://www.home-barista.com/grinders/interesting-grinder-particle-size-analysis-t93053.html) (search-snippet; claim-to-URL mapping approximate)
- Coffee Review analyzed four grinders by laser diffraction using the mode particle size — [Coffee Review](https://www.coffeereview.com/minding-the-grinds-our-approach-to-sampling-and-judging-grind-consistency/)
- Gagne's book covers water, grinding (PSD, brittle vs ductile) and percolation — [Barista Magazine review](https://www.baristamagazine.com/book-review-the-physics-of-filter-coffee-by-jonathan-gagne/)

### Inferences
- Standard definition (not sourced here): extraction yield % = (TDS% x brewed-coffee mass g) / dose g. SCA ratio 55 g/L at 1.15-1.35% TDS yields roughly EY = TDS x 18.2 x (brewed mass / water mass); a 1.35% TDS at ~0.9 beverage-to-water mass gives ~22%. This is my arithmetic from the standard formula, to be validated.
- Ratio: 55 g/L = 1:18.2, slightly weaker than the "golden ratio" 1:15-1:18 in the brief; the brief's golden-ratio claim is unsourced.

### Gaps
- EY formula, refractometer protocol (VST/Atago, filtering, temperature), and "golden ratio" conventions: no fetched source.
- EK43 specifics (Coffee ad Astra, Gagne numbers on fines %): not retrieved.
- Primary SCA Brewing Control Chart / Handbook document not read.
