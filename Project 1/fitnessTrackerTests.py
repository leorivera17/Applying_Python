# Project 1 Fitness Tracking Tests
# At least 2 tests for each function
# Name: Leo Rivera
# Section: 3
# Date: 1/14/22

import unittest
from fitnessTrackerFuncs import *


class MyTestCase(unittest.TestCase):
    def test_convert_lb_to_kg(self):
        self.assertAlmostEqual(convert_lb_to_kg(170), 77.1107029)
        self.assertAlmostEqual(convert_lb_to_kg(130), 58.9670081)
        self.assertAlmostEqual(convert_lb_to_kg(140), 63.502931800000006)

    def test_compute_MET(self):
        self.assertEqual(compute_MET(1), 5)
        self.assertEqual(compute_MET(2), 7)
        self.assertEqual(compute_MET(3), 3)

    def test_compute_calorie_burned(self):
        self.assertAlmostEqual(compute_calorie_burned(120, 64, 2), 268.8)
        self.assertAlmostEqual(compute_calorie_burned(50, 68.0388555, 2), 119.06799712499998)
        self.assertAlmostEqual(compute_calorie_burned(30, 77, 3), 121.275)

    def test_BMI_category(self):
        self.assertEqual(BMI_category(17), 'Underweight')
        self.assertEqual(BMI_category(23), 'Normal Weight')
        self.assertEqual(BMI_category(47), 'Obesity')

    def test_compute_equivalent_miles(self):
        self.assertAlmostEqual(compute_equivalent_miles(67, 2, 120), 11.896433712121212)
        self.assertAlmostEqual(compute_equivalent_miles(74, 2, 120), 13.139344696969697)
        self.assertAlmostEqual(compute_equivalent_miles(59, 2, 120), 10.475964015151513)


if __name__ == '__main__':
    unittest.main()
