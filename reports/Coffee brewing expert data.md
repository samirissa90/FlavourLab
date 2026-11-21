# Recipes sourced well, strength data not

For the FlavorLab barista expert, the notes support a usable core. Six named authors (Hoffmann, Rao, Kasuya, Hedrick, Winton and Perger) supply dose, water, temperature, pour schedule and total time for V60, and the [World Brewers Cup winners from 2016 to 2025](https://en.wikipedia.org/wiki/World_Brewers_Cup) give a competition baseline at **1:13 to 1:17**. Espresso has a clear anchor of **18 g in, 36 g out in 25 to 30 s at about 93 °C and 9 bar**. Origin production comes from the [USDA FAS July 2026 circular](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf). The weakest layer is strength: **no source publishes TDS for any named pour-over recipe**, espresso TDS and EY rest on blog snippets, and the SCA's own strength band differs by document (**1.15 to 1.35% TDS** in the Golden Cup versus **1.15 to 1.55%** in SCA 310, the latter unverified). Altitude cutoffs, harvest months and grade thresholds conflict across importers for most origins, and every origin acidity, body and sweetness score is inferred from tasting words, not sourced. The CVA has replaced the 2004 cupping form, but its total-score formula was not retrieved, so the tool should not convert CVA results to a 100-point score yet. Load each value as its own row with source, label and a conflict group rather than choosing a winner.

**How to read the labels.** [inferred] means the note's author derived the value from cited numbers or descriptors. [unverified] means the value came from a search snippet, an aggregator, a page that could not be opened, or background knowledge with no fetched source. [conflict] means sources disagree and both values are kept. Source-type tags carried from the notes are *primary*, *secondary* (compilations, transcriptions, retailer or study-guide sites), *blog*, *snippet* (search summary only) and *brief* (supplied in the research brief with no source).

## Named V60 recipes converge on 1:15 to 1:17 but publish no TDS

Ratios cluster at **1:15** (Kasuya, Hedrick, Winton) and **1:16.5 to 1:16.7** (Rao, Hoffmann), while the 2025 champion ran **1:14**. Every recipe pairs a bloom of 2x to 3x the dose with 30 to 60 seconds of wait. Temperature is the least consistent field. Hedrick sets it by roast (95 to 96 °C light, 93 to 94 °C medium, 91 to 93 °C dark), Kasuya uses 92 °C, Rao 97 °C, and the 2025 champion moved from about 96 °C for the first 120 g to 80 °C for the final 90 g. Hoffmann's published page says only "the hotter, the better" for temperature.

**Table 1.1. Named and near-named V60 recipes**

| Recipe (author) | Dose / water (g) | Ratio | Temp (°C) | Grind | Bloom (g / s) | Pours (s:cumulative g) | Total time | TDS / EY | Label and source |
|---|---|---|---|---|---|---|---|---|---|
| Ultimate V60, 30 g (Hoffmann) | 30 / 500 | 1:16.7 [inferred] | no number | medium-fine | 60 / 45 | 0:60, 45:300, 75:500 | 3:30 (drawdown done) | not stated | secondary transcription, [Hario USA](https://www.hario-usa.com/blogs/recipes-and-more-from-friends/james-hoffmann-uitimate-v60-technique) |
| Ultimate V60, 18 g variant (Hoffmann, gist) | 18 / 300 | 1:16.7 [inferred] | not stated | medium-fine, Niche Zero 40 to 50 | 45 / up to 45 | 0:45, 1:15 to 180, 1:45 to 300 [unverified] | 3:00 target | not stated | [unverified]: timings differ from the 30 g schedule, [gist](https://gist.github.com/fluency03/7fb305b8110dde5739d14697af97a99a) |
| A Better 1 Cup V60 (Hoffmann, 2022) | 15 / 250 | 1:16.7 [inferred] | 100 (one site) or "freshly boiled" [conflict] | medium-fine [unverified] | 50 / about 45 | 0:50, 45:100, 70:150, 90:200, 110:250 | about 3:00 [conflict] vs about 2:30 (summary) | not stated | secondary transcription, [aeroprecipe](https://aeroprecipe.com/recipes/james-hoffmann-better-1-cup-v60-technique); video not viewed |
| Scott Rao V60 (Hario UK interview, 2022-05-10) | 20 / 330 | 1:16.5 [inferred] | 97 | not stated ("grind fresh") | 60 / 40 | 0:60, 40:200, wait to about 70% drained, then to 330 | 4:00 to 4:30 | EY 22 to 24.5% stated; TDS not stated | primary (ambassador page), [Hario UK](https://www.hario.co.uk/blogs/hario-ambassadors/hario-v60-recipe-interview-with-hario-ambassador-scott-rao) |
| Tetsu Kasuya 4:6 (2016 WBC champion) | 20 / 300 | 1:15 | 92 | coarse | 50 / 45 | 0:50, 45:120, 90:180, 130:240, 160:300 | 3:30 (dripper removed) | not stated | secondary, [Hario Europe](https://hario-europe.com/blogs/hario-community/v60-ambassadors-tetsu-kasuya); pour timings conflict, see Conflicts |
| Lance Hedrick V60 masterclass | 20 / 300 | 1:15 | 95 to 96 light; 93 to 94 medium; 91 to 93 dark | medium-fine, "like granulated sugar" | 40 / 45 | 0:40, 45:120, 75:260, 120:300 | 2:45 to 3:00 (target) | not stated; water 75 to 150 ppm TDS | [unverified]: retailer paraphrase, [LAMOSE](https://secure.lamose.com/blogs/recipes/lance-hedricks-pour-over-masterclass-v60-technique) |
| Matt Winton five-pour (2021 WBC champion) | 20 / 300 | 1:15 | 93 bloom; 88 later pours [unverified] | medium | 60 / not stated | 60 g pours at 60, 120, 180, 240, 300, about 30 s apart | 6:50 [conflict] vs 2:40 competition | not stated | secondary, [Honest Coffee Guide](https://honestcoffeeguide.com/brew-recipes/matt-winton-v60-five-pour/) |
| Matt Perger V60 | not verified (58 g/L column implies about 11.6 g) [unverified] | 200 g water | 207 °F, about 97.2 °C [inferred] | fine | 50 / not stated | 0:50, 30:100, 60:200 | 2:20 | not stated | secondary compilation PDF, [PDF](https://www.ilcaffeespressoitaliano.com/wp-content/uploads/V-60.pdf); original source not found |

Two more sourced series sit beside these. The [Drumming Barista](https://thedrummingbarista.substack.com/p/the-drumming-baristas-top-3-v60-recipes) community recipes (2021 and 2023, medium grind for all) use 20 g / 300 g with 60 to 75 g blooms and totals of 210 to 240 s for the "Lowering the number of coffees" and "60 X 5" recipes, and 15 g / 250 g for the 2021 "First coffee of the day" (bloom 40 g, total 165 to 180 s) and "Sweet and acidic 3-pour" (total 150 to 165 s). Hario's [Hoffmann Switch and Sibarist recipe](https://www.hario-usa.com/blogs/recipes-and-more-from-friends) lists 15 g and 250 ml at 2:30. The Drumming Barista "Full-bodied 5-pour" row is internally inconsistent: its pours sum to 300 g against 250 g of water.

**Table 1.2. World Brewers Cup champions, 2016 to 2025**

| Year | Competitor (country) | Dose / water (g) | Ratio (calc.) | Temp (°C) | Pour pattern | Total time | Label and source |
|---|---|---|---|---|---|---|---|
| 2016 | Tetsu Kasuya (Japan) | 20 / 300 | 1:15 | 92 | 4:6 method | 3:00 (Wikipedia) [conflict] | [Wikipedia](https://en.wikipedia.org/wiki/World_Brewers_Cup) |
| 2017 | Chad Wang (Taiwan) | 15 / 250 | 1:16.7 | 92 | not stated | 2:00 | same |
| 2018 | Emi Fukahori (Switzerland) | 17 / 220 | 1:12.9 | 80 to 95 | hybrid immersion and pour-over | 2:55 | same |
| 2019 | Du Jianing (China) | 16 / 240 | 1:15 | 94 | 60 g, 80 g at 0:18, 100 g at 0:56 | 1:40 | [Roasters Pack](https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes) |
| 2021 | Matt Winton (Switzerland) | 20 / 300 | 1:15 | 93 / 88 | five 60 g pours | 2:40 | [Wikipedia](https://en.wikipedia.org/wiki/World_Brewers_Cup) |
| 2022 | Shih Yuan (Sherry) Hsu (Taiwan) | 14 / 200 | 1:14.3 | 70 first pour, then 95 | 4 x 50 g every 30 s; grind 75% at 1000 µm, 25% at 800 µm | not stated | same |
| 2023 | Carlos Medina (Chile) | 15.5 / 250 | 1:16.1 | 91 | 5 x 50 g every 30 s | not stated (target 2:40) | [Roasters Pack](https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes) |
| 2024 | Martin Wölfl (Austria) | 17 / 270 | 1:15.9 | 93 | 60 ml bloom, 60 ml at 0:40, 50 ml at 1:20, 100 ml at 2:00 | not stated | [WBC table](https://en.wikipedia.org/wiki/World_Brewers_Cup) |
| 2025 | George Jinyang Peng (China) | 15 / 210 | 1:14.0 | 96 (first 120 ml), 80 (final 90 ml) [conflict: 205 °F or 210 °F] | 30 g at 0:00, 90 g at 0:30, 90 g at 1:10 | 1:45 [conflict] vs 2:15 | [Sprudge](https://sprudge.com/how-to-brew-coffee-like-the-2025-world-brewers-cup-champion-338576.html); [Honest Coffee Guide](https://honestcoffeeguide.com/brew-recipes/george-jinyang-peng-2025-wbc/) |
| 2026 | Nas Jaafar (Malaysia) | not found | not found | not found | not found | not found | [Hario Europe](https://www.hario-europe.com/blogs/hario-community/2026-world-brewers-cup-championship) (listing only) |

Ratios in the table are my arithmetic from the stated doses and waters, and they are narrower than the notes' own summary. The notes describe the competition range as "1:12 to 1:16", but the table gives **1:12.9 to 1:16.7** [conflict within notes]. Competition drawdowns run 1:40 to 2:40, against everyday recipes of 2:30 to 4:30 [inferred].

**Table 1.3. Targets for TDS, extraction yield and temperature**

| Target | Value | Source | Label |
|---|---|---|---|
| SCA Golden Cup strength | TDS 1.15 to 1.35%; EY 18 to 22%; 92 to 96 °C | [Nature Sci. Rep.](https://www.nature.com/articles/s41598-020-73341-4); [BUNN](https://resource.bunn.com/assets/web/pdfs/BUNN-CoffeeBasics_Brochure_web.pdf) | snippet, secondary |
| SCA 310-2021 home-brew strength | TDS 1.15 to 1.55% at 55 g/L; 90 to 96 °C | [SCA 310](https://sca.coffee/s/SCA_Standard_310-2021.pdf) (PDF returned 404) | snippet [conflict] with the Golden Cup upper bound |
| Lockhart Brew Control Chart (1957) | "ideal" zone TDS 1.15 to 1.35%, EY 18 to 22%; the 18 to 22% figure is extraction yield, not TDS | [SCA chart article](https://www.sca.coffee/sca-news/25/issue-13/towards-a-new-brewing-chart) (404; search summary); [Freshcup](https://freshcup.com/why-the-new-coffee-brewing-control-chart-is-a-big-deal/) | snippet; a [Moccamaster page](https://us.moccamaster.com/blogs/blog/certified-by-the-sca-moccamaster-and-the-golden-cup-standard) mislabels the 18 to 22% as TDS [conflict] |
| Rao EY | 22 to 24.5% (depends on grinder, varietal and roast) | [Hario UK](https://www.hario.co.uk/blogs/hario-ambassadors/hario-v60-recipe-interview-with-hario-ambassador-scott-rao) | primary-ambassador; sits above the 18 to 22% zone [conflict] |
| V60 brew TDS | none published by any fetched source | none | gap |
| Default recipe envelope | ratio 1:15 to 1:17; 92 to 96 °C light, 91 to 93 °C dark; bloom 2x to 3x for 30 to 45 s; drawdown 2:30 to 3:30 | derived from Table 1.1 and Hedrick's roast table | [inferred] |
| Ratio arithmetic | 55 g/L equals 1:18.2, looser than the 1:15 to 1:17 recipe cluster | arithmetic | [inferred]; the "golden ratio" claim in the brief is unsourced |

Kasuya's 4:6 rule ties acidity to the first 40% of water: **more water in pour one raises acidity, less water raises sweetness**, and the final 60% sets strength within a 1:15 to 1:17 range ([Hario Europe](https://hario-europe.com/blogs/hario-community/v60-ambassadors-tetsu-kasuya); [Long Short London](https://longshortlondon.com/4-6-method-brewers-cup-champ-tetsu-kasuya/)). The Long Short London page adds that each pour starts only after the last has drained, with pours of 50, 70, 60, 60 and 60 g.

**Table 1.4. Pour-over troubleshooting rules**

| Symptom | Diagnosis | Action | Label and source |
|---|---|---|---|
| Sour, sharp, lemony | under-extracted | grind finer, raise temperature, slow the pour, add contact time | [unverified]: aggregator, [field guide](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html) |
| Bitter, harsh, astringent | over-extracted | grind coarser, lower temperature, shorten contact, reduce agitation | same |
| Drawdown fast, sour or thin | grind too coarse or bypass | grind finer, pour in the centre | [Winton](https://honestcoffeeguide.com/brew-recipes/matt-winton-v60-five-pour/); [Hedrick](https://secure.lamose.com/blogs/recipes/lance-hedricks-pour-over-masterclass-v60-technique) (faster than 2:30 means finer) |
| Drawdown slow, bitter or dry | grind too fine or fines clogging | grind coarser, reduce agitation, pre-wet filter | Winton; Hedrick (slower than 3:15 means coarser) |
| Sour and bitter together | channeling | level the bed, pour gently; if finer grind makes it more sour, suspect the bed | [inferred] from search synthesis |
| Huge bloom that overflows | very fresh, gassy coffee | more bloom water, longer bloom | [unverified]: aggregator |
| Little or no bloom | stale coffee | none needed; check roast date | [unverified] |
| Papery or cardboard taste | unrinsed filter | rinse filter | [PDG](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/) |
| Water pulls through too quickly | low agitation | gentle swirl to add agitation | PDG |

One aggregator table reverses the grind direction (bitter means finer). It contradicts every other source in the set and is excluded, as noted in the notes [conflict].

## Espresso baseline is 1:2 in 25 to 30 seconds

The modern baseline has broad agreement. **Normale** runs 18 g to 36 g in 25 to 30 s at 93 °C and 9 bar, with TDS 8 to 12% and EY 18 to 22% from a [search snippet](https://coffeebros.com/blogs/coffee/most-popular-espresso-shot-ratios-or-recipes). Breville uses 20 g to 40 g in 25 to 30 s with a "fine table salt" starting texture ([Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso)). The Italian certified single is **7 g ± 0.5 g in 25 ± 5 s at 88 ± 2 °C at the unit exit, 9 ± 1 bar, 25 ± 2.5 ml** ([Wikipedia](https://en.wikipedia.org/wiki/Espresso)). Light-roast practice moves toward 1:2.5 to 1:3 and longer shots, with time treated as a flow signal rather than a target.

**Table 2.1. Espresso parameters by style**

| Style | Dose (g) | Yield (g) | Ratio | Time (s) | Temp (°C) | Pressure (bar) | TDS / EY | Label and source |
|---|---|---|---|---|---|---|---|---|
| Italian certified single | 7 ± 0.5 | not stated | not stated | 25 ± 5 | 88 ± 2 at unit exit | 9 ± 1 | not stated | secondary, [Wikipedia](https://en.wikipedia.org/wiki/Espresso) |
| Ristretto | 18 to 22 (Breville) | about 18 to 22 | 1:1 (Breville) [conflict] vs 1:1 to 1:1.5 (snippet) | 15 to 20 | not stated | not stated | not stated | snippet, [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/espresso-vs-ristretto-vs-lungo-vs-americano-differences-flavor-and-brewing) |
| Normale (baseline) | 18 | 36 | 1:2 | 25 to 30 | 93 | 9 | TDS 8 to 12%; EY 18 to 22% | snippet, [Coffee Bros](https://coffeebros.com/blogs/coffee/most-popular-espresso-shot-ratios-or-recipes) |
| Lungo | not stated | not stated | 1:3 (Breville) to 1:3 to 1:4 (snippet) | 35 to 45 [conflict] vs 25 to 40 | not stated | not stated | not stated | snippet |
| Modern (Hoffmann method, secondary) | 16 / 18 / 20 | 40 to 48 / 45 to 54 / 50 to 60 | 1:2.5 to 1:3 | 35 to 45 / 35 to 50 / 40 to 55 | not stated | not stated | EY 23 to 24% claimed (traditional 18 to 20%) | secondary, [Complete Home Barista](https://completehomebarista.com/guides/hoffman-method-james-hoffmann-espresso-technique/) |
| Barista Hustle baseline (Rao) | 18 (basket rating) | 36 | 2:1 start; 2.5:1 to 3:1 for experienced | avoid over 35 | not stated | not stated | not stated | secondary, [Scott Rao blog](https://www.scottrao.com/blog/2024/2/26/how-to-approach-brewing-different-coffees) |
| Allonge | 18 | about 90 | 1:5 to 1:6 | about 30 | not stated | not stated | not stated | snippet |
| Light roast on a Flair (Hedrick) | 16 | 45 (shot 3) | 2.8:1, aim about 3:1 | about 60 | not stated (just off the boil) | pre-infusion about 3 bar for 10 to 12 s, then 8 to 9 bar | not stated | secondary, [Flair](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee) |

Temperature norms are broad. Wikipedia gives an 86 to 95 °C brew range, Complete Home Barista sets a default of 93 °C (200 °F) with a 90 to 96 °C adjustment window, and pre-infusion of 3 to 5 s. Roast-level temperatures (light 94 to 96 °C, dark 90 to 92 °C) come only from snippets and are [unverified]. Lever machines run 8 to 10 bar ([Wikipedia](https://en.wikipedia.org/wiki/Espresso_machine)).

**Table 2.2. Dial-in and troubleshooting by shot time (1:2 target, 25 to 30 s)**

| Shot time (s) | Diagnosis | Action | Source |
|---|---|---|---|
| under 20 | under-extracted; sour, thin, salty | grind 1 to 2 settings finer | [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso) |
| 20 to 24 | slightly under-extracted | grind 1 setting finer or raise yield | same |
| 25 to 30 | optimal | keep settings | same |
| 31 to 35 | slightly over-extracted; bitter, dry | grind 1 setting coarser | same |
| over 35 | severely over-extracted; ashy | grind 2 settings coarser | same |
| under 20, bitter and astringent | channeling | check distribution (WDT), grind slightly finer, level tamp | same |
| fast, sour, thin | under-extracted | grind finer or add 1 to 2 g dose | [Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso) |
| slow, over-extracted | over-extracted | grind coarser or reduce dose slightly | Breville |
| about 55 to 60 on light roast | under-extracted | lengthen ratio toward 1:3, coarsen grind, raise early flow | [Flair](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee) |

Other points from the same guides: fresher beans need a finer grind, darker roasts need finer grind, and Hedrick calls time "a flow meter, not a goal" (a [forum quote](https://www.home-barista.com/tips/hedrick-dial-in-espresso-forget-30-seconds-t99874-10.html), not fetched). Flair's 46.5 mm basket needs a coarser grind than a 58 mm basket (Niche Zero 24 to 28) because it makes a narrower puck.

**Table 2.3. Milk: target and ceiling temperatures**

| Milk | Target (°C) | Ceiling (°C) | Source | Label |
|---|---|---|---|---|
| Dairy, 3% | 60 to 65 | 70 | [PDG 2026](https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/) | blog |
| Dairy sweetness peak | about 60 (140 °F) | not stated | [Five Senses](https://fivesenses.com.au/blogs/news/how-to-steam-better-milk-at-home) | snippet |
| Dairy cappuccino | 55 to 65 | not stated | [Wikipedia](https://en.wikipedia.org/wiki/Cappuccino) | secondary |
| Latte, Italian definition | 58 to 70 for at least 210 g milk | not stated | [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso) | secondary |
| Oat barista blend | about 60 | 66 [conflict] vs no number | [PDG 2026](https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/); [ADS](https://ads-coffee-supplies.co.uk/?p=170252) (57 to 66 range, keep under 150 °F) | blog, snippet |
| Soy and almond | about 55 | 55 | PDG 2026 | blog |
| Plant milks, UK roaster | 50 to 55 | 55 | [Limini](https://liminicoffee.co.uk/article_understanding_milk) | blog |

The ceiling for dairy is contested. Sources give 70 °C (158 °F), 68 to 72 °C, and 65 to 71 °C as optimal ([Five Senses](https://fivesenses.com.au/blogs/news/how-to-steam-better-milk-at-home); [Lighthouse](https://www.lighthouse-coffee.com.my/?p=7081); [Clive Coffee](https://clivecoffee.com/blogs/faqs/how-to-steam-milk-for-lattes-and-cappuccinos-at-home-clive-coffee)). The claim that lactose caramelises at 60 to 65 °C is doubtful, since lactose needs far higher heat, and the PDG source puts burning above 70 °C [unverified]. The 2025 WBC competitor Jason Loo blended 70% freeze-distilled dairy, 20% coconut and 10% oat, steamed to 58 °C and chilled rapidly ([PDG 2026](https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/)). The 2024 WBC rules broadened the milk beverage beyond cow's milk ([PDG](https://perfectdailygrind.com/2023/11/new-rules-world-barista-championship-2024/)), and the 2026 rules allow up to two grinders ([WCC](https://wcc.coffee/latest-news/rules-regulations-released-for-the-2026-world-coffee-championships-in-panama)).

**Table 2.4. Espresso-based drinks: volumes and proportions**

| Drink | Espresso | Milk (ml) | Foam | Cup (ml) | Espresso:milk | Label |
|---|---|---|---|---|---|---|
| Espresso | 1 single, 25 to 30 ml | none | crema | about 60 | n/a | secondary, [Wikipedia](https://en.wikipedia.org/wiki/Espresso) |
| Doppio | 2 (50 to 60 ml) | none | n/a | demitasse | n/a | secondary |
| Macchiato | 1 | small dollop | dollop | about 60 | 1:0.25 | snippet |
| Cortado | 1 | equal to espresso | n/a | 120 to 135 | 1:1 [conflict] vs 1:1 to 1:2 | secondary |
| Flat white | 2 (50 ml) [conflict] vs 30 ml (Tourism NZ) | about 130 | about 5 mm microfoam | 150 to 200 [conflict] | about 1:2.6 [inferred] | secondary, [Wikipedia](https://en.wikipedia.org/wiki/Flat_white) |
| Cappuccino | 1 (WBC) or 25 ml (Italy) | equal to foam (thirds) | at least 1 cm (WBC minimum) | 150 to 180 (WBC); US chains 360 or more | 1:1:1 thirds | secondary, [Wikipedia](https://en.wikipedia.org/wiki/Cappuccino) |
| Latte | 1 to 2 | more than a flat white | thin, creamy | 200 to 300 (Wikipedia), 220 to 260, 236 to 443 [conflict] | about 1:2 (list) vs about 1:4 (snippet) [conflict] | secondary, [List of coffee drinks](https://en.wikipedia.org/wiki/List_of_coffee_drinks) |
| Americano | 1 to 2 | hot water | n/a | 150 to 180 (Wikipedia) vs 150 to 400 (list) [conflict] | dilution about 1:5 | secondary |
| Long black | 2 | water first, espresso over | n/a | 120 to 180 | n/a | snippet, [Onmanorama](https://www.onmanorama.com/food/features/2026/01/12/coffee-cup-sizes-guide.html) |
| Mocha | 1 to 2 | about two-thirds milk with chocolate | n/a | not stated | 1:2 | secondary |
| Café zorro | 2 | hot water | n/a | not stated | 1:1 water | secondary |
| Freddo espresso | 2 (30 to 50 ml) | ice 60 to 100 g | n/a | not stated | 1:2 with ice | secondary |

## Other methods: AeroPress well documented, cold brew and moka not

AeroPress has the most complete sourced data in this set. The **World AeroPress Championship** page lists each winner's dose, water, temperature, grinder setting and time for 2018 to 2025 ([WAC](https://worldaeropresschampionship.com/pages/recipes)). Winning doses dropped from 30 to 35 g in 2017 to 2019 to 16 to 18 g from 2022 onward, and most 2023 to 2025 podium finishes used an inverted press with a room-temperature or warm bypass. Hoffmann's "Ultimate" AeroPress is **11 g in 200 g at 99 °C**, a 1:18.2 ratio, with a total of about 3:20, from a [secondary page](https://aeroprecipe.com/recipes/james-hoffmann-aeropress-recipe).

**Table 3.1. World AeroPress Championship winners, 2021 to 2025 (first places unless noted)**

| Year, place | Competitor (country) | Dose / water (g) | Position | Temp (°C) | Grind | Time (s) |
|---|---|---|---|---|---|---|
| 2025, 1 | Nemo Pop (Australia) | 18 / 100, plus 70 g at 50 °C placed in carafe | upright | 84 | Trailmaster x25, 31 clicks, sifted 200 µm | about 70 |
| 2025, 2 | Jan Ahrend (Switzerland) | 18 / 100 | inverted | 88 | C40 Mk4, 24 clicks | about 120 |
| 2025, 3 | Dharun Vyas (India) | 16 / 65, then 208 total | inverted | 88 | C40 Red Clix, 52 clicks | about 90 |
| 2024, 1 | George Stanica (Romania) | 18 / about 100 | inverted | 96 | C40 Mk4, 58 clicks (870 µm) | about 135 |
| 2024, 2 | Sophan Nugraha (Indonesia) | 18 / 190 | inverted | 95 | C40 nitro blade, 22 clicks | 120 |
| 2024, 3 | Jamika Mahmoud (Egypt) | 18 / 150 | inverted | 75 to 80 | MK4, 900 µm | about 120 |
| 2023, 1 | Tay Wipvasutt (Thailand) | 18 / 100 | inverted | 89 | ZP6, 65 clicks | about 125 |
| 2023, 2 | Carlo Graf Bulow (Germany) | 18 / 160 | inverted | 100 | C40, 32 clicks | about 110 |
| 2023, 3 | Leon Zhang (China) | 18 / 100 at 93 °C, then 135 at 75 °C | upright | 75 to 93 | C40, 27 clicks | 100 |
| 2022, 1 | Jibbi Little (Australia) | 18 / 94 (setup lists 150) | inverted | 90 | Kinu setting 4 | about 130 |
| 2022, 2 | Simon Derutter (Belgium) | 18 / 140 (156 total) | upright | 85 | Comandante 23 clicks | about 105 |
| 2022, 3 | Jennifer Rui Ping Ho (Singapore) | 18 / 200 | inverted | 84 | Comandante 30 clicks | 120 |
| 2021, 1 | Tuomas Merikanto (Finland) | 18 / 200 (50 g at 80 °C first) | inverted | 80 | Macap Labo 70D, 7.0 | about 120 |

Source: [WAC recipes](https://worldaeropresschampionship.com/pages/recipes), official page. Hoffmann's timing for the AeroPress has three versions, a 2:00 steep, a 2.5 to 3 minute brew and a total near 3:30 [conflict]; no Hoffmann primary was opened.

**French press.** Secondary write-ups of Hoffmann's "Ultimate" method disagree on the amounts. [LAMOSE](https://secure.lamose.com/blogs/recipes/james-hoffmanns-french-press-method-the-better-way) gives **30 g in 500 g**, a 4-minute steep, stir to break the crust, skim, then settle for 5 to 8 minutes, with no plunge (ratio 1:16.7 [inferred]). [Fluent in Coffee](https://www.fluentincoffee.com/?p=5034242) gives **30 g in 450 g at 93 °C**, 1:15, medium-coarse and 10 to 12 minutes total. [Volcanica](https://volcanicacoffee.com/blogs/news/video-guide-french-press-technique-3-recipes-tested) gives **15 g in 225 ml** for 4 minutes [conflict]. Grind is coarse to medium-coarse, with 690 to 1,300 µm from [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/) and 800 to 1,100 µm or 1,000 to 1,200 µm from snippets [conflict]. None of these was checked against the video.

**Alternate drippers.** Kalita, Chemex and Origami have no manufacturer recipe in the set, and the values below come from brew guides.

**Table 3.2. Kalita, Chemex and Origami**

| Dripper and source | Dose / water (g) | Ratio | Temp (°C) | Grind | Bloom | Pours (s:cumulative g) | Time (s) | Label |
|---|---|---|---|---|---|---|---|---|
| Kalita Wave 155, [Ozone](https://ozonecoffee.co.uk/pages/kalita-wave-brew-guide) | 15 / 250 | 1:16.7 [inferred] | 93 | medium filter | 50 g at 30 s | 0:50, 30:150, 70:250 | 150 to 180 | secondary, undated |
| Kalita Wave 185, Ozone | 30 / 500 | 1:16.7 [inferred] | 93 | medium filter | 100 g at 30 s | 0:100, 30:300, 90:500 | 210 to 240 | secondary |
| Origami Air S, light roast, [Roasters Pack](https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes) | 20 / 320 | 1:16 | 95 | medium, Comandante 34 clicks (about 1,020 µm) | 60 g | 0:60, 30:120, 45:180, 60:240, 80:320 | 120 to 140 | secondary |
| Origami wave filter, medium roast, Roasters Pack | 20 / 320 | 1:16 | 92 | medium to medium-fine, Comandante 30 clicks (about 900 µm) | 50 g | 0:50, 30:100, 55:150, 80:200, 105:250, 125:320 | 160 to 180 | secondary |
| Chemex, Cafely | 55 / 917 (6-cup) | 1:16.7 [inferred] | not stated | medium-coarse (common guidance) | about 25% of water | not stated | not stated | secondary, [Cafely](https://cafely.com/blogs/coffee-brew-guide/chemex) |
| Chemex, Crema | 35 / 525 | 1:15 | not stated | not stated | not stated | not stated | not stated | secondary, [Crema](https://www.crema.co/workplace/guides/chemex-brewing) |
| Chemex, Homegrounds | not stated | 1:14 to 1:19 | not stated | not stated | about 100 g for 30 s | not stated | not stated | secondary, [Homegrounds](https://www.homegrounds.co/how-to-use-a-chemex/) |
| Chemex, Sample Coffee | 48 (6-cup) [conflict] | not stated | not stated | not stated | not stated | not stated | not stated | secondary, [Sample Coffee](https://cdn.samplecoffee.com.au/brewguides/chemex) |

The brief's Chemex figures (1:15 to 1:17, thick filter, 4 to 5 minutes) are not sourced and are not loaded.

**Cold brew.** Concentrate ratios run **1:4 to 1:6** in most guides. [Puroast](https://puroast.com/blogs/low-acid-coffee/cold-brew-ratio-the-complete-guide-to-getting-it-right) gives a 1:4 concentrate diluted 1:1, and 1:8 as a standard ready-to-drink, while another source gives 1:12 to 1:15 for ready-to-drink [conflict]. Concentrate lasts 7 to 14 days refrigerated ([Complete Home Barista](https://completehomebarista.com/guides/cold-brew-shelf-life/)) or 2 to 3 weeks sealed ([Colipse](https://colipsecoffee.com/blogs/coffee/cold-brew-shelf-life)) [conflict]; diluted cold brew keeps 3 to 5 days. No TDS or EY figure exists for any cold brew.

**Moka pot.** No verified dose, grind or time. Hoffmann's variation fills the base with water just off the boil to reduce scorching ([HuffPost](https://huffingtonpost.co.uk/entry/james-hoffmann-moka-pot-coffee-routine_uk_673b1cc9e4b0ebe12e36b57d)). Sources disagree on grind: medium-fine (Bialetti), 360 to 660 µm ([Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/)), and a claim that Hoffmann used a coarser grind with an AeroPress filter on top [conflict, unverified].

**Siphon** ratios run 1:10 to 1:15 (one guide at 1:14, one forum at 1:17), water 85 to 95 °C, total 3 to 5 minutes, and grind 375 to 800 µm [conflict on fine versus coarse]. Sources are blog-grade ([HomeGrounds](https://www.homegrounds.co/how-to-use-a-siphon-coffee-maker/); [Perfect Daily Grind](https://perfectdailygrind.com/2023/01/what-is-syphon-brewing/)).

**Batch brew and cupping.** The SCA Golden Cup standard sets **55 g/L (1:18.2) at 92 to 96 °C**, reaching 92 °C within the first minute and never exceeding 96 °C ([Nature Sci. Rep.](https://www.nature.com/articles/s41598-020-73341-4), snippet). Brew time (the brief's 4 to 8 minutes) was not found in any source. Cupping grind is "slightly coarser than typically used for paper filter drip", at 460 to 850 µm (470 to 850 on the same page) [conflict minor]. The SCA cupping protocol was not retrieved, and the brief's 8.25 g per 150 ml at 93 °C is unsourced and should not be loaded.

## Grind ranges disagree by up to 2x across guides

No standard micron chart exists. The only fetched chart, [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/), says its ranges come from "original guides and popular recipes", and its ranges are wider than the brief's. Barista Hustle's chart (HTTP 402) and the official Comandante, Weber and Baratza charts were not retrieved.

**Table 4.1. Grind size by method (µm)**

| Method | Min | Max | Note |
|---|---|---|---|
| Turkish | 40 | 220 | alternate 100 to 200 (snippet) |
| Espresso | 180 | 380 | Mahlkönig gives 200 to 400, a vendor gives 290 to 310; one HCG source says 200 to 300 but its own table says 600 to 800 [conflict] |
| Filter-machine batch | 300 | 900 | |
| AeroPress | 320 | 960 | widest range on the chart |
| Moka pot | 360 | 660 | medium-fine |
| Siphon | 375 | 800 | |
| V60 | 400 | 700 | brief says 600 to 900 [conflict] |
| Pour-over, general | 410 | 930 | |
| Steep and release | 450 | 825 | |
| Cupping | 460 | 850 | 470 to 850 on a later line |
| French press | 690 | 1,300 | alternate 800 to 1,100 and 1,000 to 1,200 [conflict] |
| Cold brew | 800 | 1,400 | alternate 1,200 to 1,600 and 1,000 to 1,500 [conflict] |
| Cold drip | 820 | 1,270 | |

Sources: [Honest Coffee Guide](https://honestcoffeeguide.com/coffee-grind-size-chart/), with snippets from [Beanbox](https://beanbox.com/blog/grind-size-cheat-sheet) and others. The chart's own labels are mixed (Turkish from 40 µm), so treat each row as a convention, not a measurement.

**Micron anchors from competitions.** Competition winners give a few micron values tied to a specific grinder. [WAC](https://worldaeropresschampionship.com/pages/recipes) lists 870 µm (C40 Mk4, 58 clicks, 2024) and 900 µm (MK4, 2024), and 200 µm sifted (Trailmaster, 2025). The WBC table gives 630 µm (Mazzer ZM, 2024) and 1,000 and 800 µm (2022). [Roasters Pack](https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes) pairs Comandante clicks with micron values, roughly 30 µm per click: 26 clicks at about 780 µm (2019), 28 at 840 µm (2023), 30 at about 900 µm and 34 at about 1,020 µm (Origami recipes). These are secondary and grinder-specific.

**Table 4.2. Grinder click settings (snippet; grinder-specific)**

| Grinder | Method | Clicks | Source note |
|---|---|---|---|
| Comandante C40 | French press | 26 to 40 | another guide says 28 to 34 ([BaristaLife](https://baristalife.co/blogs/blog/comandante-c40-grind-settings-chart)) |
| Comandante C40 Red Clix | French press | 51 to 80 | Red Clix scale differs ([HCG](https://honestcoffeeguide.com/comandante-c40-mk4-with-red-clix-grind-settings)) |
| Comandante C40 | AeroPress | 12 to 35 | typical 16 to 20 or 18 to 24 ([HCG](https://completehomebarista.com/guides/comandante-c40-grind-settings/)) |
| Comandante C40 | V60 or Kalita | 18 to 28 | start 22 to 28 (same) |
| Timemore C2 | French press | 20 to 30 | most cluster at 20 to 24 ([BaristaLife](https://baristalife.co/blogs/blog/timemore-c2-grind-settings-chart)) |
| Timemore C2 | AeroPress | 10 to 30 | one guide 10 to 14, another 11 to 30 ([HCG](https://completehomebarista.com/guides/timemore-c2-grind-settings/)) |
| Timemore C2 | V60 | 13 to 22 | another guide 14 to 18 (same) |

Click anchors transfer only within the same grinder and burr version, so store grinder model and firmware with each value.

**Water chemistry.** The SCA water standard, as restated by [field-guides](https://field-guides.vercel.app/pour-over/the-sca-water-standard.html), sets **TDS 150 mg/L (range 75 to 250), calcium hardness 68 mg/L as CaCO3 (17 to 85), alkalinity 40 mg/L as CaCO3, pH 7.0 (6.5 to 7.5), sodium 10 mg/L, and chlorine 0**. The [SCAA sheet](https://cdn.shopify.com/s/files/1/0561/9102/5336/files/water-standards.pdf) (revised 21 November 2009) lists calcium hardness as "4 grains" (68 mg/L), alkalinity 40, pH 7.0 (6.5 to 7.5) and sodium 10, but no TDS or chlorine, so the TDS figure appears to come from a study guide [conflict]. The SCAA sheet is the closest primary source and is the one to cite.

**Table 4.3. Water targets and commercial profiles**

| Parameter | SCA (secondary) | SCAA sheet, 2009 | Third Wave Water (official) | Other |
|---|---|---|---|---|
| TDS (mg/L) | 150 (75 to 250) | not listed | Classic 150; Medium 150; Dark 180; Espresso 150 | Coffee Tower gives 75 to 150 [conflict] |
| Calcium hardness (mg/L as CaCO3) | 68 (17 to 85) | 68 | not disclosed | 50 to 80 (Coffee Tower) [conflict] |
| Alkalinity (mg/L as CaCO3) | 40 | 40 | Classic 40; Medium 80; Dark 135 to 140; Espresso 80 | SCA handbook: below 40 risks corrosion; up to 75 for harder water ([Daily Coffee News](https://dailycoffeenews.com/2018/08/29/a-practical-water-guide-for-coffee-professionals-part-ii-the-sensory-data)) |
| pH | 7.0 (6.5 to 7.5) | 7.0 | not stated | not stated |
| Sodium (mg/L) | 10 | 10 | not stated | not stated |
| Mineral mix | none | none | MgSO4, calcium citrate, NaCl (Classic); KHCO3 for Medium and Espresso | Old forum quote: Classic alkalinity 0 and about 95 mg/L Mg as MgSO4 [conflict] |

Sources: [Third Wave Water](https://support.thirdwavewater.com/en-US/what-is-in-third-wave-water-76575) (mg/L per mineral withheld). Water for Coffee gives Ca 10 to 50 mg/L, Mg 5 to 30 mg/L and carbonate hardness 40 to 70 mg/L as CaCO3 ([Coffee Circle](https://coffeecircle.com/en/e/coffee-water), snippet). A Barista Hustle "Rao-like" recipe targets **GH 80 and KH 40** (1 g of concentrate per litre equals 1 ppm), but the page returned 402 [unverified]. Rao's own water preset is GH 72 and KH 20 in one guide [conflict], and [Complete Home Barista](https://completehomebarista.com/guides/best-water-recipe-espresso/) lists about 100 ppm total from 1.8 to 2.4 g per 4 L.

Flavor effects come from a [Daily Coffee News panel tasting](https://dailycoffeenews.com/2018/08/29/a-practical-water-guide-for-coffee-professionals-part-ii-the-sensory-data) (Kornman, 2018). High bicarbonate lowers perceived acidity and adds CO2 that impedes extraction; alkalinity-only water tastes flat and lacks sweetness, though it did best with dark roasts. Calcium accents acidity, while magnesium is sweet and floral in light roasts and cloying in dark ones. Distilled water scored highest overall in round two. [Hendon and Colonna-Dashwood (2014)](https://m.phys.org/news/2014-06-science-coffee.html) found magnesium extracts more efficiently than calcium and that bicarbonate hurts extraction; a [Royal Coffee blind tasting](https://www.home-barista.com/water/royal-coffee-blind-tasting-waters-t54215-20.html) could not confirm the claim that higher general hardness raises TDS [conflict].

**Table 4.4. Stoichiometry for a calculator (arithmetic from standard molar masses, not sourced recipes)**

| Conversion | Factor | Label |
|---|---|---|
| Anhydrous MgSO4 to Mg2+ | 1 mg/L Mg2+ per 4.95 mg/L MgSO4 | [inferred] |
| Anhydrous CaCl2 to Ca2+ | 1 mg/L Ca2+ per 2.77 mg/L CaCl2 | [inferred] |
| NaHCO3 to alkalinity as CaCO3 | 0.595 mg/L alkalinity per mg/L NaHCO3 (article's 0.1 g/L equals about 50 ppm; arithmetic gives 59.5) [conflict] | [inferred] |
| HCO3- to CaCO3 | multiply by 0.82 (50/61); the article's "80 ppm bicarbonate equals 130 as CaCO3" would need 159, not 80 | [inferred]; add a unit_basis field |
| Epsom versus anhydrous MgSO4 | anhydrous needs about 2x the mass of Epsom salt (heptahydrate) | [unverified] (forum) |

**Strength and burrs.** Flat burrs typically produce fewer fines than conical burrs, and the trade rule "flat for clarity, conical for body" is disputed. Rao, citing Gagne, argues that low-fines flat burrs can beat high-fines flat burrs for filter, so the rule is too simplistic ([Scott Rao](https://www.scottrao.com/blog/happymediumfines)). Grind distributions are bimodal, with boulders and fines under 100 µm, and finer settings raise the fines share ([Barista Magazine](https://www.baristamagazine.com/book-review-the-physics-of-filter-coffee-by-jonathan-gagne/)). A [2024 Scientific Reports paper](https://link.springer.com/10.1038/s41598-024-55831-x) (snippet) reports that finer espresso grinds raise pressure drop and lengthen extraction at 9 bar.

## Arabica supplies about 57% of beans; Gesha sets the price ceiling

Arabica (2n = 44, allotetraploid) is about 57% of world output and robusta (2n = 22) about 42% by [ICO's 2024/25 figures](https://www.ico.org/documents/cy2024-25/cmr-0525-e.pdf) (102.1 M and 75.4 M bags of 177.5 M total; the mapping of these figures to the document is [unverified]). The [USDA's 2024/25 estimate](https://www.comunicaffe.com/usda-biannual-report-cuts-estimate-of-world-production-for-2024-25-to-174-4-million) gives 174.4 M total and a 56.6% arabica share by my arithmetic. Liberica and excelsa are a rounding error: the 2025 species study puts global production "probably less than 1,000 metric tons", about 0.01% of exports, and calls the "1 to 2% of supply" figure outdated ([Daily Coffee News](https://dailycoffeenews.com/2025/08/21/study-says-liberica-and-excelsa-are-separate-species-with-implications-for-cultivation/)).

**Table 5.1. Species**

| Species | Ploidy (2n) | Share of output | Caffeine (% green bean) | Altitude and temperature | Disease | Cup | Source |
|---|---|---|---|---|---|---|---|
| *C. arabica* | 44 | about 57% (ICO) | 1.2 (12 mg/g) [conflict] vs 1.5 (Wikipedia comparison); PROTA 0.6 to 1.7 | 1,200 to 1,500 m typical; sea level to 2,800 m; 15 to 24 °C [conflict] vs 18 to 23 °C (GCR) | more susceptible than robusta; leaf rust costs up to $2 bn a year | sweeter, higher acidity | [Wikipedia](https://en.wikipedia.org/wiki/Coffea_arabica) |
| *C. canephora* (robusta) | 22 | about 42% (ICO) | 2.7 (Wikipedia); 1.5 to 3.3 (PROTA); 1.88 to 2.61 (7 Hainan cultivars) [conflict] | 800 to 1,500 m (snippet, unverified) vs brief 0 to 800 m [conflict]; 24 to 30 °C (GCR) vs 22 to 28 °C | "less susceptible" than arabica; not quantified | earthy, bitter, woody, low acidity | [Wikipedia](https://en.wikipedia.org/wiki/Coffea_canephora); [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6332462) |
| *C. liberica* | 22 | under 1,000 t a year (about 0.01% of exports) | 0.5 to 1.8 | lowland to 1,300 m; warm, humid | leaf rust, less than other species; berry borer 1 to 5% of fruit vs 16 to 77% in robusta (Malaysia) | more bitter than arabica or robusta | [PROTA](https://prosea.prota4u.org/view.aspx?id=608) |
| *C. dewevrei* (excelsa) | 22 [unverified] | tiny | not stated | heat- and drought-tolerant | not stated | less bitter than liberica | [DCN](https://dailycoffeenews.com/2025/08/21/study-says-liberica-and-excelsa-are-separate-species-with-implications-for-cultivation/) |
| *C. stenophylla* | 22 [unverified] | negligible | not stated | habitat mean annual temperature 24.9 °C | IUCN Vulnerable | 80.25 on one small tasting; natural sweetness, medium-high acidity | [Sci.News](https://www.sci.news/biology/coffea-stenophylla-09573.html) |
| *C. eugenioides* | 22 | negligible | 0.3 to 0.6 | not stated | not stated | mild, agreeable; low-caffeine breeding parent | [PROTA](https://prosea.prota4u.org/view.aspx?id=608) |
| *C. racemosa* | 22 | negligible | low, no % | not stated | not stated | high flavour, low caffeine | [SciELO](https://scielo.br/j/brag/a/nhMMmHfnNbFgwcLqcvySJBB/?lang=pt) |

Chromosome counts for stenophylla and excelsa are assumed from the genus norm [unverified]. Arabica's origin is the southwest Ethiopian highlands, and plantation coffee holds under 1% of the diversity of wild Yemeni populations ([Wikipedia](https://en.wikipedia.org/wiki/Coffea_arabica)). The [Denoeud 2014 genome paper](https://hal.inrae.fr/hal-02641562/document) describes robusta as an outcrossing, highly heterozygous diploid and one parent of arabica, with caffeine genes expanded by tandem duplication.

**Varieties in the World Coffee Research catalogue.** The [WCR index](https://varieties.worldcoffeeresearch.org/arabica/varieties) lists 70 arabica varieties. Table 5.2 gives the 5 to 15 degree altitude band, which is the single value the catalogue's latitude bands make most comparable (WCR gives 5N-5S, 5 to 15 and beyond 15 degrees, with no maximum). WCR's "quality potential" labels are not SCA scores.

**Table 5.2. Selected WCR varieties**

| Variety | WCR group | Origin, year | Min altitude, 5 to 15° (m) | Yield | Rust | Bean size | WCR note |
|---|---|---|---|---|---|---|---|
| Typica | Bourbon-Typica | Ethiopia, Yemen, Amsterdam 1706 | 1,300 | low | low (susceptible) | large | high quality in Central America; cold-tolerant |
| Bourbon | Bourbon-Typica | Yemen, Bourbon Island early 1700s | 1,300 | medium | low | average | excellent at highest altitudes |
| Caturra | Bourbon-Typica | Brazil, found 1915 to 1918 | 1,300 | medium | low | average | dwarf; standard in Central America |
| Catuaí | Bourbon-Typica | Brazil, created 1949, released 1972 | 1,300 | very high | low | average | compact; standard |
| Mundo Novo | Bourbon-Typica | Brazil, found 1943 | 1,300 | very high [unverified: other values listed] | mixed [unverified] | average | vigorous, productive, good cup |
| Pacas | Bourbon-Typica | El Salvador, 1949 | 1,300 | medium | low | average | dwarf; standard |
| Pacamara | Bourbon-Typica | El Salvador, Pacas x Maragogipe | 1,300 | low | low; highly susceptible to Ojo de Gallo | very large | exceptional potential; unstable across generations |
| Maragogipe | Bourbon-Typica | Brazil, 1870 | 1,000 to 1,300 | low | low | very large | good to very good in Central America |
| Villa Sarchi | Bourbon-Typica | Costa Rica, 1950s to 60s | 1,300 | medium | low | below average | adapted to highest altitudes |
| SL28 | Bourbon-Typica | Kenya, 1935 | 900 | low | low (varies by race) | large | drought-tolerant; exceptional |
| SL34 | Bourbon-Typica | Kenya, 1935 to 1939 | 900 | medium [unverified] | low [unverified] | large | exceptional but highly susceptible to CBD |
| Geisha (Panama) | Ethiopian landrace | Ethiopia, CATIE 1953, Panama 1960s | 1,300 | low | intermediate | average | delicate jasmine and peach aromas; exceptional at altitude |
| Java | Ethiopian landrace | Ethiopia, Java early 1800s | 1,300 | medium [unverified] | unclear [unverified] | large | high quality in Central America |
| Ruiru 11 | F1 hybrid | Kenya, 1985 | 700 | very high | highly resistant | large | dwarf |
| Batian | introgressed (other) | Kenya, 2010 | 700 to 900 | high | intermediate | very large | tall; tolerates low management |
| Centroamericano (H1) | F1 hybrid | Central America consortium, 2010 | above 1,300 recommended | very high | highly resistant | large | good above 1,300 m in healthy soil |
| Starmaya | F1 hybrid | Nicaragua, found 2001 | 900 to 1,300 | high | highly resistant | large | "notably high acidity" |
| Marsellesa | introgressed (Sarchimor) | Nicaragua, 2009 | 700 to 1,300 | high | intermediate | average | "notably high acidity" |
| Parainema | introgressed (Sarchimor) | Honduras, 2004 | 700 to 1,300 | very high | highly resistant (races can evolve) | large | good |
| Lempira | introgressed (Catimor) | Honduras | 700 to 1,300 | high | susceptible (rust confirmed) | average | quality potential low |
| Catimor 129 (Nyika) | introgressed (Catimor) | Colombia line, Malawi 2006 | 1,300 | high | intermediate | large | dwarf |
| Obata (Red) | introgressed (Sarchimor) | Brazil, 2000 | 700 to 1,300 | high | intermediate | large | good |
| S795 | introgressed (other) | India, CCRI | 900 | high | highly resistant in trials; susceptible in India [conflict] | large | very good |

Source for each row: the matching WCR page at `varieties.worldcoffeeresearch.org/varieties/<slug>`. Max altitudes are not in WCR.

**Varieties outside the catalogue.** Castillo (Colombia, 2005; multi-line rust resistance and reported CBD resistance; similar to Caturra in cup) and Cenicafé 1 (Colombia, 2016; improved CBD resistance) are from secondary sources, with the [Castillo page](https://www.gcrmag.com/castillo-proves-resistant-to-coffee-berry-disease) returning 403 [unverified]. Tabi (Colombia, 2002; rust-resistant, non-dwarfing) and Kent (India, 1911; initially resistant, since lost resistance) come from [Daily Coffee News](https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/). Laurina is a bourbon mutation with very low caffeine (0.3 to 0.75% versus 1.2 to 1.6%, a seller figure [unverified]). Icatu's parentage conflicts between sources. Pink Bourbon's genetics point to an Ethiopian heirloom rather than Bourbon [conflict].

**The "Core Ethiopia" group.** [Coffee Review](https://www.coffeereview.com/new-coffee-varieties/) cupping data (Oct 2023) gives Sidra 93 (7 samples, range 91 to 95), Chiroso 89 (5 samples, 84 to 94), Pink Bourbon 90 (3 samples, 89 to 92) and Wush Wush 88 (10 samples, 81 to 93). These are roaster-submitted scores on Coffee Review's own scale, not SCA scores. Sidra is absent from the WCR index, and [Royal Coffee](https://royalcoffee.com/?p=826035) says it "does not yet exist" in the catalogue. Its genetics are disputed: an Ethiopian landrace in one account, a Bourbon by Ethiopian cross in another ([Sey Coffee](https://www.seycoffee.com/products/cruz-loma)) [conflict]. Chiroso is called a Caturra mutation from Urrao, which conflicts with its Core Ethiopia grouping [conflict].

**Table 5.3. Gesha top-lot prices and related CoE records**

| Year | Top result | Price | Estate, process, score | Source | Label |
|---|---|---|---|---|---|
| 2004 | first Best of Panama Gesha | $21/lb | Hacienda La Esmeralda | [Wikipedia](https://en.wikipedia.org/wiki/Geisha_coffee) | secondary |
| 2005 | "record" per Wikipedia | $350/lb [conflict] vs "over $20/lb" per WCR | Peterson family | [WCR](https://varieties.worldcoffeeresearch.org/varieties/geisha-panama) | dates and amounts do not reconcile |
| 2017 | Best of Panama | $601/lb | Hacienda La Esmeralda, natural | [DCN](https://dailycoffeenews.com/2017/07/26/record-coffee-earns-601-per-pound-at-best-of-panama-auction) | secondary |
| 2018 | Best of Panama | $803/lb | Elida Estate, natural | [DCN](https://dailycoffeenews.com/2018/07/20/natural-geisha-breaks-best-of-panama-auction-record-at-803-per-pound) | secondary |
| 2019 | Best of Panama | $1,029/lb | Elida Estate, natural | [Beanscene](https://www.beanscenemag.com.au/elida-estate-natural-asd-geisha-makes-best-of-panama-auction-history-at-us1029-per-pound) | secondary |
| 2024 | Best of Panama | $4,542/lb (about $10,013/kg) | Lamastus Family Estates, natural [conflict: GCR says washed] | [DCN](https://dailycoffeenews.com/2024/08/15/best-of-panama-shatters-price-records-with-627-per-pound-average); [GCR](https://www.gcrmag.com/best-of-panama-auction-sees-world-record-price) | secondary |
| 2025 | Best of Panama, 6 to 7 Aug | $30,204/kg (about $13,700/lb; sources round to $13,705) | Hacienda La Esmeralda, washed, 98 points, buyer in Dubai | [Sprudge](https://sprudge.com/a-panama-gesha-broke-price-records-again-390362.html); [magazine.coffee](https://magazine.coffee/blog/1/6985/new-record-breaking-high-price-paid-at-best-of-panama-auction-2025) | primary-adjacent; Sprudge's "$1,000 per pound" claim is a likely unit error [conflict] |
| 2025 | natural lot | $23,608/kg | Hacienda La Esmeralda, 97 points | Sprudge | secondary |
| CoE Ethiopia 2022 | top Sidama lot | $400.50/lb | | [DCN](https://dailycoffeenews.com/2022/08/31/ethiopia-sidama-coffee-breaks-cup-of-excellence-record-at-400-50-lb) | secondary |
| CoE Ethiopia 2024 | top lot | $445/lb | East Sidama natural, Angelino's Coffee | [DCN](https://dailycoffeenews.com/2024/09/05/california-roaster-makes-record-bid-of-445-lb-at-ethiopia-cup-of-excellence) | secondary; the species file cites 2022 as the record, so it is out of date |

No Sidra auction record was found. Best of Panama results for 2020 to 2023 and any 2026 official results were not retrieved. Auction prices should not be used as a quality proxy, because Gesha lots run one to two orders of magnitude above CoE-winning prices.

## Brazil and Vietnam dominate volume; Ethiopia leads Africa

Production figures come from the USDA's July 2026 circular in thousand 60 kg bags, with 2025/26 as the latest estimate. Marketing years differ by country, so comparisons are approximate. World production is 178.8 M bags in 2025/26 and a forecast 189.7 M in 2026/27 ([USDA](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)). Brazil leads at 63.0 M, followed by Vietnam at 31.7 M, Colombia at 12.5 M, Indonesia at 12.37 M, Ethiopia at 11.56 M, Uganda at 7.10 M and India at 6.43 M.

### Africa and Arabia

Ethiopia's crop is 100% arabica, and it leads Africa. The USDA gives 11.56 M bags for 2025/26 and a record 12.1 M forecast for 2026/27. Uganda is about 84% robusta, and Côte d'Ivoire is entirely robusta.

**Table 6.1. Africa and Arabia: altitude, processing, harvest and flavour**

| Country, region | Altitude (m) | Varieties | Processing | Harvest | Flavour (source) | Label |
|---|---|---|---|---|---|---|
| Ethiopia, Sidama (Sidamo) | 1,500 to 2,200 | landraces, JARC selections | washed, natural | low Oct to Dec; high Nov to Jan | lemon, citrus, bright acidity ([Wikipedia](https://en.wikipedia.org/wiki/Coffee_production_in_Ethiopia)) | secondary |
| Ethiopia, Yirgacheffe | 1,676 to 2,195 (converted from 5,500 to 7,200 ft) | heirloom | washed typical; natural | Nov to Jan | washed: jasmine, bergamot, lemon, black tea; natural: blueberry, strawberry ([Copenhagen Coffee Lab](https://copenhagencoffeelab.com/en/blogs/inside-the-lab/yirgacheffe-kaffe-den-etiopiske-kaffe-alle-taler-om)) | unverified page-level |
| Ethiopia, Guji | 1,890 to 1,981 (from 6,200 to 6,500 ft) | heirloom | washed, natural, honey | Oct to Jan | [Coffee Hunter](https://coffeehunter.com/our-origins/ethiopia/) | unverified |
| Ethiopia, Harrar | 1,402 to 1,981 | longberry, shortberry, mocha | natural (dry) | Oct to Jan | fruity, winey, chocolate, spice | secondary |
| Ethiopia, Limu | 1,975 to 2,200 (one cooperative) | heirloom | washed | Oct to Jan | not stated | unverified |
| Kenya, Central (Nyeri, Kirinyaga, Murang'a, Kiambu) | 1,400 to 2,200 (AA lot 1,600 to 2,200; AB lot 1,400 to 1,800) | SL28, SL34, Ruiru 11, Batian, K7 | fully washed, raised beds | May to Jul; Oct to Dec | bright; blends with chocolatey South American coffees ([Sucafina](https://www.sucafina.com/na/origins/kenya)) | secondary |
| Rwanda (national) | 1,400 to 2,000 (lots 1,750 to 2,200) | Red Bourbon (about 95% of trees), Mibirizi, Caturra, Catuaí | central washing stations; some natural (Gakenke) | Mar to Jun; to Aug in Gakenke | Gakenke "sparkling acidity" ([Cafe Imports](https://www.cafeimports.com/europe/blog/?p=60653)) | unverified page-level |
| Burundi (Kayanza, Ngozi) | regional about 1,650 to 1,700; stations 1,600 to 2,000 | Bourbon, French Mission Bourbon, Jackson, Mibirizi | washed, honey, natural | Mar to Jul | "super sweet, clean and often floral" ([Sucafina](https://www.sucafina.com/na/origins/burundi)) | secondary |
| Uganda, Mt Elgon (Bugisu) | 1,200 to 2,600 [conflict across four sources] | SL14, SL28, Kent, Typica, Bugisu | washed (hand-pulped); DRUGAR; WUGAR | Jan to Apr and Sep to Oct; Oct to Feb in one source [conflict] | winey, fruity | secondary |
| Uganda, Rwenzori (Mubuku, Kasese) | farms 1,300 to 2,030; station about 1,020 | as above | natural (DRUGAR) and washed | Jan to Apr; Sep to Oct | not stated | secondary |
| Tanzania, north (Kilimanjaro, Arusha) | 1,050 to 2,500 | Bourbon, Kent, N39, Arusha | fully washed; natural emerging in south | Jul to Dec (Sucafina) vs May to Sep (Starbucks) [conflict] | not stated | secondary |
| Tanzania, south (Mbeya, Ruvuma) | 1,200 to 1,800 | Bourbon, Kent, N39 | washed; natural emerging | Jul to Sep | not stated | unverified |
| Malawi (Mzuzu, Misuku, Nkhata Bay) | 1,000 to 2,000; Misuku 1,700 to 2,000 | Agaro, Geisha, Catimor, Mundo Novo, Caturra | washed | Apr to Oct | not stated | unverified |
| Zambia (Muchinga, Lusaka) | 900 to 2,000 | SL34, Catimor, Starmaya, Marsellesa | not stated | Apr to Sep | not stated | unverified |
| DRC (Kivu) | 1,460 to 2,000 | not stated | washed, natural | not stated | not stated | secondary, dated |
| Yemen, Haraz | 1,800 to 2,400 vs at least 3,000 [conflict] | Udaini, Dawairi, Tuffahi, Jaadi | natural, sun-dried on raised beds | Oct to Feb | fruity, winey, "Red Sea wildness" ([Coffee Review](https://www.coffeereview.com/mocha-java-blends/)) | low reliability |
| Yemen, Bani Matar | 1,800 to 2,200 vs 2,500 to 3,000 [conflict] | as above | natural | Oct to Feb | balanced acidity, smooth body ([Ozone](https://ozonecoffee.co.uk/blogs/journal/new-release-yemen-ali-kabeer-jaadi-natural)) | low reliability |
| Saudi Arabia, Jazan (Khawlani) | 800 to 2,000 | Coffea arabica, no cultivar named | natural, shade-dried about 3 weeks | Oct to Jan | no tasting notes found ([Arab News](https://arabnews.com/node/1618606)) | secondary; UNESCO 2022 listing |

Grades in this region are mostly screen-size classes. Kenya runs AA (screen 17 or 18), AB (15 or 16) and peaberry, though AB can out-cup AA ([Royal Coffee](https://royalcoffee.com/?p=825659)). Burundi runs AA 18, AB 16 and C 14; Tanzania AA 18 and AB 15 to 17; Yemen AA 15 and A 14 (Cafe Imports chart). Ethiopia's ECX G1 to G5 scheme is not verified and is a placeholder.

**Table 6.2. Africa and Arabia: production (thousand 60 kg bags)**

| Country | 2024/25 | 2025/26 est. | 2026/27 forecast | Arabica share, 2025/26 | Label |
|---|---|---|---|---|---|
| Ethiopia | 11,460 | 11,560 | 12,100 | 100% | USDA [primary] |
| Uganda | 6,700 | 7,095 | 7,160 | 15.8% (1,120 of 7,095) | USDA |
| Kenya | 950 | 850 | 950 | about 100% | USDA; KNBS gives 51.4 kt (about 857k bags) [conflict] |
| Tanzania | 1,350 | 1,450 | 1,600 | 51.7% by arithmetic [conflict] vs 70 to 75% (trade) | USDA |
| Côte d'Ivoire | 650 | 1,300 | 1,300 | 0% | USDA; 2024/25 figure looks anomalous [unverified] |

Other African production is not in the USDA table. Rwanda is about 21,000 t (350,000 bags, [unverified]), Yemen about 26,500 t in 2024 (442,000 bags) [conflict with 18,000 to 19,000 t and an official 42,000 to 45,000 t claim], and Saudi Jazan 330 t (2020) [conflict with 646 t, 2019]. Two source conflicts matter for a dataset: ICO reports **Ethiopia 9.91 M bags for 2024/25 against USDA 11.46 M** ([ICO Oct 2025](https://www.ico.org/documents/cy2025-26/cmr-1025-e.pdf)), and Sucafina's undated multi-year average for Ethiopia is 7.86 M bags [conflict on basis]. Store both with a source label.

### Latin America and the Caribbean

Brazil is nearly 40% of world output, with **Minas Gerais over 70% of arabica and Espírito Santo about 70% of robusta** ([USDA](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)). Colombia is arabica-only and predominantly washed. The best-documented sub-regions come from the [Open Exam Prep South America and Central America guides](https://open-exam-prep.com/study-guides/sca-q-grader/coffee-geography-terroir-origins/south-american-origins), which are study-guide transcriptions, and from [Cafe Imports](https://www.cafeimports.com/north-america/colombia). No ANACAFE, ICAFE, IHCAFE, FNC, CONAB or SCAP document was retrieved, so all regional values are secondary.

**Table 6.3. Latin America: altitude, varieties, processing, harvest and flavour**

| Country, region | Altitude (m) | Varieties | Processing | Harvest | Flavour (source) | Grade | Label |
|---|---|---|---|---|---|---|---|
| Colombia, Huila | 1,500 to 2,100 vs 1,500 to 2,000 [conflict] | Caturra, Castillo, Colombia, Typica, Bourbon | washed | main Apr to Jul, mitaca Oct to Dec [conflict] vs main Nov to Jan (Cafe Imports) | red apple, panela, orange, yellow peach; medium-to-heavy body | Supremo (17/18); Excelso undefined | secondary |
| Colombia, Nariño | 1,700 to 2,300 | Caturra, Castillo, Typica, Bourbon | washed | Apr to Jul [conflict] vs single crop May to Aug | Meyer lemon, apricot, blackcurrant, honeysuckle | Supremo | secondary |
| Colombia, Cauca | 1,600 to 2,100 | Caturra, Castillo, Colombia | washed | Apr to Jul; mitaca Oct to Dec | red currant, sugarcane, sweet cherry, lemon zest | Supremo | secondary |
| Colombia, Tolima | 1,500 to 2,000 | Caturra, Castillo | washed | Oct to Dec; mitaca Apr to Jun | stone fruit, tangerine, caramel | Supremo | secondary |
| Colombia, Antioquia | 1,300 to 1,800 | Caturra, Castillo | washed | Oct to Dec; mitaca Apr to Jun | milk chocolate, hazelnut, mild citrus | Supremo | secondary |
| Brazil, Sul de Minas | 850 to 1,250 (about 1,000 in a blog) [conflict] | Yellow Bourbon, Mundo Novo, Catuaí | natural, pulped natural | Apr to Sep vs Oct to Mar [conflict] | chocolate, hazelnut, yellow fruit; low-to-medium soft acidity | none | secondary |
| Brazil, Cerrado Mineiro | 800 to 1,300 (1,400 or more in one blog) [conflict] | Catuaí, Mundo Novo | natural, pulped natural; mechanised | May to Sep | chocolate, nut, low acidity, heavy body | first Brazilian Denomination of Origin | secondary |
| Brazil, Mogiana | 900 to 1,100 | Bourbon, Catuaí | natural, pulped natural | not sourced | creamy, toffee (secondary) vs mild acidity, caramel, red fruit (snippet) [conflict] | none | secondary |
| Brazil, Matas de Minas | 600 to 1,200 | Catuaí, Mundo Novo | pulped natural, washed | not sourced | balanced citric sweetness, floral | none | secondary |
| Guatemala, Antigua | 1,500 to 1,700 vs 1,300 to 1,600 [conflict] | Bourbon, Caturra, Catuaí | washed | Sep to Apr | milk chocolate, sweet orange, floral, velvety | SHB threshold conflict (Table 7.2) | secondary |
| Guatemala, Huehuetenango | 1,600 to 2,200 vs up to 2,000 [conflict] | Bourbon, Caturra, Typica, Pache | washed | Sep to Apr | green apple, white peach, apricot, honeysuckle, winey | as above | secondary |
| Guatemala, Cobán | 1,300 to 1,500 | Bourbon, Caturra | washed | Sep to Apr | spiced stone fruit, tobacco, cedar, syrupy | as above | secondary |
| Costa Rica, Tarrazú | 1,200 to 1,900 vs 1,200 to 1,700 [conflict] | Caturra, Catuaí, Villa Sarchi | washed, honey, natural | Dec to Apr | grapefruit, green apple, cane sugar | SHB threshold 1,200 vs 1,350 [conflict] | secondary |
| Costa Rica, West Valley | 1,000 to 1,600 | Caturra, Catuaí, Villa Sarchi, Villa Lobos, SL-28, Gesha | washed, honey, natural | Dec to Apr | stone fruit, orange blossom, toffee | as above | secondary |
| Costa Rica, Tres Ríos | 1,200 to 1,650 vs 1,300 to 1,800 [conflict] | not stated | not stated | not stated | toffee, soft citrus | as above | snippet |
| Panama, Boquete | 1,200 to 1,900 vs 1,000 to 1,650 country-wide [conflict] | Geisha, Catuaí, Caturra, Mundo Novo | washed, natural, anaerobic | Nov to Mar | jasmine, bergamot, white peach, Earl Grey; silky | none | secondary |
| Honduras (six regions) | Copán 1,000 to 1,500; Opalaca 1,100 to 1,500; Montecillos 1,200 to 1,600; Comayagua 1,000 to 1,500; El Paraíso 1,000 to 1,400; Agalta 1,100 to 1,400 | Bourbon, Caturra, Catuaí, Typica, Parainema | washed most common; some honey and natural | not stated | chocolate, caramel (Copán); tropical fruit, grape (Opalaca); citrus, apricot (Montecillos); champagne, grape (El Paraíso) | SHG threshold conflict (Table 7.2) | secondary, [PDG 2017](https://perfectdailygrind.com/2017/08/introducing-the-6-coffee-regions-of-honduras/) |
| El Salvador, Apaneca-Ilamatepec | 500 to 2,300 (snippet) | Pacamara (Pacas x Maragogipe) | not stated | not stated | not stated | SHG at or above 1,200 | snippet |
| Nicaragua (national) | 1,100 to 1,600 vs 1,000 to 1,700 [conflict] | not stated | not stated | not stated | not stated | HG and SHG; no SHB | snippet |
| Mexico, Chiapas | not stated | not stated | not stated | Nov to Mar | Oaxaca: subtler, less acidic, citrus-forward | not stated | snippet |
| Peru, Cajamarca and San Martín | no verified figure | not stated | washed suited | not stated | Cusco described as both natural and washed [conflict] | not stated | snippet |
| Jamaica, Blue Mountain | cap 1,700 vs 1,800 m [conflict] | not stated | not stated | Aug to Sep vs Sep to Apr [conflict] | not stated | Grade 1 is screen 17 and up | secondary |
| Hawaii, Kona | 150 to 900 (one listing, unclear) | not stated | not stated | mid-Aug to Apr vs Aug to Dec [conflict] | not stated | HDOA grades; Extra Fancy screen 19/64 vs 18/64 [conflict] | unverified |

**Table 6.4. Latin America: production (thousand 60 kg bags)**

| Country | 2024/25 | 2025/26 est. | 2026/27 forecast | Arabica 2025/26 | Label |
|---|---|---|---|---|---|
| Brazil | 65,500 | 63,000 | 71,900 | 38,000 (60.3%); 2026/27 66.1% | USDA |
| Colombia | 14,800 | 12,500 | 13,400 | all arabica | USDA |
| Honduras | 5,200 | 5,530 | 6,030 | all arabica | USDA |
| Peru | 4,120 | 4,764 | 4,780 | all arabica | USDA |
| Mexico | 3,928 | 4,080 | 4,135 | 3,580 (87.7%) | USDA |
| Guatemala | 3,270 | 3,155 | 3,260 | 3,025 (95.9%) | USDA |
| Nicaragua | 2,660 | 2,560 | 2,440 | 2,400 | USDA |
| Costa Rica | 1,315 | 1,160 | 1,200 | all arabica | USDA |
| El Salvador | 581 | 586 | 542 | split not in table | USDA |
| Venezuela | 500 | 500 | 500 | split not in table | USDA |
| Ecuador | 355 | 350 | 350 | split not in table | USDA |

The table's columns were assigned by order from PDF text extraction, but totals reconcile (Brazil's arabica plus robusta equals total in every year). Export counts are not production: Costa Rica exports 1.2 to 1.5 M bags in 69 kg units, Guatemala 3.4 M in 69 kg units, Colombia 11 to 13 M in 70 kg units, and Panama 50,000 to 100,000 bags ([Cafe Imports](https://www.cafeimports.com/north-america/panama)). Those bag weights differ from the USDA's 60 kg standard, so they must be normalised before mixing.

### Asia-Pacific

Vietnam's crop is about 96% robusta, concentrated in the Central Highlands, which hold 92% of the area and 90% of output ([DCN on USDA](https://dailycoffeenews.com/2025/06/05/vietnam-coffee-report-production-exports-and-consumption-all-rising)). Indonesia's production is about 75% lowland robusta, and the rest is arabica from the wet-hulled regions. India is about 73% robusta.

**Table 6.5. Asia-Pacific: altitude, processing, harvest and flavour**

| Country, region | Altitude (m) | Varieties | Processing | Harvest | Flavour (source) | Grade | Label |
|---|---|---|---|---|---|---|---|
| Vietnam, Dak Lak and Dak Nong (robusta) | 400 to 800 (Dak Lak); 600 to 1,000 (Dak Nong) | robusta | washed or natural | Oct to Jan (Dak Lak); Nov to Mar in a second source [conflict] | not stated | TCVN 4193:2014 Grade 1, screen 16 or 18 | secondary, [Greentech](https://greentech-drl.pages.dev/guides/vietnam-coffee-origins) |
| Vietnam, Lam Dong (arabica and robusta) | 900 to 1,500 (Da Lat arabica about 1,000 to 1,500) | Catimor (main), Typica, Bourbon | washed arabica | Nov to Jan (arabica) | not stated | screen 16 or 18 | [Helena Coffee](https://www.helenacoffee.vn/product/arabica-catimor-fully-washed-s18/) |
| Indonesia, Mandheling (Sumatra) | 1,100 to 1,500 vs 1,200 to 1,600 [conflict] | not stated | wet-hulled (giling basah) | not stated | cocoa, tobacco, forest spice, earthy, molasses; heavy body, low acidity | G1 (loose trade term) | secondary, [Specialty Coffee Indonesia](https://specialtycoffee.id/articles/mandheling-coffee/) |
| Indonesia, Lintong (North Sumatra) | 1,400 to 1,600 vs 1,500 to 1,800 [conflict] | not stated | wet-hulled | not stated | plum, kumquat, molasses; syrupy | G1 TP (importer label) | secondary |
| Indonesia, Gayo (Aceh) | 1,400 to 1,800 or more | not stated | wet-hulled; some washed | not stated | dark chocolate, cedar, brown sugar, herbal; citrus lift | none | secondary |
| Indonesia, Toraja (Sulawesi) | 1,400 to 1,900 | not stated | wet-hulled | not stated | dark fruit, dark chocolate; heavy body | none | secondary |
| Indonesia, Kalosi (Enrekang) | 1,200 to 1,800 | not stated | dry-hulled (one guide) [conflict] | not stated | floral, spice, brighter acidity | none | secondary |
| Indonesia, Flores Bajawa | 1,200 to 1,800 (one source from 1,000) [conflict] | not stated | not stated | not stated | nutty, caramel, chocolate, medium body | none | secondary |
| Indonesia, Bali Kintamani | 1,200 to 1,700 | not stated | washed, natural, honey | not stated | citrus, molasses, bright acidity | none | secondary |
| Indonesia, Java Ijen | 900 to 1,500 (estimates vary) | not stated | mostly washed | not stated | chocolate, nuts, cinnamon, cedar; creamy | none | secondary |
| India, Mysore Nuggets (Chikmagalur, Coorg and others) | seller lots 1,067 to 1,524 (the Board gives none) | arabica (not sourced) | washed | not stated | not stated | Mysore Nuggets Extra Bold | secondary, [Coffee Board](https://coffeeboard.gov.in/Specialitycoffee.aspx) |
| India, Monsooned Malabar AA | 950 to 1,280 (seller) | arabica and robusta | dry, monsooned | not stated | musty, spicy, low acidity (brief); the Board says it mellows acidity | Monsooned Malabar AA | secondary |
| Papua New Guinea (Western and Eastern Highlands) | Eastern 400 to 1,900; Western 1,000 to 1,800; up to 2,800 claimed [conflict] | Bourbon, Typica, Arusha | washed | Apr to Sep | Simbu: melon, honey, full body ([Coffee Hunter](https://coffeehunter.com/journal-tag/papua-new-guinea/)) | none | secondary |
| China, Yunnan (Baoshan, Pu'er, Lincang) | Baoshan 1,200 to 1,800; Pu'er 1,000 to 1,500; Lincang 1,100 to 1,600; a Lincang Geisha lot 1,600 to 1,900 | Catimor (over 80% of area, per one source) | washed, honey | not stated | Baoshan: jasmine, nutty; Pu'er: plum-like acidity, caramel; Lincang: caramel, brown sugar, peach ([Yunnan Coffee Guide](https://yunnancoffeeguide.pages.dev/regions.html)) | none | secondary |
| Laos, Bolaven Plateau | 600 to 1,350 (plateau); washed lot 1,000 to 1,300 | Catimor, Typica, Caturra | not stated | not stated | not stated | none | secondary, [HomeGrounds](https://www.homegrounds.co/laos-coffee/) |
| Timor-Leste (Ermera, Letefoho) | 1,000 to 1,600, 1,200 to 1,800 or 1,300 to 1,900 [conflict] | Hibrido de Timor and others | not stated | May to Sep (Sucafina) vs May to Oct or Jun to Aug [conflict] | not stated | none | secondary, [Sucafina](https://sucafina.com/na/origins/timor-leste) |
| Philippines | arabica above 1,000 (Benguet, Kalinga, Sagada); liberica (Batangas) 300 to 600 vs 0 to 800 [conflict] | arabica; liberica; excelsa | not stated | not stated | arabica: sweet, floral, nutty | none | secondary |
| Hawaii, Ka'u | 335 to 825 (converted from 1,100 to 2,700 ft) | not stated | not stated | Aug to Dec (importer) vs mid-Aug to Apr (farm) [conflict] | not stated | HDOA grades | secondary, [Hawaii booklet](https://hca.wildapricot.org/resources/Documents/DOA-HICoffeeAssoc-Booklet.v4_print.pdf) |
| Vanuatu, Tanna | about 400 | not stated | not stated | not stated | full-bodied, nutty, low bitterness | none | secondary |

**Table 6.6. Asia-Pacific: production (thousand 60 kg bags, USDA 2025/26)**

| Country | Total | Arabica | Robusta | Note |
|---|---|---|---|---|
| Vietnam | 31,700 | 1,200 (3.8%) | 30,500 | 2026/27 forecast 32,500 |
| Indonesia | 12,370 | 1,370 (11.1%) | 11,000 | 2026/27 forecast 11,380; about 75% of robusta in Sumatra and Java |
| India | 6,430 | 1,730 (26.9%) | 4,700 | 2026/27 forecast 6,140 |
| Papua New Guinea | 800 | not stated | not stated | 2026/27 forecast 800 |
| China | 1,900 | 1,900 | 0 | all arabica (Yunnan) |
| Thailand | 900 | 0 | 900 | robusta |
| Laos | 475 | not stated | not stated | 2026/27 forecast 500 |
| Philippines | 450 | not stated | not stated | |
| Malaysia | 1,500 | not stated | not stated | listed as robusta; looks high [unverified] |

Asian Q Robusta scores run from 80 (fine robusta) to 90 (very fine) and 70 to 80 (premium) ([Kaffeemacher](https://kaffeemacher.de/en/blogs/kaffeewissen/fine-robusta-and-q-robusta-grading)). Two Vietnamese lots scored 86.00 and 85.50 in one listing [unverified]. Thailand's 2026 CoE winner from Nan scored 90.05 (name spelling unverified).

## Altitude raises density and acidity, but no source gives a rule per 100 m

The studies agree on direction and disagree on magnitude. Higher elevation is linked to denser beans, more acidity and better sensory results in several peer-reviewed or near-peer-reviewed studies, but effect sizes are reported only as correlations or significance, not as points per 100 m. Moderators include variety, shade, rainfall and processing. Altitude grade names (SHB, SHG, HG and similar) are national and inconsistent, so the same grade name can mean different metres in different countries.

**Table 7.1. Altitude studies**

| Study | Setting | Altitude finding | Label |
|---|---|---|---|
| Decazy et al. 2003, J Food Sci | 52 plots, six Honduran regions | high altitude and annual rainfall under 1,500 mm favoured quality; Olancho and El Paraíso highest ([CIRAD](https://agritrop.cirad.fr/515149)) | primary |
| Avelino et al. 2005, J Sci Food Agric | Orosi (1,020 to 1,250 m) and Santa María de Dota (1,550 to 1,780 m), Costa Rica | Dota chocolate stronger at altitude; Orosi floral depends on slope; taster preference rose with altitude in both; chemical markers weakly correlated ([Zendy](https://zendy.io/title/10.1002/jsfa.2188)) | primary; search summary only, full text not read |
| Bertrand et al. 2006, Tree Physiology | 700 to 1,600 m; El Salvador, Costa Rica, Honduras | traditional cultivars: chlorogenic acid and fat rise with elevation; Sudanese-Ethiopian hybrids show homeostasis ([CIRAD](https://publications.cirad.fr/une_notice.php?dk=532349)) | primary; snippet |
| Alpízar and Bertrand 2005 | Costa Rica | caffeine, chlorogenic acid and fat rise with elevation; trigonelline and sucrose fall ([AGRIS](https://agris.fao.org/search/fr/records/64745bb796fdec8b71b71879)) | primary; snippet; attribution flagged |
| Worku et al. 2017 | Ethiopia | title and authors only; effect sizes not retrieved | gap |
| Tolessa et al., J Sci Food Agric | Ethiopia; altitude, shade and harvest | high altitude with open or medium shade and early-to-mid harvest gave better beans; score changes small ([Sweet Maria's PDF](https://library.sweetmarias.com/wp-content/uploads/2020/08/Influence-of-growing-altitude-shade-and-harvest-period-on-quality-and-biochemical-composition-of-Ethiopian-specialty-coffee.pdf)) | primary; snippet |
| Ethiopian bean density study | south-western Ethiopia | highland beans denser than midland and lowland ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8991259)) | primary; snippet |
| Jimma University, 20 agro-ecological zones (2024) | Ethiopia | elevation correlated with bean traits; higher elevation raised acidity and complexity; rainfall not significant ([EurekAlert](https://www.eurekalert.org/news-releases/1094830)) | secondary press release |
| Beverage Plant Research 2024 (DOI 10.48130/bpr-0024-0021) | 20 Ethiopian sites | hundred-bean weight, moisture, crude fat, trigonelline and sucrose all rose with elevation | secondary; conflicts with Alpízar on trigonelline and sucrose |
| Tassew et al. 2021, Heliyon (per thesis abstract) | Kafa Biosphere Reserve | elevation significant on screen-14+ retention and most cup variables; high-elevation dry-processed lots raw 38.5 to 40%, cup 48 to 51.75% ([Jimma repository](https://repository.ju.edu.et/handle/123456789/10081?show=full)) | secondary |
| Ethiopian early-released varieties (2015) | south-west Ethiopia | cup quality correlated with acidity ([Sweet Maria's PDF](https://library.sweetmarias.com/wp-content/uploads/2020/08/Quality-Performance-of-Some-Early-Released-Coffee-Varieties-at-Three-Locations-in-South-West-Ethiopia.pdf)) | primary; snippet |
| Ovalle-Rivera et al. 2015, PLoS ONE | climate suitability, 2050s | suitability falls at lower altitudes in Mesoamerica; Ethiopia and Kenya gain; India and Vietnam lose ([IIASA](https://pure.iiasa.ac.at/11352)) | primary; PDF blocked |

Climate projections give two upslope-shift figures: **300 to 500 m** depending on location ([Table Debates](https://www.tabledebates.org/node/10876)) versus **about 300 m on average** by 2050 ([GCR](https://www.gcrmag.com/new-study-paints-grim-correlation-between-climate-change-and-coffee)) [conflict]. Neither was checked against the paper.

**Table 7.2. Altitude grade thresholds (Cafe Imports chart unless stated)**

| Country | Grade | Min (m) | Max (m) | Conflicting source |
|---|---|---|---|---|
| Costa Rica | SHB / SHG | 1,200 (chart) | not stated | SHB above 1,350 (Cafe Imports text) [conflict]; SHB above 1,200 (Open Exam Prep) |
| Costa Rica | GHB | 1,000 | 1,200 (chart) | 1,000 to 1,350 (Cafe Imports text) [conflict] |
| Costa Rica | MHB | not stated | below 1,000 | none |
| El Salvador | SHG | 1,200 | not stated | SHB above 1,400 in one source, treated as unreliable [conflict] |
| El Salvador | HG; CS | 900; 500 | 1,200; 900 | none |
| Honduras | SHG | 1,200 | not stated | 1,300 (IHCAFE, per one site); 1,350 and up; 1,500 [conflict] |
| Honduras | HG | 900 | 1,200 | 1,200 to 1,350 in one source [conflict] |
| Nicaragua | SHG; HG; CS | 1,200; 900; 500 | not stated; 1,200; 900 | cutoffs not verified in text [unverified] |
| Guatemala | SHB | 1,600 (chart) | 1,700 | above 1,350 (secondary); above 1,370 (Atlas); Open Exam Prep 1,350 [conflict] |
| Guatemala | FHB; HB | 1,500; 1,350 | 1,600; 1,500 | HB 1,200 to 1,350 (secondary); HB 1,066 to 1,370 (Atlas) [conflict] |
| Peru | SHB; HB | 1,350; 1,200 | not stated | chart prints "1200-1200" for HB (typo) |

Guatemala has at least three incompatible tables, and the best-supported value (SHB above 1,350 m) is the one to load, with the 1,600 to 1,700 m chart band kept as a disputed alternative. Costa Rica's SHB threshold is disputed (1,200 versus 1,350 m) until ICAFE is checked.

**Trigonelline and sucrose run in opposite directions.** Alpízar and Bertrand say they fall with altitude, while the 2024 Ethiopian study says they rise [conflict]. The dataset should store the direction with its study, not a single rule. On the other points the sources agree in direction: density rises with altitude, and fat and chlorogenic acid rise in traditional cultivars. A roaster consensus says acidity rises with altitude, but this is not measured and is [unverified]. Two other claims are background only: a lapse rate of about 0.6 °C per 100 m and ripening of 8 to 9 months above 1,800 m versus 6 to 7 months lower down, both [unverified]. Rainfall effects differ by study, with Decazy favouring under 1,500 mm and the Jimma study finding no significant rainfall effect [conflict in context].

## Agtron cutoffs depend on the authority; freshness runs about three weeks

Agtron cutoffs are not standardised. [Coffee Review's gourmet whole-bean scale](https://www.coffeereview.com/?p=22177) is the most complete published table, and the SCA-style alternatives are snippets that conflict with it. Second crack starts at about **Agtron 47** on that scale ([Coffee Review](https://www.coffeereview.com/?p=22177)).

**Table 8.1. Roast levels**

| Roast level | Agtron, Coffee Review (whole bean) | Alternative Agtron (snippet) | Drop temperature (blog) | Roast-name mapping (background) |
|---|---|---|---|---|
| Light | 71 to 100 | above 60 (SCA-style snippet) vs 71 to 80 [conflict] | 196 to 205 °C | Cinnamon about 85 to 100; New England to Nordic about 75 to 95 |
| Medium-light | 61 to 70 | not stated | not stated | City about 65 to 75 [conflict with Coffee Review band] |
| Medium | 51 to 60 | 45 to 60 | 210 to 220 °C | Full City about 45 to 55 [conflict] |
| Medium-dark | 41 to 50 | 35 to 45 | not stated | Vienna about 35 to 45 |
| Dark | 35 to 40 | below 35 | 225 to 230 °C | French about 25 to 35 |
| Very dark | 25 to 34 | not stated | not stated | Italian below 25 |
| Extreme dark | 0 to 24 | not stated | not stated | not stated |

Drop temperatures come from [Beanbox](https://beanbox.com/blog/light-medium-dark-roast-levels), a blog, and Beanbox notes they vary by 10 to 30 °F with probe and method [unverified]. The roast-name mapping is background knowledge with no fetched source, so it is [unverified] and should load only with a scale field (SCA_gourmet or CoffeeReview_Mbasic).

**Table 8.2. Roast metrics**

| Metric | Value | Source | Label |
|---|---|---|---|
| Development time ratio | 20 to 25% for most roasts; 15% can suit a high burner-to-batch ratio; 18 of the best 20 of 20,000 roasts fell in 20 to 25% | [Scott Rao](https://www.scottrao.com/blog/2016/8/25/development-time-ratio) | practitioner |
| Dark-roast mass | about 20% of dry matter lost; volume up to 80% | [Smrke et al. 2018](https://digitalcollection.zhaw.ch/bitstream/11475/12175/2/2017_Smrke-etal_Roasted-coffe-degassing-time-resolved-gravimetry.pdf) | primary; density units printed as kg/m3, probably g/cm3 [unverified] |
| Bean density | about 1.3 green to about 0.7 dark; porosity about 0.5 dark | Smrke 2018 | primary; units [unverified] |
| Colorette points | dark 78 ±1; medium 101 ±2; light 131 ±1 | Smrke 2018 (1 kg batch, El Salvador arabica) | primary; colour scale is not Agtron |
| Weight loss | light 12 to 14%; medium 14 to 16%; dark 16 to 20% | blog | [unverified]; moisture-loss claim of 15 to 16% light and 19 to 22% dark [conflict, different metric] |
| Roast time | 8 to 14 min | background | [unverified]; Smrke's 100 g sample roaster ran 7 to 8 min [conflict, scale] |
| Chlorogenic acid | 4 to 12% of green dry weight; dark roast loses over 80 to 90% | [Food & Function review](https://pubmed.ncbi.nlm.nih.gov/24671262/) | primary |
| CGA retention by level | light 50 to 70% of green; medium 30 to 50%; dark under 10 to 20% | background | [unverified] |
| Trigonelline and caffeine | trigonelline falls rapidly, forming pyridines and nicotinic acid; caffeine is roast-stable | Food & Function review; [J. Oleo Sci.](https://www.jstage.jst.go.jp/article/jos/71/10/71_ess22194/_article) | primary |
| Aroma | 74 volatiles identified, 25 aroma-active; the darkest roast burnt, putrid, sulfurous | [Molecules 2024](https://doaj.org/article/3851983d1e0b47ceb6dffa04801dc8a0) | primary |
| Peak temperatures | Maillard from about 150 °C; first crack about 196 °C; second about 224 °C | background | [unverified] |

Two more notes apply. Rao says his good roasts fall below 20% DTR but none above 25%, and he does not assume the ratio holds before first crack or after second-crack onset ([Home-Barista](https://www.home-barista.com/roasting/rao-on-development-time-ratio-t42962.html)). A Vietnamese robusta study reports caffeine peaking at 240 °C and then declining, a mass-loss concentration effect the source does not state ([Walailak](https://tis.wu.ac.th/index.php/tis/article/download/13444/2207/58793)) [unverified].

**Table 8.3. Freshness and degassing**

| Claim | Value | Source | Label |
|---|---|---|---|
| Whole-bean freshness | about 3 weeks | [SCA Coffee Decoded](https://sca.coffee/sca-news/coffee-decoded-9-fresh-coffee) | primary |
| Ground coffee | about 1 hour | SCA | primary |
| Whole-bean degassing | about 1 month; roughly 1% of bean weight as CO2 | [Smrke 2022](https://digitalcollection.zhaw.ch/bitstream/11475/26687/3/2022_Smrke-etal_Effects-of-different-coffee-storage-methods-on-coffee-freshness_FPSL.pdf) | primary; search summary |
| Ground coffee degassing | minutes to about 2 months | Smrke 2022 | primary |
| Storage method | screw-cap performed best; clips, tape and decanting lost freshness faster | Smrke 2022 | primary |
| Espresso rest, medium | 7 to 14 days | [Square Mile](https://shop.squaremilecoffee.com/blogs/all/rest-is-best) | snippet; 5 to 7 days in other blogs [conflict] |
| Espresso rest, light | 10 to 21 days (Coffee Parts) vs 5 to 10 days | [Coffee Parts](https://know.coffeeparts.com.au/glossary/degassing) | blog; conflict |
| Espresso rest, dark | 3 to 7 days | [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/coffee-degassing-how-long-to-rest-filter-coffee-and-espresso) | single source |
| Very fresh beans | 1 to 3 days off roast: gassy, channel-prone, gush | [Two Chimps](https://twochimpscoffee.com/what-is-coffee-degassing-2/) | snippet |
| Peak flavour window | 2 to 4 weeks after rest | [Brew Coffee Home](https://www.brewcoffeehome.com/?p=10459) | snippet |
| Aroma loss | 2-furfurylthiol weakens during staling | [Nottingham](https://nottingham-repository.worktribe.com/OutputFile/4482616) | primary; snippet |
| Staling rate | a 25 °C rise accelerates loss 100-fold | LinkedIn repost | [unverified]; do not load |
| Green coffee shelf life | 6 to 12 months at about 10 to 12% moisture and water activity 0.5 to 0.65 | background | [unverified]; numbers not retrieved |

The Smrke 2018 literature values for CO2 in roasted beans range from 0.7 to 4.3 mg/g to 16 mg/g, from studies with different times and methods, so they should not be averaged ([Smrke 2018](https://digitalcollection.zhaw.ch/bitstream/11475/12175/2/2017_Smrke-etal_Roasted-coffe-degassing-time-resolved-gravimetry.pdf)). The brief's espresso (5 to 21 days) and filter (4 to 28 days) windows match blog ranges but have no primary source.

## The flavor wheel holds 83 descriptors; the CVA total is unpublished

The SCA flavor wheel is documented here through a study-guide transcription, not the official graphic, which was not retrieved. The transcription lists **9 tier-1 families, 27 tier-2 subcategories and 83 tier-3 descriptors** ([Open Exam Prep](https://open-exam-prep.com/study-guides/sca-q-grader/flavor-wheel-sensory-lexicon/flavor-wheel-architecture)). Other sources count 85 descriptors ([glossary](https://coffee-e4d.pages.dev/learn/advanced/sca-flavor-wheel)) and 99 attributes ([Beanpoet](https://www.beanpoet.com/?p=6941)) [conflict].

**Table 9.1. SCA flavor wheel, tiers 1 to 3 (transcription)**

| Tier 1 | Tier 2 | Example tier-3 descriptors |
|---|---|---|
| Floral | Floral; Black Tea | chamomile, rose, jasmine; black tea |
| Fruity | Berry; Dried Fruit; Other Fruit; Citrus Fruit | blackberry, raspberry, blueberry, strawberry; raisin, prune; coconut, cherry, grape, apple, peach, pineapple; grapefruit, orange, lemon, lime |
| Sour/Fermented | Sour; Alcohol/Fermented | acetic, butyric, isovaleric, citric, malic acids; winey, whiskey, overripe |
| Green/Vegetative | Olive Oil; Raw; Green/Vegetative; Beany | under-ripe, peapod, fresh, hay-like, herb-like, beany |
| Other | Papery/Musty; Chemical | stale, cardboard, papery, woody, moldy, musty, animalic; bitter, salty, medicinal, petroleum, skunky, rubber |
| Roasted | Pipe Tobacco; Tobacco; Burnt; Cereal | pungent, ashy, smoky, brown/roast, grain, malt |
| Spices | Pungent; Pepper; Brown Spice | black pepper, nutmeg, cinnamon, clove, anise |
| Nutty/Cocoa | Nutty; Cocoa | peanuts, hazelnut, almond, chocolate, dark chocolate |
| Sweet | Brown Sugar; Vanilla; Overall Sweet; Sweet Aromatics | molasses, maple syrup, caramelized, honey, vanillin |

The official CVA form uses a simplified check-all-that-apply subset of these families, with Main Tastes limited to two of salty, sour, sweet, bitter and umami ([SCA CVA forms, May 2025](https://library.sweetmarias.com/wp-content/uploads/2025/06/SCA-CVA-Forms-English-May-2025.pdf), primary). The WCR Lexicon 2.0 (October 2017) defines **110 attributes**, and 24 of them have physical reference standards from FlavoursActiV capsules ([WCR](https://worldcoffeeresearch.org/news/2017/announcing-the-coffee-lexicon-2-0); [Tea & Coffee Trade Journal](https://www.teaandcoffee.net/news/18692/wcrs-sensory-lexicon-2-0-includes-new-global-flavour-standards-coffee/)).

**Table 9.2. Reference standards (2016 lexicon, transcription; intensity on the 15-point scale)**

| Attribute | Reference | Amount | Intensity |
|---|---|---|---|
| Sweet | sucrose | 1.0% | 1.0 |
| Sour | citric acid | 0.015% / 0.05% | 1.5 / 3.5 |
| Bitter | caffeine | 0.01, 0.02, 0.035, 0.05% | 2.0, 3.5, 5.0, 6.5 |
| Salty | NaCl | 0.15% | 1.5 |
| Peach (aroma) | fresh peach pit | not stated | 8.0 |
| Grape | Welch's 100% Concord juice | 1:1 with water | 5.0 |
| Lemon | lemon juice | 1:4 with water | 5.0 aroma / 7.0 flavour |
| Cardboard | cardboard, steeped in half a cup | 2 inch square | 7.5 |
| Papery | coffee filters soaked overnight | not stated | 2.5 |
| Phenolic | phenylacetic acid | 0.15 g | 6.0 |
| Mouth-drying | alum | 0.05% / 0.07% | 2.5 / 3.5 |
| Metallic | KCl | 0.10% | 1.5 |

Source: [Open Exam Prep, WCR standards](https://open-exam-prep.com/study-guides/sca-q-grader/flavor-wheel-sensory-lexicon/wcr-sensory-lexicon-standards), secondary. Jasmine and dark chocolate references are not described in any source.

**Aroma compounds mapped to the wheel.** The 2025 GC-O study of four commercial coffees (Foods 2025) gives FD and OAV values ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12469716/), primary). The wheel mapping is [inferred] from descriptors, not an SCA-published mapping.

| Compound | Odour (source) | FD / OAV | Wheel node (inferred) |
|---|---|---|---|
| Furaneol | caramel, marshmallow | FD 2187; OAV 175 to 250 | Sweet, Brown Sugar, Caramelized |
| 4-Vinyl-2-methoxyphenol | smoky | FD 243 to 2187; OAV 340 to 761 | Roasted, Burnt, Smoky |
| Guaiacol | woody | FD 2187; OAV 8 to 63 | Other, Woody (or Roasted, Smoky) |
| Furfural | nutty, almond | FD 2187; OAV 15 to 62 | Nutty/Cocoa |
| Linalool | floral, citrus, rose | FD 3 to 81; OAV 72 to 222 | Floral; Citrus |
| Isovaleric acid | sour, pungent | FD 243 to 729; OAV 72 to 200 | Sour/Fermented |
| Acetoin | buttery | FD 9; OAV 94 to 137 | no wheel node; nearest Sweet Aromatics [inferred] |
| Pyrazines (five named) | coffee, cocoa, roasted, almond, popcorn | OAV 1 to 170 | Nutty/Cocoa; Roasted |
| 2-Furfurylthiol | roasty (Grosch; 1.08 mg/L, OAV 1.1 x 10^5) | not in the 2025 paper | Roasted [inferred]; source is a [search summary](https://coffeeresearch.org/science/aromamain.htm) |

**The CVA replaces the 2004 protocol but withholds a total formula.** The CVA beta launched on 20 April 2023, and three standards followed in November 2024 (Sample Preparation and Cupping Mechanics, Descriptive Assessment, Affective Assessment, the last as SCA Standard 104-2024) ([SCA](https://sca.coffee/sca-news/sca-new-cva-cupping-standards-7ga28); [SCASA](https://magazine.coffee/blog/22/6964/education-introducing-the-coffee-value-assessment-by-the-sca-a-synopsis-from-scasa), secondary).

**Table 9.3. CVA forms (SCA, May 2025; primary)**

| Component | Content | Scale |
|---|---|---|
| Descriptive | Fragrance, Aroma, Flavor, Aftertaste, Acidity, Mouthfeel, Sweetness; CATA descriptor boxes; Main Tastes; purpose and roast level | intensity 0 to 15, marked LOW, MEDIUM, HIGH at 0, 5, 10, 15 |
| Affective | Fragrance, Aroma, Flavor, Aftertaste, Acidity, Mouthfeel, Sweetness, Overall; five cups per sample; non-uniform and defective-cup boxes; defect options Moldy, Phenolic, Potato | 9-point hedonic, 1 "extremely low" to 9 "extremely high" |
| Physical | 350 g sample; moisture; size meter calibrated to ISO 6673; Category 1 defects at 1:1 (full black, full sour, dried cherry, fungus damage, foreign matter) and 5:1 (severe insect damage); Category 2 at 3:1 (partial black, partial sour), 5:1 (parchment, floater, immature, withered, shell, broken, hull), 10:1 (slight insect damage) | defect-equivalent counts |
| Extrinsic (beta) | farming, trading (size grade, ICO number), processing (washed, natural, other), certifications | categorical |

The total score is computed on an SCA calculator (sca.coffee/cuppingscore), and the formula is not in any retrieved source. The 80-point specialty threshold and the 2004 bands (90 to 100 Outstanding, 85 to 89.99 Excellent, 80 to 84.99 Very Good) appear only in the brief and are [unverified]. The legacy 2004 form had ten attributes, and its defect rules are not retrieved. Do not convert CVA results to a 100-point score in code until the formula is obtained.

## Conflicts and gaps

Each row names a conflict or a gap, the values as sourced, the label, and how the dataset should handle it. Rows are grouped by area so each can be checked against its table.

**Pour-over and V60**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Hoffmann 2022 total time | about 3:00 (aeroprecipe) vs about 2:30 (search summary) | [conflict], [unverified] | keep both, flag video unviewed |
| Hoffmann 18 g gist vs 30 g schedule | pours 0:45, 1:15 to 180 g, 1:45 to 300 g vs 0:60, 0:45 to 300 g | [unverified] | separate recipe row, do not merge |
| Kasuya 2016 pour timings | Hario Europe 0:50, 0:45 to 120, 1:30 to 180... vs Kurasu 0:45, 1:30, 2:15, 3:00 at 60 ml each | [conflict] | store Hario Europe as primary |
| Kasuya 2016 total | 3:00 (Wikipedia) vs 3:30 (Hario Europe, Long Short London) | [conflict] | use 3:30 with note |
| Winton total time | 6:50 (Honest Coffee Guide) vs 2:40 (WBC table) | [conflict], [unverified] | keep both |
| Perger dose | not verified; a g/L column implies about 11.6 g | [unverified] | leave dose null |
| Drumming Barista "Full-bodied 5-pour" | pours sum to 300 g vs 250 g water | [conflict] | exclude or flag |
| 2025 champion temperature | 205 °F (about 96 °C) vs 210 °F (Slow Pour; likely typo) | [conflict] | store 96 °C with flag |
| 2025 champion total time | 1:45 (Sprudge) vs 2:15 (Honest Coffee Guide) | [conflict] | keep both |
| Kasuya water chemistry | 0.33 ppm and pH 6.6 (Long Short London), likely mis-transcribed | [unverified] | do not load |
| Competition ratio range | notes summary 1:12 to 1:16; table 1:12.9 to 1:16.7 | [conflict] within notes | use table arithmetic |
| Plastic versus ceramic brewing | PDG says plastic should brew cooler; Rao and Hoffmann use plastic for heat retention | [conflict] | store dripper material with a temperature note |
| V60 dose by size | 01: 12 to 24 g vs 12 to 20 g; 02: 18 to 42 g vs 18 to 40 g | [conflict] | secondary retailer comparison only; no Hario spec sheet read |
| Chemex ratio and dose | 1:14 to 1:19; 1:15; 1:17; 6-cup 55 g vs 48 g | [conflict] | secondary only; no official Chemex page |
| "Kalita Official Recipe" (21 g / 340 g) | aggregator label; not published by Kalita | [unverified] | do not attribute to Kalita |
| Target EY | Rao 22 to 24.5% vs Lockhart and SCA zone 18 to 22% | [conflict] | load both as separate targets |
| Brief's V60 grind target | brief 600 to 900 µm vs sourced 400 to 700 µm | [conflict], [brief] | keep sourced range, flag brief |
| V60 TDS | no source publishes TDS for any named recipe | gap | leave tds_pct null |

**Espresso and milk**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Ristretto ratio | 1:1 (Breville) vs 1:1 to 1:1.5 (snippet) | [conflict] | store both |
| Lungo time | 35 to 45 s vs 25 to 40 s | [conflict] | store both |
| Light-roast temperature | light 94 to 96 °C and dark 90 to 92 °C (snippets) vs 91 to 94 °C | [unverified] | load as unverified |
| Espresso EY | Hoffmann 23 to 24% claimed vs 18 to 20% traditional vs 18 to 22% typical | [conflict], [unverified] | keep as separate targets |
| Cameron 2020 | 15 g coarse matches 20 g EY (blog); 14 g not confirmed; paper not fetched | [unverified] | do not load as fact |
| Espresso rest | medium 7 to 14 vs 5 to 7; light 10 to 21 vs 5 to 10; dark 3 to 7 (single) | [conflict] | store roast-level windows with source |
| Espresso grind µm | 200 to 400 (Mahlkönig); 290 to 310 (vendor); 180 to 380 (HCG); 200 to 300 (brief); HCG table 600 to 800 | [conflict] | store 200 to 400 with source |
| Latte ratio | 1:2 (list) vs 1:4 (snippet) | [conflict] | store both |
| Latte cup | 200 to 300 vs 220 to 260 vs 236 to 443 | [conflict] | store both |
| Flat white | shot 50 ml vs 30 ml; cup 150 to 200 | [conflict] | store both |
| Cortado ratio | 1:1 vs 1:1 to 1:2 | [conflict] | store both |
| Americano water | 150 to 180 vs 150 to 400 | [conflict] | store both |
| Dairy scald threshold | 70 °C vs 68 to 72 °C vs 65 to 71 °C optimal | [conflict] | load 70 °C as hard cap, flag |
| Oat ceiling | about 60 °C (PDG) vs 57 to 66 °C with 66 max | [conflict] | store both |
| Lactose caramelisation | 60 to 65 °C claim; PDG says above 70 °C | [unverified] | do not load mechanism |
| WBC milk course | milk drink replaced cappuccino vs four identical cappuccinos | [conflict] | store as rule-set note |
| Missing drinks | affogato, breve, red eye, gibraltar, galao, café au lait | gap | leave empty |
| Basket doses | 9 g no source; 22 g only Breville's range | gap | leave empty |

**Other methods**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| AeroPress steep and total time | 2:00 steep vs 2:30 to 3:00 vs about 3:30 total | [conflict] | keep all |
| 2024 AeroPress champion | Stanica 96 °C, about 100 g (WAC) vs 92 °C, 200 g, about 2 min (Contour); name "Popescu" (Barista Magazine) | [conflict] | prefer official WAC page |
| 2025 podium orientation | snippet says 2023 to 2025 mostly inverted; WAC shows Nemo Pop upright | [conflict] | prefer official WAC page |
| French press dose and water | 30 / 500; 30 / 450; 15 / 225 | [conflict] | store all three |
| French press µm | 690 to 1,300 vs 800 to 1,100 vs 1,000 to 1,200 | [conflict] | store all, mark convention |
| French press video date | 2016 (LAMOSE) vs 2018 (brief) | [conflict] | leave date unresolved |
| Moka dose, grind and filter | 17 g medium-fine untamped vs coarser grind plus AeroPress filter | [conflict], [unverified] | leave empty |
| Cold brew ready-to-drink ratio | 1:8 vs 1:12 to 1:15 | [conflict] | store both |
| Cold brew shelf life | 7 to 14 days vs 2 to 3 weeks sealed; diluted 3 to 5 days | [conflict] | store both |
| Cold brew µm | 800 to 1,400 vs 1,200 to 1,600 vs 1,000 to 1,500 | [conflict] | store all |
| Siphon ratio, time and grind | 1:14 vs 1:17; 3 min vs 4 to 5 min; medium-fine vs medium-coarse | [conflict] | store all |
| Cupping grind | 460 to 850 µm vs 470 to 850 µm | [conflict] minor | keep 460 to 850 |
| Cupping protocol | brief's 8.25 g per 150 ml unsourced; SCA protocol not retrieved | gap, [brief] | do not load |
| Golden Cup brew time | brief's 4 to 8 min not found | gap | leave empty |
| SCA strength band | 1.15 to 1.35% (Golden Cup) vs 1.15 to 1.55% (SCA 310) | [conflict] | load as two standards |
| Batch brew temperature | 92 to 96 °C vs 90 to 96 °C | [conflict] | store both |
| Batch brew TDS for home machines | SCA 310 PDF returned 404 | gap | leave unverified |

**Grind and water**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| SCA TDS 150 mg/L | field-guides and study guide give 75 to 250; SCAA 2009 sheet lists no TDS | [conflict] | cite SCAA sheet for the other fields |
| Calcium hardness band | 68 (17 to 85) vs 50 to 80 (Coffee Tower) | [conflict] | store SCA values |
| Bicarbonate unit | 80 mg/L HCO3- equals 130 as CaCO3 (article) vs about 66 by arithmetic | [conflict], [inferred] | add unit_basis field |
| Baking soda | 0.1 g/L is 50 ppm (article) vs 59.5 (arithmetic) | [conflict] | use arithmetic, flag |
| Rao water recipe | GH 72 / KH 20 (Lotus) vs about 100 ppm (CHB) vs GH 80 / KH 40 (Barista Hustle, 402) | [conflict], [unverified] | store all three |
| Third Wave Classic alkalinity | 0 (older forum) vs 40 (official); Mg 95 mg/L MgSO4 (older) | [conflict] | use official, date the profile |
| Hendon magnesium claim | extraction and bicarbonate findings vs blind tasting did not confirm TDS effect | [conflict] | store as a claim with a test status |
| Epsom versus anhydrous MgSO4 | anhydrous needs about 2x mass | [unverified] | do not load |
| Flat versus conical burrs | trade rule vs Rao's critique | [conflict] | store as opinion |
| Brew Control Chart terms | strong, bitter and weak labels outdated; 2024 sensory chart not read | gap | leave terms out |
| EY formula and refractometer | not sourced; the formula is [inferred] | gap | flag as inferred |
| Brief's grind table | Turkish 100 to 250, espresso 200 to 300, moka 300 to 400, AeroPress 400 to 800, V60 600 to 900, Chemex 800 to 1,000, French press 900 to 1,300, cold brew 1,000 to 1,400 | [brief], not confirmed | do not load as sourced |

**Species and varieties**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Arabica and robusta share | ICO 57.5 / 42.5 (mapping unverified); USDA 56.6 / 43.4 (totals 174.4 M vs ICO 177.5 M); Brazil ministry 56 / 44 | [conflict] | store the source and total |
| Robusta altitude | 800 to 1,500 m (snippet) vs brief 0 to 800 m | [conflict], [brief] | store with confidence |
| Arabica caffeine | 1.2% (12 mg/g) vs 1.5% | [conflict] | store both |
| Robusta caffeine | 2.7% vs 1.5 to 3.3 vs 2.2 to 2.7 vs 1.88 to 2.61 | [conflict], [unverified] | store each with its study |
| Arabica and robusta temperature | arabica 15 to 24 vs 18 to 23 °C; robusta 24 to 30 vs 22 to 28 °C | [conflict] | store both |
| Liberica share | 1 to 2% (old) vs under 1,000 t (2025) | [conflict] | use the 2025 figure |
| Lipid, sucrose and CGA | arabica lipid 15 to 17 vs robusta 10.5 to 11; literature 13 to 17; Hainan 8.6 to 12; sucrose 6 to 9 vs 5 to 9.5 | [conflict], [unverified] | do not compare directly |
| Chromosome counts and caffeine for stenophylla, excelsa, eugenioides | assumed or unsourced | gap | flag |
| Sidra genetics and origin | Ethiopian landrace vs Bourbon-Ethiopian cross vs Core Ethiopia; absent from WCR | [conflict] | group "disputed" with low confidence |
| Chiroso | Caturra mutation vs Core Ethiopia | [conflict] | low group confidence |
| Pink Bourbon | Bourbon name vs Ethiopian heirloom genetics | [conflict] | low group confidence |
| WCR multi-value fields | Mundo Novo, Java and SL34 show unlabelled extra values | [unverified] | confirm on live pages |
| Laurina introduction | 1771 vs 18th to 19th century | [conflict] | store as range |
| Sudan Rume classification | landrace vs Ethiopian-type | gap | flag |
| Maracaturra score 91 | 2 samples, context unverified | [unverified] | do not use as typical |
| Stenophylla 80.25 | one small tasting | [unverified] | flag sample size |
| Gesha 2005 record | $350/lb (Wikipedia) vs "over $20/lb" (WCR) | [conflict] | store with source |
| Gesha 2024 top lot process | natural (DCN) vs washed (GCR) | [conflict] | store both |
| Sprudge 2025 "$1,000 per pound" | likely per kg | [conflict] | use the per-kg figure |
| Ethiopia CoE record | species file: 2022 at $400.50/lb; origins file: 2024 at $445/lb | [conflict] | load 2024; the species file is out of date |
| Best of Panama 2020 to 2023 and 2026 | not retrieved; a 2026 private auction figure is from a real-estate blog | gap, [unverified] | leave empty |
| Sidra auction record | none found | gap | leave empty |
| Coffee Review scores | roaster-submitted, not SCA | caveat | do not treat as SCA scores |

**Origins**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Ethiopia 2024/25 production | USDA 11.46 M vs ICO 9.91 M | [conflict] | store both with source |
| Ethiopia average | Sucafina 7.86 M (undated average) vs USDA 11.56 M (2025/26) | [conflict] | different basis |
| Kenya 2024/25 | USDA 950k vs KNBS 51.4 kt (about 857k) vs Sucafina 817.5k average | [conflict] | store all |
| Tanzania arabica share | 51.7% (USDA arithmetic) vs 70 to 75% (trade) | [conflict] | store both |
| Tanzania harvest | Sucafina May to Nov and Jul to Dec vs Starbucks May to Sep (north) and Jul to Sep (south) | [conflict] | store both |
| Mt Elgon altitude | 1,200 to 2,200; 1,300 to 2,200; 1,300 to 2,600; 1,500 to 2,500 | [conflict] | store as sources |
| Mt Elgon harvest | Oct to Feb vs Sep to Feb | [conflict] | store both |
| Yemen altitude | Haraz 1,800 to 2,400 vs at least 3,000; Bani Matar 1,800 to 2,200 vs 2,500 to 3,000 | [conflict], low reliability | store both, flag |
| Yemen production | 26,500 t (aggregator, FAOSTAT) vs 18,000 to 19,000 t vs 42,000 to 45,000 t official claim | [conflict] | flag |
| Saudi production | 330 t (2020) vs 646 t (2019, labelled GDP) | [conflict] | flag |
| Rwanda production | 21,000 t vs "over 1,000 t" specialty share | [conflict], [unverified] | flag |
| Rwanda competition name | "Best of Rwanda" (NAEB) vs "Cup of Excellence" (Twumba headline) | [conflict] | store competition field |
| Kenya auction prices | Sh901.71/kg (Jan to Sep 2025) vs Sh590.82 (2024); $268.77 vs $375.24 per 50 kg bag | [conflict], [unverified] | do not load |
| Côte d'Ivoire 2024/25 | 650 vs 1,325 (2023/24) and 1,300 (2025/26) | [unverified] anomaly | verify in PSD Online |
| Ethiopia grades | ECX G1 to G5 not verified | gap | leave empty |
| Ethiopia 2025 CoE and Burundi 2025 to 2026 | not found | gap | leave empty |
| Ethiopian $1,739/kg lot | source not identified | excluded | do not load |
| Rainfall and temperature by origin | none found except Honduras and Nariño | gap | leave empty |
| Colombia Huila altitude and harvest | 1,500 to 2,100 vs 1,500 to 2,000; main Apr to Jul vs Nov to Jan | [conflict] | store both |
| Colombia Nariño | Apr to Jul vs single crop May to Aug; 2,200 vs 2,100 m cutoff within one guide | [conflict] | store both |
| Excelso screen | not defined in any fetched page | gap | leave empty |
| Sul de Minas | 850 to 1,250 vs about 1,000; share 30% vs over 50%; harvest Apr to Sep vs Oct to Mar | [conflict] | store all |
| Cerrado altitude | 800 to 1,300 vs 1,400 or more | [conflict] | store both |
| Antigua altitude | 1,500 to 1,700 vs 1,300 to 1,600 | [conflict] | store both |
| Huehuetenango altitude | 1,600 to 2,200 vs up to 2,000 | [conflict] | store both |
| Costa Rica Tarrazú and Tres Ríos | 1,200 to 1,900 vs 1,200 to 1,700; 1,200 to 1,650 vs 1,300 to 1,800 | [conflict] | store both |
| Panama altitude | 1,200 to 1,900 (Boquete) vs 1,000 to 1,650 (country) | [conflict] | store both |
| Honduras SHG and HG | 1,200 vs 1,300 vs 1,350 vs 1,500 | [conflict] | see Table 7.2 |
| El Salvador SHB | above 1,400 vs SHG at 1,200 | [conflict] | treat 1,400 claim as unreliable |
| Nicaragua altitude | 1,100 to 1,600 vs 1,000 to 1,700 | [conflict] | store both |
| Jamaica Blue Mountain | cap 1,700 vs 1,800 m; harvest Aug to Sep, Sep to Apr, or Apr and Nov peaks | [conflict] | store all |
| Kona altitude and harvest | 150 to 900 (unclear); mid-Aug to Apr vs Aug to Dec; Extra Fancy 19/64 vs 18/64 | [conflict], [unverified] | store all |
| LatAm bag weights | 69 kg (Guatemala, Costa Rica), 70 kg (Colombia), 60 kg (USDA) | caveat | normalise before use |
| Peru altitudes, harvest and process | not verified; Cusco natural vs washed | gap, [conflict] | leave empty |
| Latin American CoE records | Guatemala, Nicaragua, Colombia, El Salvador, Peru, Mexico, Bolivia not found | gap | leave empty |
| Indonesia Mandheling altitude | 1,100 to 1,500 vs 1,200 to 1,600 | [conflict] | store both |
| Lintong altitude | 1,400 to 1,600 vs 1,500 to 1,800 | [conflict] | store both |
| Kalosi processing | dry-hulled (one guide) vs Toraja wet-hulled; labels overlap | [conflict] | flag |
| Flores Bajawa altitude | 1,200 to 1,800 vs from 1,000 | [conflict] | store both |
| Java Ijen altitude | 900 to 1,500 (sellers differ by 100 to 200 m) | [conflict] | store as union |
| Indonesia varieties and harvest | Typica, Catimor, Ateng, Timor Hybrid unsourced; harvest not found | gap | leave empty |
| Vietnam Dak Lak harvest | Oct to Jan vs Nov to Mar | [conflict] | store both |
| Vietnam robusta flavour | brief's bold, nutty, rubbery not confirmed | [brief], [unverified] | do not load as sourced |
| PNG altitude | Eastern 400 to 1,900 vs Western 1,000 to 1,800 vs up to 2,800 | [conflict] | store as sources |
| Timor-Leste altitude, harvest and Hibrido discovery | 1,000 to 1,600 vs 1,200 to 1,800 vs 1,300 to 1,900; May to Sep vs May to Oct; 1920s vs 1940s | [conflict] | store all |
| Philippines liberica altitude | 300 to 600 m vs 0 to 800 m | [conflict] | store both |
| Malaysia production | 1.5 M bags looks high | [unverified] | do not feature |
| Thailand CoE name | spelling unverified | [unverified] | flag |
| Yunnan harvest, processing and rainfall | not retrieved | gap | leave empty |
| India robusta flavour and monsooning details | not retrieved | gap | leave empty |
| Myanmar, Nepal, Sri Lanka, Okinawa, Fiji, Samoa, Australia, Malaysia liberica | no citable data | gap | leave empty |

**Altitude**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Trigonelline and sucrose direction | fall (Alpízar and Bertrand 2005) vs rise (Beverage Plant Research 2024) | [conflict] | record direction per study |
| Upslope shift | 300 to 500 m vs about 300 m average | [conflict] | cite the paper once retrieved |
| Acidity and altitude | roaster consensus; Jimma 2024 press says it rises | [unverified] vs secondary | store as direction only |
| Shade versus altitude | brief's claim not confirmed by Avelino 2005 (slope exposure) | gap | leave out |
| Effect sizes per 100 m and correlations | not retrieved from full texts | gap | store direction only, confidence medium |
| Lapse rate and ripening times | 0.6 °C per 100 m; 8 to 9 vs 6 to 7 months | [unverified] | do not load |
| Bean density numbers | no g/L or g/cm3 values by altitude | gap | leave empty |
| Rainfall effect | under 1,500 mm favoured (Decazy) vs no significant effect (Jimma) | [conflict] in context | store both with study |
| Grade cutoffs | see Table 7.2 | [conflict] | keep as separate rows with a source |
| Official ANACAFE, IHCAFE, ICAFE and Mexican, Peruvian grade tables | not retrieved | gap | flag |

**Roast and freshness**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Agtron scale | Coffee Review light 71 to 100; SCA-style snippet light above 60; another light 71 to 80 with Italian 0 to 30 | [conflict] | store scale field |
| Roast-name mapping | City 65 to 75 overlaps Medium-light; Full City 45 to 55 vs Medium 51 to 60 | [unverified], [conflict] | load only with a scale field |
| Drop temperatures | blog ranges; probe and method change values by 10 to 30 °F | [unverified] | flag probe type |
| Weight loss | dark 20% dry matter (Smrke) vs 16 to 20% (blog) vs 19 to 22% moisture (low) | [conflict] different metrics | store metric name |
| Smrke density units | printed as kg/m3 but values imply g/cm3 | [unverified] | flag |
| Roast time | 8 to 14 min (background) vs 7 to 8 min (sample roaster, 100 g) | [conflict] scale | store batch size |
| Espresso rest days | see Table 8.3 | [conflict] | store roast-level windows |
| Staling-rate claim (25 °C, 100-fold) | LinkedIn repost only | [unverified] | do not load |
| Green coffee shelf life and water activity | 6 to 12 months; aw 0.5 to 0.65 | [unverified] | leave empty |
| Freezing effect | no staling percentages | gap | leave empty |
| CO2 release values | 0.7 to 4.3 mg/g to 16 mg/g from different methods | [conflict] | do not average |
| Caffeine per cup | drip about 95 mg and espresso about 63 mg per shot (background) | [unverified] | do not load |
| CGA retention by roast | light 50 to 70% vs dark under 10 to 20% (background) | [unverified] | leave empty |
| Quantitative roast-level CGA and trigonelline | not retrieved | gap | leave empty |
| Acrylamide, phenylindanes, lactones | not retrieved | gap | leave empty |

**Flavour wheel and cupping**

| Conflict or gap | Sourced values | Label | Handling |
|---|---|---|---|
| Descriptor count | 83 (transcription) vs 85 (glossary) vs 99 attributes (Beanpoet) | [conflict] | use 83 and cite transcription |
| Official wheel graphic | not retrieved | gap | flag tier-3 table as secondary |
| CVA affective attribute count | 8 scored rows (official) vs 6 (retail blog) | [conflict] | prefer official |
| CVA total formula and 80-point equivalent | not in retrieved sources | gap | do not convert to 100 |
| 2004 protocol attributes, bands and defects | brief only; not verified | [unverified] | do not load |
| Jasmine and dark chocolate references | none described | gap | leave empty |
| Aroma-to-wheel mapping | inferred from descriptors | [inferred] | label as inferred |
| 2,3-butanedione and 2-furfurylthiol values | not in the 2025 paper; Grosch data via search | gap | flag source |
| CVA standard PDFs (SCA-103 and SCA-104-2024) and two SCA news pages | not read; two pages returned 404 | gap | flag |
| Coffee Review cupping scale | roaster-submitted, not SCA or CQI | caveat | do not treat as SCA scores |

## Conclusion

The notes give the FlavorLab tool a dependable recipe layer and a dependable origin-volume layer, but a thin strength layer. Named V60 recipes can be loaded with dose, water, ratio, temperature, pours and total time, and the champion table supplies a verified competition baseline. The strength data cannot be filled from these sources. No named pour-over recipe has TDS, espresso TDS and EY rest on blogs, and the two SCA strength bands disagree, so the tool should carry strength as a target envelope with a confidence tag, not as a per-recipe value. The same holds for origins: production volumes are usable once each figure is tagged with its marketing year and source (ICO and USDA differ by 1.5 M bags for Ethiopia), while altitude and grade thresholds should be stored as competing rows rather than one cutoff per grade. Sensory 1 to 10 ratings for origins are inferred and should never be exposed as source ratings.

For the schema, use one row per source value with `source_url`, `label` (sourced, inferred, unverified, conflict), `conflict_group`, `source_type` and `date`, plus the notes' field names (name, author, dose_g, water_g, ratio, temp_c, grind_um_min, grind_um_max, bloom_g, bloom_s, pours, total_time_s, tds_pct, ey_pct). Priority fetches, in order of value to the tool: the SCA 310 and 2004 cupping documents, the CVA calculator formula, the ICO country production table, ANACAFE and ICAFE grade rules, Hoffmann's own site (returned 404), and Barista Hustle's grind and water pages (returned 402).
