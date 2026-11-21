"""Headless smoke test for the Tk UI: python test_flavorlab_ui.py

Part A starts the UI on the real ingredient folder (read-only).
Part B drives every tab against a small fixture pack in a temp folder, so it never touches your CSVs/recipes."""
import csv
import glob
import json
import os
import shutil
import tempfile
import time
import tkinter as tk

import flavorlab_ui as ui
import model as M

REAL_HERE, REAL_RECIPES = M.HERE, ui.RECIPES_DIR
HEADER = open(os.path.join(REAL_HERE, "ingredients_v02.csv"), encoding="utf-8").readline().strip().split(",")
errors = []
root = tk.Tk()
root.withdraw()


def settle(app, timeout=240):
    t0 = time.time()
    while time.time() - t0 < timeout:
        root.update()
        if app._busy == 0 and app.designer._recalc_job is None:
            root.update()
            return
        time.sleep(0.02)
    raise TimeoutError("background work did not finish")


def write_pack(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=HEADER)
        w.writeheader()
        for r in rows:
            w.writerow({h: r.get(h, "") for h in HEADER})


# ---------------------------------------------------------------- Part A: real folder
app = ui.App(root)
n_real, n_issues = len(app.db.items), len(app.issues)
assert n_real > 0 and app.designer.ilist.get_children()
print(f"real folder: {n_real} ingredients loaded, {n_issues} invalid row(s) skipped")
app.designer.dirty = False
app.close()

# ---------------------------------------------------------------- Part B: fixture
tmp = tempfile.mkdtemp()
M.HERE = tmp
ui.RECIPES_DIR = os.path.join(tmp, "recipes")
os.makedirs(ui.RECIPES_DIR)
base = dict(solids="1", potency="1", heat_onset="2", heat_length="2", heat_zone="mid", volatility="m")
rows = [
    dict(base, name="habanero", category="chili", shu="250000", solids="0.12", fruity="6", citrus="1", floral="1",
         heat_onset="3", heat_length="3", aroma="thiol_trop:1;ester:1", aliases="hab"),
    dict(base, name="mango", category="fruit", sweet="6", sour="1", fruity="7", aroma="lactone:2;thiol_trop:1"),
    dict(base, name="apple cider vinegar", category="acid", sour="8", fruity="1", aroma="acetic:2"),
    dict(base, name="lime juice", category="acid", sour="7", citrus="7", aroma="citrus_terp:2", volatility="t"),
    dict(base, name="salt", category="savory", salty="10"),
    dict(base, name="water", category="savory", potency="0.3"),
    dict(base, name="garlic", category="veg", pungent="7", umami="1", aroma="allium:3"),
    dict(base, name="ginger", category="spice", warm="4", pungent="2", aroma="sesqui:2"),
    dict(base, name="honey", category="sweet", sweet="9", floral="2", aroma="rose:1"),
    dict(base, name="cilantro", category="herb", herbal="6", citrus="2", aroma="fatty_ald:2", volatility="t"),
    dict(base, name="carrot", category="veg", sweet="3", earthy="3", aroma="earthy_root:1"),
    dict(base, name="pineapple", category="fruit", sweet="5", sour="3", fruity="7", aroma="ester:2"),
]
write_pack(os.path.join(tmp, "ingredients_fixture.csv"), rows)
with open(os.path.join(ui.RECIPES_DIR, "mh.json"), "w") as f:
    json.dump({"name": "MH", "style": "fruity_caribbean", "fermented": ["habanero"],
               "ingredients": [{"item": "hab", "g": 100}, {"item": "mango", "g": 250},
                               {"item": "lime juice", "g": 30, "prep": "finish"}]}, f)

root = tk.Tk()
root.withdraw()
app = ui.App(root)
app.on_error = errors.append
d = app.designer
assert len(app.db.items) == len(rows) and not app.issues

# build a recipe the way the UI does
for name, g in (("habanero", 120), ("mango", 250), ("apple cider vinegar", 200), ("salt", 12)):
    d.add_ingredient(name, g)
d.add_ingredient("lime juice", 30)
d.rows[-1]["stage"] = "finish"
d.style_var.set(d._style_label("fruity_caribbean"))
d._meta_changed()
settle(app)
assert d.A is not None and 0 < d.A["overall"] <= 100 and d.sv["overall"].get() != "—"
assert "finish" in d.prep_text(d.rows[-1])

# undo
d.undo()
assert len(d.rows) == 4
d.add_ingredient("lime juice", 30)
settle(app)

# suggestions -> apply -> auto-optimize
d.suggest()
settle(app)
assert d.sugg, "expected suggestions"
ver0 = d.version
d.apply_suggestion_at(99)                                      # out of range: ignored
assert d.version == ver0
d.apply_suggestion_at(0)                                      # = double-click on the first suggestion
assert d.version == ver0 + 1 and not d.sugg
settle(app)
n_before = len(d.rows)
d.auto_optimize()
settle(app)
assert not errors, errors
d.undo()                                                       # one undo reverts the whole optimize

# prep popup logic, ferment-all
d.ferment_all()
assert any("fermented" in r["prep"] for r in d.rows)
d.undo()

# save / load round trip + CLI compatibility + legacy fermented flag
p = os.path.join(tmp, "t.json")
ui.write_recipe_file(p, d.recipe())
r = ui.read_recipe_file(p, app.db)
assert [x["item"] for x in r["ingredients"]] == [x["item"] for x in d.rows]
assert M.analyze(app.db, M.load_recipe(p))["overall"] > 0
legacy = ui.read_recipe_file(os.path.join(ui.RECIPES_DIR, "mh.json"), app.db)
assert legacy["ingredients"][0]["item"] == "habanero" and "fermented" in legacy["ingredients"][0]["prep"]
assert legacy["ingredients"][2]["stage"] == "finish"
for f in glob.glob(os.path.join(REAL_RECIPES, "*.json")):      # the repo's real recipes parse too
    assert ui.read_recipe_file(f, app.db)["ingredients"]

# missing ingredient: flagged, rest still analysed
d.rows.append({"item": "unobtainium", "g": 10.0, "prep": [], "stage": "main"})
d.refresh_table()
settle(app)
assert d.A is not None and "unobtainium" in d.warn.get("1.0", "end")
d.rows.pop()
d.refresh_table()
settle(app)

# charts render into the viewers
app.render_card()
settle(app)
assert app.card.view.src is not None and app.card.view.src.width > 1000, errors
app.card.view._render(0.3)
app.card.view.zoom_by(1.25)
assert app.card.view.z > 0.3

app.pair.a.set("habanero")
app.pair.b.set("mango")
app.pair.go()
settle(app)
assert app.pair.view.src is not None, errors

app.map.hl.insert("end", "habanero")
app.map.go()
settle(app)
assert app.map.view.src is not None, errors

app.compare.refresh_files()
app.compare.lb.selection_set(0)
app.compare.go()
settle(app)
assert app.compare.view.src is not None, errors

# browser sort / filter / detail
app.browser.q.set("a")
app.browser.sort_by("shu")
root.update()
kids = app.browser.tree.get_children()
assert kids
app.browser.tree.selection_set(kids[0])
root.update()
app.browser.q.set("")

# hot reload
pack = os.path.join(tmp, "ingredients_zz_new.csv")
n0 = len(app.db.items)
write_pack(pack, [dict(base, name="uitest berry", category="fruit", fruity="6", sweet="3")])
time.sleep(1.2)                                                # let the "just written" guard pass
app.reload_db()
assert len(app.db.items) == n0 + 1 and app.packs["uitest berry"] == "ingredients_zz_new.csv"
assert "uitest berry" in app.designer.ilist.get_children() and app.browser.tree.exists("uitest berry")
# one bad row: skipped + reported, everything else stays
write_pack(pack, [dict(base, name="bad one", category="not-a-category")])
time.sleep(1.2)
app.reload_db()
assert len(app.db.items) == n0 and len(app.issues) == 1 and "skipped" in app.db_var.get()
# unreadable file: last good list kept
with open(pack, "wb") as f:
    f.write(b"name,category\n\xff\xfe\x00bad\n")
time.sleep(1.2)
app.reload_db()
assert len(app.db.items) == n0 and "reload failed" in app.db_var.get()
os.remove(pack)
time.sleep(1.2)
app.reload_db()
assert len(app.db.items) == n0 and not app.issues

assert not errors, errors
d.dirty = False
app.close()
M.HERE = REAL_HERE
shutil.rmtree(tmp, ignore_errors=True)
print("ui ok")
