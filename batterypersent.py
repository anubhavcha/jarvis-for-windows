import psutil
import time
from playsound import playsound
from speak import speak

def battery_alert():
    while True:
     battery = psutil.sensors_battery()
     percent = int(battery.percent)

     if percent < 30 :
        playsound("mp3(data)/JARVIS Low Battery.mp3")

     elif percent < 10:
        playsound("/home/mr_zenox/Desktop/Jarvis/mp3(data)/Low Battery Jarvis.mp3")   

     elif percent == 100:
        playsound("/home/mr_zenox/Desktop/Jarvis/mp3(data)/Jarvis Overload.mp3")  

     else:
        pass

     time.sleep(60)  


def battey_persentage():
   battery = psutil.sensors_battery()
   percent = int(battery.percent)

   speak(f"the device is running on {percent}% battery power")

 