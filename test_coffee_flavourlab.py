"""Headless checks for the Coffee Flavourlab knowledge engine (no window is opened)."""
import unittest

from coffee_knowledge import METHODS, ROASTS, Knowledge


class CoffeeKnowledgeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.kb = Knowledge()

    def test_datasets_load(self):
        for name in ("brew_targets", "grind_sizes", "roast_levels", "water_profiles", "troubleshooting",
                     "origins_regions", "varieties_wcr", "processing_methods"):
            self.assertTrue(self.kb.table(name), name)

    def test_grid_covers_every_combination(self):
        grid = self.kb.grid()
        self.assertEqual(len(grid), len(METHODS) * len(ROASTS) * (1 + len(self.kb.processes)))
        keys = {(r["method"], r["roast"], r["process"]) for r in grid}
        self.assertEqual(len(keys), len(grid))

    def test_pour_over_uses_roast_specific_temperature(self):
        self.assertEqual(self.kb.summary("pour_over", "Medium")["temp_c"], "93-94")
        self.assertEqual(self.kb.summary("pour_over", "Dark")["temp_c"], "91-93")

    def test_espresso_uses_baseline_ratio_and_flags_snippet_confidence(self):
        s = self.kb.summary("espresso", "Dark")
        self.assertEqual(s["ratio"], "1:2")
        self.assertEqual(s["temp_c"], "90-92")
        self.assertEqual(s["confidence"], "snippet")

    def test_method_without_sourced_numbers_is_not_invented(self):
        s = self.kb.summary("moka", "Medium")
        self.assertIsNone(s["ratio"])
        self.assertIn("ratio", s["missing"])
        self.assertEqual(s["confidence"], "secondary")

    def test_process_lowers_confidence_when_its_source_is_weak(self):
        c = self.kb.combo("espresso", "Light", "wet_hulled_giling_basah")
        self.assertEqual(c["confidence"], "very low")
        self.assertIn("wet_hulled_giling_basah", c["cup"])

    def test_answers_troubleshooting(self):
        text = self.kb.answer("my espresso is sour and fast")
        self.assertIn("under-extracted", text)

    def test_answers_milk(self):
        self.assertIn("oat", self.kb.answer("what temperature for oat milk").lower())

    def test_flags_missing_drink(self):
        self.assertIn("no numeric source", self.kb.answer("how do I make an affogato"))

    def test_answers_origin_altitude(self):
        self.assertIn("Ethiopia", self.kb.answer("ethiopia altitude"))

    def test_answers_variety_with_alias(self):
        self.assertIn("geisha", self.kb.answer("tell me about gesha").lower())

    def test_help_and_unknown_input(self):
        self.assertIn("Ask about", self.kb.answer("help"))
        self.assertIn("No match", self.kb.answer("zzqx blorf"))
        self.assertIn("Ask about", self.kb.answer(""))


if __name__ == "__main__":
    unittest.main()
