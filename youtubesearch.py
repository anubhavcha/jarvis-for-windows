import speech_recognition as sr
import webbrowser
from speak import speak

r = sr.Recognizer()

def listen_and_searchyt():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        r.non_speaking_duration = 1.5
        audio = r.listen(source, 0, 5)

        try:
            text = r.recognize_google(audio)
            speak(f"ok searching {text} on youtube")
            speak(f"here is the top result on youtube search {text}")
            webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            speak(f"here is the top result on youtube search {text}")
           

        except:
            print("Sorry, I could not understand you.")

