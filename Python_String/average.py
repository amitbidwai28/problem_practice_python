number = int(input("Enter the number from which you start the average: "))
limit = int(input("Enter the limit which you want to set: "))
temp = 0
count = 0
for ele in range(limit):
    if (number + ele) % 2 == 0:
        temp = number + ele + temp
        count = count + 1
print("Total of the even no. fall between: ", temp)
print("Total no.s of the digit: ", count)
print("Average of the expression is: ", (temp / count))