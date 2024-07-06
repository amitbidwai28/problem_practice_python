# Define a function named divide_numbers that takes two parameters: x and y.
def divide_numbers(x, y):
    try:
        # Attempt to perform the division operation and store the result in the 'result' variable.
        result = x / y
        # Print the result of the division.
        print("Result:", result)
    except ZeroDivisionError:
        # Handle the exception if a division by zero is attempted.
        print("The division by zero operation is not allowed.")


def check_number(prompt):
    while True:

        try:
            value: float = float(input(prompt))
            return value
        except ValueError as ve:
            print("Error: Invalid input. Please Input a valid number.")


# Usage
# Define the numerator and denominator values.
numerator = check_number("Enter the numerator: ")
denominator = check_number("Enter the denominator: ")
# Call the divide_numbers function with the provided numerator and denominator.
divide_numbers(numerator, denominator)
