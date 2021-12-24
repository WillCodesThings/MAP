from pynput.keyboard import Key, Controller as KeyboardController
from pynput.keyboard import Listener
from pynput.mouse import Button, Controller as MouseController
from pynput import keyboard
import time
import pyautogui as pt
import threading

press = KeyboardController()
mouse = MouseController()

# determine func
def dertimine(image, off_x=0, off_y=0):
    position = pt.locateCenterOnScreen(image, confidence=0.7)
    if position is None:
        print(f"{image} not found...")
    else:
        pt.moveTo(position, duration=0.1)
        pt.moveRel(off_x, off_y)
        press.press(Button.left)


timesrun = 0


def move(action="walking"):
    if action == "walking":
        print("walking...")
        press.press("w")
    elif action == "running":
        print("running")
        press.press("w")
        press.release("w")
        press.press("w")
    elif action == "mining":
        global timesrun
        print("Mining...")
        mouse.press(Button.left)
        press.press("w")
        time.sleep(0.1)
        timesrun += 1
        if timesrun == 30:
            print("Checking if lava")
            mouse.release(Button.left)
            press.release("w")
            press.press("s")
            time.sleep(2)
            press.release("s")
            mouse.move(150, 200)
            mouse.press(Button.right)
            mouse.release(Button.right)
            mouse.move(-150, -200)
            timesrun = 0
    elif action == "lava":
        print("found lava...")
        print("Trying to escape...")
        mouse.release(Button.left)
        press.release("w")
        press.press("s")
        press.press(Key.space)
        mouse.press(Button.right)
        press.press("2")
        press.release("2")
        time.sleep(3)
        mouse.release(Button.right)
        time.sleep(7)
        press.release("s")
        press.release(Key.space)
        press.press("1")
        press.release("1")
        mouse.move(50, 251)
        mouse.press(Button.left)
        time.sleep(3)
        mouse.release(Button.left)
        mouse.move(-50, -251)


def find_lava():
    position = pt.locateCenterOnScreen("images/lava1.png", confidence=0.4)
    if position == None:
        return False
    else:
        return True


duration = 300
print("What would you like to do?")
print("1 |  Auto-Mine")
print("2 | WIP Auto-Sprint(With hole detection)")
print("3 | WIP TAS")
choice = input("")
if choice == "1":
    print("Starting in 5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Running")
    while duration != 0:

        if find_lava() == False:
            move("mining")
        else:
            move("lava")
        duration -= 1
