from openfunctions import open_terminal
import pyautogui as gui
import time

def update_pc():
    open_terminal()
    gui.write("sudo su")
    gui.press("enter")
    gui.write("ram")
    gui.press("enter")
    gui.write("apt update")
    gui.press("enter")
    time.sleep(8)
    gui.write('y')
    gui.press('enter')

