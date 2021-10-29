import random
dice_main=5
def main():
    print("Double dice roller Haha!!")
    die1 = random.randint(1, dice_main)
    die2 = random.randint(1, dice_main)
    total = die1 + die2
    print("First die is=" + str(die1))
    print("Seconf die is=" + str(die2))
    print("the result is " + str(total))

if __name__ == '__main__':
    main()

