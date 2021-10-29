import tkinter
import time
import math
import random

CANVAS_WIDTH = 600
CANVAS_LENGTH = 600
TO_MOVE_X = 5
TO_MOVE_Y = 9

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_LENGTH, "My Game")
    circle = canvas.create_oval(0,0,70,70, fill="RED")
    color = "blue"
    circle2 = canvas.create_oval(CANVAS_WIDTH-70,0,CANVAS_WIDTH,70, fill = color)
    dx = TO_MOVE_X
    dy = TO_MOVE_Y
    dx1 = (-dx) +1
    dy1 =dy -1
    while True:


        canvas.move(circle,dx,dy)
        canvas.move(circle2, dx1, dy1)
        if hit_left_wall(canvas, circle) or hit_right_wall(canvas, circle):
            dx *= -1
        if hit_top_wall(canvas, circle) or hit_bottom_wall(canvas, circle):
            dy = dy * -1
        if hit_left_wall(canvas, circle2) or hit_right_wall(canvas, circle2):
            dx1 *= -1
        if hit_top_wall(canvas, circle2) or hit_bottom_wall(canvas, circle2):
            dy1 = dy1 * -1
        if circles_collide(canvas, circle, circle2):
            i = random.randint(0,9999)

            dx = (dx * -1) - random.randint(1, 3)
            dy = dy * -1 + random.randint(1, 3)
            dx1 = dx * -1 - random.randint(1, 3)
            dy1 = dy1 * -1 + random.randint(1, 3)

            if i%2 != 0 :
                canvas.itemconfig(circle2,fill="red")
                canvas.itemconfig(circle, fill="green")
            else:
                canvas.itemconfig(circle2, fill="green")
                canvas.itemconfig(circle, fill="blue")














        canvas.update()

        time.sleep(1 / 50)


def hit_left_wall(canvas,object):
    return get_left_x(canvas,object) <= 0
def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH
def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0
def hit_bottom_wall(canvas,object):
    return get_bottom_y(canvas,object) >= CANVAS_LENGTH

def circles_collide(canvas,circle,circle2):
    circle2_coords = canvas.coords(circle2)
    x1 = circle2_coords[0]
    y1 = circle2_coords[1]
    x2 = circle2_coords[2]
    y2 = circle2_coords[3]
    results = canvas.find_overlapping(x1, y1, x2, y2)
    return len(results) > 1




def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]




























def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == '__main__':
    main()