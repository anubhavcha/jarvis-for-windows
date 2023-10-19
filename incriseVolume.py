from openfunctions import open_terminal
from listen import Listen
from speak import speak
import pyautogui as gui
import time

def increase_volume():
    speak("please tell me what should i fix the volume persentage")
    volume_persentage = int(Listen().lower())
    open_terminal()
    time.sleep(1)
    gui.write(f'pactl set-sink-volume @DEFAULT_SINK@ {volume_persentage}%')
    gui.press('enter')
    speak('increase volume function done')
    


