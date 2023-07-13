# CPE 101-01
# LAB 5: String Function Tests
# Name: Leo Rivera
# Section: 3

import unittest
from str_funcs import *


class TestCases(unittest.TestCase):

    def test_vowel_extractor(self):
        vowel = 'volcanoes'
        self.assertIn(vowel_extractor(vowel), 'oaoe')
        vowel = 'iguivniu'
        self.assertNotIn(vowel_extractor(vowel), 'oae')
        vowel = 'wiejfodanciu'
        self.assertIn(vowel_extractor(vowel), 'ieoaiu')

    def test_str_capitalize(self):
        self.assertEqual(str_capitalize("i don't like doing this anymore"), "I Don't Like Doing This Anymore")
        capitalize = 'not helpful'
        self.assertTrue(str_capitalize(capitalize), 'Not Helpful')
        capitalize = 'high five'
        self.assertTrue(str_capitalize(capitalize), 'Hi Five')
        capitalize = '!this is a test'
        self.assertTrue(str_capitalize(capitalize), '!this Is A Test')
        capitalize = 'i gIVe uP oN coDINg'
        self.assertTrue(str_capitalize(capitalize), 'I Give Up On Coding')

    # def test_str_cap(self):
    #   capitalize = 'well then'
    #  self.assertTrue(str_capitalize(capitalize), 'Well Then')
    # capitalize = 'not helpful'
    # self.assertTrue(str_capitalize(capitalize), 'Not Helpful')
    # capitalize = 'high five'
    # self.assertTrue(str_capitalize(capitalize), 'Hi Five')
    # capitalize = '!this is a test'
    # self.assertTrue(str_capitalize(capitalize), '!this Is A Test')
    # capitalize = 'i gIVe uP oN coDINg'
    # self.assertTrue(str_capitalize(capitalize), 'I Give Up On Coding')

    #    def test_rotate(self):
    #        word = 'abcd'
    #        self.assertTrue(rotate(word), 'nopq')
    #        word = 'nopq'
    #        self.assertTrue(rotate(word), 'abcd')
    #        word = 'abcd nopq'
    #        self.assertTrue(rotate(word), 'nopq abcd')

    def test_str_rotate(self):
        word = 'abcd'
        self.assertTrue(str_rotate(word), 'nopq')
        word = 'nopq'
        self.assertTrue(str_rotate(word), 'abcd')
        word = 'abcd nopq'
        self.assertTrue(str_rotate(word), 'nopq abcd')

    def test_make_substring(self):
        str1 = 'Test for substring function.'
        self.assertEqual(make_substring(str1, 3, 10, 2), 'tfrs')

    def test_is_palidrome(self):
        self.assertEqual(is_palindrome('radar'), True)
        self.assertEqual(is_palindrome('racecar'), True)
        self.assertEqual(is_palindrome('fdsa'), False)

    def test_count_characters(self):
        self.assertEqual(count_characters('radar', 'r'), 2)
        self.assertEqual(count_characters('egg ', 'g'), 2)
        self.assertEqual(count_characters('something', 'a'), -1)


# trying out different outcomes
#    def test_palindrome(self):
#        self.assertEqual(palindrome('racecar'), True)
#        self.assertEqual(palindrome('book'), False)
#        self.assertEqual(palindrome('bob'), True)


if __name__ == '__main__':
    unittest.main()
