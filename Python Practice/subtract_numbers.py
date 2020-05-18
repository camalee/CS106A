"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    """
    This function reads two real numbers from the user and
    prints the first number minus the second number.
    """
    print("This program subtracts one number from another.")
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
    result = first_number - second_number
    print("The result is " + str(result))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
