def is_armstrong(number):
    # Convert the number to a string to get its digits
    digits = str(number)
    num_digits = len(digits)

    # Calculate the sum of digits each raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    print("lets go")

    # Check if the calculated sum equals the original number
    return sum_of_powers == number

# Example usage
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
