import pyautogui
import keyboard
from pynput.mouse import Controller,Button
import time
import win32api , win32con

#1st tile = x=325,y=666
#2nd tile = x=407,y=666
#3nd tile = x=500,y=666
#4th tile = x=580,y=666

x1 = 286
x2 = 372
x3 = 460
x4 =544
y=560
mouse = Controller()
n=0
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)



time.sleep(1)
while keyboard.is_pressed("c") != True:
    if pyautogui.pixel(x1,y)[0] == 0:
        click(x1,y)
        n=n+1
        print(n)
    if pyautogui.pixel(x2,y)[0] == 0:
        click(x2,y)
        n = n + 1
        print(n)
    if pyautogui.pixel(x3,y)[0] == 0:
        click(x3,y)
        n = n + 1
        print(n)
    if pyautogui.pixel(x4,y)[0] == 0:
        click(x4,y)
        n = n + 1
        print(n)
# pyautogui.displayMousePosition()

# while keyboard.is_pressed("c") != True:
#
#     print('The current pointer position is {0}'.format(
#         mouse.position))
