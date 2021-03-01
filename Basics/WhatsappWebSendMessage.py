#When whatsapp web is open, send a message in the active chat/ group.

#Importing Required libraries
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Moving the cursor to the text box
pyautogui.moveTo(960, 970) 

#Adding text to the box
click(960, 970)
pyautogui.write('Hello! My name is Pranav')

time.sleep(0.5)

#Moving the cursor to the send button
pyautogui.moveTo(1790, 970)
click(1790, 970)

#Moving the cursor to the center of the screen
pyautogui.moveTo(960, 540)


#Function to click on given co-ordinates
def click(x,y):
    win32api.SetCursorPos((2533,454))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
