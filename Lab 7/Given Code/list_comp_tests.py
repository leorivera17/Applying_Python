# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3
# list comprehension tests


import unittest
from list_comp import *
from objects import *
import math


class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_distance_all(self):
        list1 = [Point(1, 1), Point(3, 3)]
        self.assertListAlmostEqual(distance_all(list1), [1.4142135623730951, 4.242640687119285])
        list1 = [Point(1, 2), Point(3, 4)]
        self.assertListAlmostEqual(distance_all(list1), [2.23606797749979, 5])
        list1 = [Point(5, 6), Point(7, 8)]
        self.assertListAlmostEqual(distance_all(list1), [7.810249675906654, 10.63014581273465])

    def test_are_in_first_quadrant(self):
        list1 = [Point(1, 1), Point(-2, 1)]
        self.assertListEqual(are_in_first_quadrant(list1), [Point(1, 1)])
        list1 = [Point(2, 1), Point(3, -1), Point(-2, 1)]
        self.assertListEqual(are_in_first_quadrant(list1), [Point(2, 1)])
        list1 = [Point(5, 1), Point(-2, 2), Point(4, -3), Point(-9, -9), Point(1, 1)]
        self.assertListEqual(are_in_first_quadrant(list1), [Point(5, 1), Point(1, 1)])

    def test_circle_distance_all(self):
        list1 = [Circle(Point(1, 1), 1), Circle(Point(3, 3), 2)]
        self.assertListAlmostEqual(circle_distance_all(list1), [1.414213562373095225, 4.242640687119285])

    def test_overlaps_all(self):
        list1 = [Circle(Point(0, 0), 1), Circle(Point(3, 3), 1)]
        self.assertListEqual(overlaps_all(list1), [Circle(Point(0, 0), 1)])
        list1 = [Circle(Point(0, 0), 1), Circle(Point(4, 4), 1)]
        self.assertListEqual(overlaps_all(list1), [Circle(Point(0, 0), 1)])
        list1 = [Circle(Point(0, 0), 1), Circle(Point(5, 5), 1)]
        self.assertListEqual(overlaps_all(list1), [Circle(Point(0, 0), 1)])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
