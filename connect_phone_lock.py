import os
import time

# Set the path to the adb executable
adb_path = "C:\\platform-tools\\adb.exe"

# Connect to the device
os.system(f"{adb_path} connect 10.70.131.98")

# Unlock the phone
os.system(f"{adb_path} shell input keyevent 26")
time.sleep(1)
os.system(f"{adb_path} shell input swipe 300 1000 300 500")
time.sleep(1)
os.system(f"{adb_path} shell input text <unlock_pattern>")
time.sleep(1)
os.system(f"{adb_path} shell input keyevent 66")

# Disconnect from the device
os.system(f"{adb_path} disconnect 10.70.131.98")
