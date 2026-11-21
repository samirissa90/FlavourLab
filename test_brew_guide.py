"""Headless checks for the interactive brew guide engine (no window is opened)."""
import json
import tempfile
import unittest
from pathlib import Path

from brew_guide import BrewGuide, altitude_band, load_config, ratio_range, render, save_config, span
from coffee_knowledge import Knowledge


class BrewGuideTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kb = Knowledge()

    def guide(self, **cfg_changes):
        cfg = load_config(Path(tempfile.gettempdir()) / "no_such_equipment_file.json")
        cfg.update(cfg_changes)
        return BrewGuide(self.kb, cfg)

    def setting(self, plan, key):
        return next(s for s in plan["settings"] if s["key"] == key)

    # parsers
    def test_parsers(self):
        self.assertEqual(ratio_range("1:15 to 1:17"), (15, 17))
        self.assertEqual(ratio_range("1:2"), (2, 2))
        self.assertEqual(span("94-96"), (94, 96))
        self.assertEqual(span("93"), (93, 93))
        self.assertEqual([altitude_band(v) for v in (None, 900, 1400, 1900)], [None, "low", "mid", "high"])

    # equipment presets
    def test_ecm_classika_preset_matches_sourced_facts(self):
        machine, grinder = self.guide().equipment()
        self.assertEqual(machine["boiler_type"], "single_boiler")
        self.assertEqual(machine["pump"], "vibration")
        self.assertEqual(machine["portafilter_mm"], 58)
        self.assertIn("PID", machine["temp_control"])
        self.assertIn("conflict_note", machine)
        self.assertTrue(grinder["name"].startswith("Eureka Mignon"))

    def test_specialita_is_sourced_and_generic_mignon_is_not(self):
        g = self.guide(grinder={"preset": "eureka_mignon_specialita", "overrides": {}}).equipment()[1]
        self.assertEqual(g["burr_mm"], 55)
        self.assertEqual(g["confidence"], "secondary")
        other = self.guide().equipment()[1]
        self.assertTrue(other["confidence"].startswith("unverified"))

    # espresso plan
    def espresso(self, **profile):
        base = {"method": "espresso", "style": "normale", "roast": "Medium", "altitude_masl": 1400}
        base.update(profile)
        return self.guide().plan(base)

    def test_baseline_espresso_numbers(self):
        plan = self.espresso()
        self.assertEqual(self.setting(plan, "dose")["value"], "18 g")
        self.assertEqual(self.setting(plan, "yield")["value"], "36 g")
        self.assertEqual(self.setting(plan, "time")["value"], "25-30 s")
        self.assertIn("9 bar", self.setting(plan, "pressure")["value"])

    def test_altitude_moves_temperature_inside_the_roast_range(self):
        high = self.setting(self.espresso(roast="Light", altitude_masl=1900), "temp")["value"]
        mid = self.setting(self.espresso(roast="Light", altitude_masl=1400), "temp")["value"]
        low = self.setting(self.espresso(roast="Light", altitude_masl=900), "temp")["value"]
        self.assertEqual((low, mid, high), ("94 C", "95 C", "96 C"))

    def test_temperature_is_always_inside_the_sourced_range(self):
        for roast, (lo, hi) in {"Light": (94, 96), "Medium": (93, 93), "Dark": (90, 92)}.items():
            for masl in (800, 1400, 2000, None):
                value = float(self.setting(self.espresso(roast=roast, altitude_masl=masl), "temp")["value"].split()[0])
                self.assertTrue(lo <= value <= hi, (roast, masl, value))

    def test_pid_setpoint_includes_measured_offset(self):
        g = self.guide(machine={"preset": "ecm_classika_pid", "overrides": {"temp_offset_c": 2}})
        plan = g.plan({"method": "espresso", "style": "normale", "roast": "Medium", "altitude_masl": 1400})
        self.assertEqual(self.setting(plan, "temp")["value"], "93 C")
        self.assertEqual(self.setting(plan, "setpoint")["value"], "95 C")

    def test_single_boiler_steps_mention_cooling_after_steaming(self):
        text = " ".join(self.espresso()["steps"])
        self.assertIn("steam", text)
        self.assertIn("cool and refill", text)

    def test_no_invented_dial_number_for_unknown_grinder(self):
        plan = self.espresso()
        grinder = self.setting(plan, "grinder")
        self.assertEqual(grinder["value"], "no absolute number is given")
        self.assertIn("not sourced", grinder["basis"])

    def test_style_changes_ratio_and_time(self):
        self.assertEqual(self.setting(self.espresso(style="lungo"), "yield")["value"], "54-72 g")
        self.assertEqual(self.setting(self.espresso(style="ristretto"), "time")["value"], "15-20 s")

    def test_machine_without_temperature_control_says_so(self):
        g = self.guide(machine={"preset": "generic_no_temp_control", "overrides": {}})
        plan = g.plan({"method": "espresso", "style": "normale", "roast": "Dark"})
        self.assertTrue(any("cannot set brew temperature" in w for w in plan["warnings"]))

    def test_region_altitude_mismatch_warns(self):
        plan = self.espresso(country="Ethiopia", region="Sidama (Sidamo)", altitude_masl=600)
        self.assertTrue(any("you entered 600" in w for w in plan["warnings"]), plan["warnings"])

    def test_freshness_warnings(self):
        self.assertTrue(any("very fresh" in w for w in self.espresso(days_since_roast=2)["warnings"]))
        self.assertFalse(any("very fresh" in w for w in self.espresso(days_since_roast=10)["warnings"]))
        self.assertTrue(any("past the roughly 3 weeks" in w for w in self.espresso(days_since_roast=60)["warnings"]))

    def test_robusta_is_flagged_as_unsupported(self):
        self.assertTrue(any("robusta" in w for w in self.espresso(species="robusta")["warnings"]))

    def test_weak_process_data_is_flagged(self):
        plan = self.espresso(process="wet_hulled_giling_basah")
        self.assertTrue(any("wet hulled" in w for w in plan["warnings"]))

    # filter methods
    def test_pour_over_plan_has_no_pressure_and_scales_with_dose(self):
        plan = self.guide().plan({"method": "pour_over", "roast": "Light", "altitude_masl": 1900, "dose_g": 20})
        self.assertEqual(self.setting(plan, "pressure")["value"], "not applicable")
        self.assertEqual(self.setting(plan, "yield")["value"], "300-340 g")
        self.assertEqual(self.setting(plan, "temp")["value"], "96 C")

    def test_unsourced_method_is_not_invented(self):
        plan = self.guide().plan({"method": "moka", "roast": "Medium", "dose_g": 20})
        self.assertEqual(self.setting(plan, "yield")["value"], "not sourced")
        self.assertTrue(any("No sourced ratio" in s["basis"] for s in plan["settings"]))

    # dial-in
    def advice(self, taste, time_s, **profile):
        g = self.guide(grinder={"preset": "eureka_mignon_specialita", "overrides": {}})
        base = {"method": "espresso", "style": "normale", "roast": "Medium", "altitude_masl": 1400}
        base.update(profile)
        plan = g.plan(base)
        return g.advise(plan, {"dose_g": 18, "yield_g": 36, "time_s": time_s, "taste": taste})

    def test_fast_sour_shot_goes_finer_in_the_grinders_direction(self):
        a = self.advice("sour / thin", 17)
        self.assertEqual(a["diagnosis"], "under-extracted")
        self.assertIn("finer", a["dial"])
        self.assertIn("clockwise", a["dial"])

    def test_slow_bitter_shot_goes_coarser(self):
        a = self.advice("bitter / harsh", 33)
        self.assertIn("coarser", a["dial"])
        self.assertIn("anticlockwise", a["dial"])

    def test_burnt_slow_shot_two_settings_coarser(self):
        self.assertIn("2 smallest dial mark(s) coarser", self.advice("burnt / ashy", 40)["dial"])

    def test_sour_in_window_changes_yield_not_grind(self):
        a = self.advice("sour / thin", 27)
        self.assertIn("raise yield", a["action"])
        self.assertEqual(a["dial"], "")
        self.assertIn("raise the PID setting", a["temp_hint"])

    def test_balanced_shot_keeps_settings(self):
        self.assertIn("keep", self.advice("balanced / sweet", 27)["action"])

    def test_sour_but_slow_points_to_channeling(self):
        self.assertIn("uneven extraction", self.advice("sour / thin", 38)["diagnosis"])

    def test_advice_reports_ratio_and_time_window(self):
        notes = " ".join(self.advice("bitter / harsh", 27)["notes"])
        self.assertIn("1:2.00", notes)
        self.assertIn("inside", notes)

    def test_calibration_measures_seconds_per_dial_unit_from_user_shots(self):
        g = self.guide(grinder={"preset": "eureka_mignon_specialita", "overrides": {}})
        plan = g.plan({"method": "espresso", "style": "normale", "roast": "Medium", "altitude_masl": 1400})
        history = [{"dose_g": 18, "yield_g": 36, "time_s": 18, "taste": "sour / thin", "dial": 12}]
        shot = {"dose_g": 18, "yield_g": 36, "time_s": 22, "taste": "sour / thin", "dial": 11}
        cal = g.calibrate(history + [shot])
        self.assertAlmostEqual(cal["s_per_unit"], -4.0)
        advice = g.advise(plan, shot, history)
        self.assertIn("-4.0 s per dial unit", advice["calibration"])
        self.assertIn("dial about 9.6", advice["calibration"])

    def test_calibration_needs_two_different_dial_readings_and_same_dose(self):
        g = self.guide()
        self.assertIsNone(g.calibrate([{"dial": 12, "time_s": 18, "dose_g": 18}]))
        self.assertIsNone(g.calibrate([{"dial": 12, "time_s": 18, "dose_g": 18}, {"dial": 12, "time_s": 22, "dose_g": 18}]))
        self.assertIsNone(g.calibrate([{"dial": 12, "time_s": 18, "dose_g": 18}, {"dial": 11, "time_s": 22, "dose_g": 21}]))

    def test_advice_asks_for_dial_readings_when_missing(self):
        self.assertIn("Enter your dial reading", self.advice("sour / thin", 17)["calibration"])

    def test_bad_numbers_fall_back_to_defaults(self):
        g = self.guide(machine={"preset": "ecm_classika_pid", "overrides": {"temp_offset_c": "abc", "basket_g": ""}})
        plan = g.plan({"method": "espresso", "style": "normale", "roast": "Medium"})
        self.assertEqual(self.setting(plan, "dose")["value"], "18 g")
        self.assertEqual(self.setting(plan, "setpoint")["value"], "93 C")

    # persistence and render
    def test_config_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "eq.json"
            cfg = load_config(path)
            cfg["machine"]["overrides"]["temp_offset_c"] = -3
            cfg["shots"].append({"time_s": 27})
            save_config(cfg, path)
            again = load_config(path)
            self.assertEqual(again["machine"]["overrides"]["temp_offset_c"], -3)
            self.assertEqual(again["shots"], [{"time_s": 27}])
            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["machine"]["preset"], "ecm_classika_pid")

    def test_render_shows_labels(self):
        text = render(self.espresso())
        self.assertIn("Water temperature", text)
        self.assertIn("[inferred]", text)


if __name__ == "__main__":
    unittest.main()
