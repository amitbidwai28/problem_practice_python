str1 = "AmitBidwai"
str2 = ""
for ele in range(len(str1)-1, -1, -1):
    str2 = str2 + str1[ele]
print("Reverse string is:  ", str2)