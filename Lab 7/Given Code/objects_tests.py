# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3


import unittest
from objects import *


class TestCases(unittest.TestCase):

    def test_Circle(self):
        center = Point(2, 2)
        radius = 3
        circle = Circle(center, radius)
        self.assertEqual(circle.center, center)
        self.assertEqual(circle.radius, radius)
        center = Point(6, 3)
        radius = 3
        circle = Circle(center, radius)
        self.assertEqual(circle.center, center)
        self.assertEqual(circle.radius, radius)
        center = Point(1, 1)
        radius = 1
        circle = Circle(center, radius)
        self.assertEqual(circle.center, center)
        self.assertEqual(circle.radius, radius)

    def test_Circle_eq(self):
        center = Point(2, 2)
        center2 = Point(2, 2)
        radius = 2
        radius2 = 2
        circle1 = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertTrue(circle1 == circle2)
        center = Point(3, 3)
        center2 = Point(3, 3)
        radius = 3
        radius2 = 3
        circle1 = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertTrue(circle1 == circle2)
        center = Point(4, 4)
        center2 = Point(4, 4)
        radius = 4
        radius2 = 4
        circle1 = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertTrue(circle1 == circle2)

    def test_Circle_ne(self):
        center = Point(2, 2)
        center2 = Point(4, 4)
        radius = 3
        radius2 = 6
        circle = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertFalse(circle == circle2)
        self.assertTrue(circle != circle2)
        center = Point(1, 2)
        center2 = Point(3, 4)
        radius = 2
        radius2 = 8
        circle = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertFalse(circle == circle2)
        self.assertTrue(circle != circle2)
        center = Point(2, 1)
        center2 = Point(4, 3)
        radius = 1
        radius2 = 6
        circle = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertFalse(circle == circle2)
        self.assertTrue(circle != circle2)

    def test_overlaps(self):
        center = Point(2, 2)
        center2 = Point(4, 4)
        radius = 3
        radius2 = 6
        circle = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertTrue(Circle.overlaps(circle, circle2))
        center = Point(1, 1)
        center2 = Point(3, 3)
        radius = 2
        radius2 = 5
        circle = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertTrue(Circle.overlaps(circle, circle2))
        center = Point(3, 3)
        center2 = Point(5, 5)
        radius = 3
        radius2 = 6
        circle = Circle(center, radius)
        circle2 = Circle(center2, radius2)
        self.assertTrue(Circle.overlaps(circle, circle2))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
