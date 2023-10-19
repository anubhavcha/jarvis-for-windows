import psutil
from playsound import playsound
from speak import speak


def plug_check():
    prev_status = None  # Initialize prev_status variable
    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        status = battery.power_plugged
        if prev_status is not None and status != prev_status:  # Check if the status has changed
            if status:
                print("Charger plugged in.")
                playsound("/home/mr_zenox/Desktop/Jarvis/mp3(data)/Programming Complete.mp3")
                speak(" charging start ")
            else:
                print("Charger unplugged.")
                playsound('/home/mr_zenox/Desktop/Jarvis/mp3(data)/Data Transfer.mp3')
                speak(" charging stoped ")
                
        prev_status = status  # Update prev_status variable
        


