import webbrowser
from speak import speak

def open_youtube():
    url = "https://www.youtube.com"
    speak("opening..")
    webbrowser.open(url)
    speak("done sir")
    