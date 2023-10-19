import datetime
import time
import os


def set_alarm(alarm_time):
    """Function to set an alarm at the specified time."""
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Alarm triggered.")
            break
