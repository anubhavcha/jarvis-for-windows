import datetime
from speak import speak

def check_time():
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    time_str = "{:02d}:{:02d}".format(hour, minute)
    speak("The time is: " + time_str)

