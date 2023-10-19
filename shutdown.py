import pyautogui as gui
import time

def shutdown():
    gui.hotkey('ctrl', 'alt', 'delete')
    time.sleep(1)
    gui.press('tab')
    time.sleep(1)
    gui.press('enter')

def reboot():
    gui.press('winleft')
    time.sleep(1)
    gui.write('reboot')
    time.sleep(1)
    gui.press('enter')
    time.sleep(1)
    gui.press('tab')
    time.sleep(1)
    gui.press('enter')
