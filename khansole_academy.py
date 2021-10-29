"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random
MIN_VALUE=10
MAX_VALUE=99
correct_answers=3


def main():
    f=0
    while f!=correct_answers:
        a = int(random.randint(MIN_VALUE,MAX_VALUE))
        b = int(random.randint(MIN_VALUE,MAX_VALUE))
        sum = a + b
        print("What is the sum of " + str(a) + "+" + str(b) + "?")
        ans = int(input("Your answer = " ))
        if ans==sum :
            f += 1
            print("Correct." + "You've gotten " + str(f) + " correct in a row")
        else:
            f=0
            print("Incorrect." + "The expected answer was " + str(sum))
    print("Congratulations. You have mastered addition!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
