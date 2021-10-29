from pynput.keyboard import Listener
import random



list_of_words=["my name is rujin devkota","i am from kathmandu nepal"]
key_pressed=""
letters_list=[]
string=random.choice(list_of_words)
score=len(string)
count=int(0)
print(string)



for i in string:
    letters_list.append(i)
print(letters_list)


def press(key):
    global key_pressed,score,letters_list,count_loop,count
    key_pressed =str(key).replace("'","")

    if letters_list[count] != key_pressed and letters_list[count]!=" ":
            print(score)
            score = score - 1

def realese(key):
  global count_loop,count,string,root
  count= count+1
  if count>=len(string):
      return False


with Listener(on_press=press, on_release=realese) as listner:
        listner.join()
        print(f"your score is {score}")
