import math

strong_number = int(input("Enter the no. which you want to test: "))
# print(math.factorial(strong_number))

temp_fact = 0
for ele in str(strong_number):
    ele1 = int(ele)
    ele2 = math.factorial(ele1)
    temp_fact = ele2 + temp_fact

if strong_number == temp_fact:
    print(strong_number, "Is Strong Number")
else:
    print(strong_number, "Is Not Strong")