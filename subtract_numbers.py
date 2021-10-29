"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""


def main():
    a= float(input("Enter the first number = "))
    b = float(input("enter the second number = "))
    diff = a - b
    print("The difference is" + str(diff) )


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
