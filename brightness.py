import pyautogui
import keyboard

def decrease_brightness():
    pyautogui.press('f6')

def decrease_volume():
    pyautogui.press('volume_down')


# Keep the script running
# while True:
#     pass

decrease_brightness()
