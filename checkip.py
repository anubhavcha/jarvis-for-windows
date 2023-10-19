from openfunctions import open_terminal
from speak import speak
import pyautogui as gui
import time

def check_ip_using_wifi():
    speak("checking start")
    open_terminal()
    time.sleep(1)
    gui.write('sudo su')
    time.sleep(1)
    gui.press('enter')
    gui.write('ram')
    gui.press('enter')
    gui.write('netdiscover')
    gui.press('enter')

    speak('sir, there are some ip i am displaying to change and use')



