# Lab 7
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 7

import unittest
from nested import *


class TestCases(unittest.TestCase):
    # def test_searched_2D(self):
    #     self.assertListEqual(search_2D([[1, 2, 3], [3, 4, 5], [1, 4, 5]], 2), [(0, 1)])

    def test_add_values(self):
        self.assertEqual(add_values([1, 2, [4, 5], 4, 'a', [6, 5, 7], 9]), 43)

    # Run the unit tests.
    if __name__ == '__main__':
        unittest.main()
