"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    This program  randomly generates simple addition problems for the user,
     reads in the answer from the user, and then checks to see if they got
     it right or wrong, until the user appears to have mastered the material
    """
    correct_responses = 0
    # True if user gets less than 3 correct responses
    while correct_responses != 3:

        number_one = random.randint(10, 99)
        number_two = random.randint(10, 99)
        result = number_one + number_two
        print("What is " + str(number_one) + " + " + str(number_two) + " ? ")
        your_answer = int(input("Your answer:"))
        # True if answer is incorrect
        if your_answer != result:
            print(" Incorrect. The expected answer is " + str(result))
        else:
            correct_responses += 1
            print(" Correct! You've gotten " + str(correct_responses) + " correct in a row.")

    # if user get 3 correct_responses
    print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
