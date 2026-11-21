# Coffee Origins in Asia and the Pacific: Regions, Altitudes, Processing, Harvest, Flavor Profiles

Research date: 2026-11-19. Latest USDA FAS world circular available: July 2026 (next release 16 Dec 2026). Production years: USDA 2025/26 (estimate) and 2026/27 (forecast). Marketing years differ: Vietnam Oct-Sep, Indonesia Apr-Mar, India Oct-Sep.

Conventions used in this file:
- Field names for the dataset: country, region, altitude_min_masl, altitude_max_masl, varieties, processing, harvest_months, grade_system, flavor_notes, acidity, body, sweetness, production_60kg_bags, production_year, source_url.
- Many regional altitude, processing and flavor claims come from seller or blog pages (importers, roasters, aggregators), not primary agencies. Sellers disagree with each other; ranges below are listed per source, not reconciled. Treat them as "indicative" unless marked otherwise.
- Several search-result summaries could not be tied to a single page. Where a claim came from a group of search results, the link points to the most relevant page in that group. Confidence for these is low-to-medium; re-verify against lot sheets before production use.
- acidity / body / sweetness (1-10): NO source in this research gave numeric 1-10 ratings. All numeric ratings in the dataset rows are INFERRED by me from the cited descriptor words and are marked `inferred`. Do not present them as source ratings.

---

## 1. Annual production (60 kg bags), arabica vs robusta, and world rank

### Takeaway
USDA FAS (July 2026) shows Vietnam firmly #2 in the world (31.7M bags in 2025/26, record 32.5M forecast for 2026/27, about 96% robusta). Indonesia was #4 in 2025/26 (12.37M) but is forecast to fall to #5 in 2026/27 (11.38M), behind Ethiopia (12.1M). India is #7 (6.43M in 2025/26), and about 75% robusta.

### Cited Findings
- USDA FAS "Coffee: World Markets and Trade", July 2026, is the latest edition; the next release is 16 Dec 2026. World production is 178.8M bags in 2025/26 and a record 189.7M forecast for 2026/27. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)
- Vietnam total: 31,700 (k bags) in 2025/26 (raised 900k on higher yields); 32,500 forecast 2026/27 (record, on expanding area and higher yields). Vietnam arabica 1,200 / robusta 30,500 in 2025/26; arabica 1,100 / robusta 31,400 in 2026/27. Vietnam domestic consumption forecast at a record 5.0M bags; bean exports forecast 25.4M. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf) (table values read from PDF text extraction; column order verified by arabica+robusta=total checks)
- Vietnam earlier USDA country-report figure: 31M bags forecast for 2025/26 (about 30M robusta, about 1M arabica), harvested area 620,000 ha; Central Highlands = 92% of area and 90% of output; marketing year Oct-Sep. — [Daily Coffee News on USDA Vietnam report (Jun 2025)](https://dailycoffeenews.com/2025/06/05/vietnam-coffee-report-production-exports-and-consumption-all-rising)
- Indonesia total: 12,370 in 2025/26 (arabica 1,370 / robusta 11,000); 11,380 forecast 2026/27 (arabica 1,380 / robusta 10,000). USDA says robusta output falls 1.0M on lower yields because excessive rainfall disrupted flowering and cherry formation in the lowland areas of Southern Sumatra and Java, "where approximately 75 percent is grown"; bean exports forecast down over 800k to 7.0M. Indonesia's marketing year starts in April. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)
- 2025/26 ranking from the same table: Brazil 63.0M, Vietnam 31.7M, Colombia 12.5M, Indonesia 12.37M, Ethiopia 11.56M, Uganda 7.10M, India 6.43M. 2026/27 forecast: Brazil 71.9M, Vietnam 32.5M, Colombia 13.4M, Ethiopia 12.1M, Indonesia 11.38M, Uganda 7.16M, India 6.14M. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)
- India: 6,430 (2025/26: arabica 1,730 / robusta 4,700) and 6,140 forecast 2026/27 (arabica 1,560 / robusta 4,580). The USDA India annual report (via Daily Coffee News, May 2026) gives the same 6.14M total (down 4.5% from 6.43M), arabica yield 452 kg/ha (-8%), robusta yield 1,239 kg/ha (-2%), exports 6.22M bags (3.68M green + 2.53M soluble), domestic consumption about 1.58M bags. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf); [Daily Coffee News, May 2026](https://dailycoffeenews.com/2026/05/20/india-coffee-report-soluble-coffee-drives-exports-but-arabica-declining/)
- Other Asia-Pacific producers in the USDA table (total, k bags, 2025/26 -> 2026/27F): China 1,900 -> 1,900 (all arabica); Thailand 900 -> 900 (all robusta); Papua New Guinea 800 -> 800; Laos 475 -> 500; Philippines 450 -> 475; Malaysia 1,500 -> 1,500 (listed as robusta). — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)
- Hawaii: a USDA-sourced figure quoted second-hand says about 6,900 acres were in coffee statewide in Jan 2021. Ka'u area about 830 acres with 80-90 farms (undated Hawaii Dept of Agriculture / Hawaii Coffee Association booklet). — [Hawaii Coffee Association booklet](https://hca.wildapricot.org/resources/Documents/DOA-HICoffeeAssoc-Booklet.v4_print.pdf)
- PNG production by province (about 90% from five highland provinces): Western Highlands 45%, Eastern Highlands 37%, Simbu 6%, Morobe 5%, East Sepik 5%. — [Devpolicy / IFPRI-CGIAR piece on PNG highlands](https://devpolicy.org/?p=83987)

### Inferences
- Rank for the tool: "Vietnam #2 (stable); Indonesia #4 in 2025/26, forecast #5 in 2026/27" is safer than a fixed "#4".
- Vietnam arabica share about 3.8% (1,200/31,700) in 2025/26; Indonesia arabica share about 11% (1,370/12,370); India arabica about 27% (1,730/6,430). These are computed from the USDA table.
- No separate USDA lines exist for Myanmar, Timor-Leste, Nepal, Sri Lanka, Taiwan, Japan, Australia, or Pacific islands in the table I read (they fall under "Other" or are absent), so their production_60kg_bags should be left null or sourced from ICO.
- Malaysia's 1.5M bags looks very high compared with what national sources would imply for a small liberica/robusta sector. Treat it as an unverified USDA PSD series (possibly processing/trade-linked); do not feature it.

### Gaps
- Per-country ICO (ICO Coffee Development Report / country statistics) figures were not retrieved; ICO pages were not reached within the research budget.
- Production figures for Myanmar, Timor-Leste, Nepal, Sri Lanka, Taiwan, Okinawa, Australia, Vanuatu, Fiji, Samoa: not found in a citable source.
- A search snippet attributed a "3.7M bags" India figure to a USDA world report; this contradicts the July 2026 PDF table (6.43M) and the India country report (6.43M). I did not reproduce the 3.7M figure; its origin is unverified.

---

## 2. Indonesia (Sumatra, Java, Sulawesi, Flores, Bali, Papua; giling basah; Lampung robusta)

### Takeaway
Indonesian arabica is a small share (about 11%) of the crop; about 75% of production is lowland robusta in Southern Sumatra (Lampung) and Java. Specialty arabica regions run roughly 1,100-1,900 masl, with wet-hulled (giling basah) lots giving heavy-body, low-acid, earthy/herbal cups, and washed or honey lots (Gayo washed, Kintamani, Ijen) cleaner and brighter.

### Cited Findings
- Giling basah (wet-hulling): smallholders or collectors remove the parchment while the bean is still wet, often 30-50% moisture, vs 10-12% for conventional dry-hulling. — [Specialty Coffee Indonesia (Sumatra guide)](https://specialtycoffee.id/?p=5372); [Giling basah explainer (mirror site, lower confidence)](https://coffee-e4d.pages.dev/indonesia/giling-basah)
- Sumatra wet-hulled coffees are described as heavy-bodied and low-acid; one source calls Gayo, Mandheling and Lintong "heavy-bodied and savory". — [Specialty Coffee Indonesia](https://specialtycoffee.id/?p=13553)
- Mandheling: one source gives 1,100-1,500 masl (cocoa, tobacco, forest spice, very full body); another 1,200-1,600 m (dark chocolate, earthy, molasses). "Mandheling" is a loose trade term, often used for any wet-hulled Sumatran coffee, including Aceh. — [Specialty Coffee Indonesia: Mandheling](https://specialtycoffee.id/articles/mandheling-coffee/); [Specialty Coffee Indonesia: Lintong vs Mandheling](https://specialtycoffee.id/?p=13553)
- Lintong (North Sumatra, Lake Toba area): altitude 1,400-1,600 masl per one source and 1,500-1,800 masl per another (conflict); notes plum, kumquat, molasses, syrupy body; cleaner than most Sumatrans because of higher altitude and cooler air. An importer lists "Sumatra Lintong G1 TP" (Grade 1, Triple Pick). — [Specialty Coffee Indonesia: Lintong vs Mandheling](https://specialtycoffee.id/?p=13553); [Inter-American Coffee, Lintong G1 TP](https://interamericancoffee.com/?p=334)
- Gayo (Aceh): one seller gives 1,400-1,800+ m with cedar and citrus lift; another lists dark chocolate, cedar, brown sugar, herbal. Wet-hulled, though some lots are fully washed. — [Artizan Coffee: Sumatra Mandheling Gayo](https://artizancoffee.com/blogs/arrivals/sumatra-mandheling-gayo); [Specialty Coffee Indonesia](https://specialtycoffee.id/?p=5372)
- Toraja (Sulawesi, Tana Toraja): 1,400-1,900 m, heavier body, lower acidity, dark fruit and chocolate; wet-hulled. Kalosi (Enrekang): 1,200-1,800 m, slightly brighter acidity, more floral, spice-forward; one guide says dry-hulled. The two are often sold under a combined "Toraja Kalosi" label. — [Specialty Coffee Indonesia: Kalosi vs Toraja](https://specialtycoffee.id/articles/sulawesi-kalosi-coffee/) (attribution at result-group level)
- Flores Bajawa (Ngada plateau): about 1,200-1,800 m (one source says from 1,000 m), volcanic ash soil, usually under shade; nutty, caramel, chocolate, medium body. — [FNB.tech Indonesian coffee origins](https://fnb.tech/indonesian-coffee-origins/) (attribution at result-group level)
- Bali Kintamani: about 1,200-1,700 m; washed, natural and honey processing; citrus, molasses, bright acidity; coffee intercropped with citrus, chilies and potatoes. — [FNB.tech Indonesian coffee origins](https://fnb.tech/indonesian-coffee-origins/) (attribution at result-group level)
- Java (Ijen Plateau): estimates range from about 900 to 1,500 m; estates are largely washed; descriptors range from chocolatey/nutty/bright to "dark chocolate, cinnamon, sage, cedar; creamy body". — [Sucafina on Indonesia](https://sucafina.com/na/news/about-indonesia) (attribution at result-group level)
- Lowland robusta in Southern Sumatra (Lampung) and Java makes up about 75% of Indonesian output per USDA. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf)
- Cup of Excellence Indonesia: first held 2021 (announced Jan 2022 with 26 CoE winners and 6 National Winners per one report); 2022 top lot 90.59 (Bahagia Ginting, Aceh), 2nd 89.85 (PT Biji Kopi Internusa, Aceh), 3rd 89.59 (Yasmin Nabila Salsabila, West Java); 2023 4th place 90.06. — [Alliance for Coffee Excellence: Indonesia 2022](https://allianceforcoffeeexcellence.org/indonesia-2022/); [GCR: inaugural Indonesia CoE](https://www.gcrmag.com/inaugural-indonesia-cup-of-excellence-prepares-for-auction)
- Kopi luwak context: at World of Coffee Jakarta, exhibitors presented "luwak-style" coffee made without civets, using microbes isolated from civet feces to ferment beans. This is the only luwak-related item found; it does not cover animal-welfare controversy. — [Barista Magazine](https://www.baristamagazine.com/highlights-from-world-of-coffee-jakarta/)

### Inferences
- Because the sellers disagree by 100-200 m, store altitude as the union range per region with `altitude_source_conflict=true`, or use the narrower overlap: Mandheling 1,200-1,500; Lintong 1,500-1,600; Gayo 1,400-1,600 (the lower end is my guess; the source says 1,400-1,800+).
- "Mandheling" and "Lintong" are better modeled as trade names (Lintong is an area; Mandheling is a loose brand name), with a flag.
- Typical wet-hulled Sumatra descriptors for the tool: earthy, herbal, cedar, tobacco, dark chocolate, heavy body, low acidity; this matches the task brief and the cited sellers.

### Gaps
- Varieties by region (Typica, Catimor/Ateng/Tim-Tim, Andungsari, Sigarar Utang, Timor Hybrid): no citable source retrieved in this pass. These are known Indonesian cultivars from the task brief, but I cannot attach sources.
- Harvest months for Indonesian regions (Sumatra main harvest, Toraja, Java, Flores, Kintamani): not found. USDA notes only that the Indonesian marketing year starts in April.
- Grading: SNI/"Grade 1 G1", "Triple Pick" appear only as importer labels; no standard document retrieved. Papua (Baliem Valley) and Aceh Sidikalang specifics not retrieved.
- Rainfall/temperature data: none found.

---

## 3. Vietnam (Central Highlands robusta; Da Lat arabica; screen 16/18)

### Takeaway
Vietnam produces about 96% robusta, concentrated in the Central Highlands (Dak Lak, Dak Nong, Lam Dong, Gia Lai), with harvest October-January. Robusta Grade 1 is sold as Screen 16 or Screen 18 under TCVN 4193:2014. Arabica is mainly Catimor around Da Lat (Lam Dong), harvested roughly November-January.

### Cited Findings
- Central Highlands = 92% of coffee area and 90% of output; harvested area 620,000 ha. — [Daily Coffee News on USDA Vietnam report](https://dailycoffeenews.com/2025/06/05/vietnam-coffee-report-production-exports-and-consumption-all-rising)
- Altitude and harvest (one exporter guide): Dak Lak 400-800 m; Dak Nong 600-1,000 m; Lam Dong 900-1,500 m; Dak Lak/Dak Nong harvest Oct-Jan, Lam Dong Nov-Mar. A second exporter page gives Dak Lak a Nov-Mar harvest (contradiction). An academic paper on the Central Highlands says harvest runs Oct-Jan. — [Greentech Vietnam coffee origins guide](https://greentech-drl.pages.dev/guides/vietnam-coffee-origins); [Vietnam Journal of Science, Technology and Engineering paper](https://vietnamscience.vjst.vn/index.php/vjste/article/download/269/255/1044)
- Grade/screen: Robusta Grade 1 is sold in Screen 16 and Screen 18 under TCVN 4193:2014; Screen 18 = beans retained on a 7.14 mm round-hole screen, and Grade 1 Screen 18 requires at least 90% retention. — [Greentech Vietnam robusta](https://greentech-drl.pages.dev/vietnam-robusta-coffee) (attribution at result-group level)
- Arabica: Catimor is the main type (with some Typica and Bourbon); Da Lat arabica about 1,000-1,500 m (Cau Dat farm about 1,200 m); harvest Nov-Jan in the Central Highlands (Oct-Jan in the north); Catimor sold in S16/S18 grades from Lam Dong. — [Helena Coffee: Arabica Catimor Fully Washed S18](https://www.helenacoffee.vn/product/arabica-catimor-fully-washed-s18/)
- Vietnamese Q Robusta lots scored 86.00 and 85.50 in one listing; a Q grader said Vietnam is improving its processing and "we have seen very good results in the cup". — [Atlas Coffee interview with Q Robusta instructors](https://www.atlascoffee.com/?p=6751); [Helena Coffee](https://www.helenacoffee.vn/?p=26023)

### Inferences
- Use harvest_months = Oct-Jan for Dak Lak/Dak Nong, Nov-Mar for Lam Dong, with a note that sources conflict for Dak Lak.
- The task brief's typical Vietnam robusta cup (bold, nutty, rubbery, high caffeine) was not directly confirmed by a source in this pass; treat as "brief-provided, unverified here".

### Gaps
- Annual rainfall/temperature for the Central Highlands: not retrieved (Frontiers paper on weather impact on robusta yield exists but was not read).
- VICOFA primary data and washed/honey/natural robusta share: not retrieved.

---

## 4. India (Karnataka, Kerala, Tamil Nadu; Monsooned Malabar; Mysore Nuggets)

### Takeaway
India produced 6.43M bags in 2025/26 (about 73% robusta). The Coffee Board lists Mysore Nuggets Extra Bold as washed arabica from Chikmagalur, Coorg, Biligiris, Bababudangiris and Shevaroys, and Monsooned Malabar AA as a dry-processed monsoon-exposed coffee used in blends. Seller altitude data runs roughly 950-1,550 m.

### Cited Findings
- Coffee Board: Mysore Nuggets Extra Bold = washed arabicas from Chikmagalur, Coorg, Biligiris, Bababudangiris and Shevaroys; "Robusta Kaapi Royale" comes from Robusta Parchment AB from Coorg, Wayanad, Chikmagalur and Travancore; monsooned coffees are dry-processed arabica and robusta used mainly in blends "to mellow and impart richness to rougher, more acidy coffees"; best grade is Monsooned Malabar AA. No altitudes are given by the Board. — [Coffee Board of India: specialty coffees](https://coffeeboard.gov.in/Specialitycoffee.aspx)
- Altitude (seller lot data): Monsooned Malabar AA from Chikmagalur family farms 1,067-1,280 masl; Mysore Coorg lot 1,220-1,524 m; Mysore Nuggets blend from Coorg/Chikmagalur 1,100-1,500 m; a Kerala Malabar monsooned coffee at 950 m. — [Royal Coffee: Monsoon Malabar AA](https://royalcoffee.com/?p=186529); [Royal NY: Mysore Coorg](https://www.royalny.com/?p=73751); [Indiamart seller listing](https://m.indiamart.com/homeblendllp); [H.R. Higgins](https://www.hrhiggins.co.uk/products/india-malabar-monsooned-coffee)
- India 2026/27: arabica 1.56M, robusta 4.58M; exports 6.22M bags with soluble 2.53M; arabica hit by excessive early-year rain followed by a dry spell. — [Daily Coffee News, May 2026](https://dailycoffeenews.com/2026/05/20/india-coffee-report-soluble-coffee-drives-exports-but-arabica-declining/)
- India was among origins Q Robusta graders favored for Fine Robusta; India is about 6% of world robusta (vs Vietnam about 40%, Uganda about 4.5% per one source). — [Atlas Coffee interview](https://www.atlascoffee.com/?p=6751)

### Inferences
- Wayanad (Kerala) and Nilgiris (Tamil Nadu) are named in the brief but no citable altitude/flavor source was found for them; Wayanad appears in the Board page only as a robusta parchment origin.
- Monsooned Malabar flavor (musty, spicy, low acidity) is from the brief; the Board says it mellows acidity, which is consistent but not a flavor-note source.

### Gaps
- Monsooning process details (months, 12-16 week exposure, bean swelling), harvest months, varieties (S795, Kent, Cauvery/Catimor, Sln series), Mysore Nuggets grade definitions (AAA/AA), and Indian rainfall/temperature: not retrieved.

---

## 5. Papua New Guinea

### Takeaway
PNG (about 800k bags in 2025/26) comes mostly from the Western Highlands (45%), Eastern Highlands (37%) and Simbu (6%), with a main harvest around April-September. Altitude sources vary widely (1,000-1,900 m typical).

### Cited Findings
- One guide lists Eastern Highlands 400-1,900 m and Western Highlands 1,000-1,800 m, both harvested April-September, with Bourbon, Typica and Arusha varieties; another gives a Kainantu-area cooperative lot at 1,300-1,600 masl, harvested June-August; a Western Highlands description cites altitudes up to 2,800 m. — [Helena Coffee PNG page](https://www.helenacoffee.vn/?p=21469) (attribution at result-group level)
- Sigri estate (Western Highlands) and Arona estate (Eastern Highlands) are the main estate coffees exported to North America; Sweet Maria's describes Kimel as a large farm that also buys from surrounding growers and sells under the same name. — [Wikipedia: Coffee production in PNG](https://en.wikipedia.org/wiki/Coffee_production_in_Papua_New_Guinea); [Sweet Maria's PNG overview](https://library.sweetmarias.com/coffee-producing-countries/oceania/papua-new-guinea-coffee-overview/) (page returned HTTP 403 on direct fetch; content seen only through search snippet)
- Simbu described as melon and honey with full complex body; Simbu specialty coverage is thin. — [Coffee Hunter journal](https://coffeehunter.com/journal-tag/papua-new-guinea/) (attribution at result-group level)
- No PNG Cup of Excellence results found; PNG appears as a standard specialty origin but no national competition table was retrieved.

### Inferences
- PNG "fruity, floral, bright" in the brief is consistent with Simbu/estate descriptors but only Simbu (melon, honey) is directly sourced. Use as moderate acidity/medium body, inferred.

### Gaps
- Arona/Kimel altitudes, harvest and grade system (PNG uses "Y", "X", "AA", "A" grades, from background knowledge, unverified here); PNG rainfall/temperature; Sigri details.

---

## 6. China (Yunnan)

### Takeaway
Yunnan (about 1.9M bags, all arabica, per USDA) is Catimor-dominant (over 80% of area per one source) in Baoshan, Pu'er and Lincang at roughly 1,000-1,900 m, with cups from nutty/floral to stone fruit and caramel; specialty lots (including Geisha) have scored 91+ in an ACE competition table.

### Cited Findings
- Catimor is over 80% of Yunnan's planted area (one source). Altitude by one guide: Baoshan 1,200-1,800 m; Pu'er 1,000-1,500 m; Lincang 1,100-1,600 m. A Sucafina Catimor HG lot from Baoshan/Menglian/Pu'er lists 1,100-1,600 m. — [Yunnan Coffee Guide: regions](https://yunnancoffeeguide.pages.dev/regions.html); [Sucafina China](https://sucafina.com/na/origins/china)
- Flavor by region (guide): Baoshan jasmine-like floral with nutty undertones; Pu'er plum-like acidity with caramel (another guide: chocolate-forward); Lincang caramel, brown sugar, peach, apricot. A single-farm Baoshan Catimor at 1,520-1,600 m: dried dates, cacao nibs, blood orange, plum, red wine; another Catimor 7963 lot: jasmine, cranberry, brown sugar, Earl Grey. — [Yunnan Coffee Guide](https://yunnancoffeeguide.pages.dev/regions.html); [Kurasu Baoshan](https://kurasu.kyoto/products/china-yunnan-baoshan-medium-roast)
- "Gems of Yunnan" (Alliance for Coffee Excellence) table lists a Lincang Geisha washed lot at 1,600-1,900 m scoring 91.78; the table is not labeled Cup of Excellence. — [ACE Gems of Yunnan 2025](https://allianceforcoffeeexcellence.org/gems-of-yunnan-2025/)

### Inferences
- "Stone fruit, honey" (brief) matches Lincang descriptors; mark Yunnan acidity moderate (5-6), body medium, sweetness 6-7, all inferred.

### Gaps
- Yunnan harvest months (typically late autumn to early spring from background knowledge, unverified), processing share (washed vs natural vs honey), and rainfall/temperature: not retrieved.

---

## 7. Southeast Asia and other Asia-Pacific origins (Thailand, Laos, Timor-Leste, Philippines, Myanmar, Malaysia, Taiwan, Nepal, Sri Lanka, Japan, Australia, Pacific islands, Hawaii)

### Takeaway
Source coverage is uneven: Laos, Timor-Leste, the Philippines and Hawaii have usable data; Thailand has only a 2026 competition result; Myanmar, Nepal, Sri Lanka, Okinawa, Fiji, Samoa and Australia were not found in citable sources.

### Cited Findings
- Laos (Bolaven Plateau): about 600-1,350 m for the plateau; washed lot 1,000-1,300 m; Geisha lot 900-1,300 m; Lao Mountain Coffee grows Catimor, Typica and Caturra at 1,200-1,300 m; Typica added in 2012; Catimor introduced for disease resistance and led farmers to replace tea. Bolaven Coffee is a Lao geographical indication (WIPO story). USDA: Laos 475k (2025/26), 500k (2026/27F). — [HomeGrounds Laos](https://www.homegrounds.co/laos-coffee/); [Lao Mountain Coffee](https://laomountain.com/pages/about-us); [WIPO: Bolaven coffee](https://www.wipo.int/en/web/ip-advantage/w/sackda)
- Thailand: USDA 900k bags (robusta, 2025/26); Thailand CoE 2026 held 18 June 2026 in Chiang Mai, winner from Nan province at 90.05 (Thai-language report; name spelling unverified); a "Best of Thailand" CoE pilot program celebrated 15 winners earlier. — [USDA FAS July 2026](https://apps.fas.usda.gov/psdonline/circulars/2026/07/coffee.pdf); [Bangkok Biz News](https://www.bangkokbiznews.com/lifestyle/1239469); [ACE Thailand 2026](https://allianceforcoffeeexcellence.org/thailand-2026/); [GCR: Best of Thailand](https://www.gcrmag.com/best-of-thailand-coe-pilot-program-celebrates-15-winners)
- Timor-Leste: Ermera district produces almost half the nation's coffee (World Bank, as quoted); Letefoho is Sucafina's main sourcing area; altitude 1,000-1,600 m or 1,200-1,800 m or 1,300-1,900 m depending on source; harvest May-September (Sucafina) or May-October / June-August on lots; Hibrido de Timor is a natural arabica x robusta cross (discovery dated 1920s or 1940s depending on source), used in breeding worldwide for disease resistance. — [Sucafina Timor-Leste](https://sucafina.com/na/origins/timor-leste); [Zest Coffee: Timor-Leste](https://www.zestcoffee.com.au/?p=8774); [Wikipedia: Coffee industry of Timor-Leste](https://wikipedia.com/wiki/Coffee_industry_of_Timor_Leste)
- Philippines: arabica above 1,000 m in Benguet, Kalinga and Sagada (Mountain Province), sweet/floral/nutty; liberica ("barako") mainly in Batangas, grown at 300-600 m by one source and 0-800 m by another; excelsa in Batangas, Quezon and Sorsogon; the commonly sold "Benguet Barako" is actually from Batangas; the etymology of "barako" is disputed; USDA 450k bags (2025/26). — [Coffeeness Philippines](https://www.coffeeness.de/en/philippines-coffee/); [Philippine Coffee Board](https://philcoffeeboard.com/the-beginners-guide-to-the-main-types-of-coffee/); [HomeGrounds Philippine coffee](https://www.homegrounds.co/philippine-coffee/)
- Hawaii: Ka'u elevation 1,100-2,700 ft (about 335-825 m), about 830 acres, 80-90 farms (undated booklet); Kona Type I grades: Extra Fancy, Fancy, No. 1, Select, Prime; Type II: Peaberry No. 1 and Prime; grading by size/shape, color, moisture and defects; sources conflict on the Extra Fancy screen (19/64 vs 18/64 inch); harvest conflicts: mid-Aug to April (Kona farm) vs Aug-Dec (importer). — [Hawaii Coffee Association booklet](https://hca.wildapricot.org/resources/Documents/DOA-HICoffeeAssoc-Booklet.v4_print.pdf); [Kona Coffee & Tea: grades](https://konacoffeeandtea.com/blogs/kona-blog/coffee-grades-hawaii); [HomeGrounds Kona grades](https://www.homegrounds.co/kona-coffee-grades-rating/); [Perfect Daily Grind: Hawaiian coffee](https://perfectdailygrind.com/2022/01/a-guide-to-hawaiian-coffee-production/); [Cafe Imports Hawaii](https://www.cafeimports.com/australia/hawaii)
- Vanuatu (Tanna): about 400 masl, volcanic soil, coffee grown since 1852; Tanna Coffee Development Company founded 1984; full-bodied, nutty, little bitterness. — [Vanuatu Tourism: Tanna Coffee](https://www.vanuatu.travel/tanna-coffee); [Espresso Coffee Guide: Vanuatu](https://espressocoffeeguide.com/gourmet-coffee/asian-indonesian-and-pacific-coffees/vanuatu-coffee)
- Taiwan: Gukeng (Yunlin County) is "Taiwan's coffee capital"; coffee seedlings were cultivated there under Japanese colonial rule; Gukeng Coffee Festival since 2003. — [SCMP on Taiwanese coffee](https://www.scmp.com/magazines/style/travel-food/article/2182194/move-over-bubble-milk-tea-meet-taiwanese-coffee)
- Australia: a Nespresso origin table lists a Mackay (Queensland) entry described as from Sri Lanka or Coorg seed (minor). — [Nespresso Guide origin table, Oceania](https://nespressoguide.com/2019/06/29/table-of-coffee-origins-oceania)

### Inferences
- Liberica/Excelsa notes for the tool: Philippines (barako = liberica, low elevation; excelsa in Batangas/Quezon/Sorsogon) is the best-supported liberica example here; Malaysia liberica not sourced.
- Kona Extra Fancy and Ka'u should carry a "US grade (HDOA)" field rather than the generic grade_system; Ka'u altitude converted to approximately 335-825 masl by me.

### Gaps
- Thailand (Chiang Mai/Chiang Rai altitude, varieties, harvest), Myanmar (Shan/Pyin Oo Lwin), Nepal (Gulmi, Kaski), Sri Lanka, Japan Okinawa, Fiji, Samoa, Malaysia liberica (Johor, Sabah), Australia (Mareeba/Daintree/Northern Rivers), Kona altitude and Kona/Ka'u flavor notes and Kona production figures (NASS not retrieved): no citable data found.
- PNG, Laos CoE and national competitions: none found.

---

## 8. Fine Robusta / Q Robusta scores and flavor descriptors

### Takeaway
Under the CQI/UCDA Q Robusta scheme, 80+ is "Fine Robusta" (above 90 "Very Fine", 70-80 "Premium"). Robusta is scored against robusta, not arabica. Vietnamese Q-graded lots of 85.5-86.0 exist. Origin-specific flavor descriptors for India, Uganda and Brazil conilon were not found.

### Cited Findings
- Scoring bands: 80+ specialty/fine; 80-90 "Fine Robusta"; above 90 "Very Fine"; 70-80 "Premium". Q Robusta grading compares robusta to robusta. — [Kaffeemacher: Fine Robusta and Q Robusta grading](https://kaffeemacher.de/en/blogs/kaffeewissen/fine-robusta-and-q-robusta-grading)
- The program began in Uganda: first Q Robusta course in 2010 with UCDA. A CQI study graded 67 canephora samples from 13 countries including Brazil, India, Indonesia, Uganda and Vietnam. — [Coffee Review: CQI takes on robusta taboo](https://www.coffeereview.com/cqi-takes-on-robusta-taboo/); [Kaffeemacher](https://kaffeemacher.de/en/blogs/kaffeewissen/fine-robusta-and-q-robusta-grading)
- Flavor depends on terroir and processing; SCA has developed a Canephora flavor wheel (SCA news issue 25). — [SCA: Developing the Canephora Flavor Wheel](https://sca.coffee/sca-news/25/issue-25-insight-canephora-flavour-wheel-ymxnw)
- Vietnamese Q-certified lots at 86.00 and 85.50 (one listing). — [Helena Coffee](https://www.helenacoffee.vn/?p=26023)

### Inferences
- A sensible default for the tool: robusta commodity grade (Screen 16/18, Grade 1) vs Fine Robusta (Q score 80+) as two separate tiers; acidity low, body high, bitter/rubbery descriptors typical for commodity, "cacao, nutty, caramel" for fine washed/honey lots (inferred from general robusta knowledge, not from these sources).

### Gaps
- Score ranges and flavor descriptors specifically by Indian robusta (e.g., Kaapi Royale, monsooned robusta), Ugandan, and Brazilian conilon: not retrieved. The SCA Canephora flavor wheel page was not opened.

---

## Draft dataset rows (all numeric ratings inferred, not source ratings)

Altitudes taken from the cited sources above (union of ranges where sources overlap; conflict noted). `rating_basis` = inferred from descriptor words. production_60kg_bags is the country total (2025/26 USDA, July 2026) and is not region-specific; `source_url` for production is the USDA PDF.

| country | region | altitude_min_masl | altitude_max_masl | varieties | processing | harvest_months | grade_system | flavor_notes | acidity | body | sweetness | rating_basis | production_60kg_bags | production_year | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Indonesia | Sumatra Lintong | 1400 | 1800 | n/a (not sourced) | wet-hulled (giling basah) | n/a (not sourced) | G1 / Triple Pick (importer label) | plum, kumquat, molasses, syrupy body | 4 | 8 | 6 | inferred | 12370000 | 2025/26 | https://specialtycoffee.id/?p=13553 |
| Indonesia | Sumatra Mandheling | 1100 | 1600 | n/a | wet-hulled | n/a | G1 (loose trade term) | cocoa, tobacco, forest spice, earthy, molasses | 3 | 9 | 5 | inferred | 12370000 | 2025/26 | https://specialtycoffee.id/articles/mandheling-coffee/ |
| Indonesia | Aceh Gayo | 1400 | 1800 | n/a | wet-hulled; some washed | n/a | n/a | dark chocolate, cedar, brown sugar, herbal, citrus lift | 4 | 8 | 6 | inferred | 12370000 | 2025/26 | https://artizancoffee.com/blogs/arrivals/sumatra-mandheling-gayo |
| Indonesia | Sulawesi Toraja | 1400 | 1900 | n/a | wet-hulled | n/a | n/a | dark fruit, dark chocolate, heavy body, low acidity | 4 | 8 | 5 | inferred | 12370000 | 2025/26 | https://specialtycoffee.id/articles/sulawesi-kalosi-coffee/ |
| Indonesia | Sulawesi Kalosi (Enrekang) | 1200 | 1800 | n/a | dry-hulled (one source) | n/a | n/a | floral, spice, brighter acidity | 5 | 7 | 5 | inferred | 12370000 | 2025/26 | https://specialtycoffee.id/articles/sulawesi-kalosi-coffee/ |
| Indonesia | Flores Bajawa | 1200 | 1800 | n/a | n/a | n/a | n/a | nutty, caramel, chocolate, medium body | 5 | 6 | 6 | inferred | 12370000 | 2025/26 | https://fnb.tech/indonesian-coffee-origins/ |
| Indonesia | Bali Kintamani | 1200 | 1700 | n/a | washed, natural, honey | n/a | n/a | citrus, molasses, bright acidity | 7 | 5 | 6 | inferred | 12370000 | 2025/26 | https://fnb.tech/indonesian-coffee-origins/ |
| Indonesia | Java Ijen | 900 | 1500 | n/a | mostly washed | n/a | n/a | chocolate, nuts, cinnamon, cedar, creamy body | 6 | 6 | 5 | inferred | 12370000 | 2025/26 | https://sucafina.com/na/news/about-indonesia |
| Vietnam | Dak Lak (robusta) | 400 | 800 | robusta | n/a | Oct-Jan (one source Nov-Mar) | TCVN 4193:2014 Grade 1, Screen 16/18 | n/a (brief: bold, nutty, rubbery) | 2 | 8 | 3 | inferred | 31700000 | 2025/26 | https://greentech-drl.pages.dev/guides/vietnam-coffee-origins |
| Vietnam | Lam Dong / Da Lat | 900 | 1500 | robusta; arabica Catimor | washed (arabica) | Nov-Mar | Screen 16/18 | n/a | 5 | 5 | 5 | inferred | 31700000 | 2025/26 | https://www.helenacoffee.vn/product/arabica-catimor-fully-washed-s18/ |
| India | Chikmagalur / Coorg (Mysore Nuggets) | 1067 | 1524 | arabica (varieties not sourced) | washed | n/a | Mysore Nuggets Extra Bold | n/a | 5 | 6 | 5 | inferred | 6430000 | 2025/26 | https://coffeeboard.gov.in/Specialitycoffee.aspx |
| India | Monsooned Malabar AA | 950 | 1280 | arabica/robusta | dry (natural) + monsooning | n/a | Monsooned Malabar AA | brief: musty, spicy, low acidity | 2 | 8 | 4 | inferred | 6430000 | 2025/26 | https://coffeeboard.gov.in/Specialitycoffee.aspx |
| Papua New Guinea | Eastern/Western Highlands | 1000 | 1900 | Bourbon, Typica, Arusha | n/a | Apr-Sep | n/a | melon, honey (Simbu) | 6 | 6 | 6 | inferred | 800000 | 2025/26 | https://www.helenacoffee.vn/?p=21469 |
| China | Yunnan Baoshan | 1200 | 1800 | Catimor (>80% of area, province) | n/a | n/a | n/a | jasmine, nutty; stone fruit, brown sugar in Lincang | 5 | 5 | 7 | inferred | 1900000 | 2025/26 | https://yunnancoffeeguide.pages.dev/regions.html |
| China | Yunnan Pu'er | 1000 | 1500 | Catimor | n/a | n/a | n/a | plum acidity, caramel, chocolate | 5 | 6 | 6 | inferred | 1900000 | 2025/26 | https://yunnancoffeeguide.pages.dev/regions.html |
| China | Yunnan Lincang | 1100 | 1900 | Catimor, Geisha (competition lot) | washed (Geisha lot) | n/a | n/a | caramel, brown sugar, peach, apricot | 6 | 5 | 7 | inferred | 1900000 | 2025/26 | https://allianceforcoffeeexcellence.org/gems-of-yunnan-2025/ |
| Laos | Bolaven Plateau | 900 | 1350 | Catimor, Typica, Caturra | washed (one lot) | n/a | n/a | n/a | n/a | n/a | n/a | not rated | 475000 | 2025/26 | https://www.homegrounds.co/laos-coffee/ |
| Timor-Leste | Ermera (Letefoho) | 1000 | 1900 | Hibrido de Timor (and others) | n/a | May-Sep | n/a | n/a | n/a | n/a | n/a | not rated | n/a | n/a | https://sucafina.com/na/origins/timor-leste |
| Philippines | Benguet / Sagada (arabica) | 1000 | null | arabica | n/a | n/a | n/a | sweet, floral, nutty | n/a | n/a | n/a | not rated | 450000 | 2025/26 | https://www.coffeeness.de/en/philippines-coffee/ |
| Philippines | Batangas (liberica/barako) | 0 | 800 | liberica; excelsa | n/a | n/a | n/a | n/a | n/a | n/a | n/a | not rated | 450000 | 2025/26 | https://www.homegrounds.co/philippine-coffee/ |
| USA (Hawaii) | Ka'u | 335 | 825 | n/a | n/a | n/a | HDOA Extra Fancy/Fancy/No.1/Select/Prime; Peaberry | n/a | n/a | n/a | n/a | not rated | n/a | n/a | https://hca.wildapricot.org/resources/Documents/DOA-HICoffeeAssoc-Booklet.v4_print.pdf |
| Vanuatu | Tanna | 400 | 400 | n/a | n/a | n/a | n/a | full-bodied, nutty, low bitterness | n/a | n/a | n/a | not rated | n/a | n/a | https://www.vanuatu.travel/tanna-coffee |

Rows for Thailand, Myanmar, Nepal, Sri Lanka, Taiwan, Okinawa, Australia, Malaysia, Fiji, Samoa, Kona, Aceh Sidikalang, Papua (Baliem), and Lampung robusta have no citable altitude/flavor data from this research pass and should be filled in a follow-up (Thailand only has USDA production 900,000 bags and a 2026 CoE result).
