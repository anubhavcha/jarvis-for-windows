import pyautogui as gui
import time
from speak import speak

def open_chrome():
    gui.press('winleft')
    time.sleep(1)
    gui.write('chrome')
    time.sleep(1)
    gui.press('enter')
    speak('done sir')


def open_code():
    gui.press('activities')  # Press the Windows key
    time.sleep(1)
    gui.write('vscode')
    time.sleep(1) 
    gui.press('enter')
    speak('now you can start sir')
    gui.hotkey("win")  # Press Windows key + left arrow key


# def open_code():
#     gui.press('winleft')
#     time.sleep(1)
#     gui.write('vscode')
#     time.sleep(1) 
#     gui.press('enter')
#     speak('now you can start sir')
#     gui.hotkey('winleft','upper arrow')

def open_terminal():
    gui.press('Super_L')
    time.sleep(1)
    gui.write('terminal')
    time.sleep(1)  
    gui.press('enter')    
    speak('open operation done')

def open_whatsapp():
    gui.press('winleft')
    time.sleep(1)
    gui.write('whatsapp')
    time.sleep(1)  
    gui.press('enter') 
    speak('exicution done sir')

def open_insta():
    gui.press('winleft')
    time.sleep(1)
    gui.write('instagram')
    time.sleep(1)  
    gui.press('enter') 
    speak('here you go')    

def open_googledrive():
    gui.press('winleft')
    gui.write('drive')
    time.sleep(1)
    gui.press('enter')
    speak('ok got it')

def open_rootTerminal():
    gui.press('winleft')
    time.sleep(1)
    gui.write('root')
    time.sleep(1)
    gui.press('enter')
    time.sleep(1)
    gui.write('ram')
    gui.press('enter')
    speak('sir,you can start now')

