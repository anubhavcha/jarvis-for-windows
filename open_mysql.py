from openfunctions import open_terminal
import time
import pyautogui as gui

def open_MYSQL():
    open_terminal()
    time.sleep(1)
    gui.write('sudo su')
    # time.sleep(1)
    gui.press('enter')
    # time.sleep(1)
    gui.write('ram')
    gui.press('enter')
    gui.write('service mysql start')
    gui.press('enter') 
    time.sleep(1)
    gui.write('mysql')
    gui.press('enter')
    time.sleep(1)
    gui.write('use mysql')
    gui.press('enter')


