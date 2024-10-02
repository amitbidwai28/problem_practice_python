sal_list = [34,1,23,67,4,89,12,34,23,1]
seen = set()
duplicates = set()
for n in sal_list:
    if n in seen:
        duplicates.add(n)
    else:
        seen.add(n)

print(duplicates)