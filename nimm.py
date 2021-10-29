"""
File: nimm.py
-------------------------
Add your comments here.
"""



def main():
    n=20
    f=0
    while n>0 :
        if (f%2)==0 :
            print("There are " + str(n) + " stones left.")
            p=int(input("Player 1 do you want to remove 1 or 2 stones?"))
            while p<1 or p>2:
                print("please enter either 1 or 2")
                p = int(input("Player 1 do you want to remove 1 or 2 stones?"))
            n -= p
            f+=1
            if n == 0:
                print("Player 2 is the winner.")
        else :
            print("there are " + str(n) + " stones left.")
            p=int(input("Player 2 do you want to remove 1 or 2 stones?"))
            while p<1 or p>2:
                print("please enter either 1 or 2")
                p = int(input("Player 2 do you want to remove 1 or 2 stones?"))
            n -=p
            f+=1
            if n==0:
                print("Player 1 is the winner.")







if __name__ == '__main__':
    main()
