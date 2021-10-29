from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
root.title("My Images")
img1 = "D:\images\h.png"
img2 = "D:\images\ii.png"
img3 = "D:\images\j.jpg"
img4 = "D:\images\k.png"
img5 = "D:\images\l.png"

images = [img1, img2, img3, img4, img5]

my_image = ImageTk.PhotoImage(Image.open(images[0]))
my_label = Label(image=my_image)
my_label.grid(row=0, column=0, columnspan=3)

exit_button = Button(root, text="Exit", bg="Black", fg="white", command=root.quit)
exit_button.grid(row=1, column=1)


def forward_image(img_num):
    global my_label
    global forward_button
    global backward_button

    my_label.grid_forget()
    my_image1 = ImageTk.PhotoImage(Image.open(images[img_num]))
    my_label = Label(image=my_image1)
    my_label.grid(row=0, column=0, columnspan=3)

    forward_button = Button(root, text="Next", command=lambda: forward_image(img_num+1))
    backward_button = Button(root, text="Back", command=lambda: backward_image(img_num-1))

    forward_button.grid(row=1, column=2)
    backward_button.grid(row=1, column=0)



    exit_button = Button(root, text="Exit", bg="Black", fg="white", command=root.quit)
    exit_button.grid(row=1, column=1)


def backward_image(img_num):
    global my_label
    global forward_button
    global backward_button
    global my_image1

    my_label.grid_forget()
    my_image1 = ImageTk.PhotoImage(Image.open(images[img_num]))
    my_label = Label(image=my_image1)
    my_label.grid(row=0, column=0, columnspan=3)

    forward_button = Button(root, text="Next", command=lambda: forward_image(img_num + 1))
    backward_button = Button(root, text="Back", command=lambda: backward_image(img_num - 1))

    forward_button.grid(row=1, column=2)
    backward_button.grid(row=1, column=0)

    exit_button = Button(root, text="Exit", bg="Black", fg="white", command=root.quit)
    exit_button.grid(row=1, column=1)


forward_button = Button(root, text="Next", command= lambda: forward_image(1))
backward_button = Button(root, text="Back", command= backward_image(1))

forward_button.grid(row=1, column=2)
backward_button.grid(row=1, column=0)

root.mainloop()
