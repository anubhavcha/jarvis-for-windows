import time
from speak import speak
from listen import Listen
from playsound import playsound




def set_reminder(duration):

    unit = duration[-1]  
    print(duration)

    try:
        interval = int(duration[:-1]) 

    except ValueError:
        speak("Invalid time duration.")
        set_reminder(duration=Listen().lower())

    if unit == "h" :
        time.sleep(interval * 3600)

    elif unit == "m":
        time.sleep(interval * 60)

    elif unit == "s" :
        time.sleep(interval)

    else:
        speak("sir you are telling Invalid time unit. , try again")
        set_reminder(duration=Listen().lower())

    print(f"Time's up! {interval} {unit} has passed.")
    playsound("/home/zeno/Desktop/Jarvis/mp3(data)/Reminder (1).mp3")
    playsound("/home/zeno/Desktop/Jarvis/mp3(data)/Reminder.mp3")


    


