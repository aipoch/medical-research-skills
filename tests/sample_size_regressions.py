"""Regression for the sample-size-basic survival calculation; no network access."""
import importlib.util
import math
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sample_size_basic", ROOT / "scientific-skills/Protocol Design/sample-size-basic/scripts/main.py")
sample_size = importlib.util.module_from_spec(spec)
sys.modules["sample_size_basic"] = sample_size
spec.loader.exec_module(sample_size)


class SurvivalSampleSize(unittest.TestCase):
    def test_matches_schoenfeld_events(self):
        # Required events from R: gsDesign::nEvents(hr, alpha = 0.025, beta = 0.2)
        # (1:1 allocation); total N = events / P(event), with P(event) = 0.5.
        calc = sample_size.SampleSizeCalculator()
        for hr, events in [(0.7, 246.7871), (0.5, 65.34566)]:
            with self.subTest(hr=hr):
                self.assertEqual(calc.survival_analysis(hr), math.ceil(events / 0.5))


if __name__ == "__main__":
    unittest.main()
