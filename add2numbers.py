"""
File: add2numbers.py
--------------------
Another python program to get some practice with variables.
This program asks the user for two integers and prints their sum.
"""

def main():
    print ("this program substracts two numbers.")
    a=input("enter the first number:")
    b=input("enter the second number:")
    a=int(a)
    b=int(b)
    diff= a - b
    print("the diff of a and b is " + str(diff) + "!" )

if __name__ == '__main__':
    main()




# This provided line is required at the end of a Python file
# to call the main() function.

