
from gi.repository import GLib
import dbus
import dbus.service
from dbus.mainloop.glib import DBusGMainLoop


# currently not working as decorator changes the method name
#  it causes dbus to not recognize the method.
#  find a fix to print name of service method on invocation
def print_name_on_invoke(func):
    def wrapper(*args, **kwargs):
        print func.__name__
        return func(*args, **kwargs)
    return wrapper

