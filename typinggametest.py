from pynput.keyboard import Listener
import random
from tkinter import *

root = Tk()

title = Label(root,text = "TYPING TEST")
title.grid(row=1, column = 0)

start_button = Button(root,text="START")
start_button.grid(row = 3, column = 0)

typer_box = Entry(root, width = 30, borderwidth=10, font = ("Helvetica", 18))
typer_box.grid(row = 2, column = 0)

























root.mainloop()