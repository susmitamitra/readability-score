from unittest import TestCase, expectedFailure
from readability_score.calculators.fleschkincaid import *

class FleshKincaidTestCase(TestCase):
    def setUp(self):
        text = "Readability is the ease with which a reader can understand a written text. In natural language, the readability of text depends on its content (the complexity of its vocabulary and syntax) and its presentation (such as typographic aspects like font size, line height, and line length)."
        self.calc = FleschKincaid(text)
        self.min_age_test = 17

    def test_range_min_age(self):
        test_range = [16,17,18]
        self.assertIn(self.calc.min_age, test_range, "min_age is not within 1yr of " + str(self.min_age_test))

    @expectedFailure
    def test_exact_min_age(self):
        self.assertEqual(self.calc.min_age, self.min_age_test, "might break because of deps")
