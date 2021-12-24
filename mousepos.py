from pynput.mouse import Button, Controller as MouseController
import time

mouse = MouseController()
time.sleep(3)
print("The mouse position is {0}".format(mouse.position))
