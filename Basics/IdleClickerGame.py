#url : https://particle-clicker.web.cern.ch/

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
while True:
    pyautogui.moveTo(800,570)
    click(800, 570)
def click(x,y):
    win32api.SetCursorPos((2533,454))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
