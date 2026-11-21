# Coffee Species and Cultivated Varieties (dataset-ready catalog notes, current to Nov 2026)

Conventions used below:
- Field names follow the brief: variety, species, group, origin_country, year, altitude_min_masl, altitude_max_masl, yield_potential, bean_size, rust_resistance, cup_notes, acidity, body, sweetness, cupping_score_typical, source_url.
- "[INFERRED]" = my own derivation from cited numbers. "[UNVERIFIED]" = taken from a secondary/aggregator source or a search-result summary whose primary document I did not open. "null" = not found.
- WCR = World Coffee Research Arabica Variety Catalog. Individual pages are at `https://varieties.worldcoffeeresearch.org/varieties/<slug>`. The catalog lists 70 Arabica varieties per its index page ([WCR index](https://varieties.worldcoffeeresearch.org/arabica/varieties)) plus a separate robusta section ([WCR robusta](https://varieties.worldcoffeeresearch.org/robusta/varieties)).
- WCR data caveat: several WCR pages render multiple option values for one field (yield, rust, nematodes, CBD) without labels, so the fetch tool read the "first" value. I flag the pages where the extraction itself noted this (Mundo Novo, Java, SL34). Verify those cells against the live page before shipping.
- WCR altitude is latitude-dependent, not a single range. Thresholds are given as (a) 5N-5S, (b) 5-15 N/S, (c) beyond 15 N/S. WCR gives no maximum altitude. For the flat `altitude_min_masl` column I suggest storing the 5-15 degree value (covers most of Central America, Colombia highlands, much of East Africa edge) and keeping the full triple in a separate `altitude_note` column [INFERRED design choice].

---

## 1. Species: Coffea arabica, canephora, liberica (incl. excelsa/dewevrei), stenophylla, eugenioides, racemosa

### Takeaway
Arabica (allotetraploid, 2n=44) is about 57% of world output and robusta (diploid, 2n=22) about 42% by ICO's 2024/25 figures; liberica/excelsa is a rounding error (probably under 1,000 t/yr, about 0.01% of exports, per the 2025 Kew-led species study, not the "1-2%" often quoted). Caffeine, chlorogenic acids, lipid and sucrose all follow arabica < robusta for caffeine/CGA and arabica > robusta for lipid/sucrose, but ranges vary by study; stenophylla is the interesting heat-tolerant, arabica-like wild species (80.25 cupping score in a single small tasting).

### Cited Findings

**Production share**
- ICO 2024/25 world production reported at 177.513 million 60-kg bags: 102.065 M arabica and 75.448 M robusta (shares of about 57.5% and 42.5% are my calculation [INFERRED]); I did not open the primary ICO PDF, the numbers came through a search summary of ICO-sourced pages — [ICO Coffee Market Report May 2025](https://www.ico.org/documents/cy2024-25/cmr-0525-e.pdf) [UNVERIFIED mapping of exact figures to this document]
- USDA (Dec 2025) 2024/25 estimate: 174.395 M bags total, arabica 98.692 M, robusta 75.703 M — [Comunicaffe](https://www.comunicaffe.com/usda-biannual-report-cuts-estimate-of-world-production-for-2024-25-to-174-4-million)
- Brazil's Ministry of Agriculture (Feb 2025): 174.9 M bags, arabica 56% / robusta+conilon 44% — [Safras](https://safras.com.br/eng/world-coffee-production-in-2024-25-is-revised-to-174-9-mln-bags/)
- Wikipedia (older framing): arabica about 55%, robusta about 45%; robusta page gives 45% in lead and 46% in cultivation section — [Wikipedia Coffea](https://en.wikipedia.org/wiki/Coffea); [Wikipedia C. canephora](https://en.wikipedia.org/wiki/Coffea_canephora)
- Liberica + excelsa: authors of the 2025 Nature Plants species-delimitation paper estimate global production "probably less than 1,000 metric tons", about 0.01% of exports, and say the "1-2% of global supply" claim is outdated (based on late-19th-century figures) — [Daily Coffee News, Aug 2025](https://dailycoffeenews.com/2025/08/21/study-says-liberica-and-excelsa-are-separate-species-with-implications-for-cultivation/)
- Arabica + robusta together exceed 99.99% of world coffee (2026 DCN article, as relayed by search summary) — [Daily Coffee News, May 2026](https://dailycoffeenews.com/2026/05/21/researchers-propose-libex-hybrid-as-climate-change-accelerates/) [UNVERIFIED, snippet only]
- stenophylla, eugenioides, racemosa: no commercial production share found (see Gaps).

**Taxonomy and genetics**
- Genus Coffea: Plants of the World Online accepts 133 species and one hybrid as of January 2026 — [Wikipedia Coffea](https://en.wikipedia.org/wiki/Coffea)
- C. arabica: 44 chromosomes (four copies of 11 chromosomes); allotetraploid hybrid of C. canephora x C. eugenioides, hybridization estimated 1.08 million to 543,000 years ago; endemic to the SW Ethiopian highlands; plantation coffee holds under 1% of the diversity of wild Yemeni populations — [Wikipedia C. arabica](https://en.wikipedia.org/wiki/Coffea_arabica)
- Denoeud et al. 2014 (Science 345:1181-1184) sequenced C. canephora, described as an outcrossing, highly heterozygous diploid and a parent of arabica (2n=4x=44); no whole-genome triplication; caffeine pathway genes expanded by tandem duplication, i.e. caffeine biosynthesis evolved independently in coffee vs tea/cacao — [Denoeud 2014 (HAL)](https://hal.inrae.fr/hal-02641562/document)
- Genus review: all taxa diploid 2n=22 except arabica (2n=44) — [PMC4244848](https://pmc.ncbi.nlm.nih.gov/articles/PMC4244848) [UNVERIFIED: the claim came through a search-result summary; I did not open this paper]
- C. eugenioides: 2n=22 per PROTA — [PROTA/PROSEA](https://prosea.prota4u.org/view.aspx?id=608) [UNVERIFIED: page content fetched covered liberica only; claim relayed via search summary]
- C. racemosa: 2n=22 (1956 Bragantia study) — [SciELO Bragantia](https://scielo.br/j/brag/a/nhMMmHfnNbFgwcLqcvySJBB/?lang=pt)
- C. canephora: two main cultivated groups, robusta and nganda — [Wikipedia C. canephora](https://en.wikipedia.org/wiki/Coffea_canephora)
- Liberica taxonomy (Davis et al. 2025, Nature Plants): 353 nuclear genes across 55 samples support splitting into C. liberica, C. dewevrei (= excelsa) and newly recognised C. klainei; wild ranges of liberica and excelsa do not overlap; wild liberica is now limited to five West African countries (reported 95% reduction from earlier estimates); C. klainei occurs in Cameroon, Gabon, Angola — [Daily Coffee News, Aug 2025](https://dailycoffeenews.com/2025/08/21/study-says-liberica-and-excelsa-are-separate-species-with-implications-for-cultivation/)
- A 2024 Nature Genetics paper reports chromosome-level assemblies of a di-haploid arabica and its progenitors C. eugenioides and C. canephora — mentioned in [Denoeud search listing](https://hal.inrae.fr/hal-02641562/document) [UNVERIFIED, no primary URL retrieved]

**Caffeine (green bean, % dry matter)**
- Arabica: normal beans about 12 mg/g (1.2%, my conversion); low-caffeine AC1/AC2/AC3 mutants 0.76 mg/g — [Wikipedia C. arabica](https://en.wikipedia.org/wiki/Coffea_arabica)
- Per 100 g dry seed (PROTA): arabica 0.6-1.7 g; canephora 1.5-3.3 g; eugenioides 0.3-0.6 g — [PROTA/PROSEA](https://prosea.prota4u.org/view.aspx?id=608) [UNVERIFIED: figures relayed via search summary of PROTA]
- Robusta: about 2.7% vs arabica 1.5% — [Wikipedia C. canephora](https://en.wikipedia.org/wiki/Coffea_canephora). Measured in 7 Hainan robusta cultivars: 1.88-2.61 g/100 g DW (trigonelline 0.75-0.87) — [PMC6332462](https://pmc.ncbi.nlm.nih.gov/articles/PMC6332462)
- Comparison table: arabica 1.2-1.5%, robusta 2.2-2.7% — [Compound Interest PDF](https://www.compoundchem.com/wp-content/uploads/2023/10/Coffee-arabica-vs-robusta-2023.pdf) [UNVERIFIED: label alignment in extracted text unclear]
- Liberica: 0.5-1.8% of dry matter, average 1.6 g/100 g — [PROTA/PROSEA](https://prosea.prota4u.org/view.aspx?id=608). Another cited figure: 1.35% (liberica) vs 1.72% (arabusta) from a 1985 source — [CORE PDF](https://core.ac.uk/download/227015243.pdf) [UNVERIFIED: attribution uncertain]
- Racemosa: described as low-caffeine with high flavour value for breeding; no bean percentage found — [SciELO Bragantia](https://scielo.br/j/brag/a/nhMMmHfnNbFgwcLqcvySJBB/?lang=pt)
- Laurina (an arabica mutant): about 0.3-0.75% (retailer claims) vs 1.2-1.6% typical arabica — [Perfect Daily Grind: What is Laurina](https://perfectdailygrind.com/2022/04/what-is-laurina-coffee/) [UNVERIFIED: seller-sourced figures]

**Chlorogenic acids, lipids, sucrose**
- Comparison table: chlorogenic acid 5.5-8.0% (arabica) vs 7.0-10.0% (robusta); lipid 15-17% vs 10.5-11.0%; sucrose 6.0-9.0% (arabica) — [Compound Interest PDF](https://www.compoundchem.com/wp-content/uploads/2023/10/Coffee-arabica-vs-robusta-2023.pdf) [UNVERIFIED: column alignment ambiguous; the source's own text is flagged for verification]
- Arabica richer in sucrose and oil, robusta higher in bioactive compounds (Brazilian study) — [CORE PDF](https://core.ac.uk/download/227015243.pdf) [UNVERIFIED: attribution of the sentence to this PDF is uncertain]
- Sucrose 5-9.5% (arabica) vs 4-7% (canephora) from a review — [Crop J. Chesereke 2021](https://www.cropj.com/chesereke_15_2_2021_201_208.pdf) [UNVERIFIED: attribution uncertain]
- Robusta (Hainan, 7 cultivars, % DW): 5-CQA 0.73-1.05, 4-CQA 0.10-0.14, total lipid 8.60-12.03; literature lipid range 13-17% (species unstated) — [PMC6332462](https://pmc.ncbi.nlm.nih.gov/articles/PMC6332462). Note this conflicts with the 5.5-10% total-CGA figures above: the paper reports single isomers, not total CGA, so do not compare directly.
- Liberica: CGA, caffeine and antioxidant data "scarce"; no reliable lipid/sucrose numbers found — [CORE PDF](https://core.ac.uk/download/227015243.pdf) [UNVERIFIED]

**Altitude, temperature, rainfall**
- Arabica: usually grown 1,200-1,500 m, range sea level to 2,800 m in some plantations; best mean temp 15-24 C; frost intolerant; rainfall 1.2-1.8 m/yr evenly spread — [Wikipedia C. arabica](https://en.wikipedia.org/wiki/Coffea_arabica)
- Temperature alternatives: arabica 18-23 C, robusta 24-30 C (one source in the search); arabica 18-24 C / robusta 22-28 C (a low-quality site) — [GCR: influence of latitude](https://www.gcrmag.com/the-influence-of-latitude-on-coffee-quality) [UNVERIFIED attribution to this URL; several search hits blended]
- Robusta altitude: "mainly cultivated at lower altitudes (800-1,500 m)" per one search source, which conflicts with the brief's 0-800 m — [Interactive effects of altitude...](https://library.sweetmarias.com/wp-content/uploads/2020/08/Interactive-effects-of-altitude-microclimate-and-shading-system-on-coffee-leaf-rust.pdf) [UNVERIFIED attribution]. Flag this conflict to the writer.
- Leaf rust incidence in arabica tends to fall with altitude; shade that keeps diurnal range low and dew point high can raise rust at mid/high altitudes — [Sweet Maria's PDF above](https://library.sweetmarias.com/wp-content/uploads/2020/08/Interactive-effects-of-altitude-microclimate-and-shading-system-on-coffee-leaf-rust.pdf); [Nature Sci Rep 2023](https://www.nature.com/articles/s41598-023-36474-w)
- Liberica: lowland to lower montane rain forest up to about 1,300 m (Malaysia 1,200 m, Philippines 900 m); warm humid; intolerant of waterlogging; flowering triggered by heavy showers — [PROTA/PROSEA](https://prosea.prota4u.org/view.aspx?id=608)
- Excelsa: crops viably under higher temperatures and tolerates extended low rainfall better than robusta; liberica/excelsa may suit low-elevation hotter, wetter sites unsuitable for arabica or robusta — [Daily Coffee News, Aug 2025](https://dailycoffeenews.com/2025/08/21/study-says-liberica-and-excelsa-are-separate-species-with-implications-for-cultivation/)
- Stenophylla: mean annual temperature of its habitat 24.9 C, 1.9 C above robusta and up to 6.8 C above arabica (about 19 C) — [Sci.News on Davis et al. 2021 Nature Plants](https://www.sci.news/biology/coffea-stenophylla-09573.html); [Smithsonian](https://www.smithsonianmag.com/smart-news/rediscovered-coffee-species-boosts-crops-climate-resilience-without-sacrificing-taste-180977558/)

**Disease tolerance**
- Arabica is generally more susceptible to disease and climate variation than robusta — [Wikipedia C. arabica](https://en.wikipedia.org/wiki/Coffea_arabica). Leaf rust (Hemileia vastatrix) causes losses up to US$2 billion/yr; cut Central American output 16% in 2012-13 — same page.
- Robusta is "less susceptible to disease" than arabica; the 1927 Timor arabica x robusta hybrid became the root of rust-resistant breeding — [Wikipedia C. canephora](https://en.wikipedia.org/wiki/Coffea_canephora). Note this is not a quantified rust-tolerance figure.
- Liberica: susceptible to leaf rust but much less than other coffees; susceptible to pink disease; berry borer attacks only 1-5% of fruit in Malaysia vs 16-77% in robusta; less nematode-susceptible than robusta — [PROTA/PROSEA](https://prosea.prota4u.org/view.aspx?id=608)
- Stenophylla: IUCN Vulnerable (threatened by deforestation); disease data not found — [Sci.News](https://www.sci.news/biology/coffea-stenophylla-09573.html)

**Cup profile and price tier**
- Arabica: sweeter taste preferred — [Wikipedia Coffea](https://en.wikipedia.org/wiki/Coffea). Robusta: lower acidity, more bitterness, woody, less fruity, "earthy", bitterness tied to pyrazines — [Wikipedia C. canephora](https://en.wikipedia.org/wiki/Coffea_canephora)
- Liberica: more bitter than arabica or robusta; excelsa is less bitter; large hard-skinned fruit hard to pulp (excelsa has softer fruit); market share expected to stay low — [PROTA/PROSEA](https://prosea.prota4u.org/view.aspx?id=608)
- Stenophylla: blind tasting against two arabica and one robusta; London roastery panel gave 80.25 (specialty threshold), notes of natural sweetness, medium-high acidity, fruitiness, good body; small sample — [Sci.News](https://www.sci.news/biology/coffea-stenophylla-09573.html); paper DOI 10.1038/s41477-021-00891-4 (Nature Plants, 19 April 2021)
- Eugenioides: seed coffee "tastes mild and agreeable" (low caffeine); useful breeding parent for low caffeine — [PROTA/PROSEA via search](https://prosea.prota4u.org/view.aspx?id=608) [UNVERIFIED]
- Racemosa: high flavour, low caffeine, breeding value — [SciELO](https://scielo.br/j/brag/a/nhMMmHfnNbFgwcLqcvySJBB/?lang=pt)

### Suggested species table (CSV-ready, with values only where cited above)

| species | common_name | ploidy_2n | caffeine_pct_green | share_world_production | altitude_note | rust_note | cup_note | source_url |
|---|---|---|---|---|---|---|---|---|
| Coffea arabica | Arabica | 44 | 0.6-1.7 (PROTA); about 1.2 typical | about 57% (ICO 2024/25, [INFERRED] ratio) | 1,200-1,500 m typical, sea level-2,800 m extremes; 15-24 C | more susceptible than robusta; rust major threat | sweeter, higher acidity | https://en.wikipedia.org/wiki/Coffea_arabica |
| Coffea canephora | Robusta | 22 | 1.5-3.3 (PROTA); about 2.7 | about 42% (ICO 2024/25, [INFERRED]) | 800-1,500 m cited [UNVERIFIED], brief says 0-800 m | "less susceptible" than arabica | earthy, bitter, woody, low acidity | https://en.wikipedia.org/wiki/Coffea_canephora |
| Coffea liberica | Liberica | 22 | 0.5-1.8 | under 0.01% of exports | up to about 1,300 m, warm humid lowlands | susceptible, less than others | bitter | https://prosea.prota4u.org/view.aspx?id=608 |
| Coffea dewevrei (excelsa) | Excelsa | 22 [UNVERIFIED] | null | part of the same under-1,000 t | heat/drought tolerant | null | less bitter than liberica | https://dailycoffeenews.com/2025/08/21/study-says-liberica-and-excelsa-are-separate-species-with-implications-for-cultivation/ |
| Coffea stenophylla | Highland coffee | 22 [UNVERIFIED] | null | negligible | mean annual temp 24.9 C | null | 80.25 SCA-style, sweet, fruity | https://www.sci.news/biology/coffea-stenophylla-09573.html |
| Coffea eugenioides | Eugenioides | 22 | 0.3-0.6 | negligible | null | null | mild, agreeable | https://prosea.prota4u.org/view.aspx?id=608 |
| Coffea racemosa | Racemosa | 22 | low (no %) | negligible | null | null | high flavour | https://scielo.br/j/brag/a/nhMMmHfnNbFgwcLqcvySJBB/?lang=pt |

### Inferences
- [INFERRED] Because liberica/excelsa output is under 1,000 t/yr, a brewing tool should treat "liberica/excelsa" as a curiosity category; do not store the legacy "1-2%" value.
- [INFERRED] The brief's robusta 22-30 C / 0-800 masl is plausible as a lower-bound agronomic range but sources found give 24-30 C and 800-1,500 m; store as ranges with a `confidence` field.
- [INFERRED] Use "excelsa" as a label that maps to C. dewevrei after the 2025 split, with `species_legacy = "C. liberica var. dewevrei"`.
- [INFERRED] For a pricing tier field: arabica specialty > arabica commodity > robusta; but no price source was retrieved, so keep tier qualitative.

### Gaps
- No primary measured values for lipid, sucrose, chlorogenic acid, or caffeine in liberica, excelsa, stenophylla, racemosa, eugenioides beans beyond the PROTA figures above; the Compound Interest and CORE numbers are unverified.
- No reliable robusta leaf-rust tolerance figure (only qualitative "less susceptible"); no numeric rainfall for robusta.
- Chromosome counts for stenophylla and dewevrei (assumed diploid 2n=22 as genus norm) not directly sourced.
- Price tier per species: no source retrieved (ICE futures / ICO price data not queried).
- Primary ICO and Nature Plants / Nature Genetics papers not opened; figures taken from secondary summaries.

---

## 2. Cultivated varieties (arabica focus, WCR-first)

### Takeaway
The WCR catalog covers 70 arabica varieties and uses a small set of groups (Bourbon-Typica group, Ethiopian landrace, Gesha, Introgressed with Sarchimor/Catimor/Other subclasses, F1 hybrid). Many named varieties in the brief are NOT in WCR (Colombia, Castillo, Tabi, Kent, Sudan Rume, Sidra, Wush Wush, Pink Bourbon, Chiroso, Maracaturra, Icatu, Arusha, Mokka, Laurina, the JARC lines, Eugenioides, Liberica-excelsa), so those rows rely on secondary sources and are marked. The classic Bourbon-Typica varieties (Typica, Bourbon, Caturra, Pacas, Villa Sarchi, Catuai) are all rust-susceptible with "standard/good" quality; the Timor-Hybrid derivatives are rust-resistant but score "good" rather than "exceptional" at altitude on WCR's scale.

### Cited Findings

#### 2a. WCR-sourced rows (field values from each WCR page; `altitude_min_masl` shown as 5N-5S / 5-15 / >15 degrees latitude; max altitude not given by WCR)

Columns: variety | group | origin_country | year | altitude_min_masl (5N-5S / 5-15 / >15) | yield_potential | bean_size | rust_resistance | CBD | nematode | nutrition | WCR description / cup | source_url

| variety | group (WCR) | origin_country | year | altitude_min_masl | yield_potential | bean_size | rust_resistance | CBD / nematodes | nutrition | cup / notes | source_url |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Typica | Bourbon-Typica (Typica related) | Ethiopia > Yemen; single plant to Amsterdam 1706 | 1706 | 1600 / 1300 / 1000 | Low | Large | Low (susceptible) | susceptible / susceptible | Medium | high quality in Central America; cold-tolerant; very rust-susceptible; quality potential "Very good" | https://varieties.worldcoffeeresearch.org/varieties/typica |
| Bourbon | Bourbon-Typica (Bourbon related) | Yemen > Bourbon Island (La Reunion), early 1700s; Brazil c.1860 | early 1700s | 1600 / 1300 / 1000 | Medium | Average | Low (susceptible) | susceptible / susceptible | Medium | "excellent quality in the cup at the highest altitudes"; Very good | https://varieties.worldcoffeeresearch.org/varieties/bourbon |
| Caturra | Bourbon-Typica (Bourbon related) | Brazil (Minas Gerais) | found 1915-18; IAC selection from 1937 | 1600 / 1300 / 1000 | Medium | Average | Low | susceptible / susceptible | High | dwarf; "standard quality in Central America"; Good | https://varieties.worldcoffeeresearch.org/varieties/caturra |
| Catuai | Bourbon-Typica (Typica and Bourbon related) | Brazil | created 1949 (Mundo Novo x Caturra), released 1972 | 1600 / 1300 / 1000 | Very high | Average | Low | susceptible / susceptible | High | compact; standard quality; Good | https://varieties.worldcoffeeresearch.org/varieties/catuai |
| Mundo Novo | Bourbon-Typica (Typica and Bourbon related) | Brazil (Sao Paulo) | found 1943; distributed from 1952 | 1600 (equator) / 1300 / 1000; Peru >1500 | Very high [UNVERIFIED: page lists Medium and Low too] | Average | mixed values listed [UNVERIFIED] | mixed / mixed | High | "vigorous, productive, good cup"; late maturing; Good | https://varieties.worldcoffeeresearch.org/varieties/mundo-novo |
| Pacas | Bourbon-Typica (Bourbon related) | El Salvador | found 1949; ISIC selection from 1960 | 1600 / 1300 / 1000 (partly stated) | Medium | Average | Low ("very high susceptibility") | susceptible / susceptible | Medium | dwarf; standard quality; Good | https://varieties.worldcoffeeresearch.org/varieties/pacas |
| Pacamara | Bourbon-Typica (Typica and Bourbon related) | El Salvador (ISIC); Pacas x Maragogipe | year not stated (DCN: released 1970s) | 1600 / 1300 / 1000 | Low | Very large | Low ("very high susceptibility"); highly susceptible to Ojo de Gallo | susceptible / susceptible | Medium | exceptional cup potential; non-uniform, unstable across generations; wins CoE in El Salvador | https://varieties.worldcoffeeresearch.org/varieties/pacamara |
| Maragogipe | Bourbon-Typica (Typica related) | Brazil (Maragogipe, Bahia) | 1870 | 1600 / (to) 1000 | Low | Very large | Low | susceptible / susceptible | Low | "good to very good cup in Central America"; Pacamara often preferred | https://varieties.worldcoffeeresearch.org/varieties/maragogipe |
| Villa Sarchi | Bourbon-Typica (Bourbon related) | Costa Rica | 1950s-60s | 1600 / 1300 / 1000 | Medium | Below average | Low | susceptible / susceptible | High | "adapted to highest altitudes, tolerates strong winds"; Good | https://varieties.worldcoffeeresearch.org/varieties/villa-sarchi |
| Tekisic | Bourbon-Typica (Bourbon related) | El Salvador | selected from 1949; released 1977 | 1600 / 1300 / 1000 | Medium | Average | Low | susceptible / susceptible | Medium | early ripening; Very good potential; economically important in Guatemala | https://varieties.worldcoffeeresearch.org/varieties/tekisic |
| SL28 | Bourbon-Typica (Bourbon related) | Kenya (Scott Labs) | 1935 | 1200 / 900 / 700 | Low | Large | Low (ratings vary by race) | susceptible / susceptible | Low | drought-tolerant, very good cup; Exceptional | https://varieties.worldcoffeeresearch.org/varieties/sl28 |
| SL34 | Bourbon-Typica (Typica related) | Kenya (Loresho Estate, Kabete) | 1935-39 | 1200 / 900 / 700 | Medium [UNVERIFIED: page also lists Low, Very high] | Large | Low [UNVERIFIED] | CBD susceptible / susceptible [UNVERIFIED] | Medium | "exceptional cup quality but highly susceptible to CBD"; needs good rainfall | https://varieties.worldcoffeeresearch.org/varieties/sl34 |
| Geisha (Panama) | Ethiopian landrace (card label: Gesha) | Ethiopia > Tanzania > CATIE (Costa Rica) 1953 (T2722) > Panama 1960s | collected 1930s | 1600 / 1300 / 1000 | Low | Average | Intermediate | susceptible / susceptible | Medium | tall, brittle branches; "delicate floral, jasmine, peach-like aromas"; Exceptional at altitude; yield first in year 4 | https://varieties.worldcoffeeresearch.org/varieties/geisha-panama |
| Java | Ethiopian landrace | Ethiopia > Java (early 1800s), Cameroon 1980-90, Costa Rica 1991 | early 1800s | 1600 / 1300 / 1000 | Medium [UNVERIFIED] | Large | unclear (several values listed) [UNVERIFIED] | CBD tolerant / nematode resistant [UNVERIFIED] | Low | high quality in Central America, tolerant, low fertilizer; Very good | https://varieties.worldcoffeeresearch.org/varieties/java |
| Ruiru 11 | F1 hybrid (introgressed) | Kenya (CRF/KALRO) | released 1985 | 1000 / 700 / 400 | Very high | Large | Highly resistant | CBD resistant / nematodes susceptible | High | dwarf; hand-pollinated seed limits supply; Good | https://varieties.worldcoffeeresearch.org/varieties/ruiru-11 |
| Batian | Introgressed (Other) | Kenya | 2010 | 1000-1200 / 700-900 / 400-700 (low band) | High | Very large | Intermediate | CBD resistant / nematodes susceptible | Medium | tall; tolerates low management; Very good | https://varieties.worldcoffeeresearch.org/varieties/batian |
| Centroamericano (H1) | F1 hybrid (introgressed) | Central America consortium (CIRAD, CATIE, PROMECAFE) | 2010 | >1300 recommended; ranges vary | Very high | Large | Highly resistant | tolerant / susceptible | Very high | "good quality above 1300 m in healthy soil"; seeds don't breed true, propagate clonally | https://varieties.worldcoffeeresearch.org/varieties/centroamericano |
| Starmaya | F1 hybrid (introgressed) | Nicaragua (CIRAD-ECOM) | found 2001; release year not stated | 1200-1600 / 900-1300 / 700-1000 (medium band) | High | Large | Highly resistant | unknown / unknown | Medium | "notably high acidity in the cup"; Very good | https://varieties.worldcoffeeresearch.org/varieties/starmaya |
| Marsellesa | Introgressed (Sarchimor related) | Nicaragua (CIRAD-ECOM) | released 2009 | 1000-1600 / 700-1300 / 400-1000 | High | Average | Intermediate | tolerant / susceptible | High | "notably high acidity in the cup"; Good | https://varieties.worldcoffeeresearch.org/varieties/marsellesa |
| Parainema | Introgressed (Sarchimor related) | Honduras (IHCAFE; T5296 selection) | released 2004 | 1000-1600 / 700-1300 / 400-1000 | Very high | Large | Highly resistant (races can evolve) | tolerant / resistant to some Meloidogyne | High | Good | https://varieties.worldcoffeeresearch.org/varieties/parainema |
| Lempira | Introgressed (Catimor related) | Honduras (IHCAFE; Timor Hybrid 832/1 x Caturra) | year not stated | 1000-1600 / 700-1300 / 400-1000 | High | Average | Susceptible (rust confirmed in Honduras) | susceptible / susceptible | High | "adapted to warmest zones and acidic soils"; quality potential Low | https://varieties.worldcoffeeresearch.org/varieties/lempira |
| Catimor 129 (Nyika) | Introgressed (Catimor related) | Colombia (Cenicafe line) > Malawi; released 2006 | 2006 (Malawi) | 1600 / 1300 / 1000 | High | Large | Intermediate | resistant / susceptible | High | dwarf; needs careful management to avoid over-bearing; Good | https://varieties.worldcoffeeresearch.org/varieties/catimor-129 |
| Obata (Red) | Introgressed (Sarchimor related) | Brazil (IAC); Costa Rica 2014 | released Brazil 2000 | 1000-1600 / 700-1300 / 400-1000 | High | Large | Intermediate | unknown | High | high-yield, rust-resistant; Good | https://varieties.worldcoffeeresearch.org/varieties/obata-red |
| S795 | Introgressed (Other) | India (CCRI; S.288 x Kent) | year not stated | 1200 / 900 / 700 | High | Large | Highly resistant in global trials; considered susceptible in India | unknown / susceptible | Medium | high-yield, widely grown in India; Very good | https://varieties.worldcoffeeresearch.org/varieties/s795 |

Notes on these rows:
- WCR "quality potential at high altitude" labels (Exceptional, Very good, Good, Low) are not SCA scores; do not convert to numeric cupping_score_typical.
- WCR has no `acidity`, `body`, `sweetness` or `cupping_score_typical` fields. Leave null except where a description is explicit (Marsellesa and Starmaya "notably high acidity").
- WCR trial data: Gesha rust/yield evaluated at 23 sites in 15 countries in WCR's International Multilocation Variety Trial; local rust performance depends on race — [WCR Geisha](https://varieties.worldcoffeeresearch.org/varieties/geisha-panama)
- Wikipedia's reading of WCR on Geisha: rust "moderate resistance", CBD susceptible, nematodes susceptible, bean size average — [Wikipedia Geisha coffee](https://en.wikipedia.org/wiki/Geisha_coffee)
- Gesha page note: "the name Geisha is often applied to coffees that don't share its genetics" — [WCR search](https://varieties.worldcoffeeresearch.org/search?q=geisha)
- Other WCR catalog entries not detailed here (index summaries only): AB3, Anacafe 14, BM139, BM71, BPL10, Caripe, Casiopea, Catigua MG2, Catisic, Costa Rica 95, Cuscatleco, EC15, Esperanza, Evaluna, Fronton, H3, Harar Rwanda, IAPAR 59, IHCAFE 90, IPR 103, IPR 107, Jackson 2/1257, K7, Kartika 1, KP423, Limani, Mibirizi, Milenio (H10), Monte Claro, Mundo Maya, Nayarita, Nemaya (robusta rootstock), Nyasaland, Oro Azteca, Pache, Paraiso, Pop3303, RAB C15, SL14, Sln.5B, Sln.6, S4808, T5175, T5296, T8667, Venecia — [WCR index](https://varieties.worldcoffeeresearch.org/arabica/varieties)

#### 2b. Varieties NOT in WCR, from secondary sources

| variety | species | group | origin_country | year | rust_resistance | cup_notes | cupping_score_typical | source_url |
|---|---|---|---|---|---|---|---|---|
| Castillo | C. arabica | Introgressed (Catimor composite; Timor Hybrid x Caturra, per most sources) | Colombia (Cenicafe) | 2005 | multi-line rust resistance; reported also CBD-resistant | early concern about cup; Cenicafe tasting study could not distinguish regional derivatives from traditional varieties; similar to Caturra | null | https://www.intelligentsia.com/blogs/stories/colombia-san-pedro-de-cartago ; https://www.gcrmag.com/castillo-proves-resistant-to-coffee-berry-disease [UNVERIFIED: page returned 403; claim from search summary] |
| Colombia (variety) | C. arabica | Introgressed (Catimor composite F5, HdT x Caturra) | Colombia (Cenicafe) | 1982 | rust resistant | null | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ |
| Tabi | C. arabica | Introgressed (Typica/Bourbon-Timor derived) | Colombia (Cenicafe) | 2002 | rust resistant, non-dwarfing | aimed at improved flavor; resembles Typica and Bourbon | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ |
| Cenicafe 1 | C. arabica | Introgressed (Catimor composite) | Colombia | 2016 | improved CBD resistance | meets or exceeds Castillo | null | https://dailycoffeenews.com/2016/12/13/fnc-releases-resistant-cenicafe-1-hybrid-launches-major-sustainability-initiative |
| Kent | C. arabica | Typica selection | India (Doddengooda Estate, Mysore) | 1911 | initially resistant, has since lost resistance | null | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ |
| Sudan Rume | C. arabica | Ethiopian-type landrace (Boma Plateau, South Sudan) | South Sudan | null | moderate disease resistance; parent of Batian, Castillo, Centroamericano, Ruiru 11 | high sensory quality, low yield | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ |
| Mokka / Mokha | C. arabica | Bourbon mutation (very low caffeine) per Royal Coffee's guide; "Mokka" ambiguous (also a 17th-c. Yemen trade name) | probably Brazil | null | null | null | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ ; Sucafina glossary https://sucafina.com/na/About/glossary [UNVERIFIED] |
| Laurina / Bourbon Pointu | C. arabica | Bourbon mutation (recessive) | La Reunion (Reunion Island) | 18th-19th c. (sources conflict; one gives 1771) | null | very low caffeine (0.3-0.75% vs 1.2-1.6%, retailer claims) | null | https://perfectdailygrind.com/2022/04/what-is-laurina-coffee/ [UNVERIFIED seller numbers] |
| Maracaturra | C. arabica | Maragogipe x Caturra | Nicaragua / Brazil / El Salvador associations | null | null | large oval beans; high altitude Central America | Coffee Review 2-sample average 91 [UNVERIFIED context/date] | https://www.coffeereview.com/new-coffee-varieties/ (page itself did not mention Maracaturra; the 91 came from a search summary of a separate Coffee Review piece) |
| Icatu | C. arabica | Robusta x Bourbon Vermelho hybrid, backcrossed to arabica (Mundo Novo); sources conflict (one calls it Catimor-based) | Brazil (IAC) | null | disease resistant | null | null | https://ozonecoffee.co.uk/blogs/varietals/coffee-varietal-icatu [UNVERIFIED] |
| Arusha | C. arabica | Bourbon/Typica sub-variety of uncertain origin | Papua New Guinea, Tanzania | null | null | null | null | https://sucafina.com/na/About/glossary [UNVERIFIED] |
| Jember / S795 | C. arabica | Kent x S288 (India); widely used in Indonesia | India | null | disease resistant | null | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ |
| Timor Hybrid | C. arabica x C. canephora | spontaneous hybrid; base resistance source for Catimor/Sarchimor | Timor | early 20th c. | baseline rust resistance | regional favorite | null | https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/ |
| Bourbon colour variants (red/yellow/orange/pink) | C. arabica | Pink Bourbon: genetic tests suggest Ethiopian heirloom (not Bourbon); other colour variants not covered in what I retrieved | Colombia (Pink Bourbon) | null | null | Pink Bourbon: floral, tropical fruit, bright acidity | Coffee Review: 3 samples avg 90 (89-92) | https://www.coffeereview.com/new-coffee-varieties/ ; https://samplecoffee.com.au/coffee/varietals [UNVERIFIED, 403 on fetch] |

**Sidra, Chiroso, Pink Bourbon, Wush Wush (new "Core Ethiopia" family)**
- Coffee Review cupping, Oct 2023: Sidra 7 samples avg 93 (low 91, high 95; three scored 95); Chiroso 5 samples avg 89 (84-94, top lot GK Coffee El Roble Chiroso washed 94, "flowers edging toward herb"); Pink Bourbon 3 samples avg 90 (89-92); Wush Wush 10 samples avg 88 (81-93) — [Coffee Review: New Coffee Varieties](https://www.coffeereview.com/new-coffee-varieties/)
- Genetics: per Christophe Montagnon of RD2 Vision, Sidra, Chiroso and Pink Bourbon are in a "Core Ethiopia" genetic group with no relationship to Bourbon or Typica — same Coffee Review page. Other claims conflict: Sey Coffee pages say Ethiopian landrace in one place and a Bourbon x Ethiopian landrace cross (citing WCR testing) in another — [Sey Coffee Cruz Loma](https://www.seycoffee.com/products/cruz-loma); [Sey Miguel Dota](https://seycoffee.com/products/2025-miguel-dota-ecuador). A Royal Coffee listing says Sidra "does not yet exist" in the WCR catalog — [Royal Coffee](https://royalcoffee.com/?p=826035). I confirmed Sidra is absent from the WCR index of 70 arabica varieties.
- Sidra origin: popular story of a Nestle breeding facility in Pichincha, Ecuador (possibly 1990s), Ethiopian and Bourbon material; Don Olger Rogel credited with introducing it to Ecuador — [Ozone Coffee: Sidra](https://ozonecoffee.co.uk/blogs/varietals/coffee-varietal-sidra) [UNVERIFIED story, genetics disputed]. Coffee Review: Sidra first selected in Colombia or neighbouring Ecuador.
- Sidra cup: floral and fruit complexity; lots described as jammy and chocolate-toned (Chromatic Finca El Diviso), floral with bright acidity (Euphora Ecuador), balanced flower and cocoa (Kakalove Las Flores) — [Coffee Review](https://www.coffeereview.com/new-coffee-varieties/)
- Wush Wush: Ethiopian origin, brought to Latin America (mainly Colombia) "about 25-30 years ago"; compared with Panama Gesha, wild rose, stone fruit, herbal — [Origin Coffee Roasters](https://www.origincoffee.co.uk/blogs/journal/wush-wush-coffee); [Sweet Maria's Wush Wush lot](https://www.sweetmarias.com/products/colombia-edward-sandoval-wush-wush-8590) [UNVERIFIED roaster sources]
- Pink Bourbon cup: floral, tropical fruit, bright acidity, silky finish — [Colipse Coffee](https://colipsecoffee.com/blogs/coffee/pink-bourbon) [UNVERIFIED roaster source]
- Chiroso: most likely a Caturra mutation planted around Urrao, Colombia (sometimes "Chiroso Caturra"); but Coffee Review/Montagnon says Core Ethiopia group, so the Caturra-mutation claim conflicts — [Coffee Review: Chiroso reviews](https://www.coffeereview.com/new-coffee-varieties/) [conflict flagged]

**Ethiopian landraces and JARC selections**
- 74110: JARC selection from a mother tree at Bishari, Illubabor, 1970s, cataloged 1974; CBD resistance, high yield, fruity profile — [19grams 74110](https://19grams.coffee/en/blogs/kaffeelexikon/74110-varietat); Sample Coffee 74110 notes "treacle, dried pineapple, apricot (black)" — [Sample Coffee](https://cdn.samplecoffee.com.au/coffee/varietals/74110) [UNVERIFIED roaster sources]
- 74112: from Metu Bishari forest, selected for CBD resistance and high yield — [Green Coffee Collective JARC glossary](https://glossary.greencoffeecollective.com/coffee-varieties-and-genetics/jarc-varietals) [UNVERIFIED]
- 74158: sources disagree on main trait. Green Coffee Collective says leaf-rust resistance and high-altitude adaptation; an SCA-prep study guide groups it with 74160 as CBD-resistant selections from wild mother trees in Illubabor/Metu forests — [Green Coffee Collective](https://glossary.greencoffeecollective.com/coffee-varieties-and-genetics/jarc-varietals); [open-exam-prep SCA guide](https://open-exam-prep.com/study-guides/sca-q-grader/coffee-geography-terroir-origins/east-african-terroirs) [UNVERIFIED, low-authority]
- Kurume: called Kurume in Yirgacheffe area and Kudhum in Guji; heirloom/landrace sub-variety — [Sample Coffee Kurume](https://cdn.samplecoffee.com.au/coffee/varietals/kurume) [UNVERIFIED]
- Classification dispute: some sources call 74110/74112 landrace-derived heirloom, others JARC selections distinct from landraces; I found no JARC primary source.

**Lineage and dates from Daily Coffee News/Royal Coffee guide (pre-WCR synthesis)**
- Gesha: wild Ethiopian forest coffee; collected 1931; CATIE 1953; Best of Panama 2004; CATIE site (600 m) poor — [Daily Coffee News guide](https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/)
- Java: selected from Ethiopian trees, 1928 (Indonesia, as Abyssinia), same page.
- Ruiru 11: SL28, SL34, Sudan Rume, Bourbon, Catimor parentage; rated lower than SLs, acidity and body favoured over sweetness — same page.
- Batian: Ruiru 11 material, F5, 2010 — same page.
- Mundo Novo: observed 1943; selection 1977; Catuai released 1970s — same page (WCR gives release 1972 for Catuai and distribution from 1952 for Mundo Novo).
- Sarchimor group: Villa Sarchi x Timor Hybrid (IAPAR 59, Obata) — same page.
- Catimor group: Timor Hybrid x Caturra, to Brazil 1967; Costa Rica 95 and Cat 129 improved selections — same page.
- Centroamericano: F1 Sarchimor x Sudan Rume — same page; Milenio (H10) cupped at 92 in a Costa Rica Las Lajas lot (Fulcrum) — [Coffee Review](https://www.coffeereview.com/new-coffee-varieties/)

**Cup-score data points (single lots, Coffee Review 2023; small n, treat as illustration)**
- Java (El Roble, Colombia, Corvus): 95, "clean, intense sweetness, cocoa, rich berry" — [Coffee Review](https://www.coffeereview.com/new-coffee-varieties/)
- SL28 (El Injerto, Guatemala, Equator): 94, "pungent, resinous note that sweetens into mango and lavender" — same page.
- Milenio: 92 — same page.

### Inferences
- [INFERRED] For `rust_resistance`, normalise WCR to a 4-level enum: susceptible (Low), intermediate, highly resistant; add a `rust_note` for context-dependent cases (S795 resistant in trials but susceptible in India; Lempira susceptible in Honduras; Parainema resistance may change as races evolve).
- [INFERRED] Because WCR catalog uses latitude-banded altitude, an `altitude_min_masl` value is only meaningful with a `latitude_band` field; otherwise store the 5-15 degree value and flag.
- [INFERRED] The Timor-Hybrid derived group (Catimor, Sarchimor, Ruiru 11, Batian, Centroamericano, Starmaya, Marsellesa, Parainema, Lempira, Obata, Castillo, Colombia, Cat129, Icatu with a robusta-derived background) can be labelled "Introgressed/hybrid"; Starmaya, Centroamericano, Milenio, Ruiru 11 are labelled F1 in WCR.
- [INFERRED] The new "Core Ethiopia" group (Sidra, Chiroso, Pink Bourbon, possibly Wush Wush) is not in WCR's group scheme; propose a label "Ethiopian-derived (Core Ethiopia), disputed" pending WCR/genomic confirmation.
- [INFERRED] Java is listed as "Ethiopian landrace" by WCR, but Gesha's WCR card group is "Gesha"; for labelling, treat both as `Ethiopian landrace` with `subgroup` = Gesha.

### Gaps
- WCR has no pages (fetched or listed) for Colombia, Castillo, Tabi, Kent, Sudan Rume, Pink Bourbon, Sidra, Wush Wush, Chiroso, Maracaturra, Icatu, Arusha, Mokka, Laurina, 74110/74112/74158, Kurume. Their rows rely on secondary sources.
- WCR has no explicit acidity/body/sweetness fields; I have no consistent sensory rating per variety (WCR, SCA or CoE) for most rows.
- Sample Coffee varietals page and Castillo GCR article returned HTTP 403; not read directly.
- Yield in kg/ha or sacks/ha not available (WCR gives categories only).
- Altitude max not available from WCR.
- WCR pages list multiple unlabeled option values on Mundo Novo, Java, SL34; confirm against the live page.
- Eugenioides, Liberica-excelsa "varieties": handled as species only above; no WCR variety page.
- Red/yellow/orange Bourbon colour variants: not researched in depth.
- Hoffmann's "World Atlas of Coffee" not consulted (no accessible text).

---

## 3. Quality premium and price context (cupping scores, auction records, variety vs terroir vs processing)

### Takeaway
Best of Panama Gesha prices have gone from $21/lb (2004) to $601/lb (2017), $803 (2018), $1,029 (2019), $4,542 (2024) and an all-time record of $30,204/kg (about $13,705/lb) on 6-7 Aug 2025, for a 98-point washed Gesha from Hacienda La Esmeralda; Cup of Excellence records are far lower (top CoE Ethiopia lot 2022: $400.50/lb). I found no Sidra auction record. No study partitions flavour by percent between variety, terroir and processing; evidence is qualitative.

### Cited Findings

**Best of Panama (Gesha) top-lot history**

| year | top lot price | estate / process / buyer | score | source_url |
|---|---|---|---|---|
| 2004 | $21/lb (then record) | Hacienda La Esmeralda (Peterson family); Gesha first introduced to the market | not found | https://en.wikipedia.org/wiki/Geisha_coffee ; https://www.coffeereview.com/new-coffee-varieties/ |
| 2005 | $350/lb ($770/kg) listed by Wikipedia as a "record"; WCR says the 2005 entry set a "record of over $20/pound" | Peterson family (Boquete) | not found | https://en.wikipedia.org/wiki/Geisha_coffee ; https://varieties.worldcoffeeresearch.org/varieties/geisha-panama [CONFLICT: dates and amounts do not reconcile; 2004 vs 2005 first entry] |
| 2017 | $601/lb | Hacienda La Esmeralda, "Rod green" natural | not found | https://dailycoffeenews.com/2017/07/26/record-coffee-earns-601-per-pound-at-best-of-panama-auction |
| 2018 | $803/lb | Elida Estate (Lamastus Family Estates), natural | not found | https://dailycoffeenews.com/2018/07/20/natural-geisha-breaks-best-of-panama-auction-record-at-803-per-pound |
| 2019 | $1,029/lb | Elida Estate (Lamastus), natural; second place Esmeralda Special Jaramillo washed $233/lb to Campos Coffee | not found | https://www.beanscenemag.com.au/elida-estate-natural-asd-geisha-makes-best-of-panama-auction-history-at-us1029-per-pound |
| 2020-2023 | not found | not found | | (gap) |
| 2024 | $4,542/lb (about $10,013/kg); weighted average $627.27/lb; total over US$1.38 M; 50 lots all at least $200/lb | Lamastus Family Estates, natural Gesha, to a consortium led by Saza Coffee (Tokyo); second lot Adaura Coffee washed $4,537/lb same buyer | not reported | https://dailycoffeenews.com/2024/08/15/best-of-panama-shatters-price-records-with-627-per-pound-average ; [CONFLICT: GCR summary calls the 2024 top lot "washed"] https://www.gcrmag.com/best-of-panama-auction-sees-world-record-price |
| 2025 (6-7 Aug) | $30,204/kg = $13,705/lb; 20 kg lot, $604,080 total; 549 bids | Hacienda La Esmeralda, washed Gesha ("Canvas of Terroir" theme), buyer Julith Coffee, Dubai | 98 (highest ever at BoP) | https://sprudge.com/a-panama-gesha-broke-price-records-again-390362.html ; https://www.gcrmag.com/best-of-panama-auction-sees-world-record-price ; https://magazine.coffee/blog/1/6985/new-record-breaking-high-price-paid-at-best-of-panama-auction-2025 |
| 2025 natural | $23,608/kg; 20 kg; to JD.com | Hacienda La Esmeralda natural | 97 | https://sprudge.com/a-panama-gesha-broke-price-records-again-390362.html |

- 2025 auction totals: about US$2.8 million; weighted average $2,861/kg (GCR cites $2,861.20); 28 of 40 Gesha lots at the 2025 Panama Cup of Excellence sold above $1,000/kg — [Sprudge](https://sprudge.com/a-panama-gesha-broke-price-records-again-390362.html); [GCR](https://www.gcrmag.com/best-of-panama-auction-sees-world-record-price)
- 2019 "Elida Natural Geisha 1029" Wikipedia notes a 100-lb lot sold for $100,000; Wikipedia gives the 2024 figure as the record before 2025 only implicitly — [Wikipedia Geisha coffee](https://en.wikipedia.org/wiki/Geisha_coffee)
- 2026: no confirmed Best of Panama 2026 results found. Hacienda La Esmeralda's separate private auction in 2026 reportedly had a top natural Geisha "Tumaco Carnaval" at $10,253/kg and a record average of $5,745/kg (real-estate blog, low authority) — [Casa Solution](https://casasolution.com/boquete-geisha-sets-a-record-average-price-of-5745-per-kilo-at-the-2026-esmeralda-auction/) [UNVERIFIED]. A Sept 2026 EFE item mentions the 30th anniversary of BoP with a 750 kg sale (US$3 M+ in headline); per-lot results not seen — [Revista E&N](https://www.revistaeyn.com/centroamericaymundo/subasta-de-750-kg-de-cafe-de-panama-recauda-mas-de-us-3-millones-JF32152931) [UNVERIFIED, headline only].
- The 2025 "Panama Geisha" trademark push (Panama seeks global trademark protection) — [Qahwa World](https://backend.qahwaworld.com/tag/coffee-trademark/) [UNVERIFIED context]

**Cup of Excellence and other auction records**
- Ethiopia CoE 2022: top lot $400.50/lb, highest price ever paid for a CoE-winning green coffee; previous CoE record was a honey-process Gesha from Costa Rica in 2018 at $300.09/lb — [Daily Coffee News, Aug 2022](https://dailycoffeenews.com/2022/08/31/ethiopia-sidama-coffee-breaks-cup-of-excellence-record-at-400-50-lb)
- Ethiopia CoE 2021: record average $32.12/lb (previous $28.44 in 2020); top lot US$330/kg to Saza Coffee (Tokyo), about $150/lb; 2020 top lot was $185.10/lb — [GCR](https://gcrmag.com/cup-of-excellence-breaks-record-after-record); [Daily Coffee News 2021](https://dailycoffeenews.com/2021/06/07/colombia-cup-of-excellence-auction-breaks-all-time-average-high-at-30-lb) [UNVERIFIED: variety of top lots not given]
- Ecuador CoE 2021 (inaugural): top lot Typica Mejorado $97.10/lb; 23 lots averaged $33.55/lb; a honey Sidra placed 20th at $29/lb — [Daily Coffee News, Dec 2021](https://dailycoffeenews.com/2021/12/07/inaugural-ecuador-cup-of-excellence-auction-results-in-record-breaking-price-per-pound). This is the closest Sidra price I found; no Sidra record found.
- Ecuador Farmers Collection auction (ACE/QIMA, March 2026): washed Imbabura Gesha $318/kg, new high for an Ecuadorian coffee; Sidra Bourbon led with 10 lots but price not found — [Direct Coffee](https://directcoffee-shop.pages.dev/the-spilt-beans/2026-03-01-ecuador-farmers-collection-auction-geisha-winner); [Daily Coffee News Apr 2026](https://dailycoffeenews.com/2026/04/03/weekly-coffee-news-record-setting-ecuador-auction-new-nkg-coffee-council/)
- Sidra competition record: 2022 Ecuador CoE 3rd place (Sey Coffee lot); World Barista Championship wins (reported twice) and a World Brewers Cup title — [Ozone Coffee](https://ozonecoffee.co.uk/blogs/varietals/coffee-varietal-sidra) [UNVERIFIED, retailer]
- 2024 Ecuador CoE national winner (Loja) was a Sidra — [The Way to Coffee](https://www.thewaytocoffee.com/beans/ecuador-la-marquesa-by-ximena-leon-sidra-2024-17-coe-national-winners)

**Typical cupping score by variety**
- Gesha at Best of Panama: 97-98 for the top two 2025 lots (cited above). The brief's "88-94 in auctions" has no direct source; the lower end of that band is not supported by retrieved material. [Do not use 88-94 as a sourced value]
- Coffee Review 2023 averages (small n): Sidra 93, Pink Bourbon 90, Chiroso 89, Wush Wush 88, Maracaturra 91 (2 samples, context unverified), Java 95 (1 sample), SL28 94 (1 sample), Milenio 92 (1 sample) — [Coffee Review](https://www.coffeereview.com/new-coffee-varieties/)
- Stenophylla 80.25 (one tasting) — [Sci.News](https://www.sci.news/biology/coffea-stenophylla-09573.html)
- Coffee Review is a roaster-submitted review with its own 100-point scale, not SCA/CQI cupping; do not treat as SCA scores.

**Variety vs terroir vs processing**
- No retrieved study gives percent contributions. A 2024 Beverages study using linear mixed models on Coffee Quality Institute data found variety effects interact with process (e.g. Bourbon and Pacamara better under natural/dry processing, per its summary) — [Beverages 2024 / DOAJ](https://doaj.org/article/5537d53b9fa64b9e9ba87c5c3eb5553b) [UNVERIFIED: abstract relayed via search]
- A 2025 PMC study of Geisha from different production zones in Panama found regional differences in sensory and physicochemical traits within a single variety, i.e. terroir matters even for Gesha — [PMC12645158](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12645158/)
- A 2025 review argues terroir should include post-harvest processing because it is often environment-dependent — [Katalog CAS: Does coffee have terroir](https://katalog.lib.cas.cz/KNAV/EdsRecord/cmedm,35804722) [UNVERIFIED]
- Competition analysis: no single variety guarantees exceptional quality — [Coffee Bros](https://coffeebros.com/blogs/coffee/the-state-of-specialty-coffee) [UNVERIFIED low authority]
- WCR on Gesha: "quality depends on elevation, rainfall, and soil"; at CATIE (about 600 m) it was poor — [Daily Coffee News guide](https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/); WCR recommends >1,600 m near the equator — [WCR Geisha](https://varieties.worldcoffeeresearch.org/varieties/geisha-panama)

### Inferences
- [INFERRED] The post-2023 price jump is about 3x year over year (2024 to 2025 per-kg: $10,013 to $30,204) driven by a single washed lot; weighted averages rose from $627/lb (2024) to about $1,298/lb (2025: $2,861/kg divided by 2.2046) — [INFERRED conversion].
- [INFERRED] Store auction prices in USD per kg AND per lb (1 kg = 2.20462 lb), and include `process`, `auction` and `year`; do not average across auction types (BoP vs CoE vs private estate auctions).
- [INFERRED] Because evidence says terroir and process interact with variety, the tool's flavour prediction should treat variety as a prior (e.g. Gesha floral, SL28 blackcurrant/mango, Marsellesa/Starmaya high acidity) with process and altitude as modifiers; no weights can be sourced.

### Gaps
- Best of Panama top lots for 2020-2023 not retrieved (I only found 2004, 2005, 2017, 2018, 2019, 2024, 2025).
- 2026 Best of Panama official results not found.
- No Sidra auction record price found; Sidra CoE record not identified.
- No sourced SCA cupping range per variety; WCR provides qualitative potential only.
- No variance-partitioning study found that quantifies variety vs terroir vs processing.
- The brief's "Gesha 88-94 in auctions" not directly sourced.

---

## 4. Genetic groups for labelling

### Takeaway
WCR's catalog assigns each variety to one of: Bourbon-Typica group (with sub-tags Bourbon related / Typica related / both), Ethiopian landrace, Gesha (card label), Introgressed (sub-tags Sarchimor, Catimor, Other), or F1 hybrid; use these as the label vocabulary and map non-WCR varieties by lineage.

### Cited Findings
- WCR group labels seen on individual pages: "Bourbon-Typica group (Typica related / Bourbon related / Typica and Bourbon related)" for Typica, Bourbon, Caturra, Catuai, Mundo Novo, Pacas, Pacamara, Maragogipe, Villa Sarchi, Tekisic, SL28, SL34; "Ethiopian landrace" for Geisha (Panama) and Java; "F1 hybrid (introgressed)" for Ruiru 11, Centroamericano, Starmaya; "Introgressed (Sarchimor related)" for Marsellesa, Parainema, Obata; "Introgressed (Catimor related)" for Lempira, Catimor 129; "Introgressed (Other)" for Batian, S795 — individual WCR pages cited in Section 2a, e.g. [Typica](https://varieties.worldcoffeeresearch.org/varieties/typica), [Batian](https://varieties.worldcoffeeresearch.org/varieties/batian)
- WCR index-card lineage labels (separate from page group): Java (AB3, BPL10), Catimor (Anacafe 14, Catisic, Costa Rica 95, Fronton, IHCAFE 90, Lempira, Oro Azteca, T5175, T8667), Sarchimor (Cuscatleco, IAPAR 59, Limani, Marsellesa, Obata, Parainema, T5296), Jackson (Jackson 2/1257), Improved Bourbon (Tekisic), Gesha (Geisha), Rootstock (Nemaya, C. canephora) — [WCR index](https://varieties.worldcoffeeresearch.org/arabica/varieties)
- Typica and Bourbon descend from Yemeni landraces; nearly all cultivated arabica descends from a handful of wild Yemeni plants; plantations hold under 1% of wild diversity — [Daily Coffee News guide](https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/); [Wikipedia C. arabica](https://en.wikipedia.org/wiki/Coffea_arabica)
- Timor Hybrid origin and Catimor/Sarchimor derivation — [Daily Coffee News guide](https://dailycoffeenews.com/2019/02/07/the-coffee-roasters-complete-guide-to-coffee-varieties-and-cultivars/)
- Catalog also includes a robusta rootstock (Nemaya) used for nematode-resistant grafting — [WCR index](https://varieties.worldcoffeeresearch.org/arabica/varieties)

### Suggested group vocabulary [INFERRED]
- `typica_group` (Typica, Maragogipe, SL34 per WCR "Typica related")
- `bourbon_group` (Bourbon, Caturra, Pacas, Villa Sarchi, Tekisic, SL28, Laurina, Pink Bourbon only if "pink Bourbon" genetics resolved)
- `typica_bourbon_cross` (Mundo Novo, Catuai, Pacamara, Maracaturra, Tabi)
- `ethiopian_landrace` (Gesha, Java, 74110/74112/74158, Kurume, Sudan Rume, Wush Wush; disputed: Sidra, Chiroso, Pink Bourbon)
- `introgressed_timor` (Catimor, Sarchimor, Castillo, Colombia, Icatu, Batian)
- `f1_hybrid` (Centroamericano H1, Milenio H10, Starmaya, Ruiru 11 per WCR)

### Inferences
- [INFERRED] WCR places Batian under "Introgressed (Other)" and Ruiru 11 as an F1 hybrid; to keep the label set to the four in the brief (Typica, Bourbon, Ethiopian landrace, Introgressed, F1), add `Gesha` as a subgroup of Ethiopian landrace and `Bourbon-Typica cross` as an explicit combined value.
- [INFERRED] The three "Core Ethiopia" varieties (Sidra, Chiroso, Pink Bourbon) should carry a `group_confidence = low` flag given conflicting genetic claims.

### Gaps
- Official WCR definitions of the group labels (a glossary page) not retrieved; groups are read off individual pages.
- Sudan Rume classification (landrace vs Ethiopian-type) varies by source.
- Maracaturra, Tabi, Icatu parentage only from secondary sources.
