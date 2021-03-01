#Send text in Whatsappp web
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
n = int(input("Number of times to spam : "))
for i in range(0, n):
    pyautogui.moveTo(960, 970) 

    click(960, 970)
    pyautogui.write('lol')

    pyautogui.moveTo(1790, 970)
    click(1790, 970)

    #pyautogui.moveTo(960, 540)    # Moves to center, not needed in spammer. Use to reduce time if wanted


def click(x,y):
    win32api.SetCursorPos((2533,454))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
