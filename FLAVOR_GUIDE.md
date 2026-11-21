# FlavorLab flavor guide (v0.2)

This guide explains the flavor science behind the numbers in `ingredients.csv`. All values are heuristic 0-10 estimates, set by hand from food-science sources; they are not lab data. To list the families with example ingredients, run `python flavorlab.py families`.

## 1. Three layers of flavor
| Layer | Senses it | FlavorLab axes |
|---|---|---|
| Taste | taste buds | sweet, sour, salty, bitter, umami (+ heat, from SHU) |
| Aroma | nose (smelled directly and from the back of the mouth while eating) | 9 broad axes + 30 aroma families |
| Chemesthesis (trigeminal) | touch and pain nerves | astringent, cooling, numbing, sinus, bite |

Chemesthesis is the "chemical touch" sense. Each of its sensations has its own receptor:
- **Capsaicin heat** (TRPV1)
- **Menthol cooling** (TRPM8)
- **Mustard, horseradish and wasabi, garlic, and cinnamaldehyde** (TRPA1)
- **Sichuan pepper's tingling numbness** (hydroxy-α-sanshool, which acts on potassium channels)

These are different sensations, so v0.2 moved them off the "pungent/allium" aroma axis:
- **sinus:** volatile isothiocyanates that go up the nose and fade quickly
- **bite:** piperine, gingerols and allicin; an oral burn
- **numbing:** sanshools; tingling that lasts minutes

## 2. Aroma families (30, in 12 groups)
| Group | Families (descriptor, example markers) |
|---|---|
| fruity | **ester** fruity esters (ethyl butanoate) · **lactone** peach/coconut (γ-decalactone) · **thiol_trop** tropical/blackcurrant (3-mercaptohexanol) · **ionone** violet/berry/tea (β-ionone, damascenone) |
| citrus | **citrus_terp** (limonene, citral) |
| floral | **floral_terp** (linalool, geraniol) · **rose** (2-phenylethanol) |
| green | **green_c6** cut grass (hexenal) · **mpyrazine** green bell pepper (methoxypyrazine) · **fatty_ald** cucumber/cilantro (decenal, nonadienal) |
| herbal | **cineole** eucalyptus · **menthol_carvone** mint/caraway · **thymol** thyme/oregano · **pine** resin (pinene, myrcene) |
| spice | **eugenol** clove · **anethole** anise · **spice_ald** cinnamon/cumin/almond · **vanillin** · **sesqui** woody-peppery (rotundone) |
| roast | **furanone** caramel/maple (furaneol, sotolon) · **pyrazine** nutty roast · **thiol_roast** coffee (2-furfurylthiol) |
| smoke | **smoke_phenol** (guaiacol) |
| sulfur | **allium** garlic/onion · **itc** mustard/horseradish |
| ferment | **ferm_acid** cheesy/funky · **marine** briny/dried seafood · **acetic** vinegar |
| earthy | **earthy_root** (geosmin) · **mushroom** (1-octen-3-ol) |

**How pairing uses families.** The pairing score gives full credit when two ingredients share the same family and partial credit when they share only a group. Some examples:
- **Chipotle + espresso** share smoke and roast.
- **Mango + habanero** share fruity esters and floral terpenes.
- **Kenyan coffee + blackcurrant** share tropical/blackcurrant thiols.

Aroma bridges can link ingredients that don't pair directly: `bridge A B` finds ingredients that share families with both.

**Chili aroma notes.** Most chili aroma research names a few compound classes:
- The habanero character comes from branched esters (for example 4-methylpentyl 3-methylbutanoate).
- Green chilis are dominated by 2-methoxy-3-isobutylpyrazine and (E)-2-nonenal.
- Fermentation increases esters and terpenes in chili mash.

## 3. Heat character (beyond Scoville)
The Chile Pepper Institute (New Mexico State University) profiles chili heat on five criteria: heat level, how fast it starts, how long it lasts, where it is felt and what it feels like. FlavorLab models three of these:
- **onset** (1 = instant … 5 = delayed)
- **length** (1 = fades fast … 5 = lingers)
- **zone** (front / mid / back)

Some reference chilis:
- **Thai bird's eye:** instant, front of the tongue, fades fast (1, 2, front)
- **Habanero:** delayed, back of mouth and throat, lingers for minutes (4, 4, back)
- **Ghost pepper:** long delay, long burn (5, 5, back)
- **New Mexican types:** mid-palate (2, 3, mid)
- **Chiltepin:** a "flash" that fades fast (1, 1, front)

**Design tip:** blend a front-zone chili with a back-zone chili to get a heat that covers the whole mouth.

**SHU vs. sauce heat.** Published pod ratings are dry-weight values. Fresh pods are about 88% water, so FlavorLab multiplies their SHU by about 0.12 (the `solids` column).

## 4. Volatility (top / middle / base notes)
- **Top notes** (citrus juice and zest, fresh herbs, wasabi and mustard, passion fruit) are lost quickly to heat and time.
- **Middle notes** (most fruit, fresh chili, vinegars, ground spices) partly survive.
- **Base notes** (dried and smoked chili, roast, caramel, ferments, sugars) are stable or even develop with cooking.

Research on cooked tomato products backs this up: heating lowers terpenes and raises compounds from fat oxidation and the Maillard reaction.

**Design tip:** add top-note ingredients at the **finish**.

## 5. Mouthfeel
- **Astringency:** tannins in hibiscus, cranberry, tea, cacao, coffee and red wine. Fat, sugar and salt soften it, and acid sharpens it.
- **Fat:** coats the mouth and damps capsaicin and bite. Dairy (casein) is the classic heat-tamer.
- **Body:** a thickness index.
  - Pulp (mango, banana, carrot, tomato paste, dates) thickens.
  - Liquids (vinegar, juice, water) thin.
  - Xanthan gum at 0.1-0.3% stabilizes the sauce and stops separation.

## 6. Interaction rules (in `perceive()`)
| Effect | Direction |
|---|---|
| Sugar ↔ acid | Each masks the other (sweet-sour balance). |
| Salt → bitterness | Suppressed. |
| Salt → umami | Boosted (synergy). |
| Acid → saltiness, heat | Both lifted. |
| Sugar, fat, menthol → heat | Damped. |
| Capsaicin → menthol cooling | Overridden. |
| Heat above 6 → fruity / floral / citrus / herbal | Masked. |
| Raw allium → floral | Masked. |
| Fat, sugar → astringency | Softened. |

## Sources (for the directions; magnitudes are hand-tuned)
- [America's Test Kitchen: Getting to know heat](https://www.americastestkitchen.com/how_tos/10850-getting-to-know-heat): habanero vs. Thai chile onset, location and duration; the NMSU heat-profile criteria.
- [Viana, chemosensory properties of the trigeminal system (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3369707): TRP channel targets of AITC, cinnamaldehyde, citral and sanshool.
- [Molecular mechanisms of trigeminal chemosensation (PubMed)](https://pubmed.ncbi.nlm.nih.gov/19686135/): capsaicin/TRPV1, menthol/TRPM8, wasabi/TRPA1, sanshool/KCNK18.
- [Chili pepper volatiles, Molecules 2022 (MDPI)](https://mdpi.com/1420-3049/27/7/2355): esters in C. chinense; aldehydes give green notes.
- [Qujiao 5 chili VOC analysis (EurekAlert)](https://eurekalert.org/news-releases/1052873): methoxypyrazine and (E)-2-nonenal as key chili odorants.
- [Fresh vs. fermented chili aroma (Food Science)](https://www.spkx.net.cn/EN/Y2022/V43/I6/309): fermentation raises esters and terpenes.
- [Thermal treatment of tomato products (ChemistryViews)](https://www.chemistryviews.org/?p=31419): heating lowers terpenes and raises Maillard and fat-oxidation volatiles.
