""" A palindrome is a string that reads the same left-to-right and right-to-left """
from collections import Counter


def check_palindrome_string(input_string):
    return sum([ele % 2 for ele in Counter(input_string).values()]) <= 1


def check_palindrome_string_2(input_string):
    return sum([input_string.count(ele) % 2 for ele in set(input_string)]) <= 1


print(check_palindrome_string_2("aabbc"))
