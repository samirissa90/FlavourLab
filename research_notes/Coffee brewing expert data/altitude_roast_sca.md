# Altitude, Processing, Roast, Freshness, SCA Flavor Wheel, SCA Cupping Scores, Coffee Chemistry (dataset-ready notes for the FlavorLab coffee brewing expert tool)

Research date: 2026-11-19. Conventions used in this file:
- Field names follow the requested schema: roast_level, agtron_min, agtron_max, drop_temp_c, weight_loss_pct, flavor_notes, wheel_tier1, wheel_tier2, wheel_tier3, process, effect_acidity, effect_body, effect_sweetness, cupping_attribute, score_min, score_max, source_url.
- Every number in "Cited Findings" has a source link. Anything from my own background knowledge (no fetched source) is placed under "Inferences" and labelled `[UNVERIFIED-BG]`. Do not load `[UNVERIFIED-BG]` rows into the dataset without a confidence flag.
- Source quality tags: [P] = primary or peer-reviewed or official SCA/WCR; [S] = secondary (reference site, trade press); [B] = roaster or retailer blog (low confidence).
- Several pages could not be fully read (HTTP 403/404, bot walls). Where only a search-result summary was available, it is noted as "(search summary only)".

---

## 1. Altitude vs quality (bean density, acidity, sweetness, cup score, ripening), lapse rate, altitude grade names, key studies

### Takeaway
Peer-reviewed work consistently links higher elevation to better sensory scores, higher bean density and higher acidity, with moderators (variety, shade, rainfall, processing). Effect sizes are small to moderate and often reported only as correlations or significance, not as points per 100 m. Altitude grade names (SHB, SHG, HG, HB and similar) are national, non-harmonised conventions, and sources conflict on cutoffs (especially Guatemala).

### Cited Findings

#### Peer-reviewed studies
- Avelino et al. 2005, J Sci Food Agric, "Effects of slope exposure, altitude and yield on coffee quality in two altitude terroirs of Costa Rica, Orosi and Santa Maria de Dota": Orosi 1020-1250 m, Santa Maria de Dota 1550 to about 1780 m. Orosi coffees showed a floral flavour that depended on slope exposure; Santa Maria de Dota coffees showed chocolate flavour that was stronger at higher altitude; taster preference rose with altitude in both terroirs; chemical markers (caffeine, trigonelline, chlorogenic acids) correlated only weakly with sensory traits. [P] — [Zendy record (DOI 10.1002/jsfa.2188)](https://zendy.io/title/10.1002/jsfa.2188) (search summary only; full text not read). Note: this paper is about slope exposure/altitude/yield, not shade; the shade-vs-altitude statement in the brief is not confirmed for Avelino 2005. A Colombian shade study states shade effects on cup quality are unclear at higher (cooler) altitudes and cites Avelino 2005 — [Sweet Maria's library PDF](https://library.sweetmarias.com/wp-content/uploads/2020/08/The-influence-of-shade-trees-on-coffee-quality-in-small-holder-coffee-agroforestry-systems-in-Southern-Colombia.pdf).
- Bertrand et al. 2006, Tree Physiology 26:1239-1248: Arabica hybrids with Sudanese-Ethiopian ancestry vs traditional cultivars at 700-1600 m in El Salvador, Costa Rica, Honduras; ten professional cup-tasters; bean composition (caffeine, chlorogenic acid, trigonelline, fat, sucrose) estimated by NIR calibration. In traditional cultivars chlorogenic acid and fat increased with elevation; hybrids showed homeostasis (bean chemistry less affected by elevation). [P] — [CIRAD record](https://publications.cirad.fr/une_notice.php?dk=532349), [FAO AGRIS record](https://agris.fao.org/search/fr/records/64745bb796fdec8b71b71879) (search summary only).
- Alpizar and Bertrand (2005, separate paper): caffeine, chlorogenic acid and fat increased with elevation while trigonelline and sucrose decreased; a summary notes Caturra at high altitude (wet process, Costa Rica) has high caffeine and fat and low trigonelline. [P] — [FAO AGRIS record](https://agris.fao.org/search/fr/records/64745bb796fdec8b71b71879) (search summary only). Flagged by the search agent as not part of Bertrand 2006.
- Decazy et al. 2003, J Food Sci 68(7):2356-2361: 52 Arabica plots in 6 Honduran regions; multiple factor analysis; high altitude and annual rainfall under 1,500 mm favoured sensory quality; Olancho and El Paraiso gave the highest-quality coffees; a CIRAD summary also lists plot altitude, rainfall, soil acidity, shade percentage, yield and bean size as quality-linked. [P] — [CIRAD agritrop 515149](https://agritrop.cirad.fr/515149), [CIRAD notice 485965](https://publications.cirad.fr/une_notice.php?dk=485965).
- Ethiopia, bean density: bean density was higher for highland than lowland and midland coffees in a south-western Ethiopia green-bean physical-quality study. [P] — [PMC8991259](https://pmc.ncbi.nlm.nih.gov/articles/PMC8991259) (search summary only).
- Ethiopia, 20 agro-ecological zones (Jimma University team, 2024): strong correlations between altitude and several bean traits; higher elevation enhanced acidity and flavour complexity; annual rainfall showed no significant correlation with bean weight, pH, moisture or biochemical composition. [S] — [EurekAlert 2025-08-14](https://www.eurekalert.org/news-releases/1094830) (press summary; correlation coefficients not retrieved).
- Ethiopia, Tolessa et al. (J Sci Food Agric), altitude x shade x harvest period: high altitude with open or medium shade and early-to-mid harvest gave superior bean quality, but authors state the quality-score changes are small. [P] — [Sweet Maria's library PDF](https://library.sweetmarias.com/wp-content/uploads/2020/08/Influence-of-growing-altitude-shade-and-harvest-period-on-quality-and-biochemical-composition-of-Ethiopian-specialty-coffee.pdf) (search summary only).
- Ethiopia, Kafa Biosphere Reserve (Tassew et al., Heliyon 2021 per a thesis abstract): elevation gradient significant (P<0.05) on screen-14+ retention and most cup variables; high-elevation dry-processed coffees scored raw quality 38.5-40% and cup quality 48.0-51.75% (as reported, scale as in the Ethiopian grading system). [S] — [Jimma University repository](https://repository.ju.edu.et/handle/123456789/10081?show=full).
- Worku, De Meulenaer, Duchateau 2017, "Effect of altitude on biochemical composition and quality of green Arabica beans can be affected by shade and postharvest processing method": title and authors confirmed only; abstract and effect sizes NOT retrieved. [S] — [reference-list citation found via search](https://www.alphagalileo.org/en-gb/Item-Display/ItemId/262052). See Gaps.
- Ethiopian early-released varieties study (2015): cup quality value and overall quality significantly and positively correlated with acidity. [P] — [Sweet Maria's library PDF](https://library.sweetmarias.com/wp-content/uploads/2020/08/Quality-Performance-of-Some-Early-Released-Coffee-Varieties-at-Three-Locations-in-South-West-Ethiopia.pdf) (search summary only).

#### Climate change and altitude suitability
- Ovalle-Rivera, Laderach, Bunn, Obersteiner, Schroth 2015, PLoS ONE 10(4):e0124155, "Projected shifts in Coffea arabica suitability among major global producing regions due to climate change": 21 GCMs, 2050s; suitability falls at lower altitudes in Mesoamerica; higher elevations near the equator in South America may gain; high latitudes lose; Ethiopia and Kenya projected more suitable, India and Vietnam less. Bunn is co-author, not lead. [P] — [IIASA PURE record](https://pure.iiasa.ac.at/11352) (full PDF blocked by bot wall; search summary only).
- Press figures for required upslope shift: 300-500 m depending on location (one report) vs 300 m higher on average by 2050 (GCR); the two conflict and neither was verified against the paper. [S] — [Table Debates](https://www.tabledebates.org/node/10876), [GCR Magazine](https://www.gcrmag.com/new-study-paints-grim-correlation-between-climate-change-and-coffee).
- Bunn et al. 2015 "A bitter cup" (Climatic Change; Arabica and Robusta): only author list and abstract opening seen; findings not confirmed. [S] — [search result listing](https://pure.iiasa.ac.at/11352).

#### Altitude grade names and cutoffs (dataset table: country, grade, elevation_masl_min, elevation_masl_max)
Source for the table below: Cafe Imports "Common Grades for Green Coffee by Country" chart, one-page PDF, text extracted locally. [S, importer trade chart] — [Cafe Imports chart](https://dev-cdn.cafeimports.com/images/Common-Coffee-Grades-Chart.pdf). Units are not printed in the extracted text; metres inferred from magnitudes.

| country | grade | elevation_masl_min | elevation_masl_max | note |
|---|---|---|---|---|
| Costa Rica | SHG/SHB | 1200 | | chart prints "1200" |
| Costa Rica | GHB | 1000 | 1200 | |
| Costa Rica | MHB | | <1000 | |
| El Salvador | SHG | 1200 | | |
| El Salvador | HG | 900 | 1200 | |
| El Salvador | CS (Central Standard) | 500 | 900 | |
| Honduras | SHG | 1200 | | |
| Honduras | HG | 900 | 1200 | |
| Honduras | CS | 500 | 900 | |
| Nicaragua | SHG | 1200 | | |
| Nicaragua | HG | 900 | 1200 | |
| Nicaragua | CS | 500 | 900 | |
| Guatemala | SHB | 1600 | 1700 | CONFLICT, see below |
| Guatemala | FHB | 1500 | 1600 | CONFLICT |
| Guatemala | HB | 1350 | 1500 | CONFLICT |
| Peru | SHB | 1350 | | |
| Peru | HB | 1200 | | chart prints "1200-1200" (typo) |

Non-altitude grades on the same chart (screen size or defect based, not altitude): Colombia Supremo screen 17, Excelso screen 15; Kenya AA 17-18, AB 15-16, PB peaberry; Tanzania AA 18, AB 15-17; Burundi AA 18, AB 16, C 14; Brazil Santos NY 2/3 screen 17-18; Ethiopia washed Gr 1 0-3 defects, Gr 2 4-12, Gr 3 13-25; Yemen AA 15, A 14; Rwanda Super Specialty 5 defects per 350 g (score 90-100), Specialty 80-90, Grade 1 70-79; Mexico "Strictly High" and Extra Prima/Prima are defined by screen 14-15+ and defect counts, not an altitude figure on the chart. — [Cafe Imports chart](https://dev-cdn.cafeimports.com/images/Common-Coffee-Grades-Chart.pdf).

- Guatemala conflict: secondary sources put SHB at above about 1,350 m or 4,500 ft (about 1,370 m), HB at about 1,200-1,350/1,400 m, Semi Hard Bean about 1,050-1,200 m; no official ANACAFE table was retrieved; the chart's 1600-1700 m SHB band looks like an outlier. [B/S] — [search results incl. coffeedesk, coffeeresearch.org, Barista Hustle](https://www.coffeeresearch.org/coffee/guatemala2.htm), [Barista Hustle](https://www.baristahustle.com/?p=342302). One site gave Honduran SHG as above about 1,200 m, another about 1,300 m (citing IHCAFE), a third 1,500 m; and a comparison table gave Mexico SHB-equivalent above 1,700 m (unsourced). Treat as origin-specific, not universal.
- SHB and SHG are regional naming variants of the same altitude logic (SHB mainly Guatemala and Costa Rica; SHG Honduras, El Salvador, Mexico); "Altura" is not explained by any retrieved source. [B] — [Green Coffee Collective glossary SHG](https://greencoffeecollective.com/pages/glossary/strictly-high-grown-shg), [SHB glossary](https://greencoffeecollective.com/pages/glossary/strictly-hard-bean-shb).

### Inferences
- Suggested JSON rule: `altitude_quality = {density: +, acidity: +, sweetness: weak +, cup_score: +, chlorogenic_acid: +, fat: +, trigonelline: -, sucrose: -(Alpizar & Bertrand)}`; magnitude per 100 m is not available from retrieved sources, so store as direction-only with confidence "medium".
- The Cafe Imports chart is the only tabular country-by-country source retrieved; use it as default with a `confidence: low` flag for Guatemala and keep the 4,500 ft (about 1,370 m) value as an alternative row.
- `[UNVERIFIED-BG]` Temperature lapse rate: about 0.6 C per 100 m is the commonly quoted environmental lapse rate (standard atmosphere about 6.5 C/km); consequence: slower cherry development at altitude, with ripening commonly cited as roughly 8-9 months at 1,800+ m vs 6-7 months at low elevation; no retrieved source gave these figures.
- `[UNVERIFIED-BG]` Cooler nights and slower ripening are the usual mechanistic explanation for denser beans and higher acidity at altitude; the retrieved studies show the correlation, not the mechanism.

### Gaps
- Effect sizes (points of cup score or percent density per 100 m, correlation r) for Avelino 2005, Bertrand 2006, Decazy 2003 and Worku 2017: only qualitative summaries retrieved; full texts paywalled or blocked.
- Temperature lapse rate (0.6 C/100 m) and cherry ripening time vs altitude: no source retrieved.
- Bean density numeric (g/L or g/cm3) by altitude: not retrieved.
- Official ANACAFE, IHCAFE, ICAFE, Procafe, FNC altitude tables; Mexico and Peru official cutoffs.
- Exact altitude shift in Ovalle-Rivera 2015 (paper PDF blocked).

---

## 2. Processing methods (steps, duration, drying, moisture, cup effect, defect risk, decaf)

### Takeaway
Retrieved sources agree qualitatively: washed = clean, crisp, higher perceived acidity and lower body; natural = fruity, sweet, heavy body, higher fermentation risk; honey = in between, scaling with mucilage left; anaerobic = a fermentation technique with sealed tanks that produces heavier, savoury or funky profiles. Quantitative drying times and the 10-12% moisture target were NOT found in citable sources (blogs only). Decaf: Swiss Water and CO2 claim 99.9% caffeine removal; US labelling threshold 97%.

### Cited Findings
- Washed: clean and crisp, clarity, low-to-medium body; removing fruit sugars/mucilage lets brightness come through. [B] — [Origin Coffee](https://origincoffee.co.uk/blogs/journal/whats-coffee-processing), [Wanderlust](https://wanderlust.coffee/coffee-processing-methods/).
- Natural: bright, intense, sweet, heavy body; lower acidity than washed; berry-like notes. [B] — [Wanderlust](https://wanderlust.coffee/coffee-processing-methods/), [Baristalife](https://baristalife.co/blogs/blog/coffee-processing-methods-explained).
- Honey (pulped natural): intermediate profile; white honey = minimal mucilage, clean light cup; yellow = more mucilage, sweeter; faster drying with frequent turning = lighter honey profile, slower drying = darker; too much retained moisture risks fermentation defects. [B] — [Wanderlust](https://wanderlust.coffee/coffee-processing-methods/), [Baristalife](https://baristalife.co/blogs/blog/coffee-processing-methods-explained).
- Anaerobic: fermentation in sealed tanks with little or no oxygen; one source gives a 48-200 h window (not tied to a specific lot or method); cups described as earthy, heavier, lower acidity, savoury or herbal, though another source says anaerobic fermentation tones down the "funky" notes of naturals; sources disagree on whether it is a method or a technique applicable to washed/natural/honey. [B] — [Elephant Cinnamon (Squarespace blog)](https://elephant-cinnamon-fxst.squarespace.com/mega-blog/coffee-processing-washed-honey-natural-amp-anaerobic), [Coffee Geek](https://coffeegeek.com/blog/farming/the-impact-of-processing-on-coffees-character/).
- SCA Extrinsic Assessment form (beta) lists process type checkboxes "Washed / Natural / Other" and fields for wet mill/station and dry mill. [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).
- SCA Physical Assessment lists a moisture field and a size meter "calibrated to ISO 6673" plus a colour checklist (Blue Green, Bluish-Green, Green, Greenish, Yellow-Green, Pale Yellow, Yellowish, Brownish) — the moisture target value itself is not printed. [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).
- Decaf, Swiss Water: water-only; certified/claimed 99.9% caffeine removed. [B/S] — [Seattle Coffee Gear](https://www.seattlecoffeegear.com/blogs/learning-center/how-coffee-is-decaffeinated), [The Takeout](https://thetakeout.com/how-do-you-remove-caffeine-from-coffee-1798252806).
- Decaf, CO2: supercritical CO2 circulated through moistened beans, caffeine dropped out on pressure release, gas recycled; typically 99.9%. [B/S] — [Seattle Coffee Gear](https://www.seattlecoffeegear.com/blogs/learning-center/how-coffee-is-decaffeinated).
- Decaf, regulatory: US "decaffeinated" label requires at least 97% caffeine removal; a retailer page says solvent methods remove only 96-97% (marketing claim). [B] — [Colipse Coffee](https://colipsecoffee.com/blogs/coffee/how-is-decaf-coffee-made), [Lifeboost](https://lifeboostcoffee.com/blogs/lifeboost/decaffeination-conundrum-which-method-removes-caffeine-while-preserving-health-and-flavor).
- Decaf, ethyl acetate ("sugarcane"/"natural"): ethyl acetate occurs naturally in fruit but the commercial supply is mostly synthetic; most, but not all, of the ethyl acetate used is synthetic. Methylene chloride safety is contested (FDA deemed both solvents acceptable per one source; ozone and activist concerns per another). [B/S] — [Coffee Review decaf article](https://www.coffeereview.com/fun-without-the-buzz-decaffeination-processes-and-issues/), [Reviewed](https://reviewed.com/cooking/features/how-is-decaf-coffee-made).

### Inferences
Dataset-ready rows below combine the cited qualitative effects with `[UNVERIFIED-BG]` numeric values (steps, durations). Load the numeric columns with `confidence=low`.

| process | steps (summary) | fermentation_hours | drying_days_typical | moisture_target_pct | effect_acidity | effect_body | effect_sweetness | funk_risk | defect_risks | confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| washed | pulp, ferment 12-48 h [UNVERIFIED-BG], wash, dry | 12-48 | 7-15 | 10-12 | high (cited, qualitative) | low-medium (cited) | medium | low | over-fermentation (sour/phenolic), uneven drying | low |
| natural | dry whole cherry on patios/beds, hull | n/a | 15-30+ | 10-12 | lower (cited) | heavy (cited) | high (cited) | high | mold, ferment/boozy, inconsistency | low |
| honey_white | pulp, ~10% mucilage left [UNVERIFIED-BG], dry | n/a | 7-12 | 10-12 | high-medium | low-medium | medium | low | mold if humid | low |
| honey_yellow | ~50% mucilage [UNVERIFIED-BG] | n/a | 10-18 | 10-12 | medium | medium | medium-high | medium | mold, ferment | low |
| honey_red_black | 80-100% mucilage, slow shaded drying [UNVERIFIED-BG] | n/a | 15-30 | 10-12 | low-medium | medium-heavy | high | medium-high | mold, ferment, high labour | low |
| pulped_natural_brazil | pulp, dry with mucilage (equivalent to honey) | n/a | 10-20 | 10-12 | medium | medium | medium-high | medium | as honey | low |
| wet_hulled (Giling Basah) | hulled at about 30-50% moisture [UNVERIFIED-BG], then dried | n/a | 2-5 [UNVERIFIED-BG] | 10-12 | low | heavy | low-medium | high (earthy, herbal) | quick mold, uneven colour (blue-green) | low |
| anaerobic | sealed tank, 48-200 h (cited, unspecified) | 48-200 | per base method | 10-12 | variable, often lower (cited) | heavier (cited) | high | high | over-ferment, vinegar/alcohol, inconsistency | low |
| carbonic_maceration | whole cherries in CO2-flushed tank [UNVERIFIED-BG] | 24-120 [UNVERIFIED-BG] | per base method | 10-12 | variable | medium-heavy | high | high | as anaerobic | low |
| thermal_shock | hot-then-cold water bath during ferment [UNVERIFIED-BG] | per base | per base | 10-12 | higher/brighter claims | medium | high | medium | unproven claims | very low |
| lactic/yeast co-ferment | inoculated starter cultures [UNVERIFIED-BG] | 48-120 | per base | 10-12 | variable | medium-heavy | high | high | inoculant dependence | very low |

Decaf rows: swiss_water 99.9% (cited), co2 99.9% (cited), ethyl_acetate (mostly synthetic per cited), methylene_chloride (contested), US label threshold 97% (cited). Decaf cup effect (muted aroma, lower body) is `[UNVERIFIED-BG]`.

### Gaps
- Drying duration in days and the 10-12% moisture target: not found in a citable source (SCA forms show a moisture field but no target). 10-12% is from the brief and common knowledge, not retrieved.
- Fermentation hours for washed, carbonic maceration, thermal shock, lactic/yeast co-ferments: no sources retrieved.
- Peer-reviewed process-vs-cup studies (for example effect sizes of natural vs washed on acidity score): none retrieved.
- Wet-hulled, thermal shock, and honey colour mucilage percentages: no source retrieved.

---

## 3. Roast levels (Agtron, drop temp, DTR, weight loss, roast time, chemistry, roast names)

### Takeaway
Agtron cutoffs differ by authority: Coffee Review classifies Light >70, Medium-Light 61-70, Medium 51-60, Medium-Dark 41-50, Dark 35-40, Very Dark 25-34, Extreme-Dark <25 on the whole-bean gourmet scale. Rao's DTR guidance is 20-25% (15% acceptable when burner capacity is high relative to batch size). Bean temps at drop of 196-205 C (light), 210-220 C (medium) and 225-230 C (dark) are repeated by blogs. Weight-loss numbers are poorly sourced.

### Cited Findings
Roast classification table (Coffee Review, M-Basic gourmet scale, whole bean) [P/S] — [Coffee Review](https://www.coffeereview.com/?p=22177):

| roast_level | agtron_min | agtron_max | flavor_notes (as in source) |
|---|---|---|---|
| Light | 71 | 100 (open top) | light brown to cinnamon colour |
| Medium-Light | 61 | 70 | moderately light brown |
| Medium | 51 | 60 | medium brown |
| Medium-Dark | 41 | 50 | rich brown; droplets of oil may appear |
| Dark | 35 | 40 | deep brownish/black; spots of oil to shiny surface |
| Very Dark | 25 | 34 | black surface covered brightly with oil |
| Extreme-Dark | 0 | 24 | black, shiny |

- Second crack begins at roughly 47 on the whole-bean Agtron scale; first crack = earliest point coffee can be ground and consumed. [P/S] — [Coffee Review](https://www.coffeereview.com/?p=22177).
- Alternative classification cited as "SCA Roast Color Classification": light above 60, medium 45-60, medium-dark 35-45, dark below 35; another table puts light at 71-80 and "Italian" at 0-30; scale range 25 (very dark) to 95 (very light) on the SCA/Agtron gourmet scale. [B] — [Coffee Review pages](https://coffeereview.com/?p=23581), [Green Plantation](https://www.greenplantation.com/a/coffee-roasting-grades-what-are-the-differences-in-coffee-roasting) (search summary only; conflicts with the Coffee Review table above).
- Drop (bean) temperatures: light 196-205 C, medium 210-220 C, dark 225-230 C; Beanbox says values vary by 10-30 F depending on probe and method. [B] — [Beanbox](https://beanbox.com/blog/light-medium-dark-roast-levels).
- Light roast = stopped near first crack; dark = into or past second crack. [B] — [Beanbox](https://beanbox.com/blog/light-medium-dark-roast-levels).
- Development time ratio (DTR) = time from first-crack onset to drop as share of total roast time. Rao: 20-25% for most roast levels between end of first crack and start of second crack; lower target such as 15% can suit a high burner-to-batch ratio; based on over 20,000 roasts tasted, 18 of the best 20 were in 20-25% DTR; example curves 22% and 21% DTR; typical charge >60% of drum capacity. [P (practitioner)] — [Scott Rao DTR article](https://www.scottrao.com/blog/2016/8/25/development-time-ratio), [Daily Coffee News](https://dailycoffeenews.com/2014/08/12/roast-development-time-and-the-prerequisite-for-any-successful-roast).
- Rao has had good roasts below 20% DTR but none above 25%; he does not assume the ratio holds well before end of first crack or well after second-crack onset. [P (practitioner)] — [Home-Barista, Rao on DTR](https://www.home-barista.com/roasting/rao-on-development-time-ratio-t42962.html).
- Mass and structure changes: for dark roast, about 20% of dry matter is lost and bean volume rises up to 80%; density falls from about 1.3 (green) to about 0.7 (dark roast) (the paper prints "kg/m3"; this is a unit typo for g/cm3 or kg/L); porosity about 0.5 for dark roast. [P] — [Smrke et al. 2018, J Agric Food Chem 66:5293](https://digitalcollection.zhaw.ch/bitstream/11475/12175/2/2017_Smrke-etal_Roasted-coffe-degassing-time-resolved-gravimetry.pdf).
- Colorette points used in Smrke et al.: dark 78 +/-1, medium 101 +/-2, light 131 +/-1 (Probatino 1 kg batch, El Salvador Arabica); roasting time in the 100 g sample roaster approximately 7-8 min at medium speed. [P] — [Smrke et al. 2018](https://digitalcollection.zhaw.ch/bitstream/11475/12175/2/2017_Smrke-etal_Roasted-coffe-degassing-time-resolved-gravimetry.pdf).
- Moisture/weight loss claim: 15-16% for light and 19-22% for dark (unsourced single site; moisture loss not total). [B, low] — [Coffee Tower pages](https://coffeetower.pages.dev/coffee/roast-levels) (flagged unreliable by the search agent).
- Roast chemistry: green coffee chlorogenic acids about 4-12% of dry weight; dark roasting destroys most (losses above 80-90%, partly converted to lactones); peak roasting temperature drives CGA loss more than time alone; trigonelline falls rapidly with roasting, forming pyridines and nicotinic acid, and is absent in Italian roast in one study; caffeine is largely roast-stable. [P] — [Food & Function review (Farah/Ferruzzi-type), PubMed 24671262](https://pubmed.ncbi.nlm.nih.gov/24671262/), [Food Chem 2021 accepted manuscript](https://pubblicazioni.unicam.it/bitstream/11581/446686/8/Peer-reviewed%20accepted%20manuscript%20of%20Food%20Chemistry%20Volume%20343%202021%20art.%20128514.pdf), [Springer Eur Food Res Technol](https://link.springer.com/content/pdf/10.1007/s00217-014-2356-z.pdf) (all from search summaries; exact percent per roast level not retrieved).
- A Vietnamese robusta study reported caffeine peaking at 240 C then declining (likely mass-loss concentration effect; source does not say). [S] — [Walailak J (tis.wu.ac.th)](https://tis.wu.ac.th/index.php/tis/article/download/13444/2207/58793).
- Roast level affects key odorants: a 2024 Molecules study (Obando and Figueroa) identified 74 compounds, 25 aroma-active; the darkest roast (RL25) was marked by burnt, putrid and sulfurous notes. [P] — [Molecules 2024 via DOAJ](https://doaj.org/article/3851983d1e0b47ceb6dffa04801dc8a0).

### Inferences
- `[UNVERIFIED-BG]` Roast-name mapping (loose, vendor-dependent): Cinnamon ~ very light, pre-/at first crack start (Agtron ~85-100, drop ~190-196 C); New England/Light ~ end first crack onset; City ~ end of first crack (Agtron ~65-75, 205-210 C); Full City ~ approach to second crack (Agtron ~45-55, 220-225 C); Vienna ~ second crack onset/rolling (Agtron ~35-45, 225-235 C); French ~ heavy second crack (Agtron ~25-35, 235-245 C); Italian ~ beyond (Agtron <25); Nordic/Omni = light roasts tailored for filter/espresso (Agtron ~75-95). Not sourced; the user's brief ranges (Light 75-95; Medium 55-75; Dark second crack 225-240 C) match this mapping, not Coffee Review's table, so store both rule sets with a `scale` field (SCA_gourmet vs CoffeeReview_Mbasic).
- `[UNVERIFIED-BG]` Typical total weight loss 12-14% light, 14-16% medium, 16-20% dark; typical roast time 8-14 min; Maillard from ~150 C, first crack ~196 C, second ~224 C; acrylamide peaks at light-medium roast then declines; phenylindanes form with darker roast and contribute bitterness. None verified here.
- Flavor outcomes (acidity falls, body and bitterness rise with roast degree) are consistent with the retrieved CGA/trigonelline loss data, but no retrieved source gave direct sensory scores by roast level.

### Gaps
- Weight loss % by roast level from a primary source (only a low-quality moisture-loss claim found).
- Drop temperatures from a primary source (blog only); whether probe is bean, drum, or air.
- Roast-name to Agtron/temperature mapping (Cinnamon, City, Full City, Vienna, French, Italian, Nordic, Omni) from a citable source.
- Phenylindane, lactone, acrylamide quantities by roast level.
- Roast time targets by roast level.

---

## 4. Freshness: degassing, best-by windows, storage, green coffee shelf life

### Takeaway
The best-sourced numbers are from the Zurich University of Applied Sciences (Smrke/Yeretzian): about 1% CO2 by weight is released from whole beans over roughly a month, while ground coffee degasses in minutes to about two months. The SCA treats whole bean as "fresh" for about three weeks and ground coffee for about one hour. Espresso and filter rest windows are only available from roaster blogs and conflict.

### Cited Findings
- SCA: whole-bean coffee "can reasonably be considered fresh within about three weeks of roasting"; ground coffee fresh for about one hour after grinding; CO2 loss is rapid for the first 20 days then slows; CO2 that whole beans lose over weeks is lost in minutes once ground; after CO2 leaves, oxygen enters, causing off-flavours and eventually rancidity; fresh coffee gives more espresso crema and stronger filter bloom. [P] — [SCA Coffee Decoded: fresh coffee](https://sca.coffee/sca-news/coffee-decoded-9-fresh-coffee).
- Smrke et al. 2018: reported CO2 release for whole roasted beans in the literature: 0.7-4.3 mg/g (time not reported; Shimoni), 9-10 mg/g in 60 days (Geiger), 6.5-14 mg/g in 30 days (IR method), up to 16 mg/g total trapped CO2 after roasting (Wang); degassing studied up to 75 days (Baggenstoss); gas released on grinding composed of 87% CO2, 7.3% CO, 5.3% N2, under 1% VOCs (Clarke and McRae); release rates in the first hours up to 40 mg/h for 12 g freshly roasted and ground coffee and up to 2 mg/h for 15 g freshly roasted whole beans; samples roasted to three degrees (Colorette 78/101/131) and three roasting speeds; Weibull model fit. [P] — [Smrke et al. 2018 PDF](https://digitalcollection.zhaw.ch/bitstream/11475/12175/2/2017_Smrke-etal_Roasted-coffe-degassing-time-resolved-gravimetry.pdf).
- Smrke et al. 2022 (storage after opening): degassing from whole beans lasts about a month; roasting produces roughly 1% CO2 by weight; ground coffee loses gas over minutes to about two months; screw-cap packaging was the best-performing storage method; clips, tape re-closure and decanting into containers lost freshness faster. [P] — [Smrke et al. 2022 PDF](https://digitalcollection.zhaw.ch/bitstream/11475/26687/3/2022_Smrke-etal_Effects-of-different-coffee-storage-methods-on-coffee-freshness_FPSL.pdf) (search summary only), [ZHAW record](https://digitalcollection.zhaw.ch/handle/11475/12175).
- Aroma staling: key aroma 2-furfurylthiol becomes less active during storage (lost on staling). [P] — [Nottingham repository](https://nottingham-repository.worktribe.com/OutputFile/4482616) (search summary only).
- Espresso/filter rest times from roaster blogs (conflicting, low confidence): at least 5-7 days with 7-11 ideal for espresso; 7-10 days for espresso; light roasts 10-21 days and medium 7-14 days; darker roasts degas faster (3-7 days) while lighter need 5-10 days; very fresh beans (1-4 days) gassy, channel-prone, fast shots. [B] — [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/coffee-degassing-how-long-to-rest-filter-coffee-and-espresso), [General Warfield's](https://generalwarfieldscoffee.com/blogs/our-blog/coffee-7-10-days-after-roasting), [Clive Coffee](https://clivecoffee.com/blogs/learn/is-your-coffee-too-fresh), [Methodical Coffee](https://methodicalcoffee.com/blogs/coffee-culture/freshly-roasted-coffee-explained-degassing-rest-and-flavor), [Partners Coffee](https://help.partnerscoffee.com/en-US/coffee-resting-and-degassing-6433419) (snippets not individually mapped to each number).
- Claim that a 25 C rise accelerates freshness loss by a factor of 100 (attributed to Smrke and Yeretzian, SCA Expo 2019): NOT verified. [B, unverified] — [LinkedIn repost](https://co.linkedin.com/in/saraovalle); lecture page: [SCA podcast 81](https://sca.coffee/sca-news/podcast/81/the-science-of-coffee-freshness-samo-smrke-expo-lectures-2019).

### Inferences
- Rule set: `ground_staleness_window_min = 60` (SCA); `whole_bean_fresh_days = 21` (SCA); `degas_complete_days ~ 30` (Smrke); `espresso_rest_days_min = 5-7` (blogs); store with a roast-level modifier (darker faster degassing) at low confidence.
- `[UNVERIFIED-BG]` Freezing: airtight portions, freeze before opening, thaw sealed to avoid condensation; commonly quoted that freezing largely halts staling, but no staleness percent figures retrieved. Green coffee shelf life 6-12 months at about 10-12% moisture and water activity about 0.5-0.65 [UNVERIFIED-BG] (numbers not retrieved). Espresso 5-21 days and filter 4-28 days windows in the brief are consistent with blog ranges but are not from a primary source.

### Gaps
- Percent staleness for freezing vs room storage; sensory shelf-life studies with numbers.
- Green coffee shelf life, water activity targets and moisture limits (no sources retrieved).
- One-way valve efficacy data.
- Per-roast-level CO2 release amounts from the Smrke 2018 results section (PDF text extracted only for the introduction and methods portions).

---

## 5. SCA Flavor Wheel (2016, with WCR Sensory Lexicon): hierarchy, reference standards, aroma-chemistry mapping

### Takeaway
The 2016 wheel has 9 tier-1 families, 27 tier-2 subcategories and 83 tier-3 descriptors in the one transcription retrieved (a secondary study-guide site); the official SCA CVA form uses a simplified CATA subset of the same families. The WCR Lexicon 2.0 defines 110 attributes with reference standards. Compound-to-descriptor mappings are best sourced from a 2025 GC-O study (furaneol, 4-vinylguaiacol, linalool, pyrazines) plus classic Grosch data (2-furfurylthiol).

### Cited Findings

#### Full hierarchy (wheel_tier1 / wheel_tier2 / wheel_tier3)
Source: transcription by a study-guide site (secondary; not the official SCA graphic; tier mapping only explicit for Fruity, Sour/Fermented and Other) [S] — [Open Exam Prep, 2016 SCA/WCR wheel architecture](https://open-exam-prep.com/study-guides/sca-q-grader/flavor-wheel-sensory-lexicon/flavor-wheel-architecture).

| wheel_tier1 | wheel_tier2 | wheel_tier3 |
|---|---|---|
| Floral | Floral; Black Tea | Chamomile; Rose; Jasmine; Black Tea |
| Fruity | Berry | Blackberry; Raspberry; Blueberry; Strawberry |
| Fruity | Dried Fruit | Raisin; Prune |
| Fruity | Other Fruit | Coconut; Cherry; Pomegranate; Pineapple; Grape; Apple; Peach; Pear |
| Fruity | Citrus Fruit | Grapefruit; Orange; Lemon; Lime |
| Sour/Fermented | Sour | Sour Aromatics; Acetic Acid; Butyric Acid; Isovaleric Acid; Citric Acid; Malic Acid |
| Sour/Fermented | Alcohol/Fermented | Winey; Whiskey; Fermented; Overripe |
| Green/Vegetative | Olive Oil; Raw; Green/Vegetative; Beany | Olive Oil; Raw; Under-ripe; Peapod; Fresh; Dark Green; Vegetative; Hay-like; Herb-like; Beany |
| Other | Papery/Musty | Stale; Cardboard; Papery; Woody; Moldy/Damp; Musty/Dusty; Musty/Earthy; Animalic |
| Other | Chemical | Bitter; Salty; Medicinal; Petroleum; Skunky; Rubber |
| Roasted | Pipe Tobacco; Tobacco; Burnt; Cereal | Pipe Tobacco; Tobacco; Pungent; Ashy; Smoky; Brown/Roast; Grain; Malt |
| Spices | Pungent; Pepper; Brown Spice | Pungent; Black Pepper; Nutmeg; Cinnamon; Clove; Anise |
| Nutty/Cocoa | Nutty; Cocoa | Peanuts; Hazelnut; Almond; Chocolate; Dark Chocolate |
| Sweet | Brown Sugar; Vanilla; Overall Sweet; Sweet Aromatics | Molasses; Maple Syrup; Caramelized; Honey; Vanilla; Vanillin; Overall Sweet; Sweet Aromatics |

Source counts: tier-1 9; tier-2 27; tier-3 83 (per-family tier-2/tier-3: Floral 2/4, Fruity 4/18, Sour/Fermented 2/10, Green/Vegetative 4/10, Other 2/14, Roasted 4/8, Spices 3/6, Nutty/Cocoa 2/5, Sweet 4/8). Some names repeat at two tiers or in two families (Pungent in Roasted and Spices; Vanilla, Overall Sweet, Sweet Aromatics, Black Tea as both tier-2 and tier-3). — same source. A glossary elsewhere cites 85 descriptors and a Beanpoet article cites 99 attributes in a sorting task; unreconciled. [B] — [Coffee-e4d glossary](https://coffee-e4d.pages.dev/learn/advanced/sca-flavor-wheel), [Beanpoet](https://www.beanpoet.com/?p=6941).

#### Official CVA CATA subset (primary, printed on the SCA Descriptive/Affective forms)
Tier-1/tier-2 as printed: Floral; Fruity (Berry, Dried Fruit, Citrus Fruit); Sour/Fermented (Sour, Fermented); Green/Vegetative; Other (Chemical, Musty/Earthy, Woody); Roasted (Cereal, Burnt, Tobacco); Nutty/Cocoa (Nutty, Cocoa); Spice; Sweet (Vanilla/Vanillin, Brown Sugar). Mouthfeel CATA: Rough (Gritty, Chalky, Sandy); Oily; Smooth (Velvety, Silky, Syrupy); Mouth-Drying; Metallic. Main Tastes (choose 2): Salty, Sour, Sweet, Bitter, Umami. [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).

#### WCR Sensory Lexicon and reference standards
- Lexicon identifies 110 flavour, aroma and texture attributes; Lexicon 2.0 published October 2017; developed at the Sensory Analysis Center, Kansas State University; basis for the revised Coffee Taster's Flavor Wheel (first redesign in 20 years). [P] — [WCR Sensory Lexicon page](https://worldcoffeeresearch.org/work/sensory-lexic), [WCR news: Lexicon 2.0](https://worldcoffeeresearch.org/news/2017/announcing-the-coffee-lexicon-2-0).
- Lexicon 2.0 added globally available references (FlavoursActiV GMP pharmaceutical-grade capsules, co-developed with Coffee Enterprises and Square Mile) for 24 attributes: Sour, Bitter, Salty, Apple, Grape, Coconut, Pineapple, Acetic acid, Butyric acid, Isovaleric acid, Fermented, Peapod, Fresh, Papery, Musty/Earthy, Musty/Dusty, Moldy/Damp, Phenolic, Petroleum, Brown Spice, Almond, Vanillin, Floral, Jasmine. First-edition examples were grocery items such as Lorna Doone cookies and Green Giant cut green beans. [P/S] — [Tea & Coffee Trade Journal, 2017-10-27](https://www.teaandcoffee.net/news/18692/wcrs-sensory-lexicon-2-0-includes-new-global-flavour-standards-coffee/), [WCR Sensory Lexicon page](https://worldcoffeeresearch.org/work/sensory-lexic).
- Blueberry reference: canned blueberries from an Oregon brand (per trade press). [S] — [Daily Coffee News 2015](https://dailycoffeenews.com/2015/05/21/is-this-your-standard-for-blueberry-in-sensory-evaluation-of-coffee).
- Reference-standard table (study-guide transcription of the 2016 edition; intensities on the Lexicon 15-point scale) [S] — [Open Exam Prep, WCR lexicon standards](https://open-exam-prep.com/study-guides/sca-q-grader/flavor-wheel-sensory-lexicon/wcr-sensory-lexicon-standards):

| attribute | reference | amount | intensity | modality |
|---|---|---|---|---|
| Sweet | sucrose solution | 1.0% | 1.0 | taste |
| Sour | citric acid | 0.015% / 0.05% | 1.5 / 3.5 | taste |
| Bitter | caffeine | 0.01 / 0.02 / 0.035 / 0.05% | 2.0 / 3.5 / 5.0 / 6.5 | taste |
| Salty | NaCl | 0.15% | 1.5 | taste |
| Blackberry | Smucker's blackberry jam | n/s | 5.5 | flavor |
| Peach | fresh peach pit | n/s | 8.0 | aroma |
| Peach | Jell-O peach powder | n/s | 7.0 | flavor |
| Grape | Welch's 100% Concord grape juice | 1:1 with water | 5.0 | flavor |
| Lemon | lemon juice | 1:4 with water | 5.0 aroma / 7.0 flavor | both |
| Black tea | Lipton black tea | n/s | 8.0 aroma / 7.0 flavor | both |
| Peapod | Le Nez du Cafe no. 3 "garden peas" | 1 drop | 7.0 | aroma |
| Cardboard | cardboard, 2 inch square | steeped in half cup | 7.5 | aroma |
| Papery | coffee filters, soaked overnight in boiling water | n/s | 2.5 | flavor |
| Phenolic | phenylacetic acid | 0.15 g | 6.0 | aroma |
| Mouth-drying | alum | 0.05% / 0.07% | 2.5 / 3.5 | mouthfeel |
| Thickness | sucrose / tomato juice | 5% / n/s | 2.0 / 4.0 | mouthfeel |
| Metallic | KCl | 0.10% | 1.5 | mouthfeel |
| Oily | 1% milk / half-and-half | | 3.0 / 6.0 | mouthfeel |
| Hazelnut | imitation hazelnut extract | 1/8 tsp in cup of milk | 3.5 (double strength 6.0) | flavor |

#### Aroma-chemistry mapping (from GC-O with FD factor and OAV; Foods 2025, 14, 3192, four commercial coffees)
[P] — [PMC12469716](https://pmc.ncbi.nlm.nih.gov/articles/PMC12469716/). Odor_descriptor (FD factor range; OAV range across the four samples):
- Furaneol: caramel, marshmallow (FD 2187 all; OAV 175-250) -> wheel Sweet / Brown Sugar / Caramelized.
- 4-Vinyl-2-methoxyphenol (4-vinylguaiacol): smoky (FD 243-2187; OAV 340-761) -> Roasted / Burnt / Smoky.
- 4-Ethyl-2-methoxyphenol: smoky (FD 1-729; OAV 12-79).
- Guaiacol: woody (FD 2187; OAV 8-63) -> Other / Papery-Musty / Woody (or Burnt/Smoky).
- Furfural: nutty, almond (FD 2187; OAV 15-62).
- Linalool: floral, citrus, rose (FD 3-81; OAV 72-222 where detected) -> Floral / Floral and Fruity / Citrus.
- Isovaleric acid: sour, pungent (FD 243-729; OAV 72-200) -> Sour/Fermented / Isovaleric Acid.
- 3-Hydroxy-2-butanone (acetoin): buttery (FD 9; OAV 94-137); 2,3-butanediol: butter (FD 243; one sample); 2,3-pentanedione: buttery/creamy (text mention only). 2,3-butanedione was NOT in this paper's tables.
- Pyrazines: 2-ethyl-5-methylpyrazine (coffee; FD 3-81; OAV 52-76), 2,3,5-trimethylpyrazine (coffee, cocoa; OAV 1-90), 2-ethyl-6-methylpyrazine (roasted, nutty; OAV 45-72), 2-ethyl-3,5-dimethylpyrazine (almond; OAV 170), 2-acetylpyrazine (popcorn; OAV 9-12) -> Nutty/Cocoa and Roasted/Cereal.
- Caramel group: maltol (OAV 8-29), 5-methylfurfural (OAV 23-48), hydroxyacetone (OAV 2-3), gamma-butyrolactone (caramel, roasted nut; OAV 1-3), furfuryl alcohol (bread; OAV 17-31).
- 2-Furfurylthiol: classic Grosch-derived table lists 1.08 mg/L, OAV 1.10x10^5, "roasty (coffee)"; pyrazines are the second most abundant aroma class with the lowest thresholds (with thiazoles); FFT is not in the 2025 paper. [S] — [Coffee Research aroma page](https://coffeeresearch.org/science/aromamain.htm), [Frontiers in Nutrition 2023 review](https://www.frontiersin.org/articles/10.3389/fnut.2023.1196816/full) (search summaries only).

### Inferences
- Mapping table for the FlavorLab aroma-family model (compound -> wheel_tier1): 2-furfurylthiol -> Roasted; linalool -> Floral (also Fruity/Citrus); 4-vinylguaiacol and 4-ethylguaiacol -> Roasted/Burnt/Smoky (also Spices/clove-like `[UNVERIFIED-BG]`); 2,3-butanedione/acetoin/2,3-pentanedione -> Sweet/dairy-buttery (no wheel node; closest "Sweet Aromatics" or "Other"); pyrazines -> Nutty/Cocoa and Roasted; furaneol/maltol -> Sweet/Brown Sugar; isovaleric/acetic/butyric acid -> Sour/Fermented; guaiacol -> Other/Woody or Roasted/Smoky. Mapping is my inference from descriptors, not an SCA-published mapping.
- The two hierarchies (secondary 83-descriptor transcription vs official CVA CATA subset) differ in granularity; use the study-guide table for tier-3 and the SCA form for the CVA-compatible tier-2 labels.
- Jasmine reference exists in Lexicon 2.0 (listed among the 24 new references), but the actual material was not described in sources.

### Gaps
- Official SCA wheel graphic text and official Lexicon PDF (110 attributes) were not retrieved; tier-2/tier-3 table above is from one secondary transcription.
- Reference standards for jasmine and dark chocolate: no source describes them (jasmine confirmed as a Lexicon 2.0 capsule only).
- 2,3-butanedione and 2-furfurylthiol numeric OAVs in coffee from a primary paper (only a Grosch-derived table via search summary).

---

## 6. SCA cupping score scale (2004 protocol) and the Coffee Value Assessment (CVA)

### Takeaway
The CVA (beta April 2023; standards released November 2024) replaces the 2004 single 100-point cupping form with a Descriptive Assessment (CATA plus 0-15 intensity) and an Affective Assessment (9-point hedonic "impression of quality") plus Physical and Extrinsic assessments. The retrieved sources do not give the CVA total-score formula (an online calculator is referenced) or any 80+ threshold within the CVA. The 2004 protocol numbers (10 attributes, score bands) come from the brief and are not verified from a retrieved source.

### Cited Findings
- Timeline: SCA unveiled the CVA beta at Re:co Symposium, Portland, 20 April 2023; November 2024 SCA released three CVA standards (Sample Preparation and Cupping Mechanics, Descriptive Assessment, Affective Assessment); Affective Assessment = SCA Standard 104-2024; the standards supersede the 2004 Cupping Protocol and Form. [P] — [SCA announcement](https://sca.coffee/sca-news/sca-new-cva-cupping-standards-7ga28), [Sprudge](https://sprudge.com/?p=209528), [SCASA synopsis](https://magazine.coffee/blog/22/6964/education-introducing-the-coffee-value-assessment-by-the-sca-a-synopsis-from-scasa).
- Structure: four assessment types: Descriptive, Affective, Physical, Extrinsic (Physical and Extrinsic only briefly defined; at time of Sprudge article in research and development). [P/S] — [SCASA synopsis](https://magazine.coffee/blog/22/6964/education-introducing-the-coffee-value-assessment-by-the-sca-a-synopsis-from-scasa), [Sprudge](https://sprudge.com/?p=209528).
- Descriptive form (SCA Version 2, June 2024): attributes Fragrance, Aroma, Flavor, Aftertaste, Acidity, Mouthfeel, Sweetness; each has an intensity scale printed as LOW / MEDIUM / HIGH with tick marks 0, 5, 10, 15; CATA descriptor boxes (see section 5); Main Tastes choose two of Salty, Sour, Sweet, Bitter, Umami; fields for Purpose and Roast Level. [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).
- Affective form (SCA Version 1/2, June 2024): 9-point scale for Fragrance, Aroma, Flavor, Aftertaste, Acidity, Mouthfeel, Sweetness, Overall, with a FINAL mark per attribute; anchors: 1 Extremely low, 2 Very low, 3 Moderately low, 4 Slightly low, 5 Neither high nor low, 6 Slightly high, 7 Moderately high, 8 Very high, 9 Extremely high ("impression of quality"); 5 cups per sample; "Non-uniform cups" and "Defective cups" checkboxes (5 each); defect check options Moldy, Phenolic, Potato; total score computed via calculator at sca.coffee/cuppingscore. [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).
- Note on attribute lists: one retail blog lists six scored affective attributes (Fragrance and Aroma, Flavor and Aftertaste, Acidity, Sweetness, Mouthfeel, Overall) and calls scoring "essentially the same 100-point system"; the official form shows eight separate scored rows (Fragrance, Aroma, Flavor, Aftertaste, Acidity, Mouthfeel, Sweetness, Overall). Prefer the official form. [B vs P] — [Royal NY](https://www.royalny.com/how-to-use-the-new-sca-cupping-form).
- The CVA moves from 2004 "Body" to "Mouthfeel", adds "Sweetness" to the scored set, separates description from evaluation, and the calculator is designed to prevent "backward scoring" (assigning the total first); cupper records session purpose. [P/S] — [SCASA synopsis](https://magazine.coffee/blog/22/6964/education-introducing-the-coffee-value-assessment-by-the-sca-a-synopsis-from-scasa).
- Q Grader certification using the existing SCA cupping form continues to play a role (CQI letter); a 100-point scale with a firm 80-point line for specialty is referenced as the incumbent practice. [S] — [Sprudge](https://sprudge.com/?p=209528).
- CVA Physical Assessment (Alpha V1, Sept 2023, amended May 2025): 350 g sample; moisture field; size meter calibrated to ISO 6673; Category 1 defects with defect-equivalent ratios: Full Black 1:1, Full Sour 1:1, Dried Cherry 1:1, Fungus Damage 1:1, Foreign Matter 1:1, Severe Insect Damage 5:1; Category 2: Partial Black 3:1, Partial Sour 3:1, Parchment 5:1, Floater 5:1, Immature/Unripe 5:1, Withered 5:1, Shell 5:1, Broken/Chipped/Cut 5:1, Hull/Husk 5:1, Slight Insect Damage 10:1; colour options (Blue Green to Brownish); counts roll up into "Total Green Defects". [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).
- Extrinsic (beta) fields: Farming (country, region, farm/co-op, producer, species, variety, harvest date), Trading (size grade, other grade, ICO number), Processing (processor, wet mill, dry mill, process type washed/natural/other), Certifications (4C, Fair Trade, Organic, Rainforest Alliance). [P] — [SCA CVA Forms May 2025 PDF](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf).
- Rwanda national grade bands (for contrast): Super Specialty 90-100, Specialty 80-90, Grade 1 70-79 with 5 defects per 350 g for the top two. [S] — [Cafe Imports chart](https://dev-cdn.cafeimports.com/images/Common-Coffee-Grades-Chart.pdf).

### Inferences
- Dataset rows (cupping_attribute, score_min, score_max) for CVA affective: Fragrance, Aroma, Flavor, Aftertaste, Acidity, Mouthfeel, Sweetness, Overall each score_min=1, score_max=9 (hedonic) [cited]; CVA descriptive intensity score_min=0, score_max=15 [cited].
- `[UNVERIFIED-BG]` 2004 SCA protocol (legacy, still used by Q graders): 10 attributes (Fragrance/Aroma, Flavor, Aftertaste, Acidity, Body, Balance, Overall = scored 6.00-10.00 in 0.25 steps; Uniformity, Clean Cup, Sweetness = 2 points per cup, max 10 each); total 100; defects deducted (taint 2 points per cup, fault 4 points per cup); bands: 90-100 Outstanding, 85-89.99 Excellent, 80-84.99 Very Good, below 80 not specialty. The score bands and 80+ threshold are given in the brief and I did not verify them in a retrieved source. Primary defect = Category 1 (e.g., full black, full sour); secondary = Category 2, as in the cited Physical form above (the legacy 5-defect-per-350 g specialty limit is `[UNVERIFIED-BG]`).
- CVA affective "Overall" is separate from sum; since the total-score formula is not published in the retrieved sources, do not implement a CVA-to-100 conversion in code until the calculator formula is obtained.

### Gaps
- CVA affective total-score formula and the equivalent of the 80+ threshold (calculator at sca.coffee/cuppingscore; PDF forms contain no formula).
- Official SCA 2004 protocol text (score ranges, defect deduction rules, band names): not retrieved.
- CVA Descriptive/Affective standard PDFs (SCA-103/104-2024) not read directly; SCA news pages for CVA returned 404 for two URLs.

---

## 7. Chemistry basics: caffeine, chlorogenic acids, trigonelline

### Takeaway
Retrieved sources support qualitative direction only: caffeine is roast-stable; chlorogenic acids drop sharply (most lost by dark roast); trigonelline degrades (to pyridines and nicotinic acid) and is nearly absent in very dark roast. Caffeine mg per 8 oz by brew method and bean type was not retrieved.

### Cited Findings
- Chlorogenic acids about 4-12% of green bean dry weight depending on species/treatment; dark roast losses above 80-90%, partly converted to lactones. [P] — [Food & Function review, PubMed 24671262](https://pubmed.ncbi.nlm.nih.gov/24671262/), [Food Chemistry 2021 accepted manuscript](https://pubblicazioni.unicam.it/bitstream/11581/446686/8/Peer-reviewed%20accepted%20manuscript%20of%20Food%20Chemistry%20Volume%20343%202021%20art.%20128514.pdf).
- Peak roast temperature, more than time alone, drives CGA degradation. [P] — [Springer EFRT paper](https://link.springer.com/content/pdf/10.1007/s00217-014-2356-z.pdf) (search summary).
- Trigonelline highest in green coffee, decreases rapidly with roasting, forms volatile pyridines and nicotinic acid; absent in the Italian roast sample in one study. [P] — [Journal of Oleo Science](https://www.jstage.jst.go.jp/article/jos/71/10/71_ess22194/_article), [Food & Function review](https://pubmed.ncbi.nlm.nih.gov/24671262/).
- Caffeine relatively stable during roasting; one robusta study reported a peak at 240 C then decline. [P/S] — [Food & Function review](https://pubmed.ncbi.nlm.nih.gov/24671262/), [Walailak J](https://tis.wu.ac.th/index.php/tis/article/download/13444/2207/58793).
- Altitude: caffeine, CGA and fat rise with elevation; trigonelline and sucrose fall (Alpizar and Bertrand 2005; Bertrand 2006) — see section 1.
- Bitter taste reference: caffeine 0.01-0.05% corresponds to Lexicon bitter intensity 2.0-6.5 — see section 5.

### Inferences
- `[UNVERIFIED-BG]` Typical caffeine in dry green beans: arabica about 1.0-1.5%, robusta about 2.0-2.7%; per 8 oz: drip about 95 mg, espresso about 63 mg per 30 mL shot (about 1 oz), cold brew concentrate higher, decaf about 2-7 mg; robusta blends roughly double arabica per bean. Not sourced here; load with `confidence=low`.
- `[UNVERIFIED-BG]` Typical CGA retention: light roast about 50-70% of green, medium about 30-50%, dark under 10-20%; the cited sources only support "most lost by dark roast".

### Gaps
- Caffeine mg per 8 oz by method (drip, French press, espresso, cold brew, instant) and by arabica vs robusta: no source retrieved.
- Quantitative CGA/trigonelline retention by named roast level.
- Water activity and moisture limits for green coffee (also listed under Freshness).

---

## Appendix: source quality summary and reliability notes
- Highest confidence: SCA CVA forms PDF (official, text extracted locally), Smrke et al. 2018 (peer-reviewed, introduction and methods read), SCA Coffee Decoded freshness page, Foods 2025 aroma study, Coffee Review Agtron table, Rao DTR article, WCR lexicon page.
- Medium: Cafe Imports grade chart (importer chart, internally inconsistent for Guatemala and Peru), Open Exam Prep transcriptions (study-guide site, not official SCA graphics).
- Low/blog: roaster and retailer pages for processing, rest times, decaf claims; the Coffee Tower and similar `.pages.dev` pages were flagged unreliable and are used only where noted.
- Fetch failures: IIASA PLoS ONE PDF (bot wall), CATIE repository (403), Home-Barista wheel thread (403), SCA CVA news pages (404 on two URLs), Smrke 2022 and Avelino/Bertrand/Worku/Decazy full texts (not read); those items rely on search summaries and are marked accordingly.
