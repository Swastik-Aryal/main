from tkinter import*

root = Tk()
mylabel1 = Label(root, text = "My name is swastik")
mylabel2 = Label(root, text = "apna time aaaega")
mylabel3 = Label(root, text = "                             ")

mylabel1.grid(row=0, column = 0)
mylabel2.grid(row = 1, column = 2)
mylabel3.grid(row = 1, column = 1)

root.mainloop()