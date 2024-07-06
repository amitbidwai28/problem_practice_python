
try:

    while True:
        # Attempt to perform the division operation and store the result in the 'result' variable.
        numerator = int(input("Enter the number: "))
        denominator = int(input("Enter the denominator: "))
        result = numerator / denominator
        # Print the result of the division.
        print("Result:", result)
except ZeroDivisionError as exe1:
        # Handle the exception if a division by zero is attempted.
    print(exe1)
    print("The division by zero operation is not allowed.")
