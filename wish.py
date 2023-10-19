import datetime
from datetime import date
from speak import speak
from playsound import playsound

today = date.today()
formatted_date = today.strftime("%d %b %Y")


now = datetime.datetime.now()

def wish():
    if now.hour == 7:
        playsound('/home/mr_zenox/Desktop/Jarvis/mp3(data)/Jarvis Morning.mp3')

    elif now.hour <12:
        speak("Good morning sir ")
        


    elif now.hour < 16:
        speak("Good afternoon sir ")
        

    else:
        speak("Good evening sir ")


def greating():
    if now.hour <12:
        speak("Good morning sir ")
        


    elif now.hour < 16:
        speak("Good afternoon sir ")
        

    else:
        speak("Good evening sir ")