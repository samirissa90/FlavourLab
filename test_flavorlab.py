"""Smoke checks for the flavor model: python test_flavorlab.py"""
import model as fl

db = fl.DB()
assert len(db.items) > 250

# heat character: habanero builds later and lingers longer than bird's eye
q = lambda spec, **kw: fl.analyze(db, fl.normalize_recipe({"ingredients": fl.parse_quick(spec), **kw}))  # noqa: E731
hab, bird = q("habanero:100,vinegar:100"), q("thai bird's eye:100,vinegar:100")
assert hab["heat_profile"]["peak_s"] > bird["heat_profile"]["peak_s"]
assert hab["heat_profile"]["zones"]["back"] == 1.0

# finish stage protects top notes; cooking loses them
cooked, finished = q("lime juice:50,vinegar:100"), q("lime juice:50:finish,vinegar:100")
assert finished["perceived"]["citrus"] > cooked["perceived"]["citrus"]
assert q("lime juice:50,vinegar:100", process="raw")["pyramid"]["processed"]["top"] > cooked["pyramid"]["processed"]["top"]

# xanthan thickens; fat & sugar soften astringency
assert q("vinegar:100,xanthan gum:0.3")["body"] > q("vinegar:100")["body"]
assert q("hibiscus:50,vinegar:100,butter:40")["perceived"]["astringent"] < q("hibiscus:50,vinegar:100")["perceived"]["astringent"]

# sichuan peppercorn tingles
assert q("sichuan peppercorn:5,neutral oil:95")["perceived"]["numbing"] > 1

# pairing: classic beats clash, shared families are reported
assert fl.pair_score(db, db.get("habanero"), db.get("mango")) > fl.pair_score(db, db.get("habanero"), db.get("fish sauce"))
assert fl.pair_score(db, db.get("cumin"), db.get("cinnamon"), explain=True)["shared_families"]


# bitter x astringent: not stacked when both share the traits, kept when one is bitter and the other astringent
def clash(bitter_a, astr_a, bitter_b, astr_b):
    a, b = db.get("cumin"), db.get("cinnamon")
    va, vb = a.vec * 0, b.vec * 0
    va[fl.VI["bitter"]], va[fl.VI["astringent"]] = bitter_a, astr_a
    vb[fl.VI["bitter"]], vb[fl.VI["astringent"]] = bitter_b, astr_b
    return fl.pair_score(db, a, b, va, vb, explain=True)["clash"]


assert clash(8, 4, 8, 4) == round((0.6 * 64 + 0.4 * 16) / 100, 2)
assert clash(8, 0, 0, 4) == clash(0, 4, 8, 0) == round(0.3 * 32 / 100, 2)
print("ok")
