"""
File: extension.py
------------------
This is a file for creating an optional extension program, if
you'd like to do so.
"""


def main():
    f=0
    p=int(input("enter any number = "))
    while p>1 :
        if p%2==0 :
            n=p//2
            print(str(p)+" is even, so lets divide it by 2 " + "= " + str(n) )
            p=n
            f+=1
        else:
            r=p*3+1
            print(str(p)+" is odd, so lets mutliply by 3 and add 1 " + "= " + str(r))
            p=r
            f+=1
    print("The process took " + str(f) +" steps to reach 1.")






# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
