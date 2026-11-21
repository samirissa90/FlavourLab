# Espresso extraction parameters, troubleshooting, and espresso-based milk drinks

Research date: 2026-11-19. Method note: many primary sources blocked automated fetching (Hoffmann site 404, Cell/Matter 403, Barista Hustle 402, Barista Magazine 429, Home-Barista 403, WBC rulebook not retrievable). Where a number comes from a search-result summary rather than a fetched page, the row says "search snippet". Rows tagged `inferred` are my reasoning from cited numbers. Rows tagged `unverified` have no confirmed primary source. Dataset field names used throughout: style, dose_g, yield_g, ratio, time_s, temp_c, pressure_bar, tds_pct, ey_pct, drink, espresso_ml, milk_ml, foam_cm, cup_ml, source_url.

---

## 1. Espresso recipe parameters by style (ristretto, normale, lungo, turbo/allonge, modern ratios), plus dial-in procedure

### Takeaway
The consensus modern baseline is 18 g in : 36 g out (1:2) in about 25-30 s at about 93 C and 9 bar, with TDS about 8-12% and extraction yield (EY) about 18-22%. Ristretto is about 1:1 to 1:1.5, lungo about 1:3 or longer, and the modern specialty/light-roast trend (Hoffmann, Rao, Hedrick) goes to 1:2.5-1:3 or longer with longer times; time is treated as an output (flow indicator), not a target.

### Cited Findings

#### 1a. Style table (CSV-ready)
```
style,dose_g,yield_g,ratio,time_s,temp_c,pressure_bar,tds_pct,ey_pct,note,source_url
italian_certified_single,7 (+/-0.5),,,25 (+/-5),88 (+/-2 at unit exit),9 (+/-1),,,"volume in cup incl. crema 25 +/-2.5 ml; cup temp 67 +/-3 C",https://en.wikipedia.org/wiki/Espresso
ristretto,,,1:1 to 1:1.5,15-20,,,,,"search snippet; ratios vary by source; Breville states 1:1",https://simonandbearns.coffee/en/blogs/kaffeeblog/espresso-vs-ristretto-vs-lungo-vs-americano-differences-flavor-and-brewing
ristretto_breville,18-22,,1:1,,,,,,"Breville: ristretto 1:1; normale 1:2; lungo 1:3",https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso
normale,18,36,1:2,25-30,93,9,8-12,18-22,"1:2 baseline; temp 93 C from search snippet; tds/ey from search snippet",https://coffeebros.com/blogs/coffee/most-popular-espresso-shot-ratios-or-recipes
normale_breville,18-22 (20 g example),40 (from 20 g),1:2,25-30 (20-40 acceptable),,9,,,"fine table salt texture start",https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso
lungo,,,1:3 to 1:4,35-45,,,,,"search snippet; another snippet gives lungo 25-40 s",https://simonandbearns.coffee/en/blogs/kaffeeblog/espresso-vs-ristretto-vs-lungo-vs-americano-differences-flavor-and-brewing
modern_hoffmann_method,16/18/20,"40-48 / 45-54 / 50-60",1:2.5 to 1:3,"35-45 / 35-50 / 40-55",,,,23-24 (claimed),"ultra-fine grind 3-5 steps finer than traditional; traditional EY 18-20; secondary blog summary of Hoffmann, not Hoffmann directly",https://completehomebarista.com/guides/hoffman-method-james-hoffmann-espresso-technique/
rao_bh_baseline,18 (basket-rated),36,2:1 start; 2.5:1 or 3:1 for experienced,avoid >35,,,,,"Barista Hustle: dose = basket rating; avoid shot times > 35 s",https://www.scottrao.com/blog/2024/2/26/how-to-approach-brewing-different-coffees
rao_very_light_roast,,,up to 5:1,30,,,,,"higher flow rates for very light roasts (page text is Scott Rao's blog)",https://www.scottrao.com/blog/2024/2/26/how-to-approach-brewing-different-coffees
allonge_turbo_search,18,90,1:5 to 1:6,~30,,,,,"search snippet: allonge style coarser grind; one source says Rao showed 60 s extractions can work",https://coffeebros.com/blogs/coffee/most-popular-espresso-shot-ratios-or-recipes
hedrick_light_roast_flair,16,45 (shot 3; shots 1-2 30 and 40 failed sour),2.8:1 (aim ~3:1),~60,"""just off the boil"" (no number)",3 -> 8-9 -> declining (3 stages),,,"Niche Zero setting 24 -> 28; Flair 46.5 mm basket; sweet/fruity at shot 3",https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee
cameron_2020_matter,20 vs 15,,,<15 s possible at 15 g coarse,,,,17-23 (typical EY, secondary blog),"model + experiment: coarser grind with 15 g can match EY of 20 g shot; EY peaks then falls at very fine grind (channeling)",https://www.sciencedaily.com/releases/2020/01/200122110447.htm
```
Caveat on the last row: the Matter paper itself (Cameron et al. 2020, vol. 2 no. 3, pp. 631-648, DOI 10.1016/j.matt.2019.12.019, https://researchportal.port.ac.uk/en/publications/systematically-improving-espresso-insights-from-mathematical-mode/) was not fetchable. The 15 g vs 20 g figure comes from a blog quoting the paper (found via search); the Cameron paper snippet confirms only that measured EY peaks at an intermediate grind and falls at fine settings due to inhomogeneous flow. A 14 g figure was NOT confirmed (sources say 15 g).

#### 1b. Basket sizes and dose
- Typical doses: single about 7 g, double about 14 g, triple about 21 g — [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)
- Breville: 18-22 g is a "safe start," depends on portafilter and roast date — [Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso)
- Complete Home Barista adjustment ranges: 18 g basket 17.5-19.0 g; 20 g basket 19.0-21.0 g; yield for 18 g at 1:2 is 36 g, range 32-45 g — [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso)
- Italian certified dose: 7 +/- 0.5 g per single — [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)
- Search snippet: a reference guide lists dose 14-22 g, ratio 1:1.5-1:2.5, 25-35 s, credited collectively to Hoffmann, Rao, Barista Hustle — [Coffee Bros snippet](https://coffeebros.com/blogs/coffee/most-popular-espresso-shot-ratios-or-recipes)
- 9 g basket: no source found (unverified). 22 g basket: only the Breville 18-22 g range supports it.

#### 1c. Volumes by style (Wikipedia)
- Double normale about 60 ml; double ristretto about 30 ml; ristretto drink about 20 ml; lungo about 60 ml (table); typical serving 25-30 ml, typical pull 25-30 s — [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)
- Americano: espresso diluted about 1:5 with hot water (150-180 ml) — [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)

#### 1d. Temperature, pressure, pre-infusion
- Brew temperature range 86-95 C (187-203 F) — [Wikipedia List of coffee drinks](https://en.wikipedia.org/wiki/List_of_coffee_drinks)
- Default 200 F (93 C), adjustment range 195-205 F (90-96 C); pre-infusion 3-5 s (range 0-10 s); tamp 30 lb — [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso)
- By roast level (search snippets; no single primary source isolated): light roast 94-96 C; dark roast 90-92 C; one source 91-94 C; light-roast pre-infusion 4-6 s at 2-3 bar — [Flair search result](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee) (page itself gives no temperature; snippet figures came from other results in the same search: https://coffeeroastco.com/blogs/coffee-roast-co-blog/how-to-dial-in-espresso-2026). Mark: unverified as primary guidance.
- Pressure: 9 bar standard (Breville; Italian certified 9 +/- 1 bar) — [Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso), [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)
- Lance Hedrick light-roast profile: pre-infusion about 3 bar for 10-12 s, ramp/spike to 8-9 bar for 10-12 s, then lower pressure while holding flow until target yield — [Flair Espresso University](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee)
- Hedrick quote (secondary): extraction time is "a flow meter, not a goal" — search snippet, [Home-Barista thread](https://www.home-barista.com/tips/hedrick-dial-in-espresso-forget-30-seconds-t99874-10.html) (not fetched)
- Lever machines: 8-10 bar (116-145 psi) — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Historical: Faema E61 (1961) electric pump 9 bar; Gaggia (1947) piston up to 12 atm; c.1906 machines about 1.5 bar — [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)
- Pressure profiling 6-9 bar: only anecdotal (a home user reported a light roast peaking at 6.6 bar tasting better at 1:3) — search snippet via Home-Barista (unverified).
- Pause after pre-infusion ("bloom") credited to Rao work on the DE1+ — search snippet (unverified).

#### 1e. TDS and extraction yield
- TDS 8-12%, EY 18-22% for specialty espresso; EY = TDS x ratio (example: 9.5% TDS at 1:2 gives 19%) — search snippet, [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/espresso-vs-ristretto-vs-lungo-vs-americano-differences-flavor-and-brewing)
- Typical EY 17-23% in the Cameron paper summary — [ScienceDaily](https://www.sciencedaily.com/releases/2020/01/200122110447.htm) (blog summary figure; unverified against paper)
- Hoffman Method targets 23-24% EY vs 18-20% traditional — [Complete Home Barista](https://completehomebarista.com/guides/hoffman-method-james-hoffmann-espresso-technique/)
- Rao and Barista Hustle: the page for brew approach excludes TDS 1.3-1.4% (filter only); no espresso TDS or EY numbers there — [Scott Rao blog](https://www.scottrao.com/blog/2024/2/26/how-to-approach-brewing-different-coffees)
- Rao book "Espresso Extraction": 1:2, 18 in 36 out, 27-32 s, about 93 C reported as default (secondary, search snippet) — [search result set](https://coffeebros.com/blogs/coffee/most-popular-espresso-shot-ratios-or-recipes)

#### 1f. Dial-in procedure
- Change one variable at a time; grind is the first thing to adjust; darker roasts need finer grind — [Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso)
- Start: texture like fine table salt — [Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso)
- Grind adjustment by shot time (1:2 target 25-30 s): under 20 s go 1-2 settings finer; 20-24 s 1 finer; 25-30 s on target; 31-35 s 1 coarser; over 35 s 2 coarser — [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso)
- Time is an output of grind, dose, and yield — search snippet, [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/espresso-vs-ristretto-vs-lungo-vs-americano-differences-flavor-and-brewing)
- Hedrick: taste matters more than time; wipe basket rim to avoid water beads causing channeling; use WDT before tamping — [Flair](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee)

### Inferences
- inferred: a combined CSV by roast level could use light 94-96 C, 1:2.5-1:3+, 30-60 s; medium 92-94 C, 1:2, 25-30 s; dark 90-92 C, 1:1.5-1:2, 22-28 s. Only the light/dark temperatures have even snippet support; time and ratio by roast level are my synthesis.
- inferred: EY at 1:2 with TDS 9-11% is 18-22%, consistent with the cited EY = TDS x ratio identity; at 1:3, TDS 7-7.5% gives the same EY range (arithmetic).
- inferred: the Italian certified "single" (7 g, 25 ml, about 3.5:1 ratio by volume) shows why Italian-style normale is a shorter ratio than the modern 1:2 by weight (arithmetic, mass of 25 ml with crema is uncertain).

### Gaps
- Primary Rao (book/blog), Hoffmann (guide returned 404), Barista Hustle recipe page (402), and Matter paper text were not retrievable; their numbers are secondary.
- SCA espresso standards document (water 90-96 C, TDS bands) not retrieved; no SCA primary number captured for espresso.
- No source for 9 g basket; no sourced temperature by roast beyond snippets.
- Hedrick's own ratios/temperatures beyond the Flair article not obtained.

---

## 2. Troubleshooting decision table

### Takeaway
Sour/thin/salty with fast flow is under-extraction (grind finer, raise yield, raise temperature); bitter/astringent/hollow with slow flow is over-extraction (grind coarser, lower yield, lower temperature); bitter-but-fast shots signal channeling, fixed by distribution (WDT), level tamp, and a clean basket rim, not by grinding coarser. Adjust one variable at a time.

### Cited Findings
CSV-ready troubleshooting table (symptom,diagnosis,action,source_url):
```
symptom,time_s,diagnosis,action,source_url
sour thin salty,<20,under-extracted,grind 1-2 settings finer,https://completehomebarista.com/guides/how-to-dial-in-espresso
sour lacks body,20-24,slightly under-extracted,grind 1 setting finer OR raise yield,https://completehomebarista.com/guides/how-to-dial-in-espresso
sour underdeveloped,25-30,under-extracted,raise yield 2-4 g,https://completehomebarista.com/guides/how-to-dial-in-espresso
balanced sweet,25-30,optimal,keep settings,https://completehomebarista.com/guides/how-to-dial-in-espresso
bitter harsh,25-30,over-extracted,lower yield 2-4 g,https://completehomebarista.com/guides/how-to-dial-in-espresso
bitter dry,31-35,slightly over-extracted,grind 1 setting coarser,https://completehomebarista.com/guides/how-to-dial-in-espresso
ashy burnt,>35,severely over-extracted,grind significantly coarser (2 settings),https://completehomebarista.com/guides/how-to-dial-in-espresso
bitter astringent but fast,<20,channeling / uneven extraction,check distribution (WDT); grind slightly finer; level tamp,https://completehomebarista.com/guides/how-to-dial-in-espresso
fast shot sour thin,fast,under-extracted,grind finer OR raise dose by 1-2 g,https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso
slow shot over-extracted,slow,over-extracted,grind coarser OR reduce dose slightly,https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso
sour on light roast,~55-60,under-extracted,lengthen ratio (yield up toward ~3:1); coarsen grind; raise flow early in shot,https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee
```
Other cited findings:
- Flow starts fast then slows: channeling or clumps; improve WDT; inconsistent timing: uneven distribution or tamp, use WDT and level tamp; cannot reach target time at grinder limit: change dose by 0.5 g; always over/under-extracted: try ratio 1:2 or 1:2.5; drift between shots: grinder retention/heat, purge — [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso)
- A tilted tamp causes channeling on the high side — search snippet via [Complete Home Barista Hoffman Method result set](https://completehomebarista.com/guides/hoffman-method-james-hoffmann-espresso-technique/) (not confirmed on the fetched page)
- Fresher beans need finer grinds, older beans coarser — [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso)
- Cameron et al.: measured EY peaks then falls at very fine grind because of inhomogeneous flow/channeling; model alone predicts a monotonic drop with coarser grind — [Portsmouth research portal abstract via search](https://researchportal.port.ac.uk/en/publications/systematically-improving-espresso-insights-from-mathematical-mode/)
- Water temperature as a fix: Barista Hustle mentions lowering temperature only qualitatively for defective flavors (no number) — [Scott Rao blog](https://www.scottrao.com/blog/2024/2/26/how-to-approach-brewing-different-coffees)
- Crema color: no sourced numeric/diagnostic guidance retrieved (see Gaps).

### Inferences
- inferred: temperature step for corrective action of +/-1-2 C is consistent with the 90-96 C operating range but no source states a step size.
- inferred: yield step 2-4 g (Complete Home Barista) equates to about +/-0.1-0.2 ratio units on an 18 g dose.

### Gaps
- No source retrieved on crema color diagnosis (pale/blonde vs dark/streaky), tamp pressure effects with numbers, or puck screen effects on time.
- Grind step size in microns per click is grinder-specific; no source.

---

## 3. Beans for espresso: roast, age, degassing, puck prep

### Takeaway
Rest espresso roast about 7-14 days (up to 10-21 for light roasts); very fresh beans (1-3 days) hold much CO2 and channel/gush. Puck prep: WDT, level tamp at about 15-30 lb, optional puck screen, clean basket rim.

### Cited Findings
- Most espresso peaks 7-14 days off roast; some naturals and darker roasts want 10+; Square Mile recommends 7-14 days — search snippets via [Square Mile](https://shop.squaremilecoffee.com/blogs/all/rest-is-best) and [Complete Home Barista](https://completehomebarista.com/guides/how-long-after-roasting-brew-espresso/)
- Beans 1-3 days off roast contain enormous CO2 causing channeling and gushing — search snippet, [Two Chimps](https://twochimpscoffee.com/what-is-coffee-degassing-2/)
- Roast-level variants (conflicting): light 10-21 days, medium 7-14 days; another source dark 3-7 days, light 5-10 days; Clive Coffee internal 7-11 days; Coffee Parts 10-21 days — search snippets via [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/coffee-degassing-how-long-to-rest-filter-coffee-and-espresso), [Clive Coffee](https://clivecoffee.com/blogs/learn/is-your-coffee-too-fresh), [Coffee Parts](https://know.coffeeparts.com.au/glossary/degassing)
- Peak flavor maintained about 2-4 weeks after rest, then gradual decline — search snippet, [Brew Coffee Home](https://www.brewcoffeehome.com/?p=10459)
- Tamp: about 30 lb (Complete Home Barista); 15-30 lb (Hoffman method guide); tamp pressure beyond about 15 kg / 33 lb noted as problem area — [Complete Home Barista](https://completehomebarista.com/guides/how-to-dial-in-espresso), [Hoffman Method guide](https://completehomebarista.com/guides/hoffman-method-james-hoffmann-espresso-technique/)
- WDT strongly recommended, especially for ultra-fine grounds; puck screen goes on last after tamping — [Hoffman Method guide](https://completehomebarista.com/guides/hoffman-method-james-hoffmann-espresso-technique/)
- Dose matched to basket rating (18 g in an 18 g basket) — [Scott Rao blog](https://www.scottrao.com/blog/2024/2/26/how-to-approach-brewing-different-coffees)
- Darker roasts need finer grind (Breville) — [Breville](https://www.breville.com/en-us/blog/coffee-and-espresso/how-to-dial-in-espresso)
- Flair 46.5 mm basket makes a narrower, deeper puck than 58 mm so needs a coarser grind (Niche Zero 24 -> 28) — [Flair](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee)
- Flow control: Hedrick's 3-stage profile above (flow-rate control stage) — [Flair](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee)

### Inferences
- inferred: a dataset can store rest_days_min/max by roast level as dark 3-7 (single source), medium 7-14, light 10-21 with conflict flagged.
- inferred: tamp pressure has weak influence relative to distribution quality; no source here directly states this, treat 15-30 lb as a tolerance band.

### Gaps
- No primary degassing study (a ZHAW attribution to a 7-14 day figure appeared on LinkedIn only; unverified).
- No numeric puck screen, flow control, or WDT needle-diameter data.

---

## 4. Milk: steaming temperature, microfoam, alternatives, art

### Takeaway
Dairy milk is steamed to about 55-65 C (peak perceived sweetness at around 60 C); above about 70 C taste degrades (scalding/burnt). Oat barista blends work best around 60 C; soy and almond are cited at about 55 C maximum to avoid curdling/splitting.

### Cited Findings
```
milk,target_temp_c,max_temp_c,note,source_url
dairy_3pct,60-65,70,"lactose sweetness window 55-65 C; above 70 C flavor unpleasant",https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/
dairy_sweetness_peak,~60,,"140 F (search snippet)",https://fivesenses.com.au/blogs/news/how-to-steam-better-milk-at-home
dairy_cappuccino_wbc_context,55-65,,"Wikipedia cappuccino: steam to 55-65 C (131-149 F) to preserve sweetness",https://en.wikipedia.org/wiki/Cappuccino
dairy_latte_wikipedia_espresso,58-70,,"caffe latte: at least 210 g milk at 58-70 C",https://en.wikipedia.org/wiki/Espresso
oat_barista,~60,,"performs best around 60 C (140 F)",https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/
soy_almond,~55,55,"maximum to prevent curdling/splitting",https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/
oat_alt_snippet,57-66 (135-150 F),66 (150 F),"keep under 150 F to prevent separation; oat barista blends use dipotassium phosphate to resist curdling in acidic espresso",https://ads-coffee-supplies.co.uk/?p=170252
plant_milk_uk_roaster,50-55,55,"alternatives served about 50 C, no more than 55 C",https://liminicoffee.co.uk/article_understanding_milk
```
- 2025 WBC competitor Jason Loo steamed a blend of 70% freeze-distilled cow's milk, 20% coconut milk, 10% oat milk to 58 C then rapidly chilled it — [Perfect Daily Grind 2026](https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/)
- Properly heated 3% dairy milk tops out about 60-65 C (Charles Temkey, Flair) — [Perfect Daily Grind 2026](https://perfectdailygrind.com/2026/02/more-baristas-focusing-on-milk-temperature-coffee-shops/)
- Scalding threshold conflict: 70 C (158 F) in some sources, 68-72 C in another, and one guide lists 65-71 C as optimal — search snippets via [Five Senses](https://fivesenses.com.au/blogs/news/how-to-steam-better-milk-at-home), [Lighthouse](https://www.lighthouse-coffee.com.my/?p=7081), [Clive Coffee](https://clivecoffee.com/blogs/faqs/how-to-steam-milk-for-lattes-and-cappuccinos-at-home-clive-coffee)
- Mechanism claim that lactose "caramelises" at 60-65 C is doubtful (lactose normally needs much higher heat); the PDG source says lactose "can caramelise or burn" above 70 C — treat mechanism as unverified.
- WBC cappuccino: minimum 1 cm foam depth, single shot, 150-180 ml total — [Wikipedia Cappuccino](https://en.wikipedia.org/wiki/Cappuccino)
- Flat white microfoam about 5 mm thin layer — [Wikipedia Flat white](https://en.wikipedia.org/wiki/Flat_white)
- WBC milk rules: milk beverage no longer required to be cow's milk after the 2024 revision; no additives to milk allowed in 2024 rules — search snippet, [Perfect Daily Grind](https://perfectdailygrind.com/2023/11/new-rules-world-barista-championship-2024/)

### Inferences
- inferred: for a latte-art tool, store dairy target 60-65 C, hard cap 70 C; oat 55-60 C; soy/almond max 55 C; flag conflicting sources.
- inferred: whole milk (3% fat) is the reference for microfoam texture; the sources retrieved give no numeric fat/protein values for whole vs plant milks.

### Gaps
- No numeric stretch/aeration time, steam pressure, or microfoam bubble size from an authoritative source.
- No retrieved latte-art technique source (pour height, wiggle frequency).
- Almond and soy: only one source (PDG quote) gives a number; no independent confirmation.
- Whole vs plant milk protein/fat comparison numbers not found.

---

## 5. Standard drinks (volumes, ratios, espresso count, foam depth, WBC definitions)

### Takeaway
Sources agree on ordering by milk proportion (macchiato < cortado < flat white < cappuccino < latte), but exact ml values vary. Anchors: cortado 1:1 espresso to milk; cappuccino thirds (1:1:1), 150-180 ml with minimum 1 cm foam (WBC); flat white about 130 ml milk plus a double, about 5 mm microfoam, 160-200 ml cup; latte 200-300 ml.

### Cited Findings
```
drink,espresso_shots,espresso_ml,milk_ml,foam_cm,cup_ml,ratio,note,source_url
espresso_single,1,25-30,0,,~60 (cup),,"crema; Italian certified 25 +/-2.5 ml",https://en.wikipedia.org/wiki/Espresso
doppio,2,50-60,0,,demitasse,,"double shot",https://en.wikipedia.org/wiki/List_of_coffee_drinks
ristretto,1,~20 (single),0,,,,"double ristretto about 30 ml",https://en.wikipedia.org/wiki/Espresso
lungo,1,~60,0,,smaller than americano,,"all water brewed through grounds",https://en.wikipedia.org/wiki/Espresso
macchiato,1,~25-30,small dollop foam,,~60,1:0.25 espresso:milk (search snippet),,https://instacuppastore.com/blogs/main-page/espresso-cup-size-guide-espresso-cappuccino-latte-cups-ml
cortado,1,,equal to espresso,,~120-135,1:1,,https://en.wikipedia.org/wiki/List_of_coffee_drinks
piccolo,1 ristretto/single,,,,~90,1:4 (one search snippet),,https://shop.procoffeegear.com/blogs/articles/coffee-drinks-chart-explained
flat_white,2 (50 ml; Tourism NZ cites 30 ml),50,~130,0.5 (about 5 mm),175 (NZ) to ~200 (AU); 150-180 and 160 in other sources,,"higher coffee to milk than latte",https://en.wikipedia.org/wiki/Flat_white
cappuccino,1 (WBC) / 1-3 today,25 (Italy),equal thirds milk+foam,>=1 (WBC min),150-180 (WBC); 150-160 (flat white page),1:1:1,"US chains 360 ml or more",https://en.wikipedia.org/wiki/Cappuccino
latte,1-2,,more than flat white,thin creamy layer,200-300 (Wikipedia Cappuccino) ; 225 (NZ); 220-260 (InstaCuppa),~1:2 espresso:milk (list-of-drinks comparison),https://en.wikipedia.org/wiki/List_of_coffee_drinks
caffe_latte_italian_def,,,>=210 g milk at 58-70 C,,,,https://en.wikipedia.org/wiki/Espresso
americano,1-2,,150-400 ml hot water (list) / 150-180 total (Wikipedia espresso),,,1:3 to 1:5,"dilution about 1:5 per Wikipedia Espresso",https://en.wikipedia.org/wiki/List_of_coffee_drinks
long_black,2,,water first then espresso poured over to keep crema,,120-180 (Onmanorama),,https://www.onmanorama.com/food/features/2026/01/12/coffee-cup-sizes-guide.html
mocha,1-2,,about 2/3 drink milk plus chocolate,,,1:2 espresso:milk,https://en.wikipedia.org/wiki/List_of_coffee_drinks
cafe_zorro,2,,hot water 1:1,,,1:1 espresso:water,https://en.wikipedia.org/wiki/List_of_coffee_drinks
freddo_espresso,2,30-50,ice 60-100,,,1:2 espresso:ice,https://en.wikipedia.org/wiki/List_of_coffee_drinks
freddo_cappuccino,2,30-50,cold milk froth 1:2 to espresso; ice 60-100,,,,"Greek; originated 1991",https://en.wikipedia.org/wiki/Cappuccino
```
- InstaCuppa volume summary: espresso and macchiato about 60 ml; cortado about 135 ml; flat white about 160 ml; cappuccino and americano about 150-180 ml; latte about 220-260 ml — search snippet, [InstaCuppa](https://instacuppastore.com/blogs/main-page/espresso-cup-size-guide-espresso-cappuccino-latte-cups-ml)
- Size-charts.com: latte 236-443 ml; cappuccino 147-177 ml — search snippet, [Size-Charts](https://size-charts.com/topics/coffee-sizes-from-espresso-to-oversized-latte)
- Italy cappuccino: 25 ml espresso, rest equally milk and foam; traditional cup max 180 ml; early-2000s fast-food versions up to 600 ml — [Wikipedia Cappuccino](https://en.wikipedia.org/wiki/Cappuccino)
- Cortado ratio 1:1 to 1:2 per Wikipedia Cappuccino; 1:1 per List of coffee drinks — [Wikipedia Cappuccino](https://en.wikipedia.org/wiki/Cappuccino)
- Affogato, breve, red eye, gibraltar, galao, cafe au lait: not found in the pages read (see Gaps).
- WBC: each competitor serves espresso, milk beverage, and signature beverage, 12 drinks across courses; the 2024 rules broadened the milk beverage to allow other milks and ratios; 2026 rules let competitors skip serving spoons (override of drink evaluation protocol), allow up to two grinders (Ceado REV Zero and E37Z-Naked are approved models) — [World Coffee Championships](https://wcc.coffee/latest-news/rules-regulations-released-for-the-2026-world-coffee-championships-in-panama), [Perfect Daily Grind 2023](https://perfectdailygrind.com/2023/11/new-rules-world-barista-championship-2024/) (snippet)
- Conflict on the WBC milk course format: Wikipedia snippet says the cappuccino was replaced by a broader "milk drink"; one blog still describes four identical cappuccinos — [Wikipedia WBC](https://en.wikipedia.org/wiki/World_Barista_Championship) vs [Barista Life](https://baristalife.co/blogs/blog/world-barista-championship-rules)

### Inferences
- inferred: espresso:milk by drink in a normalized scale: macchiato 1:0.25, cortado 1:1, flat white about 1:2.6 (50 ml : 130 ml, arithmetic from Wikipedia values), latte 1:4 (snippet), cappuccino 1:1:1 volume thirds.
- inferred: flat white vs latte differ chiefly by cup size and foam thickness (5 mm vs thicker/varied), per cited sources.

### Gaps
- WBC rulebook text (drink volumes, time limits, dairy definition for 2025/2026) not retrieved; official documents are at wcc.coffee/rules-regulations.
- piccolo, breve (half-and-half), affogato (espresso over ice cream, scoops), red eye (drip + espresso), gibraltar, galao, cafe au lait: no numeric sourcing; do not populate without another source.
- No SCA drink-definition document found.

---

## 6. Machine facts: group heads, boilers, flow profiling, grinders, grind size

### Takeaway
Boiler types are single boiler (brew only or dual-use), heat exchanger (HX, needs a 4-6 s cooling flush), dual boiler (stable brew temp and strong steam), and thermoblock. Espresso grind is cited at roughly 200-400 um in vendor sources; no peer-reviewed number for a "200-300 um" figure was found. Flat burrs give unimodal and conical burrs bimodal distributions (vendor claims).

### Cited Findings
- Single boiler (SB): brews but doesn't steam, relatively uncommon; SB/DU: one chamber for both, one at a time, purge leftover brew water before steaming — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Heat exchanger (HX): boiler at steaming temperature with brew water passed through an exchanger; needs a "cooling flush" of 4-6 s before first pull; first HX was Faema E61 (1961) — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Dual boiler (DB): separate brew and steam boilers; stable brew temperature and fast steaming at greater size and cost; first was La Marzocco GS (1970) — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Thermoblock: more stable brew temps but slower steaming — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Group head: consumer machines typically one; professional machines one to seven — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Pump: solenoid-piston, positive displacement; spring-piston lever machines 8-10 bar (116-145 psi) — [Wikipedia Espresso machine](https://en.wikipedia.org/wiki/Espresso_machine)
- Flair PRO 2 basket 46.5 mm vs 58 mm commercial basket — [Flair](https://flairespresso.com/blogs/news/espresso-university-dial-in-light-roasted-coffee)
- Espresso particle size typically 200-400 um (Mahlkonig); another vendor targets 290-310 um — search snippets, [Mahlkonig](https://www.mahlkoenig.com/blogs/news/microns-grind-consistency)
- Urnex: Mahlkonig K30 median drifted from 230 um to 320 um after 100 kg of coffee due to burr wear/fines (cleaning-company test, not peer-reviewed) — search snippet, [Urnex](https://urnex.com/blog/why-coffee-particle-size-distribution-matters-for-your-cafe)
- Peer-reviewed: Scientific Reports 2024 found finely ground espresso has a bimodal particle size distribution and finer grinds create larger pressure drop, lengthening extraction at 9 bar; used sieved fines added to one grinder — search snippet, [Scientific Reports](https://link.springer.com/10.1038/s41598-024-55831-x)
- Flat burrs unimodal; conical burrs bimodal (vendor claim) — search snippet, [Clive Coffee](https://clivecoffee.com/blogs/learn/what-is-particle-size)
- Jonathan Gagne (Barista Hustle): measuring fines down to about a dozen microns is very hard by imaging — search snippet, [Barista Hustle](https://www.baristahustle.com/?p=350279)
- Wikipedia Espresso: brew water about 88 C certified at unit exit, 9 bar entry pressure — [Wikipedia Espresso](https://en.wikipedia.org/wiki/Espresso)

### Inferences
- inferred: the "about 200-300 um" range in the task brief is a lower-bound subset of the vendor 200-400 um range; record as 200-400 um with source and flag 200-300 as unverified.
- inferred: flow profiling relevant parameters are pre-infusion pressure 2-3 bar (4-12 s), peak 8-9 bar, declining profile; supported only by Hedrick/Flair and snippets.

### Gaps
- No source for group head diameter 58 mm (not stated on the Wikipedia article), PID details, or flow profiling definitions.
- Steam boiler pressure (commonly about 1-1.5 bar) not sourced; do not populate.
- No authoritative burr geometry/diameter specs or an espresso micron standard from the SCA or a peer-reviewed measurement.
