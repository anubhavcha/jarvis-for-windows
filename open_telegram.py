import pyautogui as gui
import time
from speak import speak
def open_telegram():
    gui.press('winleft')
    time.sleep(1)
    gui.write('telegram')
    time.sleep(1)  
    gui.press('enter') 
    speak('cheack screen sir') 