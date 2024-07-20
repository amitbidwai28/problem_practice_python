# def count_of_words(entered_str):
#     count = 0
#     if len(entered_str) <= 0:
#         return "Entered string is not valid"
#     n = len(entered_str)
#     for ele
#
# req_string = input("Enter the string: ")
# count_of_words(req_string)
# print("The number of words in a string are: ", count_of_words(req_string))

import re


def count_words_regex(input_string):
    # Use regular expression to find all words
    words = input_string.split()
    return len(words)


# Example usage:
input_string = input("Enter the string: ")
print("Number of words:", count_words_regex(input_string))  # Output: 4
