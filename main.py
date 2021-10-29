
def factorial(n):
    """
    >>> factorial(2)
    2
    >>> factorial(0)
    1
    """
    result=1
    for i in range(1,n+1):
        result*=i
    return result

def main():
    i=int(input("enter a number= "))
    print(i, factorial(i))

if __name__ =='__main__':
    main()




