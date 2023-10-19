import notify2
import time

notify2.init("WhatsApp Notification Checker")

while True:
    # Get server information
    server_info = notify2.get_server_info()
    # Get active notifications
    notifications = server_info.get("notifications", [])
    # Check for new WhatsApp notifications
    for notification in notifications:
        if "whatsapp" in notification.get("summary", "").lower():
            print("New WhatsApp notification!")
    # Wait for 10 seconds before checking for new notifications again
    time.sleep(10)
