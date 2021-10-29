

a = open("mytext.txt", "a")
contents = a.read()
mylist = contents.split(",")
print(mylist[0])
