# Hario V60 and Pour-Over Brewing: Recipes, Parameters, Troubleshooting, Hardware

Research date: 2026-11-19. Method: web search plus page fetches. Several primary sources were unreachable (jameshoffmann.co.uk returned 404, SCA Standard 310 PDF returned 404, Chemex official page returned 404, Barista Hustle returned HTTP 402, chaindesk and coffeechronicler returned 404). Where a primary source was not read, the value is labeled "secondary" and the gap is listed.

Conventions used below:
- `inferred` = I calculated or deduced it from stated figures.
- `unverified` = only from a snippet, an aggregator, or a source that conflicts with another.
- `n/s` = not stated by the source.
- Field names for dataset conversion: name, author, dose_g, water_g, ratio, temp_c, grind, bloom_g, bloom_s, pours, agitation, total_time_s, tds_pct, ey_pct, source_url. No source in this batch stated TDS % for any named recipe, except Rao's extraction yield. tds_pct is `n/s` everywhere.
- Pours are written as `time_s:cumulative_g`.

---

## 1. Named published recipes (exact parameters)

### Takeaway
Primary or near-primary pages gave full parameters for Hoffmann Ultimate V60, Scott Rao, Kasuya 4:6, Lance Hedrick (via a retailer page), Matt Winton, the 2016-2025 World Brewers Cup winners (via Wikipedia and Sprudge), and Kalita, Origami and Chemex starting recipes. Others are partial. Matt Perger and Hoffmann's 2022 one-cup recipe are only from secondary compilations, and TDS % was almost never published. Third-party pages often disagree on timings, so the conflicts are flagged in each block.

### Cited Findings

#### A. James Hoffmann

**Block A1: Ultimate V60 Technique (30 g version, Hario USA)**
- name: Ultimate V60 Technique (Hario USA transcription)
- author: James Hoffmann
- dose_g: 30
- water_g: 500 (stated as 500 mL, treated as g)
- ratio: 1:16.7 (inferred)
- temp_c: n/s numeric. Text says "the hotter, the better", especially for lighter roasts. Rinse filter with water just off the boil.
- grind: medium-fine (no micron or click value)
- bloom_g: 60 (2x dose)
- bloom_s: 45
- pours: 0:60 (bloom), 45:300 (240 g over 30 s), 75:500 (200 g over 30 s, slower and gentler)
- agitation: swirl during bloom. After the last pour stir once clockwise and once anticlockwise with a spoon. Let it drain a little, then give a gentle swirl.
- total_time_s: 210 (aim for drawdown finished by 3:30)
- tds_pct / ey_pct: n/s
- date: page not dated (only a 2026 footer). Original video publication date not confirmed here.
- source_url: https://www.hario-usa.com/blogs/recipes-and-more-from-friends/james-hoffmann-uitimate-v60-technique

**Block A2: Ultimate V60, 18 g scaled variant (GitHub gist transcription)**
- name: Ultimate V60 (18 g gist version)
- author: James Hoffmann (transcribed by GitHub user fluency03; last active 2023-10-08)
- dose_g: 18
- water_g: 300 (stated as 60 g/L)
- ratio: 1:16.7 (inferred)
- temp_c: n/s numeric ("the hotter, the better")
- grind: medium-fine, Niche Zero setting 40-50
- bloom_g: 45 (page says no more than 3x dose)
- bloom_s: up to 45
- pours: as fetched, 0:45, then to 180 g at 1:15 (60%), then to 300 g at 1:45. unverified: these timings differ from the Hario USA 0:45/1:15 schedule and the fetch summary may have mis-ordered the steps.
- agitation: swirl in bloom, stir once each direction after last pour, gentle swirl before drawdown
- total_time_s: 180 (aim)
- source_url: https://gist.github.com/fluency03/7fb305b8110dde5739d14697af97a99a

**Block A3: A Better 1 Cup V60 Technique (2022)**
- name: A Better 1 Cup V60 Technique
- author: James Hoffmann
- publication date: 2022-11-22 (secondary, from a search-result summary; video not viewed)
- dose_g: 15 (light-medium roast)
- water_g: 250
- ratio: 1:16.7 (inferred)
- temp_c: 100 (aeroprecipe page; other summary says "freshly boiled")
- grind: medium-fine. One summary says "a little finer than you think", especially for light roasts. unverified
- bloom_g: 50
- bloom_s: about 45 total before the next pour (aeroprecipe: swirl at 0:10-0:15, then wait to 0:45)
- pours (aeroprecipe schedule): 0:50 (bloom), 45:100, 70:150, 90:200, 110:250. Each pour is about 10 s with 10 s rests. This is a transcription by a third-party recipe site.
- agitation: gentle swirl at 5 s after bloom and gentle swirl at about 2:00-2:05 after the last pour
- total_time_s: about 180 (aeroprecipe). Another summary gives a target around 2:30. Conflict, so total_time is unverified.
- Other facts from summaries: designed for the plastic 01 V60 (plastic holds heat better). He suggests moving the dripper to the sink before adding water, which slows the drip, and he notes preheating is important. unverified
- source_url: https://aeroprecipe.com/recipes/james-hoffmann-better-1-cup-v60-technique ; summary via search result listing https://chaindesk.ai/tools/youtube-summarizer/a-better-1-cup-v60-technique-1oB1oDrDkHM (page failed on direct fetch)

**Block A4: Other Hoffmann recipes listed on Hario USA**
- Hoffmann Switch + Sibarist: 15 g coffee, 250 ml water, 2:30 brew time. Source: https://www.hario-usa.com/blogs/recipes-and-more-from-friends (listing page; individual recipe page https://www.hario-usa.com/blogs/recipes-and-more-from-friends/james-hoffmann-switch-sibarist not opened).
- The listing also shows a Hoffmann cloth-filter recipe, but it had no numbers on the listing page.

#### B. Scott Rao

**Block B1: Hario ambassador V60 recipe (published 2022-05-10)**
- name: Scott Rao V60 recipe (Hario UK interview)
- author: Scott Rao
- dose_g: 20
- water_g: 330 (stated as 330 mL)
- ratio: 1:16.5 (inferred)
- temp_c: 97
- grind: n/s (grind fresh)
- bloom_g: 60 (3x dose, inferred)
- bloom_s: 40
- pours: 0:60 (bloom), 40:200, then wait until the slurry is about 70% drained, then to 330
- agitation: "bird's nest" dent in the dry bed with a finger. Spin the bloom aggressively right after pouring. Very gentle spin (under 1 s) after pour 1 and after pour 2.
- pour technique: low, steady, near-vertical stream at constant kettle height, moving the kettle around to wet the whole bed
- dripper: plastic V60 (chosen for heat retention)
- total_time_s: 240-270 (4:00-4:30)
- ey_pct: 22-24.5 (stated, depends on grinder, varietal, roast)
- tds_pct: n/s
- source_url: https://www.hario.co.uk/blogs/hario-ambassadors/hario-v60-recipe-interview-with-hario-ambassador-scott-rao
- Note: a "20 g / 320 g / 60 g bloom" recipe appears on other sites, but none of those pages credit Rao. Do not attribute it to him. (Search summary, https://coavacoffee.com/brew-methods/v60 and others.)
- unverified: Rao's book recipes ("The Professional Barista's Handbook", "Everything but Espresso") were not read.

#### C. Tetsu Kasuya 4:6 Method (2016 World Brewers Cup champion)

**Block C1: Hario Europe version**
- name: 4:6 Method
- author: Tetsu Kasuya
- dose_g: 20
- water_g: 300
- ratio: 1:15
- temp_c: 92
- grind: coarse
- dripper: ceramic V60
- bloom_g: 50 (pour 1)
- bloom_s: 45
- pours: 0:50, 45:120, 90:180, 130:240, 160:300 (pour 1-2 = 40%, pours 3-5 = 60%, 60 g each)
- agitation: n/s
- total_time_s: 210 (remove dripper at 3:30)
- source_url: https://hario-europe.com/blogs/hario-community/v60-ambassadors-tetsu-kasuya
- Conflicts: The Wikipedia WBC table lists the 2016 extraction time as 3:00 (https://en.wikipedia.org/wiki/World_Brewers_Cup). A search summary of Kurasu's transcription of the 2016 recipe gives pours at 0:45, 1:30, 2:15, 3:00 with 60 mL each, which differs from Hario Europe's 2:10 and 2:40. Treat per-pour timing as unverified. The Kurasu page itself was not opened (https://kurasu.kyoto/blogs/kurasu-journal/2016-world-brewers-cup-champion-tetsu-kasuya).

**Block C2: Long Short London version (adds grind and water detail)**
- Dose 20 g, water 300 g (1:15), 92 C (page says 92-95 C is fine), water 0.33 ppm / pH 6.6.
- Grind: coarse, one setting coarser than "Paper Filter" on a Ditting grinder.
- Each pour starts only after the previous pour has fully drained. Total 3:30. The page says timings are largely irrelevant once the grind is dialed in.
- Pours: 50 g, 70 g, 60 g, 60 g, 60 g.
- source_url: https://longshortlondon.com/4-6-method-brewers-cup-champ-tetsu-kasuya/

**4:6 taste-tuning rules (as published)**
- First 40% of the water (pours 1-2, 120 g of 300 g) controls the balance of acidity vs sweetness. A larger first pour gives more acidity. A smaller first pour gives more sweetness. Source: https://hario-europe.com/blogs/hario-community/v60-ambassadors-tetsu-kasuya ("more water = more acidity, less water = more sweetness") and https://longshortlondon.com/4-6-method-brewers-cup-champ-tetsu-kasuya/ (more water in first pour = more acidity).
- Last 60% (180 g, pours 3-5) is divided "according to the strength you wish to attain". Long Short London says the remaining 60% can be adjusted within a 1:15 to 1:17 concentration range. Hario Europe gives no specific rule for how many pours to use.
- Other Kasuya recipe on Hario USA: V60 Mugen, 25 g finely ground coffee, 300 ml water, 1:30 brew time. Source: https://www.hario-usa.com/blogs/recipes-and-more-from-friends

#### D. Lance Hedrick

**Block D1: Hedrick V60 masterclass (LAMOSE retailer page, not his own site)**
- name: Pour Over Masterclass V60 Technique
- author: Lance Hedrick (as presented by LAMOSE)
- dose_g: 20
- water_g: 300
- ratio: 1:15
- temp_c: 93-96, by roast (light 95-96, medium 93-94, dark 91-93)
- grind: medium-fine, "similar to granulated sugar"
- dripper: V60 size 02, rinsed with hot water
- bloom_g: 40 (2x dose)
- bloom_s: 45
- pours: 0:40, 45:120, 75:260 (starts once bed shows; largest pour, ends about 2:00), 120:300 (final gentle center pour, to about 2:15)
- agitation: 3-5 gentle stirs in the bloom plus a swirl to settle the bed, gentle swirl after each pour, spiral pours 3-4 inches above the bed. Violent stirring discouraged.
- total_time_s: 165-180 (drawdown target 2:45-3:00; slower than 3:15 means grind coarser, faster than 2:30 means grind finer)
- tds_pct: n/s (page gives water TDS target 75-150 ppm, not brew TDS)
- source_url: https://secure.lamose.com/blogs/recipes/lance-hedricks-pour-over-masterclass-v60-technique
- unverified: Hedrick's own YouTube or site recipe was not read. Retailer pages may paraphrase.

#### E. Matt Perger

**Block E1: Perger V60 (secondary compilation only)**
- name: Matt Perger V60
- author: Matt Perger
- dose_g: unverified. The compilation lists "58" in a g/L column, which would give about 11.6 g for 200 g water (inferred, ambiguous table, do not rely on it).
- water_g: 200
- temp_c: 207 F, which is about 97.2 C (inferred conversion)
- grind: fine
- bloom_g: 50
- bloom_s: n/s (pours at 30 s)
- pours: 0:50, 30:100, 60:200 (swirl the pour and finish along the outside edge to wash the filter)
- agitation: "very thorough stir" in bloom. Lift and tap the brewer after pouring to settle grounds.
- total_time_s: 140 (2:20)
- source_url: https://www.ilcaffeespressoitaliano.com/wp-content/uploads/V-60.pdf ("How to Make Coffee Database - Not Your Parents' Coffee"; page is a PDF compilation, undated). I extracted the table locally with pdftotext. The original Barista Hustle or Perger source and its date were not found.
- Note: Perger is credited with developing the Barista Hustle water recipe (mineral formula), not a V60 spec. Not verified from a primary source.

#### F. Matt Winton (2021 World Brewers Cup champion, Hario five-pour)

**Block F1**
- name: V60 Five-Pour Recipe
- author: Matt Winton
- dose_g: 20
- water_g: 300
- ratio: 1:15
- temp_c: 93 (bloom), 88 (later pours, via two kettles; or a single kettle taken off the base between pours)
- grind: medium
- dripper: Hario Metal V60 size 02, V60 paper filters
- bloom_g: 60; bloom_s: n/s
- pours: five equal 60 g pours (cumulative 60, 120, 180, 240, 300), about 30 s apart or when the bed is nearly dry
- agitation: pour from center outward in concentric circles, from a higher height to agitate
- total_time_s: honestcoffeeguide lists 6 min 50 s. This conflicts with Wikipedia's 2:40 extraction time for his competition run. Treat as unverified.
- tips: if drawdown is too long and cup tastes bitter or dry, grind coarser. If too fast and sour or thin, grind finer.
- source_url: https://honestcoffeeguide.com/brew-recipes/matt-winton-v60-five-pour/ ; competition figures from https://en.wikipedia.org/wiki/World_Brewers_Cup

#### G. Hario "official" recipe
- I did not find a single dated "Hario official" parameter sheet. Hario's own blog hosts ambassador recipes (Hoffmann, Rao, Kasuya, Winton, Tim Wendelboe, Hoffmann + Switch). Tim Wendelboe, Suiren, V60 NEO pages showed no numbers on the listing. Source: https://www.hario-usa.com/blogs/recipes-and-more-from-friends
- Hario Europe publishes a cone-based "sizes" sheet only as product copy (see section 4).
- A Hario V60 "classic ratio" of 1:16 is cited by Perfect Daily Grind (2025-03-03), with no dose, time or temperature: https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/

#### H. Kalita Wave

**Block H1: Ozone Coffee Kalita Wave 155 (single cup)**
- dose_g 15, water_g 250, ratio 1:16.7 (inferred), temp_c 93, grind medium filter, bloom_g 50, bloom_s 30
- pours: 0:50, 30:150 (50 g in circles + 50 g into center), 70:250 (same split)
- total_time_s: 150-180
- source_url: https://ozonecoffee.co.uk/pages/kalita-wave-brew-guide (undated; footer 2026)

**Block H2: Ozone Coffee Kalita Wave 185 (two cups)**
- dose_g 30, water_g 500, ratio 1:16.7 (inferred), temp_c 93, grind medium filter, bloom_g 100, bloom_s 30
- pours: 0:100, 30:300 (100 g circles + 100 g center), 90:500 (same split)
- total_time_s: 210-240
- source_url: https://ozonecoffee.co.uk/pages/kalita-wave-brew-guide

**Other Kalita Wave variants (from a search summary only, unverified):** Third Wave Coffee 15 g / 250 mL at 92 C, medium-fine, 3 min (https://www.th3rdwave.coffee/recipe/UHJvZHVjdFJlY2lwZToyOU9pN0hMdkVGblRueTZXcGJjaHRJalRnNFc=/). Pull & Pour Kalita 185: 16 g, 35 g bloom, 100 g pour at 0:45 (https://pullandpourcoffee.com/wprm_print/7754). Common Man: 15 g, 260 g water, 93 C (https://commonmancoffeeroasters.com/pages/brew-guides-kalita-wave). A page labeled "Kalita Wave Official Recipe" (21 g / 340 g) is on an aggregator (https://field-guides.vercel.app/pour-over/kalita-wave-official-recipe.html) and cannot be attributed to Kalita. I found no recipe published by Kalita itself.

#### I. Chemex (all third-party; official Chemex page was not reachable)
- Cafely: ratio 1:17, 6-cup (30 oz) 55 g coffee and 917 g water (1:16.7, per the page); bloom about 25% of the water (about 230 g, as stated). https://cafely.com/blogs/coffee-brew-guide/chemex
- LAMILL: water 200-205 F (93-96 C). https://cdn.shopify.com/s/files/1/1507/4926/files/LAMILL_Brew_Guide_-_Chemex_Large.pdf
- Crema: start at 1:15; 35 g coffee / 525 g water. https://www.crema.co/workplace/guides/chemex-brewing
- Homegrounds: ratios 1:14 to 1:19 are suggested, about 100 g bloom, 30 s. https://www.homegrounds.co/how-to-use-a-chemex/
- A Beautiful Mess: bloom 80-100 g, 45-60 s. https://abeautifulmess.com/chemex-brewing-101/
- Sample Coffee: 48 g for a 6-cup. https://cdn.samplecoffee.com.au/brewguides/chemex
- These come from search summaries, not page reads. Mark all as secondary. grind: medium-coarse is the common guidance (unverified here).

#### J. Origami (all third-party)
**Block J1: Roasters Pack, light roast (Origami Air S, V60-style cone filter)**
- dose_g 20, water_g 320, ratio 1:16, temp_c 95, grind medium (Comandante 34 clicks, about 1020 microns)
- pours: 0:60, 30:120, 45:180, 60:240, 80:320 (60 g each)
- total_time_s: 120-140
- source_url: https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes

**Block J2: Roasters Pack, medium roast (wave filter)**
- dose_g 20, water_g 320, temp_c 92, grind medium to medium-fine (Comandante 30 clicks, about 900 microns)
- pours: 0:50, 30:100, 55:150, 80:200, 105:250, 125:320
- total_time_s: 160-180
- same source_url

**Other Origami values (search summary only, unverified):** Perfect Daily Grind Origami Air S: 18 g, 1:15, 93 C, medium, 270 g yield (https://perfectdailygrind.com/2024/01/how-to-brew-coffee-with-origami-pour-over/). Kurasu: 15 g / 270 g at 88-90 C (https://kurasu.kyoto/blogs/kurasu-journal/origami-dripper-brewing-recipe-how-we-do-it-at-kurasu). 19grams: 18-23 g at 1:16-1:17, 2:00-3:20 (https://19grams.coffee/en/blogs/kaffee-zubereitung/brewguide-origami-filter).

#### K. Community recipes (The Drumming Barista, Dose and Control; posted 2021-08-18, updated 2023-01-08)
Grind: medium for all. Temp n/s. Source: https://thedrummingbarista.substack.com/p/the-drumming-baristas-top-3-v60-recipes
| name | dose_g | water_g | bloom_g | pours (s:cum g) | agitation | total_time_s |
|---|---|---|---|---|---|---|
| "Lowering the number of coffees" (2023) | 20 | 300 | 75 | 0:75, 40:150, 100:300 | swirl after bloom and after pour 2 if slow | 210-240 |
| "60 X 5" (2023) | 20 | 300 | 60 | 0:60, 40:120, 80:180, 110:240, 150:300 | 5 gentle swirls in bloom | 240 |
| "First coffee of the day" (2021) | 15 | 250 | 40 | 0:40, 40:250 | bloom swirl only | 165-180 |
| Full-bodied 5-pour (2021) | 15 | 250 | 50 | 0:50, 40:100, 70:150, 100:200, 130:250, 160:300 (see note) | bloom swirl only | 210-240 |
| Sweet and acidic 3-pour (2021) | 15 | 250 | 50 | 0:50, 40:150, 90:250 | n/s | 150-165 |
Note for the full-bodied row: the page lists pours of 50 g at 0:40, 1:10, 1:40, 2:10, 2:40 after a 50 g bloom, which sums to 300 g, not 250 g. The page says water is 250 g, so this row is internally inconsistent. unverified.

#### L. World Brewers Cup champions (2016-2025, plus 2026 name only)
Primary table: https://en.wikipedia.org/wiki/World_Brewers_Cup (secondary encyclopedia, itself citing WCE records). Columns in the CSV-ready table below.

| year | author (country) | dripper | grinder | dose_g | water_g | temp_c | pours | total_time | source |
|---|---|---|---|---|---|---|---|---|---|
| 2016 | Tetsu Kasuya (Japan) | Hario V60 ceramic | n/s | 20 | 300 | 92 | 4:6 method | 3:00 (Wikipedia) | https://en.wikipedia.org/wiki/World_Brewers_Cup |
| 2017 | Chad Wang (Taiwan) | Hario V60 ceramic | n/s | 15 | 250 | 92 | n/s | 2:00 | same |
| 2018 | Emi Fukahori (Switzerland) | GINA | n/s | 17 | 220 | 80-95 | hybrid immersion-pourover | 2:55 | same |
| 2019 | Du Jianing (China) | Origami | n/s | 16 | 240 | 94 | n/s | 1:40 | same |
| 2021 | Matt Winton (Switzerland) | Hario V60 metal | Kinu M47 | 20 | 300 | 93 and 88 | 5 pours | 2:40 | same |
| 2022 | Shih Yuan (Sherry) Hsu (Taiwan), Melbourne | Orea V3 with Kalita 185 filter | 1Zpresso K-Pro | 14 (75% at 1000 microns, 25% at 800) | 200 | 70 (1st pour), 95 (rest) | 4 x 50 g every 30 s | n/s | same |
| 2023 | Carlos Medina (Chile), Athens | Origami | 1Zpresso ZP6 Special 5.2 | 15.5 | 250 | 91 | 5 x 50 g every 30 s | n/s (target 2:40 per Roasters Pack) | same; https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes |
| 2024 | Martin Wölfl (Austria), Chicago | Orea v4 fast bottom, Sibarist filter, WDT, Melodrip | Mazzer ZM | 17 (630 microns) | 270 | 93 | bloom 60 ml, 60 ml at 0:40, 50 ml at 1:20, 100 ml at 2:00 | n/s | same |
| 2025 | Peng Jinyang / George Jinyang Peng (China), Jakarta | SOLO dripper + Melodrip | FM Grinder, 11 clicks | 15 (three roasts, 5 g each) | 210 | 96 (first 120 g), 80 (final 90 g) | 30 g at 0:00, 90 g at 0:30, 90 g at 1:10 | 1:45 | see below |
| 2026 | Nas Jaafar (Malaysia), Brussels, June 25-27, 2026 | Hario Switch base with V60 glass server | n/s | n/s | n/s | n/s | n/s | n/s | https://www.hario-europe.com/blogs/hario-community/2026-world-brewers-cup-championship |

2025 detail (Peng):
- Sprudge (2025-05-20): 15 g, 210 ml total (120 ml at 205 F, 90 ml at 176 F), pre-wet 80 ml at 205 F, mineral water 40 ppm TDS, 11 clicks on FM grinder, bloom 30 ml in about 6 s (three counter-clockwise circles), 90 ml at 0:30 over 10 s, 90 ml at 1:10 through a Melodrip, drawdown about 1:45. Natural Panama Gesha (Mount Totumas), roasted in three profiles. Source: https://sprudge.com/how-to-brew-coffee-like-the-2025-world-brewers-cup-champion-338576.html
- Slow Pour Supply: same pours, first two pours stated as 96 C (210 F) and the last at 80 C (176 F), cool to 65 C then serve at 50 C. Roast profiles at 185, 187, 189 F. Source: https://www.slowpoursupply.co/blogs/journal/2025-world-brewers-cup-champion-george-pengs-solo-dripper-recipe
- Temperature conflict: Sprudge says 205 (units not stated, 205 F is 96 C), Slow Pour says 210 F and 96 C (96 C is 205 F, so "210 F" is likely a typo, inferred). Honest Coffee Guide notes the same 205 vs 210 F discrepancy and lists a 2:15 time, which conflicts with 1:45 (https://honestcoffeeguide.com/brew-recipes/george-jinyang-peng-2025-wbc/).
- Ratio about 1:14 (inferred, 210/15).
- 2023 Medina (Roasters Pack): 15.5 g, 250 ml at 91 C, rebuilt water with equal calcium and magnesium at 65 ppm TDS, Comandante 28 clicks (about 840 microns), Origami Air S with V60-style cone filter, five 50 g pours at 0:00, 0:30, 1:00, 1:30, 2:00. https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes
- 2019 Du (Roasters Pack): 16 g ground twice, 240 ml at 94 C, water 4 ppm Ca and 15 ppm Mg (80 ppm TDS), Comandante 26 clicks (about 780 microns), pours 60 g at 0:00 (6 g/s, 10 s), 80 g at 0:18 (4 g/s, 20 s), 100 g at 0:56 (5 g/s), drip-through 1:40-1:50, yield about 190 ml. Same source.
- 2022 Hsu: The Wikipedia recipe line lists the grind distribution in microns. Dalla Corte confirms the title and the Melbourne event, with Elika Liftee second and Elysia Tan third (https://www.dallacorte.com/magazine-taiwan-s-shih-yuan-hsu-wins-the-world-brewers-cup-n-844.html). I found no 2022 or 2024 Sprudge-style recipe write-up.
- Note: the 2020 event was not held (the Wikipedia table has no 2020 row).

### Inferences
- Ratios cluster at 1:14 (2025 WBC) to 1:16.7 (Hoffmann, Kalita, Drumming Barista). Competition recipes run tighter (1:12 to 1:16 by the table: 2022 is 1:14.3, 2023 is 1:16.1, 2024 is 1:15.9, 2025 is 1:14).
- Competition drawdowns are short (1:40 to 2:40) compared with everyday recipes (2:30 to 4:30).
- The trend in recent WBC winners is multi-temperature pours (2021 93/88 C, 2022 70/95 C, 2025 96/80 C).

### Gaps
- No TDS % or extraction yield published for any recipe except Rao's 22-24.5% EY.
- Hoffmann's own site (jameshoffmann.co.uk) and the original 2022 video were not accessible; the 2022 recipe is from third-party transcription and the two summaries conflict on bloom wait and total time.
- No published grind in microns or grinder clicks for Hoffmann, Rao or Hedrick, except the Niche Zero 40-50 setting on the gist and Hedrick's "granulated sugar" description.
- Matt Perger dose and original source not confirmed.
- No official Chemex, Kalita or Origami manufacturer recipe was found.
- 2026 champion recipe (Nas Jaafar) not found.
- 2022, 2023 and 2024 winners' full pour timings and TDS were not found beyond the Wikipedia lines.

---

## 2. General target ranges (ratio, TDS, EY, SCA, Brew Control Chart, temperature, bloom)

### Takeaway
The classic "ideal" zone is TDS 1.15-1.35% and extraction yield 18-22% (Lockhart's 1957 Brew Control Chart, adopted by SCA). SCA Standard 310 (home brewers) is reported at a wider 1.15-1.55% TDS with 55 g/L, 90-96 C. The published recipes in section 1 use ratios 1:14 to 1:17, bloom 2-3.75x dose for 30-45 s, and water 91-97 C.

### Cited Findings
- Brew Control Chart: created by Ernest E. Lockhart of the Coffee Brewing Institute, released 1957. Plots extraction yield (x-axis) vs TDS (y-axis) with diagonals for brew ratio. The "ideal" central zone is TDS 1.15-1.35% and extraction 18-22%. Left side is "under-developed" (sour, grassy), right side "bitter", high TDS "strong", low TDS "weak". — [SCA, Towards a New Brewing Chart](https://www.sca.coffee/sca-news/25/issue-13/towards-a-new-brewing-chart) (listed in search results; the page itself returned 404 on direct fetch, so the figures here come from the search summary); [Freshcup summary](https://freshcup.com/why-the-new-coffee-brewing-control-chart-is-a-big-deal/)
- SCA notes the terms strong, bitter, weak, over- and under-developed are outdated and not standardized. A 2024 "Sensory Brewing Control Chart" update has fewer descriptors but keeps the "ideal" zone. — [SCA](https://www.sca.coffee/sca-news/25/issue-13/towards-a-new-brewing-chart) (search summary)
- SCA Standard 310-2021 (home brewers) is reported to set brew strength 1.15-1.55% TDS at the standard ratio, 55 g coffee per 1.000 kg water, and brewing temperature 90-96 C. These came from a search summary, because the PDF itself returned 404. — [SCA Standard 310 2021](https://sca.coffee/s/SCA_Standard_310-2021.pdf), unverified directly
- BUNN CoffeeBasics gives the Golden Cup range as 1.15-1.35% TDS (and 18-22% extraction). The Batali et al. paper quoting the SCA handbook gives 92-96 C. — [BUNN brochure](https://resource.bunn.com/assets/web/pdfs/BUNN-CoffeeBasics_Brochure_web.pdf); conflicts with the SCA 1.15-1.55% reading above. I found no source for "90.5 C".
- Classic ratio for V60: 1:16 (Perfect Daily Grind, 2025-03-03). — [PDG](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/)
- Ratios in the recipes above: 1:15 (Hedrick, Kasuya, Winton, Roasters Pack ~1:16), 1:16.5 (Rao), 1:16.7 (Hoffmann), 1:14 (2025 WBC). Kasuya's 4:6 strength rule allows 1:15 to 1:17. — see section 1 URLs
- Water temperature by roast level (Hedrick): light 95-96 C, medium 93-94 C, dark 91-93 C. — [LAMOSE](https://secure.lamose.com/blogs/recipes/lance-hedricks-pour-over-masterclass-v60-technique)
- Generic troubleshooting source gives 195-205 F (90-96 C), with cooler for dark roasts and hotter for light. — [Field guide aggregator](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html) (weak source, secondary)
- Plastic V60 should be brewed cooler than ceramic or metal (PDG), while Rao and Hoffmann use plastic for heat retention. — [PDG](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/); [Hario UK / Rao](https://www.hario.co.uk/blogs/hario-ambassadors/hario-v60-recipe-interview-with-hario-ambassador-scott-rao)
- Bloom: Hoffmann Ultimate uses 2x dose (Hario USA) and says "no more than 3x" (gist). Rao 3x (60 g / 20 g). Hedrick 2x (40 g / 20 g). Winton 3x (60 g / 20 g). Drumming Barista recipes 2.7x-3.75x. Bloom time 30-45 s in Hoffmann, Rao (40 s), Hedrick (45 s), Kasuya (45 s), Ozone Kalita (30 s). WBC winners often skip a long bloom (2025: 30 g at 15 g dose = 2x, then 30 s wait). — URLs in section 1
- Brew water for Hedrick: water TDS 75-150 ppm. 2023 Medina used 65 ppm TDS water, 2019 Du used 80 ppm, 2025 Peng 40 ppm. Long Short London lists Kasuya's water as 0.33 ppm and pH 6.6 (as stated, the number looks like it may be mis-transcribed). — [LAMOSE](https://secure.lamose.com/blogs/recipes/lance-hedricks-pour-over-masterclass-v60-technique); [Roasters Pack](https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes); [Sprudge](https://sprudge.com/how-to-brew-coffee-like-the-2025-world-brewers-cup-champion-338576.html); [Long Short London](https://longshortlondon.com/4-6-method-brewers-cup-champ-tetsu-kasuya/)

### Inferences
- Rao's published EY target (22-24.5%) sits above the 18-22% "ideal" zone. This shows modern specialty practice deliberately exceeds the Lockhart zone. Hedrick has a Brew Control Chart episode (2024), which I did not read.
- Recommended expert-tool defaults (inferred from the above): ratio 1:15-1:17, 92-96 C for light roasts, 91-93 C for dark, bloom 2-3x dose for 30-45 s, drawdown 2:30-3:30 for 1 cup.

### Gaps
- SCA Standard 310 PDF and the SCA chart article could not be opened; exact SCA wording for strength and ratio is unverified. The TDS upper bound varies by source (1.35 / 1.45 / 1.55).
- SCA Golden Cup total-dissolved-solids vs "55 g/L" range for pour-over were not verified directly.
- No source stated typical TDS % for V60 recipes (commonly about 1.3-1.5% from experience, but I did not find a citation, so it is not given).
- Barista Hustle articles (402) and Scott Rao's books were not read.

---

## 3. How variables shift flavor and troubleshooting rules

### Takeaway
Sources agree on the direction of each lever: finer grind, hotter water, longer contact and more agitation raise extraction, while the opposite lowers it. "Sour/thin" is the under-extracted pole and "bitter/astringent" the over-extracted pole. A cup that is both sour and bitter points to uneven extraction (channeling), and the fix is the pour or bed rather than a grind change. Most of this material comes from blogs and vendor guides, not controlled studies.

### Cited Findings
- Core rule: sour usually means under-extracted, bitter usually means over-extracted. — [Troubleshooting guide (aggregator)](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html); [Simon & Bearns](https://simonandbearns.coffee/en/blogs/kaffeeblog/filter-coffee-too-bitter-or-too-sour-causes-diagnosis-and-solutions)
- Sour, sharp, lemony: grind finer, raise water temperature, slow the pour, increase contact time. — [Troubleshooting guide](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html)
- Bitter, harsh: grind coarser, lower temperature, shorten contact time, reduce agitation. Astringent or drying: over-extraction or excess fines; grind coarser, reduce agitation, check for stalled drawdown. — same source
- Weak/watery: tighter ratio (less water per gram) or slightly finer grind. Too intense/muddy: more water per gram. — same source
- Sour and bitter together: uneven extraction from channeling; even the bed, pour gently, level grounds. If going finer makes the cup more sour, the bed is probably channeling. — same source; [search-result synthesis](https://baristalife.co/blogs/blog/pour-over-uneven-extraction)
- Drawdown too fast: grind too coarse or bypass; grind finer, pour in the center rather than down the walls. Drawdown slow/stalled: grind too fine, too many fines, or a clogged filter; grind coarser, reduce agitation, pre-wet the filter. Water pooling: bed clogged by fines. Large crater in bed: pour too aggressive or off-center. — [Troubleshooting guide](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html)
- Winton: drawdown too long with bitter or dry cup means grind coarser; too fast with sour or thin cup means grind finer. — [Honest Coffee Guide](https://honestcoffeeguide.com/brew-recipes/matt-winton-v60-five-pour/)
- Hedrick: drawdown slower than 3:15 means grind coarser, faster than 2:30 means grind finer (for his 20 g / 300 g recipe). — [LAMOSE](https://secure.lamose.com/blogs/recipes/lance-hedricks-pour-over-masterclass-v60-technique)
- Kasuya 4:6: more water in pour 1 gives more acidity, less gives more sweetness; last 60% sets strength. — [Hario Europe](https://hario-europe.com/blogs/hario-community/v60-ambassadors-tetsu-kasuya). A coarse grind can make the coffee taste weak with a standard V60 flow rate; Kasuya's signature V60 has no spiral at the bottom, which slows flow. — [search summary of Hario Europe](https://hario-europe.com/blogs/hario-community/v60-ambassadors-tetsu-kasuya)
- Pour technique: avoid pouring directly onto the filter edges (channeling); don't let the bed dry fully between pulse pours; swirl or tap to settle the bed before drawdown. — [PDG](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/); [Troubleshooting guide](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html)
- If water pulls through too quickly, gently swirl to add agitation; increase or reduce agitation to raise or lower extraction. — [PDG](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/)
- Rao's swirl: very gentle spin after pours fills the rib channels and levels the bed; aggressive spin in the bloom. — [Hario UK / Rao](https://www.hario.co.uk/blogs/hario-ambassadors/hario-v60-recipe-interview-with-hario-ambassador-scott-rao)
- Hoffmann: stir once each direction after the last pour to knock grounds off the wall, then a gentle swirl to flatten the bed. — [Hario USA](https://www.hario-usa.com/blogs/recipes-and-more-from-friends/james-hoffmann-uitimate-v60-technique)
- Bloom: huge foamy bloom that overflows means very fresh, gassy coffee, so use more bloom water and a longer bloom. Little or no bloom means stale coffee. — [Troubleshooting guide](https://field-guides.vercel.app/pour-over/pour-over-troubleshooting-guide.html)
- Filter: unrinsed paper adds papery or cardboard flavor. PDG recommends rinsing with room-temperature water to keep the starting temperature consistent; Hoffmann and Hario recipes use water just off the boil. Metal V60 has less pronounced ridges so the paper can sink into the gaps. — [PDG](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/); [Hario USA](https://www.hario-usa.com/blogs/recipes-and-more-from-friends/james-hoffmann-uitimate-v60-technique)
- Draw-down time vs recipe style: pulse recipes with fewer, larger pours (Drumming Barista "sweet and acidic" 3-pour) are labeled sweet and acidic, with 2:30-2:45; the 5-pour is labeled full-bodied at 3:30-4:00. — [Drumming Barista](https://thedrummingbarista.substack.com/p/the-drumming-baristas-top-3-v60-recipes) (the author's own flavor labels, no sensory data)
- Dark roasts extract more easily and turn bitter faster with high temperature or fine grind. — [search summary of troubleshooting guides](https://baristalife.co/blogs/blog/coffee-tastes-sour-adjustment)

### Inferences
- A minimal dataset of rules: (grind finer) -> +extraction, +drawdown time; (temp up) -> +extraction; (agitation up) -> +extraction, more fines migration, slower drawdown; (ratio tighter) -> +strength (TDS) with unchanged or lower EY; (more first-pour water in 4:6) -> +acidity.
- Conflict handling: one guide's table reverses the grind direction (bitter = finer), which contradicts every other source here and should be ignored (reported in a search summary, source not identified).

### Gaps
- No controlled-sensory source (e.g., Barista Hustle, SCA, or a peer-reviewed study) was read for effect sizes. The numeric effect of 1 C, one click, or a given agitation on TDS/EY is not stated by any source I opened.
- Filter paper brand comparisons (Hario vs Sibarist vs Cafec) and pour-rate (g/s) effects were not researched, apart from Du's 2019 pour rates of 4-6 g/s noted above.

---

## 4. V60 hardware facts

### Takeaway
All V60 sizes share a 60-degree cone, a single large outlet and spiral ribs. Sizes 01, 02 and 03 differ in capacity and dose range, and each needs its own size paper filter.

### Cited Findings
- Cone-shaped body with 60 degree walls; spiral ribs create air pockets so the filter does not stick to the walls; one outlet at the bottom; available in plastic, glass, ceramic and metal with different thermal conductivity, rib depth and cone dimensions. — [Perfect Daily Grind, 2025-03-03](https://perfectdailygrind.com/2025/03/v60-coffee-revisited-brew-guide/)
- Hario founded 1921; began coffee equipment in the 1940s; the ceramic V60 arrived in 2004. — same source
- Size table (from a retailer-style comparison; not Hario's official sheet): — [thecoffeekits comparison](https://thecoffeekits.pages.dev/hario-v60-size-comparison-which-size-makes-the-best-cup-of-coffee-5ONV)

| size | stated capacity (cups) | practical water range | dose range (g, at 1:15-1:17) | filter | dimensions W x D x H mm |
|---|---|---|---|---|---|
| 01 | 1-2 | 150-360 ml | 12-24 | 01 | 119 x 100 x 82 |
| 02 | 1-4 | 300-700 ml | 18-42 | 02 | 137 x 116 x 102 |
| 03 | 1-6 | 450-1000 ml | 30-60 | 03 | 157 x 137 x 122 |

- Other retailers give narrower dose ranges: 12-20 g for the 01 and 18-40 g for the 02. — [EspressoParts](https://www.espressoparts.com/products/hario-v60-02-pour-over-coffee-starter) (search summary)
- Hario Europe capacity labels (1-2, 1-4, 1-6 cups) — [Hario Europe glass dripper](https://www.hario-europe.com/products/hario-v60-dripper-glass) (from search summary; direct fetch returned HTTP 429)
- Filters are not interchangeable between sizes. — [Seattle Coffee Gear guide](https://www.seattlecoffeegear.com/pages/product-resources/hario-coffee-dripper-v60-clear-product-guide) (search summary)
- Recipe doses by size in this note: size 01 used for Hoffmann's 15 g / 250 g; size 02 for Hedrick's 20 g / 300 g, Winton's 20 g / 300 g (metal 02); Hoffmann's Ultimate 30 g / 500 g sits at the top of 02 range.
- Origami sizes: S is equivalent to V60 01 and M to V60 02. Origami Air S is a resin version, about half the weight of ceramic, only in S. Origami takes Kalita 155 and 185 wave filters (155 in S) and V60-style cone filters. — [Roasters Pack](https://theroasterspack.com/blogs/news/origami-dripper-our-extensive-guide-with-recipes); search summary of retailer pages
- Kalita Wave: 155 for about one cup (Ozone recipe 15 g / 250 g) and 185 for about two cups (30 g / 500 g). — [Ozone](https://ozonecoffee.co.uk/pages/kalita-wave-brew-guide)
- Plastic V60 retains heat better than ceramic or glass (Hoffmann's one-cup video and Rao's recipe choose plastic). — [Hario UK / Rao](https://www.hario.co.uk/blogs/hario-ambassadors/hario-v60-recipe-interview-with-hario-ambassador-scott-rao); [aeroprecipe](https://aeroprecipe.com/recipes/james-hoffmann-better-1-cup-v60-technique)

### Inferences
- Dose ceiling per size should be treated as a soft range in the tool: 01 about 12-20 g (15 g typical), 02 about 18-40 g (20 g typical), 03 about 30-60 g.

### Gaps
- No official Hario spec sheet was read (Hario Europe returned 429, Hario Global catalogue not opened). Dimensions and dose ranges are from a retailer comparison.
- Rib height and filter dimensions by size were not found. Dripper hole diameter not found.
- Other brands (Orea, Sibarist filters, SOLO, Melodrip) appear only as WBC equipment; no hardware spec was gathered.
