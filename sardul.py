from tkinter import*
from PIL import Image
from PIL import ImageTk


root = Tk()

my_label = Label(text = "I am gay. Look at me.", font= ("Helvetica", 20))
my_label.grid(row=0, column=0)


my_image = ImageTk.PhotoImage(Image.open("D:\sardul.png"))
my_label = Label(image=my_image)
my_label.grid(row=1, column=0)

root.mainloop()