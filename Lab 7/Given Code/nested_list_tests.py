# Lab 7
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3
# unittest for objects


import unittest
from nested_list import *


class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        listed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertListEqual(groups_of_3(listed), [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        listed = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertListEqual(groups_of_3(listed), [[1, 2, 3], [4, 5, 6], [7, 8]])
        listed = [1, 2, 3, 4, 5, 6, 7, 8, 8]
        self.assertListEqual(groups_of_3(listed), [[1, 2, 3], [4, 5, 6], [7, 8, 8]])

    def test_final_value(self):
        self.assertListEqual(final_value([[-1, 12, 3], [8], [], [1, -3]]), [3, 8, -3])
        self.assertListEqual(final_value([[1, 2, 3, 4, 5], [-6], [-6, -3, 0]]), [5, -6, 0])
        self.assertListEqual(final_value([[1, 2, 3, 4], [-4], [-6, -3, 0]]), [4, -4, 0])

    def test_repeat_value(self):
        self.assertListEqual(repeat_value([1, 2, 3]), [[1], [2, 2], [3, 3, 3]])
        self.assertListEqual(repeat_value([1, 5, 3, 0]), [[1], [5, 5, 5, 5, 5], [3, 3, 3], []])
        self.assertListEqual(repeat_value([1, 3, 3, 0]), [[1], [3, 3, 3], [3, 3, 3], []])


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
