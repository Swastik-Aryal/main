import pyautogui
import win32api,win32con
import time
import keyboard
from pynput.mouse import Controller

time.sleep(1)
# 213 323
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
a=  True
while a == True:
    r,g,b = pyautogui.pixel(196,333)
    if r == 83 and b== 83:
        keyboard.press_and_release("space")

