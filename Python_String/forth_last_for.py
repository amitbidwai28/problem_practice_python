
def forth_last_char(string):
    if len(string) <= 4:
        return "String is too short to count the character"

    n = len(string)
    for ele in range(n):
        if ele == n-4:
            return string[ele]





forth_char = input("Enter the string: ")
forth_last_char(forth_char)
print("4th last character is: ", forth_last_char(forth_char))