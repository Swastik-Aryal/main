import random
guess_count = 0
guess_limit = 5
out_of_guesses=False

def main():
    words = ["apple", "banana", "strawberry"]
    our_word=random.choice(words)
    word_length = len(our_word)
    print("Hello player. This is a Hangman game developed by Swastik Aryal."
          "Here, you have to guess the missing letters from the word."
          "Kindly guess only one letter at a time."
          "You will only get 3 chances so please think before actually entering a letter."
          "Hope you enjoy it.")
    print("The length of the word is " + str(word_length))
    create_problem(our_word)
    print("Hope you enjoyed the game.")

def create_problem(our_word):
    guess_count = 0
    guess_limit = 3
    a=0
    out_of_guesses = False
    list_of_letters = list(our_word)
    replaced_letter1 = random.choice(list_of_letters)
    new_word = element_replace(list_of_letters, replaced_letter1, "_")
    replaced_letter2 = random.choice(new_word)
    new_word2 = element_replace(new_word, replaced_letter2, "_")
    print(new_word2)
    while not(out_of_guesses) and a < 2:
        user_guess = input("enter a guess :: ")
        if replaced_letter1 == user_guess or replaced_letter2 == user_guess :
            if replaced_letter1 ==user_guess and replaced_letter2 != user_guess:
                print("You've got one of the letters correct.")
                guess_count +=1
                a+=1
            elif replaced_letter2 ==user_guess and replaced_letter1 != user_guess:
                print("You've got one of the letters correct.")
                guess_count += 1
                a+=1

        else:
            print("Sorry, that was incorrect")
            print(new_word)
            guess_count += 1
        if guess_count >= guess_limit:
           out_of_guesses = True
           print("You are out of guesses. You lose.")
           print("The word was " + str(our_word))
        if a==2 :
            print("Kangratulations successful person you have succeded to guess the letters correctly.")
            print("The word was " + str(our_word))





def element_replace(list_name,element,replacement):
    for n, i in enumerate(list_name):

        if i == element:
            list_name[n] = replacement
    return list_name





if __name__ == "__main__":
    main()