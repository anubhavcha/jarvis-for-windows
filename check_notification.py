import dbus
import dbus.mainloop.glib
from gi.repository import GLib

# Create a DBus session bus
bus = dbus.SessionBus()

# Define a function to handle new notifications
def handle_notification(bus, message):
    # Get the notification data
    args = message.get_args_list()
    notification = {
        'app_name': args[0],
        'replaces_id': args[1],
        'app_icon': args[2],
        'summary': args[3],
        'body': args[4],
        'actions': args[5],
        'hints': args[6],
        'expire_timeout': args[7]
    }
        
    # Read the notification out loud
    print("New notification:")
    print(notification['summary'])
    print(notification['body'])

# Connect to the DBus session bus and listen for notifications
dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus.add_match_string("type='method_call',interface='org.freedesktop.Notifications',member='Notify'")
bus.add_message_filter(handle_notification)
GLib.MainLoop().run()
