def count_words_regex(input_string):
    # Use regular expression to find all words
    words = input_string.split()
    for items in words:
        print("first character of the string", items, "is", items[0])

    return input_string


# Example usage:
input_string = input("Enter the string: ")
count_words_regex(input_string)  # Output: 4
