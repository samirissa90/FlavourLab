---
name: flavorlab
description: Generic flavor pairing rules and proven ingredient pairings from the FlavorLab project. Use when asked which ingredients pair well, why two ingredients work together, how to bridge two flavors, how to balance heat/sweet/sour/fat in a sauce or dish, or how to score a pairing. Triggers: 'pairing', 'pairs with', 'goes with', 'flavor bridge', 'flavor pairing', 'chili pairing', 'sauce balance', 'harmony score'.
---

# FlavorLab Pairing

Use these rules to suggest or judge ingredient pairings. All numbers are heuristic 0-10 or 0-1 estimates from `model.py`, not lab data. For ingredient-specific answers, run the CLI rather than guessing.

## Run the tools

```bash
python flavorlab.py pair habanero                      # pairing wheel for one ingredient
python flavorlab.py pair habanero --with mango         # score + why they pair
python flavorlab.py bridge "kenyan coffee" chipotle    # ingredients that link two others
python flavorlab.py families                           # aroma families with example ingredients
python flavorlab.py info NAME                          # one ingredient's profile
```

Add `--json` to `pair` or `bridge` for machine-readable output. Pairs with an ingredient that is not in the CSV packs are skipped.

## How a pair is scored

```
raw   = 0.25·aroma_sim + 0.20·profile_cos + 0.25·taste_contrast + 0.30·category_affinity
        − clash + 0.20·(classic pair?)
score = 100 · tanh(1.2 · max(0, raw))          # 0-100
```

- **aroma_sim** = 0.6 × cosine of aroma-family vectors (exact family) + 0.4 × cosine of family-group vectors (same group). Full credit for a shared family, partial for a shared group.
- **profile_cos**: cosine of the nine aroma axes.
- **taste_contrast**: contrast pairs that complement each other (below), capped at 1.
- **category_affinity**: how well the two kitchen roles fit (table below).
- **clash**: penalties when both ingredients are strong in the same harsh trait.
- **classic**: a bonus for the proven pairings listed below.

### Contrast pairs (weight)

Two ingredients that differ on these axes balance each other.

| Pair | Weight | Pair | Weight |
|---|---|---|---|
| sweet – sour | 1.0 | fruity – heat | 0.7 |
| sweet – heat | 0.8 | fat – heat | 0.6 |
| salty – bitter | 0.8 | numbing – heat | 0.6 |
| sweet – salty | 0.6 | sweet – bitter | 0.5 |
| umami – sour | 0.6 | sour – fat | 0.5 |
| cooling – heat | 0.4 | sweet – astringent | 0.4 |
| fat – astringent | 0.4 | | |

### Clash penalties (weight × product of both ingredients' strength)

| Clash | Weight |
|---|---|
| bitter × bitter | 0.6 |
| astringent × astringent | 0.4 |
| pungent × pungent | 0.3 |
| smoky × floral | 0.3 |
| bitter × astringent | 0.3 |
| sinus × floral | 0.2 |

### Category affinity (0-1)

Categories: chili, fruit, veg (incl. allium), acid, savory (fat and base), sweet, herb, spice. Lookup is symmetric. Any pair not listed scores 0.4.

| | chili | fruit | veg | acid | savory | sweet | herb | spice |
|---|---|---|---|---|---|---|---|---|
| **chili** | .70 | .75 | .85 | .85 | .70 | .65 | .60 | .60 |
| **fruit** | | .60 | .40 | .80 | .35 | .60 | .60 | .60 |
| **veg** | | | .70 | .60 | .75 | .40 | .70 | .70 |
| **acid** | | | | .30 | .60 | .70 | .60 | .40 |
| **savory** | | | | | .50 | .60 | .50 | .60 |
| **sweet** | | | | | | .20 | .40 | .70 |
| **herb** | | | | | | | .50 | .40 |
| **spice** | | | | | | | | .60 |

### Aroma family groups

fruity (ester, lactone, thiol_trop, ionone) · citrus · floral · green · herbal · spice · roast · smoke · sulfur · ferment · earthy. Ingredients in the same group share an aroma story even when the exact family differs.

## Design principles

Use these when building a pairing from scratch, not just checking one.

- **Heat needs a counterweight.** Sugar, fat (dairy is the classic heat-tamer) and menthol damp capsaicin. Acid sharpens it. Heat above about 6 masks fruity, floral, citrus and herbal notes, so keep the heat under that when you want fruit to show.
- **Layer the heat zones.** Blend a front-of-mouth chili (Thai bird's eye, chiltepin) with a back-of-mouth chili (habanero, ghost pepper) for full coverage.
- **Balance sweet and sour.** Sugar and acid mask each other. Fruit plus lime is the most reliable starting point.
- **Salt cuts bitterness and boosts umami.** Use it to tame bitter notes from coffee, cacao or greens.
- **Match smoke with roast.** Smoke and roast families overlap, which is why chipotle works with espresso, honey and dark chocolate.
- **Top notes go in at the finish.** Citrus juice and zest, fresh herbs and passion fruit lose most of their aroma under heat. Dried or smoked base notes survive cooking.
- **Ferment to add depth.** Fermenting chili, fruit, vegetables or herbs raises esters, terpenes and acids.
- **Astringency softens with fat, sugar and salt, and sharpens with acid.** Watch tannin-heavy ingredients (hibiscus, cacao, coffee, tea) next to bitter ones.
- **Body:** pulp (mango, banana, carrot, tomato paste, dates) thickens; vinegar and juice thin. Xanthan at 0.1-0.3% stops separation.

## Classic pairings

These get the +0.2 classic bonus. Each pair only counts when both ingredients exist in the database.

**Chili with fruit**
- habanero – mango, pineapple, passion fruit, peach, apricot, lime juice, carrot
- scotch bonnet – allspice, thyme, mango, pineapple, scallion
- ghost pepper – mango; carolina reaper – mango
- banana – scotch bonnet; guava – habanero; sour orange – habanero
- piri piri – lemon juice; aji amarillo – lime juice, garlic

**Chili with herb, acid and spice**
- jalapeño – cilantro, lime juice
- serrano – cilantro, tomatillo; tomatillo – cilantro
- ancho – cinnamon, cacao nibs, espresso, dark chocolate, mulato
- guajillo – garlic, cumin; chile de árbol – garlic; smoked paprika – garlic
- thai bird's eye – fish sauce, garlic
- gochugaru – garlic; miso – gochugaru; gochujang – toasted sesame oil
- pepitas – hatch green chile; aji panca – aji amarillo; harissa – preserved lemon
- sichuan peppercorn – chili crisp; doubanjiang – sichuan peppercorn; black vinegar – chili crisp; sansho – yuzu juice

**Smoke, chocolate and coffee**
- chipotle – honey, maple syrup, garlic, orange juice, espresso, bourbon, mezcal, black garlic
- ancho – espresso, cacao nibs, dark chocolate
- espresso – cardamom, orange zest, cacao nibs
- lapsang souchong – dark chocolate; urfa biber – cacao nibs
- ethiopian natural coffee – blueberry; kenyan coffee – blackcurrant

**Fruit with acid, spice and sweet**
- mango – lime juice; passion fruit – lime juice; pineapple – cilantro, dark rum
- strawberry – black pepper, basil; raspberry – cacao nibs; sour cherry – cacao nibs
- peach – ginger; tomato – basil; hibiscus (dried) – ginger
- tequila – lime juice; matcha – yuzu juice; honey – lemon juice; datil – honey

**Aromatics and savory**
- ginger – garlic, lime juice; lemongrass – kaffir lime leaf, galangal
- fish sauce – lime juice, palm sugar; garlic – cumin; cumin – coriander seed
- tamarind paste – dates, ginger, jaggery; black garlic – chipotle
- kombu – katsuobushi; yuzu juice – yuzu kosho; sour orange – achiote
- berbere – fenugreek; dried lime – fenugreek; bourbon – chipotle

## Answering a pairing question

1. Look up the pair with `pair A --with B` if both ingredients are in the database. Report the score and the shared families.
2. If the pair is classic, say so and name the reason (shared family, contrast, or both).
3. If the pair scores low, name the clash or the missing contrast, then suggest a bridge (`bridge A B`) or a fix (add a fat, sugar or acid to soften the clash).
4. For a full dish or sauce, check heat balance, sweet and sour balance, and whether top-note ingredients are at the finish.

## Extending the pairings

Add a `("ingredient A", "ingredient B")` tuple to `CLASSIC` in `model.py`. Names are normalized (lowercase, underscores become spaces). Retune the category table in `_AFF` or the weights in `pair_score()` only when the change is justified, since they affect every pair.
