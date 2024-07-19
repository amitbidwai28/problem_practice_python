input_string = input("Enter the string: ")
print(input_string[-1])
name = {}

index_dict = {}

# Loop through each character and its index in the string
for index, char in enumerate(input_string):
    # If the character is already in the dictionary, append the index to its list
    if char in index_dict:
        index_dict[char].append(index)
    else:
        # If the character is not in the dictionary, create a new list with the index
        index_dict[char] = [index]

print(index_dict)