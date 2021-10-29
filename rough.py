import random

words=["rujin","devkota","apple","bananna","suhi"]
game_word=random.choice(words)
print("_"*len(game_word))
letters=[]
num_guess= 7
done=False
print(game_word)

while done==False:
 user_guess = input("enter a guess :: ")
 for i in game_word:
    if user_guess==i:
          letters=i
          print(letters,end=" ")

    else:
          letters="_"
          print(letters,end="")


 num_guess=num_guess-1
 print(num_guess)
 if num_guess==0:
         done=True