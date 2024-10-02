def count_words_regex(input_string, search_string):
    x = search_string
    temp = 0
    # Use regular expression to find all words
    words = input_string.split()
    print(words)
    for eachwords in words:
        if eachwords == x:
            temp = temp + 1

    return temp


# Example usage:
input_string = input("Enter the string: ")
seacrh_string = input("Enter the string which you want to search: ")
print("Count of the string", seacrh_string, "is: ", count_words_regex(input_string, seacrh_string))
