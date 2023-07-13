# CPE 101-01
# LAB 5: String Function
# Name: Leo Rivera
# Section:3

import unittest
import test_str_funcs


# purpose  vowel_extractor (chars: str) -> str
def vowel_extractor(string1: str) -> str:
    string2 = ''
    for word in string1:
        if word in 'AEIOUaeiou':
            string2 += word
    return string2


# this code also works too
# string2 = ''
# for idx in range(len(string1)):
# if string1[idx] == 'a' or string1[idx] == 'e' or string1[idx] == 'i' or string1[idx] == 'o' or string1[
#     idx] == 'u' or string1[idx] == 'A' or string1[idx] == 'E' or string1[idx] == 'I' or string1[idx] == 'O' or \
#          string1[idx] == 'U':
#       string2 += string1[idx]
# return string2


# purpose: is to capitalize the first letter of a word
def str_capitalize(string:str)-> str:
    word = ''
    this = True
    for ch in string:
        if ch == ' ':
            this = True
            word += ch
        elif ch >= 'a' and ch <= 'z' and this == True:
            this = False
            ch = chr(ord(ch) - 32)
            word += ch
        else:
            word += ch
    return word


# this code works perfectly however you won't like it since its 'insufficien' in your eyes
# def str_cap(string:str) ->str:
#    sentence = ''
#    word = ''
#    for character in string:
#        if character != ' ':
#            word += character
#        else:
#            capital_word = first_letter(word)
#            sentence += capital_word
#            word = ''
#    return sentence

# second part of the code above(str_cap)
# def first_letter(word:str) -> str:
#    temp = ''
#    for idx in range(len(word)):
#        if 'a' <= word[0] <= 'z':
#            temp += chr(ord(word[0]) - 32)
#        else:
#            temp += word[idx]
#    return temp

# purpose: This is where we add 13 place if the letter is between a-m and -13 if n-z
def str_rotate(something: str)-> str:
    word = ''
    for ch in something:
        choice = ch
        if 'a' <= ch <= 'm' or 'A' <= ch <= 'M':
            choice += chr(ord(ch) + 13)
        if 'n' <= ch <= 'z' or 'N' <= ch <= 'Z':
            choice += chr(ord(ch) - 13)
        word += choice
    return word


# This function also works for the str_rotate, its just that I know you don't like long code
# def rotate(something):
#    word = ''
#    for character in something:
#        if character != ' ':
#            word += character
#        else:
#            reverse = first_one(word)
#            word += reverse
#        return word

# second part that helps rotate function
# def first_one(word):
#    choice = ''
#    for idx in range(len(word)):
#        if 'a' <= word[0, -1] <= 'm' or 'A' <= word[0, -1] <= 'M':
#            choice += chr(ord(word[0, -1]) + 13)
#        if 'n' <= word[0, -1] <= 'z' or 'N' <= word[0, -1] <= 'Z':
#            choice += chr(ord(word[0, -1]) - 13)
#        else:
#            choice += word[idx]
#    return choice

# purpose: we get a string and return the start idx and end idx
def make_substring(string, start_idx, end_idx, step: (str & num)) -> str:
    substring = ''
    for idx in range(start_idx, end_idx, step):
        substring += string[idx]
    return substring


# purpose: To see if the word is spelled backwards (true) if not (false)
def is_palindrome(string: str) -> bol:
    for num in range(len(string) // 2):
        if string[(len(string) - 1) - num] in string[num]:
            return True
    return False


# purpose: is to see if there is more than one letter same so print how many are there
def count_characters(string, letter:str)-> num:
    count = 0
    for one in range(len(string)):
        if letter in string[one]:
            count += 1
    if count == 0:
        return -1
    else:
        return count

# def palindrome(string):
#    num = len(string) // 2
#    counter = 0
#    for this in range(counter, num):
#        if string[counter] == string[len(string) - 1 - counter]:
#            return True
#        else:
#           return False
