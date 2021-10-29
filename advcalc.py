from tkinter import *

root = Tk()
root.title(" Swastik's Calculator !!")



def open():
    global myinput
    top = Toplevel()
    myinput = Entry(top, width=28, borderwidth=10, font=("Helvetica", 18))
    myinput.grid(row=0, column=0, columnspan=5)
    button1 = Button(top, text="1", padx=30, pady=20, command=lambda: click(1))
    button2 = Button(top, text="2", padx=30, pady=20, command=lambda: click(2))
    button3 = Button(top, text="3", padx=30, pady=20, command=lambda: click(3))
    button4 = Button(top, text="4", padx=30, pady=20, command=lambda: click(4))
    button5 = Button(top, text="5", padx=30, pady=20, command=lambda: click(5))
    button6 = Button(top, text="6", padx=30, pady=20, command=lambda: click(6))
    button7 = Button(top, text="7", padx=30, pady=20, command=lambda: click(7))
    button8 = Button(top, text="8", padx=30, pady=20, command=lambda: click(8))
    button9 = Button(top, text="9", padx=30, pady=20, command=lambda: click(9))
    button0 = Button(top, text="0", padx=30, pady=20, command=lambda: click(0))
    button_add = Button(top, text="+", font=("Helvetica", 12), padx=30, pady=20, command=add)
    button_sub = Button(top, text="-",font=("Helvetica", 12), padx=30, pady=20, command=substract)
    button_mul = Button(top, text="*",font=("Helvetica", 12), padx=31, pady=20, command=multiply)
    button_div = Button(top, text="/",font=("Helvetica", 12), padx=30, pady=20, command=divide)
    button_clear = Button(top, text="Clear", padx=60, pady=20, command=clear)
    button_equal = Button(top, text="=",font=("Helvetica", 12), padx=150, pady=20, command=equals)

    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button_clear.grid(row=1, column=3, columnspan=2)

    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    button_add.grid(row=2, column=3)
    button_sub.grid(row=2, column=4)

    button7.grid(row=3, column=0)
    button8.grid(row=3, column=1)
    button9.grid(row=3, column=2)
    button_mul.grid(row=3, column=3)
    button_div.grid(row=3, column=4)

    button0.grid(row=4, column=0)
    button_equal.grid(row=4, column=1, columnspan=4)

intro_page= Label (root,text="Hello Everyone. This is an experimental calculator made by me.", font = ("Helvetica",13), padx=10, pady=10)
intro_page.grid(row=0,column=0)
intro_page1=Label (root,text="This is just a trial version which can be used for simple calculations.", font = ("Helvetica",13), padx=10, pady=10)
intro_page1.grid(row=1,column=0)
intro_page2=Label (root,text="I will be releasing better versions which will be more useful for students very soon.", font = ("Helvetica",13), padx=10, pady=10)
intro_page2.grid(row=2,column=0)
intro_page3=Label (root,text="To use the calculator please press the button below.", font = ("Helvetica",13), padx=10, pady=10)
intro_page3.grid(row=3,column=0)
use_button = Button(root, text="Open Calculator",font=("Helvetica",11),border=5 ,padx=10,pady=10,command=open)
use_button.grid(row=4,column=0, pady=7)
#TO DEFINE THE NECESSARY FINCTIONS

def click(number):
    current = myinput.get()
    myinput.delete(0, END)
    myinput.insert(0, str(current) + str(number))

def add():
    global operation
    operation = "add"
    global number1
    number1 = float(myinput.get())
    myinput.delete(0,END)
def substract():
    global operation
    operation = "sub"
    global number1
    number1 = float(myinput.get())
    myinput.delete(0, END)
def multiply():
    global operation
    operation = "mul"
    global number1
    number1 = float(myinput.get())
    myinput.delete(0, END)
def divide():
    global operation
    operation = "div"
    global number1
    number1 = float(myinput.get())
    myinput.delete(0, END)

def equals():
    number2 = float(myinput.get())
    myinput.delete(0,END)
    if operation == "add":
        myinput.insert(0,number1 + number2)
    if operation == "sub":
        myinput.insert(0, number1-number2)
    if operation == "mul":
        myinput.insert(0, number1 * number2)
    if operation == "div":
        myinput.insert(0, number1 / number2)

def clear():
    myinput.delete(0, END)





root.mainloop()