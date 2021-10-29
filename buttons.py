from tkinter import*

root = Tk()

frame = LabelFrame(root, padx=50, pady=50)
frame.pack()

label = Label(frame, text = "Enter your Name.")
label.grid(row = 0, column = 0)

myinput = Entry(frame, border=10, font = ("Helvetica", 25) )
myinput.grid(row = 1 , column = 0)

def activity():
    mylabel = Label(frame, text= "Hi " + myinput.get())
    mylabel.grid(row = 3,column = 0)

mybutton = Button(frame, text ="OK" , padx = 70, command = activity , fg = "red" , bg = "blue")
mybutton.grid(row = 2, column = 0, pady=10)

root.mainloop()