import webbrowser
import time
import pyautogui as gui
from speak import speak
from listen import Listen

def map(location):
    # speak("sir ! tell me the location you want to see in map")
    webbrowser.open("https://www.google.com/maps/@16.3524328,79.8664982,16196013m/data=!3m1!1e3")
    time.sleep(3)
    gui.write(location)
    speak("searching.")
    gui.press("enter")
    speak(f"here is the reselt of {location} in google map")






map("satna madhya pradesh")