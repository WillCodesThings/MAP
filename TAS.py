from pynput.keyboard import Key, Controller as KeyboardController
from pynput.keyboard import Listener
from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard
import time
import pyautogui as pt
import threading

keybd = KeyboardController()
mouse = MouseController()
time.sleep(3)
mouse.move(299, 445)
